# 定位:种子 808,P 组,第 3 轮(只含 train / valid)

快照:c07s808M1_I0_open_search, c07s808M2_I0_open_search, c07s808M3_I0_open_search, c08s808Pr1a_Ea, c08s808Pr1b_Nb, c08s808Pr2a_Ea, c08s808Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.30 | +1.36 | +1.30 | -1 | 0 | c08s808Pr1b_Nb | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241)` |
| +1.26 | +1.26 | +1.79 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 50)` |
| +1.09 | +1.09 | +1.53 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` |
| +1.07 | +1.07 | +2.25 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` |
| +0.97 | +0.97 | +0.98 | -1 | 5 | c08s808Pr1a_Ea | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))` |
| +0.83 | +0.83 | +1.39 | +1 | 20 | c08s808Pr2a_Ea | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 20)))` |
| +0.79 | +0.79 | +2.47 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)` |
| +0.58 | +0.58 | +0.84 | -1 | 0 | c08s808Pr2b_Nb | `cross_regbeta(day_cov(Open, Ret), day_wstd(High, Volume), 241)` |
| +0.57 | +0.57 | +0.84 | -1 | 20 | c08s808Pr1b_Nb | `cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 30)` |
| +0.50 | +0.50 | +0.68 | +1 | 0 | c07s808M2_I0_open_search | `cross_sum(cross_autocorr_s1(ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15)), 40), 15)), 40), 15), 60)` |

## 共性:539 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.31 | 0.000 | 4 | +0.89 / -1.42 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` |
| +2.16 | 0.001 | 4 | +0.74 / -1.42 | `day_wstd(Ret, Ret)` |
| +2.12 | 0.000 | 10 | +0.67 / -1.44 | `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` |
| +2.03 | 0.000 | 15 | +0.57 / -1.46 | `cs_demean(day_wstd(Ret, Volume))` |
| +1.47 | 0.003 | 4 | +0.06 / -1.42 | `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15))` |
| +1.47 | 0.003 | 4 | +0.05 / -1.42 | `ts_product(day_wmean(Ret, Volume), 30)` |
| +1.40 | 0.003 | 4 | -0.02 / -1.42 | `day_zero_ratio(Open)` |
| +1.38 | 0.000 | 8 | -0.05 / -1.43 | `cs_rank(ts_max(day_centroid(Volume), 99))` |
| +1.38 | 0.000 | 8 | -0.05 / -1.43 | `ts_max(day_centroid(Volume), 99)` |
| +1.20 | 0.025 | 5 | -0.22 / -1.42 | `cs_rank(ts_mean(day_centroid(Volume), 20))` |
| +1.20 | 0.025 | 5 | -0.22 / -1.42 | `ts_mean(day_centroid(Volume), 20)` |
| +1.08 | 0.000 | 30 | -0.39 / -1.47 | `day_centroid(Volume)` |
| +1.07 | 0.003 | 7 | -0.35 / -1.42 | `cross_autocorr_s1(day_topw_mean(High, Vwap), 5)` |
| +1.07 | 0.003 | 7 | -0.35 / -1.42 | `cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15)` |
| +1.01 | 0.005 | 9 | -0.41 / -1.42 | `cs_rank(ts_min(day_wmean(Ret, Volume), 30))` |
| +1.01 | 0.005 | 9 | -0.41 / -1.42 | `ts_min(day_wmean(Ret, Volume), 30)` |
| +0.99 | 0.040 | 5 | -0.42 / -1.41 | `day_wmean(Vwap, Ret)` |
| +0.99 | 0.001 | 17 | -0.45 / -1.44 | `cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` |
| +0.99 | 0.001 | 17 | -0.45 / -1.44 | `cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120))` |
| +0.95 | 0.015 | 8 | -0.46 / -1.42 | `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15))` |

## 拆解(27 次评估)

### head score +0.83:`sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret)))` | -0.20 | -0.20 | +0.55 | — | (子树本身) |
| sufficiency | `sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))` | -0.20 | -0.20 | +0.55 | — | (子树本身) |
| sufficiency | `cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret)))` | -0.20 | -0.20 | +0.56 | — | (子树本身) |
| sufficiency | `cs_rank(ts_mean(day_centroid(Volume), 20))` | +1.28 | +1.75 | +1.28 | — | (子树本身) |
| knockout | `cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret)))` | -0.02 | -0.02 | +0.80 | +0.85 | `sub(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret)), cs_rank(ts_mean(day_centroid(Volume), 20)))` |
| knockout | `sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))` | +0.83 | +0.83 | +1.40 | +0.00 | `sub(cs_rank(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret)))), cs_rank(ts_mean(day_centroid(Volume), 20)))` |
| knockout | `cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret)))` | +0.83 | +0.83 | +1.39 | -0.00 | `sub(cs_rank(sub(sub(day_wstd(Ret, Volume), day_kurt(Ret)), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 20)))` |
| knockout | `cs_rank(ts_mean(day_centroid(Volume), 20))` | -0.09 | -0.09 | +0.99 | +0.92 | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))), ts_mean(day_centroid(Volume), 20))` |
| swap | `Volume->Amt` | +0.83 | +0.83 | +1.41 | — | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Amt), day_kurt(Ret))), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Amt), 20)))` |
| window | `ts_mean@20->10` | +0.67 | +0.67 | +1.25 | — | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 10)))` |
| window | `ts_mean@20->40` | +0.63 | +0.63 | +1.20 | — | `sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 40)))` |

### head score +0.79:`ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_wstd(Ret, Ret), 50)` | +0.26 | +0.26 | +0.52 | — | (子树本身) |
| sufficiency | `day_wstd(Ret, Ret)` | -3.33 | -2.33 | -3.33 | — | (子树本身) |
| window | `ts_max@50->25` | +0.61 | +0.61 | +1.80 | — | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 25)` |
| window | `ts_max@50->100` | +0.69 | +0.69 | +1.91 | — | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 100)` |

### head score +0.58:`cross_regbeta(day_cov(Open, Ret), day_wstd(High, Volume), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Open, Ret)` | -1.79 | -1.09 | -1.79 | — | (子树本身) |
| sufficiency | `day_wstd(High, Volume)` | -1.26 | -1.26 | -0.49 | — | (子树本身) |
| swap | `Open->Close` | -0.07 | +0.44 | -0.07 | — | `cross_regbeta(day_cov(Close, Ret), day_wstd(High, Volume), 241)` |
| swap | `High->Low` | +0.68 | +0.68 | +1.03 | — | `cross_regbeta(day_cov(Open, Ret), day_wstd(Low, Volume), 241)` |
| window | `cross_regbeta@241->120` | +0.48 | +0.48 | +1.48 | — | `cross_regbeta(day_cov(Open, Ret), day_wstd(High, Volume), 120)` |
| window | `cross_regbeta@241->482` | +0.56 | +0.56 | +1.36 | — | `cross_regbeta(day_cov(Open, Ret), day_wstd(High, Volume), 482)` |

### head score +0.57:`cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Ret, Vwap)` | -5.14 | -3.04 | -5.14 | — | (子树本身) |
| sufficiency | `day_wmean(Vwap, High)` | -1.34 | -1.34 | -0.38 | — | (子树本身) |
| swap | `Vwap->Close` | +0.07 | +0.09 | +0.07 | — | `cross_regbeta(day_cov(Ret, Close), day_wmean(Close, High), 30)` |
| swap | `High->Low` | +0.58 | +0.58 | +0.85 | — | `cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, Low), 30)` |
| window | `cross_regbeta@30->15` | — | — | — | — | `cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 15)` |
| window | `cross_regbeta@30->60` | +0.78 | +0.78 | +1.07 | — | `cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_rank(ts_mean(day_centroid(Volume), 20))` — ablation,自身 score +1.28(所在 head +0.83)
2. `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` — enrichment,均值差 +2.31,p 0.000
3. `day_wstd(Ret, Ret)` — enrichment,均值差 +2.16,p 0.001
4. `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` — enrichment,均值差 +2.12,p 0.000
5. `cs_demean(day_wstd(Ret, Volume))` — enrichment,均值差 +2.03,p 0.000
6. `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15))` — enrichment,均值差 +1.47,p 0.003
7. `ts_product(day_wmean(Ret, Volume), 30)` — enrichment,均值差 +1.47,p 0.003
8. `day_zero_ratio(Open)` — enrichment,均值差 +1.40,p 0.003
9. `cs_rank(ts_max(day_centroid(Volume), 99))` — enrichment,均值差 +1.38,p 0.000
10. `ts_max(day_centroid(Volume), 99)` — enrichment,均值差 +1.38,p 0.000
11. `ts_mean(day_centroid(Volume), 20)` — enrichment,均值差 +1.20,p 0.025
12. `day_centroid(Volume)` — enrichment,均值差 +1.08,p 0.000
13. `cross_autocorr_s1(day_topw_mean(High, Vwap), 5)` — enrichment,均值差 +1.07,p 0.003
14. `cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15)` — enrichment,均值差 +1.07,p 0.003
15. `cs_rank(ts_min(day_wmean(Ret, Volume), 30))` — enrichment,均值差 +1.01,p 0.005
16. `ts_min(day_wmean(Ret, Volume), 30)` — enrichment,均值差 +1.01,p 0.005
17. `day_wmean(Vwap, Ret)` — enrichment,均值差 +0.99,p 0.040
18. `cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` — enrichment,均值差 +0.99,p 0.001
19. `cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120))` — enrichment,均值差 +0.99,p 0.001
20. `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15))` — enrichment,均值差 +0.95,p 0.015
21. `ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15)), 40)` — enrichment,均值差 +0.90,p 0.057
22. `pow_05(pow_05(LogFloatShares))` — enrichment,均值差 +0.87,p 0.005
23. `pow_05(pow_05(pow_05(LogFloatShares)))` — enrichment,均值差 +0.87,p 0.056
24. `day_topw_mean(High, High)` — enrichment,均值差 +0.85,p 0.080
25. `day_kurt(Ret)` — enrichment,均值差 +0.84,p 0.002
26. `sub(day_wstd(Ret, Volume), day_kurt(Ret))` — enrichment,均值差 +0.81,p 0.004
27. `pow_05(LogFloatShares)` — enrichment,均值差 +0.81,p 0.001
28. `cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret)))` — enrichment,均值差 +0.80,p 0.016
29. `day_distinct_ratio(Ret)` — enrichment,均值差 +0.80,p 0.000
30. `ts_max(LogFloatShares, 50)` — enrichment,均值差 +0.69,p 0.034
31. `cross_quantile_q50(LogFloatShares, 60)` — enrichment,均值差 +0.68,p 0.066
32. `day_cov(Open, Ret)` — enrichment,均值差 +0.66,p 0.013
33. `day_wmean(Vwap, High)` — enrichment,均值差 +0.58,p 0.039
34. `day_topw_mean(High, Vwap)` — enrichment,均值差 +0.24,p 0.092

## 本组之前各轮的任务

- `c08s808Pr1a_Ea`:核心 `day_wmean(Ret, Volume)`;评分 92,过线 2,入 heads 1;采样计数 {'c05_no_core': 2618}
  - score +0.97(train +0.97 valid +0.98):`add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))`
  - score +0.54(train +0.54 valid +0.97):`add(cs_rank(ts_max(day_centroid(Volume), 20)), cs_rank(ts_product(add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120))), 30)))`
  - score +0.44(train +1.09 valid +0.44):`day_centroid(Volume)`
  - score +0.33(train +0.33 valid +1.37):`add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(add(cs_rank(ts_max(day_centroid(Volume), 99)), cs_rank(ts_min(day_wmean(Ret, Volume), 30))), 120)))`
  - score +0.32(train +0.32 valid +1.71):`add(cs_rank(ts_max(day_centroid(Volume), 99)), cs_rank(ts_product(day_wmean(Ret, Volume), 30)))`
- `c08s808Pr1b_Nb`:核心 `—`;评分 83,过线 2,入 heads 2;采样计数 {}
  - score +1.30(train +1.36 valid +1.30):`cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241)`
  - score +0.57(train +0.57 valid +0.84):`cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 30)`
  - score +0.40(train +0.40 valid +0.67):`cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, Ret), 30)`
  - score +0.23(train +0.23 valid +1.03):`cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, Ret), 30)`
  - score +0.18(train +0.18 valid +0.93):`cross_regbeta(day_cov(Open, Ret), day_wmean(High, Ret), 30)`
- `c08s808Pr2a_Ea`:核心 `day_wstd(Ret, Volume)`;评分 77,过线 2,入 heads 1;采样计数 {'c05_no_core': 696, 'c05_periphery_seen': 4}
  - score +0.83(train +0.83 valid +1.39):`sub(cs_rank(sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 20)))`
  - score +0.83(train +0.83 valid +1.41):`sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), cs_rank(ts_mean(day_centroid(Volume), 20)))`
  - score +0.45(train +0.45 valid +1.50):`sub(cs_rank(sub(day_wstd(Ret, Volume), day_kurt(Ret))), cs_rank(day_centroid(Volume)))`
  - score +0.38(train +1.08 valid +0.38):`sub(day_wstd(Ret, Volume), cs_rank(ts_mean(day_centroid(Volume), 1)))`
  - score +0.30(train +1.05 valid +0.30):`sub(day_wstd(Ret, Volume), day_centroid(Volume))`
- `c08s808Pr2b_Nb`:核心 `—`;评分 98,过线 1,入 heads 1;采样计数 {'c05_skeleton': 2}
  - score +0.58(train +0.58 valid +0.84):`cross_regbeta(day_cov(Open, Ret), day_wstd(High, Volume), 241)`
  - score +0.17(train +0.17 valid +0.63):`cross_regbeta(day_cov(Vwap, Ret), day_wstd(Ret, Volume), 241)`
  - score +0.10(train +0.10 valid +1.46):`cross_regbeta(day_cov(Open, Ret), day_wstd(Vwap, Open), 241)`
  - score -0.12(train -0.12 valid +1.39):`sqrt(cross_tail_mean_q25(cross_regbeta(sqrt(cross_tail_mean_q25(cross_regbeta(day_cov(Vwap, Ret), day_cov(Ret, Volume), 241), 5)), day_cov(Ret, Volume), 241), 5))`
  - score -0.61(train -0.61 valid -0.06):`sqrt(day_cov(Ret, Volume))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(window cross_regbeta@30->60):`cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 60)`
