# 相关度表:种子 2071,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.65 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.34 | 0.31 | 0.53 | 0.26 | 0.32 | 0.02 | `div(sub(day_max(High), day_min(Low)), day_open(Open))` |
| slot a seed 1 | 过 | 0.84 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.72 | 0.36 | 0.66 | 0.26 | 0.40 | 0.09 | `ts_std(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| slot a seed 2 | 过 | 0.21 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.19 | 0.01 | 0.17 | 0.47 | 0.03 | 0.05 | `div(ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 5), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60))` |
| slot a seed 3 | 废品 | 0.12 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.09 | 0.01 | 0.09 | 0.33 | 0.01 | 0.01 | `ts_rank(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60)` |
| slot a seed 4 | 过 | 0.04 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.09 | 0.09 | 0.02 | 0.45 | 0.07 | 0.05 | `sub(ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 5), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 40))` |
| slot a seed 5 | 过 | 0.09 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.12 | 0.10 | 0.04 | 0.12 | 0.12 | `ts_skew(div(sub(day_max(High), day_min(Low)), day_open(Open)), 40)` |
| slot a seed 6 | 过 | 0.16 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.28 | 0.03 | 0.07 | 0.17 | 0.01 | 0.13 | `div(ts_std(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20))` |
| slot a seed 7 | 过 | 0.07 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.01 | 0.07 | 0.07 | 0.22 | 0.07 | 0.02 | `ts_delta(ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 5), 10)` |
| slot a seed 8 | 过 | 0.12 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.10 | 0.00 | 0.10 | 0.34 | 0.01 | 0.04 | `div(div(sub(day_max(High), day_min(Low)), day_open(Open)), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60))` |
| slot a seed 9 | 过 | 0.12 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.18 | 0.09 | 0.07 | 0.04 | 0.10 | 0.06 | `ts_corr(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(Amt), 20)` |
| slot a seed 10 | 过 | 0.37 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.18 | 0.18 | 0.31 | 0.55 | 0.19 | 0.07 | `ts_corr(div(sub(day_max(High), day_min(Low)), day_open(Open)), div(sub(day_close(Close), day_open(Open)), day_open(Open)), 20)` |
| slot a seed 11 | 过 | 0.76 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.42 | 0.42 | 0.63 | 0.08 | 0.41 | 0.02 | `ts_min(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| slot a seed 12 | 过 | 0.26 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.24 | 0.03 | 0.22 | 0.51 | 0.05 | 0.05 | `ts_decay_linear(div(div(sub(day_max(High), day_min(Low)), day_open(Open)), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60)), 10)` |
| slot b seed 1 | 过 | 0.04 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.16 | 0.10 | 0.01 | 0.54 | 0.09 | 0.01 | `ts_mean(div(sub(day_close(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 20)` |
| slot b seed 2 | 废品 | 0.08 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.10 | 0.01 | 0.11 | 0.50 | 0.02 | 0.02 | `ts_mean(sub(day_argmax(High), day_argmin(Low)), 20)` |
| slot b seed 3 | 过 | 0.26 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.17 | 0.14 | 0.15 | 0.28 | 0.17 | 0.15 | `ts_mean(day_skew(Ret), 20)` |
| slot b seed 4 | 过 | 0.93 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.60 | 0.28 | 0.85 | 0.25 | 0.33 | 0.21 | `ts_mean(day_max(Ret), 20)` |
| slot b seed 5 | 过 | 0.17 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.04 | 0.25 | 0.13 | 0.19 | 0.25 | 0.04 | `ts_mean(div(sub(day_open(Open), ts_delay(day_close(Close), 1)), ts_delay(day_close(Close), 1)), 20)` |
| slot b seed 6 | 过 | 0.71 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.38 | 0.42 | 0.58 | 0.17 | 0.46 | 0.01 | `ts_std(div(sub(day_open(Open), ts_delay(day_close(Close), 1)), ts_delay(day_close(Close), 1)), 20)` |
| slot b seed 7 | 过 | 0.05 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.00 | 0.01 | 0.03 | 0.00 | 0.12 | `ts_mean(div(abs_(sub(day_close(Close), day_open(Open))), sub(day_max(High), day_min(Low))), 20)` |
| slot b seed 8 | 过 | 0.31 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.50 | 0.09 | 0.12 | 0.08 | 0.06 | 0.37 | `ts_mean(day_kurt(Ret), 20)` |
| slot b seed 9 | 过 | 0.37 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.18 | 0.18 | 0.31 | 0.55 | 0.19 | 0.07 | `ts_corr(div(sub(day_max(High), day_min(Low)), day_open(Open)), div(sub(day_close(Close), day_open(Open)), day_open(Open)), 20)` |
| slot b seed 10 | 过 | 0.27 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.12 | 0.22 | 0.56 | 0.13 | 0.03 | `ts_mean(day_corr(Ret, Amt), 20)` |
