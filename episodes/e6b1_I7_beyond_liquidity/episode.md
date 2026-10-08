# 研究实验 `e6b1_I7_beyond_liquidity`

想法 `I7_beyond_liquidity`;奖励 `long_bucket`;每臂预算 384 个候选(种群 48,随机种子 1);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

## 假设

把「躲垃圾票」和「偏向低流动性」两样都从奖励里拿掉之后(可交易池、成交额十档内排名),还有没有两段都站得住的选股内容;手里最接近的两条是「20 日收盘价走势的线性度」(桶内 +0.56 / +0.94)和「日内收益基尼系数减同档均值」(+0.49 / +0.68)

## 干预(带指引的一臂)

- 种子进首代:`ts_pearson(day_last(Close), 20)`、`cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))`
- 想法里的算子采样概率 × 8.0;候选必须含这些算子之一:(不限)
- 每棵候选树过指引 `guidance/B01.yaml`:封禁的不放行,降权 / 升权按概率放行,等价写法只放行第一个

## 对照

同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库;不带种子、不过指引、均匀采样。

## 证据

| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | 分数 ≥ 0 | 分数 ≥ 0.3 | 分数 ≥ 0.5 | 分数 ≥ 1 | **发现(分数 ≥ 0.75)** | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 带指引 | 214 | 25 | 189 | 80 / 80 | 46 | 18 | 4 | 0 | **0**(0 族) | +0.73 | +0.57 | — | 41 分 |
| 对照 | 192 | 37 | 155 | 80 / 80 | 1 | 1 | 0 | 0 | **0**(0 族) | +0.37 | +0.01 | — | 32 分 |

分数的含义:可交易池里、成交额十档内排名之后的纯多头夏普,train 与 valid 取较差的。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 692 棵树:封禁 1、不在想法邻域 0、按权重抽掉 238、与已提过的等价 0、放行 384。

## 各臂找到的(互不等价的前几个;纯多头夏普 train / valid 是奖励口径下的)

**带指引**

- +0.73(train +0.73 / valid +1.22,半衰期 20,与已知族相关 +0.23):`ts_pearson(day_last(Close), 10)`
- +0.56(train +0.56 / valid +0.94,半衰期 20,与已知族相关 +0.29):`ts_pearson(day_last(Close), 20)`
- +0.54(train +0.54 / valid +0.74,半衰期 20,与已知族相关 -0.05):`cs_bucket_demean(ts_pearson(day_last(Close), 20), cross_mean(day_sum(Amt), 30))`
- +0.54(train +0.54 / valid +1.06,半衰期 20,与已知族相关 -0.68):`cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(ts_pearson(day_last(Close), 5), 30))`
- +0.49(train +0.49 / valid +1.03,半衰期 20,与已知族相关 -0.66):`cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(ts_pearson(day_last(Open), 20), 30))`
- +0.49(train +0.49 / valid +0.68,半衰期 20,与已知族相关 +0.11):`cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))`
- +0.47(train +0.47 / valid +1.00,半衰期 20,与已知族相关 +0.30):`cross_mean(ts_pearson(day_last(Open), 20), 3)`
- +0.47(train +0.47 / valid +0.56,半衰期 60,与已知族相关 +0.21):`ts_pearson(cross_mean(ts_pearson(day_last(Close), 20), 30), 20)`

**对照**

- +0.37(train +0.37 / valid +1.10,半衰期 60,与已知族相关 -0.06):`day_gini(cross_hurst(Low, 15))`
- -0.06(train -0.04 / valid -0.06,半衰期 20,与已知族相关 -0.72):`cross_ema(day_gini(Ret), 3)`
- -0.07(train -0.07 / valid +0.19,半衰期 20,与已知族相关 -0.71):`cross_ema(cross_tail_mean_q75(cross_ema(day_gini(Ret), 3), 3), 3)`
- -0.09(train -0.09 / valid -0.02,半衰期 60,与已知族相关 -0.71):`cross_tail_mean_q75(cross_ema(day_gini(Ret), 3), 3)`
- -0.10(train -0.10 / valid +0.20,半衰期 20,与已知族相关 -0.70):`cross_ema(cross_tail_mean_q75(cross_ema(day_gini(Ret), 3), 5), 3)`
- -0.10(train -0.10 / valid +0.11,半衰期 20,与已知族相关 -0.73):`cross_ema(cross_ema(day_gini(Ret), 3), 3)`
- -0.13(train -0.13 / valid -0.12,半衰期 5,与已知族相关 -0.72):`cross_ema(cross_ema(cross_ema(day_gini(Ret), 3), 3), 3)`
- -0.14(train -0.14 / valid +0.28,半衰期 20,与已知族相关 -0.74):`cross_ema(day_gini(Ret), 10)`

## 信念更新

**种子 1(桶内奖励,发现线 0.75):带指引最好 +0.73、0 族过线;对照最好 +0.37、0 族。三个种子合读见 `episodes/e6_SUMMARY.md`:唯一过线的候选样本外没有站住,结论是该换信息源。**

