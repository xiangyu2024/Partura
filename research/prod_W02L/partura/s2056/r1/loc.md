# 定位:种子 2056,P 组,第 1 轮(只含 train / valid)

快照:prods2056M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.65 | -0.05 | -0.65 | +1 | 5 | prods2056M1_I0_open_search | `day_max(cross_corr(Amt, Ret, 60))` |
| -0.88 | -0.44 | -0.88 | +1 | 5 | prods2056M1_I0_open_search | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)` |
| -1.66 | -1.43 | -1.66 | -1 | 5 | prods2056M1_I0_open_search | `day_max(cross_corr(Ret, Ret, 15))` |

## 共性:11 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(9 次评估)

### head score -0.65:`day_max(cross_corr(Amt, Ret, 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -0.65 | -0.06 | -0.65 | — | `day_max(cross_corr(Volume, Ret, 60))` |
| window | `cross_corr@60->30` | -1.16 | -1.16 | -1.11 | — | `day_max(cross_corr(Amt, Ret, 30))` |
| window | `cross_corr@60->120` | -0.42 | -0.03 | -0.42 | — | `day_max(cross_corr(Amt, Ret, 120))` |

### head score -0.88:`cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(cross_corr(Amt, Ret, 60))` | -0.60 | -0.05 | -0.60 | — | (子树本身) |
| swap | `Amt->Volume` | -0.94 | -0.42 | -0.94 | — | `cross_min(day_max(cross_corr(Volume, Ret, 60)), 15)` |
| window | `cross_min@15->7` | -0.81 | -0.26 | -0.81 | — | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 7)` |
| window | `cross_min@15->30` | -0.85 | -0.65 | -0.85 | — | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 30)` |

### head score -1.66:`day_max(cross_corr(Ret, Ret, 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| window | `cross_corr@15->7` | — | — | — | — | `day_max(cross_corr(Ret, Ret, 7))` |
| window | `cross_corr@15->30` | — | — | — | — | `day_max(cross_corr(Ret, Ret, 30))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.23(window cross_corr@60->120):`day_max(cross_corr(Amt, Ret, 120))`
