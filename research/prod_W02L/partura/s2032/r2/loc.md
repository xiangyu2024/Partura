# 定位:种子 2032,P 组,第 2 轮(只含 train / valid)

快照:prods2032M1_I0_open_search, prods2032M2_I0_open_search, prods2032Pr1a_Ea, prods2032Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.12 | -1.12 | -1.12 | -1 | 0 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 60)` |
| -1.15 | -1.15 | -1.09 | -1 | 5 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 5)` |
| -1.20 | -1.20 | -1.03 | -1 | 5 | prods2032M1_I0_open_search | `cross_sum(day_first(Volume), 3)` |
| -1.63 | -1.62 | -1.63 | -1 | 20 | prods2032M2_I0_open_search | `div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| -1.79 | -1.66 | -1.79 | -1 | 0 | prods2032M2_I0_open_search | `ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 80)` |
| -1.80 | -1.80 | -1.59 | -1 | 20 | prods2032M2_I0_open_search | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5)), 0.5)` |

## 共性:107 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.54 | 0.000 | 10 | -0.71 / -2.25 | `cross_mean(day_sum(Volume), 30)` |
| +1.07 | 0.000 | 44 | -1.47 / -2.55 | `day_first(Volume)` |
| +1.01 | 0.093 | 4 | -1.13 / -2.14 | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` |
| +1.00 | 0.001 | 21 | -1.30 / -2.30 | `cross_ema(day_first(Volume), 20)` |
| +0.68 | 0.006 | 25 | -1.59 / -2.26 | `day_sum(Volume)` |
| +0.29 | 0.172 | 25 | -1.88 / -2.17 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.29 | 0.171 | 23 | -1.88 / -2.17 | `div(day_last(Close), day_first(Open))` |
| +0.05 | 0.350 | 7 | -2.06 / -2.11 | `day_last(High)` |
| +0.01 | 0.300 | 5 | -2.10 / -2.10 | `ts_delay(day_last(High), 1)` |
| -0.18 | 0.846 | 39 | -2.22 / -2.04 | `day_first(Open)` |
| -0.52 | 0.975 | 41 | -2.42 / -1.91 | `ts_delay(day_last(Close), 1)` |
| -0.54 | 0.988 | 48 | -2.40 / -1.86 | `day_last(Close)` |
| -0.68 | 0.855 | 4 | -2.76 / -2.08 | `div(day_sum(Amt), day_sum(Volume))` |
| -0.92 | 0.942 | 5 | -2.98 / -2.06 | `day_sum(Amt)` |
| -0.97 | 0.873 | 4 | -3.04 / -2.07 | `day_close(Low)` |
| -1.19 | 0.999 | 14 | -3.14 / -1.95 | `div(day_last(Close), ts_delay(day_last(Close), 1))` |

## 拆解(32 次评估)

### head score -1.63:`div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 60)` | -1.83 | -1.42 | -1.83 | — | (子树本身) |
| sufficiency | `div(day_last(Close), ts_delay(day_last(Close), 1))` | -4.40 | -4.40 | -4.07 | — | (子树本身) |
| sufficiency | `ts_sum(div(day_sum(Amt), day_sum(Volume)), 60)` | -1.65 | -1.39 | -1.65 | — | (子树本身) |
| sufficiency | `ts_delay(day_last(Close), 1)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume)))` | — | — | — | — | `div(ts_sum(div(day_sum(Amt), day_sum(Volume)), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| knockout | `sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)` | -1.97 | -1.97 | -1.85 | +0.34 | `div(ts_sum(mul(div(day_last(Close), ts_delay(day_last(Close), 1)), div(day_sum(Amt), day_sum(Volume))), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| knockout | `div(day_last(Close), ts_delay(day_last(Close), 1))` | -2.38 | -1.62 | -2.38 | +0.74 | `div(ts_sum(mul(sub(day_last(Close), 1), div(day_sum(Amt), day_sum(Volume))), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| knockout | `ts_sum(div(day_sum(Amt), day_sum(Volume)), 60)` | -1.72 | -1.62 | -1.72 | +0.09 | `div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 60), div(day_sum(Amt), day_sum(Volume)))` |
| swap | `Close->Vwap` | -1.66 | -1.63 | -1.66 | — | `div(ts_sum(mul(sub(div(day_last(Vwap), ts_delay(day_last(Vwap), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 60), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| swap | `Amt->Volume` | -1.73 | -1.65 | -1.73 | — | `div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Volume), day_sum(Volume))), 60), ts_sum(div(day_sum(Volume), day_sum(Volume)), 60))` |
| window | `ts_sum@60->30` | -2.00 | -1.79 | -2.00 | — | `div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 30), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |
| window | `ts_sum@60->120` | -1.69 | -1.69 | -1.56 | — | `div(ts_sum(mul(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), div(day_sum(Amt), day_sum(Volume))), 120), ts_sum(div(day_sum(Amt), day_sum(Volume)), 60))` |

### head score -1.79:`ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 80)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_last(Close), ts_delay(day_last(Close), 1))` | -4.40 | -4.40 | -4.07 | — | (子树本身) |
| sufficiency | `ts_delay(day_last(Close), 1)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_last(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)` | -1.74 | -1.66 | -1.74 | -0.06 | `ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 80)` |
| knockout | `div(day_last(Close), ts_delay(day_last(Close), 1))` | -2.08 | -1.67 | -2.08 | +0.29 | `ts_stddev(sub(day_last(Close), 1), 80)` |
| knockout | `ts_delay(day_last(Close), 1)` | — | — | — | — | `ts_stddev(sub(div(day_last(Close), day_last(Close)), 1), 80)` |
| swap | `Close->Vwap` | -1.73 | -1.67 | -1.73 | — | `ts_stddev(sub(div(day_last(Vwap), ts_delay(day_last(Vwap), 1)), 1), 80)` |
| window | `ts_stddev@80->40` | -1.96 | -1.96 | -1.37 | — | `ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 40)` |
| window | `ts_stddev@80->160` | -2.05 | -1.82 | -2.05 | — | `ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 160)` |

### head score -1.80:`sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5)), 0.5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5))` | -1.80 | -1.80 | -1.53 | — | (子树本身) |
| sufficiency | `ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20)` | -1.96 | -1.96 | -1.61 | — | (子树本身) |
| sufficiency | `div(day_last(Close), ts_delay(day_last(Close), 1))` | -4.40 | -4.40 | -4.07 | — | (子树本身) |
| knockout | `cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5))` | — | — | — | — | `sub(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5), 0.5)` |
| knockout | `select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))` | -1.58 | -1.58 | -1.47 | -0.22 | `sub(cs_rank(ts_argmax(signedpower(ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20)), 5)), 0.5)` |
| knockout | `sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)` | -2.12 | -2.12 | -1.80 | +0.32 | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(div(day_last(Close), ts_delay(day_last(Close), 1)), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 5)), 0.5)` |
| knockout | `sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1)` | -1.80 | -1.80 | -1.53 | +0.00 | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20), day_last(Close))), 5)), 0.5)` |
| swap | `Close->Vwap` | -1.83 | -1.83 | -1.52 | — | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Vwap), ts_delay(day_last(Vwap), 1)), 1), 0), ts_stddev(sub(div(day_last(Vwap), ts_delay(day_last(Vwap), 1)), 1), 20), day_last(Vwap))), 5)), 0.5)` |
| window | `ts_argmax@5->2` | -1.68 | -1.41 | -1.68 | — | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 2)), 0.5)` |
| window | `ts_argmax@5->10` | -3.13 | -3.13 | -2.75 | — | `sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 10)), 0.5)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_sum(Volume), 30)` — enrichment,均值差 +1.54,p 0.000
2. `day_first(Volume)` — enrichment,均值差 +1.07,p 0.000
3. `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` — enrichment,均值差 +1.01,p 0.093
4. `cross_ema(day_first(Volume), 20)` — enrichment,均值差 +1.00,p 0.001
5. `day_sum(Volume)` — enrichment,均值差 +0.68,p 0.006

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.22(knockout select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))):`sub(cs_rank(ts_argmax(signedpower(ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20)), 5)), 0.5)`
- 增益 +0.12(window ts_argmax@5->2):`sub(cs_rank(ts_argmax(signedpower(select_where(is_lt(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 0), ts_stddev(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 20), day_last(Close))), 2)), 0.5)`
