# 相关度表:种子 2057,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.21 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.05 | 0.22 | 0.35 | 0.20 | 0.25 | 0.08 | `ts_stddev(day_gini(Amt), 20)` |
| slot a seed 2 | 过 | 0.10 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.06 | 0.12 | 0.27 | 0.23 | 0.05 | 0.22 | `ts_stddev(day_centroid(Amt), 20)` |
| slot a seed 3 | 过 | 0.30 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.20 | 0.24 | 0.38 | 0.09 | 0.28 | 0.03 | `ts_stddev(day_gini(Volume), 40)` |
| slot a seed 4 | 过 | 0.03 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.01 | 0.12 | 0.14 | 0.17 | 0.07 | 0.15 | `ts_stddev(day_centroid(Volume), 10)` |
| slot a seed 5 | 过 | 0.24 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.12 | 0.20 | 0.31 | 0.12 | 0.24 | 0.01 | `ts_stddev(ts_stddev(day_gini(Amt), 10), 20)` |
| slot a seed 6 | 过 | 0.25 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.25 | 0.01 | 0.23 | 0.06 | 0.04 | 0.21 | `ts_stddev(ts_stddev(day_centroid(Amt), 10), 50)` |
| slot a seed 7 | 过 | 0.39 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.03 | 0.81 | 0.04 | 0.07 | 0.73 | 0.63 | `ts_mean(day_gini(Amt), 30)` |
| slot a seed 8 | 过 | 0.38 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.03 | 0.49 | 0.49 | 0.10 | 0.53 | 0.04 | `cross_mean(day_centroid(Amt), 30)` |
| slot a seed 9 | 过 | 0.33 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.14 | 0.01 | 0.21 | 0.16 | 0.04 | 0.10 | `ts_stddev(day_gini(in_pct(Amt, 1)), 20)` |
| slot a seed 10 | 过 | 0.34 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.01 | 0.44 | 0.50 | 0.19 | 0.49 | 0.04 | `ts_mean(day_centroid(Volume), 20)` |
| slot b seed 1 | 过 | 0.26 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.11 | 0.55 | 0.24 | 0.00 | 0.49 | 0.20 | `ts_mean(day_zero_ratio(Ret), 20)` |
| slot b seed 2 | 过 | 0.11 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.18 | 0.24 | 0.17 | 0.20 | 0.17 | 0.32 | `ts_stddev(day_zero_ratio(Ret), 20)` |
| slot b seed 3 | 过 | 0.26 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.10 | 0.56 | 0.21 | 0.04 | 0.50 | 0.21 | `ts_mean(day_flat_ratio(Close), 30)` |
| slot b seed 4 | 过 | 0.14 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.18 | 0.20 | 0.18 | 0.20 | 0.14 | 0.32 | `ts_stddev(day_flat_ratio(Close), 20)` |
| slot b seed 5 | 过 | 0.10 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.27 | 0.32 | 0.27 | 0.11 | 0.24 | 0.42 | `ts_stddev(day_flat_ratio(Vwap), 40)` |
| slot b seed 6 | 废品 | 0.26 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.11 | 0.54 | 0.26 | 0.07 | 0.49 | 0.20 | `cross_mean(day_zero_ratio(Ret), 10)` |
| slot b seed 7 | 废品 | 0.44 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.07 | 0.79 | 0.12 | 0.04 | 0.75 | 0.62 | `ts_mean(day_zero_ratio(in_pct(Amt, 1)), 20)` |
| slot b seed 8 | 过 | 0.24 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.21 | 0.03 | 0.28 | 0.18 | 0.03 | 0.21 | `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 20)` |
| slot b seed 9 | 过 | 0.34 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.14 | 0.75 | 0.10 | 0.02 | 0.70 | 0.59 | `ts_mean(day_flat_ratio(Vwap), 10)` |
| slot b seed 10 | 过 | 0.38 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.08 | 0.74 | 0.04 | 0.06 | 0.70 | 0.63 | `ts_stddev(day_zero_ratio(in_logchg(Amt, 1)), 30)` |
