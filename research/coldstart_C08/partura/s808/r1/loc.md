# 定位:种子 808,P 组,第 1 轮(只含 train / valid)

快照:c07s808M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(4 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.26 | +1.26 | +1.79 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 50)` |
| +0.99 | +0.99 | +1.42 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` |
| +0.68 | +0.98 | +0.68 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)` |
| +0.64 | +0.64 | +2.45 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` |

## 共性:83 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.03 | 0.002 | 4 | +0.89 / -1.15 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` |
| +2.03 | 0.000 | 14 | +0.64 / -1.39 | `cs_demean(day_wstd(Ret, Volume))` |
| +1.96 | 0.000 | 10 | +0.67 / -1.28 | `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` |
| +1.88 | 0.005 | 4 | +0.74 / -1.14 | `day_wstd(Ret, Ret)` |
| +1.61 | 0.000 | 18 | +0.21 / -1.40 | `day_wstd(Ret, Volume)` |
| +0.36 | 0.223 | 9 | -0.72 / -1.09 | `ts_max(LogFloatShares, 50)` |
| +0.13 | 0.420 | 4 | -0.92 / -1.05 | `ts_min(LogFloatShares, 50)` |

## 拆解(27 次评估)

### head score +1.26:`ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` | +0.98 | +0.98 | +2.24 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` | -0.21 | +0.79 | -0.21 | — | (子树本身) |
| sufficiency | `cs_demean(day_wstd(Ret, Volume))` | -3.47 | -2.68 | -3.47 | — | (子树本身) |
| sufficiency | `day_wstd(Ret, Volume)` | -3.47 | -2.68 | -3.47 | — | (子树本身) |
| knockout | `cs_demean(day_wstd(Ret, Volume))` | +1.03 | +1.03 | +1.54 | +0.23 | `ts_max(ts_max(ts_max(day_wstd(Ret, Volume), 50), 50), 50)` |
| swap | `Volume->Amt` | +1.25 | +1.25 | +1.68 | — | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Amt)), 50), 50), 50)` |
| window | `ts_max@50->25` | +1.00 | +1.00 | +1.63 | — | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 25)` |
| window | `ts_max@50->100` | +0.74 | +0.74 | +1.20 | — | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 100)` |

### head score +0.99:`ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_wmean(Ret, Volume), 50)` | -1.51 | +0.24 | -1.51 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Volume)` | -2.49 | -2.49 | +0.00 | — | (子树本身) |
| swap | `Volume->Amt` | +1.09 | +1.09 | +1.53 | — | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` |
| window | `ts_max@50->25` | +0.64 | +1.00 | +0.64 | — | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 25)` |
| window | `ts_max@50->100` | +0.68 | +0.68 | +1.23 | — | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 100)` |

### head score +0.68:`ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_demean(day_wstd(Ret, Volume)), 10)` | -1.41 | -1.41 | -0.28 | — | (子树本身) |
| sufficiency | `cs_demean(day_wstd(Ret, Volume))` | -3.47 | -2.68 | -3.47 | — | (子树本身) |
| sufficiency | `day_wstd(Ret, Volume)` | -3.47 | -2.68 | -3.47 | — | (子树本身) |
| knockout | `ts_max(cs_demean(day_wstd(Ret, Volume)), 10)` | -0.21 | +0.79 | -0.21 | +0.89 | `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` |
| knockout | `cs_demean(day_wstd(Ret, Volume))` | +0.65 | +0.82 | +0.65 | +0.03 | `ts_max(ts_max(day_wstd(Ret, Volume), 10), 50)` |
| swap | `Volume->Amt` | +0.70 | +0.97 | +0.70 | — | `ts_max(ts_max(cs_demean(day_wstd(Ret, Amt)), 10), 50)` |
| window | `ts_max@50->25` | -0.51 | +0.37 | -0.51 | — | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 25)` |
| window | `ts_max@50->100` | +1.07 | +1.07 | +2.25 | — | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` |

### head score +0.64:`ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_normalize(day_wstd(Ret, Ret)), 50)` | +0.22 | +0.22 | +0.75 | — | (子树本身) |
| sufficiency | `cs_normalize(day_wstd(Ret, Ret))` | -3.33 | -2.32 | -3.33 | — | (子树本身) |
| sufficiency | `day_wstd(Ret, Ret)` | -3.33 | -2.33 | -3.33 | — | (子树本身) |
| knockout | `cs_normalize(day_wstd(Ret, Ret))` | +0.79 | +0.79 | +2.47 | -0.15 | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)` |
| window | `ts_max@50->25` | +0.53 | +0.53 | +1.86 | — | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 25)` |
| window | `ts_max@50->100` | +0.63 | +0.63 | +1.67 | — | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` — ablation,自身 score +0.98(所在 head +1.26)
2. `cs_demean(day_wstd(Ret, Volume))` — enrichment,均值差 +2.03,p 0.000
3. `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` — enrichment,均值差 +1.96,p 0.000
4. `day_wstd(Ret, Ret)` — enrichment,均值差 +1.88,p 0.005
5. `day_wstd(Ret, Volume)` — enrichment,均值差 +1.61,p 0.000

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.39(window ts_max@50->100):`ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)`
- 增益 +0.15(knockout cs_normalize(day_wstd(Ret, Ret))):`ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)`
- 增益 +0.11(swap Volume->Amt):`ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)`
