# 定位:种子 2062,P 组,第 1 轮(只含 train / valid)

快照:prods2062M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.74 | -1.35 | -1.74 | -1 | 20 | prods2062M1_I0_open_search | `ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)` |
| -3.86 | -2.54 | -3.86 | -1 | 20 | prods2062M1_I0_open_search | `ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)` |
| -4.22 | -4.22 | -2.85 | -1 | 20 | prods2062M1_I0_open_search | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0), True)` |

## 共性:8 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(12 次评估)

### head score -1.74:`ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06))))` | — | — | — | — | 门槛废品 |
| window | `ts_mean@20->10` | -1.98 | -1.88 | -1.98 | — | `ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 10)` |
| window | `ts_mean@20->40` | -2.33 | -1.92 | -2.33 | — | `ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 40)` |

### head score -3.86:`ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06))))` | — | — | — | — | 门槛废品 |
| window | `ts_mean@20->10` | -3.88 | -3.08 | -3.88 | — | `ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 10)` |
| window | `ts_mean@20->40` | -3.00 | -2.70 | -3.00 | — | `ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 40)` |

### head score -4.22:`rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0), True)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False)` | -4.93 | -4.93 | -4.03 | — | (子树本身) |
| knockout | `create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0)` | -4.22 | -4.22 | -2.96 | -0.00 | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), True)` |
| swap | `Volume->Amt` | -4.22 | -4.22 | -3.03 | — | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Amt, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Amt, 10, False), 0), True)` |
| window | `in_regres@20->10` | -4.28 | -4.28 | -3.02 | — | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 10), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0), True)` |
| window | `in_regres@20->40` | -4.22 | -4.22 | -2.95 | — | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 40), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), create_valid_mask(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), Volume, 10, False), 0), True)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.86(window ts_mean@20->40):`ts_mean(day_skew(div(in_regres(Ret, in_mean_full(Ret), 20), add(in_stddev_full(in_regres(Ret, in_mean_full(Ret), 20)), create_like(in_regres(Ret, in_mean_full(Ret), 20), 1e-06)))), 40)`
