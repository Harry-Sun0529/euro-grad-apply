import re
import unittest
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
README = REPO / "README.md"
MERGED = REPO / "euro-grad-apply-full.md"
REFS = REPO / "skills/euro-grad-apply/references"
SNAPSHOT_PATTERN = re.compile(
    r"内容快照\*\*：(?P<snapshot>20\d\d-\d\d)\s+·\s+\*\*下次复审\*\*：(?P<review>20\d\d-\d\d)"
)


class ReferenceAuditTests(unittest.TestCase):
    def test_readme_snapshot_has_valid_review_window(self):
        text = README.read_text(encoding="utf-8")
        match = SNAPSHOT_PATTERN.search(text)
        self.assertIsNotNone(match, "README 缺少内容快照/下次复审字段")
        snapshot = date.fromisoformat(f"{match['snapshot']}-01")
        review = date.fromisoformat(f"{match['review']}-01")
        months = (review.year - snapshot.year) * 12 + review.month - snapshot.month
        self.assertGreater(months, 0)
        self.assertLessEqual(months, 6)

    def test_references_do_not_contain_environment_delivery_promises(self):
        forbidden = (
            "双击",
            "浏览器里编辑",
            "Ctrl+P",
            "cv_inject",
            "生成 HTML",
            "生成HTML",
            "生成文件",
        )
        violations = []
        for path in sorted(REFS.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            for phrase in forbidden:
                if phrase in text:
                    violations.append(f"{path.name}: {phrase}")
        self.assertEqual(violations, [])

    def test_merged_file_exposes_router_degradation(self):
        merged = MERGED.read_text(encoding="utf-8")
        self.assertIn("网页版 AI 知识库", merged)
        self.assertIn("不提供 slash command", merged)
        self.assertIn("不具备文件读写能力", merged)
        self.assertIn("/euro-school", merged)
        self.assertIn("/euro-docs", merged)
        self.assertIn("/euro-cv", merged)
        self.assertIn("/euro-phd", merged)
        self.assertIn("/euro-apply", merged)
        self.assertIn("/euro-visa", merged)


if __name__ == "__main__":
    unittest.main()
