---
name: euro-cv
description: >
  为某个具体项目生成定制版欧洲学术 CV，产出可在浏览器里直接编辑的单文件 HTML。
  当用户输入 /euro-cv，或说"帮我做简历"、"生成 CV"、"针对 XX 项目改简历"、
  "CV 排版"、"简历要放照片吗"、"CV 怎么导出 PDF"时触发。
---

## 这个命令做什么

产出一份**针对某一个具体项目**定制的 CV 文件：双击用浏览器打开，点任意文字就能改，Ctrl+P 导出 PDF。零安装零依赖。

内容只重组用户给的真实经历——**不编造任何数字、成果或经历**。

## 环境前置

需要能读写文件的环境（Claude Code / Codex / DSH / WorkBuddy）。

- 无文件读写能力 → 说明本命令不可用，转 `/euro-docs` 走方法学路径
- 开始前先确认模板存在：`<插件目录>/skills/euro-cv/assets/cv-template.html`
- **模板找不到时绝不凭记忆重写一个**——那会产出一个与仓库不一致、样式退化的影子模板，用户无从察觉。正确做法是报错 + 给出 GitHub raw 链接让用户手动下载 + 建议重装插件

## 必问清单（先问再答，一次最多 3 个）

1. **目标学校 + 具体项目全名**（⚠️ 必问，没有它整个定制无从谈起）
2. **学位类型**：授课型硕士 / 研究型硕士 / 博士 —— 决定探查深度和 CV 结构（见 cv-standards.md §2）
3. **有没有现成材料**：旧 CV、一段自述、成绩单信息都行，**中文即可**，不用先翻译

---

## 工作流程（四阶段，每阶段有停止点）

### 阶段 A · 探查目标项目

web search 官网主页 + 课程列表。研究型硕士 / 博士**追加**教授研究方向——**在同一轮搜索里一起查**，不要分两次。

**必须输出确认卡片，然后停下等用户确认：**

- 官方页面链接（让用户能自己点开核对）
- 关键信息摘要：学位全称、学制、核心方向、必修课、提取出的 5–10 个关键词
- ⚠️ **明确列出"没查到"的项**——宁可留白也不猜。用户无法区分"AI 查过确认没有"和"AI 压根没查"，不说出来就等于默认查过了
- 若搜到往年录取偏好类信息（论坛帖、录取案例），**标注"这是社区传闻，不是官方要求"**（理由见 cv-standards.md §8）

❌ **未经用户确认不得进入阶段 B。**

**降级**：无法联网时，请用户贴项目页面文本；用户也拿不到时，产出"未定制通用版"并**在交付说明里明确标注未做项目定制**。

### 阶段 B · 收集与核对经历

- 已有 `./euro-cv/my-experience.json` → 读取，**只问增量**
- 没有 → 按 cv-standards.md §1 的 section 清单**逐项对照**，列出"你缺这几项"
- **主动指出缺口**，尤其 bullet 缺可核实结果时**回头问用户**："这个项目你处理了多少数据？/ 优化后提升了多少？"
- 用户答不出数字 → 按 cv-standards.md §3.3 三档退让（数字 > 具体规模 > 具体方法与产出）

❌ **硬约束**：
- 不编造用户没提过的项目、成果、数字
- **成品里绝不留 `[X%]` / `[TODO]` / `[待补充]` 占位符**——宁可用第三档表述
- 每条 bullet 都要能追溯到用户原话

写入 / 更新 `./euro-cv/my-experience.json`（覆盖前先 `cp` 成 `.bak`）。

### 阶段 C · 生成

1. 按阶段 A 的关键词**重排序**（最相关的放最显眼位置）、**改写 bullet**、**统一术语**（项目用 "statistical learning" 就别写 "机器学习"）
2. 照片：按目标国查 cv-standards.md §4 预设 `meta.photo`，德奥瑞南欧默认 `"on"`，英荷北欧默认 `"off"`，并说明这是惯例非硬性要求
3. **生成动作 = 普通 JSON + 内置注入器**：
   ```text
   把最终数据先写成普通 JSON：./euro-cv/cv-<school>-<program>.json
   调用随本 skill 分发的注入器：
   python3 <插件目录>/skills/euro-cv/assets/cv_inject.py \
     --template <插件目录>/skills/euro-cv/assets/cv-template.html \
     --data ./euro-cv/cv-<school>-<program>.json \
     --output ./euro-cv/cv-<school>-<program>.html
   ```
   注入器直接读取插件内的只读模板并写出新成品，不需要先把模板复制到目标路径；这样不会在检查同名文件前覆盖用户已有成品。生成前仍要先 `ls euro-cv/`，同名的既有成品必须先询问用户覆盖还是改用 `-v2`；用户明确选择覆盖时才额外传 `--overwrite`。
   ⚠️ **绝不要自己重写整个 HTML 文件，也不要直接 Edit `<script>` 数据块**——CSS/JS 经过模型输出通道容易发生转录漂移，手写转义也无法稳定防住 `</script>`。必须让随 skill 分发的 `assets/cv_inject.py` 负责 JSON 序列化、raw-text 安全编码、占位符校验和原子写入。注入器失败就停止，不退回不安全的直接替换；`cp` 让模板字节永不过模型。

**交付话术必须包含：**
- 文件的完整路径
- 双击用浏览器打开（**建议 Chrome / Edge**）
- 点任意文字即可修改，改动自动保存
- **Ctrl+P 时记得勾选「背景图形」**，否则标题的蓝色线条不会打印
- 导出前看一眼打印预览，确认没有哪段经历被切到两页上

### 阶段 D · 多版本复用

- **换项目 = 重跑 A + C，跳过 B**（经历是稳定的，变的只是排序和术语）
- 用户在浏览器里改过内容 → 让他点工具栏「⬆️ 导出 JSON」贴回来，同步进 `my-experience.json`。不做这步，下次生成会基于过时数据
- 文件名 `cv-<school>-<program>.html`；**生成前先 `ls euro-cv/`，同名存在时问用户覆盖还是存 `-v2`，绝不静默覆盖**
- 在 `my-experience.json` 的 `_targets` 里记一笔（学校、项目、文件名、日期）

---

## JSON 数据格式

注入模板的数据结构（模板只认这个）：

```json
{
  "meta": {
    "cv_id": "tum-informatics-2026",
    "doc_title": "Zhang_Ming_CV_TUM_Informatics",
    "target": "TUM · M.Sc. Informatics",
    "photo": "off"
  },
  "name": "Zhang Ming",
  "contact": ["email", "phone", "city", "github.com/xxx"],
  "sections": [
    {"title": "Education", "entries": [
      {"title": "机构名", "meta": "2021–2025", "sub": "学位 · GPA 3.7/4.0 (Top 8%)",
       "bullets": ["..."]}
    ]}
  ]
}
```

- `cv_id` **必须每份 CV 唯一**——它是浏览器草稿的命名空间 key，重复会导致两份 CV 的编辑内容互相覆盖
- `doc_title` 会成为浏览器标题和 Ctrl+P 的默认文件名，用 `Lastname_Firstname_CV_School` 格式
- Skills 类 section 用空 `title` + 纯 `bullets` 即可

### 数据注入安全规则

1. 普通经历数据先写入独立 JSON 文件，再交给 `assets/cv_inject.py` 注入模板；不要直接 Edit `<script type="application/json" id="cv-data">` 数据块
2. 不把 `<` 改成 `&lt;`，也不要在模型输出中手写最终的 `\\u003c`；注入器会用 JSON Unicode escape 保护 `<`、`>`、`&`，浏览器解析后仍还原为原文
3. 用户文本中出现 `</script>`、HTML 标签样式文本、引号、反斜杠、中文或 emoji 时，仍走同一注入器流程；注入器失败就停止，不使用不安全的直接替换 fallback
4. 普通 JSON 里不出现裸换行；多行内容拆成数组元素
5. 中文、emoji、全角标点直接写，不转义（模板是 UTF-8，已实测无乱码）

---

## 读哪些资料

- `../euro-grad-apply/references/cv-standards.md` — section 清单、bullet 规范、各国照片惯例（**主要依据**）
- `../euro-grad-apply/references/materials-guide.md` — 其他文书如何与 CV 呼应
- `../euro-grad-apply/references/china-specific-procedures.md` — GPA 与学历表述
- `../euro-grad-apply/references/phd-guide.md` — 博士 CV 的 Publications 权重
- `../euro-grad-apply/references/cross-discipline.md` — 跨专业经历的排序叙事

## 边界

- **只重组，不创作**：每一条都必须能追溯到用户原话
- 阶段 A 的探查结果**未经用户确认不生成**
- 官方页面没写的课程 / 教授 / 要求，宁可标"未查到"也不填补
- 往年偏好类信息一律标注"社区传闻"；它只能影响措辞和排序，**不得成为隐瞒真实经历的理由**
- 不做 LaTeX、不做真 PDF 生成、不做多套模板
- **照片让用户在浏览器里上传**（工具栏有按钮），不要试图把图片转成 base64 塞进 JSON
- 生成物含真实姓名、手机号、邮箱——**cwd 是 git 仓库时提示用户把 `euro-cv/` 加进 `.gitignore`**；若检测到 cwd 就是本插件仓库，**拒绝写入**并改问用户目标目录
