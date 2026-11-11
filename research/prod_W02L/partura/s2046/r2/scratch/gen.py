# -*- coding: utf-8 -*-
A="replace_small_with_nan(Amt)"; V="replace_small_with_nan(Volume)"
B="div(day_var(%s), pow_2(day_mean(%s)))"%(A,A)
BV="div(day_var(%s), pow_2(day_mean(%s)))"%(V,V)
C="cross_delay(log(%s), 1)"%B
dvA="day_var(%s)"%A
E=[
"cross_corr(%s, %s, 240)"%(C,dvA),
"cross_corr(%s, day_var(Ret), 240)"%C,
"cross_regbeta(%s, day_sum(Ret), 241)"%C,
"cross_reg_tvalue(%s, log(%s), 120)"%(C,dvA),
"cross_regbeta(%s, log(day_mean(%s)), 120)"%(C,A),
"cross_corr(%s, cross_delta(log(day_mean(%s)), 1), 120)"%(C,A),
"cross_corr(%s, cs_demean(day_sum(Ret)), 120)"%C,
"sub(cross_mean(%s, 20), cross_mean(%s, 241))"%(C,C),
"cross_corr(%s, log(day_var(Close)), 241)"%C,
"cross_corr(%s, day_skew(%s), 241)"%(C,A),
"cs_regres(cross_corr(%s, %s, 240), log(cross_mean(day_mean(%s), 240)))"%(C,dvA,A),
"cross_corr(%s, day_var(%s), 120)"%(C,V),
"cross_reg_tvalue(%s, %s, 241)"%(C,dvA),
"ts_mean(cross_corr(%s, %s, 120), 20)"%(C,dvA),
"cross_corr(%s, log(day_var(%s)), 241)"%(C,V),
"cross_regbeta(%s, cross_delay(%s, 1), 241)"%(C,dvA),
]
G="day_gini(%s)"%A; ES="day_es_ratio_hi(%s)"%A
N=[
"cross_corr(cross_delay(log(%s), 1), %s, 240)"%(G,dvA),
"cross_corr(cross_delay(%s, 1), %s, 120)"%(G,dvA),
"cross_corr(cross_delay(log(%s), 1), %s, 240)"%(ES,dvA),
"cross_corr(cross_delay(day_centroid(%s), 1), %s, 240)"%(A,dvA),
"cross_corr(cross_delay(log(%s), 1), %s, 240)"%(BV,dvA),
"cross_corr(cross_delay(sub(log(%s), log(%s)), 1), %s, 240)"%(B,BV,dvA),
"cross_regbeta(cross_delay(log(%s), 1), log(%s), 241)"%(G,dvA),
"cross_corr(cross_delay(log(%s), 1), day_sum(Ret), 120)"%G,
"cross_corr(cross_delay(log(%s), 1), day_sum(Ret), 241)"%ES,
"cross_corr(cross_delay(day_centroid(%s), 1), day_sum(Ret), 241)"%A,
"cross_reg_tvalue(cross_delay(log(%s), 1), day_sum(Ret), 120)"%BV,
"cross_corr(cross_delay(log(%s), 1), day_var(Ret), 240)"%G,
"cross_corr(cross_delay(sub(log(%s), log(%s)), 1), %s, 240)"%(G,B,dvA),
"cross_corr(cross_delay(sub(log(%s), log(%s)), 1), day_sum(Ret), 241)"%(B,BV),
]
q=lambda s:"'"+s+"'"
hE=open('hE.txt',encoding='utf-8').read().strip().replace("'","’")
hN=open('hN.txt',encoding='utf-8').read().strip().replace("'","’")
iN=open('iN.txt',encoding='utf-8').read().strip().replace("'","’")
out="seed: 2046\nround: 2\nslots:\n  - type: E\n    core: '%s'\n    hypothesis: '%s'\n    seeds: [%s]\n  - type: N\n    hypothesis: '%s'\n    inspired_by: '%s'\n    seeds: [%s]\n"%(C,hE,", ".join(q(s) for s in E),hN,iN,", ".join(q(s) for s in N))
open("../missions.yaml","w",encoding='utf-8').write(out)
