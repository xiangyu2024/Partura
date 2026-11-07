# 相关度表:种子 904,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 1.00 | 0.28 | 0.19 | 0.02 | 0.31 | 0.03 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` |
| slot a seed 1 | 过 | 0.45 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.43 | 0.15 | 0.26 | 0.44 | 0.18 | 0.00 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)), 0.65))` |
| slot a seed 2 | 过 | 0.45 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.38 | 0.09 | 0.08 | 0.02 | 0.08 | 0.12 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), abs_(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)), 0.65))` |
| slot a seed 3 | 过 | 0.47 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.39 | 0.12 | 0.12 | 0.02 | 0.12 | 0.14 | `sub(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(log(div(cs_robust_z(day_mean(Low)), day_first(Open)))), 0.65))` |
| slot a seed 4 | 过 | 0.57 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.52 | 0.15 | 0.21 | 0.29 | 0.17 | 0.08 | `add(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), add(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)), cs_rank(cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), abs_(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60))))` |
| slot a seed 5 | 过 | 0.38 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.34 | 0.13 | 0.25 | 0.46 | 0.16 | 0.00 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.3), mul(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)), 0.7))` |
| slot a seed 6 | 过 | 0.67 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.67 | 0.21 | 0.23 | 0.34 | 0.23 | 0.01 | `mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)))` |
| slot a seed 7 | 过 | 0.67 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.61 | 0.21 | 0.10 | 0.01 | 0.20 | 0.06 | `mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), cs_rank(cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), abs_(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)))` |
| slot a seed 8 | 过 | 0.68 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.61 | 0.23 | 0.13 | 0.03 | 0.23 | 0.07 | `mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), sub(1, cs_rank(log(div(cs_robust_z(day_mean(Low)), day_first(Open))))))` |
| slot a seed 9 | 过 | 0.53 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.82 | 0.22 | 0.16 | 0.04 | 0.20 | 0.72 | `cs_first_low40(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), LogFloatCap)` |
| slot a seed 10 | 过 | 0.50 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.81 | 0.59 | 0.00 | 0.07 | 0.58 | 0.71 | `cs_first_high40(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), LogFloatCap)` |
| slot a seed 11 | 过 | 0.68 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.86 | 0.54 | 0.04 | 0.06 | 0.55 | 0.46 | `cs_first_high20(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), LogFloatCap)` |
| slot a seed 12 | 过 | 0.82 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.83 | 0.25 | 0.18 | 0.00 | 0.27 | 0.16 | `cs_first_low40(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), ListAge)` |
| slot a seed 13 | 过 | 0.99 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.99 | 0.28 | 0.18 | 0.02 | 0.30 | 0.03 | `cs_first_high40(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), ListAge)` |
| slot a seed 14 | 过 | 0.37 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.59 | 0.04 | 0.59 | 0.02 | 0.06 | 0.10 | `cs_first_low40(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), cross_mean(day_std(Ret), 60))` |
| slot a seed 15 | 过 | 0.71 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.88 | 0.75 | 0.28 | 0.07 | 0.77 | 0.32 | `cs_first_high40(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), cross_mean(day_std(Amt), 30))` |
| slot a seed 16 | 过 | 0.50 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.82 | 0.38 | 0.05 | 0.03 | 0.36 | 0.33 | `cs_first_low20(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), cross_mean(day_std(Amt), 30))` |
| slot b seed 1 | 废品 | 0.13 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.10 | 0.09 | 0.33 | 0.07 | 0.00 | 0.08 | `cross_mean(day_at_max_ratio(Close), 50)` |
| slot b seed 2 | 过 | 0.16 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.12 | 0.06 | 0.37 | 0.06 | 0.02 | 0.12 | `cross_ema(day_at_max_ratio(Close), 30)` |
| slot b seed 3 | 废品 | 0.12 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.10 | 0.13 | 0.29 | 0.03 | 0.04 | 0.07 | `cross_mean(add(day_at_max_ratio(Close), day_at_min_ratio(Close)), 50)` |
| slot b seed 4 | 废品 | 0.26 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.16 | 0.18 | 0.32 | 0.13 | 0.21 | 0.10 | `cross_mean(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 60)` |
| slot b seed 5 | 废品 | 0.09 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.12 | 0.34 | 0.26 | 0.04 | 0.24 | 0.24 | `cross_mean(day_flat_run_max(Close), 50)` |
| slot b seed 6 | 过 | 0.10 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.09 | 0.15 | 0.28 | 0.06 | 0.07 | 0.09 | `cross_tail_mean_q75(day_at_max_ratio(Close), 60)` |
| slot b seed 7 | 过 | 0.10 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.10 | 0.13 | 0.28 | 0.08 | 0.05 | 0.01 | `cs_last_low05(cross_mean(day_at_max_ratio(Close), 50), ListAge)` |
| slot b seed 8 | 过 | 0.25 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.13 | 0.12 | 0.38 | 0.08 | 0.18 | 0.16 | `ts_regbeta(day_gini(Volume), day_at_max_ratio(Close), 50)` |
| slot b seed 9 | 过 | 0.27 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.20 | 0.04 | 0.36 | 0.06 | 0.02 | 0.31 | `ts_regbeta(day_gini(Volume), day_flat_run_max(Close), 50)` |
| slot b seed 10 | 过 | 0.25 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.12 | 0.15 | 0.36 | 0.07 | 0.20 | 0.15 | `ts_corr(day_gini(Volume), day_at_max_ratio(Close), 50)` |
| slot b seed 11 | 过 | 0.02 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.01 | 0.07 | 0.12 | 0.02 | 0.04 | 0.11 | `ts_regbeta(day_gini(Amt), day_at_min_ratio(Close), 50)` |
| slot b seed 12 | 过 | 0.19 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.18 | 0.28 | 0.29 | 0.04 | 0.21 | 0.40 | `ts_regbeta(day_gini(Volume), day_flat_ratio(Vwap), 50)` |
| slot b seed 13 | 过 | 0.08 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.08 | 0.05 | 0.10 | 0.01 | 0.06 | 0.08 | `ts_regbeta(day_centroid(Amt), day_sum(Ret), 60)` |
| slot b seed 14 | 过 | 0.14 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.11 | 0.13 | 0.16 | 0.00 | 0.14 | 0.07 | `ts_corr(day_centroid(Amt), day_signed_ratio(Ret, Amt), 60)` |
| slot b seed 15 | 过 | 0.18 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.17 | 0.10 | 0.14 | 0.02 | 0.13 | 0.07 | `ts_reg_tvalue(day_gini(Volume), day_ar1_coefficient(Ret), 60)` |
| slot b seed 16 | 过 | 0.21 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.11 | 0.18 | 0.20 | 0.11 | 0.20 | 0.04 | `cross_ema(ts_regres(day_gini(Volume), day_kurt(Vwap), 50), 20)` |
| R 1 variant 1 | 过 | 0.91 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.94 | 0.28 | 0.19 | 0.02 | 0.30 | 0.03 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 60)` |
| R 1 variant 2 | 过 | 0.83 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.83 | 0.28 | 0.19 | 0.01 | 0.30 | 0.04 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 75)` |
| R 1 variant 3 | 过 | 0.89 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.93 | 0.27 | 0.18 | 0.03 | 0.29 | 0.02 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 40)` |
| R 1 variant 4 | 过 | 0.77 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.75 | 0.28 | 0.19 | 0.01 | 0.30 | 0.05 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 90)` |
| R 1 variant 5 | 过 | 0.68 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.64 | 0.26 | 0.19 | 0.00 | 0.28 | 0.07 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 120)` |
| R 1 variant 6 | 过 | 0.91 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.94 | 0.28 | 0.19 | 0.02 | 0.30 | 0.03 | `ts_regbeta(day_gini(Amt), day_kurt(Vwap), 60)` |
| R 1 variant 7 | 过 | 0.83 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.83 | 0.28 | 0.19 | 0.01 | 0.30 | 0.04 | `ts_regbeta(day_gini(Amt), day_kurt(Vwap), 75)` |
| R 1 variant 8 | 过 | 0.87 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.86 | 0.27 | 0.20 | 0.01 | 0.30 | 0.06 | `add(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), ts_regbeta(day_gini(Volume), day_kurt(Vwap), 100))` |
| R 1 variant 9 | 过 | 0.82 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.84 | 0.25 | 0.18 | 0.01 | 0.27 | 0.06 | `cross_ema(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), 10)` |
| R 1 variant 10 | 过 | 0.63 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.61 | 0.20 | 0.17 | 0.02 | 0.22 | 0.10 | `cross_ema(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), 30)` |
| R 1 variant 11 | 过 | 0.91 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.94 | 0.28 | 0.19 | 0.02 | 0.30 | 0.03 | `ts_regbeta(add(day_gini(Volume), day_gini(Amt)), day_kurt(Vwap), 60)` |
| R 1 variant 12 | 过 | 0.90 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.93 | 0.27 | 0.20 | 0.02 | 0.29 | 0.06 | `ts_regbeta(day_gini(Volume), add(day_kurt(Vwap), day_kurt(Close)), 60)` |
| R 1 variant 13 | 过 | 0.63 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.58 | 0.25 | 0.18 | 0.00 | 0.26 | 0.08 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 150)` |
| R 1 variant 14 | 过 | 0.86 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.87 | 0.36 | 0.21 | 0.02 | 0.37 | 0.02 | `ts_corr(day_gini(Volume), day_kurt(Vwap), 60)` |
| R 1 variant 15 | 过 | 0.85 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.87 | 0.35 | 0.20 | 0.02 | 0.36 | 0.03 | `ts_reg_tvalue(day_gini(Volume), day_kurt(Vwap), 60)` |
| R 1 variant 16 | 过 | 0.18 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | 0.13 | 0.12 | 0.25 | 0.06 | 0.15 | 0.01 | `ts_regbeta(day_gini(Volume), day_skew(Vwap), 60)` |
