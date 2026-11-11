import csv, re, sys
FIELDS = {'Ret','Low','High','Open','Close','Volume','Amt','LogFloatCap','LogTotalCap','LogFloatShares','LimitWidth','BoardCode','ListAge'}
def tokenize(s):
    return re.findall(r'[A-Za-z_][A-Za-z_0-9]*|-?\d+(?:\.\d+)?(?:e-?\d+)?|[(),]', s)
def parse(toks):
    pos = 0
    def node():
        nonlocal pos
        t = toks[pos]; pos += 1
        if pos < len(toks) and toks[pos] == '(':
            pos += 1
            args = []
            while toks[pos] != ')':
                args.append(node())
                if toks[pos] == ',': pos += 1
            pos += 1
            return ('op', t, args)
        return ('leaf', t)
    return node()
def skel(n):
    if n[0] == 'leaf':
        t = n[1]
        if t in FIELDS: return 'F'
        if re.match(r'-?\d', t): return None
        return 'F'  # unknown leaf treated as field
    parts = [skel(a) for a in n[2]]
    parts = [p for p in parts if p is not None]
    return 'O:%s(%s)' % (n[1], ','.join(parts))
def skeleton(expr):
    return skel(parse(tokenize(expr)))
if __name__ == '__main__':
    lib = list(csv.DictReader(open('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/struct/members.csv')))
    libsk = {}
    for r in lib:
        libsk.setdefault(r['skeleton'], []).append(r['expression'])
    # test against library: compute my skeleton for lib expressions and compare to their skeleton column
    ok = bad = 0
    for r in lib[:300]:
        try:
            if skeleton(r['expression']) == r['skeleton']: ok += 1
            else: bad += 1
        except Exception as e: bad += 1
    print('self-check ok', ok, 'bad', bad)
    seeds = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    for s in seeds:
        try:
            sk = skeleton(s)
        except Exception as e:
            print('PARSE_FAIL', s[:80]); continue
        hit = sk in libsk
        print('HIT' if hit else 'new ', sk[:110], '|', s[:70])
