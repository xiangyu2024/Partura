# 相关度表:种子 911,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.29 | 0.26 | 0.29 | 0.01 | `cross_scale(LogFloatCap, 241)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.28 | 0.26 | 0.28 | 0.01 | `select_where(is_lt(ListAge, 15), -1, cross_scale(LogFloatCap, 241))` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.25 | 0.23 | 0.37 | 0.04 | `cs_last_high10(cross_scale(LogFloatCap, 241), cross_mean(day_flat_ratio(Close), 3))` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.20 | 0.17 | 0.26 | 0.01 | `cs_last_high10(cross_scale(LogFloatCap, 241), cross_max(day_at_max_ratio(Close), 2))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.31 | 0.27 | 0.28 | 0.00 | `cs_bucket_rank(cross_scale(LogFloatCap, 241), LogFloatCap)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.26 | 0.26 | 0.05 | 0.16 | `cs_bucket_rank(cross_scale(LogFloatCap, 241), cross_mean(day_sum(Amt), 60))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.27 | 0.10 | 0.29 | 0.01 | `cross_ema(cross_scale(LogFloatCap, 241), 10)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.59 | 0.04 | 0.03 | 0.11 | `sub(cs_rank(cross_scale(LogFloatCap, 241)), cs_rank(cross_mean(day_std(Ret), 20)))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.32 | 0.55 | 0.26 | 0.14 | `add(cs_rank(cross_scale(LogFloatCap, 241)), cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 20)))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.17 | 0.22 | 0.20 | 0.31 | `sub(cs_rank(cross_scale(LogFloatCap, 241)), cs_rank(sub(LogTotalCap, LogFloatCap)))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.56 | 0.02 | 0.05 | 0.53 | 0.50 | `cs_regres(cross_scale(LogFloatCap, 241), cross_mean(day_sum(Amt), 60))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.09 | 0.06 | 0.08 | 0.00 | `cs_flip_by_state(cross_scale(LogFloatCap, 241), day_sum(Amt))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.46 | 0.30 | 0.22 | 0.46 | 0.10 | `cs_last_low10(cross_scale(LogFloatCap, 241), cross_mean(day_sum(Amt), 60))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.07 | 0.06 | 0.28 | 0.03 | `sub(cs_rank(cross_scale(LogFloatCap, 241)), cs_rank(cross_mean(day_at_max_ratio(Close), 20)))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.29 | 0.27 | 0.27 | 0.02 | `select_where(is_lt(ListAge, 15), -1, cs_bucket_rank(cross_scale(LogFloatCap, 241), LogFloatCap))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.12 | 0.14 | 0.04 | 0.17 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.34 | 0.20 | 0.24 | 0.05 | `sub(cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.37 | 0.25 | 0.24 | 0.08 | `cross_ema(sub(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 40)` |
| slot b seed 4 | 废品 | 0.00 | `—` | 0.00 | 0.15 | 0.17 | 0.06 | 0.16 | 0.13 | `cross_med(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 90)` |
| slot b seed 5 | 废品 | 0.00 | `—` | 0.00 | 0.24 | 0.08 | 0.05 | 0.20 | 0.16 | `cross_mean(is_gt(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 0), 60)` |
| slot b seed 6 | 废品 | 0.00 | `—` | 0.00 | 0.14 | 0.15 | 0.06 | 0.10 | 0.20 | `sub(cross_mean(is_gt(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 0), 90), cross_mean(is_gt(sub(div(day_last(Close), day_first(Open)), 1), 0), 90))` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.33 | 0.19 | 0.27 | 0.00 | `cs_bucket_demean(sub(cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60)), LogFloatCap)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.19 | 0.31 | 0.13 | 0.21 | 0.09 | `sub(cs_rank(cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60)), cs_rank(cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60)))` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.06 | 0.14 | 0.01 | 0.14 | `div(cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60), add(cross_stddev(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60), 0.002))` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.51 | 0.05 | 0.41 | 0.20 | `cross_tail_mean_q25(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.30 | 0.53 | 0.16 | 0.02 | `cross_mean(sub(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 20)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.13 | 0.11 | 0.05 | 0.16 | `cs_regres(cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.09 | 0.01 | 0.18 | 0.17 | `cross_corr(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1), 120)` |
