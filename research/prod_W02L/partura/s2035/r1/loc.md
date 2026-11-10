# 定位:种子 2035,P 组,第 1 轮(只含 train / valid)

快照:prods2035M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.34 | -1.19 | -1.34 | +1 | 5 | prods2035M1_I0_open_search | `inv(day_sum(Volume))` |
| -1.52 | -1.24 | -1.52 | -1 | 5 | prods2035M1_I0_open_search | `ts_max(ts_max(inv(inv(day_sum(Volume))), 10), 10)` |
| -1.67 | -1.45 | -1.67 | -1 | 5 | prods2035M1_I0_open_search | `inv(ts_max(inv(day_sum(Volume)), 10))` |

## 共性:8 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -1.45 | 1.000 | 5 | -2.96 / -1.51 | `day_sum(Amt)` |
| -1.45 | 1.000 | 5 | -2.96 / -1.51 | `inv(day_sum(Amt))` |

## 拆解(18 次评估)

### head score -1.34:`inv(day_sum(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| swap | `Volume->Amt` | -3.47 | -2.76 | -3.47 | — | `inv(day_sum(Amt))` |

### head score -1.52:`ts_max(ts_max(inv(inv(day_sum(Volume))), 10), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(inv(inv(day_sum(Volume))), 10)` | -1.43 | -1.24 | -1.43 | — | (子树本身) |
| sufficiency | `inv(inv(day_sum(Volume)))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `inv(day_sum(Volume))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `inv(inv(day_sum(Volume)))` | -1.79 | -1.63 | -1.79 | +0.27 | `ts_max(ts_max(inv(day_sum(Volume)), 10), 10)` |
| swap | `Volume->Amt` | -2.25 | -2.25 | -0.87 | — | `ts_max(ts_max(inv(inv(day_sum(Amt))), 10), 10)` |
| window | `ts_max@10->5` | -1.46 | -1.27 | -1.46 | — | `ts_max(ts_max(inv(inv(day_sum(Volume))), 10), 5)` |
| window | `ts_max@10->20` | -1.49 | -1.22 | -1.49 | — | `ts_max(ts_max(inv(inv(day_sum(Volume))), 10), 20)` |

### head score -1.67:`inv(ts_max(inv(day_sum(Volume)), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(inv(day_sum(Volume)), 10)` | -1.73 | -1.45 | -1.73 | — | (子树本身) |
| sufficiency | `inv(day_sum(Volume))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `ts_max(inv(day_sum(Volume)), 10)` | -1.40 | -1.19 | -1.40 | -0.27 | `inv(inv(day_sum(Volume)))` |
| knockout | `inv(day_sum(Volume))` | -1.43 | -1.24 | -1.43 | -0.24 | `inv(ts_max(day_sum(Volume), 10))` |
| swap | `Volume->Amt` | -4.10 | -2.93 | -4.10 | — | `inv(ts_max(inv(day_sum(Amt)), 10))` |
| window | `ts_max@10->5` | -1.70 | -1.36 | -1.70 | — | `inv(ts_max(inv(day_sum(Volume)), 5))` |
| window | `ts_max@10->20` | -1.77 | -1.66 | -1.77 | — | `inv(ts_max(inv(day_sum(Volume)), 20))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
