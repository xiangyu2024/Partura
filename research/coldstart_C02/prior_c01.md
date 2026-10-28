# C02 的先验知识:C01 的样本内结果(只含 train / valid;没有任何测试段数字)

C01:A 组 = AlphaCube GP 盲搜;B 组 = AlphaCube + Partura v1(通过先验与邻域引导 GP)。R1 两组共用。score = 纯多头十分位书扣 15bp 的 train 与 valid 夏普中较差的。
更多:C01 的 PLAN.md、beliefs_r2.md / beliefs_r3.md(Partura v1 自己的信念与诊断)、cards_r2.md / cards_r3.md、digest_r3.md、round3_workflow.json。

## 每次运行

| 运行 | 组 | 付费评估 | 通过(score ≥ 1) | 其中已知族(\|ρ\| ≥ 0.5) | 自己的 heads |
|---|---|---|---|---|---|
| c01r1s101_I0_open_search | control | 177 | 77 | 77 | 0 |
| c01r1s102_I0_open_search | control | 117 | 19 | 19 | 0 |
| c01r1s103_I0_open_search | control | 131 | 26 | 20 | 3 |
| c01r1s104_I0_open_search | control | 143 | 38 | 8 | 12 |
| c01r1s105_I0_open_search | control | 139 | 13 | 5 | 2 |
| c01r1s106_I0_open_search | control | 133 | 31 | 31 | 0 |
| c01r1s107_I0_open_search | control | 98 | 19 | 7 | 1 |
| c01r1s108_I0_open_search | control | 149 | 50 | 50 | 0 |
| c01r2s201A_I0_open_search | control | 116 | 42 | 1 | 4 |
| c01r2s201B_C2a_when_the_return_arrives | steer | 153 | 43 | 43 | 0 |
| c01r2s202A_I0_open_search | control | 137 | 38 | 24 | 2 |
| c01r2s202B_C2a_when_the_return_arrives | steer | 121 | 31 | 31 | 0 |
| c01r2s203A_I0_open_search | control | 112 | 20 | 20 | 0 |
| c01r2s203B_C2a_when_the_return_arrives | steer | 157 | 53 | 49 | 2 |
| c01r2s204A_I0_open_search | control | 175 | 80 | 65 | 7 |
| c01r2s204B_C2a_when_the_return_arrives | steer | 146 | 63 | 63 | 0 |
| c01r2s205A_I0_open_search | control | 146 | 51 | 51 | 0 |
| c01r2s205B_C2b_turnover_on_the_up_minutes | steer | 184 | 72 | 72 | 0 |
| c01r2s206A_I0_open_search | control | 153 | 73 | 73 | 0 |
| c01r2s206B_C2b_turnover_on_the_up_minutes | steer | 156 | 12 | 12 | 0 |
| c01r2s207A_I0_open_search | control | 141 | 35 | 25 | 2 |
| c01r2s208A_I0_open_search | control | 147 | 36 | 36 | 0 |
| c01r2s208B_C2b_turnover_on_the_up_minutes | steer | 131 | 21 | 21 | 0 |
| c01r3s301A_I0_open_search | control | 144 | 42 | 23 | 2 |
| c01r3s301B_C3a_slow_lottery_shape | steer | 151 | 0 | 0 | 0 |
| c01r3s302A_I0_open_search | control | 131 | 36 | 2 | 4 |
| c01r3s302B_C3a_slow_lottery_shape | steer | 148 | 0 | 0 | 0 |
| c01r3s303A_I0_open_search | control | 146 | 47 | 47 | 0 |
| c01r3s303B_C3a_slow_lottery_shape | steer | 141 | 0 | 0 | 0 |
| c01r3s304A_I0_open_search | control | 145 | 57 | 53 | 2 |
| c01r3s304B_C3a_slow_lottery_shape | steer | 138 | 0 | 0 | 0 |
| c01r3s305A_I0_open_search | control | 172 | 59 | 59 | 0 |
| c01r3s305B_I0_open_search | steer | 146 | 1 | 0 | 1 |
| c01r3s306A_I0_open_search | control | 127 | 34 | 34 | 0 |
| c01r3s306B_I0_open_search | steer | 140 | 3 | 0 | 1 |
| c01r3s307A_I0_open_search | control | 169 | 67 | 67 | 0 |
| c01r3s307B_I0_open_search | steer | 156 | 0 | 0 | 0 |
| c01r3s308A_I0_open_search | control | 153 | 24 | 14 | 3 |
| c01r3s308B_I0_open_search | steer | 146 | 0 | 0 | 0 |

## C01 的全部 heads(各运行内去重;48 个,按分数排序;C02 的新 head 必须与它们都 \|ρ\| < 0.7)

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
