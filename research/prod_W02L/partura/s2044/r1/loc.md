# 定位:种子 2044,P 组,第 1 轮(只含 train / valid)

快照:prods2044M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.20 | +0.20 | +0.49 | +1 | 5 | prods2044M1_I0_open_search | `ts_max(ts_max(day_corr(Ret, Volume), 40), 40)` |
| -0.32 | -0.32 | +0.37 | +1 | 5 | prods2044M1_I0_open_search | `ts_max(day_corr(Ret, Volume), 40)` |
| -1.12 | -1.12 | -0.99 | +1 | 20 | prods2044M1_I0_open_search | `log(neg(cross_med(day_corr(Vwap, Amt), 60)))` |

## 共性:45 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.10 | 0.015 | 7 | -1.68 / -2.78 | `day_corr(Ret, Volume)` |
| -0.05 | 0.555 | 4 | -2.66 / -2.61 | `day_corr(Close, High)` |

## 拆解(18 次评估)

### head score +0.20:`ts_max(ts_max(day_corr(Ret, Volume), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_corr(Ret, Volume), 40)` | -0.32 | -0.32 | +0.42 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Volume)` | -3.39 | -3.39 | -2.98 | — | (子树本身) |
| swap | `Volume->Amt` | +0.23 | +0.23 | +0.52 | — | `ts_max(ts_max(day_corr(Ret, Amt), 40), 40)` |
| window | `ts_max@40->20` | +0.33 | +0.33 | +0.47 | — | `ts_max(ts_max(day_corr(Ret, Volume), 40), 20)` |
| window | `ts_max@40->80` | +0.56 | +0.68 | +0.56 | — | `ts_max(ts_max(day_corr(Ret, Volume), 40), 80)` |

### head score -0.32:`ts_max(day_corr(Ret, Volume), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(Ret, Volume)` | -3.39 | -3.39 | -2.98 | — | (子树本身) |
| swap | `Volume->Amt` | -0.27 | -0.27 | +0.41 | — | `ts_max(day_corr(Ret, Amt), 40)` |
| window | `ts_max@40->20` | -0.99 | -0.99 | -0.12 | — | `ts_max(day_corr(Ret, Volume), 20)` |
| window | `ts_max@40->80` | +0.24 | +0.24 | +0.53 | — | `ts_max(day_corr(Ret, Volume), 80)` |

### head score -1.12:`log(neg(cross_med(day_corr(Vwap, Amt), 60)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_med(day_corr(Vwap, Amt), 60))` | -1.47 | -1.47 | -1.10 | — | (子树本身) |
| sufficiency | `cross_med(day_corr(Vwap, Amt), 60)` | -1.47 | -1.47 | -1.10 | — | (子树本身) |
| sufficiency | `day_corr(Vwap, Amt)` | -4.35 | -4.35 | -3.06 | — | (子树本身) |
| knockout | `neg(cross_med(day_corr(Vwap, Amt), 60))` | -1.13 | -1.13 | -1.05 | +0.00 | `log(cross_med(day_corr(Vwap, Amt), 60))` |
| knockout | `cross_med(day_corr(Vwap, Amt), 60)` | -3.79 | -3.79 | -1.99 | +2.67 | `log(neg(day_corr(Vwap, Amt)))` |
| swap | `Vwap->Close` | -1.85 | -1.29 | -1.85 | — | `log(neg(cross_med(day_corr(Close, Amt), 60)))` |
| swap | `Amt->Volume` | -1.28 | -1.28 | -1.09 | — | `log(neg(cross_med(day_corr(Vwap, Volume), 60)))` |
| window | `cross_med@60->30` | -1.72 | -1.52 | -1.72 | — | `log(neg(cross_med(day_corr(Vwap, Amt), 30)))` |
| window | `cross_med@60->120` | -1.17 | -1.17 | -0.95 | — | `log(neg(cross_med(day_corr(Vwap, Amt), 120)))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_corr(Ret, Volume)` — enrichment,均值差 +1.10,p 0.015

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.56(window ts_max@40->80):`ts_max(day_corr(Ret, Volume), 80)`
- 增益 +0.36(window ts_max@40->80):`ts_max(ts_max(day_corr(Ret, Volume), 40), 80)`
- 增益 +0.14(window ts_max@40->20):`ts_max(ts_max(day_corr(Ret, Volume), 40), 20)`
