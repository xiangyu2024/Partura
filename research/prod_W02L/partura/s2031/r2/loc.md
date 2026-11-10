# 定位:种子 2031,P 组,第 2 轮(只含 train / valid)

快照:prods2031M1_I0_open_search, prods2031M2_I0_open_search, prods2031Pr1a_Ea, prods2031Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.92 | -0.88 | -0.92 | +1 | 5 | prods2031M1_I0_open_search | `cross_ema(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), 60)` |
| -1.66 | -1.66 | -1.27 | +1 | 0 | prods2031M2_I0_open_search | `cs_mask_top_replace_mean_neg(cross_product(ts_argmin(day_first(Volume), 30), 60))` |
| -2.08 | -2.08 | -1.79 | -1 | 20 | prods2031M1_I0_open_search | `ts_mean(select_where(is_gt(div(sub(day_sum(Volume), cross_delay(day_sum(Volume), 1)), cross_delay(day_sum(Volume), 1)), cs_mean(div(sub(day_sum(Volume), cross_delay(day_sum(Volume), 1)), cross_delay(day_sum(Volume), 1))), False), neg(cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 20)), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 20)), 20)` |
| -2.26 | -2.26 | -1.14 | +1 | 20 | prods2031M2_I0_open_search | `ts_scale(ts_argmin(day_first(Amt), 30), 30)` |
| -2.28 | -2.28 | -2.24 | -1 | 20 | prods2031M1_I0_open_search | `add(select_where(is_gt(cross_stddev(sub(div(day_last(Close), day_first(Open)), 1), 20), cs_mean(cross_stddev(sub(div(day_last(Close), day_first(Open)), 1), 20)), False), neg(cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 20)), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 20)), ts_mean(select_where(is_gt(div(sub(day_sum(Volume), cross_delay(day_sum(Volume), 1)), cross_delay(day_sum(Volume), 1)), cs_mean(div(sub(day_sum(Volume), cross_delay(day_sum(Volume), 1)), cross_delay(day_sum(Volume), 1))), False), neg(cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 20)), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 20)), 20))` |
| -3.63 | -3.33 | -3.63 | -1 | 20 | prods2031M2_I0_open_search | `ts_scale(ts_argmin(day_first(Vwap), 30), 30)` |

## 共性:149 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.27 | 0.000 | 32 | -0.10 / -2.38 | `day_last(Low)` |
| +2.27 | 0.000 | 32 | -0.10 / -2.38 | `cross_delay(day_last(Low), 1)` |
| +2.24 | 0.000 | 31 | -0.11 / -2.35 | `div(day_first(Open), cross_delay(day_last(Low), 1))` |
| +2.21 | 0.000 | 29 | -0.11 / -2.32 | `cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120)` |
| +2.21 | 0.000 | 29 | -0.11 / -2.32 | `cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120)` |
| +2.16 | 0.002 | 4 | +0.21 / -1.95 | `div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), day_first(Open))` |
| +2.16 | 0.002 | 4 | +0.21 / -1.95 | `cs_mean(div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), day_first(Open)))` |
| +2.04 | 0.000 | 34 | -0.31 / -2.35 | `cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120), 120)` |
| +2.02 | 0.000 | 35 | -0.34 / -2.36 | `cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)` |
| +1.94 | 0.000 | 52 | -0.63 / -2.56 | `cs_mean(div(day_last(Close), day_first(Open)))` |
| +1.85 | 0.000 | 59 | -0.77 / -2.62 | `cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1)))` |
| +1.83 | 0.002 | 5 | -0.12 / -1.95 | `cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)` |
| +1.75 | 0.001 | 6 | -0.21 / -1.96 | `div(day_first(Open), cross_delay(day_last(Close), 10))` |
| +1.75 | 0.001 | 6 | -0.21 / -1.96 | `cross_delay(day_last(Close), 10)` |
| +1.73 | 0.007 | 4 | -0.20 / -1.93 | `div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)), cross_delay(day_last(Close), 1))` |
| +1.73 | 0.007 | 4 | -0.20 / -1.93 | `cross_regres(cross_delay(day_last(Close), 1), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)), cross_delay(day_last(Close), 1)), 120)` |
| +1.73 | 0.007 | 4 | -0.20 / -1.93 | `sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60))` |
| +1.73 | 0.000 | 27 | -0.47 / -2.20 | `cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120)` |
| +1.66 | 0.004 | 5 | -0.28 / -1.94 | `cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120)` |
| +1.66 | 0.004 | 5 | -0.28 / -1.94 | `div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120), cross_corr(cs_mean(cs_mean(div(day_last(Close), day_first(Open)))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1))` |

## 拆解(31 次评估)

### head score -0.92:`cross_ema(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_first(Open), cross_delay(day_last(Close), 1))` | -3.94 | -3.94 | -3.84 | — | (子树本身) |
| sufficiency | `cross_delay(day_last(Close), 1)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_first(Open)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| sufficiency | `day_last(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)` | -2.36 | -2.36 | -1.70 | +1.44 | `cross_ema(abs_(div(day_first(Open), cross_delay(day_last(Close), 1))), 60)` |
| knockout | `div(day_first(Open), cross_delay(day_last(Close), 1))` | -2.33 | -1.66 | -2.33 | +1.41 | `cross_ema(abs_(sub(day_first(Open), 1)), 60)` |
| knockout | `cross_delay(day_last(Close), 1)` | -2.31 | -2.02 | -2.31 | +1.38 | `cross_ema(abs_(sub(div(day_first(Open), day_last(Close)), 1)), 60)` |
| swap | `Open->Close` | -0.92 | -0.90 | -0.92 | — | `cross_ema(abs_(sub(div(day_first(Close), cross_delay(day_last(Close), 1)), 1)), 60)` |
| swap | `Close->Vwap` | -1.05 | -1.05 | -0.96 | — | `cross_ema(abs_(sub(div(day_first(Open), cross_delay(day_last(Vwap), 1)), 1)), 60)` |
| window | `cross_ema@60->30` | -1.66 | -0.84 | -1.66 | — | `cross_ema(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), 30)` |
| window | `cross_ema@60->120` | -1.20 | -1.20 | -0.36 | — | `cross_ema(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), 120)` |

### head score -1.66:`cs_mask_top_replace_mean_neg(cross_product(ts_argmin(day_first(Volume), 30), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_product(ts_argmin(day_first(Volume), 30), 60)` | -1.36 | -1.36 | -1.14 | — | (子树本身) |
| sufficiency | `ts_argmin(day_first(Volume), 30)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cross_product(ts_argmin(day_first(Volume), 30), 60)` | — | — | — | — | `cs_mask_top_replace_mean_neg(ts_argmin(day_first(Volume), 30))` |
| knockout | `ts_argmin(day_first(Volume), 30)` | — | — | — | — | `cs_mask_top_replace_mean_neg(cross_product(day_first(Volume), 60))` |
| swap | `Volume->Amt` | -1.35 | -1.35 | -1.23 | — | `cs_mask_top_replace_mean_neg(cross_product(ts_argmin(day_first(Amt), 30), 60))` |
| window | `cross_product@60->30` | -1.73 | -1.73 | -1.61 | — | `cs_mask_top_replace_mean_neg(cross_product(ts_argmin(day_first(Volume), 30), 30))` |
| window | `cross_product@60->120` | — | — | — | — | `cs_mask_top_replace_mean_neg(cross_product(ts_argmin(day_first(Volume), 30), 120))` |

### head score -2.26:`ts_scale(ts_argmin(day_first(Amt), 30), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_argmin(day_first(Amt), 30)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_first(Amt)` | -1.30 | -1.30 | -0.79 | — | (子树本身) |
| knockout | `ts_argmin(day_first(Amt), 30)` | -2.74 | -2.74 | -1.83 | +0.47 | `ts_scale(day_first(Amt), 30)` |
| swap | `Amt->Volume` | -1.99 | -1.99 | -1.01 | — | `ts_scale(ts_argmin(day_first(Volume), 30), 30)` |
| window | `ts_scale@30->15` | — | — | — | — | `ts_scale(ts_argmin(day_first(Amt), 30), 15)` |
| window | `ts_scale@30->60` | -2.30 | -2.30 | -1.51 | — | `ts_scale(ts_argmin(day_first(Amt), 30), 60)` |

### head score -3.63:`ts_scale(ts_argmin(day_first(Vwap), 30), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_argmin(day_first(Vwap), 30)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_first(Vwap)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `ts_argmin(day_first(Vwap), 30)` | -3.06 | -2.48 | -3.06 | -0.56 | `ts_scale(day_first(Vwap), 30)` |
| swap | `Vwap->Close` | -3.63 | -3.28 | -3.63 | — | `ts_scale(ts_argmin(day_first(Close), 30), 30)` |
| window | `ts_scale@30->15` | — | — | — | — | `ts_scale(ts_argmin(day_first(Vwap), 30), 15)` |
| window | `ts_scale@30->60` | -2.80 | -2.59 | -2.80 | — | `ts_scale(ts_argmin(day_first(Vwap), 30), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_last(Low)` — enrichment,均值差 +2.27,p 0.000
2. `cross_delay(day_last(Low), 1)` — enrichment,均值差 +2.27,p 0.000
3. `div(day_first(Open), cross_delay(day_last(Low), 1))` — enrichment,均值差 +2.24,p 0.000
4. `cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120)` — enrichment,均值差 +2.21,p 0.000
5. `cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120)` — enrichment,均值差 +2.21,p 0.000
6. `div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), day_first(Open))` — enrichment,均值差 +2.16,p 0.002
7. `cs_mean(div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), day_first(Open)))` — enrichment,均值差 +2.16,p 0.002
8. `cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120), 120)` — enrichment,均值差 +2.04,p 0.000
9. `cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)` — enrichment,均值差 +2.02,p 0.000
10. `cs_mean(div(day_last(Close), day_first(Open)))` — enrichment,均值差 +1.94,p 0.000
11. `cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1)))` — enrichment,均值差 +1.85,p 0.000
12. `cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)` — enrichment,均值差 +1.83,p 0.002
13. `div(day_first(Open), cross_delay(day_last(Close), 10))` — enrichment,均值差 +1.75,p 0.001
14. `cross_delay(day_last(Close), 10)` — enrichment,均值差 +1.75,p 0.001
15. `div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)), cross_delay(day_last(Close), 1))` — enrichment,均值差 +1.73,p 0.007
16. `cross_regres(cross_delay(day_last(Close), 1), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)), cross_delay(day_last(Close), 1)), 120)` — enrichment,均值差 +1.73,p 0.007
17. `sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60))` — enrichment,均值差 +1.73,p 0.007
18. `cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120)` — enrichment,均值差 +1.73,p 0.000
19. `cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120)` — enrichment,均值差 +1.66,p 0.004
20. `div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120), cross_corr(cs_mean(cs_mean(div(day_last(Close), day_first(Open)))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1))` — enrichment,均值差 +1.66,p 0.004
21. `sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120), cross_corr(cs_mean(cs_mean(div(day_last(Close), day_first(Open)))), div(day_last(Close), day_first(Open)), 120))` — enrichment,均值差 +1.66,p 0.004
22. `cross_corr(cs_mean(cs_mean(div(day_last(Close), day_first(Open)))), div(day_last(Close), day_first(Open)), 120)` — enrichment,均值差 +1.66,p 0.004
23. `cs_mean(cs_mean(div(day_last(Close), day_first(Open))))` — enrichment,均值差 +1.66,p 0.004
24. `div(day_last(Open), day_first(Open))` — enrichment,均值差 +1.65,p 0.009
25. `div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1))` — enrichment,均值差 +1.59,p 0.000
26. `sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120))` — enrichment,均值差 +1.59,p 0.000
27. `div(day_last(Close), day_first(Open))` — enrichment,均值差 +1.56,p 0.000
28. `cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)` — enrichment,均值差 +1.51,p 0.000
29. `day_last(Open)` — enrichment,均值差 +1.50,p 0.003
30. `div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1))` — enrichment,均值差 +1.42,p 0.009
31. `cross_delay(cross_delay(day_last(Close), 1), 1)` — enrichment,均值差 +1.42,p 0.006
32. `cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120)` — enrichment,均值差 +1.39,p 0.002
33. `cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), 120)` — enrichment,均值差 +1.39,p 0.002
34. `add(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1)), 120), 120), cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120), 120))` — enrichment,均值差 +1.31,p 0.052
35. `cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1)), 120)` — enrichment,均值差 +1.24,p 0.017
36. `cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1)), 120), 120)` — enrichment,均值差 +1.24,p 0.017
37. `day_min(Low)` — enrichment,均值差 +0.77,p 0.063
38. `day_max(High)` — enrichment,均值差 +0.74,p 0.069
39. `div(day_max(High), day_min(Low))` — enrichment,均值差 +0.70,p 0.093

## 本组之前各轮的任务

- `prods2031Pr1a_Ea`:核心 `div(day_first(Open), cross_delay(day_last(Close), 1))`;评分 100,过线 0,入 heads 0;采样计数 {'c05_skeleton': 530, 'c05_no_core': 1049, 'c05_periphery_seen': 3, 'mutation_refused': 2}
  - score -0.46(train +0.00 valid -0.46):`cross_mean(div(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), add(abs_(sub(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1)), 1)), sub(div(day_max(High), day_min(Low)), 1))), 60)`
  - score -0.46(train +0.00 valid -0.46):`cross_mean(div(abs_(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1))), add(abs_(sub(div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1)), 1)), sub(div(day_max(High), day_min(Low)), 1))), 60)`
  - score -0.50(train +0.31 valid -0.50):`cross_mean(div(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), add(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), sub(div(day_max(High), day_min(Low)), 1))), 60)`
  - score -0.50(train +0.31 valid -0.50):`cross_mean(div(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), add(abs_(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1))), sub(div(day_max(High), day_min(Low)), 1))), 60)`
  - score -0.52(train +0.29 valid -0.52):`cross_mean(div(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), add(abs_(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), sub(div(day_max(Close), day_min(Low)), 1))), 60)`
- `prods2031Pr1b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score +0.50(train +0.50 valid +0.66):`div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), add(cross_stddev(cross_regres(cross_delay(day_last(Close), 1), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)), cross_delay(day_last(Close), 1)), 120), 120), cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 10), 120)))`
  - score +0.49(train +0.49 valid +0.74):`div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), add(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(cross_delay(day_last(Close), 1), 1)), 120), cross_corr(cs_mean(div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), day_first(Open))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1)), 120), 120), cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 5), 120)))`
  - score +0.31(train +0.31 valid +0.35):`div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), add(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120), cross_corr(cs_mean(cs_mean(div(day_last(Close), day_first(Open)))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1)), 120), 120), cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120), 120)))`
  - score +0.31(train +0.31 valid +0.36):`div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), 120), add(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 10)), 120), cross_corr(cs_mean(cs_mean(div(day_last(Close), day_first(Open)))), div(day_last(Close), day_first(Open)), 120)), cross_delay(day_last(Close), 1)), 120), 120), cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120), 120)))`
  - score +0.29(train +0.29 valid +0.56):`div(cross_stddev(cross_regres(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Low), 1)), 120), 120), add(cross_stddev(cross_regres(cross_delay(day_last(Close), 1), div(sub(cross_corr(cs_mean(div(day_first(Open), cross_delay(day_last(Close), 1))), div(day_first(Open), cross_delay(day_last(Close), 1)), 120), cross_corr(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 60)), cross_delay(day_last(Close), 1)), 120), 120), cross_stddev(cross_regres(cs_mean(div(day_last(Close), day_first(Open))), div(day_last(Close), day_first(Open)), 120), 120)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.31(swap Volume->Amt):`cs_mask_top_replace_mean_neg(cross_product(ts_argmin(day_first(Amt), 30), 60))`
- 增益 +0.28(swap Amt->Volume):`ts_scale(ts_argmin(day_first(Volume), 30), 30)`
