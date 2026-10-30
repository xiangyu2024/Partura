# 相关度表:种子 802,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_mean(in_delta(Volume, 30))` | 1.00 | 0.41 | 0.22 | 0.17 | 0.43 | 0.29 | `day_mean(in_delta(Volume, 30))` |
| slot a seed 1 | 过 | 0.47 | `day_mean(in_delta(Volume, 30))` | 0.57 | 0.57 | 0.28 | 0.10 | 0.56 | 0.28 | `cross_ema(sign(day_mean(in_delta(Volume, 30))), 10)` |
| slot a seed 2 | 过 | 0.36 | `day_mean(in_delta(Volume, 30))` | 0.52 | 0.53 | 0.24 | 0.07 | 0.50 | 0.27 | `div(cross_mean(day_mean(in_delta(Volume, 30)), 20), cross_stddev(day_mean(in_delta(Volume, 30)), 20))` |
| slot a seed 3 | 过 | 0.61 | `day_mean(in_delta(Volume, 30))` | 0.13 | 0.07 | 0.06 | 0.09 | 0.07 | 0.01 | `cross_zscore(day_mean(in_delta(Volume, 30)), 20)` |
| slot a seed 4 | 过 | 0.44 | `day_mean(in_delta(Volume, 30))` | 0.09 | 0.04 | 0.04 | 0.03 | 0.04 | 0.01 | `cross_delta(day_mean(in_delta(Volume, 30)), 5)` |
| slot a seed 5 | 过 | 0.49 | `day_mean(in_delta(Volume, 30))` | 0.07 | 0.01 | 0.02 | 0.05 | 0.01 | 0.00 | `ts_regres(day_sum(Volume), day_mean(in_delta(Volume, 30)), 20)` |
| slot a seed 6 | 过 | 0.25 | `day_mean(in_delta(Volume, 30))` | 0.29 | 0.21 | 0.28 | 0.13 | 0.25 | 0.01 | `cross_regbeta(day_sum(Volume), day_mean(in_delta(Volume, 30)), 20)` |
| slot a seed 7 | 过 | 0.02 | `day_mean(in_delta(Volume, 30))` | 0.37 | 0.13 | 0.04 | 0.15 | 0.13 | 0.08 | `mul(day_mean(in_delta(Volume, 30)), cross_zscore(day_sum(Volume), 20))` |
| slot a seed 8 | 过 | 0.10 | `day_mean(in_delta(Volume, 30))` | 0.07 | 0.00 | 0.01 | 0.04 | 0.00 | 0.01 | `mul(day_mean(in_delta(Volume, 30)), sign(day_sum(Ret)))` |
| slot a seed 9 | 过 | 0.13 | `day_mean(in_delta(Volume, 30))` | 0.07 | 0.07 | 0.13 | 0.24 | 0.07 | 0.05 | `cross_mean(mul(day_mean(in_delta(Volume, 30)), sign(day_sum(Ret))), 20)` |
| slot a seed 10 | 过 | 0.10 | `day_mean(in_delta(Volume, 30))` | 0.05 | 0.10 | 0.07 | 0.05 | 0.10 | 0.10 | `cross_corr(day_mean(in_delta(Volume, 30)), day_sum(Ret), 20)` |
| slot a seed 11 | 过 | 0.04 | `day_mean(in_delta(Volume, 30))` | 0.18 | 0.03 | 0.05 | 0.01 | 0.03 | 0.02 | `mul(day_mean(in_delta(Volume, 30)), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1))` |
| slot a seed 12 | 过 | 0.03 | `day_mean(in_delta(Volume, 30))` | 0.06 | 0.01 | 0.03 | 0.05 | 0.01 | 0.01 | `mul(sub(cs_rank(day_mean(in_delta(Volume, 30))), 0.5), sub(cs_rank(day_sum(in_slice(Ret, 211, 240))), 0.5))` |
| slot a seed 13 | 过 | 0.61 | `day_mean(in_delta(Volume, 30))` | 0.69 | 0.24 | 0.10 | 0.07 | 0.24 | 0.16 | `cs_regres(day_mean(in_delta(Volume, 30)), day_mean(in_delta(Volume, 5)))` |
| slot b seed 1 | 过 | 0.02 | `day_mean(in_delta(Volume, 30))` | 0.10 | 0.02 | 0.02 | 0.13 | 0.03 | 0.02 | `day_corr(Ret, Volume)` |
| slot b seed 2 | 过 | 0.02 | `day_mean(in_delta(Volume, 30))` | 0.00 | 0.04 | 0.02 | 0.09 | 0.05 | 0.02 | `day_corr(Close, Volume)` |
| slot b seed 3 | 过 | 0.01 | `day_mean(in_delta(Volume, 30))` | 0.09 | 0.02 | 0.02 | 0.13 | 0.02 | 0.03 | `day_corr(Ret, in_delta(Volume, 1))` |
| slot b seed 4 | 过 | 0.04 | `day_mean(in_delta(Volume, 30))` | 0.04 | 0.01 | 0.01 | 0.14 | 0.01 | 0.06 | `day_signed_ratio(Ret, Volume)` |
| slot b seed 5 | 过 | 0.02 | `day_mean(in_delta(Volume, 30))` | 0.09 | 0.02 | 0.03 | 0.13 | 0.03 | 0.02 | `sub(day_wmean(Ret, Volume), day_mean(Ret))` |
| slot b seed 6 | 过 | 0.03 | `day_mean(in_delta(Volume, 30))` | 0.01 | 0.03 | 0.01 | 0.01 | 0.03 | 0.02 | `day_corr(Ret, in_delay(Volume, 1))` |
| slot b seed 7 | 过 | 0.02 | `day_mean(in_delta(Volume, 30))` | 0.01 | 0.04 | 0.04 | 0.14 | 0.04 | 0.01 | `day_corr(in_delay(Ret, 1), Volume)` |
| slot b seed 8 | 过 | 0.01 | `day_mean(in_delta(Volume, 30))` | 0.11 | 0.04 | 0.03 | 0.15 | 0.04 | 0.03 | `day_topw_mean(Ret, in_zscore_rolling(Volume, 30))` |
| slot b seed 9 | 过 | 0.25 | `day_mean(in_delta(Volume, 30))` | 0.31 | 0.26 | 0.09 | 0.00 | 0.25 | 0.23 | `div(day_topw_mean(abs(Ret), in_zscore_rolling(Volume, 30)), day_mean(abs(Ret)))` |
| slot b seed 10 | 过 | 0.02 | `day_mean(in_delta(Volume, 30))` | 0.12 | 0.03 | 0.02 | 0.14 | 0.03 | 0.03 | `day_topw_mean(Ret, Volume)` |
| slot b seed 11 | 过 | 0.23 | `day_mean(in_delta(Volume, 30))` | 0.04 | 0.22 | 0.09 | 0.15 | 0.22 | 0.02 | `day_corr(abs(Ret), Volume)` |
| slot b seed 12 | 过 | 0.09 | `day_mean(in_delta(Volume, 30))` | 0.00 | 0.18 | 0.09 | 0.19 | 0.19 | 0.07 | `cross_mean(day_corr(Close, Volume), 20)` |
| slot b seed 13 | 过 | 0.15 | `day_mean(in_delta(Volume, 30))` | 0.00 | 0.08 | 0.18 | 0.56 | 0.10 | 0.22 | `cross_mean(day_signed_ratio(Ret, Volume), 20)` |
| R 1 variant 1 | 过 | 0.70 | `day_mean(in_delta(Volume, 30))` | 0.83 | 0.43 | 0.23 | 0.17 | 0.45 | 0.32 | `day_mean(in_delta(Volume, 3))` |
| R 1 variant 2 | 过 | 0.74 | `day_mean(in_delta(Volume, 30))` | 0.84 | 0.38 | 0.20 | 0.16 | 0.40 | 0.29 | `day_mean(in_delta(Volume, 5))` |
| R 1 variant 3 | 过 | 0.82 | `day_mean(in_delta(Volume, 30))` | 0.90 | 0.38 | 0.20 | 0.16 | 0.39 | 0.27 | `day_mean(in_delta(Volume, 10))` |
| R 1 variant 4 | 过 | 0.81 | `day_mean(in_delta(Volume, 30))` | 0.61 | 0.19 | 0.16 | 0.13 | 0.21 | 0.08 | `day_mean(in_delta(div(Volume, day_sum(Volume)), 30))` |
| R 1 variant 5 | 过 | 0.73 | `day_mean(in_delta(Volume, 30))` | 0.57 | 0.21 | 0.16 | 0.13 | 0.23 | 0.10 | `day_mean(in_delta(div(Volume, day_sum(Volume)), 15))` |
| R 1 variant 6 | 过 | 0.83 | `day_mean(in_delta(Volume, 30))` | 0.58 | 0.17 | 0.13 | 0.18 | 0.18 | 0.09 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 30))` |
| R 1 variant 7 | 过 | 0.79 | `day_mean(in_delta(Volume, 30))` | 0.55 | 0.31 | 0.29 | 0.18 | 0.32 | 0.04 | `day_mean(in_delta(div(Volume, FloatShares), 30))` |
| R 1 variant 8 | 过 | 0.41 | `day_mean(in_delta(Volume, 30))` | 0.43 | 0.25 | 0.18 | 0.14 | 0.28 | 0.09 | `div(day_first(Volume), day_sum(Volume))` |
| R 1 variant 9 | 过 | 0.23 | `day_mean(in_delta(Volume, 30))` | 0.10 | 0.06 | 0.03 | 0.03 | 0.04 | 0.19 | `div(day_last(Volume), day_sum(Volume))` |
| R 1 variant 10 | 过 | 0.42 | `day_mean(in_delta(Volume, 30))` | 0.27 | 0.14 | 0.07 | 0.10 | 0.15 | 0.17 | `div(sub(day_last(Volume), day_first(Volume)), day_sum(Volume))` |
| R 1 variant 11 | 过 | 0.99 | `day_mean(in_delta(Volume, 30))` | 0.99 | 0.44 | 0.23 | 0.17 | 0.46 | 0.31 | `day_mean(in_delta(in_slice(Volume, 1, 239), 30))` |
| R 1 variant 12 | 过 | 0.80 | `day_mean(in_delta(Volume, 30))` | 0.60 | 0.18 | 0.16 | 0.13 | 0.20 | 0.06 | `day_mean(in_delta(div(in_slice(Volume, 1, 239), day_sum(Volume)), 30))` |
| R 1 variant 13 | 过 | 0.69 | `day_mean(in_delta(Volume, 30))` | 0.54 | 0.16 | 0.17 | 0.12 | 0.18 | 0.00 | `div(day_sum(in_slice(Volume, 0, 29)), day_sum(Volume))` |
| R 1 variant 14 | 过 | 0.59 | `day_mean(in_delta(Volume, 30))` | 0.34 | 0.15 | 0.07 | 0.10 | 0.15 | 0.16 | `div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume))` |
| R 1 variant 15 | 过 | 0.76 | `day_mean(in_delta(Volume, 30))` | 0.91 | 0.36 | 0.19 | 0.15 | 0.38 | 0.25 | `sub(day_sum(in_half(Volume, False)), day_sum(in_half(Volume, True)))` |
| R 1 variant 16 | 废品 | 0.72 | `day_mean(in_delta(Volume, 30))` | 0.86 | 0.49 | 0.21 | 0.16 | 0.50 | 0.33 | `day_median(in_delta(Volume, 30))` |
