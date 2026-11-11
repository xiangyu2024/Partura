# 定位:种子 2046,P 组,第 2 轮(只含 train / valid)

快照:prods2046M1_I0_open_search, prods2046M2_I0_open_search, prods2046Pr1a_Ea, prods2046Pr1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.88 | +1.36 | +0.88 | +1 | 0 | prods2046Pr1b_Nb | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 120)` |
| +0.18 | +1.14 | +0.18 | +1 | 0 | prods2046M1_I0_open_search | `cs_regres(log(ts_sum(day_var(Amt), 100)), log(ts_sum(day_mean(Amt), 100)))` |
| -0.67 | -0.67 | -0.63 | +1 | 20 | prods2046M1_I0_open_search | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 2)` |
| -0.77 | -0.74 | -0.77 | +1 | 5 | prods2046M1_I0_open_search | `ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 20)` |
| -1.15 | -1.15 | -0.76 | +1 | 5 | prods2046M2_I0_open_search | `div(add(div(day_var(Ret), day_max(High)), cross_max(day_cov(Amt, Close), 60)), log(ts_sum(day_argmin(Amt), 50)))` |
| -1.26 | -0.48 | -1.26 | +1 | 5 | prods2046M2_I0_open_search | `div(add(div(day_var(Amt), day_max(High)), cross_max(day_cov(Close, Close), 15)), log(ts_sum(day_argmin(Amt), 50)))` |
| -1.57 | -1.57 | -1.17 | -1 | 20 | prods2046M2_I0_open_search | `div(add(div(day_var(Ret), day_max(High)), cross_max(day_cov(Close, Close), 15)), log(day_cov(Close, Close)))` |

## 共性:169 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.36 | 0.004 | 6 | -0.41 / -1.77 | `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` |
| +1.31 | 0.003 | 4 | -0.44 / -1.75 | `cross_delay(cross_zscore(log(day_var(Ret)), 60), 1)` |
| +1.31 | 0.003 | 4 | -0.44 / -1.75 | `cross_zscore(log(day_var(Ret)), 60)` |
| +1.29 | 0.004 | 4 | -0.46 / -1.75 | `log(log(day_var(Ret)))` |
| +1.02 | 0.000 | 29 | -0.87 / -1.89 | `log(day_var(Ret))` |
| +0.97 | 0.000 | 40 | -0.98 / -1.95 | `day_var(replace_small_with_nan(Amt))` |
| +0.93 | 0.022 | 4 | -0.81 / -1.74 | `log(day_var(Amt))` |
| +0.73 | 0.001 | 25 | -1.10 / -1.83 | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` |
| +0.63 | 0.001 | 28 | -1.19 / -1.82 | `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` |
| +0.61 | 0.001 | 32 | -1.22 / -1.83 | `pow_2(day_mean(replace_small_with_nan(Amt)))` |
| +0.61 | 0.001 | 34 | -1.23 / -1.84 | `day_mean(replace_small_with_nan(Amt))` |
| +0.54 | 0.179 | 4 | -1.19 / -1.73 | `cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1)` |
| +0.50 | 0.101 | 5 | -1.23 / -1.73 | `cross_reg_tvalue(cross_delay(day_var(Low), 1), cs_demean(day_sum(Ret)), 120)` |
| +0.44 | 0.009 | 45 | -1.39 / -1.84 | `day_var(Ret)` |
| +0.36 | 0.097 | 8 | -1.37 / -1.74 | `day_var(Amt)` |
| +0.30 | 0.328 | 5 | -1.43 / -1.73 | `log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))))` |
| +0.26 | 0.290 | 4 | -1.47 / -1.73 | `day_last(Amt)` |
| +0.21 | 0.116 | 17 | -1.53 / -1.74 | `cross_delay(day_var(Low), 1)` |
| +0.15 | 0.152 | 49 | -1.61 / -1.76 | `day_sum(Ret)` |
| +0.07 | 0.469 | 19 | -1.65 / -1.73 | `cross_delay(cross_zscore(log(day_var(Low)), 60), 1)` |

## 拆解(42 次评估)

### head score +0.88:`cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1)` | -4.13 | -4.13 | -3.63 | — | (子树本身) |
| sufficiency | `log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))))` | -3.87 | -3.87 | -3.53 | — | (子树本身) |
| sufficiency | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | -3.71 | -3.36 | -3.71 | — | (子树本身) |
| sufficiency | `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` | -3.71 | -3.36 | -3.71 | — | (子树本身) |
| knockout | `cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1)` | -0.28 | -0.28 | +0.47 | +1.16 | `cross_corr(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), day_var(replace_small_with_nan(Amt)), 120)` |
| knockout | `log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))))` | +0.75 | +1.18 | +0.75 | +0.13 | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Amt)), 120)` |
| knockout | `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` | -0.69 | -0.43 | -0.69 | +1.57 | `cross_corr(cross_delay(log(log(day_var(replace_small_with_nan(Amt)))), 1), day_var(replace_small_with_nan(Amt)), 120)` |
| swap | `Amt->Volume` | +0.74 | +1.10 | +0.74 | — | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Volume)), pow_2(day_mean(replace_small_with_nan(Volume)))))), 1), day_var(replace_small_with_nan(Volume)), 120)` |
| window | `cross_corr@120->60` | +0.30 | +1.26 | +0.30 | — | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 60)` |
| window | `cross_corr@120->240` | +0.99 | +0.99 | +1.23 | — | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 240)` |

### head score +0.18:`cs_regres(log(ts_sum(day_var(Amt), 100)), log(ts_sum(day_mean(Amt), 100)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(ts_sum(day_var(Amt), 100))` | -0.28 | -0.28 | +0.24 | — | (子树本身) |
| sufficiency | `log(ts_sum(day_mean(Amt), 100))` | -1.82 | -1.82 | -0.75 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(Amt), 100)` | -0.28 | -0.28 | +0.24 | — | (子树本身) |
| sufficiency | `ts_sum(day_mean(Amt), 100)` | -1.82 | -1.82 | -0.75 | — | (子树本身) |
| knockout | `log(ts_sum(day_var(Amt), 100))` | -2.79 | -2.42 | -2.79 | +2.97 | `cs_regres(ts_sum(day_var(Amt), 100), log(ts_sum(day_mean(Amt), 100)))` |
| knockout | `log(ts_sum(day_mean(Amt), 100))` | -1.21 | -1.21 | -0.72 | +1.38 | `cs_regres(log(ts_sum(day_var(Amt), 100)), ts_sum(day_mean(Amt), 100))` |
| knockout | `ts_sum(day_var(Amt), 100)` | -1.80 | -1.24 | -1.80 | +1.98 | `cs_regres(log(day_var(Amt)), log(ts_sum(day_mean(Amt), 100)))` |
| knockout | `ts_sum(day_mean(Amt), 100)` | -1.30 | -1.30 | -0.98 | +1.47 | `cs_regres(log(ts_sum(day_var(Amt), 100)), log(day_mean(Amt)))` |
| swap | `Amt->Volume` | -1.00 | -0.14 | -1.00 | — | `cs_regres(log(ts_sum(day_var(Volume), 100)), log(ts_sum(day_mean(Volume), 100)))` |
| window | `ts_sum@100->50` | -1.54 | -0.09 | -1.54 | — | `cs_regres(log(ts_sum(day_var(Amt), 50)), log(ts_sum(day_mean(Amt), 100)))` |
| window | `ts_sum@100->200` | +1.10 | +1.15 | +1.10 | — | `cs_regres(log(ts_sum(day_var(Amt), 200)), log(ts_sum(day_mean(Amt), 100)))` |

### head score -0.67:`ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 2)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20)` | -0.76 | -0.65 | -0.76 | — | (子树本身) |
| sufficiency | `ts_std(day_var(Low), 20)` | -2.44 | -1.60 | -2.44 | — | (子树本身) |
| sufficiency | `day_std(High)` | -2.27 | -1.55 | -2.27 | — | (子树本身) |
| sufficiency | `day_var(Low)` | -2.27 | -1.53 | -2.27 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20)` | -2.23 | -1.56 | -2.23 | +1.57 | `ts_min(day_std(High), 2)` |
| knockout | `ts_std(day_var(Low), 20)` | -1.05 | -0.88 | -1.05 | +0.39 | `ts_min(ts_reg_fvalue(day_std(High), day_var(Low), 20), 2)` |
| swap | `High->Low` | -0.85 | -0.73 | -0.85 | — | `ts_min(ts_reg_fvalue(day_std(Low), ts_std(day_var(Low), 20), 20), 2)` |
| swap | `Low->High` | -0.77 | -0.60 | -0.77 | — | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(High), 20), 20), 2)` |
| window | `ts_min@2->2` | -0.67 | -0.67 | -0.63 | — | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 2)` |
| window | `ts_min@2->4` | -0.89 | -0.76 | -0.89 | — | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 4)` |

### head score -0.77:`ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241)` | -1.08 | -1.08 | -0.37 | — | (子树本身) |
| sufficiency | `ts_max(day_last(Amt), 20)` | -1.89 | -1.89 | -0.54 | — | (子树本身) |
| sufficiency | `log(day_var(Low))` | -2.33 | -1.65 | -2.33 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| knockout | `cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241)` | -0.78 | -0.78 | -0.42 | +0.01 | `ts_max(ts_max(day_last(Amt), 20), 20)` |
| knockout | `ts_max(day_last(Amt), 20)` | -1.29 | -1.29 | -0.97 | +0.52 | `ts_max(cross_corr(day_last(Amt), log(day_var(Low)), 241), 20)` |
| knockout | `log(day_var(Low))` | -1.17 | -1.17 | -0.89 | +0.39 | `ts_max(cross_corr(ts_max(day_last(Amt), 20), day_var(Low), 241), 20)` |
| swap | `Amt->Volume` | -1.17 | -1.17 | -0.85 | — | `ts_max(cross_corr(ts_max(day_last(Volume), 20), log(day_var(Low)), 241), 20)` |
| swap | `Low->High` | -0.73 | -0.73 | -0.64 | — | `ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(High)), 241), 20)` |
| window | `ts_max@20->10` | -0.83 | -0.83 | -0.77 | — | `ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 10)` |
| window | `ts_max@20->40` | -0.64 | -0.63 | -0.64 | — | `ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` — enrichment,均值差 +1.36,p 0.004
2. `cross_delay(cross_zscore(log(day_var(Ret)), 60), 1)` — enrichment,均值差 +1.31,p 0.003
3. `cross_zscore(log(day_var(Ret)), 60)` — enrichment,均值差 +1.31,p 0.003
4. `log(log(day_var(Ret)))` — enrichment,均值差 +1.29,p 0.004
5. `log(day_var(Ret))` — enrichment,均值差 +1.02,p 0.000
6. `day_var(replace_small_with_nan(Amt))` — enrichment,均值差 +0.97,p 0.000
7. `log(day_var(Amt))` — enrichment,均值差 +0.93,p 0.022
8. `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` — enrichment,均值差 +0.73,p 0.001
9. `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` — enrichment,均值差 +0.63,p 0.001
10. `pow_2(day_mean(replace_small_with_nan(Amt)))` — enrichment,均值差 +0.61,p 0.001
11. `day_mean(replace_small_with_nan(Amt))` — enrichment,均值差 +0.61,p 0.001
12. `day_var(Ret)` — enrichment,均值差 +0.44,p 0.009
13. `day_var(Amt)` — enrichment,均值差 +0.36,p 0.097

## 本组之前各轮的任务

- `prods2046Pr1a_Ea`:核心 `day_var(Low)`;评分 97,过线 0,入 heads 0;采样计数 {'c05_skeleton': 506, 'c05_no_core': 1097}
  - score -0.41(train -0.19 valid -0.41):`cross_reg_tvalue(cross_delay(day_var(Low), 1), cs_demean(day_sum(Ret)), 120)`
  - score -0.47(train -0.47 valid -0.46):`cross_corr(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), day_sum(Ret), 120)`
  - score -0.53(train -0.53 valid +0.02):`cross_reg_tvalue(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), cs_demean(day_sum(Ret)), 120)`
  - score -0.59(train -0.59 valid -0.59):`cross_reg_tvalue(cross_delay(day_var(Low), 1), day_sum(Ret), 120)`
  - score -0.61(train -0.53 valid -0.61):`cross_corr(cross_delay(day_var(Low), 1), day_sum(Ret), 120)`
- `prods2046Pr1b_Nb`:核心 `—`;评分 99,过线 3,入 heads 1;采样计数 {'c05_skeleton': 3}
  - score +0.88(train +1.36 valid +0.88):`cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 120)`
  - score +0.88(train +1.36 valid +0.88):`cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(replace_small_with_nan(Amt))))))), 1), day_var(replace_small_with_nan(Amt)), 120)`
  - score +0.75(train +1.18 valid +0.75):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Amt)), 120)`
  - score +0.34(train +0.73 valid +0.34):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(Amt)))), 1), log(day_var(Ret)), 120)`
  - score +0.30(train +0.64 valid +0.30):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), log(day_var(replace_small_with_nan(Amt))), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(window ts_max@20->40):`ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 40)`
- 增益 +0.11(window cross_corr@120->240):`cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 240)`
