
## 第 1 轮

信念:本批 3 个 head(day_kurt / day_skew / day_pdf_tail_sum_m 作用在标准化分钟收益 Z 上)分数 −1.74 到 −4.22,方向全 −1,窗口改动几乎不动分数。推断(无毛收益数):单一形状统计量毛超额约为 0,亏的是换手;alpha 来源不明,本种子可能很难出 head。

预测:
- E(核心 = day_kurt(Z)):换外围(自身 z 分数 / EMA / 十分位内 / 对波动残差 / 与收益相关)。预测大概率仍出不了 head(60%),若出,最可能是 cross_corr / cross_regres 类的慢变关系型,理由是水平控制对它们先天近似正交、换手低。
- N(左右尾期望缺口之差 + 放量分钟方向):预测出 head 的概率约 25%,若出,最可能是 es_ratio 的 60 日均值或放量分钟方向偏离,理由是 A 股彩票偏好。
- R(kurt head 的聚合替换):预期有 1 到 2 个变体比原 head 好 0.1 以上(慢聚合降换手),但仍在 0.5 以下。
上一轮:无(第 1 轮)。

## 第 2 轮

信念:第 1 轮的形状统计量(峰度 / 偏度 / 尾部和)全亏,alpha 不在那里。真正的线索来自 Pr1a 的正分候选(cross_regbeta(day_median(Amt), ·, 241),+0.32,valid +0.54)与共性表:day_median(Amt)(+1.95)、day_at_max_ratio(Vwap)(+1.71)、day_flat_run_max(Open)(+1.79)。即 alpha 更可能在成交额的典型水平和价格停留 / 封板结构里,而且是关系型慢变量。

事先预测:
- E1(核心 day_median(Amt),外围换成 中位 / 均值比、回归残差、相关、趋势、规模内去均值):出 head 概率约 30%;若出,最可能是 cross_regres / cross_regalpha 或规模内去均值的写法,因为慢、换手低,且 Pr1a 同核心已有 valid 为正。
- (E2 核心 day_at_max_ratio(Vwap) 因「恰好 2 个 GP 位」的检查被删,留给下一轮。)
- N(成交额基尼 / 时间重心):出 head 概率约 20%;若出,最可能是 cross_regres(day_gini(Amt), ...) 或 cs_bucket_demean 版本。
上一轮预测对不对:第 1 轮预测 E 与 N 大概率出不了 head(E 60% 不出、N 约 25% 出),实际 0 个 head,E 位审计未过变普通 GP,方向基本对。R 预计有变体好 0.1 以上也未出现(没有 R)。
