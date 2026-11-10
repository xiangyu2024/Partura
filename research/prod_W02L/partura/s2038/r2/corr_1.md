# 相关度表:种子 2038,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.61 | `ts_decay_linear(day_open(Volume), 5)` | 0.37 | 0.81 | 0.26 | 0.20 | 0.81 | 0.54 | `day_last(Amt)` |
| slot a seed 1 | 过 | 0.30 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.23 | 0.49 | 0.31 | 0.03 | 0.49 | 0.02 | `cs_first_low20(cross_mean(day_last(Amt), 20), LogFloatShares)` |
| slot a seed 2 | 过 | 0.28 | `ts_decay_linear(day_open(Volume), 5)` | 0.09 | 0.18 | 0.08 | 0.03 | 0.17 | 0.45 | `cs_first_low20(div(day_last(Amt), add(day_sum(Amt), 1)), LogFloatShares)` |
| slot a seed 3 | 过 | 0.21 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.21 | 0.06 | 0.34 | 0.11 | 0.08 | 0.53 | `cs_first_low20(sub(log(add(day_last(Amt), 1)), LogFloatCap), LogFloatShares)` |
| slot a seed 4 | 过 | 0.30 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.34 | 0.68 | 0.32 | 0.14 | 0.67 | 0.39 | `cs_first_low20(day_last(Amt), sub(LogFloatShares, LogFloatCap))` |
| slot a seed 5 | 过 | 0.67 | `ts_decay_linear(day_open(Volume), 5)` | 0.55 | 0.46 | 0.32 | 0.13 | 0.50 | 0.41 | `cs_first_high20(day_last(Amt), sub(LogFloatShares, LogFloatCap))` |
| slot a seed 6 | 过 | 0.47 | `ts_decay_linear(day_open(Volume), 5)` | 0.19 | 0.44 | 0.09 | 0.14 | 0.45 | 0.52 | `cs_first_low40(day_last(Amt), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 7 | 过 | 0.33 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.18 | 0.53 | 0.27 | 0.05 | 0.53 | 0.06 | `cs_first_low20(cross_ema(day_last(Amt), 5), ListAge)` |
| slot a seed 8 | 过 | 0.33 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.18 | 0.58 | 0.32 | 0.14 | 0.57 | 0.14 | `cs_last_low10(cs_first_low20(day_last(Amt), LogFloatShares), day_sum(Amt))` |
| slot a seed 9 | 过 | 0.42 | `ts_decay_linear(day_open(Volume), 5)` | 0.31 | 0.72 | 0.30 | 0.20 | 0.72 | 0.31 | `cs_bucket_rank(day_last(Amt), LogFloatShares)` |
| slot a seed 10 | 过 | 0.24 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.43 | 0.23 | 0.24 | 0.01 | 0.22 | 0.29 | `cs_first_low40(cross_ema(day_last(Amt), 10), LogFloatShares)` |
| slot a seed 11 | 过 | 0.15 | `ts_decay_linear(day_open(Volume), 5)` | 0.32 | 0.12 | 0.21 | 0.25 | 0.10 | 0.36 | `cs_first_low20(cross_zscore(day_last(Amt), 60), LogFloatShares)` |
| slot a seed 12 | 过 | 0.20 | `ts_decay_linear(day_open(Volume), 5)` | 0.33 | 0.23 | 0.23 | 0.30 | 0.21 | 0.43 | `cs_first_low20(sub(cross_mean(day_last(Amt), 5), cross_mean(day_last(Amt), 60)), LogFloatShares)` |
| slot a seed 13 | 过 | 0.27 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.25 | 0.45 | 0.31 | 0.05 | 0.46 | 0.03 | `cs_first_low20(cross_max(day_last(Amt), 20), LogFloatShares)` |
| slot a seed 14 | 过 | 0.28 | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt)` | 0.21 | 0.04 | 0.25 | 0.02 | 0.06 | 0.40 | `cs_first_low20(cross_ema(cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 60), LogFloatShares)` |
| slot a seed 15 | 过 | 0.11 | `ts_decay_linear(day_open(Volume), 5)` | 0.21 | 0.09 | 0.17 | 0.03 | 0.06 | 0.01 | `cs_bucket_rank(cross_mean(div(day_last(Amt), add(day_sum(Amt), 1)), 20), LogFloatCap)` |
| slot a seed 16 | 过 | 0.28 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.20 | 0.43 | 0.26 | 0.11 | 0.42 | 0.03 | `add(cs_first_low20(day_last(Amt), LogFloatShares), cs_first_low20(day_last(Amt), ListAge))` |
| slot b seed 1 | 过 | 0.23 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.23 | 0.01 | 0.30 | 0.28 | 0.02 | 0.01 | `cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 60), LogFloatCap)` |
| slot b seed 2 | 过 | 0.18 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.21 | 0.02 | 0.35 | 0.18 | 0.04 | 0.02 | `cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 120), LogFloatShares)` |
| slot b seed 3 | 过 | 0.26 | `ts_decay_linear(day_open(Volume), 5)` | 0.24 | 0.05 | 0.26 | 0.32 | 0.07 | 0.21 | `cs_bucket_zscore(cross_ema(day_signed_ratio(Ret, Amt), 40), cross_mean(day_sum(Amt), 60))` |
| slot b seed 4 | 过 | 0.31 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.29 | 0.30 | 0.45 | 0.11 | 0.33 | 0.00 | `cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap)` |
| slot b seed 5 | 过 | 0.66 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.64 | 0.62 | 0.32 | 0.05 | 0.61 | 0.01 | `cs_bucket_rank(cross_mean(day_autocorr_n1(Volume), 60), LogFloatCap)` |
| slot b seed 6 | 过 | 0.58 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.49 | 0.53 | 0.28 | 0.06 | 0.50 | 0.01 | `cs_bucket_rank(cross_mean(day_autocorr_n1(Volume), 60), cross_mean(day_sum(Volume), 60))` |
| slot b seed 7 | 过 | 0.68 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.68 | 0.79 | 0.29 | 0.01 | 0.78 | 0.26 | `cs_bucket_zscore(cross_ema(day_autocorr_n1(Amt), 30), LogFloatShares)` |
| slot b seed 8 | 过 | 0.44 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.37 | 0.48 | 0.43 | 0.01 | 0.51 | 0.00 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 60), LogFloatCap)` |
| slot b seed 9 | 过 | 0.36 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.32 | 0.14 | 0.21 | 0.28 | 0.11 | 0.00 | `cs_bucket_rank(mul(cross_mean(day_autocorr_n1(Volume), 60), cross_mean(day_signed_ratio(Ret, Amt), 60)), LogFloatCap)` |
| slot b seed 10 | 过 | 0.24 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.24 | 0.02 | 0.29 | 0.29 | 0.01 | 0.01 | `cross_mean(cs_bucket_rank(day_signed_ratio(Ret, Amt), LogFloatCap), 60)` |
| slot b seed 11 | 过 | 0.16 | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), ` | 0.03 | 0.09 | 0.08 | 0.28 | 0.09 | 0.00 | `cs_bucket_rank(cross_zscore(cross_mean(day_signed_ratio(Ret, Amt), 5), 120), LogFloatCap)` |
| slot b seed 12 | 过 | 0.58 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.50 | 0.54 | 0.28 | 0.05 | 0.52 | 0.01 | `cs_regres(cross_mean(day_autocorr_n1(Volume), 60), cross_mean(log(add(day_sum(Volume), 1)), 60))` |
| slot b seed 13 | 过 | 0.19 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.22 | 0.07 | 0.33 | 0.28 | 0.09 | 0.05 | `cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Volume), 60), ListAge)` |
| slot b seed 14 | 过 | 0.35 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.72 | 0.37 | 0.18 | 0.07 | 0.32 | 0.02 | `cs_bucket_demean(cross_mean(day_pos_ratio(Ret), 60), LogFloatCap)` |
| R 1 variant 1 | 过 | 0.59 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.61 | 0.48 | 0.25 | 0.01 | 0.50 | 0.04 | `cross_max(day_autocorr_n1(Volume), 60)` |
| R 1 variant 2 | 过 | 0.58 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.60 | 0.45 | 0.25 | 0.01 | 0.47 | 0.00 | `cs_bucket_rank(cross_max(day_autocorr_n1(Volume), 60), LogFloatCap)` |
| R 1 variant 3 | 过 | 0.40 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.43 | 0.18 | 0.27 | 0.02 | 0.20 | 0.34 | `cs_first_low20(cross_max(day_autocorr_n1(Volume), 60), LogFloatShares)` |
| R 1 variant 4 | 过 | 0.65 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.63 | 0.60 | 0.32 | 0.04 | 0.60 | 0.02 | `cross_mean(cs_bucket_rank(day_autocorr_n1(Volume), LogFloatCap), 60)` |
| R 2 variant 1 | 过 | 0.66 | `ts_decay_linear(day_open(Volume), 5)` | 0.91 | 0.12 | 0.14 | 0.34 | 0.16 | 0.06 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt), 20), 1))` |
| R 2 variant 2 | 过 | 0.58 | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), ` | 0.56 | 0.07 | 0.17 | 0.16 | 0.06 | 0.34 | `cs_first_low20(div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1)), LogFloatShares)` |
| R 2 variant 3 | 过 | 0.98 | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), ` | 0.98 | 0.08 | 0.09 | 0.26 | 0.11 | 0.00 | `cs_bucket_rank(div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1)), LogFloatCap)` |
| R 3 variant 1 | 过 | 0.67 | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt)` | 0.72 | 0.02 | 0.28 | 0.01 | 0.01 | 0.43 | `cs_first_low20(ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 50), LogFloatShares)` |
| R 3 variant 2 | 过 | 0.99 | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt)` | 0.99 | 0.27 | 0.24 | 0.04 | 0.31 | 0.00 | `cs_bucket_rank(ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 50), LogFloatCap)` |
| R 4 variant 1 | 过 | 0.37 | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), ` | 0.49 | 0.06 | 0.25 | 0.13 | 0.02 | 0.39 | `cs_first_low20(ts_decay_linear(div(day_open(Volume), add(day_sum(Volume), 1)), 5), LogFloatShares)` |
| R 4 variant 2 | 过 | 0.88 | `ts_decay_linear(day_open(Volume), 5)` | 0.96 | 0.33 | 0.32 | 0.24 | 0.39 | 0.01 | `cs_bucket_rank(ts_decay_linear(day_open(Volume), 5), LogFloatCap)` |
