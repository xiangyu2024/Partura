# 相关度表:种子 2028,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.41 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.16 | 0.75 | 0.15 | 0.07 | 0.67 | 0.64 | `cross_ema(day_gini(Amt), 60)` |
| slot a seed 1 | 过 | 0.21 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.19 | 0.43 | 0.12 | 0.13 | 0.35 | 0.02 | `cs_regres(cross_ema(day_gini(Amt), 60), LogFloatCap)` |
| slot a seed 2 | 过 | 0.52 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.44 | 0.59 | 0.20 | 0.10 | 0.52 | 0.48 | `cs_regres(cross_ema(day_gini(Amt), 60), log(day_last(Close)))` |
| slot a seed 3 | 过 | 0.41 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.23 | 0.34 | 0.26 | 0.00 | 0.35 | 0.09 | `sub(cross_ema(day_gini(Amt), 60), cross_ema(day_gini(Volume), 60))` |
| slot a seed 4 | 过 | 0.43 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.17 | 0.36 | 0.08 | 0.02 | 0.37 | 0.42 | `sub(cs_rank(cross_ema(day_gini(Amt), 60)), cs_rank(cross_ema(day_kurt(Volume), 60)))` |
| slot a seed 5 | 过 | 0.27 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.15 | 0.35 | 0.24 | 0.04 | 0.33 | 0.14 | `div(cross_ema(day_gini(Amt), 60), cross_ema(day_gini(Amt), 241))` |
| slot a seed 6 | 过 | 0.39 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.20 | 0.58 | 0.03 | 0.04 | 0.56 | 0.82 | `mul(cross_ema(day_gini(Amt), 60), cs_rank(LogTotalCap))` |
| slot a seed 7 | 过 | 0.20 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.18 | 0.42 | 0.12 | 0.12 | 0.35 | 0.01 | `cs_bucket_demean(cross_ema(day_gini(Amt), 60), LogFloatCap)` |
| slot a seed 8 | 过 | 0.49 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.40 | 0.57 | 0.21 | 0.10 | 0.50 | 0.43 | `cs_bucket_demean(cross_ema(day_gini(Amt), 60), day_close(Low))` |
| slot a seed 9 | 过 | 0.06 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.05 | 0.11 | 0.02 | 0.03 | 0.11 | 0.08 | `cross_corr(cross_delay(cross_ema(day_gini(Amt), 60), 1), cs_demean(ts_delta(log(day_last(Close)), 1)), 120)` |
| slot a seed 10 | 过 | 0.48 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.30 | 0.62 | 0.68 | 0.04 | 0.62 | 0.21 | `div(cross_ema(day_gini(Amt), 60), cross_ema(day_std(Ret), 60))` |
| slot a seed 11 | 过 | 0.45 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.21 | 0.73 | 0.06 | 0.01 | 0.68 | 0.81 | `cs_first_low40(LogTotalCap, cross_ema(day_gini(Amt), 60))` |
| slot a seed 12 | 过 | 0.18 | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Clo` | 0.09 | 0.30 | 0.09 | 0.08 | 0.24 | 0.02 | `cs_first_high40(LogTotalCap, cross_ema(day_gini(Amt), 60))` |
| slot a seed 13 | 过 | 0.09 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.08 | 0.02 | 0.05 | 0.00 | 0.01 | 0.02 | `cross_regbeta(cross_delay(cross_ema(day_gini(Amt), 60), 1), cs_demean(day_sum(Ret)), 120)` |
| slot a seed 14 | 过 | 0.24 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.11 | 0.32 | 0.32 | 0.05 | 0.31 | 0.08 | `ts_delta(cross_ema(day_gini(Amt), 60), 20)` |
| slot a seed 15 | 过 | 0.26 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.13 | 0.30 | 0.26 | 0.02 | 0.29 | 0.10 | `cross_zscore(cross_ema(day_gini(Amt), 60), 241)` |
| slot a seed 16 | 过 | 0.42 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.23 | 0.18 | 0.32 | 0.01 | 0.21 | 0.24 | `cs_regres(cross_ema(day_gini(Amt), 60), cross_ema(day_gini(Volume), 60))` |
| slot b seed 1 | 过 | 0.25 | `cross_quantile_q25(pow_3(day_mean(Volume)), 5)` | 0.61 | 0.31 | 0.04 | 0.06 | 0.26 | 0.00 | `cross_ema(day_durbin_watson(Ret), 60)` |
| slot b seed 2 | 过 | 0.23 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.61 | 0.35 | 0.04 | 0.06 | 0.29 | 0.06 | `cs_regres(cross_ema(day_durbin_watson(Ret), 60), LogFloatCap)` |
| slot b seed 3 | 过 | 0.55 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.63 | 0.11 | 0.02 | 0.03 | 0.12 | 0.40 | `cs_regres(cross_ema(day_durbin_watson(Ret), 60), cross_ema(day_gini(Amt), 60))` |
| slot b seed 4 | 过 | 0.28 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.12 | 0.43 | 0.32 | 0.07 | 0.43 | 0.14 | `sub(cross_ema(day_durbin_watson(Ret), 20), cross_ema(day_durbin_watson(Ret), 241))` |
| slot b seed 5 | 过 | 0.23 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.61 | 0.35 | 0.02 | 0.05 | 0.30 | 0.11 | `cs_bucket_demean(cross_ema(day_durbin_watson(Ret), 60), LogFloatCap)` |
| slot b seed 6 | 过 | 0.09 | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(neg(cs_mas` | 0.08 | 0.09 | 0.11 | 0.16 | 0.10 | 0.03 | `cross_zscore(day_durbin_watson(Ret), 120)` |
| slot b seed 7 | 过 | 0.57 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.36 | 0.35 | 0.76 | 0.02 | 0.37 | 0.12 | `div(cross_ema(day_durbin_watson(Ret), 60), cross_ema(day_std(Ret), 60))` |
| slot b seed 8 | 过 | 0.10 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.05 | 0.10 | 0.08 | 0.02 | 0.09 | 0.03 | `cross_corr(cross_delay(cross_zscore(day_durbin_watson(Ret), 60), 1), cs_demean(day_sum(Ret)), 120)` |
| slot b seed 9 | 过 | 0.27 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.43 | 0.54 | 0.03 | 0.02 | 0.50 | 0.17 | `cs_regres(cross_ema(day_durbin_watson(Ret), 60), log(cross_mean(day_mean(Volume), 20)))` |
| slot b seed 10 | 过 | 0.31 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.54 | 0.34 | 0.06 | 0.05 | 0.30 | 0.02 | `cross_tail_mean_q25(day_durbin_watson(Ret), 60)` |
| slot b seed 11 | 过 | 0.32 | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_d` | 0.22 | 0.03 | 0.09 | 0.01 | 0.04 | 0.21 | `cross_stddev(day_durbin_watson(Ret), 120)` |
| slot b seed 12 | 过 | 0.26 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.50 | 0.60 | 0.01 | 0.02 | 0.55 | 0.57 | `cs_first_low40(cross_ema(day_durbin_watson(Ret), 60), LogTotalCap)` |
| slot b seed 13 | 过 | 0.21 | `cross_quantile_q25(pow_3(day_mean(Volume)), 5)` | 0.61 | 0.37 | 0.03 | 0.05 | 0.31 | 0.11 | `cs_last_high10(cross_ema(day_durbin_watson(Ret), 60), day_close(Low))` |
| slot b seed 14 | 过 | 0.65 | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` | 0.56 | 0.42 | 0.10 | 0.01 | 0.40 | 0.62 | `sub(cs_rank(cross_ema(day_durbin_watson(Ret), 60)), cs_rank(cross_ema(day_gini(Amt), 60)))` |
| R 1 variant 1 | 过 | 0.99 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.99 | 0.27 | 0.09 | 0.06 | 0.23 | 0.32 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Volume), 3), 10))` |
| R 1 variant 2 | 过 | 0.99 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.99 | 0.27 | 0.09 | 0.06 | 0.23 | 0.32 | `div(cs_first_low40(LogTotalCap, day_close(High)), cross_ema(add(day_kurt(Volume), 3), 10))` |
| R 1 variant 3 | 过 | 0.96 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.96 | 0.27 | 0.07 | 0.06 | 0.24 | 0.31 | `div(cs_first_low40(LogTotalCap, day_close(High)), cross_ema(add(day_kurt(Volume), 3), 5))` |
| R 1 variant 4 | 过 | 0.96 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.96 | 0.27 | 0.07 | 0.06 | 0.24 | 0.31 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Volume), 3), 5))` |
| R 1 variant 5 | 过 | 0.99 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.99 | 0.26 | 0.10 | 0.06 | 0.23 | 0.32 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Amt), 3), 10))` |
| R 1 variant 6 | 过 | 0.99 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.99 | 0.26 | 0.10 | 0.06 | 0.23 | 0.32 | `div(cs_first_low40(LogTotalCap, day_close(High)), cross_ema(add(day_kurt(Amt), 3), 10))` |
| R 1 variant 7 | 过 | 0.97 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.98 | 0.14 | 0.09 | 0.04 | 0.12 | 0.23 | `div(cs_first_low40(LogTotalCap, day_close(Low)), sqrt(cross_ema(add(day_kurt(Volume), 3), 10)))` |
| R 1 variant 8 | 过 | 0.99 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(a` | 0.99 | 0.27 | 0.09 | 0.06 | 0.23 | 0.32 | `div(cs_first_low40(LogTotalCap, day_close(Vwap)), cross_ema(add(day_kurt(Volume), 3), 10))` |
