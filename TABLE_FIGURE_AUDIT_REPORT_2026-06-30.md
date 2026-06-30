# Table & Figure Integrity + Formatting Compliance Audit Report

**审计日期**: 2026-06-30 | **审计人**: Claude Code | **语料**: 全 14 章

---

## 📋 执行摘要

| 维度 | 结果 | 评级 |
|------|------|------|
| Table ZH 完整性 | 5,162 bilingual rows，0 空/占位 | ✅ Excellent |
| Figure 文件引用 | 1,400 个引用，0 broken links | ✅ Excellent |
| Figure Caption 对齐 | 277 captions，274 imgs，10/14 章节完全对齐 | ✅ Good |
| HTML 结构完整性 | ch14 发现 6 行 HTML 结构损坏 | ⚠️ Needs Fix |
| 排版合规性 | 3 个 caption 使用 ASCII '\|' | ⚠️ Minor |

---

## PHASE 1 — Table Integrity

### 1.1 双语表格统计

| 章节 | 双语 Tables | 双语 Rows |
|------|-------------|-----------|
| ch01 | 10 | 387 |
| ch02 | 27 | 16 |
| ch03 | 62 | 330 |
| ch04 | 53 | 155 |
| ch05 | 36 | 112 |
| ch06 | 27 | 109 |
| ch07 | 329 | 1,497 |
| ch08 | 633 | 1,130 |
| ch09 | 14 | 108 |
| ch10 | 20 | 0 |
| ch11 | 37 | 166 |
| ch12 | 21 | 125 |
| ch13 | 5 | 18 |
| ch14 | 110 | 1,009 |
| **合计** | **1,384** | **5,162** |

### 1.2 ZH Cell 完整性

- **空 ZH Cell**: 0（之前审计发现的 4 个空 `<tr>` 已清理）
- **占位文本** (TODO/占位/`[trans]`): 0
- **EN Cell 含中文字符**: 249 处 — 均为正常情况（寄存器字段描述中的中文注释、protocol 名称等）
- **寄存器/字段名翻译**: ✅ 全书统一不翻译（Bit/Field name 保留 EN）

### 1.3 多列表格结构（⚠️ 非翻译问题，为 PDF 原生结构）

以下章节存在多列常规表格（非双语格式）内嵌在双语行中的情况，这是 PDF spec 原生结构，不是翻译错误：

| 章节 | 说明 |
|------|------|
| ch01 | 参考文档表（3 列 PCI Sig 规范列表） |
| ch04 | Link Layer 帧格式表（含 Signal Name / Description / Requirement 多列） |
| ch05 | ARB/MUX 状态转换表（3–4 列） |
| ch06 | 链路速率/宽度矩阵表（3–5 列） |
| ch07 | 信号定义表、寄存器块多列表格（72 个内嵌常规表格） |
| ch08 | 寄存器定义表（1,560+ 个多列表格行） |
| ch13 | 性能参数对比表（ colspan=3/4/5 混用） |
| ch14 | DOE/测试向量表（ colspan=2/3/5 混用） |

---

## PHASE 2 — Figure File Integrity

### 2.1 统计

| 指标 | 数值 |
|------|------|
| 磁盘 figure 文件 | 1,860 |
| MD 中唯一 figure 引用 | 1,400 |
| Broken references（引用但文件不存在） | **0** |
| img 无 alt 属性 | **0** |

### 2.2 各章节 Figure 引用统计

| 章节 | 唯一 Figure 引用数 | img 标签数 |
|------|-------------------|-----------|
| ch01 | 17 | 7 |
| ch02 | 22 | 0 (README 说明性引用) |
| ch03 | 44 | 16 |
| ch04 | 60 | 40 |
| ch05 | 51 | 20 |
| ch06 | 35 | 13 |
| ch07 | 291 | 144 |
| ch08 | 727 | 357 |
| ch09 | 10 | 3 |
| ch10 | 27 | 8 |
| ch11 | 48 | 24 |
| ch12 | 14 | 4 |
| ch13 | 3 | 0 |
| ch14 | 51 | 18 |

### 2.3 Orphan Files（磁盘有但 MD 未引用）

> 这些文件是 MinerU 去水印处理前的原始版本，已由 `.gitignore` 中的 `.bak` 规则部分忽略。以下列出的是实际存在的非备份文件：

| 文件 | 说明 |
|------|------|
| `chapter_01/page_0050–page_0062.png` | 13 张去水印前的原版 spec 页面 |
| `chapter_01/fig_0064_2.png`, `fig_0066_2.png` | 同一 figure 的第二个版本（可能是 MinerU 输出副产物） |
| `chapter_01/*.jpx` | 原始 JPX 格式（与 PNG 双版本并存） |

**建议**: 可安全删除 `chapter_01/page_0050–page_0062.png`（已被 `fig_0062_1.png–fig_0068_1.png` 覆盖），`*.jpx` 和 `*_2.png` 若确认未使用可清理。

---

## PHASE 3 — Figure Caption & Cross-Reference

### 3.1 Caption 对齐结果

| 章节 | Caption 数 | Img 数 | 对齐状态 | 双语格式 |
|--------|-----------|--------|----------|---------|
| ch01 | 2 | 7 | ⚠️ alt 含完整标题（检测偏误，非真问题） | ✅ |
| ch02 | 6 | 0 | ⚠️ caption-only（无内嵌图，纯 TOC 引用） | ✅ |
| ch03 | 16 | 16 | ✅ 1:1 | ✅ |
| ch04 | 40 | 40 | ✅ 1:1 | ✅ |
| ch05 | 20 | 20 | ✅ 1:1 | ✅ |
| ch06 | 13 | 13 | ✅ 1:1 | ✅ |
| ch07 | 55 | 55 | ✅ 1:1 | ✅ |
| ch08 | 66 | 66 | ✅ 1:1 | ✅ |
| ch09 | 3 | 3 | ✅ 1:1 | ⚠️ ASCII '\|' 非 '｜' |
| ch10 | 8 | 8 | ✅ 1:1 | ✅ |
| ch11 | 24 | 24 | ✅ 1:1 | ✅ |
| ch12 | 4 | 4 | ✅ 1:1 | ✅ |
| ch13 | 1 | 0 | ⚠️ 1 caption 无内嵌 img（p.1019 spec 原书此处无图） | ✅ |
| ch14 | 19 | 18 | ⚠️ 1 caption (14-19) 引用 p.1194（超出 CXL 3.2 spec 范围） | ⚠️ 1 non-bi |

**总计**: 277 captions，274 img tags，**10/14 章节完全对齐**

### 3.2 ch01 Figure Caption 说明

ch01 中 `alt` 属性包含完整 figure 标题（如 `alt="Figure 1-8: CXL Downstream Port Con..."`），而非纯编号格式 `alt="Figure 1-8"`。这实际上是更好的无障碍访问（a11y）实践，不影响渲染，但导致检测脚本产生了"orphan img"误报。

---

## ⚠️ CRITICAL — ch14 HTML 结构损坏（6 行）

### 4.1 问题位置

| 行号 | 内容 |
|------|------|
| ~2962 | `<tr><td><tr><td></td>• Receiver (host) logs poisoned received error...` |
| ~3164 | `<tr><td><tr><td></td>b. Write a Compliance mode DOE to inject poison:` |
| ~3279 | `<tr><td><tr><td></td>b. Write a Compliance mode DOE to inject poison viral.` |
| ~3282 | 同上（重复步骤） |
| ~3382 | `<tr><td><tr><td></td>b. Write a Compliance mode DOE to inject poison viral:` |
| ~3385 | 同上（重复步骤） |

### 4.2 损坏结构

```
<tr><td>
  <tr><td></td>• Receiver (host) logs poisoned received error
  <td style="background-color:#e8e8e8"></td>
  <td style="background-color:#e8e8e8"></td>
</tr>
```

正确结构应为：
```
<tr>
  <td>• Receiver (host) logs poisoned received error</td>
  <td style="background-color:#e8e8e8">• 接收方（主机）记录接收到的 Poison 错误</td>
</tr>
```

### 4.3 根因

PDF spec 中的多行 bullet list（如测试步骤 a. / b. / c.），在 MinerU PDF→MD 转换时，将后续行错误解析为嵌套 `<tr><td>` 结构。

### 4.4 影响

GitHub 渲染时，该 `<td>` 内的嵌套 `<tr>` 不会被识别为行，而是作为纯文本显示，导致格式混乱。

---

## 📋 修复建议

| 优先级 | 问题 | 章节 | 工作量 | 说明 |
|--------|------|------|--------|------|
| **P1** | 6 个损坏 `<tr>` HTML 结构 | ch14 | ~15 min | 需手动重建表格行结构 |
| **P2** | 3 个 caption '\|' → '｜' | ch09 | ~2 min | 脚本批量替换 |
| **P3** | 清理 13 张 orphan page_*.png | ch01 | ~5 min | 删除未引用文件 |
| **P3** | .jpx 双版本文件清理 | ch01 | ~3 min | 确认后可删除 |

---

## ✅ 良好实践（无需修改）

| 项目 | 评价 |
|------|------|
| fig_XXXX_1.png 命名规范 | ✅ 全 14 章统一 |
| img alt 全覆盖 | ✅ ch07(144) + ch08(357) 全部有 alt |
| Bilingual caption '｜' 分隔符 | ✅ ch07/ch08 核心章节 100% 统一 |
| Figure caption / img 1:1 对齐 | ✅ ch03–ch08 核心章节完全对齐 |
| fig_*_1.png 去水印处理 | ✅ 比原始 page_*.png 小约 30% |

---

> 🤖 Generated with [Claude Code](https://claude.com/claude-code)
> 📅 2026-06-30
