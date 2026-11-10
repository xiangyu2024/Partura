# 定位:种子 2018,P 组,第 1 轮(只含 train / valid)

快照:prods2018M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.18 | -1.59 | -2.18 | +1 | 20 | prods2018M1_I0_open_search | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` |

## 共性:1 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(6 次评估)

### head score -2.18:`ts_std(cross_argmax(day_quantile(Open), 60), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_argmax(day_quantile(Open), 60)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile(Open)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `cross_argmax(day_quantile(Open), 60)` | -2.19 | -1.64 | -2.19 | +0.01 | `ts_std(day_quantile(Open), 50)` |
| swap | `Open->Close` | -2.10 | -1.56 | -2.10 | — | `ts_std(cross_argmax(day_quantile(Close), 60), 50)` |
| window | `ts_std@50->25` | -1.59 | -1.59 | -1.30 | — | `ts_std(cross_argmax(day_quantile(Open), 60), 25)` |
| window | `ts_std@50->100` | -2.19 | -1.59 | -2.19 | — | `ts_std(cross_argmax(day_quantile(Open), 60), 100)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.59(window ts_std@50->25):`ts_std(cross_argmax(day_quantile(Open), 60), 25)`
