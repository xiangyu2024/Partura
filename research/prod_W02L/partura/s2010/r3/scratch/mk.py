import yaml
D='day_durbin_watson(in_slice(Vwap, 211, 240))'
D0='day_durbin_watson(in_slice(Vwap, 1, 30))'
A='cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1)'
B='cross_delay(%s, 1)'%D
L1='cross_delay(day_sum(in_slice(Ret, 1, 210)), 1)'
L3='cross_delay(%s, 1)'%A
T='day_sum(in_slice(Ret, 211, 240))'
GAP='sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1)'
AMT='div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))'
a1='day_ar1_coefficient(in_slice(Ret, 1, 210))'
a1t='day_ar1_coefficient(in_slice(Ret, 211, 240))'
e1=[
f'cross_corr(day_std(in_slice(Ret, 211, 240)), {A}, 241)',
f'cross_corr({AMT}, {A}, 241)',
f'cross_corr(day_durbin_watson(in_slice(Close, 211, 240)), {A}, 241)',
f'cross_regbeta({A}, cs_rank({D}), 241)',
f'cross_corr({A}, {T}, 241)',
f'cross_corr({A}, day_sum(in_slice(Ret, 1, 30)), 241)',
f'cross_corr(cs_rank({A}), cs_rank({D}), 241)',
f'cross_corr({A}, abs_(day_sum(Ret)), 241)',
f'div(cross_cov({A}, {D0}, 241), cross_mean({D0}, 241))',
f'cross_corr({A}, {a1}, 241)',
f'cross_corr({A}, day_durbin_watson(in_slice(Vwap, 31, 210)), 482)',
f'cross_corr({A}, {GAP}, 241)',
f'cross_corr(sign({A}), {D}, 241)',
]
e2=[
f'cross_corr({B}, ts_sum(day_sum(in_slice(Ret, 1, 210)), 5), 241)',
f'cross_corr({B}, day_sum(in_slice(Ret, 1, 30)), 241)',
f'cross_corr({B}, {GAP}, 241)',
f'cross_regbeta(cs_rank({B}), day_sum(Ret), 241)',
f'cross_corr({B}, abs_(day_sum(in_slice(Ret, 1, 210))), 241)',
f'cross_corr({B}, {AMT}, 241)',
f'cross_corr({B}, {L1}, 482)',
f'cross_corr({B}, {L3}, 241)',
f'div(cross_cov({B}, sign(day_sum(Ret)), 241), cross_mean({B}, 241))',
f'cross_corr({B}, {a1}, 241)',
f'cross_corr(log({B}), {T}, 241)',
f'cross_corr({B}, ts_sum(day_sum(in_slice(Ret, 1, 210)), 20), 241)',
]
n=[
f'cross_corr({a1}, {A}, 241)',
f'cross_corr({a1}, {L1}, 241)',
f'cross_corr({a1t}, {A}, 241)',
f'sub(cross_corr({D}, {A}, 241), cross_corr({D}, {L1}, 241))',
f'sub(cross_corr({D}, {A}, 241), mul(add(cross_corr({D}, {L1}, 241), cross_corr({D}, {L3}, 241)), 0.5))',
f'cross_corr({a1}, {D}, 241)',
f'cross_regbeta(cs_rank({a1}), {T}, 241)',
f'cross_corr({a1}, cross_delay({a1t}, 1), 241)',
f'cross_corr({a1}, cross_delay(cross_delay(day_sum(Ret), 1), 1), 482)',
f'cross_mean(mul({a1}, sign({A})), 241)',
f'cross_corr(cs_rank({a1}), cs_rank({A}), 241)',
f'cross_corr({a1}, day_std(in_slice(Ret, 211, 240)), 241)',
]
H=f'cross_corr({D}, {A}, 241)'
def hd(r='in_slice(Ret, 1, 210)'): return f'cross_corr({D}, cross_delay(cross_delay(day_sum({r}), 1), 1), 241)'
rv=[
hd('in_slice(Ret, 1, 240)'),
hd('in_slice(Ret, 1, 30)'),
f'cross_corr(log({D}), {A}, 241)',
f'cross_corr(cs_rank({D}), cs_rank({A}), 241)',
f'cross_corr({D}, {A}, 360)',
f'cross_corr(day_durbin_watson(in_slice(Vwap, 181, 240)), {A}, 241)',
f'cross_corr(day_durbin_watson(in_slice(Vwap, 226, 240)), {A}, 241)',
f'cross_corr({D}, ts_sum({A}, 3), 241)',
f'cross_corr({D}, sign({A}), 241)',
f'div(cross_cov({D}, {A}, 241), cross_stddev({D}, 241))',
f'cross_corr({D}, cs_rank({A}), 241)',
f'cross_corr({D}, {A}, 241)'.replace('Vwap','Vwap'),
]
rv=rv[:-1]
hE1=open('hE1.txt').read().strip(); hE2=open('hE2.txt').read().strip(); hN=open('hN.txt').read().strip(); hR=open('hR.txt').read().strip()
m={'seed':2010,'round':3,'slots':[
 {'type':'E','core':A,'hypothesis':hE1,'seeds':e1,'literature':[{'title':'Dynamic Volume-Return Relation of Individual Stocks','authors':'Llorente, Michaely, Saar, Wang','year':'2002','treatment':'成交 / 微观结构状态与后续收益的延续或回吐;这里把状态换成尾盘价格路径粗糙度等,收益换成滞后两天的收益'}],
  'seeds_note':None},
 {'type':'E','core':B,'hypothesis':hE2,'seeds':e2},
 ],'R':[{'head':H,'why':hR,'variants':rv}]}
m['slots'][0].pop('seeds_note')
# N as third? only 2 slots: replace E2 by N
m['slots'][1]={'type':'N','hypothesis':hN,'inspired_by':'B030 的 day_ar1_coefficient(Ret) 裸对象(收益路径的一阶自相关)与本流第 2 轮 E 位唯一的 head:尾盘 DW 对滞后两天收益的相关(+0.51)在滞后 1 / 2 / 3 天上读数 +0.19 / +0.51 / +0.36,滞后结构本身像是信号','seeds':n,
 'literature':[{'title':'Return Reversals and Liquidity Provision (Evaporating Liquidity)','authors':'Stefan Nagel','year':'2012','treatment':'短期反转是流动性提供者的补偿;这里用分钟收益 AR(1) 的符号刻画个股的价差弹跳 / 趋势,并看它与滞后收益的耦合'},
  {'title':'Trading Volume and Serial Correlation in Stock Returns','authors':'John Campbell, Sanford Grossman, Jiang Wang','year':'1993','treatment':'库存风险使价格反转;分钟收益自相关为负的个股是有流动性提供者的票'}]}
yaml.safe_dump(m,open('../missions.yaml','w'),allow_unicode=True,sort_keys=False,width=100000)
open('e2unused.txt','w').write('\n'.join(e2))
