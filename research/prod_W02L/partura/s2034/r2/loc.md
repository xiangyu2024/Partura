# 定位:种子 2034,P 组,第 2 轮(只含 train / valid)

快照:prods2034M1_I0_open_search, prods2034M2_I0_open_search, prods2034Pr1a_Na, prods2034Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.60 | -0.60 | -0.05 | +1 | 20 | prods2034M1_I0_open_search | `cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10), cross_mean(day_sum(Amt), 30))` |
| -0.80 | -0.80 | -0.66 | +1 | 0 | prods2034M1_I0_open_search | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` |
| -1.34 | -1.17 | -1.34 | -1 | 5 | prods2034M1_I0_open_search | `ts_decay_linear(day_sum(Volume), 5)` |
| -1.88 | -1.88 | -1.28 | +1 | 5 | prods2034M2_I0_open_search | `cross_stddev(div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume)), 20)` |
| -2.14 | -2.14 | -2.11 | +1 | 20 | prods2034M2_I0_open_search | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume)), 20)` |
| -2.35 | -1.59 | -2.35 | +1 | 20 | prods2034M2_I0_open_search | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 20)` |

## 共性:150 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.58 | 0.000 | 96 | -1.52 / -3.10 | `day_sum(Amt)` |
| +1.34 | 0.000 | 74 | -1.41 / -2.75 | `log(day_sum(Amt))` |
| +1.19 | 0.000 | 19 | -1.05 / -2.24 | `cross_mean(log(day_sum(Amt)), 120)` |
| +1.13 | 0.000 | 30 | -1.19 / -2.31 | `ts_max(day_sum(Amt), 50)` |
| +1.11 | 0.000 | 25 | -1.16 / -2.27 | `cross_mean(day_sum(Amt), 120)` |
| +1.08 | 0.000 | 24 | -1.18 / -2.26 | `div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120))` |
| +1.00 | 0.000 | 22 | -1.23 / -2.23 | `ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25)` |
| +1.00 | 0.001 | 17 | -1.20 / -2.20 | `ts_max(log(day_sum(Amt)), 50)` |
| +0.99 | 0.023 | 4 | -1.13 / -2.11 | `cross_max(log(day_sum(Amt)), 25)` |
| +0.90 | 0.039 | 7 | -1.23 / -2.13 | `cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120))` |
| +0.80 | 0.015 | 9 | -1.34 / -2.14 | `cross_delay(log(day_sum(Amt)), 1)` |
| +0.78 | 0.005 | 18 | -1.40 / -2.18 | `cross_zscore(log(day_sum(Amt)), 60)` |
| +0.74 | 0.025 | 10 | -1.40 / -2.14 | `cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1)` |
| +0.37 | 0.064 | 32 | -1.80 / -2.17 | `day_sum(Ret)` |
| -0.07 | 0.613 | 4 | -2.15 / -2.09 | `log(day_sum(Ret))` |
| -0.61 | 0.963 | 6 | -2.68 / -2.06 | `log(day_std(Ret))` |
| -0.61 | 0.963 | 6 | -2.68 / -2.06 | `day_std(Ret)` |
| -1.39 | 1.000 | 26 | -3.24 / -1.85 | `day_sum(Volume)` |

## 拆解(32 次评估)

### head score -0.60:`cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10), cross_mean(day_sum(Amt), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10)` | -0.71 | -0.71 | -0.33 | — | (子树本身) |
| sufficiency | `ts_std(ts_decay_linear(day_sum(Amt), 50), 10)` | -0.93 | -0.93 | -0.46 | — | (子树本身) |
| sufficiency | `ts_decay_linear(day_sum(Amt), 50)` | -3.18 | -2.52 | -3.18 | — | (子树本身) |
| sufficiency | `cross_mean(day_sum(Amt), 30)` | -3.17 | -2.59 | -3.17 | — | (子树本身) |
| knockout | `ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10)` | -0.42 | -0.42 | -0.26 | -0.18 | `cs_bucket_zscore(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), cross_mean(day_sum(Amt), 30))` |
| knockout | `ts_std(ts_decay_linear(day_sum(Amt), 50), 10)` | -1.92 | -1.92 | -1.22 | +1.32 | `cs_bucket_zscore(ts_max(ts_decay_linear(day_sum(Amt), 50), 10), cross_mean(day_sum(Amt), 30))` |
| knockout | `ts_decay_linear(day_sum(Amt), 50)` | -2.17 | -2.17 | -1.46 | +1.56 | `cs_bucket_zscore(ts_max(ts_std(day_sum(Amt), 10), 10), cross_mean(day_sum(Amt), 30))` |
| knockout | `cross_mean(day_sum(Amt), 30)` | -1.15 | -1.15 | -1.09 | +0.55 | `cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10), day_sum(Amt))` |
| swap | `Amt->Volume` | -1.25 | -1.04 | -1.25 | — | `cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Volume), 50), 10), 10), cross_mean(day_sum(Volume), 30))` |
| window | `ts_max@10->5` | -0.53 | -0.53 | -0.33 | — | `cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 5), cross_mean(day_sum(Amt), 30))` |
| window | `ts_max@10->20` | -0.66 | -0.49 | -0.66 | — | `cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 20), cross_mean(day_sum(Amt), 30))` |

### head score -1.88:`cross_stddev(div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume))` | -3.63 | -3.60 | -3.63 | — | (子树本身) |
| sufficiency | `day_sum(in_topk_masked(Volume, Volume, 5))` | -1.28 | -1.15 | -1.28 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume))` | -1.21 | -1.21 | -1.05 | -0.67 | `cross_stddev(day_sum(in_topk_masked(Volume, Volume, 5)), 20)` |
| swap | `Volume->Amt` | -1.93 | -1.93 | -1.21 | — | `cross_stddev(div(day_sum(in_topk_masked(Amt, Amt, 5)), day_sum(Amt)), 20)` |
| window | `cross_stddev@20->10` | -1.90 | -1.90 | -1.26 | — | `cross_stddev(div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume)), 10)` |
| window | `cross_stddev@20->40` | -2.31 | -2.31 | -2.06 | — | `cross_stddev(div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume)), 40)` |

### head score -2.14:`cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume))` | -2.80 | -2.80 | -2.44 | — | (子树本身) |
| sufficiency | `day_sum(in_topk_masked(Ret, Volume, 20))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume))` | -1.16 | -1.04 | -1.16 | -0.98 | `cross_mean(day_sum(in_topk_masked(Ret, Volume, 20)), 20)` |
| swap | `Volume->Amt` | -2.13 | -2.09 | -2.13 | — | `cross_mean(div(day_sum(in_topk_masked(Ret, Amt, 20)), day_sum(Amt)), 20)` |
| window | `cross_mean@20->10` | -2.16 | -2.16 | -2.14 | — | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume)), 10)` |
| window | `cross_mean@20->40` | -2.29 | -1.87 | -2.29 | — | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume)), 40)` |

### head score -2.35:`cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume))` | -3.23 | -2.26 | -3.23 | — | (子树本身) |
| sufficiency | `day_sum(in_topk_masked(Ret, Volume, 50))` | -1.35 | -1.25 | -1.35 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume))` | -1.11 | -1.00 | -1.11 | -1.24 | `cross_mean(day_sum(in_topk_masked(Ret, Volume, 50)), 20)` |
| swap | `Volume->Amt` | -2.29 | -1.62 | -2.29 | — | `cross_mean(div(day_sum(in_topk_masked(Ret, Amt, 50)), day_sum(Amt)), 20)` |
| window | `cross_mean@20->10` | -2.19 | -1.59 | -2.19 | — | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 10)` |
| window | `cross_mean@20->40` | -2.18 | -1.43 | -2.18 | — | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_sum(Amt)` — enrichment,均值差 +1.58,p 0.000
2. `log(day_sum(Amt))` — enrichment,均值差 +1.34,p 0.000
3. `cross_mean(log(day_sum(Amt)), 120)` — enrichment,均值差 +1.19,p 0.000
4. `ts_max(day_sum(Amt), 50)` — enrichment,均值差 +1.13,p 0.000
5. `cross_mean(day_sum(Amt), 120)` — enrichment,均值差 +1.11,p 0.000
6. `div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120))` — enrichment,均值差 +1.08,p 0.000
7. `ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25)` — enrichment,均值差 +1.00,p 0.000
8. `ts_max(log(day_sum(Amt)), 50)` — enrichment,均值差 +1.00,p 0.001
9. `cross_max(log(day_sum(Amt)), 25)` — enrichment,均值差 +0.99,p 0.023
10. `cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120))` — enrichment,均值差 +0.90,p 0.039
11. `cross_delay(log(day_sum(Amt)), 1)` — enrichment,均值差 +0.80,p 0.015
12. `cross_zscore(log(day_sum(Amt)), 60)` — enrichment,均值差 +0.78,p 0.005
13. `cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1)` — enrichment,均值差 +0.74,p 0.025
14. `day_sum(Ret)` — enrichment,均值差 +0.37,p 0.064

## 本组之前各轮的任务

- `prods2034Pr1a_Na`:核心 `—`;评分 89,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.01(train +0.05 valid +0.01):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 20), cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120)))`
  - score -0.02(train -0.02 valid +0.17):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120)))`
  - score -0.04(train -0.04 valid +0.13):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(log(day_sum(Amt))), 120)))`
  - score -0.34(train +0.18 valid -0.34):`cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120))`
  - score -0.39(train -0.39 valid +0.09):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), cs_regres(ts_max(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), 50), cross_mean(log(day_sum(Amt)), 120)))`
- `prods2034Pr1b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 12}
  - score -0.21(train -0.21 valid +0.50):`cross_corr(cross_delay(day_sum(Amt), 1), day_sum(Ret), 241)`
  - score -0.49(train -0.41 valid -0.49):`cross_corr(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 120)`
  - score -0.59(train -0.59 valid +0.60):`cross_regbeta(cross_zscore(log(day_sum(Amt)), 60), day_wmean(Ret, Amt), 60)`
  - score -0.63(train -0.63 valid +0.05):`cross_regbeta(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 120)`
  - score -0.77(train -0.70 valid -0.77):`cross_corr(cross_delay(log(day_sum(Amt)), 1), day_sum(Amt), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(knockout ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10)):`cs_bucket_zscore(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), cross_mean(day_sum(Amt), 30))`
- 增益 +0.17(window cross_mean@20->40):`cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 40)`
- 增益 +0.16(window cross_mean@20->10):`cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 10)`
