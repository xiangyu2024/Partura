# 定位:种子 903,P 组,第 3 轮(只含 train / valid)

快照:prods903M1_I0_open_search, prods903M2_I0_open_search, prods903M3_I0_open_search, prods903Pr1a_Ea, prods903Pr1b_Nb, prods903Pr2a_Ea, prods903Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.51 | +1.51 | +1.60 | -1 | 5 | prods903Pr1b_Nb | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| +1.45 | +1.45 | +2.40 | -1 | 5 | prods903Pr2a_Ea | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| +1.33 | +1.33 | +2.35 | -1 | 5 | prods903M3_I0_open_search | `cs_last_low40(cross_valid_count(day_centroid(Open), 30), ts_med(day_centroid(Volume), 20))` |
| +0.96 | +0.96 | +1.05 | -1 | 20 | prods903Pr2a_Ea | `sub(cross_ema(day_centroid(Amt), 5), cross_ema(day_centroid(Amt), 60))` |
| +0.92 | +0.92 | +2.66 | -1 | 5 | prods903Pr2a_Ea | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(cross_delay(day_close(Close), 1), 1)), 60)` |
| +0.73 | +1.19 | +0.73 | -1 | 5 | prods903Pr2a_Ea | `cross_corr(day_centroid(Amt), log(day_sum(Amt)), 60)` |
| +0.71 | +0.71 | +1.19 | -1 | 5 | prods903Pr2a_Ea | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 30)), 60)` |
| +0.67 | +0.72 | +0.67 | -1 | 5 | prods903M3_I0_open_search | `cs_last_low40(cross_valid_count(ts_med(cs_last_low40(cross_valid_count(day_centroid(Open), 15), ts_med(day_centroid(Volume), 40)), 40), 30), ts_med(cs_last_low40(cross_valid_count(day_centroid(Open), 15), ts_med(day_centroid(Volume), 40)), 40))` |
| +0.63 | +0.63 | +1.13 | +1 | 5 | prods903M1_I0_open_search | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)), sqrt(day_centroid(Open)))` |
| +0.60 | +1.39 | +0.60 | +1 | 20 | prods903M2_I0_open_search | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day_centroid(Amt))` |
| +0.55 | +1.51 | +0.55 | -1 | 5 | prods903Pr2b_Nb | `cross_mean(day_centroid(in_slice(Amt, 121, 239)), 30)` |

## 共性:580 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.86 | 0.000 | 19 | +0.75 / -1.11 | `ts_med(day_centroid(Volume), 40)` |
| +1.59 | 0.001 | 6 | +0.53 / -1.07 | `cross_valid_count(day_centroid(Open), 15)` |
| +1.43 | 0.018 | 4 | +0.37 / -1.06 | `day_hurst(Ret)` |
| +1.40 | 0.000 | 68 | +0.18 / -1.22 | `day_centroid(Volume)` |
| +1.35 | 0.004 | 6 | +0.28 / -1.07 | `sub(day_centroid(Amt), day_flat_run_max(Amt))` |
| +1.31 | 0.005 | 5 | +0.25 / -1.06 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 15)), pow_2(pow_2(day_centroid(Volume))))` |
| +1.17 | 0.000 | 34 | +0.05 / -1.12 | `pow_2(day_centroid(Volume))` |
| +1.12 | 0.010 | 7 | +0.06 / -1.06 | `pow_3(cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3))))` |
| +1.07 | 0.012 | 6 | +0.00 / -1.06 | `sqrt(day_centroid(Amt))` |
| +1.05 | 0.000 | 30 | -0.05 / -1.11 | `day_centroid(Open)` |
| +1.04 | 0.008 | 9 | -0.02 / -1.07 | `day_flat_run_max(Amt)` |
| +1.03 | 0.000 | 21 | -0.06 / -1.09 | `pow_2(pow_2(day_centroid(Volume)))` |
| +0.97 | 0.003 | 15 | -0.10 / -1.08 | `cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3)))` |
| +0.96 | 0.028 | 6 | -0.10 / -1.06 | `ts_autocorr_s1(day_flat_ratio(Vwap), 5)` |
| +0.94 | 0.002 | 13 | -0.13 / -1.07 | `day_centroid(in_slice(Amt, 121, 239))` |
| +0.94 | 0.018 | 8 | -0.13 / -1.06 | `mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241)))` |
| +0.92 | 0.000 | 102 | -0.29 / -1.21 | `cs_mask_top_replace_mean_neg(day_open(Open))` |
| +0.91 | 0.004 | 18 | -0.17 / -1.08 | `cross_valid_count(day_centroid(Open), 30)` |
| +0.90 | 0.002 | 18 | -0.18 / -1.08 | `cs_rank(cross_rank(day_open(Open), 241))` |
| +0.88 | 0.002 | 20 | -0.20 / -1.08 | `cs_state_rank(day_sum(Amt), 60)` |

## 拆解(39 次评估)

### head score +1.51:`cs_regres(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(cross_mean(day_std(Amt), 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cross_mean(day_centroid(Amt), 20))` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `cs_rank(cross_mean(day_std(Amt), 30))` | -2.57 | -2.57 | -2.56 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -2.57 | -2.57 | -2.56 | — | (子树本身) |
| knockout | `cs_rank(cross_mean(day_centroid(Amt), 20))` | +0.35 | +1.40 | +0.35 | +1.16 | `cs_regres(cross_mean(day_centroid(Amt), 20), cs_rank(cross_mean(day_std(Amt), 30)))` |
| knockout | `cs_rank(cross_mean(day_std(Amt), 30))` | +0.90 | +1.53 | +0.90 | +0.60 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 20)), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +0.39 | +0.97 | +0.39 | +1.11 | `cs_regres(cs_rank(day_centroid(Amt)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| knockout | `cross_mean(day_std(Amt), 30)` | +1.42 | +1.54 | +1.42 | +0.08 | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 20)), cs_rank(day_std(Amt)))` |
| swap | `Amt->Volume` | -0.12 | +1.24 | -0.12 | — | `cs_regres(cs_rank(cross_mean(day_centroid(Volume), 20)), cs_rank(cross_mean(day_std(Volume), 30)))` |
| window | `cross_mean@20->10` | +1.21 | +1.81 | +1.21 | — | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 10)), cs_rank(cross_mean(day_std(Amt), 30)))` |
| window | `cross_mean@20->40` | +1.22 | +1.22 | +1.93 | — | `cs_regres(cs_rank(cross_mean(day_centroid(Amt), 40)), cs_rank(cross_mean(day_std(Amt), 30)))` |

### head score +1.45:`cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_open(Open), cross_delay(day_close(Close), 1))` | -3.94 | -1.84 | -3.94 | — | (子树本身) |
| sufficiency | `cross_delay(day_close(Close), 1)` | -1.33 | -1.33 | -0.38 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| sufficiency | `day_open(Open)` | -1.35 | -1.35 | -0.40 | — | (子树本身) |
| knockout | `div(day_open(Open), cross_delay(day_close(Close), 1))` | +0.39 | +0.45 | +0.39 | +1.06 | `cross_corr(day_centroid(Amt), day_open(Open), 60)` |
| knockout | `cross_delay(day_close(Close), 1)` | -1.18 | -0.59 | -1.18 | +2.63 | `cross_corr(day_centroid(Amt), div(day_open(Open), day_close(Close)), 60)` |
| swap | `Amt->Volume` | +1.44 | +1.44 | +2.45 | — | `cross_corr(day_centroid(Volume), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)` |
| swap | `Open->Close` | +1.37 | +1.37 | +2.40 | — | `cross_corr(day_centroid(Amt), div(day_open(Close), cross_delay(day_close(Close), 1)), 60)` |
| window | `cross_corr@60->30` | +0.99 | +0.99 | +1.68 | — | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 30)` |
| window | `cross_corr@60->120` | +0.96 | +0.96 | +1.72 | — | `cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 120)` |

### head score +1.33:`cs_last_low40(cross_valid_count(day_centroid(Open), 30), ts_med(day_centroid(Volume), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_valid_count(day_centroid(Open), 30)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_med(day_centroid(Volume), 20)` | +1.14 | +1.44 | +1.14 | — | (子树本身) |
| sufficiency | `day_centroid(Open)` | -3.27 | -2.96 | -3.27 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `cross_valid_count(day_centroid(Open), 30)` | +0.23 | +1.39 | +0.23 | +1.10 | `cs_last_low40(day_centroid(Open), ts_med(day_centroid(Volume), 20))` |
| knockout | `ts_med(day_centroid(Volume), 20)` | +0.13 | +0.13 | +1.48 | +1.20 | `cs_last_low40(cross_valid_count(day_centroid(Open), 30), day_centroid(Volume))` |
| swap | `Open->Close` | +1.33 | +1.33 | +2.35 | — | `cs_last_low40(cross_valid_count(day_centroid(Close), 30), ts_med(day_centroid(Volume), 20))` |
| swap | `Volume->Amt` | +1.32 | +1.32 | +2.42 | — | `cs_last_low40(cross_valid_count(day_centroid(Open), 30), ts_med(day_centroid(Amt), 20))` |
| window | `cross_valid_count@30->15` | +1.38 | +1.38 | +2.28 | — | `cs_last_low40(cross_valid_count(day_centroid(Open), 15), ts_med(day_centroid(Volume), 20))` |
| window | `cross_valid_count@30->60` | +1.35 | +1.35 | +2.55 | — | `cs_last_low40(cross_valid_count(day_centroid(Open), 60), ts_med(day_centroid(Volume), 20))` |

### head score +0.96:`sub(cross_ema(day_centroid(Amt), 5), cross_ema(day_centroid(Amt), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_ema(day_centroid(Amt), 5)` | +0.63 | +1.66 | +0.63 | — | (子树本身) |
| sufficiency | `cross_ema(day_centroid(Amt), 60)` | +0.05 | +1.03 | +0.05 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cross_ema(day_centroid(Amt), 5)` | -0.71 | -0.71 | -0.68 | +1.67 | `sub(day_centroid(Amt), cross_ema(day_centroid(Amt), 60))` |
| knockout | `cross_ema(day_centroid(Amt), 60)` | -6.39 | -6.39 | -5.98 | +7.36 | `sub(cross_ema(day_centroid(Amt), 5), day_centroid(Amt))` |
| swap | `Amt->Volume` | +0.91 | +0.94 | +0.91 | — | `sub(cross_ema(day_centroid(Volume), 5), cross_ema(day_centroid(Volume), 60))` |
| window | `cross_ema@5->2` | +0.56 | +0.56 | +0.79 | — | `sub(cross_ema(day_centroid(Amt), 2), cross_ema(day_centroid(Amt), 60))` |
| window | `cross_ema@5->10` | +1.06 | +1.06 | +1.32 | — | `sub(cross_ema(day_centroid(Amt), 10), cross_ema(day_centroid(Amt), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +1.51)
2. `cs_rank(cross_mean(day_centroid(Amt), 20))` — ablation,自身 score +1.34(所在 head +1.51)
3. `ts_med(day_centroid(Volume), 20)` — ablation,自身 score +1.14(所在 head +1.33)
4. `cross_ema(day_centroid(Amt), 5)` — ablation,自身 score +0.63(所在 head +0.96)
5. `ts_med(day_centroid(Volume), 40)` — enrichment,均值差 +1.86,p 0.000
6. `cross_valid_count(day_centroid(Open), 15)` — enrichment,均值差 +1.59,p 0.001
7. `day_hurst(Ret)` — enrichment,均值差 +1.43,p 0.018
8. `day_centroid(Volume)` — enrichment,均值差 +1.40,p 0.000
9. `sub(day_centroid(Amt), day_flat_run_max(Amt))` — enrichment,均值差 +1.35,p 0.004
10. `div(day_autocorr_n1(in_decay_linear_rolling(Close, 15)), pow_2(pow_2(day_centroid(Volume))))` — enrichment,均值差 +1.31,p 0.005
11. `pow_2(day_centroid(Volume))` — enrichment,均值差 +1.17,p 0.000
12. `pow_3(cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3))))` — enrichment,均值差 +1.12,p 0.010
13. `sqrt(day_centroid(Amt))` — enrichment,均值差 +1.07,p 0.012
14. `day_centroid(Open)` — enrichment,均值差 +1.05,p 0.000
15. `day_flat_run_max(Amt)` — enrichment,均值差 +1.04,p 0.008
16. `pow_2(pow_2(day_centroid(Volume)))` — enrichment,均值差 +1.03,p 0.000
17. `cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3)))` — enrichment,均值差 +0.97,p 0.003
18. `ts_autocorr_s1(day_flat_ratio(Vwap), 5)` — enrichment,均值差 +0.96,p 0.028
19. `day_centroid(in_slice(Amt, 121, 239))` — enrichment,均值差 +0.94,p 0.002
20. `mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241)))` — enrichment,均值差 +0.94,p 0.018
21. `cs_mask_top_replace_mean_neg(day_open(Open))` — enrichment,均值差 +0.92,p 0.000
22. `cross_valid_count(day_centroid(Open), 30)` — enrichment,均值差 +0.91,p 0.004
23. `cs_rank(cross_rank(day_open(Open), 241))` — enrichment,均值差 +0.90,p 0.002
24. `cs_state_rank(day_sum(Amt), 60)` — enrichment,均值差 +0.88,p 0.002
25. `day_sum(Amt)` — enrichment,均值差 +0.87,p 0.000
26. `cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))` — enrichment,均值差 +0.86,p 0.008
27. `day_quantile_q75(cross_valid_count(Open, 30))` — enrichment,均值差 +0.84,p 0.081
28. `pow_3(cs_mask_top_replace_mean_neg(day_open(Open)))` — enrichment,均值差 +0.83,p 0.000
29. `day_open(Open)` — enrichment,均值差 +0.83,p 0.000
30. `day_quantile_q75(cross_valid_count(Open, 3))` — enrichment,均值差 +0.81,p 0.000
31. `cross_rank(day_open(Open), 241)` — enrichment,均值差 +0.80,p 0.002
32. `div(day_open(Open), cross_delay(day_close(Close), 1))` — enrichment,均值差 +0.75,p 0.035
33. `day_centroid(Amt)` — enrichment,均值差 +0.74,p 0.000
34. `day_signed_ratio(Open, Amt)` — enrichment,均值差 +0.72,p 0.046
35. `day_close(Close)` — enrichment,均值差 +0.68,p 0.006
36. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +0.66,p 0.027
37. `day_quantile_q75(cross_valid_count(Open, 241))` — enrichment,均值差 +0.62,p 0.025

## 本组之前各轮的任务

- `prods903Pr1a_Ea`:核心 `day_open(Open)`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 749, 'c05_periphery_seen': 2}
  - score +0.39(train +0.39 valid +0.51):`add(mul(cs_mask_top_replace_mean_neg(day_open(Open)), cs_rank(cross_rank(day_open(Open), 241))), mul(sub(1, cs_state_rank(day_sum(Amt), 60)), cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))))`
  - score +0.39(train +0.39 valid +0.51):`add(mul(cs_mask_top_replace_mean_neg(day_open(Open)), cs_rank(cross_rank(day_open(Open), 241))), mul(sub(1, mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241)))), cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))))`
  - score +0.35(train +0.54 valid +0.35):`add(mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241))), mul(sub(add(mul(cs_state_rank(day_sum(Amt), 40), cs_rank(cross_rank(day_open(Open), 241))), mul(sub(1, cs_state_rank(day_sum(Amt), 60)), cs_rank(cs_mask_top_replace_mean_neg(day_open(Open))))), cs_state_rank(day_sum(Amt), 60)), cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))))`
  - score +0.32(train +0.32 valid +0.53):`add(mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241))), mul(sub(1, cs_state_rank(cross_rank(day_open(Open), 241), 60)), cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))))`
  - score +0.29(train +0.29 valid +0.41):`add(mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241))), mul(sub(1, cs_state_rank(day_sum(Amt), 60)), cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))))`
- `prods903Pr1b_Nb`:核心 `—`;评分 71,过线 2,入 heads 1;采样计数 {}
  - score +1.34(train +1.56 valid +1.34):`cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)`
  - score +0.76(train +1.15 valid +0.76):`cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 60)`
  - score +0.41(train +1.05 valid +0.41):`day_centroid(Amt)`
  - score +0.40(train +0.40 valid +0.85):`cross_mean(sub(day_centroid(Amt), day_centroid(Ret)), 60)`
  - score +0.38(train +0.38 valid +1.12):`sub(cross_mean(day_centroid(Amt), 20), cross_mean(day_centroid(Amt), 120))`
- `prods903Pr2a_Ea`:核心 `day_centroid(Amt)`;评分 88,过线 8,入 heads 5;采样计数 {'c05_no_core': 1582, 'c05_periphery_seen': 11}
  - score +1.45(train +1.45 valid +2.40):`cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)`
  - score +0.96(train +0.96 valid +1.05):`sub(cross_ema(day_centroid(Amt), 5), cross_ema(day_centroid(Amt), 60))`
  - score +0.92(train +0.92 valid +2.66):`cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(cross_delay(day_close(Close), 1), 1)), 60)`
  - score +0.76(train +1.13 valid +0.76):`cross_regalpha(day_centroid(Amt), div(day_open(Open), cross_delay(day_close(Close), 1)), 60)`
  - score +0.74(train +0.74 valid +1.83):`cross_corr(day_centroid(Amt), div(day_open(Open), cross_delay(day_open(Open), 1)), 60)`
- `prods903Pr2b_Nb`:核心 `—`;评分 73,过线 1,入 heads 1;采样计数 {}
  - score +0.55(train +1.51 valid +0.55):`cross_mean(day_centroid(in_slice(Amt, 121, 239)), 30)`
  - score +0.49(train +0.90 valid +0.49):`cross_mean(cross_mean(day_centroid(in_slice(Amt, 121, 239)), 30), 30)`
  - score +0.47(train +1.46 valid +0.47):`cross_mean(cross_mean(day_centroid(in_slice(Amt, 121, 239)), 5), 30)`
  - score +0.44(train +0.71 valid +0.44):`cross_sum(day_centroid(in_slice(Amt, 121, 239)), 30)`
  - score +0.43(train +0.43 valid +2.65):`cross_mean(div(cross_regbeta(sqrt(day_flat_run_max(Low)), ts_autocorr_s1(day_flat_ratio(Vwap), 5), 241), day_sum(Amt)), 30)`

## 比原 head 好的拆解变体(R 候选)

(没有)
