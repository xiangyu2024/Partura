# 相关度表:种子 907,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 10 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.96 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.99 | 0.54 | 0.42 | 0.13 | 0.56 | 0.14 | `cross_mean(day_centroid(Volume), 30)` |
| slot a seed 1 | 过 | 0.71 | `signedpower(cs_first_low40(abs_(LogFloatShares), LogFloatSha` | 0.72 | 0.45 | 0.17 | 0.08 | 0.47 | 0.59 | `cs_first_low40(cross_mean(day_centroid(Volume), 30), LogFloatShares)` |
| slot a seed 2 | 过 | 0.76 | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Vol` | 0.70 | 0.58 | 0.38 | 0.17 | 0.63 | 0.37 | `cs_first_low40(cross_mean(day_centroid(Volume), 30), day_std(Volume))` |
| slot a seed 3 | 过 | 0.66 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.80 | 0.55 | 0.25 | 0.14 | 0.56 | 0.54 | `cs_first_low20(cross_mean(day_centroid(Volume), 30), LogFloatCap)` |
| slot a seed 4 | 过 | 0.50 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.77 | 0.63 | 0.15 | 0.13 | 0.63 | 0.75 | `cs_first_low40(cross_mean(day_centroid(Volume), 30), LogFloatCap)` |
| slot a seed 5 | 过 | 0.67 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.65 | 0.52 | 0.30 | 0.13 | 0.52 | 0.17 | `cs_first_low20(cross_mean(day_centroid(Volume), 30), day_last(Vwap))` |
| slot a seed 6 | 过 | 0.10 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.25 | 0.01 | 0.12 | 0.05 | 0.02 | 0.06 | `cs_first_low20(cross_mean(day_centroid(Volume), 30), cross_mean(day_centroid(Volume), 30))` |
| slot a seed 7 | 过 | 0.73 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.81 | 0.25 | 0.33 | 0.08 | 0.26 | 0.28 | `cs_first_high40(LogFloatShares, cross_mean(day_centroid(Volume), 30))` |
| slot a seed 8 | 过 | 0.74 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.74 | 0.49 | 0.40 | 0.16 | 0.52 | 0.10 | `cs_first_high40(cs_first_low40(LogFloatShares, day_std(Volume)), cross_mean(day_centroid(Volume), 30))` |
| slot a seed 9 | 过 | 0.79 | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Vol` | 0.73 | 0.50 | 0.45 | 0.19 | 0.54 | 0.05 | `mul(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_first_low40(LogFloatShares, day_std(Volume))))` |
| slot a seed 10 | 过 | 0.65 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.69 | 0.18 | 0.37 | 0.09 | 0.20 | 0.46 | `mul(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(LogFloatShares))` |
| slot a seed 11 | 过 | 0.74 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.88 | 0.80 | 0.42 | 0.12 | 0.83 | 0.33 | `cs_first_low40(cross_mean(day_centroid(Volume), 30), cross_mean(day_std(Amt), 30))` |
| slot a seed 12 | 过 | 0.72 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.88 | 0.82 | 0.39 | 0.11 | 0.83 | 0.34 | `cs_first_low40(cross_mean(day_centroid(Volume), 30), cross_mean(day_sum(Amt), 30))` |
| slot a seed 13 | 过 | 0.47 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.50 | 0.52 | 0.18 | 0.13 | 0.52 | 0.44 | `cs_first_low20(cs_first_low20(cross_mean(day_centroid(Volume), 30), LogFloatCap), day_last(Vwap))` |
| slot a seed 14 | 过 | 0.68 | `signedpower(cs_first_low40(abs_(LogFloatShares), LogFloatSha` | 0.69 | 0.45 | 0.12 | 0.08 | 0.47 | 0.68 | `cs_first_low40(cs_first_low20(cross_mean(day_centroid(Volume), 30), LogFloatCap), LogFloatShares)` |
| slot a seed 15 | 过 | 0.43 | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_fi` | 0.52 | 0.17 | 0.01 | 0.10 | 0.19 | 0.33 | `cs_first_high40(cross_mean(day_centroid(Volume), 30), day_std(Volume))` |
| slot a seed 16 | 过 | 0.64 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.48 | 0.04 | 0.26 | 0.06 | 0.05 | 0.49 | `cs_first_high40(cross_mean(day_centroid(Volume), 30), LogFloatShares)` |
| slot b seed 1 | 过 | 0.60 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.60 | 0.46 | 0.23 | 0.20 | 0.46 | 0.38 | `cross_mean(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume)), 20)` |
| slot b seed 2 | 过 | 0.61 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.60 | 0.45 | 0.23 | 0.19 | 0.45 | 0.35 | `cross_mean(div(day_sum(in_slice(Volume, 211, 239)), day_sum(in_slice(Volume, 1, 239))), 20)` |
| slot b seed 3 | 过 | 0.33 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.27 | 0.32 | 0.03 | 0.09 | 0.27 | 0.43 | `cross_mean(div(day_last(Volume), day_sum(Volume)), 30)` |
| slot b seed 4 | 过 | 0.96 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.99 | 0.52 | 0.43 | 0.13 | 0.55 | 0.11 | `cross_mean(day_centroid(in_slice(Volume, 1, 239)), 30)` |
| slot b seed 5 | 过 | 0.65 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.50 | 0.32 | 0.43 | 0.06 | 0.37 | 0.16 | `cross_mean(day_centroid(in_slice(Volume, 1, 120)), 30)` |
| slot b seed 6 | 过 | 0.34 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.27 | 0.30 | 0.06 | 0.13 | 0.28 | 0.43 | `cross_mean(day_centroid(in_slice(Volume, 121, 239)), 30)` |
| slot b seed 7 | 过 | 0.84 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.77 | 0.42 | 0.45 | 0.10 | 0.47 | 0.06 | `cross_mean(div(day_sum(in_slice(Volume, 1, 30)), day_sum(in_slice(Volume, 1, 239))), 30)` |
| slot b seed 8 | 过 | 0.44 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.27 | 0.12 | 0.33 | 0.01 | 0.17 | 0.31 | `cross_mean(div(day_sum(in_slice(Volume, 61, 180)), day_sum(Volume)), 30)` |
| slot b seed 9 | 过 | 0.58 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.53 | 0.26 | 0.28 | 0.07 | 0.29 | 0.23 | `cross_mean(sub(day_centroid(Ret), day_centroid(Volume)), 30)` |
| slot b seed 10 | 过 | 0.14 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.08 | 0.01 | 0.04 | 0.15 | 0.00 | 0.11 | `cross_mean(day_signed_ratio(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), 30)` |
| slot b seed 11 | 过 | 0.16 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.10 | 0.13 | 0.06 | 0.08 | 0.12 | 0.03 | `cross_mean(day_sum(in_slice(Ret, 211, 240)), 30)` |
| slot b seed 12 | 过 | 0.15 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.09 | 0.07 | 0.13 | 0.17 | 0.08 | 0.13 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 30)` |
| slot b seed 13 | 废品 | 0.16 | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), da` | 0.09 | 0.18 | 0.21 | 0.05 | 0.20 | 0.08 | `cross_med(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 30)` |
| slot b seed 14 | 过 | 0.23 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.08 | 0.21 | 0.38 | 0.59 | 0.25 | 0.02 | `cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 30)` |
| slot b seed 15 | 过 | 0.17 | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Vol` | 0.07 | 0.17 | 0.31 | 0.26 | 0.20 | 0.07 | `sub(cs_rank(cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 30)), cs_rank(cross_mean(sub(div(day_last(Close), day_first(Open)), 1), 30)))` |
| R 1 variant 1 | 过 | 0.92 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.98 | 0.03 | 0.32 | 0.10 | 0.05 | 0.18 | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 2 | 过 | 0.97 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.99 | 0.20 | 0.37 | 0.12 | 0.23 | 0.08 | `add(cs_rank(cross_mean(day_centroid(Volume), 30)), mul(0.4, cs_rank(cross_mean(day_std(Amt), 30))))` |
| R 1 variant 3 | 过 | 0.92 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.98 | 0.03 | 0.32 | 0.10 | 0.06 | 0.18 | `add(cs_rank(cross_mean(day_centroid(Volume), 30)), mul(0.56, cs_rank(cross_mean(day_std(Amt), 30))))` |
| R 1 variant 4 | 过 | 0.92 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.98 | 0.03 | 0.31 | 0.10 | 0.05 | 0.18 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 30)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 1 variant 5 | 过 | 0.99 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 1.00 | 0.30 | 0.45 | 0.14 | 0.35 | 0.02 | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_gini(Volume), 30)))` |
| R 1 variant 6 | 过 | 0.84 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mea` | 0.90 | 0.05 | 0.32 | 0.09 | 0.06 | 0.20 | `cs_regres(cs_rank(cross_ema(day_centroid(Volume), 20)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| R 2 variant 1 | 过 | 0.89 | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_fi` | 0.81 | 0.29 | 0.14 | 0.11 | 0.32 | 0.38 | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))))` |
| R 2 variant 2 | 过 | 0.86 | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_fi` | 0.84 | 0.29 | 0.22 | 0.12 | 0.32 | 0.19 | `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` |
| R 2 variant 3 | 过 | 1.00 | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Vol` | 1.00 | 0.33 | 0.30 | 0.16 | 0.36 | 0.01 | `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` |
