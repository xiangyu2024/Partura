# 相关度表:种子 901,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.46 | 0.01 | 0.09 | 0.42 | 0.42 | `day_last(Close)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.05 | 0.06 | 0.21 | 0.01 | `cs_bucket_rank(day_last(Close), LogFloatCap)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.18 | 0.05 | 0.01 | 0.23 | `cs_bucket_rank(day_last(Close), cross_mean(day_std(Amt), 30))` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.01 | 0.01 | 0.16 | 0.45 | `sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.04 | 0.03 | 0.07 | 0.01 | `cs_bucket_rank(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), LogFloatCap)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.34 | 0.00 | 0.06 | 0.33 | 0.48 | `cs_bucket_rank(day_last(Close), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.05 | 0.01 | 0.16 | 0.43 | `sub(cs_rank(day_last(Close)), cs_rank(sub(LogFloatCap, LogFloatShares)))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.14 | 0.07 | 0.45 | 0.15 | 0.26 | `div(day_last(Close), cross_max(day_last(Close), 241))` |
| slot a seed 8 | 废品 | 0.00 | `—` | 0.00 | 0.25 | 0.34 | 0.63 | 0.27 | 0.12 | `cross_rank(day_last(Close), 120)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.30 | 0.78 | 0.21 | 0.13 | `sub(log(day_last(Close)), cross_mean(log(day_last(Close)), 60))` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.36 | 0.57 | 0.20 | 0.00 | `cs_bucket_rank(sub(log(day_last(Close)), cross_mean(log(day_last(Close)), 120)), LogFloatCap)` |
| slot a seed 11 | 废品 | 0.00 | `—` | 0.00 | 0.34 | 0.31 | 0.34 | 0.35 | 0.21 | `div(day_last(Close), ts_delay(day_last(Close), 120))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.02 | 0.01 | 0.03 | 0.02 | `cs_flip_by_state(day_last(Close), cross_mean(day_mean(Ret), 20))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.04 | 0.05 | 0.11 | 0.10 | `cs_flip_by_state(day_last(Close), day_sum(Amt))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.01 | 0.03 | 0.01 | 0.00 | `cs_flip_by_state(cs_bucket_rank(day_last(Close), LogFloatCap), cross_mean(day_mean(Ret), 20))` |
| slot a seed 15 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.29 | 0.76 | 0.19 | 0.08 | `cross_zscore(day_last(Close), 60)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.22 | 0.18 | 0.25 | 0.37 | `cross_mean(day_signed_ratio(Ret, Amt), 120)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.58 | 0.36 | 0.04 | 0.59 | 0.14 | `cross_ema(day_centroid(Amt), 60)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.11 | 0.13 | 0.10 | 0.15 | `cross_corr(day_sum(Volume), day_last(Close), 40)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.36 | 0.29 | 0.15 | 0.37 | 0.19 | `cross_mean(cs_rank(day_corr(Ret, Volume)), 120)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.42 | 0.10 | 0.26 | 0.12 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.47 | 0.34 | 0.17 | 0.47 | 0.19 | `cross_mean(day_topw_mean(Ret, Volume), 120)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.32 | 0.12 | 0.21 | 0.08 | `cross_mean(sub(sub(div(day_last(Close), day_first(Open)), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 120)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.12 | 0.14 | 0.04 | 0.17 | `cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.09 | 0.05 | 0.16 | 0.06 | `cross_mean(sub(div(day_last(Close), day_last(in_slice(Close, 0, 210))), 1), 120)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.28 | 0.32 | 0.22 | 0.28 | 0.01 | `cross_mean(sub(div(day_last(in_slice(Close, 0, 30)), day_first(Open)), 1), 60)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.03 | 0.02 | 0.28 | 0.16 | `cross_mean(day_autocorr(Ret, 1), 120)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.20 | 0.03 | 0.11 | 0.35 | `cross_mean(day_skew(Ret), 120)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.76 | 0.14 | 0.02 | 0.68 | 0.53 | `cross_mean(day_gini(Amt), 120)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.32 | 0.40 | 0.32 | 0.15 | `div(sub(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60)), add(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60)))` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.06 | 0.55 | 0.06 | 0.01 | `sub(cross_mean(day_signed_ratio(Ret, Amt), 20), cross_mean(day_signed_ratio(Ret, Amt), 120))` |
