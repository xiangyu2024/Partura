# 相关度表:种子 2023,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.05 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.10 | 0.00 | 0.01 | 0.18 | 0.00 | 0.04 | `day_sum(Ret)` |
| slot a seed 1 | 过 | 0.06 | `ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 10)` | 0.04 | 0.04 | 0.16 | 0.02 | 0.05 | 0.12 | `ts_skew(day_sum(Ret), 241)` |
| slot a seed 2 | 过 | 0.16 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.29 | 0.39 | 0.38 | 0.06 | 0.38 | 0.03 | `cross_regbeta(day_sum(Ret), cs_mean(day_sum(Ret)), 241)` |
| slot a seed 3 | 过 | 0.32 | `ts_max(day_quantile_q75(Volume), 40)` | 0.19 | 0.30 | 0.35 | 0.14 | 0.32 | 0.09 | `cross_regalpha(day_sum(Ret), cs_mean(day_sum(Ret)), 241)` |
| slot a seed 4 | 过 | 0.12 | `ts_stddev(day_quantile_q75(Volume), 10)` | 0.17 | 0.35 | 0.25 | 0.02 | 0.36 | 0.22 | `cross_corr(day_sum(Ret), cs_mean(day_sum(Ret)), 120)` |
| slot a seed 5 | 过 | 0.04 | `ts_max(day_quantile_q75(Volume), 40)` | 0.07 | 0.05 | 0.02 | 0.00 | 0.04 | 0.05 | `cross_autocorr(day_sum(Ret), 241, 1)` |
| slot a seed 6 | 过 | 0.02 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.04 | 0.01 | 0.06 | 0.02 | 0.01 | 0.03 | `cross_autocorr(day_sum(Ret), 120, 2)` |
| slot a seed 7 | 过 | 0.13 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.28 | 0.35 | 0.29 | 0.05 | 0.34 | 0.07 | `sub(cross_regbeta(day_sum(Ret), cs_mean(mul(day_sum(Ret), is_gt(day_sum(Ret), 0))), 241), cross_regbeta(day_sum(Ret), cs_mean(mul(day_sum(Ret), is_lt(day_sum(Ret), 0))), 241))` |
| slot a seed 8 | 过 | 0.04 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.05 | 0.12 | 0.13 | 0.01 | 0.12 | 0.01 | `cross_regbeta(day_sum(Ret), ts_delay(cs_mean(day_sum(Ret)), 1), 241)` |
| slot a seed 9 | 过 | 0.03 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.04 | 0.00 | 0.01 | 0.14 | 0.00 | 0.03 | `cross_regres(day_sum(Ret), cs_mean(day_sum(Ret)), 120)` |
| slot a seed 10 | 过 | 0.28 | `ts_max(day_quantile_q75(Volume), 40)` | 0.13 | 0.36 | 0.41 | 0.12 | 0.38 | 0.07 | `sub(cross_mean(mul(day_sum(Ret), is_gt(day_sum(Ret), 0)), 241), cross_mean(mul(neg(day_sum(Ret)), is_lt(day_sum(Ret), 0)), 241))` |
| slot a seed 11 | 过 | 0.21 | `ts_stddev(day_quantile_q75(Volume), 10)` | 0.10 | 0.30 | 0.39 | 0.10 | 0.32 | 0.03 | `div(cross_mean(mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0)), 241), add(cross_mean(pow_2(day_sum(Ret)), 241), 0.000001))` |
| slot a seed 12 | 过 | 0.04 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.03 | 0.11 | 0.10 | 0.01 | 0.11 | 0.01 | `cross_corr(day_sum(Ret), ts_delay(cs_mean(day_sum(Ret)), 1), 241)` |
| slot a seed 13 | 过 | 0.15 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.31 | 0.39 | 0.36 | 0.06 | 0.38 | 0.04 | `cross_regbeta(day_sum(Ret), mul(cs_mean(day_sum(Ret)), is_lt(cs_mean(day_sum(Ret)), 0)), 241)` |
| slot a seed 14 | 过 | 0.08 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.09 | 0.19 | 0.24 | 0.02 | 0.21 | 0.02 | `cross_corr(pow_2(day_sum(Ret)), cs_mean(pow_2(day_sum(Ret))), 120)` |
| slot a seed 15 | 过 | 0.04 | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), da` | 0.08 | 0.11 | 0.01 | 0.00 | 0.10 | 0.04 | `ts_skew(cross_regres(day_sum(Ret), cs_mean(day_sum(Ret)), 60), 241)` |
| slot b seed 1 | 过 | 0.30 | `ts_max(day_quantile_q75(Volume), 40)` | 0.48 | 0.03 | 0.58 | 0.01 | 0.09 | 0.18 | `cross_mean(day_wmean(Ret, is_gt(Ret, 0)), 241)` |
| slot b seed 2 | 过 | 0.33 | `ts_max(day_quantile_q75(Volume), 40)` | 0.52 | 0.01 | 0.57 | 0.02 | 0.07 | 0.12 | `cross_mean(day_wmean(Ret, is_lt(Ret, 0)), 241)` |
| slot b seed 3 | 过 | 0.14 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.16 | 0.26 | 0.31 | 0.02 | 0.26 | 0.21 | `cross_mean(add(day_wmean(Ret, is_gt(Ret, 0)), day_wmean(Ret, is_lt(Ret, 0))), 241)` |
| slot b seed 4 | 过 | 0.15 | `ts_max(day_quantile_q75(Volume), 40)` | 0.38 | 0.23 | 0.12 | 0.03 | 0.22 | 0.18 | `cross_mean(div(day_wmean(Ret, is_gt(Ret, 0)), sub(0.000001, day_wmean(Ret, is_lt(Ret, 0)))), 241)` |
| slot b seed 5 | 过 | 0.25 | `ts_max(day_quantile_q75(Volume), 40)` | 0.76 | 0.42 | 0.01 | 0.07 | 0.35 | 0.20 | `cross_mean(day_pos_ratio(Ret), 241)` |
| slot b seed 6 | 过 | 0.26 | `ts_max(day_quantile_q75(Volume), 40)` | 0.76 | 0.42 | 0.01 | 0.08 | 0.35 | 0.18 | `cross_mean(day_zero_ratio(Ret), 241)` |
| slot b seed 7 | 过 | 0.42 | `ts_max(day_quantile_q75(Volume), 40)` | 0.79 | 0.26 | 0.01 | 0.08 | 0.19 | 0.06 | `cross_mean(div(day_wmean(Ret, is_gt(Ret, 0)), add(day_std(Ret), 0.000001)), 241)` |
| slot b seed 8 | 过 | 0.12 | `ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 10)` | 0.04 | 0.21 | 0.04 | 0.03 | 0.20 | 0.19 | `cross_mean(div(day_sum(mul(pow_2(Ret), is_gt(Ret, 0))), add(day_sum(pow_2(Ret)), 0.000000001)), 241)` |
| slot b seed 9 | 过 | 0.18 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.32 | 0.03 | 0.31 | 0.02 | 0.07 | 0.38 | `cross_mean(sub(day_wstd(Ret, is_gt(Ret, 0)), day_wstd(Ret, is_lt(Ret, 0))), 241)` |
| slot b seed 10 | 过 | 0.20 | `ts_max(day_quantile_q75(Volume), 40)` | 0.40 | 0.01 | 0.60 | 0.01 | 0.06 | 0.32 | `cross_mean(day_wmean(Ret, mul(Volume, is_gt(Ret, 0))), 241)` |
| slot b seed 11 | 过 | 0.22 | `ts_max(day_quantile_q75(Volume), 40)` | 0.40 | 0.01 | 0.63 | 0.01 | 0.07 | 0.27 | `cross_mean(sub(day_wmean(Ret, mul(Volume, is_gt(Ret, 0))), day_wmean(Ret, mul(Volume, is_lt(Ret, 0)))), 241)` |
| slot b seed 12 | 过 | 0.32 | `ts_max(day_quantile_q75(Volume), 40)` | 0.51 | 0.04 | 0.61 | 0.02 | 0.11 | 0.17 | `cross_ema(sub(day_wmean(Ret, is_gt(Ret, 0)), day_mean(Ret)), 120)` |
| slot b seed 13 | 过 | 0.35 | `ts_max(day_quantile_q75(Volume), 40)` | 0.47 | 0.13 | 0.54 | 0.02 | 0.19 | 0.05 | `cs_bucket_zscore(cross_mean(day_wmean(Ret, is_gt(Ret, 0)), 241), LogFloatCap)` |
| slot b seed 14 | 过 | 0.14 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.14 | 0.21 | 0.66 | 0.04 | 0.24 | 0.18 | `cross_mean(day_wmean(Ret, is_gt(Ret, day_quantile(Ret, 0.9))), 241)` |
| slot b seed 15 | 过 | 0.25 | `ts_max(day_quantile_q75(Volume), 40)` | 0.17 | 0.14 | 0.23 | 0.09 | 0.18 | 0.02 | `cross_mean(day_wmean(Ret, log(abs_(Ret))), 241)` |
| slot b seed 16 | 过 | 0.16 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.17 | 0.12 | 0.33 | 0.04 | 0.15 | 0.30 | `cross_mean(day_wmean(Ret, sqrt(abs_(Ret))), 241)` |
| R 1 variant 1 | 过 | 0.78 | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), da` | 0.81 | 0.17 | 0.04 | 0.03 | 0.15 | 0.02 | `cs_demean(cross_mean(cross_corr(day_autocorr_n1(High), day_median(Close), 241), 30))` |
| R 1 variant 2 | 过 | 0.09 | `ts_stddev(day_quantile_q75(Volume), 10)` | 0.08 | 0.17 | 0.25 | 0.00 | 0.19 | 0.23 | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_sum(Ret), 241), 30))` |
| R 1 variant 3 | 过 | 0.21 | `ts_max(day_quantile_q75(Volume), 40)` | 0.09 | 0.26 | 0.40 | 0.08 | 0.27 | 0.06 | `cs_demean(cross_mean(cross_regres(day_autocorr_n1(High), day_median(Close), 241), 30))` |
| R 1 variant 4 | 过 | 0.91 | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), da` | 0.91 | 0.04 | 0.04 | 0.01 | 0.04 | 0.01 | `cs_demean(cross_ema(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 30))` |
| R 1 variant 5 | 过 | 0.91 | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), da` | 0.94 | 0.05 | 0.03 | 0.01 | 0.05 | 0.00 | `cross_regbeta(day_autocorr_n1(High), day_median(Close), 241)` |
