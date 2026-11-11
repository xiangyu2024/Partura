# 定位:种子 2035,P 组,第 3 轮(只含 train / valid)

快照:prods2035M1_I0_open_search, prods2035M2_I0_open_search, prods2035M3_I0_open_search, prods2035Pr1a_Na, prods2035Pr1b_Nb, prods2035Pr2a_Ea, prods2035Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.43 | -0.37 | -0.43 | +1 | 5 | prods2035M3_I0_open_search | `ts_stddev(ts_stddev(day_sum(Amt), 20), 30)` |
| -0.85 | -0.85 | -0.83 | +1 | 0 | prods2035M3_I0_open_search | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(Amt), 20), 30), 10)` |
| -1.34 | -1.19 | -1.34 | +1 | 5 | prods2035M1_I0_open_search | `inv(day_sum(Volume))` |
| -1.52 | -1.24 | -1.52 | -1 | 5 | prods2035M1_I0_open_search | `ts_max(ts_max(inv(inv(day_sum(Volume))), 10), 10)` |
| -1.64 | -1.64 | -1.56 | -1 | 5 | prods2035M2_I0_open_search | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12)), day_first(in_topk_masked(Volume, Open, 12))), 20)` |
| -1.67 | -1.45 | -1.67 | -1 | 5 | prods2035M1_I0_open_search | `inv(ts_max(inv(day_sum(Volume)), 10))` |
| -1.93 | -1.93 | -1.84 | -1 | 5 | prods2035M2_I0_open_search | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 40)` |
| -2.19 | -2.16 | -2.19 | -1 | 20 | prods2035M2_I0_open_search | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 12, False)), day_first(in_topk_masked(Volume, Open, 12, False))), 20)` |
| -2.20 | -1.87 | -2.20 | -1 | 20 | prods2035M3_I0_open_search | `ts_stddev(ts_stddev(day_sum(High), 10), 20)` |

## 共性:240 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.56 | 0.002 | 6 | -0.68 / -2.24 | `ts_quantile_q25(day_last(Ret), 40)` |
| +1.46 | 0.000 | 19 | -0.85 / -2.32 | `day_first(Amt)` |
| +1.43 | 0.015 | 4 | -0.80 / -2.23 | `cs_winsor(cross_reg_tvalue(day_argmax(Amt), day_mean(Low), 60))` |
| +1.43 | 0.015 | 4 | -0.80 / -2.23 | `cross_reg_tvalue(day_argmax(Amt), day_mean(Low), 60)` |
| +1.34 | 0.000 | 13 | -0.94 / -2.27 | `cross_reg_tvalue(day_first(Amt), day_mean(Low), 30)` |
| +1.34 | 0.000 | 13 | -0.94 / -2.27 | `cs_winsor(cross_reg_tvalue(day_first(Amt), day_mean(Low), 30))` |
| +1.26 | 0.000 | 20 | -1.05 / -2.31 | `day_std(Open)` |
| +1.20 | 0.006 | 8 | -1.04 / -2.24 | `select_where(is_lt(abs_(cross_delta(log(day_last(Close)), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0)` |
| +1.14 | 0.000 | 28 | -1.20 / -2.34 | `day_mean(Low)` |
| +1.13 | 0.004 | 13 | -1.13 / -2.26 | `day_last(Ret)` |
| +1.03 | 0.004 | 21 | -1.26 / -2.29 | `day_argmax(Amt)` |
| +1.02 | 0.032 | 9 | -1.22 / -2.24 | `sub(day_std(Open), ts_delta(day_first(Ret), 50))` |
| +0.98 | 0.013 | 14 | -1.28 / -2.26 | `day_first(Ret)` |
| +0.98 | 0.013 | 14 | -1.28 / -2.26 | `ts_delta(day_first(Ret), 50)` |
| +0.98 | 0.017 | 12 | -1.27 / -2.25 | `day_durbin_watson(Vwap)` |
| +0.93 | 0.149 | 4 | -1.29 / -2.22 | `cs_scale(cs_scale(cs_scale(LogFloatShares)))` |
| +0.91 | 0.079 | 9 | -1.33 / -2.24 | `cross_reg_tvalue(day_argmax(Amt), day_mean(Low), 30)` |
| +0.86 | 0.110 | 8 | -1.37 / -2.23 | `cs_scale(cs_scale(LogFloatShares))` |
| +0.82 | 0.062 | 19 | -1.45 / -2.27 | `cs_scale(LogFloatShares)` |
| +0.80 | 0.176 | 5 | -1.42 / -2.22 | `cs_scale(ts_delta(cs_scale(LogFloatShares), 40))` |

## 拆解(28 次评估)

### head score -0.43:`ts_stddev(ts_stddev(day_sum(Amt), 20), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_sum(Amt), 20)` | -2.48 | -2.48 | -1.08 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `ts_stddev(day_sum(Amt), 20)` | -1.51 | -1.51 | -0.69 | +1.08 | `ts_stddev(day_sum(Amt), 30)` |
| swap | `Amt->Volume` | -2.00 | -0.82 | -2.00 | — | `ts_stddev(ts_stddev(day_sum(Volume), 20), 30)` |
| window | `ts_stddev@30->15` | -1.03 | -1.03 | -0.87 | — | `ts_stddev(ts_stddev(day_sum(Amt), 20), 15)` |
| window | `ts_stddev@30->60` | -0.14 | -0.14 | +0.29 | — | `ts_stddev(ts_stddev(day_sum(Amt), 20), 60)` |

### head score -0.85:`ts_quantile_q25(ts_stddev(ts_stddev(day_sum(Amt), 20), 30), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(ts_stddev(day_sum(Amt), 20), 30)` | -0.43 | -0.37 | -0.43 | — | (子树本身) |
| sufficiency | `ts_stddev(day_sum(Amt), 20)` | -2.48 | -2.48 | -1.08 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `ts_stddev(ts_stddev(day_sum(Amt), 20), 30)` | -3.09 | -3.09 | -1.93 | +2.25 | `ts_quantile_q25(ts_stddev(day_sum(Amt), 20), 10)` |
| knockout | `ts_stddev(day_sum(Amt), 20)` | -2.65 | -2.65 | -2.14 | +1.80 | `ts_quantile_q25(ts_stddev(day_sum(Amt), 30), 10)` |
| swap | `Amt->Volume` | -2.49 | -1.35 | -2.49 | — | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(Volume), 20), 30), 10)` |
| window | `ts_quantile_q25@10->5` | -0.72 | -0.53 | -0.72 | — | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(Amt), 20), 30), 5)` |
| window | `ts_quantile_q25@10->20` | -1.58 | -1.08 | -1.58 | — | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(Amt), 20), 30), 20)` |

### head score -1.93:`cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False)))` | -4.70 | -4.70 | -3.79 | — | (子树本身) |
| sufficiency | `day_last(in_topk_masked(Volume, Close, 5, False))` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| sufficiency | `day_first(in_topk_masked(Volume, Open, 5, False))` | -2.36 | -1.61 | -2.36 | — | (子树本身) |
| knockout | `div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False)))` | -2.19 | -1.72 | -2.19 | +0.26 | `cross_stddev(day_last(in_topk_masked(Volume, Close, 5, False)), 40)` |
| swap | `Volume->Amt` | -1.86 | -1.86 | -1.81 | — | `cross_stddev(div(day_last(in_topk_masked(Amt, Close, 5, False)), day_first(in_topk_masked(Amt, Open, 5, False))), 40)` |
| swap | `Close->Vwap` | -2.11 | -2.11 | -1.96 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Vwap, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 40)` |
| window | `cross_stddev@40->20` | -2.09 | -1.96 | -2.09 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 20)` |
| window | `cross_stddev@40->80` | -2.02 | -1.92 | -2.02 | — | `cross_stddev(div(day_last(in_topk_masked(Volume, Close, 5, False)), day_first(in_topk_masked(Volume, Open, 5, False))), 80)` |

### head score -2.20:`ts_stddev(ts_stddev(day_sum(High), 10), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_sum(High), 10)` | -2.34 | -1.79 | -2.34 | — | (子树本身) |
| sufficiency | `day_sum(High)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `ts_stddev(day_sum(High), 10)` | -2.31 | -1.81 | -2.31 | +0.11 | `ts_stddev(day_sum(High), 20)` |
| swap | `High->Low` | -2.16 | -1.85 | -2.16 | — | `ts_stddev(ts_stddev(day_sum(Low), 10), 20)` |
| window | `ts_stddev@20->10` | -2.32 | -1.98 | -2.32 | — | `ts_stddev(ts_stddev(day_sum(High), 10), 10)` |
| window | `ts_stddev@20->40` | -2.16 | -1.76 | -2.16 | — | `ts_stddev(ts_stddev(day_sum(High), 10), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_quantile_q25(day_last(Ret), 40)` — enrichment,均值差 +1.56,p 0.002
2. `day_first(Amt)` — enrichment,均值差 +1.46,p 0.000
3. `cs_winsor(cross_reg_tvalue(day_argmax(Amt), day_mean(Low), 60))` — enrichment,均值差 +1.43,p 0.015
4. `cross_reg_tvalue(day_argmax(Amt), day_mean(Low), 60)` — enrichment,均值差 +1.43,p 0.015
5. `cross_reg_tvalue(day_first(Amt), day_mean(Low), 30)` — enrichment,均值差 +1.34,p 0.000
6. `cs_winsor(cross_reg_tvalue(day_first(Amt), day_mean(Low), 30))` — enrichment,均值差 +1.34,p 0.000
7. `day_std(Open)` — enrichment,均值差 +1.26,p 0.000
8. `select_where(is_lt(abs_(cross_delta(log(day_last(Close)), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0)` — enrichment,均值差 +1.20,p 0.006
9. `day_mean(Low)` — enrichment,均值差 +1.14,p 0.000
10. `day_last(Ret)` — enrichment,均值差 +1.13,p 0.004
11. `day_argmax(Amt)` — enrichment,均值差 +1.03,p 0.004
12. `sub(day_std(Open), ts_delta(day_first(Ret), 50))` — enrichment,均值差 +1.02,p 0.032
13. `day_first(Ret)` — enrichment,均值差 +0.98,p 0.013
14. `ts_delta(day_first(Ret), 50)` — enrichment,均值差 +0.98,p 0.013
15. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.98,p 0.017
16. `cross_reg_tvalue(day_argmax(Amt), day_mean(Low), 30)` — enrichment,均值差 +0.91,p 0.079
17. `cs_scale(LogFloatShares)` — enrichment,均值差 +0.82,p 0.062
18. `day_last(Close)` — enrichment,均值差 +0.30,p 0.003
19. `log(day_last(Close))` — enrichment,均值差 +0.28,p 0.004
20. `select_where(is_lt(abs_(cross_delta(log(day_last(Close)), 1)), 0.09), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0)` — enrichment,均值差 +0.23,p 0.004

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
- `prods2035Pr2a_Ea`:核心 `cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1)`;评分 97,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 28, 'c05_no_core': 1180, 'c05_skeleton': 594, 'mutation_refused': 1}
  - score +0.35(train +0.35 valid +0.58):`cross_sum(select_where(is_lt(abs_(cross_delta(log(day_last(Close)), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241)`
  - score -0.18(train +0.04 valid -0.18):`cross_sum(select_where(is_lt(abs_(cross_delta(ts_argmin(day_sum(Volume), 20), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241)`
  - score -0.19(train -0.06 valid -0.19):`cross_mean(cross_sum(select_where(is_lt(abs_(cross_delta(log(day_last(Close)), 1)), 0.09), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 120), 20)`
  - score -0.20(train +0.19 valid -0.20):`cross_sum(select_where(is_lt(abs_(cross_delta(ts_argmin(day_sum(Amt), 20), 1)), 0.15), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241)`
  - score -0.27(train -0.27 valid +0.27):`cs_bucket_zscore(cross_sum(select_where(is_lt(abs_(cross_delta(log(day_last(Close)), 1)), 0.09), cross_delta(sub(log(day_last(Amt)), LogTotalCap), 1), 0.0), 241), LogFloatCap)`
- `prods2035Pr2b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {'c05_skeleton': 15}
  - score -0.12(train +0.35 valid -0.12):`cs_first_high20(cs_bucket_demean(cs_winsor(cross_reg_tvalue(day_first(Amt), day_mean(Low), 30)), day_std(Open)), cross_reg_tvalue(day_argmax(Amt), day_first(Amt), 30))`
  - score -0.15(train +0.56 valid -0.15):`cs_bucket_demean(cs_winsor(cross_reg_tvalue(day_first(Amt), day_mean(Ret), 30)), sub(day_std(Open), ts_delta(day_first(Ret), 50)))`
  - score -0.16(train -0.16 valid -0.16):`cs_bucket_demean(day_first(Amt), sub(ts_quantile_q25(day_last(Ret), 40), ts_delta(day_first(Ret), 50)))`
  - score -0.45(train +0.19 valid -0.45):`cs_first_high20(day_durbin_watson(Vwap), cross_reg_tvalue(day_argmax(Amt), day_first(Amt), 30))`
  - score -0.52(train -0.52 valid -0.11):`cs_bucket_demean(cs_winsor(cross_reg_tvalue(day_first(Amt), day_durbin_watson(Vwap), 30)), day_std(Open))`

## 比原 head 好的拆解变体(R 候选)

(没有)
