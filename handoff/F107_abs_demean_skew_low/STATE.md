# F107_abs_demean_skew_low — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F107_abs_demean_skew_low` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #613(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_skew(Low)))`

## 现在到哪一步

- **阶段:研究完成,待审查**
- **留出段已经读过 2 次**(10-04 15:05, 10-05 12:12)—— **不许再读**。候选在留出段上的数全在 `runs/F107_abs_demean_skew_low/final.json`(`./scripts/study.sh digest F107_abs_demean_skew_low final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `study:F107_abs_demean_skew_low`:已返回结果,最后动作 10-05 00:10 → `handoff/F107_abs_demean_skew_low/agents/study_a8f81191021f7ad76.md`
  - `audit-numbers:F107_abs_demean_skew_low`:中断,最后动作 10-05 00:20 → `handoff/F107_abs_demean_skew_low/agents/audit-numbers_af741730e118097dc.md`
  - `synth:F107_abs_demean_skew_low`:已返回结果,最后动作 10-05 11:21 → `handoff/F107_abs_demean_skew_low/agents/synth_abe597cc35a36fd73.md`

**接手的人该做什么:** 研究已完成,结构化结论在 `handoff/F107_abs_demean_skew_low/results/study.json`。下一步是独立审查(审查员不要用研究员的口吻替它说话)。

## 研究现状(`notes/F107_abs_demean_skew_low/state.md`,10-05 11:19 更新)—— **先读这个文件**

# F107_abs_demean_skew_low — 研究现状

> 主研**第 6 轮(批量扫描综合轮)**写(Opus 5,2026-10-05),整页覆盖重写。
> `abs_(cs_demean(day_skew(Low)))`,挖掘 #613。记 `A = day_skew(Low)`、`B = cs_demean(A)`,信号 `abs(B)`,方向 **−1**。
> **留出段已读(tag `FINAL`,1 次),额度用完,不许再读。** 本轮只读 `study.sh table F107_abs_demean_skew_low s1 --all`
> 的 73 变体大表 + 市场解剖,**没跑任何计算、没碰任何已定稿的 notes**。

## 1. 现状

**原式的否定结论已由第二条独立路径复现、可当定论用**:对纯多头用户,F107 相对已知成交额族 `k_known` **零增量**,
原式本身不可用(utrain 多头净超额 **+1.7%**、Lshp **+0.36**,对家族 +15.4% / +2.22)。推荐仍是上一轮定死的
`recommended_id = f_m20`、`recommended_kind = known_family`,**不改判、不换人**。

**本轮唯一的新东西是一条线索**:大表里唯一换掉了对象的变体 `sub_A_day_gini = abs_(cs_demean(day_gini(Low)))`
(+10.0 / +5.4 / **+8.7%**,Lshp +2.39 / +1.26 / **+2.07**,ρo 只 0.27、ρk 0.33,cov 1.00 / dist 0.96 过门槛)。
读代码后判定:**`day_gini` 喂给价格水平时 ≈ c·σ/μ,是无尺度的日内相对波动,不是集中度** —— 它是**另一条因子穿着同一件外套**。
它 train→valid 夏普 2.39 → 1.26(超出 ±0.3 带)、valid 净超额比家族低 17pp,所以**是线索不是候选**。

本轮产出:`notes/<fid>/synthesis.md`(117 行,完整论证)、`studies/<fid>/hypo.yaml`(**40 条,40/40 parse**)、journal 第 17 条。

(…全文 6098 字符,读 `notes/F107_abs_demean_skew_low/state.md`)

## 研究日志(`notes/F107_abs_demean_skew_low/journal.md`:17 条,其中研究员自己写的 10 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:25 [主研] 第 4 轮:核验第3轮判断类 notes(数字逐个对过 JSON,全部相符)→ 下 R3(kind: writeup),重写 state.md

**本轮的处境。** `brief` 显示留出段已读过一次(tag `FINAL`,10-04 15:05),而 `lead#3` 失败、最后动作 15:44。
对照文件时间戳发现:**第 3 轮其实把全部判断类 notes 都写完了**(`11_risks.md` 15:35、`09_diagnosis.md` 15:36、
`12_next.md` 15:36、`08_variants.md` 15:37、`10_distilled.md` 15:38、`05_hypotheses.md` + `07_S_final.md` 15:39),
**只差最后两步就中断**:没写 writeup 工单、没重写 state.md(还是第 2 轮那版 40KB)。
按工单规则「留出段已读的,这一轮必须是 (c) 成文」—— (c) 的判断类 notes 已经有了,所以本轮的正确动作不是重做,
而是**核验 + 补上缺的两步**。没有开任何实验轮,没有跑任何求值运行(求值仍是 5/8)。

**核验的结果:第 3 轮的产出可以信,数字我逐个对过 JSON。** 我直接从
`runs/F107_abs_demean_skew_low/FINAL.json` 的 `results.<id>.books_user.splits` 复算了全部五条判据:
判据0 `f_K` +14.103%/1.5086(落在事前 band +13~15%/1.4~1.9);判据1 原式成本 9.04pp 吃掉毛超额 86%;
判据2 `f_m20−f_orig` = **+2.9266pp**(门槛 3pp,差 0.0734pp 没过)、Lshp +0.7100,归因分解 5.74−2.81=2.93 对得上;
判据3 `f_m20K−f_K` = **−6.1233pp / −0.5354**,中点 ho 9.2214% vs 混合 7.98%、utrain 10.4023% vs 12.82%(两段反号);
判据4 `f_m20−f_m20absret` = **+3.1295pp**;`f_m20absret` 衰减 −6.2273pp。**与 notes 里写的全部一致。**
train/valid 侧也从 `S12.json`/`S0_baseline.json` 抽核了十条(`v_bas
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:49 [执行] R3:补齐4份事实类notes+改正05_hypotheses一处笔误,report重出并通读核对,0次新求值

补了 01_expression.md / 07_S0_baseline.md / 07_neutralise.md / 07_conditional.md(均只写事实+指针,无新判断)。
05_hypotheses.md 第48行 H6 那条数字笔误 +3.4/+3.7 → +3.5/+3.8(S12.json 核实,与09_diagnosis A5一致)。
report 重出(2151行),§2(iii)载重数字表全部独立核对一致(判据2 +2.9266pp/判据3 -6.1233pp/判据4 +3.1295pp/判据0 f_K +14.103%·1.5086 等,精确到小数点后4位与工单完全相符);train/valid 抽查9条全部一致。
发现两处非授权修改范围的问题留给主研裁决:(a)报告第7节"控制变量"表其实有数据(13行),只是07_controls.md这份notes没人写过,不在本工单4份清单内;(b)09_diagnosis.md A8/B1与12_next.md共3处引用x1数字(R²0.307/残差+2.9%等)缺"numpy探路"标注,这些文件的措辞我不能改。
本工单0次新求值运行(run/final/exec全未调用),全研究服务器运行仍是5次。

### 2026-10-05 00:07 [主研] 第5轮(结题):成文后最后一道核对,0 次运行,补 07_controls.md + 三处 numpy 标注,report 重出 2181 行

本轮没有做实验、没有读留出段、没有改任何推荐或判决。做的三件事:

(a) **核对**:把 notes 里所有载重结论句与 `FINAL.json` 的「与用户表同口径」表逐条对过 ——
**无一处不符**。核到的点:五条留出段 Lnet(1.4127/4.3392/14.1035/7.9802/1.2098%)与 utrain
(1.67/5.40/15.40/12.82/7.44%)、判据 2/3/4 的差值(+2.9266 / −6.1233 / +3.1295pp)、
判据 0 的 f_K(+14.103% / 1.5086)、f_m20absret 衰减 −6.2273pp,以及 state.md §2 的表。
顺带确认 `original_at_long_halflife` 这件事没被写错:原式在它的多头最优半衰期(hl20)上也只有 +1.41%,
是「不够用」,不是「够用」——结构化结果里据此填 false。

(b) **补 `07_controls.md`**(R3 §4 第 1 条留的裁决项)。报告第 7 节那张 13 行「控制变量/已知家族自己当因子」
表下面原来是静默空白。新写的只有事实 + 指针,三组数字全部从 `S0_baseline.json` → `diagnostics.controls`
重新取并核过:已知家族两条自己就很强(`known_stdamt_mean30` +12.6/+22.3%·1.78/3.46;
`known_stdamt_max9` +13.7/+22.2%·1.99/3.59),而 `ctl_dvol20`(「低特质波动」那一维)自己当因子时
多头腿是 **−9.0% / +0.6%**(Lshp −0.89/+0.07),`ctl_cap` 的 fit 段 rank IC 只有 +0.0016。
后两条是给 11_risks §7 / 09_diagnosis C1 和 A8 加的「别混」注脚,没有下新判断。

(c) **三处「numpy 探路」标注**(R3 §4 第 2 条):`09_diagnosis.md` A8(x1 §5 的十分位百分位秩)、
B1(x1 §6 的 R² 0.307 / 残差 +2.9%)、`11_risks.md` §2(同一个 0.307)。
**`10_distill
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:07 [主研] 研究完成:推荐 f_m20(状态=被否定;kind=known_family,对纯多头用户相对成交额波动家族没有增量)

**理由。** 推荐栏按规矩填的是事前写死的第一推荐 `f_m20 = cross_mean(abs_(cs_demean(day_skew(Low))), 20)`
(ρ(v_base) 0.918 → 算提纯;用户口径 hlL 10;留出段 Lnet +4.34% / Lshp 1.012 / LTO 4.37% / Lmdd −2.92%),
**状态是「被否定」**:判据 2 要求 Lnet 领先原式 ≥3pp,实得 +2.9266pp,差 0.0734pp。读完留出段不改判、不换人,
所以没有把 `f_K` 或 `f_m60` 提成推荐。

**但对用户真正要紧的不是判据 2,而是判据 1 和 3 —— 只有这两条离门槛很远、承得住重:**
① 原式照现在的样子对只能做多的用户**不可用**:留出段毛超额 +10.45% 是真的,但 11.96% 的换手带来 9.04pp 成本,
吃掉毛超额的 86%,净只剩 +1.41%(Lshp 0.302)。树里没有任何日轴算子,半衰期已经顶到网格上界 hl20。
② 把 20 日记忆写进表达式确实把净超额抬到 +4.34%,**但归因是换手不是结构**(成本 9.04→3.30 省 5.74pp、
毛超额反而让掉 2.81pp,5.74−2.81=2.93),而且这个水平**远低于已知成交额波动家族**(`f_K` +14.10% / 1.509);
等权秩相加 `f_m20K` 只有 +7.98%,比 K 单独**低 6.12pp / 0.535 夏普**(门槛 ±3pp / ±0.3,差两倍门槛),
连分散化收益都没有(混合相对两条中点的超出部分在 utrain 与 holdout 上**符号相反** = 噪声)。
→ **不建议为 F107 单开因子位;已经在跑 cross_mean/max(day_std(Amt), 9~30) 这一族的,叠上去是减分。**

**未决(都已写进 notes,别当成本研究的结论用):**
- C1 **优先级最高,而且不是这条因子的问题**:「低特质波动」这个暴露为什么在 2023-08 之后不付钱
  (`f_m20absret` 与 `gates.g_absidio20` 逐字相同,utrain +7.44% → holdout +1.21%,衰减 −6.23pp;
  `ctl_dvol20`
…(这条日志还有后文,读 journal.md)

### 2026-10-05 11:15 [主研] 批量扫描 s1 的综合

- 原式 = abs(A − 当日全市场均值),A = day_skew(Low) = 分钟最低价**水平**分布的偏度;方向 −1 → 多头腿买「日内路径形状最平庸」的票。承重只有「折叠 + 折叠的中心」:去 abs_ → iso −31.9%,去 cs_demean → −5.4%(比什么都不做更差),折两次 → −1.4~−7.9%。
- 外层保序变换全是同一件事:abs_/pow_2/sqrt(= sqrt(abs))/cs_normalize 四行 +1.5~+2.3%、ρo 0.92~0.99 —— 这是噪声标尺。算子陷阱:pow_05 = sign(x)·abs(x)^0.5(保号),其实是 iso;log = log(abs(x)) 但把最靠中心的票 NaN 掉(正是多头书)。五个价格叶子全可换、全接近零(Low/Close/Open/High/Vwap +1.7/+1.9/+2.1/+0.8/−0.5)。
- **多头腿的净超额 100% 来自流动性倾斜**:成交额五档段内 −8.1/−6.4/−3.7/−1.6/−2.4(**每档都负**),书对最低档超配 +16.5pp 而该档段等权 +15.1%。所以 bk/res × liq/known 四行全翻负(−2.5~−3.4),overlay 阶梯从家族单独单调下坡 +15.4→13.6→13.1→12.5 → **零增量,与上一轮留出段结论一致**。
- 记忆家族(+5.0~+6.6,窗口 5/10/30/60 全平)是**换手平台不是视界平台**(LTO 10.9%→2.8%);代价是它在 6.5% 的冻结盘口段 −23.7~−40.5%,而原式在那一段 +8.5%。大表里一个筛子形态都没有 → 第二批 D 组。
- **全表唯一的例外是 sub_A_day_gini**(+10.0/+5.4/+8.7,Lshp +2.07,ρo 0.27,ρk 0.33)。按 ops_ext.py 的代码,day_gini 喂给正的紧的**价格水平**时 ≈ c·σ/μ,是**无尺度的日内相对波动,不是集中度** → 多头书 = 「相对波动最中位」的筛子。解剖处处与原式相反:成交额五档段内全正且随流动性上升(最高档 +10.7)、下跌市 +7.7(全表唯一不塌)、高波动 +14.7、次新段 +14.8(全表最好)。但 train→valid 夏普 2.39→1.26 超出噪声带、valid 比家族低 17pp → **线索不是
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F107_abs_demean_skew_low/orders/`、`notes/F107_abs_demean_skew_low/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有

## 配置里的实验计划(`configs/F107_abs_demean_skew_low.yaml`)

- 标题:日内价格水平占用分布的偏度偏离全市场多少(折叠) —— 空头腿是封板/跳价事件,多头腿是「安静且随大盘走」的股票
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_parts**(11 个变体):原式三个节点(偏度、截面去均值、折叠)和字段各自是不是必需的?它是不是「日频 |特质收益|」「分钟收益峰度」这类朴素读数的另一种写法?
  p_signed、p_nodemean、p_znorm、p_close、p_range、p_rank、p_cube、r_absret、r_kurtret、r_kurtlow、r_mktcorr
- **S2_memory**(11 个变体):把日轴记忆写进表达式之后,多头腿净超额的改善有多大、来自平滑还是结构?记忆该是均值、中位数还是极值,窗口多长最稳?
  m10、m20、m30、m60、m120、md60、mr60、mx20、m60_nodemean、m20_absret、m60_absret
- **S_final**(5 个变体):只凭 train/valid 选定的 5 个候选,在留出段上是什么样?这条因子对纯多头用户相对已知家族有没有增量?
  f_orig、f_m20、f_K、f_m20K、f_m20absret

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F107_abs_demean_skew_low`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low S0_baseline`
- `S12`  10-04 13:59  22 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low S12`
- `FINAL`  10-04 15:05  5 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low FINAL`
- `sweep_s1`  10-05 10:50  78 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low sweep_s1`
- `anatomy_s1`  10-05 10:57  0 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low anatomy_s1`
- `sweep_s2`  10-05 11:58  129 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low sweep_s2`
- `anatomy_s2`  10-05 12:09  0 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low anatomy_s2`
- `sweepfinal_s2`  10-05 12:13  8 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low sweepfinal_s2`
- `x1`(自写脚本的输出)  10-04 12:31  exit 0  → `logs/F107_abs_demean_skew_low_x1.log`
- `x2`(自写脚本的输出)  10-04 14:01  exit 0  → `logs/F107_abs_demean_skew_low_x2.log`

## 已写的 notes(`notes/F107_abs_demean_skew_low/`)

`01_expression.md`(1K)、`02_operators.md`(2K)、`03_decomposition.md`(2K)、`04_grammar.md`(2K)、`05_hypotheses.md`(19K)、`06_baseline.md`(3K)、`07_S0_baseline.md`(1K)、`07_S1_parts.md`(12K)、`07_S2_memory.md`(12K)、`07_S_final.md`(10K)、`07_conditional.md`(1K)、`07_controls.md`(2K)、`07_neutralise.md`(1K)、`07x_1_anatomy.md`(10K)、`07x_2_elevate.md`(22K)、`08_variants.md`(6K)、`09_diagnosis.md`(11K)、`10_distilled.md`(17K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(32K)、`state.md`(9K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F107_abs_demean_skew_low/`)

- `probes.py`  10-03 17:50  Probes this tree needs: abs_(cs_demean(day_skew(Low))).
- `x1_anatomy.py`  10-04 12:16  x1 -- what  abs_(cs_demean(day_skew(Low)))  reads on REAL data, and where its long leg comes from.
- `x2_elevate.py`  10-04 12:44  x2 -- can the long leg of  abs_(cs_demean(day_skew(Low)))  be made better by STRUCTURE (not only by smoothing)

## 结构化结果(`handoff/F107_abs_demean_skew_low/results/`)

- `study.json`
- `synthesis.json`

报告:`research/alpha_distillation/F107_abs_demean_skew_low.md`(10-05 00:05 生成)
