# -*- coding: utf-8 -*-
A="replace_small_with_nan(Amt)"; V="replace_small_with_nan(Volume)"
dvA="day_var(%s)"%A
C="cross_delay(log(day_gini(%s)), 1)"%A
E=[
"cross_reg_tvalue(%s, day_var(Ret), 241)"%C,
"cross_regbeta(%s, log(day_var(Ret)), 241)"%C,
"cross_corr(%s, day_mean(%s), 240)"%(C,V),
"cross_corr(%s, div(sub(day_max(High), day_min(Low)), day_mean(Close)), 240)"%C,
"cross_cov(%s, log(%s), 240)"%(C,dvA),
"sub(cross_corr(%s, %s, 120), cross_corr(%s, %s, 480))"%(C,dvA,C,dvA),
"cross_zscore(cross_corr(%s, %s, 240), 120)"%(C,dvA),
"cs_regres(cross_corr(%s, day_var(Ret), 240), cross_corr(%s, %s, 240))"%(C,C,dvA),
"cross_corr(%s, cross_delay(%s, 5), 240)"%(C,C),
"cross_corr(%s, day_mean(abs_(Ret)), 240)"%C,
"cross_reg_tvalue(%s, day_mean(%s), 241)"%(C,V),
"cross_corr(%s, log(day_gini(%s)), 240)"%(C,A),
"ts_mean(cross_corr(%s, day_var(Ret), 240), 10)"%C,
"cross_corr(%s, day_skew(Ret), 240)"%C,
"cross_corr(%s, cross_delta(log(%s), 1), 240)"%(C,dvA),
"cs_regres(cross_corr(%s, day_var(Ret), 240), log(cross_mean(day_mean(%s), 240)))"%(C,A),
]
GA="log(day_gini(%s))"%A; GR="log(day_gini(abs_(Ret)))"
AM="log(day_mean(div(abs_(Ret), %s)))"%A
L=lambda x:"cross_delay(%s, 1)"%x
N=[
"cross_corr(%s, %s, 240)"%(L(GA),GR),
"cross_corr(%s, %s, 240)"%(L(GR),dvA),
"cross_corr(%s, day_var(Ret), 240)"%L(GR),
"cross_corr(%s, %s, 240)"%(GA,GR),
"cross_reg_tvalue(%s, %s, 241)"%(L(GR),GA),
"cross_corr(%s, %s, 240)"%(L("log(day_es_ratio_hi(abs_(Ret)))"),dvA),
"cross_corr(%s, day_centroid(%s), 240)"%(L("day_centroid(abs_(Ret))"),A),
"cross_corr(%s, %s, 240)"%(L("sub(%s, %s)"%(GA,GR)),dvA),
"cross_corr(%s, %s, 240)"%(L(AM),dvA),
"cross_corr(%s, day_var(Ret), 240)"%L(AM),
"cross_regbeta(%s, log(%s), 241)"%(L(AM),dvA),
"cross_corr(%s, day_mean(%s), 240)"%(L(GR),V),
"cross_corr(%s, day_sum(Ret), 241)"%L("sub(%s, %s)"%(GA,GR)),
]
hE=open('hE.txt',encoding='utf-8').read().strip().replace("'","’")
hN=open('hN.txt',encoding='utf-8').read().strip().replace("'","’")
iN=open('iN.txt',encoding='utf-8').read().strip().replace("'","’")
q=lambda s:"'"+s+"'"
out="seed: 2046\nround: 3\nslots:\n  - type: E\n    core: '%s'\n    hypothesis: '%s'\n    seeds: [%s]\n  - type: N\n    hypothesis: '%s'\n    inspired_by: '%s'\n    seeds: [%s]\n"%(C,hE,", ".join(q(s) for s in E),hN,iN,", ".join(q(s) for s in N))
open("../missions.yaml","w",encoding='utf-8').write(out)
