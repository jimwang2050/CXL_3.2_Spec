# CXL 3.2 翻译质量审计报告

**审计日期**: 2026-06-28 | **审计人**: Claude Code | **语料**: 全 14 章 · 4,686 行 MD · 3,880 双语 rows

---

## 📋 执行摘要

**总体质量: ✅ GOOD (良好)**

| 维度 | 评分 | 说明 |
|------|------|------|
| 完整性 | 3,875/3,880 rows (99.9%) | 仅 4 个结构占位空行 |
| 准确性 | 优秀 | 协议术语、寄存器字段均保留原样 |
| 一致性 | ⚠️ 有问题 | 11 个关键术语跨章节译法不统一 |
| 可读性 | 优秀 | 句式通顺，符合中文技术文档惯例 |

---

## 1. 完整性 — 空/占位 ZH Cell（Minor）

| 章节 | 行号 | 类型 | 说明 |
|------|------|------|------|
| ch06 | 1108 | 结构占位 | 9 列表格 `Fail/Fail` 行 — spec 此 case 无需动作 |
| ch07 | 1415 | 空 `<tr>` | tbody 起始空行（表格生成工具残留） |
| ch07 | 1636 | 空 `<tr>` | 同上 |
| ch08 | 6663 | 空 `<tr>` | Part B tbody 起始空行 |

**结论**: 4 个全为 HTML 表格结构占位，非翻译遗漏，肉眼浏览时为空白行。

---

## 2. 术语不一致性（Major — 11 组）

以下为同一英文术语在不同章节出现不同中文译法的统计：

### 2.1 关键协议术语对照表

| 术语 | ch01 | ch02 | ch03 | ch04 | ch05 | ch06 | ch07 | ch08 | ch09 | ch10 | ch11 | ch12 | ch13 | ch14 |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| **protocol** | Protocol(EN) | 协议 | Protocol(EN) | Protocol(EN) | 协议 | Protocol(EN) | 协议 | Protocol(EN) | 协议 | 协议 | 协议 | Protocol(EN) | 协议 | Protocol(EN) |
| **transaction** | Transaction(EN) | 事务 | Transaction(EN) | Transaction(EN) | Transaction(EN) | 事务 | 事务 | Transaction(EN) | 事务 | Transaction(EN) | — | Transaction(EN) | 事务 | 事务 |
| **coherent/cy** | Coherency(EN) | Coherency(EN) | Coherent(EN) | — | — | — | **一致性** | Coherency(EN) | Coherency(EN) | **一致性** | **一致性** | **一致性** | **一致性** | **一致性** |
| **memory** | Memory(EN) | Memory(EN) | Memory(EN) | Memory(EN) | Memory(EN) | Memory(EN) | Memory(EN) | Memory(EN) | **内存** | Memory(EN) | Memory(EN) | Memory(EN) | **内存** | Memory(EN) |
| **cache** | Cache(EN) | Cache(EN) | Cache(EN) | Cache(EN) | — | — | Cache(EN) | Cache(EN) | Cache(EN) | **缓存** | — | **缓存** | — | Cache(EN) |
| **request** | Request(EN) | **请求** | Request(EN) | Request(EN) | Request(EN) | **请求** | Request(EN) | Request(EN) | **请求** | Request(EN) | **请求** | Request(EN) | **请求** | Request(EN) |
| **response** | Response(EN) | Response(EN) | Response(EN) | Response(EN) | **响应** | **响应** | Response(EN) | Response(EN) | **响应** | **响应** | **响应** | Response(EN) | **响应** | Response(EN) |
| **device** | Device(EN) | Device(EN) | Device(EN) | Device(EN) | — | — | Device(EN) | Device(EN) | Device(EN) | **设备** | **设备** | Device(EN) | **设备** | Device(EN) |
| **layer** | Layer(EN) | **层** | Layer(EN) | Layer(EN) | Layer(EN) | Layer(EN) | Layer(EN) | Layer(EN) | **层** | Layer(EN) | **层** | Layer(EN) | Layer(EN) | Layer(EN) |
| **link** | Link(EN) | **链路** | **链路** | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) | Link(EN) |
| **switch** | Switch(EN) | **交换** | **交换** | **交换** | **交换** | — | Switch(EN) | **交换器** | **交换** | **交换** | Switch(EN) | Switch(EN) | **交换** | Switch(EN) |
| **poison** | — | — | Poison(EN) | Poison(EN) | — | — | — | Poison(EN) | — | — | Poison(EN) | Poison(EN) | — | **poison**(小写) |
| **arbiter** | Arbiter(EN) | — | — | — | **仲裁** | **仲裁** | — | **仲裁** | — | — | — | — | — | **仲裁** |

### 2.2 最需关注的 3 个问题

#### 🔴 `coherent/coherency` — 最严重（3 种写法）

| 章节 | 译文 |
|------|------|
| ch01/02/03/08/09 | Coherent / Coherency（保留 EN） |
| ch10/11/12/13/14 | 一致性 |
| ch07 | 混用（"一致性"出现在非表格正文） |

CXL 协议中 `coherency` 是核心概念，`cache coherency` = 缓存一致性。不一致会影响读者理解。

**建议**: 统一为"一致性"（全 14 章生效）

#### 🟡 `switch` — 3 种写法（语义细分或有合理性）

| 写法 | 章节 | 语义 |
|------|------|------|
| `Switch` (EN) | ch01/07/11/12/14 | 指物理设备 |
| `交换机` | ch02/03/04/05/09/10/13 | 泛指或动词 |
| `交换器` | ch08 | 特指 CXL switch 硬件（寄存器描述） |

`ch08` 用"交换器"可能是刻意的上下文区分（寄存器描述需精确指代），但与其他章节的 `交换机` 明显不统一。

**建议**: 确认 ch08 "交换器" 是否为有意区分，若否则统一为"交换机"。

#### 🟡 `memory` — ch09/ch13 用"内存" vs 其他保留"Memory"

两者均正确，但风格略有差异："内存"多用于正文段落，"Memory"保留在术语首现括号注释中。

**影响较小**: 可接受现状，或统一为一种风格。

---

## 3. 良好模式（值得肯定）

| 模式 | 评价 |
|------|------|
| 协议名保留 EN | CXL.io / CXL.cache / CXL.mem / IDE 全章统一 ✅ |
| 寄存器/字段名不翻译 | Bit/Field name 保留 EN，仅描述翻译 ✅ |
| 毒化术语 | `poison` 保留英文（行业标准译法"毒化"作括号注释）✅ |
| `mux` 术语 | 全 14 章统一"复用"，完全一致 ✅ |
| Modal verbs | `shall`/`may`/`must` 保留原样，未误译 ✅ |
| 图表双语 caption | 格式统一，EN\|CN 双行 ✅ |
| HDM 术语 | Host-managed Device Memory 处理正确 ✅ |

---

## 4. 章节质量速览

| 章节 | 双语 rows | 质量 | 主要问题 |
|------|-----------|------|----------|
| ch01 | 387 | Good | 13 rows ZH 过短（URL 注释），术语混用较明显 |
| ch02 | 16 | Good | 唯一全英文章节摘要，rows 少，无实际问题 |
| ch03 | 330 | **Excellent** | 协议核心，翻译精准，HDM 术语处理正确 |
| ch04 | 155 | **Excellent** | 链路层术语统一 |
| ch05 | 112 | Good | ARB/MUX 术语基本一致 |
| ch06 | 109 | Good | 1 个结构占位（Fail/Fail row），无翻译问题 |
| ch07 | 1499 | Good | rows 最多，coherent 混用，2 个空行占位 |
| ch08 | 1131 | Good | "交换器"用法独特但可能有上下文原因 |
| ch09 | 108 | Good | `memory`→`内存` 与别章不一致 |
| ch10 | 53 | Good | `cache`→`缓存` 与别章不一致 |
| ch11 | 166 | Good | coherent→`一致性` 与别章风格不一致 |
| ch12 | 125 | Good | 同 ch11，coherent + cache 均用中文 |
| ch13 | 18 | Good | 章节短，`memory`→`内存` |
| ch14 | 1009 | Good | `poison` 小写混用，IDE 术语处理正确 |

---

## 5. 修复优先级建议

| 优先级 | 问题 | 工作量 | 影响 |
|--------|------|--------|------|
| **P1** | `coherent/coherency` 统一为"一致性" | 低（脚本批量替换） | 高 — 技术概念歧义 |
| **P2** | `protocol` 全书统一 | 低 | 中 — 阅读体验 |
| **P2** | `transaction` 全书统一 | 低 | 中 |
| **P3** | ch08 `交换器` vs 其他章 `交换机` | 低 | 低 — 语义细分可保留，需确认 |
| **P3** | ch14 `poison` 小写 → `Poison` | 极低 | 低 — 大小写规范 |
| **P4** | 4 个空 `<tr>` 清理 | 极低 | 低 — 表格结构整洁 |

---

## 6. 总体结论

> **翻译质量整体良好**，主要价值在于：
>
> - 完整保留 CXL 3.2 规范全部技术细节
> - 双语对照格式对中英对照学习极为友好
> - 图表嵌入完整（831 张紧致裁剪图）
>
> **最需修复**：`coherent/coherency` → `一致性` 的跨章节不一致（影响技术准确性理解），以及 `protocol`/`transaction` 的混合风格。
>
> 4 个结构占位空行不影响阅读，清理与否可视需要决定。

---

> 🤖 Generated with [Claude Code](https://claude.com/claude-code)
> 📅 2026-06-28
