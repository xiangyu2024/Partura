# 定位:种子 2040,P 组,第 3 轮(只含 train / valid)

快照:prods2040M1_I0_open_search, prods2040M2_I0_open_search, prods2040M3_I0_open_search, prods2040Pr1a_Ea, prods2040Pr1b_Nb, prods2040Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.28 | -1.28 | -1.22 | -1 | 5 | prods2040M2_I0_open_search | `ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 120)` |
| -1.38 | -1.38 | -1.07 | -1 | 20 | prods2040M3_I0_open_search | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 20))` |
| -1.47 | -1.47 | -0.90 | +1 | 20 | prods2040M1_I0_open_search | `day_first(log(Amt))` |
| -1.49 | -1.43 | -1.49 | -1 | 20 | prods2040M1_I0_open_search | `day_mean(log(Volume))` |
| -1.56 | -1.56 | -1.52 | +1 | 5 | prods2040M2_I0_open_search | `ts_stddev(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))))), 20)` |
| -1.59 | -1.59 | -1.41 | +1 | 20 | prods2040M1_I0_open_search | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` |
| -2.40 | -2.40 | -1.47 | +1 | 20 | prods2040M2_I0_open_search | `ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))))), 20)` |
| -3.14 | -2.71 | -3.14 | +1 | 20 | prods2040M3_I0_open_search | `mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))` |
| -3.20 | -3.20 | -2.34 | -1 | 20 | prods2040M3_I0_open_search | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 20))` |

## 共性:180 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.71 | 0.002 | 5 | -0.57 / -2.28 | `cs_bucket_demean(day_std(Ret), day_cov(Low, log(Amt)))` |
| +1.16 | 0.000 | 69 | -1.52 / -2.68 | `day_std(Ret)` |
| +1.07 | 0.021 | 6 | -1.20 / -2.27 | `mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 20)))` |
| +0.99 | 0.005 | 11 | -1.30 / -2.29 | `cross_mean(day_std(Ret), 20)` |
| +0.94 | 0.012 | 10 | -1.35 / -2.29 | `is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))` |
| +0.86 | 0.025 | 9 | -1.41 / -2.28 | `day_cov(Low, log(Amt))` |
| +0.83 | 0.198 | 4 | -1.42 / -2.25 | `day_signed_ratio(Low, Ret)` |
| +0.78 | 0.071 | 6 | -1.48 / -2.26 | `cs_bucket_demean(day_std(Ret), day_cov(Low, Amt))` |
| +0.73 | 0.151 | 4 | -1.52 / -2.25 | `cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))), 60)` |
| +0.57 | 0.190 | 5 | -1.68 / -2.25 | `day_std(in_logchg(in_logchg(Volume, 1), 15))` |
| +0.53 | 0.090 | 14 | -1.74 / -2.27 | `day_cov(Low, Amt)` |
| +0.48 | 0.138 | 18 | -1.80 / -2.28 | `day_std(in_logchg(Volume, 1))` |
| +0.48 | 0.004 | 41 | -1.86 / -2.34 | `day_cov(Ret, log(Amt))` |
| +0.17 | 0.518 | 9 | -2.07 / -2.24 | `day_first(log(Amt))` |
| +0.14 | 0.518 | 8 | -2.10 / -2.24 | `log(day_last(Close))` |
| +0.08 | 0.592 | 8 | -2.16 / -2.24 | `day_mean(log(Amt))` |
| -0.01 | 0.679 | 7 | -2.24 / -2.23 | `day_std(in_logchg(Volume, 15))` |
| -0.27 | 0.636 | 7 | -2.49 / -2.22 | `day_std(Low)` |
| -0.31 | 0.878 | 14 | -2.52 / -2.21 | `day_last(Close)` |
| -0.58 | 0.920 | 8 | -2.78 / -2.21 | `day_first(Open)` |

## 拆解(38 次评估)

### head score -1.28:`ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))` | — | — | — | — | 门槛废品 |
| sufficiency | `div(day_last(Close), day_first(Open))` | -4.39 | -4.39 | -3.61 | — | (子树本身) |
| knockout | `mul(sub(div(day_last(Close), day_first(Open)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))))` | — | — | — | — | `ts_mean(add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))), 120)` |
| knockout | `add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))` | -1.31 | -1.31 | -1.24 | +0.03 | `ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))))), 120)` |
| knockout | `sub(div(day_last(Close), day_first(Open)), 1)` | -1.15 | -1.15 | -0.32 | -0.14 | `ts_mean(mul(div(day_last(Close), day_first(Open)), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 120)` |
| knockout | `div(day_last(Close), day_first(Open))` | -2.27 | -1.54 | -2.27 | +0.98 | `ts_mean(mul(sub(day_last(Close), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 120)` |
| swap | `Close->Vwap` | -1.30 | -1.30 | -1.20 | — | `ts_mean(mul(sub(div(day_last(Vwap), day_first(Open)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 120)` |
| swap | `Open->Close` | -1.30 | -1.30 | -1.22 | — | `ts_mean(mul(sub(div(day_last(Close), day_first(Close)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 120)` |
| window | `ts_mean@120->60` | -1.47 | -1.47 | -1.39 | — | `ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 60)` |
| window | `ts_mean@120->240` | -0.93 | -0.93 | -0.07 | — | `ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), add(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))), day_sum(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume))))))))), 240)` |

### head score -1.38:`day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_like(in_slice(Close, 1, 1), 1)` | — | — | — | — | 门槛废品 |
| sufficiency | `create_like(in_slice(Close, 1, 1), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `in_slice(Close, 1, 1)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `create_like(in_slice(Close, 1, 1), 1)` | -2.31 | -1.55 | -2.31 | +0.94 | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), in_slice(Close, 1, 1), create_like(in_slice(Close, 1, 1), 0)), 20))` |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -2.37 | -1.59 | -2.37 | +1.00 | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), in_slice(Close, 1, 1)), 20))` |
| swap | `Close->Vwap` | -1.61 | -1.61 | -0.10 | — | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Vwap, 241), 4), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0)), 20))` |
| window | `cross_decay_linear@20->10` | — | — | — | — | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 10))` |
| window | `cross_decay_linear@20->40` | -1.26 | -1.26 | -1.25 | — | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 40))` |

### head score -3.14:`mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))` | — | — | — | — | 门槛废品 |
| sufficiency | `create_like(in_slice(Close, 1, 1), 1)` | — | — | — | — | 门槛废品 |
| knockout | `add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))))` | -3.29 | -3.29 | -3.25 | +0.15 | `mul(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(in_shift(Ret, 1)))` |
| knockout | `create_like(in_slice(Close, 1, 1), 1)` | -2.29 | -1.61 | -2.29 | -0.84 | `mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), in_slice(Close, 1, 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))` |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -2.37 | -1.62 | -2.37 | -0.77 | `mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), in_slice(Close, 1, 1))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))` |
| knockout | `create_like(in_slice(Close, 1, 1), 1)` | -2.35 | -1.54 | -2.35 | -0.79 | `mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), in_slice(Close, 1, 1), create_like(in_slice(Close, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))` |
| swap | `Close->Vwap` | -2.11 | -2.11 | -0.58 | — | `mul(add(day_mean(select_where(eq(in_roll_labels(Vwap, 241), 4), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Vwap, 241), 0), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))` |
| window | `in_shift@1->2` | -3.23 | -2.83 | -3.23 | — | `mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)))), day_mean(in_shift(Ret, 2)))` |

### head score -3.20:`day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_like(in_slice(Close, 1, 1), 1)` | — | — | — | — | 门槛废品 |
| sufficiency | `create_like(in_slice(Close, 1, 1), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `in_slice(Close, 1, 1)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `create_like(in_slice(Close, 1, 1), 1)` | -2.42 | -1.61 | -2.42 | -0.77 | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), in_slice(Close, 1, 1), create_like(in_slice(Close, 1, 1), 0)), 20))` |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -2.36 | -1.57 | -2.36 | -0.84 | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), create_like(in_slice(Close, 1, 1), 1), in_slice(Close, 1, 1)), 20))` |
| swap | `Close->Vwap` | -2.42 | -2.42 | -1.04 | — | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Vwap, 120), 4), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0)), 20))` |
| window | `cross_decay_linear@20->10` | -3.55 | -3.55 | -2.73 | — | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 10))` |
| window | `cross_decay_linear@20->40` | -2.70 | -2.70 | -1.99 | — | `day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_bucket_demean(day_std(Ret), day_cov(Low, log(Amt)))` — enrichment,均值差 +1.71,p 0.002
2. `day_std(Ret)` — enrichment,均值差 +1.16,p 0.000
3. `mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 20)))` — enrichment,均值差 +1.07,p 0.021
4. `cross_mean(day_std(Ret), 20)` — enrichment,均值差 +0.99,p 0.005
5. `is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))` — enrichment,均值差 +0.94,p 0.012
6. `day_cov(Low, log(Amt))` — enrichment,均值差 +0.86,p 0.025
7. `cs_bucket_demean(day_std(Ret), day_cov(Low, Amt))` — enrichment,均值差 +0.78,p 0.071
8. `day_cov(Low, Amt)` — enrichment,均值差 +0.53,p 0.090
9. `day_cov(Ret, log(Amt))` — enrichment,均值差 +0.48,p 0.004

## 本组之前各轮的任务

- `prods2040Pr1a_Ea`:核心 `day_cov(Ret, log(Amt))`;评分 75,过线 0,入 heads 0;采样计数 {'c05_no_core': 1048, 'c05_skeleton': 549, 'c05_periphery_seen': 3}
  - score -0.45(train -0.45 valid -0.18):`cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))), 60)`
  - score -0.45(train -0.45 valid -0.18):`cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(is_gt(day_std(Ret), cross_mean(day_std(Ret), 20)), cross_mean(day_std(Ret), 20))), 60)`
  - score -0.55(train -0.55 valid -0.27):`cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 241))), 60)`
  - score -0.58(train -0.58 valid -0.10):`cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), day_cov(Ret, log(Amt)))), 60)`
  - score -0.60(train -0.60 valid -0.11):`cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))), 60))), 60)`
- `prods2040Pr1b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score +0.26(train +0.26 valid +0.58):`cross_autocorr_s1(cs_bucket_demean(day_std(Ret), day_signed_ratio(Low, Ret)), 241)`
  - score +0.21(train +0.21 valid +0.95):`cross_autocorr_s1(cs_bucket_demean(day_std(Ret), day_signed_ratio(Ret, Ret)), 241)`
  - score +0.18(train +0.18 valid +0.53):`cross_autocorr_s1(cs_bucket_demean(cs_bucket_demean(day_std(Ret), day_std(Ret)), day_std(Ret)), 241)`
  - score +0.14(train +0.14 valid +0.16):`cross_autocorr_s1(cs_bucket_demean(day_std(Ret), day_cov(Low, Low)), 241)`
  - score +0.13(train +0.29 valid +0.13):`cross_autocorr_s1(cs_bucket_demean(day_std(Ret), cs_normalize(BoardCode)), 241)`
- `prods2040Pr2b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.47(train -0.15 valid -0.47):`cross_regbeta(day_std(in_logchg(Volume, 1)), cross_regbeta(cross_regbeta(day_std(in_logchg(Volume, 1)), day_std(Ret), 120), day_std(Ret), 120), 241)`
  - score -0.48(train +0.16 valid -0.48):`cross_regbeta(day_std(in_logchg(Volume, 1)), day_std(Ret), 241)`
  - score -0.78(train -0.78 valid +0.16):`cross_regbeta(day_std(Low), day_gini(Volume), 120)`
  - score -1.01(train -0.63 valid -1.01):`cross_regbeta(cross_regbeta(day_std(in_logchg(Volume, 1)), day_std(Ret), 241), day_std(Ret), 241)`
  - score -1.06(train -1.06 valid -0.91):`cross_regbeta(day_std(in_logchg(in_logchg(Volume, 1), 15)), day_std(in_logchg(Volume, 1)), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.03(swap Close->Vwap):`mul(add(day_mean(select_where(eq(in_roll_labels(Vwap, 241), 4), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0))), day_mean(select_where(eq(in_roll_labels(Vwap, 241), 0), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0)))), day_mean(in_shift(Ret, 1)))`
- 增益 +0.77(swap Close->Vwap):`day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Vwap, 120), 4), create_like(in_slice(Vwap, 1, 1), 1), create_like(in_slice(Vwap, 1, 1), 0)), 20))`
- 增益 +0.49(window cross_decay_linear@20->40):`day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 120), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 40))`
- 增益 +0.12(window cross_decay_linear@20->40):`day_mean(cross_decay_linear(select_where(eq(in_roll_labels(Close, 241), 4), create_like(in_slice(Close, 1, 1), 1), create_like(in_slice(Close, 1, 1), 0)), 40))`
