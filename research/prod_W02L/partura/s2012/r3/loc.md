# 定位:种子 2012,P 组,第 3 轮(只含 train / valid)

快照:prods2012M1_I0_open_search, prods2012M2_I0_open_search, prods2012M3_I0_open_search, prods2012Pr1a_Ea, prods2012Pr1b_Nb, prods2012Pr2a_Ea, prods2012Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.54 | -1.54 | -0.53 | +1 | 20 | prods2012M2_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(in_slice(Vwap, 30, 210)), 120)` |
| -1.80 | -1.53 | -1.80 | +1 | 0 | prods2012M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(day_ar1_coefficient(Volume), 50), 50)` |
| -1.99 | -1.96 | -1.99 | +1 | 20 | prods2012M2_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(Volume), 50)` |
| -2.66 | -2.66 | -2.52 | +1 | 20 | prods2012M1_I0_open_search | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20)), 5)` |
| -2.67 | -2.48 | -2.67 | +1 | 20 | prods2012M3_I0_open_search | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| -2.78 | -2.78 | -2.61 | +1 | 20 | prods2012M3_I0_open_search | `ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Volume))), 10)` |
| -2.89 | -2.69 | -2.89 | +1 | 20 | prods2012M3_I0_open_search | `ts_decay_linear(pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5))), 5)` |
| -3.01 | -2.83 | -3.01 | +1 | 20 | prods2012M1_I0_open_search | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)))` |
| -3.02 | -2.84 | -3.02 | +1 | 20 | prods2012M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)` |

## 共性:268 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.55 | 0.001 | 5 | -0.75 / -2.29 | `cs_last_high20(cs_last_high40(sub(LogFloatCap, LogFloatShares), inv(ListAge)), cross_max(day_zero_ratio(Ret), 3))` |
| +1.32 | 0.001 | 8 | -0.98 / -2.31 | `cs_last_high40(sub(LogFloatCap, LogFloatShares), inv(ListAge))` |
| +1.23 | 0.000 | 77 | -1.39 / -2.62 | `inv(ListAge)` |
| +1.21 | 0.000 | 25 | -1.17 / -2.38 | `sub(LogFloatCap, LogFloatShares)` |
| +1.15 | 0.001 | 9 | -1.16 / -2.30 | `cross_max(day_zero_ratio(Ret), 3)` |
| +1.14 | 0.000 | 11 | -1.17 / -2.31 | `neg(cross_mean(cs_winsor(day_es_ratio_hi(Open)), 60))` |
| +1.14 | 0.000 | 12 | -1.17 / -2.32 | `cross_mean(cs_winsor(day_es_ratio_hi(Open)), 60)` |
| +1.06 | 0.004 | 8 | -1.24 / -2.30 | `cs_winsor(day_at_max_ratio(Open))` |
| +1.05 | 0.001 | 11 | -1.25 / -2.31 | `day_at_max_ratio(Open)` |
| +1.02 | 0.000 | 20 | -1.32 / -2.34 | `cs_winsor(day_es_ratio_hi(Open))` |
| +1.02 | 0.000 | 30 | -1.36 / -2.38 | `day_zero_ratio(Ret)` |
| +1.00 | 0.000 | 29 | -1.37 / -2.37 | `div(day_open(Open), ts_delay(day_last(Close), 1))` |
| +1.00 | 0.013 | 6 | -1.29 / -2.29 | `sub(LogTotalCap, LogFloatCap)` |
| +0.95 | 0.000 | 36 | -1.44 / -2.39 | `day_open(Open)` |
| +0.93 | 0.000 | 25 | -1.42 / -2.35 | `day_es_ratio_hi(Open)` |
| +0.93 | 0.000 | 16 | -1.39 / -2.32 | `cross_max(day_zero_ratio(Ret), 15)` |
| +0.92 | 0.047 | 4 | -1.36 / -2.28 | `neg(cross_mean(cs_winsor(day_at_max_ratio(Open)), 60))` |
| +0.86 | 0.000 | 40 | -1.54 / -2.39 | `day_last(Close)` |
| +0.85 | 0.015 | 7 | -1.44 / -2.29 | `cross_mean(cs_winsor(sub(div(day_last(Close), day_open(Open)), 1)), 120)` |
| +0.82 | 0.053 | 5 | -1.46 / -2.28 | `cross_mean(cs_winsor(day_at_max_ratio(Open)), 60)` |

## 拆解(32 次评估)

### head score -1.54:`ts_quantile_q75(day_ar1_coefficient(in_slice(Vwap, 30, 210)), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(in_slice(Vwap, 30, 210))` | -2.48 | -2.48 | -2.44 | — | (子树本身) |
| swap | `Vwap->Close` | -2.07 | -2.06 | -2.07 | — | `ts_quantile_q75(day_ar1_coefficient(in_slice(Close, 30, 210)), 120)` |
| window | `ts_quantile_q75@120->60` | -1.62 | -1.62 | -0.63 | — | `ts_quantile_q75(day_ar1_coefficient(in_slice(Vwap, 30, 210)), 60)` |
| window | `ts_quantile_q75@120->240` | -1.38 | -1.38 | -0.51 | — | `ts_quantile_q75(day_ar1_coefficient(in_slice(Vwap, 30, 210)), 240)` |

### head score -2.67:`ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| knockout | `sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))))` | -2.64 | -2.45 | -2.64 | -0.03 | `ts_decay_linear(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| knockout | `pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.00 | -2.62 | -3.00 | +0.32 | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| swap | `Volume->Amt` | -2.74 | -2.43 | -2.74 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Amt)))))), 5)` |
| window | `ts_decay_linear@5->2` | -3.22 | -2.60 | -3.22 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 2)` |
| window | `ts_decay_linear@5->10` | -2.65 | -2.60 | -2.65 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 10)` |

### head score -2.78:`ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Volume))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -2.76 | -2.76 | -2.58 | -0.02 | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 10)` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -2.81 | -2.81 | -2.57 | +0.03 | `ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 10)` |
| swap | `Volume->Amt` | -2.84 | -2.84 | -2.57 | — | `ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Amt))), 10)` |
| window | `ts_quantile_q75@10->5` | -2.87 | -2.81 | -2.87 | — | `ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)` |
| window | `ts_quantile_q75@10->20` | -2.72 | -2.72 | -2.34 | — | `ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Volume))), 20)` |

### head score -2.89:`ts_decay_linear(pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)))` | -3.01 | -2.66 | -3.01 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5))` | -3.01 | -2.66 | -3.01 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)` | -3.01 | -2.66 | -3.01 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| knockout | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)))` | -3.00 | -2.74 | -3.00 | +0.11 | `ts_decay_linear(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)), 5)` |
| knockout | `cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5))` | -2.90 | -2.69 | -2.90 | +0.02 | `ts_decay_linear(pow_2(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)), 5)` |
| knockout | `ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)` | -3.14 | -2.64 | -3.14 | +0.26 | `ts_decay_linear(pow_2(cs_rank(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| knockout | `pow_2(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.08 | -2.81 | -3.08 | +0.19 | `ts_decay_linear(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))), 5)` |
| swap | `Volume->Amt` | -2.96 | -2.70 | -2.96 | — | `ts_decay_linear(pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Amt)))), 5))), 5)` |
| window | `ts_decay_linear@5->2` | -3.05 | -2.69 | -3.05 | — | `ts_decay_linear(pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5))), 2)` |
| window | `ts_decay_linear@5->10` | -2.87 | -2.83 | -2.87 | — | `ts_decay_linear(pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5))), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_high20(cs_last_high40(sub(LogFloatCap, LogFloatShares), inv(ListAge)), cross_max(day_zero_ratio(Ret), 3))` — enrichment,均值差 +1.55,p 0.001
2. `cs_last_high40(sub(LogFloatCap, LogFloatShares), inv(ListAge))` — enrichment,均值差 +1.32,p 0.001
3. `inv(ListAge)` — enrichment,均值差 +1.23,p 0.000
4. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +1.21,p 0.000
5. `cross_max(day_zero_ratio(Ret), 3)` — enrichment,均值差 +1.15,p 0.001
6. `neg(cross_mean(cs_winsor(day_es_ratio_hi(Open)), 60))` — enrichment,均值差 +1.14,p 0.000
7. `cross_mean(cs_winsor(day_es_ratio_hi(Open)), 60)` — enrichment,均值差 +1.14,p 0.000
8. `cs_winsor(day_at_max_ratio(Open))` — enrichment,均值差 +1.06,p 0.004
9. `day_at_max_ratio(Open)` — enrichment,均值差 +1.05,p 0.001
10. `cs_winsor(day_es_ratio_hi(Open))` — enrichment,均值差 +1.02,p 0.000
11. `day_zero_ratio(Ret)` — enrichment,均值差 +1.02,p 0.000
12. `div(day_open(Open), ts_delay(day_last(Close), 1))` — enrichment,均值差 +1.00,p 0.000
13. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +1.00,p 0.013
14. `day_open(Open)` — enrichment,均值差 +0.95,p 0.000
15. `day_es_ratio_hi(Open)` — enrichment,均值差 +0.93,p 0.000
16. `cross_max(day_zero_ratio(Ret), 15)` — enrichment,均值差 +0.93,p 0.000
17. `neg(cross_mean(cs_winsor(day_at_max_ratio(Open)), 60))` — enrichment,均值差 +0.92,p 0.047
18. `day_last(Close)` — enrichment,均值差 +0.86,p 0.000
19. `cross_mean(cs_winsor(sub(div(day_last(Close), day_open(Open)), 1)), 120)` — enrichment,均值差 +0.85,p 0.015
20. `cross_mean(cs_winsor(day_at_max_ratio(Open)), 60)` — enrichment,均值差 +0.82,p 0.053
21. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +0.81,p 0.000
22. `cs_winsor(sub(div(day_last(Close), day_open(Open)), 1))` — enrichment,均值差 +0.80,p 0.005
23. `cs_winsor(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1))` — enrichment,均值差 +0.76,p 0.009
24. `cross_mean(cs_winsor(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1)), 120)` — enrichment,均值差 +0.74,p 0.036
25. `div(day_last(Close), day_open(Open))` — enrichment,均值差 +0.74,p 0.003

## 本组之前各轮的任务

- `prods2012Pr1a_Ea`:核心 `day_ar1_coefficient(Volume)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 1062, 'c05_skeleton': 493}
  - score -1.36(train -1.29 valid -1.36):`cross_zscore(cross_ema(cross_ema(day_ar1_coefficient(Volume), 5), 5), 120)`
  - score -1.41(train -1.41 valid -0.97):`cross_corr(day_ar1_coefficient(Volume), ts_delay(day_sum(Ret), 1), 40)`
  - score -1.44(train -0.93 valid -1.44):`cross_regbeta(day_sum(Ret), day_ar1_coefficient(Volume), 60)`
  - score -1.51(train -1.51 valid -1.51):`cross_zscore(cross_ema(cross_corr(day_ar1_coefficient(Volume), ts_delay(day_sum(Ret), 1), 40), 5), 120)`
  - score -1.58(train -1.58 valid -0.19):`cross_corr(day_ar1_coefficient(Volume), abs_(day_sum(Ret)), 60)`
- `prods2012Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.97(train -0.85 valid -0.97):`mul(inv(ListAge), ts_quantile_q75(day_sum(Ret), 30))`
  - score -1.10(train -1.10 valid -0.72):`mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), cs_winsor(day_es_ratio_hi(Open)))`
  - score -1.10(train -1.10 valid -0.70):`mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), ts_rank(cross_stddev(LogTotalCap, 15), 1))`
  - score -1.11(train -1.11 valid -0.71):`mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), cs_winsor(day_es_ratio_hi(Open))))`
  - score -1.11(train -1.11 valid -0.70):`mul(mul(inv(ListAge), day_es_ratio_hi(Close)), day_es_ratio_hi(Close))`
- `prods2012Pr2a_Ea`:核心 `inv(ListAge)`;评分 108,过线 0,入 heads 0;采样计数 {'c05_no_core': 1654, 'c05_skeleton': 815, 'c05_periphery_seen': 5}
  - score -0.33(train -0.33 valid +0.59):`cs_last_high40(cs_last_high20(neg(cross_mean(cs_winsor(LogFloatShares), 60)), LogFloatCap), inv(ListAge))`
  - score -0.37(train -0.37 valid +0.39):`cs_last_high40(cs_last_high20(ts_decay_linear(mul(day_durbin_watson(Vwap), day_distinct_ratio(Close)), 40), LogFloatCap), inv(ListAge))`
  - score -0.42(train -0.42 valid +0.61):`cs_last_high40(cs_last_high20(neg(cross_mean(cs_winsor(day_at_max_ratio(Open)), 60)), LogFloatCap), inv(ListAge))`
  - score -0.42(train -0.42 valid +0.18):`cs_last_high40(sub(cs_last_high40(cs_last_high20(cs_last_high40(sub(LogFloatCap, LogFloatShares), inv(ListAge)), cross_max(day_zero_ratio(Ret), 3)), inv(ListAge)), LogFloatShares), inv(ListAge))`
  - score -0.42(train -0.42 valid +0.18):`cs_last_high40(sub(cs_last_high40(cs_last_high20(cs_last_high20(cs_last_high40(sub(LogFloatCap, LogFloatShares), inv(ListAge)), cross_max(day_zero_ratio(Ret), 3)), cross_max(day_zero_ratio(Ret), 3)), inv(ListAge)), LogFloatShares), inv(ListAge))`
- `prods2012Pr2b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.19(train -0.19 valid -0.16):`cross_mean(div(signedpower(div(abs_(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1)), LimitWidth)), LimitWidth), 120)`
  - score -0.38(train -0.38 valid +0.22):`cross_mean(div(abs_(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1)), LimitWidth), 120)`
  - score -0.38(train -0.38 valid +0.22):`abs_(cross_mean(div(abs_(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1)), LimitWidth), 120))`
  - score -0.74(train -0.74 valid -0.07):`cross_mean(div(abs_(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), day_es_ratio_hi(Vwap))), LimitWidth), 120)`
  - score -0.80(train -0.80 valid -0.20):`cross_mean(div(div(abs_(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1)), LimitWidth), LimitWidth), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.16(window ts_quantile_q75@120->240):`ts_quantile_q75(day_ar1_coefficient(in_slice(Vwap, 30, 210)), 240)`
