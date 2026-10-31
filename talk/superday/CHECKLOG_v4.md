# principles_v4.pdf check record

Build: `latexmk -xelatex principles_v4.tex` in `talk/superday/`. Output: `principles_v4.pdf`, 35 pages, 959.98 × 540 pt (13.333 × 7.5 in). Renders: `pages_v4/p-01.png` … `p-35.png` (`pdftoppm -r 60 -png`); see §1 for which pages were viewed after their last edit.

Files created: `principles_v4.tex` (copy of `principles_v3.tex`, edited), `figs_v4/` (copy of `figs_v3/` plus one new figure, `figs_v4/trail.tex`), `principles_v4.pdf`, `pages_v4/*.png`, this file, and the LaTeX by-products (`principles_v4.aux .fdb_latexmk .fls .log .nav .out .snm .toc .vrb .xdv`). Every `\fig` path points to `figs_v4/`; no `figs_v3` reference remains in the source. No existing file was modified (checked by mtime: only `*_v4*`, `figs_v4/`, `pages_v4/` changed today). No git operations, no server access.

---

## 1. Build and layout checks

- **Build**: `latexmk -xelatex` exit 0. `principles_v4.log`: 0 Overfull, 0 Underfull, 0 Missing character, 0 errors.
- **Build fixes made on the way** (all layout, no content): table column widths were summed without the inter-column padding, which made three tables overflow the text width (locate page, correlation page, audit page); the PI-plan page needed `[fragile]` for its verbatim excerpt; the frames for the prototype and C07 pages were tightened vertically until the body ends above the footline.
- **CJK**: `pdftotext` on the final PDF finds 0 CJK characters. All slide text is English; Chinese source text is paraphrased and marked as translated.
- **Visual check**: all 35 pages viewed at 60 dpi. The pages edited after the first full view (10, 11, 13, 20, 31, 32) were viewed again after their final edits; pages 12, 14 and 15 were not changed after their view. No overflow, overlap or clipping.
- **Fonts**: as v3 (Fira Sans, Fira Math, Fira Mono), embedded.
- **Page count**: 35, within the limit of 36.

## 2. Page list (35)

| page | title | status vs v3 | main sources |
|---|---|---|---|
| 1 | Partura: an LLM research team that steers a symbolic alpha miner | edited: subtitle now "Principles, one prototype round, results C01–C07, limitations"; date 2026-10-31 | brief; C07 RESULT |
| 2 | Outline | edited: five sections (see §3 row 2) | structure |
| 3–9 | v3 pages 3–9 | unchanged (figure paths to `figs_v4/`) | v3 CHECKLOG §2 |
| 10 | Prototype 1/6: how one round runs | new; figure `figs_v4/trail.tex` | workflows/c06_round.js; scripts/server/c06_conductor.sh; scripts/c06_sync.sh; scripts/c06_final.py |
| 11 | Prototype 2/6: the locate output | new | partura/s806/r1/loc.md, loc.json |
| 12 | Prototype 3/6: the PI's plan | new | partura/s806/r1/missions.yaml, missions_final.yaml |
| 13 | Prototype 4/6: seeds vs. liquidity | new | partura/s806/r1/corr_1.md |
| 14 | Prototype 5/6: Vwap is not a close | new | partura/s806/r1/audit_1.yaml, audit_record.json; rules.md §4 |
| 15 | Prototype 6/6: what the round produced | new | research/coldstart_C06/final.json; audit_record.json |
| 16 | Measuring the system, not a signal | v3 10 | v3 CHECKLOG §2 |
| 17 | Verdict rule, fixed before any run | v3 11 | v3 CHECKLOG §2 |
| 18 | Integrity | v3 12 | v3 CHECKLOG §2 |
| 19 | Design evolution, C01 to C07 | v3 13 (unchanged) | v3 CHECKLOG §2 |
| 20 | Seven comparisons, one table | v3 14, edited: retitled; C07 row; footnote (C07 result) | C07 RESULT §1; PLAN §2–§3 |
| 21 | C05 headline: cannot tell | v3 15 | v3 CHECKLOG §2 |
| 22 | Better in selection, not out of sample | v3 16 | v3 CHECKLOG §2 |
| 23 | Added heads were weaker out of sample | v3 17 | v3 CHECKLOG §2 |
| 24 | Why? Hypotheses, not tests | v3 18 | v3 CHECKLOG §2 |
| 25 | What the LLM arms cost, measured | v3 19 | v3 CHECKLOG §2 |
| 26 | C06: an independent auditor screens missions | v3 20 | v3 CHECKLOG §2 |
| 27 | C06 headline: cannot tell | v3 21 | v3 CHECKLOG §2 |
| 28 | Even better in selection, still not out of sample | v3 22 | v3 CHECKLOG §2 |
| 29 | The auditor's rejects did better | v3 23 | v3 CHECKLOG §2 |
| 30 | Why: the yardstick itself pays for control exposure | v3 24 | v3 CHECKLOG §2 |
| 31 | C07: fixed yardstick, LLM as verifier | new (replaces v3 25 "C07: fix the yardstick … (running)") | C07 RESULT §1–§2, header; C07 PLAN §2–§3; C08 PLAN |
| 32 | What the verifier kept and dropped | new | C07 RESULT §2–§4; C07 PLAN revision 1 |
| 33 | Known limitations | v3 26 (unchanged) | v3 CHECKLOG §2 |
| 34 | What the evidence supports so far | v3 27, edited: item 1 counts; item 4 replaced; C07 added | C07 RESULT §1, §4 |
| 35 | Backup: C05 per-seed numbers | v3 28 (unchanged) | C05 RESULT §2 |

Outline (page 2) ranges: Principles 3–9; Prototype 10–15; Measurement and rules 16–19; Results 20–32; Limitations and conclusion 33–34; backup 35. Checked against the frame order above.

## 3. Number and claim sources (pages 1, 2, 10–15, 20, 31, 32, 34)

Paths are under `research/coldstart_C06/partura/s806/r1/` unless stated. "Verbatim" means the value is copied from the file; "derived" means I computed it from file contents (method given).

### Page 1–2

| page | claim | source | note |
|---|---|---|---|
| 1 | subtitle: principles, one prototype round, results C01–C07, limitations | brief | — |
| 1 | date 2026-10-31 | brief | — |
| 2 | section page ranges | this deck's structure (§2 above) | — |

### Page 10 (Prototype 1/6)

| page | claim | source | note |
|---|---|---|---|
| 10 | one workflow run per round, all seeds (arguments round, seeds) | workflows/c06_round.js, `args.round`, `args.seeds` | — |
| 10 | GPU conductor: one per seed, rounds 1–3 | scripts/server/c06_conductor.sh, `for k in 1 2 3`, header | — |
| 10 | transfers: ready, fetch, push, corr | scripts/c06_sync.sh, header and `CMD` branches | — |
| 10 | round 1: loc.md, analysis.md, lit.md are C05's files, unchanged | `diff` of C06 vs C05 `s806/r1`: loc.md and loc.json identical; analysis.md and lit.md identical | missions.yaml differs (not claimed as copied) |
| 10 | round 1 runs no anatomy or literature step | workflows/c06_round.js: anatomy and literature skipped when `K === 1 && STUDY === 'C06'` | — |
| 10 | every step leaves a file; restart resumes at the first missing file; finished jobs are fetched, not rerun | scripts/c06_sync.sh (corr branch: "a finished job is only fetched"); conductor skips rounds with a DONE file (`[ -e …DONE ] && continue`); workflow resume arguments (resume_audit, start_attempt, revise_after) | — |
| 10 | final read: once, after all rounds | scripts/c06_final.py, header ("the one out-of-sample read … after every seed's rounds have ended") | — |
| 10 | evidence.json: one per episode | scripts/c05_round.py (`EP / f"{tag}_*" / "evidence.json"`) | — |
| 10 | missions_final.yaml: code applies the strikes | scripts/c06_check.py, finalize block (writes `missions_final.yaml`, drops struck seeds and disguised seeds) | — |
| 10 | PI and auditor: Opus 5.5 | workflows/c06_round.js, `M.pi` and `M.audit` = claude-opus-5-5 (non-LEAN) | — |
| 10 | GP missions: no LLM | the GP run is `scripts/c05_round.py mission`; the LLM only writes the plan | design statement |

### Page 11 (Prototype 2/6)

| page | claim | source | note |
|---|---|---|---|
| 11 | heads: 0; the heads table has 0 rows | loc.md, "## heads(0 个)" and empty table; loc.json `heads` = 0 | the brief asked for top-3 heads; none exist, so the top-3 commonality rows are shown |
| 11 | 85 scored candidates | loc.md, commonality section heading ("85 个已评分候选") | — |
| 11 | M's batch 1 only | loc.md, snapshot `c05s806M1_I0_open_search` | — |
| 11 | round 1 reuses C05's arm-B locate file unchanged | loc.md heading "B 组, 第 1 轮"; identical to research/coldstart_C05/partura/s806/r1/loc.md | — |
| 11 | +0.80, 0.000, 18, −0.67 / −1.47, add(LimitWidth, day_cov(Vwap, Ret)) | loc.md, commonality row 1 | verbatim |
| 11 | +0.78, 0.004, 6, −0.58 / −1.35, add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret))) | loc.md, commonality row 2 | verbatim |
| 11 | +0.73, 0.011, 5, −0.61 / −1.34, ts_min(add(LimitWidth, day_cov(Vwap, Ret)), 20) | loc.md, commonality row 3 | verbatim |
| 11 | "Mean diff." = mean score with minus without the subtree | derived: −0.67 − (−1.47) = 0.80; −0.58 − (−1.35) = 0.77 (file shows 0.78, rounding) | method check |
| 11 | seven subtrees in the table | loc.md commonality table, 7 rows | — |
| 11 | score = worse of train and valid residual long-only Sharpe; ≥ 0.5 is a discovery | loc.md, first paragraph | — |
| 11 | every top row wraps day_cov(Vwap, Ret); first three add LimitWidth | loc.md rows 1–3 | — |
| 11 | "a board-level constant" | my English gloss; the PI's text (missions.yaml, E hypothesis) calls it a 0.10 gap between boards | paraphrase, flagged §5 |

### Page 12 (Prototype 3/6)

| page | claim | source | note |
|---|---|---|---|
| 12 | PI (Opus 5.5) writes one E slot and one N slot | missions.yaml, slots; workflows/c06_round.js, `M.pi` | — |
| 12 | E keeps the core; N is a new idea | workflows/c06_round.js, MISSIONS_FORMAT and piPrompt rules (E seeds must contain the core; N is a new idea) | — |
| 12 | E: 14 seeds before audit, 5 after | missions.yaml E slot (14 seeds, parsed with yaml); missions_final.yaml E slot (5) | derived by counting |
| 12 | N: 15 seeds before audit, 12 after | missions.yaml N slot (15); missions_final.yaml N slot (12) | derived by counting |
| 12 | E hypothesis (translated): only the timing term is alpha; a late-moving day gives it back under T+1 | missions.yaml, E hypothesis: the timing term −R·δ, T+1 reasoning | translated and shortened |
| 12 | N hypothesis (translated): lottery-like, attention-driven buying in stocks with skewed minute returns; later returns lower | missions.yaml, N hypothesis (mechanism paragraph) | translated and shortened |
| 12 | excerpt: E core `day_cov(Vwap, Ret)`; kept seeds include `div(day_cov(Vwap, Ret), mul(day_mean(Vwap), day_var(Ret)))` and `cross_zscore(… , 20)` | missions_final.yaml, E seeds; audit_record.json `seeds_kept` (seeds 1 and 6) | excerpt, trimmed |
| 12 | R: [] (no R variants in round 1) | missions.yaml and missions_final.yaml, `R: []` | — |

### Page 13 (Prototype 4/6)

| page | claim | source | note |
|---|---|---|---|
| 13 | seed 1 abs(ρ) with liquidity 0.35 (one day, mean × var) | corr_1.md, slot a seed 1, liq column | verbatim |
| 13 | seed 3: 0.52 (5-day mean, mean × var) | corr_1.md, slot a seed 3 | verbatim |
| 13 | seed 5: 0.63 (10-day linear decay, std × std) | corr_1.md, slot a seed 5 | verbatim |
| 13 | seed 4: 0.73 (20-day mean, std × std) | corr_1.md, slot a seed 4 | verbatim |
| 13 | the four values are the sequence the auditor cited (0.35 → 0.52 → 0.63 → 0.73) | audit_1.yaml, slot a reasons (same four numbers); corr_1.md | verified in the file |
| 13 | seed 2 (std × std, one day): 0.39 | corr_1.md, slot a seed 2 | verbatim |
| 13 | window and normalisation per seed | expressions in corr_1.md (`cross_mean(…, 5)`, `cross_decay_linear(…, 10)`, `cross_mean(…, 20)`, `cross_zscore`) | seeds 1 and 3 use mean × var; seeds 4 and 5 use std × std (footnote) |
| 13 | struck: seeds 3, 4, 5; kept: seed 1 | audit_1.yaml, slot a `struck_seeds` [3,4,5,7,9,10,12,13,14]; audit_record.json `seeds_kept` | — |
| 13 | abs(ρ) ≥ 0.5 with a control = the control written another way | corr_1.md header line | — |
| 13 | abs(ρ) between daily ranks, sign ignored, train sample one day in five | corr_1.md header ("train 每 5 天一天; abs(ρ) 不分方向") | translated |
| 13 | "averaged timing effect should weaken as it is averaged" | auditor's reasoning in audit_1.yaml, slot a | labelled as the auditor's reading |

### Page 14 (Prototype 5/6)

| page | claim | source | note |
|---|---|---|---|
| 14 | slot E: novelty 3, soundness 3 | audit_1.yaml slot a; audit_record.json slot a | verbatim |
| 14 | slot N: novelty 4, soundness 4 | audit_1.yaml slot b; audit_record.json slot b | verbatim |
| 14 | E seeds 14 → 5 kept | audit_record.json slot a (`seeds` 14, `kept` 5) | verbatim |
| 14 | N seeds 15 → 12 kept | audit_record.json slot b (`seeds` 15, `kept` 12) | verbatim |
| 14 | E struck 9; four of them also fail abs(ρ) ≥ 0.5 (seeds 3, 4, 5, 12) | audit_1.yaml slot a `struck_seeds` (9 items); the audit's "struck" note for 3, 4, 5, 12 (table rule); corr_1.md liq values 0.52, 0.73, 0.63, 0.53 | see §5 item 3 on the record fields |
| 14 | N struck 3 (seeds 3, 6, 13) | audit_1.yaml slot b `struck_seeds` [3,6,13] | verbatim |
| 14 | "the PI treated Vwap as the bar's closing price" | audit_1.yaml, slot a reasons (the auditor's finding) | auditor's reading |
| 14 | Vwap is the average traded price inside each minute bar, not its close; θ is its position in the bar (0 = previous close, 1 = close) | audit_1.yaml, slot a reasons | translated, shortened |
| 14 | PI with θ = 1: day_cov · M/P̄ ≈ Q/2 − Rδ | audit_1.yaml (the PI's expansion holds only at θ = 1); missions.yaml E hypothesis (`day_cov ≈ (P̄/M)(Q/2 − R·δ)`) | the formula is the file's |
| 14 | auditor: ≈ (θ − ½)Q − Rδ | audit_1.yaml, slot a reasons ("day_cov(Vwap,Ret)·M/P̄ ≈ (θ−½)·Q − R·δ") | verbatim formula |
| 14 | θ near ½ for active names, near 1 for thin single-trade names | audit_1.yaml, slot a reasons | translated |
| 14 | (θ − ½) is a non-linear liquidity trait; linear neutralisation cannot remove it; rule §4, trap 3 | audit_1.yaml, slot a reasons; research/coldstart_C06/rules.md §4 item 3 ("非线性重写" of size, volatility and liquidity; linear neutralisation removes only the linear part) | rules §4 checked directly |
| 14 | M = 241 bars; Q realised variance; R day return; δ path offset | missions.yaml, E hypothesis ("M = 241"; Q, R, δ definitions) | — |

### Page 15 (Prototype 6/6)

| page | claim | source | note |
|---|---|---|---|
| 15 | no head passed the discovery bar in round 1 of arm C, seed 806 | final.json, `missions` (seed 806, arm C, round 1): heads 0 in slot a and slot b; `extra_heads` has no entry with a mission starting c06s806Cr1 (grep: 0 matches) | — |
| 15 | candidates scored: E 77, N 62 | final.json `missions`, arm C, round 1: slot a `scored` 77; slot b `scored` 62 | `scored` is the field name in the file |
| 15 | heads found: E 0, N 0 | final.json `missions`, arm C, round 1: `heads` 0 | — |
| 15 | seeds kept: E 5, N 12 | audit_record.json | — |
| 15 | audit novelty / soundness: E 3 / 3, N 4 / 4 | audit_record.json | — |
| 15 | discovery bar: worse of train and valid residual long-only Sharpe; 0.5 or more | loc.md, first paragraph | — |
| 15 | the round adds no head to arm C's library | scripts/c06_final.py header: library = M's heads plus each arm's extra heads of rounds 1..3; none for round 1 | derived |
| 15 | per-candidate scores are in episodes/, not held locally | `ls episodes` shows no c06s806 or Cr1 entries | checked |
| 15 | not shown: arms A and B5; rounds 2 and 3 of seed 806 list four extra heads (c06s806Cr2a ×2, Cr2b, Cr3a) | final.json `extra_heads`, arm C, seed 806 (4 entries) | arm A: heads 3 and 1; B5: heads 0 and 1 (final.json `missions`, round 1) |

### Page 20 (Seven comparisons; row C07 and footnote)

| page | claim | source | note |
|---|---|---|---|
| 20 | C07 design: fixed yardstick; LLM only verifies GP heads; 8 seeds | C07 PLAN §1–§2 (rank first, smooth, non-linear neutralisation; LLM only keeps or drops); seeds 801–808 (PLAN §2.2) | — |
| 20 | C07 verdict: cannot tell (leans V) | C07 RESULT §1 ("按 PLAN §3:分不出", i.e. cannot tell); "leans V" is the brief's label, consistent with RESULT §4.5 | — |
| 20 | median V − A +0.11; p 0.062 | C07 RESULT §1 | verbatim |
| 20 | seven comparisons; C07 row added | this deck | — |
| 20 | C04–C07 use the per-seed fused-book test Sharpe as primary; 16, 8, 8, 8 seed pairs | v3 CHECKLOG (C04 16, C05 8, C06 8); C07 RESULT §1 (8 pairs) | — |
| 20 | C07 has five non-zero pairs | C07 RESULT §1 (803–805 zero; 801, 802, 806, 807, 808 non-zero) | derived from the RESULT §2 table |
| 20 | C01, C02 valid heads (net excess > 0, t ≥ 2); C02 counts only uncorrelated heads | carried from v3 page 14 footnote (C01/C02 RESULT §1) | wording shortened |

### Page 31 (C07 result, design and verdict)

| page | claim | source | note |
|---|---|---|---|
| 31 | rank, then smooth, then non-linear neutralisation on the five controls | C07 PLAN §2.1 | — |
| 31 | M and A rerun with no LLM | C07 PLAN §2.2 | — |
| 31 | Opus 5.5 keeps or drops each GP head; V_tr sees train only | C07 PLAN §2.3 | — |
| 31 | primary: V_tr against A, 8 pairs, one-sided, as C05 | C07 PLAN §3 | — |
| 31 | verdict: cannot tell, as pre-registered | C07 RESULT §1 ("按 PLAN §3:分不出") | — |
| 31 | median difference, V − A: +0.11 (test), +0.25 (forward) | C07 RESULT §1 | verbatim |
| 31 | one-sided p (V better): 0.062 (test), 0.031 (forward) | C07 RESULT §1 | verbatim |
| 31 | seeds: V higher 4, lower 1, 3 tied (test); forward 5 / 0 | C07 RESULT §1 | verbatim |
| 31 | mean fused-book Sharpe: A −0.52, V_tr −0.09 (test); A −0.22, V_tr +0.14 (forward) | C07 RESULT §1 and §2 table | verbatim |
| 31 | five of eight pairs differ; seeds 803–805 keep one candidate each, so V and A are identical | C07 RESULT §1 | verbatim |
| 31 | 68 candidates under the new yardstick; about 200 in C05 | C07 RESULT §4.1 ("候选从 C05 的约 200 个降到 68 个") | verbatim |
| 31 | seventh read of the test segment | C07 RESULT header ("这是测试段的第 7 次读取") | — |
| 31 | "C08 (Partura generating ideas under the fixed yardstick) is running" | research/coldstart_C08/PLAN.md (title; "written 2026-10-31, before any run"); the C08 partura/s80x directories are dated 2026-10-31 12:52–13:56; no RESULT file | inferred from local files; see §5 item 5 |

### Page 32 (What the verifier kept and dropped)

| page | claim | source | note |
|---|---|---|---|
| 32 | of 68 heads, V_tr kept 9 | C07 RESULT §3 (留下 9, 去掉 59; total 68) | — |
| 32 | kept 9: test mean −0.13, forward +0.13 | C07 RESULT §3 table | verbatim |
| 32 | dropped 59: test mean +0.40, forward +0.38 | C07 RESULT §3 table | verbatim |
| 32 | seed 807: none kept; book 0 against A −0.22 | C07 RESULT §2 text ("V_tr 在 807 一个都没留 … 书按 0 计, A 是 −0.22") | verbatim values |
| 32 | seed 808: 1 of 37 kept; book +0.07 against A −1.26 | C07 RESULT §2 text (37 candidates, 1 kept) and table (V_tr +0.07, A −1.26) | verbatim values |
| 32 | "the kept ones did worse" (single heads) | C07 RESULT §3 (−0.13 kept vs +0.40 dropped) | — |
| 32 | hypothesis 1: equal-weight fusion cancels signals and leaves a shared exposure | C07 RESULT §4.3, labelled "推断" (inference) | labelled as hypothesis, not tested |
| 32 | hypothesis 2: much of what C01–C06 kept was non-linear control exposure | C07 RESULT §4.1, labelled "推断" | labelled as hypothesis, not tested |
| 32 | a verifier rule v2 was written after this test read; exploratory; output not reported | C07 PLAN, revision 1 (dated 2026-10-31; "在读过 C07 测试段之后写") | see §5 item 4 |

### Page 34 (What the evidence supports so far)

| page | claim | source | note |
|---|---|---|---|
| 34 | two worse (C01, C02); five cannot tell (C03–C07) | v3 page 27 (C01, C02 worse; C03–C06 cannot tell); C07 RESULT §1 (cannot tell) | — |
| 34 | the fused test book was 0.44 for both (C05) | carried from v3 (C05 RESULT §1–§2) | unchanged |
| 34 | item 3 (C04 feature; 12 of 14 descendants; forward mean 0.04) | carried from v3 (unchanged) | unchanged |
| 34 | C06's auditor rejects did better out of sample | carried from v3 page 27 item 4 (C06 RESULT §4) | unchanged claim |
| 34 | C07 is the first comparison to lean toward the LLM (median +0.11, p 0.062) | C07 RESULT §4.5 ("第一次在主指标上方向一致地偏向 LLM 一侧"); §1 | the brief said "the only one"; see §4 item 1 |
| 34 | its verifier only removed heads | C07 PLAN §2.3 (keep or drop only); RESULT §4.2 ("主要来自大量去掉 head") | — |

### Unchanged pages

Pages 3–9, 16–19, 21–30, 33 and 35 carry their sources from `CHECKLOG_v3.md` §3 (v3 page numbers are 10–13 → 16–19; 15–24 → 21–30; 26 → 33; 28 → 35). Page 19 (design evolution) keeps the v3 C07 row; its sources line still reads "RESULT §1 or §4 (C01–C06)", which is still accurate.

## 4. Changes beyond the brief

1. **"the only one leaning toward the LLM" became "the first comparison to lean toward the LLM."** C07 RESULT §4.5 says C07 is the first time the primary metric leans toward the LLM, in a consistent direction. The deck's own page 20 shows positive medians for C05 (+0.08) and C06 (+0.01), so "only" would contradict it. The "it only removed things" point is kept, as RESULT §4.2 and the design support it.
2. **C07 forward figures** (median +0.25, wins 5 / losses 0, p 0.031) are included from RESULT §1, as the brief's forward numbers.
3. **Caveat on page 32** that a verifier rule v2 was written after the test read (C07 PLAN revision 1). It was not in the brief, but the dropped-heads result is the post-hoc finding that revision responds to, so the caveat is needed.
4. **Outline** restructured into five sections (Principles, Prototype, Measurement and rules, Results, Limitations and conclusion) so the new pages sit in the right place.
5. **Section placement**: the prototype follows v3 page 9 ("Who reads what"), as the brief says. v3 page 8 ("Current design") is the last architecture diagram before it.
6. **Locate page**: the brief asked for the top three heads; loc.md has 0 heads, so the top three commonality rows are shown and the page says so.
7. **"One-line hypothesis"** is one sentence; in the table it wraps to two lines.
8. **Round 1 result** is "no head passed the discovery bar", as the brief specifies, because final.json has no `c06s806Cr1` entry.
9. **C08 status line** is on page 31 (the C07 page), as the brief allows.
10. **Title subtitle** no longer says C07 is running.

## 5. Open points and flags (for the user)

1. **Heads table empty.** loc.md has 0 heads (loc.json `heads` = 0). The top three rows of the commonality table are shown instead.
2. **Round 1 locate output is C05's arm-B file**, not a new C06 locate run: loc.md and loc.json are identical to `research/coldstart_C05/partura/s806/r1/`, and loc.md's title says "B 组". analysis.md and lit.md are also identical to C05's, and workflows/c06_round.js skips anatomy and literature in round 1. Stated on pages 10 and 11.
3. **audit_record.json field semantics**: for slot a, `struck_by_auditor` = 9 and `struck_by_table` = 4. Those are not additive: the table strikes are a subset of the auditor's 9 (finalize code removes the auditor's list and also checks the table rule). The slide says "9; four also fail abs(ρ) ≥ 0.5".
4. **C07 verifier rules v2 — output not in RESULT.md.** `research/coldstart_C07/final_dev_verify_v2.json` (file dated 2026-10-30 16:13) has its own `primary` block and a `verdict_primary` field, and `verify_v2/` exists. RESULT.md mentions neither. The deck does not use their numbers and says only that v2's output is not reported. The file's verdict field reads "cannot tell". Whether to report v2 is your decision; it would be exploratory, since it was written after the test read.
5. **C08 "running" is an inference.** research/coldstart_C08/PLAN.md is dated 2026-10-31 and says it was written before any run. The C08 partura/s80x directories are dated 2026-10-31 12:52–13:56, and there is no RESULT file. I did not contact the servers. Please confirm the status before presenting.
6. **Rounds 2 and 3 of seed 806** have extra heads in final.json (c06s806Cr2a ×2, Cr2b, Cr3a; test Sharpe values not shown). They are outside this one-round section, and page 15 says so.
7. **Arm A and arm B5** for the same seed and round are not shown (arm A: heads 3 and 1; B5: 0 and 1, from final.json `missions`).
8. **"Board-level constant"** for LimitWidth (page 11) is my English gloss. The PI's text describes a 0.10 gap between boards.
9. **"Four E seeds track liquidity more closely as the window grows"** (page 13) is the auditor's reading of four rows that mix two normalisations. The footnote says so.
10. **Page 14's Vwap finding** is the auditor's analysis from the code and the correlation table, labelled "not a test".
11. **C07 PLAN revision date**: the revision header says 2026-10-31, while the PLAN.md file is dated 2026-10-30 15:55. Metadata inconsistency only; the deck cites the revision as "revision 1" without a date.
12. **v3 limitation page (33)** still says the convex-transform leak "stays until C07". C07 has now run; the sentence is history and is kept unchanged.

## 6. Not sourced

- Nothing on the new or changed pages is unsourced. The one inferred status (C08 running) is flagged in §5 item 5.
- No numbers were taken from episodes/ or the C08 folder, and none from the C07 verifier output files (§5 item 4).
