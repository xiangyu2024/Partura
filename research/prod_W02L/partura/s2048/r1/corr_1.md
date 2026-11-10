# 相关度表:种子 2048,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.20 | 0.41 | 0.12 | 0.14 | `div(day_close(Close), cross_max(day_close(Close), 241))` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.11 | 0.53 | 0.01 | 0.10 | `div(day_close(Close), cross_max(day_close(Close), 120))` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.02 | 0.63 | 0.10 | 0.09 | `div(day_close(Close), cross_max(day_close(Close), 60))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.20 | 0.27 | 0.12 | 0.14 | `div(cross_ema(day_close(Close), 5), cross_max(day_close(Close), 241))` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.42 | 0.43 | 0.29 | 0.15 | `div(sub(day_close(Close), cross_min(day_close(Close), 241)), sub(cross_max(day_close(Close), 241), cross_min(day_close(Close), 241)))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.53 | 0.33 | 0.40 | 0.13 | `div(day_close(Close), cross_min(day_close(Close), 241))` |
| slot a seed 7 | 废品 | 0.00 | `—` | 0.00 | 0.25 | 0.30 | 0.09 | 0.26 | 0.15 | `cross_argmax(day_close(Close), 241)` |
| slot a seed 8 | 废品 | 0.00 | `—` | 0.00 | 0.26 | 0.30 | 0.08 | 0.26 | 0.12 | `sub(cross_argmax(day_close(Close), 241), cross_argmin(day_close(Close), 241))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.34 | 0.22 | 0.23 | 0.12 | `div(cross_max(day_close(Close), 20), cross_max(day_close(Close), 241))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.07 | 0.14 | 0.07 | 0.12 | `div(cross_delay(day_close(Close), 20), cross_max(day_close(Close), 241))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.18 | 0.40 | 0.11 | 0.17 | `div(day_close(Vwap), cross_max(day_max(High), 241))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.31 | 0.03 | 0.26 | 0.09 | `sub(div(day_close(Close), cross_max(day_close(Close), 241)), div(day_close(Close), cross_max(day_close(Close), 60)))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.17 | 0.31 | 0.07 | 0.11 | `cross_mean(div(day_close(Close), cross_max(day_close(Close), 120)), 20)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.37 | 0.44 | 0.11 | 0.37 | 0.15 | `div(cross_min(day_close(Close), 20), cross_min(day_close(Close), 241))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.13 | 0.19 | 0.25 | 0.04 | `cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 20)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.07 | 0.13 | 0.24 | 0.03 | `cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 60)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.04 | 0.10 | 0.21 | 0.01 | `cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.04 | 0.07 | 0.15 | 0.06 | `cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 241)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.37 | 0.45 | 0.35 | 0.39 | 0.07 | `cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.38 | 0.37 | 0.12 | 0.39 | 0.08 | `cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.37 | 0.32 | 0.10 | 0.37 | 0.06 | `sub(cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 120))` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.27 | 0.05 | 0.33 | 0.03 | `sub(cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 241), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241))` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.40 | 0.36 | 0.19 | 0.41 | 0.06 | `sub(cross_ema(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 60), cross_ema(sub(div(day_close(Close), day_open(Open)), 1), 60))` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.35 | 0.28 | 0.11 | 0.35 | 0.08 | `div(sub(cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 120)), add(cross_stddev(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120), 0.001))` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.04 | 0.01 | 0.20 | 0.15 | `cross_corr(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), sub(div(day_close(Close), day_open(Open)), 1), 120)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.01 | 0.00 | 0.03 | 0.05 | `cross_regbeta(cross_delay(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 1), sub(div(day_close(Close), day_open(Open)), 1), 120)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.46 | 0.04 | 0.25 | 0.12 | `sub(cross_mean(abs_(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)), 120), cross_mean(abs_(sub(div(day_close(Close), day_open(Open)), 1)), 120))` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.17 | 0.00 | 0.12 | 0.01 | `cross_regbeta(cross_delay(sub(div(day_close(Close), day_open(Open)), 1), 1), sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120)` |
