# 相关度表:种子 2003,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.03 | `pow_2(pow_2(sigmoid(sigmoid(day_max(Ret)))))` | 0.05 | 0.07 | 0.06 | 0.05 | 0.05 | 0.03 | `day_q_stat_std(Vwap)` |
| slot a seed 1 | 过 | 0.14 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.14 | 0.34 | 0.06 | 0.03 | 0.31 | 0.10 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_autocorr_n1(Volume), 30), 120)` |
| slot a seed 2 | 过 | 0.14 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.15 | 0.35 | 0.05 | 0.03 | 0.32 | 0.09 | `cross_ema(cross_corr(day_q_stat_std(Vwap), day_autocorr_n1(Volume), 60), 40)` |
| slot a seed 3 | 过 | 0.22 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.09 | 0.40 | 0.06 | 0.03 | 0.37 | 0.10 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 15), 120)` |
| slot a seed 4 | 过 | 0.23 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.10 | 0.43 | 0.06 | 0.03 | 0.40 | 0.11 | `cross_ema(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 20), 60)` |
| slot a seed 5 | 过 | 0.22 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.11 | 0.38 | 0.08 | 0.03 | 0.35 | 0.09 | `cross_decay_linear(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 30), 90)` |
| slot a seed 6 | 过 | 0.20 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.09 | 0.37 | 0.06 | 0.04 | 0.34 | 0.09 | `cross_med(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 20), 120)` |
| slot a seed 7 | 过 | 0.12 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.13 | 0.32 | 0.03 | 0.02 | 0.29 | 0.13 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_ar1_coefficient(Volume), 30), 120)` |
| slot a seed 8 | 过 | 0.21 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.11 | 0.29 | 0.07 | 0.02 | 0.28 | 0.10 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_durbin_watson(Volume), 30), 120)` |
| slot a seed 9 | 过 | 0.06 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.15 | 0.25 | 0.11 | 0.02 | 0.25 | 0.26 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_sum(Ret), 30), 241)` |
| slot a seed 10 | 过 | 0.06 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.04 | 0.11 | 0.00 | 0.01 | 0.10 | 0.19 | `cross_ema(cross_corr(ts_delay(day_q_stat_std(Vwap), 1), day_q_stat_std(Volume), 30), 60)` |
| slot a seed 11 | 过 | 0.17 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.07 | 0.17 | 0.15 | 0.02 | 0.17 | 0.05 | `sub(cross_ema(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 15), 30), cross_ema(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 15), 241))` |
| slot a seed 12 | 过 | 0.19 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.12 | 0.39 | 0.06 | 0.03 | 0.36 | 0.11 | `cross_mean(add(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 20), cross_corr(day_q_stat_std(Vwap), day_autocorr_n1(Volume), 20)), 120)` |
| slot a seed 13 | 过 | 0.14 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.07 | 0.16 | 0.03 | 0.00 | 0.15 | 0.26 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_gini(Volume), 30), 120)` |
| slot a seed 14 | 过 | 0.14 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.03 | 0.24 | 0.00 | 0.02 | 0.22 | 0.07 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_centroid(Volume), 30), 120)` |
| slot a seed 15 | 过 | 0.14 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.13 | 0.04 | 0.06 | 0.01 | 0.02 | 0.02 | `cross_mean(cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Ret), 30), 120)` |
| slot a seed 16 | 过 | 0.12 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.13 | 0.10 | 0.06 | 0.01 | 0.09 | 0.27 | `cross_mean(cross_corr(day_q_stat_std(Vwap), abs_(day_sum(Ret)), 60), 120)` |
| slot b seed 1 | 过 | 0.31 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.18 | 0.01 | 0.08 | 0.03 | 0.01 | 0.42 | `sub(LogTotalCap, LogFloatCap)` |
| slot b seed 2 | 过 | 0.23 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.21 | 0.34 | 0.01 | 0.01 | 0.30 | 0.05 | `cs_regres(sub(LogTotalCap, LogFloatCap), LogFloatCap)` |
| slot b seed 3 | 废品 | 0.17 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.14 | 0.02 | 0.04 | 0.01 | 0.03 | 0.09 | `cross_delta(sub(LogTotalCap, LogFloatCap), 241)` |
| slot b seed 4 | 废品 | 0.06 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.06 | 0.01 | 0.02 | 0.01 | 0.01 | 0.01 | `cross_delta(sub(LogTotalCap, LogFloatCap), 60)` |
| slot b seed 5 | 废品 | 0.25 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.21 | 0.03 | 0.02 | 0.02 | 0.01 | 0.06 | `cross_delta(LogFloatShares, 241)` |
| slot b seed 6 | 废品 | 0.17 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.15 | 0.04 | 0.04 | 0.02 | 0.03 | 0.03 | `cross_delta(LogFloatShares, 120)` |
| slot b seed 7 | 废品 | 0.14 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.13 | 0.07 | 0.02 | 0.01 | 0.06 | 0.03 | `cross_delta(add(sub(LogTotalCap, LogFloatCap), LogFloatShares), 241)` |
| slot b seed 8 | 废品 | 0.08 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.08 | 0.07 | 0.01 | 0.01 | 0.06 | 0.03 | `cross_delta(add(sub(LogTotalCap, LogFloatCap), LogFloatShares), 120)` |
| slot b seed 9 | 废品 | 0.08 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.10 | 0.09 | 0.04 | 0.00 | 0.07 | 0.06 | `cross_mean(abs_(sign(cross_delta(LogFloatShares, 1))), 241)` |
| slot b seed 10 | 过 | 0.20 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.16 | 0.01 | 0.03 | 0.01 | 0.01 | 0.03 | `cross_sum(abs_(cross_delta(LogFloatShares, 1)), 241)` |
| slot b seed 11 | 废品 | 0.09 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.12 | 0.12 | 0.03 | 0.01 | 0.10 | 0.10 | `cs_regres(cross_delta(add(sub(LogTotalCap, LogFloatCap), LogFloatShares), 241), LogFloatCap)` |
| slot b seed 12 | 过 | 0.21 | `sigmoid(sigmoid(day_max(Ret)))` | 0.11 | 0.18 | 0.20 | 0.06 | 0.17 | 0.51 | `cross_mean(sub(log(day_last(Volume)), LogFloatShares), 241)` |
| slot b seed 13 | 过 | 0.24 | `sigmoid(sigmoid(day_max(Ret)))` | 0.15 | 0.24 | 0.25 | 0.05 | 0.24 | 0.50 | `cross_ema(sub(log(day_last(Volume)), LogFloatShares), 60)` |
| R 1 variant 1 | 过 | 0.64 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.75 | 0.07 | 0.13 | 0.03 | 0.08 | 0.21 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 80)` |
| R 1 variant 2 | 过 | 0.55 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.62 | 0.05 | 0.12 | 0.03 | 0.06 | 0.25 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 120)` |
| R 1 variant 3 | 过 | 0.45 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.47 | 0.00 | 0.12 | 0.03 | 0.01 | 0.32 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 241)` |
| R 1 variant 4 | 过 | 0.70 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.73 | 0.06 | 0.12 | 0.03 | 0.07 | 0.26 | `cross_ema(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 60)` |
| R 1 variant 5 | 过 | 0.42 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.48 | 0.04 | 0.11 | 0.04 | 0.04 | 0.28 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 30), 120)` |
| R 1 variant 6 | 过 | 0.51 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.57 | 0.05 | 0.12 | 0.02 | 0.06 | 0.21 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 15), 120)` |
| R 1 variant 7 | 过 | 0.21 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.22 | 0.01 | 0.08 | 0.01 | 0.01 | 0.11 | `ts_mean(ts_hurst(div(day_last(Volume), day_sum(Volume)), 20), 120)` |
| R 1 variant 8 | 过 | 0.54 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.60 | 0.08 | 0.14 | 0.04 | 0.09 | 0.26 | `ts_mean(ts_hurst(day_last(Volume), 20), 120)` |
| R 1 variant 9 | 过 | 0.55 | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 2` | 0.62 | 0.05 | 0.12 | 0.03 | 0.06 | 0.25 | `ts_mean(cross_hurst(div(day_last(Volume), day_max(Low)), 20), 120)` |
| R 2 variant 1 | 过 | 0.49 | `sigmoid(sigmoid(day_max(Ret)))` | 0.80 | 0.19 | 0.73 | 0.03 | 0.24 | 0.34 | `cross_mean(day_max(Ret), 60)` |
| R 2 variant 2 | 过 | 0.45 | `sigmoid(sigmoid(day_max(Ret)))` | 0.70 | 0.13 | 0.64 | 0.01 | 0.17 | 0.38 | `cross_mean(day_max(Ret), 120)` |
| R 2 variant 3 | 过 | 0.42 | `sigmoid(sigmoid(day_max(Ret)))` | 0.60 | 0.07 | 0.57 | 0.03 | 0.10 | 0.43 | `cross_mean(day_max(Ret), 241)` |
| R 2 variant 4 | 过 | 0.45 | `sigmoid(sigmoid(day_max(Ret)))` | 0.72 | 0.17 | 0.63 | 0.01 | 0.20 | 0.29 | `cross_med(day_max(Ret), 120)` |
| R 2 variant 5 | 过 | 0.41 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.59 | 0.14 | 0.05 | 0.01 | 0.13 | 0.50 | `cross_mean(div(day_max(Ret), day_std(Ret)), 120)` |
| R 2 variant 6 | 过 | 0.43 | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_s` | 0.61 | 0.16 | 0.06 | 0.01 | 0.14 | 0.52 | `cross_ema(div(day_max(Ret), day_std(Ret)), 60)` |
