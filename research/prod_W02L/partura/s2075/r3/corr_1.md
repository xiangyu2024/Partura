# 相关度表:种子 2075,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.08 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.18 | 0.11 | 0.01 | 0.03 | 0.10 | 0.05 | `day_last(in_top_quantile_flag_q10(Ret))` |
| slot a seed 1 | 过 | 0.29 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.22 | 0.45 | 0.07 | 0.07 | 0.40 | 0.26 | `cross_ema(day_last(in_top_quantile_flag_q10(Ret)), 60)` |
| slot a seed 2 | 废品 | 0.27 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.21 | 0.42 | 0.06 | 0.07 | 0.38 | 0.24 | `ts_mean(day_last(in_top_quantile_flag_q10(Ret)), 120)` |
| slot a seed 3 | 过 | 0.09 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.08 | 0.03 | 0.08 | 0.02 | 0.05 | 0.07 | `ts_corr(day_last(in_top_quantile_flag_q10(Ret)), day_mean(Ret), 60)` |
| slot a seed 4 | 废品 | 0.08 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.08 | 0.11 | 0.04 | 0.04 | 0.10 | 0.04 | `sub(ts_mean(day_last(in_top_quantile_flag_q10(Ret)), 60), ts_mean(day_last(in_top_quantile_flag_q10(Ret)), 240))` |
| slot a seed 5 | 过 | 0.24 | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_l` | 0.27 | 0.18 | 0.04 | 0.08 | 0.16 | 0.14 | `mul(ts_mean(day_last(in_top_quantile_flag_q10(Ret)), 60), cs_rank(ListAge))` |
| slot a seed 6 | 过 | 0.34 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.21 | 0.43 | 0.13 | 0.06 | 0.40 | 0.38 | `mul(cross_ema(day_last(in_top_quantile_flag_q10(Ret)), 40), LimitWidth)` |
| slot a seed 7 | 过 | 0.06 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.03 | 0.05 | 0.01 | 0.01 | 0.05 | 0.09 | `ts_corr(day_last(in_top_quantile_flag_q10(Ret)), day_sum(Amt), 120)` |
| slot a seed 8 | 过 | 0.44 | `cross_regres(day_argmax(Open), day_quantile_q75(Open), 60)` | 0.42 | 0.01 | 0.17 | 0.43 | 0.03 | 0.09 | `cross_regres(day_last(in_top_quantile_flag_q10(Ret)), day_std(Ret), 120)` |
| slot a seed 9 | 过 | 0.61 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.35 | 0.57 | 0.15 | 0.01 | 0.57 | 0.47 | `ts_sum(mul(day_last(in_top_quantile_flag_q10(Ret)), day_close(Amt)), 60)` |
| slot a seed 10 | 过 | 0.49 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.28 | 0.30 | 0.21 | 0.01 | 0.34 | 0.17 | `div(ts_mean(day_last(in_top_quantile_flag_q10(Ret)), 60), cross_ema(day_at_max_ratio(High), 60))` |
| slot a seed 11 | 废品 | 0.28 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.22 | 0.42 | 0.04 | 0.08 | 0.38 | 0.23 | `ts_decay_linear(day_last(in_top_quantile_flag_q10(Ret)), 100)` |
| slot a seed 12 | 过 | 0.08 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.04 | 0.09 | 0.03 | 0.02 | 0.08 | 0.09 | `cross_zscore(ts_sum(day_last(in_top_quantile_flag_q10(Ret)), 90), 120)` |
| slot b seed 1 | 过 | 0.35 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_m` | 0.16 | 0.19 | 0.32 | 0.17 | 0.22 | 0.07 | `cross_ema(sub(day_at_max_ratio(High), day_at_min_ratio(Low)), 20)` |
| slot b seed 2 | 废品 | 0.36 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_m` | 0.16 | 0.20 | 0.32 | 0.12 | 0.23 | 0.06 | `ts_mean(sub(day_at_max_ratio(High), day_at_min_ratio(Low)), 60)` |
| slot b seed 3 | 过 | 0.36 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_m` | 0.16 | 0.19 | 0.31 | 0.13 | 0.23 | 0.08 | `cross_ema(mul(sub(day_at_max_ratio(High), day_at_min_ratio(Low)), LimitWidth), 30)` |
| slot b seed 4 | 废品 | 0.44 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.51 | 0.07 | 0.18 | 0.15 | 0.01 | 0.00 | `ts_sum(day_at_max_ratio(Close), 40)` |
| slot b seed 5 | 废品 | 0.34 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_m` | 0.19 | 0.19 | 0.32 | 0.18 | 0.23 | 0.04 | `sub(ts_mean(day_at_max_ratio(High), 40), ts_mean(day_at_min_ratio(Low), 40))` |
| slot b seed 6 | 过 | 0.28 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.16 | 0.16 | 0.18 | 0.06 | 0.19 | 0.05 | `ts_corr(day_at_max_ratio(High), day_mean(Ret), 60)` |
| slot b seed 7 | 过 | 0.46 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.42 | 0.03 | 0.27 | 0.12 | 0.10 | 0.01 | `cross_ema(div(day_at_max_ratio(High), add(day_at_min_ratio(Low), 0.005)), 30)` |
| slot b seed 8 | 过 | 0.47 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.43 | 0.04 | 0.24 | 0.09 | 0.11 | 0.03 | `ts_std(sub(day_at_max_ratio(High), day_at_min_ratio(Low)), 60)` |
| slot b seed 9 | 过 | 0.14 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_m` | 0.20 | 0.10 | 0.28 | 0.07 | 0.06 | 0.25 | `cross_ema(mul(day_at_max_ratio(Close), cs_rank(BoardCode)), 40)` |
| slot b seed 10 | 过 | 0.72 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(sign` | 0.29 | 0.83 | 0.49 | 0.11 | 0.87 | 0.45 | `ts_mean(mul(day_at_max_ratio(Vwap), day_sum(Amt)), 30)` |
| slot b seed 11 | 过 | 0.37 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_m` | 0.17 | 0.20 | 0.31 | 0.12 | 0.23 | 0.07 | `cross_ema(sub(day_at_max_ratio(Open), day_at_min_ratio(Open)), 30)` |
| slot b seed 12 | 过 | 0.19 | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, ` | 0.24 | 0.05 | 0.04 | 0.10 | 0.02 | 0.02 | `cross_regres(day_at_max_ratio(High), day_at_min_ratio(Low), 60)` |
| R 1 variant 1 | 过 | 0.57 | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)` | 0.53 | 0.28 | 0.01 | 0.01 | 0.27 | 0.14 | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 241)` |
| R 1 variant 2 | 过 | 0.62 | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)` | 0.59 | 0.29 | 0.01 | 0.02 | 0.28 | 0.14 | `cross_ema(div(day_skew(Ret), day_kurt(Ret)), 120)` |
| R 1 variant 3 | 过 | 0.54 | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)` | 0.49 | 0.28 | 0.02 | 0.01 | 0.26 | 0.14 | `cross_ema(div(day_skew(Ret), day_kurt(Ret)), 240)` |
| R 1 variant 4 | 过 | 0.68 | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)` | 0.68 | 0.28 | 0.02 | 0.02 | 0.28 | 0.14 | `cross_mean(div(day_skew(Ret), add(day_kurt(Ret), day_std(Ret))), 120)` |
