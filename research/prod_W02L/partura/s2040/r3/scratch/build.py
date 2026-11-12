import yaml,json
exec(open("gen.py").read().split("E=[")[0])
E=open("e.txt").read().split("\n"); N=open("n.txt").read().split("\n")
def L4(lab,F="Close"): return f"select_where(eq(in_roll_labels({F}, {lab}), 4), {ONE.replace('Close',F)}, {ZERO.replace('Close',F)})"
def L0(lab,F="Close"): return f"select_where(eq(in_roll_labels({F}, {lab}), 0), {ONE.replace('Close',F)}, {ZERO.replace('Close',F)})"
H=[h["expr"] for h in json.load(open("../loc.json"))["heads"]]
h1=f"day_mean(cross_decay_linear({L4(241)}, 20))"; assert h1 in H
h2=f"day_mean(cross_decay_linear({L4(120)}, 20))"; assert h2 in H
h3=[h for h in H if h.startswith("mul(add(day_mean(select_where(eq(in_roll_labels(Close, 241), 4)")][0]
V=lambda lab,d:f"day_mean(cross_decay_linear({L4(lab,'Vwap')}, {d}))"
R=[
 {"head":h1,"why":"本批 head 里 valid 最好(-1.07)的一条。拆解表:窗口 20→40 增益 +0.12(-1.26),Vwap 换掉 Close 后 train -1.61 / valid -0.10(valid 大幅改善、train 变差);两种改动单独都没有把分数抬到 -1 以上,而'越慢越好'的方向在 20→40 上同向。这里测更慢的衰减(60/120)和两改动的合并:Vwap 减小了收盘价的尾盘波动噪声,慢衰减降低换手;另给一条'上尾占比减下尾占比'的版本,读'日内价位更偏上还是偏下'的偏度而不只是上尾。",
  "variants":[f"day_mean(cross_decay_linear({L4(241)}, 60))",f"day_mean(cross_decay_linear({L4(241)}, 120))",V(241,40),V(241,60),
   f"day_mean(cross_decay_linear(sub({L4(241)}, {L0(241)}), 40))",f"day_mean(cross_decay_linear(sub({L4(241,'Vwap')}, {L0(241,'Vwap')}), 60))"]},
 {"head":h2,"why":"-3.20 的 head(滚动 120 分钟窗口的标签,滞后分钟窗口更短所以更吵)。拆解表:Vwap 替换 +0.78(-2.42)、衰减 20→40 +0.50(-2.70),衰减 20→10 更差(-3.55),都指向'更慢、更平滑的价格口径更好';两者从未合并过。变体:Vwap 与 40 / 60 / 120 的合并,以及把 120 分钟窗口换成整日窗口(241)的 Vwap 版。",
  "variants":[V(120,40),V(120,60),V(120,120),V(241,120)]},
 {"head":h3,"why":"-3.14 的 head。拆解表:Vwap 替换 +1.03(-2.11);去掉'标签 0 项'的敲除 +0.15(-3.29,本身变差但说明该项是噪声),换'in_shift(Ret,1)'为 2 变差微小。变体:Vwap 与去掉标签 0 项合并;再把乘数 in_shift(Ret,1)(即前一分钟收益的日均,≈ 日均收益)换成 60 日均值使其变慢,因为 -3 的主因是换手而不是方向。",
  "variants":[
   f"mul(day_mean({L4(241,'Vwap')}), day_mean(in_shift(Ret, 1)))",
   f"mul(add(day_mean({L4(241,'Vwap')}), day_mean({L0(241,'Vwap')})), cross_mean(day_mean(in_shift(Ret, 1)), 60))",
   f"cross_mean(mul(add(day_mean({L4(241,'Vwap')}), day_mean({L0(241,'Vwap')})), day_mean(in_shift(Ret, 1))), 60)",
   f"cross_mean(mul(day_mean({L4(241,'Vwap')}), day_mean(in_shift(Ret, 1))), 120)"]}]
hE=open("hyp_E.txt").read().strip(); hN=open("hyp_N.txt").read().strip()
plan={"seed":2040,"round":3,"slots":[
 {"type":"E","core":A,"hypothesis":hE,"seeds":E},
 {"type":"N","hypothesis":hN,"inspired_by":"B120(滚动标签分桶,手写库 29 条)的'价格在当天分布里待在哪'这一现象,及拆解里 Vwap 优于 Close、越慢越好:把'价位 vs 成交量'的位置关系做成新的状态变量。","seeds":N}],
 "R":R}
yaml.safe_dump(plan,open("../missions.yaml","w"),allow_unicode=True,width=100000,sort_keys=False)
open("r.txt","w").write("\n".join(v for g in R for v in g["variants"]))
