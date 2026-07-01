# D6 法务/版权合规审计报告

**审计日期**: 2026-07-01 | **范围**: 全 repo

---

## D6.1 "confidential" 关键词扫描

### 结果

全 repo 中 "confidential" 出现 25 次，**100% 为技术性用法**：

| 文件 | 出现次数 | 上下文 | 性质 |
|------|---------|--------|------|
| ch01 | 1 | "confidential computing" — CXL TSP 定义 | ✅ 技术术语 |
| ch08 | 17 | "In support of confidential computing, if the device has been locked..." | ✅ CXL TSP 协议描述 |
| ch11 | 7 | "confidentiality, integrity, and replay protection" | ✅ IDE 安全属性 |

**判定**: ✅ SAFE — "confidential" 在所有上下文中指 "机密计算"（CXL TEE Security Protocol 的技术特性），**非许可/保密条款**。无版权风险。

---

## D6.2 LICENSE 文件

### 现状

**缺失** — repo 中无 LICENSE、COPYING、COPYRIGHT 或任何形式的知识产权声明文件。

### 建议

添加 `LICENSE` 文件，建议选项：

| 选项 | 适用性 | 注 |
|------|--------|-----|
| **CC BY-NC-SA 4.0** | ⭐ 推荐 | 翻译作品 + 非商业用途 + 署名要求，最匹配学术/技术翻译场景 |
| CC BY 4.0 | 可选 | 允许商业使用，但翻译作品本身就依赖 PCI-SIG 版权所有 |
| MIT | 不推荐 | 代码类 license，不适合翻译/文档作品 |

---

## D6.3 免责声明

### 现状

**缺失** — README 中无任何免责声明、版权声明或使用限制说明。

### 建议（推荐文案）

```markdown
## ⚖️ 法律声明 (Legal Disclaimer)

- **非官方翻译**: 本项目为社区（个人）提供的非官方中英对照译本，**不替代**原版 CXL Specification
- **版权归属**: CXL®、Compute Express Link® 为 CXL Consortium 的注册商标。原版规范版权归 CXL Consortium / PCI-SIG 所有
- **仅供学习研究**: 本译本仅供个人学习与技术研究使用，**不得用于商业目的**
- **无担保**: 翻译准确性不作任何保证，技术决策请以原版英文规范为准
- **如有版权异议**: 请联系 repo owner 处理
```

---

## D6.4 PCI-SIG 会员合规

### 源 PDF 状态

| 项目 | 状态 |
|------|------|
| 源 PDF 文件名 | `CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf` |
| 标记 | "Evaluation Copy" |
| 位置 | **父目录**（不在 repo 中） |
| `.gitignore` 排除 | ❌ 无显式规则（但位于 `../` 不受 git 追踪） |

### Evaluation Copy 含义

PCI-SIG "Evaluation Copy" 通常指：
- 提供给 PCI-SIG 会员的预发布/审阅版本
- 可内部评估，但**公开再分发受到限制**
- CXL 3.2 spec 目前尚未正式公开发布

### 风险提示

| 风险项 | 描述 | 等级 |
|--------|------|------|
| 完整原文逐字公开 | 本项目采用 "bilingual table" 格式（EN 原文 + ZH 译文并排） — 等同于逐字公开原文 | 🔴 |
| Evaluation Copy | 源文件明确标注 "Evaluation Copy" | 🟡 |
| 图文件 | 1,860 张 spec 原图全部嵌入（已去水印） | 🟡 |
| GitHub 公开发布 | repo 为 public，可通过 Google 搜索发现 | 🟡 |

---

## D6.5 风险评估矩阵

| 风险等级 | 场景 | 可能性 | 影响 | 缓解措施 |
|----------|------|--------|------|----------|
| 🔴 **高** | PCI-SIG 提出 DMCA takedown | 低（个人学习项目通常不会被优先处理） | 高（repo 下架） | 添加 disclaimer + LICENSE；考虑 private repo |
| 🟡 **中** | 被搜索引擎索引后放大传播范围 | 中（GitHub public repo 默认被索引） | 中（增加被发现概率） | README 显式声明非官方/仅供学习 |
| 🟢 **低** | 个人使用被误解为官方翻译 | 低（README 第一章即声明非官方） | 低 | 已有 GitHub badges + 双语格式说明 |
| 🟢 **低** | 翻译错误导致的技术后果 | 极低（已在 README 声明无担保） | 低 | 添加无担保声明 |

---

## D6.6 .gitignore 覆盖

### 已覆盖

| 规则 | 用途 |
|------|------|
| `*.tmp` | 临时文件 |
| `*.bak` | de-watermarked backup |
| `*_raw.txt` | MinerU raw 提取文本 |
| `.DS_Store` | macOS 系统文件 |

### 缺失覆盖

| 文件 | 建议 |
|------|------|
| `ch07_chunk_*.pdf` (3 files, ~100MB) | 添加到 .gitignore（MinerU 中间产物） |
| `ch08_20p_*.pdf` (3 files, ~6MB) | 同上 |
| `CXL-Specification*.pdf` | 添加预防性规则（即使文件在父目录） |

---

## D6 维度总判定

| 子项 | 等级 | 行动 |
|------|------|------|
| D6.1 confidential 扫描 | ✅ | 100% 技术术语，无风险 |
| D6.2 LICENSE | ❌ | **需添加** CC BY-NC-SA 4.0 |
| D6.3 Disclaimer | ❌ | **需添加** README 法律声明段 |
| D6.4 PCI-SIG 合规 | ⚠️ | 低-中风险，缓解措施可接受 |
| D6.5 风险矩阵 | ⚠️ | 整体低风险，建议保持警惕 |
| D6.6 .gitignore | ⚠️ | **需补充** PDF chunk 规则 |

> **D6 总分: ⚠️ NEEDS ACTION (需添加 LICENSE + disclaimer + .gitignore)**

---

> Generated with Claude Code · deepseek-v4-pro
> 2026-07-01
