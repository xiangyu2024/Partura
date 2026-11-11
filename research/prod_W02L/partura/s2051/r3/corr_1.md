# 相关度表:种子 2051,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 11 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.33 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.21 | 0.35 | 0.04 | 0.04 | 0.30 | 0.19 | `ts_mean(day_kurt(Volume), 5)` |
| slot a seed 1 | 过 | 0.53 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.53 | 0.19 | 0.10 | 0.01 | 0.21 | 0.03 | `cross_regbeta(sub(log(day_sum(Volume)), LogFloatShares), ts_mean(day_kurt(Volume), 5), 120)` |
| slot a seed 2 | 过 | 0.48 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.47 | 0.08 | 0.12 | 0.01 | 0.12 | 0.10 | `cross_regbeta(cross_zscore(day_sum(Volume), 20), ts_mean(day_kurt(Volume), 5), 120)` |
| slot a seed 3 | 过 | 0.26 | `ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient` | 0.14 | 0.21 | 0.04 | 0.02 | 0.17 | 0.21 | `cross_regbeta(day_gini(Volume), ts_mean(day_kurt(Volume), 5), 120)` |
| slot a seed 4 | 过 | 0.38 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.35 | 0.17 | 0.15 | 0.00 | 0.20 | 0.12 | `cross_regbeta(day_centroid(Volume), ts_mean(day_kurt(Volume), 5), 120)` |
| slot a seed 5 | 过 | 0.14 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.14 | 0.01 | 0.04 | 0.00 | 0.03 | 0.04 | `cross_regbeta(day_sum(Ret), ts_mean(day_kurt(Volume), 5), 120)` |
| slot a seed 6 | 过 | 0.39 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.35 | 0.01 | 0.07 | 0.02 | 0.02 | 0.22 | `cross_regbeta(day_sum(Amt), ts_mean(day_kurt(Volume), 5), 241)` |
| slot a seed 7 | 过 | 0.54 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.54 | 0.19 | 0.13 | 0.01 | 0.22 | 0.07 | `cross_corr(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120)` |
| slot a seed 8 | 过 | 0.37 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.34 | 0.20 | 0.09 | 0.01 | 0.22 | 0.04 | `cross_corr(sub(log(day_sum(Volume)), LogFloatShares), ts_mean(day_kurt(Volume), 5), 241)` |
| slot a seed 9 | 过 | 0.58 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.58 | 0.04 | 0.06 | 0.02 | 0.06 | 0.16 | `cs_bucket_demean(cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120), LogFloatCap)` |
| slot a seed 10 | 过 | 0.44 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.43 | 0.02 | 0.03 | 0.01 | 0.04 | 0.19 | `cross_ema(cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120), 20)` |
| slot a seed 11 | 过 | 0.27 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.28 | 0.08 | 0.04 | 0.05 | 0.09 | 0.06 | `cross_zscore(cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 241), 60)` |
| slot a seed 12 | 过 | 0.17 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.16 | 0.00 | 0.04 | 0.04 | 0.01 | 0.00 | `sub(cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120), cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 30))` |
| slot b seed 1 | 过 | 0.45 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.34 | 0.46 | 0.09 | 0.01 | 0.48 | 0.28 | `cross_regbeta(day_sum(Volume), ts_mean(day_gini(Volume), 5), 120)` |
| slot b seed 2 | 过 | 0.11 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.20 | 0.34 | 0.06 | 0.01 | 0.34 | 0.47 | `cross_regbeta(day_sum(Volume), ts_mean(day_centroid(Volume), 5), 120)` |
| slot b seed 3 | 过 | 0.58 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.58 | 0.05 | 0.04 | 0.01 | 0.07 | 0.18 | `cross_regbeta(day_sum(Volume), ts_mean(day_skew(Volume), 5), 120)` |
| slot b seed 4 | 废品 | 0.06 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.07 | 0.10 | 0.01 | 0.00 | 0.10 | 0.12 | `cross_regbeta(day_sum(Volume), ts_mean(day_at_max_ratio(Volume), 5), 120)` |
| slot b seed 5 | 过 | 0.50 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.48 | 0.03 | 0.06 | 0.02 | 0.06 | 0.21 | `cross_regbeta(day_sum(Volume), ts_mean(day_es_ratio_hi(Volume), 5), 120)` |
| slot b seed 6 | 过 | 0.43 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.44 | 0.49 | 0.18 | 0.02 | 0.52 | 0.23 | `cross_regbeta(day_sum(Amt), ts_mean(day_gini(Volume), 5), 60)` |
| slot b seed 7 | 过 | 0.21 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.24 | 0.08 | 0.19 | 0.02 | 0.11 | 0.12 | `cross_regbeta(sub(log(day_sum(Volume)), LogFloatShares), ts_mean(day_centroid(Volume), 5), 120)` |
| slot b seed 8 | 过 | 0.41 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.30 | 0.40 | 0.07 | 0.00 | 0.41 | 0.22 | `cross_corr(day_sum(Volume), ts_mean(day_gini(Volume), 5), 120)` |
| slot b seed 9 | 过 | 0.26 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.27 | 0.07 | 0.18 | 0.01 | 0.10 | 0.19 | `cross_corr(day_sum(Volume), ts_mean(day_centroid(Volume), 5), 241)` |
| slot b seed 10 | 过 | 0.44 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.34 | 0.46 | 0.08 | 0.01 | 0.48 | 0.28 | `cross_regbeta(day_sum(Volume), ts_mean(day_gini(Amt), 5), 120)` |
| slot b seed 11 | 过 | 0.49 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.32 | 0.73 | 0.02 | 0.02 | 0.72 | 0.68 | `cross_regbeta(day_sum(Volume), day_zero_ratio(Volume), 120)` |
| slot b seed 12 | 过 | 0.45 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60)` | 0.30 | 0.43 | 0.05 | 0.05 | 0.42 | 0.25 | `cross_regbeta(day_gini(Volume), ts_mean(day_centroid(Volume), 5), 120)` |
| R 1 variant 1 | 过 | 0.60 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.59 | 0.05 | 0.05 | 0.01 | 0.07 | 0.15 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120)` |
| R 1 variant 2 | 过 | 0.41 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.38 | 0.01 | 0.05 | 0.01 | 0.03 | 0.24 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 241)` |
| R 1 variant 3 | 过 | 0.51 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.50 | 0.06 | 0.06 | 0.01 | 0.09 | 0.14 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 10), 120)` |
| R 1 variant 4 | 过 | 0.58 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.58 | 0.03 | 0.04 | 0.02 | 0.05 | 0.16 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 3), 120)` |
| R 1 variant 5 | 过 | 0.81 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.81 | 0.06 | 0.08 | 0.02 | 0.08 | 0.11 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 10), 60)` |
| R 1 variant 6 | 过 | 0.38 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5),` | 0.36 | 0.04 | 0.06 | 0.00 | 0.06 | 0.15 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 20), 120)` |
