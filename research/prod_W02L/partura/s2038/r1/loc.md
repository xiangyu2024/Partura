# 定位:种子 2038,P 组,第 1 轮(只含 train / valid)

快照:prods2038M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.43 | +0.11 | -0.43 | +1 | 0 | prods2038M1_I0_open_search | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 50)` |
| -1.14 | -1.14 | -1.03 | -1 | 5 | prods2038M1_I0_open_search | `ts_decay_linear(day_open(Volume), 5)` |
| -1.30 | -1.30 | -0.82 | +1 | 20 | prods2038M1_I0_open_search | `signedpower(day_open(Amt))` |

## 共性:24 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.87 | 0.001 | 5 | -1.32 / -3.19 | `day_open(Amt)` |
| -0.43 | 0.900 | 4 | -3.16 / -2.73 | `day_open(Low)` |
| -1.53 | 0.975 | 8 | -3.82 / -2.29 | `day_open(High)` |

## 拆解(16 次评估)

### head score -0.43:`ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20)` | -1.06 | -0.80 | -1.06 | — | (子树本身) |
| sufficiency | `log(cross_regbeta(day_last(Amt), day_open(Amt), 10))` | -0.87 | -0.80 | -0.87 | — | (子树本身) |
| sufficiency | `cross_regbeta(day_last(Amt), day_open(Amt), 10)` | -0.83 | -0.83 | -0.76 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| knockout | `ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20)` | -0.42 | +0.05 | -0.42 | -0.02 | `ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 50)` |
| knockout | `log(cross_regbeta(day_last(Amt), day_open(Amt), 10))` | -0.73 | +0.29 | -0.73 | +0.30 | `ts_max(ts_max(cross_regbeta(day_last(Amt), day_open(Amt), 10), 20), 50)` |
| knockout | `cross_regbeta(day_last(Amt), day_open(Amt), 10)` | -0.43 | -0.43 | -0.28 | +0.00 | `ts_max(ts_max(log(day_last(Amt)), 20), 50)` |
| swap | `Amt->Volume` | -0.50 | +0.08 | -0.50 | — | `ts_max(ts_max(log(cross_regbeta(day_last(Volume), day_open(Volume), 10)), 20), 50)` |
| window | `ts_max@50->25` | -0.59 | -0.15 | -0.59 | — | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 25)` |
| window | `ts_max@50->100` | -0.53 | +0.38 | -0.53 | — | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 100)` |

### head score -1.14:`ts_decay_linear(day_open(Volume), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_open(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.51 | -1.51 | -0.81 | — | `ts_decay_linear(day_open(Amt), 5)` |
| window | `ts_decay_linear@5->2` | -1.18 | -1.18 | -1.17 | — | `ts_decay_linear(day_open(Volume), 2)` |
| window | `ts_decay_linear@5->10` | -1.24 | -1.19 | -1.24 | — | `ts_decay_linear(day_open(Volume), 10)` |

### head score -1.30:`signedpower(day_open(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_open(Amt)` | -1.30 | -1.30 | -0.79 | — | (子树本身) |
| swap | `Amt->Volume` | — | — | — | — | `signedpower(day_open(Volume))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_open(Amt)` — enrichment,均值差 +1.87,p 0.001

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
