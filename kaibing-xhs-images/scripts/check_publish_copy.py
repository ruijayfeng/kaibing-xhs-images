#!/usr/bin/env python3
"""Check common standalone production labels in outline publish copy.

This checks Text Content, not image pixels. A necessary reader disclosure can
be recorded explicitly with Reader Disclosure and Disclosure Reason fields.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

LABEL = r"(?:概念示意|概念示例|非工具实测|非效果测评|本文未制作或测试视频|任务选择建议[，,]非效果测评)"
PRODUCTION_LINE = re.compile(rf"^{LABEL}(?:[，,、；; /]+{LABEL})*[。.!！]?$")
PAGE = re.compile(r"^## Image (\d+) of (\d+)\s*$", re.M)
COPY = re.compile(r"^\*\*Text Content\*\*:[ \t]*\n(.*?)(?=^\*\*[^\n]+\*\*:|^---\s*$|\Z)", re.M | re.S)


def field(page: str, name: str) -> str:
    match = re.search(rf"^\*\*{name}\*\*:[ \t]*(.*?)\s*$", page, re.M)
    return match[1].strip() if match else ""


def copy_line(line: str) -> str:
    line = re.sub(r"^\s*(?:[-+*]|\d+[.)])\s+", "", line).strip()
    line = re.sub(r"^(?:Title|Subtitle|Note|Caption|标题|副标题|注释)\s*[:：]\s*", "", line, flags=re.I)
    return line.replace("**", "").strip(" `\"'「」“”")


def check_publish_copy(outline: str) -> list[str]:
    headings = list(PAGE.finditer(outline))
    if not headings:
        return ["outline has no Image pages"]
    errors = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(outline)
        page = outline[heading.end():end]
        content = COPY.search(page)
        if not content or not content[1].strip():
            errors.append(f"page {heading[1]} missing Text Content")
            continue
        disclosure = copy_line(field(page, "Reader Disclosure"))
        reason = field(page, "Disclosure Reason")
        for line in content[1].splitlines():
            value = copy_line(line)
            if PRODUCTION_LINE.fullmatch(value) and not (value == disclosure and reason):
                errors.append(f"page {heading[1]} production label in publish copy: {value}; "
                              "keep metadata in Evidence Status, or record a necessary reader disclosure and its reason")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("outline", type=Path)
    args = parser.parse_args()
    try:
        errors = check_publish_copy(args.outline.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        errors = [str(exc)]
    for error in errors:
        print("ERROR", error)
    print(f"checked publish copy: {len(errors)} error(s)")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
