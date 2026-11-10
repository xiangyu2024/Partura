# 定位:种子 2042,P 组,第 2 轮(只含 train / valid)

快照:prods2042M1_I0_open_search, prods2042M2_I0_open_search, prods2042Pr1a_Ea, prods2042Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.66 | +0.66 | +1.00 | +1 | 5 | prods2042Pr1a_Ea | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 241), sub(LogFloatCap, LogFloatShares))` |
| +0.23 | +0.23 | +0.53 | +1 | 5 | prods2042M1_I0_open_search | `cs_bucket_zscore(ts_std(day_kurt(Low), 120), LogFloatCap)` |
| -0.92 | -0.92 | -0.58 | +1 | 0 | prods2042M2_I0_open_search | `cross_sum(day_kurt(Vwap), 241)` |
| -1.12 | -1.09 | -1.12 | +1 | 0 | prods2042M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)` |
| -1.63 | -1.63 | -0.71 | -1 | 0 | prods2042M1_I0_open_search | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 241))` |
| -1.78 | -1.78 | -1.15 | -1 | 0 | prods2042M2_I0_open_search | `neg(cross_sum(day_kurt(Low), 241))` |
| -1.86 | -1.69 | -1.86 | +1 | 20 | prods2042M2_I0_open_search | `cross_sum(day_kurt(Vwap), 15)` |

## 共性:183 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.81 | 0.002 | 5 | -0.69 / -2.50 | `cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Amt), 60), 60)` |
| +1.64 | 0.001 | 7 | -0.87 / -2.52 | `cross_corr(day_kurt(Vwap), day_kurt(Amt), 60)` |
| +1.53 | 0.001 | 8 | -0.99 / -2.52 | `cross_corr(day_kurt(Close), day_kurt(Volume), 120)` |
| +1.48 | 0.015 | 4 | -1.01 / -2.49 | `day_at_max_ratio(add(-5, Low))` |
| +1.42 | 0.002 | 8 | -1.09 / -2.52 | `day_wmean(Ret, Amt)` |
| +1.30 | 0.000 | 35 | -1.40 / -2.70 | `day_sum(Ret)` |
| +1.05 | 0.005 | 12 | -1.47 / -2.52 | `cross_mean(day_std(Amt), 30)` |
| +1.05 | 0.005 | 12 | -1.47 / -2.52 | `day_std(Amt)` |
| +0.99 | 0.000 | 27 | -1.61 / -2.60 | `replace_small_with_nan(is_gt(ListAge, 120))` |
| +0.99 | 0.000 | 27 | -1.61 / -2.60 | `is_gt(ListAge, 120)` |
| +0.86 | 0.004 | 22 | -1.69 / -2.56 | `day_kurt(Close)` |
| +0.80 | 0.013 | 21 | -1.75 / -2.54 | `sub(LogFloatCap, LogFloatShares)` |
| +0.73 | 0.127 | 5 | -1.75 / -2.47 | `day_kurt(Open)` |
| +0.59 | 0.006 | 82 | -2.13 / -2.72 | `day_kurt(Low)` |
| +0.37 | 0.018 | 17 | -2.11 / -2.49 | `day_kurt(Amt)` |
| +0.27 | 0.312 | 14 | -2.21 / -2.47 | `day_kurt(High)` |
| +0.24 | 0.266 | 31 | -2.25 / -2.49 | `day_kurt(Vwap)` |
| +0.24 | 0.400 | 4 | -2.22 / -2.46 | `cs_rank(day_kurt(Low))` |
| +0.23 | 0.181 | 32 | -2.26 / -2.49 | `day_kurt(Volume)` |
| -0.06 | 0.600 | 4 | -2.51 / -2.45 | `cs_rank(day_kurt(Volume))` |

## 拆解(26 次评估)

### head score +0.66:`cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 241), sub(LogFloatCap, LogFloatShares))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| sufficiency | `day_kurt(Low)` | -4.53 | -3.85 | -4.53 | — | (子树本身) |
| sufficiency | `sub(LogFloatCap, LogFloatShares)` | -1.62 | -1.39 | -1.62 | — | (子树本身) |
| knockout | `mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4)))` | -0.29 | -0.29 | +0.20 | +0.95 | `cs_bucket_zscore(cross_mean(day_sum(Ret), 241), sub(LogFloatCap, LogFloatShares))` |
| knockout | `add(day_kurt(Low), add(day_kurt(Low), 4))` | +0.28 | +0.28 | +0.85 | +0.38 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), day_kurt(Low)), 241), sub(LogFloatCap, LogFloatShares))` |
| knockout | `add(day_kurt(Low), 4)` | +0.28 | +0.28 | +0.85 | +0.38 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), day_kurt(Low))), 241), sub(LogFloatCap, LogFloatShares))` |
| knockout | `sub(LogFloatCap, LogFloatShares)` | -0.57 | -0.57 | +0.30 | +1.23 | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 241), LogFloatCap)` |
| swap | `Low->High` | +0.68 | +0.68 | +1.37 | — | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(High), add(day_kurt(High), 4))), 241), sub(LogFloatCap, LogFloatShares))` |
| window | `cross_mean@241->120` | +0.29 | +0.29 | +0.63 | — | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 120), sub(LogFloatCap, LogFloatShares))` |
| window | `cross_mean@241->482` | +0.32 | +0.32 | +0.99 | — | `cs_bucket_zscore(cross_mean(mul(day_sum(Ret), add(day_kurt(Low), add(day_kurt(Low), 4))), 482), sub(LogFloatCap, LogFloatShares))` |

### head score +0.23:`cs_bucket_zscore(ts_std(day_kurt(Low), 120), LogFloatCap)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(day_kurt(Low), 120)` | -0.97 | -0.97 | -0.68 | — | (子树本身) |
| sufficiency | `day_kurt(Low)` | -4.53 | -3.85 | -4.53 | — | (子树本身) |
| knockout | `ts_std(day_kurt(Low), 120)` | -3.51 | -3.51 | -3.20 | +3.74 | `cs_bucket_zscore(day_kurt(Low), LogFloatCap)` |
| swap | `Low->High` | +0.15 | +0.15 | +0.26 | — | `cs_bucket_zscore(ts_std(day_kurt(High), 120), LogFloatCap)` |
| window | `ts_std@120->60` | -0.42 | -0.41 | -0.42 | — | `cs_bucket_zscore(ts_std(day_kurt(Low), 60), LogFloatCap)` |
| window | `ts_std@120->240` | +0.64 | +0.64 | +0.75 | — | `cs_bucket_zscore(ts_std(day_kurt(Low), 240), LogFloatCap)` |

### head score -0.92:`cross_sum(day_kurt(Vwap), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(Vwap)` | -3.90 | -3.24 | -3.90 | — | (子树本身) |
| swap | `Vwap->Close` | -1.32 | -1.32 | -0.91 | — | `cross_sum(day_kurt(Close), 241)` |
| window | `cross_sum@241->120` | -1.30 | -1.22 | -1.30 | — | `cross_sum(day_kurt(Vwap), 120)` |
| window | `cross_sum@241->482` | -1.14 | -1.14 | -0.65 | — | `cross_sum(day_kurt(Vwap), 482)` |

### head score -1.78:`neg(cross_sum(day_kurt(Low), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(day_kurt(Low), 241)` | -1.78 | -1.78 | -1.12 | — | (子树本身) |
| sufficiency | `day_kurt(Low)` | -4.53 | -3.85 | -4.53 | — | (子树本身) |
| knockout | `cross_sum(day_kurt(Low), 241)` | -4.53 | -3.85 | -4.53 | +2.75 | `neg(day_kurt(Low))` |
| swap | `Low->High` | -1.50 | -1.50 | -0.90 | — | `neg(cross_sum(day_kurt(High), 241))` |
| window | `cross_sum@241->120` | -1.96 | -1.96 | -1.45 | — | `neg(cross_sum(day_kurt(Low), 120))` |
| window | `cross_sum@241->482` | -1.77 | -1.77 | -1.14 | — | `neg(cross_sum(day_kurt(Low), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Amt), 60), 60)` — enrichment,均值差 +1.81,p 0.002
2. `cross_corr(day_kurt(Vwap), day_kurt(Amt), 60)` — enrichment,均值差 +1.64,p 0.001
3. `cross_corr(day_kurt(Close), day_kurt(Volume), 120)` — enrichment,均值差 +1.53,p 0.001
4. `day_at_max_ratio(add(-5, Low))` — enrichment,均值差 +1.48,p 0.015
5. `day_wmean(Ret, Amt)` — enrichment,均值差 +1.42,p 0.002
6. `day_sum(Ret)` — enrichment,均值差 +1.30,p 0.000
7. `cross_mean(day_std(Amt), 30)` — enrichment,均值差 +1.05,p 0.005
8. `day_std(Amt)` — enrichment,均值差 +1.05,p 0.005
9. `replace_small_with_nan(is_gt(ListAge, 120))` — enrichment,均值差 +0.99,p 0.000
10. `is_gt(ListAge, 120)` — enrichment,均值差 +0.99,p 0.000
11. `day_kurt(Close)` — enrichment,均值差 +0.86,p 0.004
12. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.80,p 0.013
13. `day_kurt(Low)` — enrichment,均值差 +0.59,p 0.006
14. `day_kurt(Amt)` — enrichment,均值差 +0.37,p 0.018

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.41(window ts_std@120->240):`cs_bucket_zscore(ts_std(day_kurt(Low), 240), LogFloatCap)`
- 增益 +0.28(swap Low->High):`neg(cross_sum(day_kurt(High), 241))`
