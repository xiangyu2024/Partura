# 相关度表:种子 802,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 12 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.84 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.88 | 0.18 | 0.16 | 0.13 | 0.20 | 0.07 | `day_centroid(Volume)` |
| slot a seed 1 | 过 | 0.10 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.18 | 0.03 | 0.02 | 0.12 | 0.02 | 0.00 | `sub(day_centroid(Volume), day_centroid(Amt))` |
| slot a seed 2 | 过 | 0.05 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, ` | 0.24 | 0.04 | 0.15 | 0.62 | 0.06 | 0.03 | `cross_mean(sub(day_centroid(Volume), day_centroid(Amt)), 20)` |
| slot a seed 3 | 过 | 0.05 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.12 | 0.01 | 0.01 | 0.14 | 0.01 | 0.01 | `cs_regres(day_centroid(Volume), day_centroid(Amt))` |
| slot a seed 4 | 过 | 0.63 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.58 | 0.65 | 0.15 | 0.17 | 0.62 | 0.37 | `mul(day_centroid(Volume), day_gini(Volume))` |
| slot a seed 5 | 过 | 0.83 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.88 | 0.23 | 0.16 | 0.14 | 0.24 | 0.10 | `cs_regres(day_centroid(Volume), day_gini(Volume))` |
| slot a seed 6 | 过 | 0.29 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, ` | 0.49 | 0.88 | 0.18 | 0.09 | 0.84 | 0.46 | `cross_mean(mul(day_centroid(Volume), day_gini(Volume)), 20)` |
| slot a seed 7 | 过 | 0.48 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, ` | 0.77 | 0.48 | 0.42 | 0.20 | 0.51 | 0.13 | `cross_mean(day_centroid(Volume), 20)` |
| slot a seed 8 | 过 | 0.73 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.23 | 0.03 | 0.04 | 0.04 | 0.03 | 0.02 | `cross_zscore(day_centroid(Volume), 20)` |
| slot a seed 9 | 过 | 0.52 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.10 | 0.02 | 0.02 | 0.01 | 0.02 | 0.00 | `cross_delta(day_centroid(Volume), 5)` |
| slot a seed 10 | 过 | 0.02 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, ` | 0.07 | 0.03 | 0.00 | 0.05 | 0.02 | 0.02 | `mul(day_centroid(Volume), sign(ts_delay(day_sum(Ret), 1)))` |
| slot a seed 11 | 过 | 0.07 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.07 | 0.03 | 0.14 | 0.42 | 0.01 | 0.04 | `cross_mean(mul(day_centroid(Volume), sign(ts_delay(day_sum(Ret), 1))), 20)` |
| slot b seed 1 | 废品 | 0.02 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.03 | 0.03 | 0.01 | 0.01 | 0.02 | 0.01 | `cross_delta(LogFloatShares, 5)` |
| slot b seed 2 | 废品 | 0.02 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.02 | 0.04 | 0.02 | 0.01 | 0.04 | 0.02 | `cross_delta(LogFloatShares, 20)` |
| slot b seed 3 | 废品 | 0.01 | `ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)` | 0.02 | 0.04 | 0.02 | 0.01 | 0.02 | 0.00 | `sub(LogFloatShares, cross_quantile_q25(LogFloatShares, 241))` |
| slot b seed 4 | 过 | 0.01 | `ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)` | 0.02 | 0.03 | 0.00 | 0.00 | 0.02 | 0.00 | `cross_zscore(cross_delta(LogFloatShares, 20), 241)` |
| slot b seed 5 | 废品 | 0.06 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_` | 0.08 | 0.06 | 0.02 | 0.00 | 0.04 | 0.03 | `ts_argmax(abs(cross_delta(LogFloatShares, 1)), 120)` |
| slot b seed 6 | 废品 | 0.02 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.04 | 0.06 | 0.03 | 0.00 | 0.05 | 0.03 | `cross_mean(is_gt0(cross_delta(LogFloatShares, 1)), 20)` |
| slot b seed 7 | 废品 | 0.01 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_` | 0.02 | 0.05 | 0.02 | 0.01 | 0.04 | 0.02 | `cross_mean(cross_delta(LogFloatShares, 5), 60)` |
| slot b seed 8 | 过 | 0.02 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_` | 0.03 | 0.03 | 0.04 | 0.02 | 0.04 | 0.03 | `cs_regres(cross_delta(LogFloatShares, 20), LogFloatCap)` |
| slot b seed 9 | 过 | 0.02 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_` | 0.03 | 0.00 | 0.01 | 0.00 | 0.01 | 0.02 | `sub(cross_delta(LogFloatShares, 20), cross_mean(cross_delta(LogFloatShares, 20), 241))` |
| slot b seed 10 | 过 | 0.01 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.03 | 0.06 | 0.02 | 0.01 | 0.04 | 0.02 | `cross_zscore(LogFloatShares, 241)` |
| R 1 variant 1 | 过 | 0.81 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_` | 0.87 | 0.20 | 0.18 | 0.10 | 0.21 | 0.14 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| R 1 variant 2 | 过 | 0.97 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_` | 0.99 | 0.18 | 0.15 | 0.04 | 0.19 | 0.14 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 10), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| R 1 variant 3 | 过 | 0.79 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_` | 0.87 | 0.19 | 0.17 | 0.10 | 0.20 | 0.15 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 10), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| R 2 variant 1 | 过 | 0.66 | `ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)` | 0.81 | 0.24 | 0.25 | 0.06 | 0.27 | 0.04 | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 60)` |
| R 3 variant 1 | 过 | 0.88 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20` | 0.92 | 0.19 | 0.14 | 0.17 | 0.20 | 0.11 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 15))` |
