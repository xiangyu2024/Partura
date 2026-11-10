# 相关度表:种子 2060,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.71 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.94 | 0.50 | 0.28 | 0.25 | 0.50 | 0.17 | `day_ar1_coefficient(Volume)` |
| slot a seed 1 | 过 | 0.80 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.73 | 0.77 | 0.23 | 0.04 | 0.74 | 0.24 | `cross_ema(day_ar1_coefficient(Volume), 40)` |
| slot a seed 2 | 过 | 0.80 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.77 | 0.77 | 0.28 | 0.04 | 0.75 | 0.23 | `cross_mean(day_ar1_coefficient(Volume), 60)` |
| slot a seed 3 | 过 | 0.37 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.26 | 0.12 | 0.21 | 0.33 | 0.14 | 0.05 | `cross_zscore(day_ar1_coefficient(Volume), 120)` |
| slot a seed 4 | 过 | 0.60 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.44 | 0.23 | 0.40 | 0.44 | 0.27 | 0.08 | `sub(cross_mean(day_ar1_coefficient(Volume), 10), cross_mean(day_ar1_coefficient(Volume), 120))` |
| slot a seed 5 | 过 | 0.90 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.92 | 0.64 | 0.45 | 0.14 | 0.65 | 0.03 | `cs_bucket_demean(cross_mean(day_ar1_coefficient(Volume), 20), LogFloatCap)` |
| slot a seed 6 | 过 | 0.75 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.59 | 0.75 | 0.32 | 0.02 | 0.76 | 0.26 | `cs_bucket_demean(cross_ema(day_ar1_coefficient(Volume), 30), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 7 | 过 | 0.56 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.82 | 0.04 | 0.29 | 0.15 | 0.07 | 0.42 | `cs_bucket_zscore(cross_mean(day_ar1_coefficient(Volume), 20), cross_mean(log(day_sum(Amt)), 20))` |
| slot a seed 8 | 过 | 0.70 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.58 | 0.69 | 0.21 | 0.06 | 0.66 | 0.23 | `cross_semistd_neg(day_ar1_coefficient(Volume), 60)` |
| slot a seed 9 | 过 | 0.14 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.13 | 0.03 | 0.16 | 0.06 | 0.06 | 0.21 | `cross_autocorr(day_ar1_coefficient(Volume), 60, 1)` |
| slot a seed 10 | 过 | 0.07 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.02 | 0.15 | 0.04 | 0.07 | 0.15 | 0.12 | `cross_corr(day_ar1_coefficient(Volume), day_sum(Ret), 60)` |
| slot a seed 11 | 过 | 0.14 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.15 | 0.02 | 0.04 | 0.07 | 0.03 | 0.15 | `cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60)` |
| slot a seed 12 | 过 | 0.07 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.03 | 0.01 | 0.03 | 0.05 | 0.02 | 0.03 | `mul(cross_zscore(day_ar1_coefficient(Volume), 60), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 13 | 过 | 0.76 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.71 | 0.76 | 0.22 | 0.07 | 0.72 | 0.27 | `cross_tail_mean_q25(day_ar1_coefficient(Volume), 60)` |
| slot a seed 14 | 过 | 0.54 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.22 | 0.65 | 0.42 | 0.04 | 0.69 | 0.33 | `cross_mean(sub(day_ar1_coefficient(Volume), day_ar1_coefficient(Ret)), 40)` |
| slot b seed 1 | 过 | 0.10 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.24 | 0.05 | 0.14 | 0.04 | 0.07 | 0.11 | `cross_mean(day_ar1_coefficient(mul(sign(Ret), Volume)), 20)` |
| slot b seed 2 | 过 | 0.07 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.21 | 0.09 | 0.15 | 0.05 | 0.12 | 0.15 | `cross_ema(day_autocorr(mul(sign(Ret), Volume), 1), 40)` |
| slot b seed 3 | 过 | 0.88 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.76 | 0.78 | 0.45 | 0.15 | 0.79 | 0.28 | `cross_mean(sub(day_ar1_coefficient(mul(sign(Ret), Volume)), day_ar1_coefficient(Volume)), 20)` |
| slot b seed 4 | 过 | 0.01 | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(` | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | `cross_zscore(day_autocorr(mul(sign(Ret), Volume), 5), 120)` |
| slot b seed 5 | 过 | 0.06 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.01 | 0.08 | 0.05 | 0.02 | 0.06 | 0.05 | `cross_mean(day_autocorr(mul(sign(Ret), Volume), 10), 40)` |
| slot b seed 6 | 过 | 0.09 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.23 | 0.06 | 0.15 | 0.04 | 0.09 | 0.12 | `cross_mean(day_ar1_coefficient(mul(sign(Ret), Amt)), 30)` |
| slot b seed 7 | 过 | 0.07 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.23 | 0.08 | 0.12 | 0.03 | 0.10 | 0.14 | `cross_mean(sub(day_autocorr(mul(sign(Ret), Volume), 1), day_autocorr(mul(sign(Ret), Volume), 10)), 30)` |
| slot b seed 8 | 过 | 0.65 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.49 | 0.54 | 0.21 | 0.00 | 0.51 | 0.09 | `cross_mean(sub(day_ar1_coefficient(mul(sign(Ret), Volume)), day_ar1_coefficient(Ret)), 30)` |
| slot b seed 9 | 过 | 0.01 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.05 | 0.04 | 0.14 | 0.07 | 0.05 | 0.09 | `cross_corr(day_ar1_coefficient(mul(sign(Ret), Volume)), day_sum(Ret), 60)` |
| slot b seed 10 | 过 | 0.12 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.24 | 0.02 | 0.14 | 0.03 | 0.01 | 0.01 | `cs_bucket_demean(cross_mean(day_autocorr(mul(sign(Ret), Volume), 1), 30), LogFloatCap)` |
| slot b seed 11 | 过 | 0.16 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.30 | 0.01 | 0.12 | 0.04 | 0.04 | 0.13 | `cross_mean(day_ar1_coefficient(mul(sign(in_slice(Ret, 11, 230)), in_slice(Volume, 11, 230))), 20)` |
| slot b seed 12 | 过 | 0.03 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.14 | 0.02 | 0.01 | 0.01 | 0.02 | 0.00 | `cross_zscore(day_ar1_coefficient(mul(sign(Ret), Volume)), 120)` |
| slot b seed 13 | 过 | 0.40 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.32 | 0.33 | 0.06 | 0.06 | 0.28 | 0.11 | `cross_mean(day_hurst(mul(sign(Ret), Volume)), 40)` |
| R 1 variant 1 | 过 | 0.92 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.92 | 0.80 | 0.40 | 0.09 | 0.80 | 0.23 | `ts_decay_linear(day_ar1_coefficient(Volume), 40)` |
| R 1 variant 2 | 过 | 0.80 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.73 | 0.77 | 0.23 | 0.04 | 0.74 | 0.24 | `cross_ema(day_ar1_coefficient(Volume), 40)` |
| R 1 variant 3 | 过 | 0.93 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.91 | 0.75 | 0.41 | 0.20 | 0.75 | 0.24 | `ts_decay_linear(day_ar1_coefficient(in_slice(Volume, 11, 230)), 20)` |
| R 1 variant 4 | 过 | 0.96 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.98 | 0.75 | 0.42 | 0.21 | 0.76 | 0.23 | `ts_decay_linear(cs_rank(day_ar1_coefficient(Volume)), 20)` |
| R 1 variant 5 | 过 | 0.37 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.26 | 0.12 | 0.21 | 0.33 | 0.14 | 0.05 | `cross_zscore(day_ar1_coefficient(Volume), 120)` |
| R 1 variant 6 | 过 | 0.92 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.95 | 0.61 | 0.45 | 0.21 | 0.63 | 0.03 | `cs_bucket_demean(ts_decay_linear(day_ar1_coefficient(Volume), 20), LogFloatCap)` |
| R 1 variant 7 | 过 | 0.48 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.21 | 0.01 | 0.13 | 0.42 | 0.04 | 0.04 | `sub(ts_decay_linear(day_ar1_coefficient(Volume), 5), ts_decay_linear(day_ar1_coefficient(Volume), 60))` |
| R 1 variant 8 | 过 | 0.80 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.77 | 0.77 | 0.28 | 0.04 | 0.75 | 0.23 | `cross_mean(day_ar1_coefficient(Volume), 60)` |
