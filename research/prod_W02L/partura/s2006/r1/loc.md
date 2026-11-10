# 定位:种子 2006,P 组,第 1 轮(只含 train / valid)

快照:prods2006M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.17 | -1.17 | -0.75 | -1 | 20 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 50)))` |
| -1.44 | -1.27 | -1.44 | +1 | 5 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 50)))` |
| -1.51 | -1.27 | -1.51 | +1 | 5 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50)))` |

## 共性:16 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.83 | 0.039 | 4 | -1.46 / -2.30 | `day_cov(Amt, Open)` |
| -1.04 | 0.961 | 4 | -2.87 / -1.83 | `day_cov(Open, Open)` |

## 拆解(30 次评估)

### head score -1.17:`sub(0.5, abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 50)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 50))` | -1.17 | -1.17 | -0.75 | — | (子树本身) |
| sufficiency | `ts_regres(day_cov(Amt, Open), day_last(Amt), 50)` | -3.24 | -3.13 | -3.24 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Open)` | -4.76 | -4.76 | -3.84 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| knockout | `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 50))` | -3.24 | -3.13 | -3.24 | +2.06 | `sub(0.5, ts_regres(day_cov(Amt, Open), day_last(Amt), 50))` |
| knockout | `ts_regres(day_cov(Amt, Open), day_last(Amt), 50)` | -1.64 | -1.55 | -1.64 | +0.47 | `sub(0.5, abs_(day_cov(Amt, Open)))` |
| swap | `Amt->Volume` | -1.59 | -1.24 | -1.59 | — | `sub(0.5, abs_(ts_regres(day_cov(Volume, Open), day_last(Volume), 50)))` |
| swap | `Open->Close` | -1.19 | -1.19 | -0.75 | — | `sub(0.5, abs_(ts_regres(day_cov(Amt, Close), day_last(Amt), 50)))` |
| window | `ts_regres@50->25` | -2.58 | -2.58 | -1.27 | — | `sub(0.5, abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 25)))` |
| window | `ts_regres@50->100` | -0.64 | -0.64 | +0.03 | — | `sub(0.5, abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)))` |

### head score -1.44:`sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 50)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 50))` | -1.50 | -1.27 | -1.50 | — | (子树本身) |
| sufficiency | `ts_regres(day_cov(Ret, Amt), day_last(Volume), 50)` | -3.43 | -3.30 | -3.43 | — | (子树本身) |
| sufficiency | `day_cov(Ret, Amt)` | -3.93 | -3.93 | -3.13 | — | (子树本身) |
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| knockout | `abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 50))` | -3.43 | -3.30 | -3.43 | +1.99 | `sub(0.5, ts_regres(day_cov(Ret, Amt), day_last(Volume), 50))` |
| knockout | `ts_regres(day_cov(Ret, Amt), day_last(Volume), 50)` | -3.73 | -3.73 | -3.06 | +2.29 | `sub(0.5, abs_(day_cov(Ret, Amt)))` |
| swap | `Amt->Volume` | -1.50 | -1.26 | -1.50 | — | `sub(0.5, abs_(ts_regres(day_cov(Ret, Volume), day_last(Volume), 50)))` |
| swap | `Volume->Amt` | -1.18 | -1.18 | -0.78 | — | `sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Amt), 50)))` |
| window | `ts_regres@50->25` | -1.67 | -1.38 | -1.67 | — | `sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 25)))` |
| window | `ts_regres@50->100` | -1.66 | -1.32 | -1.66 | — | `sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 100)))` |

### head score -1.51:`sub(0.5, abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50))` | -1.58 | -1.27 | -1.58 | — | (子树本身) |
| sufficiency | `ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50)` | -3.24 | -3.21 | -3.24 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Vwap)` | -4.93 | -4.93 | -3.81 | — | (子树本身) |
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| knockout | `abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50))` | -3.24 | -3.21 | -3.24 | +1.73 | `sub(0.5, ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50))` |
| knockout | `ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50)` | -1.75 | -1.48 | -1.75 | +0.24 | `sub(0.5, abs_(day_cov(Amt, Vwap)))` |
| swap | `Amt->Volume` | -1.55 | -1.29 | -1.55 | — | `sub(0.5, abs_(ts_regres(day_cov(Volume, Vwap), day_last(Volume), 50)))` |
| swap | `Vwap->Close` | -1.64 | -1.24 | -1.64 | — | `sub(0.5, abs_(ts_regres(day_cov(Amt, Close), day_last(Volume), 50)))` |
| window | `ts_regres@50->25` | -1.65 | -1.37 | -1.65 | — | `sub(0.5, abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 25)))` |
| window | `ts_regres@50->100` | -1.68 | -1.42 | -1.68 | — | `sub(0.5, abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 100)))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_cov(Amt, Open)` — enrichment,均值差 +0.83,p 0.039

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
