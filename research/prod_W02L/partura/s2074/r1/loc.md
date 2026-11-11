# 定位:种子 2074,P 组,第 1 轮(只含 train / valid)

快照:prods2074M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.55 | -1.18 | -1.55 | -1 | 20 | prods2074M1_I0_open_search | `pow_2(day_close(neg(Volume)))` |
| -1.93 | -1.63 | -1.93 | +1 | 5 | prods2074M1_I0_open_search | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` |
| -2.19 | -2.19 | -2.01 | +1 | 20 | prods2074M1_I0_open_search | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` |

## 共性:9 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(6 次评估)

### head score -1.55:`pow_2(day_close(neg(Volume)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_close(neg(Volume))` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| swap | `Volume->Amt` | -3.83 | -3.16 | -3.83 | — | `pow_2(day_close(neg(Amt)))` |

### head score -1.93:`day_quantile_q25(in_rank(pow_2_5(neg(Ret))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

### head score -2.19:`ts_sum(day_ar1_coefficient(neg(Vwap)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(neg(Vwap))` | -3.09 | -2.76 | -3.09 | — | (子树本身) |
| swap | `Vwap->Close` | -2.38 | -2.15 | -2.38 | — | `ts_sum(day_ar1_coefficient(neg(Close)), 10)` |
| window | `ts_sum@10->5` | -2.18 | -2.18 | -1.98 | — | `ts_sum(day_ar1_coefficient(neg(Vwap)), 5)` |
| window | `ts_sum@10->20` | -2.48 | -2.28 | -2.48 | — | `ts_sum(day_ar1_coefficient(neg(Vwap)), 20)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
