# 定位:种子 2074,P 组,第 2 轮(只含 train / valid)

快照:prods2074M1_I0_open_search, prods2074M2_I0_open_search, prods2074Pr1a_Ea, prods2074Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.55 | -1.18 | -1.55 | -1 | 20 | prods2074M1_I0_open_search | `pow_2(day_close(neg(Volume)))` |
| -1.69 | -1.69 | -1.05 | +1 | 5 | prods2074M2_I0_open_search | `ts_max(day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5)), 20)` |
| -1.89 | -1.89 | -0.59 | +1 | 5 | prods2074M2_I0_open_search | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)` |
| -1.91 | -1.91 | -0.45 | +1 | 5 | prods2074M2_I0_open_search | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)` |
| -1.93 | -1.63 | -1.93 | +1 | 5 | prods2074M1_I0_open_search | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` |
| -2.19 | -2.19 | -2.01 | +1 | 20 | prods2074M1_I0_open_search | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` |

## 共性:113 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.37 | 0.000 | 11 | -1.16 / -2.53 | `day_quantile_q25(Ret)` |
| +0.66 | 0.089 | 4 | -1.76 / -2.42 | `day_std(Ret)` |
| +0.57 | 0.058 | 11 | -1.89 / -2.46 | `cs_rank(day_std(Amt))` |
| +0.57 | 0.058 | 11 | -1.89 / -2.46 | `signedpower(cs_rank(day_std(Amt)))` |
| +0.54 | 0.062 | 6 | -1.89 / -2.43 | `cross_mean(day_close(neg(Volume)), 10)` |
| +0.47 | 0.175 | 8 | -1.97 / -2.43 | `div(ts_stddev(ts_decay_linear(day_at_min_ratio(Vwap), 40), 5), day_at_min_ratio(in_median(Vwap)))` |
| +0.45 | 0.087 | 17 | -2.02 / -2.47 | `day_std(Amt)` |
| +0.42 | 0.001 | 44 | -2.15 / -2.56 | `day_close(neg(Volume))` |
| +0.41 | 0.131 | 13 | -2.04 / -2.45 | `day_at_min_ratio(in_median(Vwap))` |
| +0.38 | 0.205 | 12 | -2.06 / -2.44 | `ts_stddev(ts_decay_linear(day_at_min_ratio(Vwap), 40), 5)` |
| +0.28 | 0.168 | 21 | -2.17 / -2.45 | `day_at_min_ratio(Vwap)` |
| +0.18 | 0.422 | 14 | -2.25 / -2.42 | `ts_decay_linear(day_at_min_ratio(Vwap), 40)` |
| -0.12 | 0.824 | 18 | -2.50 / -2.38 | `day_argmin(Amt)` |
| -0.12 | 0.698 | 11 | -2.51 / -2.39 | `pow_2_5(day_argmin(Amt))` |
| -0.44 | 0.827 | 5 | -2.82 / -2.38 | `cs_robust_z(day_close(neg(Volume)))` |
| -0.57 | 0.797 | 4 | -2.95 / -2.38 | `day_sum(Volume)` |
| -0.70 | 0.931 | 4 | -3.07 / -2.38 | `day_max(Amt)` |

## 拆解(13 次评估)

### head score -1.69:`ts_max(day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5))` | -3.01 | -3.01 | -2.75 | — | (子树本身) |
| swap | `Amt->Volume` | -1.01 | -0.85 | -1.01 | — | `ts_max(day_cov(Volume, nt_ts_cov(Open, nt_ts_delta(Volume, 60), 5)), 20)` |
| swap | `Open->Close` | -1.44 | -1.44 | -0.94 | — | `ts_max(day_cov(Amt, nt_ts_cov(Close, nt_ts_delta(Amt, 60), 5)), 20)` |
| window | `ts_max@20->10` | -2.85 | -2.85 | -1.70 | — | `ts_max(day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5)), 10)` |
| window | `ts_max@20->40` | -0.95 | -0.95 | -0.61 | — | `ts_max(day_cov(Amt, nt_ts_cov(Open, nt_ts_delta(Amt, 60), 5)), 40)` |

### head score -1.89:`ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(nt_ts_delta(Amt, 30), Amt)` | -3.18 | -2.82 | -3.18 | — | (子树本身) |
| swap | `Amt->Volume` | -1.61 | -1.46 | -1.61 | — | `ts_max(day_cov(nt_ts_delta(Volume, 30), Volume), 20)` |
| window | `ts_max@20->10` | -2.94 | -2.94 | -1.48 | — | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 10)` |
| window | `ts_max@20->40` | -0.50 | -0.50 | -0.30 | — | `ts_max(day_cov(nt_ts_delta(Amt, 30), Amt), 40)` |

### head score -1.91:`ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(nt_ts_delta(Amt, 15), Amt)` | -3.27 | -2.84 | -3.27 | — | (子树本身) |
| swap | `Amt->Volume` | -1.40 | -1.38 | -1.40 | — | `ts_max(day_cov(nt_ts_delta(Volume, 15), Volume), 20)` |
| window | `ts_max@20->10` | -3.10 | -3.10 | -1.30 | — | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 10)` |
| window | `ts_max@20->40` | -0.48 | -0.48 | -0.12 | — | `ts_max(day_cov(nt_ts_delta(Amt, 15), Amt), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_quantile_q25(Ret)` — enrichment,均值差 +1.37,p 0.000
2. `day_std(Ret)` — enrichment,均值差 +0.66,p 0.089
3. `cs_rank(day_std(Amt))` — enrichment,均值差 +0.57,p 0.058
4. `signedpower(cs_rank(day_std(Amt)))` — enrichment,均值差 +0.57,p 0.058
5. `cross_mean(day_close(neg(Volume)), 10)` — enrichment,均值差 +0.54,p 0.062
6. `day_std(Amt)` — enrichment,均值差 +0.45,p 0.087
7. `day_close(neg(Volume))` — enrichment,均值差 +0.42,p 0.001

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

## 比原 head 好的拆解变体(R 候选)

(没有)
