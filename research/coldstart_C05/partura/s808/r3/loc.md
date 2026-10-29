# 定位:种子 808,B 组,第 3 轮(只含 train / valid)

快照:c05s808M1_I0_open_search, c05s808M2_I0_open_search, c05s808M3_I0_open_search, c05s808Br1a_Ea, c05s808Br1b_Nb, c05s808Br2a_Ea, c05s808Br2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(13 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.77 | +1.86 | +1.77 | -1 | 5 | c05s808Br2a_Ea | `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)), 20)` |
| +1.64 | +1.64 | +2.36 | -1 | 5 | c05s808Br2b_Nb | `ts_mean(cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)), 20)` |
| +1.45 | +1.47 | +1.45 | +1 | 20 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` |
| +0.99 | +0.99 | +1.91 | -1 | 5 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40), 40)` |
| +0.95 | +0.95 | +1.10 | -1 | 0 | c05s808Br2b_Nb | `ts_max(ts_max(cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap), 40), 40)` |
| +0.95 | +0.95 | +0.95 | +1 | 5 | c05s808Br2b_Nb | `ts_mean(cs_bucket_zscore(LogFloatCap, LogFloatCap), 20)` |
| +0.74 | +0.74 | +0.76 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)` |
| +0.64 | +0.64 | +0.76 | -1 | 0 | c05s808Br2b_Nb | `ts_max(ts_max(cs_bucket_zscore(day_autocorr_n1(Amt), LogFloatCap), 40), 40)` |
| +0.64 | +0.64 | +0.77 | +1 | 20 | c05s808M3_I0_open_search | `cross_quantile_q50(cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60), 60)` |
| +0.61 | +0.61 | +0.95 | +1 | 20 | c05s808Br1a_Ea | `div(LogFloatCap, inv(LogFloatShares))` |
| +0.56 | +0.74 | +0.56 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)` |
| +0.56 | +0.56 | +0.79 | +1 | 5 | c05s808Br1b_Nb | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15)` |
| +0.54 | +0.54 | +2.51 | +1 | 0 | c05s808Br2b_Nb | `ts_mean(ts_max(cs_bucket_zscore(day_distinct_ratio(Volume), LogFloatCap), 40), 20)` |

## 共性:513 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.42 | 0.000 | 11 | +0.84 / -0.59 | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` |
| +1.41 | 0.002 | 5 | +0.83 / -0.57 | `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)), 20)` |
| +1.26 | 0.039 | 4 | +0.69 / -0.57 | `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` |
| +1.23 | 0.017 | 5 | +0.67 / -0.57 | `cs_bucket_zscore(day_centroid(Amt), LogFloatCap)` |
| +1.15 | 0.001 | 9 | +0.57 / -0.58 | `cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40))` |
| +1.15 | 0.013 | 6 | +0.58 / -0.57 | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` |
| +1.13 | 0.000 | 26 | +0.51 / -0.61 | `cross_tail_mean_q75(LogFloatShares, 15)` |
| +1.11 | 0.000 | 8 | +0.54 / -0.57 | `cross_quantile_q50(LogFloatShares, 241)` |
| +1.11 | 0.000 | 16 | +0.52 / -0.59 | `cross_quantile_q50(LogFloatShares, 60)` |
| +1.11 | 0.000 | 10 | +0.53 / -0.58 | `cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15)` |
| +1.10 | 0.002 | 6 | +0.53 / -0.57 | `cross_quantile_q50(cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15), 241)` |
| +1.10 | 0.002 | 6 | +0.53 / -0.57 | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` |
| +1.09 | 0.001 | 13 | +0.51 / -0.58 | `pow_05(LogFloatShares)` |
| +1.09 | 0.000 | 14 | +0.50 / -0.59 | `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` |
| +1.08 | 0.006 | 6 | +0.51 / -0.57 | `pow_05(cross_quantile_q50(LogFloatShares, 60))` |
| +1.08 | 0.030 | 4 | +0.51 / -0.56 | `cross_mean(LogFloatShares, 15)` |
| +1.08 | 0.000 | 40 | +0.44 / -0.64 | `day_centroid(Amt)` |
| +1.07 | 0.014 | 5 | +0.51 / -0.57 | `cross_quantile_q50(cross_quantile_q50(LogFloatShares, 60), 60)` |
| +1.07 | 0.013 | 8 | +0.50 / -0.57 | `sqrt(inv(LogFloatShares))` |
| +1.05 | 0.054 | 5 | +0.49 / -0.57 | `ts_decay_linear(LogFloatShares, 50)` |

## 拆解(34 次评估)

### head score +1.77:`ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40))` | +0.67 | +0.70 | +0.67 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` | +1.45 | +1.47 | +1.45 | — | (子树本身) |
| sufficiency | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` | +1.17 | +1.17 | +2.01 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40))` | +1.27 | +1.27 | +1.71 | +0.50 | `ts_mean(day_centroid(Amt), 20)` |
| knockout | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` | +1.27 | +1.55 | +1.27 | +0.50 | `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)), 20)` |
| knockout | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` | +1.75 | +1.75 | +2.11 | +0.02 | `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)), 20)` |
| swap | `Amt->Volume` | +1.56 | +1.56 | +1.91 | — | `ts_mean(cs_bucket_rank(day_centroid(Volume), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)), 20)` |
| window | `ts_mean@20->10` | +1.49 | +1.54 | +1.49 | — | `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)), 10)` |
| window | `ts_mean@20->40` | +1.28 | +1.28 | +1.54 | — | `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)), 40)` |

### head score +1.64:`ts_mean(cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap))` | +0.50 | +0.50 | +1.72 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)` | -0.67 | -0.67 | -0.37 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Ret)` | -0.85 | -0.85 | -0.62 | — | (子树本身) |
| knockout | `cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap))` | +1.27 | +1.27 | +1.71 | +0.37 | `ts_mean(day_centroid(Amt), 20)` |
| knockout | `cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)` | +1.45 | +1.45 | +2.41 | +0.19 | `ts_mean(cs_bucket_zscore(day_centroid(Amt), day_autocorr_n1(Ret)), 20)` |
| swap | `Amt->Volume` | +1.66 | +1.66 | +2.27 | — | `ts_mean(cs_bucket_zscore(day_centroid(Volume), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)), 20)` |
| window | `ts_mean@20->10` | +1.52 | +1.52 | +2.29 | — | `ts_mean(cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)), 10)` |
| window | `ts_mean@20->40` | +1.40 | +1.40 | +2.57 | — | `ts_mean(cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)), 40)` |

### head score +0.99:`ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40)` | +0.67 | +0.67 | +1.54 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_mean(day_sum(Amt), 20)` | -1.99 | -1.99 | -1.45 | — | (子树本身) |
| sufficiency | `day_distinct_ratio(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20))` | — | — | — | — | `ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)` |
| knockout | `cross_mean(day_sum(Amt), 20)` | +0.71 | +0.71 | +1.56 | +0.27 | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), day_sum(Amt)), 40), 40)` |
| swap | `Amt->Volume` | -0.02 | -0.02 | +0.15 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Volume), 20)), 40), 40)` |
| window | `ts_max@40->20` | +0.84 | +0.84 | +1.77 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40), 20)` |
| window | `ts_max@40->80` | +1.15 | +1.15 | +2.06 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40), 80)` |

### head score +0.95:`ts_max(ts_max(cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap), 40)` | +0.06 | +0.38 | +0.06 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)` | -0.67 | -0.67 | -0.37 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Ret)` | -0.85 | -0.85 | -0.62 | — | (子树本身) |
| knockout | `cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)` | -0.03 | +0.54 | -0.03 | +0.98 | `ts_max(ts_max(day_autocorr_n1(Ret), 40), 40)` |
| window | `ts_max@40->20` | +0.57 | +0.57 | +0.61 | — | `ts_max(ts_max(cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap), 40), 20)` |
| window | `ts_max@40->80` | +0.75 | +0.75 | +1.59 | — | `ts_max(ts_max(cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap), 40), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` — ablation,自身 score +1.45(所在 head +1.77)
2. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` — ablation,自身 score +1.17(所在 head +1.77)
3. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40)` — ablation,自身 score +0.67(所在 head +0.99)
4. `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` — enrichment,均值差 +1.42,p 0.000
5. `ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)), 20)` — enrichment,均值差 +1.41,p 0.002
6. `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` — enrichment,均值差 +1.26,p 0.039
7. `cs_bucket_zscore(day_centroid(Amt), LogFloatCap)` — enrichment,均值差 +1.23,p 0.017
8. `cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40))` — enrichment,均值差 +1.15,p 0.001
9. `cross_tail_mean_q75(LogFloatShares, 15)` — enrichment,均值差 +1.13,p 0.000
10. `cross_quantile_q50(LogFloatShares, 241)` — enrichment,均值差 +1.11,p 0.000
11. `cross_quantile_q50(LogFloatShares, 60)` — enrichment,均值差 +1.11,p 0.000
12. `cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15)` — enrichment,均值差 +1.11,p 0.000
13. `cross_quantile_q50(cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15), 241)` — enrichment,均值差 +1.10,p 0.002
14. `cross_mean(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` — enrichment,均值差 +1.10,p 0.002
15. `pow_05(LogFloatShares)` — enrichment,均值差 +1.09,p 0.001
16. `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` — enrichment,均值差 +1.09,p 0.000
17. `pow_05(cross_quantile_q50(LogFloatShares, 60))` — enrichment,均值差 +1.08,p 0.006
18. `cross_mean(LogFloatShares, 15)` — enrichment,均值差 +1.08,p 0.030
19. `day_centroid(Amt)` — enrichment,均值差 +1.08,p 0.000
20. `cross_quantile_q50(cross_quantile_q50(LogFloatShares, 60), 60)` — enrichment,均值差 +1.07,p 0.014
21. `sqrt(inv(LogFloatShares))` — enrichment,均值差 +1.07,p 0.013
22. `ts_decay_linear(LogFloatShares, 50)` — enrichment,均值差 +1.05,p 0.054
23. `cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` — enrichment,均值差 +1.00,p 0.020
24. `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` — enrichment,均值差 +0.89,p 0.009
25. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)` — enrichment,均值差 +0.89,p 0.000
26. `div(LogFloatCap, inv(LogFloatShares))` — enrichment,均值差 +0.83,p 0.003
27. `cs_last_high05(LogFloatCap, LogFloatCap)` — enrichment,均值差 +0.76,p 0.018
28. `ts_max(ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40), 40)` — enrichment,均值差 +0.66,p 0.099
29. `day_distinct_ratio(Ret)` — enrichment,均值差 +0.51,p 0.002
30. `sqrt(div(LogFloatCap, inv(LogFloatShares)))` — enrichment,均值差 +0.49,p 0.054
31. `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` — enrichment,均值差 +0.49,p 0.000
32. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` — enrichment,均值差 +0.46,p 0.001
33. `inv(LogFloatShares)` — enrichment,均值差 +0.42,p 0.057

## 本组之前各轮的任务

- `c05s808Br1a_Ea`:核心 `inv(LogFloatShares)`;评分 84,过线 9,入 heads 1;采样计数 {'c05_no_core': 1289, 'c05_periphery_seen': 13}
  - score +0.61(train +0.61 valid +0.95):`div(LogFloatCap, inv(LogFloatShares))`
  - score +0.60(train +0.60 valid +0.86):`ts_mean(inv(sqrt(div(LogFloatCap, inv(LogFloatShares)))), 20)`
  - score +0.60(train +0.60 valid +0.86):`ts_mean(sqrt(div(LogFloatCap, inv(LogFloatShares))), 20)`
  - score +0.60(train +0.60 valid +0.79):`sqrt(inv(ts_mean(inv(sqrt(div(LogFloatCap, inv(LogFloatShares)))), 1)))`
  - score +0.59(train +0.59 valid +0.98):`div(LogFloatCap, inv(div(LogFloatCap, inv(LogFloatShares))))`
- `c05s808Br1b_Nb`:核心 `—`;评分 84,过线 31,入 heads 1;采样计数 {}
  - score +0.56(train +0.56 valid +0.79):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15)`
  - score +0.55(train +0.55 valid +0.79):`cross_mean(cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_mean(LogFloatShares, 15), 15), 241), 15), 15)`
  - score +0.55(train +0.55 valid +0.81):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15), 241), 15), 241), 15)`
  - score +0.55(train +0.55 valid +0.81):`cross_quantile_q50(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 241)`
  - score +0.55(train +0.55 valid +0.81):`cross_mean(cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15), 15)`
- `c05s808Br2a_Ea`:核心 `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)`;评分 102,过线 19,入 heads 1;采样计数 {'c05_no_core': 2674, 'mutation_refused': 1, 'c05_periphery_seen': 3, 'c05_skeleton': 2}
  - score +1.77(train +1.86 valid +1.77):`ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)), 20)`
  - score +1.63(train +1.93 valid +1.63):`ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40), 40)), 20)`
  - score +1.54(train +1.88 valid +1.54):`ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(ts_max(cs_bucket_zscore(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), LogFloatCap), 40), 40), 40)), 20)`
  - score +1.53(train +1.89 valid +1.53):`ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40), 40), 40)), 20)`
  - score +1.45(train +1.63 valid +1.45):`ts_mean(cs_bucket_rank(day_centroid(Amt), ts_max(ts_max(cs_bucket_zscore(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), LogFloatCap), 40)), 40), 40)), 20)`
- `c05s808Br2b_Nb`:核心 `—`;评分 84,过线 13,入 heads 5;采样计数 {}
  - score +1.64(train +1.64 valid +2.36):`ts_mean(cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap)), 20)`
  - score +1.57(train +1.57 valid +1.86):`ts_mean(cs_bucket_zscore(day_centroid(Amt), cs_bucket_zscore(day_autocorr_n1(Ret), ts_mean(cs_bucket_zscore(day_centroid(Amt), LogFloatCap), 20))), 10)`
  - score +1.12(train +1.12 valid +1.33):`ts_mean(cs_bucket_zscore(day_centroid(Amt), LogFloatCap), 20)`
  - score +1.12(train +1.12 valid +1.33):`ts_mean(cs_bucket_zscore(cs_bucket_zscore(day_centroid(Amt), LogFloatCap), LogFloatCap), 20)`
  - score +0.95(train +0.95 valid +1.10):`ts_max(ts_max(cs_bucket_zscore(day_autocorr_n1(Ret), LogFloatCap), 40), 40)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.17(window ts_max@40->80):`ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40), 80)`
