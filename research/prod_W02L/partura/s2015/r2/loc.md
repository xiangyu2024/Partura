# 定位:种子 2015,P 组,第 2 轮(只含 train / valid)

快照:prods2015M1_I0_open_search, prods2015M2_I0_open_search, prods2015Pr1a_Ea, prods2015Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.30 | -0.30 | +0.62 | +1 | 0 | prods2015M1_I0_open_search | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 50)` |
| -0.42 | -0.42 | -0.12 | +1 | 5 | prods2015M1_I0_open_search | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 40)` |
| -0.71 | -0.71 | -0.31 | +1 | 20 | prods2015M1_I0_open_search | `ts_std(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 10)` |
| -1.32 | -1.17 | -1.32 | -1 | 5 | prods2015M2_I0_open_search | `add(ts_quantile_q50(cross_max(day_close(Volume), 5), 1), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))` |
| -1.69 | -1.55 | -1.69 | -1 | 5 | prods2015M2_I0_open_search | `ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)), 50)` |
| -1.72 | -1.55 | -1.72 | -1 | 0 | prods2015M2_I0_open_search | `ts_std(ts_quantile_q50(cross_max(day_close(Volume), 5), 40), 50)` |

## 共性:122 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.14 | 0.003 | 4 | -0.66 / -1.81 | `cs_first_low20(day_min(High), day_min(Ret))` |
| +0.83 | 0.000 | 55 | -1.31 / -2.14 | `cross_stddev(day_quantile_q25(Amt), 60)` |
| +0.80 | 0.000 | 17 | -1.08 / -1.88 | `cross_stddev(cross_stddev(day_median(Amt), 60), 60)` |
| +0.73 | 0.004 | 9 | -1.09 / -1.82 | `add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60))` |
| +0.66 | 0.024 | 7 | -1.14 / -1.81 | `day_min(Ret)` |
| +0.66 | 0.000 | 49 | -1.37 / -2.03 | `cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60)` |
| +0.65 | 0.001 | 19 | -1.22 / -1.87 | `cross_stddev(day_median(Amt), 60)` |
| +0.59 | 0.083 | 4 | -1.19 / -1.79 | `cross_stddev(cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60), 60)` |
| +0.59 | 0.001 | 22 | -1.29 / -1.87 | `day_median(Amt)` |
| +0.52 | 0.048 | 7 | -1.28 / -1.80 | `cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60)` |
| +0.46 | 0.092 | 8 | -1.34 / -1.80 | `day_min(High)` |
| +0.44 | 0.104 | 6 | -1.35 / -1.79 | `cross_mean(day_sum(Amt), 30)` |
| +0.44 | 0.104 | 6 | -1.35 / -1.79 | `day_sum(Amt)` |
| +0.25 | 0.271 | 6 | -1.53 / -1.78 | `add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(day_quantile_q25(Amt), 60))` |
| -0.04 | 0.667 | 4 | -1.81 / -1.77 | `sub(cross_semistd_neg(day_quantile_q25(Amt), 60), cross_semistd_pos(day_quantile_q25(Amt), 60))` |
| -0.04 | 0.741 | 12 | -1.81 / -1.76 | `cross_semistd_neg(day_quantile_q25(Amt), 60)` |
| -0.07 | 0.823 | 16 | -1.82 / -1.76 | `cross_semistd_pos(day_quantile_q25(Amt), 60)` |
| -0.07 | 0.757 | 8 | -1.83 / -1.76 | `day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5))` |
| -0.08 | 0.753 | 7 | -1.85 / -1.76 | `day_close(Volume)` |
| -0.08 | 0.753 | 7 | -1.85 / -1.76 | `cross_max(day_close(Volume), 5)` |

## 拆解(23 次评估)

### head score -1.32:`add(ts_quantile_q50(cross_max(day_close(Volume), 5), 1), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q50(cross_max(day_close(Volume), 5), 1)` | -1.38 | -1.17 | -1.38 | — | (子树本身) |
| sufficiency | `cross_max(day_close(Volume), 5)` | -1.38 | -1.17 | -1.38 | — | (子树本身) |
| sufficiency | `day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5))` | -2.37 | -1.57 | -2.37 | — | (子树本身) |
| sufficiency | `day_close(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| knockout | `ts_quantile_q50(cross_max(day_close(Volume), 5), 1)` | -1.39 | -1.17 | -1.39 | +0.07 | `add(cross_max(day_close(Volume), 5), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))` |
| knockout | `cross_max(day_close(Volume), 5)` | -1.61 | -1.18 | -1.61 | +0.29 | `add(ts_quantile_q50(day_close(Volume), 1), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))` |
| swap | `Volume->Amt` | -4.21 | -3.33 | -4.21 | — | `add(ts_quantile_q50(cross_max(day_close(Amt), 5), 1), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))` |
| swap | `Low->High` | -1.39 | -1.17 | -1.39 | — | `add(ts_quantile_q50(cross_max(day_close(Volume), 5), 1), day_quantile_q25(sliding_top_sum_masked_p5(High, High, 5)))` |
| window | `ts_quantile_q50@1->2` | -1.43 | -1.22 | -1.43 | — | `add(ts_quantile_q50(cross_max(day_close(Volume), 5), 2), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)))` |

### head score -1.69:`ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5))` | -2.37 | -1.57 | -2.37 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| swap | `Low->High` | -1.71 | -1.57 | -1.71 | — | `ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(High, High, 5)), 50)` |
| swap | `High->Low` | -1.73 | -1.57 | -1.73 | — | `ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, Low, 5)), 50)` |
| window | `ts_cov@50->25` | -1.77 | -1.42 | -1.77 | — | `ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)), 25)` |
| window | `ts_cov@50->100` | -1.56 | -1.56 | -1.39 | — | `ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)), 100)` |

### head score -1.72:`ts_std(ts_quantile_q50(cross_max(day_close(Volume), 5), 40), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q50(cross_max(day_close(Volume), 5), 40)` | -1.85 | -1.39 | -1.85 | — | (子树本身) |
| sufficiency | `cross_max(day_close(Volume), 5)` | -1.38 | -1.17 | -1.38 | — | (子树本身) |
| sufficiency | `day_close(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| knockout | `ts_quantile_q50(cross_max(day_close(Volume), 5), 40)` | -1.42 | -1.14 | -1.42 | -0.30 | `ts_std(cross_max(day_close(Volume), 5), 50)` |
| knockout | `cross_max(day_close(Volume), 5)` | -1.79 | -1.51 | -1.79 | +0.07 | `ts_std(ts_quantile_q50(day_close(Volume), 40), 50)` |
| swap | `Volume->Amt` | -1.40 | -1.40 | -1.12 | — | `ts_std(ts_quantile_q50(cross_max(day_close(Amt), 5), 40), 50)` |
| window | `ts_std@50->25` | -1.74 | -1.57 | -1.74 | — | `ts_std(ts_quantile_q50(cross_max(day_close(Volume), 5), 40), 25)` |
| window | `ts_std@50->100` | -2.03 | -1.66 | -2.03 | — | `ts_std(ts_quantile_q50(cross_max(day_close(Volume), 5), 40), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(day_min(High), day_min(Ret))` — enrichment,均值差 +1.14,p 0.003
2. `cross_stddev(day_quantile_q25(Amt), 60)` — enrichment,均值差 +0.83,p 0.000
3. `cross_stddev(cross_stddev(day_median(Amt), 60), 60)` — enrichment,均值差 +0.80,p 0.000
4. `add(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), cross_stddev(cross_stddev(day_median(Amt), 60), 60))` — enrichment,均值差 +0.73,p 0.004
5. `day_min(Ret)` — enrichment,均值差 +0.66,p 0.024
6. `cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60)` — enrichment,均值差 +0.66,p 0.000
7. `cross_stddev(day_median(Amt), 60)` — enrichment,均值差 +0.65,p 0.001
8. `cross_stddev(cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60), 60)` — enrichment,均值差 +0.59,p 0.083
9. `day_median(Amt)` — enrichment,均值差 +0.59,p 0.001
10. `cross_stddev(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 60)` — enrichment,均值差 +0.52,p 0.048
11. `day_min(High)` — enrichment,均值差 +0.46,p 0.092

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(window ts_cov@50->100):`ts_cov(day_quantile_q25(Ret), day_quantile_q25(sliding_top_sum_masked_p5(Low, High, 5)), 100)`
