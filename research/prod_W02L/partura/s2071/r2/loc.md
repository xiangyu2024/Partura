# 定位:种子 2071,P 组,第 2 轮(只含 train / valid)

快照:prods2071M1_I0_open_search, prods2071M2_I0_open_search, prods2071Pr1a_Ea, prods2071Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.77 | -0.19 | -0.77 | -1 | 20 | prods2071M2_I0_open_search | `day_mean(pow_2(nt_cs_rank(Ret)))` |
| -0.82 | -0.61 | -0.82 | -1 | 5 | prods2071M2_I0_open_search | `day_median(pow_2(nt_cs_rank(Ret)))` |
| -1.64 | -1.62 | -1.64 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret)), 20)` |
| -1.68 | -1.68 | -1.51 | +1 | 20 | prods2071M2_I0_open_search | `pow_2(pow_2(day_q_stat_std(nt_cs_rank(High))))` |
| -1.72 | -1.71 | -1.72 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| -1.77 | -1.77 | -1.66 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 20)` |

## 共性:116 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.35 | 0.000 | 6 | -0.16 / -2.51 | `sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20))` |
| +2.35 | 0.000 | 6 | -0.16 / -2.51 | `ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)` |
| +2.25 | 0.000 | 4 | -0.21 / -2.47 | `div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))` |
| +1.93 | 0.000 | 11 | -0.65 / -2.57 | `sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open)))` |
| +1.88 | 0.000 | 8 | -0.64 / -2.52 | `div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open))` |
| +0.54 | 0.124 | 7 | -1.88 / -2.42 | `ts_rank(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| +0.49 | 0.057 | 7 | -1.93 / -2.42 | `day_corr(Ret, Amt)` |
| +0.30 | 0.206 | 71 | -2.27 / -2.58 | `sub(day_max(High), day_min(Low))` |
| +0.30 | 0.206 | 71 | -2.27 / -2.58 | `day_max(High)` |
| +0.30 | 0.206 | 71 | -2.27 / -2.58 | `day_min(Low)` |
| +0.30 | 0.199 | 68 | -2.27 / -2.56 | `div(sub(day_max(High), day_min(Low)), day_open(Open))` |
| +0.27 | 0.267 | 4 | -2.13 / -2.40 | `sub(day_close(Close), day_open(Open))` |
| +0.26 | 0.278 | 71 | -2.29 / -2.55 | `day_open(Open)` |
| +0.13 | 0.536 | 6 | -2.27 / -2.40 | `abs_(day_corr(Volume, Ret))` |
| -0.12 | 0.556 | 6 | -2.50 / -2.38 | `day_close(Close)` |
| -0.12 | 0.738 | 7 | -2.50 / -2.38 | `day_corr(Volume, Ret)` |
| -0.27 | 0.667 | 4 | -2.65 / -2.38 | `ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 5)` |
| -0.30 | 0.792 | 4 | -2.68 / -2.38 | `ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60)` |
| -0.33 | 0.645 | 4 | -2.71 / -2.38 | `day_es_ratio_lo(Amt)` |
| -0.39 | 0.792 | 4 | -2.77 / -2.38 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret)))` |

## 拆解(3 次评估)

### head score -0.77:`day_mean(pow_2(nt_cs_rank(Ret)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

### head score -0.82:`day_median(pow_2(nt_cs_rank(Ret)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

### head score -1.68:`pow_2(pow_2(day_q_stat_std(nt_cs_rank(High))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_q_stat_std(nt_cs_rank(High)))` | -1.68 | -1.68 | -1.52 | — | (子树本身) |
| sufficiency | `day_q_stat_std(nt_cs_rank(High))` | -1.68 | -1.68 | -1.52 | — | (子树本身) |
| swap | `High->Low` | -1.77 | -1.77 | -1.53 | — | `pow_2(pow_2(day_q_stat_std(nt_cs_rank(Low))))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20))` — enrichment,均值差 +2.35,p 0.000
2. `ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)` — enrichment,均值差 +2.35,p 0.000
3. `div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))` — enrichment,均值差 +2.25,p 0.000
4. `sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open)))` — enrichment,均值差 +1.93,p 0.000
5. `div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open))` — enrichment,均值差 +1.88,p 0.000
6. `day_corr(Ret, Amt)` — enrichment,均值差 +0.49,p 0.057

## 本组之前各轮的任务

- `prods2071Pr1a_Ea`:核心 `div(sub(day_max(High), day_min(Low)), day_open(Open))`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 1587, 'c05_skeleton': 780}
  - score -0.06(train +0.04 valid -0.06):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), add(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))), 20)), add(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open))), 5)`
  - score -0.06(train -0.06 valid -0.04):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)), day_open(Open)), 5)`
  - score -0.07(train -0.07 valid -0.03):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(Open)), 20)))), day_open(Open)), 20)), day_open(Open)), 5)`
  - score -0.09(train -0.09 valid -0.04):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), div(sub(day_max(High), day_min(Low)), day_open(Open))), day_open(High)), 20)), day_open(High)), 5)`
  - score -0.11(train +0.10 valid -0.11):`ts_std(div(sub(day_max(High), ts_rank(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)), day_open(Open)), 10)`
- `prods2071Pr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.42(train +0.42 valid +0.46):`cross_max(abs_(day_corr(Volume, Ret)), 241)`
  - score -1.26(train -1.26 valid -1.26):`cross_quantile_q75(cross_max(abs_(day_corr(Volume, Ret)), 15), 5)`
  - score -1.40(train -1.23 valid -1.40):`cross_quantile_q75(cross_max(abs_(day_corr(Ret, Amt)), 15), 5)`
  - score -1.40(train -0.87 valid -1.40):`cross_quantile_q75(cs_last_high40(day_corr(Vwap, Vwap), day_es_ratio_lo(Amt)), 5)`
  - score -1.45(train -1.10 valid -1.45):`cross_max(abs_(cs_bucket_demean(day_std(Volume), LimitWidth)), 15)`

## 比原 head 好的拆解变体(R 候选)

(没有)
