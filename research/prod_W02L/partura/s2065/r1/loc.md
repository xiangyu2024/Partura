# 定位:种子 2065,P 组,第 1 轮(只含 train / valid)

快照:prods2065M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.52 | -1.52 | -1.13 | +1 | 20 | prods2065M1_I0_open_search | `day_q_stat_std(in_max_rolling(Amt, 60))` |
| -1.54 | -1.54 | -1.15 | +1 | 20 | prods2065M1_I0_open_search | `day_q_stat_std(in_max_rolling(Volume, 60))` |
| -2.35 | -1.64 | -2.35 | -1 | 20 | prods2065M1_I0_open_search | `day_var(in_max_rolling(Vwap, 60))` |

## 共性:14 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(9 次评估)

### head score -1.52:`day_q_stat_std(in_max_rolling(Amt, 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -1.54 | -1.54 | -1.15 | — | `day_q_stat_std(in_max_rolling(Volume, 60))` |
| window | `in_max_rolling@60->30` | -2.05 | -2.05 | -1.69 | — | `day_q_stat_std(in_max_rolling(Amt, 30))` |
| window | `in_max_rolling@60->120` | -1.64 | -1.64 | -1.27 | — | `day_q_stat_std(in_max_rolling(Amt, 120))` |

### head score -1.54:`day_q_stat_std(in_max_rolling(Volume, 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -1.52 | -1.52 | -1.13 | — | `day_q_stat_std(in_max_rolling(Amt, 60))` |
| window | `in_max_rolling@60->30` | -2.08 | -2.08 | -1.69 | — | `day_q_stat_std(in_max_rolling(Volume, 30))` |
| window | `in_max_rolling@60->120` | -1.64 | -1.64 | -1.24 | — | `day_q_stat_std(in_max_rolling(Volume, 120))` |

### head score -2.35:`day_var(in_max_rolling(Vwap, 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -2.29 | -1.59 | -2.29 | — | `day_var(in_max_rolling(Close, 60))` |
| window | `in_max_rolling@60->30` | -2.30 | -1.64 | -2.30 | — | `day_var(in_max_rolling(Vwap, 30))` |
| window | `in_max_rolling@60->120` | -2.32 | -1.70 | -2.32 | — | `day_var(in_max_rolling(Vwap, 120))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
