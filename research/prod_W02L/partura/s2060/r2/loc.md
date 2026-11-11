# 定位:种子 2060,P 组,第 2 轮(只含 train / valid)

快照:prods2060M1_I0_open_search, prods2060M2_I0_open_search, prods2060Pr1a_Ea, prods2060Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.00 | -1.84 | -2.00 | -1 | 20 | prods2060M2_I0_open_search | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5))))` |
| -2.02 | -1.40 | -2.02 | -1 | 20 | prods2060M2_I0_open_search | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5)))` |
| -2.21 | -2.21 | -1.49 | +1 | 20 | prods2060M2_I0_open_search | `day_argmax(cross_max(nt_ts_skew(Vwap, 15), 241))` |
| -3.05 | -3.05 | -2.35 | +1 | 5 | prods2060M1_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))), 5)` |
| -3.11 | -2.86 | -3.11 | +1 | 20 | prods2060M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))), 5)` |
| -3.17 | -2.89 | -3.17 | +1 | 20 | prods2060M1_I0_open_search | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)), 5)` |

## 共性:105 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.96 | 0.069 | 4 | -1.66 / -2.61 | `sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60))` |
| +0.94 | 0.043 | 5 | -1.69 / -2.62 | `cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60)` |
| +0.93 | 0.000 | 21 | -1.84 / -2.76 | `cs_quantile_q75(LogFloatCap)` |
| +0.88 | 0.015 | 9 | -1.77 / -2.65 | `day_std(Ret)` |
| +0.82 | 0.043 | 14 | -1.86 / -2.69 | `day_at_max_ratio(Open)` |
| +0.82 | 0.001 | 13 | -1.86 / -2.68 | `sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap))` |
| +0.74 | 0.000 | 48 | -2.18 / -2.92 | `day_ar1_coefficient(Volume)` |
| +0.61 | 0.247 | 6 | -2.00 / -2.61 | `cross_autocorr_s1(day_at_max_ratio(Open), 15)` |
| -0.63 | 0.940 | 5 | -3.18 / -2.55 | `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` |
| -0.63 | 0.940 | 5 | -3.18 / -2.55 | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` |

## 拆解(19 次评估)

### head score -2.00:`pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5)))` | -2.08 | -1.84 | -2.08 | — | (子树本身) |
| sufficiency | `day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5))` | -2.04 | -1.87 | -2.04 | — | (子树本身) |
| knockout | `pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5)))` | -2.04 | -1.87 | -2.04 | +0.04 | `pow_2(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5)))` |
| swap | `Volume->Amt` | -2.02 | -1.88 | -2.02 | — | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Amt, 3), 10), 3), 5))))` |
| window | `cross_corr@5->2` | — | — | — | — | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 2))))` |
| window | `cross_corr@5->10` | -3.61 | -2.42 | -3.61 | — | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 10))))` |

### head score -2.02:`pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5))` | -1.97 | -1.40 | -1.97 | — | (子树本身) |
| sufficiency | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5)` | -1.97 | -1.40 | -1.97 | — | (子树本身) |
| sufficiency | `sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3))))` | -1.97 | -1.61 | -1.97 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))` | -1.98 | -1.60 | -1.98 | — | (子树本身) |
| knockout | `cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5))` | -1.97 | -1.40 | -1.97 | -0.04 | `pow_2(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5))` |
| knockout | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5)` | -1.97 | -1.60 | -1.97 | -0.04 | `pow_2(cs_rank(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3))))))` |
| knockout | `sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3))))` | -1.96 | -1.41 | -1.96 | -0.06 | `pow_2(cs_rank(ts_decay_linear(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3))), 5)))` |
| knockout | `pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))` | -1.98 | -1.39 | -1.98 | -0.04 | `pow_2(cs_rank(ts_decay_linear(sigmoid(day_ar1_coefficient(nt_ts_skew(Ret, 3))), 5)))` |
| window | `ts_decay_linear@5->2` | -2.00 | -1.50 | -2.00 | — | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 2)))` |
| window | `ts_decay_linear@5->10` | -2.02 | -1.34 | -2.02 | — | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 10)))` |

### head score -2.21:`day_argmax(cross_max(nt_ts_skew(Vwap, 15), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | — | — | — | — | `day_argmax(cross_max(nt_ts_skew(Close, 15), 241))` |
| window | `cross_max@241->120` | — | — | — | — | `day_argmax(cross_max(nt_ts_skew(Vwap, 15), 120))` |
| window | `cross_max@241->482` | — | — | — | — | `day_argmax(cross_max(nt_ts_skew(Vwap, 15), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60))` — enrichment,均值差 +0.96,p 0.069
2. `cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60)` — enrichment,均值差 +0.94,p 0.043
3. `day_std(Ret)` — enrichment,均值差 +0.88,p 0.015
4. `day_at_max_ratio(Open)` — enrichment,均值差 +0.82,p 0.043
5. `sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap))` — enrichment,均值差 +0.82,p 0.001
6. `day_ar1_coefficient(Volume)` — enrichment,均值差 +0.74,p 0.000

## 本组之前各轮的任务

- `prods2060Pr1a_Ea`:核心 `day_ar1_coefficient(Volume)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_no_core': 2031, 'c05_skeleton': 1041}
  - score -0.36(train +0.15 valid -0.36):`sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap))`
  - score -0.39(train -0.39 valid -0.27):`cross_zscore(sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), 60)), 241)`
  - score -0.46(train -0.12 valid -0.46):`cross_zscore(sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), 60), 60)), 241)`
  - score -0.77(train -0.77 valid -0.54):`cross_zscore(sub(sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), cs_quantile_q75(LogFloatCap)), 241)`
  - score -0.85(train -0.85 valid -0.48):`cross_zscore(sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), 241)`
- `prods2060Pr1b_Nb`:核心 `—`;评分 52,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.07(train -0.07 valid +0.17):`neg(cross_autocorr_s1(day_at_max_ratio(Open), 15))`
  - score -0.07(train -0.07 valid +0.17):`neg(neg(cross_autocorr_s1(day_at_max_ratio(Open), 15)))`
  - score -0.07(train -0.07 valid +0.17):`cross_autocorr_s1(day_at_max_ratio(Open), 15)`
  - score -0.33(train -0.11 valid -0.33):`neg(cross_autocorr_s1(day_at_max_ratio(Low), 15))`
  - score -0.33(train -0.11 valid -0.33):`cross_autocorr_s1(day_at_max_ratio(Low), 15)`

## 比原 head 好的拆解变体(R 候选)

(没有)
