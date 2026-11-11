# 定位:种子 2057,P 组,第 2 轮(只含 train / valid)

快照:prods2057M1_I0_open_search, prods2057M2_I0_open_search, prods2057Pr1a_Na, prods2057Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.35 | -1.05 | -1.35 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 20)` |
| -1.62 | -1.06 | -1.62 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 50)` |
| -1.62 | -1.07 | -1.62 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 20)` |
| -2.06 | -2.06 | -1.51 | +1 | 20 | prods2057M2_I0_open_search | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open)), 5)` |
| -2.21 | -1.98 | -2.21 | +1 | 20 | prods2057M2_I0_open_search | `day_corr(pow_2(Vwap), Close)` |
| -2.41 | -2.41 | -1.92 | +1 | 20 | prods2057M2_I0_open_search | `day_autocorr_n1(pow_2(Open))` |

## 共性:93 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.33 | 0.000 | 7 | +0.08 / -2.25 | `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)` |
| +2.24 | 0.001 | 4 | +0.06 / -2.17 | `ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10)` |
| +2.03 | 0.000 | 11 | -0.29 / -2.32 | `ts_stddev(day_zero_ratio(Ret), 10)` |
| +1.64 | 0.000 | 17 | -0.74 / -2.38 | `ts_stddev(day_centroid(Amt), 10)` |
| +1.58 | 0.000 | 11 | -0.69 / -2.26 | `ts_stddev(ts_stddev(day_centroid(Amt), 10), 50)` |
| +1.43 | 0.000 | 19 | -0.94 / -2.37 | `day_zero_ratio(Ret)` |
| +1.42 | 0.006 | 7 | -0.76 / -2.18 | `ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10)` |
| +1.29 | 0.000 | 20 | -1.06 / -2.35 | `day_centroid(Amt)` |
| +1.21 | 0.049 | 4 | -0.92 / -2.13 | `ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 50)` |
| -0.08 | 0.601 | 4 | -2.15 / -2.07 | `day_argmax(Open)` |
| -0.32 | 0.692 | 4 | -2.38 / -2.06 | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` |
| -0.70 | 0.973 | 13 | -2.68 / -1.98 | `day_sum(nt_cs_quantile_q25(Amt))` |

## 拆解(8 次评估)

### head score -2.06:`cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open))` | -2.42 | -2.42 | -1.42 | — | (子树本身) |
| swap | `Close->Vwap` | -2.91 | -2.49 | -2.91 | — | `cross_min(day_corr(pow_2(Vwap), nt_cs_mask_top_replace_mean_neg(Open)), 5)` |
| swap | `Open->Close` | — | — | — | — | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Close)), 5)` |
| window | `cross_min@5->2` | -2.18 | -2.18 | -1.29 | — | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open)), 2)` |
| window | `cross_min@5->10` | -1.92 | -1.92 | -1.84 | — | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open)), 10)` |

### head score -2.21:`day_corr(pow_2(Vwap), Close)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | — | — | — | — | `day_corr(pow_2(Close), Close)` |
| swap | `Close->Vwap` | — | — | — | — | `day_corr(pow_2(Vwap), Vwap)` |

### head score -2.41:`day_autocorr_n1(pow_2(Open))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Open->Close` | -2.26 | -2.20 | -2.26 | — | `day_autocorr_n1(pow_2(Close))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)` — enrichment,均值差 +2.33,p 0.000
2. `ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10)` — enrichment,均值差 +2.24,p 0.001
3. `ts_stddev(day_zero_ratio(Ret), 10)` — enrichment,均值差 +2.03,p 0.000
4. `ts_stddev(day_centroid(Amt), 10)` — enrichment,均值差 +1.64,p 0.000
5. `ts_stddev(ts_stddev(day_centroid(Amt), 10), 50)` — enrichment,均值差 +1.58,p 0.000
6. `day_zero_ratio(Ret)` — enrichment,均值差 +1.43,p 0.000
7. `ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10)` — enrichment,均值差 +1.42,p 0.006
8. `day_centroid(Amt)` — enrichment,均值差 +1.29,p 0.000
9. `ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 50)` — enrichment,均值差 +1.21,p 0.049

## 本组之前各轮的任务

- `prods2057Pr1a_Na`:核心 `—`;评分 57,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score +0.13(train +0.15 valid +0.13):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 50)`
  - score -0.02(train +0.11 valid -0.02):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 10), 5), 10), 50)`
  - score -0.10(train +0.19 valid -0.10):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Ret), 10), 50), 10), 50), 10), 50)`
  - score -0.15(train -0.15 valid -0.06):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 20), 50)`
  - score -0.27(train -0.05 valid -0.27):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 10), 50)`
- `prods2057Pr1b_Nb`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.32(train +0.32 valid +0.80):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 50)`
  - score +0.26(train +0.26 valid +0.70):`ts_stddev(ts_stddev(ts_delta(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 10), 50)`
  - score +0.16(train +0.16 valid +0.67):`ts_kurt(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 50), 10), 50)`
  - score +0.08(train +0.08 valid +0.18):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 10), 50), 10), 50)`
  - score +0.02(train +0.02 valid +0.64):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 20), 50), 10), 50)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.15(swap Open->Close):`day_autocorr_n1(pow_2(Close))`
- 增益 +0.14(window cross_min@5->10):`cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open)), 10)`
