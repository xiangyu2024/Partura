# 定位:种子 805,B 组,第 3 轮(只含 train / valid)

快照:c05s805M1_I0_open_search, c05s805M2_I0_open_search, c05s805M3_I0_open_search, c05s805Br1a_Ea, c05s805Br1b_Nb, c05s805Br2a_Ea, c05s805Br2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(18 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.55 | +1.55 | +2.11 | -1 | 5 | c05s805Br1a_Ea | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))` |
| +1.40 | +1.40 | +2.27 | +1 | 20 | c05s805Br2a_Ea | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))` |
| +1.25 | +1.25 | +2.49 | +1 | 20 | c05s805Br1a_Ea | `cs_last_high40(LogFloatShares, cross_mean(day_centroid(Volume), 20))` |
| +1.08 | +1.08 | +2.04 | -1 | 5 | c05s805Br1a_Ea | `cross_mean(cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret)), 20)` |
| +0.90 | +0.90 | +1.91 | +1 | 20 | c05s805Br2a_Ea | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))), cross_mean(day_centroid(Volume), 20))` |
| +0.88 | +0.88 | +1.18 | +1 | 20 | c05s805M3_I0_open_search | `ts_skew(day_wstd(Volume, Vwap), 50)` |
| +0.86 | +0.86 | +1.59 | +1 | 20 | c05s805Br2a_Ea | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_argmax(Volume), 20))` |
| +0.84 | +0.84 | +2.20 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.81 | +0.81 | +2.58 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.81 | +0.81 | +0.82 | +1 | 5 | c05s805Br2a_Ea | `cs_last_high20(cross_fangzheng(day_corr(Ret, Volume), 241), cross_mean(cross_mean(day_centroid(Volume), 20), 20))` |
| +0.64 | +1.01 | +0.64 | -1 | 20 | c05s805M2_I0_open_search | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))` |
| +0.63 | +0.63 | +0.78 | -1 | 20 | c05s805M3_I0_open_search | `ts_skew(day_corr(Volume, Vwap), 50)` |
| +0.58 | +0.58 | +0.66 | -1 | 20 | c05s805M2_I0_open_search | `cs_last_low20(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), ts_argmax(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), 20))` |
| +0.56 | +1.10 | +0.56 | +1 | 20 | c05s805Br2a_Ea | `cross_ema(cs_bucket_rank(cross_ema(cs_bucket_rank(day_corr(Ret, Volume), day_sum(Ret)), 20), day_sum(Ret)), 20)` |
| +0.53 | +1.48 | +0.53 | +1 | 20 | c05s805Br2a_Ea | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), day_centroid(Volume))` |
| +0.53 | +0.53 | +0.96 | +1 | 5 | c05s805Br1b_Nb | `cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 3), 20)` |
| +0.53 | +0.97 | +0.53 | -1 | 20 | c05s805Br1a_Ea | `cs_bucket_zscore(cross_mean(cross_mean(sub(day_centroid(Volume), pow_3(day_centroid(Volume))), 20), 20), day_centroid(Ret))` |
| +0.52 | +0.52 | +1.78 | -1 | 20 | c05s805Br2b_Nb | `cs_bucket_zscore(cross_mean(day_topw_mean(abs_(Ret), Ret), 20), cross_mean(day_mean(abs_(Ret)), 20))` |

## 共性:506 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.80 | 0.000 | 8 | +0.79 / -1.00 | `day_flat_ratio(Close)` |
| +1.72 | 0.002 | 5 | +0.73 / -0.99 | `cross_mean(day_flat_ratio(Close), 20)` |
| +1.62 | 0.000 | 7 | +0.62 / -1.00 | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` |
| +1.58 | 0.003 | 5 | +0.58 / -0.99 | `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` |
| +1.54 | 0.006 | 4 | +0.55 / -0.99 | `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` |
| +1.52 | 0.000 | 53 | +0.38 / -1.13 | `sub(day_pos_ratio(High), LogFloatShares)` |
| +1.48 | 0.012 | 4 | +0.50 / -0.99 | `day_first(abs_(sub(1, Open)))` |
| +1.48 | 0.012 | 4 | +0.50 / -0.99 | `ts_argmax(day_first(abs_(sub(1, Open))), 1)` |
| +1.44 | 0.000 | 28 | +0.39 / -1.06 | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` |
| +1.38 | 0.000 | 70 | +0.21 / -1.17 | `day_pos_ratio(High)` |
| +1.31 | 0.000 | 22 | +0.28 / -1.03 | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` |
| +1.30 | 0.006 | 7 | +0.30 / -0.99 | `cs_mean(day_distinct_ratio(Close))` |
| +1.24 | 0.000 | 27 | +0.20 / -1.04 | `day_first(abs_(sub(-1, Open)))` |
| +1.22 | 0.000 | 52 | +0.12 / -1.10 | `day_first(High)` |
| +1.21 | 0.000 | 34 | +0.15 / -1.06 | `cross_mean(day_centroid(Volume), 20)` |
| +1.19 | 0.000 | 30 | +0.14 / -1.05 | `ts_argmax(day_first(High), 1)` |
| +1.07 | 0.030 | 8 | +0.08 / -0.99 | `pow_1_5(day_centroid(Volume))` |
| +1.04 | 0.003 | 20 | +0.02 / -1.02 | `pow_2_5(day_centroid(Volume))` |
| +1.02 | 0.003 | 13 | +0.02 / -1.00 | `cross_mean(cross_mean(day_centroid(Volume), 20), 20)` |
| +0.99 | 0.020 | 12 | -0.01 / -1.00 | `pow_1_5(pow_2_5(day_centroid(Volume)))` |

## 拆解(35 次评估)

### head score +1.40:`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20))` | +1.64 | +1.64 | +2.75 | — | (子树本身) |
| sufficiency | `cross_mean(cross_mean(day_centroid(Volume), 10), 20)` | +1.34 | +1.34 | +1.93 | — | (子树本身) |
| sufficiency | `cross_mean(day_corr(Ret, Volume), 20)` | +0.21 | +0.21 | +1.88 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Volume), 10)` | +1.15 | +1.15 | +1.17 | — | (子树本身) |
| knockout | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20))` | +2.09 | +2.09 | +2.97 | -0.70 | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 10))` |
| knockout | `cross_mean(cross_mean(day_centroid(Volume), 10), 20)` | +2.07 | +2.07 | +2.69 | -0.67 | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 10)), cross_mean(day_centroid(Volume), 10))` |
| knockout | `cross_mean(day_corr(Ret, Volume), 20)` | +0.93 | +0.93 | +1.32 | +0.47 | `cs_last_high20(cs_last_high20(day_corr(Ret, Volume), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))` |
| knockout | `cross_mean(day_centroid(Volume), 10)` | +2.04 | +2.04 | +2.90 | -0.65 | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20)), cross_mean(day_centroid(Volume), 10))` |
| swap | `Volume->Amt` | +2.07 | +2.07 | +2.80 | — | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Amt), 20), cross_mean(cross_mean(day_centroid(Amt), 10), 20)), cross_mean(day_centroid(Amt), 10))` |
| window | `cross_mean@20->10` | +1.79 | +1.79 | +2.29 | — | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 10), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))` |
| window | `cross_mean@20->40` | +2.01 | +2.01 | +2.50 | — | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 40), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))` |

### head score +1.25:`cs_last_high40(LogFloatShares, cross_mean(day_centroid(Volume), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Volume), 20)` | +1.24 | +1.24 | +1.72 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| knockout | `cross_mean(day_centroid(Volume), 20)` | +0.86 | +0.86 | +1.16 | +0.39 | `cs_last_high40(LogFloatShares, day_centroid(Volume))` |
| swap | `Volume->Amt` | +1.21 | +1.21 | +2.52 | — | `cs_last_high40(LogFloatShares, cross_mean(day_centroid(Amt), 20))` |
| window | `cross_mean@20->10` | +1.21 | +1.21 | +2.29 | — | `cs_last_high40(LogFloatShares, cross_mean(day_centroid(Volume), 10))` |
| window | `cross_mean@20->40` | +0.96 | +0.96 | +2.49 | — | `cs_last_high40(LogFloatShares, cross_mean(day_centroid(Volume), 40))` |

### head score +1.08:`cross_mean(cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret))` | +0.71 | +0.71 | +1.57 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -1.38 | -1.38 | -0.48 | — | (子树本身) |
| knockout | `cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret))` | +1.24 | +1.24 | +1.72 | -0.16 | `cross_mean(day_centroid(Volume), 20)` |
| swap | `Volume->Amt` | +1.09 | +1.09 | +1.99 | — | `cross_mean(cs_bucket_zscore(day_centroid(Amt), day_centroid(Ret)), 20)` |
| window | `cross_mean@20->10` | +1.05 | +1.05 | +1.73 | — | `cross_mean(cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret)), 10)` |
| window | `cross_mean@20->40` | +0.81 | +0.81 | +1.79 | — | `cross_mean(cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret)), 40)` |

### head score +0.90:`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))), cross_mean(day_centroid(Volume), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20)))` | -0.89 | -0.89 | -0.59 | — | (子树本身) |
| sufficiency | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))` | +1.70 | +1.70 | +2.69 | — | (子树本身) |
| sufficiency | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20))` | +1.50 | +1.50 | +2.47 | — | (子树本身) |
| sufficiency | `cross_mean(cross_mean(day_centroid(Volume), 20), 20)` | +1.30 | +1.30 | +2.00 | — | (子树本身) |
| knockout | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20)))` | +1.94 | +1.94 | +2.68 | -1.04 | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20))` |
| knockout | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))` | +0.74 | +0.74 | +1.77 | +0.16 | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20))), cross_mean(day_centroid(Volume), 20))` |
| knockout | `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20))` | +0.74 | +0.74 | +1.54 | +0.15 | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20))), cross_mean(day_centroid(Volume), 20))` |
| knockout | `cross_mean(cross_mean(day_centroid(Volume), 20), 20)` | +0.74 | +0.74 | +1.54 | +0.15 | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20)), cross_mean(day_centroid(Volume), 20))), cross_mean(day_centroid(Volume), 20))` |
| swap | `Volume->Amt` | +0.80 | +0.80 | +1.95 | — | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Amt), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Amt), 20), cross_mean(cross_mean(day_centroid(Amt), 20), 20)), cross_mean(day_centroid(Amt), 20))), cross_mean(day_centroid(Amt), 20))` |
| window | `cross_mean@20->10` | +0.54 | +0.54 | +1.66 | — | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 10), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))), cross_mean(day_centroid(Volume), 20))` |
| window | `cross_mean@20->40` | +0.77 | +0.77 | +1.42 | — | `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 40), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))), cross_mean(day_centroid(Volume), 20))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20))` — ablation,自身 score +1.70(所在 head +0.90)
2. `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20))` — ablation,自身 score +1.64(所在 head +1.40)
3. `cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20))` — ablation,自身 score +1.50(所在 head +0.90)
4. `cross_mean(cross_mean(day_centroid(Volume), 10), 20)` — ablation,自身 score +1.34(所在 head +1.40)
5. `cross_mean(cross_mean(day_centroid(Volume), 20), 20)` — ablation,自身 score +1.30(所在 head +0.90)
6. `cross_mean(day_centroid(Volume), 20)` — ablation,自身 score +1.24(所在 head +1.25)
7. `cross_mean(day_centroid(Volume), 10)` — ablation,自身 score +1.15(所在 head +1.40)
8. `cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret))` — ablation,自身 score +0.71(所在 head +1.08)
9. `day_flat_ratio(Close)` — enrichment,均值差 +1.80,p 0.000
10. `cross_mean(day_flat_ratio(Close), 20)` — enrichment,均值差 +1.72,p 0.002
11. `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` — enrichment,均值差 +1.62,p 0.000
12. `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` — enrichment,均值差 +1.58,p 0.003
13. `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.54,p 0.006
14. `sub(day_pos_ratio(High), LogFloatShares)` — enrichment,均值差 +1.52,p 0.000
15. `day_first(abs_(sub(1, Open)))` — enrichment,均值差 +1.48,p 0.012
16. `ts_argmax(day_first(abs_(sub(1, Open))), 1)` — enrichment,均值差 +1.48,p 0.012
17. `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.44,p 0.000
18. `day_pos_ratio(High)` — enrichment,均值差 +1.38,p 0.000
19. `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` — enrichment,均值差 +1.31,p 0.000
20. `cs_mean(day_distinct_ratio(Close))` — enrichment,均值差 +1.30,p 0.006
21. `day_first(abs_(sub(-1, Open)))` — enrichment,均值差 +1.24,p 0.000
22. `day_first(High)` — enrichment,均值差 +1.22,p 0.000
23. `ts_argmax(day_first(High), 1)` — enrichment,均值差 +1.19,p 0.000
24. `pow_1_5(day_centroid(Volume))` — enrichment,均值差 +1.07,p 0.030
25. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.04,p 0.003
26. `pow_1_5(pow_2_5(day_centroid(Volume)))` — enrichment,均值差 +0.99,p 0.020
27. `ts_argmax(day_first(Open), 1)` — enrichment,均值差 +0.99,p 0.083
28. `day_first(Open)` — enrichment,均值差 +0.99,p 0.083
29. `pow_1_5(pow_1_5(pow_2_5(day_centroid(Volume))))` — enrichment,均值差 +0.96,p 0.099
30. `pow_3(day_centroid(Volume))` — enrichment,均值差 +0.96,p 0.015
31. `cs_bucket_rank(day_corr(Ret, Volume), day_sum(Ret))` — enrichment,均值差 +0.88,p 0.099
32. `day_centroid(Volume)` — enrichment,均值差 +0.87,p 0.000
33. `day_centroid(Ret)` — enrichment,均值差 +0.82,p 0.009
34. `sub(day_centroid(Volume), pow_3(day_centroid(Volume)))` — enrichment,均值差 +0.69,p 0.080
35. `cross_mean(day_corr(Ret, Volume), 20)` — enrichment,均值差 +0.67,p 0.003

## 本组之前各轮的任务

- `c05s805Br1a_Ea`:核心 `day_centroid(Volume)`;评分 82,过线 23,入 heads 4;采样计数 {'c05_no_core': 737, 'c05_periphery_seen': 7}
  - score +1.55(train +1.55 valid +2.11):`cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))`
  - score +1.52(train +1.52 valid +2.11):`cs_bucket_zscore(cross_mean(day_centroid(Volume), 10), day_centroid(Ret))`
  - score +1.52(train +1.52 valid +1.67):`cs_bucket_zscore(cross_mean(sub(day_centroid(Volume), pow_3(day_centroid(Volume))), 20), day_centroid(Ret))`
  - score +1.42(train +1.42 valid +2.76):`cross_mean(sub(day_centroid(Volume), pow_3(cs_bucket_rank(day_centroid(Volume), cross_mean(day_flat_ratio(Close), 20)))), 20)`
  - score +1.40(train +1.40 valid +1.40):`cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), cross_mean(day_flat_ratio(Close), 20))`
- `c05s805Br1b_Nb`:核心 `—`;评分 69,过线 2,入 heads 1;采样计数 {}
  - score +0.53(train +0.53 valid +0.96):`cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 3), 20)`
  - score +0.52(train +0.52 valid +0.97):`cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 20), 3)`
  - score +0.46(train +0.46 valid +1.10):`cross_mean(cross_mean(day_corr(Ret, Volume), 20), 20)`
  - score +0.44(train +0.44 valid +1.05):`cross_mean(cross_mean(day_corr(Ret, Amt), 20), 20)`
  - score +0.39(train +0.39 valid +0.94):`cross_mean(cross_sum(cross_mean(day_corr(Ret, Volume), 20), 15), 20)`
- `c05s805Br2a_Ea`:核心 `day_corr(Ret, Volume)`;评分 82,过线 17,入 heads 6;采样计数 {'c05_no_core': 672, 'c05_periphery_seen': 6}
  - score +1.40(train +1.40 valid +2.27):`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))`
  - score +1.39(train +1.39 valid +1.70):`cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 5))`
  - score +1.34(train +1.34 valid +1.76):`cs_last_high20(cross_mean(day_corr(Ret, Volume), 15), cross_mean(day_centroid(Volume), 20))`
  - score +1.22(train +1.22 valid +1.94):`cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20))`
  - score +1.13(train +1.13 valid +1.96):`cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 3))`
- `c05s805Br2b_Nb`:核心 `—`;评分 91,过线 1,入 heads 1;采样计数 {}
  - score +0.52(train +0.52 valid +1.78):`cs_bucket_zscore(cross_mean(day_topw_mean(abs_(Ret), Ret), 20), cross_mean(day_mean(abs_(Ret)), 20))`
  - score +0.22(train +0.22 valid +1.48):`cs_bucket_zscore(cross_mean(cross_semistd_neg(day_mean(abs_(Ret)), 15), 60), day_wstd(in_index(Ret), Volume))`
  - score -0.22(train +0.80 valid -0.22):`cs_bucket_zscore(cross_mean(cross_mean(day_wstd(in_index(Volume), Volume), 20), 20), cross_mean(day_mean(Ret), 20))`
  - score -0.22(train -0.22 valid +0.92):`cross_mean(day_mean(abs_(Ret)), 20)`
  - score -0.29(train -0.06 valid -0.29):`cs_bucket_zscore(cross_mean(day_wstd(in_index(Volume), Volume), 20), day_wstd(in_index(Ret), Low))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.04(knockout cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20)), cross_mean(day_centroid(Volume), 20)))):`cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20))`
- 增益 +0.70(knockout cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 10), 20))):`cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 10))`
- 增益 +0.67(knockout cross_mean(cross_mean(day_centroid(Volume), 10), 20)):`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 10)), cross_mean(day_centroid(Volume), 10))`
- 增益 +0.67(swap Volume->Amt):`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Amt), 20), cross_mean(cross_mean(day_centroid(Amt), 10), 20)), cross_mean(day_centroid(Amt), 10))`
- 增益 +0.65(knockout cross_mean(day_centroid(Volume), 10)):`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 20), cross_mean(day_centroid(Volume), 20)), cross_mean(day_centroid(Volume), 10))`
- 增益 +0.62(window cross_mean@20->40):`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 40), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))`
- 增益 +0.39(window cross_mean@20->10):`cs_last_high20(cs_last_high20(cross_mean(day_corr(Ret, Volume), 10), cross_mean(cross_mean(day_centroid(Volume), 10), 20)), cross_mean(day_centroid(Volume), 10))`
