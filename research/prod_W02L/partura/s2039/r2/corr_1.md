# 相关度表:种子 2039,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_open(cross_sum(log(Amt), 3))` | 1.00 | 0.78 | 0.30 | 0.25 | 0.80 | 0.52 | `day_first(cross_sum(log(Amt), 3))` |
| slot a seed 1 | 过 | 0.55 | `day_open(cross_sum(log(Amt), 3))` | 0.13 | 0.15 | 0.37 | 0.38 | 0.18 | 0.01 | `sub(day_first(cross_sum(log(Amt), 3)), cross_ema(day_first(cross_sum(log(Amt), 3)), 120))` |
| slot a seed 2 | 过 | 0.46 | `day_open(cross_sum(log(Amt), 3))` | 0.32 | 0.01 | 0.19 | 0.42 | 0.02 | 0.02 | `cross_zscore(day_first(cross_sum(log(Amt), 3)), 60)` |
| slot a seed 3 | 过 | 0.38 | `day_open(cross_sum(log(Amt), 3))` | 0.29 | 0.03 | 0.09 | 0.42 | 0.02 | 0.03 | `sub(day_first(cross_sum(log(Amt), 3)), cross_delay(day_first(cross_sum(log(Amt), 3)), 20))` |
| slot a seed 4 | 过 | 0.39 | `day_open(cross_sum(log(Amt), 3))` | 0.66 | 0.08 | 0.15 | 0.16 | 0.02 | 0.14 | `sub(day_first(cross_sum(log(Amt), 3)), day_mean(cross_sum(log(Amt), 3)))` |
| slot a seed 5 | 过 | 0.64 | `day_open(cross_sum(log(Amt), 3))` | 0.78 | 0.17 | 0.20 | 0.20 | 0.23 | 0.06 | `sub(day_first(cross_sum(log(Amt), 3)), day_quantile_q75(cross_sum(log(Amt), 3)))` |
| slot a seed 6 | 过 | 0.70 | `day_open(cross_sum(log(Amt), 3))` | 0.68 | 0.31 | 0.21 | 0.21 | 0.34 | 0.21 | `sub(day_first(cross_sum(log(Amt), 3)), day_last(cross_sum(log(Amt), 3)))` |
| slot a seed 7 | 过 | 0.32 | `day_open(cross_sum(log(Amt), 3))` | 0.62 | 0.13 | 0.10 | 0.14 | 0.07 | 0.16 | `cs_bucket_demean(day_first(cross_sum(log(Amt), 3)), day_mean(cross_sum(log(Amt), 3)))` |
| slot a seed 8 | 过 | 0.16 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt),` | 0.20 | 0.11 | 0.24 | 0.36 | 0.14 | 0.01 | `ts_regres(day_first(cross_sum(log(Amt), 3)), day_mean(cross_sum(log(Amt), 3)), 60)` |
| slot a seed 9 | 过 | 0.67 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.53 | 0.35 | 0.05 | 0.03 | 0.30 | 0.11 | `sub(day_first(cross_sum(log(Amt), 3)), day_first(cross_sum(log(Volume), 3)))` |
| slot a seed 10 | 过 | 0.75 | `day_open(cross_sum(log(Amt), 3))` | 0.80 | 0.43 | 0.38 | 0.24 | 0.46 | 0.08 | `cs_bucket_demean(day_first(cross_sum(log(Amt), 3)), LogFloatCap)` |
| slot a seed 11 | 过 | 0.38 | `day_open(cross_sum(log(Amt), 3))` | 0.67 | 0.09 | 0.15 | 0.17 | 0.03 | 0.13 | `mul(sub(day_first(cross_sum(log(Amt), 3)), day_mean(cross_sum(log(Amt), 3))), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot a seed 12 | 过 | 0.04 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.07 | 0.01 | 0.03 | 0.01 | 0.00 | 0.02 | `cross_corr(day_first(cross_sum(log(Amt), 3)), day_mean(Ret), 60)` |
| slot a seed 13 | 过 | 0.54 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.64 | 0.10 | 0.17 | 0.03 | 0.17 | 0.05 | `cross_ema(sub(day_first(cross_sum(log(Amt), 3)), day_mean(cross_sum(log(Amt), 3))), 60)` |
| slot a seed 14 | 过 | 0.77 | `day_open(cross_sum(log(Amt), 3))` | 0.86 | 0.88 | 0.28 | 0.07 | 0.89 | 0.59 | `sub(day_first(cross_sum(log(Amt), 3)), day_first(cross_sum(log(Amt), 20)))` |
| slot a seed 15 | 过 | 0.54 | `day_open(cross_sum(log(Amt), 3))` | 0.13 | 0.14 | 0.36 | 0.36 | 0.18 | 0.04 | `cs_bucket_demean(sub(day_first(cross_sum(log(Amt), 3)), cross_ema(day_first(cross_sum(log(Amt), 3)), 120)), LogFloatCap)` |
| slot b seed 1 | 过 | 0.45 | `day_open(cross_sum(log(Amt), 3))` | 0.40 | 0.50 | 0.39 | 0.00 | 0.52 | 0.05 | `cross_ema(day_centroid(Amt), 60)` |
| slot b seed 2 | 过 | 0.15 | `day_open(cross_sum(log(Amt), 3))` | 0.19 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Amt), 120)` |
| slot b seed 3 | 过 | 0.64 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.40 | 0.75 | 0.15 | 0.07 | 0.67 | 0.64 | `cross_ema(day_gini(Amt), 60)` |
| slot b seed 4 | 过 | 0.29 | `day_open(cross_sum(log(Amt), 3))` | 0.13 | 0.23 | 0.38 | 0.19 | 0.27 | 0.01 | `sub(cross_ema(day_centroid(Amt), 20), cross_ema(day_centroid(Amt), 120))` |
| slot b seed 5 | 过 | 0.29 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.33 | 0.16 | 0.28 | 0.25 | 0.19 | 0.31 | `cross_ema(day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 6 | 过 | 0.24 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.23 | 0.15 | 0.49 | 0.16 | 0.20 | 0.21 | `cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60)` |
| slot b seed 7 | 过 | 0.33 | `day_open(cross_sum(log(Amt), 3))` | 0.20 | 0.45 | 0.46 | 0.10 | 0.44 | 0.08 | `cross_ema(day_topw_mean(Ret, Amt), 120)` |
| slot b seed 8 | 过 | 0.31 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.28 | 0.17 | 0.76 | 0.01 | 0.22 | 0.31 | `cross_ema(div(day_wstd(Ret, Amt), replace_small_with_nan(is_gt(day_std(Ret), 0.0001))), 60)` |
| slot b seed 9 | 过 | 0.13 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40` | 0.10 | 0.13 | 0.21 | 0.06 | 0.15 | 0.04 | `cross_corr(day_centroid(Amt), day_wmean(Ret, Amt), 60)` |
| slot b seed 10 | 过 | 0.18 | `day_open(cross_sum(log(Amt), 3))` | 0.18 | 0.15 | 0.24 | 0.28 | 0.16 | 0.10 | `cross_ema(sub(day_centroid(Amt), day_centroid(Volume)), 60)` |
| slot b seed 11 | 过 | 0.58 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.32 | 0.81 | 0.02 | 0.07 | 0.73 | 0.63 | `cross_tail_mean_q25(day_gini(Amt), 60)` |
| slot b seed 12 | 过 | 0.45 | `day_open(cross_sum(log(Amt), 3))` | 0.42 | 0.49 | 0.38 | 0.00 | 0.51 | 0.08 | `mul(cross_ema(day_centroid(Amt), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 13 | 过 | 0.29 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.35 | 0.21 | 0.26 | 0.17 | 0.23 | 0.37 | `cross_ema(day_signed_ratio(Ret, Volume), 120)` |
| slot b seed 14 | 过 | 0.45 | `day_open(cross_sum(log(Amt), 3))` | 0.40 | 0.49 | 0.39 | 0.00 | 0.52 | 0.03 | `cs_bucket_demean(cross_ema(day_centroid(Amt), 60), LogFloatCap)` |
| slot b seed 15 | 过 | 0.77 | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` | 0.56 | 0.51 | 0.16 | 0.07 | 0.41 | 0.46 | `cross_ema(day_es_ratio_hi(Amt), 60)` |
| R 1 variant 1 | 过 | 0.67 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt),` | 0.62 | 0.60 | 0.17 | 0.05 | 0.60 | 0.36 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 150)))` |
| R 1 variant 2 | 过 | 0.59 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt),` | 0.48 | 0.59 | 0.16 | 0.04 | 0.59 | 0.35 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 241)))` |
| R 1 variant 3 | 过 | 0.76 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt),` | 0.77 | 0.62 | 0.19 | 0.06 | 0.62 | 0.37 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 100)))` |
| R 1 variant 4 | 过 | 0.59 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt),` | 0.69 | 0.61 | 0.19 | 0.04 | 0.61 | 0.35 | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 6)), day_last(cross_sum(Amt, 6)), 100)))` |
| R 2 variant 1 | 过 | 0.89 | `day_open(cross_sum(log(Amt), 3))` | 0.95 | 0.85 | 0.31 | 0.20 | 0.87 | 0.57 | `day_first(cross_sum(log(Amt), 10))` |
| R 2 variant 2 | 过 | 0.82 | `day_open(cross_sum(log(Amt), 3))` | 0.89 | 0.89 | 0.29 | 0.10 | 0.90 | 0.60 | `day_first(cross_sum(log(Amt), 20))` |
| R 2 variant 3 | 过 | 0.72 | `day_open(cross_sum(log(Amt), 3))` | 0.76 | 0.84 | 0.13 | 0.03 | 0.82 | 0.65 | `day_first(cross_sum(log(Amt), 60))` |
| R 2 variant 4 | 过 | 0.80 | `day_open(cross_sum(log(Amt), 3))` | 0.81 | 0.91 | 0.20 | 0.00 | 0.91 | 0.63 | `cross_ema(day_first(cross_sum(log(Amt), 3)), 20)` |
| R 2 variant 5 | 过 | 0.72 | `day_open(cross_sum(log(Amt), 3))` | 0.63 | 0.85 | 0.07 | 0.05 | 0.83 | 0.65 | `cross_ema(day_first(cross_sum(log(Amt), 3)), 60)` |
| R 2 variant 6 | 过 | 0.81 | `day_open(cross_sum(log(Amt), 3))` | 0.71 | 0.95 | 0.29 | 0.02 | 0.95 | 0.60 | `day_first(cross_ema(log(Amt), 20))` |
