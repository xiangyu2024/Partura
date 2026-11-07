# 相关度表:种子 906,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 31 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.51 | `cs_first_high20(cs_last_low40(day_centroid(Amt), LogFloatCap` | 0.88 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.18 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.09 | 0.18 | 0.15 | 0.13 | 0.20 | 0.06 | `cross_corr(day_centroid(Amt), div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| slot a seed 2 | 过 | 0.23 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.10 | 0.24 | 0.23 | 0.17 | 0.27 | 0.03 | `cross_corr(day_centroid(Amt), div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1)), 60)` |
| slot a seed 3 | 过 | 0.23 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.20 | 0.14 | 0.15 | 0.02 | 0.18 | 0.08 | `cross_corr(day_centroid(Amt), abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), 60)` |
| slot a seed 4 | 过 | 0.34 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.30 | 0.26 | 0.25 | 0.02 | 0.28 | 0.10 | `cross_corr(day_centroid(Amt), day_es_ratio_hi(Amt), 60)` |
| slot a seed 5 | 过 | 0.23 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.19 | 0.10 | 0.16 | 0.06 | 0.13 | 0.05 | `cross_corr(day_centroid(Amt), log(day_sum(Amt)), 60)` |
| slot a seed 6 | 过 | 0.21 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.16 | 0.15 | 0.14 | 0.03 | 0.18 | 0.05 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` |
| slot a seed 7 | 过 | 0.29 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.25 | 0.22 | 0.25 | 0.01 | 0.25 | 0.14 | `cross_corr(day_centroid(Amt), day_kurt(Amt), 60)` |
| slot a seed 8 | 过 | 0.28 | `cs_first_high20(cs_first_high20(cross_mean(day_centroid(Amt)` | 0.19 | 0.22 | 0.24 | 0.02 | 0.26 | 0.11 | `cross_corr(day_centroid(Amt), day_centroid(Ret), 60)` |
| slot a seed 9 | 过 | 0.11 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.09 | 0.06 | 0.09 | 0.03 | 0.09 | 0.03 | `cross_reg_fvalue(day_centroid(Amt), div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| slot a seed 10 | 过 | 0.18 | `cs_first_high20(cs_last_low10(LogFloatCap, LogFloatCap), cro` | 0.14 | 0.05 | 0.25 | 0.02 | 0.09 | 0.17 | `cross_autocorr(day_centroid(Amt), 60, 1)` |
| slot a seed 11 | 过 | 0.22 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.27 | 0.19 | 0.32 | 0.06 | 0.10 | 0.36 | `cross_stddev(day_centroid(Amt), 60)` |
| slot a seed 12 | 过 | 0.72 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean` | 0.82 | 0.06 | 0.18 | 0.26 | 0.09 | 0.07 | `sub(cross_ema(day_centroid(Amt), 5), cross_ema(day_centroid(Amt), 60))` |
| slot a seed 13 | 过 | 0.90 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.93 | 0.33 | 0.31 | 0.13 | 0.36 | 0.20 | `cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge)` |
| slot a seed 14 | 过 | 0.32 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.26 | 0.11 | 0.09 | 0.13 | 0.14 | 0.18 | `cs_first_low20(cross_corr(day_centroid(Amt), div(day_first(Open), cross_delay(day_last(Close), 1)), 60), ListAge)` |
| slot a seed 15 | 过 | 0.15 | `cs_first_high20(cs_first_high20(cross_mean(day_centroid(Amt)` | 0.14 | 0.09 | 0.07 | 0.01 | 0.09 | 0.06 | `cross_corr(day_centroid(Amt), day_std(Ret), 60)` |
| slot b seed 1 | 过 | 0.21 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.18 | 0.17 | 0.15 | 0.02 | 0.20 | 0.06 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 2 | 过 | 0.21 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.18 | 0.18 | 0.15 | 0.02 | 0.21 | 0.06 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60)` |
| slot b seed 3 | 过 | 0.22 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.18 | 0.19 | 0.16 | 0.02 | 0.22 | 0.06 | `cross_reg_fvalue(day_first(Volume), day_es_ratio_hi(Volume), 60)` |
| slot b seed 4 | 过 | 0.26 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.22 | 0.27 | 0.18 | 0.01 | 0.29 | 0.07 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` |
| slot b seed 5 | 过 | 0.27 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.23 | 0.24 | 0.17 | 0.02 | 0.27 | 0.07 | `cross_corr(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 6 | 过 | 0.22 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.21 | 0.19 | 0.12 | 0.01 | 0.21 | 0.08 | `cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 60)` |
| slot b seed 7 | 过 | 0.23 | `cs_first_high20(cs_last_low10(LogFloatCap, LogFloatCap), cro` | 0.21 | 0.11 | 0.19 | 0.03 | 0.16 | 0.18 | `cross_corr(div(day_first(Amt), day_skew(Amt)), day_es_ratio_hi(Amt), 60)` |
| slot b seed 8 | 过 | 0.29 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.23 | 0.31 | 0.19 | 0.01 | 0.33 | 0.07 | `cross_corr(day_first(Amt), day_skew(Amt), 60)` |
| slot b seed 9 | 过 | 0.30 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.24 | 0.33 | 0.20 | 0.01 | 0.36 | 0.04 | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` |
| slot b seed 10 | 过 | 0.33 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.20 | 0.46 | 0.17 | 0.01 | 0.48 | 0.14 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` |
| slot b seed 11 | 过 | 0.27 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.22 | 0.28 | 0.19 | 0.01 | 0.31 | 0.07 | `cross_corr(day_first(Volume), day_kurt(Volume), 60)` |
| slot b seed 12 | 过 | 0.45 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.35 | 0.28 | 0.37 | 0.07 | 0.34 | 0.05 | `cross_mean(div(day_first(Volume), add(cross_delay(day_last(Volume), 1), 1000)), 60)` |
| slot b seed 13 | 过 | 0.20 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.17 | 0.20 | 0.16 | 0.01 | 0.23 | 0.06 | `cross_reg_fvalue(day_first(Amt), day_kurt(Amt), 60)` |
| slot b seed 14 | 过 | 0.17 | `cs_first_high20(cs_first_high20(cross_mean(day_centroid(Amt)` | 0.09 | 0.27 | 0.14 | 0.03 | 0.27 | 0.03 | `cross_reg_fvalue(day_first(Amt), day_std(Ret), 60)` |
| slot b seed 15 | 过 | 0.42 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.35 | 0.19 | 0.12 | 0.03 | 0.22 | 0.09 | `cs_last_low20(cross_corr(day_first(Amt), day_kurt(Amt), 60), ListAge)` |
| slot b seed 16 | 过 | 0.36 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.32 | 0.11 | 0.10 | 0.04 | 0.14 | 0.09 | `cs_last_low20(cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 60), ListAge)` |
| R 1 variant 1 | 过 | 0.95 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.94 | 0.47 | 0.28 | 0.20 | 0.47 | 0.31 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20)` |
| R 1 variant 2 | 过 | 0.89 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.86 | 0.47 | 0.32 | 0.20 | 0.48 | 0.26 | `cross_mean(div(day_sum(in_slice(Amt, 181, 240)), day_sum(Amt)), 20)` |
| R 1 variant 3 | 过 | 0.89 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.85 | 0.47 | 0.34 | 0.20 | 0.48 | 0.22 | `cross_mean(div(day_sum(in_slice(Amt, 166, 240)), day_sum(Amt)), 20)` |
| R 1 variant 4 | 过 | 0.84 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.83 | 0.36 | 0.14 | 0.17 | 0.36 | 0.45 | `cs_first_low20(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), ListAge)` |
| R 1 variant 5 | 过 | 0.83 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.82 | 0.37 | 0.18 | 0.17 | 0.37 | 0.40 | `cs_first_low20(cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20), ListAge)` |
| R 1 variant 6 | 过 | 0.87 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.83 | 0.41 | 0.22 | 0.18 | 0.41 | 0.38 | `cs_first_high20(cs_first_low20(cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20), ListAge), cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20))` |
| R 1 variant 7 | 过 | 0.92 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.90 | 0.45 | 0.15 | 0.17 | 0.44 | 0.45 | `cross_mean(div(day_sum(in_slice(Amt, 226, 240)), day_sum(Amt)), 20)` |
| R 2 variant 1 | 过 | 0.99 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.99 | 0.35 | 0.34 | 0.18 | 0.38 | 0.18 | `cs_first_high20(cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 20), ListAge), cross_mean(day_centroid(Amt), 20))` |
| R 2 variant 2 | 过 | 0.91 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.93 | 0.37 | 0.35 | 0.13 | 0.41 | 0.16 | `cs_first_high20(cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge), cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30))` |
| R 2 variant 3 | 过 | 0.92 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.94 | 0.47 | 0.35 | 0.12 | 0.49 | 0.23 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 30), ListAge), cross_mean(day_centroid(Amt), 30))` |
| R 2 variant 4 | 过 | 0.95 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt),` | 0.96 | 0.46 | 0.34 | 0.13 | 0.49 | 0.23 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 30), ListAge), cross_mean(day_centroid(Amt), 20))` |
| R 3 variant 1 | 过 | 1.00 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.99 | 0.46 | 0.43 | 0.18 | 0.49 | 0.17 | `cross_mean(sub(day_centroid(Ret), mul(day_centroid(Amt), 4)), 20)` |
| R 3 variant 2 | 过 | 0.99 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.99 | 0.47 | 0.43 | 0.18 | 0.50 | 0.17 | `cross_mean(sub(day_centroid(Ret), mul(day_centroid(Amt), 5)), 20)` |
| R 3 variant 3 | 过 | 0.99 | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt))` | 0.98 | 0.47 | 0.43 | 0.19 | 0.50 | 0.16 | `cross_mean(sub(day_centroid(Ret), mul(day_centroid(Amt), 6)), 20)` |
| R 4 variant 1 | 过 | 0.92 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean` | 0.85 | 0.13 | 0.26 | 0.23 | 0.17 | 0.05 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 120))` |
| R 4 variant 2 | 过 | 0.78 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean` | 0.60 | 0.07 | 0.19 | 0.23 | 0.10 | 0.02 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 60))` |
