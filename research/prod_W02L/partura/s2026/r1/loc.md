# 定位:种子 2026,P 组,第 1 轮(只含 train / valid)

快照:prods2026M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.74 | -2.74 | -2.32 | +1 | 20 | prods2026M1_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` |
| -2.78 | -2.78 | -2.04 | +1 | 20 | prods2026M1_I0_open_search | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 15), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| -2.79 | -2.79 | -2.25 | +1 | 20 | prods2026M1_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |

## 共性:10 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.24 | 0.238 | 4 | -3.14 / -3.37 | `day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` |
| +0.21 | 0.238 | 4 | -3.15 / -3.36 | `day_ar1_coefficient(in_slice(Ret, 11, 230))` |
| +0.20 | 0.238 | 4 | -3.16 / -3.36 | `day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` |

## 拆解(17 次评估)

### head score -2.74:`ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` | -3.81 | -3.81 | -3.06 | — | (子树本身) |
| swap | `Volume->Amt` | -2.79 | -2.79 | -2.26 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |
| window | `ts_stddev@15->7` | -3.38 | -3.38 | -2.85 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 7)` |
| window | `ts_stddev@15->30` | -2.23 | -2.23 | -1.81 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 30)` |

### head score -2.78:`add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 15), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` | -2.74 | -2.74 | -2.33 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` | -3.81 | -3.81 | -3.06 | — | (子树本身) |
| sufficiency | `ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 15)` | -2.54 | -2.54 | -2.16 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(in_slice(Ret, 11, 230))` | -3.60 | -3.57 | -3.60 | — | (子树本身) |
| knockout | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` | -3.87 | -3.87 | -3.15 | +1.09 | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 15), day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))))` |
| knockout | `ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 15)` | -3.93 | -3.93 | -3.91 | +1.15 | `add(day_ar1_coefficient(in_slice(Ret, 11, 230)), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| swap | `Volume->Amt` | -2.84 | -2.84 | -2.03 | — | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 15), ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |
| window | `ts_stddev@15->7` | -2.89 | -2.89 | -2.16 | — | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 7), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| window | `ts_stddev@15->30` | -2.80 | -2.80 | -2.52 | — | `add(ts_stddev(day_ar1_coefficient(in_slice(Ret, 11, 230)), 30), ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |

### head score -2.79:`ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` | -3.81 | -3.81 | -3.05 | — | (子树本身) |
| swap | `Amt->Volume` | -2.74 | -2.74 | -2.33 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` |
| window | `ts_stddev@15->7` | -3.28 | -3.28 | -2.84 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 7)` |
| window | `ts_stddev@15->30` | -2.19 | -2.19 | -1.81 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 30)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.60(window ts_stddev@15->30):`ts_stddev(day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 30)`
- 增益 +0.51(window ts_stddev@15->30):`ts_stddev(day_ar1_coefficient(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 30)`
