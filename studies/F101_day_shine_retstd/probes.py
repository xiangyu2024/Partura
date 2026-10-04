"""Probes this study needs and the built-ins do not answer.

F101 is "event mask -> statistic of ANOTHER series in a short window hanging
off each event -> day mean -> cross-sectional fold".  The middle node,
`in_sustain_stddev(mask, data, 5)`, is a TRIGGER operator: its first operand
is a 0/1 mask, not a signal.  The built-in probes feed it two random float
series, so `mask == 1` is never true, the output is all-NaN, and every
built-in reading on it ("order-independent", "shift-invariant", "finite frac
0.0", homogeneity None) is vacuous.  What one actually needs to know:

* Which minutes does the window read, relative to the trigger?  Before it,
  after it, including it?  (`minute_offsets_read`; self-check: `in_delay(x, d)`
  must read exactly offset -d.)
* What counts as a trigger, and what does a row without one give?
  (`trigger_semantics`)
* What statistic is it, how is it normalised, and what happens when the
  window runs off the end of the row?  (`ramp_window_readout`: feed the ramp
  0,1,2,..., for which k consecutive integers have population std
  sqrt((k^2-1)/12) -- 0, 0.5, 0.8165, 1.1180, 1.4142 for k = 1..5 -- so one
  number reads off both the normalisation and how many values were used;
  self-check: `in_stddev_full` on a 5-wide ramp must give 1.4142 if it is the
  population std its source says it is.)
* How does the comparison that builds the mask treat NaN and ties?
  (`comparison_semantics`)
"""

import torch

from partura.probes import ProbeContext, probe


def _minute_axis_keeps_m(s):
    return s.compute_axis == "M" and not getattr(s, "reduces_m", False)


def _is_trigger_op(ctx: ProbeContext) -> bool:
    """Measured, not by name: no trigger -> nothing; one trigger per row -> one value per row."""
    if ctx.arity != 2:
        return False
    R, T = ctx.shape
    data = ctx.sample(301, positive=False)
    none = ctx.call([torch.zeros(ctx.shape, dtype=torch.float64), data]).double()
    one = torch.zeros(ctx.shape, dtype=torch.float64)
    one[:, T // 2] = 1.0
    hit = ctx.call([one, data]).double()
    return bool(torch.isfinite(none).sum() == 0 and torch.isfinite(hit).sum() == R
                and torch.isfinite(hit[:, T // 2]).all())


@probe("minute_offsets_read",
       question="第 j 分钟的输出读了输入的哪些相对分钟?(窗口朝后看还是朝前看、含不含当分钟;触发型算子以触发分钟为 j)",
       applies=lambda s: _minute_axis_keeps_m(s) and s.requires_window)
def _offsets(ctx: ProbeContext):
    R, T = ctx.shape
    j = T // 2
    data = ctx.sample(201, positive=False)
    if ctx.arity == 2 and _is_trigger_op(ctx):
        mask = torch.zeros(ctx.shape, dtype=torch.float64)
        mask[:, j] = 1.0
        pack = lambda d: [mask, d]
    elif ctx.arity == 2:
        other = ctx.sample(202, positive=False)
        pack = lambda d: [other, d]
    else:
        pack = lambda d: [d]
    base = ctx.call(pack(data)).double()[:, j]
    hits = []
    for k in range(-(j - 1), T - j - 1):
        d2 = data.clone()
        d2[:, j + k] += 10.0
        out = ctx.call(pack(d2)).double()[:, j]
        both = torch.isfinite(base) & torch.isfinite(out)
        moved = bool((((out - base).abs() > 1e-9) & both).any())
        flipped = bool((torch.isfinite(base) != torch.isfinite(out)).any())
        if moved or flipped:
            hits.append(k)
    return hits


@probe("trigger_semantics",
       question="mask 取什么值才算触发?没有触发的分钟、没有任何触发的整行,输出是什么?",
       applies=lambda s: _minute_axis_keeps_m(s) and s.category == "pair_rolling")
def _trigger(ctx: ProbeContext):
    if not _is_trigger_op(ctx):
        return "不是触发型算子(第一个操作数不是 0/1 掩码)"
    R, T = ctx.shape
    data = ctx.sample(211, positive=False)
    fires = []
    for v in (1.0, 2.0, 0.5, -1.0, float("nan")):
        m = torch.zeros(ctx.shape, dtype=torch.float64)
        m[:, T // 2] = v
        if bool(torch.isfinite(ctx.call([m, data]).double()[:, T // 2]).all()):
            fires.append(v)
    m = torch.zeros(ctx.shape, dtype=torch.float64)
    m[: R // 2, T // 2] = 1.0                      # top half of the rows has one trigger, bottom half none
    out = ctx.call([m, data]).double()
    return {"fires_on_mask_values": fires,
            "non_trigger_minutes_finite_frac": round(float(torch.isfinite(out[: R // 2]).double().mean()), 4),
            "row_without_trigger_all_nan": bool(torch.isnan(out[R // 2:]).all()),
            "int_mask_works": bool(torch.isfinite(
                ctx.call([m.to(torch.int32), data]).double()[: R // 2, T // 2]).all())}


@probe("ramp_window_readout",
       question="喂斜坡 0,1,2,…:整窗时读出多少(总体 std 是 1.4142,样本 std 是 1.5811)?"
                "触发点离行尾只剩 m 分钟时读出多少(k 个连续整数的总体 std = sqrt((k²-1)/12))?",
       applies=lambda s: _minute_axis_keeps_m(s))
def _ramp(ctx: ProbeContext):
    R, T = ctx.shape
    if ctx.arity == 1 and not ctx.spec.requires_window and ctx.caller is None:
        # full-row statistic: a 5-wide ramp is the known-answer case (self-check for std-type kernels)
        ramp = torch.arange(5, dtype=torch.float64).reshape(1, 5).repeat(R, 1)
        out = ctx.call([ramp]).double()
        return {"five_wide_ramp": round(float(out[0, 0]), 4)}
    if not (ctx.arity == 2 and _is_trigger_op(ctx)):
        return None
    ramp = torch.arange(T, dtype=torch.float64).reshape(1, T).repeat(R, 1)
    res = {}
    for m_left in (T // 2, 5, 4, 3, 2, 1):          # trigger with m_left minutes left in the row (incl. itself)
        mask = torch.zeros(ctx.shape, dtype=torch.float64)
        mask[:, T - m_left] = 1.0
        res[f"minutes_left_{m_left}"] = round(float(ctx.call([mask, ramp]).double()[0, T - m_left]), 4)
    return res


@probe("comparison_semantics",
       question="比较算子遇到 NaN、相等时给什么?输出是什么类型?(决定掩码的第一分钟和无成交行)",
       applies=lambda s: s.compute_axis is None and s.face == "shared")
def _cmp(ctx: ProbeContext):
    if ctx.arity != 2:
        return None
    a = torch.tensor([[1.0, 2.0, float("nan"), 3.0, 0.0]], dtype=torch.float64)
    b = torch.tensor([[2.0, 1.0, 1.0, float("nan"), 0.0]], dtype=torch.float64)
    out = ctx.call([a, b])
    vals = out.double().flatten().tolist()
    if not set(v for v in vals if v == v) <= {0.0, 1.0}:
        return None                                   # not a comparison (add/sub/…)
    return {"lt": vals[0], "gt": vals[1], "nan_left": vals[2], "nan_right": vals[3], "equal": vals[4]}
