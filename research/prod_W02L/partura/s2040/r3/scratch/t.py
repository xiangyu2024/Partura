import sys,re,csv,warnings
warnings.filterwarnings("ignore")
from partura import ops_ext
from alphacube.plugins import load_plugins
load_plugins(["partura.ac_plugin"])
from partura.steer import Guidance
from alphacube.parser import parse
from alphacube.mining.clustering import skeleton_key
G0=Guidance.load("/Users/wxy/Desktop/Partura-prod/guidance/C05_base.yaml")
sk=set(r["skeleton"] for r in csv.DictReader(open("/Users/wxy/Desktop/Partura-prod/research/prod_W02L/struct/members.csv")))
for l in open(sys.argv[1]):
    e=l.strip()
    if not e: continue
    try:
        t=parse(G0.canonical(e),strict=True,coerce_daily=True,n_minutes=241,allow_general=True)
        s=re.sub(r"@[\d.]+","",skeleton_key(t))
        print("HIT" if s in sk else "new",e[:110])
    except Exception as ex: print("FAIL",type(ex).__name__,str(ex)[:80],e[:80])
