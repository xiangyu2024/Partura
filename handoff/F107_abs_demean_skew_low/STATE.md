# F107_abs_demean_skew_low — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F107_abs_demean_skew_low` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #613(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_skew(Low)))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:05)—— **不许再读**。候选在留出段上的数全在 `runs/F107_abs_demean_skew_low/final.json`(`./scripts/study.sh digest F107_abs_demean_skew_low final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F107_abs_demean_skew_low#2`:已返回结果,最后动作 10-04 15:18 → `handoff/F107_abs_demean_skew_low/agents/work_R2_a2bc8edd28b214230.md`
  - `lead:F107_abs_demean_skew_low#3`:失败,最后动作 10-04 15:44 → `handoff/F107_abs_demean_skew_low/agents/lead_R3_a50b4c32e518f76fd.md`
  - `lead:F107_abs_demean_skew_low#3`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F107_abs_demean_skew_low` 看服务器上的 tag,`./scripts/study.sh digest F107_abs_demean_skew_low <tag>` 重看结果)。

## 研究现状(`notes/F107_abs_demean_skew_low/state.md`,10-04 14:42 更新)—— **先读这个文件**

# F107_abs_demean_skew_low — 研究现状

> 主研**第 2 轮**写(Opus 5,2026-10-04)。这一页**整页覆盖重写**(覆盖了第 1 轮那一版)。
> 表达式:`abs_(cs_demean(day_skew(Low)))`,来源 挖掘 #613。方向 **−1**(做多 `|B|` 小的),原式半衰期 **20**。
> 本轮的全部新证据来自 `results/R1.md`(tag `S12`,引擎 22 个变体)与 `07x_2_elevate.md`(tag `x2`,§a~§f,引擎 `st.books`)。
> 本轮写的 notes:`05_hypotheses.md` 末尾「第 2 轮裁决」+ H16、`07_S1_parts.md` / `07_S2_memory.md` / `07x_2_elevate.md` 的「解读」段、
> **`10_distilled.md` 的「读留出段之前」(候选 + 判据,已写死)**、`orders/R2.md`(kind: final)。

---

## 1. 一句话现状

**研究在实证上已经做完,而且结论是否定的;本轮已把候选与判据写死,下了 R2(kind: final)去读留出段。**
假设表上 **16 条没有一条停在「未验证」**;四个结构升华方向在 valid 上**全部不通过**;
对只能做多的用户,**八条候选 × 两种权重 = 十六个「与已知家族相加」的组合,在 valid 上无一超过已知家族单独**。
**下一步**:执行跑 `FINAL`(5 个候选,1 次运行)→ 下一轮主研读结果卡,按 `10_distilled.md` 的判据 0~4 逐条判,
写 `09_diagnosis.md` / `10_distilled.md` 的「读完留出段之后」/ `11_risks.md` / `12_next.md` / `08_variants.md`,
再下 kind: writeup 的工单。**预期结论:分辨成功、提纯成功(但归因是平滑)、升华没有、相对已知家族没有增量 → 不建议单开因子位。**

---

(…全文 24707 字符,读 `notes/F107_abs_demean_skew_low/state.md`)

## 研究日志(`notes/F107_abs_demean_skew_low/journal.md`:12 条,其中研究员自己写的 5 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 14:17 [执行] R1:S12(22变体)+x2(a-f六节)已收,均exit 0;结果卡写好,B/C两项数字有结构性缺口

做了什么:接手时 S12、x2 已在服务器跑(上一轮额度中断前起的),本轮未新起任何运行,只 wait+digest 收尾,
跑了一次 propose 草稿。写了结果卡 notes/F107_abs_demean_skew_low/results/R1.md 与三份事实类 notes
(07_S1_parts.md、07_S2_memory.md、07x_2_elevate.md)。

关键数字(全部在结果卡里逐项列出,这里只摘最关键的几个):
- H14(m20/m60 vs 对应的 absret 版本,净超额 tr/va):m20 +4.8%/+7.3% vs m20_absret +4.9%/+13.8%;
  m60 +5.6%/+6.5% vs m60_absret +6.2%/+14.8%。g_absidio20 的表达式与 m20_absret 逐字相同。
- H11 固定半衰期(hl20,train,净超额):v_base +1.1%,m10 +4.6%,m20 +4.8%,m30 +3.9%,m60 +3.3%,m120 +1.0%。
  但**这次引擎输出里没有 valid 侧的半衰期扫描、也没有跨变体同半衰期的"毛"超额**(JSON 的 sweep 只在 train、只有
  long_ann 没有 long_gross_ann)——工单 B 项要的"train 与 valid 都要"的毛/净/换手对照表,valid 那半、毛超额那列拿不到,
  已在结果卡 B 节写清楚,没有新起运行去补。
- C 项同理:g_absidio20/g_kurtlow20/known_stdamt_mean30 不在标准 diagnostics.neutralise 里(gates 本来就不自动进这张表),
  用 x1/x2 的替代数字顶上了(v_base 对 g_absidio20 残差多头毛 +2.9%;m20/m60 对 kurtLow 残差多头毛 +11.3%/+9.2%)。
- H15(x2 §a 取证):cross_mean 面板差集中在"窗口内仅 1 个有限观测"的边界格子,0.27% 的格子 |diff|>0.05,涉及 798 只股票;
  但 m10~m120 的 book 级 Lnet,x1 numpy 与引擎的差全部 ≤0.6pp(在 ±3pp 噪声带以内)。两套数字都抄进
…(这条日志还有后文,读 journal.md)

### 2026-10-04 14:43 [主研] 第 2 轮:H14/H13/H15/H4 全部落地,四个升华方向在 valid 上全不通过 → 候选与判据写死,下 R2 读留出段

**看到了什么(引擎数字,全部来自 results/R1.md 与 07x_2_elevate.md)。**

1. **H14 已确立,而且方向是「对手更好」。** m20 +4.8%/+7.3% 对 m20_absret +4.9%/**+13.8%**;
   m60 +5.6%/+6.5% 对 m60_absret +6.2%/**+14.8%**;r_absret 单独 +5.3%/+14.5%、Lshp 2.27、rIC +0.0449/+0.0493。
   train 差 ≤0.6pp(噪声内),**valid 上日频替身高 6.5~8.3pp,rIC 近乎翻倍**。第 1 轮定的判据(差 ≤3 点或两段不同向)满足。
   → **这棵树读的 241 根分钟最低价不只是没有增量,是负贡献**:把同样的「去均值 + 折叠 + 20 日记忆」
   施加在一个朴素日频收益上就更好。而 m20_absret 与 config 里的 g_absidio20 是**逐字相同的表达式**,
   与 ctl_dvol20 秩相关 −0.81 → 它就是「低特质波动」这个已知暴露。

2. **H13 被否定。** x2 §b:mean20|B−c| 在 train 上 argmax c=−0.4(+7.7%),该点 valid 只 **+2.2%**,
   而 valid 自己最好的是 c=0(+7.5%);λ 在 20 日那一族上**符号翻转**(train 选 +0.6、valid 偏 −0.3)。
   固定 hl20 下更干净:|B−(−0.4)| tr +5.6% / va +2.1% 对原式 +1.1%/+3.0% —— **train 升 4.5pp、valid 降 0.9pp,两段反向**。
   → 折叠的不对称(x1 §1 的最优桶在 −0.375)是真实的,但 c/λ 是 train 上拟合的常数,**做不成可交易的结构**。

3. **H15 已确立,x1 可以放心引用。** 8 个最大差格子全部是「窗口内仅 1 个有限观测、当天 base 为 NaN」;
   |diff|>0.05 的 0.31% 格子 mean finite-days 19.4(全体 58.1);仅 numpy 有限 24,927 对仅引擎有限 262(引擎侧多一层 mas
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:00 [auto] ⚠ 读留出段:final FINAL,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 15:06 [auto] FINAL 跑完(exit 0);重看结果:./scripts/study.sh digest F107_abs_demean_skew_low FINAL

### 2026-10-04 15:16 [执行] R2:FINAL(S_final,5变体)已跑完exit 0,留出段数字已读准写入结果卡

看到了什么(用户口径,utrain→holdout,多头腿净超额):f_orig +1.67%→+1.41%、f_m20 +5.40%→+4.34%、
f_K +15.40%→+14.10%、f_m20K +12.82%→+7.98%、f_m20absret +7.44%→+1.21%。五个候选的 sign(train)与
sign_user(utrain)全部是 -1、完全一致,holdout 没有重新拟合。check 一次通过(41/41),f_m20K 用的是
工单给的第一个写法(cs_rank 版),没有退到 cs_normalize 或 f_m60。f_m20absret 与 gates.g_absidio20
逐字比较完全相同。

两处数字贴近 10_distilled.md 写死的 3pp 门槛,精确值(未四舍五入)已写进结果卡:
判据2(f_m20 − f_orig 的 Lnet,holdout)= +2.9266pp,门槛是 ≥3pp,差一点点没过线;
判据4(f_m20 − f_m20absret,holdout)= +3.1295pp,而 valid 阶段是 f_m20absret 领先 f_m20 6.5pp ——
方向在留出段整个翻了过来。判据0(f_K 自检,Lnet+14.10%/Lshp 1.509)落在预期区间内;
判据3(f_m20K − f_K,holdout)= −6.12pp,清楚不贴线,是"更低"不是"更高"。

意外:f_K 留出段最大回撤比 utrain 深了近 5pp(−9.17%→−14.63%),其余四个候选大多是变浅。
分位剖面(Q1..Q10)、留出段固定半衰期表这次输出里都没有;逐年诊断只有自然年口径(2023 没有按
08-08 拆成上下半),三项都已如实记在结果卡 (D) 节,没有为了补数字新起任何运行。

下一步不是执行的事:留给主研按 10_distilled.md 的判据 0~4 逐条判、写「读完留出段之后」一节。

## 工单与结果卡(`notes/F107_abs_demean_skew_low/orders/`、`notes/F107_abs_demean_skew_low/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

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
- `x1`(自写脚本的输出)  10-04 12:31  exit 0  → `logs/F107_abs_demean_skew_low_x1.log`
- `x2`(自写脚本的输出)  10-04 14:01  exit 0  → `logs/F107_abs_demean_skew_low_x2.log`

## 已写的 notes(`notes/F107_abs_demean_skew_low/`)

`02_operators.md`(2K)、`03_decomposition.md`(2K)、`04_grammar.md`(2K)、`05_hypotheses.md`(19K)、`06_baseline.md`(3K)、`07_S1_parts.md`(12K)、`07_S2_memory.md`(12K)、`07_S_final.md`(10K)、`07x_1_anatomy.md`(10K)、`07x_2_elevate.md`(22K)、`08_variants.md`(6K)、`09_diagnosis.md`(11K)、`10_distilled.md`(17K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(18K)、`state.md`(38K)

## 自写的探针与分析脚本(`studies/F107_abs_demean_skew_low/`)

- `probes.py`  10-03 17:50  Probes this tree needs: abs_(cs_demean(day_skew(Low))).
- `x1_anatomy.py`  10-04 12:16  x1 -- what  abs_(cs_demean(day_skew(Low)))  reads on REAL data, and where its long leg comes from.
- `x2_elevate.py`  10-04 12:44  x2 -- can the long leg of  abs_(cs_demean(day_skew(Low)))  be made better by STRUCTURE (not only by smoothing)

## 结构化结果(`handoff/F107_abs_demean_skew_low/results/`)

(还没有)
