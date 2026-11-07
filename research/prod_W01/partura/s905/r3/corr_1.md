# 相关度表:种子 905,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.42 | `cs_regres(cross_mean(day_centroid(Amt), 12), LogFloatShares)` | 0.92 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.29 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.22 | 0.18 | 0.15 | 0.13 | 0.20 | 0.06 | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot a seed 2 | 过 | 0.22 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.15 | 0.16 | 0.14 | 0.16 | 0.18 | 0.06 | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 40)` |
| slot a seed 3 | 过 | 0.27 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.18 | 0.20 | 0.15 | 0.09 | 0.21 | 0.04 | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 120)` |
| slot a seed 4 | 过 | 0.46 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.38 | 0.14 | 0.15 | 0.02 | 0.18 | 0.08 | `cross_corr(day_centroid(Amt), abs_(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)), 60)` |
| slot a seed 5 | 过 | 0.25 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.18 | 0.13 | 0.10 | 0.08 | 0.15 | 0.01 | `cross_corr(day_centroid(Amt), cross_delay(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 60)` |
| slot a seed 6 | 过 | 0.37 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.35 | 0.10 | 0.13 | 0.03 | 0.12 | 0.01 | `cross_corr(day_centroid(Amt), log(div(day_sum(Amt), cross_delay(day_sum(Amt), 1))), 60)` |
| slot a seed 7 | 过 | 0.23 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.11 | 0.18 | 0.19 | 0.12 | 0.20 | 0.03 | `cross_corr(day_centroid(Amt), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 8 | 过 | 0.11 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.11 | 0.01 | 0.03 | 0.06 | 0.02 | 0.07 | `cross_corr(day_centroid(Amt), sub(div(day_open(Open), cross_delay(day_close(Close), 1)), div(day_close(Close), day_open(Open))), 60)` |
| slot a seed 9 | 过 | 0.25 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.21 | 0.13 | 0.16 | 0.00 | 0.14 | 0.07 | `cross_corr(day_centroid(Amt), day_signed_ratio(Ret, Amt), 60)` |
| slot a seed 10 | 过 | 0.32 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.26 | 0.13 | 0.20 | 0.05 | 0.15 | 0.02 | `cross_corr(day_centroid(Amt), day_wmean(Ret, Amt), 60)` |
| slot a seed 11 | 过 | 0.50 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.37 | 0.22 | 0.20 | 0.02 | 0.26 | 0.09 | `cross_corr(day_centroid(Amt), div(day_first(Amt), day_sum(Amt)), 60)` |
| slot a seed 12 | 过 | 0.13 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.10 | 0.06 | 0.10 | 0.01 | 0.03 | 0.08 | `cross_corr(sub(day_centroid(Amt), day_centroid(Volume)), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot a seed 13 | 过 | 0.43 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.36 | 0.18 | 0.20 | 0.12 | 0.21 | 0.01 | `add(cs_rank(cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)), cs_rank(cross_corr(day_centroid(Amt), log(day_sum(Amt)), 60)))` |
| slot a seed 14 | 过 | 0.25 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.19 | 0.17 | 0.13 | 0.08 | 0.19 | 0.06 | `cross_mean(cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 40), 20)` |
| slot b seed 1 | 过 | 0.47 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.36 | 0.27 | 0.18 | 0.01 | 0.29 | 0.07 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` |
| slot b seed 2 | 过 | 0.39 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.30 | 0.18 | 0.15 | 0.02 | 0.21 | 0.06 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60)` |
| slot b seed 3 | 过 | 0.41 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.35 | 0.19 | 0.12 | 0.01 | 0.21 | 0.08 | `cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 60)` |
| slot b seed 4 | 过 | 0.53 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.41 | 0.33 | 0.20 | 0.01 | 0.36 | 0.04 | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` |
| slot b seed 5 | 过 | 0.48 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.39 | 0.24 | 0.17 | 0.02 | 0.27 | 0.07 | `cross_corr(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 6 | 过 | 0.39 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.31 | 0.17 | 0.15 | 0.02 | 0.20 | 0.06 | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| slot b seed 7 | 过 | 0.48 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.37 | 0.28 | 0.19 | 0.01 | 0.31 | 0.07 | `cross_corr(day_first(Volume), day_kurt(Volume), 60)` |
| slot b seed 8 | 过 | 0.11 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.10 | 0.02 | 0.09 | 0.00 | 0.03 | 0.05 | `cross_corr(day_last(Amt), day_kurt(Amt), 60)` |
| slot b seed 9 | 过 | 0.48 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.38 | 0.21 | 0.22 | 0.01 | 0.23 | 0.10 | `sub(cross_corr(day_first(Amt), day_kurt(Amt), 60), cross_corr(day_last(Amt), day_kurt(Amt), 60))` |
| slot b seed 10 | 过 | 0.47 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.33 | 0.21 | 0.25 | 0.01 | 0.23 | 0.13 | `cross_corr(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), day_kurt(Amt), 60)` |
| slot b seed 11 | 过 | 0.23 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.20 | 0.10 | 0.10 | 0.13 | 0.12 | 0.07 | `cross_corr(day_first(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot b seed 12 | 过 | 0.22 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.17 | 0.10 | 0.12 | 0.12 | 0.12 | 0.05 | `cross_corr(div(day_first(Amt), day_sum(Amt)), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| slot b seed 13 | 过 | 0.09 | `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_rank(cross_m` | 0.14 | 0.11 | 0.13 | 0.02 | 0.11 | 0.09 | `cross_corr(day_first(Amt), cross_delay(day_sum(Amt), 1), 60)` |
| slot b seed 14 | 过 | 0.25 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.14 | 0.28 | 0.14 | 0.03 | 0.28 | 0.02 | `cross_corr(day_first(Amt), day_std(Ret), 60)` |
| slot b seed 15 | 过 | 0.07 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.04 | 0.09 | 0.04 | 0.01 | 0.09 | 0.04 | `cross_corr(day_first(Amt), day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 16 | 过 | 0.40 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.28 | 0.22 | 0.17 | 0.01 | 0.24 | 0.14 | `cross_corr(day_first(Amt), day_kurt(Amt), 120)` |
| R 1 variant 1 | 过 | 0.95 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.94 | 0.47 | 0.28 | 0.20 | 0.47 | 0.31 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20)` |
| R 1 variant 2 | 过 | 0.89 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.86 | 0.47 | 0.32 | 0.20 | 0.48 | 0.26 | `cross_mean(div(day_sum(in_slice(Amt, 181, 240)), day_sum(Amt)), 20)` |
| R 1 variant 3 | 过 | 0.88 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.88 | 0.52 | 0.28 | 0.14 | 0.52 | 0.34 | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 30)` |
| R 1 variant 4 | 过 | 0.95 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt` | 0.94 | 0.47 | 0.28 | 0.20 | 0.47 | 0.31 | `cross_mean(div(day_sum(in_slice(Volume, 196, 240)), day_sum(Volume)), 20)` |
| R 2 variant 1 | 过 | 0.97 | `cs_regres(cross_mean(day_centroid(Amt), 12), LogFloatShares)` | 1.00 | 0.43 | 0.38 | 0.21 | 0.46 | 0.12 | `cs_regres(cross_mean(day_centroid(Amt), 14), LogFloatShares)` |
| R 2 variant 2 | 过 | 0.94 | `cs_regres(cross_mean(day_centroid(Amt), 12), LogFloatShares)` | 0.99 | 0.45 | 0.40 | 0.21 | 0.47 | 0.12 | `cs_regres(cross_mean(day_centroid(Amt), 16), LogFloatShares)` |
| R 2 variant 3 | 过 | 0.92 | `cs_regres(cross_mean(day_centroid(Amt), 12), LogFloatShares)` | 0.99 | 0.45 | 0.41 | 0.21 | 0.48 | 0.12 | `cs_regres(cross_mean(day_centroid(Amt), 17), LogFloatShares)` |
| R 3 variant 1 | 过 | 0.90 | `cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_mask_top_re` | 0.95 | 0.37 | 0.15 | 0.05 | 0.36 | 0.31 | `cs_first_low20(cross_mean(sub(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), day_flat_run_max(Amt)), 30), ListAge)` |
| R 4 variant 1 | 过 | 0.99 | `sub(cross_mean(day_centroid(Amt), 20), mul(0.5, cross_mean(d` | 0.98 | 0.40 | 0.40 | 0.22 | 0.43 | 0.12 | `sub(cross_mean(day_centroid(Amt), 20), mul(0.35, cross_mean(day_centroid(Amt), 240)))` |
| R 5 variant 1 | 过 | 0.90 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.86 | 0.32 | 0.47 | 0.04 | 0.37 | 0.12 | `cross_tail_mean_q25(day_centroid(Amt), 90)` |
| R 5 variant 2 | 过 | 0.84 | `cross_tail_mean_q25(day_centroid(Amt), 60)` | 0.75 | 0.31 | 0.46 | 0.03 | 0.35 | 0.14 | `cross_tail_mean_q25(day_centroid(Amt), 120)` |
| R 6 variant 1 | 过 | 0.78 | `ts_quantile_q25(cs_mask_top_replace_mean_neg(day_centroid(Am` | 0.92 | 0.46 | 0.23 | 0.06 | 0.44 | 0.21 | `ts_quantile_q25(cs_mask_top_replace_mean_neg(day_centroid(Amt)), 40)` |
| R 7 variant 1 | 过 | 0.88 | `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_rank(cross_m` | 0.82 | 0.44 | 0.22 | 0.00 | 0.43 | 0.15 | `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_rank(cross_mean(day_centroid(Amt), 30))), 40)` |
| R 8 variant 1 | 过 | 0.28 | `sub(cross_mean(day_centroid(Amt), 20), mul(0.5, cross_mean(d` | 0.21 | 0.15 | 0.26 | 0.18 | 0.21 | 0.10 | `cross_regres(ts_argmin(day_argmin(Ret), 50), ts_stddev(day_wmean(Ret, Amt), 30), 241)` |
| R 8 variant 2 | 过 | 0.76 | `cross_regres(cross_regres(ts_argmin(day_argmin(Ret), 50), ts` | 0.82 | 0.08 | 0.20 | 0.07 | 0.13 | 0.04 | `cross_regres(cross_regres(ts_argmin(day_argmin(Ret), 80), ts_stddev(day_wmean(Ret, Amt), 30), 241), ts_stddev(day_wmean(Ret, Amt), 30), 241)` |
| R 8 variant 3 | 过 | 1.00 | `cross_regres(cross_regres(ts_argmin(day_argmin(Ret), 50), ts` | 1.00 | 0.07 | 0.19 | 0.07 | 0.12 | 0.04 | `cross_regres(cross_regres(ts_argmin(day_argmin(Ret), 50), ts_stddev(day_wmean(Ret, Volume), 30), 241), ts_stddev(day_wmean(Ret, Volume), 30), 241)` |
