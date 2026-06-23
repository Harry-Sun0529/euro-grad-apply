# Euro Grad Apply - 欧洲留学申请 Skill

## 这是什么 / 能帮你做什么

这是一个加载在 AI 助手上的"知识库 + 决策框架"。装上后，AI 会变成一位**精通欧洲留学申请的顾问**，能根据你的背景（学校 / GPA / 专业 / 预算 / 毕业目标）给出针对性建议，而不是泛泛的"建议你去查官网吧"。

它涵盖：

- **国家**：德国、荷兰、瑞典、挪威、丹麦、芬兰、瑞士、法国、意大利、西班牙、比利时、奥地利等
- **学科**：理工、商科、人文社科、艺术设计、建筑、医学等
- **流程**：选国选校、申请时间线、文书写作（CV / 动机信 / Research Proposal / 推荐信）、GPA 换算、语言要求、各国特殊流程（APS / CSSD 学信网 / Nuffic / Campus France / Universitaly / UA.se 等）、奖学金（CSC / DAAD / SI / Eiffel / Erasmus Mundus / EIT 等）、欧盟联合培养项目（EMJMD / EIT / N5T / EuroTech / CEMS / MSCA）、博士套磁、签证行前等等
- **特别专题**：毕业目标导向择校（回国 / 留欧 / 兼顾 / 跳板）、GAP year / 工作后申请、跨专业申请、保底校策略、中国学生特定流程，以及少量欧洲之外的对照备选（如 KAUST 全奖 STEM 研究型）

---

## 🚀 从零开始：5 分钟上手指南

### 如果你完全不熟悉 GitHub 和命令行

最简单的方法是**直接复制内容贴给 AI**：

#### 方法 A（最简单）：复制粘贴给 AI 用
1. 打开你常用的 AI 助手（Claude、ChatGPT、Gemini、Kimi、豆包、DeepSeek 等都行）
2. 在本仓库点开你最关心的文件（例如 `SKILL.md` 是核心，`references/germany.md` 是德国指南）
3. **点击文件页面右上角的 "Copy raw file" 按钮 / 或全选页面内容复制**
<img width="338" height="90" alt="image" src="https://github.com/user-attachments/assets/9c707de8-beb2-4e0a-b667-a1585da58603" />

5. 粘贴到 AI 对话框，加一句："请把这份内容作为你的知识库，然后我接下来问你欧洲留学的问题"
6. 开始问问题

#### 方法 B：下载整个仓库
1. 在本仓库首页点击绿色的 **"Code"** 按钮
2. 选 **"Download ZIP"**
3. 下载后解压，得到一个文件夹，里面是所有 `.md` 文件
4. 把文件夹拖入 AI 工具（如果你的 AI 支持上传文件夹/多文件，例如 Claude Desktop）
5. 或者把核心文件（`SKILL.md` + 你最关心的几个 `references/*.md`）一个一个粘贴
<img width="846" height="720" alt="image" src="https://github.com/user-attachments/assets/317d8dd9-0557-4b73-a11c-bb87aeafa48d" />


#### 方法 C（Claude Code 用户）
```bash
cd ~/.claude/skills/
git clone https://github.com/Harry-Sun0529/euro-grad-apply.git
```
之后 Claude Code 会自动识别 skill，正常对话即可。

---

### 开始第一次对话：怎么提问最有效

直接说**你的背景 + 你的问题**，AI 会顺着你的情况回答。

#### 🟢 好的开场举例
- "我是 985 计算机本科，GPA 88/100，雅思还没考，想申德国或荷兰 CS 硕士，毕业后倾向留在欧洲。给我做个规划。"
- "211 经管本科，GPA 84，工作了 2 年做数据分析，想跨申商业分析或数据科学。预算 30 万人民币。"
- "双非英语专业，GPA 86，考研失败了想去欧洲读人文社科硕士。回国就业为主。"
- "我已经拿到了 TU Delft 和 ETH 的 offer，怎么选？"

#### 🔴 不太好的开场举例
- "去欧洲留学好吗？" → 太宽泛，AI 给出的是百度搜索式答案
- "推荐学校" → 缺背景，AI 只能给通用列表

#### 💡 互动 tips
- 一次问一个清晰的问题，不要堆砌
- 答案不满意 → 直接说"再具体些"、"我想要表格对比"、"我背景是 X，这个推荐适合吗？"
- AI 给的所有具体数字（学费、截止日期、QS 排名）**最终都要去官网二次核实**——政策每年变化

---

### 你能问什么类型的问题（举例）

#### 选国选校
- "我想申 CS，德国 / 荷兰 / 瑞典对我来说哪个更合适？"
- "ETH 和 TU Delft 怎么对比？"
- "我 GPA 不高（82），有哪些欧洲名校还有机会？"
- "我想毕业回国进体制，哪些学校落户友好？"

#### 申请流程
- "APS 是什么？什么时候开始准备？"
- "CSSD 学信网认证怎么办？"
- "我已经毕业 2 年了，怎么解释 GAP？"
- "怎么跨专业申请数据科学？"

#### 文书 / 套磁
- "Motivation Letter 怎么写？给我一个框架"
- "怎么找博士导师套磁？给我邮件模板"
- "推荐信找谁写？怎么催推荐人？"

#### 奖学金
- "CSC 和 DAAD 能同时申吗？"
- "Erasmus Mundus 全奖竞争多激烈？"
- "免学费 + 高奖学金的组合有哪些？"

#### 时间线
- "我大三下学期开始准备来得及吗？"
- "2026 秋入学的关键时间节点是什么？"

#### 中国学生特定问题
- "Nuffic Certificate 现在还需要吗？"
- "意大利预注册流程是什么？"
- "瑞典 UA.se 怎么传成绩单？"

---

## 数据来源

- 各大学及机构官网（英文/当地语言）
- 官方政策文件与新闻报道
- 中文留学社区公开讨论（小红书、知乎、一亩三分地、豆瓣等）
- 跨平台综合，提取对中国学生有用的信息

---

## 🧭 出发前自检清单（5 分钟自问自答）

在和 AI 详细对话前，先用这 5 个问题快速给自己定位：

1. **目标**：你想读硕 / 博？毕业后回国 / 留欧 / 兼顾 / 跳板？
2. **背景**：本科学校层次（985/211/双非/中外合办）+ GPA + 专业 + 工作经验（如有）
3. **预算**：每年可承受总开销（学费 + 生活费）约多少？
4. **语言**：英语水平（雅思/托福分数或自评）+ 是否愿意学当地语言到 B1+？
5. **时间**：希望何时入学？还有多少时间做申请准备？

把答案准备好，开场就把这些信息一次性告诉 AI——比反复来回追问效率高 10 倍。

---

## 文件结构

```
SKILL.md                                    # 主技能文件（必读，AI 入口）
references/
├── germany.md                              # 德国
├── netherlands.md                          # 荷兰
├── sweden-norway-denmark-finland.md         # 北欧四国
├── switzerland.md                          # 瑞士
├── france.md                               # 法国
├── southern-europe.md                      # 意 / 西 / 葡
├── belgium-austria.md                      # 比利时 / 奥地利
├── eu-joint-programs.md                    # 欧盟联合培养（EMJMD/EIT/N5T/MSCA）
├── career-goals.md                         # 毕业目标导向择校
├── china-specific-procedures.md            # 中国学生特定流程（APS/CSSD/Campus France/Universitaly 等）
├── gap-and-work-experience.md              # GAP year / 工作后申请
├── cross-discipline.md                     # 跨专业申请
├── safety-schools.md                       # 保底校策略
├── language.md                             # 语言：英语现实 + 配偶途径 + 雅思托福 + 小语种 0 基础
├── permanent-residence-and-citizenship.md  # 永居 / 入籍路径
├── country-quick-compare.md                # 国家性价比快查表（学费/生活费/起薪/工签/入籍）
├── industry-to-country.md                  # 行业 → 国家反向映射（半导体/汽车/制药/金融/能源等）
├── application-systems.md                  # 申请系统操作（Uni-assist/Studielink/UA.se/EEF/Universitaly）
├── post-offer-checklist.md                 # 拿到 offer 后：决策 → 接受 → 签证 → 行前 → 落地
├── kaust.md                                # KAUST 沙特全奖 STEM（欧洲之外的对照备选）
├── scholarships.md                         # 奖学金大全
├── materials-guide.md                      # 文书写作
├── phd-guide.md                            # 博士申请
├── timeline.md                             # 时间线
├── chinese-info-sources.md                 # 中文信息源
└── arts-and-humanities.md                  # 艺术 / 人文类
```

---

## DIY 还是找中介？

**DIY 完全可行**——所有申请流程的官方信息都是公开的（学校官网、政府移民局、各校申请系统）。中介的核心定位是"帮你按模板批量处理流程"，适合：
- 完全不会英语、不会用电脑
- 时间极度紧张、宁愿花钱省事
- 需要中介的内推关系（少数项目有效）

中介**不适合**：
- 需要根据你个人情况定制路径（中介通常按模板批量处理）
- 想留欧长期发展（中介关心拉成生意，不关心你毕业后的事）
- 预算有限（中介费 3-10 万人民币，DIY 几乎免费）

如果你能用这个 skill + 各校官网搞清楚每一步，省下的中介费够你雅思考 5 次或者读半个学期。

---

## 注意事项

- 留学政策变化频繁，具体数字请以各校官网为准
- 不替代专业留学顾问的个性化服务
- 不对申请结果做任何保证
- 本仓库为公开知识库，欢迎 fork 和提 issue 完善
