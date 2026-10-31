# 定位:种子 801,P 组,第 2 轮(只含 train / valid)

快照:c07s801M1_I0_open_search, c07s801M2_I0_open_search, c08s801Pr1a_Ea, c08s801Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.64 | +0.64 | +1.39 | -1 | 5 | c08s801Pr1a_Ea | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)` |

## 共性:317 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.24 | 0.001 | 6 | -0.02 / -1.26 | `cs_last_high20(LimitWidth, ts_med(LimitWidth, 50))` |
| +1.19 | 0.002 | 7 | -0.08 / -1.26 | `cs_last_low10(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20))` |
| +1.17 | 0.000 | 35 | -0.19 / -1.37 | `day_centroid(Volume)` |
| +1.15 | 0.000 | 14 | -0.14 / -1.29 | `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` |
| +1.03 | 0.018 | 4 | -0.22 / -1.25 | `pow_1_5(pow_1_5(LimitWidth))` |
| +1.03 | 0.000 | 22 | -0.28 / -1.31 | `day_sum(Volume)` |
| +0.93 | 0.030 | 4 | -0.32 / -1.25 | `cross_semistd_pos(LimitWidth, 60)` |
| +0.90 | 0.055 | 4 | -0.35 / -1.25 | `cs_last_high20(cross_semistd_pos(pow_1_5(LimitWidth), 10), ts_med(LimitWidth, 50))` |
| +0.90 | 0.055 | 4 | -0.35 / -1.25 | `cross_semistd_pos(pow_1_5(LimitWidth), 10)` |
| +0.74 | 0.000 | 34 | -0.57 / -1.32 | `pow_1_5(LimitWidth)` |
| +0.71 | 0.118 | 4 | -0.54 / -1.25 | `pow_3(LogFloatShares)` |
| +0.69 | 0.000 | 30 | -0.61 / -1.30 | `ts_med(LimitWidth, 50)` |
| +0.68 | 0.019 | 19 | -0.60 / -1.28 | `div(day_topw_mean(High, Open), day_durbin_watson(Volume))` |
| +0.67 | 0.007 | 13 | -0.59 / -1.26 | `cs_last_low10(day_centroid(Volume), BoardCode)` |
| +0.67 | 0.060 | 8 | -0.58 / -1.25 | `ts_kurt(day_quantile_q25(Volume), 50)` |
| +0.63 | 0.165 | 4 | -0.61 / -1.25 | `cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15)` |
| +0.63 | 0.165 | 4 | -0.61 / -1.25 | `pow_05(cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15))` |
| +0.61 | 0.090 | 8 | -0.64 / -1.25 | `pow_2_5(pow_2_5(day_durbin_watson(Volume)))` |
| +0.58 | 0.010 | 21 | -0.70 / -1.28 | `cross_semistd_pos(pow_1_5(LimitWidth), 60)` |
| +0.57 | 0.244 | 4 | -0.67 / -1.24 | `cs_last_high20(cross_semistd_pos(pow_1_5(LimitWidth), 60), ts_kurt(log(day_quantile_q25(Volume)), 50))` |

## 拆解(11 次评估)

### head score +0.64:`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20))` | +0.08 | +0.68 | +0.08 | — | (子树本身) |
| sufficiency | `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` | -0.40 | -0.40 | -0.03 | — | (子树本身) |
| sufficiency | `div(day_topw_mean(High, Open), day_durbin_watson(Volume))` | -1.06 | -1.06 | -0.31 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20))` | +0.19 | +1.42 | +0.19 | +0.45 | `ts_corr(day_centroid(Volume), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)` |
| knockout | `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` | -0.36 | -0.36 | +0.29 | +1.00 | `ts_corr(cs_last_low05(day_centroid(Volume), day_durbin_watson(Volume)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)` |
| knockout | `div(day_topw_mean(High, Open), day_durbin_watson(Volume))` | +0.57 | +0.57 | +2.34 | +0.07 | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), day_topw_mean(High, Open), 50)` |
| swap | `Volume->Amt` | +0.57 | +0.57 | +0.88 | — | `ts_corr(cs_last_low05(day_centroid(Amt), cross_corr(day_durbin_watson(Amt), day_sum(Amt), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Amt)), 50)` |
| swap | `High->Low` | +0.62 | +0.62 | +1.35 | — | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(Low, Open), day_durbin_watson(Volume)), 50)` |
| window | `ts_corr@50->25` | +0.63 | +0.63 | +0.65 | — | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 25)` |
| window | `ts_corr@50->100` | +0.13 | +0.77 | +0.13 | — | `ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_high20(LimitWidth, ts_med(LimitWidth, 50))` — enrichment,均值差 +1.24,p 0.001
2. `cs_last_low10(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20))` — enrichment,均值差 +1.19,p 0.002
3. `day_centroid(Volume)` — enrichment,均值差 +1.17,p 0.000
4. `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` — enrichment,均值差 +1.15,p 0.000
5. `pow_1_5(pow_1_5(LimitWidth))` — enrichment,均值差 +1.03,p 0.018
6. `day_sum(Volume)` — enrichment,均值差 +1.03,p 0.000
7. `cross_semistd_pos(LimitWidth, 60)` — enrichment,均值差 +0.93,p 0.030
8. `cs_last_high20(cross_semistd_pos(pow_1_5(LimitWidth), 10), ts_med(LimitWidth, 50))` — enrichment,均值差 +0.90,p 0.055
9. `cross_semistd_pos(pow_1_5(LimitWidth), 10)` — enrichment,均值差 +0.90,p 0.055
10. `pow_1_5(LimitWidth)` — enrichment,均值差 +0.74,p 0.000
11. `ts_med(LimitWidth, 50)` — enrichment,均值差 +0.69,p 0.000
12. `div(day_topw_mean(High, Open), day_durbin_watson(Volume))` — enrichment,均值差 +0.68,p 0.019
13. `cs_last_low10(day_centroid(Volume), BoardCode)` — enrichment,均值差 +0.67,p 0.007
14. `ts_kurt(day_quantile_q25(Volume), 50)` — enrichment,均值差 +0.67,p 0.060
15. `pow_2_5(pow_2_5(day_durbin_watson(Volume)))` — enrichment,均值差 +0.61,p 0.090
16. `cross_semistd_pos(pow_1_5(LimitWidth), 60)` — enrichment,均值差 +0.58,p 0.010
17. `day_topw_mean(High, Open)` — enrichment,均值差 +0.53,p 0.028
18. `day_durbin_watson(Volume)` — enrichment,均值差 +0.44,p 0.001
19. `day_corr(Ret, Volume)` — enrichment,均值差 +0.23,p 0.055

## 本组之前各轮的任务

- `c08s801Pr1a_Ea`:核心 `day_durbin_watson(Volume)`;评分 97,过线 4,入 heads 1;采样计数 {'c05_no_core': 1821, 'c05_periphery_seen': 7}
  - score +0.64(train +0.64 valid +1.39):`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 50)`
  - score +0.59(train +0.59 valid +0.75):`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, Open), day_durbin_watson(Volume)), 30)`
  - score +0.55(train +0.94 valid +0.55):`ts_corr(cs_last_low05(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)), div(day_sum(Volume), day_durbin_watson(Volume)), 30)`
  - score +0.51(train +1.00 valid +0.51):`ts_corr(cs_last_low10(day_centroid(Volume), cross_corr(day_sum(Volume), day_sum(Volume), 20)), div(day_topw_mean(High, High), day_durbin_watson(Volume)), 40)`
  - score +0.42(train +0.42 valid +0.49):`cs_last_low10(day_centroid(Volume), cs_last_low10(day_centroid(Volume), cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)))`
- `c08s801Pr1b_Nb`:核心 `—`;评分 76,过线 0,入 heads 0;采样计数 {}
  - score +0.30(train +0.30 valid +1.35):`cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 20), cross_mean(day_mean(Ret), 20))`
  - score +0.30(train +0.30 valid +1.39):`cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Volume), 20), cross_mean(day_mean(Ret), 20))`
  - score +0.10(train +0.10 valid +0.56):`cross_mean(day_corr(Ret, Volume), 60)`
  - score +0.09(train +0.09 valid +1.37):`cross_mean(sub(cross_mean(day_corr(Ret, Volume), 60), day_corr(Ret, Volume)), 60)`
  - score +0.07(train +0.07 valid +0.57):`cross_mean(sub(day_wmean(Ret, Volume), day_corr(Ret, Volume)), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
