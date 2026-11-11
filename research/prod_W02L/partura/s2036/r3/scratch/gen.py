import yaml
D="div(day_last(Close), cross_max(day_last(Close), 241))"
C2="cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241)))"
V60="cross_mean(day_std(Ret), 60)"
R20="cross_mean(day_sum(Ret), 20)"
A60="cross_mean(day_sum(Amt), 60)"
e1=[f"cs_bucket_rank({R20}, {D})",
f"cs_bucket_zscore({V60}, {D})",
f"cs_bucket_rank({A60}, {D})",
f"cs_bucket_demean({D}, {V60})",
f"cs_flip_by_state({D}, day_sum(Ret))",
f"cs_flip_by_state({D}, day_std(Ret))",
f"cross_ema({D}, 20)",
f"sub(cs_rank({D}), cs_rank(cross_delay({D}, 20)))",
f"mul(cs_rank({D}), cs_rank({V60}))",
f"cs_first_low20(cross_semistd_neg(day_sum(Ret), 60), {D})",
f"cs_first_low20(cross_mean(day_zero_ratio(Ret), 60), {D})",
f"cs_first_low20(cross_mean(day_gini(Amt), 60), {D})",
f"cs_first_low20(cross_mean(day_centroid(Volume), 60), {D})",
f"cs_last_low20(cs_rank({D}), {A60})",
f"cs_regres({D}, {V60})",
f"cross_regbeta({R20}, {D}, 120)"]
e2=[f"cross_ema({C2}, 10)",
f"cs_flip_by_state({C2}, day_sum(Ret))",
f"cs_bucket_zscore({C2}, LogFloatCap)",
f"cs_bucket_rank({C2}, {V60})",
f"cs_first_low40({C2}, ListAge)",
f"cs_last_high20({C2}, {V60})",
f"cs_last_low20({C2}, {A60})",
f"cs_first_low40({C2}, cross_mean(day_zero_ratio(Ret), 60))",
f"cross_mean({C2}, 5)",
f"cs_regres({C2}, {V60})",
f"sub(cs_rank({C2}), cs_rank({A60}))",
f"add(cs_rank({C2}), cs_rank(cross_delta({A60}, 60)))",
f"mul(cs_rank({C2}), cs_rank({V60}))",
f"cs_flip_by_state({C2}, day_std(Ret))",
f"cs_bucket_demean({C2}, {A60})",
f"cs_first_low40({C2}, cross_semistd_neg(day_sum(Ret), 60))"]
h1=("核心 D = div(day_last(Close), cross_max(day_last(Close), 241)):收盘价相对自己 241 日最高价的位置(52 周高点锚定;深度回撤的票 D 小)。依据:第 2 轮 N 位里以 D 为段变量的 cs_first_low20(y, D) 写法 GP 评分 97 个,前五名 +0.37~+0.46,train 与 valid 同号(valid +0.44~+0.86),是本流目前唯一两段都为正的线索,但全都是『先取 D 最低 20% 段,段内按 y 排』这一种外围,没有过 0.5。这一轮在 D 外面换结构,不再只试 cs_first_low20:(1) 条件中性化——cs_bucket_rank / cs_bucket_zscore(y, D) 在 D 的十分位内给 y 排序,整个截面都参与而不是只取 20%,问的是『每个回撤档位内谁最被错杀』;反向 cs_bucket_demean(D, 波动) 问『同波动档里谁离高点最远』,去掉 D 里的高波动成分(波动越大天然离高点越远);(2) 市场状态——cs_flip_by_state(D, 全市场 20 日收益/波动):回撤效应在市场高位与低位的符号可能相反(处置效应在熊市里最强),用状态翻转检验,若只是失效则翻转版明显更差,这本身是读数;(3) 时间结构——cross_ema 平滑 D、秩差 rank(D)-rank(D 的 20 日前值)、cross_delta,问『回撤正在加深 / 正在修复』的动量,而不是水平;(4) 段内排序变量换成第 2 轮没试过的:下行半标准差(cross_semistd_neg)、零收益分钟占比(day_zero_ratio,流动性/停滞)、成交额基尼(day_gini,成交团块度,与本流第 1 轮的 energy_ratio 成团度想法同源但用在价格位置条件下)、成交量重心(day_centroid,量集中在早盘还是尾盘);(5) 乘积交互 mul(rank(D), rank(波动)) 与 cs_regres(D, 波动)。与库的差别:库里含 D 的成员(共性表里 20 个)只是 D 本身或 cross_mean 平滑的组合与 cs_first_low20 的二元写法;两库 5583 条骨架里没有 bucket_rank(·, D)、flip_by_state(D, ·)、D 的 delay 秩差、day_gini / day_zero_ratio 作段内变量这些。机制:52 周高点锚定与处置效应——持有者对回撤中的票不愿止损,价格对坏消息反应不足,回撤档越深、条件变量越能分辨『继续下跌的』与『被错杀的』。为什么样本外还会在:行为金融的慢变量(D 一年内缓变,换手低,15 bp 成本下保得住),且是跨市场的结果;第 2 轮 valid 比 train 更强,说明不依赖某一段行情。数学:D 的分母为正价格,D 在 (0,1],无爆点;cross_delay / cross_ema 窗口因果;cs_flip_by_state 无状态时输出 NaN 而非 0;热身 241 日占样本前部,不主导结果;无前视,t+1 交易。")
h2=("核心 C2 = cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241))):共性表里的现成子树(含它的候选 6 个,均值差 +1.17,p 0.025),第 2 轮里它的变体是 N 位里的头名之一(同型 +0.37~+0.46,valid +0.37~+0.45):把 20 日均价相对 241 日高点最低的 20% 段整体放前面,段内按 20 日累计收益(反转)排,即『深度回撤段里近期跌得最多的反弹』。这个核心已经是一个完整的信号,本轮在它外面做和以前不同的处理——此前含它的候选外围只有 cross_mean 平滑 / 换窗口 / 换段内变量这类:(1) 再套一层条件——cs_first_low40(C2, ListAge)(只在较新上市的票里交易这个信号)、cs_last_high20(C2, 波动)(把高波动票压到最底,问信号是不是靠最高波动的彩票股撑着)、cs_last_low20(C2, 60 日成交额)(把最不活跃的压到最底,检验容量约束);cs_first_low40(C2, 零收益占比 / 下行半标准差),问信号在『可交易 / 低停滞』子集里是不是更干净;(2) 中性化——cs_bucket_zscore(C2, LogFloatCap)、cs_bucket_rank(C2, 波动)、cs_bucket_demean(C2, 成交额)、cs_regres(C2, 波动),直接去掉核心对市值 / 波动 / 流动性的暴露(尺子只去 1~3 次项,这里是桶内去除);(3) 市场状态翻转——cs_flip_by_state(C2, 全市场收益 / 波动);(4) 与另一条腿组合——rank(C2) 减 / 加 60 日成交额秩或其 60 日变化秩,mul(rank(C2), rank(波动))。(5) 快 / 慢平滑 cross_ema(C2, 10)、cross_mean(C2, 5)(段边界处的并列换手大,平滑可能是主要增益来源)。与库的差别:两库里没有 C2 外面再套桶中性化、再套第二层 lexicographic 过滤、或状态翻转的表达式;骨架都是新的。机制:同 D——锚定与处置效应加上深度回撤中的短期反转;新外围把『信号在哪类票里真正成立』拆开。为什么样本外还会在:行为金融慢变量 + 反转的流动性补偿,是长期存在的现象,段成员缓变。数学:分母为正价格;cs_first_low20 的结果无并列;cs_first_low40(C2, ·) 里 C2 的值域为排名型,嵌套没有溢出;无前视。")
d={"seed":2036,"round":3,"slots":[
{"type":"E","core":D,"hypothesis":h1,"seeds":e1},
{"type":"E","core":C2,"hypothesis":h2,"seeds":e2}]}
for s in d["slots"]:
    for x in s["seeds"]: assert s["core"] in x, x
yaml.safe_dump(d,open("../missions.yaml","w"),allow_unicode=True,width=1000,sort_keys=False)
