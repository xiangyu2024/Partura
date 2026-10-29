# 定位:种子 807,B 组,第 3 轮(只含 train / valid)

快照:c05s807M1_I0_open_search, c05s807M2_I0_open_search, c05s807M3_I0_open_search, c05s807Br1a_Ea, c05s807Br1b_Nb, c05s807Br2a_Ea, c05s807Br2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(29 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +2.04 | +2.04 | +3.16 | -1 | 20 | c05s807M2_I0_open_search | `pow_2_5(pow_3(day_var(Ret)))` |
| +1.78 | +2.45 | +1.78 | +1 | 0 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)` |
| +1.75 | +1.76 | +1.75 | -1 | 0 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 60)` |
| +1.71 | +1.71 | +2.50 | -1 | 20 | c05s807M1_I0_open_search | `pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))` |
| +1.21 | +1.39 | +1.21 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)` |
| +1.21 | +1.21 | +1.60 | -1 | 5 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)` |
| +1.20 | +2.03 | +1.20 | -1 | 5 | c05s807M3_I0_open_search | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| +1.10 | +1.10 | +2.05 | -1 | 0 | c05s807M2_I0_open_search | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +1.09 | +1.89 | +1.09 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 15)` |
| +1.02 | +1.16 | +1.02 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 5)))), 10)` |
| +1.00 | +1.00 | +2.37 | +1 | 5 | c05s807Br2b_Nb | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_last(Open)))` |
| +1.00 | +1.00 | +2.71 | +1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret)))), day_flat_ratio(Ret), 20)` |
| +0.90 | +0.90 | +1.47 | -1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(day_mean(Ret)), pow_2(day_wmean(Ret, Ret)), 20)` |
| +0.75 | +1.14 | +0.75 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_last(in_sum_rolling(Volume, 5))), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| +0.75 | +0.75 | +1.01 | -1 | 5 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| +0.74 | +1.05 | +0.74 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(in_sum_rolling(Volume, 5), 5)), inv(cs_demean(day_distinct_ratio(Volume))), 10)` |
| +0.71 | +0.71 | +2.10 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))), 15)` |
| +0.71 | +2.02 | +0.71 | +1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))), 20)` |
| +0.70 | +1.01 | +0.70 | +1 | 5 | c05s807Br2b_Nb | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open))))` |
| +0.68 | +0.68 | +1.62 | -1 | 20 | c05s807Br1b_Nb | `pow_2(pow_2(pow_2(day_topw_mean(Ret, Amt))))` |
| +0.67 | +1.00 | +0.67 | -1 | 5 | c05s807M3_I0_open_search | `cross_regbeta(day_last(Volume), cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume)), 15)` |
| +0.67 | +0.67 | +1.17 | +1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(day_signed_ratio(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)` |
| +0.66 | +0.86 | +0.66 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(Volume), inv(cs_demean(day_distinct_ratio(Volume))), 10)` |
| +0.63 | +0.63 | +1.85 | -1 | 20 | c05s807Br2a_Ea | `cs_last_high40(cs_stddev_full(day_durbin_watson(High)), cross_corr(day_durbin_watson(High), day_quantile(Volume), 20))` |
| +0.63 | +0.63 | +0.73 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cross_regbeta(cs_normalize(day_std(High)), cs_demean(day_distinct_ratio(Volume)), 30), 10)` |
| +0.60 | +0.99 | +0.60 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cs_mask_top_replace_mean_neg(cs_robust_z(day_argmax(Volume))), 10)` |
| +0.58 | +0.58 | +0.93 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cross_regbeta(cs_normalize(day_std(High)), cs_sum(day_distinct_ratio(Volume)), 15), 10)` |
| +0.54 | +1.61 | +0.54 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 3)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 3)))), 10)` |
| +0.52 | +0.52 | +0.84 | +1 | 0 | c05s807M2_I0_open_search | `ts_sum(LogFloatShares, 30)` |

## 共性:513 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.64 | 0.000 | 16 | +0.84 / -0.80 | `ts_sum(pow_3(day_durbin_watson(High)), 1)` |
| +1.63 | 0.000 | 7 | +0.86 / -0.77 | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` |
| +1.45 | 0.000 | 30 | +0.62 / -0.83 | `pow_3(day_durbin_watson(High))` |
| +1.40 | 0.008 | 4 | +0.64 / -0.76 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +1.26 | 0.017 | 4 | +0.50 / -0.76 | `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` |
| +1.24 | 0.014 | 4 | +0.48 / -0.76 | `pow_3(pow_2_5(LogFloatShares))` |
| +1.23 | 0.005 | 6 | +0.47 / -0.76 | `cross_fangzheng(pow_2_5(LogFloatShares), 60)` |
| +1.19 | 0.012 | 7 | +0.42 / -0.76 | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +1.16 | 0.004 | 8 | +0.39 / -0.76 | `cs_mask_top_replace_mean_neg(day_quantile(Open))` |
| +1.13 | 0.001 | 12 | +0.36 / -0.77 | `cross_stddev(day_durbin_watson(High), 60)` |
| +1.05 | 0.001 | 13 | +0.27 / -0.77 | `pow_2_5(LogFloatShares)` |
| +0.92 | 0.001 | 17 | +0.14 / -0.78 | `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` |
| +0.91 | 0.001 | 18 | +0.13 / -0.78 | `cs_robust_z(day_distinct_ratio(Volume))` |
| +0.90 | 0.108 | 4 | +0.15 / -0.75 | `cs_stddev_full(sub(day_durbin_watson(High), day_quantile_q75(Ret)))` |
| +0.81 | 0.005 | 20 | +0.03 / -0.78 | `day_quantile(Open)` |
| +0.80 | 0.149 | 4 | +0.05 / -0.75 | `cross_regres(LogFloatCap, day_durbin_watson(High), 60)` |
| +0.79 | 0.040 | 12 | +0.03 / -0.76 | `log(LogFloatCap)` |
| +0.76 | 0.072 | 8 | -0.00 / -0.76 | `sub(day_durbin_watson(High), day_quantile_q75(Ret))` |
| +0.74 | 0.021 | 13 | -0.02 / -0.77 | `cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))` |
| +0.73 | 0.001 | 31 | -0.06 / -0.79 | `day_last(in_sum_rolling(Volume, 5))` |

## 拆解(27 次评估)

### head score +2.04:`pow_2_5(pow_3(day_var(Ret)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_3(day_var(Ret))` | +1.11 | +1.11 | +3.05 | — | (子树本身) |
| sufficiency | `day_var(Ret)` | -1.55 | -1.55 | +0.13 | — | (子树本身) |
| knockout | `pow_3(day_var(Ret))` | +0.70 | +0.70 | +2.70 | +1.34 | `pow_2_5(day_var(Ret))` |

### head score +1.21:`cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10))))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_last(in_sum_rolling(Volume, 10))` | -2.01 | +0.07 | -2.01 | — | (子树本身) |
| sufficiency | `day_distinct_ratio(in_sum_rolling(Volume, 10))` | — | — | — | — | 门槛废品 |
| knockout | `inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10))))` | +0.09 | +0.09 | +1.04 | +1.13 | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10))), 10)` |
| knockout | `cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))` | +0.10 | +0.10 | +0.61 | +1.11 | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(day_distinct_ratio(in_sum_rolling(Volume, 10))), 10)` |
| swap | `Volume->Amt` | +0.64 | +0.64 | +2.24 | — | `cross_regbeta(day_last(in_sum_rolling(Amt, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Amt, 10)))), 10)` |
| window | `cross_regbeta@10->5` | +0.56 | +0.56 | +0.94 | — | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 5)` |
| window | `cross_regbeta@10->20` | +1.15 | +1.42 | +1.15 | — | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 20)` |

### head score +1.21:`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_wmean(Ret, Ret))` | +0.89 | +0.89 | +1.66 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |
| knockout | `pow_2(day_wmean(Ret, Ret))` | -0.31 | -0.31 | -0.01 | +1.52 | `cross_corr(day_wmean(Ret, Ret), pow_2(day_wmean(Ret, Ret)), 20)` |
| knockout | `pow_2(day_wmean(Ret, Ret))` | -0.31 | -0.31 | -0.01 | +1.52 | `cross_corr(pow_2(day_wmean(Ret, Ret)), day_wmean(Ret, Ret), 20)` |
| window | `cross_corr@20->10` | +0.76 | +0.76 | +0.94 | — | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 10)` |
| window | `cross_corr@20->40` | +0.90 | +0.90 | +0.97 | — | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 40)` |

### head score +1.20:`cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_robust_z(day_distinct_ratio(Volume))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_std(Volume)` | -1.60 | +0.17 | -1.60 | — | (子树本身) |
| sufficiency | `day_distinct_ratio(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` | -0.26 | -0.26 | +0.08 | +1.46 | `cross_regbeta(day_std(Volume), cs_robust_z(day_distinct_ratio(Volume)), 15)` |
| knockout | `cs_robust_z(day_distinct_ratio(Volume))` | +1.29 | +1.43 | +1.29 | -0.09 | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume)), 15)` |
| swap | `Volume->Amt` | +0.99 | +0.99 | +2.28 | — | `cross_regbeta(day_std(Amt), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Amt))), 15)` |
| window | `cross_regbeta@15->7` | +0.74 | +1.58 | +0.74 | — | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 7)` |
| window | `cross_regbeta@15->30` | +0.97 | +2.10 | +0.97 | — | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2(day_wmean(Ret, Ret))` — ablation,自身 score +0.89(所在 head +1.21)
2. `ts_sum(pow_3(day_durbin_watson(High)), 1)` — enrichment,均值差 +1.64,p 0.000
3. `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` — enrichment,均值差 +1.63,p 0.000
4. `pow_3(day_durbin_watson(High))` — enrichment,均值差 +1.45,p 0.000
5. `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` — enrichment,均值差 +1.40,p 0.008
6. `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` — enrichment,均值差 +1.26,p 0.017
7. `pow_3(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.24,p 0.014
8. `cross_fangzheng(pow_2_5(LogFloatShares), 60)` — enrichment,均值差 +1.23,p 0.005
9. `pow_2(pow_2(day_wmean(Ret, Ret)))` — enrichment,均值差 +1.19,p 0.012
10. `cs_mask_top_replace_mean_neg(day_quantile(Open))` — enrichment,均值差 +1.16,p 0.004
11. `cross_stddev(day_durbin_watson(High), 60)` — enrichment,均值差 +1.13,p 0.001
12. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.05,p 0.001
13. `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` — enrichment,均值差 +0.92,p 0.001
14. `cs_robust_z(day_distinct_ratio(Volume))` — enrichment,均值差 +0.91,p 0.001
15. `day_quantile(Open)` — enrichment,均值差 +0.81,p 0.005
16. `log(LogFloatCap)` — enrichment,均值差 +0.79,p 0.040
17. `sub(day_durbin_watson(High), day_quantile_q75(Ret))` — enrichment,均值差 +0.76,p 0.072
18. `cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))` — enrichment,均值差 +0.74,p 0.021
19. `day_last(in_sum_rolling(Volume, 5))` — enrichment,均值差 +0.73,p 0.001
20. `day_distinct_ratio(Volume)` — enrichment,均值差 +0.65,p 0.000
21. `pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))` — enrichment,均值差 +0.60,p 0.049
22. `day_std(Volume)` — enrichment,均值差 +0.60,p 0.038
23. `day_wmean(Ret, Ret)` — enrichment,均值差 +0.59,p 0.000
24. `cs_normalize(day_std(High))` — enrichment,均值差 +0.58,p 0.020
25. `day_quantile_q75(Ret)` — enrichment,均值差 +0.57,p 0.096
26. `cs_stddev_full(day_durbin_watson(High))` — enrichment,均值差 +0.57,p 0.059
27. `cs_normalize(day_std(Volume))` — enrichment,均值差 +0.51,p 0.080
28. `day_durbin_watson(High)` — enrichment,均值差 +0.48,p 0.000
29. `day_std(High)` — enrichment,均值差 +0.36,p 0.080

## 本组之前各轮的任务

- `c05s807Br1a_Ea`:核心 `pow_2(day_wmean(Ret, Ret))`;评分 76,过线 13,入 heads 7;采样计数 {'c05_no_core': 2452, 'c05_skeleton': 3, 'c05_periphery_seen': 13}
  - score +1.78(train +2.45 valid +1.78):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)`
  - score +1.75(train +1.76 valid +1.75):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 60)`
  - score +1.64(train +1.64 valid +1.74):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 60)`
  - score +1.57(train +1.57 valid +2.53):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 20)`
  - score +1.21(train +1.21 valid +1.60):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)`
- `c05s807Br1b_Nb`:核心 `—`;评分 66,过线 1,入 heads 1;采样计数 {}
  - score +0.68(train +0.68 valid +1.62):`pow_2(pow_2(pow_2(day_topw_mean(Ret, Amt))))`
  - score +0.26(train +0.26 valid +0.36):`pow_2(pow_2(day_mean(Ret)))`
  - score +0.14(train +0.14 valid +0.86):`pow_2(pow_2(day_topw_mean(Ret, Amt)))`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(cross_quantile_q75(cs_rank(day_mean(Ret)), 241), 10)`
  - score -0.30(train -0.30 valid +0.57):`pow_2(day_topw_mean(Ret, Amt))`
- `c05s807Br2a_Ea`:核心 `day_durbin_watson(High)`;评分 97,过线 1,入 heads 1;采样计数 {'c05_no_core': 1331, 'c05_periphery_seen': 8}
  - score +0.63(train +0.63 valid +1.85):`cs_last_high40(cs_stddev_full(day_durbin_watson(High)), cross_corr(day_durbin_watson(High), day_quantile(Volume), 20))`
  - score +0.45(train +0.45 valid +3.26):`cs_last_high40(cs_stddev_full(day_durbin_watson(High)), day_quantile_q75(Ret))`
  - score +0.45(train +0.45 valid +1.14):`cs_last_high40(cs_stddev_full(day_durbin_watson(High)), cross_corr(day_durbin_watson(High), day_sum(Amt), 20))`
  - score +0.44(train +0.44 valid +1.68):`cs_last_high40(sub(day_durbin_watson(High), day_quantile_q75(Ret)), day_quantile_q75(Ret))`
  - score +0.43(train +0.43 valid +3.26):`cs_last_high40(cs_stddev_full(sub(sqrt(LogFloatCap), cross_regres(LogFloatCap, sub(day_durbin_watson(High), day_quantile_q75(Ret)), 60))), day_quantile_q75(Ret))`
- `c05s807Br2b_Nb`:核心 `—`;评分 75,过线 5,入 heads 2;采样计数 {}
  - score +1.00(train +1.00 valid +2.37):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_last(Open)))`
  - score +0.93(train +0.93 valid +2.30):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open)))`
  - score +0.90(train +0.90 valid +2.36):`cs_mask_top_replace_mean_neg(cs_demean(cs_mask_top_replace_mean_neg(day_quantile(Open))))`
  - score +0.70(train +1.01 valid +0.70):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open))))`
  - score +0.63(train +0.63 valid +1.97):`cs_mask_top_replace_mean_neg(cross_decay_linear(cs_mask_top_replace_mean_neg(day_quantile(Open)), 30))`

## 比原 head 好的拆解变体(R 候选)

(没有)
