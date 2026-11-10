# 定位:种子 2005,P 组,第 1 轮(只含 train / valid)

快照:prods2005M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.83 | -1.83 | -1.59 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` |
| -1.84 | -1.84 | -1.68 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(day_cov(Ret, Close), 60)` |
| -1.85 | -1.85 | -0.75 | +1 | 5 | prods2005M1_I0_open_search | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5)` |

## 共性:22 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.21 | 0.566 | 14 | -2.40 / -2.61 | `cross_max(day_cov(Amt, Low), 5)` |
| -0.06 | 0.571 | 6 | -2.51 / -2.46 | `cross_max(cross_max(day_cov(Amt, Low), 5), 5)` |

## 拆解(24 次评估)

### head score -1.83:`cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(cross_max(day_cov(Amt, Low), 5), 5)` | -2.24 | -2.24 | -2.14 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(Amt, Low), 5)` | -2.14 | -2.12 | -2.14 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Low)` | -4.50 | -4.50 | -3.34 | — | (子树本身) |
| knockout | `cross_max(cross_max(day_cov(Amt, Low), 5), 5)` | -2.16 | -2.16 | -1.62 | +0.33 | `cross_max(cross_max(day_cov(Amt, Low), 5), 30)` |
| swap | `Amt->Volume` | -0.83 | -0.60 | -0.83 | — | `cross_max(cross_max(cross_max(day_cov(Volume, Low), 5), 5), 30)` |
| swap | `Low->High` | -1.65 | -1.65 | -1.46 | — | `cross_max(cross_max(cross_max(day_cov(Amt, High), 5), 5), 30)` |
| window | `cross_max@30->15` | -2.37 | -2.37 | -2.15 | — | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 15)` |
| window | `cross_max@30->60` | -1.26 | -1.26 | -0.58 | — | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 60)` |

### head score -1.84:`cross_max(day_cov(Ret, Close), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Ret, Close)` | -1.25 | -1.14 | -1.25 | — | (子树本身) |
| swap | `Close->Vwap` | -2.08 | -2.08 | -1.12 | — | `cross_max(day_cov(Ret, Vwap), 60)` |
| window | `cross_max@60->30` | -1.96 | -1.80 | -1.96 | — | `cross_max(day_cov(Ret, Close), 30)` |
| window | `cross_max@60->120` | -1.70 | -1.35 | -1.70 | — | `cross_max(day_cov(Ret, Close), 120)` |

### head score -1.85:`cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1))` | -1.92 | -1.92 | -0.84 | — | (子树本身) |
| sufficiency | `ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | -2.29 | -2.26 | -2.29 | — | (子树本身) |
| sufficiency | `pow_3(ts_std(day_close(Amt), 50))` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| knockout | `mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1))` | -2.37 | -2.37 | -2.14 | +0.52 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 15), 5)` |
| knockout | `ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)` | -1.85 | -1.85 | -0.72 | -0.00 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), pow_3(ts_std(day_close(Amt), 50))), 5)` |
| knockout | `cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | -2.28 | -2.28 | -1.26 | +0.43 | `cross_max(mul(cross_max(day_cov(Amt, Low), 5), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5)` |
| knockout | `pow_3(ts_std(day_close(Amt), 50))` | -2.77 | -2.77 | -1.62 | +0.92 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(ts_std(day_close(Amt), 50), 1)), 5)` |
| swap | `Amt->Volume` | -1.28 | -1.28 | -1.24 | — | `cross_max(mul(cross_max(cross_max(day_cov(Volume, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Volume), 50)), 1)), 5)` |
| swap | `Low->High` | -1.74 | -1.74 | -0.63 | — | `cross_max(mul(cross_max(cross_max(day_cov(Amt, High), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5)` |
| window | `cross_max@5->2` | -1.89 | -1.89 | -0.80 | — | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 2)` |
| window | `cross_max@5->10` | -1.62 | -1.62 | -0.63 | — | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.14(window cross_max@60->120):`cross_max(day_cov(Ret, Close), 120)`
