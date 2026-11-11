import json, re
base = '/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2004'
seen = set()
def walk(o):
    if isinstance(o, dict):
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
    elif isinstance(o, str) and '(' in o: seen.add(o.strip())
for f in ['r3/loc.json', 'r3/R_prev.json', 'r1/audit_record.json', 'r2/audit_record.json', 'r1/loc.json', 'r2/loc.json', 'r2/R_prev.json', 'r1/corr_1.json', 'r2/corr_1.json']:
    try: walk(json.load(open(f'{base}/{f}')))
    except Exception as e: print('skip', f, e)
for f in ['r1/missions_final.yaml', 'r2/missions_final.yaml']:
    for ln in open(f'{base}/{f}'):
        s = ln.strip()
        if s.startswith('- ') or s.startswith('core:'):
            seen.add(s.lstrip('- ').replace('core: ', '').strip().strip("'\""))
seen = {s for s in seen if '(' in s}
def norm(e, core):
    e = re.sub(r'\s+', '', e); c = re.sub(r'\s+', '', core)
    e = e.replace(c, 'X')
    e = re.sub(r'-?\d+\.\d+|-?\b\d+\b', 'K', e)
    return e
miss = open(f'{base}/r3/missions.yaml').read().splitlines()
slots = []; cur = None
for ln in miss:
    if ln.startswith('- type:'): cur = {'seeds': []}; slots.append(cur)
    elif ln.startswith('  core:') and cur is not None: cur['core'] = ln.split(':', 1)[1].strip()
    elif re.match(r'^  - ', ln) and cur is not None and 'core' in cur: cur['seeds'].append(ln[4:].strip())
for slot in slots:
    core = slot['core']; cn = re.sub(r'\s+', '', core)
    cands = [s for s in seen if cn in re.sub(r'\s+', '', s)]
    print('== core', core, '| previously seen containing core:', len(cands))
    cn_seen = {norm(s, core) for s in cands}
    ex = {re.sub(r'\s+', '', c) for c in cands}
    for i, s in enumerate(slot['seeds'], 1):
        print(i, 'PERIPH_DUP' if norm(s, core) in cn_seen else '-', 'EXACT_DUP' if re.sub(r'\s+','',s) in ex else '-', s[:100])
    if cands:
        print('sample seen:'); [print('   ', c[:140]) for c in cands[:6]]
