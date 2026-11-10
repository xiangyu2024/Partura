# 相关度表:种子 2008,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.37 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.10 | 0.13 | 0.69 | 0.30 | 0.17 | 0.12 | `day_durbin_watson(Vwap)` |
| slot a seed 1 | 过 | 0.12 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.14 | 0.21 | 0.08 | 0.02 | 0.19 | 0.12 | `ts_skew(log(day_durbin_watson(Vwap)), 120)` |
| slot a seed 2 | 过 | 0.18 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.14 | 0.04 | 0.07 | 0.08 | 0.05 | 0.05 | `sub(cross_semistd_pos(day_durbin_watson(Vwap), 120), cross_semistd_neg(day_durbin_watson(Vwap), 120))` |
| slot a seed 3 | 过 | 0.33 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.24 | 0.36 | 0.01 | 0.02 | 0.34 | 0.09 | `cross_autocorr(log(day_durbin_watson(Vwap)), 120, 1)` |
| slot a seed 4 | 过 | 0.09 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.13 | 0.22 | 0.03 | 0.03 | 0.20 | 0.17 | `cross_autocorr(cross_ema(log(day_durbin_watson(Vwap)), 3), 241, 10)` |
| slot a seed 5 | 过 | 0.12 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.48 | 0.11 | 0.52 | 0.41 | 0.16 | 0.07 | `sub(cross_ema(log(day_durbin_watson(Vwap)), 5), cross_ema(log(day_durbin_watson(Vwap)), 120))` |
| slot a seed 6 | 过 | 0.58 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.50 | 0.03 | 0.07 | 0.02 | 0.00 | 0.36 | `div(cross_stddev(day_durbin_watson(Vwap), 120), cross_mean(day_durbin_watson(Vwap), 120))` |
| slot a seed 7 | 过 | 0.09 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.09 | 0.26 | 0.04 | 0.00 | 0.24 | 0.18 | `cross_hurst(log(day_durbin_watson(Vwap)), 120)` |
| slot a seed 8 | 过 | 0.14 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.09 | 0.07 | 0.12 | 0.05 | 0.08 | 0.06 | `cross_corr(day_durbin_watson(Vwap), day_sum(Ret), 120)` |
| slot a seed 9 | 过 | 0.27 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.18 | 0.42 | 0.08 | 0.03 | 0.41 | 0.16 | `cross_corr(day_durbin_watson(Vwap), log(day_sum(Amt)), 120)` |
| slot a seed 10 | 过 | 0.33 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.23 | 0.43 | 0.09 | 0.02 | 0.42 | 0.12 | `cross_reg_fvalue(log(day_sum(Amt)), log(day_durbin_watson(Vwap)), 120)` |
| slot a seed 11 | 过 | 0.24 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.17 | 0.12 | 0.06 | 0.01 | 0.12 | 0.07 | `cross_corr(day_durbin_watson(Vwap), abs_(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)), 120)` |
| slot a seed 12 | 过 | 0.63 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.55 | 0.35 | 0.72 | 0.01 | 0.38 | 0.03 | `cs_bucket_demean(cross_mean(log(day_durbin_watson(Vwap)), 120), LogFloatCap)` |
| slot a seed 13 | 过 | 0.54 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.47 | 0.33 | 0.11 | 0.01 | 0.33 | 0.00 | `cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 120), LogFloatCap)` |
| slot a seed 14 | 过 | 0.32 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.21 | 0.01 | 0.03 | 0.05 | 0.01 | 0.43 | `cs_first_low20(cross_autocorr(log(day_durbin_watson(Vwap)), 120, 1), LogFloatCap)` |
| slot a seed 15 | 过 | 0.27 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.20 | 0.21 | 0.09 | 0.03 | 0.18 | 0.02 | `cs_last_low10(ts_skew(log(day_durbin_watson(Vwap)), 120), ListAge)` |
| slot a seed 16 | 过 | 0.08 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.07 | 0.30 | 0.01 | 0.02 | 0.26 | 0.14 | `ts_kurt(log(day_durbin_watson(Vwap)), 241)` |
| slot b seed 1 | 过 | 0.29 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.17 | 0.08 | 0.07 | 0.01 | 0.07 | 0.34 | `cross_mean(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 60)` |
| slot b seed 2 | 过 | 0.32 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.23 | 0.11 | 0.03 | 0.02 | 0.11 | 0.40 | `cross_mean(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 241)` |
| slot b seed 3 | 过 | 0.30 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.19 | 0.09 | 0.06 | 0.01 | 0.09 | 0.37 | `cross_ema(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 40)` |
| slot b seed 4 | 过 | 0.31 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.21 | 0.05 | 0.05 | 0.02 | 0.05 | 0.34 | `cross_mean(sub(log(day_durbin_watson(Open)), log(day_durbin_watson(Vwap))), 120)` |
| slot b seed 5 | 过 | 0.27 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.18 | 0.07 | 0.02 | 0.01 | 0.07 | 0.32 | `cross_mean(div(day_durbin_watson(Close), day_durbin_watson(Vwap)), 120)` |
| slot b seed 6 | 过 | 0.14 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.24 | 0.65 | 0.08 | 0.03 | 0.58 | 0.30 | `cross_mean(div(day_var(in_delta(Vwap, 5)), day_var(in_delta(Vwap, 1))), 120)` |
| slot b seed 7 | 过 | 0.14 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.09 | 0.28 | 0.04 | 0.06 | 0.23 | 0.02 | `sub(LogFloatShares, LogFloatCap)` |
| slot b seed 8 | 过 | 0.68 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.54 | 0.15 | 0.74 | 0.01 | 0.20 | 0.24 | `cs_regres(cross_mean(log(day_durbin_watson(Vwap)), 120), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 9 | 过 | 0.66 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.47 | 0.15 | 0.65 | 0.01 | 0.19 | 0.27 | `cs_bucket_demean(cross_mean(log(day_durbin_watson(Vwap)), 120), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 10 | 过 | 0.12 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.05 | 0.26 | 0.10 | 0.06 | 0.21 | 0.00 | `cs_regres(sub(LogFloatShares, LogFloatCap), cross_mean(log(day_durbin_watson(Vwap)), 120))` |
| slot b seed 11 | 过 | 0.31 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.18 | 0.15 | 0.25 | 0.04 | 0.10 | 0.28 | `cs_last_low10(cross_mean(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 120), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 12 | 过 | 0.19 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.21 | 0.15 | 0.00 | 0.02 | 0.14 | 0.06 | `cs_bucket_zscore(cross_mean(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 120), LogFloatCap)` |
| slot b seed 13 | 过 | 0.22 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.20 | 0.30 | 0.02 | 0.01 | 0.27 | 0.01 | `cross_corr(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)), 241)` |
| slot b seed 14 | 过 | 0.21 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.21 | 0.34 | 0.05 | 0.01 | 0.32 | 0.10 | `cross_regbeta(log(day_durbin_watson(Vwap)), sub(LogFloatCap, LogFloatShares), 241)` |
| slot b seed 15 | 过 | 0.02 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.18 | 0.19 | 0.00 | 0.04 | 0.19 | 0.34 | `cs_first_low20(cross_mean(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 120), LogFloatCap)` |
| slot b seed 16 | 过 | 0.12 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.22 | 0.65 | 0.10 | 0.03 | 0.58 | 0.31 | `cross_mean(sub(log(day_var(in_delta(Vwap, 5))), log(day_var(in_delta(Vwap, 1)))), 120)` |
| R 1 variant 1 | 过 | 0.78 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.75 | 0.15 | 0.21 | 0.02 | 0.18 | 0.28 | `ts_std(log(day_durbin_watson(Vwap)), 40)` |
| R 1 variant 2 | 过 | 0.57 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.47 | 0.13 | 0.14 | 0.04 | 0.14 | 0.32 | `ts_std(log(day_durbin_watson(Vwap)), 120)` |
| R 1 variant 3 | 过 | 0.48 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.36 | 0.09 | 0.10 | 0.05 | 0.09 | 0.34 | `ts_std(log(day_durbin_watson(Vwap)), 241)` |
| R 1 variant 4 | 过 | 0.48 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.36 | 0.26 | 0.09 | 0.05 | 0.26 | 0.15 | `ts_std(cross_ema(log(day_durbin_watson(Vwap)), 5), 120)` |
| R 1 variant 5 | 过 | 0.67 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.68 | 0.14 | 0.14 | 0.02 | 0.17 | 0.16 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 20)` |
| R 1 variant 6 | 过 | 0.70 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.64 | 0.17 | 0.11 | 0.03 | 0.19 | 0.21 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 80)` |
| R 2 variant 1 | 过 | 0.62 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.64 | 0.14 | 0.04 | 0.05 | 0.14 | 0.18 | `cross_stddev(ts_sum(log(day_durbin_watson(Vwap)), 10), 241)` |
| R 2 variant 2 | 过 | 0.88 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.84 | 0.13 | 0.62 | 0.05 | 0.16 | 0.30 | `cross_mean(ts_sum(log(day_durbin_watson(Vwap)), 10), 241)` |
| R 2 variant 3 | 过 | 0.48 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.36 | 0.09 | 0.10 | 0.05 | 0.09 | 0.34 | `cross_stddev(log(day_durbin_watson(Vwap)), 241)` |
| R 3 variant 1 | 过 | 0.42 | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30` | 0.49 | 0.21 | 0.04 | 0.00 | 0.20 | 0.06 | `cross_hurst(log(day_durbin_watson(Vwap)), 30)` |
| R 3 variant 2 | 过 | 0.38 | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40` | 0.37 | 0.25 | 0.00 | 0.01 | 0.23 | 0.12 | `cross_hurst(log(day_durbin_watson(Vwap)), 60)` |
| R 3 variant 3 | 过 | 0.09 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.09 | 0.26 | 0.04 | 0.00 | 0.24 | 0.18 | `cross_hurst(log(day_durbin_watson(Vwap)), 120)` |
| R 3 variant 4 | 废品 | 0.08 | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson` | 0.20 | 0.17 | 0.11 | 0.08 | 0.17 | 0.09 | `div(cross_hurst(log(day_durbin_watson(Vwap)), 60), day_hurst(Vwap))` |
