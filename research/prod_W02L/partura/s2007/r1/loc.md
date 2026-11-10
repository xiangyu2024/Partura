# 定位:种子 2007,P 组,第 1 轮(只含 train / valid)

快照:prods2007M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.06 | -2.06 | -1.72 | +1 | 0 | prods2007M1_I0_open_search | `cross_sum(day_durbin_watson(Close), 60)` |
| -2.94 | -2.94 | -0.95 | +1 | 20 | prods2007M1_I0_open_search | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` |
| -3.13 | -3.13 | -2.71 | +1 | 20 | prods2007M1_I0_open_search | `log(day_durbin_watson(Vwap))` |

## 共性:29 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.13 | 0.030 | 8 | -3.65 / -3.78 | `day_durbin_watson(Vwap)` |
| +0.08 | 0.596 | 6 | -3.68 / -3.77 | `day_durbin_watson(Close)` |

## 拆解(12 次评估)

### head score -2.06:`cross_sum(day_durbin_watson(Close), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Close)` | -4.03 | -4.03 | -3.83 | — | (子树本身) |
| swap | `Close->Vwap` | -2.17 | -2.17 | -1.82 | — | `cross_sum(day_durbin_watson(Vwap), 60)` |
| window | `cross_sum@60->30` | -3.72 | -3.33 | -3.72 | — | `cross_sum(day_durbin_watson(Close), 30)` |
| window | `cross_sum@60->120` | -2.13 | -2.13 | -1.70 | — | `cross_sum(day_durbin_watson(Close), 120)` |

### head score -2.94:`cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_scale(day_durbin_watson(Vwap), 10)` | -5.65 | -5.65 | -4.46 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `ts_scale(day_durbin_watson(Vwap), 10)` | -2.88 | -2.88 | -2.20 | -0.06 | `cross_fangzheng(day_durbin_watson(Vwap), 10)` |
| swap | `Vwap->Close` | -3.73 | -3.55 | -3.73 | — | `cross_fangzheng(ts_scale(day_durbin_watson(Close), 10), 10)` |
| window | `cross_fangzheng@10->5` | -3.60 | -3.60 | -1.70 | — | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 5)` |
| window | `cross_fangzheng@10->20` | -2.22 | -2.22 | -0.45 | — | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 20)` |

### head score -3.13:`log(day_durbin_watson(Vwap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| swap | `Vwap->Close` | -4.05 | -4.05 | -3.91 | — | `log(day_durbin_watson(Close))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.13,p 0.030

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.72(window cross_fangzheng@10->20):`cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 20)`
