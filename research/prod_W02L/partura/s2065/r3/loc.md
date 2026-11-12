# 定位:种子 2065,P 组,第 3 轮(只含 train / valid)

快照:prods2065M1_I0_open_search, prods2065M2_I0_open_search, prods2065M3_I0_open_search, prods2065Pr1a_Na, prods2065Pr1b_Nb, prods2065Pr2a_Ea, prods2065Pr2b_Eb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.52 | -1.52 | -1.13 | +1 | 20 | prods2065M1_I0_open_search | `day_q_stat_std(in_max_rolling(Amt, 60))` |
| -1.54 | -1.54 | -1.15 | +1 | 20 | prods2065M1_I0_open_search | `day_q_stat_std(in_max_rolling(Volume, 60))` |
| -1.56 | -1.36 | -1.56 | -1 | 5 | prods2065M2_I0_open_search | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| -1.60 | -1.30 | -1.60 | -1 | 20 | prods2065M2_I0_open_search | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |
| -1.64 | -1.07 | -1.64 | -1 | 5 | prods2065M2_I0_open_search | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| -2.35 | -1.64 | -2.35 | -1 | 20 | prods2065M1_I0_open_search | `day_var(in_max_rolling(Vwap, 60))` |
| -2.36 | -2.36 | -0.72 | +1 | 20 | prods2065M3_I0_open_search | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap, 10))` |
| -2.39 | -1.57 | -2.39 | -1 | 5 | prods2065M3_I0_open_search | `day_last(sliding_bottom_mean_masked_p5(Close, Vwap, 10))` |
| -2.60 | -2.60 | -1.60 | +1 | 0 | prods2065M3_I0_open_search | `cross_sum(day_kurt(sliding_bottom_mean_masked_p5(Close, Volume, 10)), 30)` |

## 共性:179 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.81 | 0.002 | 5 | -0.46 / -2.27 | `pow_05(day_mean(Close))` |
| +1.63 | 0.000 | 28 | -0.84 / -2.48 | `day_cov(Vwap, Low)` |
| +1.63 | 0.000 | 26 | -0.83 / -2.46 | `day_wmean(Low, Close)` |
| +1.57 | 0.002 | 6 | -0.70 / -2.27 | `day_quantile_q25(Low)` |
| +1.53 | 0.000 | 30 | -0.94 / -2.48 | `pow_2(day_mean(Close))` |
| +1.52 | 0.000 | 61 | -1.22 / -2.74 | `day_mean(Close)` |
| +1.49 | 0.007 | 5 | -0.77 / -2.26 | `cross_quantile_q25(day_quantile_q25(Low), 60)` |
| +1.47 | 0.000 | 23 | -0.94 / -2.41 | `cs_first_high40(day_cov(Vwap, Low), pow_2(day_mean(Close)))` |
| +1.46 | 0.006 | 5 | -0.80 / -2.26 | `cross_quantile_q25(pow_1_5(day_mean(Close)), 60)` |
| +1.44 | 0.003 | 7 | -0.84 / -2.28 | `mul(day_wmean(Low, Close), cross_quantile_q25(pow_2(day_mean(Close)), 60))` |
| +1.39 | 0.019 | 4 | -0.86 / -2.25 | `mul(day_wmean(Low, Close), cross_quantile_q25(day_quantile_q25(Low), 60))` |
| +1.31 | 0.023 | 4 | -0.94 / -2.25 | `mul(day_wmean(Low, Close), cross_quantile_q25(pow_1_5(day_mean(Close)), 60))` |
| +1.26 | 0.000 | 13 | -1.05 / -2.31 | `cross_quantile_q25(pow_2(day_mean(Close)), 60)` |
| +1.20 | 0.010 | 7 | -1.07 / -2.27 | `pow_1_5(day_mean(Close))` |
| +0.83 | 0.098 | 5 | -1.41 / -2.24 | `cs_first_high40(day_cov(Close, Low), pow_1_5(day_mean(Close)))` |
| +0.71 | 0.072 | 6 | -1.54 / -2.24 | `day_close(Low)` |
| +0.59 | 0.197 | 6 | -1.65 / -2.24 | `day_cov(Close, Low)` |
| +0.38 | 0.219 | 5 | -1.85 / -2.23 | `cross_mean(day_mean(Close), 500)` |
| +0.29 | 0.219 | 12 | -1.95 / -2.24 | `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))` |
| +0.29 | 0.219 | 12 | -1.95 / -2.24 | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` |

## 拆解(13 次评估)

### head score -2.36:`day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap, 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Close->Vwap` | -1.91 | -1.91 | -0.68 | — | `day_durbin_watson(sliding_bottom_mean_masked_p5(Vwap, Vwap, 10))` |
| swap | `Vwap->Close` | -4.43 | -3.87 | -4.43 | — | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Close, 10))` |
| window | `sliding_bottom_mean_masked_p5@10->5` | -3.99 | -3.99 | -2.52 | — | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap, 5))` |
| window | `sliding_bottom_mean_masked_p5@10->20` | -2.09 | -2.09 | -0.78 | — | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap, 20))` |

### head score -2.39:`day_last(sliding_bottom_mean_masked_p5(Close, Vwap, 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Close->Vwap` | -2.37 | -1.59 | -2.37 | — | `day_last(sliding_bottom_mean_masked_p5(Vwap, Vwap, 10))` |
| swap | `Vwap->Close` | -2.35 | -1.57 | -2.35 | — | `day_last(sliding_bottom_mean_masked_p5(Close, Close, 10))` |
| window | `sliding_bottom_mean_masked_p5@10->5` | -2.38 | -1.56 | -2.38 | — | `day_last(sliding_bottom_mean_masked_p5(Close, Vwap, 5))` |
| window | `sliding_bottom_mean_masked_p5@10->20` | -2.28 | -1.56 | -2.28 | — | `day_last(sliding_bottom_mean_masked_p5(Close, Vwap, 20))` |

### head score -2.60:`cross_sum(day_kurt(sliding_bottom_mean_masked_p5(Close, Volume, 10)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(sliding_bottom_mean_masked_p5(Close, Volume, 10))` | -3.35 | -3.35 | -2.39 | — | (子树本身) |
| swap | `Close->Vwap` | -2.81 | -2.81 | -2.58 | — | `cross_sum(day_kurt(sliding_bottom_mean_masked_p5(Vwap, Volume, 10)), 30)` |
| swap | `Volume->Amt` | -2.63 | -2.63 | -1.62 | — | `cross_sum(day_kurt(sliding_bottom_mean_masked_p5(Close, Amt, 10)), 30)` |
| window | `cross_sum@30->15` | -2.73 | -2.73 | -2.23 | — | `cross_sum(day_kurt(sliding_bottom_mean_masked_p5(Close, Volume, 10)), 15)` |
| window | `cross_sum@30->60` | -2.38 | -2.38 | -2.33 | — | `cross_sum(day_kurt(sliding_bottom_mean_masked_p5(Close, Volume, 10)), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_05(day_mean(Close))` — enrichment,均值差 +1.81,p 0.002
2. `day_cov(Vwap, Low)` — enrichment,均值差 +1.63,p 0.000
3. `day_wmean(Low, Close)` — enrichment,均值差 +1.63,p 0.000
4. `day_quantile_q25(Low)` — enrichment,均值差 +1.57,p 0.002
5. `pow_2(day_mean(Close))` — enrichment,均值差 +1.53,p 0.000
6. `day_mean(Close)` — enrichment,均值差 +1.52,p 0.000
7. `cross_quantile_q25(day_quantile_q25(Low), 60)` — enrichment,均值差 +1.49,p 0.007
8. `cs_first_high40(day_cov(Vwap, Low), pow_2(day_mean(Close)))` — enrichment,均值差 +1.47,p 0.000
9. `cross_quantile_q25(pow_1_5(day_mean(Close)), 60)` — enrichment,均值差 +1.46,p 0.006
10. `mul(day_wmean(Low, Close), cross_quantile_q25(pow_2(day_mean(Close)), 60))` — enrichment,均值差 +1.44,p 0.003
11. `mul(day_wmean(Low, Close), cross_quantile_q25(day_quantile_q25(Low), 60))` — enrichment,均值差 +1.39,p 0.019
12. `mul(day_wmean(Low, Close), cross_quantile_q25(pow_1_5(day_mean(Close)), 60))` — enrichment,均值差 +1.31,p 0.023
13. `cross_quantile_q25(pow_2(day_mean(Close)), 60)` — enrichment,均值差 +1.26,p 0.000
14. `pow_1_5(day_mean(Close))` — enrichment,均值差 +1.20,p 0.010
15. `cs_first_high40(day_cov(Close, Low), pow_1_5(day_mean(Close)))` — enrichment,均值差 +0.83,p 0.098
16. `day_close(Low)` — enrichment,均值差 +0.71,p 0.072

## 本组之前各轮的任务

- `prods2065Pr1a_Na`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.42(train -0.42 valid -0.40):`cs_last_low10(inv(day_q_stat_std(Open)), pow_05(pow_05(day_mean(Close))))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(inv(day_q_stat_std(Close)), signedpower(day_mean(Close)))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(inv(day_q_stat_std(Close)), day_mean(Close))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(inv(day_q_stat_std(Close)), pow_05(pow_05(day_mean(Close))))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(cs_last_low10(inv(day_q_stat_std(Close)), pow_05(day_mean(Close))), day_mean(Close))`
- `prods2065Pr1b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.03(train -0.91 valid -1.03):`mul(day_max(Low), signedpower(mul(day_max(Low), signedpower(day_flat_ratio(Close)))))`
  - score -1.05(train -0.89 valid -1.05):`mul(day_close(Low), signedpower(mul(day_close(Low), signedpower(day_flat_ratio(Close)))))`
  - score -1.27(train -1.20 valid -1.27):`mul(day_close(Low), signedpower(day_flat_ratio(Low)))`
  - score -1.27(train -1.27 valid -1.04):`mul(day_close(Low), signedpower(day_flat_ratio(Close)))`
  - score -1.38(train -1.38 valid -0.92):`mul(day_close(Low), pow_2_5(day_flat_ratio(Low)))`
- `prods2065Pr2a_Ea`:核心 `day_mean(Close)`;评分 101,过线 0,入 heads 0;采样计数 {'c05_no_core': 1508, 'c05_skeleton': 687}
  - score -0.10(train -0.10 valid -0.09):`cs_bucket_zscore(mul(mul(day_wmean(Low, Close), cross_quantile_q25(day_mean(Close), 60)), cross_quantile_q25(day_mean(Close), 60)), cs_first_high40(day_cov(Vwap, Low), day_mean(Close)))`
  - score -0.10(train -0.10 valid -0.09):`cs_bucket_zscore(mul(day_wmean(Low, Close), cross_quantile_q25(pow_2(day_mean(Close)), 60)), cs_first_high40(day_cov(Vwap, Low), pow_2(day_mean(Close))))`
  - score -0.11(train -0.11 valid -0.09):`cs_bucket_zscore(mul(day_wmean(Close, Close), cross_quantile_q25(pow_2(day_mean(Close)), 60)), cs_first_high40(day_cov(Vwap, Low), pow_2(day_mean(Close))))`
  - score -0.16(train -0.16 valid -0.07):`cs_bucket_zscore(mul(day_wmean(Low, Close), cross_quantile_q25(pow_2(day_mean(Close)), 60)), cross_quantile_q25(pow_2(day_mean(Close)), 60))`
  - score -0.17(train -0.17 valid -0.05):`cs_bucket_zscore(mul(day_wmean(Low, Close), cross_quantile_q25(pow_2(pow_1_5(day_mean(Close))), 60)), cs_first_high40(day_cov(Vwap, Low), pow_2(pow_1_5(day_mean(Close)))))`
- `prods2065Pr2b_Eb`:核心 `inv(day_q_stat_std(Close))`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 2085, 'c05_skeleton': 1028, 'c05_periphery_seen': 4}
  - score -1.05(train -1.05 valid -0.95):`cross_cov(inv(day_q_stat_std(Close)), inv(day_q_stat_std(Close)), 241)`
  - score -1.07(train -1.07 valid -0.94):`cross_corr(inv(day_q_stat_std(Close)), inv(day_q_stat_std(Close)), 241)`
  - score -1.09(train -1.09 valid -0.90):`cross_reg_fvalue(day_q_stat_std(Close), inv(day_q_stat_std(Close)), 241)`
  - score -1.19(train -1.19 valid -1.00):`cross_corr(day_q_stat_std(Close), inv(day_q_stat_std(Close)), 241)`
  - score -1.19(train -1.19 valid -1.00):`cross_corr(inv(day_q_stat_std(Close)), day_q_stat_std(Close), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.45(swap Close->Vwap):`day_durbin_watson(sliding_bottom_mean_masked_p5(Vwap, Vwap, 10))`
- 增益 +0.27(window sliding_bottom_mean_masked_p5@10->20):`day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Vwap, 20))`
- 增益 +0.10(window sliding_bottom_mean_masked_p5@10->20):`day_last(sliding_bottom_mean_masked_p5(Close, Vwap, 20))`
