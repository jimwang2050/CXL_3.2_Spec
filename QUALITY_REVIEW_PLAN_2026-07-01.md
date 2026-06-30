# CXL 3.2 翻译质量审查计划（6 维模型·全 14 章）

**制定日期**: 2026-07-01 | **基于**: 三次前期审计结论综合
**模型**: 协议忠实度 · 术语一致性 · 结构可追溯 · MD 可读性 · 图表完整性 · 法务版权合规性

---

## 执行摘要

| 维度 | 前期覆盖度 | 本次计划 | 预算 |
|------|-----------|----------|------|
| 1. 协议忠实度 | 浅（仅术语层） | 深（shall/must/may × 状态机 × 错误语义） | ~2h |
| 2. 术语一致性 | 中（11 组关键术语） | PCIe 专项（TLP/DLLP/RC/EP 等 8 类） | ~1.5h |
| 3. 结构可追溯 | 中（锚点计数） | 全量锚点有效性验证 + 图号/表号交叉核查 | ~1h |
| 4. MD 可读性 | **GAP** | 标题层级 + HTML 表格 + code block + Mermaid | ~1h |
| 5. 图表完整性 | **GAP** | 寄存器位域表 + 状态机 + TLP 格式 + 时序图 | ~2h |
| 6. 法务/版权 | 未覆盖 | confidential 文本 + LICENSE + 免责声明 + risk matrix | ~0.5h |

---

## 📐 维度 1 — 协议忠实度（Protocol Fidelity）

| 目标 | 不改变 PCIe/CXL 语义，中文翻译保持 shall/must/may 的规范力 |
|------|----------------------------------------------------------|
| 检查重点 | shall→应，must→必须，may→可，should→宜；状态机描述；字段定义；时序；错误语义 |
| 现状 | ch03: shall=25 / must=41 / may=25 / should=14；ch07: shall=98 / must=91 / may=88 / should=25 |
| 风险 | 单个 shall→should 误译可能导致互操作性问题；must→may 误译导致合规性风险 |

### 审查项

| # | 项 | 方法 | 范围 |
|---|-----|------|------|
| 1.1 | shall/must/may 翻译审查 | 双语 rows 中 EN 含 modal 的 row，抽查 ZH 译文中的情态动词一致性 | ch03 + ch07 全量（~230 rows），其余 12 章每章抽 5 行 |
| 1.2 | 状态机描述检查 | EN 段落中 state/transition/entry/exit 对应 ZH 翻译，确认未丢失或错译 | ch05 ARB/MUX（279 处状态引用）+ ch09 Reset |
| 1.3 | 字段定义位宽数字核查 | EN cell 中 `N bits` / `Width: N` 等与 ZH cell 对比 | ch08 全量 register 表（145+ bitfield 段） |
| 1.4 | 错误语义翻译审计 | `poison` / `viral` / `uncorrectable` / `advisory` 等错误等级术语翻译 | ch03（事务层）+ ch11（IDE 安全）+ ch12（RAS） |
| 1.5 | 时序/顺序语义 | `before` / `after` / `within N ns` / `simultaneously` 翻译 | ch06（Flex Bus PHY）+ ch09（init sequence） |

### 判定标准

- ✅ Pass: EN→ZH 保持源规范力（shall=应 / must=必须 100%）
- ⚠️ Fix: shall 译为"可以"等弱化（需批量标注修正）
- ❌ Fail: 数字错译（bit width / timing value / register offset）

---

## 📐 维度 2 — 术语一致性（Terminology Consistency）

| 目标 | PCIe/CXL 专用术语全书统一，中英文长期稳定 |
|------|------------------------------------------|
| 检查重点 | TLP / DLLP / RC / EP / RCiEP / Requester / Completer / Ordering / Flit / Slot / ARB / MUX |
| 现状 | 前期审计覆盖 protocol/transaction/coherent 等 11 组，PCIe 专有名词未查 |

### 审查项

| # | 项 | 方法 | 预期 |
|---|-----|------|------|
| 2.1 | PCIe 拓扑术语 | Root Complex/RC, Endpoint/EP, RCiEP, Switch/Bridge 全书统一 | grep 全 14 章，每术语列出所有章节译法 |
| 2.2 | 事务层术语 | TLP/DLLP, Requester, Completer, Non-Posted/Posted, Ordering | 同上，聚焦 ch03/ch04/ch07 |
| 2.3 | CXL 协议术语 | CXL.io/CXL.cache/CXL.mem 大小写规范、flit/slot/ARP/MUX | 全 14 章统一性扫描 |
| 2.4 | RAS 术语 | poison/viral/corrected/uncorrectable/advisory/fatal | ch03/ch11/ch12 三章完整覆盖 |
| 2.5 | 寄存器属性缩写 | RsvdP/HwInit/RW/RO/RWL/RW1C 是否保留 EN（不应翻译） | ch08 全量寄存器表 |

### 判定标准

- ✅ 每术语全书一致（同一译法无歧义）
- ⚠️ 同一术语 2-3 种译法并列（用例：switch → 交换机/交换器，可能有合理性）
- ❌ 同一术语 4+ 种译法或中英混淆

---

## 📐 维度 3 — 结构可追溯（Structural Traceability）

| 目标 | 从 MD 任意段落可追溯回原文（章节号·图表号·页码·原文锚点） |
|------|----------------------------------------------------------|
| 检查重点 | `<a id="">` anchor 完整性、TOC→锚点→原文章节号映射、图表号交叉引用 |
| 现状 | 14 章均含 anchor（ch07: 128, ch08: 371），前期审计发现 TOC 链接依赖 GitHub 自动 slug（如 `#-本章目录-part-a`） |

### 审查项

| # | 项 | 方法 | 范围 |
|---|-----|------|------|
| 3.1 | Anchor 定义完整性 | 每个 `<a id="sec-X-Y">` 在 TOC 中有对应链接，每个 `(#sec-X-Y)` 有对应 anchor 定义 | 全 14 章自动化 |
| 3.2 | TOC→正文跳转验证 | TOC 中章节条目的跳转目标存在且唯一，目标编号与 TOC 编号匹配 | 全 14 章 |
| 3.3 | Figure/Table 编号 TOC 一致性 | `## 🖼 本章图表` 中列出的编号与正文 captions 对齐 | ch01–ch14 |
| 3.4 | 源页码保留 | 双语 section header `> **Source pages**: X–Y` 块，14 章均有且数字连续 | 14 章 header block |
| 3.5 | Part 子章节编号连续性 | ch07（ABC）、ch08（ABDE）、ch14（AB）Part 间过渡点锚点一致 | ch07/ch08/ch14 |

### 判定标准

- ✅ 100% TOC→anchor→标题对齐
- ⚠️ ≥95% 对齐（允许 `#-本章目录-part-a` 依赖 GitHub slug）
- ❌ <95% 或存在重复 `<a id="">`

---

## 📐 维度 4 — Markdown 可读性（Markdown Readability）

| 目标 | GitHub 渲染稳定，无断链/无格式异常/无渲染碎片 |
|------|----------------------------------------------|
| 检查重点 | 标题层级一致性、HTML 表格合规、code block 利用率、Mermaid 图可用性、锚点渲染 |
| 现状 | **GAP** — ch01/ch02 有 code block + Mermaid（2-3 个），ch03+ 无；ch08 有 391 个 `Figure 8-X` 占位 |

### 审查项

| # | 项 | 方法 | 范围 |
|---|-----|------|------|
| 4.1 | 标题层级跳级检测 | 检测 H1→H3（缺 H2）或 H2→H4（缺 H3）跳级 | 全 14 章 |
| 4.2 | HTML 表格结构验证 | `<td>`/`<tr>` 开闭标签计数匹配，colspan/rowspan 不溢出 | ch07（403 tables）+ ch08（714 tables）全量 |
| 4.3 | GitHub 样式统一性 | `style="background-color:#e8e8e8"` 的 `<td>` 统一、`width="50%"` 无歧义 | 所有双语表格 |
| 4.4 | Code block 覆盖率 | 评估规范中应使用 code block（寄存器地址、指令序列、JSON 配置）的段 | ch08 + ch11 |
| 4.5 | Mermaid 图利用率 | ch01/ch02 已有 mermaid（流程图），ch05/ch09 状态机是否可转 mermaid | ch01/ch02/ch05/ch09 |
| 4.6 | `<br>` 标签规范性 | 186 个 `<br>`（ch07），评估是否应转 `<ul>/<ol>` 或 `<p>` | ch07 + ch14 |

### 判定标准

- ✅ 标题无跳级，HTML 标签配对 100%
- ⚠️ 跳级 < 3 处（设计性），`<br>` 可接受
- ❌ 标签不配对（渲染破坏），跳级 > 10 处

---

## 📐 维度 5 — 图表完整性（Diagram & Figure Integrity）

| 目标 | 表格/流程图不丢失信息；寄存器位域、状态机、TLP 格式、时序图完整保留 |
|------|------------------------------------------------------------------|
| 检查重点 | 配置寄存器位域表 vs 源 spec、状态机图与对应文字说明的一致性、TLP 格式字段完整性 |
| 现状 | ch08 145+ bitfield 表、ch05 279 状态引用、ch04 790 TLP/flit 格式引用；1,860 张图/1,400 引用 0 broken link |

### 审查项

| # | 项 | 方法 | 范围 |
|---|-----|------|------|
| 5.1 | 寄存器位域完整性 | ch08 `Bit Location` 表列数与 spec 原文对齐；跨页 bitfield 连续 | ch08 抽 10 个密集寄存器 |
| 5.2 | 状态机图与文字一致性 | ch05 ARB/MUX Figure 5-1→5-20 文字描述在双语行中完整保留 | ch05 全 20 figures |
| 5.3 | TLP/Flit 格式字段完整性 | ch04 flit format 字段名保留 EN，位宽数字无错译 | ch04 13 inlines |
| 5.4 | 时序/波形图追迹 | ch06 Flex Bus PHY timing 参数（UI、ns、ps）无误译或精度丢失 | ch06 全量 timing 表 |
| 5.5 | 图补遗段检查 | ch07/08/14 MinerU 额外图"图补遗"段：是否有未插入但需双语 caption 的图 | ch07/08/14 图补遗段 |

### 判定标准

- ✅ bitfield 表字段数与 spec 原件一致
- ⚠️ 位域名保留 EN（设计正确），描述字段译错 1-2 处
- ❌ bit width 数字错误、状态转换丢失

---

## 📐 维度 6 — 法务/版权合规（Legal & Copyright）

| 目标 | 识别并缓解公开 GitHub repo 上发布 CXL spec 翻译的版权风险 |
|------|-----------------------------------------------------------|
| 检查重点 | PCI-SIG 对公开翻译的立场、Evaluation Copy 水印含义、confidential 文本、LICENSE |
| 现状 | **GAP** — 3 个 MD 文件含 `confidential` 关键词、无 LICENSE 文件、无免责声明 |

### 审查项

| # | 项 | 当前状态 | 建议行动 |
|---|-----|----------|----------|
| 6.1 | `confidential` 关键词扫描 | ch01/ch08/ch11 含 `confidential`（源自 PCIe spec 技术性引用 "confidential computing"） | 确认上下文：如为 security 术语，无版权风险；如为 license 条款，需删除 |
| 6.2 | LICENSE 文件 | **缺失** | 建议添加 CC BY-NC-SA 4.0 或 MIT（翻译作品可选择） |
| 6.3 | 免责声明 | **缺失** | 建议 README 添加：本翻译为社区非官方译本，不替代原版 spec |
| 6.4 | PCI-SIG 会员合规 | 源 PDF 标记 "Evaluation Copy" | 确认 repo owner PCI-SIG 会员类型是否涵盖翻译分发 |
| 6.5 | 风险评估矩阵 | 公开 GitHub repo，Google 可搜索 | 编制：学术引用 vs 商业分发风险 |
| 6.6 | `.gitignore` 覆盖 | de-watermarked backup `.bak`、源 PDF | 已验证 — `CXL-Specification*.pdf` 被忽略 |

### 风险矩阵

| 风险等级 | 场景 | 缓解措施 |
|----------|------|----------|
| **🔴 高** | PCI-SIG 提出 DMCA takedown | 确认 PCI-SIG 翻译政策；备选方案：private repo |
| **🟡 中** | "Evaluation Copy" 水印暗示不可分发 | 图已去水印，源 PDF 已 gitignore；加注"仅用于学习研究" |
| **🟢 低** | 个人学习笔记性质 | README 加 disclaimer：非官方翻译、无保证、非商业用途 |

### 判定标准

- ✅ LICENSE + disclaimer 齐备，无禁止性标记
- ⚠️ LICENSE 缺失但 disclaimer 已有
- ❌ 无 LICENSE + 无 disclaimer + 含禁止分发标记

---

## 📅 执行排班

| Phase | 维度 | 预期产出 | 注 |
|-------|------|----------|-----|
| **Phase A** | D1 协议忠实度 + D3 结构可追溯 | shall/must/may 审计表 + anchor 完整性报告 | 可并行脚本 |
| **Phase B** | D2 术语一致性 | PCIe 8 类术语全书对照表 | 可并行脚本 |
| **Phase C** | D4 MD 可读性 + D5 图表完整性 | 标题层级报告 + bitfield 完整性报告 | 需人工抽检 |
| **Phase D** | D6 法务/版权 | 合规风险报告 + 推荐行动清单 | 需人工判断 |

---

## 📊 最终产出物

| 文件 | 状态 |
|------|------|
| `QUALITY_REVIEW_PLAN_2026-07-01.md`（本文件） | ✅ 已生成 |
| `D1_PROTOCOL_FIDELITY_REPORT_2026-07-01.md` | 待执行 |
| `D2_TERMINOLOGY_CONSISTENCY_REPORT_2026-07-01.md` | 待执行 |
| `D3_STRUCTURAL_TRACEABILITY_REPORT_2026-07-01.md` | 待执行 |
| `D4_MD_READABILITY_REPORT_2026-07-01.md` | 待执行 |
| `D5_DIAGRAM_INTEGRITY_REPORT_2026-07-01.md` | 待执行 |
| `D6_LEGAL_COMPLIANCE_REPORT_2026-07-01.md` | 待执行 |

---

> 🤖 Generated with [Claude Code](https://claude.com/claude-code) · deepseek-v4-pro
> 📅 2026-07-01 | 基于 TRANSLATION_AUDIT_REPORT_2026-06-28 + TABLE_FIGURE_AUDIT_REPORT_2026-06-30
