# 相关度表:种子 803,C 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_kurt(Ret)` | 1.00 | 0.09 | 0.01 | 0.06 | 0.09 | 0.26 | `day_kurt(Ret)` |
| slot a seed 1 | 过 | 0.89 | `day_kurt(Ret)` | 0.82 | 0.17 | 0.08 | 0.12 | 0.15 | 0.14 | `mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret)))` |
| slot a seed 2 | 过 | 0.49 | `day_kurt(Ret)` | 0.79 | 0.17 | 0.17 | 0.06 | 0.16 | 0.24 | `cross_mean(mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret))), 20)` |
| slot a seed 3 | 过 | 0.50 | `day_kurt(Ret)` | 0.75 | 0.16 | 0.11 | 0.01 | 0.14 | 0.27 | `cross_ema(cs_winsor(mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret)))), 20)` |
| slot a seed 4 | 过 | 0.91 | `day_kurt(Ret)` | 0.77 | 0.11 | 0.06 | 0.10 | 0.10 | 0.16 | `sub(add(day_kurt(Ret), 3), div(3, sub(1, day_zero_ratio(Ret))))` |
| slot a seed 5 | 过 | 0.49 | `day_kurt(Ret)` | 0.74 | 0.02 | 0.10 | 0.04 | 0.02 | 0.29 | `cross_mean(sub(add(day_kurt(Ret), 3), div(3, sub(1, day_zero_ratio(Ret)))), 20)` |
| slot a seed 6 | 过 | 0.94 | `day_kurt(Ret)` | 0.81 | 0.21 | 0.01 | 0.04 | 0.19 | 0.28 | `cs_bucket_rank(day_kurt(Ret), cross_mean(day_zero_ratio(Ret), 20))` |
| slot a seed 7 | 过 | 0.45 | `day_kurt(Ret)` | 0.86 | 0.25 | 0.15 | 0.07 | 0.20 | 0.45 | `cs_bucket_rank(cross_mean(day_kurt(Ret), 20), cross_mean(day_zero_ratio(Ret), 20))` |
| slot a seed 8 | 过 | 0.42 | `day_kurt(Ret)` | 0.85 | 0.26 | 0.17 | 0.06 | 0.20 | 0.44 | `cs_bucket_zscore(cross_mean(day_kurt(Ret), 20), cross_mean(day_zero_ratio(Ret), 20))` |
| slot a seed 9 | 过 | 0.48 | `day_kurt(Ret)` | 0.86 | 0.22 | 0.08 | 0.04 | 0.20 | 0.42 | `cs_bucket_rank(cross_mean(day_kurt(Ret), 20), cross_mean(day_flat_run_max(Ret), 20))` |
| slot a seed 10 | 过 | 0.49 | `day_kurt(Ret)` | 0.87 | 0.10 | 0.14 | 0.10 | 0.06 | 0.33 | `cs_bucket_rank(cross_mean(day_kurt(Ret), 20), day_last(Close))` |
| slot a seed 11 | 过 | 0.47 | `day_kurt(Ret)` | 0.75 | 0.10 | 0.15 | 0.05 | 0.09 | 0.28 | `cs_bucket_rank(cross_mean(mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret))), 20), day_last(Close))` |
| slot a seed 12 | 过 | 0.51 | `day_kurt(Ret)` | 0.80 | 0.01 | 0.10 | 0.03 | 0.01 | 0.34 | `cs_bucket_rank(cross_mean(mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret))), 20), cross_mean(day_sum(Amt), 20))` |
| slot b seed 1 | 过 | 0.31 | `day_kurt(Ret)` | 0.50 | 0.51 | 0.11 | 0.12 | 0.47 | 0.01 | `cross_mean(div(day_std(in_pct(Close, 5)), day_std(in_pct(Close, 1))), 20)` |
| slot b seed 2 | 过 | 0.26 | `day_kurt(Ret)` | 0.46 | 0.57 | 0.10 | 0.13 | 0.53 | 0.11 | `cross_mean(div(day_std(in_pct(Close, 15)), day_std(in_pct(Close, 1))), 20)` |
| slot b seed 3 | 过 | 0.14 | `day_kurt(Ret)` | 0.38 | 0.72 | 0.08 | 0.12 | 0.67 | 0.31 | `cross_mean(div(day_std(in_logchg(Vwap, 10)), day_std(in_logchg(Vwap, 1))), 20)` |
| slot b seed 4 | 过 | 0.29 | `day_kurt(Ret)` | 0.46 | 0.53 | 0.09 | 0.10 | 0.48 | 0.03 | `cross_mean(abs_(sub(log(div(day_std(in_pct(Close, 5)), day_std(in_pct(Close, 1)))), 0.8047)), 20)` |
| slot b seed 5 | 过 | 0.23 | `day_kurt(Ret)` | 0.52 | 0.69 | 0.17 | 0.12 | 0.66 | 0.17 | `cross_mean(day_autocorr(in_logchg(Vwap, 1), 1), 20)` |
| slot b seed 6 | 过 | 0.07 | `day_kurt(Ret)` | 0.06 | 0.29 | 0.41 | 0.11 | 0.32 | 0.14 | `cross_mean(abs_(day_autocorr(in_logchg(Vwap, 1), 1)), 20)` |
| slot b seed 7 | 过 | 0.38 | `day_kurt(Ret)` | 0.56 | 0.38 | 0.03 | 0.03 | 0.34 | 0.14 | `cross_ema(day_autocorr(in_pct(Close, 1), 1), 20)` |
| slot b seed 8 | 过 | 0.04 | `day_kurt(Ret)` | 0.07 | 0.01 | 0.03 | 0.01 | 0.01 | 0.05 | `cross_mean(day_autocorr(in_logchg(Vwap, 1), 5), 20)` |
| slot b seed 9 | 过 | 0.33 | `day_kurt(Ret)` | 0.55 | 0.40 | 0.12 | 0.08 | 0.36 | 0.08 | `cross_mean(mul(div(abs_(day_sum(Ret)), day_sum(abs_(Ret))), sqrt(mul(241, sub(1, day_zero_ratio(Ret))))), 20)` |
| slot b seed 10 | 过 | 0.31 | `day_kurt(Ret)` | 0.43 | 0.36 | 0.10 | 0.09 | 0.33 | 0.14 | `cs_bucket_rank(cross_mean(div(day_std(in_pct(Close, 5)), day_std(in_pct(Close, 1))), 20), day_last(Close))` |
| slot b seed 11 | 过 | 0.15 | `day_kurt(Ret)` | 0.21 | 0.29 | 0.07 | 0.10 | 0.31 | 0.03 | `cs_bucket_rank(cross_mean(day_autocorr(in_logchg(Vwap, 1), 1), 20), cross_mean(day_zero_ratio(Ret), 20))` |
| slot b seed 12 | 过 | 0.27 | `day_kurt(Ret)` | 0.41 | 0.07 | 0.07 | 0.08 | 0.04 | 0.29 | `cs_bucket_rank(cross_mean(div(abs_(day_sum(Ret)), day_sum(abs_(Ret))), 20), cross_mean(day_zero_ratio(Ret), 20))` |
| R 1 variant 1 | 过 | 0.69 | `day_kurt(Ret)` | 0.80 | 0.07 | 0.01 | 0.07 | 0.07 | 0.11 | `day_kurt(in_logchg(Vwap, 1))` |
| R 1 variant 2 | 过 | 1.00 | `day_kurt(Ret)` | 1.00 | 0.09 | 0.01 | 0.06 | 0.09 | 0.26 | `day_kurt(in_pct(Close, 1))` |
| R 1 variant 3 | 废品 | 0.39 | `day_kurt(Ret)` | 0.34 | 0.08 | 0.15 | 0.08 | 0.08 | 0.16 | `day_kurt(in_madz(Ret, 30))` |
| R 1 variant 4 | 过 | 0.29 | `day_kurt(Ret)` | 0.18 | 0.67 | 0.09 | 0.13 | 0.63 | 0.41 | `day_gini(Ret)` |
| R 1 variant 5 | 过 | 0.46 | `day_kurt(Ret)` | 0.52 | 0.44 | 0.01 | 0.02 | 0.41 | 0.36 | `day_gini(in_logchg(Vwap, 1))` |
| R 1 variant 6 | 过 | 0.47 | `day_kurt(Ret)` | 0.40 | 0.08 | 0.04 | 0.01 | 0.07 | 0.12 | `day_es_ratio_hi(Ret)` |
| R 1 variant 7 | 过 | 0.38 | `day_kurt(Ret)` | 0.42 | 0.09 | 0.05 | 0.01 | 0.08 | 0.10 | `day_es_ratio_lo(Ret)` |
