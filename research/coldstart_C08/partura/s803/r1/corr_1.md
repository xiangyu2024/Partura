# 相关度表:种子 803,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.10 | 0.22 | 0.28 | 0.14 | 0.20 | `cross_mean(day_skew(Ret), 20)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.29 | 0.49 | 0.24 | 0.14 | `cross_mean(day_signed_ratio(Ret, mul(Ret, Ret)), 20)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.18 | 0.26 | 0.18 | 0.14 | `cross_mean(day_skew(in_logchg(Vwap, 1)), 20)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.26 | 0.34 | 0.16 | 0.15 | `cross_mean(day_skew(in_logchg(Close, 5)), 20)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.15 | 0.09 | 0.11 | 0.42 | `cross_mean(day_kurt(Ret), 20)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.06 | 0.06 | 0.01 | 0.10 | `cross_mean(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 20)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.03 | 0.15 | 0.02 | 0.04 | `sub(cross_mean(day_skew(Ret), 5), cross_mean(day_skew(Ret), 60))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.13 | 0.17 | 0.26 | 0.15 | 0.08 | `cross_mean(div(day_max(Ret), sub(day_max(Ret), day_min(Ret))), 20)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.16 | 0.31 | 0.13 | 0.08 | `ts_skew(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.04 | 0.49 | 0.08 | 0.01 | `cross_mean(div(sub(day_max(High), day_last(Close)), sub(day_max(High), day_min(Low))), 20)` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.16 | 0.22 | 0.28 | 0.19 | 0.12 | `cs_bucket_demean(cross_mean(day_skew(Ret), 20), day_last(Close))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.11 | 0.23 | 0.87 | 0.13 | 0.11 | `sub(cross_semistd_pos(day_last(Close), 20), cross_semistd_neg(day_last(Close), 20))` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.09 | 0.19 | 0.19 | 0.07 | `cross_mean(day_corr(Close, Volume), 20)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.28 | 0.53 | 0.20 | 0.09 | `cross_mean(day_corr(Ret, Volume), 20)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.32 | 0.58 | 0.25 | 0.02 | `cross_mean(day_corr(in_delay(Ret, 1), Volume), 20)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.01 | 0.02 | 0.09 | 0.06 | `cross_mean(day_corr(Ret, in_delay(Volume, 1)), 20)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.20 | 0.45 | 0.20 | 0.18 | `cross_mean(day_corr(in_logchg(Volume, 1), Ret), 20)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.43 | 0.23 | 0.15 | 0.43 | 0.00 | `cross_mean(day_corr(abs_(Ret), Volume), 20)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.16 | 0.21 | 0.11 | 0.14 | `cross_corr(day_last(Close), day_sum(Volume), 20)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.09 | 0.38 | 0.06 | 0.05 | `cross_corr(day_mean(Ret), day_sum(Amt), 20)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.50 | 0.25 | 0.10 | 0.50 | 0.09 | `cross_stddev(day_corr(Close, Volume), 20)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.00 | 0.03 | 0.14 | 0.00 | 0.01 | `sub(cross_mean(day_corr(Close, Volume), 5), cross_mean(day_corr(Close, Volume), 60))` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.18 | 0.56 | 0.10 | 0.22 | `cross_mean(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.17 | 0.29 | 0.15 | 0.14 | `cross_mean(day_wmean(sigmoid(in_zscore_expand(Ret)), Amt), 20)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.17 | 0.32 | 0.10 | 0.04 | `cross_mean(day_skew(mul(Ret, Amt)), 20)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.01 | 0.01 | 0.02 | 0.02 | `cs_flip_by_state(cross_mean(day_corr(Close, Volume), 20), day_sum(Amt))` |
