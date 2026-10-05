#!/usr/bin/env python3
"""Exercise publish-copy preflight through its command-line interface."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("check_publish_copy.py")


def outline(copy: str, metadata: str = "") -> str:
    return ("## Image 1 of 1\n\n**Text Content**:\n" + copy +
            "\n\n**Visual Concept**: 白底插画\n**Evidence Status**: 概念示意\n" + metadata)


class PublishCopyTests(unittest.TestCase):
    def run_check(self, text: str) -> subprocess.CompletedProcess:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "outline.md"
            path.write_text(text, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], text=True, capture_output=True)

    def test_internal_label_blocks_generation_preflight(self) -> None:
        for copy in ("让 AI 换个讲法\n概念示意", "- Note: 概念示例",
                     "需要探索，就做交互页\n概念示意，非工具实测",
                     "动态过程，可以用视频讲\n本文未制作或测试视频。",
                     "按问题选择\n任务选择建议，非效果测评。"):
            with self.subTest(copy=copy):
                result = self.run_check(outline(copy))
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_metadata_and_actual_reader_content_stay_usable(self) -> None:
        result = self.run_check(outline("关系复杂，就画图\n用概念示意图解释关系。\n结果只适用于单人任务。\n中文写法（本文整理）"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_necessary_disclosure_is_explicit_and_explained(self) -> None:
        metadata = "**Reader Disclosure**: 概念示意\n**Disclosure Reason**: 教学界面需与真实截图区分\n"
        self.assertEqual(self.run_check(outline("界面教学\n概念示意", metadata)).returncode, 0)
        self.assertEqual(self.run_check(outline("界面教学\n概念示意", "**Reader Disclosure**: 概念示意\n")).returncode, 1)

    def test_malformed_input_fails_cleanly(self) -> None:
        result = self.run_check("# 没有逐页文案\n")
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
