# 📚 CXL 3.2 规范中英对照翻译

> **Compute Express Link® (CXL®) Specification — Revision 3.2, Version 1.0 — October 2, 2024**

📄 **Source PDF**: [`../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf`](../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf) (1233 pages, 11 MB)
🎨 **Format**: 中英对照双语 Markdown · 原始图表保留为 PNG · 中文背景色灰色 · GitHub Flavored Markdown

---

## 📊 翻译进度 (Translation Progress)

**已完成**: `1 / 14` 章 (≈ 7%) ｜ **总页数**: 1233 ｜ **本页**: [Chapter 1 ✅](chapter_01.md)

```text
[████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 7%  (1/14)
```

---

## 📖 章节目录 (Chapters)

| Ch | English Title | 中文标题 | Pages | Status | File |
|:-:|---------------|----------|:-----:|:------:|:----:|
| 1 | Introduction | 引言 | 50–70 | ✅ Done | [📄 chapter_01.md](chapter_01.md) |
| 2 | CXL System Architecture | CXL 系统架构 | 71–84 | ⏳ Pending | chapter_02.md |
| 3 | CXL Transaction Layer | CXL 事务层 | 85–190 | ⏳ Pending | chapter_03.md |
| 4 | CXL Link Layers | CXL 链路层 | 191–261 | ⏳ Pending | chapter_04.md |
| 5 | CXL ARB/MUX | CXL 仲裁/复用 | 262–286 | ⏳ Pending | chapter_05.md |
| 6 | Flex Bus Physical Layer | Flex Bus 物理层 | 287–318 | ⏳ Pending | chapter_06.md |
| 7 | Switching | 交换 | 319–498 | ⏳ Pending | chapter_07.md |
| 8 | Control and Status Registers | 控制与状态寄存器 | 499–798 | ⏳ Pending | chapter_08.md |
| 9 | Reset, Initialization, Configuration, and Manageability | 复位、初始化、配置与管理 | 799–878 | ⏳ Pending | chapter_09.md |
| 10 | Power Management | 电源管理 | 879–891 | ⏳ Pending | chapter_10.md |
| 11 | CXL Security | CXL 安全 | 892–997 | ⏳ Pending | chapter_11.md |
| 12 | Reliability, Availability, and Serviceability | 可靠性、可用性与可服务性 | 998–1010 | ⏳ Pending | chapter_12.md |
| 13 | Performance Considerations | 性能考量 | 1011–1019 | ⏳ Pending | chapter_13.md |
| 14 | CXL Compliance Testing | CXL 一致性测试 | 1020–? | ⏳ Pending | chapter_14.md |
| App | Appendices A–C | 附录 A–C | ?–1233 | ⏳ Pending | appendices.md |

---

## ✅ 已完成任务清单 (Completed Tasks)

- [x] **Chapter 1** Introduction / 引言 (p.50–70)
  - [x] 1.0 引言
  - [x] 1.1 读者对象
  - [x] 1.2 术语与缩略语表（**Table 1-1, 11 sheets, ~250 条全部中英对照**）
  - [x] 1.3 参考文档表（Table 1-2, 2 sheets）
  - [x] 1.4 动机与总体概述（1.4.1 CXL + 1.4.2 Flex Bus, 4 张图引用）
  - [x] 1.5 Flex Bus 链路特性（4 张图引用）
  - [x] 1.6 Flex Bus 分层概览（1 张图 + 1 张 Mermaid 概念图）
  - [x] 1.7 文档范围 + 章节要点

---

## 🗂 目录结构 (Directory Layout)

```
CXL_zh/
├── README.md                       # 本文件 (GitHub 格式)
├── chapter_01.md                   # 第 1 章 引言 (✅ 已完成)
├── chapter_02.md ~ chapter_14.md   # 后续章节 (⏳ 待翻译)
├── appendices.md                   # 附录 A–C (⏳ 待翻译)
└── figures/                        # 原始图表 (PNG 渲染)
    ├── chapter_01/
    │   ├── page_0050.png ~ page_0070.png   # 全页渲染 (保留原 PDF 布局)
    │   └── fig_*.png                        # 提取的嵌入图
    ├── chapter_02/ ~ chapter_14/
    └── appendices/
```

---

## 🎨 格式约定 (Format Conventions)

### 已应用的 GitHub Flavored Markdown 特性

| 特性 | 用途 | 示例 |
|:----|:----|:-----|
| **显式锚点** | 跨设备稳定的目录跳转 | `<a id="sec-1-0"></a>` + `[链接](#sec-1-0)` |
| **HTML 表格** | 实现中文背景色灰色 | `<td style="background-color:#e8e8e8">` |
| **Mermaid 代码块** | 概念图可在线渲染 | ` ```mermaid ` |
| **GFM 任务列表** | 翻译进度可视化 | `- [x] 已完成` / `- [ ] 待办` |
| **Emoji 短码** | 视觉标识 | `📘` `📑` `🖼` `📊` `🇬🇧` `🇨🇳` |
| **相对路径图片** | GitHub 仓库内嵌图 | `![Figure](figures/chapter_01/page_0050.png)` |
| **代码块语言标识** | 语法高亮 | ` ```mermaid ` ` ```text ` ` ```bash ` |
| **文本进度条** | 一目了然的整体进度 | `[████░░░░░░]` |

### 翻译风格

- **专业术语** — 首次出现给出 `EN → 中文` 对照，后续保留英文术语
- **章节标题** — 双语并列，如 `## 1.0 Introduction | 引言`
- **表格** — Markdown 表格 + 中文单元格加灰底（`#e8e8e8`）
- **代码/寄存器字段** — 保留英文，不翻译
- **图片** — 优先用 PNG 引用（`![fig](figures/chapter_01/page_XXXX.png)`），关键概念图用 Mermaid 重绘

---

## 🛠 翻译工具链 (Toolchain)

- **PDF 提取**: [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`) — 文本+布局+图像
- **图渲染**: PyMuPDF (DPI 150) + `pdf2image`
- **Python 依赖**:
  ```bash
  python3 -m pip install --user --trusted-host pypi.org \
    pypdf pdf2image pdfplumber Pillow reportlab pandas openpyxl PyMuPDF pytesseract
  ```
- **辅助 skill** (本仓库已安装):
  - `pdf` — 官方 anthropics/skills/pdf，PDF 基础操作
  - `pdf-content-extractor` — 中文 PDF + OCR + 去水印
  - `mineru` — 高质量 PDF → Markdown（云端 API）
  - `book-to-skill` — 把整本书转成可查询 skill

---

## ➡️ 下一步 (Next Steps)

- [ ] **Chapter 2** — CXL System Architecture (p.71–84, ~14 页) — 建议优先
- [ ] **Chapter 3** — CXL Transaction Layer (p.85–190, ~106 页) — 核心协议
- [ ] **Chapter 4** — CXL Link Layers (p.191–261, ~71 页)
- [ ] 后续章节按需继续

> 💬 需要我继续翻译哪一章？建议从 **Chapter 2** 开始（中量级，可快速验证完整流程）。
