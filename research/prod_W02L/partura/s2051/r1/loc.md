# 定位:种子 2051,P 组,第 1 轮(只含 train / valid)

快照:prods2051M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.58 | -0.58 | -0.53 | +1 | 20 | prods2051M1_I0_open_search | `day_skew(nt_ts_kurt(Low, 10))` |
| -1.87 | -1.86 | -1.87 | +1 | 20 | prods2051M1_I0_open_search | `day_max(nt_ts_kurt(Vwap, 10))` |
| -2.95 | -2.95 | -1.89 | -1 | 20 | prods2051M1_I0_open_search | `day_max(nt_ts_kurt(Vwap, 30))` |

## 共性:18 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.60 | 0.046 | 5 | -2.95 / -3.56 | `day_max(nt_ts_kurt(Vwap, 30))` |

## 拆解(9 次评估)

### head score -0.58:`day_skew(nt_ts_kurt(Low, 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Low->High` | -0.51 | -0.51 | -0.43 | — | `day_skew(nt_ts_kurt(High, 10))` |
| window | `nt_ts_kurt@10->5` | -1.59 | -1.58 | -1.59 | — | `day_skew(nt_ts_kurt(Low, 5))` |
| window | `nt_ts_kurt@10->20` | -1.61 | -1.38 | -1.61 | — | `day_skew(nt_ts_kurt(Low, 20))` |

### head score -1.87:`day_max(nt_ts_kurt(Vwap, 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -0.50 | -0.18 | -0.50 | — | `day_max(nt_ts_kurt(Close, 10))` |
| window | `nt_ts_kurt@10->5` | -1.29 | -1.12 | -1.29 | — | `day_max(nt_ts_kurt(Vwap, 5))` |
| window | `nt_ts_kurt@10->20` | -2.33 | -2.33 | -1.81 | — | `day_max(nt_ts_kurt(Vwap, 20))` |

### head score -2.95:`day_max(nt_ts_kurt(Vwap, 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -4.22 | -2.93 | -4.22 | — | `day_max(nt_ts_kurt(Close, 30))` |
| window | `nt_ts_kurt@30->15` | -2.85 | -2.07 | -2.85 | — | `day_max(nt_ts_kurt(Vwap, 15))` |
| window | `nt_ts_kurt@30->60` | -4.23 | -4.23 | -2.42 | — | `day_max(nt_ts_kurt(Vwap, 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_max(nt_ts_kurt(Vwap, 30))` — enrichment,均值差 +0.60,p 0.046

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.58(window nt_ts_kurt@10->5):`day_max(nt_ts_kurt(Vwap, 5))`
