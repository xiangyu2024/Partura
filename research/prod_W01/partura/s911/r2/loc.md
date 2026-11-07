# 定位:种子 911,P 组,第 2 轮(只含 train / valid)

快照:prods911M1_I0_open_search, prods911M2_I0_open_search, prods911Pr1a_Ea, prods911Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.19 | +1.19 | +3.16 | -1 | 5 | prods911M2_I0_open_search | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 10)), pow_2_5(day_wmean(Volume, Volume)))` |
| +0.83 | +0.83 | +2.25 | -1 | 0 | prods911Pr1b_Nb | `ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close)), 10)` |
| +0.82 | +0.82 | +2.56 | +1 | 5 | prods911Pr1b_Nb | `sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |

## 共性:348 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.70 | 0.000 | 7 | +0.67 / -1.02 | `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 40))` |
| +1.55 | 0.000 | 23 | +0.46 / -1.09 | `day_wmean(Volume, Volume)` |
| +1.55 | 0.000 | 22 | +0.46 / -1.09 | `pow_2_5(day_wmean(Volume, Volume))` |
| +1.40 | 0.010 | 4 | +0.39 / -1.01 | `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 50))` |
| +1.40 | 0.003 | 6 | +0.38 / -1.01 | `ts_quantile_q75(day_close(Open), 50)` |
| +1.26 | 0.005 | 5 | +0.25 / -1.01 | `cross_min(pow_2_5(day_wmean(Volume, Low)), 15)` |
| +1.24 | 0.005 | 5 | +0.23 / -1.01 | `ts_quantile_q75(pow_2_5(day_wmean(Volume, Volume)), 10)` |
| +1.12 | 0.000 | 13 | +0.09 / -1.03 | `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Open), 40))` |
| +1.05 | 0.021 | 4 | +0.05 / -1.00 | `cs_last_low20(pow_2_5(day_var(Open)), ts_quantile_q75(day_close(Volume), 40))` |
| +1.04 | 0.000 | 45 | -0.08 / -1.12 | `pow_2_5(day_wmean(Volume, Low))` |
| +1.01 | 0.000 | 34 | -0.08 / -1.09 | `ts_quantile_q75(day_close(Open), 40)` |
| +1.01 | 0.000 | 52 | -0.13 / -1.14 | `day_close(Open)` |
| +1.01 | 0.000 | 49 | -0.13 / -1.13 | `day_wmean(Volume, Low)` |
| +1.00 | 0.001 | 15 | -0.03 / -1.03 | `ts_quantile_q75(day_close(Low), 10)` |
| +0.98 | 0.001 | 13 | -0.04 / -1.03 | `cross_scale(cross_scale(LogFloatCap, 241), 241)` |
| +0.96 | 0.007 | 7 | -0.05 / -1.01 | `day_var(Open)` |
| +0.96 | 0.007 | 7 | -0.05 / -1.01 | `pow_2_5(day_var(Open))` |
| +0.91 | 0.002 | 16 | -0.12 / -1.03 | `day_close(Low)` |
| +0.86 | 0.018 | 6 | -0.14 / -1.00 | `cross_mean(day_sum(Amt), 60)` |
| +0.85 | 0.059 | 5 | -0.16 / -1.00 | `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Low), 10))` |

## 拆解(33 次评估)

### head score +1.19:`div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 10)), pow_2_5(day_wmean(Volume, Volume)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 10))` | -0.24 | -0.24 | +0.76 | — | (子树本身) |
| sufficiency | `pow_2_5(day_wmean(Volume, Volume))` | -1.83 | -0.12 | -1.83 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(day_close(Low), 10)` | -1.30 | -1.30 | -0.44 | — | (子树本身) |
| knockout | `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 10))` | — | — | — | — | `div(pow_2_5(day_wmean(Volume, Volume)), pow_2_5(day_wmean(Volume, Volume)))` |
| knockout | `pow_2_5(day_wmean(Volume, Volume))` | +1.19 | +1.19 | +3.16 | +0.00 | `div(cs_last_low20(day_wmean(Volume, Volume), ts_quantile_q75(day_close(Low), 10)), pow_2_5(day_wmean(Volume, Volume)))` |
| knockout | `ts_quantile_q75(day_close(Low), 10)` | +1.19 | +1.19 | +3.20 | -0.01 | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), day_close(Low)), pow_2_5(day_wmean(Volume, Volume)))` |
| knockout | `pow_2_5(day_wmean(Volume, Volume))` | -0.50 | +0.69 | -0.50 | +1.69 | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 10)), day_wmean(Volume, Volume))` |
| swap | `Volume->Amt` | +1.45 | +1.45 | +3.34 | — | `div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Low), 10)), pow_2_5(day_wmean(Amt, Amt)))` |
| swap | `Low->High` | +1.15 | +1.15 | +3.17 | — | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(High), 10)), pow_2_5(day_wmean(Volume, Volume)))` |
| window | `ts_quantile_q75@10->5` | +1.17 | +1.17 | +3.19 | — | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 5)), pow_2_5(day_wmean(Volume, Volume)))` |
| window | `ts_quantile_q75@10->20` | +1.14 | +1.14 | +3.16 | — | `div(cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Low), 20)), pow_2_5(day_wmean(Volume, Volume)))` |

### head score +0.83:`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close))` | +0.80 | +0.80 | +2.38 | — | (子树本身) |
| sufficiency | `neg(day_quantile_q75(Volume))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_last(Close)` | -1.34 | -1.34 | -0.41 | — | (子树本身) |
| knockout | `cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close))` | -0.33 | -0.33 | -0.04 | +1.16 | `ts_quantile_q25(neg(day_quantile_q75(Volume)), 10)` |
| knockout | `neg(day_quantile_q75(Volume))` | -0.10 | -0.10 | +0.82 | +0.93 | `ts_quantile_q25(cs_last_low20(day_quantile_q75(Volume), day_last(Close)), 10)` |
| swap | `Volume->Amt` | +0.87 | +0.87 | +2.55 | — | `ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Amt)), day_last(Close)), 10)` |
| swap | `Close->Vwap` | +0.84 | +0.84 | +2.24 | — | `ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Vwap)), 10)` |
| window | `ts_quantile_q25@10->5` | +0.81 | +0.81 | +2.32 | — | `ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close)), 5)` |
| window | `ts_quantile_q25@10->20` | +0.74 | +0.74 | +2.28 | — | `ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close)), 20)` |

### head score +0.82:`sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_first(Volume), cross_delay(day_last(Volume), 1))` | -0.46 | -0.46 | +1.73 | — | (子树本身) |
| sufficiency | `cross_delay(day_last(Volume), 1)` | -2.12 | -0.49 | -2.12 | — | (子树本身) |
| sufficiency | `div(day_last(Close), day_first(Open))` | -3.84 | -3.84 | -3.77 | — | (子树本身) |
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1)` | +0.82 | +0.82 | +2.56 | -0.00 | `sub(cross_mean(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| knockout | `div(day_first(Volume), cross_delay(day_last(Volume), 1))` | -0.35 | -0.35 | +0.71 | +1.17 | `sub(cross_mean(sub(day_first(Volume), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| knockout | `sub(div(day_last(Close), day_first(Open)), 1)` | +0.82 | +0.82 | +2.56 | -0.00 | `sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 60), cross_mean(div(day_last(Close), day_first(Open)), 60))` |
| knockout | `cross_delay(day_last(Volume), 1)` | +0.80 | +0.80 | +2.35 | +0.02 | `sub(cross_mean(sub(div(day_first(Volume), day_last(Volume)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| swap | `Volume->Amt` | +0.81 | +0.81 | +2.59 | — | `sub(cross_mean(sub(div(day_first(Amt), cross_delay(day_last(Amt), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| swap | `Close->Vwap` | +0.83 | +0.83 | +2.55 | — | `sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 60), cross_mean(sub(div(day_last(Vwap), day_first(Open)), 1), 60))` |
| window | `cross_mean@60->30` | +0.77 | +0.77 | +3.00 | — | `sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 30), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |
| window | `cross_mean@60->120` | +0.67 | +0.67 | +2.01 | — | `sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 120), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close))` — ablation,自身 score +0.80(所在 head +0.83)
2. `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 40))` — enrichment,均值差 +1.70,p 0.000
3. `day_wmean(Volume, Volume)` — enrichment,均值差 +1.55,p 0.000
4. `pow_2_5(day_wmean(Volume, Volume))` — enrichment,均值差 +1.55,p 0.000
5. `cs_last_low20(pow_2_5(day_wmean(Volume, Volume)), ts_quantile_q75(day_close(Open), 50))` — enrichment,均值差 +1.40,p 0.010
6. `ts_quantile_q75(day_close(Open), 50)` — enrichment,均值差 +1.40,p 0.003
7. `cross_min(pow_2_5(day_wmean(Volume, Low)), 15)` — enrichment,均值差 +1.26,p 0.005
8. `ts_quantile_q75(pow_2_5(day_wmean(Volume, Volume)), 10)` — enrichment,均值差 +1.24,p 0.005
9. `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Open), 40))` — enrichment,均值差 +1.12,p 0.000
10. `cs_last_low20(pow_2_5(day_var(Open)), ts_quantile_q75(day_close(Volume), 40))` — enrichment,均值差 +1.05,p 0.021
11. `pow_2_5(day_wmean(Volume, Low))` — enrichment,均值差 +1.04,p 0.000
12. `ts_quantile_q75(day_close(Open), 40)` — enrichment,均值差 +1.01,p 0.000
13. `day_close(Open)` — enrichment,均值差 +1.01,p 0.000
14. `day_wmean(Volume, Low)` — enrichment,均值差 +1.01,p 0.000
15. `ts_quantile_q75(day_close(Low), 10)` — enrichment,均值差 +1.00,p 0.001
16. `cross_scale(cross_scale(LogFloatCap, 241), 241)` — enrichment,均值差 +0.98,p 0.001
17. `day_var(Open)` — enrichment,均值差 +0.96,p 0.007
18. `pow_2_5(day_var(Open))` — enrichment,均值差 +0.96,p 0.007
19. `day_close(Low)` — enrichment,均值差 +0.91,p 0.002
20. `cross_mean(day_sum(Amt), 60)` — enrichment,均值差 +0.86,p 0.018
21. `cs_last_low20(pow_2_5(day_wmean(Volume, Low)), ts_quantile_q75(day_close(Low), 10))` — enrichment,均值差 +0.85,p 0.059
22. `cross_scale(LogFloatCap, 241)` — enrichment,均值差 +0.84,p 0.000
23. `pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241))` — enrichment,均值差 +0.81,p 0.073
24. `day_sum(Amt)` — enrichment,均值差 +0.76,p 0.026
25. `div(day_first(Open), cross_delay(ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), pow_2(day_zero_ratio(Open))), 5), 1))` — enrichment,均值差 +0.71,p 0.074
26. `ts_quantile_q75(day_close(Volume), 40)` — enrichment,均值差 +0.63,p 0.040
27. `day_close(Volume)` — enrichment,均值差 +0.58,p 0.043
28. `day_distinct_ratio(Low)` — enrichment,均值差 +0.42,p 0.004

## 本组之前各轮的任务

- `prods911Pr1a_Ea`:核心 `cross_scale(LogFloatCap, 241)`;评分 72,过线 0,入 heads 0;采样计数 {'c05_no_core': 908, 'c05_periphery_seen': 20, 'mutation_refused': 12}
  - score +0.31(train +0.31 valid +0.75):`pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241))`
  - score +0.31(train +0.31 valid +0.75):`neg(pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241)))`
  - score +0.31(train +0.31 valid +0.75):`pow_2(pow_05(cross_scale(cross_scale(LogFloatCap, 241), 241)))`
  - score +0.31(train +0.31 valid +0.75):`sqrt(cross_scale(cross_scale(LogFloatCap, 241), 241))`
  - score +0.31(train +0.31 valid +0.75):`pow_1_5(cross_scale(cross_scale(LogFloatCap, 241), 241))`
- `prods911Pr1b_Nb`:核心 `—`;评分 99,过线 2,入 heads 2;采样计数 {}
  - score +0.83(train +0.83 valid +2.25):`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Volume)), day_last(Close)), 10)`
  - score +0.82(train +0.82 valid +2.56):`sub(cross_mean(sub(div(day_first(Volume), cross_delay(day_last(Volume), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 60))`
  - score +0.22(train +0.22 valid +2.04):`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), day_last(Open)), 5)`
  - score +0.21(train +0.21 valid +2.08):`ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), day_last(Close)), 5)`
  - score -0.13(train -0.13 valid +1.05):`cs_bucket_demean(sub(cross_mean(sub(div(day_first(Open), cross_delay(ts_quantile_q25(cs_last_low20(neg(day_quantile_q75(Low)), pow_2(day_zero_ratio(Open))), 5), 1)), 1), 60), cross_age(pow_3(cs_last_low40(cross_ema(day_durbin_watson(cross_delta(Volume, 15)), 60), sigmoid(day_open(Low)))))), LogFloatCap)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(swap Volume->Amt):`div(cs_last_low20(pow_2_5(day_wmean(Amt, Amt)), ts_quantile_q75(day_close(Low), 10)), pow_2_5(day_wmean(Amt, Amt)))`
