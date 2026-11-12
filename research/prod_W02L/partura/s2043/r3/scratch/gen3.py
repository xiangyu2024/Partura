import json,yaml
d=json.load(open('../loc.json'))
heads=[h['expr'] if isinstance(h,dict) and 'expr' in h else h for h in d['heads']]
def C(a,b,F='Volume'):
    v=f"in_slice({F}, {a}, {b})"; dv=f"sub({v}, in_delay({v}, 1))"
    s=f"replace_small_with_nan(is_gt({dv}, add(in_mean_full({dv}), in_stddev_full({dv}))))"
    return f"day_mean(mul({s}, in_slice(Ret, {a}, {b})))"
c=C(31,211); A=f"abs_({c})"
assert A in heads[0], 'core not in head'
E=[f"div(ts_stddev({A}, 241), ts_stddev({A}, 60))",
 f"cross_semistd_pos({A}, 241)",
 f"cross_semistd_neg({A}, 241)",
 f"ts_stddev(cs_rank({A}), 241)",
 f"ts_stddev(cs_robust_z({A}), 241)",
 f"ts_stddev(sqrt({A}), 241)",
 f"ts_stddev(cross_delta({A}, 1), 241)",
 f"cross_mean(ts_stddev({A}, 20), 241)",
 f"ts_decay_linear(ts_stddev({A}, 60), 241)",
 f"ts_kurt({A}, 241)",
 f"sub(cross_max({A}, 241), cross_med({A}, 241))",
 f"cross_madz({A}, 241)",
 f"ts_stddev(cs_winsor({A}), 241)",
 f"ts_stddev(cross_ema({A}, 5), 241)",
 f"sub(ts_stddev({A}, 241), cross_mean(ts_stddev({A}, 20), 241))",
 f"ts_stddev(cs_rank(cs_demean(day_sum(Ret))), 241)" ]
E=E[:15]
N=["ts_stddev(day_centroid(Volume), 241)","ts_stddev(day_gini(Volume), 241)","ts_stddev(day_hurst(Close), 241)",
 "ts_stddev(day_hurst(Ret), 241)","ts_stddev(day_ar1_coefficient(Ret), 241)","ts_stddev(day_autocorr(Ret, 5), 241)",
 "ts_stddev(day_signed_ratio(Ret, Volume), 241)","div(ts_stddev(day_gini(Volume), 241), cross_mean(day_gini(Volume), 241))",
 "ts_stddev(cs_rank(day_centroid(Volume)), 241)","ts_stddev(cs_demean(day_es_ratio_hi(Ret)), 241)",
 "ts_stddev(day_zero_ratio(Ret), 241)","ts_stddev(day_flat_ratio(Close), 241)","ts_stddev(cs_rank(day_std(Ret)), 241)",
 "ts_stddev(cs_rank(day_hurst(Open)), 241)"]
h1,h2=heads[0],heads[1]
c16=C(16,226); cA=C(31,211,'Amt')
R=[{'head':h1,'why':'head1 (ts_stddev 241 of |C|, no demean) train 0.39 / valid 0.63; 360 日 train 掉到 -0.08 而 valid 升到 0.73,说明 241 附近只是折中点,窗口再细调(180/280)和降噪(先平滑再取 std、混合两套事件窗口 31-211 与 16-226、sqrt 稳定方差)可能把 train 抬起来。',
 'variants':[f"ts_stddev({A}, 180)",f"ts_stddev({A}, 300)",f"ts_stddev(sqrt({A}), 241)",f"ts_stddev(ts_mean({A}, 3), 241)",
  f"add(ts_stddev({A}, 241), ts_stddev(abs_({c16}), 241))",f"ts_stddev(abs_({cA}), 241)",f"ts_stddev(abs_(cs_demean({c})), 300)",
  f"ts_stddev(cs_rank({A}), 241)"]},
 {'head':h2,'why':'head2 (两项和,C 与 sustain 版)同样 241 train 0.32 / valid 0.46;480 日 train -0.47、valid 0.77:试 300 日、sqrt 稳定方差、只留 C 项(两项相加增加了 sustain 项噪声)。',
 'variants':[h2.replace(', 241)',', 300)'),h2.replace('abs_(','sqrt(abs_(',1).replace(', 241)',', 241)',1) if False else h2.replace(', 241)',', 180)')]}]
y={'seed':2043,'round':3,'slots':[
 {'type':'E','core':A,'hypothesis':open('hypE.txt').read().strip(),'seeds':E},
 {'type':'N','hypothesis':open('hypN.txt').read().strip(),'inspired_by':open('insp.txt').read().strip(),'seeds':N}],'R':R}
yaml.safe_dump(y,open('../missions.yaml','w'),allow_unicode=True,width=10**6)
