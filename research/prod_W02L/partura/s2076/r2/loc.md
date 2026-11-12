# 定位:种子 2076,P 组,第 2 轮(只含 train / valid)

快照:prods2076M1_I0_open_search, prods2076M2_I0_open_search, prods2076Pr1a_Ea, prods2076Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.66 | +0.67 | +0.66 | +1 | 0 | prods2076Pr1b_Nb | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))` |
| -0.25 | -0.25 | +0.07 | +1 | 0 | prods2076M1_I0_open_search | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` |
| -0.65 | -0.65 | +0.20 | +1 | 0 | prods2076M1_I0_open_search | `cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(Low)), 15))` |
| -1.12 | -0.87 | -1.12 | -1 | 20 | prods2076M2_I0_open_search | `day_first(in_max_rolling(in_delta(Volume, 60), 30))` |
| -1.21 | -1.21 | -0.63 | +1 | 20 | prods2076M1_I0_open_search | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 20)` |
| -1.30 | -1.30 | -0.82 | +1 | 20 | prods2076M2_I0_open_search | `day_first(in_first(Amt))` |
| -1.31 | -0.69 | -1.31 | +1 | 20 | prods2076M2_I0_open_search | `day_close(cross_autocorr_s1(pow_2_5(nt_ts_scale(Ret, 5)), 241))` |

## 共性:169 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.61 | 0.000 | 10 | -0.17 / -2.78 | `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)` |
| +2.60 | 0.000 | 6 | -0.11 / -2.72 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` |
| +2.31 | 0.000 | 21 | -0.60 / -2.91 | `day_zero_ratio(Amt)` |
| +1.96 | 0.000 | 17 | -0.86 / -2.82 | `sqrt(day_skew(Open))` |
| +1.72 | 0.000 | 22 | -1.13 / -2.85 | `day_skew(Open)` |
| +1.00 | 0.013 | 6 | -1.66 / -2.66 | `day_topw_mean(Open, High)` |
| +0.93 | 0.043 | 4 | -1.71 / -2.65 | `day_signed_ratio(Open, Close)` |
| +0.93 | 0.043 | 4 | -1.71 / -2.65 | `cross_flat_ratio(day_signed_ratio(Open, Close), 10)` |
| +0.68 | 0.118 | 4 | -1.95 / -2.64 | `ts_cov(day_zero_ratio(Amt), day_min(Close), 10)` |
| +0.62 | 0.115 | 5 | -2.02 / -2.64 | `day_min(Close)` |
| +0.13 | 0.405 | 9 | -2.50 / -2.63 | `day_std(Low)` |
| +0.07 | 0.473 | 4 | -2.55 / -2.62 | `day_max(High)` |
| +0.07 | 0.477 | 4 | -2.55 / -2.62 | `day_first(Open)` |
| -0.04 | 0.573 | 6 | -2.67 / -2.62 | `day_cov(Low, Ret)` |
| -0.05 | 0.602 | 4 | -2.67 / -2.62 | `ts_max(day_var(pow_2_5(pow_2_5(Ret))), 30)` |
| -0.18 | 0.684 | 5 | -2.80 / -2.62 | `mul(day_autocorr_n1(High), day_std(Low))` |
| -0.18 | 0.684 | 5 | -2.80 / -2.62 | `day_autocorr_n1(High)` |
| -0.33 | 0.778 | 14 | -2.92 / -2.60 | `day_var(pow_2_5(pow_2_5(Ret)))` |
| -0.89 | 0.868 | 5 | -3.49 / -2.60 | `day_es_ratio_lo(Close)` |
| -1.42 | 0.921 | 4 | -4.01 / -2.59 | `day_corr(Ret, in_delay(Amt, 1))` |

## 拆解(17 次评估)

### head score +0.66:`sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` | +0.67 | +0.68 | +0.67 | — | (子树本身) |
| sufficiency | `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)` | +0.34 | +0.45 | +0.34 | — | (子树本身) |
| sufficiency | `sqrt(day_skew(Open))` | -3.08 | -3.08 | -3.08 | — | (子树本身) |
| sufficiency | `day_zero_ratio(Amt)` | — | — | — | — | 门槛废品 |
| knockout | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` | +0.35 | +0.46 | +0.35 | +0.31 | `sigmoid(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10))` |
| knockout | `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)` | — | — | — | — | `sigmoid(cross_mean(day_zero_ratio(Amt), 30))` |
| knockout | `sqrt(day_skew(Open))` | -0.21 | -0.21 | -0.12 | +0.87 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), day_skew(Open), 10), 30))` |
| swap | `Amt->Volume` | +0.60 | +0.60 | +0.61 | — | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Volume), sqrt(day_skew(Open)), 10), 30))` |
| swap | `Open->Close` | +0.50 | +0.54 | +0.50 | — | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Close)), 10), 30))` |
| window | `cross_mean@30->15` | +0.44 | +0.44 | +1.06 | — | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 15))` |
| window | `cross_mean@30->60` | +0.42 | +0.81 | +0.42 | — | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 60))` |

### head score -1.12:`day_first(in_max_rolling(in_delta(Volume, 60), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -1.33 | -1.33 | -0.91 | — | `day_first(in_max_rolling(in_delta(Amt, 60), 30))` |
| window | `in_max_rolling@30->15` | — | — | — | — | `day_first(in_max_rolling(in_delta(Volume, 60), 15))` |
| window | `in_max_rolling@30->60` | — | — | — | — | `day_first(in_max_rolling(in_delta(Volume, 60), 60))` |

### head score -1.30:`day_first(in_first(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | — | — | — | — | `day_first(in_first(Volume))` |

### head score -1.31:`day_close(cross_autocorr_s1(pow_2_5(nt_ts_scale(Ret, 5)), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| window | `cross_autocorr_s1@241->120` | -0.78 | -0.41 | -0.78 | — | `day_close(cross_autocorr_s1(pow_2_5(nt_ts_scale(Ret, 5)), 120))` |
| window | `cross_autocorr_s1@241->482` | -1.03 | -0.74 | -1.03 | — | `day_close(cross_autocorr_s1(pow_2_5(nt_ts_scale(Ret, 5)), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` — ablation,自身 score +0.67(所在 head +0.66)
2. `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)` — enrichment,均值差 +2.61,p 0.000
3. `day_zero_ratio(Amt)` — enrichment,均值差 +2.31,p 0.000
4. `sqrt(day_skew(Open))` — enrichment,均值差 +1.96,p 0.000
5. `day_skew(Open)` — enrichment,均值差 +1.72,p 0.000
6. `day_topw_mean(Open, High)` — enrichment,均值差 +1.00,p 0.013
7. `day_signed_ratio(Open, Close)` — enrichment,均值差 +0.93,p 0.043
8. `cross_flat_ratio(day_signed_ratio(Open, Close), 10)` — enrichment,均值差 +0.93,p 0.043

## 本组之前各轮的任务

- `prods2076Pr1a_Ea`:核心 `day_var(pow_2_5(pow_2_5(Ret)))`;评分 81,过线 0,入 heads 0;采样计数 {'c05_no_core': 2939, 'c05_skeleton': 1539, 'c05_periphery_seen': 4}
  - score -1.81(train -1.81 valid -0.02):`div(ts_delta(ts_autocorr_s1(day_var(pow_2_5(pow_2_5(Ret))), 30), 5), -2)`
  - score -2.34(train -2.34 valid -0.31):`div(ts_delta(ts_std(day_var(pow_2_5(pow_2_5(Ret))), 30), 5), -2)`
  - score -2.39(train -2.39 valid -0.60):`div(ts_delta(ts_autocorr_s1(day_var(pow_2_5(pow_2_5(Ret))), 10), 5), -2)`
  - score -2.45(train -2.45 valid -2.21):`add(ts_decay_linear(ts_max(day_var(pow_2_5(pow_2_5(Ret))), 30), 20), cs_last_high05(day_q_stat_std(Volume), day_min(Amt)))`
  - score -2.75(train -2.75 valid -2.59):`add(ts_decay_linear(ts_max(day_var(pow_2_5(pow_2_5(Ret))), 30), 20), day_es_ratio_lo(Close))`
- `prods2076Pr1b_Nb`:核心 `—`;评分 90,过线 3,入 heads 1;采样计数 {'c05_skeleton': 14}
  - score +0.66(train +0.67 valid +0.66):`sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))`
  - score +0.64(train +0.64 valid +0.67):`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)`
  - score +0.63(train +0.63 valid +0.67):`sigmoid(sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)))`
  - score +0.33(train +0.46 valid +0.33):`ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)`
  - score +0.13(train +0.64 valid +0.13):`sigmoid(cross_mean(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 30))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.53(window cross_autocorr_s1@241->120):`day_close(cross_autocorr_s1(pow_2_5(nt_ts_scale(Ret, 5)), 120))`
