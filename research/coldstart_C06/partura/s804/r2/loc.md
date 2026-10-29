# 定位:种子 804,C 组,第 2 轮(只含 train / valid)

快照:c05s804M1_I0_open_search, c05s804M2_I0_open_search, c06s804Cr1a_Ea, c06s804Cr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(14 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.56 | +1.56 | +2.26 | -1 | 5 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +1.22 | +1.22 | +2.54 | -1 | 5 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.03 | +1.03 | +1.85 | -1 | 0 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.91 | +0.91 | +1.87 | +1 | 0 | c05s804M1_I0_open_search | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.88 | +0.88 | +2.81 | +1 | 5 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| +0.79 | +0.79 | +1.76 | -1 | 20 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +0.78 | +0.78 | +1.94 | +1 | 0 | c05s804M1_I0_open_search | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.67 | +0.67 | +0.91 | -1 | 0 | c06s804Cr1b_Nb | `cross_stddev(day_skew(Ret), 60)` |
| +0.65 | +0.65 | +2.79 | +1 | 20 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.64 | +0.64 | +2.12 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10))` |
| +0.63 | +0.63 | +1.24 | -1 | 0 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(ts_mean(day_skew(Amt), 20), 20), 20)), day_mean(Open))` |
| +0.60 | +0.60 | +1.66 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60), cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60))` |
| +0.58 | +0.58 | +1.90 | +1 | 20 | c05s804M1_I0_open_search | `sub(sub(sub(sub(ts_mean(abs_(neg(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10))))), 30), ts_var(day_gini(High), 10)), ts_var(day_gini(High), 10)), day_centroid(sqrt(Volume))), day_centroid(sqrt(Volume)))` |
| +0.52 | +0.52 | +1.89 | -1 | 0 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_q_stat_std(Ret), 20), 20)), pow_3(day_mean(Open)))` |

## 共性:384 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.49 | 0.000 | 6 | +0.82 / -0.67 | `ts_var(day_gini(High), 5)` |
| +1.46 | 0.000 | 5 | +0.80 / -0.66 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` |
| +1.45 | 0.001 | 4 | +0.79 / -0.66 | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.32 | 0.009 | 4 | +0.66 / -0.66 | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20))` |
| +1.31 | 0.004 | 4 | +0.65 / -0.66 | `cross_ema(cross_ema(LogFloatShares, 241), 241)` |
| +1.26 | 0.001 | 7 | +0.59 / -0.67 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.25 | 0.002 | 5 | +0.59 / -0.66 | `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` |
| +1.24 | 0.004 | 4 | +0.59 / -0.66 | `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` |
| +1.18 | 0.000 | 12 | +0.50 / -0.68 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` |
| +1.09 | 0.018 | 5 | +0.43 / -0.66 | `ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)` |
| +1.02 | 0.038 | 5 | +0.37 / -0.66 | `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` |
| +0.97 | 0.000 | 59 | +0.18 / -0.79 | `cross_ema(LogFloatShares, 241)` |
| +0.93 | 0.007 | 9 | +0.27 / -0.66 | `day_centroid(sqrt(Volume))` |
| +0.93 | 0.004 | 7 | +0.27 / -0.66 | `ts_decay_linear(day_mean(Open), 20)` |
| +0.89 | 0.097 | 4 | +0.24 / -0.65 | `ts_mean(day_skew(Open), 20)` |
| +0.89 | 0.097 | 4 | +0.24 / -0.65 | `day_skew(Open)` |
| +0.84 | 0.066 | 4 | +0.18 / -0.65 | `ts_quantile_q50(day_gini(High), 10)` |
| +0.80 | 0.000 | 23 | +0.11 / -0.69 | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` |
| +0.79 | 0.000 | 72 | -0.00 / -0.79 | `day_gini(High)` |
| +0.78 | 0.000 | 46 | +0.05 / -0.74 | `ts_var(day_gini(High), 10)` |

## 拆解(44 次评估)

### head score +1.56:`cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20))` | +1.38 | +1.38 | +2.70 | — | (子树本身) |
| sufficiency | `ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)` | -1.51 | -1.51 | -0.03 | — | (子树本身) |
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | -1.35 | -1.35 | -0.45 | — | (子树本身) |
| sufficiency | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20))` | -1.16 | -1.16 | -0.51 | +2.71 | `cs_last_low10(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)` | +1.66 | +1.66 | +2.82 | -0.10 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | +0.73 | +0.73 | +2.27 | +0.83 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.89 | +0.08 | -1.89 | +3.45 | `cs_last_low10(cs_last_high20(ts_decay_linear(pow_3(day_mean(Open)), 20), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| swap | `Open->Close` | +1.56 | +1.56 | +2.25 | — | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Close)), 20)))` |
| window | `ts_decay_linear@20->10` | +1.60 | +1.60 | +2.31 | — | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 10)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| window | `ts_decay_linear@20->40` | +1.54 | +1.54 | +2.30 | — | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 40)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |

### head score +1.22:`cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20))` | +1.62 | +1.62 | +3.40 | — | (子树本身) |
| sufficiency | `ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)` | -0.86 | -0.86 | +0.99 | — | (子树本身) |
| sufficiency | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))` | -0.75 | -0.75 | +0.34 | — | (子树本身) |
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | -1.35 | -1.35 | -0.45 | — | (子树本身) |
| knockout | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20))` | +0.68 | +0.68 | +2.11 | +0.54 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| knockout | `ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)` | +1.33 | +1.33 | +2.83 | -0.11 | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| knockout | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))` | +1.30 | +1.30 | +2.59 | -0.09 | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | +1.19 | +1.19 | +2.20 | +0.03 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| swap | `Open->Close` | +1.22 | +1.22 | +2.55 | — | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Close)), 20))` |
| window | `ts_decay_linear@20->10` | +1.21 | +1.21 | +2.81 | — | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 10)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| window | `ts_decay_linear@20->40` | +1.24 | +1.24 | +2.48 | — | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 40)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |

### head score +1.03:`cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open))` | +0.73 | +0.73 | +2.06 | — | (子树本身) |
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20))` | -1.20 | -1.20 | -0.34 | — | (子树本身) |
| sufficiency | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open))` | -0.71 | -0.71 | +0.26 | +1.74 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20))` | +0.59 | +0.59 | +1.63 | +0.44 | `cs_last_low10(cs_last_low10(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.69 | +0.05 | -1.69 | +2.72 | `cs_last_low10(cs_last_low10(cs_last_high20(ts_decay_linear(pow_3(day_mean(Open)), 20), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | +0.76 | +0.76 | +2.11 | +0.27 | `cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| swap | `Open->Close` | +1.03 | +1.03 | +1.86 | — | `cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Close)), neg(ts_decay_linear(pow_3(day_mean(Close)), 20)))` |
| window | `ts_decay_linear@20->10` | +1.02 | +1.02 | +1.90 | — | `cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 10)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| window | `ts_decay_linear@20->40` | +0.98 | +0.98 | +1.70 | — | `cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 40)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |

### head score +0.88:`sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open)))` | +0.87 | +0.87 | +2.81 | — | (子树本身) |
| sufficiency | `abs_(day_wstd(Vwap, High))` | -1.06 | -1.06 | -0.39 | — | (子树本身) |
| sufficiency | `pow_3(day_mean(Open))` | -1.16 | -1.16 | -0.45 | — | (子树本身) |
| sufficiency | `ts_var(day_gini(High), 10)` | -0.33 | -0.33 | -0.07 | — | (子树本身) |
| knockout | `cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open)))` | -1.05 | -1.05 | -0.39 | +1.93 | `sub(abs_(day_wstd(Vwap, High)), ts_var(day_gini(High), 10))` |
| knockout | `abs_(day_wstd(Vwap, High))` | +0.88 | +0.88 | +2.81 | -0.00 | `sub(cs_first_low20(day_wstd(Vwap, High), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| knockout | `pow_3(day_mean(Open))` | +0.88 | +0.88 | +2.81 | -0.00 | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), day_mean(Open)), ts_var(day_gini(High), 10))` |
| knockout | `ts_var(day_gini(High), 10)` | +0.89 | +0.89 | +2.80 | -0.01 | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), day_gini(High))` |
| swap | `Vwap->Close` | +0.87 | +0.87 | +2.82 | — | `sub(cs_first_low20(abs_(day_wstd(Close, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| swap | `High->Low` | +0.88 | +0.88 | +2.81 | — | `sub(cs_first_low20(abs_(day_wstd(Vwap, Low)), pow_3(day_mean(Open))), ts_var(day_gini(Low), 10))` |
| window | `ts_var@10->5` | +0.88 | +0.88 | +2.81 | — | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 5))` |
| window | `ts_var@10->20` | +0.88 | +0.88 | +2.81 | — | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 20))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20))` — ablation,自身 score +1.62(所在 head +1.22)
2. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20))` — ablation,自身 score +1.38(所在 head +1.56)
3. `cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open)))` — ablation,自身 score +0.87(所在 head +0.88)
4. `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open))` — ablation,自身 score +0.73(所在 head +1.03)
5. `ts_var(day_gini(High), 5)` — enrichment,均值差 +1.49,p 0.000
6. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` — enrichment,均值差 +1.46,p 0.000
7. `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +1.45,p 0.001
8. `cross_ema(cross_ema(LogFloatShares, 241), 241)` — enrichment,均值差 +1.31,p 0.004
9. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.26,p 0.001
10. `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` — enrichment,均值差 +1.25,p 0.002
11. `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` — enrichment,均值差 +1.24,p 0.004
12. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` — enrichment,均值差 +1.18,p 0.000
13. `ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)` — enrichment,均值差 +1.09,p 0.018
14. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` — enrichment,均值差 +1.02,p 0.038
15. `cross_ema(LogFloatShares, 241)` — enrichment,均值差 +0.97,p 0.000
16. `day_centroid(sqrt(Volume))` — enrichment,均值差 +0.93,p 0.007
17. `ts_decay_linear(day_mean(Open), 20)` — enrichment,均值差 +0.93,p 0.004
18. `ts_mean(day_skew(Open), 20)` — enrichment,均值差 +0.89,p 0.097
19. `day_skew(Open)` — enrichment,均值差 +0.89,p 0.097
20. `ts_quantile_q50(day_gini(High), 10)` — enrichment,均值差 +0.84,p 0.066
21. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` — enrichment,均值差 +0.80,p 0.000
22. `day_gini(High)` — enrichment,均值差 +0.79,p 0.000
23. `ts_var(day_gini(High), 10)` — enrichment,均值差 +0.78,p 0.000
24. `day_signed_ratio(Close, Low)` — enrichment,均值差 +0.73,p 0.055
25. `day_signed_ratio(High, Open)` — enrichment,均值差 +0.61,p 0.004
26. `cross_delay(day_signed_ratio(High, Open), 60)` — enrichment,均值差 +0.61,p 0.020
27. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20))` — enrichment,均值差 +0.58,p 0.057
28. `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +0.57,p 0.001
29. `ts_mean(day_skew(Ret), 20)` — enrichment,均值差 +0.49,p 0.002
30. `day_skew(Ret)` — enrichment,均值差 +0.47,p 0.001
31. `ts_decay_linear(pow_3(day_mean(Open)), 20)` — enrichment,均值差 +0.46,p 0.000
32. `pow_3(day_mean(Open))` — enrichment,均值差 +0.45,p 0.000
33. `day_mean(Open)` — enrichment,均值差 +0.41,p 0.001
34. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.24,p 0.080

## 本组之前各轮的任务

- `c06s804Cr1a_Ea`:核心 `ts_decay_linear(pow_3(day_mean(Open)), 20)`;评分 99,过线 25,入 heads 6;采样计数 {'c05_no_core': 675, 'c05_periphery_seen': 2, 'mutation_refused': 1}
  - score +1.56(train +1.56 valid +2.26):`cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))`
  - score +1.22(train +1.22 valid +2.54):`cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))`
  - score +1.20(train +1.20 valid +2.20):`cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))`
  - score +1.16(train +1.16 valid +1.93):`cs_last_low10(cs_last_high20(neg(ts_decay_linear(ts_decay_linear(pow_3(day_mean(Open)), 20), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(ts_decay_linear(pow_3(day_mean(Open)), 20), 20)), ts_mean(day_skew(Ret), 20)), 50)), neg(ts_decay_linear(ts_decay_linear(pow_3(day_mean(Open)), 20), 20)))`
  - score +1.05(train +1.05 valid +2.73):`cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 50)), ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 50)), ts_mean(day_skew(Ret), 50)), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))`
- `c06s804Cr1b_Nb`:核心 `—`;评分 71,过线 2,入 heads 1;采样计数 {}
  - score +0.67(train +0.67 valid +0.91):`cross_stddev(day_skew(Ret), 60)`
  - score +0.59(train +0.59 valid +1.07):`cross_tail_mean_q75(day_skew(Ret), 60)`
  - score +0.21(train +0.21 valid +0.93):`cross_stddev(day_kurt(Ret), 10)`
  - score +0.12(train +0.12 valid +0.59):`cross_stddev(day_skew(Ret), 30)`
  - score +0.03(train +0.03 valid +0.83):`cross_stddev(day_skew(Ret), 10)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.11(knockout ts_mean(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)), 20)):`cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))`
- 增益 +0.10(knockout ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)):`cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))`
