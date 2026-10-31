# 相关度表:种子 808,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 8 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.31 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` | 0.07 | 0.08 | 0.60 | 0.28 | 0.13 | 0.14 | `day_wstd(Ret, Volume)` |
| slot a seed 1 | 过 | 0.75 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.60 | 0.01 | 0.42 | 0.00 | 0.04 | 0.40 | `ts_max(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_centroid(Volume))), 148)` |
| slot a seed 2 | 过 | 0.52 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.37 | 0.30 | 0.24 | 0.01 | 0.24 | 0.36 | `ts_max(add(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_centroid(Volume))), 148)` |
| slot a seed 3 | 过 | 0.22 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` | 0.12 | 0.23 | 0.54 | 0.00 | 0.25 | 0.02 | `ts_min(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_centroid(Volume))), 148)` |
| slot a seed 4 | 过 | 0.37 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.16 | 0.40 | 0.14 | 0.01 | 0.35 | 0.42 | `ts_max(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(abs_(day_cov(Open, Ret)))), 148)` |
| slot a seed 5 | 过 | 0.59 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.53 | 0.26 | 0.39 | 0.02 | 0.28 | 0.17 | `ts_max(add(cs_rank(day_wstd(Ret, Volume)), cs_rank(abs_(day_cov(Open, Ret)))), 148)` |
| slot a seed 6 | 过 | 0.70 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.64 | 0.30 | 0.19 | 0.03 | 0.25 | 0.38 | `sub(cs_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148)), cs_rank(cross_autocorr_s1(day_wstd(Ret, Volume), 60)))` |
| slot a seed 7 | 过 | 0.72 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.65 | 0.31 | 0.20 | 0.02 | 0.26 | 0.39 | `sub(cs_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148)), cs_rank(cross_autocorr_s1(day_wstd(Ret, Volume), 120)))` |
| slot a seed 8 | 过 | 0.98 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.97 | 0.15 | 0.38 | 0.02 | 0.10 | 0.48 | `cs_bucket_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148), cross_autocorr_s1(day_wstd(Ret, Volume), 60))` |
| slot a seed 9 | 过 | 0.97 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.96 | 0.21 | 0.34 | 0.02 | 0.16 | 0.51 | `cs_bucket_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148), ts_mean(day_centroid(Volume), 148))` |
| slot a seed 10 | 过 | 0.74 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.72 | 0.26 | 0.47 | 0.00 | 0.30 | 0.24 | `sub(cs_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148)), cs_rank(ts_mean(day_centroid(Volume), 148)))` |
| slot a seed 11 | 过 | 0.97 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.96 | 0.15 | 0.37 | 0.01 | 0.09 | 0.46 | `cs_bucket_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148), ts_mean(day_cov(Open, Ret), 148))` |
| slot a seed 12 | 过 | 0.15 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.09 | 0.30 | 0.09 | 0.01 | 0.28 | 0.08 | `cross_autocorr_s1(day_wstd(Ret, Volume), 120)` |
| slot a seed 13 | 过 | 0.30 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.53 | 0.41 | 0.59 | 0.18 | 0.44 | 0.00 | `sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(ts_mean(day_centroid(Volume), 148)))` |
| slot b seed 1 | 过 | 1.00 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 1.00 | 0.27 | 0.05 | 0.03 | 0.24 | 0.26 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Close, High), 241)` |
| slot b seed 2 | 过 | 0.21 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.19 | 0.12 | 0.04 | 0.01 | 0.12 | 0.00 | `cross_regbeta(day_corr(Open, Ret), day_wmean(Vwap, High), 241)` |
| slot b seed 3 | 过 | 0.21 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.19 | 0.12 | 0.04 | 0.01 | 0.12 | 0.00 | `cross_regbeta(day_corr(Open, Ret), day_wmean(Close, High), 241)` |
| slot b seed 4 | 过 | 0.26 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.22 | 0.10 | 0.03 | 0.04 | 0.09 | 0.13 | `cross_regbeta(day_cov(High, Ret), day_wmean(Vwap, High), 241)` |
| slot b seed 5 | 过 | 1.00 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 1.00 | 0.26 | 0.06 | 0.03 | 0.23 | 0.26 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, Volume), 241)` |
| slot b seed 6 | 过 | 1.00 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 1.00 | 0.26 | 0.07 | 0.03 | 0.24 | 0.28 | `cross_regbeta(day_cov(Open, Ret), day_topw_mean(Close, High), 241)` |
| slot b seed 7 | 过 | 0.82 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.78 | 0.26 | 0.03 | 0.04 | 0.23 | 0.24 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 180)` |
| slot b seed 8 | 过 | 0.81 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.76 | 0.27 | 0.08 | 0.02 | 0.24 | 0.28 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 361)` |
| slot b seed 9 | 过 | 0.15 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.08 | 0.28 | 0.28 | 0.36 | 0.28 | 0.16 | `cross_regres(day_cov(Open, Ret), day_wmean(Vwap, High), 241)` |
| slot b seed 10 | 过 | 0.75 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.75 | 0.26 | 0.12 | 0.02 | 0.25 | 0.04 | `cross_reg_tvalue(day_cov(Open, Ret), day_wmean(Vwap, High), 241)` |
| slot b seed 11 | 过 | 1.00 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 1.00 | 0.26 | 0.06 | 0.03 | 0.23 | 0.26 | `cross_regbeta(day_cov(Open, Ret), day_wmean(High, Volume), 241)` |
| slot b seed 12 | 过 | 0.27 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | 0.15 | 0.50 | 0.03 | 0.00 | 0.45 | 0.36 | `cross_regbeta(day_cov(Open, Ret), day_wstd(Ret, Volume), 241)` |
| slot b seed 13 | 过 | 0.61 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.54 | 0.34 | 0.02 | 0.01 | 0.32 | 0.20 | `cross_regbeta(day_wstd(Ret, Volume), day_wmean(Vwap, High), 241)` |
| slot b seed 14 | 过 | 0.28 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.11 | 0.39 | 0.08 | 0.00 | 0.35 | 0.39 | `cross_regalpha(day_cov(Open, Ret), day_wmean(Vwap, High), 241)` |
| R 1 variant 1 | 过 | 0.90 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.86 | 0.13 | 0.40 | 0.01 | 0.07 | 0.46 | `ts_max(cs_demean(cs_winsor(day_wstd(Ret, Volume))), 148)` |
| R 1 variant 2 | 过 | 0.90 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.86 | 0.13 | 0.40 | 0.01 | 0.07 | 0.46 | `ts_max(cs_winsor(cs_demean(day_wstd(Ret, Volume))), 148)` |
| R 1 variant 3 | 过 | 1.00 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 1.00 | 0.15 | 0.39 | 0.02 | 0.09 | 0.48 | `ts_max(cs_bucket_demean(day_wstd(Ret, Volume), cross_valid_count(day_last(Close), 241)), 148)` |
| R 2 variant 1 | 过 | 0.99 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.98 | 0.10 | 0.41 | 0.02 | 0.03 | 0.39 | `ts_max(cs_demean(day_wmean(Ret, Amt)), 99)` |
| R 2 variant 2 | 过 | 0.97 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 0.95 | 0.09 | 0.41 | 0.02 | 0.03 | 0.39 | `ts_max(cs_rank(day_wmean(Ret, Amt)), 99)` |
| R 3 variant 1 | 过 | 0.42 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.39 | 0.14 | 0.07 | 0.01 | 0.13 | 0.20 | `cross_regbeta(day_cov(Open, Ret), cs_demean(day_wmean(Vwap, High)), 241)` |
| R 3 variant 2 | 过 | 0.54 | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241` | 0.50 | 0.26 | 0.01 | 0.00 | 0.24 | 0.14 | `cross_regbeta(cs_demean(day_cov(Open, Ret)), day_wmean(Vwap, High), 241)` |
