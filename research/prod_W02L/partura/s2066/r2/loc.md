# 定位:种子 2066,P 组,第 2 轮(只含 train / valid)

快照:prods2066M1_I0_open_search, prods2066M2_I0_open_search, prods2066Pr1a_Na, prods2066Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.14 | -0.76 | -1.14 | -1 | 20 | prods2066M1_I0_open_search | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` |
| -1.14 | -0.76 | -1.14 | -1 | 20 | prods2066M1_I0_open_search | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))))` |
| -1.15 | -0.83 | -1.15 | -1 | 20 | prods2066M1_I0_open_search | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)))))` |
| -2.31 | -2.31 | -1.87 | +1 | 5 | prods2066M2_I0_open_search | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` |
| -2.34 | -2.34 | -2.12 | +1 | 5 | prods2066M2_I0_open_search | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` |
| -3.86 | -3.61 | -3.86 | -1 | 20 | prods2066M2_I0_open_search | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume)))), 20)` |

## 共性:109 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.37 | 0.000 | 5 | -0.52 / -2.89 | `day_centroid(pow_3(pow_1_5(Volume)))` |
| +1.83 | 0.004 | 4 | -1.02 / -2.85 | `day_hurst(cross_ema(pow_1_5(Volume), 60))` |
| +0.52 | 0.227 | 11 | -2.31 / -2.83 | `day_var(Open)` |
| +0.40 | 0.330 | 7 | -2.40 / -2.80 | `cross_delay(day_var(Open), 60)` |
| +0.38 | 0.203 | 17 | -2.45 / -2.84 | `day_signed_ratio(Ret, Open)` |
| -0.33 | 0.690 | 7 | -3.08 / -2.76 | `day_signed_ratio(Close, Low)` |
| -0.82 | 0.921 | 9 | -3.53 / -2.71 | `day_es_ratio_lo(Ret)` |
| -1.05 | 0.971 | 5 | -3.78 / -2.73 | `day_kurt(div(Volume, in_sum(Volume)))` |
| -1.17 | 0.978 | 5 | -3.89 / -2.72 | `day_skew(div(Volume, in_sum(Volume)))` |
| -1.26 | 0.999 | 15 | -3.86 / -2.61 | `day_q_stat_std(Vwap)` |
| -1.41 | 0.998 | 12 | -4.03 / -2.62 | `inv(day_q_stat_std(Vwap))` |
| -1.48 | 0.996 | 9 | -4.13 / -2.66 | `day_signed_ratio(Ret, Amt)` |

## 拆解(15 次评估)

### head score -2.31:`cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(div(Volume, in_sum(Volume)))` | -5.21 | -4.17 | -5.21 | — | (子树本身) |
| swap | `Volume->Amt` | -2.41 | -2.41 | -1.64 | — | `cross_stddev(day_skew(div(Amt, in_sum(Amt))), 20)` |
| window | `cross_stddev@20->10` | -2.59 | -2.59 | -2.42 | — | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 10)` |
| window | `cross_stddev@20->40` | -2.13 | -2.13 | -1.48 | — | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 40)` |

### head score -2.34:`cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(div(Volume, in_sum(Volume)))` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| swap | `Volume->Amt` | -2.35 | -2.35 | -1.98 | — | `cross_stddev(day_kurt(div(Amt, in_sum(Amt))), 20)` |
| window | `cross_stddev@20->10` | -2.87 | -2.87 | -2.75 | — | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 10)` |
| window | `cross_stddev@20->40` | -2.42 | -2.42 | -1.67 | — | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 40)` |

### head score -3.86:`cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume))))` | -4.56 | -4.36 | -4.56 | — | (子树本身) |
| sufficiency | `day_skew(div(Volume, in_sum(Volume)))` | -5.21 | -4.17 | -5.21 | — | (子树本身) |
| sufficiency | `day_kurt(div(Volume, in_sum(Volume)))` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| knockout | `div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume))))` | -2.31 | -2.31 | -1.84 | -1.55 | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` |
| swap | `Volume->Amt` | -3.85 | -3.58 | -3.85 | — | `cross_stddev(div(day_skew(div(Amt, in_sum(Amt))), day_kurt(div(Amt, in_sum(Amt)))), 20)` |
| window | `cross_stddev@20->10` | -3.81 | -3.81 | -3.81 | — | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume)))), 10)` |
| window | `cross_stddev@20->40` | -3.87 | -3.10 | -3.87 | — | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume)))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(pow_3(pow_1_5(Volume)))` — enrichment,均值差 +2.37,p 0.000
2. `day_hurst(cross_ema(pow_1_5(Volume), 60))` — enrichment,均值差 +1.83,p 0.004

## 本组之前各轮的任务

- `prods2066Pr1a_Na`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.34(train -0.34 valid -0.12):`cross_min(cross_semistd_pos(day_centroid(pow_3(pow_1_5(Volume))), 10), 10)`
  - score -0.38(train -0.21 valid -0.38):`cross_min(day_hurst(cross_ema(pow_1_5(cross_ema(pow_1_5(Volume), 60)), 60)), 10)`
  - score -0.47(train -0.19 valid -0.47):`cross_min(cross_min(day_centroid(pow_3(pow_1_5(Volume))), 10), 10)`
  - score -0.50(train -0.50 valid -0.12):`cross_min(day_centroid(pow_3(pow_1_5(Volume))), 10)`
  - score -0.55(train -0.55 valid +0.06):`cross_min(cross_min(day_centroid(pow_3(pow_1_5(Volume))), 10), 241)`
- `prods2066Pr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -1.25(train -0.93 valid -1.25):`cross_regbeta(cross_delay(day_var(Open), 60), inv(day_es_ratio_lo(Ret)), 10)`
  - score -1.39(train -0.81 valid -1.39):`cross_regbeta(cross_delay(day_var(Open), 3), day_es_ratio_lo(Ret), 10)`
  - score -1.44(train -1.44 valid -1.19):`cross_regbeta(cross_delay(day_var(Open), 60), inv(day_q_stat_std(Vwap)), 10)`
  - score -1.63(train -1.53 valid -1.63):`cross_regbeta(cross_delay(day_var(Open), 60), day_signed_ratio(Ret, Open), 10)`
  - score -2.03(train -2.03 valid -1.96):`mul(day_signed_ratio(Close, Low), day_signed_ratio(Ret, Open))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window cross_stddev@20->40):`cross_stddev(day_skew(div(Volume, in_sum(Volume))), 40)`
