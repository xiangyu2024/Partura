# 定位:种子 2042,P 组,第 3 轮(只含 train / valid)

快照:prods2042M1_I0_open_search, prods2042M2_I0_open_search, prods2042M3_I0_open_search, prods2042Pr1a_Ea, prods2042Pr1b_Nb, prods2042Pr2a_Ea, prods2042Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.86 | +0.86 | +1.07 | +1 | 5 | prods2042Pr1a_Ea | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Vwap), add(day_kurt(Vwap), 4))), 241), sub(LogFloatCap, LogFloatShares))` |
| +0.64 | +0.64 | +0.75 | +1 | 0 | prods2042M1_I0_open_search | `cs_bucket_zscore(ts_std(day_kurt(High), 240), LogFloatCap)` |
| -0.92 | -0.92 | -0.58 | +1 | 0 | prods2042M2_I0_open_search | `cross_sum(day_kurt(Vwap), 241)` |
| -1.12 | -1.09 | -1.12 | +1 | 0 | prods2042M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)` |
| -1.63 | -1.63 | -0.71 | -1 | 0 | prods2042M1_I0_open_search | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 241))` |
| -1.78 | -1.78 | -1.15 | -1 | 0 | prods2042M2_I0_open_search | `neg(cross_sum(day_kurt(Low), 241))` |
| -1.86 | -1.69 | -1.86 | +1 | 20 | prods2042M2_I0_open_search | `cross_sum(day_kurt(Vwap), 15)` |
| -2.03 | -1.78 | -2.03 | +1 | 20 | prods2042M3_I0_open_search | `cross_sum(pow_2(day_kurt(Close)), 15)` |
| -2.63 | -1.83 | -2.63 | +1 | 5 | prods2042M3_I0_open_search | `cross_mean(ts_std(pow_2(day_kurt(Ret)), 30), 3)` |
| -3.20 | -3.20 | -2.88 | +1 | 5 | prods2042M3_I0_open_search | `cross_sum(pow_2(day_kurt(Volume)), 15)` |

## 共性:332 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.70 | 0.000 | 15 | -0.57 / -2.27 | `cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares)` |
| +1.52 | 0.009 | 5 | -0.69 / -2.21 | `cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Amt), 60), 60)` |
| +1.35 | 0.009 | 7 | -0.87 / -2.22 | `cross_corr(day_kurt(Vwap), day_kurt(Amt), 60)` |
| +1.29 | 0.019 | 6 | -0.92 / -2.21 | `cross_ema(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4)))), 180)` |
| +1.29 | 0.000 | 157 | -1.51 / -2.80 | `day_sum(Ret)` |
| +1.25 | 0.000 | 89 | -1.28 / -2.52 | `sub(LogFloatCap, LogFloatShares)` |
| +1.23 | 0.012 | 8 | -0.99 / -2.22 | `cross_corr(day_kurt(Close), day_kurt(Volume), 120)` |
| +1.20 | 0.063 | 4 | -1.01 / -2.20 | `day_at_max_ratio(add(-5, Low))` |
| +1.13 | 0.021 | 8 | -1.09 / -2.22 | `day_wmean(Ret, Amt)` |
| +1.09 | 0.035 | 7 | -1.13 / -2.21 | `cs_bucket_zscore(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 20), sub(LogFloatCap, LogFloatShares))` |
| +1.07 | 0.000 | 51 | -1.28 / -2.35 | `day_pos_ratio(Ret)` |
| +0.94 | 0.082 | 6 | -1.27 / -2.21 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(day_pos_ratio(Ret), 0.5)), 241), sub(LogFloatCap, LogFloatShares))` |
| +0.75 | 0.071 | 12 | -1.47 / -2.22 | `day_std(Amt)` |
| +0.75 | 0.071 | 12 | -1.47 / -2.22 | `cross_mean(day_std(Amt), 30)` |
| +0.63 | 0.037 | 27 | -1.61 / -2.24 | `is_gt(ListAge, 120)` |
| +0.63 | 0.037 | 27 | -1.61 / -2.24 | `replace_small_with_nan(is_gt(ListAge, 120))` |
| +0.52 | 0.086 | 23 | -1.71 / -2.23 | `day_kurt(Close)` |
| +0.49 | 0.018 | 12 | -1.72 / -2.21 | `cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))))` |
| +0.45 | 0.330 | 5 | -1.75 / -2.20 | `day_kurt(Open)` |
| +0.41 | 0.009 | 149 | -1.96 / -2.37 | `day_kurt(Low)` |

## 拆解(26 次评估)

### head score +0.86:`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Vwap), add(day_kurt(Vwap), 4))), 241), sub(LogFloatCap, LogFloatShares))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| sufficiency | `day_kurt(Vwap)` | -3.90 | -3.24 | -3.90 | — | (子树本身) |
| sufficiency | `sub(LogFloatCap, LogFloatShares)` | -1.62 | -1.39 | -1.62 | — | (子树本身) |
| knockout | `mul(day_sum(Ret), add(day_kurt(Vwap), add(day_kurt(Vwap), 4)))` | -0.29 | -0.29 | +0.20 | +1.15 | `cs_bucket_zscore(cross_mean(day_sum(Ret), 241), sub(LogFloatCap, LogFloatShares))` |
| knockout | `add(day_kurt(Vwap), add(day_kurt(Vwap), 4))` | +0.30 | +0.30 | +1.08 | +0.56 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), day_kurt(Vwap)), 241), sub(LogFloatCap, LogFloatShares))` |
| knockout | `add(day_kurt(Vwap), 4)` | +0.30 | +0.30 | +1.08 | +0.56 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Vwap), day_kurt(Vwap))), 241), sub(LogFloatCap, LogFloatShares))` |
| knockout | `sub(LogFloatCap, LogFloatShares)` | -0.21 | -0.21 | +0.56 | +1.07 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Vwap), add(day_kurt(Vwap), 4))), 241), LogFloatCap)` |
| swap | `Vwap->Close` | +0.69 | +0.69 | +1.21 | — | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Close), add(day_kurt(Close), 4))), 241), sub(LogFloatCap, LogFloatShares))` |
| window | `cross_mean@241->120` | +0.25 | +0.25 | +0.45 | — | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Vwap), add(day_kurt(Vwap), 4))), 120), sub(LogFloatCap, LogFloatShares))` |
| window | `cross_mean@241->482` | +0.50 | +0.50 | +1.25 | — | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Vwap), add(day_kurt(Vwap), 4))), 482), sub(LogFloatCap, LogFloatShares))` |

### head score +0.64:`cs_bucket_zscore(ts_std(day_kurt(High), 240), LogFloatCap)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(day_kurt(High), 240)` | -0.59 | -0.59 | -0.27 | — | (子树本身) |
| sufficiency | `day_kurt(High)` | -3.88 | -3.44 | -3.88 | — | (子树本身) |
| knockout | `ts_std(day_kurt(High), 240)` | -3.05 | -2.99 | -3.05 | +3.69 | `cs_bucket_zscore(day_kurt(High), LogFloatCap)` |
| swap | `High->Low` | +0.64 | +0.64 | +0.75 | — | `cs_bucket_zscore(ts_std(day_kurt(Low), 240), LogFloatCap)` |
| window | `ts_std@240->120` | +0.15 | +0.15 | +0.26 | — | `cs_bucket_zscore(ts_std(day_kurt(High), 120), LogFloatCap)` |
| window | `ts_std@240->480` | -0.23 | -0.23 | +0.32 | — | `cs_bucket_zscore(ts_std(day_kurt(High), 480), LogFloatCap)` |

### head score -1.86:`cross_sum(day_kurt(Vwap), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(Vwap)` | -3.90 | -3.24 | -3.90 | — | (子树本身) |
| swap | `Vwap->Close` | -2.08 | -1.96 | -2.08 | — | `cross_sum(day_kurt(Close), 15)` |
| window | `cross_sum@15->7` | -2.03 | -1.78 | -2.03 | — | `cross_sum(day_kurt(Vwap), 7)` |
| window | `cross_sum@15->30` | -2.29 | -1.47 | -2.29 | — | `cross_sum(day_kurt(Vwap), 30)` |

### head score -2.03:`cross_sum(pow_2(day_kurt(Close)), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_kurt(Close))` | -2.91 | -2.87 | -2.91 | — | (子树本身) |
| sufficiency | `day_kurt(Close)` | -4.01 | -3.73 | -4.01 | — | (子树本身) |
| knockout | `pow_2(day_kurt(Close))` | -2.08 | -1.96 | -2.08 | +0.04 | `cross_sum(day_kurt(Close), 15)` |
| swap | `Close->Vwap` | -1.82 | -1.44 | -1.82 | — | `cross_sum(pow_2(day_kurt(Vwap)), 15)` |
| window | `cross_sum@15->7` | -2.16 | -2.03 | -2.16 | — | `cross_sum(pow_2(day_kurt(Close)), 7)` |
| window | `cross_sum@15->30` | -1.84 | -1.58 | -1.84 | — | `cross_sum(pow_2(day_kurt(Close)), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares)` — enrichment,均值差 +1.70,p 0.000
2. `cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Amt), 60), 60)` — enrichment,均值差 +1.52,p 0.009
3. `cross_corr(day_kurt(Vwap), day_kurt(Amt), 60)` — enrichment,均值差 +1.35,p 0.009
4. `cross_ema(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4)))), 180)` — enrichment,均值差 +1.29,p 0.019
5. `day_sum(Ret)` — enrichment,均值差 +1.29,p 0.000
6. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +1.25,p 0.000
7. `cross_corr(day_kurt(Close), day_kurt(Volume), 120)` — enrichment,均值差 +1.23,p 0.012
8. `day_at_max_ratio(add(-5, Low))` — enrichment,均值差 +1.20,p 0.063
9. `day_wmean(Ret, Amt)` — enrichment,均值差 +1.13,p 0.021
10. `cs_bucket_zscore(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 20), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +1.09,p 0.035
11. `day_pos_ratio(Ret)` — enrichment,均值差 +1.07,p 0.000
12. `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(day_pos_ratio(Ret), 0.5)), 241), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +0.94,p 0.082
13. `day_std(Amt)` — enrichment,均值差 +0.75,p 0.071
14. `cross_mean(day_std(Amt), 30)` — enrichment,均值差 +0.75,p 0.071
15. `is_gt(ListAge, 120)` — enrichment,均值差 +0.63,p 0.037
16. `replace_small_with_nan(is_gt(ListAge, 120))` — enrichment,均值差 +0.63,p 0.037
17. `day_kurt(Close)` — enrichment,均值差 +0.52,p 0.086
18. `cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))))` — enrichment,均值差 +0.49,p 0.018
19. `day_kurt(Low)` — enrichment,均值差 +0.41,p 0.009

## 本组之前各轮的任务

- `prods2042Pr1a_Ea`:核心 `day_kurt(Low)`;评分 97,过线 1,入 heads 1;采样计数 {'c05_no_core': 856, 'c05_skeleton': 382}
  - score +0.66(train +0.66 valid +1.00):`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 241), sub(LogFloatCap, LogFloatShares))`
  - score -0.05(train -0.05 valid +0.50):`cs_bucket_zscore(cross_mean(div(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 241), sub(LogFloatCap, LogFloatShares))`
  - score -0.09(train +0.22 valid -0.09):`cross_mean(div(day_wmean(Ret, Amt), cross_mean(div(day_wmean(Ret, Amt), add(day_kurt(Low), 4)), 241)), 241)`
  - score -0.20(train -0.20 valid +0.71):`cs_bucket_zscore(cross_mean(div(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 241), day_kurt(Low))`
  - score -0.24(train -0.01 valid -0.24):`cross_mean(div(day_wmean(Ret, Amt), add(day_kurt(Low), 4)), 241)`
- `prods2042Pr1b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.40(train +0.06 valid -0.40):`cross_corr(day_kurt(Close), day_kurt(Volume), 120)`
  - score -0.43(train -0.24 valid -0.43):`mul(cross_corr(day_kurt(Close), day_kurt(Volume), 120), replace_small_with_nan(is_gt(ListAge, 120)))`
  - score -0.43(train -0.25 valid -0.43):`add(cross_corr(day_kurt(Close), day_kurt(Volume), 120), replace_small_with_nan(is_gt(ListAge, 120)))`
  - score -0.43(train -0.28 valid -0.43):`replace_small_with_nan(mul(cross_corr(day_kurt(Close), day_kurt(Volume), 120), replace_small_with_nan(is_gt(ListAge, 120))))`
  - score -0.46(train -0.46 valid -0.44):`mul(cs_bucket_demean(cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Amt), 60), 60), day_kurt(Close)), day_at_max_ratio(add(-5, Low)))`
- `prods2042Pr2a_Ea`:核心 `mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4)))`;评分 94,过线 0,入 heads 0;采样计数 {'c05_no_core': 1185, 'c05_skeleton': 575, 'mutation_refused': 4, 'c05_periphery_seen': 3}
  - score +0.05(train +0.05 valid +0.91):`cs_bucket_zscore(cross_ema(cs_winsor(mul(cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares), add(day_kurt(Low), add(day_sum(Ret), 4)))), 15), sub(LogFloatCap, LogFloatShares))`
  - score +0.05(train +0.05 valid +1.05):`cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), add(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares), 4)))), 4))))), 4))), 150), LogFloatShares)`
  - score +0.05(train +0.05 valid +0.89):`cs_bucket_zscore(cross_ema(cs_winsor(mul(cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares), add(day_kurt(Low), add(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares), 4)))), 4)))), 15), sub(LogFloatCap, LogFloatShares))`
  - score +0.04(train +0.04 valid +1.03):`cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4)))), 4))), 150), LogFloatShares)`
  - score +0.03(train +0.03 valid +1.06):`cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(cs_winsor(mul(day_sum(Ret), add(day_kurt(Low), add(cs_bucket_demean(cross_ema(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 150), LogFloatShares), 4)))), 4))), 150), LogFloatShares)`
- `prods2042Pr2b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.17(train +0.17 valid +0.22):`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(day_pos_ratio(Ret), 0.5)), 241), sub(LogFloatCap, LogFloatShares))`
  - score +0.04(train +0.04 valid +0.11):`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(day_pos_ratio(Ret), 0.5)), 241), day_pos_ratio(Ret))`
  - score +0.03(train +0.03 valid +0.31):`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(day_pos_ratio(Ret), -5)), 10), sub(LogFloatCap, LogFloatShares)), -5)), 241), sub(LogFloatCap, LogFloatShares))`
  - score -0.02(train -0.02 valid +0.57):`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(cs_bucket_zscore(sub(day_pos_ratio(Ret), 0.5), sub(LogFloatCap, LogFloatShares)), 0.5)), 241), sub(LogFloatCap, LogFloatShares))`
  - score -0.21(train -0.21 valid +0.20):`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(cs_bucket_zscore(cross_mean(mul(day_sum(Ret), sub(day_pos_ratio(Ret), -1)), 241), sub(LogFloatCap, LogFloatShares)), -1)), 241), sub(LogFloatCap, LogFloatShares))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.22(swap Close->Vwap):`cross_sum(pow_2(day_kurt(Vwap)), 15)`
- 增益 +0.19(window cross_sum@15->30):`cross_sum(pow_2(day_kurt(Close)), 30)`
