# 相关度表:种子 2072,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.26 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.14 | 0.17 | 0.14 | 0.01 | 0.20 | 0.01 | `cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60)` |
| slot a seed 1 | 过 | 0.12 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.07 | 0.09 | 0.12 | 0.02 | 0.11 | 0.01 | `cross_zscore(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), 120)` |
| slot a seed 2 | 过 | 0.28 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.17 | 0.15 | 0.11 | 0.01 | 0.18 | 0.00 | `cross_ema(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), 20)` |
| slot a seed 3 | 过 | 0.28 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.17 | 0.16 | 0.13 | 0.00 | 0.19 | 0.00 | `ts_mean(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), 20)` |
| slot a seed 4 | 过 | 0.21 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.13 | 0.14 | 0.03 | 0.04 | 0.15 | 0.04 | `cross_tail_mean_q25(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), 60)` |
| slot a seed 5 | 过 | 0.22 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.11 | 0.15 | 0.20 | 0.01 | 0.18 | 0.07 | `cs_bucket_zscore(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), LimitWidth)` |
| slot a seed 6 | 过 | 0.26 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.14 | 0.18 | 0.13 | 0.02 | 0.21 | 0.01 | `cs_bucket_zscore(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), LogFloatCap)` |
| slot a seed 7 | 过 | 0.24 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.13 | 0.15 | 0.17 | 0.01 | 0.18 | 0.05 | `cs_bucket_demean(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), ListAge)` |
| slot a seed 8 | 过 | 0.39 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.12 | 0.59 | 0.20 | 0.02 | 0.58 | 0.48 | `sub(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), cross_corr(day_flat_ratio(Vwap), day_sum(Amt), 60))` |
| slot a seed 9 | 过 | 0.23 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.14 | 0.12 | 0.01 | 0.02 | 0.14 | 0.02 | `cs_regres(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), cross_mean(day_std(Ret), 60))` |
| slot a seed 10 | 过 | 0.09 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.03 | 0.10 | 0.14 | 0.23 | 0.12 | 0.04 | `mul(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 11 | 过 | 0.24 | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.14 | 0.14 | 0.18 | 0.01 | 0.16 | 0.08 | `cross_mean(cs_bucket_zscore(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), LimitWidth), 20)` |
| slot a seed 12 | 过 | 0.14 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.09 | 0.12 | 0.14 | 0.04 | 0.14 | 0.01 | `sub(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), cross_mean(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), 120))` |
| slot b seed 1 | 过 | 0.08 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.07 | 0.00 | 0.00 | 0.01 | 0.01 | 0.02 | `cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 1), 60)` |
| slot b seed 2 | 过 | 0.10 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.09 | 0.03 | 0.01 | 0.01 | 0.01 | 0.04 | `cross_regbeta(day_sum(Ret), cross_delay(day_sum(Ret), 1), 120)` |
| slot b seed 3 | 过 | 0.02 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hu` | 0.06 | 0.01 | 0.04 | 0.02 | 0.01 | 0.03 | `cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 2), 60)` |
| slot b seed 4 | 过 | 0.11 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.06 | 0.07 | 0.08 | 0.02 | 0.07 | 0.05 | `cross_corr(day_sum(Ret), cross_delay(day_sum(Amt), 1), 60)` |
| slot b seed 5 | 废品 | nan | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.00 | nan | nan | nan | nan | nan | `cross_corr(day_open(Ret), day_sum(Ret), 60)` |
| slot b seed 6 | 过 | 0.07 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.07 | 0.01 | 0.01 | 0.00 | 0.00 | 0.03 | `cs_bucket_zscore(cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 1), 60), LimitWidth)` |
| slot b seed 7 | 过 | 0.09 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.09 | 0.00 | 0.01 | 0.00 | 0.01 | 0.01 | `cs_bucket_zscore(cross_regbeta(day_sum(Ret), cross_delay(day_sum(Ret), 1), 120), LogFloatCap)` |
| slot b seed 8 | 过 | 0.04 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.05 | 0.01 | 0.00 | 0.02 | 0.01 | 0.00 | `cross_zscore(cross_corr(day_sum(Ret), cross_delay(day_sum(Amt), 1), 60), 120)` |
| slot b seed 9 | 过 | 0.04 | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), ` | 0.05 | 0.03 | 0.01 | 0.01 | 0.03 | 0.01 | `sub(cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 1), 60), cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 1), 250))` |
| slot b seed 10 | 过 | 0.04 | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` | 0.08 | 0.01 | 0.06 | 0.02 | 0.03 | 0.01 | `cross_corr(day_sum(Ret), cross_delay(day_flat_ratio(Close), 1), 60)` |
| slot b seed 11 | 过 | 0.08 | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quanti` | 0.07 | 0.01 | 0.02 | 0.01 | 0.00 | 0.02 | `cs_regres(cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 1), 60), cross_mean(day_std(Ret), 60))` |
| slot b seed 12 | 废品 | nan | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))` | 0.00 | nan | nan | nan | nan | nan | `cross_ema(cross_corr(day_open(Ret), day_sum(Ret), 60), 20)` |
