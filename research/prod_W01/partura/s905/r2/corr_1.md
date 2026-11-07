# 相关度表:种子 905,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 2 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.64 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.98 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.55 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.75 | 0.37 | 0.31 | 0.17 | 0.40 | 0.26 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` |
| slot a seed 2 | 过 | 0.39 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.55 | 0.49 | 0.14 | 0.17 | 0.47 | 0.09 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 3 | 过 | 0.44 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.73 | 0.52 | 0.25 | 0.18 | 0.53 | 0.54 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), LogFloatCap)` |
| slot a seed 4 | 过 | 0.39 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.69 | 0.26 | 0.40 | 0.12 | 0.16 | 0.33 | `sub(cs_rank(cross_mean(day_centroid(Amt), 30)), cs_rank(cross_mean(day_gini(Amt), 30)))` |
| slot a seed 5 | 过 | 0.51 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.76 | 0.54 | 0.42 | 0.20 | 0.57 | 0.25 | `sub(cs_rank(cross_mean(div(day_first(Amt), add(day_first(Amt), day_last(Amt))), 20)), cs_rank(cross_mean(day_centroid(Amt), 20)))` |
| slot a seed 6 | 过 | 0.15 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.24 | 0.06 | 0.01 | 0.00 | 0.05 | 0.01 | `cross_mean(sub(day_centroid(mul(Amt, is_gt(Ret, 0))), day_centroid(Amt)), 20)` |
| slot a seed 7 | 过 | 0.06 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.06 | 0.10 | 0.09 | 0.04 | 0.08 | 0.00 | `cross_mean(sub(day_centroid(mul(Amt, is_lt(Ret, 0))), day_centroid(Amt)), 20)` |
| slot a seed 8 | 过 | 0.01 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.24 | 0.04 | 0.15 | 0.62 | 0.06 | 0.03 | `cross_mean(sub(day_centroid(Amt), day_centroid(Volume)), 20)` |
| slot a seed 9 | 过 | 0.50 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.86 | 0.43 | 0.42 | 0.13 | 0.47 | 0.07 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)` |
| slot a seed 10 | 过 | 0.25 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.32 | 0.14 | 0.39 | 0.09 | 0.22 | 0.16 | `ts_min(day_centroid(Amt), 40)` |
| slot a seed 11 | 过 | 0.36 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.55 | 0.33 | 0.48 | 0.08 | 0.39 | 0.09 | `cross_tail_mean_q25(day_centroid(Amt), 60)` |
| slot a seed 12 | 过 | 0.10 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.16 | 0.17 | 0.31 | 0.10 | 0.07 | 0.32 | `cross_stddev(day_centroid(Amt), 40)` |
| slot a seed 13 | 过 | 0.64 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.60 | 0.03 | 0.03 | 0.18 | 0.02 | 0.04 | `sub(cross_mean(day_centroid(Amt), 5), cross_mean(day_centroid(Amt), 60))` |
| slot a seed 14 | 过 | 0.36 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.81 | 0.03 | 0.28 | 0.04 | 0.01 | 0.24 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 40), cross_mean(day_std(Amt), 30))` |
| slot a seed 15 | 过 | 0.42 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.83 | 0.06 | 0.29 | 0.09 | 0.04 | 0.23 | `cs_regres(cs_regres(cross_mean(day_centroid(Amt), 30), LogFloatShares), cs_rank(cross_mean(day_std(Amt), 30)))` |
| slot a seed 16 | 过 | 0.46 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.77 | 0.06 | 0.27 | 0.14 | 0.09 | 0.08 | `cs_last_low10(cross_mean(day_centroid(Amt), 20), cross_mean(day_sum(Amt), 20))` |
| slot b seed 1 | 过 | 0.44 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.63 | 0.46 | 0.23 | 0.19 | 0.46 | 0.37 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| slot b seed 2 | 过 | 0.04 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.12 | 0.17 | 0.14 | 0.04 | 0.12 | 0.43 | `cs_regres(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), cross_mean(day_centroid(Amt), 20))` |
| slot b seed 3 | 过 | 0.30 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.30 | 0.29 | 0.38 | 0.14 | 0.37 | 0.00 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 20)` |
| slot b seed 4 | 过 | 0.38 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.67 | 0.32 | 0.14 | 0.08 | 0.28 | 0.19 | `cs_regres(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), cross_mean(day_centroid(Amt), 20))` |
| slot b seed 5 | 过 | 0.20 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.28 | 0.29 | 0.03 | 0.10 | 0.24 | 0.41 | `cross_mean(div(day_last(Amt), day_sum(Amt)), 20)` |
| slot b seed 6 | 过 | 0.48 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.70 | 0.39 | 0.45 | 0.16 | 0.43 | 0.04 | `cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 20)` |
| slot b seed 7 | 过 | 0.16 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.19 | 0.10 | 0.26 | 0.02 | 0.14 | 0.25 | `cross_mean(div(day_sum(in_slice(Amt, 91, 150)), day_sum(Amt)), 20)` |
| slot b seed 8 | 过 | 0.44 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.59 | 0.26 | 0.34 | 0.14 | 0.29 | 0.05 | `cross_mean(div(day_sum(in_slice(Amt, 181, 210)), day_sum(Amt)), 20)` |
| slot b seed 9 | 过 | 0.35 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.42 | 0.48 | 0.36 | 0.19 | 0.52 | 0.31 | `cross_mean(div(day_first(Amt), add(day_first(Amt), day_last(Amt))), 20)` |
| slot b seed 10 | 过 | 0.68 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.65 | 0.05 | 0.18 | 0.19 | 0.07 | 0.05 | `cross_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), 240)` |
| slot b seed 11 | 过 | 0.44 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.63 | 0.41 | 0.25 | 0.18 | 0.40 | 0.22 | `cs_regres(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)` |
| slot b seed 12 | 过 | 0.15 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.12 | 0.83 | 0.05 | 0.02 | 0.74 | 0.53 | `cross_mean(day_gini(Amt), 30)` |
| slot b seed 13 | 过 | 0.04 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.10 | 0.02 | 0.04 | 0.20 | 0.01 | 0.10 | `cross_mean(day_signed_ratio(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), 20)` |
| slot b seed 14 | 过 | 0.10 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.11 | 0.12 | 0.07 | 0.12 | 0.12 | 0.03 | `cross_mean(sub(div(day_last(in_slice(Close, 211, 240)), day_first(in_slice(Close, 211, 240))), 1), 20)` |
| R 1 variant 1 | 过 | 0.68 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.97 | 0.40 | 0.35 | 0.22 | 0.42 | 0.12 | `cross_mean(day_centroid(Amt), 10)` |
| R 1 variant 2 | 过 | 0.61 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.94 | 0.44 | 0.39 | 0.22 | 0.46 | 0.13 | `cross_mean(day_centroid(Amt), 14)` |
| R 1 variant 3 | 过 | 0.62 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.86 | 0.06 | 0.30 | 0.17 | 0.04 | 0.20 | `cs_regres(cross_mean(day_centroid(Amt), 20), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 4 | 过 | 0.42 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.83 | 0.06 | 0.29 | 0.09 | 0.04 | 0.24 | `cs_regres(cross_mean(day_centroid(Amt), 30), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 5 | 过 | 0.58 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.91 | 0.48 | 0.42 | 0.19 | 0.51 | 0.12 | `cs_regres(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| R 1 variant 6 | 过 | 0.64 | `pow_2_5(cross_mean(day_centroid(Amt), 3))` | 0.95 | 0.41 | 0.37 | 0.22 | 0.43 | 0.11 | `cs_regres(cross_mean(day_centroid(Amt), 12), LogFloatShares)` |
| R 1 variant 7 | 过 | 0.61 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.86 | 0.06 | 0.29 | 0.17 | 0.04 | 0.20 | `cs_regres(cs_regres(cross_mean(day_centroid(Amt), 20), LogFloatShares), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 8 | 过 | 0.62 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.87 | 0.04 | 0.30 | 0.17 | 0.02 | 0.20 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30))` |
| R 2 variant 1 | 过 | 0.92 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.86 | 0.11 | 0.23 | 0.23 | 0.14 | 0.08 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 240)` |
| R 2 variant 2 | 过 | 0.88 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.79 | 0.12 | 0.24 | 0.23 | 0.16 | 0.11 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 360)` |
| R 2 variant 3 | 过 | 0.86 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.75 | 0.14 | 0.24 | 0.22 | 0.17 | 0.12 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 480)` |
| R 2 variant 4 | 过 | 0.62 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.67 | 0.16 | 0.23 | 0.14 | 0.19 | 0.12 | `cross_zscore(cross_mean(day_centroid(Amt), 40), 360)` |
| R 2 variant 5 | 过 | 0.73 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.78 | 0.08 | 0.19 | 0.24 | 0.11 | 0.09 | `cross_zscore(cross_mean(day_centroid(Amt), 10), 360)` |
| R 2 variant 6 | 过 | 0.77 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.79 | 0.35 | 0.38 | 0.23 | 0.39 | 0.12 | `sub(cross_mean(day_centroid(Amt), 20), mul(0.5, cross_mean(day_centroid(Amt), 240)))` |
| R 2 variant 7 | 过 | 0.85 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.71 | 0.02 | 0.29 | 0.22 | 0.05 | 0.07 | `add(cs_rank(cross_zscore(cross_mean(day_centroid(Amt), 20), 240)), cs_rank(cs_regres(cross_mean(day_centroid(Amt), 20), cs_rank(cross_mean(day_std(Amt), 30)))))` |
| R 2 variant 8 | 过 | 0.90 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` | 0.84 | 0.10 | 0.26 | 0.22 | 0.13 | 0.04 | `cross_zscore(cs_regres(cross_mean(day_centroid(Amt), 20), LogFloatShares), 240)` |
