# 相关度表:种子 2062,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.42 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.22 | 0.52 | 0.09 | 0.11 | 0.51 | 0.42 | `day_at_max_ratio(Vwap)` |
| slot a seed 1 | 过 | 0.48 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.26 | 0.31 | 0.28 | 0.21 | 0.24 | 0.33 | `cross_mean(day_at_max_ratio(Vwap), 20)` |
| slot a seed 2 | 过 | 0.28 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.15 | 0.02 | 0.42 | 0.07 | 0.05 | 0.23 | `cross_ema(day_at_max_ratio(Vwap), 30)` |
| slot a seed 3 | 过 | 0.16 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.15 | 0.10 | 0.22 | 0.01 | 0.12 | 0.05 | `sub(cross_mean(day_at_max_ratio(Vwap), 5), cross_mean(day_at_max_ratio(Vwap), 60))` |
| slot a seed 4 | 过 | 0.12 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.15 | 0.03 | 0.25 | 0.15 | 0.07 | 0.04 | `cross_regres(day_std(Ret), day_at_max_ratio(Vwap), 60)` |
| slot a seed 5 | 过 | 0.25 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.19 | 0.23 | 0.28 | 0.20 | 0.28 | 0.25 | `cs_bucket_demean(cross_mean(day_at_max_ratio(Vwap), 20), LogFloatCap)` |
| slot a seed 6 | 过 | 0.30 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.20 | 0.35 | 0.35 | 0.15 | 0.41 | 0.37 | `cs_regres(cross_mean(day_at_max_ratio(Vwap), 30), LogFloatCap)` |
| slot a seed 7 | 过 | 0.07 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.03 | 0.10 | 0.07 | 0.00 | 0.12 | 0.06 | `cross_corr(day_at_max_ratio(Vwap), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 8 | 过 | 0.25 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.13 | 0.14 | 0.26 | 0.57 | 0.17 | 0.05 | `mul(cross_mean(day_at_max_ratio(Vwap), 20), sign(cross_sum(day_sum(Ret), 20)))` |
| slot a seed 9 | 废品 | 0.21 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.08 | 0.16 | 0.22 | 0.26 | 0.19 | 0.02 | `sub(cross_mean(day_at_max_ratio(Vwap), 20), cross_mean(day_at_min_ratio(Vwap), 20))` |
| slot a seed 10 | 过 | 0.27 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.12 | 0.03 | 0.38 | 0.10 | 0.04 | 0.19 | `cross_stddev(day_at_max_ratio(Vwap), 60)` |
| slot a seed 11 | 过 | 0.34 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.19 | 0.11 | 0.37 | 0.11 | 0.04 | 0.24 | `cs_bucket_zscore(cross_mean(day_at_max_ratio(Vwap), 40), cross_mean(day_sum(Amt), 30))` |
| slot a seed 12 | 过 | 0.07 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.11 | 0.00 | 0.14 | 0.09 | 0.01 | 0.05 | `cross_zscore(day_at_max_ratio(Vwap), 120)` |
| slot b seed 1 | 过 | 0.05 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.12 | 0.03 | 0.03 | 0.03 | 0.02 | 0.00 | `cs_flip_by_state(cross_mean(day_autocorr_n1(Ret), 20), day_sum(Amt))` |
| slot b seed 2 | 过 | 0.07 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.14 | 0.04 | 0.03 | 0.01 | 0.03 | 0.01 | `cs_flip_by_state(cross_mean(day_autocorr_n1(Ret), 60), day_std(Ret))` |
| slot b seed 3 | 过 | 0.03 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.05 | 0.02 | 0.03 | 0.00 | 0.01 | 0.04 | `cs_flip_by_state(cross_stddev(day_autocorr_n1(Ret), 20), day_sum(Amt))` |
| slot b seed 4 | 过 | 0.03 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.06 | 0.01 | 0.00 | 0.01 | 0.01 | 0.00 | `cs_flip_by_state(cross_regres(day_std(Ret), day_autocorr_n1(Ret), 60), day_sum(Ret))` |
| slot b seed 5 | 过 | 0.02 | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 3)` | 0.07 | 0.01 | 0.01 | 0.00 | 0.01 | 0.01 | `cs_flip_by_state(cross_corr(day_autocorr_n1(Ret), day_sum(Amt), 60), day_std(Ret))` |
| slot b seed 6 | 过 | 0.05 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.08 | 0.06 | 0.05 | 0.02 | 0.05 | 0.05 | `cs_flip_by_state(cross_mean(day_gini(Amt), 30), day_std(Ret))` |
| slot b seed 7 | 过 | 0.16 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.07 | 0.15 | 0.02 | 0.01 | 0.14 | 0.11 | `cs_flip_by_state(cross_mean(day_at_min_ratio(Vwap), 20), day_sum(Ret))` |
| slot b seed 8 | 过 | 0.04 | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full` | 0.09 | 0.03 | 0.02 | 0.01 | 0.02 | 0.10 | `cs_flip_by_state(cross_mean(day_es_ratio_hi(Ret), 40), day_sum(Ret))` |
| slot b seed 9 | 过 | 0.02 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.09 | 0.01 | 0.00 | 0.04 | 0.02 | 0.03 | `cs_flip_by_state(cross_mean(day_distinct_ratio(Close), 20), day_sum(Amt))` |
| slot b seed 10 | 过 | 0.16 | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Vo` | 0.15 | 0.11 | 0.01 | 0.01 | 0.10 | 0.01 | `cs_flip_by_state(cross_mean(day_autocorr_n1(Ret), 20), day_sum(Ret))` |
| R 1 variant 1 | 过 | 0.93 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.92 | 0.47 | 0.07 | 0.02 | 0.41 | 0.29 | `ts_decay_linear(day_ar1_coefficient(Vwap), 15)` |
| R 1 variant 2 | 过 | 0.85 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.85 | 0.43 | 0.06 | 0.00 | 0.38 | 0.26 | `ts_decay_linear(day_ar1_coefficient(Vwap), 10)` |
| R 1 variant 3 | 过 | 0.85 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.85 | 0.43 | 0.06 | 0.00 | 0.38 | 0.26 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap)))), 10)` |
| R 1 variant 4 | 过 | 0.80 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.86 | 0.39 | 0.01 | 0.04 | 0.33 | 0.15 | `ts_decay_linear(day_ar1_coefficient(Close), 15)` |
| R 1 variant 5 | 过 | 0.82 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.87 | 0.49 | 0.00 | 0.05 | 0.44 | 0.28 | `ts_decay_linear(day_ar1_coefficient(High), 15)` |
| R 1 variant 6 | 过 | 0.95 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.96 | 0.49 | 0.08 | 0.03 | 0.43 | 0.30 | `ts_mean(day_ar1_coefficient(Vwap), 15)` |
| R 2 variant 1 | 过 | 0.73 | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 3)` | 0.89 | 0.42 | 0.01 | 0.02 | 0.38 | 0.23 | `cross_mean(day_ar1_coefficient(High), 6)` |
| R 2 variant 2 | 过 | 0.79 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.86 | 0.48 | 0.01 | 0.04 | 0.42 | 0.27 | `cross_mean(day_ar1_coefficient(High), 10)` |
| R 2 variant 3 | 过 | 0.72 | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 3)` | 0.89 | 0.42 | 0.01 | 0.02 | 0.38 | 0.23 | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(High))), 6)` |
| R 2 variant 4 | 过 | 0.73 | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 3)` | 0.88 | 0.36 | 0.00 | 0.00 | 0.31 | 0.13 | `cross_mean(day_ar1_coefficient(Open), 6)` |
| R 2 variant 5 | 过 | 0.80 | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(V` | 0.93 | 0.48 | 0.01 | 0.00 | 0.43 | 0.25 | `cross_mean(day_ar1_coefficient(Low), 10)` |
