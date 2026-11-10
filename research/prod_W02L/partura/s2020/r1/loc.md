# 定位:种子 2020,P 组,第 1 轮(只含 train / valid)

快照:prods2020M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `abs_(day_skew(Open))` |
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `pow_2(abs_(day_skew(Open)))` |
| -3.12 | -3.08 | -3.12 | +1 | 20 | prods2020M1_I0_open_search | `abs_(pow_2(abs_(day_skew(Open))))` |

## 共性:10 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(12 次评估)

### head score -3.12:`abs_(day_skew(Open))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| swap | `Open->Close` | -3.25 | -2.87 | -3.25 | — | `abs_(day_skew(Close))` |

### head score -3.12:`pow_2(abs_(day_skew(Open)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(day_skew(Open))` | -3.08 | -3.08 | -3.08 | — | (子树本身) |
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| knockout | `abs_(day_skew(Open))` | -3.08 | -3.08 | -3.08 | -0.04 | `pow_2(day_skew(Open))` |
| swap | `Open->Close` | -3.25 | -2.87 | -3.25 | — | `pow_2(abs_(day_skew(Close)))` |

### head score -3.12:`abs_(pow_2(abs_(day_skew(Open))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(abs_(day_skew(Open)))` | -3.08 | -3.08 | -3.08 | — | (子树本身) |
| sufficiency | `abs_(day_skew(Open))` | -3.08 | -3.08 | -3.08 | — | (子树本身) |
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| knockout | `pow_2(abs_(day_skew(Open)))` | -3.08 | -3.08 | -3.08 | -0.04 | `abs_(abs_(day_skew(Open)))` |
| knockout | `abs_(day_skew(Open))` | -3.08 | -3.08 | -3.08 | -0.04 | `abs_(pow_2(day_skew(Open)))` |
| swap | `Open->Close` | -3.25 | -2.87 | -3.25 | — | `abs_(pow_2(abs_(day_skew(Close))))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
