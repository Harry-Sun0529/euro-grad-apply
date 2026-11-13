import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
INJECTOR_PATH = REPO / "skills" / "euro-cv" / "assets" / "cv_inject.py"
TEMPLATE_PATH = REPO / "skills" / "euro-cv" / "assets" / "cv-template.html"

spec = importlib.util.spec_from_file_location("cv_inject", INJECTOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"无法加载 {INJECTOR_PATH}")
cv_inject = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cv_inject
spec.loader.exec_module(cv_inject)


class CvInjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = TEMPLATE_PATH.read_text(encoding="utf-8")

    def test_serialize_round_trips_special_text_without_html_entities(self):
        data = {
            "meta": {"cv_id": "synthetic-special"},
            "name": "A < B & C > D",
            "contact": ["a\"b", "c'd", "中文 🎓"],
            "sections": [
                {
                    "title": "Security",
                    "entries": [
                        {
                            "title": "Synthetic test",
                            "meta": "2026",
                            "sub": "",
                            "bullets": [
                                "</script><img src=x onerror=alert(1)>",
                                "line\\with\\slashes",
                                "U+2028:  and U+2029: ",
                            ],
                        }
                    ],
                }
            ],
        }

        encoded = cv_inject.serialize_payload(data)
        self.assertNotIn("</script", encoded.lower())
        self.assertNotIn("&lt;", encoded)
        self.assertIn("\\u003c", encoded)
        self.assertIn("\\u0026", encoded)
        self.assertEqual(json.loads(encoded), data)

    def test_inject_template_preserves_user_text_and_only_replaces_payload(self):
        data = {
            "meta": {"cv_id": "synthetic-render"},
            "name": "A < B",
            "contact": [],
            "sections": [
                {
                    "title": "Test",
                    "entries": [
                        {
                            "title": "Entry",
                            "meta": "2026",
                            "sub": "",
                            "bullets": ["</script><img src=x>", "latency <50ms"],
                        }
                    ],
                }
            ],
        }

        result = cv_inject.inject_template(self.template, data)
        self.assertNotIn("</script><img", result.lower())
        payload = cv_inject._extract_payload(result)
        self.assertEqual(json.loads(payload), data)

    def test_rejects_bad_placeholder_count(self):
        data = {"meta": {"cv_id": "synthetic"}}
        with self.assertRaises(cv_inject.InjectionError):
            cv_inject.inject_template(self.template.replace(cv_inject.PLACEHOLDER, "", 1), data)
        with self.assertRaises(cv_inject.InjectionError):
            cv_inject.inject_template(
                self.template.replace(cv_inject.PLACEHOLDER, cv_inject.PLACEHOLDER + cv_inject.PLACEHOLDER),
                data,
            )

    def test_rejects_non_object_payload(self):
        with self.assertRaises(cv_inject.InjectionError):
            cv_inject.serialize_payload(["not", "an", "object"])

    def test_rejects_malformed_template(self):
        data = {"meta": {"cv_id": "synthetic"}}
        with self.assertRaises(cv_inject.InjectionError):
            cv_inject.inject_template("<html></html>", data)

    def _valid_data(self):
        return {
            "meta": {"cv_id": "synthetic", "photo": "off"},
            "name": "Synthetic Person",
            "contact": ["a@example.com"],
            "sections": [
                {"title": "Education", "entries": [
                    {"title": "Uni", "meta": "2021–2025", "sub": "B.Eng.", "bullets": ["one"]}
                ]},
                {"title": "Skills", "entries": [{"title": "", "bullets": ["Python"]}]},
            ],
        }

    def test_validate_accepts_documented_schema(self):
        cv_inject.validate_cv_data(self._valid_data())

    def test_validate_rejects_misspelled_keys_and_wrong_types(self):
        cases = {
            "entries 写成 items": lambda d: d["sections"][0].update(
                items=d["sections"][0].pop("entries")),
            "entry 用了 date": lambda d: d["sections"][0]["entries"][0].update(date="2021"),
            "contact 是字符串": lambda d: d.update(contact="a@example.com"),
            "bullets 是字符串": lambda d: d["sections"][0]["entries"][0].update(bullets="one"),
            "缺 cv_id": lambda d: d["meta"].pop("cv_id"),
            "缺 name": lambda d: d.pop("name"),
            "sections 为空": lambda d: d.update(sections=[]),
            "photo 非法": lambda d: d["meta"].update(photo="yes"),
        }
        for label, mutate in cases.items():
            data = self._valid_data()
            mutate(data)
            with self.subTest(label), self.assertRaises(cv_inject.InjectionError):
                cv_inject.validate_cv_data(data)

    def test_file_injection_rejects_invalid_schema_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            data_path = directory_path / "data.json"
            output_path = directory_path / "cv.html"
            bad = self._valid_data()
            bad["sections"][0]["items"] = bad["sections"][0].pop("entries")
            data_path.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaises(cv_inject.InjectionError):
                cv_inject.inject_files(TEMPLATE_PATH, data_path, output_path)
            self.assertFalse(output_path.exists())

    def test_template_binds_editing_once_and_saves_edit_state(self):
        # 重复绑定会让粘贴插入多遍；保存不带编辑状态会在重新打开时丢修改。
        self.assertEqual(self.template.count("bindEditing();"), 1)
        self.assertIn("cv-saved", self.template)
        self.assertIn("buildSavedHTML()", self.template)

    def test_file_injection_refuses_overwrite_and_cleans_up_on_failure(self):
        data = self._valid_data()
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            template_path = directory_path / "template.html"
            data_path = directory_path / "data.json"
            output_path = directory_path / "cv.html"
            template_path.write_text(self.template, encoding="utf-8")
            data_path.write_text(json.dumps(data), encoding="utf-8")
            output_path.write_text("existing", encoding="utf-8")

            with self.assertRaises(cv_inject.InjectionError):
                cv_inject.inject_files(template_path, data_path, output_path)
            self.assertEqual(output_path.read_text(encoding="utf-8"), "existing")

            broken_template = directory_path / "broken.html"
            broken_template.write_text("broken", encoding="utf-8")
            missing_output = directory_path / "missing.html"
            with self.assertRaises(cv_inject.InjectionError):
                cv_inject.inject_files(broken_template, data_path, missing_output)
            self.assertFalse(missing_output.exists())
            self.assertEqual(list(directory_path.glob(".missing.html.*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
