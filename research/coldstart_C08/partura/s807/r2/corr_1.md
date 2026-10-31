# 相关度表:种子 807,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.17 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.07 | 0.16 | 0.72 | 0.29 | 0.21 | 0.06 | `day_std(Ret)` |
| slot a seed 1 | 过 | 0.69 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.65 | 0.17 | 0.10 | 0.00 | 0.15 | 0.43 | `cross_semistd_pos(day_std(Ret), 120)` |
| slot a seed 2 | 过 | 0.71 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.64 | 0.18 | 0.08 | 0.04 | 0.16 | 0.47 | `cross_semistd_neg(day_std(Ret), 120)` |
| slot a seed 3 | 过 | 0.20 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.18 | 0.01 | 0.09 | 0.08 | 0.01 | 0.06 | `sub(cross_semistd_pos(day_std(Ret), 120), cross_semistd_neg(day_std(Ret), 120))` |
| slot a seed 4 | 过 | 0.09 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.08 | 0.01 | 0.09 | 0.08 | 0.03 | 0.00 | `div(cross_semistd_pos(day_std(Ret), 120), cross_semistd_neg(day_std(Ret), 120))` |
| slot a seed 5 | 过 | 0.62 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.53 | 0.12 | 0.12 | 0.03 | 0.09 | 0.39 | `cross_semistd_pos(day_std(Ret), 60)` |
| slot a seed 6 | 过 | 0.65 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.54 | 0.13 | 0.09 | 0.03 | 0.10 | 0.42 | `cross_semistd_neg(day_std(Ret), 60)` |
| slot a seed 7 | 过 | 0.27 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.21 | 0.28 | 0.07 | 0.02 | 0.27 | 0.06 | `cross_autocorr(day_std(Ret), 60, 1)` |
| slot a seed 8 | 过 | 0.43 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.40 | 0.33 | 0.06 | 0.01 | 0.32 | 0.06 | `cross_autocorr(log(day_std(Ret)), 120, 1)` |
| slot a seed 9 | 废品 | 0.20 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.22 | 0.29 | 0.00 | 0.00 | 0.26 | 0.19 | `cross_hurst(day_std(Ret), 120)` |
| slot a seed 10 | 过 | 0.26 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.20 | 0.19 | 0.18 | 0.06 | 0.23 | 0.03 | `cross_zscore(cross_stddev(log(day_std(Ret)), 60), 240)` |
| slot a seed 11 | 过 | 0.93 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.91 | 0.12 | 0.24 | 0.02 | 0.15 | 0.28 | `cs_bucket_demean(cross_stddev(log(log(log(day_std(Ret)))), 120), BoardCode)` |
| slot a seed 12 | 过 | 0.89 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.97 | 0.37 | 0.24 | 0.02 | 0.38 | 0.01 | `cs_bucket_zscore(cross_stddev(log(log(log(day_std(Ret)))), 120), LogFloatCap)` |
| slot a seed 13 | 过 | 0.27 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.30 | 0.13 | 0.03 | 0.04 | 0.14 | 0.06 | `cross_regres(cross_mean(day_std(Ret), 20), cross_stddev(log(day_std(Ret)), 120), 120)` |
| slot a seed 14 | 过 | 0.94 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.94 | 0.03 | 0.15 | 0.03 | 0.05 | 0.40 | `div(cross_stddev(day_std(Ret), 120), cross_mean(day_std(Ret), 120))` |
| slot b seed 1 | 过 | 0.12 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.04 | 0.74 | 0.09 | 0.12 | 0.70 | 0.46 | `div(day_quantile_q75(Amt), day_quantile_q25(Amt))` |
| slot b seed 2 | 废品 | 0.10 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.11 | 0.76 | 0.14 | 0.02 | 0.68 | 0.52 | `cross_mean(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60)` |
| slot b seed 3 | 废品 | 0.09 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.11 | 0.71 | 0.20 | 0.01 | 0.64 | 0.53 | `cross_mean(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 120)` |
| slot b seed 4 | 过 | 0.14 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.12 | 0.85 | 0.00 | 0.02 | 0.78 | 0.55 | `cross_med(div(day_quantile_q75(Volume), day_quantile_q25(Volume)), 60)` |
| slot b seed 5 | 废品 | 0.10 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.11 | 0.76 | 0.14 | 0.02 | 0.68 | 0.52 | `log(cross_mean(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60))` |
| slot b seed 6 | 废品 | 0.12 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.14 | 0.54 | 0.24 | 0.04 | 0.47 | 0.44 | `cross_stddev(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60)` |
| slot b seed 7 | 过 | 0.09 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.09 | 0.05 | 0.13 | 0.21 | 0.07 | 0.03 | `cross_zscore(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60)` |
| slot b seed 8 | 废品 | 0.10 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.08 | 0.73 | 0.15 | 0.01 | 0.66 | 0.56 | `cs_bucket_demean(cross_mean(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60), ListAge)` |
| slot b seed 9 | 废品 | 0.10 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.09 | 0.73 | 0.15 | 0.01 | 0.66 | 0.55 | `cs_bucket_demean(cross_mean(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60), BoardCode)` |
| slot b seed 10 | 废品 | 0.24 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.12 | 0.48 | 0.04 | 0.09 | 0.41 | 0.01 | `cs_bucket_zscore(cross_mean(div(day_quantile_q75(Amt), day_quantile_q25(Amt)), 60), LogFloatCap)` |
| slot b seed 11 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.14 | 0.80 | 0.09 | 0.03 | 0.71 | 0.53 | `cross_mean(day_gini(Amt), 60)` |
| slot b seed 12 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.14 | 0.80 | 0.09 | 0.03 | 0.71 | 0.53 | `cross_mean(day_gini(Volume), 60)` |
| slot b seed 13 | 过 | 0.14 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.05 | 0.08 | 0.09 | 0.03 | 0.08 | 0.10 | `cs_rank(ListAge)` |
| R 1 variant 1 | 过 | 0.58 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var` | 0.52 | 0.08 | 0.22 | 0.04 | 0.10 | 0.10 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)` |
| R 1 variant 2 | 过 | 0.71 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var` | 0.67 | 0.10 | 0.22 | 0.06 | 0.12 | 0.07 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 90)` |
| R 1 variant 3 | 过 | 0.95 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var` | 0.94 | 0.12 | 0.22 | 0.09 | 0.14 | 0.04 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), BoardCode), 60)` |
| R 1 variant 4 | 过 | 0.59 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var` | 0.53 | 0.14 | 0.24 | 0.05 | 0.15 | 0.07 | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)` |
| R 1 variant 5 | 过 | 0.48 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var` | 0.41 | 0.03 | 0.23 | 0.04 | 0.05 | 0.19 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LogFloatCap), 120)` |
| R 2 variant 1 | 过 | 0.91 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_` | 0.92 | 0.15 | 0.22 | 0.08 | 0.17 | 0.00 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)` |
| R 2 variant 2 | 过 | 0.54 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_` | 0.53 | 0.13 | 0.23 | 0.04 | 0.14 | 0.06 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 120)` |
| R 2 variant 3 | 过 | 0.80 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var` | 0.77 | 0.15 | 0.19 | 0.06 | 0.16 | 0.00 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 30), LimitWidth), 60)` |
| R 2 variant 4 | 过 | 0.85 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_` | 0.88 | 0.21 | 0.24 | 0.10 | 0.23 | 0.04 | `cross_corr(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)` |
| R 3 variant 1 | 过 | 0.98 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.97 | 0.17 | 0.19 | 0.10 | 0.19 | 0.06 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` |
| R 3 variant 2 | 过 | 0.52 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.54 | 0.12 | 0.16 | 0.12 | 0.14 | 0.03 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 30)` |
| R 3 variant 3 | 过 | 0.95 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` | 0.95 | 0.16 | 0.19 | 0.10 | 0.18 | 0.06 | `cross_corr(ts_var(LogFloatCap, 20), log(day_sum(Volume)), 60)` |
