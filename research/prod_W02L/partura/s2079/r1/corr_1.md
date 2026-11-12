# 相关度表:种子 2079,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.15 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.09 | 0.10 | 0.21 | 0.24 | 0.11 | 0.00 | `sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1)` |
| slot a seed 1 | 过 | 0.48 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.23 | 0.47 | 0.73 | 0.02 | 0.48 | 0.05 | `cross_mean(sub(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)), 20)` |
| slot a seed 2 | 过 | 0.02 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.12 | 0.03 | 0.03 | 0.18 | 0.03 | 0.01 | `cross_zscore(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 40)` |
| slot a seed 3 | 过 | 0.09 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.31 | 0.10 | 0.02 | 0.46 | 0.08 | 0.03 | `sub(cross_mean(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 5), cross_mean(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 60))` |
| slot a seed 4 | 过 | 0.05 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.30 | 0.02 | 0.04 | 0.12 | 0.01 | 0.01 | `cross_regres(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 5 | 过 | 0.24 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.10 | 0.35 | 0.26 | 0.18 | 0.35 | 0.17 | `cross_corr(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 40)` |
| slot a seed 6 | 过 | 0.54 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.31 | 0.48 | 0.70 | 0.03 | 0.48 | 0.06 | `cross_ema(sub(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1)), 30)` |
| slot a seed 7 | 过 | 0.05 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.19 | 0.09 | 0.03 | 0.59 | 0.08 | 0.01 | `cross_delta(cross_mean(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 10), 20)` |
| slot a seed 8 | 过 | 0.47 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.20 | 0.43 | 0.72 | 0.47 | 0.45 | 0.01 | `cs_bucket_demean(cross_mean(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), LogFloatCap)` |
| slot a seed 9 | 过 | 0.62 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.46 | 0.50 | 0.69 | 0.09 | 0.52 | 0.04 | `cross_tail_mean_q75(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 10 | 过 | 0.33 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.39 | 0.09 | 0.05 | 0.08 | 0.06 | 0.14 | `cross_regbeta(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 1 | 过 | 0.28 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.07 | 0.44 | 0.49 | 0.19 | 0.48 | 0.04 | `cross_mean(day_centroid(Amt), 20)` |
| slot b seed 2 | 过 | 0.03 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.20 | 0.04 | 0.00 | 0.13 | 0.03 | 0.00 | `cross_zscore(day_centroid(Amt), 40)` |
| slot b seed 3 | 过 | 0.05 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.27 | 0.01 | 0.07 | 0.25 | 0.00 | 0.02 | `sub(cross_mean(day_centroid(Amt), 5), cross_mean(day_centroid(Amt), 60))` |
| slot b seed 4 | 过 | 0.04 | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 24` | 0.06 | 0.07 | 0.01 | 0.01 | 0.06 | 0.08 | `cross_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Amt, 1, 239)), 20)` |
| slot b seed 5 | 过 | 0.01 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | `cross_zscore(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), 40)` |
| slot b seed 6 | 废品 | 0.03 | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 24` | 0.10 | 0.01 | 0.11 | 0.50 | 0.02 | 0.02 | `cross_mean(sub(day_argmax(High), day_argmin(Low)), 20)` |
| slot b seed 7 | 过 | 0.06 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.13 | 0.06 | 0.17 | 0.33 | 0.08 | 0.03 | `cross_ema(sub(day_argmax(High), day_argmin(Low)), 30)` |
| slot b seed 8 | 过 | 0.05 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.07 | 0.01 | 0.13 | 0.64 | 0.03 | 0.04 | `cross_mean(sub(day_centroid(Amt), day_centroid(Volume)), 20)` |
| slot b seed 9 | 过 | 0.04 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.01 | 0.07 | 0.11 | 0.00 | 0.08 | 0.09 | `cross_corr(day_centroid(Amt), day_sum(Ret), 40)` |
| slot b seed 10 | 过 | 0.28 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.07 | 0.44 | 0.48 | 0.18 | 0.48 | 0.01 | `cs_bucket_demean(cross_mean(day_centroid(Amt), 20), LogFloatCap)` |
| slot b seed 11 | 废品 | 0.29 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open)` | 0.02 | 0.48 | 0.31 | 0.29 | 0.48 | 0.14 | `cross_mean(sub(day_argmax(Amt), day_argmax(High)), 20)` |
| slot b seed 12 | 过 | 0.25 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.08 | 0.24 | 0.35 | 0.58 | 0.26 | 0.04 | `cross_mean(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 20)` |
| R 1 variant 1 | 过 | 0.65 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.54 | 0.31 | 0.48 | 0.21 | 0.34 | 0.02 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 50), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |
| R 1 variant 2 | 过 | 0.71 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.63 | 0.28 | 0.45 | 0.22 | 0.30 | 0.02 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 50), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 50))` |
| R 1 variant 3 | 过 | 0.69 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.59 | 0.43 | 0.58 | 0.00 | 0.44 | 0.11 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100)` |
| R 1 variant 4 | 过 | 0.59 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close` | 0.46 | 0.35 | 0.51 | 0.18 | 0.39 | 0.06 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 50), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 200))` |
