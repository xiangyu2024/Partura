# principles_v2.pdf check record

Build: `latexmk -xelatex principles_v2.tex` in `talk/superday/`. Output: `principles_v2.pdf`, 24 pages, 959.98 × 540 pt (13.333 × 7.5 in). Renders: `pages_v2/p-01.png` … `p-24.png` (`pdftoppm -r 60 -png`), every page viewed.

Files touched: `principles_v2.tex`, `figs_v2/*.tex` (8 figures), `principles_v2.pdf` and build by-products (`.aux .log .fls .fdb_latexmk .nav .out .snm .toc .xdv`), `pages_v2/*.png`, this file. v1 files (`principles.tex`, `principles.pdf`, `figs/`, `pages/`, `OUTLINE.md`, `CHECKLOG.md`) are unchanged (mtimes 2026-10-26). No git operations, no server access.

Research read: `research/coldstart_C01`–`C05` RESULT.md and PLAN.md; `research/coldstart_C06/PLAN.md` only. Not read: `research/coldstart_C06/partura/`, `episodes/`, the contents of `coldstart_C06/calib.json` and `rules.md` (directory listing only). No C06 outcome appears anywhere in the deck.

Preamble: lines 3 to `\begin{document}` of `principles_v2.tex` are identical to `principles.tex` (checked with `diff`); only the two header comment lines were changed.

---

## 1. Page list (24)

| page | title | status vs v1 | main sources |
|---|---|---|---|
| 1 | Partura: an LLM research team that steers a symbolic alpha miner | edited (team; date 2026-10-30; subtitle) | brief |
| 2 | Outline | edited (five parts; C01–C05 finished, C06 running) | structure |
| 3 | Search is cheap, belief is expensive | kept; figure relabelled for current roles | C05 PLAN §2 |
| 4 | Tokens should buy beliefs, not candidates | kept; figure without C01 counts | structure, illustrative |
| 5 | Task specification | kept; 5,207 names; residual reward; PI | C01 PLAN §2.1, §2.2; C05 PLAN §2.6 |
| 6 | A finished output is a signal card | kept; filled-by column updated | C05 PLAN §2.5, §3; C06 PLAN §2.5 |
| 7 | The searcher is a black box with three handles | kept; ports now seeds / direct evaluation / accept filter | C05 PLAN §2.1, §2.3, §2.5; C04 RESULT §6 |
| 8 | Current design: the main search runs untouched | new (architecture figure) | C05 PLAN §2.1–2.6; C06 PLAN §2.4–2.5 |
| 9 | Who reads what, and what each may not do | new (replaces v1 agent roles) | C05 PLAN §2.6; C06 PLAN §2.4–2.6 |
| 10 | Measuring the system, not a signal | kept; matrix redrawn for C05 (seeds × rounds × A/B0/B, M row) | C05 PLAN §2.1–2.3 |
| 11 | Verdict rule, fixed before any run | new (replaces v1 C01 decision rules) | C05 PLAN §3, header, revisions |
| 12 | Integrity: what keeps the experiment honest | kept; rows updated to C05/C06 | C05 PLAN, RESULT §5; C06 PLAN §2.4, §2.6 |
| 13 | Design evolution, C01 to C06 | new (one table) | C02–C05 PLAN §1; C01–C04 RESULT |
| 14 | Five comparisons, one table | new | RESULT §1 of C01–C05 |
| 15 | C05 headline: cannot tell | new | C05 RESULT §1 |
| 16 | Better in selection, not out of sample | new (bar figure) | C05 RESULT §1, §2, §4 |
| 17 | Added heads were weaker out of sample | new (table) | C05 RESULT §1–§4b |
| 18 | Why? Hypotheses, not tests | new | C05 RESULT §4b |
| 19 | What C05 cost, measured | new | C05 RESULT §2 |
| 20 | C06: an independent auditor screens missions | new (flow figure) | C06 PLAN §2.4–2.5 |
| 21 | C06 is running; no results yet | new (status, caveat, planned box) | C06 PLAN §1, §4; C05 RESULT §6 |
| 22 | Known limitations | new (replaces v1 limitations) | C05 RESULT §6; C06 PLAN §4; C01 PLAN §4, RESULT §7 |
| 23 | What the evidence supports so far | new (conclusion) | RESULT §1 (C01–C05); C04 RESULT §3 item 3 |
| 24 | Backup: C05 per-seed numbers | new (backup) | C05 RESULT §2 per-seed table |

v1 pages not carried over: agent roles (→ 9), one round of the loop (→ 8), belief → intervention with weights and YAML (C05/C06 use no operator weights), token accounting with tiers and stopping rule (→ 19), implemented vs planned (C01-specific status table), and "Where the full pipeline stands today" (AlphaCube and two_level figures, not part of the five-part outline in the brief).

---

## 2. What changed vs v1

Removed statements: "results: C01 is running"; C01 role names (Coordinator, Lead, Executors); "8 × 192 evals per arm in every round"; C01 per-arm axis counts 1,536 / 3,072 / 4,608 (now "rounds", no numbers); "286 searchable operators" (no source found, see §5); "5,220 names" (replaced, see §5); "POP/4 = 12" seeds (C01 configuration; replaced by the C05 limit of 16); operator weights w(x) and the YAML rule (not used in C05/C06).

Added: current design (M untouched; locate tool; E/R/N missions; roles incl. C06 auditor); C05 verdict rule (one-sided Wilcoxon, 8 pairs, α = 0.05, 1/256); design evolution table; five-experiment table; C05 headline (primary and forward, both reported with their status); selection vs test vs forward; added-heads table; the "why" page labelled as hypotheses formed after reading the test period; measured C05 costs; C06 design and status with the reuse-of-test-data caveat and a dashed "planned, not tested" box (the only dashed item in the deck); limitations; conclusion; backup per-seed table.

Layout changes after the first render: page 7 caption split and S×D×M annotation moved; page 9 roles table shortened (overflowed the footer); page 11 forced breaks removed; page 13 footnote shortened; page 14 cells use `\newline`; page 15 bold removed from values; page 16 group labels hung from the baseline and caption moved; page 18 items shortened (overflowed); page 20 boxes shortened (arrow crossed text); page 21 planned box merged with its label; page 22 limitations cut to five items (overflowed); table column widths reduced by the inter-column padding (about 12 pt per boundary); the `R` column type moved out of the frame (beamer error); dashed box width reduced (0.68 pt overfull).

---

## 3. Number-source table

Format: page | claim as on slide | source file and section | note. "illustrative" = schematic, tagged on the slide.

| page | claim | source file + section | note |
|---|---|---|---|
| 1 | date 2026-10-30 | brief | talk date as instructed |
| 2 | pages 3–12, 13, 14–19, 20–21, 22–23, 24 | this deck's structure | structural |
| 3 | 256 extra evaluations per arm, round and seed | research/coldstart_C05/PLAN.md §2.3 | — |
| 3 | 0 tokens (GP ring) | design | — |
| 3 | token split by role | illustrative | tagged |
| 4 | candidate funnel proportions; step heights | illustrative | tagged |
| 4 | R1, R2, R3 | C05 PLAN §2.2 | — |
| 5 | 5,207 names | research/coldstart_C01/PLAN.md §2.1 ("5207 只 × 241 分钟") | v1 had 5,220; see §5 item 2 |
| 5 | 241 minutes; 8 fields | C01 PLAN §2.1 | — |
| 5 | search sees 2018-01-02 to 2023-08-07 | C01 PLAN §2.1 | — |
| 5 | 15 bp per side | C01 PLAN §2.2 ("扣 15bp 单边") | — |
| 5 | Opus 5.5, Opus 5, Sonnet 5, Haiku 5.5 | C05 PLAN §2.6 | — |
| 5 | r = P(t+2)/P(t+1) − 1; first-15-minute VWAP; t close → t+1 open | partura/propose.py:312 (label `open_vwap15`, horizon 1); partura/panels.py (`label_buyable`) | exact formula carried from v1; not found in research/ or AlphaCube checkout; open point §5.3 |
| 5 | five controls; residuals | C05 PLAN §2 (controls) and §3 (residual on five controls) | — |
| 6 | cross_mean(day_std(Amt), 30), sign −1 | C01 PLAN §2.5 (pool line); C02 PLAN §2.2 | — |
| 6 | thesis example text | illustrative (v1 wording) | tagged; not in research files |
| 7 | reward long_neutral (five controls) | C05 PLAN §2 ("奖励 long_neutral") and §3 | — |
| 7 | 15 bp | C01 PLAN §2.2; C03 PLAN §2 | inherited environment |
| 7 | depth 2–4 | C01 PLAN §2.2; C02 PLAN §2.2 (table); C04 RESULT §6 | open point §5.5 |
| 7 | M budget 192; population 48 | C05 PLAN §2.1 | — |
| 7 | mission runs: population 32; 96 or 128 evaluations | C05 PLAN §2.3 | — |
| 7 | seeds: E core kept; N ≤ 16 seeds | C05 PLAN §2.5 (N: "≤ 16 个种子") | — |
| 7 | direct evaluation: R ≤ 16 variants per round | C05 PLAN §2.3 ("R 直接评估 ≤ 16 次") | — |
| 7 | accept filter: |ρ| ≥ 0.7 or same skeleton | C05 PLAN §2.1 (i) and (ii) | — |
| 7 | tree example and windows 20, 30 | illustrative (v1 example; 30 = family window in C01 PLAN §2.5) | tagged; parse check from v1 not re-run |
| 8 | 4 batches per seed; M bans its own heads and skeletons | C05 PLAN §2.1 | — |
| 8 | locate tool reads train and valid only | C05 PLAN §2.4 | — |
| 8 | E, R, N missions; auditor C06 only | C05 PLAN §2.5; C06 PLAN §2.4–2.5 | — |
| 8 | layout (M, locate, Partura, library) | illustrative | tagged |
| 9 | roles and models | C05 PLAN §2.6; C06 PLAN §2.4–2.5 | — |
| 9 | librarian: papers before 2023-08-08 | C05 PLAN §2.6 | spot-check only (limitations) |
| 9 | Partura reads only own seed's output; never other seeds, arms, test numbers | C05 PLAN §2.6 | — |
| 9 | auditor does not read PI notes | C06 PLAN §2.5 | — |
| 10 | seeds 801–808; M e = 1–4; 192 per batch | C05 PLAN §2.1 | — |
| 10 | 256 extra evaluations per arm, round, seed | C05 PLAN §2.3 | — |
| 10 | round k sees M's batches 1 to k | C05 PLAN §2.2 | — |
| 10 | train 2018-01-02 to 2021-12-31; valid 2022-01-01 to 2023-08-07; test 2023-08-08 to 2025-12-31 | C05 PLAN §2 with C01 PLAN §2.1 | — |
| 10 | forward 2026-01-05 to 2026-09-16 | C01 PLAN §2.1 (start 20260105); end: C06 PLAN §4; v1 cites two_level/RESULT.md | C05 RESULT writes start as 2026-01-01; open point §5.4 |
| 11 | one-sided Wilcoxon signed-rank; 8 pairs; α = 0.05 | C05 PLAN §3 | — |
| 11 | smallest one-sided p = 1/256 | C05 PLAN §3 | — |
| 11 | valid head: net excess > 0 and t ≥ 2.0 | C05 PLAN §3 | — |
| 11 | de-dup: drop if ρ ≥ 0.7 or ρ ≤ −0.5 | C05 PLAN §3 | — |
| 11 | PLAN committed 2026-10-28 (ET) | C05 PLAN header ("写于 2026-10-28 19:50(美东)") | — |
| 11 | 14 dated revisions; none changed a comparison rule | C05 PLAN 修订 1–14; C05 RESULT §5 | — |
| 12 | 318 expressions each (test and forward) | C05 RESULT header (ledger paragraph; ledger_c05.json) | — |
| 12 | 15 bp per side; long-only deciles of residuals | C01 PLAN §2.2; C05 PLAN §3 | — |
| 13 | C01 19 → 2, 13 → 1; C02 7 → 2, 2 → 0 | C02 RESULT §6 | — |
| 13 | C03: 0 vs 0 | C03 RESULT §1 | — |
| 13 | C04: 53 vs 173 discoveries | C04 RESULT §2 table (B 53, A 173) | — |
| 13 | C02: direct tests; C03: residual reward; C04: daily fields, long leg | C02 PLAN §1–2; C03 PLAN §1–2; C04 PLAN §1–2 | — |
| 14 | C01: 3 rounds, 8 seeds; valid heads A 19, B 13; Partura worse | C01 PLAN §2.1–2.5; C01 RESULT §1–§2 | — |
| 14 | C02: 8 seeds; new valid heads A 7, B 2; Partura worse | C02 RESULT header (401–408), §1 | — |
| 14 | C03: 16 seeds; valid heads A 0, B 0; cannot tell | C03 RESULT header (601–616), §1 | — |
| 14 | C04: 16 seeds; median B − A −0.17; p(B worse) 0.11; cannot tell | C04 RESULT header (701–716), §1 | — |
| 14 | C05: 8 seeds; median +0.08; p(B better) 0.42; cannot tell | C05 RESULT header (801–808), §1 | — |
| 15 | median +0.08; p(B better) 0.42; p(B worse) 0.63; B higher 5 of 8 | C05 RESULT §1 | — |
| 15 | means A 0.44, B 0.44 (test) | C05 RESULT §1, §2 | — |
| 15 | forward: median −0.39; p(B worse) 0.039; B higher 2 of 8; means A 0.87, B 0.29; 0.67 years | C05 RESULT §1 | reported only |
| 16 | valid: A 0.94, B 1.52; B higher in 7 of 8 | C05 RESULT §4 item 1 | — |
| 16 | test: 0.44 and 0.44; B higher 5 of 8 | C05 RESULT §1, §2, §4 item 1 | — |
| 16 | forward: A 0.87, B 0.29; B lower in 6 of 8 | C05 RESULT §1, §4 item 1 | — |
| 17 | heads added 101 / 56 / 94 | C05 RESULT §2 table ("其中本组加的") | — |
| 17 | pass test rule 15 of 101; 10 of 56; 3 of 94 | C05 RESULT §2 ("测试段有效") | — |
| 17 | mean single-head test Sharpe 0.80 / 0.69 / 0.32 | C05 RESULT §2 | — |
| 17 | mean single-head forward Sharpe 0.70 / 0.36 / 0.01 | C05 RESULT §2 | — |
| 17 | in-sample score 1.04 / 1.07 / 1.01 | C05 RESULT §4b table | group level |
| 17 | E missions 0.65 (B0), 0.31 (B); N missions 0.54 (B0 plain GP), 0.19 (B) | C05 RESULT §3 table; §4 item 4 | — |
| 18 | at least 5 of 25 E cores are size or volatility rewrites | C05 RESULT §4b | hypothesis |
| 18 | examples LogFloatShares, inv(LogFloatShares), day_var(Ret) | C05 RESULT §4b | — |
| 18 | 0.65 vs 0.31 (locate output, fixed rule vs LLM) | C05 RESULT §3, §4 item 4 | — |
| 18 | about 0.05 (N heads that are or contain a full seed) | C05 RESULT §4b table | — |
| 19 | extra paid evaluations A 4,371, B0 4,579, B 4,891 | C05 RESULT §2 table | — |
| 19 | GP run time M 6.2 h, A 8.2 h, B0 6.3 h, B 6.8 h | C05 RESULT §2 table | — |
| 19 | 101 agent calls (incl. reruns) | C05 RESULT §2 | — |
| 19 | 13.21 M output tokens | C05 RESULT §2: 1,321 万 | unit conversion |
| 19 | 630 M cache read | C05 RESULT §2: 6.30 亿 | unit conversion (the string "630" also matches an unrelated CPU figure elsewhere; not used as evidence) |
| 19 | 47.8 M cache write | C05 RESULT §2: 4,783 万 = 47.83 M | unit conversion, rounded as in the brief |
| 20 | pass: both ≥ 3 and ≥ 4 seeds left; at most 3 audits; struck |ρ| ≥ 0.7 / ≥ 0.5 | C06 PLAN §2.5 (通过规则; 相关度表) | — |
| 20 | correlation table: one day in five; train only; no Sharpe | C06 PLAN §2.5 | — |
| 20 | novelty 1–5; soundness 1–5 | C06 PLAN §2.5 | — |
| 20 | R missions scored on soundness only | C06 PLAN §2.5 | — |
| 21 | 8 seeds; M and A reused from C05 | C06 PLAN §1, §2.1, §5 | design only |
| 21 | test period read five times; C06 designed after C05's test result | C06 PLAN §4; C05 RESULT §6 | — |
| 21 | clean check: data after 2026-09-16 | C06 PLAN §4 | — |
| 21 | planned, not tested: Partura sees train only | C06 PLAN §1 ("这次不做") | dashed box |
| 22 | 1/256; eight pairs; forward 0.67 years | C05 PLAN §3; C05 RESULT §1, §6 | — |
| 22 | literature dates only spot-checked | C05 RESULT §6 | — |
| 22 | C05 E missions counted family in controls | C05 RESULT §4 item 6 | — |
| 22 | survivorship; no delisted names; T+1; limit-up not buyable | C01 PLAN §4 (lines 117, 121); C01 RESULT §7 item 7 | — |
| 23 | two worse (C01, C02); three cannot tell (C03–C05) | RESULT §1 of C01–C05 | — |
| 23 | fused test book 0.44 for both | C05 RESULT §2, §4 item 1 | — |
| 23 | 12 of 14 descendants positive net excess on test; family forward mean 0.04 | C04 RESULT §3 item 3 | — |
| 23 | clean test: data after 2026-09-16 | C06 PLAN §4 | — |
| 24 | all 64 per-seed values | C05 RESULT §2 per-seed table | cell-by-cell match (see §4) |
| 24 | no head counts as 0 | C05 RESULT §2 | — |

---

## 4. Check results

**Build (last run):** `latexmk -xelatex` exit 0. `principles_v2.log`: 0 Overfull, 0 Underfull, 0 errors, 0 "Missing character", 0 font warnings.

**Fonts (`pdffonts`):** FiraSans-Book, FiraSans-BookItalic, FiraSans-Medium, FiraMath-Regular, FiraMono-Regular, all embedded. No CJK font is used; no Chinese characters appear in the source or in the PDF text.

**Alignment (`pdftotext -bbox`):** on pages 2–24 the first frame-title word starts at x = 61.20 pt (0.85 in) with yMin = 36.43 pt, the same as v1. Page numbers end at x ≈ 898.8 pt (page width − 0.85 in) and sit at y ≈ 502.7–517.3 pt, as in v1.

**Content bottom:** the lowest body text on any page ends at 495.5 pt = 6.88 in (page 14), inside the 6.91 in limit used in v1.

**Visual check:** every page rendered at 60 dpi and viewed. Final state: no text outside boxes, no overlaps, titles at the same height, nothing in the footer band.

**Number audit (automated):** every numeric token in the 24 pages was searched in the text of `research/coldstart_C01`–`C05` RESULT.md and `C01`–`C06` PLAN.md. Not found: 2019, 2020, 2024 (timeline axis ticks); 13.21, 47.8 and 630 (unit conversions listed in §3, page 19). Other matches were checked by hand against the table in §3.

**Backup table (page 24):** all 64 values compared with the per-seed rows of `research/coldstart_C05/RESULT.md` §2: 8 of 8 rows match exactly.

**Verdict labels (checked against each RESULT §1):** C01 Partura is worse; C02 Partura is worse; C03 cannot tell; C04 cannot tell; C05 cannot tell.

---

## 5. Open points (what could not be made clean or fully sourced)

1. **"286 searchable operators"** (v1, searcher page): no source found in `research/`, `docs/`, or the AlphaCube checkout. Removed.
2. **5,220 names** (v1, task figure): not in C01–C05. `research/coldstart_C01/PLAN.md` §2.1 gives 5,207 for the store; 5,220 appears only as "production view" in `scripts/signal_books.py`. Deck uses 5,207.
3. **Return and timing formula; first-15-minute VWAP** (page 5): carried from v1. Partly supported by `partura/propose.py:312` (label `open_vwap15`, horizon 1) and `partura/panels.py` (`label_buyable`). The exact P(t+2)/P(t+1) definition is not in the research files or in the AlphaCube checkout here. Check against the AlphaCube label code before presenting.
4. **Forward start date:** C05 RESULT writes 2026-01-01; C01 PLAN uses 2026-01-05 (first trading day). The deck uses 2026-01-05. Same data.
5. **Search depth 2–4** (page 7): from C01 PLAN §2.2, C02 PLAN §2.2 and C04 RESULT §6. C05 PLAN says it reuses C04's environment and does not restate depth.
6. **Illustrative items:** searcher tree and its window values (page 7); known-family thesis wording (page 6); architecture and flow layouts (pages 8, 20); token split and funnel (pages 3, 4). All tagged *illustrative* on the slide. The parse check on the tree that v1 reports was not re-run.
7. **"Partura can only add to the library"** (brief): R missions replace a head with its variant in the same arm's library (C05 PLAN §2.5; C06 PLAN §2.3). The slides say so explicitly ("R may swap a head for its variant, in its own arm's library only") rather than claim pure addition.
8. **"Valid out of sample"** (brief): the RESULT's term is 测试段有效, valid on the test segment under the pre-registered rule. The slides write "pass the test rule (net excess > 0, t ≥ 2.0)" so that the claim is not broader than the rule.
9. **Cache write** 47.8 M: source 4,783万 = 47.83 M, shown rounded, as in the brief.
10. **C06:** no outcome number appears in the deck. Page 21 gives design facts only (8 seeds; M and A reused).
11. **Dashed outlines** = planned / not built. Only one item uses one: page 21, "Partura sees train only" (C06 PLAN §1 says this check is deferred).
12. **Rule check:** C02 valid = net excess > 0 and t ≥ 2.0 (C02 PLAN §3), so the C01/C02 counts on page 14 use the same test-segment rule.

Nothing on the slides is left unsourced except the items in points 3, 6 and 9 above, which are flagged.

## 复核后的修正(主会话,2026-10-29)

- 第 13、14 页 C04 一行:原写「market cap dropped / removed from the controls」,方向写反了。
  - C04 PLAN 的原文是「奖励再去掉市值暴露」,控制里**加了** `LogFloatCap`。
  - 改为「market cap added to the controls」。
- 第 13 页 C05 一行:「it only adds」改为「it never touches M」。R 任务会在本组的库里替换 head,所以「只加」不准确;准确的说法是不改动 M。
- 第 20 页:去掉「*illustrative* thresholds」的标记。这些阈值是 C06 PLAN 事先约定的真实规则,不是示意。
- 收益定义核对了 `AlphaCube-steering/src/alphacube/label.py`:
  - target[t] = V[t+2] / V[t+1] − 1,V = 09:31–09:45 的 VWAP(第 1–15 根 bar,不含 09:30 集合竞价);
  - 入场窗口全程涨停封死的股票记为 NaN;
  - 与幻灯片一致。
- 重编译:0 条 Overfull / Underfull,0 条 Missing character,24 页。
