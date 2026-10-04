# audit-numbers:F103_amt_dw_decay — agent a8da7cfad8e5f22d5(工作流 wf_759ef2d3-03f)

- 状态:**已返回结果**;开始 10-03 23:39,最后一次动作 10-03 23:52;工具调用 48 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F103_amt_dw_decay/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-03 23:39 · Bash** — List sizes and files for the F103 study

```bash
cd /Users/wxy/Desktop/Partura && wc -c CLAUDE.md docs/method.md docs/study_playbook.md && ls -la research/alpha_distillation/F103_amt_dw_decay.md notes/F103_amt_dw_decay/ configs/F103_amt_dw_decay.yaml runs/F103_amt_dw_decay/ studies/F103_amt_dw_decay/ 2>&1
```

```
    1635 CLAUDE.md
    6534 docs/method.md
   13287 docs/study_playbook.md
   21456 total
-rw-r--r--@ 1 wxy  staff   14762 Oct  3 23:22 configs/F103_amt_dw_decay.yaml
-rw-r--r--@ 1 wxy  staff  140195 Oct  3 23:36 research/alpha_distillation/F103_amt_dw_decay.md

notes/F103_amt_dw_decay/:
total 264
drwxr-xr-x@ 22 wxy  staff    704 Oct  3 23:34 .
drwxr-xr-x@ 10 wxy  staff    320 Oct  3 18:37 ..
-rw-r--r--@  1 wxy  staff   1660 Oct  3 23:34 01_expression.md
-rw-r--r--@  1 wxy  staff   2737 Oct  3 23:36 02_operators.md
-rw-r--r--@  1 wxy  staff   1675 Oct  3 23:36 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1168 Oct  3 18:39 04_grammar.md
-rw-r--r--@  1 wxy  staff  10998 Oct  3 23:36 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3383 Oct  3 18:44 06_baseline.md
-rw-r--r--@  1 wxy  staff   4148 Oct  3 23:34 07_S1_structure.md
-rw-r--r--@  1 wxy  staff   5103 Oct  3 23:29 07_S2_distil.md
-rw-r--r--@  1 wxy  staff   2173 Oct  3 23:31 07_S_final.md
-rw-r--r--@  1 wxy  staff   1384 Oct  3 23:31 07_conditional.md
-rw-r--r--@  1 wxy  staff    859 Oct  3 23:31 07_controls.md
-rw-r--r--@  1 wxy  staff   2328 Oct  3 23:31 07_neutralise.md
-rw-r--r--@  1 wxy  staff   5582 Oct  3 23:36 07x_x1_anatomy.md
-rw-r--r--@  1 wxy  staff   7523 Oct  3 23:34 07x_x2_interaction.md
-rw-r--r--@  1 wxy  staff  14159 Oct  3 23:36 07x_x3_family.md
-rw-r--r--@  1 wxy  staff   2197 Oct  3 23:32 08_variants.md
-rw-r--r--@  1 wxy  staff   8741 Oct  3 23:33 09_diagnosis.md
-rw-r--r--@  1 wxy  staff   9958 Oct  3 23:34 10_distilled.md
-rw-r--r--@  1 wxy  staff   3045 Oct  3 23:34 11_risks.md
-rw-r--r--@  1 wxy  staff   1556 Oct  3 23:34 12_next.md

runs/F103_amt_dw_decay/:
total 904
drwxr-xr-x@  7 wxy  staff     224 Oct  3 23:26 .
drwxr-xr-x@ 19 wxy  staff     608 Oct  3 17:37 ..
-rw-r--r--@  1 wxy  staff   34269 Oct  3 17:43 S0_baseline.json
-rw-r--r--@  1 wxy  staff  110135 Oct  3 19:34 S1_structure.json
-rw-r--r--@  1 wxy  staff  203127 Oct  3 23:19 S2_distil.json
-rw-r--r--@  1 wxy  staff  100934 Oct  3 23:26 final.json
-rw-r--r--@  1 wxy  staff    4445 Oct  3 23:26 ledger.json

studies/F103_amt_dw_decay/:
total 120
drwxr-xr-x@ 7 wxy  staff    224 Oct  3 22:40 .
drwxr-xr-x@ 9 wxy  staff    288 Oct  3 18:37 ..
drwxr-xr-x@ 3 wxy  staff     96 Oct  3 22:40 __pycache__
-rw-r--r--@ 1 wxy  staff   8411 Oct  3 18:43 probes.py
-rw-r--r--@ 1 wxy  staff  14541 Oct  3 18:46 x1_anatomy.py
-rw-r--r--@ 1 wxy  staff  12787 Oct  3 19:45 x2_interaction.py
-rw-r--r--@ 1 wxy  staff  16074 Oct  3 22:40 x3_family.py
```

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/CLAUDE.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/docs/method.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/configs/F103_amt_dw_decay.yaml`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/runs/F103_amt_dw_decay/ledger.json`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/09_diagnosis.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/10_distilled.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/06_baseline.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S1_structure.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S2_distil.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S_final.md`

**10-03 23:39 · Bash** — Inspect JSON structure of run files

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
for t in ["S0_baseline","S1_structure","S2_distil","final"]:
    d=json.load(open(f"runs/F103_amt_dw_decay/{t}.json"))
    print("=====",t, type(d))
    def walk(o, pre="", depth=0):
        if depth>3: return
        if isinstance(o, dict):
            for k,v in list(o.items())[:40]:
                tp=type(v).__name__
                ln = len(v) if hasattr(v,'__len__') else ''
                print(pre+str(k), tp, ln)
                walk(v, pre+"  ", depth+1)
        elif isinstance(o, list) and o:
            print(pre+"[0]:", type(o[0]).__name__)
            walk(o[0], pre+"  ", depth+1)
    if t=="S0_baseline":
        walk(d)
    else:
        print(list(d.keys()))
EOF
```

```
===== S0_baseline <class 'dict'>
factor_id str 17
config str 30
stages list 1
  [0]: str
provenance dict 11
  alphacube_root str 26
  alphacube_commit str 7
  alphacube_dirty bool 
  partura_root str 24
  partura_commit NoneType 
  partura_code_sha str 12
  store str 51
  python str 6
  torch str 11
  numpy str 5
  host str 36
view dict 5
  days int 
  symbols int 
  first str 8
  last str 8
  warmup_rows int 
label dict 3
  kind str 11
  horizon int 
  buyable bool 
cost_per_side float 
top_frac float 
fit_split str 5
… (375 行略) …
      v_base float 
      ctl_amt float 
      ctl_cap float 
      ctl_turnrate float 
      ctl_ivol float 
      ctl_dvol20 float 
      ctl_price float 
      ctl_rev1 float 
      ctl_mom20 float 
      known_amt_max9 float 
      known_stdamt_max9 float 
      known_ivol_max9 float 
seconds float 
peak_anon_gb float 
===== S1_structure <class 'dict'>
['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
===== S2_distil <class 'dict'>
['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
===== final <class 'dict'>
['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
```

**10-03 23:39 · Bash** — Dump baseline run key numbers

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/S0_baseline.json"))
r=d["results"]["v_base"]
print(json.dumps({k:r[k] for k in ["sign","distinct","sign_user","ic_user"]}, indent=1))
print("splits.train", json.dumps(r["splits"]["train"]))
print("splits.valid", json.dumps(r["splits"]["valid"]))
b=r["books"]
print({k:b[k] for k in ["hl_ls","hl_long","hl_used","rank_by"]})
print("sweep[0]", json.dumps(b["sweep"][0]))
for s in b["sweep"]: print(json.dumps(s))
print("books.splits.train", json.dumps(b["splits"]["train"]))
print("books.splits.valid", json.dumps(b["splits"]["valid"]))
bu=r["books_user"]
print({k:bu[k] for k in ["hl_ls","hl_long","hl_used","rank_by"]})
print("books_user.splits", json.dumps(bu["splits"]))
print("profile train", r["profile"]["train"])
print("profile valid", r["profile"]["valid"])
print("errors", d["errors"], d["splits_used"], d["split_dates"], d["view"])
EOF
```

```
{
 "sign": -1.0,
 "distinct": 1.0,
 "sign_user": -1.0,
 "ic_user": {
  "sign": -1.0,
  "ic": 0.01736094212285439,
  "icir": 0.3995027372639804,
  "ic_t": 14.727515472531007,
  "rank_ic": 0.03604187165066998,
  "rank_icir": 0.43559260236171715,
  "rank_ic_t": 16.057954533521134,
  "ic_pos": 0.6835908756438558,
  "coverage": 0.7489171100003101,
  "coverage_labelled": 0.9993169233675563,
  "n_days": 1359
 }
}
splits.train {"sign": -1.0, "ic": 0.01930447112968993, "icir": 0.4461308144289802, "ic_t": 13.916135260420633, "rank_ic": 0.03927507962238811, "rank_icir": 0.5113378874076997, "rank_ic_t": 15.950136091924357, "ic_pos": 0.6988694758478932, "coverage": 0.6910973684106901, "coverage_labelled": 0.99920783881081, "n_days": 973}
splits.valid {"sign": -1.0, "ic": 0.012461839211841491, "icir": 0.28623428195305745, "ic_t": 5.623611363506585, "rank_ic": 0.027891842229732837, "rank_icir": 0.29174670459111784, "rank_ic_t": 5.731913284493574, "ic_pos": 0.6450777202072538, "coverage": 0.8946648005876163, "coverage_labelled": 0.99953254311404, "n_days": 386}
{'hl_ls': 2.0, 'hl_long': 10.0, 'hl_used': 2.0, 'rank_by': 'ls'}
sweep[0] {"halflife": 0.0, "ls_sharpe": 3.3750322675479736, "ls_turnover": 0.144644683065276, "long_sharpe": -0.37524850957327494, "long_ann": -0.01755374794315422, "long_turnover": 0.17655013358925503}
{"halflife": 0.0, "ls_sharpe": 3.3750322675479736, "ls_turnover": 0.144644683065276, "long_sharpe": -0.37524850957327494, "long_ann": -0.01755374794315422, "long_turnover": 0.17655013358925503}
{"halflife": 1.0, "ls_sharpe": 3.864072418434949, "ls_turnover": 0.10620211491097521, "long_sharpe": 0.6942149476111857, "long_ann": 0.03296452634972016, "long_turnover": 0.12200093985382299}
{"halflife": 2.0, "ls_sharpe": 4.140099556007619, "ls_turnover": 0.0846286672145119, "long_sharpe": 1.3007527947576831, "long_ann": 0.06313273616157833, "long_turnover": 0.0946738035577815}
{"halflife": 3.0, "ls_sharpe": 4.118134828642816, "ls_turnover": 0.07134759051811583, "long_sharpe": 1.5054343057419572, "long_ann": 0.07428313884247581, "long_turnover": 0.07929847365551145}
{"halflife": 5.0, "ls_sharpe": 4.125887197273392, "ls_turnover": 0.05513930730926454, "long_sharpe": 1.6218134261075428, "long_ann": 0.08143636965583276, "long_turnover": 0.0608812068350697}
{"halflife": 10.0, "ls_sharpe": 4.088846214643805, "ls_turnover": 0.036315955501275074, "long_sharpe": 1.856415056753809, "long_ann": 0.09414766345868725, "long_turnover": 0.03994329627652811}
{"halflife": 20.0, "ls_sharpe": 3.9549559476799425, "ls_turnover": 0.023208655920739035, "long_sharpe": 1.8554272009905803, "long_ann": 0.09490147024575975, "long_turnover": 0.02544357631099258}
books.splits.train {"ls_sharpe": 4.140099556007619, "ls_ann": 0.21726359515785693, "ls_mdd": -0.05626223295186705, "ls_gross_sharpe": 5.361152673239745, "ls_turnover": 0.0846286672145119, "long_sharpe": 1.3007527947576831, "long_ann": 0.06313273616157833, "long_mdd": -0.08898925579856995, "long_gross_ann": 0.13470613165126114, "long_turnover": 0.0946738035577815, "short_gross_ann": 0.4277796034927946, "long_share": 0.23948364062381447, "n_days": 973}
books.splits.valid {"ls_sharpe": 2.2157289640262485, "ls_ann": 0.13335882619364375, "ls_mdd": -0.031115999798776994, "ls_gross_sharpe": 3.2777422848407887, "ls_turnover": 0.08455823361383448, "long_sha
… (1585 字符略) …
: 8, 'excess_ann': 0.10494488540514943, 'sharpe': 3.5366066655797868, 'win': 0.6012332990750257}, {'quantile': 9, 'excess_ann': 0.12980485102134467, 'sharpe': 3.5507058610333986, 'win': 0.6012332990750257}, {'quantile': 10, 'excess_ann': 0.13807095072263487, 'sharpe': 2.806422612367524, 'win': 0.5858170606372045}]
profile valid [{'quantile': 1, 'excess_ann': -0.29100282898397795, 'sharpe': -3.803482553130161, 'win': 0.39896373056994816}, {'quantile': 2, 'excess_ann': -0.0825812495287725, 'sharpe': -1.932982785859959, 'win': 0.46113989637305697}, {'quantile': 3, 'excess_ann': -0.03507037745682831, 'sharpe': -1.1541442171839797, 'win': 0.47150259067357514}, {'quantile': 4, 'excess_ann': -0.012403955639197786, 'sharpe': -0.49592018864388243, 'win': 0.49222797927461137}, {'quantile': 5, 'excess_ann': 0.03905101821419764, 'sharpe': 2.0872156791698755, 'win': 0.5544041450777202}, {'quantile': 6, 'excess_ann': 0.04115800277858686, 'sharpe': 1.9848498443769405, 'win': 0.5518134715025906}, {'quantile': 7, 'excess_ann': 0.06215753484083718, 'sharpe': 2.764094328824258, 'win': 0.538860103626943}, {'quantile': 8, 'excess_ann': 0.07598195921608651, 'sharpe': 2.5327167933605153, 'win': 0.5544041450777202}, {'quantile': 9, 'excess_ann': 0.08434537851846909, 'sharpe': 2.1212422370878583, 'win': 0.5518134715025906}, {'quantile': 10, 'excess_ann': 0.11876882141270446, 'sharpe': 1.9878403329308543, 'win': 0.5518134715025906}]
errors {} ['train', 'valid', 'utrain'] {'train': ['20180102', '20211231'], 'valid': ['20220104', '20230807'], 'utrain': ['20180102', '20230807']} {'days': 1942, 'symbols': 5220, 'first': '20180102', 'last': '20251231', 'warmup_rows': 0}
```

**10-03 23:39 · Bash** — Dump baseline diagnostics

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/S0_baseline.json"))
dg=d["diagnostics"]
print("decay", json.dumps(dg["decay"]["v_base"]))
print("by_year_scope", dg["by_year_scope"])
for y in dg["by_year"]["v_base"]: print(json.dumps(y))
for k,v in dg["neutralise"]["v_base"].items(): print(k, json.dumps(v))
for k,v in dg["conditional"].items(): 
    print(k)
    for b in v: print("   ", json.dumps(b))
for k,v in dg["controls"].items(): print(k, json.dumps(v))
print("rank_corr v_base", json.dumps(dg["rank_corr_train"]["v_base"]))
EOF
```

```
decay [{"horizon": 1, "ic": 0.01930447112968993, "rank_ic": 0.03927507962238811}, {"horizon": 2, "ic": 0.02375055162142292, "rank_ic": 0.049661992918605145}, {"horizon": 3, "ic": 0.026098026349039113, "rank_ic": 0.05505781617546809}, {"horizon": 5, "ic": 0.027829739956347358, "rank_ic": 0.0623391774965781}, {"horizon": 10, "ic": 0.027887199219648173, "rank_ic": 0.07257044691620672}, {"horizon": 20, "ic": 0.027515996429754885, "rank_ic": 0.0802461071438728}]
by_year_scope ['20180102', '20230807']
{"year": "2018", "days": 243, "ls_sharpe": 5.425011648982146, "ls_ann": 0.22957732743895806, "ls_mdd": -0.012669695263476055, "ls_gross_sharpe": 6.8146067600593385, "ls_turnover": 0.07747597724136403, "long_sharpe": 0.4317823768015853, "long_ann": 0.019027698391098916, "long_mdd": -0.04326497846913192, "long_gross_ann": 0.08026292019504809, "long_turnover": 0.08099897064014441, "short_gross_ann": 0.4960354122718103, "long_share": 0.1392732126283982, "n_days": 243}
{"year": "2019", "days": 244, "ls_sharpe": 6.2172611367842885, "ls_ann": 0.2898594574640199, "ls_mdd": -0.025817908942980677, "ls_gross_sharpe": 7.629000768884769, "ls_turnover": 0.0868698806854787, "long_sharpe": 3.5342713440655227, "long_ann": 0.15232814742226827, "long_mdd": -0.04648954635248418, "long_gross_ann": 0.22604649334959634, "long_turnover": 0.0975110395864128, "short_gross_ann": 0.4850196811748873, "long_share": 0.3178979699052089, "n_days": 244}
{"year": "2020", "days": 243, "ls_sharpe": 4.193698007032747, "ls_ann": 0.23543809931489895, "ls_mdd": -0.027172387685482607, "ls_gross_sharpe": 5.417817478301172, "ls_turnover": 0.09126084731161532, "long_sharpe": 2.404433879144187, "long_ann": 0.11603638707759736, "long_mdd": -0.033267511535506736, "long_gross_ann": 0.19554161543857287, "long_turnover": 0.10516564598012634, "short_gross_ann": 0.4133209843263874, "long_share": 0.32115885507511543, "n_days": 243}
{"year": "2021", "days": 243, "ls_sharpe": 1.7767491152079342, "ls_ann": 0.10994724061113804, "ls_mdd": -0.05626223295186665, "ls_gross_sharpe": 2.8545419812013475, "ls_turnover": 0.0881017926324581, "long_sharpe": -0.690760936943479, "long_ann": -0.039102171799429146, "long_mdd": -0.0889892557985699, "long_gross_ann": 0.03659761135969424, "long_turnover": 0.10013198830571875, "short_gross_ann": 0.3165067803228585, "long_share": 0.10364530213092381, "n_days": 243}
{"year": "2022", "days": 242, "ls_sharpe": 2.8691807275307344, "ls_ann": 0.1676962333620599, "ls_mdd": -0.029177739164886946, "ls_gross_sharpe": 3.956612577808362, "ls_turnover": 0.08412992005046058, "long_sharpe": 1.1666355977447966, "long_ann": 0.06517806508529674, "long_mdd": -0.041941186575589776, "long_gross_ann": 0.1381138276089662, "long_turnover": 0.09647587635406012, "short_gross_ann": 0.3244830782314499, "long_share": 0.2985619355971479, "n_days": 242}
{"year": "2023", "days": 144, "ls_sharpe": 1.1696578865908482, "ls_ann": 0.07352527423444143, "ls_mdd": -0.031115999798776977, "ls_gross_sharpe": 2.2303308517700486, "ls_turnover": 0.08809236583766235, "long_sharpe": -0.2853843677955651, "long_ann": -0.014769429929816235, "long_mdd": -0.03047317247781628, "long_gross_ann": 0.06107401324174984, "long_turnover": 0.10032201477720382, "short_gross_ann": 0.21917219237367852, "long_share": 0.21792984888994174, "n_days": 144}
_traded_signal {"r2"
… (8774 字符略) …
rnover": 0.04161295482165419}
known_amt_max9 {"sign": -1.0, "rank_ic": 0.04151487266256518, "hl": 1.0, "train_ls_sharpe": 1.5678328930299816, "train_long_gross_ann": 0.1344561018992434, "train_long_ann": 0.08517527808663454, "train_ls_turnover": 0.054211529741068416, "valid_ls_sharpe": 3.8056108653256118, "valid_long_gross_ann": 0.2508343519200948, "valid_long_ann": 0.20817596736131294, "valid_ls_turnover": 0.050465172829920114}
known_stdamt_max9 {"sign": -1.0, "rank_ic": 0.0484292888234746, "hl": 0.0, "train_ls_sharpe": 2.471861888081681, "train_long_gross_ann": 0.1687062482657276, "train_long_ann": 0.09259463886003778, "train_ls_turnover": 0.08533236470913423, "valid_ls_sharpe": 4.437308958830845, "valid_long_gross_ann": 0.24917042375926737, "valid_long_ann": 0.1846945257522087, "valid_ls_turnover": 0.07725156941719918}
known_ivol_max9 {"sign": -1.0, "rank_ic": 0.050072459114398504, "hl": 10.0, "train_ls_sharpe": 1.6565157009177744, "train_long_gross_ann": -0.005149619993557228, "train_long_ann": -0.028122348265460513, "train_ls_turnover": 0.03543480532217956, "valid_ls_sharpe": 2.0614230826787154, "valid_long_gross_ann": 0.0612936669182833, "valid_long_ann": 0.03912054888448869, "valid_ls_turnover": 0.033774821443558554}
rank_corr v_base {"v_base": 1.0, "ctl_amt": 0.2813299190900311, "ctl_cap": 0.10060383599471757, "ctl_turnrate": 0.18947820219676115, "ctl_ivol": 0.26806840984936964, "ctl_dvol20": 0.17631529613697203, "ctl_price": -0.025598990772217008, "ctl_rev1": -0.007365150238598327, "ctl_mom20": 0.2625262700094036, "known_amt_max9": 0.3131131343273983, "known_stdamt_max9": 0.4118974628512611, "known_ivol_max9": 0.32510411443145987}
```

**10-03 23:40 · Bash** — Dump S1 run results table

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/S1_structure.json"))
print("errors", d["errors"], d["splits_used"], d["fit_split"], d["user_split"])
print(list(d["diagnostics"].keys()))
R=d["results"]
print(list(R.keys()))
def row(k, r):
    b=r["books"]; tr=b["splits"]["train"]; va=b["splits"]["valid"]
    s=r["splits"]
    print(f"{k:14s} sign={r['sign']:+.0f} hl={b['hl_used']:>4} dist={r['distinct']:.3f} cov={s['train']['coverage_labelled']:.4f} rIC tr/va={s['train']['rank_ic']:.4f}/{s['valid']['rank_ic']:.4f} "
          f"LS={tr['ls_sharpe']:+.2f}/{va['ls_sharpe']:+.2f} Lg={tr['long_gross_ann']*100:+.1f}/{va['long_gross_ann']*100:+.1f} Ln={tr['long_ann']*100:+.1f}/{va['long_ann']*100:+.1f} Lsh={tr['long_sharpe']:+.2f}/{va['long_sharpe']:+.2f} TO={tr['ls_turnover']*100:.1f}/{va['ls_turnover']*100:.1f} lshare={tr['long_share']:.2f}/{va['long_share']:.2f}")
    if "books_user" in r:
        u=r["books_user"]["splits"]["utrain"]
        print(f"     USER sign={r.get('sign_user')} hl={r['books_user']['hl_used']} LS={u['ls_sharpe']:+.2f} Lg={u['long_gross_ann']*100:+.1f} Ln={u['long_ann']*100:+.1f} Lsh={u['long_sharpe']:+.2f} TO={u['ls_turnover']*100:.1f}")
for k,r in R.items(): row(k,r)
dg=d["diagnostics"]
rc=dg["rank_corr_train"]
print(list(rc.keys()))
for k in R:
    if k in rc:
        print(k, {kk: round(vv,2) for kk,vv in rc[k].items() if kk in ("v_base","ref_base","ctl_amt","known_amt_max9","known_stdamt_max9","ctl_cap")})
EOF
```

```
errors {} ['train', 'valid', 'utrain'] train utrain
['decay', 'by_year', 'by_year_scope', 'neutralise', 'conditional', 'rank_corr_train']
['a_no_tsmin', 'a_A5', 'a_C', 'e_pow1', 'e_pow2', 'm_none', 'm_mean5', 'f_sum', 'f_share', 'i_rankmul', 'i_addrank']
a_no_tsmin     sign=-1 hl= 2.0 dist=1.000 cov=0.9992 rIC tr/va=0.0393/0.0279 LS=+4.14/+2.22 Lg=+13.5/+10.9 Ln=+6.3/+3.6 Lsh=+1.30/+0.66 TO=8.5/8.5 lshare=0.24/0.28
a_A5           sign=-1 hl= 3.0 dist=0.998 cov=0.9992 rIC tr/va=0.0448/0.0613 LS=+1.81/+3.69 Lg=+12.9/+23.5 Ln=+7.1/+18.0 Lsh=+1.01/+3.05 TO=6.3/6.1 lshare=0.33/0.39
a_C            sign=-1 hl= 1.0 dist=1.000 cov=0.9992 rIC tr/va=0.0051/-0.0322 LS=+1.79/-1.75 Lg=+8.7/-16.7 Ln=+4.6/-21.1 Lsh=+0.46/-2.42 TO=6.1/6.4 lshare=0.24/1.07
e_pow1         sign=-1 hl= 3.0 dist=1.000 cov=0.9992 rIC tr/va=0.0477/0.0548 LS=+2.70/+3.63 Lg=+12.4/+21.0 Ln=+5.8/+14.3 Lsh=+0.97/+2.75 TO=7.4/7.2 lshare=0.25/0.36
e_pow2         sign=-1 hl= 3.0 dist=1.000 cov=0.9992 rIC tr/va=0.0449/0.0422 LS=+3.60/+3.12 Lg=+13.3/+16.4 Ln=+6.6/+9.6 Lsh=+1.35/+1.94 TO=7.7/7.5 lshare=0.25/0.33
m_none         sign=-1 hl= 5.0 dist=0.999 cov=0.9992 rIC tr/va=0.0435/0.0317 LS=+4.35/+2.41 Lg=+13.5/+10.8 Ln=+7.1/+4.1 Lsh=+1.44/+0.73 TO=7.0/7.1 lshare=0.24/0.27
m_mean5        sign=-1 hl= 3.0 dist=1.000 cov=0.9992 rIC tr/va=0.0406/0.0299 LS=+4.26/+2.49 Lg=+13.2/+11.8 Ln=+7.8/+6.2 Lsh=+1.57/+1.11 TO=6.5/6.5 lshare=0.24/0.29
f_sum          sign=-1 hl=10.0 dist=1.000 cov=0.9992 rIC tr/va=0.0417/0.0362 LS=+3.79/+2.77 Lg=+12.5/+10.6 Ln=+9.5/+7.4 Lsh=+1.89/+1.40 TO=3.7/3.8 lshare=0.26/0.27
f_share        sign=-1 hl= 3.0 dist=1.000 cov=0.9992 rIC tr/va=0.0060/-0.0293 LS=+1.52/-1.96 Lg=+9.8/-13.7 Ln=+6.2/-17.7 Lsh=+0.60/-1.95 TO=5.0/5.5 lshare=0.33/0.68
i_rankmul      sign=-1 hl= 0.0 dist=1.000 cov=0.9992 rIC tr/va=0.0341/0.0103 LS=+2.77/-0.08 Lg=+8.3/-8.2 Ln=+0.2/-16.3 Lsh=+0.03/-2.28 TO=11.0/10.6 lshare=0.16/-0.54
i_addrank      sign=-1 hl= 2.0 dist=0.729 cov=0.9992 rIC tr/va=0.0418/0.0239 LS=+4.01/+1.81 Lg=+15.1/+10.5 Ln=+7.6/+3.2 Lsh=+1.71/+0.61 TO=9.4/9.0 lshare=0.27/0.30
['a_no_tsmin', 'a_A5', 'a_C', 'e_pow1', 'e_pow2', 'm_none', 'm_mean5', 'f_sum', 'f_share', 'i_rankmul', 'i_addrank', 'ctl_amt', 'ctl_cap', 'ctl_turnrate', 'ctl_ivol', 'ctl_dvol20', 'ctl_price', 'ctl_rev1', 'ctl_mom20', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'ref_base', 'ref_A5', 'ref_C']
a_no_tsmin {'ctl_amt': 0.28, 'ctl_cap': 0.1, 'known_amt_max9': 0.31, 'known_stdamt_max9': 0.41, 'ref_base': 1.0}
a_A5 {'ctl_amt': 0.87, 'ctl_cap': 0.47, 'known_amt_max9': 0.88, 'known_stdamt_max9': 0.86, 'ref_base': 0.5}
a_C {'ctl_amt': -0.54, 'ctl_cap': -0.38, 'known_amt_max9': -0.52, 'known_stdamt_max9': -0.39, 'ref_base': 0.49}
e_pow1 {'ctl_amt': 0.74, 'ctl_cap': 0.38, 'known_amt_max9': 0.76, 'known_stdamt_max9': 0.79, 'ref_base': 0.77}
e_pow2 {'ctl_amt': 0.51, 'ctl_cap': 0.24, 'known_amt_max9': 0.54, 'known_stdamt_max9': 0.61, 'ref_base': 0.95}
m_none {'ctl_amt': 0.36, 'ctl_cap': 0.12, 'known_amt_max9': 0.35, 'known_stdamt_max9': 0.43, 'ref_base': 0.84}
m_mean5 {'ctl_amt': 0.33, 'ctl_cap': 0.12, 'known_amt_max9': 0.36, 'known_stdamt_max9': 0.46, 'ref_base': 0.98}
f_sum {'ctl_amt': 0.42, 'ctl_cap': 0.21, 'known_amt_max9': 0.45, 'known_stdamt_max9': 0.55, 'ref_base': 0.89}
f_share {'ctl_amt': -0.53, 'ctl_cap': -0.4, 'known_amt_max9': -0.5, 'known_stdamt_max9': -0.38, 'ref_base': 0.56}
i_rankmul {'ctl_amt': 0.04, 'ctl_cap': -0.11, 'known_amt_max9': 0.06, 'known_stdamt_max9': 0.17, 'ref_base': 0.81}
i_addrank {'ctl_amt': 0.29, 'ctl_cap': 0.1, 'known_amt_max9': 0.32, 'known_stdamt_max9': 0.42, 'ref_base': 0.95}
```

**10-03 23:40 · Bash** — Dump S1 diagnostics

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/S1_structure.json"))
dg=d["diagnostics"]
print("by_year_scope", dg["by_year_scope"], list(dg["by_year"].keys()))
for k,v in dg["by_year"].items():
    print(k, [(y["year"], round(y["ls_sharpe"],2), round(y["long_ann"]*100,1)) for y in v])
print("neutralise keys", list(dg["neutralise"].keys()))
for k,v in dg["neutralise"].items():
    for c in ["_traded_signal","all_controls","ctl_amt","ctl_cap"]:
        x=v[c]
        print(k, c, {kk: round(vv,4) for kk,vv in x.items()})
print("conditional keys", list(dg["conditional"].keys()))
for k,v in dg["conditional"].items():
    print(k, [round(b["rank_ic"],4) for b in v])
print("decay keys", list(dg["decay"].keys()))
R=d["results"]
print("a_C profile train", [round(q["excess_ann"]*100,1) for q in R["a_C"].get("profile",{}).get("train",[])])
print("a_C profile valid", [round(q["excess_ann"]*100,1) for q in R["a_C"].get("profile",{}).get("valid",[])])
for k in R:
    print(k, "has profile" , "profile" in R[k], "books_user" in R[k])
EOF
```

```
by_year_scope ['20180102', '20230807'] ['a_C', 'a_A5']
a_C [('2018', 1.85, -6.7), ('2019', 4.08, 14.6), ('2020', 3.34, 25.1), ('2021', -0.7, -15.2), ('2022', -1.03, -15.7), ('2023', -3.44, -30.4)]
a_A5 [('2018', 3.38, 14.1), ('2019', 2.27, 7.8), ('2020', 0.49, -1.5), ('2021', 1.68, 7.4), ('2022', 4.22, 20.9), ('2023', 2.87, 12.8)]
neutralise keys ['a_C', 'a_A5']
a_C _traded_signal {'r2': 0.0, 'rank_ic': 0.0045, 'rank_icir': 0.0359, 'ls_sharpe': 1.7885, 'ls_gross_sharpe': 2.4087, 'long_gross_ann': 0.0869, 'short_gross_ann': 0.2691, 'long_ann': 0.0457, 'ls_turnover': 0.0606}
a_C all_controls {'r2': 0.4596, 'rank_ic': 0.0162, 'rank_icir': 0.2494, 'ls_sharpe': 1.0534, 'ls_gross_sharpe': 5.4698, 'long_gross_ann': 0.0815, 'short_gross_ann': 0.3509, 'long_ann': -0.1093, 'ls_turnover': 0.2262, 'r2_raw_panel': 0.4575}
a_C ctl_amt {'r2': 0.2966, 'rank_ic': 0.0247, 'rank_icir': 0.2486, 'ls_sharpe': 1.9772, 'ls_gross_sharpe': 4.5443, 'long_gross_ann': 0.071, 'short_gross_ann': 0.4655, 'long_ann': -0.0862, 'ls_turnover': 0.2}
a_C ctl_cap {'r2': 0.1486, 'rank_ic': 0.0042, 'rank_icir': 0.0327, 'ls_sharpe': 1.6696, 'ls_gross_sharpe': 2.3511, 'long_gross_ann': 0.0775, 'short_gross_ann': 0.2605, 'long_ann': 0.0286, 'ls_turnover': 0.0648}
a_A5 _traded_signal {'r2': 0.0, 'rank_ic': 0.0392, 'rank_icir': 0.3168, 'ls_sharpe': 1.8057, 'ls_gross_sharpe': 2.388, 'long_gross_ann': 0.1289, 'short_gross_ann': 0.2594, 'long_ann': 0.0707, 'ls_turnover': 0.0626}
a_A5 all_controls {'r2': 0.8074, 'rank_ic': 0.0123, 'rank_icir': 0.3173, 'ls_sharpe': -7.0614, 'ls_gross_sharpe': 1.8737, 'long_gross_ann': -0.0145, 'short_gross_ann': 0.1273, 'long_ann': -0.3071, 'ls_turnover': 0.3486, 'r2_raw_panel': 0.7793}
a_A5 ctl_amt {'r2': 0.7476, 'rank_ic': 0.0101, 'rank_icir': 0.1504, 'ls_sharpe': -5.524, 'ls_gross_sharpe': 1.9322, 'long_gross_ann': -0.0066, 'short_gross_ann': 0.1636, 'long_ann': -0.3548, 'ls_turnover': 0.4018}
a_A5 ctl_cap {'r2': 0.259, 'rank_ic': 0.0452, 'rank_icir': 0.3453, 'ls_sharpe': 2.0719, 'ls_gross_sharpe': 2.6561, 'long_gross_ann': 0.055, 'short_gross_ann': 0.4261, 'long_ann': -0.002, 'ls_turnover': 0.07}
conditional keys ['a_C|ref_A5', 'a_A5|ref_C', 'a_C|ctl_amt']
a_C|ref_A5 [-0.0019, -0.0064, -0.015, -0.03, -0.0514]
a_A5|ref_C [-0.0142, -0.0396, -0.0542, -0.0599, -0.0688]
a_C|ctl_amt [-0.0028, -0.008, -0.0187, -0.0355, -0.0611]
decay keys ['a_C', 'a_A5']
a_C profile train [-27.2, -3.3, 1.7, 2.4, 3.6, 3.3, 2.6, 3.4, 4.6, 8.9]
a_C profile valid [-0.1, 15.0, 9.9, 6.0, 3.7, 0.6, -2.8, -6.4, -9.0, -17.1]
a_no_tsmin has profile False False
a_A5 has profile True False
a_C has profile True False
e_pow1 has profile True False
e_pow2 has profile False False
m_none has profile False False
m_mean5 has profile False False
f_sum has profile False False
f_share has profile False False
i_rankmul has profile False False
i_addrank has profile False False
```

**10-03 23:40 · Bash** — Dump S2 run results table

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/S2_distil.json"))
print("errors", d["errors"], d["splits_used"], d["fit_split"], d["user_split"])
print(list(d["diagnostics"].keys()))
R=d["results"]
print(list(R.keys()))
def row(k, r):
    b=r["books"]; tr=b["splits"]["train"]; va=b["splits"]["valid"]
    s=r["splits"]
    print(f"{k:14s} sign={r['sign']:+.0f} hl={b['hl_used']:>4} dist={r['distinct']:.3f} cov={s['train']['coverage_labelled']:.4f} rIC tr/va={s['train']['rank_ic']:.4f}/{s['valid']['rank_ic']:.4f} "
          f"LS={tr['ls_sharpe']:+.2f}/{va['ls_sharpe']:+.2f} Lg={tr['long_gross_ann']*100:+.1f}/{va['long_gross_ann']*100:+.1f} Ln={tr['long_ann']*100:+.1f}/{va['long_ann']*100:+.1f} Lsh={tr['long_sharpe']:+.2f}/{va['long_sharpe']:+.2f} TO={tr['ls_turnover']*100:.1f}/{va['ls_turnover']*100:.1f} lshare={tr['long_share']:.2f}/{va['long_share']:.2f}")
    if "books_user" in r:
        u=r["books_user"]["splits"]["utrain"]
        print(f"     USER sign={r.get('sign_user')} hl={r['books_user']['hl_used']} LS={u['ls_sharpe']:+.2f} Lg={u['long_gross_ann']*100:+.1f} Ln={u['long_ann']*100:+.1f} Lsh={u['long_sharpe']:+.2f} TO={u['ls_turnover']*100:.1f}")
for k,r in R.items(): row(k,r)
dg=d["diagnostics"]
rc=dg["rank_corr_train"]
for k in R:
    if k in rc:
        print(k, {kk: round(vv,2) for kk,vv in rc[k].items() if kk in ("ref_base","ctl_amt","known_stdamt_max9","ctl_cap")})
print("x_std9_k1 sweep")
for s in R["x_std9_k1"]["books"]["sweep"]: print("  ", {k: round(v,4) for k,v in s.items()})
print("d_sum_k2 sweep")
for s in R["d_sum_k2"]["books"]["sweep"]: print("  ", {k: round(v,4) for k,v in s.items()})
EOF
```

```
errors {} ['train', 'valid', 'utrain'] train utrain
['decay', 'by_year', 'by_year_scope', 'neutralise', 'conditional', 'rank_corr_train']
['d_sum_k3', 'd_sum_k2', 'd_sum_k1', 'd_amt', 'b_stdamt9', 'x_std9_k1', 'x_std9_k2', 'e_peak_k2', 'x_std9_pk2', 'g_stdB', 'x_std9_k1_w15', 'x_std9_k1_w60']
d_sum_k3       sign=-1 hl=20.0 dist=1.000 cov=0.9992 rIC tr/va=0.0410/0.0336 LS=+3.93/+2.88 Lg=+13.1/+9.8 Ln=+11.1/+7.5 Lsh=+2.24/+1.45 TO=2.4/2.5 lshare=0.29/0.27
     USER sign=-1.0 hl=10.0 LS=+3.64 Lg=+11.8 Ln=+8.4 Lsh=+1.66 TO=3.9
d_sum_k2       sign=-1 hl=10.0 dist=1.000 cov=0.9992 rIC tr/va=0.0464/0.0491 LS=+3.33/+3.78 Lg=+14.9/+17.9 Ln=+11.4/+14.5 Lsh=+1.98/+2.70 TO=4.0/3.8 lshare=0.28/0.33
     USER sign=-1.0 hl=10.0 LS=+3.45 Lg=+15.7 Ln=+12.3 Lsh=+2.18 TO=3.9
d_sum_k1       sign=-1 hl=10.0 dist=1.000 cov=0.9992 rIC tr/va=0.0474/0.0604 LS=+2.36/+3.97 Lg=+15.4/+23.3 Ln=+12.5/+20.7 Lsh=+1.83/+3.37 TO=3.3/3.1 lshare=0.35/0.38
     USER sign=-1.0 hl=10.0 LS=+2.77 Lg=+17.7 Ln=+14.9 Lsh=+2.24 TO=3.2
d_amt          sign=-1 hl= 5.0 dist=1.000 cov=0.9992 rIC tr/va=0.0419/0.0646 LS=+1.42/+3.68 Lg=+13.0/+24.2 Ln=+9.4/+21.0 Lsh=+1.28/+3.28 TO=4.0/3.8 lshare=0.42/0.40
     USER sign=-1.0 hl=5.0 LS=+1.98 Lg=+16.2 Ln=+12.7 Lsh=+1.79 TO=3.9
b_stdamt9      sign=-1 hl= 0.0 dist=1.000 cov=0.9992 rIC tr/va=0.0484/0.0671 LS=+2.47/+4.44 Lg=+16.9/+24.9 Ln=+9.3/+18.5 Lsh=+1.37/+3.09 TO=8.5/7.7 lshare=0.31/0.34
     USER sign=-1.0 hl=0.0 LS=+2.94 Lg=+19.2 Ln=+11.9 Lsh=+1.82 TO=8.3
x_std9_k1      sign=-1 hl= 2.0 dist=1.000 cov=0.9992 rIC tr/va=0.0512/0.0603 LS=+3.32/+4.36 Lg=+17.5/+23.2 Ln=+11.5/+17.7 Lsh=+1.92/+3.25 TO=7.1/6.6 lshare=0.29/0.35
     USER sign=-1.0 hl=2.0 LS=+3.58 Lg=+19.1 Ln=+13.3 Lsh=+2.27 TO=6.9
x_std9_k2      sign=-1 hl= 2.0 dist=1.000 cov=0.9992 rIC tr/va=0.0476/0.0466 LS=+4.16/+3.72 Lg=+15.5/+18.3 Ln=+9.0/+11.9 Lsh=+1.79/+2.47 TO=7.7/7.5 lshare=0.24/0.32
     USER sign=-1.0 hl=2.0 LS=+4.04 Lg=+16.3 Ln=+9.8 Lsh=+1.98 TO=7.6
e_peak_k2      sign=-1 hl= 5.0 dist=1.000 cov=0.9992 rIC tr/va=0.0533/0.0625 LS=+3.10/+3.97 Lg=+17.4/+18.9 Ln=+13.6/+15.5 Lsh=+2.06/+2.70 TO=4.6/4.2 lshare=0.30/0.30
     USER sign=-1.0 hl=5.0 LS=+3.32 Lg=+17.8 Ln=+14.1 Lsh=+2.22 TO=4.4
x_std9_pk2     sign=-1 hl= 2.0 dist=1.000 cov=0.9992 rIC tr/va=0.0548/0.0610 LS=+3.73/+4.04 Lg=+18.6/+20.0 Ln=+13.3/+15.2 Lsh=+2.20/+2.78 TO=6.5/5.9 lshare=0.28/0.32
     USER sign=-1.0 hl=2.0 LS=+3.81 Lg=+19.0 Ln=+13.9 Lsh=+2.35 TO=6.3
g_stdB         sign=-1 hl= 0.0 dist=1.000 cov=0.9992 rIC tr/va=0.0424/0.0631 LS=+2.22/+4.07 Lg=+17.0/+22.7 Ln=+13.6/+19.8 Lsh=+1.90/+3.20 TO=3.9/3.5 lshare=0.38/0.35
     USER sign=-1.0 hl=0.0 LS=+2.67 Lg=+18.6 Ln=+15.4 Lsh=+2.23 TO=3.8
x_std9_k1_w15  sign=-1 hl= 1.0 dist=1.000 cov=0.9992 rIC tr/va=0.0498/0.0587 LS=+3.41/+4.34 Lg=+19.1/+24.3 Ln=+10.5/+16.6 Lsh=+1.75/+3.09 TO=9.8/9.0 lshare=0.29/0.36
x_std9_k1_w60  sign=-1 hl= 0.0 dist=1.000 cov=0.9992 rIC tr/va=0.0517/0.0616 LS=+3.25/+4.16 Lg=+16.0/+22.1 Ln=+7.4/+14.2 Lsh=+1.21/+2.70 TO=9.8/9.1 lshare=0.24/0.32
d_sum_k3 {'ctl_amt': 0.47, 'ctl_cap': 0.24, 'known_stdamt_max9': 0.52, 'ref_base': 0.86}
d_sum_k2 {'ctl_amt': 0.74, 'ctl_cap': 0.4, 'known_stdamt_max9': 0.74, 'ref_base': 0.75}
d_sum_k1 {'ctl_amt': 0.94, 'ctl_cap': 0.51, 'known_stdamt_max9': 0.88, 'ref_base': 0.52}
d_amt {'ctl_amt': 1.0, 'ctl_cap': 0.56, 'known_stdamt_max9': 0.89, 'ref_base
… (957 字符略) …
': 1.6105, 'long_ann': 0.0968, 'long_turnover': 0.0966}
   {'halflife': 2.0, 'ls_sharpe': 3.315, 'ls_turnover': 0.0708, 'long_sharpe': 1.9207, 'long_ann': 0.115, 'long_turnover': 0.0789}
   {'halflife': 3.0, 'ls_sharpe': 3.2796, 'ls_turnover': 0.062, 'long_sharpe': 1.9677, 'long_ann': 0.1173, 'long_turnover': 0.0682}
   {'halflife': 5.0, 'ls_sharpe': 3.2029, 'ls_turnover': 0.0502, 'long_sharpe': 2.1893, 'long_ann': 0.1312, 'long_turnover': 0.0543}
   {'halflife': 10.0, 'ls_sharpe': 2.9312, 'ls_turnover': 0.0355, 'long_sharpe': 2.2895, 'long_ann': 0.138, 'long_turnover': 0.0379}
   {'halflife': 20.0, 'ls_sharpe': 2.6312, 'ls_turnover': 0.0235, 'long_sharpe': 2.2121, 'long_ann': 0.1323, 'long_turnover': 0.0252}
d_sum_k2 sweep
   {'halflife': 0.0, 'ls_sharpe': 1.172, 'ls_turnover': 0.2741, 'long_sharpe': -3.166, 'long_ann': -0.1697, 'long_turnover': 0.3253}
   {'halflife': 1.0, 'ls_sharpe': 2.4997, 'ls_turnover': 0.1486, 'long_sharpe': -0.4757, 'long_ann': -0.0262, 'long_turnover': 0.1751}
   {'halflife': 2.0, 'ls_sharpe': 2.9492, 'ls_turnover': 0.1018, 'long_sharpe': 0.5683, 'long_ann': 0.0315, 'long_turnover': 0.1196}
   {'halflife': 3.0, 'ls_sharpe': 3.1025, 'ls_turnover': 0.0809, 'long_sharpe': 0.9389, 'long_ann': 0.0525, 'long_turnover': 0.095}
   {'halflife': 5.0, 'ls_sharpe': 3.2299, 'ls_turnover': 0.0602, 'long_sharpe': 1.4314, 'long_ann': 0.0812, 'long_turnover': 0.0707}
   {'halflife': 10.0, 'ls_sharpe': 3.3258, 'ls_turnover': 0.0395, 'long_sharpe': 1.9828, 'long_ann': 0.1138, 'long_turnover': 0.0463}
   {'halflife': 20.0, 'ls_sharpe': 3.0461, 'ls_turnover': 0.0244, 'long_sharpe': 2.1886, 'long_ann': 0.1261, 'long_turnover': 0.0283}
```

**10-03 23:40 · Bash** — Dump S2 diagnostics

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/S2_distil.json"))
dg=d["diagnostics"]
R=d["results"]
print("by_year_scope", dg["by_year_scope"], list(dg["by_year"].keys()))
for k,v in dg["by_year"].items():
    print(k, [(y["year"], round(y["ls_sharpe"],2), round(y["long_ann"]*100,1)) for y in v])
print("neutralise keys", list(dg["neutralise"].keys()))
for k,v in dg["neutralise"].items():
    for c in ["_traded_signal","all_controls","ctl_amt","ctl_cap"]:
        x=v[c]
        print(k, c, {kk: round(vv,4) for kk,vv in x.items()})
print("conditional keys", list(dg["conditional"].keys()))
for k,v in dg["conditional"].items():
    print(k, [round(b["rank_ic"],4) for b in v])
print("decay keys", list(dg["decay"].keys()))
for k in R:
    if "profile" in R[k]:
        print(k, "profile train", [round(q["excess_ann"]*100,1) for q in R[k]["profile"]["train"]])
        print(k, "profile valid", [round(q["excess_ann"]*100,1) for q in R[k]["profile"]["valid"]])
EOF
```

```
by_year_scope ['20180102', '20230807'] ['d_sum_k3', 'd_sum_k2', 'd_sum_k1', 'd_amt', 'b_stdamt9', 'x_std9_k1', 'x_std9_k2', 'e_peak_k2', 'x_std9_pk2', 'g_stdB']
d_sum_k3 [('2018', 3.99, 7.4), ('2019', 4.5, 16.5), ('2020', 4.61, 12.9), ('2021', 2.85, 7.0), ('2022', 3.66, 9.7), ('2023', 1.86, 3.7)]
d_sum_k2 [('2018', 4.89, 14.3), ('2019', 4.29, 14.0), ('2020', 2.26, 6.1), ('2021', 2.68, 10.7), ('2022', 4.86, 16.5), ('2023', 2.45, 10.9)]
d_sum_k1 [('2018', 3.68, 18.8), ('2019', 2.67, 11.4), ('2020', 1.13, 5.0), ('2021', 2.38, 14.4), ('2022', 4.81, 22.7), ('2023', 2.82, 17.1)]
d_amt [('2018', 2.49, 16.6), ('2019', 1.37, 8.1), ('2020', 0.19, 0.7), ('2021', 1.77, 11.8), ('2022', 4.07, 23.1), ('2023', 3.03, 17.4)]
b_stdamt9 [('2018', 4.02, 18.5), ('2019', 3.32, 9.7), ('2020', 1.2, -0.2), ('2021', 2.07, 8.7), ('2022', 5.41, 20.5), ('2023', 3.04, 14.8)]
x_std9_k1 [('2018', 5.67, 19.8), ('2019', 4.55, 13.6), ('2020', 2.08, 4.6), ('2021', 2.22, 7.6), ('2022', 5.34, 19.8), ('2023', 3.0, 13.9)]
x_std9_k2 [('2018', 6.6, 10.2), ('2019', 6.36, 16.1), ('2020', 3.37, 8.9), ('2021', 2.07, 0.4), ('2022', 4.66, 14.0), ('2023', 2.38, 8.1)]
e_peak_k2 [('2018', 5.22, 22.9), ('2019', 3.36, 11.6), ('2020', 1.91, 7.2), ('2021', 2.66, 12.2), ('2022', 5.07, 18.4), ('2023', 2.53, 10.3)]
x_std9_pk2 [('2018', 6.33, 22.7), ('2019', 4.5, 12.1), ('2020', 2.54, 7.2), ('2021', 2.62, 10.9), ('2022', 5.14, 19.5), ('2023', 2.51, 7.9)]
g_stdB [('2018', 3.87, 23.1), ('2019', 2.2, 10.4), ('2020', 1.02, 6.1), ('2021', 2.2, 14.5), ('2022', 4.9, 22.8), ('2023', 2.86, 14.5)]
neutralise keys ['d_sum_k2', 'x_std9_k1', 'e_peak_k2', 'b_stdamt9']
d_sum_k2 _traded_signal {'r2': 0.0, 'rank_ic': 0.0404, 'rank_icir': 0.4089, 'ls_sharpe': 3.3258, 'ls_gross_sharpe': 3.7496, 'long_gross_ann': 0.1488, 'short_gross_ann': 0.3801, 'long_ann': 0.1138, 'ls_turnover': 0.0395}
d_sum_k2 all_controls {'r2': 0.5545, 'rank_ic': 0.0123, 'rank_icir': 0.2564, 'ls_sharpe': -3.519, 'ls_gross_sharpe': 1.8065, 'long_gross_ann': 0.0824, 'short_gross_ann': 0.0421, 'long_ann': -0.1271, 'ls_turnover': 0.238, 'r2_raw_panel': 0.6391}
d_sum_k2 ctl_amt {'r2': 0.4621, 'rank_ic': 0.0182, 'rank_icir': 0.2648, 'ls_sharpe': -1.8472, 'ls_gross_sharpe': 2.2614, 'long_gross_ann': 0.0987, 'short_gross_ann': 0.0849, 'long_ann': -0.0994, 'ls_turnover': 0.221}
d_sum_k2 ctl_cap {'r2': 0.1631, 'rank_ic': 0.0427, 'rank_icir': 0.4546, 'ls_sharpe': 3.3299, 'ls_gross_sharpe': 3.7951, 'long_gross_ann': 0.0895, 'short_gross_ann': 0.4243, 'long_ann': 0.0549, 'ls_turnover': 0.0417}
x_std9_k1 _traded_signal {'r2': 0.0, 'rank_ic': 0.0472, 'rank_icir': 0.4594, 'ls_sharpe': 3.315, 'ls_gross_sharpe': 4.0305, 'long_gross_ann': 0.1747, 'short_gross_ann': 0.4288, 'long_ann': 0.115, 'ls_turnover': 0.0708}
x_std9_k1 all_controls {'r2': 0.6456, 'rank_ic': 0.017, 'rank_icir': 0.354, 'ls_sharpe': -2.7741, 'ls_gross_sharpe': 3.3696, 'long_gross_ann': 0.1233, 'short_gross_ann': 0.1089, 'long_ann': -0.1199, 'ls_turnover': 0.2747, 'r2_raw_panel': 0.6427}
x_std9_k1 ctl_amt {'r2': 0.5441, 'rank_ic': 0.0263, 'rank_icir': 0.4132, 'ls_sharpe': -1.9861, 'ls_gross_sharpe': 3.662, 'long_gross_ann': 0.1244, 'short_gross_ann': 0.1476, 'long_ann': -0.1297, 'ls_turnover': 0.2781}
x_std9_k1 ctl_cap {'r2': 0.1834, 'rank_ic': 0.0506, 'rank_icir': 0.5136, 'ls_sharpe': 3.2873, 'ls_gross_sharpe': 4.0563, 'long_gr
… (2113 字符略) …
]
x_std9_k1|ctl_amt [-0.0271, -0.023, -0.0275, -0.0367, -0.0462]
x_std9_k1|ctl_cap [-0.0762, -0.0671, -0.0638, -0.0492, -0.0236]
decay keys ['d_sum_k2', 'x_std9_k1']
d_sum_k3 profile train [-33.3, -12.4, -4.5, -2.1, 0.7, 5.6, 10.3, 11.4, 10.9, 13.4]
d_sum_k3 profile valid [-26.3, -11.9, -3.8, -2.8, 4.0, 3.2, 7.1, 11.6, 7.5, 11.3]
d_sum_k2 profile train [-38.3, -16.1, -5.3, -0.8, 2.7, 7.5, 8.8, 13.4, 12.6, 15.4]
d_sum_k2 profile valid [-36.6, -15.3, -7.9, -3.7, 1.2, 4.2, 10.1, 10.8, 16.7, 20.6]
d_sum_k1 profile train [-28.7, -15.3, -7.5, -1.6, 2.5, 5.5, 6.8, 9.7, 12.4, 16.2]
d_sum_k1 profile valid [-37.6, -20.2, -12.1, -5.3, -0.7, 7.4, 8.5, 14.8, 19.4, 25.7]
d_amt profile train [-18.5, -13.0, -8.7, -3.3, -1.1, 5.0, 5.7, 9.4, 11.0, 13.6]
d_amt profile valid [-36.4, -25.8, -12.1, -6.7, -0.1, 6.3, 10.9, 13.7, 23.3, 26.8]
b_stdamt9 profile train [-38.3, -17.4, -7.7, -2.6, 3.5, 6.3, 10.3, 13.6, 14.8, 17.5]
b_stdamt9 profile valid [-48.7, -19.2, -11.3, -1.7, 0.8, 6.0, 9.5, 15.2, 21.8, 27.7]
x_std9_k1 profile train [-43.4, -17.9, -7.4, 0.0, 3.3, 8.5, 9.2, 14.4, 15.4, 17.9]
x_std9_k1 profile valid [-44.5, -15.3, -9.4, -3.6, 0.7, 6.7, 6.5, 13.3, 20.4, 25.3]
e_peak_k2 profile train [-41.2, -15.1, -5.0, -1.4, 2.5, 6.5, 8.9, 12.2, 14.4, 18.2]
e_peak_k2 profile valid [-44.5, -15.3, -7.9, -2.1, 1.1, 6.0, 9.5, 13.5, 17.7, 22.0]
x_std9_pk2 profile train [-48.4, -15.6, -6.6, -1.0, 3.0, 6.3, 12.5, 13.8, 16.8, 19.4]
x_std9_pk2 profile valid [-43.9, -13.1, -8.5, -3.3, 2.6, 5.6, 8.9, 12.2, 17.1, 22.3]
g_stdB profile train [-28.7, -16.5, -7.3, -4.1, 2.2, 4.9, 8.3, 10.9, 12.8, 17.6]
g_stdB profile valid [-43.3, -21.9, -11.2, -4.6, 1.5, 7.4, 9.4, 14.1, 23.6, 25.2]
```

**10-03 23:41 · Bash** — Dump final run results

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/final.json"))
print("errors", d["errors"], d["splits_used"], d["fit_split"], d["user_split"], d["stages"], d["split_dates"])
print(list(d["diagnostics"].keys()))
R=d["results"]
print(list(R.keys()))
print(list(R["f_orig"].keys()))
for k,r in R.items():
    b=r["books"]; s=r["splits"]
    print(k, "sign",r["sign"],"hl",b["hl_used"],"dist",r["distinct"], "splits keys", list(s.keys()), "books splits", list(b["splits"].keys()))
    for sp in b["splits"]:
        x=b["splits"][sp]
        print(f"   DEC {sp:8s} LS={x['ls_sharpe']:+.3f} Lg={x['long_gross_ann']*100:+.2f} Ln={x['long_ann']*100:+.2f} Lsh={x['long_sharpe']:+.3f} TO={x['ls_turnover']*100:.2f} lshare={x['long_share']:.3f} Lmdd={x['long_mdd']*100:.1f} n={x['n_days']}")
    for sp in s:
        print(f"   IC {sp}: rank_ic={s[sp]['rank_ic']:.4f} cov={s[sp]['coverage_labelled']:.4f} sign={s[sp]['sign']}")
    bu=r["books_user"]
    print("   USER sign", r["sign_user"], "hl", bu["hl_used"], "hl_ls", bu["hl_ls"], "hl_long", bu["hl_long"], "ic_user", {kk: round(vv,4) for kk,vv in r["ic_user"].items() if kk in ("rank_ic","coverage_labelled","sign")})
    for sp in bu["splits"]:
        x=bu["splits"][sp]
        print(f"   USR {sp:8s} LS={x['ls_sharpe']:+.3f} Lg={x['long_gross_ann']*100:+.2f} Ln={x['long_ann']*100:+.2f} Lsh={x['long_sharpe']:+.3f} TO={x['ls_turnover']*100:.2f} lshare={x['long_share']:.3f} Lmdd={x['long_mdd']*100:.1f} n={x['n_days']}")
    for kk in r:
        if kk not in ("expr","stage","why","group","sign","splits","distinct","books","sign_user","ic_user","books_user","profile"):
            v=r[kk]
            print("   extra", kk, json.dumps(v)[:600])
EOF
```

```
errors {} ['train', 'valid', 'utrain', 'holdout', 'full'] train utrain ['S_final'] {'train': ['20180102', '20211231'], 'valid': ['20220104', '20230807'], 'utrain': ['20180102', '20230807'], 'holdout': ['20230808', '20251231'], 'full': ['20180102', '20251231']}
['by_year', 'by_year_scope', 'rank_corr_train']
['f_orig', 'f_sum_k3', 'f_sum_k2', 'f_std9_k1', 'f_stdamt9']
['expr', 'stage', 'why', 'group', 'sign', 'splits', 'distinct', 'books', 'sign_user', 'ic_user', 'ic_holdout', 'books_user', 'profile']
f_orig sign -1.0 hl 2.0 dist 1.0 splits keys ['train', 'valid'] books splits ['train', 'valid']
   DEC train    LS=+4.140 Lg=+13.47 Ln=+6.31 Lsh=+1.301 TO=8.46 lshare=0.239 Lmdd=-8.9 n=973
   DEC valid    LS=+2.216 Lg=+10.94 Ln=+3.61 Lsh=+0.663 TO=8.46 lshare=0.277 Lmdd=-4.2 n=386
   IC train: rank_ic=0.0393 cov=0.9992 sign=-1.0
   IC valid: rank_ic=0.0279 cov=0.9995 sign=-1.0
   USER sign -1.0 hl 2.0 hl_ls 2.0 hl_long 10.0 ic_user {'sign': -1.0, 'rank_ic': 0.036, 'coverage_labelled': 0.9993}
   USR utrain   LS=+3.533 Lg=+12.75 Ln=+5.57 Lsh=+1.108 TO=8.43 lshare=0.248 Lmdd=-9.1 n=1359
   USR holdout  LS=+3.180 Lg=+12.41 Ln=+5.47 Lsh=+1.044 TO=8.20 lshare=0.253 Lmdd=-7.1 n=581
   extra ic_holdout {"sign": -1.0, "ic": 0.014179270814937885, "icir": 0.3179827613908825, "ic_t": 7.664637906044153, "rank_ic": 0.03867540871856646, "rank_icir": 0.46139271142600435, "rank_ic_t": 11.121382964597538, "ic_pos": 0.6196213425129088, "coverage": 0.9674589091960595, "coverage_labelled": 0.9997096507593668, "n_days": 581}
f_sum_k3 sign -1.0 hl 20.0 dist 1.0 splits keys ['train', 'valid'] books splits ['train', 'valid']
   DEC train    LS=+3.927 Lg=+13.12 Ln=+11.08 Lsh=+2.244 TO=2.40 lshare=0.285 Lmdd=-5.9 n=973
   DEC valid    LS=+2.879 Lg=+9.75 Ln=+7.52 Lsh=+1.454 TO=2.54 lshare=0.275 Lmdd=-4.7 n=386
   IC train: rank_ic=0.0410 cov=0.9992 sign=-1.0
   IC valid: rank_ic=0.0336 cov=0.9995 sign=-1.0
   USER sign -1.0 hl 10.0 hl_ls 10.0 hl_long 20.0 ic_user {'sign': -1.0, 'rank_ic': 0.0389, 'coverage_labelled': 0.9993}
   USR utrain   LS=+3.640 Lg=+11.76 Ln=+8.43 Lsh=+1.658 TO=3.86 lshare=0.243 Lmdd=-7.2 n=1359
   USR holdout  LS=+3.518 Lg=+12.32 Ln=+9.23 Lsh=+1.765 TO=3.66 lshare=0.258 Lmdd=-5.1 n=581
   extra ic_holdout {"sign": -1.0, "ic": 0.026036110884722352, "icir": 0.42231278606757217, "ic_t": 10.17940272655749, "rank_ic": 0.043584156155321074, "rank_icir": 0.4601390314369165, "rank_ic_t": 11.091164335372541, "ic_pos": 0.6712564543889845, "coverage": 0.9674589091960595, "coverage_labelled": 0.9997096507593668, "n_days": 581}
f_sum_k2 sign -1.0 hl 10.0 dist 1.0 splits keys ['train', 'valid'] books splits ['train', 'valid']
   DEC train    LS=+3.326 Lg=+14.88 Ln=+11.38 Lsh=+1.983 TO=3.95 lshare=0.281 Lmdd=-6.9 n=973
   DEC valid    LS=+3.781 Lg=+17.93 Ln=+14.53 Lsh=+2.697 TO=3.84 lshare=0.331 Lmdd=-3.9 n=386
   IC train: rank_ic=0.0464 cov=0.9992 sign=-1.0
   IC valid: rank_ic=0.0491 cov=0.9995 sign=-1.0
   USER sign -1.0 hl 10.0 hl_ls 10.0 hl_long 20.0 ic_user {'sign': -1.0, 'rank_ic': 0.0471, 'coverage_labelled': 0.9993}
   USR utrain   LS=+3.446 Lg=+15.74 Ln=+12.30 Lsh=+2.179 TO=3.89 lshare=0.296 Lmdd=-6.9 n=1359
   USR holdout  LS=+3.099 Lg=+15.58 Ln=+12.64 Lsh=+2.071 TO=3.45 lshare=0.311 Lmdd=-5.2 n=581
   extra ic_holdout {"sign": -1.0, "ic": 0.028180878931543946, "icir": 0.360916002293
… (635 字符略) …
  USER sign -1.0 hl 2.0 hl_ls 2.0 hl_long 10.0 ic_user {'sign': -1.0, 'rank_ic': 0.0538, 'coverage_labelled': 0.9993}
   USR utrain   LS=+3.580 Lg=+19.10 Ln=+13.29 Lsh=+2.274 TO=6.91 lshare=0.307 Lmdd=-8.6 n=1359
   USR holdout  LS=+3.142 Lg=+16.93 Ln=+11.64 Lsh=+1.547 TO=6.36 lshare=0.277 Lmdd=-9.2 n=581
   extra ic_holdout {"sign": -1.0, "ic": 0.02876571628112386, "icir": 0.3427204755045893, "ic_t": 8.260914322021705, "rank_ic": 0.06091889781071987, "rank_icir": 0.4838444129702012, "rank_ic_t": 11.662557467133874, "ic_pos": 0.6368330464716007, "coverage": 0.9674589091960595, "coverage_labelled": 0.9997096507593668, "n_days": 581}
f_stdamt9 sign -1.0 hl 0.0 dist 1.0 splits keys ['train', 'valid'] books splits ['train', 'valid']
   DEC train    LS=+2.472 Lg=+16.87 Ln=+9.26 Lsh=+1.371 TO=8.53 lshare=0.309 Lmdd=-10.7 n=973
   DEC valid    LS=+4.437 Lg=+24.92 Ln=+18.47 Lsh=+3.092 TO=7.73 lshare=0.341 Lmdd=-4.4 n=386
   IC train: rank_ic=0.0484 cov=0.9992 sign=-1.0
   IC valid: rank_ic=0.0671 cov=0.9995 sign=-1.0
   USER sign -1.0 hl 0.0 hl_ls 0.0 hl_long 5.0 ic_user {'sign': -1.0, 'rank_ic': 0.0537, 'coverage_labelled': 0.9993}
   USR utrain   LS=+2.943 Lg=+19.16 Ln=+11.90 Lsh=+1.817 TO=8.27 lshare=0.320 Lmdd=-10.7 n=1359
   USR holdout  LS=+2.551 Lg=+15.17 Ln=+8.19 Lsh=+0.890 TO=8.03 lshare=0.248 Lmdd=-15.4 n=581
   extra ic_holdout {"sign": -1.0, "ic": 0.024984873721581063, "icir": 0.26626899016769034, "ic_t": 6.418132185268503, "rank_ic": 0.06490370211591581, "rank_icir": 0.4364150470941105, "rank_ic_t": 10.519322802577165, "ic_pos": 0.6230636833046471, "coverage": 0.9674589091960595, "coverage_labelled": 0.9997096507593668, "n_days": 581}
```

**10-03 23:41 · Bash** — Dump final diagnostics, profiles, sweeps

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/final.json"))
dg=d["diagnostics"]
print("by_year_scope", dg["by_year_scope"], list(dg["by_year"].keys()))
for k,v in dg["by_year"].items():
    print(k, [(y["year"], y["days"], round(y["ls_sharpe"],2), round(y["long_ann"]*100,1), round(y["long_sharpe"],2)) for y in v])
rc=dg["rank_corr_train"]
print(list(rc.keys()))
for k in ["f_orig","f_sum_k3","f_sum_k2","f_std9_k1","f_stdamt9"]:
    print(k, {kk: round(vv,3) for kk,vv in rc[k].items()})
R=d["results"]
for k in R:
    p=R[k]["profile"]
    print(k, list(p.keys()))
    for sp in p:
        print("  ", sp, [round(q["excess_ann"]*100,1) for q in p[sp]])
    print("  sweep_user", [(s["halflife"], round(s["ls_sharpe"],3), round(s["long_ann"]*100,1)) for s in R[k]["books_user"]["sweep"]])
    print("  splits_at_hl_long user", {sp: (round(x["ls_sharpe"],2), round(x["long_ann"]*100,1), round(x["long_sharpe"],2)) for sp,x in R[k]["books_user"]["splits_at_hl_long"].items()})
EOF
```

```
by_year_scope ['20180102', '20251231'] ['f_orig', 'f_sum_k3', 'f_sum_k2', 'f_std9_k1', 'f_stdamt9']
f_orig [('2018', 243, 5.43, 1.9, 0.43), ('2019', 244, 6.22, 15.2, 3.53), ('2020', 243, 4.19, 11.6, 2.4), ('2021', 243, 1.78, -3.9, -0.69), ('2022', 242, 2.87, 6.5, 1.17), ('2023', 242, 2.05, 2.7, 0.57), ('2024', 242, 2.86, 0.3, 0.04), ('2025', 243, 3.34, 9.1, 1.99)]
f_sum_k3 [('2018', 243, 4.73, 5.8, 1.42), ('2019', 244, 4.95, 15.3, 3.68), ('2020', 243, 4.27, 11.4, 2.49), ('2021', 243, 2.37, 2.4, 0.36), ('2022', 242, 3.9, 10.3, 1.96), ('2023', 242, 2.64, 5.9, 1.2), ('2024', 242, 3.59, 7.4, 1.24), ('2025', 243, 3.08, 10.0, 2.11)]
f_sum_k2 [('2018', 243, 4.89, 14.3, 3.28), ('2019', 244, 4.29, 14.0, 3.49), ('2020', 243, 2.26, 6.1, 0.93), ('2021', 243, 2.68, 10.7, 1.45), ('2022', 242, 4.86, 16.5, 3.01), ('2023', 242, 3.44, 14.4, 2.79), ('2024', 242, 2.89, 9.5, 1.41), ('2025', 243, 2.6, 12.9, 2.21)]
f_std9_k1 [('2018', 243, 5.67, 19.8, 4.09), ('2019', 244, 4.55, 13.6, 3.28), ('2020', 243, 2.08, 4.6, 0.68), ('2021', 243, 2.22, 7.6, 1.01), ('2022', 242, 5.34, 19.8, 3.54), ('2023', 242, 3.75, 15.4, 2.94), ('2024', 242, 3.01, 8.1, 0.9), ('2025', 243, 2.72, 12.7, 1.91)]
f_stdamt9 [('2018', 243, 4.02, 18.5, 3.28), ('2019', 244, 3.32, 9.7, 1.99), ('2020', 243, 1.2, -0.2, -0.02), ('2021', 243, 2.07, 8.7, 1.1), ('2022', 242, 5.41, 20.5, 3.35), ('2023', 242, 4.01, 17.0, 2.89), ('2024', 242, 2.21, 3.0, 0.26), ('2025', 243, 2.11, 8.4, 1.12)]
['f_orig', 'f_sum_k3', 'f_sum_k2', 'f_std9_k1', 'f_stdamt9', 'ctl_amt', 'ctl_cap', 'ctl_turnrate', 'ctl_ivol', 'ctl_dvol20', 'ctl_price', 'ctl_rev1', 'ctl_mom20', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'ref_base', 'ref_A5', 'ref_C']
f_orig {'f_orig': 1.0, 'f_sum_k3': 0.861, 'f_sum_k2': 0.745, 'f_std9_k1': 0.647, 'f_stdamt9': 0.412, 'ctl_amt': 0.281, 'ctl_cap': 0.101, 'ctl_turnrate': 0.189, 'ctl_ivol': 0.268, 'ctl_dvol20': 0.176, 'ctl_price': -0.026, 'ctl_rev1': -0.007, 'ctl_mom20': 0.263, 'known_amt_max9': 0.313, 'known_stdamt_max9': 0.412, 'known_ivol_max9': 0.325, 'ref_base': 1.0, 'ref_A5': 0.501, 'ref_C': 0.493}
f_sum_k3 {'f_orig': 0.861, 'f_sum_k3': 1.0, 'f_sum_k2': 0.929, 'f_std9_k1': 0.74, 'f_stdamt9': 0.521, 'ctl_amt': 0.473, 'ctl_cap': 0.236, 'ctl_turnrate': 0.271, 'ctl_ivol': 0.377, 'ctl_dvol20': 0.195, 'ctl_price': 0.065, 'ctl_rev1': 0.072, 'ctl_mom20': 0.298, 'known_amt_max9': 0.427, 'known_stdamt_max9': 0.521, 'known_ivol_max9': 0.321, 'ref_base': 0.861, 'ref_A5': 0.485, 'ref_C': 0.407}
f_sum_k2 {'f_orig': 0.745, 'f_sum_k3': 0.929, 'f_sum_k2': 1.0, 'f_std9_k1': 0.859, 'f_stdamt9': 0.741, 'ctl_amt': 0.745, 'ctl_cap': 0.396, 'ctl_turnrate': 0.409, 'ctl_ivol': 0.404, 'ctl_dvol20': 0.331, 'ctl_price': 0.232, 'ctl_rev1': 0.071, 'ctl_mom20': 0.317, 'known_amt_max9': 0.686, 'known_stdamt_max9': 0.741, 'known_ivol_max9': 0.331, 'ref_base': 0.745, 'ref_A5': 0.705, 'ref_C': 0.085}
f_std9_k1 {'f_orig': 0.647, 'f_sum_k3': 0.74, 'f_sum_k2': 0.859, 'f_std9_k1': 1.0, 'f_stdamt9': 0.93, 'ctl_amt': 0.754, 'ctl_cap': 0.415, 'ctl_turnrate': 0.401, 'ctl_ivol': 0.344, 'ctl_dvol20': 0.459, 'ctl_price': 0.267, 'ctl_rev1': -0.009, 'ctl_mom20': 0.302, 'known_amt_max9': 0.838, 'known_stdamt_max9': 0.93, 'known_ivol_max9': 0.45, 'ref_base': 0.647, 'ref_A5': 0.774, 'ref_C': -0.074}
f_stdamt9 {'f_orig': 0.412, 'f_sum_k3': 0.521, 'f_sum_k2': 0.741, 'f_s
… (675 字符略) …
8.1, 1.49), 'holdout': (2.92, 7.2, 1.26)}
f_sum_k3 ['train', 'valid']
   train [-33.3, -12.4, -4.5, -2.1, 0.7, 5.6, 10.3, 11.4, 10.9, 13.4]
   valid [-26.3, -11.9, -3.8, -2.8, 4.0, 3.2, 7.1, 11.6, 7.5, 11.3]
  sweep_user [(0.0, 1.476, -14.8), (1.0, 2.887, -2.6), (2.0, 3.339, 2.3), (3.0, 3.537, 4.9), (5.0, 3.624, 6.6), (10.0, 3.64, 8.4), (20.0, 3.628, 10.1)]
  splits_at_hl_long user {'utrain': (3.63, 10.1, 2.02), 'holdout': (3.33, 10.7, 1.99)}
f_sum_k2 ['train', 'valid']
   train [-38.3, -16.1, -5.3, -0.8, 2.7, 7.5, 8.8, 13.4, 12.6, 15.4]
   valid [-36.6, -15.3, -7.9, -3.7, 1.2, 4.2, 10.1, 10.8, 16.7, 20.6]
  sweep_user [(0.0, 1.225, -14.8), (1.0, 2.583, -1.2), (2.0, 3.063, 4.6), (3.0, 3.244, 7.1), (5.0, 3.39, 10.0), (10.0, 3.446, 12.3), (20.0, 3.233, 13.4)]
  splits_at_hl_long user {'utrain': (3.23, 13.4, 2.36), 'holdout': (2.88, 13.5, 2.23)}
f_std9_k1 ['train', 'valid']
   train [-43.4, -17.9, -7.4, 0.0, 3.3, 8.5, 9.2, 14.4, 15.4, 17.9]
   valid [-44.5, -15.3, -9.4, -3.6, 0.7, 6.7, 6.5, 13.3, 20.4, 25.3]
  sweep_user [(0.0, 3.531, 8.8), (1.0, 3.557, 11.7), (2.0, 3.58, 13.3), (3.0, 3.558, 13.9), (5.0, 3.446, 14.9), (10.0, 3.2, 15.6), (20.0, 2.935, 15.0)]
  splits_at_hl_long user {'utrain': (3.2, 15.6, 2.61), 'holdout': (2.75, 14.2, 1.92)}
f_stdamt9 ['train', 'valid']
   train [-38.3, -17.4, -7.7, -2.6, 3.5, 6.3, 10.3, 13.6, 14.8, 17.5]
   valid [-48.7, -19.2, -11.3, -1.7, 0.8, 6.0, 9.5, 15.2, 21.8, 27.7]
  sweep_user [(0.0, 2.943, 11.9), (1.0, 2.927, 14.2), (2.0, 2.842, 15.2), (3.0, 2.749, 15.4), (5.0, 2.658, 16.1), (10.0, 2.425, 15.7), (20.0, 2.25, 15.1)]
  splits_at_hl_long user {'utrain': (2.66, 16.1, 2.41), 'holdout': (2.2, 13.2, 1.4)}
```

**10-03 23:42 · Bash** — Check git status for out-of-scope edits and inspect study.sh

```bash
cd /Users/wxy/Desktop/Partura && git status --short partura scripts lab docs; echo "--- git status all (head)"; git status --short | head -50; echo "--- log"; git log --oneline | head -5; echo "--- study.sh"; wc -l scripts/study.sh; grep -n "exec\|log\|rsync\|scp" scripts/study.sh | head -60
```

```
 M docs/study_playbook.md
 M scripts/study.sh
 M scripts/summarize.py
--- git status all (head)
 M configs/F101_day_shine_retstd.yaml
 M configs/F102_kurt_autocorr.yaml
 M configs/F103_amt_dw_decay.yaml
 M configs/F104_kurt_masktop_amt.yaml
 M configs/F105_std_fangzheng_covamt.yaml
 M configs/F107_abs_demean_skew_low.yaml
 M docs/study_playbook.md
 M scripts/study.sh
 M scripts/summarize.py
?? logs/
?? notes/F101_day_shine_retstd/
?? notes/F102_kurt_autocorr/
?? notes/F103_amt_dw_decay/
?? notes/F104_kurt_masktop_amt/
?? notes/F105_std_fangzheng_covamt/
?? research/alpha_distillation/F101_day_shine_retstd.md
?? research/alpha_distillation/F102_kurt_autocorr.md
?? research/alpha_distillation/F103_amt_dw_decay.md
?? research/alpha_distillation/F104_kurt_masktop_amt.md
?? research/alpha_distillation/F105_std_fangzheng_covamt.md
?? studies/F101_day_shine_retstd/
?? studies/F102_kurt_autocorr/
?? studies/F103_amt_dw_decay/
?? studies/F104_kurt_masktop_amt/
?? studies/F105_std_fangzheng_covamt/
?? studies/F107_abs_demean_skew_low/
--- log
60fd492 显存上限跟着空闲量走,永远给邻居留 4 GiB
91f8a99 中性化残差同时报无成本夏普与空头腿;批次总览脚本
8dd5b69 中性化改为针对实际交易的信号;工具链端到端验通
4cf7c84 对齐用户的可交易口径,并为多研究并行做好准备
3c88991 把 Partura 从固定流水线改成按表达式定制的研究台
--- study.sh
      98 scripts/study.sh
13:#   study.sh exec <fid> <tag> <script.py>  run studies/<fid>/<script.py> on the server (returns at once)
23:RS="rsync -a --exclude __pycache__ -e"
60:    $SSH $HOST "$ENV && mkdir -p logs && rm -f logs/${fid}_${tag}.log && screen -dmS pt_${fid:0:4}_${tag} bash -c 'EXTRA=\"$extra --tag $tag\" PARTURA_SLOTS=\${PARTURA_SLOTS:-2} ./scripts/run_server.sh configs/$fid.yaml $* > logs/${fid}_${tag}.log 2>&1' && echo 'started $fid/$tag: stages $* $extra'"
62:  exec)
65:    $SSH $HOST "$ENV && mkdir -p logs && rm -f logs/${fid}_${tag}.log && screen -dmS pt_${fid:0:4}_${tag} bash -c '$ENV; nice -n 5 $RPY -u studies/$fid/$script $* > logs/${fid}_${tag}.log 2>&1; echo \"[partura exit \$? \$(date +%F_%T)]\" >> logs/${fid}_${tag}.log' && echo 'started $fid/$tag: $script'"
71:      st=$($SSH $HOST "grep -ac 'partura exit' $R/logs/${fid}_${tag}.log 2>/dev/null; grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' $R/logs/${fid}_${tag}.log 2>/dev/null | tail -4" 2>/dev/null)
77:    mkdir -p "runs/$fid" logs
78:    $RS "$SSH" "$HOST:$R/logs/${fid}_${tag}.log" logs/ 2>/dev/null
81:    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
82:         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
```

**10-03 23:42 · Bash** — Check modification times of shared files and F103 logs

```bash
cd /Users/wxy/Desktop/Partura && ls -la --time-style=full-iso docs/study_playbook.md scripts/study.sh scripts/summarize.py 2>/dev/null || stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" docs/study_playbook.md scripts/study.sh scripts/summarize.py lab/findings.yaml; echo ---; git diff --stat -- docs scripts partura lab; echo; ls -la logs | grep -i F103; echo; stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" logs/F103* notes/F103_amt_dw_decay/* studies/F103_amt_dw_decay/* runs/F103_amt_dw_decay/* configs/F103_amt_dw_decay.yaml research/alpha_distillation/F103_amt_dw_decay.md
```

```
2026-10-03 23:20:15 docs/study_playbook.md
2026-10-03 23:20:15 scripts/study.sh
2026-10-03 23:20:15 scripts/summarize.py
2026-09-30 12:21:26 lab/findings.yaml
---
 docs/study_playbook.md |  6 ++++++
 scripts/study.sh       |  2 +-
 scripts/summarize.py   | 16 ++++++++++++++--
 3 files changed, 21 insertions(+), 3 deletions(-)

-rw-r--r--@  1 wxy  staff   1946 Oct  3 19:34 F103_amt_dw_decay_S1_structure.log
-rw-r--r--@  1 wxy  staff   1650 Oct  3 23:19 F103_amt_dw_decay_S2_distil.log
-rw-r--r--@  1 wxy  staff   1101 Oct  3 23:26 F103_amt_dw_decay_final.log
-rw-r--r--@  1 wxy  staff  11410 Oct  3 19:40 F103_amt_dw_decay_x1.log
-rw-r--r--@  1 wxy  staff  10100 Oct  3 19:56 F103_amt_dw_decay_x2.log
-rw-r--r--@  1 wxy  staff  21684 Oct  3 23:04 F103_amt_dw_decay_x3.log

2026-10-03 19:34:23 logs/F103_amt_dw_decay_S1_structure.log
2026-10-03 23:19:18 logs/F103_amt_dw_decay_S2_distil.log
2026-10-03 23:26:42 logs/F103_amt_dw_decay_final.log
2026-10-03 19:40:35 logs/F103_amt_dw_decay_x1.log
2026-10-03 19:56:53 logs/F103_amt_dw_decay_x2.log
2026-10-03 23:04:07 logs/F103_amt_dw_decay_x3.log
2026-10-03 23:34:58 notes/F103_amt_dw_decay/01_expression.md
2026-10-03 23:36:24 notes/F103_amt_dw_decay/02_operators.md
2026-10-03 23:36:24 notes/F103_amt_dw_decay/03_decomposition.md
2026-10-03 18:39:41 notes/F103_amt_dw_decay/04_grammar.md
2026-10-03 23:36:24 notes/F103_amt_dw_decay/05_hypotheses.md
2026-10-03 18:44:46 notes/F103_amt_dw_decay/06_baseline.md
2026-10-03 23:34:58 notes/F103_amt_dw_decay/07_S1_structure.md
2026-10-03 23:29:46 notes/F103_amt_dw_decay/07_S2_distil.md
2026-10-03 23:31:17 notes/F103_amt_dw_decay/07_S_final.md
2026-10-03 23:31:17 notes/F103_amt_dw_decay/07_conditional.md
2026-10-03 23:31:52 notes/F103_amt_dw_decay/07_controls.md
2026-10-03 23:31:52 notes/F103_amt_dw_decay/07_neutralise.md
2026-10-03 23:36:24 notes/F103_amt_dw_decay/07x_x1_anatomy.md
2026-10-03 23:34:58 notes/F103_amt_dw_decay/07x_x2_interaction.md
2026-10-03 23:36:24 notes/F103_amt_dw_decay/07x_x3_family.md
2026-10-03 23:32:14 notes/F103_amt_dw_decay/08_variants.md
2026-10-03 23:33:42 notes/F103_amt_dw_decay/09_diagnosis.md
2026-10-03 23:34:34 notes/F103_amt_dw_decay/10_distilled.md
2026-10-03 23:34:58 notes/F103_amt_dw_decay/11_risks.md
2026-10-03 23:34:34 notes/F103_amt_dw_decay/12_next.md
2026-10-03 22:40:52 studies/F103_amt_dw_decay/__pycache__
2026-10-03 18:43:04 studies/F103_amt_dw_decay/probes.py
2026-10-03 18:46:23 studies/F103_amt_dw_decay/x1_anatomy.py
2026-10-03 19:45:18 studies/F103_amt_dw_decay/x2_interaction.py
2026-10-03 22:40:34 studies/F103_amt_dw_decay/x3_family.py
2026-10-03 17:43:26 runs/F103_amt_dw_decay/S0_baseline.json
2026-10-03 19:34:22 runs/F103_amt_dw_decay/S1_structure.json
2026-10-03 23:19:17 runs/F103_amt_dw_decay/S2_distil.json
2026-10-03 23:26:41 runs/F103_amt_dw_decay/final.json
2026-10-03 23:26:41 runs/F103_amt_dw_decay/ledger.json
2026-10-03 23:22:50 configs/F103_amt_dw_decay.yaml
2026-10-03 23:36:47 research/alpha_distillation/F103_amt_dw_decay.md
```

**10-03 23:42 · Bash** — Show diffs of shared docs and scripts

```bash
cd /Users/wxy/Desktop/Partura && git diff -- docs scripts
```

```
diff --git a/docs/study_playbook.md b/docs/study_playbook.md
index 3348762..bfee425 100644
--- a/docs/study_playbook.md
+++ b/docs/study_playbook.md
@@ -130,6 +130,12 @@ stages:
 - `cross_*` 滚的是**交易日**轴(不是截面);`cs_*` 才是截面;`nt_*` 是逐分钟的截面/日轴;`in_*` 是日内分钟轴。
 - 保序的外层一元变换(`pow_3`、`cs_rank`、`sigmoid`…)单独作用时对 rank IC 和十分位书**毫无影响**
   (F001 的结论,`decompose` 输出末尾的实验室先验里有)—— 别把它当成一个"变体"来试。
+- **`ts_*`(ND 面)长窗口算子在显存紧张时会 OOM 而求值失败**:ND 面是整张面板一次算(1942×5220×窗口),
+  邻居占着显卡时 Partura 的上限只有 2~3 GiB,`ts_stddev(x, 20)` 这类就过不去。**日频量上的日轴滚动改用
+  `cross_*`(DT 面)写**:`cross_stddev(x, 20)`、`cross_mean`、`cross_max`… 对「每股票-日一个值」的 x,
+  它和 `ts_*` 是同一个滚动统计量,但按股票分块,几百 MiB 就够。(`ts_delay` 很轻,不受影响。)
+- **各变体的半衰期是各自拟合的**:一个选 10、一个选 20,换手差一倍,多头腿净超额就能差 1~3 个点 ——
+  这不是结构差异。`digest` 里有一张「固定半衰期下的表现」,比结构之前先看它。
 - 手写库的通用调用带字面量参数(`in_slice(x, 2, 237)`、`day_quantile(x, 0.95)`),签名看 `src`。
 
 ---
diff --git a/scripts/study.sh b/scripts/study.sh
index d12bdd5..0f4d953 100755
--- a/scripts/study.sh
+++ b/scripts/study.sh
@@ -79,7 +79,7 @@ case "$cmd" in
     $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
     if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json";
     else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
-         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -60; fi
+         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
     ;;
   digest)
     fid=$1; tag=$2; base=${3:-v_base}
… (14 行略) …
+        print(f"{'variant':<20}" + "".join(f"{'hl' + format(h, 'g') + ' LS':>9}{'Lnet':>8}{'TO':>6}" for h in (5, 10, 20)))
+        for vid, r in rows:
+            sw = {x["halflife"]: x for x in r["books"]["sweep"]}
+            print(f"{vid:<20}" + "".join(
+                f"{f(sw[h]['ls_sharpe']):>9}{f(sw[h]['long_ann'], pct=True):>8}{sw[h]['ls_turnover']:>6.0%}"
+                if h in sw else f"{'—':>23}" for h in (5.0, 10.0, 20.0)))
 
     users = {k: r for k, r in res.items() if "books_user" in r}
     if users:
@@ -75,8 +87,8 @@ for path in args:
 
     b0 = res.get(base)
     if b0 and "books" in b0:
-        print(f"\n半衰期扫描 {base}(fit 段): " + "  ".join(
-            f"hl{s['halflife']:g}: LS {f(s['ls_sharpe'])} L {f(s['long_sharpe'])} TO {s['ls_turnover']:.0%}"
+        print(f"\n半衰期扫描 {base}(fit 段; LS = 扣费多空夏普, Lshp = 纯多头夏普): " + "  ".join(
+            f"hl{s['halflife']:g}: LS {f(s['ls_sharpe'])} Lshp {f(s['long_sharpe'])} TO {s['ls_turnover']:.0%}"
             for s in b0["books"]["sweep"]))
     for vid, r in res.items():
         if r.get("profile"):
```

**10-03 23:42 · Bash** — Read study.sh and list recent logs across studies

```bash
cd /Users/wxy/Desktop/Partura && cat scripts/study.sh | sed -n 1,98p; echo; echo "--- logs around"; stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" logs/* | sort | tail -40; echo; grep -rln "固定半衰期" notes/ docs/ scripts/ 2>/dev/null
```

```
#!/bin/bash
# One study's lifeline to the server.  Run from the Mac, in ~/Desktop/Partura.
# Each subcommand touches ONLY this study's files (configs/<fid>.yaml, studies/<fid>/, notes/<fid>/,
# runs/<fid>/), so several studies can run side by side without stepping on each other.
#
#   study.sh ops [regex]                   list operators (name, face/family/category, windows) — the vocabulary
#   study.sh src <operator> [...]          print the server's kernel source of an operator (the source of truth)
#   study.sh check <fid>                   parse every expression of the config on the server (do this before `run`)
#   study.sh decompose <fid>               operator dossiers + SSA decomposition + lab priors, on the server
#   study.sh propose <fid>                 candidate experiments derived from the tree (a DRAFT to curate)
#   study.sh run <fid> <tag> <stage...>    push config, start the stages on the server (returns at once)
#   study.sh final <fid> <tag> <stage>     same, but reads the HOLDOUT (once per study -- it is ledgered)
#   study.sh exec <fid> <tag> <script.py>  run studies/<fid>/<script.py> on the server (returns at once)
#   study.sh wait <fid> <tag> [seconds]    wait (default 540 s) for that job; on completion pull + print the digest
#   study.sh digest <fid> <tag> [base_id]  re-print the digest of a finished run
#   study.sh report <fid>                  push notes, build the report on the server, pull the .md back
#   study.sh status                        what Partura jobs are on the server right now
set -u
cd "$(dirname "$0")/.."
PY=${PY:-$HOME/.venvs/alphacube/bin/python}
HOST=root@connect.westd.seetacloud.com
SSH="ssh -o BatchMode=yes -o ControlPath=none -o ConnectTimeout=30 -p 29982"
RS="rsync -a --exclude __pycache__ -e"
R=/root/autodl-tmp/Partura
ENV="cd $R && export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:$R ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=\${PARTURA_SLOTS:-2}"
RPY=/root/miniconda3/envs/quant/bin/python
cmd=${1:-}; shift || true

push() {   # this study's inputs only
  local fid=$1
… (92 行略) …
2026-10-03 23:04:28 logs/F102_kurt_autocorr_x3.log
2026-10-03 23:05:06 logs/F105_std_fangzheng_covamt_x2_longleg.log
2026-10-03 23:11:01 logs/F105_std_fangzheng_covamt_final.log
2026-10-03 23:12:38 logs/F104_kurt_masktop_amt_S4_long.log
2026-10-03 23:15:26 logs/F102_kurt_autocorr_final.log
2026-10-03 23:19:18 logs/F103_amt_dw_decay_S2_distil.log
2026-10-03 23:20:57 logs/F104_kurt_masktop_amt_x2.log
2026-10-03 23:21:38 logs/F101_day_shine_retstd_audit1.log
2026-10-03 23:26:42 logs/F103_amt_dw_decay_final.log
2026-10-03 23:29:54 logs/F105_std_fangzheng_covamt_audit1.log
2026-10-03 23:33:38 logs/F102_kurt_autocorr_audit1.log
2026-10-03 23:33:50 logs/F104_kurt_masktop_amt_final.log
2026-10-03 23:36:48 logs/F101_day_shine_retstd_rev1.log
2026-10-03 23:41:08 logs/F101_day_shine_retstd_rev2.log

notes/F101_day_shine_retstd/09_diagnosis.md
notes/F101_day_shine_retstd/07x_look3.md
notes/F103_amt_dw_decay/08_variants.md
docs/study_playbook.md
scripts/summarize.py
```

**10-03 23:42 · Bash** — Read shorter note files

```bash
cd /Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay && for f in 01_expression.md 04_grammar.md 07_neutralise.md 07_conditional.md 07_controls.md 08_variants.md 11_risks.md 12_next.md; do echo "=================== $f"; cat -n $f; done
```

```
=================== 01_expression.md
     1	**来历**:挖掘库 #820(GP 搜出来的)。用户表里公布的那一行:方向 −、半衰期 2,扣费多空夏普 训练 +3.53 / 测试 +3.18,多头腿年化毛超额 +12.8% / +12.4%。
     2	Partura 自己求值复现了这一行(S0 复现训练段,S_final 复现测试段)。
     3	
     4	**一句话**:它把「当天收盘集合竞价的成交额」乘上「这只股票最近 30 天**平均**日内成交额曲线的粗糙度」的三次方,再取 5 日最大值;
     5	方向为负 —— **成交活跃、而且成交长期挤在少数几分钟里的股票,之后跑输**。
     6	
     7	读完源码、做完拆解之后的版本(证据见第 7~10 节):
     8	
     9	- 七个算子里有三个是多余的:`ts_min(·,1)` 是恒等,`cross_max(·,5)` 只是低通,`day_close(Amt)`(收盘竞价那一根)换成全天成交额反而更好。
    10	  只删这三处(5 个算子),留出段多空夏普 +3.52(原式 +3.18),多头腿净超额 +9.2%(原式 +5.5%)。
    11	- 剩下的骨架是 **成交额水平 × (30 日平均曲线的集中度)^k**。成交额水平是已知家族(F001);集中度这一支是这棵树带来的东西,
    12	  它**只在成交活跃的票里、主要在空头端**有稳定的预测力。两条腿在时间上轮动:2018–2020 和 2024–2025 集中度强,2021–2023 成交额水平强。
    13	- 原式的指数 3 让集中度占了八成权重:多空夏普不差,但多头腿弱(净超额 +5.6% / +5.5%)。把指数降到 2(两条腿各占一半)之后,
    14	  多头腿净超额 +12.3% / +12.6%、纯多头夏普 +2.18 / +2.07,多空夏普 +3.45 / +3.10 —— 这是最终推荐的版本。多头腿多出来的部分来自成交额水平那条腿和更低的换手,不来自集中度。
=================== 04_grammar.md
     1	这棵树的结构语法:
     2	
     3	```
     4	收盘集合竞价成交额(当天,一个数,带成交额尺度)
     5	    × [ 30 日平均日内成交额曲线 → 曲线粗糙度(尺度无关) ]³        # 慢变量,三次方定权
     6	        → 5 日极值记忆
     7	```
     8	
     9	和 F001 的"日内折叠 → 极值 → 乘 → 极值"看起来像,但有两处本质不同,所以不能套 F001 的问题清单:
    10	
    11	- **30 日记忆在日内折叠的里面,不在外面。** F001 是"每天算一个统计量,再在日轴上取极值";
    12	  这里是"先在日轴上把 241 条曲线平均成一条,再对平均曲线算统计量"。于是 `C` 天生是个**慢变量**
    13	  (相邻两天共用 29/30 的输入),不需要外面再套记忆;外层 `cross_max(·, 5)` 实际上只是在给 `A`
    14	  (逐日抖动的收盘竞价额)取 5 日峰值。
… (58 行略) …
     9	- **容量与成本。** 多头端是全市场成交额最低的那一两成股票;日换手 3.5%~3.9%(半衰期 10),15 bp 单边成本下多头腿每年付出约 3 个点(毛 +15.6% → 净 +12.6%)。
    10	  实际冲击成本在这类股票上会明显高于 15 bp,净超额对成本假设敏感。
    11	- **对平滑方式的依赖。** 原始日频面板不平滑时多空夏普只有 +1.17(换手 27%),半衰期 10 才到 +3.33;而且平滑必须作用在**原始数值**上(重尾 → 带衰减的峰值记忆),
    12	  先取 `log` 或排名再平滑会掉 0.7~1.1 个夏普(X3-H)。换一套组合 / 平滑流程(比如先截面标准化再 EMA),这个因子的表现会变。
    13	  同理,单日的异常成交额(数据错误、复牌首日)会在信号里停留十来天。
    14	- **制度依赖。** (a) 241 根分钟网格的版式:9:30 那根是开盘集合竞价、15:00 那根是收盘集合竞价;沪市 2018-08-20 之前没有收盘集合竞价,那 7 个半月 `C` 在沪深之间有系统性差异(X2-c)。
    15	  交易所再改竞价规则,`C` 的截面分布会跟着变。(b) 标签剔除了次日开盘封涨停买不进的票;空头端五分之一是近期打过板的票,涨跌停制度改变会直接影响空头腿。
    16	- **泄漏。** 没有发现:所有日轴算子的因果性探针通过,标签是 t+1 开盘 15 分钟 VWAP 到 t+2 同一价,因子只用到 t 日 15:00。
    17	- **过拟合。** 全研究在 train / valid 上看过 24 个引擎变体和三份脚本里约 80 行数值重建;最终结构只有两个参数(平均窗口 30、指数 2),邻域(窗口 10~60、指数 1~3、DW / 峰值占比 / CV)都是平台或单调曲线,没有孤立的尖峰。
=================== 12_next.md
     1	只列能明显降低不确定性的:
     2	
     3	1. **把空头端那个角当成剔除名单来测。** 这棵树最稳的发现是"成交最活跃 × 平均曲线最集中"的 4% 股票次日年化 −75% 上下(train / valid 都是)。
     4	   对一个纯多头的使用者,它的用法不是十分位多头书,而是从任何多头组合里剔掉这些票。需要一个带持仓约束的组合回测,十分位口径回答不了。
     5	2. **集中度那条腿在 2024–2025 年是不是真的回来了。** 留出段的排序(`f_sum_k3` > `f_sum_k2` > `f_stdamt9`)指向"是",但没有直接量过成交额中性的集中度在那段时间的 rank IC。
     6	   等 2026 年的数据进来之后,用新数据量(不要回头再读这段留出段)。它决定指数该往 3 还是往 1 调。
     7	3. **市值中性口径下的多头腿。** 在市值分层内部建多头书(或对市值 + 行业中性),看推荐版的多头腿还剩多少。现在只知道 train / valid 上秩中性化之后剩 +2% 左右。
     8	4. **与 F001 蒸馏结果一起放进组合时的边际贡献。** 两者 rank 相关 0.74;留出段上集中度给已知家族加了 0.59 个多空夏普,但那是乘法合成的结果,不是组合层面的边际。
     9	5. **"开盘第一分钟成交占比"单独立项。** `p_peak` 九成就是它;它在峰值落在开盘的 2,800 多只股票里组内 rank IC −0.046 / −0.021,而"收盘集合竞价占比"方向不稳。
    10	   这是一个比 DW 更可解释的集中度写法,值得作为独立因子走一遍同样的流程(这次没有把它放进留出段)。
```

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x1_anatomy.md`

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/logs/F103_amt_dw_decay_x1.log`

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x2_interaction.md`

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/logs/F103_amt_dw_decay_x2.log`

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x3_family.md`

10-03 23:43 · 读 `/Users/wxy/Desktop/Partura/logs/F103_amt_dw_decay_x3.log`

**10-03 23:45 · Bash** — Outline report headings and search for failure markers

```bash
cd /Users/wxy/Desktop/Partura && wc -l research/alpha_distillation/F103_amt_dw_decay.md && grep -n "^#" research/alpha_distillation/F103_amt_dw_decay.md | head -100; echo ---; grep -n "求值失败\|失败\|nan\|NaN\|None\|ERROR\|error\|缺失\b" research/alpha_distillation/F103_amt_dw_decay.md | head -40
```

```
    1326 research/alpha_distillation/F103_amt_dw_decay.md
1:# Alpha 研究报告 — F103_amt_dw_decay
11:## 1. 原始表达式
32:## 2. 算子的真实语义
36:### `day_close`
46:### `cross_decay_linear`
55:### `day_durbin_watson`
65:### `pow_3`
73:### `ts_min`
82:### `mul`
90:### `cross_max`
121:### 既往研究留下的先验
155:## 3. 数学分解
200:## 4. 结构语法
220:## 5. 竞争性假设
261:## 6. 基线指标
356:## 7. 消融实验
358:### S0_baseline
374:### S1_structure
450:### S2_distil
529:### S_final
570:### 中性化(fit 段)
670:### 条件 IC(fit 段)
693:### 控制变量自己当因子(同口径)
1014:## 8. 语义变体
1086:## 9. 机制诊断
1091:### 已确立(每条后面是实验)
1115:### 合理但没坐实
1124:### 未决
1132:### 假设的判决
… (22 行略) …
71:- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, monotone_in_window, effective_memory, isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback</sub>
78:- **实测探针**: 日轴因果性 = True; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = odd; 窗口变长 = non_increasing; 脉冲记忆天数 = 1
80:- <sub>不适用的探针: order_dependent_on_minutes, rank_preserving, isolated_spike_response, noise_averaging_exponent, trailing_nan_fallback</sub>
85:- **声明**: face `shared` / family `elementwise` / category `binary`, arity 2, 计算轴 `None`, 无窗口
87:- **实测探针**: 平移不变 = False; 齐次度 k = 2.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = even
88:- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback</sub>
95:- **实测探针**: 日轴因果性 = True; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.9948, all_nan_input_gives_all_nan=True; 取负后 = neither; 窗口变长 = non_decreasing; 脉冲记忆天数 = 5
97:- <sub>不适用的探针: order_dependent_on_minutes, rank_preserving, isolated_spike_response, noise_averaging_exponent, trailing_nan_fallback</sub>
107:- `nan_behaviour` — 10% 缺失下还剩多少有限值?整行缺失会怎样?
113:- `trailing_nan_fallback` — 当天最后 3 根是 NaN 时,输出等于哪一根?(读的是'最后一个有效分钟'还是固定的最后一列)  _(本研究新增,来自 `probes.py`)_
114:- `window_one_is_identity` — 窗口取 1 时是不是恒等变换?(数值和 NaN 位置都不变)  _(本研究新增,来自 `probes.py`)_
136:  (权重 1…30,当天最重;缺失的天从分母里剔掉,所以前 29 天也有值)。输出仍然是一条 241 点的日内曲线 ——
144:- **`day_close(Amt)` 是"最后一个非 NaN 分钟"的成交额**(`day_last` 的别名),不是收盘价、也不是全天成交额。
147:- **`ts_min(·, 1)` 是恒等变换**:`rolling_windows(x, 1)` 不补任何行,`nanmin` 在单元素窗口上就是它自己。
152:- **`cross_max(·, 5)`**:最近 5 个交易日(含当天)的 NaN 跳过最大值;全 NaN 才给 NaN。停牌日也有值(沿用前 4 天的最大值)。
240:| **H8b** | **空头腿被标签口径抬高**:t+1 开盘封涨停买不进的票标签是 NaN,在空头里记 0 | 口径本身如此;高 `G` 名单里涨停票多 | 空头十分位里标签缺失的比例远高于全市场 | X1 的各十分位标签缺失率 |
719:**1. `ts_min(·, 1)` 是恒等。** 删掉它之后与原式的 rank 相关 1.000000,NaN 位置一致率 1.000000,最大相对差 0。
771:**空头腿就是"近期打过板的活跃票"**(H8 成立)。标签缺失率 Q1 1.25%、Q10 2.48%、全市场 1.54% ——
772:空头端的缺失比全市场还低,**H8b(空头腿被"买不进记 0"抬高)不成立**;缺失多的反而是多头端。
1106:   对全部控制变量中性化后空头腿从 +42.8% 掉到 +9.1%。空头腿没有被"封涨停买不进记 0"抬高:空头十分位的标签缺失率 1.25%,低于全市场的 1.54%(H8b 不成立)。
```

10-03 23:45 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:45 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:45 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:45 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

**10-03 23:45 · Bash** — Verify rank correlations cited in notes and view run logs

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
s1=json.load(open("runs/F103_amt_dw_decay/S1_structure.json"))["diagnostics"]["rank_corr_train"]
s2=json.load(open("runs/F103_amt_dw_decay/S2_distil.json"))["diagnostics"]["rank_corr_train"]
print("a_C-f_share", s1["a_C"].get("f_share"))
print("x_std9_k1 - w15, w60", s2["x_std9_k1"].get("x_std9_k1_w15"), s2["x_std9_k1"].get("x_std9_k1_w60"))
print("d_sum_k3-d_sum_k2", s2["d_sum_k3"].get("d_sum_k2"), "d_sum_k2-d_sum_k1", s2["d_sum_k2"].get("d_sum_k1"), "x_std9_k1-b_stdamt9", s2["x_std9_k1"].get("b_stdamt9"))
print("m_mean5/e_pow2/i_addrank vs ref_base", s1["m_mean5"]["ref_base"], s1["e_pow2"]["ref_base"], s1["i_addrank"]["ref_base"])
print("a_A5 known_amt_max9", s1["a_A5"]["known_amt_max9"], s1["a_A5"]["ctl_amt"])
print("g_stdB known_stdamt", s2["g_stdB"]["known_stdamt_max9"], "b_stdamt9", s2["g_stdB"].get("b_stdamt9"))
print("e_peak_k2 ref_C?", s2["e_peak_k2"].get("ref_C"))
# S1 a_C TO, etc
EOF
echo ---; cat logs/F103_amt_dw_decay_final.log | grep -av "FutureWarning\|vmap" | head -40; echo ---; cat logs/F103_amt_dw_decay_S2_distil.log | grep -av "FutureWarning\|vmap" | head -40
```

```
a_C-f_share 0.9334201830532388
x_std9_k1 - w15, w60 0.9828279428901346 0.9851254802589221
d_sum_k3-d_sum_k2 0.9291446612546994 d_sum_k2-d_sum_k1 0.9183508013717614 x_std9_k1-b_stdamt9 0.9303417300849606
m_mean5/e_pow2/i_addrank vs ref_base 0.9772344163767025 0.9485507313502415 0.9524196552704892
a_A5 known_amt_max9 0.8807545592756039 0.8656588358540976
g_stdB known_stdamt 0.9164496409593237 b_stdamt9 0.9164496409593237
e_peak_k2 ref_C? -0.2474675105441897
---
[probes] studies/F103_amt_dw_decay/probes.py: +isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback
[runner] 14:23:39 label == /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy
[runner] 14:23:40 metrics: 5 variants; decision splits ['train', 'valid'], fit on 'train'; HOLDOUT WILL BE READ
[runner] 14:25:35 diagnostics: by_year
[runner] 14:25:43 diagnostics: rank correlation matrix (19 panels)
[runner] wrote /root/autodl-tmp/Partura/runs/F103_amt_dw_decay/final.json (184.0s, peak anon 2.61 GiB)
[partura exit 0 2026-10-04_14:26:42]
---
[guard] all 2 run slots busy, waiting ...
[guard] got run slot 0 after 147s
[probes] studies/F103_amt_dw_decay/probes.py: +isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback
[panels] 6 new expression(s) on 1942d x 5220s (+0 warm-up), device=cuda, batches of 3
[panels] GPU: 7.9 GiB free of 31.4; this run capped at 12% (3.9 GiB), chunk 334 MiB
[panels]   3/6 (12s)
[panels] GPU: 7.8 GiB free of 31.4; this run capped at 12% (3.8 GiB), chunk 327 MiB
[panels]   6/6 (28s)
[panels] done in 28s
[runner] 14:11:31 label == /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy
[runner] 14:11:31 metrics: 12 variants; decision splits ['train', 'valid'], fit on 'train'
[runner] 14:15:34 diagnostics: decay
[runner] 14:15:43 diagnostics: by_year
[runner] 14:15:54 diagnostics: neutralise (4 variants x 9 controls, on the traded signal)
[runner] 14:17:14 diagnostics: conditional IC
[runner] 14:17:32 diagnostics: rank correlation matrix (26 panels)
[runner] wrote /root/autodl-tmp/Partura/runs/F103_amt_dw_decay/S2_distil.json (496.2s, peak anon 4.16 GiB)
[partura exit 0 2026-10-04_14:19:18]
```

**10-03 23:46 · Bash** — Check analysis scripts for data-split usage

```bash
cd /Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay && grep -n "holdout\|full\|slice(\|\.dates\|2023\|2024\|2025\|utrain\|evals=\|fit=" x1_anatomy.py x2_interaction.py x3_family.py | head -120
```

```
x1_anatomy.py:31:    "bar0": "day_sum(in_slice(Amt, 0, 0))",
x1_anatomy.py:32:    "bar1": "day_sum(in_slice(Amt, 1, 1))",
x1_anatomy.py:33:    "bar238_239": "day_sum(in_slice(Amt, 238, 239))",
x1_anatomy.py:34:    "bar240": "day_sum(in_slice(Amt, 240, 240))",
x1_anatomy.py:35:    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
x1_anatomy.py:53:        sh = np.full_like(x, np.nan)
x1_anatomy.py:63:        sh = np.full(x.shape, np.nan)
x1_anatomy.py:85:    tr, va = st.slice("train"), st.slice("valid")
x1_anatomy.py:87:    dates = np.asarray(st.dates)
x1_anatomy.py:108:               "valid": (dates >= "20220101") & (dates <= "20230807")}
x1_anatomy.py:201:        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
x3_family.py:27:    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
x3_family.py:32:    "p_bar1": f"div(day_sum(in_slice({B}, 1, 1)), day_sum({B}))",
x3_family.py:60:    tr, va = st.slice("train"), st.slice("valid")
x3_family.py:61:    use = slice(tr.start, va.stop)                       # train + valid only; holdout rows are never indexed
x3_family.py:65:    dates = np.asarray(st.dates)
x3_family.py:72:        ysl[y] = slice(int(idx[0]), int(idx[-1]) + 1)
x3_family.py:100:        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
x3_family.py:163:            rk = np.full(x.shape, np.nan)
x3_family.py:208:    capP = np.full(cap.shape, np.nan)
x3_family.py:210:    amtP = np.full(amt.shape, np.nan)
x3_family.py:225:        res = np.full(p.shape, np.nan)
x3_family.py:264:    for sname, sl in (("2018-01..08-17", slice(tr.start, int(np.searchsorted(dates, "20180820")))),
x3_family.py:265:                      ("train 其余", slice(int(np.searchsorted(dates, "20180820")), tr.stop)), ("valid", va)):
x2_interaction.py:29:    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
x2_interaction.py:32:    "p_first2": f"div(day_sum(in_slice({B}, 0, 1)), day_sum({B}))",
x2_interaction.py:33:    "p_open10": f"div(day_sum(in_slice({B}, 0, 10)), day_sum({B}))",
x2_interaction.py:48:            sh = np.full_like(x, np.nan)
x2_interaction.py:55:        sh = np.full(x.shape, np.nan)
x2_interaction.py:77:    tr, va = st.slice("train"), st.slice("valid")
x2_interaction.py:78:    use = slice(tr.start, va.stop)                       # train + valid only; holdout rows are never indexed
x2_interaction.py:80:    dates = np.asarray(st.dates)
x2_interaction.py:91:        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
x2_interaction.py:109:    eps = np.full(C.shape, np.nan)
```

**10-03 23:46 · Bash** — Inspect split handling in analysis scripts

```bash
cd /Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay && sed -n 80,125p x1_anatomy.py; echo ----; sed -n 56,110p x3_family.py; echo ---; grep -n "years\|for y in\|ysl" x2_interaction.py x3_family.py | head -30
```

```
T0 = time.time()
with Study("F103_amt_dw_decay") as st:
    P = st.panels(EXPR)
    print("[x1] panels:", sorted(P), f"{time.time() - T0:.0f}s", flush=True)
    tr, va = st.slice("train"), st.slice("valid")
    tgt = st.target()
    dates = np.asarray(st.dates)
    syms = np.asarray(st.symbols)
    print("[x1] dates", dates[0], dates[tr][-1], dates[va][0], dates[va][-1], "| symbols", list(syms[:3]), list(syms[-3:]), len(syms))
    G, A, C, dsum = P["G"], P["A"], P["C"], P["dsum"]

    # ---------- 1. ts_min(., 1) ----------
    print("\n== 1. ts_min(.,1) 是不是恒等 ==")
    g2 = P["G_nomin"]
    same_nan = float((np.isfinite(G[tr]) == np.isfinite(g2[tr])).mean())
    both = np.isfinite(G[tr]) & np.isfinite(g2[tr])
    rel = np.abs(G[tr][both] - g2[tr][both]) / np.maximum(np.abs(G[tr][both]), 1e-30)
    print(f"rank corr(G, G 去掉 ts_min) = {st.rank_corr(G, g2):.6f}; NaN 位置一致率 {same_nan:.6f}; 最大相对差 {rel.max():.3e}")

    # ---------- 2. 241 网格首尾放的是什么 ----------
    print("\n== 2. 首尾分钟的成交额占全天的比例(格子中位数) ==")
    is_sh = np.asarray([s.startswith("6") or s.upper().endswith("SH") or s.upper().startswith("SH") for s in syms])
    is_sz = np.asarray([(s[:1] in "03" or s.upper().endswith("SZ") or s.upper().startswith("SZ")) and not sh
                        for s, sh in zip(syms, is_sh)])
    print(f"沪市 {is_sh.sum()} 只, 深市 {is_sz.sum()} 只, 其他 {(~is_sh & ~is_sz).sum()} 只")
    periods = {"2018-01-02~08-17": (dates >= "20180102") & (dates <= "20180817"),
               "2018-08-20~2021": (dates >= "20180820") & (dates <= "20211231"),
               "valid": (dates >= "20220101") & (dates <= "20230807")}
    with np.errstate(divide="ignore", invalid="ignore"):
        shares = {k: P[k] / dsum for k in ("bar0", "bar1", "bar238_239", "bar240", "A") if k in P}
… (70 行略) …
        return sg, b["hl_used"]
---
x2_interaction.py:81:    years = np.asarray([d[:4] for d in dates])
x2_interaction.py:114:    yy = sorted(set(years[use].tolist()))
x2_interaction.py:115:    print(f"{'':26s} " + "  ".join(f"{y:>7s}" for y in yy))
x2_interaction.py:118:        print(f"{n:26s} " + "  ".join(f"{np.nanmean(ric[years[use] == y]):+.4f}" for y in yy))
x2_interaction.py:126:        print(f"{lab:26s} " + "  ".join(f"{np.nanmean(ric[years[use] == y]):+.4f}" for y in yy))
x2_interaction.py:162:           "2019": years[use] == "2019", "2020~2021": (years[use] == "2020") | (years[use] == "2021")}
x3_family.py:66:    years = np.asarray([d[:4] for d in dates])
x3_family.py:67:    yy = sorted(set(years[use].tolist()))
x3_family.py:68:    ysl = {}
x3_family.py:69:    for y in yy:
x3_family.py:70:        idx = np.nonzero(years == y)[0]
x3_family.py:72:        ysl[y] = slice(int(idx[0]), int(idx[-1]) + 1)
x3_family.py:170:    print(f"{'':22s} hl  " + "  ".join(f"{y:>20s}" for y in yy))
x3_family.py:178:        for y in yy:
x3_family.py:179:            r = bk.book_row(sm, tgt, ysl[y], cost, top)
x3_family.py:180:            cells.append(f"{np.nanmean(ric[years[use] == y]):+.4f} {r['ls_sharpe']:+5.2f} {r['long_ann'] * 100:+6.1f}")
x3_family.py:190:    print(f"{'':22s} {'中性化对象':14s}  R2    train    valid   | " + "  ".join(f"{y:>7s}" for y in yy))
x3_family.py:203:                  + "  ".join(f"{np.nanmean(ric[years[use] == y]):+.4f}" for y in yy), flush=True)
```

**10-03 23:46 · Bash** — Read operators, decomposition and hypotheses notes

```bash
cd /Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay && cat -n 02_operators.md 03_decomposition.md; echo ======; cat -n 05_hypotheses.md | cut -c1-900
```

```
Exit code 1
     1	七个算子的内核源码逐个读过(`study.sh src`),和名字不一样、或者探针表里看不出来的地方:
     2	
     3	- **`cross_decay_linear(Amt, 30)` 不是截面运算,也不是把一天压成一个数**。`Amt` 是 (天, 股票, 241 分钟) 的立方体,
     4	  `cross_*` 沿**交易日轴**滚:对每只股票的**每一个分钟槽位**,取最近 30 个交易日同一分钟的成交额做线性衰减加权平均
     5	  (权重 1…30,当天最重;缺失的天从分母里剔掉,所以前 29 天也有值)。输出仍然是一条 241 点的日内曲线 ——
     6	  **这只股票最近 30 天的"平均日内成交额曲线"**。权重的有效样本数是 (Σw)²/Σw² = 465²/9455 ≈ 22.9 天。
     7	- **`day_durbin_watson` 在这里既不是自相关检验,也不是 F001 里的"已实现方差"**。源码是
     8	  `Σ_m (x_m − x_{m−1})² / (Σ_m x_m² + 1e−8)`,分母是 Σx² 不是方差(探针:齐次度 0、平移不变 = False)。
     9	  F001 喂的是价格水平,所以 ≈ 分钟收益的方差;这里喂的是**一条非负的成交额曲线**,它量的是这条曲线的
    10	  **粗糙度/尖峰度**:曲线越平滑(相邻分钟差不多)越接近 0,孤立尖峰越多越接近 2。
    11	  对一条"水平 b 上叠加独立噪声"的曲线,DW ≈ 2·CV²/(1+CV²);对一个孤立在末端的尖峰 s,它贡献 ≈ s²/Σx²。
    12	  实验室里那条"DW 作用在价格水平上 ≈ 已实现方差"的先验在这棵树上**不适用**(操作数换了)。
    13	- **`day_close(Amt)` 是"最后一个非 NaN 分钟"的成交额**(`day_last` 的别名),不是收盘价、也不是全天成交额。
    14	  在 241 网格上最后一根是 15:00,A 股的收盘集合竞价(14:57–15:00)撮合量记在这一根上 ——
    15	  它实际上是**收盘集合竞价成交额**(X1 第 2 节核对了版式)。
    16	- **`ts_min(·, 1)` 是恒等变换**:`rolling_windows(x, 1)` 不补任何行,`nanmin` 在单元素窗口上就是它自己。
    17	  它在树里的唯一作用是把 dt 面的日频量"过"到 nd 面,数值上什么都没做(X1 第 1 节:与删掉它的版本逐格相同)。
    18	- **`pow_3` 走的是 `pow_`**:指数 > 1 时是普通的 `x**3`(≤ 1 时才是带符号幂)。`C ≥ 0`,所以保序;
    19	  对逐日排名是 no-op,但它在 `mul` 的里面,决定的是 `C` 相对于 `A` 的权重(log 空间里系数 3)。
    20	  (X3-H 之后的补充:即使放在最外层,保序变换在这套口径下也不是 no-op —— 书是先对原始数值做 EMA 再排名的,指数还决定尾部有多重。)
    21	- **`cross_max(·, 5)`**:最近 5 个交易日(含当天)的 NaN 跳过最大值;全 NaN 才给 NaN。停牌日也有值(沿用前 4 天的最大值)。
    22	- **回看长度**:30(平均曲线)+ 5(极值)− 1 = 34 个交易日;AlphaCube 的 `max_window` 取 30。
     1	把上表写成公式(m 是 241 网格上的分钟,t 是交易日,w_j = 30 − j):
     2	
     3	```
     4	B_t(m) = Σ_{j=0..29} w_j · Amt_{t−j}(m) / Σ w_j          # 每个分钟槽位各自做 30 日线性衰减平均
     5	C_t    = Σ_{m≥2} (B_t(m) − B_t(m−1))²  /  Σ_m B_t(m)²     # 平均曲线的粗糙度,尺度无关,取值约在 [0, 2]
     6	A_t    = Amt_t(最后一个有效分钟)                          # 收盘集合竞价成交额,带成交额尺度
     7	G_t    = max_{k=0..4} A_{t−k} · C_{t−k}³                   # ts_min(·,1) 是恒等;pow_3 只是给 C 定权
     8	```
     9	
    10	三个容易被名字骗的地方:
    11	
    12	1. **"先平均、再量粗糙度"和"先量粗糙度、再平均"不是一回事。** 逐日独立的分钟噪声在 `B` 里被压到约 1/4.8
    13	   (有效样本 22.9 天),所以 `C` 里剩下的只有两类东西:**每天都出现在同一分钟的结构**(开盘/收盘集合竞价那两根、
    14	   午休前后的跳变)和**大到 30 天都平均不掉的单分钟尖峰**。`cross_decay_linear(day_durbin_watson(Amt), 30)`
    15	   则是每天粗糙度的平均,逐日噪声全在里面。两种写法的差别是 H4,X1 第 6 节直接量。
    16	2. **`A` 和 `C` 不是两路独立信号。** `A` 是今天的收盘竞价额,`C` 的分子里有平均曲线末端那根的平方
    17	   `B(15:00)²`(14:58、14:59 两根是 0,所以这根是孤立尖峰)。尾盘竞价占比高的股票,两支同时偏高。
    18	3. **整棵树在 log 空间是 `log A + 3·log C`**(外面的 5 日极值不改变这个结构)。`A` 带成交额尺度、`C` 不带;
    19	   两支谁主导排名取决于 `log A` 和 `3·log C` 的截面离散度,而不是取决于谁"更重要" —— X1 第 3 节量了。
(eval):1: ===== not found
```

**10-03 23:46 · Bash** — Skim hypotheses note

```bash
cd /Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay && cut -c1-700 05_hypotheses.md | head -60
```

```
下面的假设是**读完七个算子的内核源码之后、跑任何实验之前**写的(基线 S0 的数字是唯一已知的事实)。
每条给出「它预测什么」和「哪个实验能杀死它」。X1 是自己写的数据解剖脚本(`studies/F103_amt_dw_decay/x1_anatomy.py`),
S1~S4 是配置里的阶段。实验跑完之后的判决写在第 9 节,这里不回改。

记号:`A = day_close(Amt)`(当天最后一根有效分钟的成交额),`B = cross_decay_linear(Amt, 30)`
(每只股票**每个分钟槽位**最近 30 个交易日的线性衰减均值 —— 一条"平均日内成交额曲线"),
`C = day_durbin_watson(B) = Σ(ΔB)² / ΣB²`(这条平均曲线的粗糙度,尺度无关),原式 `G = cross_max(A · C³, 5)`。

| | 假设 | 为什么合理 | 它预测什么 | 证伪实验 |
|---|---|---|---|---|
| **H1** | **成交额水平的另一种写法**:`A` 带成交额尺度(齐次度 1),外面又是 `cross_max`,与 F001 的 `cross_max(day_sum(Amt), 9)` 同族 | 这是本项目里最强的已知家族;`day_close(Amt)` 与全天成交额应高度相关 | `A` 支单独配 5 日极值 ≈ `known_amt_max9`;`A` 换成 `day_sum(Amt)` 整树不变;对 `ctl_amt` 中性化后预测力大半消失 | 基线已部分否定(与 `ctl_amt` 的 rank 相关 0.28,R² 0.081);S1 的 `a_A_only`、S2 的 `f_sum`(换字段)给最终判决 |
| **H2** | **`C` 量的是集合竞价尖峰**:241 网格上 9:30 那根含开盘集合竞价、15:00 那根含收盘集合竞价(14:58/14:59 两根应为 0),平均曲线在首尾各有一个孤立尖峰,DW 分子里 `B_close²` 和 `(B_931 − B_930)²` 是大项 | 直接从 DW 的公式和 A 股分钟数据的版式推出来 | `C` 与"平均曲线的尾盘占比"高相关;把 DW 的操作数切掉首尾(`in_slice(B, 2, 237)`)之后 `C` 换了一个东西、整树预测力明显变化 | X1(`C` 对各成分的 rank 相关)+ S2 的 `c_inner` |
| **H3** | **`C` 量的是成交的"块状/突发性"**:30 日平均压掉的只是逐日独立的噪声(有效样本 ≈ 23 天,噪声幅度降到 1/4.8),剩下的是没被平均掉的大单脉冲;越冷清、越靠少数几笔大单成交的票 `C` 越高 | 同一公式的另一半:内部分钟的逐差平方和 | `C` 与切掉首尾后的内部 DW 高相关、与成交额水平负相关;朴素等价物是平均曲线的变异系数 `day_std(B)/day_mean(B)` | X1 + S2 的 `c_cv` |
| **H4** | **"先平均再量粗糙度"才是关键**:`DW(decay30(Amt))`(平均曲线的粗糙度)≠ `decay30(DW(Amt))`(每天粗糙度的平均)。前者只留下**在同一分钟反复出现**的结构和没平均掉的巨大尖峰 | 两个算子不可交换;GP 选了前者 | 两种写法 rank 相关明显低于 0.95,且前者配进整树更好;30→10/60 改变的是"多大的尖峰能留下来" | S2 的 `c_swap`;S3 的窗口邻域 |
| **H5** | **`pow_3` 是定权,不是机制**:在 log 空间 `log G ≈ log A + 3·log C`,指数只决定两支谁说了算 | F001 里三次方就是多余的;保序变换只能在乘法里改权重 | 指数 k 从 0(纯 `A`)到 ∞(纯 `C`)表现连续变化,k=3 不是尖峰;k=1、2 相差不大 | X1 的 k 扫描(数值重建,先核对 k=3 与引擎面板 rank 相关 = 1)+ S1 的 `e_pow1`/`e_pow2` |
| **H6** | **乘法在"约掉尺度"**:如果 `C` 与成交额水平负相关,`A·C³` 里成交额尺度被部分抵消,剩下的是"相对于自身流动性的尾盘量",即一个尺度无关的**尾盘成交占比**类信号(A 股已知的"尾盘成交占比"因子) | 基线里整树与 `ctl_amt` 的相关只有 0.28,远低于一个齐次度 1 的量应有的水平 | `G` 与 `A/day_sum(Amt)` 的相关高于与 `A` 或 `C` 单独的相关;显式比率版配同样记忆能复现大部分表现 | X1 + S2 的 `r_share` |
| **H7** | **`cross_max(·,5)` 只是低通**:`A·C³` 恒正、`C` 变化很慢,5 日最大值主要是在 `A` 上取峰值;按实验室先验,恒正的水平量取极值不是"取幅度" | lab finding:操作数恒正时极值只是低通 | 换成 `cross_mean`、或者直接删掉靠 EMA 半衰期,表现相近;窗口 3/10/15 是平台 | S3 的 `m_mean5`、`m_none`、`m_max3/10/15` |
| **H8** | **空头腿主导 = 热门股崩塌**:高 `G` 的是近期出现过成交尖峰、尾盘又放量的票(涨停打开、消息股),之后大跌;低 `G` 端只是安静股的温和正超额 | 基线 Q1 −43.8%,而 Q7~Q10 在 +10%~+14% 之间几乎是平的;按 `ctl_amt` 分桶的条件 IC 从 −0.011 单调走到 −0.054 | 空头十分位在成交额/波动/动量上都排在前面;多头端的排序力来自哪一支,决定了能不能升华 | X1 的十分位画像;各支单独的分位剖面 |
| **H8b** | **空头腿被标签口径抬高**:t+1 开盘封涨停买不进的票标签是 NaN,在空头里记 0 | 口径本身如此;高 `G` 名单里涨停票多 | 空头十分位里标签缺失的比例远高于全市场 | X1 的各十分位标签缺失率 |
| **H9** | **制度伪影**:沪市 2018-08-20 才引入收盘集合竞价,之前 `day_close(Amt)` 对沪市是连续竞价的最后一分钟,对深市是 3 分钟集合竞价的成交;`A` 在 2018 年前 8 个月会按交易所把股票分开 | 交易所规则 | `A/day_sum(Amt)` 在沪市 2018-08-20 前后跳变;2018 年的表现有一部分是"做多沪市、做空深市" | X1 的分交易所、分时期对比 |
| **H10** | **窗口是搜出来的幸运参数** | GP 就是在这么搜 | 30→15/60、5→3/10 表现塌掉 | S3 |
| **H11** | **动量 / 波动暴露**:基线中性化里 `ctl_mom20` R² 0.073、`ctl_ivol` 0.064,各自拿走约四分之一的 rank IC | 尖峰事件通常伴随上涨和高波动 | 全部控制变量 R² 只有 0.227、残差 rank IC 还剩 0.0172(无成本夏普 +2.83):**一半在已知暴露里,一半不在** —— 要回答的是"不在的那一半是什么" | 中性化表(对蒸馏候选再做一次) |
| **H12** | **多头腿可以升华**:多头端(低 `G`)的选股力如果主要来自某一支(比如"曲线平滑"),单独用那一支、配更慢的记忆,多头腿净超额应高于原式 | 基线半衰期扫描里多头腿夏普随半衰期单调上升(hl2 +1.30 → hl10 +1.86),说明多头端是慢变量、被原式的快记忆拖累了换手 | 存在一个更简单的变体,train 和 valid 上多头腿净超额都高于原式(+6.3% / +3.6%) | S4
… (821 字符略) …
_stdamt_max9 × C^k` 不比 `known_stdamt_max9` 好 | X3 的相关矩阵、残差 rank IC(逐年)、`stdamt9·C^k` 两行。**残差 rank IC 两段同号且都 > 0.01 就
| **H14** | **稳定的是"系统性的集中度",不是"块状噪声"**:`C` 有 69% 是内部分钟的块状噪声(流动性差的代理),它对成交额中性化之后 2021 年起没有预测力;而 `p_cv` 与成交额几乎无关(与 `max5(A)` 相关 0.067),X2-a 里它的逐年 rank IC 是 −0.042 / −0.055 / −0.047 / −0.028 / −0.030 / −0.027,**没有在 2021 年后归零** | X2-a 的最后一行(当时只是顺带打印的,没有跟进) | 尺度无关的集中度(`p_cv`、`p_peak`)**单独**就有两段同向的多空夏普;对 `ctl_amt` / `ctl_cap` / `ctl_turnrate` 中性化后 rank IC 基本还在;换成 `day_sum × p_peak^k` 之后两段比 `day_sum × C^k` 更平衡 | X3:`p
| **H15** | **valid 上"指数越小多头腿越好"是微盘暴露**:k = 0 的多头腿净超额 +21.0% 来自 2022–2023 年"成交额低 = 小票"的行情,不是这棵树的 alpha | valid 段正好是微盘股行情;`ctl_cap` 自己当因子在 valid 上方向是反的 | 多头十分位的市值分位随 k 减小而下降;对 `ctl_cap` 中性化之后,k = 0 / 1 相对 k = 2 / 3 的 valid 多头腿优势大幅缩小 | X3:各候选多头十分位的市值/成交额分位;市值中性化之后的两本书。**中性化后优势不变就杀死它** |
| **H16** | **集中度对多头腿没有稳定贡献**:X2-b 的 5×5 表里,低成交额那几行 `C` 的方向 train / valid 相反;如果换成系统性的集中度(`p_peak` / `p_cv`)之后两段同向("成交额低且不集中"最好),多头腿就可以用集中度升华;否则多头腿只能靠成交额水平 | X2-b | 5×5(成交额 × `p_peak`)在 train 和 valid 的低成交额行里 C5 − C1 同号 | X3 的两张 5×5 表。**低成交额行里 C5 − C1 两段反号 = 多头腿没有升华空间(这条假设成立)** |
| **H17** | **峰值分钟是固定的制度性分钟**(9:31 开盘第一分钟或 15:00 收盘集合竞价),`p_peak` 量的是"交易有多挤在开盘/收盘",不是某一次大单的记忆 | 9:31 那根中位占全天 1.0%~1.9%,15:00 那根 1.2% | `day_argmax(B)` 九成以上落在第 0/1 根或第 240 根;按峰值位置分组后 `p_peak` 的 rank IC 都在 | X3 的峰值位置分布与分组 rank IC。**若三成以上落在别的分钟,它就混着事件记忆** |
| **H18** | **"保序变换是 no-op"在这套口径下不成立**:书是先对**原始数值**做 EMA 再排名的。`A·C^k` 是重尾的正数,对它做 EMA ≈ 记住近期峰值;对 `log` 做 EMA ≈ 几何平均。所以 `pow_3`、`log` 这类保序变换只在半衰期 = 0 时是 no-op | 读 `books.py` 和 `ema_rows`:平滑在排名之前 | `log(x)` 与 `x` 的十分位书在选中的半衰期 > 0 时不同;多头端(持续低位的票)用 `log` 或排名之后更稳、换手更低 | X3:同一面板的原值 / `log` / 截面排名三种写法的两本书。**三者逐位相同就杀死它** |
```

**10-03 23:47 · Bash** — Print local digest of the final run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F103_amt_dw_decay final f_orig 2>&1 | head -80
```

```
===== F103_amt_dw_decay  [final.json]  1942d x 5220s  splits ['train', 'valid', 'utrain', 'holdout', 'full']  fit=train  184.0s  peak anon 2.61G =====

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
f_orig                 -  +0.0393  +0.0279   2  +4.14  +2.22    +13.5%    +10.9%    +6.3%    +3.6%   24%  8.5%  1.00  1.00
f_sum_k3               -  +0.0410  +0.0336  20  +3.93  +2.88    +13.1%     +9.8%   +11.1%    +7.5%   29%  2.4%  1.00  1.00
f_sum_k2               -  +0.0464  +0.0491  10  +3.33  +3.78    +14.9%    +17.9%   +11.4%   +14.5%   28%  4.0%  1.00  1.00
f_std9_k1              -  +0.0512  +0.0603   2  +3.32  +4.36    +17.5%    +23.2%   +11.5%   +17.7%   29%  7.1%  1.00  1.00
f_stdamt9              -  +0.0484  +0.0671   0  +2.47  +4.44    +16.9%    +24.9%    +9.3%   +18.5%   31%  8.5%  1.00  1.00
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):
variant                hl5 LS    Lnet    TO  hl10 LS    Lnet    TO  hl20 LS    Lnet    TO
f_orig                  +4.13   +8.1%    6%    +4.09   +9.4%    4%    +3.95   +9.5%    2%
f_sum_k3                +3.79   +6.0%    6%    +3.92   +8.8%    4%    +3.93  +11.1%    2%
f_sum_k2                +3.23   +8.1%    6%    +3.33  +11.4%    4%    +3.05  +12.6%    2%
f_std9_k1               +3.20  +13.1%    5%    +2.93  +13.8%    4%    +2.63  +13.2%    2%
f_stdamt9               +2.17  +13.7%    4%    +1.99  +13.1%    3%    +1.79  +12.2%    2%

与用户表同口径(方向/半衰期在 utrain 上定; holdout = 用户的测试段):
variant              sgn  hl  LS utr   LS ho Lgross utr Lgross ho  Lnet utr  Lnet ho Lsharpe utr Lsharpe ho short utr
f_orig                 -   2   +3.53   +3.18     +12.8%    +12.4%     +5.6%    +5.5%       +1.11      +1.04    +38.7%
f_sum_k3               -  10   +3.64   +3.52     +11.8%    +12.3%     +8.4%    +9.2%       +1.66      +1.77    +36.6%
f_sum_k2               -  10   +3.45   +3.10     +15.7%    +15.6%    +12.3%   +12.6%       +2.18      +2.07    +37.5%
f_std9_k1              -   2   +3.58   +3.14     +19.1%    +16.9%    +13.3%   +11.6%       +2.27      +1.55    +43.1%
f_stdamt9              -   0   +2.94   +2.55     +19.2%    +15.2%    +11.9%    +8.2%       +1.82      +0.89    +40.7%

半衰期扫描 f_orig(fit 段; LS = 扣费多空夏普, Lshp = 纯多头夏普): hl0: LS +3.38 Lshp -0.38 TO 14%  hl1: LS +3.86 Lshp +0.69 TO 11%  hl2: LS +4.14 Lshp +1.30 TO 8%  hl3: LS +4.12 Lshp +1.51 TO 7%  hl5: LS +4.13 Lshp +1.62 TO 6%  hl10: LS +4.09 Lshp +1.86 TO 4%  hl20: LS +3.95 Lshp +1.86 TO 2%
分位超额 f_orig [train] Q1..Q10: -43.8% -13.2% -6.0% +0.5% +4.8% +8.3% +12.2% +10.5% +13.0% +13.8%
分位超额 f_orig [valid] Q1..Q10: -29.1% -8.3% -3.5% -1.2% +3.9% +4.1% +6.2% +7.6% +8.4% +11.9%
分位超额 f_sum_k3 [train] Q1..Q10: -33.3% -12.4% -4.5% -2.1% +0.7% +5.6% +10.3% +11.4% +10.9% +13.4%
分位超额 f_sum_k3 [valid] Q1..Q10: -26.3% -11.9% -3.8% -2.8% +4.0% +3.2% +7.1% +11.6% +7.5% +11.3%
分位超额 f_sum_k2 [train] Q1..Q10: -38.3% -16.1% -5.3% -0.8% +2.7% +7.5% +8.8% +13.4% +12.6% +15.4%
分位超额 f_sum_k2 [valid] Q1..Q10: -36.6% -15.3% -7.9% -3.7% +1.2% +4.2% +10.1% +10.8% +16.7% +20.6%
分位超额 f_std9_k1 [train] Q1..Q10: -43.4% -17.9% -7.4% +0.0% +3.3% +8.5% +9.2% +14.4% +15.4% +17.9%
分位超额 f_std9_k1 [valid] Q1..Q10: -44.5% -15.3% -9.4% -3.6% +0.7% +6.7% +6.5% +13.3% +20.4% +25.3%
分位超额 f_stdamt9 [train] Q1..Q10: -38.3% -17.4% -7.7% -2.6% +3.5% +6.3% +10.3% +13.6% +14.8% +17.5%
分位超额 f_stdamt9 [valid] Q1..Q10: -48.7% -19.2% -11.3% -1.7% +0.8% +6.0% +9.5% +15.2% +21.8% +27.7%

与 f_orig 的日截面 rank 相关(fit 段; |.|>=0.95 = 同一因子族): ref_base +1.00  f_sum_k3 +0.86  f_sum_k2 +0.75  f_std9_k1 +0.65  ref_A5 +0.50  ref_C +0.49  f_stdamt9 +0.41  known_stdamt_max9 +0.41  known_ivol_max9 +0.33  known_amt_max9 +0.31  ctl_amt +0.28  ctl_ivol +0.27  ctl_mom20 +0.26  ctl_turnrate +0.19  ctl_dvol20 +0.18  ctl_cap +0.10  ctl_price -0.03  ctl_rev1 -0.01

逐年 f_orig: 2018 LS +5.43 Lg +8.0%  2019 LS +6.22 Lg +22.6%  2020 LS +4.19 Lg +19.6%  2021 LS +1.78 Lg +3.7%  2022 LS +2.87 Lg +13.8%  2023 LS +2.05 Lg +10.2%  2024 LS +2.86 Lg +7.4%  2025 LS +3.34 Lg +15.9%

逐年 f_sum_k3: 2018 LS +4.73 Lg +8.4%  2019 LS +4.95 Lg +18.9%  2020 LS +4.27 Lg +15.2%  2021 LS +2.37 Lg +6.2%  2022 LS +3.90 Lg +13.8%  2023 LS +2.64 Lg +9.5%  2024 LS +3.59 Lg +10.6%  2025 LS +3.08 Lg +13.0%

逐年 f_sum_k2: 2018 LS +4.89 Lg +17.5%  2019 LS +4.29 Lg +17.7%  2020 LS +2.26 Lg +9.7%  2021 LS +2.68 Lg +14.6%  2022 LS +4.86 Lg +19.8%  2023 LS +3.44 Lg +17.9%  2024 LS +2.89 Lg +12.4%  2025 LS +2.60 Lg +15.8%

逐年 f_std9_k1: 2018 LS +5.67 Lg +26.3%  2019 LS +4.55 Lg +19.6%  2020 LS +2.08 Lg +10.6%  2021 LS +2.22 Lg +13.3%  2022 LS +5.34 Lg +25.3%  2023 LS +3.75 Lg +21.1%  2024 LS +3.01 Lg +13.4%  2025 LS +2.72 Lg +18.0%

逐年 f_stdamt9: 2018 LS +4.02 Lg +27.3%  2019 LS +3.32 Lg +17.8%  2020 LS +1.20 Lg +7.2%  2021 LS +2.07 Lg +15.2%  2022 LS +5.41 Lg +27.0%  2023 LS +4.01 Lg +23.8%  2024 LS +2.21 Lg +10.0%  2025 LS +2.11 Lg +15.5%
```

**10-03 23:47 · Bash** — Look for clues on who edited the shared files

```bash
cd /Users/wxy/Desktop/Partura && grep -n "固定半衰期" notes/F101_day_shine_retstd/*.md notes/F103_amt_dw_decay/*.md | cut -c1-400; echo ---; grep -l "out of memory\|OOM\|OutOfMemory" logs/*.log 2>/dev/null | head; echo ---; grep -rn "ts_stddev" configs/F10*.yaml | cut -c1-200 | head -20; echo ---; stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" configs/F10*.yaml notes/F101_day_shine_retstd/07x_look3.md notes/F101_day_shine_retstd/09_diagnosis.md; ls -la partura | head -30; stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" partura/*.py | sort | tail -5
```

```
notes/F101_day_shine_retstd/07x_look3.md:8:**A. 固定半衰期的配料表**(多头腿净超额 train / valid;括号里是扣费多空夏普):
notes/F101_day_shine_retstd/07_SR_rivals.md:2:审查员自己用 `audit_1.py` 按固定半衰期 10 量过一遍(见下面「审查员的反驳实验」一节)。这里用正式口径(方向、半衰期在 train 上定)各做一次直接替换,
notes/F101_day_shine_retstd/09_diagnosis.md:20:8. **原式的多头腿从 2021 年起失效,背景版没有**(`look2.py` E、S2 逐年、`look3.py` Y)。固定半衰期 20:原式 2021–2023 多头净 +1.4% / +0.9% / +1.8%,
notes/F103_amt_dw_decay/08_variants.md:12:  同一个信号把半衰期从 2 调到 10,train 多头腿净超额能差 2~3 个点(原式 +6.3% → +9.4%,`x_std9_k1` +11.5% → +13.8%),而多空夏普几乎不动。S_final 的摘要里有固定半衰期的对照。
---
---
configs/F101_day_shine_retstd.yaml:38:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F101_day_shine_retstd.yaml:82:      - {id: s1_fold_dvol20, group: substitute, profile: true, expr: "abs_(cs_demean(ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)))", why: "�
configs/F101_day_shine_retstd.yaml:99:      # s2_fold_dvol20(20 日日频波动的同样折叠)两次都因 GPU 被邻居占满、ts_stddev 报 CUDA OOM 而失败,从本阶段拿掉;
configs/F102_kurt_autocorr.yaml:38:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F103_amt_dw_decay.yaml:38:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F104_kurt_masktop_amt.yaml:38:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F106_erm_mag_gap_1m.yaml:37:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F107_abs_demean_skew_low.yaml:38:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F108_max_ntkurt_close.yaml:37:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F105_std_fangzheng_covamt.yaml:5:expression: "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)"
configs/F105_std_fangzheng_covamt.yaml:38:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
configs/F105_std_fangzheng_covamt.yaml:49:  ref_orig:          "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)"
configs/F105_std_fangzheng_covamt.yaml:76:      - {id: v_base, group: baseline, expr: "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)", why: "原始表达式"}
configs/F105_std_fangzheng_covamt.yaml:78:  # C := cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241) —— 一年窗口的 mean+std 水平;原式 = ts_stddev(C, 5)
configs/F105_std_fangzheng_covamt.yaml:79:  # S1 第一次运行时 3 个变体(s1_relchg / s1_noecho / s1_recent)因为邻居占满显卡在 nd 面 ts_stddev 上 OOM;
configs/F105_std_fangzheng_covamt.yaml:87:         why: "删掉外层 ts_stddev,只留一年水平 C。H1 预测它不输原式;如果它明显差,说明「最近 5 天动了多少」带来了水平�
configs/F105_std_fangzheng_covamt.yaml:103:  # 工具绕行:nd 面的 ts_stddev 在 GPU 上不分块(一次要 3 x 388 MiB),邻居把显卡占满时会 OOM(S1 第一次跑挂了 3 个)。
configs/F105_std_fangzheng_covamt.yaml:110:         why: "原式的外层 ts_stddev 换成同一内核的 dt 面写法 cross_stddev。必须与原式 rank 相关 1.000、指标逐位相同;否则本�
configs/F105_std_fangzheng_covamt.yaml:167:      - {id: f_orig,  group: final, final: true, expr: "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)", why: "原始表达式(4 个算�
configs/F109_erm_mag_gap_5m_tsm20.yaml:37:  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
---
2026-10-03 23:45:03 configs/F101_day_shine_retstd.yaml
2026-10-03 23:46:04 configs/F102_kurt_autocorr.yaml
2026-10-03 23:22:50 configs/F103_amt_dw_decay.yaml
… (15 行略) …
-rw-r--r--@  1 wxy  staff   7028 Oct  3 17:44 cli.py
-rw-r--r--@  1 wxy  staff   8691 Oct  3 16:29 decompose.py
-rw-r--r--@  1 wxy  staff  17784 Oct  3 16:27 diagnose.py
-rw-r--r--@  1 wxy  staff   6169 Oct  3 16:21 guard.py
-rw-r--r--@  1 wxy  staff   4746 Sep 30 12:25 lab.py
-rw-r--r--@  1 wxy  staff  17659 Oct  3 17:44 panels.py
-rw-r--r--@  1 wxy  staff  13247 Oct  3 16:28 probes.py
-rw-r--r--@  1 wxy  staff  15689 Oct  3 16:32 propose.py
-rw-r--r--@  1 wxy  staff   5526 Oct  3 16:49 remote_tools.py
-rw-r--r--@  1 wxy  staff  19465 Oct  3 17:36 report.py
-rw-r--r--@  1 wxy  staff  15246 Sep 30 12:25 report_legacy.py
-rw-r--r--@  1 wxy  staff  17589 Oct  3 17:36 runner.py
-rw-r--r--@  1 wxy  staff  10691 Oct  3 16:28 semantics.py
-rw-r--r--@  1 wxy  staff   3733 Sep 30 01:39 splits.py
-rw-r--r--@  1 wxy  staff   5768 Oct  3 17:44 study_tools.py
2026-10-03 17:36:36 partura/report.py
2026-10-03 17:36:36 partura/runner.py
2026-10-03 17:44:56 partura/cli.py
2026-10-03 17:44:56 partura/panels.py
2026-10-03 17:44:56 partura/study_tools.py
```

**10-03 23:48 · Bash** — Extract matched half-life comparisons from final run

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open("runs/F103_amt_dw_decay/final.json"))
R=d["results"]
for k in R:
    bu=R[k]["books_user"]
    print(k, "hl_used", bu["hl_used"], "hl_long", bu["hl_long"])
    for sp,x in bu["splits_at_hl_long"].items():
        print(f"   at hl_long {sp}: LS={x['ls_sharpe']:+.3f} Lg={x['long_gross_ann']*100:+.2f} Ln={x['long_ann']*100:+.2f} Lsh={x['long_sharpe']:+.3f} TO={x['ls_turnover']*100:.2f} Lmdd={x['long_mdd']*100:.1f}")
    print("   user sweep (utrain):", [(s["halflife"], round(s["ls_sharpe"],2), round(s["long_ann"]*100,1), round(s["long_sharpe"],2), round(s["ls_turnover"]*100,1)) for s in bu["sweep"]])
    b=R[k]["books"]
    print("   train sweep:", [(s["halflife"], round(s["ls_sharpe"],2), round(s["long_ann"]*100,1), round(s["long_sharpe"],2)) for s in b["sweep"]])
    print("   dec at hl_long", b["hl_long"], {sp:(round(x['ls_sharpe'],2), round(x['long_ann']*100,1), round(x['long_sharpe'],2)) for sp,x in b["splits_at_hl_long"].items()})
EOF
```

```
Exit code 1
f_orig hl_used 2.0 hl_long 10.0
   at hl_long utrain: LS=+3.395 Lg=+11.11 Ln=+8.05 Lsh=+1.487 TO=3.64 Lmdd=-7.7
   at hl_long holdout: LS=+2.923 Lg=+10.16 Ln=+7.17 Lsh=+1.260 TO=3.60 Lmdd=-6.9
   user sweep (utrain): [(0.0, 2.79, -2.7, -0.56, 14.3), (1.0, 3.27, 2.5, 0.51, 10.6), (2.0, 3.53, 5.6, 1.11, 8.4), (3.0, 3.5, 6.6, 1.29, 7.1), (5.0, 3.47, 7.3, 1.39, 5.5), (10.0, 3.39, 8.1, 1.49, 3.6), (20.0, 3.22, 7.6, 1.39, 2.3)]
   train sweep: [(0.0, 3.38, -1.8, -0.38), (1.0, 3.86, 3.3, 0.69), (2.0, 4.14, 6.3, 1.3), (3.0, 4.12, 7.4, 1.51), (5.0, 4.13, 8.1, 1.62), (10.0, 4.09, 9.4, 1.86), (20.0, 3.95, 9.5, 1.86)]
   dec at hl_long 10.0 {'train': (4.09, 9.4, 1.86), 'valid': (2.07, 4.5, 0.73)}
f_sum_k3 hl_used 10.0 hl_long 20.0
   at hl_long utrain: LS=+3.628 Lg=+12.16 Ln=+10.09 Lsh=+2.015 TO=2.41 Lmdd=-5.9
   at hl_long holdout: LS=+3.331 Lg=+12.63 Ln=+10.65 Lsh=+1.989 TO=2.37 Lmdd=-5.4
   user sweep (utrain): [(0.0, 1.48, -14.8, -3.13, 25.1), (1.0, 2.89, -2.6, -0.54, 13.9), (2.0, 3.34, 2.3, 0.46, 9.7), (3.0, 3.54, 4.9, 0.98, 7.8), (5.0, 3.62, 6.6, 1.3, 5.9), (10.0, 3.64, 8.4, 1.66, 3.9), (20.0, 3.63, 10.1, 2.02, 2.4)]
   train sweep: [(0.0, 1.75, -15.3, -3.18), (1.0, 3.16, -2.8, -0.58), (2.0, 3.56, 1.9, 0.37), (3.0, 3.75, 4.4, 0.87), (5.0, 3.79, 6.0, 1.19), (10.0, 3.92, 8.8, 1.76), (20.0, 3.93, 11.1, 2.24)]
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
KeyError: 'splits_at_hl_long'
```

**10-03 23:49 · Bash** — Search for source of weight-share figures

```bash
cd /Users/wxy/Desktop/Partura && grep -n "53%\|47%\|0\.53\b\|0\.47\b" logs/F103_amt_dw_decay_x*.log | head; grep -n "53\|权重" studies/F103_amt_dw_decay/x2_interaction.py studies/F103_amt_dw_decay/x3_family.py | head -20; echo ---; grep -n "八成\|两成" notes/F103_amt_dw_decay/*.md | cut -c1-220
```

```
logs/F103_amt_dw_decay_x1.log:91:C_swap                   +   1 +0.0342 +0.0617  +1.16  +3.29   +6.8%/+19.5%   +3.9%/+16.7%  +0.47/+2.38   3.5%  -0.048
logs/F103_amt_dw_decay_x1.log:105:Q3      0.55     0.53     0.52     0.55     0.55     0.50     0.49     0.60     0.58     0.53     1.14%    2.09%     8.27%      -5.6%
logs/F103_amt_dw_decay_x1.log:106:Q4      0.52     0.52     0.50     0.52     0.53     0.50     0.49     0.55     0.55     0.52     1.24%    1.67%     5.88%      +0.3%
logs/F103_amt_dw_decay_x1.log:108:Q6      0.47     0.49     0.48     0.48     0.48     0.51     0.50     0.46     0.48     0.50     1.55%    1.23%     3.53%      +8.0%
logs/F103_amt_dw_decay_x1.log:109:Q7      0.45     0.48     0.47     0.45     0.46     0.51     0.50     0.43     0.45     0.49     1.65%    1.06%     2.80%     +11.9%
logs/F103_amt_dw_decay_x1.log:110:Q8      0.43     0.47     0.46     0.44     0.44     0.51     0.51     0.40     0.40     0.47     1.74%    0.91%     2.22%     +10.0%
logs/F103_amt_dw_decay_x3.log:17:dsum                     +0.28    +1.00    +0.94    +0.74    +0.86    +0.07    -0.05    -0.54    +0.89    +1.00    +0.56    +0.53
logs/F103_amt_dw_decay_x3.log:20:dsum*C^3                 +0.86    +0.47    +0.72    +0.93    +0.65    +0.51    +0.40    +0.41    +0.52    +0.47    +0.24    +0.27
logs/F103_amt_dw_decay_x3.log:28:stdamt9(F001 蒸馏)         +0.41    +0.89    +0.88    +0.74    +0.87    +0.25    +0.15    -0.39    +1.00    +0.89    +0.49    +0.47
logs/F103_amt_dw_decay_x3.log:29:amt_max9                 +0.31    +0.93    +0.88    +0.69    +0.85    +0.13    +0.02    -0.52    +0.96    +0.93    +0.54    +0.47
studies/F103_amt_dw_decay/x2_interaction.py:211:    # ---------- e. C 里到底哪一部分有用:同等权重的替换 ----------
---
notes/F103_amt_dw_decay/01_expression.md:13:- 原式的指数 3 让集中度占了八成权重:多空夏普不差,但多头腿弱(净超额 +5.6% / +5.5%)。把指数降到 2(两条腿各占一半)之后,
notes/F103_amt_dw_decay/07_S1_structure.md:33:   **去掉成交额水平那两成,剩下的"成交额中性粗糙度"在 valid 上不赚钱。**
notes/F103_amt_dw_decay/07x_x1_anatomy.md:23:整棵树大约是"两成成交额水平 + 八成**成交额中性的粗糙度**"。这解释了它与 `ctl_amt` 的 rank 相关为什么只有 0.28。
notes/F103_amt_dw_decay/07x_x3_family.md:64:原式(集中度占八成)所以在 2021 年之后走弱;k = 2 的配比**每一年多空夏普都在 +2.2 以上、多头腿净超额都在 +6% 以上**,表里其余各行都�
notes/F103_amt_dw_decay/07x_x2_interaction.md:16:**这张表是整份研究里最重要的一张。** 原式里占八成权重的那部分 —— 成交额中性的粗糙度 —— 在 2018–2020 很强,**2021 年起单
notes/F103_amt_dw_decay/07x_x2_interaction.md:17:(−0.0012 / +0.0024 / +0.0111)。原式在 2021–2023 还能有 −0.024~−0.028 的 rank IC,靠的是剩下那两成成交额水平(这三年它反而变强了),
notes/F103_amt_dw_decay/09_diagnosis.md:2:它**只在成交活跃的票里、只在空头端**有稳定的预测力。两条腿在时间上轮动,原式把八成权重押在了集中度上。
notes/F103_amt_dw_decay/11_risks.md:9:- **容量与成本。** 多头端是全市场成交额最低的那一两成股票;日换手 3.5%~3.9%(半衰期 10),15 bp 单边成本下多头腿每年付出约 3 个点(毛 +15.6%
```

**10-03 23:50 · Bash** — Check probe output and report section coverage

```bash
cd /Users/wxy/Desktop/Partura && sed -n 73,80p research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-900; echo; grep -n "window_one_is_identity" research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-300 | head -8; echo; grep -n "^\*\*脚本\*\*\|^### \|^## " research/alpha_distillation/F103_amt_dw_decay.md | sed -n 1,60p
```

```
### `ts_min`

- **实现**: `operators/nd_ts.py:171` (kernel `nd_ts.ts_min`)
- **声明**: face `nd` / family `ts` / category `rolling`, arity 1, 计算轴 `D`, 窗口 1
- **标志**: 无
- **实测探针**: 日轴因果性 = True; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = odd; 窗口变长 = non_increasing; 脉冲记忆天数 = 1
- **本研究新增的探针**: impulse_footprint = columns_hit=[3], impulse_column=3, lags_hit=[0, 0], weight_at_lag0=1.0, weight_at_last_lag=1.0, effective_n=1.0, window=1, selfcheck={'cross_mean(10)_same_column_lags_0..9_flat_0.1_neff_10': True}; window_one_is_identity = identity_at_window_1=True, selfcheck={'ts_max(x,1)_is_identity': True, 'ts_delay(x,1)_is_not': True}
- <sub>不适用的探针: order_dependent_on_minutes, rank_preserving, isolated_spike_response, noise_averaging_exponent, trailing_nan_fallback</sub>

43:- <sub>不适用的探针: causal_on_day_axis, rank_preserving, monotone_in_window, effective_memory, impulse_footprint, window_one_is_identity</sub>
52:- **本研究新增的探针**: impulse_footprint = columns_hit=[3], impulse_column=3, lags_hit=[0, 29], weight_at_lag0=0.0645, weight_at_last_lag=0.0022, effective_n=22.87, window=30, selfcheck={'cross_mean(10)_same_column_lags_0..9_flat_0.1_neff_10': True}; window_one_is_identity = identity_at_
62:- <sub>不适用的探针: causal_on_day_axis, rank_preserving, monotone_in_window, effective_memory, impulse_footprint, window_one_is_identity</sub>
71:- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, monotone_in_window, effective_memory, isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback</sub>
79:- **本研究新增的探针**: impulse_footprint = columns_hit=[3], impulse_column=3, lags_hit=[0, 0], weight_at_lag0=1.0, weight_at_last_lag=1.0, effective_n=1.0, window=1, selfcheck={'cross_mean(10)_same_column_lags_0..9_flat_0.1_neff_10': True}; window_one_is_identity = identity_at_window_1=T
88:- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback</sub>
96:- **本研究新增的探针**: impulse_footprint = columns_hit=[3], impulse_column=3, lags_hit=[0, 4], weight_at_lag0=0.9865, weight_at_last_lag=0.9872, effective_n=5.0, window=5, selfcheck={'cross_mean(10)_same_column_lags_0..9_flat_0.1_neff_10': True}; window_one_is_identity = identity_at_wind
114:- `window_one_is_identity` — 窗口取 1 时是不是恒等变换?(数值和 NaN 位置都不变)  _(本研究新增,来自 `probes.py`)_

11:## 1. 原始表达式
32:## 2. 算子的真实语义
36:### `day_close`
46:### `cross_decay_linear`
55:### `day_durbin_watson`
65:### `pow_3`
73:### `ts_min`
82:### `mul`
90:### `cross_max`
121:### 既往研究留下的先验
155:## 3. 数学分解
200:## 4. 结构语法
… (6 行略) …
529:### S_final
570:### 中性化(fit 段)
670:### 条件 IC(fit 段)
693:### 控制变量自己当因子(同口径)
717:**脚本** `studies/F103_amt_dw_decay/x1_anatomy.py`(只读 train / valid)。它不是在挑变体,而是在量这棵树的两支各是什么、谁说了算。
778:**脚本** `studies/F103_amt_dw_decay/x2_interaction.py`(只读 train / valid)。S1 之后剩下的问题:粗糙度支的钱是哪几年赚的、
870:**脚本** `studies/F103_amt_dw_decay/x3_family.py`(只读 train / valid;数值重建,方向与半衰期在 train 上定)。X2 之后剩下的问题是第二轮假设 H13~H18:
1014:## 8. 语义变体
1086:## 9. 机制诊断
1091:### 已确立(每条后面是实验)
1115:### 合理但没坐实
1124:### 未决
1132:### 假设的判决
1155:## 10. 蒸馏 / 升华后的候选
1168:### 读留出段之前定下的候选(只凭 train / valid;这一段写于 `study.sh final` 之前,之后没有改过)
1209:### 读完留出段之后(上面那段没有再动;留出段只读了这一次)
1256:## 11. 失效模式与风险
1276:## 12. 下一步实验
1289:## 附录 A — 数据段使用台账
1301:## 附录 B — 复现
```

**10-03 23:52 · StructuredOutput**

```json
{
 "factor_id": "F103_amt_dw_decay",
 "lens": "数字与流程",
 "issues": [
  {
   "severity": "major",
   "where": "notes/F103_amt_dw_decay/10_distilled.md「最终推荐」段;01_expression.md 第 13–14 行;09_diagnosis.md 已确立第 10 条;研究员汇报的 recommended",
   "what": "最终推荐是读完留出段之后从事前登记的 f_std9_k1 改成 f_sum_k2 的,决定性理由来自留出段的多头腿。recommended 的测试列因此是「五个候选里留出段多头腿最好的那个」,不是干净的样本外数字。另外,配置里事前给 f_sum_k2 写的判据在留出段上恰恰没过,而 09 第 10 条写「事前写下的三条判据都过了」,没提这第四条。01_expression 和结构化结论里也没有标注这是事后改选(只有第 10、11 节披露了)。",
   "evidence": "configs/F103_amt_dw_decay.yaml 的 S_final(mtime 23:22:50,final 日志显示 23:23:39 启动):f_std9_k1 的 why 是「事前推荐的升华版」,f_sum_k2 的 why 是「若留出段上它不如 f_sum_k3,'指数 3 是 train 的局部最优'在样本外不成立」。final.json 留出段:f_sum_k2 多空夏普 3.099,f_sum_k3 3.518,差 0.42,超过 playbook 说的 ±0.3 噪声。事前推荐的 f_std9_k1 自己的判据全过:多头净超额 11.64% 对原式 5.47%,纯多头夏普 1.547 对 1.044,多空夏普 3.142 对 3.180,比 f_stdamt9 高 0.59。五个候选的留出段纯多头夏普是 1.044 / 1.765 / 2.071 / 1.547 / 0.890,多头净超额是 5.5% / 9.2% / 12.6% / 11.6% / 8.2%,f_sum_k2 两项都是最大值。只看 train/valid 时 f_std9_k1 不输 f_sum_k2(多头净超额 11.5% / 17.7% 对 11.4% / 14.5%,多空夏普 3.32 / 4.36 对 3.33 / 3.78);所谓「三条读之前就知道的理由」在事前选 f_std9_k1 时已经知道。研究员自己写「三个都比原式值得用,差别在噪声量级」。10_distilled.md 的 mtime 是 23:34,晚于 final(23:26),「前半段写于 final 之前、之后没改」无法从文件时间核实;能独立佐证事前推荐的只有配置文件的 mtime。",
   "fix": "结构化结论和 01/09 的摘要以事前登记的 f_std9_k1 作为样本外判决(测试段多空夏普 3.14、多头净超额 11.6%、纯多头夏普 1.55)。f_sum_k2 可以保留为推荐,但要在 one_line、01_expression 和 recommended 旁明写「读留出段后在 5 个候选里改选,测试列带选择偏差」,并与 f_std9_k1 并排给数。09 第 10 条补上第四条判据未过(f_sum_k2 比 f_sum_k3 低 0.42)。"
  },
  {
   "severity": "major",
   "where": "10_distilled.md「事前判据逐条」第 1 条与「为什么说提纯成功、升华有限」;07_S2_distil.md 解读 1;07_S1_structure.md 解读 5;09_diagnosis.md 已确立第 1 条;01_expression.md 第 10 行",
   "what": "原式(半衰期 2)与提纯版(半衰期 10 或 20)的多头腿净超额直接相比,把半衰期差异记成了「删节点」的功劳。playbook §3 明确写了「各变体的半衰期是各自拟合的……这不是结构差异,比结构之前先看固定半衰期表」。「删节点带来的多头腿改善全部是成本」这句在同半衰期下不成立;「原式 +5.5% → 推荐 +12.6%」的幅度也有一部分只是半衰期。结论方向不变,归因和幅度要改。",
   "evidence": "final.json 里 f_orig 的 books_user.splits_at_hl_long(半衰期 10,utrain 上定):utrain 多空夏普 3.39、多头净超额 8.05%、纯多头夏普 1.49;留出段多空夏普 2.92、多头毛超额 10.16%、净超额 7.17%、纯多头夏普 1.26、换手 3.6%。即原式只把半衰期从 2 换到 10,留出段多头净超额就从 5.5% 到 7.2%。同为半衰期 10 时 f_sum_k3 是 9.2%(毛 12.3% 对 10.2%,换手 3.7% 对 3.6%),差的是毛超额,不是成本。train 固定半衰期 10(digest 的固定半衰期表):f_orig 多空夏普 4.09、多头净超额 9.4%;f_sum_k3 3.92、8.8%;f_sum_k2 3.33、11.4% —— 纯删节点在 train 的多头腿上没有改善。S1 的 f_sum(半衰期 10)9.5% / 7.4%,对原式半衰期 10 的 9.4% / 4.5%(S0 splits_at_hl_long):「多头腿两段都更好」在 train 上消失。同半衰期口径下 headline 是 7.2% → 12.6%、纯多头夏普 1.26 → 2.07,而不是 5.5% → 12.6%、1.04 → 2.07。",
   "fix": "第 10 节的表加一行「原式 @ 半衰期 10」(数已在 final.json 里,不需要再读留出段)。把「删节点降换手 +5.5% → +9.2%,毛超额没变」改写为:其中约 1.7 个点来自半衰期 2 → 10(原式自己也拿得到,代价是留出段多空夏普 3.18 → 2.92),同半衰期下删节点再加约 2.0 个点,且来自毛超额。S1、S2、09 里对应的比较同样注明各自的半衰期或改用固定半衰期的数。"
  },
  {
   "severity": "major",
   "where": "研究员汇报的 one_line(对应 09_diagnosis.md「合理但没坐实」第一条、07x_x3_family.md G 节)",
   "what": "one_line 把「成交挤在少数几分钟(主要是 9:31 那一根)」写成原式的描述。这个统计量是峰值占比 p_peak / day_argmax(B) 的性质,不是原式里 DW 那一支的;报告自己也把这条经济解释列在「合理但没坐实」。属于把别的变体的数写到原式头上,只需改一句。",
   "evidence": "X3-G 日志:day_argmax(B) 在 train 67.8%、valid 86.6% 落在 9:31;p_peak 与 9:31 那根占比的 rank 相关 0.781 —— 都是 p_peak 的事实。原式用的 C = DW(B):X1 日志里 C 被「切掉首尾的内部 DW」张成 0.691;C 与首根占比的 rank 相关 0.109,与头两根占比 0.131,与开盘 10 分钟占比 −0.027,与收盘竞价占比 0.422,与 p_peak 0.426(X1-3、X2-f)。X2-e 里 day_sum·p_close^4.08(多空夏普 3.51 / 3.91)不输 day_sum·p_first2^2.66(2.97 / 3.53),没有证据说有预测力的部分主要是 9:31。",
   "fix": "one_line 去掉「(主要是 9:31 那一根)」,或改成「平均日内成交曲线粗糙/集中(DW);其中有预测力的更像首尾几根与没被平均掉的尖峰,未坐实」。"
  },
  {
   "severity": "minor",
   "where": "notes/F103_amt_dw_decay/07x_x2_interaction.md d 节第 64–65 行",
   "what": "「k = 1~2 是两段都站得住的区间……多空夏普两段都在 +2.4 以上」与同一张表不符。",
   "evidence": "X2 日志与 S2_distil.json:day_sum·C^1(d_sum_k1)train 多空夏普 2.36,低于 2.4。",
   "fix": "改成「+2.3 以上」,或把区间写成 k = 1.5~2。"
  },
  {
   "severity": "minor",
   "where": "notes/F103_amt_dw_decay/09_diagnosis.md 已确立第 3 条",
   "what": "「先逐日算 DW、再平均……与成交额水平 −0.76」标错了对象。",
   "evidence": "X1 日志第 45 行:C_swap 的 −0.760 是与 max5(A)(收盘竞价额的 5 日峰值)的 rank 相关,不是与 ctl_amt;07x_x1_anatomy.md 第 6 节原文写的也是 max5(A)。",
   "fix": "改成「与 max5(A) −0.76」。"
  },
  {
   "severity": "minor",
   "where": "notes/F103_amt_dw_decay/01_expression.md 第 12 行",
   "what": "摘要把「2024–2025 集中度强」写成事实,而 09_diagnosis.md 把同一件事列在「合理但没坐实」。",
   "evidence": "09_diagnosis.md 原文:留出段只读了五个候选的两本书,没有量成交额中性的集中度在留出段的 rank IC,是从排序(f_sum_k3 3.52 > f_orig 3.18 ≈ f_std9_k1 3.14 ≈ f_sum_k2 3.10 > f_stdamt9 2.55)推出来的。",
   "fix": "01_expression 里加上「从候选排序推断,未直接测量」。"
  },
  {
   "severity": "minor",
   "where": "docs/study_playbook.md、scripts/study.sh、scripts/summarize.py(git status --short partura scripts lab docs)",
   "what": "三个共享文件有未提交改动,归属无法确认,更像是批次层面的工具更新而不是 F103 研究员所为。照章列出,由编排方确认。",
   "evidence": "git status 显示这三个文件为 M;mtime 全部是 2026-10-03 23:20:15(同一秒)。改动内容是 playbook 增加 ts_* OOM 与「各变体半衰期各自拟合」两条、wait 的 tail 从 60 行改 200 行、summarize.py 增加固定半衰期表。OOM 那条对应的是 F101 / F105 配置里记的故障,F103 的日志里没有 OOM;F103 的 notes 没有提到改工具。partura/ 与 lab/ 无改动(lab/findings.yaml mtime 仍是 09-30)。改动只影响本机 digest 的打印,不影响 runs/*.json 的任何数字。",
   "fix": "编排方确认这三处是不是自己改的;若不是,查是哪个研究改的并回滚或提交。"
  }
 ],
 "checked": [
  "已读 CLAUDE.md、docs/method.md、docs/study_playbook.md,以及全部 22 份 notes、配置、4 个 run JSON、ledger、6 份 F103 日志、3 个分析脚本和最终报告",
  "基线复现(第 4 项):S0 用户口径方向 −1、半衰期 2、多空夏普 3.5329(公布 3.53)、多头毛超额 0.1275(公布 0.128),在容差内;final.json 的 f_orig 留出段 3.180 / 0.1241 对公布的 3.18 / 0.124",
  "研究员汇报的 original / recommended 两组数字逐项对 final.json 的 books_user:全部一致(多空夏普 3.533 / 3.180 与 3.446 / 3.099;多头毛超额 0.1275 / 0.1241 与 0.1574 / 0.1558;净超额 0.0557 / 0.0547 与 0.1230 / 0.1264;纯多头夏普 1.108 / 1.044 与 2.179 / 2.071;换手 0.0843 / 0.0389;半衰期 2 / 10;rank 相关 0.745;算子数 7 / 5)",
  "06_baseline 约 30 个数字对 S0_baseline.json(多头占比 24%、十分位剖面、半衰期扫描、逐年、衰减、中性化 R² 0.227 与残差、条件 IC、rank 相关):全部一致",
  "07_S1_structure 的 12 行表与解读对 S1_structure.json(含 a_C 逐年、中性化 0.0045 → 0.0247 / 0.0162、条件 IC −0.0019 → −0.0514):全部一致",
  "07_S2_distil 的 13 行表、逐年、半衰期扫描(3.28~3.32、6.8%~11.7%)、分位剖面、用户口径一段对 S2_distil.json:全部一致",
  "07_S_final 的 8 年 × 5 候选逐年表与候选间 rank 相关对 final.json:全部一致",
  "10_distilled 的事前表(决策口径)与事后表(用户口径,含最大回撤、留出段 rank IC、换手)对 final.json:全部一致;文中各项差值(0.34、0.59、0.58 / 0.55、0.04 / −0.52 / −1.0%)复算无误",
  "09_diagnosis 的 10 条已确立、未决、假设判决表逐条回溯到 JSON 或日志:数字一致(仅第 3 条标错对象,见 issues)",
  "07_neutralise / 07_conditional / 07_controls / 08_variants / 11_risks 里的数字对 JSON:一致(含 x_std9_k1 与窗口 15 / 60 的相关 0.983 / 0.985、a_C 与 f_share 0.933、d_sum_k2 与 d_sum_k1 0.918)",
  "07x_x1 / x2 / x3 三份笔记的表与正文逐格对 logs/F103_amt_dw_decay_x1 / x2 / x3.log:一致(仅 X2-d 的「+2.4 以上」一处,见 issues);X2-e 的「C² 约 53% / 47%、峰值占比 50% / 50%」在日志里没有直接打印,是由离散度推算的近似值",
  "留出段纪律(第 2 项):ledger holdout reads = 1(5 条表达式,stage S_final);S_final 5 个候选含原式;final.json(23:26:41)是 runs 下最晚的 JSON,F103 的日志在 final 之后没有新的;final 日志有 HOLDOUT WILL BE READ,是经 study.sh final 跑的",
  "ledger 里 S0_baseline 有 4 次读取(本地时间 16:43~17:43),都早于第一份 note(18:39),属于骨架生成,不是研究员的运行;研究员实际运行为 S1、x1、x2、x3、S2、final 共 6 次(加 S0 为 7),在 8 次以内",
  "事前登记:配置 mtime 23:22:50 早于 final 启动 23:23:39,S_final 的 why 里已写明事前推荐与判据;10_distilled 前半段只用了 train / valid 数字(逐年用的是 S2 截到 8 月的 3.00,而不是 final 全年的 3.75,与事前写就相符),但文件 mtime 在 final 之后,无法独立核实未被改动",
  "口径(第 3 项):决策口径的方向和半衰期取自 train,用户口径取自 utrain(f_orig 2、f_sum_k3 10、f_sum_k2 10、f_std9_k1 2、f_stdamt9 0),留出段数字都用 utrain 定的方向和半衰期;没有发现把用户口径训练列当样本外叙述;跨口径并列处(train / valid 与留出段)都有标注",
  "分析脚本只索引 train + valid(x2 / x3 的 use = slice(tr.start, va.stop),books 的 evals 只有 train / valid),没有读留出段的行",
  "门槛(第 5 项):f_sum_k2 在 train 上 coverage_labelled 0.9992、distinct 1.0;全部 29 个变体 cov ≥ 0.999,dist 最低是 i_addrank 0.729",
  "报告本身(第 6 项):四次运行 errors 均为空,没有求值失败的变体被引用;notes 的 07_S1_structure / 07_S2_distil / 07_S_final 与配置 stage id 一致,三份 07x 都进了报告;报告生成时间 23:36:47 晚于最后一次 notes 修改 23:36:24;§6 用户口径表 v_base 的测试列是「—」(基线阶段不读留出段,原式的测试数在 §10 的 f_orig 行),属工具设计,不算缺数",
  "越界(第 7 项):partura/ 与 lab/ 无改动;docs 与 scripts 有 3 个文件改动,归属不明,见 issues"
 ],
 "overall": "数字层面很干净:核对了两百个以上的数字(远超要求的 15 个),run JSON 与日志同笔记逐位对得上,只有两处笔误级出入。基线复现、留出段只读一次、候选 5 个含原式、final 之后无新运行、方向与半衰期口径、cov / dist 门槛都通过,没有 critical 问题。\n\n需要改写的有三处:\n\n1. **推荐版是事后改选的。** 读完留出段后从事前登记的 f_std9_k1 改成 f_sum_k2,recommended 的测试列是五个候选里留出段多头腿最好的那个。配置里给 f_sum_k2 事前写的判据在留出段没过(多空夏普比 f_sum_k3 低 0.42)。第 10、11 节有披露,但 one_line、01_expression 和结构化结论没有标注。\n2. **半衰期混淆。** 原式(半衰期 2)对提纯版(半衰期 10)的多头腿比较没有控制半衰期。同半衰期下,留出段多头净超额是 7.2% → 12.6%,不是 5.5% → 12.6%;「删节点的改善全部是成本」这句归因不成立。\n3. **one_line 张冠李戴。** 「主要是 9:31 那一根」是峰值占比 p_peak 的统计,不是原式里 DW 那一支的(DW 与头两根占比的 rank 相关只有 0.13)。\n\n「提纯 / 降指数的版本多头腿优于原式」这个方向在扣掉上述两项之后仍然成立;「f_sum_k2 优于 f_std9_k1」没有样本外支持。",
 "refutation_attempt": "我试着从三个方向推翻「推荐版多头腿优于原式」这个核心结论,都没有推翻,只是幅度和归因要改。\n\n- **选择偏差**:只看事前登记的 f_std9_k1,留出段多头净超额 11.6% 对原式 5.5%,纯多头夏普 1.55 对 1.04,仍然更好;四个非原式候选的留出段多头净超额(9.2% / 12.6% / 11.6% / 8.2%)全部高于原式。\n- **半衰期混淆**:把原式也放到半衰期 10(final.json 的 splits_at_hl_long),留出段是 7.2% / 1.26,f_sum_k3 是 9.2% / 1.77,f_sum_k2 是 12.6% / 2.07,仍然更好;多空夏普上原式半衰期 10 是 2.92,反而比 f_sum_k3 的 3.52 低得更多。\n- **流程**:查了有没有第二次留出段读取、final 之后的运行、脚本里偷读留出段的行、用 utrain 或留出段定方向,都没有。\n\n反过来,我也试着为「事后改选」辩护:如果读之前就知道的三条理由足以支持 f_sum_k2,就不算用留出段挑。但这三条在事前选 f_std9_k1 时已经知道,train / valid 上 f_std9_k1 不输 f_sum_k2,所以决定性信息只能是留出段。这条辩护不成立。\n\n基线复现、门槛、数字核对三项我没有找到任何可以攻击的地方。"
}
```

```
Structured output provided successfully
```

## 它返回给工作流的结构化结果

见 `handoff/F103_amt_dw_decay/results/audit-numbers.json`。

## 它拿到的任务书

```
[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的审查员,负责**数字与流程**这一路。另一位研究员刚完成了因子 F103_amt_dw_decay 的研究;
  你的任务是找出报告里**不成立**的东西,不是帮它说话。拿不准的时候按「有问题」处理并写明证据。
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  开始之前**必须**依次读完这三份文件:CLAUDE.md、docs/method.md、docs/study_playbook.md。
  study_playbook.md 是操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西,全在里面,下面不再重复。
  不要使用 Agent / Workflow 工具去派生别的 agent;这项工作由你自己完成。
  所有写给人看的文字(notes、结论)用中文,英文术语保留。
  
  要读的材料(都在 /Users/wxy/Desktop/Partura 下):
    research/alpha_distillation/F103_amt_dw_decay.md      最终报告
    notes/F103_amt_dw_decay/*.md                           手写段落
    configs/F103_amt_dw_decay.yaml                         实验计划
    runs/F103_amt_dw_decay/*.json、runs/F103_amt_dw_decay/ledger.json  每次运行的原始结果与数据段台账
    studies/F103_amt_dw_decay/                             自写的探针与分析脚本(如果有)
  看某次运行的摘要:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F103_amt_dw_decay <tag>(tag = JSON 文件名去掉 .json)。
  
  研究员自己报告的结论(待核对):
  {
   "one_line": "成交额水平 ×(最近 30 天平均日内成交额曲线的粗糙度/集中度)³:成交活跃、且成交长期挤在少数几分钟(主要是 9:31 那一根)的股票之后跑输;钱主要在空头腿。",
   "original": {
    "expr": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "ls_train": 3.533,
    "ls_test": 3.18,
    "long_gross_train": 0.1275,
    "long_gross_test": 0.1241,
    "long_net_train": 0.0557,
    "long_net_test": 0.0547,
    "long_sharpe_train": 1.108,
    "long_sharpe_test": 1.044,
    "sign": -1,
    "halflife": 2,
    "turnover": 0.0843,
    "coverage": 0.9993,
    "distinct": 1,
    "n_operators": 7,
    "rank_corr_with_original": 1
   },
   "recommended": {
    "expr": "mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 30))))",
    "ls_train": 3.446,
    "ls_test": 3.099,
    "long_gross_train": 0.1574,
    "long_gross_test": 0.1558,
    "long_net_train": 0.123,
    "long_net_test": 0.1264,
    "long_sharpe_train": 2.179,
    "long_sharpe_test": 2.071,
    "sign": -1,
    "halflife": 10,
    "turnover": 0.0389,
    "coverage": 0.9993,
    "distinct": 1,
    "n_operators": 5,
    "rank_corr_with_original": 0.745
   },
   "recommended_kind": "distilled",
   "holdout_reads": 1,
   "server_runs": 7
  }
  
  ## 逐项检查(每一项都要实际去查,把查过的写进 checked)
  
  1. **数字对不对**。从 notes 里挑至少 15 个支撑主要结论的数字(优先 09_diagnosis、10_distilled、各阶段结论),
     逐个到 runs/F103_amt_dw_decay/*.json(或 digest 输出)里核对。差一位小数以上、张冠李戴(把 utrain 的数当成 valid 的、
     把毛超额当成净超额、把别的变体的数写到这个变体上)都算问题。
  2. **留出段纪律**。ledger.json 里 holdout 的读取次数必须是 1;S_final 里候选 ≤ 5 且含原式;
     final 那个 JSON 是不是最后一次运行(比较 runs/F103_amt_dw_decay/*.json 的修改时间:final 之后不应该再有新的阶段运行);
     notes 里有没有在读留出段**之前**就写下的候选选择理由,理由是不是只用了 train/valid 的数字。
  3. **口径**。报告里任何 valid / holdout 的数字,方向和半衰期是不是 fit 段定的(决策口径 fit=train,
     用户口径 fit=utrain);有没有把「用户口径的训练列」当成样本外来叙述。
  4. **基线复现**。S0_baseline 里原式的用户口径(utrain)是否与配置里 published 那一行一致(方向、半衰期、
     多空夏普 ±0.01、多头腿毛超额 ±0.002)。
  5. **门槛**。被推荐的候选在 train 上 cov(coverage_labelled)≥ 0.95、dist(distinct)≥ 0.5 吗?
  6. **报告本身**。有没有「求值失败」的变体被当成证据引用;表格是否有该有数却为空的;
     notes 的阶段文件名与配置里的 stage id 是否对得上(对不上的那段不会出现在报告里)。
  7. **越界**。cd /Users/wxy/Desktop/Partura && git status --short partura scripts lab docs —— 研究员不应改动这些目录
     (注意:同时有别的研究在进行,只看这几个目录)。
  
  issues 里每条写清 severity(critical = 结论因此不成立或流程违规;major = 需要改写或补实验;minor = 笔误级)、
  where(文件与位置)、what、evidence(你查到的具体数字)、fix(应该怎么改)。没有问题就返回空数组,不要凑数。
```
