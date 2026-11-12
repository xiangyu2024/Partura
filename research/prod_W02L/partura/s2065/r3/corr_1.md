# 相关度表:种子 2065,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 废品 | 0.10 | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap,` | 0.19 | 0.04 | 0.04 | 0.02 | 0.03 | 0.00 | `cross_delta(LogFloatShares, 60)` |
| slot a seed 2 | 废品 | 0.15 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.23 | 0.02 | 0.05 | 0.03 | 0.00 | 0.05 | `cross_delta(LogFloatShares, 120)` |
| slot a seed 3 | 过 | 0.21 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.27 | 0.00 | 0.05 | 0.03 | 0.02 | 0.08 | `cross_delta(LogFloatShares, 250)` |
| slot a seed 4 | 过 | 0.29 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.20 | 0.08 | 0.07 | 0.05 | 0.09 | 0.42 | `sub(LogTotalCap, LogFloatCap)` |
| slot a seed 5 | 过 | 0.29 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.20 | 0.08 | 0.07 | 0.05 | 0.09 | 0.42 | `cross_mean(sub(LogTotalCap, LogFloatCap), 20)` |
| slot a seed 6 | 废品 | 0.13 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.14 | 0.03 | 0.05 | 0.01 | 0.03 | 0.09 | `cross_delta(sub(LogTotalCap, LogFloatCap), 120)` |
| slot a seed 7 | 废品 | 0.16 | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap,` | 0.24 | 0.03 | 0.06 | 0.03 | 0.01 | 0.04 | `cross_max(cross_delta(LogFloatShares, 60), 120)` |
| slot a seed 8 | 废品 | 0.13 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.21 | 0.03 | 0.04 | 0.02 | 0.01 | 0.04 | `sub(cross_delta(LogFloatShares, 120), cross_delta(LogFloatShares, 20))` |
| slot a seed 9 | 废品 | 0.12 | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap,` | 0.21 | 0.03 | 0.04 | 0.02 | 0.02 | 0.02 | `cs_demean(cross_delta(LogFloatShares, 90))` |
| slot a seed 10 | 废品 | 0.16 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.20 | 0.00 | 0.06 | 0.03 | 0.01 | 0.11 | `mul(sub(LogTotalCap, LogFloatCap), cross_delta(LogFloatShares, 120))` |
| slot a seed 11 | 过 | 0.22 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.11 | 0.27 | 0.42 | 0.30 | 0.29 | 0.07 | `cross_delta(LogTotalCap, 120)` |
| slot a seed 12 | 废品 | 0.13 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.14 | 0.03 | 0.05 | 0.01 | 0.03 | 0.09 | `sub(cross_delta(LogTotalCap, 120), cross_delta(LogFloatCap, 120))` |
| slot b seed 1 | 过 | 0.51 | `day_var(in_max_rolling(Vwap, 60))` | 0.77 | 0.23 | 0.06 | 0.00 | 0.18 | 0.00 | `sub(LogFloatCap, LogFloatShares)` |
| slot b seed 2 | 过 | 0.50 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.44 | 0.22 | 0.07 | 0.02 | 0.23 | 0.44 | `sub(log(day_mean(Close)), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 3 | 过 | 0.50 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.44 | 0.22 | 0.07 | 0.02 | 0.23 | 0.45 | `cross_mean(sub(log(day_mean(Close)), sub(LogFloatCap, LogFloatShares)), 20)` |
| slot b seed 4 | 过 | 0.06 | `day_last(sliding_bottom_mean_masked_p5(Close, Vwap, 10))` | 0.11 | 0.01 | 0.07 | 0.06 | 0.00 | 0.05 | `cross_delta(sub(log(day_mean(Close)), sub(LogFloatCap, LogFloatShares)), 120)` |
| slot b seed 5 | 过 | 0.49 | `day_var(in_max_rolling(Vwap, 60))` | 0.77 | 0.21 | 0.02 | 0.07 | 0.16 | 0.01 | `cross_mean(sub(LogFloatCap, LogFloatShares), 60)` |
| slot b seed 6 | 过 | 0.44 | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(` | 0.46 | 0.15 | 0.16 | 0.07 | 0.15 | 0.39 | `sub(sub(LogFloatCap, LogFloatShares), log(cross_mean(day_mean(Close), 250)))` |
| slot b seed 7 | 过 | 0.51 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.45 | 0.23 | 0.06 | 0.03 | 0.24 | 0.50 | `cs_demean(sub(log(day_mean(Close)), sub(LogTotalCap, LogFloatShares)))` |
| slot b seed 8 | 过 | 0.14 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.09 | 0.11 | 0.21 | 0.40 | 0.13 | 0.14 | `sub(log(day_mean(Close)), log(cross_max(day_mean(Close), 250)))` |
| slot b seed 9 | 过 | 0.28 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.10 | 0.30 | 0.45 | 0.38 | 0.33 | 0.11 | `sub(sub(LogFloatCap, LogFloatShares), cross_mean(sub(LogFloatCap, LogFloatShares), 250))` |
| slot b seed 10 | 过 | 0.52 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.55 | 0.11 | 0.03 | 0.02 | 0.13 | 0.35 | `div(sub(LogFloatCap, LogFloatShares), log(day_mean(Close)))` |
