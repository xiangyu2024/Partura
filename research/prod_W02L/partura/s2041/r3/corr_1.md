# 相关度表:种子 2041,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.59 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.22 | 0.04 | 0.04 | 0.17 | 0.04 | 0.04 | `day_corr(in_delta(Vwap, 5), Volume)` |
| slot a seed 1 | 过 | 0.36 | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_firs` | 0.14 | 0.26 | 0.36 | 0.60 | 0.28 | 0.07 | `cross_mean(day_corr(in_delta(Vwap, 5), Volume), 20)` |
| slot a seed 2 | 过 | 0.55 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.10 | 0.02 | 0.04 | 0.08 | 0.02 | 0.02 | `cross_zscore(day_corr(in_delta(Vwap, 5), Volume), 30)` |
| slot a seed 3 | 过 | 0.35 | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(` | 0.08 | 0.40 | 0.26 | 0.13 | 0.38 | 0.13 | `ts_skew(day_corr(in_delta(Vwap, 5), Volume), 40)` |
| slot a seed 4 | 过 | 0.07 | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(` | 0.03 | 0.09 | 0.04 | 0.01 | 0.09 | 0.03 | `cross_semistd_pos(day_corr(in_delta(Vwap, 5), Volume), 30)` |
| slot a seed 5 | 过 | 0.55 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.09 | 0.03 | 0.03 | 0.11 | 0.03 | 0.02 | `sub(day_corr(in_delta(Vwap, 5), Volume), cross_mean(day_corr(in_delta(Vwap, 5), Volume), 40))` |
| slot a seed 6 | 过 | 0.29 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.15 | 0.13 | 0.22 | 0.45 | 0.15 | 0.01 | `cs_bucket_demean(cross_mean(day_corr(in_delta(Vwap, 5), Volume), 10), LogFloatCap)` |
| slot a seed 7 | 过 | 0.58 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.20 | 0.04 | 0.04 | 0.17 | 0.04 | 0.04 | `cs_bucket_zscore(day_corr(in_delta(Vwap, 5), Volume), ListAge)` |
| slot a seed 8 | 过 | 0.24 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.14 | 0.12 | 0.06 | 0.29 | 0.11 | 0.12 | `cs_bucket_zscore(cross_mean(day_corr(in_delta(Vwap, 5), Volume), 5), day_sum(Amt))` |
| slot a seed 9 | 过 | 0.13 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Vol` | 0.14 | 0.07 | 0.06 | 0.32 | 0.07 | 0.05 | `cs_last_high10(cross_mean(day_corr(in_delta(Vwap, 5), Volume), 15), day_gini(High))` |
| slot a seed 10 | 过 | 0.34 | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(` | 0.29 | 0.23 | 0.04 | 0.26 | 0.22 | 0.11 | `cross_tail_mean_q25(day_corr(in_delta(Vwap, 5), Volume), 30)` |
| slot a seed 11 | 过 | 0.38 | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_firs` | 0.17 | 0.31 | 0.37 | 0.51 | 0.33 | 0.09 | `cross_ema(day_corr(in_delta(Vwap, 5), Volume), 10)` |
| slot a seed 12 | 过 | 0.36 | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_firs` | 0.14 | 0.26 | 0.36 | 0.60 | 0.28 | 0.07 | `cs_robust_z(cross_mean(day_corr(in_delta(Vwap, 5), Volume), 20))` |
| slot b seed 1 | 过 | 0.16 | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(` | 0.21 | 0.25 | 0.13 | 0.19 | 0.25 | 0.04 | `cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 20)` |
| slot b seed 2 | 过 | 0.31 | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_firs` | 0.23 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open))), 20)` |
| slot b seed 3 | 过 | 0.11 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Vol` | 0.09 | 0.15 | 0.01 | 0.00 | 0.15 | 0.10 | `cross_corr(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open)), 20)` |
| slot b seed 4 | 过 | 0.12 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Vol` | 0.10 | 0.19 | 0.01 | 0.00 | 0.18 | 0.12 | `cross_corr(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open)), 40)` |
| slot b seed 5 | 过 | 0.15 | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(` | 0.21 | 0.22 | 0.15 | 0.08 | 0.22 | 0.04 | `cs_bucket_demean(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 10), LogFloatCap)` |
| slot b seed 6 | 过 | 0.03 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Vol` | 0.07 | 0.00 | 0.01 | 0.05 | 0.00 | 0.02 | `cross_zscore(div(day_first(Open), cross_delay(day_last(Close), 1)), 30)` |
| slot b seed 7 | 过 | 0.31 | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_firs` | 0.23 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `sub(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 20), cross_mean(div(day_last(Close), day_first(Open)), 20))` |
| slot b seed 8 | 过 | 0.09 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Vol` | 0.09 | 0.14 | 0.01 | 0.01 | 0.14 | 0.08 | `cs_bucket_zscore(cross_corr(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open)), 20), ListAge)` |
| slot b seed 9 | 过 | 0.66 | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(` | 0.34 | 0.44 | 0.55 | 0.07 | 0.48 | 0.02 | `cross_semistd_neg(div(day_first(Open), cross_delay(day_last(Close), 1)), 30)` |
| slot b seed 10 | 过 | 0.29 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), ` | 0.24 | 0.14 | 0.17 | 0.46 | 0.16 | 0.06 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_close(Vwap), day_first(Open))), 10)` |
