# 相关度表:种子 2034,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.16 | `ts_decay_linear(day_sum(Volume), 5)` | 0.10 | 0.15 | 0.31 | 0.15 | 0.20 | 0.08 | `sub(log(ts_max(day_sum(Amt), 50)), log(cross_mean(day_sum(Amt), 120)))` |
| slot a seed 2 | 过 | 0.23 | `ts_decay_linear(day_sum(Volume), 5)` | 0.31 | 0.22 | 0.44 | 0.28 | 0.28 | 0.05 | `div(ts_max(day_sum(Amt), 25), cross_med(day_sum(Amt), 120))` |
| slot a seed 3 | 过 | 0.25 | `ts_decay_linear(day_sum(Volume), 5)` | 0.44 | 0.24 | 0.37 | 0.30 | 0.29 | 0.11 | `ts_max(cross_zscore(log(day_sum(Amt)), 120), 25)` |
| slot a seed 4 | 过 | 0.29 | `ts_decay_linear(day_sum(Volume), 5)` | 0.40 | 0.30 | 0.50 | 0.35 | 0.34 | 0.07 | `cross_mean(cross_zscore(log(day_sum(Amt)), 120), 20)` |
| slot a seed 5 | 过 | 0.28 | `ts_decay_linear(day_sum(Volume), 5)` | 0.43 | 0.33 | 0.48 | 0.25 | 0.38 | 0.08 | `cross_tail_mean_q75(div(day_sum(Amt), cross_mean(day_sum(Amt), 120)), 30)` |
| slot a seed 6 | 过 | 0.35 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.16 | 0.34 | 0.36 | 0.14 | 0.39 | 0.02 | `cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120))` |
| slot a seed 7 | 过 | 0.26 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.53 | 0.04 | 0.03 | 0.02 | 0.06 | 0.05 | `cs_bucket_zscore(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 30))` |
| slot a seed 8 | 过 | 0.27 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.26 | 0.21 | 0.27 | 0.10 | 0.24 | 0.01 | `cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), LogFloatCap)` |
| slot a seed 9 | 过 | 0.09 | `ts_decay_linear(day_sum(Volume), 5)` | 0.08 | 0.12 | 0.17 | 0.29 | 0.13 | 0.06 | `cross_mean(mul(cross_zscore(log(day_sum(Amt)), 120), sign(day_sum(Ret))), 20)` |
| slot a seed 10 | 过 | 0.14 | `ts_decay_linear(day_sum(Volume), 5)` | 0.09 | 0.18 | 0.31 | 0.45 | 0.19 | 0.01 | `cross_sum(mul(cross_zscore(log(day_sum(Amt)), 120), day_sum(Ret)), 20)` |
| slot a seed 11 | 过 | 0.33 | `ts_decay_linear(day_sum(Volume), 5)` | 0.51 | 0.27 | 0.44 | 0.49 | 0.31 | 0.14 | `div(cross_mean(day_sum(Amt), 10), cross_mean(day_sum(Amt), 120))` |
| slot a seed 12 | 过 | 0.26 | `ts_decay_linear(day_sum(Volume), 5)` | 0.28 | 0.34 | 0.45 | 0.17 | 0.37 | 0.10 | `cross_quantile_q75(cross_zscore(log(day_sum(Amt)), 120), 40)` |
| slot a seed 13 | 过 | 0.33 | `ts_decay_linear(day_sum(Volume), 5)` | 0.40 | 0.35 | 0.49 | 0.33 | 0.38 | 0.14 | `cross_ema(div(day_sum(Amt), cross_mean(day_sum(Amt), 120)), 10)` |
| slot a seed 14 | 过 | 0.33 | `ts_decay_linear(day_sum(Volume), 5)` | 0.37 | 0.25 | 0.46 | 0.45 | 0.28 | 0.05 | `cross_zscore(cross_ema(log(day_sum(Amt)), 5), 120)` |
| slot a seed 15 | 过 | 0.28 | `ts_decay_linear(day_sum(Volume), 5)` | 0.42 | 0.28 | 0.45 | 0.30 | 0.33 | 0.07 | `cs_bucket_demean(cross_zscore(cross_max(log(day_sum(Amt)), 25), 120), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 16 | 过 | 0.19 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.17 | 0.23 | 0.20 | 0.10 | 0.21 | 0.08 | `ts_skew(log(day_sum(Amt)), 60)` |
| slot b seed 1 | 过 | 0.09 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.05 | 0.09 | 0.06 | 0.01 | 0.08 | 0.05 | `cross_corr(cross_delay(mul(day_sum(Ret), cross_zscore(log(day_sum(Amt)), 60)), 1), day_sum(Ret), 120)` |
| slot b seed 2 | 过 | 0.09 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.05 | 0.10 | 0.07 | 0.00 | 0.09 | 0.05 | `cross_regbeta(cross_delay(mul(day_sum(Ret), cross_zscore(log(day_sum(Amt)), 60)), 1), day_sum(Ret), 120)` |
| slot b seed 3 | 过 | 0.11 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.07 | 0.09 | 0.01 | 0.04 | 0.10 | 0.11 | `cross_corr(cross_zscore(log(day_sum(Amt)), 60), abs_(day_sum(Ret)), 60)` |
| slot b seed 4 | 过 | 0.40 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.17 | 0.37 | 0.09 | 0.01 | 0.35 | 0.01 | `cross_regbeta(log(day_sum(Amt)), log(day_std(Ret)), 60)` |
| slot b seed 5 | 过 | 0.28 | `ts_decay_linear(day_sum(Volume), 5)` | 0.44 | 0.21 | 0.33 | 0.41 | 0.24 | 0.07 | `cross_mean(cross_regres(log(day_std(Ret)), log(day_sum(Amt)), 60), 10)` |
| slot b seed 6 | 过 | 0.09 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.15 | 0.17 | 0.10 | 0.05 | 0.17 | 0.05 | `cross_mean(cross_regres(log(day_sum(Amt)), log(day_std(Ret)), 60), 10)` |
| slot b seed 7 | 过 | 0.08 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.06 | 0.03 | 0.04 | 0.23 | 0.03 | 0.01 | `cross_mean(mul(cross_regres(log(day_std(Ret)), log(day_sum(Amt)), 60), sign(day_sum(Ret))), 20)` |
| slot b seed 8 | 过 | 0.23 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.15 | 0.29 | 0.12 | 0.06 | 0.25 | 0.31 | `cross_stddev(cross_regres(log(day_std(Ret)), log(day_sum(Amt)), 60), 60)` |
| slot b seed 9 | 过 | 0.09 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.35 | 0.07 | 0.85 | 0.03 | 0.12 | 0.24 | `cs_regres(cross_mean(sub(log(day_std(Ret)), log(day_sum(Amt))), 60), cross_mean(log(day_sum(Amt)), 60))` |
| slot b seed 10 | 过 | 0.41 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.17 | 0.38 | 0.09 | 0.01 | 0.37 | 0.03 | `cs_bucket_zscore(cross_regbeta(log(day_sum(Amt)), log(day_std(Ret)), 60), LogFloatCap)` |
| slot b seed 11 | 过 | 0.11 | `ts_decay_linear(day_sum(Volume), 5)` | 0.13 | 0.18 | 0.23 | 0.20 | 0.18 | 0.05 | `cross_corr(log(day_sum(Amt)), day_sum(Ret), 60)` |
| slot b seed 12 | 过 | 0.23 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.20 | 0.14 | 0.17 | 0.03 | 0.14 | 0.03 | `cross_corr(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 120)` |
| slot b seed 13 | 过 | 0.27 | `ts_decay_linear(day_sum(Volume), 5)` | 0.23 | 0.37 | 0.37 | 0.12 | 0.39 | 0.10 | `cross_mean(cross_regres(log(day_std(Ret)), log(day_sum(Amt)), 120), 30)` |
| slot b seed 14 | 过 | 0.23 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.50 | 0.01 | 0.28 | 0.29 | 0.03 | 0.10 | `cs_bucket_demean(cross_mean(cross_regres(log(day_std(Ret)), log(day_sum(Amt)), 60), 20), cross_mean(day_sum(Amt), 30))` |
| slot b seed 15 | 过 | 0.10 | `ts_decay_linear(day_sum(Volume), 5)` | 0.10 | 0.06 | 0.32 | 0.13 | 0.09 | 0.20 | `cross_regbeta(cross_zscore(log(day_sum(Amt)), 60), day_wmean(Ret, Amt), 60)` |
| slot b seed 16 | 过 | 0.23 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.19 | 0.14 | 0.17 | 0.02 | 0.14 | 0.03 | `cross_regbeta(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 120)` |
| R 1 variant 1 | 过 | 0.19 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.28 | 0.10 | 0.26 | 0.06 | 0.14 | 0.12 | `div(ts_decay_linear(ts_max(day_sum(Amt), 50), 25), cross_mean(day_sum(Amt), 120))` |
| R 1 variant 2 | 过 | 0.20 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.25 | 0.14 | 0.29 | 0.08 | 0.18 | 0.08 | `ts_decay_linear(sub(log(ts_max(day_sum(Amt), 50)), log(cross_mean(day_sum(Amt), 120))), 25)` |
| R 1 variant 3 | 过 | 0.38 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.79 | 0.04 | 0.14 | 0.18 | 0.04 | 0.02 | `cs_bucket_zscore(ts_decay_linear(ts_max(day_sum(Amt), 50), 25), cross_mean(day_sum(Amt), 30))` |
| R 1 variant 4 | 过 | 0.36 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.79 | 0.04 | 0.07 | 0.14 | 0.06 | 0.09 | `cs_regres(ts_decay_linear(ts_max(log(day_sum(Amt)), 50), 25), cross_mean(log(day_sum(Amt)), 30))` |
| R 1 variant 5 | 过 | 0.77 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.74 | 0.66 | 0.35 | 0.07 | 0.67 | 0.03 | `cs_bucket_zscore(ts_decay_linear(ts_max(day_sum(Amt), 50), 25), LogFloatCap)` |
| R 1 variant 6 | 过 | 0.19 | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` | 0.08 | 0.20 | 0.25 | 0.09 | 0.23 | 0.10 | `ts_decay_linear(ts_max(cross_zscore(log(day_sum(Amt)), 120), 50), 25)` |
| R 2 variant 1 | 过 | 0.23 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.36 | 0.01 | 0.20 | 0.26 | 0.04 | 0.19 | `ts_max(ts_std(log(ts_decay_linear(day_sum(Amt), 50)), 10), 10)` |
| R 2 variant 2 | 过 | 0.25 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.41 | 0.01 | 0.16 | 0.20 | 0.02 | 0.21 | `ts_max(div(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), ts_decay_linear(day_sum(Amt), 50)), 10)` |
| R 2 variant 3 | 过 | 0.52 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.85 | 0.02 | 0.20 | 0.11 | 0.06 | 0.21 | `ts_max(ts_std(log(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50)), 10), 10)` |
| R 2 variant 4 | 过 | 0.32 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.42 | 0.05 | 0.12 | 0.16 | 0.08 | 0.12 | `cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10), cross_mean(day_sum(Amt), 30))` |
| R 3 variant 1 | 过 | 0.69 | `ts_decay_linear(day_sum(Volume), 5)` | 0.94 | 0.01 | 0.04 | 0.07 | 0.06 | 0.17 | `cs_regres(ts_decay_linear(log(day_sum(Volume)), 5), ts_decay_linear(log(day_sum(Amt)), 5))` |
| R 3 variant 2 | 过 | 0.74 | `ts_decay_linear(day_sum(Volume), 5)` | 0.94 | 0.04 | 0.07 | 0.23 | 0.09 | 0.22 | `cs_bucket_zscore(ts_decay_linear(day_sum(Volume), 5), cross_mean(day_sum(Amt), 30))` |
| R 3 variant 3 | 过 | 0.37 | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Am` | 0.12 | 0.34 | 0.49 | 0.21 | 0.37 | 0.35 | `sub(ts_decay_linear(log(day_sum(Volume)), 5), LogFloatShares)` |
