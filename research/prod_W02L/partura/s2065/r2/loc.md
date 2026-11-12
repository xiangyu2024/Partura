# 定位:种子 2065,P 组,第 2 轮(只含 train / valid)

快照:prods2065M1_I0_open_search, prods2065M2_I0_open_search, prods2065Pr1a_Na, prods2065Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.52 | -1.52 | -1.13 | +1 | 20 | prods2065M1_I0_open_search | `day_q_stat_std(in_max_rolling(Amt, 60))` |
| -1.54 | -1.54 | -1.15 | +1 | 20 | prods2065M1_I0_open_search | `day_q_stat_std(in_max_rolling(Volume, 60))` |
| -1.56 | -1.36 | -1.56 | -1 | 5 | prods2065M2_I0_open_search | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| -1.60 | -1.30 | -1.60 | -1 | 20 | prods2065M2_I0_open_search | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |
| -1.64 | -1.07 | -1.64 | -1 | 5 | prods2065M2_I0_open_search | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| -2.35 | -1.64 | -2.35 | -1 | 20 | prods2065M1_I0_open_search | `day_var(in_max_rolling(Vwap, 60))` |

## 共性:74 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.24 | 0.000 | 5 | -0.46 / -2.70 | `pow_05(day_mean(Close))` |
| +2.06 | 0.000 | 9 | -0.74 / -2.80 | `day_mean(Close)` |
| +1.10 | 0.018 | 6 | -1.54 / -2.64 | `day_close(Low)` |
| +0.84 | 0.046 | 8 | -1.80 / -2.64 | `inv(day_q_stat_std(Close))` |
| +0.78 | 0.056 | 9 | -1.87 / -2.64 | `day_q_stat_std(Close)` |
| +0.71 | 0.076 | 12 | -1.95 / -2.67 | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` |
| +0.71 | 0.076 | 12 | -1.95 / -2.67 | `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))` |
| +0.67 | 0.106 | 11 | -1.98 / -2.65 | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |
| +0.55 | 0.200 | 9 | -2.07 / -2.62 | `add(ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20), ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20))` |
| +0.55 | 0.200 | 9 | -2.07 / -2.62 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| +0.55 | 0.200 | 9 | -2.07 / -2.62 | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| +0.55 | 0.200 | 9 | -2.07 / -2.62 | `create_like(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))), 2)` |
| +0.49 | 0.257 | 8 | -2.11 / -2.60 | `div(add(ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20), ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)), create_like(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))), 2))` |
| +0.46 | 0.325 | 4 | -2.11 / -2.57 | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237))))))` |
| +0.46 | 0.325 | 4 | -2.11 / -2.57 | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)))))` |
| +0.46 | 0.325 | 4 | -2.11 / -2.57 | `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237))))` |
| +0.46 | 0.325 | 4 | -2.11 / -2.57 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)))))), 20)` |
| +0.46 | 0.325 | 4 | -2.11 / -2.57 | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)))))), 20)` |
| +0.46 | 0.325 | 4 | -2.11 / -2.57 | `add(ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)))))), 20), ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(div(sub(High, Low), Close), 6, 237)))))), 20))` |
| -0.55 | 0.927 | 6 | -3.05 / -2.50 | `day_last(Close)` |

## 拆解(25 次评估)

### head score -1.56:`ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` | -1.65 | -1.30 | -1.65 | — | (子树本身) |
| sufficiency | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` | -3.54 | -3.54 | -2.92 | — | (子树本身) |
| sufficiency | `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))` | -3.54 | -3.54 | -2.92 | — | (子树本身) |
| knockout | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` | -1.56 | -1.21 | -1.56 | -0.00 | `ts_stddev(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))), 20)` |
| knockout | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` | -1.30 | -1.21 | -1.30 | -0.26 | `ts_stddev(abs_(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))), 20)` |
| swap | `Close->Vwap` | -1.76 | -1.29 | -1.76 | — | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Vwap, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Vwap, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| swap | `Open->Close` | -1.67 | -1.21 | -1.67 | — | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Close, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Close, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| window | `ts_stddev@20->10` | -1.48 | -1.32 | -1.48 | — | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 10)` |
| window | `ts_stddev@20->40` | -1.41 | -1.15 | -1.41 | — | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 40)` |

### head score -1.60:`abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` | -3.54 | -3.54 | -2.92 | — | (子树本身) |
| sufficiency | `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))` | -3.54 | -3.54 | -2.92 | — | (子树本身) |
| knockout | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` | -1.60 | -1.34 | -1.60 | -0.00 | `abs_(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` |
| swap | `Close->Vwap` | -1.82 | -1.30 | -1.82 | — | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Vwap, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Vwap, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |
| swap | `Open->Close` | -1.68 | -1.31 | -1.68 | — | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Close, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Close, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |
| window | `in_delay@4->2` | -1.57 | -1.25 | -1.57 | — | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 2)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |
| window | `in_delay@4->8` | -2.05 | -1.35 | -2.05 | — | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 8)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` |

### head score -1.64:`ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` | -1.65 | -1.30 | -1.65 | — | (子树本身) |
| sufficiency | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` | -3.54 | -3.54 | -2.92 | — | (子树本身) |
| sufficiency | `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))` | -3.54 | -3.54 | -2.92 | — | (子树本身) |
| knockout | `abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))))` | -1.69 | -1.69 | -1.06 | +0.05 | `ts_mean(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))), 20)` |
| knockout | `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` | -1.36 | -1.04 | -1.36 | -0.29 | `ts_mean(abs_(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))), 20)` |
| swap | `Close->Vwap` | -1.84 | -1.07 | -1.84 | — | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Vwap, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Vwap, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| swap | `Open->Close` | -1.76 | -1.05 | -1.76 | — | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Close, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Close, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 20)` |
| window | `ts_mean@20->10` | -1.88 | -1.15 | -1.88 | — | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 10)` |
| window | `ts_mean@20->40` | -1.45 | -1.04 | -1.45 | — | `ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_05(day_mean(Close))` — enrichment,均值差 +2.24,p 0.000
2. `day_mean(Close)` — enrichment,均值差 +2.06,p 0.000
3. `day_close(Low)` — enrichment,均值差 +1.10,p 0.018
4. `inv(day_q_stat_std(Close))` — enrichment,均值差 +0.84,p 0.046
5. `day_q_stat_std(Close)` — enrichment,均值差 +0.78,p 0.056
6. `cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)))))` — enrichment,均值差 +0.71,p 0.076
7. `day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237)), in_sorted_cumsum_backward(in_slice(div(Close, in_delay(Open, 4)), 6, 237), in_slice(Volume, 6, 237))))` — enrichment,均值差 +0.71,p 0.076

## 本组之前各轮的任务

- `prods2065Pr1a_Na`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.42(train -0.42 valid -0.40):`cs_last_low10(inv(day_q_stat_std(Open)), pow_05(pow_05(day_mean(Close))))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(inv(day_q_stat_std(Close)), signedpower(day_mean(Close)))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(inv(day_q_stat_std(Close)), day_mean(Close))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(inv(day_q_stat_std(Close)), pow_05(pow_05(day_mean(Close))))`
  - score -0.44(train -0.44 valid -0.35):`cs_last_low10(cs_last_low10(inv(day_q_stat_std(Close)), pow_05(day_mean(Close))), day_mean(Close))`
- `prods2065Pr1b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.03(train -0.91 valid -1.03):`mul(day_max(Low), signedpower(mul(day_max(Low), signedpower(day_flat_ratio(Close)))))`
  - score -1.05(train -0.89 valid -1.05):`mul(day_close(Low), signedpower(mul(day_close(Low), signedpower(day_flat_ratio(Close)))))`
  - score -1.27(train -1.20 valid -1.27):`mul(day_close(Low), signedpower(day_flat_ratio(Low)))`
  - score -1.27(train -1.27 valid -1.04):`mul(day_close(Low), signedpower(day_flat_ratio(Close)))`
  - score -1.38(train -1.38 valid -0.92):`mul(day_close(Low), pow_2_5(day_flat_ratio(Low)))`

## 比原 head 好的拆解变体(R 候选)

(没有)
