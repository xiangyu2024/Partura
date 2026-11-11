# 定位:种子 2050,P 组,第 2 轮(只含 train / valid)

快照:prods2050M1_I0_open_search, prods2050M2_I0_open_search, prods2050Pr1a_Ea;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.33 | -2.33 | -1.95 | -1 | 0 | prods2050M1_I0_open_search | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 20)` |
| -2.58 | -2.58 | -1.59 | +1 | 20 | prods2050M1_I0_open_search | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 80)` |
| -2.74 | -1.34 | -2.74 | +1 | 5 | prods2050M1_I0_open_search | `cross_stddev(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 20)` |

## 共性:37 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.39 | 0.008 | 4 | -1.73 / -3.12 | `day_sum(Open)` |

## 拆解(6 次评估)

### head score -2.58:`cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 80)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -4.72 | -4.72 | -2.84 | — | (子树本身) |
| sufficiency | `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))` | -4.04 | -4.04 | -3.71 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.95 | -3.95 | -3.85 | — | (子树本身) |
| knockout | `div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret))` | -2.66 | -2.66 | -2.22 | +0.08 | `cross_mean(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 80)` |
| window | `cross_mean@80->40` | -2.79 | -2.79 | -1.61 | — | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 40)` |
| window | `cross_mean@80->160` | -2.18 | -2.18 | -1.10 | — | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 160)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_sum(Open)` — enrichment,均值差 +1.39,p 0.008

## 本组之前各轮的任务

- `prods2050Pr1a_Ea`:核心 `day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0)))`;评分 76,过线 0,入 heads 0;采样计数 {'c05_no_core': 2172, 'c05_skeleton': 1098}
  - score -0.56(train -0.56 valid -0.19):`cross_autocorr_s1(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 241)`
  - score -1.28(train -0.40 valid -1.28):`cross_corr(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_sum(Open), 30)`
  - score -1.54(train -0.76 valid -1.54):`cross_corr(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_sum(Open), 20)`
  - score -1.55(train -0.75 valid -1.55):`cross_corr(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_sum(Close), 20)`
  - score -1.56(train -1.35 valid -1.56):`cross_autocorr_s1(cross_autocorr_s1(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 241), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.40(window cross_mean@80->160):`cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 160)`
