# 定位:种子 2078,P 组,第 1 轮(只含 train / valid)

快照:prods2078M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.34 | -1.19 | -1.34 | -1 | 5 | prods2078M1_I0_open_search | `pow_05(cs_normalize(day_mean(Volume)))` |
| -1.54 | -1.19 | -1.54 | +1 | 5 | prods2078M1_I0_open_search | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))` |
| -1.80 | -1.47 | -1.80 | -1 | 20 | prods2078M1_I0_open_search | `pow_2(day_cov(Amt, Vwap))` |

## 共性:51 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.09 | 0.546 | 14 | -3.31 / -3.40 | `day_ar1_coefficient(Volume)` |

## 拆解(14 次评估)

### head score -1.34:`pow_05(cs_normalize(day_mean(Volume)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_normalize(day_mean(Volume))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_mean(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `cs_normalize(day_mean(Volume))` | -1.40 | -1.19 | -1.40 | +0.06 | `pow_05(day_mean(Volume))` |
| swap | `Volume->Amt` | -3.47 | -2.76 | -3.47 | — | `pow_05(cs_normalize(day_mean(Amt)))` |

### head score -1.54:`pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` | -1.55 | -1.17 | -1.55 | — | (子树本身) |
| sufficiency | `cs_demean(div(day_mean(Ret), 2))` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| sufficiency | `day_mean(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| knockout | `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` | — | — | — | — | `pow_1_5(cs_demean(div(day_mean(Ret), 2)))` |
| knockout | `div(day_mean(Ret), 2)` | -1.55 | -1.19 | -1.55 | +0.01 | `pow_1_5(ts_max(cs_demean(day_mean(Ret)), 30))` |
| window | `ts_max@30->15` | -2.49 | -2.26 | -2.49 | — | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 15))` |
| window | `ts_max@30->60` | -0.46 | -0.46 | -0.39 | — | `pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 60))` |

### head score -1.80:`pow_2(day_cov(Amt, Vwap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Amt, Vwap)` | -4.93 | -4.93 | -3.81 | — | (子树本身) |
| swap | `Amt->Volume` | -1.74 | -1.04 | -1.74 | — | `pow_2(day_cov(Volume, Vwap))` |
| swap | `Vwap->Close` | -1.71 | -1.60 | -1.71 | — | `pow_2(day_cov(Amt, Close))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.08(window ts_max@30->60):`pow_1_5(ts_max(cs_demean(div(day_mean(Ret), 2)), 60))`
