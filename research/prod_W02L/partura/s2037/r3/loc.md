# 定位:种子 2037,P 组,第 3 轮(只含 train / valid)

快照:prods2037M1_I0_open_search, prods2037M2_I0_open_search, prods2037M3_I0_open_search, prods2037Pr1a_Ea, prods2037Pr1b_Nb, prods2037Pr2a_Ea, prods2037Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.60 | +0.60 | +0.76 | +1 | 5 | prods2037Pr1a_Ea | `cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60)` |
| -0.28 | -0.28 | -0.12 | +1 | 5 | prods2037M1_I0_open_search | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 150)` |
| -0.86 | -0.86 | -0.81 | +1 | 5 | prods2037M1_I0_open_search | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 20, 5, False), 20)` |
| -1.09 | -1.09 | -0.93 | +1 | 5 | prods2037M1_I0_open_search | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 60)` |
| -1.53 | -1.53 | -1.45 | -1 | 20 | prods2037M2_I0_open_search | `cross_mean(sub(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt))), div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume)))), 20)` |
| -1.64 | -1.64 | -1.28 | -1 | 20 | prods2037M3_I0_open_search | `ts_sum(day_argmax(Volume), 50)` |
| -1.72 | -1.72 | -1.62 | -1 | 5 | prods2037M2_I0_open_search | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt))), 20)` |
| -1.76 | -1.76 | -1.68 | -1 | 5 | prods2037M2_I0_open_search | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume))), 20)` |
| -2.09 | -2.09 | -1.84 | +1 | 20 | prods2037M3_I0_open_search | `neg(ts_var(abs_(day_argmax(Ret)), 40))` |
| -2.32 | -2.06 | -2.32 | +1 | 5 | prods2037M3_I0_open_search | `cross_cov(day_var(Low), day_argmax(Close), 60)` |

## 共性:242 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.95 | 0.000 | 9 | -0.26 / -2.20 | `inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap)))` |
| +1.88 | 0.000 | 11 | -0.34 / -2.22 | `cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))` |
| +1.79 | 0.001 | 7 | -0.39 / -2.18 | `day_sum(Volume)` |
| +1.74 | 0.007 | 5 | -0.43 / -2.17 | `ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))), 40)` |
| +1.52 | 0.000 | 15 | -0.70 / -2.22 | `day_sum(Vwap)` |
| +1.51 | 0.000 | 121 | -1.38 / -2.88 | `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False)` |
| +1.49 | 0.000 | 78 | -1.12 / -2.61 | `day_sum(Amt)` |
| +1.45 | 0.007 | 7 | -0.73 / -2.17 | `day_sum(delete_open_close(Volume))` |
| +1.42 | 0.000 | 53 | -1.02 / -2.44 | `cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60)` |
| +1.13 | 0.011 | 10 | -1.05 / -2.18 | `energy_ratio_topm_minus_q(delete_open_close(High), 50, 5, False)` |
| +0.81 | 0.156 | 4 | -1.34 / -2.14 | `day_q_stat_std(Open)` |
| +0.64 | 0.108 | 9 | -1.52 / -2.15 | `log(day_sum(Amt))` |
| +0.60 | 0.197 | 5 | -1.54 / -2.14 | `day_std(Ret)` |
| +0.58 | 0.113 | 14 | -1.58 / -2.16 | `energy_ratio_n(Amt, 0.9, False)` |
| +0.44 | 0.247 | 7 | -1.70 / -2.14 | `day_sum(Ret)` |
| +0.12 | 0.424 | 4 | -2.01 / -2.13 | `day_gini(delete_open_close(Volume))` |
| -0.08 | 0.566 | 4 | -2.21 / -2.13 | `day_signed_ratio(High, Low)` |
| -0.24 | 0.685 | 7 | -2.36 / -2.12 | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt)))` |
| -0.27 | 0.706 | 7 | -2.39 / -2.12 | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume)))` |
| -0.31 | 0.750 | 8 | -2.43 / -2.12 | `div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))` |

## 拆解(26 次评估)

### head score -0.28:`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 150)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False)` | -4.09 | -4.06 | -4.09 | — | (子树本身) |
| swap | `Volume->Amt` | -0.24 | -0.24 | -0.16 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Amt), 50, 5, False), 150)` |
| window | `cross_stddev@150->75` | -0.65 | -0.41 | -0.65 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 75)` |
| window | `cross_stddev@150->300` | -0.70 | -0.70 | +0.24 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 300)` |

### head score -1.64:`ts_sum(day_argmax(Volume), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_argmax(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.59 | -1.59 | -1.25 | — | `ts_sum(day_argmax(Amt), 50)` |
| window | `ts_sum@50->25` | — | — | — | — | `ts_sum(day_argmax(Volume), 25)` |
| window | `ts_sum@50->100` | -1.36 | -1.36 | -0.93 | — | `ts_sum(day_argmax(Volume), 100)` |

### head score -1.72:`cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt)))` | -2.92 | -2.62 | -2.92 | — | (子树本身) |
| sufficiency | `div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))` | -3.42 | -3.03 | -3.42 | — | (子树本身) |
| sufficiency | `day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt)))` | -3.44 | -2.82 | -3.44 | — | (子树本身) |
| sufficiency | `day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))` | — | — | — | — | 门槛废品 |
| knockout | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt)))` | -3.47 | -2.59 | -3.47 | +1.75 | `cross_mean(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), 20)` |
| knockout | `div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))` | -0.89 | -0.89 | -0.55 | -0.83 | `cross_mean(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_mean(delete_open_close(Amt))), 20)` |
| swap | `Amt->Volume` | -1.76 | -1.76 | -1.67 | — | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume))), 20)` |
| window | `cross_mean@20->10` | -1.95 | -1.95 | -1.61 | — | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt))), 10)` |
| window | `cross_mean@20->40` | -2.25 | -1.83 | -2.25 | — | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt))), 40)` |

### head score -1.76:`cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume)))` | -2.94 | -2.62 | -2.94 | — | (子树本身) |
| sufficiency | `div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))` | -1.46 | -1.29 | -1.46 | — | (子树本身) |
| sufficiency | `day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume)))` | -1.57 | -1.40 | -1.57 | — | (子树本身) |
| sufficiency | `day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))` | — | — | — | — | 门槛废品 |
| knockout | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume)))` | -1.58 | -1.26 | -1.58 | -0.18 | `cross_mean(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), 20)` |
| knockout | `div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))` | -0.92 | -0.92 | -0.55 | -0.84 | `cross_mean(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_mean(delete_open_close(Volume))), 20)` |
| swap | `Volume->Amt` | -1.72 | -1.72 | -1.62 | — | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Amt))), 20)` |
| window | `cross_mean@20->10` | -1.96 | -1.96 | -1.77 | — | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume))), 10)` |
| window | `cross_mean@20->40` | -2.26 | -1.83 | -2.26 | — | `cross_mean(div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)))), day_mean(delete_open_close(Volume))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap)))` — enrichment,均值差 +1.95,p 0.000
2. `cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))` — enrichment,均值差 +1.88,p 0.000
3. `day_sum(Volume)` — enrichment,均值差 +1.79,p 0.001
4. `ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))), 40)` — enrichment,均值差 +1.74,p 0.007
5. `day_sum(Vwap)` — enrichment,均值差 +1.52,p 0.000
6. `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False)` — enrichment,均值差 +1.51,p 0.000
7. `day_sum(Amt)` — enrichment,均值差 +1.49,p 0.000
8. `day_sum(delete_open_close(Volume))` — enrichment,均值差 +1.45,p 0.007
9. `cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60)` — enrichment,均值差 +1.42,p 0.000
10. `energy_ratio_topm_minus_q(delete_open_close(High), 50, 5, False)` — enrichment,均值差 +1.13,p 0.011

## 本组之前各轮的任务

- `prods2037Pr1a_Ea`:核心 `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False)`;评分 77,过线 3,入 heads 1;采样计数 {'c05_no_core': 1610, 'c05_skeleton': 787}
  - score +0.60(train +0.60 valid +0.76):`cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60)`
  - score +0.56(train +0.56 valid +0.92):`cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(delete_open_close(Volume)), 60)`
  - score +0.51(train +0.51 valid +0.68):`cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), log(day_sum(Volume)), 60)`
  - score +0.45(train +0.45 valid +0.73):`cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 241)`
  - score +0.41(train +0.41 valid +0.80):`cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), log(day_sum(Amt)), 60)`
- `prods2037Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 14}
  - score -0.14(train -0.14 valid +0.20):`cross_corr(energy_ratio_topm_minus_q(delete_open_close(High), 50, 5, False), energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 60)`
  - score -0.17(train -0.17 valid +0.21):`cross_reg_tvalue(energy_ratio_topm_minus_q(delete_open_close(High), 50, 5, False), energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 60)`
  - score -0.19(train -0.08 valid -0.19):`cross_regalpha(energy_ratio_topm_minus_q(delete_open_close(High), 50, 5, False), energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 60)`
  - score -0.26(train +0.01 valid -0.26):`cross_regbeta(energy_ratio_topm_minus_q(delete_open_close(High), 50, 5, False), energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 60)`
  - score -0.26(train +0.01 valid -0.26):`cross_regbeta(energy_ratio_topm_minus_q(delete_open_close(delete_open_close(High)), 50, 5, False), energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 60)`
- `prods2037Pr2a_Ea`:核心 `cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60)`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 547, 'c05_no_core': 1253, 'mutation_refused': 4}
  - score +0.45(train +0.45 valid +0.64):`ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))), 40))), 40)`
  - score +0.41(train +0.41 valid +0.82):`ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))), 5))), 40)`
  - score +0.37(train +0.37 valid +0.55):`ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap))), 40)`
  - score +0.37(train +0.37 valid +0.55):`ts_quantile_q50(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap)))), 40)`
  - score +0.36(train +0.36 valid +0.72):`ts_quantile_q50(pow_05(inv(cs_last_low05(cross_corr(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), day_sum(Amt), 60), day_sum(Vwap)))), 40)`
- `prods2037Pr2b_Nb`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.08(train +0.51 valid -0.08):`cross_corr(cross_regbeta(energy_ratio_n(Amt, 0.9, False), day_sum(Amt), 5), day_sum(Amt), 241)`
  - score -0.12(train -0.12 valid -0.06):`cross_corr(energy_ratio_n(Volume, 0.9, False), day_sum(Volume), 241)`
  - score -0.15(train +0.36 valid -0.15):`cross_corr(energy_ratio_n(Amt, 0.9, False), day_sum(Amt), 241)`
  - score -0.22(train +0.02 valid -0.22):`cross_corr(energy_ratio_n(Amt, 0.9, False), day_sum(Amt), 60)`
  - score -0.35(train -0.35 valid -0.25):`cross_corr(cross_corr(energy_ratio_n(Amt, 0.9, False), day_sum(Amt), 5), day_sum(Amt), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.84(knockout div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))):`cross_mean(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Volume))), day_mean(delete_open_close(Volume))), 20)`
- 增益 +0.83(knockout div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_sum(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5))))):`cross_mean(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5)), delete_open_close(Amt))), day_mean(delete_open_close(Amt))), 20)`
