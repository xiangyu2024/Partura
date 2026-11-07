# 定位:种子 909,P 组,第 2 轮(只含 train / valid)

快照:prods909M1_I0_open_search, prods909M2_I0_open_search, prods909Pr1a_Na, prods909Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(4 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.10 | +1.10 | +2.41 | +1 | 20 | prods909M2_I0_open_search | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))))` |
| +0.99 | +0.99 | +2.76 | -1 | 5 | prods909M2_I0_open_search | `cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` |
| +0.66 | +0.66 | +2.11 | +1 | 5 | prods909M2_I0_open_search | `cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(1, day_quantile(inv(Vwap))))` |
| +0.58 | +0.58 | +1.51 | +1 | 5 | prods909Pr1b_Nb | `cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 30)` |

## 共性:343 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.44 | 0.003 | 4 | +0.30 / -1.14 | `day_wmean(is_lt(in_index(Amt), 0.125), Amt)` |
| +1.44 | 0.000 | 14 | +0.25 / -1.18 | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close)))` |
| +1.37 | 0.000 | 15 | +0.18 / -1.18 | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` |
| +1.31 | 0.004 | 4 | +0.17 / -1.14 | `abs_(day_quantile(inv(Close)))` |
| +1.30 | 0.000 | 19 | +0.10 / -1.20 | `day_quantile(inv(Close))` |
| +1.19 | 0.005 | 6 | +0.05 / -1.15 | `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` |
| +1.10 | 0.000 | 26 | -0.11 / -1.21 | `day_quantile(inv(Vwap))` |
| +0.88 | 0.000 | 61 | -0.40 / -1.28 | `day_first(Volume)` |
| +0.63 | 0.080 | 6 | -0.51 / -1.14 | `neg(cs_rank(neg(LogFloatShares)))` |
| +0.61 | 0.058 | 4 | -0.52 / -1.13 | `day_skew(Close)` |
| +0.60 | 0.023 | 9 | -0.54 / -1.14 | `neg(neg(LogFloatShares))` |
| +0.56 | 0.004 | 27 | -0.60 / -1.17 | `neg(LogFloatShares)` |
| +0.52 | 0.007 | 13 | -0.63 / -1.14 | `pow_1_5(LogFloatShares)` |
| +0.48 | 0.082 | 13 | -0.66 / -1.14 | `cs_rank(neg(LogFloatShares))` |
| +0.42 | 0.048 | 9 | -0.71 / -1.14 | `cs_rank(pow_1_5(LogFloatShares))` |
| +0.36 | 0.223 | 4 | -0.77 / -1.13 | `div(day_last(Close), day_first(Open))` |
| +0.31 | 0.185 | 6 | -0.82 / -1.13 | `day_mean(Ret)` |
| +0.27 | 0.191 | 5 | -0.86 / -1.13 | `cs_rank(cs_rank(pow_1_5(LogFloatShares)))` |
| +0.27 | 0.354 | 7 | -0.86 / -1.13 | `ts_stddev(div(day_es_ratio_hi(Close), 5), 50)` |
| +0.26 | 0.093 | 52 | -0.90 / -1.16 | `day_min(Ret)` |

## 拆解(24 次评估)

### head score +1.10:`cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` | +0.68 | +0.68 | +2.05 | — | (子树本身) |
| sufficiency | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +0.85 | +0.85 | +2.44 | — | (子树本身) |
| sufficiency | `abs_(day_min(Ret))` | -2.96 | -1.98 | -2.96 | — | (子树本身) |
| knockout | `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` | -1.65 | -1.65 | -0.96 | +2.74 | `cs_last_high40(abs_(day_min(Ret)), abs_(day_min(Ret)))` |
| knockout | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | -2.43 | -0.80 | -2.43 | +3.53 | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), day_quantile(inv(Vwap))))` |
| knockout | `abs_(day_min(Ret))` | -0.35 | -0.35 | +0.68 | +1.44 | `cs_last_high40(day_min(Ret), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))))` |
| knockout | `abs_(day_min(Ret))` | -0.36 | -0.36 | +1.19 | +1.45 | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(day_min(Ret), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))))` |
| swap | `Volume->Amt` | +1.22 | +1.22 | +2.74 | — | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))))` |
| swap | `Vwap->Close` | +1.10 | +1.10 | +2.41 | — | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close)))))` |

### head score +0.99:`cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +0.85 | +0.85 | +2.44 | — | (子树本身) |
| sufficiency | `day_quantile(inv(Vwap))` | -1.35 | -1.35 | -0.41 | — | (子树本身) |
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +0.42 | +0.42 | +1.71 | +0.56 | `cs_last_high40(day_quantile(inv(Vwap)), day_quantile(inv(Vwap)))` |
| knockout | `mul(day_first(Volume), 1)` | +0.99 | +0.99 | +2.76 | -0.00 | `cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(day_first(Volume), day_quantile(inv(Vwap))))` |
| swap | `Vwap->Close` | +0.97 | +0.97 | +2.80 | — | `cs_last_high40(day_quantile(inv(Close)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close))))` |
| swap | `Volume->Amt` | +0.94 | +0.94 | +2.91 | — | `cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))))` |

### head score +0.66:`cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(1, day_quantile(inv(Vwap))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_high20(1, day_quantile(inv(Vwap)))` | -0.80 | -0.80 | +1.46 | — | (子树本身) |
| sufficiency | `day_quantile(inv(Vwap))` | -1.35 | -1.35 | -0.41 | — | (子树本身) |
| knockout | `cs_first_high20(1, day_quantile(inv(Vwap)))` | +0.42 | +0.42 | +1.71 | +0.23 | `cs_last_high40(day_quantile(inv(Vwap)), day_quantile(inv(Vwap)))` |
| swap | `Vwap->Close` | +0.64 | +0.64 | +2.11 | — | `cs_last_high40(day_quantile(inv(Close)), cs_first_high20(1, day_quantile(inv(Close))))` |

### head score +0.58:`cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt)` | +0.13 | +0.13 | +0.22 | — | (子树本身) |
| swap | `Amt->Volume` | +0.58 | +0.58 | +1.50 | — | `cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Volume), 0.125)), 0.125), Volume), 30)` |
| window | `cross_mean@30->15` | +0.52 | +0.52 | +0.80 | — | `cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 15)` |
| window | `cross_mean@30->60` | +0.47 | +0.47 | +0.56 | — | `cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` — ablation,自身 score +0.85(所在 head +1.10)
2. `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` — ablation,自身 score +0.68(所在 head +1.10)
3. `day_wmean(is_lt(in_index(Amt), 0.125), Amt)` — enrichment,均值差 +1.44,p 0.003
4. `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close)))` — enrichment,均值差 +1.44,p 0.000
5. `abs_(day_quantile(inv(Close)))` — enrichment,均值差 +1.31,p 0.004
6. `day_quantile(inv(Close))` — enrichment,均值差 +1.30,p 0.000
7. `day_quantile(inv(Vwap))` — enrichment,均值差 +1.10,p 0.000
8. `day_first(Volume)` — enrichment,均值差 +0.88,p 0.000
9. `neg(cs_rank(neg(LogFloatShares)))` — enrichment,均值差 +0.63,p 0.080
10. `day_skew(Close)` — enrichment,均值差 +0.61,p 0.058
11. `neg(neg(LogFloatShares))` — enrichment,均值差 +0.60,p 0.023
12. `neg(LogFloatShares)` — enrichment,均值差 +0.56,p 0.004
13. `pow_1_5(LogFloatShares)` — enrichment,均值差 +0.52,p 0.007
14. `cs_rank(neg(LogFloatShares))` — enrichment,均值差 +0.48,p 0.082
15. `cs_rank(pow_1_5(LogFloatShares))` — enrichment,均值差 +0.42,p 0.048
16. `day_min(Ret)` — enrichment,均值差 +0.26,p 0.093

## 本组之前各轮的任务

- `prods909Pr1a_Na`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {}
  - score +0.37(train +0.37 valid +0.47):`div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), cross_mean(day_max(in_pct(Close, 60)), 60))`
  - score +0.20(train +0.20 valid +0.46):`div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), cross_mean(day_max(in_pct(Close, 5)), 60))`
  - score +0.20(train +0.20 valid +0.45):`div(cross_mean(day_max(in_pct(Close, 5)), 60), ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50))`
  - score -0.01(train -0.01 valid +0.08):`div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), ts_std(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50))`
  - score -0.16(train -0.16 valid +0.09):`mul(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), cross_mean(day_max(in_pct(Close, 5)), 60))`
- `prods909Pr1b_Nb`:核心 `—`;评分 82,过线 9,入 heads 1;采样计数 {}
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(in_index(Amt)), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(cross_quantile_q50(Open, 30)), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(Close), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(in_median(Amt)), 0.125), Amt), 30)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(swap Volume->Amt):`cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))))`
