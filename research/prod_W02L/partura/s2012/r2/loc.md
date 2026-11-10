# 定位:种子 2012,P 组,第 2 轮(只含 train / valid)

快照:prods2012M1_I0_open_search, prods2012M2_I0_open_search, prods2012Pr1a_Ea, prods2012Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.69 | -1.69 | -0.80 | +1 | 5 | prods2012M2_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(Vwap), 40)` |
| -1.80 | -1.53 | -1.80 | +1 | 0 | prods2012M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(day_ar1_coefficient(Volume), 50), 50)` |
| -1.99 | -1.96 | -1.99 | +1 | 20 | prods2012M2_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(Volume), 50)` |
| -2.66 | -2.66 | -2.52 | +1 | 20 | prods2012M1_I0_open_search | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20)), 5)` |
| -3.01 | -2.83 | -3.01 | +1 | 20 | prods2012M1_I0_open_search | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)))` |
| -3.02 | -2.84 | -3.02 | +1 | 20 | prods2012M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)` |

## 共性:141 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.07 | 0.008 | 5 | -1.62 / -2.69 | `cs_winsor(day_es_ratio_hi(Open))` |
| +1.07 | 0.008 | 5 | -1.62 / -2.69 | `day_es_ratio_hi(Open)` |
| +0.98 | 0.000 | 15 | -1.78 / -2.76 | `inv(ListAge)` |
| +0.77 | 0.035 | 5 | -1.91 / -2.68 | `mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Close)))` |
| +0.66 | 0.051 | 6 | -2.03 / -2.68 | `cross_corr(day_ar1_coefficient(Volume), ts_delay(day_sum(Ret), 1), 40)` |
| +0.49 | 0.043 | 11 | -2.20 / -2.69 | `ts_delay(day_sum(Ret), 1)` |
| +0.37 | 0.095 | 11 | -2.31 / -2.68 | `cross_ema(day_ar1_coefficient(Volume), 5)` |
| +0.32 | 0.101 | 18 | -2.38 / -2.70 | `ts_quantile_q75(day_sum(Ret), 30)` |
| +0.25 | 0.266 | 15 | -2.43 / -2.68 | `cs_winsor(day_es_ratio_hi(Close))` |
| +0.12 | 0.138 | 41 | -2.57 / -2.69 | `day_sum(Ret)` |
| +0.11 | 0.334 | 77 | -2.60 / -2.72 | `day_ar1_coefficient(Volume)` |
| +0.10 | 0.424 | 22 | -2.57 / -2.67 | `day_es_ratio_hi(Close)` |
| -0.04 | 0.624 | 4 | -2.69 / -2.65 | `day_ar1_coefficient(High)` |
| -0.12 | 0.777 | 4 | -2.77 / -2.65 | `ts_delay(day_sum(Ret), 20)` |
| -0.14 | 0.824 | 10 | -2.78 / -2.65 | `ts_rank(cross_stddev(LogTotalCap, 15), 1)` |
| -0.29 | 0.924 | 12 | -2.92 / -2.63 | `cross_stddev(LogTotalCap, 15)` |
| -0.43 | 0.960 | 6 | -3.06 / -2.64 | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))` |
| -0.51 | 0.999 | 14 | -3.11 / -2.60 | `pow_05(day_ar1_coefficient(Volume))` |
| -0.51 | 0.999 | 14 | -3.11 / -2.60 | `pow_2(pow_05(day_ar1_coefficient(Volume)))` |
| -0.51 | 0.995 | 9 | -3.13 / -2.62 | `cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))` |

## 拆解(25 次评估)

### head score -1.69:`ts_quantile_q75(day_ar1_coefficient(Vwap), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Vwap)` | -3.09 | -2.76 | -3.09 | — | (子树本身) |
| swap | `Vwap->Close` | -2.57 | -2.22 | -2.57 | — | `ts_quantile_q75(day_ar1_coefficient(Close), 40)` |
| window | `ts_quantile_q75@40->20` | -1.99 | -1.99 | -0.98 | — | `ts_quantile_q75(day_ar1_coefficient(Vwap), 20)` |
| window | `ts_quantile_q75@40->80` | -1.82 | -1.82 | -0.47 | — | `ts_quantile_q75(day_ar1_coefficient(Vwap), 80)` |

### head score -1.80:`ts_quantile_q75(ts_quantile_q75(day_ar1_coefficient(Volume), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(day_ar1_coefficient(Volume), 50)` | -2.02 | -1.96 | -2.02 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| swap | `Volume->Amt` | -1.85 | -1.55 | -1.85 | — | `ts_quantile_q75(ts_quantile_q75(day_ar1_coefficient(Amt), 50), 50)` |
| window | `ts_quantile_q75@50->25` | -1.77 | -1.77 | -1.64 | — | `ts_quantile_q75(ts_quantile_q75(day_ar1_coefficient(Volume), 50), 25)` |
| window | `ts_quantile_q75@50->100` | -1.36 | -1.21 | -1.36 | — | `ts_quantile_q75(ts_quantile_q75(day_ar1_coefficient(Volume), 50), 100)` |

### head score -1.99:`ts_quantile_q75(day_ar1_coefficient(Volume), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| swap | `Volume->Amt` | -2.04 | -2.04 | -1.99 | — | `ts_quantile_q75(day_ar1_coefficient(Amt), 50)` |
| window | `ts_quantile_q75@50->25` | -2.57 | -2.57 | -2.28 | — | `ts_quantile_q75(day_ar1_coefficient(Volume), 25)` |
| window | `ts_quantile_q75@50->100` | -1.65 | -1.65 | -1.60 | — | `ts_quantile_q75(day_ar1_coefficient(Volume), 100)` |

### head score -2.66:`ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20))` | -2.75 | -2.75 | -2.56 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)` | -3.08 | -3.02 | -3.08 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20))` | -3.10 | -3.04 | -3.10 | +0.44 | `ts_decay_linear(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), 5)` |
| knockout | `ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)` | -2.48 | -2.48 | -2.07 | -0.18 | `ts_decay_linear(cs_bucket_demean(pow_2(pow_05(day_ar1_coefficient(Volume))), cross_mean(day_sum(Amt), 20)), 5)` |
| knockout | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -2.70 | -2.70 | -2.69 | +0.04 | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_05(day_ar1_coefficient(Volume)), 40), cross_mean(day_sum(Amt), 20)), 5)` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -2.45 | -2.45 | -2.16 | -0.21 | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(day_ar1_coefficient(Volume)), 40), cross_mean(day_sum(Amt), 20)), 5)` |
| swap | `Volume->Amt` | -2.68 | -2.68 | -2.55 | — | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Amt))), 40), cross_mean(day_sum(Amt), 20)), 5)` |
| swap | `Amt->Volume` | -3.54 | -2.54 | -3.54 | — | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Volume), 20)), 5)` |
| window | `ts_decay_linear@5->2` | -2.75 | -2.75 | -2.55 | — | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20)), 2)` |
| window | `ts_decay_linear@5->10` | -2.68 | -2.68 | -2.47 | — | `ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40), cross_mean(day_sum(Amt), 20)), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_winsor(day_es_ratio_hi(Open))` — enrichment,均值差 +1.07,p 0.008
2. `day_es_ratio_hi(Open)` — enrichment,均值差 +1.07,p 0.008
3. `inv(ListAge)` — enrichment,均值差 +0.98,p 0.000
4. `mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Close)))` — enrichment,均值差 +0.77,p 0.035
5. `cross_corr(day_ar1_coefficient(Volume), ts_delay(day_sum(Ret), 1), 40)` — enrichment,均值差 +0.66,p 0.051
6. `ts_delay(day_sum(Ret), 1)` — enrichment,均值差 +0.49,p 0.043
7. `cross_ema(day_ar1_coefficient(Volume), 5)` — enrichment,均值差 +0.37,p 0.095

## 本组之前各轮的任务

- `prods2012Pr1a_Ea`:核心 `day_ar1_coefficient(Volume)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 1062, 'c05_skeleton': 493}
  - score -1.36(train -1.29 valid -1.36):`cross_zscore(cross_ema(cross_ema(day_ar1_coefficient(Volume), 5), 5), 120)`
  - score -1.41(train -1.41 valid -0.97):`cross_corr(day_ar1_coefficient(Volume), ts_delay(day_sum(Ret), 1), 40)`
  - score -1.44(train -0.93 valid -1.44):`cross_regbeta(day_sum(Ret), day_ar1_coefficient(Volume), 60)`
  - score -1.51(train -1.51 valid -1.51):`cross_zscore(cross_ema(cross_corr(day_ar1_coefficient(Volume), ts_delay(day_sum(Ret), 1), 40), 5), 120)`
  - score -1.58(train -1.58 valid -0.19):`cross_corr(day_ar1_coefficient(Volume), abs_(day_sum(Ret)), 60)`
- `prods2012Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.97(train -0.85 valid -0.97):`mul(inv(ListAge), ts_quantile_q75(day_sum(Ret), 30))`
  - score -1.10(train -1.10 valid -0.72):`mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), cs_winsor(day_es_ratio_hi(Open)))`
  - score -1.10(train -1.10 valid -0.70):`mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), ts_rank(cross_stddev(LogTotalCap, 15), 1))`
  - score -1.11(train -1.11 valid -0.71):`mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), mul(mul(inv(ListAge), cs_winsor(day_es_ratio_hi(Open))), cs_winsor(day_es_ratio_hi(Open))))`
  - score -1.11(train -1.11 valid -0.70):`mul(mul(inv(ListAge), day_es_ratio_hi(Close)), day_es_ratio_hi(Close))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(knockout pow_05(day_ar1_coefficient(Volume))):`ts_decay_linear(cs_bucket_demean(ts_decay_linear(pow_2(day_ar1_coefficient(Volume)), 40), cross_mean(day_sum(Amt), 20)), 5)`
- 增益 +0.18(knockout ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)):`ts_decay_linear(cs_bucket_demean(pow_2(pow_05(day_ar1_coefficient(Volume))), cross_mean(day_sum(Amt), 20)), 5)`
