# 定位:种子 2063,P 组,第 2 轮(只含 train / valid)

快照:prods2063M1_I0_open_search, prods2063M2_I0_open_search, prods2063Pr1a_Ea, prods2063Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.18 | -1.18 | -1.00 | -1 | 5 | prods2063M1_I0_open_search | `pow_05(day_var(nt_ts_min(Volume, 30)))` |
| -1.33 | -1.33 | -1.26 | +1 | 20 | prods2063M1_I0_open_search | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, Low))` |
| -1.40 | -1.30 | -1.40 | +1 | 5 | prods2063M2_I0_open_search | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)), 20)` |
| -1.54 | -1.54 | -1.53 | +1 | 5 | prods2063M2_I0_open_search | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 30)` |
| -1.77 | -1.77 | -1.05 | -1 | 20 | prods2063M2_I0_open_search | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 20)` |
| -2.02 | -2.02 | -1.53 | -1 | 20 | prods2063M1_I0_open_search | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))` |

## 共性:130 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.13 | 0.000 | 33 | -1.51 / -2.63 | `day_var(Ret)` |
| +1.09 | 0.000 | 25 | -1.47 / -2.56 | `ts_delta(LogFloatShares, 50)` |
| +0.98 | 0.000 | 26 | -1.57 / -2.54 | `day_sum(Open)` |
| +0.91 | 0.036 | 5 | -1.48 / -2.38 | `cs_first_high20(cs_first_high20(day_var(Ret), day_sum(Open)), day_sum(Open))` |
| +0.89 | 0.001 | 17 | -1.58 / -2.46 | `cs_first_high20(day_var(Ret), day_sum(Open))` |
| +0.71 | 0.049 | 6 | -1.67 / -2.38 | `day_signed_ratio(Close, Volume)` |
| +0.71 | 0.049 | 6 | -1.67 / -2.38 | `cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume)))` |
| +0.71 | 0.049 | 6 | -1.67 / -2.38 | `cs_mean(day_signed_ratio(Close, Volume))` |
| +0.63 | 0.053 | 13 | -1.78 / -2.41 | `day_sum(Ret)` |
| +0.58 | 0.169 | 6 | -1.79 / -2.38 | `ts_argmin(sigmoid(day_cov(Ret, Low)), 50)` |
| +0.55 | 0.223 | 4 | -1.82 / -2.37 | `day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5))` |
| +0.49 | 0.187 | 9 | -1.90 / -2.38 | `sigmoid(day_cov(Ret, Low))` |
| +0.41 | 0.283 | 4 | -1.95 / -2.36 | `cs_last_high20(cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume))), ts_delta(LogFloatShares, 50))` |
| +0.31 | 0.208 | 13 | -2.07 / -2.38 | `mul(day_cov(Ret, Low), day_mean(Low))` |
| +0.28 | 0.223 | 11 | -2.09 / -2.37 | `day_sum(Low)` |
| +0.22 | 0.428 | 5 | -2.13 / -2.36 | `div(day_cov(Ret, Low), day_mean(Low))` |
| +0.22 | 0.252 | 24 | -2.17 / -2.39 | `day_mean(Low)` |
| -0.16 | 0.703 | 4 | -2.51 / -2.34 | `cross_corr(mul(day_cov(Ret, Low), day_mean(Low)), day_sum(Low), 60)` |
| -0.35 | 0.925 | 46 | -2.58 / -2.22 | `day_cov(Ret, Low)` |

## 拆解(29 次评估)

### head score -1.40:`ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20))` | -1.66 | -1.66 | -1.46 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)` | -1.66 | -1.66 | -1.47 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20)` | -1.50 | -1.50 | -1.42 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20)` | -1.87 | -1.87 | -1.78 | — | (子树本身) |
| knockout | `log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20))` | -1.40 | -1.28 | -1.40 | -0.00 | `ts_max(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20), 20)` |
| knockout | `ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)` | -1.67 | -1.67 | -1.47 | +0.27 | `ts_max(log(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20)), 20)` |
| swap | `Amt->Volume` | -1.07 | -0.44 | -1.07 | — | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Volume, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)), 20)` |
| swap | `Open->Close` | -1.30 | -1.24 | -1.30 | — | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Close, Vwap, 5)), 20), 20), 20), 20)), 20)` |
| window | `ts_max@20->10` | -1.45 | -1.45 | -1.27 | — | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)), 10)` |
| window | `ts_max@20->40` | -1.16 | -1.00 | -1.16 | — | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)), 40)` |

### head score -1.54:`ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20)` | -1.87 | -1.87 | -1.78 | — | (子树本身) |
| sufficiency | `ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20)` | -2.41 | -2.13 | -2.41 | — | (子树本身) |
| sufficiency | `day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5))` | -3.54 | -3.54 | -2.76 | — | (子树本身) |
| knockout | `ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20)` | -1.63 | -1.49 | -1.63 | +0.09 | `ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 30)` |
| swap | `Amt->Volume` | -0.75 | -0.39 | -0.75 | — | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Volume, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 30)` |
| swap | `Open->Close` | -1.55 | -1.55 | -1.53 | — | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Close, Vwap, 5)), 20), 20), 30)` |
| window | `ts_max@30->15` | -1.61 | -1.61 | -1.49 | — | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 15)` |
| window | `ts_max@30->60` | -1.35 | -1.28 | -1.35 | — | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 60)` |

### head score -1.77:`ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241))` | -1.74 | -1.74 | -1.02 | — | (子树本身) |
| sufficiency | `cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)` | -1.28 | -1.28 | -1.06 | — | (子树本身) |
| sufficiency | `ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20)` | -2.55 | -2.06 | -2.55 | — | (子树本身) |
| sufficiency | `day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5))` | -2.76 | -2.76 | -2.70 | — | (子树本身) |
| knockout | `log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241))` | -1.49 | -1.49 | -1.02 | -0.27 | `ts_max(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241), 20)` |
| knockout | `cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)` | -2.14 | -2.14 | -2.03 | +0.37 | `ts_max(log(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20)), 20)` |
| knockout | `ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20)` | -1.74 | -1.74 | -1.37 | -0.02 | `ts_max(log(cross_regbeta(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), day_var(Low), 241)), 20)` |
| swap | `High->Low` | -1.80 | -1.80 | -1.39 | — | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(Low, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 20)` |
| swap | `Open->Close` | -1.89 | -1.89 | -1.09 | — | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Close, Vwap, 5)), 20), day_var(Low), 241)), 20)` |
| window | `ts_max@20->10` | -1.85 | -1.85 | -1.16 | — | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 10)` |
| window | `ts_max@20->40` | -1.66 | -1.66 | -1.12 | — | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_var(Ret)` — enrichment,均值差 +1.13,p 0.000
2. `ts_delta(LogFloatShares, 50)` — enrichment,均值差 +1.09,p 0.000
3. `day_sum(Open)` — enrichment,均值差 +0.98,p 0.000
4. `cs_first_high20(cs_first_high20(day_var(Ret), day_sum(Open)), day_sum(Open))` — enrichment,均值差 +0.91,p 0.036
5. `cs_first_high20(day_var(Ret), day_sum(Open))` — enrichment,均值差 +0.89,p 0.001
6. `day_signed_ratio(Close, Volume)` — enrichment,均值差 +0.71,p 0.049
7. `cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume)))` — enrichment,均值差 +0.71,p 0.049
8. `cs_mean(day_signed_ratio(Close, Volume))` — enrichment,均值差 +0.71,p 0.049
9. `day_sum(Ret)` — enrichment,均值差 +0.63,p 0.053

## 本组之前各轮的任务

- `prods2063Pr1a_Ea`:核心 `day_cov(Ret, Low)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 778, 'c05_no_core': 1454}
  - score -0.42(train -0.42 valid +0.18):`cross_corr(div(ts_argmin(sigmoid(day_cov(Ret, Low)), 50), day_mean(Low)), day_at_max_ratio(Low), 60)`
  - score -0.50(train -0.50 valid +0.07):`cross_corr(mul(day_cov(Ret, Low), day_at_max_ratio(Low)), day_sum(Ret), 60)`
  - score -0.72(train -0.19 valid -0.72):`cross_corr(div(ts_argmin(sigmoid(day_cov(Ret, Low)), 50), day_mean(Low)), day_sum(Ret), 60)`
  - score -0.75(train -0.75 valid -0.60):`cross_corr(mul(day_cov(Ret, Low), day_mean(Low)), cross_corr(mul(day_cov(Ret, Low), day_at_max_ratio(Low)), day_sum(Ret), 60), 60)`
  - score -0.98(train -0.98 valid -0.98):`cross_corr(mul(mul(day_cov(Ret, Low), day_mean(Low)), day_mean(Low)), day_sum(Low), 60)`
- `prods2063Pr1b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 11}
  - score -0.96(train -0.84 valid -0.96):`cs_last_high20(cs_first_high20(day_var(Ret), day_sum(Open)), LogFloatShares)`
  - score -0.99(train -0.86 valid -0.99):`cs_last_high20(cs_first_high20(day_var(Ret), day_first(Open)), LogFloatShares)`
  - score -1.10(train -1.10 valid +0.04):`cs_last_high20(cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume))), ts_delta(LogFloatShares, 50))`
  - score -1.10(train -1.10 valid +0.04):`cs_last_high20(cs_first_high20(day_var(Ret), ts_delta(LogFloatShares, 50)), ts_delta(LogFloatShares, 50))`
  - score -1.10(train -1.10 valid +0.04):`cs_last_high20(cs_first_high20(cs_first_high20(day_var(Ret), day_var(Ret)), day_var(Ret)), ts_delta(LogFloatShares, 50))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(knockout log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241))):`ts_max(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241), 20)`
- 增益 +0.11(window ts_max@20->40):`ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 40)`
