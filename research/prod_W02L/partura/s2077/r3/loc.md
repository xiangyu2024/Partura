# 定位:种子 2077,P 组,第 3 轮(只含 train / valid)

快照:prods2077M1_I0_open_search, prods2077M2_I0_open_search, prods2077M3_I0_open_search, prods2077Pr1a_Ea, prods2077Pr1b_Nb, prods2077Pr2a_Ea, prods2077Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.53 | +0.14 | -0.53 | -1 | 5 | prods2077M3_I0_open_search | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))` |
| -0.85 | -0.85 | +0.13 | +1 | 20 | prods2077M3_I0_open_search | `inv(day_cov(pow_1_5(mul(Open, Ret)), cross_scale(nt_ts_reg_fvalue(Volume, Amt, 15), 241)))` |
| -0.92 | -0.31 | -0.92 | -1 | 5 | prods2077M3_I0_open_search | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50))))` |
| -1.02 | -0.22 | -1.02 | -1 | 5 | prods2077M1_I0_open_search | `day_median(div(abs_(Ret), Amt))` |
| -1.12 | -0.87 | -1.12 | -1 | 20 | prods2077M1_I0_open_search | `day_open(in_delta(Volume, 60))` |
| -1.16 | -1.16 | -1.11 | -1 | 5 | prods2077M2_I0_open_search | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), neg(in_slice(Ret, 1, 50)), 0), select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` |
| -1.16 | -1.16 | -1.14 | -1 | 5 | prods2077M2_I0_open_search | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` |
| -1.21 | -1.21 | -1.10 | -1 | 5 | prods2077M2_I0_open_search | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), neg(in_slice(Ret, 1, 20)), 0), select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), in_slice(Volume, 1, 20), create_like(in_slice(Ret, 1, 20), 0))), in_sum(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0)))))` |
| -1.63 | -1.39 | -1.63 | -1 | 20 | prods2077M1_I0_open_search | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))` |

## 共性:341 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.46 | 0.002 | 6 | -1.45 / -2.91 | `cross_cov(day_sum(Ret), day_kurt(Amt), 40)` |
| +1.27 | 0.000 | 21 | -1.69 / -2.96 | `day_zero_ratio(Low)` |
| +1.22 | 0.005 | 5 | -1.68 / -2.90 | `ts_scale(day_zero_ratio(Low), 30)` |
| +1.18 | 0.000 | 14 | -1.75 / -2.93 | `ts_scale(cross_delta(day_zero_ratio(Low), 30), 30)` |
| +1.17 | 0.000 | 15 | -1.77 / -2.93 | `cross_delta(day_zero_ratio(Low), 30)` |
| +1.13 | 0.005 | 6 | -1.77 / -2.90 | `div(day_sum(Amt), day_sum(Volume))` |
| +0.90 | 0.063 | 4 | -1.99 / -2.89 | `day_argmin(pow_1_5(Open))` |
| +0.87 | 0.000 | 32 | -2.10 / -2.96 | `day_median(div(abs_(Ret), Amt))` |
| +0.72 | 0.095 | 4 | -2.17 / -2.89 | `cross_rank(day_argmax(Vwap), 241)` |
| +0.72 | 0.086 | 5 | -2.17 / -2.89 | `day_gini(sqrt(Volume))` |
| +0.68 | 0.054 | 7 | -2.22 / -2.90 | `day_argmin(Low)` |
| +0.62 | 0.136 | 4 | -2.27 / -2.89 | `cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(pow_1_5(Vwap)))` |
| +0.62 | 0.136 | 4 | -2.27 / -2.89 | `pow_3(cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(pow_1_5(Vwap))))` |
| +0.61 | 0.185 | 5 | -2.28 / -2.89 | `day_corr(Ret, Volume)` |
| +0.55 | 0.013 | 21 | -2.37 / -2.91 | `day_kurt(Amt)` |
| +0.44 | 0.030 | 73 | -2.53 / -2.98 | `day_sum(Ret)` |
| +0.39 | 0.157 | 11 | -2.50 / -2.89 | `day_first(Open)` |
| +0.39 | 0.044 | 17 | -2.51 / -2.90 | `day_sum(Volume)` |
| +0.38 | 0.286 | 4 | -2.51 / -2.89 | `day_sum(abs_(Ret))` |
| +0.30 | 0.357 | 6 | -2.59 / -2.89 | `abs_(day_sum(Ret))` |

## 拆解(28 次评估)

### head score -0.53:`mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q25(cs_rank(day_last(Close)), 60)` | -2.37 | -1.57 | -2.37 | — | (子树本身) |
| sufficiency | `ts_max(pow_1_5(day_durbin_watson(Amt)), 1)` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| sufficiency | `cs_rank(day_last(Close))` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| sufficiency | `pow_1_5(day_durbin_watson(Amt))` | -4.18 | -3.68 | -4.18 | — | (子树本身) |
| knockout | `cross_quantile_q25(cs_rank(day_last(Close)), 60)` | -0.51 | +0.11 | -0.51 | -0.02 | `mul(cs_rank(day_last(Close)), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))` |
| knockout | `ts_max(pow_1_5(day_durbin_watson(Amt)), 1)` | -0.50 | +0.14 | -0.50 | -0.03 | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), pow_1_5(day_durbin_watson(Amt)))` |
| knockout | `cs_rank(day_last(Close))` | -1.23 | -0.84 | -1.23 | +0.70 | `mul(cross_quantile_q25(day_last(Close), 60), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))` |
| knockout | `pow_1_5(day_durbin_watson(Amt))` | -1.05 | -0.44 | -1.05 | +0.52 | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max(day_durbin_watson(Amt), 1))` |
| swap | `Close->Vwap` | -0.49 | +0.14 | -0.49 | — | `mul(cross_quantile_q25(cs_rank(day_last(Vwap)), 60), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))` |
| swap | `Amt->Volume` | -0.50 | +0.15 | -0.50 | — | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max(pow_1_5(day_durbin_watson(Volume)), 1))` |
| window | `cross_quantile_q25@60->30` | -0.50 | +0.15 | -0.50 | — | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 30), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))` |
| window | `cross_quantile_q25@60->120` | -0.49 | +0.15 | -0.49 | — | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 120), ts_max(pow_1_5(day_durbin_watson(Amt)), 1))` |

### head score -0.85:`inv(day_cov(pow_1_5(mul(Open, Ret)), cross_scale(nt_ts_reg_fvalue(Volume, Amt, 15), 241)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(pow_1_5(mul(Open, Ret)), cross_scale(nt_ts_reg_fvalue(Volume, Amt, 15), 241))` | -2.08 | -2.08 | -1.09 | — | (子树本身) |
| swap | `Open->Close` | -0.84 | -0.84 | +0.17 | — | `inv(day_cov(pow_1_5(mul(Close, Ret)), cross_scale(nt_ts_reg_fvalue(Volume, Amt, 15), 241)))` |
| swap | `Volume->Amt` | -1.36 | -1.36 | -0.85 | — | `inv(day_cov(pow_1_5(mul(Open, Ret)), cross_scale(nt_ts_reg_fvalue(Amt, Amt, 15), 241)))` |
| window | `cross_scale@241->120` | -1.26 | -1.26 | -0.04 | — | `inv(day_cov(pow_1_5(mul(Open, Ret)), cross_scale(nt_ts_reg_fvalue(Volume, Amt, 15), 120)))` |
| window | `cross_scale@241->482` | -1.30 | -1.30 | -0.20 | — | `inv(day_cov(pow_1_5(mul(Open, Ret)), cross_scale(nt_ts_reg_fvalue(Volume, Amt, 15), 482)))` |

### head score -0.92:`neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)))` | -0.90 | -0.31 | -0.90 | — | (子树本身) |
| sufficiency | `pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50))` | -0.90 | -0.30 | -0.90 | — | (子树本身) |
| sufficiency | `ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)` | +0.57 | +0.82 | +0.57 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -3.76 | -2.94 | -3.76 | — | (子树本身) |
| knockout | `inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)))` | -0.90 | -0.30 | -0.90 | -0.02 | `neg(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)))` |
| knockout | `pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50))` | -1.68 | -1.68 | -1.51 | +0.77 | `neg(inv(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)))` |
| knockout | `ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)` | -3.74 | -3.05 | -3.74 | +2.82 | `neg(inv(pow_2(day_quantile_q75(Amt))))` |
| swap | `Amt->Volume` | -2.55 | -1.04 | -2.55 | — | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Volume), day_hurst(Open), 50))))` |
| swap | `Open->Close` | -0.89 | -0.24 | -0.89 | — | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Close), 50))))` |
| window | `ts_regbeta@50->25` | -1.21 | -1.21 | -0.98 | — | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 25))))` |
| window | `ts_regbeta@50->100` | -0.52 | -0.52 | -0.01 | — | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 100))))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_regbeta(day_quantile_q75(Amt), day_hurst(Open), 50)` — ablation,自身 score +0.57(所在 head -0.92)
2. `cross_cov(day_sum(Ret), day_kurt(Amt), 40)` — enrichment,均值差 +1.46,p 0.002
3. `day_zero_ratio(Low)` — enrichment,均值差 +1.27,p 0.000
4. `ts_scale(day_zero_ratio(Low), 30)` — enrichment,均值差 +1.22,p 0.005
5. `ts_scale(cross_delta(day_zero_ratio(Low), 30), 30)` — enrichment,均值差 +1.18,p 0.000
6. `cross_delta(day_zero_ratio(Low), 30)` — enrichment,均值差 +1.17,p 0.000
7. `div(day_sum(Amt), day_sum(Volume))` — enrichment,均值差 +1.13,p 0.005
8. `day_argmin(pow_1_5(Open))` — enrichment,均值差 +0.90,p 0.063
9. `day_median(div(abs_(Ret), Amt))` — enrichment,均值差 +0.87,p 0.000
10. `cross_rank(day_argmax(Vwap), 241)` — enrichment,均值差 +0.72,p 0.095
11. `day_gini(sqrt(Volume))` — enrichment,均值差 +0.72,p 0.086
12. `day_argmin(Low)` — enrichment,均值差 +0.68,p 0.054
13. `day_kurt(Amt)` — enrichment,均值差 +0.55,p 0.013
14. `day_sum(Ret)` — enrichment,均值差 +0.44,p 0.030
15. `day_sum(Volume)` — enrichment,均值差 +0.39,p 0.044

## 本组之前各轮的任务

- `prods2077Pr1a_Ea`:核心 `day_median(div(abs_(Ret), Amt))`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1086, 'c05_no_core': 2099}
  - score +0.34(train +0.71 valid +0.34):`cross_corr(day_median(div(abs_(Ret), Amt)), cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 20), 20)`
  - score -0.23(train -0.23 valid -0.03):`cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 20)`
  - score -0.45(train -0.45 valid +0.23):`cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 30)`
  - score -0.77(train -0.50 valid -0.77):`cross_corr(day_median(div(abs_(Ret), Amt)), cs_last_low20(pow_3(sigmoid(BoardCode)), pow_2_5(ts_mean(day_centroid(Low), 5))), 20)`
  - score -0.98(train -0.98 valid -0.54):`cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 10)`
- `prods2077Pr1b_Nb`:核心 `—`;评分 97,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.62(train -0.46 valid -0.62):`cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 10), 30), day_mean(pow_2_5(Ret)))`
  - score -0.63(train -0.39 valid -0.63):`cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_mean(pow_2_5(Ret)))`
  - score -0.99(train -0.49 valid -0.99):`cs_last_high10(pow_3(cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(pow_1_5(Vwap)))), day_gini(mul(High, Open)))`
  - score -1.13(train -0.63 valid -1.13):`cs_last_high10(pow_3(cs_last_high40(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(Low))), day_gini(Low))`
  - score -1.43(train -1.43 valid -1.41):`cs_last_high20(ts_scale(day_zero_ratio(Low), 30), day_argmin(pow_1_5(Open)))`
- `prods2077Pr2a_Ea`:核心 `day_sum(Ret)`;评分 83,过线 0,入 heads 0;采样计数 {'c05_no_core': 738, 'c05_skeleton': 343}
  - score -0.49(train -0.49 valid -0.11):`cross_cov(day_sum(Ret), day_wstd(Ret, Ret), 40)`
  - score -0.56(train -0.56 valid +0.31):`cross_cov(day_sum(Ret), day_wstd(Ret, Volume), 40)`
  - score -0.70(train -0.70 valid -0.45):`cross_corr(day_sum(Ret), sigmoid(cross_cov(day_sum(Ret), day_kurt(Amt), 40)), 30)`
  - score -1.00(train -1.00 valid -0.12):`cross_corr(day_sum(Ret), day_wstd(Ret, Volume), 30)`
  - score -1.01(train -1.01 valid -0.30):`cross_corr(day_sum(Ret), pow_2(cross_cov(day_sum(Ret), day_kurt(Amt), 40)), 30)`
- `prods2077Pr2b_Nb`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.74(train -1.74 valid -0.44):`mul(pow_05(pow_2(day_argmin(High))), inv(ts_mean(neg(ts_regbeta(LogTotalCap, day_argmax(Volume), 20)), 50)))`
  - score -1.84(train -1.84 valid -1.39):`ts_mean(ts_reg_fvalue(day_autocorr_n1(Vwap), signedpower(day_pos_ratio(Amt)), 5), 20)`
  - score -1.87(train -1.58 valid -1.87):`ts_mean(ts_pearson(day_std(sqrt(Ret)), 5), 30)`
  - score -1.96(train -1.54 valid -1.96):`ts_mean(ts_reg_fvalue(day_cov(Close, Close), signedpower(day_cov(Close, Close)), 5), 20)`
  - score -1.96(train -1.96 valid -1.92):`ts_mean(ts_pearson(day_std(sqrt(Ret)), 5), 20)`

## 比原 head 好的拆解变体(R 候选)

(没有)
