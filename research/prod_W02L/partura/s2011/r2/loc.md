# 定位:种子 2011,P 组,第 2 轮(只含 train / valid)

快照:prods2011M1_I0_open_search, prods2011M2_I0_open_search, prods2011Pr1a_Ea, prods2011Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.70 | -1.70 | -1.05 | +1 | 20 | prods2011M1_I0_open_search | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Amt), 30))` |
| -1.80 | -1.36 | -1.80 | +1 | 20 | prods2011M1_I0_open_search | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` |
| -2.00 | -1.95 | -2.00 | +1 | 20 | prods2011M2_I0_open_search | `ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 50)` |
| -2.11 | -1.98 | -2.11 | +1 | 5 | prods2011M1_I0_open_search | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)), 5)` |
| -2.43 | -2.43 | -2.30 | +1 | 20 | prods2011M2_I0_open_search | `pow_2(day_ar1_coefficient(Close))` |
| -2.66 | -2.60 | -2.66 | +1 | 20 | prods2011M2_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))), 5)` |

## 共性:108 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.16 | 0.000 | 62 | -2.31 / -3.47 | `day_ar1_coefficient(Volume)` |
| +1.08 | 0.000 | 21 | -1.93 / -3.02 | `day_sum(Ret)` |
| +0.96 | 0.016 | 5 | -1.89 / -2.85 | `log(day_sum(Ret))` |
| +0.96 | 0.016 | 5 | -1.89 / -2.85 | `cross_delta(log(day_sum(Ret)), 1)` |
| +0.87 | 0.038 | 5 | -1.97 / -2.85 | `day_sum(Amt)` |
| +0.79 | 0.005 | 10 | -2.09 / -2.88 | `cross_delay(day_ar1_coefficient(Volume), 1)` |
| +0.64 | 0.110 | 4 | -2.19 / -2.83 | `day_es_ratio_hi(Ret)` |
| +0.60 | 0.129 | 4 | -2.23 / -2.83 | `log(day_sum(Amt))` |
| +0.13 | 0.532 | 5 | -2.68 / -2.81 | `day_es_ratio_hi(Open)` |
| +0.06 | 0.555 | 4 | -2.75 / -2.81 | `pow_2(pow_2(day_ar1_coefficient(Volume)))` |
| +0.06 | 0.555 | 4 | -2.75 / -2.81 | `sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))` |
| +0.03 | 0.693 | 6 | -2.77 / -2.81 | `day_ar1_coefficient(in_logchg(Volume, 1))` |
| +0.03 | 0.790 | 13 | -2.78 / -2.81 | `pow_05(day_ar1_coefficient(Volume))` |
| -0.03 | 0.815 | 10 | -2.84 / -2.80 | `pow_2(day_ar1_coefficient(Volume))` |

## 拆解(30 次评估)

### head score -1.70:`cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Amt), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100)` | -1.65 | -1.65 | -1.61 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -3.76 | -2.87 | -3.76 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100)` | -3.18 | -3.09 | -3.18 | +1.48 | `cs_bucket_demean(pow_05(day_ar1_coefficient(Volume)), cross_mean(day_std(Amt), 30))` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -1.87 | -1.87 | -1.43 | +0.17 | `cs_bucket_demean(ts_quantile_q75(day_ar1_coefficient(Volume), 100), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_std(Amt), 30)` | -1.62 | -1.62 | -1.39 | -0.08 | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), day_std(Amt))` |
| swap | `Volume->Amt` | -1.69 | -1.69 | -1.17 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Amt)), 100), cross_mean(day_std(Amt), 30))` |
| swap | `Amt->Volume` | -2.01 | -2.01 | -1.81 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100), cross_mean(day_std(Volume), 30))` |
| window | `ts_quantile_q75@100->50` | -2.00 | -2.00 | -1.70 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50), cross_mean(day_std(Amt), 30))` |
| window | `ts_quantile_q75@100->200` | -1.08 | -1.08 | -0.13 | — | `cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Amt), 30))` |

### head score -2.00:`ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_ar1_coefficient(Volume))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `pow_2(day_ar1_coefficient(Volume))` | -2.02 | -1.96 | -2.02 | +0.02 | `ts_quantile_q75(day_ar1_coefficient(Volume), 50)` |
| swap | `Volume->Amt` | -2.04 | -2.04 | -2.01 | — | `ts_quantile_q75(pow_2(day_ar1_coefficient(Amt)), 50)` |
| window | `ts_quantile_q75@50->25` | -2.56 | -2.56 | -2.27 | — | `ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 25)` |
| window | `ts_quantile_q75@50->100` | -1.63 | -1.63 | -1.61 | — | `ts_quantile_q75(pow_2(day_ar1_coefficient(Volume)), 100)` |

### head score -2.43:`pow_2(day_ar1_coefficient(Close))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Close)` | -2.44 | -2.44 | -2.34 | — | (子树本身) |
| swap | `Close->Vwap` | -3.10 | -2.77 | -3.10 | — | `pow_2(day_ar1_coefficient(Vwap))` |

### head score -2.66:`ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5)))` | -2.63 | -2.45 | -2.63 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))` | -2.63 | -2.45 | -2.63 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5)` | -2.62 | -2.45 | -2.62 | — | (子树本身) |
| sufficiency | `pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume)))))` | -3.39 | -2.84 | -3.39 | — | (子树本身) |
| knockout | `sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5)))` | -2.63 | -2.61 | -2.63 | -0.03 | `ts_decay_linear(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5)), 5)` |
| knockout | `cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))` | -2.64 | -2.64 | -2.57 | -0.01 | `ts_decay_linear(sigmoid(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5)), 5)` |
| knockout | `ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5)` | -3.23 | -2.84 | -3.23 | +0.57 | `ts_decay_linear(sigmoid(cs_rank(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))))), 5)` |
| knockout | `pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume)))))` | -2.68 | -2.61 | -2.68 | +0.02 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume)))), 5))), 5)` |
| swap | `Volume->Amt` | -2.65 | -2.58 | -2.65 | — | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Amt))))), 5))), 5)` |
| window | `ts_decay_linear@5->2` | -2.62 | -2.50 | -2.62 | — | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))), 2)` |
| window | `ts_decay_linear@5->10` | -2.73 | -2.73 | -2.56 | — | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(sigmoid(pow_2(pow_2(day_ar1_coefficient(Volume))))), 5))), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_ar1_coefficient(Volume)` — enrichment,均值差 +1.16,p 0.000
2. `day_sum(Ret)` — enrichment,均值差 +1.08,p 0.000
3. `log(day_sum(Ret))` — enrichment,均值差 +0.96,p 0.016
4. `cross_delta(log(day_sum(Ret)), 1)` — enrichment,均值差 +0.96,p 0.016
5. `day_sum(Amt)` — enrichment,均值差 +0.87,p 0.038
6. `cross_delay(day_ar1_coefficient(Volume), 1)` — enrichment,均值差 +0.79,p 0.005

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.62(window ts_quantile_q75@100->200):`cs_bucket_demean(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 200), cross_mean(day_std(Amt), 30))`
