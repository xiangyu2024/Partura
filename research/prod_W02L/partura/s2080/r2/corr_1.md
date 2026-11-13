# 相关度表:种子 2080,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.47 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.27 | 0.52 | 0.25 | 0.09 | 0.54 | 0.26 | `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)` |
| slot a seed 1 | 过 | 0.47 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.27 | 0.52 | 0.25 | 0.09 | 0.54 | 0.26 | `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)` |
| slot a seed 2 | 过 | 0.20 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.24 | 0.19 | 0.26 | 0.17 | 0.21 | 0.04 | `cross_zscore(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 120)` |
| slot a seed 3 | 过 | 0.57 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.39 | 0.54 | 0.21 | 0.03 | 0.56 | 0.29 | `cross_ema(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 10)` |
| slot a seed 4 | 过 | 0.18 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.29 | 0.10 | 0.20 | 0.08 | 0.12 | 0.02 | `sub(cross_mean(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 20), cross_mean(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 120))` |
| slot a seed 5 | 过 | 0.20 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.24 | 0.19 | 0.26 | 0.17 | 0.21 | 0.04 | `div(sub(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), cross_mean(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 120)), cross_stddev(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 120))` |
| slot a seed 6 | 过 | 0.61 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.46 | 0.52 | 0.16 | 0.02 | 0.52 | 0.29 | `cross_mean(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 60)` |
| slot a seed 7 | 过 | 0.07 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.09 | 0.02 | 0.06 | 0.11 | 0.03 | 0.02 | `cross_regbeta(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), cross_ema(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 5), 60)` |
| slot a seed 8 | 过 | 0.17 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.19 | 0.15 | 0.21 | 0.17 | 0.18 | 0.03 | `cross_zscore(cross_ema(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 5), 60)` |
| slot a seed 9 | 过 | 0.11 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.07 | 0.16 | 0.09 | 0.01 | 0.17 | 0.09 | `sub(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), ts_cov(cs_normalize(day_mean(Volume)), day_close(Low), 50))` |
| slot a seed 10 | 过 | 0.06 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.08 | 0.05 | 0.05 | 0.01 | 0.06 | 0.00 | `cross_corr(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), cs_normalize(day_sum(Ret)), 60)` |
| slot a seed 11 | 过 | 0.09 | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 2` | 0.06 | 0.14 | 0.23 | 0.47 | 0.16 | 0.07 | `mul(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 12 | 废品 | 0.16 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.27 | 0.20 | 0.24 | 0.11 | 0.22 | 0.04 | `cross_rank(cross_ema(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 20), 60)` |
| slot b seed 1 | 过 | 0.09 | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 2` | 0.07 | 0.13 | 0.15 | 0.01 | 0.14 | 0.13 | `cross_corr(day_signed_ratio(Ret, Amt), day_centroid(Amt), 60)` |
| slot b seed 2 | 过 | 0.09 | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 2` | 0.07 | 0.13 | 0.14 | 0.02 | 0.14 | 0.14 | `cross_regbeta(day_centroid(Amt), day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 3 | 过 | 0.10 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.08 | 0.10 | 0.01 | 0.60 | 0.09 | 0.03 | `sub(cross_mean(day_signed_ratio(Ret, Amt), 20), cross_mean(day_signed_ratio(Ret, Amt), 120))` |
| slot b seed 4 | 过 | 0.06 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.18 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Amt), 120)` |
| slot b seed 5 | 过 | 0.12 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.23 | 0.13 | 0.29 | 0.28 | 0.17 | 0.02 | `sub(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 120))` |
| slot b seed 6 | 过 | 0.12 | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 2` | 0.20 | 0.07 | 0.23 | 0.44 | 0.09 | 0.20 | `cross_ema(mul(day_signed_ratio(Ret, Amt), day_centroid(Amt)), 20)` |
| slot b seed 7 | 过 | 0.21 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ` | 0.11 | 0.25 | 0.18 | 0.02 | 0.28 | 0.06 | `cross_corr(day_gini(Amt), day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 8 | 过 | 0.05 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.05 | 0.00 | 0.02 | 0.00 | 0.01 | 0.02 | `cross_zscore(cross_corr(day_signed_ratio(Ret, Amt), day_centroid(Amt), 40), 120)` |
| slot b seed 9 | 过 | 0.52 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.31 | 0.64 | 0.56 | 0.01 | 0.62 | 0.13 | `cross_regbeta(day_signed_ratio(Ret, Amt), day_sum(Ret), 60)` |
| slot b seed 10 | 过 | 0.11 | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 2` | 0.22 | 0.12 | 0.28 | 0.29 | 0.14 | 0.22 | `cross_mean(day_signed_ratio(Ret, Volume), 60)` |
| slot b seed 11 | 过 | 0.02 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_mask` | 0.09 | 0.03 | 0.04 | 0.12 | 0.03 | 0.01 | `cross_zscore(day_signed_ratio(Ret, Amt), 60)` |
| R 1 variant 1 | 过 | 0.80 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.71 | 0.04 | 0.41 | 0.06 | 0.09 | 0.30 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 25)` |
| R 1 variant 2 | 过 | 0.92 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.90 | 0.00 | 0.36 | 0.03 | 0.04 | 0.32 | `ts_std(neg(neg(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241))), 50)` |
| R 1 variant 3 | 废品 | 0.66 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.52 | 0.05 | 0.40 | 0.11 | 0.09 | 0.24 | `ts_std(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241), 25)` |
| R 1 variant 4 | 废品 | 0.58 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.42 | 0.06 | 0.40 | 0.15 | 0.10 | 0.20 | `ts_std(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241), 20)` |
| R 1 variant 5 | 过 | 0.74 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.62 | 0.05 | 0.42 | 0.08 | 0.10 | 0.28 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 5), 241), 25)` |
| R 1 variant 6 | 过 | 0.52 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.30 | 0.05 | 0.43 | 0.06 | 0.09 | 0.32 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 120), 25)` |
| R 1 variant 7 | 废品 | 0.44 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.22 | 0.05 | 0.42 | 0.10 | 0.09 | 0.27 | `ts_std(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 120), 25)` |
| R 1 variant 8 | 废品 | 0.78 | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret)` | 0.69 | 0.04 | 0.39 | 0.06 | 0.08 | 0.27 | `ts_std(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241), 35)` |
