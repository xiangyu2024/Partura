# 定位:种子 2013,P 组,第 2 轮(只含 train / valid)

快照:prods2013M1_I0_open_search, prods2013M2_I0_open_search, prods2013Pr1a_Ea, prods2013Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.04 | +1.15 | +1.04 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 120)` |
| +1.01 | +1.01 | +1.02 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 120)` |
| +0.94 | +0.97 | +0.94 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 120)` |
| +0.76 | +1.13 | +0.76 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 120)` |
| -1.97 | -1.97 | -1.97 | +1 | 20 | prods2013M2_I0_open_search | `ts_quantile_q75(pow_05(pow_05(day_ar1_coefficient(Volume))), 50)` |
| -2.21 | -2.21 | -1.81 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(cs_bucket_demean(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), cross_mean(day_sum(Amt), 20)), 5)` |
| -2.35 | -2.05 | -2.35 | +1 | 0 | prods2013M2_I0_open_search | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(pow_05(day_ar1_coefficient(Volume)))), 5))), 50)` |
| -3.15 | -3.06 | -3.15 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 5)` |
| -3.15 | -3.06 | -3.15 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| -3.31 | -3.31 | -2.78 | -1 | 20 | prods2013M2_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(sigmoid(pow_05(pow_05(day_ar1_coefficient(Volume)))), 5))), 30)` |

## 共性:158 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.79 | 0.000 | 6 | +0.86 / -1.93 | `cross_delay(day_median(Amt), 1)` |
| +1.69 | 0.020 | 4 | -0.18 / -1.87 | `cs_rank(cs_mask_top_replace_mean_neg(day_open(Vwap)))` |
| +1.69 | 0.000 | 14 | -0.29 / -1.98 | `cross_delay(day_sum(Volume), 1)` |
| +1.68 | 0.000 | 13 | -0.29 / -1.97 | `day_median(Amt)` |
| +1.62 | 0.000 | 16 | -0.38 / -1.99 | `cross_delay(cross_zscore(day_sum(Volume), 60), 1)` |
| +1.60 | 0.000 | 56 | -0.80 / -2.39 | `day_sum(Ret)` |
| +1.58 | 0.009 | 5 | -0.30 / -1.88 | `mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` |
| +1.57 | 0.010 | 4 | -0.30 / -1.87 | `mul(day_sum(Volume), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` |
| +1.54 | 0.000 | 22 | -0.50 / -2.04 | `cross_zscore(day_sum(Volume), 60)` |
| +1.44 | 0.011 | 6 | -0.45 / -1.88 | `cs_mask_top_replace_mean_neg(day_open(Vwap))` |
| +1.38 | 0.007 | 7 | -0.51 / -1.89 | `day_open(Vwap)` |
| +1.35 | 0.000 | 52 | -0.92 / -2.27 | `day_sum(Volume)` |
| +0.91 | 0.096 | 4 | -0.94 / -1.85 | `pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))` |
| +0.84 | 0.014 | 10 | -1.04 / -1.88 | `cross_delay(day_sum(Ret), 1)` |
| +0.52 | 0.079 | 15 | -1.36 / -1.88 | `day_wstd(Volume, Open)` |
| +0.48 | 0.171 | 9 | -1.37 / -1.86 | `pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))` |
| +0.45 | 0.228 | 5 | -1.39 / -1.84 | `cs_rank(cs_first_low20(day_wstd(Volume, Open), pow_2(pow_05(day_ar1_coefficient(Volume)))))` |
| +0.45 | 0.228 | 5 | -1.39 / -1.84 | `cs_first_low20(day_wstd(Volume, Open), pow_2(pow_05(day_ar1_coefficient(Volume))))` |
| +0.27 | 0.309 | 7 | -1.57 / -1.84 | `cross_regres(cs_mean(pow_2(pow_05(day_ar1_coefficient(Volume)))), pow_2(pow_05(day_ar1_coefficient(Volume))), 60)` |
| +0.24 | 0.269 | 22 | -1.63 / -1.86 | `cs_rank(day_sum(Volume))` |

## 拆解(46 次评估)

### head score +1.04:`cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume))))` | -2.18 | -1.92 | -2.18 | — | (子树本身) |
| sufficiency | `cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))` | -2.47 | -0.75 | -2.47 | — | (子树本身) |
| sufficiency | `cross_delay(day_median(Amt), 1)` | -3.80 | -3.09 | -3.80 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean_neg(day_sum(Volume))` | -2.57 | -0.74 | -2.57 | — | (子树本身) |
| knockout | `mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume))))` | +0.70 | +0.92 | +0.70 | +0.34 | `cross_regbeta(cross_delay(day_median(Amt), 1), day_sum(Ret), 120)` |
| knockout | `cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))` | +0.88 | +1.16 | +0.88 | +0.16 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_mask_top_replace_mean_neg(day_sum(Volume))), day_sum(Ret), 120)` |
| knockout | `cross_delay(day_median(Amt), 1)` | +0.38 | +0.87 | +0.38 | +0.66 | `cross_regbeta(mul(day_median(Amt), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 120)` |
| knockout | `cs_mask_top_replace_mean_neg(day_sum(Volume))` | -0.37 | +0.50 | -0.37 | +1.41 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(day_sum(Volume))), day_sum(Ret), 120)` |
| swap | `Amt->Volume` | +0.21 | +0.43 | +0.21 | — | `cross_regbeta(mul(cross_delay(day_median(Volume), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 120)` |
| swap | `Volume->Amt` | +0.91 | +0.91 | +1.26 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Amt)))), day_sum(Ret), 120)` |
| window | `cross_regbeta@120->60` | +1.08 | +1.08 | +1.21 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 60)` |
| window | `cross_regbeta@120->240` | +1.03 | +1.16 | +1.03 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 240)` |

### head score +1.01:`cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1))))` | -2.29 | -2.16 | -2.29 | — | (子树本身) |
| sufficiency | `cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))` | -2.70 | -1.02 | -2.70 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1))` | -2.85 | -0.95 | -2.85 | — | (子树本身) |
| sufficiency | `cross_delay(day_median(Amt), 1)` | -3.80 | -3.09 | -3.80 | — | (子树本身) |
| knockout | `mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1))))` | +0.70 | +0.92 | +0.70 | +0.31 | `cross_regbeta(cross_delay(day_median(Amt), 1), day_sum(Ret), 120)` |
| knockout | `cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))` | +0.34 | +0.84 | +0.34 | +0.67 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1))), day_sum(Ret), 120)` |
| knockout | `cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1))` | +0.99 | +0.99 | +1.03 | +0.02 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cross_delay(day_sum(Volume), 1))), day_sum(Ret), 120)` |
| knockout | `cross_delay(day_median(Amt), 1)` | +0.59 | +0.63 | +0.59 | +0.42 | `cross_regbeta(mul(day_median(Amt), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 120)` |
| swap | `Amt->Volume` | +0.53 | +0.53 | +0.81 | — | `cross_regbeta(mul(cross_delay(day_median(Volume), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 120)` |
| swap | `Volume->Amt` | +1.11 | +1.11 | +1.31 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Amt), 1)))), day_sum(Ret), 120)` |
| window | `cross_regbeta@120->60` | +0.82 | +0.82 | +0.96 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 60)` |
| window | `cross_regbeta@120->240` | +1.04 | +1.04 | +1.30 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 240)` |

### head score +0.94:`cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1))` | -2.46 | -2.26 | -2.46 | — | (子树本身) |
| sufficiency | `cross_delay(cross_zscore(day_sum(Amt), 60), 1)` | -1.86 | -1.68 | -1.86 | — | (子树本身) |
| sufficiency | `cross_zscore(day_sum(Amt), 60)` | -1.82 | -1.37 | -1.82 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1))` | +0.49 | +0.94 | +0.49 | +0.46 | `cross_regbeta(day_sum(Amt), day_sum(Ret), 120)` |
| knockout | `cross_delay(cross_zscore(day_sum(Amt), 60), 1)` | +0.66 | +1.37 | +0.66 | +0.29 | `cross_regbeta(mul(day_sum(Amt), cross_zscore(day_sum(Amt), 60)), day_sum(Ret), 120)` |
| knockout | `cross_zscore(day_sum(Amt), 60)` | +0.37 | +0.91 | +0.37 | +0.57 | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_sum(Amt), 1)), day_sum(Ret), 120)` |
| swap | `Amt->Volume` | +0.16 | +0.16 | +0.49 | — | `cross_regbeta(mul(day_sum(Volume), cross_delay(cross_zscore(day_sum(Volume), 60), 1)), day_sum(Ret), 120)` |
| window | `cross_regbeta@120->60` | +0.76 | +0.76 | +1.09 | — | `cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 60)` |
| window | `cross_regbeta@120->240` | +0.66 | +0.66 | +1.12 | — | `cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 240)` |

### head score +0.76:`cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1)))` | -2.79 | -2.28 | -2.79 | — | (子树本身) |
| sufficiency | `mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` | -2.77 | -2.30 | -2.77 | — | (子树本身) |
| sufficiency | `cross_delay(cross_zscore(day_sum(Volume), 60), 1)` | -2.05 | -1.30 | -2.05 | — | (子树本身) |
| sufficiency | `cross_delay(day_median(Amt), 1)` | -3.80 | -3.09 | -3.80 | — | (子树本身) |
| knockout | `mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1)))` | +0.70 | +0.92 | +0.70 | +0.06 | `cross_regbeta(cross_delay(day_median(Amt), 1), day_sum(Ret), 120)` |
| knockout | `mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` | +0.60 | +1.01 | +0.60 | +0.16 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cross_delay(day_sum(Volume), 1)), day_sum(Ret), 120)` |
| knockout | `cross_delay(cross_zscore(day_sum(Volume), 60), 1)` | +0.50 | +0.64 | +0.50 | +0.26 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_zscore(day_sum(Volume), 60))), day_sum(Ret), 120)` |
| knockout | `cross_delay(day_median(Amt), 1)` | +0.66 | +0.81 | +0.66 | +0.10 | `cross_regbeta(mul(day_median(Amt), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 120)` |
| swap | `Amt->Volume` | +0.55 | +0.61 | +0.55 | — | `cross_regbeta(mul(cross_delay(day_median(Volume), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 120)` |
| swap | `Volume->Amt` | +0.86 | +1.25 | +0.86 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 120)` |
| window | `cross_regbeta@120->60` | +0.56 | +0.56 | +0.65 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 60)` |
| window | `cross_regbeta@120->240` | +0.97 | +0.97 | +1.13 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 240)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_delay(day_median(Amt), 1)` — enrichment,均值差 +2.79,p 0.000
2. `cs_rank(cs_mask_top_replace_mean_neg(day_open(Vwap)))` — enrichment,均值差 +1.69,p 0.020
3. `cross_delay(day_sum(Volume), 1)` — enrichment,均值差 +1.69,p 0.000
4. `day_median(Amt)` — enrichment,均值差 +1.68,p 0.000
5. `cross_delay(cross_zscore(day_sum(Volume), 60), 1)` — enrichment,均值差 +1.62,p 0.000
6. `day_sum(Ret)` — enrichment,均值差 +1.60,p 0.000
7. `mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` — enrichment,均值差 +1.58,p 0.009
8. `mul(day_sum(Volume), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` — enrichment,均值差 +1.57,p 0.010
9. `cross_zscore(day_sum(Volume), 60)` — enrichment,均值差 +1.54,p 0.000
10. `cs_mask_top_replace_mean_neg(day_open(Vwap))` — enrichment,均值差 +1.44,p 0.011
11. `day_open(Vwap)` — enrichment,均值差 +1.38,p 0.007
12. `day_sum(Volume)` — enrichment,均值差 +1.35,p 0.000
13. `pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))` — enrichment,均值差 +0.91,p 0.096
14. `cross_delay(day_sum(Ret), 1)` — enrichment,均值差 +0.84,p 0.014
15. `day_wstd(Volume, Open)` — enrichment,均值差 +0.52,p 0.079

## 本组之前各轮的任务

- `prods2013Pr1a_Ea`:核心 `pow_2(pow_05(day_ar1_coefficient(Volume)))`;评分 103,过线 0,入 heads 0;采样计数 {'c05_no_core': 1840, 'c05_skeleton': 930}
  - score +0.12(train +0.66 valid +0.12):`cross_autocorr(cross_regres(cs_mask_top_replace_mean(pow_2(pow_05(day_ar1_coefficient(Volume)))), day_ar1_coefficient(Volume), 60), 60, 1)`
  - score -0.51(train +0.24 valid -0.51):`cross_hurst(cs_rank(cs_first_low20(day_wstd(Volume, Open), pow_2(cross_regres(cs_mean(pow_2(pow_05(day_ar1_coefficient(Volume)))), pow_2(pow_05(day_ar1_coefficient(Volume))), 60)))), 60)`
  - score -0.54(train -0.48 valid -0.54):`cross_hurst(cs_rank(cs_first_low20(day_wstd(Volume, Open), pow_2(pow_2(pow_2(pow_05(cross_hurst(cs_rank(cs_first_low20(day_wstd(Volume, Open), pow_2(pow_05(day_ar1_coefficient(Volume))))), 60))))))), 60)`
  - score -0.58(train -0.58 valid -0.40):`cross_hurst(cs_rank(cs_first_low20(day_wstd(Volume, Open), pow_2(pow_05(day_ar1_coefficient(Volume))))), 60)`
  - score -0.58(train -0.58 valid -0.40):`cross_hurst(cs_rank(cs_first_low20(day_wstd(Volume, Open), pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 60)`
- `prods2013Pr1b_Nb`:核心 `—`;评分 99,过线 7,入 heads 4;采样计数 {'c05_skeleton': 10}
  - score +1.04(train +1.15 valid +1.04):`cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), day_sum(Ret), 120)`
  - score +1.01(train +1.01 valid +1.02):`cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 120)`
  - score +0.97(train +0.97 valid +1.02):`cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_open(Vwap))))))), day_sum(Ret), 120)`
  - score +0.94(train +0.97 valid +0.94):`cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 120)`
  - score +0.76(train +1.13 valid +0.76):`cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(window cross_regbeta@120->240):`cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 240)`
- 增益 +0.10(swap Volume->Amt):`cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 120)`
