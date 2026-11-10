# 定位:种子 2020,P 组,第 3 轮(只含 train / valid)

快照:prods2020M1_I0_open_search, prods2020M2_I0_open_search, prods2020M3_I0_open_search, prods2020Pr1a_Ea, prods2020Pr1b_Nb, prods2020Pr2a_Na, prods2020Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.79 | +0.79 | +0.88 | +1 | 5 | prods2020Pr2b_Nb | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 241)` |
| +0.59 | +0.59 | +0.89 | +1 | 5 | prods2020Pr2b_Nb | `cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 241)` |
| -1.02 | -1.02 | -0.43 | +1 | 5 | prods2020M1_I0_open_search | `cs_bucket_zscore(cross_mean(abs_(day_skew(Open)), 241), LogFloatCap)` |
| -1.12 | -1.12 | -0.86 | +1 | 0 | prods2020M2_I0_open_search | `ts_sum(cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15), 50)` |
| -1.29 | -1.19 | -1.29 | -1 | 5 | prods2020M2_I0_open_search | `cross_regalpha(day_sum(Volume), day_argmin(Ret), 15)` |
| -1.45 | -0.77 | -1.45 | -1 | 5 | prods2020M2_I0_open_search | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))` |
| -1.66 | -1.66 | -0.76 | +1 | 20 | prods2020M3_I0_open_search | `div(ts_skew(abs_(day_max(Low)), 30), log(ts_sum(day_argmin(Amt), 50)))` |
| -2.47 | -1.45 | -2.47 | +1 | 5 | prods2020M3_I0_open_search | `div(div(day_var(Ret), day_max(High)), log(ts_sum(day_argmin(High), 50)))` |
| -2.69 | -2.69 | -1.49 | +1 | 20 | prods2020M3_I0_open_search | `ts_sum(ts_sum(day_argmin(Amt), 50), 50)` |
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `pow_2(abs_(day_skew(Open)))` |
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `abs_(pow_2(abs_(day_skew(Open))))` |

## 共性:247 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.06 | 0.000 | 26 | -0.07 / -2.14 | `day_topw_mean(pow_2_5(Volume), cross_semistd_neg(Vwap, 10))` |
| +1.68 | 0.000 | 38 | -0.50 / -2.18 | `day_es_ratio_lo(Close)` |
| +1.59 | 0.000 | 36 | -0.57 / -2.15 | `sigmoid(day_es_ratio_lo(Close))` |
| +1.54 | 0.010 | 4 | -0.40 / -1.95 | `cross_delta(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 3)` |
| +1.31 | 0.000 | 67 | -0.96 / -2.28 | `day_centroid(in_slice(Amt, 1, 240))` |
| +1.27 | 0.000 | 25 | -0.78 / -2.05 | `cs_demean(day_centroid(in_slice(Amt, 1, 240)))` |
| +1.26 | 0.002 | 11 | -0.72 / -1.98 | `day_quantile_q25(Vwap)` |
| +1.21 | 0.000 | 21 | -0.81 / -2.02 | `cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)` |
| +1.19 | 0.043 | 6 | -0.76 / -1.95 | `cs_first_high20(sigmoid(day_es_ratio_lo(Close)), sub(day_quantile_q25(Amt), day_argmax(Open)))` |
| +1.02 | 0.000 | 28 | -1.02 / -2.04 | `day_argmax(Open)` |
| +0.95 | 0.018 | 8 | -1.00 / -1.95 | `day_centroid(in_slice(Ret, 1, 240))` |
| +0.90 | 0.012 | 13 | -1.07 / -1.97 | `day_quantile_q25(Amt)` |
| +0.90 | 0.085 | 5 | -1.04 / -1.94 | `sub(day_quantile_q25(Vwap), day_argmax(Open))` |
| +0.87 | 0.060 | 6 | -1.07 / -1.94 | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), day_sum(Ret), 241)` |
| +0.68 | 0.076 | 10 | -1.27 / -1.95 | `sub(day_quantile_q25(Amt), day_argmax(Open))` |
| +0.64 | 0.020 | 14 | -1.32 / -1.96 | `day_centroid(Amt)` |
| +0.49 | 0.069 | 11 | -1.45 / -1.94 | `day_centroid(abs_(abs_(in_slice(Ret, 1, 240))))` |
| +0.49 | 0.025 | 28 | -1.49 / -1.98 | `day_sum(Ret)` |
| +0.23 | 0.231 | 12 | -1.70 / -1.93 | `cross_tail_mean_q25(day_skew(Open), 60)` |
| +0.07 | 0.324 | 39 | -1.86 / -1.93 | `day_centroid(abs_(in_slice(Ret, 1, 240)))` |

## 拆解(42 次评估)

### head score +0.79:`cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)` | -2.97 | -2.97 | -2.70 | — | (子树本身) |
| sufficiency | `cs_demean(day_centroid(in_slice(Amt, 1, 240)))` | -2.70 | -2.61 | -2.70 | — | (子树本身) |
| sufficiency | `sigmoid(sigmoid(day_es_ratio_lo(Close)))` | -2.75 | -2.75 | -2.60 | — | (子树本身) |
| sufficiency | `day_centroid(in_slice(Amt, 1, 240))` | -2.70 | -2.61 | -2.70 | — | (子树本身) |
| knockout | `cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)` | +0.22 | +0.22 | +0.68 | +0.57 | `cross_regbeta(cs_demean(day_centroid(in_slice(Amt, 1, 240))), sigmoid(sigmoid(day_es_ratio_lo(Close))), 241)` |
| knockout | `cs_demean(day_centroid(in_slice(Amt, 1, 240)))` | +0.50 | +0.50 | +0.53 | +0.29 | `cross_regbeta(cross_delay(day_centroid(in_slice(Amt, 1, 240)), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 241)` |
| knockout | `sigmoid(sigmoid(day_es_ratio_lo(Close)))` | +0.78 | +0.78 | +0.86 | +0.00 | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(day_es_ratio_lo(Close)), 241)` |
| swap | `Amt->Volume` | +0.74 | +0.74 | +0.90 | — | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Volume, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 241)` |
| swap | `Close->Vwap` | +0.60 | +0.60 | +1.03 | — | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Vwap))), 241)` |
| window | `cross_regbeta@241->120` | +0.23 | +0.23 | +0.36 | — | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 120)` |
| window | `cross_regbeta@241->482` | -0.09 | -0.09 | +0.31 | — | `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 482)` |

### head score +0.59:`cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1)` | -2.84 | -2.84 | -2.64 | — | (子树本身) |
| sufficiency | `cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1))` | -2.97 | -2.97 | -2.70 | — | (子树本身) |
| sufficiency | `cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)` | -2.97 | -2.97 | -2.70 | — | (子树本身) |
| sufficiency | `cs_demean(day_centroid(in_slice(Amt, 1, 240)))` | -2.70 | -2.61 | -2.70 | — | (子树本身) |
| knockout | `cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1)` | +0.78 | +0.78 | +0.89 | -0.19 | `cross_regbeta(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), sigmoid(day_es_ratio_lo(Close)), 241)` |
| knockout | `cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1))` | +0.60 | +0.60 | +0.88 | -0.02 | `cross_regbeta(cross_delay(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), 1), sigmoid(day_es_ratio_lo(Close)), 241)` |
| knockout | `cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)` | +0.78 | +0.78 | +0.86 | -0.19 | `cross_regbeta(cross_delay(cs_demean(cs_demean(day_centroid(in_slice(Amt, 1, 240)))), 1), sigmoid(day_es_ratio_lo(Close)), 241)` |
| knockout | `cs_demean(day_centroid(in_slice(Amt, 1, 240)))` | +0.60 | +0.60 | +0.89 | -0.01 | `cross_regbeta(cross_delay(cs_demean(cross_delay(day_centroid(in_slice(Amt, 1, 240)), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 241)` |
| swap | `Amt->Volume` | +0.72 | +0.72 | +1.02 | — | `cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Volume, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 241)` |
| swap | `Close->Vwap` | +0.50 | +0.50 | +0.79 | — | `cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Vwap)), 241)` |
| window | `cross_regbeta@241->120` | -0.20 | -0.20 | +0.26 | — | `cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 120)` |
| window | `cross_regbeta@241->482` | +0.08 | +0.08 | +1.00 | — | `cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 482)` |

### head score -1.02:`cs_bucket_zscore(cross_mean(abs_(day_skew(Open)), 241), LogFloatCap)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(abs_(day_skew(Open)), 241)` | -1.50 | -1.01 | -1.50 | — | (子树本身) |
| sufficiency | `abs_(day_skew(Open))` | -3.08 | -3.08 | -3.08 | — | (子树本身) |
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| knockout | `cross_mean(abs_(day_skew(Open)), 241)` | -2.76 | -2.76 | -2.74 | +1.75 | `cs_bucket_zscore(abs_(day_skew(Open)), LogFloatCap)` |
| knockout | `abs_(day_skew(Open))` | -2.74 | -2.74 | -1.36 | +1.73 | `cs_bucket_zscore(cross_mean(day_skew(Open), 241), LogFloatCap)` |
| swap | `Open->Close` | -0.95 | -0.95 | -0.33 | — | `cs_bucket_zscore(cross_mean(abs_(day_skew(Close)), 241), LogFloatCap)` |
| window | `cross_mean@241->120` | -1.26 | -1.26 | -1.19 | — | `cs_bucket_zscore(cross_mean(abs_(day_skew(Open)), 120), LogFloatCap)` |
| window | `cross_mean@241->482` | -1.61 | -1.61 | -0.43 | — | `cs_bucket_zscore(cross_mean(abs_(day_skew(Open)), 482), LogFloatCap)` |

### head score -1.45:`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60)` | -1.45 | -0.77 | -1.45 | — | (子树本身) |
| sufficiency | `sigmoid(day_argmin(Vwap))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_mask_top_replace_mean_neg(day_durbin_watson(Amt))` | -4.31 | -4.31 | -3.30 | — | (子树本身) |
| sufficiency | `day_argmin(Vwap)` | — | — | — | — | 门槛废品 |
| knockout | `ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60)` | — | — | — | — | `pow_05(sigmoid(day_argmin(Vwap)))` |
| knockout | `sigmoid(day_argmin(Vwap))` | -1.75 | -0.67 | -1.75 | +0.30 | `pow_05(ts_cov(day_argmin(Vwap), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))` |
| knockout | `cs_mask_top_replace_mean_neg(day_durbin_watson(Amt))` | -1.13 | -0.51 | -1.13 | -0.32 | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), day_durbin_watson(Amt), 60))` |
| swap | `Vwap->Close` | -1.20 | -0.58 | -1.20 | — | `pow_05(ts_cov(sigmoid(day_argmin(Close)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))` |
| swap | `Amt->Volume` | -1.40 | -0.84 | -1.40 | — | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Volume)), 60))` |
| window | `ts_cov@60->30` | -1.91 | -1.06 | -1.91 | — | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30))` |
| window | `ts_cov@60->120` | -0.87 | -0.70 | -0.87 | — | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 120))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_topw_mean(pow_2_5(Volume), cross_semistd_neg(Vwap, 10))` — enrichment,均值差 +2.06,p 0.000
2. `day_es_ratio_lo(Close)` — enrichment,均值差 +1.68,p 0.000
3. `sigmoid(day_es_ratio_lo(Close))` — enrichment,均值差 +1.59,p 0.000
4. `cross_delta(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 3)` — enrichment,均值差 +1.54,p 0.010
5. `day_centroid(in_slice(Amt, 1, 240))` — enrichment,均值差 +1.31,p 0.000
6. `cs_demean(day_centroid(in_slice(Amt, 1, 240)))` — enrichment,均值差 +1.27,p 0.000
7. `day_quantile_q25(Vwap)` — enrichment,均值差 +1.26,p 0.002
8. `cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)` — enrichment,均值差 +1.21,p 0.000
9. `cs_first_high20(sigmoid(day_es_ratio_lo(Close)), sub(day_quantile_q25(Amt), day_argmax(Open)))` — enrichment,均值差 +1.19,p 0.043
10. `day_argmax(Open)` — enrichment,均值差 +1.02,p 0.000
11. `day_centroid(in_slice(Ret, 1, 240))` — enrichment,均值差 +0.95,p 0.018
12. `day_quantile_q25(Amt)` — enrichment,均值差 +0.90,p 0.012
13. `sub(day_quantile_q25(Vwap), day_argmax(Open))` — enrichment,均值差 +0.90,p 0.085
14. `cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), day_sum(Ret), 241)` — enrichment,均值差 +0.87,p 0.060
15. `sub(day_quantile_q25(Amt), day_argmax(Open))` — enrichment,均值差 +0.68,p 0.076
16. `day_centroid(Amt)` — enrichment,均值差 +0.64,p 0.020
17. `day_centroid(abs_(abs_(in_slice(Ret, 1, 240))))` — enrichment,均值差 +0.49,p 0.069
18. `day_sum(Ret)` — enrichment,均值差 +0.49,p 0.025

## 本组之前各轮的任务

- `prods2020Pr1a_Ea`:核心 `day_skew(Open)`;评分 70,过线 0,入 heads 0;采样计数 {'c05_no_core': 960, 'c05_skeleton': 477}
  - score -0.12(train -0.12 valid +0.31):`cross_corr(day_skew(Open), day_centroid(Amt), 241)`
  - score -0.29(train -0.29 valid -0.25):`cross_corr(day_skew(Open), day_centroid(Ret), 60)`
  - score -0.30(train +0.10 valid -0.30):`cross_corr(cross_tail_mean_q25(day_skew(Open), 5), day_centroid(Amt), 60)`
  - score -0.46(train -0.46 valid -0.43):`cross_corr(cross_tail_mean_q25(day_skew(Open), 60), day_centroid(Volume), 60)`
  - score -0.58(train -0.40 valid -0.58):`cross_corr(cross_tail_mean_q25(day_skew(Open), 60), day_centroid(Amt), 60)`
- `prods2020Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.10(train +0.10 valid +0.38):`cross_corr(day_centroid(abs_(abs_(in_slice(Ret, 1, 240)))), day_centroid(in_slice(Amt, 1, 240)), 241)`
  - score -0.82(train -0.09 valid -0.82):`cross_corr(day_centroid(abs_(in_slice(Ret, 1, 240))), day_centroid(in_slice(Amt, 1, 240)), 60)`
  - score -0.82(train -0.09 valid -0.82):`cross_corr(day_centroid(abs_(abs_(in_slice(Ret, 1, 240)))), day_centroid(in_slice(Amt, 1, 240)), 60)`
  - score -0.82(train -0.09 valid -0.82):`cross_corr(day_centroid(abs_(abs_(abs_(in_slice(Ret, 1, 240))))), day_centroid(in_slice(Amt, 1, 240)), 60)`
  - score -0.82(train -0.09 valid -0.82):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(in_slice(Amt, 1, 240)), 60)`
- `prods2020Pr2a_Na`:核心 `—`;评分 67,过线 0,入 heads 0;采样计数 {}
  - score +0.12(train +0.12 valid +0.52):`cross_regbeta(day_centroid(in_slice(Amt, 1, 240)), day_centroid(abs_(in_slice(Ret, 1, 240))), 241)`
  - score +0.12(train +0.12 valid +0.52):`cross_regbeta(day_centroid(in_slice(Amt, 1, 240)), day_centroid(in_slice(Ret, 1, 240)), 241)`
  - score +0.12(train +0.12 valid +0.52):`cross_regbeta(day_centroid(in_slice(Amt, 1, 240)), day_centroid(abs_(abs_(in_slice(Ret, 1, 240)))), 241)`
  - score +0.12(train +0.12 valid +0.52):`cross_regbeta(day_centroid(in_slice(Amt, 1, 240)), day_centroid(abs_(abs_(abs_(in_slice(Ret, 1, 240))))), 241)`
  - score +0.10(train +0.10 valid +0.38):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(in_slice(Amt, 1, 240)), 241)`
- `prods2020Pr2b_Nb`:核心 `—`;评分 97,过线 4,入 heads 2;采样计数 {'c05_skeleton': 2}
  - score +0.79(train +0.79 valid +0.88):`cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(sigmoid(day_es_ratio_lo(Close))), 241)`
  - score +0.78(train +0.78 valid +0.87):`cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), day_es_ratio_lo(Close), 241)`
  - score +0.78(train +0.78 valid +0.86):`cross_regbeta(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1), sigmoid(day_es_ratio_lo(Close)), 241)`
  - score +0.59(train +0.59 valid +0.89):`cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Amt, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 241)`
  - score +0.46(train +0.46 valid +0.86):`cross_regbeta(cross_delay(cs_rank(day_centroid(in_slice(Amt, 1, 240))), 1), day_es_ratio_lo(Close), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.58(window ts_cov@60->120):`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 120))`
- 增益 +0.32(knockout cs_mask_top_replace_mean_neg(day_durbin_watson(Amt))):`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), day_durbin_watson(Amt), 60))`
- 增益 +0.26(swap Vwap->Close):`pow_05(ts_cov(sigmoid(day_argmin(Close)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))`
- 增益 +0.14(swap Amt->Volume):`cross_regbeta(cross_delay(cs_demean(cross_delay(cs_demean(day_centroid(in_slice(Volume, 1, 240))), 1)), 1), sigmoid(day_es_ratio_lo(Close)), 241)`
