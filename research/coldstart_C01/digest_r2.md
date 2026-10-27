# C01 证据摘要:写第 2 轮指引之前(只含 B 臂自己的运行)

运行 8 次;存下的候选 627 个(每次运行最多存 80 个);score ≥ 1 的 273 个;互不相关且不在已知族里的 heads 18 个。score = 纯多头十分位书扣 15bp 后 train 与 valid 夏普中较差的那个。

## 每次运行

| 轮 | 种子 | idea | 付费评估 | 门槛废品率 | 通过 | heads | 每百次 heads | 秒 | 采样统计 |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 101 | I0_open_search | 177 | 19% | 77 | 0 | 0.0 | 860 | {} |
| R1 | 102 | I0_open_search | 117 | 24% | 19 | 0 | 0.0 | 634 | {} |
| R1 | 103 | I0_open_search | 131 | 24% | 26 | 3 | 2.3 | 687 | {} |
| R1 | 104 | I0_open_search | 143 | 32% | 38 | 12 | 8.4 | 661 | {} |
| R1 | 105 | I0_open_search | 139 | 26% | 13 | 2 | 1.4 | 957 | {} |
| R1 | 106 | I0_open_search | 133 | 23% | 31 | 0 | 0.0 | 723 | {} |
| R1 | 107 | I0_open_search | 98 | 32% | 19 | 1 | 1.0 | 555 | {} |
| R1 | 108 | I0_open_search | 149 | 17% | 50 | 0 | 0.0 | 666 | {} |

## heads(互不相关、|ρ| 对已知族与 pool 都 < 0.5)

| 轮 | 种子 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 104 | +2.72 | +2.82 | +2.72 | 20 | -1 | 0.026 | +0.16 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)), day_std(Close)))))` |
| R1 | 104 | +2.63 | +2.63 | +3.66 | 20 | -1 | 0.033 | +0.36 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Vwap))))` |
| R1 | 104 | +2.53 | +2.53 | +3.10 | 20 | -1 | 0.031 | -0.12 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(sub(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.51 | +2.51 | +3.15 | 20 | -1 | 0.040 | +0.26 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| R1 | 104 | +2.43 | +2.43 | +3.51 | 20 | -1 | 0.037 | +0.28 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.30 | +2.30 | +2.87 | 20 | -1 | 0.041 | +0.43 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Amt), day_std(Close)), day_std(Amt))))` |
| R1 | 103 | +2.25 | +2.68 | +2.25 | 20 | -1 | 0.042 | +0.23 | `cs_first_low20(day_open(Amt), day_pos_ratio(Ret))` |
| R1 | 104 | +2.20 | +2.20 | +3.70 | 20 | -1 | 0.037 | +0.12 | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_distinct_ratio(Vwap), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret))))` |
| R1 | 104 | +1.90 | +2.08 | +1.90 | 20 | -1 | 0.032 | +0.07 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(day_std(Vwap))))` |
| R1 | 104 | +1.82 | +1.82 | +3.31 | 5 | -1 | 0.024 | +0.31 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_min(Close)), day_min(Close))))` |
| R1 | 107 | +1.76 | +1.76 | +2.39 | 20 | -1 | 0.070 | +0.23 | `cs_demean(cs_mask_top_replace_mean_neg(cs_winsor(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_std(Open))))))` |
| R1 | 103 | +1.71 | +1.71 | +2.86 | 20 | -1 | 0.051 | +0.03 | `cs_first_low20(day_open(Amt), day_distinct_ratio(Amt))` |
| R1 | 104 | +1.57 | +1.76 | +1.57 | 20 | -1 | 0.070 | -0.00 | `cs_mask_top_replace_mean_neg(cs_bucket_zscore(pow_2(cs_robust_z(pow_05(day_gini(Amt)))), ts_scale(pow_2_5(cross_tail_mean_q75(day_argmin(Vwap), 3)), 1)))` |
| R1 | 104 | +1.42 | +1.42 | +2.23 | 20 | -1 | 0.048 | +0.31 | `cs_mask_top_replace_mean_neg(inv(div(div(day_std(Close), day_std(Vwap)), cs_mask_top_replace_mean_neg(inv(div(div(day_std(Close), day_std(Vwap)), day_std(Vwap)))))))` |
| R1 | 104 | +1.20 | +1.20 | +2.44 | 20 | -1 | 0.043 | +0.41 | `cs_mask_top_replace_mean_neg(inv(div(div(div(inv(div(div(day_distinct_ratio(Vwap), day_std(Vwap)), day_std(Vwap))), day_std(Close)), day_std(Close)), day_std(Close))))` |
| R1 | 105 | +1.16 | +1.16 | +3.51 | 5 | -1 | 0.019 | +0.39 | `day_median(nt_cs_last_high40(Vwap, nt_cs_last_high40(Vwap, Close)))` |
| R1 | 105 | +1.07 | +1.07 | +1.53 | 20 | +1 | 0.014 | +0.20 | `day_median(nt_cs_first_high40(High, nt_cs_last_high40(Ret, Close)))` |
| R1 | 103 | +1.02 | +1.02 | +2.36 | 20 | -1 | 0.062 | +0.09 | `cs_first_low20(day_distinct_ratio(Close), day_distinct_ratio(Close))` |

## 通过门槛的前 60 个(含与 heads 相关或与已知族相关的)

| 轮 | 种子 | score | train | valid | 半衰期 | 换手 | ρ已知 | head | 表达式 |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 104 | +2.72 | +2.82 | +2.72 | 20 | 0.026 | +0.16 | 是 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)), day_std(Close)))))` |
| R1 | 104 | +2.65 | +2.65 | +2.84 | 20 | 0.023 | +0.33 |  | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_mean(Vwap), day_std(Close)), day_std(Close)), day_std(Close)), day_std(Close)), day_std(Close))))` |
| R1 | 104 | +2.63 | +2.63 | +3.66 | 20 | 0.033 | +0.36 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Vwap))))` |
| R1 | 104 | +2.62 | +2.62 | +3.77 | 20 | 0.033 | +0.36 |  | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Vwap)), day_std(Vwap))))` |
| R1 | 104 | +2.62 | +2.62 | +3.60 | 20 | 0.032 | +0.36 |  | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close))))` |
| R1 | 104 | +2.62 | +2.62 | +2.74 | 20 | 0.025 | +0.24 |  | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Vwap)), cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Vwap)), day_std(Vwap)))))))` |
| R1 | 104 | +2.59 | +2.59 | +3.54 | 20 | 0.024 | +0.34 |  | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), inv(div(div(day_distinct_ratio(Vwap), day_std(Vwap)), day_std(Vwap)))), day_std(Vwap))))` |
| R1 | 104 | +2.58 | +2.58 | +3.40 | 20 | 0.024 | +0.34 |  | `cs_mask_top_replace_mean_neg(inv(div(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)), day_std(Close))))` |
| R1 | 104 | +2.58 | +2.58 | +3.65 | 20 | 0.038 | +0.20 |  | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)))))` |
| R1 | 104 | +2.54 | +2.54 | +2.96 | 20 | 0.019 | +0.33 |  | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)), day_std(Close)), day_std(Close)), day_std(Close))))` |
| R1 | 104 | +2.54 | +2.54 | +3.06 | 20 | 0.025 | +0.24 |  | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)))))))` |
| R1 | 104 | +2.53 | +2.53 | +3.10 | 20 | 0.031 | -0.12 | 是 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(sub(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.51 | +2.51 | +3.15 | 20 | 0.040 | +0.26 | 是 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| R1 | 104 | +2.43 | +2.43 | +3.51 | 20 | 0.037 | +0.28 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.42 | +2.42 | +2.81 | 20 | 0.019 | +0.33 |  | `cs_mask_top_replace_mean_neg(pow_2_5(div(day_distinct_ratio(Vwap), div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)))))` |
| R1 | 104 | +2.33 | +2.33 | +3.01 | 20 | 0.048 | +0.20 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.30 | +2.30 | +3.36 | 20 | 0.063 | +0.23 |  | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| R1 | 104 | +2.30 | +2.30 | +2.87 | 20 | 0.041 | +0.43 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Amt), day_std(Close)), day_std(Amt))))` |
| R1 | 108 | +2.28 | +2.28 | +3.67 | 20 | 0.031 | +0.78 |  | `day_wstd(Amt, Amt)` |
| R1 | 104 | +2.26 | +2.26 | +3.17 | 20 | 0.045 | +0.20 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close)))))))` |
| R1 | 103 | +2.25 | +2.68 | +2.25 | 20 | 0.042 | +0.23 | 是 | `cs_first_low20(day_open(Amt), day_pos_ratio(Ret))` |
| R1 | 101 | +2.23 | +2.23 | +3.76 | 20 | 0.027 | +0.83 |  | `sub(cross_scale(day_std(Amt), 15), day_wmean(Amt, Volume))` |
| R1 | 103 | +2.23 | +2.23 | +2.39 | 20 | 0.032 | +0.35 |  | `cs_first_low20(day_open(Amt), day_distinct_ratio(Ret))` |
| R1 | 108 | +2.22 | +2.22 | +3.76 | 20 | 0.027 | +0.83 |  | `day_wmean(Amt, Amt)` |
| R1 | 103 | +2.22 | +2.22 | +2.22 | 20 | 0.033 | +0.36 |  | `cs_first_low20(day_open(Amt), day_distinct_ratio(Close))` |
| R1 | 104 | +2.21 | +2.21 | +2.31 | 20 | 0.050 | +0.14 |  | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close))))))))` |
| R1 | 104 | +2.20 | +2.20 | +3.70 | 20 | 0.037 | +0.12 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_distinct_ratio(Vwap), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret))))` |
| R1 | 106 | +2.16 | +2.16 | +3.57 | 20 | 0.026 | +0.81 |  | `mul(add(add(day_gini(Volume), add(day_gini(Volume), day_var(Amt))), add(add(day_gini(Volume), add(day_gini(Volume), day_var(Amt))), day_var(Amt))), day_skew(Amt))` |
| R1 | 101 | +2.11 | +2.11 | +3.59 | 5 | 0.041 | +0.87 |  | `mul(2, pow_2(add(day_sum(Volume), pow_1_5(add(day_sum(Volume), pow_1_5(add(cross_quantile_q75(day_std(Amt), 3), day_var(Low))))))))` |
| R1 | 106 | +2.09 | +2.09 | +3.72 | 20 | 0.029 | +0.81 |  | `add(day_max(Amt), day_argmin(Volume))` |
| R1 | 106 | +2.09 | +2.09 | +3.72 | 20 | 0.029 | +0.81 |  | `add(day_max(Amt), day_skew(Amt))` |
| R1 | 106 | +2.09 | +2.09 | +3.72 | 20 | 0.029 | +0.81 |  | `day_max(Amt)` |
| R1 | 106 | +2.08 | +2.08 | +3.63 | 20 | 0.029 | +0.80 |  | `add(day_max(Amt), day_max(Volume))` |
| R1 | 101 | +2.08 | +2.08 | +3.56 | 5 | 0.054 | +0.85 |  | `mul(5, pow_1_5(add(day_sum(Volume), pow_1_5(pow_1_5(day_std(Amt))))))` |
| R1 | 104 | +2.08 | +2.08 | +3.21 | 20 | 0.058 | +0.31 |  | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))` |
| R1 | 106 | +2.07 | +2.07 | +3.69 | 20 | 0.028 | +0.81 |  | `add(add(day_median(Amt), day_max(Amt)), day_max(Amt))` |
| R1 | 101 | +2.06 | +2.06 | +3.55 | 5 | 0.045 | +0.87 |  | `mul(2, pow_1_5(add(day_sum(Volume), pow_1_5(add(day_sum(Volume), pow_1_5(add(cross_quantile_q75(day_std(Amt), 3), day_var(Low))))))))` |
| R1 | 101 | +2.04 | +2.04 | +3.55 | 5 | 0.045 | +0.87 |  | `mul(2, pow_1_5(add(day_sum(Volume), pow_1_5(pow_1_5(cross_quantile_q75(day_std(Amt), 3))))))` |
| R1 | 101 | +2.04 | +2.04 | +3.55 | 5 | 0.045 | +0.87 |  | `mul(2, pow_1_5(add(day_topw_mean(Amt, Amt), pow_1_5(pow_1_5(cross_quantile_q75(day_std(Amt), 3))))))` |
| R1 | 101 | +2.04 | +2.04 | +3.55 | 5 | 0.045 | +0.87 |  | `mul(0.5, pow_1_5(add(day_sum(Volume), pow_1_5(pow_1_5(cross_quantile_q75(day_std(Amt), 3))))))` |
| R1 | 108 | +2.04 | +2.04 | +3.56 | 20 | 0.031 | +0.81 |  | `day_wstd(Amt, Ret)` |
| R1 | 104 | +2.03 | +2.03 | +3.75 | 20 | 0.044 | +0.38 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close))))` |
| R1 | 101 | +2.03 | +2.03 | +3.55 | 5 | 0.037 | +0.88 |  | `mul(2, pow_1_5(add(day_sum(Volume), pow_1_5(cross_quantile_q75(pow_1_5(add(day_sum(Volume), pow_1_5(cross_quantile_q75(day_std(Amt), 3)))), 3)))))` |
| R1 | 104 | +2.01 | +2.01 | +2.78 | 20 | 0.050 | +0.24 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(day_std(Close)))))` |
| R1 | 104 | +1.97 | +1.97 | +3.46 | 20 | 0.045 | +0.38 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap))))` |
| R1 | 103 | +1.96 | +1.96 | +2.21 | 20 | 0.031 | +0.35 |  | `add(cs_first_low20(day_open(Amt), day_distinct_ratio(Close)), ts_sum(day_at_min_ratio(Ret), 50))` |
| R1 | 101 | +1.95 | +1.95 | +3.44 | 5 | 0.059 | +0.85 |  | `mul(2, pow_1_5(add(day_sum(Volume), pow_1_5(day_std(Amt)))))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_max(Amt), add(day_max(Amt), day_var(Amt))), add(day_max(Amt), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_max(Volume), add(day_max(Volume), day_var(Amt))), add(day_max(Volume), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_max(Volume), add(day_max(Volume), day_var(Amt))), add(add(day_max(Volume), add(day_max(Volume), day_var(Amt))), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_median(Volume), add(day_median(Volume), day_var(Amt))), add(add(day_median(Volume), add(day_median(Volume), day_var(Amt))), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_median(Volume), add(day_median(Volume), day_var(Amt))), add(add(day_median(Volume), day_skew(Amt)), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_median(Volume), add(day_median(Volume), day_var(Amt))), add(add(day_median(Volume), add(day_median(Volume), day_skew(Amt))), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_median(Volume), day_var(Amt)), day_var(Amt))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(day_var(Amt), day_skew(Amt))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(add(day_max(Volume), day_var(Amt)), add(add(day_max(Volume), day_var(Amt)), day_var(Amt))), add(add(add(day_max(Volume), day_var(Amt)), add(add(day_max(Volume), day_var(Amt)), day_var(Amt))), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_median(Amt), add(add(day_median(Volume), day_var(Amt)), day_var(Amt))), add(add(day_median(Volume), day_var(Amt)), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_max(Volume), add(day_max(Volume), day_var(Amt))), add(add(day_median(Volume), day_var(Amt)), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(add(day_median(Volume), day_var(Amt)), add(add(day_median(Volume), day_var(Amt)), day_var(Amt))), add(add(add(day_median(Volume), day_var(Amt)), add(add(day_median(Volume), day_var(Amt)), day_var(Amt))), day_var(Amt)))` |
| R1 | 106 | +1.95 | +1.95 | +3.84 | 20 | 0.024 | +0.85 |  | `add(add(day_median(Volume), add(day_median(Volume), day_var(Amt))), add(add(day_median(Volume), add(add(day_max(Volume), add(day_max(Volume), day_var(Amt))), add(add(day_max(Volume), add(day_max(Volume), day_var(Amt))), day_var(Amt)))), day_var(Amt)))` |

## 没过线里分数最高的 30 个(对照用)

| 轮 | 种子 | score | train | valid | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|
| R1 | 105 | +0.98 | +0.98 | +2.33 | +0.62 | `log(day_cov(Vwap, Volume))` |
| R1 | 108 | +0.98 | +0.98 | +2.53 | +0.72 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 30)), ts_delay(mul(day_flat_run_max(Amt), cs_scale(day_close(Low))), 50))` |
| R1 | 108 | +0.96 | +0.96 | +2.49 | +0.71 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 30)), ts_delay(mul(day_flat_run_max(Amt), day_std(High)), 50))` |
| R1 | 106 | +0.96 | +1.80 | +0.96 | +0.57 | `add(add(day_var(Volume), add(day_var(Volume), day_skew(Amt))), add(day_var(Volume), day_skew(Amt)))` |
| R1 | 107 | +0.96 | +2.51 | +0.96 | +0.32 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_std(Volume)))` |
| R1 | 103 | +0.95 | +0.95 | +3.38 | +0.88 | `day_quantile(Amt)` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `day_median(Amt)` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `add(add(day_median(Amt), add(day_median(Amt), day_skew(Amt))), add(day_median(Amt), day_skew(Amt)))` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `add(day_median(Amt), day_skew(Amt))` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `add(add(day_median(Amt), day_skew(Amt)), day_skew(Amt))` |
| R1 | 105 | +0.95 | +0.95 | +1.27 | +0.24 | `day_open(nt_cs_last_high40(High, Close))` |
| R1 | 106 | +0.95 | +0.95 | +3.35 | +0.88 | `add(add(day_median(Volume), add(day_median(Amt), day_skew(Amt))), add(day_median(Amt), day_skew(Amt)))` |
| R1 | 103 | +0.95 | +0.95 | +3.18 | +0.94 | `add(day_sum(Amt), ts_sum(add(day_sum(Amt), ts_sum(day_at_min_ratio(Ret), 50)), 50))` |
| R1 | 101 | +0.95 | +0.95 | +1.33 | +0.68 | `sqrt(add(add(day_sum(Volume), day_var(Low)), day_var(Low)))` |
| R1 | 101 | +0.95 | +0.95 | +1.33 | +0.68 | `sqrt(day_sum(Volume))` |
| R1 | 108 | +0.94 | +1.49 | +0.94 | +0.49 | `cs_bucket_rank(day_wstd(Volume, Volume), ts_delay(add(day_flat_run_max(Amt), day_std(Low)), 50))` |
| R1 | 104 | +0.93 | +2.12 | +0.93 | +0.04 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(div(day_distinct_ratio(Vwap), day_std(Close))))` |
| R1 | 108 | +0.93 | +0.93 | +2.46 | +0.71 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 30)), ts_delay(mul(day_flat_run_max(Amt), day_std(Close)), 50))` |
| R1 | 106 | +0.92 | +0.92 | +3.24 | +0.88 | `add(add(day_median(Amt), add(day_median(Volume), day_skew(Amt))), add(day_median(Volume), day_skew(Amt)))` |
| R1 | 105 | +0.90 | +0.90 | +2.64 | +0.40 | `day_es_ratio_hi(nt_cs_first_high40(Vwap, Volume))` |
| R1 | 101 | +0.90 | +0.90 | +1.13 | +0.61 | `log(day_topw_mean(Volume, Volume))` |
| R1 | 106 | +0.89 | +1.64 | +0.89 | +0.54 | `add(add(day_median(Volume), day_max(Volume)), day_max(Volume))` |
| R1 | 105 | +0.88 | +0.88 | +2.39 | +0.63 | `log(day_cov(Close, Volume))` |
| R1 | 108 | +0.85 | +0.85 | +2.25 | +0.68 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 10)), ts_delay(mul(day_flat_run_max(Amt), day_close(Amt)), 50))` |
| R1 | 103 | +0.84 | +0.84 | +2.07 | +0.49 | `add(cs_first_low20(day_open(Amt), day_hurst(Close)), day_es_ratio_lo(Close))` |
| R1 | 104 | +0.84 | +0.84 | +2.69 | +0.23 | `cs_mask_top_replace_mean_neg(inv(cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| R1 | 108 | +0.84 | +0.84 | +2.00 | +0.44 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 30)), ts_delay(day_wstd(Amt, Vwap), 50))` |
| R1 | 105 | +0.83 | +0.83 | +2.53 | +0.13 | `day_median(nt_cs_first_low40(Vwap, Close))` |
| R1 | 106 | +0.83 | +1.67 | +0.83 | +0.53 | `day_max(Volume)` |
| R1 | 106 | +0.83 | +1.67 | +0.83 | +0.53 | `add(day_max(Volume), day_skew(Volume))` |

## 算子在通过者里的富集(出现 ≥ 3 次的;lift = 通过者中占比 ÷ 全部存下的候选中占比)

| 算子 | 全部 | 通过 | lift |
|---|---|---|---|
| cross_scale | 20 | 20 | 2.30 |
| cross_quantile_q75 | 29 | 27 | 2.14 |
| nt_cs_last_high40 | 9 | 8 | 2.04 |
| sub | 32 | 28 | 2.01 |
| day_wstd | 40 | 33 | 1.89 |
| day_pos_ratio | 22 | 18 | 1.88 |
| pow_1_5 | 55 | 45 | 1.88 |
| mul | 71 | 57 | 1.84 |
| day_topw_mean | 42 | 33 | 1.80 |
| ts_delay | 42 | 32 | 1.75 |
| day_var | 65 | 49 | 1.73 |
| day_sum | 70 | 52 | 1.71 |
| day_wmean | 22 | 16 | 1.67 |
| cs_demean | 7 | 5 | 1.64 |
| day_std | 169 | 120 | 1.63 |
| cs_bucket_rank | 47 | 33 | 1.61 |
| ts_scale | 3 | 2 | 1.53 |
| add | 185 | 118 | 1.46 |
| pow_2 | 8 | 5 | 1.44 |
| cs_mask_top_replace_mean_neg | 94 | 57 | 1.39 |
| day_flat_run_max | 32 | 19 | 1.36 |
| sqrt | 21 | 12 | 1.31 |
| inv | 61 | 32 | 1.20 |
| ts_sum | 14 | 7 | 1.15 |
| day_distinct_ratio | 87 | 43 | 1.14 |
| … | | | |
| neg | 7 | 0 | 0.00 |
| ts_mean | 3 | 0 | 0.00 |
| cross_fangzheng | 3 | 0 | 0.00 |
| ts_autocorr_s1 | 4 | 0 | 0.00 |
| cs_last_high40 | 3 | 0 | 0.00 |
| cs_last_high10 | 4 | 0 | 0.00 |
| cross_corr | 3 | 0 | 0.00 |
| ts_quantile_q75 | 4 | 0 | 0.00 |
| cross_regres | 3 | 0 | 0.00 |
| cross_semistd_neg | 3 | 0 | 0.00 |

## 叶子字段在通过者里的富集(出现 ≥ 3 次的;lift = 通过者中占比 ÷ 全部存下的候选中占比)

| 叶子字段 | 全部 | 通过 | lift |
|---|---|---|---|
| Amt | 271 | 183 | 1.55 |
| Volume | 153 | 84 | 1.26 |
| Low | 72 | 37 | 1.18 |
| Close | 206 | 85 | 0.95 |
| Vwap | 151 | 54 | 0.82 |
| High | 103 | 32 | 0.71 |
| Open | 80 | 23 | 0.66 |
| Ret | 44 | 12 | 0.63 |

注意:存下的候选只是每次运行 archive 里按适应度排前 80 的,不是全部提议;门槛废品不在里面。
