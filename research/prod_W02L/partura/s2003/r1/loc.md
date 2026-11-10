# 定位:种子 2003,P 组,第 1 轮(只含 train / valid)

快照:prods2003M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.23 | -1.11 | -1.23 | +1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 50)` |
| -1.49 | -1.30 | -1.49 | +1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| -1.57 | -1.56 | -1.57 | -1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |

## 共性:10 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.54 | 0.133 | 7 | -1.88 / -2.42 | `day_q_stat_std(Vwap)` |
| +0.44 | 0.192 | 7 | -1.91 / -2.35 | `day_last(Volume)` |
| +0.28 | 0.305 | 6 | -1.93 / -2.21 | `log(add(day_q_stat_std(Vwap), day_std(Vwap)))` |
| +0.28 | 0.305 | 6 | -1.93 / -2.21 | `add(day_q_stat_std(Vwap), day_std(Vwap))` |
| +0.05 | 0.543 | 6 | -2.03 / -2.07 | `div(day_last(Volume), day_max(Low))` |
| -0.13 | 0.655 | 5 | -2.11 / -1.98 | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` |

## 拆解(36 次评估)

### head score -1.23:`ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume))` | -1.29 | -1.07 | -1.29 | — | (子树本身) |
| sufficiency | `log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50))` | -2.08 | -1.70 | -2.08 | — | (子树本身) |
| sufficiency | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` | -2.08 | -1.70 | -2.08 | — | (子树本身) |
| sufficiency | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -1.37 | -1.37 | -1.11 | — | (子树本身) |
| knockout | `mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume))` | -2.14 | -1.80 | -2.14 | +0.91 | `ts_mean(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), 50)` |
| knockout | `log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50))` | -1.18 | -1.00 | -1.18 | -0.05 | `ts_mean(mul(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50), day_max(Volume)), 50)` |
| knockout | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` | -1.71 | -1.34 | -1.71 | +0.48 | `ts_mean(mul(log(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))), day_max(Volume)), 50)` |
| knockout | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -1.19 | -1.19 | -1.19 | -0.03 | `ts_mean(mul(log(ts_mean(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), 50)), day_max(Volume)), 50)` |
| swap | `Vwap->Close` | -1.28 | -1.11 | -1.28 | — | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Close), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 50)` |
| swap | `Volume->Amt` | -1.26 | -1.24 | -1.26 | — | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Amt)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Amt)), 20)), 50)), day_max(Amt)), 50)` |
| window | `ts_mean@50->25` | -1.36 | -1.14 | -1.36 | — | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 25)` |
| window | `ts_mean@50->100` | -1.28 | -1.01 | -1.28 | — | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 100)` |

### head score -1.49:`ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.32 | -1.12 | -1.32 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap)))` | -1.74 | -1.74 | -1.55 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))` | -1.70 | -1.70 | -1.49 | — | (子树本身) |
| sufficiency | `mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.62 | -1.62 | -1.51 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.98 | -1.98 | -1.69 | +0.49 | `ts_mean(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), 50)` |
| knockout | `log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap)))` | -1.73 | -1.72 | -1.73 | +0.24 | `ts_mean(mul(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap)), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))` | -1.06 | -0.96 | -1.06 | -0.43 | `ts_mean(mul(log(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.52 | -1.41 | -1.52 | +0.03 | `ts_mean(mul(log(add(log(add(day_q_stat_std(Vwap), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Vwap->Close` | -1.51 | -1.41 | -1.51 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Close), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Volume->Amt` | -1.49 | -1.09 | -1.49 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| window | `ts_mean@50->25` | -1.24 | -1.06 | -1.24 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.77 | -1.77 | -1.63 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 100)` |

### head score -1.57:`ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.93 | -0.61 | -1.93 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume)))` | -1.28 | -1.15 | -1.28 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))` | -1.28 | -1.15 | -1.28 | — | (子树本身) |
| sufficiency | `mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.88 | -0.58 | -1.88 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.70 | -1.37 | -1.70 | +0.13 | `ts_mean(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), 50)` |
| knockout | `log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume)))` | -1.32 | -1.04 | -1.32 | -0.25 | `ts_mean(mul(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume)), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))` | -1.05 | -0.73 | -1.05 | -0.52 | `ts_mean(mul(log(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.62 | -1.56 | -1.62 | +0.05 | `ts_mean(mul(log(add(log(add(day_q_stat_std(Vwap), day_std(Volume))), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Vwap->Close` | -1.64 | -1.56 | -1.64 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Close), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Volume->Amt` | -1.03 | -1.03 | -0.35 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Amt))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), day_std(Amt))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| window | `ts_mean@50->25` | -2.03 | -1.11 | -2.03 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.79 | -1.64 | -1.79 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 100)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.43(knockout add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))):`ts_mean(mul(log(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)`
- 增益 +0.25(window ts_mean@50->25):`ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 25)`
