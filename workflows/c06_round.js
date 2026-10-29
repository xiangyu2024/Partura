export const meta = {
  name: 'c06-round',
  description: 'C06 一轮 Partura(C 组,每个种子独立):结构解剖员(Opus 5)→ 文献员(Sonnet 5)→ PI(Opus 5.5)写任务 → 相关度表 → 独立审计员(Opus 5.5)打创新度与合理度,不过就退回 PI 重写(至多审 3 次)→ 定稿与检查',
  whenToUse: 'args = {round: k, seeds: [801, ...], skip_anatomy?: [...], skip_lit?: [...]}。research/coldstart_C06/PLAN.md §2.4–2.5',
  phases: [
    { title: 'Anatomy', detail: '结构解剖员:哪些子树是 alpha 的来源、哪些部件是烂的(第 1 轮复用 C05 的同一份)' },
    { title: 'Literature', detail: '文献员:类似结构在文献里怎么处理(第 1 轮复用)' },
    { title: 'Plan', detail: 'PI:本轮的 E / N / R 与研究笔记;审计不过时重写' },
    { title: 'Audit', detail: '相关度表 + 独立审计员:创新度、合理度' },
    { title: 'Finalize', detail: '按最后一次审计定稿;文献日期检查' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const K = args.round
const SEEDS = args.seeds
const MAX_AUDITS = 3
const M = { pi: 'claude-opus-5-5', anat: 'claude-opus-5', lib: 'claude-sonnet-5', audit: 'claude-opus-5-5', run: 'claude-haiku-5-5' }
const D = `${ROOT}/research/coldstart_C06`
const PY = '/Users/wxy/.venvs/alphacube/bin/python'
const ENVSH = `cd ${ROOT} && export ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:${ROOT}`
const STR = { type: 'string' }
const NUM = { type: 'number' }

function place(S, role) {
  return `
## 你在整件事里的位置(先读这一段)

事先约定的对照实验 C06。规则全文在 ${D}/rules.md,**先读它**(环境、任务类型、审计规则、已知陷阱、能读什么)。
**主 AlphaCube(M)**是一个不受任何 agent 影响的 GP,只按它自己的历史禁掉结构相同和高相关的因子;它每一批的产出是你们的原材料。
你们是 C 组的 Partura,**只负责随机数种子 ${S}**(其他种子各有一个独立的 Partura,彼此看不到)。团队:PI(Opus 5.5,写任务)、结构解剖员(Opus 5)、
文献员(Sonnet 5)、独立审计员(Opus 5.5)、检查(Haiku 5.5)。**你是这里的「${role}」**。现在是第 ${K} 轮(共 3 轮):能看到 M 的第 1..${K} 批,以及本种子前几轮任务的结果。
对照组把同样的算力花在更多普通搜索上;最终比的是因子库在样本外的表现。

**写文件**:本角色要写的文件是流水线下游要读的工作文件,必须落盘。用 Write;如果 Write 被拒(子代理的「不写报告文件」规则),改用 Bash heredoc 写入,写完 \`ls -l\` 确认。`
}

const ANAT_SCHEMA = {
  type: 'object',
  properties: { path: STR, cores: { type: 'array', items: { type: 'object', properties: { core: STR, why: STR }, required: ['core', 'why'] } }, queries: { type: 'array', items: STR }, summary: STR },
  required: ['path', 'cores', 'queries', 'summary'],
}
const LIB_SCHEMA = { type: 'object', properties: { path: STR, n_sources: NUM, n_verified: NUM, summary: STR }, required: ['path', 'n_sources', 'n_verified', 'summary'] }
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
const CHECK_SCHEMA = {
  type: 'object',
  properties: { exit_code: NUM, output: STR, lit_date_violations: { type: 'array', items: STR }, lit_unverified: { type: 'array', items: STR } },
  required: ['exit_code', 'output', 'lit_date_violations', 'lit_unverified'],
}

function anatPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '结构解剖员')}

## 你的任务(结构解剖员)

读 ${P}/r${K}/loc.md(细节在 loc.json),${P}/notebook.md,以及之前各轮的文件(missions_final.yaml、audit_record.json、R_prev.json 等)。回答:
1. **alpha 的来源**:哪些子树(核心)是真来源?用定位工具的证据说话 —— 共性(含它的候选 score 高多少、p、多少个候选含它)、充分性(子树单独当因子的 score)、
   必要性(跳过一个算子掉多少)、敏感性(换同类字段 / 窗口减半加倍是否稳)。区分「真来源」和「只是代理」(规则 §4 的三类陷阱),看不懂的算子去读源码。
2. **烂部件**:哪些部件必要性 ≤ 0、或换掉反而更好 —— 适合做 R。
3. **之前的任务**:E 在哪个核心上试了什么外围、有没有产出 heads;N 的结果;R 的替换与收录;审计员挡掉了什么、为什么;上一轮笔记里的预测对不对。
4. **本轮候选**:值得深挖的核心(≤ 3 个;每个写出它周围已经见过的外围写法)、R 目标、N 的灵感。
5. **文献题目**:≤ 4 个,每个对准一个核心或灵感,问「文献里对类似的结构 / 特征做过哪些处理」,写成文献员能直接拿去搜的问题(中英文关键词都给)。

写到 ${P}/r${K}/analysis.md(中文,引用的表达式写原文)。`
}

function libPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '文献员')}

## 你的任务(文献员)

读 ${P}/r${K}/analysis.md 末尾的文献题目(以及它们对准的核心)。对每个题目用 WebSearch / WebFetch 查文献(这两个工具若还没加载,先用 ToolSearch 加载 "select:WebSearch,WebFetch")。
只用 **2023-08-08 之前发表**的论文、工作论文或研究报告(arXiv / SSRN 以首版日期为准);拿不准日期的不用。

对每个题目写:文献里这类结构 / 特征是怎么被构造和处理的,摘成**能翻译成我们算子语言的处理方式**,每条处理注明出处。
每个出处写:标题、作者、年-月、来源、链接、\`verified: true/false\`(true = 你这次确实在搜索结果或页面上看到了它)。**不得编造**;搜不到就写搜不到。

写到 ${P}/r${K}/lit.md。`
}

const MISSIONS_FORMAT = `
\`\`\`yaml
seed: <种子>
round: <轮>
slots:
  - type: E
    core: '<核心表达式:原样取自 loc.md 里某个 head 的子树(整个 head 也可以),或共性表 / 核心卡里的子树>'
    hypothesis: '<为什么它是 alpha 的来源;这次要试的外围处理是什么、实现的是什么机制、为什么和以前不一样、为什么样本外还会在>'
    literature: [{title: '...', authors: '...', year: 'YYYY-MM', url: '...', treatment: '<借用的处理>'}]
    seeds: ['<原样含核心的表达式>', ...]    # 8–16 个(审计会划掉一些;剩下少于 4 个这个位就不通过)
  - type: N
    hypothesis: '<新 idea:机制是什么、算子怎样实现它、为什么样本外还会在>'
    inspired_by: '<哪一批里的什么现象 / 哪篇文献>'
    literature: [...]
    seeds: ['...', ...]                      # 8–16 个
R:                                           # 可选
  - head: '<loc.md heads 表里的表达式原文>'
    why: '<哪个部件是烂的,依据>'
    variants: ['...', ...]
\`\`\``

function piPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, 'PI')}

## 你的任务(PI)

读 ${P}/r${K}/analysis.md、lit.md、loc.md,${P}/notebook.md 与之前各轮的 missions_final.yaml、audit_record.json(若有),以及规则 §2–§4。
决定本轮的 2 个 GP 任务位(各为 E 或 N)和可选的 R(至多 16 个变体)。**你的计划会交给独立审计员**按规则 §3 打创新度与合理度;
它看不到你的笔记和文献摘要,只看 missions.yaml —— 所以 hypothesis 要把机制、算子怎么实现它、为什么和库里已有的不同、为什么样本外还会在写清楚。

写 ${P}/r${K}/missions.yaml,格式:
${MISSIONS_FORMAT}

规则:每个核心整个实验至多 2 个 E 位;3 轮里至少 1 个 N 位通过审计;E 的种子必须**原样包含**核心;E 的外围要和快照里已经见过的写法很不一样;
种子里不用 ts_spearman 与 nt_*;文献年份早于 2023-08-08(2023 年的写到月)。种子用我们的算子语言写(参考 loc.md 里的表达式、${ROOT}/partura/ops_ext.py 与 AlphaCube 的算子源码)。

然后在 ${P}/notebook.md 末尾追加「第 ${K} 轮」一节(没有就新建):你目前对本种子 alpha 来源的信念;本轮每个任务的**事先预测**(会不会产出 heads、大致是什么、为什么);上一轮的预测对不对。

写完自己跑:\`${ENVSH} && ${PY} scripts/c06_check.py ${S} ${K}\`,不合格就改到合格;check_exit_code 填最后一次的退出码。`
}

function revisePrompt(S, n, finOut) {
  const P = `${D}/partura/s${S}`
  return `${place(S, 'PI')}

## 审计没有全部通过,重写(第 ${n} 次审计之后)

审计员的意见在 ${P}/r${K}/audit_${n}.yaml,相关度表在 ${P}/r${K}/corr_${n}.md。按规则 §3 执行审计结果的输出:
${finOut}

只重写**没有通过**的任务位(或 R 组):可以换核心、换 idea、换种子,也可以把 E 改成 N(反之亦然);通过了的位原样保留,不要改。
被划掉的种子不要原样再交;与某个 head |ρ| ≥ 0.7 或与某个控制 |ρ| ≥ 0.5 的会被自动划掉。写回 ${P}/r${K}/missions.yaml(同样的格式),
在 ${P}/notebook.md 本轮一节里补一句改了什么、为什么。写完跑 \`${ENVSH} && ${PY} scripts/c06_check.py ${S} ${K}\`,不合格就改到合格。`
}

function corrPrompt(S, n) {
  return `只做一件事:在终端跑下面这条命令(Bash 工具的 timeout 设 600000)。它每次最多等 8 分半钟:输出里有「STILL RUNNING」(退出码 3)就**再跑同一条命令**,
它会接着等同一个作业、不会重算;一直重复到退出码 0 或出现「CORR FAILED」为止(最多重复 12 次)。然后原样报告最后一次的退出码和输出。不读、不改任何其他文件。

\`bash ${ROOT}/scripts/c06_sync.sh corr ${K} ${S} ${n}\``
}

function auditPrompt(S, n) {
  const P = `${D}/partura/s${S}`
  const prev = n > 1 ? `\n- 你上一次的审计 ${P}/r${K}/audit_${n - 1}.yaml:看 PI 这次是否针对你的意见改了,还是换了说法没换内容。` : ''
  return `${place(S, '独立审计员')}

## 你的任务(独立审计员,第 ${n} 次审计)

你独立于 PI:**不读** ${P}/ 下的 analysis.md、lit.md、notebook.md(规则 §5)。你要读:
- ${D}/rules.md(尤其 §3 打分标准与 §4 已知陷阱);
- PI 的计划 ${P}/r${K}/missions.yaml;
- 相关度表 ${P}/r${K}/corr_${n}.md(细节在 corr_${n}.json):每个表达式与快照里每个 head、与 5 个控制的 |ρ|(train);
- 定位输出 ${P}/r${K}/loc.md:快照里的全部 heads(主 AlphaCube 的 + 本种子之前任务的)—— 这就是「已有因子库」,以及共性表与拆解;
- 之前各轮的 ${P}/r*/missions_final.yaml 与 audit_record.json(若有):以前试过什么、挡过什么;${prev}
- 看不懂的算子去读源码(${ROOT}/partura/ops_ext.py、$HOME/Desktop/AlphaCube-steering/src/alphacube/)。

对每个任务位判断:
- **创新度**(1–5):和库里已有的 head 比,是不是本质上不同的东西或实质性的改进?相关度表的数是证据之一,但低相关不等于新(换个控制变量的写法也可能和 head 都不相关)。
- **合理度**(1–5):这个机制说得通吗?算子组合真的实现了它吗(逐个算子核对)?窗口合理吗?有没有落进 §4 的陷阱?试下去样本外会不会好?
- 逐个看种子:哪些种子不符合这个位的 idea、是陷阱、或只是 head 的换皮,划掉(写 1 起的序号)。
- 对每个 R 组只评合理度。
分数要按 §3 的标准给,不要为了放行而凑 3 分,也不要为了显得严格而压分。

写 ${P}/r${K}/audit_${n}.yaml:

\`\`\`yaml
attempt: ${n}
slots:
  - slot: a                 # 第一个任务位 a,第二个 b
    novelty: <1-5>
    soundness: <1-5>
    struck_seeds: [<序号>, ...]
    reasons: '<打分的理由:引用相关度表、具体的 head、具体的算子>'
    revise: '<不通过时:哪里不行、怎么改才能过;通过时写「—」>'
  - slot: b
    ...
R:
  - head: '<R 组的 head 原文>'
    soundness: <1-5>
    reasons: '...'
summary: '<一句话>'
\`\`\``
}

function finalizePrompt(S) {
  return `只做一件事:在终端跑 \`${ENVSH} && ${PY} scripts/c06_check.py ${S} ${K} --finalize\`,原样报告退出码和完整输出。不读、不改任何其他文件。`
}

function checkPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '检查')}

## 你的任务(检查)

读 ${P}/r${K}/missions_final.yaml 与 lit.md:missions_final.yaml 引用的每条文献,年份是否早于 2023-08-08(违反的列进 lit_date_violations);
是否在 lit.md 里出现并标了 verified: true(没有的列进 lit_unverified)。再跑 \`${ENVSH} && ${PY} scripts/c06_check.py ${S} ${K}\`,记下退出码和输出。不改任何文件。`
}

function allPass(out) {
  return /^FINALIZED/m.test(out) && !/PLAIN GP/.test(out) && !/; R (\d+)\/(?!\1\b)\d+ groups/.test(out)
}

const results = await parallel(SEEDS.map(S => async () => {
  const tag = `c06r${K}s${S}`
  const anat = (K === 1 || (args.skip_anatomy || []).includes(S)) ? { skipped: true }
    : await agent(anatPrompt(S), { label: `${tag}:anatomy`, phase: 'Anatomy', model: M.anat, schema: ANAT_SCHEMA })
  if (!anat) return { seed: S, failed: 'anatomy' }
  const lib = (K === 1 || (args.skip_lit || []).includes(S)) ? { skipped: true }
    : await agent(libPrompt(S), { label: `${tag}:literature`, phase: 'Literature', model: M.lib, schema: LIB_SCHEMA })
  let pi = await agent(piPrompt(S), { label: `${tag}:pi`, phase: 'Plan', model: M.pi, schema: PI_SCHEMA })
  if (!pi) return { seed: S, failed: 'pi' }
  const audits = []
  let fin = null
  for (let n = 1; n <= MAX_AUDITS; n++) {
    let c = await agent(corrPrompt(S, n), { label: `${tag}:corr${n}`, phase: 'Audit', model: M.run, schema: RUN_SCHEMA })
    if (!c || c.exit_code !== 0) c = await agent(corrPrompt(S, n), { label: `${tag}:corr${n}-retry`, phase: 'Audit', model: M.run, schema: RUN_SCHEMA })
    if (!c || c.exit_code !== 0) return { seed: S, failed: `corr ${n}`, corr: c, audits }
    const aud = await agent(auditPrompt(S, n), { label: `${tag}:audit${n}`, phase: 'Audit', model: M.audit, schema: AUDIT_SCHEMA })
    if (!aud) return { seed: S, failed: `audit ${n}`, audits }
    audits.push(aud)
    fin = await agent(finalizePrompt(S), { label: `${tag}:finalize${n}`, phase: 'Finalize', model: M.run, schema: RUN_SCHEMA })
    if (!fin || fin.exit_code !== 0) return { seed: S, failed: `finalize ${n}`, fin, audits }
    log(`种子 ${S} 第 ${n} 次审计:${fin.output.split('\n').find(l => l.startsWith('FINALIZED')) || fin.output.slice(0, 200)}`)
    if (allPass(fin.output) || n === MAX_AUDITS) break
    pi = await agent(revisePrompt(S, n, fin.output), { label: `${tag}:pi-revise${n}`, phase: 'Plan', model: M.pi, schema: PI_SCHEMA })
    if (!pi) return { seed: S, failed: `revise ${n}`, audits }
  }
  const chk = await agent(checkPrompt(S), { label: `${tag}:check`, phase: 'Finalize', model: M.run, schema: CHECK_SCHEMA })
  const ok = !!chk && chk.lit_date_violations.length === 0 && !!fin && fin.exit_code === 0
  return { seed: S, admissible: ok, n_audits: audits.length, final: fin && fin.output, check: chk, audits: audits.map(a => ({ slots: a.slots, R: a.R, summary: a.summary })) }
}))
return { round: K, results }
