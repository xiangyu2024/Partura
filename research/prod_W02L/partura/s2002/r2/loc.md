# 定位:种子 2002,P 组,第 2 轮(只含 train / valid)

快照:prods2002M1_I0_open_search, prods2002M2_I0_open_search, prods2002Pr1a_Ea, prods2002Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.11 | -0.11 | -0.09 | +1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| -0.75 | -0.72 | -0.75 | +1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| -1.20 | -0.98 | -1.20 | -1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 30)` |
| -1.51 | -1.33 | -1.51 | +1 | 0 | prods2002M2_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)` |
| -1.62 | -1.62 | -1.44 | -1 | 0 | prods2002M2_I0_open_search | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)), 50)` |
| -1.67 | -1.67 | -1.54 | -1 | 5 | prods2002M2_I0_open_search | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(add(day_last(Volume), day_sum(Vwap)), day_max(Low)), 20)), day_std(Low))), 20)), 50)` |

## 共性:81 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.96 | 0.003 | 5 | -1.64 / -2.60 | `cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5))` |
| +0.77 | 0.060 | 6 | -1.83 / -2.60 | `day_std(Low)` |
| +0.77 | 0.060 | 6 | -1.83 / -2.60 | `log(add(day_q_stat_std(Vwap), day_std(Low)))` |
| +0.77 | 0.060 | 6 | -1.83 / -2.60 | `add(day_q_stat_std(Vwap), day_std(Low))` |
| +0.77 | 0.003 | 14 | -1.91 / -2.68 | `sigmoid(ListAge)` |
| +0.74 | 0.004 | 12 | -1.91 / -2.65 | `cross_tail_mean_q25(sigmoid(ListAge), 5)` |
| +0.62 | 0.044 | 19 | -2.07 / -2.69 | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` |
| +0.44 | 0.231 | 5 | -2.13 / -2.57 | `day_quantile(in_max(Ret))` |
| +0.44 | 0.231 | 5 | -2.13 / -2.57 | `log(day_quantile(in_max(Ret)))` |
| +0.43 | 0.369 | 8 | -2.16 / -2.59 | `day_hurst(Volume)` |
| +0.40 | 0.410 | 17 | -2.23 / -2.63 | `day_q_stat_std(Vwap)` |
| +0.30 | 0.513 | 4 | -2.26 / -2.56 | `ts_hurst(div(day_hurst(Volume), day_max(Low)), 20)` |
| +0.30 | 0.513 | 4 | -2.26 / -2.56 | `div(day_hurst(Volume), day_max(Low))` |
| +0.29 | 0.277 | 6 | -2.27 / -2.56 | `day_open(Ret)` |
| +0.23 | 0.496 | 4 | -2.33 / -2.55 | `div(day_last(Volume), day_max(Volume))` |
| +0.20 | 0.406 | 10 | -2.37 / -2.57 | `day_max(Volume)` |
| +0.16 | 0.838 | 25 | -2.43 / -2.59 | `day_std(Vwap)` |
| +0.14 | 0.063 | 55 | -2.50 / -2.64 | `div(day_last(Volume), day_max(Low))` |
| +0.02 | 0.855 | 9 | -2.53 / -2.54 | `add(day_q_stat_std(Vwap), day_std(Vwap))` |
| -0.00 | 0.786 | 4 | -2.55 / -2.54 | `day_last(Vwap)` |

## 拆解(48 次评估)

### head score -0.11:`ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.07 | -0.07 | -0.01 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)))` | -0.66 | -0.66 | +0.06 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))` | -0.66 | -0.66 | +0.07 | — | (子树本身) |
| sufficiency | `mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.25 | -0.02 | -0.25 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.82 | -0.82 | -0.00 | +0.71 | `ts_mean(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), 25)` |
| knockout | `log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)))` | -0.17 | -0.17 | -0.04 | +0.06 | `ts_mean(mul(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| knockout | `add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))` | -1.09 | -0.14 | -1.09 | +0.98 | `ts_mean(mul(log(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| knockout | `mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.24 | -0.24 | -0.06 | +0.12 | `ts_mean(mul(log(add(log(add(day_max(Amt), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| swap | `Amt->Volume` | -0.53 | -0.08 | -0.53 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| swap | `Vwap->Close` | -0.07 | -0.07 | -0.02 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| window | `ts_mean@25->12` | -0.50 | -0.33 | -0.50 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 12)` |
| window | `ts_mean@25->50` | -0.50 | -0.44 | -0.50 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` |

### head score -0.75:`ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20))` | -1.11 | -0.70 | -1.11 | — | (子树本身) |
| sufficiency | `log(cs_sum(day_argmax(Vwap)))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_hurst(div(day_last(Amt), day_max(Low)), 20)` | -1.11 | -0.70 | -1.11 | — | (子树本身) |
| sufficiency | `cs_sum(day_argmax(Vwap))` | — | — | — | — | 门槛废品 |
| knockout | `mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20))` | — | — | — | — | `ts_mean(log(cs_sum(day_argmax(Vwap))), 50)` |
| knockout | `log(cs_sum(day_argmax(Vwap)))` | -1.17 | -0.64 | -1.17 | +0.42 | `ts_mean(mul(cs_sum(day_argmax(Vwap)), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| knockout | `ts_hurst(div(day_last(Amt), day_max(Low)), 20)` | -1.15 | -0.46 | -1.15 | +0.40 | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), div(day_last(Amt), day_max(Low))), 50)` |
| knockout | `cs_sum(day_argmax(Vwap))` | -1.85 | -1.45 | -1.85 | +1.10 | `ts_mean(mul(log(day_argmax(Vwap)), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| swap | `Vwap->Close` | -0.76 | -0.72 | -0.76 | — | `ts_mean(mul(log(cs_sum(day_argmax(Close))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| swap | `Amt->Volume` | -0.96 | -0.96 | -0.95 | — | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| window | `ts_mean@50->25` | -1.40 | -0.81 | -1.40 | — | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.19 | -0.90 | -1.19 | — | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 100)` |

### head score -1.51:`ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20))` | -1.30 | -0.98 | -1.30 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap)))` | -1.91 | -1.91 | -1.72 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))` | -1.92 | -1.92 | -1.81 | — | (子树本身) |
| sufficiency | `mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20))` | -1.97 | -1.33 | -1.97 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20))` | -1.96 | -1.96 | -1.76 | +0.45 | `ts_mean(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), 50)` |
| knockout | `log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap)))` | -2.05 | -1.84 | -2.05 | +0.54 | `ts_mean(mul(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap)), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)` |
| knockout | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))` | -1.72 | -0.73 | -1.72 | +0.21 | `ts_mean(mul(log(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)` |
| knockout | `mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20))` | -1.48 | -1.23 | -1.48 | -0.03 | `ts_mean(mul(log(add(log(add(day_q_stat_std(Vwap), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)` |
| swap | `Vwap->Close` | -1.66 | -1.22 | -1.66 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Close), day_std(Close))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Close))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 50)` |
| swap | `Volume->Amt` | -1.55 | -1.49 | -1.55 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Amt), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Amt), day_max(Low)), 20)), 50)` |
| window | `ts_mean@50->25` | -1.80 | -1.25 | -1.80 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.82 | -1.46 | -1.82 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_mean(Volume), day_max(Low)), 20)), 100)` |

### head score -1.62:`ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20))` | -1.54 | -1.54 | -1.47 | — | (子树本身) |
| sufficiency | `ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)` | -1.36 | -1.36 | -1.21 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low)))` | -1.46 | -1.03 | -1.46 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))` | -2.19 | -2.19 | -1.57 | — | (子树本身) |
| knockout | `mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20))` | -3.04 | -2.05 | -3.04 | +1.42 | `ts_mean(log(day_quantile(in_max(Ret))), 50)` |
| knockout | `ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)` | -1.79 | -1.20 | -1.79 | +0.16 | `ts_mean(mul(log(day_quantile(in_max(Ret))), div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low)))), 50)` |
| knockout | `div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low)))` | -1.72 | -1.65 | -1.72 | +0.09 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(day_last(Volume), 20)), 50)` |
| knockout | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))` | -1.65 | -1.65 | -1.32 | +0.03 | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20))), 20)), 50)` |
| swap | `Volume->Amt` | -1.76 | -1.42 | -1.76 | — | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Amt), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Amt), day_var(Open)), 20)), day_std(Low))), 20)), 50)` |
| swap | `Vwap->Close` | -1.75 | -1.75 | -1.46 | — | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Close), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)), 50)` |
| window | `ts_mean@50->25` | -2.26 | -1.77 | -2.26 | — | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)), 25)` |
| window | `ts_mean@50->100` | -2.90 | -2.18 | -2.90 | — | `ts_mean(mul(log(day_quantile(in_max(Ret))), ts_hurst(div(day_last(Volume), add(mul(log(add(day_q_stat_std(Vwap), day_std(Low))), ts_hurst(div(day_hurst(Volume), day_var(Open)), 20)), day_std(Low))), 20)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5))` — enrichment,均值差 +0.96,p 0.003
2. `day_std(Low)` — enrichment,均值差 +0.77,p 0.060
3. `log(add(day_q_stat_std(Vwap), day_std(Low)))` — enrichment,均值差 +0.77,p 0.060
4. `add(day_q_stat_std(Vwap), day_std(Low))` — enrichment,均值差 +0.77,p 0.060
5. `sigmoid(ListAge)` — enrichment,均值差 +0.77,p 0.003
6. `cross_tail_mean_q25(sigmoid(ListAge), 5)` — enrichment,均值差 +0.74,p 0.004
7. `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` — enrichment,均值差 +0.62,p 0.044
8. `div(day_last(Volume), day_max(Low))` — enrichment,均值差 +0.14,p 0.063

## 本组之前各轮的任务

- `prods2002Pr1a_Ea`:核心 `div(day_last(Volume), day_max(Low))`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1626, 'c05_no_core': 3037}
  - score -1.48(train -1.48 valid -1.46):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)), 5))`
  - score -1.51(train -1.51 valid -1.44):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5))), 5))`
  - score -1.66(train -1.23 valid -1.66):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)))`
  - score -1.71(train -1.71 valid -1.50):`cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(cross_tail_mean_q25(sigmoid(sigmoid(cs_bucket_rank(div(day_last(Volume), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)))), 5), 5))`
  - score -1.80(train -1.59 valid -1.80):`cs_bucket_rank(div(div(day_last(Volume), day_max(Low)), day_max(Low)), cross_tail_mean_q25(cs_bucket_rank(div(div(day_last(Volume), day_max(Low)), day_max(Low)), cross_tail_mean_q25(sigmoid(ListAge), 5)), 5))`
- `prods2002Pr1b_Nb`:核心 `—`;评分 0,过线 0,入 heads 0;采样计数 {'c05_skeleton': 14}

## 比原 head 好的拆解变体(R 候选)

(没有)
