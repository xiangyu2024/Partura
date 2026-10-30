# principles_v3.pdf check record

Build: `latexmk -xelatex principles_v3.tex` in `talk/superday/`. Output: `principles_v3.pdf`, 28 pages, 959.98 × 540 pt (13.333 × 7.5 in). Renders: `pages_v3/p-01.png` … `p-28.png` (`pdftoppm -r 60 -png`), every page viewed after the last build.

Files created: `principles_v3.tex` (copy of `principles_v2.tex`, changed as listed below), `figs_v3/` (copy of `figs_v2/` plus one new figure, `figs_v3/selection3.tex`), `principles_v3.pdf`, `pages_v3/*.png`, this file, and the LaTeX by-products (`.aux .log .fls .fdb_latexmk .nav .out .snm .toc .xdv`). v1 and v2 files (`principles.*`, `principles_v2.*`, `figs/`, `figs_v2/`, `pages/`, `pages_v2/`, `CHECKLOG.md`, `CHECKLOG_v2.md`, `OUTLINE.md`, `DOSSIER.md`) are unchanged (mtimes checked against the start of the session). No git operations, no server access.

Preamble: lines 3 to `\begin{document}` are identical to `principles_v2.tex`; only the two header comment lines changed. Figure paths point to `figs_v3/`.

---

## 1. Build and layout checks

- **Build**: `latexmk -xelatex` exit 0. `principles_v3.log`: 0 Overfull, 0 Underfull, 0 Missing character, 0 errors.
- **Fonts**: FiraSans-Book, FiraSans-BookItalic, FiraSans-Medium, FiraMath-Regular, FiraMono-Regular, all embedded. No CJK characters in the PDF text (checked with `pdftotext`).
- **Vertical fit**: four frames first overflowed (pages 13, 14, 19, 21; by 3–46 pt). Fixed by table row stretch (p13 1.20 → 1.00; p14 1.30 → 1.06), smaller gaps before footnotes (p13, p14, p19), and one shorter note (p21). Page 23 table columns widened so the "of which" labels stay on one line.
- **Visual check**: all 28 pages viewed at 60 dpi after the final build. No overflow, overlap or clipping. Titles sit at the same height as in v2.

## 2. Page list (28)

| page | title | status vs v2 | main sources |
|---|---|---|---|
| 1 | Partura: an LLM research team that steers a symbolic alpha miner | edited: date 2026-10-31; subtitle C01–C06 finished, C07 running | brief item 1; DOSSIER §1 |
| 2 | Outline | edited: results C01–C06 (14–24); current experiment C07 (25); limitations 26–27; backup 28 | structure |
| 3 | Search is cheap, belief is expensive | unchanged | — |
| 4 | Tokens should buy beliefs, not candidates | unchanged | — |
| 5 | Task specification | unchanged | — |
| 6 | A finished output is a signal card | unchanged | — |
| 7 | The searcher is a black box with three handles | unchanged (see open point 6) | C05 PLAN §2 |
| 8 | Current design: the main search runs untouched | unchanged | — |
| 9 | Who reads what, and what each may not do | unchanged | — |
| 10 | Measuring the system, not a signal | unchanged | — |
| 11 | Verdict rule, fixed before any run | unchanged (C05 rule; see open point 6) | C05 PLAN §3 |
| 12 | Integrity: what keeps the experiment honest | unchanged | — |
| 13 | Design evolution, C01 to C07 | edited: C07 row added; sources line | brief item 2; C07 PLAN §1–§2 |
| 14 | Six comparisons, one table | edited: retitled; C06 row; footnote (C07 running) | brief item 3; C06 RESULT §1 |
| 15 | C05 headline: cannot tell | unchanged | — |
| 16 | Better in selection, not out of sample | unchanged (two-arm C05 chart) | — |
| 17 | Added heads were weaker out of sample | unchanged | — |
| 18 | Why? Hypotheses, not tests | edited: Goodhart sub-line (C06 kept the leak; C07 ranks first) | C07 PLAN §1, §2.1 |
| 19 | What the LLM arms cost, measured | edited: retitled; C06 arm C rows added | brief item 5; C06 RESULT §6 |
| 20 | C06: an independent auditor screens missions | kept (flow figure); "running" status removed; design note added | brief item 4(a); C06 PLAN §1, §2.4–§2.5 |
| 21 | C06 headline: cannot tell | new (same layout as page 15) | brief item 4(b); C06 RESULT §1 |
| 22 | Even better in selection, still not out of sample | new (three-arm bar chart) | brief item 4(c); C06 RESULT §2 |
| 23 | The auditor's rejects did better | new (calibration table) | brief item 4(d); C06 RESULT §4 |
| 24 | Why: the yardstick itself pays for control exposure | new (labelled as hypothesis) | brief item 4(e); C06 RESULT §5 item 2 |
| 25 | C07: fix the yardstick, LLM only verifies (running) | new (design, status, caveat; no result) | brief item 4(f); C07 PLAN §1–§4 |
| 26 | Known limitations | edited: test read six times; yardstick item corrected | brief item 7 (keep other items true); C06 RESULT header; C07 PLAN §4 |
| 27 | What the evidence supports so far | edited: item 1 counts; item 4 replaced | brief item 6 |
| 28 | Backup: C05 per-seed numbers | unchanged (no C06 per-seed table needed) | C05 RESULT §2 |

## 3. Number-source table (pages changed or added)

Format: page | claim as on slide | source file and section | note. "Unit" = the RESULT figure is written in 万 or 亿 and is converted here, as in v2 page 19.

| page | claim | source | note |
|---|---|---|---|
| 1 | date 2026-10-31 | brief item 1 | — |
| 1 | C01–C06 results; C07 running | DOSSIER §1 table, §3 (C07 状态) | — |
| 2 | pages 14–24; 25; 26–27; backup 28 | this deck's structure | — |
| 13 | C07 row: rank first, then smooth; non-linear neutralisation; LLM only verifies GP output | brief item 2; C07 PLAN §1, §2 | — |
| 13 | C07 reason: rejected seeds did better; yardstick pays for non-linear control exposure | C06 RESULT §4, §5 item 2 | — |
| 14 | C06 design: C05 + independent auditor scores every mission before it runs | brief item 3; C06 PLAN §1, §2.4 | — |
| 14 | C06: median C − A +0.01; p(C better) 0.42; verdict cannot tell | C06 RESULT §1 | — |
| 14 | 16, 8 and 8 seed pairs | C04 RESULT header (16); C05 RESULT §1 (8); C06 RESULT §1 (8) | — |
| 14 | C07 running; no result yet | C07 PLAN header and §6; DOSSIER §3 | — |
| 18 | C06 kept the convex-transform leak; C07 ranks first | C07 PLAN §1 item 1, §2.1 | correction of v2 wording "C06 leaves the reward unchanged" (see §4) |
| 19 | C05 rows unchanged | C05 RESULT §2 | unit conversions: 13.21 M (1,321 万); 630 M (6.30 亿); 47.8 M (4,783 万) |
| 19 | arm C: 222 LLM agent calls, incl. Haiku runners; 38 auditor calls | C06 RESULT §6 ("222 次 agent 调用(含跑命令的 Haiku)"; "审计员 38 次") | — |
| 19 | arm C: LLM output 16.91 M | C06 RESULT §6 ("1,691 万 token") | unit |
| 19 | arm C: cache read 826 M; cache write 58.6 M | C06 RESULT §6 ("读缓存 8.26 亿"; "写缓存 5,860 万") | unit |
| 19 | C06 reran only arm C's locate, R, correlation and mission steps; M, A, B5 reused | C06 RESULT §6 (GPU line) | no C06 GP run time is reported, so none is shown |
| 20 | arm C = Partura with auditor vs A; 8 seeds; same verdict rule as C05; M and A reused, not rerun | C06 PLAN §1, §2.1; C06 RESULT header | — |
| 20 | three fixes against C05 (E reward no family count; R variant as new head; R chain to end) | DOSSIER §3 C06 设计 (三处修正); C06 PLAN §1 | carried from v2 page 21 |
| 20 | flow figure: pass rule, struck thresholds abs(ρ) ≥ 0.7 / 0.5; at most 3 audits; novelty and soundness 1–5 | C06 PLAN §2.4–§2.5 (unchanged figure `figs_v3/cflow.tex`) | — |
| 21 | test: median C − A +0.01; one-sided p (C worse) 0.63; C higher in 4 of 8 seeds | C06 RESULT §1 | — |
| 21 | test: mean fused-book Sharpe A 0.44, C 0.52 | C06 RESULT §1, §2 table | — |
| 21 | test: one-sided p (C better) 0.42 | C06 RESULT §1 | — |
| 21 | forward (report only): median C − A −0.34; p(C worse) 0.13; C higher in 2 of 8 (so lower in 6) | C06 RESULT §1 | "lower in 6" is also in C06 RESULT §1 ("C 低 6 对") |
| 21 | forward: mean A 0.87, C 0.49 | C06 RESULT §1, §2 table | — |
| 21 | forward covers 0.67 years | C06 RESULT §1 | — |
| 22 | valid: A 0.94, B5 1.52, C 1.62 | C06 RESULT §2 table | B5 = C05 Partura, as in C06 RESULT |
| 22 | test: A 0.44, B5 0.44, C 0.52 | C06 RESULT §2 table | — |
| 22 | forward: A 0.87, B5 0.29, C 0.49 | C06 RESULT §2 table | — |
| 22 | valid: C higher than A in 7 of 8 seeds | C06 RESULT §2 table ("高于 A:7 / 8") | — |
| 22 | test: C higher than A in 4 of 8 seeds | C06 RESULT §2 table ("高于 A:4 / 8") | — |
| 22 | forward: C lower than A in 6 of 8 seeds | C06 RESULT §1 (前推段 "C 低 6 对") | — |
| 22 | train: A 1.44, C 1.95; C higher in 8 of 8 | C06 RESULT §2 table | train not charted |
| 22 | train and valid output only for locate tool and auditor | C06 RESULT §7 (审计员看得到 valid); C05 PLAN §2.4 (locate reads train and valid) | — |
| 23 | accepted 469: in-sample −1.13, test mean −0.91, forward −0.83, test > 0 15% | C06 RESULT §4 calibration table | — |
| 23 | rejected 162: in-sample −0.61, test mean −0.53, forward −0.73, test > 0 34% | C06 RESULT §4 calibration table | — |
| 23 | of which struck automatically 138: test −0.59, forward −0.66 | C06 RESULT §4 calibration table | added beyond brief; same table |
| 23 | of which dropped on rewrite 24: test −0.19, forward −1.12 | C06 RESULT §4 calibration table | added beyond brief; same table |
| 23 | 24 seed-round pairs; accepted better in 3; one-sided p (accepted better) 0.999 | C06 RESULT §4 | — |
| 23 | caption: seeds are GP starting points; each read as its own factor, direction and half-life chosen on train | C06 RESULT §4 (wording from brief item 4(d) and RESULT §4 note) | — |
| 24 | hypothesis formed after reading the test period, not a test | brief item 4(e); C06 RESULT §5 (推断, "不是检验") | — |
| 24 | many rejected seeds struck for abs(ρ) ≥ 0.5 with a control | C06 RESULT §5 item 2; C06 PLAN §2.5 | "many" paraphrases 相当一部分; no count given |
| 24 | non-linear rewrites of controls earn in the linearly neutralised residual book, in and out of sample | C06 RESULT §5 item 2 | inference, labelled |
| 25 | started 2026-10-30 on two servers | DOSSIER §3 (C07 状态); C07 PLAN header date | not a RESULT |
| 25 | rank first then EMA; monotone and convex rewrites become one signal | C07 PLAN §2.1 | — |
| 25 | non-linear neutralisation on 5 control ranks, squares and cubes; 16 columns | C07 PLAN §2.1 ([1, z(c), z(c)², z(c)³]) | — |
| 25 | M and A rerun with no LLM; seeds 801–808 | C07 PLAN §2.2 | — |
| 25 | Opus 5.5 verifier; V_tr train only; V_all train and valid; 16 calls, one per seed and version | C07 PLAN §2.3 | — |
| 25 | primary V_tr against A, 8 pairs, one-sided, same rule as C05 | C07 PLAN §3 | — |
| 25 | seventh read of the test period; clean check is data after 2026-09-16 | brief item 4(f); C07 PLAN §4 | — |
| 26 | test read six times (C01–C06); C07 seventh | C06 RESULT header ("第 6 次读取"); C07 PLAN §4 | — |
| 26 | yardstick unchanged in C06; E reward family fix in C06; convex-transform leak until C07 | C06 RESULT §3 (E 奖励口径修正); C07 PLAN §1 item 1 | correction of v2 "Reward unchanged" |
| 27 | two worse (C01, C02); four cannot tell (C03–C06) | RESULT §1 of C01–C06 | — |
| 27 | gatekeeping did not help either (C06); rejected did better out of sample; C07 tests the yardstick | brief item 6; C06 RESULT §4–§5 | — |

Unchanged pages (3–11, 12, 15–17, 28) carry the v2 sources in `CHECKLOG_v2.md` §3.

## 4. Changes to wording beyond the brief's list

These were needed to keep other items true after C06:

1. **Page 18**: v2 said "C06 leaves the reward unchanged". C06's E reward did change (family no longer counted), and the convex-transform leak stayed. The sub-line now reads "C06 kept the leak; C07 ranks first."
2. **Page 26**: v2 said "Test segment read five times" and "Reward unchanged". Now six reads (C01–C06), with C07 the seventh, and "Yardstick unchanged in C06", with the family fix noted.
3. **Page 19** title changed from "What C05 cost" to "What the LLM arms cost", because the table now covers arms B and C.
4. **Page 22** legend and caption name the three arms: A plain GP, B5 C05 Partura, C C06 Partura with auditor.

## 5. Open points (what could not be sourced cleanly, or needs a decision)

1. **Unit conversions** (page 19): 13.21 M, 630 M, 47.8 M (C05) and 16.91 M, 826 M, 58.6 M (C06) are converted from 万 and 亿 in the RESULT files, as in v2. Raw strings are in C05 RESULT §2 and C06 RESULT §6.
2. **Calibration counts** (page 23): 469 accepted and 162 rejected are the RESULT §4 calibration counts, as the brief gives them. C06 RESULT §4 also reports an audit tally of 474 accepted, 147 struck and 34 dropped on rewrite. It also says 631 seeds have a test reading, of which 19 are gate rejects. RESULT does not say whether those 19 sit inside the 469 + 162. The slide does not mention 19 or 631.
3. **Per-seed counts** on page 22 (7 of 8, 4 of 8, 6 of 8) are read from the RESULT §2 table text ("高于 A") and §1. Per-seed valid values are not tabulated in RESULT, so these were not recomputed.
4. **Paraphrase** on page 24: "many rejected seeds" is a reading of RESULT §5 ("相当一部分"). RESULT gives no count.
5. **Added rows** beyond the brief: page 21 forward median −0.34 (RESULT §1); page 23 "of which" rows (RESULT §4 table). Both are sourced. Remove if the brief should match exactly.
6. **Principles pages 7 and 11** still describe the C05/C06 yardstick (reward `long_neutral`, five controls, 15 bp; C05 verdict rule). C07 changes the reward transform and the neutralisation, and page 25 says so, but pages 7 and 11 were not edited because the brief listed the changes. The speaker should say that the principles pages describe C05–C06.
7. **C06 GP run time** is not reported (C06 reused M, A and B5), so the cost table has no C06 GP row.
8. **Dates**: deck date 2026-10-31 as the brief says; "started 2026-10-30 on two servers" (page 25) is from DOSSIER §3 and C07 PLAN, because C07 has no RESULT yet.
9. **C06 ledger** (357 expressions each, C06 RESULT header) is not on any slide. Page 12 still gives C05's 318. Not changed.
10. **Page 14 and 13 tables** are set tighter than v2 (row stretch 1.00 and 1.06 against 1.20 and 1.30) to fit one added row each. Visual check passed; if the speaker wants more air, drop one row's detail rather than the stretch.

## 复核修正(主会话)

- 第 23 页「of which struck automatically, 138」改为「of which struck by the auditor or the table, 138」:RESULT 的「划掉」包括审计员划掉与相关度表自动划掉两种。
- 469 + 162 = 631,正是有测试段读数的种子;19 个门槛废品不在其中,所以页上的计数是对的。
