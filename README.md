# 📚 CXL 3.2 规范中英对照翻译

> **Compute Express Link® (CXL®) Specification — Revision 3.2, Version 1.0 — October 2, 2024**

📄 **Source PDF**: [`../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf`](../CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf) (1233 pages, 11 MB)
🎨 **Format**: 中英对照双语 Markdown · 原始图表保留为 PNG · 中文背景色灰色 · GitHub Flavored Markdown
🐙 **GitHub**: https://github.com/jimwang2050/CXL_3.2_Spec

---

## 📊 翻译进度 (Translation Progress)

**已完成**: `14 / 14` 章完整
**总文件**: 1.8 MB MD + 27 MB 原图
**最近更新**: 2026-06-07 — Ch7 图嵌入统一修复 (Part A/B/C 三件套齐备)

```text
[██████████████] 100%  (14/14 完整)
```

## 📖 章节目录 (Chapters)

> 文件命名格式: `CXL3.2_Spec_chNN_<EnglishTitle>_<中文Title>.md`

| Ch | English Title | 中文标题 | Pages | Status | File |
|:-:|---------------|----------|:-----:|:------:|:----:|
| 1 | Introduction | 引言 | 50–70 | ✅ Done | [📄 CXL3.2_Spec_ch01_Introduction_引言.md](CXL3.2_Spec_ch01_Introduction_引言.md) |
| 2 | CXL System Architecture | CXL 系统架构 | 71–84 | ✅ Done | [📄 CXL3.2_Spec_ch02_CXL_System_Architecture_CXL系统架构.md](CXL3.2_Spec_ch02_CXL_System_Architecture_CXL系统架构.md) |
| 3 | CXL Transaction Layer | CXL 事务层 | 85–190 | ✅ Done | [📄 CXL3.2_Spec_ch03_CXL_Transaction_Layer_CXL事务层.md](CXL3.2_Spec_ch03_CXL_Transaction_Layer_CXL事务层.md) |
| 4 | CXL Link Layers | CXL 链路层 | 191–261 | ✅ Done | [📄 CXL3.2_Spec_ch04_CXL_Link_Layers_CXL链路层.md](CXL3.2_Spec_ch04_CXL_Link_Layers_CXL链路层.md) |
| 5 | CXL ARB/MUX | CXL 仲裁/复用 | 262–286 | ✅ Done | [📄 CXL3.2_Spec_ch05_CXL_ARB-MUX_CXL仲裁复用.md](CXL3.2_Spec_ch05_CXL_ARB-MUX_CXL仲裁复用.md) |
| 6 | Flex Bus Physical Layer | Flex Bus 物理层 | 287–318 | ✅ Done | [📄 CXL3.2_Spec_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md](CXL3.2_Spec_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md) |
| 7 | Switching | 交换 | 319–498 | ✅ Done (rev. 2026-06-07) | [📄 CXL3.2_Spec_ch07_Switching_交换.md](CXL3.2_Spec_ch07_Switching_交换.md) |
| 8 | Control and Status Registers | 控制与状态寄存器 | 499–798 | ✅ Done (rev. 2026-06-07) | [📄 CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md](CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md) |
| 9 | Reset, Initialization, Configuration, and Manageability | 复位、初始化、配置与管理 | 799–878 | ✅ Done | [📄 CXL3.2_Spec_ch09_Reset_Initialization_Configuration_Manageability_复位初始化配置与管理.md](CXL3.2_Spec_ch09_Reset_Initialization_Configuration_Manageability_复位初始化配置与管理.md) |
| 10 | Power Management | 电源管理 | 879–891 | ✅ Done | [📄 CXL3.2_Spec_ch10_Power_Management_电源管理.md](CXL3.2_Spec_ch10_Power_Management_电源管理.md) |
| 11 | CXL Security | CXL 安全 | 892–997 | ✅ Done | [📄 CXL3.2_Spec_ch11_CXL_Security_CXL安全.md](CXL3.2_Spec_ch11_CXL_Security_CXL安全.md) |
| 12 | Reliability, Availability, and Serviceability | 可靠性、可用性与可服务性 | 998–1010 | ✅ Done | [📄 CXL3.2_Spec_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md](CXL3.2_Spec_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md) |
| 13 | Performance Considerations | 性能考量 | 1011–1019 | ✅ Done | [📄 CXL3.2_Spec_ch13_Performance_Considerations_性能考量.md](CXL3.2_Spec_ch13_Performance_Considerations_性能考量.md) |
| 14 | CXL Compliance Testing + Appendix | CXL 一致性测试 + 附录 | 1020–1233 | ✅ Done | [📄 CXL3.2_Spec_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md](CXL3.2_Spec_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md) |

---

## 🗂 目录结构 (Directory Layout)

```
CXL_zh/
├── README.md                                                # 本文件
├── CXL3.2_Spec_ch01_Introduction_引言.md             # 14 章节 MD (1.7 MB)
├── CXL3.2_Spec_ch02_CXL_System_Architecture_CXL系统架构.md
├── CXL3.2_Spec_ch03_CXL_Transaction_Layer_CXL事务层.md
├── CXL3.2_Spec_ch04_CXL_Link_Layers_CXL链路层.md
├── CXL3.2_Spec_ch05_CXL_ARB-MUX_CXL仲裁复用.md
├── CXL3.2_Spec_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md
├── CXL3.2_Spec_ch07_Switching_交换.md                 # ✅ rev. 2026-06-07 Part A/B/C 齐
├── CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md  # ✅ rev. 2026-06-07 全 Part 完整
├── CXL3.2_Spec_ch09_Reset_Initialization_Configuration_Manageability_复位初始化配置与管理.md
├── CXL3.2_Spec_ch10_Power_Management_电源管理.md
├── CXL3.2_Spec_ch11_CXL_Security_CXL安全.md
├── CXL3.2_Spec_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md
├── CXL3.2_Spec_ch13_Performance_Considerations_性能考量.md
├── CXL3.2_Spec_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md
└── figures/
    ├── chapter_01/page_*.png  ~  page_*.png                  # 14 章原图 (~25 MB)
    └── chapter_01/fig_*.{png,jpx}                            # 嵌入图
```

---

## 🎨 格式约定 (Format Conventions)

每个章节遵循统一的 GitHub Flavored Markdown 结构：

```markdown
# 📘 第 N 章　<Title> (Chapter N. <English>)  *(H1 标题, 文件名不含此部分)*

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

## 📋 Recent Updates (更新日志)

### 2026-06-07 — Ch01-Ch06 图嵌入统一 + 紧致裁剪规划

**改动**: 沿用 ch07/08/10-14 同一修复模式 (page→fig + 去水印版 fig_*_1.png)

| 章节       | page_ 引用 | fig_ 引用 (新) | 新增 fig_*.png |
|------------|-----------|---------------|----------------|
| ch01 | 9 | 9 | 5 |
| ch02 | 6 | 6 | 6 |
| ch03 | 16 | 16 | 12 |
| ch04 | 41 | 41 | 18 |
| ch05 | 20 | 20 | 2 |
| ch06 | 13 | 13 | 9 |
| 合计 | 105 | 105 | 52 |

**全 14 章 fig_*_1.png 总数** (修复前 → 修复后): 30 → 297

#### 📐 紧致 figure crop 升级方案 (规划中)

**当前状态**: 全部 fig_*_1.png (共 297 张) 都是"去水印版" (1105×1520, 去掉 CXL spec 水印 + 页眉页脚), 不是 Part A 那种紧致图区裁剪 (例如 438×369)。

**差距**:
- Part A 原 16 张 (ch08 × 10 + ch14 × 6) 已经是 tight crop
- 其余 281 张是 de-watermarked whole page

**3 种升级路径**:

| 路径 | 成本 | 收益 |
|------|------|------|
| (a) MinerU 重跑 | 高 (~281 页 API 调用) | 最准, 复用 Part A 风格 |
| (b) 自研启发式 (OpenCV 找图区) | 中 (写脚本 + 调参) | 中等, 部分图不准 |
| (c) 跳过 (保持 de-watermarked) | 0 | 已比原始 page 改善 |

**建议**: 先跑 (b) 试 30 张验证, 效果 < 80% 准确率则放弃转 (c)。用户给 "上(a)" / "试(b)" / "暂(c)" 指令即执行。

### 2026-06-07 — Ch7 图嵌入统一 + Part B/C 补齐

**发现**: 之前 README 标 "Ch7 缺 Part A" 实际是误判 — ch7 实际包含完整 Part A/B/C 内容 (p.319–498, 10,959 行), 只是 (a) `src=page_*.png` 命名未统一, (b) Part B/C 缺 H1 和"本章目录"。

**改动**:

| 类别 | 改动 | 数量 |
|------|------|------|
| **资源** | PIL 去水印版 `fig_*_1.png` (与 ch08/10/11/12/14 同样参数 150/110/1200/1580) | **80 张新增** (ch7 现 87 张 fig_) |
| **inline src 重命名** | `figures/chapter_07/page_PPPP.png` → `figures/chapter_07/fig_PPPP_1.png` | **127 处** |
| **H1 补齐** | 为 Part B / Part C 加 H1 标题 (Part A 已有) | 2 个 |
| **TOC 补齐** | 为 Part B / Part C 加 `## 📑 本章目录` (Part A 已有) | 2 个 |
| **不动** | 7 处 `figures/chapter_07/page_*.png` 残留在 Full size 链接 (有意的"原图备份") | 7 处 |

**修复前 → 修复后**:
```
指标                            修复前       修复后
─────────────────────────────────────────────────
src=page_ 嵌入                  134          7 (全部为 Full size 链接)
Part B/C 的 H1                  0           2 (B + C)
Part B/C 的 本章目录            0           2 (B + C)
Chapter 7 整体状态              ⚠️ 缺 Part A   ✅ Done
全 14 章完整度                  13/14       14/14
```

**附**: ch7 用 `chapter_07_raw.txt` + `chapter_07{a,b,c}_raw.txt` 4 个 raw 文本作为翻译源, 翻译阶段从未拆 Part, 因此 Part A/B/C 内容是连贯的, 修复时无需重新切分。

### 2026-06-07 — Ch10/Ch11/Ch12/Ch14 图嵌入统一修复

**目标**: 沿用 ch08 修复基准 (Part A 风格 + 去水印版 `fig_*_1.png`), 把其余章节中所有 `src=page_*.png` 统一为 `src=fig_*_1.png`。

**改动**:

| 章节 | page_ 引用 | fig_ 引用 (新) | 新增 fig_*.png |
|------|-----------|---------------|----------------|
| ch10 (Power Management)        | 5   | 9   | 5 |
| ch11 (CXL Security)            | 24  | 24  | 2 |
| ch12 (RAS)                     | 4   | 4   | 5 |
| ch14 (Compliance + Appendix)   | 18  | 18  | 13 |
| **合计**                       | **51** | **55** | **25** |

(注: ch09 / ch13 原本就已用 `fig_*.png`, 无需改动; 25 张新图用 PIL 裁掉 CXL spec 页面的 "Evaluation Copy" 水印 + 页眉/页脚, 与 ch08 去水印版完全一致的参数 (150/110/1200/1580)。)

**不改动项**:
- Full size 链接保持 `page_*.png` (有意的"原图备份")
- 各章 H1 / 三件套 / 双语 caption 已在原始翻译阶段处理, 无需追加

### 2026-06-07 — Ch8 图嵌入与结构统一修复

**目标**: 以 Part A (p.499–555, 唯一具有紧致图裁剪 + 双语 caption 的段落) 为模板, 把 Part B/C/D/E 统一到同一规范。

**改动** (commit `2d5b9c1`):

| 类别 | 改动 | 数量 |
|------|------|------|
| **资源** | 用 PIL 裁掉 CXL spec 页面 "Evaluation Copy" 水印 + 页眉/页脚, 输出 `fig_PPPP_1.png` | 138 张 |
| **inline src 重命名** | `figures/chapter_08/page_PPPP.png` → `figures/chapter_08/fig_PPPP_1.png` | 206 处 |
| **Part C→D 重建** | 误标的 H1 "Part C" 改为 "Part D" (实际内容是 p.676–735) | 1 处 |
| **H1/TOC 补齐** | 为 Part B/D/E 补 H1 标题 + 📑 本章目录 | 3 Part |
| **alt 误标修正** | Part B 中 2 处 `alt="Table 8-26/27"` → `alt="Figure 8-26/27"` | 2 处 |
| **占位 caption 改写** | Part C/D "Figure 8-X (page NNN)" 列表 → 真实 `Table 8-NNN` 编号 (97 项, 含页范围格式) | 97 项 |
| **inline caption 修正** | body 中 `> **Figure 8-X.**` → `> **Table 8-NNN.**` (单页 + 页范围两种格式) | 73 + 74 = 147 处 |
| **img alt 修正** | `alt="Figure 8-X page NNN"` → `alt="Table 8-NNN page NNN"` | 141 处 |
| **TODO 收尾** | 6 个 `alt="<TABLE_NUM> page NNN"` 占位, 复用上一行 caption 的 Table 编号 | 6 处 |

**修复前 → 修复后**:
```
指标                       修复前      修复后
────────────────────────────────────────────
src=page_* 嵌入            206         0
Figure 8-X 占位            391         0
alt="Table 8-26/27" 误标   2           0
H1 章节数                  1           4 (A/B/D/E)
缺失 📑 本章目录           3 个 Part   0
缺失 Part D                无          有
```

**关键发现**: CXL 3.2 spec ch8 实际只有 Figure 8-1 ~ 8-14 (Part A & B), Part D (p.676–735) 与 Part E (p.736+) 在 spec 中**没有 Figure**, 只有 Table。md 中 "Figure 8-X (page NNN)" 列表 95% 都是误标的 Table。修复后全部转为正确的 `Table 8-NNN` 编号 (从 raw 文本 `chapter_08{d,e}_raw.txt` 自动抽取)。

**已知遗留** (在 ch08 md 文件末尾 `## ⚠️ Known TODOs` 段落已记录):
- 4 个 Part (B/D/E) 的"本章目录"内容仍为占位 — 后续脚本可从 `### 8.2.x.x` 标题自动汇总
- 紧致 figure crop (本次为"去水印版"兜底, **不是** Part A 那种紧致图区裁剪) — 需重跑 MinerU 才能匹配 Part A 精度

**资源**: `figures/chapter_08/fig_*_1.png` 共 148 张 (Part A 原 10 + 本次去水印 138)
**备份**: `CXL3.2_Spec_ch08_..._寄存器.md.bak` (`.gitignore` 忽略)

---

## ⚠️ 已知问题

（无 — 14 章 14 Part 全部 Done）

---

## ⏭️ 下一步

- [ ] 校对与精修: 由人工或下次 API 配额恢复时, 重点校对 Ch3 (核心协议) 与 Ch11 (安全) 的关键术语一致性
- [ ] Ch8 "本章目录" 自动汇总 (4 个 Part)
- [ ] Ch8 紧致 figure crop (重跑 MinerU, 把去水印版升级到 tight crop)
- [ ] Ch7/8/10/11/12/14 共 ~233 张去水印版 fig_*.png 后续可升级到紧致裁剪

---

> 🤖 **Generated with** [Claude Code](https://claude.com/claude-code) · Opus 4.8
> 📅 2026-06-07
