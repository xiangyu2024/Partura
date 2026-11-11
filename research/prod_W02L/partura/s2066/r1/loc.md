# 定位:种子 2066,P 组,第 1 轮(只含 train / valid)

快照:prods2066M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.14 | -0.76 | -1.14 | -1 | 20 | prods2066M1_I0_open_search | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` |
| -1.14 | -0.76 | -1.14 | -1 | 20 | prods2066M1_I0_open_search | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))))` |
| -1.15 | -0.83 | -1.15 | -1 | 20 | prods2066M1_I0_open_search | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)))))` |

## 共性:10 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(16 次评估)

### head score -1.14:`pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))` | -1.26 | -1.21 | -1.26 | — | (子树本身) |
| swap | `Close->Vwap` | -0.73 | -0.73 | +0.04 | — | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Vwap, 30))))` |
| window | `in_cov@30->15` | -1.14 | -0.83 | -1.14 | — | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15))))` |
| window | `in_cov@30->60` | -1.11 | -0.85 | -1.11 | — | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 60))))` |

### head score -1.14:`sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | -1.13 | -0.76 | -1.13 | — | (子树本身) |
| sufficiency | `day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))` | -1.26 | -1.21 | -1.26 | — | (子树本身) |
| knockout | `abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` | -1.26 | -1.21 | -1.26 | +0.13 | `sigmoid(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` |
| swap | `Close->Vwap` | -0.73 | -0.73 | +0.04 | — | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Vwap, 30)))))` |
| window | `in_cov@30->15` | -1.14 | -0.83 | -1.14 | — | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)))))` |
| window | `in_cov@30->60` | -1.11 | -0.85 | -1.11 | — | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 60)))))` |

### head score -1.15:`pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15))))` | -1.25 | -1.21 | -1.25 | — | (子树本身) |
| sufficiency | `day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)))` | -1.25 | -1.21 | -1.25 | — | (子树本身) |
| knockout | `pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15))))` | -1.14 | -0.83 | -1.14 | -0.00 | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15))))` |
| swap | `Close->Vwap` | -0.84 | -0.84 | -0.12 | — | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Vwap, 15)))))` |
| window | `in_cov@15->7` | -1.21 | -0.91 | -1.21 | — | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 7)))))` |
| window | `in_cov@15->30` | -1.13 | -0.76 | -1.13 | — | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
