# 尺子 E:按相对挖掘冠军的 alpha 重筛 W02L 的 head(2026 未算)

做法见 ALPHA_PLAN.md。视窗 20180102 ~ 20251231,train 到 20230807;纯多头头部十分位、15 bp、减全市场等权的逐日净超额。核对:100.0% 的 head 重算的 D 与记录一致(最大差 0.000)。

挑选只用 train(对挖掘冠军的 α 的 t ≥ 2);valid 上的 α 没参与挑选，但 head 本身是按 D 在 train + valid 挑的。

## D 组合(主):train 上挑中 0 个;两段 α 都为正的 1 个;挑中的里 valid 上 t ≥ 2 的 0 个

## 原样组合:train 上挑中 3 个;两段 α 都为正的 65 个;挑中的里 valid 上 t ≥ 2 的 0 个

合并比例 a = 0.70(挖掘冠军占 70%)。**valid 判读:方向对、证据不够**

| 段 | 挖掘冠军 | W_E 腿 | 合并(a) | 合并(各半) | 两腿相关 | W_E 对冠军 α(t) | 评估比率 | 对两冠军 α(t) | 合并 − 冠军 |
|---|---|---|---|---|---|---|---|---|---|
| train | +23.0% / 4.03 | +8.1% / 1.86 | +18.7% / 4.25 | +15.6% / 4.06 | 0.16 | +5.3%(+2.75) | 1.23 | +2.1%(+1.13) | -4.55%(t -5.33) |
| valid | +17.1% / 2.13 | +8.5% / 1.44 | +14.5% / 2.30 | +12.8% / 2.31 | 0.25 | +5.4%(+1.41) | 0.94 | +3.1%(+0.95) | -2.57%(t -1.50) |

## 两段较差的评估比率最高的 30 个(head × 组合;只作描述)

| # | 组合 | train α(t) | valid α(t) | 评估比率 train / valid | 与冠军相关 valid | 自身夏普 valid | head |
|---|---|---|---|---|---|---|---|
| 1 | raw | +5.8%(+2.8) | +7.2%(+1.8) | 1.26 / 1.20 | 0.19 | 1.58 | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), d` |
| 2 | raw | +5.6%(+2.7) | +6.2%(+1.6) | 1.22 / 1.04 | 0.19 | 1.43 | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(cross_delay(cross_mean(mul(day_me` |
| 3 | raw | +3.9%(+1.6) | +7.8%(+2.0) | 0.72 / 1.31 | 0.12 | 1.56 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 4 | raw | +4.1%(+1.6) | +9.0%(+2.0) | 0.71 / 1.35 | 0.13 | 1.62 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 5 | raw | +4.1%(+1.6) | +9.0%(+2.0) | 0.71 / 1.35 | 0.13 | 1.62 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 6 | raw | +3.7%(+1.5) | +7.7%(+1.8) | 0.66 / 1.20 | 0.14 | 1.48 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 7 | raw | +2.9%(+1.6) | +3.6%(+1.0) | 0.70 / 0.65 | 0.37 | 1.39 | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), mul(cross_delay(c` |
| 8 | raw | +3.5%(+1.4) | +7.1%(+1.7) | 0.64 / 1.13 | 0.13 | 1.40 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 9 | raw | +3.6%(+1.4) | +7.7%(+1.9) | 0.63 / 1.28 | 0.17 | 1.63 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Volume, Volume, 20))), cross_corr(day_s` |
| 10 | raw | +3.6%(+1.4) | +7.7%(+1.9) | 0.63 / 1.28 | 0.17 | 1.63 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Volume, Volume, 20))), cross_corr(day_s` |
| 11 | raw | +3.5%(+1.4) | +7.7%(+1.9) | 0.63 / 1.29 | 0.17 | 1.63 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Amt, Volume, 20))), cross_corr(day_sum(` |
| 12 | raw | +3.6%(+1.4) | +8.0%(+1.8) | 0.63 / 1.19 | 0.18 | 1.56 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 13 | raw | +3.3%(+1.3) | +8.1%(+2.0) | 0.59 / 1.32 | 0.14 | 1.60 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 14 | raw | +3.2%(+1.3) | +7.8%(+1.9) | 0.59 / 1.28 | 0.13 | 1.55 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 15 | raw | +2.4%(+1.3) | +5.5%(+2.2) | 0.58 / 1.45 | -0.22 | 0.95 | `cross_corr(cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1), day_var(replace_small_` |
| 16 | raw | +2.7%(+1.4) | +3.2%(+0.9) | 0.64 / 0.58 | 0.35 | 1.29 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_la` |
| 17 | raw | +2.9%(+1.2) | +10.6%(+2.5) | 0.53 / 1.69 | -0.07 | 1.53 | `cross_regbeta(day_sum(Volume), ts_mean(day_skew(Volume), 5), 120)` |
| 18 | raw | +4.4%(+2.4) | +2.7%(+0.8) | 1.08 / 0.50 | 0.36 | 1.23 | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(cross_delay(cross_mean(mul(day_mean(H` |
| 19 | raw | +2.7%(+1.1) | +10.6%(+2.5) | 0.48 / 1.67 | 0.12 | 1.92 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(day_s` |
| 20 | raw | +2.5%(+1.0) | +6.9%(+1.2) | 0.46 / 0.78 | -0.45 | -0.26 | `cs_regres(cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_m` |
| 21 | raw | +2.5%(+1.0) | +6.9%(+1.2) | 0.46 / 0.78 | -0.45 | -0.26 | `cs_regres(cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_m` |
| 22 | raw | +2.4%(+1.0) | +7.4%(+1.9) | 0.44 / 1.25 | 0.07 | 1.39 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 23 | raw | +2.9%(+1.5) | +2.5%(+0.7) | 0.68 / 0.44 | 0.36 | 1.17 | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume))` |
| 24 | raw | +2.3%(+1.0) | +10.3%(+2.5) | 0.43 / 1.66 | -0.04 | 1.57 | `cross_regbeta(day_sum(Volume), ts_mean(day_skew(Volume), 10), 120)` |
| 25 | raw | +2.5%(+0.9) | +7.7%(+1.8) | 0.41 / 1.17 | 0.07 | 1.32 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_corr(day_sum(` |
| 26 | raw | +2.2%(+0.9) | +6.3%(+1.6) | 0.41 / 1.07 | 0.13 | 1.34 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 27 | raw | +2.1%(+0.9) | +5.8%(+1.5) | 0.40 / 0.98 | 0.15 | 1.30 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross` |
| 28 | raw | +1.8%(+0.8) | +10.4%(+2.6) | 0.35 / 1.72 | -0.05 | 1.61 | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120)` |
| 29 | raw | +1.6%(+0.8) | +4.9%(+1.0) | 0.34 / 0.66 | -0.36 | -0.15 | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replac` |
| 30 | raw | +1.6%(+0.7) | +6.7%(+1.6) | 0.33 / 1.08 | -0.28 | 0.44 | `cs_regres(cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_m` |
