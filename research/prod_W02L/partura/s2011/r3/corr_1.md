# 相关度表:种子 2011,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.33 | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(` | 0.45 | 0.16 | 0.20 | 0.15 | 0.18 | 0.01 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.43 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.39 | 0.30 | 0.28 | 0.02 | 0.30 | 0.02 | `cross_regalpha(day_centroid(Amt), cross_delay(day_sum(Ret), 1), 241)` |
| slot a seed 2 | 过 | 0.24 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.21 | 0.16 | 0.19 | 0.02 | 0.17 | 0.04 | `cross_regalpha(day_centroid(Amt), cross_delay(day_sum(Ret), 3), 241)` |
| slot a seed 3 | 过 | 0.33 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.23 | 0.22 | 0.24 | 0.03 | 0.23 | 0.04 | `cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 120)` |
| slot a seed 4 | 过 | 0.31 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.27 | 0.17 | 0.18 | 0.01 | 0.17 | 0.08 | `cross_regbeta(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241)` |
| slot a seed 5 | 过 | 0.20 | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Vol` | 0.17 | 0.09 | 0.12 | 0.02 | 0.10 | 0.06 | `cross_reg_tvalue(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241)` |
| slot a seed 6 | 过 | 0.12 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.10 | 0.10 | 0.08 | 0.02 | 0.10 | 0.04 | `cross_regalpha(day_centroid(Amt), cross_delay(day_sum(Ret), 20), 241)` |
| slot a seed 7 | 过 | 0.12 | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Vol` | 0.09 | 0.17 | 0.21 | 0.00 | 0.18 | 0.11 | `cross_regalpha(day_centroid(Amt), day_sum(Ret), 241)` |
| slot a seed 8 | 过 | 0.32 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.28 | 0.04 | 0.13 | 0.00 | 0.04 | 0.23 | `cs_bucket_demean(cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241), cross_mean(day_std(Amt), 30))` |
| slot a seed 9 | 过 | 0.37 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.33 | 0.17 | 0.17 | 0.03 | 0.17 | 0.07 | `cross_ema(cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241), 20)` |
| slot a seed 10 | 过 | 0.44 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.40 | 0.19 | 0.31 | 0.04 | 0.19 | 0.20 | `cross_regalpha(day_centroid(Amt), cross_delay(abs_(day_sum(Ret)), 2), 241)` |
| slot a seed 11 | 过 | 0.43 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.39 | 0.30 | 0.28 | 0.01 | 0.30 | 0.02 | `cross_regalpha(cross_delay(day_centroid(Amt), 1), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241)` |
| slot a seed 12 | 过 | 0.47 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.41 | 0.45 | 0.08 | 0.05 | 0.43 | 0.18 | `cross_regalpha(day_centroid(Amt), cross_delay(day_ar1_coefficient(in_logchg(Volume, 1)), 1), 241)` |
| slot a seed 13 | 过 | 0.18 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.23 | 0.10 | 0.13 | 0.08 | 0.11 | 0.04 | `sub(cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241), cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 60))` |
| slot a seed 14 | 过 | 0.17 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.20 | 0.19 | 0.09 | 0.08 | 0.20 | 0.13 | `cross_regalpha(day_centroid(Amt), cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), 241)` |
| slot a seed 15 | 过 | 0.33 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.23 | 0.21 | 0.23 | 0.02 | 0.22 | 0.05 | `cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 180)` |
| slot b seed 1 | 过 | 0.50 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.52 | 0.17 | 0.22 | 0.05 | 0.17 | 0.10 | `cross_regalpha(cross_zscore(log(day_sum(Amt)), 60), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 2 | 过 | 0.45 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.50 | 0.23 | 0.28 | 0.08 | 0.24 | 0.03 | `cross_regalpha(cross_zscore(log(day_sum(Amt)), 60), day_sum(Ret), 241)` |
| slot b seed 3 | 过 | 0.39 | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Vol` | 0.30 | 0.35 | 0.42 | 0.12 | 0.37 | 0.09 | `cross_regalpha(day_signed_ratio(Ret, Amt), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 4 | 过 | 0.28 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.21 | 0.29 | 0.04 | 0.05 | 0.29 | 0.17 | `cross_regalpha(day_gini(Amt), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 5 | 过 | 0.30 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.32 | 0.22 | 0.30 | 0.02 | 0.21 | 0.01 | `cross_regalpha(day_std(Ret), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 6 | 过 | 0.21 | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(V` | 0.19 | 0.11 | 0.07 | 0.00 | 0.11 | 0.03 | `cross_regalpha(day_es_ratio_hi(Ret), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 7 | 过 | 0.11 | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Vol` | 0.12 | 0.05 | 0.23 | 0.08 | 0.06 | 0.07 | `cross_regalpha(day_flat_ratio(Ret), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 8 | 过 | 0.42 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.47 | 0.26 | 0.31 | 0.04 | 0.27 | 0.01 | `cross_regalpha(cross_zscore(log(day_sum(Amt)), 60), cross_delay(day_sum(Ret), 5), 241)` |
| slot b seed 9 | 过 | 0.14 | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_min(ts_` | 0.08 | 0.19 | 0.09 | 0.08 | 0.19 | 0.15 | `cross_regalpha(abs_(day_sum(Ret)), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 10 | 过 | 0.44 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.40 | 0.35 | 0.36 | 0.09 | 0.36 | 0.05 | `cross_regalpha(day_skew(Ret), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 11 | 过 | 0.44 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.38 | 0.36 | 0.41 | 0.10 | 0.38 | 0.06 | `cross_regalpha(cross_delta(log(day_sum(Amt)), 1), cross_delay(day_sum(Ret), 1), 241)` |
| slot b seed 12 | 过 | 0.47 | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(V` | 0.51 | 0.20 | 0.07 | 0.02 | 0.19 | 0.33 | `cs_bucket_demean(cross_regalpha(cross_zscore(log(day_sum(Amt)), 60), cross_delay(day_sum(Ret), 1), 241), cross_mean(day_std(Amt), 30))` |
| slot b seed 13 | 过 | 0.48 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.49 | 0.15 | 0.21 | 0.02 | 0.15 | 0.12 | `cross_ema(cross_regalpha(cross_zscore(log(day_sum(Amt)), 60), cross_delay(day_sum(Ret), 1), 241), 20)` |
| slot b seed 14 | 过 | 0.55 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(` | 0.54 | 0.18 | 0.31 | 0.01 | 0.17 | 0.24 | `cross_regbeta(cross_zscore(log(day_sum(Amt)), 60), cross_delay(day_sum(Ret), 1), 241)` |
