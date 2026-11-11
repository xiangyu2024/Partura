# 相关度表:种子 2023,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 7 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.03 | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q` | 0.05 | 0.01 | 0.03 | 0.16 | 0.01 | 0.05 | `day_wmean(Ret, log(log(abs_(Ret))))` |
| slot a seed 1 | 废品 | 0.38 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.34 | 0.05 | 0.12 | 0.13 | 0.07 | 0.01 | `cross_mean(is_gt(day_wmean(Ret, log(log(abs_(Ret)))), 0), 241)` |
| slot a seed 2 | 过 | 0.96 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.96 | 0.21 | 0.33 | 0.10 | 0.25 | 0.03 | `div(cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241), add(cross_stddev(day_wmean(Ret, log(log(abs_(Ret)))), 241), 0.000001))` |
| slot a seed 3 | 过 | 0.22 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.34 | 0.21 | 0.19 | 0.03 | 0.17 | 0.36 | `cross_regbeta(cs_mean(day_wmean(Ret, log(log(abs_(Ret))))), day_wmean(Ret, log(log(abs_(Ret)))), 241)` |
| slot a seed 4 | 过 | 0.80 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.81 | 0.27 | 0.15 | 0.06 | 0.29 | 0.16 | `cross_regalpha(cs_mean(day_wmean(Ret, log(log(abs_(Ret))))), day_wmean(Ret, log(log(abs_(Ret)))), 241)` |
| slot a seed 5 | 过 | 0.13 | `ts_stddev(day_quantile_q75(Volume), 10)` | 0.18 | 0.08 | 0.19 | 0.27 | 0.11 | 0.02 | `cross_mean(cross_regres(cs_mean(day_wmean(Ret, log(log(abs_(Ret))))), day_wmean(Ret, log(log(abs_(Ret)))), 60), 120)` |
| slot a seed 6 | 过 | 0.89 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.87 | 0.13 | 0.27 | 0.12 | 0.17 | 0.06 | `cross_ema(day_wmean(Ret, log(log(abs_(Ret)))), 120)` |
| slot a seed 7 | 过 | 0.89 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.91 | 0.06 | 0.10 | 0.05 | 0.10 | 0.02 | `sub(cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241), cross_mean(day_mean(Ret), 241))` |
| slot a seed 8 | 过 | 0.60 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.59 | 0.16 | 0.33 | 0.03 | 0.19 | 0.25 | `cross_mean(sub(day_wmean(Ret, log(log(abs_(Ret)))), day_wmean(Ret, log(abs_(Ret)))), 241)` |
| slot a seed 9 | 过 | 0.93 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.93 | 0.14 | 0.27 | 0.10 | 0.18 | 0.03 | `cross_mean(div(day_wmean(Ret, log(log(abs_(Ret)))), add(day_std(Ret), 0.000001)), 241)` |
| slot a seed 10 | 过 | 0.38 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.34 | 0.07 | 0.07 | 0.12 | 0.09 | 0.04 | `cross_med(day_wmean(Ret, log(log(abs_(Ret)))), 241)` |
| slot a seed 11 | 过 | 0.29 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.30 | 0.31 | 0.02 | 0.01 | 0.30 | 0.33 | `cross_mean(mul(day_wmean(Ret, log(log(abs_(Ret)))), is_lt(cs_mean(day_wmean(Ret, log(log(abs_(Ret))))), 0)), 241)` |
| slot a seed 12 | 过 | 0.04 | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` | 0.06 | 0.05 | 0.06 | 0.00 | 0.04 | 0.01 | `cross_autocorr(day_wmean(Ret, log(log(abs_(Ret)))), 241, 1)` |
| slot a seed 13 | 过 | 0.67 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.60 | 0.27 | 0.38 | 0.29 | 0.31 | 0.04 | `cross_decay_linear(day_wmean(Ret, log(log(abs_(Ret)))), 120)` |
| slot a seed 14 | 过 | 0.41 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.58 | 0.10 | 0.14 | 0.39 | 0.12 | 0.10 | `sub(cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241), cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 30))` |
| slot b seed 1 | 过 | 0.54 | `ts_max(day_quantile_q75(Volume), 40)` | 0.82 | 0.15 | 0.03 | 0.07 | 0.09 | 0.01 | `cross_mean(day_wmean(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), 241)` |
| slot b seed 2 | 过 | 0.55 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.52 | 0.15 | 0.41 | 0.04 | 0.20 | 0.09 | `cross_mean(day_wmean(Ret, is_gt(abs_(Ret), day_quantile(abs_(Ret), 0.9))), 241)` |
| slot b seed 3 | 过 | 0.53 | `ts_max(day_quantile_q75(Volume), 40)` | 0.67 | 0.03 | 0.26 | 0.05 | 0.09 | 0.05 | `sub(cross_mean(day_wmean(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), 241), cross_mean(day_wmean(Ret, is_gt(abs_(Ret), day_quantile(abs_(Ret), 0.9))), 241))` |
| slot b seed 4 | 过 | 0.27 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.37 | 0.09 | 0.12 | 0.09 | 0.05 | 0.22 | `cross_mean(day_signed_ratio(Ret, log(log(abs_(Ret)))), 241)` |
| slot b seed 5 | 过 | 0.25 | `ts_max(day_quantile_q75(Volume), 40)` | 0.49 | 0.25 | 0.12 | 0.07 | 0.22 | 0.04 | `cross_mean(day_signed_ratio(Ret, div(1, add(abs_(Ret), 0.0001))), 241)` |
| slot b seed 6 | 过 | 0.12 | `ts_max(day_quantile_q75(Volume), 40)` | 0.41 | 0.31 | 0.05 | 0.10 | 0.27 | 0.11 | `cross_mean(day_wmean(Ret, div(1, add(abs_(Ret), 0.0005))), 241)` |
| slot b seed 7 | 过 | 0.59 | `ts_max(day_quantile_q75(Volume), 40)` | 0.56 | 0.27 | 0.22 | 0.02 | 0.29 | 0.12 | `cross_mean(day_wmean(Ret, mul(is_gt(Ret, 0), is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)))), 241)` |
| slot b seed 8 | 过 | 0.60 | `ts_max(day_quantile_q75(Volume), 40)` | 0.64 | 0.15 | 0.13 | 0.04 | 0.18 | 0.11 | `cross_mean(day_wmean(Ret, mul(is_lt(Ret, 0), is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)))), 241)` |
| slot b seed 9 | 过 | 0.54 | `ts_max(day_quantile_q75(Volume), 40)` | 0.80 | 0.12 | 0.06 | 0.08 | 0.07 | 0.03 | `cross_mean(sub(day_wmean(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), day_mean(Ret)), 241)` |
| slot b seed 10 | 过 | 0.07 | `ts_max(day_quantile_q75(Volume), 40)` | 0.26 | 0.26 | 0.07 | 0.02 | 0.23 | 0.20 | `cross_corr(day_wmean(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), day_sum(Ret), 120)` |
| slot b seed 11 | 过 | 0.47 | `ts_max(day_quantile_q75(Volume), 40)` | 0.78 | 0.22 | 0.06 | 0.07 | 0.16 | 0.02 | `cross_mean(div(day_wmean(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), add(day_wmean(abs_(Ret), mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), 0.000001)), 241)` |
| slot b seed 12 | 过 | 0.47 | `ts_max(day_quantile_q75(Volume), 40)` | 0.79 | 0.22 | 0.07 | 0.07 | 0.17 | 0.02 | `cross_mean(day_signed_ratio(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.5)), is_gt(abs_(Ret), 0.000001))), 241)` |
| slot b seed 13 | 废品 | 0.43 | `ts_max(day_quantile_q75(Volume), 40)` | 0.60 | 0.07 | 0.12 | 0.05 | 0.04 | 0.00 | `cross_mean(day_wmean(Ret, mul(is_lt(abs_(Ret), day_quantile(abs_(Ret), 0.25)), is_gt(abs_(Ret), 0.000001))), 241)` |
| slot b seed 14 | 过 | 0.33 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.27 | 0.48 | 0.41 | 0.06 | 0.47 | 0.20 | `cross_mean(day_wmean(Ret, is_gt(Amt, day_quantile(Amt, 0.75))), 241)` |
| R 1 variant 1 | 过 | 0.97 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.98 | 0.16 | 0.31 | 0.08 | 0.20 | 0.10 | `cross_mean(day_wmean(Ret, is_gt(abs_(Ret), 0.000001)), 241)` |
| R 1 variant 2 | 过 | 0.94 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.94 | 0.15 | 0.18 | 0.09 | 0.19 | 0.09 | `cross_mean(day_wmean(Ret, log(log(log(abs_(Ret))))), 241)` |
| R 1 variant 3 | 过 | 0.87 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.84 | 0.12 | 0.23 | 0.06 | 0.16 | 0.05 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 360)` |
| R 1 variant 4 | 过 | 0.89 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.87 | 0.13 | 0.27 | 0.12 | 0.17 | 0.06 | `cross_ema(day_wmean(Ret, log(log(abs_(Ret)))), 120)` |
| R 1 variant 5 | 过 | 0.38 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.34 | 0.07 | 0.07 | 0.12 | 0.09 | 0.04 | `cross_med(day_wmean(Ret, log(log(abs_(Ret)))), 241)` |
| R 1 variant 6 | 过 | 0.93 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.93 | 0.14 | 0.27 | 0.10 | 0.18 | 0.03 | `cross_mean(div(day_wmean(Ret, log(log(abs_(Ret)))), add(day_std(Ret), 0.000001)), 241)` |
| R 1 variant 7 | 过 | 0.89 | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` | 0.91 | 0.06 | 0.10 | 0.05 | 0.10 | 0.02 | `sub(cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241), cross_mean(day_mean(Ret), 241))` |
