# 定位:种子 908,P 组,第 3 轮(只含 train / valid)

快照:prods908M1_I0_open_search, prods908M2_I0_open_search, prods908M3_I0_open_search, prods908Pr1a_Ea, prods908Pr1b_Nb, prods908Pr2a_Ea, prods908Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(19 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +2.10 | +2.14 | +2.10 | +1 | 5 | prods908Pr2b_Nb | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60)` |
| +1.95 | +1.95 | +2.10 | +1 | 5 | prods908Pr2b_Nb | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` |
| +1.92 | +1.92 | +1.96 | -1 | 5 | prods908Pr1b_Nb | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20)` |
| +1.58 | +1.69 | +1.58 | -1 | 5 | prods908Pr1a_Ea | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)` |
| +1.25 | +1.25 | +1.25 | +1 | 20 | prods908Pr1b_Nb | `sub(day_centroid(Ret), mul(day_centroid(Volume), 3))` |
| +1.20 | +1.20 | +1.77 | -1 | 5 | prods908Pr2b_Nb | `cross_corr(day_first(Amt), day_centroid(Amt), 60)` |
| +1.02 | +1.04 | +1.02 | +1 | 5 | prods908M1_I0_open_search | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 50)` |
| +1.01 | +1.01 | +1.11 | -1 | 20 | prods908Pr2a_Ea | `cs_regres(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), inv(day_flat_run_max(Low)))` |
| +0.96 | +0.98 | +0.96 | -1 | 20 | prods908Pr1a_Ea | `ts_min(day_centroid(Amt), 20)` |
| +0.91 | +0.91 | +1.51 | -1 | 5 | prods908Pr2b_Nb | `cross_corr(add(div(day_first(Volume), day_es_ratio_hi(Volume)), day_es_ratio_hi(Volume)), add(day_first(Volume), cross_corr(day_first(Amt), day_kurt(Amt), 60)), 60)` |
| +0.85 | +0.85 | +1.12 | -1 | 20 | prods908Pr1a_Ea | `cs_first_low40(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)` |
| +0.80 | +0.80 | +1.72 | -1 | 5 | prods908Pr2b_Nb | `cross_corr(day_centroid(Amt), day_es_ratio_hi(Amt), 60)` |
| +0.80 | +0.80 | +1.82 | +1 | 5 | prods908Pr2b_Nb | `cross_corr(day_first(Amt), day_gini(Amt), 60)` |
| +0.73 | +0.73 | +0.89 | +1 | 5 | prods908M1_I0_open_search | `cs_bucket_zscore(day_median(High), day_wmean(Open, Amt))` |
| +0.70 | +0.70 | +1.86 | +1 | 5 | prods908Pr2b_Nb | `cs_bucket_demean(cross_mean(div(day_first(Amt), day_sum(Amt)), 60), LogFloatCap)` |
| +0.68 | +1.19 | +0.68 | +1 | 0 | prods908M3_I0_open_search | `cross_regalpha(pow_05(cs_regres(add(LogFloatShares, day_wmean(Close, Amt)), cs_quantile_q75(add(LogFloatShares, day_wmean(Close, Amt))))), ListAge, 241)` |
| +0.65 | +0.65 | +2.08 | +1 | 5 | prods908M3_I0_open_search | `pow_05(cs_regres(add(LogFloatShares, pow_05(cs_regres(day_wmean(Close, Amt), cs_quantile_q75(day_open(High))))), cs_quantile_q75(day_open(High))))` |
| +0.63 | +0.63 | +1.59 | +1 | 5 | prods908Pr2b_Nb | `sub(cross_mean(div(day_first(Amt), day_sum(Amt)), 60), cross_mean(div(day_last(Amt), day_sum(Amt)), 60))` |
| +0.53 | +0.53 | +1.26 | +1 | 20 | prods908Pr2b_Nb | `cross_corr(div(day_first(Volume), day_es_ratio_hi(Volume)), day_es_ratio_hi(Volume), 30)` |

## 共性:546 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.14 | 0.000 | 26 | +1.08 / -1.06 | `day_first(Volume)` |
| +1.78 | 0.001 | 5 | +0.81 / -0.97 | `div(day_first(Amt), day_sum(Amt))` |
| +1.72 | 0.007 | 4 | +0.75 / -0.97 | `add(div(day_first(Volume), day_es_ratio_hi(Volume)), day_es_ratio_hi(Volume))` |
| +1.61 | 0.000 | 10 | +0.63 / -0.98 | `div(day_first(Volume), day_es_ratio_hi(Volume))` |
| +1.60 | 0.000 | 27 | +0.57 / -1.03 | `day_es_ratio_hi(Volume)` |
| +1.50 | 0.000 | 28 | +0.47 / -1.03 | `day_first(Amt)` |
| +1.41 | 0.018 | 4 | +0.45 / -0.96 | `inv(day_flat_run_max(Close))` |
| +1.41 | 0.000 | 22 | +0.40 / -1.01 | `day_es_ratio_hi(Amt)` |
| +1.29 | 0.005 | 7 | +0.32 / -0.97 | `cs_regres(add(LogFloatShares, day_wmean(Close, Amt)), cs_quantile_q75(add(LogFloatShares, day_wmean(Close, Amt))))` |
| +1.25 | 0.019 | 5 | +0.29 / -0.97 | `pow_05(cs_regres(add(LogFloatShares, day_wmean(Close, Amt)), cs_quantile_q75(add(LogFloatShares, day_wmean(Close, Amt)))))` |
| +1.19 | 0.004 | 9 | +0.22 / -0.97 | `cs_quantile_q75(add(LogFloatShares, day_wmean(Close, Amt)))` |
| +1.17 | 0.013 | 7 | +0.20 / -0.97 | `day_flat_run_max(Close)` |
| +1.13 | 0.052 | 4 | +0.17 / -0.96 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| +1.09 | 0.054 | 4 | +0.13 / -0.96 | `day_kurt(Volume)` |
| +1.07 | 0.041 | 4 | +0.11 / -0.96 | `day_at_max_ratio(in_slice(Amt, 211, 240))` |
| +1.07 | 0.024 | 5 | +0.10 / -0.96 | `cs_regres(ListAge, day_centroid(Amt))` |
| +1.06 | 0.058 | 4 | +0.10 / -0.96 | `cs_quantile_q75(day_wmean(Close, Amt))` |
| +1.06 | 0.065 | 8 | +0.09 / -0.97 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| +1.03 | 0.041 | 5 | +0.06 / -0.96 | `day_sum(Close)` |
| +1.01 | 0.082 | 7 | +0.04 / -0.97 | `cross_corr(day_first(Amt), day_kurt(Amt), 60)` |

## 拆解(22 次评估)

### head score +2.10:`cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(Amt)` | -1.39 | -1.39 | -0.14 | — | (子树本身) |
| sufficiency | `day_es_ratio_hi(Volume)` | -5.46 | -3.98 | -5.46 | — | (子树本身) |
| swap | `Amt->Volume` | +2.04 | +2.11 | +2.04 | — | `cross_reg_fvalue(day_first(Volume), day_es_ratio_hi(Volume), 60)` |
| swap | `Volume->Amt` | +2.18 | +2.18 | +2.25 | — | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Amt), 60)` |
| window | `cross_reg_fvalue@60->30` | +0.52 | +0.52 | +1.44 | — | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 30)` |
| window | `cross_reg_fvalue@60->120` | +1.58 | +1.58 | +1.68 | — | `cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 120)` |

### head score +1.95:`cross_corr(day_first(Amt), day_kurt(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(Amt)` | -1.39 | -1.39 | -0.14 | — | (子树本身) |
| sufficiency | `day_kurt(Amt)` | -6.18 | -3.86 | -6.18 | — | (子树本身) |
| swap | `Amt->Volume` | +1.67 | +1.67 | +1.95 | — | `cross_corr(day_first(Volume), day_kurt(Volume), 60)` |
| window | `cross_corr@60->30` | +0.59 | +0.59 | +2.90 | — | `cross_corr(day_first(Amt), day_kurt(Amt), 30)` |
| window | `cross_corr@60->120` | +0.98 | +0.98 | +2.23 | — | `cross_corr(day_first(Amt), day_kurt(Amt), 120)` |

### head score +1.92:`cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt))` | +0.72 | +1.22 | +0.72 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Amt, 196, 240))` | -2.00 | -2.00 | -1.58 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt))` | -1.82 | -1.82 | -1.71 | +3.74 | `cross_mean(day_sum(in_slice(Amt, 196, 240)), 20)` |
| swap | `Amt->Volume` | +1.86 | +1.86 | +2.05 | — | `cross_mean(div(day_sum(in_slice(Volume, 196, 240)), day_sum(Volume)), 20)` |
| window | `cross_mean@20->10` | +1.76 | +1.76 | +2.19 | — | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 10)` |
| window | `cross_mean@20->40` | +1.65 | +1.65 | +2.39 | — | `cross_mean(div(day_sum(in_slice(Amt, 196, 240)), day_sum(Amt)), 40)` |

### head score +1.25:`sub(day_centroid(Ret), mul(day_centroid(Volume), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Ret)` | -2.89 | -1.77 | -2.89 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `mul(day_centroid(Volume), 3)` | +0.63 | +0.63 | +0.73 | +0.61 | `sub(day_centroid(Ret), day_centroid(Volume))` |
| swap | `Volume->Amt` | +1.20 | +1.20 | +1.22 | — | `sub(day_centroid(Ret), mul(day_centroid(Amt), 3))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_first(Volume)` — enrichment,均值差 +2.14,p 0.000
2. `div(day_first(Amt), day_sum(Amt))` — enrichment,均值差 +1.78,p 0.001
3. `add(div(day_first(Volume), day_es_ratio_hi(Volume)), day_es_ratio_hi(Volume))` — enrichment,均值差 +1.72,p 0.007
4. `div(day_first(Volume), day_es_ratio_hi(Volume))` — enrichment,均值差 +1.61,p 0.000
5. `day_es_ratio_hi(Volume)` — enrichment,均值差 +1.60,p 0.000
6. `day_first(Amt)` — enrichment,均值差 +1.50,p 0.000
7. `inv(day_flat_run_max(Close))` — enrichment,均值差 +1.41,p 0.018
8. `day_es_ratio_hi(Amt)` — enrichment,均值差 +1.41,p 0.000
9. `cs_regres(add(LogFloatShares, day_wmean(Close, Amt)), cs_quantile_q75(add(LogFloatShares, day_wmean(Close, Amt))))` — enrichment,均值差 +1.29,p 0.005
10. `pow_05(cs_regres(add(LogFloatShares, day_wmean(Close, Amt)), cs_quantile_q75(add(LogFloatShares, day_wmean(Close, Amt)))))` — enrichment,均值差 +1.25,p 0.019
11. `day_flat_run_max(Close)` — enrichment,均值差 +1.17,p 0.013
12. `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` — enrichment,均值差 +1.13,p 0.052
13. `day_kurt(Volume)` — enrichment,均值差 +1.09,p 0.054
14. `day_at_max_ratio(in_slice(Amt, 211, 240))` — enrichment,均值差 +1.07,p 0.041
15. `cs_regres(ListAge, day_centroid(Amt))` — enrichment,均值差 +1.07,p 0.024
16. `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` — enrichment,均值差 +1.06,p 0.065
17. `day_sum(Close)` — enrichment,均值差 +1.03,p 0.041
18. `cross_corr(day_first(Amt), day_kurt(Amt), 60)` — enrichment,均值差 +1.01,p 0.082
19. `cs_regres(add(LogFloatShares, day_wmean(Close, Amt)), cs_quantile_q75(day_open(High)))` — enrichment,均值差 +0.98,p 0.032
20. `cs_regres(ListAge, pow_3(day_centroid(Amt)))` — enrichment,均值差 +0.97,p 0.016
21. `day_centroid(Volume)` — enrichment,均值差 +0.95,p 0.006
22. `sub(day_centroid(Ret), day_centroid(Volume))` — enrichment,均值差 +0.88,p 0.095
23. `day_centroid(Amt)` — enrichment,均值差 +0.82,p 0.000
24. `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` — enrichment,均值差 +0.81,p 0.000
25. `pow_3(day_centroid(Amt))` — enrichment,均值差 +0.76,p 0.027
26. `day_sum(in_slice(Amt, 211, 240))` — enrichment,均值差 +0.72,p 0.000
27. `day_open(High)` — enrichment,均值差 +0.62,p 0.008
28. `add(LogFloatShares, day_wmean(Close, Amt))` — enrichment,均值差 +0.55,p 0.040
29. `cross_mean(day_centroid(Amt), 20)` — enrichment,均值差 +0.54,p 0.063
30. `day_kurt(Amt)` — enrichment,均值差 +0.52,p 0.031
31. `day_wmean(Close, Amt)` — enrichment,均值差 +0.50,p 0.037
32. `day_sum(Amt)` — enrichment,均值差 +0.34,p 0.001

## 本组之前各轮的任务

- `prods908Pr1a_Ea`:核心 `day_centroid(Amt)`;评分 78,过线 16,入 heads 3;采样计数 {'c05_periphery_seen': 7, 'c05_no_core': 1561}
  - score +1.58(train +1.69 valid +1.58):`cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)`
  - score +1.58(train +1.69 valid +1.58):`cs_regres(cs_bucket_zscore(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares), LogFloatShares)`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares), LogFloatShares), LogFloatShares)`
- `prods908Pr1b_Nb`:核心 `—`;评分 77,过线 5,入 heads 2;采样计数 {}
  - score +1.81(train +1.94 valid +1.81):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)`
  - score +1.81(train +1.94 valid +1.81):`cross_mean(div(sub(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), day_sum(Amt)), 20)`
  - score +1.19(train +1.69 valid +1.19):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 15)`
  - score +0.93(train +0.93 valid +1.42):`sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centroid(Volume))`
  - score +0.63(train +0.63 valid +0.73):`sub(day_centroid(Ret), day_centroid(Volume))`
- `prods908Pr2a_Ea`:核心 `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))`;评分 78,过线 5,入 heads 1;采样计数 {'c05_no_core': 934, 'c05_periphery_seen': 10}
  - score +1.01(train +1.01 valid +1.11):`cs_regres(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), inv(day_flat_run_max(Low)))`
  - score +0.97(train +0.97 valid +1.18):`cs_regres(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), inv(day_flat_run_max(Close)))`
  - score +0.83(train +0.87 valid +0.83):`cs_regres(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), inv(day_flat_run_max(Ret)))`
  - score +0.77(train +0.77 valid +1.33):`cs_regres(div(cs_regres(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), inv(day_flat_run_max(Close))), day_sum(Amt)), inv(day_flat_run_max(Close)))`
  - score +0.62(train +1.13 valid +0.62):`cs_regres(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), inv(day_sum(Close)))`
- `prods908Pr2b_Nb`:核心 `—`;评分 89,过线 33,入 heads 9;采样计数 {}
  - score +2.10(train +2.14 valid +2.10):`cross_reg_fvalue(day_first(Amt), day_es_ratio_hi(Volume), 60)`
  - score +1.95(train +1.95 valid +2.10):`cross_corr(day_first(Amt), day_kurt(Amt), 60)`
  - score +1.93(train +1.93 valid +2.22):`cross_corr(add(day_first(Volume), cross_corr(day_first(Volume), day_kurt(Amt), 60)), day_es_ratio_hi(Amt), 60)`
  - score +1.93(train +1.93 valid +2.22):`cross_corr(add(day_first(Volume), cross_corr(day_first(Amt), day_kurt(Amt), 60)), day_es_ratio_hi(Amt), 60)`
  - score +1.93(train +1.93 valid +2.22):`cross_corr(add(day_first(Volume), cross_corr(day_first(Amt), cross_corr(day_first(Amt), day_kurt(Amt), 60), 60)), day_es_ratio_hi(Amt), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
