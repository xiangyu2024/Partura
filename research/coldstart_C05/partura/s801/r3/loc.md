# 定位:种子 801,B 组,第 3 轮(只含 train / valid)

快照:c05s801M1_I0_open_search, c05s801M2_I0_open_search, c05s801M3_I0_open_search, c05s801Br1a_Ea, c05s801Br1b_Nb, c05s801Br2a_Ea, c05s801Br2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(22 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.69 | +1.69 | +2.33 | -1 | 5 | c05s801Br1b_Nb | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| +1.56 | +1.56 | +2.60 | -1 | 20 | c05s801M3_I0_open_search | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50))` |
| +1.53 | +1.53 | +3.39 | -1 | 5 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| +1.49 | +1.76 | +1.49 | -1 | 5 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| +1.44 | +1.44 | +2.06 | -1 | 0 | c05s801M3_I0_open_search | `ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 50)` |
| +1.15 | +1.31 | +1.15 | +1 | 0 | c05s801Br2a_Ea | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)))` |
| +1.10 | +1.10 | +1.92 | -1 | 5 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60))` |
| +1.07 | +1.07 | +1.25 | +1 | 0 | c05s801Br1a_Ea | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))` |
| +1.07 | +1.07 | +1.76 | -1 | 0 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), day_cov(Low, Open)), 60))` |
| +1.05 | +1.05 | +2.04 | -1 | 5 | c05s801Br2b_Nb | `cs_regres(cross_mean(div(cross_max(log(div(day_first(Open), ts_delay(div(LogFloatCap, day_distinct_ratio(Open)), 1))), 20), day_sum(Amt)), 20), LogFloatCap)` |
| +0.97 | +1.51 | +0.97 | +1 | 5 | c05s801Br2a_Ea | `mul(cs_rank(cross_min(cs_bucket_demean(neg(day_sum(Ret)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20)))` |
| +0.92 | +0.92 | +1.32 | -1 | 0 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_sum(Vwap), BoardCode)), 60))` |
| +0.87 | +0.87 | +1.55 | +1 | 5 | c05s801Br2b_Nb | `cs_regres(cross_mean(div(cross_max(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), day_sum(Amt)), 20), LogFloatCap)` |
| +0.80 | +0.80 | +1.13 | +1 | 20 | c05s801Br2b_Nb | `cs_regres(cross_mean(cross_max(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), 20), LogFloatCap)` |
| +0.75 | +0.75 | +1.66 | -1 | 0 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| +0.70 | +0.70 | +1.84 | +1 | 20 | c05s801Br2b_Nb | `cs_regres(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), LogFloatCap)` |
| +0.69 | +1.60 | +0.69 | -1 | 0 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(cs_bucket_zscore(day_sum(Vwap), BoardCode), day_cov(Low, Open)), 60))` |
| +0.67 | +0.67 | +2.63 | -1 | 0 | c05s801M3_I0_open_search | `ts_std(ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 50), 50)` |
| +0.56 | +0.56 | +2.23 | -1 | 5 | c05s801M3_I0_open_search | `cs_last_high10(LimitWidth, day_open(Open))` |
| +0.55 | +0.55 | +0.71 | +1 | 20 | c05s801Br2a_Ea | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20)))` |
| +0.53 | +0.53 | +1.80 | -1 | 20 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode), 60))` |
| +0.50 | +0.50 | +0.79 | -1 | 20 | c05s801M1_I0_open_search | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` |

## 共性:594 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.71 | 0.000 | 7 | +0.87 / -0.84 | `signedpower(ts_stddev(day_durbin_watson(Close), 20))` |
| +1.68 | 0.000 | 7 | +0.84 / -0.84 | `ts_stddev(signedpower(day_durbin_watson(Close)), 20)` |
| +1.62 | 0.004 | 4 | +0.79 / -0.83 | `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` |
| +1.42 | 0.000 | 16 | +0.56 / -0.86 | `signedpower(day_durbin_watson(Close))` |
| +1.37 | 0.000 | 28 | +0.48 / -0.88 | `pow_3(LogFloatShares)` |
| +1.33 | 0.000 | 46 | +0.41 / -0.92 | `day_durbin_watson(Close)` |
| +1.33 | 0.000 | 12 | +0.48 / -0.85 | `pow_05(pow_3(LogFloatShares))` |
| +1.33 | 0.011 | 4 | +0.50 / -0.83 | `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` |
| +1.33 | 0.000 | 10 | +0.48 / -0.84 | `pow_3(pow_3(LogFloatShares))` |
| +1.32 | 0.000 | 20 | +0.45 / -0.86 | `ts_stddev(day_durbin_watson(Close), 20)` |
| +1.31 | 0.004 | 6 | +0.48 / -0.83 | `pow_3(pow_05(pow_3(LogFloatShares)))` |
| +1.31 | 0.009 | 5 | +0.48 / -0.83 | `pow_05(LogFloatShares)` |
| +1.31 | 0.011 | 5 | +0.48 / -0.83 | `pow_2_5(LogFloatShares)` |
| +1.31 | 0.014 | 4 | +0.48 / -0.83 | `pow_05(pow_3(pow_3(LogFloatShares)))` |
| +1.31 | 0.021 | 4 | +0.48 / -0.83 | `pow_05(pow_2_5(LogFloatShares))` |
| +1.29 | 0.008 | 5 | +0.47 / -0.83 | `cs_state_rank(log(day_first(Open)), 50)` |
| +1.20 | 0.020 | 5 | +0.37 / -0.83 | `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` |
| +1.12 | 0.000 | 18 | +0.27 / -0.85 | `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` |
| +1.12 | 0.007 | 8 | +0.28 / -0.83 | `ts_std(ts_stddev(day_durbin_watson(Close), 20), 20)` |
| +1.10 | 0.000 | 29 | +0.23 / -0.87 | `day_signed_ratio(Close, Close)` |

## 拆解(39 次评估)

### head score +1.56:`signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50)` | +0.95 | +0.95 | +2.24 | — | (子树本身) |
| sufficiency | `signedpower(signedpower(day_durbin_watson(Close)))` | +1.26 | +1.26 | +3.19 | — | (子树本身) |
| sufficiency | `signedpower(day_durbin_watson(Close))` | -0.21 | -0.21 | +1.92 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Close)` | -1.85 | -1.85 | -0.03 | — | (子树本身) |
| knockout | `ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50)` | — | — | — | — | `signedpower(signedpower(signedpower(day_durbin_watson(Close))))` |
| knockout | `signedpower(signedpower(day_durbin_watson(Close)))` | +0.75 | +0.75 | +2.22 | +0.81 | `signedpower(ts_std(signedpower(day_durbin_watson(Close)), 50))` |
| swap | `Close->Vwap` | +1.39 | +1.39 | +3.23 | — | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Vwap))), 50))` |
| window | `ts_std@50->25` | +1.68 | +1.68 | +2.59 | — | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 25))` |
| window | `ts_std@50->100` | +1.59 | +1.59 | +2.24 | — | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 100))` |

### head score +1.44:`ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(ts_stddev(day_durbin_watson(Close), 20))` | +0.49 | +0.49 | +2.59 | — | (子树本身) |
| sufficiency | `ts_stddev(day_durbin_watson(Close), 20)` | +0.29 | +0.29 | +1.73 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Close)` | -1.85 | -1.85 | -0.03 | — | (子树本身) |
| knockout | `signedpower(ts_stddev(day_durbin_watson(Close), 20))` | +1.13 | +1.13 | +1.38 | +0.31 | `ts_std(ts_stddev(day_durbin_watson(Close), 20), 50)` |
| knockout | `ts_stddev(day_durbin_watson(Close), 20)` | +0.59 | +0.59 | +1.80 | +0.85 | `ts_std(signedpower(day_durbin_watson(Close)), 50)` |
| swap | `Close->Vwap` | +1.33 | +1.33 | +2.04 | — | `ts_std(signedpower(ts_stddev(day_durbin_watson(Vwap), 20)), 50)` |
| window | `ts_std@50->25` | +0.94 | +0.94 | +2.21 | — | `ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 25)` |
| window | `ts_std@50->100` | +0.90 | +0.90 | +2.73 | — | `ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 100)` |

### head score +1.15:`mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)` | +0.47 | +0.47 | +1.46 | — | (子树本身) |
| sufficiency | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20)))` | +0.51 | +0.51 | +1.19 | — | (子树本身) |
| sufficiency | `cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60))` | +0.58 | +0.65 | +0.58 | — | (子树本身) |
| knockout | `cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20))` | +0.67 | +0.67 | +1.21 | +0.48 | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20))` |
| knockout | `cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)` | +0.99 | +1.26 | +0.99 | +0.17 | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_quantile_q75(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20)))))` |
| knockout | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20)))` | +0.53 | +0.76 | +0.53 | +0.62 | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_quantile_q75(cross_mean(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), 20)))` |
| knockout | `cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60))` | -0.29 | -0.29 | -0.27 | +1.44 | `mul(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)))` |
| swap | `Vwap->Close` | +1.23 | +1.43 | +1.23 | — | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Close), cross_min(cs_bucket_zscore(day_sum(Close), BoardCode), 60)), 60)), 60)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Close), cross_min(cs_bucket_zscore(day_sum(Close), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Close)), 20))), 20)))` |
| swap | `Amt->Volume` | +0.76 | +1.08 | +0.76 | — | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Volume), day_sum(Vwap)), 20))), 20)))` |
| window | `cross_min@60->30` | +0.77 | +1.24 | +0.77 | — | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 30)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)))` |
| window | `cross_min@60->120` | +1.14 | +1.43 | +1.14 | — | `mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 120)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)))` |

### head score +1.07:`add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret)))` | +0.51 | +0.51 | +0.64 | — | (子树本身) |
| sufficiency | `sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))` | +0.51 | +0.51 | +0.64 | — | (子树本身) |
| sufficiency | `log(cross_mean(day_sum(Volume), 20))` | +0.51 | +0.51 | +0.64 | — | (子树本身) |
| sufficiency | `sub(LogFloatShares, cross_min(LogFloatShares, 120))` | — | — | — | — | 门槛废品 |
| knockout | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret)))))` | — | — | — | — | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), sub(LogFloatShares, cross_min(LogFloatShares, 120)))` |
| knockout | `mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))` | +0.55 | +0.55 | +0.64 | +0.52 | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret)))))` |
| knockout | `cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret)))` | +0.99 | +0.99 | +1.04 | +0.08 | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret)))))` |
| knockout | `sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))` | +0.93 | +0.93 | +1.40 | +0.15 | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(log(cross_mean(day_sum(Volume), 20))))))` |
| swap | `Volume->Amt` | +0.95 | +0.95 | +1.80 | — | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Amt), 20)), day_quantile(Ret))))))` |
| window | `cross_min@120->60` | +1.05 | +1.05 | +1.68 | — | `add(sub(LogFloatShares, cross_min(LogFloatShares, 60)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))` |
| window | `cross_min@120->240` | +0.53 | +0.53 | +0.91 | — | `add(sub(LogFloatShares, cross_min(LogFloatShares, 240)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))` |

## 机械核心卡(B0 按这个顺序取)

1. `signedpower(signedpower(day_durbin_watson(Close)))` — ablation,自身 score +1.26(所在 head +1.56)
2. `ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50)` — ablation,自身 score +0.95(所在 head +1.56)
3. `signedpower(ts_stddev(day_durbin_watson(Close), 20))` — enrichment,均值差 +1.71,p 0.000
4. `ts_stddev(signedpower(day_durbin_watson(Close)), 20)` — enrichment,均值差 +1.68,p 0.000
5. `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` — enrichment,均值差 +1.62,p 0.004
6. `signedpower(day_durbin_watson(Close))` — enrichment,均值差 +1.42,p 0.000
7. `pow_3(LogFloatShares)` — enrichment,均值差 +1.37,p 0.000
8. `day_durbin_watson(Close)` — enrichment,均值差 +1.33,p 0.000
9. `pow_05(pow_3(LogFloatShares))` — enrichment,均值差 +1.33,p 0.000
10. `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` — enrichment,均值差 +1.33,p 0.011
11. `pow_3(pow_3(LogFloatShares))` — enrichment,均值差 +1.33,p 0.000
12. `ts_stddev(day_durbin_watson(Close), 20)` — enrichment,均值差 +1.32,p 0.000
13. `pow_3(pow_05(pow_3(LogFloatShares)))` — enrichment,均值差 +1.31,p 0.004
14. `pow_05(LogFloatShares)` — enrichment,均值差 +1.31,p 0.009
15. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.31,p 0.011
16. `pow_05(pow_3(pow_3(LogFloatShares)))` — enrichment,均值差 +1.31,p 0.014
17. `pow_05(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.31,p 0.021
18. `cs_state_rank(log(day_first(Open)), 50)` — enrichment,均值差 +1.29,p 0.008
19. `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` — enrichment,均值差 +1.20,p 0.020
20. `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` — enrichment,均值差 +1.12,p 0.000
21. `ts_std(ts_stddev(day_durbin_watson(Close), 20), 20)` — enrichment,均值差 +1.12,p 0.007
22. `day_signed_ratio(Close, Close)` — enrichment,均值差 +1.10,p 0.000
23. `day_cov(Low, Open)` — enrichment,均值差 +1.08,p 0.024
24. `pow_05(day_signed_ratio(Close, Close))` — enrichment,均值差 +1.07,p 0.000
25. `day_zero_ratio(Vwap)` — enrichment,均值差 +1.06,p 0.057
26. `cs_state_rank(day_es_ratio_hi(Vwap), 50)` — enrichment,均值差 +1.02,p 0.041
27. `day_es_ratio_hi(Vwap)` — enrichment,均值差 +1.02,p 0.041
28. `cs_state_rank(day_es_ratio_hi(High), 50)` — enrichment,均值差 +0.96,p 0.000
29. `cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode), 60)` — enrichment,均值差 +0.95,p 0.020
30. `cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60))` — enrichment,均值差 +0.88,p 0.009
31. `sub(LogFloatShares, cross_min(LogFloatShares, 120))` — enrichment,均值差 +0.86,p 0.002
32. `cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)` — enrichment,均值差 +0.85,p 0.010
33. `day_autocorr_n1(Vwap)` — enrichment,均值差 +0.79,p 0.001
34. `cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` — enrichment,均值差 +0.72,p 0.014
35. `cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` — enrichment,均值差 +0.72,p 0.018
36. `neg(cross_mean(day_sum(Ret), 60))` — enrichment,均值差 +0.71,p 0.012
37. `log(day_first(Open))` — enrichment,均值差 +0.70,p 0.000
38. `cross_min(LogFloatShares, 120)` — enrichment,均值差 +0.69,p 0.007
39. `cross_mean(day_sum(Ret), 60)` — enrichment,均值差 +0.60,p 0.027
40. `cross_mean(div(day_first(Amt), day_sum(Amt)), 20)` — enrichment,均值差 +0.58,p 0.024
41. `cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20))` — enrichment,均值差 +0.53,p 0.065
42. `day_es_ratio_hi(High)` — enrichment,均值差 +0.49,p 0.008
43. `day_first(Open)` — enrichment,均值差 +0.27,p 0.018

## 本组之前各轮的任务

- `c05s801Br1a_Ea`:核心 `LogFloatShares`;评分 111,过线 7,入 heads 1;采样计数 {'c05_no_core': 661, 'c05_periphery_seen': 2}
  - score +1.07(train +1.07 valid +1.25):`add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))`
  - score +1.01(train +1.02 valid +1.01):`add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(day_sum(Volume))))`
  - score +0.69(train +1.15 valid +0.69):`add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret)))))`
  - score +0.69(train +1.15 valid +0.69):`add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(cross_mean(day_sum(Volume), 20), day_quantile(Ret)))))`
  - score +0.69(train +1.15 valid +0.69):`add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(cross_mean(day_sum(Volume), 20))))`
- `c05s801Br1b_Nb`:核心 `—`;评分 88,过线 13,入 heads 7;采样计数 {}
  - score +1.69(train +1.69 valid +2.33):`cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))`
  - score +1.49(train +1.76 valid +1.49):`cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))`
  - score +1.10(train +1.10 valid +1.92):`cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60))`
  - score +1.07(train +1.07 valid +1.76):`cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), day_cov(Low, Open)), 60))`
  - score +1.07(train +1.07 valid +1.76):`cs_last_high20(pow_05(day_signed_ratio(Close, Open)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), day_cov(Low, Open)), 60))`
- `c05s801Br2a_Ea`:核心 `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)`;评分 100,过线 5,入 heads 3;采样计数 {'c05_no_core': 1115, 'mutation_refused': 5, 'c05_periphery_seen': 3}
  - score +1.15(train +1.31 valid +1.15):`mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_quantile_q75(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Vwap)), 20))), 20)))`
  - score +0.97(train +1.51 valid +0.97):`mul(cs_rank(cross_min(cs_bucket_demean(neg(day_sum(Ret)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20)))`
  - score +0.71(train +0.71 valid +1.12):`mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20))), 20)))`
  - score +0.68(train +0.68 valid +0.81):`mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20))), 60)), 60)), cs_rank(cross_mean(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(day_sum(Ret), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20))), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20))), 20)))`
  - score +0.55(train +0.55 valid +0.71):`mul(cs_rank(cross_min(cs_bucket_demean(neg(cross_mean(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)), 60)), cs_rank(cross_mean(div(day_first(Amt), day_sum(Amt)), 20)))`
- `c05s801Br2b_Nb`:核心 `—`;评分 94,过线 6,入 heads 4;采样计数 {}
  - score +1.05(train +1.05 valid +2.04):`cs_regres(cross_mean(div(cross_max(log(div(day_first(Open), ts_delay(div(LogFloatCap, day_distinct_ratio(Open)), 1))), 20), day_sum(Amt)), 20), LogFloatCap)`
  - score +0.87(train +0.87 valid +1.55):`cs_regres(cross_mean(div(cross_max(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), day_sum(Amt)), 20), LogFloatCap)`
  - score +0.80(train +0.80 valid +1.13):`cs_regres(cross_mean(cross_max(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), 20), LogFloatCap)`
  - score +0.76(train +0.76 valid +1.96):`cs_regres(cross_mean(div(cs_demean(div(-5, div(LogFloatCap, day_distinct_ratio(Open)))), day_sum(Amt)), 20), LogFloatCap)`
  - score +0.70(train +0.70 valid +1.84):`cs_regres(cross_mean(div(day_first(Amt), day_sum(Amt)), 20), LogFloatCap)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.12(window ts_std@50->25):`signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 25))`
