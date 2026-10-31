# 定位:种子 802,P 组,第 3 轮(只含 train / valid)

快照:c07s802M1_I0_open_search, c07s802M2_I0_open_search, c07s802M3_I0_open_search, c08s802Pr1a_Ea, c08s802Pr1b_Nb, c08s802Pr2a_Ea, c08s802Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(16 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.70 | +1.72 | +1.70 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 20), signedpower(signedpower(day_centroid(Volume))))` |
| +1.64 | +1.91 | +1.64 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| +1.51 | +1.69 | +1.51 | -1 | 5 | c08s802Pr1a_Ea | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 60)` |
| +1.31 | +1.31 | +1.74 | -1 | 20 | c07s802M1_I0_open_search | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 15))` |
| +1.16 | +1.16 | +1.24 | -1 | 20 | c08s802Pr2a_Ea | `ts_cov(LogTotalCap, day_centroid(Volume), 40)` |
| +1.00 | +1.00 | +1.42 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(ts_reg_fvalue(ts_mean(cross_argmax(day_hurst(Volume), 3), 50), cs_stddev_full(cross_mean(day_min(High), 30)), 5), 241), 20), day_centroid(Volume))` |
| +1.00 | +1.00 | +1.66 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(day_centroid(Volume), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(day_centroid(Volume), 20), day_centroid(Volume)))` |
| +0.86 | +0.86 | +1.79 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))))` |
| +0.83 | +0.83 | +1.13 | +1 | 5 | c08s802Pr2a_Ea | `ts_cov(cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_centroid(Volume)), day_centroid(Volume), 50)` |
| +0.81 | +0.81 | +1.47 | +1 | 5 | c08s802Pr1a_Ea | `ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)` |
| +0.81 | +0.81 | +1.31 | -1 | 5 | c08s802Pr2a_Ea | `ts_cov(LogTotalCap, cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_centroid(Volume)), 50)` |
| +0.75 | +0.75 | +0.94 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 10), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 10), 20), day_centroid(Volume)))` |
| +0.70 | +0.70 | +1.20 | +1 | 20 | c08s802Pr1a_Ea | `cross_regbeta(day_sum(Volume), ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 30), 20)` |
| +0.70 | +0.70 | +1.00 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), 20), day_centroid(Volume))` |
| +0.61 | +0.61 | +0.61 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cs_regres(pow_05(cs_last_low10(day_hurst(Close), day_max(High))), signedpower(cs_last_low40(day_topw_mean(Ret, High), LimitWidth))), 20), day_centroid(Volume))` |
| +0.61 | +0.61 | +2.79 | +1 | 5 | c07s802M3_I0_open_search | `cs_first_low20(day_last(Close), cs_first_low20(day_last(Close), day_quantile_q25(High)))` |

## 共性:514 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.04 | 0.001 | 5 | +0.99 / -1.05 | `cross_quantile_q25(day_centroid(Volume), 241)` |
| +2.04 | 0.001 | 5 | +0.99 / -1.05 | `ts_argmin(cross_quantile_q25(day_centroid(Volume), 241), 20)` |
| +1.99 | 0.000 | 6 | +0.94 / -1.06 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))` |
| +1.96 | 0.000 | 16 | +0.87 / -1.09 | `cross_quantile_q25(signedpower(day_centroid(Volume)), 241)` |
| +1.95 | 0.000 | 13 | +0.87 / -1.08 | `ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20)` |
| +1.61 | 0.000 | 33 | +0.48 / -1.14 | `signedpower(day_centroid(Volume))` |
| +1.60 | 0.003 | 4 | +0.56 / -1.04 | `day_mean(neg(neg(in_delta(Volume, 5))))` |
| +1.51 | 0.003 | 8 | +0.46 / -1.06 | `signedpower(signedpower(day_centroid(Volume)))` |
| +1.34 | 0.006 | 5 | +0.30 / -1.05 | `day_mean(in_delta(Volume, 5))` |
| +1.32 | 0.000 | 11 | +0.26 / -1.06 | `day_quantile_q25(Close)` |
| +1.27 | 0.026 | 5 | +0.22 / -1.04 | `ts_decay_linear(day_quantile(Close), 20)` |
| +1.16 | 0.000 | 16 | +0.09 / -1.07 | `day_mean(neg(in_delta(Volume, 60)))` |
| +1.13 | 0.000 | 15 | +0.06 / -1.07 | `day_quantile(Close)` |
| +1.11 | 0.009 | 9 | +0.06 / -1.05 | `day_zero_ratio(Close)` |
| +1.10 | 0.000 | 104 | -0.16 / -1.25 | `day_centroid(Volume)` |
| +1.07 | 0.030 | 6 | +0.03 / -1.04 | `cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_centroid(Volume))` |
| +1.07 | 0.003 | 8 | +0.02 / -1.05 | `cs_median(cs_robust_z(day_last(Amt)))` |
| +1.01 | 0.026 | 8 | -0.04 / -1.05 | `ts_sum(day_zero_ratio(Close), 1)` |
| +0.94 | 0.000 | 22 | -0.13 / -1.07 | `day_last(Amt)` |
| +0.94 | 0.005 | 18 | -0.13 / -1.07 | `day_wmean(Low, Close)` |

## 拆解(25 次评估)

### head score +1.64:`cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` | +1.33 | +1.75 | +1.33 | — | (子树本身) |
| sufficiency | `signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))` | +1.69 | +1.77 | +1.69 | — | (子树本身) |
| knockout | `ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20)` | +1.33 | +1.75 | +1.33 | +0.31 | `cs_first_high40(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| knockout | `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` | +1.82 | +1.82 | +1.87 | -0.18 | `cs_first_high40(ts_argmin(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| knockout | `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` | +1.34 | +1.45 | +1.34 | +0.30 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))))` |
| knockout | `signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))` | +1.63 | +1.93 | +1.63 | +0.01 | `cs_first_high40(ts_argmin(cross_quantile_q25(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| swap | `Volume->Amt` | +1.54 | +1.99 | +1.54 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Amt)), 241), 20), day_centroid(Amt))), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Amt)), 241), 20), day_centroid(Amt))), 241))` |
| window | `ts_argmin@20->10` | +1.50 | +1.68 | +1.50 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 10), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| window | `ts_argmin@20->40` | +1.34 | +2.10 | +1.34 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 40), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |

### head score +1.51:`cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_delta(Volume, 30))` | +0.69 | +0.69 | +0.98 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -0.22 | -0.22 | +0.08 | — | (子树本身) |
| swap | `Volume->Amt` | +1.39 | +1.39 | +1.55 | — | `cross_reg_tvalue(day_sum(Amt), day_mean(in_delta(Amt, 30)), 60)` |
| window | `cross_reg_tvalue@60->30` | +1.10 | +1.10 | +1.14 | — | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 30)` |
| window | `cross_reg_tvalue@60->120` | +1.19 | +1.49 | +1.19 | — | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 120)` |

### head score +1.31:`day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_sum(Volume), 20)` | -1.95 | -0.51 | -1.95 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -0.22 | -0.22 | +0.08 | — | (子树本身) |
| knockout | `cross_mean(day_sum(Volume), 20)` | +0.89 | +0.89 | +1.70 | +0.42 | `day_mean(in_delta(div(Volume, day_sum(Volume)), 15))` |
| swap | `Volume->Amt` | +1.41 | +1.41 | +1.67 | — | `day_mean(in_delta(div(Amt, cross_mean(day_sum(Amt), 20)), 15))` |
| window | `in_delta@15->7` | +0.98 | +0.98 | +2.77 | — | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 7))` |
| window | `in_delta@15->30` | +1.19 | +1.25 | +1.19 | — | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 30))` |

### head score +1.16:`ts_cov(LogTotalCap, day_centroid(Volume), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| swap | `Volume->Amt` | +1.21 | +1.21 | +1.22 | — | `ts_cov(LogTotalCap, day_centroid(Amt), 40)` |
| window | `ts_cov@40->20` | -0.89 | +0.55 | -0.89 | — | `ts_cov(LogTotalCap, day_centroid(Volume), 20)` |
| window | `ts_cov@40->80` | +0.02 | +0.70 | +0.02 | — | `ts_cov(LogTotalCap, day_centroid(Volume), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))` — ablation,自身 score +1.69(所在 head +1.64)
2. `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` — ablation,自身 score +1.33(所在 head +1.64)
3. `cross_quantile_q25(day_centroid(Volume), 241)` — enrichment,均值差 +2.04,p 0.001
4. `ts_argmin(cross_quantile_q25(day_centroid(Volume), 241), 20)` — enrichment,均值差 +2.04,p 0.001
5. `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))` — enrichment,均值差 +1.99,p 0.000
6. `cross_quantile_q25(signedpower(day_centroid(Volume)), 241)` — enrichment,均值差 +1.96,p 0.000
7. `ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20)` — enrichment,均值差 +1.95,p 0.000
8. `signedpower(day_centroid(Volume))` — enrichment,均值差 +1.61,p 0.000
9. `day_mean(neg(neg(in_delta(Volume, 5))))` — enrichment,均值差 +1.60,p 0.003
10. `signedpower(signedpower(day_centroid(Volume)))` — enrichment,均值差 +1.51,p 0.003
11. `day_mean(in_delta(Volume, 5))` — enrichment,均值差 +1.34,p 0.006
12. `day_quantile_q25(Close)` — enrichment,均值差 +1.32,p 0.000
13. `ts_decay_linear(day_quantile(Close), 20)` — enrichment,均值差 +1.27,p 0.026
14. `day_mean(neg(in_delta(Volume, 60)))` — enrichment,均值差 +1.16,p 0.000
15. `day_quantile(Close)` — enrichment,均值差 +1.13,p 0.000
16. `day_zero_ratio(Close)` — enrichment,均值差 +1.11,p 0.009
17. `day_centroid(Volume)` — enrichment,均值差 +1.10,p 0.000
18. `cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_centroid(Volume))` — enrichment,均值差 +1.07,p 0.030
19. `cs_median(cs_robust_z(day_last(Amt)))` — enrichment,均值差 +1.07,p 0.003
20. `ts_sum(day_zero_ratio(Close), 1)` — enrichment,均值差 +1.01,p 0.026
21. `day_last(Amt)` — enrichment,均值差 +0.94,p 0.000
22. `day_wmean(Low, Close)` — enrichment,均值差 +0.94,p 0.005
23. `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` — enrichment,均值差 +0.91,p 0.084
24. `day_flat_run_max(Vwap)` — enrichment,均值差 +0.91,p 0.084
25. `day_quantile_q25(High)` — enrichment,均值差 +0.87,p 0.001
26. `day_quantile_q25(Open)` — enrichment,均值差 +0.86,p 0.048
27. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +0.86,p 0.048
28. `cs_robust_z(day_last(Amt))` — enrichment,均值差 +0.83,p 0.001
29. `ts_argmin(cross_quantile_q25(LogFloatShares, 241), 40)` — enrichment,均值差 +0.82,p 0.027
30. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +0.69,p 0.056
31. `cs_stddev_full(cs_robust_z(day_last(Amt)))` — enrichment,均值差 +0.59,p 0.041

## 本组之前各轮的任务

- `c08s802Pr1a_Ea`:核心 `day_mean(in_delta(Volume, 30))`;评分 85,过线 4,入 heads 3;采样计数 {'c05_no_core': 2445, 'mutation_refused': 5, 'c05_skeleton': 9}
  - score +1.10(train +1.10 valid +1.14):`cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 30)`
  - score +1.08(train +1.28 valid +1.08):`cross_regbeta(day_sum(Volume), day_mean(in_delta(Volume, 30)), 20)`
  - score +0.81(train +0.81 valid +1.47):`ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)`
  - score +0.70(train +0.70 valid +1.20):`cross_regbeta(day_sum(Volume), ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 30), 20)`
  - score +0.50(train +0.50 valid +0.74):`ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 30)`
- `c08s802Pr1b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {}
  - score -0.35(train -0.35 valid +0.87):`cross_mean(cross_mean(day_signed_ratio(Ret, Volume), 20), 20)`
  - score -0.35(train -0.35 valid +0.97):`cross_mean(cross_quantile_q75(day_signed_ratio(Ret, Volume), 3), 20)`
  - score -0.38(train -0.38 valid +0.71):`cross_mean(cross_mean(cross_mean(day_signed_ratio(Ret, Volume), 20), 20), 20)`
  - score -0.55(train -0.55 valid +1.27):`cross_mean(day_signed_ratio(Ret, Volume), 20)`
  - score -0.55(train -0.55 valid +1.21):`cross_mean(cross_mean(day_signed_ratio(Ret, Volume), 3), 20)`
- `c08s802Pr2a_Ea`:核心 `day_centroid(Volume)`;评分 94,过线 9,入 heads 3;采样计数 {'c05_no_core': 2491, 'c05_periphery_seen': 12}
  - score +1.16(train +1.16 valid +1.24):`ts_cov(LogTotalCap, day_centroid(Volume), 40)`
  - score +1.00(train +1.00 valid +1.05):`ts_cov(LogTotalCap, day_centroid(Volume), 50)`
  - score +0.91(train +0.92 valid +0.91):`cross_tail_mean_q25(ts_cov(LogTotalCap, day_centroid(Volume), 50), 3)`
  - score +0.87(train +0.87 valid +1.62):`cross_tail_mean_q25(ts_cov(LogTotalCap, day_centroid(Volume), 50), 5)`
  - score +0.83(train +0.83 valid +1.13):`ts_cov(cs_last_low20(ts_sum(day_zero_ratio(Close), 1), day_centroid(Volume)), day_centroid(Volume), 50)`
- `c08s802Pr2b_Nb`:核心 `—`;评分 81,过线 0,入 heads 0;采样计数 {}
  - score +0.08(train +0.28 valid +0.08):`sub(cross_delta(LogFloatShares, 20), cross_mean(cross_delta(LogFloatShares, 20), 241))`
  - score +0.03(train +0.15 valid +0.03):`sub(cross_delta(LogFloatShares, 20), cross_mean(cross_delta(LogFloatShares, 15), 241))`
  - score +0.01(train +0.47 valid +0.01):`sub(cross_quantile_q25(LogFloatShares, 5), cross_mean(cross_quantile_q25(LogFloatShares, 5), 241))`
  - score -0.18(train -0.18 valid +0.33):`sub(cross_delta(LogFloatShares, 20), cross_mean(cross_mean(cross_delta(LogFloatShares, 20), 241), 241))`
  - score -0.22(train -0.22 valid +1.30):`sub(cross_delta(LogFloatShares, 20), cross_mean(cs_first_high20(LimitWidth, LogTotalCap), 241))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(knockout cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)):`cs_first_high40(ts_argmin(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))`
