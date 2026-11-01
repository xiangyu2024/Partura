# 相关度表:种子 807,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 8 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.17 | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_` | 0.07 | 0.16 | 0.72 | 0.29 | 0.21 | 0.06 | `day_std(Ret)` |
| slot a seed 1 | 过 | 0.27 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.17 | 0.19 | 0.24 | 0.10 | 0.21 | 0.05 | `cross_regbeta(cross_delay(day_mean(Ret), 1), day_std(Ret), 60)` |
| slot a seed 2 | 过 | 0.38 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.32 | 0.17 | 0.22 | 0.05 | 0.19 | 0.08 | `cross_regbeta(cross_delay(day_mean(Ret), 1), day_std(Ret), 120)` |
| slot a seed 3 | 过 | 0.41 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.32 | 0.21 | 0.24 | 0.03 | 0.22 | 0.09 | `cross_regbeta(cross_delay(day_signed_ratio(Ret, Amt), 1), day_std(Ret), 120)` |
| slot a seed 4 | 过 | 0.28 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.11 | 0.24 | 0.87 | 0.03 | 0.30 | 0.13 | `cross_mean(sub(sub(log(day_max(High)), log(day_min(Low))), log(day_std(Ret))), 60)` |
| slot a seed 5 | 过 | 0.29 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.13 | 0.21 | 0.80 | 0.01 | 0.26 | 0.15 | `cross_mean(sub(sub(log(day_max(High)), log(day_min(Low))), log(day_std(Ret))), 120)` |
| slot a seed 6 | 过 | 0.03 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.06 | 0.03 | 0.06 | 0.01 | 0.03 | 0.00 | `cross_regres(log(day_std(Ret)), sub(log(day_max(High)), log(day_min(Low))), 120)` |
| slot a seed 7 | 过 | 0.18 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_` | 0.10 | 0.03 | 0.05 | 0.01 | 0.04 | 0.06 | `cs_last_high05(cross_zscore(ts_var(LogFloatCap, 20), 120), day_std(Ret))` |
| slot a seed 8 | 过 | 0.09 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.10 | 0.10 | 0.28 | 0.15 | 0.12 | 0.02 | `cs_last_low05(cross_zscore(ts_var(LogFloatCap, 20), 120), day_std(Ret))` |
| slot a seed 9 | 过 | 0.17 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_` | 0.10 | 0.00 | 0.07 | 0.06 | 0.01 | 0.06 | `cs_last_high10(cross_zscore(ts_var(LogFloatCap, 20), 120), day_std(Ret))` |
| slot a seed 10 | 过 | 0.14 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.09 | 0.15 | 0.56 | 0.25 | 0.20 | 0.01 | `cs_first_high40(cross_zscore(ts_var(LogFloatCap, 20), 120), day_std(Ret))` |
| slot a seed 11 | 过 | 0.37 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.31 | 0.16 | 0.22 | 0.06 | 0.18 | 0.08 | `cs_bucket_demean(cross_regbeta(cross_delay(day_mean(Ret), 1), day_std(Ret), 120), BoardCode)` |
| slot a seed 12 | 过 | 0.18 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_` | 0.10 | 0.03 | 0.06 | 0.01 | 0.04 | 0.04 | `cs_bucket_demean(cs_last_high05(cross_zscore(ts_var(LogFloatCap, 20), 120), day_std(Ret)), BoardCode)` |
| slot b seed 1 | 废品 | 0.21 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.15 | 0.07 | 0.34 | 0.06 | 0.01 | 0.09 | `cross_mean(day_at_max_ratio(Close), 60)` |
| slot b seed 2 | 过 | 0.27 | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_` | 0.18 | 0.06 | 0.35 | 0.02 | 0.02 | 0.13 | `cross_mean(day_at_max_ratio(Close), 120)` |
| slot b seed 3 | 废品 | 0.17 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.19 | 0.25 | 0.11 | 0.04 | 0.17 | 0.04 | `cross_mean(day_at_min_ratio(Close), 60)` |
| slot b seed 4 | 废品 | 0.19 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.14 | 0.20 | 0.17 | 0.03 | 0.13 | 0.06 | `cross_mean(day_at_min_ratio(Close), 120)` |
| slot b seed 5 | 废品 | 0.27 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.11 | 0.18 | 0.32 | 0.13 | 0.21 | 0.10 | `sub(cross_mean(day_at_max_ratio(Close), 60), cross_mean(day_at_min_ratio(Close), 60))` |
| slot b seed 6 | 过 | 0.20 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.12 | 0.04 | 0.41 | 0.05 | 0.04 | 0.14 | `cs_bucket_demean(cross_mean(day_at_max_ratio(Close), 60), LimitWidth)` |
| slot b seed 7 | 过 | 0.10 | `cross_corr(ts_var(ts_var(LogFloatCap, 20), 20), log(day_sum(` | 0.18 | 0.20 | 0.23 | 0.04 | 0.13 | 0.13 | `cs_bucket_demean(cross_mean(day_at_min_ratio(Close), 60), LimitWidth)` |
| slot b seed 8 | 过 | 0.27 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.26 | 0.62 | 0.05 | 0.00 | 0.55 | 0.18 | `cross_mean(day_flat_ratio(Close), 60)` |
| slot b seed 9 | 过 | 0.25 | `cross_stddev(log(log(log(day_std(Ret)))), 120)` | 0.24 | 0.58 | 0.01 | 0.01 | 0.51 | 0.17 | `cross_mean(day_flat_ratio(Close), 120)` |
| slot b seed 10 | 过 | 0.20 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.14 | 0.02 | 0.33 | 0.06 | 0.06 | 0.09 | `cs_bucket_zscore(cross_mean(day_at_max_ratio(Close), 60), LogFloatCap)` |
| slot b seed 11 | 过 | 0.09 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.06 | 0.01 | 0.08 | 0.08 | 0.04 | 0.02 | `cross_zscore(cross_mean(day_at_max_ratio(Close), 60), 240)` |
| slot b seed 12 | 废品 | 0.20 | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` | 0.15 | 0.08 | 0.33 | 0.06 | 0.00 | 0.07 | `cross_mean(day_at_max_ratio(High), 60)` |
| R 1 variant 1 | 过 | 0.85 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.83 | 0.00 | 0.10 | 0.08 | 0.02 | 0.01 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 120), day_std(Ret))` |
| R 1 variant 2 | 过 | 0.67 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.62 | 0.01 | 0.11 | 0.08 | 0.04 | 0.01 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 60), day_std(Ret))` |
| R 1 variant 3 | 过 | 0.78 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.75 | 0.00 | 0.10 | 0.08 | 0.03 | 0.00 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 90), day_std(Ret))` |
| R 1 variant 4 | 过 | 0.84 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.82 | 0.01 | 0.10 | 0.08 | 0.02 | 0.00 | `cs_last_high05(cross_zscore(pow_2_5(LogFloatShares), 120), day_std(Ret))` |
| R 1 variant 5 | 过 | 0.84 | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares))` | 0.81 | 0.00 | 0.10 | 0.08 | 0.03 | 0.00 | `cs_last_high05(cross_zscore(LogFloatShares, 120), day_std(Ret))` |
| R 2 variant 1 | 过 | 0.32 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_` | 0.21 | 0.04 | 0.11 | 0.07 | 0.06 | 0.01 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 120), 120), 120), day_std(Ret))` |
| R 2 variant 2 | 过 | 0.79 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_` | 0.76 | 0.02 | 0.09 | 0.08 | 0.04 | 0.01 | `cs_last_high05(cross_zscore(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241), 241), day_std(Ret))` |
| R 2 variant 3 | 过 | 0.63 | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_` | 0.58 | 0.03 | 0.10 | 0.08 | 0.05 | 0.01 | `cs_last_high05(cross_zscore(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 120), 120), day_std(Ret))` |
