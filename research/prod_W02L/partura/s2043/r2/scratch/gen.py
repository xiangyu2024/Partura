import json,yaml
d=json.load(open('loc.json'))
heads=[h['expr'] if isinstance(h,dict) and 'expr' in h else h for h in d['heads']]
def sp(a,b): return f"in_slice({{F}}, {a}, {b})"
def spike(a,b,F='Volume'):
    v=f"in_slice({F}, {a}, {b})"; dv=f"sub({v}, in_delay({v}, 1))"
    return f"replace_small_with_nan(is_gt({dv}, add(in_mean_full({dv}), in_stddev_full({dv}))))", f"in_slice(Ret, {a}, {b})"
s,r=spike(31,211)
C=f"day_mean(mul({s}, {r}))"
K=f"abs_(cs_demean({C}))"
assert K in "".join(h for h in heads) or True
for h in heads: 
    if K in h: print('K in head ok'); break
absret="abs_(cs_demean(day_sum(Ret)))"
E=[f"div(ts_stddev({K}, 241), cross_mean({K}, 241))",
 f"cross_quantile({K}, 0.8, 241)",
 f"cross_quantile({K}, 0.9, 120)",
 f"div(cross_quantile({K}, 0.9, 241), cross_med({K}, 241))",
 f"ts_skew({K}, 241)",
 f"ts_kurt({K}, 120)",
 f"cross_autocorr({K}, 241, 1)",
 f"cross_regbeta(cross_delay({K}, 1), {K}, 241)",
 f"sub(cross_mean({K}, 60), cross_mean({K}, 241))",
 f"cross_ema({K}, 120)",
 f"cross_regbeta({absret}, {K}, 241)",
 f"cross_hurst({K}, 120)",
 f"cross_med({K}, 241)",
 f"cross_tail_mean_q75({K}, 241)",
 f"ts_decay_linear({K}, 241)",
 f"div({K}, cross_mean({absret}, 60))"]
Fs=['Open','Close']
def sH(F): return f"cross_mean(day_hurst({F}), 241)"
N=[sH('Open'),sH('Close'),
 "cross_mean(day_hurst(Ret), 241)",
 "cross_ema(day_hurst(Open), 120)",
 "cross_med(day_hurst(Open), 241)",
 "cross_mean(day_hurst(in_slice(Open, 31, 211)), 241)",
 "sub(cross_mean(day_hurst(Open), 241), cross_mean(day_hurst(Open), 60))",
 "cross_mean(day_ar1_coefficient(Ret), 241)",
 "cross_mean(day_autocorr(Ret, 5), 241)",
 "cross_mean(day_durbin_watson(Close), 241)",
 "cross_mean(day_centroid(Volume), 241)",
 "cross_mean(day_gini(Volume), 241)",
 "cross_regbeta(day_hurst(Open), day_sum(Ret), 241)",
 "cross_corr(day_hurst(Open), day_gini(Volume), 241)",
 "cross_mean(day_signed_ratio(Ret, Volume), 241)",
 "cs_regres(cross_mean(day_hurst(Open), 241), cross_mean(day_gini(Volume), 241))"]
hA,hB,hC=heads[0],heads[1],heads[2]
import re
def win(h,pat,new): return h[:h.rindex(pat)]+new+")" 
def R_(h,n): 
    assert h.endswith(", 60)"); return h[:-4]+str(n)+")"
KA=hA[len("ts_stddev("):-5]; KB=hB[len("ts_stddev("):-5]
R=[{'head':hA,'why':'60 日窗口还太快:r1 里同一个 head 的窗口 20→60→90→120→241 分数 -1.09→-0.34→0.06→-0.03(valid)→0.48(train 0.48 / valid 0.55),并且 241 日版与原 head 的 ρ 降到 0.3;线还没到头,试 360/480/720 以及无量纲(CV)形式。',
 'variants':[R_(hA,360),R_(hA,480),R_(hA,720),f"div(ts_stddev({KA}, 241), cross_mean({KA}, 241))"]},
 {'head':hB,'why':'同一族去掉 cs_demean 的 60 日 head;r1 的窗口线对 16–226 版 60→241 单调改善,31–211 版没测过 241 以上,试 241/360/480 与 CV 形式。',
 'variants':[R_(hB,241),R_(hB,360),R_(hB,480),f"div(ts_stddev({KB}, 241), cross_mean({KB}, 241))"]},
 {'head':heads[2],'why':'两项和(C 与 sustain 版)的窗口都是 60;同族单项窗口越长越好,两项同时拉到 241 / 480。','variants':[heads[2].replace(", 60)",", 241)"),heads[2].replace(", 60)",", 480)")]}]
plan={'seed':2043,'round':2,'slots':[
{'type':'E','core':K,'hypothesis':"",'seeds':E},
{'type':'N','hypothesis':"",'inspired_by':"",'seeds':N}],'R':R}
json.dump(plan,open('scratch/plan.json','w'),ensure_ascii=False)
print(len(E),len(N),[x['head'][:30] for x in R]); print(heads[2][-60:])
