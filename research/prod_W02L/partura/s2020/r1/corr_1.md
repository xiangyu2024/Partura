# 相关度表:种子 2020,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.06 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.16 | 0.03 | 0.03 | 0.04 | 0.03 | 0.02 | `day_skew(Open)` |
| slot a seed 1 | 过 | 0.00 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.07 | 0.00 | 0.14 | 0.17 | 0.01 | 0.13 | `cross_ema(day_skew(Open), 40)` |
| slot a seed 2 | 过 | 0.07 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.11 | 0.03 | 0.04 | 0.02 | 0.03 | 0.00 | `cross_zscore(day_skew(Open), 120)` |
| slot a seed 3 | 过 | 0.06 | `pow_2(abs_(day_skew(Open)))` | 0.22 | 0.01 | 0.07 | 0.06 | 0.04 | 0.08 | `abs_(cross_ema(day_skew(Open), 30))` |
| slot a seed 4 | 过 | 0.11 | `pow_2(abs_(day_skew(Open)))` | 0.46 | 0.06 | 0.05 | 0.08 | 0.07 | 0.10 | `cross_tail_mean_q75(day_skew(Open), 60)` |
| slot a seed 5 | 过 | 0.10 | `pow_2(abs_(day_skew(Open)))` | 0.38 | 0.12 | 0.23 | 0.12 | 0.14 | 0.17 | `cross_tail_mean_q25(day_skew(Open), 60)` |
| slot a seed 6 | 过 | 0.01 | `pow_2(abs_(day_skew(Open)))` | 0.04 | 0.06 | 0.17 | 0.15 | 0.07 | 0.06 | `add(cross_tail_mean_q75(day_skew(Open), 60), cross_tail_mean_q25(day_skew(Open), 60))` |
| slot a seed 7 | 过 | 0.05 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.20 | 0.20 | 0.09 | 0.03 | 0.18 | 0.13 | `cross_corr(day_skew(Open), day_sum(Ret), 60)` |
| slot a seed 8 | 过 | 0.01 | `pow_2(abs_(day_skew(Open)))` | 0.01 | 0.14 | 0.12 | 0.02 | 0.16 | 0.02 | `cross_corr(day_skew(Open), sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 9 | 过 | 0.00 | `pow_2(abs_(day_skew(Open)))` | 0.01 | 0.06 | 0.06 | 0.01 | 0.07 | 0.02 | `cross_corr(cross_delay(day_skew(Open), 1), day_sum(Ret), 60)` |
| slot a seed 10 | 过 | 0.02 | `pow_2(abs_(day_skew(Open)))` | 0.03 | 0.18 | 0.10 | 0.10 | 0.17 | 0.17 | `cross_regbeta(day_skew(Open), log(day_sum(Amt)), 60)` |
| slot a seed 11 | 过 | 0.01 | `pow_2(abs_(day_skew(Open)))` | 0.02 | 0.04 | 0.03 | 0.01 | 0.02 | 0.06 | `cross_reg_fvalue(day_skew(Open), day_first(Amt), 60)` |
| slot a seed 12 | 过 | 0.02 | `pow_2(abs_(day_skew(Open)))` | 0.05 | 0.09 | 0.26 | 0.12 | 0.13 | 0.01 | `cross_corr(day_skew(Open), day_centroid(Amt), 60)` |
| slot a seed 13 | 过 | 0.00 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.04 | 0.01 | 0.02 | 0.21 | 0.01 | 0.02 | `cross_ema(cross_regres(day_skew(Amt), day_skew(Open), 60), 30)` |
| slot a seed 14 | 过 | 0.01 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.08 | 0.07 | 0.11 | 0.20 | 0.07 | 0.01 | `cs_bucket_zscore(cross_ema(day_skew(Open), 30), LogFloatCap)` |
| slot a seed 15 | 过 | 0.01 | `pow_2(abs_(day_skew(Open)))` | 0.05 | 0.18 | 0.06 | 0.16 | 0.16 | 0.01 | `cs_regres(cross_ema(day_skew(Open), 30), cross_ema(day_skew(Amt), 30))` |
| slot a seed 16 | 过 | 0.03 | `pow_2(abs_(day_skew(Open)))` | 0.12 | 0.01 | 0.00 | 0.12 | 0.01 | 0.01 | `mul(cross_ema(day_skew(Open), 20), sign(cross_mean(day_sum(Ret), 20)))` |
| slot b seed 1 | 过 | 0.10 | `pow_2(abs_(day_skew(Open)))` | 0.39 | 0.35 | 0.23 | 0.13 | 0.34 | 0.07 | `cross_mean(day_centroid(abs_(in_slice(Ret, 1, 240))), 20)` |
| slot b seed 2 | 过 | 0.10 | `pow_2(abs_(day_skew(Open)))` | 0.40 | 0.39 | 0.22 | 0.14 | 0.38 | 0.04 | `cs_bucket_zscore(cross_mean(day_centroid(abs_(in_slice(Ret, 1, 240))), 20), LogFloatCap)` |
| slot b seed 3 | 过 | 0.00 | `pow_2(abs_(day_skew(Open)))` | 0.09 | 0.24 | 0.19 | 0.15 | 0.22 | 0.03 | `cross_ema(sub(day_centroid(add(in_slice(Ret, 1, 240), abs_(in_slice(Ret, 1, 240)))), day_centroid(sub(abs_(in_slice(Ret, 1, 240)), in_slice(Ret, 1, 240)))), 30)` |
| slot b seed 4 | 过 | 0.02 | `pow_2(abs_(day_skew(Open)))` | 0.03 | 0.13 | 0.10 | 0.10 | 0.14 | 0.03 | `cross_corr(day_centroid(abs_(in_slice(Ret, 1, 240))), sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 5 | 过 | 0.00 | `pow_2(abs_(day_skew(Open)))` | 0.04 | 0.12 | 0.09 | 0.08 | 0.14 | 0.09 | `cross_corr(day_centroid(abs_(in_slice(Ret, 1, 240))), log(day_sum(Amt)), 60)` |
| slot b seed 6 | 过 | 0.02 | `pow_2(abs_(day_skew(Open)))` | 0.05 | 0.02 | 0.06 | 0.07 | 0.01 | 0.06 | `cross_regbeta(day_sum(Ret), day_centroid(abs_(in_slice(Ret, 1, 240))), 60)` |
| slot b seed 7 | 过 | 0.09 | `pow_2(abs_(day_skew(Open)))` | 0.19 | 0.25 | 0.26 | 0.21 | 0.28 | 0.10 | `sub(cross_ema(day_centroid(abs_(in_slice(Ret, 1, 240))), 10), cross_ema(day_centroid(abs_(in_slice(Ret, 1, 240))), 120))` |
| slot b seed 8 | 过 | 0.00 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.04 | 0.77 | 0.00 | 0.01 | 0.70 | 0.53 | `cross_mean(day_gini(abs_(in_slice(Ret, 1, 240))), 20)` |
| slot b seed 9 | 过 | 0.04 | `pow_2(abs_(day_skew(Open)))` | 0.25 | 0.20 | 0.27 | 0.07 | 0.23 | 0.19 | `cross_mean(sub(day_centroid(abs_(in_slice(Ret, 1, 240))), day_centroid(in_slice(Amt, 1, 240))), 30)` |
| slot b seed 10 | 过 | 0.05 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.13 | 0.25 | 0.22 | 0.03 | 0.28 | 0.09 | `cross_corr(day_centroid(abs_(in_slice(Ret, 1, 240))), day_centroid(in_slice(Amt, 1, 240)), 60)` |
| slot b seed 11 | 过 | 0.08 | `pow_2(abs_(day_skew(Open)))` | 0.34 | 0.04 | 0.07 | 0.01 | 0.02 | 0.16 | `cs_regres(cross_mean(day_centroid(abs_(in_slice(Ret, 1, 240))), 30), cross_mean(day_centroid(in_slice(Amt, 1, 240)), 30))` |
| slot b seed 12 | 过 | 0.06 | `pow_2(abs_(day_skew(Open)))` | 0.23 | 0.66 | 0.15 | 0.04 | 0.62 | 0.26 | `cross_mean(div(day_sum(in_slice(abs_(Ret), 211, 240)), day_sum(in_slice(abs_(Ret), 1, 240))), 30)` |
| slot b seed 13 | 过 | 0.10 | `pow_2(abs_(day_skew(Open)))` | 0.38 | 0.36 | 0.22 | 0.06 | 0.36 | 0.09 | `cross_mean(sub(div(day_sum(in_slice(abs_(Ret), 211, 240)), day_sum(in_slice(abs_(Ret), 1, 240))), div(day_sum(in_slice(abs_(Ret), 1, 30)), day_sum(in_slice(abs_(Ret), 1, 240)))), 30)` |
| slot b seed 14 | 过 | 0.07 | `pow_2(abs_(day_skew(Open)))` | 0.31 | 0.33 | 0.01 | 0.00 | 0.28 | 0.12 | `cross_ema(day_argmax(abs_(in_slice(Ret, 1, 240))), 40)` |
| slot b seed 15 | 过 | 0.01 | `pow_2(abs_(day_skew(Open)))` | 0.03 | 0.10 | 0.02 | 0.03 | 0.12 | 0.06 | `cross_reg_fvalue(day_centroid(abs_(in_slice(Ret, 1, 240))), day_first(Amt), 60)` |
| slot b seed 16 | 过 | 0.10 | `pow_2(abs_(day_skew(Open)))` | 0.37 | 0.30 | 0.01 | 0.00 | 0.28 | 0.07 | `cs_bucket_zscore(cross_ema(day_centroid(abs_(in_slice(Ret, 1, 240))), 20), cross_mean(day_std(Ret), 20))` |
| R 1 variant 1 | 过 | 0.23 | `pow_2(abs_(day_skew(Open)))` | 0.79 | 0.11 | 0.19 | 0.11 | 0.14 | 0.12 | `cross_mean(abs_(day_skew(Open)), 20)` |
| R 1 variant 2 | 过 | 0.15 | `pow_2(abs_(day_skew(Open)))` | 0.62 | 0.13 | 0.21 | 0.02 | 0.16 | 0.18 | `cross_mean(abs_(day_skew(Open)), 60)` |
| R 1 variant 3 | 过 | 0.14 | `pow_2(abs_(day_skew(Open)))` | 0.52 | 0.07 | 0.20 | 0.00 | 0.10 | 0.27 | `cross_ema(abs_(day_skew(Open)), 90)` |
| R 1 variant 4 | 过 | 0.96 | `pow_2(abs_(day_skew(Open)))` | 0.51 | 0.01 | 0.02 | 0.04 | 0.01 | 0.00 | `cross_zscore(abs_(day_skew(Open)), 120)` |
| R 1 variant 5 | 过 | 0.12 | `pow_2(abs_(day_skew(Open)))` | 0.49 | 0.10 | 0.22 | 0.03 | 0.14 | 0.19 | `cross_tail_mean_q75(abs_(day_skew(Open)), 60)` |
| R 1 variant 6 | 过 | 0.23 | `pow_2(abs_(day_skew(Open)))` | 0.43 | 0.14 | 0.14 | 0.11 | 0.16 | 0.06 | `div(cross_ema(abs_(day_skew(Open)), 20), cross_ema(abs_(day_skew(Open)), 120))` |
| R 1 variant 7 | 过 | 0.20 | `pow_2(abs_(day_skew(Open)))` | 0.64 | 0.26 | 0.20 | 0.05 | 0.28 | 0.02 | `cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 30), LogFloatCap)` |
| R 1 variant 8 | 过 | 0.19 | `pow_2(abs_(day_skew(Open)))` | 0.64 | 0.05 | 0.01 | 0.03 | 0.06 | 0.17 | `cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 30), cross_mean(day_std(Ret), 20))` |
| R 1 variant 9 | 过 | 0.18 | `pow_2(abs_(day_skew(Open)))` | 0.60 | 0.34 | 0.16 | 0.01 | 0.32 | 0.06 | `cs_regres(cross_ema(abs_(day_skew(Open)), 30), cross_ema(abs_(day_skew(Amt)), 30))` |
| R 1 variant 10 | 过 | 0.08 | `pow_2(abs_(day_skew(Open)))` | 0.30 | 0.08 | 0.18 | 0.03 | 0.10 | 0.19 | `cross_ema(abs_(day_skew(in_slice(Open, 121, 240))), 30)` |
| R 1 variant 11 | 过 | 0.12 | `pow_2(abs_(day_skew(Open)))` | 0.45 | 0.00 | 0.16 | 0.03 | 0.03 | 0.31 | `cross_ema(abs_(day_skew(in_slice(Open, 1, 120))), 30)` |
| R 1 variant 12 | 过 | 0.07 | `abs_(pow_2(abs_(day_skew(Open))))` | 0.24 | 0.06 | 0.01 | 0.00 | 0.06 | 0.16 | `cross_ema(sub(abs_(day_skew(in_slice(Open, 121, 240))), abs_(day_skew(in_slice(Open, 1, 120)))), 30)` |
| R 1 variant 13 | 过 | 0.08 | `pow_2(abs_(day_skew(Open)))` | 0.33 | 0.02 | 0.05 | 0.01 | 0.01 | 0.38 | `cross_ema(abs_(day_skew(sub(High, Low))), 30)` |
