# 定位:种子 2061,P 组,第 1 轮(只含 train / valid)

快照:prods2061M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.73 | -0.73 | +0.04 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 20)` |
| -0.83 | -0.83 | +0.15 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), 20)` |
| -0.85 | -0.85 | -0.75 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), 20)` |

## 共性:30 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(12 次评估)

### head score -0.73:`cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_quantile_single(Ret, Volume, 0.95, True)` | -2.94 | -2.94 | -2.29 | — | (子树本身) |
| swap | `Volume->Amt` | -0.84 | -0.84 | -0.45 | — | `cross_mean(day_pdf_quantile_single(Ret, Amt, 0.95, True), 20)` |
| window | `cross_mean@20->10` | -1.01 | -1.01 | -0.27 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 10)` |
| window | `cross_mean@20->40` | -0.55 | -0.55 | +0.00 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 40)` |

### head score -0.83:`cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_quantile_single(Ret, Volume, 0.8, True)` | -3.64 | -3.64 | -2.78 | — | (子树本身) |
| swap | `Volume->Amt` | -1.13 | -1.13 | +0.03 | — | `cross_mean(day_pdf_quantile_single(Ret, Amt, 0.8, True), 20)` |
| window | `cross_mean@20->10` | -1.36 | -1.36 | -0.76 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), 10)` |
| window | `cross_mean@20->40` | -0.87 | -0.87 | -0.22 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), 40)` |

### head score -0.85:`cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_quantile_single(Ret, Volume, 0.6, True)` | -3.49 | -3.49 | -2.73 | — | (子树本身) |
| swap | `Volume->Amt` | -0.82 | -0.82 | -0.78 | — | `cross_mean(day_pdf_quantile_single(Ret, Amt, 0.6, True), 20)` |
| window | `cross_mean@20->10` | -1.18 | -1.18 | -0.14 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), 10)` |
| window | `cross_mean@20->40` | -0.78 | -0.78 | -0.59 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.19(window cross_mean@20->40):`cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 40)`
