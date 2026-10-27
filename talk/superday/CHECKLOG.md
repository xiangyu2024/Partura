# principles.pdf 检查记录

最终版本:17 页,13.333 in × 7.5 in(959.98 × 540 pt),XeLaTeX + Beamer(metropolis 内层 / 外层 / 配色主题,字体自设 Fira Sans Book / Medium + Fira Mono + Fira Math;第 17 页来源注里的中文文件名用 FandolHei)。图全部在 `figs/*.tex`(TikZ)。

## 检查方法(每轮都做)

- `latexmk -xelatex` 后扫 `principles.log`:Overfull / Underfull hbox·vbox、Missing character、字体警告。**最终:0 条。**
- `pdffonts`:只有 FiraSans-Book / BookItalic / Medium、FiraMono-Regular、FiraMath-Regular,外加 FandolHei(只用于「可交易回测」四个字)。
- `pdftotext -bbox`:第 2–17 页的标题首词全在 x = 61.2 pt(0.85 in)、yMin = 36.43 pt,完全相同;页码右缘 898.77 pt(= 页宽 − 0.85 in)、底线 517.0–517.3 pt,相同。
- 100 dpi 灰度渲染 + 脚本量:标题顶、内容顶(1.46–1.48 in,所有页一致)、内容底(≤ 6.91 in,不进页脚区)、左缘 0.84–0.86 in、右缘 ≤ 12.48 in(= 右边距)。
- 60 dpi 渲染 `pages/p-NN.png`,逐页看图:对齐、字号、拥挤 / 重叠、框里文字有没有被截断或换行撑高框。

## 逐页(最终状态与修过的问题)

| 页 | 标题 | 结果 | 修过什么 |
|---|---|---|---|
| 1 | Partura: an LLM research loop that steers a symbolic alpha miner | 通过 | 无 |
| 2 | Outline | 通过 | 列表编号原为右对齐(离左边距 0.12 in),改成贴左边距;第一项小字加入「why tokens buy beliefs」 |
| 3 | Search is cheap, belief is expensive | 通过 | 改版为嵌套双环:内环 120 个刻度 = 每次评估;外环 5 个节点,4 个 LLM 节点的蓝色深浅与右侧 token 计量条对应,搜索节点 0 token。修过:框内文字连字符断行撑高框;环内文字顶到刻度(改为 3 行,8 × 192 的说明移到图例);图例行距过挤;「0 tokens」标签移到虚线引导线上 |
| 4 | Tokens should buy beliefs, not candidates | 通过 | **新增页**(新论点)。左:累计 token 对候选数,生成式直线 vs 阶梯(两级台阶 = C01 R2、R3 之前的两轮 agent 调用;x 轴 1,536 / 3,072 / 4,608 为真实每臂计数),右:候选漏斗,标出两种设计各在哪里付 token;比例全部标 *illustrative*。修过:两条曲线标签互相压住;纵轴标签越出左边距(左面板右移 0.2 in);虚线引导线穿过 *illustrative* 标签;整页溢出页脚(压缩纵向) |
| 5 | Task specification | 通过 | 改版:等轴三维张量(股票 × 日 × 分钟),第 t 日切片经表达式 x 收成日频矩阵的第 t 列,再进信号卡;箭头上写 $x:\mathbb{R}^{S\times D\times M}\to\mathbb{R}^{S\times D}$ 与「t close → t+1 open, 15-min VWAP」。修过:箭头标签与矩阵 / 卡片边框相压(加宽间距);矩阵标签被弧线箭头穿过;底部文字溢出(整图 yscale 0.90、行距收紧) |
| 6 | A finished output is a signal card | 通过 | 第一版表格整张不见(Beamer 把 `{...}` 当成副标题吞掉,改用 `\begingroup`);表头行异常高(p 列开头的 `\color` 产生空行,加 `\leavevmode`);表宽超出 0.1 in |
| 7 | The searcher is a black box with three handles | 通过 | 改版:黑箱内放一棵真实的类型化表达式树 `sub(cross_mean(day_skew(Ret), 20), cross_mean(day_std(Amt), 30))`(已用 AlphaCube 严格语法解析通过),模式 `day_skew(_)` 命中子树并高亮(已用 `partura.steer.Pattern` 验证);三个把手是框边上的端口。修过:说明行越出黑箱右缘(改两行);端口标签贴到高亮框(树右移 0.15 in);整页略溢出 |
| 8 | Agent roles | 通过 | 第一版表格被吞(同第 6 页);列宽总和超出版心,重新分配 |
| 9 | One round of the loop | 通过 | 改版为 UML 时序图:6 条生命线(Executors 画成 3 条并行线 + 叠放表头),消息上写文件名,重写环节放在「loop ≤ 1 [check fails]」框里,GPU 搜索是长激活条;右侧为模型层级 × 调用次数条。修过:loop 标签超出五边形并压住「issues」;GPU 说明被 evidence.json 标签遮住一行;消息标签与激活条相交(标签统一放到箭头上方并加白底遮生命线) |
| 10 | From belief to intervention | 通过 | 改版:同一组 5 个表达式族的三张对齐条形图 p(x) × w(x) = q(x),ban 为零、降权缩短、升权加长,每行左侧写造成变化的规则;下方公式 + 一条完整 YAML 规则(*illustrative*)。修过:[t] minipage 与图之间多出约 0.7 in 空白导致 YAML 溢出页面(改为固定的 `\colsafter` 间距);模式文字贴到 p 条(p 图右移 0.1 in) |
| 11 | Measuring the system, not a signal | 通过 | 改版:轮 × 种子矩阵(每格分 A|B 两半,R1 合并,种子号 101–108 / 201–208 / 301–308);下方时间轴按日期等比例(2018-01-02 至 2026-09-16 映射到版心宽,带年份刻度)。修过:R1 行标签贴到矩阵(矩阵右移);底部总数句越出右边距(删去重复半句);年份「2018」越出左边距(改左锚) |
| 12 | Decision rules, fixed before any run | 通过 | 新增贪心去重示意(*illustrative*):按分数排序,保留的 head 为蓝,被拒的用细线连到与其 \|ρ\| ≥ 0.7 的 head(上方)或 \|ρ\| ≥ 0.5 的已知族 k(下方)。修过:右栏表格顶线与左栏首行不齐;小字说明孤字换行;整页溢出 58 pt(示意图 yscale 0.72、说明并行) |
| 13 | Token accounting | 通过 | 改版:阶梯状模型层级条(块宽 = 层级,深浅 = 层级),每行写角色、每轮调用(实心 = 每轮必调,空心 = 视情况)、读什么、token(*measured, pending*);下方 C01 停止规则(实线框)与计划中的 meta-agent(虚线框)。修过:块内两行字挤出块高;「1, +1 after a redraft」压到下一列(改为「1 (+1)」并在图注解释);停止规则框文字三行撑高 |
| 14 | Integrity: what keeps the loop honest | 通过 | 第一版表格被吞(同第 6 页);每行改写成一行以内,补回结尾重点句 |
| 15 | Implemented vs. planned | 通过 | 表头基线不齐(改 base 锚点);虚线框压到第一行文字;「Tiered workflow…」一行压进 Where 列(Where 列改为文件名);计划项缩进与上面不齐 |
| 16 | Known limitations, stated before the results | 通过 | 项目符号原为右对齐(改贴左边距) |
| 17 | Where the full pipeline stands today | 通过 | **新增页**(放在最后,原有 1–16 页页码不变)。数字逐个对过来源:2.28 / +17.0% / −7.2%(可交易回测.md 第 239 行)、581 个交易日(第 13 行)、4.92(第 929 行,§18)、3.65(第 257 行)、+16.6% / 1.49 / 2.44(two_level/RESULT.md 第 4 条)。前推行数字用强调蓝,开发行灰字。修过:标题按原文太长(约 12.8 in,超出版心),改为「Where the full pipeline stands today」,「outside this experiment」放到第一行蓝字;三栏表行高过高导致整页溢出 166 pt,改为两栏(期间作为整行小标题)、表头不换行、结论句提到最前、子说明压成一行;来源注里的中文文件名缺字形,改用 FandolHei |

## 全局修过的问题

- 标题被缩进两次(frametitle 模板自带左边距,去掉多余 `\hskip`)。
- 文字起首页与图 / 表起首页的内容顶不一致(1.61 in 对 1.47 in):文字首行页加 `\textfirst`,[t] 双栏页加 `\colsfirst`,统一到 1.47 in。
- minipage 里两端对齐造成大字距:全部改 `\raggedright`,全文禁连字符。
- 图的 0.45 pt 线宽外溢触发 Overfull hbox:图统一用 `\fig{}` 装进版心宽的盒子。
- 表格线统一 0.9 pt、浅灰 #C8C8C8。

## 第三轮修订(按 `workflows/c01_round.js` 的真实调用图与数字更正)

重新编译后日志 0 条 Overfull / Underfull / 缺字形;17 页标题与页码位置不变;以下各页重新渲染逐页看过。

| 页 | 改了什么 | 检查中修过 |
|---|---|---|
| 3 | 计量条的角色说明按真实分工改:read evidence = Coordinator plan + Executors;compile guidance = Lead 写、Checker 跑校验;update beliefs = Coordinator final | 通过 |
| 5 | 立方体股票数 5,207 → 5,220(搜索视图) | 通过 |
| 8 | 角色表按工作流重写:Coordinator(plan 1–3 个问题和任务;final 改 / 否决、`beliefs_r<k>.md`、分配种子)、Executors(1–3 个并行,只交回分析,不写仓库)、Lead(写 `C01_r<k>.yaml` 与 `cards_r<k>.md` 并自跑校验)、Checker(只看 `c01_check_guidance.py` 的退出码)、Scripts/GPU(digest、16 个任务、token 账)、Judge | 第一版列宽总和超出版心 0.33 in、行折成三行导致溢出 97 pt;缩短措辞、重分列宽 |
| 9 | 时序图按真实顺序重画:代码 `c01_digest.py` → Coordinator plan → Executors(并行)→ Lead(问题与分析一起交给 Lead;Lead 写两份文件并自跑校验)→ Checker(退出码 0 才算合格;不合格:Lead 改一次、Checker 再跑一次)→ Coordinator final(审 / 改 / 否决、`beliefs_r2.md`、种子分配)→ `c01_queue.sh` 16 个任务、每次 2 个 → `evidence.json` → Judge。Executors 不再在 Lead 之后出现;层级条改为 2 / 1 (+1) / 1–3 / 1 (+1);注明每次调用无返回时最多重试 2 次、两次不合格沿用上一版指引 | 层级条注释越出右边距 0.13 in(改窄行);Executors 表头折行;Lead 自调用标签与下一条消息相压;代码说明被 `evidence.json` 标签遮住一行;loop 标签与「script output」相贴 |
| 11 | 时间轴右端标「2026-09-16」(替换 2026 年份标签),图注加一行:前推段终点 = 数据库最后一天,出自 Partura `research/two_level/RESULT.md` | 通过 |
| 13 | 层级条:Lead 1 (+1)、Executors 1–3;「读什么」按工作流改;代码行改为 scripts, GPU;图注加「每次调用无返回最多重试 2 次」 | 图注越出右边距(缩短);代码行说明压进 tokens 列(缩短) |
| 15 | implemented 加一行:C01 round workflow and its five scripts(`c01_round.js`, `c01_*`) | 行距由 0.31 改 0.29 以容纳新行;新行文字贴到 Where 列(缩短) |
| 16 | 幸存者偏差一条去掉具体股票数(改为「store 里每只票都存续到最后一天」),避免与 5,220 冲突 | 通过 |
| 17 | 脚注按给定文字重写(4.92 = §18 重选后的平滑十分位多空,剔除封板格;§11.1 同一冠军 hl3 不平滑:原标签 3.99、多头剔封涨停且空头剔封跌停 3.65;空头腿在 A 股不可交易) | 脚注多出两行导致溢出 19 pt:去掉表头行,列名写进单元格(「Long-only, …」「Long-short decile book (15 bp): …」),收紧行距 |
