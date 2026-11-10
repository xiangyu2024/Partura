# 定位:种子 2033,P 组,第 2 轮(只含 train / valid)

快照:prods2033M1_I0_open_search, prods2033M2_I0_open_search, prods2033Pr1a_Ea, prods2033Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.15 | +0.33 | +0.15 | +1 | 5 | prods2033M2_I0_open_search | `ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)), 20)` |
| -0.07 | -0.07 | +0.09 | +1 | 5 | prods2033M2_I0_open_search | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)` |
| -1.22 | -1.21 | -1.22 | -1 | 5 | prods2033M1_I0_open_search | `div(1, add(ts_stddev(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), 20), 0.0001))` |
| -1.58 | -1.58 | -1.47 | +1 | 20 | prods2033M2_I0_open_search | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)` |
| -2.50 | -2.50 | -1.75 | +1 | 5 | prods2033M1_I0_open_search | `ts_stddev(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), 10)` |
| -3.96 | -3.96 | -1.97 | +1 | 20 | prods2033M1_I0_open_search | `ts_stddev(sub(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), ts_delay(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0)), 1)), 10)` |

## 共性:125 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.83 | 0.000 | 17 | -1.13 / -2.95 | `cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1)` |
| +1.71 | 0.000 | 50 | -1.68 / -3.39 | `div(day_close(Close), cross_delay(day_close(Close), 1))` |
| +1.70 | 0.000 | 51 | -1.70 / -3.40 | `cross_delay(day_close(Close), 1)` |
| +1.70 | 0.000 | 51 | -1.70 / -3.40 | `day_close(Close)` |
| +1.54 | 0.000 | 28 | -1.51 / -3.05 | `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` |
| +1.52 | 0.000 | 18 | -1.40 / -2.92 | `replace_small_with_nan(is_gt(ListAge, 250))` |
| +1.52 | 0.000 | 18 | -1.40 / -2.92 | `is_gt(ListAge, 250)` |
| +1.51 | 0.009 | 5 | -1.25 / -2.77 | `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` |
| +1.44 | 0.022 | 6 | -1.34 / -2.77 | `cross_delay(cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 1)` |
| +1.38 | 0.002 | 15 | -1.49 / -2.87 | `cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1))` |
| +1.35 | 0.035 | 5 | -1.41 / -2.76 | `ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)` |
| +1.33 | 0.068 | 4 | -1.42 / -2.75 | `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), day_close(Close)), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` |
| +1.15 | 0.065 | 5 | -1.61 / -2.75 | `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), day_close(Close))` |
| +0.92 | 0.037 | 11 | -1.87 / -2.79 | `day_last(Amt)` |
| +0.88 | 0.059 | 10 | -1.90 / -2.78 | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)` |
| +0.88 | 0.036 | 12 | -1.91 / -2.79 | `day_quantile_q25(Low)` |
| +0.86 | 0.120 | 8 | -1.90 / -2.76 | `log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10))` |
| +0.36 | 0.334 | 4 | -2.35 / -2.72 | `cross_delay(cs_rank(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 1)` |
| +0.33 | 0.324 | 6 | -2.39 / -2.72 | `cs_rank(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1))` |
| -0.66 | 0.935 | 7 | -3.33 / -2.67 | `cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 1)), create_valid_mask(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0))` |

## 拆解(30 次评估)

### head score +0.15:`ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20))` | -0.07 | -0.07 | +0.13 | — | (子树本身) |
| sufficiency | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)` | -0.07 | -0.07 | +0.13 | — | (子树本身) |
| sufficiency | `log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)` | — | — | — | — | 门槛废品 |
| knockout | `log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20))` | +0.20 | +0.33 | +0.20 | -0.05 | `ts_max(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20), 20)` |
| knockout | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)` | -0.07 | -0.07 | +0.13 | +0.22 | `ts_max(log(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10))), 20)` |
| knockout | `log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10))` | +0.24 | +0.65 | +0.24 | -0.09 | `ts_max(log(ts_max(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10), 20)), 20)` |
| knockout | `cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)` | -2.23 | -1.20 | -2.23 | +2.38 | `ts_max(log(ts_max(log(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)), 20)), 20)` |
| swap | `Low->High` | +0.13 | +0.13 | +0.23 | — | `ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(High), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)), 20)` |
| swap | `Amt->Volume` | -1.90 | -1.01 | -1.90 | — | `ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Volume), 10)), 20), day_last(Volume), 10)), 20)), 20)` |
| window | `ts_max@20->10` | +0.06 | +0.49 | +0.06 | — | `ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)), 10)` |
| window | `ts_max@20->40` | +0.26 | +0.26 | +0.51 | — | `ts_max(log(ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)), 40)` |

### head score -0.07:`ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)` | -2.13 | -1.15 | -2.13 | — | (子树本身) |
| sufficiency | `log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10))` | -1.64 | -1.30 | -1.64 | — | (子树本身) |
| knockout | `log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10))` | -0.23 | -0.23 | +0.35 | +0.16 | `ts_max(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10), 20)` |
| knockout | `cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)` | -2.09 | -1.04 | -2.09 | +2.02 | `ts_max(log(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)), 20)` |
| knockout | `ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)` | -0.93 | -0.93 | +0.32 | +0.87 | `ts_max(log(cross_regbeta(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), day_last(Amt), 10)), 20)` |
| knockout | `log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10))` | -1.13 | -1.13 | -0.88 | +1.06 | `ts_max(log(cross_regbeta(ts_max(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10), 20), day_last(Amt), 10)), 20)` |
| swap | `Low->High` | -0.14 | -0.14 | +0.13 | — | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(High), day_last(Amt), 10)), 20), day_last(Amt), 10)), 20)` |
| swap | `Amt->Volume` | -1.76 | -1.03 | -1.76 | — | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Volume), 10)), 20), day_last(Volume), 10)), 20)` |
| window | `ts_max@20->10` | -1.72 | -1.72 | -1.15 | — | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 10)` |
| window | `ts_max@20->40` | +0.08 | +0.29 | +0.08 | — | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20), day_last(Amt), 10)), 40)` |

### head score -1.58:`cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(Low)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| swap | `Low->High` | -1.57 | -1.57 | -1.41 | — | `cross_regbeta(day_quantile_q25(High), day_last(Amt), 10)` |
| swap | `Amt->Volume` | -2.42 | -2.10 | -2.42 | — | `cross_regbeta(day_quantile_q25(Low), day_last(Volume), 10)` |
| window | `cross_regbeta@10->5` | -2.01 | -2.01 | -1.44 | — | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 5)` |
| window | `cross_regbeta@10->20` | -1.44 | -1.21 | -1.44 | — | `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 20)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1)` — enrichment,均值差 +1.83,p 0.000
2. `div(day_close(Close), cross_delay(day_close(Close), 1))` — enrichment,均值差 +1.71,p 0.000
3. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +1.70,p 0.000
4. `day_close(Close)` — enrichment,均值差 +1.70,p 0.000
5. `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap)` — enrichment,均值差 +1.54,p 0.000
6. `replace_small_with_nan(is_gt(ListAge, 250))` — enrichment,均值差 +1.52,p 0.000
7. `is_gt(ListAge, 250)` — enrichment,均值差 +1.52,p 0.000
8. `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` — enrichment,均值差 +1.51,p 0.009
9. `cross_delay(cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 1)` — enrichment,均值差 +1.44,p 0.022
10. `cs_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1))` — enrichment,均值差 +1.38,p 0.002
11. `ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)` — enrichment,均值差 +1.35,p 0.035
12. `cross_corr(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), day_close(Close)), cross_delay(cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LogFloatCap), 1), 241)` — enrichment,均值差 +1.33,p 0.068
13. `cs_bucket_demean(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), day_close(Close))` — enrichment,均值差 +1.15,p 0.065
14. `day_last(Amt)` — enrichment,均值差 +0.92,p 0.037
15. `cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)` — enrichment,均值差 +0.88,p 0.059
16. `day_quantile_q25(Low)` — enrichment,均值差 +0.88,p 0.036

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.14(window cross_regbeta@10->20):`cross_regbeta(day_quantile_q25(Low), day_last(Amt), 20)`
