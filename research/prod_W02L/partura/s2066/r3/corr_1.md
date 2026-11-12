# 相关度表:种子 2066,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.31 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.17 | 0.11 | 0.14 | 0.07 | 0.04 | 0.23 | `day_hurst(cross_ema(pow_1_5(Volume), 60))` |
| slot a seed 1 | 过 | 0.28 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.17 | 0.28 | 0.14 | 0.05 | 0.27 | 0.04 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(cross_ema(pow_1_5(Volume), 5)))` |
| slot a seed 2 | 过 | 0.06 | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_` | 0.03 | 0.15 | 0.02 | 0.00 | 0.14 | 0.26 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(cross_ema(pow_1_5(Amt), 60)))` |
| slot a seed 3 | 过 | 0.19 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.15 | 0.18 | 0.11 | 0.12 | 0.19 | 0.10 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Ret))` |
| slot a seed 4 | 过 | 0.20 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.10 | 0.36 | 0.24 | 0.17 | 0.39 | 0.04 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Amt))` |
| slot a seed 5 | 过 | 0.28 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.10 | 0.50 | 0.32 | 0.17 | 0.53 | 0.06 | `cross_mean(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Amt)), 10)` |
| slot a seed 6 | 过 | 0.20 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.10 | 0.33 | 0.24 | 0.17 | 0.36 | 0.00 | `cs_bucket_rank(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume)), LogFloatCap)` |
| slot a seed 7 | 过 | 0.10 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.13 | 0.00 | 0.12 | 0.15 | 0.03 | 0.21 | `cs_bucket_demean(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume)), cross_mean(day_mean(Amt), 20))` |
| slot a seed 8 | 过 | 0.07 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.10 | 0.01 | 0.01 | 0.15 | 0.00 | 0.01 | `cross_zscore(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume)), 20)` |
| slot a seed 9 | 过 | 0.30 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.10 | 0.53 | 0.32 | 0.11 | 0.56 | 0.07 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), cross_mean(day_hurst(Volume), 20))` |
| slot a seed 10 | 过 | 0.32 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.13 | 0.53 | 0.30 | 0.10 | 0.56 | 0.06 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), cross_ema(day_hurst(Volume), 10))` |
| slot a seed 11 | 过 | 0.02 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.02 | 0.02 | 0.07 | 0.04 | 0.04 | 0.07 | `cross_regbeta(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume), 20)` |
| slot a seed 12 | 过 | 0.20 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.10 | 0.34 | 0.23 | 0.17 | 0.36 | 0.01 | `cs_bucket_zscore(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Amt)), LogFloatCap)` |
| slot b seed 1 | 过 | 0.17 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.04 | 0.37 | 0.17 | 0.17 | 0.37 | 0.15 | `day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1))` |
| slot b seed 2 | 过 | 0.28 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.06 | 0.62 | 0.29 | 0.20 | 0.62 | 0.24 | `cross_mean(day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1)), 10)` |
| slot b seed 3 | 过 | 0.03 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.03 | 0.01 | 0.01 | 0.12 | 0.01 | 0.02 | `cross_zscore(day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1)), 20)` |
| slot b seed 4 | 过 | 0.18 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.05 | 0.38 | 0.16 | 0.15 | 0.38 | 0.15 | `day_corr(Amt, cross_delay(cross_ema(Amt, 20), 1))` |
| slot b seed 5 | 过 | 0.34 | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_` | 0.14 | 0.72 | 0.12 | 0.12 | 0.68 | 0.47 | `day_mean(abs_(sub(div(Volume, in_sum(Volume)), div(cross_delay(cross_ema(Volume, 60), 1), in_sum(cross_delay(cross_ema(Volume, 60), 1))))))` |
| slot b seed 6 | 过 | 0.41 | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_` | 0.15 | 0.84 | 0.12 | 0.07 | 0.78 | 0.54 | `cross_mean(day_mean(abs_(sub(div(Volume, in_sum(Volume)), div(cross_delay(cross_ema(Volume, 60), 1), in_sum(cross_delay(cross_ema(Volume, 60), 1)))))), 10)` |
| slot b seed 7 | 过 | 0.06 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` | 0.09 | 0.01 | 0.04 | 0.20 | 0.00 | 0.02 | `cross_zscore(day_mean(abs_(sub(div(Amt, in_sum(Amt)), div(cross_delay(cross_ema(Amt, 60), 1), in_sum(cross_delay(cross_ema(Amt, 60), 1)))))), 20)` |
| slot b seed 8 | 过 | 0.25 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.05 | 0.42 | 0.27 | 0.20 | 0.42 | 0.01 | `cs_bucket_rank(cross_mean(day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1)), 5), LogFloatCap)` |
| slot b seed 9 | 过 | 0.18 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.12 | 0.36 | 0.30 | 0.22 | 0.39 | 0.09 | `cross_stddev(day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1)), 20)` |
| slot b seed 10 | 过 | 0.17 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.04 | 0.38 | 0.17 | 0.16 | 0.39 | 0.15 | `day_corr(div(Volume, in_sum(Volume)), cross_delay(cross_ema(div(Volume, in_sum(Volume)), 60), 1))` |
| slot b seed 11 | 过 | 0.12 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.08 | 0.16 | 0.10 | 0.08 | 0.16 | 0.02 | `sub(day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1)), day_corr(Volume, cross_delay(cross_ema(Volume, 5), 1)))` |
| slot b seed 12 | 过 | 0.18 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.09 | 0.03 | 0.05 | 0.05 | 0.03 | 0.28 | `cs_bucket_demean(cross_ema(day_corr(Volume, cross_delay(cross_ema(Volume, 60), 1)), 10), cross_mean(day_mean(Amt), 20))` |
| R 1 variant 1 | 过 | 0.64 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.52 | 0.29 | 0.24 | 0.08 | 0.27 | 0.08 | `cross_stddev(day_var(cross_med(Ret, 60)), 180)` |
| R 1 variant 2 | 过 | 0.55 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.42 | 0.26 | 0.21 | 0.09 | 0.24 | 0.12 | `cross_stddev(day_var(cross_med(Ret, 60)), 240)` |
| R 1 variant 3 | 过 | 0.58 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.54 | 0.08 | 0.25 | 0.04 | 0.09 | 0.16 | `cross_stddev(day_std(cross_med(Ret, 60)), 120)` |
| R 1 variant 4 | 过 | 0.52 | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` | 0.41 | 0.26 | 0.15 | 0.07 | 0.23 | 0.04 | `cross_stddev(day_var(cross_med(Ret, 120)), 120)` |
| R 2 variant 1 | 过 | 0.65 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.58 | 0.28 | 0.03 | 0.07 | 0.21 | 0.19 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 60)` |
| R 2 variant 2 | 过 | 0.53 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.41 | 0.30 | 0.05 | 0.06 | 0.24 | 0.21 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 120)` |
| R 2 variant 3 | 过 | 0.57 | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` | 0.38 | 0.52 | 0.08 | 0.09 | 0.43 | 0.37 | `cross_mean(day_skew(div(Volume, in_sum(Volume))), 60)` |
