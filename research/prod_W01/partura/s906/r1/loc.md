# 定位:种子 906,P 组,第 1 轮(只含 train / valid)

快照:prods906M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.72 | +0.72 | +3.15 | -1 | 5 | prods906M1_I0_open_search | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))))` |

## 共性:102 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.27 | 0.000 | 47 | +0.13 / -1.13 | `day_last(Vwap)` |
| +1.14 | 0.000 | 22 | +0.34 / -0.79 | `cs_first_low20(day_last(Vwap), day_quantile(High))` |
| +1.12 | 0.000 | 8 | +0.49 / -0.64 | `cs_first_low20(day_last(Vwap), day_last(Vwap))` |
| +1.10 | 0.004 | 6 | +0.49 / -0.61 | `day_last(High)` |
| +1.09 | 0.000 | 44 | +0.07 / -1.02 | `day_quantile(High)` |
| +1.00 | 0.030 | 6 | +0.40 / -0.61 | `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` |
| +0.98 | 0.119 | 5 | +0.39 / -0.60 | `day_quantile(Vwap)` |
| +0.94 | 0.227 | 4 | +0.35 / -0.59 | `cs_first_low20(day_last(Vwap), day_quantile(Vwap))` |
| +0.93 | 0.092 | 6 | +0.33 / -0.60 | `cs_first_low20(day_quantile(High), day_quantile(High))` |
| +0.81 | 0.036 | 8 | +0.20 / -0.61 | `pow_2(cs_first_low20(day_last(Vwap), day_quantile(High)))` |

## 拆解(9 次评估)

### head score +0.72:`pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))))` | +0.72 | +0.72 | +3.15 | — | (子树本身) |
| sufficiency | `cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))` | +0.39 | +0.39 | +1.68 | — | (子树本身) |
| sufficiency | `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` | +0.32 | +0.32 | +2.25 | — | (子树本身) |
| knockout | `cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))))` | +0.32 | +0.32 | +2.25 | +0.40 | `pow_2(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))` |
| knockout | `cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))` | +0.39 | +0.39 | +1.68 | +0.32 | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))))` |
| knockout | `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` | +0.72 | +0.72 | +3.15 | +0.00 | `pow_2(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))))` |
| knockout | `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` | +0.72 | +0.72 | +3.15 | +0.00 | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))))` |
| swap | `Vwap->Close` | +0.72 | +0.72 | +3.15 | — | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Close), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Close), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Close), day_quantile(High)), day_quantile(High)))))` |
| swap | `High->Low` | +0.73 | +0.73 | +3.17 | — | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(Low)), day_quantile(Low)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(Low)), day_quantile(Low)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(Low)), day_quantile(Low)))))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))))` — ablation,自身 score +0.72(所在 head +0.72)
2. `day_last(Vwap)` — enrichment,均值差 +1.27,p 0.000
3. `cs_first_low20(day_last(Vwap), day_quantile(High))` — enrichment,均值差 +1.14,p 0.000
4. `cs_first_low20(day_last(Vwap), day_last(Vwap))` — enrichment,均值差 +1.12,p 0.000
5. `day_last(High)` — enrichment,均值差 +1.10,p 0.004
6. `day_quantile(High)` — enrichment,均值差 +1.09,p 0.000
7. `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` — enrichment,均值差 +1.00,p 0.030
8. `cs_first_low20(day_quantile(High), day_quantile(High))` — enrichment,均值差 +0.93,p 0.092
9. `pow_2(cs_first_low20(day_last(Vwap), day_quantile(High)))` — enrichment,均值差 +0.81,p 0.036

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
