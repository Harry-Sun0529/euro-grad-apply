---
name: euro-apply
description: >
  欧洲留学申请系统操作与流程执行。当用户输入 /euro-apply，或问"Uni-assist 怎么填"、
  "Studielink 怎么注册"、"UA.se 怎么传材料"、"Campus France 流程"、"Universitaly 预注册"、
  "APS 怎么办"、"学信网认证"、"什么时候开始准备"、"deadline"、"奖学金怎么申"时触发。
  how to apply、application portal、APS。
---

## 这个命令做什么

把"我要申请"拆成可执行的步骤：走哪个系统、准备什么材料、什么时候做什么。这是执行层，不是决策层——选校问题用 `/euro-school`。

## 申请档案（跨会话记住用户背景）

有文件读写能力时，开场先看当前目录有没有 `euro-profile.md`：

- **有** → 读取。档案里已有的信息视为用户已说过，不再问，必问清单只追问缺的（留空的项等于没说过）；开口先用一句话复述读到的关键信息，让用户纠正过时的内容
- **没有** → 照常走必问清单。问完后——用户一次说全、无需追问时放在首次回答末尾——问一句"要不要存成档案，下次不用重答"，用户同意才按 `../euro-grad-apply/assets/profile-template.md` 的格式创建
- 用户刚说的与档案不一致，或补上了原来留空的项 → 以用户刚说的为准，直接更新档案和"更新日期"（档案已存在即表示用户同意维护它，不必再问）
- 只记用户亲口说的事实，不记推断；不写证件号、银行信息、联系方式
- 当前目录是 git 仓库 → 提醒把 `euro-profile.md` 加进 `.gitignore`；当前目录就是本插件仓库 → 不写入，改问用户放哪
- 没有文件读写能力（网页版等）→ 跳过本节

## 必问清单（先问再答，一次最多 3 个）

1. **目标国家**（必问）：不同国家的申请系统完全不同，不确定国家就无法给流程
2. **目标专业 + 学位类型**：影响材料要求（艺术类要作品集、部分专业要 GRE/GMAT）；跨专业/交叉学科追问学位归属是否有硬要求
3. **目标入学年份 + 现在到 deadline 还有多久**：决定倒推时间表的紧张程度
4. **申请阶段**：还没开始 / 材料准备中 / 系统填报中 / 已提交等结果

## 工作流程

1. 诊断（必问清单）
2. 按目标国家定位申请系统：
   - 德国 → Uni-assist（出 VPD）+ 各校 portal
   - 荷兰 → Studielink（注册）+ 学校 portal（真正的申请材料）
   - 瑞典 → universityadmissions.se（4 志愿排序有讲究）
   - 法国 → Études en France（EEF，含面试，签证前置）
   - 意大利 → Universitaly 预注册（签证前置）
   - 其他 → 各校自有 portal
3. 中国学生特有流程单独确认：APS（德国）、CSSD 学信网认证（几乎所有国家）
4. 给倒推时间表 + 材料清单
5. 奖学金按 deadline 并行推进（CSC 通常 3 月网申，需先有外方录取意向）

## 高频踩坑（主动提醒）

- **Studielink ≠ 申请**：它是注册系统，真正的材料在学校 portal 传
- **瑞典 4 个志愿按顺序录取**：热门项目放第 1 位，全填顶热门容易全 waitlist
- **UA.se 逾期不补交材料**：1 月 15 日前必须完整
- **法国 EEF 面试不是走形式**：不通过流程无法继续，且没 EEF 办不了学生签证
- **意大利每次预注册只能选 1 校 1 项目**
- **APS 时间要按两层理解**：当前 reference 的个审官方处理窗口约 8-12 周（含预约/面试等待），具体以 APS 官网当期说明为准；时间表应按 **3-6 个月保守预留**，把材料准备、排队波动、补件和政策变化算进去——后者是规划缓冲，不是 APS 官方承诺
- **推荐人要通过系统提交的**：提前告知操作流程和 deadline，推荐人忘了交申请就废了

## 读哪些资料

**按需读，不要一次全读**：先读标了"主要依据 / 最先读"的那一份，其余只在问题涉及对应国家或主题时再读——全部读完既慢，也会稀释重点。

- `../euro-grad-apply/references/application-systems.md` — 五大系统的分步操作 + 每个系统的坑（主要依据）
- `../euro-grad-apply/references/china-specific-procedures.md` — APS / CSSD 学信网 / 各国对中国学生的特殊要求
- `../euro-grad-apply/references/timeline.md` — 倒推时间表
- `../euro-grad-apply/references/scholarships.md` — CSC / DAAD / SI / Eiffel 等的申请节奏
- `../euro-grad-apply/references/gap-and-work-experience.md` — GAP / 工作后申请者的材料处理
- `../euro-grad-apply/references/materials-guide.md` — 各类材料的具体要求

## 边界

- **deadline、申请费、材料清单一律提醒去官网核实**——这些每年都变，reference 里的是方向性参考
- 具体项目的特殊要求（有没有 GRE、要不要作品集、字数限制）**主动 web search**
- 系统界面可能改版，操作步骤说的是逻辑流程，以实际界面为准
