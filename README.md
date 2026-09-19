# Euro Grad Apply · 欧洲留学申请 Skill

> 📅 **内容快照**：2026-09 · **下次复审**：2027-01
>
> ⚠️ 学费、签证金额、奖学金额度、deadline 这些数字**年年变**。本仓库的数字都是方向性参考，做决定前请到官网核实。

一个装进 AI 的"欧洲留学顾问"。装好之后，AI 会根据你的背景（学校 / GPA / 专业 / 预算 / 毕业目标）给针对性建议，而不是泛泛的"建议你去查官网吧"。

---

## 📦 安装

**在你的 AI 里执行对应命令即可。** 找到你用的那个平台，照着做：

### Claude Code

```
/plugin marketplace add Harry-Sun0529/euro-grad-apply
/plugin install euro-grad-apply@harry-skills
```

装完直接问问题。更新：`/plugin marketplace update harry-skills`

---

### Codex

把这行发给 Codex，说"帮我安装这个 skill"：

```
https://github.com/Harry-Sun0529/euro-grad-apply
```

---

### DeepSeek Harness

```bash
git clone --depth 1 https://github.com/Harry-Sun0529/euro-grad-apply.git ~/euro-src
mkdir -p ~/.agents/skills && cp -r ~/euro-src/skills/* ~/.agents/skills/
```

**重启 DSH** 生效。更新：`cd ~/euro-src && git pull && cp -r skills/* ~/.agents/skills/`

> 只想在某个项目里用？把 `~/.agents/skills` 换成 `你的项目/.dsh/skills`。

---

### WorkBuddy

```bash
git clone --depth 1 https://github.com/Harry-Sun0529/euro-grad-apply.git ~/euro-src
mkdir -p ~/.workbuddy/skills && cp -r ~/euro-src/skills/* ~/.workbuddy/skills/
```

**重启 WorkBuddy** 生效。

---

### 不会用命令行？

**方法 A：下载后拖文件夹**

1. 点仓库首页绿色 **`Code`** → `Download ZIP` → 解压

   <img width="600" alt="download zip" src="https://github.com/user-attachments/assets/317d8dd9-0557-4b73-a11c-bb87aeafa48d" />

2. 打开你 AI 的 skills 目录：
   - **WorkBuddy**：macOS 在 Finder 按 `Cmd+Shift+G` 输入 `~/.workbuddy/skills`；Windows 地址栏输入 `%USERPROFILE%\.workbuddy\skills`
   - **DSH**：Settings → Skills → 导入文件夹
3. 把解压后 `skills/` 里的 **7 个文件夹全部**拖进去
4. 重启

> ⚠️ 必须 7 个一起装。6 个斜杠命令的资料都存在 `euro-grad-apply/references/` 里，只装命令文件夹会读不到内容。

**方法 B：用 Kimi / 豆包 / ChatGPT 等网页版 AI**

这些平台没有插件系统，但可以传进"智能体 / Projects"当知识库：

1. 下载 **[`euro-grad-apply-full.md`](euro-grad-apply-full.md)**（所有内容合并成的单文件）
2. 在 AI 里创建智能体（Kimi/豆包/通义/智谱免费，ChatGPT/Claude/Gemini 需订阅）
3. 找到"知识库 / 文件"上传入口，传这一个文件
4. 保存，之后进这个智能体直接问

**方法 C：只想试一下**

打开 [`SKILL.md`](skills/euro-grad-apply/SKILL.md) → 点右上角 "Copy raw file" → 粘贴给任何 AI，加一句"请把这当作你的知识库"。

<img width="338" alt="copy raw file" src="https://github.com/user-attachments/assets/9c707de8-beb2-4e0a-b667-a1585da58603" />

---

## 🎯 装完能干什么

**直接问就行**，AI 会自动判断该看哪部分。装了插件的话还有 6 个快捷命令：

| 命令 | 什么时候用 | 举例 |
|---|---|---|
| `/euro-school` | 选国选校 | "我这背景能申什么学校""德国还是荷兰" |
| `/euro-docs` | 写文书 | "动机信怎么写""SoP 怎么改" |
| `/euro-cv` | 做简历 | "帮我做一份投 TUM 的 CV""简历该放照片吗" |
| `/euro-phd` | 申博士 | "怎么套磁""博士有工资吗" |
| `/euro-apply` | 走申请流程 | "Uni-assist 怎么填""APS 怎么办" |
| `/euro-visa` | 拿到 offer 后 | "签证怎么办""资金证明""落地做什么" |

**覆盖范围**

- **国家**：德国、荷兰、瑞典、挪威、丹麦、芬兰、瑞士、法国、意大利、西班牙、比利时、奥地利等
- **学科**：理工、商科、人文社科、艺术设计、建筑、医学
- **全流程**：选校 → 文书 → 申请系统 → 奖学金 → 签证 → 落地 → 永居入籍
- **中国学生专属**：APS 审核、CSSD 学信网认证、**回国留服认证看院系归属**、CSC 公派、意大利预注册
- **专题**：毕业目标导向择校（回国/留欧/兼顾/跳板）、GAP year 与工作后申请、跨专业申请、保底校策略

---

## 🧭 开始前先想清楚 6 件事

把答案一次性告诉 AI，比来回追问效率高 10 倍：

1. **目标**：读硕还是读博？毕业后回国 / 留欧 / 兼顾 / 跳板？
2. **专业与学位**：想申什么专业？**学位证书上的名称有要求吗？**
   （跨专业、交叉学科尤其重要——回国留服认证看**学位授予院系**，不看你研究什么。同样做艺术治疗，挂心理系认心理学类，挂艺术学院认艺术类）
3. **背景**：本科学校层次（985/211/双非/中外合办）+ GPA + 专业 + 工作经验
4. **预算**：每年可承受总开销（学费 + 生活费）
5. **语言**：雅思/托福分数（或自评）+ 是否愿意学当地语言到 B1+
6. **时间**：希望何时入学？还有多久准备？

---

## 💬 怎么问最有效

**🟢 好的开场**
- "985 计算机本科，GPA 88，雅思没考，想申德国或荷兰 CS 硕士，倾向留欧。给我做个规划。"
- "211 经管本科 GPA 84，工作 2 年做数据分析，想跨申商业分析。预算 30 万。"
- "我拿到了 TU Delft 和 ETH 的 offer，怎么选？"

**🔴 不太好的开场**
- "去欧洲留学好吗？" → 太宽泛，只能给百度式答案
- "推荐学校" → 缺背景，只能给通用列表

**💡 小技巧**：一次问一个问题；答案不满意就说"再具体些""要表格对比"；AI 给的所有数字最终都要去官网核实。

---

## 📁 文件结构

```
skills/
├── euro-grad-apply/            # 主 skill（必装）
│   ├── SKILL.md
│   └── references/             # 27 个专题文件
│       ├── germany.md          # 各国指南
│       ├── career-goals.md     # 毕业目标导向择校
│       ├── china-specific-procedures.md  # APS / CSSD / 留服认证
│       ├── phd-guide.md        # 博士申请
│       └── ...
├── euro-school/                # /euro-school
├── euro-docs/                  # /euro-docs
├── euro-cv/                    # /euro-cv（含 assets/cv-template.html）
├── euro-phd/                   # /euro-phd
├── euro-apply/                 # /euro-apply
└── euro-visa/                  # /euro-visa

euro-grad-apply-full.md         # 全部内容合并单文件（自动生成）
```

> 所有专题资料只放在 `euro-grad-apply/references/` 一处，场景 skill 不建自己的 `references/`。

---

## DIY 还是找中介？

**DIY 完全可行**——申请流程的官方信息都是公开的。中介的核心定位是"按模板批量处理流程"，适合完全不会英语、时间极紧、或需要特定内推关系的人。

但中介**不适合**：需要按个人情况定制路径的（他们按模板走）、想留欧长期发展的（他们不关心你毕业后的事）、预算有限的（中介费 3-10 万，DIY 几乎免费）。

如果你能用这个 skill + 各校官网搞清楚每一步，省下的中介费够你雅思考 5 次。

---

## 数据来源

各大学与机构官网（英文/当地语言）、官方政策文件、中文留学社区公开讨论（小红书、知乎、一亩三分地、豆瓣、Reddit），跨平台综合后提取对中国学生有用的部分。

## 注意事项

- 留学政策变化频繁，具体数字以各校官网为准
- 不对申请结果做任何保证
- 欢迎 fork 和提 issue

> **v1.0.0 迁移提示**：skill 已移到 `skills/euro-grad-apply/`。之前 `git clone` 到 `~/.claude/skills/` 的用户请改用上面的 `/plugin` 安装。

## License

[MIT](LICENSE)
