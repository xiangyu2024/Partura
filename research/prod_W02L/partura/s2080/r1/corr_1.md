# 相关度表:种子 2080,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.32 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.23 | 0.47 | 0.23 | 0.21 | 0.47 | 0.18 | `day_q_stat_std(Volume)` |
| slot a seed 1 | 过 | 0.14 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.36 | 0.03 | 0.17 | 0.27 | 0.05 | 0.01 | `cross_zscore(day_q_stat_std(Volume), 120)` |
| slot a seed 2 | 过 | 0.15 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.27 | 0.12 | 0.34 | 0.41 | 0.16 | 0.05 | `sub(cross_mean(day_q_stat_std(Volume), 10), cross_mean(day_q_stat_std(Volume), 120))` |
| slot a seed 3 | 过 | 0.17 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.33 | 0.22 | 0.35 | 0.37 | 0.26 | 0.08 | `cross_ema(div(day_q_stat_std(Volume), cross_mean(day_q_stat_std(Volume), 60)), 10)` |
| slot a seed 4 | 过 | 0.23 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.09 | 0.29 | 0.07 | 0.03 | 0.27 | 0.24 | `cross_corr(day_q_stat_std(Volume), abs_(day_sum(Ret)), 60)` |
| slot a seed 5 | 过 | 0.08 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.12 | 0.01 | 0.05 | 0.07 | 0.01 | 0.04 | `cross_corr(day_q_stat_std(Volume), day_max(Ret), 60)` |
| slot a seed 6 | 过 | 0.10 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.14 | 0.02 | 0.03 | 0.07 | 0.01 | 0.13 | `cross_corr(day_q_stat_std(Volume), day_std(Ret), 60)` |
| slot a seed 7 | 过 | 0.08 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.09 | 0.27 | 0.21 | 0.02 | 0.24 | 0.30 | `cross_regbeta(day_std(Ret), day_q_stat_std(Volume), 60)` |
| slot a seed 8 | 过 | 0.17 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.10 | 0.18 | 0.13 | 0.02 | 0.17 | 0.14 | `cross_regbeta(abs_(day_sum(Ret)), day_q_stat_std(Volume), 60)` |
| slot a seed 9 | 过 | 0.50 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.24 | 0.77 | 0.39 | 0.16 | 0.77 | 0.27 | `sub(cross_mean(day_q_stat_std(Volume), 20), cross_mean(day_ar1_coefficient(Volume), 20))` |
| slot a seed 10 | 过 | 0.25 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.15 | 0.26 | 0.01 | 0.03 | 0.24 | 0.20 | `cross_corr(day_q_stat_std(Volume), day_ar1_coefficient(Volume), 60)` |
| slot a seed 11 | 过 | 0.16 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.39 | 0.03 | 0.09 | 0.26 | 0.01 | 0.01 | `cross_zscore(sub(day_q_stat_std(Volume), day_ar1_coefficient(Volume)), 60)` |
| slot a seed 12 | 过 | 0.06 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.11 | 0.01 | 0.00 | 0.06 | 0.01 | 0.02 | `mul(cross_zscore(day_q_stat_std(Volume), 120), sign(cross_mean(day_sum(Ret), 20)))` |
| slot b seed 1 | 过 | 0.09 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_mask` | 0.12 | 0.03 | 0.15 | 0.03 | 0.02 | 0.08 | `cross_corr(day_ar1_coefficient(Ret), day_ar1_coefficient(Volume), 60)` |
| slot b seed 2 | 过 | 0.03 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_mask` | 0.07 | 0.03 | 0.14 | 0.01 | 0.03 | 0.08 | `cross_regbeta(day_ar1_coefficient(Volume), day_ar1_coefficient(Ret), 60)` |
| slot b seed 3 | 过 | 0.12 | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_mask` | 0.14 | 0.03 | 0.12 | 0.04 | 0.02 | 0.10 | `cross_corr(day_ar1_coefficient(Ret), day_ar1_coefficient(Volume), 120)` |
| slot b seed 4 | 过 | 0.18 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.13 | 0.13 | 0.15 | 0.02 | 0.13 | 0.07 | `cross_corr(day_ar1_coefficient(Ret), day_q_stat_std(Volume), 60)` |
| slot b seed 5 | 过 | 0.08 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.12 | 0.01 | 0.01 | 0.06 | 0.00 | 0.09 | `cross_corr(day_durbin_watson(Vwap), day_ar1_coefficient(Volume), 60)` |
| slot b seed 6 | 过 | 0.20 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.10 | 0.19 | 0.01 | 0.09 | 0.17 | 0.12 | `cross_corr(day_skew(Ret), day_ar1_coefficient(Volume), 60)` |
| slot b seed 7 | 过 | 0.28 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.14 | 0.38 | 0.24 | 0.01 | 0.38 | 0.08 | `cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40)` |
| slot b seed 8 | 过 | 0.01 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.02 | 0.01 | 0.06 | 0.01 | 0.01 | 0.01 | `cross_zscore(cross_corr(day_ar1_coefficient(Ret), day_ar1_coefficient(Volume), 40), 120)` |
| slot b seed 9 | 过 | 0.30 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` | 0.08 | 0.63 | 0.47 | 0.16 | 0.67 | 0.32 | `sub(cross_mean(day_ar1_coefficient(Ret), 20), cross_mean(day_ar1_coefficient(Volume), 20))` |
| slot b seed 10 | 废品 | nan | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow` | 0.00 | nan | nan | nan | nan | nan | `cross_corr(day_open(Ret), day_ar1_coefficient(Volume), 60)` |
