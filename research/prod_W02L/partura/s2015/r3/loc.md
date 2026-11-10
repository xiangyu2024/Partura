# 定位:种子 2015,P 组,第 3 轮(只含 train / valid)

快照:prods2015M1_I0_open_search, prods2015M2_I0_open_search, prods2015M3_I0_open_search, prods2015Pr1a_Ea, prods2015Pr1b_Nb, prods2015Pr2a_Ea, prods2015Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.59 | +0.59 | +1.21 | +1 | 20 | prods2015Pr2a_Ea | `div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))` |
| -0.30 | -0.30 | +0.62 | +1 | 0 | prods2015M1_I0_open_search | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 50)` |
| -0.42 | -0.42 | -0.12 | +1 | 5 | prods2015M1_I0_open_search | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 40)` |
| -0.71 | -0.71 | -0.31 | +1 | 20 | prods2015M1_I0_open_search | `ts_std(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 10)` |
| -1.32 | -1.17 | -1.32 | -1 | 5 | prods2015M2_I0_open_search | `add(ts_quantile_q50(cross_max(day_close(Volume), 5), 1), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))` |
| -1.42 | -1.07 | -1.42 | -1 | 20 | prods2015M3_I0_open_search | `cs_mask_top_replace_mean(day_quantile_q75(add(High, day_close(Volume))))` |
| -1.42 | -1.07 | -1.42 | -1 | 20 | prods2015M3_I0_open_search | `cs_mask_top_replace_mean(day_quantile_q75(add(Open, day_close(Volume))))` |
| -1.42 | -1.07 | -1.42 | -1 | 20 | prods2015M3_I0_open_search | `cs_mask_top_replace_mean(day_quantile_q75(add(add(High, day_close(Volume)), day_close(Volume))))` |
| -1.69 | -1.55 | -1.69 | -1 | 5 | prods2015M2_I0_open_search | `ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)), 50)` |
| -1.72 | -1.55 | -1.72 | -1 | 0 | prods2015M2_I0_open_search | `ts_std(ts_quantile_q50(cross_max(day_close(Volume), 5), 40), 50)` |

## 共性:250 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.62 | 0.000 | 10 | -0.07 / -1.69 | `day_zero_ratio(Volume)` |
| +1.08 | 0.000 | 17 | -0.61 / -1.70 | `cross_semistd_pos(day_quantile_q25(Volume), 60)` |
| +1.08 | 0.000 | 13 | -0.60 / -1.68 | `sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))` |
| +1.01 | 0.000 | 71 | -0.90 / -1.91 | `sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))` |
| +0.97 | 0.020 | 4 | -0.66 / -1.64 | `cs_first_low20(day_min(High), day_min(Ret))` |
| +0.97 | 0.003 | 10 | -0.69 / -1.66 | `add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60)))` |
| +0.97 | 0.000 | 19 | -0.73 / -1.70 | `day_quantile_q25(Volume)` |
| +0.91 | 0.001 | 15 | -0.77 / -1.68 | `cross_semistd_neg(day_quantile_q25(Volume), 60)` |
| +0.86 | 0.000 | 86 | -1.06 / -1.92 | `cross_semistd_neg(day_quantile_q25(Amt), 60)` |
| +0.81 | 0.000 | 93 | -1.11 / -1.92 | `cross_semistd_pos(day_quantile_q25(Amt), 60)` |
| +0.58 | 0.011 | 17 | -1.08 / -1.66 | `cross_stddev(cross_stddev(day_median(Amt), 60), 60)` |
| +0.55 | 0.051 | 9 | -1.09 / -1.64 | `add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60))` |
| +0.49 | 0.103 | 7 | -1.14 / -1.64 | `day_min(Ret)` |
| +0.47 | 0.236 | 5 | -1.16 / -1.63 | `day_max(Volume)` |
| +0.47 | 0.236 | 5 | -1.16 / -1.63 | `cross_semistd_pos(day_max(Volume), 60)` |
| +0.44 | 0.037 | 19 | -1.22 / -1.66 | `cross_stddev(day_median(Amt), 60)` |
| +0.44 | 0.197 | 4 | -1.19 / -1.63 | `cross_stddev(cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60), 60)` |
| +0.43 | 0.036 | 23 | -1.23 / -1.66 | `day_median(Amt)` |
| +0.40 | 0.009 | 55 | -1.31 / -1.71 | `cross_stddev(day_quantile_q25(Amt), 60)` |
| +0.36 | 0.184 | 7 | -1.28 / -1.63 | `cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60)` |

## 拆解(24 次评估)

### head score +0.59:`div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60)))` | +0.06 | +0.28 | +0.06 | — | (子树本身) |
| sufficiency | `sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))` | +0.05 | +0.28 | +0.05 | — | (子树本身) |
| sufficiency | `sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))` | -0.30 | +0.18 | -0.30 | — | (子树本身) |
| sufficiency | `cross_semistd_neg(day_quantile_q25(Amt), 60)` | -2.98 | -2.41 | -2.98 | — | (子树本身) |
| knockout | `add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60)))` | +0.53 | +0.53 | +1.06 | +0.06 | `div(day_zero_ratio(Volume), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)))` |
| knockout | `sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))` | -2.76 | -2.76 | -2.27 | +3.35 | `div(day_zero_ratio(Volume), add(cross_semistd_neg(day_quantile_q25(Amt), 60), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))` |
| knockout | `sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))` | -2.79 | -2.79 | -2.29 | +3.38 | `div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), cross_semistd_neg(day_quantile_q25(Volume), 60)))` |
| knockout | `cross_semistd_neg(day_quantile_q25(Amt), 60)` | -1.50 | -1.50 | -1.15 | +2.09 | `div(day_zero_ratio(Volume), add(sub(day_quantile_q25(Amt), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))` |
| swap | `Volume->Amt` | +0.53 | +0.53 | +1.06 | — | `div(day_zero_ratio(Amt), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))))` |
| swap | `Amt->Volume` | +0.58 | +0.58 | +1.24 | — | `div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))` |
| window | `cross_semistd_neg@60->30` | +0.26 | +0.26 | +0.75 | — | `div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 30), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))` |
| window | `cross_semistd_neg@60->120` | +0.77 | +0.77 | +1.22 | — | `div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 120), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))` |

### head score -1.42:`cs_mask_top_replace_mean(day_quantile_q75(add(High, day_close(Volume))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q75(add(High, day_close(Volume)))` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_close(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| swap | `High->Low` | -1.49 | -1.07 | -1.49 | — | `cs_mask_top_replace_mean(day_quantile_q75(add(Low, day_close(Volume))))` |
| swap | `Volume->Amt` | -4.13 | -3.49 | -4.13 | — | `cs_mask_top_replace_mean(day_quantile_q75(add(High, day_close(Amt))))` |

### head score -1.42:`cs_mask_top_replace_mean(day_quantile_q75(add(Open, day_close(Volume))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q75(add(Open, day_close(Volume)))` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_close(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| swap | `Open->Close` | -1.49 | -1.07 | -1.49 | — | `cs_mask_top_replace_mean(day_quantile_q75(add(Close, day_close(Volume))))` |
| swap | `Volume->Amt` | -4.13 | -3.49 | -4.13 | — | `cs_mask_top_replace_mean(day_quantile_q75(add(Open, day_close(Amt))))` |

### head score -1.42:`cs_mask_top_replace_mean(day_quantile_q75(add(add(High, day_close(Volume)), day_close(Volume))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q75(add(add(High, day_close(Volume)), day_close(Volume)))` | -1.61 | -1.17 | -1.61 | — | (子树本身) |
| sufficiency | `day_close(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| swap | `High->Low` | -1.48 | -1.07 | -1.48 | — | `cs_mask_top_replace_mean(day_quantile_q75(add(add(Low, day_close(Volume)), day_close(Volume))))` |
| swap | `Volume->Amt` | -4.13 | -3.49 | -4.13 | — | `cs_mask_top_replace_mean(day_quantile_q75(add(add(High, day_close(Amt)), day_close(Amt))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_zero_ratio(Volume)` — enrichment,均值差 +1.62,p 0.000
2. `cross_semistd_pos(day_quantile_q25(Volume), 60)` — enrichment,均值差 +1.08,p 0.000
3. `sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))` — enrichment,均值差 +1.08,p 0.000
4. `sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))` — enrichment,均值差 +1.01,p 0.000
5. `cs_first_low20(day_min(High), day_min(Ret))` — enrichment,均值差 +0.97,p 0.020
6. `add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60)))` — enrichment,均值差 +0.97,p 0.003
7. `day_quantile_q25(Volume)` — enrichment,均值差 +0.97,p 0.000
8. `cross_semistd_neg(day_quantile_q25(Volume), 60)` — enrichment,均值差 +0.91,p 0.001
9. `cross_semistd_neg(day_quantile_q25(Amt), 60)` — enrichment,均值差 +0.86,p 0.000
10. `cross_semistd_pos(day_quantile_q25(Amt), 60)` — enrichment,均值差 +0.81,p 0.000
11. `cross_stddev(cross_stddev(day_median(Amt), 60), 60)` — enrichment,均值差 +0.58,p 0.011
12. `add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60))` — enrichment,均值差 +0.55,p 0.051
13. `cross_stddev(day_median(Amt), 60)` — enrichment,均值差 +0.44,p 0.037
14. `day_median(Amt)` — enrichment,均值差 +0.43,p 0.036
15. `cross_stddev(day_quantile_q25(Amt), 60)` — enrichment,均值差 +0.40,p 0.009
16. `cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60)` — enrichment,均值差 +0.31,p 0.049

## 本组之前各轮的任务

- `prods2015Pr1a_Ea`:核心 `cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60)`;评分 101,过线 0,入 heads 0;采样计数 {'c05_no_core': 1748, 'c05_skeleton': 864, 'mutation_refused': 3, 'c05_periphery_seen': 6}
  - score -0.47(train -0.47 valid -0.20):`div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60)))`
  - score -0.47(train -0.47 valid -0.19):`div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(cross_argmax(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60)))`
  - score -0.47(train -0.47 valid -0.20):`div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(cross_stddev(day_median(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60)))`
  - score -0.48(train -0.48 valid -0.19):`div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60))), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60)))`
  - score -0.48(train -0.48 valid -0.19):`div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(div(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), add(cross_stddev(cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60))), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60)))`
- `prods2015Pr1b_Nb`:核心 `—`;评分 70,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score +0.05(train +0.28 valid +0.05):`sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))`
  - score -0.51(train +0.05 valid -0.51):`div(cross_semistd_neg(day_quantile_q25(Amt), 60), add(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)))`
  - score -0.51(train +0.22 valid -0.51):`cross_autocorr_s1(cs_first_low20(day_min(High), day_min(Ret)), 60)`
  - score -0.58(train +0.06 valid -0.58):`cross_product(cross_autocorr_s1(cs_first_low20(day_min(High), day_min(Ret)), 60), 5)`
  - score -0.59(train -0.59 valid -0.59):`cross_product(cross_autocorr_s1(cs_first_low20(day_min(High), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))), 60), 5)`
- `prods2015Pr2a_Ea`:核心 `sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))`;评分 95,过线 3,入 heads 1;采样计数 {'c05_no_core': 1015, 'c05_skeleton': 504, 'c05_periphery_seen': 2, 'mutation_refused': 5}
  - score +0.59(train +0.59 valid +1.21):`div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))`
  - score +0.53(train +0.53 valid +1.06):`div(day_zero_ratio(Volume), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)))`
  - score +0.53(train +0.53 valid +1.06):`div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))))`
  - score +0.46(train +0.46 valid +1.22):`div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))`
  - score +0.38(train +0.62 valid +0.38):`add(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Amt), 120), cross_semistd_pos(day_quantile_q25(Amt), 120)))`
- `prods2015Pr2b_Nb`:核心 `—`;评分 99,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score +0.38(train +0.43 valid +0.38):`sub(cross_semistd_neg(day_max(Amt), 60), cross_semistd_pos(day_max(Volume), 60))`
  - score +0.32(train +0.32 valid +0.45):`sub(cross_semistd_neg(day_max(Amt), 60), cross_semistd_pos(day_max(Amt), 60))`
  - score +0.07(train +0.28 valid +0.07):`sub(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_tail_mean_q25(day_std(Ret), 60), sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))))`
  - score +0.05(train +0.28 valid +0.05):`sub(sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_pos(day_std(Ret), 60), cross_semistd_pos(day_std(Ret), 60)))`
  - score +0.05(train +0.28 valid +0.05):`sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window cross_semistd_neg@60->120):`div(day_zero_ratio(Volume), add(sub(cross_semistd_neg(day_quantile_q25(Amt), 120), cross_semistd_pos(day_quantile_q25(Amt), 60)), sub(cross_semistd_neg(day_quantile_q25(Volume), 60), cross_semistd_pos(day_quantile_q25(Volume), 60))))`
