# 相关度表:种子 2078,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.17 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.21 | 0.04 | 0.12 | 0.21 | 0.06 | 0.03 | `cross_delta(day_flat_ratio(Volume), 30)` |
| slot a seed 1 | 废品 | 0.20 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.19 | 0.13 | 0.22 | 0.24 | 0.15 | 0.04 | `cross_mean(cross_delta(day_flat_ratio(Volume), 30), 10)` |
| slot a seed 2 | 废品 | 0.71 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.62 | 0.66 | 0.12 | 0.03 | 0.65 | 0.54 | `ts_max(cross_delta(day_flat_ratio(Volume), 30), 20)` |
| slot a seed 3 | 过 | 0.16 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.23 | 0.04 | 0.12 | 0.20 | 0.06 | 0.03 | `div(cross_delta(day_flat_ratio(Volume), 30), cross_mean(day_flat_ratio(Volume), 60))` |
| slot a seed 4 | 过 | 0.04 | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))` | 0.12 | 0.05 | 0.01 | 0.05 | 0.05 | 0.06 | `mul(cross_delta(day_flat_ratio(Volume), 30), cross_mean(day_mean(Ret), 5))` |
| slot a seed 5 | 过 | 0.09 | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15` | 0.14 | 0.03 | 0.00 | 0.06 | 0.04 | 0.02 | `ts_regbeta(day_mean(Ret), cross_delta(day_flat_ratio(Volume), 30), 60)` |
| slot a seed 6 | 过 | 0.07 | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15` | 0.12 | 0.02 | 0.01 | 0.08 | 0.00 | 0.04 | `ts_corr(cross_delta(day_flat_ratio(Volume), 30), day_mean(Ret), 30)` |
| slot a seed 7 | 过 | 0.10 | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))` | 0.12 | 0.13 | 0.07 | 0.14 | 0.11 | 0.27 | `cs_last_low10(cross_delta(day_flat_ratio(Volume), 30), LogFloatCap)` |
| slot a seed 8 | 过 | 0.13 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.11 | 0.02 | 0.18 | 0.22 | 0.05 | 0.14 | `cross_mean(cs_last_low05(cross_delta(day_flat_ratio(Volume), 30), LogFloatCap), 10)` |
| slot a seed 9 | 废品 | 0.10 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.20 | 0.02 | 0.06 | 0.12 | 0.03 | 0.01 | `sub(cross_delta(day_flat_ratio(Volume), 30), cross_delta(day_flat_ratio(Amt), 30))` |
| slot a seed 10 | 过 | 0.52 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.53 | 0.48 | 0.07 | 0.01 | 0.47 | 0.28 | `cs_last_low05(ts_max(cross_delta(day_flat_ratio(Volume), 30), 20), LogFloatCap)` |
| slot b seed 1 | 过 | 0.70 | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))` | 0.66 | 0.39 | 0.11 | 0.03 | 0.36 | 0.03 | `cross_mean(day_ar1_coefficient(Ret), 20)` |
| slot b seed 2 | 过 | 0.19 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.12 | 0.14 | 0.23 | 0.24 | 0.16 | 0.02 | `sub(cross_mean(day_ar1_coefficient(Ret), 20), cross_mean(day_ar1_coefficient(Ret), 60))` |
| slot b seed 3 | 过 | 0.08 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.09 | 0.04 | 0.03 | 0.01 | 0.04 | 0.08 | `cross_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), 20)` |
| slot b seed 4 | 过 | 0.33 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.08 | 0.23 | 0.34 | 0.59 | 0.25 | 0.04 | `cross_mean(day_corr(in_slice(Volume, 2, 240), in_slice(Ret, 1, 239)), 20)` |
| slot b seed 5 | 过 | 0.31 | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` | 0.08 | 0.22 | 0.28 | 0.50 | 0.24 | 0.07 | `sub(cross_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), 20), cross_mean(day_corr(in_slice(Volume, 2, 240), in_slice(Ret, 1, 239)), 20))` |
| slot b seed 6 | 过 | 0.69 | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))` | 0.66 | 0.39 | 0.11 | 0.03 | 0.35 | 0.02 | `cross_mean(day_durbin_watson(Ret), 20)` |
| slot b seed 7 | 过 | 0.32 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), cross_mean` | 0.28 | 0.10 | 0.14 | 0.06 | 0.12 | 0.15 | `ts_stddev(day_ar1_coefficient(Ret), 30)` |
| slot b seed 8 | 过 | 0.02 | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15` | 0.02 | 0.00 | 0.01 | 0.03 | 0.00 | 0.01 | `sub(cross_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), 20), cross_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), 60))` |
| slot b seed 9 | 过 | 0.09 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.08 | 0.07 | 0.01 | 0.01 | 0.06 | 0.08 | `cross_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Amt, 1, 239)), 20)` |
| slot b seed 10 | 过 | 0.23 | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))` | 0.17 | 0.15 | 0.12 | 0.08 | 0.10 | 0.08 | `cross_mean(day_hurst(Close), 20)` |
