# 定位:种子 2006,P 组,第 2 轮(只含 train / valid)

快照:prods2006M1_I0_open_search, prods2006M2_I0_open_search;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.48 | -0.48 | +0.23 | -1 | 20 | prods2006M1_I0_open_search | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), cross_mean(day_std(Amt), 30)))` |
| -1.44 | -1.27 | -1.44 | +1 | 5 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 50)))` |
| -1.51 | -1.27 | -1.51 | +1 | 5 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50)))` |
| -1.63 | -1.63 | -1.63 | +1 | 0 | prods2006M2_I0_open_search | `cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 60)` |
| -1.70 | -1.65 | -1.70 | -1 | 5 | prods2006M2_I0_open_search | `cross_min(cross_min(day_cov(Low, Ret), 15), 15)` |
| -1.72 | -1.72 | -1.53 | -1 | 5 | prods2006M2_I0_open_search | `cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 15)` |

## 共性:30 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.87 | 0.005 | 4 | -1.46 / -2.33 | `day_cov(Amt, Open)` |
| +0.68 | 0.003 | 13 | -1.83 / -2.51 | `day_last(Volume)` |
| -0.09 | 0.934 | 12 | -2.27 / -2.18 | `day_cov(Low, Ret)` |
| -0.09 | 0.897 | 9 | -2.28 / -2.19 | `cross_min(day_cov(Low, Ret), 15)` |
| -0.23 | 0.828 | 4 | -2.41 / -2.19 | `day_autocorr_n1(High)` |
| -0.75 | 0.894 | 4 | -2.87 / -2.12 | `day_cov(Open, Open)` |

## 拆解(40 次评估)

### head score -0.48:`sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), cross_mean(day_std(Amt), 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), cross_mean(day_std(Amt), 30))` | -0.48 | -0.48 | +0.23 | — | (子树本身) |
| sufficiency | `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100))` | -0.64 | -0.64 | +0.03 | — | (子树本身) |
| sufficiency | `ts_regres(day_cov(Amt, Open), day_last(Amt), 100)` | -2.91 | -2.73 | -2.91 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Amt), 30)` | -3.76 | -2.87 | -3.76 | — | (子树本身) |
| knockout | `cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), cross_mean(day_std(Amt), 30))` | -0.64 | -0.64 | +0.03 | +0.17 | `sub(0.5, abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)))` |
| knockout | `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100))` | -2.30 | -2.30 | -1.75 | +1.82 | `sub(0.5, cs_bucket_zscore(ts_regres(day_cov(Amt, Open), day_last(Amt), 100), cross_mean(day_std(Amt), 30)))` |
| knockout | `ts_regres(day_cov(Amt, Open), day_last(Amt), 100)` | -3.46 | -2.62 | -3.46 | +2.98 | `sub(0.5, cs_bucket_zscore(abs_(day_cov(Amt, Open)), cross_mean(day_std(Amt), 30)))` |
| knockout | `cross_mean(day_std(Amt), 30)` | -0.34 | -0.34 | +0.02 | -0.13 | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), day_std(Amt)))` |
| swap | `Amt->Volume` | -1.38 | -1.38 | -0.17 | — | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Volume, Open), day_last(Volume), 100)), cross_mean(day_std(Volume), 30)))` |
| swap | `Open->Close` | -0.43 | -0.43 | +0.25 | — | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Close), day_last(Amt), 100)), cross_mean(day_std(Amt), 30)))` |
| window | `ts_regres@100->50` | -1.65 | -1.65 | -1.53 | — | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 50)), cross_mean(day_std(Amt), 30)))` |
| window | `ts_regres@100->200` | -0.21 | -0.21 | +1.46 | — | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)))` |

### head score -1.63:`cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30)` | -1.33 | -1.27 | -1.33 | — | (子树本身) |
| sufficiency | `neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -1.89 | -1.81 | -1.89 | — | (子树本身) |
| sufficiency | `cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -1.89 | -1.81 | -1.89 | — | (子树本身) |
| sufficiency | `cross_min(day_cov(Low, Ret), 15)` | -2.15 | -1.72 | -2.15 | — | (子树本身) |
| knockout | `cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30)` | -1.54 | -1.42 | -1.54 | -0.10 | `cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60)` |
| knockout | `neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10))` | -1.65 | -1.63 | -1.65 | +0.02 | `cross_sum(cross_sum(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 30), 60)` |
| knockout | `cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.51 | -2.16 | -2.51 | +0.88 | `cross_sum(cross_sum(neg(cross_min(day_cov(Low, Ret), 15)), 30), 60)` |
| knockout | `cross_min(day_cov(Low, Ret), 15)` | -2.98 | -2.93 | -2.98 | +1.34 | `cross_sum(cross_sum(neg(cross_cov(day_cov(Low, Ret), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 60)` |
| swap | `Low->High` | -1.93 | -1.93 | -1.40 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(High, Ret), 15), mul(day_autocorr_n1(High), day_std(High)), 10)), 30), 60)` |
| swap | `High->Low` | -1.65 | -1.57 | -1.65 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(Low), day_std(Low)), 10)), 30), 60)` |
| window | `cross_sum@60->30` | -1.41 | -1.36 | -1.41 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 30)` |
| window | `cross_sum@60->120` | -2.02 | -1.94 | -2.02 | — | `cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 120)` |

### head score -1.70:`cross_min(cross_min(day_cov(Low, Ret), 15), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_min(day_cov(Low, Ret), 15)` | -2.15 | -1.72 | -2.15 | — | (子树本身) |
| sufficiency | `day_cov(Low, Ret)` | -4.22 | -4.22 | -3.43 | — | (子树本身) |
| swap | `Low->High` | -2.29 | -1.82 | -2.29 | — | `cross_min(cross_min(day_cov(High, Ret), 15), 15)` |
| window | `cross_min@15->7` | -2.19 | -1.73 | -2.19 | — | `cross_min(cross_min(day_cov(Low, Ret), 15), 7)` |
| window | `cross_min@15->30` | -2.02 | -1.80 | -2.02 | — | `cross_min(cross_min(day_cov(Low, Ret), 15), 30)` |

### head score -1.72:`cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.17 | -2.17 | -1.48 | — | (子树本身) |
| sufficiency | `cross_min(cross_min(day_cov(Low, Ret), 15), 15)` | -1.72 | -1.65 | -1.72 | — | (子树本身) |
| sufficiency | `cross_min(day_cov(Low, Ret), 15)` | -2.15 | -1.72 | -2.15 | — | (子树本身) |
| sufficiency | `mul(day_autocorr_n1(High), day_std(Low))` | -2.31 | -1.58 | -2.31 | — | (子树本身) |
| knockout | `cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)` | -2.15 | -1.81 | -2.15 | +0.43 | `cross_min(cross_min(cross_min(day_cov(Low, Ret), 15), 15), 15)` |
| knockout | `cross_min(cross_min(day_cov(Low, Ret), 15), 15)` | -1.79 | -1.54 | -1.79 | +0.08 | `cross_min(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 15)` |
| knockout | `mul(day_autocorr_n1(High), day_std(Low))` | -1.60 | -1.58 | -1.60 | -0.12 | `cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), day_autocorr_n1(High), 10), 15)` |
| swap | `Low->High` | -2.11 | -2.11 | -2.04 | — | `cross_min(cross_cov(cross_min(cross_min(day_cov(High, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(High)), 10), 15)` |
| swap | `High->Low` | -1.70 | -1.70 | -1.55 | — | `cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(Low), day_std(Low)), 10), 15)` |
| window | `cross_min@15->7` | -2.02 | -2.02 | -1.59 | — | `cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 7)` |
| window | `cross_min@15->30` | -1.64 | -1.41 | -1.64 | — | `cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_cov(Amt, Open)` — enrichment,均值差 +0.87,p 0.005
2. `day_last(Volume)` — enrichment,均值差 +0.68,p 0.003

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(window ts_regres@100->200):`sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)))`
- 增益 +0.22(window cross_sum@60->30):`cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 30)`
- 增益 +0.13(knockout cross_mean(day_std(Amt), 30)):`sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), day_std(Amt)))`
- 增益 +0.12(knockout mul(day_autocorr_n1(High), day_std(Low))):`cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), day_autocorr_n1(High), 10), 15)`
