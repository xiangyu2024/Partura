# 相关度表:种子 805,C 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.16 | 0.13 | 0.20 | 0.07 | `day_centroid(Volume)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.05 | 0.09 | 0.06 | 0.01 | `cross_mean(cross_zscore(day_centroid(Volume), 20), 5)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.17 | 0.25 | 0.05 | 0.01 | `cross_ema(cross_madz(day_centroid(Volume), 60), 5)` |
| slot a seed 3 | 废品 | 0.00 | `—` | 0.00 | 0.03 | 0.13 | 0.23 | 0.05 | 0.04 | `cross_rank(cross_ema(day_centroid(Volume), 3), 120)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.10 | 0.24 | 0.03 | 0.05 | `sub(cross_ema(day_centroid(Volume), 3), cross_ema(day_centroid(Volume), 40))` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.44 | 0.17 | 0.47 | 0.00 | `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), LogFloatCap)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.35 | 0.17 | 0.05 | 0.19 | `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.04 | 0.09 | 0.06 | 0.00 | `cs_bucket_zscore(cross_mean(cross_zscore(day_centroid(Volume), 20), 5), LogFloatCap)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.37 | 0.14 | 0.26 | 0.06 | `cs_last_high10(cross_ema(day_centroid(Volume), 10), cross_mean(day_flat_ratio(Close), 20))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.00 | 0.22 | 0.01 | 0.04 | `cs_bucket_rank(cross_zscore(cross_ema(day_centroid(Volume), 5), 60), cross_mean(day_std(Ret), 20))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.09 | 0.03 | 0.09 | 0.07 | `cross_corr(day_centroid(Volume), day_signed_ratio(Ret, Amt), 20)` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.09 | 0.06 | 0.10 | 0.05 | `cross_mean(mul(cross_zscore(day_centroid(Volume), 20), day_signed_ratio(Ret, Amt)), 10)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.01 | 0.07 | 0.02 | 0.01 | `cross_mean(mul(cross_zscore(day_centroid(Volume), 20), cs_rank(cross_zscore(day_sum(Volume), 20))), 5)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.12 | 0.08 | 0.12 | 0.05 | `cs_flip_by_state(cross_ema(day_centroid(Volume), 10), day_sum(Amt))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.01 | `cross_mean(mul(cross_zscore(day_centroid(Volume), 20), day_last(Ret)), 5)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.03 | 0.01 | 0.01 | 0.00 | `cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), 10)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.05 | 0.04 | 0.02 | 0.00 | `cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), 20)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.04 | 0.01 | 0.01 | 0.00 | `cross_ema(sub(day_centroid(mul(Amt, is_gt0(Ret))), day_centroid(mul(Amt, is_lt0(Ret)))), 5)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.03 | 0.01 | 0.01 | 0.00 | `cross_mean(sub(day_centroid(mul(mul(Volume, is_gt0(Ret)), is_gt0(in_index(Volume)))), day_centroid(mul(mul(Volume, is_lt0(Ret)), is_gt0(in_index(Volume))))), 10)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.06 | 0.08 | 0.01 | 0.01 | `cross_mean(sub(day_signed_ratio(Ret, mul(Volume, in_index(Volume))), day_signed_ratio(Ret, Volume)), 10)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.07 | 0.07 | 0.02 | 0.00 | `cross_ema(sub(day_signed_ratio(Ret, mul(Volume, in_index(Volume))), day_signed_ratio(Ret, mul(Volume, sub(1, in_index(Volume))))), 5)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.10 | 0.12 | 0.04 | 0.01 | `cross_mean(sub(day_signed_ratio(Ret, mul(Volume, is_gt0(sub(in_index(Volume), 0.75)))), day_signed_ratio(Ret, Volume)), 10)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.08 | 0.16 | 0.04 | 0.04 | `cross_mean(day_corr(in_index(Volume), mul(Volume, sign(Ret))), 20)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | `cross_zscore(cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), 5), 60)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.05 | 0.04 | 0.01 | 0.00 | `cs_bucket_rank(cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), 20), LogFloatCap)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | `cs_bucket_rank(cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), 10), cross_mean(day_std(Ret), 20))` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.06 | 0.02 | 0.16 | 0.06 | `cs_last_high10(cross_mean(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), 20), cross_mean(day_flat_ratio(Close), 20))` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.03 | 0.01 | 0.03 | 0.01 | `cross_mean(mul(sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret)))), cs_rank(cross_zscore(day_sum(Volume), 20))), 10)` |
