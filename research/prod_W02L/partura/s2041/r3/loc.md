# 定位:种子 2041,P 组,第 3 轮(只含 train / valid)

快照:prods2041M1_I0_open_search, prods2041M2_I0_open_search, prods2041M3_I0_open_search, prods2041Pr1a_Ea, prods2041Pr1b_Nb, prods2041Pr2a_Ea;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.51 | -1.38 | -1.51 | -1 | 20 | prods2041M1_I0_open_search | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), Volume, create_like(in_slice(Close, 1, 1), 0)))` |
| -1.73 | -1.72 | -1.73 | -1 | 20 | prods2041M1_I0_open_search | `mul(day_sum(select_where(eq(in_roll_labels(Close, 120), 4), Volume, create_like(in_slice(Close, 1, 1), 0))), day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 3), create_like(in_slice(Close, 1, 1), 0))))` |
| -1.80 | -1.44 | -1.80 | -1 | 20 | prods2041M1_I0_open_search | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))` |
| -1.80 | -1.77 | -1.80 | -1 | 5 | prods2041M2_I0_open_search | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60))), 30)` |
| -1.81 | -1.81 | -1.75 | -1 | 5 | prods2041M2_I0_open_search | `cross_stddev(div(day_last(in_slice(Close, 1, 210)), day_first(in_slice(Open, 1, 210))), 20)` |
| -1.90 | -1.78 | -1.90 | -1 | 5 | prods2041M2_I0_open_search | `cross_stddev(div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120))), 20)` |

## 共性:182 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.83 | 0.000 | 6 | -0.73 / -2.56 | `day_first(Open)` |
| +1.73 | 0.001 | 5 | -0.82 / -2.55 | `day_close(Vwap)` |
| +1.47 | 0.005 | 4 | -1.07 / -2.53 | `add(day_centroid(Ret), add(day_gini(High), ListAge))` |
| +1.38 | 0.011 | 4 | -1.16 / -2.53 | `day_gini(Open)` |
| +1.31 | 0.000 | 16 | -1.30 / -2.62 | `day_max(Low)` |
| +1.30 | 0.000 | 15 | -1.31 / -2.61 | `cs_demean(day_max(Low))` |
| +1.28 | 0.000 | 11 | -1.30 / -2.58 | `cs_last_high05(cross_product(day_corr(Ret, Close), 15), cs_demean(day_max(Low)))` |
| +1.24 | 0.000 | 25 | -1.43 / -2.67 | `cross_product(day_corr(Ret, Close), 15)` |
| +1.23 | 0.000 | 27 | -1.45 / -2.68 | `day_corr(Ret, Close)` |
| +1.17 | 0.001 | 12 | -1.41 / -2.58 | `add(day_gini(High), ListAge)` |
| +1.15 | 0.006 | 7 | -1.39 / -2.55 | `div(day_gini(High), cs_last_high05(cross_product(day_corr(Ret, Close), 15), cs_demean(day_max(Low))))` |
| +1.02 | 0.005 | 9 | -1.53 / -2.55 | `day_corr(in_delta(Vwap, 5), Volume)` |
| +0.99 | 0.023 | 7 | -1.55 / -2.54 | `day_last(Close)` |
| +0.98 | 0.064 | 4 | -1.54 / -2.52 | `day_gini(Low)` |
| +0.90 | 0.040 | 5 | -1.62 / -2.53 | `ts_skew(day_corr(in_delta(Vwap, 5), Volume), 20)` |
| +0.90 | 0.000 | 85 | -2.02 / -2.92 | `day_gini(High)` |
| +0.77 | 0.105 | 4 | -1.75 / -2.52 | `mul(day_gini(High), ListAge)` |
| +0.71 | 0.054 | 9 | -1.82 / -2.54 | `day_skew(Volume)` |
| +0.65 | 0.187 | 4 | -1.87 / -2.52 | `ts_skew(day_last(Close), 20)` |
| +0.57 | 0.148 | 6 | -1.95 / -2.52 | `ts_argmin(day_skew(Volume), 1)` |

## 拆解(8 次评估)

### head score -1.80:`cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60)))` | -6.87 | -5.71 | -6.87 | — | (子树本身) |
| sufficiency | `day_last(in_slice(Vwap, 1, 60))` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| sufficiency | `day_first(in_slice(Open, 1, 60))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60)))` | -2.23 | -1.71 | -2.23 | +0.43 | `cross_stddev(day_last(in_slice(Vwap, 1, 60)), 30)` |
| swap | `Vwap->Close` | -1.91 | -1.81 | -1.91 | — | `cross_stddev(div(day_last(in_slice(Close, 1, 60)), day_first(in_slice(Open, 1, 60))), 30)` |
| swap | `Open->Close` | -2.03 | -1.98 | -2.03 | — | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Close, 1, 60))), 30)` |
| window | `cross_stddev@30->15` | -2.25 | -1.70 | -2.25 | — | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60))), 15)` |
| window | `cross_stddev@30->60` | -1.98 | -1.97 | -1.98 | — | `cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60))), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_first(Open)` — enrichment,均值差 +1.83,p 0.000
2. `day_close(Vwap)` — enrichment,均值差 +1.73,p 0.001
3. `add(day_centroid(Ret), add(day_gini(High), ListAge))` — enrichment,均值差 +1.47,p 0.005
4. `day_gini(Open)` — enrichment,均值差 +1.38,p 0.011
5. `day_max(Low)` — enrichment,均值差 +1.31,p 0.000
6. `cs_demean(day_max(Low))` — enrichment,均值差 +1.30,p 0.000
7. `cs_last_high05(cross_product(day_corr(Ret, Close), 15), cs_demean(day_max(Low)))` — enrichment,均值差 +1.28,p 0.000
8. `cross_product(day_corr(Ret, Close), 15)` — enrichment,均值差 +1.24,p 0.000
9. `day_corr(Ret, Close)` — enrichment,均值差 +1.23,p 0.000
10. `add(day_gini(High), ListAge)` — enrichment,均值差 +1.17,p 0.001
11. `div(day_gini(High), cs_last_high05(cross_product(day_corr(Ret, Close), 15), cs_demean(day_max(Low))))` — enrichment,均值差 +1.15,p 0.006
12. `day_corr(in_delta(Vwap, 5), Volume)` — enrichment,均值差 +1.02,p 0.005
13. `day_last(Close)` — enrichment,均值差 +0.99,p 0.023
14. `day_gini(Low)` — enrichment,均值差 +0.98,p 0.064
15. `ts_skew(day_corr(in_delta(Vwap, 5), Volume), 20)` — enrichment,均值差 +0.90,p 0.040
16. `day_gini(High)` — enrichment,均值差 +0.90,p 0.000
17. `day_skew(Volume)` — enrichment,均值差 +0.71,p 0.054

## 本组之前各轮的任务

- `prods2041Pr1a_Ea`:核心 `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), Volume, create_like(in_slice(Close, 1, 1), 0)))`;评分 59,过线 0,入 heads 0;采样计数 {'c05_no_core': 6305, 'c05_skeleton': 3334}
  - score -1.22(train -1.16 valid -1.22):`day_distinct_ratio(Open)`
  - score -1.22(train -1.10 valid -1.22):`day_distinct_ratio(High)`
  - score -2.19(train -2.19 valid -1.87):`day_es_ratio_hi(Ret)`
  - score -2.69(train -2.69 valid -2.58):`day_es_ratio_lo(Open)`
  - score -3.22(train -3.22 valid -2.64):`day_hurst(Volume)`
- `prods2041Pr1b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 17}
  - score -0.50(train -0.39 valid -0.50):`cs_first_low20(day_gini(Open), day_close(Vwap))`
  - score -0.51(train -0.41 valid -0.51):`cs_first_low20(cs_first_low20(day_gini(Open), day_first(Open)), day_first(Open))`
  - score -0.51(train -0.41 valid -0.51):`cs_first_low20(day_gini(Open), day_first(Open))`
  - score -0.52(train -0.37 valid -0.52):`cs_first_low20(day_gini(High), day_last(Close))`
  - score -0.53(train -0.36 valid -0.53):`cs_first_low20(day_gini(High), day_close(Vwap))`
- `prods2041Pr2a_Ea`:核心 `day_gini(High)`;评分 113,过线 0,入 heads 0;采样计数 {'c05_no_core': 1246, 'c05_skeleton': 679, 'c05_periphery_seen': 10}
  - score -0.54(train -0.31 valid -0.54):`div(day_gini(High), cs_last_high05(cross_product(cross_product(day_corr(Ret, Close), 15), 15), cs_demean(day_max(Low))))`
  - score -0.67(train -0.43 valid -0.67):`cs_bucket_zscore(div(day_gini(High), cs_last_high05(cross_product(day_corr(Ret, Close), 15), cs_demean(day_max(Low)))), ts_sum(day_sum(Amt), 1))`
  - score -0.87(train -0.87 valid +0.00):`cs_bucket_zscore(add(cs_bucket_zscore(add(day_centroid(Ret), add(day_gini(High), ListAge)), day_sum(Amt)), add(day_gini(High), ListAge)), day_sum(Amt))`
  - score -1.00(train -0.94 valid -1.00):`cs_bucket_zscore(div(day_gini(High), cs_last_high05(cross_product(day_corr(Ret, Close), 15), cs_demean(day_max(Low)))), ts_sum(day_skew(Volume), 1))`
  - score -1.01(train -1.01 valid -0.11):`add(day_centroid(Low), mul(cs_bucket_zscore(add(day_centroid(Ret), add(day_gini(High), ListAge)), day_sum(Amt)), ListAge))`

## 比原 head 好的拆解变体(R 候选)

(没有)
