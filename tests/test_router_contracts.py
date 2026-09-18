import re
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"


def read_skill(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


def frontmatter_description(text: str) -> str:
    end = text.find("\n---", 3)
    if not text.startswith("---") or end == -1:
        raise AssertionError("skill 缺少 frontmatter")
    body = text[3:end]
    lines = body.splitlines()
    description = []
    collecting = False
    for line in lines:
        if line.startswith("description:"):
            collecting = True
            description.append(line.split(":", 1)[1].strip())
        elif collecting and line.startswith(" "):
            description.append(line.strip())
        elif collecting:
            break
    return " ".join(description)


class RouterContractTests(unittest.TestCase):
    def test_main_skill_is_a_router_for_all_six_scene_skills(self):
        main = read_skill("euro-grad-apply")
        for command in (
            "/euro-school",
            "/euro-docs",
            "/euro-cv",
            "/euro-phd",
            "/euro-apply",
            "/euro-visa",
        ):
            self.assertIn(command, main)
        self.assertRegex(main, r"(?i)无命令|没有.*命令|网页版.*reference")
        self.assertRegex(main, r"(?i)slash command|显式.*命令|场景路由")

    def test_each_skill_description_has_an_english_discovery_anchor(self):
        anchors = {
            "euro-grad-apply": ("European", "graduate"),
            "euro-school": ("school selection", "which country"),
            "euro-docs": ("motivation letter", "statement of purpose"),
            "euro-cv": ("make me a CV", "tailor my CV"),
            "euro-phd": ("PhD application", "contacting supervisors"),
            "euro-apply": ("how to apply", "application portal"),
            "euro-visa": ("visa after offer", "arrival checklist"),
        }
        for name, expected_anchors in anchors.items():
            description = frontmatter_description(read_skill(name))
            self.assertTrue(
                any(anchor.lower() in description.lower() for anchor in expected_anchors),
                f"{name} description 缺少英文发现锚点: {expected_anchors}",
            )

    def test_cv_consultation_and_cv_delivery_are_separate_branches(self):
        cv_description = frontmatter_description(read_skill("euro-cv"))
        docs = read_skill("euro-docs")
        docs_description = frontmatter_description(docs)

        self.assertNotIn("简历要放照片吗", cv_description)
        self.assertNotIn("CV 怎么导出 PDF", cv_description)
        self.assertTrue(
            "简历要放照片吗" in docs_description or "照片" in docs_description
        )
        self.assertTrue(
            "CV 怎么导出 PDF" in docs_description or "导出 PDF" in docs_description
        )
        self.assertIn("/euro-cv", docs)
        self.assertIn("cv-standards.md", docs)

    def test_main_description_yields_to_scene_skills(self):
        main_description = frontmatter_description(read_skill("euro-grad-apply"))
        handoff_markers = (
            "优先交给",
            "让位",
            "单一场景",
            "对应命令",
        )
        self.assertTrue(
            any(marker in main_description for marker in handoff_markers),
            "主 skill description 没有声明单一场景向子 skill 让位",
        )

        exclusive_terms = (
            "帮我做简历",
            "Uni-assist 怎么填",
            "怎么套磁",
            "拿到 offer 了下一步",
        )
        for term in exclusive_terms:
            self.assertNotIn(term, main_description)

    def test_visa_has_long_term_identity_boundary(self):
        visa = read_skill("euro-visa")
        self.assertIn("permanent-residence-and-citizenship.md", visa)
        self.assertRegex(visa, r"以.*移民局官网为准")
        self.assertRegex(visa, r"长期身份.*规划|规划.*长期身份")

    def test_main_skill_states_ireland_scope_and_kaust_comparison_boundary(self):
        main = read_skill("euro-grad-apply")
        self.assertIn("爱尔兰", main)
        self.assertRegex(main, r"(?i)对照|非主覆盖|不在.*范围")
        self.assertIn("KAUST", main)
        self.assertRegex(main, r"(?i)欧洲.*KAUST|KAUST.*欧洲|同时出现|明确比较")

    def test_router_examples_cover_the_high_risk_ties(self):
        main = read_skill("euro-grad-apply")
        expected_pairs = (
            ("帮我做/生成/定制 CV", "/euro-cv"),
            ("德国还是荷兰", "/euro-school"),
            ("Uni-assist 怎么填", "/euro-apply"),
            ("读博/套磁", "/euro-phd"),
            ("拿到 offer", "/euro-visa"),
        )
        for phrase, command in expected_pairs:
            self.assertIn(phrase, main, f"缺少路由示例: {phrase}")
            self.assertIn(command, main, f"路由示例未指向 {command}")


if __name__ == "__main__":
    unittest.main()
