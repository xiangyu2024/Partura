# 定位:种子 2027,P 组,第 2 轮(只含 train / valid)

快照:prods2027M1_I0_open_search, prods2027M2_I0_open_search, prods2027Pr1a_Ea, prods2027Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.22 | -1.20 | -1.22 | +1 | 0 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` |
| -1.34 | -1.34 | -0.83 | +1 | 5 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` |
| -1.85 | -1.73 | -1.85 | +1 | 0 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` |
| -2.72 | -2.72 | -1.88 | -1 | 20 | prods2027M2_I0_open_search | `rank(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0), True)` |
| -2.82 | -2.82 | -1.78 | +1 | 20 | prods2027M2_I0_open_search | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))` |
| -2.97 | -2.97 | -1.94 | -1 | 20 | prods2027M2_I0_open_search | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20)` |

## 共性:124 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.50 | 0.000 | 7 | -1.04 / -2.55 | `cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)` |
| +1.38 | 0.000 | 10 | -1.19 / -2.57 | `cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` |
| +1.15 | 0.000 | 16 | -1.46 / -2.61 | `day_std(in_slice(Ret, 11, 230))` |
| +0.78 | 0.007 | 13 | -1.76 / -2.54 | `day_signed_ratio(Open, High)` |
| +0.76 | 0.069 | 5 | -1.73 / -2.49 | `cs_bucket_rank(LogFloatShares, cross_autocorr(day_sum(in_slice(Ret, 11, 230)), 120, 1))` |
| +0.76 | 0.011 | 12 | -1.77 / -2.53 | `cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, High))` |
| +0.76 | 0.084 | 4 | -1.73 / -2.48 | `ts_argmin(day_sum(in_slice(Ret, 11, 230)), 30)` |
| +0.74 | 0.043 | 6 | -1.75 / -2.50 | `sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1))` |
| +0.62 | 0.046 | 13 | -1.91 / -2.52 | `day_sum(in_slice(Ret, 11, 230))` |
| +0.55 | 0.151 | 6 | -1.94 / -2.49 | `cross_autocorr(day_sum(in_slice(Ret, 11, 230)), 120, 1)` |
| +0.53 | 0.139 | 12 | -1.99 / -2.51 | `ts_argmin(LogTotalCap, 30)` |
| +0.51 | 0.267 | 5 | -1.97 / -2.48 | `day_min(Ret)` |
| +0.45 | 0.171 | 8 | -2.04 / -2.49 | `day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1)` |
| +0.45 | 0.265 | 7 | -2.04 / -2.49 | `day_quantile(Open)` |
| +0.44 | 0.349 | 4 | -2.03 / -2.47 | `sub(day_min(Ret), ts_argmin(LogTotalCap, 30))` |
| +0.39 | 0.342 | 6 | -2.09 / -2.48 | `cs_regres(day_quantile(Open), day_signed_ratio(Low, Ret))` |
| +0.26 | 0.319 | 9 | -2.22 / -2.48 | `day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1)` |
| +0.20 | 0.374 | 6 | -2.27 / -2.47 | `signedpower(day_argmax(Ret))` |
| +0.19 | 0.431 | 7 | -2.29 / -2.47 | `day_argmax(Ret)` |
| +0.17 | 0.419 | 4 | -2.29 / -2.47 | `cross_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` |

## 拆解(32 次评估)

### head score -1.22:`ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(in_slice(Ret, 11, 230), 10)` | -3.63 | -3.54 | -3.63 | — | (子树本身) |
| window | `ts_stddev@45->22` | -1.67 | -1.43 | -1.67 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 22)` |
| window | `ts_stddev@45->90` | -1.56 | -1.01 | -1.56 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 90)` |

### head score -2.72:`rank(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0), True)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))))` | -3.84 | -3.51 | -3.84 | — | (子树本身) |
| sufficiency | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -3.84 | -3.51 | -3.84 | — | (子树本身) |
| knockout | `create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0)` | -2.78 | -2.78 | -1.98 | +0.05 | `rank(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), True)` |
| knockout | `abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))))` | -2.78 | -2.78 | -1.98 | +0.05 | `rank(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), create_valid_mask(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 0), True)` |
| knockout | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -3.71 | -3.53 | -3.71 | +0.99 | `rank(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0), True)` |
| knockout | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -2.78 | -2.78 | -1.98 | +0.05 | `rank(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), create_valid_mask(abs_(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 0), True)` |
| swap | `Volume->Amt` | -2.83 | -2.83 | -1.97 | — | `rank(div(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), create_valid_mask(abs_(div(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))), 0), True)` |

### head score -2.82:`sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20)` | -2.98 | -2.98 | -1.91 | — | (子树本身) |
| sufficiency | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -3.84 | -3.51 | -3.84 | — | (子树本身) |
| sufficiency | `ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20)` | -4.43 | -3.94 | -4.43 | — | (子树本身) |
| sufficiency | `add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))` | -3.43 | -2.98 | -3.43 | — | (子树本身) |
| knockout | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20)` | -3.62 | -3.62 | -2.39 | +0.81 | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20), div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))))` |
| knockout | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -4.36 | -3.80 | -4.36 | +1.55 | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20), ts_mean(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 20))` |
| knockout | `ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20)` | -3.06 | -3.06 | -1.89 | +0.24 | `sub(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))` |
| knockout | `add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))` | -2.77 | -2.77 | -1.85 | -0.04 | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 20), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)))), 20))` |
| swap | `Volume->Amt` | -2.76 | -2.76 | -1.81 | — | `sub(ts_mean(div(day_max(in_slice(Amt, 11, 240)), add(day_sum(in_slice(Amt, 11, 240)), create_like(day_sum(in_slice(Amt, 11, 240)), 1e-06))), 20), ts_mean(div(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))` |
| window | `ts_mean@20->10` | -2.87 | -2.87 | -1.82 | — | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 10), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))` |
| window | `ts_mean@20->40` | -2.73 | -2.73 | -1.89 | — | `sub(ts_mean(div(day_max(in_slice(Volume, 11, 240)), add(day_sum(in_slice(Volume, 11, 240)), create_like(day_sum(in_slice(Volume, 11, 240)), 1e-06))), 40), ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20))` |

### head score -2.97:`ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -3.84 | -3.51 | -3.84 | — | (子树本身) |
| sufficiency | `add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))` | -3.43 | -2.98 | -3.43 | — | (子树本身) |
| sufficiency | `create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)))` | -3.43 | -2.98 | -3.43 | — | (子树本身) |
| knockout | `div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)))` | -3.30 | -3.08 | -3.30 | +0.33 | `ts_mean(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 20)` |
| knockout | `add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))` | -3.39 | -3.04 | -3.39 | +0.42 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)))), 20)` |
| knockout | `create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06)` | -3.39 | -3.04 | -3.39 | +0.42 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))))), 20)` |
| swap | `Volume->Amt` | -3.00 | -3.00 | -1.89 | — | `ts_mean(div(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 20)` |
| window | `ts_mean@20->10` | -3.08 | -3.08 | -2.10 | — | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 10)` |
| window | `ts_mean@20->40` | -3.39 | -2.92 | -3.39 | — | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), add(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), create_like(day_mean(abs_(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))), 1e-06))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20)` — enrichment,均值差 +1.50,p 0.000
2. `cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60)` — enrichment,均值差 +1.38,p 0.000
3. `day_std(in_slice(Ret, 11, 230))` — enrichment,均值差 +1.15,p 0.000
4. `day_signed_ratio(Open, High)` — enrichment,均值差 +0.78,p 0.007
5. `cs_bucket_rank(LogFloatShares, cross_autocorr(day_sum(in_slice(Ret, 11, 230)), 120, 1))` — enrichment,均值差 +0.76,p 0.069
6. `cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, High))` — enrichment,均值差 +0.76,p 0.011
7. `ts_argmin(day_sum(in_slice(Ret, 11, 230)), 30)` — enrichment,均值差 +0.76,p 0.084
8. `sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1))` — enrichment,均值差 +0.74,p 0.043
9. `day_sum(in_slice(Ret, 11, 230))` — enrichment,均值差 +0.62,p 0.046

## 本组之前各轮的任务

- `prods2027Pr1a_Ea`:核心 `day_q_stat_std(in_slice(Ret, 11, 230), 10)`;评分 69,过线 0,入 heads 0;采样计数 {'c05_no_core': 713, 'c05_skeleton': 377}
  - score -0.42(train -0.14 valid -0.42):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 60), 20), 120)`
  - score -0.66(train -0.45 valid -0.66):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120)`
  - score -0.66(train -0.56 valid -0.66):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), 60), 20), 120)`
  - score -0.71(train -0.55 valid -0.71):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_autocorr(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60, 1), 120)`
  - score -0.89(train -0.89 valid -0.86):`cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_regbeta(day_std(in_slice(Ret, 11, 230)), cross_ema(cross_zscore(day_q_stat_std(in_slice(Ret, 11, 230), 10), 60), 20), 120), 120)`
- `prods2027Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -1.03(train -0.68 valid -1.03):`cross_autocorr(day_sum(in_slice(Amt, 11, 230)), 120, 1)`
  - score -1.34(train -1.20 valid -1.34):`signedpower(sub(cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, High)), ts_argmin(cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1)), 60), 30)))`
  - score -1.37(train -1.37 valid -1.30):`cross_autocorr(signedpower(sub(cs_bucket_rank(LogFloatShares, signedpower(day_argmax(Ret))), ts_argmin(cross_ema(sub(day_autocorr(mul(in_slice(Ret, 11, 60), 100), 1), day_autocorr(mul(in_slice(Ret, 121, 230), 100), 1)), 5), 30))), 120, 1)`
  - score -1.44(train -1.44 valid -1.31):`signedpower(sub(cs_bucket_rank(LogFloatShares, day_signed_ratio(High, High)), ts_argmin(cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, High)), 30)))`
  - score -1.48(train -1.07 valid -1.48):`signedpower(sub(cs_bucket_rank(LogFloatShares, day_signed_ratio(Open, Ret)), ts_argmin(day_sum(in_slice(Ret, 11, 230)), 30)))`

## 比原 head 好的拆解变体(R 候选)

(没有)
