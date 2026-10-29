# 定位:种子 806,B 组,第 3 轮(只含 train / valid)

快照:c05s806M1_I0_open_search, c05s806M2_I0_open_search, c05s806M3_I0_open_search, c05s806Br1a_Ea, c05s806Br1b_Nb, c05s806Br2a_Ea, c05s806Br2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +2.11 | +2.11 | +2.39 | +1 | 20 | c05s806M2_I0_open_search | `sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))` |
| +1.40 | +1.40 | +3.15 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` |
| +1.32 | +1.32 | +3.02 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` |
| +1.22 | +1.22 | +1.34 | -1 | 5 | c05s806M2_I0_open_search | `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` |
| +1.18 | +1.18 | +2.76 | +1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))` |
| +1.13 | +1.30 | +1.13 | +1 | 0 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))` |
| +0.97 | +0.97 | +1.54 | -1 | 20 | c05s806Br1b_Nb | `day_kurt(Ret)` |
| +0.82 | +0.82 | +1.29 | -1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(ts_quantile_q50(cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)), 10))` |
| +0.81 | +0.81 | +2.58 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))` |
| +0.63 | +0.63 | +2.03 | -1 | 5 | c05s806Br2a_Ea | `sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 50)), cs_rank(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20))), day_sum(Amt)), 20)))` |
| +0.59 | +0.59 | +2.04 | +1 | 20 | c05s806Br2a_Ea | `div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20), 40))), day_sum(Amt))` |

## 共性:465 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.47 | 0.000 | 16 | +0.48 / -0.99 | `pow_05(LogFloatShares)` |
| +1.45 | 0.000 | 15 | +0.47 / -0.98 | `ts_quantile_q50(day_centroid(Amt), 10)` |
| +1.45 | 0.011 | 4 | +0.50 / -0.95 | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` |
| +1.44 | 0.000 | 7 | +0.48 / -0.96 | `pow_1_5(LogFloatShares)` |
| +1.44 | 0.001 | 7 | +0.48 / -0.96 | `pow_05(pow_05(LogFloatShares))` |
| +1.43 | 0.002 | 5 | +0.48 / -0.95 | `abs_(LogFloatShares)` |
| +1.43 | 0.012 | 4 | +0.48 / -0.95 | `pow_05(pow_05(pow_05(LogFloatShares)))` |
| +1.36 | 0.018 | 4 | +0.41 / -0.95 | `cross_mean(day_kurt(Ret), 30)` |
| +1.27 | 0.001 | 9 | +0.31 / -0.96 | `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` |
| +1.23 | 0.001 | 12 | +0.26 / -0.97 | `log(day_open(Low))` |
| +1.22 | 0.011 | 5 | +0.27 / -0.95 | `cs_last_low40(LogFloatCap, day_quantile(Vwap))` |
| +1.13 | 0.026 | 7 | +0.18 / -0.95 | `day_quantile_q75(Amt)` |
| +1.10 | 0.001 | 16 | +0.13 / -0.97 | `day_open(Low)` |
| +1.08 | 0.037 | 4 | +0.13 / -0.95 | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` |
| +1.06 | 0.018 | 6 | +0.11 / -0.95 | `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` |
| +1.04 | 0.010 | 10 | +0.08 / -0.96 | `day_quantile_q75(pow_2_5(Close))` |
| +0.86 | 0.005 | 15 | -0.10 / -0.96 | `cs_rank(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20))` |
| +0.84 | 0.040 | 6 | -0.11 / -0.95 | `cross_decay_linear(cross_argmin(ListAge, 60), 241)` |
| +0.84 | 0.040 | 6 | -0.11 / -0.95 | `cross_argmin(ListAge, 60)` |
| +0.80 | 0.006 | 20 | -0.18 / -0.97 | `day_open(Open)` |

## 拆解(14 次评估)

### head score +2.11:`sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low40(LogFloatCap, day_quantile_q75(Amt))` | -2.08 | -0.30 | -2.08 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -1.19 | -1.19 | +0.47 | — | (子树本身) |
| knockout | `cs_last_low40(LogFloatCap, day_quantile_q75(Amt))` | -3.05 | -1.81 | -3.05 | +5.16 | `sqrt(LogFloatCap)` |
| swap | `Amt->Volume` | +0.56 | +1.50 | +0.56 | — | `sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Volume)))` |

### head score +1.18:`cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q75(pow_2_5(Amt))` | -0.46 | -0.46 | +0.75 | — | (子树本身) |
| swap | `Amt->Volume` | — | — | — | — | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Volume)))` |

### head score +1.13:`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3)` | -0.40 | -0.40 | +0.90 | — | (子树本身) |
| sufficiency | `cs_last_low40(LogFloatCap, day_quantile(Low))` | -0.37 | -0.37 | +1.04 | — | (子树本身) |
| sufficiency | `day_quantile(Low)` | -1.15 | -1.15 | -0.44 | — | (子树本身) |
| knockout | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3)` | +1.23 | +1.36 | +1.23 | -0.10 | `sqrt(cs_last_low40(LogFloatCap, day_quantile(Low)))` |
| knockout | `cs_last_low40(LogFloatCap, day_quantile(Low))` | -3.01 | -1.93 | -3.01 | +4.15 | `sqrt(cross_quantile_q25(LogFloatCap, 3))` |
| swap | `Low->High` | +1.11 | +1.31 | +1.11 | — | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(High)), 3))` |
| window | `cross_quantile_q25@3->2` | +1.26 | +1.35 | +1.26 | — | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 2))` |
| window | `cross_quantile_q25@3->6` | +1.00 | +1.10 | +1.00 | — | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 6))` |

### head score +0.97:`day_kurt(Ret)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

## 机械核心卡(B0 按这个顺序取)

1. `pow_05(LogFloatShares)` — enrichment,均值差 +1.47,p 0.000
2. `ts_quantile_q50(day_centroid(Amt), 10)` — enrichment,均值差 +1.45,p 0.000
3. `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` — enrichment,均值差 +1.45,p 0.011
4. `pow_1_5(LogFloatShares)` — enrichment,均值差 +1.44,p 0.000
5. `pow_05(pow_05(LogFloatShares))` — enrichment,均值差 +1.44,p 0.001
6. `abs_(LogFloatShares)` — enrichment,均值差 +1.43,p 0.002
7. `pow_05(pow_05(pow_05(LogFloatShares)))` — enrichment,均值差 +1.43,p 0.012
8. `cross_mean(day_kurt(Ret), 30)` — enrichment,均值差 +1.36,p 0.018
9. `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` — enrichment,均值差 +1.27,p 0.001
10. `log(day_open(Low))` — enrichment,均值差 +1.23,p 0.001
11. `cs_last_low40(LogFloatCap, day_quantile(Vwap))` — enrichment,均值差 +1.22,p 0.011
12. `day_quantile_q75(Amt)` — enrichment,均值差 +1.13,p 0.026
13. `day_open(Low)` — enrichment,均值差 +1.10,p 0.001
14. `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` — enrichment,均值差 +1.08,p 0.037
15. `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` — enrichment,均值差 +1.06,p 0.018
16. `day_quantile_q75(pow_2_5(Close))` — enrichment,均值差 +1.04,p 0.010
17. `cs_rank(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20))` — enrichment,均值差 +0.86,p 0.005
18. `cross_decay_linear(cross_argmin(ListAge, 60), 241)` — enrichment,均值差 +0.84,p 0.040
19. `cross_argmin(ListAge, 60)` — enrichment,均值差 +0.84,p 0.040
20. `day_open(Open)` — enrichment,均值差 +0.80,p 0.006
21. `ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20)` — enrichment,均值差 +0.78,p 0.004
22. `day_last(Amt)` — enrichment,均值差 +0.78,p 0.001
23. `day_kurt(Ret)` — enrichment,均值差 +0.78,p 0.008
24. `day_corr(in_index(Ret), Ret)` — enrichment,均值差 +0.75,p 0.042
25. `div(day_last(Amt), day_sum(Amt))` — enrichment,均值差 +0.74,p 0.003
26. `ts_quantile_q50(day_wmean(Ret, Amt), 20)` — enrichment,均值差 +0.70,p 0.019
27. `day_sum(Amt)` — enrichment,均值差 +0.68,p 0.004
28. `cs_rank(ts_quantile_q50(day_centroid(Amt), 20))` — enrichment,均值差 +0.62,p 0.005
29. `day_wmean(Ret, Amt)` — enrichment,均值差 +0.61,p 0.009
30. `cs_normalize(day_open(Open))` — enrichment,均值差 +0.61,p 0.096
31. `day_centroid(Amt)` — enrichment,均值差 +0.54,p 0.000

## 本组之前各轮的任务

- `c05s806Br1a_Ea`:核心 `day_cov(Vwap, Ret)`;评分 73,过线 0,入 heads 0;采样计数 {'c05_no_core': 1269, 'c05_periphery_seen': 8}
  - score +0.01(train +0.01 valid +0.19):`ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40)`
  - score -0.25(train -0.25 valid +1.18):`inv(ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 20))`
  - score -0.30(train -0.30 valid +0.48):`inv(cross_decay_linear(ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40), 241))`
  - score -0.36(train -0.36 valid +0.96):`inv(ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40))`
  - score -0.65(train -0.65 valid -0.00):`cs_last_low40(day_cov(Vwap, Ret), day_wmean(High, Vwap))`
- `c05s806Br1b_Nb`:核心 `—`;评分 68,过线 2,入 heads 1;采样计数 {}
  - score +0.97(train +0.97 valid +1.54):`day_kurt(Ret)`
  - score +0.61(train +0.61 valid +1.25):`cross_mean(day_kurt(Ret), 30)`
  - score +0.46(train +0.46 valid +2.03):`cross_mean(cross_mean(cross_ema(cross_mean(day_kurt(Ret), 20), 10), 20), 20)`
  - score +0.46(train +0.46 valid +1.99):`cross_mean(cross_mean(day_kurt(Ret), 30), 30)`
  - score +0.46(train +0.46 valid +1.89):`cross_mean(cross_mean(cross_mean(day_kurt(Ret), 30), 20), 20)`
- `c05s806Br2a_Ea`:核心 `ts_quantile_q50(day_centroid(Amt), 20)`;评分 96,过线 2,入 heads 2;采样计数 {'c05_no_core': 1815, 'c05_skeleton': 22, 'mutation_refused': 2, 'c05_periphery_seen': 5}
  - score +0.63(train +0.63 valid +2.03):`sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 50)), cs_rank(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20))), day_sum(Amt)), 20)))`
  - score +0.59(train +0.59 valid +2.04):`div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20), 40))), day_sum(Amt))`
  - score +0.41(train +0.41 valid +1.68):`sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20))), day_sum(Amt)), 20)))`
  - score +0.37(train +1.11 valid +0.37):`sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 50)), cs_rank(ts_quantile_q50(div(day_last(Amt), day_q_stat_std(Amt)), 20))), day_q_stat_std(Amt)), 20)))`
  - score +0.32(train +0.32 valid +2.26):`div(sub(cs_rank(ts_quantile_q50(day_centroid(Amt), 20)), cs_rank(ts_quantile_q50(div(day_last(Amt), day_sum(Amt)), 20))), day_sum(Amt))`
- `c05s806Br2b_Nb`:核心 `—`;评分 74,过线 0,入 heads 0;采样计数 {}
  - score +0.31(train +0.31 valid +1.31):`ts_quantile_q50(ts_quantile_q50(day_wmean(Ret, Amt), 20), 20)`
  - score +0.31(train +0.31 valid +1.31):`ts_quantile_q50(ts_quantile_q50(ts_quantile_q50(day_wmean(Ret, Amt), 1), 20), 20)`
  - score +0.26(train +0.26 valid +1.54):`ts_sum(ts_quantile_q50(day_wmean(Ret, Amt), 20), 20)`
  - score +0.24(train +0.24 valid +1.23):`ts_sum(ts_quantile_q50(ts_quantile_q50(day_wmean(Ret, Amt), 20), 20), 20)`
  - score +0.23(train +0.23 valid +1.43):`cs_last_low20(cross_decay_linear(cross_argmin(ListAge, 60), 241), cross_max(cs_rank(day_wmean(Ret, Amt)), 241))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.12(window cross_quantile_q25@3->2):`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 2))`
