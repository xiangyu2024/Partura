# 定位:种子 2020,P 组,第 2 轮(只含 train / valid)

快照:prods2020M1_I0_open_search, prods2020M2_I0_open_search, prods2020Pr1a_Ea, prods2020Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.12 | -1.12 | -0.86 | +1 | 0 | prods2020M2_I0_open_search | `ts_sum(cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15), 50)` |
| -1.22 | -1.22 | -1.11 | +1 | 5 | prods2020M1_I0_open_search | `cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 30), LogFloatCap)` |
| -1.29 | -1.19 | -1.29 | -1 | 5 | prods2020M2_I0_open_search | `cross_regalpha(day_sum(Volume), day_argmin(Ret), 15)` |
| -1.93 | -1.06 | -1.93 | -1 | 5 | prods2020M2_I0_open_search | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30))` |
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `pow_2(abs_(day_skew(Open)))` |
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `abs_(pow_2(abs_(day_skew(Open))))` |

## 共性:128 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.23 | 0.000 | 14 | -1.32 / -2.54 | `day_centroid(Amt)` |
| +1.03 | 0.001 | 14 | -1.49 / -2.52 | `day_centroid(in_slice(Amt, 1, 240))` |
| +0.93 | 0.018 | 7 | -1.53 / -2.46 | `day_centroid(abs_(abs_(in_slice(Ret, 1, 240))))` |
| +0.79 | 0.011 | 12 | -1.70 / -2.48 | `cross_tail_mean_q25(day_skew(Open), 60)` |
| +0.61 | 0.091 | 4 | -1.82 / -2.43 | `div(day_first(Open), cross_delay(day_last(Close), 1))` |
| +0.60 | 0.027 | 9 | -1.85 / -2.45 | `day_first(Open)` |
| +0.44 | 0.089 | 8 | -2.00 / -2.44 | `day_last(Close)` |
| +0.33 | 0.323 | 4 | -2.10 / -2.42 | `day_argmin(Amt)` |
| +0.26 | 0.220 | 6 | -2.17 / -2.42 | `cross_delay(day_last(Close), 1)` |
| +0.24 | 0.083 | 58 | -2.28 / -2.52 | `day_skew(Open)` |
| +0.08 | 0.424 | 22 | -2.34 / -2.42 | `day_centroid(abs_(in_slice(Ret, 1, 240)))` |
| -0.05 | 0.647 | 4 | -2.46 / -2.41 | `day_hurst(Close)` |
| -0.29 | 0.742 | 4 | -2.69 / -2.40 | `day_centroid(Open)` |
| -0.57 | 0.920 | 4 | -2.96 / -2.39 | `day_argmin(Volume)` |
| -1.84 | 0.999 | 5 | -4.18 / -2.34 | `day_skew(Amt)` |

## 拆解(34 次评估)

### head score -1.12:`ts_sum(cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15)` | -1.52 | -1.52 | -0.79 | — | (子树本身) |
| sufficiency | `ts_regalpha(day_sum(Vwap), day_skew(Volume), 10)` | -2.41 | -2.41 | -1.49 | — | (子树本身) |
| sufficiency | `day_sum(Vwap)` | -1.87 | -1.70 | -1.87 | — | (子树本身) |
| sufficiency | `day_skew(Volume)` | -5.21 | -4.17 | -5.21 | — | (子树本身) |
| knockout | `cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15)` | -1.06 | -1.06 | -0.96 | -0.06 | `ts_sum(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), 50)` |
| knockout | `ts_regalpha(day_sum(Vwap), day_skew(Volume), 10)` | -2.76 | -2.16 | -2.76 | +1.64 | `ts_sum(cross_cov(day_sum(Vwap), day_argmin(Amt), 15), 50)` |
| swap | `Vwap->Close` | -0.77 | -0.77 | -0.51 | — | `ts_sum(cross_cov(ts_regalpha(day_sum(Close), day_skew(Volume), 10), day_argmin(Amt), 15), 50)` |
| swap | `Volume->Amt` | -1.08 | -1.08 | -0.84 | — | `ts_sum(cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Amt), 10), day_argmin(Amt), 15), 50)` |
| window | `ts_sum@50->25` | -1.48 | -1.48 | -0.92 | — | `ts_sum(cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15), 25)` |
| window | `ts_sum@50->100` | -1.23 | -1.23 | -0.73 | — | `ts_sum(cross_cov(ts_regalpha(day_sum(Vwap), day_skew(Volume), 10), day_argmin(Amt), 15), 100)` |

### head score -1.22:`cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 30), LogFloatCap)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_ema(abs_(day_skew(Open)), 30)` | -1.72 | -1.27 | -1.72 | — | (子树本身) |
| sufficiency | `abs_(day_skew(Open))` | -3.08 | -3.08 | -3.08 | — | (子树本身) |
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| knockout | `cross_ema(abs_(day_skew(Open)), 30)` | -2.76 | -2.76 | -2.74 | +1.54 | `cs_bucket_zscore(abs_(day_skew(Open)), LogFloatCap)` |
| knockout | `abs_(day_skew(Open))` | -3.42 | -3.20 | -3.42 | +2.20 | `cs_bucket_zscore(cross_ema(day_skew(Open), 30), LogFloatCap)` |
| swap | `Open->Close` | -1.13 | -1.13 | -0.97 | — | `cs_bucket_zscore(cross_ema(abs_(day_skew(Close)), 30), LogFloatCap)` |
| window | `cross_ema@30->15` | -1.30 | -1.30 | -1.30 | — | `cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 15), LogFloatCap)` |
| window | `cross_ema@30->60` | -1.05 | -1.05 | -0.95 | — | `cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 60), LogFloatCap)` |

### head score -1.29:`cross_regalpha(day_sum(Volume), day_argmin(Ret), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_argmin(Ret)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.44 | -1.12 | -1.44 | — | `cross_regalpha(day_sum(Amt), day_argmin(Ret), 15)` |
| window | `cross_regalpha@15->7` | -2.41 | -1.63 | -2.41 | — | `cross_regalpha(day_sum(Volume), day_argmin(Ret), 7)` |
| window | `cross_regalpha@15->30` | -1.75 | -0.72 | -1.75 | — | `cross_regalpha(day_sum(Volume), day_argmin(Ret), 30)` |

### head score -1.93:`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30)` | -1.91 | -1.06 | -1.91 | — | (子树本身) |
| sufficiency | `sigmoid(day_argmin(Vwap))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_mask_top_replace_mean_neg(day_durbin_watson(Amt))` | -4.31 | -4.31 | -3.30 | — | (子树本身) |
| sufficiency | `day_argmin(Vwap)` | — | — | — | — | 门槛废品 |
| knockout | `ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30)` | — | — | — | — | `pow_05(sigmoid(day_argmin(Vwap)))` |
| knockout | `sigmoid(day_argmin(Vwap))` | -1.51 | -0.38 | -1.51 | -0.42 | `pow_05(ts_cov(day_argmin(Vwap), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30))` |
| knockout | `cs_mask_top_replace_mean_neg(day_durbin_watson(Amt))` | -1.78 | -0.95 | -1.78 | -0.15 | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), day_durbin_watson(Amt), 30))` |
| swap | `Vwap->Close` | -1.64 | -0.73 | -1.64 | — | `pow_05(ts_cov(sigmoid(day_argmin(Close)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30))` |
| swap | `Amt->Volume` | -1.85 | -1.07 | -1.85 | — | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Volume)), 30))` |
| window | `ts_cov@30->15` | -1.74 | -0.89 | -1.74 | — | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 15))` |
| window | `ts_cov@30->60` | -1.45 | -0.77 | -1.45 | — | `pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(Amt)` — enrichment,均值差 +1.23,p 0.000
2. `day_centroid(in_slice(Amt, 1, 240))` — enrichment,均值差 +1.03,p 0.001
3. `day_centroid(abs_(abs_(in_slice(Ret, 1, 240))))` — enrichment,均值差 +0.93,p 0.018
4. `cross_tail_mean_q25(day_skew(Open), 60)` — enrichment,均值差 +0.79,p 0.011
5. `div(day_first(Open), cross_delay(day_last(Close), 1))` — enrichment,均值差 +0.61,p 0.091
6. `day_first(Open)` — enrichment,均值差 +0.60,p 0.027
7. `day_last(Close)` — enrichment,均值差 +0.44,p 0.089
8. `day_skew(Open)` — enrichment,均值差 +0.24,p 0.083

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.48(window ts_cov@30->60):`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 60))`
- 增益 +0.29(swap Vwap->Close):`pow_05(ts_cov(sigmoid(day_argmin(Close)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 30))`
- 增益 +0.19(window ts_cov@30->15):`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), cs_mask_top_replace_mean_neg(day_durbin_watson(Amt)), 15))`
- 增益 +0.17(window cross_ema@30->60):`cs_bucket_zscore(cross_ema(abs_(day_skew(Open)), 60), LogFloatCap)`
- 增益 +0.15(knockout cs_mask_top_replace_mean_neg(day_durbin_watson(Amt))):`pow_05(ts_cov(sigmoid(day_argmin(Vwap)), day_durbin_watson(Amt), 30))`
