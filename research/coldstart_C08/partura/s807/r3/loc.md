# 定位:种子 807,P 组,第 3 轮(只含 train / valid)

快照:c07s807M1_I0_open_search, c07s807M2_I0_open_search, c07s807M3_I0_open_search, c08s807Pr1a_Ea, c08s807Pr1b_Nb, c08s807Pr2a_Ea, c08s807Pr2b_Nb;已生效的 R 替换 5 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(8 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.83 | +1.83 | +3.06 | +1 | 0 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 120)` |
| +1.79 | +1.79 | +3.02 | +1 | 0 | c07s807M1_I0_open_search | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)` |
| +1.13 | +1.13 | +1.20 | +1 | 5 | c08s807Pr1a_Ea | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` |
| +0.91 | +1.11 | +0.91 | -1 | 20 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)` |
| +0.88 | +0.88 | +1.83 | -1 | 5 | c08s807Pr2a_Ea | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241), day_std(Ret))` |
| +0.84 | +0.84 | +1.63 | -1 | 0 | c08s807Pr1b_Nb | `cross_stddev(log(log(log(day_std(Ret)))), 120)` |
| +0.69 | +1.18 | +0.69 | +1 | 5 | c08s807Pr1a_Ea | `cross_corr(ts_var(ts_var(LogFloatCap, 20), 20), log(day_sum(Amt)), 60)` |
| +0.62 | +0.62 | +0.83 | -1 | 5 | c08s807Pr2a_Ea | `cs_last_high05(cross_zscore(cross_zscore(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241), 241), 241), day_std(Ret))` |

## 共性:546 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.95 | 0.000 | 6 | +0.62 / -1.33 | `log(log(log(day_std(Ret))))` |
| +1.63 | 0.001 | 5 | +0.30 / -1.32 | `cs_mean(day_median(Close))` |
| +1.36 | 0.001 | 6 | +0.04 / -1.32 | `ts_var(LogFloatCap, 40)` |
| +1.22 | 0.000 | 17 | -0.13 / -1.35 | `log(log(day_std(Ret)))` |
| +1.20 | 0.024 | 4 | -0.12 / -1.32 | `day_mean(Amt)` |
| +1.16 | 0.002 | 9 | -0.17 / -1.33 | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)` |
| +1.03 | 0.000 | 23 | -0.32 / -1.35 | `log(day_std(Ret))` |
| +1.01 | 0.032 | 6 | -0.31 / -1.32 | `cross_stddev(log(log(day_std(Ret))), 120)` |
| +0.96 | 0.000 | 28 | -0.40 / -1.36 | `pow_2_5(LogFloatShares)` |
| +0.92 | 0.051 | 6 | -0.40 / -1.32 | `cross_zscore(cross_zscore(pow_2_5(LogFloatShares), 241), 241)` |
| +0.91 | 0.000 | 66 | -0.51 / -1.42 | `day_quantile_q75(Volume)` |
| +0.90 | 0.007 | 13 | -0.43 / -1.33 | `cross_zscore(pow_2_5(LogFloatShares), 241)` |
| +0.83 | 0.000 | 60 | -0.57 / -1.40 | `day_pos_ratio(Open)` |
| +0.83 | 0.000 | 60 | -0.57 / -1.40 | `cs_median(day_pos_ratio(Open))` |
| +0.79 | 0.038 | 9 | -0.53 / -1.32 | `day_quantile(Open)` |
| +0.78 | 0.051 | 10 | -0.54 / -1.32 | `pow_2_5(pow_2_5(LogFloatShares))` |
| +0.78 | 0.076 | 5 | -0.54 / -1.31 | `ts_regalpha(day_mean(Ret), day_pos_ratio(Amt), 20)` |
| +0.77 | 0.006 | 16 | -0.56 / -1.33 | `ts_var(LogFloatCap, 50)` |
| +0.77 | 0.067 | 9 | -0.55 / -1.32 | `cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241)` |
| +0.72 | 0.017 | 13 | -0.60 / -1.32 | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 50))` |

## 拆解(30 次评估)

### head score +1.83:`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth)` | -1.46 | -1.46 | +0.33 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -3.22 | -3.22 | -2.02 | — | (子树本身) |
| sufficiency | `ts_var(LogTotalCap, 30)` | -2.54 | -2.54 | -0.69 | — | (子树本身) |
| knockout | `cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth)` | +1.67 | +1.67 | +2.46 | +0.16 | `cross_regbeta(day_quantile_q75(Amt), ts_var(LogTotalCap, 30), 120)` |
| knockout | `ts_var(LogTotalCap, 30)` | +0.28 | +0.28 | +0.36 | +1.55 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(LogTotalCap, LimitWidth), 120)` |
| swap | `Amt->Volume` | +0.79 | +1.41 | +0.79 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 120)` |
| window | `cross_regbeta@120->60` | +1.63 | +1.63 | +2.16 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)` |
| window | `cross_regbeta@120->240` | +1.05 | +1.05 | +2.16 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 240)` |

### head score +1.79:`cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth)` | -0.86 | -0.86 | +0.45 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -3.22 | -3.22 | -2.02 | — | (子树本身) |
| sufficiency | `ts_var(LogFloatCap, 20)` | -2.71 | -2.71 | -1.62 | — | (子树本身) |
| knockout | `cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth)` | +1.65 | +1.65 | +2.71 | +0.14 | `cross_reg_tvalue(day_quantile_q75(Amt), ts_var(LogFloatCap, 20), 120)` |
| knockout | `ts_var(LogFloatCap, 20)` | -0.00 | -0.00 | +1.42 | +1.79 | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(LogFloatCap, LimitWidth), 120)` |
| swap | `Amt->Volume` | +1.27 | +1.27 | +2.04 | — | `cross_reg_tvalue(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)` |
| window | `cross_reg_tvalue@120->60` | +1.26 | +1.26 | +3.31 | — | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)` |
| window | `cross_reg_tvalue@120->240` | +1.38 | +1.38 | +2.74 | — | `cross_reg_tvalue(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 240)` |

### head score +1.13:`cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(LogFloatCap, 20)` | -2.71 | -2.71 | -1.62 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -0.22 | -0.22 | +0.08 | — | (子树本身) |
| knockout | `ts_var(LogFloatCap, 20)` | -1.02 | -1.02 | -0.34 | +2.15 | `cross_corr(LogFloatCap, day_sum(Volume), 60)` |
| swap | `Volume->Amt` | +0.79 | +0.89 | +0.79 | — | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` |
| window | `cross_corr@60->30` | +0.94 | +0.94 | +1.00 | — | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 30)` |
| window | `cross_corr@60->120` | +0.58 | +0.58 | +1.13 | — | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 120)` |

### head score +0.88:`cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241), day_std(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241)` | -0.95 | -0.80 | -0.95 | — | (子树本身) |
| sufficiency | `pow_2_5(pow_2_5(LogFloatShares))` | -0.54 | -0.54 | -0.41 | — | (子树本身) |
| sufficiency | `pow_2_5(LogFloatShares)` | -0.54 | -0.54 | -0.41 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.94 | -3.59 | -3.94 | — | (子树本身) |
| knockout | `cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241)` | -0.41 | -0.41 | +0.06 | +1.29 | `cs_last_high05(pow_2_5(pow_2_5(LogFloatShares)), day_std(Ret))` |
| knockout | `pow_2_5(pow_2_5(LogFloatShares))` | +0.83 | +0.83 | +1.70 | +0.05 | `cs_last_high05(cross_zscore(pow_2_5(LogFloatShares), 241), day_std(Ret))` |
| window | `cross_zscore@241->120` | +1.47 | +1.47 | +1.55 | — | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 120), day_std(Ret))` |
| window | `cross_zscore@241->482` | +0.50 | +0.50 | +1.61 | — | `cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 482), day_std(Ret))` |

## 机械核心卡(B0 按这个顺序取)

1. `log(log(log(day_std(Ret))))` — enrichment,均值差 +1.95,p 0.000
2. `cs_mean(day_median(Close))` — enrichment,均值差 +1.63,p 0.001
3. `ts_var(LogFloatCap, 40)` — enrichment,均值差 +1.36,p 0.001
4. `log(log(day_std(Ret)))` — enrichment,均值差 +1.22,p 0.000
5. `day_mean(Amt)` — enrichment,均值差 +1.20,p 0.024
6. `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)` — enrichment,均值差 +1.16,p 0.002
7. `log(day_std(Ret))` — enrichment,均值差 +1.03,p 0.000
8. `cross_stddev(log(log(day_std(Ret))), 120)` — enrichment,均值差 +1.01,p 0.032
9. `pow_2_5(LogFloatShares)` — enrichment,均值差 +0.96,p 0.000
10. `cross_zscore(cross_zscore(pow_2_5(LogFloatShares), 241), 241)` — enrichment,均值差 +0.92,p 0.051
11. `day_quantile_q75(Volume)` — enrichment,均值差 +0.91,p 0.000
12. `cross_zscore(pow_2_5(LogFloatShares), 241)` — enrichment,均值差 +0.90,p 0.007
13. `day_pos_ratio(Open)` — enrichment,均值差 +0.83,p 0.000
14. `cs_median(day_pos_ratio(Open))` — enrichment,均值差 +0.83,p 0.000
15. `day_quantile(Open)` — enrichment,均值差 +0.79,p 0.038
16. `pow_2_5(pow_2_5(LogFloatShares))` — enrichment,均值差 +0.78,p 0.051
17. `ts_regalpha(day_mean(Ret), day_pos_ratio(Amt), 20)` — enrichment,均值差 +0.78,p 0.076
18. `ts_var(LogFloatCap, 50)` — enrichment,均值差 +0.77,p 0.006
19. `cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241)` — enrichment,均值差 +0.77,p 0.067
20. `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 50))` — enrichment,均值差 +0.72,p 0.017
21. `day_median(Close)` — enrichment,均值差 +0.70,p 0.028
22. `cs_median(LimitWidth)` — enrichment,均值差 +0.68,p 0.001
23. `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` — enrichment,均值差 +0.64,p 0.005
24. `log(LogFloatShares)` — enrichment,均值差 +0.56,p 0.001
25. `signedpower(cs_median(LimitWidth))` — enrichment,均值差 +0.51,p 0.028
26. `day_sum(Amt)` — enrichment,均值差 +0.44,p 0.037
27. `log(log(LogFloatShares))` — enrichment,均值差 +0.43,p 0.079
28. `ts_var(LogFloatCap, 20)` — enrichment,均值差 +0.42,p 0.003
29. `day_std(Ret)` — enrichment,均值差 +0.39,p 0.000

## 本组之前各轮的任务

- `c08s807Pr1a_Ea`:核心 `ts_var(LogFloatCap, 20)`;评分 82,过线 5,入 heads 2;采样计数 {'c05_no_core': 966, 'mutation_refused': 4, 'c05_periphery_seen': 7}
  - score +0.79(train +0.89 valid +0.79):`cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)`
  - score +0.77(train +0.80 valid +0.77):`cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 30)`
  - score +0.71(train +0.72 valid +0.71):`cross_corr(ts_var(LogFloatCap, 20), log(log(day_sum(Amt))), 60)`
  - score +0.69(train +1.18 valid +0.69):`cross_corr(ts_var(ts_var(LogFloatCap, 20), 20), log(day_sum(Amt)), 60)`
  - score +0.60(train +0.71 valid +0.60):`cross_corr(ts_var(LogFloatCap, 20), log(day_sum(Amt)), 60)`
- `c08s807Pr1b_Nb`:核心 `—`;评分 80,过线 10,入 heads 1;采样计数 {}
  - score +0.84(train +0.84 valid +1.63):`cross_stddev(log(log(log(day_std(Ret)))), 120)`
  - score +0.80(train +0.80 valid +1.67):`cross_tail_mean_q75(cross_stddev(log(log(log(day_std(Ret)))), 120), 3)`
  - score +0.80(train +0.80 valid +1.95):`cross_tail_mean_q75(cross_stddev(log(log(log(log(day_std(Ret))))), 120), 3)`
  - score +0.76(train +0.76 valid +1.96):`cross_stddev(log(log(log(log(day_std(Ret))))), 120)`
  - score +0.59(train +0.59 valid +0.91):`log(cross_stddev(log(log(day_std(Ret))), 120))`
- `c08s807Pr2a_Ea`:核心 `day_std(Ret)`;评分 83,过线 10,入 heads 2;采样计数 {'c05_no_core': 1198, 'c05_periphery_seen': 9}
  - score +0.88(train +0.88 valid +1.83):`cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 241), day_std(Ret))`
  - score +0.84(train +0.84 valid +1.80):`cs_last_high05(cross_zscore(signedpower(pow_2_5(LogFloatShares)), 241), day_std(Ret))`
  - score +0.80(train +0.80 valid +1.70):`cs_last_high05(cross_zscore(pow_2_5(LogFloatShares), 241), day_std(Ret))`
  - score +0.80(train +0.80 valid +1.70):`cs_last_high05(cs_last_high05(cross_zscore(pow_2_5(LogFloatShares), 241), day_std(Ret)), day_std(Ret))`
  - score +0.78(train +0.78 valid +1.69):`cs_last_high05(cross_zscore(pow_1_5(LogFloatShares), 241), day_std(Ret))`
- `c08s807Pr2b_Nb`:核心 `—`;评分 52,过线 0,入 heads 0;采样计数 {}
  - score +0.36(train +0.36 valid +0.95):`cs_mask_top_replace_mean_neg(day_quantile(High))`
  - score +0.34(train +0.34 valid +0.93):`cs_mask_top_replace_mean_neg(day_quantile(Open))`
  - score +0.34(train +0.34 valid +0.94):`cs_mask_top_replace_mean_neg(day_quantile_q25(Open))`
  - score +0.33(train +0.33 valid +0.94):`cs_mask_top_replace_mean_neg(day_quantile(Close))`
  - score +0.08(train +0.08 valid +0.70):`cs_mask_top_replace_mean_neg(cross_decay_linear(day_quantile(Open), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.60(window cross_zscore@241->120):`cs_last_high05(cross_zscore(pow_2_5(pow_2_5(LogFloatShares)), 120), day_std(Ret))`
