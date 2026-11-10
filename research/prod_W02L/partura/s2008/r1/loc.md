# 定位:种子 2008,P 组,第 1 轮(只含 train / valid)

快照:prods2008M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.35 | -1.35 | -1.19 | +1 | 0 | prods2008M1_I0_open_search | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10), 241)` |
| -2.50 | -1.07 | -2.50 | +1 | 20 | prods2008M1_I0_open_search | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| -2.59 | -0.68 | -2.59 | +1 | 5 | prods2008M1_I0_open_search | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40)` |

## 共性:18 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.41 | 0.439 | 4 | -3.02 / -3.43 | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10)` |
| +0.33 | 0.362 | 7 | -3.14 / -3.46 | `ts_sum(log(day_durbin_watson(Vwap)), 10)` |
| -0.53 | 0.921 | 4 | -3.75 / -3.22 | `day_durbin_watson(Volume)` |
| -0.53 | 0.921 | 4 | -3.75 / -3.22 | `log(day_durbin_watson(Volume))` |

## 拆解(30 次评估)

### head score -1.35:`cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10)` | -3.78 | -3.78 | -2.58 | — | (子树本身) |
| sufficiency | `ts_sum(log(day_durbin_watson(Vwap)), 10)` | -3.56 | -3.56 | -2.11 | — | (子树本身) |
| sufficiency | `log(day_durbin_watson(Vwap))` | -3.14 | -3.14 | -2.83 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10)` | -1.40 | -1.40 | -1.22 | +0.06 | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 241)` |
| knockout | `ts_sum(log(day_durbin_watson(Vwap)), 10)` | -1.76 | -1.76 | -0.75 | +0.41 | `cross_fangzheng(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 241)` |
| knockout | `log(day_durbin_watson(Vwap))` | -1.44 | -1.44 | -0.73 | +0.09 | `cross_fangzheng(cross_fangzheng(ts_sum(day_durbin_watson(Vwap), 10), 10), 241)` |
| swap | `Vwap->Close` | -1.48 | -1.48 | -1.20 | — | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson(Close)), 10), 10), 241)` |
| window | `cross_fangzheng@241->120` | -2.07 | -1.19 | -2.07 | — | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10), 120)` |
| window | `cross_fangzheng@241->482` | -2.00 | -2.00 | -1.07 | — | `cross_fangzheng(cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10), 482)` |

### head score -2.50:`div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30)` | -2.56 | -1.10 | -2.56 | — | (子树本身) |
| sufficiency | `add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt))))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_sum(log(day_durbin_watson(Vwap)), 10)` | -3.56 | -3.56 | -2.11 | — | (子树本身) |
| sufficiency | `pow_2(cs_sum(day_autocorr_n1(Amt)))` | — | — | — | — | 门槛废品 |
| knockout | `cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30)` | -3.49 | -3.49 | -2.00 | +0.98 | `div(ts_sum(log(day_durbin_watson(Vwap)), 10), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| knockout | `add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt))))` | -3.06 | -2.04 | -3.06 | +0.55 | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), day_hurst(nt_ts_quantile_q75(High, 30)))` |
| knockout | `ts_sum(log(day_durbin_watson(Vwap)), 10)` | -2.12 | -0.65 | -2.12 | -0.39 | `div(cross_hurst(log(day_durbin_watson(Vwap)), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| knockout | `pow_2(cs_sum(day_autocorr_n1(Amt)))` | -2.49 | -1.05 | -2.49 | -0.02 | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), cs_sum(day_autocorr_n1(Amt))))` |
| swap | `Vwap->Close` | -2.89 | -1.39 | -2.89 | — | `div(cross_hurst(ts_sum(log(day_durbin_watson(Close)), 10), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| swap | `High->Low` | -2.51 | -1.06 | -2.51 | — | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), add(day_hurst(nt_ts_quantile_q75(Low, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| window | `cross_hurst@30->15` | -2.51 | -2.51 | -1.71 | — | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 15), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |
| window | `cross_hurst@30->60` | -2.35 | -2.02 | -2.35 | — | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 60), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |

### head score -2.59:`ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_fangzheng(log(day_durbin_watson(Vwap)), 10)` | -2.99 | -2.99 | -2.24 | — | (子树本身) |
| sufficiency | `log(day_durbin_watson(Vwap))` | -3.14 | -3.14 | -2.83 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `cross_fangzheng(log(day_durbin_watson(Vwap)), 10)` | -1.69 | -1.69 | -0.21 | -0.91 | `ts_std(log(day_durbin_watson(Vwap)), 40)` |
| knockout | `log(day_durbin_watson(Vwap))` | -2.34 | -0.54 | -2.34 | -0.25 | `ts_std(cross_fangzheng(day_durbin_watson(Vwap), 10), 40)` |
| swap | `Vwap->Close` | -3.40 | -0.59 | -3.40 | — | `ts_std(cross_fangzheng(log(day_durbin_watson(Close)), 10), 40)` |
| window | `ts_std@40->20` | -2.11 | -1.60 | -2.11 | — | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 20)` |
| window | `ts_std@40->80` | -2.30 | -0.63 | -2.30 | — | `ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 80)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.91(knockout cross_fangzheng(log(day_durbin_watson(Vwap)), 10)):`ts_std(log(day_durbin_watson(Vwap)), 40)`
- 增益 +0.49(window ts_std@40->20):`ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 20)`
- 增益 +0.29(window ts_std@40->80):`ts_std(cross_fangzheng(log(day_durbin_watson(Vwap)), 10), 80)`
- 增益 +0.25(knockout log(day_durbin_watson(Vwap))):`ts_std(cross_fangzheng(day_durbin_watson(Vwap), 10), 40)`
