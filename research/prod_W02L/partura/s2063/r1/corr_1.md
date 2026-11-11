# 相关度表:种子 2063,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.22 | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, L` | 0.32 | 0.20 | 0.10 | 0.07 | 0.20 | 0.10 | `day_cov(Ret, Low)` |
| slot a seed 1 | 过 | 0.39 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.40 | 0.60 | 0.42 | 0.18 | 0.59 | 0.27 | `cross_mean(day_cov(Ret, Low), 20)` |
| slot a seed 2 | 过 | 0.32 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.26 | 0.47 | 0.55 | 0.26 | 0.48 | 0.05 | `cross_mean(div(day_cov(Ret, Low), day_mean(Low)), 20)` |
| slot a seed 3 | 过 | 0.27 | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, L` | 0.10 | 0.01 | 0.05 | 0.10 | 0.00 | 0.03 | `cross_zscore(div(day_cov(Ret, Low), day_mean(Low)), 120)` |
| slot a seed 4 | 过 | 0.49 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.26 | 0.50 | 0.48 | 0.19 | 0.53 | 0.30 | `cs_bucket_zscore(cross_mean(day_cov(Ret, Low), 20), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 5 | 过 | 0.35 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.25 | 0.50 | 0.53 | 0.25 | 0.51 | 0.09 | `cs_bucket_demean(cross_mean(div(day_cov(Ret, Low), day_mean(Low)), 20), LogFloatCap)` |
| slot a seed 6 | 过 | 0.20 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.14 | 0.11 | 0.24 | 0.36 | 0.14 | 0.07 | `sub(cross_mean(div(day_cov(Ret, Low), day_mean(Low)), 20), cross_mean(div(day_cov(Ret, Low), day_mean(Low)), 120))` |
| slot a seed 7 | 过 | 0.39 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.40 | 0.61 | 0.31 | 0.14 | 0.59 | 0.33 | `cross_mean(div(day_cov(Ret, Low), day_std(Ret)), 20)` |
| slot a seed 8 | 过 | 0.32 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.25 | 0.46 | 0.41 | 0.34 | 0.47 | 0.15 | `cross_mean(sub(day_cov(Ret, Low), day_cov(Ret, High)), 20)` |
| slot a seed 9 | 过 | 0.18 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.05 | 0.17 | 0.29 | 0.18 | 0.20 | 0.03 | `cross_corr(div(day_cov(Ret, Low), day_mean(Low)), day_sum(Ret), 60)` |
| slot a seed 10 | 过 | 0.04 | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, L` | 0.01 | 0.04 | 0.06 | 0.15 | 0.04 | 0.01 | `mul(cross_zscore(div(day_cov(Ret, Low), day_mean(Low)), 60), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 11 | 过 | 0.34 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.26 | 0.48 | 0.55 | 0.26 | 0.50 | 0.07 | `cross_mean(cs_robust_z(div(day_cov(Ret, Low), day_mean(Low))), 20)` |
| slot b seed 1 | 过 | 0.41 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.09 | 0.44 | 0.50 | 0.19 | 0.49 | 0.04 | `cross_mean(day_centroid(Volume), 20)` |
| slot b seed 2 | 过 | 0.42 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.54 | 0.07 | 0.27 | 0.13 | 0.12 | 0.07 | `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)` |
| slot b seed 3 | 过 | 0.23 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.16 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Amt), 120)` |
| slot b seed 4 | 过 | 0.61 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.23 | 0.71 | 0.00 | 0.04 | 0.64 | 0.56 | `cross_mean(day_gini(Ret), 20)` |
| slot b seed 5 | 过 | 0.50 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.15 | 0.68 | 0.01 | 0.06 | 0.62 | 0.47 | `cross_mean(sub(day_gini(Ret), day_gini(Volume)), 20)` |
| slot b seed 6 | 过 | 0.53 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.08 | 0.69 | 0.39 | 0.12 | 0.69 | 0.27 | `cross_mean(day_corr(in_index(Volume), Volume), 20)` |
| slot b seed 7 | 过 | 0.32 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.43 | 0.58 | 0.23 | 0.05 | 0.55 | 0.19 | `cross_mean(day_corr(in_index(Ret), abs_(Ret)), 20)` |
| slot b seed 8 | 过 | 0.42 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.14 | 0.43 | 0.48 | 0.19 | 0.47 | 0.03 | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 9 | 过 | 0.09 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.08 | 0.04 | 0.04 | 0.13 | 0.03 | 0.01 | `cross_zscore(cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 10), 120)` |
| slot b seed 10 | 过 | 0.33 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.17 | 0.52 | 0.07 | 0.11 | 0.45 | 0.01 | `cs_bucket_demean(cross_mean(day_gini(Volume), 20), LogFloatCap)` |
| slot b seed 11 | 过 | 0.09 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.07 | 0.12 | 0.17 | 0.00 | 0.14 | 0.10 | `cross_corr(day_centroid(Volume), day_sum(Ret), 60)` |
| R 1 variant 1 | 过 | 0.15 | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, L` | 0.17 | 0.02 | 0.03 | 0.04 | 0.01 | 0.03 | `add(day_min(in_min_rolling(Amt, 5)), day_cov(Ret, High))` |
| R 1 variant 2 | 过 | 0.23 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.44 | 0.10 | 0.04 | 0.02 | 0.11 | 0.09 | `add(cs_rank(day_min(in_min_rolling(Amt, 5))), cs_rank(day_cov(Ret, High)))` |
| R 1 variant 3 | 过 | 0.31 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.34 | 0.33 | 0.11 | 0.00 | 0.33 | 0.20 | `add(cs_rank(cross_mean(day_min(Amt), 20)), cs_rank(cross_mean(div(day_cov(Ret, High), day_mean(High)), 20)))` |
| R 1 variant 4 | 过 | 0.19 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.24 | 0.33 | 0.20 | 0.01 | 0.31 | 0.17 | `cross_mean(div(day_cov(Ret, High), day_mean(High)), 20)` |
| R 1 variant 5 | 过 | 0.38 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.42 | 0.20 | 0.11 | 0.00 | 0.21 | 0.25 | `cs_bucket_demean(cross_mean(day_cov(Ret, High), 20), sub(LogFloatCap, LogFloatShares))` |
| R 1 variant 6 | 过 | 0.15 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.20 | 0.17 | 0.11 | 0.16 | 0.17 | 0.08 | `sub(day_cov(Ret, High), day_cov(Ret, Low))` |
