# 相关度表:种子 2055,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.15 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.23 | 0.00 | 0.10 | 0.07 | 0.01 | 0.17 | `ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20)` |
| slot a seed 2 | 过 | 0.42 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.64 | 0.01 | 0.06 | 0.10 | 0.01 | 0.04 | `ts_mean(day_kurt(in_autocorr(Ret, 3, 1)), 20)` |
| slot a seed 3 | 过 | 0.50 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.52 | 0.08 | 0.18 | 0.06 | 0.09 | 0.22 | `cross_mean(day_skew(in_autocorr(Ret, 10, 1)), 20)` |
| slot a seed 4 | 过 | 0.58 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.50 | 0.20 | 0.05 | 0.02 | 0.18 | 0.08 | `ts_quantile_q75(day_skew(in_autocorr(Ret, 30, 1)), 30)` |
| slot a seed 5 | 过 | 0.68 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.64 | 0.29 | 0.05 | 0.05 | 0.23 | 0.03 | `ts_mean(day_std(in_autocorr(Ret, 10, 1)), 20)` |
| slot a seed 6 | 过 | 0.35 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.36 | 0.07 | 0.37 | 0.05 | 0.11 | 0.01 | `ts_quantile_q75(day_kurt(in_autocorr(in_pct(Vwap, 1), 10, 1)), 20)` |
| slot a seed 7 | 过 | 0.79 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.74 | 0.34 | 0.13 | 0.01 | 0.30 | 0.06 | `ts_mean(day_pos_ratio(in_autocorr(Ret, 10, 1)), 20)` |
| slot a seed 8 | 过 | 0.07 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.08 | 0.18 | 0.08 | 0.03 | 0.18 | 0.08 | `ts_quantile_q75(day_kurt(in_autocorr(in_pct(Close, 1), 30, 1)), 30)` |
| slot a seed 9 | 过 | 0.27 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.18 | 0.24 | 0.15 | 0.09 | 0.24 | 0.02 | `cross_mean(day_kurt(in_autocorr(Ret, 30, 1)), 10)` |
| slot a seed 10 | 过 | 0.47 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.58 | 0.16 | 0.08 | 0.01 | 0.16 | 0.36 | `ts_mean(day_skew(in_autocorr(in_pct(Vwap, 1), 3, 1)), 30)` |
| slot b seed 1 | 过 | 0.27 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.43 | 0.28 | 0.01 | 0.01 | 0.24 | 0.19 | `ts_quantile_q75(day_kurt(in_corr(Ret, in_pct(Amt, 1), 15)), 20)` |
| slot b seed 2 | 过 | 0.09 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.08 | 0.08 | 0.02 | 0.15 | 0.10 | 0.12 | `ts_mean(day_skew(in_corr(Ret, in_pct(Amt, 1), 15)), 20)` |
| slot b seed 3 | 过 | 0.07 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.12 | 0.09 | 0.13 | 0.46 | 0.09 | 0.17 | `ts_mean(day_mean(in_corr(Ret, in_pct(Amt, 1), 30)), 20)` |
| slot b seed 4 | 过 | 0.54 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.52 | 0.37 | 0.01 | 0.01 | 0.31 | 0.22 | `ts_quantile_q75(day_kurt(in_corr(Ret, in_pct(Volume, 1), 5)), 30)` |
| slot b seed 5 | 过 | 0.06 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.05 | 0.02 | 0.01 | 0.08 | 0.03 | 0.07 | `cross_mean(day_skew(in_corr(Ret, in_pct(Volume, 1), 30)), 20)` |
| slot b seed 6 | 过 | 0.37 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.44 | 0.03 | 0.00 | 0.00 | 0.01 | 0.07 | `ts_quantile_q75(day_std(in_corr(Ret, in_pct(Amt, 1), 15)), 20)` |
| slot b seed 7 | 过 | 0.48 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.60 | 0.25 | 0.14 | 0.08 | 0.17 | 0.21 | `ts_mean(day_kurt(in_corr(Ret, in_pct(Amt, 1), 5)), 30)` |
| slot b seed 8 | 废品 | 0.07 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.14 | 0.15 | 0.07 | 0.33 | 0.13 | 0.21 | `ts_quantile_q75(day_pos_ratio(in_corr(Ret, in_pct(Amt, 1), 30)), 20)` |
| slot b seed 9 | 过 | 0.09 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.08 | 0.07 | 0.03 | 0.17 | 0.09 | 0.04 | `ts_mean(day_skew(in_corr(in_pct(Vwap, 1), in_pct(Amt, 1), 15)), 20)` |
| slot b seed 10 | 过 | 0.38 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.50 | 0.24 | 0.06 | 0.03 | 0.20 | 0.19 | `cross_mean(day_kurt(in_corr(Ret, in_pct(Amt, 1), 15)), 15)` |
| R 1 variant 1 | 过 | 0.93 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.94 | 0.30 | 0.41 | 0.05 | 0.32 | 0.26 | `ts_quantile_q75(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` |
| R 1 variant 2 | 过 | 0.89 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.88 | 0.40 | 0.22 | 0.03 | 0.35 | 0.08 | `ts_quantile_q75(day_kurt(in_autocorr(Low, 3, 1)), 15)` |
| R 1 variant 3 | 过 | 0.88 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.90 | 0.29 | 0.39 | 0.06 | 0.31 | 0.26 | `ts_quantile_q75(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 10)` |
| R 1 variant 4 | 过 | 0.85 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), ` | 0.86 | 0.30 | 0.44 | 0.10 | 0.34 | 0.24 | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` |
| R 2 variant 1 | 过 | 0.83 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.94 | 0.21 | 0.35 | 0.09 | 0.28 | 0.07 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` |
| R 2 variant 2 | 过 | 0.78 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.90 | 0.18 | 0.25 | 0.02 | 0.22 | 0.09 | `ts_quantile_q75(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` |
| R 2 variant 3 | 过 | 0.63 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.77 | 0.06 | 0.08 | 0.01 | 0.09 | 0.03 | `ts_quantile_q50(day_kurt(in_autocorr(Ret, 3, 1)), 30)` |
| R 2 variant 4 | 过 | 0.53 | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 0.70 | 0.00 | 0.01 | 0.04 | 0.02 | 0.02 | `cross_mean(sigmoid(day_kurt(in_autocorr(Ret, 3, 1))), 30)` |
