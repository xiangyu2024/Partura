# 相关度表:种子 2009,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.74 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.96 | 0.52 | 0.22 | 0.20 | 0.52 | 0.23 | `log(log(day_durbin_watson(Volume)))` |
| slot a seed 1 | 过 | 0.31 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.09 | 0.01 | 0.11 | 0.26 | 0.03 | 0.03 | `cross_zscore(log(log(day_durbin_watson(Volume))), 60)` |
| slot a seed 2 | 过 | 0.32 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.11 | 0.02 | 0.11 | 0.26 | 0.04 | 0.03 | `cross_madz(log(log(day_durbin_watson(Volume))), 60)` |
| slot a seed 3 | 过 | 0.65 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.26 | 0.22 | 0.36 | 0.30 | 0.25 | 0.08 | `sub(cross_ema(log(log(day_durbin_watson(Volume))), 5), cross_ema(log(log(day_durbin_watson(Volume))), 60))` |
| slot a seed 4 | 过 | 0.12 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.08 | 0.12 | 0.09 | 0.03 | 0.14 | 0.04 | `cross_corr(log(log(day_durbin_watson(Volume))), day_sum(Ret), 40)` |
| slot a seed 5 | 过 | 0.12 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.05 | 0.12 | 0.09 | 0.10 | 0.11 | 0.02 | `cross_corr(log(log(day_durbin_watson(Volume))), ts_delay(day_sum(Ret), 1), 40)` |
| slot a seed 6 | 过 | 0.10 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.04 | 0.09 | 0.05 | 0.10 | 0.09 | 0.01 | `mul(cross_zscore(log(log(day_durbin_watson(Volume))), 60), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 7 | 过 | 0.86 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.93 | 0.58 | 0.36 | 0.08 | 0.58 | 0.03 | `cs_bucket_demean(cross_mean(log(log(day_durbin_watson(Volume))), 20), LogFloatCap)` |
| slot a seed 8 | 过 | 0.86 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.82 | 0.61 | 0.33 | 0.07 | 0.62 | 0.14 | `cs_bucket_zscore(cross_mean(log(log(day_durbin_watson(Volume))), 20), day_last(Close))` |
| slot a seed 9 | 过 | 0.61 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.17 | 0.17 | 0.32 | 0.30 | 0.20 | 0.06 | `sub(cross_mean(log(log(day_durbin_watson(Volume))), 10), cross_mean(log(log(day_durbin_watson(Volume))), 120))` |
| slot a seed 10 | 过 | 0.41 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.10 | 0.01 | 0.16 | 0.32 | 0.03 | 0.02 | `cross_delta(cross_mean(log(log(day_durbin_watson(Volume))), 10), 20)` |
| slot a seed 11 | 过 | 0.29 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.19 | 0.02 | 0.11 | 0.25 | 0.00 | 0.00 | `sub(log(log(day_durbin_watson(Volume))), cross_mean(log(log(day_durbin_watson(Volume))), 60))` |
| slot a seed 12 | 过 | 0.07 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.10 | 0.06 | 0.06 | 0.11 | 0.06 | 0.00 | `cross_regres(log(log(day_durbin_watson(Volume))), day_sum(Ret), 60)` |
| slot a seed 13 | 过 | 0.07 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.18 | 0.07 | 0.06 | 0.08 | 0.07 | 0.02 | `cross_regres(log(log(day_durbin_watson(Volume))), abs_(day_sum(Ret)), 60)` |
| slot a seed 14 | 过 | 0.37 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.08 | 0.07 | 0.18 | 0.26 | 0.09 | 0.04 | `cs_winsor(cross_zscore(log(log(day_durbin_watson(Volume))), 120))` |
| slot a seed 15 | 过 | 0.59 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.56 | 0.47 | 0.06 | 0.04 | 0.44 | 0.25 | `cross_stddev(log(log(day_durbin_watson(Volume))), 60)` |
| slot a seed 16 | 过 | 0.56 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.15 | 0.14 | 0.32 | 0.29 | 0.18 | 0.06 | `cross_zscore(cross_ema(log(log(day_durbin_watson(Volume))), 5), 120)` |
| slot b seed 1 | 过 | 0.78 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.62 | 0.89 | 0.25 | 0.12 | 0.85 | 0.39 | `cross_mean(day_durbin_watson(div(Volume, cross_mean(Volume, 20))), 20)` |
| slot b seed 2 | 过 | 0.73 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.57 | 0.90 | 0.18 | 0.01 | 0.85 | 0.40 | `cross_mean(day_durbin_watson(div(Amt, cross_mean(Amt, 20))), 40)` |
| slot b seed 3 | 过 | 0.74 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.51 | 0.78 | 0.39 | 0.17 | 0.78 | 0.23 | `cross_mean(day_autocorr(div(Volume, cross_mean(Volume, 20)), 1), 20)` |
| slot b seed 4 | 过 | 0.72 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.47 | 0.75 | 0.34 | 0.19 | 0.74 | 0.29 | `cross_mean(day_autocorr(div(Amt, cross_mean(Amt, 20)), 5), 20)` |
| slot b seed 5 | 过 | 0.04 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.23 | 0.03 | 0.10 | 0.49 | 0.04 | 0.27 | `cross_mean(day_signed_ratio(Ret, div(Volume, cross_mean(Volume, 20))), 20)` |
| slot b seed 6 | 过 | 0.30 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.05 | 0.24 | 0.41 | 0.58 | 0.28 | 0.04 | `cross_mean(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 20)` |
| slot b seed 7 | 过 | 0.27 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.15 | 0.12 | 0.05 | 0.16 | 0.12 | 0.14 | `cross_mean(day_corr(div(Volume, cross_mean(Volume, 20)), abs_(Ret)), 20)` |
| slot b seed 8 | 过 | 0.36 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.11 | 0.27 | 0.35 | 0.55 | 0.29 | 0.05 | `cross_mean(day_corr(div(Volume, cross_mean(Volume, 20)), in_delay(Ret, 1)), 20)` |
| slot b seed 9 | 过 | 0.26 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.31 | 0.22 | 0.03 | 0.40 | 0.21 | 0.17 | `mul(cross_mean(day_signed_ratio(Ret, div(Volume, cross_mean(Volume, 20))), 20), cross_mean(day_autocorr(div(Volume, cross_mean(Volume, 20)), 1), 20))` |
| slot b seed 10 | 过 | 0.51 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.18 | 0.47 | 0.11 | 0.19 | 0.42 | 0.14 | `cross_mean(day_skew(div(Volume, cross_mean(Volume, 20))), 20)` |
| slot b seed 11 | 过 | 0.70 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.45 | 0.88 | 0.10 | 0.05 | 0.82 | 0.51 | `cross_mean(day_gini(div(Amt, cross_mean(Amt, 20))), 20)` |
| slot b seed 12 | 过 | 0.32 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.14 | 0.04 | 0.18 | 0.44 | 0.07 | 0.05 | `cross_zscore(cross_mean(day_durbin_watson(div(Volume, cross_mean(Volume, 20))), 5), 60)` |
| slot b seed 13 | 过 | 0.78 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.62 | 0.89 | 0.26 | 0.13 | 0.85 | 0.38 | `sub(cross_mean(day_durbin_watson(in_mean_rolling(div(Volume, cross_mean(Volume, 20)), 5)), 20), cross_mean(day_durbin_watson(div(Volume, cross_mean(Volume, 20))), 20))` |
| slot b seed 14 | 过 | 0.35 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.10 | 0.57 | 0.15 | 0.02 | 0.49 | 0.47 | `div(cross_mean(day_durbin_watson(in_mean_rolling(div(Amt, cross_mean(Amt, 20)), 5)), 20), cross_mean(day_durbin_watson(div(Amt, cross_mean(Amt, 20))), 20))` |
| slot b seed 15 | 过 | 0.04 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.03 | 0.01 | 0.11 | 0.20 | 0.00 | 0.06 | `cross_corr(day_durbin_watson(div(Volume, cross_mean(Volume, 20))), day_sum(Ret), 40)` |
| slot b seed 16 | 过 | 0.25 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.25 | 0.11 | 0.02 | 0.01 | 0.08 | 0.24 | `cross_mean(day_durbin_watson(mul(sign(Ret), div(Volume, cross_mean(Volume, 20)))), 20)` |
| R 1 variant 1 | 过 | 0.70 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.81 | 0.07 | 0.14 | 0.17 | 0.04 | 0.13 | `cs_bucket_demean(ts_sum(log(log(day_durbin_watson(Volume))), 10), cross_mean(day_std(Amt), 30))` |
| R 1 variant 2 | 过 | 0.94 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.96 | 0.53 | 0.36 | 0.16 | 0.54 | 0.03 | `cs_bucket_demean(ts_sum(log(log(day_durbin_watson(Volume))), 10), LogFloatCap)` |
| R 1 variant 3 | 过 | 0.65 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.84 | 0.02 | 0.17 | 0.13 | 0.02 | 0.21 | `cs_bucket_demean(ts_sum(log(log(day_durbin_watson(Volume))), 10), cross_mean(day_sum(Amt), 20))` |
| R 1 variant 4 | 过 | 0.89 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.79 | 0.70 | 0.28 | 0.21 | 0.69 | 0.32 | `ts_sum(log(log(day_durbin_watson(div(Volume, cross_mean(Volume, 20))))), 10)` |
| R 1 variant 5 | 过 | 0.79 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.62 | 0.89 | 0.23 | 0.16 | 0.85 | 0.45 | `ts_sum(log(log(day_durbin_watson(sqrt(Volume)))), 10)` |
| R 1 variant 6 | 过 | 0.79 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.67 | 0.83 | 0.21 | 0.15 | 0.79 | 0.36 | `ts_sum(log(log(day_durbin_watson(in_mean_rolling(Volume, 3)))), 10)` |
| R 1 variant 7 | 过 | 0.95 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.95 | 0.68 | 0.31 | 0.18 | 0.67 | 0.28 | `ts_med(log(log(day_durbin_watson(Volume))), 10)` |
| R 2 variant 1 | 过 | 0.74 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.81 | 0.04 | 0.11 | 0.20 | 0.03 | 0.11 | `cs_bucket_demean(ts_sum(log(log(day_durbin_watson(Volume))), 5), cross_mean(day_std(Amt), 30))` |
| R 2 variant 2 | 过 | 0.47 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.84 | 0.12 | 0.02 | 0.10 | 0.07 | 0.14 | `cs_bucket_demean(ts_sum(log(log(day_durbin_watson(Volume))), 40), cross_mean(day_std(Amt), 30))` |
| R 3 variant 1 | 过 | 0.56 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.81 | 0.05 | 0.19 | 0.13 | 0.04 | 0.20 | `cs_bucket_demean(cross_fangzheng(log(log(day_durbin_watson(Volume))), 20), cross_mean(day_std(Amt), 30))` |
| R 3 variant 2 | 过 | 0.71 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.81 | 0.04 | 0.16 | 0.23 | 0.03 | 0.15 | `cs_bucket_demean(cross_fangzheng(log(log(day_durbin_watson(Volume))), 10), cross_mean(day_std(Amt), 30))` |
| R 3 variant 3 | 过 | 0.82 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.73 | 0.77 | 0.33 | 0.17 | 0.76 | 0.31 | `cross_fangzheng(log(log(day_durbin_watson(div(Volume, cross_mean(Volume, 20))))), 20)` |
| R 3 variant 4 | 过 | 0.95 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.96 | 0.53 | 0.37 | 0.20 | 0.54 | 0.02 | `cs_bucket_demean(cross_fangzheng(log(log(day_durbin_watson(Volume))), 10), LogFloatCap)` |
