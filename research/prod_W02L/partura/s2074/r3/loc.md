# 定位:种子 2074,P 组,第 3 轮(只含 train / valid)

快照:prods2074M1_I0_open_search, prods2074M2_I0_open_search, prods2074M3_I0_open_search, prods2074Pr1a_Ea, prods2074Pr1b_Nb, prods2074Pr2a_Ea, prods2074Pr2b_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.55 | -1.18 | -1.55 | -1 | 20 | prods2074M1_I0_open_search | `pow_2(day_close(neg(Volume)))` |
| -1.69 | -1.69 | -1.05 | +1 | 5 | prods2074M2_I0_open_search | `ts_max(day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5)), 20)` |
| -1.89 | -1.89 | -0.59 | +1 | 5 | prods2074M2_I0_open_search | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` |
| -1.91 | -1.91 | -0.45 | +1 | 5 | prods2074M2_I0_open_search | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` |
| -1.93 | -1.63 | -1.93 | +1 | 5 | prods2074M1_I0_open_search | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` |
| -2.04 | -1.63 | -2.04 | -1 | 20 | prods2074M3_I0_open_search | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 3))))` |
| -2.19 | -2.19 | -2.01 | +1 | 20 | prods2074M1_I0_open_search | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` |
| -2.20 | -2.20 | -1.86 | +1 | 5 | prods2074M3_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 50)` |
| -2.37 | -1.54 | -2.37 | -1 | 20 | prods2074M3_I0_open_search | `day_quantile_q75(cross_sum(log(nt_ts_med(Low, 5)), 3))` |

## 共性:197 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.93 | 0.001 | 4 | -0.53 / -2.46 | `day_close(Ret)` |
| +1.93 | 0.001 | 4 | -0.53 / -2.46 | `cross_delay(day_close(Ret), 1)` |
| +1.78 | 0.000 | 7 | -0.70 / -2.48 | `day_topw_mean(Amt, Amt)` |
| +1.78 | 0.000 | 7 | -0.70 / -2.48 | `cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret))` |
| +1.76 | 0.000 | 13 | -0.77 / -2.53 | `cross_delay(day_sum(Ret), 1)` |
| +1.37 | 0.004 | 6 | -1.09 / -2.46 | `day_topw_mean(Amt, Ret)` |
| +1.30 | 0.000 | 17 | -1.23 / -2.53 | `day_sum(Ret)` |
| +1.09 | 0.001 | 9 | -1.38 / -2.47 | `day_topw_mean(Amt, Low)` |
| +1.05 | 0.000 | 61 | -1.69 / -2.74 | `day_quantile_q25(Ret)` |
| +1.04 | 0.004 | 7 | -1.41 / -2.45 | `cs_regres(day_topw_mean(Amt, Low), day_quantile_q25(Ret))` |
| +0.56 | 0.066 | 11 | -1.89 / -2.45 | `signedpower(cs_rank(day_std(Amt)))` |
| +0.56 | 0.066 | 11 | -1.89 / -2.45 | `cs_rank(day_std(Amt))` |
| +0.55 | 0.070 | 6 | -1.89 / -2.43 | `cross_mean(day_close(neg(Volume)), 10)` |
| +0.47 | 0.164 | 8 | -1.97 / -2.44 | `div(ts_stddev(ts_decay_linear(day_at_min_ratio(Vwap), 40), 5), day_at_min_ratio(in_median(Vwap)))` |
| +0.40 | 0.107 | 18 | -2.05 / -2.45 | `day_std(Amt)` |
| +0.40 | 0.124 | 13 | -2.04 / -2.44 | `day_at_min_ratio(in_median(Vwap))` |
| +0.38 | 0.186 | 12 | -2.06 / -2.44 | `ts_stddev(ts_decay_linear(day_at_min_ratio(Vwap), 40), 5)` |
| +0.35 | 0.004 | 44 | -2.15 / -2.49 | `day_close(neg(Volume))` |
| +0.27 | 0.170 | 21 | -2.17 / -2.44 | `day_at_min_ratio(Vwap)` |
| +0.18 | 0.377 | 14 | -2.25 / -2.43 | `ts_decay_linear(day_at_min_ratio(Vwap), 40)` |

## 拆解(10 次评估)

### head score -2.04:`day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 3))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `High->Low` | -2.00 | -1.67 | -2.00 | — | `day_first(in_sum(in_relative_distance_m(nt_ts_med(Low, 3))))` |
| window | `nt_ts_med@3->2` | -2.00 | -1.67 | -2.00 | — | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 2))))` |
| window | `nt_ts_med@3->6` | -2.03 | -1.67 | -2.03 | — | `day_first(in_sum(in_relative_distance_m(nt_ts_med(High, 6))))` |

### head score -2.20:`ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(nt_ts_med(Volume, 3))` | -2.98 | -2.90 | -2.98 | — | (子树本身) |
| swap | `Volume->Amt` | -2.22 | -2.22 | -1.81 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Amt, 3)), 50)` |
| window | `ts_quantile_q75@50->25` | -2.54 | -2.54 | -1.99 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 25)` |
| window | `ts_quantile_q75@50->100` | -1.70 | -1.59 | -1.70 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_med(Volume, 3)), 100)` |

### head score -2.37:`day_quantile_q75(cross_sum(log(nt_ts_med(Low, 5)), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Low->High` | -2.33 | -1.54 | -2.33 | — | `day_quantile_q75(cross_sum(log(nt_ts_med(High, 5)), 3))` |
| window | `cross_sum@3->2` | -2.33 | -1.55 | -2.33 | — | `day_quantile_q75(cross_sum(log(nt_ts_med(Low, 5)), 2))` |
| window | `cross_sum@3->6` | -2.34 | -1.55 | -2.34 | — | `day_quantile_q75(cross_sum(log(nt_ts_med(Low, 5)), 6))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_close(Ret)` — enrichment,均值差 +1.93,p 0.001
2. `cross_delay(day_close(Ret), 1)` — enrichment,均值差 +1.93,p 0.001
3. `day_topw_mean(Amt, Amt)` — enrichment,均值差 +1.78,p 0.000
4. `cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret))` — enrichment,均值差 +1.78,p 0.000
5. `cross_delay(day_sum(Ret), 1)` — enrichment,均值差 +1.76,p 0.000
6. `day_topw_mean(Amt, Ret)` — enrichment,均值差 +1.37,p 0.004
7. `day_sum(Ret)` — enrichment,均值差 +1.30,p 0.000
8. `day_topw_mean(Amt, Low)` — enrichment,均值差 +1.09,p 0.001
9. `day_quantile_q25(Ret)` — enrichment,均值差 +1.05,p 0.000
10. `cs_regres(day_topw_mean(Amt, Low), day_quantile_q25(Ret))` — enrichment,均值差 +1.04,p 0.004
11. `signedpower(cs_rank(day_std(Amt)))` — enrichment,均值差 +0.56,p 0.066
12. `cs_rank(day_std(Amt))` — enrichment,均值差 +0.56,p 0.066
13. `cross_mean(day_close(neg(Volume)), 10)` — enrichment,均值差 +0.55,p 0.070
14. `day_close(neg(Volume))` — enrichment,均值差 +0.35,p 0.004

## 本组之前各轮的任务

- `prods2074Pr1a_Ea`:核心 `day_close(neg(Volume))`;评分 101,过线 0,入 heads 0;采样计数 {'c05_no_core': 2089, 'c05_skeleton': 1087, 'c05_periphery_seen': 5}
  - score -0.20(train +0.23 valid -0.20):`cross_regbeta(day_close(neg(Volume)), day_quantile_q25(Ret), 60)`
  - score -0.33(train -0.31 valid -0.33):`cross_regbeta(day_close(neg(Volume)), cross_regbeta(day_close(neg(Volume)), day_quantile_q25(Ret), 60), 241)`
  - score -0.71(train -0.70 valid -0.71):`cross_regbeta(day_close(neg(Volume)), day_quantile_q25(Ret), 5)`
  - score -0.83(train -0.79 valid -0.83):`cross_regbeta(day_close(neg(Volume)), day_quantile_q25(Low), 60)`
  - score -0.88(train -0.18 valid -0.88):`cross_regbeta(day_close(neg(Volume)), day_quantile_q25(Ret), 30)`
- `prods2074Pr1b_Nb`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.66(train -0.66 valid -0.17):`cross_reg_fvalue(signedpower(cs_rank(day_std(Amt))), pow_2_5(cross_reg_fvalue(signedpower(cs_rank(day_std(Amt))), div(cross_reg_fvalue(signedpower(cs_rank(day_std(in_relative_distance_p(Vwap)))), pow_2_5(day_at_min_ratio(Vwap)), 60), day_at_min_ratio(in_relative_distance_p(Vwap))), 60)), 60)`
  - score -0.73(train -0.73 valid -0.45):`cross_reg_fvalue(signedpower(cs_rank(day_std(Amt))), pow_2_5(cross_reg_fvalue(signedpower(cs_rank(day_std(Amt))), div(ts_stddev(ts_decay_linear(day_at_min_ratio(Vwap), 40), 5), day_at_min_ratio(in_median(Vwap))), 60)), 60)`
  - score -0.73(train -0.73 valid -0.45):`cross_reg_fvalue(signedpower(cs_rank(cs_robust_z(day_std(Amt)))), pow_2_5(cross_reg_fvalue(signedpower(cs_rank(cs_robust_z(day_std(Amt)))), div(ts_stddev(ts_decay_linear(day_at_min_ratio(Vwap), 40), 5), day_at_min_ratio(in_median(Vwap))), 60)), 60)`
  - score -0.95(train -0.95 valid -0.74):`cross_reg_fvalue(signedpower(cs_rank(day_std(Amt))), pow_2_5(day_argmin(in_index(Vwap))), 60)`
  - score -1.34(train -1.33 valid -1.34):`cross_reg_fvalue(signedpower(cs_rank(day_std(Amt))), pow_2_5(day_argmin(Amt)), 5)`
- `prods2074Pr2a_Ea`:核心 `day_quantile_q25(Ret)`;评分 92,过线 0,入 heads 0;采样计数 {'c05_no_core': 1442, 'c05_skeleton': 716}
  - score +0.11(train +0.51 valid +0.11):`cross_regbeta(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), cross_delay(day_sum(Ret), 1), 30)`
  - score +0.10(train +0.71 valid +0.10):`cross_regbeta(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), cross_delay(day_sum(Ret), 1), 60)`
  - score +0.10(train +0.71 valid +0.10):`cross_regbeta(cs_regres(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), day_quantile_q25(Ret)), cross_delay(day_sum(Ret), 1), 60)`
  - score +0.00(train +0.53 valid +0.00):`cross_regbeta(cs_regres(day_topw_mean(Amt, Ret), day_quantile_q25(Ret)), cross_delay(day_sum(Ret), 1), 60)`
  - score -0.15(train -0.15 valid +0.01):`cross_regbeta(cs_regres(day_topw_mean(Amt, Amt), day_quantile_q25(Ret)), cross_delay(day_sum(Ret), 1), 15)`
- `prods2074Pr2b_I0_open_search`:核心 `—`;评分 58,过线 0,入 heads 0;采样计数 {'c05_skeleton': 21}
  - score -1.88(train -0.81 valid -1.88):`day_min(cross_corr(Open, Amt, 30))`
  - score -2.16(train -2.16 valid -2.03):`day_min(cross_corr(Open, Amt, 5))`
  - score -2.50(train -1.57 valid -2.50):`day_min(cross_corr(Open, Amt, 10))`
  - score -2.69(train -2.69 valid -2.58):`day_es_ratio_lo(Open)`
  - score -2.73(train -2.73 valid -2.68):`day_es_ratio_lo(High)`

## 比原 head 好的拆解变体(R 候选)

(没有)
