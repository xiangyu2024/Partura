# 定位:种子 2041,P 组,第 1 轮(只含 train / valid)

快照:prods2041M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.51 | -1.38 | -1.51 | -1 | 20 | prods2041M1_I0_open_search | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Volume, create_like(in_slice(Close, 1, 1), 0)))` |
| -1.73 | -1.72 | -1.73 | -1 | 20 | prods2041M1_I0_open_search | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))` |
| -1.80 | -1.44 | -1.80 | -1 | 20 | prods2041M1_I0_open_search | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))` |

## 共性:26 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.55 | 0.874 | 4 | -4.10 / -3.54 | `add(day_sum(Amt), create_like(in_slice(Close, 1, 1), 1e-05))` |
| -0.55 | 0.874 | 4 | -4.10 / -3.54 | `day_sum(Amt)` |
| -0.69 | 0.962 | 12 | -4.00 / -3.31 | `create_like(in_slice(Close, 1, 1), 1e-05)` |
| -0.71 | 0.973 | 6 | -4.18 / -3.47 | `day_sum(Volume)` |
| -0.71 | 0.973 | 6 | -4.18 / -3.47 | `add(day_sum(Volume), create_like(in_slice(Close, 1, 1), 1e-05))` |

## 拆解(18 次评估)

### head score -1.51:`day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Volume, create_like(in_slice(Close, 1, 1), 0)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_like(in_slice(Close, 1, 1), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `in_slice(Close, 1, 1)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -1.54 | -1.39 | -1.54 | +0.03 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Volume, in_slice(Close, 1, 1)))` |
| swap | `Close->Vwap` | -1.44 | -1.44 | -1.26 | — | `day_mean(select_where(eq(in_roll_labels(Vwap, 241), 0), Volume, create_like(in_slice(Vwap, 1, 1), 0)))` |
| swap | `Volume->Amt` | -3.96 | -3.96 | -3.88 | — | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Amt, create_like(in_slice(Close, 1, 1), 0)))` |

### head score -1.73:`mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0)))` | -2.49 | -2.49 | -2.49 | — | (子树本身) |
| sufficiency | `day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))` | -1.63 | -1.46 | -1.63 | — | (子树本身) |
| sufficiency | `create_like(in_slice(Close, 1, 1), 0)` | — | — | — | — | 门槛废品 |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -1.79 | -1.76 | -1.79 | +0.06 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, in_slice(Close, 1, 1))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))` |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -1.59 | -0.87 | -1.59 | -0.14 | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), in_slice(Close, 1, 1))))` |
| swap | `Close->Vwap` | -1.56 | -1.56 | -0.86 | — | `mul(day_sum(select_where(eq(in_roll_labels(Vwap, 120), 4), Volume, create_like(in_slice(Vwap, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Vwap, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Vwap, 1, 1), 0))))` |
| swap | `Volume->Amt` | -3.92 | -3.92 | -3.41 | — | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Amt, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))` |
| window | `in_shift@1->2` | -1.70 | -1.65 | -1.70 | — | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 2), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))` |

### head score -1.80:`day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_like(in_slice(Close, 1, 1), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `in_slice(Close, 1, 1)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `create_like(in_slice(Close, 1, 1), 0)` | -1.84 | -1.51 | -1.84 | +0.04 | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, in_slice(Close, 1, 1)))` |
| swap | `Close->Vwap` | -1.44 | -1.38 | -1.44 | — | `day_mean(select_where(eq(in_roll_labels(Vwap, 241), 4), Volume, create_like(in_slice(Vwap, 1, 1), 0)))` |
| swap | `Volume->Amt` | -4.13 | -3.68 | -4.13 | — | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Amt, create_like(in_slice(Close, 1, 1), 0)))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.17(swap Close->Vwap):`mul(day_sum(select_where(eq(in_roll_labels(Vwap, 120), 4), Volume, create_like(in_slice(Vwap, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Vwap, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Vwap, 1, 1), 0))))`
