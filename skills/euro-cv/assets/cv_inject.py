#!/usr/bin/env python3
"""Safely inject a CV JSON payload into the bundled HTML template.

The payload lives in a ``script[type="application/json"]`` raw-text element.
JSON Unicode escapes keep user text such as ``</script>`` from terminating that
raw-text element before the browser can parse it.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any


PLACEHOLDER = '{"__placeholder__":true}'
DATA_OPEN = '<script type="application/json" id="cv-data">'
DATA_CLOSE = "</script>"
BACKSLASH = chr(92)


class InjectionError(ValueError):
    """Raised when a template or payload cannot be safely injected."""


def serialize_payload(data: Any) -> str:
    """Serialize a CV object for safe placement in an HTML script data block."""
    if not isinstance(data, dict):
        raise InjectionError("CV 数据顶层必须是 JSON 对象")

    try:
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    except (TypeError, ValueError) as exc:
        raise InjectionError(f"CV 数据无法序列化为 JSON: {exc}") from exc

    # These characters are harmless in ordinary JSON but must not form markup
    # while the browser is tokenizing the script element's raw-text contents.
    replacements = {
        "<": BACKSLASH + "u003c",
        ">": BACKSLASH + "u003e",
        "&": BACKSLASH + "u0026",
        chr(0x2028): BACKSLASH + "u2028",
        chr(0x2029): BACKSLASH + "u2029",
    }
    return "".join(replacements.get(char, char) for char in payload)


def _extract_payload(html: str) -> str:
    # The bundled template mentions the opening tag in its HTML comment too;
    # the final occurrence is the actual data element.
    start = html.rfind(DATA_OPEN)
    if start == -1:
        raise InjectionError('模板缺少 `<script type="application/json" id="cv-data">` 数据块')
    payload_start = start + len(DATA_OPEN)
    end = html.find(DATA_CLOSE, payload_start)
    if end == -1:
        raise InjectionError("模板的数据块缺少 </script> 结束标签")
    return html[payload_start:end]


def inject_template(template_text: str, data: dict[str, Any]) -> str:
    """Return template text with one verified, safely encoded payload."""
    if template_text.count(PLACEHOLDER) != 1:
        raise InjectionError(
            f"模板占位符必须恰好出现 1 次，实际为 {template_text.count(PLACEHOLDER)} 次"
        )
    if DATA_OPEN not in template_text or DATA_CLOSE not in template_text:
        raise InjectionError("模板缺少可识别的 cv-data JSON 数据块")

    encoded = serialize_payload(data)
    result = template_text.replace(PLACEHOLDER, encoded, 1)
    payload = _extract_payload(result)

    if "</script" in payload.lower():
        raise InjectionError("安全检查失败：JSON 数据块仍包含 </script 序列")
    try:
        round_tripped = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise InjectionError(f"注入后的 JSON 无法解析: {exc}") from exc
    if round_tripped != data:
        raise InjectionError("注入后的 JSON 与输入数据不一致")

    return result


def inject_files(
    template_path: Path,
    data_path: Path,
    output_path: Path,
    *,
    overwrite: bool = False,
) -> None:
    """Inject a JSON file into a template and atomically write the HTML file."""
    if output_path.exists() and not overwrite:
        raise InjectionError(
            f"输出文件已存在：{output_path}。请换文件名，或显式使用 --overwrite。"
        )

    try:
        template_text = template_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise InjectionError(f"无法读取模板 {template_path}: {exc}") from exc
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InjectionError(f"无法读取或解析 JSON 数据 {data_path}: {exc}") from exc

    result = inject_template(template_text, data)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    temporary_path: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_path = temporary.name
            temporary.write(result)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_path, output_path)
        temporary_path = None
    except OSError as exc:
        raise InjectionError(f"无法安全写入输出文件 {output_path}: {exc}") from exc
    finally:
        if temporary_path is not None:
            try:
                os.unlink(temporary_path)
            except OSError:
                pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="将普通 JSON CV 数据安全注入 euro-cv HTML 模板"
    )
    parser.add_argument("--template", type=Path, required=True, help="HTML 模板路径")
    parser.add_argument("--data", type=Path, required=True, help="普通 JSON 数据路径")
    parser.add_argument("--output", type=Path, required=True, help="输出 HTML 路径")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="允许覆盖已有输出文件；默认拒绝静默覆盖",
    )
    args = parser.parse_args(argv)

    try:
        inject_files(
            args.template,
            args.data,
            args.output,
            overwrite=args.overwrite,
        )
    except InjectionError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
