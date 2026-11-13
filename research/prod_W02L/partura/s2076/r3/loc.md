# 定位:种子 2076,P 组,第 3 轮(只含 train / valid)

快照:prods2076M1_I0_open_search, prods2076M2_I0_open_search, prods2076M3_I0_open_search, prods2076Pr1a_Ea, prods2076Pr1b_Nb, prods2076Pr2a_Ea, prods2076Pr2b_Eb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(12 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.70 | +0.70 | +0.71 | +1 | 0 | prods2076Pr2b_Eb | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10), 30)` |
| +0.66 | +0.67 | +0.66 | +1 | 0 | prods2076Pr1b_Nb | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))` |
| +0.53 | +0.53 | +0.74 | +1 | 5 | prods2076Pr2a_Ea | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))` |
| -0.25 | -0.25 | +0.07 | +1 | 0 | prods2076M1_I0_open_search | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` |
| -0.34 | +0.44 | -0.34 | +1 | 20 | prods2076M3_I0_open_search | `day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 60))` |
| -0.65 | -0.65 | +0.20 | +1 | 0 | prods2076M1_I0_open_search | `cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(Low)), 15))` |
| -1.12 | -0.87 | -1.12 | -1 | 20 | prods2076M2_I0_open_search | `day_first(in_max_rolling(in_delta(Volume, 60), 30))` |
| -1.21 | -1.21 | -0.63 | +1 | 20 | prods2076M1_I0_open_search | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 20)` |
| -1.30 | -1.30 | -0.82 | +1 | 20 | prods2076M2_I0_open_search | `day_first(in_first(Amt))` |
| -1.30 | -1.30 | -0.82 | +1 | 20 | prods2076M3_I0_open_search | `day_mean(in_first(Amt))` |
| -1.31 | -0.69 | -1.31 | +1 | 20 | prods2076M2_I0_open_search | `day_close(cross_autocorr_s1(pow_2_5(nt_ts_scale(Ret, 5)), 241))` |
| -1.40 | -1.19 | -1.40 | -1 | 5 | prods2076M3_I0_open_search | `day_mean(abs_(cross_regres(Ret, Volume, 20)))` |

## 共性:315 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.20 | 0.000 | 11 | -0.09 / -2.29 | `sqrt(day_skew(in_slice(Open, 0, 60)))` |
| +2.18 | 0.000 | 9 | -0.09 / -2.27 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10)` |
| +2.08 | 0.000 | 118 | -0.90 / -2.99 | `day_zero_ratio(Amt)` |
| +2.03 | 0.001 | 6 | -0.22 / -2.25 | `day_skew(in_slice(Low, 0, 60))` |
| +2.00 | 0.000 | 17 | -0.32 / -2.32 | `day_skew(in_slice(Open, 0, 60))` |
| +1.98 | 0.002 | 5 | -0.26 / -2.24 | `sqrt(day_skew(in_slice(Low, 0, 60)))` |
| +1.98 | 0.002 | 5 | -0.26 / -2.24 | `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Low, 0, 60))), 10)` |
| +1.71 | 0.000 | 12 | -0.56 / -2.27 | `cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Open)), 10), 30)` |
| +1.71 | 0.000 | 12 | -0.56 / -2.27 | `ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Open)), 10)` |
| +1.64 | 0.000 | 54 | -0.85 / -2.49 | `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)` |
| +1.55 | 0.000 | 50 | -0.90 / -2.46 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` |
| +1.54 | 0.000 | 61 | -0.97 / -2.51 | `sqrt(day_skew(Open))` |
| +1.47 | 0.022 | 4 | -0.76 / -2.23 | `div(day_zero_ratio(Amt), day_sum(Low))` |
| +1.47 | 0.000 | 66 | -1.05 / -2.52 | `day_skew(Open)` |
| +1.45 | 0.021 | 5 | -0.78 / -2.23 | `abs_(day_skew(in_slice(Open, 0, 60)))` |
| +1.39 | 0.027 | 4 | -0.84 / -2.23 | `day_first(Vwap)` |
| +1.30 | 0.038 | 4 | -0.93 / -2.22 | `day_open(Open)` |
| +1.24 | 0.047 | 4 | -0.98 / -2.22 | `day_skew(in_slice(Amt, 0, 60))` |
| +1.11 | 0.032 | 6 | -1.12 / -2.23 | `day_sum(Low)` |
| +0.56 | 0.166 | 6 | -1.66 / -2.22 | `day_topw_mean(Open, High)` |

## 拆解(26 次评估)

### head score +0.70:`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10)` | +0.31 | +0.51 | +0.31 | — | (子树本身) |
| sufficiency | `sqrt(sqrt(day_skew(in_slice(Open, 0, 60))))` | -4.80 | -4.16 | -4.80 | — | (子树本身) |
| sufficiency | `sqrt(day_skew(in_slice(Open, 0, 60)))` | -4.80 | -4.16 | -4.80 | — | (子树本身) |
| sufficiency | `day_skew(in_slice(Open, 0, 60))` | -5.33 | -5.33 | -5.26 | — | (子树本身) |
| knockout | `ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10)` | — | — | — | — | `cross_mean(day_zero_ratio(Amt), 30)` |
| knockout | `sqrt(sqrt(day_skew(in_slice(Open, 0, 60))))` | +0.51 | +0.70 | +0.51 | +0.19 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| swap | `Amt->Volume` | +0.70 | +0.70 | +0.71 | — | `cross_mean(ts_cov(day_zero_ratio(Volume), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10), 30)` |
| swap | `Open->Close` | +0.43 | +0.59 | +0.43 | — | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Close, 0, 60)))), 10), 30)` |
| window | `cross_mean@30->15` | +0.37 | +0.37 | +0.77 | — | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10), 15)` |
| window | `cross_mean@30->60` | +0.47 | +0.54 | +0.47 | — | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10), 60)` |

### head score +0.53:`sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30)` | +0.32 | +0.32 | +0.39 | — | (子树本身) |
| sufficiency | `ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10)` | -0.26 | +0.04 | -0.26 | — | (子树本身) |
| sufficiency | `sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30)))` | -2.95 | -2.95 | -2.30 | — | (子树本身) |
| sufficiency | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))` | +0.47 | +0.47 | +0.61 | — | (子树本身) |
| knockout | `cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30)` | +0.45 | +0.54 | +0.45 | +0.08 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10))` |
| knockout | `ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10)` | -0.34 | -0.34 | -0.33 | +0.87 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 30))` |
| knockout | `sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30)))` | +0.46 | +0.50 | +0.46 | +0.07 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30)), 10), 30))` |
| knockout | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))` | +0.51 | +0.51 | +0.73 | +0.01 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10)), 10), 30))` |
| swap | `Amt->Volume` | +0.49 | +0.49 | +0.73 | — | `sub(cross_mean(ts_cov(day_zero_ratio(Volume), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Volume), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Volume), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Volume), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))` |
| swap | `Open->Close` | +0.49 | +0.49 | +0.58 | — | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Close)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Close)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Close)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Close)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))` |
| window | `cross_mean@10->5` | +0.51 | +0.51 | +0.60 | — | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 5), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))` |
| window | `cross_mean@10->20` | +0.68 | +0.68 | +0.93 | — | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 20), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))` |

### head score -0.34:`day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -0.62 | +0.39 | -0.62 | — | `day_max(cross_corr(Volume, cross_corr(Volume, Ret, 60), 60))` |
| window | `cross_corr@60->30` | -0.40 | -0.40 | -0.18 | — | `day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 30))` |
| window | `cross_corr@60->120` | -0.04 | +0.11 | -0.04 | — | `day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 120))` |

### head score -1.30:`day_mean(in_first(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | — | — | — | — | `day_mean(in_first(Volume))` |

## 机械核心卡(B0 按这个顺序取)

1. `sqrt(day_skew(in_slice(Open, 0, 60)))` — enrichment,均值差 +2.20,p 0.000
2. `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10)` — enrichment,均值差 +2.18,p 0.000
3. `day_zero_ratio(Amt)` — enrichment,均值差 +2.08,p 0.000
4. `day_skew(in_slice(Low, 0, 60))` — enrichment,均值差 +2.03,p 0.001
5. `day_skew(in_slice(Open, 0, 60))` — enrichment,均值差 +2.00,p 0.000
6. `sqrt(day_skew(in_slice(Low, 0, 60)))` — enrichment,均值差 +1.98,p 0.002
7. `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Low, 0, 60))), 10)` — enrichment,均值差 +1.98,p 0.002
8. `cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Open)), 10), 30)` — enrichment,均值差 +1.71,p 0.000
9. `ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Open)), 10)` — enrichment,均值差 +1.71,p 0.000
10. `ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)` — enrichment,均值差 +1.64,p 0.000
11. `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` — enrichment,均值差 +1.55,p 0.000
12. `sqrt(day_skew(Open))` — enrichment,均值差 +1.54,p 0.000
13. `div(day_zero_ratio(Amt), day_sum(Low))` — enrichment,均值差 +1.47,p 0.022
14. `day_skew(Open)` — enrichment,均值差 +1.47,p 0.000
15. `abs_(day_skew(in_slice(Open, 0, 60)))` — enrichment,均值差 +1.45,p 0.021
16. `day_first(Vwap)` — enrichment,均值差 +1.39,p 0.027
17. `day_open(Open)` — enrichment,均值差 +1.30,p 0.038
18. `day_skew(in_slice(Amt, 0, 60))` — enrichment,均值差 +1.24,p 0.047
19. `day_sum(Low)` — enrichment,均值差 +1.11,p 0.032

## 本组之前各轮的任务

- `prods2076Pr1a_Ea`:核心 `day_var(pow_2_5(pow_2_5(Ret)))`;评分 81,过线 0,入 heads 0;采样计数 {'c05_no_core': 2939, 'c05_skeleton': 1539, 'c05_periphery_seen': 4}
  - score -1.81(train -1.81 valid -0.02):`div(ts_delta(ts_autocorr_s1(day_var(pow_2_5(pow_2_5(Ret))), 30), 5), -2)`
  - score -2.34(train -2.34 valid -0.31):`div(ts_delta(ts_std(day_var(pow_2_5(pow_2_5(Ret))), 30), 5), -2)`
  - score -2.39(train -2.39 valid -0.60):`div(ts_delta(ts_autocorr_s1(day_var(pow_2_5(pow_2_5(Ret))), 10), 5), -2)`
  - score -2.45(train -2.45 valid -2.21):`add(ts_decay_linear(ts_max(day_var(pow_2_5(pow_2_5(Ret))), 30), 20), cs_last_high05(day_q_stat_std(Volume), day_min(Amt)))`
  - score -2.75(train -2.75 valid -2.59):`add(ts_decay_linear(ts_max(day_var(pow_2_5(pow_2_5(Ret))), 30), 20), day_es_ratio_lo(Close))`
- `prods2076Pr1b_Nb`:核心 `—`;评分 90,过线 3,入 heads 1;采样计数 {'c05_skeleton': 14}
  - score +0.66(train +0.67 valid +0.66):`sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))`
  - score +0.64(train +0.64 valid +0.67):`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)`
  - score +0.63(train +0.63 valid +0.67):`sigmoid(sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)))`
  - score +0.33(train +0.46 valid +0.33):`ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10)`
  - score +0.13(train +0.64 valid +0.13):`sigmoid(cross_mean(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 30))`
- `prods2076Pr2a_Ea`:核心 `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)`;评分 96,过线 1,入 heads 1;采样计数 {'c05_no_core': 2256, 'c05_skeleton': 1080, 'c05_periphery_seen': 10, 'mutation_refused': 5}
  - score +0.53(train +0.53 valid +0.74):`sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))`
  - score +0.48(train +0.48 valid +0.67):`sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Amt)), 10), 30))`
  - score +0.46(train +0.46 valid +0.63):`sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Open)), 10), 30))`
  - score +0.20(train +0.47 valid +0.20):`sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))`
  - score +0.17(train +0.17 valid +0.27):`cross_tail_mean_q25(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 30)`
- `prods2076Pr2b_Eb`:核心 `day_zero_ratio(Amt)`;评分 99,过线 6,入 heads 1;采样计数 {'c05_skeleton': 518, 'c05_no_core': 1066, 'c05_periphery_seen': 10}
  - score +0.70(train +0.70 valid +0.71):`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in_slice(Open, 0, 60)))), 10), 30)`
  - score +0.66(train +0.79 valid +0.66):`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Low, 0, 60))), 10), 30)`
  - score +0.61(train +0.68 valid +0.61):`cross_mean(ts_cov(day_zero_ratio(Amt), abs_(day_skew(in_slice(Open, 0, 60))), 10), 30)`
  - score +0.57(train +0.76 valid +0.57):`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)`
  - score +0.55(train +0.55 valid +0.63):`cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(High, 0, 60))), 10), 30)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.15(window cross_mean@10->20):`sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 20), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), sqrt(day_skew(Low)), 10), 30))), 10), 30))`
