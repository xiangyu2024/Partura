import yaml
X="day_cov(Amt, cross_delta(Amt, 30))"
S=f"cross_stddev({X}, 60)"
C=f"ts_std({S}, 50)"
L=lambda e:f"log(add({e}, 1))"
KN="cross_mean(day_std(Amt), 30)"
LK=L(KN)
A2="cross_mean(day_cov(Amt, Amt), 241)"
E=[
 f"cs_regres({L(C)}, {LK})",
 f"cs_regres({L(C)}, {L(A2)})",
 f"cs_regres(cs_regres({L(C)}, {LK}), LogFloatCap)",
 f"cs_regres({L(C)}, add({LK}, LogFloatCap))",
 f"cs_bucket_zscore({C}, {KN})",
 f"cs_bucket_demean({L(C)}, {KN})",
 f"cs_bucket_rank({C}, LogFloatCap)",
 f"cs_bucket_rank({C}, {A2})",
 f"cs_bucket_demean({L(C)}, LogTotalCap)",
 f"ts_mean(cs_regres({L(C)}, {LK}), 20)",
 f"ts_mean(cs_bucket_demean({L(C)}, {KN}), 10)",
 f"cs_regres({L(C)}, log(add(cross_mean(day_mean(Amt), 30), 1)))",
 f"cs_regres(cs_winsor({L(C)}), {LK})",
 f"cs_regres({L(C)}, log(add(cross_stddev(day_mean(Amt), 60), 1)))",
 f"sub({L(C)}, mul({LK}, 0.5))",
 f"cs_robust_z(cs_regres({L(C)}, {LK}))",
]
V="cross_stddev(day_cov(Volume, cross_delta(Volume, 30)), 60)"
XR="day_cov(abs_(Ret), cross_delta(Amt, 30))"
XS="day_cov(Ret, cross_delta(Amt, 30))"
SR=f"cross_stddev({XR}, 60)"
SS=f"cross_stddev({XS}, 60)"
XH="day_cov(Amt, cross_delta(abs_(Ret), 30))"
N=[
 f"cs_regres({L('ts_std('+SR+', 50)')}, {LK})",
 f"cs_regres({L('ts_std('+SS+', 50)')}, {LK})",
 f"cs_bucket_rank(ts_std({SR}, 50), {KN})",
 f"cs_bucket_rank(ts_std({SS}, 50), {KN})",
 f"cs_regres({L('ts_std('+V+', 50)')}, log(add(cross_mean(day_std(Volume), 30), 1)))",
 f"cs_bucket_rank(ts_std({V}, 50), cross_mean(day_std(Volume), 30))",
 f"cs_regres({L('ts_std(cross_stddev('+XH+', 60), 50)')}, {LK})",
 f"ts_corr({SR}, {S}, 120)",
 f"ts_corr({SS}, {S}, 120)",
 f"ts_regbeta({L(SR)}, {L(S)}, 120)",
 f"cs_regres({L('ts_mean('+SR+', 50)')}, {L('ts_mean('+S+', 50)')})",
 f"cs_bucket_rank(ts_mean(abs_(ts_delta({L(SR)}, 5)), 100), {KN})",
 f"cs_regres(sub({L('ts_std('+SR+', 50)')}, {L('ts_std('+S+', 50)')}), {LK})",
 f"cs_bucket_zscore({L('ts_std('+SR+', 100)')}, LogFloatCap)",
]
S120="cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 120)"
S90="cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 90)"
S180="cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 180)"
Rv=[
 f"cs_regres({L('ts_std('+S120+', 30)')}, {LK})",
 f"cs_regres({L('ts_std('+S120+', 40)')}, {LK})",
 f"cs_regres({L('ts_std('+S120+', 20)')}, {LK})",
 f"cs_regres({L('ts_std('+S90+', 50)')}, {LK})",
 f"cs_regres({L('ts_std('+S180+', 50)')}, {LK})",
 f"cs_regres({L('ts_std('+S120+', 50)')}, {L(A2)})",
 f"cs_regres(cs_regres({L('ts_std('+S120+', 50)')}, {LK}), LogFloatCap)",
 f"cs_bucket_demean({L('ts_std('+S120+', 50)')}, {KN})",
 f"cs_bucket_zscore({L('ts_std('+S120+', 50)')}, {KN})",
 f"ts_mean(cs_regres({L('ts_std('+S120+', 50)')}, {LK}), 20)",
 f"cs_regres({L('ts_std('+S120+', 50)')}, add({LK}, log(add(cross_mean(day_mean(Amt), 30), 1))))",
 f"cs_regres({L('ts_std('+S120+', 60)')}, {LK})",
]
head=f"add(ts_quantile_q50({X}, 40), {C})"
hyE=("事实(上一轮读数,不是推测):head 1 = add(q50 水平项, C),C = ts_std(S, 50),S = cross_stddev(X, 60),X = day_cov(Amt, cross_delta(Amt, 30))(分钟成交额与其 30 分钟变化的日内协方差,即成交脉冲的聚集程度)。"
"第 2 轮 R 变体 cs_regres(log(1+ts_std(S120,50)), log(1+cross_mean(day_std(Amt),30))) 得分 +0.66(train +0.66 / valid +1.08),与已知族 rho -0.16、与 head 1 rho 0.14:"
"即把 C 的对数对已知族的对数做逐日截面回归取残差,是目前唯一同时有分数又去掉已知族暴露的写法;而第 1 轮 E 位在 C 外面做的是除以量级(div),最好只有 +0.31。"
"本位核心就是 C 本身(整个核心取自 head 1 的一个子树,整个实验第 2 个也是最后 1 个 E 位),外围全部换成『截面上的残差化 / 桶内去均值』这一类:"
"log(1+C) 对 log 已知族、对 Amt^2 的 241 日水平、对流通市值、对成交额日均值的波动取逐日回归残差,cs_bucket_demean / cs_bucket_zscore / cs_bucket_rank 在已知族十分位或市值十分位内取相对位置,"
"再叠 ts_mean 平滑、cs_winsor 去尾、cs_robust_z。第 1 轮用过的外围是 div(C, 量级) 一类,这里没有任何一个种子是除法,外围算子集合 {log, add, cs_regres}、{cs_bucket_*}、{ts_mean, cs_regres} 都是新的。"
"机制:C 度量成交脉冲结构的日间不稳定程度,与已知族共享 Amt^2 的量级;残差化后留下的是『在相同流动性水平上,成交脉冲结构更不稳定的票』,即同样的成交额水平下由事件 / 大单驱动、而不是整体放量驱动的票;这类票的关注度冲击会持续,按纯多头十分位书(10 日以内换手低,窗口 50 + 60)买入。"
"为什么样本外还会在:valid 一贯好于 train(R 读数 +1.08 对 +0.66),不是 train 里拟合出的形状;嵌套窗口 60 + 50,换手低,成本不是问题;来源是微观结构而不是行情。"
"数学检查:log 的输入一律 add(·,1) 后为正;cs_regres 在每日截面内回归,不涉及除以近零的量;cs_bucket_zscore 的桶内标准差带 EPS,桶内少于 2 只则为缺失;没有 ts_rank / cross_rank,不触发 nanrank_last;所有窗口只用当日及以前的数据。"
"如果它有 alpha,最可能来自 C 在已知族残差下的剩余部分,即『脉冲结构不稳定 vs 总体流动性』的差。")
hyN=("想法:把 B133 里的『成交额脉冲聚集度 S』的价格侧版本当信号。事实(本组读数):S = cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60) 在日间的波动(ts_std 外壳)是本组唯一出过分数的东西(+0.3 到 +0.9),"
"但它只看成交额自己的节奏;把成交额的 30 分钟变化与『同一分钟的价格变动』做日内协方差,读的是另一件事:放量加速时价格是否同向大幅变动(知情 / 事件冲击,价量同步),还是放量而价格不动(被动换手、对倒 / 做市)。"
"算子怎么实现:day_cov(abs_(Ret), cross_delta(Amt, 30)) = 分钟绝对收益与成交额加速度的日内协方差(无方向,波动-放量耦合),day_cov(Ret, cross_delta(Amt, 30)) = 带方向(放量上涨 vs 放量下跌);"
"cross_stddev(·, 60) 与 ts_std(·, 50) 与 S 同一套外壳,换手低;为了不再与已知族共享 Amt^2 的量级,一律对 log 已知族做逐日截面回归残差或桶内秩(cs_regres / cs_bucket_rank / cs_bucket_zscore),"
"另有 Volume 版(股数而不是金额,与以金额为尺度的流动性控制不同)、价量次序反过来(Amt 对 cross_delta(abs_(Ret), 30))、价格侧与成交额侧 S 的时间序列相关与对数弹性(ts_corr / ts_regbeta,尺度无关,取消量级)。"
"为什么和库里 / 已出 head 不同:库里 head 与本组所有种子都只在 Amt 与自身变化之间做协方差(day_cov(Amt, cross_delta(Amt, 30)));价格 / 收益对成交额加速度的日内协方差以及它的日间波动,在 B133 到 B135 批里没有一条(B134 / B135 的协方差都是 pow_2(nt_cs_rank(·)) 与价格自身的,含禁用算子,骨架也不同),骨架逐条由库禁令核对。"
"为什么样本外还会在:来源是微观结构(事件 / 知情交易的价量耦合日间不稳定性),换手低;分数有无取决于去掉已知族之后是否还剩东西,上一轮读数说有界底没有分数而残差写法有,所以种子都用残差 / 桶内秩而不是单独的相关。"
"数学检查:abs_(Ret) 与 Ret 是分钟收益,无除法;log 输入一律 add(·,1),但 day_cov(Ret, ·) 的 cross_stddev 非负,所以 add 1 后为正;ts_corr 的分母带 EPS;ts_regbeta 的 x 是对数水平,窗口 120 日,近常数风险有限;不用 ts_rank / cross_rank,没有 nanrank_last。"
"如果它有 alpha,最可能来自价格对成交额加速的响应强度不稳定的票(事件驱动型)。")
d={"seed":2045,"round":3,"slots":[
 {"type":"E","core":C,"hypothesis":hyE,"seeds":E},
 {"type":"N","hypothesis":hyN,"inspired_by":"B133(day_cov(Amt, cross_delta(Amt, 30)) 一族,Pr1a 的 S 外壳读数)与 B134 / B135 的 day_cov(价格相关量, 成交额变化量) 外壳","seeds":N}],
 "R":[{"head":head,"why":"烂部件:第 2 轮 R 读数里去掉已知族暴露的写法 cs_regres(log(1+ts_std(S120,50)), log(1+已知族)) 得 +0.66,而同一写法外层窗口放到 100 就掉到 -0.14,说明外层窗口 / S 窗口 / 回归对象都有调的空间;本组围绕这个赢家改外层窗口 20-60、S 窗口 90-180、回归对象(Amt^2 水平、市值、两者叠加)、桶内去均值 / zscore 代替回归,看哪部件是烂的。","variants":Rv}]}
class D(yaml.SafeDumper): pass
yaml.dump(d,open("../missions.yaml","w"),Dumper=D,allow_unicode=True,width=10000,sort_keys=False)
