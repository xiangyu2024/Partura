# 定位:种子 2059,P 组,第 3 轮(只含 train / valid)

快照:prods2059M1_I0_open_search, prods2059M2_I0_open_search, prods2059M3_I0_open_search, prods2059Pr1a_Na, prods2059Pr1b_Nb, prods2059Pr2a_Ea, prods2059Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.63 | +0.63 | +0.78 | +1 | 5 | prods2059Pr2a_Ea | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))), 241)` |
| -1.45 | -1.24 | -1.45 | -1 | 20 | prods2059M2_I0_open_search | `cross_min(day_last(nt_cs_regres(Amt, Low)), 5)` |
| -1.48 | -1.46 | -1.48 | -1 | 20 | prods2059M2_I0_open_search | `cross_min(day_autocorr_n1(nt_cs_regres(Low, Low)), 5)` |
| -1.90 | -1.20 | -1.90 | +1 | 20 | prods2059M2_I0_open_search | `cross_min(day_first(nt_cs_regres(Amt, Low)), 15)` |
| -1.92 | -1.76 | -1.92 | -1 | 5 | prods2059M1_I0_open_search | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` |
| -1.95 | -1.95 | -1.92 | +1 | 20 | prods2059M3_I0_open_search | `pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5)))` |
| -2.28 | -1.32 | -2.28 | -1 | 5 | prods2059M1_I0_open_search | `cross_min(day_max(nt_cs_regres(Ret, Low)), 60)` |
| -2.39 | -2.28 | -2.39 | -1 | 20 | prods2059M1_I0_open_search | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15)` |
| -2.49 | -2.25 | -2.49 | +1 | 5 | prods2059M3_I0_open_search | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5))), 50)` |
| -2.88 | -2.88 | -1.96 | +1 | 5 | prods2059M3_I0_open_search | `ts_min(cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5)), 5)` |

## 共性:264 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.96 | 0.001 | 6 | -0.29 / -2.25 | `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))` |
| +1.77 | 0.000 | 32 | -0.65 / -2.42 | `ts_kurt(day_es_ratio_lo(Open), 10)` |
| +1.67 | 0.007 | 6 | -0.57 / -2.24 | `inv(day_q_stat_std(Open))` |
| +1.38 | 0.018 | 7 | -0.86 / -2.24 | `day_q_stat_std(Open)` |
| +1.12 | 0.004 | 15 | -1.15 / -2.27 | `inv(day_es_ratio_lo(Open))` |
| +0.95 | 0.009 | 9 | -1.28 / -2.23 | `day_wstd(Ret, Volume)` |
| +0.88 | 0.000 | 77 | -1.58 / -2.46 | `day_es_ratio_lo(Open)` |
| +0.83 | 0.016 | 6 | -1.39 / -2.22 | `ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40)` |
| +0.82 | 0.043 | 4 | -1.39 / -2.21 | `sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret))` |
| +0.79 | 0.164 | 4 | -1.43 / -2.21 | `day_wstd(Ret, Ret)` |
| +0.69 | 0.074 | 5 | -1.52 / -2.22 | `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(LogFloatCap))` |
| +0.64 | 0.074 | 6 | -1.57 / -2.22 | `inv(LogFloatCap)` |
| +0.63 | 0.027 | 9 | -1.60 / -2.22 | `day_wmean(Vwap, Volume)` |
| +0.63 | 0.027 | 9 | -1.60 / -2.22 | `pow_2_5(day_wmean(Vwap, Volume))` |
| +0.61 | 0.104 | 4 | -1.60 / -2.21 | `cross_mean(day_es_ratio_lo(Ret), 30)` |
| +0.59 | 0.223 | 4 | -1.62 / -2.21 | `inv(day_q_stat_std(Vwap))` |
| +0.47 | 0.081 | 15 | -1.76 / -2.23 | `day_topw_mean(Ret, Volume)` |
| +0.34 | 0.237 | 5 | -1.87 / -2.21 | `log(day_max(High))` |
| +0.33 | 0.225 | 5 | -1.88 / -2.21 | `day_flat_run_max(Low)` |
| +0.32 | 0.020 | 28 | -1.92 / -2.24 | `day_es_ratio_lo(Ret)` |

## 拆解(42 次评估)

### head score +0.63:`cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open))))` | -3.06 | -3.06 | -2.62 | — | (子树本身) |
| sufficiency | `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))` | -3.06 | -3.06 | -2.63 | — | (子树本身) |
| sufficiency | `ts_kurt(day_es_ratio_lo(Open), 10)` | -2.07 | -2.07 | -2.02 | — | (子树本身) |
| knockout | `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open))))` | +0.60 | +0.60 | +0.74 | +0.03 | `cross_max(ts_kurt(day_es_ratio_lo(Open), 10), 241)` |
| knockout | `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))` | +0.60 | +0.60 | +0.76 | +0.03 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), ts_kurt(day_es_ratio_lo(Open), 10)), 241)` |
| knockout | `ts_kurt(day_es_ratio_lo(Open), 10)` | -2.46 | -2.39 | -2.46 | +3.10 | `cross_max(cs_first_high20(day_es_ratio_lo(Open), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))), 241)` |
| knockout | `ts_kurt(day_es_ratio_lo(Open), 10)` | +0.58 | +0.58 | +0.71 | +0.05 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(day_es_ratio_lo(Open), inv(day_es_ratio_lo(Open)))), 241)` |
| swap | `Open->Close` | +0.43 | +0.43 | +0.90 | — | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Close), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Close), 10), inv(day_es_ratio_lo(Close)))), 241)` |
| window | `cross_max@241->120` | -0.06 | -0.06 | +0.49 | — | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))), 120)` |
| window | `cross_max@241->482` | +0.30 | +0.30 | +1.07 | — | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))), 482)` |

### head score -1.95:`pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5))` | -1.95 | -1.95 | -1.93 | — | (子树本身) |
| sufficiency | `ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5)` | -1.95 | -1.95 | -1.93 | — | (子树本身) |
| sufficiency | `ts_decay_linear(day_ar1_coefficient(Vwap), 5)` | -2.15 | -2.15 | -1.99 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Vwap)` | -3.09 | -2.76 | -3.09 | — | (子树本身) |
| knockout | `pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5))` | -1.94 | -1.94 | -1.94 | -0.00 | `pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5))` |
| knockout | `ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 5)` | -2.15 | -2.15 | -1.98 | +0.20 | `pow_2(pow_05(ts_decay_linear(day_ar1_coefficient(Vwap), 5)))` |
| knockout | `ts_decay_linear(day_ar1_coefficient(Vwap), 5)` | -2.02 | -2.02 | -1.66 | +0.08 | `pow_2(pow_05(ts_min(day_ar1_coefficient(Vwap), 5)))` |
| swap | `Vwap->Close` | -2.28 | -1.91 | -2.28 | — | `pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Close), 5), 5)))` |
| window | `ts_min@5->2` | -1.99 | -1.99 | -1.96 | — | `pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 2)))` |
| window | `ts_min@5->10` | -1.92 | -1.85 | -1.92 | — | `pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Vwap), 5), 10)))` |

### head score -2.49:`ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5)))` | -3.28 | -3.28 | -2.23 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5))` | -3.28 | -3.28 | -2.23 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5)` | -3.28 | -3.28 | -2.23 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5)))` | -3.42 | -3.03 | -3.42 | — | (子树本身) |
| knockout | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5)))` | -2.50 | -2.26 | -2.50 | +0.01 | `ts_quantile_q75(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5)), 50)` |
| knockout | `cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5))` | -2.58 | -2.22 | -2.58 | +0.08 | `ts_quantile_q75(pow_2(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5)), 50)` |
| knockout | `ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5)` | -2.46 | -2.33 | -2.46 | -0.03 | `ts_quantile_q75(pow_2(cs_rank(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))))), 50)` |
| knockout | `pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5)))` | -2.55 | -2.29 | -2.55 | +0.06 | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5)), 5))), 50)` |
| swap | `Volume->Amt` | -2.46 | -2.26 | -2.46 | — | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Amt), 5), 5))), 5))), 50)` |
| window | `ts_quantile_q75@50->25` | -2.96 | -2.96 | -2.88 | — | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5))), 25)` |
| window | `ts_quantile_q75@50->100` | -1.72 | -1.72 | -1.38 | — | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5))), 5))), 100)` |

### head score -2.88:`ts_min(cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5))` | -3.01 | -3.01 | -2.57 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5)` | -3.01 | -3.01 | -2.57 | — | (子树本身) |
| sufficiency | `pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5))` | -3.15 | -3.08 | -3.15 | — | (子树本身) |
| sufficiency | `ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)` | -3.13 | -3.04 | -3.13 | — | (子树本身) |
| knockout | `cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5))` | -2.72 | -2.72 | -2.18 | -0.16 | `ts_min(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5), 5)` |
| knockout | `ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5)` | -2.54 | -2.54 | -2.39 | -0.34 | `ts_min(cs_rank(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5))), 5)` |
| knockout | `pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5))` | -2.71 | -2.71 | -2.10 | -0.17 | `ts_min(cs_rank(ts_decay_linear(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5), 5)), 5)` |
| knockout | `ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)` | -3.16 | -3.03 | -3.16 | +0.28 | `ts_min(cs_rank(ts_decay_linear(pow_2(ts_decay_linear(day_ar1_coefficient(Volume), 1)), 5)), 5)` |
| swap | `Volume->Amt` | -2.76 | -2.76 | -1.93 | — | `ts_min(cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Amt), 1), 5)), 5)), 5)` |
| window | `ts_min@5->2` | -2.97 | -2.97 | -2.26 | — | `ts_min(cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5)), 2)` |
| window | `ts_min@5->10` | -2.75 | -2.75 | -2.27 | — | `ts_min(cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(day_ar1_coefficient(Volume), 1), 5)), 5)), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))` — enrichment,均值差 +1.96,p 0.001
2. `ts_kurt(day_es_ratio_lo(Open), 10)` — enrichment,均值差 +1.77,p 0.000
3. `inv(day_q_stat_std(Open))` — enrichment,均值差 +1.67,p 0.007
4. `day_q_stat_std(Open)` — enrichment,均值差 +1.38,p 0.018
5. `inv(day_es_ratio_lo(Open))` — enrichment,均值差 +1.12,p 0.004
6. `day_wstd(Ret, Volume)` — enrichment,均值差 +0.95,p 0.009
7. `day_es_ratio_lo(Open)` — enrichment,均值差 +0.88,p 0.000
8. `ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40)` — enrichment,均值差 +0.83,p 0.016
9. `sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret))` — enrichment,均值差 +0.82,p 0.043
10. `cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(LogFloatCap))` — enrichment,均值差 +0.69,p 0.074
11. `inv(LogFloatCap)` — enrichment,均值差 +0.64,p 0.074
12. `day_wmean(Vwap, Volume)` — enrichment,均值差 +0.63,p 0.027
13. `pow_2_5(day_wmean(Vwap, Volume))` — enrichment,均值差 +0.63,p 0.027
14. `day_topw_mean(Ret, Volume)` — enrichment,均值差 +0.47,p 0.081
15. `day_es_ratio_lo(Ret)` — enrichment,均值差 +0.32,p 0.020
16. `day_max(High)` — enrichment,均值差 +0.30,p 0.070
17. `day_es_ratio_hi(Ret)` — enrichment,均值差 +0.23,p 0.030
18. `day_mean(Ret)` — enrichment,均值差 +0.17,p 0.076

## 本组之前各轮的任务

- `prods2059Pr1a_Na`:核心 `—`;评分 81,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.43(train -0.08 valid -0.43):`cross_regbeta(day_max(Open), day_es_ratio_lo(Open), 60)`
  - score -0.44(train -0.04 valid -0.44):`cross_regbeta(day_max(High), day_es_ratio_lo(Open), 60)`
  - score -0.51(train -0.13 valid -0.51):`cross_regbeta(day_max(High), day_es_ratio_lo(High), 60)`
  - score -0.54(train -0.40 valid -0.54):`cross_regbeta(day_min(Low), day_es_ratio_lo(Open), 60)`
  - score -0.55(train -0.55 valid -0.46):`cross_regbeta(day_max(High), cross_regbeta(day_max(High), day_es_ratio_lo(Open), 60), 60)`
- `prods2059Pr1b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.23(train -1.23 valid -1.19):`cross_mean(cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret)), 15), LogFloatCap), 40)`
  - score -1.26(train -1.26 valid -1.20):`cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret)), 40), LogFloatCap)`
  - score -1.26(train -1.26 valid -1.00):`cs_bucket_zscore(cross_mean(sub(cross_mean(day_es_ratio_lo(Ret), 10), day_es_ratio_hi(Ret)), 40), LogFloatCap)`
  - score -1.27(train -1.27 valid -1.19):`cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Vwap)), 40), day_es_ratio_hi(Ret)), 40), LogFloatCap)`
  - score -1.28(train -1.19 valid -1.28):`cross_mean(cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret)), 40), LogFloatCap), 40)`
- `prods2059Pr2a_Ea`:核心 `day_es_ratio_lo(Open)`;评分 101,过线 10,入 heads 1;采样计数 {'c05_no_core': 1366, 'c05_skeleton': 665, 'c05_periphery_seen': 5}
  - score +0.63(train +0.63 valid +0.78):`cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open)))), 241)`
  - score +0.62(train +0.62 valid +1.07):`cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 30), inv(day_q_stat_std(Open))), 241)`
  - score +0.62(train +0.62 valid +0.73):`cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_es_ratio_lo(Open))), 241)`
  - score +0.61(train +0.61 valid +0.68):`cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), inv(day_q_stat_std(Open))), 241)`
  - score +0.60(train +0.60 valid +0.76):`cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10), ts_kurt(day_es_ratio_lo(Open), 10)), 241)`
- `prods2059Pr2b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.02(train -0.02 valid +0.42):`cross_regbeta(day_mean(Ret), day_wstd(Ret, Volume), 60)`
  - score -0.22(train -0.22 valid +0.38):`cross_regbeta(day_mean(Ret), day_wstd(Ret, Ret), 60)`
  - score -0.29(train -0.29 valid -0.00):`cross_regbeta(day_topw_mean(Ret, Volume), day_wstd(Ret, Ret), 60)`
  - score -0.39(train -0.39 valid +0.23):`cross_regbeta(day_topw_mean(Ret, Volume), day_wstd(Ret, Amt), 60)`
  - score -0.43(train -0.43 valid +0.24):`cross_regbeta(day_topw_mean(Ret, Volume), day_wstd(Ret, Volume), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
