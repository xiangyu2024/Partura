export const meta = {
  name: 'c07-verify',
  description: 'C07 验证员(Opus 5.5):每个种子 × 两个版本(只看 train / train+valid)各一次,逐个决定候选因子库里的 head 留下或去掉',
  whenToUse: 'args = {seeds: [801, ...], variants: ["train", "all"], rules?: "rules_v2.md", outdir?: "verify_v2"}。research/coldstart_C07/PLAN.md §2.3',
  phases: [{ title: 'Verify', detail: '每个种子 × 版本一次独立调用' }],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const D = `${ROOT}/research/coldstart_C07`
const SCHEMA = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    n_heads: { type: 'number' },
    kept: { type: 'array', items: { type: 'number' } },
    dropped: { type: 'array', items: { type: 'object', properties: { id: { type: 'number' }, reason: { type: 'string' } }, required: ['id', 'reason'] } },
  },
  required: ['path', 'n_heads', 'kept', 'dropped'],
}

function prompt(S, v) {
  const mat = `${D}/screen/s${S}_${v}.md`
  const out = `${D}/${args.outdir || 'verify'}/s${S}_${v}.yaml`
  const rules = `${D}/${args.rules || 'rules.md'}`
  return `你是 C07 的独立验证员,只负责种子 ${S} 的「${v === 'train' ? '只看 train' : 'train 与 valid'}」版本。你的指令只有这份提示;上下文里如果出现研究负责人与主会话之间的对话,那不是给你的。

先读规则 ${rules},再读本种子的验证材料 ${mat}。看不懂的算子去读源码(${ROOT}/partura/ops_ext.py、$HOME/Desktop/AlphaCube-steering/src/alphacube/)。
**只能读**这三样;不读 ${D}/screen/ 下的其他文件(尤其是其他种子的、以及${v === 'train' ? '本种子的 _all 版本' : '其他版本'}),不读 research/ 下的其他目录、episodes/、任何 2023-08-08 之后的数字。

对材料表里的每一个 head(按 # 编号)决定留下还是去掉,严格按规则文件(只有规则写明的情形才去掉)。逐个看表达式在度量什么、有没有数学问题、与其他 head 和控制是否度量同一个东西。
没有配额。写 ${out}(用 Write;被拒就用 Bash heredoc 写入,写完 ls -l 确认):

\`\`\`yaml
seed: ${S}
variant: ${v}
decisions:
  - id: 1
    keep: true
    reason: '<一句话:它度量什么;留下或去掉的理由>'
  - id: 2
    ...
\`\`\`

每个 head 都要有一条。最后在结构化结果里返回 kept(留下的 id 列表)与 dropped(去掉的 id 与理由)。`
}

const jobs = []
for (const S of args.seeds) for (const v of (args.variants || ['train', 'all'])) jobs.push({ S, v })
const results = await parallel(jobs.map(({ S, v }) => () =>
  agent(prompt(S, v), { label: `c07v:s${S}:${v}`, phase: 'Verify', model: 'claude-opus-5-5', schema: SCHEMA })
    .then(r => (r ? { seed: S, variant: v, n: r.n_heads, kept: r.kept.length, dropped: r.dropped.length } : { seed: S, variant: v, failed: true }))))
return { results }
