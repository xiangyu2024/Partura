# 相关度表:种子 806,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.48 | 0.26 | 0.14 | 0.16 | `day_max(Ret)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.11 | 0.10 | 0.07 | 0.43 | `cross_ema(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), 10)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.15 | 0.13 | 0.08 | 0.38 | `cross_tail_mean_q75(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), 20)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.15 | 0.12 | 0.07 | 0.31 | `cross_max(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), 20)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.17 | 0.23 | 0.12 | 0.14 | `cross_mean(sub(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), div(sub(day_mean(Ret), day_min(Ret)), day_std(Ret))), 20)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.13 | 0.19 | 0.09 | 0.12 | `cross_ema(sub(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), div(sub(day_mean(Ret), day_min(Ret)), day_std(Ret))), 5)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.28 | 0.40 | 0.00 | 0.03 | `cross_ema(cross_madz(day_max(Ret), 60), 5)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.03 | 0.05 | 0.07 | 0.40 | `cs_bucket_rank(cross_ema(day_max(Ret), 10), cross_mean(day_std(Ret), 20))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.12 | 0.07 | 0.20 | 0.49 | `cs_bucket_rank(cross_ema(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), 10), cross_mean(day_zero_ratio(Ret), 20))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.07 | 0.04 | 0.11 | 0.30 | `cs_last_high10(cross_ema(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), 10), cross_max(day_zero_ratio(Ret), 15))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.05 | 0.11 | 0.12 | 0.33 | `cs_last_low05(cross_ema(div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret)), 10), cross_valid_count(day_last(Close), 120))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.63 | 0.03 | 0.01 | 0.55 | 0.36 | `cross_ema(div(day_max(Ret), log(div(day_max(High), day_min(Low)))), 10)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.12 | 0.11 | 0.09 | 0.44 | `div(cross_ema(day_max(Ret), 10), cross_ema(day_std(Ret), 10))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.58 | 0.10 | 0.13 | 0.33 | `cross_max(day_max(Ret), 30)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.60 | 0.12 | 0.16 | 0.28 | `cs_last_low10(cross_max(cross_product(day_max(Ret), 3), 30), cross_valid_count(day_last(Close), 32))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.16 | 0.19 | 0.10 | 0.12 | `cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 20)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.18 | 0.11 | 0.11 | 0.11 | `cross_ema(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 5)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.40 | 0.23 | 0.34 | 0.00 | `cross_tail_mean_q75(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 20)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.28 | 0.53 | 0.15 | 0.02 | `cross_mean(sub(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open)))), 20)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.29 | 0.45 | 0.17 | 0.03 | `cross_ema(sub(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open)))), 10)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.03 | 0.04 | 0.13 | 0.09 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 20)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.09 | 0.02 | 0.08 | 0.00 | `cross_corr(cross_delay(log(div(day_last(Close), day_first(Open))), 1), log(div(day_first(Open), cross_delay(day_last(Close), 1))), 20)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.09 | 0.02 | 0.11 | 0.02 | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.05 | 0.23 | 0.03 | 0.08 | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Amt), day_sum(Amt))), 20)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.38 | 0.14 | 0.37 | 0.00 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 20)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.09 | 0.17 | 0.08 | 0.13 | `div(cross_ema(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 10), cross_ema(day_std(Ret), 10))` |
