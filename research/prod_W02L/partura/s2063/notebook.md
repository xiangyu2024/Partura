
## 第 1 轮

信念:本批 3 个 head 全亏(−1.2 / −1.3 / −2.0),富集表为空,单点水平统计(day_min / day_var / day_quantile + nt_ 算子)在新尺子下只剩成本;唯一线索是 day_cov(Ret, Low) 换成 High 增益 +0.45,指向日内路径 / 顺序信息,而不是水平。nt_ 不能进种子,所以核心只能取 day_cov(Ret, Low)。

预测:
- E(核心 day_cov(Ret, Low)):去量纲 + 价位十分位内标准化 + 慢化。我预计小概率(约 20%)出 head;若出,多半是 cross_mean(div(cov, day_mean(Low)), 20) 一类,方向看路径凸性。失败原因多半是被反转 / 波动控制吃掉。
- N(日内成交重心 / 集中度):新算子,库里没有,约 25% 出 head;最可能是 day_centroid(Volume) 20 日均值或重心差;风险是与流动性相关被残差化后剩不下。
- R:High 版本去 nt_ 与量纲修复,约 30% 概率比原 head 好 0.1 以上,但与已知族相关与否未知。
上一轮:无(第 1 轮)。

## 第 2 轮

信念:本批 6 个 head 仍全亏(-1.2 到 -2.0),第 1 轮 E(day_cov(Ret,Low) 去量纲)最好 -0.42,N(重心 / gini)的搭配 cs_last_high20 -0.96,都没过线。亏的共同点是「单点水平 / 组合出来的水平」。富集表给了两个干净的子树:day_var(Ret)(波动水平,但被控制吃掉)和 ts_delta(LogFloatShares, 50)(日频供给冲击,与分钟统计正交)。我判断水平读数没有 alpha,可能的来源是:(1) 波动的时间序列形状(vol-of-vol、杠杆相关);(2) 股本供给变化这类非价量信息。其他种子里出过正分的写法(hurst + 长窗口 max)属于别的流,本流不碰。
本轮不放 N:第 1 轮 N 已通过审计,满足 3 轮至少 1 个 N 的要求;这轮把两个位给两个富集最强且互相独立的核心(各自第一次作 E)。不放 R:唯一 R 候选(去 log)增益 +0.27 也离 0.5 线很远,且含 nt_ 不能进种子。
预测:
- E(day_var(Ret)):约 20% 出 head(score≥0.5 的概率更低,约 10%);若出,最可能是 cross_corr(day_var, day_sum(Ret), 60) 或变异系数的市值内标准化;失败原因是与波动控制仍有残余的非单调关系,或杠杆相关太噪。
- E(ts_delta(LogFloatShares, 50)):约 15% 出 head;最可能是 ListAge 或名义股价内标准化后的 50 日差,方向为供给增加者弱;风险是大量取值为 0 且覆盖低,有效票少,换手成本不占优势。
上一轮预测检查:第 1 轮预测 E 约 20% 出 head、N 约 25%、R 约 30% 比原 head 好 0.1。实际全部没出 head;R 变体全部更差(-3.38 起),Low 换 High 的增益在加上 Amt 项后并不成立,预测对 E/N 偏乐观,R 错。

## 第 3 轮

信念:本批 9 个 head 全亏(-0.70 到 -2.02),两轮共 6 个任务位没有一个过线。唯一接近的是第 2 轮 E(day_var(Ret))里 cs_bucket_zscore(cross_corr(day_var(Ret), day_sum(Ret), 241), 名义股价) 的 -0.01(valid +0.18,train 偏负);含 cross_corr(day_var(Ret), day_sum(Ret), 60) 的 11 个候选均值 -0.70,是本批最强共性。我的判断:alpha 若在,来自「杠杆 / 波动-收益耦合」这类个股慢变结构属性,而不是水平;train 与 valid 方向不一致是主要障碍(score 取较差者)。R 候选只有含 nt_ 的 head 且增益 < 0.8,离线太远,本轮不放 R。N 已在第 1 轮通过审计,本轮再放一个 N 用新算子(尾部形状),另一位把 C=cross_corr(day_var(Ret), day_sum(Ret), 60) 首次作 E 核心。
预测:
- E(C):约 25% 出 head、约 10% 过 0.5;若出,最可能是 cross_ema / cross_zscore 慢化版或 cs_flip_by_state 版(市场状态翻转);失败原因是 train 段杠杆方向与 valid 相反,慢化后仍补不回。
- N(尾部形状 es_ratio):约 15% 出 head;最可能是 Volume 右尾的 20 日均值在市值分桶内;风险是与流动性控制相关被残差化,或涨停日置缺丢票。
上一轮预测检查:第 2 轮预测 E(day_var) 约 20% 出 head、E(ts_delta 股本) 约 15%。实际都没出 head(最好 -0.01 与 -0.83);E(day_var) 最可能写法 cross_corr(day_var, day_sum(Ret), 60) 方向对(它确实是最好的),但「约 10% 过 0.5」落空;ts_delta 股本位覆盖低 / 阶梯并列,预测的风险应验。
