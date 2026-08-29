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
OUT="${1:-$REPO_ROOT/euro-grad-apply-full.md}"

{
  echo "# Euro Grad Apply · 全部内容合并版（单文件）"
  echo ""
  echo "> 本文件由所有 \`.md\` 自动合并生成，供有\"知识库文件数上限\"或不想逐个上传多文件的 AI 平台使用。"
  echo "> 只需上传这一个文件即可。**请勿手动编辑本文件**——它会在源文件更新时被自动覆盖。"
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
