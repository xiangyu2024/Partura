# 相关度表:种子 806,C 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.19 | 0.04 | 0.03 | 0.18 | 0.09 | `day_cov(Vwap, Ret)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.35 | 0.07 | 0.08 | 0.34 | 0.20 | `div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret)))` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.07 | 0.09 | 0.36 | 0.18 | `div(day_cov(Vwap, Ret), mul(day_std(Vwap), day_std(Ret)))` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.52 | 0.13 | 0.12 | 0.50 | 0.28 | `cross_mean(div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret))), 5)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.73 | 0.18 | 0.11 | 0.69 | 0.33 | `cross_mean(div(day_cov(Vwap, Ret), mul(day_std(Vwap), day_std(Ret))), 20)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.63 | 0.15 | 0.15 | 0.60 | 0.29 | `cross_decay_linear(div(day_cov(Vwap, Ret), mul(day_std(Vwap), day_std(Ret))), 10)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.02 | 0.03 | 0.02 | 0.01 | `cross_zscore(div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret))), 20)` |
| slot a seed 7 | 废品 | 0.00 | `—` | 0.00 | 0.01 | 0.01 | 0.04 | 0.01 | 0.00 | `ts_rank(div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret))), 20)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.32 | 0.06 | 0.02 | 0.29 | 0.21 | `cs_bucket_zscore(div(day_cov(Vwap, Ret), day_mean(Vwap)), day_var(Ret))` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.48 | 0.07 | 0.04 | 0.44 | 0.31 | `ts_mean(cs_bucket_zscore(div(day_cov(Vwap, Ret), day_mean(Vwap)), day_var(Ret)), 5)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.05 | 0.04 | 0.41 | 0.27 | `cs_bucket_zscore(cross_mean(div(day_cov(Vwap, Ret), day_mean(Vwap)), 5), cross_mean(day_var(Ret), 5))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.08 | 0.06 | 0.26 | 0.11 | `cs_bucket_rank(div(day_cov(Vwap, Ret), day_var(Ret)), day_mean(Vwap))` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.53 | 0.00 | 0.11 | 0.49 | 0.28 | `cs_bucket_rank(cross_mean(div(day_cov(Vwap, Ret), mul(day_std(Vwap), day_std(Ret))), 5), cross_mean(day_std(Ret), 20))` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.01 | 0.10 | 0.02 | 0.01 | `mul(sub(div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret))), 0.5), sign(day_sum(Ret)))` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.06 | 0.28 | 0.02 | 0.01 | `cross_mean(mul(sub(div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret))), 0.5), sign(day_sum(Ret))), 5)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.03 | 0.09 | 0.04 | 0.06 | `day_skew(Ret)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.09 | 0.18 | 0.07 | 0.11 | `cross_mean(day_skew(Ret), 5)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.19 | 0.16 | 0.01 | 0.29 | `cross_max(day_skew(Ret), 20)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.02 | 0.19 | 0.07 | 0.11 | `ts_mean(cs_bucket_rank(cross_mean(day_skew(Ret), 5), cross_mean(day_std(Ret), 20)), 5)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.04 | 0.14 | 0.04 | 0.04 | `div(day_sum(mul(is_gt0(Ret), mul(Ret, Ret))), day_sum(mul(Ret, Ret)))` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.29 | 0.49 | 0.24 | 0.14 | `cross_mean(div(day_sum(mul(is_gt0(Ret), mul(Ret, Ret))), day_sum(mul(Ret, Ret))), 20)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.04 | 0.01 | 0.07 | 0.12 | `day_es_ratio_hi(Ret)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.03 | `sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret))` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.03 | 0.07 | 0.02 | 0.04 | `div(add(day_max(Ret), day_min(Ret)), day_std(Ret))` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.18 | 0.25 | 0.12 | 0.14 | `cross_mean(div(add(day_max(Ret), day_min(Ret)), day_std(Ret)), 20)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.02 | 0.14 | 0.03 | 0.03 | `div(day_topw_mean(Ret, Volume), day_std(Ret))` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.09 | 0.32 | 0.10 | 0.08 | `cross_mean(div(day_topw_mean(Ret, Volume), day_std(Ret)), 5)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.01 | 0.14 | 0.01 | 0.06 | `day_signed_ratio(Ret, Volume)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.00 | 0.03 | 0.06 | 0.00 | 0.09 | `sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret))` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.01 | 0.20 | 0.04 | 0.30 | `cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 20)` |
