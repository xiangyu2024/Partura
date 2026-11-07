# 相关度表:种子 904,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.03 | 0.03 | 0.14 | 0.03 | 0.03 | `day_topw_mean(Ret, Amt)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.49 | 0.37 | 0.24 | 0.50 | 0.20 | `cross_ema(day_topw_mean(Ret, Amt), 60)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.50 | 0.27 | 0.12 | 0.50 | 0.22 | `cross_ema(day_topw_mean(Ret, Amt), 241)` |
| slot a seed 3 | 过 | 0.00 | `—` | 0.00 | 0.33 | 0.38 | 0.44 | 0.35 | 0.14 | `cross_mean(day_topw_mean(Ret, Amt), 30)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.14 | 0.51 | 0.01 | 0.01 | `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.36 | 0.36 | 0.45 | 0.19 | `cross_ema(div(day_topw_mean(Ret, Amt), cross_mean(day_std(Ret), 60)), 30)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.44 | 0.28 | 0.23 | 0.43 | 0.30 | `cross_ema(div(day_topw_mean(Ret, Amt), day_wstd(Ret, Amt)), 60)` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.42 | 0.37 | 0.24 | 0.44 | 0.17 | `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60)` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.45 | 0.50 | 0.01 | 0.45 | 0.16 | `cross_ema(mul(day_topw_mean(Ret, Amt), sign(day_sum(Ret))), 60)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.07 | 0.02 | 0.26 | 0.05 | `ts_corr(day_topw_mean(Ret, Amt), day_sum(Ret), 50)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.03 | 0.01 | 0.02 | 0.00 | `ts_corr(ts_delay(day_topw_mean(Ret, Amt), 1), day_sum(Ret), 50)` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.07 | 0.37 | 0.02 | 0.05 | `cross_ema(ts_rank(day_topw_mean(Ret, Amt), 20), 30)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.47 | 0.11 | 0.24 | 0.24 | `cross_tail_mean_q25(day_topw_mean(Ret, Amt), 60)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.49 | 0.63 | 0.12 | 0.52 | 0.05 | `cross_tail_mean_q75(day_topw_mean(Ret, Amt), 60)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.41 | 0.06 | 0.25 | 0.40 | 0.27 | `cs_bucket_rank(cross_ema(day_topw_mean(Ret, Amt), 60), cross_mean(day_std(Ret), 60))` |
| slot a seed 15 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.05 | 0.03 | 0.03 | 0.02 | `cs_flip_by_state(cross_ema(day_topw_mean(Ret, Amt), 60), cross_ema(day_sum(Ret), 60))` |
| slot a seed 16 | 过 | 0.00 | `—` | 0.00 | 0.36 | 0.06 | 0.12 | 0.30 | 0.42 | `cross_ema(sub(day_topw_mean(Ret, Amt), day_wmean(Ret, Amt)), 60)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.16 | 0.13 | 0.00 | 0.24 | `cross_ema(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.18 | 0.09 | 0.05 | 0.29 | `cross_ema(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 241)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.31 | 0.41 | 0.38 | 0.34 | 0.01 | `cross_ema(log(div(day_last(Close), day_first(Open))), 60)` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.20 | 0.35 | 0.19 | 0.22 | 0.09 | `cross_ema(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open)))), 60)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.29 | 0.09 | 0.16 | 0.13 | `cross_ema(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open)))), 241)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.17 | 0.13 | 0.07 | 0.20 | `cross_mean(cs_winsor(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 60)` |
| slot b seed 7 | 废品 | 0.00 | `—` | 0.00 | 0.04 | 0.15 | 0.06 | 0.07 | 0.12 | `cross_mean(sign(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 60)` |
| slot b seed 8 | 废品 | 0.00 | `—` | 0.00 | 0.08 | 0.21 | 0.09 | 0.10 | 0.13 | `cross_mean(sub(sign(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), sign(log(div(day_last(Close), day_first(Open))))), 60)` |
| slot b seed 9 | 废品 | 0.00 | `—` | 0.00 | 0.17 | 0.01 | 0.03 | 0.15 | 0.07 | `cross_mean(mul(sign(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), sign(log(div(day_last(Close), day_first(Open))))), 60)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.14 | 0.04 | 0.07 | 0.12 | `cross_mean(cs_winsor(mul(sign(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), log(div(day_last(Close), day_first(Open))))), 60)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.06 | 0.02 | 0.16 | 0.12 | `ts_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 50)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.07 | 0.02 | 0.22 | 0.16 | `cross_ema(ts_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 20), 30)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.06 | 0.12 | 0.03 | 0.21 | `cross_ema(div(log(div(day_first(Open), ts_delay(day_last(Close), 1))), cross_mean(day_std(Ret), 60)), 60)` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.03 | 0.09 | 0.07 | 0.04 | `cross_ema(cross_zscore(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), 30)` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.12 | 0.05 | 0.12 | 0.12 | 0.04 | `sub(cross_ema(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 15), cross_ema(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 241))` |
| slot b seed 16 | 过 | 0.00 | `—` | 0.00 | 0.39 | 0.51 | 0.05 | 0.41 | 0.20 | `cross_tail_mean_q25(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60)` |
