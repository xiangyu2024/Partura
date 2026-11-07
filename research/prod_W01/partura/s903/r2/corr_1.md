# 相关度表:种子 903,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.98 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day` | 0.98 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.24 | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)),` | 0.14 | 0.19 | 0.32 | 0.06 | 0.10 | 0.36 | `cross_stddev(day_centroid(Amt), 60)` |
| slot a seed 2 | 过 | 0.21 | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)),` | 0.13 | 0.10 | 0.36 | 0.07 | 0.01 | 0.30 | `cs_regres(cs_rank(cross_stddev(day_centroid(Amt), 60)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| slot a seed 3 | 过 | 0.24 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.20 | 0.10 | 0.16 | 0.06 | 0.13 | 0.05 | `cross_corr(day_centroid(Amt), log(day_sum(Amt)), 60)` |
| slot a seed 4 | 过 | 0.22 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.18 | 0.12 | 0.14 | 0.01 | 0.12 | 0.09 | `cross_corr(day_centroid(Amt), day_sum(Ret), 60)` |
| slot a seed 5 | 过 | 0.21 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.11 | 0.18 | 0.15 | 0.13 | 0.20 | 0.06 | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot a seed 6 | 过 | 0.45 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day` | 0.36 | 0.06 | 0.18 | 0.26 | 0.09 | 0.07 | `sub(cross_ema(day_centroid(Amt), 5), cross_ema(day_centroid(Amt), 60))` |
| slot a seed 7 | 过 | 0.90 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day` | 0.25 | 0.01 | 0.04 | 0.11 | 0.01 | 0.01 | `cross_madz(day_centroid(Amt), 60)` |
| slot a seed 8 | 过 | 0.24 | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)),` | 0.15 | 0.22 | 0.31 | 0.06 | 0.12 | 0.36 | `sub(cross_tail_mean_q75(day_centroid(Amt), 60), cross_tail_mean_q25(day_centroid(Amt), 60))` |
| slot a seed 9 | 过 | 0.72 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.62 | 0.33 | 0.48 | 0.08 | 0.39 | 0.09 | `cross_tail_mean_q25(day_centroid(Amt), 60)` |
| slot a seed 10 | 过 | 0.24 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.11 | 0.04 | 0.34 | 0.07 | 0.04 | 0.26 | `cross_semistd_neg(day_centroid(Amt), 60)` |
| slot a seed 11 | 过 | 0.13 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.05 | 0.09 | 0.30 | 0.04 | 0.12 | 0.13 | `cross_corr(day_centroid(Amt), cs_mean(day_centroid(Amt)), 60)` |
| slot a seed 12 | 过 | 0.84 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.96 | 0.02 | 0.30 | 0.09 | 0.01 | 0.22 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 30), cross_mean(day_std(Amt), 30))` |
| slot a seed 13 | 过 | 0.91 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.88 | 0.45 | 0.43 | 0.10 | 0.49 | 0.01 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 30), cross_mean(div(day_last(Amt), day_sum(Amt)), 30))` |
| slot a seed 14 | 过 | 0.21 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.25 | 0.11 | 0.12 | 0.06 | 0.12 | 0.05 | `cs_flip_by_state(cross_mean(day_centroid(Amt), 30), day_sum(Amt))` |
| slot a seed 15 | 过 | 0.64 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.80 | 0.23 | 0.27 | 0.11 | 0.17 | 0.32 | `sub(cs_rank(cross_mean(day_centroid(Amt), 30)), cs_rank(cross_mean(day_flat_run_max(Amt), 30)))` |
| slot a seed 16 | 过 | 0.23 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.13 | 0.05 | 0.25 | 0.02 | 0.09 | 0.17 | `cross_autocorr_s1(day_centroid(Amt), 60)` |
| slot b seed 1 | 过 | 0.19 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.21 | 0.04 | 0.07 | 0.04 | 0.03 | 0.01 | `cross_mean(sub(day_centroid(mul(Amt, is_gt(Ret, 0))), day_centroid(mul(Amt, is_lt(Ret, 0)))), 30)` |
| slot b seed 2 | 过 | 0.89 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.85 | 0.43 | 0.36 | 0.12 | 0.46 | 0.12 | `cross_mean(day_centroid(mul(Amt, is_gt(Ret, 0))), 30)` |
| slot b seed 3 | 过 | 0.85 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.80 | 0.46 | 0.34 | 0.09 | 0.49 | 0.14 | `cross_mean(day_centroid(mul(Amt, is_lt(Ret, 0))), 30)` |
| slot b seed 4 | 过 | 0.98 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.98 | 0.52 | 0.42 | 0.12 | 0.55 | 0.11 | `cross_mean(day_centroid(in_slice(Amt, 1, 239)), 30)` |
| slot b seed 5 | 过 | 0.64 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.49 | 0.31 | 0.43 | 0.05 | 0.36 | 0.16 | `cross_mean(day_centroid(in_slice(Amt, 1, 120)), 30)` |
| slot b seed 6 | 过 | 0.31 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.29 | 0.30 | 0.06 | 0.13 | 0.29 | 0.43 | `cross_mean(day_centroid(in_slice(Amt, 121, 239)), 30)` |
| slot b seed 7 | 过 | 0.25 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.11 | 0.03 | 0.27 | 0.03 | 0.08 | 0.38 | `cross_mean(sub(day_centroid(in_slice(Amt, 121, 239)), day_centroid(in_slice(Amt, 1, 120))), 30)` |
| slot b seed 8 | 过 | 0.62 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.46 | 0.35 | 0.44 | 0.09 | 0.43 | 0.02 | `cross_mean(div(day_sum(in_slice(Amt, 0, 2)), day_sum(Amt)), 30)` |
| slot b seed 9 | 过 | 0.04 | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)),` | 0.11 | 0.04 | 0.16 | 0.35 | 0.06 | 0.02 | `cross_mean(sub(day_argmax(High), day_argmin(Low)), 30)` |
| slot b seed 10 | 过 | 0.22 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.30 | 0.08 | 0.06 | 0.13 | 0.05 | 0.02 | `cross_mean(day_argmax(High), 60)` |
| slot b seed 11 | 过 | 0.39 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.25 | 0.21 | 0.30 | 0.28 | 0.22 | 0.02 | `cross_mean(sub(day_sum(in_slice(Ret, 121, 240)), day_sum(in_slice(Ret, 0, 120))), 30)` |
| slot b seed 12 | 过 | 0.17 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.11 | 0.13 | 0.06 | 0.08 | 0.12 | 0.03 | `cross_mean(day_sum(in_slice(Ret, 211, 240)), 30)` |
| slot b seed 13 | 过 | 0.19 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.11 | 0.20 | 0.43 | 0.34 | 0.26 | 0.04 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 30)` |
| slot b seed 14 | 过 | 0.13 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.10 | 0.23 | 0.33 | 0.39 | 0.27 | 0.10 | `cross_mean(day_corr(Amt, Ret), 30)` |
| R 1 variant 1 | 过 | 0.88 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.98 | 0.03 | 0.31 | 0.10 | 0.05 | 0.18 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 30)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 2 | 过 | 0.92 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.98 | 0.73 | 0.43 | 0.12 | 0.76 | 0.28 | `sub(cs_rank(cross_mean(day_centroid(Amt), 30)), mul(0.4, cs_rank(cross_mean(day_std(Amt), 30))))` |
| R 1 variant 3 | 过 | 0.85 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.97 | 0.83 | 0.42 | 0.12 | 0.85 | 0.36 | `sub(cs_rank(cross_mean(day_centroid(Amt), 30)), mul(0.8, cs_rank(cross_mean(day_std(Amt), 30))))` |
| R 1 variant 4 | 过 | 0.78 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.89 | 0.02 | 0.32 | 0.17 | 0.04 | 0.15 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 5 | 过 | 0.78 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.89 | 0.04 | 0.29 | 0.04 | 0.06 | 0.19 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 45)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 6 | 过 | 0.99 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 1.00 | 0.49 | 0.42 | 0.13 | 0.52 | 0.10 | `cross_mean(sub(day_centroid(Amt), mul(0.5, day_flat_run_max(Amt))), 30)` |
| R 1 variant 7 | 过 | 0.98 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.99 | 0.32 | 0.41 | 0.13 | 0.36 | 0.01 | `cross_mean(sub(day_centroid(Amt), mul(2, day_flat_run_max(Amt))), 30)` |
| R 1 variant 8 | 过 | 0.94 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.95 | 0.45 | 0.42 | 0.10 | 0.48 | 0.06 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 40)` |
| R 1 variant 9 | 过 | 0.94 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.95 | 0.40 | 0.42 | 0.17 | 0.43 | 0.07 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 22)` |
| R 1 variant 10 | 过 | 0.94 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.93 | 0.46 | 0.43 | 0.12 | 0.49 | 0.06 | `cross_ema(sub(day_centroid(Amt), day_flat_run_max(Amt)), 20)` |
| R 2 variant 1 | 过 | 0.96 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.98 | 0.55 | 0.42 | 0.12 | 0.57 | 0.14 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), cross_mean(day_centroid(Amt), 30))` |
| R 2 variant 2 | 过 | 0.90 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.90 | 0.58 | 0.42 | 0.11 | 0.60 | 0.15 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), cross_ema(day_centroid(Amt), 20))` |
| R 2 variant 3 | 过 | 0.94 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.96 | 0.54 | 0.41 | 0.12 | 0.56 | 0.16 | `div(cross_mean(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), 30), cross_mean(day_centroid(Amt), 30))` |
| R 2 variant 4 | 过 | 0.94 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.96 | 0.54 | 0.41 | 0.12 | 0.56 | 0.16 | `div(cross_mean(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), 20), cross_mean(day_centroid(Amt), 30))` |
| R 2 variant 5 | 过 | 0.67 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.63 | 0.65 | 0.22 | 0.07 | 0.62 | 0.26 | `sub(cs_rank(cross_mean(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), 30)), cs_rank(cross_mean(day_centroid(Amt), 30)))` |
| R 2 variant 6 | 过 | 0.81 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30` | 0.79 | 0.57 | 0.38 | 0.05 | 0.58 | 0.15 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), cross_mean(day_centroid(Amt), 60))` |
