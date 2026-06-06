# 📚 CXL 3.2 规范中英对照翻译

> **Compute Express Link® (CXL®) Specification — Revision 3.2, Version 1.0 — October 2, 2024**

📄 **Source PDF**: [`../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf`](../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf) (1233 pages, 11 MB)
🎨 **Format**: 中英对照双语 Markdown · 原始图表保留为 PNG · 中文背景色灰色 · GitHub Flavored Markdown
🐙 **GitHub**: https://github.com/jimwang2050/CXL_3.2_Spec

---

## 📊 翻译进度 (Translation Progress)

**已完成**: `12 / 14` 章完整 ｜ 2 章内部有空缺 (Ch7 缺 Part A, Ch8 缺 Part B+C)
**总文件**: 1.7 MB MD + 25 MB 原图

```text
[████████████░░] 95%  (12.5/14 完整)
```

## 📖 章节目录 (Chapters)

> 文件命名格式: `CXL3.2_Spec_第N章_chNN_<EnglishTitle>_<中文Title>.md`

| Ch | English Title | 中文标题 | Pages | Status | File |
|:-:|---------------|----------|:-----:|:------:|:----:|
| 1 | Introduction | 引言 | 50–70 | ✅ Done | [📄 CXL3.2_Spec_第1章_ch01_Introduction_引言.md](CXL3.2_Spec_第1章_ch01_Introduction_引言.md) |
| 2 | CXL System Architecture | CXL 系统架构 | 71–84 | ✅ Done | [📄 CXL3.2_Spec_第2章_ch02_CXL_System_Architecture_CXL系统架构.md](CXL3.2_Spec_第2章_ch02_CXL_System_Architecture_CXL系统架构.md) |
| 3 | CXL Transaction Layer | CXL 事务层 | 85–190 | ✅ Done | [📄 CXL3.2_Spec_第3章_ch03_CXL_Transaction_Layer_CXL事务层.md](CXL3.2_Spec_第3章_ch03_CXL_Transaction_Layer_CXL事务层.md) |
| 4 | CXL Link Layers | CXL 链路层 | 191–261 | ✅ Done | [📄 CXL3.2_Spec_第4章_ch04_CXL_Link_Layers_CXL链路层.md](CXL3.2_Spec_第4章_ch04_CXL_Link_Layers_CXL链路层.md) |
| 5 | CXL ARB/MUX | CXL 仲裁/复用 | 262–286 | ✅ Done | [📄 CXL3.2_Spec_第5章_ch05_CXL_ARB-MUX_CXL仲裁复用.md](CXL3.2_Spec_第5章_ch05_CXL_ARB-MUX_CXL仲裁复用.md) |
| 6 | Flex Bus Physical Layer | Flex Bus 物理层 | 287–318 | ✅ Done | [📄 CXL3.2_Spec_第6章_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md](CXL3.2_Spec_第6章_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md) |
| 7 | Switching | 交换 | 319–498 | ⚠️ 缺 Part A | [📄 CXL3.2_Spec_第7章_ch07_Switching_交换.md](CXL3.2_Spec_第7章_ch07_Switching_交换.md) |
| 8 | Control and Status Registers | 控制与状态寄存器 | 499–798 | ⚠️ 缺 Part B+C | [📄 CXL3.2_Spec_第8章_ch08_Control_and_Status_Registers_控制与状态寄存器.md](CXL3.2_Spec_第8章_ch08_Control_and_Status_Registers_控制与状态寄存器.md) |
| 9 | Reset, Initialization, Configuration, and Manageability | 复位、初始化、配置与管理 | 799–878 | ✅ Done | [📄 CXL3.2_Spec_第9章_ch09_Reset_Initialization_Configuration_Manageability_复位初始化配置与管理.md](CXL3.2_Spec_第9章_ch09_Reset_Initialization_Configuration_Manageability_复位初始化配置与管理.md) |
| 10 | Power Management | 电源管理 | 879–891 | ✅ Done | [📄 CXL3.2_Spec_第10章_ch10_Power_Management_电源管理.md](CXL3.2_Spec_第10章_ch10_Power_Management_电源管理.md) |
| 11 | CXL Security | CXL 安全 | 892–997 | ✅ Done | [📄 CXL3.2_Spec_第11章_ch11_CXL_Security_CXL安全.md](CXL3.2_Spec_第11章_ch11_CXL_Security_CXL安全.md) |
| 12 | Reliability, Availability, and Serviceability | 可靠性、可用性与可服务性 | 998–1010 | ✅ Done | [📄 CXL3.2_Spec_第12章_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md](CXL3.2_Spec_第12章_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md) |
| 13 | Performance Considerations | 性能考量 | 1011–1019 | ✅ Done | [📄 CXL3.2_Spec_第13章_ch13_Performance_Considerations_性能考量.md](CXL3.2_Spec_第13章_ch13_Performance_Considerations_性能考量.md) |
| 14 | CXL Compliance Testing + Appendix | CXL 一致性测试 + 附录 | 1020–1233 | ✅ Done | [📄 CXL3.2_Spec_第14章_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md](CXL3.2_Spec_第14章_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md) |

---

## 🗂 目录结构 (Directory Layout)

```
CXL_zh/
├── README.md                                                # 本文件
├── CXL3.2_Spec_第1章_ch01_Introduction_引言.md             # 14 章节 MD (1.7 MB)
├── CXL3.2_Spec_第2章_ch02_CXL_System_Architecture_CXL系统架构.md
├── CXL3.2_Spec_第3章_ch03_CXL_Transaction_Layer_CXL事务层.md
├── CXL3.2_Spec_第4章_ch04_CXL_Link_Layers_CXL链路层.md
├── CXL3.2_Spec_第5章_ch05_CXL_ARB-MUX_CXL仲裁复用.md
├── CXL3.2_Spec_第6章_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md
├── CXL3.2_Spec_第7章_ch07_Switching_交换.md                 # ⚠️ 缺 Part A
├── CXL3.2_Spec_第8章_ch08_Control_and_Status_Registers_控制与状态寄存器.md  # ⚠️ 缺 Part B+C
├── CXL3.2_Spec_第9章_ch09_Reset_Initialization_Configuration_Manageability_复位初始化配置与管理.md
├── CXL3.2_Spec_第10章_ch10_Power_Management_电源管理.md
├── CXL3.2_Spec_第11章_ch11_CXL_Security_CXL安全.md
├── CXL3.2_Spec_第12章_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md
├── CXL3.2_Spec_第13章_ch13_Performance_Considerations_性能考量.md
├── CXL3.2_Spec_第14章_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md
└── figures/
    ├── chapter_01/page_*.png  ~  page_*.png                  # 14 章原图 (~25 MB)
    └── chapter_01/fig_*.{png,jpx}                            # 嵌入图
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
  - `translate-book` — 并发批量翻译 (本次使用, 受 API 速率限制)

---

## ⚠️ 已知问题

1. **Ch7 缺 Part A** (p.319–380, 60 页): 由于 API 速率限制 (Token Plan Plus 5h limit), Part A 子 agent 在限制生效前未能完成
2. **Ch8 缺 Part B+C** (p.556–675, 120 页): Part B 触发内容过滤器 `output new_sensitive`, Part C 多次重试均因 429 失败

### 续传方案

API 速率限制将于 **20:00 (UTC+8) 重置**。重置后可重新调度:
- Ch7 Part A (p.319–380, ~120K 字)
- Ch8 Part B+C (p.556-675, ~150K 字)

```bash
# 重置后可执行
bash /tmp/resume_translation.sh
```

---

## ⏭️ 下一步

- [ ] **API 速率限制重置后** (20:00 UTC+8) 续传 Ch7 Part A + Ch8 Part B+C
- [ ] 合并最终分块, 重新推送
- [ ] 校对与精修: 由人工或下次 API 配额恢复时, 重点校对 Ch3 (核心协议) 与 Ch11 (安全) 的关键术语一致性

---

> 🤖 **Generated with** [Claude Code](https://claude.com/claude-code) · Opus 4.8
> 📅 2026-06-06
