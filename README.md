# Euro Grad Apply · 欧洲留学申请 Skill

> 📅 **内容快照日期**：2026-07 · **下次复审**：2027-01
>
> ⚠️ 政策、签证金额、奖学金额度、deadline 等具体数字**年年变化**——本仓库的所有具体数字均为方向性参考，做任何决定前**请到目标国官方网站二次核实**。本仓库已配置 GitHub Action 每月自动检查链接有效性 + 每半年自动提醒复审。

一个装进 AI 里的"欧洲留学顾问"。装好之后，AI 会根据你的背景（学校 / GPA / 专业 / 预算 / 毕业目标）给出针对性建议，而不是泛泛的"建议你去查官网吧"。

**零基础也能用**——不会命令行、没用过 GitHub 都没关系，看下面方法 1 或方法 2。

---

## 能帮你做什么

- **国家**：德国、荷兰、瑞典、挪威、丹麦、芬兰、瑞士、法国、意大利、西班牙、比利时、奥地利等
- **学科**：理工、商科、人文社科、艺术设计、建筑、医学等
- **全流程**：选国选校 → 文书 → 申请系统操作 → 奖学金 → 签证 → 落地 → 永居入籍
- **中国学生专属**：APS 审核、CSSD 学信网认证、**回国留服认证看院系归属**、CSC 公派、意大利预注册
- **特别专题**：毕业目标导向择校（回国 / 留欧 / 兼顾 / 跳板）、GAP year 与工作后申请、跨专业申请、保底校策略

装成插件后还有 5 个快捷命令，见[下面的表格](#5-个命令)。

---

## 🚀 三种启动方式

### 方法 1：临时试用（30 秒，什么都不装）

1. 点开仓库里你最关心的文件（如 [`skills/euro-grad-apply/SKILL.md`](skills/euro-grad-apply/SKILL.md)）
2. 点右上角 **"Copy raw file"** 复制全文
3. 粘贴给任何 AI（Kimi / 豆包 / Claude / ChatGPT / DeepSeek），加一句"请把这份内容当作你的知识库，我要问欧洲留学问题"

<img width="338" alt="copy raw file" src="https://github.com/user-attachments/assets/9c707de8-beb2-4e0a-b667-a1585da58603" />

> 缺点：每开新对话都要重新贴。

---

### 方法 2：装进 AI 的"智能体"，永久带着 ⭐ 推荐给非技术用户

装一次，之后每次对话自动带着全部内容，不用再粘贴。

**① 下载**：仓库首页绿色 **`Code`** 按钮 → `Download ZIP` → 解压（跟下载普通压缩包一样，不用命令行）

<img width="846" alt="download zip" src="https://github.com/user-attachments/assets/317d8dd9-0557-4b73-a11c-bb87aeafa48d" />

**② 找到你 AI 的"智能体"功能**（各家叫法不同，但都是同一个东西）：

| AI | 功能名 | 费用 |
|---|---|---|
| Kimi / 豆包 / 通义 / 智谱 | 智能体 | 免费 |
| Claude / ChatGPT / Gemini | Projects / GPT / Gems | 需订阅 |

**③ 创建智能体 → 找到"知识库 / 文件"上传入口 → 把 `skills/euro-grad-apply/` 里的所有 `.md` 文件拖进去 → 保存**

之后进这个智能体直接问就行。

> 📌 **如果你的 AI 限制知识库文件数量 / 上传文件太多太麻烦**：
> 不用传全部文件——直接下载单文件 **[`euro-grad-apply-full.md`](euro-grad-apply-full.md)**（已把所有内容合并成一个），只传这一个即可。

---

### 方法 3：装成插件（4 个平台）

装成插件后可以用 `/euro-school` 这样的斜杠命令，且能一键更新。

#### Claude Code

```
/plugin marketplace add Harry-Sun0529/euro-grad-apply
/plugin install euro-grad-apply@harry-skills
```

之后直接问欧洲留学问题即可自动触发。更新：`/plugin marketplace update harry-skills`

#### Codex

把这个仓库链接发给 Codex，说一句"帮我安装这个 skill"：

```
https://github.com/Harry-Sun0529/euro-grad-apply
```

装好后用 `/euro-school`、`$euro-phd` 等调用。

#### DeepSeek Harness

**A. 命令行**（可 `git pull` 更新）

```bash
git clone --depth 1 https://github.com/Harry-Sun0529/euro-grad-apply.git ~/euro-grad-apply-src
mkdir -p 你的项目目录/.dsh/skills
cp -r ~/euro-grad-apply-src/skills/* 你的项目目录/.dsh/skills/
```

`.dsh/skills/` 只在该项目生效；想全局生效改用 `.agents/skills/`。拷完**重启 DSH 或开新会话**才会被扫描到。

**B. 图形界面**（不用命令行）

1. `Code` → `Download ZIP` → 解压
2. DSH 打开 **Settings → Skills → 导入**
3. 选"导入文件夹"，选中解压目录里的 `skills/euro-grad-apply` **这个子文件夹**（不是最外层目录）
4. 保存后重启

#### WorkBuddy

**A. 命令行**

```bash
git clone --depth 1 https://github.com/Harry-Sun0529/euro-grad-apply.git ~/euro-grad-apply-src
mkdir -p ~/.workbuddy/skills
cp -r ~/euro-grad-apply-src/skills/* ~/.workbuddy/skills/
```

**重启 WorkBuddy** 后生效。

**B. 不用命令行**

1. `Code` → `Download ZIP` → 解压
2. 打开 `~/.workbuddy/skills` 目录：
   - **macOS**：Finder 按 `Cmd+Shift+G`，输入 `~/.workbuddy/skills` 回车
   - **Windows**：地址栏输入 `%USERPROFILE%\.workbuddy\skills`
   - 目录不存在就手动建一个 `skills` 文件夹
3. 把解压目录里 `skills/` 下的所有文件夹拖进去
4. 重启 WorkBuddy

装完应该长这样：

```
~/.workbuddy/skills/euro-grad-apply/SKILL.md
~/.workbuddy/skills/euro-school/SKILL.md
...
```

---

## 5 个命令

装成插件后可用。不装也没关系——直接问问题，AI 会自动判断该看哪部分内容。

| 命令 | 什么时候用 | 举例 |
|---|---|---|
| `/euro-school` | 选国选校 | "我这个背景能申什么学校""德国还是荷兰" |
| `/euro-docs` | 写文书 | "动机信怎么写""CV 怎么改" |
| `/euro-phd` | 申博士 | "怎么套磁""博士有工资吗" |
| `/euro-apply` | 走申请流程 | "Uni-assist 怎么填""APS 怎么办" |
| `/euro-visa` | 拿到 offer 之后 | "签证怎么办""资金证明""落地做什么" |

---

## 🧭 出发前自检清单

在和 AI 详细对话前，先用这 6 个问题给自己定位。**把答案一次性告诉 AI，比来回追问效率高 10 倍**：

1. **目标**：读硕还是读博？毕业后回国 / 留欧 / 兼顾 / 跳板他国？
2. **专业与学位**：想申什么专业？**学位证书上的名称有要求吗？**
   （跨专业、交叉学科申请者尤其重要——回国留服认证看**学位授予院系**，不看你研究什么。同样做艺术治疗，挂心理系认心理学类，挂艺术学院认艺术类）
3. **背景**：本科学校层次（985/211/双非/中外合办）+ GPA + 专业 + 工作经验（如有）
4. **预算**：每年可承受总开销（学费 + 生活费）约多少？
5. **语言**：英语水平（雅思/托福分数或自评）+ 是否愿意学当地语言到 B1+？
6. **时间**：希望何时入学？还有多少时间准备？

---

## 怎么提问最有效

直接说**你的背景 + 你的问题**。

**🟢 好的开场**
- "我是 985 计算机本科，GPA 88/100，雅思还没考，想申德国或荷兰 CS 硕士，毕业后倾向留在欧洲。给我做个规划。"
- "211 经管本科，GPA 84，工作了 2 年做数据分析，想跨申商业分析或数据科学。预算 30 万人民币。"
- "我已经拿到了 TU Delft 和 ETH 的 offer，怎么选？"

**🔴 不太好的开场**
- "去欧洲留学好吗？" → 太宽泛，AI 只能给百度搜索式答案
- "推荐学校" → 缺背景，AI 只能给通用列表

**💡 小技巧**
- 一次问一个清晰的问题，不要堆砌
- 答案不满意就直接说"再具体些""我想要表格对比"
- AI 给的所有具体数字（学费、截止日期、QS 排名）**最终都要去官网二次核实**

---

## 文件结构

```
euro-grad-apply/
├── skills/
│   ├── euro-grad-apply/                    # 主 skill（自然语言触发）
│   │   ├── SKILL.md
│   │   └── references/                     # 26 个专题文件
│   │       ├── germany.md                  # 各国指南
│   │       ├── netherlands.md
│   │       ├── career-goals.md             # 毕业目标导向择校
│   │       ├── china-specific-procedures.md # APS / CSSD / 留服认证
│   │       ├── phd-guide.md                # 博士申请
│   │       ├── post-offer-checklist.md     # offer 后到落地
│   │       └── ...
│   ├── euro-school/                        # /euro-school 选国选校
│   ├── euro-docs/                          # /euro-docs   文书
│   ├── euro-phd/                           # /euro-phd    博士套磁
│   ├── euro-apply/                         # /euro-apply  申请系统
│   └── euro-visa/                          # /euro-visa   签证行前
├── euro-grad-apply-full.md                 # 全部内容合并单文件（自动生成）
├── .claude-plugin/                         # Claude Code 插件清单
├── .codex-plugin/                          # Codex 插件清单
├── .workbuddy-plugin/                      # WorkBuddy 插件清单
└── README.md
```

---

## 数据来源

- 各大学及机构官网（英文 / 当地语言）
- 官方政策文件与新闻报道
- 中文留学社区公开讨论（小红书、知乎、一亩三分地、豆瓣、Reddit 等）
- 跨平台综合，提取对中国学生有用的信息

---

## DIY 还是找中介？

**DIY 完全可行**——所有申请流程的官方信息都是公开的。中介的核心定位是"帮你按模板批量处理流程"，适合：
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
- 不对申请结果做任何保证
- 本仓库为公开知识库，欢迎 fork 和提 issue 完善

> **v1.0.0 迁移提示**：skill 已移到 `skills/euro-grad-apply/`。之前 `git clone` 到 `~/.claude/skills/` 的用户请改用上面方法 3 的 `/plugin` 安装方式。

## License

[MIT](LICENSE)
