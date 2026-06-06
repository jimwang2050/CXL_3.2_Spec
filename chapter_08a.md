# 📘 第 8 章　控制与状态寄存器 (Chapter 8. Control and Status Registers) — Part A

> **Source pages**: 499–555 (Part A) | **File**: chapter_08a.md | **Format**: 中英对照双语

## 📑 本章目录 (Part A)

- [8.0 Control and Status Registers | 控制与状态寄存器](#sec-8-0)
- [8.1 Configuration Space Registers | 配置空间寄存器](#sec-8-1)
  - [8.1.1 PCIe Designated Vendor-Specific Extended Capability (DVSEC) ID Assignment | PCIe 指定厂商特定扩展能力 (DVSEC) ID 分配](#sec-8-1-1)
  - [8.1.2 CXL Data Object Exchange (DOE) Type Assignment | CXL 数据对象交换 (DOE) 类型分配](#sec-8-1-2)
  - [8.1.3 PCIe DVSEC for CXL Devices | CXL 设备的 PCIe DVSEC](#sec-8-1-3)
    - [8.1.3.1 DVSEC CXL Capability (Offset 0Ah) | DVSEC CXL 能力 (偏移 0Ah)](#sec-8-1-3-1)
    - [8.1.3.2 DVSEC CXL Control (Offset 0Ch) | DVSEC CXL 控制 (偏移 0Ch)](#sec-8-1-3-2)
    - [8.1.3.3 DVSEC CXL Status (Offset 0Eh) | DVSEC CXL 状态 (偏移 0Eh)](#sec-8-1-3-3)
    - [8.1.3.4 DVSEC CXL Control2 (Offset 10h) | DVSEC CXL 控制 2 (偏移 10h)](#sec-8-1-3-4)
    - [8.1.3.5 DVSEC CXL Status2 (Offset 12h) | DVSEC CXL 状态 2 (偏移 12h)](#sec-8-1-3-5)
    - [8.1.3.6 DVSEC CXL Lock (Offset 14h) | DVSEC CXL 锁 (偏移 14h)](#sec-8-1-3-6)
    - [8.1.3.7 DVSEC CXL Capability2 (Offset 16h) | DVSEC CXL 能力 2 (偏移 16h)](#sec-8-1-3-7)
    - [8.1.3.8 DVSEC CXL Range Registers | DVSEC CXL 范围寄存器](#sec-8-1-3-8)
    - [8.1.3.9 DVSEC CXL Capability3 (Offset 38h) | DVSEC CXL 能力 3 (偏移 38h)](#sec-8-1-3-9)
  - [8.1.4 Non-CXL Function Map DVSEC | 非 CXL 功能映射 DVSEC](#sec-8-1-4)
  - [8.1.5 CXL Extensions DVSEC for Ports | 端口的 CXL 扩展 DVSEC](#sec-8-1-5)
  - [8.1.6 GPF DVSEC for CXL Port | CXL 端口的 GPF DVSEC](#sec-8-1-6)
  - [8.1.7 GPF DVSEC for CXL Device | CXL 设备的 GPF DVSEC](#sec-8-1-7)
  - [8.1.8 PCIe DVSEC for Flex Bus Port | Flex Bus 端口的 PCIe DVSEC](#sec-8-1-8)
  - [8.1.9 Register Locator DVSEC | 寄存器定位器 DVSEC](#sec-8-1-9)
  - [8.1.10 MLD DVSEC | MLD DVSEC](#sec-8-1-10)
  - [8.1.11 Table Access DOE | 表访问 DOE](#sec-8-1-11)
  - [8.1.12 Memory Device Configuration Space Layout | 内存设备配置空间布局](#sec-8-1-12)
  - [8.1.13 FM Mailbox CCI Configuration Space Layout | FM 邮箱 CCI 配置空间布局](#sec-8-1-13)
- [8.2 Memory Mapped Registers | 内存映射寄存器](#sec-8-2)
  - [8.2.1 RCD Upstream Port and RCH Downstream Port Registers | RCD 上行端口和 RCH 下行端口寄存器](#sec-8-2-1)
  - [8.2.2 Accessing Component Registers | 访问组件寄存器](#sec-8-2-2)
  - [8.2.3 Component Register Layout and Definition | 组件寄存器布局和定义](#sec-8-2-3)
  - [8.2.4 CXL.cache and CXL.mem Registers | CXL.cache 和 CXL.mem 寄存器](#sec-8-2-4)

## 🖼 本章图表 (Part A)

- **Figure 8-1** — PCIe DVSEC for CXL Devices (p.502)
- **Figure 8-2** — Non-CXL Function Map DVSEC (p.514)
- **Figure 8-3** — CXL Extensions DVSEC for Ports (p.517)
- **Figure 8-4** — GPF DVSEC for CXL Port (p.522)
- **Figure 8-5** — GPF DVSEC for CXL Device (p.524)
- **Figure 8-6** — Register Locator DVSEC with 3 Register Block Entries (p.525)
- **Figure 8-7** — MLD DVSEC (p.527)
- **Figure 8-8** — RCD and RCH Memory Mapped Register Regions (p.532)
- **Figure 8-9** — RCH Downstream Port RCRB (p.533)
- **Figure 8-10** — RCD Upstream Port RCRB (p.535)
- **Figure 8-11** — PCIe DVSEC for Flex Bus Port (p.537)

## 📊 本章表格 (Part A)

- **Table 8-1** — Register Attributes (p.499)
- **Table 8-2** — CXL DVSEC ID Assignment (p.500-501)
- **Table 8-3** — CXL DOE Type Assignment (p.501)
- **Table 8-4** — PCIe DVSEC CXL Devices - Header (p.502)
- **Table 8-5** — Non-CXL Function Map DVSEC - Header (p.514)
- **Table 8-6** — CXL Extensions DVSEC for Ports - Header (p.517)
- **Table 8-7** — GPF DVSEC for CXL Port - Header (p.523)
- **Table 8-8** — GPF DVSEC for CXL Device - Header (p.524)
- **Table 8-9** — Register Locator DVSEC - Header (p.526)
- **Table 8-10** — Designated Vendor Specific Register Block Header (p.527)
- **Table 8-11** — MLD DVSEC - Header (p.528)
- **Table 8-12** — Coherent Device Attributes - Data Object Header (p.528)
- **Table 8-13** — Read Entry Request (p.529)
- **Table 8-14** — Read Entry Response (p.529)
- **Table 8-15** — Memory Device PCIe Capabilities and Extended Capabilities (p.530)
- **Table 8-16** — PCIe Configuration Space Header - Class Code Register (Offset 09h) for FM Mailbox CCI (p.530)
- **Table 8-17** — CXL Memory Mapped Register Regions (p.531)
- **Table 8-18** — RCH Downstream Port PCIe Capabilities and Extended Capabilities (p.533-534)
- **Table 8-19** — RCD Upstream Port PCIe Capabilities and Extended Capabilities (p.536)
- **Table 8-20** — PCIe DVSEC Header Register Settings for Flex Bus Port (p.537)
- **Table 8-21** — CXL Subsystem Component Register Ranges (p.542)
- **Table 8-22** — CXL_Capability_ID Assignment (p.543)
- **Table 8-23** — CXL.cache and CXL.mem Architectural Register Discovery (p.544)
- **Table 8-24** — CXL.cache and CXL.mem Architectural Register Header Example (Primary Range) (p.544)
- **Table 8-25** — CXL.cache and CXL.mem Architectural Register Header Example (Any Extended Range) (p.544)

---

<a id="sec-8-0"></a>
## 8.0 Control and Status Registers | 控制与状态寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CXL component control and status registers are mapped into separate spaces:</td><td style="background-color:#e8e8e8">CXL 组件的控制和状态寄存器被映射到独立的地址空间中：</td></tr>
<tr><td>• Configuration Space: Registers are accessed using configuration reads and configuration writes</td><td style="background-color:#e8e8e8">• 配置空间 (Configuration Space)：使用配置读和配置写访问寄存器</td></tr>
<tr><td>• Memory mapped space: Registers are accessed using memory reads and memory writes</td><td style="background-color:#e8e8e8">• 内存映射空间 (Memory Mapped Space)：使用内存读和内存写访问寄存器</td></tr>
<tr><td>Table 8-1 summarizes the attributes for the register bits defined in this chapter. Unless specified otherwise, the definition of these attributes is consistent with PCIe* Base Specification.</td><td style="background-color:#e8e8e8">表 8-1 总结了本章所定义寄存器位的属性。除非另有说明，这些属性的定义与 PCIe* 基础规范保持一致。</td></tr>
<tr><td>All numeric values in various registers and data structures are always encoded in little-endian format. All UUIDs in this section follow the format defined in the IETF RFC 4122 specification.</td><td style="background-color:#e8e8e8">各种寄存器和数据结构中的所有数值始终采用小端 (little-endian) 格式编码。本节中的所有 UUID 均遵循 IETF RFC 4122 规范中定义的格式。</td></tr>
<tr><td>CXL components have the same requirements as PCIe with respect to hardware initializing the register fields to their default values, with notable exceptions for system-integrated devices. See PCIe Base Specification for details.</td><td style="background-color:#e8e8e8">关于硬件将寄存器字段初始化为默认值的要求，CXL 组件与 PCIe 相同（系统集成设备除外）。详见 PCIe 基础规范。</td></tr>
</tbody>
</table>

> **Table 8-1.** Register Attributes ｜ 寄存器属性
>
> | Attribute | Description |
> |---|---|
> | RO | Read Only — 只读 |
> | ROS | Read Only Sticky: Not affected by CXL Reset. Otherwise, the behavior follows PCIe Base Specification. — 只读粘性：不受 CXL Reset 影响；其他行为遵循 PCIe 基础规范。 |
> | RW | Read-Write — 读写 |
> | RWS | Read-Write-Sticky: Not affected by CXL Reset. Otherwise, the behavior follows PCIe Base Specification. — 读写粘性：不受 CXL Reset 影响；其他行为遵循 PCIe 基础规范。 |
> | RWO | Read-Write-One-To-Lock: This attribute is not defined in PCIe Base Specification and is unique to CXL.<br/>Field becomes RO after writing 1 to it. Cleared by a hot reset, a warm reset, or a cold reset. Not affected by CXL Reset. — 写 1 锁定 (RWO)：该属性在 PCIe 基础规范中未定义，是 CXL 独有的。<br/>写入 1 后字段变为 RO。在热复位、温复位或冷复位时清除。不受 CXL Reset 影响。 |
> | RWL | Read-Write-Lockable: This attribute is not defined in PCIe Base Specification and is unique to CXL.<br/>These bits follow RW behavior until they are locked. After the bits are locked, the value cannot be altered by software until the next hot reset, warm reset, or cold reset. Upon hot reset, warm reset, or cold reset, the behavior reverts back to RW. Not affected by CXL Reset after the bits are locked. — 可锁定读写 (RWL)：该属性在 PCIe 基础规范中未定义，是 CXL 独有的。<br/>在被锁定之前遵循 RW 行为；锁定后，软件无法修改其值，直到下一次热复位、温复位或冷复位。复位后行为恢复为 RW。锁定后不受 CXL Reset 影响。 |
> | RW1C | Read-Write-One-To-Clear — 写 1 清零 |
> | RW1CS | Read-Write-One-To-Clear-Sticky: Not affected by CXL Reset. Otherwise, the behavior follows PCIe Base Specification. — 写 1 清零粘性：不受 CXL Reset 影响；其他行为遵循 PCIe 基础规范。 |
> | HwInit | Hardware Initialized — 硬件初始化 |
> | RsvdP | Reserved and Preserved — 保留且保持原值 |
> | RsvdZ | Reserved and Zero — 保留且为 0 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1"></a>
## 8.1 Configuration Space Registers | 配置空间寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section describes the Configuration Space registers that may be used to discover and configure CXL functionality. RCH Downstream Port does not map any registers into Configuration Space.</td><td style="background-color:#e8e8e8">本节描述可用于发现和配置 CXL 功能的配置空间寄存器。RCH 下行端口不向配置空间映射任何寄存器。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-1"></a>
## 8.1.1 PCIe Designated Vendor-Specific Extended Capability (DVSEC) ID Assignment | PCIe 指定厂商特定扩展能力 (DVSEC) ID 分配

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CXL specification-defined Configuration Space registers are grouped into blocks, and each block is enumerated as a PCIe Designated Vendor-Specific Extended Capability (DVSEC) structure. The DVSEC Vendor ID field is set to 1E98h to indicate that these Capability structures are defined by the CXL specification.</td><td style="background-color:#e8e8e8">CXL 规范定义的配置空间寄存器被分组为多个块，每个块都枚举为一个 PCIe 指定厂商特定扩展能力 (DVSEC) 结构。DVSEC Vendor ID 字段设置为 1E98h，以表明这些能力结构由 CXL 规范定义。</td></tr>
<tr><td>The DVSEC Revision field represents the version of the DVSEC structure. The DVSEC Revision is incremented whenever the structure is extended to add more functionality. Backward compatibility shall be maintained during this process. For all values of n, a DVSEC Revision n+1 structure may extend Revision n by replacing fields that are marked as reserved in Revision n, but must not redefine the meaning of existing fields. In addition, Revision n+1 may append new registers to Revision n structure and thereby increasing the DVSEC Length field. Software that was written for a lower Revision may continue to operate on CXL DVSEC structures with a higher Revision, but will not be able to take advantage of new functionality.</td><td style="background-color:#e8e8e8">DVSEC Revision 字段表示 DVSEC 结构的版本。当结构被扩展以添加更多功能时，DVSEC Revision 会递增。在此过程中必须保持向后兼容。对于所有 n 值，DVSEC Revision n+1 结构可以通过替换 Revision n 中标记为保留的字段来扩展 Revision n，但不得重新定义现有字段的含义。此外，Revision n+1 可以向 Revision n 结构追加新寄存器，从而增加 DVSEC Length 字段。针对较低 Revision 编写的软件可以继续在更高 Revision 的 CXL DVSEC 结构上运行，但将无法利用新功能。</td></tr>
<tr><td>The following values of DVSEC ID, as listed in Table 8-2, are defined by the CXL specification.</td><td style="background-color:#e8e8e8">如下表 8-2 所列，DVSEC ID 的以下取值由 CXL 规范定义。</td></tr>
<tr><td>Table 8-2 in this version of the specification does not define the behavior of the CXL fabric switches (see Section 2.7) and G-FAM devices (see Section 2.8).</td><td style="background-color:#e8e8e8">本规范此版本的表 8-2 未定义 CXL 交换网交换器 (见 2.7 节) 和 G-FAM 设备 (见 2.8 节) 的行为。</td></tr>
</tbody>
</table>

> **Table 8-2.** CXL DVSEC ID Assignment (Sheet 1 of 2) ｜ CXL DVSEC ID 分配 (第 1 页/共 2 页)
>
> | CXL Capability | DVSEC ID | Highest DVSEC Revision | Mandatory¹ | Not Permitted¹ | Optional¹ |
> |---|---|---|---|---|---|
> | PCIe DVSEC for CXL Devices (see Section 8.1.3) | 0000h | 3 | D1, D2, LD, FMLD | P, UP¹, DP¹, R, USP, DSP | — |
> | Non-CXL Function Map DVSEC (see Section 8.1.4) | 0002h | 0 | P, UP¹, DP¹, R, DSP | D1, D2, LD, FMLD, USP² | — |
> | CXL Extensions DVSEC for Ports (formerly known as CXL 2.0 Extensions DVSEC for Ports; see Section 8.1.5) | 0003h | 0 | R, USP, DSP | P, D1, D2, LD, FMLD, UP¹, DP¹ | — |
> | GPF DVSEC for CXL Ports (see Section 8.1.6) | 0004h | 0 | R, DSP | P, D1, D2, LD, FMLD, UP¹, DP¹, USP | — |
> | GPF DVSEC for CXL Devices (see Section 8.1.7) | 0005h | 0 | D2, LD | P, UP¹, DP¹, R, USP, DSP, FMLD | D1 |
> | PCIe DVSEC for Flex Bus Port (see Section 8.1.8) | 0007h | 2 | D1, D2, LD, FMLD, UP¹, DP¹, R, USP, DSP | P | — |
> | Register Locator DVSEC (see Section 8.1.9) | 0008h | 0 | D2, LD, FMLD, R, USP, DSP | P | D1, UP¹, DP¹ |
> | MLD DVSEC (see Section 8.1.10) | 0009h | 0 | FMLD | P, D1, D2, LD, UP¹, DP¹, R, USP, DSP | — |
> | PCIe DVSEC for Test Capability (see Section 14.16.1) | 000Ah | 0 | D1 | P, LD, FMLD, DP¹, UP¹, R, USP, DSP | D2 |
>
> 1. P – PCIe device, D1 – RCD, D2 – SLD, LD – Logical Device, FMLD – Fabric Manager owned LD FFFFh, UP¹ – RCD Upstream Port, DP¹ – RCH Downstream Port, R – CXL root port, USP – CXL Upstream Switch Port, DSP – CXL Downstream Switch Port. A physical component may be capable of operating in multiple modes. For example, a CXL device may operate either as an RCD or SLD based on the link training. In such cases, these definitions refer to the current mode of operation.
> 2. Non-CXL Function Map DVSEC is mandatory for CXL USPs that include a Switch Mailbox CCI as an additional Function.
>
> 1. P – PCIe 设备，D1 – RCD，D2 – SLD，LD – 逻辑设备，FMLD – Fabric Manager 拥有的 LD FFFFh，UP¹ – RCD 上行端口，DP¹ – RCH 下行端口，R – CXL 根端口，USP – CXL 上行交换端口，DSP – CXL 下行交换端口。一个物理组件可能能够以多种模式运行。例如，CXL 设备可能基于链路训练作为 RCD 或 SLD 运行。在这种情况下，这些定义指的是当前的操作模式。
> 2. 对于包含 Switch Mailbox CCI 作为附加功能的 CXL USP，Non-CXL Function Map DVSEC 是必需的。

> **Table 8-2.** CXL DVSEC ID Assignment (Sheet 2 of 2) ｜ CXL DVSEC ID 分配 (第 2 页/共 2 页)
>
> *Header columns as above.*

> **Table 8-3.** CXL DOE Type Assignment ｜ CXL DOE 类型分配
>
> | CXL Capability | DOE Type | Mandatory¹ | Not Permitted¹ | Optional¹ |
> |---|---|---|---|---|
> | Compliance (see Chapter 14.0)² | 0 | LD, FMLD | P, UP¹, DP¹, R, USP, DSP | D1, D2 |
> | Reserved | 1 | — | — | — |
> | Table Access (Coherent Device Attributes; see Section 8.1.11) | 2 | D2, LD, USP | FMLD, P, UP¹, DP¹, R, DSP | D1 |
>
> 1. P – PCIe device, D1 – RCD, D2 – SLD, LD – Logical Device, FMLD – Fabric Manager owned LD FFFFh, UP¹ – RCD Upstream Port, DP¹ – RCH Downstream Port, R – CXL root port, USP – CXL Upstream Switch Port, DSP – CXL Downstream Switch Port. A physical component may be capable of operating in multiple modes. For example, a CXL device may operate either as an RCD or SLD based on the link training. In such cases, these definitions refer to the current mode of operation.
> 2. eRCDs are required to implement PCIe DVSEC for Test Capability (see Section 14.16.1). For all other Devices, support for the Compliance DOE Type is highly recommended and PCIe DVSEC for Test Capability is not required if the Compliance DOE Type is implemented. If Compliance DOE Type is not implemented by a device, the device shall implement PCIe DVSEC for Test Capability (see Section 14.16.1).
>
> 1. P – PCIe 设备，D1 – RCD，D2 – SLD，LD – 逻辑设备，FMLD – Fabric Manager 拥有的 LD FFFFh，UP¹ – RCD 上行端口，DP¹ – RCH 下行端口，R – CXL 根端口，USP – CXL 上行交换端口，DSP – CXL 下行交换端口。一个物理组件可能能够以多种模式运行。例如，CXL 设备可能基于链路训练作为 RCD 或 SLD 运行。在这种情况下，这些定义指的是当前的操作模式。
> 2. eRCD 需要实现 PCIe DVSEC for Test Capability (见 14.16.1 节)。对于所有其他设备，强烈建议支持 Compliance DOE 类型；如果实现了 Compliance DOE 类型，则不需要 PCIe DVSEC for Test Capability。如果设备未实现 Compliance DOE 类型，则设备应实现 PCIe DVSEC for Test Capability (见 14.16.1 节)。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-2"></a>
## 8.1.2 CXL Data Object Exchange (DOE) Type Assignment | CXL 数据对象交换 (DOE) 类型分配

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Data Object Exchange (DOE) is a PCI-SIG-defined mechanism for the host to perform data object exchanges with a PCIe Function.</td><td style="background-color:#e8e8e8">数据对象交换 (DOE, Data Object Exchange) 是 PCI-SIG 定义的机制，用于主机与 PCIe Function 之间执行数据对象交换。</td></tr>
<tr><td>The following values of DOE Type are defined by the CXL specification. The CXL specification-defined DOE Messages use Vendor ID 1E98h.</td><td style="background-color:#e8e8e8">CXL 规范定义了以下 DOE Type 取值。CXL 规范定义的 DOE 消息使用 Vendor ID 1E98h。</td></tr>
<tr><td>Table 8-3 in this version of the specification does not define the behavior of CXL fabric switches (see Section 2.7) and G-FAM devices (see Section 2.8).</td><td style="background-color:#e8e8e8">本规范此版本的表 8-3 未定义 CXL 交换网交换器 (见 2.7 节) 和 G-FAM 设备 (见 2.8 节) 的行为。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3"></a>
## 8.1.3 PCIe DVSEC for CXL Devices | CXL 设备的 PCIe DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>Note:</strong> The CXL 1.1 specification referred to this DVSEC as "PCIe DVSEC for Flex Bus Device" and used the term "Flex Bus" while referring to various register names and fields. The CXL 2.0 specification renamed the DVSEC and the register/field names by replacing the term "Flex Bus" with the term "CXL" while retaining the functionality.</td><td style="background-color:#e8e8e8"><strong>注意：</strong>CXL 1.1 规范将该 DVSEC 称为 "PCIe DVSEC for Flex Bus Device"，并在引用各种寄存器名称和字段时使用 "Flex Bus" 一词。CXL 2.0 规范将该 DVSEC 以及寄存器/字段名称中的 "Flex Bus" 替换为 "CXL"，同时保留原有功能。</td></tr>
<tr><td>An RCD creates a new PCIe enumeration hierarchy. As such, it spawns a new Root Bus and can expose one or more PCIe device numbers and function numbers at this bus number. These are exposed as Root Complex Integrated Endpoints (RCiEP). The PCIe Configuration Space of Device 0, Function 0 shall include the CXL PCIe DVSEC as shown in Figure 8-1.</td><td style="background-color:#e8e8e8">RCD 创建一个新的 PCIe 枚举层级。因此，它派生一个新的根总线 (Root Bus)，并可以在此总线号上公开一个或多个 PCIe 设备号和功能号。这些作为根复合体集成端点 (RCiEP, Root Complex Integrated Endpoint) 公开。设备 0、功能 0 的 PCIe 配置空间应包含 CXL PCIe DVSEC，如图 8-1 所示。</td></tr>
<tr><td>A non-RCD is enumerated like a standard PCIe Endpoint and appears below a CXL Root Port or a CXL Switch. A non-RCD shall expose one PCIe device number and one or more function numbers at the parent Port's secondary bus number. These devices set PCI Express Capabilities Register.Device/Port Type=PCI Express Endpoint and thus appear as standard PCIe Endpoints (EP). The PCIe Configuration Space of Function 0 shall include the CXL PCIe DVSEC as shown in Figure 8-1.</td><td style="background-color:#e8e8e8">非 RCD 像标准 PCIe 端点一样枚举，出现在 CXL 根端口或 CXL 交换器之下。非 RCD 应在父端口的副总线号 (secondary bus number) 上公开一个 PCIe 设备号和一个或多个功能号。这些设备将 PCI Express Capabilities 寄存器的 Device/Port Type 字段设置为 PCI Express Endpoint，因此显示为标准 PCIe 端点 (EP)。功能 0 的 PCIe 配置空间应包含 CXL PCIe DVSEC，如图 8-1 所示。</td></tr>
<tr><td>In either case, the capability, status, and control fields in Function 0 DVSEC control the CXL functionality of the entire device.</td><td style="background-color:#e8e8e8">无论哪种情况，功能 0 DVSEC 中的能力、状态和控制字段都控制整个设备的 CXL 功能。</td></tr>
<tr><td>Software may use the presence of this DVSEC to differentiate between a CXL device and a PCIe device. As such, a standard PCIe device must not expose this DVSEC. See Table 8-2 for the complete listing.</td><td style="background-color:#e8e8e8">软件可以利用此 DVSEC 的存在来区分 CXL 设备和 PCIe 设备。因此，标准 PCIe 设备不得公开此 DVSEC。完整列表请参见表 8-2。</td></tr>
<tr><td>See PCIe Base Specification for a description of the standard DVSEC register fields.</td><td style="background-color:#e8e8e8">有关标准 DVSEC 寄存器字段的描述，请参见 PCIe 基础规范。</td></tr>
<tr><td>To advertise this CXL capability, the standard DVSEC register fields shall be set to the values shown in Table 8-4. The DVSEC Length field is set to 03Ch bytes to accommodate the registers included in the DVSEC. The DVSEC ID is cleared to 0h to advertise that this is a PCIe DVSEC for the CXL Device structure. An RCD may implement a DVSEC Revision of 0h or higher. Devices that are not RCDs must implement a DVSEC Revision of 1h or higher.</td><td style="background-color:#e8e8e8">为了公布此 CXL 能力，标准 DVSEC 寄存器字段应设置为表 8-4 中所示的值。DVSEC Length 字段设置为 03Ch 字节以容纳 DVSEC 中包含的寄存器。DVSEC ID 清零为 0h，以表明这是 CXL Device 结构的 PCIe DVSEC。RCD 可以实现 0h 或更高的 DVSEC Revision。非 RCD 的设备必须实现 1h 或更高的 DVSEC Revision。</td></tr>
</tbody>
</table>

> **Figure 8-1.** PCIe DVSEC for CXL Devices ｜ CXL 设备的 PCIe DVSEC
>
> <img src="figures/chapter_08/fig_0502_1.png" alt="Figure 8-1" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0502.png)

> **Table 8-4.** PCIe DVSEC CXL Devices - Header ｜ CXL 设备的 PCIe DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 3h |
> | | 31:20 | DVSEC Length | 03Ch |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0000h |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-1"></a>
### 8.1.3.1 DVSEC CXL Capability (Offset 0Ah) | DVSEC CXL 能力 (偏移 0Ah)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CXL device-specific registers are described in the following subsections.</td><td style="background-color:#e8e8e8">以下各小节描述了 CXL 设备特定寄存器。</td></tr>
</tbody>
</table>

> **Table 8-5.** DVSEC CXL Capability (Offset 0Ah) ｜ DVSEC CXL 能力 (偏移 0Ah)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RO | **Cache_Capable**: If set, indicates that the CXL.cache protocol is supported when operating in Flex Bus.CXL mode. This must be 0 for all LDs of an MLD. — 若置 1，表示在 Flex Bus.CXL 模式下支持 CXL.cache 协议。MLD 的所有 LD 必须为 0。 |
> | 1 | RO | **IO_Capable**: If set, indicates that the CXL.io protocol is supported when operating in Flex Bus.CXL mode. Must be 1. — 若置 1，表示在 Flex Bus.CXL 模式下支持 CXL.io 协议。必须为 1。 |
> | 2 | RO | **Mem_Capable**: If set, indicates that the CXL.mem protocol is supported when operating in Flex Bus.CXL mode. This must be 1 for all LDs of an MLD. — 若置 1，表示在 Flex Bus.CXL 模式下支持 CXL.mem 协议。MLD 的所有 LD 必须为 1。 |
> | 3 | RO | **Mem_HwInit_Mode**: If set, indicates that this CXL.mem-capable device initializes memory with assistance from hardware and firmware located on the device. If cleared, indicates that memory is initialized by host software such as a device driver. This bit must be ignored when Mem_Capable=0.<br/>Functions that implements the Class Code specified in Section 8.1.12.1 shall set this bit to 1. — 若置 1，表示此支持 CXL.mem 的设备借助设备上的硬件和固件初始化内存。若清零，表示由主机软件（例如设备驱动程序）初始化内存。当 Mem_Capable=0 时必须忽略此位。<br/>实现 8.1.12.1 节中规定的 Class Code 的功能应将此位置 1。 |
> | 5:4 | RO | **HDM_Count**: Number of HDM ranges implemented by the CXL device and reported through this function. This field must return 00b if Mem_Capable=0.<br/>• 00b = Zero ranges. This setting is illegal when Mem_Capable=1.<br/>• 01b = One HDM range.<br/>• 10b = Two HDM ranges.<br/>• 11b = Reserved. — CXL 设备实现并通过此功能上报的 HDM 范围数量。当 Mem_Capable=0 时该字段必须返回 00b。<br/>• 00b = 0 个范围。当 Mem_Capable=1 时此设置非法。<br/>• 01b = 1 个 HDM 范围。<br/>• 10b = 2 个 HDM 范围。<br/>• 11b = 保留。 |
> | 6 | RO | **Cache Writeback and Invalidate Capable**: If set, indicates that the device implements the Disable Caching and Initiate Cache Write Back and Invalidation control bits in the DVSEC CXL Control2 register, and the Cache Invalid status bit in the DVSEC CXL Status2 register. All devices that are not RCDs shall set this capability bit when Cache_Capable=1.¹ — 若置 1，表示设备实现 DVSEC CXL Control2 寄存器中的 Disable Caching 和 Initiate Cache Write Back and Invalidation 控制位，以及 DVSEC CXL Status2 寄存器中的 Cache Invalid 状态位。当 Cache_Capable=1 时，所有非 RCD 设备应设置此能力位。¹ |
> | 7 | RO | **CXL Reset Capable**: If set, indicates that the device supports CXL Reset and implements the CXL Reset Timeout field in this register, the Initiate CXL Reset bit in the DVSEC CXL Control2 register, and the DVSEC CXL Reset Complete status bit in the DVSEC CXL Status2 register.¹<br/>This bit must report the same value for all LDs of an MLD. — 若置 1，表示设备支持 CXL Reset 并实现此寄存器中的 CXL Reset Timeout 字段、DVSEC CXL Control2 寄存器中的 Initiate CXL Reset 位、以及 DVSEC CXL Status2 寄存器中的 DVSEC CXL Reset Complete 状态位。¹<br/>此位对 MLD 的所有 LD 必须报告相同的值。 |
> | 10:8 | RO | **CXL Reset Timeout**: If the CXL Reset Capable bit in this register is set, this field indicates the maximum time that the device may take to complete the CXL Reset. If the CXL Reset Mem Clr Capable bit in this register is 1, this time also accounts for the time that is needed for clearing or randomizing of volatile HDM Ranges. If the CXL Reset Complete status bit in the DVSEC CXL Status2 register is not set after the passage of this time duration, software may assume that CXL Reset has failed. This value must be the same for all LDs of an MLD.¹<br/>• 000b = 10 ms<br/>• 001b = 100 ms<br/>• 010b = 1 second<br/>• 011b = 10 second<br/>• 100b = 100 second<br/>• All other encodings are reserved — 若此寄存器中的 CXL Reset Capable 位置 1，则此字段表示设备完成 CXL Reset 可能所需的最长时间。如果此寄存器中的 CXL Reset Mem Clr Capable 位为 1，则此时间还包括清除或随机化易失性 HDM 范围所需的时间。如果在该时间过后 DVSEC CXL Status2 寄存器中的 CXL Reset Complete 状态位仍未置位，软件可假定 CXL Reset 已失败。MLD 的所有 LD 该值必须相同。¹<br/>• 000b = 10 ms<br/>• 001b = 100 ms<br/>• 010b = 1 秒<br/>• 011b = 10 秒<br/>• 100b = 100 秒<br/>• 所有其他编码保留 |
> | 11 | HwInit | **CXL Reset Mem Clr Capable**: When set, the Device is capable of clearing or randomizing volatile HDM Ranges during CXL Reset.¹ — 置 1 时，设备能够在 CXL Reset 期间清除或随机化易失性 HDM 范围。¹ |
> | 12 | HwInit | **TSP Capable**: When set, the Device is capable of supporting TSP and shall support TSP requests (see Section 11.5.5) and MemRdFill (see Table 3-41).² — 置 1 时，设备能够支持 TSP，应支持 TSP 请求 (见 11.5.5 节) 和 MemRdFill (见表 3-41)。² |
> | 13 | HwInit | **Multiple Logical Device**: If set, indicates that the Device is a Logical Device (which could be an FM-owned LD) within an MLD. If cleared, indicates that the Device is an SLD or an RCD.¹ — 置 1 时，表示设备是 MLD 内的逻辑设备 (可能是 FM 拥有的 LD)。清零时，表示设备是 SLD 或 RCD。¹ |
> | 14 | RO | **Viral_Capable**: If set, indicates that the CXL device supports Viral handling. This value must be 1 for all devices. — 置 1 时，表示 CXL 设备支持 Viral 处理。所有设备该值必须为 1。 |
> | 15 | HwInit | **PM Init Completion Reporting Capable**: If set, indicates that the CXL device is capable of supporting the Power Management Initialization Complete flag. All devices that are not RCDs shall set this capability bit. RCDs may implement this capability.¹<br/>This capability is not applicable to switches and root ports. Switches and root ports shall hardwire this bit to 0. — 置 1 时，表示 CXL 设备能够支持 Power Management Initialization Complete 标志位。所有非 RCD 设备应设置此能力位。RCD 可以实现此能力。¹<br/>此能力不适用于交换器和根端口。交换器和根端口应将此位硬连线为 0。 |
>
> 1. This bit/field was introduced as part of DVSEC Revision=1.
> 2. This bit/field was introduced as part of DVSEC Revision=3.
>
> 1. 此位/字段在 DVSEC Revision=1 中引入。
> 2. 此位/字段在 DVSEC Revision=3 中引入。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-2"></a>
### 8.1.3.2 DVSEC CXL Control (Offset 0Ch) | DVSEC CXL 控制 (偏移 0Ch)

> **Table 8-6.** DVSEC CXL Control (Offset 0Ch) ｜ DVSEC CXL 控制 (偏移 0Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RWL | **Cache_Enable**: When set to 1, enables CXL.cache protocol operation when in Flex Bus.CXL mode. Locked by the CONFIG_LOCK bit¹. If this bit is 0, the component is permitted to silently drop all CXL.cache transactions.<br/>Default value of this bit is 0. — 置 1 时，使能 Flex Bus.CXL 模式下的 CXL.cache 协议操作。由 CONFIG_LOCK 位¹锁定。若此位为 0，则允许组件静默丢弃所有 CXL.cache 事务。<br/>默认值为 0。 |
> | 1 | RO | **IO_Enable**: When set to 1, enables CXL.io protocol operation when in Flex Bus.CXL mode.<br/>This bit always returns 1. — 置 1 时，使能 Flex Bus.CXL 模式下的 CXL.io 协议操作。<br/>此位始终返回 1。 |
> | 2 | RWL | **Mem_Enable**: When set to 1, enables CXL.mem protocol operation when in Flex Bus.CXL mode. Locked by the CONFIG_LOCK bit¹. If this bit is 0, the component is permitted to silently drop all CXL.mem transactions.<br/>Default value of this bit is 0. — 置 1 时，使能 Flex Bus.CXL 模式下的 CXL.mem 协议操作。由 CONFIG_LOCK 位¹锁定。若此位为 0，则允许组件静默丢弃所有 CXL.mem 事务。<br/>默认值为 0。 |
> | 7:3 | RWL | **Cache_SF_Coverage**: Performance hint to the device. Locked by the CONFIG_LOCK bit¹.<br/>• 00h = Indicates no Snoop Filter coverage on the host<br/>• For all other values of N = Indicates Snoop Filter coverage on the host of 2^(N+15d) bytes (e.g., value of 5h indicates 1-MB snoop filter coverage)<br/>Default value of this field is 00h. — 设备的性能提示。由 CONFIG_LOCK 位¹锁定。<br/>• 00h = 主机上没有 Snoop Filter 覆盖<br/>• 对于 N 的所有其他值 = 主机上的 Snoop Filter 覆盖为 2^(N+15d) 字节 (例如，5h 值表示 1-MB snoop filter 覆盖)<br/>默认值为 00h。 |
> | 10:8 | RWL | **Cache_SF_Granularity**: Performance hint to the device. Locked by the CONFIG_LOCK bit¹.<br/>• 000b = Indicates 64B granular tracking on the host<br/>• 001b = Indicates 128B granular tracking on the host<br/>• 010b = Indicates 256B granular tracking on the host<br/>• 011b = Indicates 512B granular tracking on the host<br/>• 100b = Indicates 1KB granular tracking on the host<br/>• 101b = Indicates 2KB granular tracking on the host<br/>• 110b = Indicates 4KB granular tracking on the host<br/>• 111b = Reserved<br/>Default value of this field is 000b. — 设备的性能提示。由 CONFIG_LOCK 位¹锁定。<br/>• 000b = 主机上 64B 粒度跟踪<br/>• 001b = 主机上 128B 粒度跟踪<br/>• 010b = 主机上 256B 粒度跟踪<br/>• 011b = 主机上 512B 粒度跟踪<br/>• 100b = 主机上 1KB 粒度跟踪<br/>• 101b = 主机上 2KB 粒度跟踪<br/>• 110b = 主机上 4KB 粒度跟踪<br/>• 111b = 保留<br/>默认值为 000b。 |
> | 11 | RWL | **Cache_Clean_Eviction**: Performance hint to the device. Locked by the CONFIG_LOCK bit¹.<br/>• 0 = Indicates clean evictions from device caches are needed for best performance<br/>• 1 = Indicates clean evictions from device caches are NOT needed for best performance<br/>Default value of this bit is 0. — 设备的性能提示。由 CONFIG_LOCK 位¹锁定。<br/>• 0 = 表示需要从设备缓存进行 clean eviction 以获得最佳性能<br/>• 1 = 表示不需要从设备缓存进行 clean eviction 即可获得最佳性能<br/>默认值为 0。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-3"></a>
### 8.1.3.3 DVSEC CXL Status (Offset 0Eh) | DVSEC CXL 状态 (偏移 0Eh)

> **Table 8-7.** DVSEC CXL Status (Offset 0Eh) ｜ DVSEC CXL 状态 (偏移 0Eh)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 13:0 | RsvdZ | Reserved — 保留 |
> | 14 | RW1CS | **Viral_Status**: When set, indicates that the CXL device has encountered a Viral condition. This bit does not indicate that the device is currently in Viral condition. See Section 12.4 for more details. — 置 1 时，表示 CXL 设备已遇到 Viral 状况。此位并不表示设备当前处于 Viral 状态。详见 12.4 节。 |
> | 15 | RsvdZ | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-4"></a>
### 8.1.3.4 DVSEC CXL Control2 (Offset 10h) | DVSEC CXL 控制 2 (偏移 10h)

> **Table 8-8.** DVSEC CXL Control2 (Offset 10h) ｜ DVSEC CXL 控制 2 (偏移 10h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RW | **Disable Caching**: When set to 1, device shall no longer cache new modified lines in its local cache. Device shall continue to correctly respond to CXL.cache transactions.¹<br/>Default value of this bit is 0. — 置 1 时，设备应不再将其本地缓存中的新修改行进行缓存。设备应继续正确响应 CXL.cache 事务。¹<br/>默认值为 0。 |
> | 1 | RW | **Initiate Cache Write Back and Invalidation**: When set to 1, the device shall write back all modified lines in the local cache and then invalidate all lines. The device shall send a CacheFlushed message to the host, as required by CXL.cache protocol, to indicate that the device does not hold any modified lines.¹<br/>If this bit is set when Disable Caching=0, the device behavior is undefined.<br/>This bit always returns the value of 0 when read by the software. A write of 0 is ignored. — 置 1 时，设备应将本地缓存中的所有修改行回写，然后使所有行失效。设备应按照 CXL.cache 协议要求向主机发送 CacheFlushed 消息，以表明设备不再持有任何修改行。¹<br/>如果在 Disable Caching=0 时设置此位，则设备行为未定义。<br/>软件读取时，此位始终返回 0。写入 0 被忽略。 |
> | 2 | RW | **Initiate CXL Reset**: When set to 1, the device shall initiate CXL Reset as defined in Section 9.7. This bit always returns the value of 0 when read by the software. A write of 0 is ignored.¹<br/>If Software sets this bit while the previous CXL Reset is in progress, the results are undefined. — 置 1 时，设备应按照 9.7 节定义启动 CXL Reset。软件读取时，此位始终返回 0。写入 0 被忽略。¹<br/>如果软件在上一次 CXL Reset 尚未完成时设置此位，则结果未定义。 |
> | 3 | RW | **CXL Reset Mem Clr Enable**: When set, and the CXL Reset Mem Clr Capable bit in the DVSEC CXL Capability register returns 1, the device shall clear or randomize volatile HDM ranges as part of the CXL Reset operation. When the CXL Reset Mem Clr Capable bit is cleared, this bit is ignored and volatile HDM ranges may or may not be cleared or randomized during CXL Reset.¹<br/>Default value of this bit is 0. — 置 1 时，如果 DVSEC CXL Capability 寄存器中的 CXL Reset Mem Clr Capable 位返回 1，则设备应作为 CXL Reset 操作的一部分清除或随机化易失性 HDM 范围。当 CXL Reset Mem Clr Capable 位清零时，此位被忽略，CXL Reset 期间易失性 HDM 范围可能清除也可能不清除 (或不随机化)。¹<br/>默认值为 0。 |
> | 12 | RWL/RsvdP | **Direct P2P Mem Enable**: This bit must be RWL if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register is set; otherwise, this bit is permitted to be hardwired to 0. Software must not set this bit unless the Direct P2P Mem Capable bit is set.²<br/>When set, enables Direct P2P CXL.mem protocol operation. If this bit is 0, the component is not permitted to initiate Direct P2P CXL.mem transactions.<br/>Default value of this bit is 0. Locked by the CONFIG_LOCK bit¹. — 如果 DVSEC CXL Capability³ 寄存器中的 Direct P2P Mem Capable 位置 1，则此位必须为 RWL；否则，此位可硬连线为 0。除非 Direct P2P Mem Capable 位置位，否则软件不得设置此位。²<br/>置 1 时，使能 Direct P2P CXL.mem 协议操作。若此位为 0，则不允许组件发起 Direct P2P CXL.mem 事务。<br/>默认值为 0。由 CONFIG_LOCK 位¹锁定。 |
> | 13 | RsvdP | Reserved — 保留 |
> | 14 | RWL | **Viral_Enable**: When set, enables Viral handling in the CXL device. Locked by the CONFIG_LOCK bit¹.<br/>If 0, the CXL device may ignore the viral that it receives.<br/>Default value of this bit is 0. — 置 1 时，在 CXL 设备中使能 Viral 处理。由 CONFIG_LOCK 位¹锁定。<br/>若为 0，则 CXL 设备可以忽略其接收到的 viral。<br/>默认值为 0。 |
> | 15 | RsvdP | Reserved — 保留 |
>
> 1. CONFIG_LOCK bit in the DVSEC CXL Lock register.
> 2. This bit was introduced as part of DVSEC Revision=3.
>
> 1. DVSEC CXL Lock 寄存器中的 CONFIG_LOCK 位。
> 2. 此位在 DVSEC Revision=3 中引入。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-5"></a>
### 8.1.3.5 DVSEC CXL Status2 (Offset 12h) | DVSEC CXL 状态 2 (偏移 12h)

> **Table 8-9.** DVSEC CXL Status2 (Offset 12h) ｜ DVSEC CXL 状态 2 (偏移 12h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RO | **Cache Invalid**: When set, the device guarantees that it does not hold any valid lines and Disable Caching=1¹. This bit shall read as 0 when Disable Caching=0.² — 置 1 时，设备保证其不持有任何有效行，且 Disable Caching=1¹。当 Disable Caching=0 时，此位读为 0。² |
> | 1 | RO | **CXL Reset Complete**: When set, the device has successfully completed CXL Reset as defined in Section 9.7.²<br/>Device shall clear this bit upon transition of Initiate CXL Reset bit¹ from 0 to 1, prior to initiating the CXL Reset flow. — 置 1 时，设备已按 9.7 节定义成功完成 CXL Reset。²<br/>设备应在 Initiate CXL Reset 位¹ 由 0 跳变到 1 时清除此位 (在启动 CXL Reset 流程之前)。 |
> | 2 | RO | **CXL Reset Error**: When set, the device has completed CXL Reset with errors. Additional information may be available in device error records (see Section 8.2.10.2.1). Host software or Fabric Manager may optionally reissue CXL Reset.²<br/>Device shall clear this bit upon transition of the Initiate CXL Reset bit¹ from 0 to 1, prior to initiating the CXL Reset flow. — 置 1 时，设备完成 CXL Reset 时出错。附加信息可能可在设备错误记录中找到 (见 8.2.10.2.1 节)。主机软件或 Fabric Manager 可以选择重新发起 CXL Reset。²<br/>设备应在 Initiate CXL Reset 位¹ 由 0 跳变到 1 时清除此位 (在启动 CXL Reset 流程之前)。 |
> | 3 | RW1CS/ RsvdZ | **Volatile HDM Preservation Error**: This bit shall be set if the Software requested the device to preserve Volatile HDM content across a Hot Reset but the device failed to do so.³<br/>RW1CS if the Volatile HDM State after Hot Reset - Configurability bit in the DVSEC CXL Capability³ register is set; otherwise, it is RsvdZ. — 如果软件请求设备在热复位期间保留易失性 HDM 内容但设备未保留，则该位应置位。³<br/>如果 DVSEC CXL Capability³ 寄存器中的 Volatile HDM State after Hot Reset - Configurability 位置 1，则为 RW1CS；否则为 RsvdZ。 |
> | 4 | RWS/RO | **Desired Volatile HDM State after Hot Reset**: This bit must be RWS if the Volatile HDM State after Hot Reset - Configurability bit in the DVSEC CXL Capability³ register is set; otherwise, this bit is permitted to be hardwired to 0. Software must not set this bit unless the Volatile HDM State after Hot Reset - Configurability bit is set.²<br/>The reset default is 0.<br/>• 0 = Follow the Default Volatile HDM State after the Hot Reset bit in the DVSEC CXL Capability³ register<br/>• 1 = Device shall preserve the Volatile HDM content across Hot Reset — 如果 DVSEC CXL Capability³ 寄存器中的 Volatile HDM State after Hot Reset - Configurability 位置 1，则此位必须为 RWS；否则，此位可硬连线为 0。除非该 Configurability 位置位，否则软件不得设置此位。²<br/>复位默认值为 0。<br/>• 0 = 遵循 DVSEC CXL Capability³ 寄存器中 Hot Reset 后的 Default Volatile HDM State 位<br/>• 1 = 设备应在热复位期间保留易失性 HDM 内容 |
> | 5 | RW/RO | **Modified Completion Enable**: This bit must be RW if the Modified Completion Capable bit in the DVSEC CXL Capability² register is set; otherwise, this bit is permitted to be hardwired to 0. Software must not set this bit unless the Modified Completion Capable bit is set.³<br/>The reset default is 0.<br/>• 0 = This device is not permitted to return modified data<br/>• 1 = This device is permitted to return modified data using the Cmp-M response — 如果 DVSEC CXL Capability² 寄存器中的 Modified Completion Capable 位置 1，则此位必须为 RW；否则，此位可硬连线为 0。除非 Modified Completion Capable 位置位，否则软件不得设置此位。³<br/>复位默认值为 0。<br/>• 0 = 此设备不允许返回修改数据<br/>• 1 = 此设备允许使用 Cmp-M 响应返回修改数据 |
> | 14:6 | RsvdP | Reserved — 保留 |
> | 15 | RO | **Power Management Initialization Complete**: When set, indicates that the device has successfully completed the Power Management Initialization flow described in Figure 3-4 and is ready to process various Power Management messages.²<br/>If this bit is not set within 100 ms of link-up, software may conclude that Power Management initialization has failed and may then issue a Secondary Bus Reset to force link re-initialization and Power Management re-initialization. — 置 1 时，表示设备已成功完成图 3-4 中描述的电源管理初始化流程，并准备好处理各种电源管理消息。²<br/>如果在 link-up 后的 100 ms 内该位仍未置位，软件可判定电源管理初始化失败，并可发出 Secondary Bus Reset 以强制链路重新初始化和电源管理重新初始化。 |
>
> 1. This bit was introduced as part of DVSEC Revision=1.
> 2. This bit was introduced as part of DVSEC Revision=2.
> 3. This bit was introduced as part of DVSEC Revision=3.
>
> 1. 此位在 DVSEC Revision=1 中引入。
> 2. 此位在 DVSEC Revision=2 中引入。
> 3. 此位在 DVSEC Revision=3 中引入。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-6"></a>
### 8.1.3.6 DVSEC CXL Lock (Offset 14h) | DVSEC CXL 锁 (偏移 14h)

> **Table 8-10.** DVSEC CXL Lock (Offset 14h) ｜ DVSEC CXL 锁 (偏移 14h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RWO | **CONFIG_LOCK**: When set, all register fields in the PCIe DVSEC for CXL Devices Capability with the RWL attribute become read only. Consult individual register fields for details.<br/>This bit is cleared upon device Conventional Reset. This bit and all the fields that are locked by this bit are unaffected by CXL Reset.<br/>Default value of this bit is 0. — 置 1 时，PCIe DVSEC for CXL Devices Capability 中具有 RWL 属性的所有寄存器字段变为只读。详情请查阅各寄存器字段。<br/>此位在设备 Conventional Reset 时清零。此位以及由此位锁定的所有字段不受 CXL Reset 影响。<br/>默认值为 0。 |
> | 15:1 | RsvdP | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-7"></a>
### 8.1.3.7 DVSEC CXL Capability2 (Offset 16h) | DVSEC CXL 能力 2 (偏移 16h)

> **Table 8-11.** DVSEC CXL Capability2 (Offset 16h) ｜ DVSEC CXL 能力 2 (偏移 16h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RO | **Cache Size Unit**: A CXL device that is not CXL.cache-capable shall return the value of 0h.¹<br/>• 0h = Cache size is not reported<br/>• 1h = 64 KB<br/>• 2h = 1 MB<br/>• All other encodings are reserved — 不支持 CXL.cache 的 CXL 设备应返回值 0h。¹<br/>• 0h = 未报告缓存大小<br/>• 1h = 64 KB<br/>• 2h = 1 MB<br/>• 所有其他编码保留 |
> | 5:4 | HwInit | **Fallback Capability**: Defines the fallback operation mode of a Type 2 Device. Fallback operation mode is where the device does not appear as a Type 2 CXL device, yet provides useful functionality. This field is not intended for advertising debug modes of operation.²<br/>• 00b = Device either does not support fallback mode or does not advertise fallback mode<br/>• 01b = PCIe<br/>• 10b = CXL Type 1<br/>• 11b = CXL Type 3 — 定义 Type 2 设备的回退操作模式。回退操作模式是指设备不作为 Type 2 CXL 设备出现，但仍提供有用的功能。此字段不用于公布调试操作模式。²<br/>• 00b = 设备不支持回退模式或不公布回退模式<br/>• 01b = PCIe<br/>• 10b = CXL Type 1<br/>• 11b = CXL Type 3 |
> | 6 | HwInit | **Modified Completion Capable**: When set to 1, it indicates that this device is capable of returning modified data using the Cmp-M response.³ — 置 1 时，表示此设备能够使用 Cmp-M 响应返回修改数据。³ |
> | 7 | HwInit | **No Clean Writeback**: Specifies that a device shall not issue clean writebacks. This bit shall be set to 1 if the device does not support CXL.cache and does not support Direct P2P CXL.mem as a requester. For DVSEC Revisions = 1h or 2h, software can consider the device 'No Clean Writeback' capable if Cache_Capable is not set.³<br/>• 0 = Device may or may not generate clean writebacks<br/>• 1 = Device guarantees to never generate clean writebacks at the device's cacheline granularity — 指定设备不应发起 clean writeback。如果设备不支持 CXL.cache 并且作为请求者不支持 Direct P2P CXL.mem，则此位应设置为 1。对于 DVSEC Revisions = 1h 或 2h，如果 Cache_Capable 未设置，软件可认为设备具备 "No Clean Writeback" 能力。³<br/>• 0 = 设备可能生成也可能不生成 clean writeback<br/>• 1 = 设备保证在其 cacheline 粒度上永远不会生成 clean writeback |
> | 15:8 | RO | **Cache Size**: Expressed in multiples of Cache Size Unit. If Cache Size=4 and Cache Size Unit=1h, the device has a 256-KB cache.¹<br/>A CXL device that is not CXL.cache-capable shall return the value of 00h. — 以 Cache Size Unit 的倍数表示。如果 Cache Size=4 且 Cache Size Unit=1h，则设备具有 256-KB 缓存。¹<br/>不支持 CXL.cache 的 CXL 设备应返回值 00h。 |
>
> 1. This field was introduced as part of DVSEC Revision=1.
> 2. This field was introduced as part of DVSEC Revision=2.
> 3. This bit was introduced as part of DVSEC Revision=3.
>
> 1. 此字段在 DVSEC Revision=1 中引入。
> 2. 此字段在 DVSEC Revision=2 中引入。
> 3. 此位在 DVSEC Revision=3 中引入。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8"></a>
### 8.1.3.8 DVSEC CXL Range Registers | DVSEC CXL 范围寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>These registers are not applicable to an FM-owned LD.</td><td style="background-color:#e8e8e8">这些寄存器不适用于 FM 拥有的 LD。</td></tr>
<tr><td>The DVSEC CXL Range 1 register set must be implemented if Mem_Capable=1 in the DVSEC CXL Capability register. The DVSEC CXL Range 2 register set must be implemented if (Mem_Capable=1 and HDM_Count=10b in the DVSEC CXL Capability register). Each set contains 4 registers - Size High, Size Low, Base High, and Base Low.</td><td style="background-color:#e8e8e8">如果 DVSEC CXL Capability 寄存器中的 Mem_Capable=1，则必须实现 DVSEC CXL Range 1 寄存器组。如果 Mem_Capable=1 且 DVSEC CXL Capability 寄存器中的 HDM_Count=10b，则必须实现 DVSEC CXL Range 2 寄存器组。每组包含 4 个寄存器：Size High、Size Low、Base High 和 Base Low。</td></tr>
<tr><td>A CXL.mem-capable device is permitted to report zero memory size.</td><td style="background-color:#e8e8e8">支持 CXL.mem 的设备允许上报零内存大小。</td></tr>
</tbody>
</table>

<a id="sec-8-1-3-8-1"></a>
#### 8.1.3.8.1 DVSEC CXL Range 1 Size High (Offset 18h) | DVSEC CXL 范围 1 大小高 (偏移 18h)

> **Table 8-12.** DVSEC CXL Range 1 Size High (Offset 18h) ｜ DVSEC CXL 范围 1 大小高 (偏移 18h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RO | **Memory_Size_High**: Corresponds to bits 63:32 of the CXL Range 1 memory size regardless of whether the device implements CXL HDM Decoder Capability registers. — 对应 CXL 范围 1 内存大小的 bit 63:32，无论设备是否实现 CXL HDM Decoder Capability 寄存器。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-2"></a>
#### 8.1.3.8.2 DVSEC CXL Range 1 Size Low (Offset 1Ch) | DVSEC CXL 范围 1 大小低 (偏移 1Ch)

> **Table 8-13.** DVSEC CXL Range 1 Size Low (Offset 1Ch) ｜ DVSEC CXL 范围 1 大小低 (偏移 1Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RO | **Memory_Info_Valid**: When set, indicates that the CXL Range 1 Size High and Size Low registers are valid regardless of whether the device implements CXL HDM Decoder Capability registers. Must be set within 1 second of reset deassertion to the CXL device. — 置 1 时，表示 CXL 范围 1 Size High 和 Size Low 寄存器有效，无论设备是否实现 CXL HDM Decoder Capability 寄存器。必须在 CXL 设备复位取消置位后 1 秒内设置。 |
> | 1 | RO | **Memory_Active**: When set, indicates that the CXL Range 1 memory is fully initialized and available for software use regardless of whether the device implements CXL HDM Decoder Capability registers. When cleared, indicates that the CXL Range 1 memory may be unavailable for software use regardless of whether the device implements CXL HDM Decoder Capability registers. Must be set within Range 1 Memory_Active_Timeout of reset deassertion to the CXL device when Mem_HwInit_Mode=1 in the DVSEC CXL Capability register. — 置 1 时，表示 CXL 范围 1 内存已完全初始化并可供软件使用，无论设备是否实现 CXL HDM Decoder Capability 寄存器。清零时，表示 CXL 范围 1 内存可能不可供软件使用。当 DVSEC CXL Capability 寄存器中的 Mem_HwInit_Mode=1 时，必须在 CXL 设备复位取消置位后 Range 1 Memory_Active_Timeout 时间内设置。 |
> | 4:2 | RO | **Media_Type**: Indicates the memory media characteristics regardless of whether the device implements CXL HDM Decoder Capability registers. All CXL.mem devices that are not eRCDs shall set this field to 010b.<br/>• 000b = Volatile memory. This setting is deprecated starting with the CXL 2.0 specification.<br/>• 001b = Non-volatile memory. This setting is deprecated starting with the CXL 2.0 specification.<br/>• 010b = Memory characteristics are communicated via CDAT (see Section 8.1.11) and not via this field.¹<br/>• All other encodings are reserved. — 表示内存介质特性，无论设备是否实现 CXL HDM Decoder Capability 寄存器。所有非 eRCD 的 CXL.mem 设备应将此字段设置为 010b。<br/>• 000b = 易失性内存。此设置从 CXL 2.0 规范起被弃用。<br/>• 001b = 非易失性内存。此设置从 CXL 2.0 规范起被弃用。<br/>• 010b = 内存特性通过 CDAT 通信 (见 8.1.11 节)，不通过此字段。¹<br/>• 所有其他编码保留。 |
> | 7:5 | RO | **Memory_Class**: Indicates the class of memory regardless of whether the device implements CXL HDM Decoder Capability registers. All CXL.mem devices that are not eRCDs shall set this field to 010b.<br/>• 000b = Memory Class (e.g., normal DRAM). This setting is deprecated starting with the CXL 2.0 specification.<br/>• 001b = Storage Class. This setting is deprecated starting with the CXL 2.0 specification.<br/>• 010b = Memory characteristics are communicated via CDAT (see Section 8.1.11) and not via this field.¹<br/>• All other encodings are reserved. — 表示内存的类别，无论设备是否实现 CXL HDM Decoder Capability 寄存器。所有非 eRCD 的 CXL.mem 设备应将此字段设置为 010b。<br/>• 000b = Memory Class (例如普通 DRAM)。此设置从 CXL 2.0 规范起被弃用。<br/>• 001b = Storage Class。此设置从 CXL 2.0 规范起被弃用。<br/>• 010b = 内存特性通过 CDAT 通信 (见 8.1.11 节)，不通过此字段。¹<br/>• 所有其他编码保留。 |
> | 12:8 | RO | **Desired_Interleave**: If a CXL.mem-capable eRCD is connected to a single CPU via multiple CXL links, this field represents the memory interleaving desired by the device. BIOS will configure the CPU to interleave accesses to this HDM range across links at this granularity or to the closest possible value that the host supports.<br/>In all other cases, this field represents the minimum desired interleave granularity for optimal device performance regardless of whether the device implements CXL HDM Decoder Capability registers. Software should program the Interleave Granularity (IG) field in the HDM Decoder Control registers (see Section 8.2.4.20.7) to be an exact match or any larger granularity than the device advertises via the CXL HDM Decoder Capability register (see Section 8.2.4.20.1). This field is treated as a hint. The device shall function correctly if the actual value that is programmed in the Interleave Granularity (IG) field in the HDM Decoder Control registers is less than what is reported via this field.<br/>• 00h = No Interleave<br/>• 01h = 256-Byte Granularity<br/>• 02h = 4-KB Interleave<br/>• 03h = 512 Bytes¹<br/>• 04h = 1024 Bytes¹<br/>• 05h = 2048 Bytes¹<br/>• 06h = 8192 Bytes¹<br/>• 07h = 16384 Bytes¹<br/>• All other encodings are reserved<br/>Note: If a CXL device has different desired interleave values for DPA ranges that are covered by this CXL Range 1, the device should report a value that best fits the requirements for all such ranges (e.g., the maximum of the values).<br/>Note: If CXL devices in an Interleave Set advertise different values for this field, Software may choose the smallest value that best fits the set. — 如果支持 CXL.mem 的 eRCD 通过多条 CXL 链路连接到单个 CPU，则此字段表示设备期望的内存交织。BIOS 将配置 CPU 以此粒度或最接近的可用值跨链路交织此 HDM 范围的访问。<br/>在所有其他情况下，此字段表示设备最佳性能所需的最小交织粒度，无论设备是否实现 CXL HDM Decoder Capability 寄存器。软件应将 HDM Decoder Control 寄存器 (见 8.2.4.20.7 节) 中的 Interleave Granularity (IG) 字段编程为完全匹配或任何比设备通过 CXL HDM Decoder Capability 寄存器 (见 8.2.4.20.1 节) 公布的粒度更大的值。此字段视为提示。如果 HDM Decoder Control 寄存器中编程的实际 IG 值小于此字段报告的值，设备应能正确运行。<br/>• 00h = 无交织<br/>• 01h = 256 字节粒度<br/>• 02h = 4-KB 交织<br/>• 03h = 512 字节¹<br/>• 04h = 1024 字节¹<br/>• 05h = 2048 字节¹<br/>• 06h = 8192 字节¹<br/>• 07h = 16384 字节¹<br/>• 所有其他编码保留<br/>注意：如果 CXL 设备对由此 CXL Range 1 覆盖的 DPA 范围具有不同的期望交织值，则设备应报告最适合所有此类范围要求的值 (例如最大值)。<br/>注意：如果 Interleave Set 中的 CXL 设备为此字段公布不同的值，软件可以选择最适合该集合的最小值。 |
> | 15:13 | HwInit | **Memory_Active_Timeout**: For devices that advertise Mem_HwInit_Mode=1 in the DVSEC CXL Capability register, this field indicates the maximum time that the device is permitted to take to set the Memory_Active bit in this register after a hot reset, a warm reset, or a cold reset regardless of whether the device implements CXL HDM Decoder Capability registers. If the Memory_Active bit is not set after the passage of this time duration, software may assume that the HDM reported by this range has failed. This value must be the same for all LDs of an MLD.¹<br/>• 000b = 1 second<br/>• 001b = 4 seconds<br/>• 010b = 16 seconds<br/>• 011b = 64 seconds<br/>• 100b = 256 seconds<br/>• All other encodings are reserved — 对于在 DVSEC CXL Capability 寄存器中公布 Mem_HwInit_Mode=1 的设备，此字段表示设备在热复位、温复位或冷复位后允许在此寄存器中设置 Memory_Active 位的最长时间，无论设备是否实现 CXL HDM Decoder Capability 寄存器。如果在该时间过后 Memory_Active 位仍未置位，软件可假定此范围所报告的 HDM 失败。MLD 的所有 LD 此值必须相同。¹<br/>• 000b = 1 秒<br/>• 001b = 4 秒<br/>• 010b = 16 秒<br/>• 011b = 64 秒<br/>• 100b = 256 秒<br/>• 所有其他编码保留 |
> | 16 | RO | **Memory_Active_Degraded**: When set, indicates that the CXL Range 1 memory is initialized and available for software use regardless of whether the device implements CXL HDM Decoder Capability registers. When set, it also signifies a reduction in capacity or performance relative to what is expected.²<br/>If this bit is 1, the Memory_Active flag in this register shall be 0. If the Memory_Active flag in this register is 1, this bit shall be 0.<br/>Either Memory_Active or Memory_Active_Degraded shall be set within Range_1 Memory_Active_Timeout of reset deassertion to the CXL device when Mem_HwInit_Mode=1 in the DVSEC CXL Capability register. — 置 1 时，表示 CXL 范围 1 内存已初始化并可供软件使用，无论设备是否实现 CXL HDM Decoder Capability 寄存器。置 1 时还表示相对于预期容量或性能有所下降。²<br/>如果此位为 1，则此寄存器中的 Memory_Active 标志必须为 0。如果此寄存器中的 Memory_Active 标志为 1，则此位必须为 0。<br/>当 DVSEC CXL Capability 寄存器中的 Mem_HwInit_Mode=1 时，Memory_Active 或 Memory_Active_Degraded 应在 CXL 设备复位取消置位后 Range_1 Memory_Active_Timeout 时间内设置。 |
> | 27:17 | RsvdP | Reserved — 保留 |
> | 31:28 | RO | **Memory_Size_Low**: Corresponds to bits 31:28 of the CXL Range 1 memory size regardless of whether the device implements CXL HDM Decoder Capability registers. — 对应 CXL 范围 1 内存大小的 bit 31:28，无论设备是否实现 CXL HDM Decoder Capability 寄存器。 |
>
> 1. Introduced as part of DVSEC Revision=1.
> 2. This bit was introduced as part of DVSEC Revision=3.

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-3"></a>
#### 8.1.3.8.3 DVSEC CXL Range 1 Base High (Offset 20h) | DVSEC CXL 范围 1 基址高 (偏移 20h)

> **Table 8-14.** DVSEC CXL Range 1 Base High (Offset 20h) ｜ DVSEC CXL 范围 1 基址高 (偏移 20h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RWL | **Memory_Base_High**: Corresponds to bits 63:32 of CXL Range 1 base in the host address space. Locked by the CONFIG_LOCK bit in the DVSEC CXL Lock register.<br/>If a device implements CXL HDM Decoder Capability registers and software has enabled the HDM Decoder by setting the HDM Decoder Enable bit in the CXL HDM Decoder Global Control register, the value of this register is not used during address decode. It is recommended that software program this to match CXL HDM Decoder 0 Base High register for backward compatibility.<br/>Default value of this register is 0h. — 对应主机地址空间中 CXL 范围 1 基址的 bit 63:32。由 DVSEC CXL Lock 寄存器中的 CONFIG_LOCK 位锁定。<br/>如果设备实现 CXL HDM Decoder Capability 寄存器并且软件通过设置 CXL HDM Decoder Global Control 寄存器中的 HDM Decoder Enable 位使能了 HDM Decoder，则此寄存器的值不参与地址解码。建议软件将其编程为与 CXL HDM Decoder 0 Base High 寄存器匹配以保持向后兼容。<br/>默认值为 0h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-4"></a>
#### 8.1.3.8.4 DVSEC CXL Range 1 Base Low (Offset 24h) | DVSEC CXL 范围 1 基址低 (偏移 24h)

> **Table 8-15.** DVSEC CXL Range 1 Base Low (Offset 24h) ｜ DVSEC CXL 范围 1 基址低 (偏移 24h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 27:0 | RsvdP | Reserved — 保留 |
> | 31:28 | RWL | **Memory_Base_Low**: Corresponds to bits 31:28 of the CXL Range 1 base in the host address space. Locked by the CONFIG_LOCK bit in the DVSEC CXL Lock register.<br/>If a device implements CXL HDM Decoder Capability registers and software has enabled the HDM Decoder by setting the HDM Decoder Enable bit in the CXL HDM Decoder Global Control register, the value of this field is not used during address decode. It is recommended that software program this to match CXL HDM Decoder 0 Base Low register for backward compatibility.<br/>Default value of this field is 0h. — 对应主机地址空间中 CXL 范围 1 基址的 bit 31:28。由 DVSEC CXL Lock 寄存器中的 CONFIG_LOCK 位锁定。<br/>如果设备实现 CXL HDM Decoder Capability 寄存器并且软件通过设置 CXL HDM Decoder Global Control 寄存器中的 HDM Decoder Enable 位使能了 HDM Decoder，则此字段的值不参与地址解码。建议软件将其编程为与 CXL HDM Decoder 0 Base Low 寄存器匹配以保持向后兼容。<br/>默认值为 0h。 |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>A CXL.mem-capable device that does not implement CXL HDM Decoder Capability registers directs host accesses to an Address A within its local HDM if the following two equations are satisfied:</td><td style="background-color:#e8e8e8">不支持 CXL HDM Decoder Capability 寄存器的支持 CXL.mem 的设备，如果满足以下两个等式，则将主机访问定向到其本地 HDM 内的地址 A：</td></tr>
</tbody>
</table>

> **Equation 8-1.** Memory_Base[63:28] <= (A >> 28) < Memory_Base[63:28] + Memory_Size[63:28] ｜ 内存基址 [63:28] <= (A >> 28) < 内存基址 [63:28] + 内存大小 [63:28]

> **Equation 8-2.** Memory_Active AND DVSEC CXL Mem_Enable=1 ｜ 内存激活 与 DVSEC CXL Mem_Enable=1

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>where >> represents a bitwise right-shift operation.</td><td style="background-color:#e8e8e8">其中 >> 表示按位右移操作。</td></tr>
<tr><td>A CXL.mem-capable device that implements CXL HDM Decoder Capability registers follows the above behavior as long as the HDM Decoder Enable bit in the CXL HDM Decoder Global Control register (see Section 8.2.4.20.2) is 0.</td><td style="background-color:#e8e8e8">实现 CXL HDM Decoder Capability 寄存器的支持 CXL.mem 的设备，只要 CXL HDM Decoder Global Control 寄存器 (见 8.2.4.20.2 节) 中的 HDM Decoder Enable 位为 0，就遵循上述行为。</td></tr>
<tr><td><strong>Note:</strong> Software is required to set HDM Decoder Enable bit in the CXL HDM Decoder Global Control register to enable the device to generate a BISnp request or allow UIO access to its HDM. Under these scenarios, the DVSEC CXL Range 1 Base Low register, DVSEC CXL Range 1 Base High register, DVSEC CXL Range 2 Base Low register, and DVSEC CXL Range 2 Base High register do not participate in CXL.mem address decode.</td><td style="background-color:#e8e8e8"><strong>注意：</strong>软件需要设置 CXL HDM Decoder Global Control 寄存器中的 HDM Decoder Enable 位，以使设备能够生成 BISnp 请求或允许 UIO 访问其 HDM。在这些情况下，DVSEC CXL Range 1 Base Low 寄存器、DVSEC CXL Range 1 Base High 寄存器、DVSEC CXL Range 2 Base Low 寄存器和 DVSEC CXL Range 2 Base High 寄存器不参与 CXL.mem 地址解码。</td></tr>
<tr><td>If Address A is not backed by real memory (e.g., a device with less than 256 MB of memory), a device that does not implement CXL HDM Decoder Capability registers must gracefully handle those accesses (i.e., return all 1s on reads and drop writes).</td><td style="background-color:#e8e8e8">如果地址 A 不由实际内存支持 (例如，设备的内存小于 256 MB)，则未实现 CXL HDM Decoder Capability 寄存器的设备必须优雅地处理这些访问 (即读时返回全 1，写时丢弃)。</td></tr>
<tr><td>Aliasing (mapping more than one Host Physical Address (HPA) to a single Device Physical Address) is forbidden.</td><td style="background-color:#e8e8e8">禁止别名 (aliasing) (即将多个主机物理地址 (HPA) 映射到单个设备物理地址)。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-5"></a>
#### 8.1.3.8.5 DVSEC CXL Range 2 Size High (Offset 28h) | DVSEC CXL 范围 2 大小高 (偏移 28h)

> **Table 8-16.** DVSEC CXL Range 2 Size High (Offset 28h) ｜ DVSEC CXL 范围 2 大小高 (偏移 28h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RO | **Memory_Size_High**: Corresponds to bits 63:32 of the CXL Range 2 memory size regardless of whether the device implements CXL HDM Decoder Capability registers. — 对应 CXL 范围 2 内存大小的 bit 63:32，无论设备是否实现 CXL HDM Decoder Capability 寄存器。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-6"></a>
#### 8.1.3.8.6 DVSEC CXL Range 2 Size Low (Offset 2Ch) | DVSEC CXL 范围 2 大小低 (偏移 2Ch)

> **Table 8-17.** DVSEC CXL Range 2 Size Low (Offset 2Ch) ｜ DVSEC CXL 范围 2 大小低 (偏移 2Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RO | **Memory_Info_Valid**: When set, indicates that the CXL Range 2 Size High and Size Low registers are valid regardless of whether the device implements CXL HDM Decoder Capability registers. Must be set within 1 second of reset deassertion to the CXL device. — 置 1 时，表示 CXL 范围 2 Size High 和 Size Low 寄存器有效，无论设备是否实现 CXL HDM Decoder Capability 寄存器。必须在 CXL 设备复位取消置位后 1 秒内设置。 |
> | 1 | RO | **Memory_Active**: When set, indicates that the CXL Range 2 memory is fully initialized and available for software use, regardless of whether the device implements CXL HDM Decoder Capability registers. When cleared, indicates that the CXL Range 2 memory may be unavailable for software use regardless of whether the device implements CXL HDM Decoder Capability registers. Must be set within Range 2 Memory_Active_Timeout of reset deassertion to the CXL device when Mem_HwInit_Mode=1 in the DVSEC CXL Capability register. — 置 1 时，表示 CXL 范围 2 内存已完全初始化并可供软件使用，无论设备是否实现 CXL HDM Decoder Capability 寄存器。清零时，表示 CXL 范围 2 内存可能不可供软件使用。当 DVSEC CXL Capability 寄存器中的 Mem_HwInit_Mode=1 时，必须在 CXL 设备复位取消置位后 Range 2 Memory_Active_Timeout 时间内设置。 |
> | 4:2 | RO | **Media_Type**: Indicates the memory media characteristics regardless of whether the device implements CXL HDM Decoder Capability registers. All CXL.mem devices that are not eRCDs shall set this field to 010b.<br/>• 000b = Volatile memory. This setting is deprecated starting with the CXL 2.0 specification.<br/>• 001b = Non-volatile memory. This setting is deprecated starting with the CXL 2.0 specification.<br/>• 010b = Memory characteristics are communicated via CDAT (see Section 8.1.11) and not via this field.¹<br/>• 111b = Not Memory. This setting is deprecated starting with the CXL 2.0 specification.<br/>• All other encodings are reserved. — 表示内存介质特性，无论设备是否实现 CXL HDM Decoder Capability 寄存器。所有非 eRCD 的 CXL.mem 设备应将此字段设置为 010b。<br/>• 000b = 易失性内存。此设置从 CXL 2.0 规范起被弃用。<br/>• 001b = 非易失性内存。此设置从 CXL 2.0 规范起被弃用。<br/>• 010b = 内存特性通过 CDAT 通信 (见 8.1.11 节)，不通过此字段。¹<br/>• 111b = 非内存。此设置从 CXL 2.0 规范起被弃用。<br/>• 所有其他编码保留。 |
> | 7:5 | RO | **Memory_Class**: Indicates the class of memory regardless of whether the device implements CXL HDM Decoder Capability registers. All CXL.mem devices that are not eRCDs shall set this field to 010b.<br/>• 000b = Memory Class (e.g., normal DRAM), This setting is deprecated starting with the CXL 2.0 specification.<br/>• 001b = Storage Class. This setting is deprecated starting with the CXL 2.0 specification.<br/>• 010b = Memory characteristics are communicated via CDAT (see Section 8.1.11) and not via this field.¹<br/>• All other encodings are reserved. — 表示内存的类别，无论设备是否实现 CXL HDM Decoder Capability 寄存器。所有非 eRCD 的 CXL.mem 设备应将此字段设置为 010b。<br/>• 000b = Memory Class (例如普通 DRAM)，此设置从 CXL 2.0 规范起被弃用。<br/>• 001b = Storage Class。此设置从 CXL 2.0 规范起被弃用。<br/>• 010b = 内存特性通过 CDAT 通信 (见 8.1.11 节)，不通过此字段。¹<br/>• 所有其他编码保留。 |
> | 12:8 | RO | **Desired_Interleave**: See the Desired_Interleave field definition in the DVSEC CXL Range 1 Size Low register (see Section 8.1.3.8.2). — 参见 DVSEC CXL 范围 1 大小低寄存器 (见 8.1.3.8.2 节) 中 Desired_Interleave 字段的定义。 |
> | 15:13 | HwInit | **Memory_Active_Timeout**: For devices that advertises Mem_HwInit_Mode=1 in the DVSEC CXL Capability register, this field indicates the maximum time that the device is permitted to take to set the Memory_Active bit in this register after a Conventional Reset regardless of whether the device implements CXL HDM Decoder Capability registers. If the Memory_Active bit is not set after the passage of this time duration, software may assume that the HDM reported by this range has failed. This value must be the same for all LDs of an MLD.¹<br/>• 000b = 1 second<br/>• 001b = 4 seconds<br/>• 010b = 16 seconds<br/>• 011b = 64 seconds<br/>• 100b = 256 seconds<br/>• All other encodings are reserved — 对于在 DVSEC CXL Capability 寄存器中公布 Mem_HwInit_Mode=1 的设备，此字段表示设备在 Conventional Reset 后允许在此寄存器中设置 Memory_Active 位的最长时间，无论设备是否实现 CXL HDM Decoder Capability 寄存器。如果在该时间过后 Memory_Active 位仍未置位，软件可假定此范围所报告的 HDM 失败。MLD 的所有 LD 此值必须相同。¹<br/>• 000b = 1 秒<br/>• 001b = 4 秒<br/>• 010b = 16 秒<br/>• 011b = 64 秒<br/>• 100b = 256 秒<br/>• 所有其他编码保留 |
> | 16 | RO | **Memory_Active_Degraded**: When set, indicates that the CXL Range 2 memory is initialized and available for software use regardless of whether the device implements CXL HDM Decoder Capability registers. When set, it also signifies a reduction in capacity or performance relative to what is expected.²<br/>If this bit is 1, the Memory_Active flag in this register shall be 0. If the Memory_Active flag in this register is 1, this bit shall be 0.<br/>Either Memory_Active or Memory_Active_Degraded shall be set within Range_2 Memory_Active_Timeout of reset deassertion to the CXL device when Mem_HwInit_Mode=1 in the DVSEC CXL Capability register. — 置 1 时，表示 CXL 范围 2 内存已初始化并可供软件使用，无论设备是否实现 CXL HDM Decoder Capability 寄存器。置 1 时还表示相对于预期容量或性能有所下降。²<br/>如果此位为 1，则此寄存器中的 Memory_Active 标志必须为 0。如果此寄存器中的 Memory_Active 标志为 1，则此位必须为 0。<br/>当 DVSEC CXL Capability 寄存器中的 Mem_HwInit_Mode=1 时，Memory_Active 或 Memory_Active_Degraded 应在 CXL 设备复位取消置位后 Range_2 Memory_Active_Timeout 时间内设置。 |
> | 27:17 | RsvdP | Reserved — 保留 |
> | 31:28 | RO | **Memory_Size_Low**: Corresponds to bits 31:28 of the CXL Range 2 memory size regardless of whether the device implements CXL HDM Decoder Capability registers. — 对应 CXL 范围 2 内存大小的 bit 31:28，无论设备是否实现 CXL HDM Decoder Capability 寄存器。 |
>
> 1. Introduced as part of DVSEC Revision=1.
> 2. This bit was introduced as part of DVSEC Revision=3.

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-7"></a>
#### 8.1.3.8.7 DVSEC CXL Range 2 Base High (Offset 30h) | DVSEC CXL 范围 2 基址高 (偏移 30h)

> **Table 8-18.** DVSEC CXL Range 2 Base High (Offset 30h) ｜ DVSEC CXL 范围 2 基址高 (偏移 30h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RWL | **Memory_Base_High**: Corresponds to bits 63:32 of CXL Range 2 base in the host address space. Locked by the CONFIG_LOCK bit in the DVSEC CXL Lock register.<br/>If a device implements CXL HDM Decoder Capability registers and software has enabled the HDM Decoder by setting the HDM Decoder Enable bit in the CXL HDM Decoder Global Control register, the value of this register is not used during address decode. It is recommended that software program this to match the corresponding CXL HDM Decoder Base High register for backward compatibility.<br/>Default value of this register is 0000 0000h. — 对应主机地址空间中 CXL 范围 2 基址的 bit 63:32。由 DVSEC CXL Lock 寄存器中的 CONFIG_LOCK 位锁定。<br/>如果设备实现 CXL HDM Decoder Capability 寄存器并且软件通过设置 CXL HDM Decoder Global Control 寄存器中的 HDM Decoder Enable 位使能了 HDM Decoder，则此寄存器的值不参与地址解码。建议软件将其编程为与相应的 CXL HDM Decoder Base High 寄存器匹配以保持向后兼容。<br/>默认值为 0000 0000h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-8-8"></a>
#### 8.1.3.8.8 DVSEC CXL Range 2 Base Low (Offset 34h) | DVSEC CXL 范围 2 基址低 (偏移 34h)

> **Table 8-19.** DVSEC CXL Range 2 Base Low (Offset 34h) ｜ DVSEC CXL 范围 2 基址低 (偏移 34h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 27:0 | RsvdP | Reserved — 保留 |
> | 31:28 | RWL | **Memory_Base_Low**: Corresponds to bits 31:28 of the CXL Range 2 base in the host address space. Locked by the CONFIG_LOCK bit in the DVSEC CXL Lock register.<br/>If a device implements CXL HDM Decoder Capability registers and software has enabled the HDM Decoder by setting the HDM Decoder Enable bit in the CXL HDM Decoder Global Control register, the value of this field is not used during address decode. It is recommended that software program this to match the corresponding CXL HDM Decoder Base Low register for backward compatibility.<br/>Default value of this field is 0h. — 对应主机地址空间中 CXL 范围 2 基址的 bit 31:28。由 DVSEC CXL Lock 寄存器中的 CONFIG_LOCK 位锁定。<br/>如果设备实现 CXL HDM Decoder Capability 寄存器并且软件通过设置 CXL HDM Decoder Global Control 寄存器中的 HDM Decoder Enable 位使能了 HDM Decoder，则此字段的值不参与地址解码。建议软件将其编程为与相应的 CXL HDM Decoder Base Low 寄存器匹配以保持向后兼容。<br/>默认值为 0h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-3-9"></a>
### 8.1.3.9 DVSEC CXL Capability3 (Offset 38h) | DVSEC CXL 能力 3 (偏移 38h)

> **Table 8-20.** DVSEC CXL Capability3 (Offset 38h) ｜ DVSEC CXL 能力 3 (偏移 38h)
>
> | Bit | Attributes | Description¹ / 描述¹ |
> |---|---|---|
> | 0 | HwInit | **Default Volatile HDM State after Cold Reset**²<br/>• 0 = The Volatile HDM content after a Cold Reset is undefined. The content may or may not be cleared. The content may or may not be randomized.<br/>• 1 = The device shall clear or randomize the volatile HDM content after a Cold reset. The clear or randomize operation shall be completed before Memory_Active is set. — 冷复位后易失性 HDM 的默认状态²<br/>• 0 = 冷复位后易失性 HDM 内容未定义。内容可能清除也可能不清除。可能已随机化也可能未随机化。<br/>• 1 = 设备应在冷复位后清除或随机化易失性 HDM 内容。清除或随机化操作应在 Memory_Active 置位之前完成。 |
> | 1 | HwInit | **Default Volatile HDM State after Warm Reset**²<br/>• 0 = The Volatile HDM content after a Warm Reset is undefined. The content may or may not be cleared. The content may or may not be randomized.<br/>• 1 = The device shall clear or randomize the volatile HDM content after a Warm Reset. The clear or randomize operation shall be completed before Memory_Active is set. — 温复位后易失性 HDM 的默认状态²<br/>• 0 = 温复位后易失性 HDM 内容未定义。内容可能清除也可能不清除。可能已随机化也可能未随机化。<br/>• 1 = 设备应在温复位后清除或随机化易失性 HDM 内容。清除或随机化操作应在 Memory_Active 置位之前完成。 |
> | 2 | HwInit | **Default Volatile HDM State after Hot Reset**²<br/>• 0 = The Volatile HDM content after a Hot Reset is undefined. The content may or may not be cleared. The content may or may not be randomized.<br/>• 1 = The device shall clear or randomize the volatile HDM content after a Hot Reset. The clear or randomize operation shall be completed before Memory_Active is set.<br/>If the Volatile HDM State after Hot Reset - Configurability bit is set, the software is permitted to override the Default State and request that the memory be preserved across a Hot Reset. — 热复位后易失性 HDM 的默认状态²<br/>• 0 = 热复位后易失性 HDM 内容未定义。内容可能清除也可能不清除。可能已随机化也可能未随机化。<br/>• 1 = 设备应在热复位后清除或随机化易失性 HDM 内容。清除或随机化操作应在 Memory_Active 置位之前完成。<br/>如果 Volatile HDM State after Hot Reset - Configurability 位置 1，则软件可以覆盖默认状态并请求在热复位期间保留内存内容。 |
> | 3 | HwInit | **Volatile HDM State after Hot Reset - Configurability**²<br/>• 0 = The device does not support preservation of Volatile HDM State across Hot Reset<br/>• 1 = The device supports preservation of Volatile HDM State across a Hot Reset. The Software may request the device to preserve Volatile HDM content across a Hot Reset by setting the Desired Volatile HDM State after Hot Reset bit prior to the Hot Reset event. — 热复位后易失性 HDM 状态可配置性²<br/>• 0 = 设备不支持在热复位期间保留易失性 HDM 状态<br/>• 1 = 设备支持在热复位期间保留易失性 HDM 状态。软件可以通过在热复位事件之前设置 Desired Volatile HDM State after Hot Reset 位来请求设备在热复位期间保留易失性 HDM 内容。 |
> | 4 | HwInit | **Direct P2P Mem Capable**: If set, indicates that the Direct P2P CXL.mem protocol is supported.³ — 置 1 时，表示支持 Direct P2P CXL.mem 协议。³ |
> | 15:5 | RsvdP | Reserved — 保留 |
>
> 1. This register was added as part of DVSEC Revision=2.
> 2. This bit was introduced as part of DVSEC Revision=2.
> 3. This bit was introduced as part of DVSEC Revision=3.
>
> 1. 此寄存器在 DVSEC Revision=2 中添加。
> 2. 此位在 DVSEC Revision=2 中引入。
> 3. 此位在 DVSEC Revision=3 中引入。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-4"></a>
## 8.1.4 Non-CXL Function Map DVSEC | 非 CXL 功能映射 DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This DVSEC capability identifies the list of device and function numbers associated with non-virtual functions (i.e., functions that are not a Virtual Function) implemented by CXL device that are not capable of participating in CXL.cache/CXL.mem protocol. The PCIe Configuration Space of Function 0 of a CXL device may include Non-CXL Function Map DVSEC as shown in Figure 8-2. See Table 8-2 for the complete listing. To advertise this capability, the standard DVSEC register fields must be set to the values shown in Table 8-5. The DVSEC Length field must be set to 02Ch bytes to accommodate the registers included in the DVSEC. The DVSEC ID must be set to 0002h to advertise that this is a Non-CXL Function Map DVSEC capability structure for CXL ports.</td><td style="background-color:#e8e8e8">此 DVSEC 能力标识了 CXL 设备实现的非虚拟功能 (即非 Virtual Function) 的设备号和功能号列表，这些功能无法参与 CXL.cache/CXL.mem 协议。CXL 设备功能 0 的 PCIe 配置空间可包含 Non-CXL Function Map DVSEC，如图 8-2 所示。完整列表请参见表 8-2。为了公布此能力，标准 DVSEC 寄存器字段必须设置为表 8-5 中所示的值。DVSEC Length 字段必须设置为 02Ch 字节以容纳 DVSEC 中包含的寄存器。DVSEC ID 必须设置为 0002h，以表明这是 CXL 端口的 Non-CXL Function Map DVSEC 能力结构。</td></tr>
<tr><td>If this DVSEC capability is present, it must be included in Function 0 of a CXL device and the Non-CXL Function Map bit corresponding to that Function shall be 0.</td><td style="background-color:#e8e8e8">如果此 DVSEC 能力存在，则必须包含在 CXL 设备的功能 0 中，并且对应于该功能的 Non-CXL Function Map 位必须为 0。</td></tr>
<tr><td>Absence of Non-CXL Function Map DVSEC indicates that PCIe DVSEC for CXL devices (Section 8.1.3) located on Function 0 governs whether all Functions participate in CXL.cache and CXL.mem protocol.</td><td style="background-color:#e8e8e8">缺少 Non-CXL Function Map DVSEC 表示位于功能 0 上的 PCIe DVSEC for CXL devices (8.1.3 节) 控制所有功能是否参与 CXL.cache 和 CXL.mem 协议。</td></tr>
</tbody>
</table>

> **Figure 8-2.** Non-CXL Function Map DVSEC ｜ 非 CXL 功能映射 DVSEC
>
> <img src="figures/chapter_08/fig_0514_1.png" alt="Figure 8-2" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0514.png)

> **Table 8-21.** Non-CXL Function Map DVSEC - Header ｜ 非 CXL 功能映射 DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 0h |
> | | 31:20 | DVSEC Length | 02Ch |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0002h |

#### 8.1.4.1 Non-CXL Function Map Register 0 (Offset 0Ch) | 非 CXL 功能映射寄存器 0 (偏移 0Ch)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: Each bit represents a non-virtual function number implemented by the device on the same bus as the physical function that carries PCIe DVSEC for CXL devices.<br/>When a bit is set, the corresponding Device/Function number or Function number (ARI device) is not capable of participating in CXL.cache or CXL.mem protocol. Bits corresponding to Non-existent Device/Function or Function numbers shall always return 0.<br/>If the device does not support ARI, bit x in this register maps to Device x, Function 0.<br/>If the device supports ARI, bit x in this register maps to Function x. — 每个 bit 表示由设备在与承载 PCIe DVSEC for CXL devices 的物理功能所在的同一总线上实现的非虚拟功能号。<br/>当某位置 1 时，对应的设备/功能号或功能号 (ARI 设备) 不能参与 CXL.cache 或 CXL.mem 协议。对应于不存在的设备/功能或功能号的位必须始终返回 0。<br/>如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 0。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 x。 |

#### 8.1.4.2 Non-CXL Function Map Register 1 (Offset 10h) | 非 CXL 功能映射寄存器 1 (偏移 10h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: Each bit represents a non-virtual function number implemented by the device on the same bus as the physical function that carries PCIe DVSEC for CXL devices.<br/>When a bit is set, the corresponding Device/Function number or Function number (ARI device) is not capable of participating in CXL.cache or CXL.mem protocol. Bits corresponding to Non-existent Device/Function or Function numbers shall always return 0.<br/>If the device does not support ARI, bit x in this register maps to Device x, Function 1.<br/>If the device supports ARI, bit x in this register maps to Function x+32. — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 1。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 x+32。 |

#### 8.1.4.3 Non-CXL Function Map Register 2 (Offset 14h) | 非 CXL 功能映射寄存器 2 (偏移 14h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: If the device does not support ARI, bit x in this register maps to Device x, Function 2.<br/>If the device supports ARI, bit x in this register maps to Function (x+64). — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 2。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 (x+64)。 |

#### 8.1.4.4 Non-CXL Function Map Register 3 (Offset 18h) | 非 CXL 功能映射寄存器 3 (偏移 18h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: If the device does not support ARI, bit x in this register maps to Device x, Function 3.<br/>If the device supports ARI, bit x in this register maps to Function (x+96). — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 3。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 (x+96)。 |

#### 8.1.4.5 Non-CXL Function Map Register 4 (Offset 1Ch) | 非 CXL 功能映射寄存器 4 (偏移 1Ch)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: If the device does not support ARI, bit x in this register maps to Device x, Function 4.<br/>If the device supports ARI, bit x in this register maps to Function (x+128). — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 4。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 (x+128)。 |

#### 8.1.4.6 Non-CXL Function Map Register 5 (Offset 20h) | 非 CXL 功能映射寄存器 5 (偏移 20h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: If the device does not support ARI, bit x in this register maps to Device x, Function 5.<br/>If the device supports ARI, bit x in this register maps to Function (x+160). — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 5。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 (x+160)。 |

#### 8.1.4.7 Non-CXL Function Map Register 6 (Offset 24h) | 非 CXL 功能映射寄存器 6 (偏移 24h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: If the device does not support ARI, bit x in this register maps to Device x, Function 6.<br/>If the device supports ARI, bit x in this register maps to Function (x+192). — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 6。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 (x+192)。 |

#### 8.1.4.8 Non-CXL Function Map Register 7 (Offset 28h) | 非 CXL 功能映射寄存器 7 (偏移 28h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Non CXL Function**: If the device does not support ARI, bit x in this register maps to Device x, Function 7.<br/>If the device supports ARI, bit x in this register maps to Function (x+224). — 如果设备不支持 ARI，此寄存器中的 bit x 映射到设备 x、功能 7。<br/>如果设备支持 ARI，此寄存器中的 bit x 映射到功能 (x+224)。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-5"></a>
## 8.1.5 CXL Extensions DVSEC for Ports | 端口的 CXL 扩展 DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The PCIe Configuration Space of a CXL root port, CXL Downstream Switch Port, and CXL Upstream Switch Port must implement this DVSEC capability as shown in Figure 8-3. See Table 8-2 for the complete listing. To advertise this capability, the standard DVSEC register fields must be set to the values shown in Table 8-6. The DVSEC Length field must be set to 028h bytes to accommodate the registers included in the DVSEC. The DVSEC ID must be set to 0003h to advertise that this is a CXL Extension DVSEC capability structure for CXL ports.</td><td style="background-color:#e8e8e8">CXL 根端口、CXL 下行交换端口和 CXL 上行交换端口的 PCIe 配置空间必须实现此 DVSEC 能力，如图 8-3 所示。完整列表请参见表 8-2。为了公布此能力，标准 DVSEC 寄存器字段必须设置为表 8-6 中所示的值。DVSEC Length 字段必须设置为 028h 字节以容纳 DVSEC 中包含的寄存器。DVSEC ID 必须设置为 0003h，以表明这是 CXL 端口的 CXL Extension DVSEC 能力结构。</td></tr>
</tbody>
</table>

> **Figure 8-3.** CXL Extensions DVSEC for Ports ｜ 端口的 CXL 扩展 DVSEC
>
> <img src="figures/chapter_08/fig_0517_1.png" alt="Figure 8-3" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0517.png)

> **Table 8-22.** CXL Extensions DVSEC for Ports - Header ｜ 端口的 CXL 扩展 DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 0h |
> | | 31:20 | DVSEC Length | 028h |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0003h |

#### 8.1.5.1 CXL Port Extension Status (Offset 0Ah) | CXL 端口扩展状态 (偏移 0Ah)

> **Table 8-23.** CXL Port Extension Status (Offset 0Ah) ｜ CXL 端口扩展状态 (偏移 0Ah)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RO | **Port Power Management Initialization Complete**: When set, it indicates that the root port, the Upstream Switch Port or the Downstream Switch Port has successfully completed the Power Management Initialization Flow as described in Figure 3-4 and is ready to process various Power Management events.<br/>If this bit is not set within 100 ms of link-up, software may conclude that the Power Management initialization has failed and may issue Secondary Bus Reset to force link re-initialization and Power Management re-initialization. See Implementation Note. — 端口电源管理初始化完成：置 1 时，表示根端口、上行交换端口或下行交换端口已成功完成图 3-4 中描述的电源管理初始化流程，并准备好处理各种电源管理事件。<br/>如果在 link-up 后的 100 ms 内该位仍未置位，软件可判定电源管理初始化失败，并可发出 Secondary Bus Reset 以强制链路重新初始化和电源管理重新初始化。参见实现说明。 |
> | 13:1 | RsvdP | Reserved — 保留 |
> | 14 | RW1CS | **Viral Status**: When set, indicates that the Upstream Switch Port or the Downstream Switch Port has entered Viral (see Section 12.4 for more details).<br/>This bit is not applicable to Root Ports, and reads shall return the value of 0. — 置 1 时，表示上行交换端口或下行交换端口已进入 Viral (详见 12.4 节)。<br/>此位不适用于根端口，读取时应返回 0。 |
> | 15 | RsvdP | Reserved — 保留 |

> **IMPLEMENTATION NOTE** ｜ 实现说明
>
> Certain conditions such as Link Down, Secondary Bus Reset, or Downstream Port Containment reset the Downstream Component's bus number. If the Component generates the CREDIT_RTN IP2PM message with Requestor Bus=0, the Downstream Port may reject it if software has enabled ACS Source Validation. In this scenario, Power Management initialization may fail to complete and another Secondary Bus Reset alone will not facilitate recovery. Software may use the following sequence to recover from this failure:
>
> 某些情况 (如链路断开、Secondary Bus Reset 或 Downstream Port Containment) 会重置下行组件的总线号。如果组件以 Requestor Bus=0 生成 CREDIT_RTN IP2PM 消息，则在软件启用了 ACS Source Validation 时，下行端口可能会拒绝该消息。在这种情况下，电源管理初始化可能无法完成，单独再进行 Secondary Bus Reset 也不会实现恢复。软件可以使用以下序列从此故障中恢复：
>
> 1. Save the ACS Source Validation bit and the Bus Master Enable bit in the Downstream Port. — 在下行端口中保存 ACS Source Validation 位和 Bus Master Enable 位。
> 2. Clear Downstream Port's Bus Master Enable bit to 0. — 将下行端口的 Bus Master Enable 位清零。
> 3. Clear Downstream Port's ACS Source Validation bit to 0. — 将下行端口的 ACS Source Validation 位清零。
> 4. Generate Secondary Bus Reset. — 生成 Secondary Bus Reset。
> 5. Wait until the Port Power Management Initialization Complete bit is set in the Downstream Port. — 等待下行端口中 Port Power Management Initialization Complete 位置位。
> 6. Restore the ACS Source Validation bit and the Bus Master Enable setting in the Downstream Port. — 恢复下行端口中的 ACS Source Validation 位和 Bus Master Enable 设置。
> 7. Continue with device re-initialization. — 继续设备重新初始化。

#### 8.1.5.2 Port Control Extensions (Offset 0Ch) | 端口控制扩展 (偏移 0Ch)

> **Table 8-24.** Port Control Extensions (Offset 0Ch) ｜ 端口控制扩展 (偏移 0Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RW | **Unmask SBR**: When 0, SBR bit in Bridge Control register of this Port has no effect.<br/>When 1, the Port shall generate hot reset when SBR bit in Bridge Control gets set to 1.<br/>Default value of this bit is 0.<br/>When the Port is operating in PCIe mode or RCD mode, this field has no effect on SBR functionality and Port shall follow PCIe Base Specification. — 为 0 时，此端口 Bridge Control 寄存器中的 SBR 位无效。<br/>为 1 时，端口应在 Bridge Control 中的 SBR 位置 1 时生成热复位。<br/>默认值为 0。<br/>当端口在 PCIe 模式或 RCD 模式下运行时，此字段对 SBR 功能无影响，端口应遵循 PCIe 基础规范。 |
> | 1 | RW | **Unmask Link Disable**: When 0, Link Disable bit in Link Control register of this Port has no effect.<br/>When 1, the Port shall disable the CXL Link when Link Disable bit in Link Control gets set to 1 and Link is re-enabled when Link Disable bit in Link control is cleared to 0.<br/>Default value of this bit is 0.<br/>When the Port is operating in PCIe mode or RCD mode, this field has no effect on Link Disable functionality and the Port shall follow PCIe Base Specification. — 为 0 时，此端口 Link Control 寄存器中的 Link Disable 位无效。<br/>为 1 时，端口应在 Link Control 中的 Link Disable 位置 1 时禁用 CXL 链路，并在 Link Control 中的 Link Disable 位清零时重新启用链路。<br/>默认值为 0。<br/>当端口在 PCIe 模式或 RCD 模式下运行时，此字段对 Link Disable 功能无影响，端口应遵循 PCIe 基础规范。 |
> | 2 | RW | **Alt Memory and ID Space Enable**: When set to 1, the Port positively decodes downstream transactions to ranges specified in Alternate Memory Base/Limit registers, Alternate Prefetchable Memory Base/Limit, Alternate Prefetchable Base/Limit Upper 32 Bits and Alternate Bus Base/Limit registers regardless of the Memory Space Enable bit in the PCIe Command register.<br/>When cleared to 0, the Port does not decode downstream transactions to ranges specified in Alternate Memory Base/Limit registers, Alternate Prefetchable Memory Base/Limit, Alternate Prefetchable Base/Limit Upper 32 Bits and Alternate Bus Base/Limit registers.<br/>Default value of this bit is 0.<br/>Firmware/Software must ensure this bit is 0 when the Port is operating in PCIe mode. — 置 1 时，端口对 Alternate Memory Base/Limit 寄存器、Alternate Prefetchable Memory Base/Limit、Alternate Prefetchable Base/Limit Upper 32 Bits 和 Alternate Bus Base/Limit 寄存器中指定范围的下行事务进行正解码，与 PCIe Command 寄存器中的 Memory Space Enable 位无关。<br/>清零为 0 时，端口不解码 Alternate Memory Base/Limit 寄存器、Alternate Prefetchable Memory Base/Limit、Alternate Prefetchable Base/Limit Upper 32 Bits 和 Alternate Bus Base/Limit 寄存器中指定范围的下行事务。<br/>默认值为 0。<br/>固件/软件必须确保端口在 PCIe 模式下运行时此位为 0。 |
> | 3 | RW | **Alt BME**: This bit overrides the state of BME bit in Command register if the requester's bus number is within the range specified by Alternate Bus Base and Alternate Bus Limit range.<br/>This bit alone controls forwarding of Memory or I/O Requests by a Port in the Upstream direction if the requester's bus number is within the range specified by Alternate Bus Base and Alternate Bus Limit range.<br/>If the requester's bus number is within the range specified by Alternate Bus Base and Alternate Bus Limit range and this bit is 0, Memory and I/O Requests received at a Root Port or the Downstream side of a Switch Port must be handled as Unsupported Requests (UR), and for Non-Posted Requests a Completion with UR Completion Status must be returned. This bit does not affect forwarding of Completions in either the Upstream or Downstream direction.<br/>Default value of this bit is 0.<br/>Firmware/Software must ensure this bit is 0 when the Port is operating in PCIe mode. — 如果请求者的总线号在 Alternate Bus Base 和 Alternate Bus Limit 范围内，则此位覆盖 Command 寄存器中的 BME 位状态。<br/>如果请求者的总线号在 Alternate Bus Base 和 Alternate Bus Limit 范围内，则此位单独控制端口在上行方向上转发内存或 I/O 请求。<br/>如果请求者的总线号在 Alternate Bus Base 和 Alternate Bus Limit 范围内且此位为 0，则在根端口或交换端口下行侧接收的内存和 I/O 请求必须作为不支持请求 (UR) 处理，对于 Non-Posted 请求必须返回具有 UR 完成状态的完成。此位不影响上行或下行方向的完成转发。<br/>默认值为 0。<br/>固件/软件必须确保端口在 PCIe 模式下运行时此位为 0。 |
> | 4 | RW/RsvdP | **UIO To HDM Enable**<br/>• DSP that is capable of UIO Direct P2P accesses to HDM: This bit is RW. If 0, return Completer Abort to UIO accesses with Complete of Partial Match. See Table 9-18 for details. The default value of this bit is 0.<br/>• All others: This bit is RsvdP. It is permitted to be hardwired to 0 and software must not set this bit. — UIO 至 HDM 使能<br/>• 支持 UIO Direct P2P 访问 HDM 的 DSP：此位为 RW。如果为 0，则对 Complete of Partial Match 的 UIO 访问返回 Completer Abort。详见表 9-18。此位默认值为 0。<br/>• 所有其他：此位为 RsvdP。可硬连线为 0，软件不得设置此位。 |
> | 13:5 | RsvdP | Reserved — 保留 |
> | 14 | RW | **Viral Enable**: When set, enables Viral generation functionality of the Upstream Switch Port or the Downstream Switch Port. See Section 12.4 for more details.<br/>If 0, the port shall not generate viral.<br/>Default value of this bit is 0.<br/>Regardless of the state of this bit, a switch shall always forward viral as described in Section 12.4.<br/>This bit is not applicable to root ports, and reads shall return the value of 0. Viral behavior of a Root Port may be controlled by a host specific configuration mechanism. — 置 1 时，使能上行交换端口或下行交换端口的 Viral 生成功能。详见 12.4 节。<br/>若为 0，则端口不应生成 viral。<br/>默认值为 0。<br/>无论此位状态如何，交换器应始终按 12.4 节所述转发 viral。<br/>此位不适用于根端口，读取时应返回 0。根端口的 Viral 行为可由主机特定配置机制控制。 |
> | 15 | RsvdP | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

#### 8.1.5.3 Alternate Bus Base (Offset 0Eh) | 备用总线基址 (偏移 0Eh)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Alternate Bus Base Number and Alternate Bus Limit Number registers define a bus range that is decoded by the Port in addition to the standard Secondary Bus Number to Subordinate Bus Number range. An ID-routed TLP transaction received from the primary interface is forwarded to the secondary interface if the bus number is not less than the Alternate Bus Base and not greater than the Alternate Bus Limit. See Figure 9-11.</td><td style="background-color:#e8e8e8">Alternate Bus Base Number 和 Alternate Bus Limit Number 寄存器定义了除标准 Secondary Bus Number 到 Subordinate Bus Number 范围之外，端口还应解码的总线范围。如果从主接口接收的 ID 路由 TLP 事务的总线号不小于 Alternate Bus Base 且不大于 Alternate Bus Limit，则将其转发到副接口。参见图 9-11。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 7:0 | RW | **Alt Bus Base**: The lowest bus number that is positively decoded by this Port as part of alternate decode path.<br/>Default value of this field is 0. — 此端口作为备用解码路径正解码的最低总线号。<br/>此字段默认值为 0。 |

#### 8.1.5.4 Alternate Bus Limit (Offset 0Fh) | 备用总线限值 (偏移 0Fh)

See Section 8.1.5.3, "Alternate Bus Base (Offset 0Eh)." ｜ 参见 8.1.5.3 节 "Alternate Bus Base (Offset 0Eh)"。

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 7:0 | RW | **Alt Bus Limit**: The highest bus number that is positively decoded by this Port as part of alternate decode path.<br/>Default value of this field is 0.<br/>Alternate bus decoder is disabled if Alt Memory and ID Space Enable=0. — 此端口作为备用解码路径正解码的最高总线号。<br/>此字段默认值为 0。<br/>如果 Alt Memory and ID Space Enable=0，则禁用备用总线解码器。 |

#### 8.1.5.5 Alternate Memory Base (Offset 10h) | 备用内存基址 (偏移 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Alternate Memory Base and Alternate Memory Limit registers define a memory mapped address range that is in addition to the standard Memory Base and Memory Limit registers. Alternate Memory Base and Alternate Memory Limit registers are functionally equivalent to PCIe-defined Memory Base and Memory Limit registers. These are used by the Port to determine when to forward memory transactions from one interface to the other. See Figure 9-10.</td><td style="background-color:#e8e8e8">Alternate Memory Base 和 Alternate Memory Limit 寄存器定义了除标准 Memory Base 和 Memory Limit 寄存器之外的内存映射地址范围。Alternate Memory Base 和 Alternate Memory Limit 寄存器在功能上等同于 PCIe 定义的 Memory Base 和 Memory Limit 寄存器。端口使用这些寄存器确定何时将内存事务从一个接口转发到另一个接口。参见图 9-10。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RsvdP | Reserved — 保留 |
> | 15:4 | RW | **Alt Mem Base**: Corresponds to A[31:20] of the CXL.io Alternate memory base address. See definition of Memory Base register in PCIe Base Specification.<br/>Default value of this field is 000h. — 对应 CXL.io 备用内存基址的 A[31:20]。参见 PCIe 基础规范中 Memory Base 寄存器的定义。<br/>此字段默认值为 000h。 |

#### 8.1.5.6 Alternate Memory Limit (Offset 12h) | 备用内存限值 (偏移 12h)

See Section 8.1.5.5, "Alternate Memory Base (Offset 10h)." ｜ 参见 8.1.5.5 节 "Alternate Memory Base (Offset 10h)"。

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RsvdP | Reserved — 保留 |
> | 15:4 | RW | **Alt Mem Limit**: Corresponds to A[31:20] of the CXL.io Alternate memory limit address. See definition of Memory Limit register in PCIe Base Specification.<br/>Default value of this field is 000h. — 对应 CXL.io 备用内存限值的 A[31:20]。参见 PCIe 基础规范中 Memory Limit 寄存器的定义。<br/>此字段默认值为 000h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

#### 8.1.5.7 Alternate Prefetchable Memory Base (Offset 14h) | 备用可预取内存基址 (偏移 14h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Alternate Prefetchable Memory Base, Alternate Prefetchable Memory Base High, Alternate Prefetchable Memory Limit, and Alternate Prefetchable Memory Limit High registers define a 64-bit memory mapped address range that is in addition to the one defined by the PCIe standard Prefetchable Memory Base, Prefetchable Base Upper 32 bits, Prefetchable Memory Limit, and Prefetchable Limit Upper 32 bits registers. Alternate Prefetchable Memory registers are functionally equivalent to PCIe-defined Prefetchable Memory registers. These are used by the Port to determine when to forward Prefetchable memory transactions from one interface to the other.</td><td style="background-color:#e8e8e8">Alternate Prefetchable Memory Base、Alternate Prefetchable Memory Base High、Alternate Prefetchable Memory Limit 和 Alternate Prefetchable Memory Limit High 寄存器定义了除 PCIe 标准 Prefetchable Memory Base、Prefetchable Base Upper 32 bits、Prefetchable Memory Limit 和 Prefetchable Limit Upper 32 bits 寄存器定义的 64 位内存映射地址范围之外的范围。Alternate Prefetchable Memory 寄存器在功能上等同于 PCIe 定义的 Prefetchable Memory 寄存器。端口使用这些寄存器确定何时将可预取内存事务从一个接口转发到另一个接口。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RsvdP | Reserved — 保留 |
> | 15:4 | RW | **Alt Prefetch Mem Base**: Corresponds to A[31:20] of the CXL.io Alternate Prefetchable memory base address. See definition of Prefetchable Memory Base register in PCIe Base Specification.<br/>Default value of this field is 000h. — 对应 CXL.io 备用可预取内存基址的 A[31:20]。参见 PCIe 基础规范中 Prefetchable Memory Base 寄存器的定义。<br/>此字段默认值为 000h。 |

#### 8.1.5.8 Alternate Prefetchable Memory Limit (Offset 16h) | 备用可预取内存限值 (偏移 16h)

See Section 8.1.5.7, "Alternate Prefetchable Memory Base (Offset 14h)." ｜ 参见 8.1.5.7 节 "Alternate Prefetchable Memory Base (Offset 14h)"。

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RsvdP | Reserved — 保留 |
> | 15:4 | RW | **Alt Prefetch Mem Limit**: Corresponds to A[31:20] of the CXL.io Alternate Prefetchable memory limit address. See definition of Prefetchable memory limit register in PCIe Base Specification.<br/>Default value of this field is 000h. — 对应 CXL.io 备用可预取内存限值的 A[31:20]。参见 PCIe 基础规范中 Prefetchable memory limit 寄存器的定义。<br/>此字段默认值为 000h。 |

#### 8.1.5.9 Alternate Memory Prefetchable Base High (Offset 18h) | 备用内存可预取基址高 (偏移 18h)

See Section 8.1.5.7, "Alternate Prefetchable Memory Base (Offset 14h)." ｜ 参见 8.1.5.7 节 "Alternate Prefetchable Memory Base (Offset 14h)"。

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RW | **Alt Prefetch Base High**: Corresponds to A[63:32] of the CXL.io Alternate Prefetchable memory base address. See definition of Prefetchable Base Upper 32 Bits register in PCIe Base Specification.<br/>Default value of this register is 0000 0000h. — 对应 CXL.io 备用可预取内存基址的 A[63:32]。参见 PCIe 基础规范中 Prefetchable Base Upper 32 Bits 寄存器的定义。<br/>此寄存器默认值为 0000 0000h。 |

#### 8.1.5.10 Alternate Prefetchable Memory Limit High (Offset 1Ch) | 备用可预取内存限值高 (偏移 1Ch)

See Section 8.1.5.7, "Alternate Prefetchable Memory Base (Offset 14h)." ｜ 参见 8.1.5.7 节 "Alternate Prefetchable Memory Base (Offset 14h)"。

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RW | **Alt Prefetch Limit High**: Corresponds to A[63:32] of the CXL.io Alternate Prefetchable memory limit address. See definition of Prefetchable Limit Upper 32 Bits register in PCIe Base Specification.<br/>Default value of this register is 0000 0000h. — 对应 CXL.io 备用可预取内存限值的 A[63:32]。参见 PCIe 基础规范中 Prefetchable Limit Upper 32 Bits 寄存器的定义。<br/>此寄存器默认值为 0000 0000h。 |

#### 8.1.5.11 CXL RCRB Base (Offset 20h) | CXL RCRB 基址 (偏移 20h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This register is only relevant to CXL root ports and Downstream Switch Ports. Software programs this register to transition a Port to operate using RCD addressing. Software may take this step upon determining that the Port is connected to an eRCD.</td><td style="background-color:#e8e8e8">此寄存器仅与 CXL 根端口和下行交换端口相关。软件通过编程此寄存器将端口转换为使用 RCD 寻址操作。软件可以在确定端口连接到 eRCD 后执行此步骤。</td></tr>
<tr><td>System Firmware must ensure CXL RCRB Enable is 0, whenever the Port is operating in PCIe mode.</td><td style="background-color:#e8e8e8">当端口在 PCIe 模式下运行时，系统固件必须确保 CXL RCRB Enable 为 0。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RW | **CXL RCRB Enable**: When set, the RCRB region is enabled and the registers belonging to this Port can be accessed via RCH Downstream Port RCRB. After this write is complete, the Port registers shall no longer appear in Configuration Space, but rather in MMIO space starting at RCRB Base. Once a Port is transitioned to use RCD addressing, the software is responsible for ensuring it remains in that mode until the next Conventional Reset and RCRB Base Address is not modified; otherwise, the hardware behavior is undefined.<br/>Default value of this bit is 0. — 置 1 时，RCRB 区域使能，端口所属寄存器可通过 RCH Downstream Port RCRB 访问。此次写入完成后，端口寄存器应不再出现在配置空间中，而是出现在从 RCRB Base 开始的 MMIO 空间中。一旦端口转换为使用 RCD 寻址，软件应负责确保端口保持此模式直到下一次 Conventional Reset，并且不修改 RCRB Base Address；否则硬件行为未定义。<br/>默认值为 0。 |
> | 12:1 | RsvdP | Reserved — 保留 |
> | 31:13 | RW | **CXL RCRB Base Address Low**: This points to the address bits[31:13] of an 8-KB memory region where the lower 4-KB hosts the RCH Downstream Port RCRB and the upper 4-KB hosts the RCD Upstream Port RCRB.<br/>Default value of this field is 0 0000h. — 指向 8-KB 内存区域的地址位 [31:13]，其中低 4-KB 承载 RCH 下行端口 RCRB，高 4-KB 承载 RCD 上行端口 RCRB。<br/>此字段默认值为 0 0000h。 |

#### 8.1.5.12 CXL RCRB Base High (Offset 24h) | CXL RCRB 基址高 (偏移 24h)

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RW | **CXL RCRB Base Address High**: This points to the address bits [63:32] of an 8-KB memory region where the lower 4-KB hosts the RCH Downstream Port RCRB and the upper 4-KB hosts the RCD Upstream Port RCRB.<br/>Default value of this register is 0000 0000h. — 指向 8-KB 内存区域的地址位 [63:32]，其中低 4-KB 承载 RCH 下行端口 RCRB，高 4-KB 承载 RCD 上行端口 RCRB。<br/>此寄存器默认值为 0000 0000h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-6"></a>
## 8.1.6 GPF DVSEC for CXL Port | CXL 端口的 GPF DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The PCIe Configuration Space of CXL Downstream Switch Ports and CXL root ports must implement this DVSEC capability as shown in Figure 8-4. See Table 8-2 for the complete listing.</td><td style="background-color:#e8e8e8">CXL 下行交换端口和 CXL 根端口的 PCIe 配置空间必须实现此 DVSEC 能力，如图 8-4 所示。完整列表请参见表 8-2。</td></tr>
<tr><td>To advertise this capability, the standard DVSEC register fields must be set to the values shown in Table 8-7. The DVSEC Length field must be set to 010h bytes to accommodate the registers included in the DVSEC. The DVSEC ID must be set to 0004h to advertise that this is an GPF DVSEC capability structure for CXL ports.</td><td style="background-color:#e8e8e8">为了公布此能力，标准 DVSEC 寄存器字段必须设置为表 8-7 中所示的值。DVSEC Length 字段必须设置为 010h 字节以容纳 DVSEC 中包含的寄存器。DVSEC ID 必须设置为 0004h，以表明这是 CXL 端口的 GPF DVSEC 能力结构。</td></tr>
</tbody>
</table>

> **Figure 8-4.** GPF DVSEC for CXL Port ｜ CXL 端口的 GPF DVSEC
>
> <img src="figures/chapter_08/fig_0522_1.png" alt="Figure 8-4" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0522.png)

> **Table 8-25.** GPF DVSEC for CXL Port - Header ｜ CXL 端口的 GPF DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 0h |
> | | 31:20 | DVSEC Length | 010h |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0004h |

#### 8.1.6.1 GPF Phase 1 Control (Offset 0Ch) | GPF 阶段 1 控制 (偏移 0Ch)

> **Table 8-26.** GPF Phase 1 Control (Offset 0Ch) ｜ GPF 阶段 1 控制 (偏移 0Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RW | **Port GPF Phase 1 Timeout Base**: This field determines the GPF Phase 1 timeout. The timeout duration is calculated by multiplying the Timeout Base with the Timeout Scale. — 此字段确定 GPF 阶段 1 的超时值。超时时长由 Timeout Base 乘以 Timeout Scale 计算得出。 |
> | 7:4 | RsvdP | Reserved — 保留 |
> | 11:8 | RW | **Port GPF Phase 1 Timeout Scale**: This field specifies the time scale associated with GPF Phase 1 Timeout.<br/>• 0h = 1 us<br/>• 1h = 10 us<br/>• 2h = 100 us<br/>• 3h = 1 ms<br/>• 4h = 10 ms<br/>• 5h = 100 ms<br/>• 6h = 1 s<br/>• 7h = 10 s<br/>• All other encodings are reserved — 此字段指定与 GPF 阶段 1 超时关联的时间粒度。<br/>• 0h = 1 us<br/>• 1h = 10 us<br/>• 2h = 100 us<br/>• 3h = 1 ms<br/>• 4h = 10 ms<br/>• 5h = 100 ms<br/>• 6h = 1 s<br/>• 7h = 10 s<br/>• 所有其他编码保留 |
> | 15:12 | RsvdP | Reserved — 保留 |

#### 8.1.6.2 GPF Phase 2 Control (Offset 0Eh) | GPF 阶段 2 控制 (偏移 0Eh)

> **Table 8-27.** GPF Phase 2 Control (Offset 0Eh) ｜ GPF 阶段 2 控制 (偏移 0Eh)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RW | **Port GPF Phase 2 Timeout Base**: This field determines the GPF Phase 2 timeout. The timeout duration is calculated by multiplying the Timeout Base with the Timeout Scale. — 此字段确定 GPF 阶段 2 的超时值。超时时长由 Timeout Base 乘以 Timeout Scale 计算得出。 |
> | 7:4 | RsvdP | Reserved — 保留 |
> | 11:8 | RW | **Port GPF Phase 2 Timeout Scale**: This field specifies the time scale associated with GPF Phase 2 Timeout.<br/>• 0h = 1 us<br/>• 1h = 10 us<br/>• 2h = 100 us<br/>• 3h = 1 ms<br/>• 4h = 10 ms<br/>• 5h = 100 ms<br/>• 6h = 1 s<br/>• 7h = 10 s<br/>• All other encodings are reserved — 此字段指定与 GPF 阶段 2 超时关联的时间粒度。<br/>• 0h = 1 us<br/>• 1h = 10 us<br/>• 2h = 100 us<br/>• 3h = 1 ms<br/>• 4h = 10 ms<br/>• 5h = 100 ms<br/>• 6h = 1 s<br/>• 7h = 10 s<br/>• 所有其他编码保留 |
> | 15:12 | RsvdP | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-7"></a>
## 8.1.7 GPF DVSEC for CXL Device | CXL 设备的 GPF DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Function 0 of CXL.mem-capable devices must implement this DVSEC capability (see Figure 8-5) if the device supports GPF (see Table 8-2 for the complete listing). A device that does not support CXL.mem must not implement DVSEC Revision 0 capability. To advertise this capability, the standard DVSEC register fields must be set to the values shown in Table 8-8. The DVSEC Length field must be set to 010h bytes to accommodate the registers included in the DVSEC. The DVSEC ID must be set to 0005h to advertise that this is an GPF DVSEC structure for CXL devices.</td><td style="background-color:#e8e8e8">如果设备支持 GPF，则支持 CXL.mem 的设备的功能 0 必须实现此 DVSEC 能力 (见图 8-5) (完整列表请参见表 8-2)。不支持 CXL.mem 的设备不得实现 DVSEC Revision 0 能力。为了公布此能力，标准 DVSEC 寄存器字段必须设置为表 8-8 中所示的值。DVSEC Length 字段必须设置为 010h 字节以容纳 DVSEC 中包含的寄存器。DVSEC ID 必须设置为 0005h，以表明这是 CXL 设备的 GPF DVSEC 结构。</td></tr>
</tbody>
</table>

> **Figure 8-5.** GPF DVSEC for CXL Device ｜ CXL 设备的 GPF DVSEC
>
> <img src="figures/chapter_08/fig_0524_1.png" alt="Figure 8-5" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0524.png)

> **Table 8-28.** GPF DVSEC for CXL Device - Header ｜ CXL 设备的 GPF DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 0h |
> | | 31:20 | DVSEC Length | 010h |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0005h |

#### 8.1.7.1 GPF Phase 2 Duration (Offset 0Ah) | GPF 阶段 2 持续时间 (偏移 0Ah)

> **Table 8-29.** GPF Phase 2 Duration (Offset 0Ah) ｜ GPF 阶段 2 持续时间 (偏移 0Ah)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 3:0 | RO | **Device GPF Phase 2 Time Base**: This field reports the maximum amount of time this device would take to complete GPF Phase 2. The time duration is calculated by multiplying the Time Base with the Time Scale. — 此字段报告此设备完成 GPF 阶段 2 所需的最长时间。时长由 Time Base 乘以 Time Scale 计算得出。 |
> | 7:4 | RsvdP | Reserved — 保留 |
> | 11:8 | RO | **Device GPF Phase 2 Time Scale**: This field specifies the time scale associated with Device GPF Phase 2 Time.<br/>• 0h = 1 us<br/>• 1h = 10 us<br/>• 2h = 100 us<br/>• 3h = 1 ms<br/>• 4h = 10 ms<br/>• 5h = 100 ms<br/>• 6h = 1 s<br/>• 7h = 10 s<br/>• All other encodings are reserved — 此字段指定与设备 GPF 阶段 2 时间关联的时间粒度。<br/>• 0h = 1 us<br/>• 1h = 10 us<br/>• 2h = 100 us<br/>• 3h = 1 ms<br/>• 4h = 10 ms<br/>• 5h = 100 ms<br/>• 6h = 1 s<br/>• 7h = 10 s<br/>• 所有其他编码保留 |
> | 15:12 | RsvdP | Reserved — 保留 |

#### 8.1.7.2 GPF Phase 2 Power (Offset 0Ch) | GPF 阶段 2 功率 (偏移 0Ch)

> **Table 8-30.** GPF Phase 2 Power (Offset 0Ch) ｜ GPF 阶段 2 功率 (偏移 0Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | RO | **GPF Phase 2 Active Power**: Active power consumed by the device during GPF Phase 2. Expressed in multiples of mW. — 设备在 GPF 阶段 2 期间消耗的有效功率。以 mW 的倍数表示。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-8"></a>
## 8.1.8 PCIe DVSEC for Flex Bus Port | Flex Bus 端口的 PCIe DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>See Section 8.2.1.3 for the register layout.</td><td style="background-color:#e8e8e8">寄存器布局参见 8.2.1.3 节。</td></tr>
<tr><td>In RCHs and RCDs that implement RCRB, this DVSEC is accessed via RCRB.</td><td style="background-color:#e8e8e8">在实现 RCRB 的 RCH 和 RCD 中，此 DVSEC 通过 RCRB 访问。</td></tr>
<tr><td>The DVSEC associated with all other CXL devices shall be accessible via Function 0 of the device. Upstream Switch Ports, Downstream Switch Ports, and CXL root ports shall implement this DVSEC in the Configuration Space associated with the Port. See Table 8-2 for the complete listing.</td><td style="background-color:#e8e8e8">与所有其他 CXL 设备关联的此 DVSEC 应通过设备的功能 0 访问。上行交换端口、下行交换端口和 CXL 根端口应在与端口关联的配置空间中实现此 DVSEC。完整列表请参见表 8-2。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-9"></a>
## 8.1.9 Register Locator DVSEC | 寄存器定位器 DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The PCIe Configuration Space of a CXL root port, CXL Downstream Switch Port, CXL Upstream Switch Port, and non-RCDs must implement this DVSEC capability. If a CXL device implements Register Locator DVSEC, it must appear in Function 0 of the device. This requirement does not apply to CXL Switches.</td><td style="background-color:#e8e8e8">CXL 根端口、CXL 下行交换端口、CXL 上行交换端口以及非 RCD 的 PCIe 配置空间必须实现此 DVSEC 能力。如果 CXL 设备实现 Register Locator DVSEC，则它必须出现在设备的功能 0 中。此要求不适用于 CXL 交换器。</td></tr>
<tr><td>This DVSEC capability contains one or more Register Block entries. Figure 8-6 illustrates a DVSEC Capability with 3 Register Block Entries. See Table 8-2 for the complete listing.</td><td style="background-color:#e8e8e8">此 DVSEC 能力包含一个或多个寄存器块条目。图 8-6 展示了包含 3 个寄存器块条目的 DVSEC 能力。完整列表请参见表 8-2。</td></tr>
<tr><td>Each register block included in the Register Locator DVSEC has an Offset Low and an Offset High register to specify the location of the registers within the Memory Space. The Offset Low register includes an identifier which specifies the type of CXL registers. Each register block identifier shall only occur once in the Register Locator DVSEC structure, except for the Designated Vendor Specific register block identifier or the CPMU register block identifier where multiple instances are allowed. Each register block must be contained within the address range covered by the associated BAR.</td><td style="background-color:#e8e8e8">Register Locator DVSEC 中包含的每个寄存器块都有一个 Offset Low 和 Offset High 寄存器，用于指定寄存器在内存空间中的位置。Offset Low 寄存器包含一个标识符，用于指定 CXL 寄存器的类型。除 Designated Vendor Specific 寄存器块标识符或 CPMU 寄存器块标识符允许多个实例外，每个寄存器块标识符在 Register Locator DVSEC 结构中只能出现一次。每个寄存器块必须包含在关联 BAR 覆盖的地址范围内。</td></tr>
<tr><td>To advertise this capability, the standard DVSEC register fields must be set to the values shown in Table 8-9. The DVSEC Length field must be set to (0Ch+ n * 8) bytes to accommodate the registers included in the DVSEC, where n is the number of Register Blocks described by this Capability. The DVSEC ID must be set to 0008h to advertise that this is a CXL Register Locator DVSEC capability structure.</td><td style="background-color:#e8e8e8">为了公布此能力，标准 DVSEC 寄存器字段必须设置为表 8-9 中所示的值。DVSEC Length 字段必须设置为 (0Ch+ n * 8) 字节以容纳 DVSEC 中包含的寄存器，其中 n 是此能力描述的寄存器块数。DVSEC ID 必须设置为 0008h，以表明这是 CXL Register Locator DVSEC 能力结构。</td></tr>
</tbody>
</table>

> **Figure 8-6.** Register Locator DVSEC with 3 Register Block Entries ｜ 包含 3 个寄存器块条目的 Register Locator DVSEC
>
> <img src="figures/chapter_08/fig_0527_1.png" alt="Figure 8-6" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0527.png)

> **Table 8-31.** Register Locator DVSEC - Header ｜ Register Locator DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 0h |
> | | 31:20 | DVSEC Length | varies |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0008h |

#### 8.1.9.1 Register Offset Low (Offset: Varies) | 寄存器偏移低 (偏移：可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This register reports the BAR Indicator Register (BIR), the Register Block Identifier, and the lower address bits of the BAR offset associated with the Register Block.</td><td style="background-color:#e8e8e8">此寄存器上报 BAR Indicator Register (BIR)、Register Block Identifier 以及与寄存器块关联的 BAR 偏移的低地址位。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 2:0 | HwInit | **Register BIR**: Indicates which one of a Function's BARs, located beginning at Offset 10h in Configuration Space, or entry in the Enhanced Allocation capability with a matching BAR Equivalent Indicator (BEI), is used to map the CXL registers into Memory Space.<br/>Defined encodings are:<br/>• 000b = Base Address Register 10h<br/>• 001b = Base Address Register 14h<br/>• 010b = Base Address Register 18h<br/>• 011b = Base Address Register 1Ch<br/>• 100b = Base Address Register 20h<br/>• 101b = Base Address Register 24h<br/>• All other encodings are reserved<br/>The Register block must be contained within the specified BAR. The specified BAR must be associated with the Function that implements the Register Locator DVSEC.<br/>For a 64-bit BAR, the Register BIR indicates the lower DWORD. — 指示功能从配置空间偏移 10h 开始的 BAR 中的哪一个，或 Enhanced Allocation 能力中与 BAR Equivalent Indicator (BEI) 匹配的条目，用于将 CXL 寄存器映射到内存空间。<br/>已定义的编码：<br/>• 000b = 基址寄存器 10h<br/>• 001b = 基址寄存器 14h<br/>• 010b = 基址寄存器 18h<br/>• 011b = 基址寄存器 1Ch<br/>• 100b = 基址寄存器 20h<br/>• 101b = 基址寄存器 24h<br/>• 所有其他编码保留<br/>寄存器块必须包含在指定的 BAR 内。指定的 BAR 必须与实现 Register Locator DVSEC 的功能关联。<br/>对于 64 位 BAR，Register BIR 指示低 DWORD。 |
> | 7:3 | RsvdP | Reserved — 保留 |
> | 15:8 | HwInit | **Register Block Identifier**: Identifies the type of CXL registers.<br/>Defined encodings are:<br/>• 00h = Indicates the register block entry is empty and the Register BIR, Register Block Offset Low, and Register Block Offset High fields are invalid.<br/>• 01h = Component Registers. The format of the Component Register block is defined in Section 8.2.3.<br/>• 02h = BAR Virtualization ACL Registers. The format of the BAR Virtualization ACL Register Block is defined in Section 8.2.6.<br/>• 03h = CXL Device Registers. The format of the CXL Device Register block is defined in Section 8.2.9.<br/>• 04h = CPMU Registers. More than one instance per Register Locator DVSEC instance is permitted. The CPMU Register format is defined in Section 8.2.7.<br/>• 05h = CHMU Registers. More than one instance per Register Locator DVSEC instance is permitted. The CHMU Register format is defined in Section 8.2.8.<br/>• FFh = Designated Vendor Specific Registers. The format of the designated vendor specific register block starts with the header defined in Table 8-10.<br/>• All other encodings are reserved. — 标识 CXL 寄存器的类型。<br/>已定义的编码：<br/>• 00h = 表示寄存器块条目为空，Register BIR、Register Block Offset Low 和 Register Block Offset High 字段无效。<br/>• 01h = Component Registers。组件寄存器块的格式在 8.2.3 节定义。<br/>• 02h = BAR Virtualization ACL Registers。BAR Virtualization ACL 寄存器块的格式在 8.2.6 节定义。<br/>• 03h = CXL Device Registers。CXL Device 寄存器块的格式在 8.2.9 节定义。<br/>• 04h = CPMU Registers。每个 Register Locator DVSEC 实例允许多个实例。CPMU 寄存器格式在 8.2.7 节定义。<br/>• 05h = CHMU Registers。每个 Register Locator DVSEC 实例允许多个实例。CHMU 寄存器格式在 8.2.8 节定义。<br/>• FFh = Designated Vendor Specific Registers。指定厂商特定寄存器块的格式以表 8-10 定义的 Header 开始。<br/>• 所有其他编码保留。 |
> | 31:16 | HwInit | **Register Block Offset Low**: A[31:16] byte offset from the starting address of the Function's BAR associated with the Register BIR field to point to the base of the Register Block. Register Block Offset is 64-KB aligned. Hence A[15:0] is 0000h. — 从与 Register BIR 字段关联的功能 BAR 起始地址开始的 A[31:16] 字节偏移，指向寄存器块基址。寄存器块偏移按 64-KB 对齐。因此 A[15:0] 为 0000h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

#### 8.1.9.2 Register Offset High (Offset: Varies) | 寄存器偏移高 (偏移：可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This register reports the higher address bits of the BAR offset associated with the Register Block. Zeroed if the register block entry in the Register Locator DVSEC is empty.</td><td style="background-color:#e8e8e8">此寄存器上报与寄存器块关联的 BAR 偏移的高地址位。如果 Register Locator DVSEC 中的寄存器块条目为空，则清零。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 31:0 | HwInit | **Register Block Offset High**: A[63:32] byte offset from the starting address of the Function's BAR associated with the Register BIR field to point to the base of the Register Block. — 从与 Register BIR 字段关联的功能 BAR 起始地址开始的 A[63:32] 字节偏移，指向寄存器块基址。 |

> **Table 8-32.** Designated Vendor Specific Register Block Header ｜ 指定厂商特定寄存器块 Header
>
> | Offset | Bit Location | Attributes | Description / 描述 |
> |---|---|---|---|
> | 00h | 15:0 | RO | **Vendor ID**: The PCI-SIG assigned Vendor ID for the organization that defined the layout and controls the specification for this register block. — 由 PCI-SIG 分配给定义此寄存器块布局并控制其规范的组织 Vendor ID。 |
> | | 31:16 | RO | **Vendor Register Block ID**: Value defined by the Vendor ID in bits 15:0 that indicates the nature and format of the vendor specific registers. — 由 bit 15:0 中的 Vendor ID 定义的值，指示厂商特定寄存器的性质和格式。 |
> | | 35:32 | RO | **Vendor Register Block Revision**: Version number defined by the Vendor ID in bits 15:0 that indicates the version of the register block. — 由 bit 15:0 中的 Vendor ID 定义的版本号，指示寄存器块的版本。 |
> | | 63:36 | RsvdP | Reserved — 保留 |
> | 08h | 31:0 | RO | **Vendor Register Block Length**: The number of bytes in the register block, including the Designated Vendor Specific Register Block Header and the vendor specific registers. — 寄存器块中的字节数，包括 Designated Vendor Specific Register Block Header 和厂商特定寄存器。 |
> | | 63:32 | RsvdP | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-10"></a>
## 8.1.10 MLD DVSEC | MLD DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The MLD DVSEC (see Figure 8-7) applies only to FM-owned LDs and must not be implemented by any other functions. See Table 8-2 for the complete listing.</td><td style="background-color:#e8e8e8">MLD DVSEC (见图 8-7) 仅适用于 FM 拥有的 LD，不得由任何其他功能实现。完整列表请参见表 8-2。</td></tr>
<tr><td>To advertise this capability, the standard DVSEC register fields must be set to the values shown in Table 8-11. The DVSEC Length field must be set to 010h bytes to accommodate the registers included in the DVSEC. The DVSEC ID must be set to 0009h to advertise that this is an MLD DVSEC capability structure.</td><td style="background-color:#e8e8e8">为了公布此能力，标准 DVSEC 寄存器字段必须设置为表 8-11 中所示的值。DVSEC Length 字段必须设置为 010h 字节以容纳 DVSEC 中包含的寄存器。DVSEC ID 必须设置为 0009h，以表明这是 MLD DVSEC 能力结构。</td></tr>
</tbody>
</table>

> **Figure 8-7.** MLD DVSEC ｜ MLD DVSEC
>
> <img src="figures/chapter_08/fig_0527_1.png" alt="Figure 8-7" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0527.png)

> **Table 8-33.** MLD DVSEC - Header ｜ MLD DVSEC – Header
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 0h |
> | | 31:20 | DVSEC Length | 010h |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0009h |

#### 8.1.10.1 Number of LD Supported (Offset 0Ah) | 支持的 LD 数量 (偏移 0Ah)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This register is used by an MLD to advertise the number of LDs supported.</td><td style="background-color:#e8e8e8">MLD 使用此寄存器公布支持的 LD 数量。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | HwInit | **Number of LDs Supported**: This field indicates the number of LDs (not counting FM-owned LDs) that are supported. An MLD must be associated with at least one LD. As such, 0000h is an illegal value for this field. Up to 16 LDs are supported; encodings greater than 16 are reserved. — 此字段指示支持的 LD 数量 (不包括 FM 拥有的 LD)。MLD 必须至少与一个 LD 关联。因此，0000h 是此字段的非法值。最多支持 16 个 LD；大于 16 的编码保留。 |

#### 8.1.10.2 LD-ID Hot Reset Vector (Offset 0Ch) | LD-ID 热复位向量 (偏移 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This register is used by the switch to trigger hot reset of the logical device or devices associated with LD-ID Hot Reset Vector bit positions that are set to a value of 1.</td><td style="background-color:#e8e8e8">交换器使用此寄存器对 LD-ID Hot Reset Vector 中位置 1 的位关联的逻辑设备触发热复位。</td></tr>
</tbody>
</table>

> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RW | **LD-ID Hot Reset Vector**: Each bit position in this vector represents an LD-ID. Up to 16 LD-IDs are supported. Setting any bit position to 1 triggers a hot reset of the associated logical device. Multiple bits can be set simultaneously to trigger hot reset of multiple logical devices. Read of this register returns a value of 0000h. — 此向量中的每个位位置代表一个 LD-ID。最多支持 16 个 LD-ID。将任何位位置置 1 都会触发关联逻辑设备的热复位。可以同时设置多个位以触发多个逻辑设备的热复位。读取此寄存器返回 0000h。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-11"></a>
## 8.1.11 Table Access DOE | 表访问 DOE

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Coherent Device Attributes Table (CDAT) allows a device or a switch to expose its performance attributes such as latency and bandwidth characteristics and other attributes of the device or the switch. A CXL Upstream Switch Port or Function 0 of a CXL device may implement Table Access DOE capability, which can be used to read out CDAT, one entry at a time. See Table 8-3 for the complete listing.</td><td style="background-color:#e8e8e8">Coherent Device Attributes Table (CDAT) 允许设备或交换器公开其性能属性，例如延迟和带宽特性以及设备或交换器的其他属性。CXL 上行交换端口或 CXL 设备的功能 0 可以实现 Table Access DOE 能力，可用于一次读取 CDAT 一条目。完整列表请参见表 8-3。</td></tr>
<tr><td>A device may interrupt the host when CDAT content changes using the MSI associated with this DOE Capability instance. A device may share the instance of this DOE mailbox with other Data Objects.</td><td style="background-color:#e8e8e8">当 CDAT 内容更改时，设备可以使用与此 DOE 能力实例关联的 MSI 中断主机。设备可以将此 DOE 邮箱的实例与其他数据对象共享。</td></tr>
<tr><td>This type of Data Object is identified as shown below. The Vendor ID must be set to the CXL Vendor ID to indicate that this Object Type is defined by the CXL specification. The Data Object Type must be set to 02h to advertise that this is a Table Access type of data object.</td><td style="background-color:#e8e8e8">此类数据对象的标识如下所示。Vendor ID 必须设置为 CXL Vendor ID，以表明此对象类型由 CXL 规范定义。Data Object Type 必须设置为 02h，以表明这是 Table Access 类型的数据对象。</td></tr>
</tbody>
</table>

> **Table 8-34.** Coherent Device Attributes - Data Object Header ｜ Coherent Device Attributes – 数据对象 Header
>
> | Bit Location | Field | Value |
> |---|---|---|
> | 15:0 | Vendor ID | 1E98h |
> | 23:16 | Data Object Type | 02h |

#### 8.1.11.1 Read Entry | 读条目

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Read the specified entry from the specified table within the device or the switch. For CXL, the table type is always CDAT. If the HDM_Count field in DVSEC CXL Capability is 01b, CDAT content is valid only when the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low (see Section 8.1.3.8.2) is 1. If the HDM_Count field in DVSEC CXL Capability is 10b, CDAT content is valid only when Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low and DVSEC CXL Range 2 Size Low (see Section 8.1.3.8.6) are both 1.</td><td style="background-color:#e8e8e8">从设备或交换器内的指定表读取指定条目。对于 CXL，表类型始终为 CDAT。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 01b，则仅当 DVSEC CXL Range 1 Size Low (见 8.1.3.8.2 节) 中的 Memory_Info_Valid 标志为 1 时，CDAT 内容才有效。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 10b，则仅当 DVSEC CXL Range 1 Size Low 和 DVSEC CXL Range 2 Size Low (见 8.1.3.8.6 节) 中的 Memory_Info_Valid 标志都为 1 时，CDAT 内容才有效。</td></tr>
</tbody>
</table>

> **Table 8-35.** Read Entry Request ｜ 读条目请求
>
> | Data Object Byte Location | Length in Bytes | Description / 描述 |
> |---|---|---|
> | 00h | 8 | **Standard DOE Request Header**: See PCIe Base Specification. — 标准 DOE 请求 Header：参见 PCIe 基础规范。 |
> | 08h | 1 | **Table Access Request Code**: 0 to indicate this is a request to read an entry.<br/>All other values are reserved. — 表访问请求代码：0 表示这是读取条目的请求。<br/>所有其他值保留。 |
> | 09h | 1 | **Table Type**<br/>• 0 = CDAT<br/>• All other types are reserved — 表类型<br/>• 0 = CDAT<br/>• 所有其他类型保留 |
> | 0Ah | 2 | **EntryHandle**: Handle value associated with the entry being requested. For Table Type = 0, EntryHandle = 0 specifies that the request is for the CDAT header and EntryHandle>0 indicates the request is for the CDAT Structure[EntryHandle - 1]. — 与所请求条目关联的句柄值。对于 Table Type = 0，EntryHandle = 0 指定请求的是 CDAT 头，EntryHandle>0 表示请求的是 CDAT Structure[EntryHandle - 1]。 |

> **Table 8-36.** Read Entry Response ｜ 读条目响应
>
> | Data Object Byte Location | Length in Bytes | Description / 描述 |
> |---|---|---|
> | 00h | 8 | **Standard DOE Request Header**: See PCIe Base Specification. — 标准 DOE 请求 Header：参见 PCIe 基础规范。 |
> | 08h | 1 | **Table Access Response Code**: 0 to indicate this is a response to read entry request — 表访问响应代码：0 表示这是读取条目请求的响应 |
> | 09h | 1 | **Table Type**:<br/>• 0 = CDAT<br/>• All other types are reserved<br/>Shall match the input supplied during the matching Read Entry Request. — 表类型：<br/>• 0 = CDAT<br/>• 所有其他类型保留<br/>必须与匹配的读取条目请求期间提供的输入匹配。 |
> | 0Ah | 2 | **EntryHandle**: EntryHandle value associated with the next entry in the Table. EntryHandle=FFFFh represents the last entry in the table and thus the end of the table. — 与表中下一条目关联的 EntryHandle 值。EntryHandle=FFFFh 表示表中的最后一个条目，因此是表的末尾。 |
> | 0Ch | Variable | **The table entry that corresponds to the EntryHandle field in the Read Entry Request (see Table 8-13).** — 对应于 Read Entry Request (见表 8-13) 中 EntryHandle 字段的表条目。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-12"></a>
## 8.1.12 Memory Device Configuration Space Layout | 内存设备配置空间布局

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section defines the Configuration Space registers required for CXL memory devices to advertise support for the memory device capabilities (see Section 8.2.9.5) and memory device command sets (see Section 8.2.10.9).</td><td style="background-color:#e8e8e8">本节定义了 CXL 内存设备为了公布其对内存设备能力 (见 8.2.9.5 节) 和内存设备命令集 (见 8.2.10.9 节) 的支持所需的配置空间寄存器。</td></tr>
</tbody>
</table>

#### 8.1.12.1 PCIe Configuration Space Header - Class Code Register (Offset 09h) | PCIe 配置空间 Header – Class Code 寄存器 (偏移 09h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The PCIe Configuration Space Header, Class Code register (Offset 09h) shall be implemented as follows, indicating the Function is a "CXL Memory Device following the CXL 2.0 or later specification". Such a CXL device shall advertise a Register Locator DVSEC entry with Register Block Identifier=03h.</td><td style="background-color:#e8e8e8">PCIe 配置空间 Header、Class Code 寄存器 (偏移 09h) 应按如下方式实现，表明此功能是 "遵循 CXL 2.0 或更高规范的 CXL 内存设备"。此类 CXL 设备应公布一个 Register Block Identifier=03h 的 Register Locator DVSEC 条目。</td></tr>
</tbody>
</table>

> **Table 8-37.** PCIe Configuration Space Header - Class Code Register (Offset 09h) for CXL Memory Device ｜ CXL 内存设备的 PCIe 配置空间 Header – Class Code 寄存器 (偏移 09h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 7:0 | RO | **Programming Interface (PI)**: Shall be set to 10h. — 应设置为 10h。 |
> | 15:8 | RO | **Sub Class Code (SCC)**: Indicates the sub class code as CXL memory device. Shall be set to 02h. — 指示子类别代码为 CXL 内存设备。应设置为 02h。 |
> | 23:16 | RO | **Base Class Code (BCC)**: Indicates the base class code as a memory controller. Shall be set to 05h. — 指示基类代码为内存控制器。应设置为 05h。 |

#### 8.1.12.2 Memory Device PCIe Capabilities and Extended Capabilities | 内存设备的 PCIe 能力与扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The optional PCIe capabilities described in this section are required for a CXL memory device that implements the Class Code specified in Section 8.1.12.1. See PCIe Base Specification for definitions of the associated registers.</td><td style="background-color:#e8e8e8">实现 8.1.12.1 节规定的 Class Code 的 CXL 内存设备需要本节中描述的可选 PCIe 能力。相关寄存器的定义请参见 PCIe 基础规范。</td></tr>
</tbody>
</table>

> **Table 8-38.** Memory Device PCIe Capabilities and Extended Capabilities ｜ 内存设备 PCIe 能力与扩展能力
>
> | PCIe Capabilities and Extended Capabilities | Exceptions | Notes |
> |---|---|---|
> | Device Serial Number Extended Capability | Uniquely identifies the CXL memory device. | 唯一标识 CXL 内存设备。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-1-13"></a>
## 8.1.13 FM Mailbox CCI Configuration Space Layout | FM 邮箱 CCI 配置空间布局

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section defines the Configuration Space registers that are required for FM Mailbox CCI (see Section 8.2.9.6) and FM API command sets (see Section 8.2.10.9).</td><td style="background-color:#e8e8e8">本节定义了 FM Mailbox CCI (见 8.2.9.6 节) 和 FM API 命令集 (见 8.2.10.9 节) 所需的配置空间寄存器。</td></tr>
</tbody>
</table>

#### 8.1.13.1 PCIe Configuration Space Header - Class Code Register (Offset 09h) | PCIe 配置空间 Header – Class Code 寄存器 (偏移 09h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>To advertise FM Mailbox CCI support, the PCIe Configuration Space Header, Class Code register (Offset 09h) shall be implemented as indicated in Table 8-16, indicating the Function is a "CXL Fabric Management Host Interface controller". Such a CXL Function shall advertise a Register Locator DVSEC entry with Register Block Identifier=03h.</td><td style="background-color:#e8e8e8">为了公布 FM Mailbox CCI 支持，PCIe 配置空间 Header、Class Code 寄存器 (偏移 09h) 应按表 8-16 所示实现，表明此功能是 "CXL Fabric Management Host Interface 控制器"。此类 CXL 功能应公布一个 Register Block Identifier=03h 的 Register Locator DVSEC 条目。</td></tr>
</tbody>
</table>

> **Table 8-39.** PCIe Configuration Space Header - Class Code Register (Offset 09h) for FM Mailbox CCI ｜ FM Mailbox CCI 的 PCIe 配置空间 Header – Class Code 寄存器 (偏移 09h)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 7:0 | RO | **Programming Interface (PI)**: Shall be cleared to 00h. — 应清零为 00h。 |
> | 15:8 | RO | **Sub Class Code (SCC)**: Shall be set to 0Bh. — 应设置为 0Bh。 |
> | 23:16 | RO | **Base Class Code (BCC)**: Shall be set to 0Ch. — 应设置为 0Ch。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2"></a>
## 8.2 Memory Mapped Registers | 内存映射寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL memory mapped registers are located in six general regions as specified in Table 8-17. Notably, the RCH Downstream Port and RCD Upstream Port are not discoverable through PCIe Configuration Space. Instead, the RCH Downstream and RCD Upstream Port registers are implemented using PCIe Root Complex register blocks (RCRBs). Additionally, the RCH Downstream Ports and RCD Upstream Ports each implement an MEMBAR0 region (also known as Component registers) to host registers for configuring the CXL subsystem components associated with the respective Port. MEMBAR0 register (Figure 8-9) holds the address of Component registers.</td><td style="background-color:#e8e8e8">CXL 内存映射寄存器位于表 8-17 中指定的六个常规区域中。值得注意的是，RCH 下行端口和 RCD 上行端口不能通过 PCIe 配置空间发现。相反，RCH 下行和 RCD 上行端口寄存器使用 PCIe 根复合体寄存器块 (RCRB) 实现。此外，RCH 下行端口和 RCD 上行端口各自实现一个 MEMBAR0 区域 (也称为 Component 寄存器) 来托管用于配置与各自端口关联的 CXL 子系统组件的寄存器。MEMBAR0 寄存器 (图 8-9) 保存 Component 寄存器的地址。</td></tr>
<tr><td>The RCH Downstream Port and RCD Upstream Port memory mapped register regions appear in memory space as shown in Figure 8-8. Note that the RCRBs do not overlap with the MEMBAR0 regions. Also, note that the RCD Upstream Port's MEMBAR0 region must fall within the range specified by the RCH Downstream Port's memory base and limit register. As long as these requirements are satisfied, the details of how the RCRBs are mapped into memory space are implementation specific.</td><td style="background-color:#e8e8e8">RCH 下行端口和 RCD 上行端口的内存映射寄存器区域在内存空间中如图 8-8 所示。注意，RCRB 不与 MEMBAR0 区域重叠。另请注意，RCD 上行端口的 MEMBAR0 区域必须位于 RCH 下行端口的内存基址和限值寄存器指定的范围内。只要满足这些要求，RCRB 映射到内存空间的具体细节由实现决定。</td></tr>
<tr><td>Software shall use CXL.io Memory Read and Write to access memory mapped register defined in this section. Unless specified otherwise, software shall restrict the accesses width based on the following:</td><td style="background-color:#e8e8e8">软件应使用 CXL.io 内存读和写来访问本节定义的内存映射寄存器。除非另有规定，软件应根据以下规则限制访问宽度：</td></tr>
<tr><td>• A 32-bit register shall be accessed as a 1-byte, 2-byte, or 4-byte quantity.</td><td style="background-color:#e8e8e8">• 32 位寄存器应作为 1 字节、2 字节或 4 字节量访问。</td></tr>
<tr><td>• A 64-bit register shall be accessed as a 1-byte, 2-byte, 4-byte, or 8-byte quantity.</td><td style="background-color:#e8e8e8">• 64 位寄存器应作为 1 字节、2 字节、4 字节或 8 字节量访问。</td></tr>
<tr><td>• The address shall be a multiple of the access width (e.g., when accessing a register as a 4-byte quantity, the address shall be a multiple of 4).</td><td style="background-color:#e8e8e8">• 地址应是访问宽度的倍数 (例如，作为 4 字节量访问寄存器时，地址应是 4 的倍数)。</td></tr>
<tr><td>• The accesses shall map to contiguous bytes.</td><td style="background-color:#e8e8e8">• 访问应映射到连续字节。</td></tr>
<tr><td>If these rules are not followed, the behavior is undefined.</td><td style="background-color:#e8e8e8">如果不遵循这些规则，则行为未定义。</td></tr>
</tbody>
</table>

> **Table 8-40.** CXL Memory Mapped Register Regions ｜ CXL 内存映射寄存器区域
>
> | Memory Mapped Region | Description | Location |
> |---|---|---|
> | RCH Downstream Port RCRB | This is a 4-KB region with registers based upon PCIe defined registers for a root port with deltas listed in this chapter. Includes registers from PCIe Type 1 Config Header and PCIe capabilities and extended capabilities. | This is a contiguous 4-KB memory region relocatable via an implementation specific mechanism. This region is located outside the Downstream Port's MEMBAR0 region.<br/>Note: The combined Downstream and Upstream Port RCRBs are a contiguous 8-KB region. — 这是一个 4-KB 区域，其寄存器基于本章列出的根端口的 PCIe 定义寄存器。包括来自 PCIe Type 1 Config Header 和 PCIe 能力与扩展能力的寄存器。这是一个连续的 4-KB 内存区域，可通过实现特定机制重定位。该区域位于下行端口 MEMBAR0 区域之外。<br/>注意：合并的下行和上行端口 RCRB 是连续的 8-KB 区域。 |
> | RCD Upstream Port RCRB | This is a 4-KB region with registers based upon PCIe defined registers for an Upstream Port with deltas listed in this chapter. Includes 64B Config Header and PCIe capabilities and extended capabilities. | This is a contiguous 4-KB memory region relocatable via an implementation specific mechanism. This region is located outside the Upstream Port's MEMBAR0 region. This region may be located within the range specified by the Downstream Port's memory base/limit registers, but that is not a requirement.<br/>Note: The combined Downstream and Upstream Port RCRBs are a contiguous 8-KB region. The RCD Upstream Port captures the base of its RCRB from the Address field of the first MMIO Read (MRd) request received after the Conventional Reset. — 这是一个 4-KB 区域，其寄存器基于本章列出的上行端口的 PCIe 定义寄存器。包括 64B Config Header 和 PCIe 能力与扩展能力。这是一个连续的 4-KB 内存区域，可通过实现特定机制重定位。该区域位于上行端口 MEMBAR0 区域之外。此区域可位于下行端口的内存基址/限值寄存器指定的范围内，但这不是必需的。<br/>注意：合并的下行和上行端口 RCRB 是连续的 8-KB 区域。RCD 上行端口从 Conventional Reset 之后接收到的第一个 MMIO Read (MRd) 请求的 Address 字段中获取其 RCRB 的基址。 |
> | RCH Downstream Port Component Registers | This memory region hosts registers that allow software to configure CXL Downstream Port subsystem components, such as the CXL protocol, link, and physical layers and the CXL ARB/MUX. | The location of this region is specified by a 64-bit MEMBAR0 register located at Offsets 10h and 14h of the Downstream Port's RCRB. — 此内存区域托管允许软件配置 CXL 下行端口子系统组件 (例如 CXL 协议、链路和物理层以及 CXL ARB/MUX) 的寄存器。该区域的位置由位于下行端口 RCRB 偏移 10h 和 14h 处的 64 位 MEMBAR0 寄存器指定。 |
> | RCD Upstream Port Component Registers | This memory region hosts registers that allow software to configure CXL Upstream Port subsystem components, such as CXL protocol, link, and physical layers and the CXL ARB/MUX. | The location of this region is specified by a 64-bit MEMBAR0 register located at Offsets 10h and 14h of the Upstream Port's RCRB. This region is located within the range specified by the Downstream Port's memory base/limit registers. — 此内存区域托管允许软件配置 CXL 上行端口子系统组件 (例如 CXL 协议、链路和物理层以及 CXL ARB/MUX) 的寄存器。该区域的位置由位于上行端口 RCRB 偏移 10h 和 14h 处的 64 位 MEMBAR0 寄存器指定。该区域位于下行端口内存基址/限值寄存器指定的范围内。 |
> | Component Registers for All Other CXL Components | This memory region hosts registers that allow software to configure CXL Port subsystem components, such as CXL protocol, link, and physical layers and the CXL ARB/MUX. These are located in CXL root ports, CXL DSPs, CXL USPs, and CXL devices that do not have a CXL RCRB. | The CXL Port specific component registers are mapped in memory space allocated via a standard PCIe BAR associated with the appropriate PCIe non-virtual Function. Register Locator DVSEC structure (see Section 8.1.9) describes the BAR number and the offset within the BAR where these registers are mapped. — 此内存区域托管允许软件配置 CXL 端口子系统组件 (例如 CXL 协议、链路和物理层以及 CXL ARB/MUX) 的寄存器。它们位于 CXL 根端口、CXL DSP、CXL USP 以及没有 CXL RCRB 的 CXL 设备中。特定于 CXL 端口的组件寄存器映射到通过与适当 PCIe 非虚拟功能关联的标准 PCIe BAR 分配的内存空间中。Register Locator DVSEC 结构 (见 8.1.9 节) 描述了映射这些寄存器的 BAR 号和 BAR 内的偏移。 |
> | CXL CHBCR (CXL Host Bridge Component Registers) | This memory region hosts registers that allow software to configure CXL functionality that affects multiple root ports such as Memory Interleaving. | These registers are mapped in memory space, but the base address is discovered via ACPI CEDT (see Section 9.18.1). — 此内存区域托管允许软件配置影响多个根端口的 CXL 功能 (例如内存交织) 的寄存器。这些寄存器映射到内存空间，但基址通过 ACPI CEDT (见 9.18.1 节) 发现。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-1"></a>
## 8.2.1 RCD Upstream Port and RCH Downstream Port Registers | RCD 上行端口和 RCH 下行端口寄存器

#### 8.2.1.1 RCH Downstream Port RCRB | RCH 下行端口 RCRB

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The RCH Downstream Port RCRB is a 4-KB memory region that contains registers based upon the PCIe-defined registers for a root port. Figure 8-9 illustrates the layout of the CXL RCRB for a Downstream Port. With the exception of the first DWORD, the first 64 bytes of the RCH Downstream Port RCRB implement the registers from a PCIe Type 1 Configuration Header. The first DWORD of the RCRB contains a NULL Extended Capability ID with a Version of 0h and a Next Capability Offset pointer. A 64-bit MEMBAR0 is implemented at Offsets 10h and 14h; this points to a private memory region that hosts registers for configuring Downstream Port subsystem components as specified in Table 8-17. The supported PCIe capabilities and extended capabilities are discovered by following the linked lists of pointers. Supported PCIe capabilities are mapped into the offset range from 040h to 0FFh. Supported PCIe extended capabilities are mapped into the offset range from 100h to FFFh. The RCH Downstream Port supported PCIe capabilities and extended capabilities are listed in Table 8-18; please refer to PCIe Base Specification for definitions of the associated registers.</td><td style="background-color:#e8e8e8">RCH 下行端口 RCRB 是一个 4-KB 内存区域，包含基于根端口的 PCIe 定义寄存器。图 8-9 展示了下行端口的 CXL RCRB 布局。除第一个 DWORD 外，RCH 下行端口 RCRB 的前 64 字节实现 PCIe Type 1 Configuration Header 中的寄存器。RCRB 的第一个 DWORD 包含一个 NULL Extended Capability ID，Version 为 0h，并带有一个 Next Capability Offset 指针。在偏移 10h 和 14h 处实现 64 位 MEMBAR0；它指向一个私有内存区域，该区域托管用于配置下行端口子系统组件的寄存器 (如 表 8-17 所规定)。支持的 PCIe 能力和扩展能力通过跟踪指针链表来发现。受支持的 PCIe 能力映射到偏移范围 040h 至 0FFh。受支持的 PCIe 扩展能力映射到偏移范围 100h 至 FFFh。RCH 下行端口支持的 PCIe 能力和扩展能力在表 8-18 中列出；相关寄存器的定义请参见 PCIe 基础规范。</td></tr>
</tbody>
</table>

> **Figure 8-8.** RCD and RCH Memory Mapped Register Regions ｜ RCD 和 RCH 内存映射寄存器区域
>
> <img src="figures/chapter_08/fig_0532_1.png" alt="Figure 8-8" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0532.png)

> **Figure 8-9.** RCH Downstream Port RCRB ｜ RCH 下行端口 RCRB
>
> <img src="figures/chapter_08/fig_0533_1.jpx" alt="Figure 8-9" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0533.png)

> **Table 8-41.** RCH Downstream Port PCIe Capabilities and Extended Capabilities (Sheet 1 of 2) ｜ RCH 下行端口 PCIe 能力与扩展能力 (第 1 页/共 2 页)
>
> | PCIe Capabilities and Extended Capabilities | Exceptions¹ | Notes |
> |---|---|---|
> | PCIe Capability | Slot Capabilities, Slot Control, Slot Status, Slot Capabilities 2, Slot Control 2, and Slot Status 2 registers are not applicable. | N/A |
> | PCI Power Management Capability | N/A. Software should ignore. | N/A |
> | MSI Capability | N/A. Software should ignore. | N/A |
> | Advanced Error Reporting Extended Capability | N/A. Software should ignore. | Required for CXL device despite being optional for PCIe. Downstream Port is required to forward ERR_ messages. — 尽管对 PCIe 是可选的，CXL 设备需要此能力。下行端口需要转发 ERR_ 消息。 |
> | ACS Extended Capability | None | N/A |
> | Multicast Extended Capability | N/A. Software should ignore. | N/A |
> | Downstream Port Containment Extended Capability | Use with care. DPC trigger will bring down physical link, reset device state, disrupt CXL.cache and CXL.mem traffic. | N/A |
> | Designated Vendor-Specific Extended Capability (DVSEC) | None | See Section 8.2.1.3 for Flex Bus Port DVSEC definition. |
> | Secondary PCIe Extended Capability | None | None |
> | Data Link Feature Extended Capability | None | None |
> | Physical Layer 16.0 GT/s Extended Capability | None | None |
> | Physical Layer 32.0 GT/s Extended Capability | None | None |
> | Lane Margining at the Receiver Extended Capability | None | None |
> | Alternate Protocol Extended Capability | None | None |
>
> 1. It is the responsibility of software to be aware of the registers within the capabilities that are not applicable in CXL mode in case designs choose to use a common code base for PCIe mode and CXL mode.

#### 8.2.1.2 RCD Upstream Port RCRB | RCD 上行端口 RCRB

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The RCD Upstream Port RCRB is a 4-KB memory region that contains registers based upon the PCIe Base Specification-defined registers. The Upstream Port captures the upper address bits [63:12] of the first memory read received after link initialization as the base address for the Upstream Port RCRB. Figure 8-10 illustrates the layout of the RCRB for an RCD Upstream Port. With the exception of the first DWORD, the first 64 bytes of the RCD Upstream Port RCRB implement the registers from a PCIe Type 0 Configuration Header. The first DWORD of the RCRB contains a NULL Extended Capability ID with a Version of 0h and a Next Capability Offset pointer. A 64-bit BAR (labeled MEMBAR0) is implemented at Offsets 10h and 14h; this points to a memory region that hosts registers for configuring the Upstream Port subsystem CXL.mem as specified in Table 8-17. The supported PCIe capabilities and extended capabilities are discovered by following the linked lists of pointers. Supported PCIe capabilities are mapped into the offset range from 040h to 0FFh. Supported PCIe extended capabilities are mapped into the offset range from 100h to FFFh. The CXL Upstream Port-supported PCIe capabilities and extended capabilities are listed in Table 8-19; see PCIe Base Specification for definitions of the associated registers.</td><td style="background-color:#e8e8e8">RCD 上行端口 RCRB 是一个 4-KB 内存区域，包含基于 PCIe 基础规范定义寄存器集。上行端口将链路初始化后接收到的第一个内存读的高位地址 [63:12] 作为上行端口 RCRB 的基址。图 8-10 展示了 RCD 上行端口的 RCRB 布局。除第一个 DWORD 外，RCD 上行端口 RCRB 的前 64 字节实现 PCIe Type 0 Configuration Header 中的寄存器。RCRB 的第一个 DWORD 包含一个 NULL Extended Capability ID，Version 为 0h，并带有一个 Next Capability Offset 指针。在偏移 10h 和 14h 处实现 64 位 BAR (标记为 MEMBAR0)；它指向一个内存区域，该区域托管用于配置上行端口子系统 CXL.mem 的寄存器 (如 表 8-17 所规定)。支持的 PCIe 能力和扩展能力通过跟踪指针链表来发现。受支持的 PCIe 能力映射到偏移范围 040h 至 0FFh。受支持的 PCIe 扩展能力映射到偏移范围 100h 至 FFFh。CXL 上行端口支持的 PCIe 能力和扩展能力在表 8-19 中列出；相关寄存器的定义请参见 PCIe 基础规范。</td></tr>
<tr><td>The following standard registers that are part of the PCIe Type 0 header definition are considered reserved and have no effect on the behavior of an RCD Upstream Port:</td><td style="background-color:#e8e8e8">作为 PCIe Type 0 Header 定义一部分的以下标准寄存器被视为保留，并且对 RCD 上行端口的行为没有影响：</td></tr>
<tr><td>• Command register (Offset 04h)</td><td style="background-color:#e8e8e8">• Command 寄存器 (偏移 04h)</td></tr>
<tr><td>• Status register (Offset 06h)</td><td style="background-color:#e8e8e8">• Status 寄存器 (偏移 06h)</td></tr>
<tr><td>Per PCIe Base Specification, the following registers in the PCIe Capability are marked reserved for an RCiEP and shall not be implemented by the Device 0, Function 0 of the RCD:</td><td style="background-color:#e8e8e8">根据 PCIe 基础规范，PCIe 能力中的以下寄存器对于 RCiEP 标记为保留，RCD 的设备 0、功能 0 不应实现：</td></tr>
<tr><td>• Link Registers - Link Capabilities, Link Control, Link Status, Link Capabilities 2, Link Control 2, and Link Status 2</td><td style="background-color:#e8e8e8">• Link 寄存器 - Link Capabilities、Link Control、Link Status、Link Capabilities 2、Link Control 2 和 Link Status 2</td></tr>
<tr><td>• Slot Registers - Slot Capabilities, Slot Control, Slot Status, Slot Capabilities 2, Slot Control 2, and Slot Status 2</td><td style="background-color:#e8e8e8">• Slot 寄存器 - Slot Capabilities、Slot Control、Slot Status、Slot Capabilities 2、Slot Control 2 和 Slot Status 2</td></tr>
<tr><td>• Root Port Registers - Root Capabilities, Root Control, and Root Status</td><td style="background-color:#e8e8e8">• Root Port 寄存器 - Root Capabilities、Root Control 和 Root Status</td></tr>
<tr><td>Software must reference the Link registers in the Upstream Port RCRB PCIe capability structure to discover the link capabilities and link status, and to configure the link properties. These registers shall follow the PCIe Base Specification definition of an Upstream Switch Port. Software must set the ASPM Control field in the Link Control register if it wishes to enable CXL.io L1.</td><td style="background-color:#e8e8e8">软件必须参考上行端口 RCRB PCIe 能力结构中的 Link 寄存器，以发现链路能力和链路状态，并配置链路属性。这些寄存器应遵循 PCIe 基础规范中关于上行交换端口的定义。如果软件希望启用 CXL.io L1，则必须设置 Link Control 寄存器中的 ASPM Control 字段。</td></tr>
<tr><td>All fields in the Upstream Port's Device Capabilities register, Device Control register, Device Status register, Device Capabilities 2 register, Device Control 2 register, and Device Status 2 register are reserved.</td><td style="background-color:#e8e8e8">上行端口的 Device Capabilities 寄存器、Device Control 寄存器、Device Status 寄存器、Device Capabilities 2 寄存器、Device Control 2 寄存器和 Device Status 2 寄存器中的所有字段均为保留。</td></tr>
<tr><td>The Device/Port Type, Slots Implemented and Interrupt Message Number fields in the Upstream Port's Capability register are reserved.</td><td style="background-color:#e8e8e8">上行端口 Capability 寄存器中的 Device/Port Type、Slots Implemented 和 Interrupt Message Number 字段均为保留。</td></tr>
</tbody>
</table>

> **Figure 8-10.** RCD Upstream Port RCRB ｜ RCD 上行端口 RCRB
>
> <img src="figures/chapter_08/fig_0535_1.jpx" alt="Figure 8-10" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0535.png)

> **Table 8-42.** RCD Upstream Port PCIe Capabilities and Extended Capabilities ｜ RCD 上行端口 PCIe 能力与扩展能力
>
> | PCIe Capabilities and Extended Capabilities | Exceptions¹ | Notes |
> |---|---|---|
> | PCIe Capability | See Section 8.2.1.2. | None |
> | Advanced Error Reporting Extended Capability | N/A. Software should ignore. | Required for CXL devices despite being optional for PCIe. Link/Protocol errors detected by Upstream Port are logged/reported via RCiEP. — 尽管对 PCIe 是可选的，CXL 设备需要此能力。上行端口检测到的链路/协议错误通过 RCiEP 记录/上报。 |
> | Virtual Channel Extended Capability | None | VC0 and VC1 |
> | Designated Vendor-Specific Extended Capability (DVSEC) | None | See Section 8.2.1.3 for Flex Bus Port DVSEC definition. |
> | Secondary PCIe Extended Capability | None | None |
> | Data Link Feature Extended Capability | None | None |
> | Physical Layer 16.0 GT/s Extended Capability | None | None |
> | Physical Layer 32.0 GT/s Extended Capability | None | None |
> | Lane Margining at the Receiver Extended Capability | None | None |
> | Alternate Protocol Extended Capability | None | None |
>
> 1. It is the responsibility of software to be aware of the registers within the capabilities that are not applicable in CXL mode in case designs choose to use a common code base for PCIe mode and CXL mode.
> 1. 如果设计选择对 PCIe 模式和 CXL 模式使用通用代码库，则软件有责任了解在 CXL 模式下不适用的能力内的寄存器。

#### 8.2.1.3 Flex Bus Port DVSEC | Flex Bus 端口 DVSEC

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>All CXL ports implement a Flex Bus Port DVSEC. This DVSEC is located in the RCRBs of the RCD Upstream Ports and RCH Downstream Ports. RCD and RCH ports may implement DVSEC Revision = 0, 1, or 2 of this DVSEC. See Table 8-2 for the complete listing.</td><td style="background-color:#e8e8e8">所有 CXL 端口都实现 Flex Bus Port DVSEC。此 DVSEC 位于 RCD 上行端口和 RCH 下行端口的 RCRB 中。RCD 和 RCH 端口可以实现此 DVSEC 的 DVSEC Revision = 0、1 或 2。完整列表请参见表 8-2。</td></tr>
<tr><td>This DVSEC is also located in the Configuration Space of CXL root ports, Upstream Switch Ports, Downstream Switch Port, and CXL device's primary function (Function 0) if the device does not implement CXL RCRB. A CXL component that is neither an RCD nor an RCH shall report DVSEC Revision greater than or equal to 1. Revision 2 introduces 3 new registers.</td><td style="background-color:#e8e8e8">如果设备未实现 CXL RCRB，则此 DVSEC 也位于 CXL 根端口、上行交换端口、下行交换端口和 CXL 设备主功能 (功能 0) 的配置空间中。既不是 RCD 也不是 RCH 的 CXL 组件应报告 DVSEC Revision 大于或等于 1。Revision 2 引入了 3 个新寄存器。</td></tr>
<tr><td>Figure 8-11 shows the layout of the Flex Bus Port DVSEC and Table 8-20 shows how the Header 1 and Header 2 registers shall be set. The following subsections give details of the registers defined in the Flex Bus Port DVSEC.</td><td style="background-color:#e8e8e8">图 8-11 展示了 Flex Bus Port DVSEC 的布局，表 8-20 展示了 Header 1 和 Header 2 寄存器应如何设置。以下小节详细介绍了 Flex Bus Port DVSEC 中定义的寄存器。</td></tr>
</tbody>
</table>

> **Figure 8-11.** PCIe DVSEC for Flex Bus Port ｜ Flex Bus 端口的 PCIe DVSEC
>
> <img src="figures/chapter_08/fig_0537_1.png" alt="Figure 8-11" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0537.png)

> **Table 8-43.** PCIe DVSEC Header Register Settings for Flex Bus Port ｜ Flex Bus 端口的 PCIe DVSEC Header 寄存器设置
>
> | Register | Bit Location | Field | Value |
> |---|---|---|---|
> | Designated Vendor-Specific Header 1 (Offset 04h) | 15:0 | DVSEC Vendor ID | 1E98h |
> | | 19:16 | DVSEC Revision | 2h |
> | | 31:20 | DVSEC Length | 020h |
> | Designated Vendor-Specific Header 2 (Offset 08h) | 15:0 | DVSEC ID | 0007h |

<a id="sec-8-2-1-3-1"></a>
##### 8.2.1.3.1 DVSEC Flex Bus Port Capability (Offset 0Ah) | DVSEC Flex Bus 端口能力 (偏移 0Ah)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>Note:</strong> The Mem_Capable, IO_Capable, and Cache_Capable fields are also present in the Flex Bus DVSEC for the device. This allows for future scalability where multiple devices, each with potentially different capabilities, may be populated behind a single Port.</td><td style="background-color:#e8e8e8"><strong>注意：</strong>Mem_Capable、IO_Capable 和 Cache_Capable 字段也出现在设备的 Flex Bus DVSEC 中。这允许未来扩展，使得在单个端口后面可以部署多个设备，每个设备可能具有不同的能力。</td></tr>
</tbody>
</table>

> **Table 8-44.** DVSEC Flex Bus Port Capability (Offset 0Ah) ｜ DVSEC Flex Bus 端口能力 (偏移 0Ah)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | HwInit | **Cache_Capable**: If set, indicates CXL.cache protocol support when operating in Flex Bus.CXL mode. This should be cleared to 0 for all LDs of an MLD. — 置 1 时，表示在 Flex Bus.CXL 模式下支持 CXL.cache 协议。MLD 的所有 LD 应清零为 0。 |
> | 1 | HwInit | **IO_Capable**: If set, indicates CXL.io protocol support when operating in Flex Bus.CXL mode. Must be 1. — 置 1 时，表示在 Flex Bus.CXL 模式下支持 CXL.io 协议。必须为 1。 |
> | 2 | HwInit | **Mem_Capable**: If set, indicates CXL.mem protocol support when operating in Flex Bus.CXL mode. This must be 1 for all LDs of an MLD. — 置 1 时，表示在 Flex Bus.CXL 模式下支持 CXL.mem 协议。MLD 的所有 LD 必须为 1。 |
> | 4:3 | RsvdP | Reserved — 保留 |
> | 5 | HwInit | **CXL 68B Flit and VH Capable**: Formerly known as CXL2p0_Capable. If set, indicates CXL VH functionality support with 68B flits is available when operating in Flex Bus.CXL mode. This must be 1 for all LDs of an MLD.¹ — 置 1 时，表示在 Flex Bus.CXL 模式下运行时支持 68B flit 的 CXL VH 功能。MLD 的所有 LD 必须为 1。¹ |
> | 6 | HwInit | **CXL_Multi-Logical_Device_Capable**: If set, indicates Multi-Logical Device support available when operating in Flex Bus.CXL mode. This bit must be cleared to 0 on CXL host Downstream Ports. The value must be the same for all LDs of an MLD.¹ — 置 1 时，表示在 Flex Bus.CXL 模式下运行时支持多逻辑设备。此位在 CXL host Downstream Ports 上必须清零为 0。MLD 的所有 LD 该值必须相同。¹ |
> | 12:7 | RsvdP | Reserved — 保留 |
> | 13 | HwInit | **CXL Latency_Optimized_256B_Flit_Capable**: If set, indicates support for latency-optimized 256B flits as described in Section 6.2.3.1.2 when operating in Flex Bus.CXL mode. The value must be the same for all LDs of an MLD.² — 置 1 时，表示在 Flex Bus.CXL 模式下运行时支持 6.2.3.1.2 节中描述的 latency-optimized 256B flit。MLD 的所有 LD 该值必须相同。² |
> | 14 | HwInit | **CXL PBR Flit Capable**: If set, indicates support for PBR flits as described in Table 6-11 when operating in Flex Bus.CXL mode.² — 置 1 时，表示在 Flex Bus.CXL 模式下运行时支持表 6-11 中描述的 PBR flit。² |
> | 15 | RsvdP | Reserved — 保留 |
>
> 1. Introduced as part of DVSEC Revision=1.
> 2. Introduced as part of DVSEC Revision=2.
> 1. 在 DVSEC Revision=1 中引入。
> 2. 在 DVSEC Revision=2 中引入。

<a id="sec-8-2-1-3-2"></a>
##### 8.2.1.3.2 DVSEC Flex Bus Port Control (Offset 0Ch) | DVSEC Flex Bus 端口控制 (偏移 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Flex Bus physical layer uses the values that software sets in this register as a starting point for alternate protocol negotiation as long as the corresponding bit in the Flex Bus Port Capability register is set. The Flex Bus physical layer shall sample the values in this register only during exit from the Detect LTSSM state; the physical layer shall ignore any changes to this register in all other LTSSM states.</td><td style="background-color:#e8e8e8">只要 Flex Bus Port Capability 寄存器中的相应位置 1，Flex Bus 物理层就会使用软件在此寄存器中设置的值作为备用协议协商的起点。Flex Bus 物理层仅在退出 Detect LTSSM 状态时才会采样此寄存器中的值；物理层在所有其他 LTSSM 状态中将忽略对此寄存器的任何更改。</td></tr>
</tbody>
</table>

> **Table 8-45.** DVSEC Flex Bus Port Control (Offset 0Ch) ｜ DVSEC Flex Bus 端口控制 (偏移 0Ch)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RW if Downstream Port; otherwise, HwInit | **Cache_Enable**: When set, enables CXL.cache protocol operation when in Flex Bus.CXL mode.<br/>Default value of this bit is 0. — 置 1 时，在 Flex Bus.CXL 模式下使能 CXL.cache 协议操作。<br/>默认值为 0。 |
> | 1 | RO | **IO_Enable**: When set, enables CXL.io protocol operation when in Flex Bus.CXL mode. Must always be set to 1. — 置 1 时，在 Flex Bus.CXL 模式下使能 CXL.io 协议操作。必须始终设置为 1。 |
> | 2 | RW if Downstream Port; otherwise HwInit | **Mem_Enable**: When set, enables CXL.mem protocol operation when in Flex Bus.CXL mode.<br/>Default value of this bit is 0. — 置 1 时，在 Flex Bus.CXL 模式下使能 CXL.mem 协议操作。<br/>默认值为 0。 |
> | 3 | HwInit | **CXL_Sync_Hdr_Bypass_Enable**: When set, enables bypass of the 2-bit sync header by the Flex Bus physical layer when operating in Flex Bus.CXL mode. This is a performance optimization. — 置 1 时，在 Flex Bus.CXL 模式下运行时使能 Flex Bus 物理层绕过 2-bit 同步头。这是一种性能优化。 |
> | 4 | HwInit | **Drift_Buffer_Enable**: When set, enables drift buffer (instead of elastic buffer) if there is a common reference clock. — 置 1 时，如果存在公共参考时钟，则使能 drift buffer (而不是 elastic buffer)。 |
> | 5 | RW if Downstream Port; otherwise HwInit | **CXL 68B Flit and VH Enable**: Formerly known as CXL2p0_Enable. When set, enables CXL VH operation with 68B flits when in Flex Bus.CXL mode. This bit is reserved if CXL 68B Flit and VH Capable=0.¹<br/>Default value of this bit is 0. — 置 1 时，在 Flex Bus.CXL 模式下使能 68B flit 的 CXL VH 操作。如果 CXL 68B Flit and VH Capable=0，则此位保留。¹<br/>默认值为 0。 |
> | 6 | RW if Downstream Port; otherwise HwInit | **CXL_Multi-Logical_Device_Enable**: When set, enable Multi-Logical Device operation when in Flex Bus.CXL mode. This bit shall always be cleared to 0 for CXL root ports and RCH Downstream Ports.¹<br/>Default value of this bit is 0. — 置 1 时，在 Flex Bus.CXL 模式下使能多逻辑设备操作。对于 CXL 根端口和 RCH 下行端口，此位必须始终清零为 0。¹<br/>默认值为 0。 |
> | 7 | RW if Downstream Port; otherwise HwInit | **Disable_RCD_Training**: Formerly known as Disable_CXL1p1_Training. When set, RCD mode is disabled. Typical usage model is that System Firmware will use this bit to disable Hot-Plug of an eRCD below a CXL root port or DSP. This bit is reserved on all RCD and RCH Upstream Ports.¹<br/>Default value of this bit is 0. — 置 1 时，禁用 RCD 模式。典型的使用场景是系统固件使用此位禁用 CXL 根端口或 DSP 下方 eRCD 的热插拔。此位在所有 RCD 和 RCH 上行端口上保留。¹<br/>默认值为 0。 |
> | 8 | RW if Downstream Port; otherwise, RsvdP | **Retimer1_Present**: When set, indicates presence of Retimer1. This bit is defined only for a Downstream Port. This bit is reserved for an Upstream Port.<br/>Default value of this bit is 0.<br/>This bit is only used by RCH Downstream Ports. All other ports shall ignore this bit. — 置 1 时，表示存在 Retimer1。此位仅为下行端口定义。此位对于上行端口保留。<br/>默认值为 0。<br/>此位仅由 RCH 下行端口使用。所有其他端口应忽略此位。 |
> | 9 | RW if Downstream Port; otherwise, RsvdP | **Retimer2_Present**: When set, indicates presence of Retimer2. This bit is defined only for a Downstream Port. This bit is reserved for an Upstream Port.<br/>Default value of this bit is 0.<br/>This bit is only used by RCH Downstream Ports. All other ports shall ignore this bit. — 置 1 时，表示存在 Retimer2。此位仅为下行端口定义。此位对于上行端口保留。<br/>默认值为 0。<br/>此位仅由 RCH 下行端口使用。所有其他端口应忽略此位。 |
> | 12:10 | RsvdP | Reserved — 保留 |
> | 13 | RW if Downstream Port; otherwise HwInit | **CXL Latency_Optimized_256B_Flit_Enable**: When set, enables latency-optimized 256B flits when in Flex Bus.CXL mode. This bit is reserved on components that do not support 256B Flit mode.²<br/>Default value of this bit is 0. — 置 1 时，在 Flex Bus.CXL 模式下使能 latency-optimized 256B flit。不支持 256B Flit 模式的组件上此位保留。²<br/>默认值为 0。 |
> | 14 | RW if Downstream Port; otherwise, HwInit | **CXL PBR Flit Enable**: When set, enables PBR flits when in Flex Bus.CXL mode. This bit is reserved on components that do not support PBR Flit mode. See Table 6-11.²<br/>Default value of this bit is 0. — 置 1 时，在 Flex Bus.CXL 模式下使能 PBR flit。不支持 PBR Flit 模式的组件上此位保留。参见表 6-11。²<br/>默认值为 0。 |
> | 15 | RsvdP | Reserved — 保留 |
>
> 1. Introduced as part of DVSEC Revision=1.
> 2. Introduced as part of DVSEC Revision=2.
> 1. 在 DVSEC Revision=1 中引入。
> 2. 在 DVSEC Revision=2 中引入。

<a id="sec-8-2-1-3-3"></a>
##### 8.2.1.3.3 DVSEC Flex Bus Port Status (Offset 0Eh) | DVSEC Flex Bus 端口状态 (偏移 0Eh)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Flex Bus physical layer reports the results of alternate protocol negotiation in this register.</td><td style="background-color:#e8e8e8">Flex Bus 物理层在此寄存器中报告备用协议协商的结果。</td></tr>
</tbody>
</table>

> **Table 8-46.** DVSEC Flex Bus Port Status (Offset 0Eh) ｜ DVSEC Flex Bus 端口状态 (偏移 0Eh)
>
> | Bit | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RO | **Cache_Enabled**: When set, indicates that CXL.cache protocol operation has been enabled as a result of PCIe alternate protocol negotiation for Flex Bus. — 置 1 时，表示已通过 PCIe 备用协议协商为 Flex Bus 启用 CXL.cache 协议操作。 |
> | 1 | RO | **IO_Enabled**: When set, indicates that CXL.io protocol operation has been enabled as a result of PCIe alternate protocol negotiation for Flex Bus. — 置 1 时，表示已通过 PCIe 备用协议协商为 Flex Bus 启用 CXL.io 协议操作。 |
> | 2 | RO | **Mem_Enabled**: When set, indicates that CXL.mem protocol operation has been enabled as a result of PCIe alternate protocol negotiation for Flex Bus. — 置 1 时，表示已通过 PCIe 备用协议协商为 Flex Bus 启用 CXL.mem 协议操作。 |
> | 3 | RO | **CXL_Sync_Hdr_Bypass_Enabled**: When set, indicates that bypass of the 2-bit sync header by the Flex Bus physical layer has been enabled when operating in Flex Bus.CXL mode as a result of PCIe alternate protocol negotiation for Flex Bus. — 置 1 时，表示已通过 PCIe 备用协议协商在 Flex Bus.CXL 模式下运行时由 Flex Bus 物理层启用绕过 2-bit 同步头。 |
> | 4 | RO | **Drift_Buffer_Enabled**: When set, indicates that the physical layer has enabled its drift buffer instead of its elastic buffer. — 置 1 时，表示物理层已启用其 drift buffer 而非 elastic buffer。 |
> | 5 | RO | **CXL 68B Flit and VH Enabled**: Formerly known as CXL2p0_Enabled. When set, indicates that CXL VH operation with 68B Flit mode has been enabled as a result of PCIe alternate protocol negotiation for Flex Bus.¹ — 置 1 时，表示已通过 PCIe 备用协议协商为 Flex Bus 启用 68B Flit 模式的 CXL VH 操作。¹ |
> | 6 | RO | **CXL_Multi-Logical_Device_Enabled**: When set, indicates that CXL Multi-Logical Device operation has been negotiated.¹ — 置 1 时，表示已协商 CXL 多逻辑设备操作。¹ |
> | 7 | RW1CS | **Even Half Failed**: When set, indicates the Physical Layer detected a CRC error on the even flit half of a post-FEC corrected flit; however, even flit half was previously consumed because the even half passed CRC in the original flit. This bit is reserved in 68B Flit mode.<br/>This error is also logged as a Receiver Error in the AER Correctable Status register by the associated root port.² — 置 1 时，表示物理层在后 FEC 校正 flit 的偶数 flit 半部分检测到 CRC 错误；但是偶数 flit 半部分先前已被消费，因为偶数半部分在原始 flit 中通过了 CRC。在 68B Flit 模式下，此位保留。<br/>此错误还由关联根端口作为接收错误记录在 AER Correctable Status 寄存器中。² |
> | 8 | RW1CS | **CXL_Correctable_Protocol_ID_Framing_Error**: See Section 6.2.2 for more details. This bit is reserved in 256B Flit mode.<br/>It is recommended that this error also be logged as a Receiver Error in the AER Correctable Status register by the associated root port. — 详见 6.2.2 节。在 256B Flit 模式下，此位保留。<br/>建议此错误也由关联根端口作为接收错误记录在 AER Correctable Status 寄存器中。 |
> | 9 | RW1CS | **CXL_Uncorrectable_Protocol_ID_Framing_Error**: See Section 6.2.2 for more details. This bit is reserved in 256B Flit mode.<br/>It is recommended that this error also be logged as a Receiver Error in the AER Correctable Status register by the associated root port. — 详见 6.2.2 节。在 256B Flit 模式下，此位保留。<br/>建议此错误也由关联根端口作为接收错误记录在 AER Correctable Status 寄存器中。 |
> | 10 | RW1CS | **CXL_Unexpected_Protocol_ID_Dropped**: When set, indicates that the physical layer dropped a flit with an unexpected Protocol ID that is not the result of an Uncorrectable Protocol ID Framing Error. See Section 6.2.2 for more details. This bit is reserved in 256B Flit mode.<br/>It is recommended that this error also be logged as a Receiver Error in the AER Correctable Status register by the associated root port. — 置 1 时，表示物理层丢弃了一个具有意外协议 ID 的 flit，这并非 Uncorrectable Protocol ID Framing Error 的结果。详见 6.2.2 节。在 256B Flit 模式下，此位保留。<br/>建议此错误也由关联根端口作为接收错误记录在 AER Correctable Status 寄存器中。 |
> | 11 | RW1CS | **CXL_Retimers_Present_Mismatched**: When set, indicates that the Downstream Port physical layer detected an inconsistency in the "Retimers Present" or "Two Retimers Present" bits in the received TS2 Ordered Sets during Polling.Config vs. Config.Complete LTSSM states. The physical layer will force disable of the sync header bypass optimization when this error condition has been detected. See Section 6.4.1.2.1 for more details. This bit is reserved on Upstream Ports. — 置 1 时，表示下行端口物理层在 Polling.Config vs. Config.Complete LTSSM 状态期间检测到接收的 TS2 Ordered Sets 中 "Retimers Present" 或 "Two Retimers Present" 位的不一致。检测到此错误情况时，物理层将强制禁用同步头绕过优化。详见 6.4.1.2.1 节。在上行端口上此位保留。 |
> | 12 | RW1CS | **FlexBusEnableBits_Phase2_Mismatch**: When set, indicates that the Downstream Port physical layer detected that the Upstream Port did not exactly reflect the Flex Bus enable bits located in symbols 12-14 of the modified TS2 during Phase 2 of the negotiation. See Section 6.4.1.1 for more details. This bit is reserved on Upstream Ports. — 置 1 时，表示下行端口物理层检测到上行端口在协商阶段 2 期间未准确反映修改后的 TS2 中符号 12-14 处的 Flex Bus 使能位。详见 6.4.1.1 节。在上行端口上此位保留。 |
> | 13 | RO | **CXL Latency_Optimized_256B_Flit_Enabled**: When set, indicates that latency-optimized 256B flits have been enabled as a result of PCIe alternate protocol negotiation for Flex Bus.² — 置 1 时，表示已通过 PCIe 备用协议协商为 Flex Bus 启用 latency-optimized 256B flit。² |
> | 14 | RO | **CXL PBR Flit Enabled**: When set, indicates that PBR flits have been enabled as a result of PCIe alternate protocol negotiation for Flex Bus. See Table 6-11.² — 置 1 时，表示已通过 PCIe 备用协议协商为 Flex Bus 启用 PBR flit。参见表 6-11。² |
> | 15 | RO | **CXL.io_Throttle_Required_at_64GT/s**: When set, indicates that the partner Upstream Port does not support receiving consecutive CXL.io flits at 64 GT/s (see Section 6.4.1.3).<br/>This bit is only defined for Downstream Ports; this bit is reserved on Upstream Ports.² — 置 1 时，表示对端上行端口不支持以 64 GT/s 接收连续的 CXL.io flit (见 6.4.1.3 节)。<br/>此位仅针对下行端口定义；上行端口上此位保留。² |
>
> 1. Introduced as part of DVSEC Revision=1.
> 2. Introduced as part of DVSEC Revision=2.
> 1. 在 DVSEC Revision=1 中引入。
> 2. 在 DVSEC Revision=2 中引入。

<a id="sec-8-2-1-3-4"></a>
##### 8.2.1.3.4 DVSEC Flex Bus Port Received Modified TS Data Phase1 (Offset 10h) | DVSEC Flex Bus 端口接收的修改 TS 数据阶段 1 (偏移 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>If CXL alternate protocol negotiation is enabled and the Modified TS Received bit is set in the 32.0 GT/s Status register (see PCIe Base Specification), then this register contains the values received in Symbols 12 through 14 of the Modified TS1 Ordered Set during Phase 1 of CXL alternate protocol negotiation.</td><td style="background-color:#e8e8e8">如果启用了 CXL 备用协议协商并且 32.0 GT/s Status 寄存器 (见 PCIe 基础规范) 中的 Modified TS Received 位置 1，则此寄存器包含在 CXL 备用协议协商阶段 1 期间在 Modified TS1 Ordered Set 的符号 12 至 14 中接收的值。</td></tr>
</tbody>
</table>

> **Table 8-47.** DVSEC Flex Bus Port Received Modified TS Data Phase1 (Offset 10h) ｜ DVSEC Flex Bus 端口接收的修改 TS 数据阶段 1 (偏移 10h)
>
> | Bit | Attributes | Description¹ / 描述¹ |
> |---|---|---|
> | 23:0 | RO | **Received_Flex_Bus_Data_Phase_1**: This field contains the values received in Symbols 12 through 14 of the Modified TS1 Ordered Set during Phase 1 of CXL alternate protocol negotiation.² — 此字段包含在 CXL 备用协议协商阶段 1 期间在 Modified TS1 Ordered Set 的符号 12 至 14 中接收的值。² |
> | 31:24 | RsvdZ | Reserved — 保留 |
>
> 1. This register was introduced as part of DVSEC Revision=1.
> 2. This field was introduced as part of DVSEC Revision=1.
> 1. 此寄存器在 DVSEC Revision=1 中引入。
> 2. 此字段在 DVSEC Revision=1 中引入。

<a id="sec-8-2-1-3-5"></a>
##### 8.2.1.3.5 DVSEC Flex Bus Port Capability2 (Offset 14h) | DVSEC Flex Bus 端口能力 2 (偏移 14h)

> **Table 8-48.** DVSEC Flex Bus Port Capability2 (Offset 14h) ｜ DVSEC Flex Bus 端口能力 2 (偏移 14h)
>
> | Bit | Attributes | Description¹ / 描述¹ |
> |---|---|---|
> | 0 | RO | **NOP_Hint_Capable**: If set, indicates support for sending and processing NOP hints when operating with latency-optimized 256B flits in Flex Bus.CXL mode.² — 置 1 时，表示在 Flex Bus.CXL 模式下使用 latency-optimized 256B flit 运行时支持发送和处理 NOP 提示。² |
> | 31:1 | RsvdP | Reserved — 保留 |
>
> 1. This register was introduced as part of DVSEC Revision=2.
> 2. This bit was introduced as part of DVSEC Revision = 2.
> 1. 此寄存器在 DVSEC Revision=2 中引入。
> 2. 此位在 DVSEC Revision=2 中引入。

<a id="sec-8-2-1-3-6"></a>
##### 8.2.1.3.6 DVSEC Flex Bus Port Control2 (Offset 18h) | DVSEC Flex Bus 端口控制 2 (偏移 18h)

> **Table 8-49.** DVSEC Flex Bus Port Control2 (Offset 18h) ｜ DVSEC Flex Bus 端口控制 2 (偏移 18h)
>
> | Bit | Attributes | Description¹ / 描述¹ |
> |---|---|---|
> | 0 | RW | **NOP_Hint_Enable**: If set, enables sending and processing NOP hints when operating with latency-optimized 256B flits in Flex Bus.CXL mode.²<br/>The default value of this field is 0. — 置 1 时，在 Flex Bus.CXL 模式下使用 latency-optimized 256B flit 运行时使能发送和处理 NOP 提示。²<br/>此字段默认值为 0。 |
> | 31:1 | RsvdP | Reserved — 保留 |
>
> 1. This register was introduced as part of DVSEC Revision=2.
> 2. This bit was introduced as part of DVSEC Revision = 2.

<a id="sec-8-2-1-3-7"></a>
##### 8.2.1.3.7 DVSEC Flex Bus Port Status2 (Offset 1Ch) | DVSEC Flex Bus 端口状态 2 (偏移 1Ch)

> **Table 8-50.** DVSEC Flex Bus Port Status2 (Offset 1Ch) ｜ DVSEC Flex Bus 端口状态 2 (偏移 1Ch)
>
> | Bit | Attributes | Description¹ / 描述¹ |
> |---|---|---|
> | 1:0 | RO | **NOP_Hint_Info**: The Physical Layer captures what the remote link partner advertises during Phase 1 of link training.² — 物理层捕获对端链路伙伴在链路训练阶段 1 期间公布的内容。² |
> | 31:2 | RsvdP | Reserved — 保留 |
>
> 1. This register was introduced as part of DVSEC Revision=2.
> 2. This field was introduced as part of DVSEC Revision = 2.

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-2"></a>
## 8.2.2 Accessing Component Registers | 访问组件寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The RCD Upstream Port maps the Component registers in memory space that are allocated via the MEMBAR0 register of the RCD RCRB if the RCD implements RCRB. Similarly, the RCH Downstream Port maps the Component registers in memory space that are allocated via the MEMBAR0 register of the RCH RCRB. Section 8.2.3 defines the architected registers. Table 8-21 lists the relevant offset ranges from MEMBAR0 for CXL.io, CXL.cache, CXL.mem, and CXL ARB/MUX registers.</td><td style="background-color:#e8e8e8">如果 RCD 实现 RCRB，则 RCD 上行端口在内存空间中映射通过 RCD RCRB 的 MEMBAR0 寄存器分配的 Component 寄存器。类似地，RCH 下行端口在内存空间中映射通过 RCH RCRB 的 MEMBAR0 寄存器分配的 Component 寄存器。8.2.3 节定义了架构寄存器。表 8-21 列出了 MEMBAR0 中 CXL.io、CXL.cache、CXL.mem 和 CXL ARB/MUX 寄存器的相关偏移范围。</td></tr>
<tr><td>For an RCD Upstream Port that does not implement RCRB and for CXL components that are part of a CXL VH, the Component registers are mapped in memory space allocated via a standard PCIe BAR. The Register Locator DVSEC structure (see Section 8.1.9) describes the BAR number and the offset within the BAR where these registers are mapped.</td><td style="background-color:#e8e8e8">对于未实现 RCRB 的 RCD 上行端口以及作为 CXL VH 一部分的 CXL 组件，Component 寄存器映射到通过标准 PCIe BAR 分配的内存空间。Register Locator DVSEC 结构 (见 8.1.9 节) 描述了映射这些寄存器的 BAR 号和 BAR 内的偏移。</td></tr>
<tr><td>A CXL Host Bridge contains Component registers that control the functionality of one or more CXL root ports. These are labeled CHBCR. These registers are also mapped in memory space, and the base address is discovered via ACPI CEDT (see Section 9.18.1.2).</td><td style="background-color:#e8e8e8">CXL Host Bridge 包含控制一个或多个 CXL 根端口功能的 Component 寄存器。这些标记为 CHBCR。这些寄存器也映射到内存空间，基址通过 ACPI CEDT (见 9.18.1.2 节) 发现。</td></tr>
<tr><td>For register layout, see Figure 9-14 and Figure 9-15.</td><td style="background-color:#e8e8e8">有关寄存器布局，请参见图 9-14 和图 9-15。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-3"></a>
## 8.2.3 Component Register Layout and Definition | 组件寄存器布局和定义

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The layout and discovery mechanism of the Component register is identical for all CXL Components and CXL Host Bridges (CHBCR). Table 8-21 lists the relevant offset ranges from the Base of the Component register block for CXL.io, CXL.cache, CXL.mem, and CXL ARB/MUX registers.</td><td style="background-color:#e8e8e8">对于所有 CXL 组件和 CXL Host Bridge (CHBCR)，Component 寄存器的布局和发现机制相同。表 8-21 列出了 Component 寄存器块基址起的 CXL.io、CXL.cache、CXL.mem 和 CXL ARB/MUX 寄存器的相关偏移范围。</td></tr>
<tr><td>Software shall use CXL.io Memory Reads and Writes to access CXL Component registers defined in Section 8.2.4 and Section 8.2.5. Software shall restrict the access width based on the following rules:</td><td style="background-color:#e8e8e8">软件应使用 CXL.io 内存读写访问 8.2.4 节和 8.2.5 节中定义的 CXL Component 寄存器。软件应根据以下规则限制访问宽度：</td></tr>
<tr><td>• A 32-bit register shall be accessed as a 4-byte quantity. Partial reads are not permitted.</td><td style="background-color:#e8e8e8">• 32 位寄存器应作为 4 字节量访问。不允许部分读取。</td></tr>
<tr><td>• A 64-bit register shall be accessed as an 8-byte quantity. Partial reads are not permitted.</td><td style="background-color:#e8e8e8">• 64 位寄存器应作为 8 字节量访问。不允许部分读取。</td></tr>
<tr><td>• Accesses shall map to contiguous bytes.</td><td style="background-color:#e8e8e8">• 访问应映射到连续字节。</td></tr>
<tr><td>If these rules are not followed, the behavior is undefined. Note that these rules are more stringent than the general rules for the memory mapped registers that are specified in Section 8.2.</td><td style="background-color:#e8e8e8">如果不遵循这些规则，则行为未定义。请注意，这些规则比 8.2 节中规定的内存映射寄存器通用规则更严格。</td></tr>
<tr><td>This section and Table 8-22 in this version of the specification do not define the behavior of CXL fabric switches (see Section 2.7) and G-FAM devices (see Section 2.8).</td><td style="background-color:#e8e8e8">本规范此版本的本节和表 8-22 未定义 CXL 交换网交换器 (见 2.7 节) 和 G-FAM 设备 (见 2.8 节) 的行为。</td></tr>
</tbody>
</table>

> **Table 8-51.** CXL Subsystem Component Register Ranges ｜ CXL 子系统组件寄存器范围
>
> | Range | Size | Description / 描述 |
> |---|---|---|
> | 0000 0000h - 0000 0FFFh | 4 KB | Reserved for CXL.io registers. This specification does not define any CXL.io registers, hence the entire range is considered reserved. — 保留供 CXL.io 寄存器使用。本规范未定义任何 CXL.io 寄存器，因此整个范围被视为保留。 |
> | 0000 1000h - 0000 1FFFh | 4 KB | CXL.cachemem Primary Range — CXL.cachemem 主范围 |
> | 0000 2000h - 0000 DFFFh | 48 KB | Implementation specific. May host zero or more instances of CXL.cachemem Extended Ranges. — 实现特定。可托管零个或多个 CXL.cachemem Extended Range 实例。 |
> | 0000 E000h - 0000 E3FFh | 1 KB | CXL ARB/MUX registers — CXL ARB/MUX 寄存器 |
> | 0000 E400h - 0000 FFFFh | 7 KB | Reserved. The range F000-FFFFh may host CXL.cachemem Extended Range. — 保留。范围 F000-FFFFh 可托管 CXL.cachemem Extended Range。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4"></a>
## 8.2.4 CXL.cache and CXL.mem Registers | CXL.cache 和 CXL.mem 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL.cache and CXL.mem registers are located in the CXL.cachemem Primary Range (Offset 1000h-1FFFh) or one of the CXL.cachemem Extended Ranges. Within each of the 4-KB region of memory space assigned to CXL.cache and CXL.mem, the location of architecturally specified registers is described using an array of pointers. The array, described in Table 8-23, is located starting at Offset 00h of this 4-KB region. The first element of the array will declare the version of CXL.cache and CXL.mem protocols, as well as the size of the array. Each subsequent element will then host the pointers to capability-specific register blocks within the 4-KB region. Table 8-24 and Table 8-25 illustrate this concept with an example.</td><td style="background-color:#e8e8e8">CXL.cache 和 CXL.mem 寄存器位于 CXL.cachemem Primary Range (偏移 1000h-1FFFh) 或某个 CXL.cachemem Extended Range 中。在分配给 CXL.cache 和 CXL.mem 的 4-KB 内存区域内，架构规定的寄存器位置使用指针数组来描述。表 8-23 描述的数组从该 4-KB 区域的偏移 00h 处开始。数组的第一个元素将声明 CXL.cache 和 CXL.mem 协议的版本以及数组大小。每个后续元素将承载 4-KB 区域内指向能力特定寄存器块的指针。表 8-24 和表 8-25 通过示例说明了此概念。</td></tr>
<tr><td>Structures with Capability ID of 1 through 0Ah are not permitted to be part of the CXL.cachemem Extended Ranges. Capability ID 0Ah structure identifies the CXL.cachemem Extended Ranges. Structures with Capability ID 0 or Capability ID greater than 0Ah are permitted to be part of the CXL.cachemem Primary Range or any of the CXL.cachemem Extended Ranges.</td><td style="background-color:#e8e8e8">Capability ID 为 1 至 0Ah 的结构不允许成为 CXL.cachemem Extended Range 的一部分。Capability ID 0Ah 结构标识 CXL.cachemem Extended Range。Capability ID 0 或 Capability ID 大于 0Ah 的结构允许成为 CXL.cachemem Primary Range 或任何 CXL.cachemem Extended Range 的一部分。</td></tr>
<tr><td>For each capability ID, CXL_Capability_Version field is incremented whenever the structure is extended to add more functionality. Backward compatibility shall be maintained during this process. For all values of n, CXL_Capability_Version=n+1 structure may extend CXL_Capability_Version=n by replacing fields that are marked as reserved in CXL_Capability_Version= n, but shall not redefine the meaning of existing fields. In addition, CXL_Capability_Version n+1 may append new registers to the CXL_Capability_Version n structure. Software that was written for a lower CXL_Capability_Version may continue to operate on structures with a higher CXL_Capability_Version, but will not be able to take advantage of new functionality.</td><td style="background-color:#e8e8e8">对于每个 capability ID，当结构被扩展以添加更多功能时，CXL_Capability_Version 字段会递增。在此过程中必须保持向后兼容。对于所有 n 值，CXL_Capability_Version=n+1 结构可以通过替换 CXL_Capability_Version=n 中标记为保留的字段来扩展 CXL_Capability_Version=n，但不得重新定义现有字段的含义。此外，CXL_Capability_Version n+1 可以向 CXL_Capability_Version n 结构追加新寄存器。针对较低 CXL_Capability_Version 编写的软件可以继续在具有较高 CXL_Capability_Version 的结构上运行，但将无法利用新功能。</td></tr>
<tr><td>CXL_Capability_ID field represents the functionality and CXL_Capability_Version represents the version of the structure. The following values of CXL_Capability_ID are defined by CXL specification.</td><td style="background-color:#e8e8e8">CXL_Capability_ID 字段表示功能，CXL_Capability_Version 字段表示结构的版本。以下 CXL_Capability_ID 值由 CXL 规范定义。</td></tr>
</tbody>
</table>

> **Table 8-52.** CXL_Capability_ID Assignment ｜ CXL_Capability_ID 分配
>
> | Capability | ID | Highest Version | Mandatory¹ | Not Permitted¹ | Optional¹ |
> |---|---|---|---|---|---|
> | CXL NULL Capability – Software shall ignore this structure and skip to the next CXL Capability | 0 | Undefined | P | D1, D2, LD, FMLD, DP1, UP1, USP, vUSP, DSP, vDSP, R, RC | — |
> | CXL Capability (Section 8.2.4.1) | 1 | 1 | D1, D2, LD, FMLD, UP1, DP1, R, USP, vUSP, DSP, vDSP, RC | P | — |
> | CXL RAS Capability (Section 8.2.4.17) | 2 | 3 | D1, D2, LD, FMLD, UP1, DP1, R, USP, DSP | P, RC | vUSP, vDSP |
> | CXL Security Capability (Section 8.2.4.18) | 3 | 1 | DP1 | All others | — |
> | CXL Link Capability (Section 8.2.4.19) | 4 | 4 | D1, D2, LD, FMLD, UP1, DP1, R, USP, DSP | P, RC, vUSP, vDSP | — |
> | CXL HDM Decoder Capability (Section 8.2.4.20) | 5 | 3 | Type 3 D2, LD, RC except RCH, USP, vUSP | All others | Type 2 D2, D1 |
> | CXL Extended Security Capability (Section 8.2.4.21) | 6 | 2 | RC | All others | — |
> | CXL IDE Capability (Section 8.2.4.22) | 7 | 2 | P, D1, LD, UP1, DP1 | D2, FMLD, R, USP, vUSP, DSP, vDSP | — |
> | CXL Snoop Filter Capability (Section 8.2.4.23) | 8 | 1 | R | P, D1, D2, LD, FMLD, UP1, USP, vUSP, DSP, vDSP, RC | DP1 |
> | CXL Timeout and Isolation Capability (Section 8.2.4.24) | 9 | 1 | P, D1, D2, LD, FMLD, UP1, USP, vUSP, DSP, vDSP, RC | R | — |
> | CXL.cachemem Extended Register Capability (Section 8.2.4.25) | 0Ah | 1 | P | D1, D2, LD, FMLD, UP1, R, USP, vUSP, DSP, vDSP, RC | — |
> | CXL BI Route Table Capability (Section 8.2.4.26) | 0Bh | 1 | USP or vUSPs that requires explicit BI commit | All others | All other USPs or vUSPs |
> | CXL BI Decoder Capability (Section 8.2.4.27) | 0Ch | 1 | DSP or vDSPs or Type 2 D2 that advertises 256B Flit mode | P, D1, FMLD, UP1, DP1, R, USPs, RC | R², all other DSPs, all other vDSPs, all other D2s, LD |
> | CXL Cache ID Route Table Capability (Section 8.2.4.28) | 0Dh | 1 | All others | RC, USP | — |
> | CXL Cache ID Decoder Capability (Section 8.2.4.29) | 0Eh | 1 | P, D1, D2, LD, FMLD, UP1, DP1, R, USP, vUSP, RC | R, DSP, vDSP | — |
> | CXL Extended HDM Decoder Capability (Section 8.2.4.30) | 0Fh | 3 | All others | RC, USP, vUSP | — |
> | CXL Extended Metadata Capability (Section 8.2.4.31) | 10h | 1 | All others | CXL.mem capable LD or D2 that supports 256B Flit Mode | — |
>
> 1. P – PCIe device, D1 – RCD, D2 – CXL device that is not RCD, LD – Logical Device, FMLD – Fabric Manager owned LD FFFFh, UP1 – RCD Upstream Port RCRB, DP1 – RCH Downstream Port, R – CXL root port, RC – CXL Host Bridge registers in CHBCR, USP – CXL Upstream Switch Port, vUSP – see Table 1-1, DSP – CXL Downstream Switch Port, vDSP – see Table 1-1. A physical component may be capable of operating in multiple modes (e.g., a CXL device may operate either in D1 mode or D2 mode based on the link training). In such cases, these definitions refer to the current mode of operation.
> 2. Strongly recommended for a host that supports 256B Flit mode.
> 1. P – PCIe 设备，D1 – RCD，D2 – 非 RCD 的 CXL 设备，LD – 逻辑设备，FMLD – Fabric Manager 拥有的 LD FFFFh，UP1 – RCD 上行端口 RCRB，DP1 – RCH 下行端口，R – CXL 根端口，RC – CHBCR 中的 CXL Host Bridge 寄存器，USP – CXL 上行交换端口，vUSP – 见表 1-1，DSP – CXL 下行交换端口，vDSP – 见表 1-1。一个物理组件可能能够以多种模式运行 (例如，CXL 设备可能基于链路训练以 D1 模式或 D2 模式运行)。在这种情况下，这些定义指的是当前的操作模式。
> 2. 强烈建议支持 256B Flit 模式的主机使用。

> **Table 8-53.** CXL.cache and CXL.mem Architectural Register Discovery ｜ CXL.cache 和 CXL.mem 架构寄存器发现
>
> | Offset | Register Name / 寄存器名称 |
> |---|---|
> | 00h | CXL_Capability_Header |
> | 04h | (Length = n*4, where n is the number of capability headers)<br/>An array of individual capability headers. See Table 8-22 for the enumeration. — (长度 = n*4，其中 n 是 capability headers 的数量)<br/>各个 capability headers 的数组。有关枚举，请参见表 8-22。 |

> **Table 8-54.** CXL.cache and CXL.mem Architectural Register Header Example (Primary Range) ｜ CXL.cache 和 CXL.mem 架构寄存器 Header 示例 (主范围)
>
> | Byte Offset | Register Name / 寄存器名称 |
> |---|---|
> | 00h | CXL_Capability_Header |
> | 04h | CXL_RAS_Capability_Header |
> | 08h | CXL_Security_Capability_Header |
> | 0Ch | CXL_Link_Capability_Header |
> | 10h | CXL.cachemem Extended Register Capability Header |

> **Table 8-55.** CXL.cache and CXL.mem Architectural Register Header Example (Any Extended Range) ｜ CXL.cache 和 CXL.mem 架构寄存器 Header 示例 (任意扩展范围)
>
> | Byte Offset | Register Name / 寄存器名称 |
> |---|---|
> | 00h | CXL_Capability_Header |
> | 04h | CXL BI Decoder Capability Header |
> | 08h | CXL NULL Capability Header |
> | 0Ch | CXL Cache ID Decoder Capability Header |

<a id="sec-8-2-4-1"></a>
### 8.2.4.1 CXL Capability Header Register (Offset 00h) | CXL 能力 Header 寄存器 (偏移 00h)

> **Table 8-56.** CXL Capability Header Register (Offset 00h) ｜ CXL 能力 Header 寄存器 (偏移 00h)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_Capability_Header register, this field must be 0001h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_Capability_Header 寄存器，此字段必须为 0001h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. For this and the prior version of the specification, this field must be 1h. — 这定义了当前 CXL_Capability 结构的版本号。对于本规范及其先前版本，此字段必须为 1h。 |
> | 23:20 | RO | **CXL_Cache_Mem_Version**: This defines the version of the CXL.cachemem Protocol supported. For this and the prior versions of the specification, this field must be 1h. — 这定义了支持的 CXL.cachemem 协议的版本。对于本规范及其先前版本，此字段必须为 1h。 |
> | 31:24 | RO | **Array_Size**: This defines the number of elements present in the CXL_Capability array, not including the CXL_Capability_Header element. Each element is 1 DWORD in size and is located contiguous with previous elements. — 这定义了 CXL_Capability 数组中存在的元素数，不包括 CXL_Capability_Header 元素。每个元素大小为 1 DWORD，并与前一个元素连续。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-2"></a>
### 8.2.4.2 CXL RAS Capability Header (Offset: Varies) | CXL RAS 能力 Header (偏移：可变)

> **Table 8-57.** CXL RAS Capability Header (Offset: Varies) ｜ CXL RAS 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_RAS_Capability_Pointer register, this field shall be 0002h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_RAS_Capability_Pointer 寄存器，此字段必须为 0002h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. Version 3h represents the structure as defined in this specification. — 这定义了当前 CXL_Capability 结构的版本号。版本 3h 表示本规范定义的结构。 |
> | 31:20 | RO | **CXL_RAS_Capability_Pointer**: This defines the offset of the CXL RAS Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.17. — 这定义了 CXL RAS Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.17 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-3"></a>
### 8.2.4.3 CXL Security Capability Header (Offset: Varies) | CXL 安全能力 Header (偏移：可变)

> **Table 8-58.** CXL Security Capability Header (Offset: Varies) ｜ CXL 安全能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_Security_Capability_Pointer register, this field shall be 0003h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_Security_Capability_Pointer 寄存器，此字段必须为 0003h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL_Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL_Security_Capability_Pointer**: This defines the offset of the CXL Security Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.18. — 这定义了 CXL Security Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.18 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-4"></a>
### 8.2.4.4 CXL Link Capability Header (Offset: Varies) | CXL 链路能力 Header (偏移：可变)

> **Table 8-59.** CXL Link Capability Header (Offset: Varies) ｜ CXL 链路能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_Link_Capability_Pointer register, this field shall be 0004h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_Link_Capability_Pointer 寄存器，此字段必须为 0004h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. Version 4h represents the structure as defined in this specification. — 这定义了当前 CXL_Capability 结构的版本号。版本 4h 表示本规范定义的结构。 |
> | 31:20 | RO | **CXL_Link_Capability_Pointer**: This defines the offset of the CXL Link Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.19. — 这定义了 CXL Link Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.19 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-5"></a>
### 8.2.4.5 CXL HDM Decoder Capability Header (Offset: Varies) | CXL HDM Decoder 能力 Header (偏移：可变)

> **Table 8-60.** CXL HDM Decoder Capability Header (Offset: Varies) ｜ CXL HDM Decoder 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_HDM_Decoder_Capability_Pointer register, this field shall be 0005h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_HDM_Decoder_Capability_Pointer 寄存器，此字段必须为 0005h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. For this version of the specification, this field must be 3h. — 这定义了当前 CXL_Capability 结构的版本号。对于本规范版本，此字段必须为 3h。 |
> | 31:20 | RO | **CXL_HDM_Decoder_Capability_Pointer**: This defines the offset of the CXL HDM Decoder Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.20. — 这定义了 CXL HDM Decoder Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.20 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-6"></a>
### 8.2.4.6 CXL Extended Security Capability Header (Offset: Varies) | CXL 扩展安全能力 Header (偏移：可变)

> **Table 8-61.** CXL Extended Security Capability Header (Offset: Varies) ｜ CXL 扩展安全能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_Extended Security_Capability_Pointer register, this field shall be 0006h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_Extended Security_Capability_Pointer 寄存器，此字段必须为 0006h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. For this version of the specification, this field must be 2h. — 这定义了当前 CXL_Capability 结构的版本号。对于本规范版本，此字段必须为 2h。 |
> | 31:20 | RO | **CXL_Extended_Security_Capability_Pointer**: This defines the offset of the CXL Extended Security Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.21. — 这定义了 CXL Extended Security Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.21 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-7"></a>
### 8.2.4.7 CXL IDE Capability Header (Offset: Varies) | CXL IDE 能力 Header (偏移：可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This capability header is present in all ports that implement CXL IDE.</td><td style="background-color:#e8e8e8">此能力 Header 出现在实现 CXL IDE 的所有端口中。</td></tr>
</tbody>
</table>

> **Table 8-62.** CXL IDE Capability Header (Offset: Varies) ｜ CXL IDE 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_IDE_Capability_Header register, this field shall be 0007h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_IDE_Capability_Header 寄存器，此字段必须为 0007h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. For this version of the specification, this field must be 2h. — 这定义了当前 CXL_Capability 结构的版本号。对于本规范版本，此字段必须为 2h。 |
> | 31:20 | RO | **CXL IDE Capability Pointer**: This defines the offset of the CXL IDE Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.22. — 这定义了 CXL IDE Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.22 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-8"></a>
### 8.2.4.8 CXL Snoop Filter Capability Header (Offset: Varies) | CXL Snoop Filter 能力 Header (偏移：可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This capability header is required for Root Ports and optional for RCH Downstream Ports.</td><td style="background-color:#e8e8e8">根端口需要此能力 Header，RCH 下行端口可选。</td></tr>
</tbody>
</table>

> **Table 8-63.** CXL Snoop Filter Capability Header (Offset: Varies) ｜ CXL Snoop Filter 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL_Capability register. For the CXL_Snoop_Filter_Capability_Header register, this field shall be 0008h. — 这定义了 CXL_Capability 寄存器的性质和格式。对于 CXL_Snoop_Filter_Capability_Header 寄存器，此字段必须为 0008h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL_Capability structure present. For this version of the specification, this field shall be 1h. — 这定义了当前 CXL_Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL Snoop Filter Capability Pointer**: This defines the offset of the CXL Snoop Filter Capability relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.23. — 这定义了 CXL Snoop Filter Capability 相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.23 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-9"></a>
### 8.2.4.9 CXL Timeout and Isolation Capability Header (Offset: Varies) | CXL Timeout and Isolation 能力 Header (偏移：可变)

> **Table 8-64.** CXL Timeout and Isolation Capability Header (Offset: Varies) ｜ CXL Timeout and Isolation 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL Timeout and Isolation Capability Header register, this field shall be 0009h. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL Timeout and Isolation Capability Header 寄存器，此字段必须为 0009h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of the CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL_Timeout_and_Isolation_Capability_Pointer**: This defines the offset of the CXL Timeout and Isolation Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.24. — 这定义了 CXL Timeout and Isolation Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.24 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-10"></a>
### 8.2.4.10 CXL.cachemem Extended Register Capability (Offset: Varies) | CXL.cachemem 扩展寄存器能力 (偏移：可变)

> **Table 8-65.** CXL.cachemem Extended Register Capability (Offset: Varies) ｜ CXL.cachemem 扩展寄存器能力 (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL.cachemem Extended Register Capability Header register, this field shall be 000Ah. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL.cachemem Extended Register Capability Header 寄存器，此字段必须为 000Ah。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL.cachemem Extended Register Capability Pointer**: This defines the offset of the CXL.cachemem Extended Register Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.25. — 这定义了 CXL.cachemem Extended Register Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.25 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-11"></a>
### 8.2.4.11 CXL BI Route Table Capability Header (Offset: Varies) | CXL BI 路由表能力 Header (偏移：可变)

> **Table 8-66.** CXL BI Route Table Capability Header (Offset: Varies) ｜ CXL BI 路由表能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL BI Route Table Capability Header register, this field shall be 000Bh. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL BI Route Table Capability Header 寄存器，此字段必须为 000Bh。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL BI Route Table Capability Pointer**: This defines the offset of the CXL BI Route Table Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.26. — 这定义了 CXL BI Route Table Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.26 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-12"></a>
### 8.2.4.12 CXL BI Decoder Capability Header (Offset: Varies) | CXL BI Decoder 能力 Header (偏移：可变)

> **Table 8-67.** CXL BI Decoder Capability Header (Offset: Varies) ｜ CXL BI Decoder 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL BI Decoder Capability Header register, this field shall be 000Ch. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL BI Decoder Capability Header 寄存器，此字段必须为 000Ch。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL BI Decoder Capability Pointer**: This defines the offset of the CXL BI Decoder Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.27. — 这定义了 CXL BI Decoder Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.27 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-13"></a>
### 8.2.4.13 CXL Cache ID Route Table Capability Header (Offset: Varies) | CXL Cache ID 路由表能力 Header (偏移：可变)

> **Table 8-68.** CXL Cache ID Route Table Capability Header (Offset: Varies) ｜ CXL Cache ID 路由表能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL Cache ID Route Table Capability Header register, this field shall be 000Dh. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL Cache ID Route Table Capability Header 寄存器，此字段必须为 000Dh。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL Cache ID Route Table Capability Pointer**: This defines the offset of the CXL Cache ID Route Table Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.28. — 这定义了 CXL Cache ID Route Table Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.28 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-14"></a>
### 8.2.4.14 CXL Cache ID Decoder Capability Header (Offset: Varies) | CXL Cache ID Decoder 能力 Header (偏移：可变)

> **Table 8-69.** CXL Cache ID Decoder Capability Header (Offset: Varies) ｜ CXL Cache ID Decoder 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL Cache ID Decoder Capability Header register, this field shall be 000Eh. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL Cache ID Decoder Capability Header 寄存器，此字段必须为 000Eh。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL Cache ID Local Decoder Capability Pointer**: This defines the offset of the CXL Cache ID Decoder Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.29. — 这定义了 CXL Cache ID Decoder Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.29 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-15"></a>
### 8.2.4.15 CXL Extended HDM Decoder Capability Header (Offset: Varies) | CXL 扩展 HDM Decoder 能力 Header (偏移：可变)

> **Table 8-70.** CXL Extended HDM Decoder Capability Header (Offset: Varies) ｜ CXL 扩展 HDM Decoder 能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL Extended HDM Decoder Capability Header register, this field shall be 000Fh. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL Extended HDM Decoder Capability Header 寄存器，此字段必须为 000Fh。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 3h and shall track the version of the CXL HDM Decoder Capability structure. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 3h，并应跟踪 CXL HDM Decoder Capability 结构的版本。 |
> | 31:20 | RO | **CXL Extended HDM Decoder Capability Pointer**: This defines the offset of the CXL Extended HDM Decoder Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.30. — 这定义了 CXL Extended HDM Decoder Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.30 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-16"></a>
### 8.2.4.16 CXL Extended Metadata Capability Header (Offset: Varies) | CXL 扩展元数据能力 Header (偏移：可变)

> **Table 8-71.** CXL Extended Metadata Capability Header (Offset: Varies) ｜ CXL 扩展元数据能力 Header (偏移：可变)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 15:0 | RO | **CXL_Capability_ID**: This defines the nature and format of the CXL Capability register. For the CXL Extended Metadata Capability Header register, this field shall be 0010h. — 这定义了 CXL Capability 寄存器的性质和格式。对于 CXL Extended Metadata Capability Header 寄存器，此字段必须为 0010h。 |
> | 19:16 | RO | **CXL_Capability_Version**: This defines the version number of CXL Capability structure present. For this version of the specification, this field must be 1h. — 这定义了当前 CXL Capability 结构的版本号。对于本规范版本，此字段必须为 1h。 |
> | 31:20 | RO | **CXL Extended Metadata Capability Pointer**: This defines the offset of the CXL Extended Metadata Capability structure relative to the beginning of the CXL_Capability_Header register. Details in Section 8.2.4.31. — 这定义了 CXL Extended Metadata Capability 结构相对于 CXL_Capability_Header 寄存器起始位置的偏移。详见 8.2.4.31 节。 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-17"></a>
### 8.2.4.17 CXL RAS Capability Structure | CXL RAS 能力结构

> **Table 8-72.** CXL RAS Capability Structure Layout ｜ CXL RAS 能力结构布局
>
> | Offset | Register Name / 寄存器名称 |
> |---|---|
> | 00h | Uncorrectable Error Status Register |
> | 04h | Uncorrectable Error Mask Register |
> | 08h | Uncorrectable Error Severity Register |
> | 0Ch | Correctable Error Status Register |
> | 10h | Correctable Error Mask Register |
> | 14h | Error Capability and Control Register |
> | 18h | Header Log Registers |

<a id="sec-8-2-4-17-1"></a>
#### 8.2.4.17.1 Uncorrectable Error Status Register (Offset 00h) | 不可纠正错误状态寄存器 (偏移 00h)

> **Table 8-73.** Uncorrectable Error Status Register (Offset 00h) ｜ 不可纠正错误状态寄存器 (偏移 00h)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RW1CS | **Cache_Data_Parity**: Internal Uncorrectable Data error such as Data Parity error or Uncorrectable Data ECC error on CXL.cache that are not signaled by using poison on the CXL interface. The Header Log register contains the H2D Data Header if detected by either a host or a DSP. The Header Log register contains the D2H Data Header if detected by either a device or a USP.<br/>For CXL RAS Capability Version >=3, DWORD 0 of the Header Log register is reserved and the Data Header shall start at Byte Offset 4 of the Header Log register.<br/>For CXL RAS Capability Version <3, the position of the Data Header in the Header Log register is not defined by this specification. — 内部不可纠正数据错误，例如 CXL.cache 上的数据奇偶校验错误或不可纠正数据 ECC 错误，不通过在 CXL 接口上使用 poison 来指示。如果由主机或 DSP 检测到，则 Header Log 寄存器包含 H2D 数据头。如果由设备或 USP 检测到，则 Header Log 寄存器包含 D2H 数据头。<br/>对于 CXL RAS Capability Version >=3，Header Log 寄存器的 DWORD 0 保留，数据头应从 Header Log 寄存器的 Byte Offset 4 开始。<br/>对于 CXL RAS Capability Version <3，本规范未定义数据头在 Header Log 寄存器中的位置。 |
> | 1 | RW1CS | **Cache_Address_Parity**: Internal Uncorrectable Address Parity error or other uncorrectable errors associated with the Address field on CXL.cache. The Header Log register contains the H2D Request Header if detected by either a host or a DSP. The Header Log register contains D2H Request Header if detected by either a device or a USP.<br/>For CXL RAS Capability Version >=3, DWORD 0 of the Header Log register is reserved and the Request Header shall start at Byte Offset 4 of the Header Log register.<br/>For CXL RAS Capability Version <3, the position of the Request Header in the Header Log register is not defined by this specification. — 内部不可纠正地址奇偶校验错误或与 CXL.cache 上地址字段关联的其他不可纠正错误。如果由主机或 DSP 检测到，则 Header Log 寄存器包含 H2D 请求头。如果由设备或 USP 检测到，则 Header Log 寄存器包含 D2H 请求头。<br/>对于 CXL RAS Capability Version >=3，Header Log 寄存器的 DWORD 0 保留，请求头应从 Header Log 寄存器的 Byte Offset 4 开始。<br/>对于 CXL RAS Capability Version <3，本规范未定义请求头在 Header Log 寄存器中的位置。 |
> | 2 | RW1CS | **Cache_BE_Parity**: Internal Uncorrectable Byte Enable Parity error or other Byte Enable uncorrectable errors on CXL.cache. The Header Log register contains the D2H Data Header if detected by either a device or a USP.<br/>For CXL RAS Capability Version >=3, DWORD 0 of the Header Log register is reserved and the Data Header shall start at Byte Offset 4 of the Header Log register.<br/>For CXL RAS Capability Version <3, the position of the Data Header in the Header Log register is not defined by this specification. — 内部不可纠正字节使能奇偶校验错误或 CXL.cache 上的其他字节使能不可纠正错误。如果由设备或 USP 检测到，则 Header Log 寄存器包含 D2H 数据头。<br/>对于 CXL RAS Capability Version >=3，Header Log 寄存器的 DWORD 0 保留，数据头应从 Header Log 寄存器的 Byte Offset 4 开始。<br/>对于 CXL RAS Capability Version <3，本规范未定义数据头在 Header Log 寄存器中的位置。 |
> | 3 | RW1CS | **Cache_Data_ECC**: Internal Uncorrectable Data ECC error on CXL.cache that are not signaled using poison on the CXL interface. The Header Log register contains the H2D Data Header if detected by either a host or a DSP. The Header Log register contains the D2H Data Header if detected by either a device or a USP.<br/>Note: For CXL RAS Capability Version <3, it is permissible to log any Uncorrectable Data error on CXL.cache in Bit 0 and not in this bit.<br/>For CXL RAS Capability Version >=3, this bit is deprecated and all Uncorrectable Data errors on CXL.cache that are not signaled by using CXL poison are logged in bit 0.<br/>For CXL RAS Capability Version <3, the position of the Data Header in the Header Log register is not defined by this specification. — CXL.cache 上内部不可纠正数据 ECC 错误，不通过在 CXL 接口上使用 poison 来指示。如果由主机或 DSP 检测到，则 Header Log 寄存器包含 H2D 数据头。如果由设备或 USP 检测到，则 Header Log 寄存器包含 D2H 数据头。<br/>注意：对于 CXL RAS Capability Version <3，允许将 CXL.cache 上的任何不可纠正数据错误记录在 Bit 0 而不是此位中。<br/>对于 CXL RAS Capability Version >=3，此位已弃用，CXL.cache 上未通过使用 CXL poison 指示的所有不可纠正数据错误均记录在 bit 0 中。<br/>对于 CXL RAS Capability Version <3，本规范未定义数据头在 Header Log 寄存器中的位置。 |
> | 4 | RW1CS | **Mem_Data_Parity**: Internal Uncorrectable Data error such as Data Parity error or Uncorrectable Data ECC error on CXL.mem that are not signaled by using poison on the CXL interface. The Header Log register contains the M2S RwD Data Header if detected by either a host or a DSP. The Header Log register contains the S2M DRS Data header if detected by either a device or a USP.<br/>For CXL RAS Capability Version >=3, DWORD 0 of the Header Log register is reserved and the Data Header shall start at Byte Offset 4 of the Header Log register.<br/>For CXL RAS Capability Version <3, the position of the Data Header in the Header Log register is not defined by this specification. — 内部不可纠正数据错误，例如 CXL.mem 上的数据奇偶校验错误或不可纠正数据 ECC 错误，不通过在 CXL 接口上使用 poison 来指示。如果由主机或 DSP 检测到，则 Header Log 寄存器包含 M2S RwD 数据头。如果由设备或 USP 检测到，则 Header Log 寄存器包含 S2M DRS 数据头。<br/>对于 CXL RAS Capability Version >=3，Header Log 寄存器的 DWORD 0 保留，数据头应从 Header Log 寄存器的 Byte Offset 4 开始。<br/>对于 CXL RAS Capability Version <3，本规范未定义数据头在 Header Log 寄存器中的位置。 |
> | 5 | RW1CS | **Mem_Address_Parity**: Internal Uncorrectable Address Parity error or other uncorrectable errors associated with the Address field on CXL.mem.<br/>For CXL RAS Capability Version <3, the position of the M2S Req message or M2S RwD Data Header or a BISnp Req message in the Header Log register is not defined by this specification.<br/>• Logging by a Host or a DSP: If bit 0 of the Header Log register is 0, the remainder of the Header Log contains the M2S Req message. If Bit 0 of the Header Log register is 1, the remainder of the Header Log contains the M2S RwD Data Header.<br/>• Logging by a Device or a USP: The remainder of the Header Log contains the BISnp message.<br/>For CXL RAS Capability Version >=3:<br/>• Logging by a Host or a DSP: If DWORD 0 bit 0 of the Header Log register is 0, the Header Log register contains the M2S Req message, starting at Byte offset 4. If DWORD 0 bit 0 of the Header Log register is 1, the remainder of the Header Log contains the M2S RwD Data Header. The Data Header shall start at Byte Offset 4 of the Header Log register. Bits 31:1 of DWORD 0 of the Header Log register are reserved.<br/>• Logging by a Device or a USP: Header Log register contains the BISnp Req message, starting at Byte offset 4. — 内部不可纠正地址奇偶校验错误或与 CXL.mem 上地址字段关联的其他不可纠正错误。<br/>对于 CXL RAS Capability Version <3，本规范未定义 Header Log 寄存器中 M2S Req 消息或 M2S RwD 数据头或 BISnp Req 消息的位置。<br/>• 由主机或 DSP 记录：如果 Header Log 寄存器的 bit 0 为 0，则 Header Log 的其余部分包含 M2S Req 消息。如果 Header Log 寄存器的 Bit 0 为 1，则 Header Log 的其余部分包含 M2S RwD 数据头。<br/>• 由设备或 USP 记录：Header Log 的其余部分包含 BISnp 消息。<br/>对于 CXL RAS Capability Version >=3：<br/>• 由主机或 DSP 记录：如果 Header Log 寄存器的 DWORD 0 bit 0 为 0，则 Header Log 寄存器包含 M2S Req 消息，从 Byte offset 4 开始。如果 Header Log 寄存器的 DWORD 0 bit 0 为 1，则 Header Log 的其余部分包含 M2S RwD 数据头。数据头应从 Header Log 寄存器的 Byte Offset 4 开始。Header Log 寄存器的 DWORD 0 的 Bits 31:1 保留。<br/>• 由设备或 USP 记录：Header Log 寄存器包含 BISnp Req 消息，从 Byte offset 4 开始。 |
> | 6 | RW1CS | **Mem_BE_Parity**: Internal Uncorrectable Byte Enable Parity error or other Byte Enable uncorrectable errors on CXL.mem. The Header Log register contains the M2S RwD Data Header if detected by either a host or a DSP.<br/>For CXL RAS Capability Version >=3, DWORD 0 of the Header Log register is reserved and the Data Header shall start at Byte Offset 4 of the Header Log register.<br/>For CXL RAS Capability Version <3, the position of the M2S RwD or S2M DRS Data Header in the Header Log register is not defined by this specification. — 内部不可纠正字节使能奇偶校验错误或 CXL.mem 上的其他字节使能不可纠正错误。如果由主机或 DSP 检测到，则 Header Log 寄存器包含 M2S RwD 数据头。<br/>对于 CXL RAS Capability Version >=3，Header Log 寄存器的 DWORD 0 保留，数据头应从 Header Log 寄存器的 Byte Offset 4 开始。<br/>对于 CXL RAS Capability Version <3，本规范未定义 Header Log 寄存器中 M2S RwD 或 S2M DRS 数据头的位置。 |
> | 7 | RW1CS | **Mem_Data_ECC**: Internal Uncorrectable Data ECC error on CXL.mem. The Header Log register contains the M2S RwD Data Header if detected by either a host or a DSP. The Header Log register contains the S2M DRS Data header if detected by either a device or a USP.<br/>Note: For CXL RAS Capability Version <3, it is permissible to log any Uncorrectable Data error on CXL.mem in Bit 4 and not in this bit.<br/>For CXL RAS Capability Version >=3, this bit is deprecated and all Uncorrectable Data errors on CXL.mem that are not signaled by using CXL poison are logged in bit 4.<br/>For CXL RAS Capability Version <3, the position of the Data Header in the Header Log register is not defined by this specification. — CXL.mem 上内部不可纠正数据 ECC 错误。如果由主机或 DSP 检测到，则 Header Log 寄存器包含 M2S RwD 数据头。如果由设备或 USP 检测到，则 Header Log 寄存器包含 S2M DRS 数据头。<br/>注意：对于 CXL RAS Capability Version <3，允许将 CXL.mem 上的任何不可纠正数据错误记录在 Bit 4 而不是此位中。<br/>对于 CXL RAS Capability Version >=3，此位已弃用，CXL.mem 上未通过使用 CXL poison 指示的所有不可纠正数据错误均记录在 bit 4 中。<br/>对于 CXL RAS Capability Version <3，本规范未定义数据头在 Header Log 寄存器中的位置。 |
> | 8 | RW1CS/RsvdZ | **REINIT_Threshold**: REINIT Threshold Hit (i.e., (NUM_PHY_REINIT >= MAX_NUM_PHY_REINIT). See Section 4.2.8.5.1 for the definitions of NUM_PHY_REINIT and MAX_NUM_PHY_REINIT. Header Log is not applicable. No data is logged in the Header Log.<br/>This bit is reserved for 256B Flit mode. — REINIT 阈值命中 (即 (NUM_PHY_REINIT >= MAX_NUM_PHY_REINIT)。有关 NUM_PHY_REINIT 和 MAX_NUM_PHY_REINIT 的定义，请参见 4.2.8.5.1 节。Header Log 不适用。Header Log 中不记录任何数据。<br/>对于 256B Flit 模式，此位保留。 |
> | 9 | RW1CS | **Rsvd_Encoding_Violation**: Received unrecognized encoding. Header Log contains the entire flit received when operating in 68B Flit mode. This bit should be set upon a Link-Layer-related encoding violation.<br/>For CXL RAS Capability Version <3 and operating in 68B Flit mode, the scope of encoding checking should include the scope where it falls into the "Reserved" or "RSVD" definitions in Table 4-5, Table 4-6, and Table 4-9.<br/>For CXL RAS Capability Version >=3 and operating in 68B Flit mode, the scope of checking shall include the encodings that are marked as "Reserved" or "RSVD" in Table 4-5, Table 4-6, Table 4-9, and Table 4-10.<br/>For CXL RAS Capability Version <3 and operating in 256B Flit mode, the content of the Header Log register is not defined by this specification.<br/>For CXL RAS Capability Version >=3 and operating in 256B Flit mode, the scope of checking shall include the encodings that are marked as "Reserved" or "RSVD" in Table 4-14, Table 4-15, Table 4-16, Table 4-19, and Table 4-20. In these cases, DWORD 0 of the Header Log register must be either 0 or 1. The component is permitted to log other unsupported encodings beyond what is required by this specification. In that scenario, DWORD 0 must be set to 2. DWORD 0 of the Header Log register indicates what is captured in the remaining DWORDs.<br/>• DWORD 0 = 0: DWORD 1 of the Header Log register shall contain the first DWORD in the offending slot<br/>• DWORD 0 = 1: The lower 16 bits of DWORD 1 of the Header Log register shall contain the Credit field<br/>• DWORD 0 = 2: The layout of the remaining DWORDs in the Header Log register is vendor specific — 接收到无法识别的编码。在 68B Flit 模式下运行时，Header Log 包含接收到的整个 flit。在发生链路层相关编码违规时应设置此位。<br/>对于 CXL RAS Capability Version <3 并在 68B Flit 模式下运行，编码检查的范围应包括表 4-5、表 4-6 和表 4-9 中属于 "Reserved" 或 "RSVD" 定义的范围。<br/>对于 CXL RAS Capability Version >=3 并在 68B Flit 模式下运行，检查范围应包括表 4-5、表 4-6、表 4-9 和表 4-10 中标记为 "Reserved" 或 "RSVD" 的编码。<br/>对于 CXL RAS Capability Version <3 并在 256B Flit 模式下运行，Header Log 寄存器的内容由本规范未定义。<br/>对于 CXL RAS Capability Version >=3 并在 256B Flit 模式下运行，检查范围应包括表 4-14、表 4-15、表 4-16、表 4-19 和表 4-20 中标记为 "Reserved" 或 "RSVD" 的编码。在这些情况下，Header Log 寄存器的 DWORD 0 必须为 0 或 1。允许组件在本规范要求之外记录其他不支持的编码。在这种情况下，DWORD 0 必须设置为 2。Header Log 寄存器的 DWORD 0 指示其余 DWORD 中捕获的内容。<br/>• DWORD 0 = 0：Header Log 寄存器的 DWORD 1 应包含问题 slot 中的第一个 DWORD<br/>• DWORD 0 = 1：Header Log 寄存器的 DWORD 1 的低 16 位应包含 Credit 字段<br/>• DWORD 0 = 2：Header Log 寄存器中其余 DWORD 的布局由厂商特定 |
> | 10 | RW1CS | **Poison_Received**: Received Poison from the peer. No data is logged in the Header Log. — 从对端接收到 Poison。Header Log 中不记录任何数据。 |
> | 11 | RW1CS | **Receiver_Overflow**<br/>• 0 = A buffer did not overflow<br/>• 1 = A buffer overflowed and the receiver of messages is unable to sink a message<br/>The first four bits of DWORD 0 of the Header Log register indicate which buffer overflowed, and should be interpreted as follows:<br/>• 0000b --> D2H Req (Applicable to the Downstream Port)<br/>• 0001b --> D2H Rsp (Applicable to the Downstream Port)<br/>• 0010b --> D2H Data (Applicable to the Downstream Port)<br/>• 0011b --> M2S Req (Applicable to the Upstream Port)<br/>• 0100b --> S2M NDR (Applicable to the Downstream Port)<br/>• 0101b --> S2M DRS (Applicable to the Downstream Port)<br/>• 0110b --> H2D Req (Applicable to the Upstream Port)<br/>• 0111b --> H2D Rsp (Applicable to the Upstream Port)<br/>• 1000b --> H2D Data (Applicable to the Upstream Port)<br/>• 1001b --> M2S RwD (Applicable to the Upstream Port)<br/>• 1010b --> BISnp (Applicable to the Downstream Port)<br/>• 1011b --> BIRsp (Applicable to the Upstream Port)<br/>• All other encodings are reserved<br/>Bits [31:4] of DWORD 0 are reserved. — 接收方溢出<br/>• 0 = 缓冲区未溢出<br/>• 1 = 缓冲区溢出，消息接收方无法接收消息<br/>Header Log 寄存器的 DWORD 0 的前 4 位指示哪个缓冲区溢出，应按以下方式解释：<br/>• 0000b --> D2H Req (适用于 Downstream Port)<br/>• 0001b --> D2H Rsp (适用于 Downstream Port)<br/>• 0010b --> D2H Data (适用于 Downstream Port)<br/>• 0011b --> M2S Req (适用于 Upstream Port)<br/>• 0100b --> S2M NDR (适用于 Downstream Port)<br/>• 0101b --> S2M DRS (适用于 Downstream Port)<br/>• 0110b --> H2D Req (适用于 Upstream Port)<br/>• 0111b --> H2D Rsp (适用于 Upstream Port)<br/>• 1000b --> H2D Data (适用于 Upstream Port)<br/>• 1001b --> M2S RwD (适用于 Upstream Port)<br/>• 1010b --> BISnp (适用于 Downstream Port)<br/>• 1011b --> BIRsp (适用于 Upstream Port)<br/>• 所有其他编码保留<br/>DWORD 0 的 Bits [31:4] 保留。 |
> | 13:12 | RsvdZ | Reserved (Do not use) — 保留 (请勿使用) |
> | 14 | RW1CS | **Internal_Error**: Component-specific error. The format of the Header Log is component-specific. — 组件特定错误。Header Log 的格式由组件特定。 |
> | 15 | RW1CS | **CXL_IDE_Tx_Error**: See Section 8.2.4.22.4 for the next level details. No data is logged in the Header Log.¹ — 详见 8.2.4.22.4 节。Header Log 中不记录任何数据。¹ |
> | 16 | RW1CS | **CXL_IDE_Rx_Error**: See Section 8.2.4.22.4 for the next level details.¹<br/>For CXL RAS Capability Version <3, no data is logged in the Header Log.<br/>For CXL RAS Capability Version >=3, DWORD 0 defines the content of subsequent DWORDs.<br/>If DWORD 0 is 0 (applies to Rx Error Status=6h)<br/>• DWORD 1: Current Idle Flit count<br/>• DWORD 2: Expected Idle Flit count after early MAC termination<br/>• All other DWORDs are reserved<br/>If DWORD 0 is 1 (applies to Rx Error Status=7h)<br/>• DWORD 1: Current Idle Flit count<br/>• DWORD 2: Expected Idle Flit count after Key Refresh<br/>• All other DWORDs are reserved<br/>If DWORD 0 is 2 (applies to Rx Error Status=7h)<br/>• DWORD 1: Current Idle Flit count<br/>• DWORD 2: Expected Idle Flit count after IDE termination handshake<br/>• All other DWORDs are reserved<br/>All other DWORD 0 values are reserved. — 详见 8.2.4.22.4 节。¹<br/>对于 CXL RAS Capability Version <3，Header Log 中不记录任何数据。<br/>对于 CXL RAS Capability Version >=3，DWORD 0 定义后续 DWORD 的内容。<br/>如果 DWORD 0 为 0 (适用于 Rx Error Status=6h)<br/>• DWORD 1：当前 Idle Flit 计数<br/>• DWORD 2：早期 MAC 终止后期望的 Idle Flit 计数<br/>• 所有其他 DWORD 保留<br/>如果 DWORD 0 为 1 (适用于 Rx Error Status=7h)<br/>• DWORD 1：当前 Idle Flit 计数<br/>• DWORD 2：Key Refresh 后期望的 Idle Flit 计数<br/>• 所有其他 DWORD 保留<br/>如果 DWORD 0 为 2 (适用于 Rx Error Status=7h)<br/>• DWORD 1：当前 Idle Flit 计数<br/>• DWORD 2：IDE 终止握手后期望的 Idle Flit 计数<br/>• 所有其他 DWORD 保留<br/>所有其他 DWORD 0 值保留。 |
> | 17 | RW1CS | **Extended_Metadata Error**: An error associated with Extended Metadata field.²<br/>DWORD 0 of the Header Log register captures the type of error:<br/>• 0 = A Root Port in an Extended Metadata-aware host received unexpected Extended Metadata on S2M DRS.<br/>• 1 = An Extended Metadata-aware device received unexpected Extended Metadata on M2S RwD.<br/>• 2 = A Root Port in an Extended Metadata-aware host expected but did not receive Extended Metadata on S2M DRS.<br/>• 3 = An Extended Metadata-aware device expected but did not receive Extended Metadata on M2S RwD.<br/>DWORD 1 of the Header Log register contains the following:<br/>• Bits[15:0]: Tag field associated with the value of the transaction with the EMDErr.<br/>• Bits[17:16]: MetaField value of the transaction with the EMDErr.<br/>• Bits[19:18]: MetaValue value of the transaction with the EMDErr.<br/>• Bit[20]: Indicates that an EMD value was captured with the EMDErr and is stored in DWORD 1. Must be 0 if the Enable Extended Metadata Error Logging bit is 0.<br/>DWORD 2 of the Header Log register captures the Extended Metadata field value if bit[20] of DWORD 2[1] is 1. This bit must be 0 if the Enable Extended Metadata Error Logging bit is 0. — 与 Extended Metadata 字段关联的错误。²<br/>Header Log 寄存器的 DWORD 0 捕获错误类型：<br/>• 0 = Extended Metadata 感知主机中的根端口在 S2M DRS 上接收到意外的 Extended Metadata。<br/>• 1 = Extended Metadata 感知设备在 M2S RwD 上接收到意外的 Extended Metadata。<br/>• 2 = Extended Metadata 感知主机中的根端口预期但未在 S2M DRS 上接收到 Extended Metadata。<br/>• 3 = Extended Metadata 感知设备预期但未在 M2S RwD 上接收到 Extended Metadata。<br/>Header Log 寄存器的 DWORD 1 包含以下内容：<br/>• Bits[15:0]：与具有 EMDErr 的事务值关联的 Tag 字段。<br/>• Bits[17:16]：与具有 EMDErr 的事务的 MetaField 值。<br/>• Bits[19:18]：与具有 EMDErr 的事务的 MetaValue 值。<br/>• Bit[20]：指示已使用 EMDErr 捕获 EMD 值并将其存储在 DWORD 1 中。如果 Enable Extended Metadata Error Logging 位为 0，则必须为 0。<br/>Header Log 寄存器的 DWORD 2 捕获 Extended Metadata 字段值 (如果 DWORD 2[1] 的 bit[20] 为 1)。如果 Enable Extended Metadata Error Logging 位为 0，则此位必须为 0。 |
> | 31:18 | RsvdZ | Reserved — 保留 |
>
> 1. Introduced as part of Version=2.
> 2. Introduced as part of Version=3.
> 1. 在 Version=2 中引入。
> 2. 在 Version=3 中引入。

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-17-2"></a>
#### 8.2.4.17.2 Uncorrectable Error Mask Register (Offset 04h) | 不可纠正错误屏蔽寄存器 (偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Uncorrectable Error Mask register controls reporting of individual errors. When a bit is set, the corresponding error status bit in Uncorrectable Error Status register upon the error event is not set, the error is not recorded or reported in the Header Log and is not signaled.</td><td style="background-color:#e8e8e8">不可纠正错误屏蔽寄存器控制各个错误的上报。某位置 1 时，错误事件发生时不可纠正错误状态寄存器中相应的错误状态位不会置位，错误不会在 Header Log 中记录或上报，也不会发出信号。</td></tr>
</tbody>
</table>

> **Table 8-74.** Uncorrectable Error Mask Register (Offset 04h) ｜ 不可纠正错误屏蔽寄存器 (偏移 04h)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RWS | **Cache_Data_Parity_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 1 | RWS | **Cache_Address_Parity_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 2 | RWS | **Cache_BE_Parity_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 3 | RWS | **Cache_Data_ECC_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 4 | RWS | **Mem_Data_Parity_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 5 | RWS | **Mem_Address_Parity_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 6 | RWS | **Mem_BE_Parity_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 7 | RWS | **Mem_Data_ECC_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 8 | RWS/RsvdP | **REINIT_Threshold_Mask**<br/>Default value for this bit is 1. This bit is reserved for 256B Flit mode. — 默认值为 1。对于 256B Flit 模式，此位保留。 |
> | 9 | RWS | **Rsvd_Encoding_Violation_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 10 | RWS | **Poison_Received_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 11 | RWS | **Receiver_Overflow_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 13:12 | RsvdP | Reserved (Do not use) — 保留 (请勿使用) |
> | 14 | RWS | **Internal_Error_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 15 | RWS | **CXL_IDE_Tx_Mask**¹<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 16 | RWS | **CXL_IDE_Rx_Mask**¹<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 17 | RWS | **Extended_Meta_Data_Error_Mask**²<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 31:18 | RsvdP | Reserved — 保留 |
>
> 1. Introduced as part of Version=2.
> 2. Introduced as part of Version=3.

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-17-3"></a>
#### 8.2.4.17.3 Uncorrectable Error Severity Register (Offset 08h) | 不可纠正错误严重性寄存器 (偏移 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Uncorrectable Error Severity register controls whether an individual error is considered Non-fatal or Fatal error. An error is considered fatal uncorrectable when the corresponding error bit in the severity register is Set. If an error is considered fatal and viral is enabled, a Viral indication shall be generated (see Section 12.4). If the bit is Cleared, the corresponding error is considered non-fatal uncorrectable and shall not trigger a Viral indication. This register does not control whether an error is signaled as ERR_FATAL or ERR_NONFATAL over CXL.io.</td><td style="background-color:#e8e8e8">不可纠正错误严重性寄存器控制单个错误是视为 Non-fatal 还是 Fatal 错误。当严重性寄存器中相应的错误位置 1 时，该错误被视为致命的不可纠正错误。如果错误被视为致命错误并且启用了 viral，则应生成 Viral 指示 (见 12.4 节)。如果该位清零，则相应的错误被视为非致命的不可纠正错误，并且不会触发 Viral 指示。此寄存器不控制错误是否通过 CXL.io 发出 ERR_FATAL 或 ERR_NONFATAL 信号。</td></tr>
</tbody>
</table>

> **Table 8-75.** Uncorrectable Error Severity Register (Offset 08h) ｜ 不可纠正错误严重性寄存器 (偏移 08h)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RWS | **Cache_Data_Parity_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 1 | RWS | **Cache_Address_Parity_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 2 | RWS | **Cache_BE_Parity_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 3 | RWS | **Cache_Data_ECC_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 4 | RWS | **Mem_Data_Parity_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 5 | RWS | **Mem_Address_Parity_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 6 | RWS | **Mem_BE_Parity_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 7 | RWS | **Mem_Data_ECC_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 8 | RWS/RsvdP | **REINIT_Threshold_Severity**<br/>Default value for this bit is 1. This bit is reserved for 256B Flit mode. — 默认值为 1。对于 256B Flit 模式，此位保留。 |
> | 9 | RWS | **Rsvd_Encoding_Violation_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 10 | RWS | **Poison_Received_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 11 | RWS | **Receiver_Overflow_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 13:12 | RsvdP | Reserved (Do not use) — 保留 (请勿使用) |
> | 14 | RWS | **Internal_Error_Severity**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 15 | RWS | **CXL_IDE_Tx_Severity**¹<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 16 | RWS | **CXL_IDE_Rx_Severity**¹<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 17 | RWS | **Extended_Meta_Data_Error_Severity**²<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 31:18 | RsvdP | Reserved — 保留 |
>
> 1. Introduced as part of Version=2.
> 2. Introduced as part of Version=3.

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-17-4"></a>
#### 8.2.4.17.4 Correctable Error Status Register (Offset 0Ch) | 可纠正错误状态寄存器 (偏移 0Ch)

> **Table 8-76.** Correctable Error Status Register (Offset 0Ch) ｜ 可纠正错误状态寄存器 (偏移 0Ch)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RW1CS | **Cache_Data_ECC**: Internal correctable error such as correctable Data ECC error on CXL.cache. — 内部可纠正错误，例如 CXL.cache 上的可纠正数据 ECC 错误。 |
> | 1 | RW1CS | **Mem_Data_ECC**: Internal correctable error such as correctable Data ECC error on CXL.mem. — 内部可纠正错误，例如 CXL.mem 上的可纠正数据 ECC 错误。 |
> | 2 | RW1CS/RsvdZ | **CRC_Threshold**: CRC Threshold Hit. The CRC threshold is component specific. Applicable only to 68B Flit mode. Reserved for 256B Flit mode. — CRC 阈值命中。CRC 阈值由组件特定。仅适用于 68B Flit 模式。对于 256B Flit 模式保留。 |
> | 3 | RW1CS/RsvdZ | **Retry_Threshold**: Retry Threshold Hit. (NUM_RETRY>= MAX_NUM_RETRY). See Section 4.2.8.5.1 for the definitions of NUM_RETRY and MAX_NUM_RETRY. Applicable only to 68B Flit mode. Reserved for 256B Flit mode. — 重试阈值命中 (NUM_RETRY>= MAX_NUM_RETRY)。有关 NUM_RETRY 和 MAX_NUM_RETRY 的定义，请参见 4.2.8.5.1 节。仅适用于 68B Flit 模式。对于 256B Flit 模式保留。 |
> | 4 | RW1CS | **Cache_Poison_Received**: Received Poison from the peer on CXL.cache. — 在 CXL.cache 上从对端接收到 Poison。 |
> | 5 | RW1CS | **Mem_Poison_Received**: Received Poison from the peer on CXL.mem. — 在 CXL.mem 上从对端接收到 Poison。 |
> | 6 | RW1CS | **Physical_Layer_Error**: Received error indication from Physical Layer. The error indication may or may not be associated with a CXL.cachemem flit. — 从物理层接收到错误指示。该错误指示可能与 CXL.cachemem flit 相关，也可能无关。 |
> | 31:7 | RsvdZ | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

<a id="sec-8-2-4-17-5"></a>
#### 8.2.4.17.5 Correctable Error Mask Register (Offset 10h) | 可纠正错误屏蔽寄存器 (偏移 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Correctable Error Mask register controls reporting of individual errors. When a bit is set in this register, the corresponding error status bit is not set upon the error event, and the error is not signaled.</td><td style="background-color:#e8e8e8">可纠正错误屏蔽寄存器控制各个错误的上报。此寄存器中某位置 1 时，错误事件发生时相应的错误状态位不会置位，错误也不会发出信号。</td></tr>
</tbody>
</table>

> **Table 8-77.** Correctable Error Mask Register (Offset 10h) ｜ 可纠正错误屏蔽寄存器 (偏移 10h)
>
> | Bit Location | Attributes | Description / 描述 |
> |---|---|---|
> | 0 | RWS | **Cache_Data_ECC_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 1 | RWS | **Mem_Data_ECC_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 2 | RWS | **CRC_Threshold_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 3 | RWS | **Retry_Threshold_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 4 | RWS | **Cache_Poison_Received_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 5 | RWS | **Mem_Poison_Received_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 6 | RWS | **Physical_Layer_Error_Mask**<br/>Default value for this bit is 1. — 默认值为 1。 |
> | 31:7 | RsvdP | Reserved — 保留 |

[⬆️ 返回目录](#-本章目录-part-a)

---

*To be continued in Part B (p.556+)*




