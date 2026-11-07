// Test harness for workflows/prod_round.js: runs the script body against a mock of the Workflow runtime (agent / parallel / log / phase /
// args) and prints {calls, result, meta_ok} as JSON.  node tests/prod_round_harness.js <script.js> '<args json>' '<behaviour json>'
// behaviour: {"<label suffix>": <result | null>} overrides the canned result of that stage (null = the agent died); {"__seq:corr": [a, b]}
// returns a, then b for successive calls of that stage.
const fs = require('fs')
const [, , script, argsJson, behJson] = process.argv
const src = fs.readFileSync(script, 'utf8')
const m = src.match(/^export const meta = \{[\s\S]*?\n\}\n/m)
if (!m) { console.error('no meta literal'); process.exit(2) }
const body = src.replace(m[0], '')
const args = JSON.parse(argsJson || '{}')
const beh = JSON.parse(behJson || '{}')
const calls = [], logs = [], seq = {}
const CANNED = {
  fetch: { exit_code: 0, output: 'ok: 12345 bytes of locate output' },
  pi: { path: 'missions.yaml', slots: [{ type: 'E', core: 'x', hypothesis: 'h' }, { type: 'N', hypothesis: 'h2' }], n_R: 1, check_exit_code: 0, summary: 'ok' },
  corr: { exit_code: 0, output: 'corr_1.md written: 20 rows' },
  audit: { path: 'audit_1.yaml', slots: [{ slot: 'a', novelty: 4, soundness: 4, struck_seeds: [] }, { slot: 'b', novelty: 3, soundness: 3, struck_seeds: [2] }], R: [], summary: 'ok' },
  finish: { exit_code: 0, output: 'FINALIZED after 1 audit(s): slot a E novelty 4 soundness 4 seeds 8/8 -> pass\nCHECK OK: 2 slots, R 0 variants\n901 pushed (abc)\nPUSHED seed 901 round 1' },
}
async function agent(prompt, opts) {
  const stage = (opts.label.split(':')[1] || '')
  const key = stage.replace(/-retry$/, '')
  calls.push({ label: opts.label, phase: opts.phase, model: opts.model, schema: !!opts.schema, prompt })
  const sk = `__seq:${key}`                       // a "-retry" call of a stage shares the stage's behaviour / sequence
  if (beh[sk]) { seq[sk] = (seq[sk] || 0); const v = beh[sk][Math.min(seq[sk]++, beh[sk].length - 1)]; return v }
  if (key in beh) return beh[key]
  return CANNED[key]
}
async function parallel(thunks) {
  return Promise.all(thunks.map(async t => { try { return await t() } catch (e) { return null } }))
}
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
const fn = new AsyncFunction('args', 'agent', 'parallel', 'log', 'phase', 'budget', 'pipeline', body)
fn(args, agent, parallel, s => logs.push(s), () => {}, { total: null, spent: () => 0, remaining: () => Infinity }, null)
  .then(result => { console.log(JSON.stringify({ calls, logs, result })) })
  .catch(e => { console.log(JSON.stringify({ calls, logs, error: String(e.message || e) })) })
