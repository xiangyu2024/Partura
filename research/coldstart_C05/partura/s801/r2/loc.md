# 定位:种子 801,B 组,第 2 轮(只含 train / valid)

快照:c05s801M1_I0_open_search, c05s801M2_I0_open_search, c05s801Br1a_Ea, c05s801Br1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.69 | +1.69 | +2.33 | -1 | 5 | c05s801Br1b_Nb | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| +1.53 | +1.53 | +3.39 | -1 | 5 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| +1.49 | +1.76 | +1.49 | -1 | 5 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| +1.10 | +1.10 | +1.92 | -1 | 5 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60))` |
| +1.07 | +1.07 | +1.25 | +1 | 0 | c05s801Br1a_Ea | `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))` |
| +1.07 | +1.07 | +1.76 | -1 | 0 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), day_cov(Low, Open)), 60))` |
| +0.92 | +0.92 | +1.32 | -1 | 0 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_sum(Vwap), BoardCode)), 60))` |
| +0.75 | +0.75 | +1.66 | -1 | 0 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| +0.69 | +1.60 | +0.69 | -1 | 0 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(cs_bucket_zscore(day_sum(Vwap), BoardCode), day_cov(Low, Open)), 60))` |
| +0.53 | +0.53 | +1.80 | -1 | 20 | c05s801Br1b_Nb | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode), 60))` |
| +0.50 | +0.50 | +0.79 | -1 | 20 | c05s801M1_I0_open_search | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` |

## 共性:344 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.53 | 0.004 | 4 | +0.79 / -0.74 | `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` |
| +1.49 | 0.002 | 6 | +0.75 / -0.75 | `cs_bucket_zscore(day_sum(Vwap), BoardCode)` |
| +1.37 | 0.002 | 7 | +0.62 / -0.75 | `day_sum(Vwap)` |
| +1.31 | 0.000 | 28 | +0.48 / -0.83 | `pow_3(LogFloatShares)` |
| +1.25 | 0.000 | 12 | +0.48 / -0.77 | `pow_05(pow_3(LogFloatShares))` |
| +1.24 | 0.000 | 10 | +0.48 / -0.76 | `pow_3(pow_3(LogFloatShares))` |
| +1.23 | 0.011 | 4 | +0.50 / -0.74 | `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` |
| +1.23 | 0.007 | 6 | +0.48 / -0.74 | `pow_3(pow_05(pow_3(LogFloatShares)))` |
| +1.22 | 0.014 | 5 | +0.48 / -0.74 | `pow_05(LogFloatShares)` |
| +1.22 | 0.017 | 5 | +0.48 / -0.74 | `pow_2_5(LogFloatShares)` |
| +1.22 | 0.017 | 4 | +0.48 / -0.74 | `pow_05(pow_3(pow_3(LogFloatShares)))` |
| +1.22 | 0.029 | 4 | +0.48 / -0.74 | `pow_05(pow_2_5(LogFloatShares))` |
| +1.20 | 0.010 | 5 | +0.47 / -0.74 | `cs_state_rank(log(day_first(Open)), 50)` |
| +1.11 | 0.028 | 5 | +0.37 / -0.74 | `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` |
| +1.04 | 0.001 | 18 | +0.27 / -0.78 | `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` |
| +1.04 | 0.000 | 29 | +0.23 / -0.81 | `day_signed_ratio(Close, Close)` |
| +1.01 | 0.000 | 27 | +0.20 / -0.80 | `pow_05(day_signed_ratio(Close, Close))` |
| +0.99 | 0.027 | 5 | +0.26 / -0.74 | `day_cov(Low, Open)` |
| +0.93 | 0.048 | 4 | +0.20 / -0.73 | `cs_state_rank(day_es_ratio_hi(Vwap), 50)` |
| +0.93 | 0.048 | 4 | +0.20 / -0.73 | `day_es_ratio_hi(Vwap)` |

## 拆解(47 次评估)

### head score +1.69:`cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)` | +0.76 | +0.76 | +1.22 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60))` | -0.13 | -0.13 | +0.83 | — | (子树本身) |
| sufficiency | `pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume)))` | -2.36 | -2.36 | -1.92 | — | (子树本身) |
| sufficiency | `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` | -1.39 | -1.18 | -1.39 | — | (子树本身) |
| knockout | `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)` | +1.07 | +1.07 | +2.22 | +0.62 | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)))` |
| knockout | `cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60))` | -0.69 | -0.36 | -0.69 | +2.38 | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(day_sum(Vwap), 60))` |
| knockout | `pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume)))` | +1.69 | +1.69 | +2.33 | +0.00 | `cs_last_high20(cs_regres(day_at_min_ratio(Vwap), day_first(Volume)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| knockout | `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` | +1.49 | +1.49 | +2.55 | +0.21 | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cs_bucket_zscore(day_sum(Vwap), BoardCode)), 60))` |
| swap | `Vwap->Close` | +1.13 | +1.13 | +2.23 | — | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Close), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Close), cross_min(cs_bucket_zscore(day_sum(Close), BoardCode), 60)), 60))` |
| swap | `Volume->Amt` | +1.53 | +1.53 | +2.57 | — | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Amt))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| window | `cross_min@60->30` | +1.44 | +1.44 | +2.43 | — | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 30))` |
| window | `cross_min@60->120` | +2.00 | +2.00 | +2.48 | — | `cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 120))` |

### head score +1.53:`cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241)` | -0.98 | +0.15 | -0.98 | — | (子树本身) |
| sufficiency | `cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open)))` | -0.44 | +0.72 | -0.44 | — | (子树本身) |
| sufficiency | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` | +0.68 | +0.68 | +1.18 | — | (子树本身) |
| knockout | `cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241)` | -1.90 | +0.13 | -1.90 | +3.43 | `cs_first_high40(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| knockout | `cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open)))` | +1.44 | +1.44 | +3.83 | +0.09 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| knockout | `cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open)))` | +1.54 | +1.54 | +3.39 | -0.01 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))))` |
| knockout | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` | +1.46 | +1.46 | +3.63 | +0.07 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| swap | `High->Low` | +1.53 | +1.53 | +3.39 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), log(day_first(Open))))` |
| swap | `Open->Close` | +1.48 | +1.48 | +3.39 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), log(day_first(Close))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), log(day_first(Close))))` |
| window | `cross_corr@241->120` | +1.35 | +1.35 | +2.54 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 120), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| window | `cross_corr@241->482` | +1.33 | +1.33 | +1.34 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 482), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |

### head score +1.49:`cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)` | +0.76 | +0.76 | +1.22 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60))` | -0.13 | -0.13 | +0.83 | — | (子树本身) |
| sufficiency | `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` | -1.39 | -1.18 | -1.39 | — | (子树本身) |
| sufficiency | `pow_05(day_signed_ratio(Close, Close))` | — | — | — | — | 门槛废品 |
| knockout | `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)` | +1.29 | +1.48 | +1.29 | +0.20 | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)))` |
| knockout | `cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60))` | -0.41 | -0.41 | +1.85 | +1.90 | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(day_sum(Vwap), 60))` |
| knockout | `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` | +1.37 | +1.37 | +1.89 | +0.12 | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cs_bucket_zscore(day_sum(Vwap), BoardCode)), 60))` |
| knockout | `pow_05(day_signed_ratio(Close, Close))` | +1.49 | +1.75 | +1.49 | -0.00 | `cs_last_high20(day_signed_ratio(Close, Close), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| swap | `Close->Vwap` | +1.49 | +1.75 | +1.49 | — | `cs_last_high20(pow_05(day_signed_ratio(Vwap, Vwap)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))` |
| swap | `Vwap->Close` | +1.11 | +1.84 | +1.11 | — | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Close), cross_min(cs_bucket_zscore(day_sum(Close), BoardCode), 60)), 60))` |
| window | `cross_min@60->30` | +1.56 | +1.56 | +1.56 | — | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 30))` |
| window | `cross_min@60->120` | +1.33 | +1.98 | +1.33 | — | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 120))` |

### head score +1.10:`cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60)` | -1.01 | -1.01 | -0.09 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode))` | -1.62 | -0.75 | -1.62 | — | (子树本身) |
| sufficiency | `pow_05(day_signed_ratio(Close, Close))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` | -2.34 | -2.34 | -1.84 | — | (子树本身) |
| knockout | `cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60)` | -0.80 | -0.80 | +1.56 | +1.90 | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)))` |
| knockout | `cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode))` | -0.12 | -0.12 | +1.24 | +1.22 | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(day_autocorr_n1(Vwap), 60))` |
| knockout | `pow_05(day_signed_ratio(Close, Close))` | +1.10 | +1.10 | +1.92 | -0.00 | `cs_last_high20(day_signed_ratio(Close, Close), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60))` |
| knockout | `cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` | +0.15 | +0.15 | +0.36 | +0.95 | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), day_autocorr_n1(Vwap)), 60))` |
| swap | `Close->Vwap` | +1.10 | +1.10 | +1.92 | — | `cs_last_high20(pow_05(day_signed_ratio(Vwap, Vwap)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60))` |
| swap | `Vwap->Close` | +0.23 | +0.90 | +0.23 | — | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Close), cs_bucket_zscore(day_autocorr_n1(Close), BoardCode)), 60))` |
| window | `cross_min@60->30` | +1.08 | +1.08 | +2.20 | — | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 30))` |
| window | `cross_min@60->120` | +1.11 | +1.11 | +2.29 | — | `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 120))` |

## 机械核心卡(B0 按这个顺序取)

1. `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` — enrichment,均值差 +1.53,p 0.004
2. `cs_bucket_zscore(day_sum(Vwap), BoardCode)` — enrichment,均值差 +1.49,p 0.002
3. `day_sum(Vwap)` — enrichment,均值差 +1.37,p 0.002
4. `pow_3(LogFloatShares)` — enrichment,均值差 +1.31,p 0.000
5. `pow_05(pow_3(LogFloatShares))` — enrichment,均值差 +1.25,p 0.000
6. `pow_3(pow_3(LogFloatShares))` — enrichment,均值差 +1.24,p 0.000
7. `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` — enrichment,均值差 +1.23,p 0.011
8. `pow_3(pow_05(pow_3(LogFloatShares)))` — enrichment,均值差 +1.23,p 0.007
9. `pow_05(LogFloatShares)` — enrichment,均值差 +1.22,p 0.014
10. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.22,p 0.017
11. `pow_05(pow_3(pow_3(LogFloatShares)))` — enrichment,均值差 +1.22,p 0.017
12. `pow_05(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.22,p 0.029
13. `cs_state_rank(log(day_first(Open)), 50)` — enrichment,均值差 +1.20,p 0.010
14. `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` — enrichment,均值差 +1.11,p 0.028
15. `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` — enrichment,均值差 +1.04,p 0.001
16. `day_signed_ratio(Close, Close)` — enrichment,均值差 +1.04,p 0.000
17. `pow_05(day_signed_ratio(Close, Close))` — enrichment,均值差 +1.01,p 0.000
18. `day_cov(Low, Open)` — enrichment,均值差 +0.99,p 0.027
19. `cs_state_rank(day_es_ratio_hi(Vwap), 50)` — enrichment,均值差 +0.93,p 0.048
20. `day_es_ratio_hi(Vwap)` — enrichment,均值差 +0.93,p 0.048
21. `cs_state_rank(day_es_ratio_hi(High), 50)` — enrichment,均值差 +0.89,p 0.000
22. `cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode), 60)` — enrichment,均值差 +0.86,p 0.024
23. `sub(LogFloatShares, cross_min(LogFloatShares, 120))` — enrichment,均值差 +0.78,p 0.004
24. `day_autocorr_n1(Vwap)` — enrichment,均值差 +0.71,p 0.003
25. `day_first(Open)` — enrichment,均值差 +0.68,p 0.000
26. `log(day_first(Open))` — enrichment,均值差 +0.66,p 0.000
27. `cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` — enrichment,均值差 +0.63,p 0.035
28. `cross_min(LogFloatShares, 120)` — enrichment,均值差 +0.61,p 0.021
29. `day_es_ratio_hi(High)` — enrichment,均值差 +0.43,p 0.016

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.31(window cross_min@60->120):`cs_last_high20(pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume))), cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 120))`
