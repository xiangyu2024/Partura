# 定位:种子 803,C 组,第 3 轮(只含 train / valid)

快照:c05s803M1_I0_open_search, c05s803M2_I0_open_search, c05s803M3_I0_open_search, c06s803Cr1a_Ea, c06s803Cr1b_Nb, c06s803Cr2a_Ea, c06s803Cr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(17 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.65 | +1.74 | +1.65 | +1 | 0 | c06s803Cr2a_Ea | `cross_mean(sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt)), 20)` |
| +1.56 | +1.56 | +2.07 | -1 | 20 | c05s803M2_I0_open_search | `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)` |
| +1.53 | +1.53 | +3.31 | -1 | 20 | c06s803Cr2b_Nb | `div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3), cross_sum(cross_quantile_q50(ListAge, 3), 20))` |
| +1.44 | +1.44 | +2.78 | +1 | 0 | c06s803Cr2b_Nb | `div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |
| +1.28 | +1.28 | +1.40 | -1 | 5 | c06s803Cr2a_Ea | `cross_mean(sqrt(sqrt(day_centroid(Amt))), 20)` |
| +1.23 | +1.23 | +2.29 | -1 | 5 | c05s803M2_I0_open_search | `ts_skew(day_durbin_watson(Open), 50)` |
| +1.05 | +1.05 | +1.31 | +1 | 20 | c06s803Cr2a_Ea | `pow_2_5(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 20)))` |
| +0.99 | +0.99 | +1.86 | +1 | 20 | c06s803Cr1a_Ea | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)` |
| +0.97 | +0.97 | +1.54 | -1 | 20 | c05s803M1_I0_open_search | `day_kurt(Ret)` |
| +0.94 | +0.94 | +1.26 | +1 | 20 | c06s803Cr2a_Ea | `ts_decay_linear(sub(day_centroid(Ret), day_centroid(Amt)), 5)` |
| +0.93 | +0.93 | +2.44 | -1 | 20 | c06s803Cr2b_Nb | `div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 3), cross_quantile_q50(ListAge, 3))` |
| +0.91 | +0.91 | +2.82 | +1 | 5 | c06s803Cr2b_Nb | `div(cross_max(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 15), day_pos_ratio(Volume))` |
| +0.86 | +0.86 | +1.06 | +1 | 20 | c06s803Cr1b_Nb | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` |
| +0.67 | +0.91 | +0.67 | -1 | 20 | c06s803Cr2b_Nb | `div(cross_sum(ts_var(cross_sum(ts_var(pow_2_5(cs_last_low40(ts_product(day_pos_ratio(Volume), 5), day_pos_ratio(Volume))), 50), 20), 50), 20), cross_sum(day_sum(mul(Ret, Ret)), 20))` |
| +0.65 | +0.65 | +0.97 | -1 | 5 | c06s803Cr1a_Ea | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3)), 15)` |
| +0.65 | +0.65 | +1.41 | -1 | 20 | c06s803Cr2b_Nb | `div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 20), cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20))` |
| +0.62 | +0.62 | +3.20 | -1 | 0 | c06s803Cr2b_Nb | `div(cross_sum(ts_var(pow_2_5(div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 20), cross_sum(ListAge, 20))), 50), 20), cross_sum(day_var(Close), 20))` |

## 共性:462 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.82 | 0.000 | 18 | +1.03 / -0.79 | `day_std(Amt)` |
| +1.80 | 0.000 | 10 | +1.05 / -0.76 | `sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50))` |
| +1.72 | 0.000 | 14 | +0.95 / -0.77 | `ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)` |
| +1.40 | 0.000 | 11 | +0.65 / -0.75 | `ts_skew(day_durbin_watson(Open), 50)` |
| +1.39 | 0.005 | 4 | +0.66 / -0.73 | `ts_med(sub(day_hurst(Ret), day_kurt(Ret)), 40)` |
| +1.37 | 0.003 | 5 | +0.64 / -0.73 | `sub(day_hurst(Ret), day_kurt(Ret))` |
| +1.36 | 0.002 | 7 | +0.62 / -0.74 | `ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50)` |
| +1.36 | 0.002 | 7 | +0.62 / -0.74 | `cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))` |
| +1.36 | 0.002 | 7 | +0.62 / -0.74 | `pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume)))` |
| +1.33 | 0.008 | 5 | +0.60 / -0.73 | `cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20)` |
| +1.28 | 0.002 | 8 | +0.54 / -0.74 | `day_q_stat_std(Volume)` |
| +1.28 | 0.001 | 8 | +0.54 / -0.74 | `ts_med(sub(day_hurst(Close), day_kurt(Ret)), 40)` |
| +1.27 | 0.012 | 4 | +0.54 / -0.73 | `ts_quantile_q50(day_kurt(Ret), 40)` |
| +1.22 | 0.000 | 14 | +0.47 / -0.75 | `sub(day_hurst(Close), day_kurt(Ret))` |
| +1.21 | 0.000 | 15 | +0.46 / -0.76 | `day_hurst(Close)` |
| +1.18 | 0.010 | 6 | +0.44 / -0.73 | `sqrt(day_centroid(Amt))` |
| +1.11 | 0.027 | 5 | +0.38 / -0.73 | `cross_sum(cross_quantile_q50(ListAge, 3), 20)` |
| +1.10 | 0.029 | 5 | +0.37 / -0.73 | `sqrt(sqrt(day_centroid(Amt)))` |
| +1.08 | 0.000 | 65 | +0.21 / -0.87 | `day_kurt(Ret)` |
| +1.01 | 0.038 | 5 | +0.28 / -0.73 | `ts_skew(day_durbin_watson(Open), 40)` |

## 拆解(37 次评估)

### head score +1.65:`cross_mean(sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt))` | +1.56 | +1.69 | +1.56 | — | (子树本身) |
| sufficiency | `sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50))` | +1.49 | +1.61 | +1.49 | — | (子树本身) |
| sufficiency | `ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)` | +1.51 | +1.53 | +1.51 | — | (子树本身) |
| sufficiency | `day_std(Amt)` | -0.27 | -0.27 | +0.61 | — | (子树本身) |
| knockout | `sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt))` | +1.53 | +1.79 | +1.53 | +0.12 | `cross_mean(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), 20)` |
| knockout | `sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50))` | +1.61 | +1.76 | +1.61 | +0.04 | `cross_mean(sub(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50), day_centroid(Amt)), 20)` |
| knockout | `ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)` | -1.42 | -1.42 | -0.85 | +3.07 | `cross_mean(sub(sqrt(day_std(Amt)), day_centroid(Amt)), 20)` |
| swap | `Amt->Volume` | +1.17 | +1.66 | +1.17 | — | `cross_mean(sub(sqrt(ts_reg_fvalue(day_std(Volume), day_centroid(Volume), 50)), day_centroid(Volume)), 20)` |
| window | `cross_mean@20->10` | +1.52 | +1.68 | +1.52 | — | `cross_mean(sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt)), 10)` |
| window | `cross_mean@20->40` | +1.28 | +1.28 | +1.50 | — | `cross_mean(sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt)), 40)` |

### head score +1.53:`div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3), cross_sum(cross_quantile_q50(ListAge, 3), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3)` | +0.35 | +0.35 | +2.08 | — | (子树本身) |
| sufficiency | `day_sum(mul(mul(Ret, Ret), abs_(Ret)))` | +0.85 | +0.85 | +2.27 | — | (子树本身) |
| sufficiency | `cross_sum(cross_quantile_q50(ListAge, 3), 20)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_quantile_q50(ListAge, 3)` | — | — | — | — | 门槛废品 |
| knockout | `cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3)` | +1.68 | +1.68 | +3.29 | -0.15 | `div(day_sum(mul(mul(Ret, Ret), abs_(Ret))), cross_sum(cross_quantile_q50(ListAge, 3), 20))` |
| knockout | `cross_sum(cross_quantile_q50(ListAge, 3), 20)` | +1.40 | +1.40 | +3.25 | +0.13 | `div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3), cross_quantile_q50(ListAge, 3))` |
| knockout | `cross_quantile_q50(ListAge, 3)` | +1.52 | +1.52 | +3.28 | +0.01 | `div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3), cross_sum(ListAge, 20))` |
| window | `cross_sum@3->2` | +1.59 | +1.59 | +3.31 | — | `div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 2), cross_sum(cross_quantile_q50(ListAge, 3), 20))` |
| window | `cross_sum@3->6` | +1.23 | +1.23 | +3.30 | — | `div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 6), cross_sum(cross_quantile_q50(ListAge, 3), 20))` |

### head score +1.44:`div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20)` | +0.86 | +0.86 | +2.54 | — | (子树本身) |
| sufficiency | `cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20)` | +0.43 | +0.43 | +1.46 | — | (子树本身) |
| sufficiency | `ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50)` | +0.87 | +0.87 | +2.48 | — | (子树本身) |
| sufficiency | `day_sum(mul(mul(Ret, abs_(Ret)), Ret))` | +0.85 | +0.85 | +2.27 | — | (子树本身) |
| knockout | `cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20)` | +1.02 | +1.02 | +2.68 | +0.41 | `div(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |
| knockout | `cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20)` | -0.18 | -0.18 | +1.42 | +1.62 | `div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20), day_sum(mul(mul(Ret, abs_(Ret)), Ret)))` |
| knockout | `ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50)` | — | — | — | — | `div(cross_sum(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 20), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |
| knockout | `pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume)))` | +1.17 | +1.17 | +1.20 | +0.27 | `div(cross_sum(ts_var(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume)), 50), 20), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |
| swap | `Volume->Amt` | +1.41 | +1.41 | +2.79 | — | `div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Amt), day_pos_ratio(Amt))), 50), 20), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |
| window | `cross_sum@20->10` | +1.58 | +1.58 | +3.16 | — | `div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 10), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |
| window | `cross_sum@20->40` | +1.37 | +1.37 | +2.43 | — | `div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 40), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))` |

### head score +1.28:`cross_mean(sqrt(sqrt(day_centroid(Amt))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(sqrt(day_centroid(Amt)))` | -0.65 | -0.65 | +0.36 | — | (子树本身) |
| sufficiency | `sqrt(day_centroid(Amt))` | -0.51 | -0.51 | +0.43 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| knockout | `sqrt(sqrt(day_centroid(Amt)))` | +1.25 | +1.25 | +1.54 | +0.03 | `cross_mean(sqrt(day_centroid(Amt)), 20)` |
| swap | `Amt->Volume` | +1.23 | +1.23 | +1.46 | — | `cross_mean(sqrt(sqrt(day_centroid(Volume))), 20)` |
| window | `cross_mean@20->10` | +1.01 | +1.19 | +1.01 | — | `cross_mean(sqrt(sqrt(day_centroid(Amt))), 10)` |
| window | `cross_mean@20->40` | +1.30 | +1.30 | +1.61 | — | `cross_mean(sqrt(sqrt(day_centroid(Amt))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt))` — ablation,自身 score +1.56(所在 head +1.65)
2. `ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)` — ablation,自身 score +1.51(所在 head +1.65)
3. `sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50))` — ablation,自身 score +1.49(所在 head +1.65)
4. `ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50)` — ablation,自身 score +0.87(所在 head +1.44)
5. `day_std(Amt)` — enrichment,均值差 +1.82,p 0.000
6. `ts_skew(day_durbin_watson(Open), 50)` — enrichment,均值差 +1.40,p 0.000
7. `ts_med(sub(day_hurst(Ret), day_kurt(Ret)), 40)` — enrichment,均值差 +1.39,p 0.005
8. `sub(day_hurst(Ret), day_kurt(Ret))` — enrichment,均值差 +1.37,p 0.003
9. `cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))` — enrichment,均值差 +1.36,p 0.002
10. `pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume)))` — enrichment,均值差 +1.36,p 0.002
11. `cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20)` — enrichment,均值差 +1.33,p 0.008
12. `day_q_stat_std(Volume)` — enrichment,均值差 +1.28,p 0.002
13. `ts_med(sub(day_hurst(Close), day_kurt(Ret)), 40)` — enrichment,均值差 +1.28,p 0.001
14. `ts_quantile_q50(day_kurt(Ret), 40)` — enrichment,均值差 +1.27,p 0.012
15. `sub(day_hurst(Close), day_kurt(Ret))` — enrichment,均值差 +1.22,p 0.000
16. `day_hurst(Close)` — enrichment,均值差 +1.21,p 0.000
17. `sqrt(day_centroid(Amt))` — enrichment,均值差 +1.18,p 0.010
18. `cross_sum(cross_quantile_q50(ListAge, 3), 20)` — enrichment,均值差 +1.11,p 0.027
19. `sqrt(sqrt(day_centroid(Amt)))` — enrichment,均值差 +1.10,p 0.029
20. `day_kurt(Ret)` — enrichment,均值差 +1.08,p 0.000
21. `ts_skew(day_durbin_watson(Open), 40)` — enrichment,均值差 +1.01,p 0.038
22. `day_durbin_watson(Open)` — enrichment,均值差 +0.84,p 0.000
23. `sub(day_centroid(Ret), day_centroid(Amt))` — enrichment,均值差 +0.82,p 0.048
24. `cs_last_low10(cs_last_low10(LimitWidth, LimitWidth), cs_last_low10(LimitWidth, LimitWidth))` — enrichment,均值差 +0.81,p 0.089
25. `day_pos_ratio(Volume)` — enrichment,均值差 +0.77,p 0.004
26. `day_zero_ratio(Ret)` — enrichment,均值差 +0.73,p 0.002
27. `cross_sum(day_sum(mul(Ret, Ret)), 20)` — enrichment,均值差 +0.72,p 0.024
28. `day_hurst(Ret)` — enrichment,均值差 +0.70,p 0.027
29. `cs_last_low10(LimitWidth, LimitWidth)` — enrichment,均值差 +0.69,p 0.019
30. `cross_sum(ListAge, 20)` — enrichment,均值差 +0.67,p 0.056
31. `cross_stddev(LimitWidth, 10)` — enrichment,均值差 +0.54,p 0.064
32. `cross_sum(day_sum(mul(Ret, abs_(Ret))), 20)` — enrichment,均值差 +0.54,p 0.051
33. `day_centroid(Amt)` — enrichment,均值差 +0.53,p 0.002
34. `day_sum(mul(Ret, Ret))` — enrichment,均值差 +0.46,p 0.097
35. `day_sum(mul(Ret, abs_(Ret)))` — enrichment,均值差 +0.42,p 0.077

## 本组之前各轮的任务

- `c06s803Cr1a_Ea`:核心 `day_kurt(Ret)`;评分 104,过线 41,入 heads 2;采样计数 {'c05_no_core': 1974, 'c05_skeleton': 36}
  - score +0.99(train +0.99 valid +1.86):`cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)`
  - score +0.95(train +0.95 valid +1.75):`cross_ema(cs_winsor(mul(add(sub(day_skew(Low), day_kurt(Ret)), 3), sub(1, cs_winsor(mul(add(sub(day_skew(Low), day_kurt(Ret)), 3), sub(1, day_zero_ratio(Ret))))))), 20)`
  - score +0.94(train +0.94 valid +1.84):`cross_ema(cs_winsor(mul(add(day_kurt(Ret), 3), sub(1, cs_winsor(mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret))))))), 20)`
  - score +0.82(train +0.82 valid +1.79):`cross_ema(cs_winsor(mul(add(day_kurt(Ret), -5), sub(3, day_zero_ratio(Ret)))), 20)`
  - score +0.82(train +0.82 valid +1.66):`cross_ema(sub(day_hurst(Close), day_kurt(Ret)), 20)`
- `c06s803Cr1b_Nb`:核心 `—`;评分 59,过线 2,入 heads 1;采样计数 {}
  - score +0.86(train +0.86 valid +1.06):`cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))`
  - score +0.86(train +0.86 valid +1.06):`neg(cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt)))))`
  - score +0.48(train +0.48 valid +0.76):`neg(LogFloatShares)`
  - score +0.48(train +0.48 valid +0.77):`pow_2_5(LogFloatShares)`
  - score +0.38(train +0.38 valid +0.42):`neg(cs_mask_top_replace_mean(mul(LogTotalCap, neg(LogFloatShares))))`
- `c06s803Cr2a_Ea`:核心 `day_centroid(Amt)`;评分 93,过线 22,入 heads 4;采样计数 {'c05_no_core': 1958, 'c05_skeleton': 31, 'c05_periphery_seen': 10}
  - score +1.65(train +1.74 valid +1.65):`cross_mean(sub(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), day_centroid(Amt)), 20)`
  - score +1.61(train +1.81 valid +1.61):`ts_decay_linear(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), 20)`
  - score +1.52(train +1.57 valid +1.52):`ts_decay_linear(sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)), 5)`
  - score +1.51(train +1.53 valid +1.51):`ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)`
  - score +1.49(train +1.62 valid +1.49):`sqrt(ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50))`
- `c06s803Cr2b_Nb`:核心 `—`;评分 93,过线 12,入 heads 7;采样计数 {}
  - score +1.53(train +1.53 valid +3.31):`div(cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3), cross_sum(cross_quantile_q50(ListAge, 3), 20))`
  - score +1.44(train +1.44 valid +2.78):`div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))`
  - score +0.93(train +0.93 valid +2.44):`div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 3), cross_quantile_q50(ListAge, 3))`
  - score +0.91(train +0.91 valid +2.82):`div(cross_max(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 15), day_pos_ratio(Volume))`
  - score +0.86(train +0.86 valid +3.05):`div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 20), cross_sum(day_sum(mul(Ret, Ret)), 20))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.15(knockout cross_sum(day_sum(mul(mul(Ret, Ret), abs_(Ret))), 3)):`div(day_sum(mul(mul(Ret, Ret), abs_(Ret))), cross_sum(cross_quantile_q50(ListAge, 3), 20))`
- 增益 +0.14(window cross_sum@20->10):`div(cross_sum(ts_var(pow_2_5(cs_last_low40(day_q_stat_std(Volume), day_pos_ratio(Volume))), 50), 10), cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Ret)), 20))`
