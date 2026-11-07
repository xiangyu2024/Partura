# 定位:种子 911,P 组,第 3 轮(只含 train / valid)

快照:prods911M1_I0_open_search, prods911M2_I0_open_search, prods911M3_I0_open_search, prods911Pr1a_Ea, prods911Pr1b_Nb, prods911Pr2a_Ea, prods911Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(13 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.79 | +1.80 | +1.79 | +1 | 5 | prods911Pr2b_Nb | `cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 60)` |
| +1.47 | +1.47 | +3.35 | -1 | 5 | prods911M2_I0_open_search | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 40)), pow_2_5(day_wmean(Amt, Amt)))` |
| +1.47 | +1.47 | +1.61 | +1 | 5 | prods911Pr2b_Nb | `cross_corr(div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)), day_es_ratio_hi(Amt), 60)` |
| +1.21 | +1.21 | +3.03 | -1 | 5 | prods911Pr1b_Nb | `ts_quantile_q25(cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close)), 10)` |
| +1.16 | +1.16 | +2.02 | +1 | 5 | prods911Pr2b_Nb | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` |
| +0.97 | +0.97 | +2.57 | +1 | 5 | prods911Pr1b_Nb | `cross_mean(div(day_first(Volume), add(cross_delay(day_last(Volume), 1), 1000)), 60)` |
| +0.86 | +0.86 | +0.89 | +1 | 5 | prods911M3_I0_open_search | `cs_bucket_zscore(cs_mask_top_replace_mean_neg(day_close(Vwap)), cs_mask_top_replace_mean_neg(day_close(Vwap)))` |
| +0.70 | +0.70 | +1.86 | +1 | 5 | prods911Pr2b_Nb | `cs_bucket_demean(cross_mean(div(day_first(Amt), day_sum(Amt)), 60), LogFloatCap)` |
| +0.70 | +0.91 | +0.70 | +1 | 5 | prods911Pr2b_Nb | `cross_corr(sub(day_first(Amt), day_sum(Amt)), day_sum(Amt), 60)` |
| +0.65 | +0.65 | +1.54 | +1 | 5 | prods911Pr2b_Nb | `cross_corr(div(day_first(Amt), day_skew(Amt)), add(day_first(Amt), day_sum(Amt)), 60)` |
| +0.63 | +0.63 | +1.59 | +1 | 5 | prods911Pr2b_Nb | `sub(cross_mean(div(day_first(Amt), day_sum(Amt)), 60), cross_mean(div(day_last(Amt), day_sum(Amt)), 60))` |
| +0.60 | +0.60 | +1.83 | +1 | 5 | prods911M3_I0_open_search | `cs_bucket_zscore(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_close(Vwap))), day_flat_ratio(Vwap))` |
| +0.53 | +0.53 | +0.89 | +1 | 20 | prods911Pr2b_Nb | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_sum(Amt), 60)` |

## 共性:585 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.96 | 0.000 | 7 | +0.97 / -0.98 | `day_es_ratio_hi(Amt)` |
| +1.65 | 0.000 | 7 | +0.67 / -0.98 | `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 40))` |
| +1.55 | 0.001 | 7 | +0.57 / -0.98 | `div(day_first(Amt), day_skew(Amt))` |
| +1.48 | 0.000 | 23 | +0.46 / -1.02 | `day_wmean(Volume, Volume)` |
| +1.48 | 0.000 | 22 | +0.46 / -1.02 | `pow_2_5(day_wmean(Volume, Volume))` |
| +1.37 | 0.000 | 15 | +0.37 / -1.00 | `day_skew(Amt)` |
| +1.36 | 0.001 | 5 | +0.39 / -0.97 | `cs_quantile_q75(pow_3(day_quantile_q75(High)))` |
| +1.36 | 0.014 | 4 | +0.39 / -0.97 | `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 50))` |
| +1.36 | 0.004 | 6 | +0.38 / -0.97 | `ts_quantile_q75(day_close(Open), 50)` |
| +1.22 | 0.005 | 5 | +0.25 / -0.97 | `cross_min(pow_2_5(day_wmean(Volume, Low)), 15)` |
| +1.20 | 0.008 | 5 | +0.23 / -0.97 | `ts_quantile_q75(pow_2_5(day_wmean(Volume, Volume)), 10)` |
| +1.09 | 0.004 | 6 | +0.11 / -0.97 | `pow_3(day_quantile_q75(High))` |
| +1.09 | 0.004 | 6 | +0.11 / -0.97 | `day_quantile_q75(High)` |
| +1.07 | 0.000 | 13 | +0.09 / -0.98 | `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Open), 40))` |
| +1.01 | 0.029 | 4 | +0.05 / -0.97 | `cs_last_low20(pow_2_5(day_var(Open)), ts_quantile_q75(day_close(Volume), 40))` |
| +0.97 | 0.000 | 33 | -0.05 / -1.02 | `day_first(Amt)` |
| +0.95 | 0.000 | 45 | -0.08 / -1.03 | `pow_2_5(day_wmean(Volume, Low))` |
| +0.94 | 0.001 | 13 | -0.04 / -0.98 | `cross_scale(cross_scale(LogFloatCap, 241), 241)` |
| +0.94 | 0.000 | 34 | -0.08 / -1.02 | `ts_quantile_q75(day_close(Open), 40)` |
| +0.94 | 0.000 | 81 | -0.15 / -1.09 | `day_close(Open)` |

## 拆解(39 次评估)

### head score +1.79:`cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_first(Amt), day_es_ratio_hi(Amt))` | -1.40 | -1.40 | -0.26 | — | (子树本身) |
| sufficiency | `day_first(Amt)` | -1.39 | -1.39 | -0.14 | — | (子树本身) |
| sufficiency | `day_es_ratio_hi(Amt)` | -5.40 | -3.81 | -5.40 | — | (子树本身) |
| knockout | `div(day_first(Amt), day_es_ratio_hi(Amt))` | +1.88 | +1.88 | +2.22 | -0.10 | `cross_corr(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| swap | `Amt->Volume` | +1.75 | +1.77 | +1.75 | — | `cross_corr(div(day_first(Volume), day_es_ratio_hi(Volume)), day_es_ratio_hi(Volume), 60)` |
| window | `cross_corr@60->30` | +0.37 | +0.37 | +1.37 | — | `cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 30)` |
| window | `cross_corr@60->120` | +0.69 | +1.22 | +0.69 | — | `cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 120)` |

### head score +1.47:`div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 40)), pow_2_5(day_wmean(Amt, Amt)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 40))` | -1.91 | -1.91 | -0.61 | — | (子树本身) |
| sufficiency | `pow_2_5(day_wmean(Amt, Amt))` | -3.22 | -2.84 | -3.22 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(day_close(Open), 40)` | -1.26 | -1.26 | -0.50 | — | (子树本身) |
| knockout | `cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 40))` | — | — | — | — | `div(pow_2_5(day_wmean(Amt, Amt)), pow_2_5(day_wmean(Amt, Amt)))` |
| knockout | `pow_2_5(day_wmean(Amt, Amt))` | +1.47 | +1.47 | +3.35 | +0.00 | `div(cs_last_low20(day_wmean(Amt, Amt), ts_quantile_q75(day_close(Open), 40)), pow_2_5(day_wmean(Amt, Amt)))` |
| knockout | `ts_quantile_q75(day_close(Open), 40)` | +1.49 | +1.49 | +3.29 | -0.02 | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), day_close(Open)), pow_2_5(day_wmean(Amt, Amt)))` |
| knockout | `pow_2_5(day_wmean(Amt, Amt))` | +0.48 | +0.48 | +2.00 | +0.99 | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 40)), day_wmean(Amt, Amt))` |
| swap | `Amt->Volume` | +1.09 | +1.09 | +3.12 | — | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 40)), pow_2_5(day_wmean(Volume, Volume)))` |
| swap | `Open->Close` | +1.47 | +1.47 | +3.34 | — | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Close), 40)), pow_2_5(day_wmean(Amt, Amt)))` |
| window | `ts_quantile_q75@40->20` | +1.44 | +1.44 | +3.30 | — | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 20)), pow_2_5(day_wmean(Amt, Amt)))` |
| window | `ts_quantile_q75@40->80` | +1.41 | +1.41 | +3.29 | — | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Open), 80)), pow_2_5(day_wmean(Amt, Amt)))` |

### head score +1.47:`cross_corr(div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)), day_es_ratio_hi(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60))` | -0.36 | -0.36 | -0.26 | — | (子树本身) |
| sufficiency | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` | +1.16 | +1.16 | +2.02 | — | (子树本身) |
| sufficiency | `div(day_first(Amt), day_sum(Amt))` | -0.95 | -0.95 | +0.98 | — | (子树本身) |
| sufficiency | `day_first(Amt)` | -1.39 | -1.39 | -0.14 | — | (子树本身) |
| knockout | `div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60))` | +1.88 | +1.88 | +2.22 | -0.42 | `cross_corr(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| knockout | `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` | +0.89 | +0.89 | +1.00 | +0.58 | `cross_corr(div(day_first(Amt), div(day_first(Amt), day_sum(Amt))), day_es_ratio_hi(Amt), 60)` |
| knockout | `div(day_first(Amt), day_sum(Amt))` | +1.50 | +1.70 | +1.50 | -0.03 | `cross_corr(div(day_first(Amt), cross_corr(day_first(Amt), day_skew(Amt), 60)), day_es_ratio_hi(Amt), 60)` |
| swap | `Amt->Volume` | +1.24 | +1.28 | +1.24 | — | `cross_corr(div(day_first(Volume), cross_corr(div(day_first(Volume), day_sum(Volume)), day_skew(Volume), 60)), day_es_ratio_hi(Volume), 60)` |
| window | `cross_corr@60->30` | +0.43 | +0.43 | +2.48 | — | `cross_corr(div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)), day_es_ratio_hi(Amt), 30)` |
| window | `cross_corr@60->120` | +0.69 | +0.69 | +1.98 | — | `cross_corr(div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)), day_es_ratio_hi(Amt), 120)` |

### head score +1.21:`ts_quantile_q25(cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close))` | +1.28 | +1.28 | +2.95 | — | (子树本身) |
| sufficiency | `neg(pow_2_5(day_wmean(Amt, Amt)))` | -3.22 | -2.84 | -3.22 | — | (子树本身) |
| sufficiency | `pow_2_5(day_wmean(Amt, Amt))` | -3.22 | -2.84 | -3.22 | — | (子树本身) |
| sufficiency | `day_wmean(Amt, Amt)` | -3.22 | -2.84 | -3.22 | — | (子树本身) |
| knockout | `cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close))` | -3.45 | -2.68 | -3.45 | +4.66 | `ts_quantile_q25(neg(pow_2_5(day_wmean(Amt, Amt))), 10)` |
| knockout | `neg(pow_2_5(day_wmean(Amt, Amt)))` | -1.65 | -1.65 | -0.32 | +2.86 | `ts_quantile_q25(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), day_last(Close)), 10)` |
| knockout | `pow_2_5(day_wmean(Amt, Amt))` | +1.21 | +1.21 | +3.03 | +0.00 | `ts_quantile_q25(cs_last_low20(neg(day_wmean(Amt, Amt)), day_last(Close)), 10)` |
| swap | `Amt->Volume` | +0.82 | +0.82 | +2.44 | — | `ts_quantile_q25(cs_last_low20(neg(pow_2_5(day_wmean(Volume, Volume))), day_last(Close)), 10)` |
| swap | `Close->Vwap` | +1.20 | +1.20 | +3.03 | — | `ts_quantile_q25(cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Vwap)), 10)` |
| window | `ts_quantile_q25@10->5` | +1.21 | +1.21 | +3.00 | — | `ts_quantile_q25(cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close)), 5)` |
| window | `ts_quantile_q25@10->20` | +1.25 | +1.25 | +3.00 | — | `ts_quantile_q25(cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close)), 20)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low20(neg(pow_2_5(day_wmean(Amt, Amt))), day_last(Close))` — ablation,自身 score +1.28(所在 head +1.21)
2. `cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)` — ablation,自身 score +1.16(所在 head +1.47)
3. `day_es_ratio_hi(Amt)` — enrichment,均值差 +1.96,p 0.000
4. `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 40))` — enrichment,均值差 +1.65,p 0.000
5. `div(day_first(Amt), day_skew(Amt))` — enrichment,均值差 +1.55,p 0.001
6. `day_wmean(Volume, Volume)` — enrichment,均值差 +1.48,p 0.000
7. `pow_2_5(day_wmean(Volume, Volume))` — enrichment,均值差 +1.48,p 0.000
8. `day_skew(Amt)` — enrichment,均值差 +1.37,p 0.000
9. `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 50))` — enrichment,均值差 +1.36,p 0.014
10. `ts_quantile_q75(day_close(Open), 50)` — enrichment,均值差 +1.36,p 0.004
11. `cross_min(pow_2_5(day_wmean(Volume, Low)), 15)` — enrichment,均值差 +1.22,p 0.005
12. `ts_quantile_q75(pow_2_5(day_wmean(Volume, Volume)), 10)` — enrichment,均值差 +1.20,p 0.008
13. `pow_3(day_quantile_q75(High))` — enrichment,均值差 +1.09,p 0.004
14. `day_quantile_q75(High)` — enrichment,均值差 +1.09,p 0.004
15. `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Open), 40))` — enrichment,均值差 +1.07,p 0.000
16. `cs_last_low20(pow_2_5(day_var(Open)), ts_quantile_q75(day_close(Volume), 40))` — enrichment,均值差 +1.01,p 0.029
17. `day_first(Amt)` — enrichment,均值差 +0.97,p 0.000
18. `pow_2_5(day_wmean(Volume, Low))` — enrichment,均值差 +0.95,p 0.000
19. `cross_scale(cross_scale(LogFloatCap, 241), 241)` — enrichment,均值差 +0.94,p 0.001
20. `ts_quantile_q75(day_close(Open), 40)` — enrichment,均值差 +0.94,p 0.000
21. `day_close(Open)` — enrichment,均值差 +0.94,p 0.000
22. `pow_2_5(day_var(Open))` — enrichment,均值差 +0.92,p 0.011
23. `day_var(Open)` — enrichment,均值差 +0.92,p 0.011
24. `day_wmean(Volume, Low)` — enrichment,均值差 +0.91,p 0.000
25. `neg(ts_quantile_q75(day_close(Low), 10))` — enrichment,均值差 +0.88,p 0.001
26. `cross_mean(day_sum(Amt), 60)` — enrichment,均值差 +0.85,p 0.025
27. `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Low), 10))` — enrichment,均值差 +0.81,p 0.082
28. `cs_mask_top_replace_mean_neg(day_close(Open))` — enrichment,均值差 +0.79,p 0.000
29. `pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241))` — enrichment,均值差 +0.77,p 0.079
30. `div(day_first(Amt), day_sum(Amt))` — enrichment,均值差 +0.75,p 0.003
31. `neg(ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10))` — enrichment,均值差 +0.75,p 0.004
32. `cross_scale(LogFloatCap, 241)` — enrichment,均值差 +0.74,p 0.000
33. `ts_quantile_q75(day_close(Low), 1)` — enrichment,均值差 +0.73,p 0.011
34. `ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10)` — enrichment,均值差 +0.72,p 0.002
35. `day_close(Vwap)` — enrichment,均值差 +0.70,p 0.008
36. `cs_mask_top_replace_mean_neg(day_close(Vwap))` — enrichment,均值差 +0.65,p 0.024
37. `day_sum(Amt)` — enrichment,均值差 +0.62,p 0.001
38. `ts_quantile_q75(day_close(Volume), 40)` — enrichment,均值差 +0.59,p 0.062
39. `day_close(Volume)` — enrichment,均值差 +0.54,p 0.066
40. `day_close(Low)` — enrichment,均值差 +0.46,p 0.002
41. `ts_quantile_q75(day_close(Low), 10)` — enrichment,均值差 +0.45,p 0.003
42. `day_distinct_ratio(Low)` — enrichment,均值差 +0.38,p 0.006

## 本组之前各轮的任务

- `prods911Pr1a_Ea`:核心 `cross_scale(LogFloatCap, 241)`;评分 72,过线 0,入 heads 0;采样计数 {'c05_no_core': 908, 'c05_periphery_seen': 20, 'mutation_refused': 12}
  - score +0.31(train +0.31 valid +0.75):`pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241))`
  - score +0.31(train +0.31 valid +0.75):`neg(pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241)))`
  - score +0.31(train +0.31 valid +0.75):`pow_2(pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241)))`
  - score +0.31(train +0.31 valid +0.75):`sqrt(cross_scale(cross_scale(LogFloatCap, 241), 241))`
  - score +0.31(train +0.31 valid +0.75):`pow_1_5(cross_scale(cross_scale(LogFloatCap, 241), 241))`
- `prods911Pr1b_Nb`:核心 `—`;评分 99,过线 2,入 heads 2;采样计数 {}
  - score +0.83(train +0.83 valid +2.25):`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close)), 10)`
  - score +0.82(train +0.82 valid +2.56):`sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))`
  - score +0.22(train +0.22 valid +2.04):`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), day_last(Open)), 5)`
  - score +0.21(train +0.21 valid +2.08):`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), day_last(Close)), 5)`
  - score -0.13(train -0.13 valid +1.05):`cs_bucket_demean(sub(cross_mean(sub(div(day_first(Open), cross_delay(ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), pow_2(day_zero_ratio(Open))), 5), 1)), 1), 60), cross_age(pow_3(cs_last_low40(cross_ema(day_durbin_watson(cross_delta(Volume, 15)), 60), sigmoid(day_open(Low)))))), LogFloatCap)`
- `prods911Pr2a_Ea`:核心 `ts_quantile_q75(day_close(Low), 10)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 1212, 'mutation_refused': 4, 'c05_periphery_seen': 4}
  - score +0.46(train +0.46 valid +2.27):`cs_last_low40(neg(ts_quantile_q75(day_close(Low), 10)), cs_quantile_q75(pow_3(day_quantile_q75(High))))`
  - score +0.43(train +0.43 valid +1.99):`cs_last_low40(neg(ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10)), cs_quantile_q75(pow_3(day_quantile_q75(High))))`
  - score +0.43(train +0.43 valid +1.99):`cs_last_low40(neg(ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10)), cs_quantile_q75(pow_3(cs_quantile_q75(pow_3(day_quantile_q75(High))))))`
  - score +0.43(train +0.43 valid +1.99):`cs_last_low40(neg(ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10)), cs_quantile_q75(cs_last_low40(neg(ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10)), cs_quantile_q75(pow_3(day_quantile_q75(High))))))`
  - score +0.35(train +0.35 valid +2.00):`cs_last_low40(neg(ts_quantile_q75(ts_quantile_q75(day_close(Low), 10), 10)), cs_quantile_q75(day_close(Low)))`
- `prods911Pr2b_Nb`:核心 `—`;评分 80,过线 14,入 heads 8;采样计数 {}
  - score +1.79(train +1.80 valid +1.79):`cross_corr(div(day_first(Amt), day_es_ratio_hi(Amt)), day_es_ratio_hi(Amt), 60)`
  - score +1.78(train +1.97 valid +1.78):`cross_corr(div(day_first(Amt), day_skew(Amt)), day_es_ratio_hi(Amt), 60)`
  - score +1.67(train +1.67 valid +1.88):`cross_corr(div(day_first(Amt), day_skew(Amt)), day_skew(Amt), 60)`
  - score +1.53(train +1.53 valid +1.79):`cross_corr(day_first(Amt), day_skew(Amt), 60)`
  - score +1.47(train +1.47 valid +1.61):`cross_corr(div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60)), day_es_ratio_hi(Amt), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.42(knockout div(day_first(Amt), cross_corr(div(day_first(Amt), day_sum(Amt)), day_skew(Amt), 60))):`cross_corr(day_first(Amt), day_es_ratio_hi(Amt), 60)`
