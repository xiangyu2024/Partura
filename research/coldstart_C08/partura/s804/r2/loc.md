# 定位:种子 804,P 组,第 2 轮(只含 train / valid)

快照:c07s804M1_I0_open_search, c07s804M2_I0_open_search, c08s804Pr1a_Ea, c08s804Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(2 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.33 | +1.33 | +2.60 | +1 | 0 | c08s804Pr1a_Ea | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| +0.59 | +0.59 | +0.68 | +1 | 20 | c08s804Pr1b_Nb | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |

## 共性:374 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.24 | 0.000 | 6 | +1.07 / -1.17 | `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` |
| +1.32 | 0.000 | 13 | +0.14 / -1.18 | `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` |
| +1.26 | 0.000 | 31 | +0.02 / -1.24 | `sub(LogTotalCap, LogFloatCap)` |
| +1.23 | 0.000 | 16 | +0.04 / -1.19 | `ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)` |
| +1.21 | 0.000 | 18 | +0.02 / -1.19 | `ts_mean(day_distinct_ratio(Vwap), 20)` |
| +1.21 | 0.000 | 18 | +0.02 / -1.19 | `day_distinct_ratio(Vwap)` |
| +1.19 | 0.000 | 18 | -0.00 / -1.19 | `mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10))` |
| +0.86 | 0.002 | 6 | -0.29 / -1.15 | `cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60))` |
| +0.83 | 0.002 | 6 | -0.32 / -1.15 | `cross_quantile_q50(ts_var(LogFloatShares, 10), 3)` |
| +0.82 | 0.000 | 9 | -0.34 / -1.15 | `cross_delay(day_signed_ratio(High, High), 60)` |
| +0.81 | 0.000 | 16 | -0.35 / -1.17 | `day_signed_ratio(High, High)` |
| +0.81 | 0.003 | 6 | -0.34 / -1.15 | `day_signed_ratio(High, Low)` |
| +0.80 | 0.013 | 4 | -0.34 / -1.14 | `cross_delay(day_signed_ratio(Low, Low), 60)` |
| +0.80 | 0.013 | 4 | -0.34 / -1.14 | `ts_product(day_signed_ratio(Low, Low), 10)` |
| +0.79 | 0.017 | 4 | -0.35 / -1.14 | `pow_2_5(cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(day_signed_ratio(Low, Low), 10)))` |
| +0.79 | 0.000 | 72 | -0.50 / -1.29 | `ts_var(LogFloatShares, 10)` |
| +0.77 | 0.002 | 9 | -0.38 / -1.15 | `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(day_signed_ratio(Low, Low), 10))` |
| +0.77 | 0.005 | 7 | -0.38 / -1.15 | `day_signed_ratio(Low, High)` |
| +0.77 | 0.015 | 7 | -0.38 / -1.15 | `cross_delay(day_signed_ratio(High, High), 30)` |
| +0.76 | 0.016 | 5 | -0.39 / -1.14 | `ts_stddev(day_signed_ratio(Low, High), 10)` |

## 拆解(23 次评估)

### head score +1.33:`cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60))` | -0.81 | +0.19 | -0.81 | — | (子树本身) |
| sufficiency | `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` | -5.07 | -3.55 | -5.07 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` | -1.58 | -1.37 | -1.58 | — | (子树本身) |
| knockout | `cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60))` | +1.18 | +1.18 | +2.50 | +0.15 | `cs_last_high20(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), sub(LogTotalCap, LogFloatCap))` |
| knockout | `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` | +0.50 | +0.50 | +1.14 | +0.83 | `cs_last_high20(cs_last_high10(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| knockout | `ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)` | +1.22 | +1.22 | +2.55 | +0.11 | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)), sub(LogTotalCap, LogFloatCap))` |
| knockout | `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` | +1.36 | +1.36 | +2.53 | -0.04 | `cs_last_high20(cs_last_high10(sub(ts_mean(day_distinct_ratio(Vwap), 20), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| swap | `Vwap->Close` | +1.33 | +1.33 | +2.60 | — | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Close), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| window | `ts_var@10->5` | +1.33 | +1.33 | +2.60 | — | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 5), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| window | `ts_var@10->20` | +1.33 | +1.33 | +2.58 | — | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 20), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |

### head score +0.59:`sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20))` | -0.56 | -0.56 | +0.23 | — | (子树本身) |
| sufficiency | `cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)` | -0.54 | -0.54 | +0.26 | — | (子树本身) |
| sufficiency | `log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20))` | -1.22 | -1.22 | -0.84 | — | (子树本身) |
| sufficiency | `log(div(day_first(Open), ts_delay(day_last(Close), 1)))` | -3.94 | -1.84 | -3.94 | — | (子树本身) |
| knockout | `log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20))` | -1.24 | -1.24 | -0.90 | +1.84 | `sub(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |
| knockout | `cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)` | — | — | — | — | `sub(log(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |
| knockout | `log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20))` | -0.62 | -0.62 | +0.17 | +1.22 | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), cross_stddev(log(div(day_last(Close), day_first(Open))), 20))` |
| knockout | `log(div(day_first(Open), ts_delay(day_last(Close), 1)))` | +0.69 | +0.69 | +0.78 | -0.09 | `sub(log(cross_stddev(div(day_first(Open), ts_delay(day_last(Close), 1)), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |
| swap | `Open->Close` | +0.61 | +0.61 | +0.68 | — | `sub(log(cross_stddev(log(div(day_first(Close), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Close))), 20)))` |
| swap | `Close->Vwap` | +0.50 | +0.50 | +0.77 | — | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Vwap), 1))), 20)), log(cross_stddev(log(div(day_last(Vwap), day_first(Open))), 20)))` |
| window | `cross_stddev@20->10` | -0.26 | +0.66 | -0.26 | — | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |
| window | `cross_stddev@20->40` | -0.00 | -0.00 | +0.15 | — | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 40)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` — enrichment,均值差 +2.24,p 0.000
2. `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` — enrichment,均值差 +1.32,p 0.000
3. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +1.26,p 0.000
4. `ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)` — enrichment,均值差 +1.23,p 0.000
5. `ts_mean(day_distinct_ratio(Vwap), 20)` — enrichment,均值差 +1.21,p 0.000
6. `day_distinct_ratio(Vwap)` — enrichment,均值差 +1.21,p 0.000
7. `mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10))` — enrichment,均值差 +1.19,p 0.000
8. `cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60))` — enrichment,均值差 +0.86,p 0.002
9. `cross_quantile_q50(ts_var(LogFloatShares, 10), 3)` — enrichment,均值差 +0.83,p 0.002
10. `cross_delay(day_signed_ratio(High, High), 60)` — enrichment,均值差 +0.82,p 0.000
11. `day_signed_ratio(High, High)` — enrichment,均值差 +0.81,p 0.000
12. `day_signed_ratio(High, Low)` — enrichment,均值差 +0.81,p 0.003
13. `cross_delay(day_signed_ratio(Low, Low), 60)` — enrichment,均值差 +0.80,p 0.013
14. `ts_product(day_signed_ratio(Low, Low), 10)` — enrichment,均值差 +0.80,p 0.013
15. `pow_2_5(cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(day_signed_ratio(Low, Low), 10)))` — enrichment,均值差 +0.79,p 0.017
16. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.79,p 0.000
17. `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(day_signed_ratio(Low, Low), 10))` — enrichment,均值差 +0.77,p 0.002
18. `day_signed_ratio(Low, High)` — enrichment,均值差 +0.77,p 0.005
19. `cross_delay(day_signed_ratio(High, High), 30)` — enrichment,均值差 +0.77,p 0.015
20. `ts_stddev(day_signed_ratio(Low, High), 10)` — enrichment,均值差 +0.76,p 0.016
21. `day_signed_ratio(Open, Low)` — enrichment,均值差 +0.74,p 0.049
22. `ts_stddev(day_signed_ratio(Open, Low), 10)` — enrichment,均值差 +0.74,p 0.049
23. `day_signed_ratio(High, Open)` — enrichment,均值差 +0.67,p 0.000
24. `cs_last_high20(day_pos_ratio(Open), cs_normalize(BoardCode))` — enrichment,均值差 +0.64,p 0.057
25. `cross_delay(day_signed_ratio(High, Open), 60)` — enrichment,均值差 +0.64,p 0.000
26. `sub(LogFloatShares, LogFloatCap)` — enrichment,均值差 +0.63,p 0.000
27. `day_pos_ratio(Open)` — enrichment,均值差 +0.60,p 0.011
28. `cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 1e-08)), 60))` — enrichment,均值差 +0.57,p 0.072
29. `is_gt(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 1e-08)` — enrichment,均值差 +0.49,p 0.037
30. `day_flat_run_max(Amt)` — enrichment,均值差 +0.43,p 0.040
31. `day_signed_ratio(Low, Low)` — enrichment,均值差 +0.40,p 0.003
32. `mul(ts_var(LogFloatShares, 10), is_gt(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 1e-08))` — enrichment,均值差 +0.39,p 0.097
33. `ts_stddev(day_signed_ratio(Low, Low), 10)` — enrichment,均值差 +0.30,p 0.048

## 本组之前各轮的任务

- `c08s804Pr1a_Ea`:核心 `ts_var(LogFloatShares, 10)`;评分 98,过线 8,入 heads 1;采样计数 {'c05_no_core': 1812, 'c05_periphery_seen': 1}
  - score +1.33(train +1.33 valid +2.60):`cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))`
  - score +1.23(train +1.23 valid +2.55):`cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_rank(LogFloatShares, 10)), 60)), sub(LogTotalCap, LogFloatCap)), 20), 10), LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_rank(LogFloatShares, 10)), 60)), sub(LogTotalCap, LogFloatCap))`
  - score +1.22(train +1.22 valid +2.56):`cs_last_high20(cs_last_high10(sub(ts_var(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 10), LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)), sub(LogTotalCap, LogFloatCap))`
  - score +1.22(train +1.22 valid +2.55):`cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)), sub(LogTotalCap, LogFloatCap))`
  - score +1.21(train +1.21 valid +2.56):`cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(mul(ts_var(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)), 10), ts_var(LogFloatShares, 10)), 60)), sub(LogTotalCap, LogFloatCap))`
- `c08s804Pr1b_Nb`:核心 `—`;评分 90,过线 1,入 heads 1;采样计数 {}
  - score +0.59(train +0.59 valid +0.68):`sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))`
  - score +0.44(train +0.78 valid +0.44):`sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_first(Open), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))`
  - score +0.04(train +0.04 valid +0.43):`cross_mean(div(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), add(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), abs_(log(div(day_last(Close), day_first(Open)))))), 20)`
  - score -0.04(train -0.04 valid +0.53):`sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(log(div(day_last(Close), day_first(Open))), day_first(Open))), 20)))`
  - score -0.23(train -0.23 valid +1.65):`cross_mean(div(day_first(Amt), day_sum(Amt)), 20)`

## 比原 head 好的拆解变体(R 候选)

(没有)
