# 定位:种子 2002,P 组,第 3 轮(只含 train / valid)

快照:prods2002M1_I0_open_search, prods2002M2_I0_open_search, prods2002M3_I0_open_search, prods2002Pr1a_Ea, prods2002Pr1b_Nb, prods2002Pr2a_Ea, prods2002Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.01 | +0.01 | +0.03 | +1 | 0 | prods2002M1_I0_open_search | `cross_ema(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| -0.75 | -0.72 | -0.75 | +1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| -1.18 | -0.50 | -1.18 | +1 | 20 | prods2002M3_I0_open_search | `ts_mean(ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20), 50)` |
| -1.20 | -0.98 | -1.20 | -1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 30)` |
| -1.43 | -1.27 | -1.43 | -1 | 0 | prods2002M3_I0_open_search | `ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_sum(Vwap)), 50)` |
| -1.51 | -1.33 | -1.51 | +1 | 0 | prods2002M2_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)` |
| -1.52 | -1.52 | -1.13 | +1 | 0 | prods2002M3_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| -1.62 | -1.62 | -1.44 | -1 | 0 | prods2002M2_I0_open_search | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)), 50)` |
| -1.67 | -1.67 | -1.54 | -1 | 5 | prods2002M2_I0_open_search | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(add(day_last(Volume), day_sum(Vwap)), day_max(Low)), 20)), day_std(Low))), 20)), 50)` |

## 共性:159 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.28 | 0.001 | 6 | -0.91 / -2.19 | `mul(ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1), ts_delay(ts_delta(log(day_last(Close)), 1), 1))` |
| +1.28 | 0.012 | 4 | -0.90 / -2.18 | `day_var(in_delay(Low, 5))` |
| +1.23 | 0.004 | 4 | -0.95 / -2.17 | `cs_bucket_zscore(cross_stddev(sub(log(day_sum(Amt)), LogFloatCap), 120), LogFloatCap)` |
| +1.18 | 0.000 | 21 | -1.12 / -2.30 | `ts_delay(ts_delta(log(day_last(Close)), 1), 1)` |
| +1.17 | 0.000 | 7 | -1.02 / -2.19 | `cross_stddev(sub(log(day_sum(Amt)), LogFloatCap), 120)` |
| +1.11 | 0.000 | 16 | -1.15 / -2.25 | `cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60)` |
| +1.10 | 0.000 | 15 | -1.15 / -2.25 | `ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1)` |
| +1.08 | 0.000 | 23 | -1.22 / -2.30 | `day_es_ratio_lo(Vwap)` |
| +1.01 | 0.000 | 34 | -1.35 / -2.36 | `sub(log(day_sum(Amt)), LogFloatCap)` |
| +1.00 | 0.000 | 40 | -1.40 / -2.39 | `log(day_sum(Amt))` |
| +0.96 | 0.000 | 41 | -1.43 / -2.39 | `day_sum(Amt)` |
| +0.95 | 0.034 | 4 | -1.22 / -2.17 | `ts_delay(cross_zscore(ts_delta(log(day_last(Close)), 1), 60), 1)` |
| +0.95 | 0.034 | 4 | -1.22 / -2.17 | `cross_zscore(ts_delta(log(day_last(Close)), 1), 60)` |
| +0.95 | 0.034 | 4 | -1.22 / -2.17 | `mul(ts_delay(cross_zscore(ts_delta(log(day_last(Close)), 1), 60), 1), ts_delay(ts_delta(log(day_last(Close)), 1), 1))` |
| +0.63 | 0.000 | 40 | -1.67 / -2.30 | `day_last(Close)` |
| +0.57 | 0.000 | 38 | -1.71 / -2.28 | `log(day_last(Close))` |
| +0.57 | 0.000 | 36 | -1.71 / -2.27 | `ts_delta(log(day_last(Close)), 1)` |
| +0.52 | 0.129 | 5 | -1.64 / -2.16 | `cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5))` |
| +0.34 | 0.345 | 7 | -1.81 / -2.16 | `ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20)` |
| +0.33 | 0.423 | 6 | -1.83 / -2.16 | `day_std(Low)` |

## 拆解(48 次评估)

### head score +0.01:`cross_ema(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.07 | -0.07 | -0.01 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)))` | -0.66 | -0.66 | +0.06 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))` | -0.66 | -0.66 | +0.07 | — | (子树本身) |
| sufficiency | `mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.25 | -0.02 | -0.25 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.67 | -0.67 | -0.18 | +0.68 | `cross_ema(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), 12)` |
| knockout | `log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)))` | -0.17 | -0.17 | +0.11 | +0.18 | `cross_ema(mul(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| knockout | `add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))` | -0.77 | +0.27 | -0.77 | +0.77 | `cross_ema(mul(log(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| knockout | `mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.60 | +0.05 | -0.60 | +0.61 | `cross_ema(mul(log(add(log(add(day_max(Amt), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| swap | `Amt->Volume` | -0.36 | +0.24 | -0.36 | — | `cross_ema(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| swap | `Vwap->Close` | -0.03 | -0.00 | -0.03 | — | `cross_ema(mul(log(add(mul(log(add(day_max(Amt), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| window | `cross_ema@12->6` | -0.01 | -0.01 | +0.00 | — | `cross_ema(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 6)` |
| window | `cross_ema@12->24` | -0.38 | -0.34 | -0.38 | — | `cross_ema(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 24)` |

### head score -1.18:`ts_mean(ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20)` | -0.68 | -0.68 | -0.61 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.65 | -1.16 | -1.65 | — | (子树本身) |
| sufficiency | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), day_max(Low))` | -1.55 | -1.55 | -1.50 | — | (子树本身) |
| knockout | `ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20)` | -1.61 | -1.22 | -1.61 | +0.43 | `ts_mean(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -0.94 | -0.69 | -0.94 | -0.24 | `ts_mean(ts_hurst(day_last(Volume), 20), 50)` |
| knockout | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -3.43 | -2.42 | -3.43 | +2.25 | `ts_mean(ts_hurst(div(day_last(Volume), div(day_last(Volume), day_max(Low))), 20), 50)` |
| knockout | `div(day_last(Volume), day_max(Low))` | -1.37 | -0.53 | -1.37 | +0.19 | `ts_mean(ts_hurst(div(day_last(Volume), ts_hurst(day_last(Volume), 20)), 20), 50)` |
| swap | `Volume->Amt` | -1.25 | -0.34 | -1.25 | — | `ts_mean(ts_hurst(div(day_last(Amt), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 20), 50)` |
| swap | `Low->High` | -1.21 | -0.50 | -1.21 | — | `ts_mean(ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(High)), 20)), 20), 50)` |
| window | `ts_mean@50->25` | -1.48 | -0.88 | -1.48 | — | `ts_mean(ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20), 25)` |
| window | `ts_mean@50->100` | -1.51 | -0.30 | -1.51 | — | `ts_mean(ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20), 100)` |

### head score -1.43:`ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_sum(Vwap)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_sum(Vwap))` | -1.49 | -1.26 | -1.49 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.65 | -1.16 | -1.65 | — | (子树本身) |
| sufficiency | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), day_max(Low))` | -1.55 | -1.55 | -1.50 | — | (子树本身) |
| knockout | `add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_sum(Vwap))` | -1.61 | -1.22 | -1.61 | +0.19 | `ts_mean(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.34 | -1.24 | -1.34 | -0.09 | `ts_mean(add(day_last(Volume), day_sum(Vwap)), 50)` |
| knockout | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.81 | -1.68 | -1.81 | +0.39 | `ts_mean(add(div(day_last(Volume), div(day_last(Volume), day_max(Low))), day_sum(Vwap)), 50)` |
| knockout | `div(day_last(Volume), day_max(Low))` | -1.51 | -1.23 | -1.51 | +0.09 | `ts_mean(add(div(day_last(Volume), ts_hurst(day_last(Volume), 20)), day_sum(Vwap)), 50)` |
| swap | `Volume->Amt` | -3.01 | -1.96 | -3.01 | — | `ts_mean(add(div(day_last(Amt), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), day_sum(Vwap)), 50)` |
| swap | `Low->High` | -1.50 | -1.28 | -1.50 | — | `ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(High)), 20)), day_sum(Vwap)), 50)` |
| window | `ts_mean@50->25` | -1.52 | -1.26 | -1.52 | — | `ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_sum(Vwap)), 25)` |
| window | `ts_mean@50->100` | -1.57 | -1.47 | -1.57 | — | `ts_mean(add(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_sum(Vwap)), 100)` |

### head score -1.52:`ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.39 | -1.39 | -0.86 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20)))` | -2.07 | -2.07 | -1.71 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))` | -2.07 | -2.07 | -1.69 | — | (子树本身) |
| sufficiency | `mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -2.25 | -2.25 | -1.90 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -2.35 | -2.35 | -1.44 | +0.83 | `ts_mean(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), 50)` |
| knockout | `log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20)))` | -1.27 | -1.27 | -0.93 | -0.24 | `ts_mean(mul(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20)), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))` | -2.22 | -2.22 | -1.19 | +0.70 | `ts_mean(mul(log(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -2.01 | -2.01 | -1.23 | +0.50 | `ts_mean(mul(log(add(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Volume->Amt` | -1.65 | -1.65 | -1.21 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Amt), ts_hurst(div(day_last(Amt), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), ts_hurst(div(day_last(Amt), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| swap | `Low->High` | -1.49 | -1.49 | -1.06 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(High)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(High)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(High)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(High)), 20)), 50)` |
| window | `ts_mean@50->25` | -1.09 | -1.09 | -0.75 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.76 | -1.76 | -1.18 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), ts_hurst(div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `mul(ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1), ts_delay(ts_delta(log(day_last(Close)), 1), 1))` — enrichment,均值差 +1.28,p 0.001
2. `day_var(in_delay(Low, 5))` — enrichment,均值差 +1.28,p 0.012
3. `cs_bucket_zscore(cross_stddev(sub(log(day_sum(Amt)), LogFloatCap), 120), LogFloatCap)` — enrichment,均值差 +1.23,p 0.004
4. `ts_delay(ts_delta(log(day_last(Close)), 1), 1)` — enrichment,均值差 +1.18,p 0.000
5. `cross_stddev(sub(log(day_sum(Amt)), LogFloatCap), 120)` — enrichment,均值差 +1.17,p 0.000
6. `cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60)` — enrichment,均值差 +1.11,p 0.000
7. `ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1)` — enrichment,均值差 +1.10,p 0.000
8. `day_es_ratio_lo(Vwap)` — enrichment,均值差 +1.08,p 0.000
9. `sub(log(day_sum(Amt)), LogFloatCap)` — enrichment,均值差 +1.01,p 0.000
10. `log(day_sum(Amt))` — enrichment,均值差 +1.00,p 0.000
11. `day_sum(Amt)` — enrichment,均值差 +0.96,p 0.000
12. `ts_delay(cross_zscore(ts_delta(log(day_last(Close)), 1), 60), 1)` — enrichment,均值差 +0.95,p 0.034
13. `cross_zscore(ts_delta(log(day_last(Close)), 1), 60)` — enrichment,均值差 +0.95,p 0.034
14. `mul(ts_delay(cross_zscore(ts_delta(log(day_last(Close)), 1), 60), 1), ts_delay(ts_delta(log(day_last(Close)), 1), 1))` — enrichment,均值差 +0.95,p 0.034
15. `day_last(Close)` — enrichment,均值差 +0.63,p 0.000
16. `log(day_last(Close))` — enrichment,均值差 +0.57,p 0.000
17. `ts_delta(log(day_last(Close)), 1)` — enrichment,均值差 +0.57,p 0.000

## 本组之前各轮的任务

- `prods2002Pr1a_Ea`:核心 `div(day_last(Volume), day_max(Low))`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1626, 'c05_no_core': 3037}
  - score -1.48(train -1.48 valid -1.46):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)), 5))`
  - score -1.51(train -1.51 valid -1.44):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5))), 5))`
  - score -1.66(train -1.23 valid -1.66):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)))`
  - score -1.71(train -1.71 valid -1.50):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(cross_tail_mean_q25(sigmoid(sigmoid(cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)))), 5), 5))`
  - score -1.80(train -1.59 valid -1.80):`cs_bucket_rank(div(div(day_last(Volume), day_max(Low)), day_max(Low)), cross_tail_mean_q25(cs_bucket_rank(div(div(day_last(Volume), day_max(Low)), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)), 5))`
- `prods2002Pr1b_Nb`:核心 `—`;评分 0,过线 0,入 heads 0;采样计数 {'c05_skeleton': 14}
- `prods2002Pr2a_Ea`:核心 `ts_hurst(div(day_last(Volume), day_max(Volume)), 20)`;评分 0,过线 0,入 heads 0;采样计数 {}
- `prods2002Pr2b_Nb`:核心 `—`;评分 100,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.21(train -0.21 valid -0.09):`cross_regbeta(mul(ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1), ts_delay(ts_delta(day_var(in_delay(Low, 5)), 1), 1)), day_es_ratio_lo(Vwap), 120)`
  - score -0.25(train -0.09 valid -0.25):`cross_regbeta(mul(ts_delay(cross_zscore(sub(day_last(Close), LogFloatCap), 60), 1), ts_delay(ts_delta(day_var(in_quantile_q75(Low, 5)), 1), 1)), day_es_ratio_lo(Vwap), 120)`
  - score -0.32(train +0.16 valid -0.32):`cross_regbeta(mul(ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1), mul(ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1), ts_delay(ts_delta(log(day_last(Close)), 1), 1))), day_es_ratio_lo(Vwap), 120)`
  - score -0.48(train -0.48 valid -0.30):`cross_regbeta(mul(ts_delay(cross_zscore(sub(log(day_sum(Amt)), LogFloatCap), 60), 1), ts_delay(ts_delta(log(day_sum(Amt)), 1), 1)), day_es_ratio_lo(Vwap), 120)`
  - score -0.50(train -0.17 valid -0.50):`cross_regbeta(mul(ts_delay(cross_zscore(sub(log(day_sum(Close)), LogFloatCap), 60), 20), ts_delay(ts_delta(day_var(in_delay(Low, 5)), 1), 1)), day_es_ratio_lo(Vwap), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(knockout div(day_last(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))):`ts_mean(ts_hurst(day_last(Volume), 20), 50)`
