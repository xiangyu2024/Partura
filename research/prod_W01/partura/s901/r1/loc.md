# 定位:种子 901,P 组,第 1 轮(只含 train / valid)

快照:prods901M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:94 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.86 | 0.000 | 22 | -0.85 / -1.71 | `day_last(Close)` |
| +0.83 | 0.001 | 21 | -0.86 / -1.69 | `cs_demean(day_last(Close))` |
| +0.62 | 0.003 | 46 | -1.19 / -1.81 | `day_var(Low)` |
| +0.54 | 0.024 | 22 | -1.09 / -1.63 | `cs_flip_by_state(day_var(Low), day_quantile(Ret))` |
| +0.50 | 0.135 | 8 | -1.05 / -1.55 | `cs_flip_by_state(day_var(Low), day_var(Low))` |
| +0.28 | 0.115 | 31 | -1.32 / -1.60 | `day_quantile(Ret)` |
| +0.10 | 0.563 | 4 | -1.40 / -1.51 | `cross_tail_mean_q75(day_flat_run_max(Open), 241)` |
| -0.36 | 0.800 | 5 | -1.85 / -1.49 | `day_flat_run_max(Open)` |
| -0.40 | 0.832 | 5 | -1.89 / -1.48 | `day_es_ratio_hi(Ret)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `day_last(Close)` — enrichment,均值差 +0.86,p 0.000
2. `cs_demean(day_last(Close))` — enrichment,均值差 +0.83,p 0.001
3. `day_var(Low)` — enrichment,均值差 +0.62,p 0.003
4. `cs_flip_by_state(day_var(Low), day_quantile(Ret))` — enrichment,均值差 +0.54,p 0.024

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
