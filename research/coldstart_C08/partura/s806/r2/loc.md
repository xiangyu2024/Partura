# 定位:种子 806,P 组,第 2 轮(只含 train / valid)

快照:c07s806M1_I0_open_search, c07s806M2_I0_open_search, c08s806Pr1a_Ea, c08s806Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.35 | +1.49 | +1.35 | -1 | 5 | c07s806M2_I0_open_search | `ts_quantile_q50(day_centroid(Amt), 20)` |
| +0.67 | +0.67 | +1.10 | +1 | 20 | c08s806Pr1b_Nb | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| +0.60 | +0.60 | +0.82 | +1 | 20 | c08s806Pr1b_Nb | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |

## 共性:323 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.77 | 0.000 | 11 | +0.40 / -1.38 | `day_centroid(Amt)` |
| +1.69 | 0.002 | 4 | +0.35 / -1.34 | `ts_quantile_q50(day_centroid(Amt), 10)` |
| +1.29 | 0.004 | 5 | -0.05 / -1.34 | `log(day_open(Low))` |
| +1.07 | 0.012 | 6 | -0.26 / -1.34 | `day_open(Low)` |
| +1.05 | 0.011 | 6 | -0.28 / -1.34 | `day_first(Close)` |
| +0.90 | 0.045 | 4 | -0.43 / -1.33 | `cross_ema(day_min(Close), 10)` |
| +0.87 | 0.000 | 20 | -0.50 / -1.37 | `ts_corr(day_max(Ret), day_min(Close), 40)` |
| +0.87 | 0.000 | 25 | -0.51 / -1.38 | `day_min(Close)` |
| +0.86 | 0.011 | 6 | -0.47 / -1.33 | `cross_max(abs_(cross_max(cross_product(day_max(Ret), 3), 30)), 30)` |
| +0.86 | 0.003 | 9 | -0.48 / -1.34 | `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` |
| +0.86 | 0.068 | 4 | -0.47 / -1.33 | `log(div(day_first(Close), cross_delay(day_last(Close), 1)))` |
| +0.86 | 0.068 | 4 | -0.47 / -1.33 | `div(day_first(Close), cross_delay(day_last(Close), 1))` |
| +0.85 | 0.001 | 15 | -0.50 / -1.36 | `cross_ema(ts_corr(day_max(Ret), day_min(Close), 40), 10)` |
| +0.76 | 0.106 | 4 | -0.56 / -1.33 | `day_durbin_watson(Ret)` |
| +0.75 | 0.001 | 15 | -0.60 / -1.35 | `cross_max(cross_product(day_max(Ret), 3), 30)` |
| +0.71 | 0.042 | 7 | -0.62 / -1.33 | `day_open(Open)` |
| +0.71 | 0.042 | 7 | -0.62 / -1.33 | `cs_normalize(day_open(Open))` |
| +0.69 | 0.027 | 17 | -0.66 / -1.35 | `mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open))))` |
| +0.67 | 0.001 | 18 | -0.68 / -1.35 | `cross_product(day_max(Ret), 3)` |
| +0.65 | 0.046 | 16 | -0.70 / -1.35 | `cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)` |

## 拆解(28 次评估)

### head score +1.35:`ts_quantile_q50(day_centroid(Amt), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| swap | `Amt->Volume` | +1.26 | +1.46 | +1.26 | — | `ts_quantile_q50(day_centroid(Volume), 20)` |
| window | `ts_quantile_q50@20->10` | +1.03 | +1.58 | +1.03 | — | `ts_quantile_q50(day_centroid(Amt), 10)` |
| window | `ts_quantile_q50@20->40` | +1.12 | +1.14 | +1.12 | — | `ts_quantile_q50(day_centroid(Amt), 40)` |

### head score +0.67:`div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20))` | -1.08 | -1.08 | -0.94 | — | (子树本身) |
| sufficiency | `cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20)` | -0.38 | -0.07 | -0.38 | — | (子树本身) |
| sufficiency | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20)` | -0.80 | +0.52 | -0.80 | — | (子树本身) |
| sufficiency | `mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))` | -3.03 | -2.31 | -3.03 | — | (子树本身) |
| knockout | `add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20))` | -0.91 | -0.67 | -0.91 | +1.59 | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20))` |
| knockout | `cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20)` | -3.90 | -2.91 | -3.90 | +4.57 | `div(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| knockout | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20)` | +0.25 | +0.25 | +0.39 | +0.42 | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| knockout | `mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))` | -0.66 | -0.58 | -0.66 | +1.33 | `div(cross_mean(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| swap | `Open->Close` | +0.67 | +0.67 | +1.10 | — | `div(cross_mean(mul(log(div(day_first(Close), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Close), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Close), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Close))), log(div(day_last(Close), day_first(Close)))), 20)))` |
| swap | `Close->Vwap` | +0.53 | +0.53 | +1.10 | — | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Vwap), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Vwap), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Vwap), 1))), log(div(cross_delay(cross_delay(day_last(Vwap), 1), 1), cross_delay(day_last(Vwap), 1)))), 20), cross_mean(mul(log(div(day_last(Vwap), day_first(Open))), log(div(day_last(Vwap), day_first(Open)))), 20)))` |
| window | `cross_mean@20->10` | +0.22 | +0.73 | +0.22 | — | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 10), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| window | `cross_mean@20->40` | +0.04 | +0.27 | +0.04 | — | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 40), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |

### head score +0.60:`div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20))` | -1.30 | -1.30 | -0.61 | — | (子树本身) |
| sufficiency | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20)` | -0.76 | -0.76 | +0.16 | — | (子树本身) |
| sufficiency | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20)` | -1.57 | -1.40 | -1.57 | — | (子树本身) |
| sufficiency | `mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))` | -2.06 | -2.06 | -1.52 | — | (子树本身) |
| knockout | `add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20))` | -2.07 | -2.07 | -2.00 | +2.67 | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20))` |
| knockout | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20)` | -1.09 | -1.09 | -0.94 | +1.69 | `div(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| knockout | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20)` | -0.14 | -0.14 | +0.40 | +0.74 | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| knockout | `mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))` | -2.00 | +0.03 | -2.00 | +2.60 | `div(cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| swap | `Open->Close` | +0.53 | +0.53 | +0.82 | — | `div(cross_mean(mul(log(div(day_first(Close), cross_delay(day_last(Close), 1))), log(div(day_first(Close), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Close), cross_delay(day_last(Close), 1))), log(div(day_first(Close), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Close))), log(div(day_last(Close), day_first(Close)))), 20)))` |
| swap | `Close->Vwap` | +0.46 | +0.46 | +0.69 | — | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Vwap), 1))), log(div(day_first(Open), cross_delay(day_last(Vwap), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Vwap), 1))), log(div(day_first(Open), day_last(Vwap)))), 20), cross_mean(mul(log(div(day_last(Vwap), day_first(Open))), log(div(day_last(Vwap), day_first(Open)))), 20)))` |
| window | `cross_mean@20->10` | -0.11 | +0.25 | -0.11 | — | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 10), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| window | `cross_mean@20->40` | -1.02 | -0.33 | -1.02 | — | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 40), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(Amt)` — enrichment,均值差 +1.77,p 0.000
2. `ts_quantile_q50(day_centroid(Amt), 10)` — enrichment,均值差 +1.69,p 0.002
3. `log(day_open(Low))` — enrichment,均值差 +1.29,p 0.004
4. `day_open(Low)` — enrichment,均值差 +1.07,p 0.012
5. `day_first(Close)` — enrichment,均值差 +1.05,p 0.011
6. `cross_ema(day_min(Close), 10)` — enrichment,均值差 +0.90,p 0.045
7. `ts_corr(day_max(Ret), day_min(Close), 40)` — enrichment,均值差 +0.87,p 0.000
8. `day_min(Close)` — enrichment,均值差 +0.87,p 0.000
9. `cross_max(abs_(cross_max(cross_product(day_max(Ret), 3), 30)), 30)` — enrichment,均值差 +0.86,p 0.011
10. `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` — enrichment,均值差 +0.86,p 0.003
11. `log(div(day_first(Close), cross_delay(day_last(Close), 1)))` — enrichment,均值差 +0.86,p 0.068
12. `div(day_first(Close), cross_delay(day_last(Close), 1))` — enrichment,均值差 +0.86,p 0.068
13. `cross_ema(ts_corr(day_max(Ret), day_min(Close), 40), 10)` — enrichment,均值差 +0.85,p 0.001
14. `cross_max(cross_product(day_max(Ret), 3), 30)` — enrichment,均值差 +0.75,p 0.001
15. `day_open(Open)` — enrichment,均值差 +0.71,p 0.042
16. `cs_normalize(day_open(Open))` — enrichment,均值差 +0.71,p 0.042
17. `mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open))))` — enrichment,均值差 +0.69,p 0.027
18. `cross_product(day_max(Ret), 3)` — enrichment,均值差 +0.67,p 0.001
19. `cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)` — enrichment,均值差 +0.65,p 0.046
20. `div(sub(day_max(Ret), day_mean(Ret)), day_std(Ret))` — enrichment,均值差 +0.45,p 0.099
21. `sub(day_max(Ret), day_mean(Ret))` — enrichment,均值差 +0.45,p 0.099
22. `day_max(Ret)` — enrichment,均值差 +0.38,p 0.001
23. `cross_ema(day_std(Ret), 10)` — enrichment,均值差 +0.32,p 0.064
24. `day_std(Ret)` — enrichment,均值差 +0.29,p 0.024

## 本组之前各轮的任务

- `c08s806Pr1a_Ea`:核心 `day_max(Ret)`;评分 86,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 6, 'c05_no_core': 483}
  - score +0.44(train +0.44 valid +0.79):`ts_corr(day_max(Ret), day_min(Close), 40)`
  - score +0.40(train +0.40 valid +0.72):`ts_corr(day_max(Ret), day_min(Low), 40)`
  - score +0.37(train +0.42 valid +0.37):`div(cross_ema(ts_corr(day_max(Ret), day_min(Close), 40), 10), cross_ema(day_std(Ret), 10))`
  - score +0.36(train +0.52 valid +0.36):`div(cross_ema(ts_corr(day_max(Ret), day_min(Close), 40), 10), cross_ema(day_max(Ret), 10))`
  - score +0.36(train +0.36 valid +0.36):`ts_corr(day_max(Ret), day_min(Close), 50)`
- `c08s806Pr1b_Nb`:核心 `—`;评分 93,过线 2,入 heads 2;采样计数 {}
  - score +0.67(train +0.67 valid +1.10):`div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`
  - score +0.60(train +0.60 valid +0.82):`div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`
  - score +0.26(train +0.26 valid +0.68):`div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Close), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`
  - score +0.25(train +0.25 valid +0.68):`div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`
  - score +0.24(train +0.24 valid +0.68):`div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(day_last(Close), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))`

## 比原 head 好的拆解变体(R 候选)

(没有)
