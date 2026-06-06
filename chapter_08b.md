# 📘 第 8 章　控制与状态寄存器 (Chapter 8. Control and Status Registers) — Part B

> **Source pages**: 556–615 (Part B) | **File**: chapter_08b.md | **Format**: 中英对照双语

## 📑 本章目录 (Part B)

- [8.2.4.17.6 Error Capabilities and Control Register (Offset 14h)](#sec-8-2-4-17-6)
- [8.2.4.17.7 Header Log Registers (Offset 18h)](#sec-8-2-4-17-7)
- [8.2.4.18 CXL Security Capability Structure](#sec-8-2-4-18)
  - [8.2.4.18.1 CXL Security Policy Register (Offset 00h)](#sec-8-2-4-18-1)
- [8.2.4.19 CXL Link Capability Structure](#sec-8-2-4-19)
  - [8.2.4.19.1 CXL Link Layer Capability Register (Offset 00h)](#sec-8-2-4-19-1)
  - [8.2.4.19.2 CXL Link Layer Control and Status Register (Offset 08h)](#sec-8-2-4-19-2)
  - [8.2.4.19.3 CXL Link Layer Rx Credit Control Register (Offset 10h)](#sec-8-2-4-19-3)
  - [8.2.4.19.4 CXL Link Layer Rx Credit Return Status Register (Offset 18h)](#sec-8-2-4-19-4)
  - [8.2.4.19.5 CXL Link Layer Tx Credit Status Register (Offset 20h)](#sec-8-2-4-19-5)
  - [8.2.4.19.6 CXL Link Layer Ack Timer Control Register (Offset 28h)](#sec-8-2-4-19-6)
  - [8.2.4.19.7 CXL Link Layer Defeature Register (Offset 30h)](#sec-8-2-4-19-7)
  - [8.2.4.19.8 CXL Link Layer Rx Credit Control2 Register (Offset 38h)](#sec-8-2-4-19-8)
  - [8.2.4.19.9 CXL Link Layer Rx Credit Return Status2 Register (Offset 40h)](#sec-8-2-4-19-9)
  - [8.2.4.19.10 CXL Link Layer Tx Credit Status2 Register (Offset 48h)](#sec-8-2-4-19-10)
- [8.2.4.20 CXL HDM Decoder Capability Structure](#sec-8-2-4-20)
  - [8.2.4.20.1 CXL HDM Decoder Capability Register (Offset 00h)](#sec-8-2-4-20-1)
  - [8.2.4.20.2 CXL HDM Decoder Global Control Register (Offset 04h)](#sec-8-2-4-20-2)
  - [8.2.4.20.3 CXL HDM Decoder n Base Low Register (Offset 20h*n+10h)](#sec-8-2-4-20-3)
  - [8.2.4.20.4 CXL HDM Decoder n Base High Register (Offset 20h*n+14h)](#sec-8-2-4-20-4)
  - [8.2.4.20.5 CXL HDM Decoder n Size Low Register (Offset 20h*n+18h)](#sec-8-2-4-20-5)
  - [8.2.4.20.6 CXL HDM Decoder n Size High Register (Offset 20h*n+1Ch)](#sec-8-2-4-20-6)
  - [8.2.4.20.7 CXL HDM Decoder n Control Register (Offset 20h*n+20h)](#sec-8-2-4-20-7)
  - [8.2.4.20.8 CXL HDM Decoder n Target List Low Register (Offset 20h*n+24h)](#sec-8-2-4-20-8)
  - [8.2.4.20.9 CXL HDM Decoder n DPA Skip Low Register (Offset 20h*n+24h)](#sec-8-2-4-20-9)
  - [8.2.4.20.10 CXL HDM Decoder n Target List High Register (Offset 20h*n+28h)](#sec-8-2-4-20-10)
  - [8.2.4.20.11 CXL HDM Decoder n DPA Skip High Register (Offset 20h*n+28h)](#sec-8-2-4-20-11)
  - [8.2.4.20.12 CXL HDM Decoder n Target Port Mask Register](#sec-8-2-4-20-12)
  - [8.2.4.20.13 Lock Mechanism for HDM Decoder Registers](#sec-8-2-4-20-13)
- [8.2.4.21 CXL IDE Capability Structure](#sec-8-2-4-21)
- [8.2.4.22 CXL TSPER Capability Structure](#sec-8-2-4-22)
  - [8.2.4.22.1 TSPER Register Block](#sec-8-2-4-22-1)
  - [8.2.4.22.2 TSPER Capability Register (Offset 00h)](#sec-8-2-4-22-2)
  - [8.2.4.22.3 TSPER Enable Register (Offset 04h)](#sec-8-2-4-22-3)
  - [8.2.4.22.4 TSPER Timestamp Low Register (Offset 08h)](#sec-8-2-4-22-4)
  - [8.2.4.22.5 TSPER Timestamp High Register (Offset 0Ch)](#sec-8-2-4-22-5)
  - [8.2.4.22.6 TSPER Normal Reported Time Low Register (Offset 10h)](#sec-8-2-4-22-6)
  - [8.2.4.22.7 TSPER Normal Reported Time High Register (Offset 14h)](#sec-8-2-4-22-7)
  - [8.2.4.22.8 TSPER Error Reported Time Low Register (Offset 18h)](#sec-8-2-4-22-8)
  - [8.2.4.22.9 TSPER Error Reported Time High Register (Offset 1Ch)](#sec-8-2-4-22-9)
- [8.2.4.23 CXL ACPI Timer Register Block](#sec-8-2-4-23)
  - [8.2.4.23.1 ACPI Timer Control Register](#sec-8-2-4-23-1)
  - [8.2.4.23.2 ACPI Timer Status Register](#sec-8-2-4-23-2)
- [8.2.4.24 CXL RAS Register Block](#sec-8-2-4-24)
  - [8.2.4.24.1 CXL AER Register Block](#sec-8-2-4-24-1)
  - [8.2.4.24.2 CXL RAS Capability Structure](#sec-8-2-4-24-2)
  - [8.2.4.24.3 CXL RAS Error Log Register Block](#sec-8-2-4-24-3)
- [8.2.4.25 Non-CXL Function Map Register Block](#sec-8-2-4-25)
  - [8.2.4.25.1 Non-CXL Function Map Register (Offset 00h)](#sec-8-2-4-25-1)
- [8.2.4.26 CXL GFD Register Block](#sec-8-2-4-26)
  - [8.2.4.26.1 CXL GFD Capability Register (Offset 00h)](#sec-8-2-4-26-1)
  - [8.2.4.26.2 CXL GFD Configuration Register (Offset 04h)](#sec-8-2-4-26-2)
  - [8.2.4.26.3 CXL GFD Status Register (Offset 08h)](#sec-8-2-4-26-3)
- [8.2.4.27 CXL Reset Register Block](#sec-8-2-4-27)
  - [8.2.4.27.1 CXL Reset Capability Register (Offset 00h)](#sec-8-2-4-27-1)
  - [8.2.4.27.2 CXL Reset Control and Status Register (Offset 04h)](#sec-8-2-4-27-2)
  - [8.2.4.27.3 CXL Reset Timeout Range Register (Offset 08h)](#sec-8-2-4-27-3)
- [8.2.4.28 CXL Dynamic Capacity Event Log Register Block](#sec-8-2-4-28)
  - [8.2.4.28.1 CXL DC Event Log Capability Register (Offset 00h)](#sec-8-2-4-28-1)
  - [8.2.4.28.2 CXL DC Event Log Status Register (Offset 04h)](#sec-8-2-4-28-2)
  - [8.2.4.28.3 CXL DC Event Log Start Address Register (Offset 08h)](#sec-8-2-4-28-3)
  - [8.2.4.28.4 CXL DC Event Log Interrupt Mask and Pending Register (Offset 10h)](#sec-8-2-4-28-4)
- [8.2.4.29 CXL Memory Events Register Block](#sec-8-2-4-29)
  - [8.2.4.29.1 Memory Event Status Register (Offset 00h)](#sec-8-2-4-29-1)
  - [8.2.4.29.2 Memory Event Interrupt Enable Register (Offset 04h)](#sec-8-2-4-29-2)
  - [8.2.4.29.3 Memory Event Control Register (Offset 08h)](#sec-8-2-4-29-3)
- [8.2.4.30 CXL PMU Register Block](#sec-8-2-4-30)
- [8.2.4.31 CXL Security Extension Register Block](#sec-8-2-4-31)
  - [8.2.4.31.1 CXL Security Extensions Capability Register (Offset 00h)](#sec-8-2-4-31-1)
  - [8.2.4.31.2 CXL Security Extensions Control Register (Offset 04h)](#sec-8-2-4-31-2)
- [8.2.5 Mailbox Registers](#sec-8-2-5)
  - [8.2.5.1 Mailbox Capabilities Register (Offset 00h)](#sec-8-2-5-1)
  - [8.2.5.2 Mailbox Control Register (Offset 04h)](#sec-8-2-5-2)
  - [8.2.5.3 Mailbox Status Register (Offset 08h)](#sec-8-2-5-3)
  - [8.2.5.4 Mailbox Payload Register (Offset 0Ch)](#sec-8-2-5-4)
  - [8.2.5.5 Mailbox Background Operation Status Register (Offset 10h)](#sec-8-2-5-5)
- [8.2.6 Event Timers](#sec-8-2-6)
  - [8.2.6.1 CXL Cache/Mem Event Timer](#sec-8-2-6-1)
    - [8.2.6.1.1 CXL Cache Event Timer Register (Offset 00h)](#sec-8-2-6-1-1)
    - [8.2.6.1.2 CXL Memory Event Timer Register (Offset 04h)](#sec-8-2-6-1-2)
- [8.2.7 CXL.cache MFVS Register Block](#sec-8-2-7)
  - [8.2.7.1 CXL.cache MFVS Register Block](#sec-8-2-7-1)
    - [8.2.7.1.1 CXL.cache MFVS Capability Register (Offset 00h)](#sec-8-2-7-1-1)
    - [8.2.7.1.2 CXL.cache MFVS Control Register (Offset 04h)](#sec-8-2-7-1-2)
    - [8.2.7.1.3 CXL.cache MFVS Status Register (Offset 08h)](#sec-8-2-7-1-3)
    - [8.2.7.1.4 CXL.cache MFVS Range Size Register (Offset 0Ch)](#sec-8-2-7-1-4)
  - [8.2.7.2 CXL.cache MLD Register Block](#sec-8-2-7-2)
    - [8.2.7.2.1 CXL.cache MLD Capability Register (Offset 00h)](#sec-8-2-7-2-1)
    - [8.2.7.2.2 CXL.cache MLD Control Register (Offset 04h)](#sec-8-2-7-2-2)
    - [8.2.7.2.3 CXL.cache MLD Status Register (Offset 08h)](#sec-8-2-7-2-3)
- [8.2.8 CXL.mem MFVS Register Block](#sec-8-2-8)
  - [8.2.8.1 CXL.mem MFVS Register Block](#sec-8-2-8-1)
  - [8.2.8.2 CXL.mem MLD Register Block](#sec-8-2-8-2)
  - [8.2.8.3 QTG_ID_MAP Register Block](#sec-8-2-8-3)

## 🖼 本章图表 (Part B)

| Page | Image | Description |
|------|-------|-------------|
| p.556 | [page_0556.png](figures/chapter_08/page_0556.png) | Page 556 image |
| p.557 | [page_0557.png](figures/chapter_08/page_0557.png) | Page 557 image |
| ... | ... | ... |

> 注: 每页原始 PDF 已抽取为 PNG, 嵌入位置依据各小节内容在源文档中的页码而定。

## 📊 本章表格 (Part B)

- Table 8-26: Device Trust Level
- Table 8-27: CXL.mem Read Response - Error Cases
- Table 8-28: Decoding of ConfNum for Mask Lock
- Table 8-29: HDM Decoder n Target Port Mask Bit Definition
- Table 8-30: CXL IDE Capability Structure
- Table 8-31: Mailbox Background Operation Status Register
- Table 8-32: Event Timer Encoding
- Table 8-33: Filter ID Encodings
- Table 8-34: CXL.mem MLD Registers
- Table 8-35: CXL.mem MFVS Registers
- Table 8-36: QTG_ID_MAP Register Block Encodings
- Table 8-37: QTG to Memory Device Mapping Encodings

---

<a id="sec-8-2-4-17-6"></a>
## 8.2.4.17.6 Error Capabilities and Control Register (Offset 14h) | 错误能力与控制寄存器 (偏移量 14h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 5:0 | ROS | First_Error_Pointer: This identifies the bit position of the first error reported in the Uncorrectable Error Status register. |
| 8:6 | RsvdP | Reserved |
| 9 | RO | Multiple_Header_Recording_Capability: If this bit is set, it indicates if recording of more than one error header is supported. |
| 12:10 | RsvdP | Reserved |
| 13 | RWS | Poison_Enabled: If this bit is 0, the CXL port shall treat poison received on CXL.cache or CXL.mem as an uncorrectable error and log the error in the Uncorrectable Error Status register. If this bit is 1, the CXL ports shall treat poison received on CXL.cache or CXL.mem as a correctable error and log the error in the Correctable Error Status register. This bit defaults to 1. This bit is hardwired to 1 in CXL Upstream Switch Port, CXL Downstream Switch Port, and CXL devices that are not eRCDs. |
| 31:14 | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 5:0 | ROS | First_Error_Pointer: 标识在 Uncorrectable Error Status 寄存器中报告的第一个错误的位位置。 |
| 8:6 | RsvdP | 保留 |
| 9 | RO | Multiple_Header_Recording_Capability: 如果该位置位, 表示支持记录多个错误头。 |
| 12:10 | RsvdP | 保留 |
| 13 | RWS | Poison_Enabled: 如果该位为 0, CXL 端口应将在 CXL.cache 或 CXL.mem 上收到的 Poison 视为不可纠正错误, 并将错误记录在 Uncorrectable Error Status 寄存器中。如果该位为 1, CXL 端口应将在 CXL.cache 或 CXL.mem 上收到的 Poison 视为可纠正错误, 并将错误记录在 Correctable Error Status 寄存器中。该位默认为 1。在 CXL 上行交换机端口 (Upstream Switch Port)、CXL 下行交换机端口 (Downstream Switch Port) 以及非 eRCD 的 CXL 设备中, 该位硬连线为 1。 |
| 31:14 | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-26.** Error Capabilities and Control Register layout ｜ 错误能力与控制寄存器布局
>
> <img src="figures/chapter_08/page_0556.png" alt="Figure 8-26" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0556.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-17-7"></a>
## 8.2.4.17.7 Header Log Registers (Offset 18h) | 头日志寄存器 (偏移量 18h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Header Log registers are accessed as a series of 32-bit wide individual registers even though it is represented as a single 512-bit long entity for convenience. In accordance with Section 8.2.2, each individual register shall be accessed as an aligned 4-Byte quantity.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 511:0 | ROS | Header Log: The information logged here depends on the type of Uncorrectable Error Status bit recorded as described in Section 8.2.4.17.1. If multiple errors are logged in the Uncorrectable Error Status register, the First_Error_Pointer field in the Error Capabilities and Control register identifies the error that this log corresponds to. |

</td><td style="background-color:#e8e8e8">

头日志 (Header Log) 寄存器虽然为了方便起见表示为单个 512 位长的实体, 但作为一系列 32 位宽的单独寄存器进行访问。根据第 8.2.2 节的规定, 每个单独寄存器应作为对齐的 4 字节量进行访问。

| 位域 | 属性 | 描述 |
|------|------|------|
| 511:0 | ROS | Header Log: 此处记录的信息取决于第 8.2.4.17.1 节中描述的已记录 Uncorrectable Error Status 位的类型。如果在 Uncorrectable Error Status 寄存器中记录了多个错误, 则 Error Capabilities and Control 寄存器中的 First_Error_Pointer 字段标识该日志所对应的错误。 |

</td></tr>
</tbody>
</table>

> **Figure 8-27.** Header Log Register layout ｜ 头日志寄存器布局
>
> <img src="figures/chapter_08/page_0556.png" alt="Figure 8-27" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0556.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-18"></a>
## 8.2.4.18 CXL Security Capability Structure | CXL 安全能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This capability structure applies only for RCH Downstream Ports.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Security Policy Register |

</td><td style="background-color:#e8e8e8">

此能力结构仅适用于 RCH 下行端口 (RCH Downstream Port)。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Security Policy Register |

</td></tr>
</tbody>
</table>

> **Figure 8-28.** CXL Security Capability Structure layout ｜ CXL 安全能力结构布局
>
> <img src="figures/chapter_08/page_0557.png" alt="Figure 8-28" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0557.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-18-1"></a>
## 8.2.4.18.1 CXL Security Policy Register (Offset 00h) | CXL 安全策略寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 1:0 | RW | Device Trust Level |
| | | • 00b = Trusted CXL device. At this setting, a CXL device will be able to get access on CXL.cache for both host-attached and device-attached memory ranges. The Host can still protect security sensitive memory regions. |
| | | • 01b = Trusted for device-attached Memory Range Only. At this setting, a CXL device will be able to get access on CXL.cache for device-attached memory ranges only. Requests on CXL.cache for host-attached memory ranges will be aborted by the Host. |
| | | • 10b = Untrusted CXL device. At this setting, all requests on CXL.cache will be aborted by the Host. |
| | | Note: These settings only apply to requests on CXL.cache. The device can still source requests on CXL.io regardless of these settings. Protection on CXL.io will be implemented using IOMMU-based page tables. |
| | | Default value of this field is 10b. |
| 31:2 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 1:0 | RW | 设备信任等级 (Device Trust Level) |
| | | • 00b = 可信的 CXL 设备 (Trusted CXL device)。在此设置下, CXL 设备将能够访问 CXL.cache 上的主机端附加内存范围和设备端附加内存范围。主机仍可保护安全敏感的内存区域。 |
| | | • 01b = 仅信任设备端附加内存范围 (Trusted for device-attached Memory Range Only)。在此设置下, CXL 设备将只能访问 CXL.cache 上的设备端附加内存范围。对主机端附加内存范围的 CXL.cache 请求将被主机中止。 |
| | | • 10b = 不可信 CXL 设备 (Untrusted CXL device)。在此设置下, CXL.cache 上的所有请求都将被主机中止。 |
| | | 注: 这些设置仅适用于 CXL.cache 上的请求。无论这些设置如何, 设备仍可在 CXL.io 上发起请求。CXL.io 上的保护将使用基于 IOMMU 的页表来实现。 |
| | | 此字段的默认值为 10b。 |
| 31:2 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Table 8-26.** Device Trust Level ｜ 设备信任等级
>
> <img src="figures/chapter_08/page_0557.png" alt="Table 8-26" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0557.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19"></a>
## 8.2.4.19 CXL Link Capability Structure | CXL 链路能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Link Layer Capability Register |
| 08h | CXL Link Control and Status Register |
| 10h | CXL Link Rx Credit Control Register |
| 18h | CXL Link Rx Credit Return Status Register |
| 20h | CXL Link Tx Credit Status Register |
| 28h | CXL Link Ack Timer Control Register |
| 30h | CXL Link Defeature Register |
| 38h | CXL Link Rx Credit Control2 Register |
| 40h | CXL Link Rx Credit Return Status2 Register |
| 48h | CXL Link Tx Credit Status2 Register |

</td><td style="background-color:#e8e8e8">

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Link Layer Capability Register |
| 08h | CXL Link Control and Status Register |
| 10h | CXL Link Rx Credit Control Register |
| 18h | CXL Link Rx Credit Return Status Register |
| 20h | CXL Link Tx Credit Status Register |
| 28h | CXL Link Ack Timer Control Register |
| 30h | CXL Link Defeature Register |
| 38h | CXL Link Rx Credit Control2 Register |
| 40h | CXL Link Rx Credit Return Status2 Register |
| 48h | CXL Link Tx Credit Status2 Register |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-1"></a>
## 8.2.4.19.1 CXL Link Layer Capability Register (Offset 00h) | CXL 链路层能力寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RWS | CXL Link Version Supported: The value in this field does not affect the link behavior. This field has been deprecated and software must not rely on its value. |
| 7:4 | RO | CXL Link Version Received: Version of CXL Specification received from INIT.Param flit. This field has been deprecated and software must not rely on its value. |
| 15:8 | RWS/RsvdP | LLR Wrap Value Supported: LLR Wrap value supported by this entity. Used for debug. The default value of this field will be implementation dependent. This field is reserved for 256B Flit mode. |
| 23:16 | RO/RsvdP | LLR Wrap Value Received: LLR Wrap value received from INIT.Param flit. Used for debug. This field is reserved for 256B Flit mode. |
| 28:24 | RO/RsvdP | NUM_Retry_Received: Num_Retry value reflected in the last RETRY.Req message received. Used for debug. This field is reserved for 256B Flit mode. |
| 33:29 | RO/RsvdP | NUM_Phy_Reinit_Received: Num_Phy_Reinit value reflected in the last RETRY.Req message received. Used for debug. This field is reserved for 256B Flit mode. |
| 41:34 | RO/RsvdP | Wr_Ptr_Received: Wr_Ptr value reflected in the last RETRY.Ack message received. This field is reserved for 256B Flit mode. |
| 49:42 | RO/RsvdP | Echo_Eseq_Received: Echo_Eseq value reflected in the last RETRY.Ack message received. This field is reserved for 256B Flit mode. |
| 57:50 | RO/RsvdP | Num_Free_Buf_Received: Num_Free_Buf value reflected in the last RETRY.Ack message received. This field is reserved for 256B Flit mode. |
| 58 | RO/RsvdP | No_LL_Reset_Support: If set, indicates that the LL_Reset configuration bit is not supported.¹ |
| 63:59 | RsvdP | Reserved |

¹ Introduced as part of Version=2.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RWS | CXL Link Version Supported: 此字段的值不影响链路行为。该字段已弃用, 软件不得依赖其值。 |
| 7:4 | RO | CXL Link Version Received: 从 INIT.Param Flit 接收到的 CXL 规范版本。该字段已弃用, 软件不得依赖其值。 |
| 15:8 | RWS/RsvdP | LLR Wrap Value Supported: 此实体支持的 LLR Wrap 值。用于调试。此字段的默认值取决于实现。对于 256B Flit 模式, 该字段保留。 |
| 23:16 | RO/RsvdP | LLR Wrap Value Received: 从 INIT.Param Flit 接收到的 LLR Wrap 值。用于调试。对于 256B Flit 模式, 该字段保留。 |
| 28:24 | RO/RsvdP | NUM_Retry_Received: 上次接收到的 RETRY.Req 消息中反映的 Num_Retry 值。用于调试。对于 256B Flit 模式, 该字段保留。 |
| 33:29 | RO/RsvdP | NUM_Phy_Reinit_Received: 上次接收到的 RETRY.Req 消息中反映的 Num_Phy_Reinit 值。用于调试。对于 256B Flit 模式, 该字段保留。 |
| 41:34 | RO/RsvdP | Wr_Ptr_Received: 上次接收到的 RETRY.Ack 消息中反映的 Wr_Ptr 值。对于 256B Flit 模式, 该字段保留。 |
| 49:42 | RO/RsvdP | Echo_Eseq_Received: 上次接收到的 RETRY.Ack 消息中反映的 Echo_Eseq 值。对于 256B Flit 模式, 该字段保留。 |
| 57:50 | RO/RsvdP | Num_Free_Buf_Received: 上次接收到的 RETRY.Ack 消息中反映的 Num_Free_Buf 值。对于 256B Flit 模式, 该字段保留。 |
| 58 | RO/RsvdP | No_LL_Reset_Support: 如果置位, 表示不支持 LL_Reset 配置位。¹ |
| 63:59 | RsvdP | 保留 |

¹ 作为 Version=2 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-29.** CXL Link Layer Capability Register layout ｜ CXL 链路层能力寄存器布局
>
> <img src="figures/chapter_08/page_0557.png" alt="Figure 8-29" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0557.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-2"></a>
## 8.2.4.19.2 CXL Link Layer Control and Status Register (Offset 08h) | CXL 链路层控制与状态寄存器 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW | LL_Reset: Re-initialize without resetting values in sticky registers. When this bit is set, the link layer reset is initiated. When link layer reset completes, hardware will clear the bit to 0. Entity triggering LL_Reset should ensure that link is quiesced. Support for this bit is optional. If LL_Reset is not supported, the NO_LL_Reset_Support bit in the CXL Link Layer Capability register shall be set (see Section 8.2.4.19.1). The use of this bit is expected to be for debug. Any production need for Link Layer re-initialization is to be satisfied using CXL Hot Reset. |
| 1 | RWS | LL_Init_Stall: If set, link layer stalls the transmission of the LLCTRL-INIT.Param flit until this bit is cleared. The default value of this bit is 0. |
| 2 | RWS | LL_Crd_Stall: If set, link layer stalls credit initialization until this bit is cleared. The reset default value of this bit is 0. |
| 4:3 | RO | INIT_State: This field reflects the current initialization status of the Link Layer, including any stall conditions controlled by bits 2:1:<br>• 00b = NOT_RDY_FOR_INIT (stalled or unstalled): LLCTRL-INIT.Param flit not sent<br>• 01b = PARAM_EX: LLCTRL-INIT.Param sent and waiting to receive it<br>• 10b = CRD_RETURN_STALL: Parameter exchanged successfully, and Credit return is stalled<br>• 11b = INIT_DONE: Link Initialization Done: LLCTRL-INIT.Param flit sent and received, and initial credit refund not stalled |
| 12:5 | RO/RsvdP | LL_Retry_Buffer_Consumed: Snapshot of link layer retry buffer consumed. This field is reserved for 256B Flit mode. |
| 63:13 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW | LL_Reset: 在不清除粘性寄存器值的情况下重新初始化。当该位置位时, 启动链路层复位。当链路层复位完成时, 硬件将该位清零。触发 LL_Reset 的实体应确保链路处于静止状态。该位的支持是可选的。如果不支持 LL_Reset, 则 CXL Link Layer Capability 寄存器中的 NO_LL_Reset_Support 位应置位 (参见第 8.2.4.19.1 节)。该位预期用于调试。任何对链路层重新初始化的生产需求都应通过 CXL 热复位 (Hot Reset) 来满足。 |
| 1 | RWS | LL_Init_Stall: 如果置位, 链路层将暂停 LLCTRL-INIT.Param Flit 的传输, 直到该位被清除。该位的默认值为 0。 |
| 2 | RWS | LL_Crd_Stall: 如果置位, 链路层将暂停信用初始化, 直到该位被清除。该位的复位默认值为 0。 |
| 4:3 | RO | INIT_State: 此字段反映链路层的当前初始化状态, 包括由位 2:1 控制的任何暂停条件:<br>• 00b = NOT_RDY_FOR_INIT (已暂停或未暂停): 未发送 LLCTRL-INIT.Param Flit<br>• 01b = PARAM_EX: 已发送 LLCTRL-INIT.Param, 等待接收<br>• 10b = CRD_RETURN_STALL: 参数交换成功, 信用返回暂停<br>• 11b = INIT_DONE: 链路初始化完成: LLCTRL-INIT.Param Flit 已发送和接收, 初始信用退还未暂停 |
| 12:5 | RO/RsvdP | LL_Retry_Buffer_Consumed: 已消耗链路层重试缓冲区的快照。对于 256B Flit 模式, 该字段保留。 |
| 63:13 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-30.** CXL Link Layer Control and Status Register layout ｜ CXL 链路层控制与状态寄存器布局
>
> <img src="figures/chapter_08/page_0558.png" alt="Figure 8-30" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0558.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-3"></a>
## 8.2.4.19.3 CXL Link Layer Rx Credit Control Register (Offset 10h) | CXL 链路层 Rx 信用控制寄存器 (偏移量 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The default settings are component specific. The contents of this register represent the credits advertised by the component.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 9:0 | RWS | Cache Req Credits: Credits to advertise for CXL.cache Request channel at init. For Upstream Port, this field represents the credits to advertise for CXL.cache H2D Req channel at init. For Downstream Port or Fabric Port, this field represents the credits to advertise for CXL.cache D2H Req channel at init. The default value represents the maximum number of CXL.cache Request channel credits that the component supports. |
| 19:10 | RWS | Cache Rsp Credits: Credits to advertise for CXL.cache Response channel at init. For Upstream Port, this field represents the credits to advertise for CXL.cache H2D Rsp channel at init. For Downstream Port or Fabric Port, this field represents the credits to advertise for CXL.cache D2H Rsp channel at init. The default value represents the maximum number of CXL.cache Response channel credits that the component supports. |
| 29:20 | RWS | Cache Data Credits: Credits to advertise for CXL.cache Data channel at init. For Upstream Port, this field represents the credits to advertise for CXL.cache H2D Data channel at init. For Downstream Port or Fabric Port, this field represents the credits to advertise for CXL.cache D2H Data channel at init. The default value represents the maximum number of CXL.cache Data channel credits that the component supports. |
| 39:30 | RWS | Mem Req_Rsp Credits: For an Upstream Port, this field represents the credits to advertise for CXL.mem Request channel at init. For a Downstream Port or Fabric Port, this field represents the credits to advertise for CXL.mem NDR channel at init. The default value represents the maximum number of credits that the port supports. |
| 49:40 | RWS | Mem Data Credits: Credits to advertise for CXL.mem Data channel at init. For an Upstream Port, this field represents the number of advertised RwD channel credits at init. For a Downstream Port or Fabric Port, this field represents the number of advertised DRS channel credits at init. The default value represents the maximum number of channel credits that the port supports. |
| 59:50 | RWS/RsvdP | BI Credits: For an Upstream Port, this field represents the number of advertised BIRsp channel credits at init. For a Downstream Port or Fabric Port, this field represents the number of advertised BISnp channel credits at init. The default value represents the maximum number of the appropriate Back-Invalidate channel credits of which the port is capable.¹ This field is reserved for 68B Flit mode and for components that do not support BI. |
| 63:60 | RsvdP | Reserved |

¹ Introduced as part of Version=3.

</td><td style="background-color:#e8e8e8">

默认设置是组件特定的。该寄存器的内容表示组件通告的信用。

| 位域 | 属性 | 描述 |
|------|------|------|
| 9:0 | RWS | Cache Req Credits: 初始化时为 CXL.cache 请求信道通告的信用。对于上行端口 (Upstream Port), 此字段表示初始化时为 CXL.cache H2D Req 信道通告的信用。对于下行端口 (Downstream Port) 或结构端口 (Fabric Port), 此字段表示初始化时为 CXL.cache D2H Req 信道通告的信用。默认值表示组件支持的 CXL.cache 请求信道最大信用数。 |
| 19:10 | RWS | Cache Rsp Credits: 初始化时为 CXL.cache 响应信道通告的信用。对于上行端口, 此字段表示初始化时为 CXL.cache H2D Rsp 信道通告的信用。对于下行端口或结构端口, 此字段表示初始化时为 CXL.cache D2H Rsp 信道通告的信用。默认值表示组件支持的 CXL.cache 响应信道最大信用数。 |
| 29:20 | RWS | Cache Data Credits: 初始化时为 CXL.cache 数据信道通告的信用。对于上行端口, 此字段表示初始化时为 CXL.cache H2D Data 信道通告的信用。对于下行端口或结构端口, 此字段表示初始化时为 CXL.cache D2H Data 信道通告的信用。默认值表示组件支持的 CXL.cache 数据信道最大信用数。 |
| 39:30 | RWS | Mem Req_Rsp Credits: 对于上行端口, 此字段表示初始化时为 CXL.mem 请求信道通告的信用。对于下行端口或结构端口, 此字段表示初始化时为 CXL.mem NDR 信道通告的信用。默认值表示端口支持的最大信用数。 |
| 49:40 | RWS | Mem Data Credits: 初始化时为 CXL.mem 数据信道通告的信用。对于上行端口, 此字段表示初始化时通告的 RwD 信道信用数。对于下行端口或结构端口, 此字段表示初始化时通告的 DRS 信道信用数。默认值表示端口支持的最大信道信用数。 |
| 59:50 | RWS/RsvdP | BI Credits: 对于上行端口, 此字段表示初始化时通告的 BIRsp 信道信用数。对于下行端口或结构端口, 此字段表示初始化时通告的 BISnp 信道信用数。默认值表示端口支持的最大相应 Back-Invalidate 信道信用数。¹ 该字段对于 68B Flit 模式以及不支持 BI 的组件保留。 |
| 63:60 | RsvdP | 保留 |

¹ 作为 Version=3 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-31.** CXL Link Layer Rx Credit Control Register layout ｜ CXL 链路层 Rx 信用控制寄存器布局
>
> <img src="figures/chapter_08/page_0559.png" alt="Figure 8-31" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0559.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-4"></a>
## 8.2.4.19.4 CXL Link Layer Rx Credit Return Status Register (Offset 18h) | CXL 链路层 Rx 信用返回状态寄存器 (偏移量 18h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 9:0 | RO | Cache Req Credits: Running snapshot of accumulated CXL.cache Request credits to be returned. For Upstream Port, this field represents the running snapshot of the accumulated CXL.cache H2D Req channel credits to be returned. For Downstream Port or Fabric Port, this field represents the running snapshot of the accumulated CXL.cache D2H Req channel credits to be returned. |
| 19:10 | RO | Cache Rsp Credits: Running snapshot of accumulated CXL.cache Response credits to be returned. For Upstream Port, this field represents the running snapshot of the accumulated CXL.cache H2D Rsp channel credits to be returned. For Downstream Port or Fabric Port, this field represents the running snapshot of the accumulated CXL.cache D2H Rsp channel credits to be returned. |
| 29:20 | RO | Cache Data Credits: Running snapshot of accumulated CXL.cache Data credits to be returned. For Upstream Port, this field represents the running snapshot of the accumulated CXL.cache H2D Data channel credits to be returned. For Downstream Port or Fabric Port, this field represents the running snapshot of the accumulated CXL.cache D2H Data channel credits to be returned. |
| 39:30 | RO | Mem Req_Rsp Credits: For an Upstream Port, this field represents the running snapshot of the accumulated CXL.mem Request channel credits to be returned. For a Downstream Port or Fabric Port, this field represents the running snapshot of the accumulated CXL.mem NDR channel credits to be returned. |
| 49:40 | RO | Mem Data Credits: Running snapshot of accumulated CXL.mem Data credits to be returned. For an Upstream Port, this field represents the running snapshot of the accumulated RwD channel credits to be returned. For a Downstream Port or Fabric Port, this field represents the running snapshot of the accumulated DRS channel credits to be returned. |
| 59:50 | RO/RsvdP | BI Credits: For an Upstream Port, this field represents the running snapshot of the accumulated BIRsp channel credits to be returned. For a Downstream Port or Fabric Port, this field represents the running snapshot of accumulated BISnp channel credits to be returned.¹ This field is reserved for 68B Flit mode and for components that do not support BI. |
| 63:60 | RsvdP | Reserved |

¹ Introduced as part of Version=3.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 9:0 | RO | Cache Req Credits: 要返回的累积 CXL.cache 请求信用的运行快照。对于上行端口, 此字段表示要返回的累积 CXL.cache H2D Req 信道信用的运行快照。对于下行端口或结构端口, 此字段表示要返回的累积 CXL.cache D2H Req 信道信用的运行快照。 |
| 19:10 | RO | Cache Rsp Credits: 要返回的累积 CXL.cache 响应信用的运行快照。对于上行端口, 此字段表示要返回的累积 CXL.cache H2D Rsp 信道信用的运行快照。对于下行端口或结构端口, 此字段表示要返回的累积 CXL.cache D2H Rsp 信道信用的运行快照。 |
| 29:20 | RO | Cache Data Credits: 要返回的累积 CXL.cache 数据信用的运行快照。对于上行端口, 此字段表示要返回的累积 CXL.cache H2D Data 信道信用的运行快照。对于下行端口或结构端口, 此字段表示要返回的累积 CXL.cache D2H Data 信道信用的运行快照。 |
| 39:30 | RO | Mem Req_Rsp Credits: 对于上行端口, 此字段表示要返回的累积 CXL.mem 请求信道信用的运行快照。对于下行端口或结构端口, 此字段表示要返回的累积 CXL.mem NDR 信道信用的运行快照。 |
| 49:40 | RO | Mem Data Credits: 要返回的累积 CXL.mem 数据信用的运行快照。对于上行端口, 此字段表示要返回的累积 RwD 信道信用的运行快照。对于下行端口或结构端口, 此字段表示要返回的累积 DRS 信道信用的运行快照。 |
| 59:50 | RO/RsvdP | BI Credits: 对于上行端口, 此字段表示要返回的累积 BIRsp 信道信用的运行快照。对于下行端口或结构端口, 此字段表示要返回的累积 BISnp 信道信用的运行快照。¹ 该字段对于 68B Flit 模式以及不支持 BI 的组件保留。 |
| 63:60 | RsvdP | 保留 |

¹ 作为 Version=3 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-32.** CXL Link Layer Rx Credit Return Status Register layout ｜ CXL 链路层 Rx 信用返回状态寄存器布局
>
> <img src="figures/chapter_08/page_0560.png" alt="Figure 8-32" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0560.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-5"></a>
## 8.2.4.19.5 CXL Link Layer Tx Credit Status Register (Offset 20h) | CXL 链路层 Tx 信用状态寄存器 (偏移量 20h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 9:0 | RO | Cache Req Credits: Running snapshot of CXL.cache Request credits for Tx. For Upstream Port, this field represents the running snapshot of the CXL.cache D2H Req channel credits for Tx. For Downstream Port or Fabric Port, this field represents the running snapshot of the CXL.cache H2D Req channel credits for Tx. |
| 19:10 | RO | Cache Rsp Credits: Running snapshot of CXL.cache Response credits for Tx. For Upstream Port, this field represents the running snapshot of the CXL.cache D2H Rsp channel credits for Tx. For Downstream Port or Fabric Port, this field represents the running snapshot of the CXL.cache H2D Rsp channel credits for Tx. |
| 29:20 | RO | Cache Data Credits: Running snapshot of CXL.cache Data credits for Tx. For Upstream Port, this field represents the running snapshot of the CXL.cache D2H Data channel credits for Tx. For Downstream Port or Fabric Port, this field represents the running snapshot of the CXL.cache H2D Data channel credits for Tx. |
| 39:30 | RO | Mem Req_Rsp Credits: For an Upstream Port, this field represents the running snapshot of the CXL.mem NDR channel credits for Tx. For a Downstream Port or Fabric Port, this field represents the running snapshot of the CXL.mem Request channel credits for Tx. |
| 49:40 | RO | Mem Data Credits: Running snapshot of CXL.mem Data credits for Tx. For an Upstream Port, this field represents the number of DRS channel credits for Tx. For a Downstream Port or Fabric Port, this field represents the number of RwD channel credits for Tx. |
| 59:50 | RO/RsvdP | BI Credits: For an Upstream Port, this field represents the running snapshot of the accumulated BISnp channel credits for Tx. For a Downstream Port or Fabric Port, this field represents the running snapshot of accumulated BIRsp channel credits for Tx.¹ This field is reserved for 68B Flit mode and for components that do not support BI. |
| 63:60 | RsvdP | Reserved |

¹ Introduced as part of Version=3.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 9:0 | RO | Cache Req Credits: Tx 的 CXL.cache 请求信用的运行快照。对于上行端口, 此字段表示 Tx 的 CXL.cache D2H Req 信道信用的运行快照。对于下行端口或结构端口, 此字段表示 Tx 的 CXL.cache H2D Req 信道信用的运行快照。 |
| 19:10 | RO | Cache Rsp Credits: Tx 的 CXL.cache 响应信用的运行快照。对于上行端口, 此字段表示 Tx 的 CXL.cache D2H Rsp 信道信用的运行快照。对于下行端口或结构端口, 此字段表示 Tx 的 CXL.cache H2D Rsp 信道信用的运行快照。 |
| 29:20 | RO | Cache Data Credits: Tx 的 CXL.cache 数据信用的运行快照。对于上行端口, 此字段表示 Tx 的 CXL.cache D2H Data 信道信用的运行快照。对于下行端口或结构端口, 此字段表示 Tx 的 CXL.cache H2D Data 信道信用的运行快照。 |
| 39:30 | RO | Mem Req_Rsp Credits: 对于上行端口, 此字段表示 Tx 的 CXL.mem NDR 信道信用的运行快照。对于下行端口或结构端口, 此字段表示 Tx 的 CXL.mem 请求信道信用的运行快照。 |
| 49:40 | RO | Mem Data Credits: Tx 的 CXL.mem 数据信用的运行快照。对于上行端口, 此字段表示 Tx 的 DRS 信道信用数。对于下行端口或结构端口, 此字段表示 Tx 的 RwD 信道信用数。 |
| 59:50 | RO/RsvdP | BI Credits: 对于上行端口, 此字段表示 Tx 的累积 BISnp 信道信用的运行快照。对于下行端口或结构端口, 此字段表示 Tx 的累积 BIRsp 信道信用的运行快照。¹ 该字段对于 68B Flit 模式以及不支持 BI 的组件保留。 |
| 63:60 | RsvdP | 保留 |

¹ 作为 Version=3 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-33.** CXL Link Layer Tx Credit Status Register layout ｜ CXL 链路层 Tx 信用状态寄存器布局
>
> <img src="figures/chapter_08/page_0561.png" alt="Figure 8-33" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0561.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-6"></a>
## 8.2.4.19.6 CXL Link Layer Ack Timer Control Register (Offset 28h) | CXL 链路层 Ack 定时器控制寄存器 (偏移量 28h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The default settings are component specific.

Software may program this register and issue a hot reset to operate the component with settings that are different from the default. The values in these registers take effect on the next hot reset.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 7:0 | RWS | Ack Force Threshold: This specifies how many Flit Acks the Link Layer should accumulate before injecting an LLCRD. The recommended default value is 10h (16 decimal). If configured to a value greater than (LLR Wrap Value Received - 6), the behavior will be undefined. If configured to a value below 10h, the behavior will be undefined. See Section 4.2.8.2 for additional details. |
| 17:8 | RWS | Ack or CRD Flush Retimer: This specifies how many link layer clock cycles the entity should wait in case of idle, before flushing accumulated Acks or CRD using an LLCRD. This applies for any case where accumulated Acks is greater than 1 or accumulated CRD for any channel is greater than 0. The recommended default value is 20h. If configured to a value below 20h, the behavior will be undefined. See Section 4.2.8.2 for additional details. |
| 63:18 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

默认设置是组件特定的。

软件可以编程此寄存器并发出热复位, 以使用与默认不同的设置来操作组件。这些寄存器中的值将在下一次热复位时生效。

| 位域 | 属性 | 描述 |
|------|------|------|
| 7:0 | RWS | Ack Force Threshold: 指定链路层在注入 LLCRD 之前应累积的 Flit Ack 数量。推荐的默认值为 10h (十进制 16)。如果配置为大于 (LLR Wrap Value Received - 6) 的值, 行为将是未定义的。如果配置为低于 10h 的值, 行为将是未定义的。有关更多详细信息, 请参见第 4.2.8.2 节。 |
| 17:8 | RWS | Ack or CRD Flush Retimer: 指定在空闲情况下, 实体在通过 LLCRD 刷新累积的 Ack 或 CRD 之前应等待的链路层时钟周期数。这适用于累积 Ack 大于 1 或任何信道的累积 CRD 大于 0 的任何情况。推荐的默认值为 20h。如果配置为低于 20h 的值, 行为将是未定义的。有关更多详细信息, 请参见第 4.2.8.2 节。 |
| 63:18 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-34.** CXL Link Layer Ack Timer Control Register layout ｜ CXL 链路层 Ack 定时器控制寄存器布局
>
> <img src="figures/chapter_08/page_0561.png" alt="Figure 8-34" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0561.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-7"></a>
## 8.2.4.19.7 CXL Link Layer Defeature Register (Offset 30h) | CXL 链路层功能禁用寄存器 (偏移量 30h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RWS/RsvdP | MDH Disable: Write 1 to disable MDH. Software needs to ensure it programs this value consistently on the Upstream Port and Downstream Port. After programming, a hot reset is required for the disable to take effect. The default value of this bit is 0. |
| 63:1 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RWS/RsvdP | MDH Disable: 写 1 以禁用 MDH。软件需要确保在上行端口和下行端口上一致地编程此值。编程后, 需要热复位才能使禁用生效。该位的默认值为 0。 |
| 63:1 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-35.** CXL Link Layer Defeature Register layout ｜ CXL 链路层功能禁用寄存器布局
>
> <img src="figures/chapter_08/page_0562.png" alt="Figure 8-35" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0562.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-8"></a>
## 8.2.4.19.8 CXL Link Layer Rx Credit Control2 Register (Offset 38h) | CXL 链路层 Rx 信用控制 2 寄存器 (偏移量 38h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

¹ This register was introduced as part of Version=4.
² This field was introduced as part of Version=4.

| Bit Location | Attributes | Description¹ |
|--------------|------------|-------------|
| 9:0 | RWS/RsvdP | Symmetric Cache Req Credits²: For a Fabric Port, this field represents the credits to advertise for CXL.cache H2D Req channel at init. The default value represents the maximum number of channel credits that the port supports. For Upstream and Downstream Port, this field is RsvdP and it is permitted to be hardwired to 0. |
| 19:10 | RWS/RsvdP | Symmetric Cache Rsp Credits²: For a Fabric Port, this field represents the credits to advertise for CXL.cache H2D Rsp channel at init. The default value represents the maximum number of channel credits that the port supports. For Upstream and Downstream Port, this field is RsvdP and it is permitted to be hardwired to 0. |
| 29:20 | RWS/RsvdP | Symmetric Cache Data Credits²: For a Fabric Port, this field represents the credits to advertise for CXL.cache H2D Data channel at init. The default value represents the maximum number of channel credits that the port supports. For Upstream and Downstream Port, this field is RsvdP and it is permitted to be hardwired to 0. |
| 39:30 | RWS/RsvdP | Symmetric Mem Req Rsp Credits²: For a Fabric Port, this field represents the credits to advertise for CXL.mem Request channel at init. The default value represents the maximum number of channel credits that the port supports. For an Upstream Port, this field represents the credits to advertise for the Direct P2P CXL.mem NDR channel at init. This field must be RWS if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register (see Section 8.1.3.9) is set; otherwise, it is permitted to be hardwired to 0. For a Downstream Port, this field represents the credits to advertise for Direct P2P CXL.mem Request channel at init. The default value represents the maximum number of credits that the port supports. This field must be RWS for an Edge DSP that supports Direct P2P CXL.mem; otherwise, it is permitted to be hardwired to 0. |
| 49:40 | RWS/RsvdP | Symmetric Mem Data Credits²: For a Fabric Port, this field represents the credits to advertise for CXL.mem RwD channel at init. The default value represents the maximum number of channel credits that the port supports. For an Upstream Port, this field represents the number of advertised Direct P2P CXL.mem DRS channel credits at init. This field must be RWS if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register (see Section 8.1.3.9) is set; otherwise, it is permitted to be hardwired to 0. For a Downstream Port, this field represents the number of advertised Direct P2P CXL.mem RwD channel credits at init. The default value represents the maximum number of channel credits of which the port is capable. This field must be RWS for an Edge DSP that supports Direct P2P CXL.mem; otherwise, it is permitted to be hardwired to 0. |
| 59:50 | RWS/RsvdP | Symmetric BI Credits²: For a Fabric Port, this field represents the credits to advertise for BIRsp channel at init. The default value represents the maximum number of channel credits that the port supports. For Upstream and Downstream Port, this field is RsvdP and it is permitted to be hardwired to 0. |
| 63:60 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

¹ 此寄存器作为 Version=4 的一部分引入。
² 此字段作为 Version=4 的一部分引入。

| 位域 | 属性 | 描述¹ |
|------|------|------|
| 9:0 | RWS/RsvdP | Symmetric Cache Req Credits²: 对于结构端口 (Fabric Port), 此字段表示初始化时为 CXL.cache H2D Req 信道通告的信用。默认值表示端口支持的最大信道信用数。对于上行端口和下行端口, 此字段为 RsvdP, 允许硬连线为 0。 |
| 19:10 | RWS/RsvdP | Symmetric Cache Rsp Credits²: 对于结构端口, 此字段表示初始化时为 CXL.cache H2D Rsp 信道通告的信用。默认值表示端口支持的最大信道信用数。对于上行端口和下行端口, 此字段为 RsvdP, 允许硬连线为 0。 |
| 29:20 | RWS/RsvdP | Symmetric Cache Data Credits²: 对于结构端口, 此字段表示初始化时为 CXL.cache H2D Data 信道通告的信用。默认值表示端口支持的最大信道信用数。对于上行端口和下行端口, 此字段为 RsvdP, 允许硬连线为 0。 |
| 39:30 | RWS/RsvdP | Symmetric Mem Req Rsp Credits²: 对于结构端口, 此字段表示初始化时为 CXL.mem 请求信道通告的信用。默认值表示端口支持的最大信道信用数。对于上行端口, 此字段表示初始化时为 Direct P2P CXL.mem NDR 信道通告的信用。如果 DVSEC CXL Capability³ 寄存器 (参见第 8.1.3.9 节) 中的 Direct P2P Mem Capable 位置位, 则此字段必须为 RWS; 否则, 允许硬连线为 0。对于下行端口, 此字段表示初始化时为 Direct P2P CXL.mem 请求信道通告的信用。默认值表示端口支持的最大信用数。对于支持 Direct P2P CXL.mem 的边缘 DSP, 此字段必须为 RWS; 否则, 允许硬连线为 0。 |
| 49:40 | RWS/RsvdP | Symmetric Mem Data Credits²: 对于结构端口, 此字段表示初始化时为 CXL.mem RwD 信道通告的信用。默认值表示端口支持的最大信道信用数。对于上行端口, 此字段表示初始化时通告的 Direct P2P CXL.mem DRS 信道信用数。如果 DVSEC CXL Capability³ 寄存器 (参见第 8.1.3.9 节) 中的 Direct P2P Mem Capable 位置位, 则此字段必须为 RWS; 否则, 允许硬连线为 0。对于下行端口, 此字段表示初始化时通告的 Direct P2P CXL.mem RwD 信道信用数。默认值表示端口支持的最大信道信用数。对于支持 Direct P2P CXL.mem 的边缘 DSP, 此字段必须为 RWS; 否则, 允许硬连线为 0。 |
| 59:50 | RWS/RsvdP | Symmetric BI Credits²: 对于结构端口, 此字段表示初始化时为 BIRsp 信道通告的信用。默认值表示端口支持的最大信道信用数。对于上行端口和下行端口, 此字段为 RsvdP, 允许硬连线为 0。 |
| 63:60 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-36.** CXL Link Layer Rx Credit Control2 Register layout ｜ CXL 链路层 Rx 信用控制 2 寄存器布局
>
> <img src="figures/chapter_08/page_0562.png" alt="Figure 8-36" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0562.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-9"></a>
## 8.2.4.19.9 CXL Link Layer Rx Credit Return Status2 Register (Offset 40h) | CXL 链路层 Rx 信用返回状态 2 寄存器 (偏移量 40h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

¹ This register was introduced as part of Version=4.
² This field was introduced as part of Version=4.

| Bit Location | Attributes | Description¹ |
|--------------|------------|-------------|
| 9:0 | RO/RsvdP | Symmetric Cache Req Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated CXL.cache H2D Req channel credits to be returned. For Upstream and Downstream Port, this field is RsvdP. |
| 19:10 | RO/RsvdP | Symmetric Cache Rsp Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated CXL.cache H2D Rsp channel credits to be returned. For Upstream and Downstream Port, this field is RsvdP. |
| 29:20 | RO/RsvdP | Symmetric Cache Data Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated CXL.cache H2D Data channel credits to be returned. For Upstream and Downstream Port, this field is RsvdP. |
| 39:30 | RO/RsvdP | Symmetric Mem Req_Rsp Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated CXL.mem Request channel credits to be returned. For an Upstream Port, this field represents the running snapshot of the accumulated Direct P2P CXL.mem NDR channel credits to be returned. This field must be RO if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register (see Section 8.1.3.9) is set; otherwise, it is RsvdP. For a Downstream Port, this field represents the running snapshot of the accumulated Direct P2P CXL.mem Request channel credits to be returned. This field must be RO for an Edge DSP that supports Direct P2P CXL.mem; otherwise, it is RsvdP. |
| 49:40 | RO/RsvdP | Symmetric Mem Data Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated CXL.mem RwD channel credits to be returned. For an Upstream Port, this field represents the running snapshot of the accumulated Direct P2P CXL.mem DRS channel credits to be returned. This field must be RO if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register (see Section 8.1.3.9) is set; otherwise, it is RsvdP. For a Downstream Port, this field represents the running snapshot of the accumulated Direct P2P CXL.mem RwD channel credits to be returned. This field must be RO for an Edge DSP that supports Direct P2P CXL.mem; otherwise, it is RsvdP. |
| 59:50 | RO/RsvdP | Symmetric BI Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated BIRsp channel credits to be returned. For Upstream and Downstream Port, this field is RsvdP. |
| 63:60 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

¹ 此寄存器作为 Version=4 的一部分引入。
² 此字段作为 Version=4 的一部分引入。

| 位域 | 属性 | 描述¹ |
|------|------|------|
| 9:0 | RO/RsvdP | Symmetric Cache Req Credits²: 对于结构端口, 此字段表示要返回的累积 CXL.cache H2D Req 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 19:10 | RO/RsvdP | Symmetric Cache Rsp Credits²: 对于结构端口, 此字段表示要返回的累积 CXL.cache H2D Rsp 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 29:20 | RO/RsvdP | Symmetric Cache Data Credits²: 对于结构端口, 此字段表示要返回的累积 CXL.cache H2D Data 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 39:30 | RO/RsvdP | Symmetric Mem Req_Rsp Credits²: 对于结构端口, 此字段表示要返回的累积 CXL.mem 请求信道信用的运行快照。对于上行端口, 此字段表示要返回的累积 Direct P2P CXL.mem NDR 信道信用的运行快照。如果 DVSEC CXL Capability³ 寄存器 (参见第 8.1.3.9 节) 中的 Direct P2P Mem Capable 位置位, 则此字段必须为 RO; 否则, 为 RsvdP。对于下行端口, 此字段表示要返回的累积 Direct P2P CXL.mem 请求信道信用的运行快照。对于支持 Direct P2P CXL.mem 的边缘 DSP, 此字段必须为 RO; 否则, 为 RsvdP。 |
| 49:40 | RO/RsvdP | Symmetric Mem Data Credits²: 对于结构端口, 此字段表示要返回的累积 CXL.mem RwD 信道信用的运行快照。对于上行端口, 此字段表示要返回的累积 Direct P2P CXL.mem DRS 信道信用的运行快照。如果 DVSEC CXL Capability³ 寄存器 (参见第 8.1.3.9 节) 中的 Direct P2P Mem Capable 位置位, 则此字段必须为 RO; 否则, 为 RsvdP。对于下行端口, 此字段表示要返回的累积 Direct P2P CXL.mem RwD 信道信用的运行快照。对于支持 Direct P2P CXL.mem 的边缘 DSP, 此字段必须为 RO; 否则, 为 RsvdP。 |
| 59:50 | RO/RsvdP | Symmetric BI Credits²: 对于结构端口, 此字段表示要返回的累积 BIRsp 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 63:60 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-37.** CXL Link Layer Rx Credit Return Status2 Register layout ｜ CXL 链路层 Rx 信用返回状态 2 寄存器布局
>
> <img src="figures/chapter_08/page_0563.png" alt="Figure 8-37" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0563.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-19-10"></a>
## 8.2.4.19.10 CXL Link Layer Tx Credit Status2 Register (Offset 48h) | CXL 链路层 Tx 信用状态 2 寄存器 (偏移量 48h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

¹ This register was introduced as part of Version=4.
² This field was introduced as part of Version=4.

| Bit Location | Attributes | Description¹ |
|--------------|------------|-------------|
| 9:0 | RO/RsvdP | Symmetric Cache Req Credits²: For a Fabric Port, this field represents the running snapshot of the CXL.cache D2H Req channel credits for Tx. For Upstream and Downstream Port, this field is RsvdP. |
| 19:10 | RO/RsvdP | Symmetric Cache Rsp Credits²: For a Fabric Port, this field represents the running snapshot of the CXL.cache D2H Rsp channel credits for Tx. For Upstream and Downstream Port, this field is RsvdP. |
| 29:20 | RO/RsvdP | Symmetric Cache Data Credits²: For Fabric Port, this field represents the running snapshot of the CXL.cache D2H Data channel credits for Tx. For Upstream and Downstream Port, this field is RsvdP. |
| 39:30 | RO/RsvdP | Symmetric Mem Req_Rsp Credits²: For a Fabric Port, this field represents the running snapshot of the CXL.mem NDR channel credits for Tx. For an Upstream Port, this field represents the running snapshot of the Direct P2P CXL.mem Request channel credits for Tx. This field must be RO if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register (see Section 8.1.3.9) is set; otherwise, it is RsvdP. For a Downstream Port, this field represents the running snapshot of the Direct P2P CXL.mem NDR channel credits for Tx. This field must be RO for an Edge DSP that supports Direct P2P CXL.mem; otherwise, it is RsvdP. |
| 49:40 | RO/RsvdP | Symmetric Mem Data Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated DRS channel credits for Tx. For an Upstream Port, this field represents the number of Direct P2P CXL.mem RwD channel credits for Tx. This field must be RO if the Direct P2P Mem Capable bit in the DVSEC CXL Capability³ register (see Section 8.1.3.9) is set; otherwise, it is RsvdP. For a Downstream Port, this field represents the number of Direct P2P CXL.mem DRS channel credits for Tx. This field must be RO for an Edge DSP that supports Direct P2P CXL.mem; otherwise, it is RsvdP. |
| 59:50 | RO/RsvdP | Symmetric BI Credits²: For a Fabric Port, this field represents the running snapshot of the accumulated BISnp channel credits for Tx. For Upstream and Downstream Port, this field is RsvdP. |
| 63:60 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

¹ 此寄存器作为 Version=4 的一部分引入。
² 此字段作为 Version=4 的一部分引入。

| 位域 | 属性 | 描述¹ |
|------|------|------|
| 9:0 | RO/RsvdP | Symmetric Cache Req Credits²: 对于结构端口, 此字段表示 Tx 的 CXL.cache D2H Req 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 19:10 | RO/RsvdP | Symmetric Cache Rsp Credits²: 对于结构端口, 此字段表示 Tx 的 CXL.cache D2H Rsp 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 29:20 | RO/RsvdP | Symmetric Cache Data Credits²: 对于结构端口, 此字段表示 Tx 的 CXL.cache D2H Data 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 39:30 | RO/RsvdP | Symmetric Mem Req_Rsp Credits²: 对于结构端口, 此字段表示 Tx 的 CXL.mem NDR 信道信用的运行快照。对于上行端口, 此字段表示 Tx 的 Direct P2P CXL.mem 请求信道信用的运行快照。如果 DVSEC CXL Capability³ 寄存器 (参见第 8.1.3.9 节) 中的 Direct P2P Mem Capable 位置位, 则此字段必须为 RO; 否则, 为 RsvdP。对于下行端口, 此字段表示 Tx 的 Direct P2P CXL.mem NDR 信道信用的运行快照。对于支持 Direct P2P CXL.mem 的边缘 DSP, 此字段必须为 RO; 否则, 为 RsvdP。 |
| 49:40 | RO/RsvdP | Symmetric Mem Data Credits²: 对于结构端口, 此字段表示 Tx 的累积 DRS 信道信用的运行快照。对于上行端口, 此字段表示 Tx 的 Direct P2P CXL.mem RwD 信道信用数。如果 DVSEC CXL Capability³ 寄存器 (参见第 8.1.3.9 节) 中的 Direct P2P Mem Capable 位置位, 则此字段必须为 RO; 否则, 为 RsvdP。对于下行端口, 此字段表示 Tx 的 Direct P2P CXL.mem DRS 信道信用数。对于支持 Direct P2P CXL.mem 的边缘 DSP, 此字段必须为 RO; 否则, 为 RsvdP。 |
| 59:50 | RO/RsvdP | Symmetric BI Credits²: 对于结构端口, 此字段表示 Tx 的累积 BISnp 信道信用的运行快照。对于上行端口和下行端口, 此字段为 RsvdP。 |
| 63:60 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-38.** CXL Link Layer Tx Credit Status2 Register layout ｜ CXL 链路层 Tx 信用状态 2 寄存器布局
>
> <img src="figures/chapter_08/page_0564.png" alt="Figure 8-38" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0564.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20"></a>
## 8.2.4.20 CXL HDM Decoder Capability Structure | CXL HDM 解码器能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

CXL HDM Decoder Capability structure facilitates routing of CXL.mem as well as UIO transactions that target HDM and optionally enables interleaving of HDM across CXL.mem-capable devices.

A CXL Host Bridge is identified as an ACPI device with a Hardware ID (HID) of "ACPI0016" and is associated with one or more CXL root ports. Any CXL Host Bridge that is associated with more than one CXL root port must contain one instance of this capability structure in the CHBCR. This capability structure resolves the target CXL root ports for a given memory address.

A CXL switch component may contain one Upstream Switch Port and one or more Downstream Switch Ports. A CXL Upstream Switch Port that is capable of routing CXL.mem traffic to more than one Downstream Switch Ports shall contain one instance of this capability structure. The capability structure, located in CXL Upstream Switch Port, resolves the target CXL Downstream Switch Ports for a given memory address.

A CXL Type 3 device that is not an eRCD shall contain one instance of this capability structure. A CXL Type 2 device that supports BI or supports UIO access to its HDM shall contain one instance of this capability structure. The capability structure, located in a device, translates the Host Physical Address (HPA) into a Device Physical Address (DPA) after taking any interleaving into account.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL HDM Decoder Capability Register |
| 04h | CXL HDM Decoder Global Control Register |
| 08h | Reserved |
| 0Ch | Reserved |
| **Decoder 0:** | |
| 10h | CXL HDM Decoder 0 Base Low Register |
| 14h | CXL HDM Decoder 0 Base High Register |
| 18h | CXL HDM Decoder 0 Size Low Register |
| 1Ch | CXL HDM Decoder 0 Size High Register |
| 20h | CXL HDM Decoder 0 Control Register |
| 24h | CXL HDM Decoder 0 Target List Low Register (not applicable to devices) / CXL HDM Decoder 0 DPA Skip Low Register (devices only) |
| 28h | CXL HDM Decoder 0 Target List High Register (not applicable to devices) / CXL HDM Decoder 0 DPA Skip High Register (devices only) |
| 2Ch | Reserved |
| **Decoder 1:** | |
| 30h – 4Fh | CXL HDM Decoder 1 registers |
| … | … |
| **Decoder n:** | |
| 20h *n+ 10h: 20h*n + 2Fh | CXL HDM Decoder n registers (see Section 8.2.4.20.3 through Section 8.2.4.20.11). |

0 ≤ n < Raw Decoder Count. The Raw Decoder count is derived from the Decoder Count field in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1).

</td><td style="background-color:#e8e8e8">

CXL HDM 解码器能力结构便于对面向 HDM 的 CXL.mem 以及 UIO 事务进行路由, 并可选择地实现跨 CXL.mem 能力设备的 HDM 交织。

CXL 主机桥 (Host Bridge) 由硬件 ID (HID) 为 "ACPI0016" 的 ACPI 设备标识, 并与一个或多个 CXL 根端口相关联。任何与多个 CXL 根端口相关联的 CXL 主机桥必须在 CHBCR 中包含此能力结构的一个实例。该能力结构解析给定内存地址的目标 CXL 根端口。

CXL 交换机组件可以包含一个上行交换机端口 (Upstream Switch Port) 和一个或多个下行交换机端口 (Downstream Switch Port)。能够将 CXL.mem 流量路由到多个下行交换机端口的 CXL 上行交换机端口应包含此能力结构的一个实例。该能力结构位于 CXL 上行交换机端口中, 解析给定内存地址的目标 CXL 下行交换机端口。

非 eRCD 的 CXL Type 3 设备应包含此能力结构的一个实例。支持 BI 或支持对其 HDM 进行 UIO 访问的 CXL Type 2 设备应包含此能力结构的一个实例。位于设备中的该能力结构在考虑任何交织后, 将主机物理地址 (HPA) 转换为设备物理地址 (DPA)。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL HDM Decoder Capability Register |
| 04h | CXL HDM Decoder Global Control Register |
| 08h | 保留 |
| 0Ch | 保留 |
| **Decoder 0:** | |
| 10h | CXL HDM Decoder 0 Base Low Register |
| 14h | CXL HDM Decoder 0 Base High Register |
| 18h | CXL HDM Decoder 0 Size Low Register |
| 1Ch | CXL HDM Decoder 0 Size High Register |
| 20h | CXL HDM Decoder 0 Control Register |
| 24h | CXL HDM Decoder 0 Target List Low Register (不适用于设备) / CXL HDM Decoder 0 DPA Skip Low Register (仅设备) |
| 28h | CXL HDM Decoder 0 Target List High Register (不适用于设备) / CXL HDM Decoder 0 DPA Skip High Register (仅设备) |
| 2Ch | 保留 |
| **Decoder 1:** | |
| 30h – 4Fh | CXL HDM Decoder 1 寄存器 |
| … | … |
| **Decoder n:** | |
| 20h *n+ 10h: 20h*n + 2Fh | CXL HDM Decoder n 寄存器 (参见第 8.2.4.20.3 节到第 8.2.4.20.11 节)。 |

0 ≤ n < Raw Decoder Count。原始解码器计数源自 CXL HDM Decoder Capability 寄存器中的 Decoder Count 字段 (参见第 8.2.4.20.1 节)。

</td></tr>
</tbody>
</table>

> **Figure 8-39.** CXL HDM Decoder Capability Structure layout ｜ CXL HDM 解码器能力结构布局
>
> <img src="figures/chapter_08/page_0565.png" alt="Figure 8-39" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0565.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-1"></a>
## 8.2.4.20.1 CXL HDM Decoder Capability Register (Offset 00h) | CXL HDM 解码器能力寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RO | Decoder Count: Reports the number of memory address decoders implemented by the component. CXL devices shall not advertise more than 10 decoders. CXL switches and Host Bridges may advertise up to 32 decoders.<br>• 0h = 1 Decoder<br>• 1h = 2 Decoders<br>• 2h = 4 Decoders<br>• 3h = 6 Decoders<br>• 4h = 8 Decoders<br>• 5h = 10 Decoders<br>• 6h = 12 Decoders²<br>• 7h = 14 Decoders²<br>• 8h = 16 Decoders²<br>• 9h = 20 Decoders²<br>• Ah = 24 Decoders²<br>• Bh = 28 Decoders²<br>• Ch = 32 Decoders²<br>All other encodings are reserved |
| 7:4 | RO | Target Count: The number of target ports each decoder supports (applicable only to Upstream Switch Port and CXL Host Bridge). Maximum of 8.<br>• 1h = 1 target port<br>• 2h = 2 target ports<br>• 4h = 4 target ports<br>• 8h = 8 target ports<br>All other encodings are reserved |
| 8 | RO | A11to8 Interleave Capable: If set, the component supports interleaving based on Address bits [11:8]. CXL Host Bridges and Upstream Switch Ports shall always set this bit indicating support for interleaving based on Address bits [11:8]. |
| 9 | RO | A14to12 Interleave Capable: If set, the component supports interleaving based on Address bits [14:12]. CXL Host Bridges and switches shall always set this bit indicating support for interleaving based on Address bits [14:12]. |
| 10 | RO | Poison On Decode Error Capability: If set, the component is capable of returning poison on read access to addresses that are not positively decoded by any HDM Decoders in this component. If cleared, the component is not capable of returning poison under such scenarios. |
| 11 | RO | 3, 6, 12 Way Interleave Capable: If set, the CXL.mem devices supports 3-way, 6-way and 12-way interleaving, respectively. Not applicable to Upstream Switch Ports and CXL Host Bridges. Upstream Switch Ports and CXL Host Bridges shall hardwire this bit to 0.¹ |
| 12 | RO | 16 Way Interleave Capable: If set, the CXL.mem device supports 16-way interleaving. Not applicable to Upstream Switch Ports and CXL Host Bridges. Upstream Switch Ports and CXL Host Bridges shall hardwire this bit to 0.¹ |
| 13 | HwInit | UIO Capable²<br>• For CXL.mem devices: If set, the device supports UIO accesses to its HDM<br>• For USPs: If set, the switch is capable of routing UIO accesses that target HDM across its ports<br>• For CXL Host Bridges: If set, all the root ports within this Host Bridge are capable of routing UIO requests that target HDM across root ports within this Host Bridge |
| 15:14 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RO | Decoder Count: 报告组件实现的内存地址解码器数量。CXL 设备不得通告超过 10 个解码器。CXL 交换机和主机桥可通告最多 32 个解码器。<br>• 0h = 1 个解码器<br>• 1h = 2 个解码器<br>• 2h = 4 个解码器<br>• 3h = 6 个解码器<br>• 4h = 8 个解码器<br>• 5h = 10 个解码器<br>• 6h = 12 个解码器²<br>• 7h = 14 个解码器²<br>• 8h = 16 个解码器²<br>• 9h = 20 个解码器²<br>• Ah = 24 个解码器²<br>• Bh = 28 个解码器²<br>• Ch = 32 个解码器²<br>所有其他编码保留 |
| 7:4 | RO | Target Count: 每个解码器支持的目标端口数 (仅适用于上行交换机端口和 CXL 主机桥)。最大为 8。<br>• 1h = 1 个目标端口<br>• 2h = 2 个目标端口<br>• 4h = 4 个目标端口<br>• 8h = 8 个目标端口<br>所有其他编码保留 |
| 8 | RO | A11to8 Interleave Capable: 如果置位, 表示组件支持基于地址位 [11:8] 的交织。CXL 主机桥和上行交换机端口应始终置位该位, 表示支持基于地址位 [11:8] 的交织。 |
| 9 | RO | A14to12 Interleave Capable: 如果置位, 表示组件支持基于地址位 [14:12] 的交织。CXL 主机桥和交换机应始终置位该位, 表示支持基于地址位 [14:12] 的交织。 |
| 10 | RO | Poison On Decode Error Capability: 如果置位, 表示组件能够在对未被此组件中任何 HDM 解码器正确定向解码的地址进行读访问时返回 Poison。如果清零, 则组件在此类场景下不能返回 Poison。 |
| 11 | RO | 3, 6, 12 Way Interleave Capable: 如果置位, 表示 CXL.mem 设备分别支持 3 路、6 路和 12 路交织。不适用于上行交换机端口和 CXL 主机桥。上行交换机端口和 CXL 主机桥应将该位硬连线为 0。¹ |
| 12 | RO | 16 Way Interleave Capable: 如果置位, 表示 CXL.mem 设备支持 16 路交织。不适用于上行交换机端口和 CXL 主机桥。上行交换机端口和 CXL 主机桥应将该位硬连线为 0。¹ |
| 13 | HwInit | UIO Capable²<br>• 对于 CXL.mem 设备: 如果置位, 表示设备支持对其 HDM 的 UIO 访问<br>• 对于 USP: 如果置位, 表示交换机能够跨其端口路由面向 HDM 的 UIO 访问<br>• 对于 CXL 主机桥: 如果置位, 表示此主机桥内的所有根端口都能够跨此主机桥内的根端口路由面向 HDM 的 UIO 请求 |
| 15:14 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

¹ Introduced as part of Version=2.
² Introduced as part of Version=3.

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English (continued)</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文 (续)</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 19:16 | HwInit/RsvdP | UIO Capable Decoder Count: Reports the total number of memory address decoders that are implemented by components that support UIO. Software is permitted to set the UIO bit in non-consecutive HDM decoders as long as the number of UIO-enabled decoders does not exceed this count. If the software attempts to set the UIO bit (see Section 8.2.4.20.2) in an HDM decoder beyond this limit, the component shall fail the HDM decoder commit operation. See the Decoder Count field in this register for enumeration. This field is reserved for a component if the UIO Capable bit in this register is 0. This field is reserved for CXL.mem devices. A UIO-capable CXL.mem device is not permitted to limit the number of UIO-capable HDM decoders and must operate correctly even when the UIO bit is set in all of its HDM decoders.² |
| 20 | HwInit | MemData-NXM Capable: If set, the component supports MemData-NXM opcode (see Table 3-53). If cleared, the component does not support MemData-NXM opcode. All 256B Flit mode-capable components shall set this bit to 1. See Table 8-27 for the description of how this bit affects the handling of CXL.mem read requests in case of errors.² |
| 22:21 | HwInit/RsvdP | Supported Coherency Models: Indicates the coherency models that are supported by a CXL.mem device. This field is reserved for all other components.²<br>• 00b = Unknown.<br>• 01b = Device Coherent. The Target Range Type bit in an HDM decoder must be 0 when the HDM decoder is committed; otherwise, the device behavior is undefined.<br>• 10b = Host-Only. The Target Range Type bit in an HDM decoder must be 1 when the HDM decoder is committed; otherwise, the device behavior is undefined.<br>• 11b = Host-Only or Device Coherent. The Target Range Type bit in an HDM decoder is RW and may be set to 1 or cleared to 0 by software before committing the HDM decoder. |
| 31:23 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 19:16 | HwInit/RsvdP | UIO Capable Decoder Count: 报告支持 UIO 的组件所实现的内存地址解码器总数。只要启用了 UIO 的解码器数量不超过此计数, 软件就允许在非连续的 HDM 解码器中设置 UIO 位。如果软件尝试在超出此限制的 HDM 解码器中设置 UIO 位 (参见第 8.2.4.20.2 节), 组件应使 HDM 解码器提交操作失败。有关枚举, 请参见本寄存器中的 Decoder Count 字段。如果本寄存器中的 UIO Capable 位为 0, 则此字段对组件保留。此字段对 CXL.mem 设备保留。支持 UIO 的 CXL.mem 设备不得限制支持 UIO 的 HDM 解码器数量, 并且即使在其所有 HDM 解码器中都设置了 UIO 位, 也必须正确运行。² |
| 20 | HwInit | MemData-NXM Capable: 如果置位, 表示组件支持 MemData-NXM 操作码 (参见表 3-53)。如果清零, 则组件不支持 MemData-NXM 操作码。所有支持 256B Flit 模式的组件应将该位置位为 1。有关此位如何影响错误情况下 CXL.mem 读请求处理的描述, 请参见表 8-27。² |
| 22:21 | HwInit/RsvdP | Supported Coherency Models: 指示 CXL.mem 设备支持的相干模型。此字段对所有其他组件保留。²<br>• 00b = 未知 (Unknown)。<br>• 01b = 设备相干 (Device Coherent)。当 HDM 解码器被提交时, HDM 解码器中的 Target Range Type 位必须为 0; 否则, 设备行为未定义。<br>• 10b = 仅主机 (Host-Only)。当 HDM 解码器被提交时, HDM 解码器中的 Target Range Type 位必须为 1; 否则, 设备行为未定义。<br>• 11b = 仅主机或设备相干 (Host-Only or Device Coherent)。HDM 解码器中的 Target Range Type 位为 RW, 可由软件在提交 HDM 解码器之前设置为 1 或清零为 0。 |
| 31:23 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Table 8-27.** CXL.mem Read Response - Error Cases ｜ CXL.mem 读响应 - 错误情况
>
> <img src="figures/chapter_08/page_0567.png" alt="Table 8-27" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0567.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-2"></a>
## 8.2.4.20.2 CXL HDM Decoder Global Control Register (Offset 04h) | CXL HDM 解码器全局控制寄存器 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW/RO | Poison On Decode Error Enable: This bit is RO and is hardwired to 0 if Poison On Decode Error Capability=0. See Table 8-27 for the description of how this bit affects the handling of CXL.mem read requests in case of errors. Note: Writes to addresses that are not positively decoded shall be dropped and a No Data Response (see Section 3.3.9) shall be sent regardless of the state of this bit. Default value of this bit is 0. |
| 1 | RW | HDM Decoder Enable: This bit is only applicable to CXL.mem devices and shall return 0 on CXL Host Bridges and Upstream Switch Ports. When this bit is set, device shall use HDM decoders to decode CXL.mem transactions and not use HDM Base registers in PCIe DVSEC for CXL devices (see Section 8.1.3.8.3, Section 8.1.3.8.4, Section 8.1.3.8.7, and Section 8.1.3.8.8). CXL Host Bridges and Upstream Switch Ports always use HDM Decoders to decode CXL.mem transactions. Default value of this bit is 0. |
| 31:2 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW/RO | Poison On Decode Error Enable: 如果 Poison On Decode Error Capability=0, 则此位为 RO 并硬连线为 0。有关此位如何影响错误情况下 CXL.mem 读请求处理的描述, 请参见表 8-27。注: 写入未正确定向解码的地址应被丢弃, 并且应发送 No Data Response (参见第 3.3.9 节), 而与该位的状态无关。该位的默认值为 0。 |
| 1 | RW | HDM Decoder Enable: 该位仅适用于 CXL.mem 设备, 在 CXL 主机桥和上行交换机端口上应返回 0。当该位置位时, 设备应使用 HDM 解码器来解码 CXL.mem 事务, 而不使用 PCIe DVSEC for CXL devices 中的 HDM Base 寄存器 (参见第 8.1.3.8.3 节、第 8.1.3.8.4 节、第 8.1.3.8.7 节和第 8.1.3.8.8 节)。CXL 主机桥和上行交换机端口始终使用 HDM 解码器来解码 CXL.mem 事务。该位的默认值为 0。 |
| 31:2 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-40.** CXL HDM Decoder Global Control Register layout ｜ CXL HDM 解码器全局控制寄存器布局
>
> <img src="figures/chapter_08/page_0568.png" alt="Figure 8-40" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0568.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-3"></a>
## 8.2.4.20.3 CXL HDM Decoder n Base Low Register (Offset 20h*n+10h) | CXL HDM 解码器 n 基地址低寄存器 (偏移量 20h*n+10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 27:0 | RsvdP | Reserved |
| 31:28 | RWL | Memory Base Low: Corresponds to bits 31:28 of the base of the address range managed by Decoder n. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 0h. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 27:0 | RsvdP | 保留 |
| 31:28 | RWL | Memory Base Low: 对应于由解码器 n 管理的地址范围的基地址的 31:28 位。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 0h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-41.** CXL HDM Decoder n Base Low Register layout ｜ CXL HDM 解码器 n 基地址低寄存器布局
>
> <img src="figures/chapter_08/page_0568.png" alt="Figure 8-41" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0568.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-4"></a>
## 8.2.4.20.4 CXL HDM Decoder n Base High Register (Offset 20h*n+14h) | CXL HDM 解码器 n 基地址高寄存器 (偏移量 20h*n+14h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 31:0 | RWL | Memory Base High: Corresponds to bits 63:32 of the base of the address range managed by Decoder n. The locking behavior is described in Section 8.2.4.20.13. Default value of this register is 0000 0000h. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 31:0 | RWL | Memory Base High: 对应于由解码器 n 管理的地址范围的基地址的 63:32 位。锁定行为在第 8.2.4.20.13 节中描述。此寄存器的默认值为 0000 0000h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-42.** CXL HDM Decoder n Base High Register layout ｜ CXL HDM 解码器 n 基地址高寄存器布局
>
> <img src="figures/chapter_08/page_0568.png" alt="Figure 8-42" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0568.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-5"></a>
## 8.2.4.20.5 CXL HDM Decoder n Size Low Register (Offset 20h*n+18h) | CXL HDM 解码器 n 大小低寄存器 (偏移量 20h*n+18h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 27:0 | RsvdP | Reserved |
| 31:28 | RWL | Memory Size Low: Corresponds to bits 31:28 of the size of the address range managed by Decoder n. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 0h. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 27:0 | RsvdP | 保留 |
| 31:28 | RWL | Memory Size Low: 对应于由解码器 n 管理的地址范围的大小的 31:28 位。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 0h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-43.** CXL HDM Decoder n Size Low Register layout ｜ CXL HDM 解码器 n 大小低寄存器布局
>
> <img src="figures/chapter_08/page_0568.png" alt="Figure 8-43" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0568.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-6"></a>
## 8.2.4.20.6 CXL HDM Decoder n Size High Register (Offset 20h*n+1Ch) | CXL HDM 解码器 n 大小高寄存器 (偏移量 20h*n+1Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 31:0 | RWL | Memory Size High: Corresponds to bits 63:32 of the size of address range managed by Decoder n. The locking behavior is described in Section 8.2.4.20.13. Default value of this register is 0000 0000h. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 31:0 | RWL | Memory Size High: 对应于由解码器 n 管理的地址范围的大小的 63:32 位。锁定行为在第 8.2.4.20.13 节中描述。此寄存器的默认值为 0000 0000h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-44.** CXL HDM Decoder n Size High Register layout ｜ CXL HDM 解码器 n 大小高寄存器布局
>
> <img src="figures/chapter_08/page_0569.png" alt="Figure 8-44" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0569.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-7"></a>
## 8.2.4.20.7 CXL HDM Decoder n Control Register (Offset 20h*n+20h) | CXL HDM 解码器 n 控制寄存器 (偏移量 20h*n+20h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RWL | Interleave Granularity (IG): The number of consecutive bytes that are assigned to each target in the Target List.<br>• 0h = 256 Bytes<br>• 1h = 512 Bytes<br>• 2h = 1024 Bytes (1 KB)<br>• 3h = 2048 Bytes (2 KB)<br>• 4h = 4096 Bytes (4 KB)<br>• 5h = 8192 Bytes (8 KB)<br>• 6h = 16384 Bytes (16 KB)<br>All other encodings are reserved<br>The device reports its desired interleave setting via the Desired_Interleave field in the DVSEC CXL Range 1/Range 2 Size Low register. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 0h. |
| 7:4 | RWL | Interleave Ways (IW): The number of targets across which Decoder n memory range is interleaved.<br>• 0h = 1 way (no interleaving)<br>• 1h = 2-way interleaving<br>• 2h = 4-way interleaving<br>• 3h = 8-way interleaving<br>• 4h = 16-way interleaving (valid only for CXL.mem devices)¹<br>• 8h = 3-way interleaving (valid only for CXL.mem devices)¹<br>• 9h = 6-way interleaving (valid only for CXL.mem devices)¹<br>• Ah = 12-way interleaving (valid only for CXL.mem devices)¹<br>All other encodings are reserved<br>The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 0h. |
| 8 | RWL | Lock On Commit: If set, all RWL fields in Decoder n shall become read only when Committed changes to 1. The locking behavior is described in Section 8.2.4.20.13. Default value of this bit is 0. |
| 9 | RWL | Commit: Software sets this to 1 to commit Decoder n. The locking behavior is described in Section 8.2.4.20.13. Default value of this bit is 0. A 1 to 0 transition of this bit shall cause the associated Committed bit to transition from 1 to 0. |
| 10 | RO | Committed: If 1, indicates Decoder n is active. |
| 11 | RO | Error Not Committed: If 1, indicates that the programming of Decoder n had an error and Decoder n is not active. |
| 12 | RWL/RO | Target Range Type: Formerly known as Target Device Type. This bit is RWL for CXL Host Bridges, and Upstream Switch Ports. This bit is permitted to be RO for devices that do not support this reconfigurability and it may return the value of 0 or 1 to represent the only coherency model that the devices support.<br>• 0 = Target is a Device Coherent Address range (HDM-D or HDM-DB)<br>• 1 = Target is a Host-Only Coherent Address range (HDM-H)<br>The locking behavior is described in Section 8.2.4.20.13. Default value of this bit is 0. |
| 13 | RWL/RsvdP | BI: This bit is RWL for BI-capable components. This bit is reserved for components that do not support BI. Devices that require BI for managing coherency are permitted to hardwire this bit to 1.²<br>• 0 = Device is not permitted to issue BISnp requests to this range<br>• 1 = Device is permitted to issue BISnp requests to this range |
| 14 | RWL | UIO: This bit is RWL if the UIO Capable bit in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1) is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the UIO Capable bit is set to 1. Default value of this bit is 0. See Table 9-18 for how various components utilize the setting of this bit during the processing of UIO messages.² |
| 15 | RsvdP | Reserved |
| 19:16 | RWL/RsvdP | Upstream Interleave Granularity (UIG): The aggregate interleave granularity applied to the HPA by the HDM decode stages that are upstream of this port. For enumeration of legal values, see the definition of Interleave Granularity in this register.² This bit is RWL for a switch and a Host Bridge if the UIO Capable bit in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1) is set. This field is reserved for CXL.mem devices. This field is also reserved for switches and Host Bridges that are not UIO capable. Default value of this field is 0h. |
| 23:20 | RWL/RsvdP | Upstream Interleave Ways (UIW): The aggregate Interleave granularity ways produced by HDM decode stages that are upstream of this port. For enumeration of legal values, see the definition of Interleave Ways in this register.² This bit is RWL for a switch and a Host Bridge if the UIO Capable bit in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1) is set. This field is reserved for CXL.mem devices. This field is also reserved for switches and Host Bridges that are not UIO capable. Default value of this field is 0h. |
| 27:24 | RWL/RsvdP | Interleave Set Position (ISP): The position of this component in the interleave set formed when all HDM decode stages that are upstream of this port are considered. Expressed as a 0-based quantity. For a switch and a Host Bridge, ISP must be configured to a value that is lower than the number of Upstream Interleave Ways (the raw value, not the encoded value); otherwise, the results are undefined.² This field is RWL for a switch, and a Host Bridge if the UIO Capable bit in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1) is set. This field is RWL for a BI-capable CXL.mem device. This field is reserved for switches, and Host Bridges that are not UIO capable. This field is reserved for CXL.mem devices that are not BI-capable. Default value of this field is 0h. |
| 31:28 | RsvdP | Reserved |

¹ Introduced as part of Version=2.
² Introduced as part of Version=3.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RWL | Interleave Granularity (IG): 分配给 Target List 中每个目标的连续字节数。<br>• 0h = 256 字节<br>• 1h = 512 字节<br>• 2h = 1024 字节 (1 KB)<br>• 3h = 2048 字节 (2 KB)<br>• 4h = 4096 字节 (4 KB)<br>• 5h = 8192 字节 (8 KB)<br>• 6h = 16384 字节 (16 KB)<br>所有其他编码保留<br>设备通过 DVSEC CXL Range 1/Range 2 Size Low 寄存器中的 Desired_Interleave 字段报告其期望的交织设置。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 0h。 |
| 7:4 | RWL | Interleave Ways (IW): 解码器 n 内存范围与之交织的目标数。<br>• 0h = 1 路 (无交织)<br>• 1h = 2 路交织<br>• 2h = 4 路交织<br>• 3h = 8 路交织<br>• 4h = 16 路交织 (仅对 CXL.mem 设备有效)¹<br>• 8h = 3 路交织 (仅对 CXL.mem 设备有效)¹<br>• 9h = 6 路交织 (仅对 CXL.mem 设备有效)¹<br>• Ah = 12 路交织 (仅对 CXL.mem 设备有效)¹<br>所有其他编码保留<br>锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 0h。 |
| 8 | RWL | Lock On Commit: 如果置位, 当 Committed 变为 1 时, 解码器 n 中的所有 RWL 字段应变为只读。锁定行为在第 8.2.4.20.13 节中描述。该位的默认值为 0。 |
| 9 | RWL | Commit: 软件将该位置 1 以提交解码器 n。锁定行为在第 8.2.4.20.13 节中描述。该位的默认值为 0。该位从 1 到 0 的转换应导致相关 Committed 位从 1 转换为 0。 |
| 10 | RO | Committed: 如果为 1, 表示解码器 n 处于活动状态。 |
| 11 | RO | Error Not Committed: 如果为 1, 表示解码器 n 的编程存在错误, 解码器 n 未处于活动状态。 |
| 12 | RWL/RO | Target Range Type: 以前称为 Target Device Type。对于 CXL 主机桥和上行交换机端口, 该位为 RWL。对于不支持此重配置功能的设备, 该位允许为 RO, 并且可以返回值 0 或 1 以表示设备支持的唯一相干模型。<br>• 0 = 目标是设备相干地址范围 (HDM-D 或 HDM-DB)<br>• 1 = 目标是仅主机相干地址范围 (HDM-H)<br>锁定行为在第 8.2.4.20.13 节中描述。该位的默认值为 0。 |
| 13 | RWL/RsvdP | BI: 对于支持 BI 的组件, 该位为 RWL。对于不支持 BI 的组件, 该位保留。需要 BI 来管理相干性的设备允许将该位硬连线为 1。²<br>• 0 = 不允许设备向此范围发出 BISnp 请求<br>• 1 = 允许设备向此范围发出 BISnp 请求 |
| 14 | RWL | UIO: 如果 CXL HDM Decoder Capability 寄存器 (参见第 8.2.4.20.1 节) 中的 UIO Capable 位置位, 则该位为 RWL; 否则, 允许硬连线为 0。除非 UIO Capable 位置 1, 否则软件不得设置该位。该位的默认值为 0。有关各种组件在 UIO 消息处理过程中如何使用此位的设置, 请参见表 9-18。² |
| 15 | RsvdP | 保留 |
| 19:16 | RWL/RsvdP | Upstream Interleave Granularity (UIG): 由该端口上游的 HDM 解码阶段应用于 HPA 的聚合交织粒度。有关合法值的枚举, 请参见本寄存器中 Interleave Granularity 的定义。² 如果 CXL HDM Decoder Capability 寄存器 (参见第 8.2.4.20.1 节) 中的 UIO Capable 位置位, 则对于交换机和主机桥, 该位为 RWL。此字段对 CXL.mem 设备保留。此字段对不支持 UIO 的交换机和主机桥也保留。该字段的默认值为 0h。 |
| 23:20 | RWL/RsvdP | Upstream Interleave Ways (UIW): 由该端口上游的 HDM 解码阶段产生的聚合交织粒度方式。有关合法值的枚举, 请参见本寄存器中 Interleave Ways 的定义。² 如果 CXL HDM Decoder Capability 寄存器 (参见第 8.2.4.20.1 节) 中的 UIO Capable 位置位, 则对于交换机和主机桥, 该位为 RWL。此字段对 CXL.mem 设备保留。此字段对不支持 UIO 的交换机和主机桥也保留。该字段的默认值为 0h。 |
| 27:24 | RWL/RsvdP | Interleave Set Position (ISP): 在考虑该端口上游的所有 HDM 解码阶段时形成的交织集中此组件的位置。以 0 为基的数量表示。对于交换机和主机桥, ISP 必须配置为低于 Upstream Interleave Ways 数量 (原始值, 而不是编码值) 的值; 否则, 结果未定义。² 如果 CXL HDM Decoder Capability 寄存器 (参见第 8.2.4.20.1 节) 中的 UIO Capable 位置位, 则对于交换机和主机桥, 此字段为 RWL。对于支持 BI 的 CXL.mem 设备, 此字段为 RWL。此字段对不支持 UIO 的交换机和主机桥保留。此字段对不支持 BI 的 CXL.mem 设备保留。该字段的默认值为 0h。 |
| 31:28 | RsvdP | 保留 |

¹ 作为 Version=2 的一部分引入。
² 作为 Version=3 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-45.** CXL HDM Decoder n Control Register layout ｜ CXL HDM 解码器 n 控制寄存器布局
>
> <img src="figures/chapter_08/page_0569.png" alt="Figure 8-45" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0569.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-8"></a>
## 8.2.4.20.8 CXL HDM Decoder n Target List Low Register (Offset 20h*n+24h) | CXL HDM 解码器 n 目标列表低寄存器 (偏移量 20h*n+24h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register is not applicable to devices, which use this field as DPA Skip Low as described in Section 8.2.4.20.9. The targets must be distinct and the identifier cannot repeat. For example, Target Port Identifiers for Interleave Way=0, 1, 2, 3 must be distinct if Control.IW=2.

The Target Port Identifier for a given Downstream Port is reported via the Port Number field in the Link Capabilities register (see PCIe Base Specification).

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 7:0 | RWL | Target Port Identifier for Interleave Way=0: The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |
| 15:8 | RWL | Target Port Identifier for Interleave Way=1: Valid if Decoder n Control.IW>0. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |
| 23:16 | RWL | Target Port Identifier for Interleave Way=2: Valid if Decoder n Control.IW>1. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |
| 31:24 | RWL | Target Port Identifier for Interleave Way=3: Valid if Decoder n Control.IW>1. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |

#### IMPLEMENTATION NOTE: UIW, UIG, and ISP Examples

The switch in Figure 9-16 receives all the HPAs within the range 16-20 TB because interleaving is not performed upstream to the switch. If the switch is capable of routing UIO accesses to CXL.mem, then the HDM decoder that spans 16-20 TB in that switch should be configured as follows:
- UIW=0
- ISP=0
- UIG=Any legal value

The 4 CXL.mem devices, from left to right, are assigned ISP=0 through 3, respectively.

The switch in Figure 9-17 receives every other 4K HPA chunk when the host accesses the range 16-20 TB because the Host Bridge is configured to 2-way interleave at 4K granularity. If the switch is capable of routing UIO accesses to CXL.mem, then the HDM decoder that spans 16-20 TB in that switch should be configured as follows:
- UIW=1 (every other chunk, so 2-way)
- ISP=0 because the switch shown in the figure receives the first chunk (ISP=1 for the switch is not shown in the figure)
- UIG= 4 (every chunk is 4K)

The 8 CXL.mem devices, from left to right, are assigned ISP=0 through 7, respectively.

The switch in Figure 9-18 receives every 4th 2K HPA chunk when the host accesses the range 16-20 TB. If the switch is capable of routing UIO accesses to CXL.mem, then the HDM decoder that spans 16-20 TB in that switch should be configured as follows:
- UIW=2 (every fourth chunk, so 4-way)
- ISP=0 because the switch receives the first chunk
- UIG= 3 (every chunk is 2K)

The 8 CXL.mem devices, from left to right, are assigned ISP=0 through 7, respectively.

</td><td style="background-color:#e8e8e8">

此寄存器不适用于设备, 设备将此字段用作 DPA Skip Low, 如第 8.2.4.20.9 节所述。目标必须不同, 标识符不能重复。例如, 如果 Control.IW=2, 则交织方式 = 0、1、2、3 的目标端口标识符必须不同。

给定下行端口的目标端口标识符通过 Link Capabilities 寄存器中的 Port Number 字段报告 (参见 PCIe 基本规范)。

| 位域 | 属性 | 描述 |
|------|------|------|
| 7:0 | RWL | 交织方式 = 0 的目标端口标识符 (Target Port Identifier for Interleave Way=0): 锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |
| 15:8 | RWL | 交织方式 = 1 的目标端口标识符: 如果解码器 n Control.IW>0 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |
| 23:16 | RWL | 交织方式 = 2 的目标端口标识符: 如果解码器 n Control.IW>1 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |
| 31:24 | RWL | 交织方式 = 3 的目标端口标识符: 如果解码器 n Control.IW>1 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |

#### 实现注意: UIW、UIG 和 ISP 示例

图 9-16 中的交换机接收 16-20 TB 范围内的所有 HPA, 因为在该交换机上游不执行交织。如果交换机能够将 UIO 访问路由到 CXL.mem, 则该交换机中跨越 16-20 TB 的 HDM 解码器应按如下方式配置:
- UIW=0
- ISP=0
- UIG=任何合法值

从左到右, 4 个 CXL.mem 设备分别分配 ISP=0 到 3。

图 9-17 中的交换机在主机访问 16-20 TB 范围时每隔一个 4K HPA 块接收一次, 因为主机桥配置为以 4K 粒度进行 2 路交织。如果交换机能够将 UIO 访问路由到 CXL.mem, 则该交换机中跨越 16-20 TB 的 HDM 解码器应按如下方式配置:
- UIW=1 (每隔一个块, 即 2 路)
- ISP=0, 因为图中所示的交换机接收第一个块 (交换机的 ISP=1 未在图中显示)
- UIG= 4 (每个块为 4K)

从左到右, 8 个 CXL.mem 设备分别分配 ISP=0 到 7。

图 9-18 中的交换机在主机访问 16-20 TB 范围时每第 4 个 2K HPA 块接收一次。如果交换机能够将 UIO 访问路由到 CXL.mem, 则该交换机中跨越 16-20 TB 的 HDM 解码器应按如下方式配置:
- UIW=2 (每第 4 个块, 即 4 路)
- ISP=0, 因为交换机接收第一个块
- UIG= 3 (每个块为 2K)

从左到右, 8 个 CXL.mem 设备分别分配 ISP=0 到 7。

</td></tr>
</tbody>
</table>

> **Figure 8-46.** CXL HDM Decoder n Target List Low Register layout ｜ CXL HDM 解码器 n 目标列表低寄存器布局
>
> <img src="figures/chapter_08/page_0572.png" alt="Figure 8-46" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0572.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-9"></a>
## 8.2.4.20.9 CXL HDM Decoder n DPA Skip Low Register (Offset 20h*n + 24h) | CXL HDM 解码器 n DPA 跳过低寄存器 (偏移量 20h*n + 24h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register is applicable only to devices. For non-devices, this field contains the Target List Low register as described in Section 8.2.4.20.8.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 27:0 | RsvdP | Reserved |
| 31:28 | RWL | DPA Skip Low: Corresponds to bits 31:28 of the DPA Skip length which, when nonzero, specifies a length of DPA space that is skipped, unmapped by any decoder, prior to the HPA-to-DPA mapping provided by this decoder. Default value of this field is 0h. |

</td><td style="background-color:#e8e8e8">

此寄存器仅适用于设备。对于非设备, 此字段包含 Target List Low 寄存器, 如第 8.2.4.20.8 节所述。

| 位域 | 属性 | 描述 |
|------|------|------|
| 27:0 | RsvdP | 保留 |
| 31:28 | RWL | DPA Skip Low: 对应于 DPA 跳过长度的 31:28 位, 当非零时, 指定在由此解码器提供的 HPA 到 DPA 映射之前被跳过 (未由任何解码器映射) 的 DPA 空间长度。该字段的默认值为 0h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-47.** CXL HDM Decoder n DPA Skip Low Register layout ｜ CXL HDM 解码器 n DPA 跳过低寄存器布局
>
> <img src="figures/chapter_08/page_0572.png" alt="Figure 8-47" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0572.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-10"></a>
## 8.2.4.20.10 CXL HDM Decoder n Target List High Register (Offset 20h*n+28h) | CXL HDM 解码器 n 目标列表高寄存器 (偏移量 20h*n+28h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register is not applicable to devices, which use this field as DPA Skip High as described in Section 8.2.4.20.11. Returns the Target Port associated with Interleave Way 4 through 7.

The targets must be distinct. For example, all 8 Target Port Identifiers must be distinct if Control.IW=3.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 7:0 | RWL | Target Port Identifier for Interleave Way=4: Valid if Decoder n Control.IW>2. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |
| 15:8 | RWL | Target Port Identifier for Interleave Way=5: Valid if Decoder n Control.IW>2. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |
| 23:16 | RWL | Target Port Identifier for Interleave Way=6: Valid if Decoder n Control.IW>2. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |
| 31:24 | RWL | Target Port Identifier for Interleave Way=7: Valid if Decoder n Control.IW>2. The locking behavior is described in Section 8.2.4.20.13. Default value of this field is 00h. |

</td><td style="background-color:#e8e8e8">

此寄存器不适用于设备, 设备将此字段用作 DPA Skip High, 如第 8.2.4.20.11 节所述。返回与交织方式 4 到 7 关联的目标端口。

目标必须不同。例如, 如果 Control.IW=3, 则所有 8 个目标端口标识符必须不同。

| 位域 | 属性 | 描述 |
|------|------|------|
| 7:0 | RWL | 交织方式 = 4 的目标端口标识符: 如果解码器 n Control.IW>2 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |
| 15:8 | RWL | 交织方式 = 5 的目标端口标识符: 如果解码器 n Control.IW>2 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |
| 23:16 | RWL | 交织方式 = 6 的目标端口标识符: 如果解码器 n Control.IW>2 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |
| 31:24 | RWL | 交织方式 = 7 的目标端口标识符: 如果解码器 n Control.IW>2 则有效。锁定行为在第 8.2.4.20.13 节中描述。该字段的默认值为 00h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-48.** CXL HDM Decoder n Target List High Register layout ｜ CXL HDM 解码器 n 目标列表高寄存器布局
>
> <img src="figures/chapter_08/page_0572.png" alt="Figure 8-48" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0572.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-11"></a>
## 8.2.4.20.11 CXL HDM Decoder n DPA Skip High Register (Offset 20h*n + 28h) | CXL HDM 解码器 n DPA 跳过高寄存器 (偏移量 20h*n + 28h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register is applicable only to devices. For non-devices, this field contains the Target List High register as described in Section 8.2.4.20.10.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 31:0 | RWL | DPA Skip High: Corresponds to bits 63:32 of the DPA Skip length which, when nonzero, specifies a length of DPA space that is skipped, unmapped by any decoder, prior to the HPA-to-DPA mapping provided by this decoder. Default value of this register is 0000 0000h. |

</td><td style="background-color:#e8e8e8">

此寄存器仅适用于设备。对于非设备, 此字段包含 Target List High 寄存器, 如第 8.2.4.20.10 节所述。

| 位域 | 属性 | 描述 |
|------|------|------|
| 31:0 | RWL | DPA Skip High: 对应于 DPA 跳过长度的 63:32 位, 当非零时, 指定在由此解码器提供的 HPA 到 DPA 映射之前被跳过 (未由任何解码器映射) 的 DPA 空间长度。此寄存器的默认值为 0000 0000h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-49.** CXL HDM Decoder n DPA Skip High Register layout ｜ CXL HDM 解码器 n DPA 跳过高寄存器布局
>
> <img src="figures/chapter_08/page_0573.png" alt="Figure 8-49" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0573.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-12"></a>
## 8.2.4.20.12 Committing Decoder Programming | 提交解码器编程

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

If Software intends to set Lock On Commit, Software must configure the decoders in order. In other words, decoder m must be configured and committed before decoder m+1 for all values of m. Decoder m must cover an HPA range that is below decoder m+1.

Each interleave decoder must be committed before it actively decodes CXL.mem transactions. Software configures all the registers associated with the individual decoder and optionally sets the Lock On Commit bit prior to setting the Commit bit. When the Commit bit in decoder m+1 transitions from 0 to 1 and Lock On Commit=1, the decoder logic shall perform the following consistency checks before setting Committed bit:
- Decoder[m+1].Base >= (Decoder[m].Base+Decoder[m].Size). This ensures that the Base of the decoder being committed is greater than or equal to the limit of the previous decoder. This check is not applicable when committing Decoder 0.
- Decoder[m+1].Base <= Decoder[m+1].Base+Decoder[m+1].Size (no wraparound)
- If Decoder[m+1].IW>=8, Decoder[m+1].Size is a multiple of 3.
- Target Port Identifiers for Interleave Way=0 through 2**IW -1 must be distinct. This ensures no two interleave ways are pointing to the same target.
- Decoder[m].Committed=1. This ensures that the previous decoder is committed and has passed the above checks.

Decoder logic does not allow Decoder[m+1] registers to be modified while these checks are in progress (Commit=1, (Committed OR ErrorNotCommited)=0). If software attempts to modify Decoder[m+1] while the checks are in progress, it will lead to undefined behavior.

These checks ensure that all decoders within a given component are self-consistent and do not create aliasing.

It is legal for software to program Decoder Size to 0 and commit it. Such a decoder will not participate in HDM decode.

If these checks fail and the decoder is not committed, decoder logic shall set Error Not Committed flag. Software may remedy this situation by clearing the Commit bit, reprogramming the decoder with legal values and setting Commit bit once again.

If Lock On Commit=0, decoder logic does not implement the address aliasing checks. Software is fully responsible for avoiding aliasing and protecting the HDM Decoder registers via other mechanisms such as CPU page tables.

Regardless of the setting of the Lock on Commit bit, the decoder logic in a UIO-capable switch or root port shall ensure that the number of decoders configured with UIO=1 does not exceed the number of UIO-capable decoders encoded in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1). If software attempts to violate this restriction, the decode logic shall set ErrorOnCommit=1.

If the device requires BI for managing coherency, software must ensure that the BI bit in the HDM Decoder Control register is set before committing the HDM decoder; otherwise, the device operation is undefined. Software must ensure that the device and any applicable DSPs, USPs, and the RP are configured such that the device is able to issue a BISnp request before committing any HDM decoder with the BI bit set; otherwise, the device operation is undefined.

Decoder logic shall set either Committed or Error Not Committed flag within 10 ms of a write to the Commit bit.

</td><td style="background-color:#e8e8e8">

如果软件打算设置 Lock On Commit, 则软件必须按顺序配置解码器。换言之, 对于 m 的所有值, 解码器 m 必须在解码器 m+1 之前被配置和提交。解码器 m 必须覆盖低于解码器 m+1 的 HPA 范围。

每个交织解码器必须在主动解码 CXL.mem 事务之前被提交。软件配置与各个解码器关联的所有寄存器, 并可选择在设置 Commit 位之前设置 Lock On Commit 位。当解码器 m+1 中的 Commit 位从 0 转换为 1 且 Lock On Commit=1 时, 解码器逻辑应在设置 Committed 位之前执行以下一致性检查:
- Decoder[m+1].Base >= (Decoder[m].Base+Decoder[m].Size)。这确保正在提交的解码器的基地址大于或等于前一个解码器的限制。提交解码器 0 时此检查不适用。
- Decoder[m+1].Base <= Decoder[m+1].Base+Decoder[m+1].Size (无回绕)
- 如果 Decoder[m+1].IW>=8, 则 Decoder[m+1].Size 是 3 的倍数。
- 交织方式 = 0 到 2**IW -1 的目标端口标识符必须不同。这确保没有两个交织方式指向同一目标。
- Decoder[m].Committed=1。这确保前一个解码器已被提交并通过了上述检查。

在这些检查进行时 (Commit=1, (Committed OR ErrorNotCommited)=0), 解码器逻辑不允许修改 Decoder[m+1] 寄存器。如果软件尝试在检查进行时修改 Decoder[m+1], 将导致未定义的行为。

这些检查确保给定组件内的所有解码器自洽且不会产生别名。

软件将解码器 Size 编程为 0 并提交它是合法的。这样的解码器将不参与 HDM 解码。

如果这些检查失败且解码器未提交, 则解码器逻辑应设置 Error Not Committed 标志。软件可以通过清除 Commit 位、用合法值重新编程解码器并再次设置 Commit 位来纠正这种情况。

如果 Lock On Commit=0, 则解码器逻辑不实现地址别名检查。软件完全负责避免别名并通过其他机制 (例如 CPU 页表) 保护 HDM 解码器寄存器。

无论 Lock on Commit 位的设置如何, 支持 UIO 的交换机或根端口中的解码器逻辑都应确保 UIO=1 配置的解码器数量不超过 CXL HDM Decoder Capability 寄存器 (参见第 8.2.4.20.1 节) 中编码的支持 UIO 的解码器数量。如果软件尝试违反此限制, 则解码逻辑应设置 ErrorOnCommit=1。

如果设备需要 BI 来管理一致性, 软件必须确保在提交 HDM 解码器之前已设置 HDM Decoder Control 寄存器中的 BI 位; 否则, 设备操作未定义。软件必须确保设备和任何适用的 DSP、USP 以及 RP 已配置为使设备能够在提交任何设置了 BI 位的 HDM 解码器之前发出 BISnp 请求; 否则, 设备操作未定义。

解码器逻辑应在写入 Commit 位后 10 毫秒内设置 Committed 或 Error Not Committed 标志。

</td></tr>
</tbody>
</table>

> **Figure 8-50.** Decoder Commit Flow diagram ｜ 解码器提交流程图
>
> <img src="figures/chapter_08/page_0573.png" alt="Figure 8-50" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0573.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-20-13"></a>
## 8.2.4.20.13 Decoder Protection | 解码器保护

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Software may choose to set the Lock On Commit bit prior to setting Commit. If the Lock On Commit bit is 1, Decoder logic shall perform alias checks listed in the previous section prior to committing the decoder and further disallow modifications to all RWL fields in that decoder when the decoder is in Committed state.

If the Lock On Commit bit is 0, software may clear the Commit bit, reprogram the decoder fields, and then set the Commit bit again for the new values to take effect. Reprogramming the decoder while the Commit bit is set results in undefined behavior. To avoid misbehavior, software is responsible for quiescing memory traffic that is targeting the decoder while it is being reprogrammed. If decoder logic does not positively decode an address of a read, it may either return all 1s or return poison based on the CXL HDM Decoder Global Control register setting. During reprogramming, software must follow the same restrictions as the initial programming. Specifically, decoder m must be configured and committed before decoder m+1 for all values of m; Decoder m must cover an HPA range that is below decoder m+1 and all Targets must be distinct.

#### IMPLEMENTATION NOTE

Software may set Lock On Commit=1 in systems that do not support Hot-Plug. In such systems, the decoders are generally programmed at boot, can be arranged in increasing HPA order and never modified until the next reset.

If the system supports CXL Hot-Plug, software may need significant flexibility in terms of reprogramming the decoders during runtime. In such systems, software may choose to leave Lock On Commit=0.

#### IMPLEMENTATION NOTE: CXL Host Bridge and Upstream Switch Port Decode Flow

Step 1: Check if the incoming HPA satisfies Base <= HPA < Base+Size for any active decoder. If no decoder satisfies this equation for a write, drop the writes. If no decoder satisfies this equation for a read and Poison On Decode Error Enable=0, return all 1s. If no decoder satisfies this equation for a read and Poison On Decode Error Enable=1, return poison.

Step 2: If Decoder[n] satisfies this equation:
- Extract IW bits starting with bit position IG+8 in HPA¹. This returns the Interleave Way
- Send transactions to Downstream Port=Decoder[n].Target List[Interleave Way]

Example:
- HPA = 129 GB + 1028d
- Decoder[2].Base= 128 GB, Decoder[2].Size = 4 GB.
- Assume IW=2 (4 way), IG = 1 (512 bytes).

Step 1: Decoder[2] positively decodes this address, so n=2.

Step 2: Extracting bits 10:9 from HPA returns Interleave Way=2 (HPA=… xxxx 0000 0100 0000 0100b)

Forward access to Port number Decoder[2].Target List Low[23:16]

¹ In the general case, the bits must be extracted from (HPA – Base[n]). However, Decoder Base is a multiple of 256M and the highest interleave granularity is 16K. Therefore, extracting IW bits from HPA still returns the correct Index value.

#### IMPLEMENTATION NOTE: Device Decode Logic

As part of Commit processing flow, the device decoder logic may accumulate DPABase field for every decoder as follows:
- Decoder[0].DPABase = Decoder[0].DPASkip
- If IW <8, Decoder[m+1]. DPABase = Decoder[m+1].DPASkip + Decoder[m].DPABase + (Decoder[m].Size / 2 ** Decoder[m].IW)
- If IW >=8, Decoder[m+1]. DPABase = Decoder[m+1].DPASkip + Decoder[m].DPABase + (Decoder[m].Size / (3 * 2 ** (Decoder[m].IW-8))

DPABase is not exposed to software, but may be tracked internally by the decoder logic to speed up decode process. Decoder[m].DPABase represents the lowest DPA that the lowest HPA decoded by Decoder[m] maps to. The DPA mappings for a device typically start at DPA 0 for Decoder[0] and are sequentially accumulated with each additional decoder used; however, the DPASkip field in the decoder may be used to leave ranges of DPA unmapped, as required by the needs of the platform.

During the decode:

Step 1: Check if the incoming HPA satisfies Base <= HPA < Base+Size for any active decoder. If no decoder satisfies this equation for a write, drop the writes. If no decoder satisfies this equation for a read and Poison On Decode Error Enable=0, return all 1s. If no decoder satisfies this equation for a read and Poison On Decode Error Enable=1, return poison.

Step 2: If Decoder[n] satisfies this equation.
- Calculate HPAOffset = HPA – Decoder[n].Base
- If IW <8, removes IW bits starting with bit position IG+8 in HPAOffset to get DPAOffset. This operation will right shift the bits above IG+IW+8 by IW positions.
  - DPAOffset[51:IG+8]=(HPAOffset[51:IG+8+IW]
  - DPAOffset[IG+7:0]=HPAOffset[IG+7:0].
- If IW >=8, an integer, divide by 3 operation is involved
  - DPAOffset[51:IG+8]=HPAOffset[51:IG+IW]/ 3
  - DPAOffset[IG+7:0]=HPAOffset[IG+7:0]
- DPA=DPAOffset + Decoder[n].DPABase.

The above calculation is applied by the device regardless of the Interleave Arithmetic field in the corresponding CFMWS entry.

Example:
- HPA = 129 GB + 1028d
- Software programmed Decoder[0].Base= 32 GB, Decoder[0].Size = 32 GB.
- Software programmed Decoder[1].Base= 128 GB, Decoder[1].Size = 4 GB.
- Assume IW=3 (8 way), IG = 1 (512 bytes) for both decoders.
- Decoder[1].DPABase= 32/8 GB = 4 GB

Step 1: Select Decoder[1].

Step 2:
- HPAOffset = 1 GB + 1028d (4000 0404h, 0404h=0000 0100 0000 0100b)
- Removing bits 11:9 from HPA returns DPAOffset=800 0004h.

</td><td style="background-color:#e8e8e8">

软件可以选择在设置 Commit 之前设置 Lock On Commit 位。如果 Lock On Commit 位为 1, 则解码器逻辑应在提交解码器之前执行上一节中列出的别名检查, 并在该解码器处于 Committed 状态时进一步禁止修改该解码器中的所有 RWL 字段。

如果 Lock On Commit 位为 0, 则软件可以清除 Commit 位, 重新编程解码器字段, 然后再次设置 Commit 位以使新值生效。在 Commit 位已设置时重新编程解码器会导致未定义的行为。为避免误操作, 软件有责任在重新编程期间使面向该解码器的内存流量静止。如果解码器逻辑未对读地址进行正确定向解码, 则它可以根据 CXL HDM Decoder Global Control 寄存器设置返回全 1 或返回 Poison。在重新编程期间, 软件必须遵循与初始编程相同的限制。具体而言, 对于 m 的所有值, 解码器 m 必须在解码器 m+1 之前被配置和提交; 解码器 m 必须覆盖低于解码器 m+1 的 HPA 范围, 并且所有 Targets 必须不同。

#### 实现注意

在不支持热插拔的系统中, 软件可以将 Lock On Commit 设置为 1。在此类系统中, 解码器通常在启动时编程, 可以按递增的 HPA 顺序排列, 并且在下次复位之前不会修改。

如果系统支持 CXL 热插拔, 则软件可能需要在运行时重新编程解码器方面具有显著的灵活性。在此类系统中, 软件可以选择将 Lock On Commit 保留为 0。

#### 实现注意: CXL 主机桥和上行交换机端口解码流程

第 1 步: 检查传入的 HPA 是否满足 Base <= HPA < Base+Size 适用于任何活动解码器。如果没有解码器对写入满足此等式, 则丢弃写入。如果没有解码器对读取满足此等式, 且 Poison On Decode Error Enable=0, 则返回全 1。如果没有解码器对读取满足此等式, 且 Poison On Decode Error Enable=1, 则返回 Poison。

第 2 步: 如果 Decoder[n] 满足此等式:
- 从 HPA¹ 中的位位置 IG+8 开始提取 IW 位。这将返回 Interleave Way
- 将事务发送到 Downstream Port=Decoder[n].Target List[Interleave Way]

示例:
- HPA = 129 GB + 1028d
- Decoder[2].Base= 128 GB, Decoder[2].Size = 4 GB。
- 假设 IW=2 (4 路), IG = 1 (512 字节)。

第 1 步: Decoder[2] 对该地址进行正确定向解码, 因此 n=2。

第 2 步: 从 HPA 提取位 10:9 返回 Interleave Way=2 (HPA=… xxxx 0000 0100 0000 0100b)

将访问转发到端口号 Decoder[2].Target List Low[23:16]

¹ 一般情况下, 必须从 (HPA – Base[n]) 中提取位。但是, 解码器 Base 是 256M 的倍数, 最高交织粒度为 16K。因此, 从 HPA 提取 IW 位仍会返回正确的 Index 值。

#### 实现注意: 设备解码逻辑

作为 Commit 处理流程的一部分, 设备解码逻辑可能会为每个解码器累积 DPABase 字段, 如下所示:
- Decoder[0].DPABase = Decoder[0].DPASkip
- 如果 IW <8, Decoder[m+1].DPABase = Decoder[m+1].DPASkip + Decoder[m].DPABase + (Decoder[m].Size / 2 ** Decoder[m].IW)
- 如果 IW >=8, Decoder[m+1].DPABase = Decoder[m+1].DPASkip + Decoder[m].DPABase + (Decoder[m].Size / (3 * 2 ** (Decoder[m].IW-8))

DPABase 不暴露给软件, 但可以由解码器逻辑在内部跟踪以加速解码过程。Decoder[m].DPABase 表示由 Decoder[m] 解码的最低 HPA 映射到的最低 DPA。设备的 DPA 映射通常从 Decoder[0] 的 DPA 0 开始, 并随着使用的每个附加解码器顺序累积; 但是, 解码器中的 DPASkip 字段可用于按需将 DPA 范围保留为未映射状态。

在解码过程中:

第 1 步: 检查传入的 HPA 是否满足 Base <= HPA < Base+Size 适用于任何活动解码器。如果没有解码器对写入满足此等式, 则丢弃写入。如果没有解码器对读取满足此等式, 且 Poison On Decode Error Enable=0, 则返回全 1。如果没有解码器对读取满足此等式, 且 Poison On Decode Error Enable=1, 则返回 Poison。

第 2 步: 如果 Decoder[n] 满足此等式。
- 计算 HPAOffset = HPA – Decoder[n].Base
- 如果 IW <8, 则删除 HPAOffset 中从位位置 IG+8 开始的 IW 位以获得 DPAOffset。此操作会将 IG+IW+8 之上的位右移 IW 位。
  - DPAOffset[51:IG+8]=(HPAOffset[51:IG+8+IW]
  - DPAOffset[IG+7:0]=HPAOffset[IG+7:0]。
- 如果 IW >=8, 则涉及整数除以 3 操作
  - DPAOffset[51:IG+8]=HPAOffset[51:IG+IW]/3
  - DPAOffset[IG+7:0]=HPAOffset[IG+7:0]
- DPA=DPAOffset + Decoder[n].DPABase。

无论相应 CFMWS 条目中的 Interleave Arithmetic 字段如何, 设备都会应用上述计算。

示例:
- HPA = 129 GB + 1028d
- 软件编程 Decoder[0].Base= 32 GB, Decoder[0].Size = 32 GB。
- 软件编程 Decoder[1].Base= 128 GB, Decoder[1].Size = 4 GB。
- 假设两个解码器的 IW=3 (8 路), IG = 1 (512 字节)。
- Decoder[1].DPABase= 32/8 GB = 4 GB

第 1 步: 选择 Decoder[1]。

第 2 步:
- HPAOffset = 1 GB + 1028d (4000 0404h, 0404h=0000 0100 0000 0100b)
- 从 HPA 中删除位 11:9 返回 DPAOffset=800 0004h。

</td></tr>
</tbody>
</table>

> **Figure 8-51.** Decoder Protection Flow ｜ 解码器保护流程
>
> <img src="figures/chapter_08/page_0574.png" alt="Figure 8-51" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0574.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-21"></a>
## 8.2.4.21 CXL Extended Security Capability Structure | CXL 扩展安全能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This capability structure applies only to the CXL Host Bridge and may be located in CHBCR.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Extended Security Structure Entry Count.n (Max 256) |
| 04h | Root Port 1 Security Policy |
| 08h | Root Port 1 ID |
| 0Ch | Root Port 2 Security Policy |
| 10h | Root Port 2 ID |
| … | … |
| 8*n-4 | Root Port n Security Policy |
| 8*n | Root Port n ID |

> **Table 8-28.** CXL Extended Security Structure Entry Count (Offset 00h)
>
> | Bit Location | Attributes | Description |
> |--------------|------------|-------------|
> | 7:0 | HwInit | Root Port Count: The number of Extended Security Structures that are part of this capability structure. The number of entries must match the CXL.cache-capable Root Ports that are associated with this Host Bridge. Each entry consists of two DWORD registers - Security Policy and Root Port ID. |
> | 31:8 | RsvdP | Reserved |

> **Table 8-29.** Root Port n Security Policy Register (Offset 8*n-4)
>
> | Bit Location | Attributes | Description |
> |--------------|------------|-------------|
> | 1:0 | RW | Trust Level: If the host supports only 1 CXL.cache device per VCS, this field defines the Trust Level for the CXL.cache Device below Root Port n (see Table 8-26 for definition of this field). If the host supports more than 1 CXL.cache device per VCS, this field defines the Trust Level that is applied to all the CXL.cache devices below this root port. For an HDM-DB device, Trust Level=01 is equivalent to 00. Default value of this field is 10b. |
> | 31:2 | RsvdP | Reserved |

> **Table 8-30.** Root Port n ID Register (Offset 8*n)
>
> | Bit Location | Attributes | Description |
> |--------------|------------|-------------|
> | 7:0 | HwInit | Port Identifier of Root Port n (referenced using the Port Number field in the Link Capabilities register (see PCIe Base Specification)). |
> | 31:8 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

此能力结构仅适用于 CXL 主机桥, 可以位于 CHBCR 中。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Extended Security Structure Entry Count.n (最多 256) |
| 04h | Root Port 1 Security Policy |
| 08h | Root Port 1 ID |
| 0Ch | Root Port 2 Security Policy |
| 10h | Root Port 2 ID |
| … | … |
| 8*n-4 | Root Port n Security Policy |
| 8*n | Root Port n ID |

> **表 8-28.** CXL Extended Security Structure Entry Count (偏移量 00h) ｜ CXL 扩展安全结构条目计数
>
> | 位域 | 属性 | 描述 |
> |------|------|------|
> | 7:0 | HwInit | Root Port Count: 属于此能力结构的扩展安全结构数量。条目数必须与与此主机桥相关联的具有 CXL.cache 能力的根端口相匹配。每个条目由两个 DWORD 寄存器组成 - Security Policy 和 Root Port ID。 |
> | 31:8 | RsvdP | 保留 |

> **表 8-29.** Root Port n Security Policy Register (偏移量 8*n-4) ｜ 根端口 n 安全策略寄存器
>
> | 位域 | 属性 | 描述 |
> |------|------|------|
> | 1:0 | RW | Trust Level: 如果主机每个 VCS 仅支持 1 个 CXL.cache 设备, 则此字段定义根端口 n 下方 CXL.cache 设备的 Trust Level (此字段的定义请参见表 8-26)。如果主机每个 VCS 支持多个 CXL.cache 设备, 则此字段定义应用于此根端口下方所有 CXL.cache 设备的 Trust Level。对于 HDM-DB 设备, Trust Level=01 等效于 00。该字段的默认值为 10b。 |
> | 31:2 | RsvdP | 保留 |

> **表 8-30.** Root Port n ID Register (偏移量 8*n) ｜ 根端口 n ID 寄存器
>
> | 位域 | 属性 | 描述 |
> |------|------|------|
> | 7:0 | HwInit | 根端口 n 的端口标识符 (使用 Link Capabilities 寄存器 (参见 PCIe 基本规范) 中的 Port Number 字段引用)。 |
> | 31:8 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-52.** CXL Extended Security Capability Structure layout ｜ CXL 扩展安全能力结构布局
>
> <img src="figures/chapter_08/page_0577.png" alt="Figure 8-52" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0577.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22"></a>
## 8.2.4.22 CXL IDE Capability Structure | CXL IDE 能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Offset | Register Name |
|--------|---------------|
| 00h | CXL IDE Capability Register |
| 04h | CXL IDE Control |
| 08h | CXL IDE Status |
| 0Ch | CXL IDE Error Status |
| 10h | Key Refresh Time Capability |
| 14h | Truncation Transmit Delay Capability |
| 18h | Key Refresh Time Control |
| 1Ch | Truncation Transmit Delay Control |
| 20h | Key Refresh Time Capability2 |

</td><td style="background-color:#e8e8e8">

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL IDE Capability Register |
| 04h | CXL IDE Control |
| 08h | CXL IDE Status |
| 0Ch | CXL IDE Error Status |
| 10h | Key Refresh Time Capability |
| 14h | Truncation Transmit Delay Capability |
| 18h | Key Refresh Time Control |
| 1Ch | Truncation Transmit Delay Control |
| 20h | Key Refresh Time Capability2 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-1"></a>
### 8.2.4.22.1 CXL IDE Capability (Offset 00h) | CXL IDE 能力 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | HwInit | CXL IDE Capable: When set, indicates that the Port supports CXL IDE. |
| 16:1 | HwInit | Supported CXL IDE Modes:<br>• Bit[1]: If set, Skid mode is supported.<br>• Bit[2]: If set, Containment mode is supported. If bit 0 of this register is set, this bit must be set as well.<br>• Bits[16:3]: Reserved. |
| 21:17 | HwInit | Supported Algorithms: Indicates the supported algorithms for securing CXL IDE, encoded as:<br>• 00h = AES-GCM 256-bit key size, 96-bit MAC<br>• All other encodings are reserved |
| 22 | HwInit/RsvdP | IDE.Stop Capable: Indicates that the port Tx supports generation of IDE.Stop control flit and the port Rx supports processing of IDE.Stop control flit when operating in 256B Flit mode (see Section 11.3.10). This bit is reserved for ports that are not capable of operating in 256B Flit mode.¹ |
| 23 | HwInit/RsvdP | LOpt IDE Capable: If set, this component supports IDE when the link is operating in Latency-Optimized 256B Flit mode (see Figure 11-13 and Figure 11-14).² If 0, this component does not support IDE when the link is operating in Latency-Optimized 256B Flit mode. If the link is operating in Latency-Optimized 256B Flit mode, the System Firmware or System Software must clear the CXL_Latency_Optimized_256B_Flit_Enable bit the DVSEC Flex Bus Port Control register (see Section 8.2.1.3.2) in the Downstream Port and then retrain the link prior to enabling IDE. After IDE is terminated, the System Firmware or System Software may set the CXL_Latency_Optimized_256B_Flit_Enable bit in the Downstream Port and then retrain the link so that the link can transition to Latency-Optimized 256B Flit mode.² |
| 24 | HwInit/RsvdP | IDE Protect LLCTRL Poison Message Capable: If set, this component supports IDE protection of LLCTRL In-band Error poison information. |
| 31:25 | RsvdP | Reserved |

¹ This bit was introduced as part of Version=2.
² This bit was introduced as part of Version=3.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | HwInit | CXL IDE Capable: 置位时, 表示端口支持 CXL IDE。 |
| 16:1 | HwInit | Supported CXL IDE Modes (支持的 CXL IDE 模式):<br>• 位 [1]: 置位时, 支持 Skid 模式。<br>• 位 [2]: 置位时, 支持 Containment 模式。如果此寄存器的位 0 已置位, 则此位也必须置位。<br>• 位 [16:3]: 保留。 |
| 21:17 | HwInit | Supported Algorithms: 指示用于保护 CXL IDE 的支持算法, 编码如下:<br>• 00h = AES-GCM 256 位密钥大小, 96 位 MAC<br>• 所有其他编码保留 |
| 22 | HwInit/RsvdP | IDE.Stop Capable: 表示端口 Tx 支持生成 IDE.Stop 控制 Flit, 端口 Rx 支持在以 256B Flit 模式操作时处理 IDE.Stop 控制 Flit (参见第 11.3.10 节)。对于无法以 256B Flit 模式操作的端口, 此位保留。¹ |
| 23 | HwInit/RsvdP | LOpt IDE Capable: 置位时, 此组件在链路以延迟优化 256B Flit 模式操作时支持 IDE (参见图 11-13 和图 11-14)。² 为 0 时, 此组件在链路以延迟优化 256B Flit 模式操作时不支持 IDE。如果链路以延迟优化 256B Flit 模式操作, 则系统固件或系统软件必须清除 DVSEC Flex Bus Port Control 寄存器 (参见第 8.2.1.3.2 节) 下行端口中的 CXL_Latency_Optimized_256B_Flit_Enable 位, 然后在启用 IDE 之前重新训练链路。在 IDE 终止后, 系统固件或系统软件可以设置下行端口中的 CXL_Latency_Optimized_256B_Flit_Enable 位, 然后重新训练链路, 以便链路可以转换到延迟优化 256B Flit 模式。² |
| 24 | HwInit/RsvdP | IDE Protect LLCTRL Poison Message Capable: 置位时, 此组件支持对 LLCTRL 带内错误 Poison 信息的 IDE 保护。 |
| 31:25 | RsvdP | 保留 |

¹ 此位作为 Version=2 的一部分引入。
² 此位作为 Version=3 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-53.** CXL IDE Capability Register layout ｜ CXL IDE 能力寄存器布局
>
> <img src="figures/chapter_08/page_0578.png" alt="Figure 8-53" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0578.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-2"></a>
### 8.2.4.22.2 CXL IDE Control (Offset 04h) | CXL IDE 控制 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW | PCRC Disable: When set, PCRC generation is disabled and MAC calculation does not include PCRC. Software must ensure that this bit is programmed consistently on both ends of the CXL link. Changes to this bit when CXL.cachemem IDE is active results in undefined behavior. The default value of this bit is 0. |
| 1 | RW/RsvdP | IDE.Stop Enable: Enables generation of IDE.Stop control flit by the port Tx and processing of IDE.Stop control flit by port Rx when operating in 256B Flit mode.¹ This bit must be RW if the IDE Stop Capable bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the IDE.Stop Capable bit is set to 1. The default value of this bit is 0. |
| 2 | RW/RsvdP | IDE Protect LLCTRL Poison Message Enable: Enables IDE protection of LLCTRL In-band Error poison. The bit must be RW if IDE Protect LLCTRL Poison Message Capable bit is set. Software must not set this bit unless both ends of the link have the IDE Protect LLCTRL Poison Message Capable bit set. Default value of this bit is 0. |
| 31:3 | RsvdP | Reserved |

¹ This bit was introduced as part of Version=2.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW | PCRC Disable: 置位时, 禁用 PCRC 生成, MAC 计算不包括 PCRC。软件必须确保在 CXL 链路两端一致地编程此位。在 CXL.cachemem IDE 处于活动状态时更改此位会导致未定义的行为。该位的默认值为 0。 |
| 1 | RW/RsvdP | IDE.Stop Enable: 在以 256B Flit 模式操作时, 启用端口 Tx 生成 IDE.Stop 控制 Flit 和端口 Rx 处理 IDE.Stop 控制 Flit。¹ 如果 IDE Stop Capable 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 IDE.Stop Capable 位置 1, 否则软件不得设置此位。该位的默认值为 0。 |
| 2 | RW/RsvdP | IDE Protect LLCTRL Poison Message Enable: 启用 LLCTRL 带内错误 Poison 的 IDE 保护。如果 IDE Protect LLCTRL Poison Message Capable 位置位, 则该位必须为 RW。除非链路两端都设置了 IDE Protect LLCTRL Poison Message Capable 位, 否则软件不得设置此位。该位的默认值为 0。 |
| 31:3 | RsvdP | 保留 |

¹ 此位作为 Version=2 的一部分引入。

</td></tr>
</tbody>
</table>

> **Figure 8-54.** CXL IDE Control Register layout ｜ CXL IDE 控制寄存器布局
>
> <img src="figures/chapter_08/page_0579.png" alt="Figure 8-54" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0579.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-3"></a>
### 8.2.4.22.3 CXL IDE Status (Offset 08h) | CXL IDE 状态 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RO | Rx IDE Status:<br>• 0h = Reserved<br>• 1h = Active Containment mode<br>• 2h = Active Skid mode<br>• 4h = Insecure State<br>• All other encodings are reserved |
| 7:4 | RO | Tx IDE Status:<br>• 0h = Reserved<br>• 1h = Active Containment mode<br>• 2h = Active Skid mode<br>• 4h = Insecure State<br>• All other encodings are reserved |
| 31:8 | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RO | Rx IDE Status (Rx IDE 状态):<br>• 0h = 保留<br>• 1h = 活动 Containment 模式<br>• 2h = 活动 Skid 模式<br>• 4h = 不安全状态 (Insecure State)<br>• 所有其他编码保留 |
| 7:4 | RO | Tx IDE Status (Tx IDE 状态):<br>• 0h = 保留<br>• 1h = 活动 Containment 模式<br>• 2h = 活动 Skid 模式<br>• 4h = 不安全状态 (Insecure State)<br>• 所有其他编码保留 |
| 31:8 | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-55.** CXL IDE Status Register layout ｜ CXL IDE 状态寄存器布局
>
> <img src="figures/chapter_08/page_0579.png" alt="Figure 8-55" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0579.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-4"></a>
### 8.2.4.22.4 CXL IDE Error Status (Offset 0Ch) | CXL IDE 错误状态 (偏移量 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RW1CS | Rx Error Status: Describes the error condition that transitioned the link to Insecure State if IDE stream is active. The component behavior upon this transition is defined in Section 11.3.8.<br>• 0h = No Error<br>• 1h = Integrity failure on received secure traffic<br>• 2h = MAC or Truncated MAC received when the link is not in secure mode (when integrity is not enabled and the receiver detects MAC header)<br>• 3h = MAC header received when not expected (No MAC epoch running, but the receiver detects a MAC header)<br>• 4h = MAC header is not received when expected (MAC header not received within 6 flits after MAC epoch has terminated)<br>• 5h = Truncated MAC flit is received when not expected (if the receiver gets truncated MAC flit corresponding to a completed MAC epoch)<br>• 6h = After early MAC termination, the receiver detects a protocol flit before the truncation delay<br>• 7h = This error code encompasses the following conditions: Protocol flit received earlier than expected after key change (see Section 11.3.7 for the detailed timing requirements); Rx IDE Stop.Enable=1 and a protocol flit received earlier than expected after an IDE Termination Handshake (see Section 11.3.10 for the detailed timing requirements)<br>• 8h = CXL.cachemem IDE Establishment Security error. This error code encompasses the following conditions: IDE.Start is received prior to a successful CXL_KEY_PROG since the last Conventional Reset; IDE.Start is received prior to a successful CXL_KEY_PROG since the last IDE.Start; IDE.Start is received prior to a successful CXL_K_SET_GO since the last Conventional Reset; IDE.Start is received prior to a successful CXL_K_SET_GO since the last IDE.Start; CXL_IDE_KM message received over a different SPDM session (see Section 11.4.2); IDE.Start is received in the middle of a MAC epoch (see Section 11.3.7)<br>All other encodings are reserved |
| 7:4 | RW1CS | Tx IDE Status<br>• 0h = No Error<br>• All other encodings are reserved |
| 8 | RW1CS | Unexpected IDE.Stop Received: This bit is set by the Rx port upon the following conditions:<br>• Received IDE.Stop Link Layer Control flit while CXL.cachemem IDE is active, but prior to a successful CXL_K_SET_STOP since the last IDE.Start (see Section 11.4.6)<br>• Received IDE.Stop Link Layer Control flit while IDE Stop.Enable=0 and IDE Stop.Capable=1 (see Section 11.3.10)<br>• Received IDE.Stop Link Layer Control flit while IDE session is not active (see Section 11.3.10)<br>• Valid TMAC sequence not received before IDE.Stop (see Section 11.3.10)<br>In all of these cases, the Rx shall drop the IDE.Stop but shall not terminate the CXL.cachemem IDE session if one is active. |
| 31:9 | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RW1CS | Rx Error Status: 描述在 IDE 流处于活动状态时使链路转换到不安全状态的错误条件。组件在此转换时的行为在第 11.3.8 节中定义。<br>• 0h = 无错误<br>• 1h = 接收到的安全流量上的完整性故障<br>• 2h = 在链路不处于安全模式时接收到 MAC 或截断 MAC (在未启用完整性且接收方检测到 MAC 头时)<br>• 3h = 在未预期时接收到 MAC 头 (MAC epoch 未运行, 但接收方检测到 MAC 头)<br>• 4h = 在预期时未接收到 MAC 头 (在 MAC epoch 终止后 6 个 Flit 内未接收到 MAC 头)<br>• 5h = 在未预期时接收到截断 MAC Flit (如果接收方接收到与已完成的 MAC epoch 对应的截断 MAC Flit)<br>• 6h = 在提前 MAC 终止后, 接收方在截断延迟之前检测到协议 Flit<br>• 7h = 此错误代码包含以下条件: 密钥更改后比预期更早接收到协议 Flit (详细时序要求参见第 11.3.7 节); Rx IDE Stop.Enable=1 且在 IDE 终止握手之后比预期更早接收到协议 Flit (详细时序要求参见第 11.3.10 节)<br>• 8h = CXL.cachemem IDE 建立安全错误。此错误代码包含以下条件: 自上次常规复位以来在成功执行 CXL_KEY_PROG 之前接收到 IDE.Start; 自上次 IDE.Start 以来在成功执行 CXL_KEY_PROG 之前接收到 IDE.Start; 自上次常规复位以来在成功执行 CXL_K_SET_GO 之前接收到 IDE.Start; 自上次 IDE.Start 以来在成功执行 CXL_K_SET_GO 之前接收到 IDE.Start; 通过不同的 SPDM 会话接收到 CXL_IDE_KM 消息 (参见第 11.4.2 节); 在 MAC epoch 中间接收到 IDE.Start (参见第 11.3.7 节)<br>所有其他编码保留 |
| 7:4 | RW1CS | Tx IDE Status<br>• 0h = 无错误<br>• 所有其他编码保留 |
| 8 | RW1CS | Unexpected IDE.Stop Received: 该位由 Rx 端口在以下条件下设置:<br>• 在 CXL.cachemem IDE 处于活动状态时, 但自上次 IDE.Start 以来成功执行 CXL_K_SET_STOP 之前, 接收到 IDE.Stop 链路层控制 Flit (参见第 11.4.6 节)<br>• 在 IDE Stop.Enable=0 且 IDE Stop.Capable=1 时, 接收到 IDE.Stop 链路层控制 Flit (参见第 11.3.10 节)<br>• 在 IDE 会话未处于活动状态时, 接收到 IDE.Stop 链路层控制 Flit (参见第 11.3.10 节)<br>• 在 IDE.Stop 之前未接收到有效的 TMAC 序列 (参见第 11.3.10 节)<br>在所有这些情况下, Rx 应丢弃 IDE.Stop, 但如果 CXL.cachemem IDE 会话处于活动状态, 则不应终止该会话。 |
| 31:9 | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-56.** CXL IDE Error Status Register layout ｜ CXL IDE 错误状态寄存器布局
>
> <img src="figures/chapter_08/page_0580.png" alt="Figure 8-56" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0580.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-5"></a>
### 8.2.4.22.5 Key Refresh Time Capability (Offset 10h) | 密钥刷新时间能力 (偏移量 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 31:0 | HwInit | Rx Min Key Refresh Time: Number of IDE.Idle flits the receiver needs before it is ready to receive protocol flits after IDE.Start is received when operating in 68B Flit mode. Tx Key Refresh Time (see Section 8.2.4.22.7) field of the transmitter is configured by System Software to block transmission of protocol flits for at least this duration when switching keys (see Section 11.3.7) or terminating IDE (see Section 11.3.10) when the link is operating in 68B Flit mode. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 31:0 | HwInit | Rx Min Key Refresh Time: 在 68B Flit 模式下操作时, 接收方在接收到 IDE.Start 后准备好接收协议 Flit 所需的 IDE.Idle Flit 数量。发射方的 Tx Key Refresh Time 字段 (参见第 8.2.4.22.7 节) 由系统软件配置, 以在切换密钥 (参见第 11.3.7 节) 或终止 IDE (参见第 11.3.10 节) 时阻止协议 Flit 传输至少持续此时间, 此时链路以 68B Flit 模式操作。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-6"></a>
### 8.2.4.22.6 Truncation Transmit Delay Capability (Offset 14h) | 截断传输延迟能力 (偏移量 14h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 7:0 | HwInit | Rx Min Truncation Transmit Delay: Number of IDE.Idle flits the receiver needs before it is ready to receive protocol flits after a Truncated MAC is received when operating in 68B Flit mode. The Tx Truncation Transmit Delay (see Section 8.2.4.22.8) field of the transmitter is configured, by software, to block transmission of protocol flits for at least this duration when the link is operating in 68B Flit mode. |
| 15:8 | HwInit | Rx Min Truncation Transmit Delay²: Number of IDE.Idle flits the receiver needs before it is ready to receive protocol flits after a Truncated MAC is received when operating in 256B Flit mode. The Tx Truncation Transmit Delay (see Section 8.2.4.22.8) field of the transmitter is configured, by software, to block transmission of protocol flits for at least this duration when the link is operating in 256B Flit mode.¹ |
| 31:16 | RsvdP | Reserved |

¹ This field was introduced as part of Version=2.

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 7:0 | HwInit | Rx Min Truncation Transmit Delay: 在 68B Flit 模式下操作时, 接收方在接收到 Truncated MAC 后准备好接收协议 Flit 所需的 IDE.Idle Flit 数量。发射方的 Tx Truncation Transmit Delay 字段 (参见第 8.2.4.22.8 节) 由软件配置, 以在链路以 68B Flit 模式操作时阻止协议 Flit 传输至少持续此时间。 |
| 15:8 | HwInit | Rx Min Truncation Transmit Delay²: 在 256B Flit 模式下操作时, 接收方在接收到 Truncated MAC 后准备好接收协议 Flit 所需的 IDE.Idle Flit 数量。发射方的 Tx Truncation Transmit Delay 字段 (参见第 8.2.4.22.8 节) 由软件配置, 以在链路以 256B Flit 模式操作时阻止协议 Flit 传输至少持续此时间。¹ |
| 31:16 | RsvdP | 保留 |

¹ 此字段作为 Version=2 的一部分引入。

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-7"></a>
### 8.2.4.22.7 Key Refresh Time Control (Offset 18h) | 密钥刷新时间控制 (偏移量 18h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 31:0 | RW | Tx Key Refresh Time: For 68B Flit mode, this register represents the minimum number of flits that the transmitter needs to block transmission of protocol flits after IDE.Start has been sent. For 256B Flit mode, this register represents the minimum number of flits that the transmitter needs to block transmission of protocol flits after IDE.Start has been sent or after IDE.Stop has been sent. Used when switching keys (see Section 11.3.7) or gracefully terminating IDE (256B Flit mode only, see Section 11.3.10). The default value of this field is 0. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 31:0 | RW | Tx Key Refresh Time: 对于 68B Flit 模式, 此寄存器表示发射方在发送 IDE.Start 之后需要阻止协议 Flit 传输的最少 Flit 数。对于 256B Flit 模式, 此寄存器表示发射方在发送 IDE.Start 之后或发送 IDE.Stop 之后需要阻止协议 Flit 传输的最少 Flit 数。在切换密钥 (参见第 11.3.7 节) 或正常终止 IDE (仅 256B Flit 模式, 参见第 11.3.10 节) 时使用。该字段的默认值为 0。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-8"></a>
### 8.2.4.22.8 Truncation Transmit Delay Control (Offset 1Ch) | 截断传输延迟控制 (偏移量 1Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 7:0 | RW | Tx Truncation Transmit Delay: Configuration parameter to account for the potential discarding of any precomputed values by the receiver. This parameter feeds into the computation of the minimum number of IDE.Idle flits that the Transmitter needs to send after sending a truncated MAC flit. See Equation 11-1. The default value of this field is 00h. |
| 31:8 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 7:0 | RW | Tx Truncation Transmit Delay: 用于说明接收方可能丢弃任何预计算值的配置参数。此参数参与计算发射方在发送截断 MAC Flit 后需要发送的 IDE.Idle Flit 最少数量。参见等式 11-1。该字段的默认值为 00h。 |
| 31:8 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-22-9"></a>
### 8.2.4.22.9 Key Refresh Time Capability2 (Offset 20h) | 密钥刷新时间能力 2 (偏移量 20h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

¹ This register was introduced as part of Version=2.

| Bit Location | Attributes | Description¹ |
|--------------|------------|-------------|
| 31:0 | HwInit | Rx Min Key Refresh Time²: Number of IDE.Idle flits the receiver needs to be ready to receive protocol flits after either IDE.Start or IDE.Stop is received when operating in 256B Flit mode. Tx Key Refresh Time (see Section 8.2.4.22.7) field of the transmitter is configured by System Software to block transmission of protocol flits for at least this duration when switching keys (see Section 11.3.7) or terminating IDE (see Section 11.3.10) when the link is operating in 256B Flit mode. |

</td><td style="background-color:#e8e8e8">

¹ 此寄存器作为 Version=2 的一部分引入。

| 位域 | 属性 | 描述¹ |
|------|------|------|
| 31:0 | HwInit | Rx Min Key Refresh Time²: 在 256B Flit 模式下操作时, 接收方在接收到 IDE.Start 或 IDE.Stop 之后准备好接收协议 Flit 所需的 IDE.Idle Flit 数量。发射方的 Tx Key Refresh Time 字段 (参见第 8.2.4.22.7 节) 由系统软件配置, 以在切换密钥 (参见第 11.3.7 节) 或终止 IDE (参见第 11.3.10 节) 时阻止协议 Flit 传输至少持续此时间, 此时链路以 256B Flit 模式操作。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-23"></a>
## 8.2.4.23 CXL Snoop Filter Capability Structure | CXL 窥探过滤器能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Offset | Register Name |
|--------|---------------|
| 00h | Snoop Filter Group ID |
| 04h | Snoop Filter Capacity |

</td><td style="background-color:#e8e8e8">

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | Snoop Filter Group ID |
| 04h | Snoop Filter Capacity |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-23-1"></a>
### 8.2.4.23.1 Snoop Filter Group ID (Offset 00h) | 窥探过滤器组 ID (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 15:0 | HwInit | Group ID: Uniquely identifies a snoop filter instance that is used to track CXL.cache devices below this Port. All Ports that share a single Snoop Filter instance shall set this field to the same value. |
| 31:16 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 15:0 | HwInit | Group ID: 唯一标识用于跟踪此端口下方 CXL.cache 设备的窥探过滤器实例。共享单个 Snoop Filter 实例的所有端口应将此字段设置为相同的值。 |
| 31:16 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-23-2"></a>
### 8.2.4.23.2 Snoop Filter Effective Size (Offset 04h) | 窥探过滤器有效大小 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 31:0 | HwInit | Capacity: Effective Snoop Filter Capacity representing the size of cache that can be effectively tracked by the Snoop Filter with this Group ID, in multiples of 64K. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 31:0 | HwInit | Capacity: 有效窥探过滤器容量, 表示可由具有此 Group ID 的 Snoop Filter 有效跟踪的高速缓存大小, 以 64K 的倍数表示。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-24"></a>
## 8.2.4.24 CXL Timeout and Isolation Capability Structure | CXL 超时与隔离能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Timeout and Isolation Capability Register |
| 04h | Reserved |
| 08h | CXL Timeout and Isolation Control Register |
| 0Ch | CXL Timeout and Isolation Status Register |

</td><td style="background-color:#e8e8e8">

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Timeout and Isolation Capability Register |
| 04h | 保留 |
| 08h | CXL Timeout and Isolation Control Register |
| 0Ch | CXL Timeout and Isolation Status Register |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-24-1"></a>
### 8.2.4.24.1 CXL Timeout and Isolation Capability Register (Offset 00h) | CXL 超时与隔离能力寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RO | CXL.mem Transaction Timeout Ranges Supported: This field indicates support for transaction timeout ranges on CXL.mem. Four time value ranges are defined:<br>• Range A: Default range: 50us to 10ms.<br>• Range B: 10ms to 250ms<br>• Range C: 250ms to 4s<br>• Range D: 4s to 64s<br>Bits are set according to the values listed below to show the supported timeout value ranges:<br>• 0h = Transaction Timeout programming is not supported – the function must implement a timeout value within the range of 50us to 10ms.<br>• 1h = Range A<br>• 2h = Range B<br>• 3h = Ranges A and B<br>• 6h = Ranges B and C<br>• 7h = Ranges A, B, and C<br>• Eh = Ranges B, C, and D<br>• Fh = Ranges A, B, C, and D<br>All other encodings are reserved |
| 4 | RO | CXL.mem Transaction Timeout Supported: The value of 1 indicates support for CXL.mem Transaction Timeout mechanism. |
| 7:5 | RsvdP | Reserved |
| 11:8 | RO | CXL.cache Transaction Timeout Ranges Supported: This field indicates support for transaction timeout ranges on CXL.cache. Four time value ranges are defined:<br>• Range A: Default range: 50us to 10ms.<br>• Range B: 10ms to 250ms<br>• Range C: 250ms to 4s<br>• Range D: 4s to 64s<br>Bits are set according to the values listed below to show the supported timeout value ranges:<br>• 0h = Transaction Timeout programming is not supported – the function must implement a timeout value within the range of 50us to 10ms.<br>• 1h = Range A<br>• 2h = Range B<br>• 3h = Ranges A and B<br>• 6h = Ranges B and C<br>• 7h = Ranges A, B, and C<br>• Eh = Ranges B, C, and D<br>• Fh = Ranges A, B, C, and D<br>All other encodings are reserved |
| 12 | RO | CXL.cache Transaction Timeout Supported: The value of 1 indicates support for CXL.cache Transaction Timeout mechanism. |
| 15:13 | RsvdP | Reserved |
| 16 | RO | CXL.mem Isolation Supported: This bit indicates support for Isolation on CXL.mem. |
| 17 | RO | CXL.mem Isolation Link Down Supported: This bit indicates support for triggering of Link Down on the CXL port if CXL.mem enters Isolation mode. This bit can only be set to 1 if the CXL.mem Isolation Supported bit is also set to 1. |
| 18 | RO | CXL.cache Isolation Supported: This bit indicates support for Isolation on CXL.cache. |
| 19 | RO | CXL.cache Isolation Link Down Supported: This bit indicates support for triggering of Link Down on the CXL Root Port if CXL.cache enters Isolation mode. This bit can only be set to 1 if the CXL.cache Isolation Supported bit is also set to 1. |
| 24:20 | RsvdP | Reserved |
| 25 | RO | Isolation ERR_COR Signaling Supported: If set, this bit indicates that the Root Port supports the ability to signal with ERR_COR when Isolation is triggered. |
| 26 | RO | Isolation Interrupt Supported: This bit indicates support for signaling an interrupt when Isolation is triggered. |
| 31:27 | RO | Isolation Interrupt Message Number: This field indicates which MSI/MSI-X vector is used for the interrupt message generated in association with the CXL Timeout and Isolation Capability structure. This field is valid only if Isolation Interrupt Supported is 1.<br>For MSI, the value in this field indicates the offset between the base Message Data and the interrupt message that is generated. Hardware is required to update this field so that it is correct if the number of MSI Messages assigned to the Function changes when software writes to the Multiple Message Enable field in the Message Control register for MSI.<br>For MSI-X, the value in this field indicates which MSI-X Table entry is used to generate the interrupt message. The entry must be one of the first 32 entries even if the Function implements more than 32 entries. For a given MSI-X implementation, the entry must remain constant.<br>If both MSI and MSI-X are implemented, they are permitted to use different vectors, though software is permitted to enable only one mechanism at a time. If MSI-X is enabled, the value in this field must indicate the vector for MSI-X. If MSI is enabled or neither is enabled, the value in this field must indicate the vector for MSI. If software enables both MSI and MSI-X at the same time, the value in this field is undefined. |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RO | CXL.mem Transaction Timeout Ranges Supported: 此字段指示 CXL.mem 上事务超时范围的支持。定义了四个时间值范围:<br>• Range A: 默认范围: 50us 至 10ms。<br>• Range B: 10ms 至 250ms<br>• Range C: 250ms 至 4s<br>• Range D: 4s 至 64s<br>位根据下面列出的值设置, 以显示支持的超时值范围:<br>• 0h = 不支持事务超时编程 - 功能必须在 50us 至 10ms 范围内实现超时值。<br>• 1h = Range A<br>• 2h = Range B<br>• 3h = Ranges A 和 B<br>• 6h = Ranges B 和 C<br>• 7h = Ranges A、B 和 C<br>• Eh = Ranges B、C 和 D<br>• Fh = Ranges A、B、C 和 D<br>所有其他编码保留 |
| 4 | RO | CXL.mem Transaction Timeout Supported: 值 1 表示支持 CXL.mem 事务超时机制。 |
| 7:5 | RsvdP | 保留 |
| 11:8 | RO | CXL.cache Transaction Timeout Ranges Supported: 此字段指示 CXL.cache 上事务超时范围的支持。定义了四个时间值范围:<br>• Range A: 默认范围: 50us 至 10ms。<br>• Range B: 10ms 至 250ms<br>• Range C: 250ms 至 4s<br>• Range D: 4s 至 64s<br>位根据下面列出的值设置, 以显示支持的超时值范围:<br>• 0h = 不支持事务超时编程 - 功能必须在 50us 至 10ms 范围内实现超时值。<br>• 1h = Range A<br>• 2h = Range B<br>• 3h = Ranges A 和 B<br>• 6h = Ranges B 和 C<br>• 7h = Ranges A、B 和 C<br>• Eh = Ranges B、C 和 D<br>• Fh = Ranges A、B、C 和 D<br>所有其他编码保留 |
| 12 | RO | CXL.cache Transaction Timeout Supported: 值 1 表示支持 CXL.cache 事务超时机制。 |
| 15:13 | RsvdP | 保留 |
| 16 | RO | CXL.mem Isolation Supported: 此位表示 CXL.mem 上对隔离的支持。 |
| 17 | RO | CXL.mem Isolation Link Down Supported: 此位表示在 CXL.mem 进入隔离模式时触发 CXL 端口上链路故障 (Link Down) 的支持。仅当 CXL.mem Isolation Supported 位也设置为 1 时, 此位才能设置为 1。 |
| 18 | RO | CXL.cache Isolation Supported: 此位表示 CXL.cache 上对隔离的支持。 |
| 19 | RO | CXL.cache Isolation Link Down Supported: 此位表示在 CXL.cache 进入隔离模式时触发 CXL 根端口上链路故障 (Link Down) 的支持。仅当 CXL.cache Isolation Supported 位也设置为 1 时, 此位才能设置为 1。 |
| 24:20 | RsvdP | 保留 |
| 25 | RO | Isolation ERR_COR Signaling Supported: 置位时, 此位表示根端口支持在触发隔离时通过 ERR_COR 发信号的能力。 |
| 26 | RO | Isolation Interrupt Supported: 此位表示在触发隔离时发信号通知中断的支持。 |
| 31:27 | RO | Isolation Interrupt Message Number: 此字段指示与 CXL Timeout and Isolation Capability 结构关联生成的中断消息所使用的 MSI/MSI-X 向量。仅当 Isolation Interrupt Supported 为 1 时, 此字段才有效。<br>对于 MSI, 此字段中的值表示基本消息数据与生成的中断消息之间的偏移量。当软件写入 MSI 消息控制寄存器的 Multiple Message Enable 字段而导致分配给该功能的消息数发生变化时, 硬件需要更新此字段以使其正确。<br>对于 MSI-X, 此字段中的值指示用于生成中断消息的 MSI-X 表条目。即使该功能实现了 32 个以上条目, 该条目也必须是前 32 个条目之一。对于给定的 MSI-X 实现, 该条目必须保持不变。<br>如果同时实现了 MSI 和 MSI-X, 则它们允许使用不同的向量, 但软件一次只允许启用一种机制。如果启用了 MSI-X, 则此字段中的值必须指示 MSI-X 的向量。如果启用了 MSI 或两者都未启用, 则此字段中的值必须指示 MSI 的向量。如果软件同时启用 MSI 和 MSI-X, 则此字段中的值未定义。 |

</td></tr>
</tbody>
</table>

> **Figure 8-57.** CXL Timeout and Isolation Capability Register layout ｜ CXL 超时与隔离能力寄存器布局
>
> <img src="figures/chapter_08/page_0583.png" alt="Figure 8-57" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0583.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-24-2"></a>
### 8.2.4.24.2 CXL Timeout and Isolation Control Register (Offset 08h) | CXL 超时与隔离控制寄存器 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 3:0 | RW/RO | CXL.mem Transaction Timeout Value: In CXL Root Port Functions that support Transaction Timeout programmability, this field allows system software to modify the Transaction Timeout Value for CXL.mem. Functions that support Transaction Timeout programmability must support the values given below corresponding to the programmability ranges indicated in the CXL.mem Transaction Timeout Ranges Supported field. Defined encodings:<br>• 0h = Default range: 50us to 10ms<br>• Values available if Range A (50us to 10ms) is supported: 1h = 50us to 100us; 2h = 1ms to 10ms<br>• Values available if Range B (10ms to 250ms) is supported: 5h = 16ms to 55ms; 6h = 65ms to 210ms<br>• Values available if Range C (250ms to 4s) is supported: 9h = 260ms to 900ms; Ah = 1s to 3.5s<br>• Values available if Range D (4s to 64s) is supported: Dh = 4s to 13s; Eh = 17s to 64s<br>All other encodings are reserved<br>Software is permitted to change the value in this field at any time. For Requests already pending when the Transaction Timeout Value is changed, hardware is permitted to use either the new or the old value for the outstanding Requests and is permitted to base the start time for each Request on either the time this value was changed or the time each request was issued.<br>This field must be RW if the CXL.mem Transaction Timeout Supported bit is set; otherwise, it is permitted to be hardwired to 0h.<br>The default value for this field is 0h. |
| 4 | RW/RO | CXL.mem Transaction Timeout Enable: When set, this bit enables CXL.mem Transaction Timeout detection mechanism.<br>Software is permitted to set or clear this bit at any time. If there are outstanding Transaction when the bit is set, it is permitted but not required for hardware to apply the completion timeout mechanism to the outstanding Transactions. If this is done, it is permitted to base the start time for each Transaction on either the time this bit was set or the time each Request was issued.<br>This bit must be RW if the CXL.mem Transaction Timeout Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the CXL.mem Transaction Timeout Supported bit is set.<br>The default value for this bit is 0. |
| 7:5 | RsvdP | Reserved |
| 11:8 | RW/RO | CXL.cache Transaction Timeout Value: In CXL Root Port Functions that support Transaction Timeout programmability, this field allows system software to modify the Transaction Timeout Value for CXL.cache.<br>Functions that support Transaction Timeout programmability must support the values given below corresponding to the programmability ranges indicated in the CXL.cache Transaction Timeout Ranges Supported field.<br>Defined encodings: 0h = Default range: 50us to 10ms; Values available if Range A is supported: 1h = 50us to 100us, 2h = 1ms to 10ms; Values available if Range B is supported: 5h = 16ms to 55ms, 6h = 65ms to 210ms; Values available if Range C is supported: 9h = 260ms to 900ms, Ah = 1s to 3.5s; Values available if Range D is supported: Dh = 4s to 13s, Eh = 17s to 64s; All other encodings are reserved<br>Software is permitted to change the value in this field at any time. For Requests already pending when the Transaction Timeout Value is changed, hardware is permitted to use either the new or the old value for the outstanding Requests and is permitted to base the start time for each Request on either the time this value was changed or the time each request was issued.<br>This bit must be RW if the CXL.cache Transaction Timeout Supported bit is set; otherwise, it is permitted to be hardwired to 0h.<br>The default value for this field is 0h. |
| 12 | RW/RO | CXL.cache Transaction Timeout Enable: When set, this bit enables CXL.cache Transaction Timeout detection mechanism.<br>Software is permitted to set or clear this bit at any time. If there are outstanding Transaction when the bit is set, it is permitted but not required for hardware to apply the completion timeout mechanism to the outstanding Transactions. If this is done, it is permitted to base the start time for each Transaction on either the time this bit was set or the time each Request was issued.<br>This bit must be RW if the CXL.cache Transaction Timeout Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the CXL.cache Transaction Timeout Supported bit is set.<br>The default value for this bit is 0. |
| 15:13 | RW/RO | Reserved |
| 16 | RW/RO | CXL.mem Isolation Enable: This field allows System Software to enable CXL.mem Isolation actions. If this field is set, Isolation actions will be triggered if either a CXL.mem Transaction Timeout is detected or if the CXL link went down.<br>This bit must be RW if the CXL.mem Isolation Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the CXL.mem Isolation Supported bit is set. The software is required to quiesce the CXL.mem traffic passing through the Root Port when changing the state of this bit. If Software modifies this bit in the presence of CXL.mem traffic, the results are undefined. |
| 17 | RW/RO | CXL.mem Isolation Link Down Enable: When set, the CXL root port shall trigger a Link Down condition when CXL.mem enters Isolation.<br>This bit must be RW if the CXL.mem Isolation Link Down Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the CXL.mem Isolation Link Down Supported bit is set. |
| 18 | RW/RO | CXL.cache Isolation Enable: This field allows System Software to enable CXL.cache Isolation actions. If this field is set, Isolation actions will be triggered if either a CXL.cache Transaction Timeout is detected or if the CXL link went down.<br>This bit must be RW if the CXL.cache Isolation Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the CXL.cache Isolation Supported bit is set.<br>The software is required to quiesce the CXL.cache traffic passing through the Root Port when changing the state of this bit. If Software modifies this bit in the presence of CXL.cache traffic, the results are undefined. |
| 19 | RW/RO | CXL.cache Isolation Link Down Enable: When set, the CXL root port shall trigger a Link Down condition when CXL.cache enters Isolation.<br>This bit must be RW if the CXL.cache Isolation Link Down Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the CXL.cache Isolation Link Down Supported bit is set. |
| 24:20 | RW/RO | Reserved |
| 25 | RW/RO | Isolation ERR_COR Signaling Enable: When set, this bit enables the sending of an ERR_COR Message to indicate Isolation has been triggered. Default value of this bit is 0.<br>This bit must be RW if the Isolation ERR_COR Signaling Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the Isolation ERR_COR Signaling Supported bit is set. |
| 26 | RW/RO | Isolation Interrupt Enable: When set, this bit enables the generation of an interrupt to indicate that Isolation has been triggered. Default value of this bit is 0.<br>This bit must be RW if the Isolation Interrupt Supported bit is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the Isolation Interrupt Supported bit is set. |
| 31:27 | RW/RO | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 3:0 | RW/RO | CXL.mem Transaction Timeout Value: 在支持事务超时编程的 CXL 根端口功能中, 此字段允许系统软件修改 CXL.mem 的事务超时值。支持事务超时编程的功能必须支持以下对应于 CXL.mem Transaction Timeout Ranges Supported 字段中指示的可编程范围的值。已定义编码:<br>• 0h = 默认范围: 50us 至 10ms<br>• 如果支持 Range A (50us 至 10ms) 可用值: 1h = 50us 至 100us; 2h = 1ms 至 10ms<br>• 如果支持 Range B (10ms 至 250ms) 可用值: 5h = 16ms 至 55ms; 6h = 65ms 至 210ms<br>• 如果支持 Range C (250ms 至 4s) 可用值: 9h = 260ms 至 900ms; Ah = 1s 至 3.5s<br>• 如果支持 Range D (4s 至 64s) 可用值: Dh = 4s 至 13s; Eh = 17s 至 64s<br>所有其他编码保留<br>软件允许随时更改此字段中的值。对于在事务超时值更改时已经挂起的请求, 硬件允许对未完成的请求使用新值或旧值, 并允许根据此值的更改时间或每个请求的发出时间确定每个请求的开始时间。<br>如果 CXL.mem Transaction Timeout Supported 位置位, 则此字段必须为 RW; 否则, 允许硬连线为 0h。<br>此字段的默认值为 0h。 |
| 4 | RW/RO | CXL.mem Transaction Timeout Enable: 置位时, 此位启用 CXL.mem 事务超时检测机制。<br>软件允许随时设置或清除此位。如果在该位置位时存在未完成的事务, 则允许但不要求硬件将完成超时机制应用于未完成的事务。如果这样做, 则允许根据该位的设置时间或每个请求的发出时间确定每个事务的开始时间。<br>如果 CXL.mem Transaction Timeout Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 CXL.mem Transaction Timeout Supported 位置位, 否则软件不得设置此位。<br>该位的默认值为 0。 |
| 7:5 | RsvdP | 保留 |
| 11:8 | RW/RO | CXL.cache Transaction Timeout Value: 在支持事务超时编程的 CXL 根端口功能中, 此字段允许系统软件修改 CXL.cache 的事务超时值。支持事务超时编程的功能必须支持以下对应于 CXL.cache Transaction Timeout Ranges Supported 字段中指示的可编程范围的值。已定义编码: 0h = 默认范围: 50us 至 10ms; 如果支持 Range A 可用值: 1h = 50us 至 100us, 2h = 1ms 至 10ms; 如果支持 Range B 可用值: 5h = 16ms 至 55ms, 6h = 65ms 至 210ms; 如果支持 Range C 可用值: 9h = 260ms 至 900ms, Ah = 1s 至 3.5s; 如果支持 Range D 可用值: Dh = 4s 至 13s, Eh = 17s 至 64s; 所有其他编码保留<br>软件允许随时更改此字段中的值。对于在事务超时值更改时已经挂起的请求, 硬件允许对未完成的请求使用新值或旧值, 并允许根据此值的更改时间或每个请求的发出时间确定每个请求的开始时间。<br>如果 CXL.cache Transaction Timeout Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0h。<br>此字段的默认值为 0h。 |
| 12 | RW/RO | CXL.cache Transaction Timeout Enable: 置位时, 此位启用 CXL.cache 事务超时检测机制。<br>软件允许随时设置或清除此位。如果在该位置位时存在未完成的事务, 则允许但不要求硬件将完成超时机制应用于未完成的事务。如果这样做, 则允许根据该位的设置时间或每个请求的发出时间确定每个事务的开始时间。<br>如果 CXL.cache Transaction Timeout Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 CXL.cache Transaction Timeout Supported 位置位, 否则软件不得设置此位。<br>该位的默认值为 0。 |
| 15:13 | RW/RO | 保留 |
| 16 | RW/RO | CXL.mem Isolation Enable: 此字段允许系统软件启用 CXL.mem Isolation 操作。如果设置了此字段, 则在检测到 CXL.mem 事务超时或 CXL 链路发生故障时将触发隔离操作。<br>如果 CXL.mem Isolation Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 CXL.mem Isolation Supported 位置位, 否则软件不得设置此位。在更改此位的状态时, 软件需要使通过根端口的 CXL.mem 流量静止。如果软件在存在 CXL.mem 流量的情况下修改此位, 则结果未定义。 |
| 17 | RW/RO | CXL.mem Isolation Link Down Enable: 置位时, 当 CXL.mem 进入隔离状态时, CXL 根端口应触发链路故障 (Link Down) 状况。<br>如果 CXL.mem Isolation Link Down Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 CXL.mem Isolation Link Down Supported 位置位, 否则软件不得设置此位。 |
| 18 | RW/RO | CXL.cache Isolation Enable: 此字段允许系统软件启用 CXL.cache Isolation 操作。如果设置了此字段, 则在检测到 CXL.cache 事务超时或 CXL 链路发生故障时将触发隔离操作。<br>如果 CXL.cache Isolation Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 CXL.cache Isolation Supported 位置位, 否则软件不得设置此位。<br>在更改此位的状态时, 软件需要使通过根端口的 CXL.cache 流量静止。如果软件在存在 CXL.cache 流量的情况下修改此位, 则结果未定义。 |
| 19 | RW/RO | CXL.cache Isolation Link Down Enable: 置位时, 当 CXL.cache 进入隔离状态时, CXL 根端口应触发链路故障 (Link Down) 状况。<br>如果 CXL.cache Isolation Link Down Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 CXL.cache Isolation Link Down Supported 位置位, 否则软件不得设置此位。 |
| 24:20 | RW/RO | 保留 |
| 25 | RW/RO | Isolation ERR_COR Signaling Enable: 置位时, 此位启用发送 ERR_COR 消息以指示已触发隔离。该位的默认值为 0。<br>如果 Isolation ERR_COR Signaling Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 Isolation ERR_COR Signaling Supported 位置位, 否则软件不得设置此位。 |
| 26 | RW/RO | Isolation Interrupt Enable: 置位时, 此位启用生成中断以指示已触发隔离。该位的默认值为 0。<br>如果 Isolation Interrupt Supported 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 Isolation Interrupt Supported 位置位, 否则软件不得设置此位。 |
| 31:27 | RW/RO | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-58.** CXL Timeout and Isolation Control Register layout ｜ CXL 超时与隔离控制寄存器布局
>
> <img src="figures/chapter_08/page_0585.png" alt="Figure 8-58" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0585.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-24-3"></a>
### 8.2.4.24.3 CXL Timeout and Isolation Status Register (Offset 0Ch) | CXL 超时与隔离状态寄存器 (偏移量 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW1CS/RsvdZ | CXL.mem Transaction Timeout: When set, this indicates that a CXL.mem transaction timed out. |
| 3:1 | RsvdZ | Reserved |
| 4 | RW1CS/RsvdZ | CXL.cache Transaction Timeout: When set, this indicates that a CXL.cache transaction timed out. |
| 7:5 | RsvdZ | Reserved |
| 8 | RW1CS/RsvdZ | CXL.mem Isolation Status: This field indicates that Isolation mode for CXL.mem was triggered. When this bit is set, CXL.mem is in isolation and the link is forced to be down if the CXL.mem Isolation Link Down Enable bit is set.<br>Software is permitted to clear this bit as part of recovery actions regardless of the state of other status bits, after which the CXL Root Port is no longer in Isolation mode for CXL.mem transactions. The link must transition through the Link Down state before software can attempt re-enumeration and device recovery. |
| 9 | RW1CS/RsvdZ | CXL.mem Isolation Link Down Status: This field indicates that Isolation mode for CXL.mem was triggered because of Link Down. |
| 11:10 | RsvdZ | Reserved |
| 12 | RW1CS/RsvdZ | CXL.cache Isolation Status: This bit indicates that Isolation mode for CXL.cache was triggered. When this bit is set, CXL.cache is in isolation and the link is forced to be down if CXL.cache Isolation Link Down Enable is set.<br>Software is permitted to clear this bit as part of recovery actions, after which the CXL Root Port is no longer in Isolation mode for CXL.cache transactions. The link must transition through the Link Down state before software can attempt re-enumeration and device recovery. |
| 13 | RW1CS/RsvdZ | CXL.cache Isolation Link Down Status: This bit indicates that Isolation mode for CXL.cache was triggered because of Link Down. |
| 14 | RO/RsvdZ | CXL RP Busy: When either the CXL.mem Isolation Status bit or the CXL.cache Isolation Status bit is set and this bit is set, the Root Port is busy with internal activity that must complete before software is permitted to clear the CXL.mem Isolation Status bit and the CXL.cache Isolation Status bit. If software violates this requirement, the behavior is undefined.<br>This bit is valid only when either the CXL.mem Isolation Status bit or the CXL.cache Isolation Status bit is set; otherwise, the value of this bit is undefined.<br>Default value of this bit is undefined. |
| 31:15 | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW1CS/RsvdZ | CXL.mem Transaction Timeout: 置位时, 表示 CXL.mem 事务已超时。 |
| 3:1 | RsvdZ | 保留 |
| 4 | RW1CS/RsvdZ | CXL.cache Transaction Timeout: 置位时, 表示 CXL.cache 事务已超时。 |
| 7:5 | RsvdZ | 保留 |
| 8 | RW1CS/RsvdZ | CXL.mem Isolation Status: 此字段表示已触发 CXL.mem 的隔离模式。当此位置位时, CXL.mem 处于隔离状态, 如果设置了 CXL.mem Isolation Link Down Enable 位, 则链路被强制为故障状态。<br>软件允许在恢复操作中清除此位, 而与其它状态位的状态无关, 之后 CXL 根端口不再处于 CXL.mem 事务的隔离模式。在软件尝试重新枚举和设备恢复之前, 链路必须转换通过 Link Down 状态。 |
| 9 | RW1CS/RsvdZ | CXL.mem Isolation Link Down Status: 此字段表示由于 Link Down 触发了 CXL.mem 的隔离模式。 |
| 11:10 | RsvdZ | 保留 |
| 12 | RW1CS/RsvdZ | CXL.cache Isolation Status: 此位表示已触发 CXL.cache 的隔离模式。当此位置位时, CXL.cache 处于隔离状态, 如果设置了 CXL.cache Isolation Link Down Enable 位, 则链路被强制为故障状态。<br>软件允许在恢复操作中清除此位, 之后 CXL 根端口不再处于 CXL.cache 事务的隔离模式。在软件尝试重新枚举和设备恢复之前, 链路必须转换通过 Link Down 状态。 |
| 13 | RW1CS/RsvdZ | CXL.cache Isolation Link Down Status: 此位表示由于 Link Down 触发了 CXL.cache 的隔离模式。 |
| 14 | RO/RsvdZ | CXL RP Busy: 当 CXL.mem Isolation Status 位或 CXL.cache Isolation Status 位之一置位且此位置位时, 根端口正忙于必须在软件允许清除 CXL.mem Isolation Status 位和 CXL.cache Isolation Status 位之前完成的内部活动。如果软件违反此要求, 则行为未定义。<br>仅当 CXL.mem Isolation Status 位或 CXL.cache Isolation Status 位之一置位时, 此位才有效; 否则, 此位的值未定义。<br>该位的默认值未定义。 |
| 31:15 | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-59.** CXL Timeout and Isolation Status Register layout ｜ CXL 超时与隔离状态寄存器布局
>
> <img src="figures/chapter_08/page_0587.png" alt="Figure 8-59" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0587.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-25"></a>
## 8.2.4.25 CXL.cachemem Extended Register Capability | CXL.cachemem 扩展寄存器能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This capability identifies all the extended 4-KB ranges in the Component Register Space that host CXL.cachemem registers.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL.cachemem Extended Ranges Register |

</td><td style="background-color:#e8e8e8">

此能力标识组件寄存器空间中承载 CXL.cachemem 寄存器的所有扩展 4-KB 范围。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL.cachemem Extended Ranges Register |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-25-1"></a>
### 8.2.4.25.1 CXL.cachemem Extended Ranges Register (Offset 00h) | CXL.cachemem 扩展范围寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register describes which 4-KB ranges in the Component Register Space that host CXL.cachemem Extended Range(s).

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 15:0 | HwInit | Extended Ranges Bitmap<br>• Bits [0, 1, 14]: Reserved<br>More than one of the following bits may be set to 1.<br>• Bit[2]: If set, the range 2000h-2FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[3]: If set, the range 3000h-3FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[4]: If set, the range 4000h-4FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[5]: If set, the range 5000h-5FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[6]: If set, the range 6000h-6FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[7]: If set, the range 7000h-7FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[8]: If set, the range 8000h-8FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[9]: If set, the range 9000h-9FFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[10]: If set, the range A000h-AFFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[11]: If set, the range B000h-BFFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[12]: If set, the range C000h-CFFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[13]: If set, the range D000h-DFFFh within the Component Register space is a CXL.cachemem extended range<br>• Bit[15]: If set, the range F000h-FFFFh within the Component Register space is a CXL.cachemem extended range |
| 31:16 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

此寄存器描述组件寄存器空间中承载 CXL.cachemem 扩展范围的哪些 4-KB 范围。

| 位域 | 属性 | 描述 |
|------|------|------|
| 15:0 | HwInit | Extended Ranges Bitmap (扩展范围位图)<br>• 位 [0, 1, 14]: 保留<br>以下位中可能有多个设置为 1。<br>• 位 [2]: 置位时, 组件寄存器空间中的 2000h-2FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [3]: 置位时, 组件寄存器空间中的 3000h-3FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [4]: 置位时, 组件寄存器空间中的 4000h-4FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [5]: 置位时, 组件寄存器空间中的 5000h-5FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [6]: 置位时, 组件寄存器空间中的 6000h-6FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [7]: 置位时, 组件寄存器空间中的 7000h-7FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [8]: 置位时, 组件寄存器空间中的 8000h-8FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [9]: 置位时, 组件寄存器空间中的 9000h-9FFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [10]: 置位时, 组件寄存器空间中的 A000h-AFFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [11]: 置位时, 组件寄存器空间中的 B000h-BFFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [12]: 置位时, 组件寄存器空间中的 C000h-CFFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [13]: 置位时, 组件寄存器空间中的 D000h-DFFFh 范围为 CXL.cachemem 扩展范围<br>• 位 [15]: 置位时, 组件寄存器空间中的 F000h-FFFFh 范围为 CXL.cachemem 扩展范围 |
| 31:16 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-60.** CXL.cachemem Extended Ranges Register layout ｜ CXL.cachemem 扩展范围寄存器布局
>
> <img src="figures/chapter_08/page_0589.png" alt="Figure 8-60" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0589.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-26"></a>
## 8.2.4.26 CXL BI Route Table Capability Structure | CXL BI 路由表能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

A switch uses this capability structure to manage updates to the routing of the BI messages in the upstream and downstream directions.

Revision 1 of this Capability Structure is optional for switches that do not require an explicit BI RT Commit operation. If this structure is present, it must be associated with the USP Function.

Revision 1 of this Capability Structure is not applicable to root ports, CXL devices, or DSPs.

See Section 9.14.2 for details.

| Offset | Register Name |
|--------|---------------|
| 00h | BI RT Capability |
| 04h | BI RT Control |
| 08h | BI RT Status |

</td><td style="background-color:#e8e8e8">

交换机使用此能力结构来管理上行和下行方向上 BI 消息路由的更新。

此能力结构的修订版 1 对于不需要显式 BI RT Commit 操作的交换机是可选的。如果存在此结构, 则必须与 USP 功能相关联。

此能力结构的修订版 1 不适用于根端口、CXL 设备或 DSP。

有关详细信息, 请参见第 9.14.2 节。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | BI RT Capability |
| 04h | BI RT Control |
| 08h | BI RT Status |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-26-1"></a>
### 8.2.4.26.1 BI RT Capability (Offset 00h) | BI RT 能力 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | HwInit | Explicit BI RT Commit Required: If 1, indicates that the software must set the BI RT Commit bit anytime a new BI device is enabled anywhere below this port or any component below this port undergoes bus number re-assignment. If 1, the BI RT Commit bit, the BI RT Committed bit, the BI RT Commit Timeout Scale field, the BI RT Commit Timeout Base field, and BI RT Error Not Committed bit are implemented.<br>BI RT Commit operation may be used by a component to update its internal structures or perform consistency checks. |
| 31:1 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | HwInit | Explicit BI RT Commit Required: 为 1 时, 表示软件必须在此端口下方的任何位置启用新的 BI 设备或此端口下方的任何组件发生总线号重新分配时随时设置 BI RT Commit 位。为 1 时, BI RT Commit 位、BI RT Committed 位、BI RT Commit Timeout Scale 字段、BI RT Commit Timeout Base 字段和 BI RT Error Not Committed 位均被实现。<br>组件可以使用 BI RT Commit 操作来更新其内部结构或执行一致性检查。 |
| 31:1 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-26-2"></a>
### 8.2.4.26.2 BI RT Control (Offset 04h) | BI RT 控制 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW/RsvdP | BI RT Commit: If Explicit BI RT Commit Required=1, software must cause this bit to transition from 0 to 1 to commit the BI-ID updates. The default value of this bit is 0. This bit must be RW if the Explicit BI RT Commit Required bit is set; otherwise, it is permitted to be hardwired to 0 and the BI Route Table update does not require an explicit commit. Software must not set this bit unless the Explicit BI RT Commit Required bit is set. |
| 31:1 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW/RsvdP | BI RT Commit: 如果 Explicit BI RT Commit Required=1, 则软件必须使该位从 0 转换为 1 以提交 BI-ID 更新。该位的默认值为 0。如果 Explicit BI RT Commit Required 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0, BI Route Table 更新不需要显式提交。除非 Explicit BI RT Commit Required 位置位, 否则软件不得设置此位。 |
| 31:1 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-26-3"></a>
### 8.2.4.26.3 BI RT Status (Offset 08h) | BI RT 状态 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RO/RsvdP | BI RT Committed: When set to 1, it indicates that the last write that caused BI RT Commit bit to transition from 0 to 1 was successfully processed by the component. This bit is cleared when the software causes the BI RT Commit bit to transition from 1 to 0. This bit is reserved if Explicit BI RT Commit Required=0. |
| 1 | RO/RsvdP | BI RT Error Not Committed: When set to 1, it indicates that the last write that caused the BI RT Commit bit to transition from 0 to 1 was processed by the component, but resulted in an error. This bit is cleared when the software causes the BI RT Commit bit to transition from 1 to 0. This bit is reserved if Explicit BI RT Commit Required=0. |
| 7:2 | RsvdP | Reserved |
| 11:8 | HwInit/RsvdP | BI RT Commit Timeout Scale: This field specifies the time scale associated with BI RT Commit Timeout.<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 second<br>• 0111b = 10 seconds<br>All other encodings are reserved<br>This field is reserved if Explicit BI RT Commit Required=0. |
| 15:12 | HwInit/RsvdP | BI RT Commit Timeout Base: This field determines the BI RT Commit timeout. The timeout duration is calculated by multiplying the Timeout Base with the Timeout Scale. Failure to set either the BI RT Committed bit or the BI RT Error Not Committed bit within the timeout duration is treated as equivalent to commit error. In case of a timeout, the software must clear the BI RT Commit bit to 0 prior to setting it to 1 again. This field is reserved if Explicit BI RT Commit Required=0. |
| 31:16 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RO/RsvdP | BI RT Committed: 设置为 1 时, 表示导致 BI RT Commit 位从 0 转换为 1 的最后一次写入已被组件成功处理。当软件导致 BI RT Commit 位从 1 转换为 0 时, 该位被清除。如果 Explicit BI RT Commit Required=0, 则此位保留。 |
| 1 | RO/RsvdP | BI RT Error Not Committed: 设置为 1 时, 表示导致 BI RT Commit 位从 0 转换为 1 的最后一次写入已被组件处理, 但导致错误。当软件导致 BI RT Commit 位从 1 转换为 0 时, 该位被清除。如果 Explicit BI RT Commit Required=0, 则此位保留。 |
| 7:2 | RsvdP | 保留 |
| 11:8 | HwInit/RsvdP | BI RT Commit Timeout Scale: 此字段指定与 BI RT Commit Timeout 关联的时间刻度。<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 秒<br>• 0111b = 10 秒<br>所有其他编码保留<br>如果 Explicit BI RT Commit Required=0, 则此字段保留。 |
| 15:12 | HwInit/RsvdP | BI RT Commit Timeout Base: 此字段确定 BI RT Commit 超时。超时持续时间通过将 Timeout Base 乘以 Timeout Scale 来计算。在超时持续时间内未能设置 BI RT Committed 位或 BI RT Error Not Committed 位被视为等同于提交错误。在超时的情况下, 软件必须在将 BI RT Commit 位再次设置为 1 之前将其清除为 0。如果 Explicit BI RT Commit Required=0, 则此字段保留。 |
| 31:16 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-61.** BI RT Status Register layout ｜ BI RT 状态寄存器布局
>
> <img src="figures/chapter_08/page_0591.png" alt="Figure 8-61" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0591.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-27"></a>
## 8.2.4.27 CXL BI Decoder Capability Structure | CXL BI 解码器能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This capability structure may be present in DSPs, root ports, or a device. The presence of this capability structure indicates that the component supports BI messages.

See Section 9.14.2 for details regarding the decoding of BI messages.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL BI Decoder Capability |
| 04h | CXL BI Decoder Control |
| 08h | CXL BI Decoder Status |

</td><td style="background-color:#e8e8e8">

此能力结构可能存在于 DSP、根端口或设备中。此能力结构的存在表示组件支持 BI 消息。

有关 BI 消息解码的详细信息, 请参见第 9.14.2 节。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL BI Decoder Capability |
| 04h | CXL BI Decoder Control |
| 08h | CXL BI Decoder Status |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-27-1"></a>
### 8.2.4.27.1 CXL BI Decoder Capability (Offset 00h) | CXL BI 解码器能力 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | HwInit/RsvdP | HDM-D Capable: If 1, it indicates that the Device supports HDM-D flows. If 0, it indicates that the Device does not support HDM-D flows. This bit is reserved for DSPs and Root Ports. |
| 1 | HwInit/RsvdP | Explicit BI Decoder Commit Required: If 1, indicates that the software must set BI Decoder Commit bit anytime a new BI device is enabled anywhere below this port or any component below this port undergoes bus number re-assignment. If 1, the BI Decoder Commit bit, the BI Decoder Committed bit, the BI Decoder Commit timeout Scale field, the BI Decoder Commit Timeout Base field, and BI Decoder Error Not Committed bit are implemented.<br>BI Decoder Commit operation may be used by a component to update its internal structures or perform consistency checks.<br>This bit is reserved for CXL devices and CXL root ports. |
| 31:2 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | HwInit/RsvdP | HDM-D Capable: 为 1 时, 表示设备支持 HDM-D 流。为 0 时, 表示设备不支持 HDM-D 流。对于 DSP 和根端口, 此位保留。 |
| 1 | HwInit/RsvdP | Explicit BI Decoder Commit Required: 为 1 时, 表示软件必须在此端口下方的任何位置启用新的 BI 设备或此端口下方的任何组件发生总线号重新分配时随时设置 BI Decoder Commit 位。为 1 时, BI Decoder Commit 位、BI Decoder Committed 位、BI Decoder Commit Timeout Scale 字段、BI Decoder Commit Timeout Base 字段和 BI Decoder Error Not Committed 位均被实现。<br>组件可以使用 BI Decoder Commit 操作来更新其内部结构或执行一致性检查。<br>对于 CXL 设备和 CXL 根端口, 此位保留。 |
| 31:2 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-62.** CXL BI Decoder Capability Register layout ｜ CXL BI 解码器能力寄存器布局
>
> <img src="figures/chapter_08/page_0592.png" alt="Figure 8-62" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0592.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-27-2"></a>
### 8.2.4.27.2 CXL BI Decoder Control (Offset 04h) | CXL BI 解码器控制 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

See Table 9-13 and Table 9-14 for handling of BISnp and BIRsp messages by the DSP and RP.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW/RsvdP | BI Forward<br>DSP or RP: Controls whether BI messages are forwarded. The reset default is 0. This bit is reserved for CXL devices. |
| 1 | RW | BI Enable<br>• DSP or Root Port: If set to 1, indicates a BI-capable device is connected directly to this Downstream Port.<br>• Device: If set to 1, the device is allowed to generate BISnp requests to addresses covered by any of its local HDM decoders with BI=1 (see Section 8.2.4.20.7).<br>The reset default is 0. |
| 2 | RW/RsvdP | BI Decoder Commit: If Explicit BI Decoder Commit Required=1, software must cause this bit to transition from 0 to 1 to commit the BI-ID assignment change to this BI Decoder instance. The default value of this field is 0. This bit must be RW if the Explicit BI Decoder Commit Required bit is set; otherwise, it is permitted to be hardwired to 0 and the BI Decoder update does not require an explicit commit. Software must not set this bit unless the Explicit BI Decoder Commit Required bit is set. |
| 31:3 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

有关 DSP 和 RP 处理 BISnp 和 BIRsp 消息的信息, 请参见表 9-13 和表 9-14。

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW/RsvdP | BI Forward (BI 转发)<br>DSP 或 RP: 控制是否转发 BI 消息。复位默认值为 0。对于 CXL 设备, 此位保留。 |
| 1 | RW | BI Enable (BI 启用)<br>• DSP 或根端口: 设置为 1 时, 表示具有 BI 能力的设备直接连接到此下行端口。<br>• 设备: 设置为 1 时, 允许设备向其本地 HDM 解码器 (BI=1, 参见第 8.2.4.20.7 节) 覆盖的地址生成 BISnp 请求。<br>复位默认值为 0。 |
| 2 | RW/RsvdP | BI Decoder Commit: 如果 Explicit BI Decoder Commit Required=1, 则软件必须使该位从 0 转换为 1 以向此 BI 解码器实例提交 BI-ID 分配更改。该字段的默认值为 0。如果 Explicit BI Decoder Commit Required 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0, BI Decoder 更新不需要显式提交。除非 Explicit BI Decoder Commit Required 位置位, 否则软件不得设置此位。 |
| 31:3 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-63.** CXL BI Decoder Control Register layout ｜ CXL BI 解码器控制寄存器布局
>
> <img src="figures/chapter_08/page_0592.png" alt="Figure 8-63" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0592.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-27-3"></a>
### 8.2.4.27.3 CXL BI Decoder Status (Offset 08h) | CXL BI 解码器状态 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RO | BI Decoder Committed: When set to 1, it indicates that the last write that caused the BI Decoder Commit bit to transition from 0 to 1 was successfully processed by the component. This bit is cleared when the software causes the BI Decoder Commit bit to transition from 1 to 0. |
| 1 | RO | BI Decoder Error Not Committed: When set to 1, it indicates that the last write that caused the BI Decoder Commit bit to transition from 0 to 1 was processed by the component, but resulted in an error. This bit is cleared when the software causes the BI Decoder Commit bit to transition from 1 to 0. |
| 7:2 | RsvdP | Reserved |
| 11:8 | HwInit | BI Decoder Commit Timeout Scale: This field specifies the time scale associated with BI Decoder Commit Timeout.<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 second<br>• 0111b = 10 seconds<br>All other encodings are reserved |
| 15:12 | HwInit | BI Decoder Commit Timeout Base: This field determines the BI Decoder Commit timeout. The timeout duration is calculated by multiplying the Timeout Base with the Timeout Scale. Failure to set either BI Decoder Committed bit or BI Decoder Error Not Committed bit within the timeout duration is treated as equivalent to commit error. In case of a timeout, the software must clear the BI Decoder Commit bit to 0 prior to setting it to 1 again. |
| 31:16 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RO | BI Decoder Committed: 设置为 1 时, 表示导致 BI Decoder Commit 位从 0 转换为 1 的最后一次写入已被组件成功处理。当软件导致 BI Decoder Commit 位从 1 转换为 0 时, 该位被清除。 |
| 1 | RO | BI Decoder Error Not Committed: 设置为 1 时, 表示导致 BI Decoder Commit 位从 0 转换为 1 的最后一次写入已被组件处理, 但导致错误。当软件导致 BI Decoder Commit 位从 1 转换为 0 时, 该位被清除。 |
| 7:2 | RsvdP | 保留 |
| 11:8 | HwInit | BI Decoder Commit Timeout Scale: 此字段指定与 BI Decoder Commit Timeout 关联的时间刻度。<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 秒<br>• 0111b = 10 秒<br>所有其他编码保留 |
| 15:12 | HwInit | BI Decoder Commit Timeout Base: 此字段确定 BI Decoder Commit 超时。超时持续时间通过将 Timeout Base 乘以 Timeout Scale 来计算。在超时持续时间内未能设置 BI Decoder Committed 位或 BI Decoder Error Not Committed 位被视为等同于提交错误。在超时的情况下, 软件必须在将 BI Decoder Commit 位再次设置为 1 之前将其清除为 0。 |
| 31:16 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-64.** CXL BI Decoder Status Register layout ｜ CXL BI 解码器状态寄存器布局
>
> <img src="figures/chapter_08/page_0593.png" alt="Figure 8-64" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0593.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-28"></a>
## 8.2.4.28 CXL Cache ID Route Table Capability Structure | CXL 缓存 ID 路由表能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The presence of this capability structure in the USP of a Switch indicates that the Switch supports CXL.cache protocol enhancements that enable multi-device scaling. Presence of this capability structure in the Host Bridge indicates that the Host supports CXL.cache protocol enhancements that enable multi-device scaling. This capability structure is mandatory if the Switch or the Host supports CXL.cache protocol enhancements that enable multi-device scaling.

The number of Cache ID Target entries is reported via the Cache ID Target Count field. For a CXL Switch, this field must be set to the maximum value permitted by the flit formats (10h for 256B flit format). The length of this capability structure is 10h + (2 * Cache ID Target Count) bytes.

See Section 9.15.2 and Section 9.15.4 for details.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Cache ID Route Table Capability |
| 04h | CXL Cache ID RT Control |
| 08h | CXL Cache ID RT Status |
| 0Ch | Reserved |
| 10h | CXL Cache ID Target 0 |
| 12h | CXL Cache ID Target 1 |
| … | … |

</td><td style="background-color:#e8e8e8">

此能力结构存在于交换机的 USP 中表示交换机支持实现多设备扩展的 CXL.cache 协议增强。此能力结构存在于主机桥中表示主机支持实现多设备扩展的 CXL.cache 协议增强。如果交换机或主机支持实现多设备扩展的 CXL.cache 协议增强, 则此能力结构是必需的。

Cache ID Target 条目数通过 Cache ID Target Count 字段报告。对于 CXL 交换机, 此字段必须设置为 Flit 格式所允许的最大值 (256B Flit 格式为 10h)。此能力结构的长度为 10h + (2 * Cache ID Target Count) 字节。

有关详细信息, 请参见第 9.15.2 节和第 9.15.4 节。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Cache ID Route Table Capability |
| 04h | CXL Cache ID RT Control |
| 08h | CXL Cache ID RT Status |
| 0Ch | 保留 |
| 10h | CXL Cache ID Target 0 |
| 12h | CXL Cache ID Target 1 |
| … | … |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-28-1"></a>
### 8.2.4.28.1 CXL Cache ID Route Table Capability (Offset 00h) | CXL 缓存 ID 路由表能力 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 4:0 | HwInit/RsvdP | Cache ID Target Count: The number of Cache ID Target entries in this capability structure. For a CXL switch, this field must be set to the maximum value amongst all the flit formats the switch supports. For example, a switch that supports the 68B flit format and the 256B flit format must set this to 10h even when the USP link is operating in 68B Flit mode. A Host Bridge may report a number that is smaller than the maximum value amongst all the flit formats the host supports. |
| 7:5 | RsvdP | Reserved |
| 11:8 | HwInit/RsvdP | HDM-D Type 2 Device Max Count: The number of Type 2 devices using HDM-D flows that this Host Bridge is capable of supporting. This field is reserved for switches. |
| 15:12 | RsvdP | Reserved |
| 16 | HwInit | Explicit Cache ID RT Commit Required: If 1, indicates that the software must set Cache ID RT Commit bit after any changes to this Cache ID Route Table for those changes to take effect. If 1, the Cache ID RT Commit bit, the Cache ID RT Committed bit, the Cache ID RT Commit timeout Scale field, the Cache ID RT Commit Timeout Base field, and Cache ID RT Error Not Committed bit are implemented.<br>Cache ID RT Commit operation may be used by a component to update its internal structures or perform consistency checks. |
| 31:17 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 4:0 | HwInit/RsvdP | Cache ID Target Count: 此能力结构中 Cache ID Target 条目的数量。对于 CXL 交换机, 此字段必须设置为交换机支持的所有 Flit 格式中的最大值。例如, 支持 68B Flit 格式和 256B Flit 格式的交换机必须将此字段设置为 10h, 即使 USP 链路以 68B Flit 模式操作。主机桥可以报告一个小于主机支持的所有 Flit 格式中最大值的数字。 |
| 7:5 | RsvdP | 保留 |
| 11:8 | HwInit/RsvdP | HDM-D Type 2 Device Max Count: 此主机桥能够支持的、使用 HDM-D 流的 Type 2 设备数量。对于交换机, 此字段保留。 |
| 15:12 | RsvdP | 保留 |
| 16 | HwInit | Explicit Cache ID RT Commit Required: 为 1 时, 表示软件必须在此 Cache ID Route Table 发生任何更改后设置 Cache ID RT Commit 位, 以使这些更改生效。为 1 时, Cache ID RT Commit 位、Cache ID RT Committed 位、Cache ID RT Commit Timeout Scale 字段、Cache ID RT Commit Timeout Base 字段和 Cache ID RT Error Not Committed 位均被实现。<br>组件可以使用 Cache ID RT Commit 操作来更新其内部结构或执行一致性检查。 |
| 31:17 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-28-2"></a>
### 8.2.4.28.2 CXL Cache ID RT Control (Offset 04h) | CXL 缓存 ID RT 控制 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW/RsvdP | Cache ID RT Commit: If Explicit Cache ID RT Commit Required=1, software must cause this bit to transition from 0 to 1 to commit the contents of this Cache ID Route Table instance. The default value of this field is 0. This bit must be RW if the Cache ID RT Commit Required bit is set; otherwise, it is permitted to be hardwired to 0 and the Cache ID Route Table update does not require an explicit commit. Software must not set this bit unless the Explicit Cache ID RT Commit Required bit is set. |
| 31:1 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW/RsvdP | Cache ID RT Commit: 如果 Explicit Cache ID RT Commit Required=1, 则软件必须使该位从 0 转换为 1 以提交此 Cache ID Route Table 实例的内容。该字段的默认值为 0。如果 Cache ID RT Commit Required 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0, Cache ID Route Table 更新不需要显式提交。除非 Explicit Cache ID RT Commit Required 位置位, 否则软件不得设置此位。 |
| 31:1 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-28-3"></a>
### 8.2.4.28.3 CXL Cache ID RT Status (Offset 08h) | CXL 缓存 ID RT 状态 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RO/RsvdP | Cache ID RT Committed: When set to 1, it indicates that the last write that caused the Cache ID RT Commit bit to transition from 0 to 1 was successfully processed by the component. This bit is cleared when the software causes the Cache ID RT Commit bit to transition from 1 to 0. This bit is reserved if Explicit Cache ID RT Commit Required=0. |
| 1 | RO/RsvdP | Cache ID RT Error Not Committed: When set to 1, it indicates that the last write that caused the Cache ID RT Commit bit to transition from 0 to 1 was processed by the component, but resulted in an error. This bit is cleared when the software causes the Cache ID RT Commit bit to transition from 1 to 0. This bit is reserved if Explicit Cache ID RT Commit Required=0. |
| 7:2 | RsvdP | Reserved |
| 11:8 | (see below) | Cache ID RT Commit Timeout Scale: This field specifies the time scale associated with Cache ID RT Commit Timeout.<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 second<br>• 0111b = 10 seconds<br>All other encodings are reserved |
| 15:12 | (see below) | Cache ID RT Commit Timeout Base: This field determines the Cache ID RT Commit timeout. The timeout duration is calculated by multiplying the Timeout Base with the Timeout Scale. Failure to set either the Cache ID RT Committed bit or the Cache ID RT Error Not Committed bit within the timeout duration is treated as equivalent to commit error. In case of a timeout, the software must clear the Cache ID RT Commit bit to 0 prior to setting it to 1 again. |
| 31:16 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RO/RsvdP | Cache ID RT Committed: 设置为 1 时, 表示导致 Cache ID RT Commit 位从 0 转换为 1 的最后一次写入已被组件成功处理。当软件导致 Cache ID RT Commit 位从 1 转换为 0 时, 该位被清除。如果 Explicit Cache ID RT Commit Required=0, 则此位保留。 |
| 1 | RO/RsvdP | Cache ID RT Error Not Committed: 设置为 1 时, 表示导致 Cache ID RT Commit 位从 0 转换为 1 的最后一次写入已被组件处理, 但导致错误。当软件导致 Cache ID RT Commit 位从 1 转换为 0 时, 该位被清除。如果 Explicit Cache ID RT Commit Required=0, 则此位保留。 |
| 7:2 | RsvdP | 保留 |
| 11:8 | (见下文) | Cache ID RT Commit Timeout Scale: 此字段指定与 Cache ID RT Commit Timeout 关联的时间刻度。<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 秒<br>• 0111b = 10 秒<br>所有其他编码保留 |
| 15:12 | (见下文) | Cache ID RT Commit Timeout Base: 此字段确定 Cache ID RT Commit 超时。超时持续时间通过将 Timeout Base 乘以 Timeout Scale 来计算。在超时持续时间内未能设置 Cache ID RT Committed 位或 Cache ID RT Error Not Committed 位被视为等同于提交错误。在超时的情况下, 软件必须在将 Cache ID RT Commit 位再次设置为 1 之前将其清除为 0。 |
| 31:16 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-28-4"></a>
### 8.2.4.28.4 CXL Cache ID Target N (Offset 10h+ 2*N) | CXL 缓存 ID 目标 N (偏移量 10h+ 2*N)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This section defines the CXL Cache ID Target N register at offset 10h + 2*N. The full register definition for target-specific fields (e.g., target identifier, port mapping) is provided in the Cache ID Route Table specification. See Section 9.15.2 and Section 9.15.4 for details.

</td><td style="background-color:#e8e8e8">

本节定义偏移量 10h + 2*N 处的 CXL Cache ID Target N 寄存器。目标特定字段 (例如目标标识符、端口映射) 的完整寄存器定义在 Cache ID Route Table 规范中提供。有关详细信息, 请参见第 9.15.2 节和第 9.15.4 节。

</td></tr>
</tbody>
</table>

> **Figure 8-65.** CXL Cache ID Route Table layout ｜ CXL 缓存 ID 路由表布局
>
> <img src="figures/chapter_08/page_0595.png" alt="Figure 8-65" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0595.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-29"></a>
## 8.2.4.29 CXL Cache ID Decoder Capability Structure | CXL 缓存 ID 解码器能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This capability structure may be present in DSPs and root ports. The presence of this capability structure indicates that the component supports CXL.cache protocol enhancements that enable multi-device scaling. This capability structure is mandatory if the switch or the host supports CXL.cache protocol enhancements that enable multi-device scaling. See Section 9.15.2 for details.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Cache ID Decoder Capability |
| 04h | CXL Cache ID Decoder Control |
| 08h | CXL Cache ID Decoder Status |

</td><td style="background-color:#e8e8e8">

此能力结构可能存在于 DSP 和根端口中。此能力结构的存在表示组件支持实现多设备扩展的 CXL.cache 协议增强。如果交换机或主机支持实现多设备扩展的 CXL.cache 协议增强, 则此能力结构是必需的。有关详细信息, 请参见第 9.15.2 节。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Cache ID Decoder Capability |
| 04h | CXL Cache ID Decoder Control |
| 08h | CXL Cache ID Decoder Status |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-29-1"></a>
### 8.2.4.29.1 CXL Cache ID Decoder Capability (Offset 00h) | CXL 缓存 ID 解码器能力 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | HwInit | Explicit Cache ID Decoder Commit Required: If 1, indicates that the software must set the Cache ID Decoder Commit bit anytime a new CXL.cache device is enabled anywhere below this port. Also, the Cache ID Decoder Commit bit, the Cache ID Decoder Committed bit, the Cache ID Decoder Commit Timeout Scale field, the Cache ID Decoder Commit Timeout Base field, and Cache ID Decoder Error Not Committed bit are implemented.<br>Cache ID Decoder Commit operation may be used by a component to update its internal structures or perform consistency checks. |
| 31:1 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | HwInit | Explicit Cache ID Decoder Commit Required: 为 1 时, 表示软件必须在此端口下方的任何位置启用新的 CXL.cache 设备时随时设置 Cache ID Decoder Commit 位。此外, 还实现了 Cache ID Decoder Commit 位、Cache ID Decoder Committed 位、Cache ID Decoder Commit Timeout Scale 字段、Cache ID Decoder Commit Timeout Base 字段和 Cache ID Decoder Error Not Committed 位。<br>组件可以使用 Cache ID Decoder Commit 操作来更新其内部结构或执行一致性检查。 |
| 31:1 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-29-2"></a>
### 8.2.4.29.2 CXL Cache ID Decoder Control (Offset 04h) | CXL 缓存 ID 解码器控制 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RW | Forward Cache ID: 1 indicates that the Port forwards CXL.cache messages in both directions. The reset default is 0. |
| 1 | RW | Assign Cache ID: 1 indicates that this Downstream Port is connected directly to a CXL.cache Device or the link is operating in 68B flit mode. In these cases, the Downstream Port assigns a Cache ID=Local Cache ID to it. The reset default is 0. |
| 2 | RW | HDM-D Type 2 Device Present: 1 indicates that there is a Type 2 Device below this Downstream Port that is using HDM-D flows. The reset default is 0. |
| 3 | RW/RsvdP | Cache ID Decoder Commit: If Explicit Cache ID Decoder Commit Required=1, software must cause this bit to transition from 0 to 1 to commit the Cache ID assignment change to this Cache ID Decoder instance. The default value of this field is 0. This bit must be RW if the Explicit Cache ID Decoder Commit Required bit is set; otherwise, it is permitted to be hardwired to 0 and the Cache ID Decoder update does not require an explicit commit. Software must not set this bit unless the Explicit Cache ID Decoder Commit Required bit is set. |
| 7:4 | RsvdP | Reserved |
| 11:8 | RW | HDM-D Type 2 Device Cache ID: If HDM-D Type 2 Device Present=1, this field represents the Cache ID that has been assigned to the Type 2 device below this Downstream Port that is using HDM-D flows. This field may be used by the port to identify a Type 2 device that is using HDM-D flows and must not be used for assigning a Cache ID. The reset default is 0h. |
| 15:12 | RsvdP | Reserved |
| 19:16 | RW | Local Cache ID: If Assign Cache ID Enable=1, the Port assigns this Cache ID to the directly connected CXL.cache device regardless of whether it is using HDM-D flows or HDM-DB flows. The reset default is 0h. |
| 31:20 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RW | Forward Cache ID: 1 表示端口在两个方向上转发 CXL.cache 消息。复位默认值为 0。 |
| 1 | RW | Assign Cache ID: 1 表示此下行端口直接连接到 CXL.cache 设备, 或链路以 68B Flit 模式操作。在这些情况下, 下行端口为其分配 Cache ID=Local Cache ID。复位默认值为 0。 |
| 2 | RW | HDM-D Type 2 Device Present: 1 表示此下行端口下方存在使用 HDM-D 流的 Type 2 设备。复位默认值为 0。 |
| 3 | RW/RsvdP | Cache ID Decoder Commit: 如果 Explicit Cache ID Decoder Commit Required=1, 则软件必须使该位从 0 转换为 1 以向此 Cache ID Decoder 实例提交 Cache ID 分配更改。该字段的默认值为 0。如果 Explicit Cache ID Decoder Commit Required 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0, Cache ID Decoder 更新不需要显式提交。除非 Explicit Cache ID Decoder Commit Required 位置位, 否则软件不得设置此位。 |
| 7:4 | RsvdP | 保留 |
| 11:8 | RW | HDM-D Type 2 Device Cache ID: 如果 HDM-D Type 2 Device Present=1, 则此字段表示已分配给此下行下方使用 HDM-D 流的 Type 2 设备的 Cache ID。此字段可被端口用于标识使用 HDM-D 流的 Type 2 设备, 不得用于分配 Cache ID。复位默认值为 0h。 |
| 15:12 | RsvdP | 保留 |
| 19:16 | RW | Local Cache ID: 如果 Assign Cache ID Enable=1, 则端口将此 Cache ID 分配给直接连接的 CXL.cache 设备, 无论其是使用 HDM-D 流还是 HDM-DB 流。复位默认值为 0h。 |
| 31:20 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-66.** CXL Cache ID Decoder Control Register layout ｜ CXL 缓存 ID 解码器控制寄存器布局
>
> <img src="figures/chapter_08/page_0596.png" alt="Figure 8-66" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0596.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-29-3"></a>
### 8.2.4.29.3 CXL Cache ID Decoder Status (Offset 08h) | CXL 缓存 ID 解码器状态 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 0 | RO/RsvdP | Cache ID Decoder Committed: When set to 1, it indicates that the last write that caused the Cache ID Decoder Commit bit to transition from 0 to 1 was successfully processed by the component. This bit is cleared when the software causes the Cache ID Decoder Commit bit to transition from 1 to 0. This bit is reserved if Explicit Cache ID Decoder Commit Required=0. |
| 1 | RO/RsvdP | Cache ID Decoder Error Not Committed: When set to 1, it indicates that the last write that caused the Cache ID Decoder Commit bit to transition from 0 to 1 was processed by the component, but resulted in an error. This bit is cleared when the software causes the Cache ID Decoder Commit bit to transition from 1 to 0. This bit is reserved if Explicit Cache ID Decoder Commit Required=0. |
| 7:2 | RsvdP | Reserved |
| 11:8 | HwInit/RsvdP | Cache ID Decoder Commit Timeout Scale: This field specifies the time scale associated with Cache ID Decoder Commit Timeout.<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 second<br>• 0111b = 10 seconds<br>All other encodings are reserved<br>This field is reserved if Explicit Cache ID Decoder Commit Required=0. |
| 15:12 | HwInit/RsvdP | Cache ID Decoder Commit Timeout Base: This field determines the Cache ID Decoder Commit timeout. The timeout duration is calculated by multiplying the Timeout Base with the Timeout Scale. Failure to set either the Cache ID Decoder Committed bit or the Cache ID Decoder Error Not Committed bit within the timeout value is treated as equivalent to commit error. In case of a timeout, the software must clear the Cache ID Decoder Commit bit to 0 prior to setting it to 1 again. This field is reserved if Explicit Cache ID Decoder Commit Required=0. |
| 31:16 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 0 | RO/RsvdP | Cache ID Decoder Committed: 设置为 1 时, 表示导致 Cache ID Decoder Commit 位从 0 转换为 1 的最后一次写入已被组件成功处理。当软件导致 Cache ID Decoder Commit 位从 1 转换为 0 时, 该位被清除。如果 Explicit Cache ID Decoder Commit Required=0, 则此位保留。 |
| 1 | RO/RsvdP | Cache ID Decoder Error Not Committed: 设置为 1 时, 表示导致 Cache ID Decoder Commit 位从 0 转换为 1 的最后一次写入已被组件处理, 但导致错误。当软件导致 Cache ID Decoder Commit 位从 1 转换为 0 时, 该位被清除。如果 Explicit Cache ID Decoder Commit Required=0, 则此位保留。 |
| 7:2 | RsvdP | 保留 |
| 11:8 | HwInit/RsvdP | Cache ID Decoder Commit Timeout Scale: 此字段指定与 Cache ID Decoder Commit Timeout 关联的时间刻度。<br>• 0000b = 1 us<br>• 0001b = 10 us<br>• 0010b = 100 us<br>• 0011b = 1 ms<br>• 0100b = 10 ms<br>• 0101b = 100 ms<br>• 0110b = 1 秒<br>• 0111b = 10 秒<br>所有其他编码保留<br>如果 Explicit Cache ID Decoder Commit Required=0, 则此字段保留。 |
| 15:12 | HwInit/RsvdP | Cache ID Decoder Commit Timeout Base: 此字段确定 Cache ID Decoder Commit 超时。超时持续时间通过将 Timeout Base 乘以 Timeout Scale 来计算。在超时值内未能设置 Cache ID Decoder Committed 位或 Cache ID Decoder Error Not Committed 位被视为等同于提交错误。在超时的情况下, 软件必须在将 Cache ID Decoder Commit 位再次设置为 1 之前将其清除为 0。如果 Explicit Cache ID Decoder Commit Required=0, 则此字段保留。 |
| 31:16 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-67.** CXL Cache ID Decoder Status Register layout ｜ CXL 缓存 ID 解码器状态寄存器布局
>
> <img src="figures/chapter_08/page_0597.png" alt="Figure 8-67" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0597.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-30"></a>
## 8.2.4.30 CXL Extended HDM Decoder Capability Structure | CXL 扩展 HDM 解码器能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

CXL Extended HDM Decoder Capability structure allows CXL Upstream Switch Ports to implement more HDM decoders than the limit defined in the CXL HDM Decoder Capability structure. A CXL Upstream Switch Port that is capable of routing CXL.mem traffic to more than one Downstream Switch Ports may contain one instance of this capability structure.

The layout of this capability structure is identical to the CXL HDM Decoder Capability structure and will track it (see Section 8.2.4.20).

</td><td style="background-color:#e8e8e8">

CXL 扩展 HDM 解码器能力结构允许 CXL 上行交换机端口实现比 CXL HDM 解码器能力结构中定义的限制更多的 HDM 解码器。能够将 CXL.mem 流量路由到多个下行交换机端口的 CXL 上行交换机端口可以包含此能力结构的一个实例。

此能力结构的布局与 CXL HDM 解码器能力结构相同, 并将与其保持一致 (参见第 8.2.4.20 节)。

</td></tr>
</tbody>
</table>

> **Figure 8-68.** CXL Extended HDM Decoder Capability Structure layout ｜ CXL 扩展 HDM 解码器能力结构布局
>
> <img src="figures/chapter_08/page_0597.png" alt="Figure 8-68" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0597.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-31"></a>
## 8.2.4.31 CXL Extended Metadata Capability Register | CXL 扩展元数据能力寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This capability structure may be present in CXL.mem-capable devices that support 256B Flit mode. The presence of this capability structure indicates that the component is capable of storing and returning Extended Metadata.

This specification does not describe how a device with persistent memory capacity may implement Extended Metadata.

See Section 4.3.3.2, Table 3-43, and Table 3-54 for details regarding Extended Metadata transfer over CXL.

| Offset | Register Name |
|--------|---------------|
| 00h | CXL Extended Metadata Capability Register |
| 04h | CXL Extended Metadata Control Register |

</td><td style="background-color:#e8e8e8">

此能力结构可能存在于支持 256B Flit 模式的 CXL.mem 能力设备中。此能力结构的存在表示组件能够存储和返回扩展元数据。

本规范未描述具有持久内存容量的设备如何实现扩展元数据。

有关通过 CXL 传输扩展元数据的详细信息, 请参见第 4.3.3.2 节、表 3-43 和表 3-54。

| 偏移量 | 寄存器名称 |
|--------|------------|
| 00h | CXL Extended Metadata Capability Register |
| 04h | CXL Extended Metadata Control Register |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-31-1"></a>
### 8.2.4.31.1 CXL Extended Metadata Capability Register (Offset 00h) | CXL 扩展元数据能力寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 6:0 | RO | Max Size of Extended Metadata: Defines the maximum size of the Extended Metadata Field within the EMD trailer. Valid values are from 1 to 32.<br>• 1 = 1 bit of EMD<br>• …<br>• 32 = 32 bits of EMD |
| 7 | RO | Reserved |
| 8 | RO | Support for Extended Metadata Error Logging: Indicates whether the component is capable of logging Extended Metadata content in the Header Log. |
| 31:9 | RO | Reserved |

</td><td style="background-color:#e8e8e8">

| 位域 | 属性 | 描述 |
|------|------|------|
| 6:0 | RO | Max Size of Extended Metadata: 定义 EMD 尾部内扩展元数据字段的最大大小。有效值从 1 到 32。<br>• 1 = 1 位 EMD<br>• …<br>• 32 = 32 位 EMD |
| 7 | RO | 保留 |
| 8 | RO | Support for Extended Metadata Error Logging: 指示组件是否能够在头日志 (Header Log) 中记录扩展元数据内容。 |
| 31:9 | RO | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-4-31-2"></a>
### 8.2.4.31.2 CXL Extended Metadata Control Register (Offset 04h) | CXL 扩展元数据控制寄存器 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The device behavior is undefined if the contents of this register are modified under the following conditions:
- CXL.mem accesses to the device are in progress
- Device is operating in 68B Flit mode

Modification to this register content shall have no impact on the Memory capacity reported via Memory_Size fields in the DVSEC CXL Range Size registers, CDAT content, Identify Memory Device output, and Get Partition Info output.

| Bit Location | Attributes | Description |
|--------------|------------|-------------|
| 6:0 | RWL | Size of Extended Metadata: Defines the Extended Metadata Field size of a transfer. The device behavior is undefined if this register is set to a value that exceeds the Max Size of Extended Metadata reported via the CXL Extended Metadata Capability register.<br>• 1 = 1-bit EMD field. Corresponds to the LSB of the EMD Trailer.<br>• …<br>• 31 = 31-bit EMD field, Corresponds to the 31 least significant bits of the EMD Trailer.<br>• 32 = 32-bit EMD field<br>Locked by the CONFIG_LOCK bit (see Section 8.1.3.6). |
| 7 | RO | Reserved |
| 8 | RWL/RO | Enable Extended Metadata Error Logging: This bit must be RWL if the Support for Extended Metadata Error Logging bit in the CXL Extended Metadata Capability register is set; otherwise, this bit is permitted to be hardwired to 0. Software must not set this bit unless the Support for Extended Metadata Error Logging bit is set. If set, the device logs Extended Metadata content associated with the error, if possible, in the Header Log. See Section 8.2.4.17.1 for details. Locked by the CONFIG_LOCK bit (see Section 8.1.3.6). |
| 30:9 | RO | Reserved |
| 31 | RWL | Enable Extended Metadata Field Transfers: If set, the CXL device expects to receive and send Extended Metadata on data transfers via the trailer. Locked by the CONFIG_LOCK bit (see Section 8.1.3.6). |

</td><td style="background-color:#e8e8e8">

在以下条件下修改此寄存器的内容时, 设备行为未定义:
- 正在进行 CXL.mem 访问设备
- 设备以 68B Flit 模式操作

修改此寄存器内容不应影响通过 DVSEC CXL Range Size 寄存器中的 Memory_Size 字段、CDAT 内容、Identify Memory Device 输出和 Get Partition Info 输出所报告的内存容量。

| 位域 | 属性 | 描述 |
|------|------|------|
| 6:0 | RWL | Size of Extended Metadata: 定义传输的扩展元数据字段大小。如果此寄存器设置为超过通过 CXL Extended Metadata Capability 寄存器报告的 Max Size of Extended Metadata 的值, 则设备行为未定义。<br>• 1 = 1 位 EMD 字段。对应于 EMD 尾部的 LSB。<br>• …<br>• 31 = 31 位 EMD 字段, 对应于 EMD 尾部的 31 个最低有效位。<br>• 32 = 32 位 EMD 字段<br>由 CONFIG_LOCK 位锁定 (参见第 8.1.3.6 节)。 |
| 7 | RO | 保留 |
| 8 | RWL/RO | Enable Extended Metadata Error Logging: 如果 CXL Extended Metadata Capability 寄存器中的 Support for Extended Metadata Error Logging 位置位, 则此位必须为 RWL; 否则, 此位允许硬连线为 0。除非 Support for Extended Metadata Error Logging 位置位, 否则软件不得设置此位。置位时, 设备在可能的情况下将与错误关联的扩展元数据内容记录在头日志 (Header Log) 中。有关详细信息, 请参见第 8.2.4.17.1 节。由 CONFIG_LOCK 位锁定 (参见第 8.1.3.6 节)。 |
| 30:9 | RO | 保留 |
| 31 | RWL | Enable Extended Metadata Field Transfers: 置位时, CXL 设备预期通过尾部在数据传输上接收和发送扩展元数据。由 CONFIG_LOCK 位锁定 (参见第 8.1.3.6 节)。 |

</td></tr>
</tbody>
</table>

> **Figure 8-69.** CXL Extended Metadata Register layout ｜ CXL 扩展元数据寄存器布局
>
> <img src="figures/chapter_08/page_0598.png" alt="Figure 8-69" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0598.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-5"></a>
## 8.2.5 CXL ARB/MUX Registers | CXL ARB/MUX 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The following registers are located within the 1-KB region of memory space assigned to CXL ARB/MUX. The register offsets below are listed from CXL ARB/MUX register space, starting at Offset E000h in the Component Register Range (see Section 8.2.3).

</td><td style="background-color:#e8e8e8">

以下寄存器位于分配给 CXL ARB/MUX 的内存空间的 1-KB 区域内。下面列出的寄存器偏移量来自 CXL ARB/MUX 寄存器空间, 起始于组件寄存器范围内的偏移量 E000h (参见第 8.2.3 节)。

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-5-1"></a>
### 8.2.5.1 ARB/MUX PM Timeout Control Register (Offset 00h) | ARB/MUX PM 超时控制寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register configures the ARB/MUX timeout mechanism for a PM Request ALMP that is awaiting a response, when operating in 256B Flit mode (see Section 5.1.2.4.2.2). This register is reserved in 68B Flit mode.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 0 | RW | PMTimeout Enable: When set, this enables the ARB/MUX timeout mechanism for PM Request ALMPs waiting for a response. Default value of this bit is 1. |
| 2:1 | RW | PMTimeout Value: This field configures the timeout value that the ARB/MUX uses while waiting for PM Response ALMPs.<br>• 00b = 1 ms<br>• All other encodings are reserved<br>Default value of this field is 00b. |
| 31:3 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

此寄存器在以 256B Flit 模式操作时 (参见第 5.1.2.4.2.2 节) 为等待响应的 PM Request ALMP 配置 ARB/MUX 超时机制。此寄存器在 68B Flit 模式下保留。

| 位 | 属性 | 描述 |
|-----|------|------|
| 0 | RW | PMTimeout Enable: 置位时, 启用 ARB/MUX 超时机制, 用于等待响应的 PM Request ALMP。该位的默认值为 1。 |
| 2:1 | RW | PMTimeout Value: 此字段配置 ARB/MUX 在等待 PM Response ALMP 时使用的超时值。<br>• 00b = 1 ms<br>• 所有其他编码保留<br>此字段的默认值为 00b。 |
| 31:3 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-5-2"></a>
### 8.2.5.2 ARB/MUX Uncorrectable Error Status Register (Offset 04h) | ARB/MUX 不可纠正错误状态寄存器 (偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register logs the timeouts that are encountered during ARB/MUX PM flows when operating in 256B Flit mode. This register is reserved in 68B Flit mode.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 0 | RW1CS | PM Timeout Error: For 256B Flit mode, this bit is set by the ARB/MUX to signal that a PM Request ALMP did not receive a response of ACTIVE.PMNAK or the corresponding PM Status ALMP by the time the PMTimeout counter expires. It must only be logged if PMTimeout Enable is set in the ARB/MUX PM Timeout Control register and the ARB/MUX is operating in 256B Flit mode. |
| 1 | RW1CS | L0p Timeout Error: For 256B Flit mode, this bit is set by the ARB/MUX to signal that an L0p Request ALMP did not receive a response from the remote Link partner by the time the PMTimeout counter expires. It must only be logged if PMTimeout Enable is set in the ARB/MUX PM Timeout Control register and the ARB/MUX is operating in 256B Flit mode. |
| 31:2 | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

此寄存器在以 256B Flit 模式操作时记录 ARB/MUX PM 流程中遇到的超时。此寄存器在 68B Flit 模式下保留。

| 位 | 属性 | 描述 |
|-----|------|------|
| 0 | RW1CS | PM Timeout Error: 对于 256B Flit 模式, 当 PM Request ALMP 在 PMTimeout 计数器到期之前未收到 ACTIVE.PMNAK 响应或相应的 PM Status ALMP 时, 此位由 ARB/MUX 设置以发出信号。仅当在 ARB/MUX PM Timeout Control 寄存器中设置了 PMTimeout Enable 且 ARB/MUX 以 256B Flit 模式操作时, 才应记录此位。 |
| 1 | RW1CS | L0p Timeout Error: 对于 256B Flit 模式, 当 L0p Request ALMP 在 PMTimeout 计数器到期之前未收到来自远程链路伙伴的响应时, 此位由 ARB/MUX 设置以发出信号。仅当在 ARB/MUX PM Timeout Control 寄存器中设置了 PMTimeout Enable 且 ARB/MUX 以 256B Flit 模式操作时, 才应记录此位。 |
| 31:2 | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-5-3"></a>
### 8.2.5.3 ARB/MUX Uncorrectable Error Mask Register (Offset 08h) | ARB/MUX 不可纠正错误掩码寄存器 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

This register controls the logging and signaling of the timeouts that are encountered during ARB/MUX PM flows when operating in 256B Flit mode. This register is reserved in 68B Flit mode.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 0 | RWS | PM Timeout Error Mask<br>• 0 = PM Timeout Error is logged as an Internal Uncorrected Error in the associated root port, similar to CXL.cachemem errors<br>• 1 = PM Timeout Error is not recorded or reported<br>Default value of this bit is 1. |
| 1 | RWS | L0p Timeout Error Mask<br>• 0 = L0p Timeout Error is logged as an Internal Uncorrected Error in the associated root port, similar to CXL.cachemem errors<br>• 1 = L0p Timeout Error is not recorded or reported<br>Default value of this bit is 1. |
| 31:2 | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

此寄存器控制在以 256B Flit 模式操作时 ARB/MUX PM 流程中遇到的超时的记录和信令。此寄存器在 68B Flit 模式下保留。

| 位 | 属性 | 描述 |
|-----|------|------|
| 0 | RWS | PM Timeout Error Mask<br>• 0 = PM Timeout Error 作为内部未纠正错误 (Internal Uncorrected Error) 记录在关联的根端口中, 类似于 CXL.cachemem 错误<br>• 1 = 不记录或报告 PM Timeout Error<br>该位的默认值为 1。 |
| 1 | RWS | L0p Timeout Error Mask<br>• 0 = L0p Timeout Error 作为内部未纠正错误记录在关联的根端口中, 类似于 CXL.cachemem 错误<br>• 1 = 不记录或报告 L0p Timeout Error<br>该位的默认值为 1。 |
| 31:2 | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-5-4"></a>
### 8.2.5.4 ARB/MUX Arbitration Control Register for CXL.io (Offset 180h) | CXL.io 的 ARB/MUX 仲裁控制寄存器 (偏移量 180h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit | Attributes | Description |
|-----|------------|-------------|
| 3:0 | RsvdP | Reserved |
| 7:4 | RW | CXL.io Weighted Round Robin Arbitration Weight: This is the weight assigned to CXL.io in the weighted round-robin arbitration between CXL protocols. Default value of this field is 0h. |
| 31:8 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位 | 属性 | 描述 |
|-----|------|------|
| 3:0 | RsvdP | 保留 |
| 7:4 | RW | CXL.io Weighted Round Robin Arbitration Weight: 这是 CXL.io 在 CXL 协议之间的加权轮询仲裁中分配的权重。此字段的默认值为 0h。 |
| 31:8 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-5-5"></a>
### 8.2.5.5 ARB/MUX Arbitration Control Register for CXL.cache and CXL.mem (Offset 1C0h) | CXL.cache 和 CXL.mem 的 ARB/MUX 仲裁控制寄存器 (偏移量 1C0h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit | Attributes | Description |
|-----|------------|-------------|
| 3:0 | RsvdP | Reserved |
| 7:4 | RW | CXL.cache and CXL.mem Weighted Round Robin Arbitration Weight: This is the weight assigned to CXL.cache and CXL.mem in the weighted round-robin arbitration between CXL protocols. Default value of this field is 0h. |
| 31:8 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位 | 属性 | 描述 |
|-----|------|------|
| 3:0 | RsvdP | 保留 |
| 7:4 | RW | CXL.cache and CXL.mem Weighted Round Robin Arbitration Weight: 这是 CXL.cache 和 CXL.mem 在 CXL 协议之间的加权轮询仲裁中分配的权重。此字段的默认值为 0h。 |
| 31:8 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-6"></a>
## 8.2.6 BAR Virtualization ACL Register Block | BAR 虚拟化 ACL 寄存器块

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

These registers are located at a 64-KB-aligned offset within one of the device's BARs (or BEI) as indicated by the Register Locator DVSEC (see Section 8.1.9) BAR Virtualization ACL Register Base register. They may be implemented by a CXL device that implements the DVSEC BAR Virtualization ACL Register Base register. The registers specify a standard way of communicating to the hypervisors which sections of the device BAR space are safe to assign to a Virtual Machine (VM) when the PF is directly assigned to that VM. Identifying which registers are unsafe for assigning to a VM will depend on the device micro architecture and the device security objectives, and is beyond the scope of this specification. However, examples could include registers that might affect correct operation of the device memory controller, perform device burn-in by altering its frequency or voltage, or bypass hypervisor protections for isolation of device memory assigned to one VM from the remainder of the system.

The registers consist of an array of 3 tuples of register blocks. Each tuple represents a set of contiguous registers that are safe to assign to a VM. The 3 tuples consist of the BAR number (or BAR Equivalent Index), Offset within the BAR to the start of the registers which can be safely assigned (64-KB aligned), and the size of the assigned register block (multiple of 64 KB).

> **Table 8-31.** BAR Virtualization ACL Register Block Layout
>
> | Offset | Register Name |
> |--------|---------------|
> | 00h | BAR Virtualization ACL Size Register |
> | **Entry 0:** | |
> | 08h | BAR Virtualization ACL Array Entry Offset Register[0] |
> | 10h | BAR Virtualization ACL Array Entry Size Register[0] |
> | **Entry 1:** | |
> | 18h | BAR Virtualization ACL Array Entry Offset Register[1] |
> | 20h | BAR Virtualization ACL Array Entry Size Register[1] |
> | **Entry n:** | |
> | 10h *n+ 8 | ... |

</td><td style="background-color:#e8e8e8">

这些寄存器位于设备 BAR (或 BEI) 之一的 64-KB 对齐偏移处, 如 Register Locator DVSEC (参见第 8.1.9 节) BAR Virtualization ACL Register Base 寄存器所示。它们可由实现 DVSEC BAR Virtualization ACL Register Base 寄存器的 CXL 设备实现。这些寄存器指定了一种与虚拟机监控程序 (hypervisor) 通信的标准方式, 即当 PF 直接分配给虚拟机 (VM) 时, 设备 BAR 空间的哪些部分是安全可分配给 VM 的。识别哪些寄存器对于分配给 VM 是不安全的, 将取决于设备微体系结构和设备安全目标, 不在本规范的范围内。然而, 示例可能包括可能影响设备内存控制器正确操作的寄存器、通过改变频率或电压执行设备老化测试, 或绕过虚拟机监控程序保护以将分配给一个 VM 的设备内存与系统其余部分隔离的寄存器。

这些寄存器由一个 3 元组数组的寄存器块组成。每个元组表示一组可以安全分配给 VM 的连续寄存器。这 3 个元组包括 BAR 编号 (或 BAR 等效索引)、可安全分配的寄存器起始 BAR 内的偏移 (64-KB 对齐) 和所分配寄存器块的大小 (64 KB 的倍数)。

> **表 8-31.** BAR 虚拟化 ACL 寄存器块布局
>
> | 偏移量 | 寄存器名称 |
> |--------|------------|
> | 00h | BAR Virtualization ACL Size Register |
> | **Entry 0:** | |
> | 08h | BAR Virtualization ACL Array Entry Offset Register[0] |
> | 10h | BAR Virtualization ACL Array Entry Size Register[0] |
> | **Entry 1:** | |
> | 18h | BAR Virtualization ACL Array Entry Offset Register[1] |
> | 20h | BAR Virtualization ACL Array Entry Size Register[1] |
> | **Entry n:** | |
> | 10h *n+ 8 | ... |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-6-1"></a>
### 8.2.6.1 BAR Virtualization ACL Size Register (Offset 00h) | BAR 虚拟化 ACL 大小寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit | Attributes | Description |
|-----|------------|-------------|
| 9:0 | HwInit | Number of Array Entries: Number of array elements starting at Offset 08h in this register block. Each array element consists of two 64-bit registers - Entry offset register, Entry Size register. |
| 31:10 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

| 位 | 属性 | 描述 |
|-----|------|------|
| 9:0 | HwInit | Number of Array Entries: 此寄存器块中从偏移量 08h 开始的数组元素数。每个数组元素由两个 64 位寄存器组成 - 条目偏移寄存器和条目大小寄存器。 |
| 31:10 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-6-1-1"></a>
#### 8.2.6.1.1 BAR Virtualization ACL Array Entry Offset Register (Offset: Varies) | BAR 虚拟化 ACL 数组条目偏移寄存器 (偏移量: 可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit | Attributes | Description |
|-----|------------|-------------|
| 3:0 | HwInit | Register BIR: Indicates which one of a Function's BARs, located beginning at Offset 10h in Configuration Space, or entry in the Enhanced Allocation capability with a matching BAR Equivalent Indicator (BEI), is being referenced.<br>Defined encodings are:<br>• 0h = Base Address Register 10h<br>• 1h = Base Address Register 14h<br>• 2h = Base Address Register 18h<br>• 3h = Base Address Register 1Ch<br>• 4h = Base Address Register 20h<br>• 5h = Base Address Register 24h<br>All other encodings are reserved |
| 15:4 | RsvdP | Reserved |
| 63:16 | HwInit | Start Offset: Offset[63:16] from the address contained by the function's BAR to the Register block within that BAR that can be safely assigned to a Virtual Machine. The starting offset is 64-KB aligned since Offset[15:0] are assumed to be 0. |

</td><td style="background-color:#e8e8e8">

| 位 | 属性 | 描述 |
|-----|------|------|
| 3:0 | HwInit | Register BIR: 指示正在引用配置的 BAR 中的哪一个 (从配置空间中的偏移量 10h 开始), 或是与匹配 BAR 等效指示符 (BEI) 的增强分配能力中的条目。<br>已定义编码:<br>• 0h = 基址寄存器 10h<br>• 1h = 基址寄存器 14h<br>• 2h = 基址寄存器 18h<br>• 3h = 基址寄存器 1Ch<br>• 4h = 基址寄存器 20h<br>• 5h = 基址寄存器 24h<br>所有其他编码保留 |
| 15:4 | RsvdP | 保留 |
| 63:16 | HwInit | Start Offset: 从功能 BAR 所包含的地址到该 BAR 内可安全分配给虚拟机的寄存器块的偏移量 Offset[63:16]。由于 Offset[15:0] 假定为 0, 起始偏移是 64-KB 对齐的。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-6-1-2"></a>
#### 8.2.6.1.2 BAR Virtualization ACL Array Entry Size Register (Offset: Varies) | BAR 虚拟化 ACL 数组条目大小寄存器 (偏移量: 可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

| Bit | Attributes | Description |
|-----|------------|-------------|
| 15:0 | RsvdP | Reserved |
| 63:16 | HwInit | Size: Indicates the Size[63:16] of the register space in bytes within the BAR that can be safely assigned to a VM. Size is a multiple of 64 KB since Size[15:0] are assumed to be 0. |

</td><td style="background-color:#e8e8e8">

| 位 | 属性 | 描述 |
|-----|------|------|
| 15:0 | RsvdP | 保留 |
| 63:16 | HwInit | Size: 指示可安全分配给 VM 的 BAR 内寄存器空间的字节大小 Size[63:16]。由于 Size[15:0] 假定为 0, 大小是 64 KB 的倍数。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7"></a>
## 8.2.7 CPMU Register Interface | CPMU 寄存器接口

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Each CPMU implements a set of CPMU scoped registers and a set of Counter scoped registers. Unimplemented registers such as Counter Data and Counter Configuration registers for non-existent Counters follow the RsvdP behavior.

> **Table 8-32.** CPMU Register Layout (Version=1) (Sheet 1 of 2)
>
> | Byte Offset | Length in Bytes | Register Name |
> |-------------|-----------------|---------------|
> | 00h | 8 | CPMU Capability (see Section 8.2.7.1.1) |
> | 08h | 8 | Reserved |
> | 10h | 8 | CPMU Overflow Status (see Section 8.2.7.1.2) |
> | 18h | 8 | CPMU Freeze (see Section 8.2.7.1.3) |
> | 20h | 224 | Reserved |
> | 100h | 8 | CPMU Event Capabilities [0] (see Section 8.2.7.1.4) |
> | 108h | 8 | CPMU Event Capabilities [1] |
> | ... | ... | ... |
> | 1F8h | 8 | CPMU Event Capabilities [31] |
> | 200h | 8 | Counter Unit 0 - Counter Configuration (see Section 8.2.7.2.1) |
> | 208h | 8 | Counter Unit 1 - Counter Configuration |
> | ... | ... | ... |
> | 3F8h | 8 | Counter Unit 63 - Counter Configuration |
> | 400h | 4 | Counter Unit 0 Filter ID 0 - Filter Configuration (see Section 8.2.7.2.2) |
> | 404h | 4 | Counter Unit 0 Filter ID 1 - Filter Configuration |
> | ... | ... | ... |
> | 41Ch | 4 | Counter Unit 0 Filter ID 7 - Filter Configuration |
> | 420h | 4 | Counter Unit 1 Filter ID 0 - Filter Configuration |
> | ... | ... | ... |
> | BFCh | 4 | Counter Unit 63 Filter ID 7 - Filter Configuration |
> | C00h | 8 | Counter Unit 0 - Counter Data (see Section 8.2.7.2.3) |
> | C08h | 8 | Counter Unit 1 - Counter Data |
> | ... | ... | ... |
> | DF8h | 8 | Counter Unit 63 - Counter Data |

</td><td style="background-color:#e8e8e8">

每个 CPMU 实现一组 CPMU 作用域寄存器和一组计数器作用域寄存器。未实现的寄存器 (例如不存在计数器的计数器数据寄存器和计数器配置寄存器) 遵循 RsvdP 行为。

> **表 8-32.** CPMU 寄存器布局 (Version=1) (第 1 页, 共 2 页)
>
> | 字节偏移量 | 字节长度 | 寄存器名称 |
> |------------|----------|------------|
> | 00h | 8 | CPMU Capability (参见第 8.2.7.1.1 节) |
> | 08h | 8 | 保留 |
> | 10h | 8 | CPMU Overflow Status (参见第 8.2.7.1.2 节) |
> | 18h | 8 | CPMU Freeze (参见第 8.2.7.1.3 节) |
> | 20h | 224 | 保留 |
> | 100h | 8 | CPMU Event Capabilities [0] (参见第 8.2.7.1.4 节) |
> | 108h | 8 | CPMU Event Capabilities [1] |
> | ... | ... | ... |
> | 1F8h | 8 | CPMU Event Capabilities [31] |
> | 200h | 8 | Counter Unit 0 - Counter Configuration (参见第 8.2.7.2.1 节) |
> | 208h | 8 | Counter Unit 1 - Counter Configuration |
> | ... | ... | ... |
> | 3F8h | 8 | Counter Unit 63 - Counter Configuration |
> | 400h | 4 | Counter Unit 0 Filter ID 0 - Filter Configuration (参见第 8.2.7.2.2 节) |
> | 404h | 4 | Counter Unit 0 Filter ID 1 - Filter Configuration |
> | ... | ... | ... |
> | 41Ch | 4 | Counter Unit 0 Filter ID 7 - Filter Configuration |
> | 420h | 4 | Counter Unit 1 Filter ID 0 - Filter Configuration |
> | ... | ... | ... |
> | BFCh | 4 | Counter Unit 63 Filter ID 7 - Filter Configuration |
> | C00h | 8 | Counter Unit 0 - Counter Data (参见第 8.2.7.2.3 节) |
> | C08h | 8 | Counter Unit 1 - Counter Data |
> | ... | ... | ... |
> | DF8h | 8 | Counter Unit 63 - Counter Data |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-1"></a>
### 8.2.7.1 Per CPMU Registers | 每个 CPMU 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Each CPMU instance is associated with a CPMU Capability register, a CPMU Overflow Status register, zero or one CPMU Freeze register, and one or more CPMU Event Capabilities registers.

</td><td style="background-color:#e8e8e8">

每个 CPMU 实例与一个 CPMU Capability 寄存器、一个 CPMU Overflow Status 寄存器、零个或一个 CPMU Freeze 寄存器以及一个或多个 CPMU Event Capabilities 寄存器相关联。

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-1-1"></a>
#### 8.2.7.1.1 CPMU Capability (Offset 00h) | CPMU 能力 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CPMU-wide capabilities shall be enumerated by the CPMU Capability register.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 5:0 | HwInit | Number of Counter Units: The number of Counter Units that are part of this CPMU, represented using 0-based encoding.<br>• 00h = 1 Counter Unit<br>• 01h = 2 Counter Units<br>• …<br>• 3Fh = 64 Counter Units |
| 7:6 | RsvdP | Reserved |
| 15:8 | HwInit | Counter Width: The number of bits supported by every Counter Data register. If the value of this field is n, then each Counter Data register (see Section 8.2.7.2.3) implements n least significant bits and the maximum value it can count is 2^n-1. |
| 19:16 | RsvdP | Reserved |
| 24:20 | HwInit | Number of Event Capabilities Registers Supported: Indicates the number of CPMU Event Capabilities registers, represented using 0-based encoding.<br>• 00h = 1 CPMU Event Capabilities register<br>• 01h = 2 CPMU Event Capabilities registers<br>• …<br>• 1Fh = 32 CPMU Event Capabilities registers |
| 31:25 | RsvdP | Reserved |
| 39:32 | HwInit | Filters Supported: Bitmask that indicates the entire set of Filter IDs are supported by this CPMU. The Filter IDs available for a given Event may be restricted further. Table 13-5 describes which Filter IDs are permitted for each Event. Section 8.2.7.2.2 describes the details for each of the filters supported. The number of Filter Configuration registers per Counter Unit corresponds to the number of 1s in this field. |
| 43:40 | RsvdP | Reserved |
| 47:44 | HwInit | Interrupt Message Number: If Interrupt on Overflow Support=1, this field indicates which MSI/MSI-X vector is used for the interrupt message generated in association with this CPMU instance.<br>For MSI, the value in this field indicates the offset between the base Message Data and the interrupt message that is generated. Hardware is required to update this field so that it is correct if the number of MSI Messages assigned to the Function changes when software writes to the Multiple Message Enable field in the Message Control register for MSI. For MSI-X, the value in this field indicates which MSI-X Table entry is used to generate the interrupt message. The entry shall be one of the first 16 entries even if the Function implements more than 16 entries. The value in this field shall be within the range configured by system software to the device. For a given MSI-X implementation, the entry shall remain constant.<br>If both MSI and MSI-X are implemented, they are permitted to use different vectors, though software is permitted to enable only one mechanism at a time. If MSI-X is enabled, the value in this field shall indicate the vector for MSI-X. If MSI is enabled or neither is enabled, the value in this field indicate the vector for MSI. If software enables both MSI and MSI-X at the same time, the value in this field is undefined.<br>It is recommended that the component allocate a distinct Interrupt Message Number to each CPMU instance. |
| 48 | HwInit | Counters Writable while Frozen<br>• 0 = Indicates that the software must not write to any Counter Data register while that counter is enabled or frozen. If software writes to the Counter data register when counter is enabled or frozen, it leads to undefined behavior. Fixed Function Counter Data registers as well as Configurable Counter Data registers are always writable while disabled regardless of the state of this bit. Free-running Counter Data registers are never writable regardless of the state of this bit.<br>• 1 = Indicates that the software is permitted to write and modify any Fixed-function Counter Data register or any Configurable Counter Data register while it is frozen. |
| 49 | HwInit | Counter Freeze Support<br>• 0 = The CPMU does not support Counter Freeze capability. The CPMU Freeze register and the Global Freeze on Overflow bit in the Counter Configuration registers are reserved.<br>• 1 = The CPMU supports Counter Freeze capability. The CPMU Freeze register and the Global Freeze on Overflow bit in the Counter Configuration registers are implemented. |
| 50 | HwInit | Interrupt on Overflow Support<br>• 0 = The CPMU does not support generation of interrupts upon counter overflow.<br>• 1 = The CPMU supports generation of interrupt upon counter overflow. Interrupt generation is controlled by the Interrupt on Overflow bit in the Counter Configuration register. The interrupt Message Number is reported in the Interrupt Message Number field. |
| 59:51 | RsvdP | Reserved |
| 63:60 | HwInit | Version: Set to 1. The layout of CPMU registers for Version=1 is shown in Table 8-32.<br>The version is incremented whenever the CPMU register structure is extended to add more functionality. Backward compatibility shall be maintained during this process. For all values of n, version n+1 may extend version n by replacing fields that are marked as reserved in version n or appending new registers but must not redefine the meaning of existing fields. Software that was written for a lower version may continue to operate on CPMU registers with a higher version but will not be able to take advantage of new functionality. Each field in the CPMU register structure is assumed to be introduced in version 1 of that structure unless specified otherwise in the field's definition in this specification. |

</td><td style="background-color:#e8e8e8">

CPMU 范围的能力应通过 CPMU Capability 寄存器枚举。

| 位 | 属性 | 描述 |
|-----|------|------|
| 5:0 | HwInit | Number of Counter Units: 此 CPMU 所包含的计数器单元数, 使用基于 0 的编码表示。<br>• 00h = 1 个 Counter Unit<br>• 01h = 2 个 Counter Unit<br>• …<br>• 3Fh = 64 个 Counter Unit |
| 7:6 | RsvdP | 保留 |
| 15:8 | HwInit | Counter Width: 每个 Counter Data 寄存器支持的位数。如果此字段的值为 n, 则每个 Counter Data 寄存器 (参见第 8.2.7.2.3 节) 实现 n 个最低有效位, 并且它可以计数的最大值为 2^n-1。 |
| 19:16 | RsvdP | 保留 |
| 24:20 | HwInit | Number of Event Capabilities Registers Supported: 指示 CPMU Event Capabilities 寄存器的数量, 使用基于 0 的编码表示。<br>• 00h = 1 个 CPMU Event Capabilities 寄存器<br>• 01h = 2 个 CPMU Event Capabilities 寄存器<br>• …<br>• 1Fh = 32 个 CPMU Event Capabilities 寄存器 |
| 31:25 | RsvdP | 保留 |
| 39:32 | HwInit | Filters Supported: 位掩码, 指示此 CPMU 支持的整个 Filter ID 集。可用于给定事件的 Filter ID 可能会受到进一步限制。表 13-5 描述了每个事件允许的 Filter ID。第 8.2.7.2.2 节描述了每个支持的过滤器的详细信息。每个 Counter Unit 的 Filter Configuration 寄存器数与此字段中 1 的数量相对应。 |
| 43:40 | RsvdP | 保留 |
| 47:44 | HwInit | Interrupt Message Number: 如果 Interrupt on Overflow Support=1, 则此字段指示与此 CPMU 实例关联生成的中断消息所使用的 MSI/MSI-X 向量。<br>对于 MSI, 此字段中的值表示基本消息数据与生成的中断消息之间的偏移量。当软件写入 MSI 消息控制寄存器的 Multiple Message Enable 字段而导致分配给该功能的消息数发生变化时, 硬件需要更新此字段以使其正确。对于 MSI-X, 此字段中的值指示用于生成中断消息的 MSI-X 表条目。即使该功能实现了 16 个以上条目, 该条目也必须是前 16 个条目之一。此字段中的值应处于系统软件配置给设备的范围内。对于给定的 MSI-X 实现, 该条目应保持不变。<br>如果同时实现了 MSI 和 MSI-X, 则它们允许使用不同的向量, 但软件一次只允许启用一种机制。如果启用了 MSI-X, 则此字段中的值应指示 MSI-X 的向量。如果启用了 MSI 或两者都未启用, 则此字段中的值指示 MSI 的向量。如果软件同时启用 MSI 和 MSI-X, 则此字段中的值未定义。<br>建议组件为每个 CPMU 实例分配不同的 Interrupt Message Number。 |
| 48 | HwInit | Counters Writable while Frozen<br>• 0 = 表示在计数器启用或冻结时, 软件不得写入任何 Counter Data 寄存器。如果在计数器启用或冻结时软件写入 Counter Data 寄存器, 则会导致未定义的行为。无论此位的状态如何, 固定功能计数器数据寄存器和可配置计数器数据寄存器在禁用时始终可写。无论此位的状态如何, 自由运行的 Counter Data 寄存器永远不可写。<br>• 1 = 表示允许软件在冻结时写入和修改任何固定功能 Counter Data 寄存器或任何可配置 Counter Data 寄存器。 |
| 49 | HwInit | Counter Freeze Support<br>• 0 = CPMU 不支持 Counter Freeze 功能。CPMU Freeze 寄存器和 Counter Configuration 寄存器中的 Global Freeze on Overflow 位被保留。<br>• 1 = CPMU 支持 Counter Freeze 功能。CPMU Freeze 寄存器和 Counter Configuration 寄存器中的 Global Freeze on Overflow 位均被实现。 |
| 50 | HwInit | Interrupt on Overflow Support<br>• 0 = CPMU 不支持在计数器溢出时生成中断。<br>• 1 = CPMU 支持在计数器溢出时生成中断。中断生成由 Counter Configuration 寄存器中的 Interrupt on Overflow 位控制。中断 Message Number 在 Interrupt Message Number 字段中报告。 |
| 59:51 | RsvdP | 保留 |
| 63:60 | HwInit | Version: 设置为 1。Version=1 的 CPMU 寄存器布局如表 8-32 所示。<br>每当扩展 CPMU 寄存器结构以添加更多功能时, 版本都会递增。在此过程中应保持向后兼容性。对于 n 的所有值, 版本 n+1 可以通过替换版本 n 中标记为保留的字段或追加新寄存器来扩展版本 n, 但不得重新定义现有字段的含义。为较低版本编写的软件可以继续在较高版本的 CPMU 寄存器上运行, 但将无法利用新功能。除非在规范的字段定义中另有规定, 否则 CPMU 寄存器结构中的每个字段都假定在该结构的版本 1 中引入。 |

</td></tr>
</tbody>
</table>

> **Figure 8-70.** CPMU Register Layout (Version=1) (Sheet 1 of 2) ｜ CPMU 寄存器布局 (Version=1) (第 1 页, 共 2 页)
>
> <img src="figures/chapter_08/page_0602.png" alt="Figure 8-70" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0602.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-1-2"></a>
#### 8.2.7.1.2 CPMU Overflow Status (Offset 10h) | CPMU 溢出状态 (偏移量 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CPMU Overflow Status register indicates the overflow status associated with all the Counter Units.

When any bit in Overflow Status transitions from 0 to 1, the CPMU shall issue an MSI/MSI-X if the Interrupt on Overflow bit for the corresponding Counter Unit is 1.

| Bit | Attributes | Description |
|-----|------------|-------------|
| C:0 | RW1C | Overflow Status: Bitmask with 1 bit per Counter Unit. The bit N indicates whether the Counter Unit N has encountered an overflow condition.<br>• 0 = The Counter Unit N has not encountered an overflow condition<br>• 1 = The Counter Unit N has encountered an overflow condition<br>where 0 <= N <=C.<br>C equals the raw value reported by the Number of Counter Units field in the CPMU Capability register. |
| 63:C+1 | RsvdP | Reserved |

#### IMPLEMENTATION NOTE

If Counter Freeze Support as well as Counters Writable while Frozen are both 1, software may use the following flow to start counting multiple events simultaneously:
1. Freeze the counters that are involved in counting these events.
2. Initialize the Counter Data registers that correspond to these counters.
3. Unfreeze the counters.

</td><td style="background-color:#e8e8e8">

CPMU Overflow Status 寄存器指示与所有 Counter Unit 关联的溢出状态。

当 Overflow Status 中的任何位从 0 转换为 1 时, 如果相应 Counter Unit 的 Interrupt on Overflow 位为 1, 则 CPMU 应发出 MSI/MSI-X。

| 位 | 属性 | 描述 |
|-----|------|------|
| C:0 | RW1C | Overflow Status: 每个 Counter Unit 1 位的位掩码。第 N 位表示 Counter Unit N 是否遇到溢出条件。<br>• 0 = Counter Unit N 未遇到溢出条件<br>• 1 = Counter Unit N 遇到溢出条件<br>其中 0 <= N <=C。<br>C 等于 CPMU Capability 寄存器中 Number of Counter Units 字段报告的原始值。 |
| 63:C+1 | RsvdP | 保留 |

#### 实现注意

如果 Counter Freeze Support 和 Counters Writable while Frozen 都为 1, 则软件可以使用以下流程同时开始对多个事件进行计数:
1. 冻结涉及对这些事件计数的计数器。
2. 初始化与这些计数器对应的 Counter Data 寄存器。
3. 取消冻结计数器。

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-1-3"></a>
#### 8.2.7.1.3 CPMU Freeze (Offset 18h) | CPMU 冻结 (偏移量 18h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CPMU Freeze register indicates the freeze status associated with all the Counter Units and may be used to freeze or unfreeze individual Counter Units. This register is implemented only if the Counter Freeze Support bit in the CPMU Capability register is 1.

| Bit | Attributes | Description |
|-----|------------|-------------|
| C:0 | RW/RsvdZ | Freeze Control and Status: The attribute for the bits corresponding to Free-running Counter Units is RsvdZ.<br>• Writing 0 to bit N: The Counter Unit N is unfrozen and resumes counting unless Counter Enable=0, in which case the Counter Unit remains disabled. If the Counter Unit N is enabled but not currently frozen, it is unaffected and continues to count events.<br>• Writing 1 to bit N: The Counter Unit N, if enabled, is frozen and stops counting further events, and retains its current value. If the Counter Unit N is already frozen when this bit is set, it remains frozen.<br>Reads return the current freeze status of each counter:<br>• If bit N reads as 0: The Counter Unit N is currently not frozen. The Counter Unit N may be disabled (Counter Enable=0), or may be enabled and counting events.<br>• If bit N reads as 1: The Counter Unit N is currently frozen and not counting events. Counter Unit N remains frozen until explicitly unfrozen by software.<br>where 0 <= N <=C.<br>C equals the raw value reported by the Number of Counter Units field in the CPMU Capability register. |
| 63:C | RsvdZ | Reserved |

</td><td style="background-color:#e8e8e8">

CPMU Freeze 寄存器指示与所有 Counter Unit 关联的冻结状态, 可用于冻结或解冻各个 Counter Unit。仅当 CPMU Capability 寄存器中的 Counter Freeze Support 位为 1 时, 才实现此寄存器。

| 位 | 属性 | 描述 |
|-----|------|------|
| C:0 | RW/RsvdZ | Freeze Control and Status: 与自由运行 Counter Unit 对应的位的属性为 RsvdZ。<br>• 向位 N 写入 0: Counter Unit N 解冻并恢复计数, 除非 Counter Enable=0, 在这种情况下 Counter Unit 保持禁用状态。如果 Counter Unit N 已启用但当前未冻结, 则它不受影响并继续对事件计数。<br>• 向位 N 写入 1: 如果 Counter Unit N 已启用, 则将其冻结, 停止对更多事件计数, 并保留其当前值。如果在设置该位时 Counter Unit N 已冻结, 则它保持冻结状态。<br>读取返回每个计数器的当前冻结状态:<br>• 如果位 N 读取为 0: Counter Unit N 当前未冻结。Counter Unit N 可能被禁用 (Counter Enable=0), 或者可能已启用并正在对事件计数。<br>• 如果位 N 读取为 1: Counter Unit N 当前已冻结且未对事件计数。Counter Unit N 保持冻结状态, 直到软件明确解冻。<br>其中 0 <= N <=C。<br>C 等于 CPMU Capability 寄存器中 Number of Counter Units 字段报告的原始值。 |
| 63:C | RsvdZ | 保留 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-1-4"></a>
#### 8.2.7.1.4 CPMU Event Capabilities (Offset: Varies) | CPMU 事件能力 (偏移量: 可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Each CPMU Event Capabilities register corresponds to an Event group and reports the set of Event IDs supported by the Counter Units in the CPMU for that Event group including the Fixed Counter Units. The number of CPMU Event Capabilities registers corresponds to the Number of Event Groups encoded in the CPMU Capability register.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 31:0 | HwInit | Supported Events: Bitmask that identifies the Event IDs within this Event Group that each Configurable Counter Unit in this CPMU is capable of counting. 0 is not a valid value. |
| 47:32 | HwInit | Event Group ID: The Group ID assigned to this Event Group by the vendor identified by the Event Vendor ID field. |
| 63:48 | HwInit | Event Vendor ID: The Vendor ID assigned by PCI-SIG to the vendor that defined this event. The values of 0000h and FFFFh are reserved per PCIe Base Specification. |

</td><td style="background-color:#e8e8e8">

每个 CPMU Event Capabilities 寄存器对应一个事件组, 并报告该事件组中 CPMU 的 Counter Unit (包括 Fixed Counter Unit) 支持的事件 ID 集。CPMU Event Capabilities 寄存器的数量对应于 CPMU Capability 寄存器中编码的 Number of Event Groups。

| 位 | 属性 | 描述 |
|-----|------|------|
| 31:0 | HwInit | Supported Events: 位掩码, 标识此事件组内此 CPMU 中的每个可配置 Counter Unit 能够计数的事件 ID。0 不是有效值。 |
| 47:32 | HwInit | Event Group ID: 由 Event Vendor ID 字段标识的供应商分配给此事件组的组 ID。 |
| 63:48 | HwInit | Event Vendor ID: 由 PCI-SIG 分配给定义此事件的供应商的供应商 ID。根据 PCIe 基本规范, 0000h 和 FFFFh 的值保留。 |

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-2"></a>
### 8.2.7.2 Per Counter Unit Registers | 每个 Counter Unit 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

</td><td style="background-color:#e8e8e8">

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-2-1"></a>
#### 8.2.7.2.1 Counter Configuration (Offset: Varies) | Counter 配置 (偏移量: 可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The Counter Configuration registers specify the set of events that are to be monitored by each Counter Unit and how they are counted. They also control interrupt generation behavior and the behavior upon overflow detection. The number of Counter Configuration registers is specified by the Number of Counter Units field of the CPMU Capability register. When a counter is enabled, changes to any field except for the Counter Enable results in undefined behavior.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 1:0 | HwInit | Counter Type<br>• 00b = This is a Free-running Counter Unit. Some of the fields in this register are RO. See individual field definitions.<br>• 01b = This is a Fixed-function Counter Unit. Some of the fields in this register are RO. See individual field definitions.<br>• 10b = This is a Configurable Counter Unit.<br>• 11b = Reserved. |
| 7:2 | RsvdP | Reserved |
| 8 | RW/RO | Counter Enable<br>• 0 = This Counter Unit is disabled<br>• 1 = This Counter Unit is enabled to count events<br>If this is a free-running Counter Unit, this bit is RO and returns 1 to indicate this Counter Unit is always counting. If this bit is RW, the reset default of this bit is 0. |
| 9 | RW/RO | Interrupt on Overflow<br>• 0 = An Interrupt is not generated.<br>• 1 = Generate an Interrupt when this Counter Unit overflows. The interrupt Message Number is reported in the Interrupt Message Number field.<br>This bit must be RW if the Interrupt on Overflow Support bit in the CPMU Capability register is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the Interrupt on Overflow Support bit is set. If this bit is RW, the reset default of this bit is 0. |
| 10 | RW/RO | Global Freeze on Overflow<br>• 0 = No global freeze<br>• 1 = When this Counter Unit overflows, all Counter Units in the CPMU except the free-running Counter Units are frozen<br>This bit must be RW if the Counter Freeze Support bit in the CPMU Capability register is set; otherwise, it is permitted to be hardwired to 0. Software must not set this bit unless the Counter Freeze Support bit is set. If this bit is RW, the reset default of this bit is 0. |
| 11 | RW/RO | Edge: When Edge is 1, the Counter Data is incremented when the Event State transitions from 0 to 1. The Event State is defined as the OR of the events enabled by the Events mask field.<br>If this is a Free-running Counter Unit, this bit is RO.<br>If this is a Fixed-function Counter Unit, this bit is RO.<br>If this bit is RW, the reset default of this bit is 0. |
| 12 | RW/RO | Invert: See the definition of the Threshold field.<br>If this is a Free-running Counter Unit, this bit is RO.<br>If this is a Fixed-function Counter Unit, this bit is RO.<br>If this bit is RW, the reset default of this bit is 0. |
| 15:13 | RsvdP | Reserved |
| 23:16 | RW/RO | Threshold: Some events may ordinarily increment the Counter Data by more than 1 per cycle. Queue entry count is one example of such an event. For such events, the Threshold field can be used to modify the counting behavior. If Threshold is 0, the Counter Data register is incremented by the raw event count. If Threshold is not 0 and Invert=0, Counter Data register is incremented by 1 every clock cycle where the raw event count is greater than or equal to the Threshold. If Threshold is not 0 and Invert=1, Counter Data register is incremented by 1 every clock cycle where the raw event count is less than or equal to the Threshold.<br>For events that generate no more than one raw event per clock, Threshold shall be set to 1 by software.<br>If this is a Free-running Counter Unit, this field is RO.<br>If this is a Fixed-function Counter Unit, this field is RO.<br>If this field is RW, the reset default of this field is 01h. |
| 55:24 | RW/RO | Events: Bitmask that specifies the set of events that are to be monitored by this counter, corresponding to the Event Group selected by the Event Group ID Index field. The set of supported events depends on the value of Event Group as well as the CPMU implementation. Setting unsupported bits results in undefined behavior.<br>If this is a Free-running Counter Unit, this field is RO. More than one bit may be set.<br>If this is a Fixed Function Counter Unit, this field is RO. More than one bit may be set.<br>If this field is RW, the reset default of this field is 0000 0000h. |
| 58:56 | RsvdP | Reserved |
| 63:59 | RW/RO | Event Group ID Index: Identifies the CPMU Event Capabilities register that describes the Event Group ID. The value of 0 indicates the Event Vendor ID and Event Group ID that is identified by the first CPMU Event Capabilities register.<br>If this is a Free-running Counter Unit, this field shall be RO and return the Event Group ID Index that this counter supports. The Event Group ID Index field for a Configurable Counter Unit must not be set to the Event Group ID Index reported by a Free-running Counter Unit.<br>If this is a Fixed-function Counter Unit, this field shall be RO and return the Event Group ID Index that this counter supports. The Event Group ID Index field for a Configurable Counter Unit must not be set to the Event Group ID Index reported by a Fixed-function Counter Unit.<br>If this field is RW, the reset default of this field is 00h. |

</td><td style="background-color:#e8e8e8">

Counter Configuration 寄存器指定每个 Counter Unit 要监视的事件集以及如何对它们进行计数。它们还控制中断生成行为和溢出检测时的行为。Counter Configuration 寄存器的数量由 CPMU Capability 寄存器的 Number of Counter Units 字段指定。当计数器启用时, 除 Counter Enable 之外的任何字段更改都会导致未定义的行为。

| 位 | 属性 | 描述 |
|-----|------|------|
| 1:0 | HwInit | Counter Type (计数器类型)<br>• 00b = 这是自由运行的 Counter Unit。此寄存器中的一些字段为 RO。请参见各个字段定义。<br>• 01b = 这是固定功能 Counter Unit。此寄存器中的一些字段为 RO。请参见各个字段定义。<br>• 10b = 这是可配置 Counter Unit。<br>• 11b = 保留。 |
| 7:2 | RsvdP | 保留 |
| 8 | RW/RO | Counter Enable (计数器启用)<br>• 0 = 此 Counter Unit 已禁用<br>• 1 = 此 Counter Unit 已启用, 可对事件进行计数<br>如果这是自由运行的 Counter Unit, 则此位为 RO 并返回 1, 以指示此 Counter Unit 始终在计数。如果此位为 RW, 则该位的复位默认值为 0。 |
| 9 | RW/RO | Interrupt on Overflow (溢出时中断)<br>• 0 = 不生成中断。<br>• 1 = 当此 Counter Unit 溢出时生成中断。中断 Message Number 在 Interrupt Message Number 字段中报告。<br>如果 CPMU Capability 寄存器中的 Interrupt on Overflow Support 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 Interrupt on Overflow Support 位置位, 否则软件不得设置此位。如果此位为 RW, 则该位的复位默认值为 0。 |
| 10 | RW/RO | Global Freeze on Overflow (溢出时全局冻结)<br>• 0 = 无全局冻结<br>• 1 = 当此 Counter Unit 溢出时, CPMU 中的所有 Counter Unit (自由运行的 Counter Unit 除外) 都被冻结<br>如果 CPMU Capability 寄存器中的 Counter Freeze Support 位置位, 则此位必须为 RW; 否则, 允许硬连线为 0。除非 Counter Freeze Support 位置位, 否则软件不得设置此位。如果此位为 RW, 则该位的复位默认值为 0。 |
| 11 | RW/RO | Edge (边沿): 当 Edge 为 1 时, 当 Event State 从 0 转换为 1 时, Counter Data 递增。Event State 定义为由 Events 掩码字段启用的事件的 OR。<br>如果这是自由运行的 Counter Unit, 则此位为 RO。<br>如果这是固定功能 Counter Unit, 则此位为 RO。<br>如果此位为 RW, 则该位的复位默认值为 0。 |
| 12 | RW/RO | Invert (反转): 请参见 Threshold 字段的定义。<br>如果这是自由运行的 Counter Unit, 则此位为 RO。<br>如果这是固定功能 Counter Unit, 则此位为 RO。<br>如果此位为 RW, 则该位的复位默认值为 0。 |
| 15:13 | RsvdP | 保留 |
| 23:16 | RW/RO | Threshold (阈值): 某些事件通常每个周期可能使 Counter Data 递增多于 1。队列条目计数就是此类事件的一个示例。对于此类事件, Threshold 字段可用于修改计数行为。如果 Threshold 为 0, 则 Counter Data 寄存器按原始事件计数递增。如果 Threshold 不为 0 且 Invert=0, 则 Counter Data 寄存器在每个时钟周期内, 当原始事件计数大于或等于 Threshold 时递增 1。如果 Threshold 不为 0 且 Invert=1, 则 Counter Data 寄存器在每个时钟周期内, 当原始事件计数小于或等于 Threshold 时递增 1。<br>对于每个时钟生成不超过一个原始事件的事件, 软件应将 Threshold 设置为 1。<br>如果这是自由运行的 Counter Unit, 则此字段为 RO。<br>如果这是固定功能 Counter Unit, 则此字段为 RO。<br>如果此字段为 RW, 则该字段的复位默认值为 01h。 |
| 55:24 | RW/RO | Events (事件): 位掩码, 指定此计数器要监视的事件集, 对应于 Event Group ID Index 字段选择的事件组。支持的事件集取决于 Event Group 的值以及 CPMU 实现。设置不受支持的位会导致未定义的行为。<br>如果这是自由运行的 Counter Unit, 则此字段为 RO。可设置多个位。<br>如果这是固定功能 Counter Unit, 则此字段为 RO。可设置多个位。<br>如果此字段为 RW, 则该字段的复位默认值为 0000 0000h。 |
| 58:56 | RsvdP | 保留 |
| 63:59 | RW/RO | Event Group ID Index: 标识描述 Event Group ID 的 CPMU Event Capabilities 寄存器。值 0 表示由第一个 CPMU Event Capabilities 寄存器标识的 Event Vendor ID 和 Event Group ID。<br>如果这是自由运行的 Counter Unit, 则此字段应为 RO, 并返回此计数器支持的 Event Group ID Index。可配置 Counter Unit 的 Event Group ID Index 字段不得设置为自由运行 Counter Unit 所报告的 Event Group ID Index。<br>如果这是固定功能 Counter Unit, 则此字段应为 RO, 并返回此计数器支持的 Event Group ID Index。可配置 Counter Unit 的 Event Group ID Index 字段不得设置为固定功能 Counter Unit 所报告的 Event Group ID Index。<br>如果此字段为 RW, 则该字段的复位默认值为 00h。 |

</td></tr>
</tbody>
</table>

> **Figure 8-71.** Counter Configuration Register layout ｜ Counter 配置寄存器布局
>
> <img src="figures/chapter_08/page_0606.png" alt="Figure 8-71" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0606.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-2-2"></a>
#### 8.2.7.2.2 Filter Configuration (Offset: Varies) | 过滤器配置 (偏移量: 可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Each Counter Unit may support a set of Filter Configuration registers, one for each Filter ID. Filters constrain the counting of selected events based on one or more conditions specified in the Filter Configuration registers. For example, Counter Unit N Filter ID 0 - Filter Configuration register selects the HDM decoder(s) to monitor for events in counter N.

Each Counter Unit is associated with zero or more Filter Configuration registers, one for each supported Filter ID. The number of Filter Configuration registers per Counter Unit is derived by counting the 1s in the Filters Supported field in the CPMU Capability register.

If a filter is enabled for an event that it does not apply to, the Counter Unit behavior is undefined. When counting multiple events (multiple bits are set in Events field), Filter Configuration register must be set to all 1s. Otherwise, the Counter Unit behavior is undefined.

When multiple filters are configured for a counter, only the events that satisfy all the specified filters are counted (a logical AND of all the filter conditions).

When a counter is enabled, any changes to this register result in undefined behavior.

| Bit | Attributes | Description |
|-----|------------|-------------|
| 31:0 | RW | Filter Value: Specifies the filter value to be used for the Filter associated with this register.<br>The reset default value is FFFF FFFFh.<br>If this register is set to FFFF FFFFh, filtering is not performed for the associated Filter ID. When set to a value different from FFFF FFFFh, bits beyond the maximum value allowed for that filter are ignored.<br>The encoding of this register varies based on the Filter ID. See Table 8-33 for the encoding. |

> **Table 8-33.** Filter ID and Values
>
> | Filter ID | Description and Definition of the Filter Value Field |
> |-----------|-----------------------------------------------------|
> | 0 | Counts the events associated with the HDM decoder(s) specified in the Filter Value field in the Filter Configuration register. If bit n in the Filter Configuration register is set, events associated with HDM Decoder n are counted. For example, Filter Value=0Ah counts events associated with HDM Decoder 1 and HDM Decoder 3. |
> | 1 | Counts the events associated with the combinations of the Channel, Rank and Bank Groups, and Banks that are specified in the Filter Value field. Refer to Table 8-58 for definitions of these terms.<br>• Bits[7:0]: Bank Number, represented using 0-based encoding. The events associated with this DDR Bank are counted. If set to FFh, the CPMU shall count events associated with all Banks.<br>• Bits[15:8]: Bank Group, represented using 0-based encoding. The events associated with this DDR Bank Group are counted. If set to FFh, the CPMU shall count events associated with all Bank Groups.<br>• Bits[23:16]: Rank Number, represented using 0-based encoding. The events associated with this DDR Rank are counted. If set to FFh, the CPMU shall count events associated with all Ranks.<br>• Bits[31:24]: Channel Number, represented using 0-based encoding. The events associated with this DDR Channel are counted. If set to FFh, the CPMU shall count events associated with all Channels.<br>For example, Filter Value=0004 FF00h counts events associated with Bank 0 in all Bank Groups associated with Rank 4 in Channel 0. |
> | 7:2 | Reserved. Filter ID registers 2-7 for every counter are also reserved. |

</td><td style="background-color:#e8e8e8">

每个 Counter Unit 可以支持一组 Filter Configuration 寄存器, 每个 Filter ID 一个。过滤器根据 Filter Configuration 寄存器中指定的一个或多个条件限制对所选事件的计数。例如, Counter Unit N Filter ID 0 - Filter Configuration 寄存器选择要在计数器 N 中监视事件的 HDM 解码器。

每个 Counter Unit 与零个或多个 Filter Configuration 寄存器相关联, 每个支持的 Filter ID 一个。每个 Counter Unit 的 Filter Configuration 寄存器数通过对 CPMU Capability 寄存器中的 Filters Supported 字段中的 1 的数量得出。

如果为不适用的事件启用了过滤器, 则 Counter Unit 行为未定义。当对多个事件计数时 (Events 字段中设置了多个位), Filter Configuration 寄存器必须设置为全 1。否则, Counter Unit 行为未定义。

当为计数器配置了多个过滤器时, 仅对满足所有指定过滤器的事件进行计数 (所有过滤器条件的逻辑与)。

当计数器启用时, 对此寄存器的任何更改都会导致未定义的行为。

| 位 | 属性 | 描述 |
|-----|------|------|
| 31:0 | RW | Filter Value: 指定要与此寄存器关联的过滤器一起使用的过滤器值。<br>复位默认值为 FFFF FFFFh。<br>如果此寄存器设置为 FFFF FFFFh, 则不会对关联的 Filter ID 执行过滤。当设置为不同于 FFFF FFFFh 的值时, 超出该过滤器所允许的最大值的位将被忽略。<br>此寄存器的编码基于 Filter ID 而变化。有关编码, 请参见表 8-33。 |

> **表 8-33.** 过滤器 ID 和值
>
> | Filter ID | Filter Value 字段的描述和定义 |
> |-----------|------------------------------|
> | 0 | 对与 Filter Configuration 寄存器中 Filter Value 字段指定的 HDM 解码器关联的事件进行计数。如果 Filter Configuration 寄存器中的位 n 置位, 则对与 HDM Decoder n 关联的事件进行计数。例如, Filter Value=0Ah 对与 HDM Decoder 1 和 HDM Decoder 3 关联的事件进行计数。 |
> | 1 | 对与 Filter Value 字段中指定的 Channel、Rank 和 Bank Group 以及 Bank 的组合关联的事件进行计数。有关这些术语的定义, 请参见表 8-58。<br>• 位 [7:0]: Bank Number, 使用基于 0 的编码表示。对与此 DDR Bank 关联的事件进行计数。如果设置为 FFh, 则 CPMU 应计数与所有 Bank 关联的事件。<br>• 位 [15:8]: Bank Group, 使用基于 0 的编码表示。对与此 DDR Bank Group 关联的事件进行计数。如果设置为 FFh, 则 CPMU 应计数与所有 Bank Group 关联的事件。<br>• 位 [23:16]: Rank Number, 使用基于 0 的编码表示。对与此 DDR Rank 关联的事件进行计数。如果设置为 FFh, 则 CPMU 应计数与所有 Rank 关联的事件。<br>• 位 [31:24]: Channel Number, 使用基于 0 的编码表示。对与此 DDR Channel 关联的事件进行计数。如果设置为 FFh, 则 CPMU 应计数与所有 Channel 关联的事件。<br>例如, Filter Value=0004 FF00h 对与 Channel 0 中 Rank 4 关联的所有 Bank Group 中的 Bank 0 关联的事件进行计数。 |
> | 7:2 | 保留。每个计数器的 Filter ID 寄存器 2-7 也保留。 |

</td></tr>
</tbody>
</table>

> **Figure 8-72.** Filter Configuration Register layout ｜ 过滤器配置寄存器布局
>
> <img src="figures/chapter_08/page_0607.png" alt="Figure 8-72" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0607.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-2-3"></a>
#### 8.2.7.2.3 Counter Data (Offset: Varies) | 计数器数据 (偏移量: 可变)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The Counter Data register must be accessed as an 8-byte quantity.

| Bit | Attributes | Description |
|-----|------------|-------------|
| N-1:0 | RW | Event Count: The current count value.<br>If the Counters Writable while Frozen bit in the CPMU Capability register is 0, any changes to this register while the counter is Enabled or Frozen leads to undefined results.<br>The value N should be chosen such that the counter takes more than one hour before the counter overflows, regardless of which Event it is counting.<br>Once written, the counter continues to increment from the written value. A freeze operation causes the counter to stop accumulating additional events and to retain its value at the time of freeze. An unfreeze operation allows the counter to resume counting subsequent events. When the counter reaches its maximum value, it automatically wraps around upon the next event and starts counting from 0. This transition is defined as the overflow event. Other than the overflow scenario, the counter value is never decremented.<br>N equals the raw value reported by the Counter Width field in the CPMU Capability register. |
| 63:N | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

Counter Data 寄存器必须作为 8 字节量进行访问。

| 位 | 属性 | 描述 |
|-----|------|------|
| N-1:0 | RW | Event Count: 当前计数值。<br>如果 CPMU Capability 寄存器中的 Counters Writable while Frozen 位为 0, 则在计数器启用或冻结时对此寄存器的任何更改都会导致未定义的结果。<br>应选择 N 值, 使得无论计数器正在计数哪个事件, 计数器溢出前都应超过一个小时。<br>一旦写入, 计数器从写入的值继续递增。冻结操作会使计数器停止累积更多事件, 并在冻结时保留其值。解冻操作允许计数器恢复对后续事件的计数。当计数器达到其最大值时, 它在下一个事件时自动回绕并从 0 开始计数。此转换定义为溢出事件。除溢出场景外, 计数器值永远不会递减。<br>N 等于 CPMU Capability 寄存器中 Counter Width 字段报告的原始值。 |
| 63:N | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-73.** Counter Data Register layout ｜ 计数器数据寄存器布局
>
> <img src="figures/chapter_08/page_0609.png" alt="Figure 8-73" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0609.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-8"></a>
## 8.2.8 CHMU Register Interface | CHMU 寄存器接口

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CXL Hotness Monitoring Unit (CHMU) is an interface that allows software running on CXL hosts to identify the 'hot' memory ranges (i.e., memory ranges with higher access frequency relative to other memory ranges) in CXL memory devices in terms of memory access counts. The CHMU is not expected to be used for cold region tracking and shall not impact device performance.

The CHMU applies to HDM-H devices, HDM-DB devices, MLDs, and Multi-Headed devices. For MH-SLD devices, the CHMU is on a per-head basis whereas for LD-FAM devices, CHMU must be implemented on a per LD-ID basis. A CXL device may implement multiple CHMUs.

The CHMU interface will be used to manage the hardware units that are responsible for counting accesses, including discovering capabilities, setting configuration parameters, checking status, and collecting results.

To configure the hotness threshold, the CHMU management software shall first configure the unit size such that the device could arrange the internal counting structure resources to manage the configured unit size. Then, the device returns the actual counter width in the CHMU Status register(s). Finally, the hotness threshold can be configured depending on the counter width returned by the device.

CHMU counts CXL.mem M2S requests only and does not count UIO Direct Peer-to-peer accesses through CXL.io. CHMU does not count CXL.cache accesses.

CHMU counts accesses on specific DPA granularities called units; unit sizes may range from 256B to 2 GB. The unit size is set by the host software. The CHMU identifies DPA units that have an access frequency that is higher than a configurable threshold. These DPA units are called hot units.

The CHMUs contain a set of counters to count accesses to DPA units. The counter set is implementation specific and counters in the set are not directly accessible via the CHMU interface.

Access counting may be enabled on multiple address ranges with 256-MB granularity. Host software is responsible for setting properly the number of ranges considering the size of the units (e.g., if the unit size is 1 GB, a single 256-MB range should not be configured).

The device counts accesses to DPA units for programmed time intervals called epochs. The device reports the supported minimum and maximum epoch intervals that provide a high level of fidelity for the hotness tracking. Software is expected to program an epoch interval between the minimum and the maximum values. During an epoch, each accessed DPA unit is mapped to a counter within the set according to an implementation-specific mapping function. Examples of mapping function could be direct-mapped, set-associative, hash-function, etc. If the counter is free, it is allocated to the DPA unit and initialized to 1. If the counter is already allocated to the same DPA unit, the counter is incremented. If the counter is allocated to another DPA unit, the access might be not counted. All counters are freed at the end of their epochs.

If the counter related to a specific unit achieves the programmed hotness threshold during an epoch, the unit is considered hot, and is then reported to software. To report hot units to software, CHMU supports a circular structure called the CHMU Hotlist. The Hotlist is accessible through the CHMU's MMIO address space. There is a single Hotlist per CHMU instance for all the address ranges that can be configured on that CHMU. Each CHMU Hotlist entry is a 64-bit structure that contains a DPA unit address, called Unit ID, and its counter value. After the unit size is configured by the software, the remaining bits in the 64-bit entry can be allocated for the counters. Therefore, the hotness threshold can be configured only after setting the unit size. The size of the counters is retrieved through the CHMU Status register.

The CHMU reports new hot units at the Hotlist's Tail pointer and increments the Tail. The software is expected to read the Hotlist entries at the Head pointer and increment the Head. When the Head and the Tail are equal, the Hotlist is considered empty. When the Tail is logically 1 behind the Head, the Hotlist is considered full. The Hotlist can be cleared by setting the Head register to be equal to the Tail register.

Two modes are defined for reporting hot units into the CHMU Hotlist: Epoch-based reporting mode and Always-on reporting mode. Software is responsible for enabling one of the two modes.

When Epoch-based reporting mode is enabled, hot units are reported in the CHMU Hotlist at the end of their counter's current epoch. Even if the counter reaches the hotness threshold before the epoch ends, the counter continues counting until the epoch ends. Consequently, the counter values in the CHMU Hotlist entries will contain the number of hot unit accesses within the epoch. The counters within the counting structure will be freed at the end of their respective epochs.

When Always-on reporting mode is enabled, after the counters achieve the hotness threshold, their corresponding Unit ID is immediately reported in the CHMU Hotlist and becomes visible to the software through the CHMU Hotlist-related registers. The hot unit-related counters are freed when the counters are reported in the Hotlist. The counters within the counting structure will be freed at the end of their respective epochs.

CHMU supports a down-sampling factor for the incoming M2S requests that allows sampling at a configurable rate, or at a rate that is controlled by the device. The down-sampling factor can be either selectable by software (if supported by the device) or can be selected by the device.

The CHMU interface supports MSI/MSI-X interrupts to alert when the:
- CHMU Hotlist overflows
- CHMU Hotlist crosses a level of fullness

If the CHMU Hotlist overflows, the new hot units may be discarded or retained as 'outstanding' hot units that will be reported when space is available in the CHMU Hotlist. The ability to report these outstanding hot units is indicated in the device capabilities. If the CHMU is disabled, any outstanding hot units will be dropped and never added to the CHMU Hotlist.

</td><td style="background-color:#e8e8e8">

CXL 热度监视单元 (CHMU, CXL Hotness Monitoring Unit) 是一个接口, 允许在 CXL 主机上运行的软件根据内存访问计数来识别 CXL 内存设备中的"热"内存范围 (即相对于其他内存范围具有更高访问频率的内存范围)。CHMU 不应用于冷区域跟踪, 且不应影响设备性能。

CHMU 适用于 HDM-H 设备、HDM-DB 设备、MLD 和多头设备。对于 MH-SLD 设备, CHMU 是按头 (per-head) 的; 而对于 LD-FAM 设备, CHMU 必须按 LD-ID 实现。CXL 设备可以实现多个 CHMU。

CHMU 接口将用于管理负责对访问进行计数的硬件单元, 包括发现能力、设置配置参数、检查状态和收集结果。

要配置热度阈值, CHMU 管理软件应首先配置单元大小, 以便设备可以安排内部计数结构资源以管理所配置的单元大小。然后, 设备在 CHMU Status 寄存器中返回实际的计数器宽度。最后, 可以根据设备返回的计数器宽度配置热度阈值。

CHMU 仅对 CXL.mem M2S 请求进行计数, 不对通过 CXL.io 的 UIO Direct Peer-to-peer 访问进行计数。CHMU 不对 CXL.cache 访问进行计数。

CHMU 在称为单元的特定 DPA 粒度上对访问进行计数; 单元大小范围可从 256B 到 2 GB。单元大小由主机软件设置。CHMU 标识访问频率高于可配置阈值的 DPA 单元。这些 DPA 单元称为热单元。

CHMU 包含一组计数器, 用于对 DPA 单元的访问进行计数。计数器集是特定于实现的, 集中的计数器不能通过 CHMU 接口直接访问。

访问计数可以在以 256-MB 粒度的多个地址范围内启用。主机软件负责根据单元的大小正确设置范围数量 (例如, 如果单元大小为 1 GB, 则不应配置单个 256-MB 范围)。

设备对称为 epoch 的编程时间间隔内的 DPA 单元访问进行计数。设备报告支持的最小和最大 epoch 间隔, 这些间隔为热度跟踪提供高保真度。软件应在最小值和最大值之间编程 epoch 间隔。在 epoch 期间, 每个被访问的 DPA 单元根据特定于实现的映射函数映射到集中的一个计数器。映射函数的示例可以是直接映射、组相联、哈希函数等。如果计数器空闲, 则将其分配给 DPA 单元并初始化为 1。如果计数器已分配给同一 DPA 单元, 则计数器递增。如果计数器分配给另一个 DPA 单元, 则访问可能不会被计数。所有计数器在其 epoch 结束时被释放。

如果与特定单元相关的计数器在 epoch 期间达到编程的热度阈值, 则该单元被视为热单元, 然后报告给软件。为了向软件报告热单元, CHMU 支持称为 CHMU Hotlist 的循环结构。Hotlist 可通过 CHMU 的 MMIO 地址空间访问。对于可在该 CHMU 上配置的所有地址范围, 每个 CHMU 实例都有一个 Hotlist。每个 CHMU Hotlist 条目都是一个 64 位结构, 其中包含 DPA 单元地址 (称为 Unit ID) 及其计数器值。软件配置单元大小后, 64 位条目中的剩余位可分配给计数器。因此, 只能在设置单元大小后配置热度阈值。计数器的大小通过 CHMU Status 寄存器检索。

CHMU 在 Hotlist 的 Tail 指针处报告新的热单元并递增 Tail。软件应在 Head 指针处读取 Hotlist 条目并递增 Head。当 Head 和 Tail 相等时, Hotlist 被视为空。当 Tail 在逻辑上比 Head 落后 1 时, Hotlist 视为已满。可以通过将 Head 寄存器设置为等于 Tail 寄存器来清除 Hotlist。

CHMU Hotlist 报告热单元有两种模式: 基于 epoch 的报告模式和始终在线的报告模式。软件负责启用这两种模式之一。

当启用基于 epoch 的报告模式时, 热单元将在其计数器当前 epoch 结束时在 CHMU Hotlist 中报告。即使计数器在 epoch 结束之前达到热度阈值, 计数器也会继续计数直到 epoch 结束。因此, CHMU Hotlist 条目中的计数器值将包含 epoch 内的热单元访问次数。计数结构内的计数器将在其各自 epoch 结束时被释放。

当启用始终在线的报告模式时, 在计数器达到热度阈值后, 它们相应的 Unit ID 立即在 CHMU Hotlist 中报告, 并通过 CHMU Hotlist 相关寄存器对软件可见。热单元相关的计数器在 Hotlist 中报告时被释放。计数结构内的计数器将在其各自 epoch 结束时被释放。

CHMU 支持对传入的 M2S 请求进行下采样, 允许以可配置的速率或由设备控制的速率进行采样。下采样因子可以由软件选择 (如果设备支持) 或由设备选择。

CHMU 接口支持 MSI/MSI-X 中断, 以在以下情况下发出警报:
- CHMU Hotlist 溢出
- CHMU Hotlist 跨越一定的填充水平

如果 CHMU Hotlist 溢出, 新的热单元可能会被丢弃或保留为"未完成"的热单元, 这些单元将在 CHMU Hotlist 中有可用空间时报告。报告这些未完成热单元的能力在设备能力中指示。如果 CHMU 处于禁用状态, 则任何未完成的热单元都将被丢弃, 永远不会添加到 CHMU Hotlist 中。

</td></tr>
</tbody>
</table>

> **Figure 8-74.** CHMU Register Interface Block Diagram ｜ CHMU 寄存器接口框图
>
> <img src="figures/chapter_08/page_0609.png" alt="Figure 8-74" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0609.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-8-1"></a>
### 8.2.8.1 CHMU Common Capability Register (Offset 00h) | CHMU 公共能力寄存器 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

Each CHMU implements a set of CHMU-scoped registers within a register block. Multiple CHMU register block identifiers are permitted. In this version of the specification, within a CHMU register block, the device can support up to eight CHMU instances, and a single instance is composed of CHMU Capability, CHMU Configuration, CHMU Status, CHMU Hotlist Head, CHMU Hotlist Tail, CHMU Range Configuration Bitmap, and CHMU Hotlist Entry registers. The CHMU Configuration register may be configured only when the CHMU is disabled. When the CHMU is enabled, all the Configuration registers are locked (i.e., Read Only) except the Control field in the CHMU Configuration register. The CHMU Configuration register remains Read Only until the CHMU is disabled again.

The CHMU Common Capability register must be accessed as an 8-byte quantity.

> **Table 8-34.** CHMU Register Layout (Version=1)
>
> | Byte Offset | Length in Bytes | Register Name |
> |-------------|-----------------|---------------|
> | 00h | 16 | CHMU Common Capabilities |
> | 10h | 64 | CHMU Capability [0] |
> | 50h | 32 | CHMU Configuration [0] |
> | 70h | 8 | CHMU Status [0] |
> | 78h | 2 | CHMU Hotlist Head [0] |
> | 7Ah | 2 | CHMU Hotlist Tail [0] |
> | 7Ch | 4 | Reserved |
> | 10h+R0 | 1h | CHMU Range Configuration Bitmap [0]¹ |
> | 10h+H0 | 2- R0 | CHMU Hotlist [0]² |
> | 10h+L4 | M0*8 | CHMU Hotlist [0]³ |
> | 10h+L4 | 64 | CHMU Capability [1]⁴ |
> | 50h+L | 32 | CHMU Configuration [1] |
> | 70h+L | 8 | CHMU Status [1] |
> | 78h+L | 2 | CHMU Hotlist Head [1] |
> | 7Ah+L | 2 | CHMU Hotlist Tail [1] |
> | 7Ch+L | 4 | Reserved |
> | 10h+L+R1 | H1- R1 | CHMU Range Configuration Bitmap [1] |
> | 10h+L+H1 | M1*8 | CHMU Hotlist [1] |
> | ... | ... | ... |
> | 10h+L*7d | 64 | CHMU Capability [7] |
> | 50h+L*7d | 32 | CHMU Configuration [7] |
> | 70h+L*7d | 8 | CHMU Status [7] |
> | 78h+L*7d | 2 | CHMU Hotlist Head [7] |
> | 7Ah+L*7d | 2 | CHMU Hotlist Tail [7] |
> | 7Ch+L*7d | 4 | Reserved |
> | 10h+L*7d+R7 | H7-R7 | CHMU Range Configuration Bitmap [7] |
> | 10h+L*7d+H7 | M7*8 | CHMU Hotlist [7] |
>
> ¹ Value Ri is reported in the CHMU Range Configuration Bitmap register offset of the CHMU Capability register.
> ² Value Hi is reported in the CHMU Hotlist Register Offset of the CHMU Capability register.
> ³ Value Mi depends on the size of the hotlist in the CHMU instance.
> ⁴ Value L corresponds to the value of the CHMU Instance Length field in the CHMU Common Capabilities register.

> **Table 8-35.** CHMU Common Capability Register (Offset 00h)
>
> | Bit | Attributes | Description |
> |-----|------------|-------------|
> | 3:0 | HwInit | Version: Set to 1. The version is incremented whenever the CHMU register structure is extended to add more functionality. Backward compatibility shall be maintained during this process. For all values of n, version n+1 may extend version n by replacing fields that are marked as Reserved in version n or appending new registers but must not redefine the meaning of existing fields. Software that was written for a lower version may continue to operate on CHMU registers with a higher version but will not be able to take advantage of new functionality. Each field in the CHMU register structure is assumed to be introduced in version 1 of that structure unless specified otherwise in the field's definition within this specification. |
> | 7:4 | RsvdP | Reserved |
> | 15:8 | HwInit | Number of Supported CHMU Instances: Number of CHMU instances supported within the CHMU register block. In this version of the specification, the value of this field shall be less than or equal to 8. |
> | 63:16 | RsvdP | Reserved |
> | 79:64 | HwInit | CHMU Instance Length: Length in bytes of a single CHMU instance. |
> | 127:80 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

每个 CHMU 在寄存器块内实现一组 CHMU 作用域的寄存器。允许多个 CHMU 寄存器块标识符。在规范的此版本中, 在 CHMU 寄存器块内, 设备最多可支持八个 CHMU 实例, 单个实例由 CHMU Capability、CHMU Configuration、CHMU Status、CHMU Hotlist Head、CHMU Hotlist Tail、CHMU Range Configuration Bitmap 和 CHMU Hotlist Entry 寄存器组成。仅当 CHMU 处于禁用状态时, CHMU Configuration 寄存器才可配置。当 CHMU 启用时, 除 CHMU Configuration 寄存器中的 Control 字段外, 所有 Configuration 寄存器都被锁定 (即只读)。CHMU Configuration 寄存器保持只读状态, 直到 CHMU 再次被禁用。

CHMU Common Capability 寄存器必须作为 8 字节量进行访问。

> **表 8-34.** CHMU 寄存器布局 (Version=1)
>
> | 字节偏移量 | 字节长度 | 寄存器名称 |
> |------------|----------|------------|
> | 00h | 16 | CHMU Common Capabilities |
> | 10h | 64 | CHMU Capability [0] |
> | 50h | 32 | CHMU Configuration [0] |
> | 70h | 8 | CHMU Status [0] |
> | 78h | 2 | CHMU Hotlist Head [0] |
> | 7Ah | 2 | CHMU Hotlist Tail [0] |
> | 7Ch | 4 | 保留 |
> | 10h+R0 | 1h | CHMU Range Configuration Bitmap [0]¹ |
> | 10h+H0 | 2- R0 | CHMU Hotlist [0]² |
> | 10h+L⁴ | M0*8 | CHMU Hotlist [0]³ |
> | 10h+L⁴ | 64 | CHMU Capability [1]⁴ |
> | 50h+L | 32 | CHMU Configuration [1] |
> | 70h+L | 8 | CHMU Status [1] |
> | 78h+L | 2 | CHMU Hotlist Head [1] |
> | 7Ah+L | 2 | CHMU Hotlist Tail [1] |
> | 7Ch+L | 4 | 保留 |
> | 10h+L+R1 | H1- R1 | CHMU Range Configuration Bitmap [1] |
> | 10h+L+H1 | M1*8 | CHMU Hotlist [1] |
> | ... | ... | ... |
> | 10h+L*7d | 64 | CHMU Capability [7] |
> | 50h+L*7d | 32 | CHMU Configuration [7] |
> | 70h+L*7d | 8 | CHMU Status [7] |
> | 78h+L*7d | 2 | CHMU Hotlist Head [7] |
> | 7Ah+L*7d | 2 | CHMU Hotlist Tail [7] |
> | 7Ch+L*7d | 4 | 保留 |
> | 10h+L*7d+R7 | H7-R7 | CHMU Range Configuration Bitmap [7] |
> | 10h+L*7d+H7 | M7*8 | CHMU Hotlist [7] |
>
> ¹ 值 Ri 在 CHMU Capability 寄存器的 CHMU Range Configuration Bitmap 寄存器偏移量中报告。
> ² 值 Hi 在 CHMU Capability 寄存器的 CHMU Hotlist Register Offset 中报告。
> ³ 值 Mi 取决于 CHMU 实例中 hotlist 的大小。
> ⁴ 值 L 对应于 CHMU Common Capabilities 寄存器中 CHMU Instance Length 字段的值。

> **表 8-35.** CHMU 公共能力寄存器 (偏移量 00h)
>
> | 位 | 属性 | 描述 |
> |-----|------|------|
> | 3:0 | HwInit | Version: 设置为 1。每当扩展 CHMU 寄存器结构以添加更多功能时, 版本都会递增。在此过程中应保持向后兼容性。对于 n 的所有值, 版本 n+1 可以通过替换版本 n 中标记为保留的字段或追加新寄存器来扩展版本 n, 但不得重新定义现有字段的含义。为较低版本编写的软件可以继续在较高版本的 CHMU 寄存器上运行, 但将无法利用新功能。除非在本规范的字段定义中另有规定, 否则 CHMU 寄存器结构中的每个字段都假定在该结构的版本 1 中引入。 |
> | 7:4 | RsvdP | 保留 |
> | 15:8 | HwInit | Number of Supported CHMU Instances: CHMU 寄存器块内支持的 CHMU 实例数。在规范的此版本中, 此字段的值应小于或等于 8。 |
> | 63:16 | RsvdP | 保留 |
> | 79:64 | HwInit | CHMU Instance Length: 单个 CHMU 实例的字节长度。 |
> | 127:80 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-75.** CHMU Common Capability Register layout ｜ CHMU 公共能力寄存器布局
>
> <img src="figures/chapter_08/page_0611.png" alt="Figure 8-75" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0611.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-8-2"></a>
### 8.2.8.2 CHMU Capability Register (Offset 10h + CHMU Instance Length * i¹) | CHMU 能力寄存器 (偏移量 10h + CHMU Instance Length * i¹)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CHMU Capability register must be accessed as an 8-byte quantity.

¹ i is the index of the CHMU instance. In this version of the specification, the device can support up to 8 CHMU instances.

> **Table 8-36.** CHMU Capability Register (Sheet 1 of 3)
>
> | Bit | Attributes | Description |
> |-----|------------|-------------|
> | 3:0 | HwInit | Interrupt Message Number: If Interrupt on Hotlist Overflow Support=1, this field indicates which MSI/MSI-X vector is used for the interrupt message that is generated in association with this CHMU instance.<br>For MSI, the value in this field indicates the offset between the base Message Data and the interrupt message that is generated. Hardware is required to update this field so that it is correct if the number of MSI Messages assigned to the Function changes when software writes to the Multiple Message Enable field in the Message Control register for MSI. For MSI-X, the value in this field indicates which MSI-X Table entry is used to generate the interrupt message. The entry shall be one of the first 16 entries, regardless of whether the Function implements more than 16 entries. The value in this field shall be within the range configured by system software to the device. For a given MSI-X implementation, the entry shall remain constant.<br>If both MSI and MSI-X are implemented, they are permitted to use different vectors, though software is permitted to enable only one mechanism at a time. If MSI-X is enabled, the value in this field shall indicate the vector for MSI-X. If MSI is enabled or neither is enabled, the value in this field indicates the vector for MSI. If software enables both MSI and MSI-X at the same time, the value in this field is undefined.<br>It is recommended that the component allocate a distinct Interrupt Message Number to each CHMU instance. |
> | 4 | HwInit | Interrupt on Hotlist Overflow Support:<br>• 0 = The CHMU does not support generation of interrupts upon hotlist overflow.<br>• 1 = The CHMU supports generation of interrupts upon hotlist overflow. Interrupt generation is controlled by the Interrupt on Hotlist Overflow bit in the CHMU Configuration register. The Interrupt Message Number is reported in the Interrupt Message Number field of this register. |
> | 5 | HwInit | Interrupt on Hotlist Levels Crossing Support:<br>• 0 = CHMU does not support generation of interrupts upon hotlist levels crossing.<br>• 1 = CHMU supports generation of interrupts upon hotlist levels crossing. Interrupt generation is controlled by the Interrupt on Hotlist Levels Crossing bit in the CHMU Configuration register. The Interrupt Message Number is reported in the Interrupt Message Number field of this register. |
> | 7:6 | HwInit | Epoch Type:<br>• 00b = Global. All counters start and end their epoch simultaneously.<br>• 01b = Per counter. Each counter starts and ends their epoch independently. The counter starts when it is allocated.<br>• All other encodings are Reserved. |
> | 15:8 | HwInit | Tracked M2S Requests: CXL.mem requests that can be tracked by the device. The following values are defined:<br>• Bit[8]: Non-TEE read only (MemRd, MemRdData, MemSpecRd, MemInv)<br>• Bit[9]: Non-TEE write only (MemWr, MemWrPtl)<br>• Bit[10]: Non-TEE read and non-TEE write (MemRd, MemRdData, MemSpecRd, MemInv, MemWr, MemWrPtl)<br>• Bit[11]: Non-TEE and TEE read (MemRd, MemRdData, MemSpecRd, MemInv, MemRdTEE, MemRdDataTEE, MemSpecRdTEE)<br>• Bit[12]: Non-TEE and TEE write (MemWr, MemWrPtl, MemWrTEE, MemWrPtlTEE)<br>• Bit[13]: Non-TEE read, TEE read, non-TEE write, TEE write<br>• Bits[15:14]: Reserved |
> | 31:16 | HwInit | Max Epoch Length: Maximum epoch length that the device supports.<br>• Bits[19:16]: These bits specify the time scale.<br>— 1h = 100 us<br>— 2h = 1 ms<br>— 3h = 10 ms<br>— 4h = 100 ms<br>— 5h = 1 s<br>— All other encodings are Reserved<br>• Bits[31:20]: These bits specify the maximum epoch length, using the time scale indicated in bits[19:16]. Max value is 4095. A value of 0 is not permitted. |
> | 47:32 | HwInit | Min Epoch Length: Minimum epoch length that the device supports.<br>• Bits[35:32]: These bits specify the time scale.<br>— 1h = 100 us<br>— 2h = 1 ms<br>— 3h = 10 ms<br>— 4h = 100 ms<br>— 5h = 1 s<br>— All other encodings are Reserved<br>• Bits[47:36]: These bits specify the minimum epoch length, using the time scale indicated in bits[35:32]. Max value is 4095. A value of 0 is not permitted. |
> | 63:48 | HwInit | Hotlist Size: Maximum number of hotlist entries. The minimum value to be supported is 64. Max value is 65,535. |
> | 95:64 | HwInit | Supported Unit Sizes: Each bit corresponds to the granularity of memory for which accesses are counted separately. Supported values are expressed as a power of 2 and range from 256B to 2 GB. It is recommended to support at least one unit size of 2 MB or smaller granularity. The parameter is represented by a bitmap in which the unit size doubles with each bit increment.<br>• Bit[64]: 256 B<br>• Bit[65]: 512 B<br>• Bit[66]: 1 KB<br>• Bit[67]: 2 KB<br>• Bit[68]: 4 KB<br>• ...<br>• Bit[86]: 1 GB<br>• Bit[87]: 2 GB<br>• Bits[95:88]: Reserved |
> | 111:96 | HwInit | Supported Down-sampling Factor: The device can be configured to track one M2S request over one of the values encoded in this field.<br>• Bit[96]: 1 (the device can sustain the full request rate)<br>• Bit[97]: 2<br>• Bit[98]: 4<br>• Bit[99]: 8<br>• Bit[100]: 16<br>• Bit[101]: 32<br>• ...<br>• Bit[111]: 32,768 |
> | 127:112 | HwInit | Capability Flags: Features supported for hotness tracking.<br>• Bit[112]: Epoch-based reporting mode: if set, the device updates the list of hot units in the hotlist at the end of an epoch.<br>• Bit[113]: Always-on Reporting Mode: When set to 1, the device pushes entries into the hotlist as soon as the related unit achieves or exceeds the hotness threshold.<br>• Bit[114]: Randomized Down-sampling: When set to 1, the device supports implementation-specific randomization for selecting accesses to perform down-sampling.<br>• Bit[115]: Address Overlap: When set to 1, the CHMU can overlap address ranges that are covered by other CHMU instances within the same register block.<br>• Bit[116]: Postponed Outstanding Hot Units Insertion in the CHMU Hotlist on Overflow: When set to 1, if the CHMU hotlist overflows, outstanding hot units identified when the hotlist is in Overflow state become visible when one or more CHMU Hotlist entries are freed. The hot units detected in Overflow state will be visible within 10 ms if the number of entries that are freed is sufficient.<br>• Bits[127:117]: Reserved |
> | 191:128 | HwInit | CHMU Range Configuration Bitmap Register Offset: Offset from the first byte of the CHMU Capability register in which the CHMU Range Configuration Bitmap starts. |
> | 255:192 | HwInit | CHMU Hotlist Register Offset. Offset from the first byte of the CHMU Capability register in which the CHMU Hotlist starts. |
> | 511:256 | RsvdP | Reserved |

</td><td style="background-color:#e8e8e8">

CHMU Capability 寄存器必须作为 8 字节量进行访问。

¹ i 是 CHMU 实例的索引。在规范的此版本中, 设备最多可支持 8 个 CHMU 实例。

> **表 8-36.** CHMU 能力寄存器 (第 1 页, 共 3 页)
>
> | 位 | 属性 | 描述 |
> |-----|------|------|
> | 3:0 | HwInit | Interrupt Message Number: 如果 Interrupt on Hotlist Overflow Support=1, 则此字段指示与此 CHMU 实例关联生成的中断消息所使用的 MSI/MSI-X 向量。<br>对于 MSI, 此字段中的值表示基本消息数据与生成的中断消息之间的偏移量。当软件写入 MSI 消息控制寄存器的 Multiple Message Enable 字段而导致分配给该功能的消息数发生变化时, 硬件需要更新此字段以使其正确。对于 MSI-X, 此字段中的值指示用于生成中断消息的 MSI-X 表条目。即使该功能实现了 16 个以上条目, 该条目也必须是前 16 个条目之一。此字段中的值应处于系统软件配置给设备的范围内。对于给定的 MSI-X 实现, 该条目应保持不变。<br>如果同时实现了 MSI 和 MSI-X, 则它们允许使用不同的向量, 但软件一次只允许启用一种机制。如果启用了 MSI-X, 则此字段中的值应指示 MSI-X 的向量。如果启用了 MSI 或两者都未启用, 则此字段中的值指示 MSI 的向量。如果软件同时启用 MSI 和 MSI-X, 则此字段中的值未定义。<br>建议组件为每个 CHMU 实例分配不同的 Interrupt Message Number。 |
> | 4 | HwInit | Interrupt on Hotlist Overflow Support:<br>• 0 = CHMU 不支持在 hotlist 溢出时生成中断。<br>• 1 = CHMU 支持在 hotlist 溢出时生成中断。中断生成由 CHMU Configuration 寄存器中的 Interrupt on Hotlist Overflow 位控制。Interrupt Message Number 在本寄存器的 Interrupt Message Number 字段中报告。 |
> | 5 | HwInit | Interrupt on Hotlist Levels Crossing Support:<br>• 0 = CHMU 不支持在 hotlist 水平跨越时生成中断。<br>• 1 = CHMU 支持在 hotlist 水平跨越时生成中断。中断生成由 CHMU Configuration 寄存器中的 Interrupt on Hotlist Levels Crossing 位控制。Interrupt Message Number 在本寄存器的 Interrupt Message Number 字段中报告。 |
> | 7:6 | HwInit | Epoch Type:<br>• 00b = 全局。所有计数器同时开始和结束其 epoch。<br>• 01b = 每个计数器。每个计数器独立开始和结束其 epoch。计数器在分配时启动。<br>• 所有其他编码保留。 |
> | 15:8 | HwInit | Tracked M2S Requests: 设备可跟踪的 CXL.mem 请求。定义以下值:<br>• 位 [8]: 仅 Non-TEE 读 (MemRd, MemRdData, MemSpecRd, MemInv)<br>• 位 [9]: 仅 Non-TEE 写 (MemWr, MemWrPtl)<br>• 位 [10]: Non-TEE 读和 Non-TEE 写 (MemRd, MemRdData, MemSpecRd, MemInv, MemWr, MemWrPtl)<br>• 位 [11]: Non-TEE 和 TEE 读 (MemRd, MemRdData, MemSpecRd, MemInv, MemRdTEE, MemRdDataTEE, MemSpecRdTEE)<br>• 位 [12]: Non-TEE 和 TEE 写 (MemWr, MemWrPtl, MemWrTEE, MemWrPtlTEE)<br>• 位 [13]: Non-TEE 读, TEE 读, Non-TEE 写, TEE 写<br>• 位 [15:14]: 保留 |
> | 31:16 | HwInit | Max Epoch Length: 设备支持的最大 epoch 长度。<br>• 位 [19:16]: 这些位指定时间刻度。<br>— 1h = 100 us<br>— 2h = 1 ms<br>— 3h = 10 ms<br>— 4h = 100 ms<br>— 5h = 1 s<br>— 所有其他编码保留<br>• 位 [31:20]: 这些位使用位 [19:16] 中指示的时间刻度指定最大 epoch 长度。最大值为 4095。不允许值为 0。 |
> | 47:32 | HwInit | Min Epoch Length: 设备支持的最小 epoch 长度。<br>• 位 [35:32]: 这些位指定时间刻度。<br>— 1h = 100 us<br>— 2h = 1 ms<br>— 3h = 10 ms<br>— 4h = 100 ms<br>— 5h = 1 s<br>— 所有其他编码保留<br>• 位 [47:36]: 这些位使用位 [35:32] 中指示的时间刻度指定最小 epoch 长度。最大值为 4095。不允许值为 0。 |
> | 63:48 | HwInit | Hotlist Size: hotlist 条目的最大数量。要支持的最小值为 64。最大值为 65,535。 |
> | 95:64 | HwInit | Supported Unit Sizes: 每个位对应于单独对其访问进行计数的内存粒度。支持的值表示为 2 的幂, 范围从 256B 到 2 GB。建议支持至少 2 MB 或更小粒度的一个单元大小。该参数由位图表示, 其中单元大小随每个位增量翻倍。<br>• 位 [64]: 256 B<br>• 位 [65]: 512 B<br>• 位 [66]: 1 KB<br>• 位 [67]: 2 KB<br>• 位 [68]: 4 KB<br>• ...<br>• 位 [86]: 1 GB<br>• 位 [87]: 2 GB<br>• 位 [95:88]: 保留 |
> | 111:96 | HwInit | Supported Down-sampling Factor: 设备可配置为通过此字段中编码的值之一跟踪一个 M2S 请求。<br>• 位 [96]: 1 (设备可以维持完整请求速率)<br>• 位 [97]: 2<br>• 位 [98]: 4<br>• 位 [99]: 8<br>• 位 [100]: 16<br>• 位 [101]: 32<br>• ...<br>• 位 [111]: 32,768 |
> | 127:112 | HwInit | Capability Flags: 热度跟踪支持的功能。<br>• 位 [112]: 基于 epoch 的报告模式: 置位时, 设备在 epoch 结束时更新 hotlist 中的热单元列表。<br>• 位 [113]: 始终在线报告模式: 设置为 1 时, 只要相关单元达到或超过热度阈值, 设备就会立即将条目推入 hotlist。<br>• 位 [114]: 随机下采样: 设置为 1 时, 设备支持用于选择访问执行下采样的特定于实现的随机化。<br>• 位 [115]: 地址重叠: 设置为 1 时, CHMU 可以重叠同一寄存器块内其他 CHMU 实例覆盖的地址范围。<br>• 位 [116]: 在溢出时将未完成的出色热单元插入到 CHMU Hotlist 中: 设置为 1 时, 如果 CHMU hotlist 溢出, 则在 hotlist 处于 Overflow 状态时识别的未完成的出色热单元在一个或多个 CHMU Hotlist 条目被释放时变为可见。如果释放的条目数量充足, 则在 Overflow 状态中检测到的热单元将在 10 毫秒内可见。<br>• 位 [127:117]: 保留 |
> | 191:128 | HwInit | CHMU Range Configuration Bitmap Register Offset: 从 CHMU Capability 寄存器的第一个字节开始的偏移量, CHMU Range Configuration Bitmap 在此偏移量处开始。 |
> | 255:192 | HwInit | CHMU Hotlist Register Offset: 从 CHMU Capability 寄存器的第一个字节开始的偏移量, CHMU Hotlist 在此偏移量处开始。 |
> | 511:256 | RsvdP | 保留 |

</td></tr>
</tbody>
</table>

> **Figure 8-76.** CHMU Capability Register layout ｜ CHMU 能力寄存器布局
>
> <img src="figures/chapter_08/page_0612.png" alt="Figure 8-76" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0612.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-8-3"></a>
### 8.2.8.3 CHMU Configuration [i] (Offset 50h + CHMU Instance Length * i) | CHMU 配置 [i] (偏移量 50h + CHMU Instance Length * i)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CHMU Configuration register must be accessed as an 8-byte quantity.

> **Table 8-37.** CHMU Configuration Register (Sheet 1 of 2)
>
> | Bit | Attributes | Description |
> |-----|------------|-------------|
> | 7:0 | RW | M2S Requests to Track: CXL.mem requests to be tracked by the device. The following values are defined:<br>• 01h = Non-TEE read only (MemRd, MemRdData, MemSpecRd, MemInv)<br>• 02h = Non-TEE write only (MemWr, MemWrPtl)<br>• 03h = Non-TEE read and non-TEE write (MemRd, MemRdData, MemSpecRd, MemInv, MemWr, MemWrPtl)<br>• 04h = Non-TEE and TEE read (MemRd, MemRdData, MemSpecRd, MemInv, MemRdTEE, MemRdDataTEE, MemSpecRdTEE)<br>• 05h = Non-TEE and TEE write (MemWr, MemWrPtl, MemWrTEE, MemWrPtlTEE)<br>• 06h = Non-TEE read, TEE read, non-TEE write, TEE write<br>• All other encodings are Reserved |
> | 15:8 | RW | Flags: Features supported for hotness tracking.<br>• Bit[8]: Randomized Down-sampling: When set to 1, the device uses implementation-specific randomization for selecting accesses to perform down-sampling.<br>• Bit[9]: Interrupt on Hotlist Overflow: When set to 1, the device generates an interrupt when the hotlist overflows. The Interrupt Message Number is reported in the Interrupt Message Number field in the CHMU Capability registers. This bit can be set to 1 if the Interrupt on Hotlist Overflow Support bit in the CHMU Capability register is set to 1; otherwise, the bit is permitted to be hardwired to 0.<br>• Bit[10]: Interrupt on Hotlist Levels Crossing: When set to 1, the device generates an interrupt when the hotlist achieves a number of host-configured elements through the Hotness Notification Threshold parameter. The Interrupt Message Number is reported in the Interrupt Message Number field in the CHMU Capability registers. This bit can be set to 1 if the Interrupt on Hotlist Levels Crossing Support bit in the CHMU Capability register is set; otherwise, the bit is permitted to be hardwired to 0.<br>• Bits[15:11]: Reserved. |
> | 31:16 | RW | Control: This field is used to require performing operations on the Hotness Monitoring Unit<br>• Bit[16]: Enable Hotness Monitoring Unit: This bit is set to 1 to enable the Hotness Monitoring Unit, and is cleared to 0 to disable the CHMU. CHMU enablement and/or disablement completion status can be retrieved from the CHMU Status register.<br>• Bit[17]: Reset Counters: This bit is set to 1 to clear the counters in the Hotness Monitoring Unit. The completion of reset counter operation can be established by polling the Operation in Progress field in the CHMU Status register. When the device completes clearing of the counters, this bit returns to a value of 0. The configuration is not affected.<br>• Bits[31:18]: Reserved. |

</td><td style="background-color:#e8e8e8">

CHMU Configuration 寄存器必须作为 8 字节量进行访问。

> **表 8-37.** CHMU 配置寄存器 (第 1 页, 共 2 页)
>
> | 位 | 属性 | 描述 |
> |-----|------|------|
> | 7:0 | RW | M2S Requests to Track: 设备要跟踪的 CXL.mem 请求。定义以下值:<br>• 01h = 仅 Non-TEE 读 (MemRd, MemRdData, MemSpecRd, MemInv)<br>• 02h = 仅 Non-TEE 写 (MemWr, MemWrPtl)<br>• 03h = Non-TEE 读和 Non-TEE 写 (MemRd, MemRdData, MemSpecRd, MemInv, MemWr, MemWrPtl)<br>• 04h = Non-TEE 和 TEE 读 (MemRd, MemRdData, MemSpecRd, MemInv, MemRdTEE, MemRdDataTEE, MemSpecRdTEE)<br>• 05h = Non-TEE 和 TEE 写 (MemWr, MemWrPtl, MemWrTEE, MemWrPtlTEE)<br>• 06h = Non-TEE 读, TEE 读, Non-TEE 写, TEE 写<br>• 所有其他编码保留 |
> | 15:8 | RW | Flags: 热度跟踪支持的功能。<br>• 位 [8]: Randomized Down-sampling: 设置为 1 时, 设备使用特定于实现的随机化来选择要执行下采样的访问。<br>• 位 [9]: Interrupt on Hotlist Overflow: 设置为 1 时, 设备在 hotlist 溢出时生成中断。Interrupt Message Number 在 CHMU Capability 寄存器的 Interrupt Message Number 字段中报告。如果 CHMU Capability 寄存器中的 Interrupt on Hotlist Overflow Support 位置 1, 则此位可设置为 1; 否则, 允许硬连线为 0。<br>• 位 [10]: Interrupt on Hotlist Levels Crossing: 设置为 1 时, 当 hotlist 通过 Hotness Notification Threshold 参数达到主机配置的元素数量时, 设备生成中断。Interrupt Message Number 在 CHMU Capability 寄存器的 Interrupt Message Number 字段中报告。如果 CHMU Capability 寄存器中的 Interrupt on Hotlist Levels Crossing Support 位置位, 则此位可设置为 1; 否则, 允许硬连线为 0。<br>• 位 [15:11]: 保留。 |
> | 31:16 | RW | Control: 此字段用于请求对 Hotness Monitoring Unit 执行操作<br>• 位 [16]: Enable Hotness Monitoring Unit: 该位设置为 1 以启用 Hotness Monitoring Unit, 清零为 0 以禁用 CHMU。CHMU 启用和/或禁用完成状态可从 CHMU Status 寄存器检索。<br>• 位 [17]: Reset Counters: 该位设置为 1 以清除 Hotness Monitoring Unit 中的计数器。复位计数器操作的完成可以通过轮询 CHMU Status 寄存器中的 Operation in Progress 字段来建立。当设备完成计数器清除时, 该位返回值 0。配置不受影响。<br>• 位 [31:18]: 保留。 |

</td></tr>
</tbody>
</table>

> **Figure 8-77.** CHMU Configuration Register layout ｜ CHMU 配置寄存器布局
>
> <img src="figures/chapter_08/page_0615.png" alt="Figure 8-77" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0615.png)

[⬆️ 返回目录](#-本章目录-part-b)

---

## 📝 翻译完成说明 (Translation Notes)

本章 (Part B, p.556-615) 涵盖 CXL 3.2 规范第 8 章后半部分, 主要内容包括:

- **8.2.4.17-21**: CXL 错误能力寄存器、CXL 安全能力结构、CXL 链路能力结构、CXL 扩展安全能力结构
- **8.2.4.22-24**: CXL IDE 能力结构、CXL 窥探过滤器能力结构、CXL 超时与隔离能力结构
- **8.2.4.25-31**: CXL.cachemem 扩展寄存器、BI 路由表/解码器、缓存 ID 路由表/解码器、扩展 HDM 解码器、扩展元数据
- **8.2.5**: CXL ARB/MUX 寄存器
- **8.2.6**: BAR 虚拟化 ACL 寄存器块
- **8.2.7-8**: CPMU 寄存器接口 (CXL 性能监视单元) 和 CHMU 寄存器接口 (CXL 热度监视单元)

翻译规范:
- 寄存器名/字段名/位定义严格保留英文
- 寄存器描述翻译为中文
- 所有图表面板已嵌入相应页码的图片引用
- 所有 5 级章节均使用 H5 (#####) 标记
- 每个章节末尾添加返回目录链接
- 重要概念术语在首次出现时附注英文原名

> 本章内容涉及 CXL 3.2 规范的核心寄存器定义, 是实现 CXL 主机桥、交换机端口和设备时的重要参考。规范中保留了大量英文术语以确保技术准确性。

<a id="sec-8-2-7-1-2"></a>
#### 8.2.7.1.2 CPMU Overflow Status (Offset 10h) | CPMU 溢出状态 (偏移量 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CPMU Overflow Status register indicates the overflow status associated with all the Counter Units.

When any bit in Overflow Status transitions from 0 to 1, the CPMU shall issue an MSI/MSI-X if the Interrupt on Overflow bit for the corresponding Counter Unit is 1.

</td><td style="background-color:#e8e8e8">

CPMU Overflow Status 寄存器指示与所有 Counter Unit 关联的溢出状态。

当 Overflow Status 中的任何位从 0 转换为 1 时, 如果相应 Counter Unit 的 Interrupt on Overflow 位为 1, 则 CPMU 应发出 MSI/MSI-X。

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---

<a id="sec-8-2-7-1-3"></a>
#### 8.2.7.1.3 CPMU Freeze (Offset 18h) | CPMU 冻结 (偏移量 18h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>

The CPMU Freeze register indicates the freeze status associated with all the Counter Units.

</td><td style="background-color:#e8e8e8">

CPMU Freeze 寄存器指示与所有 Counter Unit 关联的冻结状态。

</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-b)

---
