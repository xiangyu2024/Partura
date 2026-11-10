# 相关度表:种子 2044,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.04 | `ts_max(day_corr(Ret, Volume), 40)` | 0.08 | 0.03 | 0.03 | 0.16 | 0.03 | 0.03 | `day_corr(Ret, Volume)` |
| slot a seed 1 | 过 | 0.23 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.18 | 0.30 | 0.29 | 0.15 | 0.31 | 0.09 | `cross_ema(cs_demean(day_corr(Ret, Volume)), 120)` |
| slot a seed 2 | 过 | 0.09 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.05 | 0.09 | 0.01 | 0.04 | 0.09 | 0.02 | `cross_autocorr(day_corr(Ret, Volume), 120, 1)` |
| slot a seed 3 | 过 | 0.45 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.51 | 0.12 | 0.11 | 0.01 | 0.07 | 0.03 | `div(sub(ts_max(day_corr(Ret, Volume), 120), ts_mean(day_corr(Ret, Volume), 120)), ts_std(day_corr(Ret, Volume), 120))` |
| slot a seed 4 | 过 | 0.51 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.55 | 0.03 | 0.20 | 0.06 | 0.01 | 0.01 | `cs_regres(ts_max(day_corr(Ret, Volume), 120), ts_std(day_corr(Ret, Volume), 120))` |
| slot a seed 5 | 过 | 0.52 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.53 | 0.06 | 0.17 | 0.06 | 0.09 | 0.02 | `add(ts_max(day_corr(Ret, Volume), 120), ts_min(day_corr(Ret, Volume), 120))` |
| slot a seed 6 | 过 | 0.31 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.35 | 0.14 | 0.02 | 0.02 | 0.10 | 0.03 | `ts_skew(day_corr(Ret, Volume), 120)` |
| slot a seed 7 | 过 | 0.05 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.05 | 0.04 | 0.02 | 0.01 | 0.02 | 0.01 | `cross_regbeta(ts_delay(day_corr(Ret, Volume), 1), day_sum(Ret), 120)` |
| slot a seed 8 | 过 | 0.05 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.05 | 0.04 | 0.02 | 0.01 | 0.03 | 0.01 | `cross_corr(ts_delay(day_corr(Ret, Volume), 1), day_sum(Ret), 120)` |
| slot a seed 9 | 过 | 0.04 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.04 | 0.05 | 0.02 | 0.00 | 0.03 | 0.01 | `cross_reg_tvalue(ts_delay(day_corr(Ret, Volume), 1), day_sum(Ret), 180)` |
| slot a seed 10 | 过 | 0.04 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.06 | 0.06 | 0.03 | 0.01 | 0.05 | 0.01 | `cross_regbeta(cs_demean(ts_delay(day_corr(Ret, Volume), 1)), cs_demean(day_sum(Ret)), 120)` |
| slot a seed 11 | 过 | 0.22 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.17 | 0.05 | 0.10 | 0.01 | 0.05 | 0.03 | `cross_corr(day_corr(Ret, Volume), day_sum(Ret), 120)` |
| slot a seed 12 | 过 | 0.22 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.17 | 0.33 | 0.22 | 0.03 | 0.33 | 0.42 | `cross_regbeta(cs_mean(day_corr(Ret, Volume)), day_corr(Ret, Volume), 120)` |
| slot a seed 13 | 过 | 0.09 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.05 | 0.20 | 0.32 | 0.21 | 0.22 | 0.04 | `mul(ts_max(day_corr(Ret, Volume), 120), sign(ts_delta(log(day_last(Close)), 120)))` |
| slot a seed 14 | 过 | 0.50 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.55 | 0.16 | 0.29 | 0.21 | 0.15 | 0.16 | `sub(cs_rank(ts_max(day_corr(Ret, Volume), 120)), cs_rank(ts_delta(log(day_last(Close)), 120)))` |
| slot a seed 15 | 过 | 0.03 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.03 | 0.06 | 0.03 | 0.01 | 0.05 | 0.03 | `cross_regbeta(ts_delay(cs_rank(day_corr(Ret, Volume)), 1), cs_rank(day_sum(Ret)), 180)` |
| slot b seed 1 | 过 | 0.05 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.07 | 0.16 | 0.28 | 0.25 | 0.19 | 0.31 | `cross_ema(day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 2 | 过 | 0.08 | `ts_max(day_corr(Ret, Volume), 40)` | 0.08 | 0.20 | 0.26 | 0.17 | 0.23 | 0.38 | `cross_ema(cs_demean(day_signed_ratio(Ret, Amt)), 120)` |
| slot b seed 3 | 过 | 0.18 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.09 | 0.21 | 0.17 | 0.05 | 0.21 | 0.13 | `sub(cs_rank(cross_sum(day_signed_ratio(Ret, Amt), 60)), cs_rank(cross_sum(day_sum(Ret), 60)))` |
| slot b seed 4 | 过 | 0.09 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.07 | 0.02 | 0.10 | 0.17 | 0.00 | 0.20 | `cs_regres(cross_sum(day_signed_ratio(Ret, Amt), 60), cross_sum(day_sum(Ret), 60))` |
| slot b seed 5 | 过 | 0.11 | `ts_max(day_corr(Ret, Volume), 40)` | 0.07 | 0.04 | 0.14 | 0.12 | 0.06 | 0.23 | `cs_regres(cross_sum(day_signed_ratio(Ret, Amt), 120), cross_sum(day_sum(Ret), 120))` |
| slot b seed 6 | 过 | 0.21 | `ts_max(day_corr(Ret, Volume), 40)` | 0.12 | 0.32 | 0.36 | 0.23 | 0.34 | 0.04 | `cs_regres(cross_sum(day_sum(Ret), 60), cross_sum(day_signed_ratio(Ret, Amt), 60))` |
| slot b seed 7 | 过 | 0.07 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.06 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | `cross_regbeta(ts_delay(day_signed_ratio(Ret, Amt), 1), day_sum(Ret), 120)` |
| slot b seed 8 | 过 | 0.06 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.06 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | `cross_corr(ts_delay(day_signed_ratio(Ret, Amt), 1), day_sum(Ret), 120)` |
| slot b seed 9 | 过 | 0.06 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.05 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | `cross_reg_tvalue(ts_delay(day_signed_ratio(Ret, Amt), 1), day_sum(Ret), 180)` |
| slot b seed 10 | 过 | 0.09 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.06 | 0.09 | 0.01 | 0.04 | 0.09 | 0.00 | `cross_autocorr(day_signed_ratio(Ret, Amt), 120, 1)` |
| slot b seed 11 | 过 | 0.08 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.07 | 0.07 | 0.01 | 0.03 | 0.07 | 0.01 | `mul(cross_autocorr(day_signed_ratio(Ret, Amt), 120, 1), sign(cross_mean(day_signed_ratio(Ret, Amt), 120)))` |
| slot b seed 12 | 过 | 0.34 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.34 | 0.07 | 0.20 | 0.05 | 0.04 | 0.14 | `ts_max(day_signed_ratio(Ret, Amt), 120)` |
| slot b seed 13 | 过 | 0.08 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.08 | 0.10 | 0.20 | 0.07 | 0.11 | 0.08 | `sub(cross_ema(day_signed_ratio(in_slice(Ret, 181, 241), in_slice(Amt, 181, 241)), 60), cross_ema(day_signed_ratio(in_slice(Ret, 1, 60), in_slice(Amt, 1, 60)), 60))` |
| slot b seed 14 | 过 | 0.01 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.03 | 0.06 | 0.04 | 0.15 | 0.06 | 0.20 | `cross_ema(day_signed_ratio(in_slice(Ret, 181, 241), in_slice(Amt, 181, 241)), 60)` |
| R 1 variant 1 | 过 | 0.82 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.82 | 0.05 | 0.02 | 0.05 | 0.08 | 0.09 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 80)` |
| R 1 variant 2 | 过 | 0.71 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.69 | 0.02 | 0.02 | 0.04 | 0.05 | 0.10 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 120)` |
| R 1 variant 3 | 过 | 0.64 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.61 | 0.00 | 0.02 | 0.04 | 0.03 | 0.10 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 160)` |
| R 1 variant 4 | 过 | 0.59 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.55 | 0.02 | 0.02 | 0.04 | 0.02 | 0.10 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 200)` |
| R 1 variant 5 | 过 | 0.68 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.65 | 0.01 | 0.02 | 0.04 | 0.04 | 0.10 | `ts_max(ts_max(day_corr(Ret, Volume), 20), 160)` |
| R 1 variant 6 | 过 | 0.71 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.69 | 0.02 | 0.01 | 0.04 | 0.05 | 0.10 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` |
| R 1 variant 7 | 过 | 0.65 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.61 | 0.06 | 0.03 | 0.04 | 0.09 | 0.06 | `ts_max(ts_max(cs_demean(day_corr(Ret, Volume)), 40), 120)` |
| R 1 variant 8 | 过 | 0.68 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.65 | 0.04 | 0.03 | 0.04 | 0.07 | 0.07 | `ts_max(ts_max(cs_rank(day_corr(Ret, Volume)), 40), 120)` |
| R 2 variant 1 | 过 | 0.45 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.38 | 0.13 | 0.06 | 0.07 | 0.14 | 0.05 | `ts_max(ts_mean(day_corr(Ret, Volume), 5), 120)` |
| R 2 variant 2 | 过 | 0.34 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.27 | 0.14 | 0.07 | 0.05 | 0.14 | 0.04 | `ts_max(ts_mean(day_corr(Ret, Volume), 10), 160)` |
| R 2 variant 3 | 过 | 0.31 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.25 | 0.17 | 0.12 | 0.06 | 0.17 | 0.04 | `ts_max(ts_mean(day_corr(Ret, Volume), 20), 120)` |
| R 2 variant 4 | 过 | 0.42 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.36 | 0.13 | 0.09 | 0.07 | 0.14 | 0.06 | `ts_max(ts_decay_linear(day_corr(Ret, Volume), 10), 120)` |
| R 2 variant 5 | 过 | 0.73 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.71 | 0.09 | 0.04 | 0.04 | 0.12 | 0.05 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` |
| R 2 variant 6 | 过 | 0.77 | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` | 0.76 | 0.08 | 0.04 | 0.05 | 0.10 | 0.07 | `ts_max(cs_rank(day_corr(Ret, Volume)), 120)` |
| R 3 variant 1 | 过 | 0.54 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.54 | 0.37 | 0.09 | 0.03 | 0.35 | 0.09 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` |
| R 3 variant 2 | 过 | 0.58 | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` | 0.57 | 0.35 | 0.10 | 0.02 | 0.34 | 0.02 | `log(neg(cross_ema(day_corr(Vwap, Amt), 120)))` |
