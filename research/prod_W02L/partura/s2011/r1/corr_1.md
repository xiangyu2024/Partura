# 相关度表:种子 2011,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.56 | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)` | 0.80 | 0.50 | 0.26 | 0.25 | 0.51 | 0.14 | `day_ar1_coefficient(Volume)` |
| slot a seed 1 | 过 | 0.14 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.09 | 0.18 | 0.01 | 0.08 | 0.17 | 0.08 | `cross_corr(day_ar1_coefficient(Volume), day_sum(Ret), 60)` |
| slot a seed 2 | 过 | 0.16 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.09 | 0.21 | 0.04 | 0.06 | 0.20 | 0.10 | `cross_corr(day_ar1_coefficient(Volume), day_sum(Ret), 120)` |
| slot a seed 3 | 过 | 0.09 | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)` | 0.03 | 0.10 | 0.09 | 0.02 | 0.10 | 0.04 | `cross_corr(cross_delay(day_ar1_coefficient(Volume), 1), day_sum(Ret), 120)` |
| slot a seed 4 | 过 | 0.17 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.19 | 0.09 | 0.16 | 0.11 | 0.10 | 0.03 | `cross_corr(day_ar1_coefficient(Volume), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 5 | 过 | 0.08 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.06 | 0.11 | 0.16 | 0.05 | 0.10 | 0.14 | `cross_regbeta(day_ar1_coefficient(Volume), day_sum(Ret), 120)` |
| slot a seed 6 | 过 | 0.22 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.27 | 0.27 | 0.03 | 0.03 | 0.24 | 0.21 | `cross_corr(day_ar1_coefficient(Volume), abs_(day_sum(Ret)), 60)` |
| slot a seed 7 | 过 | 0.08 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.11 | 0.06 | 0.03 | 0.09 | 0.05 | 0.21 | `cross_corr(day_ar1_coefficient(Volume), div(day_first(Open), cross_delay(day_last(Close), 1)), 120)` |
| slot a seed 8 | 过 | 0.25 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.06 | 0.32 | 0.11 | 0.03 | 0.31 | 0.17 | `cross_corr(day_ar1_coefficient(Volume), cross_delta(log(day_sum(Amt)), 1), 60)` |
| slot a seed 9 | 过 | 0.10 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.12 | 0.02 | 0.07 | 0.07 | 0.03 | 0.05 | `sub(cross_corr(cross_delay(day_ar1_coefficient(Volume), 1), day_sum(Ret), 60), cross_corr(day_ar1_coefficient(Volume), cross_delay(day_sum(Ret), 1), 60))` |
| slot a seed 10 | 过 | 0.05 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.02 | 0.03 | 0.02 | 0.07 | 0.03 | 0.03 | `cross_zscore(cross_corr(day_ar1_coefficient(Volume), day_sum(Ret), 60), 120)` |
| slot a seed 11 | 过 | 0.04 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.24 | 0.06 | 0.09 | 0.23 | 0.07 | 0.03 | `mul(cross_corr(day_ar1_coefficient(Volume), day_sum(Ret), 120), cross_zscore(day_ar1_coefficient(Volume), 60))` |
| slot a seed 12 | 过 | 0.07 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.04 | 0.02 | 0.05 | 0.10 | 0.02 | 0.01 | `cross_mean(mul(cross_zscore(day_ar1_coefficient(Volume), 60), sign(day_sum(Ret))), 20)` |
| slot a seed 13 | 过 | 0.27 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.31 | 0.14 | 0.13 | 0.03 | 0.10 | 0.22 | `ts_std(day_ar1_coefficient(Volume), 100)` |
| slot a seed 14 | 过 | 0.24 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.37 | 0.00 | 0.14 | 0.02 | 0.03 | 0.14 | `sub(ts_quantile_q75(day_ar1_coefficient(Volume), 100), ts_quantile_q25(day_ar1_coefficient(Volume), 100))` |
| slot a seed 15 | 过 | 0.18 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.08 | 0.49 | 0.08 | 0.01 | 0.46 | 0.75 | `cs_first_low40(cross_corr(day_ar1_coefficient(Volume), day_sum(Ret), 120), LogFloatCap)` |
| slot b seed 1 | 过 | 0.70 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.41 | 0.70 | 0.31 | 0.01 | 0.68 | 0.22 | `cross_mean(day_ar1_coefficient(in_logchg(Volume, 1)), 60)` |
| slot b seed 2 | 过 | 0.70 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.40 | 0.70 | 0.24 | 0.03 | 0.68 | 0.23 | `cross_ema(day_ar1_coefficient(in_logchg(Amt, 1)), 60)` |
| slot b seed 3 | 过 | 0.31 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.28 | 0.07 | 0.06 | 0.02 | 0.04 | 0.21 | `ts_quantile_q75(day_ar1_coefficient(mul(sign(Ret), Volume)), 100)` |
| slot b seed 4 | 过 | 0.14 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.15 | 0.06 | 0.14 | 0.02 | 0.09 | 0.24 | `cross_mean(day_ar1_coefficient(mul(sign(Ret), Amt)), 120)` |
| slot b seed 5 | 过 | 0.92 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.82 | 0.81 | 0.30 | 0.02 | 0.80 | 0.29 | `sub(cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 60), cross_mean(day_ar1_coefficient(Volume), 60))` |
| slot b seed 6 | 过 | 0.93 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.90 | 0.69 | 0.25 | 0.06 | 0.68 | 0.11 | `cross_mean(day_ar1_coefficient(sub(Volume, cross_mean(Volume, 20))), 60)` |
| slot b seed 7 | 过 | 0.07 | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)` | 0.09 | 0.04 | 0.02 | 0.04 | 0.04 | 0.00 | `cross_zscore(cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 20), 120)` |
| slot b seed 8 | 过 | 0.16 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.20 | 0.04 | 0.14 | 0.01 | 0.07 | 0.23 | `cross_mean(day_corr(mul(sign(Ret), Volume), in_delay(mul(sign(Ret), Volume), 1)), 60)` |
| slot b seed 9 | 过 | 0.17 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.22 | 0.02 | 0.17 | 0.00 | 0.04 | 0.15 | `cross_mean(day_ar1_coefficient(mul(Ret, Volume)), 60)` |
| slot b seed 10 | 过 | 0.07 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.18 | 0.36 | 0.02 | 0.05 | 0.37 | 0.75 | `cs_first_low40(cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 60), LogFloatCap)` |
| slot b seed 11 | 过 | 0.22 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.20 | 0.03 | 0.11 | 0.01 | 0.00 | 0.18 | `cs_bucket_rank(cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 60), cross_mean(day_std(Amt), 30))` |
| slot b seed 12 | 过 | 0.17 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.19 | 0.02 | 0.13 | 0.01 | 0.05 | 0.19 | `cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 20)` |
| slot b seed 13 | 过 | 0.07 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.18 | 0.12 | 0.30 | 0.24 | 0.15 | 0.05 | `sub(cross_mean(day_ar1_coefficient(in_logchg(Volume, 1)), 20), cross_mean(day_ar1_coefficient(in_logchg(Volume, 1)), 120))` |
| slot b seed 14 | 过 | 0.93 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.90 | 0.68 | 0.25 | 0.06 | 0.67 | 0.10 | `cross_mean(day_ar1_coefficient(sub(Amt, cross_mean(Amt, 20))), 60)` |
| slot b seed 15 | 过 | 0.02 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.03 | 0.02 | 0.04 | 0.01 | 0.03 | 0.03 | `mul(cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 60), sign(cross_mean(day_sum(Ret), 20)))` |
| R 1 variant 1 | 过 | 0.53 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.78 | 0.02 | 0.11 | 0.01 | 0.03 | 0.17 | `cross_mean(cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30), 40)` |
| R 1 variant 2 | 过 | 0.32 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.48 | 0.04 | 0.12 | 0.02 | 0.03 | 0.27 | `cross_ema(cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 60), 40)` |
| R 1 variant 3 | 过 | 0.24 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.14 | 0.20 | 0.09 | 0.00 | 0.20 | 0.05 | `cross_autocorr_s1(day_ar1_coefficient(in_logchg(Volume, 1)), 60)` |
| R 1 variant 4 | 过 | 0.38 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.47 | 0.08 | 0.10 | 0.01 | 0.05 | 0.21 | `cross_autocorr_s1(day_ar1_coefficient(sub(Volume, cross_mean(Volume, 20))), 60)` |
| R 1 variant 5 | 过 | 0.09 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.03 | 0.09 | 0.03 | 0.01 | 0.08 | 0.02 | `cross_autocorr_s1(day_ar1_coefficient(mul(sign(Ret), Volume)), 60)` |
| R 1 variant 6 | 过 | 0.61 | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` | 0.75 | 0.00 | 0.14 | 0.03 | 0.02 | 0.18 | `cross_autocorr_s1(cross_zscore(day_ar1_coefficient(Volume), 60), 60)` |
| R 2 variant 1 | 过 | 0.55 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.79 | 0.07 | 0.01 | 0.13 | 0.04 | 0.32 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Amt), 30))` |
| R 2 variant 2 | 过 | 0.89 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.88 | 0.62 | 0.24 | 0.05 | 0.60 | 0.01 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), LogFloatCap)` |
| R 2 variant 3 | 过 | 0.53 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.77 | 0.05 | 0.01 | 0.13 | 0.01 | 0.33 | `cs_bucket_rank(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Amt), 30))` |
| R 2 variant 4 | 过 | 0.39 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.25 | 0.49 | 0.03 | 0.05 | 0.44 | 0.25 | `sub(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), ts_quantile_q25(pow_05(day_ar1_coefficient(Volume)), 100))` |
| R 2 variant 5 | 过 | 0.57 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.29 | 0.60 | 0.02 | 0.05 | 0.55 | 0.26 | `ts_std(pow_05(day_ar1_coefficient(Volume)), 100)` |
| R 2 variant 6 | 过 | 0.59 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.33 | 0.62 | 0.07 | 0.06 | 0.56 | 0.25 | `cross_stddev(pow_05(day_ar1_coefficient(Volume)), 60)` |
| R 2 variant 7 | 过 | 0.62 | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coeff` | 0.37 | 0.59 | 0.25 | 0.04 | 0.57 | 0.15 | `ts_quantile_q75(day_ar1_coefficient(in_logchg(Volume, 1)), 100)` |
