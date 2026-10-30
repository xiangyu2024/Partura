# 定位:种子 802,C 组,第 3 轮(只含 train / valid)

快照:c05s802M1_I0_open_search, c05s802M2_I0_open_search, c05s802M3_I0_open_search, c06s802Cr1a_Ea, c06s802Cr1b_Nb, c06s802Cr2a_Ea, c06s802Cr2b_Nb;已生效的 R 替换 6 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(29 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.89 | +1.89 | +3.75 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))` |
| +1.62 | +1.62 | +2.34 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| +1.61 | +1.61 | +3.34 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))` |
| +1.49 | +1.49 | +2.83 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |
| +1.45 | +1.45 | +3.20 | -1 | 20 | c05s802M2_I0_open_search | `pow_2(pow_2_5(day_durbin_watson(High)))` |
| +1.40 | +1.40 | +2.50 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 60, 1))` |
| +1.39 | +1.39 | +2.42 | +1 | 5 | c05s802M1_I0_open_search | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))))))` |
| +1.36 | +1.36 | +2.42 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_signed_ratio(abs_(Ret), Volume), day_sum(Ret)), 60, 1))` |
| +1.34 | +1.34 | +3.26 | -1 | 20 | c05s802M3_I0_open_search | `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)` |
| +1.30 | +1.30 | +2.22 | +1 | 0 | c05s802M1_I0_open_search | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200)), 40))` |
| +1.29 | +1.29 | +1.56 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))` |
| +1.14 | +1.14 | +2.70 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40))` |
| +1.10 | +1.10 | +2.26 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30), ts_autocorr(day_signed_ratio(Ret, Open), 60, 1))` |
| +1.09 | +1.09 | +1.25 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))` |
| +1.07 | +1.07 | +2.01 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))` |
| +1.04 | +1.04 | +2.53 | +1 | 5 | c06s802Cr1b_Nb | `ts_decay_linear(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), 80)` |
| +1.03 | +1.03 | +2.76 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), day_gini(Volume))` |
| +0.93 | +0.93 | +1.68 | +1 | 5 | c05s802M1_I0_open_search | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))` |
| +0.90 | +0.90 | +1.81 | -1 | 5 | c05s802M3_I0_open_search | `cross_cov(day_max(Ret), day_cov(Ret, Ret), 30)` |
| +0.86 | +0.86 | +1.42 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))` |
| +0.85 | +0.85 | +3.04 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), day_q_stat_std(in_forward_valid_part(High)))` |
| +0.83 | +1.09 | +0.83 | -1 | 5 | c05s802M1_I0_open_search | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` |
| +0.80 | +0.80 | +2.56 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1), 60, 1))` |
| +0.79 | +1.27 | +0.79 | -1 | 5 | c06s802Cr1a_Ea | `sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))` |
| +0.76 | +0.76 | +2.70 | +1 | 20 | c06s802Cr2a_Ea | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), day_min(Ret)), 60, 1))` |
| +0.72 | +0.72 | +0.75 | -1 | 0 | c06s802Cr1a_Ea | `sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(sub(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)), day_durbin_watson(Volume), 50)), 60))` |
| +0.67 | +0.67 | +1.36 | -1 | 20 | c05s802M3_I0_open_search | `cross_cov(day_wmean(Ret, Ret), day_wmean(Ret, Ret), 5)` |
| +0.56 | +0.56 | +0.82 | +1 | 5 | c05s802M2_I0_open_search | `cross_quantile_q25(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), 241)` |
| +0.54 | +0.54 | +1.26 | +1 | 20 | c05s802M1_I0_open_search | `day_mean(neg(in_delta(Volume, 60)))` |

## 共性:513 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.04 | 0.001 | 4 | +1.28 / -0.76 | `day_sum(Vwap)` |
| +1.97 | 0.000 | 6 | +1.21 / -0.77 | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30)` |
| +1.61 | 0.000 | 17 | +0.82 / -0.80 | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)` |
| +1.26 | 0.000 | 12 | +0.48 / -0.77 | `inv(LogFloatShares)` |
| +1.24 | 0.006 | 6 | +0.48 / -0.76 | `ts_decay_linear(inv(LogFloatShares), 40)` |
| +1.24 | 0.022 | 4 | +0.48 / -0.75 | `ts_decay_linear(LogFloatShares, 40)` |
| +1.18 | 0.001 | 12 | +0.40 / -0.77 | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` |
| +1.17 | 0.001 | 10 | +0.41 / -0.77 | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` |
| +1.13 | 0.033 | 4 | +0.38 / -0.75 | `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` |
| +1.11 | 0.006 | 8 | +0.35 / -0.76 | `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` |
| +1.08 | 0.003 | 12 | +0.31 / -0.77 | `mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume))` |
| +1.06 | 0.030 | 5 | +0.31 / -0.75 | `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` |
| +1.03 | 0.000 | 32 | +0.22 / -0.81 | `cross_quantile_q25(LogFloatShares, 241)` |
| +0.99 | 0.012 | 10 | +0.22 / -0.76 | `ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1)` |
| +0.93 | 0.048 | 5 | +0.18 / -0.75 | `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` |
| +0.89 | 0.067 | 5 | +0.13 / -0.75 | `cross_decay_linear(LogFloatShares, 3)` |
| +0.88 | 0.016 | 10 | +0.12 / -0.76 | `sqrt(day_quantile_q25(Open))` |
| +0.85 | 0.001 | 23 | +0.07 / -0.78 | `day_signed_ratio(abs_(Ret), Volume)` |
| +0.82 | 0.051 | 7 | +0.07 / -0.75 | `ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)` |
| +0.82 | 0.105 | 4 | +0.07 / -0.75 | `pow_2_5(cross_decay_linear(LogFloatShares, 3))` |

## 拆解(44 次评估)

### head score +1.89:`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)` | +0.62 | +0.62 | +2.63 | — | (子树本身) |
| sufficiency | `ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1)` | -0.18 | -0.18 | +0.48 | — | (子树本身) |
| sufficiency | `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` | -1.06 | -1.06 | +2.01 | — | (子树本身) |
| sufficiency | `cs_regres(day_wmean(Volume, Volume), day_sum(Ret))` | -0.48 | -0.48 | +0.08 | — | (子树本身) |
| knockout | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)` | +1.10 | +1.10 | +3.45 | +0.79 | `cs_last_low20(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))` |
| knockout | `ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1)` | +1.17 | +1.17 | +2.68 | +0.72 | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), cs_regres(day_wmean(Volume, Volume), day_sum(Ret)))` |
| knockout | `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` | +1.12 | +1.12 | +2.25 | +0.78 | `cs_last_low20(ts_decay_linear(day_signed_ratio(Ret, Volume), 40), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))` |
| knockout | `cs_regres(day_wmean(Volume, Volume), day_sum(Ret))` | +0.73 | +0.73 | +3.18 | +1.17 | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(day_wmean(Volume, Volume), 60, 1))` |
| swap | `Volume->Amt` | +1.40 | +1.40 | +3.95 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Amt), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_wmean(Amt, Amt), day_sum(Ret)), 60, 1))` |
| window | `ts_decay_linear@40->20` | +1.94 | +1.94 | +3.83 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))` |
| window | `ts_decay_linear@40->80` | +1.90 | +1.90 | +3.38 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 80), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))` |

### head score +1.62:`cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 40)` | +0.60 | +0.60 | +1.48 | — | (子树本身) |
| sufficiency | `cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret))` | -0.72 | -0.72 | +1.26 | — | (子树本身) |
| sufficiency | `cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap))` | -0.64 | -0.64 | +1.20 | — | (子树本身) |
| sufficiency | `mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume))` | -0.58 | -0.58 | +1.27 | — | (子树本身) |
| knockout | `ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 40)` | +0.23 | +0.23 | +2.25 | +1.38 | `cs_last_low20(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| knockout | `cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret))` | +1.61 | +1.61 | +2.51 | +0.01 | `cs_last_low20(ts_decay_linear(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| knockout | `cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap))` | +1.67 | +1.67 | +2.33 | -0.05 | `cs_last_low20(ts_decay_linear(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| knockout | `mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume))` | +1.53 | +1.53 | +2.72 | +0.08 | `cs_last_low20(ts_decay_linear(cs_regres(cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Vwap)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| swap | `Volume->Amt` | +1.68 | +1.68 | +2.43 | — | `cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Amt), day_sum(Ret)), day_signed_ratio(abs_(Ret), Amt)), day_sum(Vwap)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Amt), 60, 1))` |
| swap | `Vwap->Close` | +1.62 | +1.62 | +2.32 | — | `cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Close)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| window | `ts_decay_linear@40->20` | +1.63 | +1.63 | +2.41 | — | `cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 20), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |
| window | `ts_decay_linear@40->80` | +1.60 | +1.60 | +2.64 | — | `cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 80), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))` |

### head score +1.61:`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)` | +0.62 | +0.62 | +2.63 | — | (子树本身) |
| sufficiency | `ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1)` | -0.81 | -0.81 | -0.41 | — | (子树本身) |
| sufficiency | `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` | -1.06 | -1.06 | +2.01 | — | (子树本身) |
| sufficiency | `cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret))` | -2.68 | -2.68 | -2.37 | — | (子树本身) |
| knockout | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)` | -0.04 | -0.04 | +2.30 | +1.65 | `cs_last_low20(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))` |
| knockout | `ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1)` | +1.27 | +1.27 | +2.89 | +0.34 | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)))` |
| knockout | `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` | +0.43 | +0.43 | +2.33 | +1.18 | `cs_last_low20(ts_decay_linear(day_signed_ratio(Ret, Volume), 40), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))` |
| knockout | `cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret))` | +1.58 | +1.58 | +2.98 | +0.02 | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |
| swap | `Volume->Amt` | +1.60 | +1.60 | +3.30 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Amt), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))` |
| window | `ts_decay_linear@40->20` | +1.37 | +1.37 | +3.40 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))` |
| window | `ts_decay_linear@40->80` | +1.50 | +1.50 | +3.12 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 80), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))` |

### head score +1.49:`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30)` | +0.67 | +0.67 | +2.38 | — | (子树本身) |
| sufficiency | `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` | -1.06 | -1.06 | +2.01 | — | (子树本身) |
| sufficiency | `ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1)` | -0.76 | -0.76 | -0.34 | — | (子树本身) |
| sufficiency | `day_signed_ratio(Ret, Volume)` | -2.48 | -2.48 | +1.34 | — | (子树本身) |
| knockout | `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30)` | -0.48 | -0.48 | +1.86 | +1.97 | `cs_last_low20(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |
| knockout | `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` | +0.50 | +0.50 | +1.85 | +1.00 | `cs_last_low20(ts_decay_linear(day_signed_ratio(Ret, Volume), 30), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |
| knockout | `ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1)` | +0.72 | +0.72 | +2.58 | +0.77 | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30), day_signed_ratio(Ret, Ret))` |
| swap | `Volume->Amt` | +1.55 | +1.55 | +2.82 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Amt), day_sum(Ret)), 30), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |
| window | `ts_decay_linear@30->15` | +1.25 | +1.25 | +2.79 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 15), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |
| window | `ts_decay_linear@30->60` | +1.65 | +1.65 | +2.90 | — | `cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 60), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_sum(Vwap)` — enrichment,均值差 +2.04,p 0.001
2. `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 30)` — enrichment,均值差 +1.97,p 0.000
3. `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)` — enrichment,均值差 +1.61,p 0.000
4. `inv(LogFloatShares)` — enrichment,均值差 +1.26,p 0.000
5. `ts_decay_linear(inv(LogFloatShares), 40)` — enrichment,均值差 +1.24,p 0.006
6. `ts_decay_linear(LogFloatShares, 40)` — enrichment,均值差 +1.24,p 0.022
7. `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` — enrichment,均值差 +1.18,p 0.001
8. `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` — enrichment,均值差 +1.17,p 0.001
9. `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` — enrichment,均值差 +1.13,p 0.033
10. `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` — enrichment,均值差 +1.11,p 0.006
11. `mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume))` — enrichment,均值差 +1.08,p 0.003
12. `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` — enrichment,均值差 +1.06,p 0.030
13. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.03,p 0.000
14. `ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1)` — enrichment,均值差 +0.99,p 0.012
15. `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` — enrichment,均值差 +0.93,p 0.048
16. `cross_decay_linear(LogFloatShares, 3)` — enrichment,均值差 +0.89,p 0.067
17. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +0.88,p 0.016
18. `day_signed_ratio(abs_(Ret), Volume)` — enrichment,均值差 +0.85,p 0.001
19. `ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)` — enrichment,均值差 +0.82,p 0.051
20. `day_max(Volume)` — enrichment,均值差 +0.78,p 0.003
21. `cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Ret))` — enrichment,均值差 +0.76,p 0.094
22. `ts_autocorr(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 60, 1)` — enrichment,均值差 +0.68,p 0.027
23. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.65,p 0.013
24. `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` — enrichment,均值差 +0.65,p 0.000
25. `day_signed_ratio(Ret, Volume)` — enrichment,均值差 +0.55,p 0.000
26. `day_max(Ret)` — enrichment,均值差 +0.54,p 0.067
27. `day_sum(Ret)` — enrichment,均值差 +0.41,p 0.001
28. `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` — enrichment,均值差 +0.40,p 0.020
29. `day_durbin_watson(Volume)` — enrichment,均值差 +0.39,p 0.023
30. `day_durbin_watson(High)` — enrichment,均值差 +0.39,p 0.073
31. `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` — enrichment,均值差 +0.37,p 0.032
32. `day_flat_run_max(Vwap)` — enrichment,均值差 +0.35,p 0.031
33. `day_cov(Ret, Ret)` — enrichment,均值差 +0.34,p 0.085

## 本组之前各轮的任务

- `c06s802Cr1a_Ea`:核心 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`;评分 94,过线 2,入 heads 2;采样计数 {'c05_no_core': 2402, 'c05_periphery_seen': 6, 'mutation_refused': 2, 'c05_skeleton': 2}
  - score +0.79(train +1.27 valid +0.79):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))`
  - score +0.72(train +0.72 valid +0.75):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(sub(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)), day_durbin_watson(Volume), 50)), 60))`
  - score +0.42(train +0.42 valid +2.31):`sub(day_flat_run_max(Vwap), ts_decay_linear(sigmoid(ts_regbeta(sub(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)), day_durbin_watson(Volume), 50)), 60))`
  - score +0.34(train +1.21 valid +0.34):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 40)), 50)), 60))`
  - score +0.33(train +0.33 valid +0.73):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Vwap), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))`
- `c06s802Cr1b_Nb`:核心 `—`;评分 86,过线 5,入 heads 1;采样计数 {}
  - score +0.89(train +0.89 valid +1.85):`ts_decay_linear(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), 40)`
  - score +0.62(train +0.62 valid +2.63):`ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)`
  - score +0.62(train +0.62 valid +2.63):`ts_decay_linear(cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Ret)), 40)`
  - score +0.52(train +0.52 valid +2.22):`ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20)`
  - score +0.52(train +0.52 valid +2.22):`ts_decay_linear(cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Ret)), 20)`
- `c06s802Cr2a_Ea`:核心 `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))`;评分 93,过线 32,入 heads 10;采样计数 {'c05_no_core': 1077, 'c05_periphery_seen': 4}
  - score +1.89(train +1.89 valid +3.75):`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_wmean(Volume, Volume), day_sum(Ret)), 60, 1))`
  - score +1.62(train +1.62 valid +2.34):`cs_last_low20(ts_decay_linear(cs_regres(cs_regres(mul(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_signed_ratio(abs_(Ret), Volume)), day_sum(Vwap)), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))`
  - score +1.61(train +1.61 valid +3.34):`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(cs_regres(day_signed_ratio(Ret, Ret), day_sum(Ret)), 60, 1))`
  - score +1.55(train +1.55 valid +2.69):`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1)))`
  - score +1.54(train +1.54 valid +2.69):`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40), ts_autocorr(day_signed_ratio(Ret, Volume), 60, 1))`
- `c06s802Cr2b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {}
  - score +0.28(train +0.30 valid +0.28):`cross_ema(cross_zscore(ts_argmax(day_signed_ratio(in_delta(Close, 1), mul(mul(in_delta(Close, 1), in_delta(Close, 1)), in_delta(Close, 1))), 50), 241), 10)`
  - score +0.13(train +0.13 valid +1.57):`cross_ema(cross_zscore(ts_argmax(day_signed_ratio(in_delta(Close, 1), mul(in_delta(Close, 1), in_delta(Close, 1))), 50), 241), 10)`
  - score +0.01(train +0.04 valid +0.01):`cross_ema(cross_zscore(ts_argmax(day_signed_ratio(in_delta(Close, 1), mul(in_delta(Amt, 1), in_delta(in_delta(Close, 1), 1))), 50), 241), 10)`
  - score -0.06(train -0.06 valid +0.94):`cross_ema(cross_zscore(ts_argmax(day_signed_ratio(in_delta(Close, 1), Ret), 50), 241), 10)`
  - score -0.10(train -0.05 valid -0.10):`cross_ema(cross_zscore(ts_argmax(day_signed_ratio(in_delta(Close, 3), mul(in_delta(Close, 1), in_delta(Close, 1))), 50), 241), 10)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.15(window ts_decay_linear@30->60):`cs_last_low20(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 60), ts_autocorr(day_signed_ratio(Ret, Ret), 60, 1))`
