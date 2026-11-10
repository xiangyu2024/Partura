# 相关度表:种子 2001,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `pow_1_5(day_max(Volume))` | 1.00 | 0.49 | 0.23 | 0.19 | 0.54 | 0.47 | `day_max(Volume)` |
| slot a seed 1 | 过 | 0.47 | `pow_1_5(day_max(Volume))` | 0.08 | 0.07 | 0.19 | 0.33 | 0.10 | 0.05 | `cross_zscore(log(day_max(Volume)), 120)` |
| slot a seed 2 | 过 | 0.28 | `pow_1_5(day_max(Volume))` | 0.05 | 0.16 | 0.35 | 0.41 | 0.21 | 0.07 | `sub(cross_mean(log(day_max(Volume)), 10), cross_mean(log(day_max(Volume)), 120))` |
| slot a seed 3 | 过 | 0.26 | `pow_1_5(day_max(Volume))` | 0.08 | 0.13 | 0.30 | 0.38 | 0.19 | 0.08 | `cross_ema(div(day_max(Volume), cross_mean(day_max(Volume), 60)), 10)` |
| slot a seed 4 | 过 | 0.06 | `pow_1_5(day_max(Volume))` | 0.13 | 0.65 | 0.12 | 0.10 | 0.54 | 0.41 | `cross_mean(div(day_max(Volume), day_sum(Volume)), 20)` |
| slot a seed 5 | 过 | 0.22 | `pow_1_5(day_max(Volume))` | 0.09 | 0.06 | 0.09 | 0.06 | 0.07 | 0.01 | `cross_regres(log(day_sum(Volume)), log(day_max(Volume)), 60)` |
| slot a seed 6 | 过 | 0.24 | `pow_1_5(day_max(Volume))` | 0.12 | 0.28 | 0.13 | 0.03 | 0.31 | 0.00 | `cross_regbeta(log(day_sum(Volume)), log(day_max(Volume)), 60)` |
| slot a seed 7 | 过 | 0.21 | `pow_1_5(day_max(Volume))` | 0.55 | 0.48 | 0.17 | 0.11 | 0.37 | 0.23 | `cs_regres(cross_mean(log(day_max(Volume)), 20), cross_mean(log(day_sum(Volume)), 20))` |
| slot a seed 8 | 过 | 0.12 | `pow_1_5(day_max(Volume))` | 0.09 | 0.09 | 0.11 | 0.05 | 0.10 | 0.01 | `cross_corr(day_max(Volume), abs_(day_sum(Ret)), 60)` |
| slot a seed 9 | 过 | 0.13 | `pow_1_5(day_max(Volume))` | 0.10 | 0.09 | 0.15 | 0.10 | 0.10 | 0.00 | `cross_corr(day_max(Volume), day_sum(Ret), 60)` |
| slot a seed 10 | 过 | 0.12 | `pow_1_5(day_max(Volume))` | 0.11 | 0.11 | 0.18 | 0.08 | 0.12 | 0.09 | `cross_corr(day_max(Volume), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 11 | 过 | 0.20 | `pow_1_5(day_max(Volume))` | 0.23 | 0.11 | 0.14 | 0.04 | 0.13 | 0.10 | `cross_corr(day_max(Volume), day_max(Ret), 60)` |
| slot a seed 12 | 过 | 0.13 | `pow_1_5(day_max(Volume))` | 0.17 | 0.13 | 0.09 | 0.02 | 0.14 | 0.11 | `cross_corr(day_max(Volume), day_std(Ret), 60)` |
| slot a seed 13 | 过 | 0.11 | `pow_1_5(day_max(Volume))` | 0.09 | 0.01 | 0.01 | 0.07 | 0.02 | 0.01 | `mul(cross_zscore(log(day_max(Volume)), 120), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 14 | 过 | 0.29 | `pow_1_5(day_max(Volume))` | 0.50 | 0.57 | 0.08 | 0.14 | 0.48 | 0.44 | `cs_bucket_zscore(cross_mean(div(day_max(Volume), day_sum(Volume)), 20), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 15 | 过 | 0.07 | `pow_1_5(day_max(Volume))` | 0.27 | 0.54 | 0.15 | 0.12 | 0.42 | 0.34 | `sub(cs_rank(cross_mean(day_max(Volume), 20)), cs_rank(cross_mean(day_sum(Volume), 20)))` |
| slot b seed 1 | 过 | 0.12 | `pow_1_5(day_max(Volume))` | 0.21 | 0.19 | 0.22 | 0.16 | 0.12 | 0.44 | `cross_mean(div(day_wstd(Ret, Volume), day_std(Ret)), 20)` |
| slot b seed 2 | 过 | 0.11 | `pow_1_5(day_max(Volume))` | 0.07 | 0.00 | 0.07 | 0.20 | 0.03 | 0.00 | `cross_zscore(cross_mean(div(day_wstd(Ret, Volume), day_std(Ret)), 10), 120)` |
| slot b seed 3 | 过 | 0.20 | `pow_1_5(day_max(Volume))` | 0.26 | 0.35 | 0.20 | 0.16 | 0.28 | 0.52 | `cross_mean(div(day_wmean(abs_(Ret), Volume), day_mean(abs_(Ret))), 20)` |
| slot b seed 4 | 过 | 0.12 | `pow_1_5(day_max(Volume))` | 0.32 | 0.03 | 0.25 | 0.17 | 0.08 | 0.32 | `cross_mean(div(day_topw_mean(abs_(Ret), Volume), day_mean(abs_(Ret))), 20)` |
| slot b seed 5 | 过 | 0.04 | `pow_1_5(day_max(Volume))` | 0.20 | 0.04 | 0.26 | 0.16 | 0.03 | 0.35 | `cs_bucket_zscore(cross_mean(div(day_wstd(Ret, Volume), day_std(Ret)), 20), cross_mean(day_sum(Amt), 30))` |
| slot b seed 6 | 过 | 0.20 | `pow_1_5(day_max(Volume))` | 0.10 | 0.25 | 0.34 | 0.58 | 0.27 | 0.10 | `cross_mean(sub(day_topw_mean(Ret, Volume), day_mean(Ret)), 20)` |
| slot b seed 7 | 过 | 0.26 | `pow_1_5(day_max(Volume))` | 0.13 | 0.05 | 0.17 | 0.58 | 0.07 | 0.19 | `cross_mean(day_signed_ratio(Ret, Volume), 20)` |
| slot b seed 8 | 过 | 0.13 | `pow_1_5(day_max(Volume))` | 0.03 | 0.04 | 0.06 | 0.44 | 0.03 | 0.01 | `cross_zscore(cross_mean(day_topw_mean(Ret, Volume), 10), 120)` |
| slot b seed 9 | 过 | 0.35 | `pow_1_5(day_max(Volume))` | 0.54 | 0.15 | 0.03 | 0.03 | 0.13 | 0.20 | `cross_mean(day_corr(in_delay(mul(sign(Ret), Volume), 1), Ret), 20)` |
| slot b seed 10 | 过 | 0.05 | `pow_1_5(day_max(Volume))` | 0.07 | 0.13 | 0.13 | 0.26 | 0.13 | 0.02 | `cross_mean(day_corr(in_delay(mul(sign(Ret), Volume), 1), abs_(Ret)), 20)` |
| slot b seed 11 | 过 | 0.09 | `pow_1_5(day_max(Volume))` | 0.02 | 0.07 | 0.07 | 0.13 | 0.09 | 0.02 | `cross_zscore(cross_mean(day_corr(in_delay(mul(sign(Ret), Volume), 1), Ret), 10), 120)` |
| slot b seed 12 | 过 | 0.26 | `pow_1_5(day_max(Volume))` | 0.27 | 0.01 | 0.29 | 0.04 | 0.02 | 0.11 | `cross_mean(day_topw_mean(mul(sign(in_delay(Ret, 1)), Ret), in_delay(Volume, 1)), 20)` |
| slot b seed 13 | 过 | 0.05 | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20)` | 0.35 | 0.31 | 0.38 | 0.18 | 0.35 | 0.20 | `cross_mean(div(day_topw_mean(abs_(Ret), in_delay(Volume, 1)), day_mean(abs_(Ret))), 20)` |
| slot b seed 14 | 过 | 0.02 | `pow_1_5(day_max(Volume))` | 0.04 | 0.04 | 0.05 | 0.02 | 0.04 | 0.00 | `cross_zscore(cross_mean(day_topw_mean(mul(sign(in_delay(Ret, 1)), Ret), in_delay(Volume, 1)), 10), 120)` |
| R 1 variant 1 | 过 | 0.40 | `pow_1_5(day_max(Volume))` | 0.78 | 0.34 | 0.09 | 0.09 | 0.27 | 0.05 | `cs_bucket_demean(cross_mean(day_max(Volume), 20), cross_mean(day_std(Amt), 30))` |
| R 1 variant 2 | 过 | 0.41 | `pow_1_5(day_max(Volume))` | 0.76 | 0.32 | 0.15 | 0.11 | 0.23 | 0.07 | `cs_bucket_demean(cross_mean(day_max(Volume), 20), cross_mean(day_sum(Amt), 30))` |
| R 1 variant 3 | 过 | 0.41 | `pow_1_5(day_max(Volume))` | 0.23 | 0.83 | 0.31 | 0.17 | 0.85 | 0.43 | `cs_bucket_demean(cross_mean(day_max(Volume), 20), sub(LogFloatCap, LogFloatShares))` |
| R 1 variant 4 | 过 | 0.43 | `pow_1_5(day_max(Volume))` | 0.74 | 0.09 | 0.44 | 0.07 | 0.17 | 0.34 | `cs_bucket_demean(cross_mean(day_max(Volume), 20), LogFloatCap)` |
| R 1 variant 5 | 过 | 0.86 | `pow_1_5(day_max(Volume))` | 0.96 | 0.03 | 0.15 | 0.20 | 0.09 | 0.21 | `cs_regres(log(day_max(Volume)), cross_mean(log(day_sum(Amt)), 30))` |
| R 1 variant 6 | 过 | 0.84 | `pow_1_5(day_max(Volume))` | 0.87 | 0.56 | 0.24 | 0.02 | 0.61 | 0.47 | `cross_mean(day_max(Volume), 60)` |
| R 1 variant 7 | 过 | 0.07 | `pow_1_5(day_max(Volume))` | 0.15 | 0.62 | 0.18 | 0.05 | 0.51 | 0.45 | `cross_mean(div(day_max(Volume), day_sum(Volume)), 60)` |
| R 1 variant 8 | 过 | 0.13 | `pow_1_5(day_max(Volume))` | 0.13 | 0.41 | 0.06 | 0.14 | 0.31 | 0.01 | `cs_bucket_zscore(cross_mean(div(day_max(Volume), day_sum(Volume)), 20), LogFloatCap)` |
