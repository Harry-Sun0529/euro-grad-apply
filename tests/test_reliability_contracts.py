import json
import re
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


class ReliabilityContractTests(unittest.TestCase):
    def test_lychee_workflow_reads_step_output(self):
        workflow = (REPO / ".github/workflows/link-check.yml").read_text(encoding="utf-8")
        self.assertIn("id: lychee", workflow)
        self.assertIn("steps.lychee.outputs.exit_code", workflow)
        self.assertNotIn("env.lychee_exit_code", workflow)
        self.assertIn("fail: false", workflow)
        # lychee 0.24 移除了 --exclude-mail；带着它工具直接报错退出，什么都不查。
        self.assertNotIn("--exclude-mail", workflow)
        self.assertIn("test -s ./lychee-report.md", workflow)
        # --exclude-path 是正则，带 ./ 前缀时匹配不到，合并文件会被重复检查。
        self.assertIn("--exclude-path euro-grad-apply-full.md", workflow)
        self.assertNotIn("--exclude-path ./", workflow)

    def test_cv_injector_is_distributed_with_template(self):
        injector = REPO / "skills/euro-cv/assets/cv_inject.py"
        template = REPO / "skills/euro-cv/assets/cv-template.html"
        self.assertTrue(injector.is_file())
        self.assertTrue(template.is_file())
        self.assertEqual(template.read_text(encoding="utf-8").count('{"__placeholder__":true}'), 1)

    def test_merged_file_exposes_snapshot_and_web_boundaries(self):
        merged = (REPO / "euro-grad-apply-full.md").read_text(encoding="utf-8")
        self.assertRegex(merged, r"内容快照.*下次复审")
        self.assertIn("网页版 AI 知识库", merged)
        self.assertIn("不提供 slash command", merged)
        self.assertIn("不具备文件读写能力", merged)
        self.assertIn("/euro-cv", merged)

    def test_aps_copy_distinguishes_window_from_planning_buffer(self):
        apply_skill = (REPO / "skills/euro-apply/SKILL.md").read_text(encoding="utf-8")
        procedures = (
            REPO / "skills/euro-grad-apply/references/china-specific-procedures.md"
        ).read_text(encoding="utf-8")
        combined = apply_skill + procedures
        self.assertRegex(combined, r"8-12 周")
        self.assertRegex(combined, r"3-6 个月")
        self.assertIn("规划缓冲", combined)
        self.assertIn("官方", combined)
        self.assertIn("APS 官网", combined)

    def test_manifest_versions_are_valid_json_and_current(self):
        paths = [
            REPO / ".claude-plugin/plugin.json",
            REPO / ".codex-plugin/plugin.json",
            REPO / ".workbuddy-plugin/plugin.json",
            REPO / ".claude-plugin/marketplace.json",
        ]
        payloads = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
        plugin_versions = {payload["version"] for payload in payloads[:3]}
        marketplace_version = payloads[3]["plugins"][0]["version"]
        self.assertEqual(len(plugin_versions), 1)
        version = plugin_versions.pop()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(marketplace_version, version)


if __name__ == "__main__":
    unittest.main()
