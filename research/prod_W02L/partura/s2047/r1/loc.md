# 定位:种子 2047,P 组,第 1 轮(只含 train / valid)

快照:prods2047M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.34 | -1.34 | -1.19 | +1 | 20 | prods2047M1_I0_open_search | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` |
| -1.60 | -1.47 | -1.60 | +1 | 20 | prods2047M1_I0_open_search | `cross_cov(day_min(High), day_mean(Amt), 30)` |
| -2.35 | -1.56 | -2.35 | -1 | 20 | prods2047M1_I0_open_search | `add(day_min(Ret), day_var(Open))` |

## 共性:21 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.01 | 0.795 | 12 | -2.62 / -2.61 | `day_min(Ret)` |
| -0.23 | 0.957 | 4 | -2.81 / -2.57 | `pow_2(day_min(Ret))` |

## 拆解(16 次评估)

### head score -1.34:`pow_3(cross_hurst(neg(day_min(Ret)), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_hurst(neg(day_min(Ret)), 15)` | -1.34 | -1.34 | -1.17 | — | (子树本身) |
| sufficiency | `neg(day_min(Ret))` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `cross_hurst(neg(day_min(Ret)), 15)` | -2.77 | -2.19 | -2.77 | +1.43 | `pow_3(neg(day_min(Ret)))` |
| knockout | `neg(day_min(Ret))` | -1.34 | -1.34 | -1.17 | +0.00 | `pow_3(cross_hurst(day_min(Ret), 15))` |
| window | `cross_hurst@15->7` | -2.87 | -2.87 | -2.79 | — | `pow_3(cross_hurst(neg(day_min(Ret)), 7))` |
| window | `cross_hurst@15->30` | -1.75 | -0.92 | -1.75 | — | `pow_3(cross_hurst(neg(day_min(Ret)), 30))` |

### head score -1.60:`cross_cov(day_min(High), day_mean(Amt), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_min(High)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| sufficiency | `day_mean(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| swap | `High->Low` | -1.50 | -1.50 | -1.43 | — | `cross_cov(day_min(Low), day_mean(Amt), 30)` |
| swap | `Amt->Volume` | -1.60 | -0.88 | -1.60 | — | `cross_cov(day_min(High), day_mean(Volume), 30)` |
| window | `cross_cov@30->15` | -1.71 | -1.71 | -1.67 | — | `cross_cov(day_min(High), day_mean(Amt), 15)` |
| window | `cross_cov@30->60` | -1.19 | -1.19 | -1.11 | — | `cross_cov(day_min(High), day_mean(Amt), 60)` |

### head score -2.35:`add(day_min(Ret), day_var(Open))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `day_var(Open)` | -2.22 | -1.50 | -2.22 | — | (子树本身) |
| swap | `Open->Close` | -2.32 | -1.57 | -2.32 | — | `add(day_min(Ret), day_var(Close))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
