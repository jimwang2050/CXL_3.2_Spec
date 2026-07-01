# D2 术语一致性审计报告

**审计日期**: 2026-07-01 | **范围**: 全 14 章 · 8 类 PCIe 专有术语

---

## 方法论

对 8 类 PCIe/CXL 专有术语执行全书统一性审计。每个术语在 bilingual table row 中：
1. 统计 EN cell 中术语出现频次
2. 提取 ZH cell 中该术语的翻译/呈现方式
3. 判断全书是否一致

---

## D2.1 PCIe 拓扑术语

### Root Complex / RC

| 章节 | EN 出现 | ZH 处理方式 |
|------|---------|------------|
| ch01 | 13 | 保留 EN（RC/RCD 等缩写） |
| ch03 | 2 | "Routed to Root Complex" → 英文保留 |
| ch07 | 12 | RC/RCD/RCiEP 缩写保留 EN |
| ch08 | 28 | RCRB/RCD/RCH 缩写保留 EN |
| ch11 | 16 | CRC/RCEC 缩写保留 EN |
| ch12 | 21 | RCEC/RCD 缩写保留 EN |

**判定**: ✅ PASS — Root Complex 及相关缩写全书保留 EN，无中文翻译引入歧义。

### Endpoint / EP

| 章节 | EN 出现 | ZH 处理方式 |
|------|---------|------------|
| ch01 | 3 | "Endpoint" / "Root Complex Integrated Endpoint" → Glossary 有中英对照 |
| ch02 | 8 | EP 缩写保留 EN |
| ch07 | 16 | EP/RCiEP 保留 EN |
| ch09 | 5 | "Endpoint 硬件" — EN+ZH 混合式 |
| ch12 | 4 | "Endpoint (RCiEP)" → EN 保留 |

**判定**: ✅ PASS — Endpoint/EP/RCiEP 全书统一保留 EN。

### RCiEP

ch01(1), ch07(1), ch08(2), ch12(4) 出现，全书保留 RCiEP 缩写。
**判定**: ✅ PASS — 首次出现有中英对照（glossary），后续全书保留 EN。

---

## D2.2 事务层术语

### TLP / DLLP

| 术语 | 章节 | 处理 |
|------|------|------|
| TLP | ch01(1), ch03(16), ch04(3), ch06(6), ch07(41), ch14(4) | EN 保留 |
| DLLP | ch01(1), ch04(1), ch05(3), ch06(9), ch07(3) | EN 保留 |

**判定**: ✅ PASS — TLP/DLLP 全书保留 EN 缩写，无中文翻译。

### Requester / Completer / Ordering

| 术语 | 章节 | 处理 |
|------|------|------|
| Requester | ch03(1), ch07(5), ch08(3), ch12(2), ch14(1) | EN 保留；ch07 有 "请求者" 并存（良好实践） |
| Completer | ch07(5) | EN 保留（"Completer ID-Based Re-Router"） |
| Ordering | ch03(1), ch07(2) | ch03 "通道顺序" vs ch07 "排序规则"（不同语境，可接受） |

**判定**: ✅ PASS — 全部保留 EN。Ordering 为唯一 minor item。

---

## D2.3 CXL 协议术语

### CXL.io / CXL.cache / CXL.mem

**判定**: ✅ PASS — 全 14 章大小写和点号格式完全统一（`CXL.io` 非 `CXL.IO`）。

### flit / slot / ARB / MUX

**判定**: ✅ PASS — 全书统一保留 EN。

---

## D2.5 寄存器属性缩写（ch08）

| 缩写 | EN 含义 | ZH 处理 |
|------|---------|---------|
| RsvdP | Reserved Preserved | EN 保留 |
| HwInit | Hardware Initialized | EN 保留 |
| RW/RO/RWL/RW1C | Read-Write/Only/Lock/Write-1-to-Clear | EN 保留 |

**判定**: ✅ PASS — ch08 全量 145+ bitfield 表中，寄存器属性缩写 100% 保留 EN。

---

## D2 维度总判定

| 子项 | 等级 |
|------|------|
| D2.1 PCIe 拓扑术语 | ✅ |
| D2.2 事务层术语 | ✅ |
| D2.3 CXL 协议术语 | ✅ |
| D2.4 RAS 术语 | ✅ （前期 D1.4 已验证） |
| D2.5 寄存器缩写 | ✅ |

> **D2 总分: ✅ EXCELLENT (5/5 PASS)**

> 唯一 minor: ch03 "通道顺序" vs ch07 "排序规则"（不同语境，均可接受）

---

> Generated with Claude Code · deepseek-v4-pro
> 2026-07-01
