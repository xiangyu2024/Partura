# 定位:种子 905,P 组,第 3 轮(只含 train / valid)

快照:prods905M1_I0_open_search, prods905M2_I0_open_search, prods905M3_I0_open_search, prods905Pr1a_Na, prods905Pr1b_Nb, prods905Pr2a_Ea, prods905Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +2.25 | +2.41 | +2.25 | -1 | 5 | prods905Pr2a_Ea | `cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge)` |
| +1.81 | +1.94 | +1.81 | -1 | 5 | prods905Pr2b_Nb | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| +1.47 | +1.62 | +1.47 | -1 | 20 | prods905Pr1b_Nb | `sub(cross_mean(day_centroid(Amt), 20), mul(0.5, cross_mean(day_centroid(Amt), 240)))` |
| +1.36 | +1.56 | +1.36 | -1 | 20 | prods905Pr2a_Ea | `cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 30), ListAge)` |
| +1.30 | +1.77 | +1.30 | -1 | 20 | prods905Pr1b_Nb | `cs_regres(cross_mean(day_centroid(Amt), 12), LogFloatShares)` |
| +0.91 | +0.98 | +0.91 | -1 | 20 | prods905Pr2a_Ea | `ts_quantile_q25(cs_mask_top_replace_mean_neg(day_centroid(Amt)), 20)` |
| +0.85 | +0.85 | +1.27 | -1 | 0 | prods905Pr2a_Ea | `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_rank(cross_mean(day_centroid(Amt), 30))), 20)` |
| +0.68 | +0.68 | +0.79 | +1 | 5 | prods905M3_I0_open_search | `cross_regres(cross_regres(ts_argmin(day_argmin(Ret), 50), ts_stddev(day_wmean(Ret, Amt), 30), 241), ts_stddev(day_wmean(Ret, Amt), 30), 241)` |
| +0.65 | +1.08 | +0.65 | -1 | 5 | prods905Pr2a_Ea | `cross_tail_mean_q25(day_centroid(Amt), 60)` |

## 共性:506 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.58 | 0.000 | 4 | +1.53 / -1.05 | `cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)` |
| +1.71 | 0.000 | 10 | +0.65 / -1.06 | `cross_mean(day_centroid(Amt), 10)` |
| +1.32 | 0.003 | 4 | +0.28 / -1.04 | `pow_2_5(day_centroid(Volume))` |
| +1.25 | 0.002 | 13 | +0.19 / -1.06 | `sub(day_centroid(Amt), day_flat_run_max(Amt))` |
| +1.20 | 0.001 | 16 | +0.14 / -1.07 | `day_flat_run_max(Amt)` |
| +1.17 | 0.000 | 75 | -0.03 / -1.20 | `day_centroid(Amt)` |
| +1.15 | 0.022 | 10 | +0.10 / -1.05 | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)` |
| +1.01 | 0.017 | 5 | -0.03 / -1.04 | `cs_rank(cross_mean(day_gini(Amt), 30))` |
| +1.01 | 0.017 | 5 | -0.03 / -1.04 | `cross_mean(day_gini(Amt), 30)` |
| +0.93 | 0.065 | 4 | -0.10 / -1.03 | `cross_mean(day_centroid(Amt), 30)` |
| +0.93 | 0.065 | 4 | -0.10 / -1.03 | `cs_rank(cross_mean(day_centroid(Amt), 30))` |
| +0.93 | 0.001 | 15 | -0.13 / -1.05 | `day_sum(in_slice(Amt, 211, 240))` |
| +0.90 | 0.005 | 9 | -0.14 / -1.04 | `day_centroid(Volume)` |
| +0.90 | 0.007 | 7 | -0.14 / -1.04 | `cs_mask_top_replace_mean_neg(day_centroid(Amt))` |
| +0.90 | 0.002 | 14 | -0.16 / -1.05 | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` |
| +0.80 | 0.032 | 12 | -0.24 / -1.05 | `cross_mean(day_centroid(Amt), 20)` |
| +0.77 | 0.000 | 21 | -0.29 / -1.06 | `ts_stddev(day_wmean(Ret, Amt), 50)` |
| +0.72 | 0.059 | 6 | -0.31 / -1.04 | `day_gini(Amt)` |
| +0.61 | 0.024 | 8 | -0.43 / -1.04 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| +0.58 | 0.087 | 6 | -0.46 / -1.03 | `cross_valid_count(day_argmax(Low), 30)` |

## 拆解(36 次评估)

### head score +2.25:`cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)` | +1.34 | +1.56 | +1.34 | — | (子树本身) |
| sufficiency | `sub(day_centroid(Amt), day_flat_run_max(Amt))` | +0.16 | +0.89 | +0.16 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| sufficiency | `day_flat_run_max(Amt)` | — | — | — | — | 门槛废品 |
| knockout | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)` | +1.63 | +1.63 | +1.70 | +0.62 | `cs_first_low20(sub(day_centroid(Amt), day_flat_run_max(Amt)), ListAge)` |
| knockout | `sub(day_centroid(Amt), day_flat_run_max(Amt))` | +2.07 | +2.31 | +2.07 | +0.18 | `cs_first_low20(cross_mean(day_centroid(Amt), 30), ListAge)` |
| swap | `Amt->Volume` | +2.29 | +2.45 | +2.29 | — | `cs_first_low20(cross_mean(sub(day_centroid(Volume), day_flat_run_max(Volume)), 30), ListAge)` |
| window | `cross_mean@30->15` | +2.23 | +2.27 | +2.23 | — | `cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 15), ListAge)` |
| window | `cross_mean@30->60` | +1.77 | +1.77 | +1.88 | — | `cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 60), ListAge)` |

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

### head score +1.47:`sub(cross_mean(day_centroid(Amt), 20), mul(0.5, cross_mean(day_centroid(Amt), 240)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 240)` | -0.18 | +0.64 | -0.18 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `mul(0.5, cross_mean(day_centroid(Amt), 240))` | +1.10 | +1.10 | +1.20 | +0.38 | `sub(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 240))` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +0.55 | +0.99 | +0.55 | +0.93 | `sub(day_centroid(Amt), mul(0.5, cross_mean(day_centroid(Amt), 240)))` |
| knockout | `cross_mean(day_centroid(Amt), 240)` | -0.76 | -0.76 | -0.46 | +2.23 | `sub(cross_mean(day_centroid(Amt), 20), mul(0.5, day_centroid(Amt)))` |
| swap | `Amt->Volume` | +1.51 | +1.61 | +1.51 | — | `sub(cross_mean(day_centroid(Volume), 20), mul(0.5, cross_mean(day_centroid(Volume), 240)))` |
| window | `cross_mean@20->10` | +1.34 | +2.07 | +1.34 | — | `sub(cross_mean(day_centroid(Amt), 10), mul(0.5, cross_mean(day_centroid(Amt), 240)))` |
| window | `cross_mean@20->40` | +1.17 | +1.38 | +1.17 | — | `sub(cross_mean(day_centroid(Amt), 40), mul(0.5, cross_mean(day_centroid(Amt), 240)))` |

### head score +1.36:`cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 30), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 30)` | +1.36 | +1.57 | +1.36 | — | (子树本身) |
| sufficiency | `sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt))` | +1.48 | +1.48 | +1.54 | — | (子树本身) |
| sufficiency | `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20)` | +1.38 | +1.38 | +1.39 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge))` | +1.72 | +1.72 | +2.54 | — | (子树本身) |
| knockout | `cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 30)` | +1.47 | +1.47 | +1.49 | -0.12 | `cs_first_low20(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), ListAge)` |
| knockout | `sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt))` | +1.18 | +1.57 | +1.18 | +0.18 | `cs_first_low20(cross_mean(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), 30), ListAge)` |
| knockout | `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20)` | +1.98 | +1.98 | +2.86 | -0.62 | `cs_first_low20(cross_mean(sub(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), day_flat_run_max(Amt)), 30), ListAge)` |
| knockout | `cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge))` | +1.47 | +1.47 | +1.92 | -0.12 | `cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge), 20), day_flat_run_max(Amt)), 30), ListAge)` |
| swap | `Amt->Volume` | +1.32 | +1.52 | +1.32 | — | `cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Volume), 10), ListAge)), 20), day_flat_run_max(Volume)), 30), ListAge)` |
| window | `cross_mean@30->15` | +1.46 | +1.56 | +1.46 | — | `cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 15), ListAge)` |
| window | `cross_mean@30->60` | +1.45 | +1.45 | +1.59 | — | `cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 60), ListAge)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge))` — ablation,自身 score +1.72(所在 head +1.36)
2. `sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt))` — ablation,自身 score +1.48(所在 head +1.36)
3. `ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20)` — ablation,自身 score +1.38(所在 head +1.36)
4. `cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 30)` — ablation,自身 score +1.36(所在 head +1.36)
5. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +1.47)
6. `cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)` — enrichment,均值差 +2.58,p 0.000
7. `cross_mean(day_centroid(Amt), 10)` — enrichment,均值差 +1.71,p 0.000
8. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.32,p 0.003
9. `sub(day_centroid(Amt), day_flat_run_max(Amt))` — enrichment,均值差 +1.25,p 0.002
10. `day_flat_run_max(Amt)` — enrichment,均值差 +1.20,p 0.001
11. `day_centroid(Amt)` — enrichment,均值差 +1.17,p 0.000
12. `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)` — enrichment,均值差 +1.15,p 0.022
13. `cs_rank(cross_mean(day_gini(Amt), 30))` — enrichment,均值差 +1.01,p 0.017
14. `cross_mean(day_gini(Amt), 30)` — enrichment,均值差 +1.01,p 0.017
15. `cross_mean(day_centroid(Amt), 30)` — enrichment,均值差 +0.93,p 0.065
16. `cs_rank(cross_mean(day_centroid(Amt), 30))` — enrichment,均值差 +0.93,p 0.065
17. `day_sum(in_slice(Amt, 211, 240))` — enrichment,均值差 +0.93,p 0.001
18. `day_centroid(Volume)` — enrichment,均值差 +0.90,p 0.005
19. `cs_mask_top_replace_mean_neg(day_centroid(Amt))` — enrichment,均值差 +0.90,p 0.007
20. `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` — enrichment,均值差 +0.90,p 0.002
21. `ts_stddev(day_wmean(Ret, Amt), 50)` — enrichment,均值差 +0.77,p 0.000
22. `day_gini(Amt)` — enrichment,均值差 +0.72,p 0.059
23. `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` — enrichment,均值差 +0.61,p 0.024
24. `cross_valid_count(day_argmax(Low), 30)` — enrichment,均值差 +0.58,p 0.087
25. `cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap)))` — enrichment,均值差 +0.54,p 0.003
26. `cross_regres(ts_argmin(day_argmin(Ret), 50), ts_stddev(day_wmean(Ret, Amt), 50), 241)` — enrichment,均值差 +0.53,p 0.034
27. `cs_rank(sub(LogTotalCap, LogFloatCap))` — enrichment,均值差 +0.52,p 0.001
28. `pow_2(LogFloatShares)` — enrichment,均值差 +0.50,p 0.080
29. `inv(LogFloatShares)` — enrichment,均值差 +0.49,p 0.089
30. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +0.48,p 0.002
31. `day_zero_ratio(Volume)` — enrichment,均值差 +0.46,p 0.047
32. `ts_argmin(day_argmin(Ret), 50)` — enrichment,均值差 +0.41,p 0.014
33. `day_argmin(Ret)` — enrichment,均值差 +0.40,p 0.008
34. `day_wmean(Ret, Amt)` — enrichment,均值差 +0.39,p 0.001
35. `day_sum(Amt)` — enrichment,均值差 +0.17,p 0.055

## 本组之前各轮的任务

- `prods905Pr1a_Na`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {}
  - score -0.35(train -0.35 valid +0.37):`sub(LogTotalCap, LogFloatCap)`
  - score -0.40(train -0.40 valid +0.53):`add(cs_rank(sub(cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap))), LogFloatShares)), cs_rank(sub(LogTotalCap, LogFloatCap)))`
  - score -0.42(train -0.42 valid +0.16):`add(ts_quantile_q75(sub(LogTotalCap, LogFloatCap), 50), cs_rank(ts_quantile_q75(sub(LogTotalCap, LogFloatCap), 50)))`
  - score -0.48(train -0.48 valid +0.15):`add(cs_median(sub(LogFloatCap, LogFloatShares)), cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap))))`
  - score -0.48(train -0.48 valid +0.15):`add(cs_median(add(LogFloatCap, cs_rank(sub(LogTotalCap, LogFloatCap)))), cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap))))`
- `prods905Pr1b_Nb`:核心 `—`;评分 87,过线 3,入 heads 2;采样计数 {}
  - score +0.80(train +1.48 valid +0.80):`pow_2_5(cross_mean(day_centroid(Amt), 3))`
  - score +0.66(train +0.66 valid +0.78):`cross_zscore(cross_mean(day_centroid(Amt), 20), 120)`
  - score +0.61(train +0.61 valid +0.76):`cross_zscore(cross_mean(day_centroid(Volume), 20), 120)`
  - score +0.48(train +0.48 valid +0.75):`cross_zscore(cross_mean(day_centroid(Amt), 10), 120)`
  - score +0.44(train +1.09 valid +0.44):`pow_2_5(day_centroid(Volume))`
- `prods905Pr2a_Ea`:核心 `day_centroid(Amt)`;评分 95,过线 25,入 heads 5;采样计数 {'c05_no_core': 1183, 'c05_periphery_seen': 6}
  - score +2.25(train +2.41 valid +2.25):`cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge)`
  - score +2.16(train +2.26 valid +2.16):`cs_first_low20(cross_mean(cs_first_low20(cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30), ListAge), 15), ListAge)`
  - score +2.07(train +2.10 valid +2.07):`ts_quantile_q25(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge), 20)`
  - score +1.93(train +2.09 valid +1.93):`cs_first_low20(cross_mean(cross_mean(day_centroid(Amt), 20), 20), ListAge)`
  - score +1.80(train +2.52 valid +1.80):`cs_first_low20(cross_mean(day_centroid(Amt), 20), ListAge)`
- `prods905Pr2b_Nb`:核心 `—`;评分 76,过线 7,入 heads 1;采样计数 {}
  - score +1.81(train +1.94 valid +1.81):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)`
  - score +1.49(train +1.78 valid +1.49):`cs_regres(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)`
  - score +1.49(train +1.78 valid +1.49):`cs_regres(cs_regres(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares), LogFloatShares)`
  - score +1.44(train +1.44 valid +2.19):`cs_regres(cross_mean(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), 20), LogFloatShares)`
  - score +1.24(train +1.64 valid +1.24):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 5)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.62(knockout ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20)):`cs_first_low20(cross_mean(sub(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), day_flat_run_max(Amt)), 30), ListAge)`
- 增益 +0.12(knockout cross_mean(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), 30)):`cs_first_low20(sub(ts_quantile_q25(cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge)), 20), day_flat_run_max(Amt)), ListAge)`
- 增益 +0.12(knockout cs_mask_top_replace_mean_neg(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge))):`cs_first_low20(cross_mean(sub(ts_quantile_q25(cs_first_low20(cross_mean(day_centroid(Amt), 10), ListAge), 20), day_flat_run_max(Amt)), 30), ListAge)`
