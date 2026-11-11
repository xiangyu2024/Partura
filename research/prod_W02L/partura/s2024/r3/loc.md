# 定位:种子 2024,P 组,第 3 轮(只含 train / valid)

快照:prods2024M1_I0_open_search, prods2024M2_I0_open_search, prods2024M3_I0_open_search, prods2024Pr1a_Ea, prods2024Pr1b_Nb, prods2024Pr2a_Ea;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.78 | -1.78 | -1.33 | +1 | 5 | prods2024M2_I0_open_search | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` |
| -1.79 | -1.79 | -1.39 | +1 | 5 | prods2024M2_I0_open_search | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| -1.81 | -1.81 | -1.45 | +1 | 5 | prods2024M2_I0_open_search | `ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |
| -2.05 | -2.05 | -1.80 | -1 | 20 | prods2024M1_I0_open_search | `abs_(ts_pearson(day_quantile_q75(Ret), 10))` |
| -2.28 | -2.28 | -1.28 | +1 | 5 | prods2024M3_I0_open_search | `ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 20)` |
| -2.38 | -2.27 | -2.38 | +1 | 5 | prods2024M3_I0_open_search | `ts_stddev(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 20)` |
| -2.52 | -2.52 | -1.26 | +1 | 5 | prods2024M3_I0_open_search | `ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 20)` |
| -2.89 | -2.89 | -2.89 | +1 | 20 | prods2024M1_I0_open_search | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), ts_pearson(day_quantile_q75(Ret), 5))` |
| -3.42 | -2.86 | -3.42 | -1 | 20 | prods2024M1_I0_open_search | `div(cross_mean(day_last(Volume), 40), cross_mean(day_sum(Volume), 40))` |

## 共性:239 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.88 | 0.001 | 5 | -0.62 / -2.49 | `day_first(Open)` |
| +1.71 | 0.000 | 21 | -0.89 / -2.61 | `cs_demean(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))))` |
| +1.71 | 0.001 | 7 | -0.79 / -2.51 | `day_topw_mean(High, Close)` |
| +1.66 | 0.000 | 8 | -0.85 / -2.51 | `cross_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)` |
| +1.65 | 0.002 | 6 | -0.85 / -2.50 | `cs_last_low10(day_topw_mean(High, Close), day_autocorr_n1(Amt))` |
| +1.52 | 0.000 | 11 | -1.00 / -2.52 | `day_autocorr_n1(Amt)` |
| +1.51 | 0.003 | 4 | -0.97 / -2.48 | `ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20)` |
| +1.02 | 0.000 | 16 | -1.50 / -2.52 | `day_close(Amt)` |
| +0.85 | 0.018 | 8 | -1.63 / -2.48 | `cross_mean(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)` |
| +0.64 | 0.000 | 66 | -1.99 / -2.63 | `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` |
| +0.64 | 0.007 | 10 | -1.84 / -2.48 | `signedpower(day_close(Amt))` |
| +0.59 | 0.065 | 4 | -1.88 / -2.46 | `cross_stddev(cross_zscore(day_sum(Volume), 60), 20)` |
| +0.57 | 0.017 | 7 | -1.90 / -2.47 | `ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20)` |
| +0.29 | 0.187 | 6 | -2.17 / -2.46 | `day_q_stat_std(High)` |
| +0.24 | 0.215 | 5 | -2.22 / -2.46 | `div(cross_stddev(cs_mean(day_quantile_q75(Vwap)), 20), cs_mean(cross_stddev(day_quantile_q75(Ret), 20)))` |
| +0.19 | 0.247 | 7 | -2.27 / -2.46 | `day_quantile_q75(Vwap)` |
| +0.19 | 0.247 | 7 | -2.27 / -2.46 | `cs_mean(day_quantile_q75(Vwap))` |
| +0.19 | 0.247 | 7 | -2.27 / -2.46 | `cross_stddev(cs_mean(day_quantile_q75(Vwap)), 20)` |
| +0.17 | 0.205 | 19 | -2.30 / -2.47 | `cross_zscore(day_sum(Volume), 60)` |
| +0.17 | 0.332 | 6 | -2.29 / -2.46 | `day_q_stat_std(in_slice(Ret, 11, 230))` |

## 拆解(33 次评估)

### head score -2.28:`ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)))` | -2.83 | -2.83 | -2.32 | — | (子树本身) |
| sufficiency | `day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1))` | -4.14 | -3.83 | -4.14 | — | (子树本身) |
| sufficiency | `add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))` | -4.58 | -4.26 | -4.58 | — | (子树本身) |
| sufficiency | `create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)` | — | — | — | — | 门槛废品 |
| knockout | `div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)))` | -2.42 | -2.27 | -2.42 | +0.14 | `ts_stddev(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 20)` |
| knockout | `add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))` | -2.16 | -2.16 | -1.18 | -0.12 | `ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), day_mean(abs_(in_slice(Ret, 11, 240)))), 20)` |
| knockout | `create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)` | -2.16 | -2.16 | -1.18 | -0.12 | `ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), day_mean(abs_(in_slice(Ret, 11, 240))))), 20)` |
| swap | `Volume->Amt` | -2.21 | -2.21 | -1.32 | — | `ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Amt, 11, 240), add(in_mean_full(in_slice(Amt, 11, 240)), in_stddev_full(in_slice(Amt, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 20)` |
| window | `ts_stddev@20->10` | -2.78 | -2.78 | -1.83 | — | `ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 10)` |
| window | `ts_stddev@20->40` | -2.29 | -2.29 | -1.86 | — | `ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 40)` |

### head score -2.38:`ts_stddev(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1))` | -4.14 | -3.83 | -4.14 | — | (子树本身) |
| swap | `Volume->Amt` | -2.51 | -2.28 | -2.51 | — | `ts_stddev(day_mean(in_sustain_stddev(is_gt(in_slice(Amt, 11, 240), add(in_mean_full(in_slice(Amt, 11, 240)), in_stddev_full(in_slice(Amt, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 20)` |
| window | `ts_stddev@20->10` | -2.71 | -2.50 | -2.71 | — | `ts_stddev(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 10)` |
| window | `ts_stddev@20->40` | -2.62 | -1.56 | -2.62 | — | `ts_stddev(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 40)` |

### head score -2.52:`ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)))` | -2.83 | -2.83 | -2.32 | — | (子树本身) |
| sufficiency | `day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1))` | -4.14 | -3.83 | -4.14 | — | (子树本身) |
| sufficiency | `add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))` | -4.58 | -4.26 | -4.58 | — | (子树本身) |
| sufficiency | `create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)` | — | — | — | — | 门槛废品 |
| knockout | `div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)))` | -3.70 | -3.35 | -3.70 | +1.18 | `ts_mean(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), 20)` |
| knockout | `add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))` | -2.00 | -2.00 | -1.20 | -0.52 | `ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), day_mean(abs_(in_slice(Ret, 11, 240)))), 20)` |
| knockout | `create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)` | -2.00 | -2.00 | -1.20 | -0.52 | `ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), day_mean(abs_(in_slice(Ret, 11, 240))))), 20)` |
| swap | `Volume->Amt` | -2.59 | -2.59 | -1.85 | — | `ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Amt, 11, 240), add(in_mean_full(in_slice(Amt, 11, 240)), in_stddev_full(in_slice(Amt, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 20)` |
| window | `ts_mean@20->10` | -2.34 | -2.34 | -1.93 | — | `ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 10)` |
| window | `ts_mean@20->40` | -2.65 | -2.65 | -2.27 | — | `ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 40)` |

### head score -3.42:`div(cross_mean(day_last(Volume), 40), cross_mean(day_sum(Volume), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_last(Volume), 40)` | -1.58 | -1.02 | -1.58 | — | (子树本身) |
| sufficiency | `cross_mean(day_sum(Volume), 40)` | -1.45 | -1.15 | -1.45 | — | (子树本身) |
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `cross_mean(day_last(Volume), 40)` | -2.84 | -2.84 | -2.81 | -0.59 | `div(day_last(Volume), cross_mean(day_sum(Volume), 40))` |
| knockout | `cross_mean(day_sum(Volume), 40)` | -1.89 | -1.79 | -1.89 | -1.54 | `div(cross_mean(day_last(Volume), 40), day_sum(Volume))` |
| swap | `Volume->Amt` | -3.28 | -2.83 | -3.28 | — | `div(cross_mean(day_last(Amt), 40), cross_mean(day_sum(Amt), 40))` |
| window | `cross_mean@40->20` | -3.21 | -3.21 | -2.33 | — | `div(cross_mean(day_last(Volume), 20), cross_mean(day_sum(Volume), 40))` |
| window | `cross_mean@40->80` | -2.78 | -2.34 | -2.78 | — | `div(cross_mean(day_last(Volume), 80), cross_mean(day_sum(Volume), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_first(Open)` — enrichment,均值差 +1.88,p 0.001
2. `cs_demean(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))))` — enrichment,均值差 +1.71,p 0.000
3. `day_topw_mean(High, Close)` — enrichment,均值差 +1.71,p 0.001
4. `cross_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)` — enrichment,均值差 +1.66,p 0.000
5. `cs_last_low10(day_topw_mean(High, Close), day_autocorr_n1(Amt))` — enrichment,均值差 +1.65,p 0.002
6. `day_autocorr_n1(Amt)` — enrichment,均值差 +1.52,p 0.000
7. `ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20)` — enrichment,均值差 +1.51,p 0.003
8. `day_close(Amt)` — enrichment,均值差 +1.02,p 0.000
9. `cross_mean(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)` — enrichment,均值差 +0.85,p 0.018
10. `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` — enrichment,均值差 +0.64,p 0.000
11. `signedpower(day_close(Amt))` — enrichment,均值差 +0.64,p 0.007
12. `cross_stddev(cross_zscore(day_sum(Volume), 60), 20)` — enrichment,均值差 +0.59,p 0.065
13. `ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20)` — enrichment,均值差 +0.57,p 0.017

## 本组之前各轮的任务

- `prods2024Pr1a_Ea`:核心 `day_quantile_q75(Ret)`;评分 79,过线 0,入 heads 0;采样计数 {'c05_skeleton': 416, 'c05_no_core': 807}
  - score -0.43(train -0.31 valid -0.43):`ts_reg_fvalue(ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20), day_close(Amt), 20)`
  - score -0.53(train -0.53 valid -0.52):`ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20)`
  - score -0.61(train -0.49 valid -0.61):`ts_reg_fvalue(ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20), signedpower(day_close(Amt)), 20)`
  - score -0.80(train -0.56 valid -0.80):`ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20)`
  - score -0.97(train -0.94 valid -0.97):`ts_reg_fvalue(ts_reg_fvalue(ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20), day_close(Amt), 20), day_close(Amt), 20)`
- `prods2024Pr1b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.91(train -0.52 valid -0.91):`cross_regalpha(day_sum(Close), day_close(Ret), 30)`
  - score -1.10(train -1.10 valid -0.89):`cross_regalpha(day_sum(Volume), day_close(Ret), 30)`
  - score -1.46(train -1.46 valid -1.39):`cs_flip_by_state(cross_corr(cross_zscore(day_sum(Volume), 60), cs_mean(cross_zscore(day_sum(Volume), 60)), 60), div(cross_stddev(cs_mean(day_quantile_q75(Ret)), 20), cs_mean(day_quantile_q75(Ret))))`
  - score -1.55(train -1.55 valid -1.06):`cs_flip_by_state(cross_corr(cross_zscore(day_sum(Volume), 60), cs_mean(cross_zscore(day_sum(Volume), 60)), 60), div(cross_stddev(cs_mean(day_quantile_q75(Ret)), 20), cs_mean(cross_stddev(day_quantile_q75(Ret), 20))))`
  - score -1.55(train -1.55 valid -1.20):`cross_regalpha(day_q_stat_std(High), day_close(Ret), 241)`
- `prods2024Pr2a_Ea`:核心 `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))`;评分 86,过线 0,入 heads 0;采样计数 {'c05_no_core': 546, 'c05_skeleton': 261}
  - score -0.12(train -0.12 valid -0.09):`div(cross_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60), cross_decay_linear(day_q_stat_std(in_slice(Volume, 11, 230)), 60))`
  - score -0.12(train -0.12 valid -0.09):`div(cross_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60), cross_decay_linear(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))))), 60))`
  - score -0.12(train -0.00 valid -0.12):`mul(ts_delay(cs_last_low10(day_topw_mean(High, Close), day_autocorr_n1(Amt)), 10), cs_demean(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))))`
  - score -0.12(train -0.11 valid -0.12):`div(cross_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60), cross_decay_linear(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60))`
  - score -0.13(train -0.09 valid -0.13):`div(cross_stddev(day_q_stat_std(in_slice(Volume, 11, 230)), 60), cross_decay_linear(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.54(knockout cross_mean(day_sum(Volume), 40)):`div(cross_mean(day_last(Volume), 40), day_sum(Volume))`
- 增益 +0.64(window cross_mean@40->80):`div(cross_mean(day_last(Volume), 80), cross_mean(day_sum(Volume), 40))`
- 增益 +0.52(knockout add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))):`ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), day_mean(abs_(in_slice(Ret, 11, 240)))), 20)`
- 增益 +0.52(knockout create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)):`ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), day_mean(abs_(in_slice(Ret, 11, 240))))), 20)`
- 增益 +0.18(window ts_mean@20->10):`ts_mean(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))), 10)`
- 增益 +0.14(swap Volume->Amt):`div(cross_mean(day_last(Amt), 40), cross_mean(day_sum(Amt), 40))`
- 增益 +0.12(knockout add(day_mean(abs_(in_slice(Ret, 11, 240))), create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06))):`ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), day_mean(abs_(in_slice(Ret, 11, 240)))), 20)`
- 增益 +0.12(knockout create_like(day_mean(abs_(in_slice(Ret, 11, 240))), 1e-06)):`ts_stddev(div(day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volume, 11, 240)), in_stddev_full(in_slice(Volume, 11, 240)))), in_slice(Ret, 11, 240), 5, 1, 1)), add(day_mean(abs_(in_slice(Ret, 11, 240))), day_mean(abs_(in_slice(Ret, 11, 240))))), 20)`
