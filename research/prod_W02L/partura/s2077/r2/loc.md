# 定位:种子 2077,P 组,第 2 轮(只含 train / valid)

快照:prods2077M1_I0_open_search, prods2077M2_I0_open_search, prods2077Pr1a_Ea, prods2077Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.02 | -0.22 | -1.02 | -1 | 5 | prods2077M1_I0_open_search | `day_median(div(abs_(Ret), Amt))` |
| -1.12 | -0.87 | -1.12 | -1 | 20 | prods2077M1_I0_open_search | `day_open(in_delta(Volume, 60))` |
| -1.16 | -1.16 | -1.11 | -1 | 5 | prods2077M2_I0_open_search | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), neg(in_slice(Ret, 1, 50)), 0), select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` |
| -1.16 | -1.16 | -1.14 | -1 | 5 | prods2077M2_I0_open_search | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` |
| -1.21 | -1.21 | -1.10 | -1 | 5 | prods2077M2_I0_open_search | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), neg(in_slice(Ret, 1, 20)), 0), select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), in_slice(Volume, 1, 20), create_like(in_slice(Ret, 1, 20), 0))), in_sum(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0)))))` |
| -1.63 | -1.39 | -1.63 | -1 | 20 | prods2077M1_I0_open_search | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))` |

## 共性:192 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.40 | 0.001 | 11 | -1.59 / -2.99 | `day_sum(Ret)` |
| +1.37 | 0.000 | 21 | -1.69 / -3.06 | `day_zero_ratio(Low)` |
| +1.26 | 0.007 | 5 | -1.68 / -2.94 | `ts_scale(day_zero_ratio(Low), 30)` |
| +1.25 | 0.000 | 14 | -1.75 / -3.00 | `ts_scale(cross_delta(day_zero_ratio(Low), 30), 30)` |
| +1.24 | 0.000 | 15 | -1.77 / -3.01 | `cross_delta(day_zero_ratio(Low), 30)` |
| +0.98 | 0.000 | 32 | -2.10 / -3.07 | `day_median(div(abs_(Ret), Amt))` |
| +0.94 | 0.071 | 4 | -1.99 / -2.93 | `day_argmin(pow_1_5(Open))` |
| +0.83 | 0.077 | 4 | -2.09 / -2.93 | `day_gini(sqrt(Volume))` |
| +0.76 | 0.102 | 4 | -2.17 / -2.93 | `day_argmax(Vwap)` |
| +0.76 | 0.102 | 4 | -2.17 / -2.93 | `cross_rank(day_argmax(Vwap), 241)` |
| +0.72 | 0.052 | 7 | -2.22 / -2.94 | `day_argmin(Low)` |
| +0.65 | 0.141 | 4 | -2.27 / -2.92 | `pow_3(cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(pow_1_5(Vwap))))` |
| +0.65 | 0.141 | 4 | -2.27 / -2.92 | `cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(pow_1_5(Vwap)))` |
| +0.41 | 0.264 | 4 | -2.51 / -2.92 | `day_sum(abs_(Ret))` |
| +0.33 | 0.178 | 8 | -2.59 / -2.92 | `day_argmin(pow_1_5(Vwap))` |
| +0.27 | 0.284 | 5 | -2.65 / -2.92 | `day_sum(Volume)` |
| +0.21 | 0.239 | 11 | -2.71 / -2.92 | `day_kurt(Amt)` |
| +0.11 | 0.444 | 4 | -2.80 / -2.91 | `day_topw_mean(Low, Low)` |
| -0.23 | 0.651 | 9 | -3.13 / -2.90 | `day_sum(Amt)` |
| -1.07 | 0.982 | 5 | -3.95 / -2.88 | `create_like(in_slice(Close, 1, 1), 1)` |

## 拆解(3 次评估)

### head score -1.16:`day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), neg(in_slice(Ret, 1, 50)), 0), select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -2.58 | -2.58 | -2.28 | — | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), neg(in_slice(Ret, 1, 50)), 0), select_where(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Amt, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_lt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` |

### head score -1.16:`day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.07 | -3.07 | -1.94 | — | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Amt, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` |

### head score -1.21:`day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), neg(in_slice(Ret, 1, 20)), 0), select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), in_slice(Volume, 1, 20), create_like(in_slice(Ret, 1, 20), 0))), in_sum(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -2.37 | -2.37 | -1.99 | — | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), neg(in_slice(Ret, 1, 20)), 0), select_where(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0), False), in_slice(Amt, 1, 20), create_like(in_slice(Ret, 1, 20), 0))), in_sum(is_lt(in_slice(Ret, 1, 20), create_like(in_slice(Ret, 1, 20), 0)))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_sum(Ret)` — enrichment,均值差 +1.40,p 0.001
2. `day_zero_ratio(Low)` — enrichment,均值差 +1.37,p 0.000
3. `ts_scale(day_zero_ratio(Low), 30)` — enrichment,均值差 +1.26,p 0.007
4. `ts_scale(cross_delta(day_zero_ratio(Low), 30), 30)` — enrichment,均值差 +1.25,p 0.000
5. `cross_delta(day_zero_ratio(Low), 30)` — enrichment,均值差 +1.24,p 0.000
6. `day_median(div(abs_(Ret), Amt))` — enrichment,均值差 +0.98,p 0.000
7. `day_argmin(pow_1_5(Open))` — enrichment,均值差 +0.94,p 0.071
8. `day_gini(sqrt(Volume))` — enrichment,均值差 +0.83,p 0.077
9. `day_argmin(Low)` — enrichment,均值差 +0.72,p 0.052

## 本组之前各轮的任务

- `prods2077Pr1a_Ea`:核心 `day_median(div(abs_(Ret), Amt))`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1086, 'c05_no_core': 2099}
  - score +0.34(train +0.71 valid +0.34):`cross_corr(day_median(div(abs_(Ret), Amt)), cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 20), 20)`
  - score -0.23(train -0.23 valid -0.03):`cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 20)`
  - score -0.45(train -0.45 valid +0.23):`cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 30)`
  - score -0.77(train -0.50 valid -0.77):`cross_corr(day_median(div(abs_(Ret), Amt)), cs_last_low20(pow_3(sigmoid(BoardCode)), pow_2_5(ts_mean(day_centroid(Low), 5))), 20)`
  - score -0.98(train -0.98 valid -0.54):`cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 10)`
- `prods2077Pr1b_Nb`:核心 `—`;评分 97,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.62(train -0.46 valid -0.62):`cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 10), 30), day_mean(pow_2_5(Ret)))`
  - score -0.63(train -0.39 valid -0.63):`cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_mean(pow_2_5(Ret)))`
  - score -0.99(train -0.49 valid -0.99):`cs_last_high10(pow_3(cs_last_high20(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(pow_1_5(Vwap)))), day_gini(mul(High, Open)))`
  - score -1.13(train -0.63 valid -1.13):`cs_last_high10(pow_3(cs_last_high40(ts_scale(cross_delta(day_zero_ratio(Low), 30), 30), day_argmin(Low))), day_gini(Low))`
  - score -1.43(train -1.43 valid -1.41):`cs_last_high20(ts_scale(day_zero_ratio(Low), 30), day_argmin(pow_1_5(Open)))`

## 比原 head 好的拆解变体(R 候选)

(没有)
