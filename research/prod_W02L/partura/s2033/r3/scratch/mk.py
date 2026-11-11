import yaml
R="sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)"
B=f"cs_bucket_demean({R}, LogFloatCap)"
C=f"cross_corr({B}, cross_delay({B}, 1), 241)"
P="cross_delay(day_close(Close), 1)"
P0="day_close(Close)"
pos=f"replace_small_with_nan(is_gt({C}, 0))"
def Cw(d): return f"cross_corr({B}, cross_delay({B}, 1), {d})"
E=[
 f"mul({C}, sub(1, cs_rank({P})))",
 f"add(cs_rank({C}), neg(cs_rank({P})))",
 f"mul({C}, sub(1, cs_rank(div({P0}, cross_delay({P0}, 241)))))",
 f"mul({C}, sub(1, cs_rank(div({P0}, cross_delay({P0}, 482)))))",
 f"mul({C}, sub(1, cs_rank(div({P0}, cross_max({P0}, 482)))))",
 f"mul({C}, cs_rank(sub(LogFloatShares, LogFloatCap)))",
 f"mul({C}, sub(1, cs_rank(cross_zscore({P0}, 482))))",
 f"div({C}, cs_rank({P}))",
 f"div(mul({C}, {pos}), {P})",
 f"mul({C}, cs_rank(div({P0}, cross_min({P0}, 482))))",
 f"cs_bucket_demean(div({C}, {P}), LogFloatCap)",
 f"div({C}, cross_mean({P0}, 482))",
 f"mul({C}, sub(1, cs_rank(cross_zscore({P0}, 241))))",
 f"add(cs_rank({C}), cs_rank(sub(LogFloatShares, LogFloatCap)))",
]
N=[
 f"inv({P0})",
 f"cs_bucket_demean(log({P0}), LogFloatCap)",
 f"div({P0}, cross_max({P0}, 482))",
 f"div({P0}, cross_min({P0}, 482))",
 f"sub(log({P0}), log(cross_mean({P0}, 241)))",
 f"div({P0}, cross_delay({P0}, 482))",
 f"cs_bucket_demean(div({P0}, cross_max({P0}, 482)), LogFloatCap)",
 "sub(LogFloatShares, LogFloatCap)",
 f"cross_zscore({P0}, 482)",
 f"cross_zscore({P0}, 241)",
 f"cs_bucket_demean(cross_zscore({P0}, 482), LogFloatCap)",
 f"add(cs_rank(log({P0})), cs_rank(sub(LogFloatShares, LogFloatCap)))",
 f"sub(cs_rank(log({P0})), cs_rank(sub(LogFloatShares, LogFloatCap)))",
 f"cross_corr({P0}, cross_delay({P0}, 20), 482)",
]
head=f"div({C}, {P})"
def head_with(c=C,p=P): return f"div({c}, {p})"
Rv=[
 head_with(Cw(160)), head_with(Cw(90)),
 head_with(Cw(120).replace("day_close(Close)","day_close(Vwap)"),P.replace("Close","Vwap")),
 head_with(C,"cross_delay(day_close(Close), 5)"),
 head_with(C,P0),
 head_with(C,"cross_mean(day_close(Close), 20)"),
 head_with(C,f"sqrt({P})"),
 head_with(C.replace("LogFloatCap","LogTotalCap")),
 f"cs_bucket_demean({head}, LogFloatCap)",
 f"mul({head}, {pos})",
 head_with(Cw(120),"cross_delay(day_close(Close), 5)"),
 head_with(Cw(200)),
]
hE=("机制:核心 C = 同市值十分位去均值后的日收益(后复权收盘到收盘)与其前一日值的 241 日滚动相关(同伴相对的一阶序列相关,正值 = 相对同伴有惯性)。"
"依据(只用 train / valid):第 2 轮 E 位的唯一 head +0.54(train +0.70 / valid +0.54)是 div(C, 前一日后复权收盘);拆解表里 C 单独只有 -0.20(train +0.08),除以前一日收盘一项就带来约 +0.74,把 Close 换成 Vwap 仍 +0.45,所以承重的是「C 的符号 × 后复权价位的尺度」这一交互,而不是 C 本身。"
"后复权收盘的水平 = 自基期以来的累计收益,低价位 = 长期输家(长周期反转,规则允许的已知读法),这个维度不在 5 个控制里(控制是流动性、波动、20 日反转、已知族、市值,另两个冠军信号)。"
"本轮 E 位把「除以价位」这一个外围换成别的实现,看机制到底是什么:(1) 用秩权重代替 1/P 的重尾尺度:C × (1 - cs_rank(P)),C ÷ cs_rank(P),秩和 cs_rank(C) - cs_rank(P),这样截面排序不再被价位的倒数支配;"
"(2) 平稳化的长期位置:用 1 年 / 2 年累计收益、距 2 年高点的比例、距 2 年低点的比例、482 / 241 日价位 z 分数的秩作权重(它们是「长期输家」的不同刻画,和 1/P 水平的相关性不是 1);"
"(3) 未复权价位:LogFloatShares - LogFloatCap = -log(未复权价),低价股(散户 / 彩票偏好)与后复权累计收益是两回事,用它做权重或秩和,检验承重的是累计收益还是低价;"
"(4) 只在 C > 0 的票里按 C / P 排(replace_small_with_nan(is_gt(C, 0))),因为尺度乘法使负 C 的票得分被价位拖到相反端,纯多头书只用头部;(5) 再按市值十分位去均值,把价位尺度与市值的残余暴露拿走。"
"与以前不同:第 2 轮见过的外围是 div(·, 前一日价位)、乘 day_at_min_ratio(Vwap)、嵌套的 C 自身,以及 C 外面的平滑 / 分桶后处理;本轮没有一个重复,权重全是秩 / 累计收益 / 未复权价位 / 掩码。"
"样本外还会在的理由:长周期输家 + 同伴相对惯性的组合源自 A 股散户对低价 / 深跌股的参与和反应不足,是行为偏差而非数值巧合;但 valid(+0.54)已弱于 train(+0.70),价位是否稳定是真问题,预测见笔记。")
hN=("机制:后复权收盘价的水平 = 自基期(2018 年或上市日)以来的累计收益,所以截面上它是一个超长周期(3 年以上)的动量 / 反转信号;第 2 轮 E 位 head(C / 前一日后复权收盘,+0.54)靠的就是除以这个水平(C 单独 -0.20),本流富集表里含 day_close(Close) 的 138 个候选均值 -1.29 对不含 -3.23(p 0.000),差 +1.94,是全表最强的共性子树。"
"5 个控制只有 20 日反转,没有 1 年以上的反转 / 价位,所以这一维可能还留有残差。本 N 位不再带 C,直接问:长周期位置本身(没有序列相关这一部分)有没有 alpha,以及哪种刻画最稳:"
"(a) 价位的倒数 / 对数;(b) 同市值十分位内的价位(cs_bucket_demean):去掉大盘股价位高的结构,留下同规模内的长期输家;(c) 距 2 年高点的比例(回撤深度)、距 2 年低点的比例;(d) 1 年 / 2 年累计收益与 482 / 241 日价位 z 分数,(e) 价位相对 1 年均值的偏离;(f) 未复权价 LogFloatShares - LogFloatCap(低价股)与后复权累计收益的秩和 / 秩差,把「低价」与「累计输家」拆开;(g) 价位与其 20 日滞后的 482 日相关(价位路径的平滑程度)。"
"算子:cross_max / cross_min / cross_delay / cross_mean / cross_zscore 沿日轴取窗口,cs_bucket_demean 去市值,cs_rank 取截面秩;全部只用当日及以前的数据。"
"为什么与库里不同:两个库的 5583 条里没有『后复权价位对自身 482 日极值 / 均值 / 滞后的比』这类长窗口价位位置(定位的富集表只显示 day_close(Close) 作为较大表达式的一个部件出现);快照 heads 全部是 C × 尺度或量额的回归。方向由奖励自动取最优(正负都可),所以不事先押多空。"
"样本外还会在的理由:A 股长周期反转 / 低价偏好来自散户结构与退市 / ST 约束下深跌股的定价,不是样本内数值巧合。风险:价位的倒数与市值 / 流动性控制相关(深跌小盘),尺子拿走线性 / U 形暴露后可能剩得很薄;窗口只有 482 日(约 2 年),起始 2018 年初的前两年为热身期,数值定义上由 cross_* 的最小样本处理,训练段前段会缺失但不影响 2020 年之后。")
doc={"seed":2033,"round":3,"slots":[
 {"type":"E","core":C,"hypothesis":hE,"seeds":E},
 {"type":"N","hypothesis":hN,"inspired_by":"本流第 3 批 B099(inv(day_last(Amt)) 的分位数 / 求和)与前两轮结果:富集表里 day_close(Close)(后复权价位)是最强共性子树(+1.94,p 0.000),第 2 轮 head C / 前一日收盘中除以价位贡献约 +0.74","seeds":N}],
 "R":[{"head":head,"why":"拆解表:去掉 cross_corr 为 -5.00(必要性 +5.54),去掉滞后为 -2.38;窗口 241→120 为 +0.43(train +0.89,valid +0.43),241→482 为 +0.35,Close→Vwap 为 +0.45,说明承重部件是 C 的符号与价位尺度的交互;烂的部件候选:窗口(241 日标准误大,120 / 90 / 160 是否更优)、分母的重尾尺度(未滞后 / 5 日滞后 / 平方根 / 20 日均值),以及对负 C 的票尺度反向。变体每个只改一处(两处:窗口 120 同时 Vwap / 5 日滞后)。","variants":Rv}]}
class D(yaml.SafeDumper):pass
open("missions.yaml","w").write(yaml.dump(doc,allow_unicode=True,width=10**6,Dumper=D,sort_keys=False))
