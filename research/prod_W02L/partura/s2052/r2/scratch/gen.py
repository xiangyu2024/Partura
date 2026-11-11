import yaml
V="in_local_mean(in_slice(Volume, 31, 211), 5)"
P=f"day_argmax({V})"
T=f"day_argmin(in_slice_to_end({V}, {P}))"
def L(x,i): return f"day_locate(in_slice({x}, 31, 211), {i})"
def ret(x,a,b): return f"div(sub({L(x,b)}, {L(x,a)}), {L(x,a)})"
rv=ret("Vwap",P,T); rc=ret("Close",P,T)
rebound=f"div(sub(day_last(in_slice(Vwap, 31, 211)), {L('Vwap',T)}), {L('Vwap',T)})"
depth=f"div(day_locate({V}, {T}), day_locate({V}, {P}))"
E=[f"cross_mean({rv}, 20)",f"cross_ema({rc}, 20)",f"cross_zscore({rv}, 60)",
 f"cross_mean({depth}, 20)",f"cross_decay_linear({depth}, 30)",f"cross_mean(sub({T}, {P}), 20)",
 f"cross_mean(div({L('Low',T)}, {L('Vwap',T)}), 20)",f"cross_mean({rebound}, 20)",
 f"cross_regres(day_std(Ret), cross_mean({rv}, 10), 60)",f"sub(cross_mean({rv}, 10), cross_mean({rv}, 60))",
 f"cross_stddev({rv}, 30)",f"cross_mean(sub({rv}, {rebound}), 20)",
 f"cross_mean(mul({rv}, {depth}), 20)",f"cross_mean(sub({L('Vwap',T)}, day_mean(in_slice(Vwap, 31, 211))), 20)"]
Vd=f"day_locate({V}, {P})"
burst=f"day_locate(in_delta(in_slice(Close, 31, 211), 5), {P})"
bretn=f"div({burst}, {L('Close',P)})"
bness=f"div({Vd}, day_mean({V}))"
N=[f"cross_mean(div({L('Vwap',P)}, day_mean(in_slice(Vwap, 31, 211))), 20)",
 f"cross_mean({bretn}, 20)",f"cross_zscore({bretn}, 60)",
 "cross_mean(day_corr(in_slice(Volume, 31, 211), in_delta(in_slice(Close, 31, 211), 1)), 20)",
 f"cross_mean({bness}, 20)",f"cross_regres(day_std(Ret), cross_mean({bness}, 10), 60)",
 f"cross_mean(mul({bness}, {bretn}), 20)",
 f"ts_corr({bness}, {bretn}, 40)",
 f"sub(cross_mean({bretn}, 10), cross_mean({bretn}, 60))",
 "cross_mean(day_corr(in_slice(Amt, 31, 211), in_slice(Close, 31, 211)), 20)",
 f"cross_decay_linear(sub({L('Vwap',P)}, {L('Close',P)}), 30)",
 f"cross_mean(div(sub({L('High',P)}, {L('Low',P)}), {L('Close',P)}), 20)"]
hE=("核心 C = T = day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume,31,211),5), day_argmax(...))),即当天 5 分钟平滑成交量"
"达到峰值之后、成交量萎缩到最低的那一分钟(「放量后枯竭点」)。它是 M2 批三个 head(day_tide_change / day_tide_speed,分数 -1.0~-1.14)共有的标记点之一;"
"拆解显示:把潮汐里的价格换成 Vwap 后 -1.00/-0.35 变 -0.85/-0.13(valid 近 0),说明起作用的是「放量-枯竭」这个时点而价格读数越平滑越好;"
"整段 neg(sub(...)) 时点子树单独 -1.88,说明只看时点不够、要配价格。以前见过的外围全是 day_tide_change/day_tide_speed 三标记分段拼接(峰前低谷到峰、峰到峰后低谷的相对变化或斜率),"
"本轮完全不用 tide 算子,改为在 T 上直接取读数:(a) 峰值分钟到枯竭分钟的 Vwap/Close 收益(放量冲击之后的价格漂移:知情流持续则继续同向,流动性冲击则回吐);"
"(b) 枯竭深度 = 枯竭点成交量 / 峰值成交量(冲击衰减得多快);(c) 枯竭点处 Low/Vwap(买卖价差反弹的下影)、枯竭点之后到收盘的 Vwap 反弹;(d) 峰后持续时长 T-P;"
"(e) 都取 10-30 日慢均值 / z 分数 / 对波动回归残差 / 10 对 60 日差,以降低拿来换手的日度噪声。与库里不同:库里该核心只出现在潮汐拼接里,这里是价格漂移 / 衰减深度的无拼接读法,骨架不同。"
"样本外还会在的理由:放量冲击后的吸收 / 衰减速度度量的是流动性提供者吸收冲击的能力与信息持续性,是慢变的个股微观结构属性,与年份行情无关。"
"风险:所有同族分数都为负(-1.0 起),毛超额可能约为 0,赌注是亏损主要来自快速换手而慢读法能压住。分母均为价格或成交量,不会近零;P 在窗口末尾时 T 退化,按 NaN/平价处理,属少数日。")
hN=("新 idea:「放量爆发的方向」。当天 5 分钟平滑成交量峰值分钟 P 上的价格行为:(1) 该分钟结束的 5 分钟收益(爆发是买盘推动还是卖盘砸出,标准的有符号成交量冲击,相对价格归一);"
"(2) 峰值成交量 / 全日平均(爆发程度)与方向的乘积;(3) 峰值处 Vwap 相对全日均价的位置;(4) 日内成交量与分钟收益的相关(符号流向,Amihud/Kyle 风格的流向 - 价格联动);"
"(5) 峰值分钟的 (High-Low)/Close 振幅;全部取 10-30 日慢均值 / z 分数 / 与波动回归残差。机制:机构拆单与消息驱动的放量日里,爆发方向携带知情信息,"
"其后几天出现漂移(信息缓慢扩散 + 流动性提供者补偿),是跨日可持续的结构性现象;反弹型爆发(价差宽、被动盘主导)则相反。"
"与库里不同:库里该批围绕 day_ar1_coefficient 与 day_tide_* 的时点 / 斜率拼接,从未直接读取峰值分钟上的价格与方向,也没有成交量爆发程度 × 方向的乘积;骨架(day_locate 在 argmax 上取 in_delta 收益)与潮汐 / AR(1) 不同。"
"样本外还会在的理由:信息扩散的延迟与被动盘补偿是结构性的,不依赖某年行情。风险:有符号冲击与 20 日反转控制中度相关(新尺子已去掉其非线性暴露),且与 M2 一样毛超额可能约为 0。")
out={"seed":2052,"round":2,"slots":[
 {"type":"E","core":T,"hypothesis":hE,"seeds":E},
 {"type":"N","hypothesis":hN,"inspired_by":"B002 / M2 批(day_tide_change / day_tide_speed,Close->Vwap 把 valid 从 -0.35 抬到 -0.13,峰值与枯竭点时点)","seeds":N}]}
yaml.safe_dump(out,open("missions.yaml","w"),allow_unicode=True,width=10000,sort_keys=False)
import json,re
loc=open("loc.md").read()
heads=re.findall(r"\| `(cross_mean\(day_tide_\w+\(in_slice\(Close, 31, 211\).*?)` \|$",loc.split("## 共性")[0],re.M)
R=[]
for h in heads[:2]:
    vs=[h.replace("in_slice(Close, 31, 211)","in_slice(Vwap, 31, 211)",1)]
    vs.append(vs[0][:-4]+"40)")
    vs.append(h[:-4]+"40)")
    R.append({"head":h,"why":"拆解:Close->Vwap 增益 +0.16 / 窗口 20->40 增益 +0.16(valid 更好);价格读数越平滑越好、慢均值压换手;两者叠加试。","variants":vs})
out["R"]=R
yaml.safe_dump(out,open("missions.yaml","w"),allow_unicode=True,width=10000,sort_keys=False)
