# 定位:种子 2025,P 组,第 2 轮(只含 train / valid)

快照:prods2025M1_I0_open_search, prods2025M2_I0_open_search, prods2025Pr1a_Ea, prods2025Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.72 | -0.72 | -0.39 | +1 | 0 | prods2025M1_I0_open_search | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 80)` |
| -1.42 | -1.28 | -1.42 | -1 | 5 | prods2025M2_I0_open_search | `day_sum(in_slice(Volume, 2, 237))` |
| -1.53 | -1.34 | -1.53 | -1 | 20 | prods2025M2_I0_open_search | `day_sum(in_slice(Volume, 238, 240))` |
| -1.69 | -1.61 | -1.69 | -1 | 0 | prods2025M1_I0_open_search | `ts_mean(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)` |
| -2.35 | -2.35 | -1.85 | +1 | 20 | prods2025M2_I0_open_search | `cross_mean(div(day_sum(mul(in_slice(Ret, 191, 240), in_slice(Volume, 191, 240))), day_sum(in_slice(Volume, 191, 240))), 20)` |
| -2.47 | -2.00 | -2.47 | +1 | 5 | prods2025M1_I0_open_search | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` |

## 共性:126 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.48 | 0.004 | 4 | -0.79 / -2.27 | `day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5))` |
| +1.39 | 0.001 | 8 | -0.92 / -2.31 | `day_median(Vwap)` |
| +1.37 | 0.001 | 7 | -0.92 / -2.30 | `cs_last_high10(sub(LogTotalCap, day_centroid(High)), day_median(Vwap))` |
| +1.03 | 0.040 | 5 | -1.23 / -2.26 | `sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |
| +1.00 | 0.000 | 46 | -1.58 / -2.59 | `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |
| +0.99 | 0.000 | 47 | -1.60 / -2.59 | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` |
| +0.98 | 0.047 | 5 | -1.28 / -2.26 | `cross_ema(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 5)` |
| +0.93 | 0.019 | 9 | -1.36 / -2.29 | `sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |
| +0.86 | 0.044 | 7 | -1.41 / -2.27 | `cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30)` |
| +0.84 | 0.035 | 8 | -1.43 / -2.27 | `day_sum(Amt)` |
| +0.84 | 0.018 | 10 | -1.45 / -2.29 | `day_centroid(High)` |
| +0.84 | 0.018 | 10 | -1.45 / -2.29 | `sub(LogTotalCap, day_centroid(High))` |
| +0.81 | 0.001 | 51 | -1.74 / -2.55 | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` |
| +0.79 | 0.085 | 5 | -1.46 / -2.25 | `ts_hurst(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)` |
| +0.79 | 0.085 | 5 | -1.46 / -2.25 | `cs_last_high40(day_centroid(Open), ts_hurst(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40))` |
| +0.79 | 0.018 | 14 | -1.52 / -2.31 | `day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` |
| +0.78 | 0.020 | 13 | -1.52 / -2.30 | `day_centroid(Open)` |
| +0.75 | 0.071 | 7 | -1.51 / -2.26 | `log(day_sum(Amt))` |
| +0.67 | 0.036 | 12 | -1.61 / -2.28 | `day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))` |
| +0.59 | 0.205 | 5 | -1.65 / -2.24 | `cross_mean(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 60)` |

## 拆解(13 次评估)

### head score -0.72:`ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 80)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` | -4.06 | -4.06 | -3.84 | — | (子树本身) |
| swap | `Volume->Amt` | -0.73 | -0.73 | -0.38 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), 80)` |
| window | `ts_stddev@80->40` | -1.37 | -1.37 | -1.34 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 40)` |
| window | `ts_stddev@80->160` | -0.29 | -0.29 | -0.04 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 160)` |

### head score -1.42:`day_sum(in_slice(Volume, 2, 237))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.41 | -2.76 | -3.41 | — | `day_sum(in_slice(Amt, 2, 237))` |

### head score -1.53:`day_sum(in_slice(Volume, 238, 240))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.93 | -3.53 | -3.93 | — | `day_sum(in_slice(Amt, 238, 240))` |

### head score -1.69:`ts_mean(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` | -2.17 | -1.75 | -2.17 | — | (子树本身) |
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` | -4.06 | -4.06 | -3.84 | — | (子树本身) |
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` | -2.49 | -1.96 | -2.49 | — | (子树本身) |
| knockout | `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` | -3.22 | -3.22 | -2.64 | +1.52 | `ts_mean(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 40)` |
| swap | `Volume->Amt` | -1.69 | -1.58 | -1.69 | — | `ts_mean(sub(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)` |
| window | `ts_mean@40->20` | -1.85 | -1.73 | -1.85 | — | `ts_mean(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 20)` |
| window | `ts_mean@40->80` | -2.46 | -2.06 | -2.46 | — | `ts_mean(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5))` — enrichment,均值差 +1.48,p 0.004
2. `day_median(Vwap)` — enrichment,均值差 +1.39,p 0.001
3. `cs_last_high10(sub(LogTotalCap, day_centroid(High)), day_median(Vwap))` — enrichment,均值差 +1.37,p 0.001
4. `sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` — enrichment,均值差 +1.03,p 0.040
5. `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` — enrichment,均值差 +1.00,p 0.000
6. `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` — enrichment,均值差 +0.99,p 0.000
7. `cross_ema(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 5)` — enrichment,均值差 +0.98,p 0.047
8. `sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` — enrichment,均值差 +0.93,p 0.019
9. `cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30)` — enrichment,均值差 +0.86,p 0.044
10. `day_sum(Amt)` — enrichment,均值差 +0.84,p 0.035
11. `day_centroid(High)` — enrichment,均值差 +0.84,p 0.018
12. `sub(LogTotalCap, day_centroid(High))` — enrichment,均值差 +0.84,p 0.018
13. `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` — enrichment,均值差 +0.81,p 0.001
14. `ts_hurst(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40)` — enrichment,均值差 +0.79,p 0.085
15. `cs_last_high40(day_centroid(Open), ts_hurst(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 40))` — enrichment,均值差 +0.79,p 0.085
16. `day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` — enrichment,均值差 +0.79,p 0.018
17. `day_centroid(Open)` — enrichment,均值差 +0.78,p 0.020
18. `log(day_sum(Amt))` — enrichment,均值差 +0.75,p 0.071
19. `day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))` — enrichment,均值差 +0.67,p 0.036
20. `day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` — enrichment,均值差 +0.47,p 0.085

## 本组之前各轮的任务

- `prods2025Pr1a_Ea`:核心 `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))`;评分 91,过线 0,入 heads 0;采样计数 {'c05_no_core': 1811, 'c05_skeleton': 863}
  - score -0.25(train -0.25 valid -0.11):`cross_max(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 3), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.31(train -0.23 valid -0.31):`cross_max(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.33(train -0.06 valid -0.33):`cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.40(train +0.07 valid -0.40):`cross_max(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_mean(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.45(train -0.45 valid -0.35):`cross_max(sub(sub(cross_max(sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 30), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
- `prods2025Pr1b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.43(train -0.43 valid +0.48):`cross_mean(sub(day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_skew(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))), 241)`
  - score -0.50(train +0.49 valid -0.50):`cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Ret, 11, 240))), 60)`
  - score -0.72(train +0.20 valid -0.72):`cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))), 60)`
  - score -0.72(train +0.20 valid -0.72):`cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))), 60)`
  - score -0.79(train +0.13 valid -0.79):`cross_ema(cross_ema(div(day_wmean(in_topk_masked(div(abs_(in_slice(Volume, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Vwap, 11, 240), 5), in_topk_masked(div(abs_(in_slice(Ret, 11, 240)), sqrt(in_slice(Volume, 11, 240))), in_slice(Volume, 11, 240), 5)), day_wmean(in_slice(Vwap, 11, 240), in_slice(Volume, 11, 240))), 60), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.43(window ts_stddev@80->160):`ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 160)`
