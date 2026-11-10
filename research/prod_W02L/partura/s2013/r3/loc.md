# 定位:种子 2013,P 组,第 3 轮(只含 train / valid)

快照:prods2013M1_I0_open_search, prods2013M2_I0_open_search, prods2013M3_I0_open_search, prods2013Pr1a_Ea, prods2013Pr1b_Nb, prods2013Pr2a_Ea, prods2013Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(22 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.22 | +1.22 | +1.47 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), cs_demean(day_sum(Ret)), 120)` |
| +1.13 | +1.13 | +1.31 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 240)` |
| +1.01 | +1.01 | +1.02 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(cross_delay(day_sum(Volume), 1)))), day_sum(Ret), 120)` |
| +0.94 | +0.97 | +0.94 | +1 | 5 | prods2013Pr1b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 120)` |
| +0.87 | +0.96 | +0.87 | -1 | 0 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 120)` |
| +0.81 | +0.89 | +0.81 | -1 | 20 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 120)` |
| +0.81 | +0.81 | +0.83 | -1 | 0 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_max(day_ar1_coefficient(Volume), 15), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_max(day_ar1_coefficient(Volume), 15), 3)), day_sum(Ret), 120), 120)` |
| +0.79 | +0.93 | +0.79 | -1 | 5 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120), 120)` |
| +0.63 | +1.21 | +0.63 | -1 | 0 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_sum(Amt), 1)), cross_regbeta(mul(day_sum(Amt), cross_delay(day_sum(Amt), 1)), day_sum(Ret), 120), 120)` |
| +0.62 | +0.62 | +0.63 | +1 | 0 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 15)), day_sum(Amt), 120), 120)` |
| +0.57 | +1.17 | +0.57 | -1 | 5 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120)` |
| +0.56 | +0.76 | +0.56 | -1 | 5 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120), 120), 120)` |
| +0.53 | +1.27 | +0.53 | -1 | 0 | prods2013Pr2b_Nb | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 10), 120)` |
| -0.41 | -0.37 | -0.41 | +1 | 5 | prods2013M3_I0_open_search | `cross_max(ts_std(day_close(Amt), 40), 10)` |
| -0.50 | -0.50 | +0.15 | +1 | 5 | prods2013M3_I0_open_search | `cross_quantile_q25(cross_mean(ts_regres(ts_autocorr_s1(day_close(High), 30), day_durbin_watson(Vwap), 20), 241), 5)` |
| -0.95 | -0.95 | -0.56 | +1 | 0 | prods2013M3_I0_open_search | `cross_quantile_q25(day_close(Ret), 241)` |
| -1.97 | -1.97 | -1.97 | +1 | 20 | prods2013M2_I0_open_search | `ts_quantile_q75(pow_05(pow_05(day_ar1_coefficient(Volume))), 50)` |
| -2.21 | -2.21 | -1.81 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(cs_bucket_demean(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), cross_mean(day_sum(Amt), 20)), 5)` |
| -2.35 | -2.05 | -2.35 | +1 | 0 | prods2013M2_I0_open_search | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(pow_05(day_ar1_coefficient(Volume)))), 5))), 50)` |
| -3.15 | -3.06 | -3.15 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 5)` |
| -3.15 | -3.06 | -3.15 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| -3.31 | -3.31 | -2.78 | -1 | 20 | prods2013M2_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(sigmoid(pow_05(pow_05(day_ar1_coefficient(Volume)))), 5))), 30)` |

## 共性:330 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.59 | 0.000 | 6 | +0.86 / -1.73 | `cross_delay(day_median(Amt), 1)` |
| +2.46 | 0.001 | 4 | +0.75 / -1.71 | `mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 15))` |
| +2.18 | 0.000 | 6 | +0.46 / -1.72 | `cross_max(day_ar1_coefficient(Volume), 15)` |
| +2.01 | 0.000 | 31 | +0.14 / -1.87 | `day_sum(Amt)` |
| +1.98 | 0.000 | 13 | +0.22 / -1.76 | `mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))` |
| +1.96 | 0.001 | 5 | +0.24 / -1.71 | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120)` |
| +1.79 | 0.000 | 22 | -0.01 / -1.80 | `cross_delay(day_ar1_coefficient(Volume), 1)` |
| +1.52 | 0.032 | 4 | -0.18 / -1.70 | `cs_rank(cs_mask_top_replace_mean_neg(day_open(Vwap)))` |
| +1.45 | 0.000 | 14 | -0.29 / -1.74 | `cross_delay(day_sum(Volume), 1)` |
| +1.45 | 0.000 | 13 | -0.29 / -1.74 | `day_median(Amt)` |
| +1.40 | 0.011 | 4 | -0.30 / -1.70 | `mul(day_sum(Volume), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` |
| +1.40 | 0.011 | 5 | -0.30 / -1.70 | `mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` |
| +1.39 | 0.000 | 146 | -0.91 / -2.30 | `day_sum(Ret)` |
| +1.33 | 0.011 | 5 | -0.37 / -1.70 | `mul(day_sum(Amt), day_ar1_coefficient(Volume))` |
| +1.26 | 0.017 | 6 | -0.45 / -1.70 | `cs_mask_top_replace_mean_neg(day_open(Vwap))` |
| +1.19 | 0.012 | 7 | -0.51 / -1.71 | `day_open(Vwap)` |
| +0.75 | 0.097 | 4 | -0.94 / -1.69 | `pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))` |
| +0.67 | 0.012 | 11 | -1.04 / -1.70 | `cross_delay(day_sum(Ret), 1)` |
| +0.63 | 0.000 | 132 | -1.30 / -1.93 | `day_sum(Volume)` |
| +0.58 | 0.001 | 56 | -1.20 / -1.78 | `cross_delay(cross_zscore(day_sum(Volume), 60), 1)` |

## 拆解(45 次评估)

### head score +1.22:`cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), cs_demean(day_sum(Ret)), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume))))` | -2.18 | -1.92 | -2.18 | — | (子树本身) |
| sufficiency | `cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))` | -2.47 | -0.75 | -2.47 | — | (子树本身) |
| sufficiency | `cross_delay(day_median(Amt), 1)` | -3.80 | -3.09 | -3.80 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean_neg(day_sum(Volume))` | -2.57 | -0.74 | -2.57 | — | (子树本身) |
| knockout | `mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume))))` | +0.75 | +0.75 | +1.20 | +0.47 | `cross_regbeta(cross_delay(day_median(Amt), 1), cs_demean(day_sum(Ret)), 120)` |
| knockout | `cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))` | +1.19 | +1.19 | +1.29 | +0.03 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_mask_top_replace_mean_neg(day_sum(Volume))), cs_demean(day_sum(Ret)), 120)` |
| knockout | `cross_delay(day_median(Amt), 1)` | +0.69 | +0.87 | +0.69 | +0.53 | `cross_regbeta(mul(day_median(Amt), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), cs_demean(day_sum(Ret)), 120)` |
| knockout | `cs_mask_top_replace_mean_neg(day_sum(Volume))` | -0.24 | +0.63 | -0.24 | +1.46 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(day_sum(Volume))), cs_demean(day_sum(Ret)), 120)` |
| swap | `Amt->Volume` | +0.73 | +0.73 | +0.85 | — | `cross_regbeta(mul(cross_delay(day_median(Volume), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), cs_demean(day_sum(Ret)), 120)` |
| swap | `Volume->Amt` | +0.84 | +0.84 | +1.26 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Amt)))), cs_demean(day_sum(Ret)), 120)` |
| window | `cross_regbeta@120->60` | +1.13 | +1.13 | +1.38 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), cs_demean(day_sum(Ret)), 60)` |
| window | `cross_regbeta@120->240` | +0.93 | +1.05 | +0.93 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cs_rank(cs_mask_top_replace_mean_neg(day_sum(Volume)))), cs_demean(day_sum(Ret)), 240)` |

### head score +1.13:`cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 240)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1)))` | -2.43 | -2.27 | -2.43 | — | (子树本身) |
| sufficiency | `mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))` | -2.46 | -2.25 | -2.46 | — | (子树本身) |
| sufficiency | `cross_delay(cross_zscore(day_sum(Amt), 60), 1)` | -1.86 | -1.68 | -1.86 | — | (子树本身) |
| sufficiency | `cross_delay(day_median(Amt), 1)` | -3.80 | -3.09 | -3.80 | — | (子树本身) |
| knockout | `mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1)))` | +0.91 | +0.91 | +1.20 | +0.22 | `cross_regbeta(cross_delay(day_median(Amt), 1), day_sum(Ret), 240)` |
| knockout | `mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))` | +1.09 | +1.09 | +1.28 | +0.04 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), cross_delay(day_sum(Amt), 1)), day_sum(Ret), 240)` |
| knockout | `cross_delay(cross_zscore(day_sum(Amt), 60), 1)` | +0.19 | +1.07 | +0.19 | +0.94 | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_zscore(day_sum(Amt), 60))), day_sum(Ret), 240)` |
| knockout | `cross_delay(day_median(Amt), 1)` | +0.97 | +0.97 | +1.19 | +0.16 | `cross_regbeta(mul(day_median(Amt), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 240)` |
| swap | `Amt->Volume` | +0.49 | +0.49 | +0.85 | — | `cross_regbeta(mul(cross_delay(day_median(Volume), 1), mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))), day_sum(Ret), 240)` |
| window | `cross_regbeta@240->120` | +0.86 | +1.25 | +0.86 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 120)` |
| window | `cross_regbeta@240->480` | +0.99 | +0.99 | +1.11 | — | `cross_regbeta(mul(cross_delay(day_median(Amt), 1), mul(cross_delay(day_sum(Amt), 1), cross_delay(cross_zscore(day_sum(Amt), 60), 1))), day_sum(Ret), 480)` |

### head score +0.87:`cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120)` | +0.91 | +1.43 | +0.91 | — | (子树本身) |
| sufficiency | `mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)))` | -3.83 | -3.15 | -3.83 | — | (子树本身) |
| sufficiency | `mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))` | -3.25 | -3.25 | -2.16 | — | (子树本身) |
| knockout | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120)` | — | — | — | — | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), 120)` |
| knockout | `mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)))` | +0.41 | +0.91 | +0.41 | +0.46 | `cross_regbeta(day_sum(Amt), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 120)` |
| knockout | `mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)))` | +0.98 | +1.17 | +0.98 | -0.11 | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(day_sum(Amt), day_sum(Ret), 120), 120)` |
| knockout | `mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))` | +0.92 | +1.15 | +0.92 | -0.06 | `cross_regbeta(mul(day_sum(Amt), day_sum(Amt)), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 120)` |
| swap | `Amt->Volume` | +0.53 | +0.59 | +0.53 | — | `cross_regbeta(mul(day_sum(Volume), mul(day_sum(Volume), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(mul(day_sum(Volume), mul(day_sum(Volume), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 120)` |
| swap | `Volume->Amt` | +0.91 | +0.96 | +0.91 | — | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Amt), 1))), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Amt), 1))), day_sum(Ret), 120), 120)` |
| window | `cross_regbeta@120->60` | +0.65 | +0.78 | +0.65 | — | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 60)` |
| window | `cross_regbeta@120->240` | +0.69 | +0.94 | +0.69 | — | `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 240)` |

### head score +0.81:`cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120)` | +0.62 | +0.86 | +0.62 | — | (子树本身) |
| sufficiency | `mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15))` | -3.62 | -2.81 | -3.62 | — | (子树本身) |
| sufficiency | `cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)` | -1.67 | -1.32 | -1.67 | — | (子树本身) |
| knockout | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120)` | — | — | — | — | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), 120)` |
| knockout | `mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15))` | +0.89 | +0.92 | +0.89 | -0.07 | `cross_regbeta(day_sum(Amt), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 120)` |
| knockout | `mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15))` | +0.76 | +0.87 | +0.76 | +0.05 | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(day_sum(Amt), day_sum(Ret), 120), 120)` |
| knockout | `cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)` | +0.85 | +1.13 | +0.85 | -0.04 | `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 120)` |
| swap | `Amt->Volume` | +0.13 | +0.56 | +0.13 | — | `cross_regbeta(mul(day_sum(Volume), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(mul(day_sum(Volume), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 120)` |
| swap | `Volume->Amt` | +0.82 | +0.92 | +0.82 | — | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Amt), 1), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Amt), 1), 15)), day_sum(Ret), 120), 120)` |
| window | `cross_regbeta@120->60` | -0.03 | +0.50 | -0.03 | — | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 60)` |
| window | `cross_regbeta@120->240` | +0.77 | +1.04 | +0.77 | — | `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 240)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120)` — ablation,自身 score +0.91(所在 head +0.87)
2. `cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120)` — ablation,自身 score +0.62(所在 head +0.81)
3. `cross_delay(day_median(Amt), 1)` — enrichment,均值差 +2.59,p 0.000
4. `mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 15))` — enrichment,均值差 +2.46,p 0.001
5. `cross_max(day_ar1_coefficient(Volume), 15)` — enrichment,均值差 +2.18,p 0.000
6. `day_sum(Amt)` — enrichment,均值差 +2.01,p 0.000
7. `mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))` — enrichment,均值差 +1.98,p 0.000
8. `cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120)` — enrichment,均值差 +1.96,p 0.001
9. `cross_delay(day_ar1_coefficient(Volume), 1)` — enrichment,均值差 +1.79,p 0.000
10. `cs_rank(cs_mask_top_replace_mean_neg(day_open(Vwap)))` — enrichment,均值差 +1.52,p 0.032
11. `cross_delay(day_sum(Volume), 1)` — enrichment,均值差 +1.45,p 0.000
12. `day_median(Amt)` — enrichment,均值差 +1.45,p 0.000
13. `mul(day_sum(Volume), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` — enrichment,均值差 +1.40,p 0.011
14. `mul(cross_delay(day_sum(Volume), 1), cross_delay(cross_zscore(day_sum(Volume), 60), 1))` — enrichment,均值差 +1.40,p 0.011
15. `day_sum(Ret)` — enrichment,均值差 +1.39,p 0.000
16. `mul(day_sum(Amt), day_ar1_coefficient(Volume))` — enrichment,均值差 +1.33,p 0.011
17. `cs_mask_top_replace_mean_neg(day_open(Vwap))` — enrichment,均值差 +1.26,p 0.017
18. `day_open(Vwap)` — enrichment,均值差 +1.19,p 0.012
19. `pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))` — enrichment,均值差 +0.75,p 0.097
20. `cross_delay(day_sum(Ret), 1)` — enrichment,均值差 +0.67,p 0.012
21. `day_sum(Volume)` — enrichment,均值差 +0.63,p 0.000
22. `cross_delay(cross_zscore(day_sum(Volume), 60), 1)` — enrichment,均值差 +0.58,p 0.001
23. `cross_zscore(day_sum(Volume), 60)` — enrichment,均值差 +0.46,p 0.001

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
- `prods2013Pr2a_Ea`:核心 `cross_zscore(day_sum(Volume), 60)`;评分 103,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 12, 'c05_no_core': 888, 'c05_skeleton': 437}
  - score -0.29(train -0.29 valid +0.30):`cross_regbeta(cross_delay(cross_zscore(day_sum(Volume), 60), 1), cs_robust_z(day_sum(Ret)), 120)`
  - score -0.33(train -0.33 valid +0.13):`cross_regbeta(cross_delay(cross_delay(cs_demean(cross_zscore(day_sum(Volume), 60)), 1), 1), day_sum(Ret), 120)`
  - score -0.44(train -0.44 valid +0.20):`cross_regbeta(cross_delay(cs_demean(cross_delay(cross_zscore(day_sum(Volume), 60), 1)), 1), cs_robust_z(day_sum(Ret)), 120)`
  - score -0.45(train -0.45 valid +0.60):`cross_regbeta(cross_delay(cross_zscore(day_sum(Volume), 60), 1), cs_demean(day_sum(Ret)), 120)`
  - score -0.46(train -0.12 valid -0.46):`cross_regbeta(cross_delay(cross_delay(cross_zscore(day_sum(Volume), 60), 1), 1), day_sum(Ret), 120)`
- `prods2013Pr2b_Nb`:核心 `—`;评分 83,过线 14,入 heads 9;采样计数 {'c05_skeleton': 16}
  - score +0.87(train +0.96 valid +0.87):`cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), day_sum(Ret), 120), 120)`
  - score +0.81(train +0.89 valid +0.81):`cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_delay(day_ar1_coefficient(Volume), 1), 15)), day_sum(Ret), 120), 120)`
  - score +0.81(train +0.90 valid +0.81):`cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), cross_regbeta(mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 15)), day_sum(Ret), 120), 120)`
  - score +0.81(train +0.81 valid +0.83):`cross_regbeta(mul(day_sum(Amt), cross_max(cross_max(day_ar1_coefficient(Volume), 15), 15)), cross_regbeta(mul(day_sum(Amt), cross_max(cross_max(day_ar1_coefficient(Volume), 15), 3)), day_sum(Ret), 120), 120)`
  - score +0.81(train +0.82 valid +0.81):`cross_regbeta(mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 60)), cross_regbeta(mul(day_sum(Amt), cross_max(day_ar1_coefficient(Volume), 60)), day_sum(Ret), 120), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.11(knockout mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)))):`cross_regbeta(mul(day_sum(Amt), mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1))), cross_regbeta(day_sum(Amt), day_sum(Ret), 120), 120)`
