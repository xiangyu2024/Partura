# 相关度表:种子 801,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.06 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.09 | 0.18 | 0.16 | 0.13 | 0.20 | 0.07 | `day_centroid(Volume)` |
| slot a seed 1 | 过 | 0.02 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.01 | 0.02 | 0.01 | 0.11 | 0.01 | 0.03 | `cross_zscore(day_centroid(Volume), 60)` |
| slot a seed 2 | 过 | 0.04 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.05 | 0.02 | 0.07 | 0.12 | 0.03 | 0.01 | `cross_madz(day_centroid(Volume), 120)` |
| slot a seed 3 | 废品 | 0.04 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.04 | 0.00 | 0.05 | 0.12 | 0.02 | 0.03 | `ts_rank(day_centroid(Volume), 120)` |
| slot a seed 4 | 过 | 0.14 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.15 | 0.48 | 0.42 | 0.20 | 0.51 | 0.13 | `cross_mean(day_centroid(Volume), 20)` |
| slot a seed 5 | 过 | 0.04 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.02 | 0.18 | 0.26 | 0.19 | 0.09 | 0.24 | `cross_stddev(day_centroid(Volume), 20)` |
| slot a seed 6 | 过 | 0.04 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.06 | 0.09 | 0.11 | 0.07 | 0.10 | 0.10 | `sub(day_centroid(Volume), day_centroid(Ret))` |
| slot a seed 7 | 过 | 0.09 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.08 | 0.24 | 0.29 | 0.10 | 0.27 | 0.22 | `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)` |
| slot a seed 8 | 过 | 0.05 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.03 | 0.18 | 0.22 | 0.12 | 0.22 | 0.07 | `cross_corr(day_centroid(Volume), day_centroid(Ret), 20)` |
| slot a seed 9 | 过 | 0.05 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.08 | 0.17 | 0.15 | 0.13 | 0.18 | 0.07 | `cs_bucket_rank(day_centroid(Volume), ListAge)` |
| slot a seed 10 | 过 | 0.13 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.15 | 0.02 | 0.33 | 0.15 | 0.02 | 0.19 | `cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(day_sum(Amt), 20))` |
| slot a seed 11 | 过 | 0.05 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.06 | 0.07 | 0.07 | 0.03 | 0.07 | 0.07 | `cross_corr(day_centroid(Volume), day_mean(Ret), 20)` |
| slot a seed 12 | 过 | 0.00 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.04 | 0.07 | 0.17 | 0.55 | 0.10 | 0.21 | `cross_mean(mul(day_centroid(Volume), day_signed_ratio(Ret, Amt)), 20)` |
| slot a seed 13 | 过 | 0.05 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.08 | 0.17 | 0.15 | 0.13 | 0.19 | 0.07 | `cs_bucket_rank(day_centroid(Volume), BoardCode)` |
| slot a seed 14 | 过 | 0.07 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.05 | 0.01 | 0.09 | 0.20 | 0.03 | 0.04 | `cross_zscore(cross_mean(day_centroid(Volume), 5), 120)` |
| slot b core | 废品 | 0.04 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.01 | 0.10 | 0.18 | nan | 0.08 | 0.20 | `ts_med(LimitWidth, 50)` |
| slot b seed 1 | 废品 | 0.03 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.03 | 0.06 | 0.02 | 0.01 | 0.06 | 0.03 | `sub(ts_med(LimitWidth, 50), cross_mean(LimitWidth, 250))` |
| slot b seed 2 | 废品 | 0.00 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.02 | 0.10 | 0.14 | 0.03 | 0.08 | 0.08 | `cross_zscore(ts_med(LimitWidth, 50), 250)` |
| slot b seed 3 | 过 | 0.02 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.01 | 0.01 | 0.04 | 0.00 | 0.00 | 0.07 | `cs_bucket_rank(cross_zscore(ts_med(LimitWidth, 50), 250), ListAge)` |
| slot b seed 4 | 过 | 0.07 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.05 | 0.00 | 0.00 | 0.01 | 0.02 | 0.15 | `cs_bucket_rank(ts_med(LimitWidth, 50), cross_mean(day_sum(Amt), 20))` |
| slot b seed 5 | 过 | 0.07 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.05 | 0.01 | 0.01 | 0.01 | 0.01 | 0.15 | `cs_bucket_rank(ts_med(LimitWidth, 50), cross_stddev(day_sum(Amt), 20))` |
| slot b seed 6 | 过 | 0.02 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.01 | 0.01 | 0.03 | 0.01 | 0.01 | 0.11 | `cs_bucket_rank(ts_med(LimitWidth, 50), BoardCode)` |
| slot b seed 7 | 废品 | 0.00 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | `cross_corr(ts_med(LimitWidth, 50), day_mean(Ret), 60)` |
| slot b seed 8 | 过 | 0.05 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.05 | 0.05 | 0.00 | 0.23 | 0.06 | 0.12 | `cs_last_low10(ts_med(LimitWidth, 50), cross_mean(day_mean(Ret), 20))` |
| slot b seed 9 | 过 | 0.01 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.03 | 0.07 | 0.16 | 0.55 | 0.09 | 0.23 | `cross_mean(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 20)` |
| slot b seed 10 | 过 | 0.00 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.04 | 0.07 | 0.19 | 0.55 | 0.09 | 0.17 | `cs_bucket_rank(cross_mean(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 20), BoardCode)` |
| slot b seed 11 | 过 | 0.02 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_d` | 0.05 | 0.25 | 0.09 | 0.02 | 0.23 | 0.00 | `cs_last_low10(ts_med(LimitWidth, 50), cross_mean(day_sum(Amt), 20))` |
