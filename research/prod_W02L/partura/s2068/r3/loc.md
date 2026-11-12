# 定位:种子 2068,P 组,第 3 轮(只含 train / valid)

快照:prods2068M1_I0_open_search, prods2068M2_I0_open_search, prods2068M3_I0_open_search, prods2068Pr1a_Ea, prods2068Pr1b_Nb, prods2068Pr2a_Ea, prods2068Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.61 | -1.31 | -1.61 | -1 | 5 | prods2068M1_I0_open_search | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| -1.82 | -1.63 | -1.82 | +1 | 20 | prods2068M3_I0_open_search | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 10))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |
| -2.16 | -1.88 | -2.16 | -1 | 20 | prods2068M1_I0_open_search | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| -2.40 | -2.40 | -1.85 | -1 | 20 | prods2068M3_I0_open_search | `select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |
| -2.66 | -1.75 | -2.66 | +1 | 5 | prods2068M2_I0_open_search | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open, 3), Volume, 60), 241))` |
| -2.86 | -2.64 | -2.86 | -1 | 20 | prods2068M1_I0_open_search | `day_sum(abs_(in_slice(Ret, 1, 30)))` |
| -3.23 | -3.23 | -2.61 | -1 | 20 | prods2068M3_I0_open_search | `mul(sign(ts_delta(day_sum(Volume), 1)), mul(-1, ts_delta(day_last(Close), 1)))` |
| -3.54 | -3.54 | -3.13 | +1 | 20 | prods2068M2_I0_open_search | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Volume, 21)), 5))` |
| -3.59 | -3.59 | -3.14 | +1 | 20 | prods2068M2_I0_open_search | `day_corr(abs_(Ret), in_delay(log(in_zscore_rolling(Amt, 21)), 5))` |

## 共性:214 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.47 | 0.008 | 4 | -1.55 / -3.03 | `pow_3(day_max(Low))` |
| +1.37 | 0.000 | 17 | -1.74 / -3.11 | `ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10)` |
| +1.31 | 0.011 | 5 | -1.72 / -3.03 | `pow_3(day_max(Open))` |
| +1.31 | 0.011 | 5 | -1.72 / -3.03 | `day_max(Open)` |
| +1.28 | 0.015 | 5 | -1.75 / -3.03 | `day_max(Low)` |
| +1.20 | 0.004 | 8 | -1.85 / -3.04 | `sub(day_topw_mean(Ret, Amt), day_mean(Ret))` |
| +1.17 | 0.027 | 5 | -1.86 / -3.02 | `sub(day_last(Close), day_open(Open))` |
| +1.10 | 0.005 | 12 | -1.96 / -3.06 | `day_median(cross_ema(Vwap, 15))` |
| +1.09 | 0.000 | 24 | -2.03 / -3.12 | `day_sum(abs_(in_slice(Ret, 211, 240)))` |
| +1.05 | 0.049 | 5 | -1.97 / -3.02 | `ts_sum(sub(div(day_last(Close), day_open(Open)), 1), 40)` |
| +0.98 | 0.003 | 18 | -2.10 / -3.08 | `cross_ema(day_median(Ret), 30)` |
| +0.96 | 0.001 | 29 | -2.17 / -3.13 | `day_median(Ret)` |
| +0.91 | 0.038 | 9 | -2.13 / -3.04 | `cross_fangzheng(cross_ema(day_median(Ret), 30), 30)` |
| +0.82 | 0.142 | 4 | -2.19 / -3.01 | `day_topw_mean(Ret, Volume)` |
| +0.80 | 0.026 | 14 | -2.25 / -3.05 | `day_mean(Ret)` |
| +0.79 | 0.018 | 16 | -2.26 / -3.06 | `day_topw_mean(Ret, Amt)` |
| +0.75 | 0.053 | 12 | -2.29 / -3.04 | `sigmoid(LimitWidth)` |
| +0.52 | 0.000 | 53 | -2.61 / -3.13 | `day_sum(abs_(in_slice(Ret, 1, 30)))` |
| +0.50 | 0.377 | 4 | -2.51 / -3.01 | `cross_fangzheng(cross_fangzheng(cross_ema(day_median(Ret), 30), 30), 30)` |
| +0.47 | 0.129 | 7 | -2.54 / -3.01 | `div(day_last(Close), day_open(Open))` |

## 拆解(33 次评估)

### head score -1.82:`mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 10))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5))` | -2.84 | -2.84 | -1.70 | — | (子树本身) |
| sufficiency | `cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))` | -6.02 | -5.60 | -6.02 | — | (子树本身) |
| sufficiency | `ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_rank(ts_rank(day_last(Close), 10))` | -3.74 | -3.24 | -3.74 | — | (子树本身) |
| knockout | `mul(mul(-1, cs_rank(ts_rank(day_last(Close), 10))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1)))` | -2.11 | -2.11 | -1.58 | +0.29 | `mul(cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1)), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |
| knockout | `cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5))` | -3.04 | -2.92 | -3.04 | +1.22 | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 10))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5))` |
| knockout | `mul(-1, cs_rank(ts_rank(day_last(Close), 10)))` | -1.77 | -1.63 | -1.77 | -0.05 | `mul(mul(cs_rank(ts_rank(day_last(Close), 10)), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |
| knockout | `cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))` | -6.12 | -5.77 | -6.12 | +4.30 | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 10))), ts_delta(ts_delta(day_last(Close), 1), 1)), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |
| swap | `Close->Vwap` | -1.79 | -1.65 | -1.79 | — | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Vwap), 10))), cs_rank(ts_delta(ts_delta(day_last(Vwap), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |
| swap | `Volume->Amt` | -1.73 | -1.65 | -1.73 | — | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 10))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Amt), ts_mean(day_sum(Amt), 20)), 5)))` |
| window | `ts_rank@10->5` | -1.23 | -1.23 | -1.20 | — | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 5))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |
| window | `ts_rank@10->20` | -2.75 | -2.65 | -2.75 | — | `mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 20))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))` |

### head score -2.40:`select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)` | — | — | — | — | 门槛废品 |
| sufficiency | `div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100))` | -1.61 | -1.61 | -1.49 | — | (子树本身) |
| sufficiency | `ts_delta(div(ts_sum(day_last(Close), 100), 100), 100)` | -1.82 | -1.68 | -1.82 | — | (子树本身) |
| knockout | `logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05))` | -2.40 | -2.40 | -1.85 | +0.00 | `select_where(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |
| knockout | `is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)` | -2.63 | -2.21 | -2.63 | +0.23 | `select_where(logical_or(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |
| knockout | `eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)` | -2.63 | -2.21 | -2.63 | +0.23 | `select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05), div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100))), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |
| knockout | `div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100))` | -2.13 | -2.13 | -2.01 | -0.27 | `select_where(logical_or(is_lt(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |
| swap | `Close->Vwap` | -2.39 | -2.39 | -1.79 | — | `select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Vwap), 100), 100), 100), ts_delay(day_last(Vwap), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Vwap), 100), 100), 100), ts_delay(day_last(Vwap), 100)), 0.05)), mul(-1, sub(day_last(Vwap), ts_min(day_last(Vwap), 100))), mul(-1, ts_delta(day_last(Vwap), 3)))` |
| window | `ts_delta@100->50` | -2.65 | -2.61 | -2.65 | — | `select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 50), ts_delay(day_last(Close), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |
| window | `ts_delta@100->200` | -2.28 | -1.85 | -2.28 | — | `select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 200), ts_delay(day_last(Close), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))` |

### head score -3.23:`mul(sign(ts_delta(day_sum(Volume), 1)), mul(-1, ts_delta(day_last(Close), 1)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_delta(day_sum(Volume), 1)` | -5.57 | -5.44 | -5.57 | — | (子树本身) |
| sufficiency | `ts_delta(day_last(Close), 1)` | -4.72 | -4.27 | -4.72 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_last(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `sign(ts_delta(day_sum(Volume), 1))` | -3.01 | -2.77 | -3.01 | -0.22 | `mul(ts_delta(day_sum(Volume), 1), mul(-1, ts_delta(day_last(Close), 1)))` |
| knockout | `mul(-1, ts_delta(day_last(Close), 1))` | -3.23 | -3.23 | -2.65 | +0.00 | `mul(sign(ts_delta(day_sum(Volume), 1)), ts_delta(day_last(Close), 1))` |
| knockout | `ts_delta(day_sum(Volume), 1)` | -4.72 | -4.27 | -4.72 | +1.49 | `mul(sign(day_sum(Volume)), mul(-1, ts_delta(day_last(Close), 1)))` |
| knockout | `ts_delta(day_last(Close), 1)` | -5.22 | -5.13 | -5.22 | +1.99 | `mul(sign(ts_delta(day_sum(Volume), 1)), mul(-1, day_last(Close)))` |
| swap | `Volume->Amt` | -3.40 | -3.40 | -2.74 | — | `mul(sign(ts_delta(day_sum(Amt), 1)), mul(-1, ts_delta(day_last(Close), 1)))` |
| swap | `Close->Vwap` | -3.29 | -3.29 | -2.75 | — | `mul(sign(ts_delta(day_sum(Volume), 1)), mul(-1, ts_delta(day_last(Vwap), 1)))` |
| window | `ts_delta@1->2` | -3.38 | -3.38 | -2.76 | — | `mul(sign(ts_delta(day_sum(Volume), 2)), mul(-1, ts_delta(day_last(Close), 1)))` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_3(day_max(Low))` — enrichment,均值差 +1.47,p 0.008
2. `ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10)` — enrichment,均值差 +1.37,p 0.000
3. `pow_3(day_max(Open))` — enrichment,均值差 +1.31,p 0.011
4. `day_max(Open)` — enrichment,均值差 +1.31,p 0.011
5. `day_max(Low)` — enrichment,均值差 +1.28,p 0.015
6. `sub(day_topw_mean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +1.20,p 0.004
7. `sub(day_last(Close), day_open(Open))` — enrichment,均值差 +1.17,p 0.027
8. `day_median(cross_ema(Vwap, 15))` — enrichment,均值差 +1.10,p 0.005
9. `day_sum(abs_(in_slice(Ret, 211, 240)))` — enrichment,均值差 +1.09,p 0.000
10. `ts_sum(sub(div(day_last(Close), day_open(Open)), 1), 40)` — enrichment,均值差 +1.05,p 0.049
11. `cross_ema(day_median(Ret), 30)` — enrichment,均值差 +0.98,p 0.003
12. `day_median(Ret)` — enrichment,均值差 +0.96,p 0.001
13. `cross_fangzheng(cross_ema(day_median(Ret), 30), 30)` — enrichment,均值差 +0.91,p 0.038
14. `day_mean(Ret)` — enrichment,均值差 +0.80,p 0.026
15. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.79,p 0.018
16. `sigmoid(LimitWidth)` — enrichment,均值差 +0.75,p 0.053
17. `day_sum(abs_(in_slice(Ret, 1, 30)))` — enrichment,均值差 +0.52,p 0.000

## 本组之前各轮的任务

- `prods2068Pr1a_Ea`:核心 `day_sum(abs_(in_slice(Ret, 1, 30)))`;评分 92,过线 0,入 heads 0;采样计数 {'c05_no_core': 1557, 'c05_skeleton': 896}
  - score -0.86(train -0.86 valid -0.41):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_median(cross_ema(Vwap, 10)), 30)`
  - score -0.93(train -0.93 valid -0.75):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_median(cross_ema(Vwap, 15)), 30)`
  - score -1.02(train -1.02 valid -0.63):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_quantile_q75(cross_ema(Vwap, 15)), 30)`
  - score -1.12(train -1.12 valid -0.65):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(in_slice(Ret, 211, 240))), 10), day_median(Ret), 30)`
  - score -1.12(train -1.12 valid -0.65):`cross_reg_tvalue(ts_corr(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(abs_(abs_(in_slice(Ret, 211, 240)))), 10), day_median(Ret), 30)`
- `prods2068Pr1b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.79(train -0.79 valid -0.78):`cs_bucket_demean(day_last(Close), cross_delay(day_last(Close), 1))`
  - score -0.99(train -0.85 valid -0.99):`cs_bucket_demean(cross_delay(day_last(Close), 1), day_open(Open))`
  - score -1.13(train -0.68 valid -1.13):`cs_bucket_demean(pow_3(ts_sum(sub(sub(day_last(Close), day_open(Open)), 1), 40)), sigmoid(LimitWidth))`
  - score -1.13(train -0.66 valid -1.13):`cs_bucket_demean(pow_3(ts_sum(sub(sub(day_last(Close), day_open(Close)), 1), 40)), sigmoid(LimitWidth))`
  - score -1.21(train -1.21 valid -1.19):`cs_bucket_demean(pow_3(day_max(Low)), day_open(Open))`
- `prods2068Pr2a_Ea`:核心 `day_median(Ret)`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1070, 'c05_no_core': 2353}
  - score -1.68(train -1.54 valid -1.68):`pow_3(cross_fangzheng(cross_fangzheng(cross_ema(day_median(Ret), 30), 30), 30))`
  - score -1.73(train -1.73 valid -1.61):`cross_fangzheng(cross_ema(cross_ema(cross_fangzheng(cross_ema(day_median(Ret), 30), 30), 5), 30), 30)`
  - score -1.75(train -1.60 valid -1.75):`pow_3(cross_ema(cross_fangzheng(cross_ema(day_median(Ret), 30), 30), 30))`
  - score -1.75(train -1.75 valid -1.62):`cross_fangzheng(cross_ema(cross_fangzheng(cross_ema(day_median(Ret), 30), 30), 30), 30)`
  - score -1.85(train -1.59 valid -1.85):`cross_fangzheng(cross_argmin(cross_fangzheng(cross_ema(day_median(Ret), 30), 30), 30), 30)`
- `prods2068Pr2b_Nb`:核心 `—`;评分 76,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -1.45(train -1.45 valid -1.22):`ts_decay_linear(ts_decay_linear(ts_decay_linear(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 20), 20), 30)`
  - score -1.47(train -1.41 valid -1.47):`ts_mean(ts_mean(day_topw_mean(Ret, Volume), 20), 30)`
  - score -1.51(train -1.51 valid -1.38):`ts_mean(day_topw_mean(Ret, Volume), 30)`
  - score -1.54(train -1.54 valid -1.48):`ts_mean(day_topw_mean(Ret, Amt), 30)`
  - score -1.55(train -1.34 valid -1.55):`ts_mean(div(day_topw_mean(Ret, Amt), day_mean(Ret)), 30)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.58(window ts_rank@10->5):`mul(mul(mul(-1, cs_rank(ts_rank(day_last(Close), 5))), cs_rank(ts_delta(ts_delta(day_last(Close), 1), 1))), cs_rank(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 5)))`
- 增益 +0.27(knockout div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100))):`select_where(logical_or(is_lt(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))`
- 增益 +0.22(knockout sign(ts_delta(day_sum(Volume), 1))):`mul(ts_delta(day_sum(Volume), 1), mul(-1, ts_delta(day_last(Close), 1)))`
- 增益 +0.12(window ts_delta@100->200):`select_where(logical_or(is_lt(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 200), ts_delay(day_last(Close), 100)), 0.05), eq(div(ts_delta(div(ts_sum(day_last(Close), 100), 100), 100), ts_delay(day_last(Close), 100)), 0.05)), mul(-1, sub(day_last(Close), ts_min(day_last(Close), 100))), mul(-1, ts_delta(day_last(Close), 3)))`
