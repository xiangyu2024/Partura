# 定位:种子 907,P 组,第 3 轮(只含 train / valid)

快照:prods907M1_I0_open_search, prods907M2_I0_open_search, prods907M3_I0_open_search, prods907Pr1a_Na, prods907Pr1b_Nb, prods907Pr2a_Ea, prods907Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(17 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.79 | +1.95 | +1.79 | -1 | 5 | prods907Pr2b_Nb | `cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 20)` |
| +1.73 | +1.95 | +1.73 | -1 | 5 | prods907Pr1b_Nb | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_gini(Volume), 30)))` |
| +1.46 | +1.46 | +1.78 | +1 | 5 | prods907M3_I0_open_search | `cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30), 30)` |
| +1.43 | +1.49 | +1.43 | -1 | 20 | prods907M2_I0_open_search | `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` |
| +1.43 | +1.49 | +1.43 | -1 | 20 | prods907M2_I0_open_search | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Volume)))` |
| +1.24 | +1.24 | +1.34 | +1 | 5 | prods907M3_I0_open_search | `cross_max(cross_max(cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30), 30), 30), 30)` |
| +0.99 | +0.99 | +1.25 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |
| +0.92 | +0.92 | +1.26 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 20))))` |
| +0.92 | +0.92 | +2.26 | +1 | 5 | prods907M3_I0_open_search | `cross_max(cs_mask_top_replace_mean_neg(cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_quantile_q25(Amt)), 30), 30), 30)), 30)` |
| +0.78 | +1.11 | +0.78 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(cs_rank(cross_mean(day_centroid(Volume), 30)), 20), 20))))` |
| +0.73 | +1.24 | +0.73 | +1 | 5 | prods907M2_I0_open_search | `signedpower(cs_first_low40(cs_bucket_zscore(LogFloatShares, cs_first_low40(LogFloatShares, day_std(Volume))), cs_first_low40(LogFloatShares, day_std(Volume))))` |
| +0.73 | +1.17 | +0.73 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(cross_mean(sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 30)))), 30))))` |
| +0.72 | +0.72 | +0.86 | -1 | 0 | prods907M2_I0_open_search | `signedpower(cs_first_low40(abs_(LogFloatShares), LogFloatShares))` |
| +0.57 | +0.57 | +1.71 | -1 | 20 | prods907Pr2a_Ea | `cs_first_low40(cs_first_low20(cross_mean(cs_first_high40(day_gini(Close), cross_mean(day_centroid(Volume), 30)), 30), LogFloatCap), LogFloatShares)` |
| +0.57 | +0.57 | +0.59 | -1 | 5 | prods907Pr2a_Ea | `ts_regres(day_wmean(in_mean_full(Amt), in_mean_full(Amt)), cross_mean(day_centroid(Volume), 30), 50)` |
| +0.51 | +0.51 | +1.00 | -1 | 20 | prods907Pr2a_Ea | `ts_regres(day_wmean(in_mean_full(Amt), in_mean_full(Amt)), cs_first_high40(day_gini(Open), cross_mean(day_centroid(Volume), 30)), 50)` |
| +0.51 | +0.51 | +1.35 | +1 | 20 | prods907Pr1a_Na | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), day_distinct_ratio(Close), 50), FloatShares))` |

## 共性:491 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.13 | 0.001 | 4 | +1.12 / -1.01 | `cs_first_low40(abs_(LogFloatShares), day_std(Volume))` |
| +2.09 | 0.000 | 9 | +1.05 / -1.03 | `cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))` |
| +2.05 | 0.001 | 5 | +1.03 / -1.02 | `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` |
| +2.04 | 0.000 | 6 | +1.03 / -1.02 | `cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30)` |
| +2.01 | 0.000 | 10 | +0.97 / -1.04 | `cs_first_low40(LogFloatShares, day_std(Volume))` |
| +2.00 | 0.001 | 6 | +0.98 / -1.02 | `cs_first_low40(day_std(Volume), day_std(Volume))` |
| +1.66 | 0.005 | 4 | +0.65 / -1.01 | `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` |
| +1.51 | 0.000 | 22 | +0.45 / -1.06 | `cs_rank(cross_mean(day_centroid(Volume), 30))` |
| +1.46 | 0.001 | 10 | +0.43 / -1.02 | `cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30)` |
| +1.38 | 0.009 | 4 | +0.37 / -1.01 | `day_gini(Close)` |
| +1.24 | 0.000 | 20 | +0.20 / -1.05 | `cs_quantile_q25(LogFloatShares)` |
| +1.24 | 0.001 | 13 | +0.21 / -1.03 | `abs_(LogFloatShares)` |
| +1.18 | 0.001 | 14 | +0.15 / -1.03 | `cross_mean(day_gini(Volume), 30)` |
| +1.14 | 0.000 | 105 | -0.10 / -1.24 | `day_std(Volume)` |
| +1.14 | 0.059 | 4 | +0.14 / -1.00 | `day_sum(Volume)` |
| +1.11 | 0.008 | 8 | +0.10 / -1.01 | `day_sum(in_slice(Volume, 1, 239))` |
| +1.03 | 0.041 | 5 | +0.03 / -1.01 | `ts_autocorr_s1(day_argmax(Vwap), 20)` |
| +1.03 | 0.034 | 6 | +0.02 / -1.01 | `div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239)))` |
| +0.97 | 0.005 | 12 | -0.05 / -1.02 | `cs_rank(cross_mean(day_gini(Volume), 30))` |
| +0.93 | 0.077 | 4 | -0.07 / -1.00 | `cs_bucket_zscore(LogFloatShares, day_std(Volume))` |

## 拆解(31 次评估)

### head score +1.79:`cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239)))` | +0.49 | +1.02 | +0.49 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Volume, 211, 239))` | -2.24 | -0.50 | -2.24 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Volume, 1, 239))` | -0.23 | -0.23 | +0.09 | — | (子树本身) |
| knockout | `div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239)))` | -2.08 | -0.36 | -2.08 | +3.87 | `cross_mean(day_sum(in_slice(Volume, 211, 239)), 20)` |
| swap | `Volume->Amt` | +1.81 | +1.94 | +1.81 | — | `cross_mean(div(day_sum(in_slice(Amt, 211, 239)), day_sum(in_slice(Amt, 1, 239))), 20)` |
| window | `cross_mean@20->10` | +1.60 | +1.60 | +2.15 | — | `cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 10)` |
| window | `cross_mean@20->40` | +1.59 | +1.59 | +2.37 | — | `cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 40)` |

### head score +1.73:`cs_regres(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_gini(Volume), 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cross_mean(day_centroid(Volume), 30))` | +1.73 | +1.73 | +1.88 | — | (子树本身) |
| sufficiency | `cs_rank(cross_mean(day_gini(Volume), 30))` | -2.02 | -2.02 | -1.96 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Volume), 30)` | +1.73 | +1.73 | +1.88 | — | (子树本身) |
| sufficiency | `cross_mean(day_gini(Volume), 30)` | -2.02 | -2.02 | -1.96 | — | (子树本身) |
| knockout | `cs_rank(cross_mean(day_centroid(Volume), 30))` | +1.45 | +1.68 | +1.45 | +0.28 | `cs_regres(cross_mean(day_centroid(Volume), 30), cs_rank(cross_mean(day_gini(Volume), 30)))` |
| knockout | `cs_rank(cross_mean(day_gini(Volume), 30))` | +1.69 | +1.74 | +1.69 | +0.04 | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mean(day_gini(Volume), 30))` |
| knockout | `cross_mean(day_centroid(Volume), 30)` | +0.29 | +1.42 | +0.29 | +1.44 | `cs_regres(cs_rank(day_centroid(Volume)), cs_rank(cross_mean(day_gini(Volume), 30)))` |
| knockout | `cross_mean(day_gini(Volume), 30)` | +0.78 | +1.45 | +0.78 | +0.95 | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(day_gini(Volume)))` |
| swap | `Volume->Amt` | +1.69 | +1.91 | +1.69 | — | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 30)), cs_rank(cross_mean(day_gini(Amt), 30)))` |
| window | `cross_mean@30->15` | +0.90 | +1.74 | +0.90 | — | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 15)), cs_rank(cross_mean(day_gini(Volume), 30)))` |
| window | `cross_mean@30->60` | +1.05 | +1.74 | +1.05 | — | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 60)), cs_rank(cross_mean(day_gini(Volume), 30)))` |

### head score +1.46:`cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30)` | +0.33 | +0.33 | +1.83 | — | (子树本身) |
| sufficiency | `cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30)` | -2.29 | -2.29 | -1.39 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean_neg(day_first(Volume))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30)` | +0.34 | +0.34 | +1.16 | +1.12 | `cross_max(cross_max(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30)` |
| knockout | `cs_mask_top_replace_mean_neg(day_first(Volume))` | +0.96 | +0.96 | +1.51 | +0.49 | `cross_max(cross_max(cross_zscore(day_first(Volume), 30), 30), 30)` |
| swap | `Volume->Amt` | +0.95 | +0.95 | +1.43 | — | `cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Amt)), 30), 30), 30)` |
| window | `cross_max@30->15` | +0.74 | +0.74 | +1.30 | — | `cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30), 15)` |
| window | `cross_max@30->60` | +1.25 | +1.25 | +1.72 | — | `cross_max(cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30), 60)` |

### head score +1.43:`signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low40(LogFloatShares, day_std(Volume))` | +1.43 | +1.49 | +1.43 | — | (子树本身) |
| sufficiency | `day_std(Volume)` | -1.87 | -0.20 | -1.87 | — | (子树本身) |
| knockout | `cs_first_low40(LogFloatShares, day_std(Volume))` | -0.54 | -0.54 | -0.41 | +1.97 | `signedpower(LogFloatShares)` |
| swap | `Volume->Amt` | -2.49 | -0.93 | -2.49 | — | `signedpower(cs_first_low40(LogFloatShares, day_std(Amt)))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_rank(cross_mean(day_centroid(Volume), 30))` — ablation,自身 score +1.73(所在 head +1.73)
2. `cross_mean(day_centroid(Volume), 30)` — ablation,自身 score +1.73(所在 head +1.73)
3. `cs_first_low40(LogFloatShares, day_std(Volume))` — ablation,自身 score +1.43(所在 head +1.43)
4. `cs_first_low40(abs_(LogFloatShares), day_std(Volume))` — enrichment,均值差 +2.13,p 0.001
5. `cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))` — enrichment,均值差 +2.09,p 0.000
6. `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` — enrichment,均值差 +2.05,p 0.001
7. `cross_max(cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30), 30)` — enrichment,均值差 +2.04,p 0.000
8. `cs_first_low40(day_std(Volume), day_std(Volume))` — enrichment,均值差 +2.00,p 0.001
9. `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` — enrichment,均值差 +1.66,p 0.005
10. `cross_zscore(cs_mask_top_replace_mean_neg(day_first(Volume)), 30)` — enrichment,均值差 +1.46,p 0.001
11. `day_gini(Close)` — enrichment,均值差 +1.38,p 0.009
12. `abs_(LogFloatShares)` — enrichment,均值差 +1.24,p 0.001
13. `cross_mean(day_gini(Volume), 30)` — enrichment,均值差 +1.18,p 0.001
14. `day_std(Volume)` — enrichment,均值差 +1.14,p 0.000
15. `day_sum(Volume)` — enrichment,均值差 +1.14,p 0.059
16. `day_sum(in_slice(Volume, 1, 239))` — enrichment,均值差 +1.11,p 0.008
17. `ts_autocorr_s1(day_argmax(Vwap), 20)` — enrichment,均值差 +1.03,p 0.041
18. `div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239)))` — enrichment,均值差 +1.03,p 0.034
19. `cs_rank(cross_mean(day_gini(Volume), 30))` — enrichment,均值差 +0.97,p 0.005
20. `cs_bucket_zscore(LogFloatShares, day_std(Volume))` — enrichment,均值差 +0.93,p 0.077
21. `cs_mask_top_replace_mean_neg(day_first(Volume))` — enrichment,均值差 +0.93,p 0.006
22. `day_centroid(Volume)` — enrichment,均值差 +0.90,p 0.000
23. `day_gini(Volume)` — enrichment,均值差 +0.89,p 0.002
24. `day_wmean(in_mean_full(Amt), in_mean_full(Amt))` — enrichment,均值差 +0.86,p 0.084
25. `day_first(Volume)` — enrichment,均值差 +0.82,p 0.005
26. `day_sum(in_slice(Volume, 211, 239))` — enrichment,均值差 +0.74,p 0.058
27. `cs_first_low20(cross_mean(day_centroid(Volume), 30), LogFloatCap)` — enrichment,均值差 +0.65,p 0.018
28. `day_var(in_mean_full(Volume))` — enrichment,均值差 +0.64,p 0.044
29. `cs_mask_top_replace_mean_neg(day_quantile_q25(Amt))` — enrichment,均值差 +0.56,p 0.079
30. `day_quantile_q25(Amt)` — enrichment,均值差 +0.56,p 0.069
31. `cross_zscore(cs_mask_top_replace_mean_neg(day_quantile_q25(Amt)), 30)` — enrichment,均值差 +0.55,p 0.098
32. `pow_2(day_std(Volume))` — enrichment,均值差 +0.43,p 0.053
33. `day_var(in_skew_full(Open))` — enrichment,均值差 +0.43,p 0.065

## 本组之前各轮的任务

- `prods907Pr1a_Na`:核心 `—`;评分 83,过线 1,入 heads 1;采样计数 {}
  - score +0.51(train +0.51 valid +1.35):`div(day_last(Close), div(ts_cov(day_durbin_watson(Close), day_distinct_ratio(Close), 50), FloatShares))`
  - score -0.13(train -0.13 valid +1.20):`ts_cov(day_durbin_watson(Close), day_durbin_watson(Close), 50)`
  - score -0.18(train -0.09 valid -0.18):`div(day_last(Close), div(FloatCap, FloatShares))`
  - score -0.19(train -0.19 valid -0.03):`cs_bucket_rank(div(day_last(Close), div(FloatCap, FloatShares)), LogFloatCap)`
  - score -0.21(train -0.21 valid +0.61):`sqrt(cross_ema(cs_last_low05(day_kurt(Ret), day_close(High)), 30))`
- `prods907Pr1b_Nb`:核心 `—`;评分 89,过线 14,入 heads 5;采样计数 {}
  - score +1.57(train +1.71 valid +1.57):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mean(day_gini(Volume), 30))`
  - score +1.17(train +1.17 valid +1.43):`sub(cs_rank(cross_mean(cross_mean(day_centroid(Volume), 30), 30)), cross_mean(day_gini(Volume), 30))`
  - score +0.99(train +0.99 valid +1.25):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))`
  - score +0.96(train +1.65 valid +0.96):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(cross_mean(day_gini(Amt), 30))))`
  - score +0.96(train +1.65 valid +0.96):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_gini(Amt), 30)))`
- `prods907Pr2a_Ea`:核心 `cross_mean(day_centroid(Volume), 30)`;评分 101,过线 4,入 heads 3;采样计数 {'c05_no_core': 2352, 'mutation_refused': 4, 'c05_periphery_seen': 4}
  - score +0.57(train +0.57 valid +1.71):`cs_first_low40(cs_first_low20(cross_mean(cs_first_high40(day_gini(Close), cross_mean(day_centroid(Volume), 30)), 30), LogFloatCap), LogFloatShares)`
  - score +0.57(train +0.57 valid +0.59):`ts_regres(day_wmean(in_mean_full(Amt), in_mean_full(Amt)), cross_mean(day_centroid(Volume), 30), 50)`
  - score +0.53(train +0.53 valid +0.64):`ts_regres(day_wmean(Amt, Amt), cross_mean(day_centroid(Volume), 30), 50)`
  - score +0.51(train +0.51 valid +1.00):`ts_regres(day_wmean(in_mean_full(Amt), in_mean_full(Amt)), cs_first_high40(day_gini(Open), cross_mean(day_centroid(Volume), 30)), 50)`
  - score +0.49(train +0.49 valid +1.63):`cs_first_high40(day_gini(Vwap), cross_mean(day_centroid(Volume), 30))`
- `prods907Pr2b_Nb`:核心 `—`;评分 60,过线 5,入 heads 1;采样计数 {}
  - score +1.79(train +1.95 valid +1.79):`cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 20)`
  - score +1.70(train +1.91 valid +1.70):`cross_mean(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume)), 20)`
  - score +1.66(train +1.66 valid +2.56):`cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 30)`
  - score +1.56(train +1.56 valid +1.69):`cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 5)`
  - score +1.49(train +1.55 valid +1.49):`cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 15)`

## 比原 head 好的拆解变体(R 候选)

(没有)
