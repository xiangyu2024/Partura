import csv, re, sys
members = set()
with open("/Users/wxy/Desktop/Partura-prod/research/prod_W02L/struct/members.csv", newline="") as f:
    for row in csv.DictReader(f):
        members.add(row["expression"].strip())
txt = open("/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2034/r2/missions.yaml", encoding="utf-8").read()
seeds = re.findall(r"^\s+- ((?:cross|cs|div|sub|log|sign|ts|day|in|abs|mul)[^\n]*)$", txt, flags=re.M)
hits = [s for s in seeds if s.strip() in members]
print("seed-like lines:", len(seeds), "exact library hits:", len(hits))
for h in hits: print("HIT:", h)
# duplicates within plan
from collections import Counter
c = Counter(s.strip() for s in seeds)
print("within-plan duplicates:", [k for k,v in c.items() if v>1])
