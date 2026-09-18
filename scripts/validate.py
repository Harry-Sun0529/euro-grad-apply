#!/usr/bin/env python3
"""
仓库结构校验——防止插件 manifest 漂移、reference 引用断链、合并文件过期。

用法：
    python3 scripts/validate.py

收集所有失败后一次性报错退出（不是遇到第一个就停），方便一轮修完。
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAIN_SKILL = REPO / "skills" / "euro-grad-apply"
REFS_DIR = MAIN_SKILL / "references"
# ⚠️ 约定：所有 reference 只放在 euro-grad-apply/references/ 这一处。
#    场景 skill（euro-cv 等）不建自己的 references/——下面第 5 项把每个
#    references/xxx.md 引用都拿这个硬编码路径去查，别处同名文件会误报"引用不存在"。
MERGED = REPO / "euro-grad-apply-full.md"
README = REPO / "README.md"
PLUGIN_JSONS = [
    REPO / ".claude-plugin" / "plugin.json",
    REPO / ".codex-plugin" / "plugin.json",
    REPO / ".workbuddy-plugin" / "plugin.json",
]
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
EXPECTED_NAME = "euro-grad-apply"
REQUIRED_FIELDS = ["name", "version", "description", "author", "license", "homepage", "repository"]

errors: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def load_json(path: Path):
    if not path.exists():
        fail(f"文件缺失: {path.relative_to(REPO)}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"JSON 解析失败 {path.relative_to(REPO)}: {e}")
        return None


def parse_frontmatter(text: str) -> dict | None:
    """极简 YAML frontmatter 解析——只取顶层 key，够用且无需第三方依赖。"""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    body = text[3:end]
    out: dict[str, str] = {}
    key = None
    for line in body.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([a-zA-Z_][\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            out[key] = m.group(2).strip()
        elif key and line.startswith((" ", "\t")):
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


# ---------- 1. 三份 plugin.json 可解析、字段齐全 ----------
plugins = [load_json(p) for p in PLUGIN_JSONS]
for path, data in zip(PLUGIN_JSONS, plugins):
    if data is None:
        continue
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        fail(f"{path.relative_to(REPO)} 缺字段: {missing}")
    if data.get("name") != EXPECTED_NAME:
        fail(f"{path.relative_to(REPO)} 的 name 应为 {EXPECTED_NAME}，实为 {data.get('name')!r}")
if all(p is not None for p in plugins):
    notes.append(f"三份 plugin.json 字段完整，name = {EXPECTED_NAME}")

# ---------- 2. 三份 plugin.json 内容完全相等 ----------
valid = [p for p in plugins if p is not None]
if len(valid) == 3:
    if not (valid[0] == valid[1] == valid[2]):
        fail("三份 plugin.json 内容不一致——改了一份忘了同步其他两份？"
             "（应改 .claude-plugin/plugin.json 后 cp 到另外两处）")
    else:
        notes.append("三份 plugin.json 逐字相同")

# ---------- 3. version 四处一致 ----------
mk = load_json(MARKETPLACE)
if mk is not None and valid:
    if not mk.get("plugins"):
        fail("marketplace.json 的 plugins 为空")
    else:
        entry = mk["plugins"][0]
        versions = {str(p.get("version")) for p in valid} | {str(entry.get("version"))}
        if len(versions) != 1:
            fail(f"version 不一致: {sorted(versions)}（3 份 plugin.json + marketplace 必须同版本）")
        else:
            notes.append(f"version 四处一致: {versions.pop()}")
        if entry.get("name") != EXPECTED_NAME:
            fail(f"marketplace plugins[0].name 应为 {EXPECTED_NAME}，实为 {entry.get('name')!r}")
        src = REPO / entry.get("source", "./")
        if not (src / "skills").is_dir():
            fail(f"marketplace source {entry.get('source')!r} 下找不到 skills/ 目录")

# ---------- 4. 每个 skill 的 frontmatter ----------
skill_dirs = sorted(d for d in (REPO / "skills").iterdir() if d.is_dir()) if (REPO / "skills").is_dir() else []
if not skill_dirs:
    fail("skills/ 下没有任何 skill 目录")
skill_texts: dict[Path, str] = {}
for d in skill_dirs:
    sf = d / "SKILL.md"
    if not sf.exists():
        fail(f"{d.relative_to(REPO)} 下缺 SKILL.md")
        continue
    text = sf.read_text(encoding="utf-8")
    skill_texts[sf] = text
    fm = parse_frontmatter(text)
    if fm is None:
        fail(f"{sf.relative_to(REPO)} 没有可解析的 frontmatter")
        continue
    if fm.get("name") != d.name:
        fail(f"{sf.relative_to(REPO)} 的 name={fm.get('name')!r} 与目录名 {d.name!r} 不一致")
    if not fm.get("description"):
        fail(f"{sf.relative_to(REPO)} 的 description 为空")
if skill_texts and not errors:
    notes.append(f"{len(skill_texts)} 个 SKILL.md 的 frontmatter 合法且 name 与目录名一致")

# ---------- 5. references 引用存在性 ----------
ref_pattern = re.compile(r"(?:\.\./euro-grad-apply/)?references/([A-Za-z0-9._-]+\.md)")
referenced: set[str] = set()
for sf, text in skill_texts.items():
    for fname in ref_pattern.findall(text):
        referenced.add(fname)
        if not (REFS_DIR / fname).exists():
            fail(f"{sf.relative_to(REPO)} 引用了不存在的 references/{fname}")
if referenced and not errors:
    notes.append(f"{len(referenced)} 个 reference 引用全部命中")

# ---------- 6. 反向孤儿检查 ----------
if REFS_DIR.is_dir():
    on_disk = {p.name for p in REFS_DIR.glob("*.md")}
    orphans = sorted(on_disk - referenced)
    if orphans:
        fail(f"孤儿 reference（没有任何 SKILL.md 提到，AI 永远读不到）: {orphans}")
    else:
        notes.append(f"{len(on_disk)} 个 reference 均被至少一个 SKILL.md 引用，无孤儿")

# ---------- 6. 反向孤儿检查 ----------
if REFS_DIR.is_dir():
    on_disk = {p.name for p in REFS_DIR.glob("*.md")}
    orphans = sorted(on_disk - referenced)
    if orphans:
        fail(f"孤儿 reference（没有任何 SKILL.md 提到，AI 永远读不到）: {orphans}")
    else:
        notes.append(f"{len(on_disk)} 个 reference 均被至少一个 SKILL.md 引用，无孤儿")

# ---------- 6b. 主 router 覆盖检查 ----------
main_text = skill_texts.get(MAIN_SKILL / "SKILL.md", "")
scene_commands = (
    "/euro-school",
    "/euro-docs",
    "/euro-cv",
    "/euro-phd",
    "/euro-apply",
    "/euro-visa",
)
missing_commands = [command for command in scene_commands if command not in main_text]
if missing_commands:
    fail(f"主 skill router 缺少场景命令: {missing_commands}")
else:
    notes.append("主 skill router 覆盖 6 个场景命令")

missing_from_main = sorted(
    fname for fname in (REFS_DIR.glob("*.md") if REFS_DIR.is_dir() else [])
    if fname.name not in main_text
)
if missing_from_main:
    fail(f"主 skill 兜底路由缺少 reference: {missing_from_main}")
else:
    notes.append("主 skill 兜底路由覆盖全部 reference")

if not re.search(r"(?i)无命令|网页版.*reference|不具备文件读写", main_text):
    fail("主 skill 缺少无命令环境的网页版降级声明")

# ---------- 6c. 显式章节锚点检查 ----------
anchor_pattern = re.compile(
    r"(?:\.\./euro-grad-apply/)?references/([A-Za-z0-9._-]+\.md)[^\n]*?§(\d+(?:\.\d+)?)"
)
for sf, text in skill_texts.items():
    for fname, section in anchor_pattern.findall(text):
        target = REFS_DIR / fname
        if not target.exists():
            continue
        headings = target.read_text(encoding="utf-8").splitlines()
        section_pattern = re.compile(rf"^{'#' * (section.count('.') + 2)}\s+{re.escape(section)}(?:[.：:、\s]|$)")
        if not any(section_pattern.search(line) for line in headings):
            fail(f"{sf.relative_to(REPO)} 引用 {fname} §{section}，但目标章节不存在")
if not any("§" in text for text in skill_texts.values()):
    notes.append("未发现显式章节锚点")
else:
    notes.append("显式章节锚点检查完成")

# ---------- 6d. README 快照字段检查 ----------
snapshot_text = README.read_text(encoding="utf-8") if README.exists() else ""
snapshot_match = re.search(
    r"内容快照\*\*：(20\d\d)-(\d\d)\s+·\s+\*\*下次复审\*\*：(20\d\d)-(\d\d)",
    snapshot_text,
)
if snapshot_match is None:
    fail("README 缺少可解析的内容快照/下次复审字段")
else:
    sy, sm, ry, rm = (int(value) for value in snapshot_match.groups())
    if not (1 <= sm <= 12 and 1 <= rm <= 12):
        fail("README 快照月份非法")
    months = (ry - sy) * 12 + rm - sm
    if not (0 < months <= 6):
        fail(f"README 快照与下次复审间隔应为 1-6 个月，实际为 {months} 个月")
    else:
        notes.append(f"README 快照字段合法（{sy:04d}-{sm:02d} → {ry:04d}-{rm:02d}）")

# ---------- 7. 合并文件新鲜度 ----------
build_sh = REPO / "scripts" / "build-merged.sh"
if not build_sh.exists():
    fail("scripts/build-merged.sh 缺失")
elif not MERGED.exists():
    fail("euro-grad-apply-full.md 缺失")
else:
    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        r = subprocess.run(["bash", str(build_sh), str(tmp_path)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            fail(f"build-merged.sh 执行失败: {r.stderr.strip()}")
        elif tmp_path.read_text(encoding="utf-8") != MERGED.read_text(encoding="utf-8"):
            fail("euro-grad-apply-full.md 已过期——源文件改了但合并文件没重新生成。"
                 "跑 `bash scripts/build-merged.sh` 修复。")
        else:
            notes.append("合并单文件与源文件同步")
    finally:
        tmp_path.unlink(missing_ok=True)

# ---------- 8. 可执行资产完整性 ----------
# CV 模板和注入器是 /euro-cv 的核心可执行资产。它们被误删或改坏时，
# 用户侧的表现是"AI 说生成好了，双击打开是白屏"或无法安全生成文件。
CV_TEMPLATE = REPO / "skills" / "euro-cv" / "assets" / "cv-template.html"
CV_INJECTOR = REPO / "skills" / "euro-cv" / "assets" / "cv_inject.py"
if not CV_TEMPLATE.exists():
    fail(f"CV 模板缺失: {CV_TEMPLATE.relative_to(REPO)}（/euro-cv 将无法工作）")
else:
    tpl = CV_TEMPLATE.read_text(encoding="utf-8")
    tpl_errs = []
    if 'id="cv-data"' not in tpl:
        tpl_errs.append('缺少 id="cv-data" 数据块')
    n_ph = tpl.count('{"__placeholder__":true}')
    if n_ph != 1:
        tpl_errs.append(f'占位符 {{"__placeholder__":true}} 出现 {n_ph} 次（必须恰好 1 次，'
                        f'否则注入器会失败或替换错位置）')
    if not tpl.rstrip().endswith("</html>"):
        tpl_errs.append("文件未以 </html> 结尾（可能被截断）")
    if "http://" in tpl or "https://" in tpl.replace(
            "https://github.com/Harry-Sun0529/euro-grad-apply", ""):
        tpl_errs.append("含外部资源引用——模板必须自包含，否则用户断网时打不开")
    if tpl_errs:
        for e in tpl_errs:
            fail(f"CV 模板: {e}")
    else:
        notes.append(f"CV 模板完整（{len(tpl.splitlines())} 行，自包含无外链）")

if not CV_INJECTOR.exists():
    fail(f"CV 注入器缺失: {CV_INJECTOR.relative_to(REPO)}（/euro-cv 将无法安全生成）")
else:
    try:
        compile(CV_INJECTOR.read_text(encoding="utf-8"), str(CV_INJECTOR), "exec")
    except SyntaxError as e:
        fail(f"CV 注入器语法错误: {e}")
    else:
        notes.append("CV 注入器存在且可编译")

# ---------- 汇总 ----------
print("=" * 60)
for n in notes:
    print(f"  ✅ {n}")
if errors:
    print("=" * 60)
    print(f"\n❌ {len(errors)} 项校验失败：\n")
    for i, e in enumerate(errors, 1):
        print(f"  {i}. {e}")
    print()
    sys.exit(1)
print("=" * 60)
print("\n✅ 全部校验通过\n")
