# 定位:种子 2017,P 组,第 3 轮(只含 train / valid)

快照:prods2017M1_I0_open_search, prods2017M2_I0_open_search, prods2017M3_I0_open_search, prods2017Pr1a_Ea, prods2017Pr1b_Nb, prods2017Pr2a_Ea, prods2017Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.17 | +1.05 | +0.17 | +1 | 5 | prods2017M2_I0_open_search | `ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)` |
| +0.00 | +0.00 | +0.49 | +1 | 0 | prods2017M1_I0_open_search | `signedpower(cs_mask_top_replace_mean_neg(pow_2(day_quantile(Vwap))))` |
| -0.79 | -0.79 | -0.71 | +1 | 20 | prods2017M2_I0_open_search | `div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)))` |
| -0.86 | -0.86 | -0.76 | +1 | 20 | prods2017M2_I0_open_search | `rank(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), create_valid_mask(abs_(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)))), 0), True)` |
| -1.19 | -1.02 | -1.19 | -1 | 20 | prods2017M1_I0_open_search | `cs_rank(day_quantile(Ret))` |
| -1.31 | -1.13 | -1.31 | -1 | 20 | prods2017M1_I0_open_search | `pow_2(cs_rank(cs_normalize(day_quantile(Ret))))` |
| -1.97 | -1.78 | -1.97 | -1 | 20 | prods2017M3_I0_open_search | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| -2.36 | -1.74 | -2.36 | -1 | 20 | prods2017M3_I0_open_search | `div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| -2.89 | -2.89 | -1.71 | +1 | 20 | prods2017M3_I0_open_search | `rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0), True)` |

## 共性:203 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.09 | 0.000 | 4 | -0.30 / -2.39 | `cs_normalize(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60)))` |
| +1.46 | 0.000 | 11 | -0.97 / -2.43 | `cs_normalize(cross_zscore(day_quantile_q25(Volume), 60))` |
| +1.36 | 0.000 | 14 | -1.08 / -2.44 | `cross_zscore(day_quantile_q25(Volume), 60)` |
| +1.01 | 0.000 | 20 | -1.44 / -2.45 | `day_quantile_q25(Volume)` |
| +1.00 | 0.000 | 15 | -1.42 / -2.42 | `day_last(Volume)` |
| +0.84 | 0.026 | 5 | -1.53 / -2.37 | `cs_rank(cross_delta(sub(log(add(day_quantile(Amt), 1)), LogFloatCap), 120))` |
| +0.76 | 0.065 | 4 | -1.60 / -2.37 | `cross_delta(day_quantile(Amt), 120)` |
| +0.65 | 0.007 | 17 | -1.76 / -2.40 | `cs_rank(cross_delta(log(day_quantile(Close)), 120))` |
| +0.64 | 0.017 | 13 | -1.75 / -2.39 | `cs_demean(cs_rank(cross_delta(log(day_quantile(Close)), 120)))` |
| +0.53 | 0.183 | 4 | -1.83 / -2.36 | `day_min(add(Ret, day_quantile(Vwap)))` |
| +0.46 | 0.018 | 40 | -1.98 / -2.44 | `cross_delta(log(day_quantile(Close)), 120)` |
| +0.42 | 0.218 | 4 | -1.94 / -2.36 | `day_sum(cross_reg_tvalue(High, Volume, 3))` |
| +0.40 | 0.238 | 7 | -1.96 / -2.36 | `cross_mean(log(day_quantile(Close)), 60)` |
| +0.37 | 0.281 | 4 | -1.99 / -2.36 | `day_median(Close)` |
| +0.28 | 0.377 | 5 | -2.08 / -2.36 | `day_quantile(Open)` |
| +0.28 | 0.025 | 29 | -2.11 / -2.39 | `day_quantile(Amt)` |
| +0.22 | 0.237 | 62 | -2.20 / -2.42 | `log(day_quantile(Close))` |
| +0.16 | 0.383 | 78 | -2.25 / -2.41 | `day_quantile(Close)` |
| +0.09 | 0.596 | 14 | -2.27 / -2.36 | `cross_delta(log(day_quantile(Close)), 60)` |
| +0.06 | 0.397 | 4 | -2.29 / -2.35 | `day_quantile(Volume)` |

## 拆解(41 次评估)

### head score +0.17:`ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)))` | -0.79 | -0.79 | -0.66 | — | (子树本身) |
| sufficiency | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06)))` | -3.49 | -3.46 | -3.49 | — | (子树本身) |
| sufficiency | `day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0)))` | -1.94 | -1.61 | -1.94 | — | (子树本身) |
| sufficiency | `add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))` | — | — | — | — | 门槛废品 |
| knockout | `div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)))` | -2.35 | -2.35 | -2.06 | +2.51 | `ts_mean(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)` |
| knockout | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06)))` | +0.48 | +0.74 | +0.48 | -0.32 | `ts_mean(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)` |
| knockout | `add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))` | +0.18 | +1.03 | +0.18 | -0.02 | `ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)` |
| knockout | `is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))` | -1.82 | -1.82 | -1.47 | +1.99 | `ts_mean(div(div(day_sum(select_where(day_quantile(Ret, 0.95), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)` |
| swap | `Close->Vwap` | +0.12 | +0.79 | +0.12 | — | `ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.95)), sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), create_like(Vwap, 0))), add(day_sum(is_gt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)` |
| window | `ts_mean@120->60` | -0.11 | +0.53 | -0.11 | — | `ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 60)` |
| window | `ts_mean@120->240` | +0.48 | +0.94 | +0.48 | — | `ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 240)` |

### head score -1.97:`div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0)))` | -1.58 | -1.43 | -1.58 | — | (子树本身) |
| sufficiency | `add(day_sum(Volume), create_like(day_sum(Volume), 1e-06))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `create_like(day_sum(Volume), 1e-06)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile(Ret, 0.95)` | -2.93 | -2.93 | -2.79 | — | (子树本身) |
| knockout | `is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))` | -2.95 | -2.95 | -2.19 | +0.98 | `div(day_sum(select_where(day_quantile(Ret, 0.95), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| knockout | `add(day_sum(Volume), create_like(day_sum(Volume), 1e-06))` | -1.92 | -1.78 | -1.92 | -0.05 | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), day_sum(Volume))` |
| knockout | `create_like(day_sum(Volume), 1e-06)` | -1.92 | -1.78 | -1.92 | -0.05 | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), add(day_sum(Volume), day_sum(Volume)))` |
| swap | `Close->Vwap` | -2.09 | -2.09 | -0.25 | — | `div(day_sum(select_where(is_gt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), Volume), create_like(Vwap, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| swap | `Volume->Amt` | -1.91 | -1.77 | -1.91 | — | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Amt), create_like(Close, 0))), add(day_sum(Amt), create_like(day_sum(Amt), 1e-06)))` |
| window | `in_delay@5->2` | -2.24 | -2.06 | -2.24 | — | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 2)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| window | `in_delay@5->10` | -2.04 | -1.91 | -2.04 | — | `div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 10)), create_like(Close, 1)), day_quantile(Ret, 0.95)), mul(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |

### head score -2.36:`div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0)))` | -1.54 | -1.45 | -1.54 | — | (子树本身) |
| sufficiency | `add(day_sum(Volume), create_like(day_sum(Volume), 1e-06))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `create_like(day_sum(Volume), 1e-06)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile(Ret, 0.05)` | -3.11 | -3.11 | -2.98 | — | (子树本身) |
| knockout | `is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))` | -2.39 | -2.00 | -2.39 | +0.03 | `div(day_sum(select_where(day_quantile(Ret, 0.05), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| knockout | `add(day_sum(Volume), create_like(day_sum(Volume), 1e-06))` | -2.32 | -1.74 | -2.32 | -0.04 | `div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), day_sum(Volume))` |
| knockout | `create_like(day_sum(Volume), 1e-06)` | -2.32 | -1.74 | -2.32 | -0.04 | `div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), add(day_sum(Volume), day_sum(Volume)))` |
| swap | `Close->Vwap` | -1.77 | -1.77 | -0.61 | — | `div(day_sum(select_where(is_lt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1))), Volume), create_like(Vwap, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| swap | `Volume->Amt` | -2.32 | -1.75 | -2.32 | — | `div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Amt), create_like(Close, 0))), add(day_sum(Amt), create_like(day_sum(Amt), 1e-06)))` |
| window | `in_delay@5->2` | -2.31 | -2.12 | -2.31 | — | `div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 2)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |
| window | `in_delay@5->10` | -2.34 | -1.81 | -2.34 | — | `div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 10)), create_like(Close, 1)), day_quantile(Ret, 0.05)), mul(abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), Volume), create_like(Close, 0))), add(day_sum(Volume), create_like(day_sum(Volume), 1e-06)))` |

### head score -2.89:`rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0), True)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))` | — | — | — | — | 门槛废品 |
| knockout | `create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0)` | -2.89 | -2.89 | -1.76 | +0.00 | `rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), True)` |
| knockout | `abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))))` | -2.89 | -2.89 | -1.76 | +0.00 | `rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_valid_mask(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), 0), True)` |
| swap | `Close->Vwap` | -1.43 | -1.43 | -1.11 | — | `rank(day_mean(is_lt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.05)))), 0), True)` |
| window | `in_delay@5->2` | -3.89 | -3.89 | -3.04 | — | `rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 2)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0), True)` |
| window | `in_delay@5->10` | -2.25 | -2.25 | -1.21 | — | `rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 10)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0), True)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_normalize(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60)))` — enrichment,均值差 +2.09,p 0.000
2. `cs_normalize(cross_zscore(day_quantile_q25(Volume), 60))` — enrichment,均值差 +1.46,p 0.000
3. `cross_zscore(day_quantile_q25(Volume), 60)` — enrichment,均值差 +1.36,p 0.000
4. `day_quantile_q25(Volume)` — enrichment,均值差 +1.01,p 0.000
5. `day_last(Volume)` — enrichment,均值差 +1.00,p 0.000
6. `cs_rank(cross_delta(sub(log(add(day_quantile(Amt), 1)), LogFloatCap), 120))` — enrichment,均值差 +0.84,p 0.026
7. `cross_delta(day_quantile(Amt), 120)` — enrichment,均值差 +0.76,p 0.065
8. `cs_rank(cross_delta(log(day_quantile(Close)), 120))` — enrichment,均值差 +0.65,p 0.007
9. `cs_demean(cs_rank(cross_delta(log(day_quantile(Close)), 120)))` — enrichment,均值差 +0.64,p 0.017
10. `cross_delta(log(day_quantile(Close)), 120)` — enrichment,均值差 +0.46,p 0.018
11. `day_quantile(Amt)` — enrichment,均值差 +0.28,p 0.025

## 本组之前各轮的任务

- `prods2017Pr1a_Ea`:核心 `day_quantile(Close)`;评分 103,过线 0,入 heads 0;采样计数 {'c05_no_core': 2239, 'c05_skeleton': 992}
  - score -1.11(train -0.63 valid -1.11):`cs_flip_by_state(cross_delta(log(day_quantile(Close)), 120), cross_mean(log(day_quantile(Close)), 60))`
  - score -1.26(train -1.05 valid -1.26):`cs_flip_by_state(cross_delta(log(day_quantile(Close)), 120), log(day_quantile(Close)))`
  - score -1.32(train -1.32 valid -1.31):`cs_flip_by_state(cross_delta(pow_05(day_quantile(Close)), 120), log(day_quantile(Open)))`
  - score -1.40(train -1.40 valid -1.36):`cs_flip_by_state(cross_delta(day_quantile(Close), 120), log(day_quantile(Close)))`
  - score -1.51(train -1.16 valid -1.51):`cs_flip_by_state(cross_delta(log(day_quantile(Close)), 120), day_min(add(Ret, day_quantile(Vwap))))`
- `prods2017Pr1b_Nb`:核心 `—`;评分 94,过线 0,入 heads 0;采样计数 {'c05_skeleton': 16}
  - score -0.61(train -0.61 valid +0.03):`cross_zscore(sub(log(add(day_quantile(Close), 1)), LogFloatCap), 120)`
  - score -0.73(train -0.65 valid -0.73):`cross_corr(ts_decay_linear(cs_demean(LogFloatCap), 5), day_last(Volume), 60)`
  - score -1.06(train -1.06 valid -0.42):`cross_corr(ts_decay_linear(cs_demean(cs_rank(cross_delta(pow_1_5(day_quantile(Close)), 120))), 5), day_last(Volume), 60)`
  - score -1.12(train -1.12 valid -0.78):`cross_corr(day_quantile(Amt), day_last(Volume), 60)`
  - score -1.16(train -1.16 valid -0.39):`cross_corr(day_median(Amt), day_last(Volume), 15)`
- `prods2017Pr2a_Ea`:核心 `div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)))`;评分 60,过线 0,入 heads 0;采样计数 {'c05_no_core': 5914, 'c05_skeleton': 3247}
  - score -1.22(train -1.10 valid -1.22):`day_distinct_ratio(High)`
  - score -2.36(train -2.36 valid -2.21):`day_q_stat_std(Volume)`
  - score -2.61(train -2.61 valid -1.01):`day_centroid(Vwap)`
  - score -2.68(train -2.42 valid -2.68):`day_es_ratio_hi(Open)`
  - score -2.73(train -2.73 valid -2.68):`day_es_ratio_lo(High)`
- `prods2017Pr2b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.08(train -0.08 valid +0.15):`cross_semistd_pos(cs_normalize(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60))), 241)`
  - score -0.34(train -0.34 valid -0.34):`cross_quantile_q25(cs_normalize(cross_semistd_pos(cs_normalize(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60))), 60)), 60)`
  - score -0.39(train -0.39 valid -0.39):`cross_semistd_pos(cs_normalize(cs_normalize(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60)))), 60)`
  - score -0.39(train -0.39 valid -0.38):`cross_semistd_pos(cs_normalize(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60))), 60)`
  - score -0.39(train -0.39 valid -0.38):`cross_semistd_pos(cs_normalize(cross_zscore(day_quantile_q25(Volume), 60)), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.46(swap Close->Vwap):`rank(day_mean(is_lt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Vwap, in_delay(Vwap, 5)), create_like(Vwap, 1)), day_quantile(Ret, 0.05)))), 0), True)`
- 增益 +0.64(window in_delay@5->10):`rank(day_mean(is_lt(sub(div(Close, in_delay(Close, 10)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_valid_mask(abs_(day_mean(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)))), 0), True)`
- 增益 +0.32(knockout div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06)))):`ts_mean(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 120)`
- 增益 +0.31(window ts_mean@120->240):`ts_mean(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), 240)`
