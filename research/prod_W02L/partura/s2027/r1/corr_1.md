# 相关度表:种子 2027,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.16 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.24 | 0.03 | 0.13 | 0.06 | 0.04 | 0.04 | `day_q_stat_std(in_slice(Ret, 11, 230), 10)` |
| slot a seed 1 | 过 | 0.38 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.26 | 0.11 | 0.49 | 0.01 | 0.14 | 0.22 | `cross_ema(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230), 10)), 30)` |
| slot a seed 2 | 过 | 0.35 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.34 | 0.03 | 0.14 | 0.03 | 0.01 | 0.02 | `cross_stddev(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230), 10)), 60)` |
| slot a seed 3 | 过 | 0.39 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.40 | 0.03 | 0.10 | 0.02 | 0.06 | 0.04 | `div(cross_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), add(cross_mean(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 0.000001))` |
| slot a seed 4 | 过 | 0.56 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.53 | 0.09 | 0.23 | 0.16 | 0.11 | 0.05 | `sub(cross_ema(day_q_stat_std(in_slice(Ret, 11, 230), 10), 10), cross_ema(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60))` |
| slot a seed 5 | 过 | 0.50 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.46 | 0.07 | 0.21 | 0.15 | 0.09 | 0.03 | `cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)` |
| slot a seed 6 | 过 | 0.06 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.06 | 0.02 | 0.18 | 0.01 | 0.01 | 0.13 | `cross_corr(day_q_stat_std(in_slice(Ret, 11, 230), 10), day_std(in_slice(Ret, 11, 230)), 60)` |
| slot a seed 7 | 过 | 0.25 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.26 | 0.02 | 0.06 | 0.02 | 0.03 | 0.04 | `ts_skew(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` |
| slot a seed 8 | 过 | 0.39 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.36 | 0.09 | 0.22 | 0.10 | 0.12 | 0.04 | `cross_delta(cross_ema(day_q_stat_std(in_slice(Ret, 11, 230), 10), 20), 60)` |
| slot a seed 9 | 过 | 0.02 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.03 | 0.04 | 0.02 | 0.00 | 0.04 | 0.01 | `cross_autocorr(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60, 1)` |
| slot a seed 10 | 过 | 0.26 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.29 | 0.04 | 0.03 | 0.01 | 0.02 | 0.03 | `cross_semistd_neg(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` |
| slot a seed 11 | 过 | 0.40 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.34 | 0.06 | 0.39 | 0.02 | 0.10 | 0.21 | `cross_tail_mean_q75(day_q_stat_std(in_slice(Ret, 11, 230), 10), 120)` |
| slot a seed 12 | 过 | 0.33 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.29 | 0.09 | 0.23 | 0.15 | 0.11 | 0.04 | `sub(cross_ema(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230), 10)), 5), cross_ema(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230), 10)), 120))` |
| slot a seed 13 | 过 | 0.37 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.25 | 0.12 | 0.48 | 0.01 | 0.14 | 0.20 | `ts_decay_linear(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230), 10)), 90)` |
| slot a seed 14 | 过 | 0.02 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.10 | 0.12 | 0.35 | 0.01 | 0.12 | 0.04 | `cross_regbeta(day_std(in_slice(Ret, 11, 230)), day_q_stat_std(in_slice(Ret, 11, 230), 10), 120)` |
| slot a seed 15 | 过 | 0.40 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.42 | 0.02 | 0.01 | 0.00 | 0.02 | 0.01 | `cross_ema(cross_regres(day_std(in_slice(Ret, 11, 230)), day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)` |
| slot a seed 16 | 过 | 0.10 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.06 | 0.07 | 0.23 | 0.03 | 0.07 | 0.06 | `cross_corr(day_q_stat_std(in_slice(Ret, 11, 230), 10), day_zero_ratio(in_slice(Ret, 11, 230)), 60)` |
| slot b seed 1 | 过 | 0.10 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.06 | 0.18 | 0.10 | 0.03 | 0.19 | 0.40 | `cross_ema(day_autocorr(mul(in_slice(Ret, 11, 230), 100), 3), 40)` |
| slot b seed 2 | 过 | 0.08 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.04 | 0.17 | 0.05 | 0.02 | 0.16 | 0.23 | `cross_ema(day_autocorr(mul(in_slice(Ret, 11, 230), 100), 5), 40)` |
| slot b seed 3 | 过 | 0.15 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.07 | 0.28 | 0.05 | 0.04 | 0.27 | 0.59 | `cross_ema(add(add(day_autocorr(mul(in_slice(Ret, 11, 230), 100), 2), day_autocorr(mul(in_slice(Ret, 11, 230), 100), 3)), add(day_autocorr(mul(in_slice(Ret, 11, 230), 100), 4), day_autocorr(mul(in_slice(Ret, 11, 230), 100), 5))), 60)` |
| slot b seed 4 | 过 | 0.10 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.10 | 0.28 | 0.02 | 0.03 | 0.24 | 0.18 | `cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 230), 100), 5), day_autocorr(mul(in_slice(Ret, 11, 230), 100), 1)), 60)` |
| slot b seed 5 | 过 | 0.08 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.09 | 0.39 | 0.03 | 0.01 | 0.35 | 0.04 | `cross_ema(div(day_var(in_slice(in_sum_rolling(Ret, 5), 15, 230)), mul(5, day_var(in_slice(Ret, 15, 230)))), 40)` |
| slot b seed 6 | 过 | 0.05 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.08 | 0.43 | 0.02 | 0.01 | 0.38 | 0.05 | `cross_ema(div(day_var(in_slice(in_sum_rolling(Ret, 15), 25, 230)), mul(15, day_var(in_slice(Ret, 25, 230)))), 60)` |
| slot b seed 7 | 过 | 0.06 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.08 | 0.40 | 0.02 | 0.03 | 0.35 | 0.03 | `cross_ema(cs_rank(div(day_var(in_slice(in_sum_rolling(Ret, 5), 15, 230)), mul(5, day_var(in_slice(Ret, 15, 230))))), 60)` |
| slot b seed 8 | 过 | 0.09 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.05 | 0.13 | 0.09 | 0.02 | 0.09 | 0.32 | `cross_ema(day_autocorr(sign(in_slice(Ret, 11, 230)), 2), 60)` |
| slot b seed 9 | 过 | 0.09 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.04 | 0.02 | 0.05 | 0.03 | 0.03 | 0.26 | `cross_ema(day_autocorr(sign(in_slice(Ret, 11, 230)), 5), 60)` |
| slot b seed 10 | 过 | 0.02 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.01 | 0.01 | 0.03 | 0.01 | 0.01 | 0.03 | `cross_autocorr(day_sum(in_slice(Ret, 11, 230)), 120, 1)` |
| slot b seed 11 | 过 | 0.02 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.01 | 0.05 | 0.06 | 0.01 | 0.05 | 0.06 | `cross_corr(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 190, 230)), 120)` |
| slot b seed 12 | 过 | 0.01 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.00 | 0.06 | 0.06 | 0.03 | 0.06 | 0.10 | `cross_corr(day_sum(in_slice(Ret, 11, 120)), day_sum(in_slice(Ret, 121, 230)), 120)` |
| slot b seed 13 | 过 | 0.18 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.08 | 0.02 | 0.14 | 0.02 | 0.04 | 0.30 | `cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1)), 60)` |
| slot b seed 14 | 过 | 0.39 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.37 | 0.14 | 0.22 | 0.01 | 0.15 | 0.00 | `cross_ema(day_q_stat_std(mul(in_slice(Ret, 11, 230), 100)), 60)` |
| slot b seed 15 | 过 | 0.18 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.16 | 0.44 | 0.17 | 0.01 | 0.42 | 0.01 | `cross_ema(day_q_stat_std(abs_(mul(in_slice(Ret, 11, 230), 100))), 60)` |
| slot b seed 16 | 过 | 0.03 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.02 | 0.37 | 0.14 | 0.01 | 0.37 | 0.15 | `cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 230), 100), 3), day_autocorr(sign(in_slice(Ret, 11, 230)), 3)), 60)` |
| R 1 variant 1 | 过 | 0.58 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.59 | 0.12 | 0.34 | 0.04 | 0.16 | 0.06 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 45)` |
| R 1 variant 2 | 过 | 0.51 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.49 | 0.12 | 0.34 | 0.02 | 0.16 | 0.07 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 60)` |
| R 1 variant 3 | 过 | 0.43 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.38 | 0.11 | 0.32 | 0.01 | 0.15 | 0.08 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 90)` |
| R 1 variant 4 | 过 | 0.38 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.32 | 0.10 | 0.31 | 0.00 | 0.14 | 0.09 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 120)` |
| R 1 variant 5 | 过 | 0.37 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.37 | 0.03 | 0.10 | 0.02 | 0.01 | 0.06 | `ts_stddev(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230))), 60)` |
| R 1 variant 6 | 过 | 0.49 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | 0.48 | 0.10 | 0.24 | 0.02 | 0.14 | 0.05 | `ts_stddev(day_q_stat_std(mul(in_slice(Ret, 11, 230), 100)), 60)` |
| R 2 variant 1 | 过 | 0.58 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.58 | 0.08 | 0.33 | 0.03 | 0.12 | 0.12 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` |
| R 2 variant 2 | 过 | 0.51 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.48 | 0.07 | 0.32 | 0.02 | 0.11 | 0.14 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` |
| R 2 variant 3 | 过 | 0.43 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.38 | 0.06 | 0.31 | 0.00 | 0.10 | 0.16 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 90)` |
| R 2 variant 4 | 过 | 0.38 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.32 | 0.05 | 0.30 | 0.01 | 0.08 | 0.17 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 120)` |
| R 2 variant 5 | 过 | 0.35 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.34 | 0.03 | 0.14 | 0.03 | 0.01 | 0.02 | `ts_stddev(cs_rank(day_q_stat_std(in_slice(Ret, 11, 230), 10)), 60)` |
| R 2 variant 6 | 过 | 0.49 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` | 0.48 | 0.05 | 0.23 | 0.02 | 0.09 | 0.12 | `ts_stddev(day_q_stat_std(mul(in_slice(Ret, 11, 230), 100), 10), 60)` |
| R 3 variant 1 | 过 | 0.59 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.50 | 0.02 | 0.31 | 0.02 | 0.07 | 0.22 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 45)` |
| R 3 variant 2 | 过 | 0.52 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.42 | 0.01 | 0.31 | 0.01 | 0.05 | 0.24 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 60)` |
| R 3 variant 3 | 过 | 0.45 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.33 | 0.01 | 0.29 | 0.01 | 0.03 | 0.27 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 90)` |
| R 3 variant 4 | 过 | 0.40 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` | 0.28 | 0.02 | 0.28 | 0.01 | 0.01 | 0.29 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 120)` |
