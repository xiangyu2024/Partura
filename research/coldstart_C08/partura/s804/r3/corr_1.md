# 相关度表:种子 804,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.30 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.08 | 0.47 | 0.08 | 0.01 | 0.41 | 0.42 | `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` |
| slot a seed 1 | 过 | 0.30 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.08 | 0.47 | 0.08 | 0.01 | 0.41 | 0.42 | `cs_last_high10(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ListAge)` |
| slot a seed 2 | 过 | 0.41 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.20 | 0.45 | 0.06 | 0.03 | 0.39 | 0.27 | `cs_last_low10(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ListAge)` |
| slot a seed 3 | 过 | 0.30 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.08 | 0.47 | 0.08 | 0.01 | 0.41 | 0.42 | `cs_last_high20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), cross_valid_count(day_last(Close), 60))` |
| slot a seed 4 | 过 | 0.34 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.07 | 0.52 | 0.09 | 0.01 | 0.47 | 0.57 | `cs_last_high20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` |
| slot a seed 5 | 过 | 0.31 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.05 | 0.13 | 0.03 | 0.06 | 0.09 | 0.23 | `cs_last_low20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` |
| slot a seed 6 | 过 | 0.70 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.55 | 0.33 | 0.04 | 0.03 | 0.28 | 0.00 | `cs_last_high20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 7 | 过 | 0.31 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.09 | 0.46 | 0.12 | 0.03 | 0.39 | 0.43 | `ts_mean(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 10)` |
| slot a seed 8 | 过 | 0.02 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.10 | 0.02 | 0.09 | 0.04 | 0.02 | 0.24 | `cs_last_high20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), cross_mean(day_zero_ratio(Ret), 20))` |
| slot a seed 9 | 过 | 0.35 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.13 | 0.49 | 0.00 | 0.00 | 0.43 | 0.32 | `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ts_var(ts_mean(day_distinct_ratio(Close), 20), 10))` |
| slot a seed 10 | 过 | 0.30 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.08 | 0.47 | 0.08 | 0.01 | 0.41 | 0.41 | `cs_last_high10(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LimitWidth)` |
| slot a seed 11 | 过 | 0.05 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.18 | 0.37 | 0.12 | 0.01 | 0.32 | 0.50 | `cs_first_low20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ListAge)` |
| slot a seed 12 | 过 | 0.30 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.09 | 0.46 | 0.10 | 0.02 | 0.40 | 0.43 | `cs_last_high20(ts_mean(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 5), ListAge)` |
| slot b core | 过 | 0.08 | `day_mean(in_logchg(Amt, 30))` | 0.15 | 0.09 | 0.01 | 0.06 | 0.09 | 0.26 | `day_kurt(Ret)` |
| slot b seed 1 | 过 | 0.06 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.13 | 0.06 | 0.07 | 0.11 | 0.33 | `ts_mean(day_kurt(Ret), 5)` |
| slot b seed 2 | 过 | 0.10 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.14 | 0.10 | 0.08 | 0.12 | 0.37 | `ts_mean(day_kurt(Ret), 10)` |
| slot b seed 3 | 过 | 0.15 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.15 | 0.15 | 0.09 | 0.11 | 0.42 | `ts_mean(day_kurt(Ret), 20)` |
| slot b seed 4 | 过 | 0.11 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.15 | 0.18 | 0.13 | 0.01 | 0.15 | 0.50 | `ts_mean(day_kurt(Ret), 60)` |
| slot b seed 5 | 过 | 0.17 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.12 | 0.17 | 0.09 | 0.08 | 0.33 | `ts_max(day_kurt(Ret), 20)` |
| slot b seed 6 | 过 | 0.14 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.18 | 0.14 | 0.18 | 0.02 | 0.09 | 0.36 | `ts_max(day_kurt(Ret), 60)` |
| slot b seed 7 | 过 | 0.18 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.18 | 0.12 | 0.17 | 0.09 | 0.07 | 0.33 | `ts_stddev(day_kurt(Ret), 20)` |
| slot b seed 8 | 过 | 0.19 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.18 | 0.11 | 0.19 | 0.07 | 0.06 | 0.32 | `ts_stddev(ts_mean(day_kurt(Ret), 5), 20)` |
| slot b seed 9 | 废品 | 0.10 | `day_mean(in_logchg(Amt, 30))` | 0.07 | 0.01 | 0.01 | 0.03 | 0.01 | 0.00 | `ts_rank(day_kurt(Ret), 20)` |
| slot b seed 10 | 过 | 0.07 | `day_mean(in_logchg(Amt, 30))` | 0.15 | 0.10 | 0.00 | 0.05 | 0.10 | 0.26 | `sub(day_kurt(Ret), mul(day_skew(Ret), day_skew(Ret)))` |
| slot b seed 11 | 过 | 0.12 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.17 | 0.19 | 0.08 | 0.05 | 0.17 | 0.43 | `ts_mean(sub(day_kurt(Ret), mul(day_skew(Ret), day_skew(Ret))), 20)` |
| slot b seed 12 | 过 | 0.15 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.15 | 0.15 | 0.09 | 0.11 | 0.42 | `cs_last_high10(ts_mean(day_kurt(Ret), 20), ListAge)` |
| slot b seed 13 | 过 | 0.10 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.14 | 0.10 | 0.08 | 0.12 | 0.37 | `cs_last_high20(ts_mean(day_kurt(Ret), 10), cross_valid_count(day_last(Close), 60))` |
| slot b seed 14 | 过 | 0.15 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_l` | 0.16 | 0.15 | 0.15 | 0.09 | 0.11 | 0.42 | `cs_first_low20(ts_mean(day_kurt(Ret), 20), LimitWidth)` |
| R 1 variant 1 | 过 | 0.81 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.73 | 0.27 | 0.03 | 0.03 | 0.22 | 0.06 | `cs_last_high20(cs_last_high10(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| R 1 variant 2 | 过 | 0.87 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.78 | 0.31 | 0.03 | 0.01 | 0.26 | 0.01 | `cs_last_high20(cs_last_high10(cs_last_high20(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| R 1 variant 3 | 过 | 0.46 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinc` | 0.27 | 0.49 | 0.10 | 0.02 | 0.44 | 0.55 | `cs_last_high20(cs_last_high10(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), LogFloatCap)` |
