# 相关度表:种子 2039,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.08 | `sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_for` | 0.05 | 0.03 | 0.04 | 0.17 | 0.03 | 0.02 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| slot a seed 1 | 过 | 0.05 | `sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_for` | 0.10 | 0.01 | 0.01 | 0.15 | 0.01 | 0.02 | `cross_zscore(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` |
| slot a seed 2 | 过 | 0.27 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.20 | 0.19 | 0.42 | 0.04 | 0.14 | 0.49 | `cross_tail_mean_q25(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` |
| slot a seed 3 | 过 | 0.39 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.30 | 0.05 | 0.61 | 0.12 | 0.13 | 0.36 | `cross_tail_mean_q75(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60)` |
| slot a seed 4 | 过 | 0.28 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.23 | 0.10 | 0.40 | 0.07 | 0.14 | 0.23 | `cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)` |
| slot a seed 5 | 过 | 0.21 | `day_open(cross_sum(log(Amt), 3))` | 0.11 | 0.14 | 0.29 | 0.40 | 0.18 | 0.02 | `sub(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20), cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241))` |
| slot a seed 6 | 过 | 0.42 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.23 | 0.35 | 0.42 | 0.10 | 0.38 | 0.06 | `cs_bucket_demean(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap)` |
| slot a seed 7 | 过 | 0.15 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.17 | 0.08 | 0.01 | 0.00 | 0.08 | 0.03 | `cross_corr(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_mean(Ret), 120)` |
| slot a seed 8 | 过 | 0.28 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.21 | 0.05 | 0.28 | 0.19 | 0.10 | 0.22 | `div(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), cross_ema(day_std(Ret), 60))` |
| slot a seed 9 | 过 | 0.33 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.24 | 0.14 | 0.50 | 0.16 | 0.19 | 0.23 | `mul(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot a seed 10 | 过 | 0.44 | `day_open(cross_sum(log(Amt), 3))` | 0.23 | 0.45 | 0.50 | 0.32 | 0.48 | 0.11 | `cross_ema(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_wmean(Ret, Volume)), 60)` |
| slot a seed 11 | 过 | 0.38 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.23 | 0.30 | 0.41 | 0.09 | 0.34 | 0.02 | `cross_ema(cs_bucket_demean(sub(day_wmean(Ret, Amt), day_mean(Ret)), LogFloatCap), 120)` |
| slot a seed 12 | 过 | 0.26 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.20 | 0.09 | 0.64 | 0.15 | 0.15 | 0.27 | `ts_quantile_q75(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60)` |
| slot a seed 13 | 过 | 0.35 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.28 | 0.09 | 0.59 | 0.06 | 0.01 | 0.50 | `cross_ema(abs_(sub(day_wmean(Ret, Amt), day_mean(Ret))), 60)` |
| slot a seed 14 | 过 | 0.21 | `day_open(cross_sum(log(Amt), 3))` | 0.11 | 0.13 | 0.29 | 0.40 | 0.17 | 0.03 | `cross_ema(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)), 20)` |
| slot a seed 15 | 过 | 0.18 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.15 | 0.21 | 0.44 | 0.09 | 0.23 | 0.14 | `cross_ema(mul(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Ret)), 120)` |
| slot a seed 16 | 过 | 0.40 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.26 | 0.03 | 0.58 | 0.14 | 0.10 | 0.33 | `cross_tail_mean_q75(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)), 60)` |
| slot b seed 1 | 过 | 0.28 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.26 | 0.04 | 0.34 | 0.12 | 0.09 | 0.24 | `cross_ema(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), 60)` |
| slot b seed 2 | 过 | 0.04 | `sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_for` | 0.13 | 0.00 | 0.01 | 0.11 | 0.00 | 0.01 | `cross_zscore(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), 120)` |
| slot b seed 3 | 过 | 0.56 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.35 | 0.42 | 0.11 | 0.06 | 0.36 | 0.35 | `cross_ema(sub(day_topw_mean(Ret, Amt), day_wmean(Ret, Amt)), 60)` |
| slot b seed 4 | 过 | 0.32 | `day_open(cross_sum(log(Amt), 3))` | 0.20 | 0.44 | 0.45 | 0.10 | 0.43 | 0.08 | `cross_ema(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 120)` |
| slot b seed 5 | 过 | 0.28 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.30 | 0.02 | 0.32 | 0.08 | 0.06 | 0.26 | `cross_ema(sub(day_wmean(Ret, mul(Volume, Volume)), day_wmean(Ret, Volume)), 120)` |
| slot b seed 6 | 过 | 0.29 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.28 | 0.05 | 0.37 | 0.09 | 0.10 | 0.26 | `cross_ema(sub(day_wmean(Ret, mul(Amt, Amt)), day_mean(Ret)), 120)` |
| slot b seed 7 | 过 | 0.28 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.26 | 0.04 | 0.34 | 0.12 | 0.09 | 0.24 | `cross_ema(div(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), replace_small_with_nan(is_gt(day_std(Ret), 0.0001))), 60)` |
| slot b seed 8 | 过 | 0.34 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.29 | 0.02 | 0.45 | 0.04 | 0.05 | 0.37 | `cross_tail_mean_q75(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), 120)` |
| slot b seed 9 | 过 | 0.28 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.32 | 0.00 | 0.29 | 0.06 | 0.04 | 0.26 | `cross_ema(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), 241)` |
| slot b seed 10 | 过 | 0.54 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.43 | 0.15 | 0.12 | 0.01 | 0.09 | 0.03 | `cs_bucket_demean(cross_ema(sub(day_topw_mean(Ret, Amt), day_wmean(Ret, Amt)), 120), LogFloatCap)` |
| slot b seed 11 | 过 | 0.12 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.16 | 0.03 | 0.19 | 0.01 | 0.03 | 0.03 | `cross_corr(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` |
| slot b seed 12 | 过 | 0.20 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.28 | 0.07 | 0.16 | 0.07 | 0.04 | 0.22 | `cross_ema(sub(sub(day_wmean(Ret, mul(Amt, Amt)), day_wmean(Ret, Amt)), sub(day_wmean(Ret, Amt), day_mean(Ret))), 60)` |
