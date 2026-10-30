# 相关度表:种子 808,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 4 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.03 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.03 | 0.02 | 0.03 | 0.14 | 0.02 | 0.02 | `day_wmean(Ret, Volume)` |
| slot a seed 1 | 过 | 0.51 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.58 | 0.05 | 0.05 | 0.05 | 0.06 | 0.03 | `add(cs_rank(ts_max(day_wmean(Ret, Volume), 99)), cs_rank(ts_min(day_wmean(Ret, Volume), 99)))` |
| slot a seed 2 | 过 | 0.20 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.21 | 0.23 | 0.10 | 0.09 | 0.25 | 0.13 | `add(cs_rank(ts_quantile(day_wmean(Ret, Volume), 0.95, 148)), cs_rank(ts_quantile(day_wmean(Ret, Volume), 0.05, 148)))` |
| slot a seed 3 | 过 | 0.34 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.38 | 0.25 | 0.14 | 0.12 | 0.27 | 0.11 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_wmean(Ret, Volume), 120)))` |
| slot a seed 4 | 过 | 0.81 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.80 | 0.07 | 0.27 | 0.01 | 0.02 | 0.30 | `ts_skew(day_wmean(Ret, Volume), 120)` |
| slot a seed 5 | 过 | 0.61 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.63 | 0.14 | 0.26 | 0.07 | 0.18 | 0.00 | `cs_bucket_rank(ts_skew(day_wmean(Ret, Volume), 60), LogFloatCap)` |
| slot a seed 6 | 过 | 0.72 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.83 | 0.20 | 0.10 | 0.02 | 0.16 | 0.21 | `cs_bucket_rank(ts_max(day_wmean(Ret, Volume), 99), ts_mean(day_wstd(Ret, Volume), 99))` |
| slot a seed 7 | 过 | 0.31 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.37 | 0.01 | 0.04 | 0.03 | 0.02 | 0.09 | `sub(cs_rank(ts_max(day_wmean(Ret, Volume), 99)), cs_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 99)))` |
| slot a seed 8 | 过 | 0.32 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.15 | 0.07 | 0.31 | 0.01 | 0.03 | 0.18 | `ts_max(sub(cs_rank(day_wmean(Ret, Volume)), cs_rank(day_mean(Ret))), 99)` |
| slot a seed 9 | 过 | 0.03 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.06 | 0.22 | 0.07 | 0.03 | 0.23 | 0.15 | `ts_mean(sub(cs_rank(day_wmean(Ret, Volume)), cs_rank(day_mean(Ret))), 60)` |
| slot a seed 10 | 废品 | 0.19 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)` | 0.17 | 0.04 | 0.12 | 0.13 | 0.07 | 0.03 | `ts_argmax(day_wmean(Ret, Volume), 120)` |
| slot a seed 11 | 过 | 0.76 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.64 | 0.06 | 0.35 | 0.09 | 0.01 | 0.26 | `sub(cs_rank(ts_max(day_wmean(Ret, Volume), 120)), cs_rank(ts_argmax(day_wmean(Ret, Volume), 120)))` |
| slot a seed 12 | 过 | 0.54 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.32 | 0.14 | 0.35 | 0.03 | 0.09 | 0.36 | `ts_min(day_wmean(Ret, Volume), 99)` |
| slot a seed 13 | 过 | 0.60 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.33 | 0.22 | 0.45 | 0.07 | 0.17 | 0.50 | `cross_tail_mean_q25(day_wmean(Ret, Volume), 120)` |
| slot b seed 1 | 过 | 0.08 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.15 | 0.37 | 0.46 | 0.01 | 0.37 | 0.29 | `ts_mean(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret))), 60)` |
| slot b seed 2 | 过 | 0.09 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.16 | 0.37 | 0.42 | 0.00 | 0.37 | 0.29 | `ts_mean(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret))), 120)` |
| slot b seed 3 | 过 | 0.07 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.08 | 0.33 | 0.32 | 0.01 | 0.31 | 0.18 | `ts_max(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret))), 120)` |
| slot b seed 4 | 过 | 0.07 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.14 | 0.48 | 0.42 | 0.00 | 0.47 | 0.29 | `cross_tail_mean_q75(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret))), 120)` |
| slot b seed 5 | 过 | 0.57 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.43 | 0.30 | 0.04 | 0.01 | 0.25 | 0.49 | `cs_bucket_rank(ts_mean(day_wstd(Ret, Volume), 120), ts_mean(day_std(Ret), 120))` |
| slot b seed 6 | 过 | 0.22 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)` | 0.23 | 0.43 | 0.12 | 0.01 | 0.41 | 0.00 | `ts_mean(day_corr(abs_(Ret), Volume), 60)` |
| slot b seed 7 | 过 | 0.19 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.21 | 0.39 | 0.05 | 0.01 | 0.37 | 0.01 | `ts_mean(day_corr(abs_(Ret), Volume), 120)` |
| slot b seed 8 | 过 | 0.20 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.20 | 0.42 | 0.10 | 0.02 | 0.40 | 0.01 | `cross_ema(day_corr(abs_(Ret), Volume), 40)` |
| slot b seed 9 | 过 | 0.07 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.10 | 0.34 | 0.03 | 0.00 | 0.29 | 0.01 | `cross_tail_mean_q25(day_corr(abs_(Ret), Volume), 120)` |
| slot b seed 10 | 过 | 0.17 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.18 | 0.28 | 0.31 | 0.01 | 0.27 | 0.33 | `ts_mean(sub(cs_rank(day_topw_mean(abs_(Ret), Volume)), cs_rank(day_mean(abs_(Ret)))), 120)` |
| slot b seed 11 | 过 | 0.29 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.28 | 0.57 | 0.22 | 0.01 | 0.55 | 0.03 | `ts_mean(day_corr(abs_(Ret), in_delay(Volume, 1)), 60)` |
| slot b seed 12 | 过 | 0.29 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.24 | 0.01 | 0.00 | 0.02 | 0.01 | 0.28 | `cs_bucket_rank(ts_mean(day_corr(abs_(Ret), Volume), 60), cross_mean(day_sum(Amt), 30))` |
| R 1 variant 1 | 过 | 0.91 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.85 | 0.11 | 0.42 | 0.01 | 0.05 | 0.46 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` |
| R 2 variant 1 | 过 | 0.95 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.92 | 0.09 | 0.41 | 0.01 | 0.04 | 0.44 | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)` |
| R 2 variant 2 | 过 | 0.89 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.82 | 0.14 | 0.37 | 0.02 | 0.09 | 0.47 | `ts_max(day_wstd(Ret, Ret), 148)` |
| R 2 variant 3 | 过 | 0.99 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | 0.99 | 0.09 | 0.43 | 0.01 | 0.03 | 0.45 | `ts_max(cs_rank(day_wstd(Ret, Ret)), 99)` |
| R 3 variant 1 | 过 | 1.00 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 1.00 | 0.10 | 0.41 | 0.02 | 0.03 | 0.39 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` |
| R 3 variant 2 | 过 | 0.50 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.39 | 0.32 | 0.48 | 0.04 | 0.34 | 0.16 | `ts_max(day_mean(Ret), 99)` |
| R 3 variant 3 | 过 | 0.56 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | 0.46 | 0.28 | 0.46 | 0.03 | 0.30 | 0.16 | `ts_max(day_topw_mean(Ret, Volume), 99)` |
| R 4 variant 1 | 过 | 0.69 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.52 | 0.07 | 0.71 | 0.01 | 0.13 | 0.38 | `ts_mean(cs_demean(day_wstd(Ret, Volume)), 148)` |
| R 4 variant 2 | 过 | 0.81 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.69 | 0.01 | 0.61 | 0.01 | 0.07 | 0.47 | `cross_tail_mean_q75(cs_demean(day_wstd(Ret, Volume)), 148)` |
| R 4 variant 3 | 过 | 0.82 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.72 | 0.05 | 0.51 | 0.02 | 0.10 | 0.41 | `ts_max(cs_demean(day_std(Ret)), 148)` |
| R 4 variant 4 | 过 | 0.98 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.96 | 0.15 | 0.40 | 0.02 | 0.09 | 0.49 | `ts_max(cs_rank(day_wstd(Ret, Volume)), 148)` |
| R 4 variant 5 | 过 | 1.00 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 1.00 | 0.15 | 0.39 | 0.02 | 0.09 | 0.48 | `ts_max(cs_bucket_demean(day_wstd(Ret, Volume), LimitWidth), 148)` |
| R 4 variant 6 | 过 | 0.96 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.95 | 0.16 | 0.36 | 0.01 | 0.10 | 0.41 | `cs_bucket_rank(ts_max(cs_demean(day_wstd(Ret, Volume)), 148), ListAge)` |
| R 4 variant 7 | 废品 | 0.29 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)` | 0.32 | 0.03 | 0.12 | 0.08 | 0.06 | 0.06 | `ts_argmax(cs_demean(day_wstd(Ret, Volume)), 148)` |
| R 4 variant 8 | 过 | 0.68 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), ` | 0.47 | 0.06 | 0.64 | 0.01 | 0.12 | 0.41 | `ts_quantile(cs_demean(day_wstd(Ret, Volume)), 0.9, 148)` |
