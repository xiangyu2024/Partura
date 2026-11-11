import re

MISSIONS = "/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2052/r2/missions.yaml"
OUT = "/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2052/r2/audit_1.yaml"

lines = open(MISSIONS, encoding="utf-8").read().splitlines()
r_heads = [l[len("- head: "):] for l in lines if l.startswith("- head: ")]
assert len(r_heads) == 2, r_heads


def q(s):
    return "'" + s.replace("'", "''") + "'"


slot_a = (
    "核心 C = day_argmin(in_slice_to_end(LV, day_argmax(LV)))(LV = in_local_mean(in_slice(Volume,31,211),5))原样出现在 M2 的三个 head 中,是 tide 拼接里的峰后枯竭时点子树,允许作核心。核心对 5 个控制的 |ρ| 最大 0.03,对快照 head 的原始 |ρ| 为 0.01,过 E 位门槛(<0.8)。"
    "创新度 4:外围不用 tide 算子,读数是峰到枯竭点的价格漂移(1、2、3、11、12、13)、枯竭深度(4、5、6)、枯竭点的 Low/Vwap 与反弹(7、8)、慢均值 / z 分数 / 残差(3、9、10)、以及二者的差(12)。对快照 head 的原始 |ρ|:1 号 0.35、2 号 0.38、14 号 0.45(残差 0.39),其余不超过 0.29,衰减比(4、5)不超过 0.12。1、2 号与 M2 第一个 head 有中度相关,但读的是峰后段而不是峰前段,不是换写法。"
    "合理度 4:逐个算子核对。in_slice 取 181 列;in_local_mean(d=5) 是居中的 9 分钟平滑;day_argmax / day_argmin 返回 slice 内的列号,in_slice_to_end 保留原列位置,所以 T、P 作为 day_locate 的索引对 Vwap、Close、LV、Volume 的列对齐正确。P、T 是用全日数据算出的日终量,按日终信号使用不构成分钟级前视(前提是收益按次日计,这一点在流水线里,我未核对)。分母全为正价格或正峰值成交量,未见除以近零的爆点;P 落在窗口末端时 T 退化为 P,相关 seed 的读数为 0,属少数日。"
    "9 号、10 号:cross_regres(day_std(Ret), signal, 60) 对照 rolling_ols 定义是 y 对 x 回归取残差,这里 y 为信号、x 为日内波动,即对波动取残差,方向正确。8 号的 day_last(in_slice(Vwap,31,211)) 取的是第 211 分钟而不是收盘,PI 笔记里『到收盘』的说法与实现不符,不影响合法性。"
    "数学检查的放行项:6 号 cross_mean(T−P, 20) 为整数分钟差,distinct 0.26,大量并列由股票列序打破,§4 明确不算问题;T 常贴在窗口末端时读数退化为 P 的位置,属边界主导,放行并标注。3 号 cross_zscore(…,60) 覆盖率 0.79:基底是 day_locate 在 T 或 P 上取值,日度 NaN 约 21%(1 号经 20 日均值后覆盖 0.993,掩盖了这一点),zscore 不做填充,缺失直接落在当天;这是缺失而不是热身期,但不是系统算不出,放行。14 号 Vwap_T − mean(Vwap) 是元为单位的差而不是收益,截面排序受价格水平影响,§4 不在三类之内,放行,PI 宜改为相对值。2 号与 1 号是同一表达式换字段(Close / cross_ema 对 Vwap / cross_mean),近重复,按规则只标注,不划除。"
    "如果它有 alpha,最可能来自放量冲击之后价格被吸收或衰减的速度:知情流持续则顺势漂移,流动性冲击则回吐;这是慢变的个股微观结构属性。"
)

slot_b = (
    "自动划除:2 号与 M2 第一个 head 的日度秩 |ρ| 为 0.79(≥0.7,与库禁令同一量);7 号与同一 head 的 |ρ| 为 0.73(≥0.7);12 号对 vol 控制的 |ρ| 为 0.82(≥0.8)。划除后余 9 个,≥4,过。"
    "创新度 3:本批的 N 读数(峰值分钟的价格位置、5 分钟冲击方向、量价关系、峰值成交量强度)与 M2 族的时点相同,读法不同。1 号(Vwap_P / 日均 Vwap)与 M2 第一个 head 原始 |ρ| 为 0.67、残差 0.63,是同一峰值价格水平的近邻,故不给 4。余下各 seed 对 head 的原始 |ρ| 在 0.03–0.61 之间,10 号 0.61(残差 0.51)是 Amt 与 Close 水平的相关,与 M2 相关较高。5 号(峰值成交量强度)对流动性控制 |ρ| 为 0.45,4 号对反转控制 0.47,都是中度相关而未触线。"
    "合理度 4:逐个核对。in_delta(in_slice(Close,31,211),5) 是后向 5 分钟差,在 P 列取值只用到 P 及之前的价格,P 是日终的 9 分钟平滑峰;ret5 / Close_P 与 LV_P / 日均 LV 的分母为正;day_corr 为日内相关,NaN 按有效点处理;ts_corr 与 cross_mean 的滚动都沿天轴、按股票独立,已对照 nd_ts.py 与 dt_cross.py。3 号 zscore 的覆盖率问题同 a 槽 3 号,放行。"
    "机制说不通的两处,不是数学问题,放行:10 号用的是 Amt 与 Close 的水平相关,度量的是日内价格走势与成交额的同向性,而不是『符号流向』,与 PI 的说法不是同一件事;11 号 Vwap_P − Close_P 是元值差,量纲未归一,截面排序受价格水平影响。"
    "如果它有 alpha,最可能来自峰值时刻价格相对均价的位置与 5 分钟冲击的方向(放量日里价格站在均价之上且冲击为买入方向,信息之后扩散),这是慢变的日内结构特征。"
)

r_text_1 = (
    "三个变体(Close 换 Vwap、窗口 20 换 40、两者叠加)的价格读数本身无 NaN 爆点与前视问题:day_locate 取值后只做 (loc_b − loc_a)/loc_a 与 (loc_c − loc_b)/loc_b,分母为正价格。"
    "但这一族有一个定义问题,原 head 与三个变体共有,需要 PI 注意:day_tide_change 的分支开关是 d = neg(sub(T, day_locate(in_slice(Volume,31,211), a))) = V_a − T,其中 V_a 是谷点分钟的原始成交量(label.py 注明 Volume 为原始股数),T 是 0–180 的列号。开关比较的是股数与分钟列号,不是『峰后 / 峰前』的时间关系:谷点成交量超过约 180 股走前支,否则走后支,分支主要随谷点成交量水平(流动性)而变,而不是随峰后段的时点。PI 笔记里的三标记分段解释对多数股票日不成立。"
    "这不在 §4 的三类之内,按 §3 给 3 分放行,但理由须写清。变体 1 与原 head 的 |ρ| 为 0.88,属替换分支,它的替换结论会继承这个开关,不能当作『换价格读数』的干净证据。建议 PI 在跑之前把开关改为列号之差(如 T − a),并在 train 上统计 d>0 的日占比,确认分支确实在切换。"
    "如果它有 alpha,最可能来自谷点到峰值的价格上涨(前支),这与原 head 的前支是同一个读数来源。"
)

r_text_2 = (
    "与 R 组 1 同样的分支开关问题:d 比较的是股数与列号,不是时间关系,三个变体继承它。"
    "另外分母 (b − a) 与 (c − b) 是列号之差:谷点与峰值相邻(差 1 分钟)时斜率是单分钟的价格变动,会出现大值;cross_mean(·,20) 是沿天轴的 20 日均值,单日的大值会进入均值,逐日排名压不住它,可能由少数日主导,PI 应核对 20 日均值的分布。a = b 或 c = b 时分子同为 0,得 0/0 = NaN,不是爆点。"
    "三个变体(Vwap、窗口 40、Close 窗口 40)与原 head 的 |ρ| 为 0.73、0.52、0.67,其中变体 1 的 0.73 为替换分支。合理度按 §3 给 3 分放行,理由同 R 组 1。"
    "如果它有 alpha,最可能来自峰前上涨的斜率(价格沿放量路径上行的速率),与 R 组 1 的前支是同一来源。"
)

summary = (
    "两个任务位均通过:a 槽 创新 4 / 合理 4,无划除;b 槽 创新 3 / 合理 4,自动划除 2、7、12 号,余 9 个。"
    "R 两组合理度均为 3 并保留,但两组共有的分支开关把股数与分钟列号相比较,所谓『峰后段』的机制在多数股票日并未被实现,建议 PI 修开关后再把 R 结论当作替换依据。"
)

out = []
out.append("attempt: 1")
out.append("slots:")
out.append("  - slot: a")
out.append("    novelty: 4")
out.append("    soundness: 4")
out.append("    struck_seeds: []")
out.append("    reasons: " + q(slot_a))
out.append("  - slot: b")
out.append("    novelty: 3")
out.append("    soundness: 4")
out.append("    struck_seeds: [2, 7, 12]")
out.append("    reasons: " + q(slot_b))
out.append("R:")
out.append("  - head: " + q(r_heads[0]))
out.append("    soundness: 3")
out.append("    reasons: " + q(r_text_1))
out.append("  - head: " + q(r_heads[1]))
out.append("    soundness: 3")
out.append("    reasons: " + q(r_text_2))
out.append("summary: " + q(summary))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("written", OUT)
