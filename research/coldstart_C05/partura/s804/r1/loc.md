# 定位:种子 804,B 组,第 1 轮(只含 train / valid)

快照:c05s804M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(5 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.91 | +0.91 | +1.87 | +1 | 0 | c05s804M1_I0_open_search | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.78 | +0.78 | +1.94 | +1 | 0 | c05s804M1_I0_open_search | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.76 | +0.76 | +2.63 | +1 | 5 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.65 | +0.65 | +2.79 | +1 | 20 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.58 | +0.58 | +1.90 | +1 | 20 | c05s804M1_I0_open_search | `sub(sub(sub(sub(ts_mean(abs_(neg(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10))))), 30), ts_var(day_gini(High), 10)), ts_var(day_gini(High), 10)), day_centroid(sqrt(Volume))), day_centroid(sqrt(Volume)))` |

## 共性:124 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.20 | 0.000 | 6 | +0.82 / -0.38 | `ts_var(day_gini(High), 5)` |
| +1.17 | 0.000 | 5 | +0.80 / -0.37 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` |
| +1.15 | 0.001 | 4 | +0.79 / -0.36 | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.12 | 0.000 | 14 | +0.67 / -0.45 | `ts_decay_linear(pow_3(day_mean(Open)), 20)` |
| +1.00 | 0.014 | 4 | +0.65 / -0.35 | `cross_ema(cross_ema(LogFloatShares, 241), 241)` |
| +0.99 | 0.000 | 15 | +0.55 / -0.44 | `day_mean(Open)` |
| +0.99 | 0.000 | 15 | +0.55 / -0.44 | `pow_3(day_mean(Open))` |
| +0.97 | 0.063 | 7 | +0.59 / -0.38 | `cross_quantile_q25(LogFloatShares, 241)` |
| +0.95 | 0.000 | 59 | +0.18 / -0.77 | `cross_ema(LogFloatShares, 241)` |
| +0.95 | 0.007 | 5 | +0.59 / -0.36 | `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` |
| +0.94 | 0.009 | 4 | +0.59 / -0.35 | `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` |
| +0.91 | 0.001 | 12 | +0.50 / -0.41 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` |
| +0.76 | 0.000 | 72 | -0.00 / -0.76 | `day_gini(High)` |
| +0.64 | 0.116 | 9 | +0.27 / -0.37 | `day_centroid(sqrt(Volume))` |
| +0.58 | 0.014 | 46 | +0.05 / -0.54 | `ts_var(day_gini(High), 10)` |
| +0.52 | 0.220 | 4 | +0.18 / -0.34 | `ts_quantile_q50(day_gini(High), 10)` |
| +0.45 | 0.375 | 4 | +0.12 / -0.34 | `abs_(day_corr(Vwap, High))` |
| +0.35 | 0.485 | 5 | +0.01 / -0.34 | `day_wstd(Vwap, High)` |
| +0.35 | 0.485 | 5 | +0.01 / -0.34 | `abs_(day_wstd(Vwap, High))` |
| -0.02 | 0.530 | 7 | -0.34 / -0.32 | `sub(cross_ema(LogFloatShares, 241), ts_var(LogFloatShares, 10))` |

## 拆解(46 次评估)

### head score +0.91:`sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` | +0.86 | +0.86 | +1.56 | — | (子树本身) |
| sufficiency | `cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.73 | +0.73 | +1.99 | — | (子树本身) |
| sufficiency | `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5))` | +0.59 | +0.59 | +0.97 | — | (子树本身) |
| knockout | `cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.73 | +0.73 | +1.99 | +0.19 | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.73 | +0.73 | +1.99 | +0.19 | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)))` |
| knockout | `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5))` | +0.92 | +0.92 | +1.87 | -0.00 | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| swap | `High->Low` | +0.91 | +0.91 | +1.87 | — | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(Low), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(Low), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| swap | `Open->Close` | +0.91 | +0.91 | +1.87 | — | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Close)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Close)), 20)))` |
| window | `cross_ema@241->120` | +0.92 | +0.92 | +1.83 | — | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 120), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| window | `cross_ema@241->482` | +0.93 | +0.93 | +1.91 | — | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 482), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |

### head score +0.78:`sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.78 | +0.78 | +1.94 | — | (子树本身) |
| sufficiency | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` | +0.58 | +0.58 | +0.96 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_3(day_mean(Open)), 20)` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `ts_var(day_gini(High), 10)` | -0.33 | -0.33 | -0.07 | — | (子树本身) |
| knockout | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.58 | +0.58 | +0.96 | +0.20 | `sub(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_var(day_gini(High), 10))` |
| knockout | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` | +0.78 | +0.78 | +1.94 | -0.00 | `sub(cs_first_low20(cross_ema(LogFloatShares, 241), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| knockout | `ts_decay_linear(pow_3(day_mean(Open)), 20)` | +0.80 | +0.80 | +2.06 | -0.02 | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| knockout | `ts_var(day_gini(High), 10)` | +0.78 | +0.78 | +1.95 | -0.00 | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), day_gini(High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| swap | `High->Low` | +0.78 | +0.78 | +1.94 | — | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(Low), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(Low), 10))` |
| swap | `Open->Close` | +0.78 | +0.78 | +1.94 | — | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_var(day_gini(High), 10))` |
| window | `cross_ema@241->120` | +0.77 | +0.77 | +1.93 | — | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 120), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| window | `cross_ema@241->482` | +0.78 | +0.78 | +1.95 | — | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 482), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |

### head score +0.76:`sub(cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.75 | +0.75 | +2.63 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_3(day_mean(Open)), 20)` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `abs_(day_wstd(Vwap, High))` | -1.06 | -1.06 | -0.39 | — | (子树本身) |
| sufficiency | `pow_3(day_mean(Open))` | -1.16 | -1.16 | -0.45 | — | (子树本身) |
| knockout | `cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.05 | -1.05 | -0.39 | +1.81 | `sub(abs_(day_wstd(Vwap, High)), ts_var(day_gini(High), 10))` |
| knockout | `ts_decay_linear(pow_3(day_mean(Open)), 20)` | +0.88 | +0.88 | +2.81 | -0.12 | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| knockout | `abs_(day_wstd(Vwap, High))` | +0.75 | +0.75 | +2.63 | +0.00 | `sub(cs_first_low20(day_wstd(Vwap, High), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| knockout | `pow_3(day_mean(Open))` | +0.75 | +0.75 | +2.61 | +0.00 | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(day_mean(Open), 20)), ts_var(day_gini(High), 10))` |
| swap | `Vwap->Close` | +0.74 | +0.74 | +2.62 | — | `sub(cs_first_low20(abs_(day_wstd(Close, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| swap | `High->Low` | +0.75 | +0.75 | +2.64 | — | `sub(cs_first_low20(abs_(day_wstd(Vwap, Low)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(Low), 10))` |
| window | `ts_decay_linear@20->10` | +0.80 | +0.80 | +2.57 | — | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 10)), ts_var(day_gini(High), 10))` |
| window | `ts_decay_linear@20->40` | +0.70 | +0.70 | +2.61 | — | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 40)), ts_var(day_gini(High), 10))` |

### head score +0.65:`sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.66 | +0.66 | +2.79 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_3(day_mean(Open)), 20)` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `abs_(day_corr(Vwap, High))` | -2.78 | -2.34 | -2.78 | — | (子树本身) |
| sufficiency | `pow_3(day_mean(Open))` | -1.16 | -1.16 | -0.45 | — | (子树本身) |
| knockout | `cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` | -2.78 | -2.33 | -2.78 | +3.43 | `sub(abs_(day_corr(Vwap, High)), ts_var(day_gini(High), 10))` |
| knockout | `ts_decay_linear(pow_3(day_mean(Open)), 20)` | +0.59 | +0.59 | +2.70 | +0.06 | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| knockout | `abs_(day_corr(Vwap, High))` | +0.65 | +0.65 | +2.79 | -0.00 | `sub(cs_first_low20(day_corr(Vwap, High), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| knockout | `pow_3(day_mean(Open))` | +0.64 | +0.64 | +2.75 | +0.02 | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(day_mean(Open), 20)), ts_var(day_gini(High), 10))` |
| swap | `Vwap->Close` | +0.19 | +0.19 | +2.25 | — | `sub(cs_first_low20(abs_(day_corr(Close, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| swap | `High->Low` | +0.56 | +0.56 | +2.53 | — | `sub(cs_first_low20(abs_(day_corr(Vwap, Low)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(Low), 10))` |
| window | `ts_decay_linear@20->10` | +0.67 | +0.67 | +2.71 | — | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 10)), ts_var(day_gini(High), 10))` |
| window | `ts_decay_linear@20->40` | +0.63 | +0.63 | +2.75 | — | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 40)), ts_var(day_gini(High), 10))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` — ablation,自身 score +0.86(所在 head +0.91)
2. `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — ablation,自身 score +0.78(所在 head +0.78)
3. `cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — ablation,自身 score +0.75(所在 head +0.76)
4. `cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — ablation,自身 score +0.73(所在 head +0.91)
5. `cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — ablation,自身 score +0.66(所在 head +0.65)
6. `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5))` — ablation,自身 score +0.59(所在 head +0.91)
7. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` — ablation,自身 score +0.58(所在 head +0.78)
8. `ts_var(day_gini(High), 5)` — enrichment,均值差 +1.20,p 0.000
9. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` — enrichment,均值差 +1.17,p 0.000
10. `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +1.15,p 0.001
11. `ts_decay_linear(pow_3(day_mean(Open)), 20)` — enrichment,均值差 +1.12,p 0.000
12. `cross_ema(cross_ema(LogFloatShares, 241), 241)` — enrichment,均值差 +1.00,p 0.014
13. `day_mean(Open)` — enrichment,均值差 +0.99,p 0.000
14. `pow_3(day_mean(Open))` — enrichment,均值差 +0.99,p 0.000
15. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +0.97,p 0.063
16. `cross_ema(LogFloatShares, 241)` — enrichment,均值差 +0.95,p 0.000
17. `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` — enrichment,均值差 +0.95,p 0.007
18. `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` — enrichment,均值差 +0.94,p 0.009
19. `day_gini(High)` — enrichment,均值差 +0.76,p 0.000
20. `ts_var(day_gini(High), 10)` — enrichment,均值差 +0.58,p 0.014

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.12(knockout ts_decay_linear(pow_3(day_mean(Open)), 20)):`sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))`
