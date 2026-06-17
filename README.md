# Euro Grad Apply - 欧洲留学申请 Skill

帮助中国学生规划和准备欧洲大陆硕士/博士申请的 AI 技能包。

## 覆盖范围

- **国家**：德国、荷兰、瑞典、挪威、丹麦、芬兰、瑞士、法国、意大利、西班牙、比利时、奥地利等
- **学科**：理工、商科、人文社科、艺术设计、建筑、医学等
- **内容**：选国选校、申请时间线、文书写作、GPA 换算、语言要求、各国特殊流程（APS/Nuffic/Campus France 等）、奖学金（CSC/DAAD/SI/Eiffel/Erasmus Mundus 等）、博士套磁、签证行前
- **信息整合**：从各国官网、英文/当地语言资料及中文留学社区（小红书、知乎、一亩三分地等）全网搜集信息，提取对中国学生有用的内容

## 使用方式

**Claude Code**
```bash
cd ~/.claude/skills/
git clone https://github.com/Harry-Sun0529/euro-grad-apply.git
```

**其他 AI 助手**

将 `SKILL.md` 和 `references/` 目录下的内容作为系统提示词或知识库导入即可。核心是让模型能读取 `SKILL.md`（主框架）和各 `references/*.md`（详细资料）。

安装后直接用中文或英文提问：

- "985 CS 本科 GPA 88，想申德国或荷兰硕士，怎么规划？"
- "APS 面审和 TestAS 怎么选？"
- "ETH 和 TU Delft 申请难度对比"
- "CSC 和 DAAD 能同时申吗？"
- "欧洲博士怎么套磁？"

## 文件结构

```
SKILL.md                    # 主技能文件
references/
├── germany.md              # 德国
├── netherlands.md           # 荷兰
├── sweden-norway-denmark-finland.md  # 北欧四国
├── switzerland.md           # 瑞士
├── france.md                # 法国
├── southern-europe.md       # 意/西/葡
├── belgium-austria.md       # 比利时/奥地利
├── scholarships.md          # 奖学金大全
├── materials-guide.md       # 文书写作
├── phd-guide.md             # 博士申请
├── timeline.md              # 时间线
├── chinese-info-sources.md  # 中文信息源
└── arts-and-humanities.md   # 艺术/人文类
```

## 数据来源

- 各大学及机构官网（英文/当地语言）
- 官方政策文件与新闻报道
- 中文留学社区公开讨论（小红书、知乎、一亩三分地、豆瓣等）

## 注意事项

- 留学政策变化频繁，具体数字请以各校官网为准
- 不替代专业留学顾问的个性化服务
- 不对申请结果做任何保证
