# 相关度表:种子 2073,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.94 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.99 | 0.52 | 0.26 | 0.13 | 0.49 | 0.36 | `day_cov(Low, Close)` |
| slot a seed 1 | 过 | 0.09 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.08 | 0.07 | 0.05 | 0.01 | 0.07 | 0.01 | `cross_corr(day_cov(Low, Close), day_sum(Amt), 60)` |
| slot a seed 2 | 过 | 0.26 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.09 | 0.25 | 0.30 | 0.08 | 0.27 | 0.04 | `cross_corr(day_cov(Low, Close), day_mean(Close), 60)` |
| slot a seed 3 | 过 | 0.26 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.09 | 0.25 | 0.30 | 0.08 | 0.27 | 0.04 | `cross_corr(day_cov(Low, Close), day_sum(Low), 60)` |
| slot a seed 4 | 过 | 0.07 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.08 | 0.01 | 0.03 | 0.02 | 0.02 | 0.01 | `cross_regres(log(day_sum(Amt)), log(day_cov(Low, Close)), 60)` |
| slot a seed 5 | 过 | 0.19 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.09 | 0.02 | 0.14 | 0.26 | 0.04 | 0.02 | `cross_zscore(div(day_cov(Low, Close), mul(day_mean(Close), day_mean(Close))), 120)` |
| slot a seed 6 | 过 | 0.27 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.10 | 0.11 | 0.25 | 0.39 | 0.13 | 0.04 | `cross_zscore(log(day_cov(Low, Close)), 120)` |
| slot a seed 7 | 过 | 0.34 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.17 | 0.21 | 0.46 | 0.48 | 0.24 | 0.06 | `sub(cross_mean(log(day_cov(Low, Close)), 10), cross_mean(log(day_cov(Low, Close)), 120))` |
| slot a seed 8 | 过 | 0.10 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.14 | 0.03 | 0.06 | 0.06 | 0.05 | 0.08 | `ts_skew(day_cov(Low, Close), 40)` |
| slot a seed 9 | 过 | 0.35 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.24 | 0.18 | 0.40 | 0.44 | 0.22 | 0.08 | `cross_ema(div(day_cov(Low, Close), cross_mean(day_cov(Low, Close), 60)), 10)` |
| slot a seed 10 | 过 | 0.13 | `pow_2(day_max(pow_1_5(Vwap)))` | 0.10 | 0.08 | 0.06 | 0.04 | 0.06 | 0.00 | `cross_corr(day_cov(Low, Close), day_cov(Low, High), 60)` |
| slot b seed 1 | 过 | 0.12 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(` | 0.17 | 0.02 | 0.02 | 0.06 | 0.00 | 0.11 | `cross_mean(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 20)` |
| slot b seed 2 | 过 | 0.18 | `pow_2(day_max(pow_1_5(Vwap)))` | 0.25 | 0.03 | 0.03 | 0.03 | 0.01 | 0.17 | `cross_mean(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 60)` |
| slot b seed 3 | 过 | 0.12 | `day_quantile_q75(cross_sum(pow_1_5(Volume), 3))` | 0.17 | 0.01 | 0.01 | 0.08 | 0.01 | 0.11 | `sub(cross_mean(day_es_ratio_hi(Ret), 20), cross_mean(day_es_ratio_lo(Ret), 20))` |
| slot b seed 4 | 过 | 0.40 | `pow_2(day_max(pow_1_5(Vwap)))` | 0.15 | 0.53 | 0.07 | 0.13 | 0.44 | 0.38 | `cross_mean(day_es_ratio_hi(Amt), 20)` |
| slot b seed 5 | 过 | 0.25 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.28 | 0.07 | 0.27 | 0.88 | 0.10 | 0.05 | `sub(cross_semistd_pos(day_mean(Close), 20), cross_semistd_neg(day_mean(Close), 20))` |
| slot b seed 6 | 过 | 0.32 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.12 | 0.23 | 0.40 | 0.38 | 0.26 | 0.07 | `div(cross_semistd_neg(day_mean(Close), 60), cross_semistd_pos(day_mean(Close), 60))` |
| slot b seed 7 | 废品 | 0.21 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.15 | 0.12 | 0.25 | 0.32 | 0.14 | 0.03 | `cross_mean(sub(day_at_max_ratio(High), day_at_min_ratio(Low)), 20)` |
| slot b seed 8 | 废品 | 0.60 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.82 | 0.54 | 0.23 | 0.02 | 0.48 | 0.22 | `cross_mean(day_pos_ratio(Ret), 20)` |
| slot b seed 9 | 过 | 0.31 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.10 | 0.26 | 0.47 | 0.28 | 0.27 | 0.04 | `sub(cross_mean(day_pos_ratio(Ret), 20), cross_mean(day_pos_ratio(Ret), 120))` |
| slot b seed 10 | 过 | 0.04 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.04 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | `cross_zscore(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 120)` |
| R 1 variant 1 | 过 | 0.73 | `ts_max(day_corr(pow_1_5(Ret), Vwap), 40)` | 0.72 | 0.25 | 0.24 | 0.01 | 0.27 | 0.02 | `ts_max(day_corr(pow_1_5(Ret), Close), 40)` |
| R 1 variant 2 | 过 | 0.77 | `ts_max(day_corr(pow_1_5(Ret), Vwap), 40)` | 0.77 | 0.37 | 0.16 | 0.04 | 0.35 | 0.06 | `ts_max(day_corr(pow_1_5(Ret), Open), 40)` |
| R 1 variant 3 | 过 | 0.60 | `ts_max(day_corr(pow_1_5(Ret), Vwap), 40)` | 0.61 | 0.21 | 0.20 | 0.02 | 0.23 | 0.00 | `ts_max(day_corr(pow_1_5(Ret), Close), 60)` |
| R 1 variant 4 | 过 | 0.19 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.12 | 0.06 | 0.10 | 0.15 | 0.02 | 0.07 | `ts_mean(day_corr(pow_1_5(Ret), Close), 40)` |
| R 1 variant 5 | 过 | 0.40 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.35 | 0.38 | 0.01 | 0.05 | 0.33 | 0.12 | `ts_max(day_corr(Ret, Close), 40)` |
| R 1 variant 6 | 过 | 0.17 | `ts_max(day_corr(pow_1_5(Ret), Vwap), 40)` | 0.13 | 0.06 | 0.05 | 0.07 | 0.09 | 0.14 | `ts_max(day_corr(pow_1_5(Ret), Amt), 40)` |
