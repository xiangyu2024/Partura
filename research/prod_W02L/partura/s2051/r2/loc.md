# 定位:种子 2051,P 组,第 2 轮(只含 train / valid)

快照:prods2051M1_I0_open_search, prods2051M2_I0_open_search, prods2051Pr1a_Na, prods2051Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.58 | -0.58 | -0.53 | +1 | 20 | prods2051M1_I0_open_search | `day_skew(nt_ts_kurt(Low, 10))` |
| -1.87 | -1.86 | -1.87 | +1 | 20 | prods2051M1_I0_open_search | `day_max(nt_ts_kurt(Vwap, 10))` |
| -2.23 | -2.23 | -1.00 | -1 | 20 | prods2051M2_I0_open_search | `pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 15)))))` |
| -2.80 | -2.80 | -1.19 | -1 | 20 | prods2051M2_I0_open_search | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` |
| -2.86 | -2.86 | -1.32 | -1 | 20 | prods2051M2_I0_open_search | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` |
| -2.95 | -2.95 | -1.89 | -1 | 20 | prods2051M1_I0_open_search | `day_max(nt_ts_kurt(Vwap, 30))` |

## 共性:141 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.46 | 0.006 | 4 | -0.67 / -2.13 | `day_argmax(Volume)` |
| +0.96 | 0.000 | 36 | -1.37 / -2.33 | `day_kurt(Volume)` |
| +0.86 | 0.046 | 7 | -1.27 / -2.13 | `day_min(cross_argmax(Volume, 30))` |
| +0.83 | 0.023 | 9 | -1.31 / -2.14 | `day_min(Vwap)` |
| +0.79 | 0.062 | 6 | -1.32 / -2.12 | `day_min(Close)` |
| +0.63 | 0.099 | 8 | -1.49 / -2.12 | `day_std(in_top_quantile_flag_q10(Vwap))` |
| +0.23 | 0.354 | 5 | -1.86 / -2.09 | `day_kurt(Vwap)` |
| +0.23 | 0.249 | 10 | -1.87 / -2.10 | `day_var(Open)` |
| +0.18 | 0.338 | 15 | -1.92 / -2.10 | `day_argmax(Vwap)` |
| +0.15 | 0.412 | 7 | -1.94 / -2.09 | `day_sum(Ret)` |
| +0.03 | 0.447 | 11 | -2.06 / -2.09 | `day_kurt(in_delta(Vwap, 1))` |
| -0.90 | 0.985 | 5 | -2.95 / -2.05 | `day_max(nt_ts_kurt(Vwap, 30))` |

## 拆解(10 次评估)

### head score -2.23:`pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 15)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 15))))` | -2.23 | -2.23 | -1.06 | — | (子树本身) |
| swap | `Vwap->Close` | -1.47 | -1.00 | -1.47 | — | `pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 15)))))` |
| window | `nt_ts_kurt@15->7` | -2.06 | -2.06 | -1.63 | — | `pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 7)))))` |
| window | `nt_ts_kurt@15->30` | -2.86 | -2.86 | -1.38 | — | `pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30)))))` |

### head score -2.80:`day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -0.56 | -0.26 | -0.56 | — | `day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 10))))` |
| window | `nt_ts_kurt@10->5` | -2.26 | -2.14 | -2.26 | — | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 5))))` |
| window | `nt_ts_kurt@10->20` | -2.35 | -2.35 | -1.28 | — | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 20))))` |

### head score -2.86:`day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -4.50 | -3.08 | -4.50 | — | `day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))` |
| window | `nt_ts_kurt@30->15` | -2.23 | -2.23 | -1.06 | — | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 15))))` |
| window | `nt_ts_kurt@30->60` | -4.28 | -4.28 | -1.73 | — | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 60))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_argmax(Volume)` — enrichment,均值差 +1.46,p 0.006
2. `day_kurt(Volume)` — enrichment,均值差 +0.96,p 0.000
3. `day_min(cross_argmax(Volume, 30))` — enrichment,均值差 +0.86,p 0.046
4. `day_min(Vwap)` — enrichment,均值差 +0.83,p 0.023
5. `day_min(Close)` — enrichment,均值差 +0.79,p 0.062
6. `day_std(in_top_quantile_flag_q10(Vwap))` — enrichment,均值差 +0.63,p 0.099

## 本组之前各轮的任务

- `prods2051Pr1a_Na`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 18}
  - score +0.09(train +0.26 valid +0.09):`cross_corr(day_kurt(in_delta(in_delta(Vwap, 1), 1)), day_kurt(Volume), 241)`
  - score +0.07(train +0.07 valid +0.12):`cross_corr(day_kurt(in_delta(in_delta(in_delta(Vwap, 60), 1), 1)), day_kurt(Volume), 241)`
  - score -0.07(train +0.11 valid -0.07):`cross_corr(day_kurt(in_delta(Open, 1)), day_kurt(Volume), 60)`
  - score -0.10(train +0.57 valid -0.10):`cross_corr(day_kurt(in_delta(in_delta(Open, 1), 1)), day_kurt(Volume), 60)`
  - score -0.21(train -0.00 valid -0.21):`cross_corr(day_kurt(in_delta(Vwap, 15)), day_kurt(Volume), 60)`
- `prods2051Pr1b_Nb`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score +0.07(train +0.07 valid +0.13):`cross_regbeta(day_min(cross_argmax(Volume, 30)), day_std(in_top_quantile_flag_q10(Volume)), 60)`
  - score -0.01(train -0.01 valid +0.41):`cross_regbeta(day_skew(cross_argmax(Volume, 30)), day_std(in_top_quantile_flag_q10(Volume)), 60)`
  - score -0.53(train +0.05 valid -0.53):`cross_regbeta(day_min(cross_argmax(in_top_quantile_flag_q10(Vwap), 30)), day_argmax(Vwap), 60)`
  - score -0.54(train -0.28 valid -0.54):`cross_regbeta(day_min(Vwap), day_argmax(Volume), 60)`
  - score -0.59(train -0.10 valid -0.59):`cross_regbeta(day_min(Vwap), cross_regbeta(day_min(Vwap), day_argmax(Volume), 60), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.76(swap Vwap->Close):`pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 15)))))`
- 增益 +0.63(window nt_ts_kurt@30->15):`day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 15))))`
