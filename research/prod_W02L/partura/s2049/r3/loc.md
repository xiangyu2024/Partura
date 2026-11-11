# 定位:种子 2049,P 组,第 3 轮(只含 train / valid)

快照:prods2049M1_I0_open_search, prods2049M2_I0_open_search, prods2049M3_I0_open_search, prods2049Pr1a_Na, prods2049Pr1b_Nb, prods2049Pr2a_Ea, prods2049Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.71 | -1.71 | -1.14 | -1 | 20 | prods2049M3_I0_open_search | `cross_mean(div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)` |
| -1.76 | -1.22 | -1.76 | +1 | 0 | prods2049M1_I0_open_search | `cross_ema(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 60)` |
| -2.06 | -2.00 | -2.06 | -1 | 5 | prods2049M3_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 20)` |
| -2.14 | -2.12 | -2.14 | +1 | 20 | prods2049M2_I0_open_search | `ts_mean(sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0)))), 20)` |
| -2.19 | -2.19 | -1.78 | -1 | 5 | prods2049M1_I0_open_search | `cross_tail_mean_q25(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 120)` |
| -2.23 | -2.23 | -2.02 | +1 | 20 | prods2049M2_I0_open_search | `ts_mean(day_sum(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))), 20)` |
| -2.46 | -2.40 | -2.46 | +1 | 0 | prods2049M2_I0_open_search | `ts_mean(day_sum(log(add(create_like(Ret, 1), abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))))))), 20)` |
| -3.06 | -3.06 | -2.11 | +1 | 5 | prods2049M1_I0_open_search | `ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 5)` |
| -3.08 | -3.00 | -3.08 | -1 | 20 | prods2049M3_I0_open_search | `div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` |

## 共性:221 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.69 | 0.000 | 16 | -0.44 / -2.13 | `div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))` |
| +1.54 | 0.000 | 21 | -0.61 / -2.15 | `cross_ema(day_wmean(Vwap, Volume), 60)` |
| +1.50 | 0.000 | 11 | -0.59 / -2.08 | `cross_ema(day_sum(Volume), 60)` |
| +1.45 | 0.000 | 16 | -0.66 / -2.11 | `cross_ema(day_close(Close), 60)` |
| +1.43 | 0.000 | 13 | -0.66 / -2.09 | `sub(cross_ema(day_close(Close), 60), cross_ema(day_wmean(Vwap, Volume), 60))` |
| +1.41 | 0.000 | 75 | -1.08 / -2.48 | `mul(day_wmean(Vwap, Volume), day_sum(Volume))` |
| +1.40 | 0.000 | 55 | -0.96 / -2.35 | `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))` |
| +1.38 | 0.000 | 90 | -1.19 / -2.57 | `day_wmean(Vwap, Volume)` |
| +1.35 | 0.000 | 61 | -1.03 / -2.38 | `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241))` |
| +1.35 | 0.000 | 61 | -1.03 / -2.38 | `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241)` |
| +1.35 | 0.000 | 12 | -0.73 / -2.08 | `cross_ema(cross_mean(day_wmean(Vwap, Volume), 241), 60)` |
| +1.31 | 0.000 | 65 | -1.08 / -2.39 | `cross_sum(day_sum(Volume), 241)` |
| +1.28 | 0.022 | 4 | -0.75 / -2.03 | `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)` |
| +1.26 | 0.000 | 64 | -1.11 / -2.37 | `cross_mean(day_wmean(Vwap, Volume), 241)` |
| +1.26 | 0.000 | 83 | -1.22 / -2.48 | `day_sum(Volume)` |
| +1.17 | 0.010 | 7 | -0.87 / -2.04 | `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120))` |
| +1.16 | 0.035 | 4 | -0.87 / -2.03 | `cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60)` |
| +1.16 | 0.035 | 4 | -0.87 / -2.03 | `div(cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60), cross_ema(day_sum(Volume), 60))` |
| +1.05 | 0.000 | 17 | -1.04 / -2.09 | `sub(day_wmean(Ret, Volume), day_mean(Ret))` |
| +1.04 | 0.035 | 6 | -1.00 / -2.04 | `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120)), cross_mean(day_wmean(Vwap, Volume), 120))` |

## 拆解(23 次评估)

### head score -1.71:`cross_mean(div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -3.11 | -3.00 | -3.11 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.96 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |
| knockout | `div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -3.52 | -3.38 | -3.52 | +1.81 | `cross_mean(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)` |
| window | `cross_mean@20->10` | -1.80 | -1.80 | -1.31 | — | `cross_mean(div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 10)` |
| window | `cross_mean@20->40` | -1.56 | -1.56 | -1.28 | — | `cross_mean(div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 40)` |

### head score -2.06:`ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))))` | -3.85 | -3.62 | -3.85 | — | (子树本身) |
| sufficiency | `sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))` | -3.72 | -3.72 | -2.67 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.71 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.96 | — | (子树本身) |
| knockout | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))))` | -1.34 | -1.21 | -1.34 | -0.72 | `ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| knockout | `sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))` | -1.64 | -1.64 | -1.61 | -0.42 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), 20)` |
| knockout | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.99 | -1.99 | -1.29 | -0.07 | `ts_mean(mul(sub(day_max(High), day_min(Low)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 20)` |
| knockout | `sub(day_max(High), day_min(Low))` | -2.10 | -2.10 | -1.63 | +0.04 | `ts_mean(mul(div(day_max(High), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 20)` |
| swap | `High->Low` | -2.07 | -1.97 | -2.07 | — | `ts_mean(mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 20)` |
| swap | `Low->High` | -2.14 | -2.12 | -2.14 | — | `ts_mean(mul(div(sub(day_max(High), day_min(High)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 20)` |
| window | `ts_mean@20->10` | -2.25 | -2.25 | -2.03 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 10)` |
| window | `ts_mean@20->40` | -1.40 | -1.40 | -0.51 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), sub(day_std(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))), day_std(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), 40)` |

### head score -2.46:`ts_mean(day_sum(log(add(create_like(Ret, 1), abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(log(add(create_like(Ret, 1), abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))))))` | -4.48 | -3.73 | -4.48 | — | (子树本身) |
| window | `ts_mean@20->10` | -4.02 | -3.40 | -4.02 | — | `ts_mean(day_sum(log(add(create_like(Ret, 1), abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))))))), 10)` |
| window | `ts_mean@20->40` | -3.35 | -2.69 | -3.35 | — | `ts_mean(day_sum(log(add(create_like(Ret, 1), abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))))))), 40)` |

### head score -3.08:`div(day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.96 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |

## 机械核心卡(B0 按这个顺序取)

1. `div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))` — enrichment,均值差 +1.69,p 0.000
2. `cross_ema(day_wmean(Vwap, Volume), 60)` — enrichment,均值差 +1.54,p 0.000
3. `cross_ema(day_sum(Volume), 60)` — enrichment,均值差 +1.50,p 0.000
4. `cross_ema(day_close(Close), 60)` — enrichment,均值差 +1.45,p 0.000
5. `sub(cross_ema(day_close(Close), 60), cross_ema(day_wmean(Vwap, Volume), 60))` — enrichment,均值差 +1.43,p 0.000
6. `mul(day_wmean(Vwap, Volume), day_sum(Volume))` — enrichment,均值差 +1.41,p 0.000
7. `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))` — enrichment,均值差 +1.40,p 0.000
8. `day_wmean(Vwap, Volume)` — enrichment,均值差 +1.38,p 0.000
9. `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241))` — enrichment,均值差 +1.35,p 0.000
10. `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241)` — enrichment,均值差 +1.35,p 0.000
11. `cross_ema(cross_mean(day_wmean(Vwap, Volume), 241), 60)` — enrichment,均值差 +1.35,p 0.000
12. `cross_sum(day_sum(Volume), 241)` — enrichment,均值差 +1.31,p 0.000
13. `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)` — enrichment,均值差 +1.28,p 0.022
14. `cross_mean(day_wmean(Vwap, Volume), 241)` — enrichment,均值差 +1.26,p 0.000
15. `day_sum(Volume)` — enrichment,均值差 +1.26,p 0.000
16. `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120))` — enrichment,均值差 +1.17,p 0.010
17. `cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60)` — enrichment,均值差 +1.16,p 0.035
18. `div(cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60), cross_ema(day_sum(Volume), 60))` — enrichment,均值差 +1.16,p 0.035
19. `sub(day_wmean(Ret, Volume), day_mean(Ret))` — enrichment,均值差 +1.05,p 0.000
20. `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120)), cross_mean(day_wmean(Vwap, Volume), 120))` — enrichment,均值差 +1.04,p 0.035
21. `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120)` — enrichment,均值差 +1.01,p 0.019
22. `day_close(Close)` — enrichment,均值差 +0.98,p 0.000
23. `cross_mean(day_wmean(Vwap, Volume), 120)` — enrichment,均值差 +0.94,p 0.022
24. `div(sub(cross_ema(day_close(Close), 60), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(cross_mean(day_wmean(Vwap, Volume), 241), 60))` — enrichment,均值差 +0.93,p 0.077
25. `day_wmean(Vwap, High)` — enrichment,均值差 +0.93,p 0.034
26. `cross_mean(day_wmean(Vwap, High), 241)` — enrichment,均值差 +0.93,p 0.034
27. `day_mean(Ret)` — enrichment,均值差 +0.90,p 0.001
28. `day_wmean(Ret, Volume)` — enrichment,均值差 +0.86,p 0.001
29. `cross_sum(day_sum(Volume), 120)` — enrichment,均值差 +0.79,p 0.043

## 本组之前各轮的任务

- `prods2049Pr1a_Na`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.14(train -0.14 valid +0.68):`div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120)), cross_mean(day_wmean(Vwap, Volume), 15)), cross_mean(day_wmean(Vwap, Volume), 120)), 241)), cross_mean(day_wmean(Vwap, High), 241))`
  - score -0.17(train -0.17 valid +0.68):`div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, High), 241))`
  - score -0.17(train -0.17 valid +0.68):`div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Vwap), 241))`
  - score -0.19(train -0.19 valid +0.68):`div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))`
  - score -0.28(train -0.28 valid +0.61):`div(sub(div(cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60), cross_ema(day_sum(Volume), 60)), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(day_wmean(Vwap, Volume), 60))`
- `prods2049Pr1b_Nb`:核心 `—`;评分 81,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -0.49(train -0.49 valid -0.07):`cross_corr(day_corr(Volume, Low), day_std(Volume), 120)`
  - score -0.89(train -0.87 valid -0.89):`cross_ema(div(day_sum(Ret), add(day_std(Low), 0.0001)), 120)`
  - score -1.03(train -1.03 valid -0.70):`cross_mean(div(sub(day_corr(Low, Volume), day_mean(Low)), add(day_std(Low), 0.0001)), 241)`
  - score -1.04(train -1.04 valid -0.69):`cross_mean(div(sub(day_corr(Low, Volume), sub(day_corr(Low, Volume), day_mean(Low))), add(day_std(Low), 0.0001)), 241)`
  - score -1.04(train -1.04 valid -0.69):`cross_mean(div(sub(day_corr(Low, Amt), sub(day_corr(Low, Amt), day_mean(Low))), add(day_std(Low), 0.0001)), 241)`
- `prods2049Pr2a_Ea`:核心 `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))`;评分 85,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 7, 'c05_no_core': 1074, 'c05_skeleton': 507, 'mutation_refused': 5}
  - score -0.19(train -0.19 valid +0.68):`sub(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), div(sub(cross_ema(day_close(Close), 60), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(day_sum(Volume), 60)))`
  - score -0.19(train -0.19 valid +0.68):`sub(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), div(sub(cross_ema(cross_mean(day_wmean(Vwap, Volume), 241), 60), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(day_sum(Volume), 60)))`
  - score -0.19(train -0.19 valid +0.67):`sub(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), div(add(cross_ema(day_close(Close), 60), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(day_sum(Volume), 60)))`
  - score -0.19(train -0.19 valid +0.68):`sub(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), div(sub(cross_ema(cross_ema(day_close(Close), 60), 60), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(day_sum(Volume), 60)))`
  - score -0.20(train -0.20 valid +0.75):`sub(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), div(sub(div(sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241)), div(sub(cross_ema(day_close(Close), 60), cross_ema(day_wmean(Vwap, Volume), 60)), cross_ema(day_sum(Volume), 60))), cross_ema(cross_mean(day_wmean(Vwap, Volume), 241), 60)))`
- `prods2049Pr2b_Nb`:核心 `—`;评分 70,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.13(train -0.12 valid -0.13):`cross_sum(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), 60)`
  - score -0.18(train -0.18 valid +0.20):`cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)`
  - score -0.22(train -0.22 valid -0.01):`cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 241)`
  - score -0.23(train -0.04 valid -0.23):`cross_ema(add(cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60), day_mean(Ret)), 60)`
  - score -0.24(train -0.22 valid -0.24):`cross_sum(sub(sub(cross_sum(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), 60), day_mean(Ret)), day_mean(Ret)), 3)`

## 比原 head 好的拆解变体(R 候选)

(没有)
