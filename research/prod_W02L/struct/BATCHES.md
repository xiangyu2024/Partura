# W02L 结构分批(手写库 L + 挖掘库 X;只用表达式结构;表里的统计只用样本内 2018-01-02 ~ 2023-08-07)

参数:细聚类切点余弦距离 0.6;每批 8 ~ 60 条;小块并入最相似的批要求质心余弦 ≥ 0.3;剩下的在 0.85 上再聚一次;主题 = 结构批按质心再聚类(切点 0.98,每个主题 ≤ 10 批)。

解析 5583 / 5598 条(失败 15 条,都是 `day_sum(in_slice(Volume, 1, 1))` 一类在现在的解析器下不合法的手写式)。批 240 个:结构批 198 个(4187 条),残余批 42 个(1396 条);主题 58 个。

## 主题

| 主题 | 批数 | 条数 | L / X | 冠军族成员 | 量额叶子 | 禁用算子 | 训练 |rank IC| 最大 | 共有子结构(最大那批) |
|---|---|---|---|---|---|---|---|---|
| T01 | 9 | 236 | 1 / 235 | 61 | 66% | 0% | 0.054 | `O:day_max(F)` |
| T02 | 9 | 228 | 0 / 228 | 97 | 54% | 2% | 0.060 | `O:day_cov(F,F)` |
| T03 | 10 | 194 | 0 / 194 | 122 | 44% | 1% | 0.061 | `O:day_durbin_watson(F)` |
| T04 | 10 | 180 | 1 / 179 | 46 | 79% | 0% | 0.061 | `O:ts_decay_linear(O:sigmoid(O:pow_05(O:day_ar1_coefficient(F))))` |
| T05 | 9 | 170 | 1 / 169 | 19 | 34% | 4% | 0.049 | `O:day_close(F)` |
| T06 | 5 | 152 | 28 / 124 | 16 | 18% | 3% | 0.044 | `O:day_hurst(F)` |
| T07 | 6 | 150 | 3 / 147 | 11 | 43% | 2% | 0.037 | `O:day_skew(F)` |
| T08 | 8 | 143 | 0 / 143 | 32 | 66% | 0% | 0.042 | `O:day_argmin(F)` |
| T09 | 4 | 139 | 0 / 139 | 10 | 34% | 2% | 0.049 | `O:day_quantile_q75(F)` |
| T10 | 10 | 134 | 134 / 0 | 89 | 93% | 0% | 0.055 | `O:day_q_stat_std(O:div(O:in_slice(F),O:in_sum(O:in_slice(F))))` |
| T11 | 8 | 126 | 0 / 126 | 77 | 21% | 1% | 0.059 | `O:day_mean(F)` |
| T12 | 6 | 122 | 64 / 58 | 44 | 70% | 1% | 0.054 | `O:day_first(F)` |
| T13 | 5 | 114 | 59 / 55 | 12 | 57% | 0% | 0.052 | `O:create_valid_mask(O:sub(O:div(O:day_last(F),O:ts_delay(O:day_last(F))),C:pct))` |
| T14 | 6 | 112 | 44 / 68 | 53 | 78% | 1% | 0.051 | `O:day_sum(F)` |
| T15 | 5 | 102 | 102 / 0 | 74 | 56% | 0% | 0.051 | `O:energy_ratio_n(O:delete_open_close(F))` |
| T16 | 2 | 100 | 0 / 100 | 3 | 28% | 2% | 0.046 | `O:day_argmax(F)` |
| T17 | 3 | 100 | 0 / 100 | 17 | 56% | 1% | 0.056 | `O:day_autocorr_n1(F)` |
| T18 | 4 | 95 | 39 / 56 | 41 | 89% | 3% | 0.054 | `O:cross_sum(O:log(F))` |
| T19 | 4 | 92 | 92 / 0 | 22 | 37% | 0% | 0.049 | `O:day_mean(O:select_where(O:eq(O:in_roll_labels(F),C:scl),O:create_like(O:in_sli` |
| T20 | 3 | 89 | 3 / 86 | 5 | 21% | 0% | 0.033 | `O:day_kurt(F)` |
| T21 | 3 | 84 | 84 / 0 | 68 | 100% | 0% | 0.056 | `O:mul(O:replace_small_with_nan(O:is_gt(O:sub(O:in_slice(F),O:in_delay(O:in_slice` |
| T22 | 3 | 81 | 6 / 75 | 4 | 48% | 1% | 0.042 | `O:day_corr(F,F)` |
| T23 | 3 | 79 | 0 / 79 | 13 | 16% | 66% | 0.035 | `O:cross_delta(F)` |
| T24 | 3 | 78 | 0 / 78 | 21 | 26% | 0% | 0.053 | `O:day_var(F)` |
| T25 | 4 | 77 | 1 / 76 | 1 | 4% | 1% | 0.040 | `O:day_min(F)` |
| T26 | 3 | 62 | 6 / 56 | 8 | 34% | 3% | 0.054 | `O:day_std(F)` |
| T27 | 4 | 62 | 62 / 0 | 49 | 3% | 0% | 0.056 | `O:select_where(O:is_gt(F,O:create_like(F)),O:sub(F,O:in_mean_full(O:select_where` |
| T28 | 3 | 58 | 0 / 58 | 0 | 16% | 100% | 0.027 | `O:pow_1_5(O:log(O:nt_ts_kurt(F)))` |
| T29 | 2 | 57 | 0 / 57 | 1 | 2% | 0% | 0.035 | `O:ts_max(O:cross_med(O:day_ar1_coefficient(F)))` |
| T30 | 3 | 51 | 51 / 0 | 18 | 100% | 0% | 0.051 | `O:neg(O:sub(O:day_argmin(O:in_slice_to_end(O:in_local_mean(O:in_slice(F)),O:day_` |
| T31 | 4 | 50 | 0 / 50 | 10 | 38% | 58% | 0.048 | `O:cross_sum(F)` |
| T32 | 2 | 45 | 0 / 45 | 3 | 9% | 100% | 0.033 | `O:nt_ts_autocorr_s1(F)` |
| T33 | 2 | 40 | 0 / 40 | 9 | 2% | 100% | 0.052 | `O:pow_2_5(O:nt_ts_var(F))` |
| T34 | 2 | 39 | 0 / 39 | 11 | 54% | 21% | 0.050 | `O:day_max(O:cross_corr(F,F))` |
| T35 | 2 | 36 | 0 / 36 | 20 | 97% | 100% | 0.050 | `O:day_durbin_watson(O:nt_cs_quantile_q25(F))` |
| T36 | 3 | 35 | 0 / 35 | 20 | 11% | 11% | 0.056 | `O:pow_2(F)` |
| T37 | 2 | 34 | 0 / 34 | 4 | 29% | 15% | 0.036 | `O:sigmoid(F)` |
| T38 | 2 | 34 | 0 / 34 | 2 | 68% | 100% | 0.042 | `O:cross_min(O:day_max(O:nt_cs_regres(F,F)))` |
| T39 | 2 | 32 | 0 / 32 | 5 | 97% | 0% | 0.061 | `O:ts_decay_linear(O:day_ar1_coefficient(F))` |
| T40 | 1 | 31 | 0 / 31 | 3 | 65% | 100% | 0.041 | `O:nt_ts_skew(F)` |
| T41 | 1 | 30 | 30 / 0 | 26 | 100% | 0% | 0.054 | `O:div(O:in_slice(O:in_zscore_rolling(F)),O:in_sum(O:in_slice(O:in_zscore_rolling` |
| T42 | 1 | 30 | 30 / 0 | 0 | 100% | 0% | 0.019 | `O:day_pdf_quantile_single(F,F)` |
| T43 | 2 | 29 | 0 / 29 | 0 | 24% | 0% | 0.017 | `O:cross_argmax(O:day_ar1_coefficient(F))` |
| T44 | 1 | 28 | 28 / 0 | 6 | 39% | 0% | 0.021 | `O:div(O:in_regres(F,O:in_mean_full(F)),O:add(O:in_stddev_full(O:in_regres(F,O:in` |
| T45 | 1 | 24 | 24 / 0 | 14 | 100% | 0% | 0.017 | `O:day_pdf_tail_sum_m(F,F)` |
| T46 | 1 | 23 | 0 / 23 | 3 | 83% | 0% | 0.061 | `O:sigmoid(O:day_ar1_coefficient(F))` |
| T47 | 1 | 20 | 0 / 20 | 0 | 80% | 100% | 0.050 | `O:nt_ts_min(F)` |
| T48 | 1 | 20 | 0 / 20 | 12 | 50% | 100% | 0.048 | `O:nt_ts_cov(F,F)` |
| T49 | 1 | 19 | 0 / 19 | 1 | 11% | 26% | 0.058 | `O:inv(F)` |
| T50 | 1 | 19 | 0 / 19 | 9 | 37% | 5% | 0.056 | `O:pow_2_5(F)` |
| T51 | 1 | 18 | 0 / 18 | 5 | 17% | 100% | 0.059 | `O:nt_ts_max(F)` |
| T52 | 1 | 18 | 0 / 18 | 2 | 0% | 100% | 0.051 | `O:nt_ts_mean(F)` |
| T53 | 1 | 14 | 0 / 14 | 0 | 14% | 0% | 0.030 | `O:day_q_stat_std(O:in_max_rolling(F))` |
| T54 | 1 | 13 | 13 / 0 | 11 | 100% | 0% | 0.036 | `O:div(O:add(O:ts_mean(O:abs_(O:cs_demean(O:day_sum(O:sub(O:in_sorted_cumsum_forw` |
| T55 | 1 | 11 | 0 / 11 | 0 | 82% | 0% | 0.037 | `O:day_durbin_watson(O:sliding_bottom_mean_masked_p5(F,F))` |
| T56 | 1 | 10 | 0 / 10 | 1 | 40% | 90% | 0.034 | `O:day_mean(O:nt_cs_normalize(O:in_cov(F,F)))` |
| T57 | 1 | 9 | 9 / 0 | 0 | 100% | 0% | 0.009 | `O:day_kurt(O:div(F,O:in_sum(F)))` |
| T58 | 1 | 9 | 0 / 9 | 1 | 0% | 67% | 0.026 | `O:signedpower(O:cross_med(F))` |
| R | 42 | 1396 | 462 / 934 | 415 | 49% | 16% | 0.062 | `O:abs_(O:in_delay(F))` |

## 批

| 批 | 主题 | 条数 | L / X | 冠军族成员(族数) | 骨架数 | 批内结构相似 | 量额叶子 | 禁用算子 | 训练 |rank IC| 中位 / 最大 | 适应度最大 | 共有子结构 | 代表式 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B001 | T01 | 47 | 1 / 46 | 12(4) | 30 | 0.25 | 49% | 0% | 0.036 / 0.054 | 0.042 | `O:day_max(F)` | `day_max(Amt)` |
| B002 | T01 | 47 | 0 / 47 | 13(3) | 19 | 0.63 | 94% | 0% | 0.029 / 0.050 | 0.035 | `O:ts_quantile_q75(O:ts_quantile_q75(O:day_q_stat_std(F)))` | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 5), 20)` |
| B003 | T01 | 42 | 0 / 42 | 0(0) | 35 | 0.39 | 33% | 0% | 0.008 / 0.050 | 0.031 | `O:day_q_stat_std(F)` | `ts_var(day_q_stat_std(Volume), 50)` |
| B004 | T01 | 33 | 0 / 33 | 12(5) | 29 | 0.33 | 91% | 0% | 0.017 / 0.031 | 0.026 | `O:ts_hurst(O:div(O:day_last(F),O:day_max(F)))` | `ts_mean(mul(div(day_last(Volume), day_max(Low)), ts_hurst(div(day_last(Volume), day_max(Lo` |
| B005 | T01 | 21 | 0 / 21 | 4(3) | 20 | 0.42 | 76% | 0% | 0.019 / 0.035 | 0.032 | `O:log(O:add(O:day_q_stat_std(F),O:day_std(F)))` | `ts_mean(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(log(add(day_q_stat` |
| B006 | T01 | 16 | 0 / 16 | 3(3) | 12 | 0.53 | 94% | 0% | 0.020 / 0.035 | 0.030 | `O:mul(O:log(O:add(O:day_q_stat_std(F),O:day_std(F))),O:ts_hurst(O:div(` | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_la` |
| B007 | T01 | 11 | 0 / 11 | 4(3) | 5 | 0.79 | 73% | 0% | 0.016 / 0.032 | 0.028 | `O:ts_mean(O:mul(O:log(O:add(O:mul(O:log(O:add(O:day_q_stat_std(F),O:da` | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_la` |
| B008 | T01 | 11 | 0 / 11 | 10(1) | 10 | 0.55 | 0% | 0% | 0.045 / 0.045 | 0.009 | `O:sigmoid(O:sigmoid(O:day_max(F)))` | `sigmoid(sigmoid(day_max(Ret)))` |
| B009 | T01 | 8 | 0 / 8 | 3(1) | 6 | 0.66 | 62% | 0% | 0.019 / 0.037 | 0.032 | `O:ts_sum(O:day_q_stat_std(F))` | `ts_sum(day_q_stat_std(Volume), 50)` |
| B010 | T02 | 58 | 0 / 58 | 12(8) | 40 | 0.31 | 59% | 3% | 0.020 / 0.048 | 0.033 | `O:day_cov(F,F)` | `day_cov(Volume, Ret)` |
| B011 | T02 | 29 | 0 / 29 | 2(1) | 25 | 0.46 | 7% | 0% | 0.016 / 0.030 | 0.024 | `O:mul(O:day_autocorr_n1(F),O:day_std(F))` | `cross_stddev(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High),` |
| B012 | T02 | 29 | 0 / 29 | 23(7) | 15 | 0.55 | 83% | 3% | 0.027 / 0.056 | 0.040 | `O:ts_std(O:day_cov(F,F))` | `ts_std(ts_std(day_cov(Ret, Volume), 30), 40)` |
| B013 | T02 | 25 | 0 / 25 | 18(5) | 19 | 0.41 | 76% | 0% | 0.040 / 0.060 | 0.042 | `O:cross_max(O:day_cov(F,F))` | `cross_max(day_cov(Amt, Low), 5)` |
| B014 | T02 | 25 | 0 / 25 | 8(2) | 12 | 0.54 | 0% | 0% | 0.023 / 0.035 | 0.028 | `O:cross_mean(O:day_cov(F,F))` | `cross_quantile_q25(cross_mean(day_cov(Low, Ret), 60), 15)` |
| B015 | T02 | 21 | 0 / 21 | 19(9) | 16 | 0.44 | 86% | 5% | 0.025 / 0.045 | 0.036 | `O:cross_stddev(O:day_cov(F,F))` | `add(ts_quantile_q50(cross_max(cross_fangzheng(ts_std(cross_stddev(day_cov(Amt, Amt), 60), ` |
| B016 | T02 | 16 | 0 / 16 | 0(0) | 5 | 0.71 | 88% | 0% | 0.026 / 0.036 | -0.048 | `O:sub(C:pct,O:abs_(O:ts_regres(O:day_cov(F,F),O:day_last(F))))` | `sub(0.5, abs_(ts_regres(day_cov(Open, Open), day_last(Volume), 50)))` |
| B017 | T02 | 14 | 0 / 14 | 4(1) | 11 | 0.42 | 0% | 0% | 0.020 / 0.042 | 0.033 | `O:cross_min(O:day_cov(F,F))` | `cross_mean(cross_min(day_cov(Low, Ret), 15), 60)` |
| B018 | T02 | 11 | 0 / 11 | 11(7) | 11 | 0.59 | 100% | 0% | 0.023 / 0.042 | 0.027 | `O:cross_fangzheng(O:cross_max(O:day_cov(F,F)))` | `ts_stddev(cross_fangzheng(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 241), 5)` |
| B019 | T03 | 37 | 0 / 37 | 21(5) | 28 | 0.22 | 27% | 0% | 0.046 / 0.054 | 0.041 | `O:day_durbin_watson(F)` | `day_durbin_watson(Vwap)` |
| B020 | T03 | 32 | 0 / 32 | 21(8) | 25 | 0.28 | 88% | 0% | 0.040 / 0.061 | 0.048 | `O:cross_decay_linear(F)` | `day_quantile_q75(cross_sum(cross_decay_linear(Amt, 3), 3))` |
| B021 | T03 | 25 | 0 / 25 | 15(7) | 24 | 0.37 | 76% | 4% | 0.045 / 0.061 | 0.046 | `O:day_close(O:in_relative_distance_m(F))` | `cross_max(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(cross_max(ts_min(pow_3(` |
| B022 | T03 | 19 | 0 / 19 | 12(3) | 14 | 0.48 | 26% | 5% | 0.038 / 0.056 | 0.044 | `O:ts_sum(O:log(O:day_durbin_watson(F)))` | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10)` |
| B023 | T03 | 17 | 0 / 17 | 15(6) | 9 | 0.58 | 18% | 0% | 0.042 / 0.057 | 0.046 | `O:cross_fangzheng(O:day_durbin_watson(F))` | `cross_fangzheng(day_durbin_watson(Vwap), 30)` |
| B024 | T03 | 15 | 0 / 15 | 2(1) | 14 | 0.43 | 47% | 0% | 0.042 / 0.049 | 0.029 | `O:sigmoid(O:pow_2(O:day_durbin_watson(F)))` | `ts_var(pow_2(day_durbin_watson(Ret)), 10)` |
| B025 | T03 | 14 | 0 / 14 | 14(3) | 9 | 0.55 | 36% | 0% | 0.043 / 0.053 | 0.040 | `O:log(O:log(O:day_durbin_watson(F)))` | `ts_sum(log(log(day_durbin_watson(Vwap))), 40)` |
| B026 | T03 | 14 | 0 / 14 | 14(4) | 7 | 0.71 | 0% | 0% | 0.051 / 0.055 | 0.044 | `O:ts_max(O:day_durbin_watson(F))` | `ts_max(day_durbin_watson(Close), 1)` |
| B027 | T03 | 12 | 0 / 12 | 0(0) | 11 | 0.57 | 67% | 0% | 0.043 / 0.050 | 0.033 | `O:sigmoid(O:day_durbin_watson(F))` | `sqrt(neg(sigmoid(day_durbin_watson(Amt))))` |
| B028 | T03 | 9 | 0 / 9 | 8(3) | 6 | 0.65 | 11% | 0% | 0.046 / 0.053 | 0.044 | `O:ts_sum(O:day_durbin_watson(F))` | `ts_sum(day_durbin_watson(Vwap), 20)` |
| B029 | T04 | 41 | 0 / 41 | 12(1) | 32 | 0.47 | 95% | 0% | 0.051 / 0.060 | 0.044 | `O:ts_decay_linear(O:sigmoid(O:pow_05(O:day_ar1_coefficient(F))))` | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 10)` |
| B030 | T04 | 31 | 1 / 30 | 2(2) | 20 | 0.32 | 35% | 0% | 0.017 / 0.052 | 0.031 | `O:day_ar1_coefficient(F)` | `log(day_ar1_coefficient(Volume))` |
| B031 | T04 | 20 | 0 / 20 | 4(1) | 13 | 0.46 | 80% | 0% | 0.045 / 0.060 | 0.043 | `O:pow_05(O:day_ar1_coefficient(F))` | `pow_05(day_ar1_coefficient(Volume))` |
| B032 | T04 | 18 | 0 / 18 | 3(1) | 13 | 0.45 | 72% | 0% | 0.052 / 0.061 | 0.045 | `O:pow_2(O:day_ar1_coefficient(F))` | `pow_2(day_ar1_coefficient(Volume))` |
| B033 | T04 | 14 | 0 / 14 | 6(1) | 12 | 0.53 | 100% | 0% | 0.050 / 0.061 | 0.044 | `O:ts_decay_linear(O:sigmoid(O:pow_2(O:pow_05(O:day_ar1_coefficient(F))` | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)))` |
| B034 | T04 | 14 | 0 / 14 | 8(1) | 10 | 0.75 | 100% | 0% | 0.056 / 0.061 | 0.044 | `O:pow_2(O:cs_rank(O:ts_decay_linear(O:pow_2(O:pow_05(O:day_ar1_coeffic` | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))` |
| B035 | T04 | 13 | 0 / 13 | 5(2) | 6 | 0.73 | 54% | 0% | 0.034 / 0.052 | 0.041 | `O:ts_quantile_q75(O:day_ar1_coefficient(F))` | `ts_quantile_q75(day_ar1_coefficient(Volume), 1)` |
| B036 | T04 | 12 | 0 / 12 | 1(1) | 10 | 0.53 | 92% | 0% | 0.055 / 0.061 | 0.045 | `O:pow_2(O:pow_05(O:day_ar1_coefficient(F)))` | `ts_quantile_q75(pow_2(pow_05(day_ar1_coefficient(Volume))), 10)` |
| B037 | T04 | 9 | 0 / 9 | 2(1) | 9 | 0.75 | 100% | 0% | 0.050 / 0.060 | 0.044 | `O:sigmoid(O:pow_05(O:pow_2(O:pow_05(O:day_ar1_coefficient(F)))))` | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5), 5)` |
| B038 | T04 | 8 | 0 / 8 | 3(1) | 8 | 0.64 | 100% | 0% | 0.052 / 0.059 | 0.043 | `O:sigmoid(O:pow_05(O:pow_05(O:day_ar1_coefficient(F))))` | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(sigmoid(pow_05(pow_05(day_ar1_coefficient(` |
| B039 | T05 | 53 | 1 / 52 | 4(3) | 41 | 0.28 | 34% | 6% | 0.011 / 0.049 | 0.036 | `O:day_close(F)` | `ts_pearson(day_close(High), 40)` |
| B040 | T05 | 29 | 0 / 29 | 3(3) | 24 | 0.29 | 28% | 3% | 0.011 / 0.044 | 0.028 | `O:day_quantile_q25(F)` | `ts_spearman(day_quantile_q25(Ret), 20)` |
| B041 | T05 | 21 | 0 / 21 | 0(0) | 18 | 0.55 | 0% | 0% | 0.015 / 0.027 | 0.019 | `O:ts_cov(O:day_quantile_q25(F),O:day_close(F))` | `ts_kurt(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40)` |
| B042 | T05 | 15 | 0 / 15 | 1(1) | 12 | 0.52 | 7% | 13% | 0.018 / 0.047 | 0.029 | `O:day_std(O:pow_3(F))` | `day_std(pow_3(Open))` |
| B043 | T05 | 13 | 0 / 13 | 3(2) | 8 | 0.65 | 54% | 0% | 0.019 / 0.037 | 0.027 | `O:cross_stddev(O:day_quantile_q25(F))` | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 50)` |
| B044 | T05 | 11 | 0 / 11 | 3(2) | 10 | 0.56 | 64% | 0% | 0.016 / 0.035 | 0.018 | `O:day_quantile_q25(O:sliding_top_sum_masked_p5(F,F))` | `div(ts_quantile_q50(cross_max(day_close(Volume), 5), 40), day_quantile_q25(sliding_top_sum` |
| B045 | T05 | 11 | 0 / 11 | 4(2) | 5 | 0.69 | 82% | 0% | 0.032 / 0.047 | 0.025 | `O:day_quantile_q75(O:add(F,O:day_close(F)))` | `cs_mask_top_replace_mean(day_quantile_q75(add(Amt, day_close(Volume))))` |
| B046 | T05 | 9 | 0 / 9 | 0(0) | 9 | 0.67 | 22% | 0% | 0.008 / 0.026 | 0.009 | `O:day_quantile_q25(F)` | `day_hurst(add(day_quantile_q25(Open), Open))` |
| B047 | T05 | 8 | 0 / 8 | 1(1) | 6 | 0.65 | 75% | 0% | 0.049 / 0.049 | 0.027 | `O:pow_05(O:day_close(F))` | `pow_05(pow_05(day_close(Amt)))` |
| B048 | T06 | 60 | 1 / 59 | 2(1) | 50 | 0.29 | 27% | 2% | 0.009 / 0.035 | 0.026 | `O:day_hurst(F)` | `day_hurst(Open)` |
| B049 | T06 | 58 | 3 / 55 | 4(2) | 47 | 0.27 | 17% | 5% | 0.010 / 0.041 | 0.019 | `O:day_quantile(F)` | `day_quantile(Ret, 0.95)` |
| B050 | T06 | 12 | 12 / 0 | 5(2) | 12 | 0.64 | 0% | 0% | 0.015 / 0.038 | 0.026 | `O:div(O:div(O:day_sum(O:select_where(O:is_gt(O:sub(O:div(F,O:in_delay(` | `sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Clo` |
| B051 | T06 | 12 | 12 / 0 | 5(2) | 12 | 0.62 | 17% | 0% | 0.010 / 0.044 | -0.012 | `O:day_mean(O:is_lt(O:sub(O:div(F,O:in_delay(F)),O:create_like(F)),O:da` | `sub(day_mean(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantil` |
| B052 | T06 | 10 | 0 / 10 | 0(0) | 9 | 0.80 | 0% | 0% | 0.008 / 0.015 | 0.013 | `O:cross_argmax(O:day_quantile(F))` | `ts_std(cross_argmax(cross_argmax(day_quantile(Ret), 60), 60), 50)` |
| B053 | T07 | 49 | 3 / 46 | 3(3) | 41 | 0.30 | 22% | 6% | 0.008 / 0.037 | 0.019 | `O:day_skew(F)` | `ts_stddev(day_skew(Vwap), 20)` |
| B054 | T07 | 33 | 0 / 33 | 4(3) | 21 | 0.57 | 21% | 0% | 0.011 / 0.036 | 0.035 | `O:cross_quantile_q75(O:cross_corr(O:day_skew(F),O:mul(O:day_mean(F),O:` | `signedpower(cross_quantile_q75(cross_corr(day_skew(Vwap), mul(day_mean(High), day_skew(Hig` |
| B055 | T07 | 26 | 0 / 26 | 4(2) | 24 | 0.40 | 65% | 0% | 0.012 / 0.034 | 0.026 | `O:mul(O:day_mean(F),O:day_skew(F))` | `signedpower(mul(day_mean(High), day_skew(Volume)))` |
| B056 | T07 | 18 | 0 / 18 | 0(0) | 14 | 0.58 | 72% | 0% | 0.008 / 0.023 | 0.013 | `O:cross_corr(O:cross_delta(O:day_quantile_q75(F)),O:mul(O:day_mean(F),` | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_quantile_q75(cross_corr(cross_` |
| B057 | T07 | 14 | 0 / 14 | 0(0) | 9 | 0.63 | 93% | 0% | 0.007 / 0.021 | 0.016 | `O:signedpower(O:cross_quantile_q75(O:cross_corr(O:day_mean(F),O:mul(O:` | `signedpower(cross_quantile_q75(cross_corr(day_mean(Vwap), mul(day_mean(High), day_skew(Vol` |
| B058 | T07 | 10 | 0 / 10 | 0(0) | 5 | 0.74 | 40% | 0% | 0.010 / 0.011 | -0.013 | `O:abs_(O:day_skew(F))` | `abs_(day_skew(High))` |
| B059 | T08 | 58 | 0 / 58 | 5(1) | 47 | 0.26 | 55% | 0% | 0.012 / 0.032 | 0.021 | `O:day_argmin(F)` | `ts_sum(cross_cov(day_argmin(Amt), day_argmin(Amt), 15), 50)` |
| B060 | T08 | 17 | 0 / 17 | 3(1) | 14 | 0.55 | 76% | 0% | 0.018 / 0.042 | 0.019 | `O:ts_sum(O:day_argmin(F))` | `add(day_argmin(Amt), log(ts_sum(day_argmin(Amt), 50)))` |
| B061 | T08 | 16 | 0 / 16 | 7(1) | 14 | 0.48 | 88% | 0% | 0.016 / 0.032 | 0.020 | `O:pow_1_5(O:day_argmin(F))` | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(pow_1_5(ts_quantile_q75(pow_1_5(day_argmin` |
| B062 | T08 | 14 | 0 / 14 | 9(1) | 13 | 0.51 | 93% | 0% | 0.022 / 0.029 | 0.019 | `O:sigmoid(O:ts_max(O:inv(O:day_argmin(F))))` | `sigmoid(ts_max(inv(day_argmin(Volume)), 10))` |
| B063 | T08 | 12 | 0 / 12 | 2(1) | 11 | 0.56 | 83% | 0% | 0.011 / 0.026 | 0.014 | `O:inv(O:day_argmin(F))` | `ts_max(sigmoid(sigmoid(sigmoid(ts_quantile_q75(inv(day_argmin(Volume)), 50)))), 10)` |
| B064 | T08 | 9 | 0 / 9 | 0(0) | 7 | 0.58 | 0% | 0% | 0.012 / 0.023 | -0.018 | `O:log(O:day_argmin(F))` | `ts_quantile_q75(mul(log(day_argmin(Low)), 5), 10)` |
| B065 | T08 | 9 | 0 / 9 | 6(1) | 6 | 0.57 | 78% | 0% | 0.023 / 0.032 | 0.019 | `O:ts_quantile_q50(O:day_argmin(F))` | `ts_quantile_q50(day_argmin(Amt), 40)` |
| B066 | T08 | 8 | 0 / 8 | 0(0) | 5 | 0.77 | 75% | 0% | 0.019 / 0.028 | -0.023 | `O:cs_mask_top_replace_mean(O:day_argmin(F))` | `cs_mask_top_replace_mean(day_argmin(Amt))` |
| B067 | T09 | 54 | 0 / 54 | 10(6) | 45 | 0.27 | 37% | 2% | 0.012 / 0.043 | 0.035 | `O:day_quantile_q75(F)` | `pow_2(day_quantile_q75(Volume))` |
| B068 | T09 | 48 | 0 / 48 | 0(0) | 47 | 0.31 | 46% | 4% | 0.010 / 0.041 | 0.016 | `O:day_median(F)` | `log(day_median(Amt))` |
| B069 | T09 | 26 | 0 / 26 | 0(0) | 21 | 0.34 | 12% | 0% | 0.010 / 0.029 | 0.010 | `O:sigmoid(O:day_quantile_q75(F))` | `ts_max(neg(sqrt(sigmoid(day_quantile_q75(High)))), 10)` |
| B070 | T09 | 11 | 0 / 11 | 0(0) | 11 | 0.59 | 18% | 0% | 0.011 / 0.049 | 0.011 | `O:abs_(O:cs_mean(O:ts_pearson(O:day_quantile_q75(F))))` | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), cross_argmax(cs_sum(ts_pearson(da` |
| B071 | T10 | 30 | 30 / 0 | 30(2) | 5 | 0.63 | 100% | 0% | 0.047 / 0.054 | 0.039 | `O:day_q_stat_std(O:div(O:in_slice(F),O:in_sum(O:in_slice(F))))` | `day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 5)` |
| B072 | T10 | 15 | 15 / 0 | 12(5) | 14 | 0.67 | 100% | 0% | 0.020 / 0.053 | 0.040 | `O:day_mean(O:in_sustain_stddev(O:is_gt(O:in_slice(F),O:add(O:in_mean_f` | `day_mean(in_sustain_stddev(is_gt(in_slice(Volume, 11, 240), add(in_mean_full(in_slice(Volu` |
| B073 | T10 | 14 | 14 / 0 | 10(5) | 9 | 0.66 | 100% | 0% | 0.030 / 0.055 | 0.043 | `O:day_std(O:in_topk_masked(O:in_slice(F),O:in_slice(F)))` | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 5))` |
| B074 | T10 | 14 | 14 / 0 | 4(2) | 4 | 0.67 | 100% | 0% | 0.016 / 0.041 | 0.028 | `O:div(O:day_sum(O:mul(O:in_slice(F),O:in_slice(F))),O:day_sum(O:in_sli` | `div(day_sum(mul(in_slice(Ret, 1, 20), in_slice(Volume, 1, 20))), day_sum(in_slice(Volume, ` |
| B075 | T10 | 12 | 12 / 0 | 0(0) | 3 | 0.68 | 100% | 0% | 0.004 / 0.016 | -0.006 | `O:day_pdf_quantile_bilateral_half_width(O:in_slice(F),O:in_slice(F))` | `day_pdf_quantile_bilateral_half_width(in_slice(Ret, 2, 240), in_slice(Volume, 2, 240), 0.9` |
| B076 | T10 | 10 | 10 / 0 | 10(4) | 5 | 0.59 | 100% | 0% | 0.050 / 0.054 | 0.041 | `O:day_ar1_coefficient(O:div(O:in_slice(F),O:in_sum(O:in_slice(F))))` | `day_ar1_coefficient(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` |
| B077 | T10 | 10 | 10 / 0 | 10(4) | 5 | 0.59 | 100% | 0% | 0.042 / 0.045 | 0.035 | `O:day_durbin_watson(O:div(O:in_slice(F),O:in_sum(O:in_slice(F))))` | `day_durbin_watson(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` |
| B078 | T10 | 10 | 10 / 0 | 10(4) | 5 | 0.59 | 100% | 0% | 0.050 / 0.054 | 0.041 | `O:day_autocorr(O:div(O:in_slice(F),O:in_sum(O:in_slice(F))))` | `day_autocorr(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))), 1)` |
| B079 | T10 | 10 | 10 / 0 | 1(1) | 4 | 0.60 | 0% | 0% | 0.024 / 0.040 | 0.006 | `O:day_q_stat_std(O:in_slice(F))` | `day_q_stat_std(in_slice(Ret, 11, 230), 5)` |
| B080 | T10 | 9 | 9 / 0 | 2(1) | 8 | 0.68 | 100% | 0% | 0.012 / 0.044 | 0.001 | `O:div(O:day_std(O:in_topk_masked(O:in_slice(F),O:in_slice(F))),O:add(O` | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(da` |
| B081 | T11 | 27 | 0 / 27 | 2(2) | 20 | 0.36 | 15% | 4% | 0.021 / 0.049 | 0.032 | `O:day_mean(F)` | `cross_stddev(cs_quantile_q75(day_mean(Ret)), 15)` |
| B082 | T11 | 26 | 0 / 26 | 22(7) | 21 | 0.38 | 0% | 0% | 0.044 / 0.059 | 0.047 | `O:cs_demean(O:sub(O:day_mean(F),C:scl))` | `pow_2(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 5)), 10), sub(day_me` |
| B083 | T11 | 14 | 0 / 14 | 11(7) | 11 | 0.69 | 0% | 0% | 0.027 / 0.045 | 0.038 | `O:ts_max(O:cs_demean(O:sub(O:ts_max(O:cs_demean(O:sub(O:day_mean(F),C:` | `pow_1_5(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 5)), 10), 5)), 30))` |
| B084 | T11 | 14 | 0 / 14 | 3(2) | 12 | 0.56 | 71% | 0% | 0.017 / 0.030 | 0.027 | `O:pow_3(O:day_mean(F))` | `ts_min(pow_3(day_mean(Volume)), 30)` |
| B085 | T11 | 13 | 0 / 13 | 10(4) | 11 | 0.62 | 92% | 0% | 0.026 / 0.041 | 0.036 | `O:ts_std(O:day_mean(F))` | `ts_std(ts_std(day_mean(Amt), 40), 40)` |
| B086 | T11 | 12 | 0 / 12 | 11(4) | 10 | 0.73 | 0% | 0% | 0.043 / 0.050 | 0.042 | `O:pow_2(O:ts_max(O:cs_demean(O:sub(O:ts_max(O:day_mean(F)),C:scl))))` | `pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30))` |
| B087 | T11 | 12 | 0 / 12 | 10(5) | 11 | 0.53 | 8% | 0% | 0.044 / 0.050 | 0.042 | `O:pow_2(O:ts_max(O:day_mean(F)))` | `pow_1_5(ts_max(cs_demean(sub(pow_2(ts_max(day_mean(Ret), 30)), 2)), 30))` |
| B088 | T11 | 8 | 0 / 8 | 8(3) | 8 | 0.60 | 0% | 0% | 0.046 / 0.058 | 0.044 | `O:ts_max(O:cs_demean(O:sub(O:day_mean(F),C:pct)))` | `pow_2(ts_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 30))` |
| B089 | T12 | 41 | 3 / 38 | 4(3) | 36 | 0.28 | 51% | 2% | 0.011 / 0.046 | 0.034 | `O:day_first(F)` | `ts_quantile_q75(ts_quantile_q75(day_first(Volume), 50), 40)` |
| B090 | T12 | 30 | 30 / 0 | 25(9) | 16 | 0.54 | 100% | 0% | 0.022 / 0.054 | 0.043 | `O:in_sustain_stddev(O:is_gt(O:sub(O:in_boxcox(F),O:in_forward_valid_pa` | `sub(day_sum(in_sustain_stddev(is_gt(sub(in_boxcox(Volume), in_forward_valid_part(in_boxcox` |
| B091 | T12 | 22 | 22 / 0 | 6(3) | 22 | 0.31 | 77% | 0% | 0.010 / 0.044 | 0.031 | `O:is_gt(O:div(O:sub(O:day_sum(F),O:cross_delay(O:day_sum(F))),O:cross_` | `add(select_where(is_gt(cross_stddev(sub(div(day_first(Open), cross_delay(day_last(Close), ` |
| B092 | T12 | 12 | 0 / 12 | 0(0) | 7 | 0.70 | 33% | 0% | 0.004 / 0.016 | -0.010 | `O:ts_argmin(O:day_first(F))` | `ts_scale(ts_argmin(day_first(Vwap), 30), 30)` |
| B093 | T12 | 9 | 9 / 0 | 6(4) | 9 | 0.72 | 100% | 0% | 0.022 / 0.048 | 0.035 | `O:day_sum(O:is_gt(O:sub(O:in_boxcox(F),O:in_forward_valid_part(O:in_bo` | `abs_(sub(day_sum(is_gt(sub(in_boxcox(Volume), in_forward_valid_part(in_boxcox(Volume))), a` |
| B094 | T12 | 8 | 0 / 8 | 3(1) | 3 | 0.91 | 62% | 0% | 0.018 / 0.038 | 0.022 | `O:cross_sum(O:day_first(F))` | `ts_reg_tvalue(cs_mask_top_replace_mean(sqrt(cross_sum(day_first(Volume), 30))), day_quanti` |
| B095 | T13 | 40 | 40 / 0 | 5(3) | 40 | 0.40 | 50% | 0% | 0.019 / 0.052 | 0.041 | `O:create_valid_mask(O:sub(O:div(O:day_last(F),O:ts_delay(O:day_last(F)` | `sub(1, cs_rank(abs_(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)), create_va` |
| B096 | T13 | 32 | 0 / 32 | 6(4) | 23 | 0.32 | 75% | 0% | 0.015 / 0.049 | 0.036 | `O:day_last(F)` | `cross_hurst(day_last(Amt), 30)` |
| B097 | T13 | 19 | 19 / 0 | 0(0) | 18 | 0.65 | 0% | 0% | 0.006 / 0.017 | 0.003 | `O:cs_rank(O:div(O:sub(O:div(O:day_last(F),O:ts_delay(O:day_last(F))),C` | `ts_autocorr(cs_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), ts_del` |
| B098 | T13 | 13 | 0 / 13 | 0(0) | 12 | 0.57 | 92% | 0% | 0.017 / 0.024 | 0.015 | `O:ts_max(O:log(O:cross_regbeta(O:day_quantile_q25(F),O:day_last(F))))` | `ts_max(log(cross_regbeta(day_quantile_q25(Low), day_last(Amt), 10)), 20)` |
| B099 | T13 | 10 | 0 / 10 | 1(1) | 9 | 0.74 | 90% | 0% | 0.017 / 0.046 | 0.029 | `O:cs_demean(O:ts_quantile_q50(O:inv(O:day_last(F))))` | `cs_demean(ts_quantile_q50(cs_demean(ts_quantile_q50(inv(day_last(Amt)), 10)), 10))` |
| B100 | T14 | 32 | 2 / 30 | 8(5) | 27 | 0.27 | 59% | 3% | 0.015 / 0.048 | 0.038 | `O:day_sum(F)` | `pow_2(ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(ts_decay_linear(sigmoid(ts_dec` |
| B101 | T14 | 24 | 24 / 0 | 24(6) | 3 | 0.77 | 100% | 0% | 0.022 / 0.037 | 0.021 | `O:div(O:day_sum(O:in_topk_masked(F,F)),O:day_sum(F))` | `div(day_sum(in_topk_masked(Ret, Volume, 5)), day_sum(Volume))` |
| B102 | T14 | 18 | 6 / 12 | 4(2) | 14 | 0.49 | 61% | 0% | 0.020 / 0.037 | 0.019 | `O:cs_rank(O:day_sum(F))` | `ts_min(cs_rank(ts_decay_linear(sigmoid(cs_rank(day_sum(Volume))), 10)), 20)` |
| B103 | T14 | 18 | 0 / 18 | 6(3) | 18 | 0.40 | 100% | 0% | 0.019 / 0.049 | 0.036 | `O:inv(O:day_sum(F))` | `inv(day_sum(Volume))` |
| B104 | T14 | 12 | 12 / 0 | 10(4) | 3 | 0.77 | 100% | 0% | 0.034 / 0.051 | 0.038 | `O:div(O:day_last(O:in_topk_masked(F,F)),O:day_first(O:in_topk_masked(F` | `div(day_last(in_topk_masked(Volume, Close, 5)), day_first(in_topk_masked(Volume, Open, 5))` |
| B105 | T14 | 8 | 0 / 8 | 1(1) | 3 | 0.74 | 38% | 0% | 0.029 / 0.047 | 0.039 | `O:ts_stddev(O:day_sum(F))` | `ts_stddev(ts_stddev(day_sum(High), 10), 20)` |
| B106 | T15 | 24 | 24 / 0 | 20(5) | 3 | 0.67 | 50% | 0% | 0.030 / 0.040 | 0.029 | `O:energy_ratio_n(O:delete_open_close(F))` | `energy_ratio_n(delete_open_close(Volume), 0.8, True)` |
| B107 | T15 | 24 | 24 / 0 | 12(4) | 3 | 0.67 | 50% | 0% | 0.020 / 0.043 | 0.032 | `O:energy_ratio_band_n(O:delete_open_close(F))` | `energy_ratio_band_n(delete_open_close(Volume), 0.2, True, False)` |
| B108 | T15 | 24 | 24 / 0 | 20(6) | 3 | 0.67 | 50% | 0% | 0.024 / 0.036 | 0.026 | `O:energy_ratio_topm(O:delete_open_close(F))` | `energy_ratio_topm(delete_open_close(Volume), 5, False)` |
| B109 | T15 | 18 | 18 / 0 | 14(5) | 3 | 0.67 | 50% | 0% | 0.019 / 0.046 | 0.029 | `O:energy_ratio_topm_minus_q(O:delete_open_close(F))` | `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False)` |
| B110 | T15 | 12 | 12 / 0 | 8(4) | 8 | 0.74 | 100% | 0% | 0.035 / 0.051 | 0.036 | `O:div(O:div(O:day_sum(O:mul(O:is_gt(O:in_mean_full(O:in_stddev_rolling` | `div(div(day_sum(mul(is_gt(in_mean_full(in_stddev_rolling(in_stddev_rolling(delete_open_clo` |
| B111 | T16 | 59 | 0 / 59 | 0(0) | 50 | 0.32 | 20% | 0% | 0.008 / 0.027 | 0.016 | `O:day_argmax(F)` | `cross_stddev(ts_pearson(cross_min(day_argmax(Low), 10), 5), 5)` |
| B112 | T16 | 41 | 0 / 41 | 3(2) | 36 | 0.29 | 39% | 5% | 0.010 / 0.046 | 0.019 | `O:day_open(F)` | `cs_scale(ts_argmax(cross_delay(day_open(High), 30), 5))` |
| B113 | T17 | 60 | 0 / 60 | 3(2) | 51 | 0.26 | 42% | 2% | 0.013 / 0.056 | 0.041 | `O:day_autocorr_n1(F)` | `signedpower(cross_stddev(day_autocorr_n1(Volume), 3))` |
| B114 | T17 | 32 | 0 / 32 | 12(3) | 18 | 0.48 | 97% | 0% | 0.032 / 0.055 | 0.037 | `O:cross_quantile_q25(O:day_autocorr_n1(F))` | `cross_quantile_q25(day_autocorr_n1(Volume), 15)` |
| B115 | T17 | 8 | 0 / 8 | 2(1) | 6 | 0.69 | 0% | 0% | 0.012 / 0.037 | 0.027 | `O:inv(O:ts_std(O:pow_05(O:day_autocorr_n1(F))))` | `ts_min(ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10), 10)` |
| B116 | T18 | 31 | 0 / 31 | 6(2) | 21 | 0.53 | 87% | 6% | 0.031 / 0.049 | 0.027 | `O:cross_sum(O:log(F))` | `day_open(cross_sum(log(Amt), 3))` |
| B117 | T18 | 30 | 30 / 0 | 26(9) | 16 | 0.54 | 100% | 0% | 0.022 / 0.054 | 0.043 | `O:in_sustain_stddev(O:is_gt(O:sub(O:log(F),O:in_forward_valid_part(O:l` | `sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))),` |
| B118 | T18 | 25 | 0 / 25 | 3(3) | 22 | 0.33 | 76% | 4% | 0.030 / 0.052 | 0.027 | `O:log(F)` | `day_first(log(Amt))` |
| B119 | T18 | 9 | 9 / 0 | 6(4) | 9 | 0.71 | 100% | 0% | 0.022 / 0.048 | 0.035 | `O:day_sum(O:is_gt(O:sub(O:log(F),O:in_forward_valid_part(O:log(F))),O:` | `abs_(sub(day_sum(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_f` |
| B120 | T19 | 29 | 29 / 0 | 1(1) | 7 | 0.69 | 3% | 0% | 0.005 / 0.038 | -0.024 | `O:day_mean(O:select_where(O:eq(O:in_roll_labels(F),C:scl),O:create_lik` | `day_mean(select_where(eq(in_roll_labels(Close, 241), 0), create_like(in_slice(Close, 1, 1)` |
| B121 | T19 | 28 | 28 / 0 | 10(5) | 14 | 0.47 | 57% | 0% | 0.016 / 0.045 | 0.003 | `O:select_where(O:eq(O:in_roll_labels(F),C:scl),F,O:create_like(O:in_sl` | `day_mean(select_where(eq(in_roll_labels(Close, 241), 4), select_where(less_equal(Ret, day_` |
| B122 | T19 | 18 | 18 / 0 | 11(5) | 3 | 0.78 | 0% | 0% | 0.027 / 0.049 | 0.036 | `O:div(O:day_last(O:in_slice(F)),O:day_first(O:in_slice(F)))` | `div(day_last(in_slice(Close, 1, 120)), day_first(in_slice(Open, 1, 120)))` |
| B123 | T19 | 17 | 17 / 0 | 0(0) | 17 | 0.73 | 100% | 0% | nan / nan | nan | `O:logical_and(O:is_gt(O:mul(O:in_slice(F),O:div(O:sub(O:in_slice(F),O:` | `day_sum(logical_and(is_gt(mul(in_slice(Volume, 16, 225), div(sub(in_slice(Close, 16, 225),` |
| B124 | T20 | 59 | 3 / 56 | 3(2) | 42 | 0.29 | 25% | 0% | 0.009 / 0.033 | 0.027 | `O:day_kurt(F)` | `ts_kurt(day_kurt(Low), 40)` |
| B125 | T20 | 16 | 0 / 16 | 0(0) | 6 | 0.81 | 6% | 0% | 0.015 / 0.022 | 0.014 | `O:cross_sum(O:day_kurt(F))` | `cross_sum(day_kurt(Vwap), 3)` |
| B126 | T20 | 14 | 0 / 14 | 2(1) | 10 | 0.58 | 21% | 0% | 0.024 / 0.030 | 0.021 | `O:pow_2(O:day_kurt(F))` | `pow_2(day_kurt(Ret))` |
| B127 | T21 | 42 | 42 / 0 | 34(5) | 14 | 0.52 | 100% | 0% | 0.037 / 0.056 | 0.043 | `O:mul(O:replace_small_with_nan(O:is_gt(O:sub(O:in_slice(F),O:in_delay(` | `abs_(cs_demean(day_mean(mul(replace_small_with_nan(is_gt(sub(in_slice(Volume, 2, 237), in_` |
| B128 | T21 | 33 | 33 / 0 | 25(5) | 11 | 0.55 | 100% | 0% | 0.035 / 0.053 | 0.039 | `O:in_sustain_stddev(O:is_gt(O:sub(O:in_slice(F),O:in_delay(O:in_slice(` | `day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2` |
| B129 | T21 | 9 | 9 / 0 | 9(1) | 3 | 0.62 | 100% | 0% | 0.009 / 0.013 | -0.102 | `O:is_gt(O:sub(O:in_slice(F),O:in_delay(O:in_slice(F))),O:add(O:in_mean` | `day_sum(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in` |
| B130 | T22 | 58 | 6 / 52 | 2(2) | 44 | 0.38 | 52% | 2% | 0.013 / 0.042 | 0.019 | `O:day_corr(F,F)` | `ts_quantile_q50(inv(day_corr(High, Close)), 30)` |
| B131 | T22 | 14 | 0 / 14 | 2(1) | 11 | 0.83 | 29% | 0% | 0.020 / 0.032 | 0.027 | `O:ts_min(O:ts_regres(O:day_corr(F,F),O:day_durbin_watson(F)))` | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 241)` |
| B132 | T22 | 9 | 0 / 9 | 0(0) | 7 | 0.78 | 56% | 0% | 0.011 / 0.026 | 0.015 | `O:ts_std(O:day_corr(F,F))` | `ts_std(day_corr(Ret, Volume), 40)` |
| B133 | T23 | 34 | 0 / 34 | 7(4) | 31 | 0.25 | 24% | 21% | 0.018 / 0.035 | 0.028 | `O:cross_delta(F)` | `day_open(cross_delta(Vwap, 60))` |
| B134 | T23 | 30 | 0 / 30 | 6(4) | 20 | 0.47 | 10% | 100% | 0.017 / 0.032 | 0.023 | `O:pow_2(O:nt_cs_rank(O:cross_delta(F)))` | `day_mean(pow_2(pow_2(nt_cs_rank(cross_delta(Open, 241)))))` |
| B135 | T23 | 15 | 0 / 15 | 0(0) | 15 | 0.51 | 13% | 100% | 0.015 / 0.029 | 0.020 | `O:day_cov(O:pow_2(O:nt_cs_rank(O:cross_delta(F))),F)` | `day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low)` |
| B136 | T24 | 44 | 0 / 44 | 7(6) | 38 | 0.29 | 23% | 0% | 0.018 / 0.053 | 0.038 | `O:day_var(F)` | `day_var(Low)` |
| B137 | T24 | 19 | 0 / 19 | 6(3) | 17 | 0.56 | 42% | 0% | 0.026 / 0.053 | 0.030 | `O:add(O:div(O:day_var(F),O:day_max(F)),O:cross_max(O:day_cov(F,F)))` | `ts_quantile_q75(pow_1_5(cross_cov(day_max(High), add(div(day_var(Ret), day_max(High)), cro` |
| B138 | T24 | 15 | 0 / 15 | 8(4) | 10 | 0.51 | 13% | 0% | 0.036 / 0.049 | 0.030 | `O:ts_quantile_q75(O:pow_1_5(O:cross_cov(O:day_max(F),O:day_var(F))))` | `ts_quantile_q75(ts_quantile_q75(pow_1_5(cross_cov(day_max(High), day_var(Ret), 15)), 5), 5` |
| B139 | T25 | 29 | 1 / 28 | 1(1) | 29 | 0.38 | 10% | 3% | 0.028 / 0.040 | 0.024 | `O:day_min(F)` | `pow_2(pow_05(day_min(Ret)))` |
| B140 | T25 | 20 | 0 / 20 | 0(0) | 20 | 0.54 | 0% | 0% | 0.037 / 0.037 | -0.058 | `O:sigmoid(O:day_min(F))` | `log(sigmoid(sigmoid(day_min(Ret))))` |
| B141 | T25 | 17 | 0 / 17 | 0(0) | 16 | 0.50 | 0% | 0% | 0.037 / 0.037 | 0.009 | `O:pow_2(O:sigmoid(O:day_min(F)))` | `pow_2(sigmoid(day_min(Ret)))` |
| B142 | T25 | 11 | 0 / 11 | 0(0) | 10 | 0.63 | 0% | 0% | 0.037 / 0.037 | 0.010 | `O:sigmoid(O:sigmoid(O:sigmoid(O:day_min(F))))` | `sigmoid(sigmoid(sigmoid(sigmoid(day_min(Ret)))))` |
| B143 | T26 | 38 | 6 / 32 | 7(5) | 29 | 0.36 | 32% | 5% | 0.029 / 0.054 | 0.042 | `O:day_std(F)` | `ts_skew(cs_scale(cs_normalize(ts_autocorr_s1(day_std(High), 50))), 30)` |
| B144 | T26 | 15 | 0 / 15 | 1(1) | 12 | 0.45 | 0% | 0% | 0.029 / 0.032 | 0.023 | `O:neg(O:sigmoid(O:day_std(F)))` | `neg(neg(sigmoid(day_std(Low))))` |
| B145 | T26 | 9 | 0 / 9 | 0(0) | 5 | 0.83 | 100% | 0% | 0.003 / 0.008 | -0.011 | `O:ts_min(O:ts_reg_fvalue(O:day_std(F),O:day_cov(F,F)))` | `ts_min(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 5)` |
| B146 | T27 | 34 | 34 / 0 | 25(8) | 34 | 0.44 | 3% | 0% | 0.026 / 0.053 | 0.033 | `O:select_where(O:is_gt(F,O:create_like(F)),O:sub(F,O:in_mean_full(O:se` | `day_mean(abs_(add(select_where(is_gt(Ret, create_like(Ret, 0)), sub(Ret, in_mean_full(sele` |
| B147 | T27 | 12 | 12 / 0 | 12(6) | 11 | 0.61 | 0% | 0% | 0.035 / 0.056 | 0.037 | `O:day_std(O:select_where(O:is_lt(F,O:create_like(F)),F,O:create_like(F` | `day_std(select_where(is_lt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` |
| B148 | T27 | 8 | 8 / 0 | 8(6) | 7 | 0.78 | 0% | 0% | 0.044 / 0.056 | 0.045 | `O:day_std(O:select_where(O:is_gt(F,O:create_like(F)),F,O:create_like(F` | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` |
| B149 | T27 | 8 | 8 / 0 | 4(2) | 8 | 0.93 | 12% | 0% | 0.023 / 0.039 | 0.023 | `O:day_mean(O:is_lt(O:mul(O:select_where(O:is_gt(F,O:create_like(F)),O:` | `day_mean(is_lt(mul(select_where(is_gt(Ret, create_like(Ret, 0)), day_mean(is_gt(Ret, creat` |
| B150 | T28 | 29 | 0 / 29 | 0(0) | 21 | 0.45 | 14% | 100% | 0.007 / 0.027 | -0.090 | `O:pow_1_5(O:log(O:nt_ts_kurt(F)))` | `pow_05(day_close(pow_1_5(log(nt_ts_kurt(Vwap, 30)))))` |
| B151 | T28 | 18 | 0 / 18 | 0(0) | 14 | 0.43 | 22% | 100% | 0.016 / 0.027 | -0.060 | `O:day_max(O:nt_ts_kurt(F))` | `day_max(nt_ts_kurt(Vwap, 30))` |
| B152 | T28 | 11 | 0 / 11 | 0(0) | 7 | 0.60 | 9% | 100% | 0.015 / 0.022 | -0.094 | `O:day_max(O:pow_1_5(O:pow_2(O:nt_ts_kurt(F))))` | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` |
| B153 | T29 | 32 | 0 / 32 | 1(1) | 13 | 0.49 | 3% | 0% | 0.013 / 0.035 | 0.033 | `O:ts_max(O:cross_med(O:day_ar1_coefficient(F)))` | `sigmoid(ts_max(cross_med(day_ar1_coefficient(Close), 60), 30))` |
| B154 | T29 | 25 | 0 / 25 | 0(0) | 7 | 0.64 | 0% | 0% | 0.013 / 0.020 | 0.010 | `O:ts_max(O:ts_max(O:day_ar1_coefficient(F)))` | `ts_max(ts_max(day_ar1_coefficient(Close), 5), 40)` |
| B155 | T30 | 30 | 30 / 0 | 9(3) | 10 | 0.56 | 100% | 0% | 0.019 / 0.051 | 0.037 | `O:neg(O:sub(O:day_argmin(O:in_slice_to_end(O:in_local_mean(O:in_slice(` | `day_tide_speed(in_slice(Close, 2, 237), day_argmin(in_slice_from_start(in_local_mean(in_sl` |
| B156 | T30 | 12 | 12 / 0 | 9(3) | 4 | 0.82 | 100% | 0% | 0.020 / 0.040 | 0.014 | `O:div(O:div(O:sub(O:day_locate(O:in_slice(F),O:day_argmin(O:in_slice_t` | `cross_mean(div(div(sub(day_locate(in_slice(Close, 2, 237), day_argmin(in_slice_to_end(in_l` |
| B157 | T30 | 9 | 9 / 0 | 0(0) | 3 | 0.61 | 100% | 0% | 0.002 / 0.007 | -0.105 | `O:day_argmax(O:in_local_mean(O:in_slice(F)))` | `day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5))` |
| B158 | T31 | 18 | 0 / 18 | 8(5) | 10 | 0.45 | 78% | 11% | 0.031 / 0.048 | 0.037 | `O:cross_sum(F)` | `day_quantile_q75(cross_sum(Amt, 3))` |
| B159 | T31 | 11 | 0 / 11 | 0(0) | 9 | 0.65 | 0% | 100% | 0.004 / 0.018 | 0.014 | `O:nt_cs_rank(O:cross_delta(O:nt_cs_rank(O:cross_sum(F))))` | `day_median(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 241))))` |
| B160 | T31 | 11 | 0 / 11 | 0(0) | 7 | 0.61 | 0% | 100% | 0.029 / 0.032 | 0.010 | `O:nt_ts_corr(O:in_r2(O:signedpower(F),O:pow_1_5(F)),O:sigmoid(O:sqrt(F` | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(s` |
| B161 | T31 | 10 | 0 / 10 | 2(1) | 10 | 0.50 | 50% | 50% | 0.004 / 0.044 | 0.033 | `O:signedpower(F)` | `day_quantile_q75(cross_sum(cross_sum(signedpower(Amt), 3), 3))` |
| B162 | T32 | 25 | 0 / 25 | 2(2) | 19 | 0.38 | 16% | 100% | 0.003 / 0.033 | 0.023 | `O:nt_ts_autocorr_s1(F)` | `day_q_stat_std(nt_ts_autocorr_s1(Ret, 3))` |
| B163 | T32 | 20 | 0 / 20 | 1(1) | 17 | 0.47 | 0% | 100% | 0.018 / 0.027 | 0.019 | `O:pow_2(O:day_kurt(O:nt_ts_autocorr_s1(F)))` | `sqrt(neg(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))` |
| B164 | T33 | 21 | 0 / 21 | 2(2) | 19 | 0.41 | 5% | 100% | 0.015 / 0.027 | 0.024 | `O:pow_2_5(O:nt_ts_var(F))` | `ts_std(day_quantile(pow_2_5(nt_ts_var(Low, 3))), 50)` |
| B165 | T33 | 19 | 0 / 19 | 7(4) | 17 | 0.64 | 0% | 100% | 0.022 / 0.052 | 0.036 | `O:ts_sum(O:day_var(O:pow_2_5(O:nt_ts_var(F))))` | `ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10)` |
| B166 | T34 | 25 | 0 / 25 | 9(3) | 9 | 0.65 | 44% | 0% | 0.017 / 0.050 | 0.034 | `O:day_max(O:cross_corr(F,F))` | `day_max(cross_corr(Ret, Ret, 30))` |
| B167 | T34 | 14 | 0 / 14 | 2(2) | 11 | 0.43 | 71% | 57% | 0.014 / 0.045 | 0.036 | `O:cross_corr(F,F)` | `cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 5)` |
| B168 | T35 | 22 | 0 / 22 | 8(2) | 18 | 0.52 | 100% | 100% | 0.029 / 0.050 | 0.036 | `O:day_durbin_watson(O:nt_cs_quantile_q25(F))` | `sqrt(day_durbin_watson(nt_cs_quantile_q25(Amt)))` |
| B169 | T35 | 14 | 0 / 14 | 12(2) | 5 | 0.72 | 93% | 100% | 0.037 / 0.047 | 0.035 | `O:ts_stddev(O:day_sum(O:nt_cs_quantile_q25(F)))` | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 30)` |
| B170 | T36 | 15 | 0 / 15 | 2(2) | 15 | 0.50 | 20% | 27% | 0.014 / 0.054 | 0.026 | `O:pow_2(F)` | `cross_mean(day_sum(pow_2(Ret)), 3)` |
| B171 | T36 | 11 | 0 / 11 | 10(3) | 10 | 0.64 | 0% | 0% | 0.049 / 0.056 | 0.043 | `O:day_q_stat_std(O:pow_2(F))` | `day_q_stat_std(pow_2(Ret))` |
| B172 | T36 | 9 | 0 / 9 | 8(4) | 8 | 0.63 | 11% | 0% | 0.047 / 0.054 | 0.041 | `O:day_std(O:pow_2(F))` | `day_std(pow_2(Ret))` |
| B173 | T37 | 20 | 0 / 20 | 1(1) | 20 | 0.35 | 20% | 20% | 0.010 / 0.036 | 0.031 | `O:sigmoid(F)` | `day_sum(nt_cs_sum(signedpower(sigmoid(Close))))` |
| B174 | T37 | 14 | 0 / 14 | 3(1) | 13 | 0.54 | 43% | 7% | 0.008 / 0.025 | 0.018 | `O:cross_product(O:sigmoid(F))` | `day_product(cross_product(sigmoid(Amt), 10))` |
| B175 | T38 | 19 | 0 / 19 | 2(1) | 4 | 0.82 | 58% | 100% | 0.020 / 0.042 | 0.025 | `O:cross_min(O:day_max(O:nt_cs_regres(F,F)))` | `cross_min(day_max(nt_cs_regres(Amt, Ret)), 5)` |
| B176 | T38 | 15 | 0 / 15 | 0(0) | 13 | 0.44 | 80% | 100% | 0.015 / 0.042 | 0.024 | `O:nt_cs_regres(F,F)` | `cross_min(day_last(nt_cs_regres(Amt, Low)), 5)` |
| B177 | T39 | 24 | 0 / 24 | 5(1) | 19 | 0.42 | 96% | 0% | 0.050 / 0.061 | 0.045 | `O:ts_decay_linear(O:day_ar1_coefficient(F))` | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` |
| B178 | T39 | 8 | 0 / 8 | 0(0) | 8 | 0.64 | 100% | 0% | 0.058 / 0.061 | 0.038 | `O:cs_rank(O:ts_decay_linear(O:day_ar1_coefficient(F)))` | `pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 1)))` |
| B179 | T40 | 31 | 0 / 31 | 3(1) | 22 | 0.32 | 65% | 100% | 0.009 / 0.041 | 0.024 | `O:nt_ts_skew(F)` | `cross_quantile_q25(day_autocorr_n1(nt_ts_skew(Ret, 3)), 15)` |
| B180 | T41 | 30 | 30 / 0 | 26(5) | 20 | 0.44 | 100% | 0% | 0.048 / 0.054 | 0.038 | `O:div(O:in_slice(O:in_zscore_rolling(F)),O:in_sum(O:in_slice(O:in_zsco` | `day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscor` |
| B181 | T42 | 30 | 30 / 0 | 0(0) | 3 | 0.62 | 100% | 0% | 0.007 / 0.019 | -0.006 | `O:day_pdf_quantile_single(F,F)` | `day_pdf_quantile_single(Ret, Volume, 0.6, True)` |
| B182 | T43 | 20 | 0 / 20 | 0(0) | 14 | 0.53 | 25% | 0% | 0.014 / 0.017 | 0.005 | `O:cross_argmax(O:day_ar1_coefficient(F))` | `cross_argmax(day_ar1_coefficient(Ret), 30)` |
| B183 | T43 | 9 | 0 / 9 | 0(0) | 5 | 0.61 | 22% | 0% | 0.014 / 0.017 | 0.003 | `O:pow_05(O:abs_(O:cross_argmax(O:day_ar1_coefficient(F))))` | `pow_2(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 30))))` |
| B184 | T44 | 28 | 28 / 0 | 6(2) | 27 | 0.59 | 39% | 0% | 0.005 / 0.021 | -0.013 | `O:div(O:in_regres(F,O:in_mean_full(F)),O:add(O:in_stddev_full(O:in_reg` | `day_hurst(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_` |
| B185 | T45 | 24 | 24 / 0 | 14(3) | 3 | 0.62 | 100% | 0% | 0.006 / 0.017 | 0.000 | `O:day_pdf_tail_sum_m(F,F)` | `day_pdf_tail_sum_m(Ret, Volume, 5, False)` |
| B186 | T46 | 23 | 0 / 23 | 3(1) | 18 | 0.40 | 83% | 0% | 0.052 / 0.061 | 0.044 | `O:sigmoid(O:day_ar1_coefficient(F))` | `ts_decay_linear(sigmoid(day_ar1_coefficient(Volume)), 5)` |
| B187 | T47 | 20 | 0 / 20 | 0(0) | 18 | 0.55 | 80% | 100% | 0.039 / 0.050 | 0.027 | `O:nt_ts_min(F)` | `day_close(nt_ts_med(nt_ts_min(Amt, 3), 5))` |
| B188 | T48 | 20 | 0 / 20 | 12(2) | 15 | 0.41 | 50% | 100% | 0.032 / 0.048 | 0.038 | `O:nt_ts_cov(F,F)` | `ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20)` |
| B189 | T49 | 19 | 0 / 19 | 1(1) | 17 | 0.46 | 11% | 26% | 0.013 / 0.058 | 0.009 | `O:inv(F)` | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` |
| B190 | T50 | 19 | 0 / 19 | 9(5) | 16 | 0.40 | 37% | 5% | 0.028 / 0.056 | 0.041 | `O:pow_2_5(F)` | `day_close(pow_2_5(Ret))` |
| B191 | T51 | 18 | 0 / 18 | 5(1) | 16 | 0.45 | 17% | 100% | 0.018 / 0.059 | 0.027 | `O:nt_ts_max(F)` | `day_autocorr_n1(nt_ts_max(Vwap, 3))` |
| B192 | T52 | 18 | 0 / 18 | 2(1) | 14 | 0.44 | 0% | 100% | 0.008 / 0.051 | 0.029 | `O:nt_ts_mean(F)` | `ts_stddev(sqrt(day_durbin_watson(nt_cs_mask_top_replace_mean_neg(nt_ts_mean(Close, 15)))),` |
| B193 | T53 | 14 | 0 / 14 | 0(0) | 7 | 0.71 | 14% | 0% | 0.011 / 0.030 | -0.014 | `O:day_q_stat_std(O:in_max_rolling(F))` | `day_q_stat_std(in_max_rolling(Vwap, 60))` |
| B194 | T54 | 13 | 13 / 0 | 11(1) | 13 | 0.50 | 100% | 0% | 0.035 / 0.036 | 0.024 | `O:div(O:add(O:ts_mean(O:abs_(O:cs_demean(O:day_sum(O:sub(O:in_sorted_c` | `div(add(ts_mean(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forward(in_slice(div(Close, in` |
| B195 | T55 | 11 | 0 / 11 | 0(0) | 4 | 0.83 | 82% | 0% | 0.030 / 0.037 | 0.008 | `O:day_durbin_watson(O:sliding_bottom_mean_masked_p5(F,F))` | `day_durbin_watson(sliding_bottom_mean_masked_p5(Close, Volume, 5))` |
| B196 | T56 | 10 | 0 / 10 | 1(1) | 7 | 0.76 | 40% | 90% | 0.020 / 0.034 | -0.006 | `O:day_mean(O:nt_cs_normalize(O:in_cov(F,F)))` | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))))` |
| B197 | T57 | 9 | 9 / 0 | 0(0) | 9 | 0.69 | 100% | 0% | 0.004 / 0.009 | -0.008 | `O:day_kurt(O:div(F,O:in_sum(F)))` | `div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume))))` |
| B198 | T58 | 9 | 0 / 9 | 1(1) | 8 | 0.67 | 0% | 67% | 0.020 / 0.026 | 0.023 | `O:signedpower(O:cross_med(F))` | `day_autocorr_n1(nt_ts_min(signedpower(cross_med(nt_ts_min(signedpower(cross_med(Ret, 60)),` |
| B199 | R | 24 | 24 / 0 | 18(5) | 4 | 0.46 | 100% | 0% | 0.029 / 0.049 | -0.043 | `O:abs_(O:in_delay(F))` | `day_corr(abs_(in_delay(Ret, 1)), Volume)` |
| B200 | R | 16 | 6 / 10 | 6(2) | 10 | 0.36 | 75% | 19% | 0.034 / 0.054 | 0.029 | `O:abs_(F)` | `day_corr(abs_(Ret), in_delay(Amt, 1))` |
| B201 | R | 30 | 30 / 0 | 18(5) | 5 | 0.35 | 100% | 0% | 0.021 / 0.046 | -0.054 | `O:abs_(O:in_delay(O:in_slice(F)))` | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(log(in_zscore_rolling(Volume,` |
| B202 | R | 18 | 18 / 0 | 13(6) | 5 | 0.37 | 67% | 0% | 0.027 / 0.052 | 0.043 | `O:abs_(O:in_slice(F))` | `day_corr(abs_(in_slice(Ret, 11, 230)), in_delay(in_slice(Volume, 11, 230), 1))` |
| B203 | R | 13 | 12 / 1 | 2(1) | 3 | 0.49 | 100% | 0% | 0.010 / 0.017 | 0.005 | `O:in_zscore_rolling(F)` | `day_corr(abs_(Ret), in_delay(in_zscore_rolling(Volume, 21), 1))` |
| B204 | R | 8 | 8 / 0 | 1(1) | 8 | 0.27 | 75% | 0% | 0.018 / 0.028 | -0.021 | `O:ts_delta(O:day_last(F))` | `mul(ts_rank(div(day_sum(Volume), ts_mean(day_sum(Volume), 20)), 20), ts_rank(mul(-1, ts_de` |
| B205 | R | 15 | 15 / 0 | 0(0) | 15 | 0.27 | 100% | 0% | 0.006 / 0.025 | -0.003 | `O:div(O:add(O:day_max(F),O:day_min(F)),C:scl)` | `mul(is_lt(cs_rank(ts_corr(ts_sum(add(mul(day_first(Open), 0.178404), mul(day_min(Low), sub` |
| B206 | R | 13 | 12 / 1 | 0(0) | 13 | 0.37 | 0% | 8% | 0.007 / 0.022 | 0.004 | `O:in_max_rolling(F)` | `day_mean(in_corr(in_max_rolling(High, 50), in_min_rolling(Low, 50), 50))` |
| B207 | R | 14 | 12 / 2 | 2(2) | 8 | 0.38 | 100% | 0% | 0.013 / 0.036 | 0.016 | `O:in_shift(F)` | `day_corr(Ret, in_shift(Volume, 1))` |
| B208 | R | 10 | 5 / 5 | 1(1) | 9 | 0.42 | 50% | 30% | 0.017 / 0.045 | -0.012 | `O:mul(F,F)` | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` |
| B209 | R | 8 | 8 / 0 | 4(2) | 8 | 0.56 | 0% | 0% | 0.036 / 0.046 | 0.037 | `O:div(O:in_slice(F),O:signed_pow(O:div(O:in_stddev_rolling_multi(O:in_` | `day_cov(select_where(is_gt(signed_pow(div(in_stddev_rolling_multi([in_slice(Open, 2, 237),` |
| B210 | R | 18 | 17 / 1 | 7(4) | 18 | 0.33 | 100% | 0% | 0.026 / 0.051 | 0.027 | `O:is_gt(F,O:add(O:cross_mean(F),O:cross_stddev(F)))` | `div(cross_sum(day_sum(mul(mul(in_no_neighbor(is_gt(Volume, sub(cross_mean(Volume, 20), cro` |
| B211 | R | 26 | 26 / 0 | 25(5) | 26 | 0.32 | 35% | 0% | 0.045 / 0.056 | 0.047 | `O:div(O:sub(O:day_max(F),O:day_min(F)),O:day_open(F))` | `div(sub(day_max(High), day_min(Low)), day_open(Open))` |
| B212 | R | 14 | 0 / 14 | 0(0) | 11 | 0.45 | 29% | 100% | 0.018 / 0.045 | 0.016 | `O:nt_cs_rank(F)` | `day_mean(pow_2(nt_cs_rank(Ret)))` |
| B213 | R | 8 | 0 / 8 | 0(0) | 8 | 0.50 | 25% | 12% | 0.003 / 0.018 | -0.006 | `O:cross_argmax(F)` | `day_mean(sigmoid(pow_3(cross_argmax(Open, 3))))` |
| B214 | R | 12 | 0 / 12 | 9(4) | 10 | 0.35 | 92% | 0% | 0.023 / 0.036 | 0.032 | `O:log(O:add(O:day_last(F),O:day_std(F)))` | `ts_mean(log(add(day_last(Volume), day_std(Vwap))), 30)` |
| B215 | R | 8 | 0 / 8 | 1(1) | 5 | 0.57 | 12% | 0% | 0.022 / 0.029 | 0.025 | `O:pow_1_5(O:cross_cov(O:day_mean(F),O:day_quantile(F)))` | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15)), 1)` |
| B216 | R | 10 | 0 / 10 | 2(1) | 9 | 0.31 | 70% | 0% | 0.015 / 0.023 | 0.019 | `O:log(O:add(O:day_open(F),O:day_std(F)))` | `ts_argmin(mul(log(add(day_open(Ret), day_std(Vwap))), day_max(Low)), 50)` |
| B217 | R | 11 | 0 / 11 | 1(1) | 10 | 0.38 | 27% | 91% | 0.020 / 0.046 | 0.037 | `O:nt_ts_stddev(F)` | `day_q_stat_std(nt_ts_stddev(Ret, 3))` |
| B218 | R | 18 | 0 / 18 | 2(2) | 15 | 0.30 | 44% | 17% | 0.028 / 0.052 | 0.016 | `O:pow_1_5(F)` | `pow_2(day_max(nt_ts_min(signedpower(pow_1_5(Ret)), 30)))` |
| B219 | R | 12 | 0 / 12 | 10(4) | 10 | 0.33 | 92% | 0% | 0.039 / 0.054 | 0.042 | `O:ts_std(O:day_close(F))` | `cross_delay(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(Op` |
| B220 | R | 10 | 0 / 10 | 1(1) | 10 | 0.48 | 30% | 10% | 0.010 / 0.036 | 0.005 | `O:neg(F)` | `day_last(neg(Ret))` |
| B221 | R | 12 | 0 / 12 | 7(4) | 11 | 0.40 | 42% | 100% | 0.032 / 0.049 | 0.040 | `O:nt_ts_delta(F)` | `day_max(in_mean_full(nt_ts_delta(High, 30)))` |
| B222 | R | 11 | 0 / 11 | 0(0) | 8 | 0.43 | 36% | 100% | 0.011 / 0.049 | 0.035 | `O:nt_ts_med(F)` | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 3))))` |
| B223 | R | 60 | 12 / 48 | 5(4) | 53 | 0.02 | 52% | 5% | 0.013 / 0.058 | 0.041 | `—` | `add(day_min(Ret), day_cov(Ret, Low))` |
| B224 | R | 60 | 23 / 37 | 25(16) | 47 | 0.01 | 58% | 3% | 0.022 / 0.062 | 0.046 | `—` | `cross_max(cross_max(cross_max(ts_std(day_durbin_watson(Open), 40), 5), 30), 5)` |
| B225 | R | 60 | 6 / 54 | 14(6) | 48 | 0.02 | 25% | 15% | 0.017 / 0.050 | 0.039 | `—` | `cross_quantile_q25(pow_3(day_durbin_watson(Ret)), 60)` |
| B226 | R | 60 | 28 / 32 | 18(11) | 46 | 0.01 | 52% | 3% | 0.014 / 0.051 | 0.039 | `—` | `cross_sum(cross_sum(neg(cross_cov(day_cov(Low, Ret), mul(day_autocorr_n1(High), day_std(Lo` |
| B227 | R | 60 | 23 / 37 | 20(7) | 46 | 0.02 | 55% | 35% | 0.020 / 0.048 | 0.037 | `—` | `day_corr(abs_(in_slice(Ret, 11, 230)), in_delay(in_slice(log(Volume), 11, 230), 1))` |
| B228 | R | 60 | 26 / 34 | 14(12) | 49 | 0.02 | 20% | 28% | 0.016 / 0.050 | 0.033 | `—` | `day_max(in_longest_run_of_label(in_roll_labels(Close, 241), 4))` |
| B229 | R | 60 | 28 / 32 | 13(7) | 44 | 0.02 | 30% | 35% | 0.012 / 0.043 | 0.031 | `—` | `day_mean(select_where(eq(in_shift(in_roll_labels(Close, 120), 1), 4), in_shift(Ret, 1), cr` |
| B230 | R | 60 | 44 / 16 | 22(12) | 49 | 0.02 | 45% | 12% | 0.015 / 0.047 | 0.021 | `—` | `div(day_sum(in_label_change_flags(in_roll_labels(Close, 241))), add(day_sum(select_where(g` |
| B231 | R | 60 | 21 / 39 | 7(7) | 58 | 0.02 | 62% | 10% | 0.014 / 0.052 | 0.032 | `—` | `mul(-1, ts_corr(cs_rank(ts_delta(log(day_sum(Volume)), 2)), cs_rank(div(sub(day_last(Close` |
| B232 | R | 60 | 4 / 56 | 7(6) | 54 | 0.02 | 55% | 25% | 0.021 / 0.058 | 0.047 | `—` | `pow_2(day_max(pow_1_5(log(pow_1_5(nt_ts_kurt(Vwap, 30))))))` |
| B233 | R | 60 | 9 / 51 | 18(14) | 51 | 0.01 | 30% | 3% | 0.017 / 0.054 | 0.047 | `—` | `signedpower(cross_quantile_q75(cross_corr(day_skew(Vwap), mul(day_skew(Vwap), day_skew(Vwa` |
| B234 | R | 60 | 9 / 51 | 12(8) | 51 | 0.02 | 53% | 8% | 0.015 / 0.053 | 0.043 | `—` | `signedpower(signedpower(cross_quantile_q75(cross_corr(day_skew(Vwap), mul(cross_product(cr` |
| B235 | R | 60 | 3 / 57 | 9(7) | 48 | 0.02 | 33% | 23% | 0.011 / 0.058 | 0.040 | `—` | `ts_corr(day_corr(Low, Ret), day_corr(Low, Low), 20)` |
| B236 | R | 60 | 9 / 51 | 31(14) | 52 | 0.02 | 60% | 20% | 0.027 / 0.049 | 0.042 | `—` | `ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20)` |
| B237 | R | 60 | 7 / 53 | 15(10) | 53 | 0.02 | 52% | 12% | 0.016 / 0.054 | 0.042 | `—` | `ts_mean(mul(log(add(ts_hurst(div(day_last(Volume), div(day_last(Volume), day_max(Low))), 4` |
| B238 | R | 60 | 3 / 57 | 12(8) | 51 | 0.01 | 33% | 7% | 0.014 / 0.052 | 0.041 | `—` | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), d` |
| B239 | R | 60 | 7 / 53 | 26(11) | 53 | 0.02 | 37% | 20% | 0.020 / 0.049 | 0.036 | `—` | `ts_std(ts_cov(day_cov(Close, Ret), day_close(High), 50), 40)` |
| B240 | R | 37 | 7 / 30 | 17(13) | 27 | 0.03 | 43% | 22% | 0.022 / 0.049 | 0.044 | `—` | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5)` |
