# 定位:种子 2062,P 组,第 3 轮(只含 train / valid)

快照:prods2062M1_I0_open_search, prods2062M2_I0_open_search, prods2062M3_I0_open_search, prods2062Pr1a_I0_open_search, prods2062Pr1b_Nb, prods2062Pr2a_I0_open_search, prods2062Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.74 | -1.35 | -1.74 | -1 | 20 | prods2062M1_I0_open_search | `ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)` |
| -2.69 | -1.92 | -2.69 | +1 | 5 | prods2062M3_I0_open_search | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap)))), 30)` |
| -2.75 | -2.75 | -2.05 | +1 | 20 | prods2062M3_I0_open_search | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 3)` |
| -2.89 | -2.89 | -2.75 | +1 | 5 | prods2062M3_I0_open_search | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5), 5), 5)` |
| -3.34 | -3.34 | -2.86 | -1 | 20 | prods2062M2_I0_open_search | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False), 20)` |
| -3.34 | -3.34 | -2.86 | -1 | 20 | prods2062M2_I0_open_search | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'), 20)` |
| -3.63 | -3.63 | -3.13 | -1 | 20 | prods2062M2_I0_open_search | `day_pdf_tail_sum_m(Ret, Volume, 50, False)` |
| -3.86 | -2.54 | -3.86 | -1 | 20 | prods2062M1_I0_open_search | `ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)` |
| -4.22 | -4.22 | -2.85 | -1 | 20 | prods2062M1_I0_open_search | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0), True)` |

## 共性:226 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.71 | 0.001 | 7 | -1.04 / -2.76 | `day_median(Amt)` |
| +1.65 | 0.009 | 4 | -1.09 / -2.73 | `cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30)` |
| +1.62 | 0.000 | 10 | -1.15 / -2.78 | `cross_sum(day_sum(Ret), 241)` |
| +1.57 | 0.002 | 6 | -1.18 / -2.75 | `day_flat_run_max(Open)` |
| +1.57 | 0.002 | 6 | -1.18 / -2.75 | `ts_stddev(day_flat_run_max(Open), 20)` |
| +1.32 | 0.000 | 21 | -1.50 / -2.83 | `day_at_max_ratio(Vwap)` |
| +1.26 | 0.000 | 20 | -1.56 / -2.82 | `inv(day_at_max_ratio(Vwap))` |
| +1.16 | 0.002 | 9 | -1.59 / -2.75 | `ts_stddev(day_autocorr_n1(Ret), 20)` |
| +1.12 | 0.000 | 15 | -1.66 / -2.78 | `day_median(Low)` |
| +1.08 | 0.002 | 10 | -1.67 / -2.75 | `day_autocorr_n1(Ret)` |
| +1.03 | 0.000 | 24 | -1.78 / -2.81 | `day_sum(Ret)` |
| +1.02 | 0.045 | 4 | -1.71 / -2.72 | `cross_corr(day_cov(High, Volume), day_quantile_q25(Amt), 5)` |
| +0.94 | 0.002 | 16 | -1.84 / -2.77 | `day_quantile_q25(Amt)` |
| +0.87 | 0.011 | 12 | -1.88 / -2.75 | `ts_min(LogFloatShares, 20)` |
| +0.85 | 0.015 | 10 | -1.89 / -2.74 | `day_cov(High, Volume)` |
| +0.81 | 0.081 | 6 | -1.92 / -2.73 | `day_min(cross_scale(Ret, 3))` |
| +0.79 | 0.075 | 6 | -1.94 / -2.73 | `day_at_max_ratio(Open)` |
| +0.77 | 0.102 | 5 | -1.96 / -2.72 | `cross_sum(day_at_max_ratio(Open), 241)` |
| +0.64 | 0.195 | 4 | -2.08 / -2.72 | `day_wmean(Ret, Close)` |
| +0.62 | 0.170 | 5 | -2.10 / -2.72 | `day_at_min_ratio(Amt)` |

## 拆解(26 次评估)

### head score -2.69:`ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap)))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap))))` | -3.10 | -2.77 | -3.10 | — | (子树本身) |
| sufficiency | `pow_05(sigmoid(day_ar1_coefficient(Vwap)))` | -3.10 | -2.76 | -3.10 | — | (子树本身) |
| sufficiency | `sigmoid(day_ar1_coefficient(Vwap))` | -3.10 | -2.76 | -3.10 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Vwap)` | -3.09 | -2.76 | -3.09 | — | (子树本身) |
| knockout | `sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap))))` | -2.71 | -1.94 | -2.71 | +0.03 | `ts_decay_linear(pow_05(sigmoid(day_ar1_coefficient(Vwap))), 30)` |
| knockout | `pow_05(sigmoid(day_ar1_coefficient(Vwap)))` | -2.73 | -1.94 | -2.73 | +0.04 | `ts_decay_linear(sigmoid(sigmoid(day_ar1_coefficient(Vwap))), 30)` |
| knockout | `sigmoid(day_ar1_coefficient(Vwap))` | -2.68 | -1.93 | -2.68 | -0.00 | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Vwap))), 30)` |
| swap | `Vwap->Close` | -2.82 | -1.88 | -2.82 | — | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Close)))), 30)` |
| window | `ts_decay_linear@30->15` | -2.19 | -2.10 | -2.19 | — | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap)))), 15)` |
| window | `ts_decay_linear@30->60` | -2.19 | -2.19 | -2.16 | — | `ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap)))), 60)` |

### head score -2.75:`cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(sigmoid(day_ar1_coefficient(Low)))` | -2.88 | -2.88 | -2.70 | — | (子树本身) |
| sufficiency | `sigmoid(day_ar1_coefficient(Low))` | -2.89 | -2.89 | -2.69 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Low)` | -2.89 | -2.89 | -2.69 | — | (子树本身) |
| knockout | `sigmoid(sigmoid(day_ar1_coefficient(Low)))` | -2.75 | -2.75 | -2.10 | -0.01 | `cross_mean(sigmoid(day_ar1_coefficient(Low)), 3)` |
| swap | `Low->High` | -2.37 | -2.37 | -2.13 | — | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(High))), 3)` |
| window | `cross_mean@3->2` | -2.96 | -2.96 | -2.27 | — | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 2)` |
| window | `cross_mean@3->6` | -2.62 | -2.62 | -2.01 | — | `cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 6)` |

### head score -2.89:`ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5), 5), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5), 5)` | -3.46 | -3.02 | -3.46 | — | (子树本身) |
| sufficiency | `ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5)` | -3.32 | -2.86 | -3.32 | — | (子树本身) |
| sufficiency | `sigmoid(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5)` | -2.76 | -2.76 | -2.61 | -0.13 | `ts_min(ts_min(sigmoid(day_ar1_coefficient(Volume)), 5), 5)` |
| knockout | `sigmoid(day_ar1_coefficient(Volume))` | -2.93 | -2.93 | -2.69 | +0.04 | `ts_min(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5), 5)` |
| swap | `Volume->Amt` | -2.92 | -2.92 | -2.67 | — | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Amt)), 5), 5), 5)` |
| window | `ts_min@5->2` | -3.32 | -3.15 | -3.32 | — | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5), 5), 2)` |
| window | `ts_min@5->10` | -3.11 | -3.11 | -3.02 | — | `ts_min(ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5), 5), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_median(Amt)` — enrichment,均值差 +1.71,p 0.001
2. `cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30)` — enrichment,均值差 +1.65,p 0.009
3. `cross_sum(day_sum(Ret), 241)` — enrichment,均值差 +1.62,p 0.000
4. `day_flat_run_max(Open)` — enrichment,均值差 +1.57,p 0.002
5. `ts_stddev(day_flat_run_max(Open), 20)` — enrichment,均值差 +1.57,p 0.002
6. `day_at_max_ratio(Vwap)` — enrichment,均值差 +1.32,p 0.000
7. `inv(day_at_max_ratio(Vwap))` — enrichment,均值差 +1.26,p 0.000
8. `ts_stddev(day_autocorr_n1(Ret), 20)` — enrichment,均值差 +1.16,p 0.002
9. `day_median(Low)` — enrichment,均值差 +1.12,p 0.000
10. `day_autocorr_n1(Ret)` — enrichment,均值差 +1.08,p 0.002
11. `day_sum(Ret)` — enrichment,均值差 +1.03,p 0.000
12. `cross_corr(day_cov(High, Volume), day_quantile_q25(Amt), 5)` — enrichment,均值差 +1.02,p 0.045
13. `day_quantile_q25(Amt)` — enrichment,均值差 +0.94,p 0.002
14. `ts_min(LogFloatShares, 20)` — enrichment,均值差 +0.87,p 0.011
15. `day_cov(High, Volume)` — enrichment,均值差 +0.85,p 0.015
16. `day_min(cross_scale(Ret, 3))` — enrichment,均值差 +0.81,p 0.081
17. `day_at_max_ratio(Open)` — enrichment,均值差 +0.79,p 0.075
18. `day_gini(Amt)` — enrichment,均值差 +0.53,p 0.032

## 本组之前各轮的任务

- `prods2062Pr1a_I0_open_search`:核心 `—`;评分 98,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.32(train +0.32 valid +0.54):`cross_regbeta(day_median(Amt), inv(cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30)), 241)`
  - score +0.14(train +0.14 valid +0.39):`cross_regbeta(day_median(Amt), cross_regbeta(day_median(Amt), LogFloatShares, 241), 241)`
  - score -0.49(train +0.22 valid -0.49):`cross_regbeta(day_median(Amt), day_at_max_ratio(Vwap), 241)`
  - score -0.52(train -0.52 valid +0.04):`pow_05(cross_regalpha(inv(day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap), 60))`
  - score -0.87(train -0.87 valid -0.65):`inv(cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30))`
- `prods2062Pr1b_Nb`:核心 `—`;评分 57,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -1.51(train -1.51 valid -1.39):`add(day_min(cross_scale(Ret, 5)), day_min(cross_scale(Ret, 3)))`
  - score -1.69(train -1.54 valid -1.69):`add(day_min(cross_scale(Ret, 5)), day_wmean(Ret, Close))`
  - score -1.70(train -1.53 valid -1.70):`add(day_min(cross_scale(Ret, 5)), day_quantile(Ret))`
  - score -1.86(train -1.86 valid -1.37):`add(day_min(cross_scale(Ret, 3)), day_quantile(Vwap))`
  - score -1.94(train -1.94 valid -1.73):`add(day_min(cross_scale(Ret, 10)), day_quantile(Vwap))`
- `prods2062Pr2a_I0_open_search`:核心 `—`;评分 79,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -1.30(train -1.30 valid -0.91):`log(cross_tail_mean_q25(cs_last_high20(day_skew(Volume), day_mean(Close)), 5))`
  - score -1.30(train -1.30 valid -0.91):`log(log(cross_tail_mean_q25(cs_last_high20(day_skew(Volume), day_mean(Close)), 5)))`
  - score -1.32(train -1.32 valid -0.93):`log(cross_tail_mean_q25(cs_last_high20(day_skew(Volume), day_mean(Close)), 10))`
  - score -1.32(train -1.32 valid -0.93):`log(log(cross_tail_mean_q25(cs_last_high20(day_skew(Volume), day_mean(Close)), 10)))`
  - score -1.38(train -1.38 valid -0.97):`log(cross_tail_mean_q25(cross_tail_mean_q25(cs_last_high20(day_skew(Volume), day_mean(Close)), 5), 5))`
- `prods2062Pr2b_Nb`:核心 `—`;评分 100,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.59(train -0.59 valid -0.15):`div(cross_sum(day_sum(Ret), 241), day_median(Low))`
  - score -0.80(train -0.80 valid -0.59):`div(cross_sum(day_sum(Ret), 241), cs_mean(div(cross_sum(day_sum(Ret), 241), day_median(Low))))`
  - score -0.82(train -0.82 valid -0.11):`div(cross_sum(day_sum(Ret), 241), cs_rank(day_cov(High, Amt)))`
  - score -0.90(train -0.90 valid -0.03):`div(cross_sum(day_sum(Ret), 241), cs_mean(day_median(Low)))`
  - score -0.90(train -0.90 valid -0.03):`div(div(cross_sum(day_sum(Ret), 241), cs_mean(day_cov(High, Amt))), cs_mean(day_cov(High, Amt)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.50(window ts_decay_linear@30->15):`ts_decay_linear(sigmoid(pow_05(sigmoid(day_ar1_coefficient(Vwap)))), 15)`
- 增益 +0.39(swap Low->High):`cross_mean(sigmoid(sigmoid(day_ar1_coefficient(High))), 3)`
- 增益 +0.14(window cross_mean@3->6):`cross_mean(sigmoid(sigmoid(day_ar1_coefficient(Low))), 6)`
