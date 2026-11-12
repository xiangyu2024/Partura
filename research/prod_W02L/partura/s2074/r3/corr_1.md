# 相关度表:种子 2074,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.52 | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` | 0.25 | 0.53 | 0.13 | 0.10 | 0.54 | 0.48 | `cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret))` |
| slot a seed 1 | 过 | 0.66 | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` | 0.17 | 0.72 | 0.14 | 0.03 | 0.73 | 0.58 | `cross_mean(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), 60)` |
| slot a seed 2 | 过 | 0.19 | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 3)))` | 0.14 | 0.04 | 0.15 | 0.20 | 0.01 | 0.01 | `cross_zscore(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), 120)` |
| slot a seed 3 | 过 | 0.25 | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` | 0.10 | 0.23 | 0.21 | 0.09 | 0.23 | 0.09 | `cross_corr(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), day_sum(Ret), 60)` |
| slot a seed 4 | 过 | 0.49 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 5` | 0.21 | 0.47 | 0.17 | 0.04 | 0.47 | 0.22 | `cross_corr(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 5 | 过 | 0.28 | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 3)))` | 0.29 | 0.03 | 0.01 | 0.29 | 0.02 | 0.07 | `cross_regres(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), day_std(Ret), 60)` |
| slot a seed 6 | 过 | 0.18 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.19 | 0.11 | 0.13 | 0.32 | 0.09 | 0.05 | `sub(cross_mean(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), 10), cross_mean(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), 60))` |
| slot a seed 7 | 过 | 0.37 | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` | 0.17 | 0.32 | 0.30 | 0.07 | 0.37 | 0.04 | `cs_bucket_zscore(cross_mean(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), 20), LogFloatCap)` |
| slot a seed 8 | 过 | 0.71 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 5` | 0.31 | 0.77 | 0.01 | 0.04 | 0.75 | 0.49 | `cross_corr(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), day_std(Amt), 120)` |
| slot a seed 9 | 过 | 0.02 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.04 | 0.01 | 0.02 | 0.00 | 0.02 | 0.03 | `cross_corr(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), day_close(Ret), 120)` |
| slot a seed 10 | 过 | 0.04 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.05 | 0.04 | 0.01 | 0.00 | 0.04 | 0.01 | `cross_regbeta(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), day_close(Ret), 60)` |
| slot a seed 11 | 过 | 0.14 | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 3)))` | 0.16 | 0.02 | 0.23 | 0.27 | 0.06 | 0.01 | `cross_ema(cross_zscore(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), 60), 10)` |
| slot a seed 12 | 过 | 0.72 | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` | 0.29 | 0.76 | 0.21 | 0.07 | 0.77 | 0.59 | `div(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), cross_mean(day_topw_mean(Amt, Amt), 120))` |
| slot b seed 1 | 过 | 0.07 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 5` | 0.03 | 0.06 | 0.00 | 0.01 | 0.06 | 0.02 | `cross_regbeta(day_sum(Ret), cross_delay(day_close(Ret), 1), 60)` |
| slot b seed 2 | 过 | 0.07 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 5` | 0.03 | 0.06 | 0.00 | 0.00 | 0.06 | 0.03 | `cross_regbeta(day_sum(Ret), cross_delay(day_close(Ret), 1), 120)` |
| slot b seed 3 | 过 | 0.03 | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` | 0.01 | 0.03 | 0.00 | 0.00 | 0.03 | 0.02 | `cross_corr(day_sum(Ret), cross_delay(day_close(Ret), 1), 60)` |
| slot b seed 4 | 过 | 0.14 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.17 | 0.08 | 0.10 | 0.02 | 0.08 | 0.04 | `cross_corr(day_close(Ret), day_sum(Ret), 60)` |
| slot b seed 5 | 过 | 0.17 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.18 | 0.09 | 0.07 | 0.00 | 0.08 | 0.05 | `cross_corr(day_close(Ret), day_sum(Ret), 120)` |
| slot b seed 6 | 过 | 0.01 | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` | 0.02 | 0.01 | 0.01 | 0.00 | 0.01 | 0.01 | `cross_corr(day_close(Ret), cross_delay(day_close(Ret), 1), 60)` |
| slot b seed 7 | 过 | 0.03 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 5` | 0.04 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | `cross_regbeta(day_close(Ret), cross_delay(day_sum(Ret), 1), 60)` |
| slot b seed 8 | 过 | 0.24 | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` | 0.14 | 0.23 | 0.27 | 0.10 | 0.25 | 0.09 | `cross_mean(sub(day_close(Ret), day_topw_mean(Ret, Amt)), 60)` |
| slot b seed 9 | 过 | 0.01 | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` | 0.01 | 0.01 | 0.01 | 0.00 | 0.01 | 0.01 | `cross_zscore(cross_regbeta(day_sum(Ret), cross_delay(day_close(Ret), 1), 60), 120)` |
| slot b seed 10 | 过 | 0.02 | `pow_2(day_close(neg(Volume)))` | 0.08 | 0.01 | 0.01 | 0.04 | 0.01 | 0.00 | `cross_regres(day_sum(Ret), cross_delay(day_close(Ret), 1), 60)` |
| slot b seed 11 | 过 | 0.06 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 5` | 0.05 | 0.05 | 0.02 | 0.01 | 0.04 | 0.02 | `cross_corr(day_close(Ret), day_std(Ret), 60)` |
| slot b seed 12 | 过 | 0.12 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.14 | 0.04 | 0.06 | 0.01 | 0.03 | 0.01 | `cross_corr(day_close(Ret), day_topw_mean(Ret, Amt), 60)` |
