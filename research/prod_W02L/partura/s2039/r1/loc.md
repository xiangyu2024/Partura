# 定位:种子 2039,P 组,第 1 轮(只含 train / valid)

快照:prods2039M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.26 | -2.26 | -2.17 | +1 | 20 | prods2039M1_I0_open_search | `pow_05(day_autocorr_n1(Close))` |
| -2.77 | -1.94 | -2.77 | +1 | 5 | prods2039M1_I0_open_search | `ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 10)` |
| -2.93 | -1.97 | -2.93 | -1 | 5 | prods2039M1_I0_open_search | `ts_min(ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10), 10)` |

## 共性:7 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.35 | 0.886 | 4 | -3.24 / -2.89 | `ts_std(pow_05(day_autocorr_n1(Ret)), 10)` |
| -0.35 | 0.886 | 4 | -3.24 / -2.89 | `inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10))` |
| -0.35 | 0.886 | 4 | -3.24 / -2.89 | `pow_05(day_autocorr_n1(Ret))` |

## 拆解(21 次评估)

### head score -2.26:`pow_05(day_autocorr_n1(Close))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr_n1(Close)` | -2.26 | -2.26 | -2.21 | — | (子树本身) |
| swap | `Close->Vwap` | -2.51 | -2.51 | -2.37 | — | `pow_05(day_autocorr_n1(Vwap))` |

### head score -2.77:`ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `inv(ts_std(pow_05(day_autocorr_n1(Open)), 10))` | -2.38 | -1.89 | -2.38 | — | (子树本身) |
| sufficiency | `ts_std(pow_05(day_autocorr_n1(Open)), 10)` | -2.40 | -1.73 | -2.40 | — | (子树本身) |
| sufficiency | `pow_05(day_autocorr_n1(Open))` | -2.43 | -2.43 | -1.91 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Open)` | -2.43 | -2.43 | -1.91 | — | (子树本身) |
| knockout | `inv(ts_std(pow_05(day_autocorr_n1(Open)), 10))` | -2.49 | -1.76 | -2.49 | -0.28 | `ts_min(ts_std(pow_05(day_autocorr_n1(Open)), 10), 10)` |
| knockout | `ts_std(pow_05(day_autocorr_n1(Open)), 10)` | -2.42 | -2.39 | -2.42 | -0.35 | `ts_min(inv(pow_05(day_autocorr_n1(Open))), 10)` |
| knockout | `pow_05(day_autocorr_n1(Open))` | -2.80 | -2.04 | -2.80 | +0.02 | `ts_min(inv(ts_std(day_autocorr_n1(Open), 10)), 10)` |
| swap | `Open->Close` | -2.80 | -1.82 | -2.80 | — | `ts_min(inv(ts_std(pow_05(day_autocorr_n1(Close)), 10)), 10)` |
| window | `ts_min@10->5` | -2.59 | -2.00 | -2.59 | — | `ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 5)` |
| window | `ts_min@10->20` | -2.62 | -2.26 | -2.62 | — | `ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 20)` |

### head score -2.93:`ts_min(ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10)` | -3.82 | -2.63 | -3.82 | — | (子树本身) |
| sufficiency | `inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10))` | -3.94 | -2.87 | -3.94 | — | (子树本身) |
| sufficiency | `ts_std(pow_05(day_autocorr_n1(Ret)), 10)` | -4.04 | -2.83 | -4.04 | — | (子树本身) |
| sufficiency | `pow_05(day_autocorr_n1(Ret))` | -3.69 | -3.50 | -3.69 | — | (子树本身) |
| knockout | `inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10))` | -3.66 | -3.08 | -3.66 | +0.72 | `ts_min(ts_min(ts_std(pow_05(day_autocorr_n1(Ret)), 10), 10), 10)` |
| knockout | `ts_std(pow_05(day_autocorr_n1(Ret)), 10)` | -2.94 | -2.66 | -2.94 | +0.00 | `ts_min(ts_min(inv(pow_05(day_autocorr_n1(Ret))), 10), 10)` |
| knockout | `pow_05(day_autocorr_n1(Ret))` | -1.99 | -1.94 | -1.99 | -0.94 | `ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 10)` |
| window | `ts_min@10->5` | -3.90 | -2.58 | -3.90 | — | `ts_min(ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10), 5)` |
| window | `ts_min@10->20` | -2.49 | -1.67 | -2.49 | — | `ts_min(ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10), 20)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.94(knockout pow_05(day_autocorr_n1(Ret))):`ts_min(ts_min(inv(ts_std(day_autocorr_n1(Ret), 10)), 10), 10)`
- 增益 +0.44(window ts_min@10->20):`ts_min(ts_min(inv(ts_std(pow_05(day_autocorr_n1(Ret)), 10)), 10), 20)`
- 增益 +0.28(knockout inv(ts_std(pow_05(day_autocorr_n1(Open)), 10))):`ts_min(ts_std(pow_05(day_autocorr_n1(Open)), 10), 10)`
- 增益 +0.18(window ts_min@10->5):`ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 5)`
- 增益 +0.16(window ts_min@10->20):`ts_min(inv(ts_std(pow_05(day_autocorr_n1(Open)), 10)), 20)`
