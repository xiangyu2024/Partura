# 定位:种子 2028,P 组,第 3 轮(只含 train / valid)

快照:prods2028M1_I0_open_search, prods2028M2_I0_open_search, prods2028M3_I0_open_search, prods2028Pr1b_Nb, prods2028Pr2a_Ea, prods2028Pr2b_Eb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.87 | +0.98 | +0.87 | -1 | 0 | prods2028Pr1b_Nb | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Volume), 3), 20))` |
| -0.04 | +0.00 | -0.04 | +1 | 5 | prods2028M2_I0_open_search | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 90))` |
| -1.49 | -1.31 | -1.49 | -1 | 5 | prods2028M3_I0_open_search | `cross_quantile_q25(pow_3(day_mean(Volume)), 5)` |
| -1.64 | -0.96 | -1.64 | +1 | 20 | prods2028M3_I0_open_search | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(neg(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume)))))))` |
| -1.69 | -1.45 | -1.69 | -1 | 5 | prods2028M3_I0_open_search | `cross_quantile_q25(pow_3(day_mean(Volume)), 15)` |
| -1.91 | -1.91 | -1.55 | -1 | 20 | prods2028M2_I0_open_search | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 30))` |

## 共性:175 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.86 | 0.000 | 6 | +0.00 / -1.86 | `cross_ema(day_gini(Amt), 60)` |
| +1.81 | 0.000 | 5 | -0.03 / -1.84 | `cs_last_low10(cross_ema(day_gini(Amt), 60), day_close(Low))` |
| +1.71 | 0.000 | 10 | -0.18 / -1.89 | `day_gini(Amt)` |
| +0.87 | 0.009 | 10 | -0.97 / -1.84 | `ts_delay(day_last(Close), 1)` |
| +0.84 | 0.057 | 5 | -0.98 / -1.82 | `cross_corr(cross_delay(cross_zscore(day_kurt(Volume), 60), 1), cs_demean(ts_delta(log(day_last(Close)), 1)), 120)` |
| +0.81 | 0.001 | 59 | -1.25 / -2.07 | `day_close(Low)` |
| +0.79 | 0.032 | 7 | -1.03 / -1.82 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.78 | 0.053 | 8 | -1.05 / -1.83 | `cs_last_high05(LogTotalCap, LogTotalCap)` |
| +0.73 | 0.024 | 15 | -1.12 / -1.85 | `cs_last_high05(LogTotalCap, day_close(Low))` |
| +0.69 | 0.031 | 14 | -1.16 / -1.85 | `cs_demean(ts_delta(log(day_last(Close)), 1))` |
| +0.69 | 0.020 | 24 | -1.20 / -1.89 | `pow_2_5(LogTotalCap)` |
| +0.68 | 0.170 | 4 | -1.13 / -1.81 | `day_at_max_ratio(sqrt(Vwap))` |
| +0.66 | 0.009 | 25 | -1.22 / -1.89 | `day_last(Close)` |
| +0.63 | 0.021 | 20 | -1.23 / -1.86 | `cross_delay(cross_zscore(day_kurt(Volume), 60), 1)` |
| +0.62 | 0.105 | 12 | -1.22 / -1.83 | `cross_ema(day_kurt(Volume), 60)` |
| +0.55 | 0.205 | 5 | -1.26 / -1.81 | `cs_first_low40(cs_last_high05(LogTotalCap, day_close(Low)), pow_2_5(LogTotalCap))` |
| +0.52 | 0.068 | 15 | -1.32 / -1.84 | `day_first(Open)` |
| +0.47 | 0.115 | 16 | -1.36 / -1.84 | `log(day_last(Close))` |
| +0.47 | 0.115 | 16 | -1.36 / -1.84 | `ts_delta(log(day_last(Close)), 1)` |
| +0.41 | 0.096 | 27 | -1.45 / -1.85 | `cross_zscore(day_kurt(Volume), 60)` |

## 拆解(32 次评估)

### head score +0.87:`div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Volume), 3), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low40(LogTotalCap, day_close(Low))` | +0.02 | +0.02 | +0.56 | — | (子树本身) |
| sufficiency | `day_close(Low)` | -2.35 | -1.59 | -2.35 | — | (子树本身) |
| sufficiency | `day_kurt(Volume)` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| knockout | `cs_first_low40(LogTotalCap, day_close(Low))` | -3.47 | -2.61 | -3.47 | +4.34 | `div(LogTotalCap, cross_ema(add(day_kurt(Volume), 3), 20))` |
| knockout | `add(day_kurt(Volume), 3)` | +0.82 | +0.82 | +0.88 | +0.05 | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(day_kurt(Volume), 20))` |
| swap | `Low->High` | +0.87 | +1.00 | +0.87 | — | `div(cs_first_low40(LogTotalCap, day_close(High)), cross_ema(add(day_kurt(Volume), 3), 20))` |
| swap | `Volume->Amt` | +0.86 | +1.04 | +0.86 | — | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Amt), 3), 20))` |
| window | `cross_ema@20->10` | +0.92 | +0.92 | +0.93 | — | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Volume), 3), 10))` |
| window | `cross_ema@20->40` | +0.81 | +0.89 | +0.81 | — | `div(cs_first_low40(LogTotalCap, day_close(Low)), cross_ema(add(day_kurt(Volume), 3), 40))` |

### head score -0.04:`pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 90))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 90)` | -0.04 | +0.00 | -0.04 | — | (子树本身) |
| sufficiency | `ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10)` | — | — | — | — | 门槛废品 |
| sufficiency | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)` | -2.10 | -2.10 | -2.06 | — | (子树本身) |
| knockout | `ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 90)` | — | — | — | — | `pow_1_5(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10))` |
| knockout | `ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10)` | -0.15 | -0.15 | -0.03 | +0.10 | `pow_1_5(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 90))` |
| knockout | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10))` | -0.06 | -0.06 | +0.06 | +0.01 | `pow_1_5(ts_max(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10), 10), 90))` |
| knockout | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)` | — | — | — | — | `pow_1_5(ts_max(ts_max(pow_2(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2))), 10), 90))` |
| window | `ts_max@90->45` | -0.56 | -0.56 | -0.41 | — | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 45))` |
| window | `ts_max@90->180` | -0.43 | +0.22 | -0.43 | — | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 180))` |

### head score -1.49:`cross_quantile_q25(pow_3(day_mean(Volume)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_3(day_mean(Volume))` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_mean(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `pow_3(day_mean(Volume))` | -1.55 | -1.30 | -1.55 | +0.07 | `cross_quantile_q25(day_mean(Volume), 5)` |
| swap | `Volume->Amt` | -4.01 | -3.01 | -4.01 | — | `cross_quantile_q25(pow_3(day_mean(Amt)), 5)` |
| window | `cross_quantile_q25@5->2` | -1.41 | -1.15 | -1.41 | — | `cross_quantile_q25(pow_3(day_mean(Volume)), 2)` |
| window | `cross_quantile_q25@5->10` | -1.68 | -1.41 | -1.68 | — | `cross_quantile_q25(pow_3(day_mean(Volume)), 10)` |

### head score -1.64:`cs_mask_top_replace_mean(cs_mask_top_replace_mean(neg(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume)))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean(neg(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))))` | -2.07 | -0.70 | -2.07 | — | (子树本身) |
| sufficiency | `neg(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume)))))` | -1.37 | -1.18 | -1.37 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))` | -1.37 | -1.18 | -1.37 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean(pow_3(day_mean(Volume)))` | -1.39 | -1.19 | -1.39 | — | (子树本身) |
| knockout | `neg(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume)))))` | -1.30 | -1.19 | -1.30 | -0.34 | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))))` |
| knockout | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))` | -1.40 | -0.70 | -1.40 | -0.24 | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(neg(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))))` |
| swap | `Volume->Amt` | -1.61 | -1.61 | -1.40 | — | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(neg(cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Amt)))))))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_ema(day_gini(Amt), 60)` — enrichment,均值差 +1.86,p 0.000
2. `cs_last_low10(cross_ema(day_gini(Amt), 60), day_close(Low))` — enrichment,均值差 +1.81,p 0.000
3. `day_gini(Amt)` — enrichment,均值差 +1.71,p 0.000
4. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +0.87,p 0.009
5. `cross_corr(cross_delay(cross_zscore(day_kurt(Volume), 60), 1), cs_demean(ts_delta(log(day_last(Close)), 1)), 120)` — enrichment,均值差 +0.84,p 0.057
6. `day_close(Low)` — enrichment,均值差 +0.81,p 0.001
7. `div(day_first(Open), ts_delay(day_last(Close), 1))` — enrichment,均值差 +0.79,p 0.032
8. `cs_last_high05(LogTotalCap, LogTotalCap)` — enrichment,均值差 +0.78,p 0.053
9. `cs_last_high05(LogTotalCap, day_close(Low))` — enrichment,均值差 +0.73,p 0.024
10. `cs_demean(ts_delta(log(day_last(Close)), 1))` — enrichment,均值差 +0.69,p 0.031
11. `pow_2_5(LogTotalCap)` — enrichment,均值差 +0.69,p 0.020
12. `day_last(Close)` — enrichment,均值差 +0.66,p 0.009
13. `cross_delay(cross_zscore(day_kurt(Volume), 60), 1)` — enrichment,均值差 +0.63,p 0.021
14. `day_first(Open)` — enrichment,均值差 +0.52,p 0.068
15. `cross_zscore(day_kurt(Volume), 60)` — enrichment,均值差 +0.41,p 0.096
16. `day_kurt(Volume)` — enrichment,均值差 +0.19,p 0.065

## 本组之前各轮的任务

- `prods2028Pr1b_Nb`:核心 `—`;评分 71,过线 2,入 heads 1;采样计数 {'c05_skeleton': 2}
  - score +0.73(train +0.73 valid +0.82):`div(cs_first_low40(LogTotalCap, day_close(Low)), day_kurt(Volume))`
  - score +0.58(train +0.58 valid +0.77):`div(cs_first_low40(cs_last_high05(LogTotalCap, cs_first_low40(cs_last_high05(LogTotalCap, day_close(Low)), day_close(Low))), day_close(Low)), day_kurt(Volume))`
  - score -0.44(train -0.44 valid +0.15):`div(cs_first_low40(cs_last_high05(LogTotalCap, LogTotalCap), cs_mask_top_replace_mean_neg(LogTotalCap)), -5)`
  - score -0.59(train -0.59 valid +0.16):`div(cs_first_low40(cs_last_high05(cs_last_high05(pow_2_5(LogTotalCap), day_close(Low)), cs_last_high05(pow_2_5(LogTotalCap), day_close(Low))), cs_last_high05(cs_last_high05(pow_2_5(LogTotalCap), day_close(Low)), cs_last_high05(pow_2_5(LogTotalCap), day_close(Low)))), -5)`
  - score -0.59(train -0.59 valid +0.16):`div(cs_first_low40(cs_last_high05(cs_last_high05(LogTotalCap, day_close(Low)), cs_last_high05(LogTotalCap, day_close(Low))), cs_last_high05(cs_last_high05(LogTotalCap, day_close(Low)), cs_last_high05(LogTotalCap, day_close(Low)))), -5)`
- `prods2028Pr2a_Ea`:核心 `day_kurt(Volume)`;评分 102,过线 0,入 heads 0;采样计数 {'c05_no_core': 965, 'c05_skeleton': 455}
  - score -0.22(train -0.22 valid +0.02):`cross_corr(cross_delay(cross_zscore(day_kurt(Volume), 60), 1), cs_demean(ts_delta(log(day_last(Close)), 1)), 120)`
  - score -0.32(train +0.06 valid -0.32):`cross_corr(cs_rank(day_kurt(Volume)), day_at_max_ratio(sqrt(Vwap)), 120)`
  - score -0.35(train -0.29 valid -0.35):`mul(cross_corr(cs_rank(day_kurt(Volume)), day_at_max_ratio(sqrt(Vwap)), 120), replace_small_with_nan(is_gt(ListAge, 120)))`
  - score -0.41(train -0.41 valid -0.13):`mul(cross_corr(cross_delay(cross_zscore(day_kurt(Volume), 60), 1), cs_demean(ts_delta(log(log(day_last(Vwap))), 1)), 120), replace_small_with_nan(is_gt(ListAge, 120)))`
  - score -0.42(train -0.12 valid -0.42):`mul(cross_corr(cross_delay(cross_zscore(day_kurt(Volume), 3), 1), sub(div(is_gt(ListAge, 120), ts_delay(day_last(Close), 1)), 1), 120), div(is_gt(ListAge, 120), ts_delay(day_last(Close), 1)))`
- `prods2028Pr2b_Eb`:核心 `day_close(Low)`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 730, 'c05_no_core': 1450}
  - score +0.34(train +0.34 valid +0.44):`cs_last_low10(day_gini(Amt), day_close(Low))`
  - score +0.17(train +0.17 valid +0.44):`cs_last_low10(cross_ema(day_gini(Amt), 60), day_close(Low))`
  - score +0.11(train +0.11 valid +0.36):`cs_last_low10(cross_ema(day_kurt(Volume), 60), day_close(Low))`
  - score +0.11(train +0.11 valid +0.36):`cs_last_low10(cross_ema(day_kurt(Volume), 60), cs_last_low10(cross_ema(day_gini(Amt), 60), day_close(Low)))`
  - score +0.11(train +0.11 valid +0.36):`cs_last_low10(cross_ema(day_kurt(Volume), 60), cs_last_low10(cross_ema(day_gini(Amt), 60), cs_last_low10(cross_ema(day_gini(Amt), 60), day_close(Low))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(knockout cs_mask_top_replace_mean(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))):`cs_mask_top_replace_mean(cs_mask_top_replace_mean(neg(cs_mask_top_replace_mean(pow_3(day_mean(Volume))))))`
