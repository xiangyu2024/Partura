# 定位:种子 2058,P 组,第 1 轮(只含 train / valid)

快照:prods2058M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.12 | -1.12 | -1.11 | -1 | 5 | prods2058M1_I0_open_search | `day_std(pow_2(Volume))` |
| -2.58 | -2.41 | -2.58 | -1 | 5 | prods2058M1_I0_open_search | `cross_mean(day_std(pow_2(Ret)), 3)` |
| -2.61 | -2.42 | -2.61 | -1 | 5 | prods2058M1_I0_open_search | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)` |

## 共性:7 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(13 次评估)

### head score -1.12:`day_std(pow_2(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.66 | -3.22 | -3.66 | — | `day_std(pow_2(Amt))` |

### head score -2.58:`cross_mean(day_std(pow_2(Ret)), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(pow_2(Ret))` | -2.87 | -2.78 | -2.87 | — | (子树本身) |
| window | `cross_mean@3->2` | -2.94 | -2.59 | -2.94 | — | `cross_mean(day_std(pow_2(Ret)), 2)` |
| window | `cross_mean@3->6` | -2.27 | -1.90 | -2.27 | — | `cross_mean(day_std(pow_2(Ret)), 6)` |

### head score -2.61:`cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(neg(neg(sigmoid(day_std(pow_2(Ret))))))` | — | — | — | — | 门槛废品 |
| sufficiency | `neg(neg(sigmoid(day_std(pow_2(Ret)))))` | — | — | — | — | 门槛废品 |
| sufficiency | `neg(sigmoid(day_std(pow_2(Ret))))` | — | — | — | — | 门槛废品 |
| sufficiency | `sigmoid(day_std(pow_2(Ret)))` | — | — | — | — | 门槛废品 |
| knockout | `sqrt(neg(neg(sigmoid(day_std(pow_2(Ret))))))` | — | — | — | — | `cross_mean(neg(neg(sigmoid(day_std(pow_2(Ret))))), 3)` |
| knockout | `neg(neg(sigmoid(day_std(pow_2(Ret)))))` | — | — | — | — | `cross_mean(sqrt(neg(sigmoid(day_std(pow_2(Ret))))), 3)` |
| knockout | `sigmoid(day_std(pow_2(Ret)))` | -2.62 | -2.49 | -2.62 | +0.01 | `cross_mean(sqrt(neg(neg(day_std(pow_2(Ret))))), 3)` |
| window | `cross_mean@3->2` | — | — | — | — | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 2)` |
| window | `cross_mean@3->6` | — | — | — | — | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 6)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.30(window cross_mean@3->6):`cross_mean(day_std(pow_2(Ret)), 6)`
