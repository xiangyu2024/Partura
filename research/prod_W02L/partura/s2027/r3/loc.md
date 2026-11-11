# 定位:种子 2027,P 组,第 3 轮(只含 train / valid)

快照:prods2027M1_I0_open_search, prods2027M2_I0_open_search, prods2027M3_I0_open_search, prods2027Pr1a_Ea, prods2027Pr1b_Nb, prods2027Pr2a_Ea, prods2027Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.13 | -0.80 | -1.13 | +1 | 20 | prods2027M3_I0_open_search | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15), 50)` |
| -1.22 | -1.20 | -1.22 | +1 | 0 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` |
| -1.34 | -1.34 | -0.83 | +1 | 5 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` |
| -1.34 | -1.19 | -1.34 | -1 | 5 | prods2027M3_I0_open_search | `day_mean(Volume)` |
| -1.34 | -1.34 | -1.31 | -1 | 20 | prods2027M3_I0_open_search | `pow_2(cross_cov(day_last(Volume), day_mean(Ret), 5))` |
| -1.85 | -1.73 | -1.85 | +1 | 0 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` |
| -2.72 | -2.72 | -1.88 | -1 | 20 | prods2027M2_I0_open_search | `rank(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0), True)` |
| -2.82 | -2.82 | -1.78 | +1 | 20 | prods2027M2_I0_open_search | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))` |
| -2.97 | -2.97 | -1.94 | -1 | 20 | prods2027M2_I0_open_search | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20)` |

## 共性:247 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.68 | 0.001 | 4 | -0.41 / -2.09 | `ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30)` |
| +1.18 | 0.000 | 22 | -0.98 / -2.17 | `inv(day_quantile_q25(Volume))` |
| +1.15 | 0.001 | 8 | -0.94 / -2.10 | `cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60)` |
| +1.11 | 0.000 | 19 | -1.04 / -2.15 | `cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120)` |
| +1.10 | 0.000 | 23 | -1.06 / -2.16 | `day_quantile_q25(Volume)` |
| +1.06 | 0.001 | 11 | -1.05 / -2.11 | `day_flat_run_max(Open)` |
| +1.01 | 0.017 | 6 | -1.08 / -2.08 | `ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60), 30), 40)` |
| +1.01 | 0.011 | 5 | -1.07 / -2.08 | `cross_ema(cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60), 20)` |
| +0.93 | 0.019 | 7 | -1.16 / -2.09 | `ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60), 30)` |
| +0.89 | 0.009 | 7 | -1.20 / -2.09 | `cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60)` |
| +0.89 | 0.000 | 15 | -1.23 / -2.11 | `day_kurt(in_slice(Ret, 11, 230))` |
| +0.85 | 0.044 | 4 | -1.23 / -2.07 | `day_corr(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240))` |
| +0.82 | 0.000 | 43 | -1.38 / -2.20 | `day_std(in_slice(Ret, 11, 230))` |
| +0.79 | 0.025 | 9 | -1.30 / -2.09 | `day_flat_run_max(Amt)` |
| +0.75 | 0.028 | 6 | -1.33 / -2.08 | `day_mean(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` |
| +0.73 | 0.000 | 69 | -1.54 / -2.26 | `cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` |
| +0.71 | 0.000 | 66 | -1.54 / -2.25 | `cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)` |
| +0.68 | 0.069 | 8 | -1.40 / -2.08 | `cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60)` |
| +0.55 | 0.117 | 7 | -1.53 / -2.08 | `cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 250)` |
| +0.34 | 0.351 | 5 | -1.73 / -2.07 | `cs_bucket_rank(LogFloatShares, cross_autocorr(day_sum(in_slice(Ret, 11, 230)), 120, 1))` |

## 拆解(19 次评估)

### head score -1.13:`ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15)` | -1.65 | -1.65 | -1.30 | — | (子树本身) |
| sufficiency | `ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50)` | -2.20 | -1.75 | -2.20 | — | (子树本身) |
| sufficiency | `cross_cov(day_mean(Vwap), day_max(High), 15)` | -2.31 | -1.84 | -2.31 | — | (子树本身) |
| sufficiency | `day_mean(Vwap)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15)` | -2.27 | -1.85 | -2.27 | +1.14 | `ts_sum(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), 50)` |
| knockout | `ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50)` | -2.02 | -1.63 | -2.02 | +0.89 | `ts_sum(cross_cov(cross_cov(day_mean(Vwap), day_max(High), 15), day_max(High), 15), 50)` |
| knockout | `cross_cov(day_mean(Vwap), day_max(High), 15)` | -2.78 | -2.07 | -2.78 | +1.65 | `ts_sum(cross_cov(ts_sum(day_mean(Vwap), 50), day_max(High), 15), 50)` |
| swap | `Vwap->Close` | -1.22 | -0.80 | -1.22 | — | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Close), day_max(High), 15), 50), day_max(High), 15), 50)` |
| swap | `High->Low` | -1.26 | -0.81 | -1.26 | — | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(Low), 15), 50), day_max(Low), 15), 50)` |
| window | `ts_sum@50->25` | -1.12 | -0.77 | -1.12 | — | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15), 25)` |
| window | `ts_sum@50->100` | -0.82 | -0.82 | -0.72 | — | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15), 100)` |

### head score -1.34:`day_mean(Volume)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.47 | -2.76 | -3.47 | — | `day_mean(Amt)` |

### head score -1.34:`pow_2(cross_cov(day_last(Volume), day_mean(Ret), 5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(day_last(Volume), day_mean(Ret), 5)` | -4.23 | -3.76 | -4.23 | — | (子树本身) |
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_mean(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| knockout | `cross_cov(day_last(Volume), day_mean(Ret), 5)` | -1.61 | -1.18 | -1.61 | +0.27 | `pow_2(day_last(Volume))` |
| swap | `Volume->Amt` | -3.09 | -3.03 | -3.09 | — | `pow_2(cross_cov(day_last(Amt), day_mean(Ret), 5))` |
| window | `cross_cov@5->2` | -1.58 | -1.50 | -1.58 | — | `pow_2(cross_cov(day_last(Volume), day_mean(Ret), 2))` |
| window | `cross_cov@5->10` | -1.63 | -1.36 | -1.63 | — | `pow_2(cross_cov(day_last(Volume), day_mean(Ret), 10))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30)` — enrichment,均值差 +1.68,p 0.001
2. `inv(day_quantile_q25(Volume))` — enrichment,均值差 +1.18,p 0.000
3. `cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60)` — enrichment,均值差 +1.15,p 0.001
4. `cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120)` — enrichment,均值差 +1.11,p 0.000
5. `day_quantile_q25(Volume)` — enrichment,均值差 +1.10,p 0.000
6. `day_flat_run_max(Open)` — enrichment,均值差 +1.06,p 0.001
7. `ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60), 30), 40)` — enrichment,均值差 +1.01,p 0.017
8. `cross_ema(cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60), 20)` — enrichment,均值差 +1.01,p 0.011
9. `ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60), 30)` — enrichment,均值差 +0.93,p 0.019
10. `cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60)` — enrichment,均值差 +0.89,p 0.009
11. `day_kurt(in_slice(Ret, 11, 230))` — enrichment,均值差 +0.89,p 0.000
12. `day_corr(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240))` — enrichment,均值差 +0.85,p 0.044
13. `day_std(in_slice(Ret, 11, 230))` — enrichment,均值差 +0.82,p 0.000
14. `day_flat_run_max(Amt)` — enrichment,均值差 +0.79,p 0.025
15. `day_mean(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` — enrichment,均值差 +0.75,p 0.028
16. `cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` — enrichment,均值差 +0.73,p 0.000
17. `cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)` — enrichment,均值差 +0.71,p 0.000
18. `cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60)` — enrichment,均值差 +0.68,p 0.069
19. `day_q_stat_std(in_slice(Ret, 11, 230), 10)` — enrichment,均值差 +0.10,p 0.073

## 本组之前各轮的任务

- `prods2027Pr1a_Ea`:核心 `day_q_stat_std(in_slice(Ret, 11, 230), 10)`;评分 69,过线 0,入 heads 0;采样计数 {'c05_no_core': 713, 'c05_skeleton': 377}
  - score -0.42(train -0.14 valid -0.42):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60), 20), 120)`
  - score -0.66(train -0.45 valid -0.66):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120)`
  - score -0.66(train -0.56 valid -0.66):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), 60), 20), 120)`
  - score -0.71(train -0.55 valid -0.71):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_autocorr(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60, 1), 120)`
  - score -0.89(train -0.89 valid -0.86):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), 120)`
- `prods2027Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -1.03(train -0.68 valid -1.03):`cross_autocorr(day_sum(in_slice(Amt, 11, 230)), 120, 1)`
  - score -1.34(train -1.20 valid -1.34):`signedpower(sub(cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, High)), ts_argmin(cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1)), 60), 30)))`
  - score -1.37(train -1.37 valid -1.30):`cross_autocorr(signedpower(sub(cs_bucket_rank(LogFloatShares, signedpower(day_argmax(Ret))), ts_argmin(cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1)), 5), 30))), 120, 1)`
  - score -1.44(train -1.44 valid -1.31):`signedpower(sub(cs_bucket_rank(LogFloatShares, day_signed_ratio(High, High)), ts_argmin(cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, High)), 30)))`
  - score -1.48(train -1.07 valid -1.48):`signedpower(sub(cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, Ret)), ts_argmin(day_sum(in_slice(Ret, 11, 230)), 30)))`
- `prods2027Pr2a_Ea`:核心 `cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)`;评分 80,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 26, 'c05_no_core': 1134, 'c05_skeleton': 621, 'mutation_refused': 6}
  - score -0.65(train -0.39 valid -0.65):`cross_regbeta(day_kurt(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120)`
  - score -0.66(train -0.45 valid -0.66):`sub(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), cross_regbeta(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 250))`
  - score -0.67(train -0.46 valid -0.67):`sub(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20))`
  - score -0.72(train -0.45 valid -0.72):`sub(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), cross_regbeta(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60), 250))`
  - score -0.75(train -0.51 valid -0.75):`sub(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), 60), 20), 120), cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 250))`
- `prods2027Pr2b_Nb`:核心 `—`;评分 82,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.18(train -0.18 valid +0.11):`ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60), 30), 40), 60), 30), 40)`
  - score -0.24(train -0.24 valid -0.09):`ts_mean(ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 40), 40)`
  - score -0.25(train -0.25 valid -0.25):`ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, ts_mean(cross_reg_fvalue(ListAge, ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Amt), 60), 30), 40), 60), 40), 60), 30), 40)`
  - score -0.28(train -0.28 valid -0.20):`ts_mean(ts_cov(inv(day_quantile_q25(Volume)), ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 30), 40)`
  - score -0.31(train -0.31 valid -0.17):`ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, ts_mean(ts_cov(inv(day_quantile_q25(Volume)), ListAge, 30), 40), 60), 30), 40)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.31(window ts_sum@50->100):`ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(High), 15), 50), day_max(High), 15), 100)`
