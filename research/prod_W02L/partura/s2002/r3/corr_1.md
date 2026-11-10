# 相关度表:种子 2002,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.19 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day` | 0.10 | 0.15 | 0.32 | 0.21 | 0.16 | 0.03 | `day_es_ratio_lo(Vwap)` |
| slot a seed 1 | 过 | 0.41 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day` | 0.24 | 0.37 | 0.72 | 0.33 | 0.40 | 0.07 | `cross_mean(day_es_ratio_lo(Vwap), 20)` |
| slot a seed 2 | 过 | 0.53 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.29 | 0.41 | 0.68 | 0.06 | 0.43 | 0.10 | `cross_mean(day_es_ratio_lo(Vwap), 60)` |
| slot a seed 3 | 过 | 0.51 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.26 | 0.38 | 0.56 | 0.07 | 0.40 | 0.06 | `cross_stddev(day_es_ratio_lo(Vwap), 60)` |
| slot a seed 4 | 过 | 0.05 | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), ` | 0.11 | 0.01 | 0.04 | 0.20 | 0.00 | 0.01 | `cross_zscore(day_es_ratio_lo(Vwap), 60)` |
| slot a seed 5 | 过 | 0.09 | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), ` | 0.10 | 0.03 | 0.17 | 0.47 | 0.05 | 0.06 | `sub(cross_mean(day_es_ratio_lo(Vwap), 10), cross_mean(day_es_ratio_lo(Vwap), 120))` |
| slot a seed 6 | 过 | 0.41 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day` | 0.24 | 0.40 | 0.69 | 0.33 | 0.42 | 0.03 | `cs_bucket_zscore(cross_mean(day_es_ratio_lo(Vwap), 20), LogFloatCap)` |
| slot a seed 7 | 过 | 0.38 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day` | 0.26 | 0.01 | 0.54 | 0.04 | 0.01 | 0.39 | `cs_bucket_zscore(cross_mean(day_es_ratio_lo(Vwap), 60), cross_mean(day_std(Amt), 30))` |
| slot a seed 8 | 过 | 0.25 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.12 | 0.22 | 0.24 | 0.12 | 0.23 | 0.08 | `cross_corr(day_es_ratio_lo(Vwap), ts_delta(log(day_last(Close)), 1), 60)` |
| slot a seed 9 | 过 | 0.45 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day` | 0.33 | 0.42 | 0.78 | 0.18 | 0.44 | 0.08 | `cross_mean(sub(day_es_ratio_lo(Vwap), day_es_ratio_hi(Vwap)), 20)` |
| slot a seed 10 | 过 | 0.52 | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), ` | 0.70 | 0.14 | 0.17 | 0.12 | 0.08 | 0.01 | `cross_mean(sub(day_es_ratio_lo(Vwap), day_es_ratio_lo(Close)), 20)` |
| slot a seed 11 | 过 | 0.07 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.09 | 0.07 | 0.02 | 0.56 | 0.06 | 0.04 | `cross_mean(mul(day_es_ratio_lo(Vwap), sign(ts_delta(log(day_last(Close)), 1))), 20)` |
| slot a seed 12 | 过 | 0.54 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.28 | 0.42 | 0.64 | 0.07 | 0.44 | 0.07 | `cross_tail_mean_q25(day_es_ratio_lo(Vwap), 60)` |
| slot a seed 13 | 过 | 0.08 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_st` | 0.06 | 0.05 | 0.03 | 0.02 | 0.06 | 0.00 | `cross_autocorr(day_es_ratio_lo(Vwap), 60, 1)` |
| slot a seed 14 | 过 | 0.51 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.25 | 0.41 | 0.70 | 0.09 | 0.43 | 0.11 | `cross_ema(day_es_ratio_lo(Vwap), 30)` |
| slot a seed 15 | 过 | 0.50 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.24 | 0.40 | 0.54 | 0.08 | 0.42 | 0.02 | `cs_bucket_zscore(cross_stddev(day_es_ratio_lo(Vwap), 60), LogFloatCap)` |
| slot b seed 1 | 过 | 0.29 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.17 | 0.26 | 0.09 | 0.12 | 0.25 | 0.03 | `cross_mean(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 60)` |
| slot b seed 2 | 过 | 0.26 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.15 | 0.22 | 0.05 | 0.10 | 0.22 | 0.00 | `cross_mean(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 120)` |
| slot b seed 3 | 过 | 0.38 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.17 | 0.36 | 0.34 | 0.22 | 0.38 | 0.07 | `sub(cross_mean(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 60), cross_mean(sub(log(day_last(Close)), log(day_first(Open))), 60))` |
| slot b seed 4 | 过 | 0.17 | `ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volu` | 0.06 | 0.21 | 0.05 | 0.01 | 0.20 | 0.15 | `cross_corr(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), sub(log(day_last(Close)), log(day_first(Open))), 120)` |
| slot b seed 5 | 过 | 0.19 | `ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volu` | 0.07 | 0.21 | 0.02 | 0.00 | 0.20 | 0.12 | `cross_regbeta(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), sub(log(day_last(Close)), log(day_first(Open))), 60)` |
| slot b seed 6 | 过 | 0.28 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.16 | 0.23 | 0.09 | 0.12 | 0.22 | 0.00 | `cs_bucket_zscore(cross_mean(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 60), LogFloatCap)` |
| slot b seed 7 | 过 | 0.23 | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), ` | 0.14 | 0.13 | 0.06 | 0.01 | 0.17 | 0.02 | `div(cross_stddev(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 60), add(cross_stddev(sub(log(day_last(Close)), log(day_first(Open))), 60), 0.0001))` |
| slot b seed 8 | 过 | 0.63 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.33 | 0.50 | 0.47 | 0.05 | 0.52 | 0.01 | `cross_tail_mean_q25(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 60)` |
| slot b seed 9 | 过 | 0.13 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day` | 0.07 | 0.11 | 0.16 | 0.01 | 0.13 | 0.02 | `cross_corr(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), ts_delay(sub(log(day_last(Close)), log(day_first(Open))), 1), 60)` |
| slot b seed 10 | 过 | 0.39 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.20 | 0.38 | 0.35 | 0.26 | 0.40 | 0.08 | `cross_ema(sub(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), sub(log(day_last(Close)), log(day_first(Open)))), 40)` |
| slot b seed 11 | 过 | 0.17 | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_` | 0.17 | 0.04 | 0.20 | 0.20 | 0.03 | 0.20 | `cs_bucket_zscore(sub(cross_mean(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 60), cross_mean(sub(log(day_last(Close)), log(day_first(Open))), 60)), cross_mean(day_std(Amt), 30))` |
| slot b seed 12 | 过 | 0.10 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.05 | 0.11 | 0.10 | 0.13 | 0.11 | 0.04 | `cross_zscore(cross_mean(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 20), 120)` |
