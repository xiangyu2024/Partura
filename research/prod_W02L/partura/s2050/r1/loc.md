# 定位:种子 2050,P 组,第 1 轮(只含 train / valid)

快照:prods2050M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.33 | -2.33 | -1.95 | -1 | 0 | prods2050M1_I0_open_search | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)` |
| -2.74 | -1.34 | -2.74 | +1 | 5 | prods2050M1_I0_open_search | `cross_stddev(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)` |
| -3.32 | -3.32 | -1.86 | +1 | 20 | prods2050M1_I0_open_search | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)` |

## 共性:8 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.81 | 0.115 | 5 | -3.36 / -4.17 | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` |

## 拆解(15 次评估)

### head score -2.33:`cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.71 | — | (子树本身) |
| window | `cross_stddev@20->10` | -2.96 | -2.67 | -2.96 | — | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 10)` |
| window | `cross_stddev@20->40` | -2.03 | -1.39 | -2.03 | — | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 40)` |

### head score -2.74:`cross_stddev(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -4.72 | -4.72 | -2.84 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.71 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |
| knockout | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -2.33 | -2.33 | -1.92 | -0.42 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)` |
| window | `cross_stddev@20->10` | -3.63 | -1.97 | -3.63 | — | `cross_stddev(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 10)` |
| window | `cross_stddev@20->40` | -2.89 | -1.41 | -2.89 | — | `cross_stddev(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 40)` |

### head score -3.32:`cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -4.72 | -4.72 | -2.84 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.71 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |
| knockout | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -3.65 | -3.64 | -3.65 | +0.32 | `cross_mean(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)` |
| window | `cross_mean@20->10` | -3.90 | -3.90 | -2.07 | — | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 10)` |
| window | `cross_mean@20->40` | -2.79 | -2.79 | -1.61 | — | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.54(window cross_mean@20->40):`cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 40)`
