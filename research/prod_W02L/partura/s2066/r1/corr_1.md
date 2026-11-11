# 相关度表:种子 2066,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.07 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.01 | 0.36 | 0.42 | 0.24 | 0.40 | 0.04 | `cross_mean(day_centroid(Amt), 10)` |
| slot a seed 2 | 过 | 0.00 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.02 | 0.04 | 0.04 | 0.06 | 0.04 | 0.00 | `cross_zscore(day_centroid(Amt), 20)` |
| slot a seed 3 | 过 | 0.03 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.01 | 0.03 | 0.30 | 0.22 | 0.02 | 0.23 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 10), cross_mean(day_mean(Amt), 20))` |
| slot a seed 4 | 过 | 0.07 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.01 | 0.40 | 0.45 | 0.23 | 0.44 | 0.01 | `cs_bucket_zscore(cross_ema(day_centroid(Volume), 5), LogFloatCap)` |
| slot a seed 5 | 过 | 0.01 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.06 | 0.03 | 0.20 | 0.12 | 0.07 | 0.05 | `sub(cross_mean(day_centroid(Amt), 5), cross_mean(day_centroid(Ret), 5))` |
| slot a seed 6 | 过 | 0.02 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.06 | 0.05 | 0.23 | 0.14 | 0.09 | 0.06 | `cross_mean(sub(day_centroid(Amt), day_centroid(Ret)), 10)` |
| slot a seed 7 | 过 | 0.00 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.01 | 0.02 | 0.04 | 0.06 | 0.02 | 0.01 | `cs_bucket_demean(cross_zscore(day_centroid(Amt), 20), cross_mean(day_gini(Amt), 20))` |
| slot a seed 8 | 过 | 0.06 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.06 | 0.41 | 0.27 | 0.08 | 0.41 | 0.01 | `cross_ema(day_centroid(Ret), 10)` |
| slot a seed 9 | 过 | 0.01 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.01 | 0.03 | 0.01 | 0.07 | 0.03 | 0.00 | `cs_bucket_rank(cross_zscore(day_centroid(Ret), 20), LogFloatCap)` |
| slot a seed 10 | 过 | 0.01 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.07 | 0.01 | 0.23 | 0.11 | 0.04 | 0.01 | `cs_bucket_rank(cross_ema(sub(day_centroid(Amt), day_centroid(Ret)), 10), cross_mean(day_mean(Amt), 20))` |
| slot b seed 1 | 过 | 0.01 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.08 | 0.03 | 0.06 | 0.46 | 0.02 | 0.11 | `cross_mean(day_signed_ratio(Ret, Amt), 10)` |
| slot b seed 2 | 过 | 0.01 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.08 | 0.02 | 0.09 | 0.51 | 0.00 | 0.14 | `cross_ema(day_signed_ratio(Ret, Amt), 5)` |
| slot b seed 3 | 过 | 0.01 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.03 | 0.01 | 0.03 | 0.01 | 0.01 | 0.02 | `cross_zscore(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 4 | 过 | 0.01 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.07 | 0.01 | 0.03 | 0.34 | 0.00 | 0.11 | `cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 5), cross_mean(day_mean(Amt), 20))` |
| slot b seed 5 | 过 | 0.01 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.03 | 0.02 | 0.03 | 0.01 | 0.02 | 0.00 | `cs_bucket_demean(cross_zscore(day_signed_ratio(Ret, Amt), 20), LogFloatCap)` |
| slot b seed 6 | 过 | 0.06 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.08 | 0.39 | 0.13 | 0.26 | 0.34 | 0.07 | `sub(cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 10)), cs_rank(cross_mean(day_pos_ratio(Ret), 10)))` |
| slot b seed 7 | 过 | 0.04 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.07 | 0.04 | 0.13 | 0.06 | 0.04 | 0.10 | `cross_mean(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Volume)), 10)` |
| slot b seed 8 | 过 | 0.01 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.09 | 0.00 | 0.17 | 0.61 | 0.02 | 0.14 | `cross_mean(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 9 | 过 | 0.02 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.09 | 0.04 | 0.15 | 0.52 | 0.02 | 0.13 | `cs_bucket_zscore(cross_ema(day_signed_ratio(Ret, Volume), 10), cross_mean(day_mean(Amt), 20))` |
| slot b seed 10 | 过 | 0.00 | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)` | 0.02 | 0.08 | 0.11 | 0.18 | 0.09 | 0.00 | `cross_zscore(cross_mean(day_signed_ratio(Ret, Amt), 5), 40)` |
| R 1 variant 1 | 过 | 0.04 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.10 | 0.30 | 0.07 | 0.09 | 0.27 | 0.03 | `pow_2(day_mean(in_corr(Ret, Close, 30)))` |
| R 1 variant 2 | 过 | 0.04 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.10 | 0.30 | 0.07 | 0.09 | 0.27 | 0.03 | `day_mean(in_corr(Ret, Close, 30))` |
| R 1 variant 3 | 过 | 0.04 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.11 | 0.29 | 0.09 | 0.10 | 0.26 | 0.00 | `day_mean(in_corr(Ret, Close, 15))` |
| R 1 variant 4 | 过 | 0.08 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.04 | 0.60 | 0.15 | 0.14 | 0.59 | 0.41 | `day_mean(in_corr(Ret, Vwap, 30))` |
| R 1 variant 5 | 过 | 0.02 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.06 | 0.04 | 0.04 | 0.00 | 0.03 | 0.01 | `pow_2(day_mean(in_corr(Ret, Amt, 30)))` |
| R 1 variant 6 | 过 | 0.02 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.04 | 0.02 | 0.03 | 0.16 | 0.02 | 0.06 | `day_mean(in_corr(Ret, Amt, 30))` |
| R 1 variant 7 | 过 | 0.01 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | 0.06 | 0.01 | 0.03 | 0.15 | 0.02 | 0.07 | `day_mean(in_corr(Ret, Volume, 15))` |
| R 1 variant 8 | 过 | 0.04 | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)` | 0.10 | 0.30 | 0.07 | 0.09 | 0.27 | 0.03 | `sigmoid(abs_(day_mean(in_corr(Ret, Close, 30))))` |
