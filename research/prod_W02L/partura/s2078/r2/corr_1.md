# 相关度表:种子 2078,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.66 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.72 | 0.56 | 0.13 | 0.13 | 0.56 | 0.42 | `day_flat_run_max(Volume)` |
| slot a seed 1 | 废品 | 0.81 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.73 | 0.78 | 0.17 | 0.04 | 0.77 | 0.57 | `cross_mean(day_flat_run_max(Volume), 20)` |
| slot a seed 2 | 废品 | 0.67 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.59 | 0.66 | 0.01 | 0.02 | 0.63 | 0.58 | `ts_max(day_flat_run_max(Volume), 30)` |
| slot a seed 3 | 废品 | 0.10 | `pow_2(day_cov(Amt, Vwap))` | 0.06 | 0.03 | 0.12 | 0.19 | 0.01 | 0.06 | `sub(day_flat_run_max(Volume), cross_mean(day_flat_run_max(Volume), 60))` |
| slot a seed 4 | 废品 | 0.17 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.15 | 0.10 | 0.21 | 0.28 | 0.12 | 0.02 | `div(cross_mean(day_flat_run_max(Volume), 5), cross_mean(day_flat_run_max(Volume), 60))` |
| slot a seed 5 | 过 | 0.66 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.63 | 0.53 | 0.15 | 0.09 | 0.54 | 0.34 | `cs_last_low05(cross_mean(day_flat_run_max(Volume), 10), LogTotalCap)` |
| slot a seed 6 | 过 | 0.31 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.46 | 0.21 | 0.04 | 0.05 | 0.22 | 0.06 | `cs_last_low10(day_flat_run_max(Volume), LogFloatCap)` |
| slot a seed 7 | 过 | 0.46 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.44 | 0.43 | 0.00 | 0.03 | 0.41 | 0.25 | `cs_last_low05(ts_max(day_flat_run_max(Volume), 20), LogFloatCap)` |
| slot a seed 8 | 过 | 0.12 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.09 | 0.01 | 0.03 | 0.29 | 0.02 | 0.03 | `mul(day_flat_run_max(Volume), cross_mean(day_mean(Ret), 5))` |
| slot a seed 9 | 过 | 0.09 | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15` | 0.17 | 0.01 | 0.03 | 0.07 | 0.02 | 0.04 | `ts_regbeta(day_mean(Ret), day_flat_run_max(Volume), 60)` |
| slot a seed 10 | 废品 | 0.37 | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15` | 0.14 | 0.36 | 0.15 | 0.02 | 0.36 | 0.17 | `sub(cs_normalize(cross_mean(day_flat_run_max(Volume), 20)), cs_normalize(cross_mean(day_flat_ratio(Volume), 20)))` |
| slot a seed 11 | 过 | 0.56 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.49 | 0.37 | 0.08 | 0.08 | 0.38 | 0.23 | `cross_mean(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), 10)` |
| slot a seed 12 | 废品 | 0.33 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.11 | 0.39 | 0.05 | 0.05 | 0.34 | 0.42 | `ts_stddev(day_flat_run_max(Volume), 30)` |
| slot b seed 1 | 过 | 0.11 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.10 | 0.01 | 0.13 | 0.52 | 0.02 | 0.00 | `cross_mean(div(day_last(Close), day_mean(Close)), 20)` |
| slot b seed 2 | 过 | 0.30 | `pow_2(day_cov(Amt, Vwap))` | 0.33 | 0.36 | 0.42 | 0.23 | 0.35 | 0.03 | `cross_mean(div(day_last(Close), day_quantile_q75(Close)), 20)` |
| slot b seed 3 | 过 | 0.08 | `pow_2(day_cov(Amt, Vwap))` | 0.08 | 0.03 | 0.04 | 0.46 | 0.02 | 0.01 | `sub(cross_mean(div(day_last(Close), day_mean(Close)), 20), cross_mean(div(day_last(Close), day_mean(Close)), 60))` |
| slot b seed 4 | 废品 | 0.36 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.58 | 0.16 | 0.07 | 0.23 | 0.09 | 0.01 | `cross_mean(day_at_max_ratio(Close), 20)` |
| slot b seed 5 | 废品 | 0.24 | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15` | 0.17 | 0.13 | 0.24 | 0.30 | 0.16 | 0.02 | `sub(cross_mean(day_at_max_ratio(Close), 20), cross_mean(day_at_min_ratio(Close), 20))` |
| slot b seed 6 | 过 | 0.10 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.19 | 0.10 | 0.01 | 0.53 | 0.09 | 0.03 | `cross_mean(div(sub(day_last(Close), day_min(Close)), sub(day_max(Close), day_min(Close))), 20)` |
| slot b seed 7 | 过 | 0.26 | `pow_2(day_cov(Amt, Vwap))` | 0.14 | 0.16 | 0.30 | 0.85 | 0.19 | 0.05 | `cross_mean(div(day_last(Close), day_first(Close)), 20)` |
| slot b seed 8 | 废品 | 0.17 | `pow_05(cs_normalize(day_mean(Volume)))` | 0.26 | 0.06 | 0.03 | 0.18 | 0.03 | 0.05 | `ts_max(div(sub(day_last(Close), day_min(Close)), sub(day_max(Close), day_min(Close))), 20)` |
| slot b seed 9 | 过 | 0.23 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), cross_mean` | 0.21 | 0.00 | 0.05 | 0.05 | 0.01 | 0.06 | `ts_regbeta(div(day_last(Close), day_mean(Close)), div(day_mean(High), day_mean(Close)), 60)` |
| slot b seed 10 | 过 | 0.46 | `pow_2(day_cov(Amt, Vwap))` | 0.49 | 0.48 | 0.72 | 0.04 | 0.49 | 0.04 | `cross_mean(div(sub(day_max(Close), day_last(Close)), day_mean(Close)), 20)` |
