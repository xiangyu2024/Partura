# 定位:种子 2058,P 组,第 2 轮(只含 train / valid)

快照:prods2058M1_I0_open_search, prods2058M2_I0_open_search, prods2058Pr1a_Ea, prods2058Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.08 | -0.02 | -0.08 | +1 | 5 | prods2058M2_I0_open_search | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 20)` |
| -1.12 | -1.12 | -1.11 | -1 | 5 | prods2058M1_I0_open_search | `day_std(pow_2(Volume))` |
| -1.12 | -0.95 | -1.12 | -1 | 5 | prods2058M2_I0_open_search | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)))` |
| -1.55 | -1.44 | -1.55 | -1 | 0 | prods2058M1_I0_open_search | `cross_mean(day_std(pow_2(Ret)), 20)` |
| -1.64 | -1.64 | -0.30 | -1 | 20 | prods2058M2_I0_open_search | `day_sum(sigmoid(Vwap))` |
| -2.61 | -2.42 | -2.61 | -1 | 5 | prods2058M1_I0_open_search | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)` |

## 共性:91 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.89 | 0.025 | 4 | -1.44 / -2.34 | `day_quantile(cross_regbeta(Open, Amt, 241))` |
| +0.89 | 0.025 | 4 | -1.44 / -2.34 | `cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5)` |
| +0.34 | 0.284 | 4 | -1.97 / -2.31 | `cs_demean(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth))` |
| +0.16 | 0.257 | 16 | -2.17 / -2.32 | `div(day_last(Close), ts_delay(day_last(Close), 1))` |
| +0.13 | 0.213 | 21 | -2.20 / -2.33 | `day_last(Close)` |
| +0.08 | 0.275 | 20 | -2.23 / -2.31 | `ts_delay(day_last(Close), 1)` |
| +0.02 | 0.397 | 4 | -2.28 / -2.30 | `cross_ema(day_std(pow_2(Ret)), 120)` |
| -0.45 | 0.979 | 34 | -2.58 / -2.13 | `day_std(pow_2(Ret))` |

## 拆解(25 次评估)

### head score -0.08:`ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20)` | -0.91 | -0.91 | -0.27 | — | (子树本身) |
| sufficiency | `log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10))` | -0.94 | -0.94 | -0.84 | — | (子树本身) |
| sufficiency | `cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)` | -4.25 | -2.76 | -4.25 | — | (子树本身) |
| sufficiency | `day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open)))))` | -3.05 | -3.05 | -2.72 | — | (子树本身) |
| knockout | `log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10))` | -0.25 | +0.00 | -0.25 | +0.17 | `ts_max(ts_max(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10), 20), 20)` |
| knockout | `cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)` | -3.35 | -2.72 | -3.35 | +3.27 | `ts_max(ts_max(log(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open)))))), 20), 20)` |
| swap | `Vwap->Close` | -0.17 | -0.08 | -0.17 | — | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Close, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 20)` |
| swap | `High->Low` | +0.00 | +0.05 | +0.00 | — | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(Low, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 20)` |
| window | `ts_max@20->10` | -0.65 | -0.51 | -0.65 | — | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 10)` |
| window | `ts_max@20->40` | +0.20 | +0.42 | +0.20 | — | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(div(Vwap, nt_ts_quantile_q75(in_quantile_q75(High, 30), 60)), 30), nt_cs_mask_top_replace_mean_neg(nt_cs_stddev_full(div(sigmoid(Ret), pow_3(Open))))), day_open(Amt), 10)), 20), 40)` |

### head score -1.12:`pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5))` | -1.06 | -0.95 | -1.06 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)` | — | — | — | — | 门槛废品 |
| sufficiency | `pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30)))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))` | — | — | — | — | 门槛废品 |
| knockout | `cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5))` | — | — | — | — | `pow_2(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5))` |
| knockout | `ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)` | -1.01 | -0.93 | -1.01 | -0.11 | `pow_2(cs_rank(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30)))))` |
| knockout | `pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30)))` | -1.06 | -0.96 | -1.06 | -0.06 | `pow_2(cs_rank(ts_decay_linear(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30)), 5)))` |
| swap | `High->Low` | -0.97 | -0.97 | -0.91 | — | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(Low), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)))` |
| swap | `Close->Vwap` | -1.04 | -0.99 | -1.04 | — | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Vwap, 60), 5), 30))), 5)))` |
| window | `ts_decay_linear@5->2` | -0.94 | -0.94 | -0.93 | — | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 2)))` |
| window | `ts_decay_linear@5->10` | -0.96 | -0.93 | -0.96 | — | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 10)))` |

### head score -1.55:`cross_mean(day_std(pow_2(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(pow_2(Ret))` | -2.87 | -2.78 | -2.87 | — | (子树本身) |
| window | `cross_mean@20->10` | -2.15 | -1.78 | -2.15 | — | `cross_mean(day_std(pow_2(Ret)), 10)` |
| window | `cross_mean@20->40` | -1.84 | -1.84 | -1.70 | — | `cross_mean(day_std(pow_2(Ret)), 40)` |

### head score -1.64:`day_sum(sigmoid(Vwap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | — | — | — | — | `day_sum(sigmoid(Close))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_quantile(cross_regbeta(Open, Amt, 241))` — enrichment,均值差 +0.89,p 0.025
2. `cross_ema(day_quantile(cross_regbeta(Open, Amt, 241)), 5)` — enrichment,均值差 +0.89,p 0.025

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window ts_decay_linear@5->2):`pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 2)))`
- 增益 +0.15(window ts_decay_linear@5->10):`pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 10)))`
- 增益 +0.15(swap High->Low):`pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(Low), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)))`
- 增益 +0.11(knockout ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30))), 5)):`pow_2(cs_rank(pow_2(day_autocorr_n1(nt_ts_corr(in_quantile_q75(sigmoid(High), 10), in_rank_rolling(nt_ts_var(Close, 60), 5), 30)))))`
