import json, re
base = '/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2004'
texts = []
texts.append(open(f'{base}/r3/loc.json').read())
texts.append(open(f'{base}/r3/R_prev.json').read())
for d in ['r1', 'r2']:
    for fn in ['missions_final.yaml', 'audit_1.yaml', 'audit_record.json', 'corr_1.json']:
        try: texts.append(open(f'{base}/{d}/{fn}').read())
        except Exception: pass
# extract expression-like strings: "...(" lines from json/yaml raw text, unescape
raw = '\n'.join(texts).replace('\\"', '"')
seen = set(re.findall(r'((?:cs_|ts_|cross_|day_|add|sub|mul|div|neg|sign|abs_|sigmoid|in_slice|cs_)[A-Za-z_0-9]*\(.*?\)\)?)(?=[\"\'\n,\]]|$)', raw))
def norm(e, core):
    e = e.replace(' ', '')
    e = e.replace(core.replace(' ', ''), 'X')
    e = re.sub(r'-?\d+\.\d+|-?\b\d+\b', 'K', e)
    return e
miss = open(f'{base}/r3/missions.yaml').read().splitlines()
slots = []
cur = None
for ln in miss:
    if ln.startswith('- type:'):
        cur = {'seeds': []}; slots.append(cur)
    elif ln.startswith('  core:') and cur is not None:
        cur['core'] = ln.split(':', 1)[1].strip()
    elif re.match(r'^  - ', ln) and cur is not None and 'core' in cur:
        cur['seeds'].append(ln[4:].strip())
for slot in slots:
    core = slot['core']; cn = core.replace(' ', '')
    cands = [s for s in seen if cn in s.replace(' ', '')]
    cn_seen = {norm(s, core) for s in cands}
    ex = {c.replace(' ', '') for c in cands}
    print('== core', core, '| seen containing core:', len(cands), '| seeds:', len(slot['seeds']))
    for i, s in enumerate(slot['seeds'], 1):
        print(i, 'PERIPH_DUP' if norm(s, core) in cn_seen else '-', 'EXACT_DUP' if s.replace(' ', '') in ex else '-', s[:120])
