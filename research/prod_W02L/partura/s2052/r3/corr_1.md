# 相关度表:种子 2052,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.30 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.27 | 0.17 | 0.53 | 0.28 | 0.20 | 0.11 | `day_max(Ret)` |
| slot a seed 1 | 过 | 0.24 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.20 | 0.01 | 0.12 | 0.15 | 0.01 | 0.35 | `cross_mean(div(day_max(Ret), day_std(Ret)), 20)` |
| slot a seed 2 | 过 | 0.10 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 16, 226), ` | 0.05 | 0.04 | 0.14 | 0.08 | 0.05 | 0.02 | `cross_regres(cross_mean(day_max(Ret), 20), cross_mean(day_std(Ret), 20), 60)` |
| slot a seed 3 | 过 | 0.25 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 2, 237), d` | 0.16 | 0.04 | 0.07 | 0.45 | 0.02 | 0.08 | `sub(cross_mean(day_max(Ret), 5), cross_mean(day_max(Ret), 60))` |
| slot a seed 4 | 过 | 0.32 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 2, 237), d` | 0.11 | 0.01 | 0.21 | 0.51 | 0.02 | 0.03 | `cross_mean(cross_zscore(day_max(Ret), 60), 10)` |
| slot a seed 5 | 过 | 0.29 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.21 | 0.14 | 0.28 | 0.30 | 0.18 | 0.12 | `cross_mean(sub(day_max(Ret), abs_(day_min(Ret))), 20)` |
| slot a seed 6 | 过 | 0.35 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.19 | 0.30 | 0.56 | 0.14 | 0.37 | 0.05 | `cross_mean(div(day_max(Ret), LimitWidth), 30)` |
| slot a seed 7 | 过 | 0.42 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.28 | 0.73 | 0.40 | 0.05 | 0.76 | 0.26 | `cross_cov(day_max(Ret), day_sum(Amt), 60)` |
| slot a seed 8 | 过 | 0.13 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.11 | 0.02 | 0.04 | 0.09 | 0.04 | 0.09 | `cross_corr(day_max(Ret), day_wmean(Ret, Amt), 60)` |
| slot a seed 9 | 过 | 0.13 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.12 | 0.10 | 0.09 | 0.10 | 0.06 | 0.29 | `cross_stddev(div(day_max(Ret), day_std(Ret)), 30)` |
| slot a seed 10 | 过 | 0.43 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.32 | 0.25 | 0.69 | 0.04 | 0.29 | 0.28 | `cross_quantile(day_max(Ret), 0.9, 60)` |
| slot a seed 11 | 过 | 0.47 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.32 | 0.29 | 0.85 | 0.21 | 0.34 | 0.22 | `cross_decay_linear(sub(day_max(Ret), day_wmean(Ret, Amt)), 30)` |
| slot a seed 12 | 过 | 0.21 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.11 | 0.17 | 0.34 | 0.11 | 0.20 | 0.09 | `cross_regres(cross_mean(div(day_max(Ret), day_std(Ret)), 10), cross_mean(day_std(Ret), 60), 120)` |
| slot b seed 1 | 过 | 0.22 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 2, 237), d` | 0.13 | 0.11 | 0.21 | 0.38 | 0.13 | 0.14 | `div(day_open(Open), ts_max(day_open(Open), 250))` |
| slot b seed 2 | 过 | 0.36 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.17 | 0.39 | 0.53 | 0.30 | 0.40 | 0.12 | `div(day_open(Open), ts_min(day_open(Open), 250))` |
| slot b seed 3 | 废品 | 0.35 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.19 | 0.30 | 0.47 | 0.46 | 0.32 | 0.09 | `ts_rank(day_open(Open), 250)` |
| slot b seed 4 | 过 | 0.19 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Low), 5),` | 0.16 | 0.30 | 0.32 | 0.17 | 0.29 | 0.03 | `div(sub(ts_max(day_open(Open), 120), ts_min(day_open(Open), 120)), day_open(Open))` |
| slot b seed 5 | 过 | 0.38 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 2, 237), d` | 0.25 | 0.24 | 0.44 | 0.54 | 0.27 | 0.08 | `div(day_open(Open), cross_mean(day_open(Open), 120))` |
| slot b seed 6 | 过 | 0.29 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.14 | 0.34 | 0.45 | 0.15 | 0.35 | 0.11 | `div(cross_mean(day_open(Open), 20), cross_mean(day_open(Open), 250))` |
| slot b seed 7 | 过 | 0.12 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.07 | 0.26 | 0.31 | 0.03 | 0.27 | 0.09 | `sub(div(day_open(Open), ts_max(day_open(Open), 250)), div(day_open(Open), ts_max(day_open(Open), 60)))` |
| slot b seed 8 | 废品 | 0.14 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.05 | 0.25 | 0.30 | 0.08 | 0.27 | 0.15 | `cross_argmax(day_open(Open), 250)` |
| slot b seed 9 | 废品 | 0.10 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.04 | 0.17 | 0.17 | 0.04 | 0.17 | 0.06 | `cross_argmin(day_open(Open), 250)` |
| slot b seed 10 | 过 | 0.23 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 2, 237), d` | 0.13 | 0.10 | 0.21 | 0.40 | 0.12 | 0.14 | `div(day_last(Close), ts_max(day_last(Close), 250))` |
| slot b seed 11 | 过 | 0.17 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.11 | 0.11 | 0.13 | 0.04 | 0.12 | 0.15 | `cross_corr(day_open(Open), day_sum(Amt), 120)` |
| slot b seed 12 | 废品 | 0.21 | `cross_mean(day_tide_change(in_slice(Vwap, 31, 211), day_argm` | 0.14 | 0.32 | 0.36 | 0.18 | 0.32 | 0.08 | `sub(cross_rank(day_open(Open), 250), cross_rank(day_open(Open), 20))` |
