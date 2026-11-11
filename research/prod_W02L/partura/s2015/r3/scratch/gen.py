import yaml
def A(q='Amt',d=60,s='day_quantile_q25'):
    x=f'{s}({q})'
    return f'sub(cross_semistd_neg({x}, {d}), cross_semistd_pos({x}, {d}))'
ZR='day_zero_ratio(Volume)'
Z=lambda d: f'cross_mean({ZR}, {d})'
AA=A(); AV=A('Volume')
e1=[
 f'add(cs_rank({Z(20)}), cs_rank({AA}))',
 f'mul(cs_rank({Z(60)}), cs_rank({AA}))',
 f'sub({Z(20)}, {Z(120)})',
 f'cs_bucket_zscore({Z(20)}, cross_mean(day_sum(Amt), 30))',
 f'cross_mean(sub(day_zero_ratio(Ret), {ZR}), 20)',
 f'div({Z(60)}, cross_mean(day_quantile_q25(Amt), 60))',
 f'cross_stddev({ZR}, 60)',
 f'cross_corr({ZR}, day_std(Ret), 60)',
 f'cs_flip_by_state({Z(20)}, day_sum(Amt))',
 f'mul({Z(60)}, {A("Amt",60,"day_median")})',
 f'cross_max({ZR}, 60)',
 f'add(cs_rank({Z(60)}), cs_rank(sub(log(cross_mean(day_sum(Amt), 20)), log(cross_mean(day_sum(Amt), 120)))))',
]
ZRr='day_zero_ratio(Ret)'
e2=[
 'cross_mean(day_flat_run_max(Volume), 60)',
 'cross_mean(day_distinct_ratio(Close), 20)',
 'cross_mean(day_flat_ratio(Ret), 20)',
 'sub(cross_mean(day_flat_run_max(Ret), 20), cross_mean(day_flat_run_max(Volume), 20))',
 'cross_stddev(day_flat_run_max(Volume), 60)',
 'cross_corr(day_zero_ratio(Volume), day_zero_ratio(Ret), 60)',
 'cs_bucket_zscore(cross_mean(day_distinct_ratio(Close), 20), LogFloatCap)',
 'cross_delta(cross_mean(day_flat_ratio(Ret), 20), 60)',
 'mul(cs_rank(cross_mean(day_flat_run_max(Volume), 60)), cs_rank(cross_mean(day_distinct_ratio(Close), 60)))',
 'sub(cs_rank(cross_mean(day_distinct_ratio(Close), 60)), cs_rank(cross_mean(day_flat_ratio(Ret), 60)))',
 'cs_flip_by_state(cross_mean(day_flat_run_max(Volume), 20), day_sum(Amt))',
 'cross_mean(sub(day_flat_run_max(Ret), day_flat_run_max(Volume)), 60)',
]
head=f'div({ZR}, add({AA}, {AV}))'
def H(num=ZR,da=60,dv=60,dn=None):
    return f'div({num}, add({A("Amt",da)}, {A("Volume",dv)}))'
R=[H(da=120),H(da=120,dv=120),H(da=240,dv=120),H(da=240,dv=240),H(num=Z(20),da=120),H(num=Z(20),da=120,dv=120),
   f'div({Z(20)}, {A("Amt",120)})', f'div({ZR}, add({A("Amt",120)}, {A("Volume",120,"day_median")}))']
doc=dict(seed=2015,round=3,slots=[
 dict(type='E',core=ZR,hypothesis=open('h1.txt').read().strip(),seeds=e1),
 dict(type='N',hypothesis=open('h2.txt').read().strip(),inspired_by=open('i2.txt').read().strip(),seeds=e2)],
 R=[dict(head=head,why=open('r.txt').read().strip(),variants=R)])
yaml.safe_dump(doc,open('missions.yaml','w'),allow_unicode=True,width=10000,sort_keys=False)
