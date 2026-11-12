# 定位:种子 2055,P 组,第 3 轮(只含 train / valid)

快照:prods2055M1_I0_open_search, prods2055M2_I0_open_search, prods2055M3_I0_open_search, prods2055Pr1a_Na, prods2055Pr2a_Ea, prods2055Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.94 | -0.76 | -0.94 | +1 | 5 | prods2055M1_I0_open_search | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` |
| -1.03 | -1.03 | -0.57 | -1 | 0 | prods2055M3_I0_open_search | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241))` |
| -1.22 | -1.22 | -0.70 | +1 | 0 | prods2055M3_I0_open_search | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241), 50)` |
| -1.71 | -1.71 | -1.70 | +1 | 5 | prods2055M3_I0_open_search | `ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10), 50), 50)` |
| -1.82 | -1.78 | -1.82 | +1 | 5 | prods2055M2_I0_open_search | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` |
| -1.83 | -1.62 | -1.83 | +1 | 5 | prods2055M1_I0_open_search | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))), 30)` |
| -1.89 | -0.98 | -1.89 | +1 | 5 | prods2055M1_I0_open_search | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` |
| -1.94 | -1.76 | -1.94 | -1 | 20 | prods2055M2_I0_open_search | `ts_std(day_last(pow_2_5(nt_ts_var(Low, 3))), 50)` |
| -2.02 | -2.02 | -1.62 | +1 | 5 | prods2055M2_I0_open_search | `ts_std(neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)), 50)` |

## 共性:173 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.24 | 0.005 | 6 | -1.24 / -2.48 | `day_wmean(Ret, in_pct(Amt, 1))` |
| +1.21 | 0.009 | 4 | -1.25 / -2.46 | `day_flat_run_max(High)` |
| +1.05 | 0.010 | 5 | -1.41 / -2.46 | `pow_05(day_flat_run_max(Ret))` |
| +0.82 | 0.011 | 10 | -1.66 / -2.48 | `day_kurt(in_autocorr(Ret, 10, 1))` |
| +0.81 | 0.012 | 9 | -1.67 / -2.47 | `day_flat_run_max(Ret)` |
| +0.67 | 0.118 | 4 | -1.78 / -2.45 | `day_quantile(High)` |
| +0.64 | 0.005 | 15 | -1.85 / -2.49 | `cross_product(day_argmax(Amt), 10)` |
| +0.47 | 0.284 | 4 | -1.97 / -2.44 | `day_kurt(in_autocorr(in_pct(Vwap, 1), 10, 1))` |
| +0.39 | 0.101 | 8 | -2.06 / -2.45 | `day_argmax(High)` |
| +0.37 | 0.317 | 6 | -2.08 / -2.45 | `ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10)` |
| +0.28 | 0.466 | 4 | -2.16 / -2.44 | `day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3))))` |
| +0.26 | 0.474 | 11 | -2.19 / -2.45 | `day_var(pow_2_5(nt_ts_var(Low, 3)))` |
| +0.12 | 0.521 | 6 | -2.32 / -2.44 | `day_signed_ratio(Ret, Amt)` |
| +0.10 | 0.518 | 4 | -2.34 / -2.43 | `sqrt(day_argmax(Amt))` |
| +0.08 | 0.711 | 5 | -2.35 / -2.44 | `sigmoid(pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))))))` |
| +0.08 | 0.711 | 5 | -2.35 / -2.44 | `sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))))` |
| +0.08 | 0.711 | 5 | -2.35 / -2.44 | `pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))` |
| +0.08 | 0.695 | 4 | -2.35 / -2.43 | `sigmoid(sigmoid(pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))))` |
| +0.03 | 0.049 | 52 | -2.41 / -2.44 | `day_argmax(Amt)` |
| +0.02 | 0.750 | 6 | -2.42 / -2.43 | `day_median(Open)` |

## 拆解(32 次评估)

### head score -1.03:`neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241)` | -1.03 | -1.03 | -0.60 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10)` | -1.96 | -1.95 | -1.96 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(nt_ts_var(Ret, 3)))` | -2.86 | -2.42 | -2.86 | — | (子树本身) |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241)` | -1.96 | -1.95 | -1.96 | +0.93 | `neg(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10))` |
| knockout | `ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10)` | -0.84 | -0.84 | -0.64 | -0.19 | `neg(cross_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 241))` |
| window | `cross_sum@241->120` | -1.13 | -0.51 | -1.13 | — | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 120))` |
| window | `cross_sum@241->482` | -1.57 | -1.57 | -0.99 | — | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 482))` |

### head score -1.22:`ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241)` | -1.03 | -1.03 | -0.60 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10)` | -1.96 | -1.95 | -1.96 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(nt_ts_var(Ret, 3)))` | -2.86 | -2.42 | -2.86 | — | (子树本身) |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241)` | -1.03 | -1.03 | -0.93 | -0.19 | `ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 50)` |
| knockout | `ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10)` | -1.09 | -1.08 | -1.09 | -0.14 | `ts_std(cross_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 241), 50)` |
| window | `ts_std@50->25` | -0.97 | -0.97 | -0.70 | — | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241), 25)` |
| window | `ts_std@50->100` | -2.27 | -1.59 | -2.27 | — | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241), 100)` |

### head score -1.71:`ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10), 50)` | -1.89 | -1.89 | -1.85 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10)` | -2.43 | -1.75 | -2.43 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(nt_ts_var(Low, 3)))` | -2.19 | -1.59 | -2.19 | — | (子树本身) |
| knockout | `ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10)` | -1.72 | -1.67 | -1.72 | +0.01 | `ts_std(ts_std(day_var(pow_2_5(nt_ts_var(Low, 3))), 50), 50)` |
| swap | `Low->High` | -1.94 | -1.79 | -1.94 | — | `ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(High, 3))), 10), 50), 50)` |
| window | `ts_std@50->25` | -1.81 | -1.81 | -1.67 | — | `ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10), 50), 25)` |
| window | `ts_std@50->100` | -1.87 | -1.87 | -1.80 | — | `ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10), 50), 100)` |

### head score -2.02:`ts_std(neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30))` | -2.10 | -2.10 | -1.76 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)` | -2.10 | -2.10 | -1.76 | — | (子树本身) |
| sufficiency | `ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10)` | -2.04 | -2.04 | -1.76 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241)` | -1.98 | -1.98 | -1.72 | — | (子树本身) |
| knockout | `neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30))` | -2.02 | -2.02 | -1.64 | -0.00 | `ts_std(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30), 50)` |
| knockout | `cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)` | -2.19 | -2.19 | -1.74 | +0.17 | `ts_std(neg(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10)), 50)` |
| knockout | `ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10)` | -2.23 | -2.23 | -1.67 | +0.21 | `ts_std(neg(cross_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 30)), 50)` |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241)` | -1.92 | -1.92 | -1.64 | -0.10 | `ts_std(neg(cross_sum(ts_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 10), 30)), 50)` |
| swap | `Low->High` | -2.17 | -2.17 | -1.69 | — | `ts_std(neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(High, 3)))), 10), 241), 10), 30)), 50)` |
| window | `ts_std@50->25` | -2.05 | -2.05 | -1.66 | — | `ts_std(neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)), 25)` |
| window | `ts_std@50->100` | -2.00 | -2.00 | -1.62 | — | `ts_std(neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_wmean(Ret, in_pct(Amt, 1))` — enrichment,均值差 +1.24,p 0.005
2. `day_flat_run_max(High)` — enrichment,均值差 +1.21,p 0.009
3. `pow_05(day_flat_run_max(Ret))` — enrichment,均值差 +1.05,p 0.010
4. `day_kurt(in_autocorr(Ret, 10, 1))` — enrichment,均值差 +0.82,p 0.011
5. `day_flat_run_max(Ret)` — enrichment,均值差 +0.81,p 0.012
6. `cross_product(day_argmax(Amt), 10)` — enrichment,均值差 +0.64,p 0.005
7. `day_argmax(Amt)` — enrichment,均值差 +0.03,p 0.049

## 本组之前各轮的任务

- `prods2055Pr1a_Na`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -1.04(train -1.04 valid -0.92):`ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 30)`
  - score -1.12(train -1.12 valid -0.98):`ts_quantile_q75(ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20), 20)`
  - score -1.14(train -1.01 valid -1.14):`ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 50)`
  - score -1.15(train -1.15 valid -0.54):`ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20)`
  - score -1.26(train -1.06 valid -1.26):`ts_quantile_q75(ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20), 30)`
- `prods2055Pr2a_Ea`:核心 `day_argmax(Amt)`;评分 102,过线 0,入 heads 0;采样计数 {'c05_no_core': 1454, 'c05_skeleton': 714}
  - score -0.69(train -0.69 valid -0.18):`cs_bucket_rank(cross_product(day_argmax(Amt), 10), pow_1_5(day_argmax(High)))`
  - score -0.84(train -0.84 valid -0.68):`cs_bucket_rank(cross_product(day_argmax(Amt), 10), pow_1_5(day_flat_run_max(High)))`
  - score -0.96(train -0.96 valid -0.53):`cs_bucket_rank(cross_product(day_argmax(Amt), 10), day_argmax(Amt))`
  - score -0.97(train -0.97 valid -0.68):`cs_bucket_rank(cross_product(day_argmax(Amt), 5), pow_1_5(day_flat_run_max(High)))`
  - score -0.97(train -0.90 valid -0.97):`cs_bucket_rank(cross_product(day_argmax(Amt), 10), pow_1_5(day_flat_run_max(Ret)))`
- `prods2055Pr2b_Nb`:核心 `—`;评分 80,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.19(train -0.19 valid -0.12):`ts_mean(ts_mean(day_wmean(Ret, Volume), 50), 20)`
  - score -0.35(train -0.35 valid -0.16):`ts_mean(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 20), 20)`
  - score -0.55(train -0.55 valid -0.30):`ts_mean(day_wmean(Ret, in_pct(Volume, 1)), 20)`
  - score -0.59(train -0.59 valid -0.28):`ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 20)`
  - score -0.60(train -0.48 valid -0.60):`ts_sum(ts_mean(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 20), 20), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.25(window ts_std@50->25):`ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241), 25)`
- 增益 +0.19(knockout ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10)):`neg(cross_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 241))`
- 增益 +0.19(knockout cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 241)):`ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10), 50)`
- 增益 +0.14(knockout ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10)):`ts_std(cross_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 241), 50)`
- 增益 +0.10(knockout cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241)):`ts_std(neg(cross_sum(ts_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 10), 30)), 50)`
