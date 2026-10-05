# 07_S0_baseline — S0_baseline 阶段事实记录(工单 R3 补写)

来源:`runs/F106_erm_mag_gap_1m/S0_baseline.json`(10-04 11:50,exit 0,220.0s,splits `['train','valid','utrain']`,只有 1 个变体 `v_base`)。
本文件只记事实,**不下结论**(解读见 `09_diagnosis.md` A2)。`S0_baseline` 不是 final 阶段,没有触发留出段读取,JSON 里没有 `holdout` 字段 —— 这是预期行为,不是遗漏。

## 问题(配置里 S0_baseline 阶段的 question)

> Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?

## 1. v_base 两套书

### 1a. 决策口径(`books`;方向/半衰期在 train 上拟合;报 train / valid)

| sgn | hlL | Lnet tr | Lnet va | Lshp tr | Lshp va | Lgross tr | Lgross va | LTO | hlS | LS tr | LS va | short tr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| − | 20 | −6.9% | −3.2% | −2.15 | −1.23 | −5.1% | −1.8% | 2.4% | 20 | +2.82 | +3.24 | +27.9% |

固定半衰期扫描(train,`books.sweep`):

| hl | Lnet | Lshp | LTO |
|---|---|---|---|
| 0 | −67.2% | −19.51 | 88% |
| 2 | −32.5% | −9.93 | 37% |
| 5 | −18.5% | −5.82 | 17% |
| 10 | −10.6% | −3.26 | 7% |
| 20 | −6.9% | −2.15 | 2% |

### 1b. 用户口径(`books_user`;方向/半衰期在 utrain 上拟合;报 utrain / holdout——holdout 本阶段未算)

| sgn | hlL | Lnet utr | Lnet ho | Lshp utr | Lshp ho | Lgross utr | Lgross ho | LTO | hlS | LS utr | LS ho | short utr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| − | 20 | −5.8% | **—(未算)** | −1.91 | **—** | −4.2% | **—** | 2.2% | 20 | +2.91 | **—** | +26.3% |

## 2. cov / dist

rIC(原始日频面板):train +0.0067、valid +0.0027。rICtraded(平滑后交易信号):train +0.0165、valid +0.0086。
**cov = 1.00、dist = 0.99**(两道门槛都过;这里的 cov 是 train/valid 范围内的面板覆盖率,数值上与 `S_final` 的 holdout cov 0.9675 不同,
是因为统计的 split 不同,不是矛盾,见 `08_variants.md` §2)。

## 3. 分位超额 Q1..Q10(Q10 = 多头端)

| split | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|---|---|---|---|---|---|---|---|---|---|---|
| train | −28.4% | +0.1% | +3.5% | +2.0% | +4.7% | +6.6% | +7.9% | +5.9% | +3.2% | −5.3% |
| valid | −22.7% | +3.5% | +10.2% | +2.6% | +2.6% | +5.4% | +1.3% | −1.2% | +0.1% | −1.8% |

倒 U,两端(Q1、Q10)都明显弱于中段。

## 4. 逐年(`by_year`,utrain 范围内,2018–2023;本阶段非 final,没有 2024/2025)

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|
| Lnet | −9.2% | −6.2% | −8.6% | −4.1% | −0.8% | −7.4% |
| LS | +1.82 | +4.17 | +3.25 | +2.33 | +3.22 | +3.31 |

六年 Lnet 全负。

## 5. 核对:`S0_baseline/v_base` 与 `S_final/f_orig` 是不是同一本书

**是**。两处是同一个表达式在两次运行里各算一次,train/valid 的全部数字(1a 表、固定半衰期扫描、分位剖面、逐年 2018–2023)**逐项相同**
(对照 `07_S_final.md` §2a/§3a/§6/§7 的 f_orig 行),cov/dist 在 train/valid 范围内也相同(1.00/0.99)。
`S0_baseline` 的 utrain 行(Lnet +… / Lshp … / LS +2.91 / short +26.3%)与 `S_final` 的 f_orig utrain 行逐项相同。
没有发现不一致。

## 解读

原样对纯多头用户不可用,且不是成本问题(半衰期网格 {0,2,5,10,20} 上每一点毛/净全负)。判断全文见 `09_diagnosis.md` A2。

## 原始输出在哪

- `./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- `runs/F106_erm_mag_gap_1m/S0_baseline.json`
- （该阶段还有中性化、已知家族自比较、条件 IC、衰减等输出,工单未要求逐项抄录,`digest` 命令可查全文,未在本文件重复。）
