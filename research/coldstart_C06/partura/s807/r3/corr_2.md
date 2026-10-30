# 相关度表:种子 807,C 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 24 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.60 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.58 | 0.02 | 0.22 | 0.10 | 0.07 | 0.30 | `div(cross_stddev(day_std(Ret), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 2 | 过 | 0.62 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.62 | 0.12 | 0.11 | 0.00 | 0.10 | 0.41 | `cross_stddev(ts_delta(log(day_std(Ret)), 1), 60)` |
| slot a seed 3 | 过 | 0.74 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.76 | 0.04 | 0.16 | 0.02 | 0.07 | 0.35 | `cross_stddev(ts_delta(log(cross_mean(day_std(Ret), 5)), 5), 60)` |
| slot a seed 4 | 过 | 0.60 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.58 | 0.10 | 0.10 | 0.00 | 0.08 | 0.41 | `cross_mean(abs_(ts_delta(log(day_std(Ret)), 1)), 60)` |
| slot a seed 5 | 过 | 0.54 | `ts_sum(LogFloatShares, 30)` | 0.47 | 0.06 | 0.06 | 0.01 | 0.05 | 0.34 | `cross_med(abs_(ts_delta(log(day_std(Ret)), 1)), 60)` |
| slot a seed 6 | 过 | 0.60 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.59 | 0.12 | 0.12 | 0.03 | 0.09 | 0.39 | `cross_semistd_pos(day_std(Ret), 60)` |
| slot a seed 7 | 过 | 0.61 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.60 | 0.13 | 0.09 | 0.03 | 0.10 | 0.42 | `cross_semistd_neg(day_std(Ret), 60)` |
| slot a seed 8 | 过 | 0.73 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.74 | 0.01 | 0.21 | 0.06 | 0.03 | 0.36 | `cross_semistd_pos(cross_mean(day_std(Ret), 5), 60)` |
| slot a seed 9 | 过 | 0.61 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.58 | 0.06 | 0.30 | 0.18 | 0.11 | 0.28 | `cross_stddev(cs_demean(log(day_std(Ret))), 20)` |
| slot a seed 10 | 过 | 0.38 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.37 | 0.30 | 0.09 | 0.00 | 0.29 | 0.03 | `cross_autocorr(log(day_std(Ret)), 60, 1)` |
| slot a seed 11 | 过 | 0.30 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.29 | 0.15 | 0.05 | 0.04 | 0.10 | 0.17 | `div(cross_stddev(log(div(day_max(High), day_min(Low))), 20), cross_mean(log(div(day_max(High), day_min(Low))), 20))` |
| slot a seed 12 | 过 | 0.62 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.61 | 0.11 | 0.21 | 0.09 | 0.04 | 0.32 | `div(cross_stddev(day_wstd(Ret, Amt), 20), cross_mean(day_wstd(Ret, Amt), 20))` |
| slot a seed 13 | 过 | 0.57 | `ts_sum(LogFloatShares, 30)` | 0.58 | 0.03 | 0.21 | 0.12 | 0.06 | 0.32 | `cross_mean(div(day_std(in_stddev_rolling(Ret, 30)), day_mean(in_stddev_rolling(Ret, 30))), 20)` |
| slot a seed 14 | 过 | 0.47 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.56 | 0.05 | 0.00 | 0.05 | 0.01 | 0.28 | `cs_bucket_rank(div(cross_stddev(day_std(Ret), 20), cross_mean(day_std(Ret), 20)), cross_mean(day_std(Ret), 20))` |
| slot a seed 15 | 过 | 0.64 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.61 | 0.00 | 0.15 | 0.01 | 0.02 | 0.34 | `cs_bucket_rank(cross_stddev(ts_delta(log(day_std(Ret)), 1), 60), cross_mean(day_sum(Amt), 30))` |
| slot b seed 1 | 过 | 0.47 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.42 | 0.15 | 0.18 | 0.06 | 0.08 | 0.28 | `div(cross_stddev(day_sum(Volume), 60), cross_mean(day_sum(Volume), 60))` |
| slot b seed 2 | 过 | 0.51 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.43 | 0.10 | 0.21 | 0.07 | 0.03 | 0.28 | `div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| slot b seed 3 | 过 | 0.38 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.29 | 0.09 | 0.19 | 0.17 | 0.03 | 0.17 | `div(cross_stddev(day_sum(Volume), 20), cross_mean(day_sum(Volume), 20))` |
| slot b seed 4 | 过 | 0.38 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.32 | 0.20 | 0.17 | 0.02 | 0.14 | 0.32 | `div(cross_stddev(day_sum(Volume), 120), cross_mean(day_sum(Volume), 120))` |
| slot b seed 5 | 过 | 0.56 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.47 | 0.05 | 0.26 | 0.05 | 0.02 | 0.27 | `cross_stddev(log(day_sum(Volume)), 60)` |
| slot b seed 6 | 过 | 0.30 | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` | 0.26 | 0.17 | 0.14 | 0.08 | 0.10 | 0.15 | `cross_stddev(ts_delta(log(day_sum(Volume)), 1), 60)` |
| slot b seed 7 | 过 | 0.26 | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` | 0.23 | 0.18 | 0.12 | 0.08 | 0.12 | 0.13 | `cross_mean(abs_(ts_delta(log(day_sum(Volume)), 1)), 60)` |
| slot b seed 8 | 过 | 0.35 | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` | 0.27 | 0.11 | 0.19 | 0.12 | 0.04 | 0.15 | `cross_semistd_pos(day_sum(Volume), 60)` |
| slot b seed 9 | 过 | 0.14 | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` | 0.18 | 0.25 | 0.02 | 0.01 | 0.20 | 0.11 | `cross_semistd_neg(day_sum(Volume), 60)` |
| slot b seed 10 | 过 | 0.39 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.23 | 0.01 | 0.29 | 0.31 | 0.07 | 0.07 | `div(cross_max(day_sum(Volume), 20), cross_med(day_sum(Volume), 60))` |
| slot b seed 11 | 过 | 0.36 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.26 | 0.18 | 0.21 | 0.03 | 0.13 | 0.32 | `div(cross_stddev(div(day_std(Ret), day_sum(Amt)), 60), cross_mean(div(day_std(Ret), day_sum(Amt)), 60))` |
| slot b seed 12 | 过 | 0.52 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.44 | 0.00 | 0.23 | 0.08 | 0.06 | 0.22 | `cs_bucket_rank(div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60)), cross_mean(day_sum(Amt), 30))` |
| slot b seed 13 | 过 | 0.37 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.40 | 0.03 | 0.12 | 0.09 | 0.09 | 0.01 | `cs_bucket_rank(div(cross_stddev(day_sum(Volume), 60), cross_mean(day_sum(Volume), 60)), LogFloatCap)` |
| slot b seed 14 | 过 | 0.13 | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` | 0.22 | 0.21 | 0.10 | 0.08 | 0.15 | 0.12 | `cs_regres(div(cross_stddev(day_sum(Volume), 60), cross_mean(day_sum(Volume), 60)), div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60)))` |
| R 1 variant 1 | 过 | 0.73 | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(` | 0.73 | 0.10 | 0.04 | 0.01 | 0.08 | 0.10 | `cross_corr(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| R 1 variant 2 | 过 | 0.90 | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(` | 0.90 | 0.27 | 0.14 | 0.09 | 0.30 | 0.10 | `cross_regbeta(day_std(Amt), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| R 2 variant 1 | 过 | 1.00 | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_d` | 0.99 | 0.07 | 0.04 | 0.02 | 0.07 | 0.06 | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), cs_winsor(inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10))))), 10)` |
| R 2 variant 2 | 过 | 0.80 | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_d` | 0.45 | 0.03 | 0.01 | 0.01 | 0.04 | 0.04 | `cross_corr(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)` |
| R 2 variant 3 | 过 | 0.97 | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_d` | 0.96 | 0.08 | 0.04 | 0.02 | 0.08 | 0.06 | `cross_regbeta(day_last(in_sum_rolling(Amt, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)` |
| R 3 variant 1 | 过 | 0.75 | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_rep` | 0.79 | 0.10 | 0.08 | 0.07 | 0.13 | 0.01 | `cross_regbeta(cs_normalize(day_std(Amt)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 15)` |
| R 4 variant 1 | 过 | 0.83 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.86 | 0.09 | 0.19 | 0.01 | 0.12 | 0.34 | `ts_sum(cross_stddev(log(day_std(Ret)), 60), 1)` |
| R 4 variant 2 | 过 | 0.83 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` | 0.82 | 0.10 | 0.26 | 0.03 | 0.14 | 0.34 | `ts_sum(cross_stddev(cs_demean(log(day_std(Ret))), 60), 1)` |
| R 5 variant 1 | 过 | 0.40 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(da` | 0.31 | 0.46 | 0.00 | 0.09 | 0.42 | 0.42 | `day_quantile(Open)` |
