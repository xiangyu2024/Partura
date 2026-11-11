# 定位:种子 2034,P 组,第 3 轮(只含 train / valid)

快照:prods2034M1_I0_open_search, prods2034M2_I0_open_search, prods2034M3_I0_open_search, prods2034Pr1a_Na, prods2034Pr1b_Nb, prods2034Pr2a_Ea, prods2034Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(18 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.22 | +1.22 | +1.22 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| +1.13 | +1.13 | +1.49 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| +0.99 | +0.99 | +1.05 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241))` |
| +0.98 | +1.46 | +0.98 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241))` |
| +0.64 | +0.64 | +0.85 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(div(cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume)), day_sum(Vwap)), 241)), day_sum(Volume)), day_sum(Vwap)), 241))` |
| +0.59 | +0.92 | +0.59 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Ret), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| +0.57 | +0.82 | +0.57 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Ret), 30), cs_last_low40(div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume)), day_sum(Vwap)), 241))` |
| +0.56 | +0.85 | +0.56 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_autocorr_n1(Ret), cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_autocorr_n1(Ret), day_sum(Vwap)), 241))), 241))` |
| +0.55 | +0.77 | +0.55 | +1 | 5 | prods2034Pr2a_Ea | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cs_stddev_full(ts_argmin(day_at_max_ratio(Vwap), 40)), cs_last_low40(day_autocorr_n1(Vwap), day_sum(Vwap)), 241))` |
| -0.38 | -0.38 | +0.08 | +1 | 20 | prods2034M1_I0_open_search | `cs_bucket_zscore(ts_std(log(ts_decay_linear(day_sum(Amt), 50)), 10), cross_mean(day_sum(Amt), 30))` |
| -0.80 | -0.80 | -0.66 | +1 | 0 | prods2034M1_I0_open_search | `ts_decay_linear(ts_max(day_sum(Amt), 50), 50)` |
| -1.10 | -0.65 | -1.10 | -1 | 20 | prods2034M3_I0_open_search | `mul(-1, ts_corr(cs_rank(day_first(Open)), cs_rank(day_sum(Volume)), 10))` |
| -1.34 | -1.17 | -1.34 | -1 | 5 | prods2034M1_I0_open_search | `ts_decay_linear(day_sum(Volume), 5)` |
| -1.34 | -1.19 | -1.34 | -1 | 5 | prods2034M3_I0_open_search | `pow_2(cs_rank(day_sum(Volume)))` |
| -1.55 | -1.36 | -1.55 | -1 | 0 | prods2034M3_I0_open_search | `ts_quantile_q75(pow_2(cs_rank(day_sum(Volume))), 50)` |
| -1.58 | -1.58 | -1.55 | +1 | 20 | prods2034M2_I0_open_search | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 20)), cross_mean(day_sum(Volume), 60)), 20)` |
| -1.63 | -1.23 | -1.63 | +1 | 20 | prods2034M2_I0_open_search | `cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), cross_mean(day_sum(Volume), 60)), 40)` |
| -1.88 | -1.88 | -1.28 | +1 | 5 | prods2034M2_I0_open_search | `cross_stddev(div(day_sum(in_topk_masked(Volume, Volume, 5)), day_sum(Volume)), 20)` |

## 共性:287 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.75 | 0.000 | 6 | +0.83 / -1.92 | `cs_last_low40(day_sum(Vwap), day_sum(Vwap))` |
| +2.73 | 0.000 | 30 | +0.59 / -2.15 | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` |
| +2.48 | 0.000 | 25 | +0.41 / -2.08 | `day_sum(Vwap)` |
| +2.44 | 0.000 | 24 | +0.37 / -2.06 | `day_quantile_q75(Low)` |
| +2.40 | 0.000 | 23 | +0.34 / -2.05 | `cross_rank(day_quantile_q75(Low), 30)` |
| +2.35 | 0.000 | 6 | +0.44 / -1.91 | `cs_last_low40(day_autocorr_n1(Ret), day_sum(Vwap))` |
| +2.35 | 0.000 | 6 | +0.44 / -1.91 | `day_autocorr_n1(Ret)` |
| +2.07 | 0.001 | 6 | +0.17 / -1.90 | `cs_last_low40(div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume)), day_sum(Vwap))` |
| +1.20 | 0.000 | 64 | -0.93 / -2.13 | `day_sum(in_topk_masked(Ret, Volume, 20))` |
| +0.94 | 0.011 | 14 | -0.97 / -1.91 | `div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume))` |
| +0.87 | 0.000 | 19 | -1.05 / -1.92 | `cross_mean(log(day_sum(Amt)), 120)` |
| +0.78 | 0.035 | 4 | -1.09 / -1.87 | `cross_mean(div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume)), 30)` |
| +0.76 | 0.001 | 25 | -1.16 / -1.93 | `cross_mean(day_sum(Amt), 120)` |
| +0.75 | 0.000 | 30 | -1.19 / -1.94 | `ts_max(day_sum(Amt), 50)` |
| +0.75 | 0.047 | 4 | -1.13 / -1.87 | `cross_max(log(day_sum(Amt)), 25)` |
| +0.74 | 0.001 | 24 | -1.18 / -1.92 | `div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120))` |
| +0.70 | 0.011 | 17 | -1.20 / -1.90 | `ts_max(log(day_sum(Amt)), 50)` |
| +0.68 | 0.003 | 22 | -1.23 / -1.91 | `ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25)` |
| +0.67 | 0.044 | 17 | -1.23 / -1.90 | `sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False)))` |
| +0.64 | 0.101 | 7 | -1.23 / -1.88 | `cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120))` |

## 拆解(47 次评估)

### head score +1.22:`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241)` | -1.46 | -1.02 | -1.46 | — | (子树本身) |
| sufficiency | `day_sum(in_topk_masked(Ret, Volume, 20))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `cross_rank(day_quantile_q75(Low), 30)` | — | — | — | — | 门槛废品 |
| knockout | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | +1.17 | +1.17 | +1.17 | +0.05 | `cs_first_high20(day_sum(in_topk_masked(Ret, Volume, 20)), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| knockout | `cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241)` | -1.52 | -1.22 | -1.52 | +2.74 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_rank(day_quantile_q75(Low), 30))` |
| knockout | `cross_rank(day_quantile_q75(Low), 30)` | +0.55 | +1.24 | +0.55 | +0.67 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(day_quantile_q75(Low), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| knockout | `cs_last_low40(day_sum(Vwap), day_sum(Vwap))` | -0.91 | -0.83 | -0.91 | +2.13 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), day_sum(Vwap), 241))` |
| swap | `Volume->Amt` | +1.68 | +1.68 | +1.76 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Amt, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| swap | `Low->High` | +1.20 | +1.20 | +1.21 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(High), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| window | `cross_regbeta@241->120` | +0.73 | +1.01 | +0.73 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 120))` |
| window | `cross_regbeta@241->482` | +1.17 | +1.17 | +1.28 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 482))` |

### head score +1.13:`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241)` | -1.32 | -1.32 | -0.77 | — | (子树本身) |
| sufficiency | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `cross_rank(cross_rank(day_quantile_q75(Low), 30), 30)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_sum(in_topk_masked(Ret, Volume, 20))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| knockout | `cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241)` | -1.50 | -1.17 | -1.50 | +2.63 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_rank(cross_rank(day_quantile_q75(Low), 30), 30))` |
| knockout | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | +1.10 | +1.10 | +1.45 | +0.03 | `cs_first_high20(day_sum(in_topk_masked(Ret, Volume, 20)), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| knockout | `cross_rank(cross_rank(day_quantile_q75(Low), 30), 30)` | +1.22 | +1.22 | +1.22 | -0.09 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| swap | `Volume->Amt` | +1.57 | +1.57 | +2.00 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Amt, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| swap | `Low->High` | +1.11 | +1.11 | +1.43 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(High), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))` |
| window | `cross_regbeta@241->120` | +0.82 | +0.82 | +0.85 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 120))` |
| window | `cross_regbeta@241->482` | +1.13 | +1.13 | +1.53 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 482))` |

### head score +0.99:`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241)` | -1.62 | -1.62 | -1.00 | — | (子树本身) |
| sufficiency | `day_sum(in_topk_masked(Ret, Volume, 20))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `cross_rank(day_quantile_q75(Low), 30)` | — | — | — | — | 门槛废品 |
| knockout | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | +0.85 | +0.85 | +1.01 | +0.14 | `cs_first_high20(day_sum(in_topk_masked(Ret, Volume, 20)), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241))` |
| knockout | `cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241)` | -1.52 | -1.22 | -1.52 | +2.51 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_rank(day_quantile_q75(Low), 30))` |
| knockout | `cross_rank(day_quantile_q75(Low), 30)` | +0.44 | +0.99 | +0.44 | +0.55 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(day_quantile_q75(Low), cs_last_low40(day_sum(Low), day_sum(Low)), 241))` |
| knockout | `cs_last_low40(day_sum(Low), day_sum(Low))` | -0.94 | -0.94 | -0.87 | +1.93 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), day_sum(Low), 241))` |
| swap | `Volume->Amt` | +1.47 | +1.47 | +1.66 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Amt, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241))` |
| swap | `Low->High` | +0.86 | +0.86 | +1.03 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(High), 30), cs_last_low40(day_sum(High), day_sum(High)), 241))` |
| window | `cross_regbeta@241->120` | +0.42 | +0.42 | +0.72 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 120))` |
| window | `cross_regbeta@241->482` | +0.90 | +1.01 | +0.90 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 482))` |

### head score +0.98:`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241)` | -2.29 | -1.87 | -2.29 | — | (子树本身) |
| sufficiency | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| sufficiency | `cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20)))` | -1.36 | -1.22 | -1.36 | — | (子树本身) |
| sufficiency | `day_sum(in_topk_masked(Ret, Volume, 20))` | -1.37 | -1.22 | -1.37 | — | (子树本身) |
| knockout | `cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241)` | -1.52 | -1.22 | -1.52 | +2.50 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_rank(day_quantile_q75(Low), 30))` |
| knockout | `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` | +0.81 | +1.37 | +0.81 | +0.17 | `cs_first_high20(day_sum(in_topk_masked(Ret, Volume, 20)), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241))` |
| knockout | `cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20)))` | -1.34 | -1.34 | -1.24 | +2.32 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), day_sum(in_topk_masked(Ret, Volume, 20)), 241))` |
| knockout | `cross_rank(day_quantile_q75(Low), 30)` | -0.31 | +0.34 | -0.31 | +1.28 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(day_quantile_q75(Low), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241))` |
| swap | `Volume->Amt` | +0.88 | +0.88 | +1.32 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Amt, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Amt, 20)), day_sum(in_topk_masked(Ret, Amt, 20))), 241))` |
| swap | `Low->High` | +0.80 | +1.37 | +0.80 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(High), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 241))` |
| window | `cross_regbeta@241->120` | +0.58 | +1.06 | +0.58 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 120))` |
| window | `cross_regbeta@241->482` | +1.21 | +1.43 | +1.21 | — | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low40(day_sum(Vwap), day_sum(Vwap))` — enrichment,均值差 +2.75,p 0.000
2. `signedpower(day_sum(in_topk_masked(Ret, Volume, 20)))` — enrichment,均值差 +2.73,p 0.000
3. `day_sum(Vwap)` — enrichment,均值差 +2.48,p 0.000
4. `day_quantile_q75(Low)` — enrichment,均值差 +2.44,p 0.000
5. `cross_rank(day_quantile_q75(Low), 30)` — enrichment,均值差 +2.40,p 0.000
6. `cs_last_low40(day_autocorr_n1(Ret), day_sum(Vwap))` — enrichment,均值差 +2.35,p 0.000
7. `day_autocorr_n1(Ret)` — enrichment,均值差 +2.35,p 0.000
8. `cs_last_low40(div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume)), day_sum(Vwap))` — enrichment,均值差 +2.07,p 0.001
9. `day_sum(in_topk_masked(Ret, Volume, 20))` — enrichment,均值差 +1.20,p 0.000
10. `div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume))` — enrichment,均值差 +0.94,p 0.011
11. `cross_mean(log(day_sum(Amt)), 120)` — enrichment,均值差 +0.87,p 0.000
12. `cross_mean(div(sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False))), day_sum(Volume)), 30)` — enrichment,均值差 +0.78,p 0.035
13. `cross_mean(day_sum(Amt), 120)` — enrichment,均值差 +0.76,p 0.001
14. `ts_max(day_sum(Amt), 50)` — enrichment,均值差 +0.75,p 0.000
15. `cross_max(log(day_sum(Amt)), 25)` — enrichment,均值差 +0.75,p 0.047
16. `div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120))` — enrichment,均值差 +0.74,p 0.001
17. `ts_max(log(day_sum(Amt)), 50)` — enrichment,均值差 +0.70,p 0.011
18. `ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25)` — enrichment,均值差 +0.68,p 0.003
19. `sub(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20, False)))` — enrichment,均值差 +0.67,p 0.044
20. `day_sum(in_topk_masked(Volume, in_topk_masked(Volume, Ret, 5), 5))` — enrichment,均值差 +0.62,p 0.042
21. `log(day_sum(Amt))` — enrichment,均值差 +0.61,p 0.000
22. `cross_delay(log(day_sum(Amt)), 1)` — enrichment,均值差 +0.54,p 0.041
23. `day_sum(Amt)` — enrichment,均值差 +0.52,p 0.000
24. `cross_zscore(log(day_sum(Amt)), 60)` — enrichment,均值差 +0.49,p 0.027
25. `day_sum(in_topk_masked(Ret, Volume, 20, False))` — enrichment,均值差 +0.48,p 0.092
26. `cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1)` — enrichment,均值差 +0.48,p 0.072
27. `div(day_sum(in_topk_masked(Volume, Ret, 5)), cross_mean(abs_(day_sum(Ret)), 60))` — enrichment,均值差 +0.48,p 0.050

## 本组之前各轮的任务

- `prods2034Pr1a_Na`:核心 `—`;评分 89,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.01(train +0.05 valid +0.01):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 20), cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120)))`
  - score -0.02(train -0.02 valid +0.17):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120)))`
  - score -0.04(train -0.04 valid +0.13):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(log(day_sum(Amt))), 120)))`
  - score -0.34(train +0.18 valid -0.34):`cs_regres(ts_max(log(day_sum(Amt)), 50), cross_mean(log(day_sum(Amt)), 120))`
  - score -0.39(train -0.39 valid +0.09):`cs_bucket_zscore(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), cs_regres(ts_max(ts_decay_linear(div(ts_max(day_sum(Amt), 50), cross_mean(day_sum(Amt), 120)), 25), 50), cross_mean(log(day_sum(Amt)), 120)))`
- `prods2034Pr1b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 12}
  - score -0.21(train -0.21 valid +0.50):`cross_corr(cross_delay(day_sum(Amt), 1), day_sum(Ret), 241)`
  - score -0.49(train -0.41 valid -0.49):`cross_corr(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 120)`
  - score -0.59(train -0.59 valid +0.60):`cross_regbeta(cross_zscore(log(day_sum(Amt)), 60), day_wmean(Ret, Amt), 60)`
  - score -0.63(train -0.63 valid +0.05):`cross_regbeta(cross_delay(cross_zscore(log(day_sum(Amt)), 60), 1), day_sum(Ret), 120)`
  - score -0.77(train -0.70 valid -0.77):`cross_corr(cross_delay(log(day_sum(Amt)), 1), day_sum(Amt), 120)`
- `prods2034Pr2a_Ea`:核心 `day_sum(in_topk_masked(Ret, Volume, 20))`;评分 103,过线 21,入 heads 9;采样计数 {'c05_periphery_seen': 6, 'c05_no_core': 1289, 'c05_skeleton': 685}
  - score +1.22(train +1.22 valid +1.22):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`
  - score +1.22(train +1.26 valid +1.22):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_quantile_q75(Low), day_sum(Vwap)), 241))`
  - score +1.13(train +1.13 valid +1.49):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`
  - score +1.11(train +1.49 valid +1.11):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Volume), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`
  - score +1.03(train +1.03 valid +1.51):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 10), cs_last_low40(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), day_sum(Vwap)), 241))`
- `prods2034Pr2b_Nb`:核心 `—`;评分 89,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -1.04(train -0.70 valid -1.04):`cross_quantile_q50(div(day_sum(in_topk_masked(Volume, Ret, 5)), day_sum(Ret)), 60)`
  - score -1.04(train -1.04 valid -0.96):`cross_quantile_q50(div(day_sum(in_topk_masked(Volume, Ret, 5)), cross_mean(abs_(day_sum(Ret)), 60)), 60)`
  - score -1.08(train -1.02 valid -1.08):`cross_mean(div(div(day_sum(in_topk_masked(Volume, Ret, 5)), cross_mean(abs_(day_sum(Ret)), 60)), cross_mean(abs_(day_sum(Ret)), 60)), 20)`
  - score -1.14(train -1.14 valid -0.92):`cross_mean(div(day_sum(in_topk_masked(Volume, Ret, 5)), cross_mean(abs_(cross_mean(abs_(day_sum(Ret)), 60)), 60)), 20)`
  - score -1.14(train -1.14 valid -0.98):`cross_quantile_q50(div(day_sum(in_topk_masked(Volume, Ret, 5)), cross_mean(abs_(day_sum(in_topk_masked(Volume, in_topk_masked(Volume, in_topk_masked(Volume, Ret, 5), 5), 5))), 60)), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.46(swap Volume->Amt):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Amt, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`
- 增益 +0.44(swap Volume->Amt):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Amt, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))`
- 增益 +0.23(window cross_regbeta@241->482):`cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(in_topk_masked(Ret, Volume, 20))), 482))`
