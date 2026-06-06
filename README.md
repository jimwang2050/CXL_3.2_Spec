# 📚 CXL 3.2 规范中英对照翻译

> **Compute Express Link® (CXL®) Specification — Revision 3.2, Version 1.0 — October 2, 2024**

📄 **Source PDF**: [`../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf`](../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf) (1233 pages, 11 MB)
🎨 **Format**: 中英对照双语 Markdown · 原始图表保留为 PNG · 中文背景色灰色 · GitHub Flavored Markdown
🐙 **GitHub**: https://github.com/jimwang2050/CXL_3.2_Spec

---

## 📊 翻译进度 (Translation Progress)

**已完成**: `14 / 14` 章框架 (12 章完整, Ch7/Ch8 内部有空缺) ｜ **总文件**: 1.7 MB MD + 25 MB 原图

```text
[████████████░░] 95%  (12.5/14 完整)
```

### ✅ 已完成 (完整 12 章)

- [x] **Chapter 1** Introduction / 引言 (p.50–70) — 964 行
- [x] **Chapter 2** CXL System Architecture / CXL 系统架构 (p.71–84) — 1630 行
- [x] **Chapter 3** CXL Transaction Layer / CXL 事务层 (p.85–190) — 1607 行
- [x] **Chapter 4** CXL Link Layers / CXL 链路层 (p.191–261) — 1893 行
- [x] **Chapter 5** CXL ARB/MUX / CXL 仲裁复用 (p.262–286) — 973 行
- [x] **Chapter 6** Flex Bus Physical Layer / Flex Bus 物理层 (p.287–318) — 1319 行
- [x] **Chapter 9** Reset, Initialization, Configuration, and Manageability (p.799–878) — 537 行
- [x] **Chapter 10** Power Management / 电源管理 (p.879–891) — 1019 行
- [x] **Chapter 11** CXL Security / CXL 安全 (p.892–997) — 1209 行
- [x] **Chapter 12** Reliability, Availability, and Serviceability / RAS (p.998–1010) — 630 行
- [x] **Chapter 13** Performance Considerations / 性能考量 (p.1011–1019) — 404 行
- [x] **Chapter 14** CXL Compliance Testing + Appendices A–C / 一致性测试 + 附录 (p.1020–1233) — 3563 行

### ⚠️ 内部有空缺 (2 章)

- [ ] **Chapter 7** Switching / 交换 (p.319–498) — 缺 Part A (p.319–380), API 速率限制
- [ ] **Chapter 8** Control and Status Registers / 控制与状态寄存器 (p.499–798) — 缺 Part B+C (p.556–675), 触发内容过滤器

---

## 🗂 目录结构 (Directory Layout)

```
CXL_zh/
├── README.md                  # 本文件
├── chapter_01.md ~ 14.md      # 14 章节中英对照 (1.7 MB)
└── figures/
    ├── chapter_01/page_*.png  ~ page_*.png   # 全页渲染
    ├── chapter_01/fig_*.{png,jpx}            # 嵌入图
    ├── chapter_02/ ~ 14/                     # 同上结构
```

---

## 🎨 格式约定 (Format Conventions)

每个章节遵循统一的 GitHub Flavored Markdown 结构：

```markdown
# 📘 第 N 章　<Title> (Chapter N. <English>)

> **Source pages**: X–Y | **File**: chapter_NN.md | **Format**: 中英对照双语

## 📑 本章目录 (Table of Contents)
## 🖼 本章图表 (Figures)
## 📊 本章表格 (Tables)

<a id="sec-N-X"></a>
## N.X Section | 中文标题

<table>
<tr><th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr>
<tr><td>English text</td><td style="background-color:#e8e8e8">中文翻译</td></tr>
</table>

> **Figure N-X.** Title
> <img src="figures/chapter_NN/page_XXXX.png" width="700">

[⬆️ 返回目录](#-本章目录-table-of-contents)
```

### 已应用的 GitHub 特性

| 特性 | 实现 |
|------|------|
| **显式锚点** | `<a id="sec-N-X">` 跨设备稳定 |
| **中文灰底** | `<td style="background-color:#e8e8e8">` |
| **图表内嵌** | `<img src="..." width="700">` |
| **任务列表** | `- [x]` / `- [ ]` 进度可视化 |
| **返回目录** | 每节末尾 `[⬆️ 返回目录]` 跳转 |

### 翻译风格

- 首次出现术语: `EN (中文)` 对照, 后续保留英文
- 章节标题双语并列: `## 1.0 Introduction | 引言`
- 表格用 Markdown + 中文列加灰底
- 寄存器字段 (Bit/Field name) **不翻译**, 描述翻译
- 代码、协议字段、寄存器定义保留英文

---

## 🛠 工具链 (Toolchain)

- **PDF 提取**: [PyMuPDF](https://pymupdf.readthedocs.io/) (fitz) — 文本+布局+图像
- **图渲染**: PyMuPDF 150 DPI
- **Python 依赖**: `pypdf pdf2image pdfplumber Pillow reportlab pandas openpyxl PyMuPDF pytesseract`
- **辅助 skills** (本仓库已安装):
  - `pdf` — 官方 anthropics/skills/pdf
  - `pdf-content-extractor` — 中文 PDF + OCR + 去水印
  - `mineru` — 高质量 PDF → Markdown
  - `book-to-skill` — 把整本书转成可查询 skill
  - `translate-book` — 并发批量翻译 (本次使用, 但受 API 速率限制)

---

## ⚠️ 已知问题

1. **Ch7 缺 Part A** (p.319–380, 60 页): 由于 API 速率限制 (Token Plan Plus 5h limit), Part A 子 agent 在限制生效前未能完成
2. **Ch8 缺 Part B+C** (p.556–675, 120 页): Part B 触发内容过滤器 `output new_sensitive`, Part C 多次重试均因 429 失败
3. **Ch14 已合并完整** (含附录 A/B/C): 通过 2-way split 拼接, 3563 行

### 续传方案

API 速率限制将于 **20:00 (UTC+8) 重置**。重置后可重新调度:
- Ch7 Part A (p.319–380, ~120K 字)
- Ch8 Part B+C (p.556-675, ~150K 字)

```bash
# 重置后可执行
python3 /tmp/extract_ch8_bc.py  # 重新抽取
# 然后用 Agent 工具并发调度翻译
```

---

## ⏭️ 下一步

- [ ] **API 速率限制重置后** (20:00 UTC+8) 续传 Ch7 Part A + Ch8 Part B+C
- [ ] 合并最终分块, 重新推送
- [ ] 在 GitHub 仓库 README 中添加章节目录链接
- [ ] 校对与精修: 由人工或下次 API 配额恢复时, 重点校对 Ch3 (核心协议) 与 Ch11 (安全) 的关键术语一致性

---

> 🤖 **Generated with** [Claude Code](https://claude.com/claude-code) · Opus 4.8
> 📅 2026-06-06
