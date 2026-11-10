# W02L 交接(接手先读这个，再读 PROGRESS.md 最上面一节)

更新于 2026-11-09 22:30 EST(服务器 11-10 11:30)。

## 现在在哪

- **第 0 步**(服务器自己在跑，不用管):已打分 3282 / 5583 条，错误 0,过闸门 2513;A 下 head 6 个,B 下 0 个。`bash scripts/w02l_status.sh`(服务器)看进度。
- **流**:已建 48 / 80 条;已结束 31 / 240 个流-轮;新 head 17 个(B 下 ≥ 0.5、|ρK| < 0.5),详见服务器 `research/prod_W02L/report.md`(本机有拷贝)。
- **GP 任务**:已推送的流-轮在服务器 `prod_conductor` 里排队 / 运行(3 路显卡，中位 27 分钟一次搜索)。服务器自己跑，不用管。

## 本机流水线里正在半路的(如果会话断了，按这个补)

| 轮 | 流 | 停在 | 补的办法 |
|---|---|---|---|
| 1 | 2044 2045 2046 2047 2049 | 相关度表在算(PI 已过 c06_check) | `prod_round.sh corr 1 "2044 2045 2046 2047 2049"` |
| 2 | 2007 | 相关度表在算(最慢) | `PROD_HOSTS=research/prod_W02L/hosts.json PROD_ENV=w02l bash scripts/prod_round.sh corr 2 "2007"`(服务器上已起的会自己算完，再跑一次只是取回) |

每个流拿到 `partura/s<流>/r<k>/corr_1.md` 以后:工作流 stage `audit`,然后 `prod_round.sh finish <k> "<流>"`。
工作流:`w02l-round.js`,args `{round: k, seeds: [数字, ...], stage: "pi" | "audit"}`,**seeds 要传数字**。PI 用 Sonnet 5.5,审计用 Haiku 5.5。
每批的 token 记到 `TOKENS.md`。

然后循环:`bash scripts/w02l_pending.sh` 列出新 READY 的流 → `prod_round.sh fetch` → PI → corr → audit → finish。

## 第 0 步结束以后

1. `--spearman-only` 补算 30 条 `ts_spearman`;
2. 重跑 MAKEUP.md 里的搜索;
3. 建剩下 32 条流;
4. 全部轮次结束后建 W02L 库，按 PLAN §7:两层合成并集 vs C(L∪X),拟合到 2025-12-31,test 2026 只读一次并记账;
5. 写 RESULT.md。

## 等用户定的

1. head 规则加第二判据：残差 ρ 或尺子 D(D = B + 市值 / 流动性 / 价位十分位哑变量，2028 阶跃带在 D 下 −3.66)。
2. 加第 0 步进程。
3. GP 分钟维度的设计改动。
4. AlphaCube「所有限制」那一批。
5. 省 token:第 3 轮只做前两轮有起色的流；审计只在用了 E 位或 R 组时做。
   - 现在每个流-轮约 50 万 token,累计约 3,500 万。

## 规矩(用户定的，别破)

- 服务器上文件只能放在 `c02_partura` 和 `bkxehsw` 里。
- 不杀不是自己起的进程。
- 2026 test 只按预先写好的规则读一次。
