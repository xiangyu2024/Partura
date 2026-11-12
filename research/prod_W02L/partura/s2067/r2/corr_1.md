# 相关度表:种子 2067,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.66 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.69 | 0.66 | 0.24 | 0.22 | 0.64 | 0.32 | `day_durbin_watson(Amt)` |
| slot a seed 1 | 过 | 0.41 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.09 | 0.07 | 0.17 | 0.35 | 0.09 | 0.04 | `sub(day_durbin_watson(Amt), cross_mean(day_durbin_watson(Amt), 60))` |
| slot a seed 2 | 过 | 0.39 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.08 | 0.02 | 0.10 | 0.33 | 0.03 | 0.04 | `div(sub(day_durbin_watson(Amt), cross_mean(day_durbin_watson(Amt), 40)), cross_stddev(day_durbin_watson(Amt), 40))` |
| slot a seed 3 | 过 | 0.66 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.69 | 0.48 | 0.28 | 0.21 | 0.47 | 0.03 | `cs_bucket_zscore(day_durbin_watson(Amt), LogFloatCap)` |
| slot a seed 4 | 过 | 0.39 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.08 | 0.01 | 0.10 | 0.33 | 0.03 | 0.02 | `cs_bucket_zscore(sub(day_durbin_watson(Amt), cross_mean(day_durbin_watson(Amt), 40)), LogFloatCap)` |
| slot a seed 5 | 过 | 0.10 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.12 | 0.03 | 0.01 | 0.05 | 0.03 | 0.04 | `sub(day_durbin_watson(Amt), day_durbin_watson(Volume))` |
| slot a seed 6 | 过 | 0.20 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.06 | 0.29 | 0.17 | 0.18 | 0.32 | 0.15 | `cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 30)` |
| slot a seed 7 | 过 | 0.19 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.07 | 0.07 | 0.03 | 0.11 | 0.08 | 0.05 | `mul(day_durbin_watson(Amt), sign(day_sum(Ret)))` |
| slot a seed 8 | 过 | 0.12 | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Lo` | 0.13 | 0.07 | 0.14 | 0.34 | 0.11 | 0.01 | `cross_ema(mul(day_durbin_watson(Amt), sign(day_sum(Ret))), 20)` |
| slot a seed 9 | 过 | 0.38 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.16 | 0.41 | 0.50 | 0.29 | 0.43 | 0.11 | `sub(cross_ema(day_durbin_watson(Amt), 10), cross_ema(day_durbin_watson(Amt), 60))` |
| slot a seed 10 | 过 | 0.48 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.35 | 0.49 | 0.18 | 0.16 | 0.49 | 0.22 | `sub(day_durbin_watson(Amt), day_durbin_watson(abs_(Ret)))` |
| slot a seed 11 | 过 | 0.45 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.31 | 0.83 | 0.24 | 0.00 | 0.80 | 0.35 | `cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(abs_(Ret))), 30)` |
| slot a seed 12 | 过 | 0.06 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.17 | 0.02 | 0.03 | 0.04 | 0.02 | 0.02 | `div(day_durbin_watson(Amt), day_durbin_watson(Volume))` |
| slot b seed 1 | 过 | 0.40 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.53 | 0.15 | 0.14 | 0.11 | 0.16 | 0.02 | `sub(day_corr(Amt, in_delay(Amt, 5)), day_corr(Amt, in_delay(Amt, 1)))` |
| slot b seed 2 | 过 | 0.39 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.51 | 0.44 | 0.40 | 0.13 | 0.47 | 0.01 | `cross_mean(sub(day_corr(Amt, in_delay(Amt, 5)), day_corr(Amt, in_delay(Amt, 1))), 20)` |
| slot b seed 3 | 过 | 0.36 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.24 | 0.32 | 0.15 | 0.14 | 0.33 | 0.17 | `sub(day_corr(Volume, in_delay(Volume, 5)), day_corr(abs_(Ret), in_delay(abs_(Ret), 5)))` |
| slot b seed 4 | 过 | 0.31 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.21 | 0.75 | 0.29 | 0.05 | 0.75 | 0.36 | `cross_mean(sub(day_corr(Volume, in_delay(Volume, 5)), day_corr(abs_(Ret), in_delay(abs_(Ret), 5))), 30)` |
| slot b seed 5 | 过 | 0.61 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.73 | 0.42 | 0.20 | 0.17 | 0.41 | 0.17 | `day_corr(Amt, in_delay(Amt, 10))` |
| slot b seed 6 | 过 | 0.53 | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(A` | 0.59 | 0.29 | 0.20 | 0.18 | 0.30 | 0.07 | `sub(day_corr(Amt, in_delay(Amt, 15)), day_corr(Amt, in_delay(Amt, 1)))` |
| slot b seed 7 | 过 | 0.41 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.50 | 0.49 | 0.38 | 0.03 | 0.51 | 0.01 | `cs_bucket_zscore(cross_ema(sub(day_corr(Amt, in_delay(Amt, 5)), day_corr(Amt, in_delay(Amt, 1))), 20), LogFloatCap)` |
| slot b seed 8 | 过 | 0.36 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.24 | 0.32 | 0.15 | 0.14 | 0.33 | 0.17 | `sub(day_corr(Amt, in_delay(Amt, 5)), day_corr(abs_(Ret), in_delay(abs_(Ret), 5)))` |
| slot b seed 9 | 过 | 0.52 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.58 | 0.74 | 0.32 | 0.04 | 0.73 | 0.22 | `cross_mean(sub(day_corr(Volume, in_delay(Volume, 30)), day_corr(Volume, in_delay(Volume, 5))), 30)` |
| slot b seed 10 | 过 | 0.52 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.63 | 0.79 | 0.29 | 0.00 | 0.77 | 0.26 | `cross_mean(sub(day_corr(Amt, in_delay(Amt, 5)), day_corr(Ret, in_delay(Ret, 5))), 40)` |
| slot b seed 11 | 过 | 0.26 | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Lo` | 0.28 | 0.67 | 0.20 | 0.02 | 0.68 | 0.38 | `cross_ema(sub(day_corr(Amt, in_delay(Amt, 15)), day_corr(abs_(Ret), in_delay(abs_(Ret), 15))), 30)` |
| R 1 variant 1 | 过 | 0.64 | `ts_var(day_q_stat_std(abs_(High)), 20)` | 0.80 | 0.16 | 0.06 | 0.06 | 0.12 | 0.10 | `ts_var(day_q_stat_std(abs_(Low)), 40)` |
| R 1 variant 2 | 过 | 0.53 | `ts_var(day_q_stat_std(abs_(High)), 20)` | 0.69 | 0.18 | 0.08 | 0.05 | 0.14 | 0.12 | `ts_var(day_q_stat_std(abs_(Low)), 60)` |
| R 1 variant 3 | 过 | 0.57 | `ts_var(day_q_stat_std(abs_(High)), 20)` | 0.74 | 0.19 | 0.07 | 0.04 | 0.15 | 0.15 | `ts_var(day_q_stat_std(abs_(High)), 60)` |
| R 1 variant 4 | 过 | 0.74 | `ts_var(day_q_stat_std(abs_(High)), 20)` | 0.86 | 0.14 | 0.05 | 0.07 | 0.11 | 0.09 | `ts_var(day_q_stat_std(abs_(Low)), 30)` |
| R 1 variant 5 | 过 | 0.64 | `ts_var(day_q_stat_std(abs_(High)), 20)` | 0.80 | 0.16 | 0.06 | 0.06 | 0.12 | 0.10 | `ts_std(day_q_stat_std(abs_(Low)), 40)` |
| R 1 variant 6 | 过 | 0.67 | `ts_var(day_q_stat_std(abs_(High)), 20)` | 0.83 | 0.14 | 0.04 | 0.05 | 0.11 | 0.08 | `ts_var(day_q_stat_std(abs_(Close)), 40)` |
