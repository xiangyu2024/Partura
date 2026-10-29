# 相关度表:种子 801,C 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.04 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.07 | 0.07 | 0.45 | 0.07 | 0.08 | `cross_corr(log(div(day_last(Close), ts_delay(day_last(Close), 1))), day_sum(Amt), 20)` |
| slot a seed 2 | 过 | 0.06 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.11 | 0.06 | 0.20 | 0.10 | 0.11 | `cross_corr(log(div(day_last(Close), ts_delay(day_last(Close), 1))), day_sum(Amt), 60)` |
| slot a seed 3 | 过 | 0.03 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.10 | 0.13 | 0.50 | 0.11 | 0.07 | `cross_corr(log(div(day_last(Close), ts_delay(day_last(Close), 1))), cross_zscore(day_sum(Amt), 60), 20)` |
| slot a seed 4 | 过 | 0.03 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.06 | 0.08 | 0.38 | 0.06 | 0.05 | `cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 20)` |
| slot a seed 5 | 过 | 0.02 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.09 | 0.09 | 0.19 | 0.09 | 0.05 | `cross_corr(day_sum(Ret), day_sum(Amt), 40)` |
| slot a seed 6 | 过 | 0.00 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.02 | 0.10 | 0.20 | 0.54 | 0.12 | 0.01 | `cross_mean(mul(div(log(div(day_last(Close), ts_delay(day_last(Close), 1))), cross_stddev(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20)), cross_zscore(day_sum(Amt), 20)), 20)` |
| slot a seed 7 | 过 | 0.01 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.08 | 0.09 | 0.37 | 0.08 | 0.04 | `cross_regbeta(cross_zscore(day_sum(Amt), 60), div(log(div(day_last(Close), ts_delay(day_last(Close), 1))), cross_stddev(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 60)), 20)` |
| slot a seed 8 | 过 | 0.07 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.06 | 0.19 | 0.31 | 0.46 | 0.21 | 0.02 | `cross_mean(mul(log(div(day_last(Close), ts_delay(day_last(Close), 1))), sub(log(day_sum(Amt)), cross_mean(log(day_sum(Amt)), 60))), 20)` |
| slot a seed 9 | 过 | 0.02 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.06 | 0.17 | 0.28 | 0.53 | 0.20 | 0.09 | `cross_mean(day_corr(Ret, Amt), 20)` |
| slot a seed 10 | 过 | 0.03 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.06 | 0.20 | 0.28 | 0.45 | 0.23 | 0.10 | `cross_ema(day_corr(Ret, Amt), 10)` |
| slot a seed 11 | 过 | 0.00 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.13 | 0.31 | 0.49 | 0.17 | 0.01 | `cross_mean(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 20)` |
| slot a seed 12 | 过 | 0.02 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.15 | 0.23 | 0.27 | 0.54 | 0.24 | 0.14 | `cross_mean(div(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 20)` |
| slot a seed 13 | 过 | 0.08 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.10 | 0.07 | 0.02 | 0.20 | 0.07 | 0.02 | `cross_mean(mul(day_signed_ratio(Ret, Amt), cross_zscore(day_sum(Amt), 20)), 20)` |
| slot b seed 1 | 过 | 0.23 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.10 | 0.10 | 0.22 | 0.28 | 0.14 | 0.20 | `cross_mean(day_skew(Ret), 20)` |
| slot b seed 2 | 过 | 0.21 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.09 | 0.10 | 0.20 | 0.28 | 0.14 | 0.19 | `cross_mean(day_skew(in_logchg(Close, 1)), 20)` |
| slot b seed 3 | 过 | 0.14 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.07 | 0.20 | 0.18 | 0.28 | 0.21 | 0.09 | `cross_med(day_skew(in_logchg(Close, 5)), 20)` |
| slot b seed 4 | 过 | 0.24 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.08 | 0.11 | 0.20 | 0.22 | 0.15 | 0.23 | `cross_ema(day_skew(in_logchg(Close, 1)), 10)` |
| slot b seed 5 | 过 | 0.31 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.09 | 0.12 | 0.22 | 0.08 | 0.15 | 0.30 | `cross_mean(day_skew(Ret), 60)` |
| slot b seed 6 | 过 | 0.22 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.10 | 0.10 | 0.23 | 0.34 | 0.14 | 0.20 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(mul(Ret, Ret)), sqrt(day_sum(mul(Ret, Ret))))), 20)` |
| slot b seed 7 | 过 | 0.24 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.23 | 0.21 | 0.29 | 0.49 | 0.24 | 0.14 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), sign(Ret))), day_sum(mul(Ret, Ret))), 20)` |
| slot b seed 8 | 过 | 0.33 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.23 | 0.29 | 0.29 | 0.16 | 0.31 | 0.20 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), sign(Ret))), day_sum(mul(Ret, Ret))), 60)` |
| slot b seed 9 | 过 | 0.01 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.17 | 0.02 | 0.06 | 0.06 | 0.01 | 0.10 | `cross_mean(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 20)` |
| slot b seed 10 | 过 | 0.17 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.07 | 0.25 | 0.03 | 0.03 | 0.21 | 0.31 | `cross_mean(day_es_ratio_hi(in_logchg(Close, 1)), 20)` |
| slot b seed 11 | 过 | 0.55 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.53 | 0.08 | 0.13 | 0.15 | 0.05 | 0.40 | `cross_mean(div(day_max(Ret), day_std(Ret)), 20)` |
| slot b seed 12 | 过 | 0.04 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.04 | 0.16 | 0.17 | 0.15 | 0.18 | 0.08 | `ts_skew(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 60)` |
| slot b seed 13 | 过 | 0.04 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.03 | 0.17 | 0.17 | 0.11 | 0.19 | 0.08 | `ts_skew(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 120)` |
| slot b seed 14 | 过 | 0.07 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.01 | 0.13 | 0.24 | 0.54 | 0.14 | 0.03 | `cross_mean(div(sub(day_max(High), day_first(Open)), sub(day_max(High), day_min(Low))), 20)` |
| R 1 variant 1 | 过 | 1.00 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 1.00 | 0.28 | 0.08 | 0.01 | 0.29 | 0.78 | `LogFloatShares` |
| R 1 variant 2 | 过 | 1.00 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 1.00 | 0.28 | 0.08 | 0.01 | 0.29 | 0.78 | `inv(LogFloatShares)` |
| R 1 variant 3 | 过 | 0.58 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.87 | 0.32 | 0.07 | 0.08 | 0.27 | 0.02 | `sub(LogFloatCap, LogFloatShares)` |
| R 1 variant 4 | 过 | 0.07 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.30 | 0.46 | 0.01 | 0.09 | 0.42 | 0.42 | `log(day_last(Close))` |
| R 1 variant 5 | 过 | 0.58 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.87 | 0.32 | 0.07 | 0.04 | 0.26 | 0.03 | `cross_mean(sub(LogFloatCap, LogFloatShares), 20)` |
| R 1 variant 6 | 过 | 0.07 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.30 | 0.46 | 0.01 | 0.04 | 0.42 | 0.42 | `log(cross_mean(day_last(Close), 20))` |
| R 1 variant 7 | 过 | 1.00 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 1.00 | 0.28 | 0.08 | 0.01 | 0.29 | 0.78 | `cross_min(LogFloatShares, 20)` |
| R 1 variant 8 | 过 | 1.00 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 1.00 | 0.28 | 0.08 | 0.01 | 0.29 | 0.78 | `cross_max(LogFloatShares, 20)` |
| R 1 variant 9 | 过 | 0.53 | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` | 0.27 | 0.05 | 0.08 | 0.02 | 0.03 | 0.41 | `sub(LogTotalCap, LogFloatCap)` |
