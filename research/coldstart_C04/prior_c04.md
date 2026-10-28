# C04 的先验知识:C01、C02、C03 的样本内结果(只含 train / valid;没有任何测试段数字)

C01:A = GP 盲搜,B = Partura v1(先验 + 邻域);C02:A = GP 盲搜 + 相关度拒绝,B = Partura v2(假设直接测 + 设计初始种群 + GP 精修);C03:同 C02 的两组,奖励换成 `long_neutral`(对流动性 / 波动 / 20 日反转 / 已知族做截面中性化后的残差书)。
C01、C02 的奖励是 `long`(没有中性化),它们的 head 在 C04 的奖励下分数未知,很多会掉(大多带风格暴露)。C04 的奖励在 C03 的控制变量上再加市值 `LogFloatCap`:C03 的 head 也可能部分是市值暴露。
更多:C01 的 beliefs_r2/r3.md、cards_r*;C02、C03 的 hypotheses_r1.yaml、direct_r1.md、design_r1.md、beliefs_r1.md。

## C01 的全部 heads(各运行内去重,48 个;C04 的新 head 必须与它们 \|ρ\| < 0.7)

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

## C02 的全部 heads(各运行内去重,49 个;C04 的新 head 必须与它们 \|ρ\| < 0.7)

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

## C03 的全部 heads(各运行内去重,71 个;C04 的新 head 必须与它们 \|ρ\| < 0.7)

| 运行 | 组 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|
| c03r1s602A_I0_open_search | control | +1.49 | +1.49 | +3.19 | 5 | +1 | 0.041 | -0.18 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(pow_2(day_close(Open))))` |
| c03r1s602A_I0_open_search | control | +1.45 | +1.45 | +3.35 | 5 | +1 | 0.035 | -0.02 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(pow_2(cs_mask_top_replace_mean_neg(pow_2(day_mean(Open))))))` |
| c03r1s604B_C2a_volume_backed_minutes | steer | +1.43 | +1.43 | +1.56 | 5 | +1 | 0.052 | -0.18 | `cross_mean(day_corr(Volume, div(Ret, Volume)), 60)` |
| c03r1s603A_I0_open_search | control | +1.40 | +1.40 | +2.17 | 0 | +1 | 0.057 | -0.32 | `ts_min(cs_last_high40(cs_scale(cs_last_high40(cs_scale(day_autocorr_n1(Ret)), cross_regalpha(cross_regalpha(day_open(Amt), day_ar1_coefficient(Ret), 15), day_centroid(Volume), 241))), cross_regalpha(day_open(Amt), day_centroid(Volume), 241)), 20)` |
| c03r1s603B_C2a_volume_backed_minutes | steer | +1.36 | +1.45 | +1.36 | 5 | +1 | 0.042 | -0.22 | `cross_mean(day_corr(div(Ret, Volume), Volume), 241)` |
| c03r1s603B_C2a_volume_backed_minutes | steer | +1.29 | +1.33 | +1.29 | 0 | +1 | 0.045 | -0.19 | `cross_sum(cross_mean(day_corr(Volume, div(Ret, Volume)), 60), 30)` |
| c03r1s612A_I0_open_search | control | +1.20 | +1.20 | +1.45 | 5 | -1 | 0.077 | -0.48 | `ts_mean(pow_3(ts_mean(day_centroid(Volume), 10)), 10)` |
| c03r1s610A_I0_open_search | control | +1.14 | +1.14 | +1.57 | 20 | -1 | 0.066 | +0.02 | `signedpower(cs_normalize(abs_(cs_normalize(abs_(signedpower(abs_(day_sum(Ret))))))))` |
| c03r1s602B_C2a_volume_backed_minutes | steer | +1.13 | +1.15 | +1.13 | 5 | -1 | 0.077 | -0.49 | `cross_ema(cross_ema(day_centroid(Volume), 3), 3)` |
| c03r1s608A_I0_open_search | control | +1.09 | +1.09 | +2.88 | 20 | -1 | 0.039 | -0.22 | `sigmoid(signedpower(sigmoid(signedpower(pow_3(ts_skew(sigmoid(cs_first_high40(day_cov(Vwap, Amt), pow_3(ts_skew(day_ar1_coefficient(Ret), 50)))), 50))))))` |
| c03r1s605A_I0_open_search | control | +1.06 | +1.06 | +1.50 | 0 | +1 | 0.040 | -0.08 | `cross_sum(signedpower(cs_last_low40(cross_sum(signedpower(cs_last_low40(day_argmax(Low), cross_sum(neg(signedpower(cs_last_low40(day_argmax(Low), cs_last_low40(day_argmax(Low), day_kurt(Close))))), 60))), 60), cross_sum(neg(signedpower(cs_last_low40(day_argmax(Low), cs_last_low40(day_argmax(Low), day_kurt(Close))))), 60))), 60)` |
| c03r1s611A_I0_open_search | control | +1.06 | +1.57 | +1.06 | 0 | +1 | 0.048 | -0.14 | `ts_decay_linear(ts_decay_linear(ts_product(cross_reg_tvalue(day_topw_mean(Volume, Volume), day_centroid(Ret), 60), 10), 10), 10)` |
| c03r1s608A_I0_open_search | control | +1.04 | +1.04 | +1.87 | 5 | +1 | 0.088 | -0.43 | `sigmoid(cs_first_high40(day_cov(Amt, Amt), pow_3(ts_skew(day_ar1_coefficient(Ret), 50))))` |
| c03r1s602A_I0_open_search | control | +0.99 | +0.99 | +1.01 | 20 | -1 | 0.067 | +0.11 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(pow_2(day_durbin_watson(Open))))` |
| c03r1s603A_I0_open_search | control | +0.91 | +0.91 | +1.53 | 5 | -1 | 0.038 | +0.07 | `ts_min(ts_min(cs_last_high40(cs_scale(day_autocorr_n1(Volume)), cs_last_high40(cs_scale(day_autocorr_n1(Ret)), cross_regalpha(cs_last_high40(cs_scale(day_autocorr_n1(Volume)), cs_last_high40(cs_scale(day_autocorr_n1(Ret)), cross_regalpha(day_open(Amt), day_centroid(Volume), 241))), day_centroid(Volume), 241))), 20), 20)` |
| c03r1s602A_I0_open_search | control | +0.90 | +0.90 | +2.65 | 20 | +1 | 0.030 | +0.08 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(pow_2(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(pow_2(day_mean(Open)))))))` |
| c03r1s612A_I0_open_search | control | +0.89 | +0.89 | +0.92 | 20 | -1 | 0.067 | -0.09 | `ts_mean(cross_regres(day_argmax(Vwap), pow_3(day_centroid(Volume)), 241), 10)` |
| c03r1s611A_I0_open_search | control | +0.88 | +0.88 | +1.12 | 20 | +1 | 0.033 | -0.10 | `ts_product(cross_reg_tvalue(cross_reg_tvalue(day_topw_mean(Vwap, Volume), day_centroid(Ret), 5), day_centroid(Ret), 60), 10)` |
| c03r1s608A_I0_open_search | control | +0.88 | +0.88 | +1.97 | 0 | -1 | 0.072 | -0.05 | `sigmoid(signedpower(pow_3(ts_skew(sigmoid(cs_first_high40(day_cov(Vwap, Amt), pow_3(ts_skew(day_ar1_coefficient(Amt), 50)))), 50))))` |
| c03r1s603A_I0_open_search | control | +0.85 | +0.85 | +1.44 | 0 | +1 | 0.072 | -0.14 | `ts_min(cs_last_high40(cs_scale(day_autocorr_n1(Ret)), cross_regalpha(cross_regalpha(day_open(Amt), day_ar1_coefficient(Ret), 10), day_centroid(Volume), 241)), 20)` |
| c03r1s611A_I0_open_search | control | +0.84 | +0.84 | +2.91 | 5 | +1 | 0.045 | -0.28 | `ts_product(cross_reg_tvalue(day_topw_mean(Volume, Volume), day_open(Amt), 60), 10)` |
| c03r1s615A_I0_open_search | control | +0.84 | +0.84 | +1.60 | 20 | +1 | 0.023 | +0.01 | `inv(sigmoid(ts_scale(day_corr(Low, Volume), 30)))` |
| c03r1s601A_I0_open_search | control | +0.82 | +0.86 | +0.82 | 5 | -1 | 0.073 | +0.19 | `pow_2_5(cross_reg_fvalue(pow_2_5(pow_1_5(day_last(Open))), day_var(Ret), 15))` |
| c03r1s611A_I0_open_search | control | +0.79 | +0.79 | +1.71 | 0 | -1 | 0.062 | -0.24 | `ts_quantile_q75(cross_reg_tvalue(day_topw_mean(Volume, Volume), day_centroid(Ret), 60), 10)` |
| c03r1s602B_C2a_volume_backed_minutes | steer | +0.76 | +0.76 | +1.37 | 5 | -1 | 0.068 | -0.48 | `cross_min(cs_scale(cross_min(cs_scale(cross_ema(cross_min(cs_scale(cross_ema(day_centroid(Volume), 3)), 10), 3)), 10)), 10)` |
| c03r1s608A_I0_open_search | control | +0.76 | +0.76 | +2.56 | 20 | +1 | 0.032 | +0.15 | `sigmoid(signedpower(pow_3(ts_skew(sigmoid(cs_first_high40(day_cov(Vwap, Amt), pow_3(signedpower(pow_3(ts_skew(sigmoid(cs_first_high40(day_cov(Vwap, Amt), pow_3(ts_skew(day_ar1_coefficient(Ret), 50)))), 50)))))), 50))))` |
| c03r1s605A_I0_open_search | control | +0.73 | +0.73 | +2.50 | 20 | -1 | 0.042 | -0.04 | `cross_sum(signedpower(signedpower(signedpower(cs_last_low40(day_argmax(Low), day_kurt(Low))))), 60)` |
| c03r1s601A_I0_open_search | control | +0.73 | +0.73 | +0.93 | 5 | -1 | 0.058 | +0.16 | `pow_2_5(cross_reg_fvalue(cross_reg_fvalue(pow_2_5(pow_1_5(day_last(Open))), day_var(Ret), 3), day_var(Ret), 60))` |
| c03r1s603A_I0_open_search | control | +0.72 | +0.72 | +1.53 | 20 | +1 | 0.051 | +0.15 | `ts_min(cs_last_high40(ts_min(day_autocorr_n1(Ret), 20), cross_regalpha(day_open(Amt), day_ar1_coefficient(Ret), 15)), 20)` |
| c03r1s612B_C2b_intraday_jumpiness | steer | +0.72 | +0.72 | +1.73 | 0 | -1 | 0.065 | +0.28 | `div(cross_stddev(day_std(Ret), 60), cross_mean(day_es_ratio_hi(Ret), 60))` |
| c03r1s612A_I0_open_search | control | +0.70 | +0.70 | +1.02 | 20 | -1 | 0.055 | -0.11 | `ts_mean(cross_regres(cross_regres(day_argmax(Close), pow_3(day_centroid(Volume)), 241), day_centroid(Volume), 241), 10)` |
| c03r1s614A_I0_open_search | control | +0.67 | +0.67 | +0.82 | 0 | +1 | 0.042 | -0.18 | `sqrt(cs_last_low40(day_quantile_q25(Vwap), day_quantile_q25(Vwap)))` |
| c03r1s616B_C2b_intraday_jumpiness | steer | +0.67 | +0.67 | +1.57 | 0 | -1 | 0.080 | +0.26 | `div(cross_stddev(day_var(Ret), 60), cross_mean(day_es_ratio_hi(Ret), 60))` |
| c03r1s603A_I0_open_search | control | +0.66 | +0.71 | +0.66 | 0 | +1 | 0.072 | -0.04 | `ts_min(cs_last_high40(cs_scale(day_autocorr_n1(Ret)), cross_regalpha(cross_regalpha(day_open(Amt), day_ar1_coefficient(Ret), 241), day_centroid(Volume), 241)), 20)` |
| c03r1s614B_C2b_intraday_jumpiness | steer | +0.65 | +0.65 | +1.54 | 0 | -1 | 0.062 | +0.16 | `div(cross_stddev(day_std(Ret), 60), cross_hurst(day_std(Ret), 60))` |
| c03r1s605A_I0_open_search | control | +0.65 | +0.65 | +0.97 | 20 | -1 | 0.041 | -0.06 | `cross_sum(signedpower(cs_last_low40(cs_last_low40(day_argmax(Low), cs_last_low40(day_argmax(Low), day_kurt(Low))), cs_last_low40(day_argmax(Low), day_kurt(Low)))), 60)` |
| c03r1s602B_C2a_volume_backed_minutes | steer | +0.64 | +0.64 | +2.00 | 5 | +1 | 0.047 | -0.34 | `cross_min(cs_scale(cross_ema(cross_ema(day_corr(Ret, Volume), 30), 3)), 10)` |
| c03r1s611A_I0_open_search | control | +0.63 | +0.63 | +0.89 | 20 | -1 | 0.047 | -0.14 | `ts_product(cross_reg_tvalue(day_topw_mean(Volume, Volume), day_centroid(Close), 60), 10)` |
| c03r1s603B_C2a_volume_backed_minutes | steer | +0.62 | +0.62 | +1.25 | 0 | -1 | 0.036 | -0.30 | `cross_sum(cross_mean(day_signed_ratio(Ret, div(Ret, Volume)), 60), 30)` |
| c03r1s609B_C2b_intraday_jumpiness | steer | +0.62 | +0.62 | +1.74 | 0 | +1 | 0.070 | -0.40 | `cross_stddev(cross_stddev(day_wstd(Volume, Amt), 60), 60)` |
| c03r1s615A_I0_open_search | control | +0.62 | +0.66 | +0.62 | 20 | -1 | 0.065 | +0.30 | `pow_05(day_skew(log(log(Amt))))` |
| c03r1s610B_C2b_intraday_jumpiness | steer | +0.62 | +0.62 | +1.18 | 0 | -1 | 0.059 | +0.15 | `cross_stddev(day_std(in_stddev_rolling(Ret, 5)), 60)` |
| c03r1s613B_C2b_intraday_jumpiness | steer | +0.62 | +0.62 | +1.18 | 0 | -1 | 0.059 | +0.15 | `cross_stddev(day_std(in_stddev_rolling(Ret, 5)), 60)` |
| c03r1s608A_I0_open_search | control | +0.62 | +0.62 | +2.30 | 20 | +1 | 0.033 | +0.08 | `sigmoid(signedpower(pow_3(ts_skew(sigmoid(cs_first_high40(day_corr(Vwap, Amt), signedpower(pow_3(ts_skew(sigmoid(cs_first_high40(day_corr(Vwap, Amt), pow_3(ts_skew(day_ar1_coefficient(Ret), 50)))), 50))))), 50))))` |
| c03r1s616B_C2b_intraday_jumpiness | steer | +0.61 | +0.67 | +0.61 | 20 | +1 | 0.048 | -0.06 | `div(cross_stddev(day_std(Ret), 60), div(cross_stddev(day_var(Ret), 60), cross_mean(day_std(Ret), 60)))` |
| c03r1s611A_I0_open_search | control | +0.61 | +0.61 | +0.70 | 0 | +1 | 0.048 | -0.13 | `ts_product(cross_reg_tvalue(day_topw_mean(Volume, Volume), day_centroid(Ret), 241), 10)` |
| c03r1s602A_I0_open_search | control | +0.61 | +0.61 | +1.75 | 0 | +1 | 0.033 | -0.33 | `cs_mask_top_replace_mean_neg(pow_2(day_mean(Open)))` |
| c03r1s601A_I0_open_search | control | +0.60 | +0.60 | +1.38 | 20 | -1 | 0.069 | +0.09 | `div(pow_1_5(signedpower(pow_2_5(cross_reg_fvalue(day_min(Vwap), day_var(Ret), 3)))), day_min(Open))` |
| c03r1s609B_C2b_intraday_jumpiness | steer | +0.57 | +0.57 | +1.41 | 0 | -1 | 0.059 | +0.22 | `div(cross_stddev(day_std(Ret), 60), cross_valid_count(day_std(Ret), 60))` |
| c03r1s601A_I0_open_search | control | +0.57 | +0.57 | +0.91 | 5 | -1 | 0.067 | +0.24 | `pow_2_5(cross_reg_fvalue(cross_reg_fvalue(pow_2_5(pow_1_5(day_quantile(Open))), day_var(Ret), 60), day_var(Ret), 60))` |
| c03r1s614A_I0_open_search | control | +0.56 | +0.56 | +1.55 | 20 | -1 | 0.031 | +0.12 | `inv(cs_last_low40(day_quantile_q25(Vwap), day_open(Close)))` |
| c03r1s603A_I0_open_search | control | +0.56 | +0.56 | +2.27 | 20 | +1 | 0.047 | -0.06 | `ts_min(cs_last_high40(ts_min(day_autocorr_n1(Ret), 20), cross_regalpha(cs_scale(day_autocorr_n1(Volume)), day_ar1_coefficient(Ret), 15)), 20)` |
| c03r1s615B_C2b_intraday_jumpiness | steer | +0.55 | +0.55 | +1.41 | 0 | -1 | 0.059 | +0.22 | `cross_stddev(day_std(Ret), 60)` |
| c03r1s605B_C2a_volume_backed_minutes | steer | +0.55 | +0.55 | +1.87 | 0 | +1 | 0.041 | -0.39 | `cross_ema(cross_ema(day_corr(Ret, Volume), 15), 30)` |
| c03r1s607B_C2a_volume_backed_minutes | steer | +0.54 | +0.54 | +1.64 | 20 | +1 | 0.038 | -0.36 | `cross_mean(cross_ema(day_corr(Ret, Volume), 30), 3)` |
| c03r1s611A_I0_open_search | control | +0.53 | +0.53 | +1.01 | 5 | +1 | 0.046 | -0.21 | `ts_product(cross_reg_tvalue(day_topw_mean(Volume, Volume), day_centroid(Volume), 60), 10)` |
| c03r1s606B_C2a_volume_backed_minutes | steer | +0.52 | +0.52 | +2.56 | 20 | -1 | 0.025 | -0.29 | `cross_mean(day_corr(Ret, div(div(abs_(Ret), Volume), Volume)), 60)` |
| c03r1s607A_I0_open_search | control | +0.52 | +0.52 | +0.92 | 20 | +1 | 0.063 | -0.44 | `cross_delay(log(cross_delay(log(cross_delay(log(log(day_std(Volume))), 30)), 3)), 60)` |
| c03r1s615A_I0_open_search | control | +0.52 | +0.74 | +0.52 | 20 | +1 | 0.022 | -0.02 | `inv(sigmoid(ts_scale(ts_scale(day_corr(Low, log(Amt)), 10), 10)))` |
| c03r1s601B_C2a_volume_backed_minutes | steer | +0.51 | +0.51 | +1.63 | 20 | +1 | 0.038 | -0.35 | `cross_ema(day_corr(Ret, Volume), 30)` |
| c03r1s603B_C2a_volume_backed_minutes | steer | +0.51 | +0.51 | +1.63 | 20 | +1 | 0.038 | -0.35 | `cross_ema(day_corr(Ret, Volume), 30)` |
| c03r1s604B_C2a_volume_backed_minutes | steer | +0.51 | +0.51 | +1.63 | 20 | +1 | 0.038 | -0.35 | `cross_ema(day_corr(Ret, Volume), 30)` |
| c03r1s606B_C2a_volume_backed_minutes | steer | +0.51 | +0.51 | +1.63 | 20 | +1 | 0.038 | -0.35 | `cross_ema(day_corr(Ret, Volume), 30)` |
| c03r1s608B_C2a_volume_backed_minutes | steer | +0.51 | +0.51 | +1.63 | 20 | +1 | 0.038 | -0.35 | `cross_ema(day_corr(Ret, Volume), 30)` |
| c03r1s601B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |
| c03r1s602B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |
| c03r1s604B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |
| c03r1s605B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |
| c03r1s606B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |
| c03r1s607B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |
| c03r1s608B_C2a_volume_backed_minutes | steer | +0.50 | +0.50 | +1.40 | 5 | -1 | 0.041 | -0.28 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 60)` |

## C02 的直接检验(B 组,64 个变体;只含 train / valid)

| 假设 | 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 相关度拒绝 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H1_slow_intraday_reversal | v4 | core | +0.98 | +0.99 | +0.98 | -1.00 | 5.0 | +0.04 | +0.30 |  | `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` |
| H1_slow_intraday_reversal | v2 | core | +0.86 | +0.89 | +0.86 | -1.00 | 20.0 | +0.03 | +0.24 |  | `ts_mean(day_mean(Ret), 30)` |
| H2_overnight_vs_intraday | v3 | core | +0.86 | +0.89 | +0.86 | +1.00 | 20.0 | +0.03 | +0.24 |  | `cross_mean(sub(mul(2, day_first(Ret)), day_sum(Ret)), 30)` |
| H1_slow_intraday_reversal | v1 | core | +0.84 | +0.97 | +0.84 | -1.00 | 20.0 | +0.03 | +0.23 |  | `cross_mean(log(div(day_last(Close), day_first(Open))), 30)` |
| H1_slow_intraday_reversal | v7 | ablation | +0.84 | +0.96 | +0.84 | -1.00 | 20.0 | +0.03 | +0.23 |  | `cross_mean(log(div(day_last(Close), day_first(Close))), 30)` |
| H1_slow_intraday_reversal | v5 | ablation | +0.66 | +0.66 | +0.72 | -1.00 | 20.0 | +0.04 | +0.11 |  | `cross_mean(log(div(day_last(Close), day_first(Open))), 15)` |
| H1_slow_intraday_reversal | v9 | ablation | +0.65 | +0.65 | +0.79 | -1.00 | 20.0 | +0.04 | +0.09 |  | `log(div(day_last(Close), ts_delay(day_last(Close), 20)))` |
| H1_slow_intraday_reversal | v8 | ablation | +0.60 | +0.60 | +0.72 | -1.00 | 20.0 | +0.03 | +0.22 |  | `div(cross_mean(day_sum(Ret), 30), cross_mean(day_std(Ret), 30))` |
| H3_money_weighted_price_reverts | v1 | core | +0.51 | +0.51 | +0.63 | -1.00 | 20.0 | +0.02 | +0.40 |  | `cross_mean(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Close)), 30)` |
| H7_daily_max_lottery | v3 | core | +0.47 | +0.47 | +0.54 | -1.00 | 5.0 | +0.05 | +0.18 |  | `ts_skew(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 40)` |
| H1_slow_intraday_reversal | v6 | ablation | +0.44 | +0.96 | +0.44 | -1.00 | 5.0 | +0.04 | +0.30 |  | `cross_mean(log(div(day_last(Close), day_first(Open))), 60)` |
| H1_slow_intraday_reversal | v11 | ablation | +0.43 | +0.43 | +1.03 | -1.00 | 20.0 | +0.03 | +0.20 |  | `div(cross_mean(log(div(day_last(Close), day_first(Open))), 30), cross_mean(log(div(day_max(High), day_min(Low))), 30))` |
| H1_slow_intraday_reversal | v3 | core | +0.42 | +1.06 | +0.42 | -1.00 | 5.0 | +0.04 | +0.30 |  | `ts_mean(day_mean(Ret), 50)` |
| H4_intraday_price_volume_corr | v6 | ablation | +0.39 | +0.39 | +0.79 | -1.00 | 5.0 | +0.04 | +0.50 |  | `add(cs_rank(cross_mean(day_corr(Close, Volume), 30)), cs_rank(cross_stddev(day_corr(Close, Volume), 30)))` |
| H3_money_weighted_price_reverts | v8 | ablation | +0.34 | +0.34 | +0.87 | -1.00 | 20.0 | +0.03 | +0.35 |  | `cross_mean(day_topw_mean(Ret, Amt), 30)` |
| H1_slow_intraday_reversal | v12 | ablation | +0.22 | +0.64 | +0.22 | -1.00 | 20.0 | +0.03 | -0.01 |  | `cs_regres(cross_mean(log(div(day_last(Close), day_first(Open))), 30), cross_mean(log(div(day_max(High), day_min(Low))), 30))` |
| H5_closing_push_reverts | v2 | core | +0.17 | +0.17 | +0.93 | -1.00 | 5.0 | +0.04 | -0.01 |  | `cross_mean(day_last(Ret), 30)` |
| H5_closing_push_reverts | v5 | ablation | +0.17 | +0.17 | +0.93 | +1.00 | 5.0 | +0.04 | -0.01 |  | `cross_mean(sub(day_first(Ret), day_last(Ret)), 30)` |
| H2_overnight_vs_intraday | v8 | ablation | +0.15 | +0.15 | +0.42 | +1.00 | 5.0 | +0.04 | +0.23 |  | `sub(ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 50), ts_mean(log(div(day_last(Close), day_first(Open))), 50))` |
| H1_slow_intraday_reversal | v10 | ablation | +0.13 | +0.13 | +0.64 | -1.00 | 5.0 | +0.06 | +0.18 |  | `ts_mean(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 30)` |
| H2_overnight_vs_intraday | v2 | core | +0.07 | +0.07 | +0.66 | +1.00 | 20.0 | +0.03 | +0.20 |  | `sub(ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 30), ts_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H3_money_weighted_price_reverts | v2 | core | +0.05 | +0.05 | +0.43 | -1.00 | 5.0 | +0.05 | +0.26 |  | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 30)` |
| H3_money_weighted_price_reverts | v3 | core | +0.01 | +0.01 | +0.61 | -1.00 | 5.0 | +0.05 | +0.35 |  | `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 30)` |
| H2_overnight_vs_intraday | v11 | control | -0.08 | -0.08 | +1.32 | -1.00 | 20.0 | +0.02 | +0.52 | 是 | `ts_mean(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 30)` |
| H3_money_weighted_price_reverts | v5 | ablation | -0.08 | -0.08 | +0.11 | -1.00 | 20.0 | +0.02 | +0.24 |  | `cross_mean(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 30)` |
| H6_attention_shock | v1 | core | -0.18 | -0.18 | +0.79 | -1.00 | 20.0 | +0.04 | +0.12 |  | `log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60)))` |
| H4_intraday_price_volume_corr | v7 | ablation | -0.18 | -0.18 | +0.91 | -1.00 | 5.0 | +0.05 | +0.26 |  | `cross_mean(day_corr(in_delay(Ret, 3), Volume), 30)` |
| H4_intraday_price_volume_corr | v2 | core | -0.28 | -0.28 | -0.05 | -1.00 | 20.0 | +0.03 | +0.27 |  | `cross_mean(day_corr(Ret, Volume), 30)` |
| H3_money_weighted_price_reverts | v11 | control | -0.32 | -0.32 | +1.34 | -1.00 | 20.0 | +0.03 | +0.07 |  | `cross_mean(sub(day_signed_ratio(Ret, cross_delay(Amt, 3)), day_signed_ratio(Ret, Close)), 30)` |
| H4_intraday_price_volume_corr | v10 | control | -0.34 | -0.34 | +1.01 | -1.00 | 5.0 | +0.02 | +0.44 |  | `cross_mean(day_corr(abs_(Ret), Volume), 30)` |
| H6_attention_shock | v4 | ablation | -0.35 | -0.25 | -0.35 | -1.00 | 5.0 | +0.06 | +0.04 |  | `div(cross_stddev(day_sum(Amt), 30), cross_mean(day_sum(Amt), 30))` |
| H7_daily_max_lottery | v1 | core | -0.38 | -0.38 | +0.66 | -1.00 | 5.0 | +0.05 | +0.43 |  | `ts_max(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20)` |
| H3_money_weighted_price_reverts | v6 | ablation | -0.40 | -0.40 | +0.16 | -1.00 | 20.0 | +0.03 | +0.31 |  | `cross_mean(div(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 30)` |
| H3_money_weighted_price_reverts | v9 | ablation | -0.45 | -0.15 | -0.45 | +1.00 | 5.0 | +0.04 | -0.35 |  | `cs_regres(cross_mean(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Close)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_intraday_price_volume_corr | v5 | ablation | -0.46 | -0.46 | +0.98 | -1.00 | 5.0 | +0.04 | +0.55 | 是 | `cross_stddev(day_corr(Close, Volume), 30)` |
| H1_slow_intraday_reversal | v13 | control | -0.47 | -0.47 | +0.67 | -1.00 | 5.0 | +0.02 | +0.53 | 是 | `cross_mean(log(div(day_max(High), day_min(Low))), 30)` |
| H7_daily_max_lottery | v2 | core | -0.67 | -0.67 | +0.21 | -1.00 | 20.0 | +0.04 | +0.07 |  | `div(ts_max(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20), ts_std(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20))` |
| H3_money_weighted_price_reverts | v4 | control | -0.67 | -0.67 | +0.56 | -1.00 | 20.0 | +0.03 | +0.09 |  | `cross_mean(sub(day_topw_mean(Ret, cross_delay(Amt, 3)), day_mean(Ret)), 30)` |
| H4_intraday_price_volume_corr | v8 | ablation | -0.72 | -0.66 | -0.72 | -1.00 | 20.0 | +0.03 | +0.23 |  | `cs_regres(cross_mean(day_corr(Close, Volume), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H6_attention_shock | v2 | core | -0.83 | -0.83 | -0.10 | -1.00 | 20.0 | +0.10 | +0.02 |  | `mul(sign(cross_sum(day_sum(Ret), 5)), log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60))))` |
| H4_intraday_price_volume_corr | v4 | ablation | -0.87 | -0.20 | -0.87 | -1.00 | 5.0 | +0.03 | +0.26 |  | `cross_mean(day_corr(Close, Volume), 60)` |
| H7_daily_max_lottery | v4 | ablation | -0.89 | -0.89 | -0.16 | -1.00 | 5.0 | +0.05 | +0.37 |  | `cs_regres(ts_max(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_intraday_price_volume_corr | v1 | core | -0.92 | -0.52 | -0.92 | -1.00 | 20.0 | +0.03 | +0.24 |  | `cross_mean(day_corr(Close, Volume), 30)` |
| H3_money_weighted_price_reverts | v7 | ablation | -0.95 | -0.95 | -0.75 | -1.00 | 20.0 | +0.02 | +0.16 |  | `cross_mean(day_signed_ratio(Ret, Amt), 30)` |
| H7_daily_max_lottery | v5 | control | -0.95 | -0.95 | +0.07 | -1.00 | 5.0 | +0.04 | +0.51 | 是 | `ts_std(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20)` |
| H2_overnight_vs_intraday | v5 | ablation | -1.07 | -0.60 | -1.07 | +1.00 | 20.0 | +0.02 | +0.06 |  | `ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 50)` |
| H2_overnight_vs_intraday | v10 | ablation | -1.20 | -0.36 | -1.20 | +1.00 | 5.0 | +0.06 | +0.17 |  | `cs_regres(cross_mean(sub(mul(2, day_first(Ret)), day_sum(Ret)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_intraday_price_volume_corr | v9 | ablation | -1.23 | -1.23 | -0.83 | +1.00 | 20.0 | +0.02 | -0.21 |  | `cs_regres(cross_mean(day_corr(Ret, Volume), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_intraday_price_volume_corr | v3 | ablation | -1.30 | -0.82 | -1.30 | -1.00 | 20.0 | +0.04 | +0.17 |  | `cross_mean(day_corr(Close, Volume), 15)` |
| H6_attention_shock | v6 | control | -1.37 | -1.37 | -0.46 | -1.00 | 20.0 | +0.05 | -0.02 |  | `log(div(cross_mean(day_std(Ret), 5), cross_mean(day_std(Ret), 60)))` |
| H6_attention_shock | v3 | ablation | -1.62 | -1.62 | -0.52 | -1.00 | 20.0 | +0.04 | +0.10 |  | `cs_regres(log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60))), cross_ema(cross_scale(mul(signedpower(day_std(Volume)), day_first(Volume)), 241), 15))` |
| H5_closing_push_reverts | v8 | control | -1.63 | -0.37 | -1.63 | -1.00 | 20.0 | +0.03 | +0.04 |  | `cross_mean(day_last(in_sum_rolling(in_delay(Ret, 60), 30)), 30)` |
| H5_closing_push_reverts | v1 | core | -1.64 | -1.17 | -1.64 | -1.00 | 5.0 | +0.04 | -0.12 |  | `cross_mean(day_last(in_sum_rolling(Ret, 30)), 30)` |
| H5_closing_push_reverts | v3 | core | -1.65 | -1.13 | -1.65 | -1.00 | 5.0 | +0.04 | -0.12 |  | `cross_mean(log(div(day_last(Close), day_last(in_delay(Close, 30)))), 30)` |
| H2_overnight_vs_intraday | v1 | core | -1.66 | -0.71 | -1.66 | +1.00 | 20.0 | +0.02 | +0.09 |  | `ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 30)` |
| H6_attention_shock | v5 | ablation | -1.71 | -1.71 | -0.63 | -1.00 | 20.0 | +0.04 | +0.07 |  | `cs_regres(log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60))), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H3_money_weighted_price_reverts | v10 | ablation | -1.73 | -1.04 | -1.73 | +1.00 | 20.0 | +0.02 | -0.29 |  | `cs_regres(cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H5_closing_push_reverts | v4 | ablation | -1.75 | -0.76 | -1.75 | -1.00 | 5.0 | +0.05 | -0.01 |  | `cross_mean(day_last(in_sum_rolling(Ret, 15)), 30)` |
| H5_closing_push_reverts | v6 | ablation | -1.90 | -0.16 | -1.90 | -1.00 | 5.0 | +0.03 | -0.50 | 是 | `cross_mean(div(day_last(in_sum_rolling(Amt, 30)), day_sum(Amt)), 30)` |
| H2_overnight_vs_intraday | v4 | ablation | -2.04 | -0.86 | -2.04 | +1.00 | 20.0 | +0.03 | +0.10 |  | `ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)` |
| H5_closing_push_reverts | v7 | ablation | -2.47 | -1.74 | -2.47 | -1.00 | 5.0 | +0.05 | -0.15 |  | `cs_regres(cross_mean(day_last(in_sum_rolling(Ret, 30)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H2_overnight_vs_intraday | v9 | ablation | -2.79 | -1.02 | -2.79 | +1.00 | 20.0 | +0.02 | +0.08 |  | `cs_regres(ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H2_overnight_vs_intraday | v6 | ablation | — | — | — | — | — | — | — |  | `cross_mean(day_first(Ret), 30)` |
| H2_overnight_vs_intraday | v7 | ablation | — | — | — | — | — | — | — |  | `cross_mean(log(div(day_first(Close), day_first(Open))), 30)` |

## C03 的直接检验(B 组,64 个变体;只含 train / valid)

| 假设 | 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 相关度拒绝 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H5_vol_of_vol_ambiguity | v5 | ablation | +0.38 | +0.38 | +0.86 | -1.00 | 0.0 | +0.06 | +0.09 |  | `div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60))` |
| H5_vol_of_vol_ambiguity | v3 | core | +0.31 | +0.31 | +1.35 | -1.00 | 0.0 | +0.05 | -0.15 |  | `cross_mean(div(day_std(in_stddev_rolling(Ret, 5)), day_mean(in_stddev_rolling(Ret, 5))), 60)` |
| H5_vol_of_vol_ambiguity | v7 | ablation | +0.28 | +0.28 | +1.30 | -1.00 | 0.0 | +0.05 | -0.11 |  | `cross_mean(day_kurt(Ret), 30)` |
| H4_volume_conditioned_reversal | v7 | ablation | +0.22 | +0.22 | +2.30 | +1.00 | 20.0 | +0.05 | -0.27 |  | `cross_mean(day_corr(Ret, Volume), 30)` |
| H5_vol_of_vol_ambiguity | v1 | core | +0.22 | +0.22 | +1.19 | -1.00 | 0.0 | +0.06 | -0.13 |  | `cross_mean(div(day_std(in_stddev_rolling(Ret, 5)), day_mean(in_stddev_rolling(Ret, 5))), 30)` |
| H5_vol_of_vol_ambiguity | v4 | ablation | +0.11 | +0.11 | +0.53 | -1.00 | 0.0 | +0.07 | +0.11 |  | `div(cross_stddev(day_std(Ret), 30), cross_mean(day_std(Ret), 30))` |
| H3_signed_variance_asymmetry | v4 | ablation | +0.04 | +0.04 | +1.58 | -1.00 | 20.0 | +0.04 | -0.23 |  | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 30)` |
| H5_vol_of_vol_ambiguity | v2 | core | +0.04 | +0.04 | +1.00 | -1.00 | 0.0 | +0.05 | +0.02 |  | `cross_mean(div(day_std(in_stddev_rolling(Ret, 15)), day_mean(in_stddev_rolling(Ret, 15))), 30)` |
| H6_turnover_instability | v8 | control | -0.05 | +0.31 | -0.05 | +1.00 | 20.0 | +0.03 | -0.00 |  | `abs_(cs_demean(cs_rank(cross_mean(day_sum(Amt), 30))))` |
| H2_smart_money_minutes | v5 | ablation | -0.08 | -0.08 | +0.30 | -1.00 | 5.0 | +0.07 | +0.16 |  | `cross_mean(div(day_topw_mean(Close, abs_(Ret)), day_wmean(Close, Volume)), 30)` |
| H5_vol_of_vol_ambiguity | v6 | ablation | -0.11 | -0.11 | +1.09 | -1.00 | 0.0 | +0.08 | +0.19 |  | `cross_mean(day_std(in_stddev_rolling(Ret, 5)), 30)` |
| H4_volume_conditioned_reversal | v12 | control | -0.24 | -0.09 | -0.24 | -1.00 | 20.0 | +0.05 | +0.30 |  | `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` |
| H6_turnover_instability | v6 | ablation | -0.27 | -0.07 | -0.27 | -1.00 | 5.0 | +0.07 | -0.12 |  | `div(cross_max(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| H4_volume_conditioned_reversal | v2 | core | -0.27 | -0.09 | -0.27 | -1.00 | 20.0 | +0.04 | +0.07 |  | `cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 60)` |
| H1_price_conditional_range | v10 | control | -0.29 | -0.29 | +0.59 | -1.00 | 0.0 | +0.06 | +0.53 | 是 | `cross_mean(log(div(day_max(High), day_min(Low))), 30)` |
| H5_vol_of_vol_ambiguity | v10 | control | -0.35 | -0.35 | -0.04 | -1.00 | 20.0 | +0.05 | +0.15 |  | `abs_(cs_demean(cs_rank(cross_mean(day_std(Ret), 30))))` |
| H3_signed_variance_asymmetry | v1 | core | -0.38 | -0.33 | -0.38 | -1.00 | 20.0 | +0.05 | +0.29 |  | `cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 30)` |
| H3_signed_variance_asymmetry | v3 | core | -0.39 | -0.39 | -0.35 | -1.00 | 20.0 | +0.05 | +0.29 |  | `cross_mean(day_signed_ratio(in_demean(Ret), pow_2(in_demean(Ret))), 30)` |
| H6_turnover_instability | v2 | core | -0.39 | +0.24 | -0.39 | -1.00 | 5.0 | +0.07 | -0.03 |  | `div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| H3_signed_variance_asymmetry | v2 | core | -0.41 | -0.10 | -0.41 | -1.00 | 5.0 | +0.05 | +0.31 |  | `cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 60)` |
| H6_turnover_instability | v5 | ablation | -0.47 | -0.47 | +0.13 | -1.00 | 0.0 | +0.06 | -0.14 |  | `div(cross_stddev(day_sum(Amt), 241), cross_mean(day_sum(Amt), 241))` |
| H6_turnover_instability | v1 | core | -0.50 | -0.50 | -0.24 | -1.00 | 20.0 | +0.06 | +0.04 |  | `div(cross_stddev(day_sum(Amt), 30), cross_mean(day_sum(Amt), 30))` |
| H1_price_conditional_range | v3 | core | -0.54 | -0.42 | -0.54 | -1.00 | 20.0 | +0.05 | +0.30 |  | `cross_corr(day_last(Close), day_std(Ret), 30)` |
| H6_turnover_instability | v7 | ablation | -0.62 | -0.23 | -0.62 | -1.00 | 5.0 | +0.07 | -0.04 |  | `cs_regres(div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60)), cross_scale(mul(signedpower(day_std(Volume)), day_first(Volume)), 241))` |
| H3_signed_variance_asymmetry | v7 | ablation | -0.68 | -0.60 | -0.68 | -1.00 | 20.0 | +0.07 | +0.16 |  | `cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 10)` |
| H6_turnover_instability | v10 | control | -0.74 | -0.74 | +0.41 | +1.00 | 20.0 | +0.11 | -0.12 |  | `log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60)))` |
| H6_turnover_instability | v9 | ablation | -0.78 | -0.78 | -0.46 | -1.00 | 20.0 | +0.07 | -0.00 |  | `div(cross_stddev(day_sum(Amt), 15), cross_mean(day_sum(Amt), 15))` |
| H1_price_conditional_range | v2 | core | -0.80 | -0.80 | -0.59 | -1.00 | 20.0 | +0.05 | +0.20 |  | `cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 60)` |
| H4_volume_conditioned_reversal | v3 | core | -0.89 | -0.14 | -0.89 | -1.00 | 20.0 | +0.05 | +0.15 |  | `sub(div(cross_mean(mul(log(div(day_last(Close), day_first(Open))), day_sum(Amt)), 30), cross_mean(day_sum(Amt), 30)), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| H1_price_conditional_range | v11 | control | -0.90 | -0.90 | -0.58 | +1.00 | 5.0 | +0.05 | -0.42 |  | `log(day_last(Close))` |
| H3_signed_variance_asymmetry | v8 | ablation | -0.94 | -0.94 | -0.73 | -1.00 | 20.0 | +0.05 | +0.18 |  | `cs_regres(cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_volume_conditioned_reversal | v1 | core | -1.02 | -0.71 | -1.02 | -1.00 | 20.0 | +0.06 | +0.08 |  | `cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 30)` |
| H5_vol_of_vol_ambiguity | v8 | ablation | -1.03 | -1.03 | +0.49 | -1.00 | 20.0 | +0.05 | -0.07 |  | `cs_regres(cross_mean(div(day_std(in_stddev_rolling(Ret, 5)), day_mean(in_stddev_rolling(Ret, 5))), 30), cross_mean(day_kurt(Ret), 30))` |
| H3_signed_variance_asymmetry | v6 | ablation | -1.05 | -0.31 | -1.05 | -1.00 | 5.0 | +0.06 | +0.17 |  | `cross_mean(day_skew(Ret), 30)` |
| H1_price_conditional_range | v8 | ablation | -1.06 | +0.11 | -1.06 | -1.00 | 20.0 | +0.06 | +0.17 |  | `cross_corr(day_last(Close), day_sum(Amt), 30)` |
| H6_turnover_instability | v3 | core | -1.10 | +0.21 | -1.10 | -1.00 | 0.0 | +0.09 | +0.07 |  | `cross_stddev(log(day_sum(Amt)), 60)` |
| H3_signed_variance_asymmetry | v9 | ablation | -1.25 | -0.70 | -1.25 | -1.00 | 20.0 | +0.05 | +0.34 |  | `cs_regres(cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 30), cross_mean(day_skew(Ret), 30))` |
| H1_price_conditional_range | v1 | core | -1.27 | -0.70 | -1.27 | -1.00 | 20.0 | +0.06 | +0.22 |  | `cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 30)` |
| H3_signed_variance_asymmetry | v5 | ablation | -1.29 | -0.92 | -1.29 | -1.00 | 20.0 | +0.06 | +0.19 |  | `cross_mean(day_signed_ratio(Ret, Ret), 30)` |
| H2_smart_money_minutes | v7 | ablation | -1.34 | -1.22 | -1.34 | -1.00 | 20.0 | +0.05 | +0.12 |  | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(cross_delay(Volume, 3)))), day_wmean(Close, Volume)), 30)` |
| H1_price_conditional_range | v6 | ablation | -1.35 | -0.97 | -1.35 | -1.00 | 20.0 | +0.06 | +0.21 |  | `cross_corr(day_mean(Vwap), log(div(day_max(High), day_min(Low))), 30)` |
| H4_volume_conditioned_reversal | v4 | ablation | -1.36 | -1.36 | +0.19 | +1.00 | 20.0 | +0.05 | -0.24 |  | `cross_mean(day_corr(Close, Volume), 30)` |
| H4_volume_conditioned_reversal | v5 | ablation | -1.40 | -1.08 | -1.40 | +1.00 | 20.0 | +0.07 | -0.10 |  | `ts_corr(log(div(day_last(Close), ts_delay(day_last(Close), 1))), day_sum(Amt), 30)` |
| H5_vol_of_vol_ambiguity | v9 | control | -1.41 | -1.41 | -0.51 | +1.00 | 0.0 | +0.07 | +0.57 | 是 | `cross_mean(day_zero_ratio(Ret), 30)` |
| H4_volume_conditioned_reversal | v6 | ablation | -1.46 | -0.80 | -1.46 | -1.00 | 20.0 | +0.06 | +0.11 |  | `cross_corr(log(div(day_last(Close), day_first(Open))), log(day_sum(Amt)), 30)` |
| H3_signed_variance_asymmetry | v10 | control | -1.50 | -1.50 | -0.57 | -1.00 | 20.0 | +0.06 | +0.57 | 是 | `cross_mean(day_pos_ratio(Ret), 30)` |
| H4_volume_conditioned_reversal | v10 | core | -1.51 | -1.51 | +0.38 | +1.00 | 20.0 | +0.05 | -0.23 |  | `cs_regres(cross_mean(day_corr(Close, Volume), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| H6_turnover_instability | v4 | core | -1.55 | -1.55 | +1.27 | -1.00 | 20.0 | +0.05 | -0.07 |  | `cross_stddev(ts_delta(log(day_sum(Amt)), 1), 60)` |
| H4_volume_conditioned_reversal | v9 | ablation | -1.67 | -1.10 | -1.67 | -1.00 | 20.0 | +0.06 | +0.03 |  | `cs_regres(cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_volume_conditioned_reversal | v8 | ablation | -1.70 | -1.70 | +0.36 | +1.00 | 20.0 | +0.06 | -0.17 |  | `cross_mean(day_corr(Close, Volume), 15)` |
| H2_smart_money_minutes | v4 | core | -1.70 | -1.51 | -1.70 | -1.00 | 20.0 | +0.07 | -0.02 |  | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(pow_05(Volume)))), day_wmean(Close, Volume)), 30)` |
| H1_price_conditional_range | v4 | ablation | -1.75 | -1.58 | -1.75 | -1.00 | 20.0 | +0.06 | +0.19 |  | `cross_mean(day_corr(Close, abs_(Ret)), 30)` |
| H2_smart_money_minutes | v10 | control | -1.83 | -0.64 | -1.83 | -1.00 | 20.0 | +0.07 | -0.01 |  | `cross_mean(div(day_last(Close), day_wmean(Close, Volume)), 30)` |
| H1_price_conditional_range | v5 | ablation | -1.93 | -1.37 | -1.93 | -1.00 | 20.0 | +0.08 | +0.15 |  | `cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 15)` |
| H1_price_conditional_range | v7 | ablation | -1.98 | -1.16 | -1.98 | -1.00 | 20.0 | +0.06 | +0.21 |  | `cross_corr(log(div(day_last(Close), day_first(Open))), log(div(day_max(High), day_min(Low))), 30)` |
| H1_price_conditional_range | v9 | ablation | -2.20 | -1.17 | -2.20 | -1.00 | 20.0 | +0.06 | +0.19 |  | `cs_regres(cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| H4_volume_conditioned_reversal | v11 | control | -2.33 | -0.43 | -2.33 | +1.00 | 20.0 | +0.05 | -0.03 |  | `cross_corr(abs_(log(div(day_last(Close), day_first(Open)))), day_sum(Amt), 30)` |
| H2_smart_money_minutes | v8 | ablation | -2.40 | -0.69 | -2.40 | +1.00 | 20.0 | +0.05 | +0.16 |  | `cross_mean(div(day_topw_mean(Vwap, div(abs_(Ret), pow_05(Volume))), day_wmean(Vwap, Volume)), 30)` |
| H2_smart_money_minutes | v1 | core | -2.56 | -0.65 | -2.56 | +1.00 | 20.0 | +0.05 | +0.15 |  | `cross_mean(div(day_mean(in_topk_masked_exact(div(abs_(Ret), pow_05(Volume)), Close, 20)), day_wmean(Close, Volume)), 30)` |
| H2_smart_money_minutes | v9 | ablation | -2.62 | -1.24 | -2.62 | +1.00 | 20.0 | +0.05 | +0.13 |  | `cs_regres(cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(Volume))), day_wmean(Close, Volume)), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| H2_smart_money_minutes | v3 | core | -3.06 | -0.88 | -3.06 | +1.00 | 20.0 | +0.05 | +0.12 |  | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(Volume))), day_wmean(Close, Volume)), 30)` |
| H2_smart_money_minutes | v6 | ablation | -3.39 | -0.99 | -3.39 | -1.00 | 20.0 | +0.04 | +0.23 |  | `cross_mean(div(day_topw_mean(Close, Volume), day_wmean(Close, Volume)), 30)` |
| H2_smart_money_minutes | v11 | control | -3.74 | -1.53 | -3.74 | +1.00 | 5.0 | +0.06 | +0.09 |  | `cross_mean(div(day_mean(Close), day_wmean(Close, Volume)), 30)` |
| H2_smart_money_minutes | v2 | core | -3.89 | -1.53 | -3.89 | +1.00 | 20.0 | +0.08 | +0.04 |  | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(Volume))), day_wmean(Close, Volume)), 10)` |

