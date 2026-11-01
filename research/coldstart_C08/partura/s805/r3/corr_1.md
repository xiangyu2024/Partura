# 相关度表:种子 805,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 5 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.14 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.28 | 0.02 | 0.02 | 0.13 | 0.03 | 0.02 | `day_corr(Ret, Volume)` |
| slot a seed 1 | 过 | 0.79 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.77 | 0.28 | 0.23 | 0.17 | 0.31 | 0.02 | `cross_tail_mean_q75(cross_mean(day_corr(Ret, Volume), 3), 60)` |
| slot a seed 2 | 过 | 0.61 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.59 | 0.19 | 0.32 | 0.17 | 0.21 | 0.17 | `cross_tail_mean_q25(cross_mean(day_corr(Ret, Volume), 3), 60)` |
| slot a seed 3 | 过 | 0.71 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.68 | 0.31 | 0.17 | 0.14 | 0.33 | 0.00 | `cross_tail_mean_q75(day_corr(Ret, Volume), 60)` |
| slot a seed 4 | 过 | 0.44 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.44 | 0.01 | 0.26 | 0.14 | 0.04 | 0.15 | `cross_tail_mean_q25(day_corr(Ret, Volume), 60)` |
| slot a seed 5 | 过 | 0.24 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.31 | 0.05 | 0.06 | 0.23 | 0.06 | 0.05 | `cs_bucket_rank(cross_mean(day_corr(Ret, Volume), 3), BoardCode)` |
| slot a seed 6 | 过 | 0.24 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.31 | 0.05 | 0.06 | 0.23 | 0.06 | 0.04 | `cs_bucket_rank(cross_mean(day_corr(Ret, Volume), 3), ListAge)` |
| slot a seed 7 | 过 | 0.04 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.06 | 0.00 | 0.02 | 0.05 | 0.01 | 0.01 | `cs_flip_by_state(cross_mean(day_corr(Ret, Volume), 3), day_std(Ret))` |
| slot a seed 8 | 过 | 0.02 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.05 | 0.01 | 0.01 | 0.03 | 0.01 | 0.01 | `cs_flip_by_state(cross_mean(day_corr(Ret, Volume), 3), day_sum(Volume))` |
| slot a seed 9 | 过 | 0.14 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.29 | 0.02 | 0.02 | 0.13 | 0.02 | 0.02 | `mul(day_corr(Ret, Volume), day_centroid(Volume))` |
| slot a seed 10 | 过 | 0.53 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.52 | 0.15 | 0.23 | 0.49 | 0.17 | 0.08 | `cross_mean(mul(day_corr(Ret, Volume), day_centroid(Volume)), 20)` |
| slot a seed 11 | 过 | 0.24 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.32 | 0.04 | 0.05 | 0.22 | 0.05 | 0.04 | `mul(cross_mean(day_corr(Ret, Volume), 3), day_centroid(Volume))` |
| slot b seed 1 | 过 | 0.17 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.05 | 0.01 | 0.00 | 0.01 | 0.01 | 0.03 | `mul(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False)))` |
| slot b seed 2 | 过 | 0.04 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.06 | 0.01 | 0.01 | 0.05 | 0.01 | 0.08 | `cross_mean(mul(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False))), 20)` |
| slot b seed 3 | 过 | 0.08 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.10 | 0.00 | 0.01 | 0.04 | 0.01 | 0.11 | `cross_mean(mul(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False))), 60)` |
| slot b seed 4 | 过 | 0.12 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.11 | 0.05 | 0.06 | 0.05 | 0.06 | 0.10 | `cross_corr(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False)), 60)` |
| slot b seed 5 | 过 | 0.17 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.05 | 0.02 | 0.01 | 0.01 | 0.02 | 0.03 | `mul(mul(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False))), div(day_sum(in_half(Amt, False)), day_sum(Amt)))` |
| slot b seed 6 | 过 | 0.04 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.06 | 0.01 | 0.00 | 0.05 | 0.01 | 0.06 | `cs_bucket_rank(cross_mean(mul(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False))), 20), BoardCode)` |
| slot b seed 7 | 过 | 0.04 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.06 | 0.01 | 0.00 | 0.05 | 0.01 | 0.06 | `cs_bucket_rank(cross_mean(mul(day_mean(in_half(Ret, True)), day_mean(in_half(Ret, False))), 20), ListAge)` |
| slot b seed 8 | 过 | 0.26 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.15 | 0.17 | 0.33 | 0.67 | 0.19 | 0.00 | `cross_mean(day_mean(in_half(Ret, True)), 20)` |
| slot b seed 9 | 过 | 0.06 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.24 | 0.04 | 0.04 | 0.33 | 0.03 | 0.04 | `cross_mean(day_mean(in_half(Ret, False)), 20)` |
| slot b seed 10 | 过 | 0.32 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.20 | 0.46 | 0.67 | 0.18 | 0.47 | 0.09 | `cross_mean(mul(abs_(day_mean(in_half(Ret, True))), abs_(day_mean(in_half(Ret, False)))), 20)` |
| R 1 variant 1 | 过 | 0.93 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.94 | 0.28 | 0.37 | 0.18 | 0.32 | 0.02 | `sub(cross_min(day_corr(Ret, Ret), 90), cross_mean(day_corr(Ret, Volume), 60))` |
| R 1 variant 2 | 过 | 0.88 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.87 | 0.26 | 0.36 | 0.17 | 0.30 | 0.01 | `sub(cross_min(day_corr(Ret, Ret), 120), cross_mean(day_corr(Ret, Volume), 60))` |
| R 1 variant 3 | 过 | 0.84 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.81 | 0.24 | 0.36 | 0.16 | 0.29 | 0.03 | `sub(cross_min(day_corr(Ret, Ret), 150), cross_mean(day_corr(Ret, Volume), 60))` |
| R 1 variant 4 | 过 | 0.80 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.77 | 0.23 | 0.35 | 0.15 | 0.27 | 0.04 | `sub(cross_min(day_corr(Ret, Ret), 180), cross_mean(day_corr(Ret, Volume), 60))` |
| R 1 variant 5 | 过 | 0.88 | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(R` | 0.87 | 0.26 | 0.36 | 0.17 | 0.30 | 0.01 | `sub(cross_min(day_corr(Ret, Ret), 120), cross_mean(day_corr(Ret, Amt), 60))` |
