# audit-mechanism:F103_amt_dw_decay — agent a4b7f0588d11e04ba(工作流 wf_759ef2d3-03f)

- 状态:**已返回结果**;开始 10-03 23:39,最后一次动作 10-04 00:01;工具调用 37 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F103_amt_dw_decay/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-03 23:39 · Bash** — List project files and doc sizes

```bash
cd /Users/wxy/Desktop/Partura && wc -l CLAUDE.md docs/method.md docs/study_playbook.md && ls
```

```
      27 CLAUDE.md
     123 docs/method.md
     181 docs/study_playbook.md
     331 total
CLAUDE.md
README.md
batches
configs
docs
lab
logs
notes
partura
research
runs
scripts
shared
studies
tests
tmp
```

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/CLAUDE.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/docs/method.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

**10-03 23:39 · Bash** — List F103 study materials and sizes

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F103_amt_dw_decay/ runs/F103_amt_dw_decay/ studies/F103_amt_dw_decay/ 2>&1; wc -l research/alpha_distillation/F103_amt_dw_decay.md configs/F103_amt_dw_decay.yaml notes/F103_amt_dw_decay/*.md
```

```
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
… (17 行略) …
      22 notes/F103_amt_dw_decay/02_operators.md
      19 notes/F103_amt_dw_decay/03_decomposition.md
      17 notes/F103_amt_dw_decay/04_grammar.md
      38 notes/F103_amt_dw_decay/05_hypotheses.md
      31 notes/F103_amt_dw_decay/06_baseline.md
      41 notes/F103_amt_dw_decay/07_S1_structure.md
      42 notes/F103_amt_dw_decay/07_S2_distil.md
      18 notes/F103_amt_dw_decay/07_S_final.md
       8 notes/F103_amt_dw_decay/07_conditional.md
       6 notes/F103_amt_dw_decay/07_controls.md
      15 notes/F103_amt_dw_decay/07_neutralise.md
      60 notes/F103_amt_dw_decay/07x_x1_anatomy.md
      91 notes/F103_amt_dw_decay/07x_x2_interaction.md
     143 notes/F103_amt_dw_decay/07x_x3_family.md
      13 notes/F103_amt_dw_decay/08_variants.md
      66 notes/F103_amt_dw_decay/09_diagnosis.md
      87 notes/F103_amt_dw_decay/10_distilled.md
      17 notes/F103_amt_dw_decay/11_risks.md
      10 notes/F103_amt_dw_decay/12_next.md
    2216 total
```

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/configs/F103_amt_dw_decay.yaml`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

10-03 23:39 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md`

**10-03 23:41 · Bash** — Read the study.sh helper script

```bash
cd /Users/wxy/Desktop/Partura && cat scripts/study.sh | head -120
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
… (48 行略) …
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json";
    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
    ;;
  digest)
    fid=$1; tag=$2; base=${3:-v_base}
    "$PY" scripts/summarize.py "runs/$fid/$tag.json" --base "$base"
    ;;
  report)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.cli report configs/$fid.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'" || exit 1
    mkdir -p research/alpha_distillation
    $RS "$SSH" "$HOST:$R/research/alpha_distillation/$fid.md" research/alpha_distillation/ && wc -l "research/alpha_distillation/$fid.md"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,16p' "$0"; exit 2 ;;
esac
```

**10-03 23:41 · Bash** — Print server kernel source for key operators

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src day_durbin_watson cross_decay_linear day_close day_last day_sum 2>&1 | head -250
```

```
### day_durbin_watson  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_durbin_watson
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:272
@op("dt", "day", arity=1)
def day_durbin_watson(x: torch.Tensor) -> torch.Tensor:
    """Per-row Durbin-Watson statistic; NaN if <2 valid points or the row
    is constant."""
    D, T = x.shape
    if T < 2:
        return torch.full((D, 1), float("nan"), dtype=x.dtype, device=x.device)
    valid_mask = ~torch.isnan(x)
    n_valid = valid_mask.sum(dim=1, keepdim=True)
    has_enough_data = n_valid >= 2

    diff = x[:, 1:] - x[:, :-1]
    diff_mask = valid_mask[:, 1:] & valid_mask[:, :-1]
    numerator = torch.where(diff_mask, diff ** 2, torch.zeros_like(diff)).sum(dim=1, keepdim=True)

    x_sq_masked = torch.where(valid_mask, x ** 2, torch.zeros_like(x))
    denominator = x_sq_masked.sum(dim=1, keepdim=True)

    dw = torch.where(
        has_enough_data & (denominator > 1e-8),
        numerator / (denominator + 1e-8),
        torch.full_like(x[:, :1], float("nan")),
    )
    mean_x = torch.where(valid_mask, x, torch.zeros_like(x)).sum(dim=1, keepdim=True) / n_valid.clamp(min=1)
    var_x = x_sq_masked.sum(dim=1, keepdim=True) / n_valid.clamp(min=1) - mean_x ** 2
    is_constant = var_x < 1e-8
    return torch.where(is_constant, torch.full_like(dw, float("nan")), dw)

### cross_decay_linear  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_decay_linear
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:284
@op("dt", "cross", arity=1, requires_window=True)
def cross_decay_linear(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), decay_linear_last, axis=0)

### day_close  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_close
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:144
@op("dt", "day", arity=1)
def day_close(x: torch.Tensor) -> torch.Tensor:
    """Alias for `day_last` (last non-NaN value of the day)."""
    return day_last(x)

### day_last  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_last
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:133
@op("dt", "day", arity=1)
def day_last(x: torch.Tensor) -> torch.Tensor:
    return last_valid_last(x).unsqueeze(-1)

### day_sum  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_sum
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:83
@op("dt", "day", arity=1)
def day_sum(x: torch.Tensor) -> torch.Tensor:
    return C._sum(x).unsqueeze(-1)
```

**10-03 23:41 · Bash** — Print digest of the final holdout run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F103_amt_dw_decay final f_orig 2>&1 | head -300
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

**10-03 23:41 · Bash** — Show holdout ledger and study_tools API

```bash
cd /Users/wxy/Desktop/Partura && cat runs/F103_amt_dw_decay/ledger.json && ls partura/ && grep -n "def " partura/study_tools.py | head -80
```

```
{
  "entries": [
    {
      "when": "2026-10-03T23:43:32Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:43:32Z",
      "split": "valid",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:43:32Z",
      "split": "utrain",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:47:56Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
… (168 行略) …
remote_tools.py
report.py
report_legacy.py
runner.py
semantics.py
splits.py
study_tools.py
45:    def __init__(self, factor_id: str, device: str = "cuda", gpu_fraction: float = 0.0) -> None:
55:    def __enter__(self) -> "Study":
68:    def __exit__(self, *exc) -> None:
75:    def panels(self, expressions: Dict[str, str]) -> Dict[str, np.ndarray]:
82:    def control(self, name: str) -> np.ndarray:
90:    def target(self, horizon: int = 1) -> np.ndarray:
93:    def slice(self, split: str) -> slice:
99:    def dates(self):
103:    def symbols(self):
107:    def sign(self, panel: np.ndarray, split: str = "train") -> float:
111:    def ic(self, panel: np.ndarray, split: str = "train", sign: Optional[float] = None) -> Dict[str, float]:
116:    def books(self, panel: np.ndarray, fit: str = "train", evals: Sequence[str] = ("train", "valid"),
126:    def rank_corr(self, a: np.ndarray, b: np.ndarray, split: str = "train") -> float:
```

10-03 23:41 · 读 `/Users/wxy/Desktop/Partura/partura/study_tools.py`

10-03 23:41 · 读 `/Users/wxy/Desktop/Partura/partura/books.py`

**10-03 23:42 · Bash** — Print source for remaining operators

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src cross_max ts_min pow_2 pow_3 mul day_std 2>&1 | head -150; grep -n "def src\|getsource\|helper" partura/remote_tools.py | head -20
```

```
### cross_max  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_max
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:232
@op("dt", "cross", arity=1, requires_window=True)
def cross_max(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), nanmax_last, axis=0)

### ts_min  face=nd family=ts category=rolling axis=D reduces_m=False lookahead=False kernel=nd_ts.ts_min
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_ts.py:171
@op("nd", "ts", arity=1, requires_window=True)
def ts_min(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, d, nanmin_last, axis=0)

### pow_2  face=shared family=elementwise category=unary axis=None reduces_m=False lookahead=False kernel=common.pow_
# /root/autodl-tmp/AlphaCube/src/alphacube/catalog.py:146
    ("pow_2", "pow_", lambda f: (lambda x: f(x, 2.0))),

### pow_3  face=shared family=elementwise category=unary axis=None reduces_m=False lookahead=False kernel=common.pow_
# /root/autodl-tmp/AlphaCube/src/alphacube/catalog.py:148
    ("pow_3", "pow_", lambda f: (lambda x: f(x, 3.0))),

### mul  face=shared family=elementwise category=binary axis=None reduces_m=False lookahead=False kernel=common.mul
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/common.py:158
@op("shared", "elementwise", arity=2)
def mul(x, y) -> torch.Tensor:
    if isinstance(x, (int, float)) and isinstance(y, torch.Tensor):
        x = create_like(y, x)
    elif isinstance(y, (int, float)) and isinstance(x, torch.Tensor):
        y = create_like(x, y)
    return torch.mul(x, y)

### day_std  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_std
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:108
@op("dt", "day", arity=1)
def day_std(x: torch.Tensor) -> torch.Tensor:
    return C._stddev(x).unsqueeze(-1)

1:"""Small read-only helpers a study runs ON THE SERVER (through scripts/study.sh).
52:def src(names) -> int:
61:            f, (lines, line) = inspect.getsourcefile(fn), inspect.getsourcelines(fn)
```

**10-03 23:42 · Bash** — Read the src helper in remote_tools

```bash
cd /Users/wxy/Desktop/Partura && sed -n 40,90p partura/remote_tools.py
```

```
        flags = ",".join(k for k in ("lookahead", "boolean_output", "trivial_boolean", "resource_risk",
                                     "coarse_output") if getattr(sp, k))
        win = f" win {list(sp.windows)}" if sp.requires_window else ""
        print(f"  {n:<34} {sp.face}/{sp.family}/{sp.category:<12} arity {sp.arity} axis {sp.compute_axis}{win}"
              f"{'  [' + flags + ']' if flags else ''}")
    print("# 只在完整库里的通用调用(手写因子用的;参数含字面量,签名看 src):")
    for n, sp in sorted(cat.entries.items()):
        if pat.search(n) and n not in reg._ops:
            print(f"  {n:<34} {sp.face}/{sp.family}  axis {sp.compute_axis} reduces_m {sp.reduces_m}")
    return 0


def src(names) -> int:
    reg, cat = _catalogs()
    for name in names:
        spec = reg._ops.get(name) or cat.get(name)
        if spec is None:
            print(f"### {name}: not found (ambiguous in the full catalog: {name in cat.ambiguous})")
            continue
        fn = inspect.unwrap(spec.fn)
        try:
            f, (lines, line) = inspect.getsourcefile(fn), inspect.getsourcelines(fn)
            print(f"### {name}  face={spec.face} family={spec.family} category={spec.category} "
                  f"axis={spec.compute_axis} reduces_m={spec.reduces_m} lookahead={spec.lookahead} "
                  f"kernel={spec.kernel_id}\n# {f}:{line}")
            print("".join(lines))
        except (OSError, TypeError) as exc:
            print(f"### {name}: {spec.kernel_id}: source unavailable ({exc})")
    return 0


def _config(fid: str) -> dict:
    return yaml.safe_load((PARTURA_ROOT / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))


def check(fid: str) -> int:
    from alphacube.expression import contains_lookahead, is_valid_root
    from .panels import parse_research
    cfg = _config(fid)
    items = {**(cfg.get("controls") or {}), **(cfg.get("gates") or {})}
    ids = set()
    bad = 0
    for st in cfg["stages"]:
        for v in st["variants"]:
            if v["id"] in ids:
                bad += 1
                print(f"DUPLICATE id {v['id']} (stage {st['id']}) — a later one silently replaces the earlier")
            ids.add(v["id"])
            items[f"{st['id']}/{v['id']}"] = v["expr"]
    keys = {}
    for k, s in items.items():
```

**10-03 23:42 · Bash** — Locate local AlphaCube operator sources

```bash
cd /Users/wxy/Desktop && ls -d */ 2>/dev/null | head -40; find /Users/wxy/Desktop -maxdepth 4 -name "dt_cross.py" -not -path "*/node_modules/*" 2>/dev/null | head
```

```
230A/
230P_hw2/
AlphaCube/
AlphaFactorMining/
AlphaFactorMining_autodl/
ETF_类型异质性研究项目/
JPM-Project-3ii/
Partura/
Texas Play/
Xiangyu Wang SRC/
__pycache__/
code/
hrx+/
hurst/
p_r_v/
proper_risk_taking/
ps8/
qmt_server_calculate/
result/
results/
train_model/
transform/
viewdb/
桌面整理/
面试刷题/
/Users/wxy/Desktop/code/operators/dt_cross.py
/Users/wxy/Desktop/AlphaFactorMining/src/operators/dt_cross.py
```

10-03 23:42 · 读 `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/x2_interaction.py`

**10-03 23:44 · Bash** — List diagnose.py functions and header

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^def \|^    def " partura/diagnose.py | head -60 && sed -n 1,60p partura/diagnose.py
```

```
42:def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
64:def rank_rows(x: np.ndarray) -> np.ndarray:
79:def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
83:def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
95:def _ir(x: np.ndarray) -> float:
100:def _tstat(x: np.ndarray) -> float:
105:def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
113:def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
136:def distinct_fraction(panel: np.ndarray, step: int = 5, min_names: int = 30) -> float:
149:def metric_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
162:    def curve(v: np.ndarray) -> Tuple[float, float]:
190:def _zrank(x: np.ndarray) -> np.ndarray:
197:def neutralise(panel: np.ndarray, controls: Dict[str, np.ndarray], space: str = "rank",
244:def conditional_ic(panel: np.ndarray, target: np.ndarray, gate: np.ndarray, buckets: int = 5,
271:def decay(panel: np.ndarray, targets: Dict[int, np.ndarray], sign: float = 1.0) -> List[Dict[str, float]]:
280:def by_year(panel: np.ndarray, target: np.ndarray, years: np.ndarray, *, sign: float = 1.0,
299:def extreme_day_dependence(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
318:def smoothing_sweep(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
341:def pair_rank_corr(a: np.ndarray, b: np.ndarray) -> float:
347:def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
"""Diagnostics that turn a panel into evidence about a hypothesis.

AlphaCube already answers "how good is it" (IC, ICIR, turnover, net Sharpe).
Partura needs to answer "where does it come from", so this module adds the
discriminating measurements AlphaCube has no reason to own:

* ``neutralise``        -- daily cross-sectional residual after regressing the
  factor on control panels (size / price / volatility / reversal / momentum).
  If the alpha survives, the controls do not explain it; if it dies, they do.
* ``conditional_ic``    -- the IC of A inside quantile buckets of B.  This is
… (30 行略) …

def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
    """``rank_rows`` on an accelerator: per-row average ranks (ties averaged) of
    the finite cells, NaN elsewhere -- the same answer as the pandas version
    (locked by tests/test_partura.py), without the CPU.  The server's CPU quota
    is usually taken by a neighbouring job while its GPU sits idle, and ranking
    a 1400 x 5200 panel is the single hottest call in a study."""
    import torch
    x = np.asarray(x, dtype=np.float64)
    out = np.empty(x.shape, dtype=np.float64)
    for a in range(0, x.shape[0], rows):
        t = torch.as_tensor(x[a:a + rows], device=device)
        fin = torch.isfinite(t)
        s, order = torch.sort(torch.where(fin, t, torch.full_like(t, float("inf"))), dim=1, stable=True)
        lo = torch.searchsorted(s, s, right=False)
        hi = torch.searchsorted(s, s, right=True)
        avg = (lo + hi + 1).to(torch.float64) / 2.0
        r = torch.empty_like(t).scatter_(1, order, avg)
        r[~fin] = float("nan")
        out[a:a + rows] = r.cpu().numpy()
```

**10-03 23:44 · Bash** — Read rank, IC and neutralise helpers

```bash
cd /Users/wxy/Desktop/Partura && sed -n 60,135p partura/diagnose.py && sed -n 186,270p partura/diagnose.py
```

```
        out[a:a + rows] = r.cpu().numpy()
    return out


def rank_rows(x: np.ndarray) -> np.ndarray:
    dev = os.environ.get("PARTURA_RANK_DEVICE", "")
    if dev:
        try:
            return _rank_rows_torch(x, dev)
        except Exception as exc:                         # never let the fast path decide the answer
            print(f"[diagnose] rank on {dev} failed ({type(exc).__name__}: {exc}); using pandas", flush=True)
    return _rank_rows_pandas(x)

COST_PER_SIDE = 0.0015          # 15 bp, AlphaCube's production assumption
TURNOVER_CAP = 0.30
TOP_FRAC = 0.10


# ---------------------------------------------------------------- basics
def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
    return cs_pearson(np.asarray(panel, dtype=np.float64), target)


def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
                   target_ranks: Optional[np.ndarray] = None) -> np.ndarray:
    """``rank_rows`` is pandas' ``rank(axis=1)`` -- correct (ties averaged, inf
    skipped) but slow on a 1000 x 5000 panel, and this is the single hottest
    call in a run.  Pre-computed ranks may be passed in; a correlation is
    invariant to an affine map, so a flipped factor can reuse the unflipped
    ranks with a sign."""
… (111 行略) …
    p = np.asarray(panel, dtype=np.float64)
    g = np.asarray(gate, dtype=np.float64)
    t = np.asarray(target, dtype=np.float64)
    rg = rank_rows(g)
    n = np.isfinite(rg).sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore"):
        b = np.floor((rg - 1.0) / np.maximum(n, 1) * buckets)
    rows = []
    for k in range(buckets):
        sel = (b == k)
        pk = np.where(sel, p, np.nan)
        ric = rank_ic_series(pk, np.where(sel, t, np.nan))
        icc = cs_pearson(np.where(sel, p, np.nan), np.where(sel, t, np.nan))
        rows.append({"bucket": k, "rank_ic": nanmean_quiet(ric), "rank_icir": _ir(ric),
                     "ic": nanmean_quiet(icc), "n_days": int(np.isfinite(ric).sum()),
                     "mean_names": float(np.nanmean(sel.sum(axis=1)))})
    return rows


# ---------------------------------------------------------------- time
```

**10-03 23:45 · Bash** — Check which Partura jobs are on the server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh status 2>&1 | tail -20
```

```
	554070.pt_F105_rev1	(10/04/26 14:42:24)	(Detached)

540353, 30176 MiB
554072, 860 MiB
container anon 9.0 GiB
gpu.lock slot0.lock slot1.lock slot2.lock
```

**10-03 23:45 · Bash** — Read the head of x3 script and limit-up logic in x1

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1,80p studies/F103_amt_dw_decay/x3_family.py && grep -n "lim\|1.095" studies/F103_amt_dw_decay/x1_anatomy.py | head -20
```

```
"""X3 -- after S1 / X1 / X2 the tree is  (amount level) x (roughness of the 30-day average intraday Amt curve)^k.
What is still open (hypotheses H13..H18 in notes/05_hypotheses.md, written before this script ran):

A. H13  Is the distilled skeleton the same family as F001's distilled factor cross_max(day_std(Amt), 9)?
B. H14  Do the scale-free concentration measures of the average curve (p_cv, p_peak) carry the signal alone,
        and what do exponent scans of day_sum * X^k look like for them?
C.      Year by year (books at the train-fitted half-life): which skeleton holds up after 2021?
D. H13/H14  Residual rank IC by year after neutralising on the known family.
E. H15  Is the valid long leg of the low-k variants a micro-cap tilt?
F. H16  5x5 dependent sorts amount x {p_peak, p_cv}: is "less concentrated is better" stable in the low-amount rows?
G. H17  Which minute is the peak of the average curve?
H. H18  The book smooths RAW values before ranking: is a monotone transform (log / rank) still a no-op?

Only `train` / `valid` rows are ever touched.
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

B = "cross_decay_linear(Amt, 30)"
EXPR = {
    "G": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "C": f"day_durbin_watson({B})",
    "dsum": "day_sum(Amt)",
    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
    "p_cv": f"div(day_std({B}), day_mean({B}))",
    "p_peak": f"div(day_max({B}), day_sum({B}))",
    "p_close": f"div(day_last({B}), day_sum({B}))",
… (35 行略) …
    years = np.asarray([d[:4] for d in dates])
    yy = sorted(set(years[use].tolist()))
    ysl = {}
    for y in yy:
        idx = np.nonzero(years == y)[0]
        idx = idx[(idx >= tr.start) & (idx < cut)]
        ysl[y] = slice(int(idx[0]), int(idx[-1]) + 1)
    G, C, dsum = P["G"], P["C"], P["dsum"]
    amt = np.asarray(st.control("ctl_amt"), dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap"), dtype=np.float64)
    turn = np.asarray(st.control("ctl_turnrate"), dtype=np.float64)
    std9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
    amt9 = np.asarray(st.control("known_amt_max9"), dtype=np.float64)
    print(f"[x3] panels ready {time.time() - T0:.0f}s; train {dates[tr][0]}..{dates[tr][-1]}  valid {dates[va][0]}..{dates[va][-1]}", flush=True)

14:   many of its labels are missing (locked at limit-up)?                (H8, H8b)
219:    lim5 = rmax((ctl["ctl_rev1"] >= 1.095).astype(np.float64), 5)[tr]
220:    lim1 = (ctl["ctl_rev1"] >= 1.095).astype(np.float64)[tr]
232:        l1 = float(np.nansum(np.where(sel, lim1, 0.0)) / max(sel.sum(), 1))
233:        l5 = float(np.nansum(np.where(sel, lim5, 0.0)) / max(sel.sum(), 1))
```

**10-03 23:46 · 写文件** `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/audit_1.py`(14471 字符)

**10-03 23:47 · Bash** — Patch the audit script and compile-check it

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import re, pathlib
p = pathlib.Path("studies/F103_amt_dw_decay/audit_1.py")
s = p.read_text()

# 1. average-rank zr (ties get the same rank; needed for the discrete limit-up count)
old = '''def zr(v):
    r = np.argsort(np.argsort(v, kind="stable"), kind="stable").astype(np.float64)
    return r / max(v.size - 1, 1) - 0.5
'''
new = '''def zr(v):
    _, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
    start = np.cumsum(cnt) - cnt
    r = (start + (cnt - 1) / 2.0)[inv]                          # 0-based average rank, ties share a rank
    return r / max(v.size - 1, 1) - 0.5
'''
assert old in s; s = s.replace(old, new)

# 2. keep only the smoothed signals sections B / D / E need
old = '''            sm = bk.smoothed(sig, hl)
            SM[(name, hl)] = sm
'''
new = '''            sm = bk.smoothed(sig, hl)
            if (name, hl) in KEEP:
                SM[(name, hl)] = sm
'''
assert old in s; s = s.replace(old, new)
old = '''    SM = {}
    for name, p in V.items():'''
new = '''    SM = {}
    KEEP = {("dsum*C^2 (REC)", 10), ("orig G", 2), ("orig G", 10), ("dsum*C^3", 10), ("dsum (amt only)", 10), ("dsum*C^1", 10)}
    for name, p in V.items():'''
assert old in s; s = s.replace(old, new)

# 3. cache daily series
old = '''    def daily(key, sl):
        sm, t = SM[key][sl], tgt[sl]
'''
new = '''    DAILY = {}

… (36 行略) …
        da, db = daily(a, ut)[0] - daily(b, ut)[0], years[ut]
        print(f"{'':28s} 逐年 d 年化(utrain 连续建书): " + "  ".join(f"{y} {np.nanmean(da[db == y]) * 25200:+5.1f}%" for y in yrs))
    print(f"[audit] E done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ D
'''
assert old in s; s = s.replace(old, new)
p.write_text(s)
EOF
~/.venvs/alphacube/bin/python -m py_compile studies/F103_amt_dw_decay/audit_1.py && echo compiled OK
```

```
compiled OK
```

**10-03 23:47 · Bash** — Review the patched middle of the audit script

```bash
cd /Users/wxy/Desktop/Partura && sed -n 95,175p studies/F103_amt_dw_decay/audit_1.py
```

```
with Study("F103_amt_dw_decay") as st:
    P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPR).items()}
    tr, va, ut = st.slice("train"), st.slice("valid"), st.slice("utrain")
    cut = va.stop                                              # nothing at or after this row is ever touched
    assert ut.stop <= cut and tr.stop <= cut
    tgt = np.asarray(st.target(), dtype=np.float64)[:cut]
    cost, top = float(st.cfg.get("cost_per_side", bk.COST)), float(st.cfg.get("top_frac", bk.TOP_FRAC))
    dates = np.asarray(st.dates)[:cut]
    years = np.asarray([d[:4] for d in dates])
    G, A, C, dsum = (P[k][:cut] for k in ("G", "A", "C", "dsum"))
    ctl = {n: np.asarray(st.control(n), dtype=np.float64)[:cut] for n in
           ("ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_mom20", "ctl_price", "ctl_rev1")}
    SPL = (("train", tr), ("valid", va), ("utrain", ut))
    print(f"[audit] panels ready {time.time() - T0:.0f}s; rows used 0..{cut} ({dates[tr][0]}..{dates[va][-1]}); "
          f"sign(train): G {st.sign(P['G']):+.0f}  dsum*C^2 {st.sign(P['dsum'] * P['C'] ** 2):+.0f}", flush=True)

    V = {"orig G": G, "A*C^3 (no max)": A * C ** 3, "dsum*C^3": dsum * C ** 3, "dsum*C^2 (REC)": dsum * C ** 2,
         "dsum*C^1": dsum * C, "dsum (amt only)": dsum}

    # ------------------------------------------------------------------ A
    print("\n== A. 固定半衰期下的两本书(方向一律 -1;每格 = 扣费多空夏普 | 多头腿净超额 | 纯多头夏普 | 多空日换手) ==")
    SM = {}
    KEEP = {("dsum*C^2 (REC)", 10), ("orig G", 2), ("orig G", 10), ("dsum*C^3", 10), ("dsum (amt only)", 10), ("dsum*C^1", 10)}
    for name, p in V.items():
        sig = -p
        fit_tr = bk.fit_halflives(sig, tgt, tr, cost, top)
        fit_ut = bk.fit_halflives(sig, tgt, ut, cost, top)
        print(f"\n{name}:  按多空夏普选的半衰期 train {fit_tr['hl_ls']:.0f} / utrain {fit_ut['hl_ls']:.0f};"
              f"  按纯多头夏普选 train {fit_tr['hl_long']:.0f} / utrain {fit_ut['hl_long']:.0f}")
        print("   utrain 上各半衰期的多空夏普: " + "  ".join(f"hl{s['halflife']:.0f} {s['ls_sharpe']:+.2f}" for s in fit_ut["sweep"]))
… (31 行略) …
             (("dsum*C^3", 10), ("orig G", 10), "纯删节点 k3@10 - 原式@10(同半衰期)"),
             (("orig G", 10), ("orig G", 2), "原式@10 - 原式@2(只改半衰期)"),
             (("dsum*C^2 (REC)", 10), ("dsum*C^3", 10), "REC@10 - k3@10(只改指数)"),
             (("dsum*C^2 (REC)", 10), ("dsum (amt only)", 10), "REC@10 - 纯成交额@10(C^2 加了什么)"),
             (("dsum*C^2 (REC)", 10), ("dsum*C^1", 10), "REC@10 - k1@10")]
    for a, b, lab in pairs:
        out = []
        for sn, sl in SPL:
            la, na = daily(a, sl)
            lb, nb = daily(b, sl)
            (m1, t1), (m2, t2) = tstat(la - lb), tstat(na - nb)
            out.append(f"{sn}: LS {m1:+5.1f}% (t {t1:+.1f})  L {m2:+5.1f}% (t {t2:+.1f})")
        print(f"{lab:38s} " + "   ".join(out), flush=True)
    print(f"[audit] B done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ E
    print("\n== E. C 给已知家族加的东西是 alpha 还是'减掉一部分成交额水平暴露'?  d = 加了 C 的多空净收益 - 没加的;"
          "回归 d = a + b * (纯成交额水平的多空净收益) ==")
    std9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)[:cut]
    SM[("std9", 0)] = -std9
```

**10-03 23:47 · Bash** — Start the audit script on the server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh exec F103_amt_dw_decay audit1 audit_1.py 2>&1 | tail -5
```

```
started F103_amt_dw_decay/audit1: audit_1.py
```

**10-03 23:47 · Bash** — Print the overview for F103

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python scripts/overview_for.py F103_amt_dw_decay 2>&1 | head -120
```

```
== F103_amt_dw_decay  (挖掘 #820; 方向 -1, 半衰期 2) ==
可交易信号(方向 x 面板,按公布的半衰期平滑)在 train 上的日截面 rank 相关:
  本批其他因子: F105(#25) +0.33  F108(#3264) +0.32  F101(day_shine_retstd) +0.30  F104(#4190) +0.30  F102(#3961) +0.29  F115(all_tide_mean_30) +0.22
  控制变量:     ctl_amt -0.26  ctl_mom20 -0.25  ctl_ivol -0.25  ctl_dvol20 -0.21  ctl_turnrate -0.17  ctl_range -0.13  ctl_cap -0.10  ctl_price +0.03  ctl_rev1 +0.03
  已知家族:     known_amt_max9 -0.32  known_stdamt_max9 -0.42  known_ivol_max9 -0.34
控制变量能张成它多少(秩空间逐日回归的 R²): 全部 0.227;单个: ctl_amt 0.081  ctl_mom20 0.073  ctl_ivol 0.064  ctl_dvol20 0.054  ctl_turnrate 0.038  ctl_cap 0.034  ctl_range 0.023  ctl_rev1 0.007  ctl_price 0.005
(注意:控制变量的符号没有对齐方向;相关的正负要结合因子方向读。|相关| ≥ 0.95 在 AlphaCube 里算同一因子族。)
```

**10-03 23:47 · Bash** — Wait for the audit job and print its log

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F103_amt_dw_decay audit1 540 2>&1 | tail -150
```

```
    ok = (n >= 2)[:, None]
    long_ = ok & (pos >= (n - k)[:, None]) & (pos < n[:, None])
    short = ok & (pos < k[:, None])
    w_sorted = np.where(long_, 0.5 / k[:, None], np.where(short, -0.5 / k[:, None], 0.0))
    w = np.zeros((D, S), dtype=np.float64)
    np.put_along_axis(w, order, w_sorted, axis=1)
    return w
--- alphacube.operators.common._sum  (5 lines)
def _sum(x: torch.Tensor) -> torch.Tensor:
    value = x.nansum(dim=-1)
    return torch.where(
        torch.isfinite(x).any(dim=-1), value, torch.full_like(value, float("nan"))
    )
[guard] all 2 run slots busy, waiting ...
[guard] got run slot 0 after 234s
[audit] panels ready 236s; rows used 0..1359 (20180102..20230807); sign(train): G -1  dsum*C^2 -1

== A. 固定半衰期下的两本书(方向一律 -1;每格 = 扣费多空夏普 | 多头腿净超额 | 纯多头夏普 | 多空日换手) ==

orig G:  按多空夏普选的半衰期 train 2 / utrain 2;  按纯多头夏普选 train 10 / utrain 10
   utrain 上各半衰期的多空夏普: hl0 +2.79  hl1 +3.27  hl2 +3.53  hl3 +3.50  hl5 +3.47  hl10 +3.39  hl20 +3.22
   hl2   train +4.14 |  +6.3% | +1.30 |  8.5%    valid +2.22 |  +3.6% | +0.66 |  8.5%    utrain +3.53 |  +5.6% | +1.11 |  8.4%
   hl5   train +4.13 |  +8.1% | +1.62 |  5.5%    valid +2.15 |  +5.0% | +0.86 |  5.6%    utrain +3.47 |  +7.3% | +1.39 |  5.5%
   hl10  train +4.09 |  +9.4% | +1.86 |  3.6%    valid +2.07 |  +4.5% | +0.73 |  3.8%    utrain +3.39 |  +8.1% | +1.49 |  3.6%
   hl20  train +3.95 |  +9.5% | +1.86 |  2.3%    valid +1.79 |  +2.9% | +0.46 |  2.4%    utrain +3.22 |  +7.6% | +1.39 |  2.3%

A*C^3 (no max):  按多空夏普选的半衰期 train 5 / utrain 5;  按纯多头夏普选 train 20 / utrain 20
   utrain 上各半衰期的多空夏普: hl0 -1.45  hl1 +2.38  hl2 +3.20  hl3 +3.54  hl5 +3.73  hl10 +3.69  hl20 +3.51
   hl2   train +3.72 |  +1.0% | +0.21 | 13.1%    valid +2.02 |  -1.1% | -0.20 | 13.0%    utrain +3.20 |  +0.5% | +0.09 | 13.1%
   hl5   train +4.35 |  +7.1% | +1.44 |  7.0%    valid +2.41 |  +4.1% | +0.73 |  7.1%    utrain +3.73 |  +6.3% | +1.22 |  7.0%
   hl10  train +4.33 |  +8.5% | +1.65 |  4.3%    valid +2.41 |  +4.8% | +0.79 |  4.5%    utrain +3.69 |  +7.4% | +1.37 |  4.3%
   hl20  train +4.12 | +10.3% | +1.98 |  2.5%    valid +2.27 |  +3.9% | +0.64 |  2.8%    utrain +3.51 |  +8.5% | +1.55 |  2.6%

dsum*C^3:  按多空夏普选的半衰期 train 20 / utrain 10;  按纯多头夏普选 train 20 / utrain 20
   utrain 上各半衰期的多空夏普: hl0 +1.48  hl1 +2.89  hl2 +3.34  hl3 +3.54  hl5 +3.62  hl10 +3.64  hl20 +3.63
   hl2   train +3.56 |  +1.9% | +0.37 |  9.7%    valid +2.76 |  +3.2% | +0.66 |  9.6%    utrain +3.34 |  +2.3% | +0.46 |  9.7%
   hl5   train +3.79 |  +6.0% | +1.19 |  5.9%    valid +3.19 |  +7.9% | +1.55 |  5.9%    utrain +3.62 |  +6.6% | +1.30 |  5.9%
   hl10  train +3.92 |  +8.8% | +1.76 |  3.9%    valid +2.96 |  +7.3% | +1.39 |  3.9%    utrain +3.64 |  +8.4% | +1.66 |  3.9%
   hl20  train +3.93 | +11.1% | +2.24 |  2.4%    valid +2.88 |  +7.5% | +1.45 |  2.5%    utrain +3.63 | +10.1% | +2.02 |  2.4%

dsum*C^2 (REC):  按多空夏普选的半衰期 train 10 / utrain 10;  按纯多头夏普选 train 20 / utrain 20
   utrain 上各半衰期的多空夏普: hl0 +1.22  hl1 +2.58  hl2 +3.06  hl3 +3.24  hl5 +3.39  hl10 +3.45  hl20 +3.23
   hl2   train +2.95 |  +3.1% | +0.57 | 10.2%    valid +3.40 |  +8.3% | +1.66 |  9.8%    utrain +3.06 |  +4.6% | +0.86 | 10.1%
   hl5   train +3.23 |  +8.1% | +1.43 |  6.0%    valid +3.84 | +14.6% | +2.81 |  5.9%    utrain +3.39 | +10.0% | +1.80 |  5.9%
   hl10  train +3.33 | +11.4% | +1.98 |  4.0%    valid +3.78 | +14.5% | +2.70 |  3.8%    utrain +3.45 | +12.3% | +2.18 |  3.9%
   hl20  train +3.05 | +12.6% | +2.19 |  2.4%    valid +3.77 | +15.3% | +2.81 |  2.4%    utrain +3.23 | +13.4% | +2.36 |  2.4%

dsum*C^1:  按多空夏普选的半衰期 train 10 / utrain 10;  按纯多头夏普选 train 10 / utrain 20
   utrain 上各半衰期的多空夏普: hl0 +0.84  hl1 +2.17  hl2 +2.64  hl3 +2.75  hl5 +2.76  hl10 +2.77  hl20 +2.53
   hl2   train +2.26 |  +5.6% | +0.85 |  9.3%    valid +3.81 | +13.6% | +2.37 |  8.8%    utrain +2.64 |  +7.9% | +1.24 |  9.2%
   hl5   train +2.36 | +10.1% | +1.50 |  5.2%    valid +3.99 | +18.1% | +3.03 |  4.9%    utrain +2.76 | +12.4% | +1.89 |  5.1%
   hl10  train +2.36 | +12.5% | +1.83 |  3.3%    valid +3.97 | +20.7% | +3.37 |  3.1%    utrain +2.77 | +14.9% | +2.24 |  3.2%
   hl20  train +2.12 | +12.6% | +1.82 |  2.1%    valid +3.73 | +21.7% | +3.50 |  1.9%    utrain +2.53 | +15.2% | +2.26 |  2.0%

dsum (amt only):  按多空夏普选的半衰期 train 5 / utrain 5;  按纯多头夏普选 train 10 / utrain 10
   utrain 上各半衰期的多空夏普: hl0 +0.29  hl1 +1.52  hl2 +1.84  hl3 +1.95  hl5 +1.98  hl10 +1.91  hl20 +1.80
   hl2   train +1.26 |  +5.6% | +0.77 |  7.4%    valid +3.59 | +17.7% | +2.85 |  7.1%    utrain +1.84 |  +9.1% | +1.30 |  7.3%
   hl5   train +1.42 |  +9.4% | +1.28 |  4.0%    valid +3.68 | +21.0% | +3.28 |  3.8%    utrain +1.98 | +12.7% | +1.79 |  3.9%
   hl10  train +1.34 | +10.3% | +1.39 |  2.6%    valid +3.58 | +22.8% | +3.50 |  2.4%    utrain +1.91 | +13.9% | +1.93 |  2.5%
   hl20  train +1.23 |  +9.7% | +1.30 |  1.7%    valid +3.49 | +23.7% | +3.64 |  1.5%    utrain +1.80 | +13.7% | +1.89 |  1.6%
[audit] A done 360s

== B. 日度配对差(a - b):年化均值差(%) 与 t 值;LS = 多空净收益,L = 多头腿净超额 ==
REC@10 - 原式@2(报告里的对比)                  train: LS  +1.7% (t +0.7)  L  +5.1% (t +1.8)   valid: LS +10.8% (t +3.0)  L +10.9% (t +2.5)   utrain: LS  +4.3% (t +2.0)  L  +6.7% (t +2.8)
REC@10 - 原式@10(同半衰期)                   train: LS  +4.0% (t +1.5)  L  +2.0% (t +0.7)   valid: LS +11.7% (t +3.4)  L +10.0% (t +2.1)   utrain: LS  +6.2% (t +2.9)  L  +4.2% (t +1.7)
纯删节点 k3@10 - 原式@10(同半衰期)               train: LS  +3.1% (t +2.5)  L  -0.6% (t -0.4)   valid: LS  +5.4% (t +3.2)  L  +2.8% (t +1.1)   utrain: LS  +3.8% (t +3.7)  L  +0.4% (t +0.3)
原式@10 - 原式@2(只改半衰期)                    train: LS  -2.2% (t -1.8)  L  +3.1% (t +2.5)   valid: LS  -0.9% (t -0.5)  L  +0.9% (t +0.5)   utrain: LS  -1.8% (t -1.8)  L  +2.5% (t +2.4)
REC@10 - k3@10(只改指数)                   train: LS  +0.9% (t +0.5)  L  +2.5% (t +1.3)   valid: LS  +6.3% (t +2.9)  L  +7.2% (t +2.7)   utrain: LS  +2.4% (t +1.8)  L  +3.9% (t +2.4)
REC@10 - 纯成交额@10(C^2 加了什么)             train: LS +11.9% (t +5.2)  L  +1.1% (t +0.5)   valid: LS  -2.4% (t -0.7)  L  -8.3% (t -3.1)   utrain: LS  +7.8% (t +4.1)  L  -1.6% (t -0.9)
REC@10 - k1@10                         train: LS  +4.1% (t +2.9)  L  -1.1% (t -0.8)   valid: LS  -3.9% (t -1.9)  L  -6.2% (t -3.2)   utrain: LS  +1.8% (t +1.5)  L  -2.6% (t -2.1)
[audit] B done 370s

== E. C 给已知家族加的东西是 alpha 还是'减掉一部分成交额水平暴露'?  d = 加了 C 的多空净收益 - 没加的;回归 d = a + b * (纯成交额水平的多空净收益) ==
F001蒸馏*C@2 - F001蒸馏@0        train : d 年化  +4.0% (t +3.4)   b -0.16  corr -0.62   a 年化  +6.0% (t +6.5)   夏普: 没加 +2.47 -> 加了 +3.32
F001蒸馏*C@2 - F001蒸馏@0        valid : d 年化  -2.1% (t -1.4)   b -0.11  corr -0.45   a 年化  +0.9% (t +0.7)   夏普: 没加 +4.44 -> 加了 +4.36
F001蒸馏*C@2 - F001蒸馏@0        utrain: d 年化  +2.2% (t +2.4)   b -0.15  corr -0.58   a 年化  +4.8% (t +6.2)   夏普: 没加 +2.94 -> 加了 +3.58
                             逐年 d 年化(utrain 连续建书): 2018  +5.3%  2019  +5.5%  2020  +5.9%  2021  -0.9%  2022  -2.7%  2023  -1.1%
REC@10 - 纯成交额@10             train : d 年化 +11.9% (t +5.2)   b -0.30  corr -0.58   a 年化 +15.4% (t +8.3)   夏普: 没加 +1.34 -> 加了 +3.33
REC@10 - 纯成交额@10             valid : d 年化  -2.4% (t -0.7)   b -0.29  corr -0.51   a 年化  +5.4% (t +1.8)   夏普: 没加 +3.58 -> 加了 +3.78
REC@10 - 纯成交额@10             utrain: d 年化  +7.8% (t +4.1)   b -0.30  corr -0.57   a 年化 +12.6% (t +8.0)   夏普: 没加 +1.91 -> 加了 +3.45
                             逐年 d 年化(utrain 连续建书): 2018 +10.2%  2019 +18.0%  2020 +15.2%  2021  +4.0%  2022  -1.1%  2023  -4.6%
[audit] E done 376s

== D. 多头十分位里标签缺失(记 0 收益)的权重占比 ==
dsum*C^2 (REC)@hl10  train: 多头 2.61%  全市场(有信号的票) 1.47%   valid: 多头 9.09%  全市场(有信号的票) 2.96%
orig G@hl2   train: 多头 2.32%  全市场(有信号的票) 1.47%   valid: 多头 8.36%  全市场(有信号的票) 2.96%
dsum (amt only)@hl10  train: 多头 3.44%  全市场(有信号的票) 1.47%   valid: 多头 7.97%  全市场(有信号的票) 2.96%

== C. 成交额最高 1/5 里的角落:是不是 C 特有的 ==
[audit] C loop done 389s

C1. 成交额最高 1/5 内,按不同变量再五分:最高一组(那 4%)的次日超额(年化 %);括号行 = 最高组 - 最低组
                              train    valid     2018     2019     2020     2021     2022     2023
整行(成交额最高 1/5)平均               -19.5    -34.3    -21.7    -19.8    -12.3    -24.2    -37.7    -28.6
C(集中度)                        -75.4    -63.6    -86.6    -86.9    -77.7    -50.3    -80.9    -34.6
   (5 - 1)                    -88.4    -34.3    -85.6   -111.8   -114.8    -41.3    -58.7     +6.8
成交额(组内再取最高)                   -19.5    -49.8    -21.7    -15.1     -6.8    -34.5    -59.0    -34.3
   (5 - 1)                     -8.4    -29.3     -5.7     -4.5     -4.7    -18.8    -35.8    -18.3
换手率                           -74.9    -94.6    -72.2    -72.6    -74.0    -80.7   -109.8    -68.9
   (5 - 1)                    -77.8    -83.6    -81.6    -82.4    -84.7    -62.5    -97.5    -60.2
20日波动                         -60.5    -77.3    -68.1    -60.1    -49.3    -64.4    -86.9    -61.1
   (5 - 1)                    -56.6    -55.3    -64.8    -68.5    -51.3    -41.5    -56.4    -53.5
日内波动                          -72.0    -91.2    -62.2    -76.6    -71.8    -77.5   -108.2    -62.6
   (5 - 1)                    -64.6    -75.6    -45.9    -76.3    -75.2    -60.8    -90.9    -49.8
20日动量                         -64.3    -90.3    -90.0    -83.6    -48.0    -37.8   -100.9    -72.6
   (5 - 1)                    -64.5    -80.5    -98.4    -93.1    -55.5    -13.7    -90.5    -63.6
30日MAX                        -62.7    -71.8    -75.3    -64.2    -56.0    -55.1    -80.3    -57.4
   (5 - 1)                    -58.0    -59.3    -72.0    -71.5    -53.9    -34.8    -65.1    -49.6
小市值                           -67.0    -76.2    -59.5    -67.2    -65.4    -76.1    -85.7    -60.3
   (5 - 1)                    -69.5    -65.0    -67.7    -73.2    -80.1    -56.8    -71.8    -53.5
低价                            -35.4    -36.1    -24.7    -41.0    -44.6    -31.1    -41.6    -26.8
   (5 - 1)                    -39.1     -9.2    -22.6    -57.5    -69.2     -6.8    -17.2     +4.3

C2. C 角落(成交额最高 1/5 x C 最高 1/5)按近期是否涨停过(日收益 >= 9.5%)拆开:次日超额(年化 %)与占比
                              train    valid     2018     2019     2020     2021     2022     2023
角落里近5日涨停过的占比                  46.1%    44.0%    42.6%    46.0%    47.6%    48.3%    48.4%    36.8%
整行里近5日涨停过的占比                  17.3%    17.0%    13.1%    16.3%    19.3%    20.6%    18.4%    14.7%
角落里近30日涨停过的占比                 70.9%    68.3%    68.4%    71.5%    71.1%    72.7%    73.0%    60.3%
整行里近30日涨停过的占比                 44.4%    43.6%    34.0%    41.8%    49.2%    52.5%    46.2%    39.3%
角落 且 近5日涨停过                  -117.7   -117.1   -145.2   -141.1   -108.7    -76.0   -136.0    -85.2
角落 且 近5日没涨停                   -34.8    -17.7    -37.1    -38.2    -43.5    -20.5    -24.8     -5.8
非角落 且 近5日涨停过                  -26.8    -58.8    -48.1    -33.7     -6.2    -19.4    -66.7    -45.6
非角落 且 近5日没涨停                   -2.8    -23.4     -2.8     +0.8     +8.4    -17.7    -22.7    -24.7
角落 且 近30日涨停过                  -89.2    -88.1   -107.6   -102.3    -87.2    -59.9   -102.6    -63.7
角落 且 近30日没涨停                  -41.3     -7.8    -39.3    -48.6    -53.2    -23.9    -19.3    +11.6
非角落 且 近30日涨停过                 -20.0    -37.7    -32.4    -22.9     -5.9    -18.7    -38.3    -36.6
非角落 且 近30日没涨停                  +3.0    -20.0     +1.5    +10.1    +16.1    -15.9    -20.5    -19.3

C3. 成交额最高 1/5 内,C 对已知暴露做组内秩回归:残差的最高组 / (5-1) / 组内 rank IC,对照同一批票上的原始 C
                              train    valid     2018     2019     2020     2021     2022     2023
-- 控制变量: 换手率+市值  (组内 R2 train 0.195 / valid 0.121)
原始 C 最高组                      -75.4    -63.6    -86.6    -86.9    -77.7    -50.3    -80.9    -34.6
残差 C 最高组                      -51.5    -44.7    -53.6    -57.4    -56.6    -38.4    -57.8    -22.8
已知暴露拟合值 最高组                   -74.4    -85.5    -63.6    -78.1    -78.8    -77.0    -97.9    -64.8
原始 C (5-1)                    -88.4    -34.3    -85.6   -111.8   -114.8    -41.3    -58.7     +6.8
残差 C (5-1)                    -58.5    -13.5    -48.5    -76.0    -81.4    -28.2    -32.3    +18.0
原始 C 组内 rank IC             -0.0613  -0.0254  -0.0604  -0.0806  -0.0705  -0.0337  -0.0359  -0.0078
残差 C 组内 rank IC             -0.0371  -0.0038  -0.0352  -0.0487  -0.0472  -0.0175  -0.0127  +0.0111
拟合值 组内 rank IC              -0.0706  -0.0727  -0.0612  -0.0883  -0.0778  -0.0553  -0.0731  -0.0721
-- 控制变量: 全部已知  (组内 R2 train 0.410 / valid 0.327)
原始 C 最高组                      -68.6    -57.9    -85.4    -86.5    -68.0    -35.9    -74.7    -29.8
残差 C 最高组                      -32.5    -21.7    -37.7    -40.0    -28.5    -24.4    -29.7     -8.2
已知暴露拟合值 最高组                   -66.7    -74.6    -73.3    -88.3    -66.1    -39.6    -89.8    -49.0
原始 C (5-1)                    -81.1    -28.1    -80.8   -111.6   -104.1    -27.6    -51.3    +10.8
残差 C (5-1)                    -33.6    +12.5    -31.9    -46.4    -45.5    -10.4     -0.2    +33.9
原始 C 组内 rank IC             -0.0590  -0.0232  -0.0588  -0.0812  -0.0670  -0.0289  -0.0335  -0.0060
残差 C 组内 rank IC             -0.0230  +0.0057  -0.0226  -0.0300  -0.0278  -0.0113  -0.0015  +0.0177
拟合值 组内 rank IC              -0.0646  -0.0482  -0.0588  -0.0875  -0.0773  -0.0342  -0.0544  -0.0379
[audit] done 389s
[partura exit 0 2026-10-04_14:54:13]
```

**10-03 23:54 · Bash** — Show helper source dump from the audit log

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F103_amt_dw_decay_audit1.log | sed -n 1,150p
```

```
== 0. 内部函数源码(服务器上的 AlphaCube) ==
--- alphacube.operators.dt_cross.rolling_reduce  (2 lines)
def rolling_reduce(x: torch.Tensor, d: int, reducer, axis: int = 0) -> torch.Tensor:
    return reducer(rolling_windows(x, d, axis))
--- alphacube.operators.dt_cross.decay_linear_last  (9 lines)
def decay_linear_last(w: torch.Tensor) -> torch.Tensor:
    """Linearly-weighted (most recent = heaviest) mean over valid entries."""
    d = w.shape[-1]
    weights = torch.arange(1, d + 1, dtype=w.dtype, device=w.device)
    valid = ~torch.isnan(w)
    w_filled = torch.where(valid, w, torch.zeros_like(w))
    weighted_sum = (w_filled * weights).sum(dim=-1)
    weight_total = (valid.to(w.dtype) * weights).sum(dim=-1)
    return torch.where(weight_total > EPS, weighted_sum / weight_total, torch.full_like(weighted_sum, float("nan")))
--- alphacube.operators.dt_cross.nanmax_last  (4 lines)
def nanmax_last(w: torch.Tensor) -> torch.Tensor:
    filled = torch.where(torch.isnan(w), torch.full_like(w, float("-inf")), w)
    out = filled.max(dim=-1).values
    return torch.where(torch.isnan(w).all(dim=-1), torch.full_like(out, float("nan")), out)
--- alphacube.operators.dt_day.last_valid_last  (13 lines)
def last_valid_last(w: torch.Tensor) -> torch.Tensor:
    """Last non-NaN value along the last dim; NaN if the slice has none.
    Shared by DT's `day_last`/`in_last`, same contract as `first_valid_last`.
    """
    d = w.shape[-1]
    idx = torch.arange(d, device=w.device).expand_as(w)
    valid = ~torch.isnan(w)
    idx_when_valid = torch.where(valid, idx, torch.full_like(idx, -1))
    last_idx = idx_when_valid.max(dim=-1, keepdim=True).values
    has_valid = last_idx >= 0
… (100 行略) …
   hl20  train +3.05 | +12.6% | +2.19 |  2.4%    valid +3.77 | +15.3% | +2.81 |  2.4%    utrain +3.23 | +13.4% | +2.36 |  2.4%

dsum*C^1:  按多空夏普选的半衰期 train 10 / utrain 10;  按纯多头夏普选 train 10 / utrain 20
   utrain 上各半衰期的多空夏普: hl0 +0.84  hl1 +2.17  hl2 +2.64  hl3 +2.75  hl5 +2.76  hl10 +2.77  hl20 +2.53
   hl2   train +2.26 |  +5.6% | +0.85 |  9.3%    valid +3.81 | +13.6% | +2.37 |  8.8%    utrain +2.64 |  +7.9% | +1.24 |  9.2%
   hl5   train +2.36 | +10.1% | +1.50 |  5.2%    valid +3.99 | +18.1% | +3.03 |  4.9%    utrain +2.76 | +12.4% | +1.89 |  5.1%
   hl10  train +2.36 | +12.5% | +1.83 |  3.3%    valid +3.97 | +20.7% | +3.37 |  3.1%    utrain +2.77 | +14.9% | +2.24 |  3.2%
   hl20  train +2.12 | +12.6% | +1.82 |  2.1%    valid +3.73 | +21.7% | +3.50 |  1.9%    utrain +2.53 | +15.2% | +2.26 |  2.0%

dsum (amt only):  按多空夏普选的半衰期 train 5 / utrain 5;  按纯多头夏普选 train 10 / utrain 10
   utrain 上各半衰期的多空夏普: hl0 +0.29  hl1 +1.52  hl2 +1.84  hl3 +1.95  hl5 +1.98  hl10 +1.91  hl20 +1.80
   hl2   train +1.26 |  +5.6% | +0.77 |  7.4%    valid +3.59 | +17.7% | +2.85 |  7.1%    utrain +1.84 |  +9.1% | +1.30 |  7.3%
   hl5   train +1.42 |  +9.4% | +1.28 |  4.0%    valid +3.68 | +21.0% | +3.28 |  3.8%    utrain +1.98 | +12.7% | +1.79 |  3.9%
   hl10  train +1.34 | +10.3% | +1.39 |  2.6%    valid +3.58 | +22.8% | +3.50 |  2.4%    utrain +1.91 | +13.9% | +1.93 |  2.5%
   hl20  train +1.23 |  +9.7% | +1.30 |  1.7%    valid +3.49 | +23.7% | +3.64 |  1.5%    utrain +1.80 | +13.7% | +1.89 |  1.6%
[audit] A done 360s

== B. 日度配对差(a - b):年化均值差(%) 与 t 值;LS = 多空净收益,L = 多头腿净超额 ==
REC@10 - 原式@2(报告里的对比)                  train: LS  +1.7% (t +0.7)  L  +5.1% (t +1.8)   valid: LS +10.8% (t +3.0)  L +10.9% (t +2.5)   utrain: LS  +4.3% (t +2.0)  L  +6.7% (t +2.8)
REC@10 - 原式@10(同半衰期)                   train: LS  +4.0% (t +1.5)  L  +2.0% (t +0.7)   valid: LS +11.7% (t +3.4)  L +10.0% (t +2.1)   utrain: LS  +6.2% (t +2.9)  L  +4.2% (t +1.7)
```

**10-03 23:57 · Bash** — Inspect structure of final.json

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d = json.load(open("runs/F103_amt_dw_decay/final.json"))
print(list(d.keys()))
def walk(o, path="", depth=0):
    if isinstance(o, dict) and depth < 3:
        for k, v in o.items():
            t = type(v).__name__
            n = len(v) if hasattr(v, "__len__") else ""
            print("  " * depth + f"{k}: {t} {n}")
            if depth < 2: walk(v, path + "/" + k, depth + 1)
walk(d)
EOF
```

```
['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
factor_id: str 17
config: str 30
stages: list 1
provenance: dict 11
  alphacube_root: str 26
  alphacube_commit: str 7
  alphacube_dirty: bool 
  partura_root: str 24
  partura_commit: NoneType 
  partura_code_sha: str 12
  store: str 51
  python: str 6
  torch: str 11
  numpy: str 5
  host: str 36
view: dict 5
  days: int 
  symbols: int 
  first: str 8
  last: str 8
  warmup_rows: int 
label: dict 3
  kind: str 11
  horizon: int 
  buyable: bool 
cost_per_side: float 
top_frac: float 
fit_split: str 5
user_split: str 6
… (92 行略) …
    f_sum_k3: dict 19
    f_sum_k2: dict 19
    f_std9_k1: dict 19
    f_stdamt9: dict 19
    ctl_amt: dict 19
    ctl_cap: dict 19
    ctl_turnrate: dict 19
    ctl_ivol: dict 19
    ctl_dvol20: dict 19
    ctl_price: dict 19
    ctl_rev1: dict 19
    ctl_mom20: dict 19
    known_amt_max9: dict 19
    known_stdamt_max9: dict 19
    known_ivol_max9: dict 19
    ref_base: dict 19
    ref_A5: dict 19
    ref_C: dict 19
seconds: float 
peak_anon_gb: float
```

**10-03 23:57 · Bash** — Extract user-caliber book rows from final.json

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d = json.load(open("runs/F103_amt_dw_decay/final.json"))
for k, r in d["results"].items():
    bu = r["books_user"]
    print(k, "keys:", list(bu.keys()))
    print("   hl_ls", bu.get("hl_ls"), "hl_long", bu.get("hl_long"), "hl_used", bu.get("hl_used"))
    for sp, row in bu["splits"].items():
        print(f"   {sp:8s} LS {row['ls_sharpe']:+.3f}  Lgross {row['long_gross_ann']*100:+.2f}%  Lnet {row['long_ann']*100:+.2f}%  Lshp {row['long_sharpe']:+.3f}  Lmdd {row['long_mdd']*100:+.1f}%  TO {row['ls_turnover']*100:.2f}%  short {row['short_gross_ann']*100:+.1f}%  n {row['n_days']}")
    if "splits_at_hl_long" in bu:
        for sp, row in bu["splits_at_hl_long"].items():
            print(f"   [at hl_long {bu['hl_long']}] {sp:8s} LS {row['ls_sharpe']:+.3f}  Lnet {row['long_ann']*100:+.2f}%  Lshp {row['long_sharpe']:+.3f}  TO {row['ls_turnover']*100:.2f}%")
print(d["diagnostics"]["rank_corr_train"]["f_sum_k2"]["f_orig"], d["diagnostics"]["rank_corr_train"]["f_sum_k2"]["ctl_amt"])
EOF
```

```
f_orig keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
   hl_ls 2.0 hl_long 10.0 hl_used 2.0
   utrain   LS +3.533  Lgross +12.75%  Lnet +5.57%  Lshp +1.108  Lmdd -9.1%  TO 8.43%  short +38.7%  n 1359
   holdout  LS +3.180  Lgross +12.41%  Lnet +5.47%  Lshp +1.044  Lmdd -7.1%  TO 8.20%  short +36.6%  n 581
   [at hl_long 10.0] utrain   LS +3.395  Lnet +8.05%  Lshp +1.487  TO 3.64%
   [at hl_long 10.0] holdout  LS +2.923  Lnet +7.17%  Lshp +1.260  TO 3.60%
f_sum_k3 keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
   hl_ls 10.0 hl_long 20.0 hl_used 10.0
   utrain   LS +3.640  Lgross +11.76%  Lnet +8.43%  Lshp +1.658  Lmdd -7.2%  TO 3.86%  short +36.6%  n 1359
   holdout  LS +3.518  Lgross +12.32%  Lnet +9.23%  Lshp +1.765  Lmdd -5.1%  TO 3.66%  short +35.4%  n 581
   [at hl_long 20.0] utrain   LS +3.628  Lnet +10.09%  Lshp +2.015  TO 2.41%
   [at hl_long 20.0] holdout  LS +3.331  Lnet +10.65%  Lshp +1.989  TO 2.37%
f_sum_k2 keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
   hl_ls 10.0 hl_long 20.0 hl_used 10.0
   utrain   LS +3.446  Lgross +15.74%  Lnet +12.30%  Lshp +2.179  Lmdd -6.9%  TO 3.89%  short +37.5%  n 1359
   holdout  LS +3.099  Lgross +15.58%  Lnet +12.64%  Lshp +2.071  Lmdd -5.2%  TO 3.45%  short +34.6%  n 581
   [at hl_long 20.0] utrain   LS +3.233  Lnet +13.39%  Lshp +2.360  TO 2.40%
   [at hl_long 20.0] holdout  LS +2.876  Lnet +13.54%  Lshp +2.233  TO 2.15%
f_std9_k1 keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
   hl_ls 2.0 hl_long 10.0 hl_used 2.0
   utrain   LS +3.580  Lgross +19.10%  Lnet +13.29%  Lshp +2.274  Lmdd -8.6%  TO 6.91%  short +43.1%  n 1359
   holdout  LS +3.142  Lgross +16.93%  Lnet +11.64%  Lshp +1.547  Lmdd -9.2%  TO 6.36%  short +44.1%  n 581
   [at hl_long 10.0] utrain   LS +3.200  Lnet +15.59%  Lshp +2.610  TO 3.44%
   [at hl_long 10.0] holdout  LS +2.749  Lnet +14.16%  Lshp +1.924  TO 3.12%
f_stdamt9 keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
   hl_ls 0.0 hl_long 5.0 hl_used 0.0
   utrain   LS +2.943  Lgross +19.16%  Lnet +11.90%  Lshp +1.817  Lmdd -10.7%  TO 8.27%  short +40.7%  n 1359
   holdout  LS +2.551  Lgross +15.17%  Lnet +8.19%  Lshp +0.890  Lmdd -15.4%  TO 8.03%  short +46.0%  n 581
   [at hl_long 5.0] utrain   LS +2.658  Lnet +16.13%  Lshp +2.410  TO 4.06%
   [at hl_long 5.0] holdout  LS +2.199  Lnet +13.23%  Lshp +1.402  TO 3.90%
0.745168134833809 0.7445991437629734
```

**10-03 23:59 · Bash** — Confirm audit log and files exist locally

```bash
cd /Users/wxy/Desktop/Partura && ls -la logs/F103_amt_dw_decay_audit1.log studies/F103_amt_dw_decay/ && git status --short 2>/dev/null | head -10; ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d = json.load(open("runs/F103_amt_dw_decay/S2_distil.json"))
n = d["diagnostics"].get("neutralise") or d["diagnostics"].get("neutralize")
print(type(n), list(d["diagnostics"].keys()))
EOF
```

```
-rw-r--r--@ 1 wxy  staff  19904 Oct  3 23:54 logs/F103_amt_dw_decay_audit1.log

studies/F103_amt_dw_decay/:
total 160
drwxr-xr-x@ 8 wxy  staff    256 Oct  3 23:46 .
drwxr-xr-x@ 9 wxy  staff    288 Oct  3 18:37 ..
drwxr-xr-x@ 4 wxy  staff    128 Oct  3 23:47 __pycache__
-rw-r--r--@ 1 wxy  staff  18544 Oct  3 23:47 audit_1.py
-rw-r--r--@ 1 wxy  staff   8411 Oct  3 18:43 probes.py
-rw-r--r--@ 1 wxy  staff  14541 Oct  3 18:46 x1_anatomy.py
-rw-r--r--@ 1 wxy  staff  12787 Oct  3 19:45 x2_interaction.py
-rw-r--r--@ 1 wxy  staff  16074 Oct  3 22:40 x3_family.py
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
<class 'dict'> ['decay', 'by_year', 'by_year_scope', 'neutralise', 'conditional', 'rank_corr_train']
```

**10-04 00:01 · StructuredOutput**

```json
{
 "factor_id": "F103_amt_dw_decay",
 "lens": "机制与过拟合",
 "issues": [
  {
   "severity": "major",
   "where": "verdict 第 (2) 点、10_distilled.md「为什么说提纯成功、升华有限」、established 第 1 条(S1 f_sum「多头腿两段更好」)",
   "what": "多头腿改善的第一步被归因于「删节点降换手」,实际上换手下降 100% 来自半衰期 2→10(原式按多空夏普选半衰期时 hl2 只比 hl10 高 0.05/0.14),与删节点无关。同半衰期下,删三个节点对多头腿在 train/utrain 上没有贡献。报告自己在 08_variants 里提醒过「先看固定半衰期表」,但结论没有照此改写。",
   "evidence": "audit_1 A/B 节 + final.json 的 splits_at_hl_long 行(同一次留出段读取里已算好,未重读):原式@hl10 换手 3.6%(utrain 与留出段都是),k3@hl10 是 3.9%/3.7%。utrain 多头腿净超额:原式@2 +5.6% → 原式@10 +8.1%(配对差 +2.5%,t +2.4)→ k3@10 +8.4%(配对差 +0.4%,t +0.3;train −0.6%,valid +2.8% t +1.1)→ k2@10 +12.3%。留出段:原式@10 多头腿净超额 +7.2%、纯多头夏普 1.26、LS 2.92 → k3@10 +9.2%/1.77/3.52 → k2@10 +12.6%/2.07/3.10。S1 的 f_sum 对原式「两段更好」在 hl10 下 train 是 +8.8% 对 +9.4%(更差)。另外 hl0(不平滑)时 utrain 多空夏普:原式 +2.79、A·C³(删 cross_max)−1.45、推荐者 +1.22 —— cross_max「多余」只在下游一定有 EMA 时成立。",
   "fix": "把多头腿的分解改成三步并以 原式@hl10 为基准:只改半衰期(utrain +2.5 点 / 留出段 +1.7 点,对原式本身就可用)、删节点(+0.4 / +2.1)、指数 3→2(+3.9 / +3.4,已知暴露)。verdict 里「删节点降换手」改为「半衰期 2→10 降换手」;established 第 1 条删去「多头腿两段更好」或注明是半衰期差异;注明 5 个算子的版本依赖外部 EMA(hl≥5)。"
  },
  {
   "severity": "major",
   "where": "verdict 主句与 recommended(多头腿净超额 +12.3%/+12.6%、纯多头夏普 2.18/2.07)、established 第 6 条",
   "what": "推荐者的多头腿不是这棵树给的,而且在同半衰期下不优于纯成交额水平:对只能做多的用户,它相对已知家族没有收益上的增量,集中度腿反而略微拖累多头腿。报告承认「第二步增加的是已知暴露」,但没有给出「纯 day_sum(Amt) 同半衰期」这一行,读者会把 +12.3% 读成提纯成果。",
   "evidence": "audit_1 A/B 节(utrain,hl10):day_sum(Amt) 多头腿净超额 +13.9%/纯多头夏普 1.93;day_sum·C(k=1,与 ctl_amt 相关 0.94)+14.9%/2.24;推荐者 +12.3%/2.18。配对差 推荐者 − 纯成交额:多头腿 train +1.1%(t +0.5)、valid −8.3%(t −3.1)、utrain −1.6%(t −0.9);推荐者 − k1:utrain −2.6%(t −2.1)。C² 加的全在多空(train LS +11.9%/年 t +5.2,valid −2.4%)。留出段(final.json hl_long 行):f_stdamt9@hl5 多头腿净超额 +13.2%、f_std9_k1@hl10 +14.2%,都不低于推荐者的 +12.6%;推荐者只赢在纯多头夏普(2.07 对 1.40 / 1.92)。中性化表里推荐者的残差是各候选中最小的:all_controls 后 rank IC 0.0123、无成本多空夏普 +1.81(原式 0.0172/+2.83,x_std9_k1 0.0170/+3.37,F001 蒸馏 0.0193/+5.03)。相对原式@hl10 的多头腿优势 train 只有 +2.0%(t +0.7),valid +10.0%(t +2.1,正是成交额水平的大年)。",
   "fix": "verdict 明写:对纯多头,多头腿收益来自已知的成交额水平家族,同半衰期下 day_sum(Amt) 或 k=1 不输;推荐者相对已知家族的优势只在留出段的纯多头夏普/回撤(事后选出的一个观测)。在第 10 节对比表里加上 day_sum@hl10、k=1@hl10 两行(train/valid/utrain),并写出中性化后推荐者残差最小这一点。"
  },
  {
   "severity": "major",
   "where": "mechanism 第 (4) 点、established 第 4 条、09_diagnosis 已确立第 5 条、11_risks「这棵树最稳的发现」、12_next 第 1 条(剔除名单)",
   "what": "「成交最活跃 × 曲线最集中的 4% 两段都稳定」这个事实成立,但它不是集中度特有的:在成交额最高 1/5 里按任何已知的热门股代理再取最高 1/5,都得到同样深或更深、且更稳定的角落;把 C 对已知暴露做组内残差后,valid 上角落和组内 rank IC 都消失。研究只做了全截面的 eps_C 与事件变量的 rank 相关(X2-f,R² 0.174),没有在预测力所在的角落里做替换实验,所以没有排除「角落 = 已知的高换手/高波动/近期涨停效应,C 只是它的一个代理」。",
   "evidence": "audit_1 C 节(与 X2-b 同口径,C 角落复现 −75.4%/−63.6%)。C1:同一行里按换手率取最高组 −74.9%/−94.6%(2021–2023 逐年 −80.7/−109.8/−68.9,C 是 −50.3/−80.9/−34.6),日内波动 −72.0/−91.2,20 日动量 −64.3/−90.3,小市值 −67.0/−76.2;整行平均 −19.5/−34.3。C 的组内 5−1 价差 2023 年是 +6.8,换手率是 −60.2。C2:角落里 46%/44% 近 5 日有过 ≥9.5% 的涨幅(整行 17%);剔掉这些票后角落 −34.8%/−17.7%,而非角落且没涨停的是 −2.8%/−23.4% —— valid 上角落完全是近期涨停票。C3:C 对{换手率,市值}做组内秩残差后组内 rank IC −0.0613/−0.0254 → −0.0371/−0.0038;对全部已知暴露(加波动、动量、价格、MAX、涨停次数,组内 R² 0.41/0.33)后 −0.0230/+0.0057,逐年 −0.023/−0.030/−0.028/−0.011/−0.002/+0.018;残差最高组 −32.5%/−21.7%(valid 上比整行平均 −34.3% 还好),已知暴露拟合值的最高组 −66.7%/−74.6%。",
   "fix": "把这条从「集中度的稳定发现」降级为:角落是已知的「活跃 × 热门」效应,C 是代理之一;C 特有的成分只在 2018–2020(GP 的样本内)存在,2021 减半,2022–2023 为零或反号。one_line/mechanism 里「集中度只在活跃票里有预测力」后面加上「2021 年起这部分已被换手率/波动/涨停史解释」。12_next 的剔除名单实验要以换手率或涨停史的角落为基准,C 须证明有增量。"
  },
  {
   "severity": "major",
   "where": "family、mechanism 第 (5) 点、established 第 5/6 条(「集中度腿不在已知家族里」「两条腿轮动」「留出段上集中度腿加了 +0.59」)",
   "what": "「集中度腿在已知家族之外、且会轮动回来」的唯一证据是留出段一次配对差 +0.59;train/valid 上同一个增量是单调衰减而不是轮动。notes 的 09_diagnosis 把它放在「合理但没坐实」,但 JSON 的 family/established 把它写成了结论。竞争解释「乘 C 等于减掉一部分成交额水平暴露,在成交额水平走弱/2024 微盘回撤时机械地更好」没有排除。",
   "evidence": "audit_1 E 节:F001 蒸馏×C − F001 蒸馏 的多空净收益差逐年 +5.3/+5.5/+5.9/−0.9/−2.7/−1.1 %(2018→2023);推荐者 − 纯成交额 +10.2/+18.0/+15.2/+4.0/−1.1/−4.6 %。增量与纯成交额水平多空收益的相关 −0.62/−0.45(train/valid),回归系数 −0.16/−0.11;对冲掉成交额水平后的 alpha train +6.0%(t +6.5),valid +0.9%(t +0.7)。X3-D 自己的残差 rank IC valid 是 +0.0016~+0.0066。留出段 581 天单个多空夏普的标准误约 0.65,两个相关 0.93 的因子的配对差标准误约 0.3~0.4,+0.59 约 1.5 个标准误;留出段没有放 day_sum 基准,也没有量成交额中性集中度的 IC(报告自己承认)。",
   "fix": "family 改为:「水平腿与 F001 同族;集中度腿在 2018–2020 有已知家族之外的成分,2021–2023 没有,留出段一次观测(+0.59,约 1.5σ)提示可能恢复,未坐实」。mechanism (5) 的「轮动」改为「2021–2023 成交额水平强、集中度增量为零;是否回归待新数据」。established 第 6 条后半句移到「合理但没坐实」。"
  },
  {
   "severity": "major",
   "where": "10_distilled.md「最终推荐」、verdict「事前写下的三条判据在留出段都过了」、recommended 的 ls_test / long_*_test",
   "what": "最终推荐是读完留出段之后改选的(事前首选 f_std9_k1),playbook 硬规矩 3 的精神是留出段不参与挑选;而且推荐者自己在 config 里的事前判据被留出段触发了,却没有出现在 verdict 的判据清点里。改选的留出段理由(「多头腿更稳」)有一部分是半衰期产物。报告做了披露,但「轻微选择偏差」+「三条判据都过」的表述把不利结果说轻了。",
   "evidence": "config 里 f_sum_k2 的 why:「若留出段上它不如 f_sum_k3,'指数 3 是 train 的局部最优'这个读法在样本外不成立」;留出段 f_sum_k2 多空夏普 +3.10 < f_sum_k3 +3.52(−0.42),即第四条事前判据没过,而被推荐的正是这一步。final.json hl_long 行:事前首选 f_std9_k1 在 hl10 下留出段多头腿净超额 +14.2%、纯多头夏普 1.92(推荐者 +12.6%/2.07),与推荐者分不出高下;报告引用的 +11.6%/1.55 是 hl2 的数。「成交额水平占比高的候选多头腿明显变差:f_stdamt9 1.82→0.89」是 hl0 的数,hl5 下是 2.41→1.40、净超额 16.1%→13.2%。在三个非基准候选里按留出段纯多头夏普取最大,预期上偏约 0.2~0.3。",
   "fix": "报告与 JSON 并列给出:协议内的推荐(事前首选 f_std9_k1:留出段 LS 3.14、多头腿 +11.6%/1.55)与事后改选(f_sum_k2),后者的留出段数字标为「事后在三个候选中选出,不是干净的样本外」。「三条判据都过了」后面补一句「f_sum_k2 自己的判据(不低于 f_sum_k3)没过」。10_distilled 里候选的留出段多头腿对比补上同半衰期(hl_long)的数字。"
  },
  {
   "severity": "major",
   "where": "JSON 的 known_exposure_r2: 0.227 与 recommended_kind: distilled",
   "what": "0.227 是原式的 R²,不是推荐者的;推荐者被已知暴露张成一半以上。推荐者与原式的 rank 相关 0.745,恰好等于它与 ctl_amt 的相关(0.745),与 F001 蒸馏结果 0.74 —— 它是原式和成交额水平家族的中点,不是同一个因子的提纯;按 0.95 的同族线甚至 0.86 的 f_sum_k3 都不算同族。把它标成 distilled 会让汇总表误读。",
   "evidence": "中性化表:d_sum_k2 all_controls R² 0.554(原始日频面板 0.639),ctl_amt 单独 0.462;v_base 才是 0.227/0.081。final.json rank_corr_train:f_sum_k2–f_orig 0.7452,f_sum_k2–ctl_amt 0.7446;f_sum_k3–f_orig 0.86。11_risks 正文写对了(「推荐版有一半以上是已知暴露」),与 JSON 字段矛盾。",
   "fix": "known_exposure_r2 改成 0.554(并注明原式 0.227 是尺度抵消)。recommended_kind 改为 blend/elevated,或者把 distilled 给 f_sum_k3(5 个算子、与原式 0.86、留出段 LS +3.52、事前判据通过),f_sum_k2 作为「向已知家族加权的混合版」单列。"
  },
  {
   "severity": "minor",
   "where": "X1-8(标签缺失率只查了 train)、11_risks 容量一段",
   "what": "多头十分位里标签缺失(记 0 收益)的权重在 valid 上很高,X1-8「H8b 不成立、缺失不是问题」只对 train 的空头端成立。口径上偏保守(持仓收益为正时低估超额),但说明多头书约一成权重在次日开盘买不进或没有成交的票上,留出段可能更高。",
   "evidence": "audit_1 D 节:推荐者@hl10 多头书标签缺失权重 train 2.61%(全市场 1.47%)、valid 9.09%(全市场 2.96%);原式@hl2 2.32%/8.36%;day_sum@hl10 3.44%/7.97%。",
   "fix": "查清这些票的构成(北交所 / 停牌前后 / 开盘 15 分钟无成交),在容量与成本风险里写出 valid 的 9%,并说明多头腿净超额是在「这部分记 0」的口径下算的。"
  },
  {
   "severity": "minor",
   "where": "JSON 的 variants_tested: 24、11_risks「过拟合」",
   "what": "24 只数了引擎变体;X1–X3 三份脚本另有约 80 行数值重建(k 扫描 0~8、p_peak/p_cv 各指数、窗口、log/rank 变换)同样在 train/valid 上看过并影响了候选选择,有效比较次数约 100。",
   "evidence": "11_risks 自己写的「24 个引擎变体和三份脚本里约 80 行数值重建」;ledger 只记了引擎运行(train/valid 各 32 条表达式)。",
   "fix": "字段或风险段写成「24 个引擎变体 + 约 80 行数值重建」;推荐者位于单调曲线中段而非孤立峰值这一点可以保留。"
  },
  {
   "severity": "minor",
   "where": "established 第 2 条、09_diagnosis 第 2 条「尺度也不能约掉」",
   "what": "措辞不准:i_addrank(两支排名相加,完全没有数值尺度)与原式相关 0.95、表现相同(+4.01/+1.81);塌掉的 i_rankmul、f_share 的共同点是对成交额水平的载荷为 0 或负(与 ctl_amt 相关 0.04 / −0.53)。实验区分的是「成交额水平载荷」,不是「数值尺度」。",
   "evidence": "S1 表:i_addrank +4.01/+1.81,i_rankmul +2.77/−0.08,f_share +1.52/−1.96;08_variants 的「一条轴」读法本身就是按与 ctl_amt 的相关排的。",
   "fix": "改成「成交额水平的载荷不能降到零(0.04 时 valid 不赚钱)」,删去「尺度」的说法。"
  }
 ],
 "checked": [
  "读完 CLAUDE.md、docs/method.md、docs/study_playbook.md、最终报告全文(含全部 notes 段落)、configs/F103_amt_dw_decay.yaml、ledger.json、S_final 的 digest、overview_for.py 输出、x2/x3 脚本",
  "算子语义(study.sh src + audit_1 第 0 节印出的内部函数源码):day_durbin_watson = Σ(Δx)²/(Σx²+1e-8),相邻两点都有效才计差分,常数行/有效点<2 给 NaN,齐次度 0 —— 与 notes 一致;cross_decay_linear → decay_linear_last 权重 1..d、当天最重、NaN 天从分母剔除 —— 一致;day_close = last_valid_last(最后一个非 NaN 分钟)—— 一致;day_sum = nansum,全 NaN 给 NaN(停牌日不会变成 0 混进多头端)—— notes 没写但无碍;pow_ 指数>1 时是普通幂 —— 一致;cross_max = NaN 跳过的最大值 —— 一致;ema_rows 因果、缺失日不更新状态 —— 一致。日轴全部因果,无跨日向前看;标签 t+1 开盘→t+2 开盘,因子只用到 t 日 15:00",
  "established 1(三个节点多余):ts_min 逐位相同 ✓;cross_max 低通 ✓(但仅在下游有 EMA 时:hl0 下 A·C³ utrain −1.45 对原式 +2.79);「day_close→day_sum 多头腿两段更好」是半衰期混淆(见 issue 1);留出段 f_sum_k3 +3.52 对 +3.18 通过事前判据,同 hl10 下是 3.52 对 2.92",
  "established 2(骨架/缺一不可/先平均后折叠):S1、X1-6、X2-e 支持;没排除的读法是「所有变体都落在成交额水平载荷这一条轴上」,「尺度」措辞不准(issue 9)",
  "established 3(R² 0.227 是尺度抵消不是新颖):X1-4 斜率 + 中性化表支持,成立;但该数被填进了推荐者的 known_exposure_r2(issue 6)",
  "established 4(单边避雷、4% 角稳定):事实复现(−75.4%/−63.6%),但不是 C 特有,valid 上被已知暴露完全解释(issue 3,audit C 节)",
  "established 5(轮动):逐年事实核对无误;「轮动」只有一个周期且留出段一侧是推断,train/valid 上增量是单调衰减(issue 4,audit E 节)",
  "established 6(k 3→2 提升多头腿、C 给 F001 加 0.59):数字与 final.json 一致;同半衰期下相对原式 train 不显著,相对纯成交额/k=1 多头腿不占优(issue 2);+0.59 约 1.5σ 且在 hl_long 口径下仍是 +0.55(2.75 对 2.20),对半衰期稳健",
  "分辨:overview 确认原式 R² 0.227、与本批其他因子相关 ≤0.33;推荐者 R² 0.554/0.639、ctl_amt 单独 0.462、与 F001 蒸馏 0.74;中性化后残差在候选里最小",
  "噪声/邻域:推荐者在 k=1/1.5/2/3 的单调曲线中段、窗口 10~60 平台、utrain 上 hl5/10/20 的多空夏普 3.39/3.45/3.23,不是孤立尖峰;但它相对 k3/原式的优势主要来自 valid(配对 t 2.7~3.4,train 0.5~1.5),留出段多空夏普反而输 k3 0.42",
  "同一个因子吗:与原式 rank 相关 0.745(= 与 ctl_amt 的 0.745),不同族;纯删节点 f_sum_k3 是 0.86",
  "多头腿:名义上三段都比原式好;同 hl10 口径下 utrain +4.2 点(t 1.7)、留出段 +5.5 点(7.2%→12.6%),多空夏普持平或略低 —— 多头腿变好而多空没有同向变好",
  "留出段:只读了一次(ledger:holdout reads=1,5 条表达式);前后记诚实,但推荐是读后改选、f_sum_k2 自己的事前判据未过(issue 5);JSON 数字与 final.json 逐项核对一致(ls 3.446/3.099、long_net 12.30%/12.64%、long_sharpe 2.179/2.071、换手 3.89%、rank 相关 0.745)",
  "未改动 configs/F103_amt_dw_decay.yaml、notes、partura/、scripts/;没有读留出段(audit_1 把所有数组截到 valid 末行之前;留出段同半衰期数字取自研究员那一次 final 运行已存的 final.json)"
 ],
 "refutation_attempt": "做了一次反驳实验:/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/audit_1.py(study.sh exec,tag audit1;日志 /Users/wxy/Desktop/Partura/logs/F103_amt_dw_decay_audit1.log)。只用 train/valid/utrain,所有面板在计算前截到 valid 最后一行,没有读留出段,没有用 final,没有改 config。口径自检:原式 hl2 复现 +4.14/+2.22/+3.53,推荐者 hl10 复现 +3.33/+3.78/+3.45,C 角落复现 X2-b 的 −75.4%/−63.6%。\n\n设计与结果:\nA/B. 固定半衰期 + 日度配对差(iid t 值,未做自相关修正)。问题:「提纯让多头腿更好」是不是只是半衰期。结果:原式@hl10 utrain LS 3.39、多头腿净超额 +8.1%、纯多头夏普 1.49、换手 3.6%;k3@hl10 3.64/+8.4%/1.66/3.9%;推荐者@hl10 3.45/+12.3%/2.18/3.9%;k1@hl10 2.77/+14.9%/2.24;纯 day_sum@hl10 1.91/+13.9%/1.93。配对差(多头腿净超额,utrain):只改半衰期 +2.5%(t 2.4);删节点 +0.4%(t 0.3);推荐者−原式@10 +4.2%(t 1.7,train +2.0% t 0.7,valid +10.0% t 2.1);推荐者−纯成交额 −1.6%(t −0.9,valid −8.3% t −3.1);推荐者−k1 −2.6%(t −2.1)。多空上 C² 对纯成交额 train +11.9%/年(t 5.2)、valid −2.4%。结论:换手下降全部来自半衰期;删节点对多头腿在 utrain 上无贡献(留出段 final.json 的 hl_long 行显示 +2.1 点);推荐者的多头腿就是成交额水平的多头腿。这一点对研究员不利的部分成立,但推荐者相对原式的多头腿优势在同半衰期下仍为正,没有被推翻。\nC. 角落特异性。问题:「成交最活跃 × 最集中的 4%」是不是 C 特有。结果:同一行按换手率取最高组 −74.9%/−94.6%(C:−75.4%/−63.6%),日内波动 −72.0/−91.2,动量 −64.3/−90.3,小市值 −67.0/−76.2;角落里 46%/44% 近 5 日涨停过,剔掉后 −34.8%/−17.7%(非角落且没涨停 −2.8%/−23.4%);C 对全部已知暴露做组内秩残差后组内 rank IC −0.0230/+0.0057(逐年 −0.023/−0.030/−0.028/−0.011/−0.002/+0.018),残差最高组 −32.5%/−21.7%(整行平均 −19.5%/−34.3%)。结论:机制第 (4) 点里「集中度特有、两段稳定」被推翻一半 —— 2018–2020 有 C 特有成分,valid 上完全是已知的热门股效应。\nE. C 对已知家族的增量是 alpha 还是减仓。F001 蒸馏×C − F001 蒸馏 逐年 +5.3/+5.5/+5.9/−0.9/−2.7/−1.1 %;与成交额水平多空收益相关 −0.62/−0.45;对冲后 alpha train +6.0%(t 6.5)、valid +0.9%(t 0.7)。结论:train/valid 上是衰减不是轮动;留出段的 +0.59 无法在不重读留出段的前提下与「减仓」解释分开。\nD. 多头书标签缺失权重:推荐者 train 2.61%、valid 9.09%(全市场 1.47%/2.96%)。\n0. 内部函数源码与 notes 的算子描述一致,没有发现跨日向前看或 NaN 语义读错。",
 "overall": "没有发现 critical 问题:算子语义读对了,没有泄漏,留出段只读一次,数字与原始 JSON 一致,研究员对大部分弱点(已知暴露、小市值倾斜、读后改选)做了披露。推荐的表达式本身是一个可用的因子(留出段 LS +3.10、多头腿净超额 +12.6%),不是挑出来的噪声尖峰。\n\n但有六处需要降级或改写,都指向同一件事 —— 报告把「向已知的成交额水平家族加权」和「换了半衰期」的收益,写成了这棵树提纯的成果:\n1. 多头腿改善里,换手下降全部来自半衰期 2→10(原式自己换半衰期就能拿到 utrain +2.5 点 / 留出段 +1.7 点),删节点在 utrain 上对多头腿贡献为零。\n2. 推荐者的多头腿在同半衰期下不优于纯 day_sum(Amt) 或 k=1;对纯多头用户,这棵树相对已知家族没有收益增量,只有留出段上(事后选出的)夏普/回撤优势。\n3. 「活跃 × 集中的 4% 角」不是集中度特有的:换手率、波动、动量、涨停史给出同样深且更稳的角落;C 特有的成分只在 2018–2020 存在,valid 上为零。\n4. 「集中度腿在已知家族之外、会轮动回来」只有留出段一次约 1.5σ 的观测支持,train/valid 上是单调衰减。\n5. 推荐是读完留出段后改选的,且它自己的事前判据(不低于 k=3)没过;同半衰期下事前首选 f_std9_k1 并不差。\n6. JSON 里 known_exposure_r2 0.227 是原式的(推荐者 0.554),recommended_kind 标成 distilled 而它与原式只有 0.745。\n\n建议的定性:提纯 = f_sum_k3(5 个算子,与原式 0.86,事前判据通过,留出段 LS +3.52);f_sum_k2 是「原式与成交额水平家族的混合版」,对多头腿更好但增量是已知暴露;机制一句话应改为「成交额水平 × 一个在 2018–2020 有独立信息、此后被换手率/波动/涨停史解释的集中度代理」。"
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/audit_1.py`

## 它返回给工作流的结构化结果

见 `handoff/F103_amt_dw_decay/results/audit-mechanism.json`。

## 它拿到的任务书

```
[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的审查员,负责**机制与过拟合**这一路 —— 一个多疑的量化研究员。另一位研究员刚完成了因子 F103_amt_dw_decay 的研究;
  你的任务是**尝试推翻**它的机制解释和它推荐的候选。默认立场:在证据把别的解释排除掉之前,结论不成立。
  
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
  
  研究员自己报告的结论(待推翻):
  {
   "one_line": "成交额水平 ×(最近 30 天平均日内成交额曲线的粗糙度/集中度)³:成交活跃、且成交长期挤在少数几分钟(主要是 9:31 那一根)的股票之后跑输;钱主要在空头腿。",
   "mechanism": "原式 = cross_max(A·C³, 5),A = day_close(Amt) 是收盘集合竞价那一根的成交额(带成交额尺度),C = day_durbin_watson(cross_decay_linear(Amt,30)) 是\"先把 241 根分钟成交额逐分钟做 30 日平均、再量这条平均曲线的粗糙度\"(尺度无关)。读源码+拆解后:(1) ts_min(·,1) 是恒等、cross_max(·,5) 只是低通(书对原始数值做 EMA,重尾正数的 EMA 本身就是带衰减的峰值记忆)、收盘竞价那一根换成全天成交额更好——三个节点多余;(2) 骨架是「成交额水平 × 集中度^k」,两条腿缺一不可,且\"先平均再折叠\"不可交换;(3) C³ 把 A 的成交额尺度约掉一半多(log C 对 log 成交额斜率 −0.174,×3),所以原式与 ctl_amt 相关只有 0.28、全部控制变量 R² 只有 0.227,这是抵消不是新颖;(4) 交互是真的且单边:集中度只在成交活跃的票里有预测力,两段都稳定的只有\"成交最活跃 × 曲线最集中\"的 4% 股票(次日超额年化 −75%/−64%~−79%),空头十分位五分之一是近 5 日打过板的票;成交额低的那几行里集中度方向 train/valid 相反,对多头腿没有稳定贡献;(5) 两条腿在时间上轮动:集中度 2018–2020 与 2024–2025 强,成交额水平 2021–2023 强(valid 恰是成交额水平的大年)。指数 k 是两条腿的配比旋钮(同时决定尾部多重):k=3 押集中度,多空夏普不差但多头腿弱;k=2 两腿各半,多头腿净超额翻倍。",
   "family": "成交额水平 × 30 日平均日内成交曲线的集中度:水平腿与 F001 同族(成交额水平 + 峰值记忆),集中度腿不在已知家族里(留出段上给 F001 蒸馏结果加了 0.59 个多空夏普),但它只在活跃票的空头端稳定。",
   "known_exposure_r2": 0.227,
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
   "verdict": "提纯成功,升华有限。推荐 mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 30))))(5 个算子,原式 7 个):用户口径 训练/测试 多头腿净超额 +5.6%/+5.5% → +12.3%/+12.6%,纯多头夏普 +1.11/+1.04 → +2.18/+2.07,多空夏普 +3.53/+3.18 → +3.45/+3.10(低 0.08,噪声以内),换手 8.4% → 3.9%;2018–2025 每一年多空夏普 ≥ +2.2、多头腿净超额 ≥ +6%。事前写下的三条判据在留出段都过了:纯删节点版(k=3)多空夏普 +3.52 对原式 +3.18;事前推荐的升华版 f_std9_k1 多头腿 +11.6%/+1.55 高于原式、多空夏普 +3.14;它比已知家族基准(F001 蒸馏,+2.55)高 0.59。必须说明的三点:(1) 最终推荐是读完留出段之后在五个事前定死的候选里改选的——事前首选是 f_std9_k1(依据是 valid 上的优势),留出段没有重现该优势(多空夏普打平,纯多头夏普 1.55 对 2.07),改选 f_sum_k2 的理由有三条是事前已知的(换手低一半、多头腿不依赖近乎掷硬币的半衰期、与 F001 蒸馏结果相关 0.74 而非 0.93),一条来自留出段,所以它的留出段数字带轻微选择偏差;(2) 多头腿的改善拆开是两步:删节点降换手(+5.5% → +9.2%,毛超额不变)和把指数从 3 降到 2、把权重还给成交额水平(+9.2% → +12.6%)——第二步增加的是已知暴露(ctl_amt 单独的 R² 从 0.081 升到 0.462),多头十分位市值百分位 0.29/0.21,train/valid 上市值中性后只剩约 +2%;(3) 这棵树特有的集中度腿对多头腿没有稳定贡献,它的价值在空头端(那 4% 活跃且集中的票)。若只看多空夏普,k=3 的纯删节点版(留出段 +3.52)更合适。",
   "established": [
    "七个算子里三个多余:ts_min(·,1) 恒等(探针 + S1 a_no_tsmin 逐位相同);cross_max(·,5) 只是低通(S1:删掉 +4.35/+2.41、换均值 +4.26/+2.49,原式 +4.14/+2.22);收盘竞价额换成全天成交额多头腿两段更好(S1 f_sum)。三个一起删(f_sum_k3)留出段多空夏普 +3.52 对原式 +3.18,多头腿净超额 +9.2% 对 +5.5%(S_final)。",
    "骨架是「成交额水平 × 30 日平均曲线集中度^k」,两条腿缺一不可、尺度不能约掉、平均必须在折叠之前:只留 A +1.81/+3.69,只留 C +1.79/−1.75,A 换成尾盘占比 valid −1.96,排名相乘 valid −0.08(S1);先逐日 DW 再平均代入整树 +1.00/+1.14(X1-6);当日 DW 方向都反 −1.38/−2.77(X2-e);窗口 10~60 是平台。",
    "原式被全部控制变量张成的 R² 只有 0.227,是因为 C³ 把 A 的成交额尺度约掉一半多(log C 对 log 成交额斜率 −0.174,X1-4),不是因为它新;中性化后 rank IC 0.0358 → 0.0172,空头腿 +42.8% → +9.1%,多头腿毛超额 +13.5% → +11.4%(S0 中性化表)。各版本中性化后的残差 rank IC 都在 0.012~0.019(S2 中性化表)。",
    "集中度是单边的避雷变量:C 的条件 rank IC 按成交额五分桶 −0.0028 → −0.0611(S1);5×5 依次分组两段都稳定的只有「成交最活跃 × 最集中」的 4%(次日超额年化 −75%/−64%,用峰值占比 −75%/−79%),低成交额行方向 train/valid 相反(X2-b、X3-F)。空头十分位 20.68% 近 5 日打过板,标签缺失率不高于全市场(X1-8)。",
    "两条腿轮动:成交额水平 2020 年多空夏普 +0.19、2022 年 +4.07;集中度单独 2020 年 +4.94、2023 上半年 −0.28(X3-C);留出段 2024/2025 年 F001 蒸馏结果 +2.21/+2.11,k=3 版 +3.59/+3.08(S_final 逐年)。valid 是成交额水平的大年(各成交额类控制变量多空夏普是 train 的 1.8~3.4 倍)。",
    "指数 3 → 2(f_sum_k2)把多头腿净超额从 +5.6%/+5.5% 提到 +12.3%/+12.6%、纯多头夏普 +1.11/+1.04 → +2.18/+2.07,多空夏普 +3.45/+3.10(S2、S_final);留出段上集中度腿给 F001 蒸馏结果加了 +0.59 多空夏普(f_std9_k1 +3.14 对 f_stdamt9 +2.55,S_final)。"
   ],
   "variants_tested": 24
  }
  
  ## 要回答的问题(把查过的写进 checked)
  
  1. **每条「已确立」的结论,背后是哪个实验?** 那个实验真的能把这条结论和它最强的竞争解释区分开吗?
     还是换一种解释也会得到同样的结果?把研究**没有排除**的那个解释写出来。
  2. **算子语义读对了吗?** 自己用 ./scripts/study.sh src <算子> 读关键算子的源码,核对 notes 里对它的描述。
     特别留意:时间方向(有没有用到当天之后的数据;日内向前看是允许的,跨日向前看不允许)、
     NaN 与边界行为、带不带尺度、布尔/档位输出。
  3. **「分辨」站得住吗?** 说它是(或不是)某个已知暴露,有没有中性化的 R² 与残差表现、有没有直接替换实验?
     看 overview:cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python scripts/overview_for.py F103_amt_dw_decay
  4. **推荐的候选是不是挑出来的噪声?** 数一数全研究试了多少个变体;推荐者相对原式的改进有多大
     (这批因子在测试段上的噪声大约是多空夏普 ±0.3);改进是不是 train 和 valid 同向、多头腿和多空同向;
     邻域(窗口、指数换一档)稳不稳;它是不是恰好只在 valid 上最好。
  5. **它还是同一个因子吗?** 推荐者与原式的 rank 相关是多少?如果很低,这不是「提纯」而是换了一个因子 ——
     可以,但必须这么说。
  6. **多头腿**。用户只能做多。推荐者的多头腿净超额、纯多头夏普相对原式是变好了还是只是多空夏普变好了?
  7. **留出段**。留出段的结果支持还是不支持 notes 里的说法?有没有把不利的留出段结果轻描淡写?
  
  你**可以**做一次反驳实验(不是必须):在 configs/F103_amt_dw_decay.yaml 末尾加一个阶段 SA_audit(≤ 6 个变体,
  只用 train/valid,**绝不**读留出段、绝不用 study.sh final),用 ./scripts/study.sh check 然后
  ./scripts/study.sh run F103_amt_dw_decay audit1 SA_audit、wait 取结果;或者写 studies/F103_amt_dw_decay/audit_*.py 用 exec 跑。
  只在它能直接检验你最怀疑的那一点时才做。做了就把设计与结果写进 refutation_attempt。
  
  issues 里每条写清 severity(critical = 机制结论或推荐因此不成立;major = 需要降级措辞或补实验;minor)、
  where、what、evidence、fix。没有问题就返回空数组,不要凑数;但也不要因为报告写得流畅就放过它。
```
