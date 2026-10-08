# 新版 AlphaCube(`partura-steering` @ `155ce38`)在服务器上的验收(2026-10-07 19:36 PDT)

## 放在哪

- 新引擎**并排**放在 `/root/autodl-tmp/Partura/vendor/AlphaCube-steering/`(`src/`、`scripts/`、`tests/`、`VERSION`),没有覆盖 `/root/autodl-tmp/AlphaCube`。
  服务器上现有的那份 `src/` 和本机基线 `517fd09` 逐字节相同(`rsync -rcn` 无差异)。
- 用新引擎的方式:`PYTHONPATH=<vendor>/src:<Partura> ALPHACUBE_ROOT=<vendor>`;数据路径(`mirror`、`_bench`)仍是原来的绝对路径,不受影响。
- 日频库:`/root/autodl-tmp/Partura/daily_fields/`(`FloatCap`、`TotalCap`、`FloatShares` 三个 (5220, 2114) 的 float64 平面,各 88 MB;建库 14 秒)。
  来源 `qmt_daily_data/daily_capital/<日期>.parquet`,列 `circulating_market_value` / `total_market_value` / `circulating_capital`;有限覆盖 82.9% / 82.9% / 83.3%(未上市、已退市的格子为空;
  停牌日有股本没有市值)。挂上之后九个字段都可用(另有派生的 `LimitWidth`、`BoardCode`、`ListAge` 和三个 `Log*`)。核对:000001.SZ 2026-09-16 流通市值 2270 亿 ÷ 流通股本 194 亿 = 11.70 元。

## 本机(CPU,合成数据)

子代理在最终提交上重跑:基线对基线 14/14 相同;基线对新分支 12/14 相同,另两个只差「新分支多出来的属性」那份报告;附加检查 30/31(差的是故意改的那一处);真 CLI 7/7。
测试 966 passed / 10 skipped / 1 xfailed(总领自己又跑了一遍,同数)。

## 服务器(GPU,`scripts/server/ac_accept/run.sh`;报告在本目录)

| 阶段 | 比什么 | 结果 |
|---|---|---|
| `self` | 旧对旧,合成数据(对照) | 14 / 14 相同 |
| `cross` | 旧对新,合成数据:GP 4 种适应度 × 2 个种子、RL 3 次、表达式求值、生成器随机流、注册表 | 12 / 14 相同;`generator`、`registry` 只差 `additive_surface.json`(新分支才有的属性) |
| `extra_self` / `extra` | 带封禁、滚动块的运行 | 5 / 5;4 / 5(差的是 `rl_banned_typo_seed0`:RL 路径上永远匹配不上的封禁键由静默忽略改为报错,故意的) |
| `prod_self` | 旧对旧,**生产库**(对照) | 5 / 5 相同 |
| `prod` | 旧对新,**生产库**:数据身份(`contract_hash` 6a0acbd1…)、B01 的 15 条原式 + 5 条已知族在 2025-01 ~ 03 全市场上的面板、GP(rank_ic 种子 0、long 种子 1)、RL(alphagen) | 4 / 5 相同;`prod_identity` 只差 `additive_surface.json`(`daily` 属性:没有 / None) |

- 第一遍(`report_*_run1.json`、`logs/server/_ac_accept_run1.log`)里有三个 GP 任务报「不同」,差的只是进度行里的内存读数(`cg 37/90G` 对 `38/90G`,别的租户的作业在动);
  对照组里同样出现。日志过滤加上这一项之后重跑,全部相同。结果文件(存档 CSV、成员、因子值、合成值)两遍都逐字节相同。
- **重放一次存档的搜索**:e7c1(对照臂,种子 1,预算 192)用新引擎重跑(`episodes/acc7c1_I5_within_bucket_anything`):78 个候选,表达式、顺序、每一个分数全部相同;
  付费评估 110、没过门槛 32 也相同。

## 走正式钩子的搜索(2026-10-07 20:15 PDT;Partura `main` @ `cd926a3`,已并入 `ac-plugin`)

`scripts/idea_search.py` 现在通过 `partura/ac_plugin.py`(`load_plugins` + `SearchHooks` + 注册的打分器)指引搜索,不再给 AlphaCube 打猴子补丁。
用新引擎、新路线把两次存档的运行在新标签下重跑,再用 `scripts/plugin_acceptance.py` 逐候选比对:

| 重跑 | 对着 | 结果 |
|---|---|---|
| `e7cx1`(对照臂,种子 1,预算 192) | `e7c1` | 相同:78 个候选,付费评估 110,没过门槛 32 |
| `e7bx1`(只开先验的一臂,种子 1) | `e7b1` | 相同:80 个候选,付费评估 143,没过门槛 38;提议 521、接受 237、被先验抽掉 277、封禁 4、近亲 3、变异被拒 7 —— 每一项计数都一样 |

本机(CPU、合成数据)另有 21 对运行、34 个臂的比对全部相同(六个想法、五种奖励、各种 `--parts` 组合)。
分支上原有的两处会挪动随机抽取的改动(`in_sustain` 三个算子声明为实值、指引权重也作用到 `nt_` 孪生体)改成了默认关闭,要用时设 `PARTURA_AC_FIXES`,并且会记进证据文件。
已知的一处不等价:生成器连续 64 次被拒之后的回退路径,新引擎会再问一遍筛子(概率约 5e-6 / 次,本机和这两次重跑都没有碰到)。

## 结论

不传新参数时,新引擎在本机 CPU、服务器 GPU、合成数据、生产库上都和现在这份逐字节一致;唯一故意的差别是 RL 路径对无效封禁键报错。

## 还没做的(要用户点头)

- 把 `partura-steering` 并入 AlphaCube 的 `main` / `tradable-backtest` 并推到 GitHub。
- 用新引擎替换服务器上的 `/root/autodl-tmp/AlphaCube/src`(现在两份并排,Partura 用 vendor 那份,别的作业不受影响)。
