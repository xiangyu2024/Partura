export const meta = {
  name: 'prod-round',
  description: 'PROD W01 一轮 Partura(精简流程,每个种子独立):取定位输出 → PI(Sonnet 5.5)写任务 → 相关度表 → 审计(Haiku 5.5,1 次)→ 定稿 + 检查 + 推送',
  whenToUse: 'args = {round: 1|2|3, seeds: [901, ...], stage?: "pi"|"audit", from?: {seed: "fetch"|"pi"|"corr"|"audit"|"finish"}}。修订 2 起用 stage:总领先 scripts/prod_round.sh fetch,再 stage "pi",再 prod_round.sh corr,再 stage "audit",再 prod_round.sh finish。research/prod_W01/PLAN.md;规则 research/prod_W01/rules.md',
  phases: [
    { title: 'Fetch', detail: '从种子所在服务器取本轮的定位输出(只是一条命令,Haiku)' },
    { title: 'Plan', detail: 'PI(Sonnet 5.5):本轮的 E / N / R 与研究笔记' },
    { title: 'Audit', detail: '相关度表(一条命令,Haiku)+ 审计员(Haiku 5.5,只审 1 次)' },
    { title: 'Finish', detail: '定稿 + 检查 + 推送到种子所在服务器(一条命令,Haiku)' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura-prod'
const K = args.round
const SEEDS = args.seeds
const FROM = args.from || {}                       // resume: {seed: stage} -- start that seed at the stage (its earlier files are on disk)
const ONLY = args.stage                            // 修订 2: 'pi' | 'audit' = run only that agent; fetch / corr / finish are scripts/prod_round.sh
const M = { pi: 'claude-sonnet-5-5', audit: 'claude-haiku-5-5', run: 'claude-haiku-5-5' }
const D = `${ROOT}/research/prod_W01`
const PY = '/Users/wxy/.venvs/alphacube/bin/python'
const ENVSH = `cd ${ROOT} && export PARTURA_C0X=PROD PARTURA_STUDY_DIR=prod_W01 C06_CTRL_STRIKE=0.8 ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:${ROOT}`
const STAGES = ['fetch', 'pi', 'corr', 'audit', 'finish']
const STR = { type: 'string' }
const NUM = { type: 'number' }

if (![1, 2, 3].includes(K)) throw new Error(`args.round must be 1, 2 or 3; got ${JSON.stringify(K)}`)
if (!Array.isArray(SEEDS) || SEEDS.length === 0 || !SEEDS.every(s => Number.isInteger(s) && s >= 901 && s <= 912)) throw new Error(`args.seeds must be a list of seeds 901..912; got ${JSON.stringify(SEEDS)}`)
for (const s of Object.keys(FROM)) if (!STAGES.includes(FROM[s])) throw new Error(`args.from[${s}] must be one of ${STAGES.join(', ')}`)
if (ONLY !== undefined && !['pi', 'audit'].includes(ONLY)) throw new Error(`args.stage must be "pi" or "audit"; got ${JSON.stringify(ONLY)}`)

const PI_SCHEMA = {
  type: 'object',
  properties: { path: STR, slots: { type: 'array', items: { type: 'object', properties: { type: STR, core: STR, hypothesis: STR }, required: ['type', 'hypothesis'] } }, n_R: NUM, check_exit_code: NUM, summary: STR },
  required: ['path', 'slots', 'n_R', 'check_exit_code', 'summary'],
}
const RUN_SCHEMA = { type: 'object', properties: { exit_code: NUM, output: STR }, required: ['exit_code', 'output'] }
const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    path: STR,
    slots: { type: 'array', items: { type: 'object', properties: { slot: STR, novelty: NUM, soundness: NUM, struck_seeds: { type: 'array', items: NUM } }, required: ['slot', 'novelty', 'soundness', 'struck_seeds'] } },
    R: { type: 'array', items: { type: 'object', properties: { head: STR, soundness: NUM }, required: ['head', 'soundness'] } },
    summary: STR,
  },
  required: ['path', 'slots', 'R', 'summary'],
}

const WRITE_NOTE = `**写文件**:本角色要写的文件是流水线下游要读的工作文件,必须落盘。用 Write;如果 Write 被拒(子代理的「不写报告文件」规则),改用 Bash heredoc 写入,写完 \`ls -l\` 确认。`

function place(S, role) {
  return `
## 你在整件事里的位置(先读这一段)

这是生产运行 PROD(第 1 波)的第 ${K} 轮(共 3 轮)。规则全文在 ${D}/rules.md,**先读它**(环境、任务类型、审计规则、已知陷阱、能读什么)。
**主 AlphaCube(M)**是一个不受任何 agent 影响的 GP,只按它自己的历史禁掉结构相同和高相关的因子;它每一批的产出是你们的原材料。
Partura 对每个随机数种子有一个独立的小组,彼此看不到;你们**只负责种子 ${S}**。**你是这里的「${role}」**。
这一轮能看到 M 的第 1..${K} 批,以及本种子前几轮任务的结果。

**你的指令只有这份提示**。照本提示把你这一步完整做完,不要改动别的步骤,也不要去读本提示没有让你读的东西(规则 §5 的读写范围是硬规矩)。

${WRITE_NOTE}`
}

const MISSIONS_FORMAT = `
\`\`\`yaml
seed: <种子>
round: <轮>
slots:
  - type: E
    core: '<核心表达式:原样取自 loc.md 里某个 head 的子树(整个 head 也可以),或共性表 / 核心卡里的子树>'
    hypothesis: '<为什么它是 alpha 的来源;这次要试的外围处理是什么、实现的是什么机制、为什么和以前不一样、为什么样本外还会在>'
    seeds: ['<原样含核心的表达式>', ...]    # 8–16 个(审计会划掉一些;剩下少于 4 个这个位就不通过)
  - type: N
    hypothesis: '<新 idea:机制是什么、算子怎样实现它、为什么样本外还会在>'
    inspired_by: '<哪一批里的什么现象>'
    seeds: ['...', ...]                      # 8–16 个
R:                                           # 可选
  - head: '<loc.md heads 表里的表达式原文>'
    why: '<哪个部件是烂的,依据>'
    variants: ['...', ...]
\`\`\``

function runPrompt(cmd, retry) {
  return `(只做一件事。)在终端跑下面这条命令(Bash 工具的 timeout 设 600000),原样报告它的退出码和完整输出。${retry || ''}不读、不改任何其他文件。

\`${cmd}\``
}

function fetchPrompt(S) {
  return runPrompt(`bash ${ROOT}/scripts/prod_sync.sh fetch ${K} "${S}"`, '失败(退出码非 0)就再跑一次同一条命令,以第二次的结果为准。')
}

function piPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, 'PI')}

## 你的任务(PI)

读 ${P}/r${K}/loc.md(细节在 loc.json),${P}/r${K}/R_prev.json(若有),${P}/notebook.md 与之前各轮的 missions_final.yaml、audit_record.json(若有),以及规则 §2–§4。
决定本轮的 2 个 GP 任务位(各为 E 或 N)和可选的 R(至多 16 个变体)。**你的计划会交给独立审计员**按规则 §3 打创新度与合理度;
它看不到你的笔记,只看 missions.yaml —— 所以 hypothesis 要把机制、算子怎么实现它、为什么和库里已有的不同、为什么样本外还会在写清楚。

写 ${P}/r${K}/missions.yaml,格式:
${MISSIONS_FORMAT}

规则:每个核心整个实验至多 2 个 E 位;3 轮里至少 1 个 N 位通过审计;E 的种子必须**原样包含**核心;E 的外围要和快照里已经见过的写法很不一样;
种子里不用 ts_spearman 与 nt_*。种子用我们的算子语言写(参考 loc.md 里的表达式、${ROOT}/partura/ops_ext.py 与 AlphaCube 的算子源码)。
**不要打开 \`guidance/\` 下的任何文件**(规则 §5):\`c06_check.py\` 会自己加载它需要的那份,已知族的定义规则 §1 里有;需要规范化 / 查重就直接跑 \`c06_check.py\`。

然后在 ${P}/notebook.md 末尾追加「第 ${K} 轮」一节(没有就新建):你目前对本种子 alpha 来源的信念;本轮每个任务的**事先预测**(会不会产出 heads、大致是什么、为什么);上一轮的预测对不对。

写完自己跑:\`${ENVSH} && ${PY} scripts/c06_check.py ${S} ${K}\`,不合格就改到合格;check_exit_code 填最后一次的退出码。`
}

function corrPrompt(S) {
  return `(只做一件事。)在终端跑下面这条命令(Bash 工具的 timeout 设 600000)。它每次最多等 5 分钟左右:输出里有「STILL RUNNING」(退出码 3)就**再跑同一条命令**,
它会接着等同一个作业、不会重算;一直重复到退出码 0 或出现「CORR FAILED」为止(最多重复 12 次)。然后原样报告最后一次的退出码和输出。不读、不改任何其他文件。

\`bash ${ROOT}/scripts/prod_sync.sh corr ${K} ${S} 1\``
}

function auditPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '独立审计员')}

## 你的任务(独立审计员,只审这一次)

你独立于 PI:**不读** ${P}/notebook.md(规则 §5)。你要读:
- ${D}/rules.md(尤其 §3 打分标准与 §4 已知陷阱);
- PI 的计划 ${P}/r${K}/missions.yaml;
- 相关度表 ${P}/r${K}/corr_1.md(细节在 corr_1.json):每个表达式与快照里每个 head、与 5 个控制的 |ρ|(train);
- 快照里的全部 heads(主 AlphaCube 的 + 本种子之前任务的)—— 这就是「已有因子库」。只需要 loc.md 开头的 heads 表:\`sed -n '1,/^## 共性/p' ${P}/r${K}/loc.md\`,不用读它后面的共性表与拆解;
- 之前各轮的 ${P}/r*/missions_final.yaml 与 audit_record.json(若有):以前试过什么、挡过什么;
- 看不懂的算子去读源码(${ROOT}/partura/ops_ext.py、$HOME/Desktop/AlphaCube-steering/src/alphacube/):**先 \`grep -rn "def <算子名>"\` 找到定义,只读那一段**(sed -n 起,止),不要整个文件读。

对每个任务位判断:
- **创新度**(1–5):和库里已有的 head 比,是不是本质上不同的东西或实质性的改进?相关度表的数是证据之一,但低相关不等于新(换个控制变量的写法也可能和 head 都不相关)。
- **合理度**(1–5):这个机制说得通吗?算子组合真的实现了它吗(逐个算子核对)?窗口合理吗?有没有落进 §4 的陷阱?
- 逐个看种子:哪些种子不符合这个位的 idea、是陷阱、或只是 head 的换皮,划掉(写 1 起的序号)。
- 对每个 R 组只评合理度。
分数要按 §3 的标准给:只挡数学问题和明显度量同一个东西的,其余放行;不要为了放行而凑 3 分,也不要为了显得严格而压分。

写 ${P}/r${K}/audit_1.yaml:

\`\`\`yaml
attempt: 1
slots:
  - slot: a                 # 第一个任务位 a,第二个 b
    novelty: <1-5>
    soundness: <1-5>
    struck_seeds: [<序号>, ...]
    reasons: '<打分的理由:引用相关度表、具体的 head、具体的算子;并写一句「如果它有 alpha,最可能来自哪里」>'
  - slot: b
    ...
R:
  - head: '<R 组的 head 原文>'
    soundness: <1-5>
    reasons: '...'
summary: '<一句话>'
\`\`\``
}

function finishPrompt(S) {
  return runPrompt(`${ENVSH} && ${PY} scripts/prod_finish.py ${K} ${S}`,
    '它依次定稿、检查、推送到种子所在的服务器;最后一行是「PUSHED …」或「NOT PUSHED …」。别的都不用做,失败也不要重试,原样报告。')
}

async function runSeed(S) {
  const tag = `prod r${K} s${S}`
  const from = STAGES.indexOf(FROM[S] || 'fetch')
  const out = { seed: S }
  if (from <= 0) {
    const f = await agent(fetchPrompt(S), { label: `${tag}:fetch`, phase: 'Fetch', model: M.run, schema: RUN_SCHEMA })
    if (!f || f.exit_code !== 0) return { ...out, failed: 'fetch', detail: f && f.output }
  }
  if (from <= 1) {
    const pi = await agent(piPrompt(S), { label: `${tag}:pi`, phase: 'Plan', model: M.pi, schema: PI_SCHEMA })
    if (!pi) return { ...out, failed: 'pi' }
    if (pi.check_exit_code !== 0) return { ...out, failed: 'pi-check', detail: pi.summary }
    out.plan = { slots: pi.slots.map(s => s.type), n_R: pi.n_R }
  }
  if (from <= 2) {
    let c = await agent(corrPrompt(S), { label: `${tag}:corr`, phase: 'Audit', model: M.run, schema: RUN_SCHEMA })
    if (!c || c.exit_code !== 0) c = await agent(corrPrompt(S), { label: `${tag}:corr-retry`, phase: 'Audit', model: M.run, schema: RUN_SCHEMA })
    if (!c || c.exit_code !== 0) return { ...out, failed: 'corr', detail: c && c.output }
  }
  if (from <= 3) {
    const aud = await agent(auditPrompt(S), { label: `${tag}:audit`, phase: 'Audit', model: M.audit, schema: AUDIT_SCHEMA })
    if (!aud) return { ...out, failed: 'audit' }
    out.audit = { slots: aud.slots, R: aud.R, summary: aud.summary }
  }
  const fin = await agent(finishPrompt(S), { label: `${tag}:finish`, phase: 'Finish', model: M.run, schema: RUN_SCHEMA })
  if (!fin) return { ...out, failed: 'finish' }
  const text = fin.output || ''
  out.finalized = (text.split('\n').find(l => l.startsWith('FINALIZED')) || '').slice(0, 300)
  out.pushed = /^PUSHED /m.test(text)               // prod_finish.py prints PUSHED only on success; the agent may not see the exit code
  log(`种子 ${S} 第 ${K} 轮:${out.pushed ? '已推送' : '未推送'}。${out.finalized || text.slice(-200)}`)
  if (!out.pushed) out.failed = 'finish'
  if (!out.pushed) out.detail = text.slice(-600)
  return out
}

async function runStage(S) {
  const tag = `prod r${K} s${S}`
  if (ONLY === 'pi') {
    const pi = await agent(piPrompt(S), { label: `${tag}:pi`, phase: 'Plan', model: M.pi, schema: PI_SCHEMA })
    if (!pi) return { seed: S, failed: 'pi' }
    if (pi.check_exit_code !== 0) return { seed: S, failed: 'pi-check', detail: pi.summary }
    return { seed: S, plan: { slots: pi.slots.map(s => s.type), n_R: pi.n_R }, summary: pi.summary }
  }
  const aud = await agent(auditPrompt(S), { label: `${tag}:audit`, phase: 'Audit', model: M.audit, schema: AUDIT_SCHEMA })
  if (!aud) return { seed: S, failed: 'audit' }
  return { seed: S, audit: { slots: aud.slots.map(s => ({ slot: s.slot, novelty: s.novelty, soundness: s.soundness, struck: s.struck_seeds })), R: aud.R, summary: aud.summary } }
}

const results = await parallel(SEEDS.map(S => () => (ONLY ? runStage(S) : runSeed(S))))
return { round: K, stage: ONLY || 'all', results: results.map((r, i) => r || { seed: SEEDS[i], failed: 'error' }) }
