# 相关度表:种子 2051,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.25 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.58 | 0.09 | 0.01 | 0.07 | 0.11 | 0.15 | `cross_mean(day_kurt(in_delta(Vwap, 1)), 20)` |
| slot a seed 2 | 过 | 0.12 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.17 | 0.23 | 0.09 | 0.07 | 0.26 | 0.11 | `cross_mean(day_skew(in_delta(Vwap, 1)), 60)` |
| slot a seed 3 | 过 | 0.25 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.49 | 0.08 | 0.05 | 0.05 | 0.12 | 0.17 | `cross_mean(day_kurt(in_logchg(Vwap, 5)), 40)` |
| slot a seed 4 | 过 | 0.27 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.59 | 0.16 | 0.00 | 0.10 | 0.18 | 0.02 | `cross_mean(day_max(in_zscore_rolling(Vwap, 30)), 20)` |
| slot a seed 5 | 过 | 0.26 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.46 | 0.01 | 0.21 | 0.14 | 0.00 | 0.08 | `cross_mean(day_min(in_zscore_rolling(Vwap, 30)), 20)` |
| slot a seed 6 | 过 | 0.14 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.36 | 0.17 | 0.13 | 0.21 | 0.18 | 0.02 | `sub(cross_mean(day_max(in_zscore_rolling(Vwap, 30)), 20), cross_mean(abs_(day_min(in_zscore_rolling(Vwap, 30))), 20))` |
| slot a seed 7 | 过 | 0.11 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.21 | 0.42 | 0.32 | 0.10 | 0.44 | 0.32 | `cross_mean(day_max(in_madz(Vwap, 30)), 20)` |
| slot a seed 8 | 过 | 0.21 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.48 | 0.09 | 0.00 | 0.06 | 0.10 | 0.21 | `cross_mean(day_es_ratio_hi(in_delta(Vwap, 1)), 20)` |
| slot a seed 9 | 过 | 0.10 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.10 | 0.02 | 0.09 | 0.00 | 0.04 | 0.10 | `cross_mean(sub(day_es_ratio_hi(in_delta(Vwap, 1)), day_es_ratio_lo(in_delta(Vwap, 1))), 60)` |
| slot a seed 10 | 过 | 0.23 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.45 | 0.03 | 0.01 | 0.04 | 0.01 | 0.19 | `cross_stddev(day_kurt(in_delta(Vwap, 1)), 60)` |
| slot a seed 11 | 过 | 0.24 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.26 | 0.02 | 0.21 | 0.05 | 0.01 | 0.30 | `cross_mean(div(day_max(in_stddev_rolling(in_delta(Vwap, 1), 10)), day_mean(in_stddev_rolling(in_delta(Vwap, 1), 10))), 20)` |
| slot a seed 12 | 过 | 0.23 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.56 | 0.21 | 0.01 | 0.03 | 0.22 | 0.00 | `cs_bucket_demean(cross_mean(day_kurt(in_delta(Vwap, 1)), 40), LogFloatCap)` |
| slot a seed 13 | 过 | 0.11 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.11 | 0.17 | 0.11 | 0.03 | 0.20 | 0.06 | `cross_corr(day_kurt(in_delta(Vwap, 1)), day_kurt(Volume), 60)` |
| slot a seed 14 | 过 | 0.02 | `day_skew(nt_ts_kurt(Low, 10))` | 0.06 | 0.03 | 0.04 | 0.07 | 0.01 | 0.16 | `cross_ema(sub(day_kurt(in_delta(Low, 1)), day_kurt(in_delta(High, 1))), 30)` |
| slot b seed 1 | 废品 | 0.01 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.07 | 0.07 | 0.06 | 0.33 | 0.08 | 0.01 | `cross_mean(day_argmax(Vwap), 20)` |
| slot b seed 2 | 废品 | 0.06 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.16 | 0.05 | 0.18 | 0.48 | 0.07 | 0.01 | `cross_mean(day_argmin(Vwap), 20)` |
| slot b seed 3 | 废品 | 0.04 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.06 | 0.01 | 0.09 | 0.51 | 0.00 | 0.00 | `cross_mean(sub(day_argmax(Vwap), day_argmin(Vwap)), 20)` |
| slot b seed 4 | 过 | 0.04 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.08 | 0.06 | 0.17 | 0.32 | 0.08 | 0.02 | `cross_mean(sub(day_argmax(High), day_argmin(Low)), 40)` |
| slot b seed 5 | 过 | 0.08 | `day_skew(nt_ts_kurt(Low, 10))` | 0.11 | 0.44 | 0.49 | 0.19 | 0.48 | 0.04 | `cross_mean(day_centroid(Amt), 20)` |
| slot b seed 6 | 过 | 0.01 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.07 | 0.07 | 0.06 | 0.33 | 0.08 | 0.01 | `sub(cross_mean(day_argmax(Vwap), 20), cross_mean(day_centroid(Amt), 20))` |
| slot b seed 7 | 过 | 0.05 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.10 | 0.04 | 0.10 | 0.56 | 0.02 | 0.02 | `cross_mean(day_corr(Vwap, in_index(Vwap)), 20)` |
| slot b seed 8 | 过 | 0.09 | `day_skew(nt_ts_kurt(Low, 10))` | 0.10 | 0.33 | 0.19 | 0.02 | 0.33 | 0.04 | `cross_mean(day_corr(Vwap, Amt), 40)` |
| slot b seed 9 | 过 | 0.08 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.18 | 0.31 | 0.28 | 0.21 | 0.24 | 0.33 | `cross_mean(day_at_max_ratio(Vwap), 20)` |
| slot b seed 10 | 过 | 0.15 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.19 | 0.54 | 0.04 | 0.04 | 0.50 | 0.41 | `cross_mean(day_at_min_ratio(Vwap), 20)` |
| slot b seed 11 | 过 | 0.01 | `day_skew(nt_ts_kurt(Low, 10))` | 0.07 | 0.08 | 0.06 | 0.31 | 0.09 | 0.00 | `cs_bucket_demean(cross_mean(day_argmax(Vwap), 20), LogFloatCap)` |
| slot b seed 12 | 过 | 0.07 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.08 | 0.01 | 0.15 | 0.08 | 0.05 | 0.15 | `cross_corr(day_argmax(Vwap), day_sum(Ret), 60)` |
| slot b seed 13 | 过 | 0.03 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.09 | 0.07 | 0.04 | 0.22 | 0.07 | 0.02 | `cross_ema(sub(day_argmax(Vwap), day_centroid(Amt)), 30)` |
| slot b seed 14 | 过 | 0.06 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.10 | 0.01 | 0.18 | 0.27 | 0.03 | 0.03 | `cross_mean(day_corr(Vwap, in_index(Vwap)), 60)` |
