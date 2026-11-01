# 相关度表:种子 808,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 10 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.70 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.75 | 0.48 | 0.42 | 0.20 | 0.51 | 0.13 | `ts_mean(day_centroid(Volume), 20)` |
| slot a seed 1 | 过 | 0.67 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.70 | 0.46 | 0.41 | 0.20 | 0.48 | 0.10 | `cs_bucket_rank(ts_mean(day_centroid(Volume), 20), LogFloatShares)` |
| slot a seed 2 | 过 | 0.25 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.23 | 0.09 | 0.11 | 0.22 | 0.05 | 0.00 | `sub(cs_rank(ts_mean(day_centroid(Volume), 20)), cs_rank(ts_mean(day_centroid(Amt), 120)))` |
| slot a seed 3 | 过 | 0.38 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.19 | 0.02 | 0.28 | 0.00 | 0.04 | 0.23 | `ts_std(ts_mean(day_centroid(Volume), 20), 60)` |
| slot a seed 4 | 过 | 0.20 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.10 | 0.06 | 0.16 | 0.00 | 0.08 | 0.07 | `cross_autocorr_s1(ts_mean(day_centroid(Volume), 20), 60)` |
| slot a seed 5 | 过 | 0.40 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.20 | 0.08 | 0.21 | 0.25 | 0.11 | 0.05 | `sub(ts_mean(day_centroid(Volume), 20), ts_mean(day_centroid(Volume), 120))` |
| slot a seed 6 | 过 | 0.15 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.14 | 0.17 | 0.01 | 0.00 | 0.14 | 0.15 | `cross_regbeta(day_cov(Open, Ret), ts_mean(day_centroid(Volume), 20), 241)` |
| slot a seed 7 | 过 | 0.48 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.54 | 0.44 | 0.37 | 0.02 | 0.46 | 0.01 | `cross_tail_mean_q25(ts_mean(day_centroid(Volume), 20), 120)` |
| slot a seed 8 | 过 | 0.67 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.75 | 0.36 | 0.35 | 0.15 | 0.40 | 0.10 | `cs_bucket_demean(ts_mean(day_centroid(Volume), 20), day_distinct_ratio(Ret))` |
| slot a seed 9 | 过 | 0.05 | `cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 30)` | 0.10 | 0.01 | 0.04 | 0.01 | 0.01 | 0.01 | `ts_corr(ts_mean(day_centroid(Volume), 20), day_wmean(Ret, Volume), 60)` |
| slot a seed 10 | 过 | 0.18 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.18 | 0.11 | 0.05 | 0.02 | 0.09 | 0.03 | `cs_last_high10(day_zero_ratio(Open), ts_mean(day_centroid(Volume), 20))` |
| slot a seed 11 | 过 | 0.35 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.30 | 0.21 | 0.23 | 0.02 | 0.21 | 0.12 | `ts_regbeta(ts_mean(day_centroid(Volume), 20), ts_mean(day_wstd(Ret, Volume), 20), 120)` |
| slot a seed 12 | 废品 | 0.38 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.20 | 0.06 | 0.20 | 0.25 | 0.09 | 0.05 | `ts_rank(ts_mean(day_centroid(Volume), 20), 120)` |
| slot b seed 1 | 过 | 0.36 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.11 | 0.80 | 0.09 | 0.03 | 0.71 | 0.53 | `ts_mean(day_gini(Volume), 60)` |
| slot b seed 2 | 过 | 0.48 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.29 | 0.48 | 0.23 | 0.02 | 0.37 | 0.37 | `ts_mean(day_es_ratio_hi(Volume), 99)` |
| slot b seed 3 | 过 | 0.22 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.11 | 0.54 | 0.02 | 0.09 | 0.45 | 0.01 | `cs_bucket_rank(ts_mean(day_gini(Volume), 60), LogFloatCap)` |
| slot b seed 4 | 过 | 0.08 | `cross_sum(cross_autocorr_s1(ts_max(cs_last_high05(day_distin` | 0.09 | 0.08 | 0.21 | 0.06 | 0.09 | 0.02 | `sub(cs_rank(ts_mean(day_gini(Volume), 60)), cs_rank(ts_mean(day_gini(Amt), 20)))` |
| slot b seed 5 | 过 | 0.43 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.25 | 0.03 | 0.30 | 0.01 | 0.02 | 0.21 | `ts_std(day_gini(Volume), 120)` |
| slot b seed 6 | 过 | 0.48 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.42 | 0.20 | 0.26 | 0.04 | 0.25 | 0.04 | `ts_corr(day_gini(Volume), day_wmean(Ret, Volume), 60)` |
| slot b seed 7 | 过 | 0.51 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.49 | 0.01 | 0.15 | 0.00 | 0.03 | 0.18 | `ts_regbeta(day_es_ratio_hi(Volume), day_wmean(Ret, Volume), 120)` |
| slot b seed 8 | 过 | 0.24 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` | 0.09 | 0.31 | 0.07 | 0.00 | 0.27 | 0.31 | `cross_autocorr_s1(day_gini(Volume), 60)` |
| slot b seed 9 | 废品 | 0.13 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(` | 0.15 | 0.15 | 0.04 | 0.01 | 0.16 | 0.18 | `ts_max(day_at_max_ratio(Volume), 99)` |
| slot b seed 10 | 过 | 0.54 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.34 | 0.39 | 0.26 | 0.01 | 0.29 | 0.39 | `cross_tail_mean_q75(day_es_ratio_hi(Volume), 120)` |
| slot b seed 11 | 过 | 0.32 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.25 | 0.71 | 0.17 | 0.05 | 0.62 | 0.51 | `cs_bucket_demean(ts_mean(day_gini(Volume), 60), ts_mean(day_centroid(Volume), 20))` |
| slot b seed 12 | 过 | 0.41 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.40 | 0.18 | 0.14 | 0.02 | 0.20 | 0.16 | `cross_regbeta(day_gini(Volume), day_wstd(Ret, Volume), 241)` |
