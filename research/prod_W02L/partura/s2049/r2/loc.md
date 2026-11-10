# 定位:种子 2049,P 组,第 2 轮(只含 train / valid)

快照:prods2049M1_I0_open_search, prods2049M2_I0_open_search, prods2049Pr1a_Na, prods2049Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.76 | -1.22 | -1.76 | +1 | 0 | prods2049M1_I0_open_search | `cross_ema(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 60)` |
| -2.14 | -2.12 | -2.14 | +1 | 20 | prods2049M2_I0_open_search | `ts_mean(sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0)))), 20)` |
| -2.19 | -2.19 | -1.78 | -1 | 5 | prods2049M1_I0_open_search | `cross_tail_mean_q25(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 120)` |
| -2.23 | -2.23 | -2.02 | +1 | 20 | prods2049M2_I0_open_search | `ts_mean(day_sum(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))), 20)` |
| -2.46 | -2.40 | -2.46 | +1 | 0 | prods2049M2_I0_open_search | `ts_mean(day_sum(log(add(create_like(Ret, 1), abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))))))), 20)` |
| -3.06 | -3.06 | -2.11 | +1 | 5 | prods2049M1_I0_open_search | `ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 5)` |

## 共性:120 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.67 | 0.000 | 8 | -0.82 / -2.49 | `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))` |
| +1.60 | 0.001 | 7 | -0.87 / -2.48 | `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120))` |
| +1.56 | 0.004 | 4 | -0.87 / -2.43 | `cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60)` |
| +1.56 | 0.004 | 4 | -0.87 / -2.43 | `div(cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60), cross_ema(day_sum(Volume), 60))` |
| +1.56 | 0.004 | 4 | -0.87 / -2.43 | `cross_ema(day_wmean(Vwap, Volume), 60)` |
| +1.50 | 0.000 | 43 | -1.42 / -2.92 | `day_wmean(Vwap, Volume)` |
| +1.49 | 0.000 | 28 | -1.24 / -2.73 | `mul(day_wmean(Vwap, Volume), day_sum(Volume))` |
| +1.47 | 0.003 | 5 | -0.98 / -2.44 | `cross_ema(day_sum(Volume), 60)` |
| +1.46 | 0.005 | 6 | -1.00 / -2.45 | `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120)), cross_mean(day_wmean(Vwap, Volume), 120))` |
| +1.46 | 0.000 | 30 | -1.29 / -2.75 | `day_sum(Volume)` |
| +1.44 | 0.002 | 8 | -1.04 / -2.48 | `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120)` |
| +1.38 | 0.002 | 9 | -1.11 / -2.48 | `cross_mean(day_wmean(Vwap, Volume), 120)` |
| +1.35 | 0.006 | 7 | -1.11 / -2.46 | `day_wmean(Vwap, High)` |
| +1.35 | 0.006 | 7 | -1.11 / -2.46 | `cross_mean(day_wmean(Vwap, High), 241)` |
| +1.35 | 0.000 | 14 | -1.19 / -2.54 | `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241))` |
| +1.35 | 0.000 | 14 | -1.19 / -2.54 | `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241)` |
| +1.23 | 0.004 | 10 | -1.25 / -2.48 | `cross_sum(day_sum(Volume), 120)` |
| +1.22 | 0.000 | 18 | -1.34 / -2.57 | `cross_sum(day_sum(Volume), 241)` |
| +1.06 | 0.002 | 17 | -1.48 / -2.53 | `cross_mean(day_wmean(Vwap, Volume), 241)` |
| +1.04 | 0.040 | 5 | -1.38 / -2.43 | `day_std(Ret)` |

## 拆解(25 次评估)

### head score -1.76:`cross_ema(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20)` | -1.94 | -1.94 | -1.50 | — | (子树本身) |
| sufficiency | `day_std(Volume)` | -1.21 | -1.10 | -1.21 | — | (子树本身) |
| sufficiency | `day_cov(Volume, Low)` | -4.21 | -4.21 | -3.77 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20)` | -1.56 | -1.36 | -1.56 | -0.20 | `cross_ema(day_std(Volume), 60)` |
| swap | `Volume->Amt` | -1.96 | -1.02 | -1.96 | — | `cross_ema(ts_reg_fvalue(day_std(Amt), day_cov(Amt, Low), 20), 60)` |
| swap | `Low->High` | -2.10 | -2.10 | -2.00 | — | `cross_ema(ts_reg_fvalue(day_std(Volume), day_cov(Volume, High), 20), 60)` |
| window | `cross_ema@60->30` | -1.89 | -0.59 | -1.89 | — | `cross_ema(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 30)` |
| window | `cross_ema@60->120` | -1.74 | -1.74 | -1.70 | — | `cross_ema(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 120)` |

### head score -2.14:`ts_mean(sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0))))` | -2.76 | -2.62 | -2.76 | — | (子树本身) |
| sufficiency | `day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0)))` | -4.75 | -3.82 | -4.75 | — | (子树本身) |
| sufficiency | `day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))` | -4.37 | -3.19 | -4.37 | — | (子树本身) |
| knockout | `sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0))))` | -3.41 | -1.56 | -3.41 | +1.27 | `ts_mean(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), 20)` |
| window | `ts_mean@20->10` | -2.44 | -2.34 | -2.44 | — | `ts_mean(sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0)))), 10)` |
| window | `ts_mean@20->40` | -2.25 | -1.83 | -2.25 | — | `ts_mean(sub(day_mean(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))), day_mean(select_where(is_lt(Ret, create_like(Ret, 0)), abs_(sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0))))), create_like(Ret, 0)))), 40)` |

### head score -2.19:`cross_tail_mean_q25(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40)` | -2.07 | -2.07 | -1.16 | — | (子树本身) |
| sufficiency | `day_std(High)` | -2.27 | -1.55 | -2.27 | — | (子树本身) |
| sufficiency | `day_cov(Volume, Low)` | -4.21 | -4.21 | -3.77 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40)` | -2.43 | -1.76 | -2.43 | +0.24 | `cross_tail_mean_q25(day_std(High), 120)` |
| swap | `High->Low` | -2.19 | -1.97 | -2.19 | — | `cross_tail_mean_q25(ts_reg_fvalue(day_std(Low), day_cov(Volume, Low), 40), 120)` |
| swap | `Volume->Amt` | -2.64 | -2.64 | -2.61 | — | `cross_tail_mean_q25(ts_reg_fvalue(day_std(High), day_cov(Amt, Low), 40), 120)` |
| window | `cross_tail_mean_q25@120->60` | -2.59 | -2.37 | -2.59 | — | `cross_tail_mean_q25(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 60)` |
| window | `cross_tail_mean_q25@120->240` | -2.52 | -2.52 | -1.57 | — | `cross_tail_mean_q25(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 240)` |

### head score -2.23:`ts_mean(day_sum(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0))))` | -2.90 | -2.90 | -1.75 | — | (子树本身) |
| window | `ts_mean@20->10` | -2.43 | -2.43 | -1.63 | — | `ts_mean(day_sum(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))), 10)` |
| window | `ts_mean@20->40` | -2.94 | -1.94 | -2.94 | — | `ts_mean(day_sum(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_gt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)), select_where(is_lt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(select_where(is_lt(Ret, create_like(Ret, 0)), Ret, create_like(Ret, 0)))), create_like(Ret, 0)))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241)), cross_mean(day_wmean(Vwap, Volume), 241))` — enrichment,均值差 +1.67,p 0.000
2. `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120))` — enrichment,均值差 +1.60,p 0.001
3. `cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60)` — enrichment,均值差 +1.56,p 0.004
4. `div(cross_ema(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 60), cross_ema(day_sum(Volume), 60))` — enrichment,均值差 +1.56,p 0.004
5. `cross_ema(day_wmean(Vwap, Volume), 60)` — enrichment,均值差 +1.56,p 0.004
6. `day_wmean(Vwap, Volume)` — enrichment,均值差 +1.50,p 0.000
7. `mul(day_wmean(Vwap, Volume), day_sum(Volume))` — enrichment,均值差 +1.49,p 0.000
8. `cross_ema(day_sum(Volume), 60)` — enrichment,均值差 +1.47,p 0.003
9. `sub(div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120), cross_sum(day_sum(Volume), 120)), cross_mean(day_wmean(Vwap, Volume), 120))` — enrichment,均值差 +1.46,p 0.005
10. `day_sum(Volume)` — enrichment,均值差 +1.46,p 0.000
11. `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 120)` — enrichment,均值差 +1.44,p 0.002
12. `cross_mean(day_wmean(Vwap, Volume), 120)` — enrichment,均值差 +1.38,p 0.002
13. `day_wmean(Vwap, High)` — enrichment,均值差 +1.35,p 0.006
14. `cross_mean(day_wmean(Vwap, High), 241)` — enrichment,均值差 +1.35,p 0.006
15. `div(cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241), cross_sum(day_sum(Volume), 241))` — enrichment,均值差 +1.35,p 0.000
16. `cross_sum(mul(day_wmean(Vwap, Volume), day_sum(Volume)), 241)` — enrichment,均值差 +1.35,p 0.000
17. `cross_sum(day_sum(Volume), 120)` — enrichment,均值差 +1.23,p 0.004
18. `cross_sum(day_sum(Volume), 241)` — enrichment,均值差 +1.22,p 0.000
19. `cross_mean(day_wmean(Vwap, Volume), 241)` — enrichment,均值差 +1.06,p 0.002
20. `day_std(Ret)` — enrichment,均值差 +1.04,p 0.040
21. `day_corr(Ret, Open)` — enrichment,均值差 +1.02,p 0.053
22. `day_topw_mean(Amt, Amt)` — enrichment,均值差 +0.96,p 0.044
23. `day_min(Low)` — enrichment,均值差 +0.66,p 0.059
24. `sub(day_max(High), day_min(Low))` — enrichment,均值差 +0.66,p 0.059
25. `day_max(High)` — enrichment,均值差 +0.66,p 0.059
26. `day_std(Low)` — enrichment,均值差 +0.49,p 0.058

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

## 比原 head 好的拆解变体(R 候选)

(没有)
