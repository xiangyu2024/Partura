# 定位:种子 2026,P 组,第 3 轮(只含 train / valid)

快照:prods2026M1_I0_open_search, prods2026M2_I0_open_search, prods2026M3_I0_open_search, prods2026Pr1a_Ea, prods2026Pr1b_Nb, prods2026Pr2a_Ea, prods2026Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.83 | +0.83 | +1.00 | +1 | 0 | prods2026Pr2a_Ea | `cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), 241)` |
| -1.61 | -1.61 | -1.21 | +1 | 5 | prods2026M1_I0_open_search | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120))` |
| -1.70 | -1.70 | -1.65 | +1 | 20 | prods2026M1_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)` |
| -1.73 | -1.73 | -1.29 | +1 | 5 | prods2026M1_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 120)` |
| -2.79 | -2.79 | -2.31 | +1 | 20 | prods2026M3_I0_open_search | `ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 15)` |
| -2.86 | -2.86 | -2.37 | +1 | 20 | prods2026M3_I0_open_search | `ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15)` |
| -2.87 | -2.87 | -2.04 | +1 | 20 | prods2026M3_I0_open_search | `add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 15), ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15))` |
| -3.31 | -2.89 | -3.31 | +1 | 20 | prods2026M2_I0_open_search | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |
| -3.33 | -2.89 | -3.33 | +1 | 20 | prods2026M2_I0_open_search | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), ts_mean(day_durbin_watson(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| -3.38 | -3.31 | -3.38 | -1 | 20 | prods2026M2_I0_open_search | `ts_stddev(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |

## 共性:241 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.86 | 0.000 | 4 | +0.52 / -2.34 | `mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), day_sum(in_slice(Ret, 11, 230)))` |
| +2.86 | 0.000 | 4 | +0.52 / -2.34 | `mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), day_sum(in_slice(Ret, 11, 230))))` |
| +2.44 | 0.000 | 11 | +0.04 / -2.40 | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))))` |
| +2.18 | 0.000 | 19 | -0.29 / -2.46 | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))` |
| +1.72 | 0.000 | 32 | -0.80 / -2.52 | `day_sum(in_slice(Ret, 11, 230))` |
| +1.51 | 0.000 | 63 | -1.18 / -2.69 | `day_flat_run_max(in_slice(Ret, 11, 230))` |
| +1.46 | 0.002 | 6 | -0.87 / -2.33 | `cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)), day_flat_run_max(in_slice(Ret, 11, 230)), 120)` |
| +1.35 | 0.015 | 4 | -0.97 / -2.31 | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_flat_run_max(in_slice(Ret, 11, 230)))` |
| +1.02 | 0.051 | 4 | -1.29 / -2.31 | `cross_ema(cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares)), 40)` |
| +0.95 | 0.028 | 5 | -1.36 / -2.31 | `div(signedpower(day_flat_run_max(Low)), abs_(day_q_stat_std(Low)))` |
| +0.95 | 0.039 | 5 | -1.36 / -2.31 | `cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares))` |
| +0.89 | 0.000 | 20 | -1.48 / -2.37 | `cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` |
| +0.87 | 0.042 | 4 | -1.43 / -2.31 | `sub(day_flat_run_max(in_slice(Open, 11, 120)), day_flat_run_max(in_slice(Ret, 121, 230)))` |
| +0.85 | 0.027 | 7 | -1.47 / -2.32 | `sub(LogFloatCap, LogFloatShares)` |
| +0.83 | 0.006 | 10 | -1.50 / -2.33 | `abs_(LogTotalCap)` |
| +0.81 | 0.010 | 9 | -1.51 / -2.32 | `cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap))` |
| +0.81 | 0.010 | 9 | -1.51 / -2.32 | `ts_pearson(cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap)), 10)` |
| +0.77 | 0.037 | 6 | -1.54 / -2.31 | `cross_reg_fvalue(day_es_ratio_hi(High), day_quantile_q25(Low), 241)` |
| +0.77 | 0.014 | 9 | -1.55 / -2.32 | `day_hurst(High)` |
| +0.77 | 0.014 | 9 | -1.55 / -2.32 | `abs_(day_hurst(High))` |

## 拆解(24 次评估)

### head score +0.83:`cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))))` | -2.95 | -2.95 | -2.36 | — | (子树本身) |
| sufficiency | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))` | -3.14 | -3.14 | -2.50 | — | (子树本身) |
| sufficiency | `day_flat_run_max(in_slice(Ret, 11, 230))` | — | — | — | — | 门槛废品 |
| knockout | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))))` | -2.44 | -2.14 | -2.44 | +3.27 | `cross_mean(day_flat_run_max(in_slice(Ret, 11, 230)), 241)` |
| knockout | `mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))` | -0.81 | -0.81 | -0.13 | +1.65 | `cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_flat_run_max(in_slice(Ret, 11, 230))), 241)` |
| window | `cross_mean@241->120` | +0.48 | +0.48 | +0.55 | — | `cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), 120)` |
| window | `cross_mean@241->482` | +0.04 | +0.04 | +0.65 | — | `cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), 482)` |

### head score -2.79:`ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1)` | -3.82 | -3.82 | -3.01 | — | (子树本身) |
| swap | `Amt->Volume` | -2.86 | -2.86 | -2.37 | — | `ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15)` |
| window | `ts_stddev@15->7` | -3.30 | -3.30 | -2.99 | — | `ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 7)` |
| window | `ts_stddev@15->30` | -2.24 | -2.24 | -1.67 | — | `ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 30)` |

### head score -2.86:`ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1)` | -3.85 | -3.85 | -3.02 | — | (子树本身) |
| swap | `Volume->Amt` | -2.79 | -2.79 | -2.32 | — | `ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 15)` |
| window | `ts_stddev@15->7` | -3.39 | -3.39 | -2.95 | — | `ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 7)` |
| window | `ts_stddev@15->30` | -2.23 | -2.23 | -1.63 | — | `ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 30)` |

### head score -2.87:`add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 15), ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15)` | -2.86 | -2.86 | -2.37 | — | (子树本身) |
| sufficiency | `day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1)` | -3.85 | -3.85 | -3.02 | — | (子树本身) |
| sufficiency | `ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 15)` | -2.27 | -2.27 | -1.81 | — | (子树本身) |
| sufficiency | `day_autocorr(in_slice(Ret, 11, 230), 1)` | -3.84 | -3.48 | -3.84 | — | (子树本身) |
| knockout | `ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15)` | -3.74 | -3.74 | -3.14 | +0.87 | `add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 15), day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1))` |
| knockout | `ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 15)` | -4.12 | -3.66 | -4.12 | +1.25 | `add(day_autocorr(in_slice(Ret, 11, 230), 1), ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15))` |
| swap | `Volume->Amt` | -2.89 | -2.89 | -1.99 | — | `add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 15), ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 15))` |
| window | `ts_stddev@15->7` | -2.55 | -2.55 | -2.03 | — | `add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 7), ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15))` |
| window | `ts_stddev@15->30` | -2.89 | -2.89 | -2.18 | — | `add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 30), ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15))` |

## 机械核心卡(B0 按这个顺序取)

1. `mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), day_sum(in_slice(Ret, 11, 230)))` — enrichment,均值差 +2.86,p 0.000
2. `mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), day_sum(in_slice(Ret, 11, 230))))` — enrichment,均值差 +2.86,p 0.000
3. `mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))))` — enrichment,均值差 +2.44,p 0.000
4. `mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))` — enrichment,均值差 +2.18,p 0.000
5. `day_sum(in_slice(Ret, 11, 230))` — enrichment,均值差 +1.72,p 0.000
6. `day_flat_run_max(in_slice(Ret, 11, 230))` — enrichment,均值差 +1.51,p 0.000
7. `cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)), day_flat_run_max(in_slice(Ret, 11, 230)), 120)` — enrichment,均值差 +1.46,p 0.002
8. `mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_flat_run_max(in_slice(Ret, 11, 230)))` — enrichment,均值差 +1.35,p 0.015
9. `cross_ema(cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares)), 40)` — enrichment,均值差 +1.02,p 0.051
10. `div(signedpower(day_flat_run_max(Low)), abs_(day_q_stat_std(Low)))` — enrichment,均值差 +0.95,p 0.028
11. `cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +0.95,p 0.039
12. `cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` — enrichment,均值差 +0.89,p 0.000
13. `sub(day_flat_run_max(in_slice(Open, 11, 120)), day_flat_run_max(in_slice(Ret, 121, 230)))` — enrichment,均值差 +0.87,p 0.042
14. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.85,p 0.027
15. `abs_(LogTotalCap)` — enrichment,均值差 +0.83,p 0.006
16. `cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap))` — enrichment,均值差 +0.81,p 0.010
17. `ts_pearson(cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap)), 10)` — enrichment,均值差 +0.81,p 0.010
18. `cross_reg_fvalue(day_es_ratio_hi(High), day_quantile_q25(Low), 241)` — enrichment,均值差 +0.77,p 0.037
19. `day_hurst(High)` — enrichment,均值差 +0.77,p 0.014
20. `abs_(day_hurst(High))` — enrichment,均值差 +0.77,p 0.014
21. `sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120))` — enrichment,均值差 +0.74,p 0.013
22. `signedpower(day_flat_run_max(Low))` — enrichment,均值差 +0.73,p 0.038
23. `ts_delta(LogTotalCap, 1)` — enrichment,均值差 +0.73,p 0.015
24. `day_flat_run_max(Low)` — enrichment,均值差 +0.69,p 0.041
25. `day_flat_run_max(in_slice(Open, 11, 120))` — enrichment,均值差 +0.66,p 0.076
26. `day_quantile_q25(Low)` — enrichment,均值差 +0.47,p 0.060
27. `day_es_ratio_hi(High)` — enrichment,均值差 +0.42,p 0.067
28. `cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` — enrichment,均值差 +0.40,p 0.058

## 本组之前各轮的任务

- `prods2026Pr1a_Ea`:核心 `day_ar1_coefficient(in_slice(Ret, 11, 230))`;评分 98,过线 0,入 heads 0;采样计数 {'c05_skeleton': 670, 'c05_no_core': 1292}
  - score +0.19(train +0.36 valid +0.19):`mul(cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)), day_flat_run_max(in_slice(Ret, 11, 230)), 120), day_flat_run_max(in_slice(Ret, 11, 230)))`
  - score -0.33(train -0.31 valid -0.33):`mul(cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_ema(cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_ema(cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares)), 40)), day_flat_run_max(in_slice(Ret, 11, 230)), 120)), 40)), day_flat_run_max(in_slice(Ret, 11, 230)), 120), replace_small_with_nan(is_gt(ListAge, 130)))`
  - score -0.48(train -0.14 valid -0.48):`mul(cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)), day_flat_run_max(in_slice(Ret, 11, 230)), 120), replace_small_with_nan(is_gt(ListAge, 130)))`
  - score -0.55(train -0.08 valid -0.55):`mul(cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 5)), day_flat_run_max(in_slice(Ret, 11, 230)), 120), day_flat_run_max(in_slice(Ret, 11, 230)))`
  - score -0.56(train -0.56 valid -0.02):`mul(cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), is_gt(ListAge, 130)), day_flat_run_max(in_slice(Ret, 11, 230)), 120), replace_small_with_nan(is_gt(ListAge, 130)))`
- `prods2026Pr1b_Nb`:核心 `—`;评分 99,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score -0.51(train -0.24 valid -0.51):`cross_stddev(sub(day_corr(in_delay(in_topk_masked(in_slice(Volume, 11, 230), in_slice(Ret, 11, 230), 5), 1), in_slice(Ret, 11, 230)), day_corr(in_delay(in_slice(Ret, 11, 230), 1), in_slice(Ret, 11, 230))), 120)`
  - score -1.08(train -1.08 valid -0.86):`cross_mean(day_cov(Low, div(signedpower(sqrt(in_max(abs_(in_topk_masked_exact_k5(Ret, Vwap))))), div(abs_(day_hurst(High)), mul(0.5, day_corr(in_delay(in_slice(Low, 11, 230), 3), in_slice(Ret, 11, 230)))))), 241)`
  - score -1.11(train -1.11 valid -0.77):`cross_mean(day_cov(Low, div(signedpower(sqrt(in_max(abs_(in_topk_masked_exact_k5(Ret, Vwap))))), div(abs_(day_hurst(High)), mul(0.5, day_corr(in_delay(in_slice(Ret, 11, 230), 3), in_slice(Ret, 11, 230)))))), 241)`
  - score -1.12(train -1.12 valid -1.05):`cross_mean(sub(day_corr(in_delay(in_topk_masked(abs_(in_slice(Ret, 11, 230)), in_slice(Ret, 11, 230), 10), 3), in_slice(Low, 11, 230)), day_corr(in_delay(in_delay(in_slice(Ret, 11, 230), 1), 3), in_slice(Ret, 11, 230))), 241)`
  - score -1.13(train -0.75 valid -1.13):`cross_mean(sub(day_corr(in_delay(in_topk_masked(abs_(in_slice(Ret, 11, 230)), in_slice(Ret, 11, 230), 10), 3), in_slice(Low, 11, 230)), abs_(day_hurst(High))), 241)`
- `prods2026Pr2a_Ea`:核心 `day_flat_run_max(in_slice(Ret, 11, 230))`;评分 79,过线 3,入 heads 1;采样计数 {'c05_no_core': 1281, 'c05_skeleton': 653, 'c05_periphery_seen': 3}
  - score +0.83(train +0.83 valid +1.00):`cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), 241)`
  - score +0.78(train +0.78 valid +1.05):`cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), day_sum(in_slice(Ret, 11, 230))))), 241)`
  - score +0.62(train +0.62 valid +0.82):`cross_mean(mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))), mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))), day_sum(in_slice(Ret, 11, 230)))), 241)`
  - score +0.45(train +0.45 valid +0.79):`cross_mean(mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230))), 241)`
  - score +0.44(train +0.44 valid +0.49):`cross_mean(mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), mul(mul(day_flat_run_max(in_slice(Ret, 11, 230)), mul(day_flat_run_max(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)))), day_sum(in_slice(Ret, 11, 230)))), 60)`
- `prods2026Pr2b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.44(train -0.44 valid -0.24):`cross_ema(sub(div(signedpower(day_flat_run_max(Low)), abs_(day_autocorr_n1(Vwap))), day_flat_run_max(Low)), 60)`
  - score -0.84(train -0.84 valid +0.19):`cross_ema(sub(div(signedpower(day_flat_run_max(Low)), abs_(day_q_stat_std(Low))), day_flat_run_max(in_slice(Ret, 121, 230))), 60)`
  - score -0.86(train -0.86 valid +0.09):`cross_ema(sub(div(signedpower(day_flat_run_max(Low)), abs_(day_q_stat_std(Low))), day_flat_run_max(in_slice(High, 121, 230))), 60)`
  - score -1.12(train -0.99 valid -1.12):`cross_ema(sub(day_flat_run_max(in_slice(Open, 11, 120)), day_flat_run_max(in_slice(Ret, 121, 230))), 60)`
  - score -1.18(train -1.18 valid +0.40):`cross_ema(sub(div(signedpower(day_flat_run_max(Low)), abs_(day_q_stat_std(Low))), day_argmin(in_slice(Ret, 121, 230))), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.63(window ts_stddev@15->30):`ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 30)`
- 增益 +0.55(window ts_stddev@15->30):`ts_stddev(day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1), 30)`
- 增益 +0.32(window ts_stddev@15->7):`add(ts_stddev(day_autocorr(in_slice(Ret, 11, 230), 1), 7), ts_stddev(day_autocorr(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 1), 15))`
