# 相关度表:种子 905,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.07 | 0.08 | 0.27 | 0.02 | `sub(LogFloatCap, LogFloatShares)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.06 | 0.09 | 0.22 | 0.00 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.17 | 0.04 | 0.04 | 0.21 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), cross_mean(day_sum(Amt), 20))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.00 | 0.09 | 0.28 | 0.03 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), cross_mean(day_std(Ret), 20))` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.03 | `mul(cs_rank(sub(LogFloatCap, LogFloatShares)), sub(cs_state_rank(log(day_last(Close)), 120), 0.5))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | `mul(cs_rank(sub(LogFloatCap, LogFloatShares)), sub(cs_state_rank(day_sum(Amt), 60), 0.5))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.00 | 0.04 | 0.06 | 0.03 | `cs_flip_by_state(sub(LogFloatCap, LogFloatShares), log(day_last(Close)))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.00 | 0.05 | 0.06 | 0.03 | `cs_flip_by_state(sub(LogFloatCap, LogFloatShares), day_sum(Amt))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.16 | 0.23 | 0.14 | 0.10 | 0.13 | `add(cs_rank(sub(LogFloatCap, LogFloatShares)), cs_rank(neg(cross_mean(day_skew(Ret), 20))))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.18 | 0.39 | 0.32 | 0.04 | `add(cs_rank(sub(LogFloatCap, LogFloatShares)), cs_rank(cross_zscore(cross_mean(day_sum(Amt), 5), 120)))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.23 | 0.03 | 0.41 | 0.20 | 0.12 | `add(cs_rank(sub(LogFloatCap, LogFloatShares)), cs_rank(div(day_last(Close), cross_max(day_last(Close), 120))))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.05 | 0.10 | 0.40 | 0.42 | `add(cs_rank(sub(LogFloatCap, LogFloatShares)), cs_rank(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.00 | 0.04 | 0.18 | 0.24 | `add(cs_rank(sub(LogFloatCap, LogFloatShares)), cs_rank(sub(LogTotalCap, LogFloatCap)))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.31 | 0.13 | 0.10 | 0.15 | `mul(cs_rank(sub(LogFloatCap, LogFloatShares)), cs_rank(neg(cross_mean(day_skew(Ret), 20))))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.16 | 0.34 | 0.47 | 0.21 | 0.08 | `cross_zscore(cross_mean(day_std(Amt), 10), 120)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.22 | 0.53 | 0.10 | 0.11 | `div(cross_mean(day_std(Amt), 10), cross_mean(day_std(Amt), 60))` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.28 | 0.15 | 0.24 | 0.05 | `cross_zscore(cross_mean(day_gini(Amt), 10), 120)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.20 | 0.24 | 0.10 | 0.05 | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.09 | 0.04 | 0.09 | 0.00 | `cross_zscore(cross_mean(day_kurt(Amt), 10), 120)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.16 | 0.33 | 0.49 | 0.20 | 0.08 | `cross_zscore(cross_mean(day_sum(Amt), 5), 120)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.30 | 0.43 | 0.37 | 0.35 | 0.14 | `div(cross_mean(day_sum(Amt), 20), cross_mean(day_sum(Amt), 120))` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.36 | 0.41 | 0.08 | 0.05 | `cross_zscore(cross_mean(day_std(Ret), 10), 120)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.35 | 0.42 | 0.14 | 0.04 | `cross_zscore(cross_mean(div(sub(day_max(High), day_min(Low)), day_mean(Vwap)), 10), 120)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.12 | 0.33 | 0.07 | 0.04 | `sub(cross_mean(day_skew(Ret), 20), cross_mean(day_skew(Ret), 120))` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.03 | 0.53 | 0.04 | 0.20 | `div(day_last(Close), cross_max(day_last(Close), 120))` |
| slot b seed 12 | 废品 | 0.00 | `—` | 0.00 | 0.25 | 0.34 | 0.63 | 0.27 | 0.12 | `cross_rank(day_last(Close), 120)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.12 | 0.14 | 0.04 | 0.17 | `cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
