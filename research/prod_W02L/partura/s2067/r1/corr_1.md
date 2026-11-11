# 相关度表:种子 2067,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 1.00 | 0.33 | 0.20 | 0.19 | 0.33 | 0.07 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| slot a seed 1 | 过 | 0.55 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.77 | 0.64 | 0.25 | 0.03 | 0.61 | 0.12 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 60)` |
| slot a seed 2 | 过 | 0.56 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.76 | 0.64 | 0.21 | 0.02 | 0.61 | 0.13 | `cross_ema(day_corr(abs_(in_delay(Ret, 5)), Amt), 40)` |
| slot a seed 3 | 过 | 0.51 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.72 | 0.61 | 0.21 | 0.05 | 0.58 | 0.14 | `div(cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 60), cross_stddev(day_corr(abs_(in_delay(Ret, 5)), Amt), 60))` |
| slot a seed 4 | 过 | 0.40 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.48 | 0.40 | 0.19 | 0.03 | 0.41 | 0.02 | `cross_stddev(day_corr(abs_(in_delay(Ret, 5)), Amt), 60)` |
| slot a seed 5 | 过 | 0.30 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.20 | 0.24 | 0.44 | 0.33 | 0.28 | 0.05 | `sub(cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 20), cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 120))` |
| slot a seed 6 | 过 | 0.54 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.76 | 0.57 | 0.27 | 0.03 | 0.55 | 0.02 | `cs_bucket_zscore(cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 60), LogFloatCap)` |
| slot a seed 7 | 过 | 0.52 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.70 | 0.58 | 0.18 | 0.02 | 0.55 | 0.11 | `cross_ema(sign(day_corr(abs_(in_delay(Ret, 5)), Amt)), 30)` |
| slot a seed 8 | 过 | 0.51 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.72 | 0.58 | 0.20 | 0.04 | 0.55 | 0.11 | `cross_tail_mean_q25(day_corr(abs_(in_delay(Ret, 5)), Amt), 60)` |
| slot a seed 9 | 过 | 0.27 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.13 | 0.14 | 0.34 | 0.34 | 0.18 | 0.04 | `cross_mean(ts_regres(day_sum(Ret), day_corr(abs_(in_delay(Ret, 5)), Amt), 60), 20)` |
| slot a seed 10 | 过 | 0.42 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.47 | 0.61 | 0.32 | 0.04 | 0.61 | 0.15 | `cs_bucket_zscore(cross_ema(day_corr(abs_(in_delay(Ret, 5)), Amt), 40), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 11 | 过 | 0.18 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.07 | 0.14 | 0.20 | 0.25 | 0.16 | 0.00 | `cross_mean(mul(day_corr(abs_(in_delay(Ret, 5)), Amt), sign(day_sum(Ret))), 40)` |
| slot a seed 12 | 过 | 0.57 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.82 | 0.66 | 0.31 | 0.01 | 0.64 | 0.12 | `cross_mean(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), cs_mean(day_corr(abs_(in_delay(Ret, 5)), Amt))), 40)` |
| slot b seed 1 | 过 | 0.34 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.28 | 0.04 | 0.01 | 0.00 | 0.04 | 0.01 | `sub(day_corr(abs_(Ret), in_delay(Volume, 5)), day_corr(abs_(in_delay(Ret, 5)), Volume))` |
| slot b seed 2 | 过 | 0.22 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.35 | 0.17 | 0.06 | 0.07 | 0.14 | 0.04 | `cross_mean(sub(day_corr(abs_(Ret), in_delay(Volume, 5)), day_corr(abs_(in_delay(Ret, 5)), Volume)), 60)` |
| slot b seed 3 | 过 | 0.25 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.40 | 0.18 | 0.09 | 0.07 | 0.15 | 0.03 | `cross_ema(sub(day_corr(abs_(Ret), in_delay(Volume, 5)), day_corr(abs_(in_delay(Ret, 5)), Volume)), 40)` |
| slot b seed 4 | 过 | 0.34 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` | 0.28 | 0.04 | 0.01 | 0.00 | 0.03 | 0.01 | `sub(day_corr(abs_(Ret), in_delay(Amt, 5)), day_corr(abs_(in_delay(Ret, 5)), Amt))` |
| slot b seed 5 | 过 | 0.21 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.35 | 0.16 | 0.07 | 0.07 | 0.13 | 0.04 | `cross_mean(sub(day_corr(abs_(Ret), in_delay(Amt, 5)), day_corr(abs_(in_delay(Ret, 5)), Amt)), 60)` |
| slot b seed 6 | 过 | 0.19 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.19 | 0.03 | 0.03 | 0.11 | 0.03 | 0.01 | `sub(day_corr(Ret, in_delay(Volume, 5)), day_corr(in_delay(Ret, 5), Volume))` |
| slot b seed 7 | 过 | 0.29 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.22 | 0.33 | 0.28 | 0.12 | 0.34 | 0.06 | `cross_mean(sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(Volume, 5))), 60)` |
| slot b seed 8 | 过 | 0.09 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.23 | 0.02 | 0.14 | 0.05 | 0.04 | 0.03 | `cross_mean(div(sub(day_corr(abs_(Ret), in_delay(Volume, 5)), day_corr(abs_(in_delay(Ret, 5)), Volume)), add(abs_(day_corr(abs_(Ret), in_delay(Volume, 5))), abs_(day_corr(abs_(in_delay(Ret, 5)), Volume)))), 60)` |
| slot b seed 9 | 过 | 0.24 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.09 | 0.26 | 0.32 | 0.24 | 0.28 | 0.06 | `cross_mean(day_corr(in_delay(Ret, 5), in_delay(Volume, 5)), 60)` |
| slot b seed 10 | 过 | 0.26 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.41 | 0.21 | 0.00 | 0.07 | 0.18 | 0.01 | `cs_bucket_zscore(cross_mean(sub(day_corr(abs_(Ret), in_delay(Volume, 10)), day_corr(abs_(in_delay(Ret, 10)), Volume)), 60), LogFloatCap)` |
| slot b seed 11 | 过 | 0.32 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.17 | 0.36 | 0.36 | 0.28 | 0.38 | 0.09 | `cross_mean(sub(day_corr(Ret, in_delay(Amt, 1)), day_corr(in_delay(Ret, 1), Amt)), 40)` |
| slot b seed 12 | 过 | 0.22 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.36 | 0.17 | 0.06 | 0.07 | 0.13 | 0.06 | `cross_ema(sub(day_corr(abs_(Ret), in_delay(log(Amt), 5)), day_corr(abs_(in_delay(Ret, 5)), log(Amt))), 40)` |
| R 1 variant 1 | 过 | 0.56 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.79 | 0.26 | 0.15 | 0.13 | 0.26 | 0.08 | `day_corr(abs_(in_delay(Ret, 15)), Amt)` |
| R 1 variant 2 | 过 | 0.49 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.73 | 0.23 | 0.13 | 0.10 | 0.23 | 0.07 | `day_corr(abs_(in_delay(Ret, 20)), Amt)` |
| R 1 variant 3 | 过 | 0.38 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.58 | 0.19 | 0.10 | 0.07 | 0.18 | 0.07 | `day_corr(abs_(in_delay(Ret, 30)), Amt)` |
| R 1 variant 4 | 过 | 0.58 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.81 | 0.62 | 0.36 | 0.14 | 0.61 | 0.14 | `cross_mean(day_corr(abs_(in_delay(Ret, 10)), Amt), 20)` |
| R 1 variant 5 | 过 | 0.58 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.78 | 0.66 | 0.28 | 0.03 | 0.64 | 0.16 | `cross_ema(day_corr(abs_(in_delay(Ret, 10)), Amt), 20)` |
| R 2 variant 1 | 过 | 0.56 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.79 | 0.26 | 0.15 | 0.13 | 0.26 | 0.08 | `day_corr(abs_(in_delay(Ret, 15)), Volume)` |
| R 2 variant 2 | 过 | 0.49 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` | 0.73 | 0.23 | 0.13 | 0.11 | 0.23 | 0.07 | `day_corr(abs_(in_delay(Ret, 20)), Volume)` |
| R 2 variant 3 | 过 | 0.58 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.81 | 0.62 | 0.36 | 0.14 | 0.61 | 0.14 | `cross_mean(day_corr(abs_(in_delay(Ret, 10)), Volume), 20)` |
| R 2 variant 4 | 过 | 0.58 | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` | 0.78 | 0.66 | 0.28 | 0.04 | 0.64 | 0.16 | `cross_ema(day_corr(abs_(in_delay(Ret, 10)), Volume), 20)` |
