import json, re, csv, yaml, sys, os, warnings
warnings.filterwarnings("ignore")
from partura import ops_ext
from alphacube.plugins import load_plugins
load_plugins(["partura.ac_plugin"])
from partura.steer import Guidance
from alphacube.parser import parse
from alphacube.mining.clustering import skeleton_key
R2 = "/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2040/r2"
G0 = Guidance.load("/Users/wxy/Desktop/Partura-prod/guidance/C05_base.yaml")
loc = json.load(open(R2 + "/loc.json"))
C = "cs_bucket_demean(day_std(Ret), day_cov(Low, log(Amt)))"
E = [
 f"cross_mean({C}, 120)",
 f"cross_stddev({C}, 120)",
 f"cross_hurst({C}, 241)",
 f"cross_corr({C}, ts_delta(log(day_last(Close)), 1), 120)",
 f"cross_regbeta({C}, cs_mean(day_std(Ret)), 120)",
 f"sub(cross_semistd_pos({C}, 120), cross_semistd_neg({C}, 120))",
 f"cross_tail_mean_q75({C}, 241)",
 f"sub(cross_mean({C}, 20), cross_mean({C}, 241))",
 f"cross_argmax({C}, 120)",
 f"cross_mean(cross_rank({C}, 241), 20)",
 f"cross_corr({C}, day_cov(Ret, log(Amt)), 120)",
 f"cross_mean(cross_zscore({C}, 241), 60)",
 f"mul(cs_demean(cs_rank(cross_mean({C}, 60))), cs_demean(cs_rank(cross_stddev({C}, 60))))",
 f"cross_mean(abs_({C}), 120)",
 f"cross_corr({C}, cross_delay({C}, 5), 241)",
 f"cross_regres(cross_mean({C}, 20), cross_mean({C}, 120), 241)",
]
VT = "day_std(in_logchg(Volume, 1))"
N = [
 f"cross_mean(cs_bucket_demean({VT}, day_std(Ret)), 120)",
 f"cross_autocorr_s1(cs_bucket_demean({VT}, day_cov(Low, log(Amt))), 241)",
 f"cross_mean(sub(cs_rank({VT}), cs_rank(day_std(Ret))), 120)",
 f"cross_mean(cross_zscore(sub(cs_rank({VT}), cs_rank(day_std(Ret))), 241), 20)",
 f"cross_corr({VT}, day_std(Ret), 120)",
 f"cross_regbeta({VT}, day_std(Ret), 120)",
 f"cross_stddev(cs_bucket_demean({VT}, day_std(Ret)), 120)",
 f"cross_autocorr_s1({VT}, 241)",
 f"cross_mean(cs_bucket_zscore({VT}, LogFloatCap), 120)",
 f"cross_mean(cs_bucket_demean({VT}, day_std(Ret)), 60)",
 f"sub(cross_mean({VT}, 20), cross_mean({VT}, 241))",
 f"cross_mean(day_gini(Volume), 120)",
 f"cross_hurst({VT}, 241)",
 f"cross_mean(day_signed_ratio(in_logchg(Volume, 1), Ret), 120)",
 f"cross_mean(day_signed_ratio(in_logchg(Volume, 1), Ret), 20)",
 f"cross_mean(cs_bucket_demean(day_signed_ratio(in_logchg(Volume, 1), Ret), day_std(Ret)), 120)",
]
# R: head 5 variants
H = [h["expr"] for h in loc["heads"]]
head5 = [h for h in H if h.startswith("ts_mean(mul(sub(div(day_last(Close), day_first(Open)), 1), add(")][0]
inner = head5[len("ts_mean("):-len(", 20)")]
assert head5 == f"ts_mean({inner}, 20)"
RET = "sub(div(day_last(Close), day_first(Open)), 1)"
assert inner.startswith(f"mul({RET}, add(")
CNT = inner[len(f"mul({RET}, "):-1]
Rv = [
 f"ts_mean({inner}, 60)",
 f"ts_mean({inner}, 120)",
 f"ts_mean(mul(sign({RET}), {CNT}), 60)",
 f"ts_mean(mul({RET}, cs_rank({CNT})), 60)",
 f"ts_mean(cs_bucket_demean({inner}, day_mean(log(Amt))), 60)",
 f"ts_mean(mul(cs_rank({RET}), cs_rank({CNT})), 60)",
]
bad = 0
sk = set(r["skeleton"] for r in csv.DictReader(open("/Users/wxy/Desktop/Partura-prod/research/prod_W02L/struct/members.csv")))
def skel(e):
    t = parse(G0.canonical(e), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
    return re.sub(r"@[\d.]+", "", skeleton_key(t))
for tag, L in (("E", E), ("N", N), ("R", Rv)):
    for i, e in enumerate(L):
        s = skel(e)
        if s in sk:
            print("LIB SKELETON HIT", tag, i + 1, e[:100]); bad += 1
print("done", bad)
HYP_E = open(R2 + "/scratch/hyp_E.txt").read().strip()
HYP_N = open(R2 + "/scratch/hyp_N.txt").read().strip()
WHYR = open(R2 + "/scratch/why_R.txt").read().strip()
plan = {"seed": 2040, "round": 2, "slots": [
  {"type": "E", "core": C, "hypothesis": HYP_E, "seeds": E},
  {"type": "N", "hypothesis": HYP_N, "inspired_by": "B118 / 第 1 轮 N 位的最好候选 cross_autocorr_s1(cs_bucket_demean(day_std(Ret), day_signed_ratio(Low, Ret)), 241)(train +0.26 / valid +0.58,本流唯一正分)和 B119 的成交量跳变计数:慢的、同伴去均值的、读成交量节奏的状态变量。", "seeds": N}],
  "R": [{"head": head5, "why": WHYR, "variants": Rv}]}
yaml.safe_dump(plan, open(R2 + "/missions.yaml", "w"), allow_unicode=True, width=100000, sort_keys=False)
