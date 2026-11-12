# 定位:种子 2050,P 组,第 3 轮(只含 train / valid)

快照:prods2050M1_I0_open_search, prods2050M2_I0_open_search, prods2050M3_I0_open_search, prods2050Pr1a_Ea, prods2050Pr2a_Ea, prods2050Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.04 | -2.04 | -0.32 | +1 | 5 | prods2050M1_I0_open_search | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 240)` |
| -2.23 | -2.23 | -1.00 | -1 | 20 | prods2050M3_I0_open_search | `day_max(pow_1_5(log(nt_ts_kurt(Vwap, 15))))` |
| -2.23 | -2.23 | -1.00 | -1 | 20 | prods2050M3_I0_open_search | `day_max(log(nt_ts_kurt(Vwap, 15)))` |
| -2.33 | -2.33 | -1.95 | -1 | 0 | prods2050M1_I0_open_search | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)` |
| -2.74 | -1.34 | -2.74 | +1 | 5 | prods2050M1_I0_open_search | `cross_stddev(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)` |
| -2.80 | -2.80 | -1.20 | -1 | 20 | prods2050M3_I0_open_search | `pow_05(day_max(pow_1_5(log(nt_ts_kurt(Vwap, 10)))))` |

## 共性:155 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.38 | 0.006 | 4 | -1.22 / -2.59 | `ts_kurt(div(day_last(Close), day_first(Open)), 50)` |
| +1.28 | 0.000 | 8 | -1.35 / -2.62 | `cs_bucket_demean(day_sum(Open), LogFloatCap)` |
| +1.05 | 0.018 | 4 | -1.54 / -2.58 | `pow_3(day_distinct_ratio(Open))` |
| +1.03 | 0.000 | 42 | -1.81 / -2.84 | `day_sum(Open)` |
| +0.93 | 0.012 | 6 | -1.66 / -2.59 | `day_distinct_ratio(Open)` |
| +0.70 | 0.091 | 4 | -1.88 / -2.58 | `cross_ema(day_sum(Open), 20)` |
| +0.45 | 0.057 | 21 | -2.17 / -2.62 | `div(day_last(Close), day_first(Open))` |
| +0.40 | 0.228 | 5 | -2.17 / -2.57 | `ts_kurt(day_hurst(Close), 50)` |
| +0.36 | 0.236 | 6 | -2.21 / -2.57 | `day_sum(Amt)` |
| +0.31 | 0.247 | 8 | -2.27 / -2.57 | `day_hurst(Close)` |
| +0.29 | 0.357 | 4 | -2.27 / -2.57 | `cross_mean(div(day_last(Close), day_first(Open)), 60)` |
| +0.29 | 0.159 | 39 | -2.34 / -2.63 | `day_last(Close)` |
| +0.26 | 0.330 | 5 | -2.30 / -2.57 | `cross_mean(day_sum(Amt), 20)` |
| +0.26 | 0.175 | 31 | -2.35 / -2.61 | `day_first(Open)` |
| +0.12 | 0.495 | 8 | -2.44 / -2.56 | `cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| +0.08 | 0.541 | 23 | -2.49 / -2.57 | `cross_delay(day_last(Close), 1)` |
| +0.05 | 0.587 | 4 | -2.51 / -2.56 | `day_first(Close)` |
| +0.05 | 0.587 | 4 | -2.51 / -2.56 | `div(day_first(Close), cross_delay(day_last(Close), 1))` |
| -0.03 | 0.626 | 4 | -2.59 / -2.56 | `cross_delay(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 60), 1)` |
| -0.07 | 0.742 | 17 | -2.62 / -2.55 | `div(day_first(Open), cross_delay(day_last(Close), 1))` |

## 拆解(16 次评估)

### head score -2.04:`cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 240)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -4.72 | -4.72 | -2.84 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.71 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |
| knockout | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -2.58 | -2.58 | -1.96 | +0.54 | `cross_mean(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 240)` |
| window | `cross_mean@240->120` | -2.45 | -2.45 | -1.19 | — | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 120)` |
| window | `cross_mean@240->480` | -2.22 | -2.22 | -0.50 | — | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 480)` |

### head score -2.23:`day_max(pow_1_5(log(nt_ts_kurt(Vwap, 15))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -1.47 | -0.99 | -1.47 | — | `day_max(pow_1_5(log(nt_ts_kurt(Close, 15))))` |
| window | `nt_ts_kurt@15->7` | -2.06 | -2.06 | -1.63 | — | `day_max(pow_1_5(log(nt_ts_kurt(Vwap, 7))))` |
| window | `nt_ts_kurt@15->30` | -2.87 | -2.87 | -1.38 | — | `day_max(pow_1_5(log(nt_ts_kurt(Vwap, 30))))` |

### head score -2.23:`day_max(log(nt_ts_kurt(Vwap, 15)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -1.47 | -1.00 | -1.47 | — | `day_max(log(nt_ts_kurt(Close, 15)))` |
| window | `nt_ts_kurt@15->7` | -2.07 | -2.07 | -1.63 | — | `day_max(log(nt_ts_kurt(Vwap, 7)))` |
| window | `nt_ts_kurt@15->30` | -2.86 | -2.86 | -1.38 | — | `day_max(log(nt_ts_kurt(Vwap, 30)))` |

### head score -2.80:`pow_05(day_max(pow_1_5(log(nt_ts_kurt(Vwap, 10)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(pow_1_5(log(nt_ts_kurt(Vwap, 10))))` | -2.80 | -2.80 | -1.23 | — | (子树本身) |
| swap | `Vwap->Close` | -0.56 | -0.25 | -0.56 | — | `pow_05(day_max(pow_1_5(log(nt_ts_kurt(Close, 10)))))` |
| window | `nt_ts_kurt@10->5` | -2.26 | -2.16 | -2.26 | — | `pow_05(day_max(pow_1_5(log(nt_ts_kurt(Vwap, 5)))))` |
| window | `nt_ts_kurt@10->20` | -2.35 | -2.35 | -1.27 | — | `pow_05(day_max(pow_1_5(log(nt_ts_kurt(Vwap, 20)))))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_kurt(div(day_last(Close), day_first(Open)), 50)` — enrichment,均值差 +1.38,p 0.006
2. `cs_bucket_demean(day_sum(Open), LogFloatCap)` — enrichment,均值差 +1.28,p 0.000
3. `pow_3(day_distinct_ratio(Open))` — enrichment,均值差 +1.05,p 0.018
4. `day_sum(Open)` — enrichment,均值差 +1.03,p 0.000
5. `day_distinct_ratio(Open)` — enrichment,均值差 +0.93,p 0.012
6. `cross_ema(day_sum(Open), 20)` — enrichment,均值差 +0.70,p 0.091
7. `div(day_last(Close), day_first(Open))` — enrichment,均值差 +0.45,p 0.057

## 本组之前各轮的任务

- `prods2050Pr1a_Ea`:核心 `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))`;评分 76,过线 0,入 heads 0;采样计数 {'c05_no_core': 2172, 'c05_skeleton': 1098}
  - score -0.56(train -0.56 valid -0.19):`cross_autocorr_s1(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 241)`
  - score -1.28(train -0.40 valid -1.28):`cross_corr(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_sum(Open), 30)`
  - score -1.54(train -0.76 valid -1.54):`cross_corr(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_sum(Open), 20)`
  - score -1.55(train -0.75 valid -1.55):`cross_corr(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_sum(Close), 20)`
  - score -1.56(train -1.35 valid -1.56):`cross_autocorr_s1(cross_autocorr_s1(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 241), 241)`
- `prods2050Pr2a_Ea`:核心 `day_sum(Open)`;评分 100,过线 0,入 heads 0;采样计数 {'c05_no_core': 1788, 'c05_skeleton': 853}
  - score -0.89(train -0.82 valid -0.89):`cs_bucket_demean(cs_bucket_demean(day_sum(Open), cross_tail_mean_q25(day_sum(Open), 60)), cross_tail_mean_q25(day_sum(Open), 60))`
  - score -0.90(train -0.90 valid -0.88):`cs_last_high05(LogFloatCap, day_sum(Open))`
  - score -0.93(train -0.85 valid -0.93):`cs_bucket_demean(cross_mean(cs_bucket_demean(day_sum(Open), day_quantile_q25(Open)), 20), day_quantile_q25(Open))`
  - score -1.07(train -1.07 valid -0.87):`cross_mean(cs_bucket_demean(day_sum(Open), LogFloatCap), 20)`
  - score -1.09(train -1.09 valid -0.87):`cs_bucket_demean(cs_bucket_demean(cross_mean(cs_bucket_demean(day_sum(Open), LogFloatCap), 20), LogFloatCap), LogFloatCap)`
- `prods2050Pr2b_Nb`:核心 `—`;评分 100,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.29(train -0.27 valid -0.29):`ts_kurt(pow_3(day_es_ratio_lo(Close)), 50)`
  - score -0.46(train -0.46 valid -0.10):`ts_kurt(pow_3(day_es_ratio_lo(Open)), 50)`
  - score -0.61(train -0.61 valid -0.29):`cross_mean(div(ts_kurt(div(day_last(Close), day_first(Open)), 50), cross_delay(div(day_first(Open), cross_delay(div(day_last(Close), day_first(Open)), 1)), 1)), 60)`
  - score -1.06(train -0.87 valid -1.06):`cs_bucket_zscore(pow_3(day_distinct_ratio(Open)), day_last(Close))`
  - score -1.18(train -1.18 valid -1.06):`cross_mean(div(ts_kurt(div(day_last(Close), day_first(Open)), 50), cross_delay(day_last(Close), 10)), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.76(swap Vwap->Close):`day_max(log(nt_ts_kurt(Close, 15)))`
- 增益 +0.76(swap Vwap->Close):`day_max(pow_1_5(log(nt_ts_kurt(Close, 15))))`
