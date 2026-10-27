# Superday Topic B — principles part: page outline and layout spec

Scope of this file: the **principles / method** half of the 20-minute talk (task definition, agents, loop, steering
interface, evaluation protocol, token accounting). The results half (C01 cold-start comparison, the bad-signal case)
is added after C01 finishes; nothing in this half quotes a C01 number.

Emphasis: **Partura is the subject.** AlphaCube appears only as "the agent-free searcher" (one slide, black box with
an interface).

## Page outline (principles part, ~12 minutes)

| # | Title (English, as on the slide) | The one point of the page | Main visual |
|---|---|---|---|
| 1 | Partura: an LLM research loop that steers a symbolic alpha miner | Title, name, Topic B, date | — |
| 2 | Outline | Principles (this deck) → results (C01, running) → limitations | numbered list, results part marked *in progress* |
| 3 | Search is cheap, belief is expensive | LLMs should not write thousands of formulas; they should form beliefs and change where a cheap searcher looks | two-speed loop sketch: inner loop (0 tokens) / outer loop (tokens) |
| 4 | Task specification | Exact inputs and the exact output object | input → system → output block diagram + signal definition formula |
| 5 | A finished output is a signal card | Definition of done: thesis + implementation + evidence + provenance | table (field / content / who fills it); example row marked *illustrative* |
| 6 | The searcher is a black box with three handles | AlphaCube = typed GP over a (stock, day, minute) tensor; Partura only touches seeds, sampling weights, accept filter | box diagram of the searcher with the three handles |
| 7 | Agent roles | Who does what, on which model, with what input / output; proposer ≠ judge | table: role / model / reads / writes / may not |
| 8 | One round of the loop | Order of work and the files that carry it | swimlane flowchart (Coordinator, Lead, Executors, Checker, Searcher, Judge) |
| 9 | From belief to intervention | A guidance file turns beliefs into a change of the proposal distribution | formula q(x) ∝ p(x)·w(x) + four intervention types + YAML excerpt (*illustrative*) |
| 10 | Measuring the system, not a signal | Matched-budget A/B: same GP, same seed, same budget, with vs without Partura | round × seed design diagram + split timeline |
| 11 | Decision rules, fixed before any run | Heads, "valid", verdict table | formulas + verdict table |
| 12 | Token accounting | Tokens are spent only in the outer loop; what is measured and the stopping rule | cost model formula + role/model budget table (*measured values: pending*) |
| 13 | Integrity: what keeps the loop honest | Cold start, information barrier, direction fixed on train, ledgered holdout, costs, immutable raw results | two-column checklist (mechanism / how it is enforced) |
| 14 | Implemented vs. planned | Separate what runs today from what is design | status table |
| 15 | Known limitations, stated before the results | Survivorship (no delisted names), A-share long-only, test segment seen by the designer, power | short list |

## Layout spec (applies to every page)

- **Page**: 16:9, 13.333 in × 7.5 in (33.87 cm × 19.05 cm), so point sizes are literal.
- **Theme**: Beamer Metropolis, XeLaTeX, Fira Sans (text) + Fira Math (math). White background.
- **Grid**: left and right text margin 0.85 in; frame title baseline at the same height on every page;
  content block starts at the same height on every page; all elements left-aligned to the left margin.
  Page number bottom-right, 12 pt, mid-gray, same position on every page. No header/footer bars.
- **Type sizes**: frame title 32 pt; body 20 pt; secondary text (second level, figure labels) 16–18 pt;
  footnotes / citations / *illustrative* tags 14 pt. At most two text levels per page.
- **Colors**: text dark gray `#2E2E2E`; secondary gray `#6B6B6B`; rules / light lines `#C8C8C8`;
  one accent blue `#1F5A96` (LLM / Partura components, the one key phrase of a page). Nothing else.
- **Figures**: TikZ; one line width (0.9 pt) for all boxes and arrows; arrow tip `Stealth`; square corners;
  no fills except a single 10 % accent tint allowed to mark "the LLM part"; dashed outline = planned / not yet built.
  Node text 16–18 pt. Same box height and spacing across figures.
- **Math**: the same symbols everywhere: stock $i$, day $t$, signal $s_{i,t}$, forward return $r_{i,t+1}$,
  expression $x$, proposal distribution $p(x)$, guidance weight $w(x)$, arms $A$ (search alone) / $B$ (search + Partura),
  number of seeds $K$, budget per arm per seed $N$.
- **Honesty markers**: any schematic number carries an *illustrative* tag; implemented vs planned are separate
  (status words, dashed outlines); no C01 result appears in this part.
- **Forbidden**: gradients, shadows, rounded cards, icons, photos, three-column dense layouts, progress bars.
