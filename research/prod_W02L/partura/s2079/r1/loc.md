# 定位:种子 2079,P 组,第 1 轮(只含 train / valid)

快照:prods2079M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.78 | -0.78 | -0.60 | +1 | 20 | prods2079M1_I0_open_search | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| -1.52 | -1.52 | -1.06 | +1 | 5 | prods2079M1_I0_open_search | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 241), 20)` |
| -1.54 | -1.54 | -1.22 | +1 | 5 | prods2079M1_I0_open_search | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |

## 共性:40 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.42 | 0.869 | 4 | -3.21 / -2.79 | `day_ar1_coefficient(Volume)` |

## 拆解(31 次评估)

### head score -0.78:`sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5)` | -0.79 | -0.79 | -0.53 | — | (子树本身) |
| sufficiency | `ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40)` | -2.25 | -2.25 | -2.08 | — | (子树本身) |
| sufficiency | `signedpower(day_ar1_coefficient(in_shift(Low, 15)))` | -4.38 | -4.38 | -3.60 | — | (子树本身) |
| sufficiency | `cross_cov(day_close(Amt), day_hurst(Open), 30)` | -2.56 | -2.56 | -2.16 | — | (子树本身) |
| knockout | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5)` | -2.33 | -2.33 | -2.08 | +1.54 | `sub(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| knockout | `ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40)` | -1.10 | -1.10 | -0.81 | +0.32 | `sub(ts_var(cross_cov(day_close(Amt), day_hurst(Open), 30), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| knockout | `signedpower(day_ar1_coefficient(in_shift(Low, 15)))` | -0.78 | -0.78 | -0.58 | +0.00 | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5), day_ar1_coefficient(in_shift(Low, 15)))` |
| knockout | `cross_cov(day_close(Amt), day_hurst(Open), 30)` | -0.66 | -0.66 | -0.23 | -0.13 | `sub(ts_var(ts_mean(day_close(Amt), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| swap | `Amt->Volume` | -3.13 | -1.41 | -3.13 | — | `sub(ts_var(ts_mean(cross_cov(day_close(Volume), day_hurst(Open), 30), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| swap | `Open->Close` | -0.77 | -0.77 | -0.45 | — | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Close), 30), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| window | `ts_var@5->2` | -0.52 | -0.52 | -0.45 | — | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 2), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| window | `ts_var@5->10` | -0.71 | -0.63 | -0.71 | — | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 10), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |

### head score -1.52:`ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 241), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_regbeta(day_quantile_q25(Low), day_var(Low), 241)` | -1.45 | -1.45 | -1.16 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Low)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_var(Low)` | -2.27 | -1.53 | -2.27 | — | (子树本身) |
| knockout | `cross_regbeta(day_quantile_q25(Low), day_var(Low), 241)` | -2.39 | -1.63 | -2.39 | +0.87 | `ts_max(day_quantile_q25(Low), 20)` |
| swap | `Low->High` | -1.52 | -1.52 | -1.25 | — | `ts_max(cross_regbeta(day_quantile_q25(High), day_var(High), 241), 20)` |
| window | `ts_max@20->10` | -1.57 | -1.57 | -1.20 | — | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 241), 10)` |
| window | `ts_max@20->40` | -1.49 | -1.49 | -1.49 | — | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 241), 40)` |

### head score -1.54:`sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100)` | -1.35 | -1.35 | -1.29 | — | (子树本身) |
| sufficiency | `ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100)` | -1.84 | -1.84 | -1.79 | — | (子树本身) |
| sufficiency | `div(day_max(High), ts_delay(day_last(Close), 1))` | -2.74 | -2.74 | -2.70 | — | (子树本身) |
| sufficiency | `div(day_min(Low), ts_delay(day_last(Close), 1))` | -2.69 | -2.55 | -2.69 | — | (子树本身) |
| knockout | `sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1)` | -1.54 | -1.54 | -1.28 | +0.00 | `sub(ts_stddev(div(day_max(High), ts_delay(day_last(Close), 1)), 100), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |
| knockout | `sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1)` | -1.54 | -1.54 | -1.28 | +0.00 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100), ts_stddev(div(day_min(Low), ts_delay(day_last(Close), 1)), 100))` |
| knockout | `div(day_max(High), ts_delay(day_last(Close), 1))` | -2.17 | -1.72 | -2.17 | +0.63 | `sub(ts_stddev(sub(day_max(High), 1), 100), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |
| knockout | `div(day_min(Low), ts_delay(day_last(Close), 1))` | -2.06 | -1.69 | -2.06 | +0.52 | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100), ts_stddev(sub(day_min(Low), 1), 100))` |
| swap | `High->Low` | -1.49 | -1.42 | -1.49 | — | `sub(ts_stddev(sub(div(day_max(Low), ts_delay(day_last(Close), 1)), 1), 100), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |
| swap | `Close->Vwap` | -1.62 | -1.62 | -1.32 | — | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Vwap), 1)), 1), 100), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Vwap), 1)), 1), 100))` |
| window | `ts_stddev@100->50` | -1.40 | -1.40 | -1.04 | — | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 50), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |
| window | `ts_stddev@100->200` | -1.50 | -1.50 | -1.35 | — | `sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 200), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.14(window ts_stddev@100->50):`sub(ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 50), ts_stddev(sub(div(day_min(Low), ts_delay(day_last(Close), 1)), 1), 100))`
