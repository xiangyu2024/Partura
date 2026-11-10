# 定位:种子 2035,P 组,第 2 轮(只含 train / valid)

快照:prods2035M1_I0_open_search, prods2035M2_I0_open_search, prods2035Pr1a_Na, prods2035Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.34 | -1.19 | -1.34 | +1 | 5 | prods2035M1_I0_open_search | `inv(day_sum(Volume))` |
| -1.52 | -1.24 | -1.52 | -1 | 5 | prods2035M1_I0_open_search | `ts_max(ts_max(inv(inv(day_sum(Volume))), 10), 10)` |
| -1.64 | -1.64 | -1.56 | -1 | 5 | prods2035M2_I0_open_search | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12))), 20)` |
| -1.67 | -1.45 | -1.67 | -1 | 5 | prods2035M1_I0_open_search | `inv(ts_max(inv(day_sum(Volume)), 10))` |
| -2.14 | -1.96 | -2.14 | -1 | 20 | prods2035M2_I0_open_search | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 20)` |
| -2.19 | -2.16 | -2.19 | -1 | 20 | prods2035M2_I0_open_search | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False))), 20)` |

## 共性:108 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.88 | 0.033 | 4 | -1.29 / -2.17 | `cs_scale(cs_scale(cs_scale(LogFloatShares)))` |
| +0.84 | 0.001 | 19 | -1.45 / -2.28 | `cs_scale(LogFloatShares)` |
| +0.83 | 0.010 | 8 | -1.37 / -2.20 | `cs_scale(cs_scale(LogFloatShares))` |
| +0.75 | 0.036 | 5 | -1.42 / -2.17 | `cs_scale(ts_delta(cs_scale(LogFloatShares), 40))` |
| +0.65 | 0.042 | 9 | -1.54 / -2.19 | `ts_delta(cs_scale(LogFloatShares), 40)` |
| +0.64 | 0.002 | 17 | -1.60 / -2.24 | `sub(log(day_last(Amt)), LogTotalCap)` |
| +0.63 | 0.002 | 16 | -1.60 / -2.23 | `cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1)` |
| +0.61 | 0.001 | 21 | -1.64 / -2.26 | `log(day_last(Amt))` |
| +0.57 | 0.002 | 22 | -1.69 / -2.25 | `day_last(Amt)` |
| +0.54 | 0.035 | 11 | -1.65 / -2.19 | `cs_robust_z(day_open(Amt))` |
| +0.54 | 0.045 | 9 | -1.65 / -2.18 | `sqrt(cs_robust_z(day_open(Amt)))` |
| +0.39 | 0.074 | 34 | -1.87 / -2.26 | `day_last(Close)` |
| +0.39 | 0.086 | 12 | -1.79 / -2.18 | `day_open(Amt)` |
| +0.35 | 0.121 | 33 | -1.90 / -2.24 | `log(day_last(Close))` |
| +0.27 | 0.157 | 28 | -1.93 / -2.21 | `sub(log(day_last(Close)), LogTotalCap)` |
| +0.12 | 0.318 | 23 | -2.04 / -2.16 | `cross_delta(sub(log(day_last(Close)), LogTotalCap), 1)` |
| +0.10 | 0.575 | 5 | -2.04 / -2.14 | `cross_sum(cross_delta(sub(log(day_last(Close)), LogTotalCap), 1), 242)` |
| +0.06 | 0.435 | 11 | -2.08 / -2.14 | `day_signed_ratio(Amt, Volume)` |
| +0.05 | 0.186 | 11 | -2.09 / -2.14 | `abs_(cross_delta(sub(log(day_last(Close)), LogTotalCap), 1))` |
| -0.06 | 0.512 | 8 | -2.19 / -2.13 | `pow_3(pow_2_5(day_signed_ratio(Amt, Volume)))` |

## 拆解(24 次评估)

### head score -1.64:`cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12)))` | -4.18 | -4.18 | -3.73 | — | (子树本身) |
| sufficiency | `day_last(in_topk_masked(Volume, Close, 12))` | -2.36 | -1.59 | -2.36 | — | (子树本身) |
| sufficiency | `day_first(in_topk_masked(Volume, Open, 12))` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12)))` | -2.34 | -1.77 | -2.34 | +0.70 | `cross_stddev(day_last(in_topk_masked(Volume, Close, 12)), 20)` |
| swap | `Volume->Amt` | -1.60 | -1.60 | -1.46 | — | `cross_stddev(div(day_last(in_topk_masked(Amt, Close, 12)), day_first(in_topk_masked(Amt, Open, 12))), 20)` |
| swap | `Close->Vwap` | -1.63 | -1.63 | -1.45 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Vwap, 12)), day_first(in_topk_masked(Volume, Open, 12))), 20)` |
| window | `cross_stddev@20->10` | -1.89 | -1.89 | -1.63 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12))), 10)` |
| window | `cross_stddev@20->40` | -1.95 | -1.95 | -1.11 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12))), 40)` |

### head score -2.14:`cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False)))` | -4.70 | -4.70 | -3.79 | — | (子树本身) |
| sufficiency | `day_last(in_topk_masked(Volume, Close, 5, False))` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| sufficiency | `day_first(in_topk_masked(Volume, Open, 5, False))` | -2.36 | -1.61 | -2.36 | — | (子树本身) |
| knockout | `div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False)))` | -2.31 | -1.81 | -2.31 | +0.16 | `cross_stddev(day_last(in_topk_masked(Volume, Close, 5, False)), 20)` |
| swap | `Volume->Amt` | -2.09 | -1.90 | -2.09 | — | `cross_stddev(div(day_last(in_topk_masked(Amt, Close, 5, False)), day_first(in_topk_masked(Amt, Open, 5, False))), 20)` |
| swap | `Close->Vwap` | -2.20 | -2.11 | -2.20 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Vwap, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 20)` |
| window | `cross_stddev@20->10` | -2.40 | -1.94 | -2.40 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 10)` |
| window | `cross_stddev@20->40` | -1.93 | -1.93 | -1.84 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 40)` |

### head score -2.19:`cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False)))` | -5.20 | -5.20 | -3.45 | — | (子树本身) |
| sufficiency | `day_last(in_topk_masked(Volume, Close, 12, False))` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| sufficiency | `day_first(in_topk_masked(Volume, Open, 12, False))` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False)))` | -2.31 | -1.81 | -2.31 | +0.11 | `cross_stddev(day_last(in_topk_masked(Volume, Close, 12, False)), 20)` |
| swap | `Volume->Amt` | -2.18 | -2.18 | -2.17 | — | `cross_stddev(div(day_last(in_topk_masked(Amt, Close, 12, False)), day_first(in_topk_masked(Amt, Open, 12, False))), 20)` |
| swap | `Close->Vwap` | -2.72 | -1.66 | -2.72 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Vwap, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False))), 20)` |
| window | `cross_stddev@20->10` | -2.30 | -2.30 | -2.28 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False))), 10)` |
| window | `cross_stddev@20->40` | -2.28 | -2.28 | -1.97 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_scale(cs_scale(cs_scale(LogFloatShares)))` — enrichment,均值差 +0.88,p 0.033
2. `cs_scale(LogFloatShares)` — enrichment,均值差 +0.84,p 0.001
3. `cs_scale(cs_scale(LogFloatShares))` — enrichment,均值差 +0.83,p 0.010
4. `cs_scale(ts_delta(cs_scale(LogFloatShares), 40))` — enrichment,均值差 +0.75,p 0.036
5. `ts_delta(cs_scale(LogFloatShares), 40)` — enrichment,均值差 +0.65,p 0.042
6. `sub(log(day_last(Amt)), LogTotalCap)` — enrichment,均值差 +0.64,p 0.002
7. `cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1)` — enrichment,均值差 +0.63,p 0.002
8. `log(day_last(Amt))` — enrichment,均值差 +0.61,p 0.001
9. `day_last(Amt)` — enrichment,均值差 +0.57,p 0.002
10. `cs_robust_z(day_open(Amt))` — enrichment,均值差 +0.54,p 0.035
11. `sqrt(cs_robust_z(day_open(Amt)))` — enrichment,均值差 +0.54,p 0.045
12. `day_last(Close)` — enrichment,均值差 +0.39,p 0.074
13. `day_open(Amt)` — enrichment,均值差 +0.39,p 0.086

## 本组之前各轮的任务

- `prods2035Pr1a_Na`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score +0.10(train +0.10 valid +0.54):`cross_sum(select_where(is_lt(abs_(cross_delta(sub(sub(log(day_last(Close)), LogTotalCap), LogTotalCap), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241)`
  - score -0.14(train -0.14 valid +0.64):`cross_sum(select_where(is_lt(abs_(cross_delta(sub(abs_(cross_delta(sub(log(day_last(Close)), LogTotalCap), 1)), LogTotalCap), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241)`
  - score -0.21(train +0.28 valid -0.21):`cross_sum(select_where(is_lt(abs_(cross_delta(sub(log(log(day_last(Close))), LogTotalCap), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241)`
  - score -0.59(train -0.40 valid -0.59):`cross_sum(select_where(is_lt(abs_(cross_delta(sub(log(day_last(Close)), LogTotalCap), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), cross_delta(sub(log(day_last(Close)), LogTotalCap), 1)), 1), 0.0), 241)`
  - score -0.62(train -0.29 valid -0.62):`cross_sum(select_where(is_lt(abs_(cross_delta(sub(log(day_last(Close)), LogTotalCap), 10)), 0.15), cross_delta(sub(log(day_last(Amt)), is_lt(abs_(cross_delta(sub(log(day_last(Close)), LogTotalCap), 10)), 0.15)), 1), 0.0), 241)`
- `prods2035Pr1b_Nb`:核心 `—`;评分 62,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score -0.99(train -0.99 valid -0.08):`ts_delta(cs_scale(ts_std(cs_scale(ts_delta(cs_scale(LogFloatShares), 40)), 40)), 40)`
  - score -1.08(train -1.08 valid -0.80):`ts_delta(cs_scale(ts_delta(cs_scale(cs_scale(LogFloatShares)), 40)), 40)`
  - score -1.08(train -1.08 valid -0.80):`ts_delta(cs_scale(cs_scale(ts_delta(cs_scale(LogFloatShares), 40))), 40)`
  - score -1.08(train -1.08 valid -0.80):`ts_delta(cs_scale(ts_delta(cs_scale(LogFloatShares), 40)), 40)`
  - score -1.18(train -1.18 valid -0.98):`ts_delta(cs_scale(cs_scale(cs_scale(cs_scale(LogFloatShares)))), 50)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(window cross_stddev@20->40):`cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 40)`
