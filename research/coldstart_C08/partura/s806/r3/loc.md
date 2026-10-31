# 定位:种子 806,P 组,第 3 轮(只含 train / valid)

快照:c07s806M1_I0_open_search, c07s806M2_I0_open_search, c07s806M3_I0_open_search, c08s806Pr1a_Ea, c08s806Pr1b_Nb, c08s806Pr2a_Ea, c08s806Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.35 | +1.49 | +1.35 | -1 | 5 | c07s806M2_I0_open_search | `ts_quantile_q50(day_centroid(Amt), 20)` |
| +1.12 | +1.20 | +1.12 | +1 | 20 | c08s806Pr2b_Nb | `cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)` |
| +1.01 | +1.29 | +1.01 | -1 | 5 | c08s806Pr2a_Ea | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))` |
| +0.96 | +0.96 | +1.64 | -1 | 20 | c08s806Pr2a_Ea | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` |
| +0.67 | +0.67 | +1.10 | +1 | 20 | c08s806Pr1b_Nb | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(cross_delay(cross_delay(day_last(Close), 1), 1), cross_delay(day_last(Close), 1)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| +0.60 | +0.60 | +0.82 | +1 | 20 | c08s806Pr1b_Nb | `div(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 20), add(cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), day_last(Close)))), 20), cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)))` |
| +0.50 | +0.50 | +0.51 | +1 | 20 | c08s806Pr2a_Ea | `cs_first_low40(LogFloatShares, day_centroid(Amt))` |

## 共性:477 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.62 | 0.004 | 4 | +0.35 / -1.26 | `ts_quantile_q50(day_centroid(Amt), 10)` |
| +1.50 | 0.000 | 13 | +0.21 / -1.29 | `day_std(Amt)` |
| +1.43 | 0.000 | 11 | +0.15 / -1.28 | `cross_mean(day_std(Amt), 30)` |
| +1.32 | 0.000 | 12 | +0.03 / -1.28 | `cross_ema(day_centroid(Amt), 20)` |
| +1.22 | 0.007 | 5 | -0.05 / -1.26 | `log(day_open(Low))` |
| +1.03 | 0.008 | 7 | -0.24 / -1.27 | `day_first(Close)` |
| +1.00 | 0.020 | 6 | -0.26 / -1.26 | `day_open(Low)` |
| +0.96 | 0.000 | 52 | -0.40 / -1.36 | `day_centroid(Amt)` |
| +0.94 | 0.035 | 6 | -0.32 / -1.26 | `mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))` |
| +0.89 | 0.042 | 5 | -0.37 / -1.26 | `div(day_first(Close), cross_delay(day_last(Close), 1))` |
| +0.89 | 0.042 | 5 | -0.37 / -1.26 | `log(div(day_first(Close), cross_delay(day_last(Close), 1)))` |
| +0.88 | 0.001 | 16 | -0.40 / -1.28 | `div(day_first(Amt), day_sum(Amt))` |
| +0.83 | 0.074 | 4 | -0.43 / -1.26 | `cross_ema(day_min(Close), 10)` |
| +0.79 | 0.024 | 6 | -0.47 / -1.26 | `cross_max(abs_(cross_max(cross_product(day_max(Ret), 3), 30)), 30)` |
| +0.79 | 0.001 | 20 | -0.50 / -1.28 | `ts_corr(day_max(Ret), day_min(Close), 40)` |
| +0.79 | 0.008 | 9 | -0.48 / -1.27 | `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` |
| +0.77 | 0.004 | 15 | -0.50 / -1.28 | `cross_ema(ts_corr(day_max(Ret), day_min(Close), 40), 10)` |
| +0.75 | 0.001 | 26 | -0.55 / -1.29 | `day_min(Close)` |
| +0.73 | 0.004 | 11 | -0.54 / -1.27 | `pow_3(LogFloatShares)` |
| +0.72 | 0.027 | 6 | -0.54 / -1.26 | `abs_(LogFloatShares)` |

## 拆解(32 次评估)

### head score +1.12:`cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))))` | — | — | — | — | 门槛废品 |
| sufficiency | `mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))` | -4.31 | -1.96 | -4.31 | — | (子树本身) |
| sufficiency | `mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))` | -1.04 | -1.04 | +0.38 | — | (子树本身) |
| sufficiency | `is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0)` | — | — | — | — | 门槛废品 |
| knockout | `mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1)))))` | — | — | — | — | `cross_mean(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), 20)` |
| knockout | `mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))` | +1.26 | +1.26 | +1.75 | -0.14 | `cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))), 20)` |
| knockout | `mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))` | +1.26 | +1.26 | +1.75 | -0.14 | `cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(div(day_first(Amt), day_sum(Amt)), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)` |
| knockout | `is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0)` | -0.21 | -0.21 | +0.42 | +1.34 | `cross_mean(mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)` |
| swap | `Open->Close` | +1.12 | +1.20 | +1.12 | — | `cross_mean(mul(is_gt(log(div(day_first(Close), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Close), cross_delay(day_last(Close), 1))))), log(div(day_first(Close), cross_delay(day_last(Close), 1))))), 20)` |
| swap | `Close->Vwap` | +1.13 | +1.20 | +1.13 | — | `cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Vwap), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Vwap), 1))))), log(div(day_first(Open), cross_delay(day_last(Vwap), 1))))), 20)` |
| window | `cross_mean@20->10` | +0.94 | +0.94 | +1.12 | — | `cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 10)` |
| window | `cross_mean@20->40` | +0.80 | +0.80 | +1.02 | — | `cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 40)` |

### head score +1.01:`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30))` | +1.01 | +1.30 | +1.01 | — | (子树本身) |
| sufficiency | `cross_ema(day_centroid(Amt), 20)` | +0.90 | +1.63 | +0.90 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -2.57 | -2.57 | -2.56 | — | (子树本身) |
| knockout | `cross_ema(day_centroid(Amt), 20)` | +0.46 | +0.67 | +0.46 | +0.54 | `cs_bucket_rank(cs_bucket_rank(day_centroid(Amt), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_std(Amt), 30)` | +0.92 | +0.92 | +1.06 | +0.08 | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), day_std(Amt)), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_std(Amt), 30)` | +1.19 | +1.19 | +1.19 | -0.18 | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30)), day_std(Amt))` |
| swap | `Amt->Volume` | -0.54 | +0.87 | -0.54 | — | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Volume), 20), cross_mean(day_std(Volume), 30)), cross_mean(day_std(Volume), 30))` |
| window | `cross_ema@20->10` | +1.36 | +1.50 | +1.36 | — | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 10), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))` |
| window | `cross_ema@20->40` | +0.19 | +0.52 | +0.19 | — | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 40), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))` |

### head score +0.96:`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` | +0.96 | +0.96 | +1.62 | — | (子树本身) |
| sufficiency | `cross_mean(cross_ema(day_centroid(Amt), 20), 30)` | +0.89 | +1.17 | +0.89 | — | (子树本身) |
| sufficiency | `cross_ema(day_centroid(Amt), 20)` | +0.90 | +1.63 | +0.90 | — | (子树本身) |
| knockout | `cross_mean(cross_ema(day_centroid(Amt), 20), 30)` | -3.30 | -3.30 | -3.29 | +4.26 | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_ema(day_centroid(Amt), 20)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` |
| knockout | `cross_mean(cross_ema(day_centroid(Amt), 20), 30)` | -0.81 | -0.49 | -0.81 | +1.77 | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_ema(day_centroid(Amt), 20))` |
| knockout | `cross_ema(day_centroid(Amt), 20)` | -0.42 | -0.42 | +0.29 | +1.38 | `cs_bucket_rank(cs_bucket_rank(day_centroid(Amt), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` |
| swap | `Amt->Volume` | +0.93 | +0.93 | +1.88 | — | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Volume), 20), cross_mean(cross_ema(day_centroid(Volume), 20), 30)), cross_mean(cross_ema(day_centroid(Volume), 20), 30))` |
| window | `cross_ema@20->10` | +1.07 | +1.07 | +1.69 | — | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 10), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` |
| window | `cross_ema@20->40` | -0.10 | +1.07 | -0.10 | — | `cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 40), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` |

### head score +0.50:`cs_first_low40(LogFloatShares, day_centroid(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| swap | `Amt->Volume` | +0.35 | +0.35 | +0.41 | — | `cs_first_low40(LogFloatShares, day_centroid(Volume))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30))` — ablation,自身 score +1.01(所在 head +1.01)
2. `cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(cross_ema(day_centroid(Amt), 20), 30))` — ablation,自身 score +0.96(所在 head +0.96)
3. `cross_ema(day_centroid(Amt), 20)` — ablation,自身 score +0.90(所在 head +1.01)
4. `cross_mean(cross_ema(day_centroid(Amt), 20), 30)` — ablation,自身 score +0.89(所在 head +0.96)
5. `ts_quantile_q50(day_centroid(Amt), 10)` — enrichment,均值差 +1.62,p 0.004
6. `day_std(Amt)` — enrichment,均值差 +1.50,p 0.000
7. `cross_mean(day_std(Amt), 30)` — enrichment,均值差 +1.43,p 0.000
8. `log(day_open(Low))` — enrichment,均值差 +1.22,p 0.007
9. `day_first(Close)` — enrichment,均值差 +1.03,p 0.008
10. `day_open(Low)` — enrichment,均值差 +1.00,p 0.020
11. `day_centroid(Amt)` — enrichment,均值差 +0.96,p 0.000
12. `mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))` — enrichment,均值差 +0.94,p 0.035
13. `div(day_first(Close), cross_delay(day_last(Close), 1))` — enrichment,均值差 +0.89,p 0.042
14. `log(div(day_first(Close), cross_delay(day_last(Close), 1)))` — enrichment,均值差 +0.89,p 0.042
15. `div(day_first(Amt), day_sum(Amt))` — enrichment,均值差 +0.88,p 0.001
16. `cross_ema(day_min(Close), 10)` — enrichment,均值差 +0.83,p 0.074
17. `cross_max(abs_(cross_max(cross_product(day_max(Ret), 3), 30)), 30)` — enrichment,均值差 +0.79,p 0.024
18. `ts_corr(day_max(Ret), day_min(Close), 40)` — enrichment,均值差 +0.79,p 0.001
19. `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` — enrichment,均值差 +0.79,p 0.008
20. `cross_ema(ts_corr(day_max(Ret), day_min(Close), 40), 10)` — enrichment,均值差 +0.77,p 0.004
21. `day_min(Close)` — enrichment,均值差 +0.75,p 0.001
22. `pow_3(LogFloatShares)` — enrichment,均值差 +0.73,p 0.004
23. `abs_(LogFloatShares)` — enrichment,均值差 +0.72,p 0.027
24. `pow_3(pow_3(LogFloatShares))` — enrichment,均值差 +0.72,p 0.039
25. `pow_3(abs_(LogFloatShares))` — enrichment,均值差 +0.72,p 0.058
26. `is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0)` — enrichment,均值差 +0.71,p 0.026
27. `day_sum(Amt)` — enrichment,均值差 +0.71,p 0.002
28. `abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))` — enrichment,均值差 +0.68,p 0.054
29. `cross_max(cross_product(day_max(Ret), 3), 30)` — enrichment,均值差 +0.67,p 0.005
30. `day_open(Open)` — enrichment,均值差 +0.64,p 0.081
31. `cs_normalize(day_open(Open))` — enrichment,均值差 +0.64,p 0.081
32. `mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open))))` — enrichment,均值差 +0.61,p 0.051
33. `cross_product(day_max(Ret), 3)` — enrichment,均值差 +0.59,p 0.008
34. `day_first(Amt)` — enrichment,均值差 +0.59,p 0.005
35. `cross_mean(mul(log(div(day_last(Close), day_first(Open))), log(div(day_last(Close), day_first(Open)))), 20)` — enrichment,均值差 +0.57,p 0.080
36. `day_max(Ret)` — enrichment,均值差 +0.25,p 0.027

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
- `c08s806Pr2a_Ea`:核心 `day_centroid(Amt)`;评分 77,过线 9,入 heads 3;采样计数 {'c05_no_core': 935, 'c05_periphery_seen': 6}
  - score +1.01(train +1.29 valid +1.01):`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))`
  - score +1.01(train +1.30 valid +1.01):`cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30))`
  - score +0.96(train +1.41 valid +0.96):`cs_bucket_rank(cross_ema(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 241)), 20), cross_mean(day_std(Amt), 241))`
  - score +0.96(train +0.96 valid +1.64):`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))`
  - score +0.91(train +0.91 valid +0.93):`cs_bucket_rank(cross_ema(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30)), 20), cross_mean(day_std(Amt), 30))`
- `c08s806Pr2b_Nb`:核心 `—`;评分 100,过线 2,入 heads 1;采样计数 {}
  - score +1.12(train +1.20 valid +1.12):`cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)`
  - score +0.80(train +0.89 valid +0.80):`cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 60)`
  - score +0.48(train +0.48 valid +1.31):`cross_mean(mul(cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20), mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)`
  - score +0.26(train +0.70 valid +0.26):`cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(log(div(day_first(Open), cross_delay(day_last(Close), 1))), log(div(day_first(Open), cross_delay(day_last(Amt), 1))))), 20)`
  - score +0.22(train +0.22 valid +1.74):`cross_mean(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), ts_argmax(pow_2(day_wmean(Ret, High)), 40))))), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.35(window cross_ema@20->10):`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 10), cross_mean(day_std(Amt), 30)), cross_mean(day_std(Amt), 30))`
- 增益 +0.18(knockout cross_mean(day_std(Amt), 30)):`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30)), day_std(Amt))`
- 增益 +0.14(knockout mul(mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), log(div(day_first(Open), cross_delay(day_last(Close), 1))))):`cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))), 20)`
- 增益 +0.14(knockout mul(div(day_first(Amt), day_sum(Amt)), abs_(log(div(day_first(Open), cross_delay(day_last(Close), 1)))))):`cross_mean(mul(is_gt(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 0), mul(div(day_first(Amt), day_sum(Amt)), log(div(day_first(Open), cross_delay(day_last(Close), 1))))), 20)`
- 增益 +0.11(window cross_ema@20->10):`cs_bucket_rank(cs_bucket_rank(cross_ema(day_centroid(Amt), 10), cross_mean(cross_ema(day_centroid(Amt), 20), 30)), cross_mean(cross_ema(day_centroid(Amt), 20), 30))`
