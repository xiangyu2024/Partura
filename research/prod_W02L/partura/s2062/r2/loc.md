# 定位:种子 2062,P 组,第 2 轮(只含 train / valid)

快照:prods2062M1_I0_open_search, prods2062M2_I0_open_search, prods2062Pr1a_I0_open_search, prods2062Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.74 | -1.35 | -1.74 | -1 | 20 | prods2062M1_I0_open_search | `ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)` |
| -3.34 | -3.34 | -2.86 | -1 | 20 | prods2062M2_I0_open_search | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False), 20)` |
| -3.34 | -3.34 | -2.86 | -1 | 20 | prods2062M2_I0_open_search | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'), 20)` |
| -3.63 | -3.63 | -3.13 | -1 | 20 | prods2062M2_I0_open_search | `day_pdf_tail_sum_m(Ret, Volume, 50, False)` |
| -3.86 | -2.54 | -3.86 | -1 | 20 | prods2062M1_I0_open_search | `ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)` |
| -4.22 | -4.22 | -2.85 | -1 | 20 | prods2062M1_I0_open_search | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0), True)` |

## 共性:103 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.95 | 0.000 | 7 | -1.04 / -2.99 | `day_median(Amt)` |
| +1.85 | 0.009 | 4 | -1.09 / -2.93 | `cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30)` |
| +1.79 | 0.002 | 6 | -1.18 / -2.97 | `ts_stddev(day_flat_run_max(Open), 20)` |
| +1.79 | 0.002 | 6 | -1.18 / -2.97 | `day_flat_run_max(Open)` |
| +1.71 | 0.000 | 21 | -1.50 / -3.21 | `day_at_max_ratio(Vwap)` |
| +1.62 | 0.000 | 20 | -1.56 / -3.18 | `inv(day_at_max_ratio(Vwap))` |
| +1.39 | 0.001 | 9 | -1.59 / -2.98 | `ts_stddev(day_autocorr_n1(Ret), 20)` |
| +1.32 | 0.001 | 10 | -1.67 / -2.99 | `day_autocorr_n1(Ret)` |
| +1.00 | 0.041 | 6 | -1.92 / -2.92 | `day_min(cross_scale(Ret, 3))` |
| +0.82 | 0.082 | 11 | -2.13 / -2.95 | `ts_stddev(day_flat_run_max(High), 20)` |
| +0.82 | 0.082 | 11 | -2.13 / -2.95 | `day_flat_run_max(High)` |
| +0.82 | 0.139 | 4 | -2.08 / -2.89 | `day_wmean(Ret, Close)` |
| +0.80 | 0.103 | 5 | -2.10 / -2.90 | `day_at_min_ratio(Amt)` |
| +0.66 | 0.221 | 6 | -2.24 / -2.90 | `day_last(Low)` |
| +0.52 | 0.392 | 6 | -2.37 / -2.89 | `cross_autocorr_s1(cs_last_high40(ListAge, day_topw_mean(Open, Ret)), 5)` |
| +0.52 | 0.392 | 6 | -2.37 / -2.89 | `cs_last_high40(ListAge, day_topw_mean(Open, Ret))` |
| +0.47 | 0.412 | 5 | -2.41 / -2.89 | `inv(cross_autocorr_s1(cs_last_high40(ListAge, day_topw_mean(Open, Ret)), 5))` |
| +0.34 | 0.434 | 11 | -2.56 / -2.90 | `day_topw_mean(Open, Ret)` |

## 拆解(9 次评估)

### head score -3.34:`cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_tail_sum_m(Ret, Volume, 50, False)` | -3.63 | -3.63 | -3.24 | — | (子树本身) |
| swap | `Volume->Amt` | -3.39 | -3.39 | -3.02 | — | `cross_mean(day_pdf_tail_sum_m(Ret, Amt, 50, False), 20)` |
| window | `cross_mean@20->10` | -3.45 | -3.45 | -2.87 | — | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False), 10)` |
| window | `cross_mean@20->40` | -2.97 | -2.97 | -2.84 | — | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False), 40)` |

### head score -3.34:`cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank')` | -3.63 | -3.63 | -3.24 | — | (子树本身) |
| swap | `Volume->Amt` | -3.39 | -3.39 | -3.02 | — | `cross_mean(day_pdf_tail_sum_m(Ret, Amt, 50, False, 'rank'), 20)` |
| window | `cross_mean@20->10` | -3.45 | -3.45 | -2.87 | — | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'), 10)` |
| window | `cross_mean@20->40` | -2.97 | -2.97 | -2.84 | — | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'), 40)` |

### head score -3.63:`day_pdf_tail_sum_m(Ret, Volume, 50, False)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.59 | -3.59 | -3.21 | — | `day_pdf_tail_sum_m(Ret, Amt, 50, False)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_median(Amt)` — enrichment,均值差 +1.95,p 0.000
2. `cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30)` — enrichment,均值差 +1.85,p 0.009
3. `ts_stddev(day_flat_run_max(Open), 20)` — enrichment,均值差 +1.79,p 0.002
4. `day_flat_run_max(Open)` — enrichment,均值差 +1.79,p 0.002
5. `day_at_max_ratio(Vwap)` — enrichment,均值差 +1.71,p 0.000
6. `inv(day_at_max_ratio(Vwap))` — enrichment,均值差 +1.62,p 0.000
7. `ts_stddev(day_autocorr_n1(Ret), 20)` — enrichment,均值差 +1.39,p 0.001
8. `day_autocorr_n1(Ret)` — enrichment,均值差 +1.32,p 0.001
9. `day_min(cross_scale(Ret, 3))` — enrichment,均值差 +1.00,p 0.041
10. `ts_stddev(day_flat_run_max(High), 20)` — enrichment,均值差 +0.82,p 0.082
11. `day_flat_run_max(High)` — enrichment,均值差 +0.82,p 0.082

## 本组之前各轮的任务

- `prods2062Pr1a_I0_open_search`:核心 `—`;评分 98,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.32(train +0.32 valid +0.54):`cross_regbeta(day_median(Amt), inv(cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30)), 241)`
  - score +0.14(train +0.14 valid +0.39):`cross_regbeta(day_median(Amt), cross_regbeta(day_median(Amt), LogFloatShares, 241), 241)`
  - score -0.49(train +0.22 valid -0.49):`cross_regbeta(day_median(Amt), day_at_max_ratio(Vwap), 241)`
  - score -0.52(train -0.52 valid +0.04):`pow_05(cross_regalpha(inv(day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap), 60))`
  - score -0.87(train -0.87 valid -0.65):`inv(cross_regalpha(inv(day_at_max_ratio(Vwap)), ts_stddev(day_flat_run_max(Open), 20), 30))`
- `prods2062Pr1b_Nb`:核心 `—`;评分 57,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -1.51(train -1.51 valid -1.39):`add(day_min(cross_scale(Ret, 5)), day_min(cross_scale(Ret, 3)))`
  - score -1.69(train -1.54 valid -1.69):`add(day_min(cross_scale(Ret, 5)), day_wmean(Ret, Close))`
  - score -1.70(train -1.53 valid -1.70):`add(day_min(cross_scale(Ret, 5)), day_quantile(Ret))`
  - score -1.86(train -1.86 valid -1.37):`add(day_min(cross_scale(Ret, 3)), day_quantile(Vwap))`
  - score -1.94(train -1.94 valid -1.73):`add(day_min(cross_scale(Ret, 10)), day_quantile(Vwap))`

## 比原 head 好的拆解变体(R 候选)

(没有)
