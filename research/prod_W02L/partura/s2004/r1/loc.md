# 定位:种子 2004,P 组,第 1 轮(只含 train / valid)

快照:prods2004M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.64 | -0.64 | -0.08 | +1 | 5 | prods2004M1_I0_open_search | `ts_skew(day_cov(Ret, Volume), 40)` |
| -0.73 | -0.73 | -0.30 | +1 | 5 | prods2004M1_I0_open_search | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume, Amt), 15), 241)` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2004M1_I0_open_search | `day_cov(Volume, Volume)` |

## 共性:55 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.16 | 0.002 | 7 | -1.61 / -2.77 | `day_cov(Ret, Volume)` |

## 拆解(13 次评估)

### head score -0.64:`ts_skew(day_cov(Ret, Volume), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Ret, Volume)` | -3.37 | -3.37 | -2.66 | — | (子树本身) |
| swap | `Volume->Amt` | -0.82 | -0.82 | -0.09 | — | `ts_skew(day_cov(Ret, Amt), 40)` |
| window | `ts_skew@40->20` | -1.67 | -1.67 | -0.47 | — | `ts_skew(day_cov(Ret, Volume), 20)` |
| window | `ts_skew@40->80` | -0.63 | -0.63 | +0.05 | — | `ts_skew(day_cov(Ret, Volume), 80)` |

### head score -0.73:`cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume, Amt), 15), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(day_sum(High), day_cov(Volume, Amt), 15)` | -1.59 | -1.26 | -1.59 | — | (子树本身) |
| sufficiency | `day_sum(High)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| sufficiency | `day_cov(Volume, Amt)` | -1.27 | -1.27 | -1.07 | — | (子树本身) |
| knockout | `cross_corr(day_sum(High), day_cov(Volume, Amt), 15)` | -2.39 | -1.60 | -2.39 | +1.66 | `cross_quantile_q50(day_sum(High), 241)` |
| swap | `High->Low` | -0.73 | -0.73 | -0.34 | — | `cross_quantile_q50(cross_corr(day_sum(Low), day_cov(Volume, Amt), 15), 241)` |
| swap | `Volume->Amt` | -0.67 | -0.67 | -0.18 | — | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Amt, Amt), 15), 241)` |
| window | `cross_quantile_q50@241->120` | -1.87 | -0.60 | -1.87 | — | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume, Amt), 15), 120)` |
| window | `cross_quantile_q50@241->482` | -1.07 | -1.07 | -0.05 | — | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume, Amt), 15), 482)` |

### head score -1.16:`day_cov(Volume, Volume)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.75 | -2.98 | -3.75 | — | `day_cov(Amt, Amt)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_cov(Ret, Volume)` — enrichment,均值差 +1.16,p 0.002

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
