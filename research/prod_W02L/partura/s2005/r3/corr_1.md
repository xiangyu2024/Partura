# 相关度表:种子 2005,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 1.00 | 0.72 | 0.21 | 0.01 | 0.73 | 0.38 | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` |
| slot a seed 1 | 过 | 0.62 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.86 | 0.06 | 0.07 | 0.06 | 0.07 | 0.05 | `cs_bucket_zscore(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), cross_mean(day_std(Amt), 30))` |
| slot a seed 2 | 过 | 0.80 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.70 | 0.51 | 0.21 | 0.02 | 0.53 | 0.18 | `cs_bucket_zscore(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), LogFloatCap)` |
| slot a seed 3 | 过 | 0.44 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.64 | 0.00 | 0.11 | 0.14 | 0.04 | 0.10 | `div(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), ts_mean(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| slot a seed 4 | 过 | 0.62 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.77 | 0.14 | 0.19 | 0.06 | 0.18 | 0.05 | `div(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), cross_mean(day_cov(Amt, Amt), 241))` |
| slot a seed 5 | 过 | 0.50 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.96 | 0.17 | 0.15 | 0.07 | 0.15 | 0.21 | `div(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), mul(cross_mean(day_std(Amt), 30), cross_mean(day_std(Amt), 30)))` |
| slot a seed 6 | 过 | 0.52 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.54 | 0.23 | 0.23 | 0.07 | 0.26 | 0.11 | `cross_zscore(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), 241)` |
| slot a seed 7 | 过 | 0.25 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.27 | 0.10 | 0.15 | 0.07 | 0.13 | 0.04 | `sub(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), ts_delay(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), 60))` |
| slot a seed 8 | 过 | 0.81 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.76 | 0.63 | 0.13 | 0.02 | 0.64 | 0.54 | `cs_last_low10(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), ListAge)` |
| slot a seed 9 | 过 | 0.46 | `cross_max(day_cov(Ret, Close), 241)` | 0.34 | 0.21 | 0.02 | 0.07 | 0.15 | 0.03 | `div(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), ts_std(cross_stddev(day_cov(Volume, Volume), 60), 50))` |
| slot a seed 10 | 过 | 0.41 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.28 | 0.35 | 0.11 | 0.04 | 0.31 | 0.30 | `cs_bucket_zscore(div(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), ts_std(cross_stddev(day_cov(Volume, Volume), 60), 50)), LogFloatCap)` |
| slot a seed 11 | 过 | 0.60 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.51 | 0.34 | 0.06 | 0.01 | 0.37 | 0.23 | `cs_bucket_demean(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 12 | 过 | 0.24 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.62 | 0.13 | 0.14 | 0.04 | 0.10 | 0.64 | `cs_first_low40(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), LogFloatCap)` |
| slot a seed 13 | 废品 | 0.42 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.45 | 0.17 | 0.20 | 0.10 | 0.20 | 0.09 | `ts_rank(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), 120)` |
| slot a seed 14 | 过 | 0.25 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.33 | 0.01 | 0.14 | 0.08 | 0.03 | 0.17 | `cross_ema(div(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), ts_mean(cross_stddev(day_cov(Amt, Amt), 60), 50)), 20)` |
| slot a seed 15 | 过 | 0.28 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.46 | 0.04 | 0.12 | 0.08 | 0.01 | 0.06 | `cs_bucket_zscore(cross_zscore(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), 120), cross_mean(day_std(Amt), 30))` |
| slot a seed 16 | 过 | 0.09 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.06 | 0.10 | 0.12 | 0.00 | 0.10 | 0.05 | `sub(cross_zscore(ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50), 241), cross_zscore(ts_std(cross_stddev(day_cov(Volume, Volume), 60), 50), 241))` |
| slot b seed 1 | 过 | 0.30 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.31 | 0.07 | 0.24 | 0.02 | 0.10 | 0.16 | `ts_std(cross_stddev(day_gini(Amt), 60), 50)` |
| slot b seed 2 | 过 | 0.12 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.15 | 0.03 | 0.04 | 0.01 | 0.00 | 0.08 | `ts_std(cross_stddev(day_skew(Amt), 60), 50)` |
| slot b seed 3 | 过 | 0.07 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.12 | 0.07 | 0.02 | 0.02 | 0.04 | 0.08 | `ts_std(cross_stddev(day_kurt(Amt), 60), 50)` |
| slot b seed 4 | 过 | 0.23 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.28 | 0.02 | 0.19 | 0.03 | 0.02 | 0.22 | `ts_std(cross_stddev(day_centroid(Amt), 60), 50)` |
| slot b seed 5 | 过 | 0.20 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.26 | 0.07 | 0.16 | 0.03 | 0.01 | 0.20 | `ts_std(cross_stddev(day_es_ratio_hi(Amt), 60), 50)` |
| slot b seed 6 | 废品 | 0.12 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.08 | 0.09 | 0.09 | 0.03 | 0.09 | 0.16 | `ts_std(cross_stddev(day_at_max_ratio(Amt), 60), 50)` |
| slot b seed 7 | 过 | 0.46 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.54 | 0.11 | 0.31 | 0.03 | 0.14 | 0.28 | `ts_std(cross_stddev(day_std(Ret), 60), 50)` |
| slot b seed 8 | 过 | 0.90 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.81 | 0.59 | 0.27 | 0.01 | 0.61 | 0.19 | `ts_std(cross_stddev(day_cov(Ret, Amt), 60), 50)` |
| slot b seed 9 | 过 | 0.77 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.78 | 0.52 | 0.20 | 0.04 | 0.49 | 0.29 | `ts_std(cross_stddev(day_cov(Close, Close), 60), 50)` |
| slot b seed 10 | 过 | 0.27 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.30 | 0.02 | 0.17 | 0.03 | 0.05 | 0.17 | `div(ts_std(cross_stddev(day_gini(Amt), 60), 50), ts_mean(cross_stddev(day_gini(Amt), 60), 50))` |
| slot b seed 11 | 过 | 0.14 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.21 | 0.03 | 0.04 | 0.01 | 0.02 | 0.16 | `cross_corr(cross_stddev(day_std(Amt), 60), cross_stddev(day_std(Ret), 60), 120)` |
| slot b seed 12 | 过 | 0.37 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.39 | 0.09 | 0.24 | 0.02 | 0.12 | 0.20 | `ts_std(cross_stddev(day_zero_ratio(Ret), 60), 50)` |
| slot b seed 13 | 过 | 0.97 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)),` | 0.95 | 0.62 | 0.22 | 0.01 | 0.64 | 0.28 | `ts_std(cross_stddev(day_std(Amt), 60), 50)` |
| slot b seed 14 | 过 | 0.27 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.11 | 0.34 | 0.13 | 0.02 | 0.32 | 0.49 | `ts_std(cross_stddev(day_es_ratio_lo(Amt), 60), 50)` |
| R 1 variant 1 | 过 | 0.81 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stdd` | 0.43 | 0.75 | 0.21 | 0.07 | 0.76 | 0.44 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stddev(day_cov(Amt, Amt), 120), 100))` |
| R 1 variant 2 | 过 | 0.91 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stdd` | 0.73 | 0.77 | 0.21 | 0.06 | 0.78 | 0.46 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 100))` |
| R 1 variant 3 | 过 | 0.80 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stdd` | 0.27 | 0.79 | 0.28 | 0.14 | 0.81 | 0.47 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stddev(day_cov(Amt, Amt), 120), 50))` |
| R 1 variant 4 | 过 | 0.90 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stdd` | 0.65 | 0.84 | 0.29 | 0.09 | 0.86 | 0.49 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stddev(day_cov(Amt, Amt), 30), 50))` |
| R 1 variant 5 | 过 | 0.83 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_std` | 0.63 | 0.69 | 0.13 | 0.04 | 0.69 | 0.39 | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 120)` |
| R 1 variant 6 | 过 | 0.66 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_std` | 0.32 | 0.59 | 0.04 | 0.06 | 0.59 | 0.37 | `ts_std(cross_stddev(day_cov(Amt, Amt), 120), 241)` |
| R 2 variant 1 | 过 | 0.80 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_std` | 0.40 | 0.77 | 0.18 | 0.04 | 0.77 | 0.45 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 120), 100))` |
| R 2 variant 2 | 过 | 0.90 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_std` | 0.69 | 0.78 | 0.18 | 0.04 | 0.78 | 0.46 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 100))` |
