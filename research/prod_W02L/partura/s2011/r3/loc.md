# 定位:种子 2011,P 组,第 3 轮(只含 train / valid)

快照:prods2011M1_I0_open_search, prods2011M2_I0_open_search, prods2011M3_I0_open_search, prods2011Pr1a_Ea, prods2011Pr1b_Nb, prods2011Pr2a_Ea, prods2011Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.08 | -1.08 | -0.13 | +1 | 20 | prods2011M1_I0_open_search | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Amt), 30))` |
| -1.38 | -1.38 | -0.83 | +1 | 20 | prods2011M2_I0_open_search | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Amt), 30))` |
| -1.77 | -1.69 | -1.77 | +1 | 0 | prods2011M2_I0_open_search | `cross_ema(day_ar1_coefficient(Close), 120)` |
| -1.80 | -1.36 | -1.80 | +1 | 20 | prods2011M1_I0_open_search | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` |
| -1.98 | -1.96 | -1.98 | +1 | 20 | prods2011M3_I0_open_search | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 50)` |
| -2.11 | -1.98 | -2.11 | +1 | 5 | prods2011M1_I0_open_search | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)), 5)` |
| -2.66 | -2.60 | -2.66 | +1 | 20 | prods2011M2_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))), 5)` |
| -2.87 | -2.87 | -2.67 | +1 | 5 | prods2011M3_I0_open_search | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_min(ts_decay_linear(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5), 5), 5))), 5)))` |
| -3.03 | -2.81 | -3.03 | +1 | 20 | prods2011M3_I0_open_search | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(ts_decay_linear(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5), 1))))), 5)` |

## 共性:232 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.52 | 0.009 | 5 | -0.92 / -2.44 | `cross_delay(cross_delay(day_sum(Ret), 1), 1)` |
| +1.38 | 0.014 | 4 | -1.05 / -2.43 | `day_sum(Volume)` |
| +1.16 | 0.038 | 4 | -1.26 / -2.43 | `cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1)` |
| +1.14 | 0.001 | 15 | -1.34 / -2.48 | `day_centroid(Amt)` |
| +0.99 | 0.001 | 18 | -1.49 / -2.48 | `cross_delay(day_sum(Ret), 1)` |
| +0.98 | 0.001 | 13 | -1.48 / -2.46 | `cross_autocorr_s1(day_ar1_coefficient(in_logchg(Volume, 1)), 120)` |
| +0.88 | 0.034 | 7 | -1.56 / -2.43 | `cross_zscore(log(day_sum(Amt)), 60)` |
| +0.87 | 0.000 | 66 | -1.79 / -2.65 | `day_sum(Ret)` |
| +0.81 | 0.002 | 20 | -1.67 / -2.48 | `day_sum(Amt)` |
| +0.70 | 0.020 | 14 | -1.75 / -2.45 | `log(day_sum(Amt))` |
| +0.64 | 0.000 | 72 | -1.96 / -2.61 | `day_ar1_coefficient(in_logchg(Volume, 1))` |
| +0.61 | 0.171 | 4 | -1.81 / -2.42 | `cross_mean(day_median(Amt), 30)` |
| +0.57 | 0.142 | 5 | -1.85 / -2.42 | `cross_delta(log(day_sum(Amt)), 1)` |
| +0.57 | 0.153 | 5 | -1.85 / -2.42 | `day_median(Amt)` |
| +0.53 | 0.147 | 5 | -1.89 / -2.42 | `log(day_sum(Ret))` |
| +0.53 | 0.147 | 5 | -1.89 / -2.42 | `cross_delta(log(day_sum(Ret)), 1)` |
| +0.34 | 0.186 | 10 | -2.09 / -2.42 | `cross_delay(day_ar1_coefficient(Volume), 1)` |
| +0.22 | 0.406 | 4 | -2.19 / -2.41 | `day_es_ratio_hi(Ret)` |
| -0.07 | 0.980 | 78 | -2.46 / -2.38 | `day_ar1_coefficient(Volume)` |
| -0.28 | 0.853 | 5 | -2.68 / -2.40 | `day_es_ratio_hi(Open)` |

## 拆解(36 次评估)

### head score -1.08:`cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Amt), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200)` | -1.25 | -1.25 | -0.52 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -3.76 | -2.87 | -3.76 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200)` | -3.18 | -3.09 | -3.18 | +2.10 | `cs_bucket_demean(pow_05(day_ar1_coefficient(Volume)), cross_mean(day_std(Amt), 30))` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -1.22 | -1.22 | -0.40 | +0.14 | `cs_bucket_demean(ts_quantile_q75(day_ar1_coefficient(Volume), 200), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_std(Amt), 30)` | -1.18 | -1.18 | -0.05 | +0.10 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200), day_std(Amt))` |
| swap | `Volume->Amt` | -1.08 | -1.08 | -0.14 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Amt)), 200), cross_mean(day_std(Amt), 30))` |
| swap | `Amt->Volume` | -1.41 | -1.41 | -0.75 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Volume), 30))` |
| window | `ts_quantile_q75@200->100` | -1.70 | -1.70 | -1.05 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Amt), 30))` |
| window | `ts_quantile_q75@200->400` | -1.10 | -1.10 | -0.02 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 400), cross_mean(day_std(Amt), 30))` |

### head score -1.38:`cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Amt), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 200)` | -1.26 | -1.26 | -0.54 | — | (子树本身) |
| sufficiency | `pow_2(day_ar1_coefficient(Volume))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -3.76 | -2.87 | -3.76 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 200)` | -3.27 | -3.27 | -3.25 | +1.89 | `cs_bucket_demean(pow_2(day_ar1_coefficient(Volume)), cross_mean(day_std(Amt), 30))` |
| knockout | `pow_2(day_ar1_coefficient(Volume))` | -1.22 | -1.22 | -0.40 | -0.16 | `cs_bucket_demean(ts_quantile_q75(day_ar1_coefficient(Volume), 200), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_std(Amt), 30)` | -1.74 | -1.74 | -0.82 | +0.36 | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 200), day_std(Amt))` |
| swap | `Volume->Amt` | -1.39 | -1.39 | -0.92 | — | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Amt)), 200), cross_mean(day_std(Amt), 30))` |
| swap | `Amt->Volume` | -1.72 | -1.72 | -0.98 | — | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Volume), 30))` |
| window | `ts_quantile_q75@200->100` | -1.99 | -1.99 | -1.81 | — | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Amt), 30))` |
| window | `ts_quantile_q75@200->400` | -1.59 | -1.59 | -0.62 | — | `cs_bucket_demean(ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 400), cross_mean(day_std(Amt), 30))` |

### head score -1.77:`cross_ema(day_ar1_coefficient(Close), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Close)` | -2.44 | -2.44 | -2.34 | — | (子树本身) |
| swap | `Close->Vwap` | -2.03 | -2.03 | -1.44 | — | `cross_ema(day_ar1_coefficient(Vwap), 120)` |
| window | `cross_ema@120->60` | -1.88 | -1.88 | -1.68 | — | `cross_ema(day_ar1_coefficient(Close), 60)` |
| window | `cross_ema@120->240` | -1.62 | -1.62 | -1.61 | — | `cross_ema(day_ar1_coefficient(Close), 240)` |

### head score -1.98:`ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -2.02 | -1.96 | -2.02 | +0.04 | `ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Volume))), 50)` |
| knockout | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -2.00 | -1.96 | -2.00 | +0.02 | `ts_quantile_q75(sigmoid(pow_05(day_ar1_coefficient(Volume))), 50)` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -2.03 | -1.95 | -2.03 | +0.04 | `ts_quantile_q75(sigmoid(pow_2(day_ar1_coefficient(Volume))), 50)` |
| swap | `Volume->Amt` | -2.38 | -2.04 | -2.38 | — | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Amt)))), 50)` |
| window | `ts_quantile_q75@50->25` | -2.57 | -2.57 | -2.27 | — | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 25)` |
| window | `ts_quantile_q75@50->100` | -1.66 | -1.66 | -1.60 | — | `ts_quantile_q75(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_delay(cross_delay(day_sum(Ret), 1), 1)` — enrichment,均值差 +1.52,p 0.009
2. `day_sum(Volume)` — enrichment,均值差 +1.38,p 0.014
3. `cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1)` — enrichment,均值差 +1.16,p 0.038
4. `day_centroid(Amt)` — enrichment,均值差 +1.14,p 0.001
5. `cross_delay(day_sum(Ret), 1)` — enrichment,均值差 +0.99,p 0.001
6. `cross_autocorr_s1(day_ar1_coefficient(in_logchg(Volume, 1)), 120)` — enrichment,均值差 +0.98,p 0.001
7. `cross_zscore(log(day_sum(Amt)), 60)` — enrichment,均值差 +0.88,p 0.034
8. `day_sum(Ret)` — enrichment,均值差 +0.87,p 0.000
9. `day_sum(Amt)` — enrichment,均值差 +0.81,p 0.002
10. `log(day_sum(Amt))` — enrichment,均值差 +0.70,p 0.020
11. `day_ar1_coefficient(in_logchg(Volume, 1))` — enrichment,均值差 +0.64,p 0.000

## 本组之前各轮的任务

- `prods2011Pr1a_Ea`:核心 `day_ar1_coefficient(Volume)`;评分 68,过线 0,入 heads 0;采样计数 {'c05_no_core': 1456, 'c05_skeleton': 720}
  - score -0.72(train -0.59 valid -0.72):`cross_corr(cross_delay(day_ar1_coefficient(Volume), 1), day_sum(Ret), 120)`
  - score -0.85(train -0.85 valid -0.77):`cross_corr(day_ar1_coefficient(Volume), cross_delay(day_sum(Ret), 1), 60)`
  - score -0.95(train +0.03 valid -0.95):`cross_corr(day_ar1_coefficient(Volume), cross_delta(day_sum(Amt), 1), 60)`
  - score -1.00(train -1.00 valid -0.80):`cross_corr(cross_fangzheng(day_ar1_coefficient(Volume), 3), day_sum(Ret), 120)`
  - score -1.19(train -1.19 valid -0.97):`cross_corr(cross_delay(day_ar1_coefficient(Volume), 3), day_sum(Ret), 120)`
- `prods2011Pr1b_Nb`:核心 `—`;评分 53,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -1.79(train -1.79 valid -1.08):`sub(cross_mean(day_ar1_coefficient(in_logchg(Volume, 1)), 20), cross_mean(day_ar1_coefficient(in_logchg(Volume, 1)), 120))`
  - score -2.19(train -2.19 valid -1.87):`log(signedpower(day_es_ratio_hi(Ret)))`
  - score -2.19(train -2.19 valid -1.87):`inv(signedpower(day_es_ratio_hi(Ret)))`
  - score -2.19(train -2.19 valid -1.87):`pow_2(day_es_ratio_hi(Ret))`
  - score -2.19(train -2.19 valid -1.87):`abs_(signedpower(day_es_ratio_hi(Ret)))`
- `prods2011Pr2a_Ea`:核心 `day_ar1_coefficient(in_logchg(Volume, 1))`;评分 85,过线 0,入 heads 0;采样计数 {'c05_no_core': 761, 'c05_skeleton': 360, 'c05_periphery_seen': 7, 'mutation_refused': 4}
  - score +0.19(train +0.19 valid +0.71):`cross_regalpha(day_ar1_coefficient(in_logchg(Volume, 1)), cross_delay(day_sum(Ret), 1), 241)`
  - score -0.15(train -0.15 valid +0.30):`cross_cov(day_ar1_coefficient(in_logchg(Volume, 1)), cross_delay(day_ar1_coefficient(in_logchg(Volume, 1)), 1), 241)`
  - score -0.16(train -0.16 valid +0.18):`cross_corr(day_ar1_coefficient(in_logchg(Volume, 1)), cross_delay(day_ar1_coefficient(in_logchg(Volume, 1)), 1), 241)`
  - score -0.22(train -0.22 valid +0.68):`cross_corr(day_ar1_coefficient(in_logchg(Volume, 1)), day_sum(Volume), 241)`
  - score -0.26(train -0.26 valid +0.74):`cross_corr(day_ar1_coefficient(in_logchg(Volume, 1)), cross_delay(day_sum(Volume), 1), 241)`
- `prods2011Pr2b_Nb`:核心 `—`;评分 67,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score +0.32(train +0.32 valid +0.44):`cross_regalpha(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241)`
  - score +0.27(train +0.32 valid +0.27):`cross_corr(day_centroid(Amt), cross_delay(day_sum(Ret), 1), 241)`
  - score +0.19(train +0.58 valid +0.19):`cross_corr(day_centroid(Amt), cross_delay(cross_delay(day_sum(Ret), 1), 1), 241)`
  - score -0.32(train -0.32 valid +0.60):`cross_corr(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 241)`
  - score -0.52(train -0.52 valid +0.13):`cs_bucket_rank(cross_corr(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 241), cross_mean(day_std(Amt), 30))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.16(knockout pow_2(day_ar1_coefficient(Volume))):`cs_bucket_demean(ts_quantile_q75(day_ar1_coefficient(Volume), 200), cross_mean(day_std(Amt), 30))`
- 增益 +0.15(window cross_ema@120->240):`cross_ema(day_ar1_coefficient(Close), 240)`
