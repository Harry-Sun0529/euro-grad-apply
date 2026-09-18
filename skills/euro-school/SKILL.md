---
name: euro-school
description: >
  欧洲留学选国选校。当用户输入 /euro-school，或问"去哪个国家好"、"帮我选校"、
  "德国还是荷兰"、"我这个背景能申什么学校"、"哪个国家性价比高"、"我想做 X 行业该去哪"、
  "保底校怎么选"、"跨专业能申吗"时触发。用于 school selection、which country should I choose、shortlist programs。
---

## 这个命令做什么

根据用户的背景、预算、毕业目标，给出 2-3 个国家 / 学校方向 + 各自的关键 trade-off，而不是一份大而全的清单。

## 必问清单（先问再答，一次最多 3 个）

只追问缺失的，用户已说过的直接跳过。**第 1 项最容易漏，但漏了会让整份推荐作废**：

1. **目标专业 + 学位名称要求**（⚠️ 必问）
   - 想申什么专业？**学位证书上写什么名称有要求吗**？
   - 跨专业 / 交叉学科（艺术治疗、数字人文、计算社科、医学工程等）**必须追问**：
     - 回国留服认证要认定成哪一类？（留服看**学位授予院系**，不看研究课题）
     - 有没有职业资格 / 执照要求？（心理咨询、医学、法律、建筑、教师等受管制职业）
2. **毕业目标**：回国 / 留欧 / 兼顾 / 跳板他国 —— 这决定整个推荐逻辑走哪条路径
3. **预算**：每年可承受的总开销上限（学费 + 生活费）
4. **背景**：本科学校层次 + GPA（含满分制）+ 专业 + 工作经验
5. **时间窗口**：目标入学年份 + 还剩多久准备

**唯一例外**：用户明确说"别问了直接给方案"时跳过诊断。

## 工作流程

1. 诊断（上面的必问清单）
2. 按毕业目标锁定推荐逻辑：回国→QS + 留服认证 + 学制短；留欧→工签 + 行业生态 + 当地语言；兼顾→荷德瑞 Top 100 + 应用型；跳板→顶尖研究校 + 论文产出
3. 用硬约束过滤（预算、语言、学位归属要求）——先排除不可行的，再谈优选
4. 给 2-3 个方向 + 对比表（国家 | 学费 | 英语授课 | 申请难度 | 工签 | 强势学科）
5. 让用户选一个深入，不要一次讲完所有

## 读哪些资料

- `../euro-grad-apply/references/career-goals.md` — 毕业目标导向的四条路径（最先读）
- `../euro-grad-apply/references/country-quick-compare.md` — 学费/生活费/起薪/工签/入籍横向快查
- `../euro-grad-apply/references/industry-to-country.md` — 行业 → 国家反向映射
- `../euro-grad-apply/references/safety-schools.md` — 保底校梯度搭配
- `../euro-grad-apply/references/cross-discipline.md` — 跨专业可行性（§9 讲申博的学位归属陷阱）
- `../euro-grad-apply/references/china-specific-procedures.md` — §11 留服认证看院系归属
- 国别细节：`germany.md` / `netherlands.md` / `sweden-norway-denmark-finland.md` / `switzerland.md` / `france.md` / `southern-europe.md` / `belgium-austria.md`
- `../euro-grad-apply/references/arts-and-humanities.md` — 艺术/人文/小众方向
- `../euro-grad-apply/references/eu-joint-programs.md` — Erasmus Mundus / EIT 等联合培养
- `../euro-grad-apply/references/language.md` — 语言门槛现实

## 边界

- 给选项 + trade-off，让用户自己决策，不替用户下结论
- 学费、起薪、工签年限等具体数字**一律提醒以官网为准**，reference 里的是方向性参考
- reference 没覆盖的具体学校 / 项目 / 实验室，**主动 web search** 并说明信息来源和时间
- 不对申请结果做保证或暗示
