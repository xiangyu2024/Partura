# 定位:种子 2069,P 组,第 2 轮(只含 train / valid)

快照:prods2069M1_I0_open_search, prods2069M2_I0_open_search, prods2069Pr1a_Ea, prods2069Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.92 | -1.45 | -1.92 | -1 | 5 | prods2069M2_I0_open_search | `cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)` |
| -2.31 | -2.16 | -2.31 | -1 | 20 | prods2069M1_I0_open_search | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_sum(Amt), day_sum(Volume)), 4), 2)), ts_rank(ts_decay_linear(mul(div(ts_delta(add(mul(day_first(Open), 0.147155), mul(day_min(Low), sub(create_like(day_last(Close), 1), 0.147155))), 2), add(mul(day_first(Open), 0.147155), mul(day_min(Low), sub(create_like(day_last(Close), 1), 0.147155)))), -1), 3), 16)), -1)` |
| -2.50 | -2.50 | -1.57 | +1 | 20 | prods2069M1_I0_open_search | `pairwise_min(cs_rank(ts_decay_linear(sub(add(div(add(day_max(High), day_min(Low)), 2), day_max(High)), add(div(day_sum(Amt), day_sum(Volume)), day_max(High))), 20)), cs_rank(ts_decay_linear(ts_corr(div(add(day_max(High), day_min(Low)), 2), ts_mean(day_sum(Volume), 40), 3), 5)))` |
| -2.56 | -1.97 | -2.56 | +1 | 20 | prods2069M2_I0_open_search | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)` |
| -2.66 | -2.66 | -1.73 | +1 | 20 | prods2069M2_I0_open_search | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)` |
| -2.75 | -2.75 | -1.99 | +1 | 20 | prods2069M1_I0_open_search | `sub(cs_rank(ts_decay_linear(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4), 7)), cs_rank(ts_decay_linear(ts_rank(ts_argmin(ts_corr(cs_rank(day_first(Open)), cs_rank(ts_mean(day_sum(Volume), 15)), 20), 8), 6), 8)))` |

## 共性:153 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.18 | 0.000 | 32 | -0.72 / -2.90 | `day_std(Amt)` |
| +1.95 | 0.001 | 5 | -0.56 / -2.51 | `ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` |
| +1.86 | 0.000 | 38 | -1.04 / -2.91 | `cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4))` |
| +1.81 | 0.000 | 20 | -0.87 / -2.68 | `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5)` |
| +1.77 | 0.000 | 39 | -1.12 / -2.90 | `cs_rank(cross_mean(day_skew(Ret), 20))` |
| +1.76 | 0.000 | 22 | -0.94 / -2.70 | `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20)))` |
| +1.76 | 0.000 | 44 | -1.19 / -2.95 | `day_skew(Ret)` |
| +1.74 | 0.000 | 18 | -0.91 / -2.65 | `ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26)` |
| +1.70 | 0.000 | 41 | -1.20 / -2.90 | `cross_mean(day_skew(Ret), 20)` |
| +1.69 | 0.000 | 8 | -0.84 / -2.53 | `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` |
| +1.66 | 0.009 | 4 | -0.82 / -2.49 | `cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5)` |
| +1.65 | 0.001 | 7 | -0.86 / -2.52 | `cross_mean(day_skew(Low), 20)` |
| +1.65 | 0.001 | 7 | -0.86 / -2.52 | `day_skew(Low)` |
| +1.57 | 0.004 | 6 | -0.93 / -2.50 | `cs_rank(cross_mean(day_skew(Low), 20))` |
| +1.36 | 0.017 | 5 | -1.13 / -2.49 | `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20)))` |
| +1.16 | 0.054 | 4 | -1.31 / -2.47 | `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5)` |
| +0.67 | 0.003 | 77 | -2.11 / -2.78 | `ts_mean(day_sum(Volume), 5)` |
| +0.67 | 0.003 | 77 | -2.11 / -2.78 | `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)` |
| +0.67 | 0.003 | 77 | -2.11 / -2.78 | `ts_sum(ts_mean(day_sum(Volume), 5), 26)` |
| +0.61 | 0.009 | 81 | -2.16 / -2.77 | `div(day_sum(Amt), day_sum(Volume))` |

## 拆解(15 次评估)

### head score -1.92:`cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50))` | -4.97 | -4.59 | -4.97 | — | (子树本身) |
| swap | `High->Low` | -3.04 | -3.04 | -2.34 | — | `cross_mean(day_mean(in_regbeta(in_max_rolling(Low, 50), in_min_rolling(Low, 50), 50)), 20)` |
| swap | `Low->High` | -1.95 | -1.68 | -1.95 | — | `cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(High, 50), 50)), 20)` |
| window | `cross_mean@20->10` | -2.21 | -2.14 | -2.21 | — | `cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 10)` |
| window | `cross_mean@20->40` | -1.35 | -1.19 | -1.35 | — | `cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 40)` |

### head score -2.56:`cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50))` | -4.97 | -4.59 | -4.97 | — | (子树本身) |
| swap | `High->Low` | -1.85 | -1.63 | -1.85 | — | `cross_stddev(day_mean(in_regbeta(in_max_rolling(Low, 50), in_min_rolling(Low, 50), 50)), 20)` |
| swap | `Low->High` | -2.26 | -1.90 | -2.26 | — | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(High, 50), 50)), 20)` |
| window | `cross_stddev@20->10` | -2.62 | -2.14 | -2.62 | — | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 10)` |
| window | `cross_stddev@20->40` | -2.42 | -1.83 | -2.42 | — | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 40)` |

### head score -2.66:`cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50))` | -3.62 | -3.62 | -1.95 | — | (子树本身) |
| swap | `High->Low` | -2.87 | -2.87 | -2.10 | — | `cross_mean(day_mean(in_corr(in_max_rolling(Low, 50), in_min_rolling(Low, 50), 50)), 20)` |
| swap | `Low->High` | -2.74 | -2.74 | -1.72 | — | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(High, 50), 50)), 20)` |
| window | `cross_mean@20->10` | -2.91 | -2.91 | -1.83 | — | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 10)` |
| window | `cross_mean@20->40` | -2.60 | -2.60 | -1.96 | — | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_std(Amt)` — enrichment,均值差 +2.18,p 0.000
2. `ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` — enrichment,均值差 +1.95,p 0.001
3. `cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4))` — enrichment,均值差 +1.86,p 0.000
4. `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5)` — enrichment,均值差 +1.81,p 0.000
5. `cs_rank(cross_mean(day_skew(Ret), 20))` — enrichment,均值差 +1.77,p 0.000
6. `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20)))` — enrichment,均值差 +1.76,p 0.000
7. `day_skew(Ret)` — enrichment,均值差 +1.76,p 0.000
8. `ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26)` — enrichment,均值差 +1.74,p 0.000
9. `cross_mean(day_skew(Ret), 20)` — enrichment,均值差 +1.70,p 0.000
10. `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4)` — enrichment,均值差 +1.69,p 0.000
11. `cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5)` — enrichment,均值差 +1.66,p 0.009
12. `cross_mean(day_skew(Low), 20)` — enrichment,均值差 +1.65,p 0.001
13. `day_skew(Low)` — enrichment,均值差 +1.65,p 0.001
14. `cs_rank(cross_mean(day_skew(Low), 20))` — enrichment,均值差 +1.57,p 0.004
15. `mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20)))` — enrichment,均值差 +1.36,p 0.017
16. `ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5)` — enrichment,均值差 +1.16,p 0.054
17. `ts_mean(day_sum(Volume), 5)` — enrichment,均值差 +0.67,p 0.003
18. `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)` — enrichment,均值差 +0.67,p 0.003
19. `ts_sum(ts_mean(day_sum(Volume), 5), 26)` — enrichment,均值差 +0.67,p 0.003
20. `div(day_sum(Amt), day_sum(Volume))` — enrichment,均值差 +0.61,p 0.009
21. `day_sum(Amt)` — enrichment,均值差 +0.50,p 0.012

## 本组之前各轮的任务

- `prods2069Pr1a_Ea`:核心 `ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)`;评分 89,过线 0,入 heads 0;采样计数 {'c05_no_core': 400, 'c05_skeleton': 197, 'c05_periphery_seen': 1}
  - score +0.04(train +0.04 valid +0.26):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(cs_last_high10(cross_mean(ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_std(Amt)), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5), 26), 5), 26), 4), 5), day_std(Amt))`
  - score -0.02(train +0.07 valid -0.02):`cs_last_high10(cross_max(ts_corr(day_sum(Volume), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_std(Amt))`
  - score -0.06(train +0.08 valid -0.06):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Low), 20))), 5), 26), 5), 26), 4), 5), day_std(Amt))`
  - score -0.13(train +0.24 valid -0.13):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 5), day_std(Amt))`
  - score -0.16(train +0.41 valid -0.16):`cs_last_high10(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(mul(cs_rank(ts_corr(div(day_sum(Amt), day_sum(Volume)), ts_sum(ts_mean(day_sum(Volume), 5), 26), 4)), cs_rank(cross_mean(day_skew(Ret), 20))), 5), 26), 4), 20))), 5), 26), 4), 5), day_std(Amt))`
- `prods2069Pr1b_Nb`:核心 `—`;评分 103,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.28(train -0.28 valid +0.34):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), cross_mean(cross_mean(day_skew(Ret), 20), 20)), 20)), cs_rank(cross_mean(cross_mean(day_skew(Ret), 20), 20)))`
  - score -0.47(train -0.47 valid +0.10):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), cross_mean(day_skew(Ret), 20)), 20)), cs_rank(cross_mean(day_skew(Ret), 20)))`
  - score -0.57(train -0.34 valid -0.57):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), cs_rank(cross_mean(day_skew(Ret), 60))))`
  - score -0.74(train -0.74 valid -0.09):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), cs_rank(cross_mean(day_skew(Ret), 20)))`
  - score -0.92(train -0.92 valid -0.55):`mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), mul(cs_rank(cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 20)), cs_rank(cross_mean(day_skew(Ret), 20))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.71(swap High->Low):`cross_stddev(day_mean(in_regbeta(in_max_rolling(Low, 50), in_min_rolling(Low, 50), 50)), 20)`
- 增益 +0.57(window cross_mean@20->40):`cross_mean(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 40)`
- 增益 +0.31(swap Low->High):`cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(High, 50), 50)), 20)`
- 增益 +0.14(window cross_stddev@20->40):`cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50)), 40)`
