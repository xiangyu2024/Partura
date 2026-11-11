# 相关度表:种子 2044,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.98 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.99 | 0.18 | 0.08 | 0.03 | 0.19 | 0.10 | `ts_std(day_corr(Ret, Volume), 40)` |
| slot a seed 1 | 过 | 0.92 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.90 | 0.06 | 0.26 | 0.01 | 0.05 | 0.12 | `cross_ema(cs_demean(ts_std(day_corr(Ret, Volume), 40)), 120)` |
| slot a seed 2 | 过 | 0.85 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.79 | 0.08 | 0.23 | 0.03 | 0.07 | 0.11 | `ts_mean(ts_std(day_corr(Ret, Volume), 40), 120)` |
| slot a seed 3 | 过 | 0.66 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.66 | 0.19 | 0.12 | 0.05 | 0.21 | 0.01 | `cross_zscore(ts_std(day_corr(Ret, Volume), 40), 241)` |
| slot a seed 4 | 过 | 0.51 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.50 | 0.13 | 0.10 | 0.06 | 0.15 | 0.00 | `sub(ts_std(day_corr(Ret, Volume), 40), ts_delay(ts_std(day_corr(Ret, Volume), 40), 60))` |
| slot a seed 5 | 过 | 0.89 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.88 | 0.16 | 0.12 | 0.02 | 0.15 | 0.09 | `cs_regres(ts_std(day_corr(Ret, Volume), 40), ts_max(cs_demean(day_corr(Ret, Volume)), 120))` |
| slot a seed 6 | 过 | 0.96 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.98 | 0.23 | 0.02 | 0.03 | 0.24 | 0.12 | `cs_regres(ts_std(day_corr(Ret, Volume), 40), ts_mean(day_std(Ret), 120))` |
| slot a seed 7 | 过 | 0.96 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.98 | 0.06 | 0.11 | 0.04 | 0.08 | 0.18 | `cs_bucket_demean(ts_std(day_corr(Ret, Volume), 40), ts_mean(log(day_sum(Amt)), 60))` |
| slot a seed 8 | 过 | 0.73 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.69 | 0.12 | 0.06 | 0.03 | 0.13 | 0.09 | `cs_bucket_demean(cross_ema(ts_std(day_corr(Ret, Volume), 40), 60), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 9 | 过 | 0.71 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.87 | 0.11 | 0.68 | 0.02 | 0.14 | 0.02 | `sub(cs_rank(ts_std(day_corr(Ret, Volume), 40)), cs_rank(ts_mean(day_std(Ret), 40)))` |
| slot a seed 10 | 过 | 0.12 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.12 | 0.18 | 0.32 | 0.22 | 0.19 | 0.03 | `mul(ts_std(day_corr(Ret, Volume), 40), sign(ts_delta(log(day_last(Close)), 120)))` |
| slot a seed 11 | 过 | 0.21 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.18 | 0.03 | 0.01 | 0.04 | 0.02 | 0.02 | `cross_corr(ts_std(day_corr(Ret, Volume), 40), day_std(Ret), 120)` |
| slot a seed 12 | 过 | 0.24 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.23 | 0.01 | 0.19 | 0.04 | 0.03 | 0.12 | `cross_semistd_pos(ts_std(day_corr(Ret, Volume), 40), 120)` |
| slot a seed 13 | 过 | 0.94 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.92 | 0.04 | 0.26 | 0.01 | 0.04 | 0.12 | `ts_mean(cs_demean(ts_std(day_corr(Ret, Volume), 40)), 241)` |
| slot b seed 1 | 过 | 0.41 | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin` | 0.51 | 0.14 | 0.06 | 0.02 | 0.14 | 0.12 | `ts_max(cs_demean(day_corr(Ret, in_delay(Ret, 1))), 120)` |
| slot b seed 2 | 过 | 0.29 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.18 | 0.31 | 0.10 | 0.05 | 0.25 | 0.10 | `ts_min(cs_demean(day_corr(Ret, in_delay(Ret, 1))), 120)` |
| slot b seed 3 | 过 | 0.33 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.31 | 0.27 | 0.08 | 0.07 | 0.21 | 0.03 | `cross_ema(cs_demean(day_corr(Ret, in_delay(Ret, 1))), 120)` |
| slot b seed 4 | 过 | 0.21 | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` | 0.19 | 0.06 | 0.06 | 0.00 | 0.07 | 0.07 | `ts_max(cs_demean(day_corr(Ret, in_delay(Ret, 5))), 120)` |
| slot b seed 5 | 过 | 0.31 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.23 | 0.37 | 0.16 | 0.02 | 0.38 | 0.02 | `ts_max(cs_demean(day_corr(Volume, in_delay(Volume, 1))), 120)` |
| slot b seed 6 | 过 | 0.47 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.32 | 0.58 | 0.08 | 0.07 | 0.54 | 0.22 | `ts_min(cs_demean(day_corr(Volume, in_delay(Volume, 1))), 120)` |
| slot b seed 7 | 过 | 0.58 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.45 | 0.68 | 0.09 | 0.07 | 0.64 | 0.22 | `cross_ema(cs_demean(day_corr(Volume, in_delay(Volume, 1))), 120)` |
| slot b seed 8 | 过 | 0.46 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.32 | 0.64 | 0.04 | 0.07 | 0.58 | 0.40 | `ts_max(cs_demean(day_durbin_watson(Volume)), 120)` |
| slot b seed 9 | 过 | 0.35 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.36 | 0.07 | 0.14 | 0.01 | 0.09 | 0.22 | `ts_max(cs_demean(day_corr(abs_(Ret), in_delay(abs_(Ret), 1))), 120)` |
| slot b seed 10 | 过 | 0.51 | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin` | 0.60 | 0.10 | 0.03 | 0.02 | 0.10 | 0.13 | `ts_max(ts_max(day_corr(Ret, in_delay(Ret, 1)), 40), 120)` |
| slot b seed 11 | 过 | 0.74 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.78 | 0.16 | 0.03 | 0.05 | 0.14 | 0.07 | `sub(ts_max(cs_demean(day_corr(Volume, in_delay(Volume, 1))), 120), ts_max(cs_demean(day_corr(Ret, Volume)), 120))` |
| slot b seed 12 | 过 | 0.29 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.18 | 0.31 | 0.10 | 0.05 | 0.25 | 0.10 | `ts_max(cs_demean(day_durbin_watson(Ret)), 120)` |
| R 1 variant 1 | 过 | 0.99 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.99 | 0.03 | 0.22 | 0.01 | 0.02 | 0.18 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 60), 241)` |
| R 1 variant 2 | 过 | 0.99 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.98 | 0.05 | 0.20 | 0.01 | 0.05 | 0.17 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 20), 241)` |
| R 1 variant 3 | 过 | 0.97 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 0.96 | 0.02 | 0.22 | 0.01 | 0.02 | 0.18 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 300)` |
| R 1 variant 4 | 过 | 1.00 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 1.00 | 0.04 | 0.21 | 0.01 | 0.04 | 0.17 | `cross_fangzheng(ts_std(add(day_corr(Ret, Volume), day_corr(Ret, Amt)), 40), 241)` |
| R 1 variant 5 | 过 | 1.00 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 1.00 | 0.03 | 0.22 | 0.01 | 0.03 | 0.17 | `cross_fangzheng(ts_mean(ts_std(day_corr(Ret, Volume), 40), 5), 241)` |
| R 1 variant 6 | 过 | 1.00 | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` | 1.00 | 0.04 | 0.21 | 0.01 | 0.04 | 0.17 | `cross_fangzheng(cs_demean(ts_std(day_corr(Ret, Volume), 40)), 241)` |
