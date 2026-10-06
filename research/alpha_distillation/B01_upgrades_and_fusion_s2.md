# B01:各条升级版的回测,以及把它们融合之后的样本内外结果

## 怎么读

- **样本内** = 2018-01-02 ~ 2023-08-07;**样本外** = 2023-08-08 ~ 2025-12-31。升级版全部只看样本内的数字选出来,样本外只是读数。
- **超额** = 每天等权买入因子排名最好的 10% 股票,相对「全市场等权」的年化超额收益,**已扣单边 15bp 交易成本**(纯多头,不做空)。
- **夏普** = 这条超额收益曲线的年化夏普;**最大回撤** = 这条超额曲线自己的回撤;**日换手** = 这本多头书每天换掉的比例。
- 样本外只有两年半,单个数字的噪声大约是超额 ±3 个点、夏普 ±0.3。

## 先说结论

1. **融合有用,而且样本外站得住**。9 个独立升级版等权融合:样本内 +20.1%(夏普 3.95),样本外 +17.3%(夏普 1.93);8 个年份的超额都在 +15% ~ +22% 之间。对照:已知族单独 +15.4% / +14.1%(夏普 2.22 / 1.51)。
2. **升级前后**。原式 15 条直接融合:+15.8% / +11.1%(夏普 3.26 / 1.63);升级版 15 条融合:+20.2% / +16.0%(夏普 3.65 / 1.63)。超额多了 4~5 个点,但样本外夏普没变 —— 因为这 15 个升级版里有 11 个落在已知族里(表 2),波动跟着已知族走。只用 9 个独立的反而更好。
3. **平滑**。成员各自平滑之后,融合后再平滑不增加收益(样本内选的是不再平滑);它换来的是换手从 3.0% 降到 1.3%、样本外回撤从 -14.1% 收到 -10.5%,样本外夏普基本不变(1.93 → 1.90)。成员不先各自平滑就直接融合则明显更差(换手 20% 以上,要靠很长的半衰期才救回来)。
4. **风险点**。所有升级版融合的样本外最大回撤都发生在 2024-01-16 ~ 02-06(微盘股踩踏)这三周:独立 9 个 -13.5%、已知族 -13.8%、升级版 15 条 -17.2%,而原式 15 条融合只有 -5.3%。升级版比原式更偏低流动性的小票,这是它多赚的来源之一,也是它的尾部风险。
5. **打折看**。成员是从每条因子几百个变体里按样本内挑出来的,样本内的夏普(3.9)有选择偏差,样本外(1.9)大约是它的一半 —— 以样本外为准。

## 一、各条升级版

### 表 1:独立的新因子(和已知的成交额族不是一个东西,每条原式最多一个)

| 来自 | 升级版做了什么 | 样本内超额 | 样本外超额 | 样本内夏普 | 样本外夏普 | 样本外最大回撤 | 日换手 | 原式的超额(样本内 → 样本外) |
|---|---|---|---|---|---|---|---|---|
| F107 挖掘 #613 | 把原式里日内最低价的「偏度」换成「基尼系数」(一天里价格偏离的不均匀程度,有界、不怕单笔异常),再做 30 日指数平均。买离全市场均值最近的(既不死水也不乱跳) | **+11.7%** | **+11.2%** | 2.87 | 2.10 | -7.6% | 3.9% | +1.7% → +1.4% |
| F102 挖掘 #3961 | 分钟收益短窗自相关的日内峰度,原式是 15 日求和,改成 60 日取最大。买近 60 日没出过极端值的(极端值基本是封板日) | **+11.3%** | **+7.0%** | 2.85 | 1.45 | -3.8% | 3.1% | +8.9% → +2.5% |
| F101 手写 day_shine_retstd | 原式只统计「放量分钟」后的波动;这一版把条件放宽到几乎所有有成交的分钟,变成日内 5 分钟波动水平离全市场均值的距离。买最接近均值的 | **+9.7%** | **+7.2%** | 2.68 | 1.60 | -4.7% | 5.2% | +7.1% → +7.1% |
| F111 挖掘 #953 | 原式(日内中位价近 10 日走势的单调程度,买稳步上行的)不变,只是把近 15 日盘口冻结最重的两成股票排到最后 | **+13.5%** | **+7.7%** | 2.46 | 1.05 | -9.0% | 4.3% | +12.3% → +6.0% |
| F103 挖掘 #820 | 原式里成交额的 30 日线性衰减均值,换成 30 日下行半标准差。仍是成交额类,和已知族相关 0.67,算半个新东西 | **+12.6%** | **+8.8%** | 2.24 | 1.15 | -11.3% | 4.1% | +8.1% → +7.2% |
| F113 挖掘 #1375 | 原式整棵树丢掉,只留一个念头:分钟收益绝对值的基尼系数(30 日均值),并且只在成交额相近的股票之间比 | **+8.1%** | **+2.3%** | 2.00 | 0.28 | -12.4% | 1.7% | +0.7% → -0.6% |
| F112 挖掘 #574 | 去掉最外层的 30 日自身缩放。剩下的其实是「低价股」:按价格平方排,最便宜的一成被挖掉,买第二便宜的那一档 | **+8.4%** | **+7.9%** | 1.85 | 1.53 | -5.6% | 2.2% | +4.2% → +6.9% |
| F110 手写 ret_fair_log | 只留原式的第一个乘数:开盘到收盘的日内涨跌幅,取立方后做 30 日指数平均。买近一个月日内大跌过的(日内反转) | **+8.8%** | **+12.5%** | 1.79 | 1.11 | -16.8% | 3.0% | -0.2% → -0.8% |
| F115 手写 all_tide_mean_30 | 潮汐因子:分子不变,分母里两个成交量谷底改用未平滑的原始成交量来定位 | **+6.7%** | **+2.5%** | 1.72 | 0.42 | -9.7% | 4.6% | +4.1% → +1.8% |

### 表 2:已知族(成交额离散度 `cross_mean(day_std(Amt), 30)`,买成交额波动小的)的升级版

这些和已知族是同一个东西的不同写法,彼此高度重合,**只能选一个用,不能叠加**。

| 来自 | 升级版做了什么 | 样本内超额 | 样本外超额 | 样本内夏普 | 样本外夏普 | 样本外最大回撤 | 日换手 | 原式的超额(样本内 → 样本外) |
|---|---|---|---|---|---|---|---|---|
| 对照 | 已知族本身,不做任何改动 | **+15.4%** | **+14.1%** | 2.22 | 1.51 | -14.6% | 3.2% | — |
| F103 挖掘 #820 | 已知族,先把近 15 日盘口冻结最重的两成排到最后,再把上市最短的两成排到最后 | **+18.1%** | **+16.8%** | 3.16 | 1.74 | -15.7% | 3.4% | +8.1% → +7.2% |
| F104 挖掘 #4190 | 已知族,把近 15 日「收盘价不动的分钟占比」最高的两成排到最后(原式自己的多头腿不可用) | **+18.5%** | **+14.5%** | 3.15 | 1.56 | -14.9% | 3.5% | +1.8% → -2.1% |
| F108 挖掘 #3264 | 已知族,把近 15 日出现过最长价格冻结段的两成排到最后(原式自己的多头腿不可用) | **+17.8%** | **+14.7%** | 2.84 | 1.56 | -15.2% | 3.1% | +1.0% → -3.2% |
| F114 挖掘 #1421 | 已知族的排名 + 0.5 × 近 15 日价格不动分钟占比的排名(给冻结盘口加一个罚项) | **+15.7%** | **+15.4%** | 2.80 | 1.68 | -15.6% | 4.5% | +3.6% → +0.2% |
| F105 挖掘 #25 | 原式不变,把近 15 日盘口冻结最重的两成排到最后 | **+13.3%** | **+10.2%** | 2.75 | 1.22 | -14.6% | 6.1% | +11.8% → +8.9% |
| F101 手写 day_shine_retstd | 只在成交额最低的四成股票里,按 F101 反向选 | **+16.0%** | **+15.6%** | 2.67 | 2.03 | -9.0% | 3.9% | +7.1% → +7.1% |
| F113 挖掘 #1375 | 已知族的排名 + 0.25 × 分钟收益基尼(30 日均值)的排名 | **+17.2%** | **+12.9%** | 2.66 | 1.32 | -17.8% | 4.1% | +0.7% → -0.6% |
| F109 手写 erm_mag_gap_5m_tsm20 | 已知族,把 F109 读数最高的两成排到最后 | **+15.6%** | **+13.2%** | 2.37 | 1.40 | -15.0% | 3.4% | -3.2% → +2.9% |
| F115 手写 all_tide_mean_30 | 已知族,把 F115 读数最高的两成排到最后 | **+15.2%** | **+12.6%** | 2.25 | 1.34 | -15.7% | 3.6% | +4.1% → +1.8% |
| F106 手写 erm_mag_gap_1m | 「零收益分钟少」的排名 减 「成交额」的排名:买不钉在一个价位上、又不拥挤的。原式的分母 +1e-6 把它变成了涨跌停探测器,这一版整个重写 | **+12.1%** | **+15.5%** | 2.08 | 1.70 | -14.5% | 3.1% | -5.8% → -3.2% |
| F112 挖掘 #574 | 已知族的排名 + 0.25 × 原式的排名 | **+13.5%** | **+12.9%** | 2.00 | 1.36 | -15.0% | 2.6% | +4.2% → +6.9% |
| F110 手写 ret_fair_log | 已知族的排名 + 0.25 × 原式的排名 | **+13.4%** | **+12.6%** | 1.95 | 1.34 | -14.8% | 2.5% | -0.2% → -0.8% |

没有自己的独立升级版的:F104、F105、F106、F108、F109、F114(原式自身的多头腿扣费后站不住,最好的版本就是表 2 里借已知族的那一行)。

### 表达式

- **表 1 的 F101**(方向:买低;平滑半衰期 20 日)
  `abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Amt, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in_mean_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))), in_stddev_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))))), in_slice(Ret, 2, 237), 5))))`
- **表 1 的 F102**(方向:买低;平滑半衰期 2 日)
  `cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60)`
- **表 1 的 F103**(方向:买低;平滑半衰期 10 日)
  `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_semistd_neg(Amt, 30))), 1)), 5)`
- **表 1 的 F107**(方向:买低;平滑半衰期 2 日)
  `cross_ema(abs_(cs_demean(day_gini(Low))), 30)`
- **表 1 的 F110**(方向:买低;平滑半衰期 5 日)
  `cross_ema(pow_3(sub(div(day_last(Close), day_first(Open)), 1)), 30)`
- **表 1 的 F111**(方向:买高;平滑半衰期 20 日)
  `cs_last_high20(ts_spearman(day_quantile(Close), 10), cross_max(day_zero_ratio(Ret), 15))`
- **表 1 的 F112**(方向:买低;平滑半衰期 10 日)
  `signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High))))`
- **表 1 的 F113**(方向:买低;平滑半衰期 20 日)
  `cs_bucket_rank(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))`
- **表 1 的 F115**(方向:买低;平滑半衰期 10 日)
  `cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_slice(Volume, 31, 211), day_argmax(in_slice(Volume, 31, 211)))), day_argmin(in_slice_from_start(in_slice(Volume, 31, 211), day_argmax(in_slice(Volume, 31, 211)))))), 20)`
- **表 2 的 F103**(方向:买高;平滑半衰期 2 日)
  `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), neg(cross_valid_count(day_last(Close), 241)))`
- **表 2 的 F104**(方向:买高;平滑半衰期 2 日)
  `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_ratio(Close), 15))`
- **表 2 的 F105**(方向:买高;平滑半衰期 5 日)
  `cs_last_high20(neg(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)), cross_max(day_zero_ratio(Ret), 15))`
- **表 2 的 F106**(方向:买高;平滑半衰期 0 日)
  `sub(cs_rank(neg(cross_mean(day_zero_ratio(Ret), 30))), cs_rank(cross_mean(day_sum(Amt), 30)))`
- **表 2 的 F108**(方向:买高;平滑半衰期 3 日)
  `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_run_max(Close), 15))`
- **表 2 的 F109**(方向:买高;平滑半衰期 2 日)
  `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20))`
- **表 2 的 F110**(方向:买低;平滑半衰期 10 日)
  `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)), day_mean(in_sustain_stddev(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)))))), 0.25))`
- **表 2 的 F112**(方向:买低;平滑半衰期 10 日)
  `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)), 0.25))`
- **表 2 的 F113**(方向:买低;平滑半衰期 0 日)
  `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cross_mean(day_gini(Ret), 30)), 0.25))`
- **表 2 的 F114**(方向:买低;平滑半衰期 0 日)
  `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cross_mean(day_flat_ratio(Close), 15)), 0.5))`
- **表 2 的 F115**(方向:买高;平滑半衰期 1 日)
  `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20))`
- **表 2 的 F101**(方向:买高;平滑半衰期 20 日)
  `cs_first_low40(neg(abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in_mean_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))), in_stddev_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))))), in_slice(Ret, 2, 237), 5))))), cross_mean(day_sum(Amt), 30))`

## 二、融合

**融合的做法**:每个成员先按自己在样本内最合适的半衰期做指数平滑;每天把各成员在全市场的排名(0~1)取等权平均;买平均排名最好的 10%。成员怎么选是规则定的(只看样本内):表 1 的 9 个独立升级版;「升级版 15 条」是每条原式各取样本内夏普最高的那个版本(不管它属于哪一族)。

### 表 3:融合之后(成员各自平滑后等权融合;融合后要不要再平滑由样本内决定)

| 组合 | 成员数 | 样本内超额 | 样本外超额 | 样本内夏普 | 样本外夏普 | 样本内最大回撤 | 样本外最大回撤 | 日换手 | 逐年超额 2018…2025 |
|---|---|---|---|---|---|---|---|---|---|
| 对照:已知族单独 | 1 | **+15.4%** | **+14.1%** | 2.22 | 1.51 | -9.2% | -14.6% | 3.2% | +17% +10% +7% +16% +25% +21% +9% +14% |
| **原式** 15 条等权(升级之前) | 15 | **+15.8%** | **+11.1%** | 3.26 | 1.63 | -4.2% | -7.1% | 3.8% | +14% +18% +15% +18% +16% +10% +13% +10% |
| **升级版** 15 条等权 | 15 | **+20.2%** | **+16.0%** | 3.65 | 1.63 | -7.5% | -17.8% | 3.6% | +24% +18% +15% +19% +24% +23% +11% +18% |
| **独立的 9 个**等权 | 9 | **+20.1%** | **+17.3%** | 3.95 | 1.93 | -5.9% | -14.1% | 3.3% | +19% +22% +17% +21% +22% +18% +15% +19% |
| 已知族里最好的升级版,单独 | 1 | **+18.1%** | **+16.8%** | 3.16 | 1.74 | -7.8% | -15.7% | 3.4% | +22% +15% +10% +16% +26% +21% +14% +16% |
| 独立的 9 个 + 已知族最好的一个(10 个等权) | 10 | **+20.3%** | **+17.7%** | 3.91 | 1.87 | -6.0% | -15.9% | 3.3% | +18% +22% +17% +21% +23% +19% +16% +20% |
| 一半已知族最好的一个 + 一半独立 9 个的均值 | 10 | **+20.2%** | **+18.3%** | 3.62 | 1.82 | -7.3% | -17.8% | 3.1% | +21% +20% +15% +19% +25% +21% +14% +20% |

(逐年那一列里 2023 年横跨样本内外。)

### 表 4:平滑的作用(以「独立的 9 个等权」为例,融合之后再做一次指数平滑)

| 融合后的半衰期(日) | 样本内超额 | 样本内夏普 | 样本内换手 | 样本外超额 | 样本外夏普 | 样本外最大回撤 | 样本外换手 |
|---|---|---|---|---|---|---|---|
| 0(样本内选中) | +20.1% | 3.95 | 3.3% | +17.3% | 1.93 | -14.1% | 3.0% |
| 1 | +19.2% | 3.80 | 3.0% | +16.9% | 1.91 | -13.9% | 2.7% |
| 2 | +18.2% | 3.63 | 2.7% | +16.5% | 1.89 | -13.2% | 2.5% |
| 3 | +17.9% | 3.58 | 2.5% | +16.3% | 1.91 | -12.8% | 2.3% |
| 5 | +16.9% | 3.41 | 2.3% | +15.4% | 1.85 | -12.7% | 2.1% |
| 10 | +15.7% | 3.19 | 1.9% | +14.8% | 1.84 | -12.1% | 1.7% |
| 20 | +14.7% | 3.04 | 1.5% | +14.2% | 1.90 | -10.5% | 1.3% |

如果成员**不**先各自平滑、直接融合再统一平滑(同样是这 9 个):

| 统一的半衰期(日) | 样本内超额 | 样本内夏普 | 样本内换手 | 样本外超额 | 样本外夏普 | 样本外换手 |
|---|---|---|---|---|---|---|
| 0 | +7.5% | 1.45 | 22.3% | +4.2% | 0.47 | 19.5% |
| 1 | +15.6% | 2.99 | 11.4% | +10.8% | 1.21 | 10.2% |
| 2 | +18.1% | 3.48 | 7.7% | +13.2% | 1.46 | 6.9% |
| 3 | +19.0% | 3.68 | 6.1% | +14.4% | 1.59 | 5.4% |
| 5(样本内选中) | +19.0% | 3.69 | 4.5% | +14.4% | 1.60 | 4.1% |
| 10 | +18.6% | 3.63 | 3.1% | +15.1% | 1.74 | 2.7% |
| 20 | +17.3% | 3.42 | 2.1% | +14.4% | 1.80 | 1.8% |

曲线图:`research/alpha_distillation/B01_fusion_curves.svg`。
