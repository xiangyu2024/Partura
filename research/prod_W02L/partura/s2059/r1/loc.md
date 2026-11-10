# 定位:种子 2059,P 组,第 1 轮(只含 train / valid)

快照:prods2059M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.92 | -1.76 | -1.92 | -1 | 5 | prods2059M1_I0_open_search | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` |
| -2.28 | -1.32 | -2.28 | -1 | 5 | prods2059M1_I0_open_search | `cross_min(day_max(nt_cs_regres(Ret, Low)), 60)` |
| -2.39 | -2.28 | -2.39 | -1 | 20 | prods2059M1_I0_open_search | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15)` |

## 共性:13 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.09 | 0.418 | 6 | -2.88 / -2.97 | `day_max(nt_cs_regres(Ret, Low))` |
| -0.41 | 0.889 | 5 | -3.18 / -2.77 | `day_max(nt_cs_regres(Amt, Low))` |

## 拆解(14 次评估)

### head score -1.92:`cross_min(day_max(nt_cs_regres(High, Low)), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(nt_cs_regres(High, Low))` | -1.85 | -1.66 | -1.85 | — | (子树本身) |
| swap | `High->Low` | — | — | — | — | `cross_min(day_max(nt_cs_regres(Low, Low)), 15)` |
| swap | `Low->High` | — | — | — | — | `cross_min(day_max(nt_cs_regres(High, High)), 15)` |
| window | `cross_min@15->7` | -1.72 | -1.72 | -1.68 | — | `cross_min(day_max(nt_cs_regres(High, Low)), 7)` |
| window | `cross_min@15->30` | -2.02 | -1.94 | -2.02 | — | `cross_min(day_max(nt_cs_regres(High, Low)), 30)` |

### head score -2.28:`cross_min(day_max(nt_cs_regres(Ret, Low)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(nt_cs_regres(Ret, Low))` | -3.49 | -2.46 | -3.49 | — | (子树本身) |
| swap | `Low->High` | -2.25 | -1.32 | -2.25 | — | `cross_min(day_max(nt_cs_regres(Ret, High)), 60)` |
| window | `cross_min@60->30` | -2.31 | -2.30 | -2.31 | — | `cross_min(day_max(nt_cs_regres(Ret, Low)), 30)` |
| window | `cross_min@60->120` | -1.43 | -0.58 | -1.43 | — | `cross_min(day_max(nt_cs_regres(Ret, Low)), 120)` |

### head score -2.39:`cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_min(day_max(nt_cs_regres(Ret, Low)), 15)` | -2.79 | -2.79 | -2.70 | — | (子树本身) |
| sufficiency | `day_max(nt_cs_regres(Ret, Low))` | -3.49 | -2.46 | -3.49 | — | (子树本身) |
| swap | `Low->High` | -2.35 | -2.28 | -2.35 | — | `cross_min(cross_min(day_max(nt_cs_regres(Ret, High)), 15), 15)` |
| window | `cross_min@15->7` | -2.69 | -2.69 | -2.37 | — | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 7)` |
| window | `cross_min@15->30` | -2.28 | -1.53 | -2.28 | — | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 30)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.85(window cross_min@60->120):`cross_min(day_max(nt_cs_regres(Ret, Low)), 120)`
- 增益 +0.20(window cross_min@15->7):`cross_min(day_max(nt_cs_regres(High, Low)), 7)`
- 增益 +0.11(window cross_min@15->30):`cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 30)`
