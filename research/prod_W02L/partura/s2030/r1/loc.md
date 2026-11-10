# 定位:种子 2030,P 组,第 1 轮(只含 train / valid)

快照:prods2030M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.19 | -0.19 | +0.06 | +1 | 5 | prods2030M1_I0_open_search | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 30))` |
| -0.40 | -0.40 | -0.38 | +1 | 5 | prods2030M1_I0_open_search | `pow_2(ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 30))` |
| -0.43 | -0.43 | -0.20 | +1 | 5 | prods2030M1_I0_open_search | `pow_2(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 30))` |

## 共性:6 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(28 次评估)

### head score -0.19:`pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 30)` | -0.20 | -0.20 | +0.00 | — | (子树本身) |
| sufficiency | `pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20))` | -0.56 | -0.51 | -0.56 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)` | -0.56 | -0.51 | -0.56 | — | (子树本身) |
| sufficiency | `ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10)` | -1.55 | -0.87 | -1.55 | — | (子树本身) |
| knockout | `ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 30)` | -0.56 | -0.51 | -0.56 | +0.37 | `pow_2(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)))` |
| knockout | `pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20))` | -0.20 | -0.20 | +0.00 | +0.01 | `pow_2(ts_max(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20), 30))` |
| knockout | `ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)` | -0.52 | -0.39 | -0.52 | +0.33 | `pow_2(ts_max(pow_2(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10)), 30))` |
| knockout | `ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10)` | -0.35 | -0.35 | +0.12 | +0.16 | `pow_2(ts_max(pow_2(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 20)), 30))` |
| window | `ts_max@30->15` | -0.52 | -0.52 | -0.17 | — | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 15))` |
| window | `ts_max@30->60` | -0.15 | -0.03 | -0.15 | — | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 60))` |

### head score -0.40:`pow_2(ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 30)` | -0.42 | -0.41 | -0.42 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40)` | -1.41 | -0.84 | -1.41 | — | (子树本身) |
| sufficiency | `cs_demean(sub(day_mean(Ret), 0.5))` | -4.34 | -4.34 | -3.69 | — | (子树本身) |
| sufficiency | `day_mean(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| knockout | `ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 30)` | -1.37 | -0.81 | -1.37 | +0.97 | `pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40))` |
| knockout | `ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40)` | -1.52 | -1.19 | -1.52 | +1.11 | `pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30))` |
| knockout | `sub(day_mean(Ret), 0.5)` | -0.43 | -0.41 | -0.43 | +0.03 | `pow_2(ts_max(ts_max(cs_demean(day_mean(Ret)), 40), 30))` |
| window | `ts_max@30->15` | -0.62 | -0.51 | -0.62 | — | `pow_2(ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 15))` |
| window | `ts_max@30->60` | -0.12 | -0.12 | +0.01 | — | `pow_2(ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 60))` |

### head score -0.43:`pow_2(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 30)` | -0.41 | -0.40 | -0.41 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30)` | -1.47 | -0.96 | -1.47 | — | (子树本身) |
| sufficiency | `cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5))` | -2.35 | -2.35 | -2.19 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10)` | -2.35 | -2.35 | -2.19 | — | (子树本身) |
| knockout | `ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 30)` | -1.26 | -1.13 | -1.26 | +0.82 | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30))` |
| knockout | `sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)` | -0.44 | -0.44 | -0.24 | +0.00 | `pow_2(ts_max(ts_max(cs_demean(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10)), 30), 30))` |
| knockout | `ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10)` | -0.54 | -0.47 | -0.54 | +0.10 | `pow_2(ts_max(ts_max(cs_demean(sub(cs_demean(sub(day_mean(Ret), -0.5)), -0.5)), 30), 30))` |
| window | `ts_max@30->15` | -0.52 | -0.52 | -0.35 | — | `pow_2(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 15))` |
| window | `ts_max@30->60` | -0.19 | -0.19 | +0.01 | — | `pow_2(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 60))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.28(window ts_max@30->60):`pow_2(ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 60))`
- 增益 +0.25(window ts_max@30->60):`pow_2(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 60))`
