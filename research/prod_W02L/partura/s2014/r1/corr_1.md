# 相关度表:种子 2014,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.44 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.09 | 0.46 | 0.01 | 0.07 | 0.42 | 0.43 | `day_quantile_q25(High)` |
| slot a seed 1 | 过 | 0.14 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.07 | 0.17 | 0.03 | 0.01 | 0.18 | 0.45 | `sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 2 | 过 | 0.14 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.07 | 0.17 | 0.03 | 0.01 | 0.18 | 0.45 | `cross_mean(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), 20)` |
| slot a seed 3 | 废品 | 0.05 | `ts_std(day_quantile_q25(Ret), 10)` | 0.06 | 0.03 | 0.16 | 0.04 | 0.01 | 0.09 | `cross_delta(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), 241)` |
| slot a seed 4 | 过 | 0.08 | `ts_std(day_quantile_q25(Ret), 10)` | 0.04 | 0.05 | 0.25 | 0.19 | 0.07 | 0.05 | `cross_delta(cross_mean(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), 20), 120)` |
| slot a seed 5 | 过 | 0.07 | `ts_std(day_quantile_q25(Ret), 10)` | 0.07 | 0.05 | 0.02 | 0.02 | 0.03 | 0.02 | `cs_bucket_zscore(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), LogFloatCap)` |
| slot a seed 6 | 过 | 0.30 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.02 | 0.33 | 0.01 | 0.04 | 0.32 | 0.47 | `cs_bucket_zscore(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 7 | 过 | 0.33 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.02 | 0.35 | 0.01 | 0.05 | 0.34 | 0.49 | `cs_bucket_rank(day_quantile_q25(High), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 8 | 过 | 0.16 | `ts_std(day_quantile_q25(Ret), 10)` | 0.17 | 0.08 | 0.06 | 0.03 | 0.04 | 0.23 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), day_quantile_q25(High))` |
| slot a seed 9 | 废品 | 0.28 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.15 | 0.36 | 0.22 | 0.04 | 0.35 | 0.21 | `sub(cross_delta(log(day_quantile_q25(High)), 241), cross_delta(log(day_quantile_q25(High)), 20))` |
| slot a seed 10 | 废品 | 0.04 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.05 | 0.04 | 0.12 | 0.04 | 0.02 | 0.13 | `cs_bucket_demean(cross_delta(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), 241), LogFloatCap)` |
| slot a seed 11 | 过 | 0.28 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.36 | 0.31 | 0.33 | 0.32 | 0.32 | 0.16 | `cross_delta(log(day_quantile_q25(High)), 120)` |
| slot a seed 12 | 过 | 0.09 | `ts_std(day_quantile_q25(Ret), 10)` | 0.07 | 0.04 | 0.03 | 0.01 | 0.02 | 0.08 | `cs_regres(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), LogFloatCap)` |
| slot a seed 13 | 废品 | 0.06 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.04 | 0.06 | 0.26 | 0.10 | 0.08 | 0.12 | `cs_bucket_rank(cross_delta(cross_mean(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), 20), 241), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 14 | 过 | 0.13 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.08 | 0.16 | 0.03 | 0.02 | 0.18 | 0.49 | `sub(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), sub(LogTotalCap, LogFloatCap))` |
| slot b seed 1 | 过 | 0.29 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.25 | 0.28 | 0.04 | 0.06 | 0.23 | 0.02 | `sub(LogFloatCap, LogFloatShares)` |
| slot b seed 2 | 过 | 0.24 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.23 | 0.25 | 0.02 | 0.07 | 0.20 | 0.00 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot b seed 3 | 过 | 0.21 | `ts_std(day_quantile_q25(Ret), 10)` | 0.22 | 0.01 | 0.13 | 0.02 | 0.04 | 0.20 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), cross_mean(day_sum(Amt), 20))` |
| slot b seed 4 | 过 | 0.28 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.28 | 0.29 | 0.00 | 0.06 | 0.24 | 0.03 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), cross_mean(day_std(Ret), 20))` |
| slot b seed 5 | 过 | 0.25 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.24 | 0.24 | 0.03 | 0.05 | 0.19 | 0.08 | `cs_regres(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot b seed 6 | 过 | 0.39 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.25 | 0.45 | 0.13 | 0.16 | 0.40 | 0.08 | `add(log(add(abs_(day_quantile_q25(Ret)), 0.000001)), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 7 | 过 | 0.48 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.30 | 0.54 | 0.13 | 0.02 | 0.47 | 0.12 | `cross_mean(add(log(add(abs_(day_quantile_q25(Ret)), 0.000001)), sub(LogFloatCap, LogFloatShares)), 20)` |
| slot b seed 8 | 过 | 0.29 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.11 | 0.27 | 0.90 | 0.22 | 0.33 | 0.15 | `cs_bucket_rank(cross_mean(day_std(Ret), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 9 | 过 | 0.54 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.08 | 0.68 | 0.41 | 0.01 | 0.65 | 0.35 | `cs_bucket_rank(cross_mean(day_zero_ratio(Ret), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 10 | 过 | 0.57 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.07 | 0.70 | 0.42 | 0.01 | 0.68 | 0.37 | `cs_bucket_rank(cross_mean(day_flat_ratio(Close), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 11 | 过 | 0.41 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.10 | 0.47 | 0.64 | 0.03 | 0.48 | 0.03 | `cs_bucket_zscore(cross_mean(day_distinct_ratio(Close), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 12 | 过 | 0.50 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.19 | 0.60 | 0.61 | 0.13 | 0.60 | 0.19 | `cs_bucket_rank(cross_mean(day_quantile_q25(Ret), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 13 | 过 | 0.65 | `ts_std(day_quantile_q25(Ret), 10)` | 0.71 | 0.12 | 0.41 | 0.17 | 0.15 | 0.09 | `cs_bucket_rank(cross_stddev(day_quantile_q25(Ret), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 14 | 过 | 0.18 | `ts_std(day_quantile_q25(Ret), 10)` | 0.24 | 0.13 | 0.01 | 0.04 | 0.08 | 0.22 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogTotalCap)` |
| slot b seed 15 | 过 | 0.31 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.21 | 0.34 | 0.07 | 0.08 | 0.29 | 0.22 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), sub(LogTotalCap, LogFloatCap))` |
| slot b seed 16 | 过 | 0.53 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.21 | 0.55 | 0.11 | 0.09 | 0.49 | 0.56 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatShares)` |
| R 1 variant 1 | 过 | 0.73 | `ts_std(day_quantile_q25(Ret), 10)` | 0.86 | 0.13 | 0.17 | 0.12 | 0.14 | 0.00 | `ts_std(day_quantile_q25(Ret), 5)` |
| R 1 variant 2 | 过 | 0.51 | `ts_std(day_quantile_q25(Ret), 10)` | 0.66 | 0.21 | 0.16 | 0.12 | 0.21 | 0.02 | `ts_std(day_quantile_q25(Ret), 3)` |
| R 1 variant 3 | 过 | 0.59 | `ts_std(day_quantile_q25(Ret), 10)` | 0.69 | 0.30 | 0.06 | 0.01 | 0.26 | 0.11 | `div(ts_std(day_quantile_q25(Ret), 5), abs_(ts_mean(day_quantile_q25(Ret), 5)))` |
| R 1 variant 4 | 过 | 0.63 | `ts_std(day_quantile_q25(Ret), 10)` | 0.77 | 0.05 | 0.20 | 0.12 | 0.07 | 0.04 | `cs_bucket_zscore(ts_std(day_quantile_q25(Ret), 5), sub(LogFloatCap, LogFloatShares))` |
| R 1 variant 5 | 过 | 0.59 | `ts_std(day_quantile_q25(Ret), 10)` | 0.66 | 0.08 | 0.00 | 0.10 | 0.08 | 0.03 | `ts_std(cross_zscore(day_quantile_q25(Ret), 60), 5)` |
| R 2 variant 1 | 过 | 0.99 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.96 | 0.83 | 0.04 | 0.04 | 0.80 | 0.52 | `cross_stddev(day_quantile_q25(Amt), 241)` |
| R 2 variant 2 | 过 | 0.99 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.95 | 0.85 | 0.00 | 0.04 | 0.80 | 0.57 | `cross_mean(day_quantile_q25(Amt), 241)` |
| R 2 variant 3 | 过 | 0.55 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.09 | 0.54 | 0.16 | 0.03 | 0.48 | 0.49 | `div(cross_stddev(day_quantile_q25(Amt), 241), cross_mean(day_quantile_q25(Amt), 241))` |
| R 2 variant 4 | 过 | 0.77 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.83 | 0.58 | 0.11 | 0.10 | 0.56 | 0.02 | `cs_bucket_zscore(cross_fangzheng(day_quantile_q25(Amt), 241), LogFloatCap)` |
| R 2 variant 5 | 过 | 0.43 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.76 | 0.01 | 0.33 | 0.07 | 0.04 | 0.10 | `cs_bucket_zscore(cross_fangzheng(day_quantile_q25(Amt), 241), cross_mean(day_sum(Amt), 60))` |
| R 3 variant 1 | 过 | 0.81 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.49 | 0.80 | 0.17 | 0.01 | 0.80 | 0.44 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 60)` |
| R 3 variant 2 | 过 | 0.75 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.33 | 0.74 | 0.11 | 0.04 | 0.73 | 0.42 | `cross_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 120)` |
| R 3 variant 3 | 过 | 0.83 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.53 | 0.82 | 0.21 | 0.01 | 0.83 | 0.45 | `ts_max(log(cross_regbeta(cs_sum(day_quantile_q25(Low)), day_last(Amt), 10)), 40)` |
| R 3 variant 4 | 过 | 0.78 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.39 | 0.80 | 0.17 | 0.01 | 0.80 | 0.44 | `ts_max(log(cross_regbeta(cs_sum(day_quantile_q25(Low)), day_last(Amt), 10)), 60)` |
| R 3 variant 5 | 过 | 0.12 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.14 | 0.07 | 0.04 | 0.01 | 0.08 | 0.04 | `ts_max(cross_corr(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10), 40)` |
