# -*- coding: utf-8 -*-
import yaml
R = "sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1)"
H = "day_hurst(Low)"
E = [
    f"cross_mean({H}, 60)",
    f"cross_zscore({H}, 120)",
    f"cross_corr({H}, {R}, 60)",
    f"cross_mean(mul({H}, sign({R})), 60)",
    f"sub(cross_mean({H}, 20), cross_mean({H}, 241))",
    f"cross_quantile({H}, 0.9, 60)",
    f"cross_max(sub({H}, day_hurst(High)), 60)",
    f"cross_mean(sub({H}, day_hurst(High)), 120)",
    f"cross_tail_mean_q75({H}, 120)",
    f"cs_regres(cross_max({H}, 60), cross_mean(day_std(Ret), 60))",
    f"cs_bucket_zscore(cross_max({H}, 60), LogFloatCap)",
    f"div(cross_max({H}, 60), cross_mean(day_hurst(Close), 60))",
    f"ts_regbeta({H}, {R}, 60)",
    f"cross_ema({H}, 60)",
    f"cs_last_low10(cross_max({H}, 60), ListAge)",
    f"cross_mean(mul({H}, day_pos_ratio(Volume)), 60)",
]
N = [
    "sub(cross_mean(day_hurst(Close), 60), cross_hurst(day_last(Close), 60))",
    "cross_hurst(day_last(Close), 120)",
    f"cross_hurst({R}, 120)",
    "cross_hurst(day_mean(Ret), 120)",
    "cross_hurst(day_std(Ret), 120)",
    "cross_hurst(day_gini(Amt), 120)",
    "cross_hurst(day_centroid(Amt), 120)",
    "cross_hurst(day_signed_ratio(Ret, Amt), 120)",
    "cross_hurst(day_topw_mean(Ret, Amt), 120)",
    "cross_hurst(day_pos_ratio(Volume), 120)",
    f"cross_hurst({H}, 120)",
    f"sub(cross_hurst({R}, 120), cross_hurst(day_std(Ret), 120))",
    f"cs_bucket_zscore(cross_hurst({R}, 120), LogFloatCap)",
    "cross_hurst(day_flat_ratio(Close), 120)",
    "cross_hurst(day_skew(Ret), 120)",
    "cross_hurst(day_last(Close), 241)",
]
Rv = [
    {"head": "pow_2(ts_max(day_hurst(Low), 30))",
     "why": "拆解显示 ts_max 窗口 30->60 使 score 从 -1.17 升到 +0.10(train 与 valid 都改善),说明 30 日窗口太短、被噪声吃掉;沿窗口方向继续拉长,并换 High/Close 价路径与分位数读法,检验 hurst 的慢极值是否是来源。",
     "variants": ["pow_2(ts_max(day_hurst(Low), 60))", "pow_2(ts_max(day_hurst(Low), 90))", "pow_2(ts_max(day_hurst(Low), 120))", "pow_2(ts_max(day_hurst(Low), 241))", "pow_2(ts_max(day_hurst(Close), 120))", "pow_2(ts_max(day_hurst(High), 90))", "ts_max(day_hurst(Low), 90)", "pow_2(cross_quantile(day_hurst(Low), 0.9, 90))"]},
    {"head": "ts_max(day_hurst(Vwap), 50)",
     "why": "拆解显示 Vwap->Close 使 score 从 -1.54 到 -0.03(两段持平),窗口 100 比 25 好;烂的部件是 Vwap(成交加权引入噪声)与短窗口,所以换 Close/Open 并继续拉长窗口。",
     "variants": ["ts_max(day_hurst(Close), 100)", "ts_max(day_hurst(Close), 120)", "ts_max(day_hurst(Close), 241)", "ts_max(day_hurst(Open), 100)", "cross_quantile(day_hurst(Close), 0.9, 100)", "cross_mean(day_hurst(Close), 100)"]},
]
E_HYP = ("机制。核心 day_hurst(Low) = 当天约 241 根分钟 Low 价格序列的 R/S Hurst 指数(累计偏离均值的极差 / 标准差,取 log 再除以 log 241):衡量当日价格路径是单边漂移的趋势日(值高)还是围绕均值来回震荡(值低)。它是尺度无关的日内形状量(价格水平与波动大小被 S 除掉),不含成交额,也不含价格水平的排序信息。"
         "本流证据(只用 train/valid):R 拆解里 pow_2(ts_max(day_hurst(Low),30)) 把窗口 30 改 60 得 score +0.10(train +0.10 / valid +0.30),ts_max(day_hurst(Vwap),50) 换 Close 为 -0.03(train -0.03 / valid +0.17),是本种子全部评分里最接近 0 的几条;说明慢窗口的 hurst 极值带有一点信息,短窗口被噪声吃掉。"
         "解释:一只票在近 60~120 日内出现过的趋势日,代表机构拆单持续推动(知情资金逐步推进)留下的日内足迹,而不是散户的来回震荡;这是 Kyle 式价格冲击 / 订单流持续性(Barclay-Warner 隐形交易、Chordia-Subrahmanyam 订单流自相关)的日内形状版本。"
         "本轮外围不再只用 ts_max 取极值,而是五类很不同的处理:(1) 慢均值 / EMA / 上四分位 / 分位数(cross_mean、cross_ema、cross_tail_mean_q75、cross_quantile),把极值换成稳健的趋势日倾向;(2) 相对自己的历史(cross_zscore、20 日减 241 日),近期趋势日异常增多;(3) 与价格新闻耦合(与日收益的 60 日相关 / 回归斜率、乘当日收益符号),趋势日方向是否与收益同向,把 hurst 变成有方向的持续性;(4) 路径不对称(Low 的 hurst 减 High 的 hurst),下沿路径比上沿路径更趋势意味着低点被持续抬高(被动吸筹)还是持续压低;(5) 去掉别的来源与分段(对 60 日波动回归残差、市值十分位内标准化、新上市最低 10% 筛子、与成交量上涨占比相乘)。"
         "与库里不同:库里 day_hurst 全部只出现在 ts_max / pow_2 / cross_med 极值链里,两个库 5583 条表达式里没有 cross_zscore / cross_ema / cross_tail_mean_* / cs_bucket_* / cs_last_* / ListAge / LogFloatCap,也没有 day_hurst 与收益的耦合或 Low-High 差;骨架不同,日度秩也应与库 head 的极值读数明显不同(平均而不是极值,方向耦合)。"
         "样本外还会在的理由:读数来自日内形状而非价格水平,不受后复权价格序累计收益的吸收;窗口 60~241 日,日换手低,15bp 成本不是主要损耗;与两个 Amt 水平族冠军不同源。"
         "数学检查:无前视(只用当日分钟,t+1 交易);day_hurst 在 S<1e-9(全天价平,如一字板)时返回缺失而不是 inf,这些票当天缺失;种子里唯一的除法是 div(cross_max(H,60), cross_mean(day_hurst(Close),60)),分母是 hurst 的均值(量级 0.3~1,不近零);cross_corr 在窗口内一方不变时缺失;不使用 ts_rank / cross_rank / in_rank_rolling,nanrank_last 陷阱不涉及;窗口 ≤ 241,热身期不主导。风险:hurst 与日内波动 / 反转有共线(种子 10 用回归残差对冲);一字板多的票读数缺失。")
N_HYP = ("机制。把 Hurst 指数从单日分钟路径搬到日频序列:cross_hurst(X, d) 是 X 在过去 d 个交易日里的 R/S Hurst 指数(累计偏离的极差 / 标准差),衡量一个日度属性的长记忆 / 持续性(>0.5 持续、<0.5 回复),无量纲、被标准差归一,因此与价格水平、成交额水平、波动水平这些已被控制与冠军吸掉的通道不同源。"
         "库里的 day_hurst 只作用在分钟路径(单日,被 ts_max / cross_med 极值链处理),没有对日度序列使用 cross_hurst;这是库里没有的结构。想法来自本批(B048,day_hurst(F) 一族)的现象:同样是 R/S 量,日内路径上慢极值读法在 0 附近、其余读法在噪声带,说明可检验的是持续性这个形状而不是水平;在日度序列上做同一度量,就是把这只票的走势 / 资金行为是否有记忆直接量出来。"
         "16 个种子是同一想法的不同被测对象:(1) 价格路径的持续性,收盘价自身的 120 / 241 日 Hurst(趋势平滑度)与日收益的 Hurst(收益长记忆,动量 / 反转机制的指示);(2) 日度收益均值、波动 day_std(Ret)(波动聚集长记忆)、偏度的 Hurst;(3) 资金行为的持续性,成交额重心、成交额基尼、成交额加权符号占比、大额分钟偏置、成交量上涨占比的 Hurst;(4) 日内 hurst 的 Hurst(跨尺度一致);(5) 日内 Hurst 与日频 Hurst 之差;(6) 收益 Hurst 减波动 Hurst(去掉波动持续性);(7) 市值十分位内标准化。"
         "文献:Mandelbrot R/S 分析、Peters 分形市场假说、Cajueiro-Tabak 用 Hurst 度量市场效率、Hong-Stein 信息逐步扩散(慢消化导致收益持续)。"
         "样本外还会在的理由:一只股票的信息消化速度 / 持有人结构是慢变的结构特征,窗口 120~241 日,日换手低(15bp 成本不是主因),且量的是持续性而非水平,与控制(流动性、波动、20 日反转、成交额族、市值)和两个冠军的水平通道不同源。"
         "数学检查:无前视(cross_hurst 只用 t 日及以前的日度值);R/S 的分母是窗口标准差,S<1e-9 时返回缺失而不是 inf(已核对 dt_cross.cross_hurst),没有除零爆点;day_flat_ratio(Close)、day_pos_ratio(Volume) 等有界序列的窗口标准差不会近零(一字板多的票会缺失);cross_hurst 前 d-1 天缺失,窗口最长 241,热身期只占样本开头;不使用 ts_rank / cross_rank / in_rank_rolling,nanrank_last 陷阱不涉及。"
         "风险:Hurst 的 R/S 估计在有限窗口里有向上偏误且受自相关 / 非平稳影响,价格水平序列的 Hurst 接近 1、区分度低(种子 2、16 是对照);若与低波动控制共线,残差会很小。")
d = {"seed": 2016, "round": 3, "slots": [
    {"type": "E", "core": H, "hypothesis": E_HYP, "seeds": E},
    {"type": "N", "hypothesis": N_HYP,
     "inspired_by": "B048(day_hurst(F) 一族):日内 R/S Hurst 的慢极值读法接近 0 分(pow_2(ts_max(day_hurst(Low),60)) = +0.10、ts_max(day_hurst(Close),50) = -0.03),其余读法在噪声带,说明有信息的是持续性这个形状;把同一度量搬到日频序列。",
     "seeds": N}],
     "R": Rv}
open('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2016/r3/missions.yaml', 'w', encoding='utf-8').write(
    yaml.safe_dump(d, allow_unicode=True, width=10**6, sort_keys=False))
