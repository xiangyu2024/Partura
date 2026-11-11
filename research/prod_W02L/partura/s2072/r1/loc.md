# 定位:种子 2072,P 组,第 1 轮(只含 train / valid)

快照:prods2072M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.81 | -0.81 | -0.72 | +1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 50)` |
| -1.33 | -0.90 | -1.33 | +1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 20)` |
| -1.45 | -1.35 | -1.45 | -1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)` |

## 共性:11 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.14 | 0.536 | 4 | -1.93 / -2.07 | `ts_hurst(day_last(Volume), 20)` |
| -0.42 | 0.794 | 4 | -2.29 / -1.87 | `day_open(Ret)` |

## 拆解(36 次评估)

### head score -0.81:`ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20))` | -0.78 | -0.61 | -0.78 | — | (子树本身) |
| sufficiency | `log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap)))` | -1.49 | -1.13 | -1.49 | — | (子树本身) |
| sufficiency | `add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))` | -1.50 | -1.12 | -1.50 | — | (子树本身) |
| sufficiency | `log(add(day_last(Volume), day_std(Vwap)))` | -1.60 | -1.19 | -1.60 | — | (子树本身) |
| knockout | `mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20))` | -1.54 | -1.12 | -1.54 | +0.73 | `ts_mean(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), 50)` |
| knockout | `log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap)))` | -1.49 | -1.31 | -1.49 | +0.69 | `ts_mean(mul(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap)), ts_hurst(day_last(Volume), 20)), 50)` |
| knockout | `add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))` | -0.85 | -0.84 | -0.85 | +0.05 | `ts_mean(mul(log(log(add(day_last(Volume), day_std(Vwap)))), ts_hurst(day_last(Volume), 20)), 50)` |
| knockout | `log(add(day_last(Volume), day_std(Vwap)))` | -2.17 | -1.46 | -2.17 | +1.36 | `ts_mean(mul(log(add(add(day_last(Volume), day_std(Vwap)), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 50)` |
| swap | `Volume->Amt` | -1.02 | -1.02 | -0.51 | — | `ts_mean(mul(log(add(log(add(day_last(Amt), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Amt), 20)), 50)` |
| swap | `Vwap->Close` | -0.80 | -0.80 | -0.63 | — | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Close))), day_std(Close))), ts_hurst(day_last(Volume), 20)), 50)` |
| window | `ts_mean@50->25` | -0.77 | -0.52 | -0.77 | — | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 25)` |
| window | `ts_mean@50->100` | -1.63 | -1.11 | -1.63 | — | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 100)` |

### head score -1.33:`ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20))` | -1.80 | -1.38 | -1.80 | — | (子树本身) |
| sufficiency | `ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)` | -0.78 | -0.78 | -0.67 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50))` | -1.43 | -1.19 | -1.43 | — | (子树本身) |
| sufficiency | `ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` | -2.19 | -1.52 | -2.19 | — | (子树本身) |
| knockout | `mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20))` | -1.69 | -1.27 | -1.69 | +0.36 | `ts_mean(log(add(day_last(Volume), day_std(Vwap))), 20)` |
| knockout | `ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)` | -1.35 | -1.16 | -1.35 | +0.02 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50))), 20)` |
| knockout | `div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50))` | -1.56 | -1.20 | -1.56 | +0.23 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 20)` |
| knockout | `ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` | -3.70 | -1.78 | -3.70 | +2.37 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))), 20)), 20)` |
| swap | `Volume->Amt` | -1.61 | -1.61 | -1.09 | — | `ts_mean(mul(log(add(day_last(Amt), day_std(Vwap))), ts_hurst(div(day_last(Amt), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)), 20)), 20)` |
| swap | `Vwap->Close` | -1.28 | -0.97 | -1.28 | — | `ts_mean(mul(log(add(day_last(Volume), day_std(Close))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 20)` |
| window | `ts_mean@20->10` | -1.46 | -0.96 | -1.46 | — | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 10)` |
| window | `ts_mean@20->40` | -1.69 | -1.15 | -1.69 | — | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 40)` |

### head score -1.45:`ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20))` | -1.50 | -1.38 | -1.50 | — | (子树本身) |
| sufficiency | `ts_hurst(log(day_quantile(in_max(Ret))), 20)` | -1.25 | -1.23 | -1.25 | — | (子树本身) |
| sufficiency | `log(add(day_last(Volume), day_std(Vwap)))` | -1.60 | -1.19 | -1.60 | — | (子树本身) |
| sufficiency | `log(day_quantile(in_max(Ret)))` | -2.71 | -2.06 | -2.71 | — | (子树本身) |
| knockout | `mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20))` | -1.76 | -1.33 | -1.76 | +0.31 | `ts_mean(log(add(day_last(Volume), day_std(Vwap))), 50)` |
| knockout | `ts_hurst(log(day_quantile(in_max(Ret))), 20)` | -2.29 | -1.55 | -2.29 | +0.84 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), log(day_quantile(in_max(Ret)))), 50)` |
| knockout | `log(add(day_last(Volume), day_std(Vwap)))` | -1.37 | -0.89 | -1.37 | -0.08 | `ts_mean(mul(add(day_last(Volume), day_std(Vwap)), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)` |
| knockout | `log(day_quantile(in_max(Ret)))` | -2.59 | -1.15 | -2.59 | +1.14 | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(day_quantile(in_max(Ret)), 20)), 50)` |
| swap | `Volume->Amt` | -1.77 | -1.77 | -1.54 | — | `ts_mean(mul(log(add(day_last(Amt), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)` |
| swap | `Vwap->Close` | -1.48 | -1.35 | -1.48 | — | `ts_mean(mul(log(add(day_last(Volume), day_std(Close))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)` |
| window | `ts_mean@50->25` | -1.88 | -1.40 | -1.88 | — | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 25)` |
| window | `ts_mean@50->100` | — | — | — | — | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 100)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
