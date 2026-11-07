# 定位:种子 912,P 组,第 3 轮(只含 train / valid)

快照:prods912M1_I0_open_search, prods912M2_I0_open_search, prods912M3_I0_open_search, prods912Pr1a_Ea, prods912Pr1b_Nb, prods912Pr2a_Ea, prods912Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.37 | +1.37 | +2.44 | -1 | 0 | prods912Pr1a_Ea | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Close))), ListAge)` |
| +1.08 | +1.49 | +1.08 | +1 | 20 | prods912Pr1b_Nb | `cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| +0.96 | +0.96 | +1.75 | -1 | 20 | prods912Pr1a_Ea | `cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ts_delta(log(day_quantile(Close)), 40)), ListAge)` |
| +0.80 | +0.80 | +1.69 | -1 | 20 | prods912Pr1a_Ea | `cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10), ListAge)` |
| +0.76 | +0.76 | +1.82 | -1 | 5 | prods912M1_I0_open_search | `cs_first_high40(BoardCode, ts_var(sqrt(day_durbin_watson(Vwap)), 20))` |
| +0.74 | +0.74 | +1.58 | -1 | 5 | prods912Pr1a_Ea | `cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), ListAge)` |

## 共性:571 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.73 | 0.000 | 7 | +0.44 / -1.29 | `day_centroid(Volume)` |
| +1.72 | 0.000 | 5 | +0.44 / -1.28 | `cs_demean(day_centroid(Volume))` |
| +1.72 | 0.001 | 4 | +0.44 / -1.28 | `cs_demean(cs_demean(day_centroid(Volume)))` |
| +1.52 | 0.004 | 4 | +0.24 / -1.28 | `ts_var(sqrt(day_durbin_watson(Low)), 10)` |
| +1.50 | 0.000 | 18 | +0.18 / -1.32 | `pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| +1.47 | 0.005 | 4 | +0.19 / -1.28 | `ts_var(ts_var(day_corr(Low, Low), 1), 1)` |
| +1.36 | 0.004 | 5 | +0.08 / -1.28 | `day_durbin_watson(Low)` |
| +1.36 | 0.004 | 5 | +0.08 / -1.28 | `sqrt(day_durbin_watson(Low))` |
| +1.35 | 0.010 | 4 | +0.07 / -1.28 | `day_quantile(Close)` |
| +1.28 | 0.006 | 5 | -0.00 / -1.28 | `ts_var(day_corr(Vwap, Low), 1)` |
| +1.22 | 0.007 | 6 | -0.06 / -1.28 | `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| +1.17 | 0.025 | 4 | -0.10 / -1.28 | `ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10)` |
| +1.13 | 0.031 | 4 | -0.15 / -1.28 | `cs_first_high40(day_pos_ratio(Vwap), pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10)))` |
| +1.12 | 0.000 | 20 | -0.19 / -1.31 | `day_sum(Volume)` |
| +1.11 | 0.005 | 7 | -0.17 / -1.28 | `cs_last_high40(ts_sum(day_es_ratio_lo(Open), 30), cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5), 15))` |
| +1.11 | 0.012 | 5 | -0.17 / -1.28 | `cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume))` |
| +1.10 | 0.026 | 4 | -0.18 / -1.28 | `add(day_sum(Volume), day_at_min_ratio(Ret))` |
| +1.10 | 0.026 | 4 | -0.18 / -1.28 | `div(day_first(Volume), add(day_sum(Volume), day_at_min_ratio(Ret)))` |
| +1.08 | 0.024 | 4 | -0.19 / -1.28 | `cross_mean(cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume)), 241)` |
| +1.08 | 0.010 | 6 | -0.20 / -1.28 | `day_quantile(Amt)` |

## 拆解(36 次评估)

### head score +1.37:`cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Close))), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Close)))` | +0.81 | +0.81 | +2.03 | — | (子树本身) |
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 20)` | +0.22 | +0.22 | +0.37 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| sufficiency | `log(day_last(Close))` | -1.34 | -1.34 | -0.41 | — | (子树本身) |
| knockout | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Close)))` | +0.74 | +0.74 | +1.27 | +0.63 | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), ListAge)` |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 20)` | -0.70 | -0.70 | +2.54 | +2.07 | `cs_first_low20(cs_first_low20(sqrt(day_durbin_watson(Vwap)), log(day_last(Close))), ListAge)` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +1.33 | +1.33 | +2.67 | +0.05 | `cs_first_low20(cs_first_low20(ts_var(day_durbin_watson(Vwap), 20), log(day_last(Close))), ListAge)` |
| knockout | `log(day_last(Close))` | +1.37 | +1.37 | +2.44 | -0.00 | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), day_last(Close)), ListAge)` |
| swap | `Vwap->Close` | +1.09 | +1.09 | +2.58 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Close)), 20), log(day_last(Close))), ListAge)` |
| swap | `Close->Vwap` | +1.38 | +1.38 | +2.44 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Vwap))), ListAge)` |
| window | `ts_var@20->10` | +1.07 | +1.07 | +2.76 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Close))), ListAge)` |
| window | `ts_var@20->40` | +1.21 | +1.21 | +3.00 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 40), log(day_last(Close))), ListAge)` |

### head score +1.08:`cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20))` | -0.69 | +0.94 | -0.69 | — | (子树本身) |
| sufficiency | `ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40)` | +0.56 | +1.12 | +0.56 | — | (子树本身) |
| sufficiency | `sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1)))` | -3.94 | -1.83 | -3.94 | — | (子树本身) |
| sufficiency | `log(ts_delay(day_last(Close), 1))` | -1.33 | -1.33 | -0.38 | — | (子树本身) |
| knockout | `cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20))` | +0.95 | +1.22 | +0.95 | +0.13 | `cs_last_low10(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ListAge)` |
| knockout | `ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40)` | +0.94 | +0.94 | +1.46 | +0.14 | `cs_last_low10(cs_last_high40(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| knockout | `sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1)))` | -0.56 | +0.11 | -0.56 | +1.64 | `cs_last_low10(cs_last_high40(ts_skew(log(day_first(Open)), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| knockout | `log(ts_delay(day_last(Close), 1))` | +1.05 | +1.36 | +1.05 | +0.03 | `cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Open)), ts_delay(day_last(Close), 1)), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| swap | `Open->Close` | +1.08 | +1.51 | +1.08 | — | `cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Close)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| swap | `Close->Vwap` | +1.11 | +1.66 | +1.11 | — | `cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Vwap), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| window | `ts_skew@40->20` | +0.65 | +1.51 | +0.65 | — | `cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 20), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |
| window | `ts_skew@40->80` | +0.22 | +1.20 | +0.22 | — | `cs_last_low10(cs_last_high40(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 80), ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |

### head score +0.96:`cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ts_delta(log(day_quantile(Close)), 40)), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ts_delta(log(day_quantile(Close)), 40))` | +0.55 | +0.55 | +0.95 | — | (子树本身) |
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | +0.07 | +0.07 | +1.04 | — | (子树本身) |
| sufficiency | `ts_delta(log(day_quantile(Close)), 40)` | -0.53 | -0.53 | -0.51 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| knockout | `cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ts_delta(log(day_quantile(Close)), 40))` | +0.67 | +0.67 | +1.54 | +0.29 | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ListAge)` |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | -0.89 | -0.89 | +0.18 | +1.85 | `cs_first_low20(cs_bucket_rank(sqrt(day_durbin_watson(Vwap)), ts_delta(log(day_quantile(Close)), 40)), ListAge)` |
| knockout | `ts_delta(log(day_quantile(Close)), 40)` | +0.61 | +0.61 | +1.65 | +0.35 | `cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_quantile(Close))), ListAge)` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +0.75 | +0.75 | +1.04 | +0.22 | `cs_first_low20(cs_bucket_rank(ts_var(day_durbin_watson(Vwap), 10), ts_delta(log(day_quantile(Close)), 40)), ListAge)` |
| swap | `Vwap->Close` | +0.79 | +0.79 | +1.36 | — | `cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Close)), 10), ts_delta(log(day_quantile(Close)), 40)), ListAge)` |
| swap | `Close->Vwap` | +1.00 | +1.00 | +1.76 | — | `cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ts_delta(log(day_quantile(Vwap)), 40)), ListAge)` |
| window | `ts_var@10->5` | +1.03 | +1.03 | +1.56 | — | `cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 5), ts_delta(log(day_quantile(Close)), 40)), ListAge)` |
| window | `ts_var@10->20` | +1.06 | +1.06 | +1.19 | — | `cs_first_low20(cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 20), ts_delta(log(day_quantile(Close)), 40)), ListAge)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(Volume)` — enrichment,均值差 +1.73,p 0.000
2. `cs_demean(day_centroid(Volume))` — enrichment,均值差 +1.72,p 0.000
3. `cs_demean(cs_demean(day_centroid(Volume)))` — enrichment,均值差 +1.72,p 0.001
4. `ts_var(sqrt(day_durbin_watson(Low)), 10)` — enrichment,均值差 +1.52,p 0.004
5. `pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` — enrichment,均值差 +1.50,p 0.000
6. `ts_var(ts_var(day_corr(Low, Low), 1), 1)` — enrichment,均值差 +1.47,p 0.005
7. `day_durbin_watson(Low)` — enrichment,均值差 +1.36,p 0.004
8. `sqrt(day_durbin_watson(Low))` — enrichment,均值差 +1.36,p 0.004
9. `day_quantile(Close)` — enrichment,均值差 +1.35,p 0.010
10. `ts_var(day_corr(Vwap, Low), 1)` — enrichment,均值差 +1.28,p 0.006
11. `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` — enrichment,均值差 +1.22,p 0.007
12. `ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10)` — enrichment,均值差 +1.17,p 0.025
13. `cs_first_high40(day_pos_ratio(Vwap), pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10)))` — enrichment,均值差 +1.13,p 0.031
14. `day_sum(Volume)` — enrichment,均值差 +1.12,p 0.000
15. `cs_last_high40(ts_sum(day_es_ratio_lo(Open), 30), cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5), 15))` — enrichment,均值差 +1.11,p 0.005
16. `cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume))` — enrichment,均值差 +1.11,p 0.012
17. `add(day_sum(Volume), day_at_min_ratio(Ret))` — enrichment,均值差 +1.10,p 0.026
18. `div(day_first(Volume), add(day_sum(Volume), day_at_min_ratio(Ret)))` — enrichment,均值差 +1.10,p 0.026
19. `cross_mean(cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume)), 241)` — enrichment,均值差 +1.08,p 0.024
20. `day_quantile(Amt)` — enrichment,均值差 +1.08,p 0.010
21. `ts_kurt(day_quantile(Amt), 50)` — enrichment,均值差 +1.08,p 0.010
22. `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` — enrichment,均值差 +1.07,p 0.000
23. `cs_last_low10(day_zero_ratio(Vwap), ListAge)` — enrichment,均值差 +1.05,p 0.032
24. `sqrt(day_durbin_watson(Vwap))` — enrichment,均值差 +1.04,p 0.000
25. `day_first(Volume)` — enrichment,均值差 +1.02,p 0.000
26. `cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15)))` — enrichment,均值差 +1.00,p 0.005
27. `log(log(day_last(Close)))` — enrichment,均值差 +0.99,p 0.019
28. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.97,p 0.000
29. `day_pos_ratio(Vwap)` — enrichment,均值差 +0.94,p 0.001
30. `cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5)` — enrichment,均值差 +0.94,p 0.013
31. `cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5), 15)` — enrichment,均值差 +0.94,p 0.013
32. `ts_var(ts_var(sqrt(day_durbin_watson(Vwap)), 10), 10)` — enrichment,均值差 +0.91,p 0.006
33. `ts_delta(log(log(day_last(Close))), 20)` — enrichment,均值差 +0.90,p 0.046
34. `ts_sum(day_es_ratio_lo(Open), 30)` — enrichment,均值差 +0.81,p 0.000
35. `pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))` — enrichment,均值差 +0.80,p 0.012
36. `cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15)` — enrichment,均值差 +0.79,p 0.005
37. `day_corr(Low, Vwap)` — enrichment,均值差 +0.75,p 0.015
38. `ts_var(day_corr(Low, Vwap), 1)` — enrichment,均值差 +0.75,p 0.015
39. `ts_var(day_corr(Low, Low), 1)` — enrichment,均值差 +0.73,p 0.002
40. `day_corr(Low, Low)` — enrichment,均值差 +0.71,p 0.001
41. `day_corr(Vwap, Low)` — enrichment,均值差 +0.69,p 0.058
42. `day_at_min_ratio(Ret)` — enrichment,均值差 +0.67,p 0.087
43. `day_zero_ratio(Vwap)` — enrichment,均值差 +0.65,p 0.000
44. `cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5)` — enrichment,均值差 +0.63,p 0.009
45. `day_es_ratio_lo(Open)` — enrichment,均值差 +0.59,p 0.001
46. `cs_bucket_rank(day_zero_ratio(Vwap), ListAge)` — enrichment,均值差 +0.48,p 0.030
47. `day_argmax(Volume)` — enrichment,均值差 +0.45,p 0.034

## 本组之前各轮的任务

- `prods912Pr1a_Ea`:核心 `ts_var(sqrt(day_durbin_watson(Vwap)), 10)`;评分 103,过线 10,入 heads 4;采样计数 {'c05_no_core': 2051, 'mutation_refused': 9, 'c05_periphery_seen': 8}
  - score +1.12(train +1.12 valid +2.74):`cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Close))), ListAge)`
  - score +0.80(train +0.80 valid +1.69):`cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10), ListAge)`
  - score +0.75(train +0.75 valid +1.25):`cs_first_low20(ts_var(ts_var(sqrt(day_durbin_watson(Vwap)), 10), 10), ListAge)`
  - score +0.74(train +0.74 valid +1.58):`cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), ListAge)`
  - score +0.72(train +0.72 valid +1.56):`cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ListAge)`
- `prods912Pr1b_Nb`:核心 `—`;评分 101,过线 1,入 heads 1;采样计数 {}
  - score +0.56(train +1.12 valid +0.56):`ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40)`
  - score +0.15(train +0.15 valid +0.21):`sub(cs_rank(ts_std(log(day_first(Open)), 20)), cs_rank(ts_std(sub(log(day_last(Close)), log(day_first(Open))), 20)))`
  - score +0.15(train +0.15 valid +0.21):`sub(cs_rank(ts_std(sub(log(day_first(Open)), ts_std(sub(log(day_first(Open)), log(day_first(Open))), 20)), 20)), cs_rank(ts_std(sub(log(day_last(Close)), log(day_first(Open))), 20)))`
  - score -0.08(train +0.13 valid -0.08):`sub(cs_rank(ts_std(sub(log(day_first(Open)), ts_std(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 20)), 20)), cs_rank(ts_std(sub(log(day_last(Close)), log(day_first(Open))), 20)))`
  - score -0.08(train +0.07 valid -0.08):`sub(cs_rank(ts_std(sub(log(day_first(Close)), ts_std(sub(log(day_first(Close)), log(ts_delay(day_last(Close), 1))), 20)), 20)), cs_rank(ts_std(sub(log(day_last(Close)), log(day_first(Open))), 20)))`
- `prods912Pr2a_Ea`:核心 `sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1)))`;评分 100,过线 0,入 heads 0;采样计数 {'c05_no_core': 1808, 'mutation_refused': 4, 'c05_periphery_seen': 7, 'c05_skeleton': 2}
  - score +0.41(train +0.41 valid +1.38):`ts_corr(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), ts_delay(sub(log(day_last(Close)), log(day_first(Open))), 1), 60)`
  - score +0.21(train +0.21 valid +0.26):`cs_first_low20(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Amt)), 20))`
  - score +0.00(train +0.12 valid +0.00):`ts_corr(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), day_first(Open), 60)`
  - score -0.03(train +0.78 valid -0.03):`cs_first_low20(ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40), ts_var(sqrt(day_durbin_watson(Vwap)), 20))`
  - score -0.03(train -0.03 valid +0.05):`ts_corr(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), ts_delay(sub(log(day_last(Close)), sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1)))), 1), 60)`
- `prods912Pr2b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {}
  - score +0.35(train +0.35 valid +1.35):`ts_mean(div(day_first(Volume), add(day_sum(Volume), 1)), 60)`
  - score +0.35(train +0.35 valid +1.35):`ts_mean(div(day_first(Volume), add(day_sum(Volume), -5)), 60)`
  - score +0.35(train +0.35 valid +1.35):`ts_mean(div(day_first(Volume), add(day_sum(Volume), day_at_min_ratio(Ret))), 60)`
  - score +0.35(train +0.35 valid +1.35):`ts_mean(div(day_first(Volume), add(day_sum(Volume), day_at_min_ratio(Volume))), 60)`
  - score +0.34(train +0.34 valid +1.56):`cs_last_low10(ts_mean(div(day_first(Volume), add(day_sum(Volume), 1)), 40), ListAge)`

## 比原 head 好的拆解变体(R 候选)

(没有)
