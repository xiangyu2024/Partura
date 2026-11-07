
# 第 1 轮(种子 908)

## 我现在对本种子 alpha 来源的信念(只依据 M 第 1 批 + 定位,train/valid)

- 最强的一条线:day_centroid(Amt) = 成交额在日内的重心。含它的候选 26/86,均分 -0.25 对 -1.51(p≈0);单独用(早盘重者多头,hl 20)train 1.05 / valid 0.41,
  差 valid 一点没到 0.5。head1 = ts_quantile_q75(cs_regres(ListAge, pow_3(centroid)), 10) = 0.75。
- 读源码后的重要事实(dailyfields.py):ListAge 对 2018-01-02 已上市的股票全部是 10000+d(一个并列块),只有之后的新股是真实天数。
  所以 head1 的 cs_regres(ListAge, c^3) 实质是'老股 vs 次新股分组 + 老股内部按 centroid 排序'。凡是'ListAge 当 Y、centroid 当 X'的写法都会和 head1 高度同构
  (日度秩 ρ 很可能 ≥ 0.7,会被库禁令 / 相关度表划掉),所以 E 的种子必须换路径:ListAge 当 X(同类桶、回归掉),或根本不用 ListAge。
- ListAge 单独不是 alpha(cs_regres(ListAge, c^3) 自己 -0.37,ts_quantile_q75(ListAge,10) 过不了 distinct 闸门);ts 上的 q75 才把它变成 +0.75。
  窗口 5/10/20 = 0.51/0.75/0.90 单调,Volume 版 0.82 > Amt 版 0.75:信号慢变、越平滑越好,所以我判断 centroid 是'水平'(股票的交易风格)而不是'变化'。
- head2 = 价格十分位桶内 z-score(q25(High) 对 wmean(Open,Amt))。两个子树单独 -1.35/-1.33,换 Low / Close 都 ≈ 0.49:
  我不确定它读的是日内漂移还是桶内名义价格水平,两种读法都说得通,不押它;本轮只在 R 里动它外层的选择。
- 弱证据:cs_regres(ListAge, LogFloatShares) 4 个候选 +0.82(p 0.074),很可能还是 ListAge 老股/次新分组;day_max(Ret) 5 个候选 -1.55(不显著),'彩票型'一类不押。

## 本轮计划

- 位 1(E,核心 day_centroid(Amt)):14 个种子,外围一个都不用 ts_quantile_q75 / pow_3 / ListAge 作 Y。四类:
  (a) 时间轴估计量 cross_mean / ema / med / quantile_q25;(b) 去混杂方向相反——centroid 当 Y 对 ListAge 回归 / 在 ListAge、流通股本、价格水平的十分位桶内 z-score;
  (c) 证伪用:cross_zscore(40)、5 日减 60 日(去掉水平);(d) 买入分钟 vs 卖出分钟的成交额重心之差、Amt 与 Volume 重心之差(= 量加权日内价格趋势)。
  核心 day_centroid(Amt) 这是第 1 个 E 位(上限 2)。
- 位 2(N):'日内活动的时间结构'的其他估计量(爆发时点 day_topw_mean(in_index)、时间对成交额的相关、|Ret| 重心、开盘 / 尾盘 30 分钟占比、
  下午半场内部重心、买卖分钟重心差、价格路径对时间的相关)。14 个种子,不含 day_centroid(Amt)、ListAge、pow_3、桶。
  选这个而不是'名义价格 / 流通股本'的理由:证据强度差一个量级(p≈0 对 p=0.07);如果本轮 E 和 N 都没出 head,第 2 轮转去价格 / 股本结构那一条线。
- R:head1 8 个变体(窗口拉长 + Volume 叠加 + 去 pow_3 + 换 q50 / 均值);head2 6 个变体(只动外层:桶内 rank / demean、权重 Volume、q75、中位数)。共 14。

## 事先预测(下一轮要对答案)

1. E 位:至少产出 1 个 head 的概率约 45%。若有,最可能是'centroid 的时间平滑 / 下尾分位(cross_quantile_q25、cross_mean 20)'或
   '在 ListAge 十分位桶内 z-score 的 centroid',方向 = 低 centroid 多头,hl 20,train ≈ 1.0-1.3,valid 0.5-0.7(valid 是瓶颈)。
   证伪种子(cross_zscore 40、5 减 60)我预测不出 head,分数明显低于水平写法(若它们反而好,说明我对'水平而非变化'的判断是错的)。
   买卖方向拆分(种子 12、13)预测 train 好 valid 差。最大风险:所有 ListAge 桶 / 回归种子与 head1 的 |ρ| ≥ 0.7 被划掉,只剩纯时间平滑种子。
   96 次评估里大部分候选会是 0.2-0.5 的'差一点'(valid 受限)。
2. N 位:至少 1 个 head 的概率约 25%。若有,最可能来自 day_topw_mean(in_index(Amt), Amt) 或 day_corr(in_index(Amt), Amt)(与 centroid 同一潜变量,
   但 ρ 不到 0.7)。开盘 / 尾盘 30 分钟占比预测与流动性控制相关高、被奖励尺子吃掉;day_centroid(Ret) 与 day_corr(in_index(Close), Close) 预测弱。
3. R:head1 的窗口 20 变体(已知 +0.896,ρ 0.96)几乎肯定替换(概率 90%);Volume + 窗口 20/30 叠加的变体有 ~60% 概率比 20 版更高;
   去 pow_3 / 换 q50 / 换均值预测不如 q75。head2 的变体有 ≥ 0.68 的概率约 15%,最可能是 cs_bucket_rank。
4. 上一轮预测:无(这是第 1 轮)。

## 下一轮要看的

- E 位里哪一类种子活到最后(时间平滑 / ListAge 桶 / 方向拆分),证伪种子是否真的差。
- 哪些种子被相关度表划掉(|ρ| ≥ 0.7 对 head1 的是 ListAge 路径;≥ 0.8 对控制的)。
- N 位里是不是还是 Amt 的时间结构出 head;出的话与 E 的 head 是否同一个潜变量(ρ)。
