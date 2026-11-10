# 定位:种子 2004,P 组,第 2 轮(只含 train / valid)

快照:prods2004M1_I0_open_search, prods2004M2_I0_open_search, prods2004Pr1a_Ea, prods2004Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.64 | -0.64 | -0.08 | +1 | 5 | prods2004M1_I0_open_search | `ts_skew(day_cov(Ret, Volume), 40)` |
| -0.73 | -0.73 | -0.30 | +1 | 5 | prods2004M1_I0_open_search | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume, Amt), 15), 241)` |
| -0.75 | -0.75 | -0.65 | -1 | 20 | prods2004M2_I0_open_search | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2004M1_I0_open_search | `day_cov(Volume, Volume)` |
| -1.27 | -0.71 | -1.27 | +1 | 20 | prods2004M2_I0_open_search | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 15)` |
| -1.40 | -1.32 | -1.40 | -1 | 20 | prods2004M2_I0_open_search | `cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` |

## 共性:179 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.28 | 0.001 | 6 | -0.96 / -2.24 | `day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239))` |
| +1.21 | 0.002 | 5 | -1.02 / -2.23 | `cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)` |
| +1.03 | 0.012 | 5 | -1.19 / -2.23 | `div(day_cov(Ret, Volume), day_mean(Volume))` |
| +0.90 | 0.009 | 7 | -1.33 / -2.23 | `cross_zscore(day_cov(Ret, Volume), 60)` |
| +0.90 | 0.020 | 6 | -1.33 / -2.23 | `cross_zscore(day_cov(Ret, Volume), 120)` |
| +0.82 | 0.059 | 4 | -1.39 / -2.21 | `day_cov(Volume, Volume)` |
| +0.72 | 0.041 | 7 | -1.50 / -2.22 | `day_mean(Volume)` |
| +0.71 | 0.033 | 11 | -1.53 / -2.24 | `day_std(Ret)` |
| +0.71 | 0.000 | 75 | -1.78 / -2.49 | `day_cov(Ret, Volume)` |
| +0.40 | 0.217 | 10 | -1.82 / -2.22 | `day_cov(in_slice(Ret, 1, 239), in_slice(Ret, 1, 239))` |
| +0.34 | 0.291 | 4 | -1.86 / -2.20 | `cross_corr(day_cov(Ret, Volume), day_std(Ret), 60)` |
| +0.21 | 0.476 | 4 | -1.99 / -2.20 | `day_last(Close)` |
| +0.21 | 0.476 | 4 | -1.99 / -2.20 | `ts_delay(day_last(Close), 1)` |
| +0.21 | 0.476 | 4 | -1.99 / -2.20 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.21 | 0.471 | 5 | -1.99 / -2.20 | `day_first(Open)` |
| +0.19 | 0.446 | 9 | -2.02 / -2.21 | `day_cov(Ret, Ret)` |
| +0.12 | 0.551 | 21 | -2.09 / -2.21 | `mul(day_autocorr_n1(High), day_std(Low))` |
| +0.12 | 0.572 | 22 | -2.09 / -2.21 | `day_autocorr_n1(High)` |
| +0.09 | 0.621 | 24 | -2.12 / -2.21 | `day_std(Low)` |
| +0.07 | 0.532 | 5 | -2.13 / -2.20 | `neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` |

## 拆解(36 次评估)

### head score -0.75:`add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)` | -2.24 | -2.06 | -2.24 | — | (子树本身) |
| sufficiency | `cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -3.22 | -3.22 | -3.22 | — | (子树本身) |
| sufficiency | `ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10)` | -0.81 | -0.81 | -0.72 | — | (子树本身) |
| sufficiency | `cross_min(day_skew(Open), 15)` | -2.28 | -2.28 | -1.19 | — | (子树本身) |
| knockout | `add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20))` | -0.75 | -0.75 | -0.63 | +0.00 | `add(ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| knockout | `ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)` | -0.27 | +0.13 | -0.27 | -0.48 | `add(add(-0.5, day_ar1_coefficient(Amt)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| knockout | `cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -0.55 | -0.55 | -0.26 | -0.20 | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_min(day_skew(Open), 15), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| knockout | `ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10)` | -2.25 | -1.54 | -2.25 | +1.50 | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)), neg(day_cov(Low, Close)))` |
| swap | `Amt->Volume` | -0.75 | -0.75 | -0.66 | — | `add(add(-0.5, ts_cov(day_ar1_coefficient(Volume), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| swap | `Open->Close` | -0.76 | -0.76 | -0.66 | — | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Close), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| window | `ts_cov@20->10` | -0.77 | -0.77 | -0.65 | — | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 10)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |
| window | `ts_cov@20->40` | -0.75 | -0.75 | -0.68 | — | `add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 40)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))` |

### head score -1.27:`cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -2.46 | -0.85 | -2.46 | — | (子树本身) |
| sufficiency | `cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.46 | -0.85 | -2.46 | — | (子树本身) |
| sufficiency | `cross_min(neg(day_cov(Ret, Close)), 15)` | -2.04 | -1.69 | -2.04 | — | (子树本身) |
| sufficiency | `neg(day_cov(Ret, Close))` | -1.25 | -1.14 | -1.25 | — | (子树本身) |
| knockout | `neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -1.30 | -0.71 | -1.30 | +0.03 | `cross_sum(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 15)` |
| knockout | `cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.00 | -1.78 | -2.00 | +0.73 | `cross_sum(neg(cross_min(neg(day_cov(Ret, Close)), 15)), 15)` |
| knockout | `cross_min(neg(day_cov(Ret, Close)), 15)` | -1.87 | -1.85 | -1.87 | +0.61 | `cross_sum(neg(cross_cov(neg(day_cov(Ret, Close)), mul(day_autocorr_n1(High), day_std(Low)), 10)), 15)` |
| knockout | `neg(day_cov(Ret, Close))` | -2.32 | -2.32 | -2.07 | +1.06 | `cross_sum(neg(cross_cov(cross_min(day_cov(Ret, Close), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 15)` |
| swap | `Close->Vwap` | -1.45 | -1.10 | -1.45 | — | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Vwap)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 15)` |
| swap | `High->Low` | -1.34 | -0.73 | -1.34 | — | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(Low), day_std(Low)), 10)), 15)` |
| window | `cross_sum@15->7` | -1.87 | -0.57 | -1.87 | — | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 7)` |
| window | `cross_sum@15->30` | -1.44 | -0.78 | -1.44 | — | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Ret, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30)` |

### head score -1.40:`cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -2.41 | -2.41 | -1.71 | — | (子树本身) |
| sufficiency | `cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.41 | -2.41 | -1.71 | — | (子树本身) |
| sufficiency | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` | -2.51 | -1.86 | -2.51 | — | (子树本身) |
| sufficiency | `neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -2.29 | -2.06 | -2.29 | — | (子树本身) |
| knockout | `neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -1.46 | -1.31 | -1.46 | +0.06 | `cross_sum(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10), 60)` |
| knockout | `cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.81 | -1.92 | -2.81 | +1.41 | `cross_sum(neg(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)), 60)` |
| knockout | `cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` | -1.82 | -1.82 | -1.81 | +0.42 | `cross_sum(neg(cross_cov(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` |
| knockout | `neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -1.46 | -1.31 | -1.46 | +0.06 | `cross_sum(neg(cross_cov(cross_sum(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` |
| swap | `Low->High` | -1.36 | -1.29 | -1.36 | — | `cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(High, Close)), 15), mul(day_autocorr_n1(High), day_std(High)), 10)), 60), mul(day_autocorr_n1(High), day_std(High)), 10)), 60)` |
| swap | `Close->Vwap` | -1.40 | -1.29 | -1.40 | — | `cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Vwap)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` |
| window | `cross_sum@60->30` | -1.50 | -1.50 | -1.24 | — | `cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30)` |
| window | `cross_sum@60->120` | -1.72 | -1.08 | -1.72 | — | `cross_sum(neg(cross_cov(cross_sum(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), mul(day_autocorr_n1(High), day_std(Low)), 10)), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239))` — enrichment,均值差 +1.28,p 0.001
2. `cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)` — enrichment,均值差 +1.21,p 0.002
3. `div(day_cov(Ret, Volume), day_mean(Volume))` — enrichment,均值差 +1.03,p 0.012
4. `cross_zscore(day_cov(Ret, Volume), 60)` — enrichment,均值差 +0.90,p 0.009
5. `cross_zscore(day_cov(Ret, Volume), 120)` — enrichment,均值差 +0.90,p 0.020
6. `day_cov(Volume, Volume)` — enrichment,均值差 +0.82,p 0.059
7. `day_mean(Volume)` — enrichment,均值差 +0.72,p 0.041
8. `day_std(Ret)` — enrichment,均值差 +0.71,p 0.033
9. `day_cov(Ret, Volume)` — enrichment,均值差 +0.71,p 0.000

## 本组之前各轮的任务

- `prods2004Pr1a_Ea`:核心 `day_cov(Ret, Volume)`;评分 76,过线 0,入 heads 0;采样计数 {'c05_no_core': 931, 'c05_skeleton': 456}
  - score -0.25(train -0.25 valid -0.20):`cross_corr(day_cov(Ret, Volume), day_std(Ret), 60)`
  - score -0.27(train -0.27 valid -0.18):`cross_reg_tvalue(day_cov(Ret, Volume), day_std(Ret), 60)`
  - score -0.48(train -0.48 valid -0.11):`add(cross_tail_mean_q75(cross_zscore(day_cov(Ret, Volume), 120), 60), cross_tail_mean_q25(cross_zscore(day_cov(Ret, Volume), 120), 60))`
  - score -0.65(train -0.65 valid -0.51):`cs_mask_top_replace_mean_neg(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30))`
  - score -0.67(train -0.67 valid -0.57):`cs_regres(cs_rank(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)), cs_rank(cross_mean(day_sum(Ret), 20)))`
- `prods2004Pr1b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.41(train -0.41 valid -0.02):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Ret, 1, 239)), 60)`
  - score -0.42(train -0.42 valid +0.06):`cross_corr(day_cov(Ret, Ret), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60)`
  - score -0.52(train -0.52 valid -0.52):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60)`
  - score -0.67(train -0.67 valid +0.02):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 241)`
  - score -0.68(train -0.68 valid -0.27):`cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Volume, 1, 239), in_slice(Volume, 1, 239)), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.20(knockout cross_cov(cross_min(day_skew(Open), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)):`add(add(-0.5, ts_cov(day_ar1_coefficient(Amt), cross_min(day_skew(Open), 15), 20)), ts_regbeta(neg(day_cov(Low, Close)), cross_regalpha(day_quantile(Vwap), day_quantile(High), 15), 10))`
