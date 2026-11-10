# 定位:种子 2025,P 组,第 3 轮(只含 train / valid)

快照:prods2025M1_I0_open_search, prods2025M2_I0_open_search, prods2025M3_I0_open_search, prods2025Pr1a_Ea, prods2025Pr1b_Nb, prods2025Pr2a_Ea, prods2025Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.28 | -0.28 | -0.13 | +1 | 0 | prods2025M1_I0_open_search | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 5)), 160)` |
| -1.42 | -1.28 | -1.42 | -1 | 5 | prods2025M2_I0_open_search | `day_sum(in_slice(Volume, 2, 237))` |
| -1.53 | -1.34 | -1.53 | -1 | 20 | prods2025M2_I0_open_search | `day_sum(in_slice(Volume, 238, 240))` |
| -1.69 | -1.61 | -1.69 | -1 | 0 | prods2025M1_I0_open_search | `ts_mean(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)` |
| -2.04 | -2.04 | -0.84 | -1 | 5 | prods2025M3_I0_open_search | `cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 20)` |
| -2.14 | -2.14 | -2.13 | +1 | 20 | prods2025M2_I0_open_search | `cross_ema(div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240))), 120)` |
| -2.37 | -1.68 | -2.37 | -1 | 5 | prods2025M3_I0_open_search | `cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 20)` |
| -2.44 | -2.44 | -1.35 | -1 | 20 | prods2025M3_I0_open_search | `cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9), 20)` |
| -2.47 | -2.00 | -2.47 | +1 | 5 | prods2025M1_I0_open_search | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` |

## 共性:246 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.92 | 0.004 | 4 | -0.28 / -2.20 | `cs_first_low20(LogFloatShares, LogFloatShares)` |
| +1.55 | 0.002 | 5 | -0.66 / -2.20 | `cross_decay_linear(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)` |
| +1.40 | 0.008 | 4 | -0.79 / -2.19 | `day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5))` |
| +1.30 | 0.001 | 8 | -0.92 / -2.21 | `day_median(Vwap)` |
| +1.28 | 0.002 | 7 | -0.92 / -2.21 | `cs_last_high10(sub(LogTotalCap, day_centroid(High)), day_median(Vwap))` |
| +1.27 | 0.033 | 4 | -0.92 / -2.19 | `day_kurt(Volume)` |
| +1.05 | 0.015 | 7 | -1.15 / -2.20 | `ts_med(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 20)` |
| +0.96 | 0.055 | 5 | -1.23 / -2.19 | `sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |
| +0.91 | 0.061 | 5 | -1.28 / -2.19 | `cross_ema(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 5)` |
| +0.78 | 0.064 | 7 | -1.41 / -2.19 | `cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30)` |
| +0.76 | 0.058 | 8 | -1.43 / -2.20 | `day_sum(Amt)` |
| +0.75 | 0.036 | 10 | -1.45 / -2.20 | `day_centroid(High)` |
| +0.75 | 0.036 | 10 | -1.45 / -2.20 | `sub(LogTotalCap, day_centroid(High))` |
| +0.73 | 0.001 | 46 | -1.58 / -2.31 | `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |
| +0.72 | 0.123 | 5 | -1.46 / -2.19 | `ts_hurst(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)` |
| +0.72 | 0.123 | 5 | -1.46 / -2.19 | `cs_last_high40(day_centroid(Open), ts_hurst(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40))` |
| +0.71 | 0.001 | 47 | -1.60 / -2.31 | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` |
| +0.69 | 0.039 | 13 | -1.52 / -2.21 | `day_centroid(Open)` |
| +0.68 | 0.106 | 7 | -1.51 / -2.19 | `log(day_sum(Amt))` |
| +0.62 | 0.066 | 13 | -1.58 / -2.20 | `day_wmean(in_slice(Volume, 1, 50), in_slice(Volume, 1, 50))` |

## 拆解(19 次评估)

### head score -0.28:`ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 5)), 160)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 5))` | -4.20 | -4.20 | -3.96 | — | (子树本身) |
| swap | `Volume->Amt` | -0.28 | -0.28 | -0.12 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 5)), 160)` |
| window | `ts_stddev@160->80` | -0.83 | -0.83 | -0.79 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 5)), 80)` |
| window | `ts_stddev@160->320` | -0.94 | -0.94 | -0.10 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 5)), 320)` |

### head score -2.04:`cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median')` | -5.18 | -5.18 | -3.22 | — | (子树本身) |
| swap | `Volume->Amt` | -1.84 | -1.84 | -0.99 | — | `cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Amt, 2, 240), 0.9, 'median'), 20)` |
| window | `cross_mean@20->10` | -2.07 | -2.07 | -0.87 | — | `cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 10)` |
| window | `cross_mean@20->40` | -2.18 | -2.18 | -1.27 | — | `cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 40)` |

### head score -2.14:`cross_ema(div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240))), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240)))` | -4.76 | -4.76 | -4.26 | — | (子树本身) |
| sufficiency | `day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240)))` | -5.79 | -5.79 | -5.47 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Volume, 191, 240))` | -1.56 | -1.32 | -1.56 | — | (子树本身) |
| knockout | `div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240)))` | -2.16 | -1.89 | -2.16 | +0.02 | `cross_ema(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), 120)` |
| swap | `Volume->Amt` | -2.19 | -2.15 | -2.19 | — | `cross_ema(div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Amt, 191, 240))), day_sum(in_slice(Amt, 191, 240))), 120)` |
| window | `cross_ema@120->60` | -2.05 | -2.05 | -2.05 | — | `cross_ema(div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240))), 60)` |
| window | `cross_ema@120->240` | -2.22 | -2.22 | -1.75 | — | `cross_ema(div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240))), 240)` |

### head score -2.37:`cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median')` | -5.18 | -5.18 | -3.22 | — | (子树本身) |
| swap | `Volume->Amt` | -2.11 | -2.11 | -2.05 | — | `cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Amt, 2, 240), 0.9, 'median'), 20)` |
| window | `cross_stddev@20->10` | -1.80 | -1.67 | -1.80 | — | `cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 10)` |
| window | `cross_stddev@20->40` | -2.50 | -2.50 | -2.01 | — | `cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(LogFloatShares, LogFloatShares)` — enrichment,均值差 +1.92,p 0.004
2. `cross_decay_linear(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)` — enrichment,均值差 +1.55,p 0.002
3. `day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5))` — enrichment,均值差 +1.40,p 0.008
4. `day_median(Vwap)` — enrichment,均值差 +1.30,p 0.001
5. `cs_last_high10(sub(LogTotalCap, day_centroid(High)), day_median(Vwap))` — enrichment,均值差 +1.28,p 0.002
6. `day_kurt(Volume)` — enrichment,均值差 +1.27,p 0.033
7. `ts_med(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 20)` — enrichment,均值差 +1.05,p 0.015
8. `sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` — enrichment,均值差 +0.96,p 0.055
9. `cross_ema(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 5)` — enrichment,均值差 +0.91,p 0.061
10. `cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30)` — enrichment,均值差 +0.78,p 0.064
11. `day_sum(Amt)` — enrichment,均值差 +0.76,p 0.058
12. `day_centroid(High)` — enrichment,均值差 +0.75,p 0.036
13. `sub(LogTotalCap, day_centroid(High))` — enrichment,均值差 +0.75,p 0.036
14. `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` — enrichment,均值差 +0.73,p 0.001
15. `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` — enrichment,均值差 +0.71,p 0.001
16. `day_centroid(Open)` — enrichment,均值差 +0.69,p 0.039
17. `day_wmean(in_slice(Volume, 1, 50), in_slice(Volume, 1, 50))` — enrichment,均值差 +0.62,p 0.066
18. `day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))` — enrichment,均值差 +0.59,p 0.098
19. `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` — enrichment,均值差 +0.55,p 0.012
20. `day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` — enrichment,均值差 +0.43,p 0.000
21. `sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` — enrichment,均值差 +0.41,p 0.000
22. `day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` — enrichment,均值差 +0.34,p 0.001

## 本组之前各轮的任务

- `prods2025Pr1a_Ea`:核心 `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))`;评分 91,过线 0,入 heads 0;采样计数 {'c05_no_core': 1811, 'c05_skeleton': 863}
  - score -0.25(train -0.25 valid -0.11):`cross_max(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 3), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.31(train -0.23 valid -0.31):`cross_max(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.33(train -0.06 valid -0.33):`cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.40(train +0.07 valid -0.40):`cross_max(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_mean(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.45(train -0.45 valid -0.35):`cross_max(sub(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
- `prods2025Pr1b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.43(train -0.43 valid +0.48):`cross_mean(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.50(train +0.49 valid -0.50):`cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Ret, 11, 240))), 60)`
  - score -0.72(train +0.20 valid -0.72):`cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))), 60)`
  - score -0.72(train +0.20 valid -0.72):`cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))), 60)`
  - score -0.79(train +0.13 valid -0.79):`cross_ema(cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))), 60), 60)`
- `prods2025Pr2a_Ea`:核心 `sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))`;评分 77,过线 0,入 heads 0;采样计数 {'c05_no_core': 1042, 'c05_skeleton': 428, 'c05_periphery_seen': 9}
  - score -0.34(train -0.34 valid -0.00):`cross_decay_linear(cross_decay_linear(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241), 60)`
  - score -0.40(train -0.40 valid -0.18):`cross_sum(sub(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.40(train -0.40 valid +0.24):`cross_sum(cross_decay_linear(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241), 241)`
  - score -0.45(train -0.45 valid +0.03):`cross_sum(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.46(train -0.46 valid +0.34):`cross_decay_linear(cross_decay_linear(cross_decay_linear(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241), 241), 60)`
- `prods2025Pr2b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score +0.49(train +0.99 valid +0.49):`cross_mean(cs_first_low20(LogFloatShares, day_wmean(in_slice(Volume, 1, 50), in_slice(Volume, 1, 50))), 15)`
  - score +0.46(train +0.46 valid +0.92):`cross_mean(cs_first_low20(LogFloatShares, LogFloatShares), 30)`
  - score +0.45(train +0.45 valid +0.87):`cross_mean(cs_first_low20(LogFloatShares, LogFloatShares), 3)`
  - score +0.25(train +0.25 valid +0.55):`cs_first_low20(cs_first_low20(LogFloatShares, day_kurt(Volume)), cs_first_low20(LogFloatShares, day_kurt(Volume)))`
  - score +0.17(train +0.86 valid +0.17):`cross_mean(cs_first_low20(LogFloatShares, day_wmean(in_slice(Volume, 1, 50), in_slice(Volume, 1, 50))), 3)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.57(window cross_stddev@20->10):`cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9, 'median'), 10)`
- 增益 +0.26(swap Volume->Amt):`cross_stddev(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Amt, 2, 240), 0.9, 'median'), 20)`
- 增益 +0.20(swap Volume->Amt):`cross_mean(day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Amt, 2, 240), 0.9, 'median'), 20)`
