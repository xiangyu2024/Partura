# 定位:种子 2058,P 组,第 3 轮(只含 train / valid)

快照:prods2058M1_I0_open_search, prods2058M2_I0_open_search, prods2058M3_I0_open_search, prods2058Pr1a_Ea, prods2058Pr1b_Nb, prods2058Pr2a_Ea, prods2058Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.08 | -0.02 | -0.08 | +1 | 5 | prods2058M2_I0_open_search | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 20)` |
| -0.90 | -0.90 | -0.37 | +1 | 0 | prods2058M3_I0_open_search | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(Amt), 10)), 3), 241)` |
| -1.12 | -1.12 | -1.11 | -1 | 5 | prods2058M1_I0_open_search | `day_std(pow_2(Volume))` |
| -1.12 | -0.95 | -1.12 | -1 | 5 | prods2058M2_I0_open_search | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)))` |
| -1.55 | -1.44 | -1.55 | -1 | 0 | prods2058M1_I0_open_search | `cross_mean(day_std(pow_2(Ret)), 20)` |
| -1.64 | -1.64 | -0.30 | -1 | 20 | prods2058M2_I0_open_search | `day_sum(sigmoid(Vwap))` |
| -1.98 | -1.98 | -1.90 | +1 | 20 | prods2058M3_I0_open_search | `ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 50)` |
| -2.61 | -2.42 | -2.61 | -1 | 5 | prods2058M1_I0_open_search | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)` |
| -2.66 | -1.66 | -2.66 | -1 | 20 | prods2058M3_I0_open_search | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))` |

## 共性:194 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.68 | 0.000 | 9 | -0.46 / -2.14 | `cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap)` |
| +0.92 | 0.000 | 57 | -1.42 / -2.33 | `day_quantile(cross_regbeta(Open, Amt, 241))` |
| +0.63 | 0.064 | 4 | -1.44 / -2.08 | `cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5)` |
| +0.10 | 0.545 | 4 | -1.97 / -2.07 | `cs_demean(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth))` |
| -0.11 | 0.586 | 16 | -2.17 / -2.05 | `div(day_last(Close), ts_delay(day_last(Close), 1))` |
| -0.22 | 0.629 | 4 | -2.28 / -2.06 | `cross_ema(day_std(pow_2(Ret)), 120)` |
| -0.34 | 0.784 | 4 | -2.40 / -2.06 | `day_quantile_q25(Amt)` |
| -0.39 | 0.954 | 37 | -2.38 / -1.99 | `day_last(Close)` |
| -0.40 | 0.959 | 30 | -2.40 / -2.00 | `ts_delay(day_last(Close), 1)` |
| -0.50 | 0.963 | 17 | -2.52 / -2.02 | `day_open(Open)` |
| -0.52 | 0.858 | 7 | -2.56 / -2.05 | `div(day_last(Close), day_open(Open))` |
| -0.63 | 1.000 | 34 | -2.58 / -1.95 | `day_std(pow_2(Ret))` |
| -0.71 | 0.989 | 10 | -2.74 / -2.03 | `div(day_open(Open), ts_delay(day_last(Close), 1))` |

## 拆解(21 次评估)

### head score -0.90:`cross_fangzheng(cross_max(day_product(cross_product(sigmoid(Amt), 10)), 3), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(day_product(cross_product(sigmoid(Amt), 10)), 3)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_product(cross_product(sigmoid(Amt), 10))` | — | — | — | — | 门槛废品 |
| knockout | `cross_max(day_product(cross_product(sigmoid(Amt), 10)), 3)` | -0.94 | -0.94 | -0.34 | +0.03 | `cross_fangzheng(day_product(cross_product(sigmoid(Amt), 10)), 241)` |
| swap | `Amt->Volume` | -0.90 | -0.90 | -0.34 | — | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(Volume), 10)), 3), 241)` |
| window | `cross_fangzheng@241->120` | -0.92 | -0.92 | -0.86 | — | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(Amt), 10)), 3), 120)` |
| window | `cross_fangzheng@241->482` | -0.87 | -0.87 | -0.39 | — | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(Amt), 10)), 3), 482)` |

### head score -1.98:`ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_product(pow_2(cross_product(sigmoid(Amt), 10)))` | — | — | — | — | 门槛废品 |
| swap | `Amt->Volume` | -1.99 | -1.99 | -1.87 | — | `ts_std(day_product(pow_2(cross_product(sigmoid(Volume), 10))), 50)` |
| window | `ts_std@50->25` | -3.11 | -2.45 | -3.11 | — | `ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 25)` |
| window | `ts_std@50->100` | -1.15 | -1.01 | -1.15 | — | `ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 100)` |

### head score -2.66:`mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10)` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_stddev_full(day_product(cross_product(sigmoid(Low), 15)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_product(cross_product(sigmoid(Low), 15))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open)))` | -2.62 | -1.66 | -2.62 | — | (子树本身) |
| knockout | `ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10)` | -2.62 | -1.66 | -2.62 | -0.04 | `mul(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))` |
| knockout | `cs_stddev_full(day_product(cross_product(sigmoid(Low), 15)))` | -2.62 | -1.67 | -2.62 | -0.04 | `mul(ts_max(day_product(cross_product(sigmoid(Low), 15)), 10), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))` |
| knockout | `cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open)))` | -2.45 | -1.64 | -2.45 | -0.21 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10), cs_mask_top_replace_mean(day_quantile(Open)))` |
| swap | `Low->High` | -2.62 | -1.66 | -2.62 | — | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(High), 15))), 10), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))` |
| swap | `Open->Close` | -2.63 | -1.66 | -2.63 | — | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Close))))` |
| window | `ts_max@10->5` | -2.62 | -1.67 | -2.62 | — | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 5), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))` |
| window | `ts_max@10->20` | -2.61 | -1.66 | -2.61 | — | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 20), cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open))))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap)` — enrichment,均值差 +1.68,p 0.000
2. `day_quantile(cross_regbeta(Open, Amt, 241))` — enrichment,均值差 +0.92,p 0.000
3. `cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5)` — enrichment,均值差 +0.63,p 0.064

## 本组之前各轮的任务

- `prods2058Pr1a_Ea`:核心 `day_std(pow_2(Ret))`;评分 103,过线 0,入 heads 0;采样计数 {'c05_no_core': 2358, 'c05_skeleton': 1293}
  - score -1.17(train -1.16 valid -1.17):`cs_last_high40(day_std(pow_2(Ret)), day_quantile(cross_regbeta(Open, Amt, 30)))`
  - score -1.39(train -1.39 valid -0.63):`cs_last_high40(day_std(pow_2(Ret)), day_quantile(cross_regbeta(cross_regbeta(Open, Amt, 241), Amt, 60)))`
  - score -1.39(train -1.26 valid -1.39):`sub(cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5), cross_ema(day_std(pow_2(Ret)), 120))`
  - score -1.39(train -1.26 valid -1.39):`sub(cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5), cross_ema(day_std(pow_2(Ret)), 30))`
  - score -1.39(train -1.26 valid -1.39):`sub(cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5), day_std(pow_2(Ret)))`
- `prods2058Pr1b_Nb`:核心 `—`;评分 78,过线 0,入 heads 0;采样计数 {'c05_skeleton': 12}
  - score -0.20(train -0.20 valid +0.26):`cs_regres(ListAge, LogTotalCap)`
  - score -0.20(train -0.20 valid +0.26):`cs_regres(cs_regres(ListAge, LogTotalCap), LogTotalCap)`
  - score -0.23(train -0.23 valid +0.07):`cs_regres(day_pos_ratio(Amt), LogTotalCap)`
  - score -0.31(train -0.31 valid +0.00):`cs_regres(ListAge, day_last(Volume))`
  - score -0.37(train +0.32 valid -0.37):`cross_max(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 60)`
- `prods2058Pr2a_Ea`:核心 `day_quantile(cross_regbeta(Open, Amt, 241))`;评分 83,过线 0,入 heads 0;采样计数 {'c05_no_core': 1044, 'c05_skeleton': 476, 'mutation_refused': 5, 'c05_periphery_seen': 6}
  - score +0.16(train +0.49 valid +0.16):`div(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), day_quantile(cross_reg_fvalue(Amt, Amt, 241)))`
  - score +0.04(train +0.32 valid +0.04):`div(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), day_quantile(cross_regalpha(Open, Amt, 241)))`
  - score -0.33(train -0.27 valid -0.33):`div(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), day_quantile(cross_regbeta(Open, Amt, 241)))`
  - score -0.55(train -0.55 valid -0.44):`div(cs_bucket_zscore(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), LogFloatCap), day_quantile(cross_reg_fvalue(Open, Amt, 241)))`
  - score -0.55(train -0.55 valid -0.44):`div(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), day_quantile(cross_reg_fvalue(Open, Amt, 241)))`
- `prods2058Pr2b_Nb`:核心 `—`;评分 81,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.75(train -0.72 valid -0.75):`ts_scale(day_quantile_q25(in_scale_rolling(cross_corr(Amt, Low, 60), 5)), 40)`
  - score -0.92(train -0.79 valid -0.92):`sub(cross_mean(sub(div(day_open(Amt), ts_delay(day_last(cross_reg_tvalue(Volume, High, 60)), 1)), 0.5), 60), cross_mean(sub(div(day_last(Close), day_open(Open)), 1), 60))`
  - score -1.05(train -1.05 valid -0.13):`day_es_ratio_hi(cross_reg_tvalue(Open, cross_cov(Amt, Low, 60), 60))`
  - score -1.07(train -0.51 valid -1.07):`day_es_ratio_hi(cross_reg_tvalue(Volume, Amt, 60))`
  - score -1.15(train -0.70 valid -1.15):`day_quantile_q75(cross_reg_tvalue(Low, cross_cov(Amt, Low, 60), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(knockout cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_quantile(Open)))):`mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(Low), 15))), 10), cs_mask_top_replace_mean(day_quantile(Open)))`
