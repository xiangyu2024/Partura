import yaml
def W(n, a=(2,240), f='Volume'):
    return f"day_pdf_quantile_bilateral_half_width(in_slice(Ret, {a[0]}, {a[1]}), in_slice({f}, {a[0]}, {a[1]}), {n})"
V,R="in_slice(Volume, 11, 240)","in_slice(Ret, 11, 240)"
def T(p, largest=True, f=V):
    return f"in_topk_masked({f}, {R}, {p}{'' if largest else ', False'})"
sig5=f"day_std({T(5)})"; sigq=f"day_std({T(5,False)})"
S=f"ts_stddev({sig5}, 160)"
full=f"day_std({R})"
F=f"ts_stddev({full}, 160)"
N=[
 f"cross_stddev(sub({W(0.9)}, {W(0.5)}), 120)",
 f"cross_mean(sub({W(0.9)}, {W(0.5)}), 241)",
 f"cross_stddev(sub({W(0.9)}, {W(0.7)}), 160)",
 f"ts_stddev(sub({W(0.9)}, {W(0.5)}), 160)",
 f"cross_ema(sub({W(0.9)}, {W(0.5)}), 120)",
 f"cross_stddev(sub({W(0.9,f='Amt')}, {W(0.5,f='Amt')}), 120)",
 f"cross_stddev(sub({W(0.9,a=(2,120))}, {W(0.9,a=(121,240))}), 120)",
 f"cross_mean(sub({W(0.9,a=(2,120))}, {W(0.9,a=(121,240))}), 241)",
 f"cross_stddev(sub({W(0.9)}, {W(0.9,f='Amt')}), 120)",
 f"cross_mean(sub({W(0.9)}, {W(0.9,f='Amt')}), 241)",
 f"cross_stddev(sub({W(0.95)}, {W(0.8)}), 160)",
 f"ts_mean(sub({W(0.9,a=(11,230))}, {W(0.5,a=(11,230))}), 120)",
 f"cross_stddev(sub({W(0.5,a=(2,120))}, {W(0.5,a=(121,240))}), 160)",
]
E=[
 f"sub(cs_rank({S}), cs_rank({F}))",
 f"cs_regres({S}, {F})",
 f"sub({S}, ts_stddev({sigq}, 160))",
 f"add(cs_rank({S}), cs_rank(cross_stddev({W(0.9)}, 160)))",
 f"add(cs_rank({S}), cs_rank(ts_corr({sig5}, day_sum(Ret), 160)))",
 f"ts_rank({S}, 241)",
 f"sub({S}, cross_delay({S}, 60))",
 f"cs_regres({S}, cross_mean({full}, 160))",
 f"add(cs_rank({S}), cs_rank(ts_corr({sig5}, {sigq}, 160)))",
 f"sub(cs_rank({S}), cs_rank(ts_stddev(day_std({T(5,f='in_slice(Amt, 11, 240)')}), 160)))",
]
Rr=[
 dict(head=S, why="窗口 80 / 320 都比 160 差(−0.83 / −0.94,320 的 train 坏、valid −0.10),160 是峰;峰附近的窗口与放量分钟占比 p 没有测过,看峰是否更尖",
  variants=[f"ts_stddev({sig5}, 120)", f"ts_stddev({sig5}, 200)", f"ts_stddev({sig5}, 240)",
            f"ts_stddev(day_std({T(7)}), 160)", f"ts_stddev(day_std({T(4)}), 160)"]),
 dict(head=f"cross_mean({W(0.9)}, 20)", why="同一对象的 'median' 版本拆解:窗口 20→10 对 cross_stddev 增益 +0.57、Volume→Amt 对 cross_mean 增益 +0.20 / 对 cross_stddev +0.26,变异性读法更好、更短窗口更好;本 head 是 prob 中心版,这些改动没有在它上面试过",
  variants=[f"cross_stddev({W(0.9)}, 10)", f"cross_stddev({W(0.9)}, 5)", f"cross_mean({W(0.9,f='Amt')}, 20)", f"cross_stddev({W(0.9,f='Amt')}, 10)"]),
]
doc=dict(seed=2025, round=3, slots=[
 dict(type='N', hypothesis=open('scratch/N_hyp.txt').read().strip(), inspired_by=open('scratch/N_insp.txt').read().strip(), seeds=N),
 dict(type='E', core=S, hypothesis=open('scratch/E_hyp.txt').read().strip(), seeds=E)], R=Rr)
yaml.safe_dump(doc, open('missions.yaml','w'), allow_unicode=True, width=10000, sort_keys=False)
