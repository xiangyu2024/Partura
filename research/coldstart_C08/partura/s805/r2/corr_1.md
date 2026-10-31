# 相关度表:种子 805,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.05 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.11 | 0.02 | 0.02 | 0.13 | 0.03 | 0.02 | `day_corr(Ret, Volume)` |
| slot a seed 1 | 废品 | 0.30 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.25 | 0.27 | 0.25 | 0.20 | 0.28 | 0.14 | `cross_mean(is_gt0(day_corr(Ret, Volume)), 60)` |
| slot a seed 2 | 废品 | 0.30 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.24 | 0.29 | 0.28 | 0.20 | 0.32 | 0.11 | `cross_mean(is_lt0(day_corr(Ret, Volume)), 60)` |
| slot a seed 3 | 废品 | 0.30 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.25 | 0.29 | 0.27 | 0.20 | 0.30 | 0.12 | `sub(cross_mean(is_gt0(day_corr(Ret, Volume)), 60), cross_mean(is_lt0(day_corr(Ret, Volume)), 60))` |
| slot a seed 4 | 过 | 0.48 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.45 | 0.01 | 0.04 | 0.01 | 0.03 | 0.16 | `sub(cross_max(day_corr(Ret, Volume), 60), cross_mean(day_corr(Ret, Volume), 60))` |
| slot a seed 5 | 过 | 0.33 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.30 | 0.12 | 0.01 | 0.04 | 0.13 | 0.05 | `sub(cross_min(day_corr(Ret, Volume), 60), cross_mean(day_corr(Ret, Volume), 60))` |
| slot a seed 6 | 过 | 0.06 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.13 | 0.06 | 0.04 | 0.22 | 0.06 | 0.00 | `sub(cross_mean(day_corr(Ret, Volume), 5), cross_mean(day_corr(Ret, Volume), 60))` |
| slot a seed 7 | 过 | 0.56 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.53 | 0.20 | 0.00 | 0.01 | 0.21 | 0.11 | `cross_stddev(day_corr(Ret, Volume), 60)` |
| slot a seed 8 | 过 | 0.15 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.17 | 0.13 | 0.04 | 0.03 | 0.12 | 0.07 | `sub(day_corr(Ret, Volume), day_corr(mul(Ret, is_gt0(Ret)), Volume))` |
| slot a seed 9 | 过 | 0.17 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.22 | 0.14 | 0.07 | 0.17 | 0.14 | 0.05 | `sub(day_corr(Ret, Volume), day_corr(mul(Ret, is_lt0(Ret)), Volume))` |
| slot a seed 10 | 过 | 0.05 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.11 | 0.03 | 0.03 | 0.14 | 0.03 | 0.02 | `mul(day_corr(Ret, Volume), day_std(Ret))` |
| slot a seed 11 | 过 | 0.34 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.32 | 0.20 | 0.35 | 0.54 | 0.23 | 0.05 | `cross_mean(mul(day_corr(Ret, Volume), day_std(Ret)), 20)` |
| slot a seed 12 | 过 | 0.11 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.14 | 0.05 | 0.06 | 0.23 | 0.06 | 0.04 | `cross_mean(day_corr(Ret, Volume), 3)` |
| slot a seed 13 | 过 | 0.70 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.70 | 0.19 | 0.20 | 0.23 | 0.23 | 0.01 | `cross_max(cross_mean(day_corr(Ret, Volume), 3), 30)` |
| slot b seed 1 | 过 | 0.05 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.09 | 0.01 | 0.01 | 0.14 | 0.01 | 0.06 | `day_signed_ratio(Ret, Amt)` |
| slot b seed 2 | 过 | 0.11 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.10 | 0.08 | 0.18 | 0.56 | 0.10 | 0.22 | `cross_mean(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 3 | 过 | 0.20 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_ope` | 0.17 | 0.19 | 0.25 | 0.27 | 0.23 | 0.32 | `cross_mean(day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 4 | 过 | 0.05 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.09 | 0.01 | 0.01 | 0.14 | 0.01 | 0.06 | `day_signed_ratio(Ret, Volume)` |
| slot b seed 5 | 过 | 0.11 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), ` | 0.10 | 0.08 | 0.18 | 0.56 | 0.10 | 0.22 | `cross_mean(day_signed_ratio(Ret, Volume), 20)` |
| slot b seed 6 | 过 | 0.13 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.17 | 0.05 | 0.07 | 0.06 | 0.04 | 0.08 | `sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Volume))` |
| slot b seed 7 | 过 | 0.17 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_ope` | 0.29 | 0.26 | 0.01 | 0.11 | 0.24 | 0.30 | `cross_stddev(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 8 | 过 | 0.06 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_ope` | 0.08 | 0.08 | 0.07 | 0.22 | 0.08 | 0.00 | `sub(cross_mean(day_signed_ratio(Ret, Amt), 5), cross_mean(day_signed_ratio(Ret, Amt), 60))` |
| slot b seed 9 | 过 | 0.05 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.07 | 0.01 | 0.00 | 0.13 | 0.01 | 0.04 | `cs_bucket_rank(day_signed_ratio(Ret, Amt), BoardCode)` |
| slot b seed 10 | 过 | 0.05 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.07 | 0.01 | 0.00 | 0.13 | 0.01 | 0.04 | `cs_bucket_rank(day_signed_ratio(Ret, Amt), ListAge)` |
| slot b seed 11 | 过 | 0.03 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.22 | 0.00 | 0.00 | 0.10 | 0.00 | 0.05 | `day_signed_ratio(in_half(Ret, True), in_half(Amt, True))` |
| slot b seed 12 | 过 | 0.11 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.04 | 0.01 | 0.02 | 0.10 | 0.01 | 0.05 | `day_signed_ratio(in_half(Ret, False), in_half(Amt, False))` |
| slot b seed 13 | 过 | 0.11 | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_c` | 0.21 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | `sub(day_signed_ratio(in_half(Ret, True), in_half(Amt, True)), day_signed_ratio(in_half(Ret, False), in_half(Amt, False)))` |
| R 1 variant 1 | 过 | 0.55 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_ope` | 0.69 | 0.54 | 0.42 | 0.13 | 0.56 | 0.14 | `cross_mean(day_centroid(Volume), 30)` |
| R 1 variant 2 | 过 | 0.47 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_ope` | 0.74 | 0.45 | 0.40 | 0.23 | 0.47 | 0.13 | `cross_mean(day_centroid(Volume), 15)` |
| R 1 variant 3 | 过 | 0.48 | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_ope` | 0.62 | 0.56 | 0.39 | 0.06 | 0.57 | 0.14 | `cross_mean(day_centroid(Volume), 60)` |
