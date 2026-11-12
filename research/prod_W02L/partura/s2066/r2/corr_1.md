# 相关度表:种子 2066,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.05 | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_` | 0.04 | 0.20 | 0.16 | 0.14 | 0.21 | 0.05 | `day_centroid(pow_3(pow_1_5(Volume)))` |
| slot a seed 1 | 过 | 0.02 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.01 | 0.02 | 0.02 | 0.07 | 0.02 | 0.00 | `cross_zscore(day_centroid(pow_3(pow_1_5(Volume))), 20)` |
| slot a seed 2 | 过 | 0.30 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.19 | 0.29 | 0.14 | 0.03 | 0.27 | 0.15 | `cross_stddev(day_centroid(pow_3(pow_1_5(Volume))), 20)` |
| slot a seed 3 | 过 | 0.06 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.03 | 0.00 | 0.12 | 0.30 | 0.02 | 0.02 | `cross_ema(cross_zscore(day_centroid(pow_3(pow_1_5(Volume))), 40), 5)` |
| slot a seed 4 | 过 | 0.12 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.07 | 0.38 | 0.35 | 0.20 | 0.39 | 0.00 | `cs_bucket_rank(cross_mean(day_centroid(pow_3(pow_1_5(Volume))), 10), LogFloatCap)` |
| slot a seed 5 | 过 | 0.02 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.01 | 0.00 | 0.01 | 0.07 | 0.00 | 0.02 | `cs_bucket_demean(cross_zscore(day_centroid(pow_3(pow_1_5(Volume))), 20), cross_mean(day_mean(Amt), 20))` |
| slot a seed 6 | 过 | 0.09 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.06 | 0.32 | 0.25 | 0.18 | 0.34 | 0.14 | `sub(cross_mean(day_centroid(pow_3(pow_1_5(Volume))), 5), cross_mean(day_centroid(Ret), 5))` |
| slot a seed 7 | 过 | 0.27 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.19 | 0.19 | 0.14 | 0.03 | 0.18 | 0.01 | `cs_bucket_zscore(cross_stddev(day_centroid(pow_3(pow_1_5(Volume))), 20), LogFloatCap)` |
| slot a seed 8 | 过 | 0.06 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.11 | 0.10 | 0.31 | 0.18 | 0.15 | 0.10 | `cross_regbeta(day_centroid(pow_3(pow_1_5(Volume))), day_centroid(Amt), 20)` |
| slot a seed 9 | 过 | 0.04 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.04 | 0.13 | 0.28 | 0.29 | 0.16 | 0.02 | `sub(cross_ema(day_centroid(pow_3(pow_1_5(Volume))), 5), cross_ema(day_centroid(pow_3(pow_1_5(Volume))), 60))` |
| slot a seed 10 | 过 | 0.03 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.01 | 0.02 | 0.00 | 0.11 | 0.02 | 0.01 | `cs_bucket_rank(cross_zscore(day_centroid(pow_3(pow_1_5(Volume))), 30), cross_mean(day_std(Ret), 20))` |
| slot b core | 过 | 0.31 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.17 | 0.11 | 0.14 | 0.07 | 0.04 | 0.23 | `day_hurst(cross_ema(pow_1_5(Volume), 60))` |
| slot b seed 1 | 过 | 0.27 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.14 | 0.11 | 0.14 | 0.05 | 0.05 | 0.24 | `cross_mean(day_hurst(cross_ema(pow_1_5(Volume), 60)), 20)` |
| slot b seed 2 | 过 | 0.16 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.13 | 0.04 | 0.02 | 0.08 | 0.05 | 0.10 | `cross_zscore(day_hurst(cross_ema(pow_1_5(Volume), 60)), 20)` |
| slot b seed 3 | 过 | 0.17 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.11 | 0.20 | 0.41 | 0.32 | 0.26 | 0.00 | `cross_stddev(day_hurst(cross_ema(pow_1_5(Volume), 60)), 20)` |
| slot b seed 4 | 过 | 0.26 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.16 | 0.05 | 0.12 | 0.07 | 0.11 | 0.00 | `cs_bucket_rank(cross_mean(day_hurst(cross_ema(pow_1_5(Volume), 60)), 10), LogFloatCap)` |
| slot b seed 5 | 过 | 0.18 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.13 | 0.02 | 0.00 | 0.07 | 0.01 | 0.07 | `cs_bucket_demean(cross_zscore(day_hurst(cross_ema(pow_1_5(Volume), 60)), 20), cross_mean(day_mean(Amt), 20))` |
| slot b seed 6 | 过 | 0.15 | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_` | 0.11 | 0.37 | 0.23 | 0.16 | 0.39 | 0.06 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(pow_1_5(Volume)))` |
| slot b seed 7 | 过 | 0.25 | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_` | 0.09 | 0.56 | 0.29 | 0.07 | 0.58 | 0.08 | `cross_ema(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(pow_1_5(Volume))), 10)` |
| slot b seed 8 | 过 | 0.23 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.14 | 0.06 | 0.12 | 0.06 | 0.11 | 0.00 | `cs_bucket_zscore(cross_ema(day_hurst(cross_ema(pow_1_5(Volume), 60)), 10), LogFloatCap)` |
| slot b seed 9 | 过 | 0.05 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.04 | 0.05 | 0.07 | 0.00 | 0.06 | 0.04 | `cross_regbeta(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_centroid(Amt), 20)` |
| slot b seed 10 | 过 | 0.14 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.12 | 0.10 | 0.02 | 0.07 | 0.12 | 0.13 | `sub(cross_ema(day_hurst(cross_ema(pow_1_5(Volume), 60)), 5), cross_ema(day_hurst(cross_ema(pow_1_5(Volume), 60)), 60))` |
