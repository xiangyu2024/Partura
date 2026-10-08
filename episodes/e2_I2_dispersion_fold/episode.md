# 研究实验 `e2_I2_dispersion_fold`

想法 `I2_dispersion_fold`;奖励 `long_marginal`;每臂预算 192 个候选(种群 48,随机种子 0);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

## 假设

日内价格 / 收益的离散度离「同类股票的典型值」越近越好(既不死水也不乱跳);哪个离散度统计量、以谁为参照(全市场 / 同成交额档)、多长的记忆

## 干预(带指引的一臂)

- 种子进首代:`cross_ema(abs_(cs_demean(day_gini(Low))), 30)`、`abs_(cs_demean(day_mean(in_stddev_rolling(in_slice(Ret, 2, 237), 5))))`、`abs_(cs_bucket_demean(day_gini(Ret), cross_mean(day_sum(Amt), 30)))`
- 想法里的算子采样概率 × 8.0;候选必须含这些算子之一:day_gini、day_std、day_es_ratio_hi、day_es_ratio_lo、day_wstd、day_distinct_ratio
- 每棵候选树过指引 `guidance/B01.yaml`:封禁的不放行,降权 / 升权按概率放行,等价写法只放行第一个

## 对照

同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库;不带种子、不过指引、均匀采样。

## 证据

| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | 分数 ≥ 0 | 分数 ≥ 0.1 | 分数 ≥ 0.2 | 分数 ≥ 0.3 | **发现(分数 ≥ 0.2)** | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 带指引 | 104 | 17 | 87 | 79 / 80 | 7 | 0 | 0 | 0 | **0**(0 族) | +0.02 | +0.01 | — | 20 分 |
| 对照 | 125 | 21 | 104 | 80 / 80 | 9 | 1 | 0 | 0 | **0**(0 族) | +0.10 | +0.08 | — | 23 分 |

分数的含义:候选与已知池五五混合后的纯多头夏普减池子自己的,train 与 valid 取较差的(旧口径)。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 674 棵树:封禁 0、不在想法邻域 435、按权重抽掉 40、与已提过的等价 82、放行 117。

## 各臂找到的(互不等价的前几个;纯多头夏普 train / valid 是奖励口径下的)

**带指引**

- +0.02(train +1.66 / valid +3.67,半衰期 20,与已知族相关 +0.86):`cs_bucket_rank(cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 3))), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 3)))`
- +0.02(train +1.66 / valid +3.67,半衰期 20,与已知族相关 +0.86):`cs_bucket_demean(cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 3))), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 3)))`
- +0.02(train +1.66 / valid +3.67,半衰期 20,与已知族相关 +0.86):`cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(abs_(day_es_ratio_lo(Open)), 3)))`
- +0.01(train +1.74 / valid +3.56,半衰期 5,与已知族相关 +0.82):`cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 15)))`
- +0.00(train +1.65 / valid +3.70,半衰期 20,与已知族相关 +0.88):`cs_bucket_rank(day_mean(Amt), cs_bucket_zscore(cross_valid_count(cs_robust_z(ts_var(day_es_ratio_hi(pow_05(Volume)), 10)), 30), abs_(abs_(ts_pearson(inv(log(day_es_ratio_hi(Amt))), 40)))))`
- +0.00(train +1.65 / valid +3.67,半衰期 20,与已知族相关 +0.86):`cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(pow_1_5(abs_(day_es_ratio_lo(Open))), 3)))`
- +0.00(train +1.74 / valid +3.55,半衰期 20,与已知族相关 +0.79):`cs_bucket_rank(cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 30))), cs_demean(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 30)))`
- -0.00(train +1.64 / valid +3.63,半衰期 20,与已知族相关 +0.84):`cs_bucket_rank(day_mean(Amt), cs_demean(cross_stddev(pow_3(cross_stddev(pow_3(abs_(day_es_ratio_lo(Open))), 10)), 3)))`

**对照**

- +0.10(train +1.75 / valid +3.67,半衰期 20,与已知族相关 +0.17):`day_quantile_q25(in_delta(in_delta(nt_ts_var(Amt, 60), 60), 60))`
- +0.10(train +1.74 / valid +3.71,半衰期 20,与已知族相关 +0.85):`day_std(Amt)`
- +0.08(train +1.74 / valid +3.62,半衰期 20,与已知族相关 +0.85):`day_quantile_q25(in_delta(in_delta(nt_ts_var(in_delta(in_delta(nt_ts_var(Amt, 60), 60), 5), 5), 5), 60))`
- +0.06(train +1.84 / valid +3.61,半衰期 20,与已知族相关 +0.80):`day_std(in_delta(in_delta(nt_ts_var(Amt, 60), 60), 60))`
- +0.04(train +1.69 / valid +3.64,半衰期 20,与已知族相关 +0.83):`day_quantile_q25(in_delta(in_delta(in_delta(in_delta(nt_ts_var(Amt, 5), 5), 60), 5), 60))`
- +0.03(train +1.73 / valid +3.57,半衰期 20,与已知族相关 +0.77):`day_quantile_q25(in_delta(nt_ts_var(Amt, 60), 60))`
- +0.03(train +1.67 / valid +3.70,半衰期 20,与已知族相关 +0.85):`day_quantile_q25(in_delta(in_delta(nt_ts_var(Amt, 5), 5), 60))`
- +0.02(train +1.97 / valid +3.57,半衰期 20,与已知族相关 +0.81):`day_std(nt_ts_var(Amt, 3))`

## 信念更新

**假设没有被否定,被否定的是奖励的写法。**

- 池子(排掉冻结盘口的已知族)在这个奖励的股票池里自己的纯多头夏普是 train 1.64、valid 3.55。种子与它五五混合之后:
  `cross_ema(abs_(cs_demean(day_gini(Low))), 30)` train 2.28(**+0.64**)、valid 3.36(−0.19);
  `abs_(cs_demean(day_mean(in_stddev_rolling(Ret, 10))))` train 1.97(**+0.33**)、valid 3.54(−0.01)。
  也就是说:在 2018–2021,离散度折叠给池子加 0.3~0.6 夏普;在 2022-01~2023-08(已知族自己夏普 3.55 的一段),掺什么进去都是持平或略降,而且降幅在噪声(±0.3)以内。
- 奖励取「两段里较差的增量」,于是这类候选全部得负分,192 个预算两臂都是 0 个过线(带指引最好 +0.02,对照最好 +0.10)。
  **R3(对池子的边际贡献)与 R4(取两段较差者)不能这样叠用**:在池子本身夏普 3.5 的一段里要求「再加 0.2」是不讲统计的。
- 改法(等审查工作流结束后改 `partura/steer.py`):边际 / 筛子类奖励改成**成对的逐日差**(混合书减池子书)在 train+valid 合并段上的信息比;
  任一段的成对信息比低于 −1 才判负。水平类奖励(`long` / `long_tradable` / `long_bucket`)仍取两段较差者。
- 另一条:带指引的一臂为了满足「必须含想法的算子」,把想法的算子塞进了 `cs_bucket_rank(day_mean(Amt), <想法的东西>)` 的**分桶键**里,排序用的还是成交额水平(与已知族相关 0.86)。
  「含有」太弱 —— 邻域约束要写成结构(想法的算子必须在被排序的那条路径上),或者干脆交给奖励去罚。新规则:`cs_bucket_rank(cs_bucket_rank(_1, _2), _2)` 改写成内层。
- 对规则的影响:U2(有界的日内离散度统计量,升权)不变;R3 的状态从「已实现」改成「已实现,口径待改(见本实验)」。

