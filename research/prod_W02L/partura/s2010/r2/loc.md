# 定位:种子 2010,P 组,第 2 轮(只含 train / valid)

快照:prods2010M1_I0_open_search, prods2010M2_I0_open_search, prods2010Pr1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.15 | -0.15 | -0.10 | +1 | 0 | prods2010M1_I0_open_search | `cross_stddev(ts_sum(day_durbin_watson(Vwap), 10), 241)` |
| -1.89 | -1.67 | -1.89 | -1 | 5 | prods2010M1_I0_open_search | `cross_zscore(ts_sum(day_durbin_watson(Volume), 20), 120)` |
| -2.13 | -2.13 | -1.96 | +1 | 20 | prods2010M2_I0_open_search | `ts_min(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5), 5)` |
| -2.33 | -2.11 | -2.33 | +1 | 0 | prods2010M2_I0_open_search | `ts_quantile_q75(pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))), 50)` |
| -2.34 | -2.11 | -2.34 | +1 | 0 | prods2010M2_I0_open_search | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))), 50)` |
| -2.39 | -2.39 | -2.35 | -1 | 0 | prods2010M1_I0_open_search | `ts_sum(day_durbin_watson(High), 20)` |

## 共性:84 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.73 | 0.000 | 9 | -1.02 / -2.75 | `day_durbin_watson(in_slice(Vwap, 211, 240))` |
| +1.50 | 0.000 | 17 | -1.37 / -2.87 | `day_sum(in_slice(Ret, 1, 210))` |
| +0.88 | 0.013 | 7 | -1.75 / -2.64 | `day_durbin_watson(in_slice(Vwap, 1, 30))` |
| -0.61 | 0.697 | 4 | -3.15 / -2.54 | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 20)` |
| -0.65 | 0.946 | 10 | -3.14 / -2.49 | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))` |
| -0.71 | 0.977 | 12 | -3.18 / -2.46 | `cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))` |
| -0.72 | 0.982 | 7 | -3.22 / -2.50 | `day_durbin_watson(Vwap)` |
| -0.73 | 0.968 | 5 | -3.25 / -2.52 | `ts_sum(day_durbin_watson(Vwap), 10)` |
| -0.77 | 0.989 | 18 | -3.17 / -2.40 | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)` |
| -0.86 | 0.980 | 6 | -3.36 / -2.50 | `sigmoid(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))))` |
| -1.19 | 1.000 | 37 | -3.23 / -2.04 | `sigmoid(pow_05(day_ar1_coefficient(Volume)))` |
| -1.23 | 1.000 | 38 | -3.24 / -2.01 | `day_ar1_coefficient(Volume)` |
| -1.23 | 1.000 | 38 | -3.24 / -2.01 | `pow_05(day_ar1_coefficient(Volume))` |

## 拆解(32 次评估)

### head score -0.15:`cross_stddev(ts_sum(day_durbin_watson(Vwap), 10), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(day_durbin_watson(Vwap), 10)` | -3.48 | -3.48 | -2.33 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `ts_sum(day_durbin_watson(Vwap), 10)` | -0.40 | -0.39 | -0.40 | +0.25 | `cross_stddev(day_durbin_watson(Vwap), 241)` |
| swap | `Vwap->Close` | -0.17 | -0.17 | +0.04 | — | `cross_stddev(ts_sum(day_durbin_watson(Close), 10), 241)` |
| window | `cross_stddev@241->120` | -1.00 | -0.29 | -1.00 | — | `cross_stddev(ts_sum(day_durbin_watson(Vwap), 10), 120)` |
| window | `cross_stddev@241->482` | -1.16 | -1.16 | -0.53 | — | `cross_stddev(ts_sum(day_durbin_watson(Vwap), 10), 482)` |

### head score -1.89:`cross_zscore(ts_sum(day_durbin_watson(Volume), 20), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(day_durbin_watson(Volume), 20)` | -3.17 | -3.17 | -3.08 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Volume)` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| knockout | `ts_sum(day_durbin_watson(Volume), 20)` | -2.23 | -1.27 | -2.23 | +0.34 | `cross_zscore(day_durbin_watson(Volume), 120)` |
| swap | `Volume->Amt` | -1.90 | -1.72 | -1.90 | — | `cross_zscore(ts_sum(day_durbin_watson(Amt), 20), 120)` |
| window | `cross_zscore@120->60` | -2.03 | -1.94 | -2.03 | — | `cross_zscore(ts_sum(day_durbin_watson(Volume), 20), 60)` |
| window | `cross_zscore@120->240` | -2.28 | -1.76 | -2.28 | — | `cross_zscore(ts_sum(day_durbin_watson(Volume), 20), 240)` |

### head score -2.13:`ts_min(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5)` | -2.30 | -2.30 | -2.16 | — | (子树本身) |
| sufficiency | `sigmoid(pow_05(day_ar1_coefficient(High)))` | -2.64 | -2.64 | -2.30 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(High))` | -2.64 | -2.64 | -2.30 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(High)` | -2.64 | -2.64 | -2.30 | — | (子树本身) |
| knockout | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5)` | -2.13 | -2.08 | -2.13 | -0.00 | `ts_min(sigmoid(pow_05(day_ar1_coefficient(High))), 5)` |
| knockout | `sigmoid(pow_05(day_ar1_coefficient(High)))` | -2.12 | -2.12 | -2.05 | -0.01 | `ts_min(ts_decay_linear(pow_05(day_ar1_coefficient(High)), 5), 5)` |
| knockout | `pow_05(day_ar1_coefficient(High))` | -2.13 | -2.13 | -2.04 | -0.01 | `ts_min(ts_decay_linear(sigmoid(day_ar1_coefficient(High)), 5), 5)` |
| swap | `High->Low` | -2.35 | -2.35 | -2.24 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Low))), 5), 5)` |
| window | `ts_min@5->2` | -2.25 | -2.25 | -2.05 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5), 2)` |
| window | `ts_min@5->10` | -2.25 | -2.14 | -2.25 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5), 10)` |

### head score -2.33:`ts_quantile_q75(pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))))` | -3.41 | -2.91 | -3.41 | — | (子树本身) |
| sufficiency | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))` | -3.41 | -2.91 | -3.41 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))` | -3.41 | -2.91 | -3.41 | — | (子树本身) |
| sufficiency | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)` | -3.41 | -2.91 | -3.41 | — | (子树本身) |
| knockout | `pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))))` | -2.33 | -2.11 | -2.33 | +0.00 | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))), 50)` |
| knockout | `cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))` | -2.23 | -2.08 | -2.23 | -0.09 | `ts_quantile_q75(pow_2(pow_2(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))), 50)` |
| knockout | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)` | -2.09 | -1.96 | -2.09 | -0.23 | `ts_quantile_q75(pow_2(pow_2(cs_rank(sigmoid(pow_05(day_ar1_coefficient(Volume)))))), 50)` |
| swap | `Volume->Amt` | -2.30 | -2.09 | -2.30 | — | `ts_quantile_q75(pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Amt))), 5)))), 50)` |
| window | `ts_quantile_q75@50->25` | -2.81 | -2.74 | -2.81 | — | `ts_quantile_q75(pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))), 25)` |
| window | `ts_quantile_q75@50->100` | -1.65 | -1.59 | -1.65 | — | `ts_quantile_q75(pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_durbin_watson(in_slice(Vwap, 211, 240))` — enrichment,均值差 +1.73,p 0.000
2. `day_sum(in_slice(Ret, 1, 210))` — enrichment,均值差 +1.50,p 0.000
3. `day_durbin_watson(in_slice(Vwap, 1, 30))` — enrichment,均值差 +0.88,p 0.013

## 本组之前各轮的任务

- `prods2010Pr1b_Nb`:核心 `—`;评分 70,过线 0,入 heads 0;采样计数 {'c05_skeleton': 20}
  - score +0.13(train +0.40 valid +0.13):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), day_sum(in_slice(Ret, 1, 210)), 241)`
  - score -0.23(train +0.27 valid -0.23):`cross_corr(day_durbin_watson(in_slice(in_forward_valid_part(High), 211, 240)), day_sum(in_slice(Ret, 1, 210)), 120)`
  - score -0.52(train -0.52 valid -0.31):`cross_corr(day_durbin_watson(in_slice(in_forward_valid_part(High), 211, 240)), day_sum(in_slice(in_forward_valid_part(High), 1, 210)), 120)`
  - score -0.53(train -0.53 valid -0.30):`cross_corr(day_durbin_watson(in_slice(in_forward_valid_part(High), 211, 240)), day_sum(in_slice(High, 1, 210)), 120)`
  - score -0.53(train +0.68 valid -0.53):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), day_topw_mean(Amt, in_forward_valid_part(High)), 120)`

## 比原 head 好的拆解变体(R 候选)

(没有)
