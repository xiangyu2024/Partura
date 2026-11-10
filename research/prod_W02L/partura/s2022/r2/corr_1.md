# 相关度表:种子 2022,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.21 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.10 | 0.72 | 0.28 | 0.25 | 0.73 | 0.49 | `day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))` |
| slot a seed 1 | 过 | 0.11 | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` | 0.10 | 0.10 | 0.23 | 0.06 | 0.02 | 0.30 | `cross_mean(cs_bucket_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), day_mean(in_slice(Amt, 2, 237))), 120)` |
| slot a seed 2 | 过 | 0.11 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.10 | 0.11 | 0.20 | 0.04 | 0.04 | 0.31 | `cross_mean(cs_bucket_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), day_mean(in_slice(Amt, 2, 237))), 241)` |
| slot a seed 3 | 过 | 0.08 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.07 | 0.59 | 0.32 | 0.04 | 0.60 | 0.04 | `cross_ema(cs_bucket_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), LogFloatCap), 60)` |
| slot a seed 4 | 过 | 0.13 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.08 | 0.16 | 0.21 | 0.06 | 0.15 | 0.01 | `cross_mean(cross_regres(day_mean(in_slice(Amt, 2, 237)), day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), 120), 30)` |
| slot a seed 5 | 过 | 0.21 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.09 | 0.32 | 0.46 | 0.24 | 0.36 | 0.12 | `cross_ema(cross_zscore(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), 120), 30)` |
| slot a seed 6 | 过 | 0.04 | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` | 0.05 | 0.00 | 0.11 | 0.05 | 0.02 | 0.05 | `cross_corr(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), day_sum(Ret), 120)` |
| slot a seed 7 | 过 | 0.20 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.15 | 0.11 | 0.04 | 0.05 | 0.10 | 0.21 | `cross_corr(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), day_mean(in_slice(Amt, 2, 237)), 120)` |
| slot a seed 8 | 过 | 0.07 | `ts_pearson(mul(log(day_argmin(Low)), 1), 10)` | 0.09 | 0.23 | 0.19 | 0.05 | 0.17 | 0.37 | `cross_stddev(cs_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))), 120)` |
| slot a seed 9 | 过 | 0.15 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.12 | 0.82 | 0.07 | 0.07 | 0.80 | 0.62 | `cross_mean(cs_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))), 241)` |
| slot a seed 10 | 过 | 0.25 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.10 | 0.43 | 0.56 | 0.32 | 0.47 | 0.14 | `sub(cross_mean(cs_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))), 20), cross_mean(cs_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))), 241))` |
| slot a seed 11 | 过 | 0.15 | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` | 0.14 | 0.06 | 0.41 | 0.20 | 0.14 | 0.16 | `cross_mean(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(cross_mean(day_mean(in_slice(Amt, 2, 237)), 60), 1)), 60)` |
| slot a seed 12 | 过 | 0.11 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.06 | 0.21 | 0.14 | 0.10 | 0.17 | 0.42 | `cross_mean(sub(cs_rank(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))), cs_rank(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))))), 120)` |
| slot b seed 1 | 过 | 0.09 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.04 | 0.55 | 0.20 | 0.05 | 0.54 | 0.10 | `cross_mean(cs_rank(day_argmax(in_slice(Amt, 2, 237))), 120)` |
| slot b seed 2 | 过 | 0.05 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.07 | 0.52 | 0.13 | 0.05 | 0.50 | 0.09 | `cross_mean(cs_rank(day_argmax(in_slice(Amt, 2, 237))), 241)` |
| slot b seed 3 | 过 | 0.10 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.05 | 0.59 | 0.23 | 0.03 | 0.58 | 0.11 | `cross_ema(cs_rank(day_argmax(in_slice(Amt, 2, 237))), 60)` |
| slot b seed 4 | 过 | 0.18 | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` | 0.22 | 0.46 | 0.06 | 0.10 | 0.42 | 0.08 | `cross_mean(sub(cs_rank(day_argmax(in_slice(Amt, 2, 237))), cs_rank(day_argmin(in_slice(Low, 2, 237)))), 120)` |
| slot b seed 5 | 过 | 0.14 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.03 | 0.56 | 0.16 | 0.01 | 0.52 | 0.12 | `cross_mean(sub(cs_rank(day_argmax(in_slice(Amt, 2, 237))), cs_rank(day_argmax(in_slice(High, 2, 237)))), 120)` |
| slot b seed 6 | 过 | 0.18 | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` | 0.22 | 0.46 | 0.00 | 0.09 | 0.41 | 0.09 | `cross_mean(div(sub(day_argmax(in_slice(Amt, 2, 237)), day_argmin(in_slice(Low, 2, 237))), 235), 241)` |
| slot b seed 7 | 过 | 0.07 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.09 | 0.10 | 0.08 | 0.03 | 0.10 | 0.11 | `cross_corr(day_argmax(in_slice(Amt, 2, 237)), day_argmin(in_slice(Low, 2, 237)), 120)` |
| slot b seed 8 | 过 | 0.05 | `ts_pearson(mul(log(day_argmin(Low)), 1), 10)` | 0.03 | 0.02 | 0.04 | 0.02 | 0.01 | 0.20 | `cross_stddev(cs_rank(day_argmax(in_slice(Amt, 2, 237))), 120)` |
| slot b seed 9 | 过 | 0.10 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.03 | 0.56 | 0.12 | 0.06 | 0.52 | 0.16 | `cross_mean(sub(day_argmax(in_slice(Amt, 2, 237)), mul(day_centroid(in_slice(Amt, 2, 237)), 235)), 120)` |
| slot b seed 10 | 过 | 0.26 | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` | 0.33 | 0.03 | 0.05 | 0.19 | 0.02 | 0.09 | `cross_mean(cs_rank(sub(day_centroid(in_slice(Amt, 2, 237)), day_centroid(in_slice(Volume, 2, 237)))), 120)` |
| slot b seed 11 | 过 | 0.13 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.13 | 0.05 | 0.10 | 0.01 | 0.04 | 0.08 | `cross_corr(day_argmax(in_slice(Amt, 2, 237)), cs_mean(day_argmax(in_slice(Amt, 2, 237))), 120)` |
| slot b seed 12 | 过 | 0.05 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.07 | 0.52 | 0.13 | 0.05 | 0.50 | 0.09 | `cross_mean(cs_rank(day_argmax(in_slice(Volume, 2, 237))), 241)` |
| R 1 variant 1 | 过 | 0.78 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.81 | 0.24 | 0.26 | 0.11 | 0.26 | 0.17 | `ts_pearson(day_argmin(Low), 20)` |
| R 1 variant 2 | 过 | 0.69 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.80 | 0.22 | 0.24 | 0.13 | 0.23 | 0.16 | `ts_pearson(day_argmin(Low), 15)` |
| R 1 variant 3 | 过 | 0.85 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.88 | 0.27 | 0.27 | 0.08 | 0.28 | 0.19 | `ts_pearson(day_argmin(Low), 25)` |
| R 1 variant 4 | 过 | 0.91 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.94 | 0.28 | 0.28 | 0.05 | 0.29 | 0.20 | `ts_pearson(day_argmin(Low), 30)` |
| R 1 variant 5 | 过 | 0.85 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.88 | 0.27 | 0.27 | 0.08 | 0.28 | 0.19 | `ts_pearson(mul(day_argmin(Low), 0.5), 25)` |
| R 1 variant 6 | 过 | 0.76 | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` | 0.84 | 0.28 | 0.27 | 0.12 | 0.29 | 0.21 | `ts_pearson(pow_05(day_argmin(Low)), 20)` |
