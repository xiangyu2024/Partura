# 定位:种子 2008,P 组,第 3 轮(只含 train / valid)

快照:prods2008M1_I0_open_search, prods2008M2_I0_open_search, prods2008M3_I0_open_search, prods2008Pr1a_Ea, prods2008Pr1b_Nb, prods2008Pr2a_Ea, prods2008Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.09 | -0.07 | -0.09 | +1 | 0 | prods2008M1_I0_open_search | `cross_stddev(ts_sum(log(day_durbin_watson(Vwap)), 10), 241)` |
| -1.10 | -1.10 | -0.69 | +1 | 0 | prods2008M2_I0_open_search | `cross_fangzheng(day_durbin_watson(Vwap), 241)` |
| -1.51 | -1.51 | -0.78 | +1 | 0 | prods2008M2_I0_open_search | `cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10), 10)` |
| -1.69 | -1.69 | -0.21 | +1 | 5 | prods2008M1_I0_open_search | `ts_std(log(day_durbin_watson(Vwap)), 40)` |
| -1.79 | -1.79 | -1.78 | -1 | 0 | prods2008M2_I0_open_search | `ts_sum(log(log(cross_fangzheng(day_durbin_watson(Vwap), 60))), 10)` |
| -2.50 | -1.07 | -2.50 | +1 | 20 | prods2008M1_I0_open_search | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| -2.84 | -2.11 | -2.84 | -1 | 20 | prods2008M3_I0_open_search | `div(ts_min(day_median(Amt), 30), ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3), 20))` |
| -3.21 | -2.96 | -3.21 | -1 | 20 | prods2008M3_I0_open_search | `ts_quantile_q75(cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3), 30)` |
| -3.28 | -3.07 | -3.28 | +1 | 20 | prods2008M3_I0_open_search | `ts_quantile_q75(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 30)` |

## 共性:196 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.12 | 0.013 | 4 | -0.95 / -2.06 | `mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120))), LogFloatCap))` |
| +1.01 | 0.003 | 7 | -1.07 / -2.08 | `cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(LogFloatCap)), LogFloatCap)` |
| +0.96 | 0.000 | 131 | -1.72 / -2.68 | `log(day_durbin_watson(Vwap))` |
| +0.94 | 0.000 | 13 | -1.16 / -2.10 | `mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(LogFloatCap))` |
| +0.88 | 0.000 | 71 | -1.48 / -2.36 | `cross_stddev(log(day_durbin_watson(Vwap)), 120)` |
| +0.80 | 0.054 | 4 | -1.26 / -2.06 | `sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)))` |
| +0.78 | 0.000 | 29 | -1.37 / -2.16 | `sub(LogFloatCap, LogFloatShares)` |
| +0.75 | 0.001 | 16 | -1.35 / -2.10 | `replace_small_with_nan(LogFloatCap)` |
| +0.72 | 0.000 | 31 | -1.44 / -2.16 | `mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120)))` |
| +0.68 | 0.000 | 36 | -1.48 / -2.17 | `is_gt(ListAge, 120)` |
| +0.68 | 0.000 | 36 | -1.48 / -2.17 | `replace_small_with_nan(is_gt(ListAge, 120))` |
| +0.63 | 0.023 | 10 | -1.45 / -2.07 | `cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120))), LogFloatCap)` |
| +0.53 | 0.113 | 6 | -1.53 / -2.06 | `log(log(day_durbin_watson(Vwap)))` |
| +0.17 | 0.570 | 5 | -1.88 / -2.05 | `log(day_sum(Amt))` |
| +0.17 | 0.570 | 5 | -1.88 / -2.05 | `day_sum(Amt)` |
| +0.12 | 0.687 | 9 | -1.92 / -2.05 | `day_durbin_watson(Close)` |
| +0.03 | 0.780 | 7 | -2.02 / -2.04 | `log(day_durbin_watson(Close))` |
| +0.02 | 0.766 | 6 | -2.02 / -2.04 | `sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap)))` |
| -1.00 | 0.947 | 4 | -3.02 / -2.02 | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10)` |
| -1.14 | 0.995 | 7 | -3.14 / -2.00 | `ts_sum(log(day_durbin_watson(Vwap)), 10)` |

## 拆解(38 次评估)

### head score -1.79:`ts_sum(log(log(cross_fangzheng(day_durbin_watson(Vwap), 60))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(log(cross_fangzheng(day_durbin_watson(Vwap), 60)))` | -1.99 | -1.64 | -1.99 | — | (子树本身) |
| sufficiency | `log(cross_fangzheng(day_durbin_watson(Vwap), 60))` | -1.99 | -1.63 | -1.99 | — | (子树本身) |
| sufficiency | `cross_fangzheng(day_durbin_watson(Vwap), 60)` | -1.99 | -1.63 | -1.99 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `log(log(cross_fangzheng(day_durbin_watson(Vwap), 60)))` | -1.79 | -1.79 | -1.78 | -0.00 | `ts_sum(log(cross_fangzheng(day_durbin_watson(Vwap), 60)), 10)` |
| knockout | `cross_fangzheng(day_durbin_watson(Vwap), 60)` | -3.64 | -3.64 | -2.20 | +1.85 | `ts_sum(log(log(day_durbin_watson(Vwap))), 10)` |
| swap | `Vwap->Close` | -1.90 | -1.90 | -1.58 | — | `ts_sum(log(log(cross_fangzheng(day_durbin_watson(Close), 60))), 10)` |
| window | `ts_sum@10->5` | -1.77 | -1.77 | -1.63 | — | `ts_sum(log(log(cross_fangzheng(day_durbin_watson(Vwap), 60))), 5)` |
| window | `ts_sum@10->20` | -2.24 | -2.22 | -2.24 | — | `ts_sum(log(log(cross_fangzheng(day_durbin_watson(Vwap), 60))), 20)` |

### head score -2.84:`div(ts_min(day_median(Amt), 30), ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3), 20)` | -2.63 | -2.63 | -2.10 | — | (子树本身) |
| sufficiency | `cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3)` | -3.68 | -3.68 | -2.89 | — | (子树本身) |
| sufficiency | `sigmoid(sigmoid(pow_2(day_durbin_watson(Amt))))` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| sufficiency | `sigmoid(pow_2(day_durbin_watson(Amt)))` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| knockout | `ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3), 20)` | -2.82 | -2.21 | -2.82 | -0.02 | `div(ts_min(day_median(Amt), 30), cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3))` |
| knockout | `cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3)` | -2.91 | -2.12 | -2.91 | +0.07 | `div(ts_min(day_median(Amt), 30), ts_hurst(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 20))` |
| knockout | `sigmoid(sigmoid(pow_2(day_durbin_watson(Amt))))` | -2.80 | -2.11 | -2.80 | -0.03 | `div(ts_min(day_median(Amt), 30), ts_hurst(cross_mean(sigmoid(pow_2(day_durbin_watson(Amt))), 3), 20))` |
| swap | `Amt->Volume` | -1.98 | -1.75 | -1.98 | — | `div(ts_min(day_median(Volume), 30), ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Volume)))), 3), 20))` |
| window | `ts_min@30->15` | -3.24 | -2.85 | -3.24 | — | `div(ts_min(day_median(Amt), 15), ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3), 20))` |
| window | `ts_min@30->60` | -2.66 | -1.85 | -2.66 | — | `div(ts_min(day_median(Amt), 60), ts_hurst(cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 3), 20))` |

### head score -3.21:`ts_quantile_q75(cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3)` | -3.70 | -3.51 | -3.70 | — | (子树本身) |
| sufficiency | `pow_3(sigmoid(pow_2(day_durbin_watson(Ret))))` | -3.53 | -3.53 | -3.41 | — | (子树本身) |
| sufficiency | `sigmoid(pow_2(day_durbin_watson(Ret)))` | -3.53 | -3.53 | -3.41 | — | (子树本身) |
| sufficiency | `pow_2(day_durbin_watson(Ret))` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| knockout | `cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3)` | -2.94 | -2.81 | -2.94 | -0.27 | `ts_quantile_q75(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 30)` |
| knockout | `pow_3(sigmoid(pow_2(day_durbin_watson(Ret))))` | -3.28 | -2.97 | -3.28 | +0.07 | `ts_quantile_q75(cross_mean(sigmoid(pow_2(day_durbin_watson(Ret))), 3), 30)` |
| knockout | `sigmoid(pow_2(day_durbin_watson(Ret)))` | -3.04 | -2.93 | -3.04 | -0.17 | `ts_quantile_q75(cross_mean(pow_3(pow_2(day_durbin_watson(Ret))), 3), 30)` |
| knockout | `pow_2(day_durbin_watson(Ret))` | -3.19 | -2.90 | -3.19 | -0.02 | `ts_quantile_q75(cross_mean(pow_3(sigmoid(day_durbin_watson(Ret))), 3), 30)` |
| window | `ts_quantile_q75@30->15` | -3.29 | -3.24 | -3.29 | — | `ts_quantile_q75(cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3), 15)` |
| window | `ts_quantile_q75@30->60` | -3.28 | -2.82 | -3.28 | — | `ts_quantile_q75(cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3), 60)` |

### head score -3.28:`ts_quantile_q75(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(sigmoid(pow_2(day_durbin_watson(Amt))))` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| sufficiency | `sigmoid(pow_2(day_durbin_watson(Amt)))` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| sufficiency | `pow_2(day_durbin_watson(Amt))` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Amt)` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| knockout | `sigmoid(sigmoid(pow_2(day_durbin_watson(Amt))))` | -3.22 | -3.07 | -3.22 | -0.06 | `ts_quantile_q75(sigmoid(pow_2(day_durbin_watson(Amt))), 30)` |
| knockout | `pow_2(day_durbin_watson(Amt))` | -3.22 | -3.08 | -3.22 | -0.06 | `ts_quantile_q75(sigmoid(sigmoid(day_durbin_watson(Amt))), 30)` |
| swap | `Amt->Volume` | -3.18 | -3.09 | -3.18 | — | `ts_quantile_q75(sigmoid(sigmoid(pow_2(day_durbin_watson(Volume)))), 30)` |
| window | `ts_quantile_q75@30->15` | -3.47 | -3.47 | -3.22 | — | `ts_quantile_q75(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 15)` |
| window | `ts_quantile_q75@30->60` | -3.41 | -2.56 | -3.41 | — | `ts_quantile_q75(sigmoid(sigmoid(pow_2(day_durbin_watson(Amt)))), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120))), LogFloatCap))` — enrichment,均值差 +1.12,p 0.013
2. `cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(LogFloatCap)), LogFloatCap)` — enrichment,均值差 +1.01,p 0.003
3. `log(day_durbin_watson(Vwap))` — enrichment,均值差 +0.96,p 0.000
4. `mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(LogFloatCap))` — enrichment,均值差 +0.94,p 0.000
5. `cross_stddev(log(day_durbin_watson(Vwap)), 120)` — enrichment,均值差 +0.88,p 0.000
6. `sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)))` — enrichment,均值差 +0.80,p 0.054
7. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.78,p 0.000
8. `replace_small_with_nan(LogFloatCap)` — enrichment,均值差 +0.75,p 0.001
9. `mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120)))` — enrichment,均值差 +0.72,p 0.000
10. `is_gt(ListAge, 120)` — enrichment,均值差 +0.68,p 0.000
11. `replace_small_with_nan(is_gt(ListAge, 120))` — enrichment,均值差 +0.68,p 0.000
12. `cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120))), LogFloatCap)` — enrichment,均值差 +0.63,p 0.023

## 本组之前各轮的任务

- `prods2008Pr1a_Ea`:核心 `day_durbin_watson(Vwap)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 685, 'c05_no_core': 1379}
  - score -0.06(train -0.06 valid +0.04):`cs_bucket_zscore(cross_stddev(cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 120), LogFloatCap), 120), LogFloatCap)`
  - score -0.67(train -0.22 valid -0.67):`cross_corr(day_durbin_watson(Vwap), log(day_durbin_watson(Vwap)), 120)`
  - score -0.73(train -0.73 valid -0.02):`cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 120), LogFloatCap)`
  - score -0.82(train -0.82 valid +0.09):`cs_bucket_zscore(cross_stddev(cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 3), LogFloatCap), 120), LogFloatCap)`
  - score -1.14(train -0.52 valid -1.14):`cross_corr(day_durbin_watson(Vwap), log(LogFloatCap), 120)`
- `prods2008Pr1b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.67(train -0.06 valid -0.67):`cross_regbeta(log(day_durbin_watson(Vwap)), sub(sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap))), cross_regbeta(log(day_durbin_watson(Vwap)), sub(sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap))), LogFloatShares), 241)), 241)`
  - score -0.78(train -0.78 valid -0.68):`sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)))`
  - score -1.02(train -0.32 valid -1.02):`cross_regbeta(log(log(log(log(day_durbin_watson(Vwap))))), sub(LogFloatCap, LogFloatShares), 241)`
  - score -1.04(train -0.32 valid -1.04):`cross_regbeta(log(day_durbin_watson(Vwap)), sub(LogFloatCap, cross_regbeta(log(day_durbin_watson(Vwap)), sub(LogFloatCap, LogFloatShares), 241)), 241)`
  - score -1.04(train -0.40 valid -1.04):`cross_regbeta(log(pow_05(day_durbin_watson(Vwap))), sub(LogFloatCap, LogFloatShares), 241)`
- `prods2008Pr2a_Ea`:核心 `cross_stddev(log(day_durbin_watson(Vwap)), 120)`;评分 96,过线 0,入 heads 0;采样计数 {'c05_no_core': 1006, 'c05_skeleton': 496, 'mutation_refused': 6, 'c05_periphery_seen': 3}
  - score -0.25(train -0.25 valid +0.27):`cross_mean(cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120))), LogFloatCap)), LogFloatCap))), LogFloatCap), 120)`
  - score -0.43(train -0.43 valid -0.09):`cross_mean(cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(LogFloatCap)), LogFloatCap)), LogFloatCap), 120)`
  - score -0.55(train -0.55 valid -0.41):`cross_mean(cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(cross_stddev(log(day_durbin_watson(Vwap)), 120))), LogFloatCap), 120)`
  - score -0.58(train -0.58 valid +0.32):`cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(day_corr(Volume, Volume))), sub(day_durbin_watson(Vwap), LogFloatShares))`
  - score -0.61(train -0.61 valid -0.24):`cross_mean(cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), cs_bucket_zscore(mul(cross_stddev(log(day_durbin_watson(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120))), LogFloatCap)), LogFloatCap), 120)`
- `prods2008Pr2b_Nb`:核心 `—`;评分 0,过线 0,入 heads 0;采样计数 {}

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(knockout cross_mean(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 3)):`ts_quantile_q75(pow_3(sigmoid(pow_2(day_durbin_watson(Ret)))), 30)`
- 增益 +0.17(knockout sigmoid(pow_2(day_durbin_watson(Ret)))):`ts_quantile_q75(cross_mean(pow_3(pow_2(day_durbin_watson(Ret))), 3), 30)`
