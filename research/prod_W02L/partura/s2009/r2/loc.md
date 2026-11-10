# 定位:种子 2009,P 组,第 2 轮(只含 train / valid)

快照:prods2009M1_I0_open_search, prods2009M2_I0_open_search, prods2009Pr1a_Ea, prods2009Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.77 | -1.38 | -1.77 | +1 | 5 | prods2009M2_I0_open_search | `ts_max(day_durbin_watson(Close), 40)` |
| -2.11 | -1.65 | -2.11 | +1 | 5 | prods2009M2_I0_open_search | `ts_max(day_durbin_watson(Close), 30)` |
| -2.23 | -1.65 | -2.23 | +1 | 20 | prods2009M1_I0_open_search | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` |
| -2.27 | -1.92 | -2.27 | +1 | 20 | prods2009M1_I0_open_search | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` |
| -2.35 | -2.20 | -2.35 | +1 | 20 | prods2009M1_I0_open_search | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` |
| -2.73 | -2.31 | -2.73 | +1 | 5 | prods2009M2_I0_open_search | `ts_max(day_durbin_watson(Close), 20)` |

## 共性:140 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.32 | 0.021 | 4 | -1.20 / -2.51 | `day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))` |
| +0.72 | 0.022 | 11 | -1.81 / -2.53 | `log(cross_mean(log(log(day_durbin_watson(Volume))), 120))` |
| +0.50 | 0.064 | 14 | -2.02 / -2.53 | `cross_mean(log(log(day_durbin_watson(Volume))), 120)` |
| +0.06 | 0.478 | 12 | -2.42 / -2.48 | `ts_delay(day_sum(Ret), 1)` |
| +0.00 | 0.370 | 4 | -2.48 / -2.48 | `log(log(log(log(day_durbin_watson(Volume)))))` |
| -0.06 | 0.576 | 22 | -2.53 / -2.47 | `day_sum(Ret)` |
| -0.12 | 0.537 | 8 | -2.59 / -2.47 | `log(log(log(day_durbin_watson(Volume))))` |
| -0.12 | 0.614 | 9 | -2.59 / -2.47 | `cross_mean(log(log(day_durbin_watson(Volume))), 10)` |
| -0.13 | 0.697 | 59 | -2.55 / -2.42 | `log(day_durbin_watson(Volume))` |
| -0.13 | 0.697 | 59 | -2.55 / -2.42 | `log(log(day_durbin_watson(Volume)))` |
| -0.13 | 0.697 | 59 | -2.55 / -2.42 | `day_durbin_watson(Volume)` |
| -0.13 | 0.552 | 4 | -2.61 / -2.47 | `cross_delta(cross_mean(log(log(day_durbin_watson(Volume))), 10), 20)` |
| -0.35 | 0.824 | 5 | -2.81 / -2.46 | `cross_corr(log(log(day_durbin_watson(Volume))), ts_delay(day_sum(Ret), 1), 40)` |
| -0.96 | 0.997 | 11 | -3.36 / -2.40 | `day_durbin_watson(Close)` |
| -1.21 | 0.999 | 9 | -3.61 / -2.40 | `log(log(day_durbin_watson(Vwap)))` |
| -1.21 | 0.999 | 9 | -3.61 / -2.40 | `day_durbin_watson(Vwap)` |
| -1.21 | 0.999 | 9 | -3.61 / -2.40 | `log(day_durbin_watson(Vwap))` |
| -1.32 | 0.998 | 6 | -3.74 / -2.42 | `ts_max(day_durbin_watson(Close), 5)` |

## 拆解(12 次评估)

### head score -1.77:`ts_max(day_durbin_watson(Close), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Close)` | -4.03 | -4.03 | -3.83 | — | (子树本身) |
| swap | `Close->Vwap` | -2.21 | -1.30 | -2.21 | — | `ts_max(day_durbin_watson(Vwap), 40)` |
| window | `ts_max@40->20` | -2.75 | -2.31 | -2.75 | — | `ts_max(day_durbin_watson(Close), 20)` |
| window | `ts_max@40->80` | -0.92 | -0.45 | -0.92 | — | `ts_max(day_durbin_watson(Close), 80)` |

### head score -2.11:`ts_max(day_durbin_watson(Close), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Close)` | -4.03 | -4.03 | -3.83 | — | (子树本身) |
| swap | `Close->Vwap` | -1.73 | -1.55 | -1.73 | — | `ts_max(day_durbin_watson(Vwap), 30)` |
| window | `ts_max@30->15` | -3.64 | -2.93 | -3.64 | — | `ts_max(day_durbin_watson(Close), 15)` |
| window | `ts_max@30->60` | -1.19 | -0.64 | -1.19 | — | `ts_max(day_durbin_watson(Close), 60)` |

### head score -2.73:`ts_max(day_durbin_watson(Close), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Close)` | -4.03 | -4.03 | -3.83 | — | (子树本身) |
| swap | `Close->Vwap` | -2.20 | -2.20 | -1.57 | — | `ts_max(day_durbin_watson(Vwap), 20)` |
| window | `ts_max@20->10` | -3.59 | -3.39 | -3.59 | — | `ts_max(day_durbin_watson(Close), 10)` |
| window | `ts_max@20->40` | -1.80 | -1.37 | -1.80 | — | `ts_max(day_durbin_watson(Close), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))` — enrichment,均值差 +1.32,p 0.021
2. `log(cross_mean(log(log(day_durbin_watson(Volume))), 120))` — enrichment,均值差 +0.72,p 0.022
3. `cross_mean(log(log(day_durbin_watson(Volume))), 120)` — enrichment,均值差 +0.50,p 0.064

## 本组之前各轮的任务

- `prods2009Pr1a_Ea`:核心 `log(log(day_durbin_watson(Volume)))`;评分 99,过线 0,入 heads 0;采样计数 {'c05_no_core': 1562, 'c05_skeleton': 736, 'c05_periphery_seen': 3}
  - score -0.69(train -0.69 valid -0.37):`cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 60)`
  - score -0.82(train -0.82 valid +0.34):`cross_stddev(cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 60), 60)`
  - score -0.96(train -0.96 valid -0.59):`cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 5)`
  - score -1.10(train -0.99 valid -1.10):`cross_stddev(log(cross_mean(log(log(log(log(day_durbin_watson(Volume))))), 120)), 60)`
  - score -1.18(train -1.18 valid +0.11):`cross_stddev(cross_stddev(log(cross_med(log(log(day_durbin_watson(Volume))), 60)), 60), 60)`
- `prods2009Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.03(train -0.03 valid +0.23):`cross_mean(cross_mean(day_wmean(Ret, div(Amt, cross_mean(Close, 20))), 20), 241)`
  - score -0.05(train -0.05 valid +0.20):`cross_mean(cross_mean(day_wmean(Ret, add(Amt, Amt)), 20), 241)`
  - score -0.38(train -0.38 valid -0.25):`cross_mean(cross_mean(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 20), 241)`
  - score -0.48(train -0.48 valid +0.65):`cross_mean(day_corr(div(Volume, cross_mean(Amt, 20)), Amt), 241)`
  - score -0.55(train -0.55 valid -0.03):`cross_mean(day_corr(sub(in_delay(Ret, 1), cross_mean(Amt, 20)), in_delay(Ret, 1)), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.93(window ts_max@20->40):`ts_max(day_durbin_watson(Close), 40)`
- 增益 +0.92(window ts_max@30->60):`ts_max(day_durbin_watson(Close), 60)`
- 增益 +0.85(window ts_max@40->80):`ts_max(day_durbin_watson(Close), 80)`
- 增益 +0.53(swap Close->Vwap):`ts_max(day_durbin_watson(Vwap), 20)`
- 增益 +0.37(swap Close->Vwap):`ts_max(day_durbin_watson(Vwap), 30)`
