# 定位:种子 807,C 组,第 3 轮(只含 train / valid)

快照:c05s807M1_I0_open_search, c05s807M2_I0_open_search, c05s807M3_I0_open_search, c06s807Cr1a_Ea, c06s807Cr1b_Nb, c06s807Cr2a_Na, c06s807Cr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(24 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.78 | +1.78 | +2.69 | -1 | 20 | c05s807M2_I0_open_search | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)` |
| +1.49 | +1.49 | +2.45 | -1 | 20 | c06s807Cr1a_Ea | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` |
| +1.27 | +1.27 | +2.25 | -1 | 0 | c05s807M2_I0_open_search | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` |
| +1.21 | +1.39 | +1.21 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)` |
| +1.20 | +2.03 | +1.20 | -1 | 5 | c05s807M3_I0_open_search | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| +1.18 | +1.18 | +1.35 | -1 | 20 | c05s807M1_I0_open_search | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +1.09 | +1.89 | +1.09 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 15)` |
| +1.02 | +1.16 | +1.02 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 5)))), 10)` |
| +0.93 | +0.93 | +2.30 | +1 | 5 | c06s807Cr2b_Nb | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open)))` |
| +0.83 | +0.83 | +1.35 | -1 | 5 | c06s807Cr1a_Ea | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` |
| +0.75 | +1.14 | +0.75 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_last(in_sum_rolling(Volume, 5))), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| +0.75 | +0.75 | +1.01 | -1 | 5 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| +0.74 | +1.05 | +0.74 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(in_sum_rolling(Volume, 5), 5)), inv(cs_demean(day_distinct_ratio(Volume))), 10)` |
| +0.71 | +0.71 | +2.10 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))), 15)` |
| +0.70 | +1.01 | +0.70 | +1 | 5 | c06s807Cr2b_Nb | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open))))` |
| +0.67 | +1.00 | +0.67 | -1 | 5 | c05s807M3_I0_open_search | `cross_regbeta(day_last(Volume), cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume)), 15)` |
| +0.66 | +0.86 | +0.66 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(Volume), inv(cs_demean(day_distinct_ratio(Volume))), 10)` |
| +0.63 | +0.63 | +0.73 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cross_regbeta(cs_normalize(day_std(High)), cs_demean(day_distinct_ratio(Volume)), 30), 10)` |
| +0.60 | +0.99 | +0.60 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cs_mask_top_replace_mean_neg(cs_robust_z(day_argmax(Volume))), 10)` |
| +0.59 | +0.59 | +1.83 | -1 | 20 | c06s807Cr1a_Ea | `cross_mean(cross_min(pow_2(pow_2(day_wmean(Ret, Ret))), 30), 5)` |
| +0.58 | +0.58 | +0.93 | -1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cross_regbeta(cs_normalize(day_std(High)), cs_sum(day_distinct_ratio(Volume)), 15), 10)` |
| +0.55 | +0.55 | +0.73 | -1 | 5 | c06s807Cr1a_Ea | `cross_mean(cs_winsor(pow_2(day_wmean(Ret, Ret))), 10)` |
| +0.54 | +1.61 | +0.54 | +1 | 20 | c05s807M3_I0_open_search | `cross_regbeta(day_last(in_sum_rolling(Volume, 3)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 3)))), 10)` |
| +0.52 | +0.52 | +0.84 | +1 | 0 | c05s807M2_I0_open_search | `ts_sum(LogFloatShares, 30)` |

## 共性:526 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.65 | 0.000 | 16 | +0.84 / -0.80 | `ts_sum(pow_3(day_durbin_watson(High)), 1)` |
| +1.64 | 0.000 | 7 | +0.86 / -0.78 | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` |
| +1.46 | 0.000 | 30 | +0.62 / -0.84 | `pow_3(day_durbin_watson(High))` |
| +1.44 | 0.005 | 4 | +0.67 / -0.77 | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +1.41 | 0.007 | 4 | +0.64 / -0.77 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +1.26 | 0.015 | 4 | +0.50 / -0.76 | `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` |
| +1.26 | 0.000 | 12 | +0.47 / -0.78 | `pow_2_5(LogFloatShares)` |
| +1.24 | 0.016 | 4 | +0.48 / -0.76 | `pow_3(pow_2_5(LogFloatShares))` |
| +1.24 | 0.005 | 6 | +0.47 / -0.77 | `cross_fangzheng(pow_2_5(LogFloatShares), 60)` |
| +1.17 | 0.000 | 57 | +0.29 / -0.88 | `day_durbin_watson(High)` |
| +1.14 | 0.000 | 12 | +0.36 / -0.78 | `cross_stddev(day_durbin_watson(High), 60)` |
| +1.05 | 0.038 | 4 | +0.29 / -0.76 | `cs_mask_top_replace_mean_neg(day_quantile(Open))` |
| +0.93 | 0.001 | 17 | +0.14 / -0.78 | `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` |
| +0.91 | 0.001 | 18 | +0.13 / -0.79 | `cs_robust_z(day_distinct_ratio(Volume))` |
| +0.85 | 0.000 | 69 | -0.02 / -0.87 | `day_wmean(Ret, Ret)` |
| +0.83 | 0.007 | 14 | +0.06 / -0.78 | `cs_normalize(pow_2(day_wmean(Ret, Ret)))` |
| +0.83 | 0.000 | 62 | -0.02 / -0.85 | `pow_2(day_wmean(Ret, Ret))` |
| +0.75 | 0.015 | 13 | -0.02 / -0.77 | `cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))` |
| +0.74 | 0.000 | 31 | -0.06 / -0.80 | `day_last(in_sum_rolling(Volume, 5))` |
| +0.73 | 0.127 | 4 | -0.03 / -0.76 | `cross_decay_linear(day_quantile(Open), 241)` |

## 拆解(32 次评估)

### head score +1.27:`ts_sum(cross_stddev(day_std(Ret), 60), 1)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_std(Ret), 60)` | +1.27 | +1.27 | +2.25 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -2.56 | -2.56 | -2.40 | — | (子树本身) |
| knockout | `cross_stddev(day_std(Ret), 60)` | -2.56 | -2.56 | -2.40 | +3.82 | `ts_sum(day_std(Ret), 1)` |
| window | `ts_sum@1->2` | +0.97 | +0.97 | +2.24 | — | `ts_sum(cross_stddev(day_std(Ret), 60), 2)` |

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

### head score +1.09:`cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_normalize(day_std(Volume))` | -1.58 | +0.15 | -1.58 | — | (子树本身) |
| sufficiency | `cs_robust_z(day_distinct_ratio(Volume))` | — | — | — | — | 门槛废品 |
| knockout | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))))` | +1.05 | +1.41 | +1.05 | +0.05 | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` |
| knockout | `cs_normalize(day_std(Volume))` | +0.77 | +1.94 | +0.77 | +0.33 | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 15)` |
| knockout | `cs_robust_z(day_distinct_ratio(Volume))` | +0.31 | +1.91 | +0.31 | +0.78 | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))), 15)` |
| swap | `Volume->Amt` | +1.37 | +1.47 | +1.37 | — | `cross_regbeta(cs_normalize(day_std(Amt)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Amt)))), 15)` |
| window | `cross_regbeta@15->7` | +0.73 | +1.87 | +0.73 | — | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 7)` |
| window | `cross_regbeta@15->30` | +1.28 | +2.18 | +1.28 | — | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_stddev(day_std(Ret), 60)` — ablation,自身 score +1.27(所在 head +1.27)
2. `ts_sum(pow_3(day_durbin_watson(High)), 1)` — enrichment,均值差 +1.65,p 0.000
3. `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` — enrichment,均值差 +1.64,p 0.000
4. `pow_3(day_durbin_watson(High))` — enrichment,均值差 +1.46,p 0.000
5. `pow_2(pow_2(day_wmean(Ret, Ret)))` — enrichment,均值差 +1.44,p 0.005
6. `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` — enrichment,均值差 +1.41,p 0.007
7. `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` — enrichment,均值差 +1.26,p 0.015
8. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.26,p 0.000
9. `pow_3(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.24,p 0.016
10. `cross_fangzheng(pow_2_5(LogFloatShares), 60)` — enrichment,均值差 +1.24,p 0.005
11. `day_durbin_watson(High)` — enrichment,均值差 +1.17,p 0.000
12. `cross_stddev(day_durbin_watson(High), 60)` — enrichment,均值差 +1.14,p 0.000
13. `cs_mask_top_replace_mean_neg(day_quantile(Open))` — enrichment,均值差 +1.05,p 0.038
14. `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` — enrichment,均值差 +0.93,p 0.001
15. `cs_robust_z(day_distinct_ratio(Volume))` — enrichment,均值差 +0.91,p 0.001
16. `day_wmean(Ret, Ret)` — enrichment,均值差 +0.85,p 0.000
17. `cs_normalize(pow_2(day_wmean(Ret, Ret)))` — enrichment,均值差 +0.83,p 0.007
18. `pow_2(day_wmean(Ret, Ret))` — enrichment,均值差 +0.83,p 0.000
19. `cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))` — enrichment,均值差 +0.75,p 0.015
20. `day_last(in_sum_rolling(Volume, 5))` — enrichment,均值差 +0.74,p 0.000
21. `day_quantile(Open)` — enrichment,均值差 +0.70,p 0.024
22. `day_distinct_ratio(Volume)` — enrichment,均值差 +0.66,p 0.000
23. `day_std(Volume)` — enrichment,均值差 +0.61,p 0.024
24. `cs_normalize(day_std(High))` — enrichment,均值差 +0.59,p 0.009
25. `cs_normalize(day_std(Volume))` — enrichment,均值差 +0.52,p 0.053
26. `day_var(Ret)` — enrichment,均值差 +0.50,p 0.064
27. `day_std(High)` — enrichment,均值差 +0.37,p 0.042
28. `cs_demean(day_distinct_ratio(Volume))` — enrichment,均值差 +0.33,p 0.070

## 本组之前各轮的任务

- `c06s807Cr1a_Ea`:核心 `pow_2(day_wmean(Ret, Ret))`;评分 84,过线 20,入 heads 4;采样计数 {'c05_no_core': 1519, 'c05_periphery_seen': 6}
  - score +1.49(train +1.49 valid +2.45):`ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)`
  - score +1.12(train +1.12 valid +1.64):`cross_decay_linear(cs_normalize(pow_2(day_wmean(Ret, Ret))), 5)`
  - score +1.08(train +1.08 valid +1.81):`cross_mean(cross_mean(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)), 241), 5)`
  - score +1.06(train +1.06 valid +1.06):`ts_var(ts_var(pow_2(day_wmean(Ret, Ret)), 30), 30)`
  - score +1.03(train +1.03 valid +1.39):`ts_var(pow_2(day_wmean(Ret, Ret)), 50)`
- `c06s807Cr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {}
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(pow_2(cross_quantile_q75(cs_rank(day_mean(Ret)), 241)), 10)`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(pow_2(cross_quantile_q75(cs_rank(cs_rank(day_mean(Ret))), 241)), 10)`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(cross_quantile_q75(cs_rank(day_mean(Ret)), 241), 10)`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(cross_quantile_q75(cs_rank(cs_rank(day_mean(Ret))), 241), 10)`
  - score -0.41(train -0.41 valid +1.08):`cross_semistd_pos(pow_2(cross_quantile_q75(day_mean(Ret), 241)), 10)`
- `c06s807Cr2a_Na`:核心 `—`;评分 100,过线 0,入 heads 0;采样计数 {}
  - score -0.02(train -0.02 valid +0.02):`sub(cross_mean(log(div(day_first(Open), ts_delay(ts_delay(day_last(Close), 1), 1))), 120), cross_mean(cs_robust_z(cs_flip_by_state(LogFloatShares, day_wstd(Vwap, Vwap))), 120))`
  - score -0.04(train -0.01 valid -0.04):`sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 120), cross_mean(div(day_last(Close), day_first(Open)), 120))`
  - score -0.24(train -0.17 valid -0.24):`sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 120), cross_mean(log(div(day_last(Close), day_first(Vwap))), 120))`
  - score -0.28(train -0.15 valid -0.28):`sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 120), cross_mean(log(div(day_last(Close), day_first(Open))), 120))`
  - score -0.28(train -0.15 valid -0.28):`sub(sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 120), cross_mean(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 120)), cross_mean(log(div(day_last(Close), day_first(Open))), 120))`
- `c06s807Cr2b_Nb`:核心 `—`;评分 53,过线 3,入 heads 2;采样计数 {}
  - score +0.93(train +0.93 valid +2.30):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open)))`
  - score +0.80(train +0.80 valid +2.19):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_min(Open)))`
  - score +0.70(train +1.01 valid +0.70):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open))))`
  - score +0.44(train +0.44 valid +1.08):`cs_mask_top_replace_mean_neg(day_quantile(Open))`
  - score +0.43(train +0.43 valid +1.02):`cs_mask_top_replace_mean_neg(cs_scale(day_quantile(Open)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window cross_regbeta@15->30):`cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 30)`
