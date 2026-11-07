# 相关度表:种子 902,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.18 | 0.14 | 0.28 | 0.09 | `div(day_first(Amt), day_sum(Amt))` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.37 | 0.03 | 0.35 | 0.10 | `cross_ema(div(day_first(Amt), day_sum(Amt)), 30)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.00 | 0.12 | 0.23 | 0.04 | 0.06 | `cross_mean(cross_zscore(div(day_first(Amt), day_sum(Amt)), 60), 20)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.10 | 0.20 | 0.10 | 0.12 | `sub(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), cross_mean(div(day_first(Amt), day_sum(Amt)), 120))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.31 | 0.36 | 0.08 | 0.39 | 0.00 | `cs_bucket_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 30), LogFloatCap)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.37 | 0.08 | 0.37 | 0.04 | `cs_bucket_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 30), ListAge)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.58 | 0.33 | 0.02 | 0.61 | 0.18 | `cross_med(div(day_first(Amt), day_sum(Amt)), 40)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.34 | 0.03 | 0.15 | 0.23 | `cross_tail_mean_q75(div(day_first(Amt), day_sum(Amt)), 60)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.28 | 0.05 | 0.02 | 0.27 | `cross_stddev(div(day_first(Amt), day_sum(Amt)), 40)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.02 | 0.13 | 0.02 | 0.09 | `sub(cross_mean(mul(div(day_first(Amt), day_sum(Amt)), is_gt0(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1))), 40), cross_mean(mul(div(day_first(Amt), day_sum(Amt)), is_gt0(neg(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)))), 40))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.26 | 0.02 | 0.15 | 0.72 | `cs_first_low40(cross_mean(div(day_first(Amt), day_sum(Amt)), 30), LogFloatCap)` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.61 | 0.10 | 0.10 | 0.64 | 0.72 | `cs_first_high40(cross_mean(div(day_first(Amt), day_sum(Amt)), 30), LogFloatCap)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.61 | 0.33 | 0.02 | 0.65 | 0.20 | `cross_mean(cs_rank(div(day_first(Amt), day_sum(Amt))), 40)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.57 | 0.27 | 0.12 | 0.59 | 0.47 | `sub(cross_mean(cs_rank(div(day_first(Amt), day_sum(Amt))), 30), cross_mean(cs_rank(div(day_last(Amt), day_sum(Amt))), 30))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.40 | 0.33 | 0.08 | 0.48 | 0.17 | `cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 30)` |
| slot a seed 15 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.09 | 0.05 | 0.46 | 0.21 | `cross_mean(cs_last_high10(div(day_first(Amt), day_sum(Amt)), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 30)` |
| slot a seed 16 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.32 | 0.08 | 0.12 | 0.17 | `cross_mean(cs_bucket_rank(div(day_first(Amt), day_sum(Amt)), cross_mean(day_sum(Amt), 20)), 30)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.03 | 0.09 | 0.27 | 0.43 | `cross_mean(div(day_last(Amt), day_sum(Amt)), 30)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.51 | 0.23 | 0.14 | 0.50 | 0.40 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 30)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.43 | 0.45 | 0.09 | 0.47 | 0.05 | `cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 30)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.33 | 0.01 | 0.16 | 0.33 | `cross_mean(div(day_sum(in_slice(Amt, 61, 180)), day_sum(Amt)), 40)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.54 | 0.41 | 0.09 | 0.56 | 0.11 | `cross_mean(day_centroid(in_slice(Amt, 1, 239)), 40)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.55 | 0.42 | 0.13 | 0.57 | 0.15 | `sub(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 30), cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 30))` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.07 | 0.08 | 0.12 | 0.03 | `cross_mean(day_last(in_pct(Close, 30)), 30)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.29 | 0.38 | 0.22 | 0.00 | `cross_mean(day_first(in_pct(Close, 30)), 30)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.04 | 0.15 | 0.00 | 0.11 | `cross_mean(day_signed_ratio(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), 30)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.15 | 0.29 | 0.07 | 0.12 | `cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.14 | 0.10 | 0.05 | 0.01 | `cross_mean(sub(day_signed_ratio(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30))), 30)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.51 | 0.42 | 0.13 | 0.54 | 0.19 | `cross_mean(sub(div(day_sum(in_slice(Amt, 1, 5)), day_sum(Amt)), div(day_sum(in_slice(Amt, 236, 240)), day_sum(Amt))), 30)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.05 | 0.14 | 0.01 | 0.02 | `cross_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 5), 120)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.09 | 0.06 | 0.04 | 0.01 | `cs_bucket_rank(cross_mean(div(day_last(Amt), day_sum(Amt)), 30), LogFloatCap)` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.49 | 0.20 | 0.15 | 0.49 | 0.46 | `cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 20)` |
