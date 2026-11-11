# 相关度表:种子 2074,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.39 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.23 | 0.35 | 0.28 | 0.21 | 0.34 | 0.11 | `day_quantile_q25(Ret)` |
| slot a seed 1 | 过 | 0.46 | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` | 0.20 | 0.56 | 0.40 | 0.02 | 0.54 | 0.17 | `cross_mean(day_quantile_q25(Ret), 60)` |
| slot a seed 2 | 过 | 0.18 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.08 | 0.04 | 0.12 | 0.26 | 0.05 | 0.02 | `cross_zscore(day_quantile_q25(Ret), 120)` |
| slot a seed 3 | 过 | 0.32 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.32 | 0.25 | 0.10 | 0.01 | 0.22 | 0.16 | `div(day_quantile_q25(Ret), day_std(Ret))` |
| slot a seed 4 | 过 | 0.42 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.29 | 0.39 | 0.22 | 0.03 | 0.34 | 0.32 | `cross_mean(div(day_quantile_q25(Ret), day_std(Ret)), 60)` |
| slot a seed 5 | 过 | 0.21 | `pow_2(day_close(neg(Volume)))` | 0.18 | 0.09 | 0.10 | 0.01 | 0.10 | 0.25 | `cross_corr(day_quantile_q25(Ret), day_std(Amt), 60)` |
| slot a seed 6 | 过 | 0.27 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.34 | 0.12 | 0.07 | 0.07 | 0.09 | 0.09 | `cross_regbeta(day_quantile_q25(Ret), day_sum(Ret), 60)` |
| slot a seed 7 | 过 | 0.09 | `pow_2(day_close(neg(Volume)))` | 0.10 | 0.07 | 0.02 | 0.28 | 0.06 | 0.06 | `cross_regres(day_quantile_q25(Ret), day_std(Ret), 60)` |
| slot a seed 8 | 过 | 0.40 | `ts_max(day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5)` | 0.20 | 0.47 | 0.41 | 0.02 | 0.46 | 0.02 | `cs_bucket_zscore(cross_mean(day_quantile_q25(Ret), 60), LogFloatCap)` |
| slot a seed 9 | 过 | 0.23 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.23 | 0.02 | 0.21 | 0.01 | 0.02 | 0.28 | `cross_corr(day_quantile_q25(Ret), day_sum(Volume), 60)` |
| slot a seed 10 | 过 | 0.23 | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` | 0.07 | 0.17 | 0.31 | 0.24 | 0.19 | 0.04 | `sub(cross_mean(day_quantile_q25(Ret), 20), cross_mean(day_quantile_q25(Ret), 120))` |
| slot a seed 11 | 过 | 0.22 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.11 | 0.14 | 0.25 | 0.05 | 0.14 | 0.10 | `cross_regbeta(day_quantile_q25(Ret), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 12 | 过 | 0.40 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.26 | 0.47 | 0.04 | 0.03 | 0.43 | 0.28 | `cs_regres(cross_mean(day_quantile_q25(Ret), 60), cross_mean(day_std(Ret), 60))` |
| slot b seed 1 | 过 | 0.15 | `pow_2(day_close(neg(Volume)))` | 0.09 | 0.12 | 0.02 | 0.09 | 0.11 | 0.24 | `cross_mean(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), 60)` |
| slot b seed 2 | 过 | 0.13 | `pow_2(day_close(neg(Volume)))` | 0.11 | 0.06 | 0.01 | 0.20 | 0.05 | 0.17 | `cross_mean(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), 20)` |
| slot b seed 3 | 废品 | 0.17 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.15 | 0.03 | 0.02 | 0.03 | 0.03 | 0.05 | `cross_zscore(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), 120)` |
| slot b seed 4 | 过 | 0.17 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.14 | 0.11 | 0.09 | 0.09 | 0.10 | 0.18 | `cross_mean(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), day_std(Ret)), 60)` |
| slot b seed 5 | 过 | 0.07 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.09 | 0.01 | 0.03 | 0.07 | 0.01 | 0.03 | `cs_bucket_zscore(cross_mean(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), 60), LogFloatCap)` |
| slot b seed 6 | 过 | 0.23 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.28 | 0.17 | 0.19 | 0.04 | 0.15 | 0.19 | `cross_corr(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), day_sum(Ret), 60)` |
| slot b seed 7 | 废品 | 0.08 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.05 | 0.02 | 0.04 | 0.10 | 0.02 | 0.02 | `cross_regres(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), day_sum(Ret), 60)` |
| slot b seed 8 | 过 | 0.13 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.15 | 0.05 | 0.13 | 0.09 | 0.03 | 0.22 | `sub(cross_mean(day_quantile_q75(Ret), 60), cross_mean(neg(day_quantile_q25(Ret)), 60))` |
| slot b seed 9 | 过 | 0.13 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.15 | 0.05 | 0.13 | 0.09 | 0.03 | 0.22 | `cross_mean(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), 60)` |
| slot b seed 10 | 过 | 0.21 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.17 | 0.13 | 0.29 | 0.01 | 0.15 | 0.13 | `cross_regbeta(day_quantile_q75(Ret), day_quantile_q25(Ret), 60)` |
| slot b seed 11 | 过 | 0.20 | `pow_2(day_close(neg(Volume)))` | 0.15 | 0.15 | 0.07 | 0.11 | 0.15 | 0.16 | `cs_regres(cross_mean(div(add(day_quantile_q75(Ret), day_quantile_q25(Ret)), sub(day_quantile_q75(Ret), day_quantile_q25(Ret))), 60), cross_mean(day_skew(Ret), 60))` |
