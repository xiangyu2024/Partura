# 相关度表:种子 901,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.00 | `—` | 0.00 | 0.17 | 0.11 | 0.10 | 0.18 | 0.07 | `day_argmax(Amt)` |
| slot a seed 1 | 废品 | 0.00 | `—` | 0.00 | 0.50 | 0.31 | 0.14 | 0.50 | 0.17 | `cross_mean(day_argmax(Amt), 20)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.59 | 0.31 | 0.10 | 0.58 | 0.21 | `cross_ema(day_argmax(Amt), 15)` |
| slot a seed 3 | 废品 | 0.00 | `—` | 0.00 | 0.54 | 0.31 | 0.07 | 0.54 | 0.13 | `cross_med(day_argmax(Amt), 30)` |
| slot a seed 4 | 废品 | 0.00 | `—` | 0.00 | 0.43 | 0.20 | 0.07 | 0.42 | 0.30 | `cross_tail_mean_q75(day_argmax(Amt), 40)` |
| slot a seed 5 | 废品 | 0.00 | `—` | 0.00 | 0.54 | 0.33 | 0.07 | 0.56 | 0.07 | `cross_mean(is_lt(day_argmax(Amt), 15), 30)` |
| slot a seed 6 | 废品 | 0.00 | `—` | 0.00 | 0.27 | 0.14 | 0.08 | 0.27 | 0.27 | `cross_mean(is_gt(day_argmax(Amt), 225), 30)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.02 | 0.08 | 0.02 | 0.00 | `cross_zscore(day_argmax(Amt), 60)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.10 | 0.18 | 0.03 | 0.02 | `sub(cross_mean(day_argmax(Amt), 10), cross_mean(day_argmax(Amt), 60))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.06 | 0.06 | 0.13 | 0.25 | `cross_stddev(day_argmax(Amt), 30)` |
| slot a seed 10 | 废品 | 0.00 | `—` | 0.00 | 0.48 | 0.27 | 0.30 | 0.47 | 0.14 | `cross_mean(sub(day_argmax(Amt), day_argmax(High)), 20)` |
| slot a seed 11 | 废品 | 0.00 | `—` | 0.00 | 0.00 | 0.03 | 0.08 | 0.00 | 0.01 | `cross_mean(sub(day_argmax(Amt), day_argmax(Volume)), 20)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.24 | 0.10 | 0.45 | 0.18 | `cross_mean(sub(day_argmax(Amt), mul(day_centroid(Amt), 240)), 20)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.38 | 0.33 | 0.12 | 0.39 | 0.00 | `cs_bucket_rank(cross_mean(day_argmax(Amt), 20), LogFloatCap)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.18 | 0.10 | 0.01 | 0.12 | `cs_bucket_rank(cross_mean(day_argmax(Amt), 20), cross_mean(day_std(Amt), 30))` |
| slot a seed 15 | 过 | 0.00 | `—` | 0.00 | 0.47 | 0.33 | 0.06 | 0.49 | 0.00 | `cs_bucket_rank(cross_mean(is_lt(day_argmax(Amt), 15), 30), LogFloatCap)` |
| slot a seed 16 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.16 | 0.06 | 0.01 | 0.14 | `cs_bucket_rank(cross_ema(day_argmax(Amt), 15), cross_mean(day_std(Amt), 30))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.41 | 0.19 | 0.48 | 0.10 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.23 | 0.36 | 0.14 | 0.31 | 0.06 | `cs_bucket_zscore(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), LogFloatShares)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.23 | 0.19 | 0.38 | 0.21 | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.64 | 0.32 | 0.15 | 0.63 | 0.22 | `cs_bucket_zscore(cross_mean(day_corr(in_index(Amt), Amt), 20), LogFloatShares)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.47 | 0.41 | 0.19 | 0.50 | 0.14 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap))` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.36 | 0.14 | 0.34 | 0.01 | `cs_bucket_zscore(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), sub(LogTotalCap, LogFloatCap))` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.22 | 0.18 | 0.45 | 0.34 | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), sub(LogTotalCap, LogFloatCap))` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.46 | 0.39 | 0.19 | 0.49 | 0.14 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), ListAge)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.22 | 0.18 | 0.44 | 0.34 | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), ListAge)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.38 | 0.18 | 0.47 | 0.12 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.33 | 0.15 | 0.39 | 0.00 | `cs_bucket_zscore(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.20 | 0.43 | 0.11 | 0.04 | `cs_bucket_zscore(cross_mean(sub(day_centroid(Amt), day_centroid(Volume)), 30), LogFloatShares)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.29 | 0.13 | 0.00 | 0.16 | `cs_bucket_zscore(cross_stddev(day_centroid(Amt), 30), LogFloatShares)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.77 | 0.00 | 0.02 | 0.68 | 0.38 | `cs_bucket_zscore(cross_mean(day_gini(Amt), 20), LogFloatShares)` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.43 | 0.25 | 0.28 | 0.03 | `cs_bucket_zscore(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 40), LogFloatShares)` |
| slot b seed 16 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.03 | 0.14 | 0.03 | 0.03 | `cs_bucket_zscore(cross_mean(day_signed_ratio(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), 30), LogFloatShares)` |
