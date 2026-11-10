# 定位:种子 2042,P 组,第 1 轮(只含 train / valid)

快照:prods2042M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.12 | -1.09 | -1.12 | +1 | 0 | prods2042M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)` |
| -1.63 | -1.63 | -0.71 | -1 | 0 | prods2042M1_I0_open_search | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 241))` |
| -1.63 | -1.49 | -1.63 | +1 | 5 | prods2042M1_I0_open_search | `ts_std(day_kurt(Low), 50)` |

## 共性:55 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.75 | 0.031 | 12 | -2.97 / -3.72 | `day_kurt(Low)` |
| +0.46 | 0.232 | 7 | -3.16 / -3.62 | `day_kurt(Vwap)` |
| +0.39 | 0.274 | 4 | -3.20 / -3.59 | `day_kurt(High)` |
| -0.17 | 0.774 | 8 | -3.70 / -3.54 | `day_kurt(Volume)` |
| -0.30 | 0.810 | 6 | -3.82 / -3.53 | `day_kurt(Ret)` |
| -1.47 | 0.657 | 4 | -4.92 / -3.45 | `day_kurt(Amt)` |

## 拆解(26 次评估)

### head score -1.12:`ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20))` | -1.11 | -1.11 | -0.62 | — | (子树本身) |
| sufficiency | `log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20)))` | -1.66 | -1.66 | -1.21 | — | (子树本身) |
| sufficiency | `add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))` | -1.66 | -1.66 | -1.20 | — | (子树本身) |
| sufficiency | `mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20))` | -2.09 | -2.09 | -1.37 | — | (子树本身) |
| knockout | `mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20))` | -2.07 | -2.07 | -1.59 | +0.95 | `ts_mean(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), 50)` |
| knockout | `log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20)))` | -0.93 | -0.73 | -0.93 | -0.19 | `ts_mean(mul(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20)), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)` |
| knockout | `add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))` | -1.92 | -1.92 | -1.37 | +0.80 | `ts_mean(mul(log(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)` |
| knockout | `mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20))` | -1.60 | -1.60 | -1.26 | +0.48 | `ts_mean(mul(log(add(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 50)` |
| swap | `Volume->Amt` | -1.20 | -1.20 | -1.11 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Amt), ts_hurst(div(day_kurt(Amt), ts_hurst(div(day_kurt(Amt), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Amt), day_max(Low)), 20)), ts_hurst(div(day_kurt(Amt), ts_hurst(div(day_kurt(Amt), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Amt), day_max(Low)), 20)), 50)` |
| swap | `Low->High` | -1.14 | -1.14 | -1.14 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(High)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(High)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(High)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(High)), 20)), 50)` |
| window | `ts_mean@50->25` | -0.57 | -0.45 | -0.57 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 25)` |
| window | `ts_mean@50->100` | -1.49 | -1.49 | -1.04 | — | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), ts_hurst(div(day_kurt(Volume), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 20))), ts_hurst(div(day_kurt(Volume), day_max(Low)), 20)), 100)` |

### head score -1.63:`neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 241)` | -1.63 | -1.63 | -0.67 | — | (子树本身) |
| sufficiency | `ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | -1.84 | -1.38 | -1.84 | — | (子树本身) |
| sufficiency | `ts_std(day_kurt(Low), 50)` | -1.65 | -1.49 | -1.65 | — | (子树本身) |
| sufficiency | `day_kurt(Low)` | -4.53 | -3.85 | -4.53 | — | (子树本身) |
| knockout | `cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 241)` | -1.84 | -1.38 | -1.84 | +0.21 | `neg(ts_decay_linear(ts_std(day_kurt(Low), 50), 10))` |
| knockout | `ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | -1.51 | -1.51 | -0.66 | -0.12 | `neg(cross_sum(ts_std(day_kurt(Low), 50), 241))` |
| knockout | `ts_std(day_kurt(Low), 50)` | -1.95 | -1.95 | -1.12 | +0.32 | `neg(cross_sum(ts_decay_linear(day_kurt(Low), 10), 241))` |
| swap | `Low->High` | -1.61 | -1.61 | -0.65 | — | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(High), 50), 10), 241))` |
| window | `cross_sum@241->120` | -1.60 | -1.60 | -0.93 | — | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 120))` |
| window | `cross_sum@241->482` | -1.68 | -1.68 | -0.83 | — | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10), 482))` |

### head score -1.63:`ts_std(day_kurt(Low), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(Low)` | -4.53 | -3.85 | -4.53 | — | (子树本身) |
| swap | `Low->High` | -2.13 | -1.23 | -2.13 | — | `ts_std(day_kurt(High), 50)` |
| window | `ts_std@50->25` | -1.84 | -1.51 | -1.84 | — | `ts_std(day_kurt(Low), 25)` |
| window | `ts_std@50->100` | -1.27 | -1.10 | -1.27 | — | `ts_std(day_kurt(Low), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_kurt(Low)` — enrichment,均值差 +0.75,p 0.031

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.36(window ts_std@50->100):`ts_std(day_kurt(Low), 100)`
- 增益 +0.12(knockout ts_decay_linear(ts_std(day_kurt(Low), 50), 10)):`neg(cross_sum(ts_std(day_kurt(Low), 50), 241))`
