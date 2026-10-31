# 定位:种子 802,P 组,第 2 轮(只含 train / valid)

快照:c07s802M1_I0_open_search, c07s802M2_I0_open_search, c08s802Pr1a_Ea, c08s802Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(12 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.70 | +1.72 | +1.70 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 20), signedpower(signedpower(day_centroid(Volume))))` |
| +1.23 | +1.73 | +1.23 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| +1.19 | +1.25 | +1.19 | -1 | 20 | c07s802M1_I0_open_search | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 30))` |
| +1.10 | +1.10 | +1.14 | -1 | 20 | c08s802Pr1a_Ea | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 30)` |
| +1.00 | +1.00 | +1.42 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(ts_reg_fvalue(ts_mean(cross_argmax(day_hurst(Volume), 3), 50), cs_stddev_full(cross_mean(day_min(High), 30)), 5), 241), 20), day_centroid(Volume))` |
| +1.00 | +1.00 | +1.66 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(day_centroid(Volume), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(day_centroid(Volume), 20), day_centroid(Volume)))` |
| +0.86 | +0.86 | +1.79 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume)))))` |
| +0.81 | +0.81 | +1.47 | +1 | 5 | c08s802Pr1a_Ea | `ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)` |
| +0.75 | +0.75 | +0.94 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 10), 20), day_centroid(Volume))), 241), 20), cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 10), 20), day_centroid(Volume)))` |
| +0.70 | +0.70 | +1.20 | +1 | 20 | c08s802Pr1a_Ea | `cross_regbeta(day_sum(Volume), ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 30), 20)` |
| +0.70 | +0.70 | +1.00 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), 20), day_centroid(Volume))` |
| +0.61 | +0.61 | +0.61 | -1 | 20 | c07s802M2_I0_open_search | `cs_first_high40(ts_argmin(cs_regres(pow_05(cs_last_low10(day_hurst(Close), day_max(High))), signedpower(cs_last_low40(day_topw_mean(Ret, High), LimitWidth))), 20), day_centroid(Volume))` |

## 共性:302 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.08 | 0.001 | 5 | +0.99 / -1.10 | `cross_quantile_q25(day_centroid(Volume), 241)` |
| +2.08 | 0.001 | 5 | +0.99 / -1.10 | `ts_argmin(cross_quantile_q25(day_centroid(Volume), 241), 20)` |
| +2.04 | 0.000 | 6 | +0.94 / -1.10 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))` |
| +2.04 | 0.000 | 16 | +0.87 / -1.17 | `cross_quantile_q25(signedpower(day_centroid(Volume)), 241)` |
| +2.02 | 0.000 | 13 | +0.87 / -1.15 | `ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20)` |
| +1.81 | 0.000 | 54 | +0.42 / -1.38 | `day_centroid(Volume)` |
| +1.73 | 0.000 | 33 | +0.48 / -1.25 | `signedpower(day_centroid(Volume))` |
| +1.64 | 0.006 | 4 | +0.56 / -1.08 | `day_mean(neg(neg(in_delta(Volume, 5))))` |
| +1.56 | 0.006 | 8 | +0.46 / -1.10 | `signedpower(signedpower(day_centroid(Volume)))` |
| +1.38 | 0.009 | 5 | +0.30 / -1.08 | `day_mean(in_delta(Volume, 5))` |
| +1.22 | 0.000 | 16 | +0.09 / -1.12 | `day_mean(neg(in_delta(Volume, 60)))` |
| +1.11 | 0.006 | 8 | +0.02 / -1.09 | `cs_median(cs_robust_z(day_last(Amt)))` |
| +1.00 | 0.000 | 22 | -0.13 / -1.13 | `day_last(Amt)` |
| +0.94 | 0.140 | 6 | -0.14 / -1.08 | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` |
| +0.94 | 0.140 | 6 | -0.14 / -1.08 | `day_flat_run_max(Vwap)` |
| +0.92 | 0.195 | 4 | -0.15 / -1.07 | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` |
| +0.90 | 0.090 | 10 | -0.19 / -1.09 | `sqrt(day_quantile_q25(Open))` |
| +0.90 | 0.090 | 10 | -0.19 / -1.09 | `day_quantile_q25(Open)` |
| +0.88 | 0.002 | 19 | -0.23 / -1.12 | `cs_robust_z(day_last(Amt))` |
| +0.87 | 0.060 | 15 | -0.24 / -1.10 | `ts_argmin(cross_quantile_q25(LogFloatShares, 241), 40)` |

## 拆解(30 次评估)

### head score +1.70:`cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 20), signedpower(signedpower(day_centroid(Volume))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 20)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241)` | -0.07 | +0.90 | -0.07 | — | (子树本身) |
| sufficiency | `signedpower(signedpower(signedpower(day_centroid(Volume))))` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| sufficiency | `signedpower(signedpower(day_centroid(Volume)))` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 20)` | -0.00 | +0.73 | -0.00 | +1.70 | `cs_first_high40(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), signedpower(signedpower(day_centroid(Volume))))` |
| knockout | `cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241)` | +0.15 | +0.15 | +1.40 | +1.55 | `cs_first_high40(ts_argmin(signedpower(signedpower(signedpower(day_centroid(Volume)))), 20), signedpower(signedpower(day_centroid(Volume))))` |
| knockout | `signedpower(signedpower(signedpower(day_centroid(Volume))))` | +1.67 | +1.75 | +1.67 | +0.02 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(day_centroid(Volume))), 241), 20), signedpower(signedpower(day_centroid(Volume))))` |
| swap | `Volume->Amt` | +1.40 | +1.67 | +1.40 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Amt)))), 241), 20), signedpower(signedpower(day_centroid(Amt))))` |
| window | `ts_argmin@20->10` | +1.55 | +1.67 | +1.55 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 10), signedpower(signedpower(day_centroid(Volume))))` |
| window | `ts_argmin@20->40` | +1.60 | +1.78 | +1.60 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(signedpower(signedpower(day_centroid(Volume)))), 241), 40), signedpower(signedpower(day_centroid(Volume))))` |

### head score +1.23:`cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 20)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241)` | +0.54 | +0.54 | +0.66 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` | +1.33 | +1.75 | +1.33 | — | (子树本身) |
| knockout | `ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 20)` | +1.07 | +1.07 | +1.12 | +0.16 | `cs_first_high40(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| knockout | `cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241)` | +1.64 | +1.91 | +1.64 | -0.41 | `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| knockout | `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` | +0.55 | +1.23 | +0.55 | +0.68 | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 20), signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))))` |
| swap | `Volume->Amt` | +1.12 | +1.73 | +1.12 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Amt)), 241), 20), day_centroid(Amt))), 241), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Amt)), 241), 20), day_centroid(Amt))), 241))` |
| window | `ts_argmin@20->10` | +1.42 | +1.42 | +1.47 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 10), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |
| window | `ts_argmin@20->40` | +0.89 | +1.54 | +0.89 | — | `cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 40), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))` |

### head score +1.19:`day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_sum(Volume), 20)` | -1.95 | -0.51 | -1.95 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -0.22 | -0.22 | +0.08 | — | (子树本身) |
| knockout | `cross_mean(day_sum(Volume), 20)` | +0.84 | +0.84 | +1.18 | +0.35 | `day_mean(in_delta(div(Volume, day_sum(Volume)), 30))` |
| swap | `Volume->Amt` | +1.13 | +1.26 | +1.13 | — | `day_mean(in_delta(div(Amt, cross_mean(day_sum(Amt), 20)), 30))` |
| window | `in_delta@30->15` | +1.31 | +1.31 | +1.74 | — | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 15))` |
| window | `in_delta@30->60` | +0.18 | +1.12 | +0.18 | — | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 60))` |

### head score +1.10:`cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_delta(Volume, 30))` | +0.69 | +0.69 | +0.98 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -0.22 | -0.22 | +0.08 | — | (子树本身) |
| swap | `Volume->Amt` | +1.10 | +1.10 | +1.26 | — | `cross_reg_tvalue(day_sum(Amt), day_mean(in_delta(Amt, 30)), 30)` |
| window | `cross_reg_tvalue@30->15` | -0.18 | +1.23 | -0.18 | — | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 15)` |
| window | `cross_reg_tvalue@30->60` | +1.51 | +1.69 | +1.51 | — | `cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241)` — ablation,自身 score +1.33(所在 head +1.23)
2. `day_mean(in_delta(Volume, 30))` — ablation,自身 score +0.69(所在 head +1.10)
3. `cross_quantile_q25(day_centroid(Volume), 241)` — enrichment,均值差 +2.08,p 0.001
4. `ts_argmin(cross_quantile_q25(day_centroid(Volume), 241), 20)` — enrichment,均值差 +2.08,p 0.001
5. `cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))` — enrichment,均值差 +2.04,p 0.000
6. `cross_quantile_q25(signedpower(day_centroid(Volume)), 241)` — enrichment,均值差 +2.04,p 0.000
7. `ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20)` — enrichment,均值差 +2.02,p 0.000
8. `day_centroid(Volume)` — enrichment,均值差 +1.81,p 0.000
9. `signedpower(day_centroid(Volume))` — enrichment,均值差 +1.73,p 0.000
10. `day_mean(neg(neg(in_delta(Volume, 5))))` — enrichment,均值差 +1.64,p 0.006
11. `signedpower(signedpower(day_centroid(Volume)))` — enrichment,均值差 +1.56,p 0.006
12. `day_mean(in_delta(Volume, 5))` — enrichment,均值差 +1.38,p 0.009
13. `day_mean(neg(in_delta(Volume, 60)))` — enrichment,均值差 +1.22,p 0.000
14. `cs_median(cs_robust_z(day_last(Amt)))` — enrichment,均值差 +1.11,p 0.006
15. `day_last(Amt)` — enrichment,均值差 +1.00,p 0.000
16. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +0.90,p 0.090
17. `day_quantile_q25(Open)` — enrichment,均值差 +0.90,p 0.090
18. `cs_robust_z(day_last(Amt))` — enrichment,均值差 +0.88,p 0.002
19. `ts_argmin(cross_quantile_q25(LogFloatShares, 241), 40)` — enrichment,均值差 +0.87,p 0.060
20. `cs_stddev_full(cs_robust_z(day_last(Amt)))` — enrichment,均值差 +0.63,p 0.070

## 本组之前各轮的任务

- `c08s802Pr1a_Ea`:核心 `day_mean(in_delta(Volume, 30))`;评分 85,过线 4,入 heads 3;采样计数 {'c05_no_core': 2445, 'mutation_refused': 5, 'c05_skeleton': 9}
  - score +1.10(train +1.10 valid +1.14):`cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 30)`
  - score +1.08(train +1.28 valid +1.08):`cross_regbeta(day_sum(Volume), day_mean(in_delta(Volume, 30)), 20)`
  - score +0.81(train +0.81 valid +1.47):`ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 50)`
  - score +0.70(train +0.70 valid +1.20):`cross_regbeta(day_sum(Volume), ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 30), 20)`
  - score +0.50(train +0.50 valid +0.74):`ts_autocorr_s1(day_mean(in_delta(Volume, 30)), 30)`
- `c08s802Pr1b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {}
  - score -0.35(train -0.35 valid +0.87):`cross_mean(cross_mean(day_signed_ratio(Ret, Volume), 20), 20)`
  - score -0.35(train -0.35 valid +0.97):`cross_mean(cross_quantile_q75(day_signed_ratio(Ret, Volume), 3), 20)`
  - score -0.38(train -0.38 valid +0.71):`cross_mean(cross_mean(cross_mean(day_signed_ratio(Ret, Volume), 20), 20), 20)`
  - score -0.55(train -0.55 valid +1.27):`cross_mean(day_signed_ratio(Ret, Volume), 20)`
  - score -0.55(train -0.55 valid +1.21):`cross_mean(cross_mean(day_signed_ratio(Ret, Volume), 3), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.41(knockout cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241)):`cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 20), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))`
- 增益 +0.41(window cross_reg_tvalue@30->60):`cross_reg_tvalue(day_sum(Volume), day_mean(in_delta(Volume, 30)), 60)`
- 增益 +0.19(window ts_argmin@20->10):`cs_first_high40(ts_argmin(cross_quantile_q25(cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241), 241), 10), cross_quantile_q25(signedpower(cs_first_high40(ts_argmin(cross_quantile_q25(signedpower(day_centroid(Volume)), 241), 20), day_centroid(Volume))), 241))`
- 增益 +0.12(window in_delta@30->15):`day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 15))`
