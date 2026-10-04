# F113_nested_tsmax_demean — 交接状态

_自动生成于 2026-10-04 13:43(`python scripts/recorder.py --brief F113_nested_tsmax_demean` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1375(批次 B01_single_factors)
- 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F113_nested_tsmax_demean`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F113_nested_tsmax_demean#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F113_nested_tsmax_demean#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F113_nested_tsmax_demean#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:14 → `handoff/F113_nested_tsmax_demean/agents/work_R0_a90200e4d0e83c361.md`
- agent `lead:F113_nested_tsmax_demean#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:31 → `handoff/F113_nested_tsmax_demean/agents/lead_R1_a2eb883d5a1bdefdc.md`
- agent `lead:F113_nested_tsmax_demean#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F113_nested_tsmax_demean#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F113_nested_tsmax_demean` 看服务器上的 tag,`./scripts/study.sh digest F113_nested_tsmax_demean <tag>` 重看结果)。

## 研究现状(`notes/F113_nested_tsmax_demean/state.md`,10-04 13:31 更新)—— **先读这个文件**

# 研究现状 — F113_nested_tsmax_demean

> 主研每轮**整个覆盖重写**这一页。最近更新:**第 1 轮(主研 Opus 5),2026-10-04**。
> 流水在 `journal.md`(只追加);这一页是"现在的理解"。

---

## 1. 一句话现状

R0 建档已完成(表达式/算子/分解/基线四份事实文件 + `results/R0.md`),**我(第一个主研)这一轮写了
`04_grammar.md`(结构语法)和 `05_hypotheses.md`(10 条竞争性假设),并下了第一张工单 `orders/R1.md`**
(kind: experiment,2 次服务器运行:消融阶梯 `S1_chain` 10 个变体 + 自写脚本 `x1_ties`)。
**下一步是执行去跑 R1、写 `results/R1.md`;再下一轮主研读它、裁决 H1~H9。**
本轮**没有跑任何服务器运行**(只读了 `ops`、`src`、`partura/diagnose.py`)。

---

(…全文 12421 字符,读 `notes/F113_nested_tsmax_demean/state.md`)

## 研究日志(`notes/F113_nested_tsmax_demean/journal.md`:1 条,其中研究员自己写的 1 条)

最近的 12 条(完整的看文件):

### 2026-10-04 13:12 [执行] R0 建档完成:四份事实文件+结果卡已写,树是不分支链/恒非负/82天回看,基线已对齐公布值

看了什么:study.sh brief;study.sh digest F113_nested_tsmax_demean S0_baseline;scripts/overview_for.py;
study.sh decompose;表达式里全部 7 个不同算子(day_mean/ts_max/sub/cs_demean/pow_2/mul/pow_1_5)的 study.sh src
(含它们调用的 rolling_windows/nanmax_last/create_like/cs_mean/_mean/_valid/sign)。另外读了 S0_baseline.json
和 ledger.json 原文、configs/F113_nested_tsmax_demean.yaml 的 git 历史。

写了什么:notes/F113_nested_tsmax_demean/{01_expression,02_operators,03_decomposition,06_baseline}.md
和 results/R0.md。没有写假设表、没有设计或跑新实验、没有碰 state.md 或配置文件(按分工这些是主研的事)。

结构事实(源码推导,非实测):表达式是一条不分支的链(12 个中间节点全部只被引用 1 次),只用 Ret 一个字段;
两次 pow_2 + 四次 ts_max 组合可证明原始输出恒 ≥ 0(或 NaN),方向完全是外部加的 sign=-1;对 Ret 的尺度是
6 次齐次;四层 ts_max(5/30/20/30)串联,累计回看 82 个交易日(比最大单窗口 30 长得多)。sub(ts_max(...,5),-5)
紧跟 cs_demean,这个"-5"被精确代数抵消,与取值无关——是本次找到的唯一恒等节点。

基线(S0_baseline,errors={}):公布的 sgn/hl/ls[0]/long[0] 四个可核对字段全部复现一致,但公布表"long"列核对
下来是多头腿毛超额(Lgross=+3.7%=0.037),不是净超额(Lnet 只有+0.7%)。决策口径下多头腿净超额/夏普 train 为正
(+1.6%/0.39)、valid 转负(-1.7%/-0.52),long_share 很低且 valid 更低(15.7%→4.2%),钱主要在空头腿;多空夏普
两段都稳(+2.59/+2.39)。分位剖面不单调,valid 峰值在 Q3(+11.5%)不在 Q10(+1.5%)。全部控制变量只张成
R²=0.058。rank IC 随持有期单调上升(不是衰减)。

异常(写进了结果卡,没下结论):① known_stdamt_mean30 缺失于 S0 的中性化表/rank相关表/overview_for.py——
核对 git 历史,加入这条配置的 commit 5ed9d09 比 S0_baseline.json 生成时间晚,判断是时序问题不是求值失败,
但未重跑验证;② view.warmup_rows 实测为 0(配置写 warmup:60,结构需要 82 天),猜测数据源无更早历史,未核实;
③ books 的 rank_by 字段是旧值 'ls'(配置现在是 'long'),但完整 7 点 sweep 证实 hl=1 同时是两种准则的最大值,
数字未受影响;④ digest 的 rICtraded 两段都是空;⑤ digest(原始面板)与 overview_for.py(交易信号)的 rank
相关符号相反(翻方向)但数值对得上,两张表不能直接合并引用。

下一步交给主研:读 results/R0.md 和四份 notes 定研究方向;已标出的异常(尤其①②)可能需要先决定要不要重跑 S0。

## 工单与结果卡(`notes/F113_nested_tsmax_demean/orders/`、`notes/F113_nested_tsmax_demean/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F113_nested_tsmax_demean.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F113_nested_tsmax_demean`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S0_baseline`

## 已写的 notes(`notes/F113_nested_tsmax_demean/`)

- `01_expression.md`  4248 字节  10-04 13:07
- `02_operators.md`  10430 字节  10-04 13:08
- `03_decomposition.md`  7986 字节  10-04 13:09
- `04_grammar.md`  8997 字节  10-04 13:23
- `05_hypotheses.md`  11082 字节  10-04 13:43
- `06_baseline.md`  14224 字节  10-04 13:11
- `journal.md`  3137 字节  10-04 13:12
- `state.md`  21057 字节  10-04 13:31

## 自写的探针与分析脚本(`studies/F113_nested_tsmax_demean/`)

(无)

## 结构化结果(`handoff/F113_nested_tsmax_demean/results/`)

(还没有)
