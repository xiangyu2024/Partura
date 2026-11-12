# 相关度表:种子 2067,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.10 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.12 | 0.03 | 0.01 | 0.05 | 0.03 | 0.04 | `sub(day_durbin_watson(Amt), day_durbin_watson(Volume))` |
| slot a seed 1 | 过 | 0.23 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.09 | 0.36 | 0.17 | 0.16 | 0.39 | 0.18 | `cross_ema(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 20)` |
| slot a seed 2 | 过 | 0.07 | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice` | 0.10 | 0.04 | 0.03 | 0.03 | 0.04 | 0.00 | `cross_zscore(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 60)` |
| slot a seed 3 | 过 | 0.15 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.05 | 0.12 | 0.14 | 0.26 | 0.15 | 0.01 | `cs_bucket_zscore(cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 20), LogFloatCap)` |
| slot a seed 4 | 过 | 0.11 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.07 | 0.01 | 0.10 | 0.26 | 0.03 | 0.02 | `sub(cross_ema(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 10), cross_ema(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 60))` |
| slot a seed 5 | 过 | 0.21 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.06 | 0.23 | 0.23 | 0.28 | 0.26 | 0.09 | `div(cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 20), cross_stddev(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 20))` |
| slot a seed 6 | 过 | 0.29 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.24 | 0.34 | 0.39 | 0.07 | 0.36 | 0.00 | `cross_mean(mul(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), sign(day_sum(Ret))), 30)` |
| slot a seed 7 | 过 | 0.17 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.28 | 0.01 | 0.53 | 0.00 | 0.03 | 0.28 | `cross_tail_mean_q25(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 40)` |
| slot a seed 8 | 过 | 0.03 | `ts_var(day_q_stat_std(abs_(Low)), 60)` | 0.04 | 0.05 | 0.05 | 0.01 | 0.06 | 0.02 | `cross_semistd_neg(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 40)` |
| slot a seed 9 | 过 | 0.22 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.09 | 0.38 | 0.14 | 0.12 | 0.40 | 0.23 | `cross_ema(cs_winsor(sub(day_durbin_watson(Amt), day_durbin_watson(Volume))), 30)` |
| slot a seed 10 | 过 | 0.49 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.62 | 0.73 | 0.16 | 0.02 | 0.68 | 0.40 | `sub(cross_ema(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 20), cross_ema(day_durbin_watson(abs_(Ret)), 20))` |
| slot a seed 11 | 过 | 0.20 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.12 | 0.27 | 0.17 | 0.12 | 0.29 | 0.04 | `cs_bucket_zscore(cross_ema(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 30), LogTotalCap)` |
| slot a seed 12 | 过 | 0.21 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.07 | 0.35 | 0.19 | 0.13 | 0.37 | 0.16 | `cross_mean(cs_robust_z(sub(day_durbin_watson(Amt), day_durbin_watson(Volume))), 40)` |
| slot b seed 1 | 过 | 0.12 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.21 | 0.06 | 0.17 | 0.06 | 0.09 | 0.16 | `cross_mean(sub(day_durbin_watson(in_slice(Amt, 0, 120)), day_durbin_watson(in_slice(Amt, 121, 240))), 30)` |
| slot b seed 2 | 过 | 0.14 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.26 | 0.09 | 0.20 | 0.08 | 0.12 | 0.14 | `cross_ema(sub(day_durbin_watson(in_slice(Amt, 1, 60)), day_durbin_watson(in_slice(Amt, 181, 240))), 20)` |
| slot b seed 3 | 过 | 0.18 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.05 | 0.26 | 0.16 | 0.16 | 0.29 | 0.10 | `cross_mean(sub(day_durbin_watson(in_slice(Amt, 0, 120)), day_durbin_watson(in_slice(Volume, 0, 120))), 30)` |
| slot b seed 4 | 过 | 0.12 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.06 | 0.21 | 0.03 | 0.02 | 0.21 | 0.08 | `cross_ema(sub(day_durbin_watson(in_slice(Amt, 121, 240)), day_durbin_watson(in_slice(Volume, 121, 240))), 30)` |
| slot b seed 5 | 过 | 0.14 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.21 | 0.17 | 0.13 | 0.08 | 0.19 | 0.00 | `cs_bucket_zscore(cross_mean(sub(day_durbin_watson(in_slice(Amt, 0, 120)), day_durbin_watson(in_slice(Amt, 121, 240))), 20), LogFloatCap)` |
| slot b seed 6 | 过 | 0.33 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.31 | 0.35 | 0.34 | 0.07 | 0.37 | 0.03 | `cross_mean(sub(day_gini(Amt), day_gini(Volume)), 30)` |
| slot b seed 7 | 过 | 0.40 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.43 | 0.51 | 0.46 | 0.05 | 0.54 | 0.04 | `cross_ema(day_centroid(Amt), 30)` |
| slot b seed 8 | 过 | 0.18 | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Lo` | 0.50 | 0.09 | 0.27 | 0.09 | 0.14 | 0.07 | `cross_mean(sub(day_centroid(Amt), day_centroid(abs_(Ret))), 30)` |
| slot b seed 9 | 过 | 0.40 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.18 | 0.82 | 0.14 | 0.03 | 0.79 | 0.40 | `cross_ema(sub(day_durbin_watson(in_slice(Amt, 1, 240)), day_durbin_watson(in_slice(abs_(Ret), 1, 240))), 30)` |
| slot b seed 10 | 过 | 0.14 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.06 | 0.01 | 0.00 | 0.02 | 0.01 | 0.01 | `cross_zscore(sub(day_durbin_watson(in_slice(Amt, 0, 120)), day_durbin_watson(in_slice(Amt, 121, 240))), 60)` |
| R 1 variant 1 | 过 | 0.61 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.89 | 0.63 | 0.38 | 0.15 | 0.62 | 0.12 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 20)` |
| R 1 variant 2 | 过 | 0.57 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.82 | 0.66 | 0.31 | 0.01 | 0.64 | 0.12 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 40)` |
| R 1 variant 3 | 过 | 0.60 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.83 | 0.66 | 0.30 | 0.04 | 0.64 | 0.13 | `cross_ema(day_corr(abs_(in_delay(Ret, 5)), Amt), 20)` |
| R 1 variant 4 | 过 | 0.56 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.76 | 0.64 | 0.21 | 0.02 | 0.61 | 0.13 | `cross_ema(day_corr(abs_(in_delay(Ret, 5)), Amt), 40)` |
| R 1 variant 5 | 过 | 0.85 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.22 | 0.02 | 0.09 | 0.22 | 0.04 | 0.02 | `cross_zscore(day_corr(abs_(in_delay(Ret, 5)), Amt), 60)` |
| R 1 variant 6 | 过 | 0.57 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.85 | 0.59 | 0.37 | 0.06 | 0.58 | 0.02 | `cs_bucket_zscore(cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 30), LogFloatCap)` |
| R 2 variant 1 | 过 | 0.61 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.89 | 0.63 | 0.38 | 0.15 | 0.62 | 0.12 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Volume), 20)` |
| R 2 variant 2 | 过 | 0.57 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.82 | 0.66 | 0.31 | 0.01 | 0.64 | 0.12 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Volume), 40)` |
| R 2 variant 3 | 过 | 0.58 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.79 | 0.65 | 0.25 | 0.00 | 0.62 | 0.13 | `cross_ema(day_corr(abs_(in_delay(Ret, 5)), Volume), 30)` |
| R 2 variant 4 | 过 | 0.85 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.22 | 0.02 | 0.09 | 0.22 | 0.04 | 0.02 | `cross_zscore(day_corr(abs_(in_delay(Ret, 5)), Volume), 60)` |
