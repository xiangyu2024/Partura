# 相关度表:种子 2030,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.47 | `abs_(ts_std(day_first(Amt), 50))` | 0.19 | 0.50 | 0.28 | 0.25 | 0.50 | 0.17 | `day_ar1_coefficient(Amt)` |
| slot a seed 1 | 过 | 0.29 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.24 | 0.10 | 0.10 | 0.06 | 0.06 | 0.24 | `cross_stddev(day_ar1_coefficient(Amt), 100)` |
| slot a seed 2 | 过 | 0.24 | `abs_(ts_std(day_first(Amt), 50))` | 0.14 | 0.23 | 0.00 | 0.07 | 0.23 | 0.18 | `cross_corr(day_ar1_coefficient(Amt), cs_demean(day_mean(Ret)), 100)` |
| slot a seed 3 | 过 | 0.38 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.24 | 0.31 | 0.47 | 0.33 | 0.35 | 0.10 | `cross_ema(sub(day_ar1_coefficient(Amt), cross_mean(day_ar1_coefficient(Amt), 120)), 10)` |
| slot a seed 4 | 过 | 0.44 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.36 | 0.02 | 0.15 | 0.06 | 0.05 | 0.21 | `cross_autocorr_s1(day_ar1_coefficient(Amt), 60)` |
| slot a seed 5 | 过 | 0.18 | `pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 4` | 0.13 | 0.07 | 0.07 | 0.07 | 0.04 | 0.07 | `cross_ema(sub(day_ar1_coefficient(Amt), day_ar1_coefficient(Volume)), 60)` |
| slot a seed 6 | 过 | 0.05 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.04 | 0.02 | 0.03 | 0.02 | 0.01 | 0.04 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_ar1_coefficient(Volume)), 60)` |
| slot a seed 7 | 过 | 0.25 | `sub(day_mean(in_sustain_stddev(is_gt(sub(in_boxcox(Volume), ` | 0.31 | 0.03 | 0.13 | 0.04 | 0.02 | 0.09 | `cross_corr(day_ar1_coefficient(Amt), day_ar1_coefficient(Ret), 100)` |
| slot a seed 8 | 过 | 0.30 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.12 | 0.15 | 0.47 | 0.46 | 0.18 | 0.04 | `cross_ema(mul(day_ar1_coefficient(Amt), cs_demean(ts_delta(log(day_last(Close)), 1))), 60)` |
| slot a seed 9 | 过 | 0.63 | `abs_(ts_std(day_first(Amt), 50))` | 0.46 | 0.64 | 0.19 | 0.06 | 0.63 | 0.14 | `cross_tail_mean_q75(day_ar1_coefficient(Amt), 120)` |
| slot a seed 10 | 过 | 0.25 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.26 | 0.06 | 0.06 | 0.03 | 0.07 | 0.06 | `cross_corr(day_ar1_coefficient(Amt), div(day_first(Amt), day_sum(Amt)), 100)` |
| slot a seed 11 | 过 | 0.57 | `abs_(ts_std(day_first(Amt), 50))` | 0.19 | 0.59 | 0.42 | 0.15 | 0.61 | 0.28 | `cross_ema(is_gt(day_ar1_coefficient(Amt), cross_mean(day_ar1_coefficient(Amt), 60)), 60)` |
| slot a seed 12 | 过 | 0.25 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.23 | 0.12 | 0.07 | 0.08 | 0.08 | 0.20 | `cross_stddev(sub(day_ar1_coefficient(Amt), cross_ema(day_ar1_coefficient(Amt), 20)), 100)` |
| slot b seed 1 | 过 | 0.21 | `abs_(ts_std(day_first(Amt), 50))` | 0.28 | 0.50 | 0.09 | 0.08 | 0.41 | 0.35 | `cross_ema(day_kurt(Volume), 60)` |
| slot b seed 2 | 过 | 0.23 | `abs_(ts_std(day_first(Amt), 50))` | 0.30 | 0.53 | 0.12 | 0.08 | 0.43 | 0.39 | `cross_ema(day_skew(Amt), 60)` |
| slot b seed 3 | 过 | 0.39 | `pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 4` | 0.25 | 0.40 | 0.03 | 0.03 | 0.37 | 0.00 | `cross_ema(day_corr(Volume, abs_(Ret)), 60)` |
| slot b seed 4 | 过 | 0.33 | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1),` | 0.14 | 0.28 | 0.32 | 0.23 | 0.30 | 0.06 | `cross_ema(day_corr(Amt, Ret), 60)` |
| slot b seed 5 | 过 | 0.42 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.18 | 0.40 | 0.40 | 0.19 | 0.41 | 0.03 | `cross_ema(day_corr(Volume, in_delay(Ret, 1)), 60)` |
| slot b seed 6 | 过 | 0.59 | `abs_(ts_std(day_first(Amt), 50))` | 0.28 | 0.79 | 0.04 | 0.07 | 0.74 | 0.41 | `cross_ema(day_durbin_watson(Volume), 60)` |
| slot b seed 7 | 过 | 0.67 | `abs_(ts_std(day_first(Amt), 50))` | 0.33 | 0.76 | 0.16 | 0.04 | 0.73 | 0.29 | `cross_ema(day_q_stat_std(Volume), 60)` |
| slot b seed 8 | 过 | 0.57 | `abs_(ts_std(day_first(Amt), 50))` | 0.16 | 0.63 | 0.23 | 0.03 | 0.61 | 0.20 | `cross_ema(day_argmax(Volume), 60)` |
| slot b seed 9 | 过 | 0.29 | `abs_(ts_std(day_first(Amt), 50))` | 0.07 | 0.39 | 0.21 | 0.03 | 0.39 | 0.24 | `cross_stddev(day_argmax(Amt), 100)` |
| slot b seed 10 | 过 | 0.18 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.26 | 0.17 | 0.10 | 0.07 | 0.13 | 0.04 | `sub(cross_ema(day_kurt(Volume), 20), cross_ema(day_kurt(Volume), 120))` |
| slot b seed 11 | 过 | 0.11 | `pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 4` | 0.13 | 0.32 | 0.03 | 0.06 | 0.26 | 0.20 | `cross_stddev(day_kurt(Volume), 100)` |
| slot b seed 12 | 过 | 0.23 | `ts_mean(sub(day_ar1_coefficient(Amt), day_first(Volume)), 40` | 0.27 | 0.03 | 0.06 | 0.05 | 0.00 | 0.03 | `cross_autocorr_s1(day_corr(Volume, abs_(Ret)), 60)` |
| R 1 variant 1 | 过 | 0.44 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.36 | 0.02 | 0.15 | 0.06 | 0.05 | 0.21 | `cross_autocorr_s1(day_ar1_coefficient(Amt), 60)` |
| R 1 variant 2 | 过 | 0.71 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.69 | 0.14 | 0.22 | 0.03 | 0.16 | 0.17 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Volume)), 100)` |
| R 1 variant 3 | 过 | 0.63 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.59 | 0.12 | 0.21 | 0.02 | 0.14 | 0.19 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Volume)), 120)` |
| R 1 variant 4 | 过 | 0.99 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.99 | 0.20 | 0.25 | 0.06 | 0.22 | 0.12 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Amt)), 60)` |
| R 1 variant 5 | 过 | 1.00 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 1.00 | 0.20 | 0.25 | 0.06 | 0.22 | 0.12 | `cross_autocorr_s1(day_first(Volume), 60)` |
| R 1 variant 6 | 过 | 1.00 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 1.00 | 0.20 | 0.25 | 0.06 | 0.22 | 0.12 | `cross_autocorr_s1(sub(day_ar1_coefficient(Volume), day_first(Volume)), 60)` |
| R 1 variant 7 | 过 | 0.82 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.82 | 0.20 | 0.23 | 0.04 | 0.23 | 0.06 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), div(day_first(Volume), cross_mean(day_first(Volume), 30))), 60)` |
| R 1 variant 8 | 过 | 0.42 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.33 | 0.03 | 0.15 | 0.05 | 0.06 | 0.20 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), div(day_first(Amt), day_sum(Amt))), 60)` |
