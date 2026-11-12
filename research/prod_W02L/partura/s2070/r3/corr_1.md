# 相关度表:种子 2070,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.44 | `day_quantile_q75(mul(High, Ret))` | 0.35 | 0.73 | 0.18 | 0.15 | 0.72 | 0.55 | `day_zero_ratio(Volume)` |
| slot a seed 1 | 废品 | 0.53 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.46 | 0.81 | 0.03 | 0.05 | 0.78 | 0.69 | `ts_mean(day_zero_ratio(Volume), 60)` |
| slot a seed 2 | 过 | 0.15 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.08 | 0.05 | 0.23 | 0.29 | 0.07 | 0.03 | `sub(ts_mean(day_zero_ratio(Volume), 5), ts_mean(day_zero_ratio(Volume), 60))` |
| slot a seed 3 | 过 | 0.06 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.06 | 0.04 | 0.03 | 0.04 | 0.04 | `ts_regres(LogFloatCap, day_zero_ratio(Volume), 60)` |
| slot a seed 4 | 过 | 0.08 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.12 | 0.03 | 0.17 | 0.11 | 0.02 | `ts_regres(ListAge, day_zero_ratio(Volume), 60)` |
| slot a seed 5 | 过 | 0.06 | `day_quantile_q75(mul(High, Ret))` | 0.04 | 0.03 | 0.02 | 0.11 | 0.05 | 0.03 | `ts_corr(day_zero_ratio(Volume), day_sum(Ret), 40)` |
| slot a seed 6 | 过 | 0.08 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.07 | 0.06 | 0.11 | 0.17 | 0.04 | 0.07 | `ts_regres(day_std(Ret), day_zero_ratio(Volume), 40)` |
| slot a seed 7 | 过 | 0.54 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.23 | 0.21 | 0.91 | 0.22 | 0.28 | 0.15 | `ts_regalpha(day_zero_ratio(Volume), day_std(Ret), 20)` |
| slot a seed 8 | 过 | 0.48 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.48 | 0.78 | 0.00 | 0.05 | 0.74 | 0.70 | `ts_std(day_zero_ratio(Volume), 40)` |
| slot a seed 9 | 废品 | 0.48 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.47 | 0.81 | 0.07 | 0.03 | 0.77 | 0.68 | `ts_max(day_zero_ratio(Volume), 20)` |
| slot a seed 10 | 过 | 0.15 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.02 | 0.21 | 0.29 | 0.04 | 0.05 | `div(day_zero_ratio(Volume), ts_mean(day_zero_ratio(Volume), 60))` |
| slot a seed 11 | 过 | 0.38 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.23 | 0.68 | 0.15 | 0.01 | 0.68 | 0.58 | `ts_corr(day_zero_ratio(Volume), day_sum(Amt), 30)` |
| slot a seed 12 | 过 | 0.06 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.08 | 0.06 | 0.07 | 0.08 | 0.04 | 0.06 | `ts_regres(day_sum(Amt), day_zero_ratio(Volume), 30)` |
| slot a seed 13 | 过 | 0.25 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.06 | 0.33 | 0.21 | 0.01 | 0.33 | 0.09 | `ts_skew(day_zero_ratio(Volume), 60)` |
| slot a seed 14 | 废品 | 0.37 | `day_quantile_q75(mul(High, Ret))` | 0.34 | 0.69 | 0.12 | 0.14 | 0.69 | 0.60 | `mul(day_zero_ratio(Volume), LimitWidth)` |
| slot a seed 15 | 废品 | 0.12 | `day_quantile_q75(mul(High, Ret))` | 0.08 | 0.01 | 0.00 | 0.14 | 0.01 | 0.03 | `ts_delta(day_zero_ratio(Volume), 10)` |
| slot a seed 16 | 过 | 0.11 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.06 | 0.17 | 0.03 | 0.10 | 0.17 | 0.20 | `ts_corr(day_zero_ratio(Volume), ts_delay(day_sum(Ret), 1), 40)` |
| slot b seed 1 | 过 | 0.21 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.11 | 0.25 | 0.13 | 0.19 | 0.25 | 0.04 | `ts_mean(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 20)` |
| slot b seed 2 | 过 | 0.23 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.09 | 0.16 | 0.30 | 0.85 | 0.19 | 0.05 | `ts_mean(div(sub(day_last(Close), day_first(Open)), day_first(Open)), 20)` |
| slot b seed 3 | 过 | 0.22 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.10 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `sub(ts_mean(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 20), ts_mean(div(sub(day_last(Close), day_first(Open)), day_first(Open)), 20))` |
| slot b seed 4 | 过 | 0.14 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.06 | 0.19 | 0.01 | 0.00 | 0.18 | 0.12 | `ts_corr(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), div(sub(day_last(Close), day_first(Open)), day_first(Open)), 40)` |
| slot b seed 5 | 过 | 0.18 | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` | 0.15 | 0.12 | 0.04 | 0.01 | 0.16 | 0.03 | `div(ts_std(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 40), ts_std(div(sub(day_last(Close), day_first(Open)), day_first(Open)), 40))` |
| slot b seed 6 | 过 | 0.10 | `day_quantile_q75(mul(High, Ret))` | 0.08 | 0.10 | 0.06 | 0.21 | 0.10 | 0.10 | `ts_corr(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), day_sum(in_slice(Volume, 0, 29)), 20)` |
| slot b seed 7 | 过 | 0.05 | `day_quantile_q75(mul(High, Ret))` | 0.03 | 0.03 | 0.05 | 0.04 | 0.04 | 0.02 | `ts_regres(ts_delay(div(sub(day_last(Close), day_first(Open)), day_first(Open)), 1), div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 60)` |
| slot b seed 8 | 过 | 0.18 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.09 | 0.22 | 0.15 | 0.06 | 0.22 | 0.04 | `ts_decay_linear(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 10)` |
| slot b seed 9 | 过 | 0.13 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.09 | 0.10 | 0.14 | 0.02 | 0.12 | 0.03 | `ts_corr(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), ts_delay(div(sub(day_last(Close), day_first(Open)), day_first(Open)), 1), 40)` |
| slot b seed 10 | 废品 | nan | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(s` | 0.00 | nan | nan | nan | nan | nan | `ts_mean(sub(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), cross_mean(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 1)), 20)` |
| slot b seed 11 | 过 | 0.08 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.09 | 0.06 | 0.10 | 0.10 | 0.08 | `ts_skew(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 60)` |
| slot b seed 12 | 过 | 0.04 | `day_quantile_q75(mul(High, Ret))` | 0.04 | 0.02 | 0.05 | 0.04 | 0.03 | 0.01 | `ts_regres(div(sub(day_last(Close), day_first(Open)), day_first(Open)), div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), 40)` |
| slot b seed 13 | 过 | 0.06 | `ts_std(cross_stddev(day_cov(cross_mean(Open, 241), Amt), 60)` | 0.10 | 0.05 | 0.04 | 0.15 | 0.05 | 0.04 | `ts_mean(mul(div(sub(day_first(Open), ts_delay(day_last(Close), 1)), ts_delay(day_last(Close), 1)), is_gt(day_sum(Amt), ts_mean(day_sum(Amt), 20))), 20)` |
