# 相关度表:种子 2073,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.97 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_` | 0.96 | 0.90 | 0.25 | 0.00 | 0.90 | 0.56 | `ts_std(day_close(Amt), 50)` |
| slot a seed 1 | 过 | 0.87 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.69 | 0.78 | 0.09 | 0.05 | 0.77 | 0.53 | `cross_max(ts_std(day_close(Amt), 50), 120)` |
| slot a seed 2 | 过 | 0.32 | `pow_2(day_max(pow_1_5(Vwap)))` | 0.65 | 0.38 | 0.06 | 0.08 | 0.33 | 0.35 | `div(ts_std(day_close(Amt), 50), cross_mean(day_sum(Amt), 50))` |
| slot a seed 3 | 过 | 0.41 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.36 | 0.40 | 0.26 | 0.06 | 0.40 | 0.16 | `div(ts_std(day_close(Amt), 50), ts_std(day_sum(Amt), 50))` |
| slot a seed 4 | 过 | 0.43 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_` | 0.34 | 0.28 | 0.34 | 0.15 | 0.31 | 0.07 | `cross_zscore(log(ts_std(day_close(Amt), 50)), 120)` |
| slot a seed 5 | 过 | 0.31 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_` | 0.30 | 0.16 | 0.32 | 0.11 | 0.19 | 0.01 | `sub(ts_std(day_close(Amt), 50), cross_mean(ts_std(day_close(Amt), 50), 120))` |
| slot a seed 6 | 过 | 0.16 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_` | 0.16 | 0.08 | 0.11 | 0.06 | 0.09 | 0.01 | `cross_regres(log(ts_std(day_sum(Amt), 50)), log(ts_std(day_close(Amt), 50)), 60)` |
| slot a seed 7 | 过 | 0.10 | `abs_(ts_std(ts_std(day_close(Amt), 40), 40))` | 0.05 | 0.04 | 0.11 | 0.07 | 0.06 | 0.01 | `cross_corr(ts_std(day_close(Amt), 50), day_sum(Amt), 60)` |
| slot a seed 8 | 废品 | 0.40 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_` | 0.30 | 0.26 | 0.33 | 0.17 | 0.29 | 0.07 | `ts_rank(ts_std(day_close(Amt), 50), 120)` |
| slot a seed 9 | 过 | 0.36 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.28 | 0.41 | 0.24 | 0.01 | 0.40 | 0.16 | `cross_mean(div(ts_std(day_close(Amt), 50), ts_std(day_sum(Amt), 50)), 20)` |
| slot a seed 10 | 过 | 0.15 | `abs_(ts_std(ts_std(day_close(Amt), 40), 40))` | 0.32 | 0.02 | 0.08 | 0.13 | 0.04 | 0.03 | `ts_skew(ts_std(day_close(Amt), 50), 60)` |
| slot b seed 1 | 过 | 0.31 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.37 | 0.29 | 0.15 | 0.04 | 0.25 | 0.34 | `cross_mean(div(day_close(Amt), day_sum(Amt)), 20)` |
| slot b seed 2 | 过 | 0.39 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.35 | 0.50 | 0.12 | 0.05 | 0.46 | 0.30 | `ts_std(div(day_close(Amt), day_sum(Amt)), 50)` |
| slot b seed 3 | 过 | 0.47 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.57 | 0.39 | 0.07 | 0.04 | 0.34 | 0.03 | `cross_mean(day_durbin_watson(Ret), 40)` |
| slot b seed 4 | 过 | 0.24 | `ts_max(day_corr(pow_1_5(Ret), Close), 60)` | 0.23 | 0.08 | 0.12 | 0.02 | 0.10 | 0.18 | `ts_std(day_durbin_watson(Ret), 60)` |
| slot b seed 5 | 过 | 0.78 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_` | 0.27 | 0.86 | 0.21 | 0.04 | 0.82 | 0.40 | `cross_mean(day_durbin_watson(Amt), 40)` |
| slot b seed 6 | 过 | 0.22 | `day_quantile_q75(cross_sum(pow_1_5(Volume), 3))` | 0.12 | 0.18 | 0.09 | 0.01 | 0.20 | 0.09 | `cross_corr(day_durbin_watson(Ret), div(day_close(Amt), day_sum(Amt)), 60)` |
| slot b seed 7 | 过 | 0.31 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.21 | 0.25 | 0.30 | 0.20 | 0.27 | 0.05 | `sub(cross_mean(day_durbin_watson(Ret), 20), cross_mean(day_durbin_watson(Ret), 120))` |
| slot b seed 8 | 过 | 0.27 | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` | 0.24 | 0.36 | 0.04 | 0.04 | 0.33 | 0.17 | `cross_max(ts_std(div(day_close(Amt), day_sum(Amt)), 50), 120)` |
| slot b seed 9 | 过 | 0.43 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.19 | 0.53 | 0.09 | 0.10 | 0.46 | 0.40 | `ts_std(day_durbin_watson(Amt), 50)` |
| slot b seed 10 | 过 | 0.10 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(` | 0.19 | 0.12 | 0.50 | 0.06 | 0.08 | 0.12 | `ts_std(abs_(day_close(Ret)), 50)` |
| slot b seed 11 | 过 | 0.45 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.38 | 0.41 | 0.15 | 0.01 | 0.36 | 0.34 | `cross_mean(mul(day_durbin_watson(Ret), div(day_close(Amt), day_sum(Amt))), 40)` |
| R 1 variant 1 | 过 | 0.95 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.89 | 0.76 | 0.20 | 0.05 | 0.75 | 0.39 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 90)` |
| R 1 variant 2 | 过 | 0.81 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.57 | 0.68 | 0.14 | 0.06 | 0.68 | 0.35 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 180)` |
| R 1 variant 3 | 过 | 0.74 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.45 | 0.65 | 0.11 | 0.07 | 0.63 | 0.33 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 240)` |
| R 1 variant 4 | 过 | 0.89 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.75 | 0.73 | 0.18 | 0.05 | 0.72 | 0.38 | `cross_max(mul(ts_std(day_durbin_watson(Close), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 120)` |
| R 1 variant 5 | 过 | 0.74 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.45 | 0.65 | 0.11 | 0.07 | 0.63 | 0.33 | `cross_max(mul(ts_std(day_durbin_watson(Close), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 240)` |
| R 1 variant 6 | 过 | 0.83 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.73 | 0.59 | 0.29 | 0.05 | 0.59 | 0.13 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_std(day_close(Amt), 50)), 120)` |
| R 1 variant 7 | 过 | 0.86 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.78 | 0.62 | 0.27 | 0.10 | 0.61 | 0.18 | `cross_mean(mul(ts_std(day_durbin_watson(Open), 40), ts_std(day_close(Amt), 50)), 120)` |
| R 1 variant 8 | 过 | 0.81 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(po` | 0.70 | 0.58 | 0.28 | 0.05 | 0.59 | 0.13 | `cross_max(mul(ts_std(day_durbin_watson(Open), 60), ts_std(day_close(Amt), 50)), 120)` |
| R 2 variant 1 | 过 | 0.55 | `ts_max(day_corr(pow_1_5(Ret), Close), 60)` | 0.50 | 0.09 | 0.10 | 0.02 | 0.10 | 0.04 | `ts_max(day_corr(pow_1_5(Ret), Close), 180)` |
| R 2 variant 2 | 过 | 0.46 | `ts_max(day_corr(pow_1_5(Ret), Close), 60)` | 0.41 | 0.06 | 0.08 | 0.02 | 0.07 | 0.05 | `ts_max(day_corr(pow_1_5(Ret), Close), 240)` |
| R 2 variant 3 | 过 | 0.38 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.40 | 0.31 | 0.06 | 0.06 | 0.26 | 0.07 | `ts_max(day_corr(pow_05(Ret), Close), 120)` |
| R 2 variant 4 | 过 | 0.38 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.36 | 0.31 | 0.07 | 0.05 | 0.25 | 0.12 | `ts_max(day_corr(signedpower(Ret), Close), 120)` |
| R 2 variant 5 | 过 | 0.16 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(` | 0.16 | 0.06 | 0.01 | 0.03 | 0.03 | 0.18 | `ts_max(day_corr(pow_1_5(Ret), Amt), 120)` |
| R 2 variant 6 | 过 | 0.25 | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` | 0.20 | 0.12 | 0.11 | 0.06 | 0.07 | 0.13 | `ts_mean(day_corr(pow_1_5(Ret), Close), 120)` |
