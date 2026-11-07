# 相关度表:种子 906,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 13 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.71 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.70 | 0.48 | 0.42 | 0.19 | 0.51 | 0.13 | `cross_mean(day_centroid(Amt), 20)` |
| slot a seed 1 | 过 | 0.63 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.66 | 0.02 | 0.31 | 0.17 | 0.01 | 0.18 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30))` |
| slot a seed 2 | 过 | 0.71 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.69 | 0.40 | 0.43 | 0.18 | 0.43 | 0.00 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), LogFloatCap)` |
| slot a seed 3 | 过 | 0.62 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.66 | 0.39 | 0.01 | 0.10 | 0.39 | 0.19 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 4 | 过 | 0.71 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.69 | 0.46 | 0.41 | 0.19 | 0.48 | 0.10 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| slot a seed 5 | 过 | 0.70 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.68 | 0.46 | 0.41 | 0.19 | 0.48 | 0.11 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)` |
| slot a seed 6 | 过 | 0.43 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.39 | 0.07 | 0.20 | 0.24 | 0.10 | 0.05 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` |
| slot a seed 7 | 过 | 0.43 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.39 | 0.08 | 0.21 | 0.24 | 0.11 | 0.05 | `sub(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 120))` |
| slot a seed 8 | 过 | 0.58 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.61 | 0.37 | 0.31 | 0.17 | 0.40 | 0.26 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` |
| slot a seed 9 | 过 | 0.61 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.56 | 0.42 | 0.36 | 0.14 | 0.44 | 0.02 | `cs_last_low20(cross_mean(day_centroid(Amt), 20), ListAge)` |
| slot a seed 10 | 过 | 0.47 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.53 | 0.33 | 0.24 | 0.14 | 0.35 | 0.38 | `cs_first_high20(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 11 | 过 | 0.49 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.45 | 0.32 | 0.31 | 0.11 | 0.33 | 0.21 | `cs_last_high20(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 12 | 过 | 0.33 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.29 | 0.16 | 0.21 | 0.06 | 0.19 | 0.22 | `sub(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_centroid(Ret), 20)))` |
| slot a seed 13 | 过 | 0.61 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.56 | 0.45 | 0.45 | 0.18 | 0.50 | 0.08 | `sub(cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20)), cs_rank(cross_mean(day_centroid(Amt), 20)))` |
| slot a seed 14 | 过 | 0.44 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.60 | 0.30 | 0.36 | 0.17 | 0.21 | 0.33 | `sub(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_gini(Amt), 20)))` |
| slot a seed 15 | 过 | 0.49 | `cs_first_low20(LogFloatCap, LogFloatCap)` | 0.56 | 0.15 | 0.32 | 0.12 | 0.18 | 0.15 | `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(LogFloatCap, LogFloatCap))` |
| slot a seed 16 | 过 | 0.66 | `cs_first_low20(LogFloatCap, LogFloatCap)` | 0.48 | 0.11 | 0.19 | 0.05 | 0.12 | 0.04 | `cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 20))` |
| slot b seed 1 | 过 | 0.35 | `sigmoid(cs_first_low20(cs_first_low20(cross_mean(day_first(A` | 0.24 | 0.29 | 0.38 | 0.14 | 0.37 | 0.00 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 20)` |
| slot b seed 2 | 过 | 0.54 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), c` | 0.44 | 0.46 | 0.23 | 0.19 | 0.46 | 0.37 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| slot b seed 3 | 过 | 0.62 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.55 | 0.39 | 0.45 | 0.16 | 0.43 | 0.04 | `cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 20)` |
| slot b seed 4 | 过 | 0.26 | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centro` | 0.16 | 0.10 | 0.20 | 0.00 | 0.13 | 0.21 | `cross_mean(div(day_sum(in_slice(Amt, 121, 150)), day_sum(Amt)), 20)` |
| slot b seed 5 | 过 | 0.39 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), c` | 0.33 | 0.24 | 0.28 | 0.09 | 0.27 | 0.22 | `cross_mean(sub(day_centroid(Ret), day_centroid(Amt)), 20)` |
| slot b seed 6 | 过 | 0.17 | `cs_first_low20(LogFloatCap, day_sum(Low))` | 0.10 | 0.09 | 0.06 | 0.20 | 0.10 | 0.29 | `cross_mean(day_wstd(in_index(Amt), Amt), 20)` |
| slot b seed 7 | 过 | 0.37 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.21 | 0.64 | 0.24 | 0.02 | 0.62 | 0.07 | `cross_mean(day_corr(abs_(sub(in_index(Amt), 0.5)), Amt), 20)` |
| slot b seed 8 | 过 | 0.66 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), c` | 0.68 | 0.69 | 0.33 | 0.15 | 0.67 | 0.29 | `cross_mean(day_corr(in_index(Amt), Amt), 20)` |
| slot b seed 9 | 过 | 0.42 | `cs_last_low20(cross_mean(day_gini(Amt), 20), cs_first_low20(` | 0.16 | 0.52 | 0.15 | 0.10 | 0.41 | 0.30 | `cross_mean(day_es_ratio_hi(Amt), 20)` |
| slot b seed 10 | 过 | 0.33 | `sigmoid(cs_first_low20(cs_first_low20(cross_mean(day_first(A` | 0.24 | 0.07 | 0.29 | 0.12 | 0.01 | 0.23 | `cs_bucket_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), cross_mean(day_std(Amt), 30))` |
| slot b seed 11 | 过 | 0.37 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), c` | 0.42 | 0.02 | 0.10 | 0.17 | 0.01 | 0.13 | `cs_bucket_rank(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), cross_mean(day_std(Amt), 30))` |
| slot b seed 12 | 过 | 0.53 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), c` | 0.45 | 0.48 | 0.37 | 0.20 | 0.52 | 0.24 | `sub(cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20)), cs_rank(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)))` |
| slot b seed 13 | 过 | 0.08 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.07 | 0.01 | 0.08 | 0.19 | 0.03 | 0.04 | `cross_zscore(cross_mean(div(day_first(Amt), day_sum(Amt)), 5), 120)` |
| slot b seed 14 | 过 | 0.38 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap` | 0.33 | 0.14 | 0.31 | 0.07 | 0.17 | 0.01 | `cs_bucket_rank(cross_mean(sub(day_centroid(Ret), day_centroid(Amt)), 20), LogFloatCap)` |
| R 1 variant 1 | 过 | 0.24 | `cs_first_low20(LogFloatCap, LogFloatCap)` | 0.20 | 0.01 | 0.08 | 0.00 | 0.00 | 0.20 | `cs_first_low20(LogFloatCap, LogTotalCap)` |
| R 1 variant 2 | 过 | 0.31 | `cs_first_low20(LogFloatCap, LogFloatCap)` | 0.20 | 0.05 | 0.05 | 0.00 | 0.04 | 0.07 | `cs_first_low20(LogTotalCap, LogTotalCap)` |
| R 1 variant 3 | 过 | 0.93 | `cs_first_low20(LogFloatCap, LogFloatCap)` | 0.70 | 0.23 | 0.04 | 0.00 | 0.21 | 0.03 | `cs_first_low20(LogTotalCap, LogFloatCap)` |
| R 1 variant 4 | 过 | 0.92 | `cs_first_low20(LogFloatCap, LogFloatCap)` | 0.94 | 0.18 | 0.05 | 0.04 | 0.16 | 0.04 | `cs_first_low20(LogFloatCap, cross_mean(LogFloatCap, 20))` |
| R 2 variant 1 | 过 | 0.88 | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap))` | 0.98 | 0.10 | 0.10 | 0.04 | 0.09 | 0.26 | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 5))` |
| R 2 variant 2 | 过 | 0.85 | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap))` | 0.95 | 0.07 | 0.13 | 0.04 | 0.05 | 0.26 | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))` |
| R 2 variant 3 | 过 | 0.78 | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap))` | 0.90 | 0.01 | 0.21 | 0.08 | 0.03 | 0.22 | `cs_last_low10(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))` |
| R 2 variant 4 | 过 | 0.68 | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centro` | 0.79 | 0.14 | 0.30 | 0.13 | 0.17 | 0.14 | `cs_last_low20(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))` |
| R 3 variant 1 | 过 | 0.97 | `cs_first_low20(LogFloatCap, day_sum(Low))` | 0.96 | 0.22 | 0.10 | 0.05 | 0.22 | 0.60 | `cs_first_low20(LogFloatCap, cross_mean(day_sum(Low), 20))` |
| R 3 variant 2 | 过 | 0.99 | `cs_first_low20(LogFloatCap, day_sum(Low))` | 0.98 | 0.21 | 0.11 | 0.03 | 0.22 | 0.60 | `cs_first_low20(LogFloatCap, cross_mean(day_sum(Low), 5))` |
| R 3 variant 3 | 过 | 0.56 | `cs_first_low20(LogFloatCap, day_sum(Low))` | 0.22 | 0.25 | 0.06 | 0.02 | 0.27 | 0.71 | `cs_first_low20(LogFloatCap, sub(LogFloatCap, LogFloatShares))` |
| R 4 variant 1 | 过 | 0.92 | `sigmoid(cs_first_low20(cs_first_low20(cross_mean(day_first(A` | 0.94 | 0.17 | 0.14 | 0.00 | 0.11 | 0.24 | `sigmoid(cs_first_low20(cs_first_low20(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), day_last(Vwap)))` |
| R 4 variant 2 | 过 | 0.74 | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centro` | 0.69 | 0.05 | 0.26 | 0.07 | 0.11 | 0.18 | `cs_first_low20(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| R 5 variant 1 | 过 | 0.97 | `cs_last_low20(cross_mean(day_gini(Amt), 20), cs_first_low20(` | 0.98 | 0.40 | 0.07 | 0.04 | 0.35 | 0.19 | `cs_last_low20(cross_mean(day_gini(Amt), 60), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| R 5 variant 2 | 过 | 1.00 | `cs_last_low20(cross_mean(day_gini(Amt), 20), cs_first_low20(` | 1.00 | 0.42 | 0.02 | 0.03 | 0.37 | 0.18 | `cs_last_low20(cross_mean(day_gini(Volume), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| R 6 variant 1 | 过 | 0.83 | `cs_first_low20(cross_mean(day_signed_ratio(Ret, Amt), 20), c` | 0.93 | 0.01 | 0.18 | 0.16 | 0.02 | 0.03 | `cs_first_low20(cross_mean(day_signed_ratio(Ret, Amt), 60), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
