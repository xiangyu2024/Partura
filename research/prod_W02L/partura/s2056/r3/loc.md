# 定位:种子 2056,P 组,第 3 轮(只含 train / valid)

快照:prods2056M1_I0_open_search, prods2056M2_I0_open_search, prods2056M3_I0_open_search, prods2056Pr1a_Ea, prods2056Pr1b_Nb, prods2056Pr2a_Ea, prods2056Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.98 | +1.42 | +0.98 | +1 | 0 | prods2056Pr1b_Nb | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 120)` |
| -0.20 | -0.02 | -0.20 | +1 | 5 | prods2056M1_I0_open_search | `day_max(cross_corr(Amt, Ret, 180))` |
| -0.88 | -0.44 | -0.88 | +1 | 5 | prods2056M1_I0_open_search | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)` |
| -1.11 | -1.11 | -0.89 | +1 | 20 | prods2056M3_I0_open_search | `ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40), 10)` |
| -1.29 | -1.29 | -0.86 | +1 | 20 | prods2056M3_I0_open_search | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 30)` |
| -1.55 | -1.55 | -0.88 | +1 | 20 | prods2056M3_I0_open_search | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 20)` |
| -1.66 | -1.43 | -1.66 | -1 | 5 | prods2056M1_I0_open_search | `day_max(cross_corr(Ret, Ret, 15))` |
| -1.68 | -1.68 | -1.21 | -1 | 20 | prods2056M2_I0_open_search | `cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 5)` |
| -1.72 | -1.30 | -1.72 | -1 | 5 | prods2056M2_I0_open_search | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), 30))` |
| -1.80 | -1.59 | -1.80 | +1 | 5 | prods2056M2_I0_open_search | `cross_min(day_argmax(cross_corr(Amt, Ret, 60)), 15)` |

## 共性:225 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.36 | 0.003 | 4 | -0.49 / -1.85 | `day_signed_ratio(Amt, cross_delay(cross_mean(Amt, 20), 1))` |
| +1.25 | 0.002 | 6 | -0.62 / -1.86 | `day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60))` |
| +1.18 | 0.017 | 5 | -0.68 / -1.86 | `day_std(Vwap)` |
| +1.10 | 0.004 | 6 | -0.76 / -1.86 | `day_first(cross_delay(cross_mean(Amt, 20), 1))` |
| +0.91 | 0.029 | 5 | -0.94 / -1.85 | `cross_delay(day_std(Amt), 1)` |
| +0.84 | 0.038 | 6 | -1.01 / -1.85 | `cross_delay(div(day_std(Amt), day_first(Open)), 1)` |
| +0.79 | 0.013 | 11 | -1.08 / -1.87 | `ts_skew(div(day_std(Amt), day_sum(Amt)), 50)` |
| +0.72 | 0.004 | 24 | -1.18 / -1.91 | `day_max(cross_corr(Amt, Ret, 60))` |
| +0.70 | 0.055 | 8 | -1.15 / -1.86 | `div(day_std(Amt), day_first(Open))` |
| +0.70 | 0.004 | 22 | -1.20 / -1.90 | `cross_delay(div(day_std(Amt), day_sum(Amt)), 1)` |
| +0.63 | 0.062 | 8 | -1.22 / -1.85 | `day_corr(Amt, cross_mean(Amt, 20))` |
| +0.57 | 0.002 | 95 | -1.50 / -2.07 | `day_sum(Amt)` |
| +0.56 | 0.021 | 19 | -1.32 / -1.88 | `day_std(Ret)` |
| +0.55 | 0.179 | 5 | -1.29 / -1.84 | `pow_1_5(ts_skew(div(day_std(Amt), day_sum(Amt)), 50))` |
| +0.55 | 0.001 | 74 | -1.46 / -2.01 | `day_std(Amt)` |
| +0.51 | 0.004 | 54 | -1.45 / -1.95 | `div(day_std(Amt), day_sum(Amt))` |
| +0.41 | 0.339 | 4 | -1.43 / -1.84 | `cross_delay(div(day_last(Close), day_first(Open)), 1)` |
| +0.25 | 0.073 | 44 | -1.63 / -1.88 | `day_last(Close)` |
| +0.21 | 0.146 | 48 | -1.66 / -1.88 | `day_first(Open)` |
| +0.12 | 0.550 | 10 | -1.71 / -1.84 | `day_min(Ret)` |

## 拆解(33 次评估)

### head score +0.98:`cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(div(day_std(Volume), day_sum(Volume)), 1)` | -4.07 | -4.00 | -4.07 | — | (子树本身) |
| sufficiency | `div(day_std(Volume), day_sum(Volume))` | -3.89 | -3.89 | -3.84 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_std(Volume)` | -1.21 | -1.10 | -1.21 | — | (子树本身) |
| knockout | `cross_delay(div(day_std(Volume), day_sum(Volume)), 1)` | +0.30 | +0.77 | +0.30 | +0.67 | `cross_corr(day_sum(Volume), div(day_std(Volume), day_sum(Volume)), 120)` |
| knockout | `div(day_std(Volume), day_sum(Volume))` | -0.28 | -0.26 | -0.28 | +1.26 | `cross_corr(day_sum(Volume), cross_delay(day_std(Volume), 1), 120)` |
| swap | `Volume->Amt` | +0.76 | +1.53 | +0.76 | — | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 120)` |
| window | `cross_corr@120->60` | +0.55 | +0.55 | +0.72 | — | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 60)` |
| window | `cross_corr@120->240` | +1.41 | +1.41 | +1.52 | — | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 240)` |

### head score -1.11:`ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40)` | -2.70 | -2.36 | -2.70 | — | (子树本身) |
| sufficiency | `sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_durbin_watson(nt_cs_quantile_q25(Amt))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40)` | -3.39 | -3.08 | -3.39 | +2.28 | `ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10)` |
| knockout | `sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt)))` | -1.68 | -1.68 | -1.09 | +0.57 | `ts_stddev(ts_stddev(day_durbin_watson(nt_cs_quantile_q25(Amt)), 40), 10)` |
| swap | `Amt->Volume` | -0.45 | -0.45 | +0.08 | — | `ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Volume))), 40), 10)` |
| window | `ts_stddev@10->5` | -2.61 | -1.81 | -2.61 | — | `ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40), 5)` |
| window | `ts_stddev@10->20` | -0.96 | -0.96 | -0.63 | — | `ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40), 20)` |

### head score -1.29:`ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10)` | -3.15 | -3.15 | -2.98 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_durbin_watson(nt_cs_quantile_q25(Amt))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10)` | -2.13 | -2.13 | -2.04 | +0.84 | `ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 30)` |
| knockout | `sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt)))` | -2.25 | -1.75 | -2.25 | +0.96 | `ts_stddev(ts_stddev(day_durbin_watson(nt_cs_quantile_q25(Amt)), 10), 30)` |
| swap | `Amt->Volume` | -1.36 | -1.36 | -0.81 | — | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Volume))), 10), 30)` |
| window | `ts_stddev@30->15` | -1.70 | -1.70 | -1.34 | — | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 15)` |
| window | `ts_stddev@30->60` | -0.77 | -0.70 | -0.77 | — | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 60)` |

### head score -1.55:`ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10)` | -3.15 | -3.15 | -2.98 | — | (子树本身) |
| sufficiency | `sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_durbin_watson(nt_cs_quantile_q25(Amt))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10)` | -2.64 | -2.64 | -2.48 | +1.09 | `ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 20)` |
| knockout | `sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt)))` | -2.11 | -2.02 | -2.11 | +0.57 | `ts_stddev(ts_stddev(day_durbin_watson(nt_cs_quantile_q25(Amt)), 10), 20)` |
| swap | `Amt->Volume` | -1.50 | -1.50 | -0.36 | — | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Volume))), 10), 20)` |
| window | `ts_stddev@20->10` | -1.75 | -1.75 | -1.37 | — | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 10)` |
| window | `ts_stddev@20->40` | -0.97 | -0.97 | -0.81 | — | `ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_signed_ratio(Amt, cross_delay(cross_mean(Amt, 20), 1))` — enrichment,均值差 +1.36,p 0.003
2. `day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60))` — enrichment,均值差 +1.25,p 0.002
3. `day_std(Vwap)` — enrichment,均值差 +1.18,p 0.017
4. `day_first(cross_delay(cross_mean(Amt, 20), 1))` — enrichment,均值差 +1.10,p 0.004
5. `cross_delay(day_std(Amt), 1)` — enrichment,均值差 +0.91,p 0.029
6. `cross_delay(div(day_std(Amt), day_first(Open)), 1)` — enrichment,均值差 +0.84,p 0.038
7. `ts_skew(div(day_std(Amt), day_sum(Amt)), 50)` — enrichment,均值差 +0.79,p 0.013
8. `day_max(cross_corr(Amt, Ret, 60))` — enrichment,均值差 +0.72,p 0.004
9. `div(day_std(Amt), day_first(Open))` — enrichment,均值差 +0.70,p 0.055
10. `cross_delay(div(day_std(Amt), day_sum(Amt)), 1)` — enrichment,均值差 +0.70,p 0.004
11. `day_corr(Amt, cross_mean(Amt, 20))` — enrichment,均值差 +0.63,p 0.062
12. `day_sum(Amt)` — enrichment,均值差 +0.57,p 0.002
13. `day_std(Ret)` — enrichment,均值差 +0.56,p 0.021
14. `day_std(Amt)` — enrichment,均值差 +0.55,p 0.001
15. `div(day_std(Amt), day_sum(Amt))` — enrichment,均值差 +0.51,p 0.004
16. `day_last(Close)` — enrichment,均值差 +0.25,p 0.073

## 本组之前各轮的任务

- `prods2056Pr1a_Ea`:核心 `day_max(cross_corr(Amt, Ret, 60))`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 959, 'c05_no_core': 1909, 'mutation_refused': 2}
  - score -0.08(train -0.08 valid +0.16):`mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60)))), mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60))))`
  - score -0.20(train -0.20 valid +0.09):`mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60)))`
  - score -0.53(train -0.53 valid -0.23):`mul(sub(day_max(in_slice(cross_corr(Volume, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60)))`
  - score -0.70(train -0.70 valid -0.55):`sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60)))`
  - score -0.75(train -0.75 valid -0.72):`sub(day_max(cross_corr(Amt, Ret, 60)), cross_mean(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), 60))`
- `prods2056Pr1b_Nb`:核心 `—`;评分 86,过线 1,入 heads 1;采样计数 {'c05_skeleton': 5}
  - score +0.52(train +0.70 valid +0.52):`cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 60)`
  - score -0.20(train +0.01 valid -0.20):`cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_first(Open)), 1), 60)`
  - score -0.59(train -0.16 valid -0.59):`cross_corr(day_sum(Amt), cross_delay(day_std(Amt), 1), 60)`
  - score -0.66(train +0.27 valid -0.66):`cross_corr(day_std(Amt), day_min(Ret), 60)`
  - score -0.82(train -0.65 valid -0.82):`cross_corr(cross_corr(day_sum(Amt), cross_delay(day_std(Amt), 1), 60), cross_delay(day_std(Amt), 1), 60)`
- `prods2056Pr2a_Ea`:核心 `div(day_std(Amt), day_sum(Amt))`;评分 104,过线 0,入 heads 0;采样计数 {'c05_skeleton': 743, 'c05_no_core': 1552, 'c05_periphery_seen': 1}
  - score +0.48(train +0.48 valid +0.62):`cross_corr(day_std(Ret), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 90)`
  - score +0.29(train +0.58 valid +0.29):`cross_corr(day_std(Vwap), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 90)`
  - score +0.17(train +0.68 valid +0.17):`cross_corr(day_std(Close), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 90)`
  - score +0.11(train +0.56 valid +0.11):`cross_corr(day_std(Ret), cross_delay(cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 1), 90)`
  - score +0.03(train +0.77 valid +0.03):`cross_corr(day_es_ratio_lo(Vwap), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 90)`
- `prods2056Pr2b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.19(train -0.19 valid +0.62):`cross_corr(day_signed_ratio(Amt, cross_delay(cross_mean(Amt, 20), 1)), div(cross_corr(day_signed_ratio(Amt, cross_delay(cross_mean(Amt, 20), 1)), mul(day_last(Close), day_first(cross_delay(cross_mean(Amt, 20), 1))), 60), day_first(cross_delay(cross_mean(Amt, 20), 1))), 60)`
  - score -0.26(train -0.26 valid +0.61):`cross_corr(day_signed_ratio(Amt, cross_delay(cross_mean(Amt, 20), 1)), div(cross_corr(day_signed_ratio(Amt, cross_delay(cross_mean(Amt, 20), 1)), div(day_last(Close), day_first(cross_delay(cross_mean(Amt, 20), 1))), 60), day_first(cross_delay(cross_mean(Amt, 20), 1))), 60)`
  - score -0.44(train -0.44 valid -0.40):`cross_corr(day_signed_ratio(Amt, cross_delay(cross_mean(cross_mean(Amt, 20), 20), 1)), div(day_last(Close), day_first(cross_delay(cross_mean(cross_mean(Amt, 20), 20), 1))), 60)`
  - score -0.48(train -0.48 valid -0.08):`cross_corr(day_corr(Amt, cross_mean(Amt, 241)), div(day_last(Close), day_first(Open)), 60)`
  - score -0.57(train -0.57 valid -0.54):`cross_corr(day_corr(Amt, cross_mean(Amt, 20)), day_first(Open), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.66(swap Amt->Volume):`ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Volume))), 40), 10)`
- 增益 +0.58(window ts_stddev@20->40):`ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 40)`
- 增益 +0.52(window ts_stddev@30->60):`ts_stddev(ts_stddev(sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt))), 10), 60)`
- 增益 +0.43(window cross_corr@120->240):`cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 240)`
- 增益 +0.15(window ts_stddev@10->20):`ts_stddev(ts_stddev(sigmoid(day_durbin_watson(nt_cs_quantile_q25(Amt))), 40), 20)`
