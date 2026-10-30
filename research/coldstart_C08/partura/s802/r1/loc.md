# 定位:种子 802,P 组,第 1 轮(只含 train / valid)

快照:c07s802M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.69 | +0.69 | +0.98 | -1 | 20 | c07s802M1_I0_open_search | `day_mean(in_delta(Volume, 30))` |

## 共性:98 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.59 | 0.003 | 4 | +0.57 / -1.02 | `day_mean(in_delta(Volume, 5))` |
| +1.58 | 0.008 | 4 | +0.56 / -1.02 | `day_mean(neg(neg(in_delta(Volume, 5))))` |
| +1.25 | 0.003 | 16 | +0.09 / -1.16 | `day_mean(neg(in_delta(Volume, 60)))` |
| +1.07 | 0.001 | 22 | -0.13 / -1.20 | `day_last(Amt)` |
| +1.07 | 0.014 | 8 | +0.02 / -1.05 | `cs_median(cs_robust_z(day_last(Amt)))` |
| +0.90 | 0.009 | 19 | -0.23 / -1.13 | `cs_robust_z(day_last(Amt))` |
| +0.88 | 0.355 | 6 | -0.14 / -1.01 | `day_flat_run_max(Vwap)` |
| +0.88 | 0.355 | 6 | -0.14 / -1.01 | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` |
| +0.84 | 0.401 | 4 | -0.15 / -0.99 | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` |
| +0.72 | 0.456 | 7 | -0.29 / -1.01 | `sqrt(sigmoid(LimitWidth))` |
| +0.72 | 0.456 | 7 | -0.29 / -1.01 | `sigmoid(LimitWidth)` |
| +0.69 | 0.470 | 7 | -0.32 / -1.01 | `day_durbin_watson(Volume)` |
| +0.56 | 0.166 | 10 | -0.45 / -1.02 | `cs_stddev_full(cs_robust_z(day_last(Amt)))` |

## 拆解(3 次评估)

### head score +0.69:`day_mean(in_delta(Volume, 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -0.81 | +0.11 | -0.81 | — | `day_mean(in_delta(Amt, 30))` |
| window | `in_delta@30->15` | +0.51 | +0.51 | +1.34 | — | `day_mean(in_delta(Volume, 15))` |
| window | `in_delta@30->60` | +0.52 | +0.59 | +0.52 | — | `day_mean(in_delta(Volume, 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_mean(in_delta(Volume, 5))` — enrichment,均值差 +1.59,p 0.003
2. `day_mean(neg(neg(in_delta(Volume, 5))))` — enrichment,均值差 +1.58,p 0.008
3. `day_mean(neg(in_delta(Volume, 60)))` — enrichment,均值差 +1.25,p 0.003
4. `day_last(Amt)` — enrichment,均值差 +1.07,p 0.001
5. `cs_median(cs_robust_z(day_last(Amt)))` — enrichment,均值差 +1.07,p 0.014
6. `cs_robust_z(day_last(Amt))` — enrichment,均值差 +0.90,p 0.009

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
