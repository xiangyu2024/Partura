# 定位:种子 2002,P 组,第 1 轮(只含 train / valid)

快照:prods2002M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.99 | -0.96 | -0.99 | +1 | 5 | prods2002M1_I0_open_search | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| -1.08 | -0.26 | -1.08 | +1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` |
| -1.20 | -0.98 | -1.20 | -1 | 0 | prods2002M1_I0_open_search | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 30)` |

## 共性:30 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.44 | 0.151 | 19 | -2.07 / -2.52 | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` |
| +0.16 | 0.333 | 5 | -2.10 / -2.26 | `day_open(Ret)` |
| +0.04 | 0.298 | 8 | -2.20 / -2.25 | `day_max(Volume)` |
| -0.14 | 0.803 | 14 | -2.31 / -2.17 | `day_std(Vwap)` |

## 拆解(35 次评估)

### head score -0.99:`ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `log(cs_sum(day_argmax(Vwap)))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `cs_sum(day_argmax(Vwap))` | — | — | — | — | 门槛废品 |
| knockout | `mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | — | — | — | — | `ts_mean(log(cs_sum(day_argmax(Vwap))), 50)` |
| knockout | `log(cs_sum(day_argmax(Vwap)))` | -1.22 | -1.14 | -1.22 | +0.23 | `ts_mean(mul(cs_sum(day_argmax(Vwap)), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| knockout | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.63 | -1.58 | -1.63 | +0.64 | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), div(day_last(Volume), day_max(Low))), 50)` |
| knockout | `cs_sum(day_argmax(Vwap))` | -2.19 | -1.74 | -2.19 | +1.20 | `ts_mean(mul(log(day_argmax(Vwap)), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Vwap->Close` | -0.98 | -0.98 | -0.96 | — | `ts_mean(mul(log(cs_sum(day_argmax(Close))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| swap | `Volume->Amt` | -0.75 | -0.72 | -0.75 | — | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)` |
| window | `ts_mean@50->25` | -1.26 | -0.91 | -1.26 | — | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.40 | -1.00 | -1.40 | — | `ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 100)` |

### head score -1.08:`ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -0.75 | +0.17 | -0.75 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)))` | -0.76 | -0.17 | -0.76 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))` | -0.74 | -0.16 | -0.74 | — | (子树本身) |
| sufficiency | `mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -1.34 | -0.33 | -1.34 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -1.96 | -1.00 | -1.96 | +0.88 | `ts_mean(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), 50)` |
| knockout | `log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)))` | -1.21 | -0.56 | -1.21 | +0.14 | `ts_mean(mul(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap)), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` |
| knockout | `add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))` | -1.33 | -0.28 | -1.33 | +0.25 | `ts_mean(mul(log(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` |
| knockout | `mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20))` | -1.39 | -0.26 | -1.39 | +0.31 | `ts_mean(mul(log(add(log(add(day_max(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` |
| swap | `Volume->Amt` | -0.45 | -0.45 | -0.36 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Amt)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Amt)), 20)), 50)` |
| swap | `Vwap->Close` | -1.11 | -0.21 | -1.11 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Close))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)` |
| window | `ts_mean@50->25` | -0.53 | -0.08 | -0.53 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.46 | -0.49 | -1.46 | — | `ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 100)` |

### head score -1.20:`ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.18 | -1.14 | -1.18 | — | (子树本身) |
| sufficiency | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), day_max(Low))` | -1.55 | -1.55 | -1.50 | — | (子树本身) |
| sufficiency | `day_max(Volume)` | -1.16 | -1.10 | -1.16 | — | (子树本身) |
| knockout | `mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20))` | -1.32 | -1.07 | -1.32 | +0.13 | `ts_mean(day_max(Volume), 30)` |
| knockout | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.47 | -1.21 | -1.47 | +0.28 | `ts_mean(mul(day_max(Volume), div(day_last(Volume), day_max(Low))), 30)` |
| knockout | `div(day_last(Volume), day_max(Low))` | -1.25 | -1.00 | -1.25 | +0.06 | `ts_mean(mul(day_max(Volume), ts_hurst(day_last(Volume), 20)), 30)` |
| swap | `Volume->Amt` | -2.65 | -2.65 | -1.95 | — | `ts_mean(mul(day_max(Amt), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 30)` |
| swap | `Low->High` | -1.26 | -0.99 | -1.26 | — | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(High)), 20)), 30)` |
| window | `ts_mean@30->15` | -1.08 | -1.01 | -1.08 | — | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 15)` |
| window | `ts_mean@30->60` | -1.30 | -1.08 | -1.30 | — | `ts_mean(mul(day_max(Volume), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 60)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.63(swap Volume->Amt):`ts_mean(mul(log(add(mul(log(add(day_max(Amt), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Amt)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Amt), day_max(Amt)), 20)), 50)`
- 增益 +0.55(window ts_mean@50->25):`ts_mean(mul(log(add(mul(log(add(day_max(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 25)`
- 增益 +0.24(swap Volume->Amt):`ts_mean(mul(log(cs_sum(day_argmax(Vwap))), ts_hurst(div(day_last(Amt), day_max(Low)), 20)), 50)`
