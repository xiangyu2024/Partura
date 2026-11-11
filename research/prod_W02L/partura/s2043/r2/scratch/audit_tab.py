import json
d = json.load(open('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2043/r2/corr_1.json'))
rows = d['rows']
print('controls sample', rows[0]['controls'] if not isinstance(rows[0]['controls'], str) else rows[0]['controls'][:200])
for r in rows:
    if r['where'].startswith('slot a') or r['where'].startswith('slot b') or r['where'].startswith('R'):
        c = r['controls']
        ctrl = c if isinstance(c, dict) else None
        cv = [round(v,2) for v in (ctrl.values() if ctrl else [])] if ctrl else c
        flag = []
        if r['max_head'] is not None and r['max_head']>=0.7: flag.append('HEAD>=0.7')
        if ctrl and any(abs(v)>=0.8 for v in ctrl.values()): flag.append('CTRL>=0.8')
        if ctrl and any(0.5<=abs(v)<0.8 for v in ctrl.values()): flag.append('ctrl0.5+')
        if r['max_head_resid'] is not None and r['max_head_resid']>=0.5: flag.append('resid>=0.5')
        print(f"{r['where']:<22} raw={r['max_head']:.2f} res={r['max_head_resid']:.2f} ctrl={cv} {flag} | {r['top_heads'][0] if isinstance(r['top_heads'],list) and r['top_heads'] else ''}"[:260])
