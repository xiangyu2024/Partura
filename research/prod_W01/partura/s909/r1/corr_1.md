# 相关度表:种子 909,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.29 | 0.10 | 0.20 | 0.24 | `cross_mean(day_skew(in_pct(Close, 5)), 60)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.31 | 0.25 | 0.23 | 0.10 | `cross_mean(day_skew(in_pct(Close, 15)), 30)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.29 | 0.11 | 0.24 | 0.11 | `cross_mean(day_skew(in_pct(Vwap, 10)), 60)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.23 | 0.01 | 0.00 | 0.39 | `cross_mean(day_kurt(in_pct(Close, 5)), 60)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.23 | 0.01 | 0.18 | 0.24 | `cross_mean(day_es_ratio_hi(in_pct(Close, 5)), 60)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.12 | 0.01 | 0.01 | 0.18 | `sub(cross_mean(day_es_ratio_hi(in_pct(Close, 5)), 60), cross_mean(day_es_ratio_lo(in_pct(Close, 5)), 60))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.24 | 0.06 | 0.04 | 0.36 | `div(cross_mean(day_max(in_pct(Close, 5)), 60), cross_mean(day_std(in_pct(Close, 5)), 60))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.48 | 0.12 | 0.26 | 0.23 | `cross_mean(add(day_max(in_pct(Close, 5)), day_min(in_pct(Close, 5))), 60)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.32 | 0.40 | 0.32 | 0.15 | `div(sub(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60)), add(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60)))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.16 | 0.61 | 0.12 | 0.16 | `sub(cs_rank(cross_semistd_pos(day_last(Close), 30)), cs_rank(cross_semistd_neg(day_last(Close), 30)))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.19 | 0.16 | 0.20 | 0.07 | `ts_skew(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.01 | 0.03 | 0.32 | 0.04 | `cross_mean(day_pos_ratio(in_pct(Close, 5)), 60)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.25 | 0.02 | 0.35 | 0.27 | `cross_mean(day_gini(in_pct(Close, 5)), 60)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.22 | 0.08 | 0.15 | 0.30 | `cross_mean(day_skew(Ret), 60)` |
| slot a seed 15 | 废品 | 0.00 | `—` | 0.00 | 0.18 | 0.32 | 0.13 | 0.21 | 0.10 | `sub(cross_mean(day_at_max_ratio(Close), 60), cross_mean(day_at_min_ratio(Close), 60))` |
| slot a seed 16 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.03 | 0.16 | 0.05 | 0.07 | `div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), ts_std(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.12 | 0.14 | 0.04 | 0.17 | `cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.41 | 0.35 | 0.32 | 0.01 | `cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.19 | 0.31 | 0.13 | 0.21 | 0.09 | `sub(cs_rank(cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)), cs_rank(cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60)))` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.37 | 0.29 | 0.24 | 0.07 | `cross_ema(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open))), 30)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.06 | 0.20 | 0.01 | 0.10 | `cross_mean(div(day_last(Close), day_wmean(Close, Volume)), 60)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.56 | 0.39 | 0.05 | 0.57 | 0.14 | `cross_mean(day_centroid(Amt), 60)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.56 | 0.19 | 0.08 | 0.54 | 0.44 | `cross_mean(day_wmean(is_gt(in_index(Amt), 0.875), Amt), 60)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.43 | 0.42 | 0.02 | 0.46 | 0.08 | `cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 60)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.09 | 0.05 | 0.14 | 0.04 | `cross_mean(sub(div(day_last(Close), day_last(in_delay(Close, 30))), 1), 60)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.16 | 0.24 | 0.04 | 0.07 | `cross_mean(day_corr(in_index(Close), Close), 60)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.30 | 0.36 | 0.31 | 0.33 | 0.22 | `cross_mean(day_signed_ratio(in_pct(Close, 5), Amt), 60)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.23 | 0.44 | 0.18 | 0.28 | 0.08 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.42 | 0.38 | 0.26 | 0.44 | 0.16 | `cross_mean(day_topw_mean(in_pct(Close, 1), Volume), 60)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.18 | 0.14 | 0.16 | 0.10 | `cross_mean(div(day_topw_mean(Vwap, div(abs_(in_pct(Close, 1)), sqrt(Volume))), day_wmean(Vwap, Volume)), 60)` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.40 | 0.24 | 0.42 | 0.07 | `cross_mean(day_corr(Amt, in_pct(Close, 5)), 60)` |
| slot b seed 16 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.14 | 0.13 | 0.01 | 0.23 | `cross_ema(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
