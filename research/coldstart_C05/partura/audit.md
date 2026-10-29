# C05 Partura 隔离审计(按会话记录;scratchpad 里的 audit_c05.py)

| 轮 | workflow | 命中 | 判断 |
|---|---|---|---|
| 1 | wf_dc2ca335(805、807) | 2 | 误报:805 解剖员写进 analysis.md 的文字里提到 `guidance/C05_base.yaml`(原话是「按规矩没有读」),不是读取 |
| 1 | wf_f88075ab(801、803) | 4 | 803 的 2 处是同样的误报(写入内容里的文字)。**801 解剖员真的读了 `guidance/C05_base.yaml`**(grep 与 head -40):提示禁的是 guidance/ 下所有 C0 开头的文件,本意是挡 C01–C04 的设计;C05_base 是环境的基准定义(已知族、奖励),不含任何结果。照实记为一次轻微越界 |
| 1 | wf_a9dae9f2(806、808) | 0 | — |
| 1 | wf_ccce5e8c(801 重跑文献员与 PI) | 0 | — |
