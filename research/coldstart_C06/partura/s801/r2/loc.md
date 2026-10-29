# 定位:种子 801,C 组,第 2 轮(只含 train / valid)

快照:c05s801M1_I0_open_search, c05s801M2_I0_open_search, c06s801Cr1a_Na, c06s801Cr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(5 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.53 | +1.53 | +3.39 | -1 | 5 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| +1.22 | +1.30 | +1.22 | -1 | 20 | c06s801Cr1b_Nb | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)` |
| +0.75 | +0.75 | +1.66 | -1 | 0 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| +0.61 | +0.61 | +2.61 | +1 | 20 | c06s801Cr1a_Na | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)` |
| +0.50 | +0.50 | +0.79 | -1 | 20 | c05s801M1_I0_open_search | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` |

## 共性:326 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.58 | 0.003 | 4 | +0.79 / -0.79 | `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` |
| +1.37 | 0.001 | 7 | +0.57 / -0.80 | `day_sum(pow_3(Volume))` |
| +1.37 | 0.000 | 28 | +0.48 / -0.89 | `pow_3(LogFloatShares)` |
| +1.30 | 0.000 | 12 | +0.48 / -0.82 | `pow_05(pow_3(LogFloatShares))` |
| +1.29 | 0.000 | 10 | +0.48 / -0.81 | `pow_3(pow_3(LogFloatShares))` |
| +1.28 | 0.008 | 4 | +0.50 / -0.78 | `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` |
| +1.27 | 0.003 | 6 | +0.48 / -0.79 | `pow_3(pow_05(pow_3(LogFloatShares)))` |
| +1.27 | 0.007 | 5 | +0.48 / -0.79 | `pow_05(LogFloatShares)` |
| +1.27 | 0.009 | 5 | +0.48 / -0.79 | `pow_2_5(LogFloatShares)` |
| +1.27 | 0.010 | 4 | +0.48 / -0.78 | `pow_05(pow_3(pow_3(LogFloatShares)))` |
| +1.26 | 0.018 | 4 | +0.48 / -0.78 | `pow_05(pow_2_5(LogFloatShares))` |
| +1.25 | 0.016 | 4 | +0.47 / -0.78 | `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` |
| +1.25 | 0.007 | 5 | +0.47 / -0.79 | `cs_state_rank(log(day_first(Open)), 50)` |
| +1.24 | 0.003 | 8 | +0.44 / -0.80 | `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))` |
| +1.22 | 0.018 | 4 | +0.44 / -0.78 | `mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))` |
| +1.15 | 0.029 | 5 | +0.37 / -0.79 | `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` |
| +1.09 | 0.001 | 18 | +0.27 / -0.83 | `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` |
| +0.98 | 0.042 | 4 | +0.20 / -0.78 | `cs_state_rank(day_es_ratio_hi(Vwap), 50)` |
| +0.98 | 0.042 | 4 | +0.20 / -0.78 | `day_es_ratio_hi(Vwap)` |
| +0.94 | 0.000 | 28 | +0.09 / -0.85 | `cs_state_rank(day_es_ratio_hi(High), 50)` |

## 拆解(41 次评估)

### head score +1.53:`cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241)` | -0.98 | +0.15 | -0.98 | — | (子树本身) |
| sufficiency | `cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open)))` | -0.44 | +0.72 | -0.44 | — | (子树本身) |
| sufficiency | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` | +0.68 | +0.68 | +1.18 | — | (子树本身) |
| knockout | `cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241)` | -1.90 | +0.13 | -1.90 | +3.43 | `cs_first_high40(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| knockout | `cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open)))` | +1.44 | +1.44 | +3.83 | +0.09 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| knockout | `cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open)))` | +1.54 | +1.54 | +3.39 | -0.01 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))))` |
| knockout | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` | +1.46 | +1.46 | +3.63 | +0.07 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| swap | `High->Low` | +1.53 | +1.53 | +3.39 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Low), 50), log(day_first(Open)))), log(day_first(Open))))` |
| swap | `Open->Close` | +1.48 | +1.48 | +3.39 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), log(day_first(Close))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Close)))), log(day_first(Close))))` |
| window | `cross_corr@241->120` | +1.35 | +1.35 | +2.54 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 120), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| window | `cross_corr@241->482` | +1.33 | +1.33 | +1.34 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 482), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |

### head score +1.22:`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume))))` | +0.83 | +0.93 | +0.83 | — | (子树本身) |
| sufficiency | `day_sum(mul(mul(Ret, Ret), Ret))` | -0.35 | +0.14 | -0.35 | — | (子树本身) |
| sufficiency | `mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))` | -1.65 | -0.16 | -1.65 | — | (子树本身) |
| sufficiency | `day_sum(pow_3(Volume))` | -1.82 | +0.04 | -1.82 | — | (子树本身) |
| knockout | `div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume))))` | -0.52 | -0.00 | -0.52 | +1.73 | `cross_mean(day_sum(mul(mul(Ret, Ret), Ret)), 20)` |
| knockout | `mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))` | +0.70 | +0.70 | +1.46 | +0.52 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), day_sum(pow_3(Volume))), 20)` |
| swap | `Volume->Amt` | — | — | — | — | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Amt)), day_sum(pow_3(Amt)))), 20)` |
| window | `cross_mean@20->10` | +1.14 | +1.36 | +1.14 | — | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 10)` |
| window | `cross_mean@20->40` | +1.18 | +1.35 | +1.18 | — | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 40)` |

### head score +0.75:`cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241)` | -0.34 | -0.34 | -0.29 | — | (子树本身) |
| sufficiency | `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` | +0.00 | +0.00 | +1.85 | — | (子树本身) |
| sufficiency | `cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))` | +0.00 | +0.00 | +1.85 | — | (子树本身) |
| knockout | `cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241)` | -1.99 | +0.56 | -1.99 | +2.74 | `cs_first_high40(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| knockout | `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` | -0.38 | -0.38 | +1.63 | +1.13 | `cs_first_high40(cross_corr(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| knockout | `cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))` | -0.55 | +0.33 | -0.55 | +1.30 | `cs_first_high40(cross_corr(inv(cs_state_rank(day_es_ratio_hi(Vwap), 50)), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| knockout | `cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))` | +0.32 | +0.33 | +0.32 | +0.43 | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_state_rank(day_es_ratio_hi(Vwap), 50), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| swap | `Vwap->Close` | +0.75 | +0.75 | +1.66 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Close), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Close), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Close), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| swap | `High->Low` | +0.75 | +0.75 | +1.66 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(Low), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(Low), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(Low), 50))))` |
| window | `cross_corr@241->120` | +0.22 | +1.13 | +0.22 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 120), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| window | `cross_corr@241->482` | -0.54 | +0.45 | -0.54 | — | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 482), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |

### head score +0.61:`cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` | +0.48 | +0.48 | +2.34 | — | (子树本身) |
| sufficiency | `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))` | -2.36 | -2.36 | +0.62 | — | (子树本身) |
| sufficiency | `sub(day_wmean(Ret, Amt), day_mean(Ret))` | -2.15 | -1.27 | -2.15 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Amt)` | -1.87 | -1.12 | -1.87 | — | (子树本身) |
| knockout | `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` | +0.38 | +0.38 | +2.23 | +0.23 | `cross_mean(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 15)` |
| knockout | `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))` | +0.06 | +0.06 | +1.65 | +0.54 | `cross_mean(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 10), 15)` |
| knockout | `sub(day_wmean(Ret, Amt), day_mean(Ret))` | +0.38 | +0.38 | +2.12 | +0.23 | `cross_mean(cross_ema(div(day_wmean(Ret, Amt), day_std(Ret)), 10), 15)` |
| swap | `Amt->Volume` | +0.60 | +0.60 | +2.64 | — | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_std(Ret)), 10), 15)` |
| window | `cross_mean@15->7` | +0.65 | +0.65 | +2.64 | — | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 7)` |
| window | `cross_mean@15->30` | +0.50 | +0.50 | +2.73 | — | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume))))` — ablation,自身 score +0.83(所在 head +1.22)
2. `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` — enrichment,均值差 +1.58,p 0.003
3. `day_sum(pow_3(Volume))` — enrichment,均值差 +1.37,p 0.001
4. `pow_3(LogFloatShares)` — enrichment,均值差 +1.37,p 0.000
5. `pow_05(pow_3(LogFloatShares))` — enrichment,均值差 +1.30,p 0.000
6. `pow_3(pow_3(LogFloatShares))` — enrichment,均值差 +1.29,p 0.000
7. `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` — enrichment,均值差 +1.28,p 0.008
8. `pow_3(pow_05(pow_3(LogFloatShares)))` — enrichment,均值差 +1.27,p 0.003
9. `pow_05(LogFloatShares)` — enrichment,均值差 +1.27,p 0.007
10. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.27,p 0.009
11. `pow_05(pow_3(pow_3(LogFloatShares)))` — enrichment,均值差 +1.27,p 0.010
12. `pow_05(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.26,p 0.018
13. `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` — enrichment,均值差 +1.25,p 0.016
14. `cs_state_rank(log(day_first(Open)), 50)` — enrichment,均值差 +1.25,p 0.007
15. `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))` — enrichment,均值差 +1.24,p 0.003
16. `mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))` — enrichment,均值差 +1.22,p 0.018
17. `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` — enrichment,均值差 +1.15,p 0.029
18. `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` — enrichment,均值差 +1.09,p 0.001
19. `cs_state_rank(day_es_ratio_hi(Vwap), 50)` — enrichment,均值差 +0.98,p 0.042
20. `day_es_ratio_hi(Vwap)` — enrichment,均值差 +0.98,p 0.042
21. `cs_state_rank(day_es_ratio_hi(High), 50)` — enrichment,均值差 +0.94,p 0.000
22. `cross_ema(day_corr(Ret, Amt), 10)` — enrichment,均值差 +0.85,p 0.083
23. `log(day_first(Open))` — enrichment,均值差 +0.72,p 0.000
24. `day_first(Open)` — enrichment,均值差 +0.69,p 0.000
25. `day_corr(Ret, Amt)` — enrichment,均值差 +0.67,p 0.100
26. `day_wmean(Ret, Amt)` — enrichment,均值差 +0.56,p 0.057
27. `sub(day_wmean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +0.53,p 0.066
28. `day_es_ratio_hi(High)` — enrichment,均值差 +0.49,p 0.012

## 本组之前各轮的任务

- `c06s801Cr1a_Na`:核心 `—`;评分 86,过线 1,入 heads 1;采样计数 {}
  - score +0.61(train +0.61 valid +2.61):`cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)`
  - score +0.50(train +0.50 valid +2.90):`cross_ema(cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15), 10)`
  - score +0.48(train +0.48 valid +2.34):`cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)`
  - score +0.44(train +0.44 valid +2.21):`cross_mean(div(cross_ema(day_corr(Ret, Amt), 10), day_std(Ret)), 15)`
  - score +0.43(train +0.43 valid +2.45):`cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 15)`
- `c06s801Cr1b_Nb`:核心 `—`;评分 83,过线 4,入 heads 1;采样计数 {}
  - score +1.22(train +1.30 valid +1.22):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)`
  - score +0.79(train +0.79 valid +1.28):`cross_mean(div(day_sum(mul(mul(Ret, in_logchg(Close, 1)), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))), 20)`
  - score +0.72(train +0.72 valid +1.64):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(mul(Ret, Ret), Ret))))), 20)`
  - score +0.55(train +0.55 valid +1.47):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))), 20)`
  - score +0.38(train +0.38 valid +1.38):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
