# 相关度表:种子 804,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.00 | `—` | 0.00 | 0.05 | 0.02 | 0.00 | 0.04 | 0.03 | `ts_var(LogFloatShares, 10)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.30 | 0.06 | 0.07 | 0.25 | 0.02 | `cs_last_high10(sub(LogFloatShares, LogFloatCap), mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)))` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.06 | 0.07 | 0.24 | 0.03 | `cs_last_high05(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 40))` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.14 | 0.39 | 0.07 | 0.09 | `cs_last_high10(div(cross_mean(day_sum(Volume), 5), cross_mean(day_sum(Volume), 60)), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 50))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.25 | 0.32 | 0.15 | 0.07 | `cs_last_high10(div(cross_mean(day_sum(Volume), 20), cross_mean(day_sum(Volume), 60)), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 50))` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.17 | 0.43 | 0.08 | 0.08 | `cs_last_high05(div(cross_mean(day_sum(Volume), 5), cross_mean(day_sum(Volume), 60)), mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.16 | 0.45 | 0.09 | 0.11 | `cs_last_high10(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60)), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 40))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.34 | 0.07 | 0.34 | 0.31 | `cs_last_high20(sub(log(cross_mean(day_sum(Volume), 20)), LogFloatShares), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 20))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.07 | 0.06 | 0.20 | 0.02 | `cs_last_high10(cs_last_high10(sub(LogFloatShares, LogFloatCap), mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8))), sub(LogFloatShares, cross_ema(LogFloatShares, 241)))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.09 | 0.33 | 0.04 | 0.22 | `cs_last_high10(cs_last_high10(div(cross_mean(day_sum(Volume), 5), cross_mean(day_sum(Volume), 60)), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 50)), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.30 | 0.06 | 0.07 | 0.25 | 0.02 | `cs_last_high10(sub(LogFloatShares, LogFloatCap), mul(ts_var(LogFloatShares, 10), sign(ts_delta(LogFloatShares, 10))))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.17 | 0.42 | 0.07 | 0.07 | `cs_first_low20(cs_last_high10(div(cross_mean(day_sum(Volume), 5), cross_mean(day_sum(Volume), 60)), mul(ts_var(LogFloatShares, 10), sign(ts_delta(LogFloatShares, 10)))), mul(ts_var(LogFloatShares, 10), sign(ts_delta(LogFloatShares, 10))))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.05 | 0.04 | 0.17 | 0.19 | `cs_last_high20(cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 60)), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.18 | 0.39 | 0.09 | 0.08 | `cs_last_high10(div(cross_mean(day_sum(Volume), 10), cross_mean(day_sum(Volume), 60)), ts_mean(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(LogFloatShares, 10), 1e-8)), 30))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.14 | 0.39 | 0.07 | 0.09 | `cs_last_high10(div(cross_mean(day_sum(Volume), 5), cross_mean(day_sum(Volume), 60)), ts_max(mul(ts_var(LogFloatShares, 10), sign(ts_delta(LogFloatShares, 10))), 50))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.16 | 0.19 | 0.10 | 0.12 | `cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.13 | 0.14 | 0.05 | 0.17 | `cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.18 | 0.15 | 0.10 | 0.14 | `cross_ema(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.61 | 0.15 | 0.48 | 0.09 | `cross_mean(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 20)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.28 | 0.53 | 0.15 | 0.02 | `sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), cross_mean(log(div(day_last(Close), day_first(Open))), 20))` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.33 | 0.20 | 0.23 | 0.05 | `sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), cross_mean(log(div(day_last(Close), day_first(Open))), 60))` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.03 | 0.04 | 0.13 | 0.09 | `cross_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 20)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.07 | 0.02 | 0.16 | 0.13 | `cross_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 60)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.11 | 0.09 | 0.04 | 0.07 | `cross_mean(mul(sign(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), log(div(day_last(Close), day_first(Open)))), 20)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.08 | 0.00 | 0.10 | 0.01 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.15 | 0.04 | 0.23 | 0.08 | `cross_mean(div(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), add(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), abs_(log(div(day_last(Close), day_first(Open)))))), 20)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.38 | 0.14 | 0.37 | 0.00 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 20)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.05 | 0.23 | 0.03 | 0.08 | `cross_mean(mul(log(div(day_first(Open), ts_delay(day_last(Close), 1))), div(day_first(Amt), day_sum(Amt))), 20)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.05 | 0.22 | 0.05 | 0.06 | `cross_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), div(day_first(Amt), day_sum(Amt)), 20)` |
