# 定位:种子 806,C 组,第 3 轮(只含 train / valid)

快照:c05s806M1_I0_open_search, c05s806M2_I0_open_search, c05s806M3_I0_open_search, c06s806Cr1a_Ea, c06s806Cr1b_Nb, c06s806Cr2a_Ea, c06s806Cr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(14 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.78 | +2.05 | +1.78 | +1 | 20 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` |
| +1.40 | +1.40 | +3.15 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` |
| +1.32 | +1.32 | +3.02 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` |
| +1.22 | +1.22 | +1.34 | -1 | 5 | c05s806M2_I0_open_search | `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` |
| +1.18 | +1.18 | +2.76 | +1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))` |
| +1.13 | +1.30 | +1.13 | +1 | 0 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))` |
| +0.94 | +1.02 | +0.94 | -1 | 20 | c06s806Cr2a_Ea | `ts_quantile_q50(sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret)), 5)` |
| +0.93 | +0.93 | +1.74 | -1 | 5 | c06s806Cr2a_Ea | `ts_quantile_q50(sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret))), 20)` |
| +0.82 | +0.82 | +1.29 | -1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(ts_quantile_q50(cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)), 10))` |
| +0.81 | +0.81 | +2.58 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))` |
| +0.80 | +0.80 | +2.63 | -1 | 20 | c06s806Cr2b_Nb | `sub(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret)))))` |
| +0.68 | +0.68 | +1.74 | -1 | 20 | c06s806Cr2a_Ea | `ts_quantile_q50(ts_quantile_q75(sub(day_centroid(Amt), day_centroid(Ret)), 20), 20)` |
| +0.59 | +0.59 | +1.51 | -1 | 20 | c06s806Cr2a_Ea | `cs_bucket_rank(sub(ts_quantile_q50(day_centroid(Amt), 10), ts_quantile_q50(day_centroid(Amt), 50)), ts_quantile_q50(day_centroid(Amt), 50))` |
| +0.58 | +0.68 | +0.58 | +1 | 20 | c06s806Cr2a_Ea | `cs_first_low40(LogFloatShares, day_centroid(Amt))` |

## 共性:466 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.62 | 0.004 | 4 | +0.76 / -0.86 | `sqrt(day_q_stat_std(pow_1_5(Ret)))` |
| +1.62 | 0.004 | 4 | +0.76 / -0.86 | `cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))` |
| +1.60 | 0.001 | 6 | +0.73 / -0.87 | `sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_ar1_coefficient(Open))))` |
| +1.48 | 0.000 | 31 | +0.54 / -0.94 | `day_q_stat_std(pow_1_5(Ret))` |
| +1.43 | 0.000 | 11 | +0.55 / -0.88 | `day_at_min_ratio(Open)` |
| +1.40 | 0.000 | 10 | +0.53 / -0.88 | `cs_stddev_full(sqrt(day_at_min_ratio(Open)))` |
| +1.40 | 0.000 | 10 | +0.53 / -0.88 | `sqrt(day_at_min_ratio(Open))` |
| +1.37 | 0.000 | 16 | +0.48 / -0.89 | `pow_05(LogFloatShares)` |
| +1.35 | 0.026 | 4 | +0.50 / -0.86 | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` |
| +1.35 | 0.004 | 7 | +0.48 / -0.87 | `pow_1_5(LogFloatShares)` |
| +1.34 | 0.010 | 7 | +0.48 / -0.87 | `pow_05(pow_05(LogFloatShares))` |
| +1.34 | 0.014 | 5 | +0.48 / -0.86 | `abs_(LogFloatShares)` |
| +1.33 | 0.045 | 4 | +0.48 / -0.86 | `pow_05(pow_05(pow_05(LogFloatShares)))` |
| +1.32 | 0.000 | 20 | +0.42 / -0.90 | `ts_quantile_q50(day_centroid(Amt), 10)` |
| +1.18 | 0.003 | 9 | +0.31 / -0.87 | `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` |
| +1.14 | 0.002 | 12 | +0.26 / -0.88 | `log(day_open(Low))` |
| +1.13 | 0.017 | 5 | +0.27 / -0.86 | `cs_last_low40(LogFloatCap, day_quantile(Vwap))` |
| +1.04 | 0.060 | 4 | +0.19 / -0.85 | `ts_quantile_q50(day_centroid(Amt), 50)` |
| +1.04 | 0.035 | 7 | +0.18 / -0.86 | `day_quantile_q75(Amt)` |
| +1.01 | 0.002 | 16 | +0.13 / -0.88 | `day_open(Low)` |

## 拆解(26 次评估)

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

### head score +0.94:`ts_quantile_q50(sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret))` | -0.13 | -0.13 | +0.64 | — | (子树本身) |
| sufficiency | `sub(day_centroid(Amt), day_std(Ret))` | -0.10 | -0.10 | +0.57 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -2.56 | -2.56 | -2.40 | — | (子树本身) |
| knockout | `sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret))` | +1.01 | +1.08 | +1.01 | -0.07 | `ts_quantile_q50(sub(day_centroid(Amt), day_std(Ret)), 5)` |
| swap | `Amt->Volume` | +0.92 | +1.02 | +0.92 | — | `ts_quantile_q50(sub(sub(day_centroid(Volume), day_std(Ret)), day_std(Ret)), 5)` |
| window | `ts_quantile_q50@5->2` | +0.50 | +0.50 | +1.03 | — | `ts_quantile_q50(sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret)), 2)` |
| window | `ts_quantile_q50@5->10` | +0.93 | +1.07 | +0.93 | — | `ts_quantile_q50(sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret)), 10)` |

### head score +0.93:`ts_quantile_q50(sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret)))` | +0.50 | +0.50 | +1.57 | — | (子树本身) |
| sufficiency | `mul(day_centroid(Amt), day_centroid(Ret))` | -1.91 | -0.64 | -1.91 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| knockout | `sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret)))` | +1.21 | +1.21 | +1.27 | -0.27 | `ts_quantile_q50(day_centroid(Amt), 20)` |
| knockout | `mul(day_centroid(Amt), day_centroid(Ret))` | — | — | — | — | `ts_quantile_q50(sub(day_centroid(Amt), day_centroid(Amt)), 20)` |
| swap | `Amt->Volume` | +0.98 | +0.98 | +1.72 | — | `ts_quantile_q50(sub(day_centroid(Volume), mul(day_centroid(Volume), day_centroid(Ret))), 20)` |
| window | `ts_quantile_q50@20->10` | +0.68 | +0.68 | +1.38 | — | `ts_quantile_q50(sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret))), 10)` |
| window | `ts_quantile_q50@20->40` | +0.84 | +0.84 | +1.81 | — | `ts_quantile_q50(sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `sqrt(day_q_stat_std(pow_1_5(Ret)))` — enrichment,均值差 +1.62,p 0.004
2. `cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))` — enrichment,均值差 +1.62,p 0.004
3. `sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_ar1_coefficient(Open))))` — enrichment,均值差 +1.60,p 0.001
4. `day_q_stat_std(pow_1_5(Ret))` — enrichment,均值差 +1.48,p 0.000
5. `day_at_min_ratio(Open)` — enrichment,均值差 +1.43,p 0.000
6. `cs_stddev_full(sqrt(day_at_min_ratio(Open)))` — enrichment,均值差 +1.40,p 0.000
7. `sqrt(day_at_min_ratio(Open))` — enrichment,均值差 +1.40,p 0.000
8. `pow_05(LogFloatShares)` — enrichment,均值差 +1.37,p 0.000
9. `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` — enrichment,均值差 +1.35,p 0.026
10. `pow_1_5(LogFloatShares)` — enrichment,均值差 +1.35,p 0.004
11. `pow_05(pow_05(LogFloatShares))` — enrichment,均值差 +1.34,p 0.010
12. `abs_(LogFloatShares)` — enrichment,均值差 +1.34,p 0.014
13. `pow_05(pow_05(pow_05(LogFloatShares)))` — enrichment,均值差 +1.33,p 0.045
14. `ts_quantile_q50(day_centroid(Amt), 10)` — enrichment,均值差 +1.32,p 0.000
15. `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` — enrichment,均值差 +1.18,p 0.003
16. `log(day_open(Low))` — enrichment,均值差 +1.14,p 0.002
17. `cs_last_low40(LogFloatCap, day_quantile(Vwap))` — enrichment,均值差 +1.13,p 0.017
18. `ts_quantile_q50(day_centroid(Amt), 50)` — enrichment,均值差 +1.04,p 0.060
19. `day_quantile_q75(Amt)` — enrichment,均值差 +1.04,p 0.035
20. `day_open(Low)` — enrichment,均值差 +1.01,p 0.002
21. `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` — enrichment,均值差 +0.98,p 0.054
22. `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` — enrichment,均值差 +0.96,p 0.032
23. `day_quantile_q75(pow_2_5(Close))` — enrichment,均值差 +0.95,p 0.027
24. `sqrt(day_ar1_coefficient(Open))` — enrichment,均值差 +0.78,p 0.006
25. `day_centroid(Ret)` — enrichment,均值差 +0.74,p 0.001
26. `day_ar1_coefficient(Open)` — enrichment,均值差 +0.72,p 0.004
27. `day_open(Open)` — enrichment,均值差 +0.70,p 0.018
28. `cs_stddev_full(sqrt(day_ar1_coefficient(Open)))` — enrichment,均值差 +0.70,p 0.016
29. `day_centroid(Amt)` — enrichment,均值差 +0.69,p 0.000
30. `sub(day_centroid(Amt), day_centroid(Ret))` — enrichment,均值差 +0.60,p 0.007

## 本组之前各轮的任务

- `c06s806Cr1a_Ea`:核心 `day_cov(Vwap, Ret)`;评分 77,过线 0,入 heads 0;采样计数 {'c05_no_core': 1616, 'c05_periphery_seen': 9}
  - score -0.09(train +0.10 valid -0.09):`ts_corr(day_cov(Vwap, Ret), cross_reg_fvalue(cross_autocorr_s1(day_cov(Vwap, Ret), 241), day_cov(Vwap, Ret), 3), 40)`
  - score -0.10(train -0.10 valid -0.05):`ts_corr(day_cov(Vwap, Ret), cross_reg_fvalue(day_q_stat_std(Low), day_cov(Vwap, Ret), 3), 40)`
  - score -0.36(train -0.36 valid +0.10):`inv(cross_autocorr_s1(day_cov(Vwap, Ret), 241))`
  - score -0.38(train -0.38 valid +0.63):`inv(cross_decay_linear(day_cov(Vwap, Ret), 10))`
  - score -0.40(train -0.40 valid +1.50):`inv(cross_decay_linear(day_cov(Vwap, Ret), 30))`
- `c06s806Cr1b_Nb`:核心 `—`;评分 62,过线 0,入 heads 0;采样计数 {}
  - score +0.12(train +0.12 valid +1.34):`cross_mean(sub(cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Amt, Ret)), 20), day_signed_ratio(Amt, Ret)), 20)`
  - score +0.06(train +0.06 valid +2.33):`cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 60)`
  - score -0.12(train -0.12 valid +1.93):`cross_mean(sub(cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 20), day_signed_ratio(Ret, Ret)), 20)`
  - score -0.13(train -0.13 valid +2.26):`cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 20)`
  - score -0.21(train -0.21 valid +2.31):`cross_mean(sub(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), day_signed_ratio(Ret, Ret)), 20)`
- `c06s806Cr2a_Ea`:核心 `day_centroid(Amt)`;评分 75,过线 16,入 heads 5;采样计数 {'c05_no_core': 802, 'c05_periphery_seen': 9}
  - score +0.94(train +1.02 valid +0.94):`ts_quantile_q50(sub(sub(day_centroid(Amt), day_std(Ret)), day_std(Ret)), 5)`
  - score +0.93(train +0.93 valid +1.74):`ts_quantile_q50(sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret))), 20)`
  - score +0.93(train +0.93 valid +1.29):`ts_quantile_q50(sub(day_centroid(Amt), day_centroid(Ret)), 30)`
  - score +0.90(train +0.90 valid +1.05):`sub(day_centroid(Amt), day_centroid(Ret))`
  - score +0.87(train +0.87 valid +1.08):`ts_quantile_q50(sub(day_centroid(Amt), day_centroid(Ret)), 20)`
- `c06s806Cr2b_Nb`:核心 `—`;评分 87,过线 26,入 heads 1;采样计数 {}
  - score +0.80(train +0.80 valid +2.63):`sub(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret)))))`
  - score +0.79(train +0.79 valid +2.61):`sub(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(sub(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret)))))))), cs_stddev_full(sqrt(sub(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))), cs_stddev_full(sqrt(day_q_stat_std(pow_1_5(Ret))))))))`
  - score +0.77(train +0.77 valid +2.60):`sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_ar1_coefficient(Open)))))))`
  - score +0.76(train +0.76 valid +2.61):`sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(day_ar1_coefficient(Open))))`
  - score +0.76(train +0.76 valid +2.61):`sub(sub(sub(day_q_stat_std(pow_1_5(Ret)), cs_stddev_full(sqrt(cs_stddev_full(sqrt(day_at_min_ratio(Open)))))), cs_demean(sqrt(cs_stddev_full(sqrt(day_at_min_ratio(Open)))))), cs_stddev_full(sqrt(day_ar1_coefficient(Open))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(knockout sub(day_centroid(Amt), mul(day_centroid(Amt), day_centroid(Ret)))):`ts_quantile_q50(day_centroid(Amt), 20)`
- 增益 +0.12(window cross_quantile_q25@3->2):`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 2))`
