import re
rows=[]
for line in open('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2028/r3/corr_1.md',encoding='utf-8'):
    if not line.startswith('| slot') and not line.startswith('| R '): continue
    cells=[c.strip() for c in line.strip().strip('|').split('|')]
    rows.append(cells)
for c in rows:
    name=c[0]; raw=float(c[2]); resid=float(c[4]); ctrl=[float(x) for x in c[5:10]]
    flags=[]
    if raw>=0.7: flags.append('HEAD>=0.7')
    if any(x>=0.8 for x in ctrl): flags.append('CTRL>=0.8:'+','.join(n for n,x in zip(['liq','vol','rev','known','size'],ctrl) if x>=0.8))
    print(f"{name:12s} raw={raw:.2f} resid={resid:.2f} ctrl={ctrl} {'; '.join(flags)} | {c[-1][:90]}")
