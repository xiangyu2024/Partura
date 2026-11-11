# 定位:种子 2047,P 组,第 3 轮(只含 train / valid)

快照:prods2047M1_I0_open_search, prods2047M2_I0_open_search, prods2047M3_I0_open_search, prods2047Pr1a_Na, prods2047Pr1b_Nb, prods2047Pr2a_Ea, prods2047Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.71 | -0.71 | -0.68 | +1 | 5 | prods2047M1_I0_open_search | `cross_corr(day_min(High), day_mean(Amt), 60)` |
| -1.34 | -1.34 | -1.19 | +1 | 20 | prods2047M1_I0_open_search | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` |
| -2.35 | -1.56 | -2.35 | -1 | 20 | prods2047M1_I0_open_search | `add(day_min(Ret), day_var(Open))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M2_I0_open_search | `sqrt(sqrt(sigmoid(day_min(Ret))))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M2_I0_open_search | `sqrt(sigmoid(day_min(Ret)))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M2_I0_open_search | `pow_1_5(pow_2(sqrt(sigmoid(day_min(Ret)))))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M3_I0_open_search | `sigmoid(pow_2(sigmoid(day_min(Ret))))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M3_I0_open_search | `abs_(sigmoid(pow_2(sigmoid(day_min(Ret)))))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M3_I0_open_search | `pow_2(sigmoid(pow_2(sigmoid(day_min(Ret)))))` |

## 共性:288 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.24 | 0.011 | 5 | -1.25 / -2.49 | `day_centroid(mul(2, cross_delta(Close, 30)))` |
| +1.12 | 0.006 | 4 | -1.36 / -2.48 | `cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` |
| +1.06 | 0.008 | 7 | -1.44 / -2.49 | `ts_med(day_ar1_coefficient(Close), 1)` |
| +1.06 | 0.008 | 7 | -1.44 / -2.49 | `cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20)` |
| +0.98 | 0.000 | 24 | -1.57 / -2.55 | `cross_delay(day_min(Ret), 1)` |
| +0.98 | 0.050 | 4 | -1.50 / -2.48 | `sub(day_max(Low), cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20))` |
| +0.95 | 0.018 | 4 | -1.53 / -2.48 | `div(day_max(High), day_min(Low))` |
| +0.95 | 0.018 | 4 | -1.53 / -2.48 | `log(div(day_max(High), day_min(Low)))` |
| +0.95 | 0.004 | 12 | -1.56 / -2.51 | `day_max(Low)` |
| +0.95 | 0.009 | 8 | -1.55 / -2.49 | `day_ar1_coefficient(Close)` |
| +0.92 | 0.028 | 5 | -1.56 / -2.48 | `day_at_max_ratio(Open)` |
| +0.84 | 0.000 | 14 | -1.67 / -2.51 | `cross_mean(day_sum(Ret), 120)` |
| +0.80 | 0.010 | 7 | -1.69 / -2.49 | `cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)` |
| +0.72 | 0.009 | 11 | -1.77 / -2.50 | `pow_2(day_argmin(High))` |
| +0.71 | 0.010 | 21 | -1.81 / -2.52 | `sub(day_last(Close), day_min(Low))` |
| +0.68 | 0.003 | 16 | -1.82 / -2.51 | `sub(day_sum(Ret), cs_mean(day_sum(Ret)))` |
| +0.66 | 0.061 | 5 | -1.82 / -2.48 | `cross_mean(day_sum(Ret), 241)` |
| +0.64 | 0.054 | 4 | -1.83 / -2.48 | `log(day_sum(Vwap))` |
| +0.62 | 0.000 | 93 | -2.05 / -2.67 | `day_sum(Ret)` |
| +0.60 | 0.006 | 25 | -1.92 / -2.52 | `day_max(High)` |

## 拆解(19 次评估)

### head score -2.82:`sigmoid(pow_2(sigmoid(day_min(Ret))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(sigmoid(day_min(Ret)))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `sigmoid(day_min(Ret))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `pow_2(sigmoid(day_min(Ret)))` | -2.77 | -2.19 | -2.77 | -0.05 | `sigmoid(sigmoid(day_min(Ret)))` |
| knockout | `sigmoid(day_min(Ret))` | — | — | — | — | `sigmoid(pow_2(day_min(Ret)))` |

### head score -2.82:`abs_(sigmoid(pow_2(sigmoid(day_min(Ret)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(sigmoid(day_min(Ret))))` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `pow_2(sigmoid(day_min(Ret)))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `sigmoid(day_min(Ret))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `sigmoid(pow_2(sigmoid(day_min(Ret))))` | -2.77 | -2.18 | -2.77 | -0.05 | `abs_(pow_2(sigmoid(day_min(Ret))))` |
| knockout | `pow_2(sigmoid(day_min(Ret)))` | -2.77 | -2.19 | -2.77 | -0.05 | `abs_(sigmoid(sigmoid(day_min(Ret))))` |
| knockout | `sigmoid(day_min(Ret))` | — | — | — | — | `abs_(sigmoid(pow_2(day_min(Ret))))` |

### head score -2.82:`pow_2(sigmoid(pow_2(sigmoid(day_min(Ret)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(sigmoid(day_min(Ret))))` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `pow_2(sigmoid(day_min(Ret)))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `sigmoid(day_min(Ret))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `sigmoid(pow_2(sigmoid(day_min(Ret))))` | -2.77 | -2.18 | -2.77 | -0.05 | `pow_2(pow_2(sigmoid(day_min(Ret))))` |
| knockout | `pow_2(sigmoid(day_min(Ret)))` | -2.77 | -2.19 | -2.77 | -0.05 | `pow_2(sigmoid(sigmoid(day_min(Ret))))` |
| knockout | `sigmoid(day_min(Ret))` | — | — | — | — | `pow_2(sigmoid(pow_2(day_min(Ret))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(mul(2, cross_delta(Close, 30)))` — enrichment,均值差 +1.24,p 0.011
2. `cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` — enrichment,均值差 +1.12,p 0.006
3. `ts_med(day_ar1_coefficient(Close), 1)` — enrichment,均值差 +1.06,p 0.008
4. `cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20)` — enrichment,均值差 +1.06,p 0.008
5. `cross_delay(day_min(Ret), 1)` — enrichment,均值差 +0.98,p 0.000
6. `sub(day_max(Low), cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20))` — enrichment,均值差 +0.98,p 0.050
7. `div(day_max(High), day_min(Low))` — enrichment,均值差 +0.95,p 0.018
8. `log(div(day_max(High), day_min(Low)))` — enrichment,均值差 +0.95,p 0.018
9. `day_max(Low)` — enrichment,均值差 +0.95,p 0.004
10. `day_ar1_coefficient(Close)` — enrichment,均值差 +0.95,p 0.009
11. `day_at_max_ratio(Open)` — enrichment,均值差 +0.92,p 0.028
12. `cross_mean(day_sum(Ret), 120)` — enrichment,均值差 +0.84,p 0.000
13. `cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)` — enrichment,均值差 +0.80,p 0.010
14. `pow_2(day_argmin(High))` — enrichment,均值差 +0.72,p 0.009
15. `sub(day_last(Close), day_min(Low))` — enrichment,均值差 +0.71,p 0.010
16. `sub(day_sum(Ret), cs_mean(day_sum(Ret)))` — enrichment,均值差 +0.68,p 0.003
17. `cross_mean(day_sum(Ret), 241)` — enrichment,均值差 +0.66,p 0.061
18. `log(day_sum(Vwap))` — enrichment,均值差 +0.64,p 0.054
19. `day_sum(Ret)` — enrichment,均值差 +0.62,p 0.000
20. `day_max(High)` — enrichment,均值差 +0.60,p 0.006
21. `day_argmin(High)` — enrichment,均值差 +0.59,p 0.017
22. `log(div(day_first(Open), cross_delay(day_last(Close), 1)))` — enrichment,均值差 +0.57,p 0.051
23. `div(day_first(Open), cross_delay(day_last(Close), 1))` — enrichment,均值差 +0.53,p 0.017
24. `cs_mean(day_sum(Ret))` — enrichment,均值差 +0.48,p 0.006
25. `day_max(Close)` — enrichment,均值差 +0.47,p 0.086
26. `day_last(Close)` — enrichment,均值差 +0.45,p 0.009
27. `day_min(Low)` — enrichment,均值差 +0.45,p 0.012

## 本组之前各轮的任务

- `prods2047Pr1a_Na`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.32(train +0.11 valid -0.32):`cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)`
  - score -0.49(train -0.24 valid -0.49):`cross_regbeta(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)`
  - score -0.57(train -0.10 valid -0.57):`cross_reg_tvalue(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)`
  - score -0.67(train -0.41 valid -0.67):`cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_min(Ret))), 120)`
  - score -0.69(train -0.21 valid -0.69):`cross_corr(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)`
- `prods2047Pr1b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score -0.20(train +0.31 valid -0.20):`cross_regbeta(cross_delay(div(sub(day_last(Close), day_min(Low)), sub(day_centroid(mul(-0.5, cross_delta(Close, 30))), cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20))), 1), day_sum(Ret), 120)`
  - score -0.21(train +0.14 valid -0.21):`cross_regbeta(cross_delay(mul(sub(day_last(Close), day_min(Low)), sub(day_max(Low), sub(day_max(High), day_min(Low)))), 1), day_sum(Ret), 120)`
  - score -0.43(train -0.43 valid -0.41):`cross_regbeta(day_max(High), sub(day_centroid(mul(2, cross_delta(Close, 30))), 1), 120)`
  - score -0.43(train -0.43 valid -0.41):`cross_regbeta(day_max(High), sub(day_centroid(mul(-0.5, cross_delta(Close, 30))), 1), 120)`
  - score -0.49(train -0.49 valid -0.30):`cross_regbeta(cross_delay(day_max(High), 1), sub(day_centroid(mul(2, cross_delta(Close, 30))), 1), 120)`
- `prods2047Pr2a_Ea`:核心 `day_sum(Ret)`;评分 72,过线 0,入 heads 0;采样计数 {'c05_no_core': 841, 'c05_skeleton': 455}
  - score -0.89(train -0.89 valid -0.02):`cross_mean(day_sum(Ret), 241)`
  - score -0.93(train -0.93 valid -0.15):`div(cross_mean(day_sum(Ret), 241), cross_stddev(day_sum(Ret), 120))`
  - score -0.99(train -0.99 valid -0.47):`div(cross_mean(day_sum(Ret), 241), cross_mean(day_sum(Ret), 120))`
  - score -1.23(train -1.23 valid -1.21):`sub(cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120), cross_mean(day_sum(Ret), 120))`
  - score -1.27(train -1.27 valid -0.72):`cross_mean(sub(cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120), cross_mean(day_sum(Ret), 15)), 120)`
- `prods2047Pr2b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {'c05_skeleton': 19}
  - score -0.99(train -0.92 valid -0.99):`ts_std(cross_mean(cs_bucket_demean(day_open(High), LogFloatShares), 60), 5)`
  - score -1.02(train -1.02 valid -1.00):`cross_corr(day_argmax(High), day_min(Ret), 120)`
  - score -1.50(train -1.26 valid -1.50):`cross_corr(day_argmin(Ret), day_min(Ret), 120)`
  - score -1.60(train -1.55 valid -1.60):`cross_corr(mul(day_argmin(Low), cross_mean(day_argmax(High), 120)), day_min(Low), 120)`
  - score -1.65(train -1.07 valid -1.65):`ts_std(cross_mean(cs_first_low20(day_open(Vwap), LogFloatShares), 60), 5)`

## 比原 head 好的拆解变体(R 候选)

(没有)
