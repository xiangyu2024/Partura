# 相关度表:种子 907,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.07 | 0.08 | 0.27 | 0.02 | `sub(LogFloatCap, LogFloatShares)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.07 | 0.03 | 0.26 | 0.03 | `cross_mean(div(day_sum(Amt), day_sum(Volume)), 20)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.01 | 0.01 | 0.16 | 0.45 | `div(day_last(Close), div(FloatCap, FloatShares))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.01 | 0.01 | 0.16 | 0.45 | `cross_mean(div(day_wmean(Vwap, Volume), div(day_sum(Amt), day_sum(Volume))), 20)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.46 | 0.01 | 0.04 | 0.42 | 0.42 | `cross_mean(day_last(Close), 20)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.04 | 0.04 | 0.06 | 0.26 | `sub(cs_rank(div(day_last(Close), div(FloatCap, FloatShares))), cs_rank(sub(LogFloatCap, LogFloatShares)))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.08 | 0.02 | 0.03 | 0.41 | `sub(LogFloatCap, LogTotalCap)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.06 | 0.09 | 0.22 | 0.00 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.04 | 0.03 | 0.07 | 0.01 | `cs_bucket_rank(div(day_last(Close), div(FloatCap, FloatShares)), LogFloatCap)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.05 | 0.02 | 0.09 | 0.49 | `add(cs_rank(sub(LogFloatCap, LogTotalCap)), cs_rank(div(day_last(Close), div(FloatCap, FloatShares))))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.06 | 0.01 | 0.25 | 0.01 | `cs_bucket_rank(sub(LogFloatCap, LogTotalCap), LogFloatCap)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.54 | 0.42 | 0.13 | 0.56 | 0.14 | `cross_mean(day_centroid(Volume), 30)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.83 | 0.05 | 0.02 | 0.74 | 0.53 | `cross_mean(day_gini(Volume), 30)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.31 | 0.37 | 0.08 | 0.39 | 0.02 | `cross_mean(div(day_first(Volume), day_sum(Volume)), 30)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.46 | 0.16 | 0.05 | 0.41 | 0.02 | `cross_mean(day_distinct_ratio(Close), 30)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.08 | 0.13 | 0.23 | 0.07 | `cross_mean(day_corr(Close, Volume), 30)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.20 | 0.08 | 0.44 | 0.00 | `cross_mean(day_corr(Volume, abs_(Ret)), 30)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.23 | 0.43 | 0.16 | 0.25 | `cross_mean(day_signed_ratio(Ret, Amt), 30)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.14 | 0.11 | 0.09 | 0.08 | `cross_mean(sub(div(day_wmean(Close, Volume), day_mean(Close)), 1), 30)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.24 | 0.18 | 0.17 | 0.24 | `cross_mean(day_skew(Ret), 30)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.52 | 0.17 | 0.06 | 0.40 | 0.32 | `cross_mean(day_es_ratio_hi(Volume), 30)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.08 | 0.24 | 0.00 | 0.04 | `sub(cross_mean(day_centroid(Volume), 10), cross_mean(day_centroid(Volume), 60))` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.40 | 0.12 | 0.16 | 0.33 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_gini(Volume), 30)))` |
