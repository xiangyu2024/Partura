# 定位:种子 2016,P 组,第 2 轮(只含 train / valid)

快照:prods2016M1_I0_open_search, prods2016M2_I0_open_search, prods2016Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.30 | -1.27 | -1.30 | +1 | 20 | prods2016M1_I0_open_search | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 30)` |
| -2.35 | -1.59 | -2.35 | +1 | 20 | prods2016M1_I0_open_search | `sub(day_kurt(Ret), day_quantile_q25(Open))` |
| -2.39 | -1.59 | -2.39 | -1 | 5 | prods2016M2_I0_open_search | `pow_05(day_close(Close))` |
| -2.39 | -1.60 | -2.39 | -1 | 5 | prods2016M2_I0_open_search | `pow_05(day_close(Vwap))` |
| -2.42 | -1.61 | -2.42 | -1 | 5 | prods2016M1_I0_open_search | `abs_(day_quantile_q25(Open))` |
| -2.74 | -2.08 | -2.74 | +1 | 20 | prods2016M2_I0_open_search | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40))))` |

## 共性:77 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.97 | 0.005 | 7 | -1.75 / -2.71 | `day_first(Close)` |
| +0.89 | 0.012 | 6 | -1.80 / -2.69 | `day_signed_ratio(sub(Close, day_first(Open)), Close)` |
| +0.84 | 0.020 | 6 | -1.85 / -2.69 | `day_signed_ratio(sub(Close, day_first(Close)), Amt)` |
| +0.74 | 0.119 | 4 | -1.92 / -2.66 | `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60)` |
| +0.73 | 0.054 | 7 | -1.96 / -2.69 | `sub(day_topw_mean(Ret, Amt), day_mean(Ret))` |
| +0.54 | 0.029 | 19 | -2.21 / -2.76 | `day_first(Open)` |
| +0.50 | 0.130 | 8 | -2.18 / -2.68 | `day_topw_mean(Ret, Amt)` |
| +0.47 | 0.074 | 15 | -2.25 / -2.72 | `div(day_last(Close), cross_delay(day_last(Close), 1))` |
| +0.15 | 0.419 | 12 | -2.50 / -2.65 | `day_signed_ratio(sub(Close, day_first(Open)), Amt)` |
| +0.02 | 0.422 | 5 | -2.61 / -2.62 | `day_signed_ratio(Ret, Ret)` |
| -0.05 | 0.508 | 15 | -2.66 / -2.61 | `day_mean(Ret)` |
| -0.18 | 0.769 | 30 | -2.73 / -2.56 | `day_last(Close)` |
| -0.28 | 0.861 | 26 | -2.81 / -2.53 | `cross_delay(day_last(Close), 1)` |
| -0.50 | 0.822 | 7 | -3.08 / -2.58 | `day_quantile_q25(Open)` |
| -0.66 | 0.967 | 6 | -3.23 / -2.57 | `day_signed_ratio(sub(Close, cross_delay(day_last(Close), 1)), Amt)` |
| -0.93 | 0.922 | 5 | -3.49 / -2.56 | `day_signed_ratio(sub(Close, cross_delay(day_last(Close), 1)), Close)` |
| -1.10 | 0.995 | 5 | -3.65 / -2.55 | `pow_05(day_close(Amt))` |
| -1.16 | 0.998 | 6 | -3.69 / -2.53 | `day_close(Amt)` |

## 拆解(14 次评估)

### head score -2.39:`pow_05(day_close(Close))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_close(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| swap | `Close->Vwap` | -2.35 | -1.60 | -2.35 | — | `pow_05(day_close(Vwap))` |

### head score -2.39:`pow_05(day_close(Vwap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_close(Vwap)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| swap | `Vwap->Close` | -2.35 | -1.60 | -2.35 | — | `pow_05(day_close(Close))` |

### head score -2.74:`pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40)))` | -2.69 | -2.08 | -2.69 | — | (子树本身) |
| sufficiency | `pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40))` | -2.69 | -2.07 | -2.69 | — | (子树本身) |
| sufficiency | `ts_quantile_q50(inv(pow_05(day_close(Amt))), 40)` | -2.69 | -2.07 | -2.69 | — | (子树本身) |
| sufficiency | `inv(pow_05(day_close(Amt)))` | -3.85 | -3.33 | -3.85 | — | (子树本身) |
| knockout | `pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40)))` | -2.69 | -2.07 | -2.69 | -0.05 | `pow_2(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40)))` |
| knockout | `ts_quantile_q50(inv(pow_05(day_close(Amt))), 40)` | -3.85 | -3.33 | -3.85 | +1.11 | `pow_2(pow_05(pow_05(inv(pow_05(day_close(Amt))))))` |
| knockout | `inv(pow_05(day_close(Amt)))` | -2.70 | -2.09 | -2.70 | -0.04 | `pow_2(pow_05(pow_05(ts_quantile_q50(pow_05(day_close(Amt)), 40))))` |
| swap | `Amt->Volume` | -1.72 | -1.36 | -1.72 | — | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Volume))), 40))))` |
| window | `ts_quantile_q50@40->20` | -3.42 | -2.49 | -3.42 | — | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 20))))` |
| window | `ts_quantile_q50@40->80` | -2.75 | -1.82 | -2.75 | — | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 80))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_first(Close)` — enrichment,均值差 +0.97,p 0.005
2. `day_signed_ratio(sub(Close, day_first(Open)), Close)` — enrichment,均值差 +0.89,p 0.012
3. `day_signed_ratio(sub(Close, day_first(Close)), Amt)` — enrichment,均值差 +0.84,p 0.020
4. `sub(day_topw_mean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +0.73,p 0.054
5. `day_first(Open)` — enrichment,均值差 +0.54,p 0.029
6. `div(day_last(Close), cross_delay(day_last(Close), 1))` — enrichment,均值差 +0.47,p 0.074

## 本组之前各轮的任务

- `prods2016Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.71(train -0.71 valid -0.46):`cross_mean(day_wmean(Ret, Ret), 60)`
  - score -0.71(train -0.71 valid -0.70):`cross_corr(cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60), sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 60)`
  - score -1.14(train -1.14 valid -0.31):`cross_mean(sub(day_signed_ratio(sub(Close, day_first(Close)), Ret), day_signed_ratio(sub(Close, day_first(Ret)), Close)), 241)`
  - score -1.14(train -1.14 valid -0.61):`cross_mean(sub(day_signed_ratio(sub(Close, day_first(Open)), Amt), day_signed_ratio(sub(Close, day_first(Ret)), Close)), 241)`
  - score -1.14(train -1.14 valid -0.61):`cross_mean(sub(day_signed_ratio(sub(Close, day_first(Close)), Amt), day_signed_ratio(sub(Close, day_first(Ret)), Close)), 241)`

## 比原 head 好的拆解变体(R 候选)

(没有)
