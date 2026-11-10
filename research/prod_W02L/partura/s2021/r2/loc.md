# 定位:种子 2021,P 组,第 2 轮(只含 train / valid)

快照:prods2021M1_I0_open_search, prods2021M2_I0_open_search, prods2021Pr1a_Ea, prods2021Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.20 | -1.54 | -2.20 | +1 | 5 | prods2021M1_I0_open_search | `add(div(pow_1_5(day_argmin(Amt)), day_max(High)), cross_max(day_cov(Close, Close), 15))` |
| -2.50 | -2.50 | -2.14 | +1 | 5 | prods2021M1_I0_open_search | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20), 5)` |
| -2.90 | -2.90 | -2.89 | +1 | 5 | prods2021M1_I0_open_search | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 20), 5)` |

## 共性:71 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.14 | 0.001 | 4 | -0.30 / -2.44 | `sub(day_max(High), LogFloatShares)` |
| +1.31 | 0.008 | 6 | -1.12 / -2.44 | `log(day_max(High))` |
| +0.89 | 0.016 | 32 | -1.84 / -2.72 | `day_max(High)` |
| +0.86 | 0.006 | 6 | -1.54 / -2.40 | `neg(abs_(day_pos_ratio(Ret)))` |
| +0.85 | 0.009 | 5 | -1.53 / -2.38 | `cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret))))` |
| +0.76 | 0.000 | 14 | -1.71 / -2.47 | `day_std(Close)` |
| +0.71 | 0.001 | 12 | -1.73 / -2.44 | `abs_(day_std(Close))` |
| +0.61 | 0.007 | 10 | -1.80 / -2.41 | `abs_(day_pos_ratio(Ret))` |
| +0.59 | 0.001 | 17 | -1.88 / -2.46 | `day_pos_ratio(Ret)` |
| +0.56 | 0.296 | 4 | -1.79 / -2.36 | `sub(LogFloatCap, LogFloatShares)` |
| +0.42 | 0.276 | 5 | -1.93 / -2.35 | `ts_med(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)` |
| +0.32 | 0.301 | 10 | -2.05 / -2.37 | `ts_delay(day_last(Close), 1)` |
| +0.32 | 0.397 | 7 | -2.04 / -2.36 | `cross_ema(day_max(High), 5)` |
| +0.26 | 0.421 | 9 | -2.10 / -2.36 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.17 | 0.280 | 5 | -2.16 / -2.34 | `neg(day_pos_ratio(Ret))` |
| +0.09 | 0.349 | 4 | -2.24 / -2.33 | `pow_3(abs_(day_pos_ratio(Ret)))` |
| -0.03 | 0.648 | 13 | -2.35 / -2.32 | `day_first(Open)` |
| -0.06 | 0.691 | 13 | -2.37 / -2.31 | `day_last(Close)` |
| -0.14 | 0.866 | 6 | -2.46 / -2.31 | `div(day_last(Close), day_first(Open))` |
| -0.34 | 0.928 | 4 | -2.65 / -2.31 | `day_argmin(Amt)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_max(High), LogFloatShares)` — enrichment,均值差 +2.14,p 0.001
2. `log(day_max(High))` — enrichment,均值差 +1.31,p 0.008
3. `day_max(High)` — enrichment,均值差 +0.89,p 0.016
4. `neg(abs_(day_pos_ratio(Ret)))` — enrichment,均值差 +0.86,p 0.006
5. `cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret))))` — enrichment,均值差 +0.85,p 0.009
6. `day_std(Close)` — enrichment,均值差 +0.76,p 0.000
7. `abs_(day_std(Close))` — enrichment,均值差 +0.71,p 0.001
8. `abs_(day_pos_ratio(Ret))` — enrichment,均值差 +0.61,p 0.007
9. `day_pos_ratio(Ret)` — enrichment,均值差 +0.59,p 0.001

## 本组之前各轮的任务

- `prods2021Pr1a_Ea`:核心 `day_max(High)`;评分 86,过线 0,入 heads 0;采样计数 {'c05_no_core': 1741, 'c05_skeleton': 873}
  - score -0.22(train -0.05 valid -0.22):`div(log(LogFloatShares), sub(day_max(High), LogFloatShares))`
  - score -0.27(train -0.05 valid -0.27):`div(log(day_max(High)), sub(day_max(High), LogFloatShares))`
  - score -0.30(train -0.12 valid -0.30):`div(day_max(High), sub(day_max(High), LogFloatShares))`
  - score -0.42(train -0.26 valid -0.42):`div(log(day_max(High)), sub(LogFloatCap, cross_ema(day_max(High), 5)))`
  - score -0.42(train -0.36 valid -0.42):`div(log(day_autocorr_n1(High)), sub(day_max(High), LogFloatShares))`
- `prods2021Pr1b_Nb`:核心 `—`;评分 74,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -1.26(train -1.26 valid -1.24):`sub(ts_med(sub(div(day_first(Open), cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret))))), 1), 40), cs_bucket_zscore(abs_(day_std(Close)), neg(abs_(day_pos_ratio(Ret)))))`
  - score -1.52(train -1.44 valid -1.52):`cs_bucket_zscore(abs_(day_std(Close)), pow_3(abs_(day_pos_ratio(Ret))))`
  - score -1.53(train -1.44 valid -1.53):`cs_bucket_zscore(abs_(day_std(Close)), pow_05(abs_(day_pos_ratio(Ret))))`
  - score -1.53(train -1.44 valid -1.53):`cs_bucket_zscore(abs_(day_std(Close)), day_pos_ratio(Ret))`
  - score -1.53(train -1.44 valid -1.53):`cs_bucket_zscore(abs_(day_std(Close)), pow_3(day_pos_ratio(Ret)))`

## 比原 head 好的拆解变体(R 候选)

(没有)
