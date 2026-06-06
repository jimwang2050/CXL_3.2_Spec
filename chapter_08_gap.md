# 📘 第 8 章　控制与状态寄存器 (Chapter 8. Control and Status Registers) — Part C (gap fill, p.616-645)

> **Source pages**: 616–645 (gap fill) | **File**: chapter_08_gap.md | **Format**: 中英对照双语

## 📑 本章目录 (Part C Gap)

- [8.2.8.4 CHMU Status | CHMU 状态寄存器](#sec-8-2-8-4)
- [8.2.8.5 CHMU Hotlist Head Register | CHMU 热列表头寄存器](#sec-8-2-8-5)
- [8.2.8.6 CHMU Hotlist Tail Register | CHMU 热列表尾寄存器](#sec-8-2-8-6)
- [8.2.8.7 CHMU Range Configuration Bitmap Register | CHMU 范围配置位图寄存器](#sec-8-2-8-7)
- [8.2.8.8 CHMU Hotlist Entry Register | CHMU 热列表条目寄存器](#sec-8-2-8-8)
- [8.2.9 CXL Device Register Interface | CXL 设备寄存器接口](#sec-8-2-9)
  - [8.2.9.1 CXL Device Capabilities Array Register | CXL 设备能力数组寄存器](#sec-8-2-9-1)
  - [8.2.9.2 CXL Device Capability Header Register | CXL 设备能力头寄存器](#sec-8-2-9-2)
    - [8.2.9.2.1 CXL Device Capabilities | CXL 设备能力](#sec-8-2-9-2-1)
  - [8.2.9.3 Device Status Registers | 设备状态寄存器](#sec-8-2-9-3)
    - [8.2.9.3.1 Event Status Register | 事件状态寄存器](#sec-8-2-9-3-1)
  - [8.2.9.4 Mailbox Registers | 邮箱寄存器](#sec-8-2-9-4)
    - [8.2.9.4.1 Attributes of the Primary Mailbox | 主邮箱属性](#sec-8-2-9-4-1)
    - [8.2.9.4.2 Attributes of the Secondary Mailbox | 副邮箱属性](#sec-8-2-9-4-2)
    - [8.2.9.4.3 Mailbox Capabilities Register | 邮箱能力寄存器](#sec-8-2-9-4-3)
    - [8.2.9.4.4 Mailbox Control Register | 邮箱控制寄存器](#sec-8-2-9-4-4)
    - [8.2.9.4.5 Command Register | 命令寄存器](#sec-8-2-9-4-5)
      - [8.2.9.4.5.1 Command Return Codes | 命令返回码](#sec-8-2-9-4-5-1)
    - [8.2.9.4.6 Mailbox Status Register | 邮箱状态寄存器](#sec-8-2-9-4-6)
    - [8.2.9.4.7 Background Command Status Register | 后台命令状态寄存器](#sec-8-2-9-4-7)
    - [8.2.9.4.8 Command Payload Registers | 命令有效载荷寄存器](#sec-8-2-9-4-8)
  - [8.2.9.5 Memory Device Capabilities | 内存设备能力](#sec-8-2-9-5)
    - [8.2.9.5.1 Memory Device Status Registers | 内存设备状态寄存器](#sec-8-2-9-5-1)
      - [8.2.9.5.1.1 Memory Device Status Register | 内存设备状态寄存器](#sec-8-2-9-5-1-1)
  - [8.2.9.6 FM Mailbox CCI Capability | FM 邮箱 CCI 能力](#sec-8-2-9-6)
    - [8.2.9.6.1 FM Mailbox CCI Status Registers | FM 邮箱 CCI 状态寄存器](#sec-8-2-9-6-1)
      - [8.2.9.6.1.1 FM Mailbox CCI Status Register | FM 邮箱 CCI 状态寄存器](#sec-8-2-9-6-1-1)
  - [8.2.10 Component Command Interface | 组件命令接口](#sec-8-2-10)
    - [8.2.10.1 Information and Status Command Set | 信息和状态命令集](#sec-8-2-10-1)
      - [8.2.10.1.1 Identify (Opcode 0001h) | Identify（操作码 0001h）](#sec-8-2-10-1-1)
      - [8.2.10.1.2 Background Operation Status (Opcode 0002h) | 后台操作状态（操作码 0002h）](#sec-8-2-10-1-2)
      - [8.2.10.1.3 Get Response Message Limit (Opcode 0003h) | 获取响应消息限制（操作码 0003h）](#sec-8-2-10-1-3)
      - [8.2.10.1.4 Set Response Message Limit (Opcode 0004h) | 设置响应消息限制（操作码 0004h）](#sec-8-2-10-1-4)
      - [8.2.10.1.5 Request Abort Background Operation (Opcode 0005h) | 请求中止后台操作（操作码 0005h）](#sec-8-2-10-1-5)
    - [8.2.10.2 Events | 事件](#sec-8-2-10-2)
      - [8.2.10.2.1 Event Records | 事件记录](#sec-8-2-10-2-1)
        - [8.2.10.2.1.1 General Media Event Record | 通用介质事件记录](#sec-8-2-10-2-1-1)

## 🖼 本章图表 (Part C Gap)

- **Figure 8-12** — PCIe MCAP / CXL Compatibility (p.620)
- **Figure 8-13** — CXL Device Registers (p.622)
- **Figure 8-14** — Mailbox Registers (p.625)

## 📊 本章表格 (Part C Gap)

- **Table 8-37** — CHMU Configuration Register (Sheet 2 of 2) (p.616)
- **Table 8-38** — CHMU Status Register (p.617)
- **Table 8-39** — CHMU Hotlist Head Register (p.617)
- **Table 8-40** — CHMU Hotlist Tail Register (p.618)
- **Table 8-41** — CHMU Range Configuration Bitmap Register (p.618)
- **Table 8-42** — CHMU Hotlist Register (p.619)
- **Table 8-43** — CXL Defined Type-Specific Capabilities (p.622)
- **Table 8-44** — CXL Defined Capability Identifiers (Vendor ID = 1E98h or 0000h) (p.623)
- **Table 8-45** — CXL Defined Mailbox Type Identifiers (p.627)
- **Table 8-46** — CXL defined Command Return Codes (Vendor ID = 1E98h or 0000h) (p.628-629)
- **Table 8-47** — CXL Defined Memory Device Capabilities Identifiers (Vendor ID = 1E98h or 0000h) (p.630)
- **Table 8-48** — CXL Defined FM Mailbox CCI Capabilities Identifiers (Vendor ID = 1E98h or 0000h) (p.631)
- **Table 8-49** — CXL Defined Generic Component Command Opcodes (Vendor ID = 1E98h or 0000h) (p.634-635)
- **Table 8-50** — Identify Output Payload (p.636-637)
- **Table 8-51** — Background Operation Status Output Payload (p.637)
- **Table 8-52** — Get Response Message Limit Output Payload (p.638)
- **Table 8-53** — Set Response Message Limit Input Payload (p.638)
- **Table 8-54** — Set Response Message Limit Output Payload (p.639)
- **Table 8-55** — Common Event Record Format (p.640-641)
- **Table 8-56** — Component Identifier Format (p.643)
- **Table 8-57** — General Media Event Record (p.644-645)

---

<a id="sec-8-2-8-4"></a>
## 8.2.8.4 CHMU Status [i] (Offset 70h + CHMU Instance Length * i) | CHMU 状态寄存器 [i]（偏移 70h + CHMU Instance Length * i）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CHMU Status register must be accessed as an 8-byte quantity.</td><td style="background-color:#e8e8e8">CHMU Status 寄存器必须以 8 字节为单位访问。</td></tr>
</tbody>
</table>

> **Table 8-37.** CHMU Configuration Register (Sheet 2 of 2) ｜ CHMU 配置寄存器（第 2 页，共 2 页）
>
> | Bit | Attributes | Description |
> |---|---|---|
> | 103:96 | RW | Down-sampling Factor: If down-sampling is enabled, the device tracks one M2S request over the value encoded in this field.<br/>• Bits[99:96]: Down-sampling factor: One of the 16 possible values reported in the Supported Down-sampling Factor field in the CHMU Capability register.<br/>• Bits[103:100]: Reserved. | 下采样因子（Down-sampling Factor）：如果启用了下采样，设备对该字段中编码的若干 M2S 请求跟踪一次。<br/>• Bits[99:96]：下采样因子：为 CHMU Capability 寄存器中 Supported Down-sampling Factor 字段所报告的 16 种可能值之一。<br/>• Bits[103:100]：保留。 |
> | 111:104 | RW | Reporting Mode: This field is used to enable one of the reporting modes that the device supports.<br/>• 00h = Enable Epoch-based reporting mode. The device ignores this field if the host programs a value that corresponds to an unsupported capability.<br/>• 01h = Enable Always-on Reporting Mode. The device ignores this field if the host programs a value that corresponds to an unsupported capability.<br/>• All other encodings are Reserved. | 报告模式（Reporting Mode）：此字段用于启用设备所支持的某种报告模式。<br/>• 00h = 启用基于 Epoch 的报告模式。如果主机编程的值对应于不支持的能力，设备将忽略此字段。<br/>• 01h = 启用始终开启报告模式（Always-on Reporting Mode）。如果主机编程的值对应于不支持的能力，设备将忽略此字段。<br/>• 所有其他编码为保留。 |
> | 127:112 | RW | Epoch Length: Host-configured epoch length.<br/>• Bits[115:112]: These bits specify the time scale.<br/>— 1h = 100 us<br/>— 2h = 1 ms<br/>— 3h = 10 ms<br/>— 4h = 100 ms<br/>— 5h = 1 s<br/>— All other encodings are Reserved.<br/>• Bits[127:116]: These bits specify the epoch length, using the time scale indicated in bits[115:112]. | Epoch 长度（Epoch Length）：主机配置的 epoch 长度。<br/>• Bits[115:112]：这些位指定时间刻度。<br/>— 1h = 100 us<br/>— 2h = 1 ms<br/>— 3h = 10 ms<br/>— 4h = 100 ms<br/>— 5h = 1 s<br/>— 所有其他编码为保留。<br/>• Bits[127:116]：这些位使用 bits[115:112] 中指示的时间刻度指定 epoch 长度。 |
> | 143:128 | RW | Hotlist Notification Threshold: The device generates an interrupt when the number of entries in the Hotlist is greater than or equal to the value in this field and bit[1] of the Overflow Interrupt Status field, "Hotlist Level Crossed", in the CHMU Status register is equal to 0. Upon this condition, bit[1] of the Overflow Interrupt Status field in the CHMU Status register is set to 1.<br/>The value in this field cannot exceed the Hotlist size programmed in the Hotlist Size field in the CHMU Capability register. If the value of this field exceeds the programmed Hotlist size, this field is ignored, and no interrupts are generated.<br/>When bit[10] of the Flags field, "Interrupt on Hotlist Levels Crossing", is cleared to 0, this field is ignored. | 热列表通知阈值（Hotlist Notification Threshold）：当热列表中的条目数大于或等于此字段中的值，并且 CHMU Status 寄存器中 Overflow Interrupt Status 字段的 bit[1] "Hotlist Level Crossed" 等于 0 时，设备产生中断。在该条件下，CHMU Status 寄存器中 Overflow Interrupt Status 字段的 bit[1] 被置 1。<br/>此字段的值不能超过 CHMU Capability 寄存器中 Hotlist Size 字段所编程的热列表大小。如果此字段的值超过已编程的热列表大小，则此字段被忽略，不会产生中断。<br/>当 Flags 字段的 bit[10] "Interrupt on Hotlist Levels Crossing" 清零为 0 时，此字段被忽略。 |
> | 255:144 | RsvdP | Reserved | 保留 |

> **Table 8-38.** CHMU Status Register ｜ CHMU 状态寄存器
>
> | Bit | Attributes | Description |
> |---|---|---|
> | 15:0 | RO | Status: This field is used to retrieve CHMU-related status and error information.<br/>• Bit[0]: Tracking enabled: When set to 1, the CHMU is enabled. When cleared to 0, the CHMU is disabled.<br/>• Bits[15:1]: Reserved. | 状态（Status）：此字段用于检索与 CHMU 相关的状态和错误信息。<br/>• Bit[0]：跟踪已启用（Tracking enabled）：置 1 时，CHMU 已启用；清零时，CHMU 已禁用。<br/>• Bits[15:1]：保留。 |
> | 31:16 | RO | Operation In progress: This status information returns the operation currently in progress.<br/>• 0000h = No operation in progress. Indicates that no operations that can be started through the Control field in the CHMU Configuration register are in progress.<br/>• 0001h = Enablement in progress. Indicates that enabling of the CHMU is not yet complete.<br/>• 0002h = Disablement in progress. Indicates that disabling of the CHMU is not yet complete.<br/>• 0003h = Reset counters in progress. Indicates that resetting of the CHMU counters is not yet complete.<br/>• All other encodings are Reserved. | 进行中的操作（Operation In progress）：此状态信息返回当前正在进行的操作。<br/>• 0000h = 没有正在进行的操作。表示没有可通过 CHMU Configuration 寄存器中 Control 字段启动的操作正在进行中。<br/>• 0001h = 启用进行中。表示 CHMU 的启用尚未完成。<br/>• 0002h = 禁用进行中。表示 CHMU 的禁用尚未完成。<br/>• 0003h = 计数器复位进行中。表示 CHMU 计数器的复位尚未完成。<br/>• 所有其他编码为保留。 |
> | 39:32 | RO | Counter Width: Current number of bits in each counter used for counting the accesses.<br/>This field also indicates the counter width in each Hotlist entry. | 计数器宽度（Counter Width）：用于对访问进行计数的每个计数器中的当前位数。<br/>此字段还指示每个热列表条目中的计数器宽度。 |
> | 47:40 | RW1C | Overflow Interrupt Status:<br/>• Bit[40]: Hotlist Overflow. When set to 1, the Hotlist has encountered an overflow condition. Additional Hotlist Overflow interrupts are not generated until software clears this bit.<br/>• Bit[41]: Hotlist Level Crossed. When set to 1, the Hotlist has achieved the Hotlist Notification Threshold set by the software. Additional Hotlist Level Crossed interrupts are not generated until software clears this bit to 0.<br/>• Bits[47:42]: Reserved. | 溢出中断状态（Overflow Interrupt Status）：<br/>• Bit[40]：热列表溢出（Hotlist Overflow）。置 1 时，热列表已遇到溢出条件。在软件清除此位之前，不会再产生额外的热列表溢出中断。<br/>• Bit[41]：达到热列表等级（Hotlist Level Crossed）。置 1 时，热列表已达到软件设置的 Hotlist Notification Threshold。在软件将此位清零之前，不会再产生额外的 Hotlist Level Crossed 中断。<br/>• Bits[47:42]：保留。 |
> | 63:48 | RsvdP | Reserved | 保留 |

> **Figure 8-13 (context).** CXL Device Registers (p.622) — referenced here for CHMU context
>
> <img src="figures/chapter_08/page_0617.png" alt="Page 617" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0617.png)

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-8-5"></a>
## 8.2.8.5 CHMU Hotlist Head Register (Offset 78h + CHMU Instance Length * i) | CHMU 热列表头寄存器（偏移 78h + CHMU Instance Length * i）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CHMU Hotlist Head register must be accessed as a 2-byte quantity.</td><td style="background-color:#e8e8e8">CHMU Hotlist Head 寄存器必须以 2 字节为单位访问。</td></tr>
</tbody>
</table>

> **Table 8-39.** CHMU Hotlist Head Register ｜ CHMU 热列表头寄存器
>
> | Bit | Attributes | Description |
> |---|---|---|
> | 15:0 | RW | Head: Index that points to the oldest hot Unit ID in the hotlist that has not yet been read by software. Software reads hot unit entries at this index. This field can be written, by way the host, to the first unread entry.<br/>The Hotlist is considered empty when Head == Tail.<br/>The Hotlist is considered full when Head == (Tail + 1) mod (Hotlist Size). In this condition, the number of units in the CHMU Hotlist is equal to the Hotlist Size – 1. | 头（Head）：指向热列表中尚未被软件读取的最旧的热 Unit ID 的索引。软件在此索引处读取热单元条目。此字段可由主机写入以指向第一个未读条目。<br/>当 Head == Tail 时，热列表视为空。<br/>当 Head == (Tail + 1) mod (Hotlist Size) 时，热列表视为满。在此条件下，CHMU 热列表中的单元数等于 Hotlist Size – 1。 |

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-8-6"></a>
## 8.2.8.6 CHMU Hotlist Tail Register (Offset 7Ah + CHMU Instance Length * i) | CHMU 热列表尾寄存器（偏移 7Ah + CHMU Instance Length * i）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CHMU Hotlist Tail register must be accessed as a 2-byte quantity. The value of this register must not be changed while the CHMU is enabled. If the value is changed while the CHMU is enabled, the device behavior is undefined.</td><td style="background-color:#e8e8e8">CHMU Hotlist Tail 寄存器必须以 2 字节为单位访问。在 CHMU 启用期间不得更改此寄存器的值。如果在 CHMU 启用期间更改其值，则设备行为未定义。</td></tr>
</tbody>
</table>

> **Table 8-40.** CHMU Hotlist Tail Register ｜ CHMU 热列表尾寄存器
>
> | Bit | Attributes | Description |
> |---|---|---|
> | 15:0 | RW | Tail: Index that points to the Hotlist entry in which the device will report the next hot unit. The device increments this field after writing a hot unit entry at this index.<br/>The Hotlist is considered empty when Head == Tail.<br/>The Hotlist is considered full when Head == (Tail + 1) mod (Hotlist Size). In this condition, the number of units in the CHMU Hotlist is equal to the Hotlist Size – 1. | 尾（Tail）：指向设备将在其中报告下一个热单元的热列表条目的索引。设备在此索引处写入热单元条目后递增此字段。<br/>当 Head == Tail 时，热列表视为空。<br/>当 Head == (Tail + 1) mod (Hotlist Size) 时，热列表视为满。在此条件下，CHMU 热列表中的单元数等于 Hotlist Size – 1。 |

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-8-7"></a>
## 8.2.8.7 CHMU Range Configuration Bitmap Register (Offset 10h + CHMU Instance Length * i + CHMU Range Configuration Bitmap Offset[i]) | CHMU 范围配置位图寄存器（偏移 10h + CHMU Instance Length * i + CHMU Range Configuration Bitmap Offset[i]）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This register is used to enable tracking with a 256-MB DPA range granularity. The valid number of Range Configuration Bitmap fields will cover the total device memory capacity. The register may be padded with Reserved bits (with values of 0) until the offset indicated by the device through the CHMU Hotlist Register Offset of the CHMU Capability register. The length of the CHMU Range Configuration Bitmap register is equal to CHMU Hotlist Register Offset - CHMU Range Configuration Bitmap Register Offset. These offset parameters are reported in the CHMU Capability register.</td><td style="background-color:#e8e8e8">此寄存器用于以 256-MB DPA 范围粒度启用跟踪。有效的 Range Configuration Bitmap 字段数量将覆盖设备的总内存容量。该寄存器可填充保留位（值为 0），直到设备通过 CHMU Capability 寄存器的 CHMU Hotlist Register Offset 所指示的偏移为止。CHMU Range Configuration Bitmap 寄存器的长度等于 CHMU Hotlist Register Offset - CHMU Range Configuration Bitmap Register Offset。这些偏移参数在 CHMU Capability 寄存器中报告。</td></tr>
<tr><td>The CHMU Range Configuration Bitmap register must be accessed as an 8-byte quantity.</td><td style="background-color:#e8e8e8">CHMU Range Configuration Bitmap 寄存器必须以 8 字节为单位访问。</td></tr>
</tbody>
</table>

> **Table 8-41.** CHMU Range Configuration Bitmap Register ｜ CHMU 范围配置位图寄存器
>
> | Bit | Attributes | Description |
> |---|---|---|
> | 63:0 | RW | Range Configuration Bitmap 0: Bitmap indicating 256-MB DPA ranges that are enabled to track accesses starting from DPA = 0000 0000 0000 0000h. | 范围配置位图 0（Range Configuration Bitmap 0）：位图，指示已启用以跟踪从 DPA = 0000 0000 0000 0000h 开始的访问的 256-MB DPA 范围。 |
> | 127:64 | RW | Range Configuration Bitmap 1: Bitmap indicating 256-MB DPA ranges that are enabled to track accesses starting from DPA = 0000 0004 0000 0000h. | 范围配置位图 1（Range Configuration Bitmap 1）：位图，指示已启用以跟踪从 DPA = 0000 0004 0000 0000h 开始的访问的 256-MB DPA 范围。 |
> | … | RW | … | … |

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-8-8"></a>
## 8.2.8.8 CHMU Hotlist Entry Register (Offset 10h + CHMU Instance Length * i + CHMU Hotlist Register Offset[i]) | CHMU 热列表条目寄存器（偏移 10h + CHMU Instance Length * i + CHMU Hotlist Register Offset[i]）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The CHMU Hotlist entries provide the Unit ID that exceeds the programmed hotness threshold and the corresponding counter value. The number of bits for the counter values is the same as the one returned by the device in the CHMU Status register after the unit size is programmed by the Unit Size field in the CHMU Configuration register. The number of bits associated with the Unit IDs depend on the programmed unit size. The counter bits will be placed in the least significant bits of the entry.</td><td style="background-color:#e8e8e8">CHMU 热列表条目提供超出已编程热度阈值的 Unit ID 以及相应的计数值。计数器值的位数与 CHMU Configuration 寄存器中 Unit Size 字段对单元大小进行编程后，设备在 CHMU Status 寄存器中返回的位数相同。与 Unit ID 关联的位数取决于已编程的单元大小。计数器位将放置在条目的最低有效位。</td></tr>
<tr><td>Each CHMU Hotlist Entry register must be accessed as an 8-byte quantity.</td><td style="background-color:#e8e8e8">每个 CHMU Hotlist Entry 寄存器必须以 8 字节为单位访问。</td></tr>
</tbody>
</table>

> **Table 8-42.** CHMU Hotlist Register ｜ CHMU 热列表寄存器
>
> | Bit | Attributes | Description |
> |---|---|---|
> | 63:0 | RO | Entry 0: CHMU Hotlist Entry 0, which reports the Unit ID and related counter value that exceeds the programmed Hotness Threshold:<br/>• Bits[63:N]: Unit ID<br/>• Bits[N-1:0]: Counter value<br/>N is the Counter width value returned by the device in the CHMU Status register.<br/>The counter value is invalid if Always-on Reporting mode is enabled. | 条目 0（Entry 0）：CHMU 热列表条目 0，报告超出已编程热度阈值（Hotness Threshold）的 Unit ID 和相关计数值：<br/>• Bits[63:N]：Unit ID<br/>• Bits[N-1:0]：计数值<br/>N 是设备在 CHMU Status 寄存器中返回的计数器宽度值。<br/>如果启用了 Always-on Reporting 模式，则计数值无效。 |
> | 127:64 | RO | Entry 1. CHMU Hotlist Entry 1, which reports the Unit ID and related counter value exceeding the programmed Hotness Threshold:<br/>• Bits[63:N] Unit ID<br/>• Bits[N-1:0] Counter value<br/>N is the Counter width value returned by the device in the CHMU Status register.<br/>The counter value is invalid if Always-on Reporting mode is enabled. | 条目 1（Entry 1）。CHMU 热列表条目 1，报告超出已编程热度阈值（Hotness Threshold）的 Unit ID 和相关计数值：<br/>• Bits[63:N]：Unit ID<br/>• Bits[N-1:0]：计数值<br/>N 是设备在 CHMU Status 寄存器中返回的计数器宽度值。<br/>如果启用了 Always-on Reporting 模式，则计数值无效。 |
> | … | RO | … | … |
> | (64*M-1):(64*(M-1)) | RO | Entry M-1¹. CHMU Hotlist Entry M-1, which reports the Unit ID and related value counter exceeding the programmed Hotness Threshold:<br/>• Bits[63:N] Unit ID<br/>• Bits[N-1:0] Counter value<br/>N is the Counter width value returned by the device in the CHMU Status register.<br/>The counter value is Invalid if Always-on Reporting mode is enabled. | 条目 M-1¹（Entry M-1）。CHMU 热列表条目 M-1，报告超出已编程热度阈值（Hotness Threshold）的 Unit ID 和相关计数值：<br/>• Bits[63:N]：Unit ID<br/>• Bits[N-1:0]：计数值<br/>N 是设备在 CHMU Status 寄存器中返回的计数器宽度值。<br/>如果启用了 Always-on Reporting 模式，则计数值无效。 |
>
> 1. M is the Hotlist Size in the CHMU Capability register.
> 2. 1. M 是 CHMU Capability 寄存器中的 Hotlist Size。

> **Figure 8-12 (context).** Page render for CHMU register continuation (p.619)
>
> <img src="figures/chapter_08/page_0619.png" alt="Page 619" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0619.png)

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9"></a>
## 8.2.9 CXL Device Register Interface | CXL 设备寄存器接口

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL device registers are mapped in memory space allocated via a standard PCIe BAR. The entry in the Register Locator DVSEC structure (see Section 8.1.9) with Register Identifier = 03h describes the BAR number and the offset within the BAR where these registers are mapped. The PCIe BAR shall be marked as prefetchable in the PCIe Configuration Space Header. At the beginning of the CXL device register block is a CXL Device Capabilities Array register that defines the size of the CXL Device Capabilities Array followed by a list of CXL Device Capability headers. Each header contains an offset to the capability-specific register structure from the start of the CXL device register block.</td><td style="background-color:#e8e8e8">CXL 设备寄存器映射在通过标准 PCIe BAR 分配的内存空间中。Register Locator DVSEC 结构（参见 8.1.9 节）中 Register Identifier = 03h 的条目描述了这些寄存器所映射到的 BAR 编号以及 BAR 内的偏移。在 PCIe 配置空间头中，该 PCIe BAR 应标记为可预取（prefetchable）。CXL 设备寄存器块的开头是一个 CXL Device Capabilities Array 寄存器，用于定义 CXL Device Capabilities Array 的大小，后跟一个 CXL Device Capability 头列表。每个头包含从 CXL 设备寄存器块开始到特定能力寄存器结构的偏移。</td></tr>
<tr><td>An MLD shall implement one instance of CXL Device registers in the MMIO space of each applicable LD.</td><td style="background-color:#e8e8e8">MLD 应在每个适用 LD 的 MMIO 空间中实现 CXL Device 寄存器的一个实例。</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE — Compatibility with PCIe MMIO Capabilities (MCAP) Register Block | 实现说明 — 与 PCIe MMIO Capabilities (MCAP) 寄存器块的兼容性**
>
> CXL components are expected to transition to the PCIe standard MCAP Register Block that has the same format as the CXL defined capabilities. When doing so, CXL components are required to maintain compatibility with legacy CXL software as portrayed in Figure 8-12.
>
> CXL 组件预计将过渡到具有与 CXL 定义能力相同格式的 PCIe 标准 MCAP Register Block。过渡时，CXL 组件需要与遗留 CXL 软件保持兼容性，如图 8-12 所示。

> **Figure 8-12.** PCIe MCAP / CXL Compatibility ｜ PCIe MCAP / CXL 兼容性
>
> <img src="figures/chapter_08/fig_0620_1.png" alt="Figure 8-12" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0620.png)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>No registers defined in Section 8.2.9 are larger than 64-bit wide so that is the maximum access size allowed for these registers. If this rule is not followed, the behavior is undefined.</td><td style="background-color:#e8e8e8">8.2.9 节中定义的寄存器宽度均不超过 64 位，因此这是这些寄存器允许的最大访问大小。如果不遵守此规则，则行为未定义。</td></tr>
<tr><td>To illustrate how the fields fit together, the layouts in Section 8.2.9.1, Section 8.2.9.2, and Figure 8-14 (Mailbox registers) are shown as wider than a 64-bit register. Implementations are expected to use any size accesses for this information up to 64 bits without loss of functionality – the information is designed to be accessed in chunks, each no greater than 64 bits.</td><td style="background-color:#e8e8e8">为了说明各字段如何组合，8.2.9.1 节、8.2.9.2 节以及图 8-14（邮箱寄存器）中的布局显示为宽于 64 位寄存器。实现应使用不大于 64 位的任意大小访问来获取这些信息而不会损失功能——这些信息设计为可按不超过 64 位的块进行访问。</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE — Continued | 实现说明 — 续**
>
> 1. CXL components are required to advertise CXL defined capabilities in both the legacy CXL Device Capabilities Array and the PCIe MCAP Array. Legacy CXL software discovers the CXL Device Capabilities Array using the entry in the CXL Register Locator DVSEC with Register Identifier = 03h (CXL Device Registers). Updated software discovers the PCIe MCAP Array using the entry in the PCIe MMIO Register Block Locator (MRBL) Extended Capability with Register Block Identifier = 01h (MMIO Capabilities). Updated SW should check the PCIe MCAP Array first and only fallback to the legacy CXL Device Capabilities Array if it's not supported.
>
> 1. CXL 组件需要在遗留 CXL Device Capabilities Array 和 PCIe MCAP Array 中都通告 CXL 定义的能力。遗留 CXL 软件使用 CXL Register Locator DVSEC 中 Register Identifier = 03h（CXL Device Registers）的条目来发现 CXL Device Capabilities Array。更新后的软件使用 PCIe MMIO Register Block Locator (MRBL) Extended Capability 中 Register Block Identifier = 01h（MMIO Capabilities）的条目来发现 PCIe MCAP Array。更新后的软件应首先检查 PCIe MCAP Array，仅当不支持时再回退到遗留 CXL Device Capabilities Array。
>
> 2. While CXL defined capabilities must be advertised in both the legacy CXL Device Capabilities Array and the PCIe MCAP Array, CXL components may choose to implement the register structures for CXL defined capabilities in one of the following ways. In either case, legacy software locates the register structure from the offset specified in the header in the legacy CXL Device Capabilities Array. Updated software locates the register structure from the offset specified in the header in the PCIe MCAP Array.
>
> 2. 虽然 CXL 定义的能力必须在遗留 CXL Device Capabilities Array 和 PCIe MCAP Array 中都进行通告，但 CXL 组件可以选择以下列方式之一来实现 CXL 定义能力的寄存器结构。在任一情况下，遗留软件都根据遗留 CXL Device Capabilities Array 中头所指定的偏移来定位寄存器结构。更新后的软件根据 PCIe MCAP Array 中头所指定的偏移来定位寄存器结构。
>
> &nbsp;&nbsp;&nbsp;&nbsp;a. CXL components may alias the location of CXL defined capabilities specified in the legacy CXL Device Capabilities Array and the PCIe MCAP Array to a single instance of the register structure. In this case, the CXL Device Capabilities Array, the PCIe MCAP Array, and the register structures are required to be located in the same PCIe BAR and both the CXL Device Capabilities Array and the PCIe MCAP Array must be located below the register structures.
>
> &nbsp;&nbsp;&nbsp;&nbsp;a. CXL 组件可以将遗留 CXL Device Capabilities Array 和 PCIe MCAP Array 中指定的 CXL 定义能力位置别名（alias）到寄存器结构的单个实例。在这种情况下，CXL Device Capabilities Array、PCIe MCAP Array 和寄存器结构必须位于同一 PCIe BAR 中，并且 CXL Device Capabilities Array 和 PCIe MCAP Array 都必须位于寄存器结构之下。
>
> &nbsp;&nbsp;&nbsp;&nbsp;b. CXL components may choose to implement two instances of the register structures for CXL defined capabilities; one located from the offset specified in the header in the CXL Device Capabilities Array and one located from the offset specified in the header in the PCIe MCAP Array. Updated software is required to use the instance of the register structure located via the PCIe MCAP Array.
>
> &nbsp;&nbsp;&nbsp;&nbsp;b. CXL 组件可以选择为 CXL 定义能力实现两个寄存器结构实例：一个位于 CXL Device Capabilities Array 中头所指定的偏移处，另一个位于 PCIe MCAP Array 中头所指定的偏移处。更新后的软件需要使用通过 PCIe MCAP Array 定位的寄存器结构实例。
>
> 3. CXL components that support both the CXL primary mailbox and the PCIe MMB are required to alias the PCIe MMB (Vendor ID = 0001h and MCAP ID = 0001h) to the CXL Primary Mailbox registers. Refer to Section 9.20 for complete details.
>
> 3. 同时支持 CXL primary mailbox 和 PCIe MMB 的 CXL 组件需要将 PCIe MMB（Vendor ID = 0001h 且 MCAP ID = 0001h）别名（alias）到 CXL Primary Mailbox 寄存器。完整细节请参见 9.20 节。

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9-1"></a>
## 8.2.9.1 CXL Device Capabilities Array Register (Offset 00h) | CXL 设备能力数组寄存器（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> CXL components are recommended to transition to the equivalent PCIe MCAP Array Register as defined in [PCIe].
>
> 建议 CXL 组件过渡到 [PCIe] 中定义的等效 PCIe MCAP Array Register。

> **Figure 8-13.** CXL Device Registers ｜ CXL 设备寄存器
>
> <img src="figures/chapter_08/page_0622.png" alt="Figure 8-13" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0622.png)

> **CXL Device Capabilities Array Register Layout | CXL Device Capabilities Array 寄存器布局**
>
> | Bits | Attributes | Description |
> |---|---|---|
> | 15:0 | - | Capability ID: See equivalent MCAP ID field in the MCAP Array Register¹.<br/>1. Refer to [PCIe] for the definition of this field. | Capability ID：请参阅 MCAP Array Register¹ 中等效的 MCAP ID 字段。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 23:16 | - | Version: See equivalent MCAP Array Version field in the MCAP Array Register¹.<br/>1. Refer to [PCIe] for the definition of this field. | Version：请参阅 MCAP Array Register¹ 中等效的 MCAP Array Version 字段。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 27:24 | - | Type: See equivalent MCAP Type field in the MCAP Array Register¹. For CXL, bit 27 is fixed to 0 and bits 26:24 are defined in Table 8-43.<br/>1. Refer to [PCIe] for the definition of this field. | Type：请参阅 MCAP Array Register¹ 中等效的 MCAP Type 字段。对于 CXL，bit 27 固定为 0，bits 26:24 在表 8-43 中定义。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 31:28 | - | Refer to [PCIe] for the definition of this field. | 此字段的定义请参阅 [PCIe]。 |
> | 47:32 | - | Capabilities Count: See equivalent MCAP Count field in the MCAP Array Register¹.<br/>1. Refer to [PCIe] for the definition of this field. | Capabilities Count：请参阅 MCAP Array Register¹ 中等效的 MCAP Count 字段。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 127:48 | - | Refer to [PCIe] for the definition of this field. | 此字段的定义请参阅 [PCIe]。 |

> **Table 8-43.** CXL Defined Type-Specific Capabilities ｜ CXL 定义的 Type-Specific 能力
>
> | Type | Description |
> |---|---|
> | 0h | Reserved for PCIe¹.<br/>1. Refer to [PCIe] for the definition of this type. | 为 PCIe¹ 保留。<br/>1. 此类型的定义请参阅 [PCIe]。 |
> | 1h | Memory Device Capabilities (see Section 8.2.9.5). | 内存设备能力（参见 8.2.9.5 节）。 |
> | 2h | FM Mailbox CCI Capabilities (see Section 8.2.9.6). | FM 邮箱 CCI 能力（参见 8.2.9.6 节）。 |
> | 3-7h | Reserved | 保留 |

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9-2"></a>
## 8.2.9.2 CXL Device Capability Header Register (Offset: Varies) | CXL 设备能力头寄存器（偏移：可变）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Each capability in the CXL device capabilities array is described by a CXL Device Capability Header register that identifies the specific capability and points to the capability register structure in register space.</td><td style="background-color:#e8e8e8">CXL 设备能力数组中的每个能力由一个 CXL Device Capability Header 寄存器描述，该寄存器标识特定能力并指向寄存器空间中的能力寄存器结构。</td></tr>
</tbody>
</table>

<a id="sec-8-2-9-2-1"></a>
### 8.2.9.2.1 CXL Device Capabilities | CXL 设备能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL defined device capability register structures are identified by a 2-byte identifier.</td><td style="background-color:#e8e8e8">CXL 定义的设备能力寄存器结构由 2 字节标识符标识。</td></tr>
<tr><td>• CXL defined capability identifiers 0000h-3FFFh describe generic CXL device capabilities as specified in Table 8-44.</td><td style="background-color:#e8e8e8">• CXL 定义的能力标识符 0000h-3FFFh 描述表 8-44 中规定的通用 CXL 设备能力。</td></tr>
<tr><td>• Capability identifiers 4000h-7FFFh describe type-specific capabilities associated with the type specified in the CXL Device Capabilities Array register (see Section 8.2.9.1).</td><td style="background-color:#e8e8e8">• 能力标识符 4000h-7FFFh 描述与 CXL Device Capabilities Array 寄存器中指定的类型（参见 8.2.9.1 节）相关联的 Type-Specific 能力。</td></tr>
<tr><td>• Capability identifiers 8000h-FFFFh describe vendor specific capabilities.</td><td style="background-color:#e8e8e8">• 能力标识符 8000h-FFFFh 描述厂商特定能力。</td></tr>
<tr><td>CXL defined Capability identifiers 0000h-3FFFh that are not specified in this table are reserved.</td><td style="background-color:#e8e8e8">本表未指定的 CXL 定义能力标识符 0000h-3FFFh 为保留。</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> CXL components are recommended to transition to the equivalent PCIe MCAP Header Register as defined in [PCIe].
>
> 建议 CXL 组件过渡到 [PCIe] 中定义的等效 PCIe MCAP Header Register。

> **CXL Device Capability Header Register Layout | CXL Device Capability Header 寄存器布局**
>
> | Bits | Attributes | Description |
> |---|---|---|
> | 15:0 | - | Capability ID: See equivalent MCAP ID field in the MCAP Header Register¹. See Section 8.2.9.2.1 for the list of CXL defined capability identifiers.<br/>1. Refer to [PCIe] for the definition of this field. | Capability ID：请参阅 MCAP Header Register¹ 中等效的 MCAP ID 字段。CXL 定义的能力标识符列表请参见 8.2.9.2.1 节。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 23:16 | - | Version: See equivalent MCAP Version field in the MCAP Header Register¹.<br/>1. Refer to [PCIe] for the definition of this field. | Version：请参阅 MCAP Header Register¹ 中等效的 MCAP Version 字段。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 31:24 | - | Refer to [PCIe] for the definition of this field. | 此字段的定义请参阅 [PCIe]。 |
> | 63:32 | - | Offset: See equivalent MCAP Offset field in the MCAP Header Register¹.<br/>1. Refer to [PCIe] for the definition of this field. | Offset：请参阅 MCAP Header Register¹ 中等效的 MCAP Offset 字段。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 95:64 | - | Length: See equivalent MCAP Length field in the MCAP Header Register¹.<br/>1. Refer to [PCIe] for the definition of this field. | Length：请参阅 MCAP Header Register¹ 中等效的 MCAP Length 字段。<br/>1. 此字段的定义请参阅 [PCIe]。 |
> | 127:96 | - | Refer to [PCIe] for the definition of this field. | 此字段的定义请参阅 [PCIe]。 |

> **Table 8-44.** CXL Defined Capability Identifiers (Vendor ID = 1E98h or 0000h) ｜ CXL 定义的能力标识符（Vendor ID = 1E98h 或 0000h）
>
> | Capability ID | Description | Required¹ | Version |
> |---|---|---|---|
> | 0001h | Device Status Registers: Describes the generic CXL device status registers. Only one instance of this register structure shall exist per device. | M | 02h |
> | 0002h | Primary Mailbox Registers: Describes the primary mailbox registers. Only one instance of this register structure shall exist per device. | M | 01h |
> | 0003h | Secondary Mailbox Registers: Describes the secondary mailbox registers. At most one instance of this register structure shall exist per device. | O | 01h |
>
> | Capability ID | Description | 必需¹ | Version |
> |---|---|---|---|
> | 0001h | Device Status Registers：描述通用 CXL 设备状态寄存器。每个设备只能存在此寄存器结构的一个实例。 | M | 02h |
> | 0002h | Primary Mailbox Registers：描述主邮箱寄存器。每个设备只能存在此寄存器结构的一个实例。 | M | 01h |
> | 0003h | Secondary Mailbox Registers：描述副邮箱寄存器。每个设备最多只能存在此寄存器结构的一个实例。 | O | 01h |
>
> 1. M = Mandatory for all devices that implement the CXL Device Register entry (Register Block Identifier=03h) in the Register Locator DVSEC (see Section 8.1.9). O = Optional.
> 1. M = 在 Register Locator DVSEC（参见 8.1.9 节）中实现 CXL Device Register 条目（Register Block Identifier=03h）的所有设备必需。O = 可选。

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9-3"></a>
## 8.2.9.3 Device Status Registers (Offset: Varies) | 设备状态寄存器（偏移：可变）

<a id="sec-8-2-9-3-1"></a>
### 8.2.9.3.1 Event Status Register (Device Status Registers Capability Offset + 00h) | 事件状态寄存器（设备状态寄存器能力偏移 + 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Event Status register indicates which events are currently ready for host actions, such as fetching event log records. The host may choose to poll for these events by periodically reading this register, or it may choose to enable interrupts for some of these events. The only pollable/interruptible events that are not indicated in this register are mailbox command completions since each set of mailbox registers provides that information.</td><td style="background-color:#e8e8e8">Event Status 寄存器指示当前哪些事件已准备好供主机处理，例如获取事件日志记录。主机可选择通过定期读取此寄存器来轮询这些事件，也可选择为某些事件启用中断。本寄存器中未指示的唯一可轮询/可中断事件是邮箱命令完成，因为每组邮箱寄存器都提供该信息。</td></tr>
<tr><td>Unless specified otherwise in the field definitions below, each field is present in version 1 and later of this structure. The device shall report the version of this structure in the Version field of the CXL Device Capability Header register.</td><td style="background-color:#e8e8e8">除非下面的字段定义另有规定，否则此结构中的每个字段都存在于版本 1 及更高版本中。设备应在 CXL Device Capability Header 寄存器的 Version 字段中报告此结构的版本。</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> CXL components are permitted to set the PCIe MCAP Vendor ID to 0000h for CXL defined capabilities. 0000h is a PCI-SIG reserved value for legacy CXL compatibility. However, it is strongly recommended to use the CXL Vendor ID (1E98h) to identify CXL defined capabilities.
>
> 对于 CXL 定义的能力，允许 CXL 组件将 PCIe MCAP Vendor ID 设置为 0000h。0000h 是 PCI-SIG 为遗留 CXL 兼容性保留的值。但是，强烈建议使用 CXL Vendor ID（1E98h）来标识 CXL 定义的能力。

> **Event Status Register Layout | Event Status 寄存器布局**
>
> | Bits | Attributes | Description |
> |---|---|---|
> | 31:0 | RO | Event Status: When set, one or more event records exist in the specified event log. The device implements a single instance of the event log for host use, which can be accessed either via Primary Mailbox or Secondary mailbox, if applicable. The negotiation between the Operating System and the System Firmware for the ownership of Memory Error Event Logs is managed by CXL _OSC mechanism (See Section 9.18.2).<br/>Use the Get and Clear Event Records commands to retrieve and clear the event records. Once the event log has zero event records, the bit is cleared.<br/>• Bit[0]: Informational Event Log<br/>• Bit[1]: Warning Event Log<br/>• Bit[2]: Failure Event Log<br/>• Bit[3]: Fatal Event Log<br/>• Bit[4]: Dynamic Capacity Event Log¹<br/>• Bits[31:5]: Reserved<br/>1. This bit was introduced with Version=2. | Event Status：置位时，指定事件日志中存在一条或多条事件记录。设备为主机使用实现了事件日志的单个实例，可通过 Primary Mailbox 或 Secondary Mailbox（如果适用）访问。操作系统与系统固件之间关于内存错误事件日志所有权的协商由 CXL _OSC 机制管理（参见 9.18.2 节）。<br/>使用 Get and Clear Event Records 命令检索和清除事件记录。一旦事件日志中的事件记录数为零，该位即被清除。<br/>• Bit[0]：Informational Event Log<br/>• Bit[1]：Warning Event Log<br/>• Bit[2]：Failure Event Log<br/>• Bit[3]：Fatal Event Log<br/>• Bit[4]：Dynamic Capacity Event Log¹<br/>• Bits[31:5]：保留<br/>1. 此位在 Version=2 中引入。 |
> | 63:32 | RO | Reserved | 保留 |

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9-4"></a>
## 8.2.9.4 Mailbox Registers (Offset: Varies) | 邮箱寄存器（偏移：可变）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL defined extensions to the PCIe standard MMIO Mailbox Capability (MMB) Registers are described in this section. Refer to the MMIO Mailbox Capability (MMB) Section of the [PCIe MMPT ECN] for the definition of fields not listed.</td><td style="background-color:#e8e8e8">本节描述了对 PCIe 标准 MMIO Mailbox Capability (MMB) 寄存器的 CXL 定义扩展。未列出字段的定义请参阅 [PCIe MMPT ECN] 的 MMIO Mailbox Capability (MMB) 一节。</td></tr>
<tr><td>There are two types of CXL mailboxes provided through the device's register interface: primary and secondary. Each mailbox represents a unique CCI instance in the device and the properties of each instance are defined in Section 9.1.1. The secondary mailbox does not support background operations. The status of a background operation issued to a device's primary mailbox can be retrieved from the Background Command Status register, as detailed in Section 8.2.9.4.7.</td><td style="background-color:#e8e8e8">通过设备的寄存器接口提供两种类型的 CXL 邮箱：主邮箱和副邮箱。每个邮箱代表设备中的一个唯一 CCI 实例，每个实例的属性在 9.1.1 节中定义。副邮箱不支持后台操作。下发给设备主邮箱的后台操作的状态可从 Background Command Status 寄存器获取，详见 8.2.9.4.7 节。</td></tr>
</tbody>
</table>

> **Figure 8-14.** Mailbox Registers ｜ 邮箱寄存器
>
> <img src="figures/chapter_08/page_0625.png" alt="Figure 8-14" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0625.png)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The register interface for both types of mailboxes is the same and is described in the MMB Registers section of [PCIe]. CXL defined extensions to the MMB Registers are called out in this section. The difference between the two types of mailboxes is their intended use and commands allowed. Details on these differences are described in Section 8.2.9.4.1 and Section 8.2.9.4.2.</td><td style="background-color:#e8e8e8">两种邮箱类型的寄存器接口相同，并在 [PCIe] 的 MMB Registers 一节中描述。对 MMB 寄存器的 CXL 定义扩展将在本节中指出。两种邮箱类型的区别在于其预期用途和允许的命令。有关这些区别的详细信息，请参见 8.2.9.4.1 节和 8.2.9.4.2 节。</td></tr>
<tr><td>Commands that require a longer execution time than the MMB command timeout shall be completed asynchronously in the background. Only one command can be executed in the background at a time. The status of a background command can be retrieved from the Background Command Status register. Background commands do not continue to execute across Conventional Resets. For devices with multiple mailboxes, only the primary mailbox shall be used to issue background commands.</td><td style="background-color:#e8e8e8">执行时间超过 MMB 命令超时的命令应在后台异步完成。一次只能执行一个后台命令。后台命令的状态可从 Background Command Status 寄存器获取。后台命令不会在 Conventional Reset 之间继续执行。对于具有多个邮箱的设备，只能使用主邮箱下发后台命令。</td></tr>
<tr><td>The device shall report the version of these structures in the Version field of the CXL Device Capability Header register.</td><td style="background-color:#e8e8e8">设备应在 CXL Device Capability Header 寄存器的 Version 字段中报告这些结构的版本。</td></tr>
<tr><td>In case of a timeout, the caller may attempt to recover the device by either issuing CXL or Conventional Reset to the device.</td><td style="background-color:#e8e8e8">在发生超时的情况下，调用方可以通过向设备下发 CXL Reset 或 Conventional Reset 来尝试恢复设备。</td></tr>
<tr><td>When a command is successfully started as a background operation, the device shall return the Background Command Started return code defined in Section 8.2.9.4.5.1. While the command is executing in the background, the device should update the percentage complete in the Background Command Status register at least once per second. An ongoing background command may be aborted by issuing a Request Abort Background Operation command (see Section 8.2.10.1.5). It is strongly recommended that devices continue to accept new non-background commands while the background operation is running. The background operation shall not write to the Command Payload registers. Once the command completes in the background, the device shall update the Background Command Status register with the appropriate return code as defined in Section 8.2.9.4.5.1. The caller may then retrieve the results of the background operation from the Background Command Status register.</td><td style="background-color:#e8e8e8">当命令作为后台操作成功启动时，设备应返回 8.2.9.4.5.1 节中定义的 Background Command Started 返回码。在命令于后台执行期间，设备应至少每秒更新一次 Background Command Status 寄存器中的完成百分比。可通过下发 Request Abort Background Operation 命令（参见 8.2.10.1.5 节）来中止正在运行的后台命令。强烈建议设备在后台操作运行期间继续接受新的非后台命令。后台操作不应写入 Command Payload 寄存器。一旦命令在后台完成，设备应使用 8.2.9.4.5.1 节中定义的相应返回码更新 Background Command Status 寄存器。然后，调用方可以从 Background Command Status 寄存器中检索后台操作的结果。</td></tr>
<tr><td>The Mailbox registers are described in Figure 8-14.</td><td style="background-color:#e8e8e8">邮箱寄存器如图 8-14 所示。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9-4-1"></a>
### 8.2.9.4.1 Attributes of the Primary Mailbox | 主邮箱的属性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The primary mailbox supports all commands described in Section 8.2.10. The primary mailbox also supports the optional feature to provide mailbox completion interrupts, if implemented by a device. Implementation of the primary mailbox is mandatory.</td><td style="background-color:#e8e8e8">主邮箱支持 8.2.10 节中描述的所有命令。如果设备实现了邮箱完成中断，主邮箱还支持提供邮箱完成中断的可选功能。主邮箱的实现是必需的。</td></tr>
<tr><td>The exact details on how the primary mailbox is used may vary. The intended use is to provide the main method for submitting commands to the device, used by both pre-boot software and OS software. The platform shall coordinate the use of the primary mailbox so that only one software entity "owns" the mailbox at a given time and that the transfer of ownership happens in-between mailbox commands so that one entity cannot corrupt the mailbox state of the other. The intended practice is that the pre-boot software uses the primary mailbox until control is transferred to the OS being booted, and at that time the OS takes over sole ownership of the primary mailbox until the OS is shut down. Because the physical address of the primary mailbox can change as the result of a PCIe reconfiguration performed by the primary mailbox owner, each time the primary mailbox changes ownership, the new owner shall read the appropriate configuration registers to discover the current location of the mailbox registers, just as it does during device initialization.</td><td style="background-color:#e8e8e8">主邮箱的详细使用方式可能有所不同。其预期用途是提供向设备下发命令的主要方法，由预启动软件和操作系统软件使用。平台应协调主邮箱的使用，以便在给定时间只有一个软件实体"拥有"邮箱，并且所有权的转移发生在邮箱命令之间，从而一个实体不能破坏另一个实体的邮箱状态。预期做法是：预启动软件使用主邮箱，直到控制权转移给正在启动的操作系统；此时，操作系统接管主邮箱的唯一所有权，直到操作系统关闭。由于主邮箱的物理地址可能因主邮箱所有者执行的 PCIe 重新配置而发生变化，因此每次主邮箱所有权发生变化时，新所有者应读取相应的配置寄存器以发现邮箱寄存器的当前位置，就像在设备初始化期间所做的那样。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

<a id="sec-8-2-9-4-2"></a>
### 8.2.9.4.2 Attributes of the Secondary Mailbox | 副邮箱的属性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The secondary mailbox, if implemented by a device, supports only a subset of the commands described in Section 8.2.10. The Command Effects Log shall specify which CXL defined commands are allowed on the secondary mailbox, and all other commands shall return the error Unsupported Mailbox or CCI. The secondary mailbox does not support mailbox completion interrupts. Therefore, any fields related to command interrupts shall be set to 0 on the Secondary MB. Implementation of the secondary mailbox is optional.</td><td style="background-color:#e8e8e8">如果设备实现了副邮箱，则其仅支持 8.2.10 节中描述的命令的子集。Command Effects Log 应指定哪些 CXL 定义的命令在副邮箱上被允许，所有其他命令应返回错误 Unsupported Mailbox or CCI。副邮箱不支持邮箱完成中断。因此，在 Secondary MB 上任何与命令中断相关的字段都应设置为 0。副邮箱的实现是可选的。</td></tr>
<tr><td>The exact details on how the secondary mailbox is used may vary. The intended use is to provide a method for submitting commands to the device by platform firmware that processes events while the OS owns the primary mailbox. By using the secondary mailbox, platform firmware does not corrupt the state of any in-progress mailbox operations on the primary mailbox.</td><td style="background-color:#e8e8e8">副邮箱的详细使用方式可能有所不同。其预期用途是：在操作系统拥有主邮箱的同时，为处理事件的平台固件提供一种向设备下发命令的方法。通过使用副邮箱，平台固件不会破坏主邮箱上任何正在进行的邮箱操作的状态。</td></tr>
<tr><td>The secondary mailbox shall return identical information as the primary mailbox for a Get Log command issued with Log Identifier=CEL. Devices shall indicate which commands are allowed on the secondary mailbox by setting the Secondary Mailbox Supported flag for the supported opcodes in the Command Effects Log. The set of commands that are supported on the secondary mailbox is implementation specific. It is recommended (but not required) that the secondary mailbox supports all commands in the Events, Logs, and Identify command sets defined in Section 8.2.10.</td><td style="background-color:#e8e8e8">对于以 Log Identifier=CEL 下发的 Get Log 命令，副邮箱应返回与主邮箱相同的信息。设备应通过在 Command Effects Log 中为支持的操作码设置 Secondary Mailbox Supported 标志来指示哪些命令在副邮箱上被允许。副邮箱支持的命令集是实现特定的。建议（但非必需）副邮箱支持 8.2.10 节中定义的 Events、Logs 和 Identify 命令集中的所有命令。</td></tr>
<tr><td>Since the physical address of the secondary mailbox can change as a result of a PCIe reconfiguration performed by the primary mailbox owner, each time the secondary mailbox is used, the software using it shall read the appropriate configuration registers to discover the current location of the mailbox registers.</td><td style="background-color:#e8e8e8">由于副邮箱的物理地址可能因主邮箱所有者执行的 PCIe 重新配置而发生变化，因此每次使用副邮箱时，使用它的软件应读取相应的配置寄存器以发现邮箱寄存器的当前位置。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c-gap)

---

