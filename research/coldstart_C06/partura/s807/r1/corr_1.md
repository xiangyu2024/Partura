# 相关度表:种子 807,C 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.89 | 0.06 | 0.22 | 0.15 | 0.07 | 0.13 | `pow_2(day_wmean(Ret, Ret))` |
| slot a seed 1 | 过 | 0.33 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.49 | 0.18 | 0.24 | 0.21 | 0.21 | 0.23 | `cross_mean(div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret))), 20)` |
| slot a seed 2 | 过 | 0.30 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.54 | 0.15 | 0.24 | 0.21 | 0.19 | 0.22 | `cross_tail_mean_q75(div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret))), 20)` |
| slot a seed 3 | 过 | 0.32 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.26 | 0.21 | 0.12 | 0.12 | 0.21 | 0.19 | `cross_med(div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret))), 20)` |
| slot a seed 4 | 过 | 0.32 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.41 | 0.03 | 0.18 | 0.19 | 0.01 | 0.36 | `cs_bucket_rank(cross_mean(div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret))), 20), cross_mean(day_sum(Amt), 20))` |
| slot a seed 5 | 过 | 0.32 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.75 | 0.01 | 0.24 | 0.20 | 0.06 | 0.33 | `cross_mean(div(pow_2(day_wmean(Ret, Ret)), day_var(Ret)), 20)` |
| slot a seed 6 | 过 | 0.25 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.47 | 0.06 | 0.01 | 0.13 | 0.03 | 0.29 | `cs_bucket_rank(cross_mean(pow_2(day_wmean(Ret, Ret)), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 7 | 过 | 0.23 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.48 | 0.07 | 0.01 | 0.13 | 0.03 | 0.28 | `cs_bucket_rank(cross_tail_mean_q75(pow_2(day_wmean(Ret, Ret)), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 8 | 过 | 0.20 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.49 | 0.07 | 0.01 | 0.12 | 0.03 | 0.25 | `cs_bucket_rank(cross_max(pow_2(day_wmean(Ret, Ret)), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 9 | 过 | 0.30 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.18 | 0.04 | 0.01 | 0.09 | 0.04 | 0.26 | `cs_bucket_rank(cross_med(pow_2(day_wmean(Ret, Ret)), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 10 | 过 | 0.27 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.28 | 0.02 | 0.01 | 0.14 | 0.04 | 0.20 | `cs_bucket_rank(cross_quantile_q75(div(pow_2(day_wmean(Ret, Ret)), pow_2(LimitWidth)), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 11 | 过 | 0.22 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.49 | 0.06 | 0.01 | 0.14 | 0.01 | 0.23 | `cs_bucket_rank(cross_mean(div(pow_2(day_wmean(Ret, Ret)), pow_2(LimitWidth)), 20), cross_mean(day_std(Ret), 20))` |
| slot a seed 12 | 过 | 0.29 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.01 | 0.04 | 0.06 | 0.22 | 0.02 | 0.00 | `cross_zscore(cross_mean(pow_2(day_wmean(Ret, Ret)), 5), 60)` |
| slot a seed 13 | 过 | 0.36 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.01 | 0.01 | 0.02 | 0.16 | 0.00 | 0.01 | `cross_zscore(cross_mean(div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret))), 5), 60)` |
| slot b seed 1 | 过 | 0.13 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.06 | 0.26 | 0.07 | 0.05 | 0.25 | 0.32 | `cross_mean(abs_(day_signed_ratio(Ret, Amt)), 20)` |
| slot b seed 2 | 过 | 0.14 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.09 | 0.27 | 0.04 | 0.02 | 0.25 | 0.34 | `cross_tail_mean_q75(abs_(day_signed_ratio(Ret, Amt)), 20)` |
| slot b seed 3 | 过 | 0.10 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.07 | 0.28 | 0.10 | 0.05 | 0.29 | 0.26 | `day_mean(div(abs_(in_sum_rolling(mul(sign(Ret), Amt), 30)), in_sum_rolling(Amt, 30)))` |
| slot b seed 4 | 过 | 0.09 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.08 | 0.31 | 0.10 | 0.04 | 0.33 | 0.32 | `day_mean(div(abs_(in_sum_rolling(mul(sign(Ret), Amt), 15)), in_sum_rolling(Amt, 15)))` |
| slot b seed 5 | 过 | 0.09 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.08 | 0.51 | 0.19 | 0.05 | 0.53 | 0.44 | `cross_mean(day_mean(div(abs_(in_sum_rolling(mul(sign(Ret), Amt), 30)), in_sum_rolling(Amt, 30))), 20)` |
| slot b seed 6 | 过 | 0.15 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.07 | 0.02 | 0.00 | 0.01 | 0.01 | 0.18 | `cs_bucket_rank(cross_mean(abs_(day_signed_ratio(Ret, Amt)), 20), cross_mean(day_sum(Amt), 20))` |
| slot b seed 7 | 过 | 0.13 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.07 | 0.01 | 0.05 | 0.01 | 0.04 | 0.16 | `cs_bucket_rank(cross_mean(day_mean(div(abs_(in_sum_rolling(mul(sign(Ret), Amt), 30)), in_sum_rolling(Amt, 30))), 20), cross_mean(day_sum(Amt), 20))` |
| slot b seed 8 | 过 | 0.20 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.13 | 0.34 | 0.01 | 0.10 | 0.31 | 0.01 | `cross_mean(div(abs_(day_topw_mean(Ret, Amt)), day_std(Ret)), 20)` |
| slot b seed 9 | 过 | 0.15 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.05 | 0.26 | 0.01 | 0.11 | 0.24 | 0.30 | `cross_stddev(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 10 | 过 | 0.17 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.05 | 0.03 | 0.06 | 0.15 | 0.01 | 0.17 | `cs_bucket_rank(cross_stddev(day_signed_ratio(Ret, Amt), 20), cross_mean(day_sum(Amt), 20))` |
| slot b seed 11 | 过 | 0.09 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.01 | 0.01 | 0.01 | 0.03 | 0.01 | 0.01 | `cross_zscore(cross_mean(abs_(day_signed_ratio(Ret, Amt)), 5), 60)` |
| slot b seed 12 | 过 | 0.08 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.14 | 0.45 | 0.02 | 0.03 | 0.40 | 0.42 | `cross_mean(abs_(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Ret))), 20)` |
| R 1 variant 1 | 过 | 0.29 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.91 | 0.08 | 0.52 | 0.21 | 0.15 | 0.28 | `cross_max(pow_2(day_wmean(Ret, Ret)), 20)` |
| R 1 variant 2 | 过 | 0.38 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.42 | 0.19 | 0.60 | 0.23 | 0.23 | 0.30 | `cross_quantile_q75(pow_2(day_wmean(Ret, Ret)), 20)` |
| R 1 variant 3 | 过 | 0.32 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.90 | 0.11 | 0.57 | 0.23 | 0.17 | 0.30 | `cross_tail_mean_q75(pow_2(day_wmean(Ret, Ret)), 20)` |
| R 1 variant 4 | 过 | 0.38 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.35 | 0.20 | 0.55 | 0.20 | 0.23 | 0.28 | `cross_med(pow_2(day_wmean(Ret, Ret)), 20)` |
| R 1 variant 5 | 过 | 1.00 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.98 | 0.06 | 0.22 | 0.15 | 0.07 | 0.13 | `pow_1_5(pow_2(day_wmean(Ret, Ret)))` |
| R 1 variant 6 | 过 | 0.94 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.67 | 0.07 | 0.01 | 0.07 | 0.06 | 0.09 | `pow_2(pow_2(div(day_wmean(Ret, Ret), day_wmean(abs_(Ret), Ret))))` |
| R 1 variant 7 | 过 | 0.95 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.87 | 0.00 | 0.01 | 0.06 | 0.00 | 0.13 | `pow_2(pow_2(div(day_wmean(Ret, Ret), day_std(Ret))))` |
| R 1 variant 8 | 过 | 0.47 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.62 | 0.03 | 0.02 | 0.02 | 0.03 | 0.08 | `pow_2(pow_2(day_signed_ratio(Ret, Ret)))` |
| R 1 variant 9 | 过 | 0.97 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.21 | 0.00 | 0.01 | 0.11 | 0.00 | 0.11 | `cs_bucket_rank(pow_2(pow_2(day_wmean(Ret, Ret))), cross_mean(day_std(Ret), 20))` |
| R 1 variant 10 | 过 | 0.59 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.70 | 0.03 | 0.22 | 0.13 | 0.00 | 0.11 | `pow_2(pow_2(day_wmean(Ret, Amt)))` |
| R 1 variant 11 | 过 | 0.54 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | 0.38 | 0.16 | 0.24 | 0.13 | 0.16 | 0.05 | `pow_2(pow_2(day_mean(Ret)))` |
