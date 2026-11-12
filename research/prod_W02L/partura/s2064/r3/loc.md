# 定位:种子 2064,P 组,第 3 轮(只含 train / valid)

快照:prods2064M1_I0_open_search, prods2064M2_I0_open_search, prods2064M3_I0_open_search, prods2064Pr1a_Ea, prods2064Pr1b_Nb, prods2064Pr2a_Ea, prods2064Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.35 | -0.35 | -0.18 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 25)` |
| -0.50 | -0.28 | -0.50 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)), 50)` |
| -0.63 | -0.63 | +0.25 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 241)), 50)` |
| -0.98 | -0.53 | -0.98 | +1 | 20 | prods2064M3_I0_open_search | `ts_stddev(day_std(nt_ts_skew(nt_ts_mean(Close, 15), 5)), 10)` |
| -1.22 | -1.22 | +0.03 | -1 | 5 | prods2064M2_I0_open_search | `neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 241))` |
| -1.45 | -0.88 | -1.45 | +1 | 20 | prods2064M3_I0_open_search | `sqrt(day_std(nt_ts_skew(nt_ts_mean(Close, 10), 5)))` |
| -1.48 | -1.36 | -1.48 | -1 | 20 | prods2064M3_I0_open_search | `ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))), 10)` |
| -1.73 | -1.73 | -1.55 | -1 | 0 | prods2064M2_I0_open_search | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 241))` |
| -2.05 | -2.00 | -2.05 | -1 | 20 | prods2064M2_I0_open_search | `day_durbin_watson(nt_ts_max(nt_ts_max(Vwap, 5), 5))` |

## 共性:224 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.54 | 0.001 | 5 | -0.25 / -1.79 | `ts_delay(day_last(High), 1)` |
| +1.45 | 0.005 | 4 | -0.33 / -1.78 | `div(day_max(High), ts_delay(day_last(High), 1))` |
| +1.43 | 0.001 | 6 | -0.36 / -1.79 | `day_last(High)` |
| +1.30 | 0.008 | 4 | -0.47 / -1.78 | `cs_bucket_demean(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), ts_delay(day_last(Close), 1))` |
| +1.07 | 0.014 | 5 | -0.71 / -1.78 | `cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap)` |
| +1.07 | 0.000 | 141 | -1.36 / -2.43 | `day_last(Close)` |
| +0.93 | 0.000 | 135 | -1.38 / -2.32 | `ts_delay(day_last(Close), 1)` |
| +0.92 | 0.043 | 4 | -0.85 / -1.77 | `cs_bucket_demean(cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap), LogFloatCap)` |
| +0.80 | 0.012 | 10 | -0.99 / -1.79 | `cs_bucket_demean(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap)` |
| +0.76 | 0.000 | 90 | -1.30 / -2.06 | `div(day_max(High), ts_delay(day_last(Close), 1))` |
| +0.76 | 0.000 | 94 | -1.31 / -2.07 | `day_max(High)` |
| +0.72 | 0.000 | 36 | -1.15 / -1.87 | `cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60)` |
| +0.69 | 0.000 | 60 | -1.25 / -1.94 | `div(day_last(Close), ts_delay(day_last(Close), 1))` |
| +0.66 | 0.001 | 40 | -1.21 / -1.87 | `day_at_max_ratio(Close)` |
| +0.60 | 0.009 | 30 | -1.23 / -1.84 | `cross_delay(day_at_max_ratio(Close), 1)` |
| +0.10 | 0.478 | 5 | -1.66 / -1.76 | `day_var(pow_2_5(neg(Ret)))` |
| +0.05 | 0.544 | 25 | -1.71 / -1.76 | `day_var(pow_2_5(Ret))` |
| -1.18 | 0.994 | 6 | -2.90 / -1.72 | `day_close(pow_2_5(Amt))` |

## 拆解(14 次评估)

### head score -0.98:`ts_stddev(day_std(nt_ts_skew(nt_ts_mean(Close, 15), 5)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(nt_ts_skew(nt_ts_mean(Close, 15), 5))` | -1.28 | -0.65 | -1.28 | — | (子树本身) |
| swap | `Close->Vwap` | -2.02 | -2.02 | -0.83 | — | `ts_stddev(day_std(nt_ts_skew(nt_ts_mean(Vwap, 15), 5)), 10)` |
| window | `ts_stddev@10->5` | -1.03 | -0.64 | -1.03 | — | `ts_stddev(day_std(nt_ts_skew(nt_ts_mean(Close, 15), 5)), 5)` |
| window | `ts_stddev@10->20` | -0.88 | -0.65 | -0.88 | — | `ts_stddev(day_std(nt_ts_skew(nt_ts_mean(Close, 15), 5)), 20)` |

### head score -1.45:`sqrt(day_std(nt_ts_skew(nt_ts_mean(Close, 10), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(nt_ts_skew(nt_ts_mean(Close, 10), 5))` | -1.42 | -0.88 | -1.42 | — | (子树本身) |
| swap | `Close->Vwap` | -1.01 | -0.95 | -1.01 | — | `sqrt(day_std(nt_ts_skew(nt_ts_mean(Vwap, 10), 5)))` |
| window | `nt_ts_skew@5->2` | -1.84 | -1.84 | -1.53 | — | `sqrt(day_std(nt_ts_skew(nt_ts_mean(Close, 10), 2)))` |
| window | `nt_ts_skew@5->10` | -2.88 | -2.66 | -2.88 | — | `sqrt(day_std(nt_ts_skew(nt_ts_mean(Close, 10), 10)))` |

### head score -1.48:`ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15))))` | -0.88 | -0.73 | -0.88 | — | (子树本身) |
| sufficiency | `day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))` | -0.88 | -0.73 | -0.88 | — | (子树本身) |
| knockout | `sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15))))` | -1.10 | -0.82 | -1.10 | -0.38 | `ts_stddev(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15))), 10)` |
| swap | `Close->Vwap` | -0.07 | +0.33 | -0.07 | — | `ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Vwap, 15)))), 10)` |
| window | `ts_stddev@10->5` | -1.53 | -1.36 | -1.53 | — | `ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))), 5)` |
| window | `ts_stddev@10->20` | -1.24 | -1.24 | -1.06 | — | `ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))), 20)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_delay(day_last(High), 1)` — enrichment,均值差 +1.54,p 0.001
2. `div(day_max(High), ts_delay(day_last(High), 1))` — enrichment,均值差 +1.45,p 0.005
3. `day_last(High)` — enrichment,均值差 +1.43,p 0.001
4. `cs_bucket_demean(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), ts_delay(day_last(Close), 1))` — enrichment,均值差 +1.30,p 0.008
5. `cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap)` — enrichment,均值差 +1.07,p 0.014
6. `day_last(Close)` — enrichment,均值差 +1.07,p 0.000
7. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +0.93,p 0.000
8. `cs_bucket_demean(cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap), LogFloatCap)` — enrichment,均值差 +0.92,p 0.043
9. `cs_bucket_demean(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap)` — enrichment,均值差 +0.80,p 0.012
10. `div(day_max(High), ts_delay(day_last(Close), 1))` — enrichment,均值差 +0.76,p 0.000
11. `day_max(High)` — enrichment,均值差 +0.76,p 0.000
12. `cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60)` — enrichment,均值差 +0.72,p 0.000
13. `div(day_last(Close), ts_delay(day_last(Close), 1))` — enrichment,均值差 +0.69,p 0.000
14. `day_at_max_ratio(Close)` — enrichment,均值差 +0.66,p 0.001
15. `cross_delay(day_at_max_ratio(Close), 1)` — enrichment,均值差 +0.60,p 0.009

## 本组之前各轮的任务

- `prods2064Pr1a_Ea`:核心 `day_var(pow_2_5(Ret))`;评分 65,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1028, 'c05_no_core': 2295, 'c05_periphery_seen': 8}
  - score -0.63(train -0.63 valid +0.20):`cross_autocorr(day_var(pow_2_5(Ret)), 120, 1)`
  - score -0.82(train -0.82 valid -0.41):`cross_corr(day_var(pow_2_5(Ret)), day_var(pow_2_5(neg(Ret))), 120)`
  - score -1.02(train -1.02 valid -0.32):`cross_corr(day_var(pow_2_5(Ret)), cross_delay(day_last(Close), 1), 120)`
  - score -1.52(train -1.47 valid -1.52):`cs_first_low20(cross_flat_ratio(day_es_ratio_lo(Open), 10), cross_tail_mean_q75(day_var(pow_2_5(Ret)), 10))`
  - score -1.56(train -1.56 valid +0.04):`div(cross_mean(day_var(pow_2_5(Ret)), 60), cross_mean(day_var(pow_2_5(neg(Ret))), 60))`
- `prods2064Pr1b_Nb`:核心 `—`;评分 60,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score +0.09(train +0.28 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(High), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth))), 120)`
  - score +0.09(train +0.28 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(High), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95)), LimitWidth))), 120)`
  - score +0.09(train +0.12 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Low), 1)), 1), LimitWidth))), 120)`
  - score +0.09(train +0.23 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth))), 120)`
  - score +0.08(train +0.43 valid +0.08):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(High), 1)), 1), LimitWidth))), 120)`
- `prods2064Pr2a_Ea`:核心 `div(day_max(High), ts_delay(day_last(Close), 1))`;评分 93,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 6, 'c05_skeleton': 642, 'c05_no_core': 1407, 'mutation_refused': 6}
  - score -0.10(train -0.01 valid -0.10):`cs_bucket_demean(cs_last_low05(cross_max(div(day_max(High), ts_delay(cs_bucket_demean(cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap), LogFloatCap), 1)), 60), LogFloatCap), LogFloatCap)`
  - score -0.16(train +0.02 valid -0.16):`cs_bucket_demean(cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap), LogFloatCap)`
  - score -0.27(train +0.33 valid -0.27):`div(cs_bucket_demean(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1))`
  - score -0.29(train -0.29 valid +0.20):`div(cs_bucket_demean(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap), ts_delay(day_last(Close), 1))`
  - score -0.30(train +0.44 valid -0.30):`div(cs_bucket_demean(cross_max(cs_bucket_demean(cs_last_low05(cross_max(div(day_max(High), ts_delay(day_last(Close), 1)), 60), LogFloatCap), LogFloatCap), 60), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1))`
- `prods2064Pr2b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score +0.27(train +0.28 valid +0.27):`cross_mean(mul(cross_delay(day_at_max_ratio(Close), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)), 120)`
  - score +0.26(train +0.26 valid +0.42):`cross_mean(mul(cross_delay(day_at_max_ratio(Close), 1), mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth)), 120)`
  - score +0.21(train +0.21 valid +0.26):`cross_mean(mul(cross_delay(day_at_max_ratio(Close), 1), sub(div(day_last(Close), ts_delay(day_last(Open), 1)), 1)), 120)`
  - score +0.20(train +0.20 valid +0.29):`cross_mean(mul(cross_delay(day_at_max_ratio(Close), 1), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_last(Close), ts_delay(day_last(Close), 1)))), 120)`
  - score +0.15(train +0.26 valid +0.15):`cross_mean(mul(cross_delay(day_at_max_ratio(Close), 1), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth)), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.38(knockout sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15))))):`ts_stddev(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15))), 10)`
- 增益 +0.24(window ts_stddev@10->20):`ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))), 20)`
- 增益 +0.10(window ts_stddev@10->20):`ts_stddev(day_std(nt_ts_skew(nt_ts_mean(Close, 15), 5)), 20)`
