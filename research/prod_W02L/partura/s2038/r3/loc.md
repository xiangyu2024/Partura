# 定位:种子 2038,P 组,第 3 轮(只含 train / valid)

快照:prods2038M1_I0_open_search, prods2038M2_I0_open_search, prods2038M3_I0_open_search, prods2038Pr1a_Na, prods2038Pr1b_Nb, prods2038Pr2a_I0_open_search, prods2038Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.23 | -0.23 | -0.22 | +1 | 20 | prods2038M1_I0_open_search | `div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt), 20), 1))` |
| -0.43 | +0.11 | -0.43 | +1 | 0 | prods2038M1_I0_open_search | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 50)` |
| -1.01 | -1.01 | -0.66 | +1 | 20 | prods2038M2_I0_open_search | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Volume), 60), 50), 15), 15)` |
| -1.14 | -1.14 | -1.03 | -1 | 5 | prods2038M1_I0_open_search | `ts_decay_linear(day_open(Volume), 5)` |
| -1.52 | -1.52 | -0.83 | -1 | 5 | prods2038M2_I0_open_search | `ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241), 50)` |
| -1.64 | -0.80 | -1.64 | -1 | 5 | prods2038M3_I0_open_search | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50), 50)` |
| -1.87 | -1.07 | -1.87 | +1 | 20 | prods2038M2_I0_open_search | `cross_hurst(day_autocorr_n1(Amt), 60)` |
| -1.90 | -0.69 | -1.90 | -1 | 0 | prods2038M3_I0_open_search | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 50)` |
| -1.95 | -1.36 | -1.95 | -1 | 5 | prods2038M3_I0_open_search | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30), 50)` |

## 共性:301 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.39 | 0.000 | 11 | -0.98 / -2.36 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` |
| +1.36 | 0.001 | 8 | -0.99 / -2.35 | `cross_regbeta(day_last(Amt), day_open(Amt), 10)` |
| +1.27 | 0.002 | 7 | -1.07 / -2.34 | `cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10))` |
| +1.26 | 0.006 | 4 | -1.07 / -2.33 | `cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)), 10)` |
| +1.21 | 0.000 | 16 | -1.17 / -2.38 | `day_open(Amt)` |
| +1.20 | 0.000 | 17 | -1.18 / -2.38 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| +1.17 | 0.023 | 5 | -1.16 / -2.33 | `cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap)` |
| +1.16 | 0.000 | 13 | -1.21 / -2.36 | `cross_min(day_last(Close), 482)` |
| +1.11 | 0.002 | 7 | -1.23 / -2.34 | `cross_mean(day_last(Close), 10)` |
| +1.11 | 0.002 | 7 | -1.23 / -2.34 | `cross_min(cross_mean(day_last(Close), 10), 482)` |
| +1.09 | 0.000 | 35 | -1.35 / -2.44 | `day_last(Amt)` |
| +1.09 | 0.008 | 5 | -1.24 / -2.33 | `sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares))` |
| +1.08 | 0.000 | 21 | -1.31 / -2.39 | `day_wmean(Ret, Amt)` |
| +0.97 | 0.000 | 52 | -1.51 / -2.48 | `cross_mean(LogFloatShares, 10)` |
| +0.93 | 0.000 | 44 | -1.52 / -2.45 | `cross_min(cross_mean(LogFloatShares, 10), 482)` |
| +0.93 | 0.000 | 22 | -1.45 / -2.38 | `day_mean(Ret)` |
| +0.91 | 0.000 | 41 | -1.53 / -2.44 | `sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))` |
| +0.85 | 0.000 | 58 | -1.63 / -2.48 | `day_last(Close)` |
| +0.83 | 0.019 | 7 | -1.50 / -2.33 | `sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)` |
| +0.78 | 0.000 | 53 | -1.67 / -2.45 | `log(day_last(Close))` |

## 拆解(39 次评估)

### head score -0.23:`div(cross_mean(day_open(Amt), 5), add(cross_mean(day_sum(Amt), 20), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_open(Amt), 5)` | -1.59 | -1.59 | -0.87 | — | (子树本身) |
| sufficiency | `cross_mean(day_sum(Amt), 20)` | -3.63 | -2.77 | -3.63 | — | (子树本身) |
| sufficiency | `day_open(Amt)` | -1.30 | -1.30 | -0.79 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `add(cross_mean(day_sum(Amt), 20), 1)` | -0.23 | -0.23 | -0.22 | -0.00 | `div(cross_mean(day_open(Amt), 5), cross_mean(day_sum(Amt), 20))` |
| knockout | `cross_mean(day_open(Amt), 5)` | -0.41 | -0.41 | -0.19 | +0.18 | `div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1))` |
| knockout | `cross_mean(day_sum(Amt), 20)` | -0.69 | -0.69 | -0.13 | +0.46 | `div(cross_mean(day_open(Amt), 5), add(day_sum(Amt), 1))` |
| swap | `Amt->Volume` | -0.21 | -0.21 | -0.18 | — | `div(cross_mean(day_open(Volume), 5), add(cross_mean(day_sum(Volume), 20), 1))` |
| window | `cross_mean@5->2` | -0.34 | -0.34 | -0.18 | — | `div(cross_mean(day_open(Amt), 2), add(cross_mean(day_sum(Amt), 20), 1))` |
| window | `cross_mean@5->10` | -0.45 | -0.45 | -0.32 | — | `div(cross_mean(day_open(Amt), 10), add(cross_mean(day_sum(Amt), 20), 1))` |

### head score -1.64:`ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50)` | -2.51 | -1.42 | -2.51 | — | (子树本身) |
| sufficiency | `ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30)` | -4.22 | -4.22 | -3.22 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(day_autocorr_n1(Volume), 15)` | -2.90 | -2.90 | -2.49 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Volume)` | -3.18 | -2.53 | -3.18 | — | (子树本身) |
| knockout | `ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30)` | -3.47 | -2.40 | -3.47 | +1.83 | `ts_min(ts_min(cross_quantile_q25(day_autocorr_n1(Volume), 15), 50), 50)` |
| knockout | `cross_quantile_q25(day_autocorr_n1(Volume), 15)` | -1.63 | -0.75 | -1.63 | -0.02 | `ts_min(ts_min(ts_regres(day_autocorr_n1(Volume), day_durbin_watson(High), 30), 50), 50)` |
| swap | `Volume->Amt` | -1.81 | -0.81 | -1.81 | — | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Amt), 15), day_durbin_watson(High), 30), 50), 50)` |
| swap | `High->Low` | -1.91 | -0.52 | -1.91 | — | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Low), 30), 50), 50)` |
| window | `ts_min@50->25` | -2.03 | -0.89 | -2.03 | — | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50), 25)` |
| window | `ts_min@50->100` | -1.24 | -0.39 | -1.24 | — | `ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50), 100)` |

### head score -1.90:`ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30)` | -5.84 | -4.38 | -5.84 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(day_autocorr_n1(Volume), 15)` | -2.90 | -2.90 | -2.49 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Volume)` | -3.18 | -2.53 | -3.18 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Ret)` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| knockout | `ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30)` | -3.26 | -2.56 | -3.26 | +1.36 | `ts_min(cross_quantile_q25(day_autocorr_n1(Volume), 15), 50)` |
| knockout | `cross_quantile_q25(day_autocorr_n1(Volume), 15)` | -1.79 | -0.38 | -1.79 | -0.11 | `ts_min(ts_regres(day_autocorr_n1(Volume), day_durbin_watson(Ret), 30), 50)` |
| swap | `Volume->Amt` | -1.49 | -0.67 | -1.49 | — | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Amt), 15), day_durbin_watson(Ret), 30), 50)` |
| window | `ts_min@50->25` | -1.63 | -1.63 | -1.46 | — | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 25)` |
| window | `ts_min@50->100` | -1.32 | -0.32 | -1.32 | — | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 100)` |

### head score -1.95:`ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30)` | -3.66 | -3.66 | -2.99 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15)` | -2.97 | -2.97 | -2.79 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(day_autocorr_n1(Volume), 15)` | -2.90 | -2.90 | -2.49 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Volume)` | -3.18 | -2.53 | -3.18 | — | (子树本身) |
| knockout | `ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30)` | -3.37 | -2.55 | -3.37 | +1.42 | `ts_min(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), 50)` |
| knockout | `cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15)` | -2.51 | -1.42 | -2.51 | +0.56 | `ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50)` |
| swap | `Volume->Amt` | -1.89 | -1.41 | -1.89 | — | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Amt), 15), 15), day_durbin_watson(High), 30), 50)` |
| swap | `High->Low` | -2.39 | -1.53 | -2.39 | — | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(Low), 30), 50)` |
| window | `ts_min@50->25` | -3.52 | -1.96 | -3.52 | — | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30), 25)` |
| window | `ts_min@50->100` | -1.73 | -0.78 | -1.73 | — | `ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)` — enrichment,均值差 +1.39,p 0.000
2. `cross_regbeta(day_last(Amt), day_open(Amt), 10)` — enrichment,均值差 +1.36,p 0.001
3. `cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10))` — enrichment,均值差 +1.27,p 0.002
4. `cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)), 10)` — enrichment,均值差 +1.26,p 0.006
5. `day_open(Amt)` — enrichment,均值差 +1.21,p 0.000
6. `sub(day_wmean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +1.20,p 0.000
7. `cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap)` — enrichment,均值差 +1.17,p 0.023
8. `cross_min(day_last(Close), 482)` — enrichment,均值差 +1.16,p 0.000
9. `cross_mean(day_last(Close), 10)` — enrichment,均值差 +1.11,p 0.002
10. `cross_min(cross_mean(day_last(Close), 10), 482)` — enrichment,均值差 +1.11,p 0.002
11. `day_last(Amt)` — enrichment,均值差 +1.09,p 0.000
12. `sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares))` — enrichment,均值差 +1.09,p 0.008
13. `day_wmean(Ret, Amt)` — enrichment,均值差 +1.08,p 0.000
14. `cross_mean(LogFloatShares, 10)` — enrichment,均值差 +0.97,p 0.000
15. `cross_min(cross_mean(LogFloatShares, 10), 482)` — enrichment,均值差 +0.93,p 0.000
16. `day_mean(Ret)` — enrichment,均值差 +0.93,p 0.000
17. `sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))` — enrichment,均值差 +0.91,p 0.000
18. `day_last(Close)` — enrichment,均值差 +0.85,p 0.000
19. `sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)` — enrichment,均值差 +0.83,p 0.019
20. `log(day_last(Close))` — enrichment,均值差 +0.78,p 0.000
21. `sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482))` — enrichment,均值差 +0.71,p 0.031
22. `cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)` — enrichment,均值差 +0.70,p 0.001
23. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.64,p 0.000
24. `sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +0.62,p 0.000
25. `cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10)` — enrichment,均值差 +0.58,p 0.001

## 本组之前各轮的任务

- `prods2038Pr1a_Na`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.52(train -0.52 valid -0.51):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))), LogFloatCap)`
  - score -0.75(train -0.61 valid -0.75):`cs_bucket_demean(sub(div(cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(LogFloatShares, 482)), LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(LogFloatShares, 482))), LogFloatCap)`
  - score -0.94(train -0.94 valid -0.85):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))), LogFloatCap)`
  - score -0.99(train -0.99 valid -0.83):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(cross_mean(LogFloatShares, 10), 10), 482)), LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(cross_mean(LogFloatShares, 10), 10), 482))), LogFloatCap)`
  - score -1.04(train -0.59 valid -1.04):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 241), cross_min(cross_mean(LogFloatShares, 10), 482))), LogFloatCap)`
- `prods2038Pr1b_Nb`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 19}
  - score +0.48(train +0.75 valid +0.48):`cs_first_low20(day_last(Amt), LogFloatShares)`
  - score +0.48(train +0.75 valid +0.48):`cs_first_low20(cs_first_low20(day_last(Amt), LogFloatShares), LogFloatShares)`
  - score -0.09(train +0.02 valid -0.09):`cross_ema(cs_rank(cross_regbeta(day_last(Amt), cs_last_low10(day_autocorr_n1(Close), day_q_stat_std(Ret)), 10)), 60)`
  - score -0.18(train -0.18 valid +0.01):`cross_ema(cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 241)`
  - score -0.33(train -0.33 valid -0.27):`cs_first_low20(day_last(Amt), cs_first_low20(day_last(Amt), LogFloatShares))`
- `prods2038Pr2a_I0_open_search`:核心 `—`;评分 80,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.19(train -0.13 valid -0.19):`cs_first_low20(ts_stddev(LogTotalCap, 5), day_quantile(abs_(neg(High))))`
  - score -0.93(train +0.07 valid -0.93):`cs_first_low20(day_autocorr_n1(Low), cross_product(cross_product(day_autocorr_n1(Low), 30), 30))`
  - score -0.96(train +0.13 valid -0.96):`cs_first_low20(ts_stddev(LogTotalCap, 5), cross_product(cross_product(day_autocorr_n1(Low), 30), 30))`
  - score -1.00(train -0.09 valid -1.00):`cs_first_low20(ts_stddev(LogTotalCap, 5), cross_product(day_autocorr_n1(Low), 30))`
  - score -1.06(train -0.10 valid -1.06):`cs_first_low20(cross_product(day_autocorr_n1(Low), 30), cross_product(cross_product(day_autocorr_n1(Low), 30), 30))`
- `prods2038Pr2b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score +0.23(train +0.23 valid +0.24):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241), LogFloatCap)))`
  - score -0.15(train -0.15 valid +0.03):`cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap)))`
  - score -0.17(train -0.15 valid -0.17):`cs_mask_top_replace_mean_neg(cs_bucket_rank(cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap), LogFloatCap))`
  - score -0.19(train -0.16 valid -0.19):`cs_mask_top_replace_mean_neg(cs_bucket_rank(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120), LogFloatCap))`
  - score -0.26(train -0.05 valid -0.26):`cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.58(window ts_min@50->100):`ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 100)`
- 增益 +0.41(swap Volume->Amt):`ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Amt), 15), day_durbin_watson(Ret), 30), 50)`
- 增益 +0.41(window ts_min@50->100):`ts_min(ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(High), 30), 50), 100)`
- 增益 +0.27(window ts_min@50->25):`ts_min(ts_regres(cross_quantile_q25(day_autocorr_n1(Volume), 15), day_durbin_watson(Ret), 30), 25)`
- 增益 +0.22(window ts_min@50->100):`ts_min(ts_regres(cross_quantile_q25(cross_quantile_q25(day_autocorr_n1(Volume), 15), 15), day_durbin_watson(High), 30), 100)`
- 增益 +0.11(knockout cross_quantile_q25(day_autocorr_n1(Volume), 15)):`ts_min(ts_regres(day_autocorr_n1(Volume), day_durbin_watson(Ret), 30), 50)`
