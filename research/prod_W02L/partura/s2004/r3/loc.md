# 定位:种子 2004,P 组,第 3 轮(只含 train / valid)

快照:prods2004M1_I0_open_search, prods2004M2_I0_open_search, prods2004M3_I0_open_search, prods2004Pr1a_Ea, prods2004Pr1b_Nb, prods2004Pr2a_Ea, prods2004Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.12 | +0.24 | +0.12 | +1 | 0 | prods2004M3_I0_open_search | `ts_std(ts_max(ts_std(day_cov(Ret, Ret), 40), 40), 40)` |
| -0.21 | +0.13 | -0.21 | +1 | 5 | prods2004M3_I0_open_search | `ts_std(day_cov(Amt, Amt), 50)` |
| -0.32 | -0.08 | -0.32 | +1 | 5 | prods2004M3_I0_open_search | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(day_cov(Amt, Amt), 50))` |
| -0.64 | -0.64 | -0.08 | +1 | 5 | prods2004M1_I0_open_search | `ts_skew(day_cov(Ret, Volume), 40)` |
| -0.73 | -0.73 | -0.30 | +1 | 5 | prods2004M1_I0_open_search | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume, Amt), 15), 241)` |
| -0.75 | -0.75 | -0.65 | -1 | 20 | prods2004M2_I0_open_search | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2004M1_I0_open_search | `day_cov(Volume, Volume)` |
| -1.27 | -0.71 | -1.27 | +1 | 20 | prods2004M2_I0_open_search | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 15)` |
| -1.40 | -1.32 | -1.40 | -1 | 20 | prods2004M2_I0_open_search | `cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` |

## 共性:245 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.74 | 0.000 | 5 | -0.35 / -2.09 | `cs_demean(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))))` |
| +1.12 | 0.005 | 6 | -0.96 / -2.08 | `day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239))` |
| +1.06 | 0.010 | 5 | -1.02 / -2.08 | `cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)` |
| +1.01 | 0.041 | 4 | -1.06 / -2.07 | `ts_std(day_cov(Ret, Ret), 40)` |
| +0.94 | 0.001 | 18 | -1.18 / -2.13 | `cs_demean(div(day_cov(Ret, Volume), day_mean(Volume)))` |
| +0.89 | 0.054 | 6 | -1.19 / -2.08 | `cross_tail_mean_q25(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))), 120)` |
| +0.79 | 0.112 | 4 | -1.27 / -2.07 | `cross_ema(div(day_cov(Ret, Volume), day_mean(Volume)), 120)` |
| +0.79 | 0.110 | 4 | -1.28 / -2.07 | `day_cov(Amt, Amt)` |
| +0.78 | 0.012 | 9 | -1.31 / -2.08 | `ts_std(day_cov(Ret, Volume), 40)` |
| +0.75 | 0.029 | 7 | -1.33 / -2.08 | `cross_zscore(day_cov(Ret, Volume), 60)` |
| +0.74 | 0.046 | 6 | -1.33 / -2.07 | `cross_zscore(day_cov(Ret, Volume), 120)` |
| +0.71 | 0.067 | 5 | -1.36 / -2.07 | `ts_std(ts_std(day_cov(Ret, Volume), 40), 40)` |
| +0.69 | 0.000 | 123 | -1.71 / -2.40 | `day_cov(Ret, Volume)` |
| +0.55 | 0.104 | 11 | -1.53 / -2.08 | `day_std(Ret)` |
| +0.53 | 0.098 | 8 | -1.54 / -2.07 | `day_cov(Volume, Volume)` |
| +0.49 | 0.009 | 40 | -1.65 / -2.14 | `div(day_cov(Ret, Volume), day_mean(Volume))` |
| +0.45 | 0.014 | 42 | -1.68 / -2.13 | `day_mean(Volume)` |
| +0.25 | 0.386 | 10 | -1.82 / -2.07 | `day_cov(in_slice(Ret, 1, 239), in_slice(Ret, 1, 239))` |
| +0.21 | 0.411 | 15 | -1.86 / -2.07 | `day_cov(Ret, Ret)` |
| +0.20 | 0.436 | 4 | -1.86 / -2.06 | `cross_corr(day_cov(Ret, Volume), day_std(Ret), 60)` |

## 拆解(19 次评估)

### head score +0.12:`ts_std(ts_max(ts_std(day_cov(Ret, Ret), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_std(day_cov(Ret, Ret), 40), 40)` | -1.30 | -0.47 | -1.30 | — | (子树本身) |
| sufficiency | `ts_std(day_cov(Ret, Ret), 40)` | -2.63 | -1.31 | -2.63 | — | (子树本身) |
| sufficiency | `day_cov(Ret, Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |
| knockout | `ts_max(ts_std(day_cov(Ret, Ret), 40), 40)` | -1.72 | -0.26 | -1.72 | +1.84 | `ts_std(ts_std(day_cov(Ret, Ret), 40), 40)` |
| knockout | `ts_std(day_cov(Ret, Ret), 40)` | -1.63 | -0.37 | -1.63 | +1.75 | `ts_std(ts_max(day_cov(Ret, Ret), 40), 40)` |
| window | `ts_std@40->20` | -0.56 | -0.56 | -0.42 | — | `ts_std(ts_max(ts_std(day_cov(Ret, Ret), 40), 40), 20)` |
| window | `ts_std@40->80` | -0.96 | +0.13 | -0.96 | — | `ts_std(ts_max(ts_std(day_cov(Ret, Ret), 40), 40), 80)` |

### head score -0.21:`ts_std(day_cov(Amt, Amt), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Amt, Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| swap | `Amt->Volume` | -1.10 | -1.10 | -1.06 | — | `ts_std(day_cov(Volume, Volume), 50)` |
| window | `ts_std@50->25` | -2.45 | -2.45 | -1.09 | — | `ts_std(day_cov(Amt, Amt), 25)` |
| window | `ts_std@50->100` | +0.30 | +0.30 | +0.51 | — | `ts_std(day_cov(Amt, Amt), 100)` |

### head score -0.32:`add(ts_quantile_q50(day_cov(Amt, Amt), 40), ts_std(day_cov(Amt, Amt), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q50(day_cov(Amt, Amt), 40)` | -2.98 | -2.34 | -2.98 | — | (子树本身) |
| sufficiency | `ts_std(day_cov(Amt, Amt), 50)` | -0.20 | +0.13 | -0.20 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| knockout | `ts_quantile_q50(day_cov(Amt, Amt), 40)` | +0.01 | +0.16 | +0.01 | -0.32 | `add(day_cov(Amt, Amt), ts_std(day_cov(Amt, Amt), 50))` |
| knockout | `ts_std(day_cov(Amt, Amt), 50)` | -3.16 | -2.56 | -3.16 | +2.85 | `add(ts_quantile_q50(day_cov(Amt, Amt), 40), day_cov(Amt, Amt))` |
| swap | `Amt->Volume` | -1.15 | -1.15 | -1.11 | — | `add(ts_quantile_q50(day_cov(Volume, Volume), 40), ts_std(day_cov(Volume, Volume), 50))` |
| window | `ts_quantile_q50@40->20` | -0.20 | -0.05 | -0.20 | — | `add(ts_quantile_q50(day_cov(Amt, Amt), 20), ts_std(day_cov(Amt, Amt), 50))` |
| window | `ts_quantile_q50@40->80` | -0.30 | -0.13 | -0.30 | — | `add(ts_quantile_q50(day_cov(Amt, Amt), 80), ts_std(day_cov(Amt, Amt), 50))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_demean(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))))` — enrichment,均值差 +1.74,p 0.000
2. `day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239))` — enrichment,均值差 +1.12,p 0.005
3. `cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)` — enrichment,均值差 +1.06,p 0.010
4. `ts_std(day_cov(Ret, Ret), 40)` — enrichment,均值差 +1.01,p 0.041
5. `cs_demean(div(day_cov(Ret, Volume), day_mean(Volume)))` — enrichment,均值差 +0.94,p 0.001
6. `cross_tail_mean_q25(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))), 120)` — enrichment,均值差 +0.89,p 0.054
7. `ts_std(day_cov(Ret, Volume), 40)` — enrichment,均值差 +0.78,p 0.012
8. `cross_zscore(day_cov(Ret, Volume), 60)` — enrichment,均值差 +0.75,p 0.029
9. `cross_zscore(day_cov(Ret, Volume), 120)` — enrichment,均值差 +0.74,p 0.046
10. `ts_std(ts_std(day_cov(Ret, Volume), 40), 40)` — enrichment,均值差 +0.71,p 0.067
11. `day_cov(Ret, Volume)` — enrichment,均值差 +0.69,p 0.000
12. `day_cov(Volume, Volume)` — enrichment,均值差 +0.53,p 0.098
13. `div(day_cov(Ret, Volume), day_mean(Volume))` — enrichment,均值差 +0.49,p 0.009
14. `day_mean(Volume)` — enrichment,均值差 +0.45,p 0.014

## 本组之前各轮的任务

- `prods2004Pr1a_Ea`:核心 `day_cov(Ret, Volume)`;评分 76,过线 0,入 heads 0;采样计数 {'c05_no_core': 931, 'c05_skeleton': 456}
  - score -0.25(train -0.25 valid -0.20):`cross_corr(day_cov(Ret, Volume), day_std(Ret), 60)`
  - score -0.27(train -0.27 valid -0.18):`cross_reg_tvalue(day_cov(Ret, Volume), day_std(Ret), 60)`
  - score -0.48(train -0.48 valid -0.11):`add(cross_tail_mean_q75(cross_zscore(day_cov(Ret, Volume), 120), 60), cross_tail_mean_q25(cross_zscore(day_cov(Ret, Volume), 120), 60))`
  - score -0.65(train -0.65 valid -0.51):`cs_mask_top_replace_mean_neg(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30))`
  - score -0.67(train -0.67 valid -0.57):`cs_regres(cs_rank(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)), cs_rank(cross_mean(day_sum(Ret), 20)))`
- `prods2004Pr1b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.41(train -0.41 valid -0.02):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Ret, 1, 239)), 60)`
  - score -0.42(train -0.42 valid +0.06):`cross_corr(day_cov(Ret, Ret), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60)`
  - score -0.52(train -0.52 valid -0.52):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60)`
  - score -0.67(train -0.67 valid +0.02):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 241)`
  - score -0.68(train -0.68 valid -0.27):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Volume, 1, 239), in_slice(Volume, 1, 239)), 60)`
- `prods2004Pr2a_Ea`:核心 `div(day_cov(Ret, Volume), day_mean(Volume))`;评分 80,过线 0,入 heads 0;采样计数 {'c05_no_core': 1465, 'c05_skeleton': 681, 'c05_periphery_seen': 5}
  - score -0.01(train -0.01 valid +0.30):`add(cross_tail_mean_q75(cs_demean(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume)))), 120), cross_tail_mean_q25(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))), 120))`
  - score -0.01(train -0.01 valid +0.30):`add(cross_tail_mean_q75(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))), 120), cross_tail_mean_q25(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))), 120))`
  - score -0.17(train -0.17 valid +0.20):`cross_ema(div(day_cov(Ret, Volume), day_mean(Volume)), 120)`
  - score -0.17(train -0.17 valid +0.20):`cs_demean(cross_ema(div(day_cov(Ret, Volume), day_mean(Volume)), 120))`
  - score -0.19(train -0.19 valid +0.16):`cross_ema(cs_demean(div(day_cov(Ret, Volume), day_mean(Volume))), 120)`
- `prods2004Pr2b_Nb`:核心 `—`;评分 0,过线 0,入 heads 0;采样计数 {}

## 比原 head 好的拆解变体(R 候选)

(没有)
