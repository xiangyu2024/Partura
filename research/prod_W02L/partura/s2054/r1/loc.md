# 定位:种子 2054,P 组,第 1 轮(只含 train / valid)

快照:prods2054M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.37 | -0.37 | -0.37 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 5)))` |
| -0.41 | -0.38 | -0.41 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 5)))` |
| -0.45 | -0.26 | -0.45 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))` |

## 共性:9 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(12 次评估)

### head score -0.37:`day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Close->Vwap` | -0.70 | -0.18 | -0.70 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Vwap), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Vwap)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Vwap)), 15), 5)))` |
| swap | `Vwap->Close` | -0.38 | -0.38 | -0.36 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Close), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 5)))` |
| window | `nt_ts_regalpha@5->2` | -0.36 | -0.19 | -0.36 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 2)))` |
| window | `nt_ts_regalpha@5->10` | -0.50 | -0.50 | -0.36 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 10)))` |

### head score -0.41:`day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Close->Vwap` | -0.80 | -0.29 | -0.80 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Vwap), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Vwap)), 15), 5)))` |
| swap | `Vwap->Close` | -0.39 | -0.39 | -0.29 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Close), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 5)))` |
| window | `nt_ts_regalpha@5->2` | -0.46 | +0.04 | -0.46 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 2)))` |
| window | `nt_ts_regalpha@5->10` | -0.49 | -0.49 | -0.35 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 10)))` |

### head score -0.45:`day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `High->Low` | -0.32 | -0.25 | -0.32 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Low), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))` |
| swap | `Vwap->Close` | -0.37 | -0.32 | -0.37 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Close), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))` |
| window | `nt_ts_regalpha@3->2` | -0.42 | -0.08 | -0.42 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 2)))` |
| window | `nt_ts_regalpha@3->6` | -0.48 | -0.48 | -0.41 | — | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 6)))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(swap High->Low):`day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Low), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))`
