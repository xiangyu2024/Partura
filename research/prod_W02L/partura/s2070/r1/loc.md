# 定位:种子 2070,P 组,第 1 轮(只含 train / valid)

快照:prods2070M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.01 | -2.01 | -1.77 | +1 | 20 | prods2070M1_I0_open_search | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 5)` |
| -2.76 | -1.73 | -2.76 | -1 | 20 | prods2070M1_I0_open_search | `day_quantile_q75(mul(High, Ret))` |
| -2.80 | -2.21 | -2.80 | +1 | 5 | prods2070M1_I0_open_search | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` |

## 共性:9 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(17 次评估)

### head score -2.01:`ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5)` | -2.44 | -2.44 | -2.32 | — | (子树本身) |
| sufficiency | `sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))))` | -2.74 | -2.40 | -2.74 | — | (子树本身) |
| sufficiency | `pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))` | -2.73 | -2.40 | -2.73 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))` | -2.73 | -2.40 | -2.73 | — | (子树本身) |
| knockout | `ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5)` | -1.73 | -1.73 | -1.35 | -0.28 | `ts_min(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5)` |
| knockout | `sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))))` | -2.01 | -2.01 | -1.77 | -0.00 | `ts_min(ts_decay_linear(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))), 5), 5)` |
| knockout | `pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))` | -2.01 | -2.01 | -1.77 | -0.00 | `ts_min(ts_decay_linear(sigmoid(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))), 5), 5)` |
| knockout | `pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))` | -2.00 | -2.00 | -1.78 | -0.01 | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30))))))), 5), 5)` |
| swap | `Volume->Amt` | -2.01 | -2.01 | -1.75 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Amt, mul(Amt, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 5)` |
| swap | `High->Low` | -2.01 | -2.01 | -1.75 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, Low))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 5)` |
| window | `ts_min@5->2` | -2.17 | -2.17 | -2.05 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 2)` |
| window | `ts_min@5->10` | -1.92 | -1.92 | -1.46 | — | `ts_min(ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5), 10)` |

### head score -2.76:`day_quantile_q75(mul(High, Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `High->Low` | -2.73 | -1.73 | -2.73 | — | `day_quantile_q75(mul(Low, Ret))` |

### head score -2.80:`ts_mean(day_q_stat_std(mul(Close, Close)), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(mul(Close, Close))` | -3.21 | -3.21 | -2.61 | — | (子树本身) |
| swap | `Close->Vwap` | -3.18 | -2.52 | -3.18 | — | `ts_mean(day_q_stat_std(mul(Vwap, Vwap)), 40)` |
| window | `ts_mean@40->20` | -2.54 | -2.33 | -2.54 | — | `ts_mean(day_q_stat_std(mul(Close, Close)), 20)` |
| window | `ts_mean@40->80` | -2.35 | -2.35 | -2.22 | — | `ts_mean(day_q_stat_std(mul(Close, Close)), 80)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.45(window ts_mean@40->80):`ts_mean(day_q_stat_std(mul(Close, Close)), 80)`
- 增益 +0.28(knockout ts_decay_linear(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5)):`ts_min(sigmoid(pow_05(pow_2(pow_05(sigmoid(sigmoid(day_last(nt_ts_corr(sigmoid(mul(Volume, mul(Volume, High))), cross_cov(sqrt(Low), pow_05(Close), 15), 30)))))))), 5)`
- 增益 +0.26(window ts_mean@40->20):`ts_mean(day_q_stat_std(mul(Close, Close)), 20)`
