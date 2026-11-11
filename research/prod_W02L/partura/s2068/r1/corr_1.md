# 相关度表:种子 2068,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 1.00 | 0.34 | 0.65 | 0.31 | 0.36 | 0.01 | `day_sum(abs_(in_slice(Ret, 1, 30)))` |
| slot a seed 1 | 过 | 0.60 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.65 | 0.12 | 0.10 | 0.09 | 0.11 | 0.10 | `div(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(Ret)))` |
| slot a seed 2 | 过 | 0.56 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.32 | 0.05 | 0.05 | 0.42 | 0.04 | 0.07 | `sub(day_sum(abs_(in_slice(Ret, 1, 30))), ts_mean(day_sum(abs_(in_slice(Ret, 1, 30))), 60))` |
| slot a seed 3 | 过 | 0.64 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.24 | 0.02 | 0.12 | 0.40 | 0.00 | 0.02 | `div(sub(day_sum(abs_(in_slice(Ret, 1, 30))), ts_mean(day_sum(abs_(in_slice(Ret, 1, 30))), 60)), ts_stddev(day_sum(abs_(in_slice(Ret, 1, 30))), 60))` |
| slot a seed 4 | 废品 | 0.61 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.27 | 0.05 | 0.06 | 0.37 | 0.03 | 0.01 | `ts_rank(day_sum(abs_(in_slice(Ret, 1, 30))), 40)` |
| slot a seed 5 | 过 | 0.88 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.87 | 0.34 | 0.43 | 0.25 | 0.35 | 0.03 | `sub(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))))` |
| slot a seed 6 | 过 | 0.46 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.19 | 0.02 | 0.05 | 0.04 | 0.02 | 0.03 | `div(day_sum(abs_(in_slice(Ret, 1, 30))), ts_mean(day_sum(abs_(in_slice(Ret, 1, 30))), 5))` |
| slot a seed 7 | 过 | 0.38 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.18 | 0.05 | 0.07 | 0.07 | 0.05 | 0.01 | `ts_delta(day_sum(abs_(in_slice(Ret, 1, 30))), 5)` |
| slot a seed 8 | 过 | 0.10 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.03 | 0.00 | 0.01 | 0.08 | 0.00 | 0.02 | `mul(day_sum(abs_(in_slice(Ret, 1, 30))), day_corr(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)))` |
| slot a seed 9 | 过 | 0.58 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.64 | 0.08 | 0.09 | 0.08 | 0.07 | 0.13 | `div(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 31, 210))))` |
| slot a seed 10 | 过 | 0.21 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.09 | 0.13 | 0.10 | 0.03 | 0.13 | 0.05 | `ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 20)` |
| slot a seed 11 | 过 | 0.61 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.69 | 0.17 | 0.21 | 0.14 | 0.17 | 0.17 | `ts_decay_linear(div(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(Ret))), 10)` |
| slot a seed 12 | 废品 | 0.36 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.11 | 0.03 | 0.01 | 0.09 | 0.03 | 0.01 | `sub(ts_rank(day_sum(abs_(in_slice(Ret, 1, 30))), 20), ts_rank(day_sum(abs_(in_slice(Ret, 211, 240))), 20))` |
| slot b seed 1 | 过 | 0.15 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.06 | 0.25 | 0.13 | 0.19 | 0.25 | 0.04 | `ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 20)` |
| slot b seed 2 | 过 | 0.31 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), d` | 0.03 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `sub(ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 20), ts_mean(sub(div(day_last(Close), day_open(Open)), 1), 20))` |
| slot b seed 3 | 过 | 0.39 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.05 | 0.34 | 0.36 | 0.32 | 0.36 | 0.07 | `sub(ts_sum(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 40), ts_sum(sub(div(day_last(Close), day_open(Open)), 1), 40))` |
| slot b seed 4 | 过 | 0.18 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.06 | 0.26 | 0.15 | 0.13 | 0.26 | 0.04 | `ts_decay_linear(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 20)` |
| slot b seed 5 | 过 | 0.13 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.08 | 0.26 | 0.11 | 0.17 | 0.25 | 0.06 | `div(ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 20), ts_stddev(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 20))` |
| slot b seed 6 | 废品 | 0.07 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), d` | 0.04 | 0.00 | 0.02 | 0.08 | 0.00 | 0.02 | `ts_rank(sub(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_open(Open)), 1)), 30)` |
| slot b seed 7 | 过 | 0.72 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.63 | 0.30 | 0.57 | 0.14 | 0.30 | 0.08 | `sub(ts_mean(abs_(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1)), 20), ts_mean(abs_(sub(div(day_last(Close), day_open(Open)), 1)), 20))` |
| slot b seed 8 | 过 | 0.04 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.08 | 0.19 | 0.01 | 0.00 | 0.18 | 0.12 | `ts_corr(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_open(Open)), 1), 40)` |
| slot b seed 9 | 过 | 0.17 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.04 | 0.22 | 0.15 | 0.09 | 0.22 | 0.03 | `mul(ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 10), ts_mean(abs_(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1)), 40))` |
| slot b seed 10 | 废品 | 0.07 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), d` | 0.08 | 0.05 | 0.01 | 0.05 | 0.04 | 0.04 | `sub(ts_rank(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 20), ts_rank(sub(div(day_last(Close), day_open(Open)), 1), 20))` |
| slot b seed 11 | 过 | 0.01 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.11 | 0.01 | 0.02 | 0.07 | 0.01 | 0.01 | `ts_delta(ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 10), 10)` |
| slot b seed 12 | 过 | 0.07 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.07 | 0.05 | 0.08 | 0.03 | 0.06 | 0.03 | `sub(ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 5), ts_mean(sub(div(day_open(Open), cross_delay(day_last(Close), 1)), 1), 60))` |
