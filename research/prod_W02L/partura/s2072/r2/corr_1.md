# 相关度表:种子 2072,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.89 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.94 | 0.47 | 0.06 | 0.03 | 0.43 | 0.44 | `day_quantile_q25(Low)` |
| slot a seed 1 | 过 | 0.27 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.12 | 0.24 | 0.44 | 0.60 | 0.27 | 0.07 | `cross_zscore(day_quantile_q25(Low), 120)` |
| slot a seed 2 | 过 | 0.31 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.15 | 0.24 | 0.43 | 0.22 | 0.26 | 0.04 | `cross_ema(sub(day_quantile_q25(Low), cross_mean(day_quantile_q25(Low), 120)), 10)` |
| slot a seed 3 | 过 | 0.29 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.31 | 0.28 | 0.41 | 0.16 | 0.28 | 0.05 | `div(day_quantile_q25(Low), day_mean(Vwap))` |
| slot a seed 4 | 过 | 0.54 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.35 | 0.53 | 0.66 | 0.03 | 0.52 | 0.06 | `cross_mean(div(day_quantile_q25(Low), day_mean(Vwap)), 60)` |
| slot a seed 5 | 过 | 0.70 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.85 | 0.18 | 0.11 | 0.01 | 0.16 | 0.01 | `cs_bucket_zscore(day_quantile_q25(Low), LogFloatCap)` |
| slot a seed 6 | 过 | 0.69 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.65 | 0.34 | 0.04 | 0.01 | 0.29 | 0.27 | `cs_bucket_demean(day_quantile_q25(Low), LimitWidth)` |
| slot a seed 7 | 过 | 0.39 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.73 | 0.29 | 0.06 | 0.03 | 0.29 | 0.64 | `cs_regres(day_quantile_q25(Low), LogFloatCap)` |
| slot a seed 8 | 过 | 0.18 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.09 | 0.01 | 0.01 | 0.02 | 0.00 | 0.01 | `ts_hurst(day_quantile_q25(Low), 20)` |
| slot a seed 9 | 过 | 0.86 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.93 | 0.42 | 0.01 | 0.05 | 0.38 | 0.43 | `cross_tail_mean_q25(day_quantile_q25(Low), 60)` |
| slot a seed 10 | 过 | 0.39 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.34 | 0.14 | 0.18 | 0.12 | 0.16 | 0.14 | `cross_corr(day_quantile_q25(Low), day_sum(Amt), 60)` |
| slot a seed 11 | 过 | 0.13 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.15 | 0.12 | 0.34 | 0.74 | 0.15 | 0.01 | `cs_bucket_zscore(cross_zscore(day_quantile_q25(Low), 60), ListAge)` |
| slot a seed 12 | 过 | 0.89 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.94 | 0.45 | 0.02 | 0.05 | 0.40 | 0.43 | `cross_mean(day_quantile_q25(Low), 60)` |
| slot b seed 1 | 过 | 0.43 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.12 | 0.67 | 0.07 | 0.08 | 0.60 | 0.62 | `cross_mean(day_flat_ratio(Vwap), 60)` |
| slot b seed 2 | 过 | 0.61 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.55 | 0.48 | 0.06 | 0.08 | 0.41 | 0.20 | `cross_mean(day_flat_ratio(Close), 120)` |
| slot b seed 3 | 过 | 0.63 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.53 | 0.51 | 0.14 | 0.07 | 0.45 | 0.20 | `cross_mean(day_zero_ratio(Ret), 60)` |
| slot b seed 4 | 过 | 0.58 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.55 | 0.38 | 0.20 | 0.06 | 0.33 | 0.04 | `cross_mean(sub(day_flat_ratio(Vwap), day_zero_ratio(Ret)), 60)` |
| slot b seed 5 | 废品 | 0.42 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.44 | 0.26 | 0.16 | 0.10 | 0.18 | 0.19 | `cross_mean(day_flat_run_max(Close), 60)` |
| slot b seed 6 | 过 | 0.26 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.12 | 0.30 | 0.01 | 0.12 | 0.24 | 0.02 | `cs_bucket_zscore(cross_mean(day_flat_ratio(Vwap), 60), LogFloatCap)` |
| slot b seed 7 | 过 | 0.64 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.41 | 0.61 | 0.10 | 0.06 | 0.55 | 0.38 | `cs_bucket_zscore(cross_mean(day_zero_ratio(Ret), 60), LimitWidth)` |
| slot b seed 8 | 过 | 0.44 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.13 | 0.66 | 0.01 | 0.08 | 0.59 | 0.59 | `cs_regres(cross_mean(day_flat_ratio(Vwap), 60), cross_mean(day_std(Ret), 60))` |
| slot b seed 9 | 过 | 0.09 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.11 | 0.05 | 0.23 | 0.24 | 0.06 | 0.04 | `cross_zscore(day_flat_ratio(Vwap), 120)` |
| slot b seed 10 | 过 | 0.61 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.55 | 0.47 | 0.05 | 0.08 | 0.40 | 0.21 | `cross_mean(sub(day_pos_ratio(Ret), 0.5), 120)` |
| slot b seed 11 | 过 | 0.26 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.14 | 0.17 | 0.14 | 0.01 | 0.20 | 0.01 | `cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60)` |
| slot b seed 12 | 过 | 0.38 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.18 | 0.48 | 0.16 | 0.08 | 0.42 | 0.55 | `cs_bucket_zscore(cross_mean(day_flat_run_max(Vwap), 60), sub(LogFloatCap, LogFloatShares))` |
