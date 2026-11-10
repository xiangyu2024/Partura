# 定位:种子 2005,P 组,第 3 轮(只含 train / valid)

快照:prods2005M1_I0_open_search, prods2005M2_I0_open_search, prods2005M3_I0_open_search, prods2005Pr1a_Ea, prods2005Pr1b_Nb, prods2005Pr2a_Ea, prods2005Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.62 | +0.62 | +0.93 | +1 | 5 | prods2005M3_I0_open_search | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| +0.56 | +0.56 | +1.03 | +1 | 0 | prods2005M3_I0_open_search | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| +0.44 | +0.44 | +0.84 | +1 | 0 | prods2005M3_I0_open_search | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| -1.09 | -0.95 | -1.09 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(day_cov(Ret, Close), 241)` |
| -1.42 | -1.27 | -1.42 | -1 | 20 | prods2005M2_I0_open_search | `cross_mean(day_cov(Close, Ret), 3)` |
| -1.47 | -1.42 | -1.47 | +1 | 20 | prods2005M1_I0_open_search | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30), cross_mean(day_std(Amt), 30))` |
| -1.54 | -1.54 | -1.20 | -1 | 0 | prods2005M2_I0_open_search | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 60)` |
| -1.70 | -1.70 | -1.61 | +1 | 5 | prods2005M2_I0_open_search | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30), 3)` |
| -1.85 | -1.85 | -0.75 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5)` |

## 共性:242 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.24 | 0.000 | 16 | -0.22 / -2.46 | `day_cov(Amt, Amt)` |
| +2.23 | 0.000 | 9 | -0.17 / -2.40 | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` |
| +2.21 | 0.000 | 14 | -0.23 / -2.44 | `cross_stddev(day_cov(Amt, Amt), 60)` |
| +2.15 | 0.001 | 4 | -0.20 / -2.35 | `cross_fangzheng(cross_stddev(day_cov(Amt, Amt), 60), 241)` |
| +1.43 | 0.006 | 5 | -0.92 / -2.34 | `div(day_cov(Amt, Low), mul(day_std(Amt), cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241)))` |
| +1.43 | 0.006 | 5 | -0.92 / -2.34 | `mul(day_std(Amt), cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241))` |
| +1.37 | 0.000 | 10 | -1.00 / -2.37 | `sub(day_std(Amt), day_std(Low))` |
| +1.37 | 0.001 | 9 | -1.00 / -2.37 | `div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low)))` |
| +1.37 | 0.001 | 9 | -1.00 / -2.37 | `cross_stddev(div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low))), 241)` |
| +1.15 | 0.007 | 7 | -1.20 / -2.35 | `cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241)` |
| +1.12 | 0.000 | 14 | -1.26 / -2.38 | `div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low)))` |
| +0.86 | 0.002 | 15 | -1.51 / -2.37 | `mul(day_std(Low), day_std(Low))` |
| +0.66 | 0.001 | 36 | -1.75 / -2.41 | `day_std(Amt)` |
| +0.65 | 0.037 | 9 | -1.69 / -2.34 | `cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241)` |
| +0.59 | 0.089 | 6 | -1.74 / -2.33 | `pow_3(day_cov(Ret, Close))` |
| +0.51 | 0.003 | 50 | -1.91 / -2.42 | `day_std(Low)` |
| +0.51 | 0.097 | 6 | -1.82 / -2.33 | `day_cov(Close, Ret)` |
| +0.48 | 0.181 | 4 | -1.85 / -2.32 | `day_flat_run_max(Low)` |
| +0.38 | 0.156 | 8 | -1.95 / -2.33 | `ts_delay(day_close(Close), 1)` |
| +0.37 | 0.101 | 8 | -1.95 / -2.33 | `day_zero_ratio(Ret)` |

## 拆解(35 次评估)

### head score +0.62:`add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` | +0.56 | +0.56 | +1.02 | — | (子树本身) |
| sufficiency | `ts_quantile_q50(day_cov(Amt, Amt), 1)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| sufficiency | `cross_stddev(day_cov(Amt, Amt), 60)` | +0.14 | +0.35 | +0.14 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| knockout | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` | +0.26 | +0.43 | +0.26 | +0.36 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), cross_stddev(day_cov(Amt, Amt), 60))` |
| knockout | `ts_quantile_q50(day_cov(Amt, Amt), 1)` | +0.62 | +0.62 | +0.92 | +0.00 | `add(day_cov(Amt, Amt), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| knockout | `cross_stddev(day_cov(Amt, Amt), 60)` | +0.01 | +0.16 | +0.01 | +0.61 | `add(ts_quantile_q50(day_cov(Amt, Amt), 1), ts_std(day_cov(Amt, Amt), 50))` |
| swap | `Amt->Volume` | -2.13 | -0.74 | -2.13 | — | `add(ts_quantile_q50(day_cov(Volume, Volume), 1), ts_std(cross_stddev(day_cov(Volume, Volume), 60), 50))` |
| window | `ts_quantile_q50@1->2` | +0.62 | +0.62 | +0.90 | — | `add(ts_quantile_q50(day_cov(Amt, Amt), 2), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |

### head score +0.56:`add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40)` | -2.47 | -2.03 | -2.47 | — | (子树本身) |
| sufficiency | `cross_max(day_min(nt_ts_skew(Close, 3)), 5)` | -1.64 | -1.64 | -1.40 | — | (子树本身) |
| sufficiency | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` | +0.56 | +0.56 | +1.02 | — | (子树本身) |
| sufficiency | `day_min(nt_ts_skew(Close, 3))` | -1.91 | -1.91 | -1.61 | — | (子树本身) |
| knockout | `ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40)` | +0.56 | +0.56 | +1.02 | +0.00 | `add(cross_max(day_min(nt_ts_skew(Close, 3)), 5), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| knockout | `cross_max(day_min(nt_ts_skew(Close, 3)), 5)` | +0.56 | +0.56 | +1.02 | -0.00 | `add(ts_quantile_q50(day_min(nt_ts_skew(Close, 3)), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| knockout | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` | +0.14 | +0.33 | +0.14 | +0.42 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40), cross_stddev(day_cov(Amt, Amt), 60))` |
| knockout | `cross_stddev(day_cov(Amt, Amt), 60)` | -0.20 | +0.11 | -0.20 | +0.76 | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40), ts_std(day_cov(Amt, Amt), 50))` |
| swap | `Close->Vwap` | +0.56 | +0.56 | +1.02 | — | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Vwap, 3)), 5), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| swap | `Amt->Volume` | -1.41 | -0.57 | -1.41 | — | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 40), ts_std(cross_stddev(day_cov(Volume, Volume), 60), 50))` |
| window | `ts_quantile_q50@40->20` | +0.56 | +0.56 | +1.02 | — | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 20), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| window | `ts_quantile_q50@40->80` | +0.56 | +0.56 | +1.02 | — | `add(ts_quantile_q50(cross_max(day_min(nt_ts_skew(Close, 3)), 5), 80), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |

### head score +0.44:`add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` | +0.56 | +0.56 | +1.02 | — | (子树本身) |
| sufficiency | `ts_quantile_q50(day_cov(Amt, Amt), 40)` | -2.98 | -2.34 | -2.98 | — | (子树本身) |
| sufficiency | `cross_stddev(day_cov(Amt, Amt), 60)` | +0.14 | +0.35 | +0.14 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| knockout | `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` | +0.04 | +0.17 | +0.04 | +0.41 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), cross_stddev(day_cov(Amt, Amt), 60))` |
| knockout | `ts_quantile_q50(day_cov(Amt, Amt), 40)` | +0.62 | +0.62 | +0.92 | -0.18 | `add(day_cov(Amt, Amt), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| knockout | `cross_stddev(day_cov(Amt, Amt), 60)` | -0.30 | -0.08 | -0.30 | +0.74 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(day_cov(Amt, Amt), 50))` |
| swap | `Amt->Volume` | -2.11 | -0.94 | -2.11 | — | `add(ts_quantile_q50(day_cov(Volume, Volume), 40), ts_std(cross_stddev(day_cov(Volume, Volume), 60), 50))` |
| window | `ts_quantile_q50@40->20` | +0.58 | +0.58 | +1.05 | — | `add(ts_quantile_q50(day_cov(Amt, Amt), 20), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |
| window | `ts_quantile_q50@40->80` | +0.41 | +0.41 | +0.78 | — | `add(ts_quantile_q50(day_cov(Amt, Amt), 80), ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50))` |

### head score -1.09:`cross_max(day_cov(Ret, Close), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Ret, Close)` | -1.25 | -1.14 | -1.25 | — | (子树本身) |
| swap | `Close->Vwap` | -1.71 | -1.71 | -0.86 | — | `cross_max(day_cov(Ret, Vwap), 241)` |
| window | `cross_max@241->120` | -1.70 | -1.35 | -1.70 | — | `cross_max(day_cov(Ret, Close), 120)` |
| window | `cross_max@241->482` | -1.37 | -1.32 | -1.37 | — | `cross_max(day_cov(Ret, Close), 482)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_std(cross_stddev(day_cov(Amt, Amt), 60), 50)` — ablation,自身 score +0.56(所在 head +0.62)
2. `day_cov(Amt, Amt)` — enrichment,均值差 +2.24,p 0.000
3. `cross_stddev(day_cov(Amt, Amt), 60)` — enrichment,均值差 +2.21,p 0.000
4. `cross_fangzheng(cross_stddev(day_cov(Amt, Amt), 60), 241)` — enrichment,均值差 +2.15,p 0.001
5. `div(day_cov(Amt, Low), mul(day_std(Amt), cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241)))` — enrichment,均值差 +1.43,p 0.006
6. `mul(day_std(Amt), cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241))` — enrichment,均值差 +1.43,p 0.006
7. `sub(day_std(Amt), day_std(Low))` — enrichment,均值差 +1.37,p 0.000
8. `div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low)))` — enrichment,均值差 +1.37,p 0.001
9. `cross_stddev(div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low))), 241)` — enrichment,均值差 +1.37,p 0.001
10. `cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241)` — enrichment,均值差 +1.15,p 0.007
11. `div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low)))` — enrichment,均值差 +1.12,p 0.000
12. `mul(day_std(Low), day_std(Low))` — enrichment,均值差 +0.86,p 0.002
13. `day_std(Amt)` — enrichment,均值差 +0.66,p 0.001
14. `cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241)` — enrichment,均值差 +0.65,p 0.037
15. `pow_3(day_cov(Ret, Close))` — enrichment,均值差 +0.59,p 0.089
16. `day_std(Low)` — enrichment,均值差 +0.51,p 0.003
17. `day_cov(Close, Ret)` — enrichment,均值差 +0.51,p 0.097
18. `day_cov(Ret, Close)` — enrichment,均值差 +0.32,p 0.058

## 本组之前各轮的任务

- `prods2005Pr1a_Ea`:核心 `day_cov(Ret, Close)`;评分 76,过线 0,入 heads 0;采样计数 {'c05_no_core': 1334, 'c05_skeleton': 680}
  - score -0.84(train -0.34 valid -0.84):`inv(cross_tail_mean_q25(pow_3(day_cov(Ret, Close)), 241))`
  - score -1.12(train -0.99 valid -1.12):`cs_last_high20(sub(day_cov(Ret, Close), day_flat_run_max(Low)), day_cov(Ret, Close))`
  - score -1.19(train -1.19 valid -0.39):`cs_last_high20(day_cov(Ret, Close), day_cov(Ret, Close))`
  - score -1.25(train -1.14 valid -1.25):`neg(day_cov(Ret, Close))`
  - score -1.25(train -1.14 valid -1.25):`signedpower(day_cov(Ret, Close))`
- `prods2005Pr1b_Nb`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 17}
  - score -0.91(train -0.91 valid -0.89):`cross_corr(div(cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt)), day_sum(Amt)), day_zero_ratio(Ret), 60)`
  - score -0.93(train -0.92 valid -0.93):`cross_corr(day_close(Amt), day_zero_ratio(Ret), 15)`
  - score -0.99(train -0.86 valid -0.99):`cross_corr(div(day_close(Amt), day_sum(Amt)), div(day_first(Open), ts_delay(day_close(Close), 1)), 60)`
  - score -1.00(train -0.91 valid -1.00):`cross_corr(div(day_close(Amt), day_sum(Amt)), div(day_first(Vwap), ts_delay(day_close(Close), 1)), 60)`
  - score -1.06(train -0.98 valid -1.06):`cross_corr(div(cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt)), day_sum(Amt)), day_sum(Ret), 60)`
- `prods2005Pr2a_Ea`:核心 `day_cov(Amt, Low)`;评分 98,过线 0,入 heads 0;采样计数 {'c05_no_core': 759, 'c05_skeleton': 411}
  - score +0.08(train +0.46 valid +0.08):`div(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), cross_tail_mean_q25(div(day_cov(Amt, Low), day_std(Low)), 241))), 241), cross_stddev(div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low))), 241))`
  - score -0.03(train -0.03 valid +0.07):`div(cross_mean(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241), cross_stddev(div(day_cov(Amt, Low), mul(day_ar1_coefficient(Low), day_std(Low))), 241))`
  - score -0.05(train -0.05 valid +0.01):`div(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241), cross_stddev(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241))`
  - score -0.07(train -0.07 valid -0.05):`div(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Low), day_std(Low))), 241))), 241), cross_stddev(div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low))), 241))`
  - score -0.12(train +0.43 valid -0.12):`div(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), cross_tail_mean_q25(day_cov(Amt, Low), 241))), 241), cross_stddev(div(day_cov(Amt, Low), sub(day_std(Amt), day_std(Low))), 241))`
- `prods2005Pr2b_Nb`:核心 `—`;评分 0,过线 0,入 heads 0;采样计数 {}

## 比原 head 好的拆解变体(R 候选)

(没有)
