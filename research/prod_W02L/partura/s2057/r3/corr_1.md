# 相关度表:种子 2057,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.24 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.15 | 0.02 | 0.22 | 0.13 | 0.06 | 0.14 | `ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10)` |
| slot a seed 1 | 过 | 0.30 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.11 | 0.04 | 0.27 | 0.11 | 0.06 | 0.19 | `cs_bucket_demean(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), LimitWidth)` |
| slot a seed 2 | 过 | 0.21 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.14 | 0.11 | 0.20 | 0.13 | 0.14 | 0.02 | `cs_bucket_rank(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), LogTotalCap)` |
| slot a seed 3 | 过 | 0.23 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.14 | 0.02 | 0.21 | 0.13 | 0.06 | 0.12 | `cs_bucket_rank(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), ListAge)` |
| slot a seed 4 | 过 | 0.29 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.09 | 0.05 | 0.26 | 0.11 | 0.07 | 0.17 | `cs_bucket_demean(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), BoardCode)` |
| slot a seed 5 | 过 | 0.24 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.15 | 0.02 | 0.22 | 0.13 | 0.06 | 0.14 | `cs_robust_z(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10))` |
| slot a seed 6 | 过 | 0.33 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.15 | 0.03 | 0.28 | 0.09 | 0.07 | 0.20 | `ts_decay_linear(cs_bucket_rank(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), LimitWidth), 20)` |
| slot a seed 7 | 废品 | 0.07 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.04 | 0.04 | 0.09 | 0.13 | 0.05 | 0.02 | `ts_rank(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 120)` |
| slot a seed 8 | 过 | 0.28 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.25 | 0.09 | 0.15 | 0.06 | 0.12 | 0.07 | `ts_corr(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), ts_stddev(day_std(Ret), 10), 60)` |
| slot a seed 9 | 过 | 0.23 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.15 | 0.02 | 0.21 | 0.13 | 0.06 | 0.13 | `sub(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), ts_stddev(ts_stddev(ts_stddev(day_std(Ret), 10), 50), 10))` |
| slot a seed 10 | 过 | 0.32 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.26 | 0.16 | 0.27 | 0.12 | 0.21 | 0.01 | `cs_bucket_rank(add(cs_bucket_rank(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), LimitWidth), cs_bucket_rank(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), LimitWidth)), LogFloatCap)` |
| slot b seed 1 | 过 | 0.30 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.33 | 0.03 | 0.32 | 0.09 | 0.10 | 0.10 | `ts_stddev(ts_stddev(day_flat_run_max(Close), 10), 50)` |
| slot b seed 2 | 废品 | 0.46 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.53 | 0.34 | 0.06 | 0.16 | 0.26 | 0.18 | `ts_mean(day_flat_run_max(Close), 20)` |
| slot b seed 3 | 过 | 0.20 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.18 | 0.01 | 0.25 | 0.13 | 0.06 | 0.09 | `ts_stddev(ts_stddev(ts_stddev(day_flat_run_max(Close), 10), 50), 10)` |
| slot b seed 4 | 废品 | 0.26 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.14 | 0.13 | 0.24 | 0.29 | 0.16 | 0.02 | `ts_mean(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 20)` |
| slot b seed 5 | 过 | 0.34 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.42 | 0.05 | 0.18 | 0.15 | 0.03 | 0.00 | `ts_stddev(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 30)` |
| slot b seed 6 | 过 | 0.48 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.41 | 0.31 | 0.22 | 0.01 | 0.29 | 0.08 | `ts_stddev(ts_stddev(day_distinct_ratio(Close), 10), 50)` |
| slot b seed 7 | 过 | 0.38 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.27 | 0.85 | 0.18 | 0.05 | 0.79 | 0.62 | `ts_mean(day_distinct_ratio(Vwap), 20)` |
| slot b seed 8 | 过 | 0.34 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.42 | 0.05 | 0.19 | 0.19 | 0.03 | 0.00 | `ts_stddev(day_at_max_ratio(High), 30)` |
| slot b seed 9 | 过 | 0.39 | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)),` | 0.31 | 0.03 | 0.38 | 0.08 | 0.04 | 0.26 | `cs_bucket_rank(ts_stddev(ts_stddev(day_flat_run_max(Close), 10), 50), LimitWidth)` |
| slot b seed 10 | 过 | 0.18 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.23 | 0.34 | 0.06 | 0.11 | 0.28 | 0.40 | `ts_stddev(sub(day_flat_run_max(Close), day_zero_ratio(Ret)), 30)` |
| slot b seed 11 | 废品 | 0.49 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.55 | 0.32 | 0.17 | 0.07 | 0.26 | 0.01 | `ts_mean(day_at_min_ratio(Low), 20)` |
| slot b seed 12 | 过 | 0.21 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.15 | 0.38 | 0.23 | 0.19 | 0.31 | 0.40 | `ts_stddev(day_flat_run_max(Vwap), 20)` |
| R 1 variant 1 | 过 | 0.81 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.42 | 0.28 | 0.77 | 0.33 | 0.33 | 0.12 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 8)` |
| R 1 variant 2 | 过 | 0.84 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.48 | 0.31 | 0.81 | 0.31 | 0.35 | 0.12 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 10)` |
| R 1 variant 3 | 过 | 0.87 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.51 | 0.32 | 0.82 | 0.30 | 0.36 | 0.12 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 12)` |
| R 1 variant 4 | 过 | 0.90 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.59 | 0.34 | 0.85 | 0.28 | 0.38 | 0.12 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 15)` |
| R 1 variant 5 | 过 | 0.95 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` | 0.73 | 0.36 | 0.87 | 0.22 | 0.40 | 0.13 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 20)` |
