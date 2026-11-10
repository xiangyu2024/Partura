# 定位:种子 2033,P 组,第 3 轮(只含 train / valid)

快照:prods2033M1_I0_open_search, prods2033M2_I0_open_search, prods2033M3_I0_open_search, prods2033Pr1a_Ea, prods2033Pr1b_Nb, prods2033Pr2a_Ea, prods2033Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.54 | +0.70 | +0.54 | +1 | 5 | prods2033Pr2a_Ea | `div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), cross_delay(day_close(Close), 1))` |
| +0.15 | +0.33 | +0.15 | +1 | 5 | prods2033M2_I0_open_search | `ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)), 20)` |
| -0.07 | -0.07 | +0.09 | +1 | 5 | prods2033M2_I0_open_search | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)` |
| -1.22 | -1.21 | -1.22 | -1 | 5 | prods2033M1_I0_open_search | `div(1, add(ts_stddev(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), 20), 0.0001))` |
| -1.31 | -0.90 | -1.31 | +1 | 5 | prods2033M2_I0_open_search | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 60)` |
| -1.93 | -1.93 | -0.20 | -1 | 5 | prods2033M3_I0_open_search | `cross_quantile_q25(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 241)` |
| -2.50 | -2.50 | -1.75 | +1 | 5 | prods2033M1_I0_open_search | `ts_stddev(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), 10)` |
| -2.55 | -2.55 | -0.50 | +1 | 20 | prods2033M3_I0_open_search | `neg(cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10), 241))` |
| -2.63 | -1.95 | -2.63 | +1 | 20 | prods2033M3_I0_open_search | `ts_std(inv(day_last(Amt)), 50)` |
| -3.96 | -3.96 | -1.97 | +1 | 20 | prods2033M1_I0_open_search | `ts_stddev(sub(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), ts_delay(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), 1)), 10)` |

## 共性:238 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.94 | 0.000 | 138 | -1.29 / -3.23 | `day_close(Close)` |
| +1.74 | 0.001 | 7 | -0.42 / -2.16 | `div(day_close(Close), cross_delay(div(day_last(Amt), day_sum(Amt)), 1))` |
| +1.70 | 0.000 | 64 | -0.86 / -2.57 | `cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1)` |
| +1.65 | 0.000 | 52 | -0.82 / -2.47 | `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` |
| +1.61 | 0.000 | 115 | -1.28 / -2.88 | `div(day_close(Close), cross_delay(day_close(Close), 1))` |
| +1.59 | 0.003 | 6 | -0.55 / -2.15 | `mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap))` |
| +1.57 | 0.000 | 12 | -0.61 / -2.19 | `day_at_min_ratio(Vwap)` |
| +1.57 | 0.000 | 118 | -1.32 / -2.88 | `cross_delay(day_close(Close), 1)` |
| +1.55 | 0.000 | 75 | -1.05 / -2.60 | `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` |
| +1.48 | 0.000 | 12 | -0.71 / -2.18 | `cross_delay(div(day_last(Amt), day_sum(Amt)), 1)` |
| +1.15 | 0.006 | 11 | -1.02 / -2.16 | `div(day_last(Open), day_sum(Amt))` |
| +1.06 | 0.004 | 15 | -1.12 / -2.18 | `day_last(Open)` |
| +0.95 | 0.000 | 34 | -1.30 / -2.24 | `div(day_last(Amt), day_sum(Amt))` |
| +0.80 | 0.001 | 44 | -1.45 / -2.26 | `day_sum(Amt)` |
| +0.79 | 0.121 | 6 | -1.34 / -2.13 | `cross_delay(cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 1)` |
| +0.71 | 0.164 | 5 | -1.41 / -2.12 | `ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)` |
| +0.70 | 0.211 | 4 | -1.42 / -2.12 | `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), day_close(Close)), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` |
| +0.66 | 0.076 | 15 | -1.49 / -2.15 | `cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1))` |
| +0.61 | 0.066 | 19 | -1.55 / -2.16 | `replace_small_with_nan(is_gt(ListAge, 250))` |
| +0.61 | 0.066 | 19 | -1.55 / -2.16 | `is_gt(ListAge, 250)` |

## 拆解(37 次评估)

### head score +0.54:`div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), cross_delay(day_close(Close), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` | -0.20 | +0.08 | -0.20 | — | (子树本身) |
| sufficiency | `cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1)` | -6.46 | -6.46 | -6.04 | — | (子树本身) |
| sufficiency | `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` | -4.54 | -4.54 | -4.26 | — | (子树本身) |
| knockout | `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` | -5.00 | -4.78 | -5.00 | +5.54 | `div(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(day_close(Close), 1))` |
| knockout | `cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1)` | -2.38 | -1.62 | -2.38 | +2.92 | `div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 241), cross_delay(day_close(Close), 1))` |
| knockout | `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` | -1.71 | -1.57 | -1.71 | +2.25 | `div(cross_corr(LogFloatCap, cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), cross_delay(day_close(Close), 1))` |
| knockout | `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` | -1.18 | -1.18 | -1.05 | +1.72 | `div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(LogFloatCap, 1), 241), cross_delay(day_close(Close), 1))` |
| swap | `Close->Vwap` | +0.45 | +0.64 | +0.45 | — | `div(cross_corr(cs_bucket_demean(sub(div(day_close(Vwap), cross_delay(day_close(Vwap), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Vwap), cross_delay(day_close(Vwap), 1)), 1), LogFloatCap), 1), 241), cross_delay(day_close(Vwap), 1))` |
| window | `cross_corr@241->120` | +0.43 | +0.89 | +0.43 | — | `div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 120), cross_delay(day_close(Close), 1))` |
| window | `cross_corr@241->482` | +0.35 | +0.60 | +0.35 | — | `div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 482), cross_delay(day_close(Close), 1))` |

### head score -1.31:`cross_regbeta(day_quantile_q25(Low), day_last(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(Low)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| swap | `Low->High` | -1.27 | -0.89 | -1.27 | — | `cross_regbeta(day_quantile_q25(High), day_last(Amt), 60)` |
| swap | `Amt->Volume` | -2.16 | -1.49 | -2.16 | — | `cross_regbeta(day_quantile_q25(Low), day_last(Volume), 60)` |
| window | `cross_regbeta@60->30` | -1.43 | -0.94 | -1.43 | — | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 30)` |
| window | `cross_regbeta@60->120` | -1.34 | -1.26 | -1.34 | — | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 120)` |

### head score -1.93:`cross_quantile_q25(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10))` | -3.94 | -2.92 | -3.94 | — | (子树本身) |
| sufficiency | `ts_quantile_q50(inv(day_last(Amt)), 10)` | -3.94 | -2.92 | -3.94 | — | (子树本身) |
| sufficiency | `inv(day_last(Amt))` | -3.85 | -3.33 | -3.85 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| knockout | `cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10))` | -2.04 | -2.04 | -0.19 | +0.11 | `cross_quantile_q25(ts_quantile_q50(inv(day_last(Amt)), 10), 241)` |
| knockout | `ts_quantile_q50(inv(day_last(Amt)), 10)` | -2.32 | -2.32 | -0.43 | +0.39 | `cross_quantile_q25(cs_demean(inv(day_last(Amt))), 241)` |
| knockout | `inv(day_last(Amt))` | -2.80 | -2.21 | -2.80 | +0.87 | `cross_quantile_q25(cs_demean(ts_quantile_q50(day_last(Amt), 10)), 241)` |
| swap | `Amt->Volume` | -2.02 | -1.81 | -2.02 | — | `cross_quantile_q25(cs_demean(ts_quantile_q50(inv(day_last(Volume)), 10)), 241)` |
| window | `cross_quantile_q25@241->120` | -2.09 | -2.09 | -0.72 | — | `cross_quantile_q25(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 120)` |
| window | `cross_quantile_q25@241->482` | -1.93 | -1.93 | -0.44 | — | `cross_quantile_q25(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 482)` |

### head score -2.55:`neg(cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10), 241)` | -2.55 | -2.55 | -0.50 | — | (子树本身) |
| sufficiency | `ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10)` | -3.69 | -2.92 | -3.69 | — | (子树本身) |
| sufficiency | `cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10))` | -3.94 | -2.92 | -3.94 | — | (子树本身) |
| sufficiency | `ts_quantile_q50(inv(day_last(Amt)), 10)` | -3.94 | -2.92 | -3.94 | — | (子树本身) |
| knockout | `cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10), 241)` | -3.69 | -2.92 | -3.69 | +1.14 | `neg(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10))` |
| knockout | `ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10)` | -2.56 | -2.56 | -0.52 | +0.01 | `neg(cross_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 241))` |
| knockout | `cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10))` | -2.67 | -2.31 | -2.67 | +0.12 | `neg(cross_sum(ts_sum(ts_quantile_q50(inv(day_last(Amt)), 10), 10), 241))` |
| knockout | `ts_quantile_q50(inv(day_last(Amt)), 10)` | — | — | — | — | `neg(cross_sum(ts_sum(cs_demean(inv(day_last(Amt))), 10), 241))` |
| swap | `Amt->Volume` | -2.15 | -1.92 | -2.15 | — | `neg(cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Volume)), 10)), 10), 241))` |
| window | `cross_sum@241->120` | -2.71 | -2.35 | -2.71 | — | `neg(cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10), 120))` |
| window | `cross_sum@241->482` | -1.98 | -1.98 | -0.23 | — | `neg(cross_sum(ts_sum(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_close(Close)` — enrichment,均值差 +1.94,p 0.000
2. `div(day_close(Close), cross_delay(div(day_last(Amt), day_sum(Amt)), 1))` — enrichment,均值差 +1.74,p 0.001
3. `cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1)` — enrichment,均值差 +1.70,p 0.000
4. `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` — enrichment,均值差 +1.65,p 0.000
5. `div(day_close(Close), cross_delay(day_close(Close), 1))` — enrichment,均值差 +1.61,p 0.000
6. `mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap))` — enrichment,均值差 +1.59,p 0.003
7. `day_at_min_ratio(Vwap)` — enrichment,均值差 +1.57,p 0.000
8. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +1.57,p 0.000
9. `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` — enrichment,均值差 +1.55,p 0.000
10. `cross_delay(div(day_last(Amt), day_sum(Amt)), 1)` — enrichment,均值差 +1.48,p 0.000
11. `div(day_last(Open), day_sum(Amt))` — enrichment,均值差 +1.15,p 0.006
12. `day_last(Open)` — enrichment,均值差 +1.06,p 0.004
13. `div(day_last(Amt), day_sum(Amt))` — enrichment,均值差 +0.95,p 0.000
14. `day_sum(Amt)` — enrichment,均值差 +0.80,p 0.001
15. `cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1))` — enrichment,均值差 +0.66,p 0.076
16. `replace_small_with_nan(is_gt(ListAge, 250))` — enrichment,均值差 +0.61,p 0.066
17. `is_gt(ListAge, 250)` — enrichment,均值差 +0.61,p 0.066
18. `day_last(Amt)` — enrichment,均值差 +0.53,p 0.031

## 本组之前各轮的任务

- `prods2033Pr1a_Ea`:核心 `div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1))`;评分 83,过线 0,入 heads 0;采样计数 {'c05_no_core': 1688, 'c05_skeleton': 827, 'c05_periphery_seen': 5, 'mutation_refused': 7}
  - score -1.45(train -1.45 valid -1.27):`cross_med(cross_med(div(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), 10), 60)`
  - score -1.55(train -1.04 valid -1.55):`cross_med(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 30)), 1), 0)), 120)`
  - score -1.93(train -1.74 valid -1.93):`cross_med(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), day_argmax(High)), 0)), 120)`
  - score -2.30(train -2.09 valid -2.30):`cross_med(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), cross_max(div(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), ts_delay(sub(day_last(Close), 1), 1)), 30)), 1)), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), cross_max(div(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), ts_delay(sub(day_last(Close), 1), 1)), 30)), 1))), 120)`
  - score -2.32(train -1.77 valid -2.32):`inv(cross_max(cross_max(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), 15), 15))`
- `prods2033Pr1b_Nb`:核心 `—`;评分 77,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.29(train +0.29 valid +0.65):`mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), replace_small_with_nan(is_gt(ListAge, 250)))`
  - score +0.04(train +0.04 valid +0.29):`mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), replace_small_with_nan(LogFloatCap))`
  - score -0.01(train +0.25 valid -0.01):`mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), day_close(Close)), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), replace_small_with_nan(is_gt(ListAge, 250)))`
  - score -0.04(train -0.04 valid +0.66):`mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), div(day_close(Close), cross_delay(day_close(Close), 1))), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 2), LogFloatCap), 1), 241), replace_small_with_nan(is_gt(ListAge, 250)))`
  - score -0.14(train +0.17 valid -0.14):`cross_regbeta(cross_delay(cs_demean(sub(cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 1)), 1), cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 241)`
- `prods2033Pr2a_Ea`:核心 `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)`;评分 75,过线 1,入 heads 1;采样计数 {'c05_periphery_seen': 11, 'c05_no_core': 1832, 'c05_skeleton': 836, 'mutation_refused': 12}
  - score +0.54(train +0.70 valid +0.54):`div(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), cross_delay(day_close(Close), 1))`
  - score +0.22(train +0.22 valid +0.99):`mul(mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap)), day_at_min_ratio(Vwap))`
  - score +0.20(train +0.20 valid +0.79):`mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap))), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap))`
  - score +0.13(train +0.13 valid +0.85):`mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap))`
  - score +0.05(train +0.07 valid +0.05):`cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), mul(cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241), day_at_min_ratio(Vwap))), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)`
- `prods2033Pr2b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.27(train +0.27 valid +0.69):`cross_regbeta(sub(div(day_close(Amt), cross_delay(div(day_last(Amt), day_sum(Amt)), 1)), 1), div(day_last(Open), day_sum(High)), 60)`
  - score +0.10(train +0.49 valid +0.10):`cross_regbeta(sub(div(day_close(Close), cross_delay(div(day_last(Amt), day_sum(Amt)), 1)), 1), div(day_last(Open), day_sum(Amt)), 60)`
  - score +0.10(train +0.49 valid +0.10):`cross_regbeta(sub(div(day_close(Close), cross_delay(div(day_last(Amt), day_sum(Amt)), 1)), 5), div(day_last(Open), day_sum(Amt)), 60)`
  - score +0.10(train +0.49 valid +0.10):`cross_regbeta(sub(div(day_close(Close), cross_delay(div(day_last(Amt), day_sum(Amt)), 1)), -5), div(day_last(Open), day_sum(Amt)), 60)`
  - score +0.09(train +0.48 valid +0.09):`cross_regbeta(sub(div(day_close(Close), cross_delay(div(day_last(Amt), day_sum(Amt)), 1)), 1), div(day_close(Close), day_sum(Amt)), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
