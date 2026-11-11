import os,sys,re,csv,warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2034/r2/scratch')
from partura import ops_ext
from alphacube.parser import parse
from alphacube.plugins import load_plugins
from alphacube.mining.clustering import skeleton_key
load_plugins(["partura.ac_plugin"])
import seeds
def P(s): return parse(s,strict=True,coerce_daily=True,n_minutes=241,allow_general=True)
sk=lambda t: re.sub(r"@\d+","",skeleton_key(t))
lib=set(r['skeleton'] for r in csv.DictReader(open('/Users/wxy/Desktop/Partura-prod/research/prod_W02L/struct/members.csv')))
print(len(lib))
for name in ('E_SEEDS','N_SEEDS'):
    for s in getattr(seeds,name):
        try:
            t=P(s); k=sk(t); print(name, 'LIB' if k in lib else 'ok ', s[:100])
        except Exception as e: print(name,'ERR',type(e).__name__,str(e)[:80],s[:90])
