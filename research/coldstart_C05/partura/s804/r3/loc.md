# 定位:种子 804,B 组,第 3 轮(只含 train / valid)

快照:c05s804M1_I0_open_search, c05s804M2_I0_open_search, c05s804M3_I0_open_search, c05s804Br1a_Ea, c05s804Br1b_Nb, c05s804Br2a_Ea, c05s804Br2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(18 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.23 | +1.42 | +1.23 | -1 | 5 | c05s804Br1b_Nb | `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 20)` |
| +0.91 | +0.91 | +1.87 | +1 | 0 | c05s804M1_I0_open_search | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.88 | +0.88 | +1.05 | -1 | 20 | c05s804Br1b_Nb | `sub(day_centroid(Volume), day_centroid(Ret))` |
| +0.88 | +0.88 | +2.81 | +1 | 5 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| +0.84 | +0.84 | +2.35 | +1 | 5 | c05s804Br1a_Ea | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)` |
| +0.78 | +0.78 | +1.94 | +1 | 0 | c05s804M1_I0_open_search | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.73 | +0.73 | +1.95 | +1 | 20 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| +0.71 | +0.71 | +0.82 | -1 | 20 | c05s804Br2b_Nb | `abs_(ts_mean(day_signed_ratio(Ret, Amt), 20))` |
| +0.67 | +0.67 | +1.59 | +1 | 20 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| +0.67 | +0.67 | +1.43 | +1 | 0 | c05s804Br1a_Ea | `sqrt(cs_flip_by_state(day_mean(Open), day_mean(Open)))` |
| +0.67 | +0.67 | +1.33 | -1 | 20 | c05s804Br1b_Nb | `add(day_cov(in_index(Volume), Volume), day_centroid(Ret))` |
| +0.65 | +0.65 | +2.79 | +1 | 20 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.64 | +0.64 | +2.12 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10))` |
| +0.60 | +0.60 | +1.66 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60), cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60))` |
| +0.59 | +0.59 | +1.83 | +1 | 20 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50), 3), 3), 50))` |
| +0.58 | +0.58 | +1.90 | +1 | 20 | c05s804M1_I0_open_search | `sub(sub(sub(sub(ts_mean(abs_(neg(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10))))), 30), ts_var(day_gini(High), 10)), ts_var(day_gini(High), 10)), day_centroid(sqrt(Volume))), day_centroid(sqrt(Volume)))` |
| +0.57 | +0.57 | +1.28 | -1 | 20 | c05s804M3_I0_open_search | `inv(day_es_ratio_lo(add(Volume, Vwap)))` |
| +0.51 | +0.51 | +2.04 | +1 | 5 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_topw_mean(Amt, Ret), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` |

## 共性:589 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.78 | 0.000 | 6 | +0.82 / -0.96 | `ts_var(day_gini(High), 5)` |
| +1.76 | 0.000 | 5 | +0.80 / -0.96 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` |
| +1.75 | 0.000 | 4 | +0.79 / -0.96 | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.66 | 0.000 | 14 | +0.67 / -0.98 | `ts_decay_linear(pow_3(day_mean(Open)), 20)` |
| +1.61 | 0.001 | 4 | +0.65 / -0.96 | `cross_ema(cross_ema(LogFloatShares, 241), 241)` |
| +1.56 | 0.000 | 7 | +0.59 / -0.96 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.54 | 0.001 | 5 | +0.59 / -0.96 | `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` |
| +1.54 | 0.001 | 4 | +0.59 / -0.96 | `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` |
| +1.53 | 0.000 | 15 | +0.55 / -0.98 | `pow_3(day_mean(Open))` |
| +1.53 | 0.003 | 4 | +0.58 / -0.96 | `day_cov(in_index(Volume), Volume)` |
| +1.47 | 0.000 | 12 | +0.50 / -0.97 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` |
| +1.36 | 0.008 | 5 | +0.41 / -0.96 | `day_es_ratio_lo(add(Volume, Vwap))` |
| +1.32 | 0.010 | 5 | +0.37 / -0.96 | `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` |
| +1.27 | 0.001 | 7 | +0.31 / -0.96 | `abs_(ts_mean(day_signed_ratio(Ret, Amt), 20))` |
| +1.25 | 0.000 | 59 | +0.18 / -1.07 | `cross_ema(LogFloatShares, 241)` |
| +1.23 | 0.001 | 9 | +0.27 / -0.96 | `day_centroid(sqrt(Volume))` |
| +1.20 | 0.000 | 12 | +0.23 / -0.97 | `ts_mean(day_signed_ratio(Ret, Amt), 20)` |
| +1.14 | 0.026 | 4 | +0.18 / -0.95 | `ts_quantile_q50(day_gini(High), 10)` |
| +1.14 | 0.024 | 4 | +0.18 / -0.95 | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3)` |
| +1.14 | 0.024 | 4 | +0.18 / -0.95 | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3)` |

## 拆解(28 次评估)

### head score +1.23:`ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(day_centroid(Volume), LogFloatCap)` | +0.11 | +0.52 | +0.11 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| knockout | `cs_bucket_rank(day_centroid(Volume), LogFloatCap)` | +1.24 | +1.24 | +1.72 | -0.02 | `ts_mean(day_centroid(Volume), 20)` |
| swap | `Volume->Amt` | +1.16 | +1.46 | +1.16 | — | `ts_mean(cs_bucket_rank(day_centroid(Amt), LogFloatCap), 20)` |
| window | `ts_mean@20->10` | +0.67 | +1.26 | +0.67 | — | `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 10)` |
| window | `ts_mean@20->40` | +0.79 | +1.18 | +0.79 | — | `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 40)` |

### head score +0.71:`abs_(ts_mean(day_signed_ratio(Ret, Amt), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(day_signed_ratio(Ret, Amt), 20)` | -0.34 | -0.34 | +1.65 | — | (子树本身) |
| sufficiency | `day_signed_ratio(Ret, Amt)` | -2.50 | -2.50 | +1.28 | — | (子树本身) |
| knockout | `ts_mean(day_signed_ratio(Ret, Amt), 20)` | -1.51 | -1.51 | +0.12 | +2.23 | `abs_(day_signed_ratio(Ret, Amt))` |
| swap | `Amt->Volume` | +0.72 | +0.72 | +0.94 | — | `abs_(ts_mean(day_signed_ratio(Ret, Volume), 20))` |
| window | `ts_mean@20->10` | -0.32 | -0.32 | +0.12 | — | `abs_(ts_mean(day_signed_ratio(Ret, Amt), 10))` |
| window | `ts_mean@20->40` | +1.07 | +1.07 | +1.42 | — | `abs_(ts_mean(day_signed_ratio(Ret, Amt), 40))` |

### head score +0.67:`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50)` | -2.56 | -1.06 | -2.56 | — | (子树本身) |
| sufficiency | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3)` | -4.67 | -3.32 | -4.67 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(pow_05(Amt))` | -0.36 | -0.36 | +0.03 | — | (子树本身) |
| knockout | `ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50)` | -2.68 | -0.81 | -2.68 | +3.36 | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), day_median(Volume))` |
| knockout | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3)` | -0.37 | -0.37 | +2.57 | +1.05 | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cs_flip_by_state(LogFloatShares, day_mean(Open)), 50))` |
| knockout | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3)` | -0.71 | -0.71 | -0.31 | +1.39 | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cs_flip_by_state(LogFloatShares, day_mean(Open)), 3), 50))` |
| knockout | `cs_flip_by_state(LogFloatShares, day_mean(Open))` | — | — | — | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(LogFloatShares, cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| swap | `Amt->Volume` | +0.64 | +0.64 | +1.63 | — | `cs_first_high20(day_autocorr_n1(pow_05(Volume)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Volume, Ret), 3), 3), 50))` |
| swap | `Volume->Amt` | -0.24 | +0.56 | -0.24 | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Amt), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| window | `ts_reg_tvalue@50->25` | -0.62 | +0.15 | -0.62 | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 25))` |
| window | `ts_reg_tvalue@50->100` | +0.91 | +0.91 | +2.39 | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 100))` |

### head score +0.67:`sqrt(cs_flip_by_state(day_mean(Open), day_mean(Open)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_flip_by_state(day_mean(Open), day_mean(Open))` | -1.21 | -1.21 | -0.08 | — | (子树本身) |
| sufficiency | `day_mean(Open)` | -1.16 | -1.16 | -0.44 | — | (子树本身) |
| knockout | `cs_flip_by_state(day_mean(Open), day_mean(Open))` | -1.15 | -1.15 | -0.44 | +1.83 | `sqrt(day_mean(Open))` |
| swap | `Open->Close` | +0.69 | +0.69 | +1.43 | — | `sqrt(cs_flip_by_state(day_mean(Close), day_mean(Close)))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_var(day_gini(High), 5)` — enrichment,均值差 +1.78,p 0.000
2. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` — enrichment,均值差 +1.76,p 0.000
3. `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +1.75,p 0.000
4. `ts_decay_linear(pow_3(day_mean(Open)), 20)` — enrichment,均值差 +1.66,p 0.000
5. `cross_ema(cross_ema(LogFloatShares, 241), 241)` — enrichment,均值差 +1.61,p 0.001
6. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.56,p 0.000
7. `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` — enrichment,均值差 +1.54,p 0.001
8. `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` — enrichment,均值差 +1.54,p 0.001
9. `pow_3(day_mean(Open))` — enrichment,均值差 +1.53,p 0.000
10. `day_cov(in_index(Volume), Volume)` — enrichment,均值差 +1.53,p 0.003
11. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` — enrichment,均值差 +1.47,p 0.000
12. `day_es_ratio_lo(add(Volume, Vwap))` — enrichment,均值差 +1.36,p 0.008
13. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` — enrichment,均值差 +1.32,p 0.010
14. `abs_(ts_mean(day_signed_ratio(Ret, Amt), 20))` — enrichment,均值差 +1.27,p 0.001
15. `cross_ema(LogFloatShares, 241)` — enrichment,均值差 +1.25,p 0.000
16. `day_centroid(sqrt(Volume))` — enrichment,均值差 +1.23,p 0.001
17. `ts_mean(day_signed_ratio(Ret, Amt), 20)` — enrichment,均值差 +1.20,p 0.000
18. `ts_quantile_q50(day_gini(High), 10)` — enrichment,均值差 +1.14,p 0.026
19. `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3)` — enrichment,均值差 +1.14,p 0.024
20. `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3)` — enrichment,均值差 +1.14,p 0.024
21. `day_autocorr_n1(pow_05(Amt))` — enrichment,均值差 +1.09,p 0.000
22. `day_gini(High)` — enrichment,均值差 +1.08,p 0.000
23. `ts_var(day_gini(High), 10)` — enrichment,均值差 +1.07,p 0.000
24. `abs_(day_corr(Vwap, High))` — enrichment,均值差 +1.07,p 0.043
25. `cs_mask_top_replace_mean_neg(day_last(Low))` — enrichment,均值差 +1.05,p 0.045
26. `day_signed_ratio(Close, Low)` — enrichment,均值差 +1.03,p 0.010
27. `abs_(day_wstd(Vwap, High))` — enrichment,均值差 +0.96,p 0.049
28. `day_wstd(Vwap, High)` — enrichment,均值差 +0.96,p 0.049
29. `inv(cs_mask_top_replace_mean_neg(day_last(Low)))` — enrichment,均值差 +0.95,p 0.095
30. `cross_delay(day_signed_ratio(Close, Low), 60)` — enrichment,均值差 +0.94,p 0.046
31. `day_signed_ratio(High, Open)` — enrichment,均值差 +0.91,p 0.000
32. `cross_delay(day_signed_ratio(High, Open), 60)` — enrichment,均值差 +0.91,p 0.001
33. `day_median(Volume)` — enrichment,均值差 +0.82,p 0.001
34. `day_last(Low)` — enrichment,均值差 +0.80,p 0.068
35. `day_signed_ratio(Low, Low)` — enrichment,均值差 +0.62,p 0.061
36. `cs_mask_top_replace_mean(day_durbin_watson(Ret))` — enrichment,均值差 +0.62,p 0.004
37. `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` — enrichment,均值差 +0.61,p 0.077
38. `sub(cross_ema(LogFloatShares, 241), ts_var(LogFloatShares, 10))` — enrichment,均值差 +0.61,p 0.048
39. `ts_stddev(day_signed_ratio(Low, Low), 10)` — enrichment,均值差 +0.59,p 0.084
40. `cs_flip_by_state(LogFloatShares, day_mean(Open))` — enrichment,均值差 +0.57,p 0.029
41. `day_signed_ratio(Ret, Amt)` — enrichment,均值差 +0.57,p 0.004
42. `ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)` — enrichment,均值差 +0.56,p 0.060
43. `pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret)))` — enrichment,均值差 +0.55,p 0.022
44. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.55,p 0.017
45. `day_durbin_watson(Ret)` — enrichment,均值差 +0.54,p 0.009
46. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)` — enrichment,均值差 +0.50,p 0.089
47. `day_topw_mean(Amt, Ret)` — enrichment,均值差 +0.30,p 0.027
48. `cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3)` — enrichment,均值差 +0.27,p 0.062
49. `cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3)` — enrichment,均值差 +0.27,p 0.048

## 本组之前各轮的任务

- `c05s804Br1a_Ea`:核心 `day_mean(Open)`;评分 95,过线 8,入 heads 6;采样计数 {'c05_no_core': 701, 'c05_periphery_seen': 3}
  - score +0.84(train +0.84 valid +2.35):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)`
  - score +0.73(train +0.73 valid +1.95):`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))`
  - score +0.68(train +0.68 valid +1.62):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), day_mean(Open))`
  - score +0.67(train +0.67 valid +1.59):`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))`
  - score +0.65(train +0.65 valid +1.89):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)`
- `c05s804Br1b_Nb`:核心 `—`;评分 81,过线 5,入 heads 3;采样计数 {}
  - score +0.88(train +0.88 valid +1.05):`sub(day_centroid(Volume), day_centroid(Ret))`
  - score +0.71(train +0.71 valid +1.57):`cs_bucket_rank(day_centroid(Volume), day_centroid(Ret))`
  - score +0.67(train +1.26 valid +0.67):`ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 10)`
  - score +0.67(train +0.67 valid +1.33):`add(day_cov(in_index(Volume), Volume), day_centroid(Ret))`
  - score +0.67(train +0.67 valid +1.33):`sub(add(day_cov(in_index(Volume), Volume), day_centroid(Ret)), day_centroid(Ret))`
- `c05s804Br2a_Ea`:核心 `sub(day_centroid(Volume), day_centroid(Ret))`;评分 104,过线 0,入 heads 0;采样计数 {'c05_no_core': 3092, 'c05_periphery_seen': 1, 'c05_skeleton': 1}
  - score -0.24(train -0.24 valid +1.86):`ts_sum(cs_first_low20(cs_stddev_full(sub(sub(day_centroid(Volume), day_centroid(Ret)), ts_sum(cs_first_low20(cs_stddev_full(day_quantile_q25(Ret)), sub(sub(day_centroid(Volume), day_centroid(Ret)), day_centroid(Ret))), 5))), sub(sub(day_centroid(Volume), day_centroid(Ret)), day_centroid(Ret))), 30)`
  - score -0.40(train -0.40 valid +0.31):`ts_sum(cs_first_low20(ts_sum(cs_first_low20(cs_stddev_full(day_quantile_q25(Vwap)), sub(sub(day_centroid(Volume), day_centroid(Ret)), day_centroid(Ret))), 30), sub(sub(day_centroid(Volume), day_centroid(Ret)), day_centroid(Ret))), 30)`
  - score -0.44(train -0.44 valid +1.47):`ts_sum(cs_first_low20(cs_stddev_full(day_kurt(Ret)), sub(day_centroid(Volume), ts_sum(cs_first_low20(cs_stddev_full(day_quantile_q25(Ret)), sub(day_centroid(Volume), day_centroid(Ret))), 30))), 20)`
  - score -0.54(train -0.54 valid +1.96):`ts_sum(cs_first_low20(cs_stddev_full(day_kurt(Ret)), sub(day_centroid(Volume), day_centroid(Ret))), 20)`
  - score -0.54(train -0.54 valid +1.96):`ts_sum(cs_first_low20(cs_stddev_full(day_centroid(Ret)), sub(day_centroid(Volume), day_centroid(Ret))), 20)`
- `c05s804Br2b_Nb`:核心 `—`;评分 78,过线 9,入 heads 1;采样计数 {}
  - score +0.71(train +0.71 valid +0.82):`abs_(ts_mean(day_signed_ratio(Ret, Amt), 20))`
  - score +0.71(train +0.71 valid +0.82):`abs_(abs_(ts_mean(day_signed_ratio(Ret, Amt), 20)))`
  - score +0.70(train +0.70 valid +0.73):`abs_(ts_mean(ts_mean(day_signed_ratio(Ret, Amt), 20), 20))`
  - score +0.63(train +0.63 valid +0.92):`ts_mean(abs_(ts_mean(day_signed_ratio(Ret, Amt), 20)), 10)`
  - score +0.62(train +0.62 valid +1.09):`ts_mean(abs_(ts_mean(day_signed_ratio(Ret, Amt), 20)), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.35(window ts_mean@20->40):`abs_(ts_mean(day_signed_ratio(Ret, Amt), 40))`
- 增益 +0.24(window ts_reg_tvalue@50->100):`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 100))`
