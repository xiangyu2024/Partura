# 定位:种子 902,P 组,第 2 轮(只含 train / valid)

快照:prods902M1_I0_open_search, prods902M2_I0_open_search, prods902Pr1a_Na, prods902Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:325 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.14 | 0.013 | 4 | +0.11 / -1.03 | `cs_last_low40(add(LogFloatShares, 0.5), sub(day_sum(Vwap), 0.5))` |
| +1.08 | 0.007 | 6 | +0.04 / -1.04 | `cs_last_low40(add(LogFloatShares, -5), sub(day_sum(Vwap), 0.5))` |
| +1.05 | 0.001 | 10 | -0.00 / -1.05 | `cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5))` |
| +1.03 | 0.009 | 8 | -0.01 / -1.04 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 15)` |
| +1.02 | 0.001 | 13 | -0.04 / -1.06 | `div(day_first(Amt), day_sum(Amt))` |
| +1.00 | 0.012 | 6 | -0.03 / -1.03 | `cross_min(cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5)), 5)` |
| +0.97 | 0.030 | 5 | -0.06 / -1.03 | `cs_last_low40(add(LogFloatShares, add(LogFloatShares, -5)), sub(day_sum(Vwap), 0.5))` |
| +0.93 | 0.001 | 15 | -0.13 / -1.06 | `day_sum(Amt)` |
| +0.90 | 0.000 | 55 | -0.27 / -1.17 | `day_sum(Vwap)` |
| +0.80 | 0.006 | 15 | -0.25 / -1.05 | `day_first(Amt)` |
| +0.72 | 0.041 | 8 | -0.32 / -1.03 | `cs_bucket_rank(day_max(High), day_quantile_q25(Open))` |
| +0.50 | 0.034 | 22 | -0.55 / -1.05 | `day_max(High)` |
| +0.45 | 0.144 | 8 | -0.58 / -1.03 | `day_first(High)` |
| +0.42 | 0.219 | 6 | -0.60 / -1.02 | `sub(day_topw_mean(Ret, Ret), day_last(Ret))` |
| +0.37 | 0.062 | 21 | -0.67 / -1.04 | `day_quantile_q25(Open)` |
| +0.31 | 0.437 | 4 | -0.71 / -1.02 | `day_std(High)` |
| +0.29 | 0.365 | 4 | -0.73 / -1.02 | `day_gini(Close)` |
| +0.29 | 0.365 | 4 | -0.73 / -1.02 | `cs_demean(day_gini(Close))` |
| +0.29 | 0.371 | 14 | -0.74 / -1.03 | `day_sum(Low)` |
| +0.25 | 0.339 | 5 | -0.77 / -1.02 | `day_topw_mean(Ret, Volume)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low40(add(LogFloatShares, 0.5), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +1.14,p 0.013
2. `cs_last_low40(add(LogFloatShares, -5), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +1.08,p 0.007
3. `cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +1.05,p 0.001
4. `cross_mean(div(day_first(Amt), day_sum(Amt)), 15)` — enrichment,均值差 +1.03,p 0.009
5. `div(day_first(Amt), day_sum(Amt))` — enrichment,均值差 +1.02,p 0.001
6. `cross_min(cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5)), 5)` — enrichment,均值差 +1.00,p 0.012
7. `cs_last_low40(add(LogFloatShares, add(LogFloatShares, -5)), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +0.97,p 0.030
8. `day_sum(Amt)` — enrichment,均值差 +0.93,p 0.001
9. `day_sum(Vwap)` — enrichment,均值差 +0.90,p 0.000
10. `day_first(Amt)` — enrichment,均值差 +0.80,p 0.006
11. `cs_bucket_rank(day_max(High), day_quantile_q25(Open))` — enrichment,均值差 +0.72,p 0.041
12. `day_max(High)` — enrichment,均值差 +0.50,p 0.034
13. `day_quantile_q25(Open)` — enrichment,均值差 +0.37,p 0.062

## 本组之前各轮的任务

- `prods902Pr1a_Na`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {}
  - score +0.21(train +0.21 valid +1.21):`cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 30)`
  - score +0.15(train +0.15 valid +1.26):`cross_mean(div(day_first(Amt), day_sum(Amt)), 30)`
  - score +0.14(train +0.14 valid +1.45):`cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 20)`
  - score +0.11(train +0.11 valid +1.43):`cross_mean(cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 30), 30)`
  - score +0.11(train +0.11 valid +1.19):`cross_mean(cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 15), 20)`
- `prods902Pr1b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {}
  - score +0.47(train +0.47 valid +0.77):`cs_last_high05(cs_bucket_rank(day_max(High), day_max(High)), div(day_first(High), -5))`
  - score +0.47(train +0.47 valid +0.77):`cs_last_high05(cs_bucket_rank(day_max(High), day_max(High)), div(day_first(High), -2))`
  - score +0.43(train +0.43 valid +0.77):`cs_last_high05(cs_bucket_rank(day_max(High), day_max(High)), div(day_quantile_q25(Open), -5))`
  - score +0.42(train +0.42 valid +0.75):`cs_bucket_rank(day_max(High), day_max(High))`
  - score +0.41(train +0.41 valid +0.92):`cs_last_high05(cs_bucket_rank(day_max(High), day_quantile_q25(Open)), div(day_first(Close), -2))`

## 比原 head 好的拆解变体(R 候选)

(没有)
