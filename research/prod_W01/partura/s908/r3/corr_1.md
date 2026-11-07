# 相关度表:种子 908,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 19 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.97 | `sub(day_centroid(Ret), mul(day_centroid(Volume), 3))` | 0.91 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.31 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` | 0.25 | 0.18 | 0.15 | 0.13 | 0.20 | 0.06 | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot a seed 2 | 过 | 0.64 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` | 0.61 | 0.14 | 0.15 | 0.02 | 0.18 | 0.08 | `cross_corr(day_centroid(Amt), abs_(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)), 60)` |
| slot a seed 3 | 过 | 0.22 | `cross_corr(day_centroid(Amt), day_es_ratio_hi(Amt), 60)` | 0.21 | 0.11 | 0.14 | 0.01 | 0.12 | 0.09 | `cross_corr(day_centroid(Amt), sub(div(day_close(Close), day_open(Open)), 1), 60)` |
| slot a seed 4 | 过 | 0.52 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` | 0.49 | 0.10 | 0.16 | 0.06 | 0.13 | 0.05 | `cross_corr(day_centroid(Amt), log(day_sum(Amt)), 60)` |
| slot a seed 5 | 过 | 0.91 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.87 | 0.41 | 0.32 | 0.18 | 0.44 | 0.16 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_q_stat_std(Ret), 30))` |
| slot a seed 6 | 过 | 0.87 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.97 | 0.02 | 0.32 | 0.17 | 0.04 | 0.15 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| slot a seed 7 | 过 | 0.92 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.89 | 0.35 | 0.38 | 0.23 | 0.39 | 0.12 | `sub(cross_mean(day_centroid(Amt), 20), mul(0.5, cross_mean(day_centroid(Amt), 240)))` |
| slot a seed 8 | 过 | 0.73 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.79 | 0.33 | 0.31 | 0.13 | 0.36 | 0.20 | `cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge)` |
| slot a seed 9 | 过 | 0.99 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.98 | 0.47 | 0.40 | 0.19 | 0.50 | 0.14 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))` |
| slot a seed 10 | 过 | 0.97 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.97 | 0.37 | 0.43 | 0.18 | 0.41 | 0.01 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), LogTotalCap)` |
| slot a seed 11 | 过 | 0.50 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.52 | 0.06 | 0.18 | 0.26 | 0.09 | 0.07 | `sub(cross_ema(day_centroid(Amt), 5), cross_ema(day_centroid(Amt), 60))` |
| slot a seed 12 | 过 | 0.50 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` | 0.46 | 0.14 | 0.21 | 0.05 | 0.17 | 0.08 | `cross_corr(day_centroid(Amt), div(day_sum(Amt), cross_mean(day_sum(Amt), 20)), 60)` |
| slot a seed 13 | 过 | 0.28 | `cross_corr(day_centroid(Amt), day_es_ratio_hi(Amt), 60)` | 0.26 | 0.13 | 0.16 | 0.00 | 0.14 | 0.07 | `cross_corr(day_centroid(Amt), day_signed_ratio(Ret, Amt), 60)` |
| slot a seed 14 | 过 | 0.31 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` | 0.29 | 0.09 | 0.07 | 0.01 | 0.09 | 0.06 | `cross_corr(day_centroid(Amt), day_std(Ret), 60)` |
| slot a seed 15 | 过 | 0.81 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.85 | 0.37 | 0.31 | 0.17 | 0.40 | 0.26 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` |
| slot a seed 16 | 过 | 0.98 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.98 | 0.40 | 0.43 | 0.18 | 0.43 | 0.00 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), LogFloatCap)` |
| slot b seed 1 | 过 | 0.30 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` | 0.29 | 0.10 | 0.10 | 0.13 | 0.12 | 0.07 | `cross_corr(day_first(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot b seed 2 | 过 | 0.36 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 0.36 | 0.09 | 0.02 | 0.01 | 0.10 | 0.05 | `cross_corr(day_first(Amt), abs_(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)), 60)` |
| slot b seed 3 | 过 | 0.46 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 0.41 | 0.16 | 0.09 | 0.01 | 0.18 | 0.04 | `cross_corr(div(day_first(Amt), day_sum(Amt)), abs_(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)), 60)` |
| slot b seed 4 | 过 | 0.23 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` | 0.18 | 0.15 | 0.12 | 0.11 | 0.17 | 0.05 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot b seed 5 | 过 | 0.26 | `cross_corr(day_centroid(Amt), day_es_ratio_hi(Amt), 60)` | 0.18 | 0.13 | 0.23 | 0.02 | 0.15 | 0.05 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), abs_(sub(div(day_close(Close), day_open(Open)), 1)), 60)` |
| slot b seed 6 | 过 | 0.17 | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20)` | 0.12 | 0.17 | 0.14 | 0.03 | 0.17 | 0.07 | `cross_corr(day_first(Amt), day_last(Amt), 60)` |
| slot b seed 7 | 过 | 0.20 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` | 0.31 | 0.11 | 0.13 | 0.02 | 0.11 | 0.09 | `cross_corr(day_first(Amt), cross_delay(day_sum(Amt), 1), 60)` |
| slot b seed 8 | 过 | 0.20 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 0.15 | 0.28 | 0.14 | 0.03 | 0.28 | 0.02 | `cross_corr(day_first(Amt), day_std(Ret), 60)` |
| slot b seed 9 | 过 | 0.35 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` | 0.30 | 0.18 | 0.18 | 0.02 | 0.21 | 0.07 | `cross_corr(day_first(Amt), div(day_sum(Amt), cross_mean(day_sum(Amt), 20)), 60)` |
| slot b seed 10 | 过 | 0.65 | `cs_bucket_demean(cross_mean(div(day_first(Amt), day_sum(Amt)` | 0.78 | 0.09 | 0.29 | 0.03 | 0.01 | 0.30 | `cross_stddev(div(day_first(Amt), day_sum(Amt)), 60)` |
| slot b seed 11 | 过 | 0.46 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt` | 0.42 | 0.46 | 0.10 | 0.02 | 0.39 | 0.37 | `cross_stddev(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 60)` |
| slot b seed 12 | 过 | 0.79 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 0.81 | 0.19 | 0.12 | 0.01 | 0.21 | 0.08 | `cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 60)` |
| slot b seed 13 | 过 | 0.48 | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` | 0.45 | 0.20 | 0.15 | 0.03 | 0.23 | 0.05 | `cross_corr(day_first(Amt), day_sum(in_slice(Amt, 1, 30)), 60)` |
| slot b seed 14 | 废品 | 0.38 | `cross_corr(day_first(Amt), day_gini(Amt), 60)` | 0.15 | 0.78 | 0.11 | 0.00 | 0.74 | 0.49 | `cross_mean(day_flat_run_max(Amt), 30)` |
| slot b seed 15 | 废品 | 0.30 | `ts_min(day_centroid(Amt), 20)` | 0.33 | 0.37 | 0.22 | 0.07 | 0.27 | 0.22 | `cross_mean(day_flat_run_max(Close), 30)` |
| slot b seed 16 | 过 | 0.46 | `cs_first_low40(cs_bucket_zscore(cross_mean(day_centroid(Amt)` | 0.28 | 0.64 | 0.06 | 0.02 | 0.61 | 0.55 | `cs_first_low20(cross_mean(day_flat_run_max(Amt), 30), ListAge)` |
| R 1 variant 1 | 过 | 0.99 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60` | 1.00 | 0.17 | 0.15 | 0.02 | 0.20 | 0.06 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| R 1 variant 2 | 过 | 0.84 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60` | 0.89 | 0.17 | 0.15 | 0.02 | 0.20 | 0.08 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 75)` |
| R 1 variant 3 | 过 | 0.74 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60` | 0.76 | 0.16 | 0.15 | 0.01 | 0.19 | 0.09 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 90)` |
| R 1 variant 4 | 过 | 0.84 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60` | 0.89 | 0.17 | 0.16 | 0.02 | 0.20 | 0.08 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 75)` |
| R 2 variant 1 | 过 | 0.89 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 0.91 | 0.26 | 0.18 | 0.01 | 0.28 | 0.09 | `cross_corr(day_first(Amt), day_kurt(Amt), 75)` |
| R 2 variant 2 | 过 | 0.91 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 0.94 | 0.28 | 0.18 | 0.02 | 0.30 | 0.05 | `cross_corr(day_first(Amt), day_kurt(Amt), 50)` |
| R 2 variant 3 | 过 | 1.00 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` | 1.00 | 0.27 | 0.18 | 0.01 | 0.30 | 0.07 | `cross_corr(day_first(Amt), day_kurt(Volume), 60)` |
| R 3 variant 1 | 过 | 0.95 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt` | 0.98 | 0.50 | 0.28 | 0.17 | 0.50 | 0.32 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 25)` |
| R 3 variant 2 | 过 | 0.99 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt` | 0.99 | 0.47 | 0.27 | 0.19 | 0.47 | 0.33 | `cross_mean(div(day_sum(in_slice(Amt, 201, 240)), day_sum(Amt)), 20)` |
| R 3 variant 3 | 过 | 0.93 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt` | 0.93 | 0.55 | 0.28 | 0.15 | 0.54 | 0.36 | `cross_ema(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 15)` |
