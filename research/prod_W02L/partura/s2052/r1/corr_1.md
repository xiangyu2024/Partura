# 相关度表:种子 2052,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.15 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.19 | 0.23 | 0.02 | 0.00 | 0.20 | 0.11 | `day_ar1_coefficient(High)` |
| slot a seed 1 | 过 | 0.33 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.24 | 0.53 | 0.02 | 0.09 | 0.47 | 0.31 | `cross_mean(day_ar1_coefficient(High), 20)` |
| slot a seed 2 | 过 | 0.40 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.33 | 0.57 | 0.06 | 0.09 | 0.49 | 0.37 | `cross_ema(day_ar1_coefficient(High), 20)` |
| slot a seed 3 | 过 | 0.34 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.25 | 0.54 | 0.02 | 0.08 | 0.47 | 0.32 | `cross_decay_linear(day_ar1_coefficient(High), 30)` |
| slot a seed 4 | 过 | 0.07 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.11 | 0.07 | 0.09 | 0.05 | 0.07 | 0.00 | `sub(cross_mean(day_ar1_coefficient(High), 10), cross_mean(day_ar1_coefficient(High), 60))` |
| slot a seed 5 | 过 | 0.04 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.11 | 0.01 | 0.00 | 0.03 | 0.00 | 0.00 | `cross_zscore(day_ar1_coefficient(High), 60)` |
| slot a seed 6 | 过 | 0.00 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.02 | 0.07 | 0.09 | 0.18 | 0.09 | 0.03 | `cross_mean(sub(day_ar1_coefficient(High), day_ar1_coefficient(Low)), 20)` |
| slot a seed 7 | 过 | 0.01 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.01 | 0.09 | 0.09 | 0.17 | 0.10 | 0.01 | `cross_mean(div(day_ar1_coefficient(High), day_ar1_coefficient(Low)), 20)` |
| slot a seed 8 | 过 | 0.03 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.08 | 0.03 | 0.01 | 0.05 | 0.03 | 0.04 | `cross_zscore(sub(day_ar1_coefficient(High), day_ar1_coefficient(Close)), 60)` |
| slot a seed 9 | 过 | 0.06 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.11 | 0.04 | 0.04 | 0.03 | 0.02 | 0.04 | `cross_regres(day_std(Ret), day_ar1_coefficient(High), 60)` |
| slot a seed 10 | 过 | 0.11 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.05 | 0.12 | 0.07 | 0.01 | 0.11 | 0.05 | `cross_corr(day_ar1_coefficient(High), day_std(Ret), 60)` |
| slot a seed 11 | 过 | 0.27 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.16 | 0.45 | 0.03 | 0.08 | 0.38 | 0.27 | `cross_stddev(day_ar1_coefficient(High), 30)` |
| slot a seed 12 | 过 | 0.36 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.28 | 0.57 | 0.00 | 0.08 | 0.50 | 0.34 | `cross_quantile(day_ar1_coefficient(High), 0.25, 40)` |
| slot a seed 13 | 过 | 0.26 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.15 | 0.44 | 0.01 | 0.08 | 0.38 | 0.25 | `div(cross_mean(day_ar1_coefficient(High), 20), cross_stddev(day_ar1_coefficient(High), 20))` |
| slot a seed 14 | 过 | 0.02 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.02 | 0.05 | 0.07 | 0.03 | 0.06 | 0.01 | `ts_skew(day_ar1_coefficient(High), 40)` |
| slot a seed 15 | 过 | 0.02 | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 3` | 0.02 | 0.12 | 0.07 | 0.04 | 0.13 | 0.03 | `cross_regbeta(day_ar1_coefficient(Low), day_ar1_coefficient(High), 60)` |
| slot b seed 1 | 过 | 0.38 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.30 | 0.50 | 0.13 | 0.04 | 0.46 | 0.14 | `cross_mean(div(day_std(in_delta(Close, 5)), day_std(in_delta(Close, 1))), 20)` |
| slot b seed 2 | 过 | 0.38 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.30 | 0.52 | 0.11 | 0.03 | 0.47 | 0.21 | `cross_mean(div(day_std(in_delta(Close, 15)), day_std(in_delta(Close, 1))), 20)` |
| slot b seed 3 | 过 | 0.07 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.10 | 0.10 | 0.18 | 0.30 | 0.11 | 0.01 | `sub(cross_mean(div(day_std(in_delta(Close, 5)), day_std(in_delta(Close, 1))), 10), cross_mean(div(day_std(in_delta(Close, 5)), day_std(in_delta(Close, 1))), 60))` |
| slot b seed 4 | 过 | 0.12 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.03 | 0.31 | 0.99 | 0.22 | 0.38 | 0.08 | `cross_mean(day_durbin_watson(Close), 20)` |
| slot b seed 5 | 过 | 0.21 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.13 | 0.15 | 0.12 | 0.08 | 0.10 | 0.08 | `cross_mean(day_hurst(Close), 20)` |
| slot b seed 6 | 过 | 0.15 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.10 | 0.07 | 0.12 | 0.11 | 0.04 | 0.03 | `cross_mean(day_autocorr(Close, 30), 20)` |
| slot b seed 7 | 过 | 0.27 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.22 | 0.16 | 0.12 | 0.06 | 0.16 | 0.18 | `cross_mean(div(abs_(sub(day_last(Close), day_first(Close))), day_sum(abs_(in_delta(Close, 1)))), 20)` |
| slot b seed 8 | 过 | 0.02 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.07 | 0.02 | 0.02 | 0.01 | 0.03 | 0.01 | `cross_zscore(div(abs_(sub(day_last(Close), day_first(Close))), day_sum(abs_(in_delta(Close, 1)))), 60)` |
| slot b seed 9 | 过 | 0.13 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.08 | 0.05 | 0.11 | 0.10 | 0.03 | 0.01 | `cross_mean(abs_(day_corr(Close, in_index(Close))), 20)` |
| slot b seed 10 | 过 | 0.05 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.03 | 0.04 | 0.10 | 0.55 | 0.03 | 0.02 | `cross_mean(day_corr(Close, in_index(Close)), 20)` |
| slot b seed 11 | 过 | 0.33 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.24 | 0.68 | 0.07 | 0.05 | 0.63 | 0.36 | `cross_mean(div(day_std(in_delta(Vwap, 5)), day_std(in_delta(Vwap, 1))), 20)` |
| slot b seed 12 | 过 | 0.05 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.10 | 0.07 | 0.11 | 0.19 | 0.08 | 0.01 | `cross_regres(day_std(Ret), cross_mean(div(day_std(in_delta(Close, 5)), day_std(in_delta(Close, 1))), 5), 60)` |
| R 1 variant 1 | 过 | 0.65 | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 3` | 0.63 | 0.12 | 0.10 | 0.01 | 0.11 | 0.01 | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 5), 80)` |
| R 1 variant 2 | 过 | 0.78 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.78 | 0.22 | 0.09 | 0.04 | 0.20 | 0.09 | `cross_mean(ts_max(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 5), 40)` |
| R 1 variant 3 | 过 | 0.54 | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 3` | 0.56 | 0.07 | 0.02 | 0.03 | 0.09 | 0.17 | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(Vwap), 5), 30), 5), 40)` |
| R 2 variant 1 | 过 | 0.83 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.84 | 0.17 | 0.10 | 0.04 | 0.14 | 0.06 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 60), 10)` |
| R 2 variant 2 | 过 | 0.85 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.85 | 0.18 | 0.10 | 0.04 | 0.16 | 0.07 | `cross_mean(cross_med(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 60), 5)` |
| R 2 variant 3 | 过 | 0.57 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.59 | 0.05 | 0.03 | 0.04 | 0.07 | 0.13 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Vwap), 5), 30), 60), 5)` |
| R 3 variant 1 | 过 | 0.83 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5` | 0.84 | 0.17 | 0.10 | 0.04 | 0.14 | 0.06 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 60), 10)` |
| R 3 variant 2 | 过 | 0.55 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5)` | 0.58 | 0.06 | 0.02 | 0.04 | 0.08 | 0.13 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Vwap), 5), 30), 60), 10)` |
