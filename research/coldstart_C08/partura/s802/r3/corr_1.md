# 相关度表:种子 802,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 16 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.74 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.55 | 0.41 | 0.22 | 0.17 | 0.43 | 0.29 | `day_mean(in_delta(Volume, 30))` |
| slot a seed 1 | 过 | 0.70 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.50 | 0.34 | 0.20 | 0.14 | 0.36 | 0.26 | `mul(day_mean(in_delta(Volume, 30)), day_at_max_ratio(Close))` |
| slot a seed 2 | 过 | 0.70 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.48 | 0.33 | 0.19 | 0.13 | 0.35 | 0.27 | `mul(day_mean(in_delta(Volume, 30)), day_at_min_ratio(Close))` |
| slot a seed 3 | 过 | 0.03 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(sig` | 0.05 | 0.01 | 0.00 | 0.03 | 0.01 | 0.01 | `mul(day_mean(in_delta(Volume, 30)), sub(day_at_max_ratio(Close), day_at_min_ratio(Close)))` |
| slot a seed 4 | 过 | 0.69 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.54 | 0.44 | 0.20 | 0.15 | 0.45 | 0.28 | `cs_regres(day_mean(in_delta(Volume, 30)), day_at_max_ratio(Close))` |
| slot a seed 5 | 过 | 0.73 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.55 | 0.42 | 0.22 | 0.17 | 0.44 | 0.28 | `cs_regres(day_mean(in_delta(Volume, 30)), day_at_min_ratio(Close))` |
| slot a seed 6 | 过 | 0.38 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, ` | 0.36 | 0.48 | 0.39 | 0.19 | 0.53 | 0.30 | `cross_mean(mul(day_mean(in_delta(Volume, 30)), day_at_max_ratio(Close)), 20)` |
| slot a seed 7 | 过 | 0.33 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, ` | 0.32 | 0.49 | 0.34 | 0.08 | 0.54 | 0.34 | `cross_mean(mul(day_mean(in_delta(Volume, 30)), day_at_min_ratio(Close)), 20)` |
| slot a seed 8 | 过 | 0.40 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.11 | 0.03 | 0.04 | 0.01 | 0.04 | 0.00 | `cross_delta(mul(day_mean(in_delta(Volume, 30)), day_at_max_ratio(Close)), 5)` |
| slot a seed 9 | 过 | 0.40 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.08 | 0.03 | 0.03 | 0.02 | 0.03 | 0.00 | `cross_delta(mul(day_mean(in_delta(Volume, 30)), day_at_min_ratio(Close)), 5)` |
| slot a seed 10 | 过 | 0.18 | `ts_cov(LogTotalCap, day_centroid(Volume), 40)` | 0.16 | 0.03 | 0.18 | 0.25 | 0.05 | 0.07 | `cross_mean(mul(day_mean(in_delta(Volume, 30)), sub(day_at_max_ratio(Close), day_at_min_ratio(Close))), 20)` |
| slot b core | 过 | 0.42 | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Clos` | 0.40 | 0.46 | 0.01 | 0.09 | 0.42 | 0.42 | `day_quantile_q25(Close)` |
| slot b seed 1 | 过 | 0.40 | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Clos` | 0.38 | 0.52 | 0.08 | 0.15 | 0.47 | 0.25 | `mul(day_quantile_q25(Close), day_distinct_ratio(Close))` |
| slot b seed 2 | 过 | 0.16 | `ts_cov(cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_c` | 0.23 | 0.03 | 0.21 | 0.09 | 0.03 | 0.42 | `cs_regres(day_quantile_q25(Close), day_distinct_ratio(Close))` |
| slot b seed 3 | 过 | 0.21 | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Clos` | 0.16 | 0.38 | 0.18 | 0.18 | 0.34 | 0.05 | `cs_regres(day_distinct_ratio(Close), day_quantile_q25(Close))` |
| slot b seed 4 | 过 | 0.41 | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Clos` | 0.39 | 0.54 | 0.09 | 0.07 | 0.49 | 0.25 | `cross_mean(mul(day_quantile_q25(Close), day_distinct_ratio(Close)), 20)` |
| slot b seed 5 | 过 | 0.20 | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Clos` | 0.36 | 0.19 | 0.08 | 0.03 | 0.20 | 0.63 | `cs_regres(day_quantile_q25(Close), LogFloatCap)` |
| slot b seed 6 | 过 | 0.20 | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Clos` | 0.36 | 0.19 | 0.08 | 0.01 | 0.20 | 0.63 | `cross_mean(cs_regres(day_quantile_q25(Close), LogFloatCap), 20)` |
| slot b seed 7 | 过 | 0.16 | `ts_cov(cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_c` | 0.25 | 0.26 | 0.16 | 0.00 | 0.26 | 0.75 | `cs_regres(mul(day_quantile_q25(Close), day_distinct_ratio(Close)), LogFloatCap)` |
| slot b seed 8 | 过 | 0.04 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.03 | 0.03 | 0.03 | 0.08 | 0.02 | 0.00 | `mul(day_quantile_q25(Close), cross_delta(day_distinct_ratio(Close), 5))` |
| slot b seed 9 | 过 | 0.06 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.04 | 0.03 | 0.03 | 0.12 | 0.02 | 0.01 | `cross_delta(mul(day_quantile_q25(Close), day_distinct_ratio(Close)), 5)` |
| slot b seed 10 | 过 | 0.11 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.22 | 0.44 | 0.10 | 0.14 | 0.42 | 0.53 | `cs_regres(cs_regres(day_quantile_q25(Close), day_distinct_ratio(Close)), LogFloatCap)` |
| R 1 variant 1 | 过 | 0.78 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_` | 0.84 | 0.16 | 0.12 | 0.09 | 0.16 | 0.14 | `cs_first_high40(ts_argmin(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| R 1 variant 2 | 过 | 0.91 | `cs_first_high40(ts_argmin(ts_argmin(cross_quantile_q25(signe` | 0.79 | 0.12 | 0.11 | 0.14 | 0.13 | 0.06 | `cs_first_high40(ts_argmin(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 20), signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))))` |
