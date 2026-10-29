# 相关度表:种子 808,C 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.06 | 0.09 | 0.22 | 0.00 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.06 | 0.08 | 0.23 | 0.08 | `cs_regres(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.06 | 0.09 | 0.22 | 0.00 | `cs_bucket_rank(log(div(day_sum(Amt), day_sum(Volume))), LogFloatCap)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.07 | 0.04 | 0.22 | 0.00 | `cs_bucket_rank(cross_mean(log(div(day_sum(Amt), day_sum(Volume))), 20), LogFloatCap)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.00 | 0.09 | 0.22 | 0.02 | `cs_bucket_rank(cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap), cross_mean(day_std(Ret), 20))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.14 | 0.07 | 0.04 | 0.15 | `cs_bucket_rank(cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap), cross_mean(day_sum(Amt), 30))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.10 | 0.11 | 0.28 | 0.20 | `cs_bucket_rank(cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap), ListAge)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.16 | 0.05 | 0.07 | 0.12 | 0.22 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogTotalCap)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.05 | 0.08 | 0.23 | 0.09 | `cs_regres(cs_regres(sub(LogFloatCap, LogFloatShares), LogFloatCap), cross_mean(day_std(Ret), 20))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.22 | 0.14 | 0.07 | 0.15 | `sub(cs_rank(cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)), cs_rank(cross_mean(day_skew(Ret), 20)))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.45 | 0.24 | 0.14 | 0.02 | `sub(cs_rank(cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)), cs_rank(div(cross_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), LimitWidth)))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.14 | 0.13 | 0.06 | 0.13 | `mul(sub(1.0, cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)), cs_rank(cross_mean(day_skew(Ret), 20)))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.28 | 0.53 | 0.20 | 0.09 | `cross_mean(day_corr(Ret, Volume), 20)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.38 | 0.49 | 0.20 | 0.02 | `cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.32 | 0.57 | 0.27 | 0.13 | `cross_mean(sub(day_topw_mean(Ret, Volume), day_mean(Ret)), 20)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.01 | 0.07 | 0.18 | 0.13 | `cross_mean(day_corr(Ret, in_delay(mul(Ret, Volume), 1)), 20)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.09 | 0.19 | 0.19 | 0.07 | `cross_mean(day_corr(Close, Volume), 20)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.34 | 0.23 | 0.34 | 0.13 | `cross_mean(day_corr(Ret, Volume), 60)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.28 | 0.45 | 0.23 | 0.10 | `cross_ema(day_corr(Ret, Amt), 10)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.27 | 0.51 | 0.19 | 0.10 | `div(cross_mean(day_corr(Ret, Volume), 20), cross_stddev(day_corr(Ret, Volume), 20))` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.28 | 0.50 | 0.15 | 0.00 | `cs_bucket_rank(cross_mean(day_corr(Ret, Volume), 20), LogFloatCap)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.43 | 0.23 | 0.15 | 0.43 | 0.00 | `cross_mean(day_corr(abs_(Ret), Volume), 20)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.01 | 0.43 | 0.07 | 0.02 | `cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20), cross_mean(day_std(Ret), 20))` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.20 | 0.32 | 0.02 | 0.16 | `sub(cs_rank(cross_mean(day_corr(Ret, Volume), 20)), cs_rank(cross_mean(day_corr(Ret, in_delay(mul(Ret, Volume), 1)), 20)))` |
