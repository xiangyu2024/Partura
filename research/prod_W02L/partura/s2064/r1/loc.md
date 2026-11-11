# 定位:种子 2064,P 组,第 1 轮(只含 train / valid)

快照:prods2064M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.46 | -0.46 | -0.40 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 50)` |
| -0.50 | -0.28 | -0.50 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)), 50)` |
| -0.63 | -0.63 | +0.25 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 241)), 50)` |

## 共性:17 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.49 | 0.006 | 8 | -1.24 / -2.73 | `day_var(pow_2_5(Ret))` |
| -1.35 | 0.986 | 6 | -2.90 / -1.55 | `day_close(pow_2_5(Amt))` |

## 拆解(25 次评估)

### head score -0.46:`ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30))` | -1.21 | -0.76 | -1.21 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)` | -1.21 | -0.76 | -1.21 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(Ret)), 40)` | -1.31 | -1.12 | -1.31 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(Ret))` | -3.10 | -2.51 | -3.10 | — | (子树本身) |
| knockout | `neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30))` | -0.46 | -0.46 | -0.40 | +0.00 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30), 50)` |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)` | -0.38 | -0.24 | -0.38 | -0.09 | `ts_std(neg(ts_sum(day_var(pow_2_5(Ret)), 40)), 50)` |
| knockout | `ts_sum(day_var(pow_2_5(Ret)), 40)` | -0.63 | -0.27 | -0.63 | +0.17 | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 30)), 50)` |
| window | `ts_std@50->25` | -0.35 | -0.35 | -0.18 | — | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 25)` |
| window | `ts_std@50->100` | -0.81 | -0.62 | -0.81 | — | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 100)` |

### head score -0.50:`ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30))` | -1.43 | -0.89 | -1.43 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)` | -1.43 | -0.89 | -1.43 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(Ret)), 10)` | -2.31 | -1.89 | -2.31 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(Ret))` | -3.10 | -2.51 | -3.10 | — | (子树本身) |
| knockout | `neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30))` | -0.52 | -0.28 | -0.52 | +0.03 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30), 50)` |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)` | -0.36 | -0.36 | -0.35 | -0.13 | `ts_std(neg(ts_sum(day_var(pow_2_5(Ret)), 10)), 50)` |
| knockout | `ts_sum(day_var(pow_2_5(Ret)), 10)` | -0.63 | -0.27 | -0.63 | +0.13 | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 30)), 50)` |
| window | `ts_std@50->25` | -1.06 | -0.60 | -1.06 | — | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)), 25)` |
| window | `ts_std@50->100` | -0.62 | -0.62 | -0.30 | — | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)), 100)` |

### head score -0.63:`ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 241)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_sum(day_var(pow_2_5(Ret)), 241))` | -0.16 | -0.16 | +0.21 | — | (子树本身) |
| sufficiency | `cross_sum(day_var(pow_2_5(Ret)), 241)` | -0.16 | -0.16 | +0.21 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(Ret))` | -3.10 | -2.51 | -3.10 | — | (子树本身) |
| knockout | `neg(cross_sum(day_var(pow_2_5(Ret)), 241))` | -0.63 | -0.63 | +0.24 | -0.00 | `ts_std(cross_sum(day_var(pow_2_5(Ret)), 241), 50)` |
| knockout | `cross_sum(day_var(pow_2_5(Ret)), 241)` | -0.79 | -0.61 | -0.79 | +0.16 | `ts_std(neg(day_var(pow_2_5(Ret))), 50)` |
| window | `ts_std@50->25` | -0.89 | -0.89 | -0.03 | — | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 241)), 25)` |
| window | `ts_std@50->100` | -1.01 | -1.01 | +0.18 | — | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 241)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_var(pow_2_5(Ret))` — enrichment,均值差 +1.49,p 0.006

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(knockout cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)):`ts_std(neg(ts_sum(day_var(pow_2_5(Ret)), 10)), 50)`
- 增益 +0.11(window ts_std@50->25):`ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 25)`
