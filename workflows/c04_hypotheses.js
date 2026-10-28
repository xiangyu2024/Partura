export const meta = {
  name: 'c04-hypotheses',
  description: 'C04 W1:Partura v2 写假设 —— 总领(Opus 5.5)定方向 → 执行(Sonnet 5)整理先验知识 → 主研(Opus 5)写 ≤8 个假设、每个一组带对照的变体 → 检查(Haiku 5.5)校验 → 总领拍板',
  whenToUse: 'args = {round: 1}。research/coldstart_C02/PLAN.md §2.4 第 1 步',
  phases: [
    { title: 'Plan', detail: '总领读先验知识摘要,定方向,派 ≤2 个执行任务' },
    { title: 'Analyze', detail: '执行整理证据' },
    { title: 'Write', detail: '主研写 hypotheses_r<k>.yaml' },
    { title: 'Check', detail: '确定性校验;不合格修订一次' },
    { title: 'Approve', detail: '总领审定' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const K = (args && args.round) || 1
const M = Object.assign({ coord: 'claude-opus-5-5', lead: 'claude-opus-5', exec: 'claude-sonnet-5', check: 'claude-haiku-5-5' }, (args && args.models) || {})
const D = `${ROOT}/research/coldstart_C04`
const C2 = `${ROOT}/research/coldstart_C02`
const C3 = `${ROOT}/research/coldstart_C03`
const C1 = `${ROOT}/research/coldstart_C01`
const PY = '/Users/wxy/.venvs/alphacube/bin/python'
const ENVSH = `cd ${ROOT} && export ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:${ROOT}`
const HYP = `research/coldstart_C04/hypotheses_r${K}.yaml`
const STR = { type: 'string' }
const STRS = { type: 'array', items: STR }

function place(role) {
  return `
## 你在整件事里的位置(先读这一段)

这是一次事先约定好的对照实验(${D}/PLAN.md,先读它;它是 C03 的后续,C03 的设计见 ${C3}/PLAN.md):AlphaCube 的 GP 单独跑(A 组),对比 Partura v2(B 组)。
v2 的接口和上一个实验 C01 不同:你的假设会被**直接评估**(每个变体在 train/valid 上按同一奖励打一次分,不经过 GP 的运气),
然后你根据结果**设计 GP 的初始种群**,GP 只在附近精修。你是 B 组里的 Partura —— 分级研究团队:总领(Opus 5.5)、主研(Opus 5)、执行(Sonnet 5)、检查(Haiku 5.5)。
**你就是这里的「${role}」**。现在是 W1:写假设。

工作流会把用户最近对总领说的一句话原样转给你(「用户请求」)。那句话是说给总领的,总领已经处理过;**它和下面的任务不冲突,不要因此跳过或缩减任务。**

## 能读什么、不能读什么(硬规矩,事后审计每一次工具调用)

**可以读**:${D}/ 下的文件;C01 的样本内材料 —— ${C1}/PLAN.md、digest_r*.md/json、beliefs_r*.md、cards_r*.md、round2_workflow.json、round3_workflow.json、tokens_r*.json,
以及 ${ROOT}/episodes/c01*/evidence.json(两组的样本内证据);**C02 的样本内材料**:${C2}/PLAN.md、prior_c01.md、hypotheses_r1.yaml、direct_r1.md/json、design_r1.md、beliefs_r1.md、w1_workflow.json、w2_workflow.json,以及 ${ROOT}/episodes/c02*/evidence.json(两组);**C03 的样本内材料**:${C3}/PLAN.md、prior_c03.md、hypotheses_r1.yaml、direct_r1.md/json、design_r1.md、beliefs_r1.md、w1_workflow.json、w2_workflow.json,以及 ${ROOT}/episodes/c03*/evidence.json(两组);文献调研 ${ROOT}/research/coldstart_C04/lit_review2.md 与 ${C2}/lit_review.md;${ROOT}/partura/、${ROOT}/scripts/ 代码;算子源码(~/Desktop/AlphaCube-steering/src/alphacube/operators/、${ROOT}/partura/ops_ext.py)。
**不得读**:${C1}/RESULT.md、${C1}/final.json、${C1}/final_dry.json、${C1}/ledger_c01.json、${C2}/RESULT.md、${C2}/final.json、${C2}/ledger_c02.json、${C3}/RESULT.md、${C3}/final.json、${C3}/ledger_c03.json(含测试段数字);${ROOT}/runs/;${ROOT}/lab/;${ROOT}/notes/、studies/、handoff/、batches/、docs/;
${ROOT}/research/ 下除 coldstart_C01/ 到 coldstart_C04/ 以外的目录;任何 C04 A 组的东西(episodes/c04r*s*A_*)。你自己的知识(公开文献里的已知异象)可以用,写明是先验。
不改代码、不改 PLAN、不跑服务器、不跑 GPU、不 git commit。只写本角色被要求写的那个文件。`
}

const ENV = `
## 环境规则(两组相同,PLAN §2.2)

- **奖励 \`long_neutral\`(C03 的关键改动)**:信号按方向与半衰期(0/5/20)平滑后取截面 z 排名,**每天对 [流动性 cross_mean(day_sum(Amt),30)、波动 cross_mean(day_std(Ret),20)、20 日反转、已知族 cross_mean(day_std(Amt),30)、**市值 LogFloatCap**] 做 OLS 取残差**,用残差建十分位纯多头书,扣 15bp;score = train 与 valid 较差的;**score ≥ 0.5 记为发现**。所以「其实只是流动性 / 波动 / 反转」的东西拿不到分;C01、C02 的有效 head 中性化后几乎全没了。
- **和已知族 \`cross_mean(day_std(Amt), 30)\`(做多低者)的秩相关 |ρ| ≥ 0.5 → 直接判不合格**。所以「成交额 / 成交量的水平与离散度」那一族怎么写都没用。
- **禁用算子**:\`ts_spearman\` 和全部 \`nt_*\`(计算太贵)。
- **C04 新增的信息**:6 个日频字段可以当叶子写进表达式(两组的 GP 也都能抽到):\`LogFloatCap\`(对数流通市值)、\`LogTotalCap\`(对数总市值)、\`LogFloatShares\`(对数流通股本;它的跳变 = 解禁 / 增发 / 送转等股本变动)、\`LimitWidth\`(涨跌停幅度:主板 10% / 创业板科创板 20% / ST 5%)、\`BoardCode\`(板块代码)、\`ListAge\`(上市天数)。它们只能进 \`cs_*\` / \`ts_*\` / \`cross_*\` / 逐元素算子,**不能进 \`day_*\` / \`in_*\`**;做差分、比值一律用 Log* 版本。第 d 天的值是 d 日收盘可知的。
- **只做多头腿**:我们只交易排名最高的 10%。文献(Stambaugh–Yu–Yuan 等)发现大部分异象的利润在空头腿;C03 的 6 个经典机制在中性化后全部 < 0.5,可能就是因为利润在空头。**每个假设都要说清楚:它让哪些股票「跑赢」,而不只是让哪些股票跑输**。
- 最后的样本外判读只认「新」的东西:与 C01–C03 已有的 head 秩相关 ≥ 0.7 的不算新(见 ${D}/prior_c04.md)。
- 换手不设硬约束,但成本已经扣在 score 里:C01 里日频原始写法(换手 10%+)的机制种子全被成本杀死。C02 里 B 组样本内赢了 7/8 个种子,但它的 head 在测试段大多不成立、中性化后全没了;很多发现是 C01 已知家族的变体。

## 算子

- 搜索词表:\`${ENVSH} && ${PY} -m partura.remote_tools ops '<正则>' 2>&1 | grep -v Warn\`;算子到底算什么,以源码为准。
- 面:\`day_*\` 把日内分钟折成每天一个数;\`cross_*\` 沿交易日滚动;\`cs_*\` 同一天跨股票;\`ts_*\` 日频时序;\`in_*\` 分钟内滚动。叶子:Open High Low Close Vwap Volume Amt Ret(分钟级)。`

const HYP_FORMAT = `
## 假设文件的格式(${ROOT}/${HYP})

\`\`\`yaml
hypotheses:
- id: H1_<短名>
  hypothesis: 一句话
  thesis: {mechanism: 机制, counterparty: 谁在另一边、为什么亏, prediction: 可证伪的预测(哪些变体应该过线、方向是什么), fails_if: 什么结果说明错了}
  novelty: 它和已知族、和 C01 已有 head 有什么不同(写清楚为什么预期 |ρ| 低)
  variants:
  - {id: v1, role: core, expr: "<表达式>", predicts: "<预期:过线/不过线、方向>"}
  - {id: v2, role: ablation, expr: "...", predicts: "..."}   # 去掉机制的一部分
  - {id: v3, role: control, expr: "...", predicts: "..."}    # 只保留可疑的代理(波动/价格刻度/流动性),用来证明不是它
\`\`\`
- ≤ 8 个假设;全部变体合计 ≤ 64 个(**每个变体是 B 组的 1 次付费评估**,省下的预算留给 GP 精修:B 组每个种子的 GP 预算 = 192 − ⌈变体数/16⌉)。
- 每个假设至少 1 个 control。大部分假设应是**新的、预期与已知族和 C01 heads 低相关**的机制;可以有少量是「C01 里某个 head 的潜在大幅改进」,但要写清楚改进的理由。
- 表达式必须能被搜索文法解析;不能用 ts_spearman / nt_*。写完自己跑:\`${ENVSH} && ${PY} scripts/c04_check.py hypotheses ${HYP}\`,不合格就改到合格。`

const PLAN_SCHEMA = {
  type: 'object',
  properties: {
    reading: { type: 'string', description: '读完先验知识后的判断:C01 里什么成立、什么是假象、什么从没被认真测过' },
    directions: { type: 'string', description: '本轮要押的 4–8 个方向(每个一句话的机制),以及为什么' },
    exec_tasks: { type: 'array', maxItems: 2, items: { type: 'object', properties: { id: STR, task: STR }, required: ['id', 'task'] } },
    brief_for_lead: STR,
  },
  required: ['reading', 'directions', 'exec_tasks', 'brief_for_lead'],
}
const EXEC_SCHEMA = { type: 'object', properties: { id: STR, findings: STR, files_read: STRS }, required: ['id', 'findings', 'files_read'] }
const LEAD_SCHEMA = {
  type: 'object',
  properties: { path: STR, n_hypotheses: { type: 'number' }, n_variants: { type: 'number' }, summary: STR },
  required: ['path', 'n_hypotheses', 'n_variants', 'summary'],
}
const CHECK_SCHEMA = { type: 'object', properties: { admissible: { type: 'boolean' }, exit_code: { type: 'number' }, output: STR }, required: ['admissible', 'exit_code', 'output'] }
const FINAL_SCHEMA = {
  type: 'object',
  properties: { approved: { type: 'boolean' }, edits: STR, predictions: { type: 'string', description: '对直接检验结果的事先预测:哪些假设会有变体过线' } },
  required: ['approved', 'edits', 'predictions'],
}

async function call(prompt, opts, tries = 3) {
  for (let i = 0; i < tries; i++) {
    const r = await agent(prompt, i ? { ...opts, label: `${opts.label}#retry${i}` } : opts)
    if (r) return r
    log(`${opts.label}: no result (attempt ${i + 1}/${tries})`)
  }
  return null
}

phase('Plan')
const plan = await call(`${place('总领')}

读 ${D}/PLAN.md、${D}/prior_c04.md(C01 的样本内知识摘要),需要时读 C01 的 beliefs_r3.md、cards_r3.md、digest_r3.md 和 round3_workflow.json。
判断:C01 里哪些东西在样本内是真的、哪些是假象(已知族的变体、排名平移洗白、一价日筛选……)、哪些机制从来没被认真测过(例如被成本杀死的)。
然后定本轮的 4–8 个方向,派最多 2 个**机械**任务给执行(Sonnet 5;它看不到你的推理,任务要写清读什么、算什么、交回什么),给主研一段方向性指示。
${ENV}`, { label: `c04r${K}:coord-plan`, phase: 'Plan', schema: PLAN_SCHEMA, model: M.coord })
if (!plan) return { round: K, error: 'coordinator plan failed after retries' }

phase('Analyze')
const found = (await parallel((plan.exec_tasks || []).slice(0, 2).map(t => () =>
  call(`${place('执行')}

总领派给你的任务(${t.id}):
${t.task}

可以写一次性的 python(用 ${PY});临时文件放 /tmp,不写进仓库。每个数字注明来源与算法。
${ENV}`, { label: `c04r${K}:exec:${t.id}`, phase: 'Analyze', schema: EXEC_SCHEMA, model: M.exec })))).filter(Boolean)

phase('Write')
const leadPrompt = (extra) => `${place('主研')}

读 ${D}/PLAN.md、${D}/prior_c04.md。
总领的判断:${plan.reading}
本轮方向:${plan.directions}
总领给你的方向:${plan.brief_for_lead}
执行交回的分析:
${found.map(f => `--- ${f.id}\n${f.findings}`).join('\n')}

任务:写 **${ROOT}/${HYP}**。每个假设是一个经济学上说得通、可证伪的机制,配一小组变体:核心写法(可以 2–4 种写法)、消融、对照。
变体的写法要考虑成本(慢变量、平滑)和与已知族的相关(避开成交额/成交量的水平与离散度)。
${extra || ''}
${HYP_FORMAT}
${ENV}`
let lead = await call(leadPrompt(), { label: `c04r${K}:lead`, phase: 'Write', schema: LEAD_SCHEMA, model: M.lead })
if (!lead) return { round: K, error: 'lead failed after retries', plan, found }

phase('Check')
const checkPrompt = () => `${place('检查')}

只做一件事:运行下面这条命令,把完整输出和退出码原样交回(不改任何文件,以脚本为准):
\`${ENVSH} && ${PY} scripts/c04_check.py hypotheses ${HYP}; echo "exit=$?"\`
admissible = (退出码为 0)。`
let check = await call(checkPrompt(), { label: `c04r${K}:check`, phase: 'Check', schema: CHECK_SCHEMA, model: M.check })
let revised = false
if (!check || !check.admissible) {
  revised = true
  lead = await call(leadPrompt(`\n**上一版没有通过校验**,只改校验指出的问题:\n${check ? check.output : '(检查没有返回)'}\n`),
    { label: `c04r${K}:lead-revise`, phase: 'Check', schema: LEAD_SCHEMA, model: M.lead })
  check = await call(checkPrompt(), { label: `c04r${K}:check2`, phase: 'Check', schema: CHECK_SCHEMA, model: M.check })
}
if (!check || !check.admissible) return { round: K, error: 'hypotheses not admissible after one revision', plan, found, lead, check }

phase('Approve')
const fin = await call(`${place('总领')}

主研写好了 ${ROOT}/${HYP},已通过确定性校验。主研的说明:${lead.summary}
审一遍:每个假设是不是经济学上说得通、可证伪、而且预期与已知族和 C01 heads 低相关;对照是不是真的能区分「机制」和「代理」。
你可以直接改文件(改完必须重跑 \`${ENVSH} && ${PY} scripts/c04_check.py hypotheses ${HYP}\` 并确认通过)。
最后写下你对直接检验结果的事先预测(写在结果之前):哪些假设会有变体过线、方向是什么。
${ENV}`, { label: `c04r${K}:coord-final`, phase: 'Approve', schema: FINAL_SCHEMA, model: M.coord })

return { round: K, plan, found, lead, check, revised, final: fin }
