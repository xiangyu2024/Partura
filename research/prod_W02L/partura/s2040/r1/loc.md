# 定位:种子 2040,P 组,第 1 轮(只含 train / valid)

快照:prods2040M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.47 | -1.47 | -0.90 | +1 | 20 | prods2040M1_I0_open_search | `day_first(log(Amt))` |
| -1.49 | -1.43 | -1.49 | -1 | 20 | prods2040M1_I0_open_search | `day_mean(log(Volume))` |
| -1.59 | -1.59 | -1.41 | +1 | 20 | prods2040M1_I0_open_search | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` |

## 共性:24 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(5 次评估)

### head score -1.47:`day_first(log(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | — | — | — | — | `day_first(log(Volume))` |

### head score -1.49:`day_mean(log(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -2.82 | -2.76 | -2.82 | — | `day_mean(log(Amt))` |

### head score -1.59:`add(day_min(log(Amt)), day_cov(Ret, log(Amt)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_min(log(Amt))` | -1.59 | -1.59 | -1.45 | — | (子树本身) |
| sufficiency | `day_cov(Ret, log(Amt))` | -3.10 | -3.10 | -1.84 | — | (子树本身) |
| swap | `Amt->Volume` | -2.45 | -2.20 | -2.45 | — | `add(day_min(log(Volume)), day_cov(Ret, log(Volume)))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
