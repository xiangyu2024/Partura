# 定位:种子 2071,P 组,第 3 轮(只含 train / valid)

快照:prods2071M1_I0_open_search, prods2071M2_I0_open_search, prods2071M3_I0_open_search, prods2071Pr1a_Ea, prods2071Pr1b_Nb, prods2071Pr2a_Ea, prods2071Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.77 | -0.19 | -0.77 | -1 | 20 | prods2071M2_I0_open_search | `day_mean(pow_2(nt_cs_rank(Ret)))` |
| -0.82 | -0.61 | -0.82 | -1 | 5 | prods2071M2_I0_open_search | `day_median(pow_2(nt_cs_rank(Ret)))` |
| -1.64 | -1.62 | -1.64 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret)), 20)` |
| -1.68 | -1.68 | -1.51 | +1 | 20 | prods2071M2_I0_open_search | `pow_2(pow_2(day_q_stat_std(nt_cs_rank(High))))` |
| -1.69 | -1.69 | -1.03 | +1 | 20 | prods2071M3_I0_open_search | `day_max(signedpower(cross_argmax(Vwap, 15)))` |
| -1.72 | -1.71 | -1.72 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| -1.77 | -1.77 | -1.66 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 20)` |
| -2.09 | -2.09 | -1.41 | +1 | 20 | prods2071M3_I0_open_search | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 10)` |
| -2.35 | -2.35 | -1.00 | -1 | 20 | prods2071M3_I0_open_search | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Vwap, 30))), 20)` |

## 共性:241 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.05 | 0.002 | 4 | -0.03 / -2.08 | `cross_max(abs_(abs_(day_corr(Volume, Ret))), 241)` |
| +1.92 | 0.000 | 6 | -0.16 / -2.09 | `ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)` |
| +1.92 | 0.000 | 6 | -0.16 / -2.09 | `sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20))` |
| +1.91 | 0.000 | 8 | -0.20 / -2.10 | `abs_(abs_(day_corr(Volume, Ret)))` |
| +1.86 | 0.000 | 13 | -0.28 / -2.14 | `cross_max(abs_(day_corr(Volume, Ret)), 241)` |
| +1.86 | 0.003 | 4 | -0.21 / -2.07 | `div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))` |
| +1.46 | 0.000 | 11 | -0.65 / -2.11 | `sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open)))` |
| +1.45 | 0.001 | 8 | -0.64 / -2.09 | `div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open))` |
| +1.45 | 0.016 | 4 | -0.61 / -2.07 | `cross_max(ts_mean(abs_(day_corr(Volume, Ret)), 5), 241)` |
| +1.13 | 0.066 | 5 | -0.94 / -2.06 | `ts_mean(abs_(day_corr(Volume, Ret)), 1)` |
| +0.92 | 0.001 | 16 | -1.19 / -2.10 | `cross_argmax(abs_(sub(day_close(Close), day_open(Open))), 120)` |
| +0.79 | 0.001 | 19 | -1.31 / -2.10 | `abs_(sub(day_close(Close), day_open(Open)))` |
| +0.74 | 0.001 | 23 | -1.38 / -2.11 | `sub(day_close(Close), day_open(Open))` |
| +0.66 | 0.023 | 10 | -1.41 / -2.07 | `ts_mean(abs_(day_corr(Volume, Ret)), 5)` |
| +0.65 | 0.103 | 4 | -1.40 / -2.05 | `sub(cross_argmax(day_sum(Amt), 120), cross_argmax(abs_(sub(day_close(Close), day_open(Open))), 120))` |
| +0.63 | 0.047 | 9 | -1.43 / -2.07 | `cross_argmax(sub(day_max(High), day_min(Low)), 120)` |
| +0.61 | 0.002 | 30 | -1.51 / -2.12 | `day_close(Close)` |
| +0.60 | 0.001 | 58 | -1.58 / -2.19 | `abs_(day_corr(Volume, Ret))` |
| +0.58 | 0.014 | 17 | -1.50 / -2.08 | `cross_argmax(day_sum(Amt), 120)` |
| +0.56 | 0.003 | 59 | -1.62 / -2.18 | `day_corr(Volume, Ret)` |

## 拆解(24 次评估)

### head score -1.69:`day_max(signedpower(cross_argmax(Vwap, 15)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | — | — | — | — | `day_max(signedpower(cross_argmax(Close, 15)))` |
| window | `cross_argmax@15->7` | — | — | — | — | `day_max(signedpower(cross_argmax(Vwap, 7)))` |
| window | `cross_argmax@15->30` | — | — | — | — | `day_max(signedpower(cross_argmax(Vwap, 30)))` |

### head score -2.09:`ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume))` | -1.67 | -1.20 | -1.67 | — | (子树本身) |
| sufficiency | `day_close(cross_argmax(Vwap, 60))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_close(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_kurt(Volume)` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| knockout | `cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume))` | -2.88 | -2.88 | -1.36 | +0.78 | `ts_regbeta(day_kurt(Volume), day_close(cross_argmax(Vwap, 60)), 10)` |
| knockout | `mul(-5, day_close(Volume))` | -2.09 | -2.09 | -1.39 | -0.00 | `ts_regbeta(cs_regres(day_close(Volume), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 10)` |
| swap | `Volume->Amt` | -2.24 | -2.24 | -1.48 | — | `ts_regbeta(cs_regres(mul(-5, day_close(Amt)), day_kurt(Amt)), day_close(cross_argmax(Vwap, 60)), 10)` |
| swap | `Vwap->Close` | -2.25 | -2.25 | -1.62 | — | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Close, 60)), 10)` |
| window | `ts_regbeta@10->5` | -3.45 | -3.45 | -2.41 | — | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 5)` |
| window | `ts_regbeta@10->20` | -1.38 | -1.37 | -1.38 | — | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 20)` |

### head score -2.35:`ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Vwap, 30))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Vwap, 30)))` | -2.81 | -2.62 | -2.81 | — | (子树本身) |
| sufficiency | `ts_std(signedpower(day_var(Close)), 5)` | -2.39 | -1.55 | -2.39 | — | (子树本身) |
| sufficiency | `signedpower(day_var(Close))` | -2.24 | -1.52 | -2.24 | — | (子树本身) |
| sufficiency | `day_quantile_q25(cross_argmax(Vwap, 30))` | — | — | — | — | 门槛废品 |
| knockout | `add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Vwap, 30)))` | -1.88 | -1.51 | -1.88 | -0.47 | `ts_autocorr_s1(ts_std(signedpower(day_var(Close)), 5), 20)` |
| knockout | `ts_std(signedpower(day_var(Close)), 5)` | -2.81 | -1.77 | -2.81 | +0.46 | `ts_autocorr_s1(add(signedpower(day_var(Close)), day_quantile_q25(cross_argmax(Vwap, 30))), 20)` |
| knockout | `signedpower(day_var(Close))` | -2.49 | -2.49 | -1.28 | +0.14 | `ts_autocorr_s1(add(ts_std(day_var(Close), 5), day_quantile_q25(cross_argmax(Vwap, 30))), 20)` |
| swap | `Close->Vwap` | -2.37 | -2.37 | -0.84 | — | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Vwap)), 5), day_quantile_q25(cross_argmax(Vwap, 30))), 20)` |
| swap | `Vwap->Close` | -1.99 | -1.99 | -1.01 | — | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Close, 30))), 20)` |
| window | `ts_autocorr_s1@20->10` | -2.60 | -2.60 | -0.93 | — | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Vwap, 30))), 10)` |
| window | `ts_autocorr_s1@20->40` | -2.13 | -2.09 | -2.13 | — | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Vwap, 30))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_max(abs_(abs_(day_corr(Volume, Ret))), 241)` — enrichment,均值差 +2.05,p 0.002
2. `ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)` — enrichment,均值差 +1.92,p 0.000
3. `sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20))` — enrichment,均值差 +1.92,p 0.000
4. `abs_(abs_(day_corr(Volume, Ret)))` — enrichment,均值差 +1.91,p 0.000
5. `cross_max(abs_(day_corr(Volume, Ret)), 241)` — enrichment,均值差 +1.86,p 0.000
6. `div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))` — enrichment,均值差 +1.86,p 0.003
7. `sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open)))` — enrichment,均值差 +1.46,p 0.000
8. `div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open))` — enrichment,均值差 +1.45,p 0.001
9. `cross_max(ts_mean(abs_(day_corr(Volume, Ret)), 5), 241)` — enrichment,均值差 +1.45,p 0.016
10. `ts_mean(abs_(day_corr(Volume, Ret)), 1)` — enrichment,均值差 +1.13,p 0.066
11. `cross_argmax(abs_(sub(day_close(Close), day_open(Open))), 120)` — enrichment,均值差 +0.92,p 0.001
12. `abs_(sub(day_close(Close), day_open(Open)))` — enrichment,均值差 +0.79,p 0.001
13. `sub(day_close(Close), day_open(Open))` — enrichment,均值差 +0.74,p 0.001
14. `ts_mean(abs_(day_corr(Volume, Ret)), 5)` — enrichment,均值差 +0.66,p 0.023
15. `cross_argmax(sub(day_max(High), day_min(Low)), 120)` — enrichment,均值差 +0.63,p 0.047
16. `day_close(Close)` — enrichment,均值差 +0.61,p 0.002
17. `abs_(day_corr(Volume, Ret))` — enrichment,均值差 +0.60,p 0.001
18. `cross_argmax(day_sum(Amt), 120)` — enrichment,均值差 +0.58,p 0.014
19. `day_corr(Volume, Ret)` — enrichment,均值差 +0.56,p 0.003
20. `day_sum(Amt)` — enrichment,均值差 +0.50,p 0.010

## 本组之前各轮的任务

- `prods2071Pr1a_Ea`:核心 `div(sub(day_max(High), day_min(Low)), day_open(Open))`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 1587, 'c05_skeleton': 780}
  - score -0.06(train +0.04 valid -0.06):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), add(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))), 20)), add(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))), 5)`
  - score -0.06(train -0.06 valid -0.04):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open)), 5)`
  - score -0.07(train -0.07 valid -0.03):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)))), day_open(Open)), 20)), day_open(Open)), 5)`
  - score -0.09(train -0.09 valid -0.04):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(High)), 20)), day_open(High)), 5)`
  - score -0.11(train +0.10 valid -0.11):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)), day_open(Open)), 10)`
- `prods2071Pr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.42(train +0.42 valid +0.46):`cross_max(abs_(day_corr(Volume, Ret)), 241)`
  - score -1.26(train -1.26 valid -1.26):`cross_quantile_q75(cross_max(abs_(day_corr(Volume, Ret)), 15), 5)`
  - score -1.40(train -1.23 valid -1.40):`cross_quantile_q75(cross_max(abs_(day_corr(Ret, Amt)), 15), 5)`
  - score -1.40(train -0.87 valid -1.40):`cross_quantile_q75(cs_last_high40(day_corr(Vwap, Vwap), day_es_ratio_lo(Amt)), 5)`
  - score -1.45(train -1.10 valid -1.45):`cross_max(abs_(cs_bucket_demean(day_std(Volume), LimitWidth)), 15)`
- `prods2071Pr2a_Ea`:核心 `abs_(day_corr(Volume, Ret))`;评分 82,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 16, 'c05_no_core': 1518, 'c05_skeleton': 756}
  - score +0.42(train +0.42 valid +0.46):`cross_max(ts_mean(abs_(day_corr(Volume, Ret)), 1), 241)`
  - score +0.42(train +0.42 valid +0.46):`cross_max(abs_(abs_(day_corr(Volume, Ret))), 241)`
  - score +0.41(train +0.41 valid +0.54):`ts_mean(cross_max(abs_(day_corr(Volume, Ret)), 241), 5)`
  - score +0.41(train +0.41 valid +0.54):`ts_mean(cross_max(abs_(abs_(day_corr(Volume, Ret))), 241), 5)`
  - score +0.41(train +0.41 valid +0.54):`ts_mean(cross_max(abs_(abs_(abs_(day_corr(Volume, Ret)))), 241), 5)`
- `prods2071Pr2b_Nb`:核心 `—`;评分 98,过线 0,入 heads 0;采样计数 {'c05_skeleton': 16}
  - score +0.03(train +0.03 valid +0.86):`sub(cross_argmax(sub(day_max(Open), day_min(Low)), 120), cross_argmax(abs_(sub(day_close(Close), day_open(Open))), 120))`
  - score -0.13(train -0.13 valid +0.91):`sub(cross_argmax(sub(day_max(High), day_min(Low)), 120), cross_argmax(abs_(sub(day_close(Close), day_open(Open))), 120))`
  - score -0.24(train -0.24 valid +0.96):`sub(cross_argmax(sub(day_max(High), day_min(Low)), 120), cross_argmax(abs_(sub(day_close(Open), day_open(Open))), 120))`
  - score -0.65(train -0.65 valid +0.38):`sub(cross_argmax(day_sum(Amt), 120), cross_argmax(abs_(sub(day_close(Close), day_open(High))), 120))`
  - score -0.72(train -0.61 valid -0.72):`cross_argmax(div(sub(day_max(High), day_min(Low)), day_open(Open)), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.36(swap Vwap->Close):`ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Close, 30))), 20)`
