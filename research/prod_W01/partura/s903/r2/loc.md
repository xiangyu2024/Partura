# 定位:种子 903,P 组,第 2 轮(只含 train / valid)

快照:prods903M1_I0_open_search, prods903M2_I0_open_search, prods903Pr1a_Ea, prods903Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.34 | +1.56 | +1.34 | -1 | 5 | prods903Pr1b_Nb | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)` |
| +0.63 | +0.63 | +1.13 | +1 | 5 | prods903M1_I0_open_search | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)), sqrt(day_centroid(Open)))` |
| +0.60 | +1.39 | +0.60 | +1 | 20 | prods903M2_I0_open_search | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day_centroid(Amt))` |

## 共性:346 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.40 | 0.004 | 6 | +0.28 / -1.12 | `sub(day_centroid(Amt), day_flat_run_max(Amt))` |
| +1.36 | 0.005 | 5 | +0.25 / -1.11 | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 15)), pow_2(pow_2(day_centroid(Volume))))` |
| +1.26 | 0.000 | 34 | +0.05 / -1.22 | `pow_2(day_centroid(Volume))` |
| +1.26 | 0.003 | 8 | +0.14 / -1.12 | `day_flat_run_max(Amt)` |
| +1.23 | 0.000 | 39 | -0.00 / -1.23 | `day_centroid(Volume)` |
| +1.17 | 0.012 | 7 | +0.06 / -1.12 | `pow_3(cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3))))` |
| +1.14 | 0.000 | 33 | -0.06 / -1.20 | `day_centroid(Amt)` |
| +1.14 | 0.000 | 102 | -0.29 / -1.43 | `cs_mask_top_replace_mean_neg(day_open(Open))` |
| +1.12 | 0.008 | 6 | +0.00 / -1.11 | `sqrt(day_centroid(Amt))` |
| +1.10 | 0.000 | 21 | -0.06 / -1.16 | `pow_2(pow_2(day_centroid(Volume)))` |
| +1.03 | 0.003 | 15 | -0.10 / -1.14 | `cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3)))` |
| +0.99 | 0.018 | 8 | -0.13 / -1.12 | `mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241)))` |
| +0.99 | 0.000 | 146 | -0.52 / -1.51 | `day_open(Open)` |
| +0.97 | 0.001 | 22 | -0.18 / -1.15 | `day_sum(Amt)` |
| +0.96 | 0.002 | 18 | -0.18 / -1.14 | `cs_rank(cross_rank(day_open(Open), 241))` |
| +0.94 | 0.001 | 20 | -0.20 / -1.15 | `cs_state_rank(day_sum(Amt), 60)` |
| +0.94 | 0.000 | 51 | -0.29 / -1.23 | `pow_3(cs_mask_top_replace_mean_neg(day_open(Open)))` |
| +0.91 | 0.007 | 14 | -0.22 / -1.13 | `cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))` |
| +0.90 | 0.000 | 41 | -0.30 / -1.20 | `day_quantile_q75(cross_valid_count(Open, 3))` |
| +0.88 | 0.080 | 5 | -0.22 / -1.11 | `day_quantile_q75(cross_valid_count(Open, 30))` |

## 拆解(13 次评估)

### head score +1.34:`cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_centroid(Amt), day_flat_run_max(Amt))` | +0.16 | +0.89 | +0.16 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| sufficiency | `day_flat_run_max(Amt)` | — | — | — | — | 门槛废品 |
| knockout | `sub(day_centroid(Amt), day_flat_run_max(Amt))` | +1.72 | +1.72 | +1.83 | -0.38 | `cross_mean(day_centroid(Amt), 30)` |
| swap | `Amt->Volume` | +1.20 | +1.48 | +1.20 | — | `cross_mean(sub(day_centroid(Volume), day_flat_run_max(Volume)), 30)` |
| window | `cross_mean@30->15` | +1.00 | +1.51 | +1.00 | — | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 15)` |
| window | `cross_mean@30->60` | +0.76 | +1.15 | +0.76 | — | `cross_mean(sub(day_centroid(Amt), day_flat_run_max(Amt)), 60)` |

### head score +0.60:`div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day_centroid(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr_n1(in_decay_linear_rolling(Close, 30))` | -3.39 | -2.36 | -3.39 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| swap | `Close->Vwap` | +0.51 | +1.37 | +0.51 | — | `div(day_autocorr_n1(in_decay_linear_rolling(Vwap, 30)), day_centroid(Amt))` |
| swap | `Amt->Volume` | +0.45 | +1.41 | +0.45 | — | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 30)), day_centroid(Volume))` |
| window | `in_decay_linear_rolling@30->15` | +0.53 | +1.38 | +0.53 | — | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 15)), day_centroid(Amt))` |
| window | `in_decay_linear_rolling@30->60` | +0.52 | +1.41 | +0.52 | — | `div(day_autocorr_n1(in_decay_linear_rolling(Close, 60)), day_centroid(Amt))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_centroid(Amt), day_flat_run_max(Amt))` — enrichment,均值差 +1.40,p 0.004
2. `div(day_autocorr_n1(in_decay_linear_rolling(Close, 15)), pow_2(pow_2(day_centroid(Volume))))` — enrichment,均值差 +1.36,p 0.005
3. `pow_2(day_centroid(Volume))` — enrichment,均值差 +1.26,p 0.000
4. `day_flat_run_max(Amt)` — enrichment,均值差 +1.26,p 0.003
5. `day_centroid(Volume)` — enrichment,均值差 +1.23,p 0.000
6. `pow_3(cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3))))` — enrichment,均值差 +1.17,p 0.012
7. `day_centroid(Amt)` — enrichment,均值差 +1.14,p 0.000
8. `cs_mask_top_replace_mean_neg(day_open(Open))` — enrichment,均值差 +1.14,p 0.000
9. `sqrt(day_centroid(Amt))` — enrichment,均值差 +1.12,p 0.008
10. `pow_2(pow_2(day_centroid(Volume)))` — enrichment,均值差 +1.10,p 0.000
11. `cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3)))` — enrichment,均值差 +1.03,p 0.003
12. `mul(cs_state_rank(day_sum(Amt), 60), cs_rank(cross_rank(day_open(Open), 241)))` — enrichment,均值差 +0.99,p 0.018
13. `day_open(Open)` — enrichment,均值差 +0.99,p 0.000
14. `day_sum(Amt)` — enrichment,均值差 +0.97,p 0.001
15. `cs_rank(cross_rank(day_open(Open), 241))` — enrichment,均值差 +0.96,p 0.002
16. `cs_state_rank(day_sum(Amt), 60)` — enrichment,均值差 +0.94,p 0.001
17. `pow_3(cs_mask_top_replace_mean_neg(day_open(Open)))` — enrichment,均值差 +0.94,p 0.000
18. `cs_rank(cs_mask_top_replace_mean_neg(day_open(Open)))` — enrichment,均值差 +0.91,p 0.007
19. `day_quantile_q75(cross_valid_count(Open, 3))` — enrichment,均值差 +0.90,p 0.000
20. `day_quantile_q75(cross_valid_count(Open, 30))` — enrichment,均值差 +0.88,p 0.080
21. `cross_rank(day_open(Open), 241)` — enrichment,均值差 +0.87,p 0.003
22. `day_signed_ratio(Open, Amt)` — enrichment,均值差 +0.77,p 0.061
23. `day_quantile_q75(cross_valid_count(Open, 241))` — enrichment,均值差 +0.68,p 0.024

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

## 比原 head 好的拆解变体(R 候选)

(没有)
