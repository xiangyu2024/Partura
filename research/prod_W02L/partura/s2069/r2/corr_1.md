# 相关度表:种子 2069,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.13 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.10 | 0.14 | 0.15 | 0.28 | 0.17 | 0.15 | `cross_mean(day_skew(Ret), 20)` |
| slot a seed 1 | 过 | 0.14 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.09 | 0.24 | 0.14 | 0.28 | 0.26 | 0.00 | `cs_bucket_rank(cross_mean(day_skew(Ret), 20), LogFloatCap)` |
| slot a seed 2 | 过 | 0.12 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.10 | 0.14 | 0.13 | 0.28 | 0.17 | 0.09 | `cs_bucket_rank(cross_mean(day_skew(Ret), 20), ListAge)` |
| slot a seed 3 | 过 | 0.14 | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min` | 0.10 | 0.03 | 0.09 | 0.27 | 0.00 | 0.25 | `cs_bucket_rank(cross_mean(day_skew(Ret), 20), cross_mean(day_std(Amt), 30))` |
| slot a seed 4 | 过 | 0.14 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.09 | 0.24 | 0.14 | 0.28 | 0.26 | 0.00 | `cs_bucket_zscore(cross_mean(day_skew(Ret), 20), LogFloatCap)` |
| slot a seed 5 | 过 | 0.17 | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), i` | 0.13 | 0.70 | 0.23 | 0.05 | 0.69 | 0.56 | `cs_first_low40(cross_mean(day_skew(Ret), 20), cross_mean(day_std(Amt), 20))` |
| slot a seed 6 | 过 | 0.14 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.13 | 0.07 | 0.13 | 0.33 | 0.10 | 0.05 | `sub(cross_mean(day_skew(Ret), 20), cross_mean(day_skew(Ret), 120))` |
| slot a seed 7 | 过 | 0.13 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.11 | 0.01 | 0.08 | 0.33 | 0.03 | 0.02 | `cross_zscore(cross_mean(day_skew(Ret), 20), 60)` |
| slot a seed 8 | 过 | 0.12 | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), i` | 0.25 | 0.17 | 0.11 | 0.24 | 0.18 | 0.02 | `div(cross_mean(day_skew(Ret), 20), cross_stddev(day_skew(Ret), 20))` |
| slot a seed 9 | 过 | 0.17 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.12 | 0.06 | 0.11 | 0.41 | 0.09 | 0.15 | `sub(cross_mean(day_skew(Ret), 20), cross_mean(day_skew(Low), 20))` |
| slot a seed 10 | 过 | 0.09 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.03 | 0.01 | 0.09 | 0.26 | 0.01 | 0.14 | `mul(cs_rank(cross_mean(day_skew(Ret), 20)), cs_rank(neg(cross_mean(day_corr(Ret, Volume), 20))))` |
| slot a seed 11 | 过 | 0.14 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.09 | 0.24 | 0.14 | 0.28 | 0.26 | 0.00 | `cs_bucket_rank(sub(cross_mean(day_skew(Ret), 20), cross_mean(day_wmean(Ret, Amt), 20)), LogFloatCap)` |
| slot a seed 12 | 过 | 0.13 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.10 | 0.14 | 0.15 | 0.28 | 0.17 | 0.15 | `cs_last_high10(cross_mean(day_skew(Ret), 20), ListAge)` |
| slot b seed 1 | 过 | 0.16 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.04 | 0.36 | 0.42 | 0.24 | 0.40 | 0.04 | `cross_mean(day_centroid(Amt), 10)` |
| slot b seed 2 | 过 | 0.12 | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min` | 0.05 | 0.03 | 0.35 | 0.19 | 0.01 | 0.29 | `cs_bucket_rank(cross_mean(day_centroid(Amt), 20), cross_mean(day_std(Amt), 30))` |
| slot b seed 3 | 过 | 0.06 | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), i` | 0.05 | 0.08 | 0.11 | 0.18 | 0.09 | 0.00 | `cross_zscore(cross_mean(day_signed_ratio(Ret, Amt), 5), 40)` |
| slot b seed 4 | 过 | 0.20 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.23 | 0.09 | 0.17 | 0.60 | 0.06 | 0.00 | `cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 20), LogFloatCap)` |
| slot b seed 5 | 过 | 0.30 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.22 | 0.24 | 0.41 | 0.64 | 0.26 | 0.05 | `cross_mean(day_topw_mean(Ret, Volume), 20)` |
| slot b seed 6 | 过 | 0.25 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.22 | 0.01 | 0.19 | 0.51 | 0.00 | 0.06 | `cs_bucket_rank(cross_mean(day_topw_mean(Ret, Volume), 10), cross_mean(day_std(Amt), 30))` |
| slot b seed 7 | 过 | 0.37 | `cross_mean(day_mean(in_corr(in_max_rolling(High, 50), in_min` | 0.22 | 0.51 | 0.06 | 0.11 | 0.44 | 0.01 | `cs_bucket_rank(cross_mean(day_gini(Amt), 20), LogFloatCap)` |
| slot b seed 8 | 过 | 0.09 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.10 | 0.15 | 0.23 | 0.20 | 0.16 | 0.03 | `sub(cross_mean(day_gini(Amt), 5), cross_mean(day_gini(Amt), 60))` |
| slot b seed 9 | 过 | 0.23 | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), i` | 0.20 | 0.29 | 0.26 | 0.25 | 0.32 | 0.10 | `mul(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_signed_ratio(Ret, Amt), 20)))` |
| slot b seed 10 | 过 | 0.16 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.15 | 0.01 | 0.12 | 0.30 | 0.03 | 0.01 | `cs_bucket_rank(sub(cross_mean(day_centroid(Volume), 10), cross_mean(day_centroid(Volume), 60)), ListAge)` |
| slot b seed 11 | 过 | 0.24 | `mul(pairwise_max(cs_rank(ts_decay_linear(ts_delta(div(day_su` | 0.12 | 0.12 | 0.42 | 0.60 | 0.17 | 0.07 | `cs_rank(cross_mean(day_wmean(Ret, Amt), 20))` |
| slot b seed 12 | 过 | 0.23 | `cross_stddev(day_mean(in_regbeta(in_max_rolling(High, 50), i` | 0.14 | 0.72 | 0.27 | 0.16 | 0.72 | 0.37 | `cs_first_low40(cross_mean(day_signed_ratio(Ret, Amt), 10), cross_mean(day_std(Amt), 20))` |
