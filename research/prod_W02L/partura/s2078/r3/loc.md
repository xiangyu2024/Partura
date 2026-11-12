# 定位:种子 2078,P 组,第 3 轮(只含 train / valid)

快照:prods2078M1_I0_open_search, prods2078M2_I0_open_search, prods2078M3_I0_open_search, prods2078Pr1a_Ea, prods2078Pr1b_Nb, prods2078Pr2a_Ea, prods2078Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.23 | +0.01 | -0.23 | +1 | 5 | prods2078M1_I0_open_search | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), cross_mean(day_std(Ret), 60))` |
| -0.64 | -0.00 | -0.64 | +1 | 20 | prods2078M2_I0_open_search | `sigmoid(ts_regbeta(day_quantile(High), day_skew(Volume), 30))` |
| -0.98 | -0.98 | -0.40 | +1 | 20 | prods2078M2_I0_open_search | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 30))` |
| -1.26 | -1.26 | -1.25 | -1 | 5 | prods2078M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 241))` |
| -1.34 | -1.19 | -1.34 | -1 | 5 | prods2078M1_I0_open_search | `pow_05(cs_normalize(day_mean(Volume)))` |
| -1.49 | -1.49 | -0.85 | -1 | 20 | prods2078M3_I0_open_search | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))` |
| -1.70 | -1.33 | -1.70 | +1 | 20 | prods2078M3_I0_open_search | `signedpower(neg(neg(sigmoid(day_cov(Open, Ret)))))` |
| -1.70 | -1.70 | -1.63 | +1 | 5 | prods2078M3_I0_open_search | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))` |
| -1.80 | -1.47 | -1.80 | -1 | 20 | prods2078M1_I0_open_search | `pow_2(day_cov(Amt, Vwap))` |

## 共性:304 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.37 | 0.000 | 12 | -0.15 / -2.52 | `cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)` |
| +2.36 | 0.000 | 5 | -0.11 / -2.47 | `cs_last_low05(cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10), LogTotalCap)` |
| +2.35 | 0.000 | 6 | -0.13 / -2.48 | `cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10)` |
| +2.25 | 0.002 | 4 | -0.20 / -2.46 | `cross_mean(cs_last_low05(day_flat_run_max(Volume), cs_last_low05(day_flat_run_max(Volume), LogTotalCap)), 10)` |
| +2.19 | 0.000 | 38 | -0.52 / -2.70 | `cs_last_low05(day_flat_run_max(Volume), LogTotalCap)` |
| +1.94 | 0.000 | 10 | -0.55 / -2.49 | `cs_last_low05(day_flat_run_max(Volume), cs_last_low05(day_flat_run_max(Volume), LogTotalCap))` |
| +1.80 | 0.000 | 9 | -0.68 / -2.48 | `cross_mean(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), 10)` |
| +1.50 | 0.000 | 57 | -1.21 / -2.71 | `day_flat_run_max(Volume)` |
| +1.49 | 0.023 | 4 | -0.96 / -2.45 | `cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close))), 20)` |
| +1.46 | 0.005 | 7 | -1.00 / -2.46 | `div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close)))` |
| +1.45 | 0.000 | 30 | -1.12 / -2.57 | `day_flat_ratio(Volume)` |
| +1.43 | 0.015 | 5 | -1.02 / -2.45 | `cs_last_low05(cross_mean(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), 10), LogTotalCap)` |
| +1.39 | 0.000 | 18 | -1.12 / -2.51 | `mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open))` |
| +1.35 | 0.004 | 9 | -1.12 / -2.47 | `day_sum(Vwap)` |
| +1.35 | 0.000 | 24 | -1.19 / -2.54 | `cross_delta(day_flat_ratio(Volume), 30)` |
| +1.23 | 0.000 | 22 | -1.29 / -2.52 | `day_min(Close)` |
| +1.20 | 0.029 | 6 | -1.26 / -2.45 | `cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)` |
| +1.18 | 0.000 | 43 | -1.42 / -2.60 | `cs_demean(div(day_mean(Ret), 2))` |
| +1.18 | 0.000 | 43 | -1.42 / -2.60 | `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` |
| +1.15 | 0.001 | 20 | -1.35 / -2.51 | `day_max(Close)` |

## 拆解(17 次评估)

### head score -1.49:`sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 3)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(cross_sum(in_sum_rolling(Amt, 5), 3))` | -1.49 | -1.49 | -0.84 | — | (子树本身) |
| swap | `Amt->Volume` | -1.20 | -1.20 | -1.09 | — | `sub(0.5, day_first(cross_sum(in_sum_rolling(Volume, 5), 3)))` |
| window | `cross_sum@3->2` | -1.45 | -1.45 | -0.81 | — | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 2)))` |
| window | `cross_sum@3->6` | -1.70 | -1.70 | -0.86 | — | `sub(0.5, day_first(cross_sum(in_sum_rolling(Amt, 5), 6)))` |

### head score -1.70:`signedpower(neg(neg(sigmoid(day_cov(Open, Ret)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(neg(sigmoid(day_cov(Open, Ret))))` | — | — | — | — | 门槛废品 |
| sufficiency | `neg(sigmoid(day_cov(Open, Ret)))` | — | — | — | — | 门槛废品 |
| sufficiency | `sigmoid(day_cov(Open, Ret))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_cov(Open, Ret)` | -1.65 | -1.33 | -1.65 | — | (子树本身) |
| knockout | `neg(neg(sigmoid(day_cov(Open, Ret))))` | — | — | — | — | `signedpower(neg(sigmoid(day_cov(Open, Ret))))` |
| knockout | `sigmoid(day_cov(Open, Ret))` | -1.65 | -1.33 | -1.65 | -0.04 | `signedpower(neg(neg(day_cov(Open, Ret))))` |
| swap | `Open->Close` | — | — | — | — | `signedpower(neg(neg(sigmoid(day_cov(Close, Ret)))))` |

### head score -1.70:`sub(-2, abs_(day_mean(nt_ts_argmax(High, 3))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(day_mean(nt_ts_argmax(High, 3)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_mean(nt_ts_argmax(High, 3))` | — | — | — | — | 门槛废品 |
| knockout | `abs_(day_mean(nt_ts_argmax(High, 3)))` | — | — | — | — | `sub(-2, day_mean(nt_ts_argmax(High, 3)))` |
| swap | `High->Low` | — | — | — | — | `sub(-2, abs_(day_mean(nt_ts_argmax(Low, 3))))` |
| window | `nt_ts_argmax@3->2` | — | — | — | — | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 2))))` |
| window | `nt_ts_argmax@3->6` | — | — | — | — | `sub(-2, abs_(day_mean(nt_ts_argmax(High, 6))))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)` — enrichment,均值差 +2.37,p 0.000
2. `cs_last_low05(cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10), LogTotalCap)` — enrichment,均值差 +2.36,p 0.000
3. `cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10)` — enrichment,均值差 +2.35,p 0.000
4. `cross_mean(cs_last_low05(day_flat_run_max(Volume), cs_last_low05(day_flat_run_max(Volume), LogTotalCap)), 10)` — enrichment,均值差 +2.25,p 0.002
5. `cs_last_low05(day_flat_run_max(Volume), LogTotalCap)` — enrichment,均值差 +2.19,p 0.000
6. `cs_last_low05(day_flat_run_max(Volume), cs_last_low05(day_flat_run_max(Volume), LogTotalCap))` — enrichment,均值差 +1.94,p 0.000
7. `cross_mean(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), 10)` — enrichment,均值差 +1.80,p 0.000
8. `day_flat_run_max(Volume)` — enrichment,均值差 +1.50,p 0.000
9. `cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close))), 20)` — enrichment,均值差 +1.49,p 0.023
10. `div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close)))` — enrichment,均值差 +1.46,p 0.005
11. `day_flat_ratio(Volume)` — enrichment,均值差 +1.45,p 0.000
12. `cs_last_low05(cross_mean(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), 10), LogTotalCap)` — enrichment,均值差 +1.43,p 0.015
13. `mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open))` — enrichment,均值差 +1.39,p 0.000
14. `day_sum(Vwap)` — enrichment,均值差 +1.35,p 0.004
15. `cross_delta(day_flat_ratio(Volume), 30)` — enrichment,均值差 +1.35,p 0.000
16. `day_min(Close)` — enrichment,均值差 +1.23,p 0.000
17. `cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)` — enrichment,均值差 +1.20,p 0.029
18. `cs_demean(div(day_mean(Ret), 2))` — enrichment,均值差 +1.18,p 0.000
19. `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` — enrichment,均值差 +1.18,p 0.000
20. `day_max(Close)` — enrichment,均值差 +1.15,p 0.001
21. `sub(day_max(Close), day_min(Close))` — enrichment,均值差 +1.14,p 0.002
22. `day_quantile_q25(Open)` — enrichment,均值差 +1.07,p 0.000
23. `day_mean(Ret)` — enrichment,均值差 +1.04,p 0.000
24. `ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30)` — enrichment,均值差 +1.01,p 0.008

## 本组之前各轮的任务

- `prods2078Pr1a_Ea`:核心 `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)`;评分 96,过线 0,入 heads 0;采样计数 {'c05_no_core': 2722, 'c05_skeleton': 1277, 'mutation_refused': 11, 'c05_periphery_seen': 4}
  - score -0.03(train -0.03 valid +0.14):`cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)`
  - score -0.07(train -0.07 valid +0.07):`cross_regbeta(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)`
  - score -0.41(train -0.41 valid -0.35):`cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241), 241)`
  - score -0.44(train -0.44 valid +0.38):`cs_bucket_zscore(cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241), ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30))`
  - score -0.58(train -0.58 valid -0.08):`ts_stddev(ts_max(cs_demean(div(ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30), 2)), 30), 30)`
- `prods2078Pr1b_Nb`:核心 `—`;评分 61,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.09(train -0.02 valid -0.09):`cs_last_low05(day_flat_ratio(Volume), LogTotalCap)`
  - score -0.09(train -0.02 valid -0.09):`cs_last_low05(cs_last_low05(day_flat_ratio(Volume), LogTotalCap), LogTotalCap)`
  - score -0.09(train -0.02 valid -0.09):`cs_last_low05(day_flat_ratio(Volume), cs_last_low05(day_flat_ratio(Volume), LogTotalCap))`
  - score -0.24(train +0.35 valid -0.24):`cs_last_low05(day_flat_run_max(Volume), LogTotalCap)`
  - score -0.24(train +0.35 valid -0.24):`cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)`
- `prods2078Pr2a_Ea`:核心 `day_flat_run_max(Volume)`;评分 94,过线 0,入 heads 0;采样计数 {'c05_no_core': 1441, 'c05_skeleton': 673, 'c05_periphery_seen': 12}
  - score -0.03(train +0.49 valid -0.03):`cross_mean(cs_last_low05(cross_mean(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), 10), LogTotalCap), 5)`
  - score -0.03(train +0.52 valid -0.03):`cross_mean(cs_last_low05(cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10), LogTotalCap), 5)`
  - score -0.05(train +0.77 valid -0.05):`cross_mean(cs_last_low40(cross_mean(cs_last_low05(cross_mean(cs_last_low05(cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10), LogTotalCap), 10), cs_last_low05(day_flat_run_max(Volume), LogTotalCap)), 10), cs_last_low05(day_flat_run_max(Volume), LogTotalCap)), 10)`
  - score -0.13(train +0.41 valid -0.13):`cross_mean(cs_last_low05(cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)), cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)), 10), cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)), 10)`
  - score -0.13(train +0.41 valid -0.13):`cross_mean(cs_last_low05(cross_mean(cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap), 10), LogTotalCap), 10)`
- `prods2078Pr2b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score -0.59(train -0.59 valid -0.56):`cross_mean(div(cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), sub(day_max(Close), day_min(Close))), sub(day_max(Close), day_min(Close))), 20), sub(day_max(Close), day_min(Close))), 20)`
  - score -0.64(train -0.51 valid -0.64):`cross_mean(div(cross_mean(cross_delta(day_flat_ratio(Volume), 30), 15), sub(day_max(Close), day_min(Close))), 20)`
  - score -0.74(train -0.58 valid -0.74):`cross_mean(div(cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), cross_mean(div(cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close))), 20), sub(day_max(Close), day_min(Close))), 20))), 20), sub(day_max(Close), cross_mean(div(cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close))), 20), sub(day_max(Close), day_min(Close))), 20))), 20)`
  - score -0.77(train -0.53 valid -0.77):`cross_mean(div(cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close))), 20), sub(day_max(Close), day_min(Close))), 20)`
  - score -0.79(train -0.63 valid -0.79):`cross_mean(div(cross_mean(div(mul(cross_delta(day_flat_ratio(Volume), 30), day_quantile_q25(Open)), sub(day_max(Close), day_min(Close))), 15), sub(day_max(Close), day_min(Close))), 20)`

## 比原 head 好的拆解变体(R 候选)

(没有)
