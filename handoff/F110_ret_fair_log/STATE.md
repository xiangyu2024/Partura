# F110_ret_fair_log — 交接状态

_自动生成于 2026-10-05 00:42(`python scripts/recorder.py --brief F110_ret_fair_log` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 ret_fair_log(批次 B01_single_factors)
- 表达式:`mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)), day_mean(in_sustain_stddev(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 23:28)—— **不许再读**。候选在留出段上的数全在 `runs/F110_ret_fair_log/final.json`(`./scripts/study.sh digest F110_ret_fair_log final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F110_ret_fair_log#1`:已返回结果,最后动作 10-04 23:40 → `handoff/F110_ret_fair_log/agents/work_R1_a19055ac0f98830d9.md`
  - `lead:F110_ret_fair_log#2`:已返回结果,最后动作 10-05 00:14 → `handoff/F110_ret_fair_log/agents/lead_R2_a6887d8909433a81f.md`
  - `work:F110_ret_fair_log#2`:中断,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F110_ret_fair_log` 看服务器上的 tag,`./scripts/study.sh digest F110_ret_fair_log <tag>` 重看结果)。

## 研究现状(`notes/F110_ret_fair_log/state.md`,10-05 00:13 更新)—— **先读这个文件**

# F110_ret_fair_log — 研究现状(主研第 6 轮重写,2026-10-05)

> 第 **6** 位主研,工单 **R4(writeup)**。**留出段已读(只许一次,已用完)** ⇒ 本轮按规矩成文,判断类 notes 已写完。
> `01`/`02`/`03`/`04`/`06` 照用;`02`/`03` 里「成交量脉冲处的价格冲击」那个读法**已被实测推翻**。

## 1. 一句话现状

**研究已收口。** `orders/R4.md`(writeup)在等执行:不跑实验,只做补 `07_S_final.md` + 出报告 +
**逐个核对本轮新算的 16 项派生数字**。执行交回 `results/R4.md` 后即可交付(一般不再回到主研)。

**最终结论**:原式对只能做多的用户是零(四段 −0.0/−0.6/−0.2/−0.8%,八年无一例外)。推荐一条**升华**版
`cross_mean(mul(D, abs_(D)), 20)`(corr 0.673 < 0.8 ⇒ 换了一条因子),四段 `Ln` +7.9/+8.1/+8.0/**+12.8%**、
`Lshp` +1.32/+1.38/+1.34/**+1.17** ⇒ **留出段站住了**。**但交易建议仍是「不建议进组合」**,依据收缩为
「加不出增量」+「中性化后归零」(事前理由「明显输给已知家族」**已被留出段推翻** —— 只输 1.26 点)。

(…全文 6492 字符,读 `notes/F110_ret_fair_log/state.md`)

## 研究日志(`notes/F110_ret_fair_log/journal.md`:22 条,其中研究员自己写的 11 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:25 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 23:28 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F110_ret_fair_log S_final

### 2026-10-04 23:39 [执行] R3:final(S_final,5候选)exit 0,留出段只读了一次(ledger确认holdout reads=1)

tag=S_final,阶段 S_final,5 个变体(f_orig/f_cmT20/f_cvxD20/f_cmDsig20/f_known30),check 25/25 OK 后一次 final 跑完,exit 0,154.2s。
canary 7 项全部吻合(corr(f_orig,v_base)=1.000;corr(f_cmT20,f_orig)=+0.896;corr(f_cvxD20,f_orig)=+0.673;
corr(f_cmDsig20,f_cvxD20)=+0.899;corr(f_known30,f_orig)=+0.351;f_cvxD20/f_known30 train Ln/Lshp 与 S1_long 一致)。

holdout(20230808 起,581 天)主数字——多头口径 Ln/Lshp:
f_orig −0.8%/−0.07;f_cmT20 +4.3%/+0.47;f_cvxD20 +12.8%/+1.17;f_cmDsig20 +9.5%/+0.99;f_known30 +14.1%/+1.51。
J3-a(cmT20−orig)=+5.08pt;J3-b(cvxD20−cmT20)=+8.55pt;J4|cvxD20−cmDsig20|=3.35pt;
J5-a(known30−cvxD20,Ln)=+1.26pt;J5-b(同上,Lshp)=+0.33。5 条 holdout cov 全 0.9997、dist 全≥0.97,无求值失败/符号异常。

值得主研注意:f_cvxD20 holdout Ln(+12.8%)比 train/valid(+7.9%/+8.1%)都高出 4.7~4.9 点,超过±3点噪声带,但 Lshp 差在±0.3内;
f_known30 holdout(+14.1%/+1.51)比 valid(+22.3%/+3.46)低 8.2点/1.95,远超噪声带,但比 train(+12.6%/+1.78)只差+1.5点/-0.27。
JSON 里 holdout 的 profile(分位剖面)和 sweep(固定半衰期)都不存在,只有 train/valid;dist 字段不分段。
结果卡 notes/F110_ret_fair_log/results/R3.md。

### 2026-10-05 00:11 [主研] 第 6 轮:裁决留出段 6 条判据(J4 灰区未裁决、J5 字面过关但事前理由被推翻),推荐不变,写完全部判断类 notes,下 R4(writeup)

**看到了什么。** R3 的 `S_final` exit 0、ledger 确认 holdout 只读 1 次、7 项 canary 全过
(含 `corr(f_orig, v_base) = 1.000`)。最硬的一条外部校验:`f_known30` holdout +14.1%/+1.51
**正好落在用户给的参照 +13~15% / 1.4~1.9 里** ⇒ 段落、口径、扣费、拟合都正常,绝对水平可信,
不必退回「只读相对排序」。5 条候选 holdout 多头口径:`f_orig` −0.8%/−0.07、`f_cmT20` +4.3%/+0.47、
`f_cvxD20` **+12.8%/+1.17**、`f_cmDsig20` +9.5%/+0.99、`f_known30` +14.1%/+1.51。

**六条判据的裁决(全文在 `10_distilled.md` §7)。**
- **J0 过**(正中用户参照)、**J1 过**(原式四段 −0.0/−0.6/−0.2/−0.8%,2024 −0.2%、2025 −2.1%,
  **八年四段无一为正** ⇒ 核心否定结论被留出段确认)、**J6 过**(cov 0.9997、dist ≥0.97)。
- **J2 过,但方式不对称,必须照实写**:`Ln` +12.8% 超门槛 7.9 点,`Lshp` +1.17 只超 0.15。
  留出段变好的是**水平**(`Lg` +10.6%→+15.3%),**风险调整后没变好**(`Lshp` 1.34→1.17)。
  ⇒ 写「净超额更高、夏普持平(略低)」,**不许写「它在留出段上更好」**。
- **J3 两半都过,但比例变了**:原式→`f_cmT20` +5.08 点(`Lg` −0.35、`LTO` 10.31%→3.13% ⇒ **省成本**);
  `f_cmT20`→`f_cvxD20` +8.55 点(`Lg` **+8.68**、`LTO` 3.13%→3.31% ⇒ **真 alpha**)。
  两个机制签名在留出段完整复现,但训练段的「一半一半」变成 **37% 平滑 / 63% 结构**
  ⇒ 报告不许再写「一半一半」。
- **J4 未裁决** —— 这一条我没有当成过关写。|`cvxD20` − `
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:14 [主研] 第 6 轮补记:抽验 JSON 抓到自己两处笔误(cmDsig20 holdout Lshp = 0.986 非 0.994 ⇒ J4 夏普差 +0.19;2025 是 243 天 ⇒ 2023 后段是 96 天非 98 天),已改 notes 并写进 R4 让执行复核

下 R4 之前我把本轮新算的派生数字从 `runs/F110_ret_fair_log/S_final.json` 独立重算了一遍(没有拿结果卡
的摘要互相印证)。**16 项里 14 项完全对上**,抓到两处是我自己的转录错误:

1. **`f_cmDsig20` 的 holdout `Lshp` 是 0.986,我初稿写成了 0.994** ⇒ J4 的夏普旁证是 **+0.19**(1.175 − 0.986),
   不是 +0.18。已改 `10` §7 J4、`09` §二 A、`state.md` §4。**上一条日志(第 21 条)里的 +0.18 没法改(日志只追加),
   以 notes 为准。** 这不影响 J4 的裁决 —— 0.19 仍在 ±0.3 噪声带内,灰区未裁决的结论不变。
2. **天数**:`results/R3.md` 写「2024 242 天、2025 241 天」,但 `diagnostics.by_year` 里 **2025 是 243 天**
   ⇒ 2023 年的留出部分是 **96 天**(581 − 242 − 243),不是结果卡推的 98 天;2023 全年 242 天 ⇒ valid 部分是 146 天。
   已把全部 notes 的「98 天 / valid 144 天」改成「96 天 / valid 146 天」,并把权重三元组改成 96/242/243。
   **用正确天数重算,结论一模一样**:候选 ≈ **−0.0%**、已知家族 ≈ **+26.0%** ⇒「时间分布近乎互补」这条站得住,
   只是天数要写对。R4 第 11 项让执行从 JSON 确认 2025 的 `days`/`n_days`。

**逐项核对通过的(全精度,供执行对照)**:J3-a +5.078 / J3-b +8.545;holdout `Lg` 两步 −0.351 / +8.678;
归因 37.3% 平滑 / 62.7% 结构;J4 `Ln` 3.351;J5-a +1.256 / J5-b +0.334;
`Ln` 差距 utrain 7.44 → holdout 1.26(
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F110_ret_fair_log/orders/`、`notes/F110_ret_fair_log/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有
- R4:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F110_ret_fair_log.yaml`)

- 标题:日内收益 × |放量后波动 − 缩量后波动|:按『成交量跳变处的价格冲击』加权的日内收益累积(方向为负 = 加权的月度日内反转)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_long**(8 个变体):把平滑写进表达式(cross_mean 盒式 + 口径里的 EMA)之后,多头腿能不能站住?权重支路还重要吗?它是不是就是 20 日反转?
  w_cmT20、w_cmD20、w_cmDsig20、w_cvxD20、w_cmD60、w_cmD20lag10、w_cmDcc20、w_known30
- **S_final**(5 个变体):5 条最终候选在用户测试段上的纯多头读数(整个研究唯一一次读留出段)
  f_orig、f_cmT20、f_cvxD20、f_cmDsig20、f_known30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F110_ret_fair_log`)

- `S0_baseline`  10-04 11:53  1 个变体  → `./scripts/study.sh digest F110_ret_fair_log S0_baseline`
- `S1_long`  10-04 15:08  8 个变体  → `./scripts/study.sh digest F110_ret_fair_log S1_long`
- `S_final`  10-04 23:28  5 个变体  → `./scripts/study.sh digest F110_ret_fair_log S_final`
- `x1`(自写脚本的输出)  10-04 13:07  exit 97  → `logs/F110_ret_fair_log_x1.log`
- `x1c`(自写脚本的输出)  10-04 14:05  exit 0  → `logs/F110_ret_fair_log_x1c.log`
- `x1d`(自写脚本的输出)  10-04 14:09  exit 0  → `logs/F110_ret_fair_log_x1d.log`
- `x2`(自写脚本的输出)  10-04 15:07  exit 0  → `logs/F110_ret_fair_log_x2.log`

## 已写的 notes(`notes/F110_ret_fair_log/`)

`01_expression.md`(1K)、`02_operators.md`(4K)、`03_decomposition.md`(3K)、`04_grammar.md`(2K)、`05_hypotheses.md`(24K)、`06_baseline.md`(4K)、`07_S1_long.md`(8K)、`07x_01_x1_anatomy.md`(14K)、`07x_02_x2_GHI.md`(8K)、`08_variants.md`(5K)、`09_diagnosis.md`(12K)、`10_distilled.md`(19K)、`11_risks.md`(7K)、`12_next.md`(6K)、`journal.md`(36K)、`state.md`(10K)

## 自写的探针与分析脚本(`studies/F110_ret_fair_log/`)

- `probes.py`  10-04 12:14  Probes this tree needs:  D * | M - Q |
- `x1_anatomy.py`  10-04 15:04  F110 X1: anatomy of  T = D * |M - Q|  and of the signal that is actually traded, -EMA20(T).

## 结构化结果(`handoff/F110_ret_fair_log/results/`)

(还没有)
