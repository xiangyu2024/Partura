# 定位:种子 808,P 组,第 2 轮(只含 train / valid)

快照:c07s808M1_I0_open_search, c07s808M2_I0_open_search, c08s808Pr1a_Ea, c08s808Pr1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(8 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.30 | +1.36 | +1.30 | -1 | 0 | c08s808Pr1b_Nb | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241)` |
| +1.26 | +1.26 | +1.79 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 50)` |
| +1.09 | +1.09 | +1.53 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` |
| +1.07 | +1.07 | +2.25 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` |
| +0.97 | +0.97 | +0.98 | -1 | 5 | c08s808Pr1a_Ea | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))` |
| +0.79 | +0.79 | +2.47 | -1 | 0 | c07s808M1_I0_open_search | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)` |
| +0.57 | +0.57 | +0.84 | -1 | 20 | c08s808Pr1b_Nb | `cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 30)` |
| +0.50 | +0.50 | +0.68 | +1 | 0 | c07s808M2_I0_open_search | `cross_sum(cross_autocorr_s1(ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15)), 40), 15)), 40), 15), 60)` |

## 共性:337 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.24 | 0.001 | 4 | +0.89 / -1.35 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` |
| +2.09 | 0.001 | 4 | +0.74 / -1.35 | `day_wstd(Ret, Ret)` |
| +2.06 | 0.000 | 10 | +0.67 / -1.39 | `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` |
| +1.98 | 0.000 | 15 | +0.57 / -1.41 | `cs_demean(day_wstd(Ret, Volume))` |
| +1.40 | 0.005 | 4 | +0.06 / -1.34 | `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15))` |
| +1.40 | 0.005 | 4 | +0.05 / -1.34 | `ts_product(day_wmean(Ret, Volume), 30)` |
| +1.33 | 0.006 | 4 | -0.02 / -1.34 | `day_zero_ratio(Open)` |
| +1.31 | 0.001 | 8 | -0.05 / -1.36 | `cs_rank(ts_max(day_centroid(Volume), 99))` |
| +1.31 | 0.001 | 8 | -0.05 / -1.36 | `ts_max(day_centroid(Volume), 99)` |
| +1.26 | 0.000 | 12 | -0.11 / -1.37 | `day_centroid(Volume)` |
| +1.11 | 0.000 | 24 | -0.29 / -1.41 | `day_wstd(Ret, Volume)` |
| +1.00 | 0.007 | 7 | -0.35 / -1.35 | `cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15)` |
| +1.00 | 0.007 | 7 | -0.35 / -1.35 | `cross_autocorr_s1(day_topw_mean(High, Vwap), 5)` |
| +0.94 | 0.009 | 9 | -0.41 / -1.35 | `ts_min(day_wmean(Ret, Volume), 30)` |
| +0.94 | 0.009 | 9 | -0.41 / -1.35 | `cs_rank(ts_min(day_wmean(Ret, Volume), 30))` |
| +0.92 | 0.002 | 17 | -0.45 / -1.37 | `cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120))` |
| +0.92 | 0.002 | 17 | -0.45 / -1.37 | `cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` |
| +0.88 | 0.025 | 8 | -0.46 / -1.35 | `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15))` |
| +0.86 | 0.008 | 12 | -0.50 / -1.36 | `day_cov(Open, Ret)` |
| +0.82 | 0.083 | 5 | -0.52 / -1.34 | `ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15)), 40)` |

## 拆解(30 次评估)

### head score +1.30:`cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Open, Ret)` | -1.79 | -1.09 | -1.79 | — | (子树本身) |
| sufficiency | `day_wmean(Vwap, High)` | -1.34 | -1.34 | -0.38 | — | (子树本身) |
| swap | `Open->Close` | +0.81 | +0.81 | +1.14 | — | `cross_regbeta(day_cov(Close, Ret), day_wmean(Vwap, High), 241)` |
| swap | `Vwap->Close` | +1.33 | +1.40 | +1.33 | — | `cross_regbeta(day_cov(Open, Ret), day_wmean(Close, High), 241)` |
| window | `cross_regbeta@241->120` | +0.46 | +0.46 | +1.22 | — | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 120)` |
| window | `cross_regbeta@241->482` | +0.70 | +0.70 | +0.95 | — | `cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 482)` |

### head score +1.09:`ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_wmean(Ret, Amt), 50)` | -1.42 | +0.25 | -1.42 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Amt)` | -2.46 | -2.46 | +0.01 | — | (子树本身) |
| swap | `Amt->Volume` | +0.99 | +0.99 | +1.42 | — | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` |
| window | `ts_max@50->25` | +0.65 | +1.03 | +0.65 | — | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 25)` |
| window | `ts_max@50->100` | +0.71 | +0.71 | +1.18 | — | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 100)` |

### head score +1.07:`ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_demean(day_wstd(Ret, Volume)), 10)` | -1.41 | -1.41 | -0.28 | — | (子树本身) |
| sufficiency | `cs_demean(day_wstd(Ret, Volume))` | -3.47 | -2.68 | -3.47 | — | (子树本身) |
| sufficiency | `day_wstd(Ret, Volume)` | -3.47 | -2.68 | -3.47 | — | (子树本身) |
| knockout | `ts_max(cs_demean(day_wstd(Ret, Volume)), 10)` | +1.03 | +1.03 | +2.21 | +0.04 | `ts_max(cs_demean(day_wstd(Ret, Volume)), 100)` |
| knockout | `cs_demean(day_wstd(Ret, Volume))` | +0.89 | +0.89 | +1.99 | +0.18 | `ts_max(ts_max(day_wstd(Ret, Volume), 10), 100)` |
| swap | `Volume->Amt` | +1.08 | +1.08 | +2.23 | — | `ts_max(ts_max(cs_demean(day_wstd(Ret, Amt)), 10), 100)` |
| window | `ts_max@100->50` | +0.68 | +0.98 | +0.68 | — | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)` |
| window | `ts_max@100->200` | +0.51 | +0.51 | +1.01 | — | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 200)` |

### head score +0.97:`add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120))` | -0.98 | -0.98 | +0.09 | — | (子树本身) |
| sufficiency | `cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120))` | +0.10 | +0.78 | +0.10 | — | (子树本身) |
| sufficiency | `cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | -0.98 | -0.98 | +0.09 | — | (子树本身) |
| sufficiency | `cross_tail_mean_q25(day_centroid(Volume), 120)` | +0.10 | +0.78 | +0.10 | — | (子树本身) |
| knockout | `cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120))` | +0.09 | +0.78 | +0.09 | +0.89 | `add(cross_tail_mean_q75(day_wmean(Ret, Volume), 120), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))` |
| knockout | `cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120))` | -0.94 | -0.94 | +0.04 | +1.91 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cross_tail_mean_q25(day_centroid(Volume), 120))` |
| knockout | `cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` | -0.65 | +0.06 | -0.65 | +1.63 | `add(cs_rank(day_wmean(Ret, Volume)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))` |
| knockout | `cross_tail_mean_q25(day_centroid(Volume), 120)` | -1.62 | -1.62 | -0.36 | +2.59 | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(day_centroid(Volume)))` |
| swap | `Volume->Amt` | +0.99 | +1.01 | +0.99 | — | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Amt), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Amt), 120)))` |
| window | `cross_tail_mean_q75@120->60` | -0.46 | +1.41 | -0.46 | — | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 60)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))` |
| window | `cross_tail_mean_q75@120->240` | +0.56 | +0.81 | +0.56 | — | `add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 240)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)` — enrichment,均值差 +2.24,p 0.001
2. `day_wstd(Ret, Ret)` — enrichment,均值差 +2.09,p 0.001
3. `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` — enrichment,均值差 +2.06,p 0.000
4. `cs_demean(day_wstd(Ret, Volume))` — enrichment,均值差 +1.98,p 0.000
5. `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15))` — enrichment,均值差 +1.40,p 0.005
6. `ts_product(day_wmean(Ret, Volume), 30)` — enrichment,均值差 +1.40,p 0.005
7. `day_zero_ratio(Open)` — enrichment,均值差 +1.33,p 0.006
8. `cs_rank(ts_max(day_centroid(Volume), 99))` — enrichment,均值差 +1.31,p 0.001
9. `ts_max(day_centroid(Volume), 99)` — enrichment,均值差 +1.31,p 0.001
10. `day_centroid(Volume)` — enrichment,均值差 +1.26,p 0.000
11. `day_wstd(Ret, Volume)` — enrichment,均值差 +1.11,p 0.000
12. `cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 5), 15)` — enrichment,均值差 +1.00,p 0.007
13. `cross_autocorr_s1(day_topw_mean(High, Vwap), 5)` — enrichment,均值差 +1.00,p 0.007
14. `ts_min(day_wmean(Ret, Volume), 30)` — enrichment,均值差 +0.94,p 0.009
15. `cs_rank(ts_min(day_wmean(Ret, Volume), 30))` — enrichment,均值差 +0.94,p 0.009
16. `cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120))` — enrichment,均值差 +0.92,p 0.002
17. `cross_tail_mean_q75(day_wmean(Ret, Volume), 120)` — enrichment,均值差 +0.92,p 0.002
18. `cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15))` — enrichment,均值差 +0.88,p 0.025
19. `day_cov(Open, Ret)` — enrichment,均值差 +0.86,p 0.008
20. `ts_max(cs_last_high05(day_distinct_ratio(Ret), cross_autocorr_s1(cross_autocorr_s1(day_topw_mean(High, Vwap), 15), 15)), 40)` — enrichment,均值差 +0.82,p 0.083
21. `day_topw_mean(High, High)` — enrichment,均值差 +0.78,p 0.092
22. `day_distinct_ratio(Ret)` — enrichment,均值差 +0.76,p 0.000
23. `day_wmean(Vwap, High)` — enrichment,均值差 +0.71,p 0.017
24. `ts_max(LogFloatShares, 50)` — enrichment,均值差 +0.62,p 0.052

## 本组之前各轮的任务

- `c08s808Pr1a_Ea`:核心 `day_wmean(Ret, Volume)`;评分 92,过线 2,入 heads 1;采样计数 {'c05_no_core': 2618}
  - score +0.97(train +0.97 valid +0.98):`add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120)))`
  - score +0.54(train +0.54 valid +0.97):`add(cs_rank(ts_max(day_centroid(Volume), 20)), cs_rank(ts_product(add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(day_centroid(Volume), 120))), 30)))`
  - score +0.44(train +1.09 valid +0.44):`day_centroid(Volume)`
  - score +0.33(train +0.33 valid +1.37):`add(cs_rank(cross_tail_mean_q75(day_wmean(Ret, Volume), 120)), cs_rank(cross_tail_mean_q25(add(cs_rank(ts_max(day_centroid(Volume), 99)), cs_rank(ts_min(day_wmean(Ret, Volume), 30))), 120)))`
  - score +0.32(train +0.32 valid +1.71):`add(cs_rank(ts_max(day_centroid(Volume), 99)), cs_rank(ts_product(day_wmean(Ret, Volume), 30)))`
- `c08s808Pr1b_Nb`:核心 `—`;评分 83,过线 2,入 heads 2;采样计数 {}
  - score +1.30(train +1.36 valid +1.30):`cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, High), 241)`
  - score +0.57(train +0.57 valid +0.84):`cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, High), 30)`
  - score +0.40(train +0.40 valid +0.67):`cross_regbeta(day_cov(Ret, Vwap), day_wmean(Vwap, Ret), 30)`
  - score +0.23(train +0.23 valid +1.03):`cross_regbeta(day_cov(Open, Ret), day_wmean(Vwap, Ret), 30)`
  - score +0.18(train +0.18 valid +0.93):`cross_regbeta(day_cov(Open, Ret), day_wmean(High, Ret), 30)`

## 比原 head 好的拆解变体(R 候选)

(没有)
