# 相关度表:种子 2072,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.37 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.35 | 0.10 | 0.17 | 0.08 | 0.12 | 0.09 | `ts_hurst(day_last(Volume), 20)` |
| slot a seed 1 | 过 | 0.77 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.85 | 0.10 | 0.15 | 0.01 | 0.11 | 0.20 | `cross_mean(ts_hurst(day_last(Volume), 20), 60)` |
| slot a seed 2 | 过 | 0.24 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.22 | 0.07 | 0.13 | 0.09 | 0.09 | 0.00 | `cross_zscore(ts_hurst(day_last(Volume), 20), 120)` |
| slot a seed 3 | 过 | 0.67 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.70 | 0.22 | 0.16 | 0.02 | 0.24 | 0.01 | `cs_bucket_zscore(cross_mean(ts_hurst(day_last(Volume), 20), 20), LogFloatCap)` |
| slot a seed 4 | 过 | 0.28 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.24 | 0.10 | 0.14 | 0.06 | 0.11 | 0.06 | `sub(ts_hurst(day_last(Volume), 20), ts_hurst(day_sum(Ret), 20))` |
| slot a seed 5 | 过 | 0.61 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.63 | 0.10 | 0.11 | 0.02 | 0.11 | 0.14 | `cross_mean(sub(ts_hurst(day_last(Volume), 20), ts_hurst(day_sum(Ret), 20)), 60)` |
| slot a seed 6 | 过 | 0.31 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.31 | 0.06 | 0.12 | 0.05 | 0.07 | 0.08 | `cs_regres(ts_hurst(day_last(Volume), 20), ts_hurst(day_sum(Amt), 20))` |
| slot a seed 7 | 过 | 0.14 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.06 | 0.09 | 0.22 | 0.57 | 0.11 | 0.02 | `mul(ts_hurst(day_last(Volume), 20), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 8 | 过 | 0.38 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.41 | 0.10 | 0.12 | 0.06 | 0.11 | 0.00 | `div(cross_mean(ts_hurst(day_last(Volume), 20), 10), cross_mean(ts_hurst(day_last(Volume), 20), 120))` |
| slot a seed 9 | 过 | 0.64 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.68 | 0.13 | 0.19 | 0.03 | 0.15 | 0.15 | `cross_ema(ts_hurst(day_last(Volume), 20), 10)` |
| slot a seed 10 | 过 | 0.24 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.22 | 0.07 | 0.14 | 0.09 | 0.09 | 0.01 | `cs_bucket_zscore(cross_zscore(ts_hurst(day_last(Volume), 20), 120), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 11 | 过 | 0.04 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.07 | 0.04 | 0.04 | 0.00 | 0.04 | 0.03 | `cross_corr(ts_hurst(day_last(Volume), 20), day_sum(Ret), 60)` |
| slot a seed 12 | 过 | 0.63 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.68 | 0.09 | 0.16 | 0.01 | 0.11 | 0.20 | `cross_mean(abs_(sub(ts_hurst(day_last(Volume), 20), 0.5)), 60)` |
| slot b seed 1 | 过 | 0.44 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.12 | 0.50 | 0.44 | 0.02 | 0.52 | 0.04 | `cross_mean(day_centroid(Volume), 60)` |
| slot b seed 2 | 过 | 0.39 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.07 | 0.78 | 0.09 | 0.08 | 0.70 | 0.63 | `cross_mean(day_gini(Volume), 60)` |
| slot b seed 3 | 过 | 0.02 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.02 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Volume), 120)` |
| slot b seed 4 | 过 | 0.43 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.41 | 0.10 | 0.26 | 0.07 | 0.14 | 0.08 | `cross_mean(sub(day_centroid(Volume), day_centroid(abs_(Ret))), 60)` |
| slot b seed 5 | 过 | 0.34 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.03 | 0.44 | 0.49 | 0.19 | 0.48 | 0.01 | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), LogFloatCap)` |
| slot b seed 6 | 过 | 0.57 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.37 | 0.75 | 0.06 | 0.09 | 0.69 | 0.69 | `cs_bucket_zscore(cross_mean(day_gini(Volume), 60), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 7 | 过 | 0.39 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.07 | 0.80 | 0.05 | 0.08 | 0.72 | 0.63 | `cs_regres(cross_mean(day_gini(Volume), 60), cross_mean(day_std(Ret), 60))` |
| slot b seed 8 | 过 | 0.43 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.12 | 0.49 | 0.44 | 0.02 | 0.52 | 0.04 | `cross_mean(day_centroid(Amt), 60)` |
| slot b seed 9 | 过 | 0.07 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.08 | 0.08 | 0.21 | 0.31 | 0.10 | 0.03 | `sub(cross_mean(day_centroid(Volume), 10), cross_mean(day_centroid(Volume), 120))` |
| slot b seed 10 | 过 | 0.40 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.14 | 0.42 | 0.27 | 0.01 | 0.42 | 0.02 | `cross_mean(div(day_gini(Volume), day_gini(Amt)), 60)` |
| slot b seed 11 | 过 | 0.23 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.20 | 0.68 | 0.06 | 0.08 | 0.61 | 0.48 | `cross_ema(sub(day_gini(Volume), day_gini(abs_(Ret))), 20)` |
| slot b seed 12 | 过 | 0.22 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.20 | 0.07 | 0.16 | 0.24 | 0.10 | 0.05 | `cross_mean(mul(day_centroid(Volume), sign(day_sum(Ret))), 60)` |
