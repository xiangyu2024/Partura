# 相关度表:种子 2016,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.05 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.14 | 0.04 | 0.03 | 0.02 | 0.03 | 0.04 | `day_hurst(Low)` |
| slot a seed 1 | 过 | 0.22 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.16 | 0.22 | 0.12 | 0.04 | 0.17 | 0.20 | `cross_mean(day_hurst(Low), 60)` |
| slot a seed 2 | 过 | 0.03 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.06 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | `cross_zscore(day_hurst(Low), 120)` |
| slot a seed 3 | 过 | 0.11 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.13 | 0.07 | 0.01 | 0.01 | 0.05 | 0.06 | `cross_corr(day_hurst(Low), sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 4 | 过 | 0.07 | `sub(day_kurt(Ret), day_quantile_q25(Open))` | 0.08 | 0.01 | 0.12 | 0.30 | 0.03 | 0.07 | `cross_mean(mul(day_hurst(Low), sign(sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1))), 60)` |
| slot a seed 5 | 过 | 0.16 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.18 | 0.02 | 0.03 | 0.07 | 0.01 | 0.01 | `sub(cross_mean(day_hurst(Low), 20), cross_mean(day_hurst(Low), 241))` |
| slot a seed 6 | 过 | 0.36 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.38 | 0.16 | 0.03 | 0.01 | 0.15 | 0.10 | `cross_quantile(day_hurst(Low), 0.9, 60)` |
| slot a seed 7 | 过 | 0.17 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.05 | 0.16 | 0.11 | 0.03 | 0.13 | 0.16 | `cross_max(sub(day_hurst(Low), day_hurst(High)), 60)` |
| slot a seed 8 | 过 | 0.07 | `ts_max(day_hurst(Vwap), 50)` | 0.09 | 0.06 | 0.09 | 0.00 | 0.06 | 0.06 | `cross_mean(sub(day_hurst(Low), day_hurst(High)), 120)` |
| slot a seed 9 | 过 | 0.34 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.34 | 0.21 | 0.03 | 0.02 | 0.20 | 0.12 | `cross_tail_mean_q75(day_hurst(Low), 120)` |
| slot a seed 10 | 过 | 0.59 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.65 | 0.01 | 0.17 | 0.03 | 0.02 | 0.03 | `cs_regres(cross_max(day_hurst(Low), 60), cross_mean(day_std(Ret), 60))` |
| slot a seed 11 | 过 | 0.61 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.65 | 0.13 | 0.04 | 0.04 | 0.15 | 0.05 | `cs_bucket_zscore(cross_max(day_hurst(Low), 60), LogFloatCap)` |
| slot a seed 12 | 过 | 0.23 | `abs_(day_quantile_q25(Open))` | 0.24 | 0.13 | 0.17 | 0.06 | 0.07 | 0.12 | `div(cross_max(day_hurst(Low), 60), cross_mean(day_hurst(Close), 60))` |
| slot a seed 13 | 过 | 0.11 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.12 | 0.08 | 0.04 | 0.01 | 0.07 | 0.06 | `ts_regbeta(day_hurst(Low), sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 14 | 过 | 0.29 | `pow_05(day_close(Vwap))` | 0.14 | 0.29 | 0.15 | 0.05 | 0.23 | 0.27 | `cross_ema(day_hurst(Low), 60)` |
| slot a seed 15 | 过 | 0.50 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.57 | 0.12 | 0.02 | 0.06 | 0.14 | 0.20 | `cs_last_low10(cross_max(day_hurst(Low), 60), ListAge)` |
| slot a seed 16 | 过 | 0.74 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.40 | 0.73 | 0.03 | 0.05 | 0.68 | 0.64 | `cross_mean(mul(day_hurst(Low), day_pos_ratio(Volume)), 60)` |
| slot b seed 1 | 过 | 0.06 | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 3` | 0.07 | 0.03 | 0.06 | 0.03 | 0.03 | 0.01 | `sub(cross_mean(day_hurst(Close), 60), cross_hurst(day_last(Close), 60))` |
| slot b seed 2 | 过 | 0.11 | `pow_05(day_close(Close))` | 0.06 | 0.09 | 0.05 | 0.05 | 0.07 | 0.08 | `cross_hurst(day_last(Close), 120)` |
| slot b seed 3 | 过 | 0.05 | `ts_max(day_hurst(Vwap), 50)` | 0.04 | 0.06 | 0.09 | 0.00 | 0.06 | 0.01 | `cross_hurst(sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 120)` |
| slot b seed 4 | 过 | 0.06 | `pow_05(day_close(Close))` | 0.06 | 0.06 | 0.04 | 0.00 | 0.05 | 0.03 | `cross_hurst(day_mean(Ret), 120)` |
| slot b seed 5 | 过 | 0.28 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.09 | 0.27 | 0.01 | 0.04 | 0.24 | 0.14 | `cross_hurst(day_std(Ret), 120)` |
| slot b seed 6 | 过 | 0.33 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.11 | 0.34 | 0.02 | 0.02 | 0.33 | 0.33 | `cross_hurst(day_gini(Amt), 120)` |
| slot b seed 7 | 过 | 0.08 | `ts_max(day_hurst(Vwap), 50)` | 0.10 | 0.04 | 0.14 | 0.00 | 0.06 | 0.08 | `cross_hurst(day_centroid(Amt), 120)` |
| slot b seed 8 | 过 | 0.08 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.13 | 0.05 | 0.01 | 0.02 | 0.06 | 0.01 | `cross_hurst(day_signed_ratio(Ret, Amt), 120)` |
| slot b seed 9 | 过 | 0.05 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.09 | 0.03 | 0.00 | 0.02 | 0.03 | 0.01 | `cross_hurst(day_topw_mean(Ret, Amt), 120)` |
| slot b seed 10 | 过 | 0.45 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.15 | 0.47 | 0.03 | 0.03 | 0.45 | 0.53 | `cross_hurst(day_pos_ratio(Volume), 120)` |
| slot b seed 11 | 过 | 0.04 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.04 | 0.04 | 0.01 | 0.00 | 0.03 | 0.00 | `cross_hurst(day_hurst(Low), 120)` |
| slot b seed 12 | 过 | 0.22 | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt` | 0.10 | 0.18 | 0.05 | 0.04 | 0.17 | 0.11 | `sub(cross_hurst(sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 120), cross_hurst(day_std(Ret), 120))` |
| slot b seed 13 | 过 | 0.04 | `ts_max(day_hurst(Vwap), 50)` | 0.04 | 0.05 | 0.09 | 0.00 | 0.05 | 0.00 | `cs_bucket_zscore(cross_hurst(sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 120), LogFloatCap)` |
| slot b seed 14 | 过 | 0.09 | `ts_max(day_hurst(Vwap), 50)` | 0.09 | 0.11 | 0.13 | 0.02 | 0.13 | 0.16 | `cross_hurst(day_flat_ratio(Close), 120)` |
| slot b seed 15 | 过 | 0.03 | `pow_05(day_close(Close))` | 0.02 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | `cross_hurst(day_skew(Ret), 120)` |
| slot b seed 16 | 过 | 0.10 | `abs_(day_quantile_q25(Open))` | 0.04 | 0.08 | 0.01 | 0.06 | 0.07 | 0.08 | `cross_hurst(day_last(Close), 241)` |
| R 1 variant 1 | 过 | 0.62 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.66 | 0.10 | 0.06 | 0.04 | 0.11 | 0.00 | `pow_2(ts_max(day_hurst(Low), 60))` |
| R 1 variant 2 | 过 | 0.47 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.47 | 0.08 | 0.05 | 0.02 | 0.10 | 0.01 | `pow_2(ts_max(day_hurst(Low), 90))` |
| R 1 variant 3 | 过 | 0.36 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.35 | 0.07 | 0.06 | 0.01 | 0.10 | 0.03 | `pow_2(ts_max(day_hurst(Low), 120))` |
| R 1 variant 4 | 过 | 0.21 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.18 | 0.03 | 0.05 | 0.01 | 0.06 | 0.05 | `pow_2(ts_max(day_hurst(Low), 241))` |
| R 1 variant 5 | 过 | 0.35 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.33 | 0.07 | 0.05 | 0.01 | 0.09 | 0.05 | `pow_2(ts_max(day_hurst(Close), 120))` |
| R 1 variant 6 | 过 | 0.45 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.45 | 0.09 | 0.06 | 0.03 | 0.11 | 0.00 | `pow_2(ts_max(day_hurst(High), 90))` |
| R 1 variant 7 | 过 | 0.47 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.47 | 0.08 | 0.05 | 0.02 | 0.10 | 0.01 | `ts_max(day_hurst(Low), 90)` |
| R 1 variant 8 | 过 | 0.31 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.31 | 0.17 | 0.04 | 0.01 | 0.16 | 0.11 | `pow_2(cross_quantile(day_hurst(Low), 0.9, 90))` |
| R 2 variant 1 | 过 | 0.40 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.39 | 0.08 | 0.06 | 0.02 | 0.10 | 0.05 | `ts_max(day_hurst(Close), 100)` |
| R 2 variant 2 | 过 | 0.35 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.33 | 0.07 | 0.05 | 0.01 | 0.09 | 0.05 | `ts_max(day_hurst(Close), 120)` |
| R 2 variant 3 | 过 | 0.20 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.17 | 0.02 | 0.05 | 0.01 | 0.05 | 0.07 | `ts_max(day_hurst(Close), 241)` |
| R 2 variant 4 | 过 | 0.42 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.42 | 0.07 | 0.04 | 0.02 | 0.09 | 0.04 | `ts_max(day_hurst(Open), 100)` |
| R 2 variant 5 | 过 | 0.28 | `pow_2(ts_max(day_hurst(Low), 30))` | 0.29 | 0.14 | 0.08 | 0.01 | 0.12 | 0.04 | `cross_quantile(day_hurst(Close), 0.9, 100)` |
| R 2 variant 6 | 过 | 0.28 | `pow_05(day_close(Vwap))` | 0.13 | 0.23 | 0.15 | 0.05 | 0.17 | 0.16 | `cross_mean(day_hurst(Close), 100)` |
