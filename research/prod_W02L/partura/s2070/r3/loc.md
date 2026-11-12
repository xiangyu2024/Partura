# 定位:种子 2070,P 组,第 3 轮(只含 train / valid)

快照:prods2070M1_I0_open_search, prods2070M2_I0_open_search, prods2070M3_I0_open_search, prods2070Pr1a_Ea, prods2070Pr1b_Nb, prods2070Pr2a_Ea, prods2070Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.77 | -0.35 | -0.77 | +1 | 0 | prods2070M3_I0_open_search | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60), 50)` |
| -1.50 | -1.50 | -0.90 | -1 | 20 | prods2070M2_I0_open_search | `cross_mean(day_cov(select_where(is_gt(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2), add(in_mean_full(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2)), in_stddev_full(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2))), False), signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2), nan_tensor(in_slice(Low, 2, 237))), div(in_slice(Ret, 2, 237), signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2))), 20)` |
| -1.52 | -1.36 | -1.52 | +1 | 0 | prods2070M3_I0_open_search | `cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20)` |
| -1.52 | -1.36 | -1.52 | +1 | 0 | prods2070M3_I0_open_search | `div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))` |
| -1.68 | -1.68 | -1.30 | +1 | 20 | prods2070M2_I0_open_search | `cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2), div(in_slice(Ret, 2, 237), signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2))), 20)` |
| -1.83 | -1.83 | -1.66 | +1 | 5 | prods2070M2_I0_open_search | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2), div(in_slice(Ret, 2, 237), signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2))), 20), cross_stddev(day_cov(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2), div(in_slice(Ret, 2, 237), signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5), in_mean_rolling_multi([in_slice(Open, 2, 237), in_slice(Close, 2, 237), in_slice(High, 2, 237), in_slice(Low, 2, 237)], 5)), 2))), 20))` |
| -2.01 | -2.01 | -1.77 | +1 | 20 | prods2070M1_I0_open_search | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 5)` |
| -2.76 | -1.73 | -2.76 | -1 | 20 | prods2070M1_I0_open_search | `day_quantile_q75(mul(High, Ret))` |
| -2.80 | -2.21 | -2.80 | +1 | 5 | prods2070M1_I0_open_search | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` |

## 共性:209 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.87 | 0.000 | 5 | -0.47 / -2.34 | `ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40)` |
| +1.37 | 0.001 | 7 | -0.97 / -2.34 | `ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20)` |
| +1.29 | 0.000 | 15 | -1.09 / -2.39 | `day_zero_ratio(Volume)` |
| +1.04 | 0.001 | 8 | -1.30 / -2.33 | `day_corr(Ret, Amt)` |
| +0.91 | 0.023 | 4 | -1.40 / -2.31 | `ts_mean(day_corr(Ret, Amt), 40)` |
| +0.88 | 0.024 | 4 | -1.43 / -2.31 | `cs_last_high10(cross_argmin(day_es_ratio_lo(Close), 241), ts_regalpha(day_argmin(Vwap), LogFloatCap, 10))` |
| +0.85 | 0.049 | 4 | -1.46 / -2.31 | `ts_mean(day_skew(mul(Ret, Volume)), 20)` |
| +0.76 | 0.059 | 4 | -1.55 / -2.31 | `day_autocorr_n1(Close)` |
| +0.76 | 0.059 | 4 | -1.55 / -2.31 | `cs_last_low20(day_durbin_watson(Vwap), day_autocorr_n1(Close))` |
| +0.76 | 0.012 | 10 | -1.57 / -2.33 | `ts_std(day_quantile_q75(mul(High, Ret)), 20)` |
| +0.75 | 0.005 | 12 | -1.58 / -2.34 | `day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237))` |
| +0.74 | 0.014 | 9 | -1.59 / -2.33 | `ts_mean(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 20)` |
| +0.74 | 0.007 | 11 | -1.59 / -2.33 | `cross_argmin(day_es_ratio_lo(Close), 241)` |
| +0.70 | 0.050 | 8 | -1.62 / -2.32 | `ts_stddev(day_quantile_q75(mul(High, Ret)), 20)` |
| +0.69 | 0.082 | 4 | -1.61 / -2.31 | `cross_valid_count(day_argmin(Open), 10)` |
| +0.69 | 0.082 | 4 | -1.61 / -2.31 | `day_argmin(Open)` |
| +0.64 | 0.004 | 26 | -1.73 / -2.37 | `day_sum(sub(Close, Vwap))` |
| +0.63 | 0.016 | 13 | -1.70 / -2.33 | `day_es_ratio_lo(Close)` |
| +0.63 | 0.104 | 5 | -1.68 / -2.31 | `day_quantile(Amt)` |
| +0.63 | 0.104 | 5 | -1.68 / -2.31 | `day_durbin_watson(Vwap)` |

## 拆解(27 次评估)

### head score -0.77:`ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | -1.46 | -1.46 | -1.17 | — | (子树本身) |
| sufficiency | `day_cov(cross_mean(Open, 241), Amt)` | -1.53 | -1.53 | -1.04 | — | (子树本身) |
| knockout | `cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | -1.54 | -1.54 | -1.38 | +0.77 | `ts_std(day_cov(cross_mean(Open, 241), Amt), 50)` |
| swap | `Open->Close` | -0.78 | -0.39 | -0.78 | — | `ts_std(cross_stddev(day_cov(cross_mean(Close, 241), Amt), 60), 50)` |
| swap | `Amt->Volume` | -0.76 | +0.02 | -0.76 | — | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Volume), 60), 50)` |
| window | `ts_std@50->25` | -0.44 | -0.44 | +0.05 | — | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60), 25)` |
| window | `ts_std@50->100` | -0.66 | -0.61 | -0.66 | — | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60), 100)` |

### head score -1.52:`cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))` | -4.15 | -3.12 | -4.15 | — | (子树本身) |
| sufficiency | `day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))` | -2.19 | -2.19 | -2.09 | — | (子树本身) |
| knockout | `div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))` | -3.50 | -2.48 | -3.50 | +1.98 | `cross_mean(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), 20)` |
| swap | `Amt->Volume` | — | — | — | — | `cross_mean(div(day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20)` |
| swap | `Volume->Amt` | — | — | — | — | `cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Amt, sub(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True))), day_sum(mul(in_sum(Amt), is_lt(Amt, sub(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True)))), 20)` |
| window | `cross_mean@20->10` | -1.53 | -1.34 | -1.53 | — | `cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 10)` |
| window | `cross_mean@20->40` | -1.60 | -1.39 | -1.60 | — | `cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 40)` |

### head score -1.52:`div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20)` | — | — | — | — | 门槛废品 |
| sufficiency | `div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20)` | -1.58 | -1.36 | -1.58 | — | (子树本身) |
| sufficiency | `day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))` | -3.98 | -3.98 | -2.04 | — | (子树本身) |
| knockout | `cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20)` | — | — | — | — | `div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20), div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))))` |
| knockout | `div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))))` | -1.74 | -1.40 | -1.74 | +0.21 | `div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20), cross_mean(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20))` |
| knockout | `cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20)` | — | — | — | — | `div(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))` |
| knockout | `div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))` | -3.36 | -2.29 | -3.36 | +1.83 | `div(cross_mean(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), 20), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))` |
| swap | `Amt->Volume` | — | — | — | — | `div(cross_mean(div(day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 20), cross_mean(div(day_sum(mul(in_sum(Volume), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Volume), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))` |
| swap | `Volume->Amt` | — | — | — | — | `div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Amt, sub(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True))), day_sum(mul(in_sum(Amt), is_lt(Amt, sub(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True)))), 20), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Amt, add(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True)), is_gt(Amt, add(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Amt, add(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True)), is_gt(Amt, add(cross_mean(Amt, 20), cross_stddev(Amt, 20)), True))))), 20))` |
| window | `cross_mean@20->10` | -1.53 | -1.34 | -1.53 | — | `div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 10), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))` |
| window | `cross_mean@20->40` | -1.60 | -1.39 | -1.60 | — | `div(cross_mean(div(day_sum(mul(in_sum(Amt), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))), day_sum(mul(in_sum(Volume), is_lt(Volume, sub(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), 40), cross_mean(div(day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)))), day_sum(mul(in_sum(Amt), mul(in_is_neighbor(is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True)), is_gt(Volume, add(cross_mean(Volume, 20), cross_stddev(Volume, 20)), True))))), 20))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40)` — enrichment,均值差 +1.87,p 0.000
2. `ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20)` — enrichment,均值差 +1.37,p 0.001
3. `day_zero_ratio(Volume)` — enrichment,均值差 +1.29,p 0.000
4. `day_corr(Ret, Amt)` — enrichment,均值差 +1.04,p 0.001
5. `ts_mean(day_corr(Ret, Amt), 40)` — enrichment,均值差 +0.91,p 0.023
6. `cs_last_high10(cross_argmin(day_es_ratio_lo(Close), 241), ts_regalpha(day_argmin(Vwap), LogFloatCap, 10))` — enrichment,均值差 +0.88,p 0.024
7. `ts_mean(day_skew(mul(Ret, Volume)), 20)` — enrichment,均值差 +0.85,p 0.049
8. `day_autocorr_n1(Close)` — enrichment,均值差 +0.76,p 0.059
9. `cs_last_low20(day_durbin_watson(Vwap), day_autocorr_n1(Close))` — enrichment,均值差 +0.76,p 0.059
10. `ts_std(day_quantile_q75(mul(High, Ret)), 20)` — enrichment,均值差 +0.76,p 0.012
11. `day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237))` — enrichment,均值差 +0.75,p 0.005
12. `ts_mean(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 20)` — enrichment,均值差 +0.74,p 0.014
13. `cross_argmin(day_es_ratio_lo(Close), 241)` — enrichment,均值差 +0.74,p 0.007
14. `ts_stddev(day_quantile_q75(mul(High, Ret)), 20)` — enrichment,均值差 +0.70,p 0.050
15. `cross_valid_count(day_argmin(Open), 10)` — enrichment,均值差 +0.69,p 0.082
16. `day_argmin(Open)` — enrichment,均值差 +0.69,p 0.082
17. `day_sum(sub(Close, Vwap))` — enrichment,均值差 +0.64,p 0.004
18. `day_es_ratio_lo(Close)` — enrichment,均值差 +0.63,p 0.016
19. `ts_regalpha(day_argmin(Vwap), LogFloatCap, 10)` — enrichment,均值差 +0.60,p 0.045
20. `day_last(Vwap)` — enrichment,均值差 +0.58,p 0.012
21. `ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20)` — enrichment,均值差 +0.58,p 0.028
22. `day_argmin(Vwap)` — enrichment,均值差 +0.54,p 0.060

## 本组之前各轮的任务

- `prods2070Pr1a_Ea`:核心 `day_quantile_q75(mul(High, Ret))`;评分 101,过线 0,入 heads 0;采样计数 {'c05_no_core': 1754, 'c05_skeleton': 829}
  - score -0.87(train -0.87 valid -0.69):`cross_rank(ts_stddev(day_quantile_q75(mul(High, Ret)), 20), 60)`
  - score -1.03(train -0.99 valid -1.03):`div(ts_mean(day_quantile_q75(mul(High, Ret)), 10), div(ts_mean(day_quantile_q75(mul(High, Ret)), 10), ts_std(day_quantile_q75(mul(High, Ret)), 20)))`
  - score -1.03(train -1.03 valid -0.18):`div(ts_mean(day_quantile_q75(mul(High, High)), 10), ts_std(day_quantile_q75(mul(High, Ret)), 20))`
  - score -1.05(train -1.02 valid -1.05):`div(ts_mean(day_quantile_q75(sigmoid(Vwap)), 10), ts_std(day_quantile_q75(mul(High, Ret)), 20))`
  - score -1.06(train -1.03 valid -1.06):`div(ts_mean(sigmoid(ts_stddev(day_quantile_q75(mul(High, Ret)), 20)), 10), ts_std(day_quantile_q75(mul(High, Ret)), 20))`
- `prods2070Pr1b_Nb`:核心 `—`;评分 82,过线 0,入 heads 0;采样计数 {}
  - score -0.08(train -0.08 valid +0.17):`ts_mean(ts_regres(day_last(Vwap), ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40), 10), 40)`
  - score -0.21(train +0.09 valid -0.21):`ts_mean(ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40), 40)`
  - score -0.42(train -0.42 valid -0.07):`ts_mean(ts_regres(ts_mean(day_skew(pow_05(Volume)), 20), ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40), 20), 40)`
  - score -0.44(train -0.44 valid -0.07):`ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40)`
  - score -0.48(train -0.48 valid -0.01):`ts_mean(ts_regres(ts_mean(day_skew(mul(Ret, Ret)), 20), day_zero_ratio(Volume), 20), 40)`
- `prods2070Pr2a_Ea`:核心 `ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20)`;评分 58,过线 0,入 heads 0;采样计数 {'c05_no_core': 6103, 'c05_skeleton': 3193}
  - score -2.68(train -2.42 valid -2.68):`day_es_ratio_hi(Open)`
  - score -2.69(train -2.69 valid -2.58):`day_es_ratio_lo(Open)`
  - score -2.73(train -2.73 valid -2.68):`day_es_ratio_lo(High)`
  - score -2.75(train -2.75 valid -2.58):`day_es_ratio_lo(Close)`
  - score -3.81(train -2.76 valid -3.81):`day_kurt(Ret)`
- `prods2070Pr2b_Nb`:核心 `—`;评分 100,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.95(train -0.95 valid -0.90):`cross_reg_fvalue(day_sum(sub(Close, Vwap)), cs_last_high10(ts_min(ts_med(LogTotalCap, 5), 1), ts_regalpha(ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20), LogFloatCap, 10)), 241)`
  - score -0.98(train -0.84 valid -0.98):`cross_reg_fvalue(day_sum(sub(Close, Vwap)), cs_last_high10(ts_min(ts_med(LogTotalCap, 5), 1), ts_regalpha(day_argmin(Vwap), LogFloatCap, 10)), 241)`
  - score -1.14(train -1.01 valid -1.14):`sub(ts_mean(sub(ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20), ts_mean(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 20)), 20), ts_mean(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 20))`
  - score -1.21(train -1.21 valid -0.90):`cross_reg_fvalue(day_sum(sub(Close, Vwap)), day_std(pow_1_5(Volume)), 241)`
  - score -1.24(train -1.24 valid -0.96):`sub(ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20), ts_mean(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 20))`

## 比原 head 好的拆解变体(R 候选)

(没有)
