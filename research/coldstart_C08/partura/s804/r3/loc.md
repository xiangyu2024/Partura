# 定位:种子 804,P 组,第 3 轮(只含 train / valid)

快照:c07s804M1_I0_open_search, c07s804M2_I0_open_search, c07s804M3_I0_open_search, c08s804Pr1a_Ea, c08s804Pr1b_Nb, c08s804Pr2a_I0_open_search, c08s804Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.33 | +1.33 | +2.60 | +1 | 0 | c08s804Pr1a_Ea | `cs_last_high20(cs_last_high10(sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap), ts_max(ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60), 60)), sub(LogTotalCap, LogFloatCap))` |
| +1.28 | +1.28 | +1.28 | -1 | 20 | c07s804M3_I0_open_search | `day_mean(in_logchg(Amt, 30))` |
| +0.59 | +0.59 | +0.68 | +1 | 20 | c08s804Pr1b_Nb | `sub(log(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)), log(cross_stddev(log(div(day_last(Close), day_first(Open))), 20)))` |

## 共性:530 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.32 | 0.000 | 6 | +1.07 / -1.25 | `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` |
| +1.40 | 0.000 | 13 | +0.14 / -1.26 | `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` |
| +1.32 | 0.000 | 31 | +0.02 / -1.30 | `sub(LogTotalCap, LogFloatCap)` |
| +1.31 | 0.000 | 16 | +0.04 / -1.26 | `ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)` |
| +1.28 | 0.000 | 18 | +0.02 / -1.27 | `ts_mean(day_distinct_ratio(Vwap), 20)` |
| +1.28 | 0.000 | 18 | +0.02 / -1.27 | `day_distinct_ratio(Vwap)` |
| +1.26 | 0.000 | 18 | -0.00 / -1.26 | `mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10))` |
| +1.20 | 0.004 | 5 | -0.04 / -1.23 | `day_last(Low)` |
| +1.11 | 0.015 | 5 | -0.12 / -1.23 | `pow_1_5(pow_1_5(LogFloatShares))` |
| +1.10 | 0.003 | 4 | -0.13 / -1.23 | `sigmoid(sigmoid(day_kurt(Ret)))` |
| +1.02 | 0.002 | 11 | -0.22 / -1.24 | `pow_1_5(LogFloatShares)` |
| +0.95 | 0.000 | 19 | -0.31 / -1.26 | `day_kurt(Ret)` |
| +0.95 | 0.004 | 6 | -0.29 / -1.23 | `cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60))` |
| +0.92 | 0.000 | 12 | -0.33 / -1.24 | `sigmoid(day_kurt(Ret))` |
| +0.91 | 0.004 | 6 | -0.32 / -1.23 | `cross_quantile_q50(ts_var(LogFloatShares, 10), 3)` |
| +0.90 | 0.001 | 9 | -0.34 / -1.24 | `cross_delay(day_signed_ratio(High, High), 60)` |
| +0.89 | 0.000 | 16 | -0.35 / -1.25 | `day_signed_ratio(High, High)` |
| +0.89 | 0.005 | 6 | -0.34 / -1.23 | `day_signed_ratio(High, Low)` |
| +0.89 | 0.017 | 4 | -0.34 / -1.23 | `cross_delay(day_signed_ratio(Low, Low), 60)` |
| +0.89 | 0.017 | 4 | -0.34 / -1.23 | `ts_product(day_signed_ratio(Low, Low), 10)` |

## 拆解(3 次评估)

### head score +1.28:`day_mean(in_logchg(Amt, 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | +1.25 | +1.25 | +1.27 | — | `day_mean(in_logchg(Volume, 30))` |
| window | `in_logchg@30->15` | +1.11 | +1.11 | +1.58 | — | `day_mean(in_logchg(Amt, 15))` |
| window | `in_logchg@30->60` | +0.22 | +1.56 | +0.22 | — | `day_mean(in_logchg(Amt, 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), LogFloatCap)` — enrichment,均值差 +2.32,p 0.000
2. `ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10)` — enrichment,均值差 +1.40,p 0.000
3. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +1.32,p 0.000
4. `ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60)` — enrichment,均值差 +1.31,p 0.000
5. `ts_mean(day_distinct_ratio(Vwap), 20)` — enrichment,均值差 +1.28,p 0.000
6. `day_distinct_ratio(Vwap)` — enrichment,均值差 +1.28,p 0.000
7. `mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10))` — enrichment,均值差 +1.26,p 0.000
8. `day_last(Low)` — enrichment,均值差 +1.20,p 0.004
9. `pow_1_5(pow_1_5(LogFloatShares))` — enrichment,均值差 +1.11,p 0.015
10. `sigmoid(sigmoid(day_kurt(Ret)))` — enrichment,均值差 +1.10,p 0.003
11. `pow_1_5(LogFloatShares)` — enrichment,均值差 +1.02,p 0.002
12. `day_kurt(Ret)` — enrichment,均值差 +0.95,p 0.000
13. `cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), ts_var(LogFloatShares, 10)), 60))` — enrichment,均值差 +0.95,p 0.004
14. `sigmoid(day_kurt(Ret))` — enrichment,均值差 +0.92,p 0.000
15. `cross_quantile_q50(ts_var(LogFloatShares, 10), 3)` — enrichment,均值差 +0.91,p 0.004
16. `cross_delay(day_signed_ratio(High, High), 60)` — enrichment,均值差 +0.90,p 0.001
17. `day_signed_ratio(High, High)` — enrichment,均值差 +0.89,p 0.000
18. `day_signed_ratio(High, Low)` — enrichment,均值差 +0.89,p 0.005
19. `cross_delay(day_signed_ratio(Low, Low), 60)` — enrichment,均值差 +0.89,p 0.017
20. `ts_product(day_signed_ratio(Low, Low), 10)` — enrichment,均值差 +0.89,p 0.017
21. `pow_2_5(cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(day_signed_ratio(Low, Low), 10)))` — enrichment,均值差 +0.88,p 0.023
22. `day_signed_ratio(Low, High)` — enrichment,均值差 +0.86,p 0.007
23. `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(day_signed_ratio(Low, Low), 10))` — enrichment,均值差 +0.86,p 0.003
24. `cross_delay(day_signed_ratio(High, High), 30)` — enrichment,均值差 +0.85,p 0.016
25. `ts_stddev(day_signed_ratio(Low, High), 10)` — enrichment,均值差 +0.84,p 0.021
26. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.84,p 0.000
27. `day_signed_ratio(Open, Low)` — enrichment,均值差 +0.83,p 0.053
28. `ts_stddev(day_signed_ratio(Open, Low), 10)` — enrichment,均值差 +0.83,p 0.053
29. `day_signed_ratio(High, Open)` — enrichment,均值差 +0.74,p 0.000
30. `cs_last_high20(day_pos_ratio(Open), cs_normalize(BoardCode))` — enrichment,均值差 +0.73,p 0.058
31. `cross_delay(day_signed_ratio(High, Open), 60)` — enrichment,均值差 +0.71,p 0.000
32. `sub(LogFloatShares, LogFloatCap)` — enrichment,均值差 +0.71,p 0.000
33. `pow_05(LogFloatShares)` — enrichment,均值差 +0.69,p 0.096
34. `day_pos_ratio(Open)` — enrichment,均值差 +0.68,p 0.009
35. `cs_last_high10(sub(LogFloatShares, LogFloatCap), ts_max(mul(ts_var(LogFloatShares, 10), is_gt(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 1e-08)), 60))` — enrichment,均值差 +0.66,p 0.077
36. `is_gt(ts_var(ts_mean(day_distinct_ratio(Vwap), 20), 10), 1e-08)` — enrichment,均值差 +0.58,p 0.043
37. `day_flat_run_max(Amt)` — enrichment,均值差 +0.52,p 0.052
38. `day_signed_ratio(Low, Low)` — enrichment,均值差 +0.48,p 0.003
39. `ts_stddev(day_signed_ratio(Low, Low), 10)` — enrichment,均值差 +0.38,p 0.042

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
- `c08s804Pr2a_I0_open_search`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {}
  - score -0.00(train -0.00 valid +0.43):`cs_mask_top_replace_mean_neg(day_kurt(Ret))`
  - score -0.04(train -0.04 valid +0.42):`sigmoid(cs_mask_top_replace_mean_neg(day_kurt(Ret)))`
  - score -0.05(train -0.05 valid +0.73):`cs_mask_top_replace_mean_neg(sigmoid(day_kurt(Ret)))`
  - score -0.06(train -0.06 valid +0.74):`sigmoid(cs_mask_top_replace_mean_neg(sigmoid(day_kurt(Ret))))`
  - score -0.06(train -0.06 valid +0.69):`cs_mask_top_replace_mean_neg(sigmoid(sigmoid(sigmoid(day_kurt(Ret)))))`
- `c08s804Pr2b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {}
  - score +0.47(train +0.47 valid +1.65):`cs_first_low20(pow_1_5(LogFloatShares), LogTotalCap)`
  - score +0.47(train +0.47 valid +1.65):`cs_first_low20(pow_1_5(pow_1_5(LogFloatShares)), LogTotalCap)`
  - score +0.47(train +0.47 valid +1.65):`cs_first_low20(cs_first_low20(pow_1_5(pow_1_5(LogFloatShares)), LogTotalCap), LogTotalCap)`
  - score +0.47(train +0.47 valid +1.65):`cs_first_low20(pow_05(cs_first_low20(pow_1_5(LogFloatShares), LogTotalCap)), LogTotalCap)`
  - score +0.47(train +0.47 valid +1.65):`cs_first_low20(pow_1_5(cs_first_low20(pow_1_5(pow_1_5(LogFloatShares)), LogTotalCap)), LogTotalCap)`

## 比原 head 好的拆解变体(R 候选)

(没有)
