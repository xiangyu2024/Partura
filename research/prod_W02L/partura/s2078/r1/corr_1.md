# 相关度表:种子 2078,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 1.00 | 0.45 | 0.64 | 0.22 | 0.49 | 0.00 | `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` |
| slot a seed 1 | 过 | 0.86 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.93 | 0.36 | 0.23 | 0.22 | 0.37 | 0.05 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_std(Ret), 30))` |
| slot a seed 2 | 过 | 0.92 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.83 | 0.49 | 0.66 | 0.11 | 0.52 | 0.00 | `sub(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), ts_min(cs_demean(div(day_mean(Ret), 2)), 30))` |
| slot a seed 3 | 过 | 0.99 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.98 | 0.44 | 0.62 | 0.15 | 0.48 | 0.01 | `sub(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(cs_demean(div(day_mean(Ret), 2)), 30))` |
| slot a seed 4 | 过 | 0.63 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.45 | 0.30 | 0.38 | 0.24 | 0.34 | 0.13 | `mul(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_skew(Ret), 30))` |
| slot a seed 5 | 过 | 0.83 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.89 | 0.47 | 0.05 | 0.04 | 0.49 | 0.56 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_mean(Volume), 30))` |
| slot a seed 6 | 过 | 0.51 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.43 | 0.09 | 0.21 | 0.28 | 0.12 | 0.02 | `sub(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_delay(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30))` |
| slot a seed 7 | 过 | 0.55 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.29 | 0.29 | 0.46 | 0.43 | 0.33 | 0.03 | `mul(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_corr(Ret, Volume), 30))` |
| slot a seed 8 | 过 | 0.97 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.98 | 0.46 | 0.64 | 0.18 | 0.50 | 0.00 | `cross_mean(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 5)` |
| slot a seed 9 | 过 | 0.74 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.77 | 0.22 | 0.27 | 0.26 | 0.26 | 0.08 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_stddev(day_mean(Ret), 30))` |
| slot a seed 10 | 过 | 0.39 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.51 | 0.16 | 0.34 | 0.20 | 0.07 | 0.24 | `sub(cs_normalize(ts_max(cs_demean(div(day_mean(Ret), 2)), 30)), cs_normalize(cross_mean(day_pos_ratio(Ret), 30)))` |
| slot a seed 11 | 过 | 0.29 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.54 | 0.24 | 0.23 | 0.20 | 0.15 | 0.23 | `mul(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_flat_ratio(Ret), 30))` |
| slot a seed 12 | 过 | 0.56 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.14 | 0.32 | 0.96 | 0.09 | 0.38 | 0.07 | `sub(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_std(Ret), 30))` |
| slot b seed 1 | 过 | 0.48 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.08 | 0.44 | 0.50 | 0.19 | 0.49 | 0.04 | `cross_mean(day_centroid(Volume), 20)` |
| slot b seed 2 | 过 | 0.55 | `pow_2(day_cov(Amt, Vwap))` | 0.12 | 0.82 | 0.01 | 0.06 | 0.74 | 0.62 | `cross_mean(day_gini(Volume), 20)` |
| slot b seed 3 | 废品 | 0.84 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.81 | 0.77 | 0.15 | 0.03 | 0.76 | 0.59 | `cross_mean(day_flat_ratio(Volume), 20)` |
| slot b seed 4 | 废品 | 0.72 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.54 | 0.86 | 0.15 | 0.00 | 0.83 | 0.66 | `cross_mean(day_zero_ratio(Volume), 20)` |
| slot b seed 5 | 过 | 0.16 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.13 | 0.01 | 0.13 | 0.64 | 0.03 | 0.04 | `sub(cross_mean(day_centroid(Volume), 20), cross_mean(day_centroid(Amt), 20))` |
| slot b seed 6 | 过 | 0.59 | `pow_2(day_cov(Amt, Vwap))` | 0.30 | 0.78 | 0.36 | 0.11 | 0.77 | 0.26 | `mul(cross_mean(day_ar1_coefficient(Volume), 20), cross_mean(day_centroid(Volume), 20))` |
| slot b seed 7 | 过 | 0.50 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.28 | 0.45 | 0.25 | 0.14 | 0.45 | 0.00 | `cross_mean(day_corr(Volume, abs(Ret)), 20)` |
| slot b seed 8 | 过 | 0.41 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.17 | 0.35 | 0.32 | 0.12 | 0.37 | 0.03 | `div(cross_mean(day_gini(Volume), 20), cross_mean(day_gini(Amt), 20))` |
| slot b seed 9 | 过 | 0.18 | `pow_2(day_cov(Amt, Vwap))` | 0.04 | 0.33 | 0.40 | 0.20 | 0.24 | 0.47 | `sub(cs_normalize(cross_mean(day_centroid(Volume), 20)), cs_normalize(cross_mean(day_gini(Volume), 20)))` |
| slot b seed 10 | 过 | 0.62 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.29 | 0.77 | 0.42 | 0.14 | 0.78 | 0.23 | `cross_mean(day_ar1_coefficient(Volume), 20)` |
| slot b seed 11 | 过 | 0.92 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.94 | 0.72 | 0.20 | 0.07 | 0.74 | 0.59 | `cross_mean(day_distinct_ratio(Volume), 20)` |
| slot b seed 12 | 过 | 0.49 | `pow_2(day_cov(Amt, Vwap))` | 0.22 | 0.67 | 0.01 | 0.07 | 0.61 | 0.46 | `sub(cross_mean(day_gini(Volume), 20), cross_mean(day_gini(Ret), 20))` |
| R 1 variant 1 | 过 | 0.75 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.61 | 0.40 | 0.56 | 0.07 | 0.42 | 0.07 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 60))` |
| R 1 variant 2 | 过 | 0.62 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.38 | 0.33 | 0.49 | 0.02 | 0.35 | 0.12 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 90))` |
| R 1 variant 3 | 过 | 0.75 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.61 | 0.40 | 0.56 | 0.07 | 0.42 | 0.07 | `ts_max(cs_demean(div(day_mean(Ret), 2)), 60)` |
| R 1 variant 4 | 过 | 0.53 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.27 | 0.27 | 0.44 | 0.00 | 0.28 | 0.17 | `ts_max(cs_demean(div(day_mean(Ret), 2)), 120)` |
| R 1 variant 5 | 过 | 0.70 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.49 | 0.43 | 0.57 | 0.02 | 0.45 | 0.06 | `sub(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), ts_min(cs_demean(div(day_mean(Ret), 2)), 60))` |
| R 1 variant 6 | 过 | 0.57 | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` | 0.60 | 0.29 | 0.12 | 0.08 | 0.29 | 0.02 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), cross_mean(day_std(Ret), 60))` |
