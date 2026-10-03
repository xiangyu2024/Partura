"""Write the skeleton config of one study from a batch file.

The skeleton carries only what is the SAME for every factor of the batch --
label, splits, cost, the published row to reproduce, the shared controls and
the "known family" panels to compare against -- plus a single stage,
``S0_baseline``, that scores the original expression.  Everything else (which
questions to ask, which variants, which extra controls, which probes) is the
study's own work and is deliberately not generated here.

    python scripts/new_study.py batches/B01_single_factors.yaml [factor_id ...]
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SHARED = "/root/autodl-tmp/Partura/shared"

batch = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
want = set(sys.argv[2:])

TEMPLATE = '''# Partura study {fid}  ({lib} / {name})
# 这份文件只有 S0_baseline 是生成的。后面的阶段、变体、额外控制变量、探针,都要按**这棵树**来写。
factor_id: {fid}
title: "(读完这棵树之后,用一句话写它是什么)"
expression: "{expr}"
baseline_id: v_base

# 用户表里公布的这一行(pick_single_factors 的口径);S0 要先把它复现出来
published: {{sign: {sign}, hl: {hl}, ls: [{ls0}, {ls1}], long: [{lo0}, {lo1}], lib: "{lib}", name: "{name}"}}

label: {{kind: open_vwap15, horizon: 1, buyable: true,
        verify_against: /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy}}
cost_per_side: 0.0015
top_frac: 0.10
rank_by: ls
horizons: [1, 2, 3, 5, 10, 20]
warmup: 60

# train + valid = 用户的训练段(utrain);holdout = 用户的测试段,只在最后读一次
splits:
  train:   ["20180102", "20211231"]
  valid:   ["20220101", "20230807"]
  utrain:  ["20180102", "20230807"]
  holdout: ["20230808", "20251231"]
  full:    ["20180102", "20251231"]
fit_split: train
user_split: utrain

# ---- 这一批共用的控制变量(都是日频、因果、只用到 t 日收盘)。按这棵树的嫌疑增删。
controls:
  ctl_amt:    "log(add(day_sum(Amt), 1))"                                  # 成交额水平
  ctl_price:  "log(day_last(Close))"                                       # 价格水平
  ctl_ivol:   "day_std(Ret)"                                               # 日内已实现波动
  ctl_range:  "div(sub(day_max(High), day_min(Low)), day_last(Close))"     # 日内振幅
  ctl_rev1:   "div(day_last(Close), ts_delay(day_last(Close), 1))"         # 当日收益(毛比值,秩等价)
  ctl_mom20:  "div(day_last(Close), ts_delay(day_last(Close), 20))"        # 20 日动量
  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
external_controls:
  ctl_cap:      {shared}/log_float_cap.npy        # log 流通市值 —— 把"规模"和"成交活跃"分开
  ctl_turnrate: {shared}/log_turnover_rate.npy    # log(成交额 / 流通市值)

# ---- 既往研究里确认过的家族,用来分辨"这是不是已知的东西换了个写法"
gates:
  known_amt_max9:    "cross_max(day_sum(Amt), 9)"          # F001:成交额水平 + 极值记忆
  known_stdamt_max9: "cross_max(day_std(Amt), 9)"          # F001 的蒸馏结果
  known_ivol_max9:   "cross_max(day_var(Ret), 9)"          # F001:日内波动 + 极值记忆
corr_with: [ctl_amt, ctl_cap, ctl_turnrate, ctl_ivol, ctl_dvol20, ctl_price, ctl_rev1, ctl_mom20,
            known_amt_max9, known_stdamt_max9, known_ivol_max9]

diagnostics:
  decay:      [v_base]
  by_year:    [v_base]
  neutralise: [v_base]
  profile:    [v_base]
  conditional:
    - {{factor: v_base, gate: ctl_cap, buckets: 5}}
    - {{factor: v_base, gate: ctl_amt, buckets: 5}}

stages:
  - id: S0_baseline
    question: "Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?"
    variants:
      - {{id: v_base, group: baseline, expr: "{expr}", why: "原始表达式"}}
'''

for f in batch["factors"]:
    if want and f["id"] not in want:
        continue
    dest = ROOT / "configs" / f"{f['id']}.yaml"
    if dest.exists():
        print(f"skip {dest.name} (exists)")
        continue
    dest.write_text(TEMPLATE.format(fid=f["id"], lib=f["lib"], name=f["name"], expr=f["expr"],
                                    sign=f["sign"], hl=f["hl"], ls0=f["ls"][0], ls1=f["ls"][1],
                                    lo0=f["long"][0], lo1=f["long"][1], shared=SHARED), encoding="utf-8")
    print(f"wrote {dest.name}")
