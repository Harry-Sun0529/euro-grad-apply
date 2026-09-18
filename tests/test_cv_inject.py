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

    def test_file_injection_refuses_overwrite_and_cleans_up_on_failure(self):
        data = {"meta": {"cv_id": "synthetic"}}
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
