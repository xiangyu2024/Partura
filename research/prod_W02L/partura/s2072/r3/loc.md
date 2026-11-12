# 定位:种子 2072,P 组,第 3 轮(只含 train / valid)

快照:prods2072M1_I0_open_search, prods2072M2_I0_open_search, prods2072M3_I0_open_search, prods2072Pr1a_Ea, prods2072Pr1b_Nb, prods2072Pr2a_I0_open_search, prods2072Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.81 | -0.81 | -0.72 | +1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 50)` |
| -1.33 | -0.90 | -1.33 | +1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 20)` |
| -1.45 | -1.35 | -1.45 | -1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)` |
| -1.45 | -1.45 | -1.16 | -1 | 20 | prods2072M3_I0_open_search | `ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), 20)` |
| -1.47 | -1.43 | -1.47 | +1 | 0 | prods2072M2_I0_open_search | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` |
| -1.50 | -1.50 | -0.85 | -1 | 0 | prods2072M3_I0_open_search | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 50)` |
| -1.80 | -1.24 | -1.80 | +1 | 20 | prods2072M3_I0_open_search | `ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 50)` |
| -2.18 | -1.65 | -2.18 | -1 | 20 | prods2072M2_I0_open_search | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60)), 5)` |
| -2.36 | -1.82 | -2.36 | -1 | 20 | prods2072M2_I0_open_search | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15)), 1)` |

## 共性:231 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.90 | 0.000 | 19 | -1.23 / -2.13 | `pow_05(day_quantile_q25(Low))` |
| +0.85 | 0.000 | 20 | -1.28 / -2.13 | `day_quantile_q25(Low)` |
| +0.84 | 0.003 | 8 | -1.24 / -2.08 | `inv(ts_hurst(day_last(Volume), 20))` |
| +0.83 | 0.005 | 13 | -1.27 / -2.10 | `day_distinct_ratio(Low)` |
| +0.80 | 0.044 | 4 | -1.27 / -2.07 | `sub(cross_argmax(day_quantile_q25(Amt), 241), BoardCode)` |
| +0.80 | 0.008 | 7 | -1.28 / -2.08 | `pow_05(inv(ts_hurst(day_last(Volume), 20)))` |
| +0.78 | 0.044 | 5 | -1.29 / -2.07 | `cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60)` |
| +0.78 | 0.001 | 13 | -1.32 / -2.10 | `pow_3(LimitWidth)` |
| +0.70 | 0.012 | 8 | -1.38 / -2.08 | `abs_(ts_hurst(day_last(Volume), 20))` |
| +0.70 | 0.085 | 4 | -1.37 / -2.07 | `pow_05(LimitWidth)` |
| +0.68 | 0.074 | 5 | -1.39 / -2.07 | `day_max(Vwap)` |
| +0.63 | 0.002 | 18 | -1.47 / -2.10 | `day_es_ratio_hi(Vwap)` |
| +0.59 | 0.021 | 19 | -1.51 / -2.10 | `day_flat_ratio(Vwap)` |
| +0.59 | 0.004 | 18 | -1.51 / -2.10 | `cs_winsor(ts_hurst(day_last(Volume), 20))` |
| +0.55 | 0.073 | 10 | -1.53 / -2.08 | `day_wstd(High, Amt)` |
| +0.54 | 0.122 | 5 | -1.52 / -2.07 | `cs_last_low20(day_es_ratio_hi(Vwap), day_wstd(High, Amt))` |
| +0.44 | 0.302 | 5 | -1.62 / -2.06 | `day_std(High)` |
| +0.43 | 0.000 | 69 | -1.75 / -2.18 | `ts_hurst(day_last(Volume), 20)` |
| +0.41 | 0.146 | 26 | -1.69 / -2.10 | `day_sum(Ret)` |
| +0.41 | 0.070 | 10 | -1.66 / -2.07 | `day_wstd(Close, Amt)` |

## 拆解(34 次评估)

### head score -1.45:`ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))` | -0.99 | -0.99 | -0.93 | — | (子树本身) |
| sufficiency | `log(add(day_open(Ret), day_std(Vwap)))` | -2.28 | -1.62 | -2.28 | — | (子树本身) |
| sufficiency | `add(day_open(Ret), day_std(Vwap))` | -2.27 | -1.54 | -2.27 | — | (子树本身) |
| sufficiency | `day_open(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))` | -2.40 | -1.46 | -2.40 | +0.94 | `ts_mean(log(add(day_open(Ret), day_std(Vwap))), 20)` |
| knockout | `log(add(day_open(Ret), day_std(Vwap)))` | -2.43 | -1.57 | -2.43 | +0.97 | `ts_mean(mul(add(day_open(Ret), day_std(Vwap)), day_std(Vwap)), 20)` |
| knockout | `add(day_open(Ret), day_std(Vwap))` | — | — | — | — | `ts_mean(mul(log(day_open(Ret)), day_std(Vwap)), 20)` |
| swap | `Vwap->Close` | -1.46 | -1.46 | -1.04 | — | `ts_mean(mul(log(add(day_open(Ret), day_std(Close))), day_std(Close)), 20)` |
| window | `ts_mean@20->10` | -1.33 | -1.33 | -1.06 | — | `ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), 10)` |
| window | `ts_mean@20->40` | -1.33 | -1.33 | -1.21 | — | `ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), 40)` |

### head score -1.50:`ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10))` | -1.31 | -1.31 | -1.01 | — | (子树本身) |
| sufficiency | `log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))` | -1.26 | -1.26 | -0.84 | — | (子树本身) |
| sufficiency | `ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)` | -3.00 | -3.00 | -2.23 | — | (子树本身) |
| sufficiency | `add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))` | -2.28 | -1.62 | -2.28 | — | (子树本身) |
| knockout | `mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10))` | -1.30 | -1.30 | -0.94 | -0.20 | `ts_mean(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), 50)` |
| knockout | `log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))` | -2.30 | -1.43 | -2.30 | +0.79 | `ts_mean(mul(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 50)` |
| knockout | `ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)` | -3.25 | -1.89 | -3.25 | +1.74 | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low))), 50)` |
| knockout | `add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))` | -2.30 | -1.83 | -2.30 | +0.80 | `ts_mean(mul(log(log(add(day_open(Ret), day_std(Vwap)))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 50)` |
| swap | `Vwap->Close` | -1.46 | -1.46 | -0.88 | — | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Close))), day_std(Close))), ts_hurst(div(log(add(day_open(Ret), day_std(Close))), day_max(Low)), 10)), 50)` |
| swap | `Low->High` | -1.50 | -1.50 | -0.87 | — | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(High)), 10)), 50)` |
| window | `ts_mean@50->25` | -1.52 | -1.52 | -1.09 | — | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 25)` |
| window | `ts_mean@50->100` | -1.26 | -1.26 | -1.05 | — | `ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 100)` |

### head score -1.80:`ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20))` | -1.78 | -1.78 | -1.35 | — | (子树本身) |
| sufficiency | `log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))))` | -1.48 | -1.48 | -1.45 | — | (子树本身) |
| sufficiency | `ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)` | -2.31 | -2.31 | -2.23 | — | (子树本身) |
| sufficiency | `div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))` | -2.56 | -2.56 | -1.09 | — | (子树本身) |
| knockout | `mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20))` | -1.73 | -1.08 | -1.73 | -0.06 | `ts_mean(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), 50)` |
| knockout | `log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))))` | -2.28 | -2.28 | -0.73 | +0.49 | `ts_mean(mul(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 50)` |
| knockout | `ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)` | -2.54 | -2.54 | -1.79 | +0.74 | `ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), 50)` |
| knockout | `div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))` | -2.98 | -2.23 | -2.98 | +1.19 | `ts_mean(mul(log(day_hurst(Volume)), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 50)` |
| swap | `Volume->Amt` | -1.81 | -1.21 | -1.81 | — | `ts_mean(mul(log(div(day_hurst(Amt), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Amt), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 50)` |
| swap | `Vwap->Close` | -1.81 | -1.10 | -1.81 | — | `ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Close))), day_std(Close))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Close))), day_std(Close)))), 20)), 50)` |
| window | `ts_mean@50->25` | -1.36 | -1.28 | -1.36 | — | `ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 25)` |
| window | `ts_mean@50->100` | — | — | — | — | `ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_05(day_quantile_q25(Low))` — enrichment,均值差 +0.90,p 0.000
2. `day_quantile_q25(Low)` — enrichment,均值差 +0.85,p 0.000
3. `inv(ts_hurst(day_last(Volume), 20))` — enrichment,均值差 +0.84,p 0.003
4. `day_distinct_ratio(Low)` — enrichment,均值差 +0.83,p 0.005
5. `sub(cross_argmax(day_quantile_q25(Amt), 241), BoardCode)` — enrichment,均值差 +0.80,p 0.044
6. `pow_05(inv(ts_hurst(day_last(Volume), 20)))` — enrichment,均值差 +0.80,p 0.008
7. `cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60)` — enrichment,均值差 +0.78,p 0.044
8. `pow_3(LimitWidth)` — enrichment,均值差 +0.78,p 0.001
9. `abs_(ts_hurst(day_last(Volume), 20))` — enrichment,均值差 +0.70,p 0.012
10. `pow_05(LimitWidth)` — enrichment,均值差 +0.70,p 0.085
11. `day_max(Vwap)` — enrichment,均值差 +0.68,p 0.074
12. `day_es_ratio_hi(Vwap)` — enrichment,均值差 +0.63,p 0.002
13. `day_flat_ratio(Vwap)` — enrichment,均值差 +0.59,p 0.021
14. `cs_winsor(ts_hurst(day_last(Volume), 20))` — enrichment,均值差 +0.59,p 0.004
15. `day_wstd(High, Amt)` — enrichment,均值差 +0.55,p 0.073
16. `ts_hurst(day_last(Volume), 20)` — enrichment,均值差 +0.43,p 0.000
17. `day_wstd(Close, Amt)` — enrichment,均值差 +0.41,p 0.070
18. `day_last(Volume)` — enrichment,均值差 +0.38,p 0.003

## 本组之前各轮的任务

- `prods2072Pr1a_Ea`:核心 `ts_hurst(day_last(Volume), 20)`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 1166, 'c05_skeleton': 599, 'mutation_refused': 6, 'c05_periphery_seen': 6}
  - score -0.58(train -0.58 valid -0.44):`cs_scale(cs_mask_top_replace_mean_neg(cs_bucket_zscore(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth))))`
  - score -0.58(train -0.58 valid -0.44):`cs_mask_top_replace_mean_neg(cs_bucket_zscore(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth)))`
  - score -0.69(train -0.69 valid -0.30):`cs_scale(cs_mask_top_replace_mean_neg(cs_bucket_zscore(cs_first_low40(abs_(ts_hurst(day_last(Volume), 20)), pow_05(inv(ts_hurst(day_last(Volume), 20)))), pow_3(LimitWidth))))`
  - score -0.73(train -0.70 valid -0.73):`cs_mask_top_replace_mean_neg(cs_first_low40(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth)))`
  - score -0.73(train -0.70 valid -0.73):`cs_mask_top_replace_mean_neg(cs_first_low40(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_05(LimitWidth)))`
- `prods2072Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.20(train -0.20 valid +0.32):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), -1), cs_last_low20(day_mean(Vwap), day_wstd(Amt, Amt)), 30)`
  - score -0.39(train -0.39 valid -0.03):`cross_regbeta(div(pow_05(day_quantile_q25(Amt)), -1), cs_last_low20(day_es_ratio_hi(Vwap), day_wstd(Close, Amt)), 30)`
  - score -0.65(train -0.53 valid -0.65):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), -1), cs_last_low20(day_es_ratio_hi(Amt), day_wstd(High, Amt)), 30)`
  - score -0.71(train -0.49 valid -0.71):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), -1), cs_last_low20(day_es_ratio_hi(Vwap), day_quantile_q25(Low)), 30)`
  - score -0.84(train -0.76 valid -0.84):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), 5), cs_last_low20(day_es_ratio_hi(Low), day_wstd(Close, Amt)), 241)`
- `prods2072Pr2a_I0_open_search`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.93(train -0.90 valid -0.93):`ts_regalpha(sub(cross_argmax(day_quantile_q25(Amt), 241), BoardCode), cross_argmax(day_wstd(Vwap, Low), 241), 20)`
  - score -0.97(train -0.97 valid -0.45):`ts_regalpha(sub(cross_argmax(day_quantile_q25(Amt), 241), BoardCode), cross_argmax(ts_regalpha(sub(cross_argmax(day_quantile_q25(Amt), 241), BoardCode), cross_argmax(day_quantile_q25(Amt), 241), 20), 241), 20)`
  - score -0.99(train -0.99 valid -0.25):`ts_regalpha(sub(cross_argmax(day_wstd(Vwap, Low), 241), BoardCode), cross_argmax(ts_regalpha(sub(cross_argmax(day_wstd(Vwap, Low), 241), BoardCode), cross_argmax(day_wstd(Vwap, Low), 241), 20), 241), 20)`
  - score -1.18(train -1.18 valid +0.01):`ts_regalpha(sub(cross_argmax(day_quantile_q25(Vwap), 241), BoardCode), cross_argmax(ts_regalpha(sub(cross_argmax(day_quantile_q25(Vwap), 241), BoardCode), cross_argmax(day_quantile_q25(Vwap), 241), 20), 241), 20)`
  - score -1.38(train -1.38 valid -1.11):`cross_argmin(day_quantile_q25(Amt), 241)`
- `prods2072Pr2b_Nb`:核心 `—`;评分 97,过线 0,入 heads 0;采样计数 {'c05_skeleton': 12}
  - score -0.20(train -0.20 valid +0.71):`cross_corr(day_flat_ratio(Vwap), cs_regres(cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), day_distinct_ratio(Low)), 60)`
  - score -0.36(train -0.36 valid -0.32):`cs_regres(cross_corr(day_flat_ratio(Vwap), day_sum(Low), 60), day_distinct_ratio(Low))`
  - score -0.41(train -0.41 valid -0.33):`cross_corr(day_flat_ratio(Vwap), day_sum(Low), 60)`
  - score -0.60(train -0.60 valid +0.75):`cross_corr(day_flat_ratio(Vwap), cross_corr(day_flat_ratio(Vwap), day_sum(Ret), 60), 60)`
  - score -0.88(train -0.88 valid -0.79):`cs_regres(cs_regres(day_max(Vwap), day_distinct_ratio(Low)), day_distinct_ratio(Low))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.44(window ts_mean@50->25):`ts_mean(mul(log(div(day_hurst(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))))), ts_hurst(div(day_last(Volume), log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)))), 20)), 25)`
- 增益 +0.24(window ts_mean@50->100):`ts_mean(mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10)), 100)`
- 增益 +0.20(knockout mul(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 10))):`ts_mean(log(add(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap))), 50)`
- 增益 +0.13(window ts_mean@20->10):`ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), 10)`
- 增益 +0.12(window ts_mean@20->40):`ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), day_std(Vwap)), 40)`
