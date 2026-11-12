# 定位:种子 2069,P 组,第 3 轮(只含 train / valid)

快照:prods2069M1_I0_open_search, prods2069M2_I0_open_search, prods2069M3_I0_open_search, prods2069Pr1a_Ea, prods2069Pr1b_Nb, prods2069Pr2a_Ea, prods2069Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.91 | -1.91 | -1.21 | +1 | 5 | prods2069M3_I0_open_search | `cross_stddev(day_corr(Close, in_shift(Volume, 1)), 20)` |
| -1.92 | -1.45 | -1.92 | -1 | 5 | prods2069M2_I0_open_search | `cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)` |
| -2.28 | -2.28 | -1.85 | +1 | 20 | prods2069M3_I0_open_search | `cross_mean(day_corr(Close, in_shift(Volume, 1)), 20)` |
| -2.31 | -2.16 | -2.31 | -1 | 20 | prods2069M1_I0_open_search | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_sum(Amt), day_sum(Volume)), 4), 2)), ts_rank(ts_decay_linear(mul(div(ts_delta(add(mul(day_first(Open), 0.147155), mul(day_min(Low), sub(create_like(day_last(Close), 1), 0.147155))), 2), add(mul(day_first(Open), 0.147155), mul(day_min(Low), sub(create_like(day_last(Close), 1), 0.147155)))), -1), 3), 16)), -1)` |
| -2.40 | -2.23 | -2.40 | +1 | 5 | prods2069M3_I0_open_search | `cross_stddev(day_corr(Ret, in_shift(Volume, 1)), 20)` |
| -2.50 | -2.50 | -1.57 | +1 | 20 | prods2069M1_I0_open_search | `pairwise_min(cs_rank(ts_decay_linear(sub(add(div(add(day_max(High), day_min(Low)), 2), day_max(High)), add(div(day_sum(Amt), day_sum(Volume)), day_max(High))), 20)), cs_rank(ts_decay_linear(ts_corr(div(add(day_max(High), day_min(Low)), 2), ts_mean(day_sum(Volume), 40), 3), 5)))` |
| -2.56 | -1.97 | -2.56 | +1 | 20 | prods2069M2_I0_open_search | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)` |
| -2.66 | -2.66 | -1.73 | +1 | 20 | prods2069M2_I0_open_search | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)` |
| -2.75 | -2.75 | -1.99 | +1 | 20 | prods2069M1_I0_open_search | `sub(cs_rank(ts_decay_linear(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4), 7)), cs_rank(ts_decay_linear(ts_rank(ts_argmin(ts_corr(cs_rank(day_first(Open)), cs_rank(ts_mean(day_sum(Volume), 15)), 20), 8), 6), 8)))` |

## 共性:262 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.87 | 0.001 | 5 | -0.56 / -2.43 | `ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` |
| +1.87 | 0.000 | 33 | -0.77 / -2.63 | `day_std(Amt)` |
| +1.66 | 0.000 | 20 | -0.87 / -2.53 | `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5)` |
| +1.61 | 0.000 | 8 | -0.84 / -2.45 | `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` |
| +1.60 | 0.000 | 18 | -0.91 / -2.51 | `ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26)` |
| +1.60 | 0.007 | 4 | -0.82 / -2.42 | `cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5)` |
| +1.59 | 0.000 | 22 | -0.94 / -2.53 | `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20)))` |
| +1.59 | 0.000 | 38 | -1.04 / -2.63 | `cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4))` |
| +1.58 | 0.001 | 7 | -0.86 / -2.44 | `cross_mean(day_skew(Low), 20)` |
| +1.58 | 0.001 | 7 | -0.86 / -2.44 | `day_skew(Low)` |
| +1.50 | 0.004 | 6 | -0.93 / -2.43 | `cs_rank(cross_mean(day_skew(Low), 20))` |
| +1.32 | 0.000 | 45 | -1.30 / -2.63 | `cs_rank(cross_mean(day_skew(Ret), 20))` |
| +1.30 | 0.017 | 5 | -1.13 / -2.42 | `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20)))` |
| +1.27 | 0.000 | 87 | -1.55 / -2.82 | `day_skew(Ret)` |
| +1.27 | 0.002 | 8 | -1.17 / -2.44 | `cross_mean(cross_mean(day_skew(Ret), 20), 20)` |
| +1.23 | 0.000 | 84 | -1.56 / -2.79 | `cross_mean(day_skew(Ret), 20)` |
| +1.11 | 0.059 | 4 | -1.31 / -2.42 | `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5)` |
| +1.00 | 0.051 | 4 | -1.41 / -2.41 | `pow_3(cross_mean(cross_mean(day_skew(Ret), 20), 20))` |
| +0.98 | 0.029 | 5 | -1.44 / -2.42 | `cross_delay(pow_3(cross_mean(day_skew(Ret), 20)), 30)` |
| +0.98 | 0.001 | 14 | -1.47 / -2.45 | `pow_3(cross_mean(day_skew(Ret), 20))` |

## 拆解(14 次评估)

### head score -1.91:`cross_stddev(day_corr(Close, in_shift(Volume, 1)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(Close, in_shift(Volume, 1))` | -4.00 | -4.00 | -3.03 | — | (子树本身) |
| swap | `Close->Vwap` | -1.70 | -1.70 | -0.30 | — | `cross_stddev(day_corr(Vwap, in_shift(Volume, 1)), 20)` |
| swap | `Volume->Amt` | -1.92 | -1.92 | -1.21 | — | `cross_stddev(day_corr(Close, in_shift(Amt, 1)), 20)` |
| window | `cross_stddev@20->10` | -2.29 | -2.29 | -1.63 | — | `cross_stddev(day_corr(Close, in_shift(Volume, 1)), 10)` |
| window | `cross_stddev@20->40` | -1.90 | -1.90 | -1.86 | — | `cross_stddev(day_corr(Close, in_shift(Volume, 1)), 40)` |

### head score -2.28:`cross_mean(day_corr(Close, in_shift(Volume, 1)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(Close, in_shift(Volume, 1))` | -4.00 | -4.00 | -3.03 | — | (子树本身) |
| swap | `Close->Vwap` | -2.51 | -2.51 | -1.68 | — | `cross_mean(day_corr(Vwap, in_shift(Volume, 1)), 20)` |
| swap | `Volume->Amt` | -2.23 | -2.23 | -1.80 | — | `cross_mean(day_corr(Close, in_shift(Amt, 1)), 20)` |
| window | `cross_mean@20->10` | -2.64 | -2.64 | -1.89 | — | `cross_mean(day_corr(Close, in_shift(Volume, 1)), 10)` |
| window | `cross_mean@20->40` | -1.74 | -1.74 | -1.54 | — | `cross_mean(day_corr(Close, in_shift(Volume, 1)), 40)` |

### head score -2.40:`cross_stddev(day_corr(Ret, in_shift(Volume, 1)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(Ret, in_shift(Volume, 1))` | -4.67 | -4.67 | -3.02 | — | (子树本身) |
| swap | `Volume->Amt` | -2.64 | -2.30 | -2.64 | — | `cross_stddev(day_corr(Ret, in_shift(Amt, 1)), 20)` |
| window | `cross_stddev@20->10` | -2.87 | -2.24 | -2.87 | — | `cross_stddev(day_corr(Ret, in_shift(Volume, 1)), 10)` |
| window | `cross_stddev@20->40` | -2.35 | -1.81 | -2.35 | — | `cross_stddev(day_corr(Ret, in_shift(Volume, 1)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` — enrichment,均值差 +1.87,p 0.001
2. `day_std(Amt)` — enrichment,均值差 +1.87,p 0.000
3. `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5)` — enrichment,均值差 +1.66,p 0.000
4. `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` — enrichment,均值差 +1.61,p 0.000
5. `ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26)` — enrichment,均值差 +1.60,p 0.000
6. `cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5)` — enrichment,均值差 +1.60,p 0.007
7. `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20)))` — enrichment,均值差 +1.59,p 0.000
8. `cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4))` — enrichment,均值差 +1.59,p 0.000
9. `cross_mean(day_skew(Low), 20)` — enrichment,均值差 +1.58,p 0.001
10. `day_skew(Low)` — enrichment,均值差 +1.58,p 0.001
11. `cs_rank(cross_mean(day_skew(Low), 20))` — enrichment,均值差 +1.50,p 0.004
12. `cs_rank(cross_mean(day_skew(Ret), 20))` — enrichment,均值差 +1.32,p 0.000
13. `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20)))` — enrichment,均值差 +1.30,p 0.017
14. `day_skew(Ret)` — enrichment,均值差 +1.27,p 0.000
15. `cross_mean(cross_mean(day_skew(Ret), 20), 20)` — enrichment,均值差 +1.27,p 0.002
16. `cross_mean(day_skew(Ret), 20)` — enrichment,均值差 +1.23,p 0.000
17. `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5)` — enrichment,均值差 +1.11,p 0.059
18. `pow_3(cross_mean(cross_mean(day_skew(Ret), 20), 20))` — enrichment,均值差 +1.00,p 0.051
19. `cross_delay(pow_3(cross_mean(day_skew(Ret), 20)), 30)` — enrichment,均值差 +0.98,p 0.029
20. `pow_3(cross_mean(day_skew(Ret), 20))` — enrichment,均值差 +0.98,p 0.001
21. `mul(cs_robust_z(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 20)))` — enrichment,均值差 +0.97,p 0.051
22. `cs_robust_z(cross_mean(day_centroid(Amt), 20))` — enrichment,均值差 +0.97,p 0.051
23. `cs_last_high20(day_signed_ratio(Close, Vwap), day_q_stat_std(Ret))` — enrichment,均值差 +0.95,p 0.035
24. `day_signed_ratio(Close, Vwap)` — enrichment,均值差 +0.75,p 0.013
25. `day_centroid(Amt)` — enrichment,均值差 +0.75,p 0.070
26. `cross_mean(day_centroid(Amt), 20)` — enrichment,均值差 +0.75,p 0.070
27. `cs_last_high20(day_signed_ratio(Close, Vwap), day_min(Ret))` — enrichment,均值差 +0.71,p 0.082
28. `ts_scale(cross_mean(day_skew(Ret), 20), 40)` — enrichment,均值差 +0.70,p 0.048
29. `day_min(Ret)` — enrichment,均值差 +0.49,p 0.080
30. `day_sum(Volume)` — enrichment,均值差 +0.42,p 0.028
31. `ts_sum(ts_mean(day_sum(Volume), 5), 26)` — enrichment,均值差 +0.41,p 0.016
32. `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)` — enrichment,均值差 +0.41,p 0.016
33. `ts_mean(day_sum(Volume), 5)` — enrichment,均值差 +0.41,p 0.016
34. `div(day_sum(Amt), day_sum(Volume))` — enrichment,均值差 +0.35,p 0.040
35. `day_sum(Amt)` — enrichment,均值差 +0.27,p 0.052

## 本组之前各轮的任务

- `prods2069Pr1a_Ea`:核心 `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)`;评分 89,过线 0,入 heads 0;采样计数 {'c05_no_core': 400, 'c05_skeleton': 197, 'c05_periphery_seen': 1}
  - score +0.04(train +0.04 valid +0.26):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(cs_last_high10(cross_mean(ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_std(Amt)), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5), 26), 5), 26), 4), 5), day_std(Amt))`
  - score -0.02(train +0.07 valid -0.02):`cs_last_high10(cross_max(ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_std(Amt))`
  - score -0.06(train +0.08 valid -0.06):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5), 26), 5), 26), 4), 5), day_std(Amt))`
  - score -0.13(train +0.24 valid -0.13):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_std(Amt))`
  - score -0.16(train +0.41 valid -0.16):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 20))), 5), 26), 4), 5), day_std(Amt))`
- `prods2069Pr1b_Nb`:核心 `—`;评分 103,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.28(train -0.28 valid +0.34):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), cross_mean(cross_mean(day_skew(Ret), 20), 20)), 20)), cs_rank(cross_mean(cross_mean(day_skew(Ret), 20), 20)))`
  - score -0.47(train -0.47 valid +0.10):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), cross_mean(day_skew(Ret), 20)), 20)), cs_rank(cross_mean(day_skew(Ret), 20)))`
  - score -0.57(train -0.34 valid -0.57):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), cs_rank(cross_mean(day_skew(Ret), 60))))`
  - score -0.74(train -0.74 valid -0.09):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), cs_rank(cross_mean(day_skew(Ret), 20)))`
  - score -0.92(train -0.92 valid -0.55):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), cs_rank(cross_mean(day_skew(Ret), 20))))`
- `prods2069Pr2a_Ea`:核心 `cross_mean(day_skew(Ret), 20)`;评分 99,过线 0,入 heads 0;采样计数 {'c05_no_core': 2395, 'c05_skeleton': 1189, 'mutation_refused': 7}
  - score -0.86(train -0.86 valid -0.30):`ts_scale(ts_scale(pow_3(ts_scale(pow_3(cross_mean(day_skew(Ret), 20)), 40)), 40), 40)`
  - score -0.88(train -0.88 valid -0.69):`ts_scale(ts_scale(ts_scale(pow_3(cross_mean(day_skew(Ret), 20)), 40), 40), 40)`
  - score -0.92(train -0.69 valid -0.92):`ts_scale(ts_scale(pow_3(cross_mean(day_skew(Ret), 20)), 40), 40)`
  - score -0.94(train -0.83 valid -0.94):`ts_scale(ts_scale(ts_scale(cross_mean(day_skew(Ret), 20), 40), 40), 40)`
  - score -0.96(train -0.93 valid -0.96):`ts_scale(ts_scale(cross_mean(day_skew(Ret), 20), 40), 40)`
- `prods2069Pr2b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.91(train -0.84 valid -0.91):`mul(cs_robust_z(mul(cs_robust_z(cross_mean(day_centroid(Amt), 20)), mul(cs_robust_z(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 20))))), mul(cs_median(mul(cs_robust_z(cross_mean(day_centroid(Amt), 20)), mul(cs_robust_z(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 20))))), cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 20))))`
  - score -1.14(train -0.62 valid -1.14):`sigmoid(cs_last_high20(day_signed_ratio(Vwap, Vwap), cs_last_high20(day_signed_ratio(Close, Vwap), day_q_stat_std(Ret))))`
  - score -1.20(train -1.11 valid -1.20):`sigmoid(sigmoid(cs_last_high20(day_signed_ratio(Close, Vwap), day_q_stat_std(Ret))))`
  - score -1.20(train -1.11 valid -1.20):`sigmoid(sigmoid(sigmoid(sigmoid(cs_last_high20(day_signed_ratio(Close, Vwap), day_q_stat_std(Ret))))))`
  - score -1.29(train -0.82 valid -1.29):`sigmoid(sigmoid(cs_last_high20(day_signed_ratio(Close, Vwap), day_mean(Ret))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.54(window cross_mean@20->40):`cross_mean(day_corr(Close, in_shift(Volume, 1)), 40)`
- 增益 +0.21(swap Close->Vwap):`cross_stddev(day_corr(Vwap, in_shift(Volume, 1)), 20)`
