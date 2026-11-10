# 定位:种子 2029,P 组,第 2 轮(只含 train / valid)

快照:prods2029M1_I0_open_search, prods2029M2_I0_open_search, prods2029Pr1a_Ea, prods2029Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.35 | +1.44 | +1.35 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| +1.09 | +1.20 | +1.09 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| +1.00 | +1.09 | +1.00 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| +0.82 | +0.94 | +0.82 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| +0.66 | +0.81 | +0.66 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| +0.65 | +0.91 | +0.65 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| -0.03 | +0.15 | -0.03 | +1 | 0 | prods2029M1_I0_open_search | `ts_std(ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| -0.11 | -0.11 | +0.11 | +1 | 0 | prods2029M1_I0_open_search | `ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| -0.21 | -0.06 | -0.21 | +1 | 0 | prods2029M1_I0_open_search | `ts_max(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| -0.94 | -0.52 | -0.94 | +1 | 5 | prods2029M2_I0_open_search | `pow_1_5(ts_max(pow_2(ts_max(cs_rank(sub(ts_max(day_mean(Ret), 10), 5)), 30)), 30))` |
| -1.37 | -1.37 | +0.34 | +1 | 5 | prods2029M2_I0_open_search | `pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))` |

## 共性:115 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.69 | 0.007 | 4 | +0.02 / -1.67 | `log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` |
| +1.58 | 0.001 | 8 | -0.14 / -1.72 | `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| +1.42 | 0.000 | 22 | -0.46 / -1.88 | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| +1.41 | 0.000 | 51 | -0.82 / -2.24 | `day_mean(Amt)` |
| +1.39 | 0.000 | 50 | -0.82 / -2.22 | `ts_std(day_mean(Amt), 40)` |
| +1.32 | 0.000 | 45 | -0.81 / -2.13 | `ts_std(ts_std(day_mean(Amt), 40), 40)` |
| +1.22 | 0.051 | 5 | -0.44 / -1.66 | `log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))` |
| +1.22 | 0.002 | 10 | -0.50 / -1.72 | `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)` |
| +1.20 | 0.000 | 41 | -0.84 / -2.04 | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| +0.95 | 0.054 | 8 | -0.73 / -1.68 | `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` |
| +0.80 | 0.024 | 9 | -0.87 / -1.67 | `log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120))))` |
| +0.75 | 0.166 | 4 | -0.89 / -1.64 | `sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap)` |
| +0.53 | 0.073 | 12 | -1.14 / -1.67 | `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))` |
| +0.51 | 0.157 | 5 | -1.12 / -1.63 | `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))))` |
| -0.17 | 0.747 | 24 | -1.75 / -1.57 | `log(cross_semistd_neg(day_mean(Volume), 120))` |
| -0.29 | 0.874 | 26 | -1.83 / -1.55 | `cross_semistd_neg(day_mean(Volume), 120)` |
| -0.40 | 0.855 | 27 | -1.92 / -1.52 | `log(cross_semistd_pos(day_mean(Volume), 120))` |
| -0.47 | 0.868 | 8 | -2.04 / -1.58 | `log(day_mean(Volume))` |
| -0.57 | 0.970 | 32 | -2.02 / -1.45 | `cross_semistd_pos(day_mean(Volume), 120)` |
| -0.76 | 0.924 | 5 | -2.34 / -1.58 | `day_sum(Ret)` |

## 拆解(42 次评估)

### head score +1.35:`cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` | -0.44 | -0.44 | +0.55 | — | (子树本身) |
| sufficiency | `log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` | +0.00 | +0.00 | +0.16 | — | (子树本身) |
| sufficiency | `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` | +0.00 | +0.00 | +0.16 | — | (子树本身) |
| sufficiency | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` | -0.29 | -0.29 | -0.10 | — | (子树本身) |
| knockout | `sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` | -0.10 | -0.10 | -0.02 | +1.45 | `cs_last_low10(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| knockout | `log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` | +1.27 | +1.39 | +1.27 | +0.08 | `cs_last_low10(sub(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| knockout | `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` | +1.35 | +1.44 | +1.35 | +0.00 | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| swap | `Amt->Volume` | +0.68 | +0.68 | +1.14 | — | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Volume), 40), 40)), ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40))` |
| window | `ts_std@40->20` | +1.35 | +1.44 | +1.35 | — | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 20)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| window | `ts_std@40->80` | +1.35 | +1.44 | +1.35 | — | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 80)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |

### head score +1.09:`cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` | -0.43 | -0.43 | +0.55 | — | (子树本身) |
| sufficiency | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | -0.29 | -0.29 | -0.10 | — | (子树本身) |
| sufficiency | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` | -0.29 | -0.29 | -0.10 | — | (子树本身) |
| sufficiency | `ts_std(ts_std(day_mean(Amt), 40), 40)` | -0.43 | -0.43 | +0.56 | — | (子树本身) |
| knockout | `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` | -0.35 | -0.35 | -0.11 | +1.44 | `cs_last_low10(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | +0.78 | +0.81 | +0.78 | +0.31 | `cs_last_low10(sub(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` | +1.09 | +1.20 | +1.09 | +0.00 | `cs_last_low10(sub(log(ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| swap | `Amt->Volume` | +0.80 | +0.80 | +0.81 | — | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)), ts_std(ts_std(day_mean(Volume), 40), 40)), ts_std(ts_std(day_mean(Volume), 40), 40))` |
| window | `ts_std@40->20` | +1.09 | +1.20 | +1.09 | — | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 20)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| window | `ts_std@40->80` | +1.09 | +1.20 | +1.09 | — | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 80)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |

### head score +1.00:`cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap)` | -1.10 | -1.10 | -0.75 | — | (子树本身) |
| sufficiency | `log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))` | -1.60 | -1.60 | -1.05 | — | (子树本身) |
| sufficiency | `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` | -1.60 | -1.60 | -1.05 | — | (子树本身) |
| sufficiency | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | -0.29 | -0.29 | -0.10 | — | (子树本身) |
| knockout | `sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap)` | -1.19 | -1.19 | +0.44 | +2.19 | `cs_last_low10(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| knockout | `log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))` | +1.23 | +1.35 | +1.23 | -0.23 | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| knockout | `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` | +1.35 | +1.57 | +1.35 | -0.35 | `cs_last_low10(sub(log(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| knockout | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | -0.18 | +0.02 | -0.18 | +1.18 | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| swap | `Amt->Volume` | -0.09 | +0.23 | -0.09 | — | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)))` |
| window | `ts_std@40->20` | +0.56 | +0.56 | +0.75 | — | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 20)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| window | `ts_std@40->80` | +1.06 | +1.31 | +1.06 | — | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 80)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |

### head score +0.82:`cs_last_low10(sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)), LogFloatCap)` | -0.93 | -0.93 | -0.86 | — | (子树本身) |
| sufficiency | `log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40))` | -0.98 | -0.74 | -0.98 | — | (子树本身) |
| sufficiency | `ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)` | -0.97 | -0.74 | -0.97 | — | (子树本身) |
| sufficiency | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` | +0.26 | +0.26 | +0.27 | — | (子树本身) |
| knockout | `sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)), LogFloatCap)` | -0.14 | -0.14 | +0.66 | +0.97 | `cs_last_low10(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40))` | +1.24 | +1.45 | +1.24 | -0.42 | `cs_last_low10(sub(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)` | +1.35 | +1.59 | +1.35 | -0.53 | `cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` | +0.80 | +1.04 | +0.80 | +0.02 | `cs_last_low10(sub(log(ts_std(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| swap | `Amt->Volume` | +0.83 | +0.83 | +0.99 | — | `cs_last_low10(sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Volume), 40), 40)), 40)), LogFloatCap), ts_std(ts_std(day_mean(Volume), 40), 40))` |
| window | `ts_std@40->20` | +0.37 | +0.37 | +0.52 | — | `cs_last_low10(sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 20)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| window | `ts_std@40->80` | +0.83 | +1.11 | +0.83 | — | `cs_last_low10(sub(log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 80)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` — enrichment,均值差 +1.69,p 0.007
2. `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` — enrichment,均值差 +1.58,p 0.001
3. `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` — enrichment,均值差 +1.42,p 0.000
4. `day_mean(Amt)` — enrichment,均值差 +1.41,p 0.000
5. `ts_std(day_mean(Amt), 40)` — enrichment,均值差 +1.39,p 0.000
6. `ts_std(ts_std(day_mean(Amt), 40), 40)` — enrichment,均值差 +1.32,p 0.000
7. `log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))` — enrichment,均值差 +1.22,p 0.051
8. `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)` — enrichment,均值差 +1.22,p 0.002
9. `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` — enrichment,均值差 +1.20,p 0.000
10. `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` — enrichment,均值差 +0.95,p 0.054
11. `log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120))))` — enrichment,均值差 +0.80,p 0.024
12. `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))` — enrichment,均值差 +0.53,p 0.073

## 本组之前各轮的任务

- `prods2029Pr1a_Ea`:核心 `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)`;评分 99,过线 8,入 heads 6;采样计数 {'c05_skeleton': 1120, 'c05_no_core': 2155, 'mutation_refused': 2}
  - score +1.35(train +1.44 valid +1.35):`cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))`
  - score +1.35(train +1.44 valid +1.35):`cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))`
  - score +1.09(train +1.20 valid +1.09):`cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))`
  - score +1.09(train +1.20 valid +1.09):`cs_last_low10(sub(log(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))`
  - score +1.00(train +1.09 valid +1.00):`cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))`
- `prods2029Pr1b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {}
  - score +0.41(train +0.60 valid +0.41):`sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241)))))), log(cross_semistd_neg(day_mean(Volume), 241)))`
  - score -0.31(train +0.12 valid -0.31):`sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))))), log(cross_semistd_neg(day_mean(Volume), 120)))`
  - score -0.33(train -0.26 valid -0.33):`sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))`
  - score -0.39(train +0.15 valid -0.39):`sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))), log(sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))), log(cross_semistd_neg(day_mean(Volume), 120)))))`
  - score -0.42(train -0.01 valid -0.42):`sub(log(cross_semistd_pos(day_mean(Volume), 120)), sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))))), log(cross_semistd_neg(day_mean(Volume), 120))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.53(knockout ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40)):`cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))`
- 增益 +0.42(knockout log(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40))):`cs_last_low10(sub(ts_std(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), 40), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))`
- 增益 +0.23(knockout log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))):`cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))`
