# 相关度表:种子 2077,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.19 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.18 | 0.23 | 0.02 | 0.03 | 0.20 | 0.12 | `day_kurt(Amt)` |
| slot a seed 1 | 过 | 0.38 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.16 | 0.45 | 0.02 | 0.12 | 0.37 | 0.26 | `cross_mean(day_kurt(Amt), 20)` |
| slot a seed 2 | 过 | 0.10 | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max` | 0.10 | 0.02 | 0.04 | 0.01 | 0.03 | 0.00 | `cross_delta(day_kurt(Amt), 20)` |
| slot a seed 3 | 过 | 0.14 | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max` | 0.09 | 0.03 | 0.03 | 0.02 | 0.04 | 0.02 | `ts_scale(day_kurt(Amt), 40)` |
| slot a seed 4 | 过 | 0.18 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.14 | 0.24 | 0.02 | 0.43 | 0.23 | 0.08 | `cross_regres(day_kurt(Amt), day_sum(Amt), 30)` |
| slot a seed 5 | 过 | 0.18 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.14 | 0.25 | 0.04 | 0.39 | 0.24 | 0.08 | `cross_regres(day_kurt(Amt), day_std(Amt), 30)` |
| slot a seed 6 | 过 | 0.09 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.09 | 0.03 | 0.06 | 0.01 | 0.05 | 0.03 | `cross_corr(day_kurt(Amt), day_sum(in_slice(Ret, 1, 30)), 20)` |
| slot a seed 7 | 过 | 0.25 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.08 | 0.29 | 0.01 | 0.08 | 0.22 | 0.17 | `cross_stddev(day_kurt(Amt), 30)` |
| slot a seed 8 | 过 | 0.07 | `mul(cross_quantile_q25(cs_rank(day_last(Close)), 60), ts_max` | 0.18 | 0.07 | 0.08 | 0.01 | 0.06 | 0.01 | `sub(cross_mean(day_kurt(Amt), 10), cross_mean(day_kurt(Amt), 60))` |
| slot a seed 9 | 过 | 0.35 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.23 | 0.42 | 0.49 | 0.04 | 0.41 | 0.01 | `cross_corr(day_kurt(Amt), day_kurt(Volume), 30)` |
| slot a seed 10 | 过 | 0.15 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), cre` | 0.14 | 0.06 | 0.07 | 0.01 | 0.08 | 0.02 | `cross_reg_tvalue(day_kurt(Amt), day_sum(Ret), 30)` |
| slot a seed 11 | 过 | 0.15 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 20), cre` | 0.17 | 0.11 | 0.09 | 0.06 | 0.13 | 0.06 | `cross_corr(day_kurt(Amt), day_std(Ret), 20)` |
| slot a seed 12 | 废品 | 0.06 | `day_open(in_delta(Volume, 60))` | 0.06 | 0.04 | 0.07 | 0.04 | 0.04 | 0.00 | `ts_mean(cross_rank(day_kurt(Amt), 20), 10)` |
| slot b seed 1 | 过 | 0.27 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.14 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open))), 20)` |
| slot b seed 2 | 过 | 0.30 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.15 | 0.38 | 0.36 | 0.21 | 0.39 | 0.07 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open))), 60)` |
| slot b seed 3 | 过 | 0.20 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.12 | 0.25 | 0.09 | 0.15 | 0.25 | 0.04 | `cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 40)` |
| slot b seed 4 | 过 | 0.29 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.14 | 0.32 | 0.43 | 0.49 | 0.35 | 0.06 | `cross_mean(div(day_last(Close), day_first(Open)), 40)` |
| slot b seed 5 | 过 | 0.14 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), cre` | 0.07 | 0.18 | 0.00 | 0.01 | 0.17 | 0.11 | `cross_corr(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open)), 30)` |
| slot b seed 6 | 过 | 0.02 | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), n` | 0.05 | 0.01 | 0.04 | 0.05 | 0.02 | 0.01 | `cross_regres(div(day_last(Close), day_first(Open)), div(day_first(Open), cross_delay(day_last(Close), 1)), 30)` |
| slot b seed 7 | 过 | 0.14 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), cre` | 0.07 | 0.18 | 0.00 | 0.01 | 0.17 | 0.11 | `cross_reg_tvalue(div(day_last(Close), day_first(Open)), div(day_first(Open), cross_delay(day_last(Close), 1)), 30)` |
| slot b seed 8 | 过 | 0.34 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.32 | 0.42 | 0.58 | 0.17 | 0.46 | 0.01 | `cross_stddev(div(day_first(Open), cross_delay(day_last(Close), 1)), 20)` |
| slot b seed 9 | 过 | 0.27 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.14 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `sub(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 20), cross_mean(div(day_last(Close), day_first(Open)), 20))` |
| slot b seed 10 | 过 | 0.69 | `neg(inv(pow_2(ts_regbeta(day_quantile_q75(Amt), day_hurst(Op` | 0.20 | 0.97 | 0.39 | 0.13 | 0.97 | 0.59 | `cross_mean(mul(div(day_last(Close), day_first(Open)), day_sum(in_slice(Amt, 1, 30))), 20)` |
