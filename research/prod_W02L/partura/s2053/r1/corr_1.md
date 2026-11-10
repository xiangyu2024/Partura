# 相关度表:种子 2053,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 废品 | 0.00 | `—` | 0.00 | 0.50 | 0.31 | 0.09 | 0.50 | 0.17 | `cross_mean(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), 20)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.54 | 0.31 | 0.09 | 0.53 | 0.19 | `cross_ema(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), 10)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.02 | 0.09 | 0.09 | 0.03 | `cross_zscore(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), 60)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.50 | 0.19 | 0.49 | 0.04 | `cross_mean(day_centroid(Volume), 20)` |
| slot a seed 5 | 废品 | 0.00 | `—` | 0.00 | 0.24 | 0.31 | 0.10 | 0.27 | 0.13 | `cross_mean(sub(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), day_argmax(in_local_mean(abs_(in_slice(Ret, 2, 237)), 5))), 20)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.02 | 0.04 | 0.02 | 0.01 | `cross_zscore(sub(day_centroid(Volume), day_centroid(abs_(Ret))), 40)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.19 | 0.11 | 0.02 | 0.20 | 0.00 | `cross_corr(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), day_argmax(in_local_mean(abs_(in_slice(Ret, 2, 237)), 5)), 60)` |
| slot a seed 8 | 废品 | 0.00 | `—` | 0.00 | 0.49 | 0.26 | 0.03 | 0.49 | 0.11 | `cross_mean(day_argmax(in_local_mean(in_slice(Volume, 16, 226), 5)), 30)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.30 | 0.10 | 0.45 | 0.20 | `cross_stddev(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), 20)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.28 | 0.11 | 0.24 | 0.12 | `cross_ema(sub(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), day_argmax(in_local_mean(abs_(in_slice(Ret, 2, 237)), 5))), 5)` |
| slot b seed 1 | 废品 | 0.00 | `—` | 0.00 | 0.48 | 0.35 | 0.13 | 0.49 | 0.15 | `cross_mean(sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)))), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))), 20)` |
| slot b seed 2 | 废品 | 0.00 | `—` | 0.00 | 0.48 | 0.31 | 0.09 | 0.48 | 0.16 | `cross_mean(sub(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))))), 20)` |
| slot b seed 3 | 废品 | 0.00 | `—` | 0.00 | 0.32 | 0.29 | 0.12 | 0.33 | 0.08 | `cross_mean(sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))))), 20)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.00 | 0.03 | 0.09 | 0.01 | 0.00 | `cross_zscore(sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)))), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))), 60)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.48 | 0.34 | 0.13 | 0.39 | 0.61 | `cross_ema(div(day_max(in_local_mean(in_slice(Volume, 2, 237), 5)), day_min(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))))), 10)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.38 | 0.15 | 0.16 | 0.07 | `cross_mean(div(day_min(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)))), day_max(in_local_mean(in_slice(Volume, 2, 237), 5))), 20)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.38 | 0.13 | 0.01 | 0.37 | 0.21 | `cross_stddev(sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)))), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))), 30)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.23 | 0.01 | 0.21 | 0.16 | `cross_corr(sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)))), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))), sub(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))))), 60)` |
| slot b seed 9 | 废品 | 0.00 | `—` | 0.00 | 0.38 | 0.26 | 0.14 | 0.39 | 0.14 | `cross_mean(sub(day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 2, 237), 5), day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))))), 10)` |
