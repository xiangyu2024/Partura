# 相关度表:种子 805,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.16 | 0.13 | 0.20 | 0.07 | `day_centroid(Volume)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.52 | 0.39 | 0.13 | 0.54 | 0.16 | `cross_med(day_centroid(Volume), 30)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.56 | 0.35 | 0.06 | 0.56 | 0.17 | `cross_med(day_centroid(Volume), 60)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.02 | 0.08 | 0.03 | 0.02 | `cross_zscore(day_centroid(Volume), 30)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.03 | 0.11 | 0.01 | 0.01 | `cross_madz(day_centroid(Volume), 60)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.03 | 0.19 | 0.02 | 0.04 | `sub(cross_mean(day_centroid(Volume), 5), cross_mean(day_centroid(Volume), 60))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.30 | 0.12 | 0.07 | 0.28 | `cross_stddev(day_centroid(Volume), 30)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.11 | 0.10 | 0.17 | 0.14 | `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.33 | 0.11 | 0.43 | 0.23 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 30)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.01 | 0.03 | 0.02 | 0.00 | `sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(Volume))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.02 | 0.03 | 0.04 | 0.01 | `cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(Volume)), 10)` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.11 | 0.07 | 0.10 | 0.10 | `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.15 | 0.13 | 0.19 | 0.07 | `cs_bucket_rank(day_centroid(Volume), BoardCode)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.51 | 0.36 | 0.13 | 0.53 | 0.17 | `cs_bucket_rank(cross_med(day_centroid(Volume), 30), BoardCode)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.15 | 0.13 | 0.18 | 0.07 | `cs_bucket_rank(day_centroid(Volume), ListAge)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.02 | 0.09 | 0.05 | 0.02 | `day_corr(Close, Volume)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.08 | 0.13 | 0.23 | 0.07 | `cross_mean(day_corr(Close, Volume), 30)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.11 | 0.13 | 0.28 | 0.08 | `cross_mean(day_corr(Close, Amt), 30)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.09 | 0.10 | 0.15 | 0.09 | `cross_mean(day_corr(in_rank(Close), in_rank(Volume)), 30)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.02 | 0.09 | 0.05 | 0.02 | `day_corr(in_slice(Close, 1, 237), in_slice(Volume, 1, 237))` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.09 | 0.12 | 0.25 | 0.08 | `cross_mean(day_corr(in_slice(Close, 1, 237), in_slice(Volume, 1, 237)), 30)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.03 | 0.09 | 0.04 | 0.01 | `div(day_wmean(Close, Volume), day_mean(Close))` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.14 | 0.11 | 0.09 | 0.08 | `cross_mean(div(day_wmean(Close, Volume), day_mean(Close)), 30)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.33 | 0.39 | 0.27 | 0.10 | `cross_mean(day_corr(Ret, Volume), 30)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.06 | 0.07 | 0.12 | 0.05 | `cross_mean(day_corr(in_delta(Close, 5), in_delay(Volume, 5)), 30)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.55 | 0.24 | 0.04 | 0.55 | 0.10 | `cross_stddev(day_corr(Close, Volume), 30)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.07 | 0.12 | 0.23 | 0.09 | `cs_bucket_rank(cross_mean(day_corr(Close, Volume), 30), BoardCode)` |
