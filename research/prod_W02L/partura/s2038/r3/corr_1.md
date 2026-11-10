# 相关度表:种子 2038,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.03 | `ts_decay_linear(day_open(Volume), 5)` | 0.09 | 0.03 | 0.04 | 0.17 | 0.03 | 0.02 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| slot a seed 1 | 过 | 0.53 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.27 | 0.07 | 0.44 | 0.08 | 0.03 | 0.55 | `cs_first_low20(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), LogFloatShares)` |
| slot a seed 2 | 过 | 0.50 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.25 | 0.05 | 0.37 | 0.03 | 0.02 | 0.51 | `cs_first_low20(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), ListAge)` |
| slot a seed 3 | 过 | 0.38 | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_a` | 0.30 | 0.14 | 0.36 | 0.15 | 0.18 | 0.00 | `cs_last_low10(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), ListAge)` |
| slot a seed 4 | 过 | 0.72 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.59 | 0.03 | 0.53 | 0.05 | 0.03 | 0.42 | `cross_tail_mean_q75(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` |
| slot a seed 5 | 过 | 0.73 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.62 | 0.09 | 0.54 | 0.02 | 0.02 | 0.48 | `sub(cross_tail_mean_q75(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), cross_tail_mean_q25(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120))` |
| slot a seed 6 | 过 | 0.19 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.17 | 0.14 | 0.17 | 0.15 | 0.13 | 0.04 | `div(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), add(cross_stddev(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), 0.000001))` |
| slot a seed 7 | 过 | 0.20 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt` | 0.19 | 0.09 | 0.23 | 0.45 | 0.12 | 0.01 | `cross_ema(cross_zscore(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), 20)` |
| slot a seed 8 | 过 | 0.07 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.06 | 0.03 | 0.03 | 0.01 | 0.04 | 0.01 | `sub(cross_semistd_pos(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), cross_semistd_neg(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120))` |
| slot a seed 9 | 过 | 0.52 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.33 | 0.17 | 0.50 | 0.15 | 0.23 | 0.17 | `cs_bucket_zscore(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), LogFloatShares)` |
| slot a seed 10 | 过 | 0.50 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.33 | 0.19 | 0.32 | 0.03 | 0.17 | 0.64 | `cs_first_low40(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatShares)` |
| slot a seed 11 | 过 | 0.51 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.34 | 0.20 | 0.48 | 0.16 | 0.25 | 0.12 | `cs_regres(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), LogFloatShares)` |
| slot a seed 12 | 过 | 0.40 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.30 | 0.04 | 0.39 | 0.13 | 0.02 | 0.47 | `cross_ema(cs_first_low20(sub(day_wmean(Ret, Amt), day_mean(Ret)), LogFloatShares), 40)` |
| slot a seed 13 | 过 | 0.48 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.26 | 0.07 | 0.44 | 0.09 | 0.09 | 0.40 | `cs_first_low20(cs_bucket_rank(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), LogFloatCap), LogFloatShares)` |
| slot a seed 14 | 过 | 0.41 | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_a` | 0.17 | 0.18 | 0.51 | 0.35 | 0.24 | 0.13 | `ts_decay_linear(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60)` |
| slot b seed 1 | 过 | 0.34 | `ts_decay_linear(day_open(Volume), 5)` | 0.10 | 0.38 | 0.01 | 0.01 | 0.35 | 0.60 | `cs_first_low20(cross_mean(div(day_last(Amt), add(day_sum(Amt), 1)), 60), LogFloatShares)` |
| slot b seed 2 | 过 | 0.36 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.23 | 0.49 | 0.25 | 0.03 | 0.48 | 0.01 | `cs_first_low20(cross_ema(day_last(Amt), 20), LogFloatShares)` |
| slot b seed 3 | 过 | 0.18 | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_a` | 0.32 | 0.05 | 0.28 | 0.24 | 0.03 | 0.35 | `cs_first_low20(cross_zscore(day_last(Amt), 120), LogFloatShares)` |
| slot b seed 4 | 过 | 0.17 | `ts_decay_linear(day_open(Volume), 5)` | 0.18 | 0.10 | 0.31 | 0.15 | 0.08 | 0.31 | `cs_first_low20(cross_ema(day_signed_ratio(Ret, Amt), 60), LogFloatShares)` |
| slot b seed 5 | 过 | 0.30 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.34 | 0.68 | 0.32 | 0.14 | 0.67 | 0.39 | `cs_first_low20(day_last(Amt), sub(LogFloatShares, LogFloatCap))` |
| slot b seed 6 | 过 | 0.67 | `ts_decay_linear(day_open(Volume), 5)` | 0.55 | 0.46 | 0.32 | 0.13 | 0.50 | 0.41 | `cs_first_high20(day_last(Amt), sub(LogFloatShares, LogFloatCap))` |
| slot b seed 7 | 过 | 0.24 | `ts_decay_linear(day_open(Volume), 5)` | 0.11 | 0.34 | 0.05 | 0.02 | 0.31 | 0.55 | `cs_first_high20(cross_mean(div(day_last(Amt), add(day_sum(Amt), 1)), 60), sub(LogTotalCap, LogFloatCap))` |
| slot b seed 8 | 过 | 0.38 | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(V` | 0.24 | 0.16 | 0.32 | 0.03 | 0.11 | 0.49 | `cs_first_low20(cross_ema(div(day_open(Amt), add(day_last(Amt), 1)), 30), LogFloatShares)` |
| slot b seed 9 | 过 | 0.24 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.20 | 0.33 | 0.24 | 0.08 | 0.33 | 0.12 | `cs_first_low20(cs_first_low20(day_last(Amt), LogFloatShares), ListAge)` |
| slot b seed 10 | 过 | 0.46 | `ts_decay_linear(day_open(Volume), 5)` | 0.29 | 0.38 | 0.01 | 0.04 | 0.37 | 0.66 | `cs_first_low40(cross_mean(div(day_last(Amt), add(day_sum(Amt), 1)), 20), LogFloatShares)` |
| slot b seed 11 | 过 | 0.37 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.26 | 0.46 | 0.17 | 0.07 | 0.44 | 0.02 | `cs_first_low20(cross_ema(cs_rank(day_last(Amt)), 40), LogFloatShares)` |
| slot b seed 12 | 过 | 0.27 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.25 | 0.45 | 0.31 | 0.05 | 0.46 | 0.03 | `cs_first_low20(cross_max(day_last(Amt), 20), LogFloatShares)` |
| R 1 variant 1 | 过 | 0.83 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt` | 0.92 | 0.17 | 0.21 | 0.17 | 0.22 | 0.01 | `div(cross_mean(day_open(Amt), 5), add(day_sum(Amt), 1))` |
| R 1 variant 2 | 过 | 0.65 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt` | 0.91 | 0.14 | 0.09 | 0.27 | 0.17 | 0.10 | `div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1))` |
| R 1 variant 3 | 过 | 0.60 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt` | 0.60 | 0.09 | 0.20 | 0.21 | 0.06 | 0.37 | `cs_first_low20(div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt), 20), 1)), LogFloatShares)` |
| R 1 variant 4 | 过 | 0.98 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt` | 0.96 | 0.06 | 0.16 | 0.33 | 0.10 | 0.05 | `cs_bucket_rank(div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt), 20), 1)), LogFloatShares)` |
| R 1 variant 5 | 过 | 0.48 | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt` | 0.54 | 0.05 | 0.25 | 0.09 | 0.02 | 0.39 | `cs_first_low20(div(cross_mean(day_open(Amt), 5), add(day_sum(Amt), 1)), LogFloatShares)` |
| R 2 variant 1 | 过 | 0.52 | `ts_decay_linear(day_open(Volume), 5)` | 0.36 | 0.86 | 0.18 | 0.02 | 0.85 | 0.57 | `ts_max(ts_max(log(day_last(Amt)), 20), 50)` |
| R 2 variant 2 | 过 | 0.33 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.22 | 0.43 | 0.22 | 0.04 | 0.42 | 0.04 | `cs_first_low20(ts_max(ts_max(log(day_last(Amt)), 20), 50), LogFloatShares)` |
| R 2 variant 3 | 过 | 0.29 | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_a` | 0.17 | 0.37 | 0.13 | 0.04 | 0.34 | 0.17 | `ts_max(ts_max(div(day_last(Amt), add(day_sum(Amt), 1)), 20), 50)` |
| R 3 variant 1 | 过 | 0.65 | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume),` | 0.61 | 0.01 | 0.06 | 0.04 | 0.01 | 0.09 | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 100)` |
| R 3 variant 2 | 过 | 0.65 | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume),` | 0.61 | 0.01 | 0.06 | 0.04 | 0.01 | 0.09 | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Amt), 15), day_durbin_watson(Ret), 30), 100)` |
