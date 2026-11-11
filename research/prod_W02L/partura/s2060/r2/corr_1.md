# 相关度表:种子 2060,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.35 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.78 | 0.17 | 0.08 | 0.04 | 0.15 | 0.01 | `day_at_max_ratio(Open)` |
| slot a seed 1 | 废品 | 0.51 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.70 | 0.17 | 0.07 | 0.22 | 0.10 | 0.01 | `cross_mean(day_at_max_ratio(Open), 20)` |
| slot a seed 2 | 过 | 0.40 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.48 | 0.01 | 0.22 | 0.08 | 0.06 | 0.01 | `cross_ema(day_at_max_ratio(Open), 60)` |
| slot a seed 3 | 过 | 0.07 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.18 | 0.08 | 0.05 | 0.04 | 0.09 | 0.01 | `cross_zscore(day_at_max_ratio(Open), 60)` |
| slot a seed 4 | 废品 | 0.20 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.19 | 0.13 | 0.20 | 0.03 | 0.15 | 0.01 | `sub(cross_mean(day_at_max_ratio(Open), 5), cross_mean(day_at_max_ratio(Open), 60))` |
| slot a seed 5 | 过 | 0.16 | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coeffic` | 0.21 | 0.12 | 0.16 | 0.09 | 0.16 | 0.02 | `cross_corr(day_at_max_ratio(Open), day_sum(Ret), 40)` |
| slot a seed 6 | 过 | 0.24 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.19 | 0.23 | 0.23 | 0.05 | 0.24 | 0.04 | `cross_corr(day_at_max_ratio(Open), day_std(Ret), 40)` |
| slot a seed 7 | 废品 | 0.38 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.61 | 0.04 | 0.12 | 0.20 | 0.02 | 0.03 | `cs_bucket_demean(cross_mean(day_at_max_ratio(Open), 20), LogFloatCap)` |
| slot a seed 8 | 过 | 0.02 | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coeffic` | 0.03 | 0.01 | 0.01 | 0.00 | 0.02 | 0.00 | `cross_autocorr(day_at_max_ratio(Open), 30, 3)` |
| slot a seed 9 | 废品 | 0.05 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.28 | 0.02 | 0.02 | 0.04 | 0.02 | 0.00 | `sub(day_at_max_ratio(Open), day_at_min_ratio(Open))` |
| slot a seed 10 | 废品 | 0.27 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.17 | 0.18 | 0.29 | 0.20 | 0.21 | 0.03 | `cross_mean(sub(day_at_max_ratio(Open), day_at_min_ratio(Open)), 30)` |
| slot a seed 11 | 过 | 0.41 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.59 | 0.06 | 0.18 | 0.19 | 0.02 | 0.01 | `cross_stddev(day_at_max_ratio(Open), 30)` |
| slot a seed 12 | 废品 | 0.25 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.13 | 0.09 | 0.21 | 0.50 | 0.12 | 0.03 | `mul(cross_mean(day_at_max_ratio(Open), 10), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 13 | 过 | 0.03 | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coeffic` | 0.12 | 0.02 | 0.02 | 0.01 | 0.03 | 0.00 | `cross_zscore(sub(day_at_max_ratio(Open), day_at_max_ratio(Close)), 60)` |
| slot a seed 14 | 过 | 0.10 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.18 | 0.06 | 0.17 | 0.05 | 0.08 | 0.03 | `cross_corr(day_at_max_ratio(Open), day_ar1_coefficient(Volume), 60)` |
| slot b seed 1 | 过 | 0.02 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.07 | 0.01 | 0.03 | 0.12 | 0.02 | 0.02 | `cross_zscore(day_corr(Volume, Ret), 60)` |
| slot b seed 2 | 过 | 0.22 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.20 | 0.07 | 0.12 | 0.21 | 0.08 | 0.01 | `cross_zscore(day_corr(Volume, abs(Ret)), 120)` |
| slot b seed 3 | 过 | 0.06 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.06 | 0.07 | 0.06 | 0.24 | 0.06 | 0.00 | `sub(cross_mean(day_corr(Volume, Ret), 5), cross_mean(day_corr(Volume, Ret), 60))` |
| slot b seed 4 | 过 | 0.38 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.28 | 0.07 | 0.20 | 0.35 | 0.10 | 0.01 | `sub(cross_mean(day_corr(Volume, abs(Ret)), 10), cross_mean(day_corr(Volume, abs(Ret)), 60))` |
| slot b seed 5 | 过 | 0.07 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.14 | 0.04 | 0.01 | 0.12 | 0.04 | 0.01 | `cross_zscore(day_argmax(Volume), 60)` |
| slot b seed 6 | 过 | 0.10 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.09 | 0.02 | 0.05 | 0.12 | 0.01 | 0.01 | `cross_zscore(day_argmax(Amt), 120)` |
| slot b seed 7 | 过 | 0.37 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.54 | 0.09 | 0.14 | 0.07 | 0.07 | 0.02 | `cross_corr(day_corr(Volume, abs(Ret)), day_std(Ret), 60)` |
| slot b seed 8 | 过 | 0.70 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.58 | 0.46 | 0.25 | 0.14 | 0.46 | 0.03 | `cs_bucket_zscore(cross_mean(day_corr(Volume, abs(Ret)), 20), LogFloatCap)` |
| slot b seed 9 | 过 | 0.01 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.10 | 0.01 | 0.01 | 0.14 | 0.01 | 0.02 | `cross_zscore(day_corr(Amt, Ret), 120)` |
| slot b seed 10 | 过 | 0.38 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.29 | 0.28 | 0.17 | 0.04 | 0.28 | 0.02 | `cross_mean(day_corr(Vwap, Volume), 30)` |
| slot b seed 11 | 过 | 0.23 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.17 | 0.04 | 0.12 | 0.17 | 0.05 | 0.01 | `sub(cross_zscore(day_corr(Volume, Ret), 60), cross_zscore(day_ar1_coefficient(Volume), 60))` |
| slot b seed 12 | 过 | 0.10 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.19 | 0.08 | 0.08 | 0.00 | 0.08 | 0.01 | `cross_corr(day_corr(Volume, Ret), day_sum(Ret), 60)` |
| slot b seed 13 | 过 | 0.20 | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_me` | 0.31 | 0.03 | 0.06 | 0.05 | 0.00 | 0.03 | `cross_autocorr(day_corr(Volume, abs(Ret)), 60, 1)` |
| slot b seed 14 | 过 | 0.20 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.19 | 0.02 | 0.08 | 0.22 | 0.03 | 0.01 | `cross_zscore(day_corr(Volume, sub(High, Low)), 60)` |
| R 1 variant 1 | 过 | 0.42 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.30 | 0.18 | 0.27 | 0.32 | 0.20 | 0.07 | `cross_zscore(day_ar1_coefficient(Volume), 250)` |
| R 1 variant 2 | 过 | 0.57 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.43 | 0.19 | 0.37 | 0.44 | 0.22 | 0.06 | `cross_zscore(cross_mean(day_ar1_coefficient(Volume), 10), 120)` |
| R 1 variant 3 | 过 | 0.51 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05` | 0.37 | 0.29 | 0.47 | 0.34 | 0.33 | 0.08 | `sub(cross_mean(day_ar1_coefficient(Volume), 20), cross_mean(day_ar1_coefficient(Volume), 120))` |
| R 1 variant 4 | 过 | 0.70 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.40 | 0.27 | 0.41 | 0.41 | 0.30 | 0.10 | `sub(cross_mean(day_ar1_coefficient(Volume), 5), cross_mean(day_ar1_coefficient(Volume), 250))` |
| R 1 variant 5 | 过 | 0.30 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.20 | 0.04 | 0.12 | 0.32 | 0.06 | 0.04 | `cross_zscore(day_ar1_coefficient(Volume), 60)` |
| R 1 variant 6 | 过 | 0.63 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.42 | 0.39 | 0.53 | 0.33 | 0.43 | 0.11 | `sub(cross_ema(day_ar1_coefficient(Volume), 10), cross_ema(day_ar1_coefficient(Volume), 80))` |
| R 1 variant 7 | 过 | 0.36 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.26 | 0.09 | 0.21 | 0.32 | 0.12 | 0.01 | `cs_bucket_zscore(cross_zscore(day_ar1_coefficient(Volume), 120), LogFloatCap)` |
| R 1 variant 8 | 过 | 0.37 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar` | 0.26 | 0.12 | 0.21 | 0.33 | 0.14 | 0.05 | `cross_zscore(day_ar1_coefficient(Amt), 120)` |
