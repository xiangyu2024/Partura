# 定位:种子 2068,P 组,第 1 轮(只含 train / valid)

快照:prods2068M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.61 | -1.31 | -1.61 | -1 | 5 | prods2068M1_I0_open_search | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| -2.16 | -1.88 | -2.16 | -1 | 20 | prods2068M1_I0_open_search | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| -2.86 | -2.64 | -2.86 | -1 | 20 | prods2068M1_I0_open_search | `day_sum(abs_(in_slice(Ret, 1, 30)))` |

## 共性:18 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(20 次评估)

### head score -1.61:`sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20)` | -1.32 | -1.20 | -1.32 | — | (子树本身) |
| sufficiency | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20)` | -3.25 | -3.25 | -2.62 | — | (子树本身) |
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` | -2.12 | -1.88 | -2.12 | — | (子树本身) |
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240))))` | -4.29 | -4.29 | -3.97 | — | (子树本身) |
| knockout | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20)` | -3.04 | -2.11 | -3.04 | +1.43 | `sub(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| knockout | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20)` | -2.55 | -2.10 | -2.55 | +0.94 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))))` |
| knockout | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` | -1.39 | -1.25 | -1.39 | -0.22 | `sub(ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| knockout | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240))))` | -1.40 | -1.28 | -1.40 | -0.21 | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20))` |
| swap | `High->Low` | -1.58 | -1.27 | -1.58 | — | `sub(ts_mean(mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| swap | `Low->High` | -1.55 | -1.34 | -1.55 | — | `sub(ts_mean(mul(div(sub(day_max(High), day_min(High)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(mul(div(sub(day_max(High), day_min(High)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| window | `ts_mean@20->10` | -2.34 | -1.49 | -2.34 | — | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 10), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |
| window | `ts_mean@20->40` | -1.95 | -1.95 | -1.81 | — | `sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 40), ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240)))), 20))` |

### head score -2.16:`mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.91 | -1.70 | -1.91 | — | (子树本身) |
| sufficiency | `day_sum(abs_(in_slice(Ret, 1, 30)))` | -2.82 | -2.64 | -2.82 | — | (子树本身) |
| sufficiency | `sub(day_max(High), day_min(Low))` | -2.18 | -1.53 | -2.18 | — | (子树本身) |
| sufficiency | `day_max(High)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.89 | -1.32 | -1.89 | -0.27 | `mul(sub(day_max(High), day_min(Low)), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| knockout | `sub(day_max(High), day_min(Low))` | -2.76 | -2.62 | -2.76 | +0.60 | `mul(div(day_max(High), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| swap | `High->Low` | -2.14 | -1.93 | -2.14 | — | `mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` |
| swap | `Low->High` | -2.13 | -1.86 | -2.13 | — | `mul(div(sub(day_max(High), day_min(High)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30))))` |

### head score -2.86:`day_sum(abs_(in_slice(Ret, 1, 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(knockout mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 211, 240))))):`sub(ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(in_slice(Ret, 1, 30)))), 20), ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20))`
