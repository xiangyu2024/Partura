# 定位:种子 2026,P 组,第 2 轮(只含 train / valid)

快照:prods2026M1_I0_open_search, prods2026M2_I0_open_search, prods2026Pr1a_Ea, prods2026Pr1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.61 | -1.61 | -1.21 | +1 | 5 | prods2026M1_I0_open_search | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120))` |
| -1.70 | -1.70 | -1.65 | +1 | 20 | prods2026M1_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)` |
| -1.73 | -1.73 | -1.29 | +1 | 5 | prods2026M1_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 120)` |
| -3.31 | -2.89 | -3.31 | +1 | 20 | prods2026M2_I0_open_search | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |
| -3.33 | -2.89 | -3.33 | +1 | 20 | prods2026M2_I0_open_search | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), ts_mean(day_durbin_watson(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| -3.38 | -3.31 | -3.38 | -1 | 20 | prods2026M2_I0_open_search | `ts_stddev(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |

## 共性:135 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.78 | 0.000 | 6 | -0.87 / -2.65 | `cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)), day_flat_run_max(in_slice(Ret, 11, 230)), 120)` |
| +1.48 | 0.000 | 17 | -1.28 / -2.76 | `day_flat_run_max(in_slice(Ret, 11, 230))` |
| +1.32 | 0.024 | 4 | -1.29 / -2.61 | `cross_ema(cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares)), 40)` |
| +1.29 | 0.000 | 20 | -1.48 / -2.76 | `cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` |
| +1.26 | 0.017 | 5 | -1.36 / -2.62 | `cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares))` |
| +1.18 | 0.015 | 6 | -1.44 / -2.63 | `sub(LogFloatCap, LogFloatShares)` |
| +1.16 | 0.002 | 10 | -1.50 / -2.66 | `abs_(LogTotalCap)` |
| +1.14 | 0.003 | 9 | -1.51 / -2.65 | `ts_pearson(cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap)), 10)` |
| +1.14 | 0.003 | 9 | -1.51 / -2.65 | `cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap))` |
| +1.09 | 0.003 | 9 | -1.55 / -2.65 | `abs_(day_hurst(High))` |
| +1.09 | 0.003 | 9 | -1.55 / -2.65 | `day_hurst(High)` |
| +1.08 | 0.015 | 6 | -1.54 / -2.62 | `cross_reg_fvalue(day_es_ratio_hi(High), day_quantile_q25(Low), 241)` |
| +1.06 | 0.003 | 8 | -1.57 / -2.64 | `sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120))` |
| +1.06 | 0.004 | 10 | -1.59 / -2.65 | `ts_delta(LogTotalCap, 1)` |
| +0.95 | 0.042 | 6 | -1.67 / -2.62 | `cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20)` |
| +0.77 | 0.139 | 4 | -1.83 / -2.60 | `cross_corr(day_ar1_coefficient(in_slice(Ret, 11, 230)), day_sum(in_slice(Ret, 11, 230)), 120)` |
| +0.76 | 0.013 | 15 | -1.90 / -2.66 | `day_es_ratio_hi(High)` |
| +0.74 | 0.029 | 12 | -1.90 / -2.64 | `day_quantile_q25(Low)` |
| +0.72 | 0.019 | 10 | -1.90 / -2.63 | `cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` |
| +0.66 | 0.053 | 10 | -1.97 / -2.62 | `day_corr(in_delay(in_slice(Ret, 11, 230), 3), in_slice(Ret, 11, 230))` |

## 拆解(26 次评估)

### head score -1.61:`add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120)` | -1.77 | -1.77 | -1.27 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` | -3.81 | -3.81 | -3.06 | — | (子树本身) |
| sufficiency | `ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` | -1.83 | -1.83 | -1.78 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(in_slice(Ret, 11, 230))` | -3.60 | -3.57 | -3.60 | — | (子树本身) |
| knockout | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120)` | -3.91 | -3.91 | -2.97 | +2.30 | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))))` |
| knockout | `ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` | -3.76 | -3.67 | -3.76 | +2.15 | `add(day_ar1_coefficient(in_slice(Ret, 11, 230)), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120))` |
| swap | `Volume->Amt` | -1.58 | -1.58 | -1.25 | — | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 120))` |
| window | `ts_stddev@120->60` | -1.87 | -1.67 | -1.87 | — | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 60), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120))` |
| window | `ts_stddev@120->240` | -1.65 | -1.65 | -1.23 | — | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 240), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120))` |

### head score -1.70:`ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` | -3.81 | -3.81 | -3.06 | — | (子树本身) |
| swap | `Volume->Amt` | -1.66 | -1.66 | -1.54 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 60)` |
| window | `ts_stddev@60->30` | -2.23 | -2.23 | -1.81 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 30)` |
| window | `ts_stddev@60->120` | -1.77 | -1.77 | -1.27 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120)` |

### head score -1.73:`ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` | -3.81 | -3.81 | -3.05 | — | (子树本身) |
| swap | `Amt->Volume` | -1.77 | -1.77 | -1.27 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 120)` |
| window | `ts_stddev@120->60` | -1.66 | -1.66 | -1.54 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 60)` |
| window | `ts_stddev@120->240` | -2.11 | -2.11 | -0.26 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 240)` |

### head score -3.31:`add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` | -3.66 | -3.66 | -3.19 | — | (子树本身) |
| sufficiency | `day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` | -3.98 | -3.98 | -3.10 | — | (子树本身) |
| sufficiency | `ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15)` | -3.71 | -3.34 | -3.71 | — | (子树本身) |
| sufficiency | `day_durbin_watson(in_slice(Ret, 11, 230))` | -3.58 | -3.58 | -3.48 | — | (子树本身) |
| knockout | `ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` | -3.29 | -2.97 | -3.29 | -0.02 | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))))` |
| knockout | `ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15)` | -3.18 | -2.92 | -3.18 | -0.13 | `add(day_durbin_watson(in_slice(Ret, 11, 230)), ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |
| swap | `Amt->Volume` | -3.28 | -2.89 | -3.28 | — | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 15), ts_mean(day_durbin_watson(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| window | `ts_mean@15->7` | -3.21 | -2.95 | -3.21 | — | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 7), ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |
| window | `ts_mean@15->30` | -3.28 | -2.78 | -3.28 | — | `add(ts_mean(day_durbin_watson(in_slice(Ret, 11, 230)), 30), ts_mean(day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_corr(sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)), day_flat_run_max(in_slice(Ret, 11, 230)), 120)` — enrichment,均值差 +1.78,p 0.000
2. `day_flat_run_max(in_slice(Ret, 11, 230))` — enrichment,均值差 +1.48,p 0.000
3. `cross_ema(cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares)), 40)` — enrichment,均值差 +1.32,p 0.024
4. `cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` — enrichment,均值差 +1.29,p 0.000
5. `cs_regres(cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +1.26,p 0.017
6. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +1.18,p 0.015
7. `abs_(LogTotalCap)` — enrichment,均值差 +1.16,p 0.002
8. `ts_pearson(cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap)), 10)` — enrichment,均值差 +1.14,p 0.003
9. `cs_bucket_zscore(ts_delta(LogTotalCap, 1), abs_(LogTotalCap))` — enrichment,均值差 +1.14,p 0.003
10. `abs_(day_hurst(High))` — enrichment,均值差 +1.09,p 0.003
11. `day_hurst(High)` — enrichment,均值差 +1.09,p 0.003
12. `cross_reg_fvalue(day_es_ratio_hi(High), day_quantile_q25(Low), 241)` — enrichment,均值差 +1.08,p 0.015
13. `sub(cross_tail_mean_q75(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120), cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120))` — enrichment,均值差 +1.06,p 0.003
14. `ts_delta(LogTotalCap, 1)` — enrichment,均值差 +1.06,p 0.004
15. `cross_ema(day_ar1_coefficient(in_slice(Ret, 11, 230)), 20)` — enrichment,均值差 +0.95,p 0.042
16. `day_es_ratio_hi(High)` — enrichment,均值差 +0.76,p 0.013
17. `day_quantile_q25(Low)` — enrichment,均值差 +0.74,p 0.029
18. `cross_med(day_ar1_coefficient(in_slice(Ret, 11, 230)), 120)` — enrichment,均值差 +0.72,p 0.019
19. `day_corr(in_delay(in_slice(Ret, 11, 230), 3), in_slice(Ret, 11, 230))` — enrichment,均值差 +0.66,p 0.053
20. `is_gt(ListAge, 130)` — enrichment,均值差 +0.46,p 0.048
21. `replace_small_with_nan(is_gt(ListAge, 130))` — enrichment,均值差 +0.46,p 0.048

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

## 比原 head 好的拆解变体(R 候选)

(没有)
