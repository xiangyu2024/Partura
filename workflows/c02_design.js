export const meta = {
  name: 'c02-design',
  description: 'C02 W2:Partura v2 读直接检验结果,设计 GP 的初始种群与先验 —— 总领(Opus 5.5)判读 → 主研(Opus 5)写 guidance/C02_r<k>.yaml → 检查(Haiku 5.5)校验 → 总领拍板、分配种子、写事先预测',
  whenToUse: 'args = {round: 1, n_direct: <直接检验的变体数>}。research/coldstart_C02/PLAN.md §2.4 第 3 步',
  phases: [
    { title: 'Read', detail: '总领判读直接检验:哪些假设在样本内成立、哪些是代理' },
    { title: 'Write', detail: '主研写初始种群(种子)与先验' },
    { title: 'Check', detail: '确定性校验;不合格修订一次' },
    { title: 'Approve', detail: '总领审定、分配种子、写预测' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const K = (args && args.round) || 1
const NDIRECT = (args && args.n_direct) || 64
const M = Object.assign({ coord: 'claude-opus-5-5', lead: 'claude-opus-5', check: 'claude-haiku-5-5' }, (args && args.models) || {})
const D = `${ROOT}/research/coldstart_C02`
const C1 = `${ROOT}/research/coldstart_C01`
const PY = '/Users/wxy/.venvs/alphacube/bin/python'
const ENVSH = `cd ${ROOT} && export ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:${ROOT}`
const GUIDE = `guidance/C02_r${K}.yaml`
const SEEDS = Array.from({ length: 8 }, (_, i) => 400 + 100 * (K - 1) + 1 + i)
const GPB = 192 - Math.ceil(NDIRECT / 8)
const STR = { type: 'string' }

function place(role) {
  return `
## 你在整件事里的位置(先读这一段)

事先约定的对照实验(${D}/PLAN.md,先读它):AlphaCube 的 GP 单独跑(A 组)对比 Partura v2(B 组)。你是 B 组的 Partura,分级团队:总领(Opus 5.5)、主研(Opus 5)、检查(Haiku 5.5)。
**你就是这里的「${role}」**。现在是 W2:你在 W1 写的假设已经被**直接评估**过了(结果在 ${D}/direct_r${K}.md / .json),
你要据此**设计 GP 的初始种群**(种子)和先验;GP 会在这个种群附近精修,每个种子(随机数种子)预算 ${GPB} 次付费评估(= 192 − ⌈${NDIRECT}/8⌉,直接检验已经花掉的从 B 组预算里扣)。

工作流会把用户最近对总领说的一句话原样转给你(「用户请求」)。那句话是说给总领的,总领已经处理过;**它和下面的任务不冲突,不要因此跳过或缩减任务。**

## 能读什么、不能读什么(硬规矩,事后审计)

**可以读**:${D}/ 下的文件(PLAN.md、prior_c01.md、hypotheses_r${K}.yaml、direct_r${K}.md/json、W1 的记录);C01 的样本内材料(${C1}/PLAN.md、digest_r*、beliefs_r*、cards_r*、round*_workflow.json;episodes/c01*/evidence.json);代码与算子源码。
**不得读**:${C1}/RESULT.md、final*.json、ledger_c01.json;${ROOT}/runs/、lab/、notes/、studies/、handoff/、batches/、docs/;任何 C02 A 组的东西(episodes/c02r*s*A_*)。
不改代码、不改 PLAN、不跑服务器、不 git commit。只写本角色被要求写的那个文件。`
}

const ENV = `
## 环境规则(两组相同)

奖励 \`long\`(纯多头十分位扣 15bp;score = train 与 valid 较差的;**score ≥ 0.7 为发现**);**与已知族 \`cross_mean(day_std(Amt), 30)\` 的 |ρ| ≥ 0.5 → 判不合格**;
**禁 \`ts_spearman\` 与全部 \`nt_*\`**。样本外只认与 C01 heads |ρ| < 0.7 的「新」东西(C01 heads 见 ${D}/prior_c01.md)。

## 指引文件的格式(${ROOT}/${GUIDE})

从 ${ROOT}/guidance/C02_base.yaml 复制起步;\`pool\` 必须原样;\`reward: []\`、\`evaluation: []\`。
- \`ideas\`:1 或 2 个。每个 idea 的 \`seeds\` 就是你设计的**初始种群**:≤ 24 个表达式,会占初代 48 个个体里的最多一半,另一半是 GP 自己的随机树(它们也过环境规则和你的先验)。
  每个种子在平行的 \`seed_roles\` 里标 \`new\`(新的、预期与已知族和 C01 heads 低相关的机制)或 \`improve\`(对 C01 某个 head 或某个直接检验发现的潜在大幅改进);**improve ≤ 1/3**。
  每个 idea 要有 \`id\`(C2…开头)、\`hypothesis\`、\`thesis: {mechanism, counterparty, prediction, fails_if}\`、\`seeds\`、\`seed_roles\`、\`reward: long\`。
  \`grammar.day_ops\` 是可选的「邻域硬约束」(候选必须含其一;C01 证明它很容易被装饰性满足,慎用);idea 里出现的算子采样频率 ×8。
- **种子怎么选**:优先用直接检验里**成立的**写法及其近邻(换窗口、换平滑、换归一化),让 GP 在已确认有信号的机制附近精修;再放一部分没测过但理由充分的新写法。
  被相关度拒绝、或对照变体同样过线(说明是代理)的写法不要放。种子不加换手约束。
- \`priors\`(可选):\`{id, action: ban|weight|rewrite|family, pattern, w, why, evidence}\`。模式语法:\`_\` 任意子树、\`$w\` 数字、\`{a|b}\`、\`@price\`/\`@flow\`/\`@any\`、\`root:\`。
  **按字段类型加权**:例如 \`{id: P_flow, action: weight, w: 0.3, pattern: '@flow', unless: '__never__(_)', why: ..., evidence: [...]}\` —— 含 Amt/Volume 叶子的树以 0.3 的相对概率被接受
  (必须带这个 \`unless\`,否则会被折叠成对叶子无效的算子权重)。一条 w > 1 的规则会让其余所有树相对降权。
- 种子分配:随机数种子 ${SEEDS.join(', ')};1 个 idea 用满 8 个;2 个 idea 时前 4 个给第一个、后 4 个给第二个。
- 写完自己跑:\`${ENVSH} && ${PY} scripts/c02_check.py guidance ${GUIDE}\`,不合格就改到合格。`

const READ_SCHEMA = {
  type: 'object',
  properties: {
    reading: { type: 'string', description: '逐个假设:直接检验说明了什么(机制成立 / 只是代理 / 被成本或相关度拒绝 / 没测到),对照有没有区分开' },
    design: { type: 'string', description: '初始种群怎么配:押哪几个已确认的机制做精修、放哪些新写法、哪些 improve;1 个还是 2 个 idea;要不要先验' },
  },
  required: ['reading', 'design'],
}
const LEAD_SCHEMA = { type: 'object', properties: { path: STR, n_seeds: { type: 'number' }, summary: STR }, required: ['path', 'n_seeds', 'summary'] }
const CHECK_SCHEMA = { type: 'object', properties: { admissible: { type: 'boolean' }, exit_code: { type: 'number' }, output: STR }, required: ['admissible', 'exit_code', 'output'] }
const FINAL_SCHEMA = {
  type: 'object',
  properties: {
    approved: { type: 'boolean' },
    assignment: { type: 'array', items: { type: 'object', properties: { idea: STR, seeds: { type: 'array', items: { type: 'number' } } }, required: ['idea', 'seeds'] } },
    edits: STR,
    predictions: { type: 'string', description: '对 B 组 GP 精修结果的事先预测(写在结果之前)' },
  },
  required: ['approved', 'assignment', 'edits', 'predictions'],
}

async function call(prompt, opts, tries = 3) {
  for (let i = 0; i < tries; i++) {
    const r = await agent(prompt, i ? { ...opts, label: `${opts.label}#retry${i}` } : opts)
    if (r) return r
    log(`${opts.label}: no result (attempt ${i + 1}/${tries})`)
  }
  return null
}

phase('Read')
const rd = await call(`${place('总领')}

读 ${D}/PLAN.md、${D}/hypotheses_r${K}.yaml、${D}/direct_r${K}.md(必要时读 .json)、${D}/prior_c01.md。
逐个假设判读直接检验:机制在样本内成立了吗?对照有没有把「机制」和「代理(波动 / 价格刻度 / 流动性)」区分开?哪些被相关度拒绝、哪些被成本杀死?
然后给出初始种群的设计方案(交给主研去写)。
${ENV}`, { label: `c02r${K}:coord-read`, phase: 'Read', schema: READ_SCHEMA, model: M.coord })
if (!rd) return { round: K, error: 'coordinator read failed after retries' }

phase('Write')
const leadPrompt = (extra) => `${place('主研')}

总领的判读:${rd.reading}
总领的设计方案:${rd.design}

任务:写 **${ROOT}/${GUIDE}**(以及一页说明 ${D}/design_r${K}.md:每个种子从哪来、为什么、预期它的 GP 后代会找到什么)。
${extra || ''}
${ENV}`
let lead = await call(leadPrompt(), { label: `c02r${K}:lead`, phase: 'Write', schema: LEAD_SCHEMA, model: M.lead })
if (!lead) return { round: K, error: 'lead failed after retries', read: rd }

phase('Check')
const checkPrompt = () => `${place('检查')}

只做一件事:运行下面这条命令,把完整输出和退出码原样交回(不改任何文件,以脚本为准):
\`${ENVSH} && ${PY} scripts/c02_check.py guidance ${GUIDE}; echo "exit=$?"\`
admissible = (退出码为 0)。`
let check = await call(checkPrompt(), { label: `c02r${K}:check`, phase: 'Check', schema: CHECK_SCHEMA, model: M.check })
let revised = false
if (!check || !check.admissible) {
  revised = true
  lead = await call(leadPrompt(`\n**上一版没有通过校验**,只改校验指出的问题:\n${check ? check.output : '(检查没有返回)'}\n`),
    { label: `c02r${K}:lead-revise`, phase: 'Check', schema: LEAD_SCHEMA, model: M.lead })
  check = await call(checkPrompt(), { label: `c02r${K}:check2`, phase: 'Check', schema: CHECK_SCHEMA, model: M.check })
}
if (!check || !check.admissible) return { round: K, error: 'guidance not admissible after one revision', read: rd, lead, check }

phase('Approve')
const fin = await call(`${place('总领')}

主研写好了 ${ROOT}/${GUIDE} 与 ${D}/design_r${K}.md,已通过确定性校验。主研的说明:${lead.summary}
审一遍:种子是不是建立在直接检验的证据上(成立的机制 + 有理由的新写法),有没有把已知族、代理、被拒绝的写法带进来;improve 是否 ≤ 1/3。
你可以直接改文件(改完必须重跑 \`${ENVSH} && ${PY} scripts/c02_check.py guidance ${GUIDE}\` 并确认通过)。
写 ${D}/beliefs_r${K}.md:你现在相信什么、对 B 组 GP 精修结果的可证伪预测(heads 数、哪类结构、与已知族 / C01 heads 的相关)。最后给出种子分配。
${ENV}`, { label: `c02r${K}:coord-final`, phase: 'Approve', schema: FINAL_SCHEMA, model: M.coord })

return { round: K, read: rd, lead, check, revised, final: fin }
