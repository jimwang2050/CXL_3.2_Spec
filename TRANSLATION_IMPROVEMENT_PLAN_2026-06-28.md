# CXL 3.2 翻译质量提升计划
**制定日期**: 2026-06-28 | **基于**: `TRANSLATION_AUDIT_REPORT_2026-06-28.md`

---

## 📋 问题清单（经逐行核查确认）

### P4 — 结构性占位空行（4 处，非翻译错误）

| # | 章节 | 行号 | 类型 | 描述 |
|---|------|------|------|------|
| S1 | ch06 | ~1108 | `<tr>` 残缺 | 9 列表格 `Fail/Fail` 行，末尾 3 个 `<td></td>` 空 cell；SPEC 此 case 定义为"无需动作" |
| S2 | ch07 | ~1415 | 空 `<tr>` | tbody 起始行，EN/ZH 均为空 |
| S3 | ch07 | ~1636 | 空 `<tr>` | 同上 |
| S4 | ch08 | ~6663 | 空 `<tr>` | Part B tbody 起始行，EN/ZH 均为空 |

**性质**: HTML 表格生成工具残留，非翻译遗漏，肉眼浏览为空白行。

---

### P4 — ch07 章节标题缺少中文副标题（3 处）

| # | 章节 | 现行标题 | 建议补全 |
|---|------|----------|----------|
| H1 | ch07 | `### 7.3.1 CXL.io` | `### 7.3.1 CXL.io | CXL.io` |
| H2 | ch07 | `### 7.3.2 CXL.cache` | `### 7.3.2 CXL.cache | CXL.cache` |
| H3 | ch07 | `### 7.3.3 CXL.mem` | `### 7.3.3 CXL.mem | CXL.mem` |

**性质**: 与同文件其他 200+ 个 `## EN | CN` 双语标题风格不一致；这三个恰好是纯协议名，可接受保留 EN，但补全后全书风格更统一。

---

### P4 — ch14 `poison` 大小写混用（7 处 EN cell）

| # | 现行 EN | ZH 译文 |
|---|---------|---------|
| P1 | `poisoned received error` | `poison 错误` |
| P2 | `inject poison:` | `注入 poison：` |
| P3 | `inject poison viral.` | `注入 poison viral.` |
| P4 | `poisoned received error` | `poison 错误` |
| P5 | `inject poison viral:` | `注入 poison viral：` |
| P6 | `poisoned received error` | `poison 错误` |
| P7 | `poison 错误` (ZH) | — |

**规范**: 其他章节（ch03/ch04/ch08/ch11/ch12）均用 `Poison`（首字母大写），ch14 用 lowercase `poison` 与全书不一致。

---

### P3 — 其他观察项（可接受，不列入本次计划）

| 项 | 描述 | 决定 |
|----|------|------|
| `VendPrefixL0` (ch03) | 纯协议名，EN-only 标题可接受 | 不改 |
| `CXL.io` / `CXL.cache` / `CXL.mem` | 协议名保留 EN，全书统一 | 不改 |
| `mux` → `复用` | 全 14 章完全统一 | 良好 |
| 寄存器字段 Bit/Field name | 不翻译，仅描述翻译 | 良好 |
| HDM-D / HDM-DB / HDM-H | 保留 EN | 良好 |

---

## ✅ 本次计划范围

```
┌─────────────────────────────────────────────────────────┐
│  范围结论                                               │
│                                                         │
│  P4 级（4+3+7 = 14 处精确修改）                        │
│  ├── S1-S4: 4 个空 <tr> 行清理                         │
│  ├── H1-H3: 3 个 ch07 标题补 CN 副标题                 │
│  └── P1-P7: 7 处 ch14 poison 大小写修正               │
│                                                         │
│  总计：3 类 · 14 处修改 · 0 风险                        │
│  预计工作量：脚本批量处理 < 30 分钟                       │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠 修复方案

### S1–S4: 清理空 `<tr>` 行

```python
# 精确删除以下 4 个空行（不涉及任何内容翻译修改）

# ch06 ~line 1108 — 找到该 Fail/Fail row，将末尾 3 个 <td></td> 改为注释
# ch07 ~line 1415, 1636 — 删除整行 <tr><td></td><td style="..."></td></tr>
# ch08 ~line 6663 — 同上
```

### H1–H3: 补全 ch07 标题副标题

```python
# ch07:
# ### 7.3.1 CXL.io  →  ### 7.3.1 CXL.io | CXL.io
# ### 7.3.2 CXL.cache  →  ### 7.3.2 CXL.cache | CXL.cache
# ### 7.3.3 CXL.mem  →  ### 7.3.3 CXL.mem | CXL.mem
```

### P1–P7: ch14 poison 大小写修正

```python
# 在 EN cell（<td> 中，将 poison → Poison
# 仅影响 7 个 <tr> 中的 EN cell，ZH cell 不变
# 脚本: re.sub(r'\bpoison\b', 'Poison', en_cell_text)
```

---

## 📊 预期结果

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| 空 `<tr>` 行 | 4 | 0 |
| 缺 CN 副标题的章节 | 3 | 0 |
| poison 大小写错误 | 7 | 0 |
| 表格结构整洁度 | 4 个空白行 | 全部清除 |

---

## ⏭ 未列入本次计划的后续项

如未来有第二次提升，可考虑：

| 优先级 | 项 | 说明 |
|--------|----|------|
| P3 | `coherent` → `一致性` 术语表 | ch01 Glossary 表中已有 EN\|CN，实际歧义有限 |
| P3 | ch07 正文"硬件一致性不是必需的" → "硬件一致性（coherency）不是必需的" | 括号加注 EN 术语可消除歧义 |

---

> 🤖 Generated with [Claude Code](https://claude.com/claude-code)
> 📅 2026-06-28
