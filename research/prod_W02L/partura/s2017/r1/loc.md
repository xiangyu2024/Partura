# 定位:种子 2017,P 组,第 1 轮(只含 train / valid)

快照:prods2017M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.59 | -0.59 | +0.12 | +1 | 5 | prods2017M1_I0_open_search | `signedpower(cs_mask_top_replace_mean_neg(day_quantile(Vwap)))` |
| -1.19 | -1.02 | -1.19 | -1 | 20 | prods2017M1_I0_open_search | `cs_rank(day_quantile(Ret))` |
| -1.31 | -1.13 | -1.31 | -1 | 20 | prods2017M1_I0_open_search | `pow_2(cs_rank(cs_normalize(day_quantile(Ret))))` |

## 共性:30 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.21 | 0.258 | 6 | -2.45 / -2.66 | `day_quantile(Close)` |
| -0.18 | 0.631 | 5 | -2.77 / -2.59 | `day_quantile(Vwap)` |

## 拆解(10 次评估)

### head score -0.59:`signedpower(cs_mask_top_replace_mean_neg(day_quantile(Vwap)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean_neg(day_quantile(Vwap))` | -0.59 | -0.59 | +0.13 | — | (子树本身) |
| sufficiency | `day_quantile(Vwap)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `cs_mask_top_replace_mean_neg(day_quantile(Vwap))` | -2.38 | -1.61 | -2.38 | +1.79 | `signedpower(day_quantile(Vwap))` |
| swap | `Vwap->Close` | -0.56 | -0.56 | +0.16 | — | `signedpower(cs_mask_top_replace_mean_neg(day_quantile(Close)))` |

### head score -1.19:`cs_rank(day_quantile(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile(Ret)` | — | — | — | — | 门槛废品 |

### head score -1.31:`pow_2(cs_rank(cs_normalize(day_quantile(Ret))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cs_normalize(day_quantile(Ret)))` | -1.25 | -1.13 | -1.25 | — | (子树本身) |
| sufficiency | `cs_normalize(day_quantile(Ret))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `cs_rank(cs_normalize(day_quantile(Ret)))` | — | — | — | — | `pow_2(cs_normalize(day_quantile(Ret)))` |
| knockout | `cs_normalize(day_quantile(Ret))` | -1.14 | -1.02 | -1.14 | -0.16 | `pow_2(cs_rank(day_quantile(Ret)))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.16(knockout cs_normalize(day_quantile(Ret))):`pow_2(cs_rank(day_quantile(Ret)))`
