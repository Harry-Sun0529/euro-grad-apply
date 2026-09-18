#!/usr/bin/env bash
# 把所有 skill 内容合并成单文件 euro-grad-apply-full.md
# 供有"知识库文件数上限"或不想逐个上传多文件的 AI 平台使用
#
# 用法：
#   bash scripts/build-merged.sh              # 写入仓库根目录的 euro-grad-apply-full.md
#   bash scripts/build-merged.sh /tmp/out.md  # 写入指定路径（validate 用来做新鲜度 diff）
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$REPO_ROOT/skills/euro-grad-apply"
README="$REPO_ROOT/README.md"
OUT="${1:-$REPO_ROOT/euro-grad-apply-full.md}"

SNAPSHOT_LINE="$(grep -m1 -E '^> .*内容快照.*下次复审.*$' "$README" || true)"
if [[ -z "$SNAPSHOT_LINE" ]]; then
  echo "错误：README.md 缺少可解析的内容快照/下次复审行" >&2
  exit 1
fi

{
  echo "# Euro Grad Apply · 全部内容合并版（单文件）"
  echo ""
  echo "$SNAPSHOT_LINE"
  echo "> 本文件是给网页版 AI 知识库 / Projects 上传的单文件版本。它包含主 skill 与 references，不提供 slash command，也不具备文件读写能力。"
  echo "> 需要生成可编辑 \`/euro-cv\` HTML 成品或使用场景命令时，请安装完整插件；本文件由源文件自动合并生成，**请勿手动编辑**。"
  echo ""
  echo "> 源仓库：https://github.com/Harry-Sun0529/euro-grad-apply"
  echo ""
  echo "---"
  echo ""
  cat "$SKILL_DIR/SKILL.md"
  echo ""
  for f in $(ls "$SKILL_DIR"/references/*.md | sort); do
    echo ""
    echo "---"
    echo ""
    echo "<!-- ===== 来源文件: references/$(basename "$f") ===== -->"
    echo ""
    cat "$f"
    echo ""
  done
} > "$OUT"

echo "生成完成: $OUT ($(wc -l < "$OUT") 行, $(wc -c < "$OUT") 字节)"
