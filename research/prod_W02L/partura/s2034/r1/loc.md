# 定位:种子 2034,P 组,第 1 轮(只含 train / valid)

快照:prods2034M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.80 | -0.80 | -0.66 | +1 | 0 | prods2034M1_I0_open_search | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` |
| -1.26 | -1.26 | -0.10 | -1 | 0 | prods2034M1_I0_open_search | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10)), 10)` |
| -1.34 | -1.17 | -1.34 | -1 | 5 | prods2034M1_I0_open_search | `ts_decay_linear(day_sum(Volume), 5)` |

## 共性:23 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.46 | 0.221 | 12 | -2.47 / -2.93 | `day_sum(Amt)` |

## 拆解(20 次评估)

### head score -0.80:`ts_decay_linear(ts_max(day_sum(Amt), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_sum(Amt), 50)` | -0.50 | -0.50 | -0.34 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `ts_max(day_sum(Amt), 50)` | -3.18 | -2.52 | -3.18 | +2.38 | `ts_decay_linear(day_sum(Amt), 50)` |
| swap | `Amt->Volume` | -1.78 | -1.40 | -1.78 | — | `ts_decay_linear(ts_max(day_sum(Volume), 50), 50)` |
| window | `ts_decay_linear@50->25` | -0.34 | -0.34 | -0.20 | — | `ts_decay_linear(ts_max(day_sum(Amt), 50), 25)` |
| window | `ts_decay_linear@50->100` | -1.36 | -1.36 | -0.89 | — | `ts_decay_linear(ts_max(day_sum(Amt), 50), 100)` |

### head score -1.26:`ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10))` | -1.09 | -1.09 | -0.23 | — | (子树本身) |
| sufficiency | `ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10)` | -1.09 | -1.09 | -0.23 | — | (子树本身) |
| sufficiency | `ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50)` | -3.07 | -2.21 | -3.07 | — | (子树本身) |
| sufficiency | `ts_decay_linear(day_sum(Amt), 50)` | -3.18 | -2.52 | -3.18 | — | (子树本身) |
| knockout | `inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10))` | -1.41 | -1.41 | -0.60 | +0.15 | `ts_min(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10), 10)` |
| knockout | `ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10)` | -2.11 | -2.11 | -1.36 | +0.85 | `ts_min(inv(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50)), 10)` |
| knockout | `ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50)` | -0.71 | -0.71 | -0.32 | -0.55 | `ts_min(inv(ts_std(ts_decay_linear(day_sum(Amt), 50), 10)), 10)` |
| swap | `Amt->Volume` | -1.83 | -1.43 | -1.83 | — | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Volume), 50), 50), 10)), 10)` |
| window | `ts_min@10->5` | -1.10 | -1.10 | -0.14 | — | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10)), 5)` |
| window | `ts_min@10->20` | -1.15 | -1.15 | -0.32 | — | `ts_min(inv(ts_std(ts_decay_linear(ts_decay_linear(day_sum(Amt), 50), 50), 10)), 20)` |

### head score -1.34:`ts_decay_linear(day_sum(Volume), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| swap | `Volume->Amt` | -3.61 | -2.69 | -3.61 | — | `ts_decay_linear(day_sum(Amt), 5)` |
| window | `ts_decay_linear@5->2` | -1.40 | -1.16 | -1.40 | — | `ts_decay_linear(day_sum(Volume), 2)` |
| window | `ts_decay_linear@5->10` | -1.54 | -1.22 | -1.54 | — | `ts_decay_linear(day_sum(Volume), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
