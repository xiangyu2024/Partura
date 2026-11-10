# 相关度表:种子 2044,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 1.00 | 0.09 | 0.04 | 0.04 | 0.12 | 0.05 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` |
| slot a seed 1 | 过 | 0.75 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.79 | 0.02 | 0.20 | 0.06 | 0.06 | 0.03 | `cs_regres(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_std(day_corr(Ret, Volume), 120))` |
| slot a seed 2 | 过 | 1.00 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 1.00 | 0.09 | 0.01 | 0.04 | 0.11 | 0.04 | `cs_regres(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_mean(day_std(Ret), 120))` |
| slot a seed 3 | 过 | 1.00 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 1.00 | 0.09 | 0.04 | 0.04 | 0.12 | 0.05 | `cs_regres(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_mean(log(day_sum(Amt)), 120))` |
| slot a seed 4 | 过 | 0.95 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.96 | 0.07 | 0.07 | 0.05 | 0.10 | 0.04 | `cs_regres(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_max(day_std(Ret), 120))` |
| slot a seed 5 | 过 | 0.96 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.96 | 0.03 | 0.04 | 0.00 | 0.05 | 0.07 | `sub(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_mean(cs_demean(day_corr(Ret, Volume)), 120))` |
| slot a seed 6 | 过 | 0.97 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.97 | 0.03 | 0.02 | 0.01 | 0.06 | 0.08 | `sub(ts_max(cs_demean(day_corr(Ret, Volume)), 120), cross_ema(cs_demean(day_corr(Ret, Volume)), 120))` |
| slot a seed 7 | 过 | 0.67 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.67 | 0.03 | 0.15 | 0.06 | 0.06 | 0.04 | `add(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_min(cs_demean(day_corr(Ret, Volume)), 120))` |
| slot a seed 8 | 过 | 0.67 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.72 | 0.06 | 0.13 | 0.01 | 0.02 | 0.02 | `div(sub(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_mean(cs_demean(day_corr(Ret, Volume)), 120)), ts_std(day_corr(Ret, Volume), 120))` |
| slot a seed 9 | 废品 | 0.07 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.06 | 0.12 | 0.13 | 0.00 | 0.13 | 0.01 | `sub(cs_rank(ts_max(cs_demean(day_corr(Ret, Volume)), 120)), cs_rank(ts_max(cs_demean(day_corr(Ret, Amt)), 120)))` |
| slot a seed 10 | 过 | 0.10 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.12 | 0.20 | 0.31 | 0.21 | 0.21 | 0.03 | `mul(ts_max(cs_demean(day_corr(Ret, Volume)), 120), sign(ts_delta(log(day_last(Close)), 120)))` |
| slot a seed 11 | 过 | 0.10 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.11 | 0.12 | 0.29 | 0.29 | 0.15 | 0.21 | `mul(ts_max(cs_demean(day_corr(Ret, Volume)), 120), cs_demean(ts_mean(day_signed_ratio(Ret, Amt), 60)))` |
| slot a seed 12 | 过 | 0.62 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.68 | 0.13 | 0.28 | 0.21 | 0.12 | 0.12 | `sub(cs_rank(ts_max(cs_demean(day_corr(Ret, Volume)), 120)), cs_rank(ts_delta(log(day_last(Close)), 120)))` |
| slot a seed 13 | 过 | 0.96 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.97 | 0.03 | 0.03 | 0.05 | 0.07 | 0.06 | `cs_regres(ts_max(cs_demean(day_corr(Ret, Volume)), 120), ts_max(cs_demean(day_corr(Close, High)), 120))` |
| slot b seed 1 | 过 | 0.63 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.57 | 0.02 | 0.03 | 0.02 | 0.05 | 0.19 | `ts_max(cs_demean(day_corr(abs_(Ret), Volume)), 120)` |
| slot b seed 2 | 过 | 0.33 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.21 | 0.19 | 0.07 | 0.04 | 0.14 | 0.05 | `ts_min(cs_demean(day_corr(abs_(Ret), Volume)), 120)` |
| slot b seed 3 | 过 | 0.32 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.28 | 0.07 | 0.10 | 0.01 | 0.04 | 0.24 | `ts_max(cs_demean(day_corr(Ret, in_delay(Volume, 1))), 120)` |
| slot b seed 4 | 过 | 0.46 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.40 | 0.01 | 0.06 | 0.02 | 0.03 | 0.26 | `ts_max(cs_demean(day_corr(in_delay(Ret, 1), Volume)), 120)` |
| slot b seed 5 | 过 | 0.63 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.58 | 0.07 | 0.02 | 0.03 | 0.09 | 0.10 | `ts_max(cs_demean(day_corr(Ret, in_delta(Volume, 1))), 120)` |
| slot b seed 6 | 过 | 0.25 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.21 | 0.22 | 0.05 | 0.01 | 0.22 | 0.05 | `ts_max(cs_demean(day_corr(Close, Volume)), 120)` |
| slot b seed 7 | 过 | 0.23 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.17 | 0.17 | 0.10 | 0.01 | 0.17 | 0.01 | `ts_max(cs_demean(day_corr(Vwap, Volume)), 120)` |
| slot b seed 8 | 过 | 0.67 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.61 | 0.02 | 0.01 | 0.02 | 0.01 | 0.20 | `ts_max(ts_max(day_corr(abs_(Ret), Amt), 40), 120)` |
| slot b seed 9 | 过 | 0.65 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.67 | 0.07 | 0.08 | 0.03 | 0.10 | 0.09 | `sub(ts_max(cs_demean(day_corr(abs_(Ret), Volume)), 120), ts_max(cs_demean(day_corr(Ret, Volume)), 120))` |
| slot b seed 10 | 过 | 0.26 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.19 | 0.16 | 0.04 | 0.05 | 0.16 | 0.04 | `ts_min(cs_demean(day_corr(Ret, in_delta(Volume, 1))), 120)` |
| slot b seed 11 | 过 | 0.56 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.50 | 0.10 | 0.02 | 0.02 | 0.12 | 0.02 | `ts_max(cs_demean(day_corr(abs_(Ret), in_delta(Volume, 1))), 120)` |
| slot b seed 12 | 过 | 0.26 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.21 | 0.26 | 0.06 | 0.01 | 0.25 | 0.08 | `ts_max(cs_demean(day_corr(Close, in_delay(Volume, 1))), 120)` |
| R 1 variant 1 | 过 | 1.00 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 1.00 | 0.09 | 0.04 | 0.04 | 0.12 | 0.05 | `ts_max(cs_demean(add(day_corr(Ret, Volume), day_corr(Ret, Amt))), 120)` |
| R 1 variant 2 | 过 | 0.89 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.88 | 0.06 | 0.03 | 0.04 | 0.09 | 0.06 | `ts_max(ts_max(cs_demean(day_corr(Ret, Volume)), 40), 120)` |
| R 1 variant 3 | 过 | 0.85 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.84 | 0.04 | 0.03 | 0.04 | 0.07 | 0.06 | `ts_max(cs_demean(day_corr(Ret, Volume)), 180)` |
| R 1 variant 4 | 过 | 0.96 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.95 | 0.08 | 0.04 | 0.05 | 0.10 | 0.07 | `ts_max(cs_rank(day_corr(Ret, Volume)), 120)` |
| R 1 variant 5 | 过 | 0.48 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.43 | 0.18 | 0.08 | 0.07 | 0.19 | 0.00 | `ts_max(cs_demean(ts_mean(day_corr(Ret, Volume), 5)), 120)` |
| R 1 variant 6 | 过 | 0.27 | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` | 0.12 | 0.53 | 0.10 | 0.03 | 0.48 | 0.43 | `ts_max(cs_demean(day_corr(Ret, Vwap)), 120)` |
| R 2 variant 1 | 过 | 0.89 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.88 | 0.05 | 0.02 | 0.04 | 0.08 | 0.06 | `ts_max(cs_demean(day_corr(Ret, Amt)), 160)` |
| R 2 variant 2 | 过 | 0.85 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.84 | 0.04 | 0.02 | 0.04 | 0.07 | 0.06 | `ts_max(ts_max(cs_demean(day_corr(Ret, Amt)), 20), 160)` |
| R 2 variant 3 | 过 | 0.87 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.88 | 0.12 | 0.05 | 0.06 | 0.15 | 0.04 | `ts_max(cs_demean(day_corr(Ret, Amt)), 90)` |
| R 2 variant 4 | 过 | 0.96 | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` | 0.95 | 0.07 | 0.03 | 0.05 | 0.10 | 0.07 | `ts_max(cs_rank(day_corr(Ret, Amt)), 120)` |
| R 2 variant 5 | 过 | 0.89 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.88 | 0.05 | 0.02 | 0.04 | 0.08 | 0.06 | `ts_max(ts_max(cs_demean(day_corr(Ret, Amt)), 40), 120)` |
| R 2 variant 6 | 过 | 0.89 | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` | 0.88 | 0.05 | 0.03 | 0.04 | 0.08 | 0.06 | `ts_max(cs_demean(add(day_corr(Ret, Amt), day_corr(Ret, Volume))), 160)` |
