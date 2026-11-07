# 相关度表:种子 902,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.12 | 0.15 | 0.06 | 0.15 | `cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.34 | 0.29 | 0.24 | 0.04 | `sub(cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 40))` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.37 | 0.21 | 0.27 | 0.05 | `sub(cross_mean(cs_winsor(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 60), cross_mean(cs_winsor(sub(div(day_last(Close), day_first(Open)), 1)), 60))` |
| slot a seed 4 | 废品 | 0.00 | `—` | 0.00 | 0.11 | 0.15 | 0.08 | 0.08 | 0.17 | `sub(cross_mean(is_gt0(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 60), cross_mean(is_gt0(sub(div(day_last(Close), day_first(Open)), 1)), 60))` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.14 | 0.04 | 0.05 | 0.10 | `cross_mean(mul(sign(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), sub(div(day_last(Close), day_first(Open)), 1)), 40)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.07 | 0.02 | 0.16 | 0.13 | `cross_corr(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1), 60)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.15 | 0.04 | 0.07 | 0.00 | `sub(cs_rank(cross_stddev(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)), cs_rank(cross_stddev(sub(div(day_last(Close), day_first(Open)), 1), 40)))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.13 | 0.17 | 0.07 | 0.12 | `cross_mean(div(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), LimitWidth), 30)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.38 | 0.14 | 0.37 | 0.00 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 20)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.33 | 0.28 | 0.26 | 0.00 | `cs_bucket_demean(sub(cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 40)), LogFloatCap)` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.05 | 0.16 | 0.00 | 0.12 | `div(cross_sum(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40), add(cross_sum(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), cross_sum(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.36 | 0.36 | 0.23 | 0.05 | `cross_ema(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 20)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.07 | 0.04 | 0.12 | 0.10 | `div(cross_sum(mul(sign(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), sub(div(day_last(Close), day_first(Open)), 1)), 40), cross_sum(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.24 | 0.25 | 0.15 | 0.08 | `sub(cross_med(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40), cross_med(sub(div(day_last(Close), day_first(Open)), 1), 40))` |
| slot a seed 15 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.51 | 0.05 | 0.41 | 0.20 | `cross_tail_mean_q25(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.27 | 0.31 | 0.46 | 0.28 | 0.02 | `sub(ts_sum(mul(greater(ts_rank(vol_1d, 20), 0.5), ret_1d), 20), ts_sum(mul(less(ts_rank(vol_1d, 20), 0.5), ret_1d), 20))` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.35 | 0.39 | 0.28 | 0.36 | 0.06 | `ts_sum(mul(greater(ts_rank(amt_1d, 60), 0.8), ret_1d), 60)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.00 | 0.15 | 0.05 | 0.03 | `ts_sum(mul(less(ts_rank(vol_1d, 60), 0.3), ret_1d), 60)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.23 | 0.50 | 0.15 | 0.02 | `sub(div(ts_sum(mul(vol_1d, ret_1d), 20), ts_sum(vol_1d, 20)), ts_mean(ret_1d, 20))` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.10 | 0.27 | 0.12 | 0.10 | `ts_corr(ret_1d, vol_1d, 40)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.09 | 0.00 | 0.12 | 0.04 | `ts_corr(ret_1d, mul(ts_delay(ret_1d, 1), ts_delay(sub(div(vol_1d, ts_mean(vol_1d, 20)), 1), 1)), 60)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.33 | 0.61 | 0.27 | 0.12 | `cross_mean(day_topw_mean(Ret, Volume), 20)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.32 | 0.57 | 0.27 | 0.13 | `cross_mean(sub(day_topw_mean(Ret, Volume), day_mean(Ret)), 20)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.01 | 0.01 | 0.16 | 0.45 | `cross_mean(div(day_topw_mean(Vwap, div(abs_(Ret), sqrt(Volume))), div(day_sum(Amt), day_sum(Volume))), 20)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.14 | 0.10 | 0.12 | 0.22 | `cross_mean(sub(cs_rank(day_signed_ratio(Ret, Amt)), cs_rank(ret_1d)), 20)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.00 | 0.02 | 0.16 | 0.45 | `cross_mean(sub(div(day_last(Close), div(day_sum(Amt), day_sum(Volume))), 1), 20)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.22 | 0.48 | 0.13 | 0.02 | `cs_bucket_demean(sub(div(ts_sum(mul(vol_1d, ret_1d), 20), ts_sum(vol_1d, 20)), ts_mean(ret_1d, 20)), LogFloatCap)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.22 | 0.26 | 0.15 | 0.01 | `ts_mean(mul(sign(ret_1d), sub(div(vol_1d, ts_mean(vol_1d, 20)), 1)), 40)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.09 | 0.19 | 0.19 | 0.07 | `cross_mean(day_corr(Close, Volume), 20)` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.16 | 0.25 | 0.35 | 0.20 | 0.28 | `cross_mean(day_signed_ratio(Ret, Amt), 40)` |
| slot b seed 16 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.11 | 0.01 | 0.07 | 0.03 | `ts_corr(ts_delay(day_signed_ratio(Ret, Amt), 1), ret_1d, 60)` |
