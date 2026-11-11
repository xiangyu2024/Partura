# 定位:种子 2075,P 组,第 1 轮(只含 train / valid)

快照:prods2075M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.53 | -0.53 | +0.01 | -1 | 20 | prods2075M1_I0_open_search | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))))` |
| -1.12 | -1.12 | -0.75 | +1 | 5 | prods2075M1_I0_open_search | `cross_autocorr_s1(day_cov(Ret, Volume), 241)` |
| -1.46 | -1.46 | -0.73 | +1 | 5 | prods2075M1_I0_open_search | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 15))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |

## 共性:47 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.56 | 0.097 | 7 | -2.37 / -2.93 | `day_last(Close)` |
| +0.27 | 0.432 | 4 | -2.59 / -2.86 | `day_sum(Volume)` |

## 拆解(27 次评估)

### head score -0.53:`abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5))))` | -1.79 | -1.79 | -1.28 | — | (子树本身) |
| sufficiency | `cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))` | -1.79 | -1.79 | -1.28 | — | (子树本身) |
| sufficiency | `div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5)` | -1.49 | -1.49 | -1.29 | — | (子树本身) |
| knockout | `cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5))))` | -1.79 | -1.79 | -1.28 | +1.25 | `abs_(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5))))` |
| knockout | `cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))` | — | — | — | — | `abs_(cs_demean(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5))))` |
| knockout | `div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5))` | -2.73 | -1.02 | -2.73 | +2.20 | `abs_(cs_demean(cs_rank(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5))))` |
| knockout | `mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume))` | -1.47 | -0.47 | -1.47 | +0.94 | `abs_(cs_demean(cs_rank(div(ts_sum(day_sum(Volume), 5), ts_sum(day_sum(Volume), 5)))))` |
| swap | `Close->Vwap` | -0.54 | -0.54 | -0.02 | — | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Vwap), ts_delay(day_last(Vwap), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))))` |
| swap | `Amt->Volume` | -1.38 | -0.53 | -1.38 | — | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Volume), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))))` |
| window | `ts_sum@5->2` | -1.78 | -1.78 | -1.06 | — | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 2), ts_sum(day_sum(Volume), 5)))))` |
| window | `ts_sum@5->10` | -1.84 | -1.84 | -0.28 | — | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 10), ts_sum(day_sum(Volume), 5)))))` |

### head score -1.12:`cross_autocorr_s1(day_cov(Ret, Volume), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Ret, Volume)` | -3.37 | -3.37 | -2.66 | — | (子树本身) |
| swap | `Volume->Amt` | -1.13 | -1.13 | -0.59 | — | `cross_autocorr_s1(day_cov(Ret, Amt), 241)` |
| window | `cross_autocorr_s1@241->120` | -1.07 | -0.94 | -1.07 | — | `cross_autocorr_s1(day_cov(Ret, Volume), 120)` |
| window | `cross_autocorr_s1@241->482` | -0.86 | -0.86 | -0.66 | — | `cross_autocorr_s1(day_cov(Ret, Volume), 482)` |

### head score -1.46:`add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 15))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(sqrt(cross_quantile_q75(day_var(High), 15)))` | -2.40 | -1.49 | -2.40 | — | (子树本身) |
| sufficiency | `ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40)` | -2.34 | -2.34 | -1.54 | — | (子树本身) |
| sufficiency | `sqrt(cross_quantile_q75(day_var(High), 15))` | -2.40 | -1.49 | -2.40 | — | (子树本身) |
| sufficiency | `ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20)` | -4.99 | -3.65 | -4.99 | — | (子树本身) |
| knockout | `sigmoid(sqrt(cross_quantile_q75(day_var(High), 15)))` | -2.60 | -1.79 | -2.60 | +1.14 | `add(sqrt(cross_quantile_q75(day_var(High), 15)), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |
| knockout | `ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40)` | -1.68 | -1.68 | -1.45 | +0.23 | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 15))), ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20))` |
| knockout | `sqrt(cross_quantile_q75(day_var(High), 15))` | -2.02 | -2.02 | -1.19 | +0.56 | `add(sigmoid(cross_quantile_q75(day_var(High), 15)), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |
| knockout | `ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20)` | -2.62 | -2.62 | -1.72 | +1.16 | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 15))), ts_autocorr_s1(cross_hurst(day_durbin_watson(Ret), 5), 40))` |
| swap | `High->Low` | -1.79 | -1.79 | -0.96 | — | `add(sigmoid(sqrt(cross_quantile_q75(day_var(Low), 15))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |
| window | `cross_quantile_q75@15->7` | -1.56 | -1.56 | -0.97 | — | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 7))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |
| window | `cross_quantile_q75@15->30` | -2.10 | -2.10 | -1.30 | — | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 30))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_last(Close)` — enrichment,均值差 +0.56,p 0.097

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.26(window cross_autocorr_s1@241->482):`cross_autocorr_s1(day_cov(Ret, Volume), 482)`
