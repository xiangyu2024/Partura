# 定位:种子 804,B 组,第 2 轮(只含 train / valid)

快照:c05s804M1_I0_open_search, c05s804M2_I0_open_search, c05s804Br1a_Ea, c05s804Br1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(16 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.91 | +0.91 | +1.87 | +1 | 0 | c05s804M1_I0_open_search | `sub(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))), cs_first_low20(sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20)))` |
| +0.88 | +0.88 | +1.05 | -1 | 20 | c05s804Br1b_Nb | `sub(day_centroid(Volume), day_centroid(Ret))` |
| +0.88 | +0.88 | +2.81 | +1 | 5 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` |
| +0.84 | +0.84 | +2.35 | +1 | 5 | c05s804Br1a_Ea | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)` |
| +0.78 | +0.78 | +1.94 | +1 | 0 | c05s804M1_I0_open_search | `sub(cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.73 | +0.73 | +1.95 | +1 | 20 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| +0.67 | +0.67 | +1.59 | +1 | 20 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| +0.67 | +1.26 | +0.67 | -1 | 20 | c05s804Br1b_Nb | `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 10)` |
| +0.67 | +0.67 | +1.33 | -1 | 20 | c05s804Br1b_Nb | `add(day_cov(in_index(Volume), Volume), day_centroid(Ret))` |
| +0.65 | +0.65 | +2.79 | +1 | 20 | c05s804M1_I0_open_search | `sub(cs_first_low20(abs_(day_corr(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20)), ts_var(day_gini(High), 10))` |
| +0.64 | +0.64 | +2.12 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10))` |
| +0.60 | +0.60 | +1.66 | -1 | 20 | c05s804M2_I0_open_search | `cs_first_high40(cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60), cross_delay(cs_first_high40(day_signed_ratio(High, Open), ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)), 60))` |
| +0.59 | +0.59 | +1.83 | +1 | 20 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50), 3), 3), 50))` |
| +0.58 | +0.58 | +1.90 | +1 | 20 | c05s804M1_I0_open_search | `sub(sub(sub(sub(ts_mean(abs_(neg(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10))))), 30), ts_var(day_gini(High), 10)), ts_var(day_gini(High), 10)), day_centroid(sqrt(Volume))), day_centroid(sqrt(Volume)))` |
| +0.55 | +0.55 | +1.08 | +1 | 5 | c05s804Br1a_Ea | `cs_bucket_rank(sqrt(cs_flip_by_state(day_mean(Open), day_mean(Open))), ListAge)` |
| +0.51 | +0.51 | +2.04 | +1 | 5 | c05s804Br1a_Ea | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_topw_mean(Amt, Ret), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` |

## 共性:378 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.60 | 0.000 | 6 | +0.82 / -0.78 | `ts_var(day_gini(High), 5)` |
| +1.58 | 0.000 | 5 | +0.80 / -0.78 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` |
| +1.56 | 0.000 | 4 | +0.79 / -0.77 | `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +1.48 | 0.000 | 14 | +0.67 / -0.81 | `ts_decay_linear(pow_3(day_mean(Open)), 20)` |
| +1.42 | 0.002 | 4 | +0.65 / -0.77 | `cross_ema(cross_ema(LogFloatShares, 241), 241)` |
| +1.37 | 0.001 | 7 | +0.59 / -0.78 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.36 | 0.000 | 15 | +0.55 / -0.81 | `pow_3(day_mean(Open))` |
| +1.36 | 0.001 | 5 | +0.59 / -0.77 | `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` |
| +1.36 | 0.002 | 4 | +0.59 / -0.77 | `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` |
| +1.35 | 0.005 | 4 | +0.58 / -0.77 | `day_cov(in_index(Volume), Volume)` |
| +1.29 | 0.000 | 12 | +0.50 / -0.80 | `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` |
| +1.14 | 0.027 | 5 | +0.37 / -0.77 | `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` |
| +1.10 | 0.000 | 59 | +0.18 / -0.93 | `cross_ema(LogFloatShares, 241)` |
| +1.05 | 0.004 | 9 | +0.27 / -0.78 | `day_centroid(sqrt(Volume))` |
| +0.95 | 0.043 | 4 | +0.18 / -0.77 | `ts_quantile_q50(day_gini(High), 10)` |
| +0.95 | 0.041 | 4 | +0.18 / -0.77 | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3)` |
| +0.95 | 0.041 | 4 | +0.18 / -0.77 | `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3)` |
| +0.93 | 0.000 | 72 | -0.00 / -0.93 | `day_gini(High)` |
| +0.91 | 0.000 | 18 | +0.11 / -0.80 | `day_autocorr_n1(pow_05(Amt))` |
| +0.91 | 0.000 | 46 | +0.05 / -0.87 | `ts_var(day_gini(High), 10)` |

## 拆解(38 次评估)

### head score +0.88:`sub(day_centroid(Volume), day_centroid(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -1.38 | -1.38 | -0.48 | — | (子树本身) |
| swap | `Volume->Amt` | +0.90 | +0.90 | +1.05 | — | `sub(day_centroid(Amt), day_centroid(Ret))` |

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

### head score +0.84:`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)))` | +1.10 | +1.10 | +2.39 | — | (子树本身) |
| sufficiency | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` | +1.35 | +1.35 | +2.61 | — | (子树本身) |
| sufficiency | `ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)` | +1.44 | +1.44 | +2.99 | — | (子树本身) |
| sufficiency | `cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3)` | -1.20 | -1.20 | -0.52 | — | (子树本身) |
| knockout | `sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)))` | +0.56 | +0.92 | +0.56 | +0.28 | `cs_bucket_rank(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)), ListAge)` |
| knockout | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` | -0.82 | -0.82 | -0.44 | +1.66 | `cs_bucket_rank(sqrt(day_autocorr_n1(pow_05(Amt))), ListAge)` |
| knockout | `ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)` | -2.56 | -1.42 | -2.56 | +3.40 | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), day_median(Volume))), ListAge)` |
| knockout | `cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3)` | -1.46 | +0.10 | -1.46 | +2.29 | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), day_mean(Open), 50))), ListAge)` |
| swap | `Amt->Volume` | +0.77 | +0.77 | +1.66 | — | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Volume)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Volume, Ret), 3), 3), 50))), ListAge)` |
| swap | `Volume->Amt` | +0.97 | +0.97 | +2.55 | — | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Amt), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)` |
| window | `ts_regbeta@50->25` | +0.56 | +0.56 | +0.83 | — | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 25))), ListAge)` |
| window | `ts_regbeta@50->100` | +0.57 | +0.81 | +0.57 | — | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 100))), ListAge)` |

### head score +0.73:`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)` | -0.14 | -0.14 | +0.35 | — | (子树本身) |
| sufficiency | `cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3)` | -1.20 | -1.20 | -0.52 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(pow_05(Amt))` | -0.36 | -0.36 | +0.03 | — | (子树本身) |
| sufficiency | `cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3)` | -0.50 | -0.50 | +0.60 | — | (子树本身) |
| knockout | `ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)` | -2.68 | -0.81 | -2.68 | +3.41 | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), day_median(Volume))` |
| knockout | `cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3)` | -0.30 | -0.30 | +0.44 | +1.03 | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), day_mean(Open), 50))` |
| knockout | `cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3)` | -0.55 | -0.55 | -0.19 | +1.28 | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), day_mean(Open), 3), 50))` |
| swap | `Amt->Volume` | +0.78 | +0.78 | +2.06 | — | `cs_first_high20(day_autocorr_n1(pow_05(Volume)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Volume, Ret), 3), 3), 50))` |
| swap | `Volume->Amt` | +0.60 | +0.60 | +1.81 | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Amt), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` |
| window | `ts_reg_tvalue@50->25` | +0.11 | +0.11 | +0.78 | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 25))` |
| window | `ts_reg_tvalue@50->100` | +0.70 | +0.70 | +1.65 | — | `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 100))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)` — ablation,自身 score +1.44(所在 head +0.84)
2. `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))` — ablation,自身 score +1.35(所在 head +0.84)
3. `sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)))` — ablation,自身 score +1.10(所在 head +0.84)
4. `cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open)))` — ablation,自身 score +0.87(所在 head +0.88)
5. `ts_var(day_gini(High), 5)` — enrichment,均值差 +1.60,p 0.000
6. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5))` — enrichment,均值差 +1.58,p 0.000
7. `cs_first_low20(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` — enrichment,均值差 +1.56,p 0.000
8. `ts_decay_linear(pow_3(day_mean(Open)), 20)` — enrichment,均值差 +1.48,p 0.000
9. `cross_ema(cross_ema(LogFloatShares, 241), 241)` — enrichment,均值差 +1.42,p 0.002
10. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.37,p 0.001
11. `pow_3(day_mean(Open))` — enrichment,均值差 +1.36,p 0.000
12. `ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10)` — enrichment,均值差 +1.36,p 0.001
13. `sub(cross_ema(LogFloatShares, 241), ts_var(sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10)), 10))` — enrichment,均值差 +1.36,p 0.002
14. `day_cov(in_index(Volume), Volume)` — enrichment,均值差 +1.35,p 0.005
15. `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` — enrichment,均值差 +1.29,p 0.000
16. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 30)` — enrichment,均值差 +1.14,p 0.027
17. `cross_ema(LogFloatShares, 241)` — enrichment,均值差 +1.10,p 0.000
18. `day_centroid(sqrt(Volume))` — enrichment,均值差 +1.05,p 0.004
19. `ts_quantile_q50(day_gini(High), 10)` — enrichment,均值差 +0.95,p 0.043
20. `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3)` — enrichment,均值差 +0.95,p 0.041
21. `cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3)` — enrichment,均值差 +0.95,p 0.041
22. `day_gini(High)` — enrichment,均值差 +0.93,p 0.000
23. `day_autocorr_n1(pow_05(Amt))` — enrichment,均值差 +0.91,p 0.000
24. `ts_var(day_gini(High), 10)` — enrichment,均值差 +0.91,p 0.000
25. `abs_(day_corr(Vwap, High))` — enrichment,均值差 +0.88,p 0.096
26. `day_signed_ratio(Close, Low)` — enrichment,均值差 +0.84,p 0.050
27. `day_signed_ratio(High, Open)` — enrichment,均值差 +0.74,p 0.002
28. `cross_delay(day_signed_ratio(High, Open), 60)` — enrichment,均值差 +0.73,p 0.015
29. `day_median(Volume)` — enrichment,均值差 +0.64,p 0.009
30. `day_centroid(Ret)` — enrichment,均值差 +0.64,p 0.040
31. `cs_mask_top_replace_mean(day_durbin_watson(Ret))` — enrichment,均值差 +0.43,p 0.072
32. `day_centroid(Volume)` — enrichment,均值差 +0.41,p 0.067
33. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.36,p 0.048
34. `day_topw_mean(Amt, Ret)` — enrichment,均值差 +0.13,p 0.098

## 本组之前各轮的任务

- `c05s804Br1a_Ea`:核心 `day_mean(Open)`;评分 95,过线 8,入 heads 6;采样计数 {'c05_no_core': 701, 'c05_periphery_seen': 3}
  - score +0.84(train +0.84 valid +2.35):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)`
  - score +0.73(train +0.73 valid +1.95):`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))`
  - score +0.68(train +0.68 valid +1.62):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), day_mean(Open))`
  - score +0.67(train +0.67 valid +1.59):`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), cross_reg_tvalue(cs_flip_by_state(LogFloatShares, day_mean(Open)), day_topw_mean(Amt, Ret), 3), 3), 50))`
  - score +0.65(train +0.65 valid +1.89):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_reg_tvalue(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)`
- `c05s804Br1b_Nb`:核心 `—`;评分 81,过线 5,入 heads 3;采样计数 {}
  - score +0.88(train +0.88 valid +1.05):`sub(day_centroid(Volume), day_centroid(Ret))`
  - score +0.71(train +0.71 valid +1.57):`cs_bucket_rank(day_centroid(Volume), day_centroid(Ret))`
  - score +0.67(train +1.26 valid +0.67):`ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 10)`
  - score +0.67(train +0.67 valid +1.33):`add(day_cov(in_index(Volume), Volume), day_centroid(Ret))`
  - score +0.67(train +0.67 valid +1.33):`sub(add(day_cov(in_index(Volume), Volume), day_centroid(Ret)), day_centroid(Ret))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(swap Volume->Amt):`cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Amt), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)`
