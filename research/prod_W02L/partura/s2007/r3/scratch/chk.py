import re,yaml,glob
def seeds(p):
    d=yaml.safe_load(open(p))
    out=[]
    for s in d['slots']:
        out.append((s.get('type'),s.get('core'),s.get('seeds',[])))
    return out
r2=seeds('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2007/r2/missions_final.yaml')
r3=seeds('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2007/r3/missions.yaml')
def ops(e): return set(re.findall(r'([a-zA-Z_][a-zA-Z_0-9]*)\(',e))
def canon(e): return e.replace(' ','')
K='day_close(in_kurt_full(Amt))'
r2K=[s for t,c,ss in r2 if c==K for s in ss]
print('r2 K seeds',len(r2K))
r3K=[(i,s) for i,(t,c,ss) in enumerate(r3) if c==K for s in ss]
print('r3 K seeds',len(r3K))
for i,s in r3K:
    exact=[x for x in r2K if canon(x)==canon(s)]
    sameops=[x for x in r2K if ops(x)==ops(s)]
    if exact or sameops: print('SEED',s[:90],'EXACT' if exact else '', 'SAMEOPS:',[x[:80] for x in sameops])
