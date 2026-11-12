# 相关度表:种子 2068,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.17 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.37 | 0.18 | 0.12 | 0.01 | 0.18 | 0.08 | `day_median(Ret)` |
| slot a seed 1 | 过 | 0.46 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.14 | 0.34 | 0.41 | 0.70 | 0.36 | 0.13 | `ts_mean(sub(day_mean(Ret), day_median(Ret)), 20)` |
| slot a seed 2 | 废品 | 0.37 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.46 | 0.40 | 0.25 | 0.01 | 0.37 | 0.24 | `ts_rank(day_median(Ret), 40)` |
| slot a seed 3 | 废品 | 0.44 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.40 | 0.43 | 0.28 | 0.05 | 0.41 | 0.14 | `ts_mean(day_median(Ret), 30)` |
| slot a seed 4 | 过 | 0.43 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.13 | 0.15 | 0.44 | 0.59 | 0.20 | 0.06 | `ts_mean(sub(day_median(Ret), day_wmean(Ret, Amt)), 20)` |
| slot a seed 5 | 废品 | 0.41 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.39 | 0.41 | 0.27 | 0.04 | 0.39 | 0.15 | `ts_mean(div(day_median(Ret), day_std(Ret)), 20)` |
| slot a seed 6 | 废品 | 0.04 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.30 | 0.06 | 0.05 | 0.12 | 0.05 | 0.02 | `sub(ts_mean(day_median(Ret), 10), ts_mean(day_median(Ret), 60))` |
| slot a seed 7 | 过 | 0.45 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.13 | 0.28 | 0.33 | 0.65 | 0.30 | 0.13 | `ts_decay_linear(sub(day_median(Ret), day_mean(Ret)), 20)` |
| slot a seed 8 | 废品 | 0.42 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.40 | 0.44 | 0.27 | 0.03 | 0.41 | 0.20 | `ts_corr(day_median(Ret), day_signed_ratio(Ret, Amt), 30)` |
| slot a seed 9 | 废品 | 0.52 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.46 | 0.49 | 0.33 | 0.03 | 0.47 | 0.17 | `ts_stddev(day_median(Ret), 40)` |
| slot a seed 10 | 废品 | 0.47 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.23 | 0.12 | 0.22 | 0.23 | 0.09 | 0.13 | `cs_bucket_demean(ts_mean(day_median(Ret), 20), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| slot a seed 11 | 过 | 0.45 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.47 | 0.29 | 0.19 | 0.16 | 0.28 | 0.04 | `ts_mean(sub(day_median(Ret), day_median(in_slice(Ret, 1, 30))), 20)` |
| slot a seed 12 | 废品 | 0.42 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.39 | 0.41 | 0.28 | 0.04 | 0.39 | 0.14 | `div(ts_mean(day_median(Ret), 20), ts_mean(day_pos_ratio(Ret), 20))` |
| slot b seed 1 | 过 | 0.57 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.60 | 0.52 | 0.18 | 0.12 | 0.46 | 0.18 | `ts_mean(sub(day_signed_ratio(Ret, Amt), sub(mul(2, day_pos_ratio(Ret)), 1)), 20)` |
| slot b seed 2 | 过 | 0.39 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.12 | 0.11 | 0.41 | 0.55 | 0.16 | 0.09 | `ts_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20)` |
| slot b seed 3 | 过 | 0.19 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.15 | 0.09 | 0.26 | 0.39 | 0.11 | 0.19 | `ts_mean(day_signed_ratio(Ret, Amt), 40)` |
| slot b seed 4 | 过 | 0.11 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.10 | 0.10 | 0.12 | 0.02 | 0.12 | 0.11 | `ts_corr(day_signed_ratio(Ret, Amt), day_centroid(Amt), 40)` |
| slot b seed 5 | 过 | 0.18 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.18 | 0.00 | 0.15 | 0.60 | 0.01 | 0.13 | `ts_mean(mul(day_signed_ratio(Ret, Amt), day_centroid(Amt)), 20)` |
| slot b seed 6 | 过 | 0.54 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.24 | 0.33 | 0.48 | 0.45 | 0.35 | 0.05 | `ts_mean(day_topw_mean(Ret, Volume), 30)` |
| slot b seed 7 | 过 | 0.11 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_op` | 0.10 | 0.11 | 0.10 | 0.35 | 0.11 | 0.01 | `sub(ts_mean(day_signed_ratio(Ret, Amt), 10), ts_mean(day_signed_ratio(Ret, Amt), 60))` |
| slot b seed 8 | 废品 | 0.12 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), d` | 0.07 | 0.01 | 0.03 | 0.11 | 0.01 | 0.02 | `ts_rank(sub(day_wmean(Ret, Amt), day_median(Ret)), 40)` |
| slot b seed 9 | 过 | 0.18 | `day_var(cross_quantile_q50(in_regbeta(in_zscore_rolling(Open` | 0.31 | 0.05 | 0.16 | 0.04 | 0.05 | 0.13 | `ts_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Amt)), 20)` |
| slot b seed 10 | 过 | 0.45 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), d` | 0.20 | 0.20 | 0.32 | 0.58 | 0.21 | 0.05 | `ts_decay_linear(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 20)` |
| slot b seed 11 | 算不出:KeyError: 'x' | | | | | | | | | `ts_mean(day_signed_ratio(in_slice(Ret, 181, 240), Amt), 20)` |
| slot b seed 12 | 过 | 0.02 | `day_sum(abs_(in_slice(Ret, 1, 30)))` | 0.13 | 0.16 | 0.18 | 0.10 | 0.08 | 0.20 | `ts_corr(day_signed_ratio(Ret, Amt), day_pos_ratio(Ret), 30)` |
