# 定位:种子 801,P 组,第 3 轮(只含 train / valid)

快照:c07s801M1_I0_open_search, c07s801M2_I0_open_search, c07s801M3_I0_open_search, c08s801Pr1a_Ea, c08s801Pr1b_Nb, c08s801Pr2a_Ea, c08s801Pr2b_Eb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.50 | +1.50 | +1.63 | -1 | 5 | c08s801Pr2a_Ea | `cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), cross_mean(ts_kurt(day_min(Ret), 5), 20))` |
| +0.77 | +0.77 | +1.95 | -1 | 20 | c08s801Pr2b_Eb | `cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 20)` |
| +0.64 | +0.64 | +0.94 | -1 | 20 | c08s801Pr2a_Ea | `cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20))` |
| +0.64 | +0.64 | +1.39 | -1 | 5 | c08s801Pr1a_Ea | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)` |
| +0.63 | +0.63 | +0.73 | -1 | 20 | c08s801Pr2a_Ea | `sub(day_centroid(Volume), day_centroid(Ret))` |
| +0.52 | +0.58 | +0.52 | -1 | 20 | c08s801Pr2a_Ea | `cross_zscore(cross_mean(day_centroid(Volume), 5), 120)` |

## 共性:536 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.75 | 0.000 | 11 | +0.51 / -1.24 | `cross_mean(day_sum(Amt), 20)` |
| +1.75 | 0.000 | 17 | +0.49 / -1.26 | `day_sum(Amt)` |
| +1.40 | 0.000 | 19 | +0.15 / -1.25 | `cross_mean(day_centroid(Volume), 20)` |
| +1.25 | 0.000 | 94 | -0.17 / -1.42 | `day_centroid(Volume)` |
| +1.20 | 0.002 | 6 | -0.02 / -1.21 | `cs_last_high20(LimitWidth, ts_med(LimitWidth, 50))` |
| +1.16 | 0.022 | 8 | -0.06 / -1.22 | `cross_mean(abs_(day_centroid(Volume)), 20)` |
| +1.14 | 0.006 | 7 | -0.08 / -1.22 | `cs_last_low10(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20))` |
| +1.09 | 0.001 | 14 | -0.14 / -1.23 | `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` |
| +1.06 | 0.004 | 14 | -0.17 / -1.23 | `abs_(day_centroid(Volume))` |
| +0.99 | 0.025 | 4 | -0.22 / -1.21 | `pow_1_5(pow_1_5(LimitWidth))` |
| +0.94 | 0.000 | 24 | -0.30 / -1.24 | `day_sum(Volume)` |
| +0.90 | 0.023 | 5 | -0.31 / -1.21 | `cross_mean(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 20)` |
| +0.89 | 0.039 | 4 | -0.32 / -1.21 | `cross_semistd_pos(LimitWidth, 60)` |
| +0.86 | 0.066 | 4 | -0.35 / -1.21 | `cross_semistd_pos(pow_1_5(LimitWidth), 10)` |
| +0.86 | 0.066 | 4 | -0.35 / -1.21 | `cs_last_high20(cross_semistd_pos(pow_1_5(LimitWidth), 10), ts_med(LimitWidth, 50))` |
| +0.82 | 0.007 | 10 | -0.40 / -1.22 | `day_product(Ret)` |
| +0.81 | 0.043 | 6 | -0.40 / -1.21 | `mul(ts_med(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 50), day_signed_ratio(Ret, Amt))` |
| +0.67 | 0.000 | 34 | -0.57 / -1.24 | `pow_1_5(LimitWidth)` |
| +0.67 | 0.129 | 4 | -0.54 / -1.21 | `pow_3(LogFloatShares)` |
| +0.65 | 0.007 | 19 | -0.57 / -1.22 | `mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))` |

## 拆解(35 次评估)

### head score +1.50:`cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), cross_mean(ts_kurt(day_min(Ret), 5), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(abs_(day_centroid(Volume)), 20)` | +1.28 | +1.75 | +1.28 | — | (子树本身) |
| sufficiency | `cross_mean(ts_kurt(day_min(Ret), 5), 20)` | -1.15 | -1.15 | +0.46 | — | (子树本身) |
| sufficiency | `abs_(day_centroid(Volume))` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| sufficiency | `ts_kurt(day_min(Ret), 5)` | -1.17 | -1.17 | -0.47 | — | (子树本身) |
| knockout | `cross_mean(abs_(day_centroid(Volume)), 20)` | +0.70 | +0.79 | +0.70 | +0.81 | `cs_bucket_rank(abs_(day_centroid(Volume)), cross_mean(ts_kurt(day_min(Ret), 5), 20))` |
| knockout | `cross_mean(ts_kurt(day_min(Ret), 5), 20)` | +1.24 | +1.60 | +1.24 | +0.27 | `cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), ts_kurt(day_min(Ret), 5))` |
| knockout | `abs_(day_centroid(Volume))` | +1.50 | +1.50 | +1.63 | +0.00 | `cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(ts_kurt(day_min(Ret), 5), 20))` |
| knockout | `ts_kurt(day_min(Ret), 5)` | +1.67 | +1.67 | +1.68 | -0.17 | `cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), cross_mean(day_min(Ret), 20))` |
| swap | `Volume->Amt` | +1.52 | +1.52 | +1.72 | — | `cs_bucket_rank(cross_mean(abs_(day_centroid(Amt)), 20), cross_mean(ts_kurt(day_min(Ret), 5), 20))` |
| window | `cross_mean@20->10` | +1.51 | +1.51 | +1.57 | — | `cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 10), cross_mean(ts_kurt(day_min(Ret), 5), 20))` |
| window | `cross_mean@20->40` | +1.38 | +1.38 | +1.65 | — | `cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 40), cross_mean(ts_kurt(day_min(Ret), 5), 20))` |

### head score +0.77:`cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)))` | -1.27 | -1.27 | -0.35 | — | (子树本身) |
| sufficiency | `ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50)` | -0.60 | -0.60 | +0.46 | — | (子树本身) |
| sufficiency | `mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)))` | -2.43 | -2.43 | +0.06 | — | (子树本身) |
| sufficiency | `mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))` | -2.53 | -2.53 | +0.22 | — | (子树本身) |
| knockout | `mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)))` | -0.58 | -0.58 | +0.79 | +1.36 | `cross_mean(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), 20)` |
| knockout | `ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50)` | -0.94 | -0.94 | +0.25 | +1.71 | `cross_mean(mul(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 20)` |
| knockout | `mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)))` | -0.41 | -0.41 | +1.31 | +1.19 | `cross_mean(mul(ts_med(ts_med(LimitWidth, 50), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 20)` |
| knockout | `mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))` | -0.40 | -0.40 | +1.15 | +1.17 | `cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), ts_med(LimitWidth, 50)), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 20)` |
| swap | `Amt->Volume` | +0.75 | +0.75 | +1.91 | — | `cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Volume))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Volume))), 20)` |
| window | `cross_mean@20->10` | +0.86 | +0.86 | +1.47 | — | `cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 10)` |
| window | `cross_mean@20->40` | +0.43 | +0.43 | +1.38 | — | `cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 40)` |

### head score +0.64:`cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20)` | +1.47 | +1.47 | +1.68 | — | (子树本身) |
| sufficiency | `cross_mean(abs_(day_centroid(Volume)), 20)` | +1.28 | +1.75 | +1.28 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Volume), 20)` | +1.28 | +1.75 | +1.28 | — | (子树本身) |
| sufficiency | `abs_(day_centroid(Volume))` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20)` | -2.46 | -2.46 | -2.04 | +3.10 | `cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(abs_(day_centroid(Volume)), 20))` |
| knockout | `cross_mean(day_centroid(Volume), 20)` | -0.83 | -0.33 | -0.83 | +1.48 | `cs_bucket_rank(day_centroid(Volume), cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20))` |
| knockout | `abs_(day_centroid(Volume))` | +0.64 | +0.64 | +0.94 | -0.00 | `cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(cross_mean(day_centroid(Volume), 20), 20))` |
| swap | `Volume->Amt` | +0.58 | +0.58 | +0.85 | — | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(cross_mean(abs_(day_centroid(Amt)), 20), 20))` |
| window | `cross_mean@20->10` | +0.55 | +0.68 | +0.55 | — | `cs_bucket_rank(cross_mean(day_centroid(Volume), 10), cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20))` |
| window | `cross_mean@20->40` | -0.10 | +0.85 | -0.10 | — | `cs_bucket_rank(cross_mean(day_centroid(Volume), 40), cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20))` |

### head score +0.63:`sub(day_centroid(Volume), day_centroid(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -2.89 | -1.77 | -2.89 | — | (子树本身) |
| swap | `Volume->Amt` | +0.61 | +0.61 | +0.75 | — | `sub(day_centroid(Amt), day_centroid(Ret))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(cross_mean(abs_(day_centroid(Volume)), 20), 20)` — ablation,自身 score +1.47(所在 head +0.64)
2. `cross_mean(abs_(day_centroid(Volume)), 20)` — ablation,自身 score +1.28(所在 head +1.50)
3. `cross_mean(day_centroid(Volume), 20)` — ablation,自身 score +1.28(所在 head +0.64)
4. `cross_mean(day_sum(Amt), 20)` — enrichment,均值差 +1.75,p 0.000
5. `day_sum(Amt)` — enrichment,均值差 +1.75,p 0.000
6. `day_centroid(Volume)` — enrichment,均值差 +1.25,p 0.000
7. `cs_last_high20(LimitWidth, ts_med(LimitWidth, 50))` — enrichment,均值差 +1.20,p 0.002
8. `cs_last_low10(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20))` — enrichment,均值差 +1.14,p 0.006
9. `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` — enrichment,均值差 +1.09,p 0.001
10. `abs_(day_centroid(Volume))` — enrichment,均值差 +1.06,p 0.004
11. `pow_1_5(pow_1_5(LimitWidth))` — enrichment,均值差 +0.99,p 0.025
12. `day_sum(Volume)` — enrichment,均值差 +0.94,p 0.000
13. `cross_mean(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 20)` — enrichment,均值差 +0.90,p 0.023
14. `cross_semistd_pos(LimitWidth, 60)` — enrichment,均值差 +0.89,p 0.039
15. `cross_semistd_pos(pow_1_5(LimitWidth), 10)` — enrichment,均值差 +0.86,p 0.066
16. `cs_last_high20(cross_semistd_pos(pow_1_5(LimitWidth), 10), ts_med(LimitWidth, 50))` — enrichment,均值差 +0.86,p 0.066
17. `day_product(Ret)` — enrichment,均值差 +0.82,p 0.007
18. `mul(ts_med(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 50), day_signed_ratio(Ret, Amt))` — enrichment,均值差 +0.81,p 0.043
19. `pow_1_5(LimitWidth)` — enrichment,均值差 +0.67,p 0.000
20. `mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))` — enrichment,均值差 +0.65,p 0.007
21. `ts_kurt(day_quantile_q25(Volume), 50)` — enrichment,均值差 +0.63,p 0.065
22. `div(day_topw_mean(High, Open), day_durbin_watson(Volume))` — enrichment,均值差 +0.62,p 0.032
23. `cs_last_low10(day_centroid(Volume), BoardCode)` — enrichment,均值差 +0.62,p 0.013
24. `ts_med(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 50)` — enrichment,均值差 +0.58,p 0.058
25. `pow_2_5(pow_2_5(day_durbin_watson(Volume)))` — enrichment,均值差 +0.57,p 0.094
26. `cross_semistd_pos(pow_1_5(LimitWidth), 60)` — enrichment,均值差 +0.53,p 0.014
27. `day_topw_mean(High, Open)` — enrichment,均值差 +0.48,p 0.050
28. `ts_med(LimitWidth, 50)` — enrichment,均值差 +0.44,p 0.000
29. `day_durbin_watson(Volume)` — enrichment,均值差 +0.32,p 0.006
30. `day_signed_ratio(Ret, Amt)` — enrichment,均值差 +0.30,p 0.031
31. `day_corr(Ret, Volume)` — enrichment,均值差 +0.19,p 0.079

## 本组之前各轮的任务

- `c08s801Pr1a_Ea`:核心 `day_durbin_watson(Volume)`;评分 97,过线 4,入 heads 1;采样计数 {'c05_no_core': 1821, 'c05_periphery_seen': 7}
  - score +0.64(train +0.64 valid +1.39):`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)`
  - score +0.59(train +0.59 valid +0.75):`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 30)`
  - score +0.55(train +0.94 valid +0.55):`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_sum(Volume), day_durbin_watson(Volume)), 30)`
  - score +0.51(train +1.00 valid +0.51):`ts_corr(cs_last_low10(day_centroid(Volume), cross_corr(day_sum(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, High), day_durbin_watson(Volume)), 40)`
  - score +0.42(train +0.42 valid +0.49):`cs_last_low10(day_centroid(Volume), cs_last_low10(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)))`
- `c08s801Pr1b_Nb`:核心 `—`;评分 76,过线 0,入 heads 0;采样计数 {}
  - score +0.30(train +0.30 valid +1.35):`cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 20), cross_mean(day_mean(Ret), 20))`
  - score +0.30(train +0.30 valid +1.39):`cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Volume), 20), cross_mean(day_mean(Ret), 20))`
  - score +0.10(train +0.10 valid +0.56):`cross_mean(day_corr(Ret, Volume), 60)`
  - score +0.09(train +0.09 valid +1.37):`cross_mean(sub(cross_mean(day_corr(Ret, Volume), 60), day_corr(Ret, Volume)), 60)`
  - score +0.07(train +0.07 valid +0.57):`cross_mean(sub(day_wmean(Ret, Volume), day_corr(Ret, Volume)), 60)`
- `c08s801Pr2a_Ea`:核心 `day_centroid(Volume)`;评分 82,过线 19,入 heads 4;采样计数 {'c05_no_core': 713, 'c05_periphery_seen': 6}
  - score +1.50(train +1.50 valid +1.63):`cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), cross_mean(ts_kurt(day_min(Ret), 5), 20))`
  - score +1.49(train +1.68 valid +1.49):`cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(day_sum(Amt), 20))`
  - score +1.49(train +1.68 valid +1.49):`cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), cross_mean(day_sum(Amt), 20))`
  - score +1.49(train +1.68 valid +1.49):`cs_bucket_rank(cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(day_sum(Amt), 20)), cross_mean(day_sum(Amt), 20))`
  - score +1.32(train +1.38 valid +1.32):`cs_bucket_rank(cross_mean(day_centroid(Volume), 20), cross_mean(day_sum(Ret), 20))`
- `c08s801Pr2b_Eb`:核心 `ts_med(LimitWidth, 50)`;评分 103,过线 2,入 heads 1;采样计数 {'c05_no_core': 1975, 'c05_periphery_seen': 8, 'mutation_refused': 2}
  - score +0.77(train +0.77 valid +1.95):`cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 50), mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt))), 20)`
  - score +0.68(train +0.68 valid +1.89):`cross_mean(mul(ts_med(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 50), day_signed_ratio(Ret, Amt)), 20)`
  - score +0.17(train +0.17 valid +1.72):`cross_mean(mul(ts_med(mul(mul(ts_med(mul(ts_med(LimitWidth, 50), day_signed_ratio(Ret, Amt)), 50), day_signed_ratio(Ret, Amt)), day_signed_ratio(Ret, Amt)), 50), day_signed_ratio(Ret, Amt)), 20)`
  - score -0.01(train +0.11 valid -0.01):`cs_first_low40(ts_med(pow_2(cs_last_high05(cs_bucket_rank(ts_hurst(LimitWidth, 50), BoardCode), ts_med(LimitWidth, 50))), 50), day_product(Ret))`
  - score -0.07(train -0.07 valid +0.08):`pow_2(cs_last_high05(cs_bucket_rank(ts_hurst(LimitWidth, 50), BoardCode), ts_med(LimitWidth, 50)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.17(knockout ts_kurt(day_min(Ret), 5)):`cs_bucket_rank(cross_mean(abs_(day_centroid(Volume)), 20), cross_mean(day_min(Ret), 20))`
