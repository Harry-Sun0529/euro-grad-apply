# Euro Grad Apply

帮中国学生申请欧洲大陆（非英国）硕士、博士的 AI skill。装好之后，AI 有了整套欧洲申请的知识——选校、文书、APS、签证、奖学金、毕业去留，你直接用自己的话提问，它会结合你的背景给建议，而不是让你去查官网。

> **内容快照**：2026-09 · **下次复审**：2027-01
>
> 学费、签证金额、奖学金额度、deadline 这些数字年年变。仓库里的数字都是方向性参考，做决定前请到官网核实。

## 三十秒装好

看你用哪个 AI，对号入座：

| 你用的 AI | 装法 | 耗时 |
|---|---|---|
| Claude Code | 两条命令 | 1 分钟 |
| Codex | 发一个链接 | 1 分钟 |
| DeepSeek Harness / WorkBuddy | 复制文件 | 5 分钟 |
| Kimi / 豆包 / ChatGPT 等网页版 | 下载一个文件，传进智能体 | 5 分钟 |
| 不会命令行 | 下载解压，拖文件夹 | 10 分钟 |

详细步骤在下面。装完可以直接问一句试试：

```
我 985 计算机本科，GPA 88，雅思还没考，
想申德国或荷兰的 CS 硕士，毕业倾向留在欧洲。
帮我做个规划。
```

---

## 各平台安装步骤

### Claude Code

```
/plugin marketplace add Harry-Sun0529/euro-grad-apply
/plugin install euro-grad-apply@harry-skills
```

装完直接问问题。更新：`/plugin marketplace update harry-skills`

### Codex

把这行发给 Codex，说"帮我安装这个 skill"：

```
https://github.com/Harry-Sun0529/euro-grad-apply
```

### DeepSeek Harness（DSH）

```bash
git clone --depth 1 https://github.com/Harry-Sun0529/euro-grad-apply.git ~/euro-src
mkdir -p ~/.agents/skills && cp -r ~/euro-src/skills/* ~/.agents/skills/
```

重启 DSH 生效。更新：`cd ~/euro-src && git pull && cp -r skills/* ~/.agents/skills/`

只想在某个项目里用的话，把 `~/.agents/skills` 换成 `你的项目/.dsh/skills`。

### WorkBuddy

```bash
git clone --depth 1 https://github.com/Harry-Sun0529/euro-grad-apply.git ~/euro-src
mkdir -p ~/.workbuddy/skills && cp -r ~/euro-src/skills/* ~/.workbuddy/skills/
```

重启 WorkBuddy 生效。

### 不会用命令行

1. 点仓库首页绿色 **Code** 按钮 → Download ZIP → 解压

   <img width="600" alt="download zip" src="https://github.com/user-attachments/assets/317d8dd9-0557-4b73-a11c-bb87aeafa48d" />

2. 打开你 AI 的 skills 目录：
   - WorkBuddy：macOS 在 Finder 按 `Cmd+Shift+G` 输入 `~/.workbuddy/skills`；Windows 地址栏输入 `%USERPROFILE%\.workbuddy\skills`
   - DSH：Settings → Skills → 导入文件夹
3. 把解压后 `skills/` 里的 **7 个文件夹全部**拖进去
4. 重启

注意必须 7 个一起装。6 个斜杠命令的资料都放在 `euro-grad-apply/references/` 里，只装命令文件夹的话命令会读不到内容。

### Kimi / 豆包 / ChatGPT 等网页版

这些平台没有插件系统，但可以传进"智能体 / Projects"当知识库：

1. 下载 [`euro-grad-apply-full.md`](euro-grad-apply-full.md)（所有内容合并成的单文件）
2. 在 AI 里创建智能体（Kimi、豆包、通义、智谱免费；ChatGPT、Claude、Gemini 需订阅）
3. 找到"知识库 / 文件"上传入口，把这一个文件传上去
4. 保存，之后进这个智能体直接问

网页版拿到的是知识库（该问什么、各国怎么选、流程怎么走），但没有斜杠命令，也不能生成 CV 成品文件——那个需要本地文件系统。

只想试一下的话：打开 [`SKILL.md`](skills/euro-grad-apply/SKILL.md)，点右上角 Copy raw file，粘贴给任何 AI，加一句"请把这当作你的知识库"。

<img width="338" alt="copy raw file" src="https://github.com/user-attachments/assets/9c707de8-beb2-4e0a-b667-a1585da58603" />

---

## 装完能干什么

不用记命令，直接问就行，AI 会自己判断该查哪部分资料。装了插件的话另有 6 个快捷命令：

| 命令 | 什么时候用 | 举例 |
|---|---|---|
| `/euro-school` | 选国选校 | "我这背景能申什么学校""德国还是荷兰" |
| `/euro-docs` | 写文书 | "动机信怎么写""SoP 怎么改" |
| `/euro-cv` | 做简历 | "帮我做一份投 TUM 的 CV" |
| `/euro-phd` | 申博士 | "怎么套磁""博士有工资吗" |
| `/euro-apply` | 走申请流程 | "Uni-assist 怎么填""APS 怎么办" |
| `/euro-visa` | 拿到 offer 后 | "签证怎么办""资金证明""落地做什么" |

覆盖德国、荷兰、瑞典、挪威、丹麦、芬兰、瑞士、法国、意大利、西班牙、比利时、奥地利；理工、商科、人文社科、艺术设计、建筑、医学；从选校、文书、申请系统、奖学金、签证、落地到永居入籍的全流程。

中国学生特有的部分单独写了：APS 审核、CSSD 学信网认证、回国留服认证看院系归属、CSC 公派、意大利预注册。其中"学位证书上的名称"这件事最容易被忽略——同样做艺术治疗，挂心理系回国认心理学类，挂艺术学院认艺术类。想清楚你要哪一类再选项目。

还有几个专题：按毕业目标选校（回国 / 留欧 / 兼顾 / 跳板，四种目标走完全不同的路）、GAP 和工作后再申请、跨专业、保底校怎么搭。

---

## 开始前想清楚 6 件事

把答案一次性告诉 AI，比被来回追问快得多：

1. 读硕还是读博？毕业后回国、留欧、兼顾还是当跳板？
2. 想申什么专业？学位证书上的名称有要求吗？（跨专业、交叉学科的看上面留服认证那段）
3. 本科什么层次（985/211/双非/中外合办）？GPA 多少？什么专业？有没有工作经验？
4. 一年总共能花多少（学费加生活费）？
5. 雅思托福考了吗？多少分？愿不愿意学当地语言？
6. 想什么时候入学？还有多久准备？

---

## 怎么问最有效

好的开场是这样的：

> 985 计算机本科，GPA 88，雅思没考，想申德国或荷兰 CS 硕士，倾向留欧。给我做个规划。

> 211 经管本科 GPA 84，工作 2 年做数据分析，想跨申商业分析，预算 30 万。

> 拿到了 TU Delft 和 ETH 的 offer，怎么选？

不太行的开场："去欧洲留学好吗"（太宽泛，只能得到百科式答案）、"推荐学校"（没背景，只能给通用清单）。

一次问一个问题；答案不够就说"再具体些""做个表格对比"；AI 给的数字，最终以官网为准。

---

## DIY 还是找中介

DIY 完全可行——申请流程的官方信息都是公开的。中介的定位是"按模板批量处理流程"，适合完全不会英语、时间极紧、或需要特定内推关系的人。

中介不适合你，如果：你想按自己情况定制路径（中介按模板走）、你打算留欧长期发展（中介不管你毕业后的事）、你预算有限（中介费 3-10 万，DIY 几乎免费）。

用这个 skill 加各校官网搞清楚每一步，省下的中介费够你雅思考 5 次。

---

## 文件结构

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

euro-grad-apply-full.md         # 全部内容合并单文件（自动生成，别手改）
```

所有专题资料只放在 `euro-grad-apply/references/` 一处，场景 skill 不建自己的 references 目录。

---

## 数据来源与注意事项

数据来自各大学与机构官网（英文/当地语言）、官方政策文件、中文留学社区的公开讨论（小红书、知乎、一亩三分地、豆瓣、Reddit），取对中国学生有用的部分。

- 留学政策变化频繁，具体数字以各校官网为准
- 不对申请结果做任何保证
- 欢迎 fork 和提 issue

v1.0.0 之前的用户看这里：skill 已移到 `skills/euro-grad-apply/` 目录。之前 `git clone` 到 `~/.claude/skills/` 的装法已失效，请改用上面的 `/plugin` 安装。

## License

[MIT](LICENSE)
