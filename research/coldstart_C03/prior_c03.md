# C03 的先验知识:C01 与 C02 的样本内结果(只含 train / valid;没有任何测试段数字)

C01:A = GP 盲搜,B = Partura v1(先验 + 邻域);C02:A = GP 盲搜 + 相关度拒绝,B = Partura v2(假设直接测 + 设计初始种群 + GP 精修)。
两个实验的奖励都是 `long`(没有中性化)。C03 换成 `long_neutral`:这些 head 在新奖励下的分数未知,很多会掉(它们大多带风格暴露)。
更多:C01 的 beliefs_r2/r3.md、cards_r*;C02 的 hypotheses_r1.yaml、direct_r1.md、design_r1.md、beliefs_r1.md。

## C01 的全部 heads(各运行内去重,48 个;C03 的新 head 必须与它们 \|ρ\| < 0.7)

| 运行 | 组 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|
| c01r1s104_I0_open_search | control | +2.72 | +2.82 | +2.72 | 20 | -1 | 0.026 | +0.16 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)), day_std(Close)))))` |
| c01r1s104_I0_open_search | control | +2.63 | +2.63 | +3.66 | 20 | -1 | 0.033 | +0.36 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Vwap))))` |
| c01r1s104_I0_open_search | control | +2.53 | +2.53 | +3.10 | 20 | -1 | 0.031 | -0.12 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(sub(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| c01r1s104_I0_open_search | control | +2.51 | +2.51 | +3.15 | 20 | -1 | 0.040 | +0.26 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| c01r1s104_I0_open_search | control | +2.43 | +2.43 | +3.51 | 20 | -1 | 0.037 | +0.28 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| c01r2s203B_C2a_when_the_return_arrives | steer | +2.32 | +2.32 | +3.36 | 5 | -1 | 0.063 | +0.38 | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, Close)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| c01r1s104_I0_open_search | control | +2.30 | +2.30 | +2.87 | 20 | -1 | 0.041 | +0.43 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Amt), day_std(Close)), day_std(Amt))))` |
| c01r1s103_I0_open_search | control | +2.25 | +2.68 | +2.25 | 20 | -1 | 0.042 | +0.23 | `cs_first_low20(day_open(Amt), day_pos_ratio(Ret))` |
| c01r1s104_I0_open_search | control | +2.20 | +2.20 | +3.70 | 20 | -1 | 0.037 | +0.12 | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_distinct_ratio(Vwap), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret))))` |
| c01r3s308A_I0_open_search | control | +2.05 | +2.05 | +3.38 | 20 | -1 | 0.023 | +0.32 | `cross_scale(mul(signedpower(day_std(Volume)), day_first(Volume)), 241)` |
| c01r2s201A_I0_open_search | control | +1.99 | +1.99 | +3.16 | 20 | +1 | 0.040 | +0.23 | `ts_pearson(log(log(log(pow_1_5(day_sum(Close))))), 10)` |
| c01r3s301A_I0_open_search | control | +1.98 | +1.98 | +3.07 | 20 | +1 | 0.041 | +0.23 | `signedpower(signedpower(ts_spearman(day_wmean(Open, Open), 10)))` |
| c01r2s202A_I0_open_search | control | +1.95 | +1.95 | +3.15 | 5 | -1 | 0.046 | +0.25 | `ts_decay_linear(cs_first_low40(day_open(Amt), cs_scale(day_cov(pow_05(Ret), Ret))), 10)` |
| c01r3s302A_I0_open_search | control | +1.94 | +1.94 | +2.64 | 20 | +1 | 0.026 | +0.32 | `ts_spearman(sqrt(log(day_close(High))), 30)` |
| c01r1s104_I0_open_search | control | +1.90 | +2.08 | +1.90 | 20 | -1 | 0.032 | +0.07 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(day_std(Vwap))))` |
| c01r2s204A_I0_open_search | control | +1.88 | +1.88 | +2.81 | 5 | +1 | 0.046 | +0.30 | `cs_normalize(add(log(pow_2(ts_spearman(day_open(Vwap), 30))), cs_quantile_q50(log(pow_2(ts_spearman(day_open(Vwap), 30))))))` |
| c01r2s207A_I0_open_search | control | +1.88 | +1.88 | +2.19 | 20 | -1 | 0.023 | +0.31 | `log(abs_(log(abs_(ts_spearman(day_topw_mean(Low, nt_cs_winsor(Amt)), 40)))))` |
| c01r2s203B_C2a_when_the_return_arrives | steer | +1.87 | +1.87 | +4.02 | 20 | -1 | 0.048 | +0.07 | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, mul(Amt, Amt))))), day_sum(Ret)), day_distinct_ratio(mul(Amt, Amt)))` |
| c01r1s104_I0_open_search | control | +1.82 | +1.82 | +3.31 | 5 | -1 | 0.024 | +0.31 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_min(Close)), day_min(Close))))` |
| c01r2s204A_I0_open_search | control | +1.78 | +1.78 | +3.16 | 5 | -1 | 0.023 | +0.26 | `sub(cs_first_low20(pow_1_5(signedpower(day_open(Vwap))), signedpower(day_open(Vwap))), cross_ema(ts_spearman(day_open(Vwap), 30), 5))` |
| c01r1s107_I0_open_search | control | +1.76 | +1.76 | +2.39 | 20 | -1 | 0.070 | +0.23 | `cs_demean(cs_mask_top_replace_mean_neg(cs_winsor(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_std(Open))))))` |
| c01r3s301A_I0_open_search | control | +1.74 | +1.74 | +2.07 | 0 | +1 | 0.063 | +0.33 | `signedpower(ts_spearman(day_wmean(Open, Volume), 50))` |
| c01r3s308A_I0_open_search | control | +1.74 | +1.74 | +2.84 | 20 | +1 | 0.045 | +0.18 | `cs_bucket_demean(ts_pearson(ts_med(day_max(Vwap), 1), 10), day_argmax(Ret))` |
| c01r2s207A_I0_open_search | control | +1.72 | +1.72 | +2.78 | 20 | -1 | 0.044 | +0.20 | `log(log(abs_(ts_spearman(day_topw_mean(Low, Amt), 10))))` |
| c01r1s103_I0_open_search | control | +1.71 | +1.71 | +2.86 | 20 | -1 | 0.051 | +0.03 | `cs_first_low20(day_open(Amt), day_distinct_ratio(Amt))` |
| c01r2s204A_I0_open_search | control | +1.70 | +1.70 | +1.96 | 20 | -1 | 0.117 | +0.40 | `cs_normalize(add(log(log(day_wmean(Amt, High))), cs_quantile_q50(log(cs_regres(day_gini(High), day_zero_ratio(Open))))))` |
| c01r2s202A_I0_open_search | control | +1.58 | +1.58 | +3.73 | 5 | -1 | 0.037 | +0.29 | `ts_decay_linear(cs_first_low40(day_open(Amt), cs_first_low40(day_open(Amt), day_median(Open))), 10)` |
| c01r1s104_I0_open_search | control | +1.57 | +1.76 | +1.57 | 20 | -1 | 0.070 | -0.00 | `cs_mask_top_replace_mean_neg(cs_bucket_zscore(pow_2(cs_robust_z(pow_05(day_gini(Amt)))), ts_scale(pow_2_5(cross_tail_mean_q75(day_argmin(Vwap), 3)), 1)))` |
| c01r2s204A_I0_open_search | control | +1.56 | +1.56 | +2.63 | 20 | -1 | 0.045 | +0.15 | `sub(cs_first_low20(pow_1_5(sub(pow_2_5(day_wmean(Amt, Volume)), cross_ema(day_topw_mean(Low, Close), 60))), sub(pow_2_5(day_wmean(Amt, Volume)), cross_ema(day_topw_mean(Low, Close), 60))), cross_ema(ts_spearman(day_open(Vwap), 30), 5))` |
| c01r2s201A_I0_open_search | control | +1.52 | +1.52 | +2.39 | 20 | +1 | 0.037 | +0.24 | `ts_pearson(ts_pearson(day_sum(Close), 20), 10)` |
| c01r2s201A_I0_open_search | control | +1.51 | +1.51 | +3.06 | 5 | +1 | 0.069 | +0.23 | `ts_pearson(ts_pearson(ts_pearson(pow_05(day_sum(Close)), 10), 10), 10)` |
| c01r3s302A_I0_open_search | control | +1.44 | +1.44 | +3.03 | 5 | +1 | 0.047 | +0.24 | `ts_spearman(log(ts_spearman(log(day_close(Low)), 10)), 30)` |
| c01r1s104_I0_open_search | control | +1.42 | +1.42 | +2.23 | 20 | -1 | 0.048 | +0.31 | `cs_mask_top_replace_mean_neg(inv(div(div(day_std(Close), day_std(Vwap)), cs_mask_top_replace_mean_neg(inv(div(div(day_std(Close), day_std(Vwap)), day_std(Vwap)))))))` |
| c01r2s201A_I0_open_search | control | +1.39 | +1.39 | +2.76 | 5 | +1 | 0.082 | +0.21 | `ts_pearson(abs_(log(ts_pearson(day_sum(Close), 10))), 10)` |
| c01r3s302A_I0_open_search | control | +1.35 | +1.35 | +2.72 | 5 | +1 | 0.047 | +0.31 | `ts_spearman(log(day_close(cross_zscore(Open, 15))), 30)` |
| c01r2s204A_I0_open_search | control | +1.35 | +1.35 | +2.66 | 20 | -1 | 0.033 | +0.34 | `cs_first_low20(pow_1_5(day_first(Amt)), pow_2_5(day_open(Vwap)))` |
| c01r2s204A_I0_open_search | control | +1.34 | +1.34 | +2.37 | 0 | +1 | 0.017 | +0.37 | `cross_ema(cs_normalize(ts_spearman(day_open(Vwap), 30)), 60)` |
| c01r3s306B_I0_open_search | steer | +1.23 | +1.23 | +1.35 | 5 | -1 | 0.008 | +0.09 | `ts_product(cross_quantile_q25(pow_2(day_kurt(High)), 30), 50)` |
| c01r1s104_I0_open_search | control | +1.20 | +1.20 | +2.44 | 20 | -1 | 0.043 | +0.41 | `cs_mask_top_replace_mean_neg(inv(div(div(div(inv(div(div(day_distinct_ratio(Vwap), day_std(Vwap)), day_std(Vwap))), day_std(Close)), day_std(Close)), day_std(Close))))` |
| c01r2s204A_I0_open_search | control | +1.18 | +1.18 | +2.63 | 0 | +1 | 0.052 | +0.33 | `cs_first_low20(pow_1_5(pow_2(ts_spearman(day_open(Vwap), 30))), pow_2_5(day_open(Vwap)))` |
| c01r1s105_I0_open_search | control | +1.16 | +1.16 | +3.51 | 5 | -1 | 0.019 | +0.39 | `day_median(nt_cs_last_high40(Vwap, nt_cs_last_high40(Vwap, Close)))` |
| c01r3s302A_I0_open_search | control | +1.14 | +1.14 | +2.17 | 20 | +1 | 0.025 | +0.23 | `ts_spearman(log(ts_spearman(day_wmean(cross_zscore(Open, 15), cross_scale(Amt, 15)), 30)), 30)` |
| c01r1s105_I0_open_search | control | +1.07 | +1.07 | +1.53 | 20 | +1 | 0.014 | +0.20 | `day_median(nt_cs_first_high40(High, nt_cs_last_high40(Ret, Close)))` |
| c01r3s308A_I0_open_search | control | +1.06 | +2.20 | +1.06 | 20 | -1 | 0.024 | +0.47 | `mul(signedpower(cross_scale(day_first(Volume), 241)), day_first(Volume))` |
| c01r3s305B_I0_open_search | steer | +1.05 | +1.05 | +1.76 | 5 | +1 | 0.055 | +0.28 | `ts_reg_tvalue(div(day_autocorr_n1(Vwap), day_flat_ratio(Close)), cs_state_rank(day_autocorr_n1(Vwap), 5), 30)` |
| c01r3s304A_I0_open_search | control | +1.03 | +1.03 | +2.51 | 20 | +1 | 0.021 | +0.42 | `neg(cs_last_low40(day_min(Amt), day_std(Volume)))` |
| c01r3s304A_I0_open_search | control | +1.03 | +1.03 | +2.50 | 5 | +1 | 0.072 | -0.02 | `ts_min(cs_last_low40(neg(cs_last_low40(ts_min(day_var(Amt), 1), ts_min(day_var(Amt), 1))), day_std(Volume)), 1)` |
| c01r1s103_I0_open_search | control | +1.02 | +1.02 | +2.36 | 20 | -1 | 0.062 | +0.09 | `cs_first_low20(day_distinct_ratio(Close), day_distinct_ratio(Close))` |

## C02 的全部 heads(各运行内去重,49 个;C03 的新 head 必须与它们 \|ρ\| < 0.7)

| 运行 | 组 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|
| c02r1s401B_C2a_slow_intraday_reversal | steer | +2.24 | +2.24 | +3.33 | 5 | -1 | 0.075 | +0.39 | `div(day_last(Close), day_sum(pow_3(log(Close))))` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +1.85 | +1.85 | +3.46 | 5 | +1 | 0.042 | +0.33 | `pow_05(ts_pearson(day_sum(Ret), 30))` |
| c02r1s405B_C2b_return_shape_and_tug | steer | +1.75 | +1.75 | +3.38 | 5 | +1 | 0.042 | +0.33 | `ts_pearson(day_sum(Ret), 30)` |
| c02r1s406B_C2b_return_shape_and_tug | steer | +1.75 | +1.75 | +3.38 | 5 | +1 | 0.042 | +0.33 | `ts_pearson(day_sum(Ret), 30)` |
| c02r1s407B_C2b_return_shape_and_tug | steer | +1.75 | +1.75 | +3.38 | 5 | +1 | 0.042 | +0.33 | `ts_pearson(day_sum(Ret), 30)` |
| c02r1s406A_I0_open_search | control | +1.70 | +1.70 | +2.26 | 5 | -1 | 0.015 | +0.12 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(add(abs_(day_skew(Open)), day_max(Vwap)), day_argmax(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.61 | +1.61 | +2.14 | 5 | -1 | 0.016 | +0.10 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(add(abs_(day_skew(Open)), pow_1_5(day_first(Amt))), day_argmax(Ret), 40), 241))` |
| c02r1s401B_C2a_slow_intraday_reversal | steer | +1.58 | +1.58 | +3.00 | 0 | -1 | 0.022 | +0.33 | `cross_ema(cross_scale(day_last(Close), 15), 241)` |
| c02r1s406A_I0_open_search | control | +1.57 | +1.57 | +3.45 | 0 | -1 | 0.016 | +0.16 | `cs_rank(cross_regbeta(pow_1_5(pow_1_5(day_first(Amt))), ts_reg_tvalue(pow_1_5(pow_1_5(day_first(Amt))), abs_(day_skew(Open)), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.57 | +1.57 | +1.99 | 5 | -1 | 0.017 | +0.00 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(add(abs_(day_skew(Open)), day_max(Vwap)), day_hurst(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.49 | +1.49 | +2.79 | 5 | -1 | 0.015 | +0.37 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), day_argmax(Ret), 241))` |
| c02r1s406A_I0_open_search | control | +1.48 | +1.48 | +2.40 | 5 | -1 | 0.016 | +0.10 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_tvalue(pow_1_5(day_first(Amt)), day_argmax(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.46 | +1.46 | +3.11 | 0 | +1 | 0.017 | +0.19 | `cs_rank(cross_regbeta(pow_1_5(pow_1_5(day_first(Amt))), ts_reg_tvalue(pow_1_5(pow_1_5(day_first(Amt))), day_argmax(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.45 | +1.45 | +2.36 | 5 | -1 | 0.017 | +0.01 | `cs_rank(cross_regbeta(pow_1_5(pow_1_5(day_first(Amt))), ts_reg_fvalue(day_es_ratio_hi(Close), day_durbin_watson(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.44 | +1.44 | +3.09 | 0 | -1 | 0.023 | +0.13 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(day_es_ratio_hi(Close), day_argmax(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.35 | +1.35 | +1.58 | 5 | +1 | 0.017 | -0.14 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(add(abs_(day_skew(Amt)), day_max(Vwap)), day_argmax(Ret), 40), 241))` |
| c02r1s406A_I0_open_search | control | +1.34 | +1.34 | +2.56 | 0 | -1 | 0.020 | +0.03 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), cross_regbeta(pow_1_5(day_first(Amt)), abs_(day_skew(Open)), 241), 241))` |
| c02r1s406A_I0_open_search | control | +1.33 | +1.33 | +3.07 | 5 | +1 | 0.014 | +0.32 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), abs_(day_skew(Open)), 241))` |
| c02r1s406A_I0_open_search | control | +1.33 | +1.33 | +2.48 | 5 | +1 | 0.016 | +0.31 | `cs_last_low40(cross_regbeta(pow_1_5(pow_1_5(day_first(Amt))), ts_reg_fvalue(day_flat_ratio(Close), day_durbin_watson(Ret), 40), 241), neg(day_last(Open)))` |
| c02r1s403A_I0_open_search | control | +1.22 | +1.38 | +1.22 | 20 | -1 | 0.047 | -0.13 | `add(cs_first_high20(day_quantile_q25(Ret), day_std(Ret)), -5)` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +1.11 | +1.11 | +2.72 | 20 | +1 | 0.021 | +0.15 | `ts_pearson(log(ts_pearson(day_sum(Ret), 30)), 50)` |
| c02r1s406A_I0_open_search | control | +1.10 | +1.10 | +3.16 | 5 | -1 | 0.015 | +0.04 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(add(abs_(day_skew(Open)), day_max(Vwap)), cross_regbeta(pow_1_5(day_first(Amt)), abs_(day_skew(Open)), 241), 40), 241))` |
| c02r1s403B_C2a_slow_intraday_reversal | steer | +1.09 | +1.09 | +1.14 | 5 | -1 | 0.038 | +0.33 | `cross_ema(log(div(day_last(Low), day_first(Open))), 30)` |
| c02r1s406A_I0_open_search | control | +1.09 | +1.73 | +1.09 | 5 | -1 | 0.017 | +0.19 | `cs_rank(cross_regbeta(pow_1_5(day_first(Amt)), neg(day_last(Open)), 241))` |
| c02r1s401B_C2a_slow_intraday_reversal | steer | +1.04 | +1.04 | +1.25 | 20 | -1 | 0.038 | +0.11 | `pow_2(cross_scale(day_last(log(Open)), 30))` |
| c02r1s407B_C2b_return_shape_and_tug | steer | +1.02 | +1.02 | +1.65 | 20 | -1 | 0.044 | +0.05 | `ts_skew(log(div(day_last(Close), day_first(in_first(log(High))))), 40)` |
| c02r1s403B_C2a_slow_intraday_reversal | steer | +1.01 | +1.01 | +1.26 | 20 | -1 | 0.035 | +0.17 | `ts_scale(log(sqrt(day_max(Close))), 40)` |
| c02r1s401B_C2a_slow_intraday_reversal | steer | +1.00 | +1.00 | +2.18 | 20 | -1 | 0.020 | +0.22 | `div(cross_ema(log(div(day_last(Close), day_first(Open))), 30), day_min(pow_3(log(Close))))` |
| c02r1s407B_C2b_return_shape_and_tug | steer | +1.00 | +1.00 | +3.00 | 5 | +1 | 0.041 | +0.18 | `div(ts_pearson(day_mean(Ret), 20), day_first(in_first(log(High))))` |
| c02r1s402B_C2a_slow_intraday_reversal | steer | +0.98 | +0.99 | +0.98 | 5 | -1 | 0.038 | +0.30 | `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` |
| c02r1s404B_C2a_slow_intraday_reversal | steer | +0.98 | +0.99 | +0.98 | 5 | -1 | 0.038 | +0.30 | `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` |
| c02r1s404B_C2a_slow_intraday_reversal | steer | +0.97 | +0.97 | +1.42 | 20 | -1 | 0.038 | +0.12 | `ts_scale(sqrt(day_mean(sigmoid(log(sqrt(Vwap))))), 30)` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +0.95 | +0.95 | +1.80 | 5 | +1 | 0.053 | +0.09 | `pow_05(ts_pearson(day_skew(Ret), 30))` |
| c02r1s402B_C2a_slow_intraday_reversal | steer | +0.92 | +0.92 | +1.24 | 20 | -1 | 0.039 | +0.12 | `abs_(ts_scale(sqrt(day_mean(log(Low))), 30))` |
| c02r1s405B_C2b_return_shape_and_tug | steer | +0.87 | +0.87 | +1.74 | 5 | +1 | 0.053 | +0.09 | `ts_pearson(day_skew(Ret), 30)` |
| c02r1s406B_C2b_return_shape_and_tug | steer | +0.87 | +0.87 | +1.74 | 5 | +1 | 0.053 | +0.09 | `ts_pearson(day_skew(Ret), 30)` |
| c02r1s407B_C2b_return_shape_and_tug | steer | +0.87 | +0.87 | +3.02 | 5 | +1 | 0.056 | +0.22 | `ts_pearson(div(ts_pearson(day_mean(Ret), 20), day_first(in_first(log(High)))), 20)` |
| c02r1s404A_I0_open_search | control | +0.86 | +0.86 | +1.40 | 20 | +1 | 0.041 | +0.16 | `ts_quantile_q75(ts_reg_tvalue(day_first(Amt), day_gini(Low), 10), 10)` |
| c02r1s406A_I0_open_search | control | +0.81 | +0.81 | +2.33 | 5 | -1 | 0.014 | +0.01 | `cs_rank(cross_regbeta(cs_last_low40(cross_regbeta(pow_1_5(day_first(Amt)), ts_reg_fvalue(day_es_ratio_hi(Close), day_durbin_watson(Ret), 40), 241), neg(day_last(Open))), ts_reg_tvalue(pow_1_5(pow_1_5(day_first(Amt))), day_argmax(Ret), 40), 241))` |
| c02r1s408A_I0_open_search | control | +0.79 | +0.79 | +0.83 | 20 | +1 | 0.024 | +0.24 | `ts_regalpha(cross_regres(ts_stddev(day_sum(Low), 50), pow_1_5(day_at_max_ratio(High)), 5), cs_last_high40(pow_05(pow_3(day_max(in_max(Low)))), cs_regres(day_quantile_q25(Close), day_at_max_ratio(Volume))), 5)` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +0.79 | +0.79 | +2.16 | 20 | +1 | 0.027 | +0.16 | `ts_pearson(pow_05(ts_pearson(day_sum(Ret), 50)), 30)` |
| c02r1s402A_I0_open_search | control | +0.78 | +0.78 | +1.54 | 0 | -1 | 0.011 | +0.44 | `ts_max(sub(day_last(sqrt(Vwap)), day_autocorr_n1(Vwap)), 20)` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +0.78 | +0.78 | +1.65 | 20 | +1 | 0.027 | +0.19 | `pow_05(ts_pearson(pow_05(ts_pearson(day_pos_ratio(Ret), 30)), 30))` |
| c02r1s406B_C2b_return_shape_and_tug | steer | +0.78 | +0.78 | +0.96 | 20 | -1 | 0.034 | +0.17 | `ts_decay_linear(day_sum(Ret), 30)` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +0.74 | +0.74 | +3.76 | 5 | +1 | 0.049 | +0.16 | `pow_05(ts_pearson(pow_05(ts_pearson(day_sum(Ret), 30)), 30))` |
| c02r1s408A_I0_open_search | control | +0.74 | +0.74 | +0.80 | 20 | -1 | 0.031 | +0.16 | `ts_regalpha(cross_regres(ts_stddev(day_sum(Low), 50), pow_1_5(pow_3(day_max(in_max(Vwap)))), 5), cs_last_high40(ts_quantile_q50(day_skew(Close), 30), cs_regres(day_cov(Vwap, Ret), day_at_max_ratio(Volume))), 5)` |
| c02r1s407B_C2b_return_shape_and_tug | steer | +0.72 | +0.72 | +1.56 | 20 | -1 | 0.035 | +0.06 | `ts_skew(log(div(day_last(log(High)), day_sum(log(log(High))))), 40)` |
| c02r1s407B_C2b_return_shape_and_tug | steer | +0.72 | +0.72 | +1.33 | 20 | +1 | 0.035 | +0.19 | `ts_skew(ts_pearson(day_mean(Ret), 5), 40)` |
| c02r1s408B_C2b_return_shape_and_tug | steer | +0.72 | +0.72 | +2.07 | 20 | -1 | 0.045 | +0.08 | `ts_skew(ts_delay(day_last(Close), 1), 40)` |

