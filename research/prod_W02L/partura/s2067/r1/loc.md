# 定位:种子 2067,P 组,第 1 轮(只含 train / valid)

快照:prods2067M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.66 | -2.34 | -2.66 | +1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 5)), Volume)` |
| -2.70 | -2.34 | -2.70 | +1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| -2.89 | -2.63 | -2.89 | -1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` |

## 共性:24 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(8 次评估)

### head score -2.66:`day_corr(abs_(in_delay(Ret, 5)), Volume)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -2.77 | -2.34 | -2.77 | — | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| window | `in_delay@5->2` | -3.07 | -2.85 | -3.07 | — | `day_corr(abs_(in_delay(Ret, 2)), Volume)` |
| window | `in_delay@5->10` | -2.53 | -2.23 | -2.53 | — | `day_corr(abs_(in_delay(Ret, 10)), Volume)` |

### head score -2.70:`day_corr(abs_(in_delay(Ret, 5)), Amt)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -2.73 | -2.34 | -2.73 | — | `day_corr(abs_(in_delay(Ret, 5)), Volume)` |
| window | `in_delay@5->2` | -3.07 | -2.86 | -3.07 | — | `day_corr(abs_(in_delay(Ret, 2)), Amt)` |
| window | `in_delay@5->10` | -2.47 | -2.22 | -2.47 | — | `day_corr(abs_(in_delay(Ret, 10)), Amt)` |

### head score -2.89:`day_corr(abs_(in_delay(Ret, 1)), log(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -2.85 | -2.65 | -2.85 | — | `day_corr(abs_(in_delay(Ret, 1)), log(Volume))` |
| window | `in_delay@1->2` | -3.48 | -2.71 | -3.48 | — | `day_corr(abs_(in_delay(Ret, 2)), log(Amt))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.22(window in_delay@5->10):`day_corr(abs_(in_delay(Ret, 10)), Amt)`
- 增益 +0.13(window in_delay@5->10):`day_corr(abs_(in_delay(Ret, 10)), Volume)`
