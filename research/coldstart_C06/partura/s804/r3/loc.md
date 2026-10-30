# 定位:种子 804,C 组,第 3 轮(只含 train / valid)

快照:c05s804M1_I0_open_search, c05s804M2_I0_open_search, c05s804M3_I0_open_search, c06s804Cr1a_Ea, c06s804Cr1b_Nb, c06s804Cr2a_Ea, c06s804Cr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(20 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.66 | +1.66 | +2.82 | -1 | 5 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +1.39 | +1.39 | +1.59 | -1 | 5 | c06s804Cr2b_Nb | `neg(ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 20))` |
| +1.33 | +1.33 | +2.83 | -1 | 5 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.30 | +1.30 | +2.08 | +1 | 5 | c06s804Cr2b_Nb | `neg(ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 20))` |
| +1.03 | +1.03 | +1.85 | -1 | 0 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20)), day_mean(Open)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.94 | +0.94 | +1.43 | -1 | 20 | c06s804Cr2b_Nb | `day_kurt(abs_(Ret))` |
| +0.91 | +0.91 | +1.87 | +1 | 0 | c05s804M1_I0_open_search | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.89 | +0.89 | +1.90 | -1 | 20 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +0.88 | +0.88 | +2.81 | +1 | 5 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| +0.83 | +0.83 | +1.39 | -1 | 0 | c06s804Cr2a_Ea | `cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(LogFloatCap))` |
| +0.78 | +0.78 | +1.94 | +1 | 0 | c05s804M1_I0_open_search | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.67 | +0.67 | +0.91 | -1 | 0 | c06s804Cr1b_Nb | `cross_stddev(day_skew(Ret), 60)` |
| +0.65 | +0.65 | +2.79 | +1 | 20 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.64 | +0.64 | +2.12 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10))` |
| +0.63 | +0.63 | +1.24 | -1 | 0 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(ts_mean(day_skew(Amt), 20), 20), 20)), day_mean(Open))` |
| +0.61 | +0.61 | +2.09 | +1 | 5 | c06s804Cr2a_Ea | `cs_last_high20(neg(ts_mean(cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt))), 60), 20)), cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt))), 60))` |
| +0.60 | +0.60 | +1.66 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60), cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60))` |
| +0.58 | +0.58 | +1.90 | +1 | 20 | c05s804M1_I0_open_search | `sub(sub(sub(sub(ts_mean(abs_(neg(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10))))), 30), ts_var(day_gini(High), 10)), ts_var(day_gini(High), 10)), day_centroid(sqrt(Volume))), day_centroid(sqrt(Volume)))` |
| +0.57 | +0.57 | +1.28 | -1 | 20 | c05s804M3_I0_open_search | `inv(day_es_ratio_lo(add(Volume, Vwap)))` |
| +0.52 | +0.52 | +1.89 | -1 | 0 | c06s804Cr1a_Ea | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_q_stat_std(Ret), 20), 20)), pow_3(day_mean(Open)))` |

## 共性:574 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.74 | 0.000 | 5 | +1.01 / -0.73 | `neg(ts_mean(day_centroid(sqrt(Volume)), 20))` |
| +1.65 | 0.000 | 9 | +0.91 / -0.74 | `ts_mean(day_centroid(sqrt(Volume)), 20)` |
| +1.55 | 0.000 | 6 | +0.82 / -0.73 | `ts_var(day_gini(High), 5)` |
| +1.53 | 0.000 | 5 | +0.80 / -0.73 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` |
| +1.52 | 0.001 | 4 | +0.79 / -0.73 | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.39 | 0.009 | 4 | +0.66 / -0.73 | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20))` |
| +1.38 | 0.000 | 23 | +0.61 / -0.77 | `day_centroid(sqrt(Volume))` |
| +1.38 | 0.004 | 4 | +0.65 / -0.73 | `cross_ema(cross_ema(LogFloatShares, 241), 241)` |
| +1.32 | 0.001 | 7 | +0.59 / -0.73 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.31 | 0.004 | 4 | +0.59 / -0.72 | `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` |
| +1.31 | 0.002 | 5 | +0.59 / -0.73 | `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` |
| +1.24 | 0.000 | 12 | +0.50 / -0.74 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` |
| +1.16 | 0.007 | 7 | +0.43 / -0.73 | `day_sum(Amt)` |
| +1.15 | 0.017 | 5 | +0.43 / -0.73 | `ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)` |
| +1.13 | 0.019 | 5 | +0.41 / -0.73 | `day_es_ratio_lo(add(Volume, Vwap))` |
| +1.09 | 0.025 | 5 | +0.37 / -0.73 | `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` |
| +1.00 | 0.004 | 7 | +0.27 / -0.73 | `ts_decay_linear(day_mean(Open), 20)` |
| +0.99 | 0.000 | 59 | +0.18 / -0.82 | `cross_ema(LogFloatShares, 241)` |
| +0.96 | 0.081 | 4 | +0.24 / -0.72 | `ts_mean(day_skew(Open), 20)` |
| +0.96 | 0.081 | 4 | +0.24 / -0.72 | `day_skew(Open)` |

## 拆解(38 次评估)

### head score +1.66:`cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)))` | +1.62 | +1.62 | +2.95 | — | (子树本身) |
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | -1.35 | -1.35 | -0.45 | — | (子树本身) |
| sufficiency | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)))` | -1.16 | -1.16 | -0.51 | +2.82 | `cs_last_low10(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | +0.91 | +0.91 | +2.41 | +0.75 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), neg(ts_decay_linear(pow_3(day_mean(Open)), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.89 | +0.13 | -1.89 | +3.55 | `cs_last_low10(cs_last_high20(ts_decay_linear(pow_3(day_mean(Open)), 20), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| knockout | `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` | -1.14 | -1.14 | -0.49 | +2.80 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(ts_decay_linear(pow_3(day_mean(Open)), 20), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| swap | `Open->Close` | +1.66 | +1.66 | +2.82 | — | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Close)), 20)))` |
| window | `ts_decay_linear@20->10` | +1.70 | +1.70 | +2.83 | — | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 10)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| window | `ts_decay_linear@20->40` | +1.65 | +1.65 | +2.61 | — | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 40)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), neg(ts_decay_linear(pow_3(day_mean(Open)), 20)))` |

### head score +1.39:`neg(ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 20)` | +1.39 | +1.39 | +1.59 | — | (子树本身) |
| sufficiency | `neg(ts_mean(day_centroid(sqrt(Volume)), 10))` | +0.86 | +1.12 | +0.86 | — | (子树本身) |
| sufficiency | `ts_mean(day_centroid(sqrt(Volume)), 10)` | +0.86 | +1.12 | +0.86 | — | (子树本身) |
| sufficiency | `day_centroid(sqrt(Volume))` | +0.06 | +0.06 | +0.17 | — | (子树本身) |
| knockout | `ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 20)` | +0.86 | +1.12 | +0.86 | +0.53 | `neg(neg(ts_mean(day_centroid(sqrt(Volume)), 10)))` |
| knockout | `neg(ts_mean(day_centroid(sqrt(Volume)), 10))` | +1.39 | +1.39 | +1.59 | +0.00 | `neg(ts_mean(ts_mean(day_centroid(sqrt(Volume)), 10), 20))` |
| knockout | `ts_mean(day_centroid(sqrt(Volume)), 10)` | +1.34 | +1.34 | +1.51 | +0.05 | `neg(ts_mean(neg(day_centroid(sqrt(Volume))), 20))` |
| swap | `Volume->Amt` | +1.36 | +1.36 | +1.45 | — | `neg(ts_mean(neg(ts_mean(day_centroid(sqrt(Amt)), 10)), 20))` |
| window | `ts_mean@20->10` | +1.13 | +1.13 | +1.25 | — | `neg(ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 10))` |
| window | `ts_mean@20->40` | +1.09 | +1.16 | +1.09 | — | `neg(ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 40))` |

### head score +1.33:`cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)))` | +1.69 | +1.69 | +3.49 | — | (子树本身) |
| sufficiency | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))` | -0.75 | -0.75 | +0.34 | — | (子树本身) |
| sufficiency | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | -1.35 | -1.35 | -0.45 | — | (子树本身) |
| knockout | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)))` | +0.68 | +0.68 | +2.11 | +0.65 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| knockout | `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))` | +1.33 | +1.33 | +2.83 | +0.00 | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| knockout | `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` | +1.28 | +1.28 | +2.37 | +0.05 | `cs_last_low10(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| swap | `Open->Close` | +1.33 | +1.33 | +2.84 | — | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Close)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Close)), 20))` |
| window | `ts_decay_linear@20->10` | +1.32 | +1.32 | +2.77 | — | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 10)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| window | `ts_decay_linear@20->40` | +1.30 | +1.30 | +2.85 | — | `cs_last_low10(cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 40)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20))), ts_decay_linear(pow_3(day_mean(Open)), 20))` |

### head score +1.30:`neg(ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 20)` | +1.30 | +1.30 | +2.08 | — | (子树本身) |
| sufficiency | `div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt))` | -0.10 | -0.10 | +0.52 | — | (子树本身) |
| sufficiency | `day_sum(mul(Amt, is_gt(in_index(Amt), 0.875)))` | -0.23 | +0.09 | -0.23 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -0.48 | -0.48 | +0.89 | — | (子树本身) |
| knockout | `ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 20)` | -0.10 | -0.10 | +0.52 | +1.40 | `neg(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)))` |
| knockout | `div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt))` | -1.87 | -1.77 | -1.87 | +3.17 | `neg(ts_mean(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), 20))` |
| swap | `Amt->Volume` | +1.31 | +1.31 | +2.07 | — | `neg(ts_mean(div(day_sum(mul(Volume, is_gt(in_index(Volume), 0.875))), day_sum(Volume)), 20))` |
| window | `ts_mean@20->10` | +1.08 | +1.08 | +1.85 | — | `neg(ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 10))` |
| window | `ts_mean@20->40` | +1.28 | +1.28 | +2.23 | — | `neg(ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), cs_last_high20(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), ts_mean(day_skew(Ret), 20)))` — ablation,自身 score +1.69(所在 head +1.33)
2. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)))` — ablation,自身 score +1.62(所在 head +1.66)
3. `ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 20)` — ablation,自身 score +1.39(所在 head +1.39)
4. `ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 20)` — ablation,自身 score +1.30(所在 head +1.30)
5. `neg(ts_mean(day_centroid(sqrt(Volume)), 10))` — ablation,自身 score +0.86(所在 head +1.39)
6. `ts_mean(day_centroid(sqrt(Volume)), 10)` — ablation,自身 score +0.86(所在 head +1.39)
7. `neg(ts_mean(day_centroid(sqrt(Volume)), 20))` — enrichment,均值差 +1.74,p 0.000
8. `ts_mean(day_centroid(sqrt(Volume)), 20)` — enrichment,均值差 +1.65,p 0.000
9. `ts_var(day_gini(High), 5)` — enrichment,均值差 +1.55,p 0.000
10. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` — enrichment,均值差 +1.53,p 0.000
11. `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +1.52,p 0.001
12. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20))` — enrichment,均值差 +1.39,p 0.009
13. `day_centroid(sqrt(Volume))` — enrichment,均值差 +1.38,p 0.000
14. `cross_ema(cross_ema(LogFloatShares, 241), 241)` — enrichment,均值差 +1.38,p 0.004
15. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.32,p 0.001
16. `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` — enrichment,均值差 +1.31,p 0.004
17. `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` — enrichment,均值差 +1.31,p 0.002
18. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` — enrichment,均值差 +1.24,p 0.000
19. `day_sum(Amt)` — enrichment,均值差 +1.16,p 0.007
20. `ts_mean(cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20)), 20)` — enrichment,均值差 +1.15,p 0.017
21. `day_es_ratio_lo(add(Volume, Vwap))` — enrichment,均值差 +1.13,p 0.019
22. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` — enrichment,均值差 +1.09,p 0.025
23. `ts_decay_linear(day_mean(Open), 20)` — enrichment,均值差 +1.00,p 0.004
24. `cross_ema(LogFloatShares, 241)` — enrichment,均值差 +0.99,p 0.000
25. `ts_mean(day_skew(Open), 20)` — enrichment,均值差 +0.96,p 0.081
26. `day_skew(Open)` — enrichment,均值差 +0.96,p 0.081
27. `cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt))), 60)` — enrichment,均值差 +0.95,p 0.027
28. `day_quantile(Amt)` — enrichment,均值差 +0.94,p 0.005
29. `pow_2_5(day_quantile(Amt))` — enrichment,均值差 +0.94,p 0.005
30. `ts_quantile_q50(day_gini(High), 10)` — enrichment,均值差 +0.91,p 0.053
31. `cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt)))` — enrichment,均值差 +0.87,p 0.024
32. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(day_skew(Ret), 20))` — enrichment,均值差 +0.86,p 0.000
33. `abs_(day_corr(Vwap, High))` — enrichment,均值差 +0.84,p 0.091
34. `ts_var(day_gini(High), 10)` — enrichment,均值差 +0.83,p 0.000
35. `cs_mask_top_replace_mean_neg(day_last(Low))` — enrichment,均值差 +0.82,p 0.085
36. `day_gini(High)` — enrichment,均值差 +0.82,p 0.000
37. `day_signed_ratio(Close, Low)` — enrichment,均值差 +0.79,p 0.043
38. `cross_delay(day_signed_ratio(High, Open), 60)` — enrichment,均值差 +0.67,p 0.013
39. `day_signed_ratio(High, Open)` — enrichment,均值差 +0.67,p 0.002
40. `cs_last_high20(neg(ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_mean(ts_mean(day_skew(Ret), 20), 20))` — enrichment,均值差 +0.65,p 0.053
41. `neg(ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +0.62,p 0.000
42. `sub(cross_stddev(day_skew(Ret), 60), LogFloatCap)` — enrichment,均值差 +0.59,p 0.020
43. `ts_mean(day_skew(Ret), 20)` — enrichment,均值差 +0.59,p 0.000
44. `ts_decay_linear(pow_3(day_mean(Open)), 20)` — enrichment,均值差 +0.50,p 0.000
45. `pow_3(day_mean(Open))` — enrichment,均值差 +0.49,p 0.000
46. `day_mean(Open)` — enrichment,均值差 +0.46,p 0.000
47. `cs_mask_top_replace_mean(day_durbin_watson(Ret))` — enrichment,均值差 +0.37,p 0.056
48. `day_skew(Ret)` — enrichment,均值差 +0.32,p 0.011
49. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.31,p 0.056

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
- `c06s804Cr2a_Ea`:核心 `cross_stddev(day_skew(Ret), 60)`;评分 103,过线 2,入 heads 2;采样计数 {'c05_no_core': 2784, 'mutation_refused': 6, 'c05_skeleton': 4}
  - score +0.83(train +0.83 valid +1.39):`cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(LogFloatCap))`
  - score +0.61(train +0.61 valid +2.09):`cs_last_high20(neg(ts_mean(cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt))), 60), 20)), cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt))), 60))`
  - score +0.48(train +0.48 valid +0.86):`cs_last_high20(neg(LogFloatCap), cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), LogFloatCap), pow_2_5(day_quantile(Amt))), 60))`
  - score +0.46(train +0.46 valid +1.19):`cs_last_high20(neg(ts_mean(day_skew(Ret), 20)), cross_stddev(cs_last_low40(sub(cross_stddev(day_skew(Ret), 60), day_quantile(Amt)), pow_2_5(day_quantile(Amt))), 60))`
  - score +0.39(train +0.39 valid +1.21):`sub(cross_stddev(day_skew(Ret), 60), LogFloatCap)`
- `c06s804Cr2b_Nb`:核心 `—`;评分 88,过线 18,入 heads 3;采样计数 {}
  - score +1.39(train +1.39 valid +1.59):`neg(ts_mean(neg(ts_mean(day_centroid(sqrt(Volume)), 10)), 20))`
  - score +1.34(train +1.34 valid +1.52):`neg(neg(ts_mean(day_centroid(sqrt(Volume)), 20)))`
  - score +1.34(train +1.34 valid +1.52):`neg(ts_mean(day_centroid(sqrt(Volume)), 20))`
  - score +1.33(train +1.33 valid +1.55):`neg(ts_mean(day_centroid(sqrt(Amt)), 20))`
  - score +1.30(train +1.30 valid +2.08):`neg(ts_mean(div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.875))), day_sum(Amt)), 20))`

## 比原 head 好的拆解变体(R 候选)

(没有)
