# 定位:种子 906,P 组,第 3 轮(只含 train / valid)

快照:prods906M1_I0_open_search, prods906M2_I0_open_search, prods906M3_I0_open_search, prods906Pr1a_Ea, prods906Pr1b_Nb, prods906Pr2a_Ea, prods906Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(31 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +2.36 | +2.36 | +2.38 | -1 | 5 | prods906Pr2a_Ea | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge), cross_mean(day_centroid(Amt), 20))` |
| +1.81 | +1.94 | +1.81 | -1 | 5 | prods906Pr2b_Nb | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| +1.80 | +1.80 | +2.56 | -1 | 5 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, LogFloatCap)` |
| +1.63 | +1.63 | +1.88 | +1 | 5 | prods906Pr2b_Nb | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 20)` |
| +1.62 | +1.81 | +1.62 | -1 | 5 | prods906Pr1a_Ea | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.59 | +1.59 | +3.81 | -1 | 5 | prods906Pr2a_Ea | `cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 20))` |
| +1.58 | +1.58 | +2.38 | -1 | 5 | prods906Pr2a_Ea | `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(LogFloatCap, LogFloatCap))` |
| +1.50 | +1.50 | +3.04 | -1 | 5 | prods906Pr1a_Ea | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))` |
| +1.41 | +2.00 | +1.41 | -1 | 20 | prods906Pr2a_Ea | `cs_first_high20(cs_first_high20(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap)), cross_mean(day_std(Amt), 20))` |
| +1.30 | +1.30 | +3.56 | -1 | 5 | prods906Pr1a_Ea | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.20 | +1.20 | +2.53 | -1 | 5 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Open)))` |
| +1.18 | +1.18 | +1.32 | -1 | 20 | prods906Pr2a_Ea | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 241))` |
| +1.13 | +1.20 | +1.13 | -1 | 20 | prods906Pr2a_Ea | `cs_first_high20(cs_first_low20(cross_mean(cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge), cross_mean(day_open(Amt), 20)), 20), ListAge), cross_mean(day_open(Amt), 20))` |
| +1.10 | +1.10 | +1.66 | +1 | 5 | prods906Pr2a_Ea | `cs_first_low40(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 20))` |
| +1.03 | +1.03 | +1.09 | -1 | 5 | prods906Pr2a_Ea | `cs_first_high20(cs_first_high20(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap)), cross_mean(day_centroid(Ret), 20))` |
| +0.98 | +0.98 | +3.57 | -1 | 5 | prods906Pr2a_Ea | `cs_first_high20(cs_last_low10(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 20))` |
| +0.94 | +0.94 | +2.69 | -1 | 5 | prods906Pr1b_Nb | `cs_first_low20(cs_first_low20(LogFloatCap, day_last(Open)), cs_first_low20(LogFloatCap, day_last(Open)))` |
| +0.92 | +0.92 | +1.84 | -1 | 20 | prods906Pr2a_Ea | `cs_first_high20(cross_mean(day_centroid(Amt), 20), sub(day_q_stat_std(Ret), LogFloatCap))` |
| +0.84 | +0.84 | +2.55 | +1 | 5 | prods906Pr2b_Nb | `cross_mean(div(sub(day_centroid(Ret), day_centroid(Amt)), day_sum(Amt)), 20)` |
| +0.81 | +0.81 | +1.09 | +1 | 0 | prods906Pr2b_Nb | `cross_mean(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), 241)` |
| +0.79 | +0.79 | +1.03 | -1 | 5 | prods906Pr2a_Ea | `sub(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_centroid(Ret), 20)))` |
| +0.74 | +0.74 | +0.78 | -1 | 20 | prods906M3_I0_open_search | `cross_max(signedpower(day_centroid(Amt)), 3)` |
| +0.73 | +0.73 | +0.92 | +1 | 20 | prods906Pr1a_Ea | `cs_last_low20(cross_mean(day_gini(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +0.72 | +0.72 | +3.15 | -1 | 5 | prods906M1_I0_open_search | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))))` |
| +0.70 | +0.70 | +2.29 | +1 | 5 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Open))))` |
| +0.68 | +0.68 | +1.94 | -1 | 0 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, day_sum(Low))` |
| +0.66 | +0.66 | +2.33 | +1 | 5 | prods906Pr1a_Ea | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap)), day_centroid(Amt))` |
| +0.58 | +0.58 | +1.45 | -1 | 20 | prods906Pr2a_Ea | `cs_first_high20(cs_last_low40(day_centroid(Amt), LogFloatCap), cross_mean(day_centroid(Amt), 20))` |
| +0.54 | +0.54 | +1.35 | -1 | 0 | prods906Pr1a_Ea | `sigmoid(cs_first_low20(cs_first_low20(cross_mean(day_first(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), day_last(Vwap)))` |
| +0.51 | +0.58 | +0.51 | -1 | 20 | prods906Pr2a_Ea | `cs_first_high20(cross_madz(cross_mean(day_centroid(Amt), 20), 15), sub(LogTotalCap, LogFloatCap))` |
| +0.50 | +0.50 | +1.86 | +1 | 20 | prods906Pr1a_Ea | `cs_first_low20(cross_mean(day_signed_ratio(Ret, Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |

## 共性:502 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.20 | 0.000 | 6 | +1.65 / -0.55 | `day_q_stat_std(Ret)` |
| +1.93 | 0.000 | 6 | +1.38 / -0.55 | `cross_mean(cross_mean(day_centroid(Amt), 20), 20)` |
| +1.89 | 0.000 | 5 | +1.35 / -0.54 | `sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt))` |
| +1.88 | 0.000 | 9 | +1.33 / -0.56 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` |
| +1.78 | 0.000 | 9 | +1.23 / -0.56 | `cs_first_high20(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap))` |
| +1.72 | 0.003 | 4 | +1.18 / -0.54 | `cross_mean(day_std(Ret), 20)` |
| +1.72 | 0.003 | 4 | +1.18 / -0.54 | `day_std(Ret)` |
| +1.70 | 0.001 | 5 | +1.16 / -0.54 | `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.67 | 0.000 | 18 | +1.09 / -0.58 | `sub(LogTotalCap, LogFloatCap)` |
| +1.60 | 0.000 | 79 | +0.82 / -0.78 | `cross_mean(day_centroid(Amt), 20)` |
| +1.56 | 0.000 | 136 | +0.61 / -0.95 | `day_centroid(Amt)` |
| +1.55 | 0.000 | 10 | +1.00 / -0.56 | `cs_first_low20(LogFloatCap, LogFloatCap)` |
| +1.39 | 0.014 | 4 | +0.86 / -0.54 | `cross_mean(day_centroid(Amt), 3)` |
| +1.09 | 0.010 | 6 | +0.55 / -0.54 | `pow_2(pow_2(day_centroid(Volume)))` |
| +1.05 | 0.081 | 4 | +0.51 / -0.53 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.03 | 0.035 | 5 | +0.50 / -0.53 | `cs_first_low20(LogFloatCap, day_last(Open))` |
| +1.03 | 0.019 | 6 | +0.49 / -0.54 | `day_last(High)` |
| +1.00 | 0.036 | 6 | +0.46 / -0.54 | `day_last(Open)` |
| +0.96 | 0.025 | 8 | +0.42 / -0.54 | `signedpower(day_centroid(Amt))` |
| +0.93 | 0.067 | 6 | +0.40 / -0.54 | `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` |

## 拆解(32 次评估)

### head score +2.36:`cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge), cross_mean(day_centroid(Amt), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` | +1.80 | +2.52 | +1.80 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` | +1.34 | +1.72 | +1.34 | +1.02 | `cs_first_high20(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 20))` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +1.41 | +1.41 | +1.75 | +0.95 | `cs_first_high20(cs_first_low20(day_centroid(Amt), ListAge), cross_mean(day_centroid(Amt), 20))` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +1.92 | +2.05 | +1.92 | +0.44 | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge), day_centroid(Amt))` |
| swap | `Amt->Volume` | +2.37 | +2.40 | +2.37 | — | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Volume), 20), ListAge), cross_mean(day_centroid(Volume), 20))` |
| window | `cross_mean@20->10` | +1.76 | +2.04 | +1.76 | — | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge), cross_mean(day_centroid(Amt), 20))` |
| window | `cross_mean@20->40` | +1.92 | +1.92 | +2.10 | — | `cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 40), ListAge), cross_mean(day_centroid(Amt), 20))` |

### head score +1.81:`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | +0.28 | +0.98 | +0.28 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Amt, 211, 240))` | -1.92 | -1.92 | -1.76 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | -1.80 | -1.64 | -1.80 | +3.61 | `cross_mean(day_sum(in_slice(Amt, 211, 240)), 20)` |
| swap | `Amt->Volume` | +1.70 | +1.91 | +1.70 | — | `cross_mean(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume)), 20)` |
| window | `cross_mean@20->10` | +1.53 | +1.53 | +1.65 | — | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 10)` |
| window | `cross_mean@20->40` | +1.31 | +1.31 | +2.00 | — | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 40)` |

### head score +1.63:`cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt))` | +1.20 | +1.20 | +1.22 | — | (子树本身) |
| sufficiency | `sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt))` | +0.88 | +0.88 | +1.43 | — | (子树本身) |
| sufficiency | `sub(day_centroid(Ret), day_centroid(Amt))` | +0.61 | +0.61 | +0.75 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -2.89 | -1.77 | -2.89 | — | (子树本身) |
| knockout | `sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt))` | +1.23 | +1.23 | +1.82 | +0.40 | `cross_mean(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), 20)` |
| swap | `Amt->Volume` | +1.66 | +1.66 | +1.82 | — | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centroid(Volume)), day_centroid(Volume)), 20)` |
| window | `cross_mean@20->10` | +1.05 | +1.44 | +1.05 | — | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 10)` |
| window | `cross_mean@20->40` | +0.96 | +0.96 | +2.10 | — | `cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 40)` |

### head score +1.59:`cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `cs_first_low20(LogFloatCap, LogFloatCap)` | +1.80 | +1.80 | +2.56 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +1.59 | +1.59 | +2.74 | -0.00 | `cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), day_centroid(Amt))` |
| knockout | `cs_first_low20(LogFloatCap, LogFloatCap)` | +0.98 | +0.98 | +3.57 | +0.61 | `cs_first_high20(LogFloatCap, cross_mean(day_centroid(Amt), 20))` |
| swap | `Amt->Volume` | +1.58 | +1.58 | +3.81 | — | `cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Volume), 20))` |
| window | `cross_mean@20->10` | +1.49 | +1.49 | +3.41 | — | `cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 10))` |
| window | `cross_mean@20->40` | +1.34 | +1.34 | +3.98 | — | `cs_first_high20(cs_first_low20(LogFloatCap, LogFloatCap), cross_mean(day_centroid(Amt), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)` — ablation,自身 score +1.80(所在 head +2.36)
2. `cs_first_low20(LogFloatCap, LogFloatCap)` — ablation,自身 score +1.80(所在 head +1.59)
3. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +1.59)
4. `sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt))` — ablation,自身 score +1.20(所在 head +1.63)
5. `day_q_stat_std(Ret)` — enrichment,均值差 +2.20,p 0.000
6. `cross_mean(cross_mean(day_centroid(Amt), 20), 20)` — enrichment,均值差 +1.93,p 0.000
7. `sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt))` — enrichment,均值差 +1.89,p 0.000
8. `cs_first_high20(cross_mean(day_centroid(Amt), 20), sub(LogTotalCap, LogFloatCap))` — enrichment,均值差 +1.78,p 0.000
9. `cross_mean(day_std(Ret), 20)` — enrichment,均值差 +1.72,p 0.003
10. `day_std(Ret)` — enrichment,均值差 +1.72,p 0.003
11. `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` — enrichment,均值差 +1.70,p 0.001
12. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +1.67,p 0.000
13. `day_centroid(Amt)` — enrichment,均值差 +1.56,p 0.000
14. `cross_mean(day_centroid(Amt), 3)` — enrichment,均值差 +1.39,p 0.014
15. `pow_2(pow_2(day_centroid(Volume)))` — enrichment,均值差 +1.09,p 0.010
16. `cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` — enrichment,均值差 +1.05,p 0.081
17. `cs_first_low20(LogFloatCap, day_last(Open))` — enrichment,均值差 +1.03,p 0.035
18. `day_last(High)` — enrichment,均值差 +1.03,p 0.019
19. `day_last(Open)` — enrichment,均值差 +1.00,p 0.036
20. `signedpower(day_centroid(Amt))` — enrichment,均值差 +0.96,p 0.025
21. `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` — enrichment,均值差 +0.93,p 0.067
22. `cs_first_low20(day_last(Vwap), day_quantile(High))` — enrichment,均值差 +0.91,p 0.002
23. `sub(day_centroid(Ret), day_centroid(Amt))` — enrichment,均值差 +0.90,p 0.005
24. `pow_2(day_centroid(Volume))` — enrichment,均值差 +0.89,p 0.020
25. `cs_first_low20(day_quantile(High), day_quantile(High))` — enrichment,均值差 +0.87,p 0.084
26. `pow_2(day_centroid(Amt))` — enrichment,均值差 +0.83,p 0.032
27. `cs_first_low20(day_last(Vwap), day_last(Vwap))` — enrichment,均值差 +0.83,p 0.000
28. `day_std(Amt)` — enrichment,均值差 +0.81,p 0.095
29. `day_last(Vwap)` — enrichment,均值差 +0.80,p 0.000
30. `day_centroid(Volume)` — enrichment,均值差 +0.77,p 0.008
31. `pow_2(cs_first_low20(day_last(Vwap), day_quantile(High)))` — enrichment,均值差 +0.74,p 0.084
32. `day_quantile(High)` — enrichment,均值差 +0.66,p 0.005
33. `cross_mean(day_centroid(Amt), 15)` — enrichment,均值差 +0.57,p 0.087
34. `day_centroid(Ret)` — enrichment,均值差 +0.46,p 0.033

## 本组之前各轮的任务

- `prods906Pr1a_Ea`:核心 `cs_first_low20(day_last(Vwap), day_last(Vwap))`;评分 82,过线 28,入 heads 7;采样计数 {'c05_no_core': 820, 'c05_periphery_seen': 5}
  - score +1.62(train +1.81 valid +1.62):`cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))`
  - score +1.50(train +1.50 valid +3.04):`cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))`
  - score +1.48(train +1.48 valid +1.75):`cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))`
  - score +1.48(train +1.48 valid +1.75):`sqrt(cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))))`
  - score +1.30(train +1.30 valid +3.56):`cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))`
- `prods906Pr1b_Nb`:核心 `—`;评分 69,过线 9,入 heads 5;采样计数 {}
  - score +1.80(train +1.80 valid +2.56):`cs_first_low20(LogFloatCap, LogFloatCap)`
  - score +1.20(train +1.20 valid +2.53):`cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Open)))`
  - score +1.19(train +1.19 valid +2.55):`cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Close)))`
  - score +1.18(train +1.18 valid +2.55):`cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Vwap)))`
  - score +0.94(train +0.94 valid +2.69):`cs_first_low20(cs_first_low20(LogFloatCap, day_last(Open)), cs_first_low20(LogFloatCap, day_last(Open)))`
- `prods906Pr2a_Ea`:核心 `cross_mean(day_centroid(Amt), 20)`;评分 112,过线 47,入 heads 13;采样计数 {'c05_no_core': 2225, 'c05_skeleton': 6, 'c05_periphery_seen': 8, 'mutation_refused': 6}
  - score +2.36(train +2.36 valid +2.38):`cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge), cross_mean(day_centroid(Amt), 20))`
  - score +2.09(train +2.09 valid +2.45):`cs_first_high20(cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_q_stat_std(Ret), 30)), cross_mean(day_centroid(Amt), 20))`
  - score +2.08(train +2.08 valid +2.39):`cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_q_stat_std(Ret), 30))`
  - score +1.94(train +1.94 valid +2.52):`cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_q_stat_std(Ret), 20))`
  - score +1.91(train +1.91 valid +2.28):`cs_first_high20(cs_first_low20(cross_mean(cs_first_high20(cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge), cross_mean(day_centroid(Amt), 20)), 20), ListAge), cross_mean(day_centroid(Amt), 20))`
- `prods906Pr2b_Nb`:核心 `—`;评分 90,过线 10,入 heads 4;采样计数 {}
  - score +1.81(train +1.94 valid +1.81):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)`
  - score +1.63(train +1.63 valid +1.88):`cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 20)`
  - score +1.62(train +1.62 valid +1.70):`cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 15)`
  - score +1.44(train +1.44 valid +1.62):`cross_mean(sub(sub(sub(day_centroid(Ret), day_centroid(Amt)), day_centroid(Amt)), day_centroid(Amt)), 3)`
  - score +1.27(train +1.27 valid +1.80):`cross_mean(sub(sub(day_flat_run_max(Ret), day_centroid(Amt)), day_centroid(Amt)), 20)`

## 比原 head 好的拆解变体(R 候选)

(没有)
