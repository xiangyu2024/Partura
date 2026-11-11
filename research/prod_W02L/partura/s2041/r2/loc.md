# 定位:种子 2041,P 组,第 2 轮(只含 train / valid)

快照:prods2041M1_I0_open_search, prods2041M2_I0_open_search, prods2041Pr1a_Ea, prods2041Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.51 | -1.38 | -1.51 | -1 | 20 | prods2041M1_I0_open_search | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Volume, create_like(in_slice(Close, 1, 1), 0)))` |
| -1.73 | -1.72 | -1.73 | -1 | 20 | prods2041M1_I0_open_search | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))` |
| -1.80 | -1.44 | -1.80 | -1 | 20 | prods2041M1_I0_open_search | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))` |
| -1.81 | -1.81 | -1.75 | -1 | 5 | prods2041M2_I0_open_search | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210))), 20)` |
| -1.90 | -1.78 | -1.90 | -1 | 5 | prods2041M2_I0_open_search | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120))), 20)` |
| -1.94 | -1.85 | -1.94 | -1 | 5 | prods2041M2_I0_open_search | `cross_stddev(div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30))), 20)` |

## 共性:110 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.13 | 0.000 | 6 | -0.73 / -2.86 | `day_first(Open)` |
| +2.01 | 0.001 | 5 | -0.82 / -2.83 | `day_close(Vwap)` |
| +1.32 | 0.003 | 9 | -1.53 / -2.85 | `day_corr(in_delta(Vwap, 5), Volume)` |
| +1.31 | 0.001 | 14 | -1.60 / -2.91 | `day_gini(High)` |
| +1.27 | 0.007 | 7 | -1.55 / -2.82 | `day_last(Close)` |
| +1.17 | 0.031 | 5 | -1.62 / -2.79 | `ts_skew(day_corr(in_delta(Vwap, 5), Volume), 20)` |
| +0.90 | 0.091 | 4 | -1.87 / -2.77 | `ts_skew(day_last(Close), 20)` |
| +0.43 | 0.228 | 5 | -2.33 / -2.76 | `day_close(Amt)` |
| -1.16 | 1.000 | 28 | -3.60 / -2.45 | `in_slice(Close, 1, 1)` |
| -1.18 | 1.000 | 26 | -3.64 / -2.46 | `create_like(in_slice(Close, 1, 1), 0)` |
| -1.32 | 1.000 | 14 | -3.90 / -2.57 | `create_like(in_slice(Close, 1, 1), 1e-05)` |
| -1.41 | 0.988 | 4 | -4.10 / -2.69 | `add(day_sum(Amt), create_like(in_slice(Close, 1, 1), 1e-05))` |
| -1.41 | 0.988 | 4 | -4.10 / -2.69 | `day_sum(Amt)` |
| -1.52 | 0.999 | 6 | -4.18 / -2.66 | `add(day_sum(Volume), create_like(in_slice(Close, 1, 1), 1e-05))` |
| -1.52 | 0.999 | 6 | -4.18 / -2.66 | `day_sum(Volume)` |

## 拆解(24 次评估)

### head score -1.81:`cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210)))` | -4.47 | -4.47 | -3.71 | — | (子树本身) |
| sufficiency | `day_last(in_slice(Close, 1, 210))` | -2.37 | -1.62 | -2.37 | — | (子树本身) |
| sufficiency | `day_first(in_slice(Open, 1, 210))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210)))` | -2.29 | -1.79 | -2.29 | +0.48 | `cross_stddev(day_last(in_slice(Close, 1, 210)), 20)` |
| swap | `Close->Vwap` | -1.79 | -1.79 | -1.74 | — | `cross_stddev(div(day_last(in_slice(Vwap, 1, 210)), day_first(in_slice(Open, 1, 210))), 20)` |
| swap | `Open->Close` | -1.98 | -1.72 | -1.98 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Close, 1, 210))), 20)` |
| window | `cross_stddev@20->10` | -2.04 | -1.91 | -2.04 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210))), 10)` |
| window | `cross_stddev@20->40` | -1.71 | -1.71 | -1.36 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210))), 40)` |

### head score -1.90:`cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120)))` | -4.82 | -4.82 | -3.40 | — | (子树本身) |
| sufficiency | `day_last(in_slice(Close, 1, 120))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_first(in_slice(Open, 1, 120))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120)))` | -2.36 | -1.80 | -2.36 | +0.46 | `cross_stddev(day_last(in_slice(Close, 1, 120)), 20)` |
| swap | `Close->Vwap` | -1.96 | -1.83 | -1.96 | — | `cross_stddev(div(day_last(in_slice(Vwap, 1, 120)), day_first(in_slice(Open, 1, 120))), 20)` |
| swap | `Open->Close` | -2.09 | -1.62 | -2.09 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Close, 1, 120))), 20)` |
| window | `cross_stddev@20->10` | -2.20 | -1.95 | -2.20 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120))), 10)` |
| window | `cross_stddev@20->40` | -1.91 | -1.91 | -1.60 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120))), 40)` |

### head score -1.94:`cross_stddev(div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30)))` | -6.72 | -5.96 | -6.72 | — | (子树本身) |
| sufficiency | `day_last(in_slice(Close, 1, 30))` | -2.36 | -1.61 | -2.36 | — | (子树本身) |
| sufficiency | `day_first(in_slice(Open, 1, 30))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30)))` | -2.26 | -1.80 | -2.26 | +0.32 | `cross_stddev(day_last(in_slice(Close, 1, 30)), 20)` |
| swap | `Close->Vwap` | -1.84 | -1.84 | -1.77 | — | `cross_stddev(div(day_last(in_slice(Vwap, 1, 30)), day_first(in_slice(Open, 1, 30))), 20)` |
| swap | `Open->Close` | -2.04 | -1.63 | -2.04 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Close, 1, 30))), 20)` |
| window | `cross_stddev@20->10` | -3.21 | -2.00 | -3.21 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30))), 10)` |
| window | `cross_stddev@20->40` | -1.98 | -1.98 | -1.76 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_first(Open)` — enrichment,均值差 +2.13,p 0.000
2. `day_close(Vwap)` — enrichment,均值差 +2.01,p 0.001
3. `day_corr(in_delta(Vwap, 5), Volume)` — enrichment,均值差 +1.32,p 0.003
4. `day_gini(High)` — enrichment,均值差 +1.31,p 0.001
5. `day_last(Close)` — enrichment,均值差 +1.27,p 0.007
6. `ts_skew(day_corr(in_delta(Vwap, 5), Volume), 20)` — enrichment,均值差 +1.17,p 0.031
7. `ts_skew(day_last(Close), 20)` — enrichment,均值差 +0.90,p 0.091

## 本组之前各轮的任务

- `prods2041Pr1a_Ea`:核心 `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))`;评分 59,过线 0,入 heads 0;采样计数 {'c05_no_core': 6305, 'c05_skeleton': 3334}
  - score -1.22(train -1.16 valid -1.22):`day_distinct_ratio(Open)`
  - score -1.22(train -1.10 valid -1.22):`day_distinct_ratio(High)`
  - score -2.19(train -2.19 valid -1.87):`day_es_ratio_hi(Ret)`
  - score -2.69(train -2.69 valid -2.58):`day_es_ratio_lo(Open)`
  - score -3.22(train -3.22 valid -2.64):`day_hurst(Volume)`
- `prods2041Pr1b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 17}
  - score -0.50(train -0.39 valid -0.50):`cs_first_low20(day_gini(Open), day_close(Vwap))`
  - score -0.51(train -0.41 valid -0.51):`cs_first_low20(cs_first_low20(day_gini(Open), day_first(Open)), day_first(Open))`
  - score -0.51(train -0.41 valid -0.51):`cs_first_low20(day_gini(Open), day_first(Open))`
  - score -0.52(train -0.37 valid -0.52):`cs_first_low20(day_gini(High), day_last(Close))`
  - score -0.53(train -0.36 valid -0.53):`cs_first_low20(day_gini(High), day_close(Vwap))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.11(swap Close->Vwap):`cross_stddev(div(day_last(in_slice(Vwap, 1, 30)), day_first(in_slice(Open, 1, 30))), 20)`
