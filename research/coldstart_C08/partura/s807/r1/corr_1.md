# 相关度表:种子 807,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.16 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.09 | 0.37 | 0.51 | 0.07 | 0.39 | 0.07 | `ts_var(LogFloatCap, 20)` |
| slot a seed 1 | 过 | 0.08 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.06 | 0.29 | 0.02 | 0.02 | 0.27 | 0.03 | `sub(log(ts_var(LogFloatCap, 20)), log(cross_mean(day_var(Ret), 20)))` |
| slot a seed 2 | 过 | 0.10 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.09 | 0.40 | 0.02 | 0.02 | 0.36 | 0.06 | `cross_mean(sub(log(ts_var(LogFloatCap, 20)), log(cross_mean(day_var(Ret), 20))), 60)` |
| slot a seed 3 | 过 | 0.02 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_re` | 0.02 | 0.02 | 0.07 | 0.06 | 0.02 | 0.02 | `cross_regres(log(cross_mean(day_var(Ret), 20)), log(ts_var(LogFloatCap, 20)), 120)` |
| slot a seed 4 | 过 | 0.05 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.02 | 0.07 | 0.03 | 0.06 | 0.08 | 0.04 | `sub(log(ts_var(LogFloatCap, 20)), mul(2, log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20))))` |
| slot a seed 5 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.08 | 0.34 | 0.41 | 0.04 | 0.34 | 0.14 | `cross_mean(ts_var(LogFloatCap, 20), 120)` |
| slot a seed 6 | 过 | 0.13 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.07 | 0.43 | 0.48 | 0.04 | 0.43 | 0.10 | `cross_med(ts_var(LogFloatCap, 20), 60)` |
| slot a seed 7 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.09 | 0.30 | 0.40 | 0.04 | 0.30 | 0.14 | `cross_tail_mean_q75(ts_var(LogFloatCap, 20), 120)` |
| slot a seed 8 | 过 | 0.08 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.08 | 0.09 | 0.20 | 0.13 | 0.11 | 0.04 | `cross_zscore(ts_var(LogFloatCap, 20), 120)` |
| slot a seed 9 | 过 | 0.07 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.08 | 0.12 | 0.20 | 0.13 | 0.14 | 0.05 | `sub(log(ts_var(LogFloatCap, 20)), log(cross_mean(ts_var(LogFloatCap, 20), 120)))` |
| slot a seed 10 | 过 | 0.09 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.09 | 0.06 | 0.04 | 0.02 | 0.04 | 0.01 | `div(cross_stddev(ts_var(LogFloatCap, 20), 60), cross_mean(ts_var(LogFloatCap, 20), 60))` |
| slot a seed 11 | 过 | 0.13 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.07 | 0.50 | 0.47 | 0.04 | 0.49 | 0.01 | `cross_mean(cs_bucket_rank(ts_var(LogFloatCap, 20), LogFloatCap), 60)` |
| slot a seed 12 | 过 | 0.14 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.10 | 0.36 | 0.38 | 0.03 | 0.38 | 0.06 | `cs_bucket_zscore(cross_mean(ts_var(LogFloatCap, 20), 60), BoardCode)` |
| slot a seed 13 | 过 | 0.06 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.12 | 0.07 | 0.08 | 0.00 | 0.06 | 0.40 | `cross_mean(sub(log(ts_var(LogFloatCap, 20)), sub(log(day_sum(Amt)), LogFloatCap)), 60)` |
| slot a seed 14 | 过 | 0.30 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.33 | 0.18 | 0.20 | 0.13 | 0.20 | 0.07 | `cross_corr(ts_var(LogFloatCap, 20), log(day_sum(Amt)), 60)` |
| slot b seed 1 | 过 | 0.15 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.13 | 0.10 | 0.21 | 0.07 | 0.03 | 0.28 | `div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| slot b seed 2 | 过 | 0.11 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.11 | 0.15 | 0.20 | 0.02 | 0.09 | 0.32 | `div(cross_stddev(day_sum(Amt), 120), cross_mean(day_sum(Amt), 120))` |
| slot b seed 3 | 过 | 0.16 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.13 | 0.01 | 0.30 | 0.06 | 0.07 | 0.27 | `cross_stddev(log(day_sum(Amt)), 60)` |
| slot b seed 4 | 过 | 0.11 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.11 | 0.08 | 0.24 | 0.00 | 0.03 | 0.30 | `cross_stddev(sub(log(day_sum(Amt)), LogFloatCap), 120)` |
| slot b seed 5 | 过 | 0.16 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.14 | 0.06 | 0.31 | 0.06 | 0.00 | 0.27 | `cross_stddev(log(day_quantile_q75(Amt)), 60)` |
| slot b seed 6 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.12 | 0.07 | 0.30 | 0.01 | 0.02 | 0.29 | `cross_stddev(log(day_quantile_q75(Amt)), 120)` |
| slot b seed 7 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.12 | 0.16 | 0.14 | 0.07 | 0.10 | 0.26 | `sub(log(cross_max(day_sum(Amt), 60)), log(cross_med(day_sum(Amt), 60)))` |
| slot b seed 8 | 过 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.11 | 0.02 | 0.28 | 0.01 | 0.03 | 0.29 | `sub(log(cross_tail_mean_q75(day_sum(Amt), 120)), log(cross_tail_mean_q25(day_sum(Amt), 120)))` |
| slot b seed 9 | 过 | 0.11 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.11 | 0.14 | 0.18 | 0.09 | 0.07 | 0.17 | `cross_stddev(cross_delta(log(day_sum(Amt)), 1), 60)` |
| slot b seed 10 | 过 | 0.11 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.07 | 0.20 | 0.22 | 0.15 | 0.21 | 0.02 | `cross_mean(abs_(cross_zscore(day_sum(Amt), 20)), 60)` |
| slot b seed 11 | 过 | 0.14 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.11 | 0.15 | 0.15 | 0.01 | 0.17 | 0.26 | `div(cross_stddev(cross_mean(day_std(Ret), 5), 60), cross_mean(day_std(Ret), 60))` |
| slot b seed 12 | 过 | 0.10 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.09 | 0.08 | 0.16 | 0.02 | 0.09 | 0.37 | `cross_stddev(log(day_std(Ret)), 120)` |
| slot b seed 13 | 过 | 0.17 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.13 | 0.18 | 0.25 | 0.09 | 0.23 | 0.01 | `cs_bucket_zscore(cross_stddev(log(day_sum(Amt)), 60), LogFloatCap)` |
| slot b seed 14 | 过 | 0.17 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.13 | 0.04 | 0.27 | 0.04 | 0.10 | 0.35 | `add(cs_rank(cross_stddev(log(day_sum(Amt)), 60)), cs_rank(cross_stddev(log(day_std(Ret)), 60)))` |
| R 1 variant 1 | 过 | 0.92 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.94 | 0.09 | 0.17 | 0.13 | 0.11 | 0.01 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)` |
| R 1 variant 2 | 过 | 0.48 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.56 | 0.11 | 0.22 | 0.09 | 0.14 | 0.04 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)` |
| R 1 variant 3 | 过 | 0.34 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.49 | 0.12 | 0.19 | 0.04 | 0.14 | 0.01 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(ts_var(LogFloatCap, 50), ts_var(LogFloatCap, 20)), LimitWidth), 60)` |
| R 1 variant 4 | 过 | 0.48 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.55 | 0.21 | 0.25 | 0.12 | 0.23 | 0.03 | `cross_corr(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)` |
| R 1 variant 5 | 过 | 0.50 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.56 | 0.15 | 0.24 | 0.10 | 0.18 | 0.02 | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)` |
| R 1 variant 6 | 过 | 0.36 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.41 | 0.06 | 0.22 | 0.09 | 0.08 | 0.12 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LogFloatCap), 60)` |
| R 2 variant 1 | 过 | 0.48 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.70 | 0.15 | 0.18 | 0.04 | 0.16 | 0.00 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 60)` |
| R 2 variant 2 | 过 | 0.46 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.66 | 0.15 | 0.18 | 0.03 | 0.16 | 0.00 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 30), BoardCode), 60)` |
| R 2 variant 3 | 过 | 0.37 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.52 | 0.09 | 0.19 | 0.04 | 0.11 | 0.07 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 30), LogFloatCap), 60)` |
| R 2 variant 4 | 过 | 0.38 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.54 | 0.15 | 0.21 | 0.06 | 0.16 | 0.00 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)` |
| R 2 variant 5 | 过 | 0.36 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.53 | 0.13 | 0.14 | 0.01 | 0.14 | 0.01 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 40), LimitWidth), 60)` |
| R 2 variant 6 | 过 | 0.48 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add` | 0.68 | 0.19 | 0.21 | 0.06 | 0.21 | 0.03 | `cross_corr(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 30), LimitWidth), 60)` |
