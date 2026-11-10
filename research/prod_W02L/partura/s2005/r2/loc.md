# 定位:种子 2005,P 组,第 2 轮(只含 train / valid)

快照:prods2005M1_I0_open_search, prods2005M2_I0_open_search, prods2005Pr1a_Ea, prods2005Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.42 | -1.27 | -1.42 | -1 | 20 | prods2005M2_I0_open_search | `cross_mean(day_cov(Close, Ret), 3)` |
| -1.47 | -1.42 | -1.47 | +1 | 20 | prods2005M1_I0_open_search | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30), cross_mean(day_std(Amt), 30))` |
| -1.54 | -1.54 | -1.20 | -1 | 0 | prods2005M2_I0_open_search | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 60)` |
| -1.70 | -1.70 | -1.61 | +1 | 5 | prods2005M2_I0_open_search | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30), 3)` |
| -1.84 | -1.84 | -1.68 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(day_cov(Ret, Close), 60)` |
| -1.85 | -1.85 | -0.75 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5)` |

## 共性:154 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.74 | 0.021 | 6 | -1.74 / -2.48 | `pow_3(day_cov(Ret, Close))` |
| +0.66 | 0.021 | 6 | -1.82 / -2.48 | `day_cov(Close, Ret)` |
| +0.62 | 0.071 | 4 | -1.85 / -2.47 | `day_flat_run_max(Low)` |
| +0.55 | 0.000 | 40 | -2.05 / -2.60 | `day_cov(Ret, Close)` |
| +0.53 | 0.049 | 8 | -1.95 / -2.48 | `ts_delay(day_close(Close), 1)` |
| +0.53 | 0.021 | 8 | -1.95 / -2.48 | `day_zero_ratio(Ret)` |
| +0.52 | 0.090 | 6 | -1.95 / -2.47 | `day_first(Open)` |
| +0.42 | 0.075 | 10 | -2.06 / -2.48 | `day_close(Close)` |
| +0.42 | 0.039 | 13 | -2.07 / -2.49 | `day_sum(Ret)` |
| +0.30 | 0.083 | 7 | -2.17 / -2.47 | `div(cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt)), day_sum(Amt))` |
| +0.22 | 0.268 | 4 | -2.24 / -2.46 | `div(day_sum(Ret), ts_delay(day_close(Close), 1))` |
| +0.19 | 0.190 | 9 | -2.28 / -2.46 | `cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt))` |
| +0.16 | 0.423 | 10 | -2.30 / -2.46 | `day_mean(Close)` |
| +0.09 | 0.531 | 10 | -2.37 / -2.46 | `day_var(Ret)` |
| +0.08 | 0.536 | 10 | -2.38 / -2.46 | `cross_mean(day_cov(Low, Ret), 60)` |
| +0.06 | 0.554 | 14 | -2.40 / -2.46 | `cross_max(day_cov(Amt, Low), 5)` |
| +0.06 | 0.187 | 22 | -2.40 / -2.46 | `day_distinct_ratio(Vwap)` |
| +0.04 | 0.609 | 9 | -2.41 / -2.46 | `div(day_cov(Ret, Close), day_mean(Close))` |
| +0.00 | 0.347 | 34 | -2.45 / -2.45 | `day_sum(Amt)` |
| -0.00 | 0.620 | 5 | -2.46 / -2.45 | `neg(cross_mean(day_cov(Low, Ret), 60))` |

## 拆解(36 次评估)

### head score -1.42:`cross_mean(day_cov(Close, Ret), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Close, Ret)` | -1.25 | -1.14 | -1.25 | — | (子树本身) |
| swap | `Close->Vwap` | -3.38 | -2.44 | -3.38 | — | `cross_mean(day_cov(Vwap, Ret), 3)` |
| window | `cross_mean@3->2` | -1.29 | -1.21 | -1.29 | — | `cross_mean(day_cov(Close, Ret), 2)` |
| window | `cross_mean@3->6` | -1.41 | -1.41 | -1.40 | — | `cross_mean(day_cov(Close, Ret), 6)` |

### head score -1.47:`cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30), cross_mean(day_std(Amt), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | -1.83 | -1.83 | -1.59 | — | (子树本身) |
| sufficiency | `cross_max(cross_max(day_cov(Amt, Low), 5), 5)` | -2.24 | -2.24 | -2.14 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(Amt, Low), 5)` | -2.14 | -2.12 | -2.14 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -3.76 | -2.87 | -3.76 | — | (子树本身) |
| knockout | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | -2.07 | -2.07 | -2.04 | +0.60 | `cs_bucket_demean(cross_max(cross_max(day_cov(Amt, Low), 5), 5), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_max(cross_max(day_cov(Amt, Low), 5), 5)` | -1.54 | -1.49 | -1.54 | +0.06 | `cs_bucket_demean(cross_max(cross_max(day_cov(Amt, Low), 5), 30), cross_mean(day_std(Amt), 30))` |
| knockout | `cross_mean(day_std(Amt), 30)` | -1.43 | -1.43 | -1.06 | -0.05 | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30), day_std(Amt))` |
| swap | `Amt->Volume` | -2.91 | -2.91 | -2.85 | — | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Volume, Low), 5), 5), 30), cross_mean(day_std(Volume), 30))` |
| swap | `Low->High` | -1.57 | -1.52 | -1.57 | — | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, High), 5), 5), 30), cross_mean(day_std(Amt), 30))` |
| window | `cross_max@30->15` | -1.68 | -1.67 | -1.68 | — | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 15), cross_mean(day_std(Amt), 30))` |
| window | `cross_max@30->60` | -1.48 | -1.48 | -0.86 | — | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 60), cross_mean(day_std(Amt), 30))` |

### head score -1.54:`cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` | -1.72 | -1.72 | -1.13 | — | (子树本身) |
| sufficiency | `neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -3.88 | -3.54 | -3.88 | — | (子树本身) |
| sufficiency | `cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -3.88 | -3.54 | -3.88 | — | (子树本身) |
| sufficiency | `cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15)` | -2.54 | -2.38 | -2.54 | — | (子树本身) |
| knockout | `neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -1.54 | -1.54 | -1.25 | -0.00 | `cross_sum(cross_sum(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 60), 60)` |
| knockout | `cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -3.30 | -2.33 | -3.30 | +1.76 | `cross_sum(cross_sum(neg(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15)), 60), 60)` |
| knockout | `cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15)` | -1.80 | -1.42 | -1.80 | +0.26 | `cross_sum(cross_sum(neg(cross_cov(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 60)` |
| swap | `Low->High` | -1.78 | -1.41 | -1.78 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(High, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(High)), 10)), 60), 60)` |
| swap | `High->Low` | -1.54 | -1.54 | -1.25 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(Low), day_std(Low)), 10)), 60), 60)` |
| window | `cross_sum@60->30` | -1.54 | -1.54 | -1.21 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 30)` |
| window | `cross_sum@60->120` | -1.40 | -1.40 | -1.34 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 120)` |

### head score -1.70:`cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30)` | -1.77 | -1.63 | -1.77 | — | (子树本身) |
| sufficiency | `neg(cross_mean(day_cov(Close, Ret), 10))` | -1.95 | -1.41 | -1.95 | — | (子树本身) |
| sufficiency | `cross_mean(day_cov(Close, Ret), 10)` | -1.95 | -1.41 | -1.95 | — | (子树本身) |
| sufficiency | `day_cov(Close, Ret)` | -1.25 | -1.14 | -1.25 | — | (子树本身) |
| knockout | `cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30)` | -2.02 | -1.47 | -2.02 | +0.32 | `cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 3)` |
| knockout | `neg(cross_mean(day_cov(Close, Ret), 10))` | -1.70 | -1.70 | -1.57 | +0.00 | `cross_sum(cross_sum(cross_mean(day_cov(Close, Ret), 10), 30), 3)` |
| knockout | `cross_mean(day_cov(Close, Ret), 10)` | -1.56 | -1.56 | -1.49 | -0.14 | `cross_sum(cross_sum(neg(day_cov(Close, Ret)), 30), 3)` |
| swap | `Close->Vwap` | -2.42 | -2.24 | -2.42 | — | `cross_sum(cross_sum(neg(cross_mean(day_cov(Vwap, Ret), 10)), 30), 3)` |
| window | `cross_sum@3->2` | -1.80 | -1.69 | -1.80 | — | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30), 2)` |
| window | `cross_sum@3->6` | -1.69 | -1.69 | -1.61 | — | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10)), 30), 6)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_3(day_cov(Ret, Close))` — enrichment,均值差 +0.74,p 0.021
2. `day_cov(Close, Ret)` — enrichment,均值差 +0.66,p 0.021
3. `day_flat_run_max(Low)` — enrichment,均值差 +0.62,p 0.071
4. `day_cov(Ret, Close)` — enrichment,均值差 +0.55,p 0.000
5. `ts_delay(day_close(Close), 1)` — enrichment,均值差 +0.53,p 0.049
6. `day_zero_ratio(Ret)` — enrichment,均值差 +0.53,p 0.021
7. `day_first(Open)` — enrichment,均值差 +0.52,p 0.090
8. `day_close(Close)` — enrichment,均值差 +0.42,p 0.075
9. `day_sum(Ret)` — enrichment,均值差 +0.42,p 0.039
10. `div(cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt)), day_sum(Amt))` — enrichment,均值差 +0.30,p 0.083

## 本组之前各轮的任务

- `prods2005Pr1a_Ea`:核心 `day_cov(Ret, Close)`;评分 76,过线 0,入 heads 0;采样计数 {'c05_no_core': 1334, 'c05_skeleton': 680}
  - score -0.84(train -0.34 valid -0.84):`inv(cross_tail_mean_q25(pow_3(day_cov(Ret, Close)), 241))`
  - score -1.12(train -0.99 valid -1.12):`cs_last_high20(sub(day_cov(Ret, Close), day_flat_run_max(Low)), day_cov(Ret, Close))`
  - score -1.19(train -1.19 valid -0.39):`cs_last_high20(day_cov(Ret, Close), day_cov(Ret, Close))`
  - score -1.25(train -1.14 valid -1.25):`neg(day_cov(Ret, Close))`
  - score -1.25(train -1.14 valid -1.25):`signedpower(day_cov(Ret, Close))`
- `prods2005Pr1b_Nb`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 17}
  - score -0.91(train -0.91 valid -0.89):`cross_corr(div(cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt)), day_sum(Amt)), day_zero_ratio(Ret), 60)`
  - score -0.93(train -0.92 valid -0.93):`cross_corr(day_close(Amt), day_zero_ratio(Ret), 15)`
  - score -0.99(train -0.86 valid -0.99):`cross_corr(div(day_close(Amt), day_sum(Amt)), div(day_first(Open), ts_delay(day_close(Close), 1)), 60)`
  - score -1.00(train -0.91 valid -1.00):`cross_corr(div(day_close(Amt), day_sum(Amt)), div(day_first(Vwap), ts_delay(day_close(Close), 1)), 60)`
  - score -1.06(train -0.98 valid -1.06):`cross_corr(div(cs_last_high40(day_distinct_ratio(Vwap), day_close(Amt)), day_sum(Amt)), day_sum(Ret), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.14(window cross_sum@60->120):`cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 120)`
- 增益 +0.14(window cross_mean@3->2):`cross_mean(day_cov(Close, Ret), 2)`
