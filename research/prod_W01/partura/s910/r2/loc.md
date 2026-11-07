# 定位:种子 910,P 组,第 2 轮(只含 train / valid)

快照:prods910M1_I0_open_search, prods910M2_I0_open_search, prods910Pr1a_Na, prods910Pr1b_Eb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.85 | +1.85 | +2.58 | -1 | 5 | prods910M1_I0_open_search | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |
| +1.53 | +1.53 | +2.40 | -1 | 20 | prods910Pr1b_Eb | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))` |
| +1.42 | +1.42 | +2.62 | -1 | 5 | prods910M1_I0_open_search | `cs_first_low20(cs_first_low20(LogFloatCap, day_last(High)), ListAge)` |
| +1.34 | +1.34 | +2.50 | +1 | 0 | prods910Pr1a_Na | `cs_first_low20(cross_mean(LogFloatCap, 60), cross_mean(day_sum(Amt), 60))` |
| +0.89 | +0.89 | +1.59 | -1 | 5 | prods910Pr1a_Na | `cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)` |
| +0.83 | +0.83 | +2.26 | -1 | 5 | prods910Pr1a_Na | `cs_first_low20(cross_mean(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| +0.80 | +0.80 | +1.83 | -1 | 20 | prods910Pr1b_Eb | `cs_first_low20(cs_first_high20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_stddev(log(ts_regres(day_skew(Ret), cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 10)), 10))` |
| +0.76 | +0.83 | +0.76 | +1 | 20 | prods910Pr1a_Na | `cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), day_sum(Amt))` |
| +0.72 | +0.72 | +1.21 | +1 | 5 | prods910Pr1a_Na | `cs_first_low20(cross_mean(day_sum(Amt), 60), cross_mean(day_es_ratio_lo(Amt), 60))` |
| +0.55 | +0.55 | +3.11 | -1 | 5 | prods910Pr1b_Eb | `cs_first_low20(cs_first_high20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_delta(log(LogFloatCap), 60))` |

## 共性:371 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.29 | 0.000 | 9 | +1.52 / -0.76 | `ts_quantile_q75(LogFloatCap, 10)` |
| +2.05 | 0.004 | 5 | +1.32 / -0.73 | `cross_fangzheng(ts_quantile_q75(LogFloatCap, 10), 3)` |
| +2.05 | 0.004 | 4 | +1.32 / -0.73 | `cross_fangzheng(LogFloatCap, 3)` |
| +2.04 | 0.001 | 6 | +1.30 / -0.74 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 1)` |
| +1.57 | 0.003 | 9 | +0.82 / -0.75 | `cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3)` |
| +1.42 | 0.022 | 4 | +0.69 / -0.72 | `pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))` |
| +1.42 | 0.022 | 4 | +0.69 / -0.72 | `cs_regres(day_q_stat_std(Amt), day_hurst(Close))` |
| +1.42 | 0.022 | 4 | +0.69 / -0.72 | `pow_05(cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))))` |
| +1.42 | 0.022 | 4 | +0.69 / -0.72 | `cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close))))` |
| +1.29 | 0.066 | 4 | +0.57 / -0.72 | `cs_first_low20(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), ts_quantile_q75(LogFloatCap, 1))` |
| +1.28 | 0.035 | 4 | +0.56 / -0.72 | `cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60))` |
| +1.28 | 0.035 | 4 | +0.56 / -0.72 | `pow_2(cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60)))` |
| +1.19 | 0.000 | 106 | +0.14 / -1.05 | `ts_quantile_q75(LogFloatCap, 1)` |
| +1.17 | 0.020 | 6 | +0.45 / -0.73 | `day_q_stat_std(Amt)` |
| +1.16 | 0.000 | 21 | +0.38 / -0.77 | `day_hurst(Close)` |
| +1.12 | 0.015 | 6 | +0.39 / -0.73 | `cs_first_high40(day_durbin_watson(Amt), day_hurst(Close))` |
| +1.11 | 0.013 | 7 | +0.38 / -0.73 | `neg(LogFloatCap)` |
| +1.10 | 0.028 | 5 | +0.38 / -0.72 | `day_sum(Open)` |
| +1.10 | 0.028 | 5 | +0.38 / -0.72 | `cs_robust_z(day_sum(Open))` |
| +1.09 | 0.050 | 4 | +0.38 / -0.72 | `cs_first_low40(sqrt(day_quantile_q25(Open)), day_sum(High))` |

## 拆解(27 次评估)

### head score +1.53:`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` | +1.85 | +1.85 | +2.58 | — | (子树本身) |
| sufficiency | `pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close)))))` | -5.04 | -4.51 | -5.04 | — | (子树本身) |
| sufficiency | `cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3)` | -4.83 | -3.32 | -4.83 | — | (子树本身) |
| sufficiency | `cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))` | -5.04 | -4.52 | -5.04 | — | (子树本身) |
| knockout | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` | -4.37 | -4.13 | -4.37 | +5.91 | `cs_last_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))` |
| knockout | `pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close)))))` | +1.54 | +1.54 | +2.39 | -0.00 | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close)))))` |
| knockout | `cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3)` | +1.50 | +1.50 | +2.46 | +0.03 | `cs_last_low20(cs_first_low20(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))` |
| knockout | `cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))` | +1.19 | +1.19 | +1.66 | +0.35 | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(day_skew(Ret)))` |
| swap | `Close->Vwap` | — | — | — | — | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Vwap))))))` |
| window | `cross_fangzheng@3->2` | +1.54 | +1.54 | +2.41 | — | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 2), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))` |
| window | `cross_fangzheng@3->6` | +1.55 | +1.55 | +2.34 | — | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 6), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))` |

### head score +1.42:`cs_first_low20(cs_first_low20(LogFloatCap, day_last(High)), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(LogFloatCap, day_last(High))` | +0.63 | +0.63 | +1.95 | — | (子树本身) |
| sufficiency | `day_last(High)` | -1.34 | -1.34 | -0.40 | — | (子树本身) |
| knockout | `cs_first_low20(LogFloatCap, day_last(High))` | +0.12 | +0.12 | +2.38 | +1.30 | `cs_first_low20(LogFloatCap, ListAge)` |
| swap | `High->Low` | +1.42 | +1.42 | +2.62 | — | `cs_first_low20(cs_first_low20(LogFloatCap, day_last(Low)), ListAge)` |

### head score +1.34:`cs_first_low20(cross_mean(LogFloatCap, 60), cross_mean(day_sum(Amt), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_sum(Amt), 60)` | -1.01 | -1.01 | -0.30 | — | (子树本身) |
| sufficiency | `cross_mean(LogFloatCap, 60)` | -2.74 | -2.20 | -2.74 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `cross_mean(day_sum(Amt), 60)` | -0.63 | -0.63 | -0.06 | +1.98 | `cs_first_low20(cross_mean(LogFloatCap, 60), day_sum(Amt))` |
| knockout | `cross_mean(LogFloatCap, 60)` | +1.34 | +1.34 | +2.54 | +0.00 | `cs_first_low20(LogFloatCap, cross_mean(day_sum(Amt), 60))` |
| swap | `Amt->Volume` | +1.10 | +1.10 | +2.97 | — | `cs_first_low20(cross_mean(LogFloatCap, 60), cross_mean(day_sum(Volume), 60))` |
| window | `cross_mean@60->30` | +1.33 | +1.33 | +2.52 | — | `cs_first_low20(cross_mean(LogFloatCap, 30), cross_mean(day_sum(Amt), 60))` |
| window | `cross_mean@60->120` | +1.28 | +1.28 | +2.54 | — | `cs_first_low20(cross_mean(LogFloatCap, 120), cross_mean(day_sum(Amt), 60))` |

### head score +0.89:`cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low10(neg(LogFloatCap), LogFloatCap)` | +0.66 | +0.66 | +1.26 | — | (子树本身) |
| sufficiency | `neg(LogFloatCap)` | -5.03 | -3.60 | -5.03 | — | (子树本身) |
| knockout | `cs_last_low10(neg(LogFloatCap), LogFloatCap)` | +0.88 | +0.88 | +1.61 | +0.02 | `cs_bucket_rank(neg(LogFloatCap), LogFloatCap)` |
| knockout | `neg(LogFloatCap)` | +0.88 | +0.88 | +1.61 | +0.02 | `cs_bucket_rank(cs_last_low10(LogFloatCap, LogFloatCap), LogFloatCap)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` — ablation,自身 score +1.85(所在 head +1.53)
2. `cs_last_low10(neg(LogFloatCap), LogFloatCap)` — ablation,自身 score +0.66(所在 head +0.89)
3. `ts_quantile_q75(LogFloatCap, 10)` — enrichment,均值差 +2.29,p 0.000
4. `cross_fangzheng(ts_quantile_q75(LogFloatCap, 10), 3)` — enrichment,均值差 +2.05,p 0.004
5. `cross_fangzheng(LogFloatCap, 3)` — enrichment,均值差 +2.05,p 0.004
6. `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 1)` — enrichment,均值差 +2.04,p 0.001
7. `cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3)` — enrichment,均值差 +1.57,p 0.003
8. `pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))` — enrichment,均值差 +1.42,p 0.022
9. `cs_regres(day_q_stat_std(Amt), day_hurst(Close))` — enrichment,均值差 +1.42,p 0.022
10. `pow_05(cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))))` — enrichment,均值差 +1.42,p 0.022
11. `cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close))))` — enrichment,均值差 +1.42,p 0.022
12. `cs_first_low20(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), ts_quantile_q75(LogFloatCap, 1))` — enrichment,均值差 +1.29,p 0.066
13. `cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60))` — enrichment,均值差 +1.28,p 0.035
14. `pow_2(cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60)))` — enrichment,均值差 +1.28,p 0.035
15. `ts_quantile_q75(LogFloatCap, 1)` — enrichment,均值差 +1.19,p 0.000
16. `day_q_stat_std(Amt)` — enrichment,均值差 +1.17,p 0.020
17. `day_hurst(Close)` — enrichment,均值差 +1.16,p 0.000
18. `cs_first_high40(day_durbin_watson(Amt), day_hurst(Close))` — enrichment,均值差 +1.12,p 0.015
19. `neg(LogFloatCap)` — enrichment,均值差 +1.11,p 0.013
20. `day_sum(Open)` — enrichment,均值差 +1.10,p 0.028
21. `cs_robust_z(day_sum(Open))` — enrichment,均值差 +1.10,p 0.028
22. `cs_first_low40(sqrt(day_quantile_q25(Open)), day_sum(High))` — enrichment,均值差 +1.09,p 0.050
23. `sqrt(day_sum(High))` — enrichment,均值差 +1.09,p 0.081
24. `pow_05(cs_first_high40(day_durbin_watson(Amt), day_hurst(Close)))` — enrichment,均值差 +1.07,p 0.030
25. `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` — enrichment,均值差 +1.06,p 0.000
26. `cs_first_high20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` — enrichment,均值差 +1.04,p 0.033
27. `day_durbin_watson(Amt)` — enrichment,均值差 +1.01,p 0.002
28. `log(ts_regres(day_skew(Ret), day_autocorr_n1(Ret), 10))` — enrichment,均值差 +0.92,p 0.068
29. `ts_delta(log(ts_regres(day_skew(Ret), day_autocorr_n1(Ret), 10)), 60)` — enrichment,均值差 +0.92,p 0.068
30. `ts_quantile_q75(ts_quantile_q75(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 1), 1)` — enrichment,均值差 +0.81,p 0.081
31. `ts_quantile_q75(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 1)` — enrichment,均值差 +0.81,p 0.081
32. `ts_regres(day_skew(Ret), day_autocorr_n1(Ret), 10)` — enrichment,均值差 +0.81,p 0.037
33. `day_skew(Ret)` — enrichment,均值差 +0.71,p 0.015
34. `cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3)` — enrichment,均值差 +0.71,p 0.000
35. `cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3)` — enrichment,均值差 +0.66,p 0.000
36. `cross_mean(day_sum(Amt), 60)` — enrichment,均值差 +0.66,p 0.087
37. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +0.47,p 0.085
38. `day_autocorr_n1(Ret)` — enrichment,均值差 +0.44,p 0.069

## 本组之前各轮的任务

- `prods910Pr1a_Na`:核心 `—`;评分 89,过线 10,入 heads 5;采样计数 {}
  - score +1.34(train +1.34 valid +2.50):`cs_first_low20(cross_mean(LogFloatCap, 60), cross_mean(day_sum(Amt), 60))`
  - score +0.89(train +0.89 valid +1.59):`cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)`
  - score +0.89(train +0.89 valid +1.59):`cs_bucket_rank(cs_last_low10(neg(LogFloatCap), cs_last_low10(neg(LogFloatCap), LogFloatCap)), LogFloatCap)`
  - score +0.88(train +0.88 valid +1.61):`cs_bucket_rank(LogFloatCap, LogFloatCap)`
  - score +0.83(train +0.83 valid +2.26):`cs_first_low20(cross_mean(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))`
- `prods910Pr1b_Eb`:核心 `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))`;评分 113,过线 29,入 heads 3;采样计数 {'c05_no_core': 1960, 'c05_skeleton': 8, 'mutation_refused': 3}
  - score +1.53(train +1.53 valid +2.40):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))`
  - score +1.46(train +1.46 valid +2.31):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_first_high40(day_centroid(Close), day_hurst(Close))))`
  - score +1.46(train +1.46 valid +2.46):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_last_high20(day_durbin_watson(Amt), day_hurst(Close))))`
  - score +1.39(train +1.39 valid +2.16):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), pow_05(cs_regres(day_skew(Ret), day_hurst(Volume))))))`
  - score +1.36(train +1.36 valid +2.16):`cs_last_low20(cs_first_low20(cross_fangzheng(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_first_high40(day_centroid(Close), day_zero_ratio(Close))))`

## 比原 head 好的拆解变体(R 候选)

(没有)
