# 定位:种子 2016,P 组,第 1 轮(只含 train / valid)

快照:prods2016M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.30 | -1.27 | -1.30 | +1 | 20 | prods2016M1_I0_open_search | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 30)` |
| -2.35 | -1.59 | -2.35 | +1 | 20 | prods2016M1_I0_open_search | `sub(day_kurt(Ret), day_quantile_q25(Open))` |
| -2.42 | -1.61 | -2.42 | -1 | 5 | prods2016M1_I0_open_search | `abs_(day_quantile_q25(Open))` |

## 共性:8 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(11 次评估)

### head score -1.30:`cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(Open)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_kurt(Volume)` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| swap | `Open->Close` | -1.26 | -1.26 | -1.16 | — | `cross_reg_tvalue(day_quantile_q25(Close), day_kurt(Volume), 30)` |
| swap | `Volume->Amt` | -1.22 | -1.16 | -1.22 | — | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Amt), 30)` |
| window | `cross_reg_tvalue@30->15` | -1.44 | -1.44 | -1.33 | — | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 15)` |
| window | `cross_reg_tvalue@30->60` | -1.51 | -1.07 | -1.51 | — | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 60)` |

### head score -2.35:`sub(day_kurt(Ret), day_quantile_q25(Open))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(Ret)` | -3.81 | -2.76 | -3.81 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Open)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| swap | `Open->Close` | -2.31 | -1.59 | -2.31 | — | `sub(day_kurt(Ret), day_quantile_q25(Close))` |

### head score -2.42:`abs_(day_quantile_q25(Open))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(Open)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| swap | `Open->Close` | -2.38 | -1.61 | -2.38 | — | `abs_(day_quantile_q25(Close))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
