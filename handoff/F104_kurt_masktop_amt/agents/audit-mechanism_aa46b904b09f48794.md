# audit-mechanism:F104_kurt_masktop_amt — agent aa46b904b09f48794(工作流 wf_759ef2d3-03f)

- 状态:**已返回结果**;开始 10-03 23:43,最后一次动作 10-04 00:01;工具调用 35 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F104_kurt_masktop_amt/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-03 23:43 · Bash** — Read CLAUDE.md and size of method docs

```bash
cd /Users/wxy/Desktop/Partura && wc -l CLAUDE.md docs/method.md docs/study_playbook.md && cat CLAUDE.md
```

```
      27 CLAUDE.md
     123 docs/method.md
     181 docs/study_playbook.md
     331 total
# 给接手这个项目的 agent

**读 `docs/method.md` 之前不要开始做研究。** 最容易犯的错是把上一条因子的
`configs/*.yaml` 改个表达式就跑 —— 那不是研究,那是又一次盲搜。

一句话版本:

> 实验计划和探针集合都是**这棵树**的性质,每条表达式都要重新推;
> 唯一跨研究复用的是 `lab/findings.yaml` 里的结论,而且它是**先验**,不是证据。

拿到一条新表达式,按这个顺序走:

1. `partura decompose "<expr>"` —— 先看清楚每个算子的**实现**和**探针实测值**,
   以及实验室里与这棵树相关的既往先验。
2. **想一遍这棵树特有的问题**。内置探针答不上来的,就为这次研究写:
   `studies/<factor_id>/probes.py`,一个探针回答一个问题,声明适用范围,
   写完先在**已知答案的算子**上自检(见 `docs/method.md` §3)。
3. `partura propose "<expr>" --factor-id <fid> --out configs/<fid>.draft.yaml`
   —— 它给的是**候选**。删掉没信息量的,补上只有读了这棵树才想得到的,
   每条 `why` 写成一句可证伪的话;控制变量、门控、诊断项按这棵树的嫌疑挑。
4. `partura run` 训练段 + 验证段,一个阶段回答一个问题,看完结果再决定下一阶段。
5. `--holdout` 只用一次,在最终候选上。
6. `partura report`,然后把**可迁移**的结论写回 `lab/findings.yaml`,
   每条都要写清楚**什么情况下会失效**。

硬规矩:方向只在训练段定一次;所有钱的数字扣 15 bp 并给换手;留出段有台账;
原始结果不覆盖;判据一律实测,不写死名单。
```

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/docs/method.md`

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

**10-03 23:43 · Bash** — List F104 study materials

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F104_kurt_masktop_amt/ runs/F104_kurt_masktop_amt/ studies/F104_kurt_masktop_amt/ 2>&1; wc -l research/alpha_distillation/F104_kurt_masktop_amt.md configs/F104_kurt_masktop_amt.yaml; wc -c notes/F104_kurt_masktop_amt/*.md
```

```
notes/F104_kurt_masktop_amt/:
total 248
drwxr-xr-x@ 23 wxy  staff    736 Oct  3 23:38 .
drwxr-xr-x@ 10 wxy  staff    320 Oct  3 18:37 ..
-rw-r--r--@  1 wxy  staff   1707 Oct  3 23:40 01_expression.md
-rw-r--r--@  1 wxy  staff   5500 Oct  3 23:40 02_operators.md
-rw-r--r--@  1 wxy  staff   2124 Oct  3 19:49 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1652 Oct  3 19:49 04_grammar.md
-rw-r--r--@  1 wxy  staff  11938 Oct  3 23:40 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3071 Oct  3 23:27 06_baseline.md
-rw-r--r--@  1 wxy  staff   3351 Oct  3 23:01 07_S1_mask.md
-rw-r--r--@  1 wxy  staff   3298 Oct  3 23:00 07_S2_resid.md
-rw-r--r--@  1 wxy  staff   5427 Oct  3 23:02 07_S3_reader.md
-rw-r--r--@  1 wxy  staff   5031 Oct  3 23:25 07_S4_long.md
-rw-r--r--@  1 wxy  staff    775 Oct  3 23:40 07_S_final.md
-rw-r--r--@  1 wxy  staff   1989 Oct  3 23:40 07_conditional.md
-rw-r--r--@  1 wxy  staff   1064 Oct  3 23:29 07_controls.md
-rw-r--r--@  1 wxy  staff   3010 Oct  3 23:29 07_neutralise.md
-rw-r--r--@  1 wxy  staff   6731 Oct  3 23:40 07x_anatomy.md
-rw-r--r--@  1 wxy  staff   7776 Oct  3 23:25 07x_longleg.md
-rw-r--r--@  1 wxy  staff   3121 Oct  3 23:40 08_variants.md
-rw-r--r--@  1 wxy  staff   5451 Oct  3 23:39 09_diagnosis.md
-rw-r--r--@  1 wxy  staff   8961 Oct  3 23:39 10_distilled.md
-rw-r--r--@  1 wxy  staff   2792 Oct  3 23:39 11_risks.md
-rw-r--r--@  1 wxy  staff   1309 Oct  3 23:38 12_next.md

runs/F104_kurt_masktop_amt/:
total 1368
drwxr-xr-x@  9 wxy  staff     288 Oct  3 23:33 .
drwxr-xr-x@ 19 wxy  staff     608 Oct  3 17:37 ..
… (22 行略) …
    2124 notes/F104_kurt_masktop_amt/03_decomposition.md
    1652 notes/F104_kurt_masktop_amt/04_grammar.md
   11938 notes/F104_kurt_masktop_amt/05_hypotheses.md
    3071 notes/F104_kurt_masktop_amt/06_baseline.md
    3351 notes/F104_kurt_masktop_amt/07_S1_mask.md
    3298 notes/F104_kurt_masktop_amt/07_S2_resid.md
    5427 notes/F104_kurt_masktop_amt/07_S3_reader.md
    5031 notes/F104_kurt_masktop_amt/07_S4_long.md
     775 notes/F104_kurt_masktop_amt/07_S_final.md
    1989 notes/F104_kurt_masktop_amt/07_conditional.md
    1064 notes/F104_kurt_masktop_amt/07_controls.md
    3010 notes/F104_kurt_masktop_amt/07_neutralise.md
    6731 notes/F104_kurt_masktop_amt/07x_anatomy.md
    7776 notes/F104_kurt_masktop_amt/07x_longleg.md
    3121 notes/F104_kurt_masktop_amt/08_variants.md
    5451 notes/F104_kurt_masktop_amt/09_diagnosis.md
    8961 notes/F104_kurt_masktop_amt/10_distilled.md
    2792 notes/F104_kurt_masktop_amt/11_risks.md
    1309 notes/F104_kurt_masktop_amt/12_next.md
   86078 total
```

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/configs/F104_kurt_masktop_amt.yaml`

**10-03 23:43 · Bash** — Read notes 01-06

```bash
cd /Users/wxy/Desktop/Partura && for f in 01_expression 02_operators 03_decomposition 04_grammar 05_hypotheses 06_baseline; do echo "=================== $f"; cat notes/F104_kurt_masktop_amt/$f.md; done
```

```
=================== 01_expression
这条表达式是挖掘库里的 #4190(GP 搜出来的),用户表里公布的一行是:方向 −1、EMA 半衰期 20、扣费多空夏普 3.20 / 1.89(训练 / 测试)、
多头腿年化毛超额 7.3% / 4.0%。Partura 自己求值后 S0 复现了训练列(方向 −1、半衰期 20、多空 3.20、多头毛超额 7.3%);最后读留出段的那一次,测试列也对上了(1.89、4.0%)。

**一句话**:它量的是「这只股票当天的成交额有多集中在少数几分钟里」(日内成交额的峰度,与「最大一分钟占全天成交额的比例」
的日截面秩相关 0.93),但在取峰度之前,先把每一分钟里全市场成交额最低的 10% 股票的那一格改写成全市场均值 ——
这一步的实际效果是**把峰度与流动性水平的关系翻了过来**(自身峰度与成交额的秩相关 −0.17,过了 mask 之后 +0.11)。
方向为负:成交越是集中爆在少数几分钟的股票,之后越跑输;钱八成在空头腿。

读名字会读错两处:`mask_top…_neg` 改的是**底部** 10%,不是顶部;「替换成均值」不是缩尾,而是把不活跃股票的安静分钟
抬到市场均值的量级。

**研究的结论先放在这里**:mask 实际在做的是「对流动性水平做条件化」;写成显式的截面残差之后(`f_kurt30`),测试段多空 2.13(原式 1.89)、多头腿净超额 +1.4%(原式 −2.1%)。
它是一条空头腿 / 排除型的因子,自己的多头腿做不出来;把流动性水平放回来的排除式合成(`f_exclcv`)测试段多头腿净超额 +12.3%、纯多头夏普 1.26,
但那本多头书的钱是流动性溢价 —— 没有超过只用已知家族的 `cross_mean(day_std(Amt), 30)`(+14.1%、1.51)。

=================== 02_operators
读源码(`study.sh src` + `x1_anatomy.py` 第 0 节打印的服务器端辅助函数)时发现的、算子名字里看不出来的五件事:

1. **`nt_cs_mask_top_replace_mean_neg` 改的是「底部」而不是「顶部」,而且是逐分钟的截面。**
   内核是 `-cs_mask_top_replace_mean(-x)`:先取负、把最大的 10% 换成行均值、再取负 —— 等价于
   **把这一分钟全市场成交额最低的 `ceil(0.1 × 有效股票数)` 只股票,改写成这一分钟的截面均值**。
   NT 面的适配器(`engine.kernels.apply_cube` 的 `spec.face == "nt"` 分支)一天一天地取 (分钟, 股票) 这张面,
   行 = 分钟、列 = 股票,所以「截面」是**同一分钟跨股票**。名字里的 `mask_top` 在 `_neg` 版本里实际是 mask bottom。

2. **替换值是「含被替换者在内的全体有效股票的均值」**(`row_means = nanmean(x_masked)`,探针
   `tie_break_replaced_set` 的自检确认)。成交额在截面上极度右偏,均值远大于中位数,所以对被替换的股票来说
   这是一个**比它自己的水平大一到两个数量级的数**:探针 `replacement_vs_own_level` 在截面对数正态
   σ = 1.0 / 1.5 / 2.0 下测到新值 / 旧值的中位数是 **8.5 / 35.7 / 192 倍**(解析值 exp(σ²/2 + 1.645σ),自检通过)。
   「替换成均值」听上去像缩尾,**实际是往不活跃股票的日内序列里打尖峰**。
… (116 行略) …
   分位剖面 Q1 **−34.1%**、Q2 −9.5%、Q3 −1.8%,Q4~Q9 在 +2.9%~+7.8% 之间近乎平,Q10 +10.6%。这是一个「避开最差 10%」的形状,
   不是一个从头到尾单调的排序。
2. **多头腿扣费之后在 valid 上是负的。** 多头腿净超额 train **+4.8%** / valid **−5.8%**(毛 +10.1% / +0.4%),纯多头夏普 +1.00 / −1.24。
   valid 的剖面里 Q10 只有 +0.6%,Q3~Q9 之间没有次序。用户表公布的是毛超额(7.3%),扣费后的用户口径是 **+1.8%**、纯多头夏普 0.38。
   对一个只能做多的使用者,原式的多头腿基本不可用。
3. **没有平滑就没有这条因子。** 半衰期扫描(train,扣费多空夏普):hl0 **−11.64**(日换手 81%)、hl1 −2.95、hl2 +0.25、hl3 +1.43、
   hl5 +2.51、hl10 +3.45、hl20 **+3.91**(换手 7%)—— 单调改善到可选集合的上界。树里没有任何日轴记忆,
   值钱的是外面那个 EMA 造出来的慢变量;rank IC 随预测期上升(h1 0.0199 → h10 0.0260)也说明它预测的是持续性的漂移。
4. **逐年单调变弱。** 扣费多空夏普 2018 +4.97、2019 +5.24、2020 +3.62、2021 +2.27、2022 +1.63、2023 +1.11;
   多头腿毛超额 2018~2021 在 +7%~+12%,2022 +2.2%,2023 **−2.5%**。valid 的 1.47 不是某几天造成的,是一条向下的趋势。
5. **信号在数值里也在秩里**:train 上 Pearson IC 0.0288(t = 18.9)、rank IC 0.0199(t = 15.4)。Pearson 反而更高 ——
   峰度是重尾量,极端的那几个值本身带信息。(S2 一度把它读成「幅度比名次重要」;S3 的 `r_rankavg30` 把时间尺度的差别排除之后,这个读法基本被否定。)

条件 IC(原始日频面板,train)给了第一条关于结构的线索:按当天成交额分五组,最不活跃的一组 IC +0.0012、最活跃的一组 −0.0338;
按流通市值分组则是小市值更强(−0.0285 → −0.0076)。这条线索被来回读了三次,最后站住的是最初的读法:

- S0 的读法:「信号在活跃股票里,mask 改的那批不活跃股票里没有信号」。
- x1 用平滑后的可交易信号、按「被改写的分钟数」分组重做,读到相反的结论(深度不活跃的一组 IC 最高,见 07x_anatomy 第 6 点)。
- x2 §4 发现「被改写的分钟数」本身混着流动性(桶内集中度与成交额正相关,最高 +0.36);按 30 日成交额分组,集中度信号在**最活跃**的五分之一里最强
  (−0.037,其余 −0.016~−0.026)。逐日面板在不活跃股票里是噪声这一点是对的,但平滑之后它们的信号也只有活跃股票的一半。
```

**10-03 23:43 · Bash** — Read stage notes 07_*

```bash
cd /Users/wxy/Desktop/Partura && for f in 07_S1_mask 07_S2_resid 07_S3_reader 07_S4_long 07_S_final 07_conditional 07_controls 07_neutralise; do echo "=================== $f"; cat notes/F104_kurt_masktop_amt/$f.md; done
```

```
=================== 07_S1_mask
**结果**(train / valid;方向与半衰期在 train 上定)

- `p_noabs`:每一个指标都与原式相同(3.91 / 1.47)。**`abs_` 是空操作(H9 成立)**,从树里删掉;后面的阶段用它当原式的替身。
- `p_nat`(删掉 mask,只留自身峰度):rank IC 0.0131 / **−0.0016**,扣费多空 1.72 / **−1.19**,多头腿净超额 −2.3% / −21.7%。
  valid 的分位剖面两头都是负的(Q1 −13.7%、Q10 −13.0%),逐年 2021 起转负(−0.77、−0.84、−2.02)。
  **mask 不是旁观者(H1 否定)**:没有它,这条因子在 valid 上是反的。
- `p_kfrac`(只留「被改写的分钟占比」):拟合出来的方向是 **+**,扣费多空 0.06 / 2.76,取值离散度 0.05(过不了 0.5 的门槛);
  与 `ctl_amt` 的秩相关 **−0.91**,与原式 −0.12。它就是一个成交额水平代理,不是原式。**mask 也不是 k 的计数器(H2 否定)**,
  与 x1 的结论一致(原式与两点公式的 Spearman 0.157)。
- `p_mirror`(改成改写每分钟最活跃的 10%):0.62 / −3.11,比删掉 mask 还差。被改写的必须是**不活跃**的那一端。
- 三种「不用排名阈值的地板」:

  | | 扣费多空 | 多头腿净超额 | 与 `ctl_amt` 的秩相关 | 与原式的秩相关 |
  |---|---|---|---|---|
  | 原式(`p_noabs`) | 3.91 / 1.47 | +4.8% / −5.8% | +0.14 | 1 |
  | `f_addmed`(每分钟加截面中位数) | **4.42 / 1.52** | +7.0% / −4.7% | +0.15 | 0.62 |
  | `f_floormed`(与截面中位数取 max) | 3.76 / 0.52 | +4.0% / −11.1% | +0.12 | 0.68 |
  | `f_addmean`(每分钟加截面均值) | 3.23 / 0.05 | +0.6% / −20.1% | −0.19 | 0.43 |
  | `p_nat`(无地板) | 1.72 / −1.19 | −2.3% / −21.7% | −0.18 | 0.62 |

**解读**

1. **「地板」这个读法(H10)在 train 上成立、在 valid 上不够。** 三种地板在 train 上都保住了原式的大部分(3.23~4.42),
   说明「恰好是最低 10% 被替换」这个排名结构不是必需的;但 valid 上的结果跟着地板的写法大幅摆动(0.05 / 0.52 / 1.52)。
   地板的高度不是一个稳的参数。
2. **在 valid 上站得住的两个(原式、`f_addmed`),恰好是与成交额水平正相关的两个(+0.14、+0.15);站不住的两个(`p_nat`、`f_addmean`)
   是负相关的(−0.18、−0.19)。** `f_floormed`(+0.12)居中,valid 0.52 —— 所以这只是一条线索,不是判决;
   但它指向的方向很具体:决定 valid 表现的可能不是地板本身,而是它把因子**往流动性的哪一边倾斜**。
3. 中性化表给了直接的证据:自身峰度 `p_nat` 对当天成交额取残差后,rank IC 从 0.0124 升到 **0.0262**,无成本多空夏普从 2.86 升到 **4.79**
… (164 行略) …
对全部 14 个控制变量:R² **0.319**,rank IC 0.0195 → **0.0073**(剩 37%),无成本夏普 4.74 → **2.52**(剩 53%);
空头腿毛超额 33.7% → 4.9%,多头腿 10.5% → 8.2%。

**4. H15(彩票股 / 涨停板 / 量价同向)的判决:部分成立,没有哪一个单独成立。**

| 只对它中性化 | R² | 残差 rank IC | 残差无成本夏普 | 残差空头腿毛超额 |
|---|---|---|---|---|
| (未中性化的 `r_ref30`) | — | 0.0195 | 4.74 | 33.7% |
| `ctl_max30` 过去 30 日最大单日涨幅 | 0.018 | 0.0147 | 3.41 | 23.7% |
| `ctl_pvcorr30` 30 日平均分钟量价相关 | 0.043 | 0.0150 | 3.83 | 21.1% |
| `ctl_retkurt30` 30 日平均分钟收益峰度 | 0.038 | 0.0155 | 3.31 | 19.9% |
| `ctl_ivol` 日内波动 | 0.040 | 0.0120 | 4.07 | 25.1% |
| `ctl_mom20` 20 日动量 | 0.020 | 0.0146 | 3.53 | 20.6% |

每一个都只张成 2%~4%,却各自拿走两到四成的 rank IC 和两成半到四成的空头腿;14 个控制变量合起来拿走 63% 的 rank IC 和 85% 的空头腿。
也就是说:成交最集中的那 10% 股票,同时是最近大涨过、价格有跳、量价同向、波动高的那批 —— 这些特征各自都预示跑输,集中度是它们的一个共同读数,
而不是其中某一个的别名。控制掉全部之后剩下的是一个小得多、偏多头腿的残差(rank IC 0.0073)。

**5. 合成版是流动性因子。** `l_add` 对全部控制变量 R² 0.633(只对 `ctl_amt30` 就有 0.493),`l_addcv` 0.727(`ctl_amt30` 0.451);
对 `ctl_amt30` 中性化后 `l_addcv` 剩下 rank IC 0.0292、无成本夏普 3.66 —— 那就是集中度的部分。
```

**10-03 23:43 · Bash** — Read notes 07x through 12

```bash
cd /Users/wxy/Desktop/Partura && for f in 07x_anatomy 07x_longleg 08_variants 09_diagnosis 10_distilled 11_risks 12_next; do echo "=================== $f"; cat notes/F104_kurt_masktop_amt/$f.md; done
```

```
<persisted-output>
Output too large (35.5KB). Full output saved to: /Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bnbsq8f9m.txt

Preview (first 2KB):
=================== 07x_anatomy
### x1 — 这棵树在真实数据上读到的是什么(`studies/F104_kurt_masktop_amt/x1_anatomy.py`,只用 utrain)

内置诊断回答不了的四个问题,在跑任何阶段之前先量了一遍。合成探针(`probes.py`)对 mask 节点的预言是
「它把被替换的分钟打成几十倍的尖峰,峰度被替换分钟数 k 钉死」;这一节是拿真实数据去核对那个预言 —— 结果是**预言被否定**,
阶段计划因此改写(H10、H11 都是这一节之后才提出来的)。

**(1) `abs_` 是空操作。** 带 / 不带 `abs_` 的两块面板有限值位置完全一致,最大差 2.9e-4(峰度本身是 10 的量级);
只有 48% 的格子逐位相同,是 float32 在不同分块大小下求和顺序不同造成的。

**(2) mask 节点不是「k 的计数器」。** k = 当天被改写的分钟数(241 根里)。

| k | 股票日占比 | 原式中位数 | 自身峰度中位数 | 两点公式预言 | 成交额截面分位 | 次日年化超额 |
|---|---|---|---|---|---|---|
| 0 | 33.6% | 11.12 | 11.12 | — | 0.799 | −10.4% |
| 1 | 6.8% | 11.49 | 11.48 | 236.0 | 0.649 | −1.1% |
| 3–5 | 7.0% | 12.21 | 12.37 | 55.3 | 0.527 | +3.1% |
| 13–30 | 12.7% | 11.64 | 13.82 | 7.1 | 0.349 | +8.2% |
| 61–120 | 11.6% | 8.57 | 17.81 | −1.6 | 0.118 | +9.7% |
| 121–180 | 3.1% | 9.62 | 23.26 | −1.9 | 0.040 | −2.7% |

- 被改写的不是「少数极不活跃的股票」:66% 的股票日至少有一分钟被改写,约四成在 12 分钟以上(逐年 38%~44%)。
- 原式的读数随 k 几乎是平的(11.1 → 12.2 → 8.6),与两点公式的日截面 Spearman 只有 **0.157**;
  而**自身**峰度随 k 从 11 升到 23(k 越大 = 越不活跃 = 成交越断续)。mask 做的事情是把不活跃股票「虚高」的峰度压回来。
- 原因:截面均值 μ(d,m) 自己在日内是 U 形的,被改写的分钟拿到的是**全市场共同的日内成交曲线**的一段,不是一个常数尖峰。
  k ≤ 5 的股票日注入的成交额不到自身的 2%;k ≥ 31 的股票日,(自身+注入)/自身 的中位数是 **3.62**。
- 净效果体现在与流动性的关系上:日截面 Spearman(自身峰度, log 成交额) = **−0.174**,过了 mask 之后 = **+0.110**。
  原式与自身峰度的 Spearman 是 0.630(全部格子)/ 0.470(k>0 的格子)。

**(3) 股票代码顺序没有泄漏进来(H6 否定)。** 零成交分钟只占全部「股票×分钟」的 3.8%~6.9%,低于 10% 的配额,并列的 0 几乎总是
全部被改写。给定「自身零成交分钟数」,k 在列下标前 / 中 / 后三分之一之间没有差别(5~19 个零成交分钟:34.8 / 34.4 / 33.9);
k 与列下标的 Spearman −0.074,原式与列下标 −0.031。

**(4) 自身峰度读的是「最大的那一根」,不是集合竞价(H5 基本否定)。** 在 k=0 的格子上,自身峰度与各个朴素读数的日截面 Spearman:
最大一分钟占比 **0.932**、偏度 **0.986**、变异系数 0.672、首根占比 0.191、末根占比 −0.015。
最大一分钟落在第一根的只有 0.3% 的股票日、落在末根的 3.7%,但落在**开盘后第 2~6 根**的有 29.4% —— 这一条留给 S3 的 `r_kurt_noopen30`。
最大一分钟占比的中位数是 3.24%(均匀分布是 0.41%)。

**(5) 两端十分位里是谁(可交易信号 = EMA-20 的 −原式)。**

| | 次日年化超额 train / valid | 成交额分位 | 换手率分位 | 日内波动分位 | 20 日动量分位 | 「EMA 自身峰度」分位 | 深度不活跃(EMA k ≥ 20)占比 |
|---|---|---|---|---|---|---|---|
...
</persisted-output>
```

10-03 23:43 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bnbsq8f9m.txt`

**10-03 23:43 · Bash** — Read holdout ledger and study.sh

```bash
cd /Users/wxy/Desktop/Partura && cat runs/F104_kurt_masktop_amt/ledger.json; cat scripts/study.sh | head -150
```

```
{
  "entries": [
    {
      "when": "2026-10-03T23:50:53Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:50:53Z",
      "split": "valid",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:50:53Z",
      "split": "utrain",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-04T00:25:35Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
… (255 行略) …
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json";
    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
    ;;
  digest)
    fid=$1; tag=$2; base=${3:-v_base}
    "$PY" scripts/summarize.py "runs/$fid/$tag.json" --base "$base"
    ;;
  report)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.cli report configs/$fid.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'" || exit 1
    mkdir -p research/alpha_distillation
    $RS "$SSH" "$HOST:$R/research/alpha_distillation/$fid.md" research/alpha_distillation/ && wc -l "research/alpha_distillation/$fid.md"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,16p' "$0"; exit 2 ;;
esac
```

**10-03 23:43 · Bash** — Show final run digest

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F104_kurt_masktop_amt final 2>&1 | head -300
```

```
===== F104_kurt_masktop_amt  [final.json]  1942d x 5220s  splits ['train', 'valid', 'utrain', 'holdout', 'full']  fit=train  405.7s  peak anon 4.15G =====

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
f_orig                 -  +0.0199  +0.0100  20  +3.91  +1.47    +10.1%     +0.4%    +4.8%    -5.8%   23%  7.0%  1.00  1.00
f_kurt30               -  +0.0212  +0.0052   1  +3.75  +1.91    +10.5%     +5.6%    +5.4%    +0.3%   24%  6.1%  1.00  1.00
f_cv30                 -  +0.0281  +0.0190   0  +3.77  +2.37     +9.5%     +4.5%    +4.1%    -0.9%   19%  6.2%  1.00  1.00
f_exclcv               -  +0.0408  +0.0538   0  +3.94  +4.44    +19.1%    +23.0%   +15.0%   +19.1%   32%  5.2%  1.00  1.00
f_std30                -  +0.0343  +0.0565   0  +1.87  +3.70    +15.2%    +24.4%   +12.6%   +22.3%   42%  2.9%  1.00  1.00
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):
variant                hl5 LS    Lnet    TO  hl10 LS    Lnet    TO  hl20 LS    Lnet    TO
f_orig                  +2.51   -6.0%   19%    +3.45   +0.3%   12%    +3.91   +4.8%    7%
f_kurt30                +3.35   +5.8%    4%    +3.14   +5.8%    3%    +2.90   +5.8%    2%
f_cv30                  +3.11   +4.5%    3%    +2.72   +4.0%    2%    +2.49   +4.3%    2%
f_exclcv                +3.07  +12.9%    3%    +2.88  +12.5%    2%    +2.67  +10.7%    2%
f_std30                 +1.58  +11.0%    2%    +1.49   +9.8%    2%    +1.30   +8.4%    1%

与用户表同口径(方向/半衰期在 utrain 上定; holdout = 用户的测试段):
variant              sgn  hl  LS utr   LS ho Lgross utr Lgross ho  Lnet utr  Lnet ho Lsharpe utr Lsharpe ho short utr
f_orig                 -  20   +3.20   +1.89      +7.3%     +4.0%     +1.8%    -2.1%       +0.38      -0.39    +31.2%
f_kurt30               -   0   +3.20   +2.13     +10.3%     +9.7%     +2.7%    +1.4%       +0.56      +0.28    +33.8%
f_cv30                 -   0   +3.36   +2.16      +8.1%     +3.4%     +2.7%    -1.8%       +0.60      -0.29    +37.5%
f_exclcv               -   0   +4.06   +3.16     +20.2%    +15.8%    +16.2%   +12.3%       +2.77      +1.26    +38.5%
f_std30                -   0   +2.33   +1.94     +17.8%    +16.2%    +15.4%   +14.1%       +2.22      +1.51    +24.7%
分位超额 f_orig [train] Q1..Q10: -34.1% -9.5% -1.8% +2.9% +5.0% +6.0% +6.8% +6.3% +7.8% +10.6%
分位超额 f_orig [valid] Q1..Q10: -24.7% -2.5% +3.5% +5.3% +4.6% -0.1% +6.3% +4.3% +2.7% +0.6%
分位超额 f_kurt30 [train] Q1..Q10: -34.1% -7.6% +0.1% +2.8% +3.8% +5.8% +5.2% +5.1% +7.9% +11.1%
分位超额 f_kurt30 [valid] Q1..Q10: -24.1% +4.6% +8.6% +5.4% +5.8% +3.0% +0.7% -2.9% -7.0% +5.9%
分位超额 f_cv30 [train] Q1..Q10: -40.6% -10.4% +0.5% +4.4% +5.6% +7.0% +7.0% +7.5% +9.6% +9.4%
分位超额 f_cv30 [valid] Q1..Q10: -31.9% +2.3% +9.5% +8.3% +3.6% +1.8% +0.7% -0.8% +1.7% +4.7%
分位超额 f_exclcv [train] Q1..Q10: -40.6% -12.4% -3.6% +0.8% +2.9% +7.1% +4.7% +9.9% +12.1% +19.2%
分位超额 f_exclcv [valid] Q1..Q10: -35.0% -14.2% -13.3% -6.7% -2.6% +5.0% +11.9% +13.6% +17.3% +23.9%
分位超额 f_std30 [train] Q1..Q10: -21.4% -13.2% -7.8% -2.6% +0.1% +3.7% +5.5% +8.6% +11.4% +15.8%
分位超额 f_std30 [valid] Q1..Q10: -34.1% -24.0% -13.3% -5.1% +0.5% +3.7% +9.6% +15.1% +21.0% +26.6%

中性化 f_orig(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0272  LSgross +5.15  LS +3.91  Lgross +10.1%  short +33.9%  TO 7.0%
  all_controls   R2 0.175  残差 rIC +0.0137  LSgross +2.56  LS -1.68  Lgross +8.9%  short +8.7%  TO 18.9%  (原始日频面板上的 R2 只有 0.089)
  ctl_amt        R2 0.049  残差 rIC +0.0205  LSgross +3.17  LS +1.46  Lgross +8.0%  short +22.8%  TO 11.0%
  ctl_price      R2 0.012  残差 rIC +0.0279  LSgross +5.81  LS +4.44  Lgross +11.1%  short +34.2%  TO 7.1%
  ctl_ivol       R2 0.024  残差 rIC +0.0221  LSgross +5.33  LS +2.45  Lgross +11.4%  short +26.9%  TO 13.7%
  ctl_range      R2 0.013  残差 rIC +0.0239  LSgross +5.38  LS +2.57  Lgross +10.2%  short +30.5%  TO 14.1%
  ctl_rev1       R2 0.004  残差 rIC +0.0275  LSgross +5.53  LS +3.26  Lgross +10.3%  short +34.4%  TO 12.1%
  ctl_mom20      R2 0.008  残差 rIC +0.0244  LSgross +4.45  LS +2.87  Lgross +10.3%  short +25.0%  TO 8.1%
  ctl_dvol20     R2 0.034  残差 rIC +0.0202  LSgross +3.29  LS +1.86  Lgross +8.0%  short +19.8%  TO 8.0%
  ctl_amt30      R2 0.055  残差 rIC +0.0233  LSgross +3.56  LS +2.48  Lgross +7.5%  short +29.6%  TO 7.5%
  ctl_kshare30   R2 0.042  残差 rIC +0.0265  LSgross +4.59  LS +3.46  Lgross +10.4%  short +35.2%  TO 7.5%
  ctl_max30      R2 0.035  残差 rIC +0.0197  LSgross +3.28  LS +1.81  Lgross +7.4%  short +18.9%  TO 7.8%
  ctl_pvcorr30   R2 0.038  残差 rIC +0.0232  LSgross +3.99  LS +2.34  Lgross +9.5%  short +22.4%  TO 8.7%
  ctl_retkurt30  R2 0.018  残差 rIC +0.0249  LSgross +4.59  LS +3.20  Lgross +10.5%  short +25.9%  TO 7.2%
  ctl_cap        R2 0.013  残差 rIC +0.0282  LSgross +5.18  LS +3.98  Lgross +11.8%  short +34.1%  TO 7.0%
  ctl_turnrate   R2 0.031  残差 rIC +0.0195  LSgross +3.30  LS +1.42  Lgross +6.4%  short +20.9%  TO 10.3%

中性化 f_exclcv(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0408  LSgross +4.55  LS +3.94  Lgross +19.1%  short +40.2%  TO 5.2%
  all_controls   R2 0.774  残差 rIC +0.0113  LSgross +1.77  LS -3.92  Lgross +3.3%  short +9.2%  TO 25.9%  (原始日频面板上的 R2 只有 0.774)
  ctl_amt        R2 0.468  残差 rIC +0.0190  LSgross +1.62  LS -3.70  Lgross +5.5%  short +7.1%  TO 27.4%
  ctl_price      R2 0.061  残差 rIC +0.0394  LSgross +4.34  LS +3.63  Lgross +16.3%  short +31.1%  TO 5.1%
  ctl_ivol       R2 0.121  残差 rIC +0.0288  LSgross +4.63  LS +0.08  Lgross +18.1%  short +23.6%  TO 27.1%
  ctl_range      R2 0.089  残差 rIC +0.0308  LSgross +5.07  LS -0.42  Lgross +18.4%  short +27.3%  TO 32.7%
  ctl_rev1       R2 0.010  残差 rIC +0.0415  LSgross +4.82  LS +2.86  Lgross +19.9%  short +40.1%  TO 16.1%
  ctl_mom20      R2 0.029  残差 rIC +0.0357  LSgross +4.02  LS +2.83  Lgross +16.2%  short +27.7%  TO 8.4%
  ctl_dvol20     R2 0.223  残差 rIC +0.0225  LSgross +2.34  LS +1.03  Lgross +15.9%  short +8.6%  TO 9.1%
  ctl_amt30      R2 0.567  残差 rIC +0.0292  LSgross +4.56  LS +3.30  Lgross +13.6%  short +20.5%  TO 6.2%
  ctl_kshare30   R2 0.288  残差 rIC +0.0373  LSgross +5.20  LS +4.33  Lgross +14.9%  short +37.4%  TO 5.8%
  ctl_max30      R2 0.229  残差 rIC +0.0235  LSgross +2.78  LS +1.42  Lgross +10.5%  short +13.3%  TO 7.7%
  ctl_pvcorr30   R2 0.111  残差 rIC +0.0353  LSgross +4.04  LS +2.67  Lgross +18.5%  short +23.8%  TO 9.5%
  ctl_retkurt30  R2 0.003  残差 rIC +0.0408  LSgross +4.49  LS +3.85  Lgross +18.3%  short +39.5%  TO 5.4%
  ctl_cap        R2 0.172  残差 rIC +0.0436  LSgross +3.60  LS +3.03  Lgross +11.5%  short +38.4%  TO 5.3%
  ctl_turnrate   R2 0.111  残差 rIC +0.0281  LSgross +3.28  LS +1.13  Lgross +18.3%  short +15.2%  TO 14.5%

控制变量 / 已知家族自己当因子(同口径):
  ctl_amt           - rIC +0.0419 hl 3  LS +1.03/+3.47  Lgross +9.5%/+23.6%  TO 5.5%
  ctl_price         - rIC +0.0059 hl 1  LS +0.08/+2.09  Lgross +4.8%/+12.1%  TO 1.0%
  ctl_ivol          - rIC +0.0403 hl 10  LS +1.07/+1.85  Lgross -4.2%/+3.2%  TO 4.4%
  ctl_range         - rIC +0.0388 hl 20  LS +0.76/+1.61  Lgross -2.4%/+9.1%  TO 3.4%
  ctl_rev1          - rIC +0.0143 hl 20  LS +1.51/+2.21  Lgross +5.2%/+6.4%  TO 14.3%
  ctl_mom20         - rIC +0.0334 hl 5  LS +1.06/+2.23  Lgross +4.7%/+10.5%  TO 6.9%
  ctl_dvol20        - rIC +0.0456 hl 0  LS +0.80/+1.57  Lgross -3.7%/+5.0%  TO 9.0%
  ctl_amt30         - rIC +0.0288 hl 0  LS +1.20/+3.29  Lgross +10.5%/+23.4%  TO 2.3%
  ctl_kshare30      + rIC +0.0135 hl 0  LS +0.14/+2.71  Lgross +3.0%/+17.8%  TO 2.3%
  ctl_max30         - rIC +0.0452 hl 0  LS +1.43/+1.60  Lgross +0.2%/+8.9%  TO 5.8%
  ctl_pvcorr30      - rIC +0.0234 hl 20  LS +0.61/+0.87  Lgross +0.2%/+1.8%  TO 2.5%
  ctl_retkurt30     - rIC +0.0276 hl 0  LS +2.36/+1.87  Lgross +4.0%/+12.9%  TO 5.2%
  ctl_cap           + rIC +0.0016 hl 20  LS +0.01/-0.94  Lgross +0.9%/-8.8%  TO 0.5%
  ctl_turnrate      - rIC +0.0462 hl 5  LS +1.06/+2.43  Lgross -0.7%/+10.2%  TO 4.0%
  known_amt_max9    - rIC +0.0415 hl 1  LS +1.57/+3.81  Lgross +13.4%/+25.1%  TO 5.4%
  known_stdamt_max9 - rIC +0.0484 hl 0  LS +2.47/+4.44  Lgross +16.9%/+24.9%  TO 8.5%
  known_ivol_max9   - rIC +0.0501 hl 10  LS +1.66/+2.06  Lgross -0.5%/+6.1%  TO 3.5%
  g_burst30         - rIC +0.0212 hl 1  LS +3.75/+1.91  Lgross +10.5%/+5.6%  TO 6.1%
  g_cv30            - rIC +0.0281 hl 0  LS +3.77/+2.37  Lgross +9.5%/+4.5%  TO 6.2%
  g_base_m30        - rIC +0.0237 hl 1  LS +3.25/+1.38  Lgross +7.6%/+1.6%  TO 6.0%

逐年 f_orig: 2018 LS +4.97 Lg +10.6%  2019 LS +5.24 Lg +12.3%  2020 LS +3.62 Lg +7.0%  2021 LS +2.27 Lg +10.4%  2022 LS +1.63 Lg +2.2%  2023 LS +1.45 Lg +1.6%  2024 LS +2.53 Lg +6.2%  2025 LS +1.22 Lg +0.4%

逐年 f_kurt30: 2018 LS +5.03 Lg +14.8%  2019 LS +5.81 Lg +16.5%  2020 LS +3.65 Lg +10.5%  2021 LS +1.62 Lg +5.4%  2022 LS +1.83 Lg +6.4%  2023 LS +2.14 Lg +8.4%  2024 LS +2.21 Lg +10.8%  2025 LS +2.12 Lg +8.1%

逐年 f_cv30: 2018 LS +5.35 Lg +10.6%  2019 LS +6.01 Lg +15.3%  2020 LS +3.61 Lg +7.7%  2021 LS +1.50 Lg +4.4%  2022 LS +2.24 Lg +3.4%  2023 LS +2.60 Lg +5.4%  2024 LS +2.14 Lg +7.4%  2025 LS +2.20 Lg -0.9%

逐年 f_exclcv: 2018 LS +5.65 Lg +28.3%  2019 LS +5.30 Lg +18.8%  2020 LS +3.20 Lg +13.9%  2021 LS +2.60 Lg +15.3%  2022 LS +4.98 Lg +25.7%  2023 LS +4.07 Lg +21.9%  2024 LS +2.59 Lg +11.5%  2025 LS +3.41 Lg +15.7%

逐年 f_std30: 2018 LS +3.01 Lg +20.5%  2019 LS +1.84 Lg +12.8%  2020 LS +0.66 Lg +9.2%  2021 LS +2.18 Lg +18.2%  2022 LS +4.22 Lg +26.7%  2023 LS +3.75 Lg +23.4%  2024 LS +1.45 Lg +11.3%  2025 LS +1.60 Lg +16.6%
衰减 f_cv30 rank IC: h1 +0.0281  h2 +0.0356  h3 +0.0392  h5 +0.0434  h10 +0.0477  h20 +0.0518
衰减 f_exclcv rank IC: h1 +0.0408  h2 +0.0534  h3 +0.0604  h5 +0.0700  h10 +0.0835  h20 +0.0984
```

**10-03 23:46 · Bash** — Print kernel source of key operators

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src nt_cs_mask_top_replace_mean_neg day_kurt cs_regres cs_rank cross_mean pow_3 2>&1 | head -300
```

```
### nt_cs_mask_top_replace_mean_neg  face=nt family=cs category=unary axis=S reduces_m=False lookahead=False kernel=nd_cs.cs_mask_top_replace_mean_neg
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_cs.py:239
@op("nd", "cs", arity=1)
def cs_mask_top_replace_mean_neg(
    x: torch.Tensor, valid_mask: Optional[torch.Tensor] = None, top_ratio: float = 0.1
) -> torch.Tensor:
    """Bottom-band counterpart: replace the *lowest* `top_ratio` fraction
    of each row with that row's mean, via the negate-flip-negate trick.
    """
    return -cs_mask_top_replace_mean(-x, valid_mask, top_ratio)

### day_kurt  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_kurt
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:123
@op("dt", "day", arity=1)
def day_kurt(x: torch.Tensor) -> torch.Tensor:
    return C._kurt(x).unsqueeze(-1)

### cs_regres  face=nd family=cs category=binary axis=S reduces_m=False lookahead=False kernel=nd_cs.cs_regres
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_cs.py:253
@op("nd", "cs", arity=2)
def cs_regres(Y: torch.Tensor, X: torch.Tensor, valid_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
    """Cross-sectional (per-row, across stocks) OLS residual of
    `Y ~ alpha + beta*X`, one independent regression per time step.
    """
    mask = torch.isfinite(X) & torch.isfinite(Y)
    if valid_mask is not None:
        mask = mask & valid_mask

    X_ = torch.where(mask, X, torch.zeros_like(X))
    Y_ = torch.where(mask, Y, torch.zeros_like(Y))
… (11 行略) …

    y_pred = beta * (X - x_mean) + y_mean
    residuals = Y - y_pred
    return torch.where(mask, residuals, torch.full_like(residuals, float("nan")))

### cs_rank  face=nd family=cs category=unary axis=S reduces_m=False lookahead=False kernel=nd_cs.cs_rank
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_cs.py:83
@op("nd", "cs", arity=1)
def cs_rank(x: torch.Tensor, valid_mask: Optional[torch.Tensor] = None, pct: bool = True) -> torch.Tensor:
    return _common_rank(x, valid_mask=valid_mask, pct=pct)

### cross_mean  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_mean
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:222
@op("dt", "cross", arity=1, requires_window=True)
def cross_mean(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), nanmean_last, axis=0)

### pow_3  face=shared family=elementwise category=unary axis=None reduces_m=False lookahead=False kernel=common.pow_
# /root/autodl-tmp/AlphaCube/src/alphacube/catalog.py:148
    ("pow_3", "pow_", lambda f: (lambda x: f(x, 3.0))),
```

**10-03 23:46 · Bash** — Run overview for F104

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python scripts/overview_for.py F104_kurt_masktop_amt 2>&1 | head -150
```

```
== F104_kurt_masktop_amt  (挖掘 #4190; 方向 -1, 半衰期 20) ==
可交易信号(方向 x 面板,按公布的半衰期平滑)在 train 上的日截面 rank 相关:
  本批其他因子: F101(day_shine_retstd) +0.30  F103(#820) +0.30  F105(#25) +0.24  F109(erm_mag_gap_5m_tsm20) +0.20  F107(#613) +0.18  F108(#3264) +0.18
  控制变量:     ctl_amt -0.19  ctl_turnrate -0.16  ctl_dvol20 -0.16  ctl_ivol -0.13  ctl_range -0.09  ctl_price +0.07  ctl_mom20 -0.06  ctl_cap -0.05  ctl_rev1 +0.02
  已知家族:     known_amt_max9 -0.22  known_stdamt_max9 -0.27  known_ivol_max9 -0.17
控制变量能张成它多少(秩空间逐日回归的 R²): 全部 0.125;单个: ctl_amt 0.049  ctl_dvol20 0.034  ctl_turnrate 0.031  ctl_ivol 0.024  ctl_range 0.013  ctl_cap 0.013  ctl_price 0.012  ctl_mom20 0.008  ctl_rev1 0.004
(注意:控制变量的符号没有对齐方向;相关的正负要结合因子方向读。|相关| ≥ 0.95 在 AlphaCube 里算同一因子族。)
```

**10-03 23:46 · Bash** — Read researcher's captured helper sources

```bash
cd /Users/wxy/Desktop/Partura && cat studies/F104_kurt_masktop_amt/x1_sources.log | head -220
```

```
======== 0. helper sources on the SERVER (the `src` tool only shows registered operators) ========
# common._kurt
def _kurt(x: torch.Tensor) -> torch.Tensor:
    x_demeaned = x - x.nanmean(dim=-1, keepdim=True)
    x_var = torch.nanmean(torch.pow(x_demeaned, 2), dim=-1, keepdim=True)
    x_4 = torch.pow(x_demeaned, 4)
    return div(_mean(x_4), torch.pow(_mean(x_var), 2)) - 3

# common.rank
@op("nd", "cs", arity=1)
def rank(x: torch.Tensor, valid_mask: Optional[torch.Tensor] = None, pct: bool = True) -> torch.Tensor:
    """Rank along the last dim (ascending), NaN-safe. `valid_mask` defaults
    to `isfinite(x)` — the old code's crash-prone reliance on a mutable
    module-level `tensor_mask` global has been removed.
    """
    if valid_mask is None:
        valid_mask = torch.isfinite(x)
    x_rank = x.clone()
    # Invalid entries are pushed ABOVE every valid value (not below) so they
    # land at the end of the sort and don't shift valid entries' ranks.
    x_rank[~valid_mask] = torch.finfo(x.dtype).max
    # stable=True: ties keep index order, which is the only tie-break every torch
    # backend agrees on. Without it CPU and GPU hand tied values each other's ranks
    # (a 1/n difference, not an ULP one) and minute data ties constantly -- prices
    # sit on a tick grid, volumes repeat, suspended minutes are zero.
    ranks = (torch.argsort(torch.argsort(x_rank, dim=-1, descending=False, stable=True),
                           dim=-1, stable=True) + 1).to(x.dtype)
    if pct:
        valid_count = valid_mask.sum(dim=-1, keepdim=True).to(x.dtype)
        ranks = torch.where(valid_count > 0, ranks / valid_count, torch.full_like(ranks, float("nan")))
… (42 行略) …

======== 0b. probe self-checks with the SERVER kernels ========
[selfcheck] tie_break_replaced_set     on cs_mask_top_replace_mean       PASS  {'tie_free_changes_exactly_the_extreme_decile': True, 'replacement_is_row_mean_incl_replaced_cells': True}
            value: {'tied_frac_0.05': {'n_tied': 10, 'n_changed': 20, 'n_changed_expected_ceil(0.1n)': 20, 'changed_among_tied': 10, 'which': 'all tied cells'}, 'tied_frac_0.3': {'n_tied': 60, 'n_changed': 20, 'n_changed_expected_ceil(0.1n)': 20, 'changed_among_tied': 20, 'which': 'HIGHEST column index among the tied'}}
[selfcheck] replacement_vs_own_level   on cs_mask_top_replace_mean       PASS  {'lognormal_sigma1.5_expected_ratio': 0.261, 'within_10pct': True, 'changed_frac_is_0.1': True}
            value: {'sigma_1.0': {'changed_frac': 0.1, 'median_new_over_old': 0.319, 'p10_new_over_old': 0.162}, 'sigma_1.5': {'changed_frac': 0.1, 'median_new_over_old': 0.26, 'p10_new_over_old': 0.094}, 'sigma_2.0': {'changed_frac': 0.1, 'median_new_over_old': 0.272, 'p10_new_over_old': 0.07}}
[selfcheck] composite_by_liquidity     on cs_mask_top_replace_mean       PASS  {'untouched_stocks_read_plain_kurt_exactly': True, 'total_overwritten_frac': 0.1}
            value: {'liq_decile_1': {'minutes_overwritten': 0.0, 'tree_kurt_median': 11.14, 'plain_kurt_median': 11.14}, 'liq_decile_2': {'minutes_overwritten': 0.0, 'tree_kurt_median': 9.11, 'plain_kurt_median': 9.11}, 'liq_decile_3': {'minutes_overwritten': 0.0, 'tree_kurt_median': 10.04, 'plain_kurt_median': 10.04}, 'liq_decile_4': {'minutes_overwritten': 0.1, 'tree_kurt_median': 9.71, 'plain_kurt_median': 10.24}, 'liq_decil
… (2805 字符略) …
_decile_10': {'minutes_overwritten': 0.0, 'tree_kurt_median': 10.0, 'plain_kurt_median': 10.0}, 'spearman(tree, plain) over all stocks': 0.542, 'spearman(tree, liquidity level)': 0.538, 'spearman(plain, liquidity level)': -0.015}
[selfcheck] spike_count_response       on day_kurt                       PASS  {'day_kurt_matches_1/(w(1-w))-6': True, 'day_mean_matches_1+w(R-1)': True}
            value: {'R=10,own_noise_sigma=0.8': {0: 9.45, 1: 25.1, 2: 25.61, 5: 19.24, 12: 9.88, 24: 3.83, 60: -0.78, 120: -1.96, 180: -0.59, 217: 5.43, 236: 43.87, 240: 236.0}, 'R=50,own_noise_sigma=0.8': {0: 9.45, 1: 199.93, 2: 106.09, 5: 41.7, 12: 14.89, 24: 5.1, 60: -0.66, 120: -2.0, 180: -0.71, 217: 5.16, 236: 43.24, 240: 236.0}, 'pure_two_point(R=50,no_noise)': {1: 236.004, 2: 115.508, 5: 43.221, 12: 15.136, 24: 5.152, 60: -0.652, 120: -2.0, 180: -0.71, 217: 5.152, 236: 43.221, 240: 236.004}}
[selfcheck] spike_count_response       on day_mean                       PASS  {'day_kurt_matches_1/(w(1-w))-6': True, 'day_mean_matches_1+w(R-1)': True}
            value: {'R=10,own_noise_sigma=0.8': {0: 1.38, 1: 1.43, 2: 1.48, 5: 1.64, 12: 2.0, 24: 2.61, 60: 4.47, 120: 7.54, 180: 10.63, 217: 12.53, 236: 13.51, 240: 13.72}, 'R=50,own_noise_sigma=0.8': {0: 1.38, 1: 1.66, 2: 1.94, 5: 2.78, 12: 4.74, 24: 8.09, 60: 18.18, 120: 34.97, 180: 51.77, 217: 62.13, 236: 67.45, 240: 68.58}, 'pure_two_point(R=50,no_noise)': {1: 1.203, 2: 1.407, 5: 2.017, 12: 3.44, 24: 5.88, 60: 13.199, 120: 25.398, 180: 37.598, 217: 45.12, 236: 48.983, 240: 49.797}}
[guard] container anon is already 31.0 GiB (limit 34.0); not starting a Partura run on top of it
[partura exit 1 2026-10-04_09:41:03]
```

**10-03 23:46 · Bash** — Print more operator sources and list partura package

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src cs_mask_top_replace_mean day_std day_mean day_sum add div cross_max nt_cs_mean 2>&1 | head -200; ls partura/; ls logs | grep F104
```

```
### cs_mask_top_replace_mean  face=nd family=cs category=unary axis=S reduces_m=False lookahead=False kernel=nd_cs.cs_mask_top_replace_mean
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_cs.py:208
@op("nd", "cs", arity=1)
def cs_mask_top_replace_mean(
    x: torch.Tensor, valid_mask: Optional[torch.Tensor] = None, top_ratio: float = 0.1
) -> torch.Tensor:
    """Replace the top `top_ratio` fraction (by value, per row) of each
    row with that row's mean.

    The original implementation used `torch.topk` to find candidate top
    indices and then a Python `for i in range(N)` loop (`N` there is
    actually the number of ROWS/time steps, not stocks — a misleading
    variable name) to build the final replace-mask row by row. Replaced
    here with: rank each row (ascending, valid-aware, via `common.rank`
    with `pct=False`), threshold by `top_ratio`, `torch.where` to
    replace — one vectorized pass, no loop.
    """
    assert 0.0 <= top_ratio <= 1.0
    mask = _valid(x, valid_mask)

    x_masked = torch.where(mask, x, torch.full_like(x, float("nan")))
    row_means = _mean(x_masked).unsqueeze(-1).expand_as(x)

    count = mask.sum(dim=-1, keepdim=True).to(x.dtype)
    n_top = torch.ceil(count * top_ratio)
    integer_rank = _common_rank(x, valid_mask=mask, pct=False)  # ascending, NaN where invalid
    # Top `n_top` largest values per row <=> rank strictly greater than
    # (count - n_top). NaN ranks (invalid entries) never satisfy this.
    top_mask = mask & (integer_rank > (count - n_top))

… (67 行略) …
diagnose.py
guard.py
lab.py
panels.py
probes.py
propose.py
remote_tools.py
report.py
report_legacy.py
runner.py
semantics.py
splits.py
study_tools.py
F104_kurt_masktop_amt_S1_mask.log
F104_kurt_masktop_amt_S2_resid.log
F104_kurt_masktop_amt_S3_reader.log
F104_kurt_masktop_amt_S4_long.log
F104_kurt_masktop_amt_final.log
F104_kurt_masktop_amt_x1.log
F104_kurt_masktop_amt_x2.log
```

**10-03 23:46 · Bash** — Outline of final report headings

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^#\|^##\|^###" research/alpha_distillation/F104_kurt_masktop_amt.md | head -120
```

```
1:# Alpha 研究报告 — F104_kurt_masktop_amt
11:## 1. 原始表达式
32:## 2. 算子的真实语义
36:### `abs_`
44:### `nt_cs_mask_top_replace_mean_neg`
54:### `day_kurt`
84:### 既往研究留下的先验
140:## 3. 数学分解
181:## 4. 结构语法
203:## 5. 竞争性假设
231:## 6. 基线指标
329:## 7. 消融实验
331:### S0_baseline
347:### S1_mask
409:### S2_resid
464:### S3_reader
544:### S4_long
615:### S_final
645:### 中性化(fit 段)
864:### 条件 IC(fit 段)
894:### 控制变量自己当因子(同口径)
928:### x1 — 这棵树在真实数据上读到的是什么(`studies/F104_kurt_masktop_amt/x1_anatomy.py`,只用 utrain)
999:### x2 — 多头腿的解剖(`studies/F104_kurt_masktop_amt/x2_longleg.py`,只用 train / valid;数字来自 `logs/F104_kurt_masktop_amt_x2.log`)
1092:## 8. 语义变体
1188:## 9. 机制诊断
1190:### 已确立的证据(每条后面是它依据的实验)
1214:### 合理但尚未坐实的解读
1222:### 未决
1230:## 10. 蒸馏 / 升华后的候选
1243:### 读留出段之前写下的:候选、理由、预测(只凭 train / valid;这一段在 `study.sh final` 之前定稿,之后没有改过)
1282:### 留出段(20230808–20251231,只读了这一次;方向与半衰期在用户训练段上定)—— 读完之后写的
1328:## 11. 失效模式与风险
1348:## 12. 下一步实验
1361:## 附录 A — 数据段使用台账
1373:## 附录 B — 复现
1376:# S0_baseline: 189.0s, 峰值 anon 3.03 GiB, stages ['S0_baseline']
1377:# S1_mask: 257.8s, 峰值 anon 3.64 GiB, stages ['S1_mask']
1378:# S2_resid: 403.9s, 峰值 anon 3.86 GiB, stages ['S2_resid']
1379:# S3_reader: 568.7s, 峰值 anon 4.67 GiB, stages ['S3_reader']
1380:# S4_long: 490.5s, 峰值 anon 4.56 GiB, stages ['S4_long']
1381:# final: 405.7s, 峰值 anon 4.15 GiB, stages ['S_final']
```

10-03 23:46 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F104_kurt_masktop_amt.md`

10-03 23:46 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F104_kurt_masktop_amt.md`

**10-03 23:47 · Bash** — Inspect final.json top-level structure

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F104_kurt_masktop_amt/final.json'))
print(d.keys())
for k,v in d.items():
    if isinstance(v,(str,int,float)): print(k, v)
    elif isinstance(v,dict): print(k, 'dict', list(v.keys())[:30])
    elif isinstance(v,list): print(k,'list',len(v))
EOF
```

```
dict_keys(['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb'])
factor_id F104_kurt_masktop_amt
config configs/F104_kurt_masktop_amt.yaml
stages list 1
provenance dict ['alphacube_root', 'alphacube_commit', 'alphacube_dirty', 'partura_root', 'partura_commit', 'partura_code_sha', 'store', 'python', 'torch', 'numpy', 'host']
view dict ['days', 'symbols', 'first', 'last', 'warmup_rows']
label dict ['kind', 'horizon', 'buyable']
cost_per_side 0.0015
top_frac 0.1
fit_split train
user_split utrain
rank_by ls
halflives list 7
splits_used list 5
split_dates dict ['train', 'valid', 'utrain', 'holdout', 'full']
results dict ['f_orig', 'f_kurt30', 'f_cv30', 'f_exclcv', 'f_std30']
errors dict []
engine_timings list 0
diagnostics dict ['decay', 'by_year', 'by_year_scope', 'neutralise', 'controls', 'rank_corr_train']
seconds 405.7
peak_anon_gb 4.15
```

**10-03 23:47 · Bash** — Inspect final.json per-variant result fields

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F104_kurt_masktop_amt/final.json'))
r=d['results']
print(list(r['f_exclcv'].keys()))
for vid in r:
    v=r[vid]
    print('=====',vid, v.get('why','')[:300])
    for key in ['user','splits','user_splits','splits_user']:
        if key in v: print(key, json.dumps(v[key],ensure_ascii=False)[:1500])
EOF
```

```
['expr', 'stage', 'why', 'group', 'sign', 'splits', 'distinct', 'books', 'sign_user', 'ic_user', 'ic_holdout', 'books_user', 'profile']
===== f_orig 原式(3 个算子,外加 20 日半衰期的外置平滑)
splits {"train": {"sign": -1.0, "ic": 0.02883933915450076, "icir": 0.6056629524095045, "ic_t": 18.89241293216724, "rank_ic": 0.019889339760500814, "rank_icir": 0.49462563101079493, "rank_ic_t": 15.428831548493902, "ic_pos": 0.7410071942446043, "coverage": 0.6910971715238646, "coverage_labelled": 0.9992075497008869, "n_days": 973}, "valid": {"sign": -1.0, "ic": 0.014089948809343831, "icir": 0.35654893127751514, "ic_t": 7.005075031184416, "rank_ic": 0.009986651330328448, "rank_icir": 0.27240514221580875, "rank_ic_t": 5.351911877186263, "ic_pos": 0.6450777202072538, "coverage": 0.8946648005876163, "coverage_labelled": 0.99953254311404, "n_days": 386}}
===== f_kurt30 提纯(峰度读数,原式的直系):预测留出段多空夏普不比原式低 0.3 以上、多头腿净超额不低于原式;两条都不成立则提纯只在样本内成立
splits {"train": {"sign": -1.0, "ic": 0.019873519882362477, "icir": 0.3013337557847395, "ic_t": 9.399488151021997, "rank_ic": 0.021178081448524743, "rank_icir": 0.25183335804377355, "rank_ic_t": 7.85542482222102, "ic_pos": 0.6372045220966084, "coverage": 0.6910914618059247, "coverage_labelled": 0.999199165513118, "n_days": 973}, "valid": {"sign": -1.0, "ic": 0.00616025463756336, "icir": 0.08522019390566853, "ic_t": 1.6743111537099131, "rank_ic": 0.005175676816372921, "rank_icir": 0.060647400270279254, "rank_ic_t": 1.191532359436276, "ic_pos": 0.5155440414507773, "coverage": 0.8946648005876163, "coverage_labelled": 0.99953254311404, "n_days": 386}}
===== f_cv30 提纯(变异系数读数):预测与 f_kurt30 在 ±0.3 以内 —— 读数不是这条因子的本质;它同时是 f_exclcv 里「只有集中度」的那一半
splits {"train": {"sign": -1.0, "ic": 0.022664364751687153, "icir": 0.3072959288683418, "ic_t": 9.58546590551458, "rank_ic": 0.02812952269002309, "rank_icir": 0.32130954670217354, "rank_ic_t": 10.022591956789592, "ic_pos": 0.6382322713257965, "coverage": 0.6910973684106901, "coverage_labelled": 0.99920783881081, "n_days": 973}, "valid": {"sign": -1.0, "ic": 0.012218445167429547, "icir": 0.14995221265337857, "ic_t": 2.94609353326445, "rank_ic": 0.01901197023166938, "rank_icir": 0.19800187608955744, "rank_ic_t": 3.8901196347804006, "ic_pos": 0.5440414507772021, "coverage": 0.8946648005876163, "coverage_labelled": 0.99953254311404, "n_days": 386}}
===== f_exclcv 事前推荐的升华候选(纯多头用):流动性水平的秩 + 集中度秩的三次方(只罚最集中的一批)。预测留出段多头腿净超额与纯多头夏普都高于原式;两项都不高于原式则升华失败
splits {"train": {"sign": -1.0, "ic": 0.023975243921027466, "icir": 0.26467467457333965, "ic_t": 8.255983339964395, "rank_ic": 0.04080730801207486, "rank_icir": 0.4219293301042504, "rank_ic_t": 13.161219620269296, "ic_pos": 0.5981500513874615, "coverage": 0.6910973684106901, "coverage_labelled": 0.99920783881081, "n_days": 973}, "valid": {"sign": -1.0, "ic": 0.028459310375434223, "icir": 0.3307383943180988, "ic_t": 6.497978439005479, "rank_ic": 0.053820920393534824, "rank_icir": 0.5504232165494234, "rank_ic_t": 10.814100373318752, "ic_pos": 0.6217616580310881, "coverage": 0.8946648005876163, "coverage_labelled": 0.99953254311404, "n_days": 386}}
===== f_std30 已知家族基准(F001 的量写在同一时间尺度上,2 个算子):train / valid 上多头腿净超额最高。f_exclcv 相对它若纯多头夏普低 0.3 以上且多头腿净超额低 3 个点以上,集中度在样本外没有给多头腿加东西
splits {"train": {"sign": -1.0, "ic": 0.00953984227690454, "icir": 0.10757674274343655, "ic_t": 3.355635733903006, "rank_ic": 0.0343093421478664, "rank_icir": 0.2610044483918318, "rank_ic_t": 8.14149816582646, "ic_pos": 0.5416238437821171, "coverage": 0.6910973684106901, "coverage_labelled": 0.99920783881081, "n_days": 973}, "valid": {"sign": -1.0, "ic": 0.02096519638423234, "icir": 0.2338706944871741, "ic_t": 4.594830102583387, "rank_ic": 0.056475720869782836, "rank_icir": 0.44230871482770506, "rank_ic_t": 8.689987439348744, "ic_pos": 0.616580310880829, "coverage": 0.8946648005876163, "coverage_labelled": 0.99953254311404, "n_days": 386}}
```

**10-03 23:47 · Bash** — Print user-口径 books and holdout IC

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F104_kurt_masktop_amt/final.json'))
r=d['results']
for vid in r:
    v=r[vid]
    print('=====',vid)
    print(' sign_user', v['sign_user'])
    print(' ic_user', {k:round(x,4) if isinstance(x,float) else x for k,x in v['ic_user'].items()})
    print(' ic_holdout', {k:round(x,4) if isinstance(x,float) else x for k,x in v['ic_holdout'].items()})
    bu=v['books_user']
    print(' books_user keys', list(bu.keys()))
    for k,x in bu.items():
        if k in ('splits','splits_at_hl_long'):
            for sp,m in x.items():
                print('  ',k,sp, {kk:(round(vv,4) if isinstance(vv,float) else vv) for kk,vv in m.items() if not isinstance(vv,(list,dict))})
        elif not isinstance(x,(list,dict)): print('  ',k,x)
        else: print('  ',k,type(x).__name__, (list(x.keys())[:12] if isinstance(x,dict) else len(x)))
EOF
```

```
===== f_orig
 sign_user -1.0
 ic_user {'sign': -1.0, 'ic': 0.0247, 'icir': 0.5365, 'ic_t': 19.7775, 'rank_ic': 0.0171, 'rank_icir': 0.4324, 'rank_ic_t': 15.9419, 'ic_pos': 0.7138, 'coverage': 0.7489, 'coverage_labelled': 0.9993, 'n_days': 1359}
 ic_holdout {'sign': -1.0, 'ic': 0.0151, 'icir': 0.395, 'ic_t': 9.5205, 'rank_ic': 0.0144, 'rank_icir': 0.3747, 'rank_ic_t': 9.0317, 'ic_pos': 0.6695, 'coverage': 0.9675, 'coverage_labelled': 0.9997, 'n_days': 581}
 books_user keys ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits']
   hl_ls 20.0
   hl_long 20.0
   hl_used 20.0
   rank_by ls
   sweep list 7
   splits utrain {'ls_sharpe': 3.1965, 'ls_ann': 0.1382, 'ls_mdd': -0.0361, 'ls_gross_sharpe': 4.4594, 'ls_turnover': 0.072, 'long_sharpe': 0.3802, 'long_ann': 0.0181, 'long_mdd': -0.1314, 'long_gross_ann': 0.0734, 'long_turnover': 0.0731, 'short_gross_ann': 0.3119, 'long_share': 0.1905, 'n_days': 1359}
   splits holdout {'ls_sharpe': 1.8909, 'ls_ann': 0.0911, 'ls_mdd': -0.0373, 'ls_gross_sharpe': 3.2032, 'ls_turnover': 0.0834, 'long_sharpe': -0.3914, 'long_ann': -0.0214, 'long_mdd': -0.0903, 'long_gross_ann': 0.0404, 'long_turnover': 0.0817, 'short_gross_ann': 0.268, 'long_share': 0.1309, 'n_days': 581}
===== f_kurt30
 sign_user -1.0
 ic_user {'sign': -1.0, 'ic': 0.016, 'icir': 0.2347, 'ic_t': 8.6506, 'rank_ic': 0.0166, 'rank_icir': 0.1962, 'rank_ic_t': 7.2342, 'ic_pos': 0.6026, 'coverage': 0.7489, 'coverage_labelled': 0.9993, 'n_days': 1359}
 ic_holdout {'sign': -1.0, 'ic': 0.0087, 'icir': 0.1228, 'ic_t': 2.961, 'rank_ic': 0.0143, 'rank_icir': 0.1719, 'rank_ic_t': 4.1437, 'ic_pos': 0.5473, 'coverage': 0.9674, 'coverage_labelled': 0.9997, 'n_days': 581}
 books_user keys ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
   hl_ls 0.0
   hl_long 2.0
   hl_used 0.0
   rank_by ls
   sweep list 7
   splits utrain {'ls_sharpe': 3.1989, 'ls_ann': 0.1553, 'ls_mdd': -0.0607, 'ls_gross_sharpe': 4.547, 'ls_turnover': 0.0864, 'long_sharpe': 0.5607, 'long_ann': 0.0273, 'long_mdd': -0.1148, 'long_gross_ann': 0.103, 'long_turnover': 0.1001, 'short_gross_ann': 0.3383, 'long_share': 0.2334, 'n_days': 1359}
   splits holdout {'ls_sharpe': 2.1339, 'ls_ann': 0.1212, 'ls_mdd': -0.0557, 'ls_gross_sharpe': 3.3587, 'ls_turnover': 0.0919, 'long_sharpe': 0.2844, 'long_ann': 0.0136, 'long_mdd': -0.045, 'long_gross_ann': 0.097, 'long_turnover': 0.1102, 'short_gross_ann': 0.2843, 'long_share': 0.2544, 'n_days': 581}
   splits_at_hl_long utrain {'ls_sharpe': 3.1594, 'ls_ann': 0.15, 'ls_mdd': -0.0604, 'ls_gross_sharpe': 3.9576, 'ls_turnover': 0.0501, 'long_sharpe': 0.8863, 'long_ann': 0.0436, 'long_mdd': -0.1007, 'long_gross_ann': 0.0848, 'long_turnover': 0.0544, 'short_gross_ann': 0.2909, 'long_share': 0.2257, 'n_days': 1359}
   splits_at_hl_long holdout {'ls_sharpe': 1.9723, 'ls_ann': 0.1093, 'ls_mdd': -0.0504, 'ls_gross_sharpe': 2.6787, 'ls_turnover': 0.0517, 'long_sharpe': 0.7898, 'long_ann': 0.0391, 'long_mdd': -0.0395, 'long_gross_ann': 0.0833, 'long_turnover': 0.0584, 'short_gross_ann': 0.2136, 'long_share': 0.2804, 'n_days': 581}
===== f_cv30
 sign_user -1.0
 ic_user {'sign': -1.0, 'ic': 0.0197, 'icir': 0.2586, 'ic_t': 9.5325, 'rank_ic': 0.0255, 'rank_icir': 0.2834, 'rank_ic_t': 10.4464, 'ic_pos': 0.6115, 'coverage': 0.7489, 'coverage_labelled': 0.9993, 'n_day
… (1089 字符略) …
g_mdd': -0.0731, 'long_gross_ann': 0.1916, 'long_turnover': 0.0397, 'short_gross_ann': 0.3485, 'long_share': 0.3548, 'n_days': 1359}
   splits_at_hl_long holdout {'ls_sharpe': 3.045, 'ls_ann': 0.2198, 'ls_mdd': -0.0648, 'ls_gross_sharpe': 3.418, 'ls_turnover': 0.0357, 'long_sharpe': 1.2402, 'long_ann': 0.1209, 'long_mdd': -0.186, 'long_gross_ann': 0.1475, 'long_turnover': 0.0352, 'short_gross_ann': 0.3459, 'long_share': 0.299, 'n_days': 581}
===== f_std30
 sign_user -1.0
 ic_user {'sign': -1.0, 'ic': 0.0128, 'icir': 0.1435, 'ic_t': 5.2895, 'rank_ic': 0.0406, 'rank_icir': 0.3105, 'rank_ic_t': 11.4464, 'ic_pos': 0.5629, 'coverage': 0.7489, 'coverage_labelled': 0.9993, 'n_days': 1359}
 ic_holdout {'sign': -1.0, 'ic': 0.0155, 'icir': 0.1626, 'ic_t': 3.9194, 'rank_ic': 0.0503, 'rank_icir': 0.3193, 'rank_ic_t': 7.6961, 'ic_pos': 0.5852, 'coverage': 0.9675, 'coverage_labelled': 0.9997, 'n_days': 581}
 books_user keys ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits']
   hl_ls 0.0
   hl_long 0.0
   hl_used 0.0
   rank_by ls
   sweep list 7
   splits utrain {'ls_sharpe': 2.3343, 'ls_ann': 0.192, 'ls_mdd': -0.1195, 'ls_gross_sharpe': 2.5869, 'ls_turnover': 0.0274, 'long_sharpe': 2.2242, 'long_ann': 0.154, 'long_mdd': -0.0917, 'long_gross_ann': 0.1781, 'long_turnover': 0.0319, 'short_gross_ann': 0.2473, 'long_share': 0.4187, 'n_days': 1359}
   splits holdout {'ls_sharpe': 1.9422, 'ls_ann': 0.1869, 'ls_mdd': -0.1103, 'ls_gross_sharpe': 2.1391, 'ls_turnover': 0.0251, 'long_sharpe': 1.5086, 'long_ann': 0.141, 'long_mdd': -0.1463, 'long_gross_ann': 0.1624, 'long_turnover': 0.0283, 'short_gross_ann': 0.2493, 'long_share': 0.3945, 'n_days': 581}
```

**10-03 23:47 · Bash** — Read study_tools API

```bash
cd /Users/wxy/Desktop/Partura && wc -l partura/study_tools.py && sed -n 1,400p partura/study_tools.py
```

```
     131 partura/study_tools.py
"""What a study's own analysis script needs, in one import.

A study often has a question no stock diagnostic answers -- "is the signal
only there on days the stock hit its limit?", "does the long leg survive if
the top 1% of names is dropped?".  Those analyses live in
``studies/<factor_id>/*.py`` and run on the server through
``scripts/study.sh exec``.  This module gives them the same panels, label,
splits and safety rails the runner uses, so a bespoke number is comparable
with a table number and cannot take the server down:

    from partura.study_tools import Study
    with Study("F107_abs_demean_skew_low") as st:
        p = st.panels({"x": "day_skew(Low)"})["x"]            # cached, GPU-locked
        tr = st.slice("train")
        print(st.books(p, fit="train", evals=("train", "valid")))

Never read ``holdout`` here: the holdout is read once, by the runner, with
``--holdout``, and that read is ledgered.  ``Study.slice("holdout")`` refuses.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, Optional, Sequence

from . import guard

guard.limit_threads(2)
… (82 行略) …
        s = self.slice(split)
        p = np.asarray(panel[s], dtype=np.float64)
        return dg.ic_row(p, self.target()[s], sign=self.sign(panel) if sign is None else sign)

    def books(self, panel: np.ndarray, fit: str = "train", evals: Sequence[str] = ("train", "valid"),
              sign: Optional[float] = None) -> Dict[str, object]:
        """Decile L/S and the long leg, in the user's convention (see partura.books)."""
        sg = self.sign(panel, fit) if sign is None else sign
        return bk.books(sg * np.asarray(panel, dtype=np.float64), self.target(), self.slice(fit),
                        {e: self.slice(e) for e in evals},
                        cost=float(self.cfg.get("cost_per_side", bk.COST)),
                        top_frac=float(self.cfg.get("top_frac", bk.TOP_FRAC)),
                        rank_by=self.cfg.get("rank_by", "ls"))

    def rank_corr(self, a: np.ndarray, b: np.ndarray, split: str = "train") -> float:
        s = self.slice(split)
        return dg.pair_rank_corr(a[s], b[s])


__all__ = ["Study", "bk", "dg"]
```

10-03 23:47 · 读 `/Users/wxy/Desktop/Partura/studies/F104_kurt_masktop_amt/x2_longleg.py`

**10-03 23:47 · Bash** — Read x2 log output

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F104_kurt_masktop_amt_x2.log | head -150
```

```
[panels] 5 new expression(s) on 1942d x 5220s (+0 warm-up), device=cuda, batches of 3
[panels] GPU: 7.9 GiB free of 31.4; this run capped at 12% (3.9 GiB), chunk 334 MiB
[panels]   3/5 (19s)
[panels] GPU: 7.8 GiB free of 31.4; this run capped at 12% (3.8 GiB), chunk 327 MiB
[panels]   5/5 (47s)
[panels] done in 47s

======== 1. neighbourhood of l_excl (train/valid; sign and half-life fitted on train) ========
self-check -- the stage tables say: bk (= r_ref30) hl 1 LS +3.75/+1.91 Lnet +5.4%/+0.3%;  excl (= l_excl) hl 0 LS +3.52/+3.96 Lnet +13.1%/+16.7%
bk         sgn -1 hl   1  LS +3.75/+1.91  Lgross +10.5%/+5.6%  Lnet +5.4%/+0.3%  Lsharpe +1.08/+0.06  short +33.7%/+23.3%  TO 6.1%  dist 1.00
excl       sgn -1 hl   0  LS +3.52/+3.96  Lgross +18.4%/+22.2%  Lnet +13.1%/+16.7%  Lsharpe +2.20/+3.11  short +34.9%/+30.0%  TO 6.8%  dist 1.00
excl_p2    sgn -1 hl   0  LS +3.38/+3.73  Lgross +18.0%/+20.1%  Lnet +12.2%/+14.0%  Lsharpe +2.14/+2.79  short +34.2%/+30.5%  TO 7.2%  dist 1.00
excl_p6    sgn -1 hl   0  LS +3.54/+4.32  Lgross +17.6%/+25.3%  Lnet +13.5%/+20.9%  Lsharpe +2.07/+3.49  short +35.3%/+30.0%  TO 6.2%  dist 1.00
excl_cv    sgn -1 hl   0  LS +3.94/+4.44  Lgross +19.1%/+23.0%  Lnet +15.0%/+19.1%  Lsharpe +2.50/+3.55  short +40.2%/+34.5%  TO 5.2%  dist 1.00
excl_std   sgn -1 hl   0  LS +3.88/+3.99  Lgross +18.6%/+21.8%  Lnet +13.4%/+16.2%  Lsharpe +2.27/+3.08  short +38.2%/+30.3%  TO 6.8%  dist 1.00
excl_60    sgn -1 hl   0  LS +3.37/+3.72  Lgross +16.9%/+19.6%  Lnet +13.5%/+16.3%  Lsharpe +2.33/+2.92  short +29.8%/+26.4%  TO 4.4%  dist 1.00

======== 2. rank correlation of the TRADED signals (sign x panel, EMA at the fitted half-life) ========
[train]     base      bk      bc    excl   addcv   std30    f001   amt30
    base     1.00    0.52    0.31    0.46    0.37    0.26    0.27    0.20
      bk     0.52    1.00    0.78    0.55    0.53    0.08    0.12   -0.05
      bc     0.31    0.78    1.00    0.38    0.64    0.04    0.09   -0.12
    excl     0.46    0.55    0.38    1.00    0.86    0.83    0.75    0.76
   addcv     0.37    0.53    0.64    0.86    1.00    0.77    0.71    0.67
   std30     0.26    0.08    0.04    0.83    0.77    1.00    0.87    0.98
    f001     0.27    0.12    0.09    0.75    0.71    0.87    1.00    0.84
   amt30     0.20   -0.05   -0.12    0.76    0.67    0.98    0.84    1.00
[valid]     base      bk      bc    excl   addcv   std30    f001   amt30
    base     1.00    0.58    0.34    0.36    0.26    0.11    0.13    0.04
      bk     0.58    1.00    0.69    0.55    0.45    0.06    0.10   -0.05
… (87 行略) …
      bk      0.45    0.36                   0.810           0.04          0.11           0.08         11.3%
      bc      0.49    0.49                   0.971           0.01          0.06           0.04          9.4%
    excl      0.12    0.26                   0.258           0.42          0.48           0.52         18.9%
   addcv      0.24    0.31                   0.411           0.16          0.27           0.26         16.9%
   std30      0.06    0.26                   0.179           0.86          0.66           1.00         15.8%
    f001      0.10    0.26                   0.182           0.61          1.00           0.66         17.6%
   amt30      0.05    0.27                   0.175           1.00          0.61           0.86         10.9%
[valid] universe median daily Amt = 7.443e+07 (raw units)
          rk amt30  rk cap  med Amt / universe med  in amt30 long  in f001 long  in std30 long  gross excess
    base      0.53    0.56                   1.295           0.19          0.15           0.17          0.6%
      bk      0.45    0.42                   0.819           0.04          0.10           0.07          6.1%
      bc      0.48    0.57                   0.942           0.02          0.07           0.04          4.6%
    excl      0.12    0.24                   0.274           0.40          0.46           0.47         23.7%
   addcv      0.23    0.36                   0.422           0.16          0.27           0.24         16.9%
   std30      0.05    0.20                   0.185           0.89          0.69           1.00         27.0%
    f001      0.09    0.21                   0.188           0.65          1.00           0.69         27.3%
   amt30      0.05    0.20                   0.183           1.00          0.65           0.89         25.6%

[x2 done]
[partura exit 0 2026-10-04_14:20:57]
```

**10-03 23:48 · Bash** — List function signatures in diagnose, books, panels

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^def \|^class \|^    def " partura/diagnose.py partura/books.py partura/panels.py
```

```
partura/books.py:48:def stats(net: np.ndarray) -> Dict[str, float]:
partura/books.py:58:def long_book(w: np.ndarray, sig: np.ndarray, target: np.ndarray, cost: float = COST):
partura/books.py:70:def short_leg_excess(w: np.ndarray, sig: np.ndarray, target: np.ndarray) -> np.ndarray:
partura/books.py:81:def smoothed(sig: np.ndarray, halflife: float) -> np.ndarray:
partura/books.py:85:def fit_halflives(sig: np.ndarray, target: np.ndarray, fit: slice, cost: float = COST,
partura/books.py:106:def book_row(sm: np.ndarray, target: np.ndarray, days: slice, cost: float = COST,
partura/books.py:129:def books(sig: np.ndarray, target: np.ndarray, fit: slice, evals: Dict[str, slice], *,
partura/books.py:146:def quantile_profile(sm: np.ndarray, target: np.ndarray, days: slice, n: int = 10) -> List[Dict[str, float]]:
partura/diagnose.py:42:def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
partura/diagnose.py:64:def rank_rows(x: np.ndarray) -> np.ndarray:
partura/diagnose.py:79:def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
partura/diagnose.py:83:def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
partura/diagnose.py:95:def _ir(x: np.ndarray) -> float:
partura/diagnose.py:100:def _tstat(x: np.ndarray) -> float:
partura/diagnose.py:105:def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
partura/diagnose.py:113:def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
partura/diagnose.py:136:def distinct_fraction(panel: np.ndarray, step: int = 5, min_names: int = 30) -> float:
partura/diagnose.py:149:def metric_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
partura/diagnose.py:162:    def curve(v: np.ndarray) -> Tuple[float, float]:
partura/diagnose.py:190:def _zrank(x: np.ndarray) -> np.ndarray:
partura/diagnose.py:197:def neutralise(panel: np.ndarray, controls: Dict[str, np.ndarray], space: str = "rank",
partura/diagnose.py:244:def conditional_ic(panel: np.ndarray, target: np.ndarray, gate: np.ndarray, buckets: int = 5,
partura/diagnose.py:271:def decay(panel: np.ndarray, targets: Dict[int, np.ndarray], sign: float = 1.0) -> List[Dict[str, float]]:
partura/diagnose.py:280:def by_year(panel: np.ndarray, target: np.ndarray, years: np.ndarray, *, sign: float = 1.0,
partura/diagnose.py:299:def extreme_day_dependence(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
partura/diagnose.py:318:def smoothing_sweep(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
partura/diagnose.py:341:def pair_rank_corr(a: np.ndarray, b: np.ndarray) -> float:
partura/diagnose.py:347:def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
partura/panels.py:50:def parse_research(src: str, n_minutes: int = 241):
partura/panels.py:60:def _drop_page_cache(path: Path) -> None:
partura/panels.py:71:def _atomic_save(path: Path, arr: np.ndarray) -> None:
partura/panels.py:77:def auto_gpu_fraction(reserve_gb: Optional[float] = None, hi: Optional[float] = None, lo: float = 0.03) -> float:
partura/panels.py:96:def _is_oom(msg: Optional[str]) -> bool:
partura/panels.py:100:class PanelSet:
partura/panels.py:101:    def __init__(self, store_path: str, start: str, end: str, *, warmup: int = 60,
partura/panels.py:143:    def _chunk_for(fraction: float) -> int:
partura/panels.py:147:    def _refresh_gpu_cap(self) -> None:
partura/panels.py:164:    def view_id(self) -> str:
partura/panels.py:168:    def _cache_path(self, expr_key: str) -> Optional[Path]:
partura/panels.py:175:    def target(self, horizon: int = 1) -> np.ndarray:
partura/panels.py:203:    def external(self, path: str) -> np.ndarray:
partura/panels.py:214:    def _engine(self, device: str, chunk_bytes: Optional[int] = None) -> CubeEngine:
partura/panels.py:230:    def _evaluate(self, exprs: List[object], names: List[str]) -> Tuple[List[Optional[np.ndarray]], Dict[int, str]]:
partura/panels.py:267:    def compute(self, expressions: Dict[str, str]) -> Dict[str, np.ndarray]:
partura/panels.py:351:    def split_slice(self, split: str) -> slice:
```

**10-03 23:48 · Bash** — Read books.py and key diagnose/panels functions

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1,160p partura/books.py && sed -n 60,135p partura/diagnose.py && sed -n 186,245p partura/diagnose.py && sed -n 170,205p partura/panels.py
```

```
"""The tradable-book metrics, in exactly the convention the user's tables use.

AlphaCube's current single-factor ranking (``scripts/pick_single_factors.py``)
judges a factor by two books built from a causally EMA-smoothed signal:

* a **decile long/short book** (gross 1), after 15 bp per unit turnover, and
* a **pure long book**: the long leg of that same decile book rescaled to
  weight 1, minus the equal-weight return of every stock that has both a
  signal and a label that day.  A holding whose label is missing (it opened
  locked at limit-up and could not have been bought) earns 0.

The half-life is chosen from {0, 1, 2, 3, 5, 10, 20} on the FIT period only,
by that book's own after-cost Sharpe, and then held fixed.

``stats`` and ``long_book`` are vendored from that script rather than imported
(the script lives in another session's working tree and changes under us); the
vendoring is guarded by a reproduction check against the user's published
table (``scripts/reproduce_table.py``), which is the only thing that makes a
Partura number comparable with one of theirs.

On top of that convention this module adds the two views a distillation needs:

* ``leg_anatomy`` -- how much of the spread is the long leg and how much is the
  short leg.  In A-shares the short leg cannot be traded, and a book whose
  spread is 80% short leg is a different object from one that is 80% long leg
  even when the two Sharpe ratios agree.
* ``quantile_profile`` -- mean next-day excess by signal quantile.  A decile
  book assumes "more signal is better"; the profile says whether that is true.
"""

… (282 行略) …
                # Same rule as Label(buyable=True) -- a name that opens locked at
                # limit-up on the entry day cannot be bought, so its label is
                # dropped -- but the lock table is read once, not once per horizon
                # (it scans the opening window of every day; five extra horizons
                # used to cost five extra scans).  The runner still checks the
                # h=1 result against the user's own label file, cell for cell.
                if self._locks is None:
                    from alphacube.tradability import entry_locks
                    self._locks = entry_locks(self.view)[0]
                lag = 1
                full[:-lag][self._locks[lag:]] = np.nan
            t = np.asarray(full[self.trim:], dtype=np.float64)
            self._targets[horizon] = t
            if p is not None:
                _atomic_save(p, t)
        return self._targets[horizon]

    def external(self, path: str) -> np.ndarray:
        """A (n_days, n_symbols) panel somebody else computed (market cap, a
        library panel).  Shape is checked; alignment is the caller's claim."""
```

**10-03 23:48 · Bash** — Locate local AlphaCube copy

```bash
cd /Users/wxy/Desktop/Partura && cat partura/bridge.py | head -60; ls ~/Desktop/AlphaCube/src/alphacube/ 2>/dev/null | head -40
```

```
"""Locate and import AlphaCube, and record exactly which version was used.

Partura never reimplements AlphaCube's store, parser, engine, label or
backtest primitives -- it imports them.  The only thing this module adds is
provenance: every Partura artefact carries the AlphaCube commit, the store
path and the library versions it was produced with, so a number in a report
can always be traced back to the code that made it.
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional

PARTURA_ROOT = Path(__file__).resolve().parents[1]


def alphacube_root() -> Path:
    """`$ALPHACUBE_ROOT`, else the sibling directory of the Partura checkout."""
    env = os.environ.get("ALPHACUBE_ROOT")
    cands = [Path(env)] if env else []
    cands += [PARTURA_ROOT.parent / "AlphaCube", Path.home() / "Desktop" / "AlphaCube",
              Path("/root/autodl-tmp/AlphaCube")]
    for c in cands:
        if (c / "src" / "alphacube" / "__init__.py").is_file():
            return c.resolve()
… (36 行略) …
cli.py
combine
daily.py
engine
execution
expression.py
fullcatalog.py
label.py
legacy
metrics.py
mining
models
operators
parser.py
pipeline.py
portfolio
research.py
store.py
synthetic.py
tradability.py
```

**10-03 23:48 · Bash** — Read local AlphaCube metrics helpers

```bash
cd ~/Desktop/AlphaCube/src/alphacube && grep -n "def long_short_weights" -A 40 metrics.py | head -80; grep -n "def portfolio_returns" -A 30 metrics.py | head -50; grep -n "def ema_rows" -A 25 metrics.py | head -40
```

```
282:def long_short_weights(alpha: np.ndarray, top_frac: float) -> np.ndarray:
283-    """(D, S) alpha -> (D, S) target weights: equal-weight long the top ``top_frac``,
284-    short the bottom, gross exposure 1 (so +0.5 long / -0.5 short) and net 0.
285-    Days with too few names are all-zero rather than NaN, so a gap in the alpha
286-    means "hold nothing", not "hold the previous book forever".
287-
288-    Ties at a boundary go by symbol order (a stable sort). numpy's default sort
289-    is not stable, and which of the tied names it put in the book depended on
290-    the rest of the row: nudging one mid-ranked name changed the book in 12 of
291-    200 tied rows, i.e. turnover charged for trades nobody would make. With
292-    turnover now part of the GP fitness (``rank_ic_turnover`` builds the same
293-    book in torch) that noise would also have been selected against."""
294-    alpha = np.asarray(alpha, dtype=np.float64)
295-    D, S = alpha.shape
296-    fin = np.isfinite(alpha)
297-    n = fin.sum(axis=1)
298-    order = np.argsort(np.where(fin, alpha, np.inf), axis=1, kind="stable")     # non-finite last
299-    k = np.maximum(1, np.floor(n * top_frac).astype(np.int64))
300-    pos = np.arange(S)[None, :]
301-    ok = (n >= 2)[:, None]
302-    long_ = ok & (pos >= (n - k)[:, None]) & (pos < n[:, None])
303-    short = ok & (pos < k[:, None])
304-    w_sorted = np.where(long_, 0.5 / k[:, None], np.where(short, -0.5 / k[:, None], 0.0))
305-    w = np.zeros((D, S), dtype=np.float64)
306-    np.put_along_axis(w, order, w_sorted, axis=1)
307-    return w
308-
309-
310-def apply_turnover_cap(target: np.ndarray, cap: Optional[float]) -> np.ndarray:
311-    """Walk the book forward, never trading more than ``cap`` in a day.
… (48 行略) …
221-    if halflife <= 0:
222-        return x
223-    a = 1.0 - 0.5 ** (1.0 / float(halflife))
224-    out = np.full_like(x, np.nan)
225-    state = np.full(x.shape[1], np.nan)
226-    for t in range(x.shape[0]):
227-        row = x[t]
228-        fin = np.isfinite(row)
229-        fresh = fin & ~np.isfinite(state)
230-        state = np.where(fresh, row, state)
231-        upd = fin & ~fresh
232-        state[upd] = a * row[upd] + (1.0 - a) * state[upd]
233-        out[t, fin] = state[fin]
234-    return out
235-
236-
237-def sampled_abs_corr(a: np.ndarray, b: np.ndarray, sample_days: int = 250) -> float:
238-    D = a.shape[0]
239-    idx = np.linspace(0, D - 1, num=min(sample_days, D)).astype(int)
240-    x, y = a[idx].reshape(-1), b[idx].reshape(-1)
```

**10-03 23:49 · Bash** — Read PanelSet init and check server status

```bash
cd /Users/wxy/Desktop/Partura && sed -n 100,170p partura/panels.py && sed -n 345,365p partura/panels.py && cat partura/splits.py | head -40 && grep -n "status" -A3 scripts/study.sh | head -5 && ./scripts/study.sh status
```

```
class PanelSet:
    def __init__(self, store_path: str, start: str, end: str, *, warmup: int = 60,
                 device: str = "cpu", chunk_symbols: Optional[int] = None, chunk_days: Optional[int] = None,
                 cache_dir: Optional[str] = None, mirror_root: Optional[str] = None,
                 max_symbols: Optional[int] = None, gpu_fraction: Optional[float] = None,
                 torch_threads: Optional[int] = None, workdir: Optional[str] = None,
                 label_kind: str = "open_vwap15", label_buyable: bool = False,
                 batch: int = 4, cpu_fallback: bool = False, chunk_bytes: Optional[int] = None,
                 quiet: bool = False) -> None:
        # gpu_fraction None / 0 / "auto" = follow what is free on the card (the default on the server)
        self.auto_fraction = device.startswith("cuda") and (gpu_fraction in (None, 0, 0.0, "auto"))
        self.gpu_fraction = None if self.auto_fraction else gpu_fraction
        self._user_chunk_bytes = chunk_bytes
        if device.startswith("cuda"):
            f = auto_gpu_fraction() if self.auto_fraction else float(gpu_fraction)
            torch.cuda.set_per_process_memory_fraction(f)
            self.gpu_fraction = f
        self.store_path = store_path
        self.store = open_cube_store(store_path, mirror_root=mirror_root)
        self.view, self.trim = warmed_view(self.store, start, end, warmup, max_symbols=max_symbols)
        self.start, self.end, self.warmup = start, end, warmup
        self.device, self.chunk_symbols, self.chunk_days = device, chunk_symbols, chunk_days
        self.torch_threads, self.workdir = torch_threads, workdir
        self.label_kind, self.label_buyable = label_kind, bool(label_buyable)
        self.batch, self.cpu_fallback = max(1, int(batch)), bool(cpu_fallback)
        if chunk_bytes is None and device.startswith("cuda"):
            chunk_bytes = self._chunk_for(self.gpu_fraction)
        self.chunk_bytes = chunk_bytes
        self.quiet = quiet
        self.dates: List[str] = list(self.view.dates[self.trim:])
… (92 行略) …


@dataclass
class LedgerEntry:
    when: str
    split: str
17:#   study.sh status                        what Partura jobs are on the server right now
18-set -u
19-cd "$(dirname "$0")/.."
20-PY=${PY:-$HOME/.venvs/alphacube/bin/python}
--
	555038.pt_F103_audit1	(10/04/26 14:47:41)	(Detached)
	554862.pt_F102_rev1	(10/04/26 14:46:53)	(Detached)
	554070.pt_F105_rev1	(10/04/26 14:42:24)	(Detached)

540353, 30176 MiB
554072, 860 MiB
554865, 862 MiB
container anon 15.1 GiB
gpu.lock slot0.lock slot1.lock slot2.lock
```

**10-03 23:50 · 写文件** `/Users/wxy/Desktop/Partura/studies/F104_kurt_masktop_amt/audit_span.py`(12266 字符)

**10-03 23:50 · Bash** — Syntax-check and launch the audit script on the server

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python -c "import ast,sys; ast.parse(open('studies/F104_kurt_masktop_amt/audit_span.py').read()); print('syntax ok')" && ./scripts/study.sh exec F104_kurt_masktop_amt audit1 audit_span.py
```

```
syntax ok
started F104_kurt_masktop_amt/audit1: audit_span.py
```

**10-03 23:51 · Bash** — Tabulate all variants across runs from raw JSON

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
for tag in ['S0_baseline','S1_mask','S2_resid','S3_reader','S4_long','final']:
    d=json.load(open(f'runs/F104_kurt_masktop_amt/{tag}.json'))
    print('=====',tag, 'fit',d['fit_split'], 'splits', d['splits_used'])
    for vid,v in d['results'].items():
        s=v['splits']; b=v['books']['splits']
        tr,va=s['train'],s['valid']
        print(f"{vid:<16} sgn {v['sign']:+.0f} hl {v['books']['hl_used']:>4} rIC {tr['rank_ic']:+.4f}/{va['rank_ic']:+.4f} t {tr['rank_ic_t']:+5.1f}/{va['rank_ic_t']:+5.1f} ICIR {tr['rank_icir']:+.2f}/{va['rank_icir']:+.2f} | LS {b['train']['ls_sharpe']:+.2f}/{b['valid']['ls_sharpe']:+.2f} Lnet {b['train']['long_ann']*100:+5.1f}/{b['valid']['long_ann']*100:+5.1f} Lshp {b['train']['long_sharpe']:+.2f}/{b['valid']['long_sharpe']:+.2f} short {b['train']['short_gross_ann']*100:+5.1f}/{b['valid']['short_gross_ann']*100:+5.1f} TO {b['train']['ls_turnover']*100:.1f} dist {v.get('distinct')}")
EOF
```

```
===== S0_baseline fit train splits ['train', 'valid', 'utrain']
v_base           sgn -1 hl 20.0 rIC +0.0199/+0.0100 t +15.4/ +5.4 ICIR +0.49/+0.27 | LS +3.91/+1.47 Lnet  +4.8/ -5.8 Lshp +1.00/-1.24 short +33.9/+24.3 TO 7.0 dist 1.0
===== S1_mask fit train splits ['train', 'valid', 'utrain']
p_noabs          sgn -1 hl 20.0 rIC +0.0199/+0.0100 t +15.4/ +5.4 ICIR +0.49/+0.27 | LS +3.91/+1.47 Lnet  +4.8/ -5.8 Lshp +1.00/-1.24 short +33.9/+24.3 TO 7.0 dist 1.0
p_nat            sgn -1 hl 10.0 rIC +0.0131/-0.0016 t  +5.9/ -0.5 ICIR +0.19/-0.03 | LS +1.72/-1.19 Lnet  -2.3/-21.7 Lshp -0.27/-2.63 short +33.8/+14.2 TO 10.3 dist 1.0
p_kfrac          sgn +1 hl 10.0 rIC +0.0301/+0.0502 t  +8.0/ +8.6 ICIR +0.26/+0.44 | LS +0.06/+2.76 Lnet  +1.5/+17.9 Lshp +0.20/+2.74 short  +0.5/+18.2 TO 2.2 dist 0.04916102443332352
p_mirror         sgn -1 hl 10.0 rIC +0.0010/-0.0055 t  +0.5/ -2.4 ICIR +0.02/-0.12 | LS +0.62/-3.11 Lnet  -1.0/-14.9 Lshp -0.20/-2.91 short +13.7/ -7.7 TO 10.0 dist 0.994727047146402
f_addmean        sgn -1 hl 20.0 rIC +0.0100/-0.0133 t  +4.6/ -3.4 ICIR +0.15/-0.18 | LS +3.23/+0.05 Lnet  +0.6/-20.1 Lshp +0.08/-2.41 short +42.6/+25.2 TO 6.0 dist 1.0
f_addmed         sgn -1 hl 20.0 rIC +0.0278/+0.0108 t +15.6/ +3.7 ICIR +0.50/+0.19 | LS +4.42/+1.52 Lnet  +7.0/ -4.7 Lshp +1.51/-0.77 short +38.9/+26.2 TO 6.7 dist 1.0
f_floormed       sgn -1 hl 10.0 rIC +0.0241/+0.0093 t +14.1/ +3.4 ICIR +0.45/+0.18 | LS +3.76/+0.52 Lnet  +4.0/-11.1 Lshp +0.78/-1.90 short +39.0/+25.1 TO 10.9 dist 0.9995328194347115
===== S2_resid fit train splits ['train', 'valid', 'utrain']
q_ref            sgn -1 hl 20.0 rIC +0.0199/+0.0100 t +15.4/ +5.4 ICIR +0.49/+0.27 | LS +3.91/+1.47 Lnet  +4.8/ -5.8 Lshp +1.00/-1.24 short +33.9/+24.3 TO 7.0 dist 1.0
q_nat_ramt       sgn -1 hl 20.0 rIC +0.0187/+0.0067 t +10.2/ +2.6 ICIR +0.33/+0.13 | LS +1.71/-0.27 Lnet  +0.0/-14.0 Lshp +0.00/-1.86 short +25.9/+15.7 TO 8.0 dist 1.0
q_nat_m30        sgn -1 hl  1.0 rIC +0.0087/-0.0156 t  +2.3/ -2.8 ICIR +0.08/-0.14 | LS +1.52/-1.19 Lnet  -0.2/-17.5 Lshp -0.02/-2.20 short +24.3/ +5.8 TO 5.3 dist 1.0
q_nat_ramt30     sgn -1 hl  1.0 rIC +0.0212/+0.0052 t  +7.9/ +1.2 ICIR +0.25/+0.06 | LS +3.75/+1.91 Lnet  +5.4/ +0.3 Lshp +1.08/+0.06 short +33.7/+23.3 TO 6.1 dist 1.0
q_base_ramt30    sgn -1 hl  0.0 rIC +0.0207/+0.0090 t +10.8/ +3.1 ICIR +0.35/+0.16 | LS +2.23/+0.57 Lnet  +0.8/ -8.6 Lshp +0.12/-1.75 short +27.5/+20.1 TO 9.0 dist 1.0
q_nat_rk30       sgn -1 hl  1.0 rIC +0.0189/+0.0019 t  +7.1/ +0.4 ICIR +0.23/+0.02 | LS +2.69/+1.20 Lnet  +5.8/ -1.6 Lshp +1.12/-0.30 short +22.5/+18.0 TO 6.1 dist 1.0
q_addmed_m30     sgn -1 hl  1.0 rIC +0.0315/+0.0158 t +14.0/ +3.7 ICIR +0.45/+0.19 | LS +4.15/+1.43 Lnet  +7.6/ -2.4 Lshp +1.65/-0.43 short +34.4/+22.1 TO 6.0 dist 1.0
===== S3_reader fit train splits ['train', 'valid', 'utrain']
r_ref30          sgn -1 hl  1.0 rIC +0.0212/+0.0052 t  +7.9/ +1.2 ICIR +0.25/+0.06 | LS +3.75/+1.91 Lnet  +5.4/ +0.3 Lshp +1.08/+0.06 short +33.7/+23.3 TO 6.1 dist 1.0
r_base_m30       sgn -1 hl  1.0 rIC +0.0237/+0.0112 t +13.3/ +3.9 ICIR +0.43/+0.20 | LS +3.25/+1.38 Lnet  +2.8/ -3.5 Lshp +0.61/-0.83 short +28.3/+19.5 TO 6.0 dist 1.0
r_maxsh30        sgn -1 hl  0.0 rIC +0.0262/+0.0137 t  +9.2/ +2.8 ICIR +0.30/+0.14 | LS +3.69/+2.06 Lnet  +3.1/ -2.0 Lshp +0.62/-0.44 short +40.1/+29.2 TO 7.3 dist 1.0
r_cv30        
… (2363 字符略) …
 short +30.4/+27.9 TO 5.4 dist 0.7866347018279892
l_add2           sgn -1 hl  0.0 rIC +0.0350/+0.0509 t  +9.7/ +8.8 ICIR +0.31/+0.45 | LS +2.67/+3.58 Lnet +12.5/+16.1 Lshp +2.12/+3.05 short +29.0/+31.4 TO 6.6 dist 0.8757299696332632
l_addcv          sgn -1 hl  0.0 rIC +0.0405/+0.0526 t +13.9/+11.2 ICIR +0.45/+0.57 | LS +3.48/+3.81 Lnet +11.9/+11.8 Lshp +2.24/+2.86 short +37.7/+36.1 TO 5.7 dist 0.779746835443038
l_gate           sgn -1 hl  1.0 rIC +0.0136/-0.0009 t  +5.2/ -0.2 ICIR +0.17/-0.01 | LS +1.61/-1.40 Lnet +10.1/ +7.3 Lshp +2.01/+1.80 short  +6.6/-12.3 TO 5.7 dist 1.0
l_excl           sgn -1 hl  0.0 rIC +0.0358/+0.0455 t +11.7/ +9.2 ICIR +0.38/+0.47 | LS +3.52/+3.96 Lnet +13.1/+16.7 Lshp +2.20/+3.11 short +34.9/+30.0 TO 6.8 dist 1.0
===== final fit train splits ['train', 'valid', 'utrain', 'holdout', 'full']
f_orig           sgn -1 hl 20.0 rIC +0.0199/+0.0100 t +15.4/ +5.4 ICIR +0.49/+0.27 | LS +3.91/+1.47 Lnet  +4.8/ -5.8 Lshp +1.00/-1.24 short +33.9/+24.3 TO 7.0 dist 1.0
f_kurt30         sgn -1 hl  1.0 rIC +0.0212/+0.0052 t  +7.9/ +1.2 ICIR +0.25/+0.06 | LS +3.75/+1.91 Lnet  +5.4/ +0.3 Lshp +1.08/+0.06 short +33.7/+23.3 TO 6.1 dist 1.0
f_cv30           sgn -1 hl  0.0 rIC +0.0281/+0.0190 t +10.0/ +3.9 ICIR +0.32/+0.20 | LS +3.77/+2.37 Lnet  +4.1/ -0.9 Lshp +0.89/-0.20 short +40.1/+31.1 TO 6.2 dist 1.0
f_exclcv         sgn -1 hl  0.0 rIC +0.0408/+0.0538 t +13.2/+10.8 ICIR +0.42/+0.55 | LS +3.94/+4.44 Lnet +15.0/+19.1 Lshp +2.50/+3.55 short +40.2/+34.5 TO 5.2 dist 1.0
f_std30          sgn -1 hl  0.0 rIC +0.0343/+0.0565 t  +8.1/ +8.7 ICIR +0.26/+0.44 | LS +1.87/+3.70 Lnet +12.6/+22.3 Lshp +1.78/+3.46 short +21.1/+33.8 TO 2.9 dist 1.0
```

**10-03 23:51 · Bash** — Wait for the audit script to finish

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F104_kurt_masktop_amt audit1 540
```

```
[valid] long decile of f_std30: concentration rank mean 0.57, share >0.8 6.2%, share >0.6 54.3%

[audit_span done]
[partura exit 0 2026-10-04_14:56:58]
(no runs/F104_kurt_masktop_amt/audit1.json — an exec job prints its own output; full log: logs/F104_kurt_masktop_amt_audit1.log)
[guard] all 2 run slots busy, waiting ...
[guard] got run slot 0 after 186s

======== 0. self-check against the stage tables (LS net train/valid: base 3.91/1.47, bk 3.75/1.91, bc 3.77/2.37, exclcv 3.94/4.44, std30 1.87/3.70, base30 3.25/1.38) ========
   base hl 20  LS +3.91/+1.47  traded rIC +0.0272/+0.0133 (t +14.4/+4.4)  Lnet +4.8%/-5.8%
 base30 hl  1  LS +3.25/+1.38  traded rIC +0.0222/+0.0104 (t +12.5/+3.7)  Lnet +2.8%/-3.5%
     bk hl  1  LS +3.75/+1.91  traded rIC +0.0195/+0.0042 (t +7.3/+1.0)  Lnet +5.4%/+0.3%
     bc hl  0  LS +3.77/+2.37  traded rIC +0.0281/+0.0190 (t +10.0/+3.9)  Lnet +4.1%/-0.9%
 exclcv hl  0  LS +3.94/+4.44  traded rIC +0.0408/+0.0538 (t +13.2/+10.8)  Lnet +15.0%/+19.1%
  std30 hl  0  LS +1.87/+3.70  traded rIC +0.0343/+0.0565 (t +8.1/+8.7)  Lnet +12.6%/+22.3%
  amt30 hl  1  LS +1.20/+3.19  traded rIC +0.0277/+0.0522 (t +6.3/+7.6)  Lnet +8.5%/+21.4%

======== A. spanning: rank-space daily OLS residual of a TRADED signal on other traded signals (dg.neutralise) ========
columns: R2 | residual rank IC train/valid (t) | gross LS Sharpe train/valid | long gross / short gross excess train, valid | share of rank IC kept train/valid
base                       R2   nan | rIC +0.0272/+0.0133 (t +14.4/ +4.4) | LSgross +5.15/+2.81 | L +10.1% S +33.9% , L  +0.4% S +24.3% | kept --/--
base | amt30               R2 0.042 | rIC +0.0233/+0.0110 (t +11.4/ +3.5) | LSgross +3.56/+2.03 | L  +7.5% S +29.6% , L  -3.2% S +22.5% | kept 86%/83%
base | bk                  R2 0.289 | rIC +0.0207/+0.0115 (t +12.1/ +5.1) | LSgross +1.75/+2.16 | L  +7.4% S  +5.9% , L +16.9% S  -3.5% | kept 76%/87%
base | bk, amt30           R2 0.338 | rIC +0.0147/+0.0078 (t  +8.4/ +3.3) | LSgross +1.65/+1.48 | L  +7.4% S  +3.6% , L +13.1% S  -4.9% | kept 54%/59%
base | bk, bc, amt30       R2 0.350 | rIC +0.0182/+0.0100 (t  +9.8/ +4.1) | LSgross +2.13/+1.58 | L  +7.8% S  +7.0% , L +12.6% S  -3.6% | kept 67%/75%

base30                     R2   nan | rIC +0.0222/+0.0104 (t +12.5/ +3.7) | LSgross +4.36/+2.50 | L  +7.6% S +28.3% , L  +1.6% S +19.5% | kept --/--
base30 | amt30             R2 0.042 | rIC +0.0190/+0.0080 (t  +9.9/ +2.7) | LSgross +3.10/+1.73 | L  +7.2% S +23.5% , L  -2.0% S +18.1% | kept 85%/77%
base30 | bk                R2 0.388 | rIC +0.0134/+0.0066 (t  +8.3/ +3.2) | LSgross +0.41/+1.58 | L  +7.0% S  -4.2% , L +19.3% S  -9.8% | kept 60%/64%
base30 | bk, amt30         R2 0.438 | rIC +0.0072/+0.0025 (t  +4.3/ +1.1) | LSgross +0.15/+1.10 | L  +5.8% S  -4.8% , L +16.1% S  -9.9% | kept 32%/24%
base30 | bk, bc, amt30     R2 0.460 | rIC +0.0132/+0.0072 (t  +7.2/ +3.0) | LSgross +0.86/+1.50 | L  +6.3% S  -0.7% , L +16.6% S  -8.2% | kept 59%/70%

bk                         R2   nan | rIC +0.0195/+0.0042 (t  +7.3/ +1.0) | LSgross +4.74/+2.84 | L +10.5% S +33.7% , L  +5.6% S +23.3% | kept --/--
bk | base30                R2 0.388 | rIC +0.0101/-0.0003 (t  +3.7/ -0.1) | LSgross +0.90/-1.21 | L +10.0% S  -2.6% , L +10.8% S -19.0% | kept 52%/-6%
bk | base30, amt30         R2 0.415 | rIC +0.0129/+0.0038 (t  +5.4/ +1.0) | LSgross +1.64/-0.74 | L +10.4% S  +2.1% , L +11.6% S -16.5% | kept 66%/90%
bk | base(EMA20), amt30    R2 0.310 | rIC +0.0096/+0.0005 (t  +4.1/ +0.1) | LSgross +1.50/-1.03 | L  +7.0% S  +4.1% , L  +8.0% S -14.8% | kept 49%/13%

bc                         R2   nan | rIC +0.0281/+0.0190 (t +10.0/ +3.9) | LSgross +4.65/+3.17 | L  +9.5% S +40.1% , L  +4.5% S +31.1% | kept --/--
bc | base30                R2 0.139 | rIC +0.0216/+0.0163 (t  +8.0/ +3.6) | LSgross +2.39/+1.00 | L +10.3% S  +9.4% , L  +8.2% S  -0.2% | kept 77%/86%
bc | base30, amt30         R2 0.170 | rIC +0.0261/+0.0230 (t +11.0/ +5.4) | LSgross +3.75/+2.84 | L +11.3% S +23.2% , L  +9.9% S +14.7% | kept 93%/121%
bc | base(EMA20), amt30    R2 0.139 | rIC +0.0244/+0.0215 (t +10.4/ +5.2) | LSgross +3.46/+2.68 | L +10.6% S +21.8% , L  +9.7% S +13.1% | kept 87%/113%


======== B. where the decile books of the 'liquidity-orthogonal' residual sit in amt30 (traded signal) ========
   bk [train] short decile: mean amt30 rank 0.67  share in least-active quintile 2%  in most-active quintile 34%  mean cap rank 0.54
   bk [train]  long decile: mean amt30 rank 0.45  share in least-active quintile 14%  in most-active quintile 5%  mean cap rank 0.36
   bk [valid] short decile: mean amt30 rank 0.68  share in least-active quintile 1%  in most-active quintile 35%  mean cap rank 0.55
   bk [valid]  long decile: mean amt30 rank 0.45  share in least-active quintile 15%  in most-active quintile 5%  mean cap rank 0.42
   bc [train] short decile: mean amt30 rank 0.65  share in least-active quintile 1%  in most-active quintile 31%  mean cap rank 0.50
   bc [train]  long decile: mean amt30 rank 0.49  share in least-active quintile 7%  in most-active quintile 5%  mean cap rank 0.49
   bc [valid] short decile: mean amt30 rank 0.66  share in least-active quintile 0%  in most-active quintile 31%  mean cap rank 0.51
   bc [valid]  long decile: mean amt30 rank 0.48  share in least-active quintile 9%  in most-active quintile 5%  mean cap rank 0.57
 base [train] short decile: mean amt30 rank 0.62  share in least-active quintile 3%  in most-active quintile 26%  mean cap rank 0.53
 base [train]  long decile: mean amt30 rank 0.37  share in least-active quintile 54%  in most-active quintile 23%  mean cap rank 0.46
 base [valid] short decile: mean amt30 rank 0.60  share in least-active quintile 7%  in most-active quintile 26%  mean cap rank 0.47
 base [valid]  long decile: mean amt30 rank 0.53  share in least-active quintile 29%  in most-active quintile 34%  mean cap rank 0.56

======== C. locked-at-limit-up cells (label NaN -> earns 0 in the short book): how much of the short leg is that? ========
label check: buyable-finite cells 5208786, raw-finite 5219822, buyable finite but raw NaN 0, max |diff| where both finite 0.00e+00
[train] locked cells: 0.175% of all cells; mean raw label on them +551 bp; per day 9.1 names
[valid] locked cells: 0.107% of all cells; mean raw label on them +465 bp; per day 5.6 names
columns: locked share in universe / short decile / long decile | mean raw label of locked cells in the short decile | LS net Sharpe buyable -> short leg on raw label | short-leg gross excess buyable -> raw
   base [train] locked 0.24% / 0.49% / 0.58% | +439 bp | LS +3.91 (chk +3.91) -> +3.22 | short +33.9% (chk +33.9%) -> +28.5%
   base [valid] locked 0.11% / 0.46% / 0.07% | +459 bp | LS +1.47 (chk +1.47) -> +0.85 | short +24.3% (chk +24.3%) -> +19.0%
     bk [train] locked 0.24% / 0.49% / 0.09% | +454 bp | LS +3.75 (chk +3.75) -> +3.13 | short +33.7% (chk +33.7%) -> +28.1%
     bk [valid] locked 0.11% / 0.40% / 0.02% | +464 bp | LS +1.91 (chk +1.91) -> +1.44 | short +23.3% (chk +23.3%) -> +18.6%
     bc [train] locked 0.24% / 0.60% / 0.05% | +407 bp | LS +3.77 (chk +3.77) -> +3.16 | short +40.1% (chk +40.1%) -> +34.1%
     bc [valid] locked 0.11% / 0.48% / 0.01% | +434 bp | LS +2.37 (chk +2.37) -> +1.87 | short +31.1% (chk +31.1%) -> +25.8%
 exclcv [train] locked 0.24% / 0.41% / 0.10% | +408 bp | LS +3.94 (chk +3.94) -> +3.59 | short +40.2% (chk +40.2%) -> +36.0%
 exclcv [valid] locked 0.11% / 0.34% / 0.03% | +471 bp | LS +4.44 (chk +4.44) -> +4.05 | short +34.5% (chk +34.5%) -> +30.3%
  std30 [train] locked 0.24% / 0.12% / 0.80% | +447 bp | LS +1.87 (chk +1.87) -> +1.79 | short +21.1% (chk +21.1%) -> +19.7%
  std30 [valid] locked 0.11% / 0.09% / 0.11% | +462 bp | LS +3.70 (chk +3.70) -> +3.62 | short +33.8% (chk +33.8%) -> +32.7%
  amt30 [train] locked 0.24% / 0.07% / 0.94% | +435 bp | LS +1.20 (chk +1.20) -> +1.15 | short +13.4% (chk +13.4%) -> +12.6%
  amt30 [valid] locked 0.11% / 0.03% / 0.20% | +569 bp | LS +3.19 (chk +3.19) -> +3.15 | short +27.7% (chk +27.7%) -> +27.2%

======== D. f_exclcv's long decile: is it 'the least-active decile minus the most concentrated 10-20%'? ========
[train] long decile of f_exclcv: concentration rank mean 0.32, max 0.66, share >0.6 3.0%, share >0.4 38.2%; amt30 rank mean 0.13, p90 0.24; overlap with amt30 long 37%, with std30 long 49%
[train] long decile of f_std30: concentration rank mean 0.56, share >0.8 3.4%, share >0.6 51.9%
[valid] long decile of f_exclcv: concentration rank mean 0.31, max 0.66, share >0.6 2.5%, share >0.4 35.9%; amt30 rank mean 0.13, p90 0.23; overlap with amt30 long 36%, with std30 long 46%
[valid] long decile of f_std30: concentration rank mean 0.57, share >0.8 6.2%, share >0.6 54.3%

[audit_span done]
[partura exit 0 2026-10-04_14:56:58]
```

**10-03 23:59 · Bash** — Confirm audit log pulled and locate orthogonality claims in notes

```bash
cd /Users/wxy/Desktop/Partura && ls -la logs/F104_kurt_masktop_amt_audit1.log studies/F104_kurt_masktop_amt/audit_span.py && grep -c "" logs/F104_kurt_masktop_amt_audit1.log && grep -n "事前\|之前定稿\|读之前" notes/F104_kurt_masktop_amt/10_distilled.md | head; grep -n "R² 0.002\|流动性上是中性\|正交" notes/F104_kurt_masktop_amt/*.md | head -20
```

```
-rw-r--r--@ 1 wxy  staff   8485 Oct  3 23:56 logs/F104_kurt_masktop_amt_audit1.log
-rw-r--r--@ 1 wxy  staff  12266 Oct  3 23:50 studies/F104_kurt_masktop_amt/audit_span.py
77
1:### 读留出段之前写下的:候选、理由、预测(只凭 train / valid;这一段在 `study.sh final` 之前定稿,之后没有改过)
10:| `f_exclcv` | `add(cs_rank(cross_mean(day_sum(Amt), 30)), pow_3(cs_rank(<f_cv30>)))` | **升华候选(事前推荐,纯多头用)** | x2:3.94 / 4.44,+15.0% / +19.1%,2.50 / 3.55,换手 5.2%;指数 2 / 3 / 6、60 日窗口、换水平腿都不塌 |
23:**读之前的判断**
29:3. *升华*:事前推荐 `f_exclcv`。**预测**:留出段多头腿净超额与纯多头夏普都高于原式;两项都不高于原式,升华失败。
33:5. **推荐规则(事前定死)**:
42:上面那张「最终对比」表逐条对照事前的预测:
44:| 事前预测 | 留出段 | 判定 |
52:按事前定死的规则(第 5 条第一支):`f_exclcv` 的多头腿好于原式,相对 `f_std30` 纯多头夏普低 0.25、净超额低 1.8 个点,没有同时越过 0.3 与 3 个点的线 → **推荐 `f_exclcv`**。
notes/F104_kurt_masktop_amt/07_neutralise.md:12:**3. 提纯骨架对成交额水平是正交的,对其余的已知暴露不是。** `r_ref30`(= `q_nat_ramt30`)对 `ctl_amt` / `ctl_amt30` 的 R² 都是 0.002。
notes/F104_kurt_masktop_amt/07x_longleg.md:89:  多头腿从 +10.6% 掉到 +0.6% 是这个成分漂移,不是集中度信号失效。提纯骨架的多头十分位在流动性上是中性的(重合 4%),它的多头腿(+11.3% / +6.1% 毛)才是集中度自己的。
notes/F104_kurt_masktop_amt/08_variants.md:16:| C. 集中度对流动性取残差(提纯骨架) | `r_ref30`、`r_maxsh30`、`r_cv30`、`r_rankavg30`、`r_kurt15`、`r_kurt60`、`r_kurt_noopen30`、`r_kurt_max30`;方向拆分 `r_up30`、`r_dn30`;近亲 `q_nat_rk30`、`l_stdres30` | 相互秩相关多数在 0.7~0.96(极值记忆版 0.5~0.8);与成交额水平正交 | 3.2~3.8 / 1.6~2.4(方向拆分 2.5~2.7 / 1.9~2.2;近亲 2.7~3.8 / 0.8~1.2) |
notes/F104_kurt_masktop_amt/09_diagnosis.md:17:   多头腿净超额相应地 +4.8% → −5.8%,留出段 −2.1%。提纯式的多头十分位在流动性上是中性的(与最不活跃十分位的重合只有 4%),多头腿净超额 train / valid 是 +5.4% / +0.3%,留出段 +1.4%。
```

**10-04 00:01 · StructuredOutput**

```json
{
 "factor_id": "F104_kurt_masktop_amt",
 "lens": "机制与过拟合",
 "issues": [
  {
   "severity": "major",
   "where": "recommended / recommended_kind=elevated;verdict 第 (1) 句「相对原式是实打实的升华」;notes/F104_kurt_masktop_amt/10_distilled.md 推荐规则第 5 条;07x_longleg.md §1",
   "what": "推荐式 f_exclcv 被标成 elevated,但相对正确的基准(已知家族、只有 2 个算子的 f_std30)它在纯多头口径上没有任何一段样本外更好,而且它不是原式的升华而是换了一条因子(流动性家族 + 集中度的双重排序)。事前规则是合取式(纯多头夏普低 0.3 以上「并且」净超额低 3 个点以上才不推荐),举证责任放在基准一边,默认结果就是推荐合成版;按 playbook §0(「没有升华空间是合格结论,不要为了有个升华版去凑」),这里的证据支持的是「没有超出 F001 家族的升华」。「五条事前预测全部成立」读起来像背书,其中第 2、4 条本身就是「多头腿做不出来 / 不超过已知家族」的预测。",
   "evidence": "多头腿净超额 train/valid/holdout:f_exclcv +15.0%/+19.1%/+12.3%,f_std30 +12.6%/+22.3%/+14.1% —— 只有 train 更好,valid 与留出段都更差,不同向。留出段纯多头夏普 1.26 对 1.51,多头回撤 −18.5% 对 −14.6%,多空日换手 5.1% 对 2.7%,算子 12 对 2。与原式秩相关 0.37,与 std30 可交易信号 0.82~0.83,全部控制变量 R² 0.774。邻域不是平台而是斜坡:指数 1/2/3/6 的 valid 多头净超额 11.3→14.0→16.7→20.9,终点是纯流动性 21.4(即「集中度权重越小越好」)。x2 逐年:在最不活跃十分位里剔除最集中一批的增益 2022 年起为 0。审查实验 D:f_exclcv 多头十分位与 amt30 多头十分位只重合 36~37%、与 std30 重合 46~49%,集中度秩 >0.6 的成员只有 2.5~3%(f_std30 的多头书里这类占 52~54%)—— 它把已知家族多头书的一半换掉了,而 valid 上最不活跃一层里集中度五分位是平的(24.4…22.0),换掉的那一半只是丢了流动性溢价。",
   "fix": "recommended_kind 改成 distilled(提纯式,注明「空头腿/排除型,纯多头不可用」),结论首句写成「没有超出 F001 家族的升华;纯多头直接用 cross_mean(day_std(Amt),30) / cross_max(day_std(Amt),9)」。f_exclcv 如要保留,只能标为「另一条因子(流动性家族 + 集中度双重排序,与原式秩相关 0.37)」,增量只在多空夏普与逐年稳定性,且该增量见下一条要打折。"
  },
  {
   "severity": "major",
   "where": "09_diagnosis.md 未决最后一条、11_risks.md「标签口径抬高空头腿」;verdict / one_line 里所有多空夏普的比较(2.13 对 1.89、3.16 对 1.94)",
   "what": "研究把「次日开盘封涨停的票在空头里记 0」列为没量过的未决项,但所有关于集中度的结论都建在这条空头腿上。审查实测这不是小数:集中度类因子的多空夏普被这一口径抬高约 0.5~0.7,是 ±0.3 噪声带的两倍;流动性家族几乎不受影响。于是「集中度相对已知家族多出来的多空夏普」被系统性高估,对纯多头使用者而言这些封板票本来就买不到,「避开它们」也没有价值。",
   "evidence": "audit_span.py §C(只用 train/valid;自检:用同一标签时逐位复现阶段表)。封板格子占比:全体 0.24%/0.11%,空头十分位 原式 0.49%/0.46%、f_kurt30 0.49%/0.40%、f_cv30 0.60%/0.48%、f_exclcv 0.41%/0.34%,f_std30 只有 0.12%/0.09%;这些格子的原始标签均值 +4.1%~+4.7%。空头腿改按原始标签计的扣费多空夏普 train/valid:原式 3.91→3.22 / 1.47→0.85;f_kurt30 3.75→3.13 / 1.91→1.44;f_cv30 3.77→3.16 / 2.37→1.87;f_exclcv 3.94→3.59 / 4.44→4.05;f_std30 1.87→1.79 / 3.70→3.62;空头腿毛超额各掉约 4~6 个点。f_exclcv 相对 f_std30 的多空优势 valid 上从 0.74 缩到 0.43。",
   "fix": "报告加一列「空头腿按原始标签计」的多空夏普与空头腿超额(train/valid),verdict 第 (2) 句的「3.16 对 1.94」和提纯式的「2.13 对 1.89」加注「同口径估计高估约 0.4~0.6,流动性基准不受影响」(留出段不能再读,只能按 train/valid 的幅度注明)。"
  },
  {
   "severity": "major",
   "where": "family 字段「本身不属于成交额水平家族(对成交额 R² 0.002)」;07_neutralise.md 第 3 点;09_diagnosis.md 第 6 点「提纯式…流动性中性」;verdict「去掉流动性污染后的读数」",
   "what": "「与流动性正交」只在线性秩回归的意义上成立,而用来证明它的中性化表与 cs_regres 是同一个线性秩空间,结构上看不见尾部。秩是有界的:不活跃股票的峰度秩预测值约 0.73,残差最多 +0.27;活跃股票预测值约 0.27,残差可到 +0.73 —— 所以残差最高的十分位(空头书,钱全在这里)机械地由活跃股票组成。提纯式的空头腿因此带着一段没写明的流动性水平暴露,valid 上的「不输原式」有相当一部分是它。",
   "evidence": "audit_span.py §B:f_kurt30 空头十分位的 amt30 平均分位 0.67/0.68(train/valid),34~35% 在最活跃五分位、只有 1~2% 在最不活跃五分位;f_cv30 同样(0.65/0.66,31%,0~1%)。用研究自己 x2 §3 双重排序的行收益(L1…L5:train +10.6/+6.3/+0.9/−5.3/−12.5,valid +23.7/+10.6/+2.5/−10.9/−26.0)按这个分布折算(粗估,中间三档按均值 0.67 反推):同样流动性分布的随机股票空头超额约 5 个点(train)与约 10 个点(valid),而 f_kurt30 空头腿毛超额是 33.7% / 23.3% —— valid 上约四成是流动性位置。",
   "fix": "把条件化改成分桶内取秩(例如在 amt30 的 10~20 个分桶里对集中度取秩,或对分桶哑变量取残差),重报 train/valid 的两本书与空头十分位的流动性分布;R² 0.002 改述为「线性秩意义上正交,尾部不是」;「valid 不输」的说法以分桶中性后的数字为准。"
  },
  {
   "severity": "major",
   "where": "established 第 1、2 条;one_line「mask 节点是一个歪打正着的流动性条件化」;verdict「同一机制去掉流动性污染后的读数」;known_exposure_r2 0.175",
   "what": "「显式条件化可以替代 mask」只在十分位书的空头腿上成立,在 rank IC 上不成立。原式里有一块既不是自身集中度、也不是线性流动性的成分,带着过半的 rank IC,而且全在多头侧;反过来 f_kurt30 在 valid 上没有任何原式之外的信息。也就是说 f_kurt30 是原式的「空头腿那一半」,不是「原式去掉污染」。这块没被命名的成分最可能是 mask 造出来的非线性不流动性读数(只在流动性分布的下三分之一起作用,线性秩控制变量看不见)—— 研究没有排除、也没有检验这个解释;若成立,known_exposure_r2 0.175 只是线性下界,「一小段流动性倾斜」的说法偏小。",
   "evidence": "audit_span.py §A(可交易信号的逐日秩空间残差,dg.neutralise)。原式(EMA-20)rIC 0.0272/0.0133;对 f_kurt30 + amt30 取残差后 R² 0.338,残差 rIC 0.0147/0.0078(t 8.4/3.3,保留 54%/59%),无成本多空夏普 5.15/2.81 → 1.65/1.48,空头腿 33.9%/24.3% → 3.6%/−4.9%,多头腿毛超额 +7.4%/+13.1%。再加 f_cv30 仍保留 67%/75%(t 9.8/4.1)。同时间尺度的 r_base_m30:保留 32%/24%(只加 kurt30+amt30)或 59%/70%(再加 cv30)。反方向:f_kurt30 对 原式 + amt30 取残差,rIC 0.0096/0.0005(t 4.1/0.1),valid 无成本多空 −1.03;f_cv30 同样处理保留 87%/113%(t 10.4/5.2),多空 3.46/2.68。",
   "fix": "措辞降级为「mask 的空头腿读的是同等流动性下的集中度(已确立);原式另有一块占 rank IC 过半、落在多头侧的 mask 特有成分,未解释」。补一个实验:在同一 spanning 回归里加 ctl_kshare30 与 amt30 分桶哑变量 —— 残差 IC 若消失,原式 = 集中度(空头侧)+ 非线性不流动性(多头侧),故事闭合且已知暴露占比要上调;若不消失,mask 里有本研究没读到的东西。"
  },
  {
   "severity": "minor",
   "where": "10_distilled.md「提纯式用峰度版」;07_S2_resid.md、established 第 2 条「valid 与留出段不输」",
   "what": "「不输原式」只在十分位多空夏普这一把尺子上成立。峰度版提纯式的 rank IC 在 valid 上不显著,rank ICIR 在三段上都只有原式的一半左右;变异系数读数在三段的 rank IC 都更高,且是两个读数里唯一带有原式之外信息的,但被定为「这条因子自己的干净写法」的是峰度版,事后给的理由是留出段多头腿 +1.4% 对 −1.8%(两者都在 0 附近)。",
   "evidence": "final.json:rank IC(t)train/valid/holdout —— f_orig 0.0199(15.4)/0.0100(5.4)/0.0144(9.0);f_kurt30 0.0212(7.9)/0.0052(1.2)/0.0143(4.1);f_cv30 0.0281(10.0)/0.0190(3.9)/0.0207(4.5)。rank ICIR:原式 0.49/0.27/0.37,f_kurt30 0.25/0.06/0.17,f_cv30 0.32/0.20/0.19。",
   "fix": "在提纯结论里并列写出 rank IC / ICIR 的对比,明说「按十分位书不输、按 IC 稳定性减半」;峰度版与变异系数版谁是「干净写法」按 train/valid 的证据定(IC 与独立信息支持变异系数版),不要引用留出段的多头腿差异。"
  },
  {
   "severity": "minor",
   "where": "configs/F104_kurt_masktop_amt.yaml 里 l_excl / f_exclcv 的 why(「只罚最集中的一批,其余股票按流动性排」);07_S4_long.md 第 5 点;12_next.md 第 4 条",
   "what": "pow_3(cs_rank) 的语义描述不准。cs_rank 是 (0,1] 的百分位,三次方在多头十分位的入选线(两项之和约 0.22)附近并不小:集中度秩 0.6 的罚分已是 0.216,等于把整条入选线用完。所以它不是「最不活跃十分位剔掉最集中的 10~20%」,而是「不活跃 且 集中度低于约六成分位」的双重排序。",
   "evidence": "解析:U+V³ 的 10% 分位 c 满足 (3/4)c^(4/3)=0.1,c≈0.22,要求 V<0.60。实测(audit_span.py §D):f_exclcv 多头十分位集中度秩均值 0.31~0.32、最大 0.66、>0.4 的占 36~38%;amt30 秩均值 0.13、p90 0.23~0.24。",
   "fix": "改称「双重排序」并写出实际入选条件;真正的排除式(最不活跃十分位剔掉最集中五分之一)研究已量过:train +5.1 个点、valid −0.2 个点,直接引用它作为「排除条件对多头书 2022 年起无增益」的证据。"
  }
 ],
 "checked": [
  "三份必读文件(CLAUDE.md、docs/method.md、docs/study_playbook.md)、全部 notes、configs、x1/x2 脚本与日志、6 个运行 JSON 与 ledger 均已读",
  "算子源码(study.sh src + x1_sources.log):nt_cs_mask_top_replace_mean_neg = −mask_top(−x),逐分钟截面把最低 ceil(0.1N) 只改写成含被替换者的行均值,并列按列下标稳定排序破平局 —— 与 notes 一致;day_kurt 是总体超额峰度、nanmean、不缩尾 —— 一致;cs_regres(Y,X) 是 Y 对 X 带截距的逐日 OLS 残差、任一缺失输出 NaN —— 一致(R² 0.002 也印证残差方向没写反);cs_rank 是 (0,1] 百分位;cross_mean 是交易日轴 nanmean 滚动",
  "时间方向:所有用到的算子注册表 lookahead=False;日内截面算子只用当天。我读了 cross_mean 的内核但没有读 rolling_reduce 本体,也没有自己重跑因果探针 —— 这一项依赖注册表标志与研究的 check",
  "数字核对:S0~S4 与 final 的每个变体(rank IC、t、ICIR、多空、多头净超额、纯多头夏普、空头腿、换手、dist)从原始 JSON 重新列表,与 notes 和结构化结论里的数字逐项一致;recommended 的 12 项指标与 final.json 的 books_user 一致",
  "留出段:ledger 显示 holdout 只读 1 次、5 条表达式;final.json 里嵌着运行当时的 why 文本(含对 f_std30 的合取规则),说明规则确实在读留出段之前定下;x1/x2 脚本只切 train/valid/utrain",
  "变体数:41 个阶段变体 + x2 的 4 个邻域写法 = 45,与报告一致;服务器运行 8 次(含 final)",
  "问题 1(每条已确立结论背后的实验):第 1、2 条见 issues 第 4 条;第 3 条(读数/窗口/时段/方向不是本质)有 S3 的 11 个单零件替换支撑,站得住;第 4 条(钱在空头腿、与已知暴露重叠)有中性化表支撑,但水平受标签口径影响(issues 第 2 条);第 5 条(原式多头腿是漂移的流动性暴露)有 x2 §5 支撑,审查实验 B 进一步看到原式多头十分位是哑铃形(最不活跃五分位 54%→29%,最活跃五分位 23%→34%);第 6 条(与 F001 是同一量的两半、合成版不超过已知家族)站得住",
  "问题 3(分辨):overview 与中性化表都读了;原式对 9 个共用控制变量 R² 0.125、对 14 个 0.175 属实,但全部是线性秩回归,对 mask 的非线性流动性通道和提纯式的尾部倾斜都是盲的(issues 第 3、4 条)",
  "问题 4(是不是挑出来的噪声):f_exclcv 相对原式的改进远大于噪声,但来源是换成流动性因子;相对 f_std30,多空三段都更高(空头腿、且被标签口径抬高),多头腿只有 train 更高;指数邻域是指向纯流动性的斜坡",
  "问题 5(还是不是同一个因子):f_exclcv 与原式 0.37、f_kurt30 与原式可交易信号 0.52/0.58 —— 研究如实写了「不是等价改写」,但结构化结论仍用 elevated 标签",
  "问题 6(多头腿):相对原式大幅变好(−2.1% → +12.3%,−0.39 → 1.26);相对已知家族基准没有变好",
  "问题 7(留出段):数字照实报告,没有隐瞒;轻描淡写之处在框架 ——「实打实的升华」「五条预测全部成立」放在前面,「不超过已知家族」放在第二句"
 ],
 "refutation_attempt": "做了一次反驳实验:/Users/wxy/Desktop/Partura/studies/F104_kurt_masktop_amt/audit_span.py(study.sh exec,tag audit1,日志 /Users/wxy/Desktop/Partura/logs/F104_kurt_masktop_amt_audit1.log)。只切 train/valid,没有读留出段,没有改配置。自检通过:7 块面板的扣费多空与多头净超额逐位复现阶段表(原式 3.91/1.47、f_kurt30 3.75/1.91、f_exclcv 3.94/4.44 等),混合标签函数在两腿用同一标签时复现 book_row。\n\n设计(跑之前定的判据):\nA. spanning —— 如果「原式 = 同等流动性下的集中度 + 流动性倾斜」,原式的可交易信号对 {f_kurt30, amt30}(再加 f_cv30)取秩空间残差后应该几乎没有 rank IC;若 train 和 valid 都保留 40% 以上,机制没有覆盖原式。\nB. 提纯式两端十分位在 amt30 上的位置(「与流动性正交」在尾部成不成立)。\nC. 封涨停格子在各空头十分位里的占比,以及空头腿改按原始标签计的多空夏普;判据是掉 0.5 以上算实质。\nD. f_exclcv 多头十分位的集中度分布(是不是「排除」)。\n\n结果:\nA. 部分推翻。空头腿被完全张成:原式对 f_kurt30 取残差后空头腿毛超额 33.9%→5.9%(train)、24.3%→−3.5%(valid)—— 「空头腿读的是同等流动性下的集中度」站得住。但 rank IC 没被张成:对 f_kurt30 + amt30 取残差仍保留 54%/59%(t 8.4/3.3),这块残差的钱在多头侧(毛超额 +7.4%/+13.1%)。反方向,f_kurt30 在 valid 上没有原式之外的信息(t 0.1),f_cv30 有(t 5.2)。\nB. 推翻「流动性中性」:f_kurt30 空头十分位 amt30 平均分位 0.67,34~35% 在最活跃五分位、1~2% 在最不活跃五分位;粗估 valid 上空头腿约四成是流动性位置。\nC. 越过判据:集中度类因子的多空夏普掉 0.5~0.7(原式 valid 1.47→0.85,f_kurt30 1.91→1.44),流动性家族只掉 0.05~0.08。\nD. 不是排除:f_exclcv 多头十分位与 amt30 多头十分位只重合 36~37%,集中度秩上限 0.66。\n\n没有推翻的:mask 不是旁观者也不是计数器、读数/窗口/时段/方向无关、钱在空头腿、与 F001 是同一量的两半、合成版多头腿不超过已知家族 —— 这些结论在审查实验里没有出现反证。A 里那块未解释成分「是非线性不流动性」只是我的推断,没有检验。",
 "overall": "机制的核心一半站得住,推荐的标签站不住。四条 major、两条 minor,没有 critical —— 研究的事实陈述基本属实、留出段只读一次且规则确为事前写入,问题在措辞强度、一把线性尺子的盲区和推荐的归类。\n\n站得住的:原式的空头腿读的是「同等流动性下成交在日内有多不均匀」,审查实验里 f_kurt30 把原式的空头腿完全张成;读数、窗口、时段、方向都不是本质;它与 F001 的 day_std(Amt) 是同一个量的两半;合成版的多头腿不超过已知家族。\n\n需要降级或补实验的:\n1. 推荐式 f_exclcv 不该标 elevated。纯多头口径上它在 valid 和留出段都不如 2 个算子的 f_std30(留出段 +12.3% 对 +14.1%,夏普 1.26 对 1.51,回撤更深、换手翻倍),与原式秩相关只有 0.37,是另一条因子。诚实的结论是「提纯成一条空头腿因子,没有超出 F001 家族的升华」。\n2. 所有多空夏普的比较都被标签口径抬高:集中度类因子约 0.5~0.7,流动性基准几乎不受影响。合成版相对已知家族的多空优势在 valid 上从 0.74 缩到 0.43。\n3. 提纯式「与流动性正交(R² 0.002)」只是线性秩意义上的;它的空头十分位三分之一在最活跃五分位,valid 上空头腿约四成是流动性位置(粗估)。\n4. 「mask = 流动性条件化、f_kurt30 = 原式去掉污染」说过头了:原式有一块占 rank IC 过半、落在多头侧的 mask 特有成分没有被命名,最可能是非线性不流动性,未检验;若成立,已知暴露 R² 0.175 只是线性下界。\n\n对只能做多的使用者,结论不变且更简单:这条因子自己没有可用的多头腿,纯多头用 F001 家族即可。"
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F104_kurt_masktop_amt/audit_span.py`

## 它返回给工作流的结构化结果

见 `handoff/F104_kurt_masktop_amt/results/audit-mechanism.json`。

## 它拿到的任务书

```
[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的审查员,负责**机制与过拟合**这一路 —— 一个多疑的量化研究员。另一位研究员刚完成了因子 F104_kurt_masktop_amt 的研究;
  你的任务是**尝试推翻**它的机制解释和它推荐的候选。默认立场:在证据把别的解释排除掉之前,结论不成立。
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  开始之前**必须**依次读完这三份文件:CLAUDE.md、docs/method.md、docs/study_playbook.md。
  study_playbook.md 是操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西,全在里面,下面不再重复。
  不要使用 Agent / Workflow 工具去派生别的 agent;这项工作由你自己完成。
  所有写给人看的文字(notes、结论)用中文,英文术语保留。
  
  要读的材料(都在 /Users/wxy/Desktop/Partura 下):
    research/alpha_distillation/F104_kurt_masktop_amt.md      最终报告
    notes/F104_kurt_masktop_amt/*.md                           手写段落
    configs/F104_kurt_masktop_amt.yaml                         实验计划
    runs/F104_kurt_masktop_amt/*.json、runs/F104_kurt_masktop_amt/ledger.json  每次运行的原始结果与数据段台账
    studies/F104_kurt_masktop_amt/                             自写的探针与分析脚本(如果有)
  看某次运行的摘要:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F104_kurt_masktop_amt <tag>(tag = JSON 文件名去掉 .json)。
  
  研究员自己报告的结论(待推翻):
  {
   "one_line": "它读的是「相对于同等流动性的股票,成交在日内分布得有多不均匀」,方向为负;mask 节点是一个歪打正着的流动性条件化。提纯后是一条空头腿/排除型因子(测试段多空 2.13 对原式 1.89,多头腿净超额仍只有 +1.4%);把流动性水平放回来的排除式合成测试段多头腿净超额 +12.3%、纯多头夏普 1.26,远好于原式,但没有超过只用已知家族的 cross_mean(day_std(Amt),30)(+14.1%、1.51)。",
   "mechanism": "day_kurt(Amt) 读的是成交额在日内 241 分钟上的集中度(与最大一分钟占比秩相关 0.93、与偏度 0.99)。裸的集中度与流动性负相关(越不活跃成交越断续,峰度越高;日频 −0.17,30 日尺度 −0.46),而不活跃股票之后是跑赢的,所以裸峰度带着一段方向错了的流动性暴露,valid 上整条因子反号(1.72 / −1.19)。nt_cs_mask_top_replace_mean_neg 把每分钟全市场成交额最低 10% 的格子改写成截面均值:改的是底部不是顶部,也不是缩尾,而是往不活跃股票的序列里注入一段全市场共同的日内成交曲线,净效果是把峰度与成交额的秩相关翻成 +0.11 —— 一个粗糙的「对流动性水平做条件化」。把它写成显式的截面残差 cs_regres(rank(30 日均值读数), rank(30 日成交额)) 之后,train 持平、valid 与留出段不输;读数换成最大一分钟占比或变异系数、窗口 15/30/60、去掉开盘收盘几根、只读上涨或只读下跌分钟,书都相同 —— 它不是「单根脉冲 / 拉升 / 开盘抢筹」。钱在空头腿(多头只占毛价差两成多):最集中的那 10% 股票同时是最近大涨过、价格有跳、量价同向、波动高的那批,14 个控制变量拿走提纯式 63% 的 rank IC 和 85% 的空头腿;信号在最活跃的五分之一股票里最强,valid 上只剩「活跃股票里最集中的 20%」。原式的多头腿其实是一段会漂移的流动性暴露(多头十分位 train 上 42% 是最不活跃十分位,valid 上 19%)。day_std(Amt)=day_mean(Amt)×变异系数,所以它是 F001 蒸馏因子里「std 相对于 sum 多出来的那一半」。",
   "family": "日内成交集中度对流动性水平取残差(峰度/变异系数读数等价)—— 与 F001 的 day_std(Amt) 是同一个量的两半(std = 水平 × 变异系数),本身不属于成交额水平家族(对成交额 R² 0.002),但空头腿与彩票/波动/价格跳跃/量价同向等已知暴露高度重叠;推荐的合成式则落回流动性家族(与 30 日成交额秩相关 0.75,R² 0.774)",
   "known_exposure_r2": 0.175,
   "recommended": {
    "expr": "add(cs_rank(cross_mean(day_sum(Amt), 30)), pow_3(cs_rank(cs_regres(cs_rank(cross_mean(div(day_std(Amt), day_mean(Amt)), 30)), cs_rank(cross_mean(day_sum(Amt), 30))))))",
    "sign": -1,
    "halflife": 0,
    "ls_train": 4.06,
    "ls_test": 3.16,
    "long_gross_train": 0.2022,
    "long_gross_test": 0.1579,
    "long_net_train": 0.1621,
    "long_net_test": 0.1225,
    "long_sharpe_train": 2.77,
    "long_sharpe_test": 1.26,
    "turnover": 0.0513,
    "coverage": 0.9993,
    "distinct": 1,
    "n_operators": 12,
    "rank_corr_with_original": 0.37
   },
   "recommended_kind": "elevated",
   "verdict": "推荐式 f_exclcv 是按读留出段之前定死的规则选出来的(多头腿好于原式,且相对已知家族基准没有「纯多头夏普低 0.3 以上并且净超额低 3 个点以上」),必须连着三句话读:(1) 相对原式是实打实的升华 —— 测试段多头腿净超额 −2.1% → +12.3%,纯多头夏普 −0.39 → +1.26,多空 1.89 → 3.16;(2) 但那本多头书的钱是流动性溢价:测试段它没有超过只用已知家族的 cross_mean(day_std(Amt),30)(+14.1%、1.51),对全部控制变量 R² 0.774;库里已有 F001 家族因子的话,纯多头用它们就够了,集中度多出来的只是多空夏普(3.16 对 1.94)和逐年稳定性(八年最低 2.59 对 0.66),空头做不了就拿不到;(3) 测试段多头腿回撤 −18.5%,是一本低流动性小票书。这条因子自己的干净写法是提纯式 cs_regres(cs_rank(cross_mean(day_kurt(Amt),30)), cs_rank(cross_mean(day_sum(Amt),30))):测试段多空 2.13(原式 1.89)、多头腿净超额 +1.4%(原式 −2.1%),2021~2025 每年多空 1.6~2.2;它与原式的可交易信号秩相关只有 0.52、算子数 7 对 3,不是等价改写而是同一机制去掉流动性污染后的读数。它是空头腿/排除型因子,自己的多头腿做不出来 —— 这是因子的性质,不是写法问题。五条事前预测在留出段全部成立;留出段只读了一次。",
   "established": [
    "abs_ 是空操作;mask 既不是旁观者也不是被改写分钟数的计数器,而是把峰度与成交额的秩相关从 −0.17 翻到 +0.11 的流动性条件化:删掉它 valid 反号(S1 p_nat 1.72/−1.19),只留被改写占比则是成交额代理(p_kfrac 与 ctl_amt −0.91),原式与两点公式的 Spearman 只有 0.157,代码顺序并列破平局在真实数据上没咬到(x1 §1–§3、S1)",
    "显式条件化可以替代 mask:cs_regres(rank(30 日均值峰度), rank(30 日成交额)) train/valid 3.75/1.91(原式 3.91/1.47),留出段 2.13 对 1.89、多头腿净超额 +1.4% 对 −2.1%;条件化必须在慢时间尺度上做(逐日版 1.71/−0.27)。但它不是原式的等价改写:同尺度秩相关 0.61、可交易信号 0.52,原式或地板写法再做条件化反而更差(2.23/0.57、2.13/−0.53)(S2、S3、x2 §2、S_final)",
    "读数、记忆、窗口、时段、方向都不是本质:最大一分钟占比 3.69/2.06、变异系数 3.77/2.37、逐日秩均值 3.21/1.87、窗口 15/60 为 3.53/1.73 与 3.49/1.64、去掉开盘收盘几根 3.27/2.19、只读上涨/下跌分钟 2.71/1.88 与 2.49/2.22 且方向同为负;留出段峰度版与变异系数版 2.13/2.16(S3、S_final)",
    "钱在空头腿且与已知暴露重叠:原式对 9 个共用控制变量 R² 0.125(加本研究 5 个后 0.175),提纯式对 14 个控制变量 R² 0.319,中性化拿走 63% 的 rank IC 和 85% 的空头腿(33.7%→4.9%)而多头腿不动;条件 IC 集中在 ctl_max30/ctl_pvcorr30 最高五分之一(−0.037,其余 −0.004~−0.019)和最活跃五分之一(−0.037,其余 −0.016~−0.026)(中性化表、条件 IC 表、x2 §4)",
    "原式的多头腿是一段会漂移的流动性暴露:多头十分位 train 上 42% 是全市场最不活跃十分位、valid 上 19%,多头腿净超额 +4.8%→−5.8%→留出段 −2.1%;提纯式多头十分位流动性中性(重合 4%)(x2 §5、S_final)",
    "与 F001 是同一个量的两半,且合成版多头腿不超过已知家族:std 对成交额取残差与变异系数读数秩相关 0.91(S4);合成版多头腿净超额 train/valid/留出 +15.0%/+19.1%/+12.3% 对 cross_mean(day_std(Amt),30) 的 +12.6%/+22.3%/+14.1%;在最不活跃十分位里剔除最集中一批的增益从 2018 年 +9.9 个点降到 2022 年起的 0(S4、x2 §1/§3、S_final)"
   ],
   "variants_tested": 45
  }
  
  ## 要回答的问题(把查过的写进 checked)
  
  1. **每条「已确立」的结论,背后是哪个实验?** 那个实验真的能把这条结论和它最强的竞争解释区分开吗?
     还是换一种解释也会得到同样的结果?把研究**没有排除**的那个解释写出来。
  2. **算子语义读对了吗?** 自己用 ./scripts/study.sh src <算子> 读关键算子的源码,核对 notes 里对它的描述。
     特别留意:时间方向(有没有用到当天之后的数据;日内向前看是允许的,跨日向前看不允许)、
     NaN 与边界行为、带不带尺度、布尔/档位输出。
  3. **「分辨」站得住吗?** 说它是(或不是)某个已知暴露,有没有中性化的 R² 与残差表现、有没有直接替换实验?
     看 overview:cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python scripts/overview_for.py F104_kurt_masktop_amt
  4. **推荐的候选是不是挑出来的噪声?** 数一数全研究试了多少个变体;推荐者相对原式的改进有多大
     (这批因子在测试段上的噪声大约是多空夏普 ±0.3);改进是不是 train 和 valid 同向、多头腿和多空同向;
     邻域(窗口、指数换一档)稳不稳;它是不是恰好只在 valid 上最好。
  5. **它还是同一个因子吗?** 推荐者与原式的 rank 相关是多少?如果很低,这不是「提纯」而是换了一个因子 ——
     可以,但必须这么说。
  6. **多头腿**。用户只能做多。推荐者的多头腿净超额、纯多头夏普相对原式是变好了还是只是多空夏普变好了?
  7. **留出段**。留出段的结果支持还是不支持 notes 里的说法?有没有把不利的留出段结果轻描淡写?
  
  你**可以**做一次反驳实验(不是必须):在 configs/F104_kurt_masktop_amt.yaml 末尾加一个阶段 SA_audit(≤ 6 个变体,
  只用 train/valid,**绝不**读留出段、绝不用 study.sh final),用 ./scripts/study.sh check 然后
  ./scripts/study.sh run F104_kurt_masktop_amt audit1 SA_audit、wait 取结果;或者写 studies/F104_kurt_masktop_amt/audit_*.py 用 exec 跑。
  只在它能直接检验你最怀疑的那一点时才做。做了就把设计与结果写进 refutation_attempt。
  
  issues 里每条写清 severity(critical = 机制结论或推荐因此不成立;major = 需要降级措辞或补实验;minor)、
  where、what、evidence、fix。没有问题就返回空数组,不要凑数;但也不要因为报告写得流畅就放过它。
```
