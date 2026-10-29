# 定位:种子 803,B 组,第 3 轮(只含 train / valid)

快照:c05s803M1_I0_open_search, c05s803M2_I0_open_search, c05s803M3_I0_open_search, c05s803Br1a_Ea, c05s803Br1b_Nb, c05s803Br2a_Ea, c05s803Br2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(8 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.81 | +1.81 | +2.51 | -1 | 20 | c05s803M2_I0_open_search | `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 6)` |
| +1.43 | +1.43 | +2.22 | -1 | 5 | c05s803M2_I0_open_search | `ts_skew(day_var(Ret), 50)` |
| +1.41 | +1.41 | +1.68 | -1 | 5 | c05s803Br2a_Ea | `mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))` |
| +1.16 | +1.16 | +1.33 | +1 | 20 | c05s803Br2b_Nb | `ts_skew(div(day_first(Open), ts_delay(day_last(Close), 1)), 50)` |
| +0.97 | +0.97 | +1.54 | -1 | 20 | c05s803M1_I0_open_search | `day_kurt(Ret)` |
| +0.90 | +0.90 | +1.05 | -1 | 20 | c05s803Br1b_Nb | `sub(day_centroid(Amt), day_centroid(Ret))` |
| +0.73 | +0.73 | +2.30 | +1 | 5 | c05s803Br1a_Ea | `cross_corr(day_kurt(Ret), day_gini(Ret), 241)` |
| +0.53 | +0.53 | +0.78 | -1 | 20 | c05s803Br1b_Nb | `sub(day_centroid(Amt), LogFloatShares)` |

## 共性:424 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.77 | 0.002 | 4 | +0.48 / -1.29 | `neg(LogFloatShares)` |
| +1.57 | 0.013 | 5 | +0.28 / -1.29 | `ts_skew(day_durbin_watson(Open), 40)` |
| +1.37 | 0.004 | 5 | +0.08 / -1.29 | `cs_last_low10(cs_last_low10(LimitWidth, LimitWidth), cs_last_low10(LimitWidth, LimitWidth))` |
| +1.27 | 0.000 | 20 | -0.06 / -1.33 | `cs_last_low10(LimitWidth, LimitWidth)` |
| +1.23 | 0.019 | 4 | -0.06 / -1.29 | `cs_last_low05(cross_stddev(LimitWidth, 10), cross_stddev(LimitWidth, 10))` |
| +1.16 | 0.000 | 36 | -0.21 / -1.37 | `cross_stddev(LimitWidth, 10)` |
| +1.10 | 0.038 | 4 | -0.18 / -1.28 | `day_flat_ratio(sqrt(sqrt(Ret)))` |
| +1.04 | 0.004 | 11 | -0.26 / -1.30 | `cs_last_low05(cross_stddev(LimitWidth, 10), ts_std(day_ar1_coefficient(Close), 50))` |
| +1.03 | 0.067 | 5 | -0.26 / -1.29 | `cs_rank(cross_mean(day_sum(Amt), 20))` |
| +1.01 | 0.018 | 6 | -0.28 / -1.29 | `cs_state_rank(day_ar1_coefficient(Close), 50)` |
| +1.00 | 0.052 | 6 | -0.29 / -1.29 | `cross_mean(day_sum(Amt), 20)` |
| +0.99 | 0.012 | 11 | -0.31 / -1.30 | `day_centroid(Amt)` |
| +0.96 | 0.017 | 7 | -0.33 / -1.29 | `cs_last_low05(cross_stddev(LimitWidth, 10), day_ar1_coefficient(Close))` |
| +0.91 | 0.115 | 5 | -0.37 / -1.28 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.76 | 0.000 | 54 | -0.61 / -1.37 | `day_flat_ratio(sqrt(Ret))` |
| +0.74 | 0.044 | 9 | -0.55 / -1.29 | `ts_delay(ts_skew(day_gini(Amt), 50), 1)` |
| +0.67 | 0.175 | 4 | -0.61 / -1.28 | `cs_rank(ts_corr(log(day_durbin_watson(Open)), day_sum(Ret), 50))` |
| +0.63 | 0.052 | 13 | -0.66 / -1.29 | `ts_skew(day_gini(Amt), 50)` |
| +0.63 | 0.011 | 62 | -0.74 / -1.37 | `day_durbin_watson(Open)` |
| +0.56 | 0.182 | 13 | -0.74 / -1.29 | `ts_delay(day_last(Close), 1)` |

## 拆解(31 次评估)

### head score +1.81:`cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 6)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_skew(day_durbin_watson(Open), 50)` | +1.18 | +1.18 | +2.26 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Open)` | -2.13 | -2.13 | -0.11 | — | (子树本身) |
| knockout | `ts_skew(day_durbin_watson(Open), 50)` | -2.32 | -1.79 | -2.32 | +4.13 | `cross_autocorr_s1(day_durbin_watson(Open), 6)` |
| swap | `Open->Close` | +1.89 | +1.89 | +2.56 | — | `cross_autocorr_s1(ts_skew(day_durbin_watson(Close), 50), 6)` |
| window | `cross_autocorr_s1@6->3` | +1.56 | +1.56 | +2.06 | — | `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 3)` |
| window | `cross_autocorr_s1@6->12` | +1.78 | +1.78 | +2.59 | — | `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 12)` |

### head score +1.43:`ts_skew(day_var(Ret), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_var(Ret)` | -1.55 | -1.55 | +0.13 | — | (子树本身) |
| window | `ts_skew@50->25` | +1.21 | +1.21 | +2.48 | — | `ts_skew(day_var(Ret), 25)` |
| window | `ts_skew@50->100` | +1.35 | +1.35 | +2.39 | — | `ts_skew(day_var(Ret), 100)` |

### head score +1.41:`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_skew(day_durbin_watson(Open), 50))` | +0.98 | +0.98 | +1.19 | — | (子树本身) |
| sufficiency | `ts_skew(day_durbin_watson(Open), 50)` | +1.18 | +1.18 | +2.26 | — | (子树本身) |
| sufficiency | `cs_rank(day_sum(Amt))` | -2.51 | -2.19 | -2.51 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Open)` | -2.13 | -2.13 | -0.11 | — | (子树本身) |
| knockout | `sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5)` | -0.43 | -0.43 | +0.06 | +1.84 | `mul(cs_rank(ts_skew(day_durbin_watson(Open), 50)), sub(cs_rank(day_sum(Amt)), 0.5))` |
| knockout | `cs_rank(ts_skew(day_durbin_watson(Open), 50))` | -2.59 | -2.14 | -2.59 | +4.00 | `mul(sub(ts_skew(day_durbin_watson(Open), 50), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))` |
| knockout | `sub(cs_rank(day_sum(Amt)), 0.5)` | -0.52 | +0.74 | -0.52 | +1.93 | `mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), cs_rank(day_sum(Amt)))` |
| knockout | `ts_skew(day_durbin_watson(Open), 50)` | +0.36 | +0.36 | +0.58 | +1.05 | `mul(sub(cs_rank(day_durbin_watson(Open)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))` |
| swap | `Open->Close` | +1.36 | +1.36 | +2.34 | — | `mul(sub(cs_rank(ts_skew(day_durbin_watson(Close), 50)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))` |
| swap | `Amt->Volume` | -0.08 | +0.22 | -0.08 | — | `mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(day_sum(Volume)), 0.5))` |
| window | `ts_skew@50->25` | +1.11 | +1.22 | +1.11 | — | `mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 25)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))` |
| window | `ts_skew@50->100` | +1.65 | +1.65 | +2.21 | — | `mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 100)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))` |

### head score +1.16:`ts_skew(div(day_first(Open), ts_delay(day_last(Close), 1)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_first(Open), ts_delay(day_last(Close), 1))` | -3.56 | -2.32 | -3.56 | — | (子树本身) |
| sufficiency | `ts_delay(day_last(Close), 1)` | -1.17 | -1.17 | -0.45 | — | (子树本身) |
| sufficiency | `day_first(Open)` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `day_last(Close)` | -1.13 | -1.13 | -0.29 | — | (子树本身) |
| knockout | `div(day_first(Open), ts_delay(day_last(Close), 1))` | -1.06 | -1.06 | -0.41 | +2.21 | `ts_skew(day_first(Open), 50)` |
| knockout | `ts_delay(day_last(Close), 1)` | -1.02 | -1.02 | +0.34 | +2.17 | `ts_skew(div(day_first(Open), day_last(Close)), 50)` |
| swap | `Open->Close` | +1.17 | +1.17 | +1.33 | — | `ts_skew(div(day_first(Close), ts_delay(day_last(Close), 1)), 50)` |
| swap | `Close->Vwap` | +1.09 | +1.09 | +1.18 | — | `ts_skew(div(day_first(Open), ts_delay(day_last(Vwap), 1)), 50)` |
| window | `ts_skew@50->25` | +0.35 | +1.06 | +0.35 | — | `ts_skew(div(day_first(Open), ts_delay(day_last(Close), 1)), 25)` |
| window | `ts_skew@50->100` | +0.69 | +0.69 | +1.56 | — | `ts_skew(div(day_first(Open), ts_delay(day_last(Close), 1)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_skew(day_durbin_watson(Open), 50)` — ablation,自身 score +1.18(所在 head +1.81)
2. `cs_rank(ts_skew(day_durbin_watson(Open), 50))` — ablation,自身 score +0.98(所在 head +1.41)
3. `neg(LogFloatShares)` — enrichment,均值差 +1.77,p 0.002
4. `ts_skew(day_durbin_watson(Open), 40)` — enrichment,均值差 +1.57,p 0.013
5. `cs_last_low10(cs_last_low10(LimitWidth, LimitWidth), cs_last_low10(LimitWidth, LimitWidth))` — enrichment,均值差 +1.37,p 0.004
6. `cs_last_low10(LimitWidth, LimitWidth)` — enrichment,均值差 +1.27,p 0.000
7. `cs_last_low05(cross_stddev(LimitWidth, 10), cross_stddev(LimitWidth, 10))` — enrichment,均值差 +1.23,p 0.019
8. `cross_stddev(LimitWidth, 10)` — enrichment,均值差 +1.16,p 0.000
9. `day_flat_ratio(sqrt(sqrt(Ret)))` — enrichment,均值差 +1.10,p 0.038
10. `cs_last_low05(cross_stddev(LimitWidth, 10), ts_std(day_ar1_coefficient(Close), 50))` — enrichment,均值差 +1.04,p 0.004
11. `cs_rank(cross_mean(day_sum(Amt), 20))` — enrichment,均值差 +1.03,p 0.067
12. `cs_state_rank(day_ar1_coefficient(Close), 50)` — enrichment,均值差 +1.01,p 0.018
13. `cross_mean(day_sum(Amt), 20)` — enrichment,均值差 +1.00,p 0.052
14. `day_centroid(Amt)` — enrichment,均值差 +0.99,p 0.012
15. `cs_last_low05(cross_stddev(LimitWidth, 10), day_ar1_coefficient(Close))` — enrichment,均值差 +0.96,p 0.017
16. `day_flat_ratio(sqrt(Ret))` — enrichment,均值差 +0.76,p 0.000
17. `ts_delay(ts_skew(day_gini(Amt), 50), 1)` — enrichment,均值差 +0.74,p 0.044
18. `ts_skew(day_gini(Amt), 50)` — enrichment,均值差 +0.63,p 0.052
19. `day_durbin_watson(Open)` — enrichment,均值差 +0.63,p 0.011
20. `day_first(Open)` — enrichment,均值差 +0.50,p 0.094
21. `day_ar1_coefficient(Close)` — enrichment,均值差 +0.48,p 0.008
22. `ts_std(day_ar1_coefficient(Close), 50)` — enrichment,均值差 +0.44,p 0.059
23. `day_gini(Amt)` — enrichment,均值差 +0.41,p 0.066

## 本组之前各轮的任务

- `c05s803Br1a_Ea`:核心 `day_kurt(Ret)`;评分 80,过线 1,入 heads 1;采样计数 {'c05_no_core': 1322, 'c05_skeleton': 30}
  - score +0.73(train +0.73 valid +2.30):`cross_corr(day_kurt(Ret), day_gini(Ret), 241)`
  - score -0.03(train -0.03 valid +1.50):`div(cross_fangzheng(day_kurt(Ret), 3), day_kurt(Ret))`
  - score -0.04(train +0.35 valid -0.04):`div(day_argmin(High), cross_corr(day_kurt(Ret), day_gini(Close), 20))`
  - score -0.14(train +0.20 valid -0.14):`cross_fangzheng(cross_fangzheng(cross_fangzheng(day_kurt(Ret), 15), 30), 15)`
  - score -0.16(train -0.16 valid +0.95):`div(day_argmin(Ret), day_kurt(Ret))`
- `c05s803Br1b_Nb`:核心 `—`;评分 65,过线 6,入 heads 2;采样计数 {}
  - score +0.90(train +0.90 valid +1.05):`sub(day_centroid(Amt), day_centroid(Ret))`
  - score +0.90(train +0.90 valid +1.05):`neg(sub(day_centroid(Amt), day_centroid(Ret)))`
  - score +0.90(train +0.90 valid +1.05):`neg(neg(sub(day_centroid(Amt), day_centroid(Ret))))`
  - score +0.53(train +0.53 valid +0.78):`sub(day_centroid(Amt), LogFloatShares)`
  - score +0.52(train +0.52 valid +0.84):`sub(neg(LogFloatShares), day_centroid(Ret))`
- `c05s803Br2a_Ea`:核心 `ts_skew(day_durbin_watson(Open), 50)`;评分 85,过线 4,入 heads 1;采样计数 {'c05_no_core': 1813, 'c05_skeleton': 33, 'mutation_refused': 2}
  - score +1.41(train +1.41 valid +1.68):`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))`
  - score +0.93(train +0.93 valid +1.19):`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(cross_mean(day_sum(Amt), 10)), 0.5))`
  - score +0.91(train +0.98 valid +0.91):`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(cross_mean(day_sum(Amt), 20)), 0.5))`
  - score +0.91(train +0.98 valid +0.91):`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(cs_rank(cross_mean(day_sum(Amt), 20))), 0.5))`
  - score +0.10(train +0.10 valid +0.24):`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 50)), 0.5), sub(cs_rank(ts_corr(log(day_durbin_watson(Open)), day_sum(Ret), 50)), 0.5))`
- `c05s803Br2b_Nb`:核心 `—`;评分 88,过线 1,入 heads 1;采样计数 {'c05_skeleton': 1}
  - score +1.16(train +1.16 valid +1.33):`ts_skew(div(day_first(Open), ts_delay(day_last(Close), 1)), 50)`
  - score +0.38(train +0.38 valid +0.58):`ts_skew(div(div(day_first(Open), ts_delay(ts_delay(day_last(Close), 1), 1)), ts_delay(ts_skew(day_gini(Amt), 50), 1)), 50)`
  - score +0.37(train +0.37 valid +0.38):`ts_skew(div(div(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(ts_skew(day_gini(Amt), 50), 1)), 50)`
  - score +0.35(train +0.35 valid +0.51):`ts_skew(div(day_first(Open), ts_delay(ts_skew(day_gini(Amt), 50), 1)), 50)`
  - score +0.12(train +0.12 valid +1.38):`div(cross_semistd_pos(day_sum(Amt), 50), cross_semistd_neg(day_sum(Amt), 50))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(window ts_skew@50->100):`mul(sub(cs_rank(ts_skew(day_durbin_watson(Open), 100)), 0.5), sub(cs_rank(day_sum(Amt)), 0.5))`
