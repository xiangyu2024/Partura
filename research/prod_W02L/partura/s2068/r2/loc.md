# 定位:种子 2068,P 组,第 2 轮(只含 train / valid)

快照:prods2068M1_I0_open_search, prods2068M2_I0_open_search, prods2068Pr1a_Ea, prods2068Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.61 | -1.31 | -1.61 | -1 | 5 | prods2068M1_I0_open_search | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| -2.16 | -1.88 | -2.16 | -1 | 20 | prods2068M1_I0_open_search | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| -2.66 | -1.75 | -2.66 | +1 | 5 | prods2068M2_I0_open_search | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open, 3), Volume, 60), 241))` |
| -2.86 | -2.64 | -2.86 | -1 | 20 | prods2068M1_I0_open_search | `day_sum(abs_(in_slice(Ret, 1, 30)))` |
| -3.54 | -3.54 | -3.13 | +1 | 20 | prods2068M2_I0_open_search | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Volume, 21)), 5))` |
| -3.59 | -3.59 | -3.14 | +1 | 20 | prods2068M2_I0_open_search | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Amt, 21)), 5))` |

## 共性:138 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.96 | 0.001 | 4 | -1.17 / -3.13 | `day_median(Ret)` |
| +1.56 | 0.015 | 4 | -1.55 / -3.12 | `pow_3(day_max(Low))` |
| +1.52 | 0.000 | 17 | -1.74 / -3.26 | `ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10)` |
| +1.40 | 0.020 | 5 | -1.72 / -3.12 | `day_max(Open)` |
| +1.40 | 0.020 | 5 | -1.72 / -3.12 | `pow_3(day_max(Open))` |
| +1.37 | 0.022 | 5 | -1.75 / -3.12 | `day_max(Low)` |
| +1.26 | 0.000 | 24 | -2.03 / -3.29 | `day_sum(abs_(in_slice(Ret, 211, 240)))` |
| +1.26 | 0.038 | 5 | -1.86 / -3.12 | `sub(day_last(Close), day_open(Open))` |
| +1.21 | 0.006 | 12 | -1.96 / -3.18 | `day_median(cross_ema(Vwap, 15))` |
| +1.14 | 0.061 | 5 | -1.97 / -3.11 | `ts_sum(sub(div(day_last(Close), day_open(Open)), 1), 40)` |
| +0.85 | 0.056 | 12 | -2.29 / -3.15 | `sigmoid(LimitWidth)` |
| +0.75 | 0.000 | 53 | -2.61 / -3.36 | `day_sum(abs_(in_slice(Ret, 1, 30)))` |
| +0.56 | 0.150 | 7 | -2.54 / -3.10 | `div(day_last(Close), day_open(Open))` |
| +0.52 | 0.088 | 32 | -2.68 / -3.19 | `day_last(Close)` |
| +0.38 | 0.177 | 32 | -2.78 / -3.16 | `day_open(Open)` |
| -0.06 | 0.680 | 20 | -3.13 / -3.06 | `cross_delay(day_last(Close), 1)` |
| -0.65 | 0.974 | 14 | -3.66 / -3.01 | `div(day_open(Open), cross_delay(day_last(Close), 1))` |

## 拆解(10 次评估)

### head score -2.66:`day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open, 3), Volume, 60), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Open->Close` | -2.46 | -2.20 | -2.46 | — | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Close, 3), Volume, 60), 241))` |
| swap | `Volume->Amt` | -1.73 | -1.73 | -0.35 | — | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open, 3), Amt, 60), 241))` |
| window | `cross_quantile_q50@241->120` | -3.34 | -1.92 | -3.34 | — | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open, 3), Volume, 60), 120))` |
| window | `cross_quantile_q50@241->482` | -3.28 | -2.09 | -3.28 | — | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open, 3), Volume, 60), 482))` |

### head score -3.54:`day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Volume, 21)), 5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.59 | -3.59 | -3.16 | — | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Amt, 21)), 5))` |
| window | `in_delay@5->2` | -4.01 | -4.01 | -4.00 | — | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Volume, 21)), 2))` |
| window | `in_delay@5->10` | -3.92 | -3.92 | -3.44 | — | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Volume, 21)), 10))` |

### head score -3.59:`day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Amt, 21)), 5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -3.54 | -3.54 | -3.16 | — | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Volume, 21)), 5))` |
| window | `in_delay@5->2` | -4.03 | -3.90 | -4.03 | — | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Amt, 21)), 2))` |
| window | `in_delay@5->10` | -4.06 | -4.06 | -3.52 | — | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Amt, 21)), 10))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_median(Ret)` — enrichment,均值差 +1.96,p 0.001
2. `pow_3(day_max(Low))` — enrichment,均值差 +1.56,p 0.015
3. `ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10)` — enrichment,均值差 +1.52,p 0.000
4. `day_max(Open)` — enrichment,均值差 +1.40,p 0.020
5. `pow_3(day_max(Open))` — enrichment,均值差 +1.40,p 0.020
6. `day_max(Low)` — enrichment,均值差 +1.37,p 0.022
7. `day_sum(abs_(in_slice(Ret, 211, 240)))` — enrichment,均值差 +1.26,p 0.000
8. `sub(day_last(Close), day_open(Open))` — enrichment,均值差 +1.26,p 0.038
9. `day_median(cross_ema(Vwap, 15))` — enrichment,均值差 +1.21,p 0.006
10. `ts_sum(sub(div(day_last(Close), day_open(Open)), 1), 40)` — enrichment,均值差 +1.14,p 0.061
11. `sigmoid(LimitWidth)` — enrichment,均值差 +0.85,p 0.056
12. `day_sum(abs_(in_slice(Ret, 1, 30)))` — enrichment,均值差 +0.75,p 0.000
13. `day_last(Close)` — enrichment,均值差 +0.52,p 0.088

## 本组之前各轮的任务

- `prods2068Pr1a_Ea`:核心 `day_sum(abs_(in_slice(Ret, 1, 30)))`;评分 92,过线 0,入 heads 0;采样计数 {'c05_no_core': 1557, 'c05_skeleton': 896}
  - score -0.86(train -0.86 valid -0.41):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_median(cross_ema(Vwap, 10)), 30)`
  - score -0.93(train -0.93 valid -0.75):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_median(cross_ema(Vwap, 15)), 30)`
  - score -1.02(train -1.02 valid -0.63):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_quantile_q75(cross_ema(Vwap, 15)), 30)`
  - score -1.12(train -1.12 valid -0.65):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_median(Ret), 30)`
  - score -1.12(train -1.12 valid -0.65):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(abs_(in_slice(Ret, 211, 240)))), 10), day_median(Ret), 30)`
- `prods2068Pr1b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.79(train -0.79 valid -0.78):`cs_bucket_demean(day_last(Close), cross_delay(day_last(Close), 1))`
  - score -0.99(train -0.85 valid -0.99):`cs_bucket_demean(cross_delay(day_last(Close), 1), day_open(Open))`
  - score -1.13(train -0.68 valid -1.13):`cs_bucket_demean(pow_3(ts_sum(sub(sub(day_last(Close), day_open(Open)), 1), 40)), sigmoid(LimitWidth))`
  - score -1.13(train -0.66 valid -1.13):`cs_bucket_demean(pow_3(ts_sum(sub(sub(day_last(Close), day_open(Close)), 1), 40)), sigmoid(LimitWidth))`
  - score -1.21(train -1.21 valid -1.19):`cs_bucket_demean(pow_3(day_max(Low)), day_open(Open))`

## 比原 head 好的拆解变体(R 候选)

(没有)
