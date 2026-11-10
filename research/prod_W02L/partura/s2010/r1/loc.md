# 定位:种子 2010,P 组,第 1 轮(只含 train / valid)

快照:prods2010M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.16 | -1.16 | -0.51 | +1 | 0 | prods2010M1_I0_open_search | `cross_fangzheng(ts_sum(day_durbin_watson(Vwap), 10), 241)` |
| -2.60 | -2.60 | -2.46 | -1 | 5 | prods2010M1_I0_open_search | `sqrt(ts_scale(ts_sum(day_durbin_watson(Volume), 20), 40))` |
| -2.63 | -2.49 | -2.63 | -1 | 0 | prods2010M1_I0_open_search | `ts_sum(day_durbin_watson(Low), 20)` |

## 共性:9 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.36 | 0.905 | 5 | -3.25 / -2.88 | `ts_sum(day_durbin_watson(Vwap), 10)` |

## 拆解(18 次评估)

### head score -1.16:`cross_fangzheng(ts_sum(day_durbin_watson(Vwap), 10), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(day_durbin_watson(Vwap), 10)` | -3.48 | -3.48 | -2.33 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `ts_sum(day_durbin_watson(Vwap), 10)` | -1.08 | -1.08 | -0.79 | -0.08 | `cross_fangzheng(day_durbin_watson(Vwap), 241)` |
| swap | `Vwap->Close` | -1.36 | -1.36 | -0.49 | — | `cross_fangzheng(ts_sum(day_durbin_watson(Close), 10), 241)` |
| window | `cross_fangzheng@241->120` | -1.36 | -1.04 | -1.36 | — | `cross_fangzheng(ts_sum(day_durbin_watson(Vwap), 10), 120)` |
| window | `cross_fangzheng@241->482` | -2.06 | -2.06 | -0.61 | — | `cross_fangzheng(ts_sum(day_durbin_watson(Vwap), 10), 482)` |

### head score -2.60:`sqrt(ts_scale(ts_sum(day_durbin_watson(Volume), 20), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_scale(ts_sum(day_durbin_watson(Volume), 20), 40)` | -2.60 | -2.60 | -2.39 | — | (子树本身) |
| sufficiency | `ts_sum(day_durbin_watson(Volume), 20)` | -3.17 | -3.17 | -3.08 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Volume)` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| knockout | `ts_scale(ts_sum(day_durbin_watson(Volume), 20), 40)` | -3.17 | -3.17 | -3.08 | +0.56 | `sqrt(ts_sum(day_durbin_watson(Volume), 20))` |
| knockout | `ts_sum(day_durbin_watson(Volume), 20)` | -2.90 | -2.90 | -2.88 | +0.29 | `sqrt(ts_scale(day_durbin_watson(Volume), 40))` |
| swap | `Volume->Amt` | -2.66 | -2.66 | -2.44 | — | `sqrt(ts_scale(ts_sum(day_durbin_watson(Amt), 20), 40))` |
| window | `ts_scale@40->20` | -2.89 | -2.89 | -2.68 | — | `sqrt(ts_scale(ts_sum(day_durbin_watson(Volume), 20), 20))` |
| window | `ts_scale@40->80` | -2.61 | -2.61 | -2.57 | — | `sqrt(ts_scale(ts_sum(day_durbin_watson(Volume), 20), 80))` |

### head score -2.63:`ts_sum(day_durbin_watson(Low), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Low)` | -3.74 | -3.74 | -3.18 | — | (子树本身) |
| swap | `Low->High` | -2.39 | -2.39 | -2.35 | — | `ts_sum(day_durbin_watson(High), 20)` |
| window | `ts_sum@20->10` | -3.38 | -3.38 | -3.30 | — | `ts_sum(day_durbin_watson(Low), 10)` |
| window | `ts_sum@20->40` | -3.49 | -2.66 | -3.49 | — | `ts_sum(day_durbin_watson(Low), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(swap Low->High):`ts_sum(day_durbin_watson(High), 20)`
