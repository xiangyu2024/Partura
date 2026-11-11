# 相关度表:种子 2073,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.94 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.99 | 0.52 | 0.26 | 0.13 | 0.49 | 0.36 | `day_cov(Low, High)` |
| slot a seed 1 | 过 | 0.57 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.33 | 0.49 | 0.74 | 0.20 | 0.51 | 0.00 | `cross_mean(div(day_cov(Low, High), mul(day_mean(Close), day_mean(Close))), 20)` |
| slot a seed 2 | 过 | 0.27 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.11 | 0.11 | 0.25 | 0.39 | 0.13 | 0.04 | `cross_zscore(log(day_cov(Low, High)), 120)` |
| slot a seed 3 | 过 | 0.34 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.17 | 0.21 | 0.46 | 0.47 | 0.24 | 0.06 | `sub(cross_mean(log(day_cov(Low, High)), 10), cross_mean(log(day_cov(Low, High)), 120))` |
| slot a seed 4 | 过 | 0.46 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.26 | 0.52 | 0.09 | 0.03 | 0.47 | 0.16 | `cross_mean(div(day_cov(Low, High), day_cov(Close, Close)), 20)` |
| slot a seed 5 | 过 | 0.07 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.07 | 0.01 | 0.03 | 0.02 | 0.02 | 0.01 | `cross_regres(log(day_sum(Amt)), log(day_cov(Low, High)), 60)` |
| slot a seed 6 | 过 | 0.09 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.08 | 0.07 | 0.05 | 0.01 | 0.07 | 0.01 | `cross_corr(day_cov(Low, High), day_sum(Amt), 60)` |
| slot a seed 7 | 过 | 0.73 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.69 | 0.45 | 0.22 | 0.15 | 0.45 | 0.41 | `cs_bucket_zscore(log(day_cov(Low, High)), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 8 | 过 | 0.19 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.09 | 0.02 | 0.14 | 0.26 | 0.04 | 0.02 | `cross_zscore(div(day_cov(Low, High), mul(day_mean(Close), day_mean(Close))), 120)` |
| slot a seed 9 | 过 | 0.36 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.24 | 0.19 | 0.40 | 0.44 | 0.22 | 0.08 | `cross_ema(div(day_cov(Low, High), cross_mean(day_cov(Low, High), 60)), 10)` |
| slot a seed 10 | 过 | 0.13 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.21 | 0.10 | 0.14 | 0.04 | 0.14 | 0.28 | `cs_bucket_zscore(cross_mean(div(day_cov(Low, High), day_cov(Close, Close)), 20), cross_mean(day_sum(Amt), 30))` |
| slot b seed 1 | 过 | 0.65 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.09 | 0.69 | 0.39 | 0.12 | 0.69 | 0.27 | `cross_mean(day_corr(in_index(Amt), Amt), 20)` |
| slot b seed 2 | 过 | 0.49 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.06 | 0.44 | 0.49 | 0.19 | 0.48 | 0.04 | `cross_mean(day_centroid(Amt), 20)` |
| slot b seed 3 | 过 | 0.22 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(` | 0.33 | 0.07 | 0.27 | 0.12 | 0.12 | 0.07 | `cross_mean(sub(day_centroid(Amt), day_centroid(abs_(Ret))), 20)` |
| slot b seed 4 | 过 | 0.14 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.04 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Amt), 120)` |
| slot b seed 5 | 过 | 0.11 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.10 | 0.01 | 0.13 | 0.64 | 0.03 | 0.04 | `cross_mean(sub(day_centroid(Amt), day_centroid(Volume)), 20)` |
| slot b seed 6 | 过 | 0.65 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.09 | 0.69 | 0.39 | 0.12 | 0.69 | 0.27 | `cross_mean(day_corr(in_index(Close), Amt), 20)` |
| slot b seed 7 | 过 | 0.53 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.32 | 0.58 | 0.23 | 0.05 | 0.55 | 0.19 | `cross_mean(day_corr(in_index(Amt), abs_(Ret)), 20)` |
| slot b seed 8 | 过 | 0.12 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(` | 0.05 | 0.00 | 0.38 | 0.20 | 0.05 | 0.28 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), cross_mean(day_sum(Amt), 30))` |
| slot b seed 9 | 过 | 0.09 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.15 | 0.00 | 0.17 | 0.61 | 0.02 | 0.14 | `cross_mean(day_signed_ratio(Ret, Amt), 20)` |
