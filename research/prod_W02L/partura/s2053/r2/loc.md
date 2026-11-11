# 定位:种子 2053,P 组,第 2 轮(只含 train / valid)

快照:prods2053M1_I0_open_search, prods2053M2_I0_open_search, prods2053Pr1a_Na;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.52 | -0.52 | +0.96 | +1 | 0 | prods2053M2_I0_open_search | `day_first(cross_sum(Amt, 241))` |
| -0.98 | -0.98 | -0.64 | +1 | 5 | prods2053M2_I0_open_search | `day_first(cross_sum(Amt, 30))` |
| -1.33 | -1.19 | -1.33 | -1 | 5 | prods2053M2_I0_open_search | `day_sum(cross_sum(Volume, 3))` |

## 共性:63 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.81 | 0.011 | 17 | -1.82 / -2.63 | `cross_semistd_neg(day_topw_mean(Ret, Close), 3)` |
| +0.80 | 0.009 | 20 | -1.86 / -2.66 | `day_topw_mean(Ret, Close)` |
| +0.78 | 0.035 | 8 | -1.73 / -2.51 | `ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)` |
| +0.63 | 0.097 | 6 | -1.83 / -2.47 | `cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30))` |

## 拆解(9 次评估)

### head score -0.52:`day_first(cross_sum(Amt, 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -1.66 | -1.40 | -1.66 | — | `day_first(cross_sum(Volume, 241))` |
| window | `cross_sum@241->120` | -0.26 | -0.26 | +0.30 | — | `day_first(cross_sum(Amt, 120))` |
| window | `cross_sum@241->482` | -0.55 | -0.55 | +0.78 | — | `day_first(cross_sum(Amt, 482))` |

### head score -0.98:`day_first(cross_sum(Amt, 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -1.20 | -1.20 | -1.19 | — | `day_first(cross_sum(Volume, 30))` |
| window | `cross_sum@30->15` | -1.61 | -1.61 | -0.34 | — | `day_first(cross_sum(Amt, 15))` |
| window | `cross_sum@30->60` | -0.14 | -0.02 | -0.14 | — | `day_first(cross_sum(Amt, 60))` |

### head score -1.33:`day_sum(cross_sum(Volume, 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.55 | -2.70 | -3.55 | — | `day_sum(cross_sum(Amt, 3))` |
| window | `cross_sum@3->2` | -1.37 | -1.16 | -1.37 | — | `day_sum(cross_sum(Volume, 2))` |
| window | `cross_sum@3->6` | -1.44 | -1.23 | -1.44 | — | `day_sum(cross_sum(Volume, 6))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_semistd_neg(day_topw_mean(Ret, Close), 3)` — enrichment,均值差 +0.81,p 0.011
2. `day_topw_mean(Ret, Close)` — enrichment,均值差 +0.80,p 0.009
3. `ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)` — enrichment,均值差 +0.78,p 0.035
4. `cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30))` — enrichment,均值差 +0.63,p 0.097

## 本组之前各轮的任务

- `prods2053Pr1a_Na`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.74(train -0.74 valid -0.55):`cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30))`
  - score -0.74(train -0.74 valid -0.55):`cs_demean(cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)))`
  - score -0.74(train -0.74 valid -0.55):`ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)`
  - score -0.76(train -0.76 valid -0.62):`cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 40))`
  - score -0.87(train -0.87 valid -0.86):`cs_demean(ts_stddev(ts_quantile_q50(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 5), 40))`

## 比原 head 好的拆解变体(R 候选)

(没有)
