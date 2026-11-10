# 定位:种子 2039,P 组,第 2 轮(只含 train / valid)

快照:prods2039M1_I0_open_search, prods2039M2_I0_open_search, prods2039Pr1a_Ea, prods2039Pr1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.07 | -1.01 | -1.07 | -1 | 20 | prods2039M2_I0_open_search | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50)))` |
| -1.41 | -1.41 | -0.74 | +1 | 20 | prods2039M2_I0_open_search | `day_first(cross_sum(log(Amt), 3))` |
| -1.41 | -1.41 | -0.74 | +1 | 20 | prods2039M2_I0_open_search | `day_open(cross_sum(log(Amt), 3))` |
| -1.76 | -1.13 | -1.76 | -1 | 0 | prods2039M1_I0_open_search | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40)` |
| -1.85 | -1.85 | -1.64 | +1 | 0 | prods2039M1_I0_open_search | `cross_ema(pow_05(day_autocorr_n1(Close)), 120)` |
| -2.21 | -2.21 | -2.01 | +1 | 20 | prods2039M1_I0_open_search | `ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 40)` |

## 共性:147 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.14 | 0.013 | 5 | -1.62 / -2.76 | `abs_(abs_(day_distinct_ratio(High)))` |
| +1.01 | 0.000 | 21 | -1.86 / -2.86 | `day_distinct_ratio(High)` |
| +0.93 | 0.000 | 17 | -1.90 / -2.83 | `abs_(day_distinct_ratio(High))` |
| +0.91 | 0.006 | 6 | -1.85 / -2.76 | `cs_last_low40(pow_05(BoardCode), ts_quantile_q75(day_autocorr_n1(Close), 50))` |
| +0.89 | 0.023 | 4 | -1.86 / -2.74 | `replace_small_with_nan(day_autocorr_n1(Close))` |
| +0.79 | 0.002 | 12 | -1.99 / -2.78 | `ts_quantile_q75(day_autocorr_n1(Close), 50)` |
| +0.79 | 0.006 | 9 | -1.98 / -2.77 | `day_mean(Ret)` |
| +0.71 | 0.007 | 15 | -2.08 / -2.79 | `cross_decay_linear(day_close(High), 10)` |
| +0.66 | 0.064 | 5 | -2.08 / -2.74 | `day_es_ratio_hi(Volume)` |
| +0.64 | 0.007 | 21 | -2.17 / -2.81 | `day_close(High)` |
| +0.58 | 0.018 | 14 | -2.19 / -2.78 | `pow_05(BoardCode)` |
| +0.58 | 0.020 | 15 | -2.20 / -2.78 | `day_flat_ratio(Low)` |
| +0.45 | 0.050 | 13 | -2.31 / -2.76 | `day_flat_ratio(Close)` |
| +0.42 | 0.065 | 11 | -2.33 / -2.75 | `replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95))` |
| +0.42 | 0.065 | 11 | -2.33 / -2.75 | `is_lt(day_flat_ratio(Close), 0.95)` |
| +0.42 | 0.065 | 11 | -2.33 / -2.75 | `mul(day_autocorr_n1(Close), replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95)))` |
| +0.33 | 0.315 | 5 | -2.40 / -2.73 | `day_var(Ret)` |
| +0.07 | 0.096 | 49 | -2.67 / -2.74 | `day_autocorr_n1(Close)` |
| -0.19 | 0.814 | 4 | -2.90 / -2.71 | `day_max(Ret)` |
| -0.21 | 0.403 | 5 | -2.93 / -2.71 | `day_quantile_q75(cross_sum(log(Amt), 3))` |

## 拆解(24 次评估)

### head score -1.07:`sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50))` | -1.05 | -1.01 | -1.05 | — | (子树本身) |
| sufficiency | `ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50)` | -5.85 | -4.53 | -5.85 | — | (子树本身) |
| sufficiency | `day_quantile_q75(cross_sum(log(Amt), 3))` | -4.19 | -3.36 | -4.19 | — | (子树本身) |
| sufficiency | `day_last(cross_sum(Amt, 3))` | -4.02 | -3.13 | -4.02 | — | (子树本身) |
| knockout | `abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50))` | -5.85 | -4.53 | -5.85 | +4.78 | `sub(0.5, ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50))` |
| knockout | `ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 50)` | -4.19 | -3.36 | -4.19 | +3.12 | `sub(0.5, abs_(day_quantile_q75(cross_sum(log(Amt), 3))))` |
| swap | `Amt->Volume` | -1.71 | -1.39 | -1.71 | — | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Volume), 3)), day_last(cross_sum(Volume, 3)), 50)))` |
| window | `ts_regres@50->25` | -2.41 | -2.41 | -1.41 | — | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 25)))` |
| window | `ts_regres@50->100` | -0.55 | -0.21 | -0.55 | — | `sub(0.5, abs_(ts_regres(day_quantile_q75(cross_sum(log(Amt), 3)), day_last(cross_sum(Amt, 3)), 100)))` |

### head score -1.41:`day_first(cross_sum(log(Amt), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -2.33 | -1.09 | -2.33 | — | `day_first(cross_sum(log(Volume), 3))` |
| window | `cross_sum@3->2` | -1.29 | -1.29 | -0.66 | — | `day_first(cross_sum(log(Amt), 2))` |
| window | `cross_sum@3->6` | -1.36 | -1.36 | -0.39 | — | `day_first(cross_sum(log(Amt), 6))` |

### head score -1.41:`day_open(cross_sum(log(Amt), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -2.33 | -1.09 | -2.33 | — | `day_open(cross_sum(log(Volume), 3))` |
| window | `cross_sum@3->2` | -1.29 | -1.29 | -0.66 | — | `day_open(cross_sum(log(Amt), 2))` |
| window | `cross_sum@3->6` | -1.36 | -1.36 | -0.39 | — | `day_open(cross_sum(log(Amt), 6))` |

### head score -1.76:`ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10)` | -3.03 | -2.58 | -3.03 | — | (子树本身) |
| sufficiency | `inv(ts_std(day_autocorr_n1(Ret), 10))` | -2.64 | -2.64 | -2.53 | — | (子树本身) |
| sufficiency | `ts_std(day_autocorr_n1(Ret), 10)` | -2.68 | -2.66 | -2.68 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Ret)` | -3.69 | -3.50 | -3.69 | — | (子树本身) |
| knockout | `ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10)` | -2.10 | -1.15 | -2.10 | +0.33 | `ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 40)` |
| knockout | `inv(ts_std(day_autocorr_n1(Ret), 10))` | -3.53 | -3.31 | -3.53 | +1.77 | `ts_min(ts_min(ts_std(day_autocorr_n1(Ret), 10), 10), 40)` |
| knockout | `ts_std(day_autocorr_n1(Ret), 10)` | -2.64 | -2.22 | -2.64 | +0.87 | `ts_min(ts_min(inv(day_autocorr_n1(Ret)), 10), 40)` |
| window | `ts_min@40->20` | -1.88 | -1.69 | -1.88 | — | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 20)` |
| window | `ts_min@40->80` | -1.75 | -0.81 | -1.75 | — | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `abs_(abs_(day_distinct_ratio(High)))` — enrichment,均值差 +1.14,p 0.013
2. `day_distinct_ratio(High)` — enrichment,均值差 +1.01,p 0.000
3. `abs_(day_distinct_ratio(High))` — enrichment,均值差 +0.93,p 0.000
4. `cs_last_low40(pow_05(BoardCode), ts_quantile_q75(day_autocorr_n1(Close), 50))` — enrichment,均值差 +0.91,p 0.006
5. `replace_small_with_nan(day_autocorr_n1(Close))` — enrichment,均值差 +0.89,p 0.023
6. `ts_quantile_q75(day_autocorr_n1(Close), 50)` — enrichment,均值差 +0.79,p 0.002
7. `day_mean(Ret)` — enrichment,均值差 +0.79,p 0.006
8. `cross_decay_linear(day_close(High), 10)` — enrichment,均值差 +0.71,p 0.007
9. `day_es_ratio_hi(Volume)` — enrichment,均值差 +0.66,p 0.064
10. `day_close(High)` — enrichment,均值差 +0.64,p 0.007
11. `pow_05(BoardCode)` — enrichment,均值差 +0.58,p 0.018
12. `day_flat_ratio(Low)` — enrichment,均值差 +0.58,p 0.020
13. `day_flat_ratio(Close)` — enrichment,均值差 +0.45,p 0.050
14. `replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95))` — enrichment,均值差 +0.42,p 0.065
15. `is_lt(day_flat_ratio(Close), 0.95)` — enrichment,均值差 +0.42,p 0.065
16. `mul(day_autocorr_n1(Close), replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95)))` — enrichment,均值差 +0.42,p 0.065
17. `day_autocorr_n1(Close)` — enrichment,均值差 +0.07,p 0.096

## 本组之前各轮的任务

- `prods2039Pr1a_Ea`:核心 `day_autocorr_n1(Close)`;评分 103,过线 0,入 heads 0;采样计数 {'c05_no_core': 1927, 'c05_skeleton': 955}
  - score -1.48(train -1.48 valid -1.33):`cross_corr(mul(day_autocorr_n1(Close), replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95))), day_mean(Ret), 120)`
  - score -1.53(train -1.53 valid -1.26):`cross_corr(mul(mul(day_autocorr_n1(Close), replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95))), replace_small_with_nan(is_lt(day_flat_ratio(Close), 0.95))), day_mean(Ret), 60)`
  - score -1.63(train -1.63 valid -1.60):`cross_corr(mul(mul(day_autocorr_n1(Close), replace_small_with_nan(day_autocorr_n1(Close))), replace_small_with_nan(day_autocorr_n1(Close))), day_mean(Ret), 60)`
  - score -1.65(train -1.65 valid -1.57):`cross_corr(mul(add(day_autocorr_n1(Close), replace_small_with_nan(day_autocorr_n1(Close))), replace_small_with_nan(day_autocorr_n1(Close))), day_mean(Ret), 60)`
  - score -1.65(train -1.65 valid -1.61):`cross_corr(mul(mul(day_autocorr_n1(Close), replace_small_with_nan(day_autocorr_n1(Close))), ts_quantile_q75(day_autocorr_n1(Close), 50)), day_mean(Ret), 60)`
- `prods2039Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score -0.50(train -0.32 valid -0.50):`cross_corr(cross_decay_linear(day_at_max_ratio(High), 10), abs_(abs_(day_distinct_ratio(High))), 60)`
  - score -1.18(train -1.13 valid -1.18):`cross_corr(cross_decay_linear(day_close(High), 10), abs_(day_distinct_ratio(High)), 60)`
  - score -1.18(train -1.13 valid -1.18):`cross_corr(cross_decay_linear(day_close(High), 10), abs_(abs_(day_distinct_ratio(High))), 60)`
  - score -1.18(train -1.13 valid -1.18):`cross_corr(cross_decay_linear(day_close(High), 10), day_distinct_ratio(High), 60)`
  - score -1.46(train -0.94 valid -1.46):`abs_(cross_corr(cross_decay_linear(day_close(High), 10), abs_(day_distinct_ratio(High)), 60))`

## 比原 head 好的拆解变体(R 候选)

(没有)
