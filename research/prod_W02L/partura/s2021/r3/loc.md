# 定位:种子 2021,P 组,第 3 轮(只含 train / valid)

快照:prods2021M1_I0_open_search, prods2021M2_I0_open_search, prods2021M3_I0_open_search, prods2021Pr1a_Ea, prods2021Pr1b_Nb, prods2021Pr2a_Na, prods2021Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.20 | -1.54 | -2.20 | +1 | 5 | prods2021M1_I0_open_search | `add(div(pow_1_5(day_argmin(Amt)), day_max(High)), cross_max(day_cov(Close, Close), 15))` |
| -2.22 | -2.05 | -2.22 | +1 | 20 | prods2021M1_I0_open_search | `cs_bucket_demean(ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 5), cross_mean(day_sum(Amt), 60))` |
| -2.50 | -2.50 | -2.14 | +1 | 5 | prods2021M1_I0_open_search | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20), 5)` |

## 共性:158 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.75 | 0.001 | 4 | -0.30 / -2.06 | `sub(day_max(High), LogFloatShares)` |
| +1.07 | 0.008 | 7 | -1.00 / -2.06 | `signedpower(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 2)` |
| +1.06 | 0.009 | 5 | -0.99 / -2.05 | `cs_mask_top_replace_mean(cs_last_high05(BoardCode, day_open(Volume)))` |
| +0.99 | 0.001 | 13 | -1.10 / -2.10 | `cs_last_high05(BoardCode, day_open(Volume))` |
| +0.93 | 0.028 | 6 | -1.12 / -2.05 | `log(day_max(High))` |
| +0.88 | 0.007 | 9 | -1.19 / -2.06 | `ts_delay(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 1)` |
| +0.80 | 0.002 | 15 | -1.29 / -2.09 | `day_open(Volume)` |
| +0.75 | 0.001 | 30 | -1.41 / -2.16 | `day_at_max_ratio(Close)` |
| +0.70 | 0.003 | 26 | -1.43 / -2.13 | `sub(day_at_max_ratio(Close), day_at_min_ratio(Close))` |
| +0.64 | 0.004 | 31 | -1.50 / -2.14 | `day_at_min_ratio(Close)` |
| +0.50 | 0.133 | 5 | -1.53 / -2.03 | `cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret))))` |
| +0.49 | 0.120 | 6 | -1.54 / -2.03 | `neg(abs_(day_pos_ratio(Ret)))` |
| +0.33 | 0.080 | 14 | -1.71 / -2.04 | `day_std(Close)` |
| +0.31 | 0.104 | 12 | -1.73 / -2.04 | `abs_(day_std(Close))` |
| +0.24 | 0.266 | 33 | -1.83 / -2.06 | `day_max(High)` |
| +0.23 | 0.476 | 4 | -1.79 / -2.02 | `sub(LogFloatCap, LogFloatShares)` |
| +0.22 | 0.218 | 10 | -1.80 / -2.03 | `abs_(day_pos_ratio(Ret))` |
| +0.16 | 0.289 | 25 | -1.88 / -2.04 | `day_pos_ratio(Ret)` |
| +0.12 | 0.574 | 8 | -1.90 / -2.02 | `day_pos_ratio(neg(Ret))` |
| +0.09 | 0.540 | 5 | -1.93 / -2.02 | `ts_med(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)` |

## 拆解(11 次评估)

### head score -2.22:`cs_bucket_demean(ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 5), cross_mean(day_sum(Amt), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 5)` | -2.83 | -2.83 | -2.62 | — | (子树本身) |
| sufficiency | `ts_var(pow_1_5(day_argmin(Amt)), 60)` | -2.80 | -2.80 | -2.75 | — | (子树本身) |
| sufficiency | `pow_1_5(day_argmin(Amt))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_mean(day_sum(Amt), 60)` | -1.46 | -1.46 | -0.86 | — | (子树本身) |
| knockout | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 5)` | -1.79 | -1.79 | -0.19 | -0.43 | `cs_bucket_demean(ts_var(pow_1_5(day_argmin(Amt)), 60), cross_mean(day_sum(Amt), 60))` |
| knockout | `ts_var(pow_1_5(day_argmin(Amt)), 60)` | — | — | — | — | `cs_bucket_demean(ts_quantile_q75(pow_1_5(day_argmin(Amt)), 5), cross_mean(day_sum(Amt), 60))` |
| knockout | `pow_1_5(day_argmin(Amt))` | -1.60 | -1.60 | +0.05 | -0.62 | `cs_bucket_demean(ts_quantile_q75(ts_var(day_argmin(Amt), 60), 5), cross_mean(day_sum(Amt), 60))` |
| knockout | `cross_mean(day_sum(Amt), 60)` | -2.26 | -2.26 | -1.71 | +0.04 | `cs_bucket_demean(ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 5), day_sum(Amt))` |
| swap | `Amt->Volume` | -2.70 | -2.70 | -1.32 | — | `cs_bucket_demean(ts_quantile_q75(ts_var(pow_1_5(day_argmin(Volume)), 60), 5), cross_mean(day_sum(Volume), 60))` |
| window | `ts_quantile_q75@5->2` | -1.91 | -1.91 | -0.22 | — | `cs_bucket_demean(ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 2), cross_mean(day_sum(Amt), 60))` |
| window | `ts_quantile_q75@5->10` | -2.11 | -2.11 | -0.05 | — | `cs_bucket_demean(ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 60), 10), cross_mean(day_sum(Amt), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_max(High), LogFloatShares)` — enrichment,均值差 +1.75,p 0.001
2. `signedpower(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 2)` — enrichment,均值差 +1.07,p 0.008
3. `cs_mask_top_replace_mean(cs_last_high05(BoardCode, day_open(Volume)))` — enrichment,均值差 +1.06,p 0.009
4. `cs_last_high05(BoardCode, day_open(Volume))` — enrichment,均值差 +0.99,p 0.001
5. `log(day_max(High))` — enrichment,均值差 +0.93,p 0.028
6. `ts_delay(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 1)` — enrichment,均值差 +0.88,p 0.007
7. `day_open(Volume)` — enrichment,均值差 +0.80,p 0.002
8. `day_at_max_ratio(Close)` — enrichment,均值差 +0.75,p 0.001
9. `sub(day_at_max_ratio(Close), day_at_min_ratio(Close))` — enrichment,均值差 +0.70,p 0.003
10. `day_at_min_ratio(Close)` — enrichment,均值差 +0.64,p 0.004
11. `day_std(Close)` — enrichment,均值差 +0.33,p 0.080

## 本组之前各轮的任务

- `prods2021Pr1a_Ea`:核心 `day_max(High)`;评分 86,过线 0,入 heads 0;采样计数 {'c05_no_core': 1741, 'c05_skeleton': 873}
  - score -0.22(train -0.05 valid -0.22):`div(log(LogFloatShares), sub(day_max(High), LogFloatShares))`
  - score -0.27(train -0.05 valid -0.27):`div(log(day_max(High)), sub(day_max(High), LogFloatShares))`
  - score -0.30(train -0.12 valid -0.30):`div(day_max(High), sub(day_max(High), LogFloatShares))`
  - score -0.42(train -0.26 valid -0.42):`div(log(day_max(High)), sub(LogFloatCap, cross_ema(day_max(High), 5)))`
  - score -0.42(train -0.36 valid -0.42):`div(log(day_autocorr_n1(High)), sub(day_max(High), LogFloatShares))`
- `prods2021Pr1b_Nb`:核心 `—`;评分 74,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -1.26(train -1.26 valid -1.24):`sub(ts_med(sub(div(day_first(Open), cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret))))), 1), 40), cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret)))))`
  - score -1.52(train -1.44 valid -1.52):`cs_bucket_zscore(abs_(day_std(Close)), pow_3(abs_(day_pos_ratio(Ret))))`
  - score -1.53(train -1.44 valid -1.53):`cs_bucket_zscore(abs_(day_std(Close)), pow_05(abs_(day_pos_ratio(Ret))))`
  - score -1.53(train -1.44 valid -1.53):`cs_bucket_zscore(abs_(day_std(Close)), day_pos_ratio(Ret))`
  - score -1.53(train -1.44 valid -1.53):`cs_bucket_zscore(abs_(day_std(Close)), pow_3(day_pos_ratio(Ret)))`
- `prods2021Pr2a_Na`:核心 `—`;评分 73,过线 0,入 heads 0;采样计数 {}
  - score -0.10(train -0.10 valid +0.33):`cross_ema(signedpower(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 2), 60)`
  - score -0.11(train +0.15 valid -0.11):`cross_ema(mul(ts_delay(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 60)`
  - score -0.19(train -0.19 valid +0.04):`cross_ema(signedpower(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 2), 15)`
  - score -0.21(train -0.21 valid +0.23):`cross_ema(signedpower(ts_delay(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 1), 2), 60)`
  - score -0.26(train -0.26 valid -0.12):`cross_ema(sub(day_at_max_ratio(Close), day_at_min_ratio(Close)), 30)`
- `prods2021Pr2b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.52(train +0.13 valid -0.52):`pow_1_5(pow_1_5(cs_mask_top_replace_mean(cs_last_high05(pow_1_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(cs_first_high20(cs_last_high05(BoardCode, day_open(Volume)), day_open(Volume))))), day_open(Volume)))))`
  - score -0.60(train +0.07 valid -0.60):`pow_1_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(cs_first_high20(cs_last_high05(BoardCode, day_open(Volume)), day_open(Volume)))))`
  - score -0.88(train -0.88 valid -0.50):`cs_mask_top_replace_mean(cs_last_high05(cs_last_high05(BoardCode, cs_mask_top_replace_mean(cs_last_high05(BoardCode, day_open(Volume)))), cs_mask_top_replace_mean(cs_last_high05(BoardCode, day_open(Volume)))))`
  - score -0.91(train -0.91 valid -0.64):`pow_1_5(cs_mask_top_replace_mean(cs_last_high05(cs_last_high05(BoardCode, day_open(Volume)), day_open(Volume))))`
  - score -0.92(train -0.92 valid -0.69):`pow_1_5(cs_mask_top_replace_mean(cs_last_high05(BoardCode, day_open(Volume))))`

## 比原 head 好的拆解变体(R 候选)

(没有)
