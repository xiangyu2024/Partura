# 定位:种子 2032,P 组,第 1 轮(只含 train / valid)

快照:prods2032M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.12 | -1.12 | -1.12 | -1 | 0 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 60)` |
| -1.15 | -1.15 | -1.09 | -1 | 5 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 5)` |
| -1.20 | -1.20 | -1.03 | -1 | 5 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 3)` |

## 共性:7 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.21 | 0.029 | 4 | -1.17 / -2.38 | `day_first(Volume)` |

## 拆解(12 次评估)

### head score -1.12:`cross_sum(day_first(Volume), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -0.14 | -0.02 | -0.14 | — | `cross_sum(day_first(Amt), 60)` |
| window | `cross_sum@60->30` | -1.20 | -1.20 | -1.19 | — | `cross_sum(day_first(Volume), 30)` |
| window | `cross_sum@60->120` | -1.69 | -0.96 | -1.69 | — | `cross_sum(day_first(Volume), 120)` |

### head score -1.15:`cross_sum(day_first(Volume), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.66 | -1.66 | -0.90 | — | `cross_sum(day_first(Amt), 5)` |
| window | `cross_sum@5->2` | -1.16 | -1.16 | -1.16 | — | `cross_sum(day_first(Volume), 2)` |
| window | `cross_sum@5->10` | -1.38 | -1.31 | -1.38 | — | `cross_sum(day_first(Volume), 10)` |

### head score -1.20:`cross_sum(day_first(Volume), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.49 | -1.49 | -0.84 | — | `cross_sum(day_first(Amt), 3)` |
| window | `cross_sum@3->2` | -1.16 | -1.16 | -1.16 | — | `cross_sum(day_first(Volume), 2)` |
| window | `cross_sum@3->6` | -1.17 | -1.17 | -1.16 | — | `cross_sum(day_first(Volume), 6)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_first(Volume)` — enrichment,均值差 +1.21,p 0.029

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
