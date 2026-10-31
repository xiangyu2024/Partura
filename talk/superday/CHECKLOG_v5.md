# principles_v5.pdf check record

Build: `latexmk -xelatex principles_v5.tex` in `talk/superday/`. Output: `principles_v5.pdf`, 20 pages, 959.98 × 540 pt (13.333 × 7.5 in). Renders: `pages_v5/p-01.png` … `p-20.png` (`pdftoppm -r 60 -png`). Pages 10 and 18 were re-viewed after their last text edit; the other 18 pages were viewed in the build before, and their source did not change afterwards.

Files created: `principles_v5.tex`, `figs_v5/` (copy of `figs_v4/`, with new `flow.tex` and `outflow.tex`, and `selection.tex` made compact), `principles_v5.pdf`, `pages_v5/*.png`, this file, and the LaTeX by-products (`principles_v5.aux .fdb_latexmk .fls .log .nav .out .snm .toc .xdv`). `principles_v5.tex` was assembled from `principles_v4.tex` by a script kept in the session scratchpad (`/private/tmp/claude-501/-Users-wxy-Desktop-AlphaCube/84cd2fa5-62ee-4d6f-b035-b604567ee88d/scratchpad/assemble.py`): the preamble and the principles frames 3–9 are copied from v4 byte for byte except the figure path (`figs_v4/` → `figs_v5/`) and the two header comment lines; all other frames are new text in that scratchpad. No existing file was modified: nothing was written to any `*_v4*`, `*_v3*`, `CHECKLOG_v*`, `OUTLINE.md`, `figs_v4/` or `pages_v4/` (their mtimes are 2026-10-31 14:02–14:14 or earlier). No git operations, no servers.

---

## 1. Build and layout checks

- **Build**: `latexmk -xelatex` exit 0. `principles_v5.log`: 0 Overfull, 0 Underfull, 0 Missing character, 0 LaTeX warnings.
- **Page count**: 20, within the limit of 26.
- **CJK**: `pdftotext` on the final PDF finds 0 CJK characters. All slide text is English.
- **Fonts**: Fira Sans (Book, Medium, BookItalic), Fira Math, Fira Mono, all embedded.
- **Layout fixes made on the way** (no content change): the flow figure's file labels were too wide for 16 pt mono in a 2.6 in column (two-line labels for the two-file stages); the flow boxes and the C05 selection chart were shortened; text was trimmed on pages 10–13, 15–18 and 20 until no body text ran into the footline.
- **Visual check**: all 20 pages viewed at 60 dpi (see the note under Build). No overflow, overlap or clipping seen.

## 2. Page list (20)

| page | title | status vs v4 | main sources |
|---|---|---|---|
| 1 | Partura: an LLM research team that steers a symbolic alpha miner | subtitle now "Principles, the prototype flow, results C01–C07 (C08 running), limitations"; date 2026-10-31 | brief; research/coldstart\_C08/STATUS.md |
| 2 | Outline | rewritten: 4 items, pages 3–9 · 10–13 · 14–18 · 19–20 | this deck's structure |
| 3–9 | v4 3–9 | unchanged (figure paths to `figs_v5/`) | CHECKLOG\_v4 §2 (from v3 CHECKLOG §3) |
| 10 | Prototype: input → agent decision → audit → output | new (replaces v4 10–15, first of four) | workflows/c06\_round.js; scripts/server/c06\_conductor.sh; scripts/c06\_sync.sh; scripts/c06\_final.py; file names as in research/coldstart\_C06/partura/s806/r1/ |
| 11 | Input and decision: a real example | new: one locate row from v4 11, PI slots from v4 12 | loc.md; missions.yaml; missions\_final.yaml |
| 12 | Audit: a real example | new: correlation rows from v4 13, auditor finding and counts from v4 14 | corr\_1.md; audit\_1.yaml; audit\_record.json |
| 13 | Output: what runs and how it is judged | new, from v4 15 | final.json; audit\_record.json; scripts/c06\_final.py |
| 14 | Verdict rule, fixed before any run | v4 17, plus two sentences (what A is; no run repeated); lead shortened | C05 RESULT header, §2, §5; C06 RESULT §3; scripts/c06\_final.py header |
| 15 | Eight experiments, one table | v4 20 + C08 row; footnote gives C08 status; v4 19 "why" line not added (no room) | RESULT §1–§2 of C01–C07; research/coldstart\_C08/STATUS.md |
| 16 | C05: better in selection, not out of sample | merges v4 21 and 22; selection chart compacted (values unchanged) | C05 RESULT §1, §2, §4 |
| 17 | C06: the auditor's rejects did better | v4 29, plus the C06 verdict line (v4 27) and the selection numbers (v4 28) | C06 RESULT §1, §2, §4, §5 |
| 18 | C07: fixed yardstick, LLM as verifier | v4 31 and 32 merged; kept/dropped table; one hypothesis line | C07 RESULT header, §1–§4; C07 PLAN revision 1 |
| 19 | Known limitations | v4 33; "read six times" corrected to seven; C08 development-set bullet added | C07 RESULT header; research/coldstart\_C08/PLAN.md §3 |
| 20 | What the evidence supports so far | v4 34; C08 running; one cost line (v4 25) | C05 RESULT §2; C06 RESULT §6; C04 RESULT; C07 RESULT §1, §4 |

**v4 pages not carried (and where their content went)**: 16 "Measuring the system" matrix (folded into the arm sentence on page 14; figure dropped); 18 "Integrity" table (folded into the "no run repeated" sentence on page 14; table dropped); 19 design-evolution table (dropped); 21 + 22 (merged into 16); 23 "Added heads were weaker out of sample" (dropped; not on the keep list); 24 "Why? Hypotheses" (dropped; the C07 hypothesis line on page 18 is the only hypothesis line); 25 cost detail (one line on page 20); 26 C06 design flow (dropped; `figs_v5/cflow.tex` kept as an unused copy); 27 C06 headline (its verdict line now on page 17); 28 C06 three-arm selection chart (dropped; its numbers are on page 17); 29 kept as page 17; 30 "Why: yardstick" (its auto-strike fact is on page 17, its hypothesis folded into page 18); 31 + 32 (merged into 18); 33 → 19; 34 → 20; 35 backup per-seed page (dropped).

---

## 3. Number and claim sources

Paths are under `research/coldstart_C0x/` unless stated. "Verified" means I re-read the value in the file for this version; "carried" means the value is on v4 and its source is in CHECKLOG_v4 (and v3 where noted).

### Page 1–2

| page | claim | source | note |
|---|---|---|---|
| 1 | subtitle: results C01–C07, C08 running | C07 RESULT header; coldstart_C08/STATUS.md (2026-10-31) | — |
| 1 | date 2026-10-31 | brief | unchanged |
| 2 | page ranges 3–9, 10–13, 14–18, 19–20 | this deck (§2 above) | — |

### Page 3–9

Unchanged from v4. Their numbers (e.g. 5,207 stocks, 241 minutes, 8 fields; budget 192, population 48; 2018-01-02 to 2023-08-07; 15 bp per side) are carried from v4 3–9; sources in CHECKLOG_v3 §2–§3 (via CHECKLOG_v4 §3 "Unchanged pages").

### Page 10 (prototype flow)

| page | claim | source | note |
|---|---|---|---|
| 10 | one command per round: `workflows/c06_round.js` (laptop, all seeds) | workflows/c06\_round.js, `args.round`, `args.seeds` (per v4 CHECKLOG §3 p10) | carried |
| 10 | `scripts/server/c06_conductor.sh` on the GPU server, one seed, rounds 1–3 | scripts/server/c06\_conductor.sh header and `for k in 1 2 3` (verified) | the conductor runs one seed's rounds, so "one command per round" applies to the workflow; the text says "once per seed" for the conductor |
| 10 | stages write loc.md → missions.yaml → corr_1.md + audit_1.yaml → missions_final.yaml + evidence.json | file names: research/coldstart\_C06/partura/s806/r1/ (loc.md, missions.yaml, corr\_1.md, audit\_1.yaml, missions\_final.yaml); evidence.json one per episode: scripts/c05\_round.py (v4 CHECKLOG §3 p10) | evidence.json is in episodes/, not in s806/r1/ |
| 10 | "send back for rewrite" | workflows/c06\_round.js (audit fails → PI rewrites, at most 3 audits); C06 RESULT §4 ("每轮审计 1–3 次") | the arrow is a schematic of that rule |
| 10 | PI and auditor: Opus 5.5 | workflows/c06\_round.js, `M.pi` and `M.audit` (per v4 CHECKLOG §3 p10) | carried |
| 10 | fused book read once, after all rounds | scripts/c06\_final.py header ("the one out-of-sample read … after every seed's rounds have ended") | carried |
| 10 | every step leaves a file; a restart resumes at the first missing one | scripts/c06\_sync.sh; conductor skips rounds with a DONE file (v4 CHECKLOG §3 p10) | carried |
| 10 | GP jobs run with no LLM | design statement (v4 CHECKLOG §3 p10: the GP run is `scripts/c05_round.py mission`) | carried |
| 10 | example: seed 806, round 1, arm C | research/coldstart\_C06/partura/s806/r1/ | — |

### Page 11 (input and decision)

| page | claim | source | note |
|---|---|---|---|
| 11 | heads table has 0 rows; top commonality row shown | loc.md, `## heads(0 个)` (verified) | carried (v4 CHECKLOG §3 p11) |
| 11 | +0.80, 0.000, 18, −0.67 / −1.47, `add(LimitWidth, day_cov(Vwap, Ret))` | loc.md commonality row 1 (verified: `\| +0.80 \| 0.000 \| 18 \| -0.67 / -1.47 \|`) | carried; "Mean diff." = score with minus without (derived: −0.67 − (−1.47) = 0.80) |
| 11 | score = worse of train and valid residual long-only Sharpe; 0.5 or more is a discovery | loc.md first paragraph | carried |
| 11 | PI (Opus 5.5) writes one E slot that keeps a core, one N slot that is a new idea | missions.yaml; workflows/c06\_round.js, `M.pi` (verified: `- type: E`, `core: 'day_cov(Vwap, Ret)'`) | carried |
| 11 | E: day_cov(Vwap, Ret), kept; 14 → 5 | missions.yaml E slot (14 seeds); missions\_final.yaml E slot (5); audit_record.json slot a `seeds` 14, `kept` 5 | carried (v4 CHECKLOG §3 p12, p14) |
| 11 | N: intraday skewness; 15 → 12 | missions.yaml N slot (15); missions\_final.yaml N slot (12); audit_record.json slot b | carried |
| 11 | E and N hypotheses, translated | missions.yaml hypothesis fields (translated and shortened) | carried; translation flagged on the page |

### Page 12 (audit)

| page | claim | source | note |
|---|---|---|---|
| 12 | \|ρ\| with liquidity: seed 1 0.35; seed 3 0.52; seed 5 0.63; seed 4 0.73 | corr\_1.md, slot a rows (verified: seed 1 `0.35`, seed 3 `0.52`, seed 4 `0.73`, seed 5 `0.63`) | carried (v4 CHECKLOG §3 p13) |
| 12 | windows and "divided by" per seed | corr\_1.md expression strings (verified: seed 1 `div(day_cov…, mul(day_mean(Vwap), day_var(Ret)))`; seed 3 `cross_mean(…, 5)`; seed 4 `cross_mean(…, 20)`; seed 5 `cross_decay_linear(…, 10)`) | carried |
| 12 | outcomes: seed 1 kept; seeds 3, 4, 5 struck | audit_1.yaml slot a `struck_seeds` [3, 4, 5, 7, 9, 10, 12, 13, 14] (verified); seed 1 in `seeds_kept` | carried |
| 12 | "as the averaging window grows, four E seeds track liquidity more closely" | auditor's reading in audit_1.yaml slot a (v4 CHECKLOG §5 item 9) | labelled as the auditor's reading in the footnote |
| 12 | rule: \|ρ\| ≥ 0.5 with a control = the control written another way | corr\_1.md header line | carried |
| 12 | slot E: 14 in, 5 kept; 9 struck, four also fail \|ρ\| ≥ 0.5 | audit_record.json slot a (`seeds` 14, `kept` 5); audit_1.yaml slot a `struck_seeds` (9 items) | carried (v4 CHECKLOG §3 p14, §5 item 3) |
| 12 | slot N: 15 in, 12 kept; 3 struck | audit_record.json slot b; audit_1.yaml slot b `struck_seeds` [3, 6, 13] (verified) | carried |
| 12 | "the PI treated Vwap as the bar's closing price" | audit_1.yaml slot a reasons (auditor's finding) | carried (v4 CHECKLOG §3 p14) |
| 12 | Vwap is the average traded price inside each minute bar; θ = position in the bar (0 = previous close, 1 = close) | audit_1.yaml slot a reasons | translated and shortened |
| 12 | PI with θ = 1: day_cov·M/P̄ ≈ Q/2 − Rδ; auditor: ≈ (θ − ½)Q − Rδ | audit_1.yaml slot a reasons (verbatim formula); missions.yaml E hypothesis | carried |
| 12 | a non-linear liquidity trait that linear neutralisation cannot remove | audit_1.yaml slot a reasons; research/coldstart\_C06/rules.md §4 item 3 | carried |

### Page 13 (output)

| page | claim | source | note |
|---|---|---|---|
| 13 | E: novelty 3, soundness 3; seeds kept 5; candidates scored 77; heads found 0 | audit_record.json slot a; research/coldstart\_C06/final.json `missions` (verified: `{"seed": 806, "arm": "C", "round": 1, "slot": "a", "type": "E", "scored": 77, "heads": 0}`) | carried (v4 CHECKLOG §3 p15) |
| 13 | N: novelty 4, soundness 4; kept 12; scored 62; heads 0 | audit_record.json slot b; final.json `missions` slot b (verified: `"scored": 62, "heads": 0`) | carried |
| 13 | No head passed the discovery bar in arm C, seed 806, round 1 | final.json `missions` (heads 0 in both slots) | carried |
| 13 | discovery bar: worse of train and valid residual long-only Sharpe; 0.5 or more | loc.md first paragraph | carried |
| 13 | rounds 2 and 3 of seed 806 list four extra heads: c06s806Cr2a twice, Cr2b, Cr3a | final.json `extra_heads` → `C`, seed 806: c06s806Cr2a\_Ea ×2, c06s806Cr2b\_Nb, c06s806Cr3a\_Ea (verified, 4 entries) | carried (v4 CHECKLOG §3 p15) |
| 13 | these heads are in arm C's library | scripts/c06\_final.py header: L_X = M's heads plus X's extra heads of rounds 1..3 | derived from the header |
| 13 | flow captions: fused book per seed, equal-weight z-rank, read on test against A | v4 page 17 verdict rule (v3 CHECKLOG §2); C06 RESULT §1 (arm A is the plain GP) | carried |
| 13 | arms A and B5 not shown | v4 CHECKLOG §3 p15 | carried |

### Page 14 (verdict rule)

| page | claim | source | note |
|---|---|---|---|
| 14 | verdict table (better / worse / cannot tell; one-sided Wilcoxon, α = 0.05) | v4 page 17; C05 PLAN §3 (via v3 CHECKLOG §2) | carried |
| 14 | valid head: test net excess > 0 and t ≥ 2.0 | C06 RESULT §3 ("测试段有效(年化 > 0 且 t ≥ 2.0)"), verified | carried; source corrected from v4's "C06 RESULT §1" |
| 14 | de-duplication: ρ ≥ 0.7 or ρ ≤ −0.5 to a kept head | scripts/c06\_final.py header (verified: "rho >= 0.7 or <= -0.5 with a head kept") | carried |
| 14 | 8 pairs; equal-weight z-rank fusion | v4 page 17; C06 RESULT header and §1 (8 pairs) | carried |
| 14 | A is plain GP with extra evaluations close to Partura's: 4,371 for A, 4,891 for B | C05 RESULT §2, table row "额外付费评估" (verified: 4,371 / 4,579 / 4,891) | new sentence, from a number in v4 page 25 |
| 14 | test read once per ledger; 318 expressions each (C05) | C05 RESULT header ("测试段读 1 次 … 各 318 个表达式") | the "318" is not on the page; the rule is |
| 14 | no run is repeated because its result looks bad | v4 page 18 ("No run is repeated because its result looks bad") | carried |
| 14 | PLAN committed 2026-10-28 (ET), before any run; 14 dated revisions; none changed a comparison rule | C05 RESULT header ("从 PLAN 提交(2026-10-28 19:50 美东)"; "修订 1–14"); C05 RESULT §5 ("没有改任何比较规则", verified) | carried |
| 14 | forward 2026, B vs. B0, valid heads by arm and mission type reported, not in the verdict | v4 page 17 footnote | carried |

### Page 15 (eight experiments)

| page | claim | source | note |
|---|---|---|---|
| 15 | C01: valid heads A 19, B 13; Partura is worse | C01 RESULT §1 (verified: "A 臂 19 个,B 臂 13 个") | carried |
| 15 | C02: new valid heads A 7, B 2; Partura is worse | C02 RESULT §1 (verified: "A 组 7 个,B 组 2 个") | carried |
| 15 | C03: valid heads A 0, B 0; cannot tell | C03 RESULT §1 (verified) | carried |
| 15 | C04: median B − A −0.17; p(B worse) 0.11; cannot tell | C04 RESULT §1 (verified: "中位差(B − A)= −0.17,p(B 更差) = 0.11") | carried |
| 15 | C05: median B − A +0.08; p(B better) 0.42; cannot tell | C05 RESULT §1 (verified) | carried |
| 15 | C06: median C − A +0.01; p(C better) 0.42; cannot tell | C06 RESULT §1 (verified) | carried |
| 15 | C07: median V − A +0.11; p 0.062; cannot tell (leans V) | C07 RESULT §1 (verified) | carried |
| 15 | 16, 8, 8, 8 seed pairs for C04–C07; C07 five non-zero pairs | v4 CHECKLOG §3 p20 (v3 CHECKLOG for C04–C06; C07 RESULT §1) | carried |
| 15 | C02 counts uncorrelated heads only | v4 page 20 footnote (v3 CHECKLOG) | carried |
| 15 | C08 design: Partura generates missions under the fixed yardstick; permissive auditor | research/coldstart\_C08/PLAN.md §1–§2 (C07 yardstick; 宽松审计员) and STATUS.md | the wording is the brief's |
| 15 | C08 verdict: running; no result yet | research/coldstart\_C08/STATUS.md (2026-10-31: round 3 "正在跑" for 801–807; 808 waiting for its round-3 locate; no RESULT file) | see §5 item 1 |

### Page 16 (C05)

| page | claim | source | note |
|---|---|---|---|
| 16 | primary verdict: cannot tell, as pre-registered | C05 RESULT §1 (verified: "按 PLAN §3:分不出") | carried |
| 16 | selection (valid): A 0.94, B 1.52; B higher in 7 of 8 seeds | C05 RESULT §2 (verified: "B 的库在 valid 上的融合夏普均值 1.52,A 0.94,8 对里 B 高 7 对") | carried (v4 page 22) |
| 16 | test: A 0.44, B 0.44; B higher in 5 of 8 | C05 RESULT §1 (verified: 均值 A +0.44、B +0.44; B 高 5 对) | carried |
| 16 | forward 2026: A 0.87, B 0.29; B lower in 6 of 8 | C05 RESULT §1 (verified: 均值 A +0.87、B +0.29; B 高 2 对、低 6 对) | carried |
| 16 | median B − A: +0.08 (test), −0.39 (forward) | C05 RESULT §1 (verified) | carried |
| 16 | one-sided p (B worse) 0.63 (test), 0.039 (forward); p (B better) 0.42 | C05 RESULT §1 (verified) | carried |
| 16 | seeds where B is higher: 5 of 8 (test), 2 of 8 (forward) | C05 RESULT §1 (verified) | carried |
| 16 | test segment 2023-08-08 to 2025-12-31; forward 2026 is 0.67 years | C05 RESULT §1 (verified) | carried |
| 16 | Partura chose its missions from train and valid output only | C05 RESULT §4 (v4 page 22 footnote) | carried |

### Page 17 (C06)

| page | claim | source | note |
|---|---|---|---|
| 17 | verdict: cannot tell; median C − A +0.01; p(C better) 0.42 | C06 RESULT §1 (verified: 中位差 +0.01, p(C 更好) = 0.42) | carried (v4 page 21) |
| 17 | selection (valid): C 1.62, A 0.94 | C06 RESULT §2 table, valid row (verified: C 1.62; A 0.94) | new on this page (v4 page 28 figure; numbers verified in the RESULT table) |
| 17 | test: C 0.52, A 0.44; "level on test" | C06 RESULT §2 table, 测试段 row (verified: C 0.52; A 0.44); "level" is v4's wording (page 21) | carried |
| 17 | accepted 469 seeds, in-sample −1.13, test mean −0.91, forward −0.83, test above 0 15% | C06 RESULT §4 table (verified) | carried (v4 page 29) |
| 17 | rejected 162 seeds, −0.61, −0.53, −0.73, 34% | C06 RESULT §4 table (verified) | carried |
| 17 | of which struck 138: test −0.59, forward −0.66 | C06 RESULT §4 table (verified) | carried |
| 17 | of which dropped on rewrite 24: test −0.19, forward −1.12 | C06 RESULT §4 table (verified) | carried |
| 17 | seed-round pairs 24; accepted better in 3; p = 0.999 | C06 RESULT §4 (verified) | carried |
| 17 | many rejected seeds struck automatically for \|ρ\| ≥ 0.5 with a control | C06 RESULT §5 item 2 (verified: "与某个控制 \|ρ\| ≥ 0.5 自动划掉") | carried (v4 page 30 source); the hypothesis that goes with it is on page 18 |

### Page 18 (C07)

| page | claim | source | note |
|---|---|---|---|
| 18 | primary verdict: cannot tell | C07 RESULT §1 (verified: "按 PLAN §3:分不出") | carried |
| 18 | median V − A +0.11 (test), +0.25 (forward) | C07 RESULT §1 (verified) | carried |
| 18 | one-sided p (V better) 0.062 (test), 0.031 (forward) | C07 RESULT §1 (verified) | carried |
| 18 | seeds V higher / lower: 4 / 1, 3 tied (test); 5 / 0 (forward) | C07 RESULT §1 (verified) | carried |
| 18 | mean fused book: A −0.52, V_tr −0.09 (test); A −0.22, V_tr +0.14 (forward) | C07 RESULT §1 and §2 table (verified) | carried |
| 18 | of 68 heads, V_tr kept 9; dropped 59 | C07 RESULT §3 (verified: 留下 9, 去掉 59) | carried |
| 18 | kept: test −0.13, forward +0.13; dropped: test +0.40, forward +0.38 | C07 RESULT §3 table (verified) | carried |
| 18 | seed 807 kept none; book 0 against A −0.22 | C07 RESULT §2 text (verified) | carried |
| 18 | seed 808 kept 1 of 37; book +0.07 against A −1.26 | C07 RESULT §2 text and table (verified) | carried |
| 18 | seeds 803–805 keep one candidate each, so V and A are identical | C07 RESULT §1 (verified) | footnote, carried |
| 18 | candidates 68, against about 200 in C05 | C07 RESULT §4.1 (verified) | carried |
| 18 | seventh read of the test segment | C07 RESULT header (verified: "这是测试段的第 7 次读取") | carried |
| 18 | verifier rule v2 written after this read (PLAN revision 1); exploratory; output not reported | C07 PLAN revision 1 (dated 2026-10-31; "在读过 C07 测试段之后写"); v4 CHECKLOG §5 item 4 | carried |
| 18 | hypothesis: non-linear control exposure; equal-weight fusion cancels signal | C07 RESULT §4.1 and §4.3, labelled 推断 (inference) | labelled "Hypothesis, not a test" on the page |

### Page 19 (limitations)

| page | claim | source | note |
|---|---|---|---|
| 19 | test segment read seven times; C01–C06 each read it; C07 is the seventh | C07 RESULT header (verified); C06 RESULT header ("这是测试段的第 6 次读取") | corrected from v4's title "six times" |
| 19 | C08 treats the test segment as a development set; confirmation waits for data after 2026-09-16 | research/coldstart\_C08/PLAN.md §3 (verified: "测试段…是开发集…确认要等 2026-09-16 之后的新数据") | new bullet sentence |
| 19 | eight seed pairs; smallest one-sided p is 1/256; forward 2026 is 0.67 years | v4 page 33 (v4 page 17 for 1/256); 8 pairs = 2⁸ ⇒ 1/256 (derived); 0.67 years: C05 RESULT §1 | carried |
| 19 | round k sees M's first k batches; literature dates spot-checked only | v4 page 33 (v3 CHECKLOG §2) | carried |
| 19 | C05's E reward counted the family in the controls; fixed in C06; convex-transform leak stays until C07 | v4 page 33 (v3 CHECKLOG §2); C06 RESULT §6 (rule fix) | carried |
| 19 | survivorship; no delisted names; T+1 and limit-up names cannot be bought | v4 page 33 (v3 CHECKLOG §2) | carried |

### Page 20 (what the evidence supports)

| page | claim | source | note |
|---|---|---|---|
| 20 | two worse (C01, C02); five cannot tell (C03–C07) | v4 page 34 (v3 CHECKLOG §3 p27); C01–C07 RESULT §1 | carried |
| 20 | C08 is running; no result yet | research/coldstart\_C08/STATUS.md | new (v4 page 34 did not mention C08) |
| 20 | C05: fused test book 0.44 for both A and B | C05 RESULT §1 (verified) | carried |
| 20 | C04 feature (daily return scaled by limit width) came from Partura; 12 of its 14 descendants positive net excess on test | C04 RESULT §4 (verified: "12 / 14 净超额为正"; "14 个是 C2a 种子的后代") and its line on the W2 construction | carried (v4 page 34 item 3) |
| 20 | refinement reversed Partura's sign; family's forward mean 0.04 | C04 RESULT (verified: "写的方向是 −1 … GP 精修后留下的几乎都是 +1"; "前推段均值只有 0.04") | carried; wording shortened from v4 |
| 20 | C06 auditor rejects did better out of sample | C06 RESULT §4 (verified) | carried |
| 20 | C07 first comparison to lean toward the LLM; median +0.11; p 0.062; verifier only removed heads | C07 RESULT §4.5 and §1 (verified) | carried (v4 page 34 item 4) |
| 20 | LLM output tokens: C05 arm B 13.21 M; C06 arm C 16.91 M | C05 RESULT §2 (verified: "输出 1,321 万 token"); C06 RESULT §6 (verified: "输出 1,691 万 token") | carried (v4 page 25, one line here) |
| 20 | M, A and B0 used no LLM tokens | C05 RESULT §2 table, LLM row (verified: 0 / 0 / 0) | carried (v4 page 25) |

---

## 4. Changes beyond the brief

1. **Results block = 7 pages (14–20)**, the cap in the brief. It includes limitations and the evidence page, because v4's pages 16–34 were the range to compress.
2. **v4 page 16 (matrix) and page 18 (integrity)** were not on the keep list and did not fit the 7-page cap. Their key content is folded into page 14 (arm definition; "no run is repeated"). Restoring both as separate pages would make the results block 9 pages and the deck 22 pages (still within 26); say if you want them.
3. **Design-evolution "why" line** (brief: "fold the key why into the table if room"): I tried a 14 pt line under the table on page 15, and it did not fit with the 8-row table, so it is not on the deck. The "why" text per step is in v4 page 19 if needed.
4. **C06 selection numbers** (valid 1.62 vs 0.94, test 0.52 vs 0.44) were added to page 17 from C06 RESULT §2. They are not on the keep list; they carry the C05 "selection, not out of sample" pattern to C06. Drop them if the page should be shorter.
5. **Limitations**: "Test segment read six times" changed to "seven times". v4's title said six while its text said C07 was the seventh read; C07 RESULT's header confirms seven.
6. **Hypothesis lines**: one only, on page 18, labelled "Hypothesis, not a test". v4 page 24 and page 30 hypotheses are not on the deck (the auto-strike fact of v4 page 30 is on page 17 as a fact).
7. **C05 selection chart** compacted: 1 Sharpe = 0.90 in (v4: 2.2 in). Bar heights and labels are the v4 values; the note moved to the page footnote. The chart's group labels (7 of 8; 5 of 8; 6 of 8) are unchanged.
8. **Flow page file labels**: stages 3 and 4 write two files each; they are shown as two-line labels because 16 pt mono does not fit "corr_1.md + audit_1.yaml" or "missions_final.yaml + evidence.json" in one 2.6 in column. Stage 4's label is right-aligned to the text margin.
9. **Locate section name**: loc.md's section for the decomposition is titled 拆解 (decomposition) and shows 0 evaluations in this snapshot. The deck says "ablation", as the brief does.
10. **"One command per round"**: the sentence says the laptop workflow runs all seeds for one round, and the GPU conductor runs one seed's rounds 1–3. The conductor is not one command per round, so the text does not say that.
11. **Outline and subtitle** updated; date kept at 2026-10-31.

---

## 5. Open points (for the user)

1. **C08 status.** v4 inferred "running" from research/coldstart_C08/PLAN.md alone. This version cites coldstart_C08/STATUS.md (dated 2026-10-31), which says rounds 1 and 2 are finalised for all seeds and round 3 is running for 801–807, with 808 waiting for its round-3 locate. No RESULT file exists. Please confirm before presenting.
2. **C08 row wording** ("Partura generates missions under the fixed yardstick; permissive auditor") is the brief's. It matches C08 PLAN §1–§2, which I read, but I did not open rules.md.
3. **Verifier rule v2** is still not reported, as in v4 (CHECKLOG_v4 §5 item 4). The deck says only that it exists and is exploratory.
4. **Matrix and integrity pages** dropped from the deck (see §4 item 2).
5. **Round-1 locate output** is still C05's arm-B file (CHECKLOG_v4 §5 item 2); page 11 states that the heads table is empty and the top row is shown.

## 6. Not sourced

- Nothing on the new or changed pages is unsourced. Items that come from the brief rather than a file: the C08 row's wording (§5 item 2), the page titles, and the word "ablation" (§4 item 9).
- The name "Xiangyu Wang" and "Trexquant Superday · Topic B" on the title page are carried from v4.
