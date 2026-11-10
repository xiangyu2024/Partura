# 定位:种子 2032,P 组,第 3 轮(只含 train / valid)

快照:prods2032M1_I0_open_search, prods2032M2_I0_open_search, prods2032M3_I0_open_search, prods2032Pr1a_Ea, prods2032Pr1b_Nb, prods2032Pr2a_Ea, prods2032Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.58 | +0.67 | +0.58 | -1 | 20 | prods2032Pr2a_Ea | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 60)` |
| -0.25 | -0.11 | -0.25 | +1 | 5 | prods2032M3_I0_open_search | `ts_std(ts_std(day_last(Amt), 50), 50)` |
| -0.49 | -0.06 | -0.49 | +1 | 5 | prods2032M3_I0_open_search | `ts_regbeta(day_last(Amt), day_durbin_watson(Open), 10)` |
| -0.52 | -0.52 | -0.43 | +1 | 5 | prods2032M3_I0_open_search | `ts_std(day_last(Amt), 50)` |
| -1.12 | -1.12 | -1.12 | -1 | 0 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 60)` |
| -1.15 | -1.15 | -1.09 | -1 | 5 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 5)` |
| -1.20 | -1.20 | -1.03 | -1 | 5 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 3)` |
| -1.63 | -1.62 | -1.63 | -1 | 20 | prods2032M2_I0_open_search | `div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| -1.79 | -1.66 | -1.79 | -1 | 0 | prods2032M2_I0_open_search | `ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 80)` |
| -1.80 | -1.80 | -1.59 | -1 | 20 | prods2032M2_I0_open_search | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5)), 0.5)` |

## 共性:262 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.88 | 0.000 | 7 | +0.19 / -1.69 | `cs_quantile_q75(day_wstd(Amt, Vwap))` |
| +1.88 | 0.000 | 7 | +0.19 / -1.69 | `day_wstd(Amt, Vwap)` |
| +1.74 | 0.000 | 18 | -0.02 / -1.75 | `cross_mean(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 20)` |
| +1.71 | 0.001 | 5 | +0.04 / -1.67 | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)))` |
| +1.67 | 0.003 | 4 | +0.01 / -1.66 | `cross_mean(ts_min(day_min(Close), 1), 30)` |
| +1.67 | 0.003 | 4 | +0.01 / -1.66 | `ts_min(day_min(Close), 1)` |
| +1.50 | 0.002 | 5 | -0.17 / -1.66 | `cross_mean(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 30)` |
| +1.42 | 0.006 | 5 | -0.24 / -1.66 | `neg(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)))` |
| +1.41 | 0.004 | 5 | -0.25 / -1.66 | `day_min(Close)` |
| +1.22 | 0.019 | 4 | -0.43 / -1.65 | `cross_mean(cross_ema(day_first(Volume), 20), 30)` |
| +1.19 | 0.000 | 81 | -0.81 / -2.00 | `cross_mean(day_sum(Volume), 30)` |
| +1.14 | 0.000 | 142 | -1.12 / -2.25 | `day_sum(Volume)` |
| +1.11 | 0.000 | 75 | -0.85 / -1.95 | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` |
| +1.08 | 0.000 | 92 | -0.94 / -2.01 | `cross_ema(day_first(Volume), 20)` |
| +1.00 | 0.000 | 115 | -1.08 / -2.07 | `day_first(Volume)` |
| +0.96 | 0.054 | 4 | -0.69 / -1.65 | `mul(day_last(Close), day_first(Open))` |
| +0.87 | 0.064 | 4 | -0.78 / -1.65 | `ts_std(day_last(Amt), 50)` |
| +0.44 | 0.284 | 5 | -1.20 / -1.64 | `cross_ema(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 20)` |
| +0.42 | 0.184 | 9 | -1.23 / -1.65 | `ts_delay(mul(sub(div(day_last(Close), day_first(Open)), 1), cross_zscore(log(add(day_sum(Volume), 1)), 60)), 1)` |
| +0.19 | 0.480 | 4 | -1.45 / -1.64 | `day_last(Volume)` |

## 拆解(26 次评估)

### head score +0.58:`cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)))` | -1.29 | -1.04 | -1.29 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` | +0.03 | +0.03 | +0.42 | — | (子树本身) |
| sufficiency | `cross_ema(day_first(Volume), 20)` | -1.05 | -1.05 | -1.03 | — | (子树本身) |
| knockout | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)))` | +0.05 | +0.05 | +0.68 | +0.53 | `cross_regbeta(cross_ema(day_first(Volume), 20), cs_quantile_q75(day_wstd(Amt, Close)), 60)` |
| knockout | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` | -0.51 | +0.13 | -0.51 | +1.09 | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_ema(day_first(Volume), 20)), cs_quantile_q75(day_wstd(Amt, Close)), 60)` |
| knockout | `cross_ema(day_first(Volume), 20)` | -0.73 | -0.73 | -0.36 | +1.31 | `cross_regbeta(cs_bucket_zscore(day_first(Volume), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 60)` |
| knockout | `cross_ema(day_first(Volume), 20)` | -0.73 | +0.19 | -0.73 | +1.31 | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(day_first(Volume), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 60)` |
| swap | `Volume->Amt` | +0.32 | +0.62 | +0.32 | — | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Amt), 20), cs_bucket_zscore(cross_ema(day_first(Amt), 20), cross_mean(day_sum(Amt), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 60)` |
| swap | `Amt->Volume` | — | — | — | — | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Volume, Close)), 60)` |
| window | `cross_regbeta@60->30` | +0.09 | +0.13 | +0.09 | — | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 30)` |
| window | `cross_regbeta@60->120` | +0.47 | +0.57 | +0.47 | — | `cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 120)` |

### head score -0.25:`ts_std(ts_std(day_last(Amt), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(day_last(Amt), 50)` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| swap | `Amt->Volume` | -2.15 | -1.12 | -2.15 | — | `ts_std(ts_std(day_last(Volume), 50), 50)` |
| window | `ts_std@50->25` | -0.29 | -0.29 | +0.89 | — | `ts_std(ts_std(day_last(Amt), 50), 25)` |
| window | `ts_std@50->100` | -0.26 | -0.10 | -0.26 | — | `ts_std(ts_std(day_last(Amt), 50), 100)` |

### head score -0.49:`ts_regbeta(day_last(Amt), day_durbin_watson(Open), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Open)` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| swap | `Amt->Volume` | -1.85 | -0.95 | -1.85 | — | `ts_regbeta(day_last(Volume), day_durbin_watson(Open), 10)` |
| swap | `Open->Close` | -0.33 | -0.16 | -0.33 | — | `ts_regbeta(day_last(Amt), day_durbin_watson(Close), 10)` |
| window | `ts_regbeta@10->5` | -1.16 | -0.78 | -1.16 | — | `ts_regbeta(day_last(Amt), day_durbin_watson(Open), 5)` |
| window | `ts_regbeta@10->20` | +0.02 | +0.52 | +0.02 | — | `ts_regbeta(day_last(Amt), day_durbin_watson(Open), 20)` |

### head score -0.52:`ts_std(day_last(Amt), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| swap | `Amt->Volume` | -1.42 | -1.06 | -1.42 | — | `ts_std(day_last(Volume), 50)` |
| window | `ts_std@50->25` | -1.56 | -1.56 | -0.48 | — | `ts_std(day_last(Amt), 25)` |
| window | `ts_std@50->100` | -0.53 | -0.53 | -0.18 | — | `ts_std(day_last(Amt), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_wstd(Amt, Vwap)` — enrichment,均值差 +1.88,p 0.000
2. `cross_mean(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 20)` — enrichment,均值差 +1.74,p 0.000
3. `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)))` — enrichment,均值差 +1.71,p 0.001
4. `cross_mean(ts_min(day_min(Close), 1), 30)` — enrichment,均值差 +1.67,p 0.003
5. `ts_min(day_min(Close), 1)` — enrichment,均值差 +1.67,p 0.003
6. `cross_mean(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 30)` — enrichment,均值差 +1.50,p 0.002
7. `neg(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)))` — enrichment,均值差 +1.42,p 0.006
8. `day_min(Close)` — enrichment,均值差 +1.41,p 0.004
9. `cross_mean(cross_ema(day_first(Volume), 20), 30)` — enrichment,均值差 +1.22,p 0.019
10. `cross_mean(day_sum(Volume), 30)` — enrichment,均值差 +1.19,p 0.000
11. `day_sum(Volume)` — enrichment,均值差 +1.14,p 0.000
12. `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` — enrichment,均值差 +1.11,p 0.000
13. `cross_ema(day_first(Volume), 20)` — enrichment,均值差 +1.08,p 0.000
14. `day_first(Volume)` — enrichment,均值差 +1.00,p 0.000
15. `mul(day_last(Close), day_first(Open))` — enrichment,均值差 +0.96,p 0.054
16. `ts_std(day_last(Amt), 50)` — enrichment,均值差 +0.87,p 0.064

## 本组之前各轮的任务

- `prods2032Pr1a_Ea`:核心 `day_first(Volume)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 1391, 'c05_skeleton': 673}
  - score +0.03(train +0.03 valid +0.42):`cs_bucket_zscore(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), cross_mean(day_sum(Volume), 30))`
  - score +0.03(train +0.03 valid +0.42):`cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))`
  - score -0.10(train +0.07 valid -0.10):`cs_bucket_zscore(cross_ema(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 20), cross_mean(day_sum(Volume), 30))`
  - score -0.26(train -0.26 valid -0.23):`cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(cross_mean(day_sum(Volume), 30), 30))`
  - score -0.29(train -0.14 valid -0.29):`cs_bucket_zscore(cross_ema(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(cross_mean(day_sum(Volume), 30), 30)), 20), cross_mean(cross_mean(day_sum(Volume), 30), 30))`
- `prods2032Pr1b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.83(train +0.00 valid -0.83):`div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), add(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(High), 1)), 1)), 40), cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))`
  - score -0.84(train -0.06 valid -0.84):`div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), add(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))`
  - score -0.84(train -0.06 valid -0.84):`div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), add(cross_mean(abs_(sub(div(day_first(High), ts_delay(day_last(Close), 1)), 1)), 40), cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))`
  - score -0.84(train -0.06 valid -0.84):`div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), add(cross_mean(abs_(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1))), 40), cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))`
  - score -0.86(train +0.04 valid -0.86):`div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), add(cross_mean(abs_(sub(div(day_first(Open), ts_delay(ts_delay(day_last(High), 1), 1)), 1)), 40), cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))`
- `prods2032Pr2a_Ea`:核心 `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))`;评分 92,过线 2,入 heads 1;采样计数 {'c05_no_core': 918, 'c05_skeleton': 422, 'mutation_refused': 8, 'c05_periphery_seen': 7}
  - score +0.58(train +0.67 valid +0.58):`cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Close)), 60)`
  - score +0.51(train +0.51 valid +0.63):`cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Vwap)), 60)`
  - score +0.47(train +0.47 valid +0.58):`cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))), cs_quantile_q75(day_wstd(Amt, Volume)), 60)`
  - score +0.40(train +0.40 valid +0.98):`div(cross_mean(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), 20), add(cross_stddev(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(cs_bucket_zscore(cross_ema(day_first(Volume), 20), day_first(Volume)), 30)), 60), 1))`
  - score +0.37(train +0.37 valid +0.75):`cross_regbeta(cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30)), cs_quantile_q75(day_wstd(Amt, Volume)), 60)`
- `prods2032Pr2b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score +0.17(train +0.44 valid +0.17):`cross_regbeta(ts_delay(mul(sub(day_sum(Volume), 1), cross_zscore(log(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)), 10)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 120)`
  - score +0.11(train +0.11 valid +0.65):`cross_regbeta(ts_delay(mul(sub(day_sum(Volume), 1), cross_zscore(log(add(day_sum(Volume), 1)), 10)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 120)`
  - score -0.02(train +0.33 valid -0.02):`cross_regbeta(ts_delay(mul(sub(ts_delay(mul(sub(day_sum(Volume), 1), cross_zscore(log(add(day_sum(Amt), 1)), 10)), 1), 1), cross_zscore(log(add(day_sum(Amt), 1)), 60)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 120)`
  - score -0.24(train -0.18 valid -0.24):`cross_regbeta(ts_delay(mul(sub(mul(day_last(Close), day_first(Open)), mul(sub(mul(day_last(Close), day_first(Open)), 1), cross_zscore(log(add(day_sum(Volume), 1)), 60))), cross_zscore(log(add(day_sum(Volume), 1)), 60)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 120)`
  - score -0.51(train -0.51 valid +0.12):`cross_regbeta(ts_delay(mul(sub(mul(day_last(Close), day_first(Open)), 2), cross_zscore(log(add(day_sum(Volume), 1)), 60)), 1), sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.51(window ts_regbeta@10->20):`ts_regbeta(day_last(Amt), day_durbin_watson(Open), 20)`
- 增益 +0.17(swap Open->Close):`ts_regbeta(day_last(Amt), day_durbin_watson(Close), 10)`
