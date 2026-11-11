# 定位:种子 2063,P 组,第 1 轮(只含 train / valid)

快照:prods2063M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.18 | -1.18 | -1.00 | -1 | 5 | prods2063M1_I0_open_search | `pow_05(day_var(nt_ts_min(Volume, 30)))` |
| -1.33 | -1.33 | -1.26 | +1 | 20 | prods2063M1_I0_open_search | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, Low))` |
| -2.02 | -2.02 | -1.53 | -1 | 20 | prods2063M1_I0_open_search | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))` |

## 共性:18 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(20 次评估)

### head score -1.18:`pow_05(day_var(nt_ts_min(Volume, 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_var(nt_ts_min(Volume, 30))` | -1.18 | -1.18 | -1.06 | — | (子树本身) |
| swap | `Volume->Amt` | -2.16 | -2.16 | -0.84 | — | `pow_05(day_var(nt_ts_min(Amt, 30)))` |
| window | `nt_ts_min@30->15` | -1.12 | -1.12 | -1.00 | — | `pow_05(day_var(nt_ts_min(Volume, 15)))` |
| window | `nt_ts_min@30->60` | -1.23 | -1.23 | -1.06 | — | `pow_05(day_var(nt_ts_min(Volume, 60)))` |

### head score -1.33:`add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, Low))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_min(nt_ts_med(nt_ts_min(Amt, 3), 5))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_cov(Ret, Low)` | -4.22 | -4.22 | -3.43 | — | (子树本身) |
| swap | `Amt->Volume` | -1.67 | -1.30 | -1.67 | — | `add(day_min(nt_ts_med(nt_ts_min(Volume, 3), 5)), day_cov(Ret, Low))` |
| swap | `Low->High` | -0.88 | -0.88 | -0.63 | — | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, High))` |
| window | `nt_ts_med@5->2` | -3.77 | -3.77 | -3.43 | — | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 2)), day_cov(Ret, Low))` |
| window | `nt_ts_med@5->10` | -2.14 | -2.14 | -1.65 | — | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 10)), day_cov(Ret, Low))` |

### head score -2.02:`add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30)` | -2.89 | -2.72 | -2.89 | — | (子树本身) |
| sufficiency | `cs_normalize(day_autocorr_n1(Low))` | -2.98 | -2.98 | -2.32 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Low)` | -2.98 | -2.98 | -2.32 | — | (子树本身) |
| knockout | `ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30)` | -2.24 | -2.24 | -1.63 | +0.23 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), cs_normalize(day_autocorr_n1(Low)))` |
| knockout | `cs_normalize(day_autocorr_n1(Low))` | -2.07 | -2.07 | -1.55 | +0.06 | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), ts_hurst(day_autocorr_n1(Low), 30))` |
| swap | `Volume->Amt` | -2.85 | -2.85 | -2.71 | — | `add(day_quantile(in_min_rolling(nt_ts_min(Amt, 10), 15)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))` |
| swap | `Low->High` | -2.05 | -2.05 | -1.55 | — | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), ts_hurst(cs_normalize(day_autocorr_n1(High)), 30))` |
| window | `in_min_rolling@15->7` | -1.98 | -1.98 | -1.63 | — | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 7)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))` |
| window | `in_min_rolling@15->30` | -2.84 | -2.09 | -2.84 | — | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 30)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.45(swap Low->High):`add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, High))`
