# C01 证据摘要:写第 3 轮指引之前(只含 B 臂自己的运行)

运行 15 次;存下的候选 1187 个(每次运行最多存 80 个);score ≥ 1 的 568 个;互不相关且不在已知族里的 heads 20 个。score = 纯多头十分位书扣 15bp 后 train 与 valid 夏普中较差的那个。

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
| R2 | 201 | C2a_when_the_return_arrives | 153 | 14% | 43 | 0 | 0.0 | 1120 | {"proposed": 367, "accepted": 217, "outside": 81, "banned": 69} |
| R2 | 202 | C2a_when_the_return_arrives | 121 | 25% | 31 | 0 | 0.0 | 764 | {"proposed": 396, "banned": 85, "accepted": 230, "outside": 61, "equivalent": 20} |
| R2 | 203 | C2a_when_the_return_arrives | 157 | 19% | 53 | 2 | 1.3 | 841 | {"proposed": 387, "accepted": 233, "outside": 53, "banned": 88, "equivalent": 13} |
| R2 | 204 | C2a_when_the_return_arrives | 146 | 27% | 63 | 0 | 0.0 | 1964 | {"proposed": 372, "accepted": 221, "banned": 87, "outside": 40, "equivalent": 24} |
| R2 | 205 | C2b_turnover_on_the_up_minutes | 184 | 5% | 72 | 0 | 0.0 | 3474 | {"proposed": 360, "banned": 67, "accepted": 241, "outside": 52} |
| R2 | 206 | C2b_turnover_on_the_up_minutes | 156 | 14% | 12 | 0 | 0.0 | 9824 | {"proposed": 364, "outside": 67, "accepted": 229, "banned": 68} |
| R2 | 208 | C2b_turnover_on_the_up_minutes | 131 | 19% | 21 | 0 | 0.0 | 1393 | {"proposed": 347, "banned": 81, "outside": 36, "accepted": 229, "equivalent": 1} |

## 失败的运行(按 PLAN §6 修订 2:重跑后仍失败的 B 运行,该种子的发现记为 0)

| 轮 | 任务 | 退出码 | 原因(日志摘录) |
|---|---|---|---|
| R2 | c01r2s207B | 143 | 被停止:磁盘守护(数据盘不足 60 GB)或单任务时限 | [partura exit 135 2026-10-27_17:32:49] [partura exit 143 2026-10-27_18:46:48] |

磁盘守护日志:

    [guard] 2026-10-27_18:46:45 free 57G < 60G: spill tmp/alphacube_kkr_z4om (196G), killing: 167733 
    [guard] 2026-10-27_18:47:17 removed tmp/alphacube_kkr_z4om; free now 252G

运行时间:见上表「秒」一列。注意:分钟级跨股票截面算子(nt_cs_* / nt_ts_*)与日内折叠混用的表达式,引擎要把整块 (股票, 日, 分钟) 中间量落盘,每个节点约 6.8 GB,并且很慢;R2 有一次运行因此写满数据盘。

## heads(互不相关、|ρ| 对已知族与 pool 都 < 0.5)

| 轮 | 种子 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 104 | +2.72 | +2.82 | +2.72 | 20 | -1 | 0.026 | +0.16 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)), day_std(Close)))))` |
| R1 | 104 | +2.63 | +2.63 | +3.66 | 20 | -1 | 0.033 | +0.36 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Vwap))))` |
| R1 | 104 | +2.53 | +2.53 | +3.10 | 20 | -1 | 0.031 | -0.12 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(sub(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.51 | +2.51 | +3.15 | 20 | -1 | 0.040 | +0.26 | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| R1 | 104 | +2.43 | +2.43 | +3.51 | 20 | -1 | 0.037 | +0.28 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R2 | 203 | +2.32 | +2.32 | +3.36 | 5 | -1 | 0.063 | +0.38 | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, Close)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R1 | 104 | +2.30 | +2.30 | +2.87 | 20 | -1 | 0.041 | +0.43 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Amt), day_std(Close)), day_std(Amt))))` |
| R1 | 103 | +2.25 | +2.68 | +2.25 | 20 | -1 | 0.042 | +0.23 | `cs_first_low20(day_open(Amt), day_pos_ratio(Ret))` |
| R1 | 104 | +2.20 | +2.20 | +3.70 | 20 | -1 | 0.037 | +0.12 | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_distinct_ratio(Vwap), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret))))` |
| R1 | 104 | +1.90 | +2.08 | +1.90 | 20 | -1 | 0.032 | +0.07 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(day_std(Vwap))))` |
| R2 | 203 | +1.87 | +1.87 | +4.02 | 20 | -1 | 0.048 | +0.07 | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, mul(Amt, Amt))))), day_sum(Ret)), day_distinct_ratio(mul(Amt, Amt)))` |
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
| R2 | 203 | +2.43 | +2.43 | +2.72 | 20 | 0.027 | +0.40 |  | `cs_first_low20(sub(mul(2, day_last(mul(Amt, Amt))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.43 | +2.43 | +3.38 | 20 | 0.039 | +0.67 |  | `day_first(in_max(mul(in_skew_full(mul(in_max(Amt), Amt)), Amt)))` |
| R2 | 203 | +2.43 | +2.43 | +2.72 | 20 | 0.027 | +0.40 |  | `cs_first_low20(sub(mul(2, day_last(mul(Amt, Amt))), day_gini(High)), day_distinct_ratio(Close))` |
| R1 | 104 | +2.43 | +2.43 | +3.51 | 20 | 0.037 | +0.28 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Vwap), day_std(Close)), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R1 | 104 | +2.42 | +2.42 | +2.81 | 20 | 0.019 | +0.33 |  | `cs_mask_top_replace_mean_neg(pow_2_5(div(day_distinct_ratio(Vwap), div(div(day_distinct_ratio(Vwap), day_std(Close)), day_std(Close)))))` |
| R2 | 201 | +2.42 | +2.42 | +3.84 | 20 | 0.030 | +0.76 |  | `div(mul(day_std(Amt), day_at_min_ratio(Vwap)), mul(day_hurst(pow_05(Volume)), day_centroid(Ret)))` |
| R2 | 201 | +2.34 | +2.34 | +3.83 | 20 | 0.030 | +0.76 |  | `div(mul(day_std(Amt), day_at_min_ratio(Vwap)), mul(day_hurst(pow_05(Open)), day_centroid(Ret)))` |
| R1 | 104 | +2.33 | +2.33 | +3.01 | 20 | 0.048 | +0.20 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Vwap)))))))` |
| R2 | 203 | +2.32 | +2.32 | +3.36 | 5 | 0.063 | +0.38 | 是 | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, Close)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R1 | 104 | +2.30 | +2.30 | +3.36 | 20 | 0.063 | +0.23 |  | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close))))))` |
| R1 | 104 | +2.30 | +2.30 | +2.87 | 20 | 0.041 | +0.43 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(day_distinct_ratio(Amt), day_std(Close)), day_std(Amt))))` |
| R2 | 203 | +2.28 | +2.28 | +3.18 | 5 | 0.065 | +0.42 |  | `cs_first_low20(sub(mul(2, day_last(in_stddev_full(mul(mul(Amt, Amt), Open)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R1 | 108 | +2.28 | +2.28 | +3.67 | 20 | 0.031 | +0.78 |  | `day_wstd(Amt, Amt)` |
| R1 | 104 | +2.26 | +2.26 | +3.17 | 20 | 0.045 | +0.20 |  | `cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close)))))))` |
| R1 | 103 | +2.25 | +2.68 | +2.25 | 20 | 0.042 | +0.23 | 是 | `cs_first_low20(day_open(Amt), day_pos_ratio(Ret))` |
| R2 | 203 | +2.25 | +2.25 | +3.42 | 5 | 0.055 | +0.40 |  | `cs_first_low20(sub(mul(2, day_last(in_stddev_full(mul(Amt, Open)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.25 | +2.25 | +3.45 | 20 | 0.037 | +0.68 |  | `day_first(in_max(mul(in_skew_full(mul(Amt, Amt)), Amt)))` |
| R1 | 101 | +2.23 | +2.23 | +3.76 | 20 | 0.027 | +0.83 |  | `sub(cross_scale(day_std(Amt), 15), day_wmean(Amt, Volume))` |
| R1 | 103 | +2.23 | +2.23 | +2.39 | 20 | 0.032 | +0.35 |  | `cs_first_low20(day_open(Amt), day_distinct_ratio(Ret))` |
| R1 | 108 | +2.22 | +2.22 | +3.76 | 20 | 0.027 | +0.83 |  | `day_wmean(Amt, Amt)` |
| R1 | 103 | +2.22 | +2.22 | +2.22 | 20 | 0.033 | +0.36 |  | `cs_first_low20(day_open(Amt), day_distinct_ratio(Close))` |
| R2 | 203 | +2.22 | +2.22 | +2.90 | 20 | 0.026 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, Amt)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.22 | +2.22 | +2.90 | 20 | 0.026 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(mul(Amt, Amt), Amt)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.22 | +2.22 | +2.90 | 20 | 0.026 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, in_max(Amt))))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.22 | +2.22 | +2.90 | 20 | 0.026 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(in_max(mul(Amt, Amt)), in_max(Amt))))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.22 | +2.22 | +2.90 | 20 | 0.026 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(Amt, in_max(mul(Amt, Amt)))))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.22 | +2.22 | +2.90 | 20 | 0.026 | +0.41 |  | `cs_first_low20(sub(mul(sub(mul(2, day_last(in_max(mul(Amt, Amt)))), day_sum(Ret)), day_last(in_max(mul(Amt, Amt)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R1 | 104 | +2.21 | +2.21 | +2.31 | 20 | 0.050 | +0.14 |  | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), cs_mask_top_replace_mean_neg(inv(div(day_distinct_ratio(Vwap), day_std(Close))))))))` |
| R2 | 203 | +2.21 | +2.21 | +3.19 | 5 | 0.070 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(mul(Amt, Amt), High)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.20 | +2.20 | +3.19 | 5 | 0.070 | +0.41 |  | `cs_first_low20(sub(mul(2, day_last(in_max(mul(in_max(mul(Close, Amt)), in_max(Amt))))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R1 | 104 | +2.20 | +2.20 | +3.70 | 20 | 0.037 | +0.12 | 是 | `cs_mask_top_replace_mean_neg(inv(div(div(div(div(div(day_distinct_ratio(Vwap), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret)), day_std(Ret))))` |
| R2 | 203 | +2.20 | +2.20 | +2.84 | 20 | 0.024 | +0.42 |  | `cs_first_low20(sub(mul(2, day_last(in_stddev_full(mul(Amt, Amt)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R2 | 203 | +2.16 | +2.16 | +2.98 | 20 | 0.025 | +0.41 |  | `cs_first_low20(sub(mul(sub(mul(2, day_last(in_max(mul(Amt, in_max(mul(Amt, Amt)))))), day_sum(Ret)), day_last(in_max(mul(Amt, Close)))), day_sum(Ret)), day_distinct_ratio(Close))` |
| R1 | 106 | +2.16 | +2.16 | +3.57 | 20 | 0.026 | +0.81 |  | `mul(add(add(day_gini(Volume), add(day_gini(Volume), day_var(Amt))), add(add(day_gini(Volume), add(day_gini(Volume), day_var(Amt))), day_var(Amt))), day_skew(Amt))` |
| R2 | 203 | +2.15 | +2.15 | +3.63 | 20 | 0.026 | +0.81 |  | `day_last(in_max(mul(Amt, Amt)))` |
| R2 | 203 | +2.15 | +2.15 | +3.63 | 20 | 0.026 | +0.81 |  | `day_first(in_max(mul(Amt, Amt)))` |
| R2 | 203 | +2.15 | +2.15 | +3.63 | 20 | 0.026 | +0.81 |  | `day_last(in_max(in_max(mul(Amt, Amt))))` |
| R2 | 203 | +2.15 | +2.15 | +3.63 | 20 | 0.026 | +0.81 |  | `sub(mul(2, day_last(in_max(mul(Amt, Amt)))), day_sum(Ret))` |
| R2 | 203 | +2.15 | +2.15 | +3.63 | 20 | 0.026 | +0.81 |  | `sub(mul(2, day_last(in_max(mul(Amt, Amt)))), day_sum(in_max(Amt)))` |
| R2 | 205 | +2.14 | +2.14 | +3.37 | 20 | 0.028 | +0.79 |  | `day_wstd(nt_ts_decay_linear(signedpower(Amt), 3), Volume)` |
| R2 | 201 | +2.13 | +2.13 | +3.80 | 20 | 0.024 | +0.85 |  | `div(day_std(Amt), mul(day_hurst(pow_05(Ret)), day_centroid(Ret)))` |
| R2 | 203 | +2.13 | +2.13 | +3.71 | 20 | 0.023 | +0.80 |  | `day_last(in_max(in_max(mul(mul(Amt, Amt), High))))` |
| R2 | 203 | +2.12 | +2.12 | +3.35 | 5 | 0.064 | +0.81 |  | `day_last(in_max(mul(in_max(mul(Amt, Amt)), Amt)))` |
| R2 | 203 | +2.12 | +2.12 | +3.35 | 5 | 0.064 | +0.81 |  | `mul(2, day_last(in_max(mul(mul(Amt, Amt), Amt))))` |
| R2 | 203 | +2.12 | +2.12 | +3.35 | 5 | 0.064 | +0.81 |  | `day_last(in_max(mul(in_max(mul(Amt, Amt)), in_max(Amt))))` |
| R2 | 203 | +2.12 | +2.12 | +3.35 | 5 | 0.064 | +0.81 |  | `day_last(in_max(mul(Amt, mul(Amt, Amt))))` |
| R2 | 203 | +2.12 | +2.12 | +3.35 | 5 | 0.064 | +0.81 |  | `day_last(in_max(in_max(in_max(mul(Amt, in_max(mul(Amt, Amt)))))))` |

## 没过线里分数最高的 30 个(对照用)

| 轮 | 种子 | score | train | valid | ρ已知 | 表达式 |
|---|---|---|---|---|---|---|
| R2 | 206 | +1.00 | +1.00 | +2.11 | +0.63 | `sub(1, ts_spearman(day_skew(nt_cs_regres(nt_cs_mask_top_replace_mean(High), nt_cs_regres(nt_cs_mask_top_replace_mean(High), Amt))), 50))` |
| R2 | 205 | +0.99 | +1.52 | +0.99 | +0.57 | `sub(day_wstd(nt_ts_delay(Volume, 5), div(Amt, div(Amt, High))), pow_05(cross_ema(day_q_stat_std(Low), 5)))` |
| R2 | 202 | +0.99 | +0.99 | +3.24 | +0.79 | `day_last(pow_1_5(sqrt(sqrt(sqrt(pow_1_5(Amt))))))` |
| R1 | 105 | +0.98 | +0.98 | +2.33 | +0.62 | `log(day_cov(Vwap, Volume))` |
| R1 | 108 | +0.98 | +0.98 | +2.53 | +0.72 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 30)), ts_delay(mul(day_flat_run_max(Amt), cs_scale(day_close(Low))), 50))` |
| R2 | 204 | +0.98 | +0.98 | +3.34 | +0.92 | `div(ts_min(abs_(day_std(Amt)), 5), sub(day_last(Ret), day_centroid(Open)))` |
| R2 | 206 | +0.97 | +0.97 | +2.12 | +0.61 | `sub(1, ts_spearman(day_skew(nt_cs_regres(nt_cs_quantile_q25(High), Amt)), 50))` |
| R2 | 201 | +0.97 | +1.38 | +0.97 | +0.29 | `day_first(div(Low, nt_cs_bucket_rank(Open, Volume)))` |
| R1 | 108 | +0.96 | +0.96 | +2.49 | +0.71 | `cs_bucket_rank(div(ts_quantile_q25(day_var(Amt), 50), ts_argmin(day_q_stat_std(Close), 30)), ts_delay(mul(day_flat_run_max(Amt), day_std(High)), 50))` |
| R1 | 106 | +0.96 | +1.80 | +0.96 | +0.57 | `add(add(day_var(Volume), add(day_var(Volume), day_skew(Amt))), add(day_var(Volume), day_skew(Amt)))` |
| R2 | 206 | +0.96 | +0.96 | +2.35 | +0.57 | `sub(1, ts_spearman(day_skew(nt_cs_regres(nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean(High)), Amt)), 50))` |
| R2 | 202 | +0.96 | +1.71 | +0.96 | +0.24 | `day_last(pow_1_5(sqrt(div(Ret, Volume))))` |
| R1 | 107 | +0.96 | +2.51 | +0.96 | +0.32 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_std(Volume)))` |
| R2 | 202 | +0.95 | +0.95 | +3.20 | +0.79 | `day_last(sqrt(sqrt(Amt)))` |
| R1 | 103 | +0.95 | +0.95 | +3.38 | +0.88 | `day_quantile(Amt)` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `day_median(Amt)` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `add(add(day_median(Amt), add(day_median(Amt), day_skew(Amt))), add(day_median(Amt), day_skew(Amt)))` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `add(day_median(Amt), day_skew(Amt))` |
| R1 | 106 | +0.95 | +0.95 | +3.38 | +0.88 | `add(add(day_median(Amt), day_skew(Amt)), day_skew(Amt))` |
| R2 | 203 | +0.95 | +0.95 | +2.60 | +0.64 | `cs_first_low20(sub(mul(2, day_last(in_max(Amt))), day_sum(Ret)), cs_bucket_demean(day_sum(Ret), day_q_stat_std(Volume)))` |
| R1 | 105 | +0.95 | +0.95 | +1.27 | +0.24 | `day_open(nt_cs_last_high40(High, Close))` |
| R2 | 205 | +0.95 | +1.88 | +0.95 | +0.59 | `day_wstd(nt_ts_decay_linear(signedpower(Volume), 15), div(Low, pow_2_5(day_distinct_ratio(Volume))))` |
| R2 | 204 | +0.95 | +1.83 | +0.95 | +0.68 | `day_first(abs_(nt_ts_quantile_q50(mul(Volume, cross_fangzheng(Volume, 30)), 10)))` |
| R2 | 204 | +0.95 | +1.83 | +0.95 | +0.68 | `day_first(mul(cross_fangzheng(Volume, 30), Volume))` |
| R1 | 106 | +0.95 | +0.95 | +3.35 | +0.88 | `add(add(day_median(Volume), add(day_median(Amt), day_skew(Amt))), add(day_median(Amt), day_skew(Amt)))` |
| R1 | 103 | +0.95 | +0.95 | +3.18 | +0.94 | `add(day_sum(Amt), ts_sum(add(day_sum(Amt), ts_sum(day_at_min_ratio(Ret), 50)), 50))` |
| R1 | 101 | +0.95 | +0.95 | +1.33 | +0.68 | `sqrt(add(add(day_sum(Volume), day_var(Low)), day_var(Low)))` |
| R1 | 101 | +0.95 | +0.95 | +1.33 | +0.68 | `sqrt(day_sum(Volume))` |
| R2 | 206 | +0.94 | +0.94 | +2.10 | +0.58 | `sub(1, ts_spearman(day_skew(nt_cs_regres(nt_cs_regres(nt_cs_mask_top_replace_mean(High), Amt), Amt)), 50))` |
| R2 | 206 | +0.94 | +0.94 | +2.10 | +0.58 | `sub(1, ts_spearman(day_skew(nt_cs_regres(nt_cs_mask_top_replace_mean(High), Amt)), 50))` |

## 算子在通过者里的富集(出现 ≥ 3 次的;lift = 通过者中占比 ÷ 全部存下的候选中占比)

| 算子 | 全部 | 通过 | lift |
|---|---|---|---|
| cross_scale | 20 | 20 | 2.09 |
| nt_ts_quantile_q25 | 21 | 21 | 2.09 |
| nt_ts_decay_linear | 38 | 37 | 2.03 |
| cross_quantile_q75 | 29 | 27 | 1.95 |
| nt_cs_normalize | 17 | 15 | 1.84 |
| day_topw_mean | 64 | 54 | 1.76 |
| in_stddev_full | 5 | 4 | 1.67 |
| nt_cs_last_high40 | 10 | 8 | 1.67 |
| nt_ts_delay | 33 | 26 | 1.65 |
| day_pos_ratio | 23 | 18 | 1.64 |
| mul | 247 | 192 | 1.62 |
| day_var | 65 | 49 | 1.58 |
| in_max | 57 | 41 | 1.50 |
| signedpower | 63 | 45 | 1.49 |
| cs_demean | 7 | 5 | 1.49 |
| day_std | 228 | 162 | 1.48 |
| cs_bucket_rank | 47 | 33 | 1.47 |
| pow_2_5 | 43 | 30 | 1.46 |
| day_wmean | 23 | 16 | 1.45 |
| pow_1_5 | 92 | 63 | 1.43 |
| day_sum | 110 | 75 | 1.42 |
| ts_scale | 3 | 2 | 1.39 |
| day_first | 118 | 78 | 1.38 |
| day_at_min_ratio | 65 | 42 | 1.35 |
| ts_delay | 50 | 32 | 1.34 |
| … | | | |
| ts_autocorr_s1 | 4 | 0 | 0.00 |
| cs_last_high10 | 5 | 0 | 0.00 |
| cross_corr | 3 | 0 | 0.00 |
| nt_cs_first_low20 | 4 | 0 | 0.00 |
| ts_quantile_q75 | 5 | 0 | 0.00 |
| cross_regres | 4 | 0 | 0.00 |
| cross_semistd_neg | 5 | 0 | 0.00 |
| cross_semistd_pos | 5 | 0 | 0.00 |
| sigmoid | 5 | 0 | 0.00 |
| cross_hurst | 3 | 0 | 0.00 |

## 叶子字段在通过者里的富集(出现 ≥ 3 次的;lift = 通过者中占比 ÷ 全部存下的候选中占比)

| 叶子字段 | 全部 | 通过 | lift |
|---|---|---|---|
| Amt | 633 | 464 | 1.53 |
| Volume | 320 | 180 | 1.18 |
| Vwap | 239 | 107 | 0.94 |
| Ret | 211 | 91 | 0.90 |
| Low | 167 | 72 | 0.90 |
| High | 204 | 81 | 0.83 |
| Close | 289 | 112 | 0.81 |
| Open | 171 | 64 | 0.78 |

注意:存下的候选只是每次运行 archive 里按适应度排前 80 的,不是全部提议;门槛废品不在里面。
