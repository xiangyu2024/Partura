import yaml
K="ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30)"
R="in_slice(Ret, 11, 230)"
F="cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60)"
IL="inv(day_quantile_q25(Volume))"
e=[
 f"cross_ema({K}, 20)",
 f"cross_ema(cross_zscore({K}, 60), 20)",
 f"ts_mean({K}, 80)",
 f"ts_decay_linear({K}, 40)",
 f"sub({K}, ts_mean({K}, 60))",
 f"div({K}, add(ts_stddev({K}, 60), 0.000001))",
 f"cs_bucket_rank(LogFloatShares, ts_mean({K}, 20))",
 f"cs_bucket_rank(BoardCode, ts_mean({K}, 40))",
 f"cs_regres(ts_mean({K}, 40), day_std({R}))",
 f"cross_regbeta({K}, day_mean({R}), 120)",
 f"cross_corr({K}, day_std({R}), 120)",
 f"sub(ts_mean({K}, 20), ts_mean({K}, 120))",
 f"ts_mean(signedpower({K}, 0.5), 40)",
 f"cross_ema(cs_regres({K}, LogFloatCap), 20)",
 f"ts_mean(mul({K}, day_flat_ratio(Open)), 40)",
 f"cross_ema(ts_stddev({K}, 30), 20)",
]
n=[
 "cross_reg_tvalue(ListAge, day_flat_run_max(Close), 60)",
 f"cross_reg_tvalue(ListAge, {IL}, 60)",
 "cross_regbeta(ListAge, day_flat_run_max(Open), 120)",
 f"cross_reg_fvalue(ListAge, day_std({R}), 60)",
 f"cross_reg_fvalue(ListAge, day_gini(in_slice(Volume, 11, 230)), 60)",
 "ts_mean(cross_reg_tvalue(ListAge, day_flat_ratio(Open), 60), 20)",
 "cross_corr(ListAge, day_flat_run_max(Open), 60)",
 "sub(cross_reg_tvalue(ListAge, day_flat_run_max(Open), 60), cross_reg_tvalue(ListAge, day_flat_run_max(Open), 250))",
 f"cross_reg_tvalue(day_flat_run_max(Open), {IL}, 60)",
 f"cross_reg_fvalue(day_flat_run_max(Open), day_std({R}), 60)",
 f"cross_regbeta(ListAge, {IL}, 120)",
 f"cross_ema(cross_reg_tvalue(ListAge, day_flat_run_max(Amt), 60), 20)",
]
hE=("机制:核心 K = ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30)。"
"day_flat_run_max(Open) 是当日开盘价序列中最长的「价格不动」连续段占比(僵价 / 一字板 / 极薄票);ListAge 是每天 +1 的上市天数,cross_reg_fvalue(ListAge, ·, 60) 是对时间的 60 日回归 F 值,即「僵价程度在近 60 日是否出现显著趋势」;inv(day_quantile_q25(Volume)) 是下四分位分钟成交量的倒数,即最冷清分钟的非流动性。K 是这两条日度序列 30 日的协方差:非流动性上升的同时僵价趋势增强的票(逐步被市场遗忘 / 进入冷门状态),反向的是被重新发现的票。"
"本组前两轮在含 K 的候选里最好的成绩是 train -0.18 / valid +0.11(本组所有快照中最好),说明 K 是真有信息的部件,以前的外围只是 ts_mean(K,40)、对 K 自身再套 cov / fvalue 的嵌套。"
"本任务换掉外围,写成不同的机制:(a)慢状态与截面标准化(cross_ema、cross_zscore 后 EMA、ts_mean 80、线性衰减);(b)偏离自身慢均值、短减长(去掉水平留变化);(c)除以自身波动(信噪比);(d)板块 / 规模内排名(cs_bucket_rank 以 BoardCode、LogFloatShares 分组,A 股涨跌停宽度不同,僵价含义不同,组内比较去掉制度差异);(e)对分钟波动 / 市值做截面残差,以及对日均收益、波动做 120 日滚动斜率 / 相关(K 对状态的敏感度,承接第 1 轮「回归斜率最好」的教训);(f)符号幂变换后再平均、乘以僵价占比、K 的波动。"
"为什么样本外还会在:冷门化 / 僵价趋势是关注度与流动性供给的慢变量,A 股关注度驱动的散户交易使被遗忘的票长期被低估或高估,慢变量半衰期长,换手低,扣 15bp 后仍可存活;尺子已去掉流动性、波动、市值与两个冠军的线性与非线性暴露,剩下的是僵价趋势与流动性的联动。风险:停牌日僵价占比为缺失,ListAge 对新股偏短,cov 的量纲随波动变化。")
hN=("机制:把「对上市天数(时间)的滚动回归」当作一个通用的『趋势显著性 / 斜率 / 相关』算子,作用在微观结构状态量上,读的是状态量近 60~250 日是否在系统性地变坏或变好,而不是状态量的水平或离散度。库里的 4206+1392 条在 cross_reg_fvalue(ListAge, 僵价占比) 这种 F 值上有一批嵌套写法(第 2 轮最好 valid +0.11),但没有 t 值(带符号:趋势方向,F 值把方向丢了)、没有斜率(量纲化趋势)、没有时间相关、没有换成别的状态量(波动、成交量集中度、非线性流动性、收盘价僵价)的版本,也没有 250 日对 60 日的趋势差(趋势的变化)。"
"算子实现:cross_reg_tvalue(ListAge, y, 60) = 对 y 做 y ~ α + β·ListAge 的 60 日滚动回归的 t 值,符号 = 趋势方向;cross_regbeta 给斜率;cross_corr(ListAge, y, 60) 给秩无关的趋势相关;cross_reg_tvalue(僵价占比, 非流动性, 60) 把自变量换成僵价占比,读的是非流动性对僵价的敏感度。与库的区别:F 值是 t 值的平方,丢了符号,而『变坏』与『变好』对未来收益方向相反,t 值与斜率保留了这个方向;这是不同的数学对象,不是 F 的换写。"
"为什么样本外还会在:状态量的方向性趋势代表流动性 / 关注度的再配置(Amihud 流动性溢价的时间变化、被遗忘的票的低关注度溢价),A 股散户关注度与僵价的慢变化是持续的行为特征;趋势类读数是 60 日以上的慢变量,低换手,适合扣 15bp 后的纯多头。尺子去掉对流动性、波动的线性 / 非线性暴露,剩下方向。风险:时间回归对共同的上市年龄效应(新股)敏感,新股僵价与普遍规律相反;t 值有 1/√60 级别的抽样噪声。")
d={'seed':2027,'round':3,'slots':[
 {'type':'E','core':K,'hypothesis':hE,'seeds':e},
 {'type':'N','hypothesis':hN,'inspired_by':'第 3 个结构批 B081 与第 2 轮 N 位结果:含 cross_reg_fvalue(ListAge, day_flat_run_max(·), 60) 与 inv(day_quantile_q25(Volume)) 的候选均值差 +1.1~+1.7(p≤0.001),Pr2b 里 ts_mean(ts_cov(inv(q25 Volume), cross_reg_fvalue(ListAge, day_flat_run_max(Amt),60),30),40) train -0.18 / valid +0.11,是本组最好;现象是「僵价对时间的趋势」承重',
  'seeds':n}]}
yaml.safe_dump(d,open('missions.yaml','w'),allow_unicode=True,width=200,sort_keys=False)
