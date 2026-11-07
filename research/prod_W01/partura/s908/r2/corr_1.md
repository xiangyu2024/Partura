# 相关度表:种子 908,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 7 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.63 | `sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centro` | 0.67 | 0.15 | 0.07 | 0.10 | 0.15 | 0.16 | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` |
| slot a seed 1 | 过 | 0.69 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.66 | 0.38 | 0.07 | 0.03 | 0.35 | 0.26 | `cross_max(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| slot a seed 2 | 过 | 0.54 | `ts_min(day_centroid(Amt), 20)` | 0.47 | 0.07 | 0.32 | 0.22 | 0.13 | 0.03 | `cross_min(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| slot a seed 3 | 过 | 0.84 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.84 | 0.53 | 0.17 | 0.11 | 0.51 | 0.42 | `cross_quantile_q75(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 30)` |
| slot a seed 4 | 过 | 0.82 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.82 | 0.53 | 0.11 | 0.07 | 0.50 | 0.39 | `cross_tail_mean_q75(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 30)` |
| slot a seed 5 | 过 | 0.33 | `ts_min(day_centroid(Amt), 20)` | 0.26 | 0.13 | 0.29 | 0.11 | 0.05 | 0.16 | `cross_semistd_pos(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 30)` |
| slot a seed 6 | 过 | 0.62 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.61 | 0.05 | 0.18 | 0.19 | 0.07 | 0.05 | `cross_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), 240)` |
| slot a seed 7 | 过 | 0.57 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.56 | 0.02 | 0.15 | 0.19 | 0.04 | 0.02 | `cross_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), 120)` |
| slot a seed 8 | 过 | 0.35 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.29 | 0.23 | 0.26 | 0.01 | 0.26 | 0.11 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), day_es_ratio_hi(Amt), 60)` |
| slot a seed 9 | 过 | 0.36 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.27 | 0.26 | 0.26 | 0.01 | 0.28 | 0.10 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), day_skew(Amt), 60)` |
| slot a seed 10 | 过 | 0.20 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.17 | 0.18 | 0.13 | 0.02 | 0.19 | 0.05 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), day_sum(Amt), 60)` |
| slot a seed 11 | 过 | 0.28 | `ts_min(day_centroid(Amt), 20)` | 0.31 | 0.09 | 0.12 | 0.02 | 0.11 | 0.12 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), div(day_sum(in_slice(Amt, 0, 30)), day_sum(Amt)), 60)` |
| slot a seed 12 | 过 | 0.96 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.97 | 0.39 | 0.23 | 0.19 | 0.38 | 0.21 | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)` |
| slot a seed 13 | 过 | 0.93 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.91 | 0.31 | 0.25 | 0.17 | 0.32 | 0.21 | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), day_wmean(Open, Amt))` |
| slot a seed 14 | 过 | 0.92 | `cs_first_low40(cs_bucket_zscore(cross_mean(day_centroid(Amt)` | 0.86 | 0.41 | 0.07 | 0.11 | 0.41 | 0.68 | `cs_first_low40(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)` |
| slot a seed 15 | 过 | 0.42 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume` | 0.40 | 0.10 | 0.02 | 0.04 | 0.08 | 0.06 | `ts_quantile_q75(cs_regres(ListAge, div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 20)` |
| slot a seed 16 | 过 | 0.94 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.92 | 0.49 | 0.43 | 0.20 | 0.52 | 0.14 | `sub(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), cross_mean(div(day_sum(in_slice(Amt, 0, 30)), day_sum(Amt)), 20))` |
| slot b seed 1 | 过 | 0.30 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.32 | 0.24 | 0.17 | 0.02 | 0.27 | 0.07 | `cross_corr(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 2 | 过 | 0.36 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.32 | 0.33 | 0.20 | 0.01 | 0.36 | 0.04 | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` |
| slot b seed 3 | 过 | 0.26 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.29 | 0.20 | 0.12 | 0.01 | 0.22 | 0.07 | `cross_corr(div(day_first(Volume), day_es_ratio_hi(Volume)), day_es_ratio_hi(Volume), 60)` |
| slot b seed 4 | 过 | 0.34 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.33 | 0.28 | 0.20 | 0.02 | 0.31 | 0.05 | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_es_ratio_hi(Amt), 60)` |
| slot b seed 5 | 过 | 0.15 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.14 | 0.05 | 0.14 | 0.01 | 0.04 | 0.02 | `cross_corr(day_last(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 6 | 过 | 0.11 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.13 | 0.03 | 0.09 | 0.00 | 0.04 | 0.03 | `cross_corr(day_last(Amt), day_skew(Amt), 60)` |
| slot b seed 7 | 过 | 0.27 | `ts_min(day_centroid(Amt), 20)` | 0.30 | 0.15 | 0.14 | 0.03 | 0.18 | 0.05 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` |
| slot b seed 8 | 过 | 0.35 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.33 | 0.46 | 0.17 | 0.01 | 0.48 | 0.14 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` |
| slot b seed 9 | 过 | 0.30 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.29 | 0.27 | 0.18 | 0.01 | 0.29 | 0.07 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` |
| slot b seed 10 | 过 | 0.41 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.38 | 0.26 | 0.25 | 0.02 | 0.28 | 0.10 | `cross_corr(day_centroid(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 11 | 过 | 0.41 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.37 | 0.30 | 0.26 | 0.01 | 0.32 | 0.10 | `cross_corr(day_centroid(Volume), day_skew(Volume), 60)` |
| slot b seed 12 | 过 | 0.55 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.40 | 0.48 | 0.26 | 0.07 | 0.49 | 0.31 | `sub(cross_mean(div(day_first(Amt), day_sum(Amt)), 60), cross_mean(div(day_last(Amt), day_sum(Amt)), 60))` |
| slot b seed 13 | 过 | 0.42 | `cs_first_low40(cs_bucket_zscore(cross_mean(day_centroid(Amt)` | 0.33 | 0.43 | 0.29 | 0.05 | 0.50 | 0.24 | `cs_bucket_demean(cross_mean(div(day_first(Amt), day_sum(Amt)), 60), LogFloatCap)` |
| slot b seed 14 | 过 | 0.40 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.33 | 0.29 | 0.35 | 0.02 | 0.36 | 0.07 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 60)` |
| R 1 variant 1 | 过 | 0.92 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.94 | 0.51 | 0.23 | 0.14 | 0.50 | 0.40 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 30)` |
| R 1 variant 2 | 过 | 0.96 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.98 | 0.49 | 0.23 | 0.16 | 0.48 | 0.39 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 25)` |
| R 1 variant 3 | 过 | 0.98 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.98 | 0.45 | 0.24 | 0.19 | 0.45 | 0.34 | `cross_mean(div(day_sum(in_slice(Amt, 211, 239)), day_sum(Amt)), 20)` |
| R 1 variant 4 | 过 | 0.95 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.94 | 0.47 | 0.28 | 0.20 | 0.47 | 0.31 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20)` |
| R 1 variant 5 | 过 | 0.92 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.90 | 0.45 | 0.15 | 0.17 | 0.44 | 0.45 | `cross_mean(div(day_sum(in_slice(Amt, 226, 240)), day_sum(Amt)), 20)` |
| R 1 variant 6 | 过 | 0.89 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.86 | 0.47 | 0.32 | 0.20 | 0.48 | 0.26 | `cross_mean(div(day_sum(in_slice(Amt, 181, 240)), day_sum(Amt)), 20)` |
| R 1 variant 7 | 过 | 0.94 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.93 | 0.53 | 0.21 | 0.15 | 0.52 | 0.43 | `cross_ema(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 15)` |
| R 1 variant 8 | 过 | 0.92 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.94 | 0.51 | 0.23 | 0.14 | 0.50 | 0.40 | `cross_mean(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume)), 30)` |
| R 2 variant 1 | 过 | 1.00 | `sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centro` | 1.00 | 0.15 | 0.15 | 0.11 | 0.17 | 0.09 | `sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centroid(Amt))` |
| R 2 variant 2 | 过 | 0.99 | `sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centro` | 0.98 | 0.17 | 0.16 | 0.12 | 0.18 | 0.08 | `sub(day_centroid(Ret), mul(day_centroid(Volume), 3))` |
| R 2 variant 3 | 过 | 0.99 | `sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centro` | 0.98 | 0.13 | 0.14 | 0.10 | 0.15 | 0.10 | `sub(day_centroid(Ret), mul(day_centroid(Volume), 1.5))` |
| R 2 variant 4 | 过 | 0.59 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.97 | 0.27 | 0.27 | 0.18 | 0.29 | 0.15 | `cross_mean(sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centroid(Volume)), 5)` |
| R 3 variant 1 | 过 | 0.92 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.93 | 0.51 | 0.41 | 0.12 | 0.53 | 0.11 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 30), LogFloatShares), LogFloatShares)` |
| R 3 variant 2 | 过 | 0.92 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.93 | 0.51 | 0.41 | 0.13 | 0.54 | 0.11 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Volume), 30), LogFloatShares), LogFloatShares)` |
| R 3 variant 3 | 过 | 0.96 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.97 | 0.48 | 0.41 | 0.15 | 0.51 | 0.11 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 25), LogFloatShares), LogFloatShares)` |
| R 3 variant 4 | 过 | 0.92 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.93 | 0.50 | 0.41 | 0.12 | 0.53 | 0.11 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 30), LogFloatShares)` |
