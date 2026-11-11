# 定位:种子 2029,P 组,第 3 轮(只含 train / valid)

快照:prods2029M1_I0_open_search, prods2029M2_I0_open_search, prods2029M3_I0_open_search, prods2029Pr1a_Ea, prods2029Pr1b_Nb, prods2029Pr2a_Ea;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(14 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.35 | +1.44 | +1.35 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| +1.35 | +1.59 | +1.35 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| +1.23 | +1.35 | +1.23 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| +1.09 | +1.20 | +1.09 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| +0.66 | +0.81 | +0.66 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| +0.65 | +0.91 | +0.65 | -1 | 0 | prods2029Pr1a_Ea | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| -0.03 | +0.15 | -0.03 | +1 | 0 | prods2029M1_I0_open_search | `ts_std(ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| -0.11 | -0.11 | +0.11 | +1 | 0 | prods2029M1_I0_open_search | `ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| -0.21 | -0.06 | -0.21 | +1 | 0 | prods2029M1_I0_open_search | `ts_max(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| -0.57 | -0.57 | -0.51 | +1 | 5 | prods2029M3_I0_open_search | `pow_2(ts_max(pow_2(cs_demean(sub(pow_2(ts_max(day_mean(Ret), 30)), day_corr(Amt, Close)))), 30))` |
| -0.79 | -0.04 | -0.79 | +1 | 5 | prods2029M3_I0_open_search | `pow_2(ts_max(ts_max(ts_max(ts_max(pow_2(ts_max(day_mean(Ret), 10)), 20), 50), 20), 30))` |
| -0.89 | -0.19 | -0.89 | +1 | 5 | prods2029M3_I0_open_search | `pow_1_5(ts_max(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(day_mean(Ret), 10)), 20), 30)), 50), 30))` |
| -0.94 | -0.52 | -0.94 | +1 | 5 | prods2029M2_I0_open_search | `pow_1_5(ts_max(pow_2(ts_max(cs_rank(sub(ts_max(day_mean(Ret), 10), 5)), 30)), 30))` |
| -1.37 | -1.37 | +0.34 | +1 | 5 | prods2029M2_I0_open_search | `pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))` |

## 共性:188 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.74 | 0.005 | 4 | +0.02 / -1.72 | `log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` |
| +1.61 | 0.001 | 8 | -0.14 / -1.75 | `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| +1.39 | 0.000 | 22 | -0.46 / -1.85 | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| +1.38 | 0.002 | 6 | -0.35 / -1.73 | `log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241))))` |
| +1.28 | 0.048 | 5 | -0.44 / -1.72 | `log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))` |
| +1.26 | 0.001 | 10 | -0.50 / -1.75 | `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)` |
| +1.21 | 0.000 | 53 | -0.82 / -2.03 | `day_mean(Amt)` |
| +1.17 | 0.000 | 50 | -0.82 / -2.00 | `ts_std(day_mean(Amt), 40)` |
| +1.16 | 0.000 | 45 | -0.81 / -1.96 | `ts_std(ts_std(day_mean(Amt), 40), 40)` |
| +1.08 | 0.000 | 41 | -0.84 / -1.92 | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| +1.00 | 0.044 | 8 | -0.73 / -1.73 | `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` |
| +0.85 | 0.012 | 9 | -0.87 / -1.73 | `log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120))))` |
| +0.81 | 0.159 | 4 | -0.89 / -1.70 | `sub(log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)), LogFloatCap)` |
| +0.69 | 0.037 | 10 | -1.04 / -1.72 | `cross_scale(cross_semistd_pos(day_mean(Volume), 120), 60)` |
| +0.59 | 0.019 | 21 | -1.16 / -1.75 | `log(cross_semistd_neg(day_mean(Volume), 241))` |
| +0.59 | 0.019 | 21 | -1.16 / -1.75 | `cross_semistd_neg(day_mean(Volume), 241)` |
| +0.58 | 0.166 | 4 | -1.11 / -1.70 | `pow_2(ts_max(day_mean(Ret), 10))` |
| +0.58 | 0.120 | 5 | -1.12 / -1.70 | `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))))` |
| +0.57 | 0.040 | 16 | -1.17 / -1.73 | `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241)))` |
| +0.54 | 0.054 | 13 | -1.19 / -1.72 | `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))` |

## 拆解(44 次评估)

### head score +1.35:`cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap)` | +0.28 | +0.29 | +0.28 | — | (子树本身) |
| sufficiency | `log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)))` | -0.06 | +0.15 | -0.06 | — | (子树本身) |
| sufficiency | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` | +0.26 | +0.26 | +0.27 | — | (子树本身) |
| sufficiency | `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)` | -0.40 | -0.28 | -0.40 | — | (子树本身) |
| knockout | `sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap)` | +0.30 | +0.30 | +0.36 | +1.05 | `cs_last_low10(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)))` | +1.32 | +1.45 | +1.32 | +0.03 | `cs_last_low10(sub(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` | +1.35 | +1.58 | +1.35 | -0.00 | `cs_last_low10(sub(log(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)` | +1.17 | +1.28 | +1.17 | +0.18 | `cs_last_low10(sub(log(cs_last_low10(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| swap | `Amt->Volume` | +0.67 | +1.23 | +0.67 | — | `cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)), LogFloatCap), ts_std(ts_std(day_mean(Volume), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Volume), 40), 40))` |
| window | `ts_std@40->20` | +1.24 | +1.41 | +1.24 | — | `cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 20)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| window | `ts_std@40->80` | +1.33 | +1.47 | +1.33 | — | `cs_last_low10(sub(log(cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 80)), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))), LogFloatCap), ts_std(ts_std(day_mean(Amt), 40), 40))` |

### head score +1.23:`cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap)` | -1.84 | -1.58 | -1.84 | — | (子树本身) |
| sufficiency | `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` | -1.60 | -1.60 | -1.05 | — | (子树本身) |
| sufficiency | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | -0.29 | -0.29 | -0.10 | — | (子树本身) |
| knockout | `sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap)` | -1.17 | -1.17 | +0.42 | +2.41 | `cs_last_low10(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| knockout | `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` | +0.09 | +0.09 | +0.12 | +1.14 | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| knockout | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | -0.09 | -0.09 | -0.02 | +1.33 | `cs_last_low10(sub(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| knockout | `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` | +1.23 | +1.33 | +1.23 | +0.01 | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` |
| swap | `Amt->Volume` | +0.58 | +1.04 | +0.58 | — | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40)))` |
| window | `ts_std@40->20` | +1.25 | +1.39 | +1.25 | — | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 20), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |
| window | `ts_std@40->80` | +1.28 | +1.33 | +1.28 | — | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 80), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))` |

### head score +0.66:`cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` | +0.00 | +0.00 | +0.17 | — | (子树本身) |
| sufficiency | `log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt)))))` | -1.91 | -1.91 | -1.57 | — | (子树本身) |
| sufficiency | `cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))` | -2.26 | -1.97 | -2.26 | — | (子树本身) |
| sufficiency | `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` | +0.00 | +0.00 | +0.16 | — | (子树本身) |
| knockout | `sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` | -2.01 | -2.01 | -0.92 | +2.68 | `cs_last_low10(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt)))))` | +0.67 | +0.81 | +0.67 | -0.01 | `cs_last_low10(sub(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt)))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))` | +0.67 | +0.81 | +0.67 | -0.01 | `cs_last_low10(sub(log(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30)), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| knockout | `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` | +0.90 | +1.00 | +0.90 | -0.23 | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| swap | `Vwap->Close` | +0.66 | +0.81 | +0.66 | — | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Close)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| swap | `Close->Vwap` | +0.67 | +0.81 | +0.67 | — | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Vwap, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| window | `ts_argmin@30->15` | +0.67 | +0.81 | +0.67 | — | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 15), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |
| window | `ts_argmin@30->60` | +0.67 | +0.81 | +0.67 | — | `cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 60), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))` |

### head score +0.65:`cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)), LogFloatCap)` | -1.60 | -1.60 | +0.06 | — | (子树本身) |
| sufficiency | `log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40))` | -2.26 | -2.26 | -2.01 | — | (子树本身) |
| sufficiency | `ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)` | -2.26 | -2.26 | -2.01 | — | (子树本身) |
| sufficiency | `log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40))` | -0.33 | -0.33 | -0.31 | — | (子树本身) |
| knockout | `sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)), LogFloatCap)` | -1.53 | -1.53 | -1.01 | +2.18 | `cs_last_low10(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| knockout | `log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40))` | +0.71 | +1.00 | +0.71 | -0.05 | `cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| knockout | `ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 40)` | +1.16 | +1.16 | +1.26 | -0.50 | `cs_last_low10(sub(log(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40))), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| knockout | `log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40))` | -0.96 | -0.46 | -0.96 | +1.61 | `cs_last_low10(sub(log(ts_std(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| swap | `Amt->Volume` | +0.09 | +0.09 | +0.47 | — | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40), 40), 40)), 40)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40), 40), 40)))` |
| window | `ts_std@40->20` | +0.50 | +0.56 | +0.50 | — | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 20)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |
| window | `ts_std@40->80` | +0.69 | +0.92 | +0.69 | — | `cs_last_low10(sub(log(ts_std(log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)), 80)), LogFloatCap), log(ts_std(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40), 40)))` |

## 机械核心卡(B0 按这个顺序取)

1. `log(ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40))` — enrichment,均值差 +1.74,p 0.005
2. `ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` — enrichment,均值差 +1.61,p 0.001
3. `log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40))` — enrichment,均值差 +1.39,p 0.000
4. `log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241))))` — enrichment,均值差 +1.38,p 0.002
5. `log(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40))` — enrichment,均值差 +1.28,p 0.048
6. `sub(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), LogFloatCap)` — enrichment,均值差 +1.26,p 0.001
7. `day_mean(Amt)` — enrichment,均值差 +1.21,p 0.000
8. `ts_std(day_mean(Amt), 40)` — enrichment,均值差 +1.17,p 0.000
9. `ts_std(ts_std(day_mean(Amt), 40), 40)` — enrichment,均值差 +1.16,p 0.000
10. `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` — enrichment,均值差 +1.08,p 0.000
11. `ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40)` — enrichment,均值差 +1.00,p 0.044
12. `log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120))))` — enrichment,均值差 +0.85,p 0.012
13. `cross_scale(cross_semistd_pos(day_mean(Volume), 120), 60)` — enrichment,均值差 +0.69,p 0.037
14. `log(cross_semistd_neg(day_mean(Volume), 241))` — enrichment,均值差 +0.59,p 0.019
15. `cross_semistd_neg(day_mean(Volume), 241)` — enrichment,均值差 +0.59,p 0.019
16. `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241)))` — enrichment,均值差 +0.57,p 0.040
17. `sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 120)))` — enrichment,均值差 +0.54,p 0.054

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
- `prods2029Pr2a_Ea`:核心 `cross_semistd_pos(day_mean(Volume), 120)`;评分 89,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 37, 'c05_no_core': 1577, 'c05_skeleton': 818, 'mutation_refused': 3}
  - score +0.02(train +0.54 valid +0.02):`cs_bucket_zscore(sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241)))), log(cross_semistd_neg(day_mean(Volume), 241))), LogFloatCap)`
  - score -0.11(train +0.62 valid -0.11):`cs_bucket_zscore(sub(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Amt), 241)))), log(cross_semistd_neg(day_mean(Amt), 241))), LogFloatCap)`
  - score -0.12(train +0.38 valid -0.12):`cs_bucket_zscore(div(log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241)))), log(cross_semistd_neg(day_mean(Volume), 241))), LogFloatCap)`
  - score -0.20(train -0.20 valid +0.05):`sub(cs_bucket_zscore(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241))), LogFloatCap), log(cross_semistd_neg(day_mean(Volume), 241)))`
  - score -0.24(train +0.56 valid -0.24):`cs_bucket_zscore(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(sub(log(cross_semistd_pos(day_mean(Volume), 120)), log(cross_semistd_neg(day_mean(Volume), 241))))), LogFloatCap)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.23(knockout ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)):`cs_last_low10(sub(log(cs_last_low40(ts_argmin(ts_mean(abs_(day_mean(Vwap)), 30), 30), sigmoid(inv(day_wstd(Close, Amt))))), ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), ts_std(ts_std(day_mean(Amt), 40), 40))`
