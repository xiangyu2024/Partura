# 相关度表:种子 2063,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.33 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.14 | 0.21 | 0.77 | 0.32 | 0.26 | 0.02 | `day_var(Ret)` |
| slot a seed 1 | 过 | 0.26 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.24 | 0.07 | 0.12 | 0.04 | 0.09 | 0.34 | `div(ts_std(day_var(Ret), 60), ts_mean(day_var(Ret), 60))` |
| slot a seed 2 | 过 | 0.24 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.29 | 0.04 | 0.23 | 0.46 | 0.07 | 0.13 | `sub(ts_mean(day_var(Ret), 10), ts_mean(day_var(Ret), 120))` |
| slot a seed 3 | 过 | 0.20 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.23 | 0.00 | 0.07 | 0.04 | 0.02 | 0.32 | `div(ts_max(day_var(Ret), 60), ts_mean(day_var(Ret), 60))` |
| slot a seed 4 | 过 | 0.37 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.31 | 0.21 | 0.56 | 0.04 | 0.25 | 0.30 | `ts_skew(day_var(Ret), 60)` |
| slot a seed 5 | 废品 | 0.16 | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60` | 0.16 | 0.15 | 0.32 | inf | 0.21 | 0.10 | `ts_kurt(day_var(Ret), 120)` |
| slot a seed 6 | 过 | 0.21 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.12 | 0.14 | 0.17 | 0.11 | 0.15 | 0.06 | `cross_corr(day_var(Ret), day_sum(Ret), 60)` |
| slot a seed 7 | 过 | 0.31 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.15 | 0.26 | 0.18 | 0.09 | 0.28 | 0.05 | `cross_corr(day_var(Ret), day_sum(Volume), 60)` |
| slot a seed 8 | 过 | 0.27 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.12 | 0.24 | 0.27 | 0.01 | 0.24 | 0.02 | `cross_corr(day_var(Ret), cross_delay(day_var(Ret), 5), 60)` |
| slot a seed 9 | 过 | 0.23 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.21 | 0.03 | 0.35 | 0.47 | 0.07 | 0.00 | `cross_mean(cross_zscore(day_var(Ret), 120), 10)` |
| slot a seed 10 | 过 | 0.28 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.28 | 0.07 | 0.28 | 0.46 | 0.11 | 0.16 | `sub(cross_ema(day_var(Ret), 5), cross_ema(day_var(Ret), 60))` |
| slot a seed 11 | 过 | 0.44 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.25 | 0.37 | 0.10 | 0.06 | 0.39 | 0.09 | `cs_bucket_demean(div(ts_std(day_var(Ret), 60), ts_mean(day_var(Ret), 60)), LogFloatCap)` |
| slot a seed 12 | 过 | 0.17 | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(A` | 0.13 | 0.09 | 0.15 | 0.05 | 0.09 | 0.09 | `cs_bucket_zscore(cross_corr(day_var(Ret), day_sum(Ret), 120), sub(LogFloatCap, LogFloatShares))` |
| slot b core | 废品 | 0.06 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.14 | 0.04 | 0.03 | 0.02 | 0.03 | 0.01 | `ts_delta(LogFloatShares, 50)` |
| slot b seed 1 | 废品 | 0.21 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.15 | 0.12 | 0.02 | 0.01 | 0.13 | 0.26 | `cs_bucket_demean(ts_delta(LogFloatShares, 50), ListAge)` |
| slot b seed 2 | 过 | 0.18 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.23 | 0.01 | 0.04 | 0.03 | 0.01 | 0.07 | `sub(ts_delta(LogFloatShares, 50), ts_delta(LogFloatShares, 250))` |
| slot b seed 3 | 废品 | 0.15 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.20 | 0.03 | 0.05 | 0.03 | 0.01 | 0.04 | `ts_max(ts_delta(LogFloatShares, 50), 120)` |
| slot b seed 4 | 废品 | 0.23 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.47 | 0.15 | 0.01 | 0.02 | 0.12 | 0.05 | `cs_bucket_zscore(ts_delta(LogFloatShares, 50), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 5 | 废品 | 0.24 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.19 | 0.14 | 0.03 | 0.01 | 0.15 | 0.24 | `cs_bucket_demean(ts_delta(LogFloatShares, 50), BoardCode)` |
| slot b seed 6 | 废品 | 0.07 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.02 | 0.09 | 0.12 | 0.10 | 0.10 | 0.03 | `mul(ts_delta(LogFloatShares, 50), sign(cross_mean(day_sum(Ret), 60)))` |
| slot b seed 7 | 废品 | 0.07 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.14 | 0.04 | 0.03 | 0.02 | 0.03 | 0.01 | `div(ts_delta(LogFloatShares, 50), cross_mean(day_std(Ret), 20))` |
| slot b seed 8 | 过 | 0.01 | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60` | 0.01 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | `cross_corr(ts_delta(LogFloatShares, 50), day_sum(Ret), 120)` |
| slot b seed 9 | 过 | 0.09 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.11 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | `sub(ts_delta(LogFloatShares, 50), cross_mean(ts_delta(LogFloatShares, 50), 250))` |
| slot b seed 10 | 过 | 0.17 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.20 | 0.01 | 0.05 | 0.03 | 0.00 | 0.04 | `cross_ema(ts_delta(LogFloatShares, 50), 20)` |
| slot b seed 11 | 废品 | 0.13 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)),` | 0.04 | 0.12 | 0.00 | 0.01 | 0.12 | 0.21 | `cs_bucket_zscore(ts_max(ts_delta(LogFloatShares, 50), 120), ListAge)` |
| slot b seed 12 | 过 | 0.29 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.15 | 0.23 | 0.30 | 0.29 | 0.26 | 0.06 | `sub(ts_delta(LogFloatShares, 50), cross_mean(day_sum(Ret), 50))` |
