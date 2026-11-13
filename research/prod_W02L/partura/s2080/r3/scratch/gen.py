import yaml
C1="cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40)"
C2="cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)"
D2="cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(neg(Ret)))), 10), 241)"
V2="cross_sum(ts_sum(day_var(Ret), 10), 241)"
LP="sub(LogFloatCap, LogFloatShares)"
e1=[f"ts_std({C1}, 25)",f"ts_std({C1}, 60)",f"sub({C1}, ts_mean({C1}, 120))",f"ts_rank({C1}, 120)",
f"sub(ts_max({C1}, 60), ts_min({C1}, 60))",f"div({C1}, ts_std({C1}, 60))",f"cross_zscore(ts_std({C1}, 20), 120)",
f"sub(cross_mean({C1}, 10), cross_mean({C1}, 60))",f"ts_skew({C1}, 60)",f"sub({C1}, ts_delay({C1}, 20))",
f"abs_(sub({C1}, ts_mean({C1}, 120)))",f"mul(sign({C1}), ts_std({C1}, 40))"]
e2=[f"sub(ts_std({C2}, 25), ts_std({D2}, 25))",f"div({C2}, {D2})",f"sub({C2}, {D2})",f"ts_rank({C2}, 120)",
f"sub({C2}, ts_mean({C2}, 120))",f"cross_zscore(ts_std({C2}, 25), 120)",f"div(ts_std({C2}, 25), ts_mean({C2}, 25))",
f"ts_skew({C2}, 50)",f"sub(ts_max({C2}, 60), ts_min({C2}, 60))",f"ts_corr({C2}, {V2}, 60)",
f"div({C2}, {V2})",f"sub(ts_std({C2}, 25), ts_std({V2}, 25))"]
n=[LP,f"cross_zscore({LP}, 60)",f"mul({LP}, cross_mean(day_max(Ret), 20))",f"sub({LP}, cross_mean({LP}, 120))",
f"cs_bucket_rank({LP}, LogFloatCap)",f"cs_bucket_rank(cross_mean(day_max(Ret), 20), {LP})",
f"sub(cs_robust_z({LP}), cs_robust_z(cross_mean(day_std(Ret), 60)))",
"mul(cs_robust_z(LogFloatShares), cs_robust_z(cross_mean(day_sum(Ret), 20)))",
f"cross_mean(cs_bucket_rank(day_mean(Amt), {LP}), 20)",f"cross_mean(cs_bucket_rank(day_sum(Ret), {LP}), 20)"]
H1="机制:核心 C1 = cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40),即 40 日滚动里「分钟收益一阶自相关」对「分钟成交量成团程度(Q 统计量)」的回归斜率:成交成团的日子里价格是延续(知情拆单,正斜率)还是反弹(做市商库存回补 / 买卖价差反弹,负斜率),是订单流持续性的慢变读数(Hasbrouck 式冲击持续性)。依据:本批富集表里含 C1 的 8 个候选均值差 +1.09(p 0.002)、含 / 不含 -1.26 / -2.36,是批内最显著的两变量结构,且是此前没作过核心的(第 1 轮 E 是 day_q_stat_std(Volume) 单量,第 2 轮 E 是 ts_cov 量价核心)。快照里含 C1 的外围只有:直接用、cs_winsor 包一层、cross_delay 滞后 60 日(N 位 Pr1b);没有一个外围读它的变化或离散度。本轮外围换成对 C1 序列本身的二阶读法:(a) ts_std(C1, 25/60),即持续性本身的不稳定度(本库 head 的共同外围正是 ts_std / ts_var 这类对慢变量取波动,但都套在价格或成交额上,从没套在订单流持续性上);(b) C1 减自己 120 日均值 / ts_rank / 减 20 日前的值,即相对自己常态的持续性变化,去掉让水平控制起作用的持久截面差;(c) 极差、偏度、绝对偏离,读持续性的极端程度而非方向。为什么和库里不同:这些外围算子是 ts_std / ts_rank / ts_skew / ts_max-ts_min / ts_delay 与 sub / div,与 Pr1b 的 cs_winsor / cross_delay 外围、与库里 ts_quantile / ts_kurt 外围都不是同一个算子集合,骨架由 c06_check 与库禁令把关;读的东西(持续性的离散度与变化)也不是水平。为什么样本外还会在:订单流持续性由参与者构成(算法执行 vs 零散散户)决定,是慢变属性,40 日窗口外再加 25-120 日的二阶窗口,换手低,15 bp 下不被吃掉;符号由奖励选。最可能的失败:Q 统计量近常数(停牌、零成交日)时回归斜率被噪声主导,或与波动控制相关。数学检查:cross_regbeta 有效对不足时只影响新股与停牌多的票,可交易掩码已排除;ts_std 25 之后热身期约 65 日,不主导;全部只用 t 日及以前数据,无前视(无 cross_shift / ts_shift / in_local_mean);不含 ts_spearman 与 nt_*。"
H2="机制:核心 C2 = cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241),即 Ret 的 6.25 次幂(pow_2_5 对负数返回缺失,所以只保留上涨分钟并放大尾部)在日内的方差,10 日累加再做 241 日滚动和:过去一年里上行极端分钟的分散度,是彩票型 / MAX 型暴露(Bali-Cakici-Whitelaw 2011)的分钟级版本。依据:本批第一个 head ts_std(neg(neg(C2)), 25) 是批内唯一 valid 为正(+0.56)的 head,train -0.37;拆解里 C2 自身 sufficiency 为 -0.25(valid +0.03),窗口 25->50 变差,说明 C2 带信息,外围 ts_std 25 读的是它的波动。但 head 对 C2 只有一种处理(ts_std 外围,neg(neg()) 是空操作)。本位把 C2 与它的下行对应物 D(同样写法但对 neg(Ret) 取幂,只保留下跌分钟)配对,读上行尾部相对下行尾部的不对称:sub(C2, D)、div(C2, D)、sub(ts_std(C2,25), ts_std(D,25));并用全收益方差 V = cross_sum(ts_sum(day_var(Ret), 10), 241) 归一化,读方差里由上行极端贡献的份额 div(C2, V),去掉总波动水平(波动控制会吃掉水平读法);另有对 C2 自身的二阶读法:ts_rank、减 120 日均值、ts_skew、极差、变异系数。为什么和库里不同:快照里含 C2 的外围只有 ts_std(neg(neg(·)), 25/50) 及其去 ts_sum / 缩窗口的 R 变体,没有一个含下行对应物、总方差归一化或 ts_rank / ts_skew 外围;不对称读法引入了新的字段处理(neg(Ret))。为什么样本外还会在:极端上涨彩票偏好(散户追逐 MAX)是稳定的行为现象,A 股散户占比高,不对称份额比水平更不易被波动控制吃掉;241 日窗口使换手低。最可能的失败:C2 与波动 / 流动性控制高相关、残差后无剩余。数学检查:pow_2_5 对负数缺失是已知行为(规则 §4),这里把它当作显式的只留上涨分钟,并对 neg(Ret) 配对地取下行,不是漏洞;day_var 只在有效分钟 <2 时缺失;全部无前视;不含 ts_spearman 与 nt_*。"
H3="机制:名义股价(不复权的流通价格水平)。日频字段 LogFloatCap 减 LogFloatShares = log(流通市值/流通股数) = log 名义价格。控制里有 LogFloatCap(及其平方立方),但同一市值内名义价格差别很大:低价股偏彩票偏好、散户占比高,高价股偏机构;A 股的低价效应(名义价格错觉,Birru-Wang 2016:投资者把低名义价格股看作更有上行空间)独立于市值。算子实现:sub(LogFloatCap, LogFloatShares) 直接得名义价格水平;cs_bucket_rank(·, LogFloatCap) 给同一市值十分位内的名义价格排名,即对市值中性的名义价格,避开控制;再做相互作用:名义价格 x 近 20 日最大日内收益(彩票需求)、名义价格桶内的近期收益 / 成交额排名,读低价股里哪些在被追。启发于本批:共性表里最显著的单项之一是 cs_robust_z(LogFloatShares)(20 个候选,含 / 不含 -1.49 / -2.39,均值差 +0.89,p 0.000),说明股数这个静态量在本批最有信息,而它与市值控制并不重合;本流此前 4 个任务位没有一个用过日频字段叶子。为什么和库里不同:库里 5583 条表达式几乎都是分钟聚合,名义价格(两字段之差)作为核心结构未出现过,骨架由 c06_check 与库禁令核对;不等于任何控制(流动性 = 成交额水平,市值 = LogFloatCap 本身)。为什么样本外还会在:名义价格静态、换手近零,低价偏好是行为偏差、散户占比不变,15 bp 下几乎无成本;最可能的失败:仙股 / ST 股的风险使其被波动或流动性控制吃掉,或市值非线性暴露残余。数学检查:两个字段是日频,停牌日也有值,无热身缺失;差是 log 比,无除近零;cs_robust_z 的 MAD 非零;无前视;不含 ts_spearman 与 nt_*。"
IN="共性表 cs_robust_z(LogFloatShares)(20 个候选,均值差 +0.89,p 0.000)说明股数这一静态量最有信息;控制只含 LogFloatCap,名义价格(LogFloatCap 减 LogFloatShares)未被控制"
RH="ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 25)"
doc={"seed":2080,"round":3,"slots":[
{"type":"E","core":C1,"hypothesis":H1,"seeds":e1},
{"type":"E","core":C2,"hypothesis":H2,"seeds":e2},
{"type":"N","hypothesis":H3,"inspired_by":IN,"seeds":n}],
"R":[{"head":RH,"why":"该头(valid +0.56,train -0.37)的 neg(neg()) 是空操作,上一轮已把窗口缩到 25 并替换;余下的烂部件是 pow_2_5 只留上涨分钟(下行信息被扔掉)和 241 日滚动和偏长、ts_sum 10 的重叠平滑。试换成保号的 signedpower、缩短 241、换成 ts_mean 外围,依据拆解里窗口 25->50 变差、knockout neg 不变。",
"variants":[
"ts_std(cross_sum(ts_sum(day_var(signedpower(Ret, 2.5)), 10), 241), 25)",
"ts_std(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 241), 25)",
"ts_std(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 120), 25)",
"ts_std(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 120), 40)",
"ts_std(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(neg(Ret)))), 10), 241), 25)",
"ts_std(sub(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241), cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(neg(Ret)))), 10), 241)), 25)",
"ts_std(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 5), 241), 15)",
"ts_mean(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241), 25)"]}]}
open('missions.yaml','w').write(yaml.safe_dump(doc,allow_unicode=True,width=100000,sort_keys=False))
