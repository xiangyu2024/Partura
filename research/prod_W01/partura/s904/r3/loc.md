# 定位:种子 904,P 组,第 3 轮(只含 train / valid)

快照:prods904M1_I0_open_search, prods904M2_I0_open_search, prods904M3_I0_open_search, prods904Pr1a_Ea, prods904Pr1b_Nb, prods904Pr2a_Ea, prods904Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.27 | +1.46 | +1.27 | +1 | 0 | prods904M3_I0_open_search | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_1_5(day_var(High)), 30)), 241)` |
| +0.97 | +0.97 | +1.30 | +1 | 20 | prods904Pr2a_Ea | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))` |
| +0.92 | +0.97 | +0.92 | +1 | 5 | prods904M2_I0_open_search | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` |
| +0.80 | +0.80 | +1.68 | +1 | 20 | prods904Pr2a_Ea | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))` |
| +0.60 | +0.60 | +1.15 | +1 | 0 | prods904M3_I0_open_search | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30)), 241)` |
| +0.59 | +0.59 | +0.68 | +1 | 5 | prods904M3_I0_open_search | `cross_corr(ts_delay(ts_med(day_distinct_ratio(Amt), 30), 50), pow_2(ts_decay_linear(pow_2_5(day_var(High)), 30)), 241)` |
| +0.52 | +0.52 | +1.31 | +1 | 5 | prods904Pr2a_Ea | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Amt, Amt), 60), 60))), 0.65))` |

## 共性:571 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.31 | 0.000 | 5 | +0.90 / -1.41 | `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)` |
| +2.31 | 0.000 | 5 | +0.90 / -1.41 | `cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))` |
| +1.71 | 0.000 | 9 | +0.30 / -1.41 | `cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30))` |
| +1.69 | 0.000 | 10 | +0.28 / -1.42 | `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)` |
| +1.31 | 0.000 | 39 | -0.17 / -1.48 | `cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50))` |
| +1.29 | 0.011 | 4 | -0.11 / -1.40 | `day_topw_mean(Ret, Volume)` |
| +1.29 | 0.011 | 4 | -0.11 / -1.40 | `cross_zscore(day_topw_mean(Ret, Volume), 60)` |
| +1.21 | 0.000 | 34 | -0.25 / -1.46 | `cross_zscore(day_topw_mean(Ret, Amt), 60)` |
| +1.15 | 0.003 | 6 | -0.25 / -1.40 | `day_topw_mean(Amt, Amt)` |
| +1.09 | 0.008 | 6 | -0.31 / -1.40 | `cs_first_low40(day_var(High), day_var(High))` |
| +1.06 | 0.000 | 16 | -0.36 / -1.42 | `div(cs_robust_z(day_mean(Low)), day_first(Open))` |
| +1.04 | 0.000 | 12 | -0.37 / -1.41 | `log(div(cs_robust_z(day_mean(Low)), day_first(Open)))` |
| +1.03 | 0.000 | 17 | -0.39 / -1.42 | `cs_robust_z(day_mean(Low))` |
| +0.98 | 0.001 | 16 | -0.43 / -1.41 | `pow_2_5(day_var(High))` |
| +0.97 | 0.000 | 55 | -0.51 / -1.48 | `day_var(High)` |
| +0.94 | 0.000 | 47 | -0.53 / -1.46 | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` |
| +0.87 | 0.000 | 20 | -0.54 / -1.42 | `day_mean(Low)` |
| +0.85 | 0.004 | 14 | -0.55 / -1.41 | `ts_decay_linear(pow_2_5(day_var(High)), 30)` |
| +0.84 | 0.007 | 13 | -0.57 / -1.41 | `pow_2(ts_decay_linear(pow_2_5(day_var(High)), 30))` |
| +0.84 | 0.000 | 72 | -0.65 / -1.49 | `day_kurt(Vwap)` |

## 拆解(43 次评估)

### head score +1.27:`cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_1_5(day_var(High)), 30)), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(ts_decay_linear(pow_1_5(day_var(High)), 30))` | -1.09 | -1.09 | -0.57 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_1_5(day_var(High)), 30)` | -1.09 | -1.09 | -0.57 | — | (子树本身) |
| sufficiency | `pow_1_5(day_var(High))` | -1.30 | -1.30 | -0.45 | — | (子树本身) |
| sufficiency | `day_var(High)` | -1.30 | -1.30 | -0.45 | — | (子树本身) |
| knockout | `pow_2(ts_decay_linear(pow_1_5(day_var(High)), 30))` | +0.99 | +1.04 | +0.99 | +0.28 | `cross_corr(LogFloatCap, ts_decay_linear(pow_1_5(day_var(High)), 30), 241)` |
| knockout | `ts_decay_linear(pow_1_5(day_var(High)), 30)` | -0.09 | -0.09 | +1.58 | +1.36 | `cross_corr(LogFloatCap, pow_2(pow_1_5(day_var(High))), 241)` |
| knockout | `pow_1_5(day_var(High))` | +0.77 | +1.15 | +0.77 | +0.50 | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(day_var(High), 30)), 241)` |
| swap | `High->Low` | +1.16 | +1.28 | +1.16 | — | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_1_5(day_var(Low)), 30)), 241)` |
| window | `cross_corr@241->120` | -0.32 | +0.09 | -0.32 | — | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_1_5(day_var(High)), 30)), 120)` |
| window | `cross_corr@241->482` | +0.51 | +0.51 | +1.10 | — | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_1_5(day_var(High)), 30)), 482)` |

### head score +0.97:`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)))` | +0.12 | +0.12 | +1.04 | — | (子树本身) |
| sufficiency | `cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))` | +0.12 | +0.12 | +1.04 | — | (子树本身) |
| sufficiency | `cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50))` | +0.89 | +0.89 | +0.89 | — | (子树本身) |
| sufficiency | `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)` | +0.12 | +0.12 | +1.04 | — | (子树本身) |
| knockout | `mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65)` | +0.83 | +0.83 | +1.28 | +0.14 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))))` |
| knockout | `cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)))` | +0.93 | +0.93 | +1.24 | +0.04 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)), 0.65))` |
| knockout | `mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35)` | +0.62 | +0.84 | +0.62 | +0.35 | `add(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))` |
| swap | `Volume->Amt` | +0.93 | +0.93 | +1.24 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Amt), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))` |
| swap | `Vwap->Close` | +0.89 | +0.89 | +1.24 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Close), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))` |
| window | `ts_regbeta@50->25` | +0.64 | +0.64 | +1.07 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 25)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))` |
| window | `ts_regbeta@50->100` | +0.98 | +0.98 | +1.53 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 100)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))` |

### head score +0.80:`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30))` | -0.44 | -0.44 | +0.56 | — | (子树本身) |
| sufficiency | `cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50))` | +0.89 | +0.89 | +0.89 | — | (子树本身) |
| sufficiency | `cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)` | -0.44 | -0.44 | +0.56 | — | (子树本身) |
| sufficiency | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` | +0.92 | +0.97 | +0.92 | — | (子树本身) |
| knockout | `mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65)` | +0.27 | +0.27 | +1.67 | +0.53 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)))` |
| knockout | `mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35)` | +1.23 | +1.23 | +1.52 | -0.43 | `add(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))` |
| knockout | `cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30))` | +1.08 | +1.08 | +1.33 | -0.28 | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30), 0.65))` |
| knockout | `cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50))` | +0.93 | +0.93 | +1.00 | -0.14 | `add(mul(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))` |
| swap | `Volume->Amt` | +0.92 | +0.92 | +1.55 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Amt), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Amt), 60), 30)), 0.65))` |
| swap | `Vwap->Close` | +0.98 | +0.98 | +1.71 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Close), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))` |
| window | `ts_regbeta@50->25` | +0.24 | +0.24 | +1.42 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 25)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))` |
| window | `ts_regbeta@50->100` | +0.84 | +0.84 | +1.53 | — | `add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 100)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))` |

### head score +0.60:`cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30)), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30))` | -1.03 | -1.03 | -0.60 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30)` | -1.07 | -1.07 | -0.54 | — | (子树本身) |
| sufficiency | `pow_2_5(pow_2_5(day_var(High)))` | -1.30 | -1.30 | -0.45 | — | (子树本身) |
| sufficiency | `pow_2_5(day_var(High))` | -1.30 | -1.30 | -0.45 | — | (子树本身) |
| knockout | `pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30))` | +0.48 | +0.48 | +1.45 | +0.12 | `cross_corr(LogFloatCap, ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30), 241)` |
| knockout | `ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30)` | +0.20 | +0.20 | +0.86 | +0.40 | `cross_corr(LogFloatCap, pow_2(pow_2_5(pow_2_5(day_var(High)))), 241)` |
| knockout | `pow_2_5(pow_2_5(day_var(High)))` | +0.78 | +0.78 | +1.42 | -0.18 | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(day_var(High)), 30)), 241)` |
| swap | `High->Low` | +0.33 | +0.33 | +1.44 | — | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(Low))), 30)), 241)` |
| window | `cross_corr@241->120` | +0.12 | +0.12 | +0.36 | — | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30)), 120)` |
| window | `cross_corr@241->482` | +0.69 | +0.69 | +0.83 | — | `cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(pow_2_5(day_var(High))), 30)), 482)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` — ablation,自身 score +0.92(所在 head +0.80)
2. `cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50))` — ablation,自身 score +0.89(所在 head +0.97)
3. `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)` — enrichment,均值差 +2.31,p 0.000
4. `cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))` — enrichment,均值差 +2.31,p 0.000
5. `cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30))` — enrichment,均值差 +1.71,p 0.000
6. `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)` — enrichment,均值差 +1.69,p 0.000
7. `day_topw_mean(Ret, Volume)` — enrichment,均值差 +1.29,p 0.011
8. `cross_zscore(day_topw_mean(Ret, Volume), 60)` — enrichment,均值差 +1.29,p 0.011
9. `cross_zscore(day_topw_mean(Ret, Amt), 60)` — enrichment,均值差 +1.21,p 0.000
10. `day_topw_mean(Amt, Amt)` — enrichment,均值差 +1.15,p 0.003
11. `cs_first_low40(day_var(High), day_var(High))` — enrichment,均值差 +1.09,p 0.008
12. `div(cs_robust_z(day_mean(Low)), day_first(Open))` — enrichment,均值差 +1.06,p 0.000
13. `log(div(cs_robust_z(day_mean(Low)), day_first(Open)))` — enrichment,均值差 +1.04,p 0.000
14. `cs_robust_z(day_mean(Low))` — enrichment,均值差 +1.03,p 0.000
15. `pow_2_5(day_var(High))` — enrichment,均值差 +0.98,p 0.001
16. `day_var(High)` — enrichment,均值差 +0.97,p 0.000
17. `day_mean(Low)` — enrichment,均值差 +0.87,p 0.000
18. `ts_decay_linear(pow_2_5(day_var(High)), 30)` — enrichment,均值差 +0.85,p 0.004
19. `pow_2(ts_decay_linear(pow_2_5(day_var(High)), 30))` — enrichment,均值差 +0.84,p 0.007
20. `day_kurt(Vwap)` — enrichment,均值差 +0.84,p 0.000
21. `sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))` — enrichment,均值差 +0.77,p 0.070
22. `day_gini(Volume)` — enrichment,均值差 +0.76,p 0.000
23. `ts_delay(ts_med(day_distinct_ratio(Amt), 30), 50)` — enrichment,均值差 +0.65,p 0.001
24. `abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30))` — enrichment,均值差 +0.63,p 0.049
25. `abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40))` — enrichment,均值差 +0.61,p 0.054
26. `pow_05(abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)))` — enrichment,均值差 +0.61,p 0.071
27. `ts_med(day_distinct_ratio(Amt), 30)` — enrichment,均值差 +0.60,p 0.002
28. `day_distinct_ratio(Amt)` — enrichment,均值差 +0.55,p 0.002
29. `cs_first_low40(LogFloatCap, day_var(High))` — enrichment,均值差 +0.54,p 0.028
30. `ts_decay_linear(ts_scale(ts_regalpha(day_centroid(Close), day_argmin(Ret), 40), 50), 30)` — enrichment,均值差 +0.53,p 0.075
31. `ts_scale(ts_regalpha(day_centroid(Close), day_argmin(Ret), 40), 50)` — enrichment,均值差 +0.53,p 0.075
32. `pow_2(ts_decay_linear(ts_scale(ts_regalpha(day_centroid(Close), day_argmin(Ret), 40), 50), 30))` — enrichment,均值差 +0.53,p 0.075
33. `ts_regres(day_gini(Volume), day_kurt(Vwap), 50)` — enrichment,均值差 +0.53,p 0.013
34. `pow_2(ts_decay_linear(pow_2_5(cs_first_low40(LogFloatCap, day_var(High))), 30))` — enrichment,均值差 +0.49,p 0.071
35. `ts_decay_linear(pow_2_5(cs_first_low40(LogFloatCap, day_var(High))), 30)` — enrichment,均值差 +0.49,p 0.071
36. `pow_2_5(cs_first_low40(LogFloatCap, day_var(High)))` — enrichment,均值差 +0.48,p 0.062
37. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.42,p 0.001
38. `ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)` — enrichment,均值差 +0.41,p 0.027
39. `ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)` — enrichment,均值差 +0.31,p 0.037

## 本组之前各轮的任务

- `prods904Pr1a_Ea`:核心 `day_topw_mean(Ret, Amt)`;评分 65,过线 0,入 heads 0;采样计数 {'c05_no_core': 868, 'c05_periphery_seen': 2}
  - score +0.17(train +0.17 valid +0.86):`cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 15)`
  - score +0.12(train +0.12 valid +0.83):`cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 10)`
  - score +0.09(train +0.09 valid +1.08):`cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)`
  - score +0.05(train +0.05 valid +1.15):`cross_ema(cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 15), 15)`
  - score +0.02(train +0.02 valid +2.36):`cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 10), 15), 15)`
- `prods904Pr1b_Nb`:核心 `—`;评分 99,过线 0,入 heads 0;采样计数 {}
  - score +0.29(train +0.29 valid +0.65):`cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), abs_(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)`
  - score -0.01(train -0.01 valid +0.73):`log(div(cs_robust_z(day_mean(Low)), day_first(Open)))`
  - score -0.16(train -0.16 valid +0.10):`cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 10))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)`
  - score -0.21(train -0.21 valid +0.06):`cross_mean(cs_winsor(sub(log(div(day_min(Open), ts_delay(day_last(Close), 1))), log(cs_winsor(sub(log(div(day_min(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open)))))))), 60)`
  - score -0.21(train -0.21 valid -0.02):`cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)`
- `prods904Pr2a_Ea`:核心 `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)`;评分 107,过线 14,入 heads 3;采样计数 {'c05_no_core': 2901, 'c05_skeleton': 3, 'mutation_refused': 2}
  - score +0.97(train +0.97 valid +1.30):`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))`
  - score +0.97(train +0.97 valid +1.30):`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)), 0.65))`
  - score +0.91(train +0.91 valid +1.56):`add(mul(cs_rank(ts_cov(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60))), 0.65))`
  - score +0.83(train +0.83 valid +1.35):`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Volume), 60), 30)), 0.65))`
  - score +0.83(train +1.21 valid +0.83):`mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), cs_rank(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 60)))`
- `prods904Pr2b_Nb`:核心 `—`;评分 70,过线 0,入 heads 0;采样计数 {}
  - score +0.25(train +0.25 valid +0.89):`cross_ema(ts_regres(day_gini(Volume), day_kurt(Vwap), 10), 20)`
  - score -0.18(train -0.18 valid +1.21):`cross_ema(cross_ema(ts_regres(day_gini(Volume), day_kurt(Vwap), 50), 60), 20)`
  - score -0.23(train -0.23 valid +1.04):`cross_ema(ts_regres(day_gini(Volume), day_kurt(Vwap), 50), 30)`
  - score -0.27(train -0.27 valid +0.57):`cross_ema(ts_regres(day_gini(Volume), day_kurt(Vwap), 50), 20)`
  - score -0.27(train -0.27 valid +0.79):`ts_skew(cross_reg_tvalue(day_quantile(Open), day_gini(High), 5), 40)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.43(knockout mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35)):`add(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))`
- 增益 +0.28(knockout cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30))):`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)), 0.35), mul(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30), 0.65))`
- 增益 +0.18(swap Vwap->Close):`add(mul(cs_rank(ts_regbeta(day_gini(Volume), day_kurt(Close), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Volume), 60), 30)), 0.65))`
- 增益 +0.18(knockout pow_2_5(pow_2_5(day_var(High)))):`cross_corr(LogFloatCap, pow_2(ts_decay_linear(pow_2_5(day_var(High)), 30)), 241)`
- 增益 +0.12(swap Volume->Amt):`add(mul(cs_rank(ts_regbeta(day_gini(Amt), day_kurt(Vwap), 50)), 0.35), mul(cs_rank(cross_ema(cross_zscore(day_signed_ratio(Ret, Amt), 60), 30)), 0.65))`
