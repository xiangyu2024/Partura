# 定位:种子 912,P 组,第 2 轮(只含 train / valid)

快照:prods912M1_I0_open_search, prods912M2_I0_open_search, prods912Pr1a_Ea, prods912Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.12 | +1.12 | +2.74 | -1 | 5 | prods912Pr1a_Ea | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Close))), ListAge)` |
| +0.80 | +0.80 | +1.69 | -1 | 20 | prods912Pr1a_Ea | `cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10), ListAge)` |
| +0.76 | +0.76 | +1.82 | -1 | 5 | prods912M1_I0_open_search | `cs_first_high40(BoardCode, ts_var(sqrt(day_durbin_watson(Vwap)), 20))` |
| +0.74 | +0.74 | +1.58 | -1 | 5 | prods912Pr1a_Ea | `cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), ListAge)` |
| +0.61 | +0.61 | +0.95 | -1 | 20 | prods912Pr1a_Ea | `cs_bucket_rank(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ts_delta(log(day_quantile(Close)), 40))` |
| +0.56 | +1.12 | +0.56 | +1 | 20 | prods912Pr1b_Nb | `ts_skew(sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1))), 40)` |

## 共性:404 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.42 | 0.006 | 4 | +0.24 / -1.18 | `ts_var(sqrt(day_durbin_watson(Low)), 10)` |
| +1.41 | 0.000 | 18 | +0.18 / -1.23 | `pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| +1.37 | 0.008 | 4 | +0.19 / -1.18 | `ts_var(ts_var(day_corr(Low, Low), 1), 1)` |
| +1.27 | 0.005 | 5 | +0.08 / -1.18 | `sqrt(day_durbin_watson(Low))` |
| +1.27 | 0.005 | 5 | +0.08 / -1.18 | `day_durbin_watson(Low)` |
| +1.18 | 0.009 | 5 | -0.00 / -1.18 | `ts_var(day_corr(Vwap, Low), 1)` |
| +1.12 | 0.009 | 6 | -0.06 / -1.18 | `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| +1.07 | 0.030 | 4 | -0.10 / -1.18 | `ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10)` |
| +1.05 | 0.000 | 116 | -0.42 / -1.47 | `sqrt(day_durbin_watson(Vwap))` |
| +1.04 | 0.000 | 99 | -0.38 / -1.42 | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` |
| +1.03 | 0.043 | 4 | -0.15 / -1.18 | `cs_first_high40(day_pos_ratio(Vwap), pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10)))` |
| +1.01 | 0.006 | 7 | -0.17 / -1.18 | `cs_last_high40(ts_sum(day_es_ratio_lo(Open), 30), cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5), 15))` |
| +1.01 | 0.013 | 5 | -0.17 / -1.18 | `cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume))` |
| +0.99 | 0.000 | 124 | -0.48 / -1.47 | `day_durbin_watson(Vwap)` |
| +0.98 | 0.025 | 4 | -0.19 / -1.18 | `cross_mean(cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume)), 241)` |
| +0.98 | 0.013 | 6 | -0.20 / -1.18 | `day_quantile(Amt)` |
| +0.98 | 0.013 | 6 | -0.20 / -1.18 | `ts_kurt(day_quantile(Amt), 50)` |
| +0.95 | 0.037 | 4 | -0.23 / -1.18 | `cs_last_low10(day_zero_ratio(Vwap), ListAge)` |
| +0.90 | 0.007 | 9 | -0.29 / -1.19 | `cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15)))` |
| +0.89 | 0.026 | 6 | -0.29 / -1.18 | `log(log(day_last(Close)))` |

## 拆解(41 次评估)

### head score +1.12:`cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Close))), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Close)))` | +0.39 | +0.39 | +2.14 | — | (子树本身) |
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | +0.07 | +0.07 | +1.04 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| sufficiency | `log(day_last(Close))` | -1.34 | -1.34 | -0.41 | — | (子树本身) |
| knockout | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Close)))` | +0.67 | +0.67 | +1.54 | +0.44 | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ListAge)` |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | -0.70 | -0.70 | +2.54 | +1.81 | `cs_first_low20(cs_first_low20(sqrt(day_durbin_watson(Vwap)), log(day_last(Close))), ListAge)` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +0.96 | +0.96 | +2.79 | +0.15 | `cs_first_low20(cs_first_low20(ts_var(day_durbin_watson(Vwap), 10), log(day_last(Close))), ListAge)` |
| knockout | `log(day_last(Close))` | +1.06 | +1.06 | +2.75 | +0.05 | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), day_last(Close)), ListAge)` |
| swap | `Vwap->Close` | +0.96 | +0.96 | +2.76 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Close)), 10), log(day_last(Close))), ListAge)` |
| swap | `Close->Vwap` | +1.10 | +1.10 | +2.73 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), log(day_last(Vwap))), ListAge)` |
| window | `ts_var@10->5` | +0.74 | +0.74 | +2.60 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 5), log(day_last(Close))), ListAge)` |
| window | `ts_var@10->20` | +1.37 | +1.37 | +2.44 | — | `cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Close))), ListAge)` |

### head score +0.80:`cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10)` | -0.70 | -0.70 | -0.07 | — | (子树本身) |
| sufficiency | `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` | +0.08 | +0.08 | +1.04 | — | (子树本身) |
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | +0.07 | +0.07 | +1.04 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| knockout | `ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10)` | +0.69 | +0.69 | +1.53 | +0.11 | `cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), ListAge)` |
| knockout | `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` | +0.75 | +0.75 | +1.22 | +0.05 | `cs_first_low20(ts_var(ts_var(sqrt(day_durbin_watson(Vwap)), 10), 10), ListAge)` |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | +0.69 | +0.69 | +1.88 | +0.11 | `cs_first_low20(ts_var(sqrt(sqrt(day_durbin_watson(Vwap))), 10), ListAge)` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +0.73 | +0.82 | +0.73 | +0.07 | `cs_first_low20(ts_var(sqrt(ts_var(day_durbin_watson(Vwap), 10)), 10), ListAge)` |
| swap | `Vwap->Close` | +0.54 | +0.54 | +1.33 | — | `cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Close)), 10)), 10), ListAge)` |
| window | `ts_var@10->5` | +0.44 | +0.44 | +1.53 | — | `cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 5), ListAge)` |
| window | `ts_var@10->20` | +0.83 | +0.83 | +1.96 | — | `cs_first_low20(ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 20), ListAge)` |

### head score +0.76:`cs_first_high40(BoardCode, ts_var(sqrt(day_durbin_watson(Vwap)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 20)` | +0.22 | +0.22 | +0.37 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.27 | -2.37 | -3.27 | — | (子树本身) |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 20)` | -3.49 | -0.66 | -3.49 | +4.25 | `cs_first_high40(BoardCode, sqrt(day_durbin_watson(Vwap)))` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +0.74 | +0.74 | +1.18 | +0.02 | `cs_first_high40(BoardCode, ts_var(day_durbin_watson(Vwap), 20))` |
| swap | `Vwap->Close` | +0.51 | +0.51 | +0.95 | — | `cs_first_high40(BoardCode, ts_var(sqrt(day_durbin_watson(Close)), 20))` |
| window | `ts_var@20->10` | +0.74 | +0.74 | +2.12 | — | `cs_first_high40(BoardCode, ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| window | `ts_var@20->40` | +0.62 | +0.62 | +1.21 | — | `cs_first_high40(BoardCode, ts_var(sqrt(day_durbin_watson(Vwap)), 40))` |

### head score +0.74:`cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` | +0.08 | +0.08 | +1.04 | — | (子树本身) |
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | +0.07 | +0.07 | +1.04 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.27 | -2.37 | -3.27 | — | (子树本身) |
| knockout | `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` | +0.67 | +0.67 | +1.54 | +0.06 | `cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 10), ListAge)` |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | -1.98 | -1.98 | -1.16 | +2.71 | `cs_first_low20(sqrt(sqrt(day_durbin_watson(Vwap))), ListAge)` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +0.51 | +0.51 | +1.75 | +0.23 | `cs_first_low20(sqrt(ts_var(day_durbin_watson(Vwap), 10)), ListAge)` |
| swap | `Vwap->Close` | +0.37 | +0.37 | +1.83 | — | `cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Close)), 10)), ListAge)` |
| window | `ts_var@10->5` | +0.43 | +0.43 | +1.86 | — | `cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 5)), ListAge)` |
| window | `ts_var@10->20` | +0.74 | +0.74 | +1.27 | — | `cs_first_low20(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 20)), ListAge)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_var(sqrt(day_durbin_watson(Low)), 10)` — enrichment,均值差 +1.42,p 0.006
2. `pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` — enrichment,均值差 +1.41,p 0.000
3. `ts_var(ts_var(day_corr(Low, Low), 1), 1)` — enrichment,均值差 +1.37,p 0.008
4. `sqrt(day_durbin_watson(Low))` — enrichment,均值差 +1.27,p 0.005
5. `day_durbin_watson(Low)` — enrichment,均值差 +1.27,p 0.005
6. `ts_var(day_corr(Vwap, Low), 1)` — enrichment,均值差 +1.18,p 0.009
7. `sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` — enrichment,均值差 +1.12,p 0.009
8. `ts_var(sqrt(ts_var(sqrt(day_durbin_watson(Vwap)), 10)), 10)` — enrichment,均值差 +1.07,p 0.030
9. `sqrt(day_durbin_watson(Vwap))` — enrichment,均值差 +1.05,p 0.000
10. `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` — enrichment,均值差 +1.04,p 0.000
11. `cs_first_high40(day_pos_ratio(Vwap), pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10)))` — enrichment,均值差 +1.03,p 0.043
12. `cs_last_high40(ts_sum(day_es_ratio_lo(Open), 30), cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5), 15))` — enrichment,均值差 +1.01,p 0.006
13. `cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume))` — enrichment,均值差 +1.01,p 0.013
14. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.99,p 0.000
15. `cross_mean(cs_last_low10(day_zero_ratio(Vwap), day_argmax(Volume)), 241)` — enrichment,均值差 +0.98,p 0.025
16. `day_quantile(Amt)` — enrichment,均值差 +0.98,p 0.013
17. `ts_kurt(day_quantile(Amt), 50)` — enrichment,均值差 +0.98,p 0.013
18. `cs_last_low10(day_zero_ratio(Vwap), ListAge)` — enrichment,均值差 +0.95,p 0.037
19. `cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15)))` — enrichment,均值差 +0.90,p 0.007
20. `log(log(day_last(Close)))` — enrichment,均值差 +0.89,p 0.026
21. `day_pos_ratio(Vwap)` — enrichment,均值差 +0.85,p 0.001
22. `cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5)` — enrichment,均值差 +0.84,p 0.016
23. `cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))), 5), 15)` — enrichment,均值差 +0.84,p 0.016
24. `ts_var(ts_var(sqrt(day_durbin_watson(Vwap)), 10), 10)` — enrichment,均值差 +0.82,p 0.009
25. `ts_delta(log(log(day_last(Close))), 20)` — enrichment,均值差 +0.80,p 0.058
26. `ts_sum(day_es_ratio_lo(Open), 30)` — enrichment,均值差 +0.72,p 0.000
27. `pow_2_5(cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15))` — enrichment,均值差 +0.70,p 0.017
28. `cross_max(cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5), 15)` — enrichment,均值差 +0.69,p 0.008
29. `day_corr(Low, Vwap)` — enrichment,均值差 +0.65,p 0.025
30. `ts_var(day_corr(Low, Vwap), 1)` — enrichment,均值差 +0.65,p 0.025
31. `ts_var(day_corr(Low, Low), 1)` — enrichment,均值差 +0.63,p 0.006
32. `day_corr(Low, Low)` — enrichment,均值差 +0.62,p 0.003
33. `day_corr(Vwap, Low)` — enrichment,均值差 +0.59,p 0.084
34. `day_zero_ratio(Vwap)` — enrichment,均值差 +0.56,p 0.000
35. `cross_mean(cs_bucket_rank(day_zero_ratio(Vwap), ListAge), 5)` — enrichment,均值差 +0.53,p 0.019
36. `day_es_ratio_lo(Open)` — enrichment,均值差 +0.50,p 0.003
37. `cs_bucket_rank(day_zero_ratio(Vwap), ListAge)` — enrichment,均值差 +0.38,p 0.062
38. `day_argmax(Volume)` — enrichment,均值差 +0.35,p 0.069

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.26(window ts_var@10->20):`cs_first_low20(cs_first_low20(ts_var(sqrt(day_durbin_watson(Vwap)), 20), log(day_last(Close))), ListAge)`
