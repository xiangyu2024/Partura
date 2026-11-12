# 定位:种子 2077,P 组,第 1 轮(只含 train / valid)

快照:prods2077M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.02 | -0.22 | -1.02 | -1 | 5 | prods2077M1_I0_open_search | `day_median(div(abs_(Ret), Amt))` |
| -1.12 | -0.87 | -1.12 | -1 | 20 | prods2077M1_I0_open_search | `day_open(in_delta(Volume, 60))` |
| -1.63 | -1.39 | -1.63 | -1 | 20 | prods2077M1_I0_open_search | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))` |

## 共性:51 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.63 | 0.964 | 13 | -3.99 / -3.37 | `in_slice(Close, 1, 1)` |
| -0.63 | 0.964 | 13 | -3.99 / -3.37 | `create_like(in_slice(Close, 1, 1), 0)` |
| -0.71 | 0.914 | 4 | -4.18 / -3.47 | `create_like(in_slice(Close, 1, 1), 1)` |

## 拆解(8 次评估)

### head score -1.02:`day_median(div(abs_(Ret), Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -2.19 | -0.73 | -2.19 | — | `day_median(div(abs_(Ret), Volume))` |

### head score -1.12:`day_open(in_delta(Volume, 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -1.33 | -1.33 | -0.91 | — | `day_open(in_delta(Amt, 60))` |
| window | `in_delta@60->30` | — | — | — | — | `day_open(in_delta(Volume, 30))` |
| window | `in_delta@60->120` | — | — | — | — | `day_open(in_delta(Volume, 120))` |

### head score -1.63:`day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `High->Low` | -1.56 | -1.42 | -1.56 | — | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, Low, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))` |
| swap | `Vwap->Close` | -1.37 | -1.37 | -1.25 | — | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Close))))` |
| window | `nt_ts_delay@10->5` | -1.72 | -1.37 | -1.72 | — | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 5), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))` |
| window | `nt_ts_delay@10->20` | -1.57 | -1.38 | -1.57 | — | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 20), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Vwap))))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(swap Vwap->Close):`day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), nt_cs_mask_top_replace_mean(nt_cs_mask_top_replace_mean_neg(Close))))`
