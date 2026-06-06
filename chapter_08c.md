# 📘 第 8 章　控制与状态寄存器 (Chapter 8. Control and Status Registers) — Part C

> **Source pages**: 676–735 (Part C) | **File**: chapter_08c.md | **Format**: 中英对照双语

## 📑 本章目录 (Part C)

- [8.2.10.5.2 Get Log (Opcode 0401h)](#sec-8-2-10-5-2)
- [8.2.10.5.2.1 Command Effects Log (CEL)](#sec-8-2-10-5-2-1)
- [8.2.10.5.2.2 Vendor Debug Log](#sec-8-2-10-5-2-2)
- [8.2.10.5.2.3 Component State Dump Log](#sec-8-2-10-5-2-3)
- [8.2.10.5.2.4 DDR5 Error Check Scrub (ECS) Log](#sec-8-2-10-5-2-4)
- [8.2.10.5.2.5 Media Test Capability Log](#sec-8-2-10-5-2-5)
- [8.2.10.5.2.6 Media Test Results Logs](#sec-8-2-10-5-2-6)
- [8.2.10.5.3 Get Log Capabilities (Opcode 0402h)](#sec-8-2-10-5-3)
- [8.2.10.5.4 Clear Log (Opcode 0403h)](#sec-8-2-10-5-4)
- [8.2.10.5.5 Populate Log (Opcode 0404h)](#sec-8-2-10-5-5)
- [8.2.10.5.6 Get Supported Logs Sub-List (Opcode 0405h)](#sec-8-2-10-5-6)
- [8.2.10.6 Features](#sec-8-2-10-6)
- [8.2.10.6.1 Get Supported Features (Opcode 0500h)](#sec-8-2-10-6-1)
- [8.2.10.6.2 Get Feature (Opcode 0501h)](#sec-8-2-10-6-2)
- [8.2.10.6.3 Set Feature (Opcode 0502h)](#sec-8-2-10-6-3)
- [8.2.10.6.4 Metabits Storage Feature Discovery and Configuration](#sec-8-2-10-6-4)
- [8.2.10.7 Maintenance](#sec-8-2-10-7)
- [8.2.10.7.1 Perform Maintenance (Opcode 0600h)](#sec-8-2-10-7-1)
- [8.2.10.7.1.1 PPR Maintenance Operations](#sec-8-2-10-7-1-1)
- [8.2.10.7.1.2 sPPR Maintenance Operation](#sec-8-2-10-7-1-2)
- [8.2.10.7.1.3 hPPR Maintenance Operation](#sec-8-2-10-7-1-3)
- [8.2.10.7.1.4 Memory Sparing Maintenance Operations](#sec-8-2-10-7-1-4)
- [8.2.10.7.1.5 Device Built-in Test Operations](#sec-8-2-10-7-1-5)
- [8.2.10.7.2 Features Associated with Maintenance Operations](#sec-8-2-10-7-2)
- [8.2.10.7.2.1 sPPR Feature Discovery and Configuration](#sec-8-2-10-7-2-1)
- [8.2.10.7.2.2 hPPR Feature Discovery and Configuration](#sec-8-2-10-7-2-2)
- [8.2.10.7.2.3 Memory Sparing Features](#sec-8-2-10-7-2-3)
- [8.2.10.8 PBR Component Command Set](#sec-8-2-10-8)
- [8.2.10.8.1 Identify PBR Component (Opcode 0700h)](#sec-8-2-10-8-1)
- [8.2.10.8.2 Claim Ownership (Opcode 0701h)](#sec-8-2-10-8-2)
- [8.2.10.8.3 Read CDAT (Opcode 0702h)](#sec-8-2-10-8-3)
- [8.2.10.9 Memory Device Command Sets](#sec-8-2-10-9)
- [8.2.10.9.1.1 Identify Memory Device (Opcode 4000h)](#sec-8-2-10-9-1-1)
- [8.2.10.9.2.1 Get Partition Info (Opcode 4100h)](#sec-8-2-10-9-2-1)
- [8.2.10.9.2.2 Set Partition Info (Opcode 4101h)](#sec-8-2-10-9-2-2)
- [8.2.10.9.2.3 Get LSA (Opcode 4102h)](#sec-8-2-10-9-2-3)
- [8.2.10.9.2.4 Set LSA (Opcode 4103h)](#sec-8-2-10-9-2-4)
- [8.2.10.9.3.1 Get Health Info (Opcode 4200h)](#sec-8-2-10-9-3-1)
- [8.2.10.9.3.2 Get Alert Configuration (Opcode 4201h)](#sec-8-2-10-9-3-2)
- [8.2.10.9.3.3 Set Alert Configuration (Opcode 4202h)](#sec-8-2-10-9-3-3)
- [8.2.10.9.3.4 Get Shutdown State (Opcode 4203h)](#sec-8-2-10-9-3-4)
- [8.2.10.9.3.5 Set Shutdown State (Opcode 4204h)](#sec-8-2-10-9-3-5)
- [8.2.10.9.4.1 Get Poison List (Opcode 4300h)](#sec-8-2-10-9-4-1)
- [8.2.10.9.4.2 Inject Poison (Opcode 4301h)](#sec-8-2-10-9-4-2)
- [8.2.10.9.4.3 Clear Poison (Opcode 4302h)](#sec-8-2-10-9-4-3)
- [8.2.10.9.4.4 Get Scan Media Capabilities (Opcode 4303h)](#sec-8-2-10-9-4-4)
- [8.2.10.9.4.5 Scan Media (Opcode 4304h)](#sec-8-2-10-9-4-5)
- [8.2.10.9.4.6 Get Scan Media Results (Opcode 4305h)](#sec-8-2-10-9-4-6)

## 🖼 本章图表 (Part C)

- Figure 8-X (page 676): Get Supported Logs Output Payload
- Figure 8-X (page 677): Command Effects Log structure
- Figure 8-X (page 678): CEL Entry Structure
- Figure 8-X (page 681): DDR5 Error Check Scrub (ECS) Log
- Figure 8-X (page 682): Media Test Capability Log
- Figure 8-X (page 685): Media Test Results Logs
- Figure 8-X (page 688): Error Signature
- Figure 8-X (page 690): Get Log Capabilities
- Figure 8-X (page 691): Clear Log / Populate Log Input Payload
- Figure 8-X (page 692): Get Supported Logs Sub-List
- Figure 8-X (page 693): Get Supported Features
- Figure 8-X (page 695): Get Feature Input/Output
- Figure 8-X (page 697): Set Feature Input Payload
- Figure 8-X (page 698): Metabits Storage Feature
- Figure 8-X (page 701): PPR Maintenance Operations
- Figure 8-X (page 704): Memory Sparing
- Figure 8-X (page 705): Device Built-in Test
- Figure 8-X (page 707): Test Parameters Entry
- Figure 8-X (page 708): Maintenance Operation Classes
- Figure 8-X (page 711): sPPR Feature
- Figure 8-X (page 713): hPPR Feature
- Figure 8-X (page 715): Memory Sparing Features
- Figure 8-X (page 716): PBR Component Command Set
- Figure 8-X (page 717): Claim Ownership
- Figure 8-X (page 718): Read CDAT
- Figure 8-X (page 719): CXL Defined Memory Device Command Opcodes
- Figure 8-X (page 722): Identify Memory Device Output Payload
- Figure 8-X (page 724): Get Partition Info
- Figure 8-X (page 725): Set Partition Info
- Figure 8-X (page 726): Get LSA / Set LSA
- Figure 8-X (page 727): Get Health Info Output Payload
- Figure 8-X (page 729): Get Alert Configuration
- Figure 8-X (page 731): Set Alert Configuration
- Figure 8-X (page 732): Get/Set Shutdown State
- Figure 8-X (page 733): Get Poison List
- Figure 8-X (page 735): Media Error Record

## 📊 本章表格 (Part C)

- Table 8-82: Get Supported Logs Output Payload
- Table 8-83: Get Supported Logs Supported Log Entry
- Table 8-84: Get Log Input Payload
- Table 8-85: Get Log Output Payload
- Table 8-86: CEL Output Payload
- Table 8-87: CEL Entry Structure
- Table 8-88: Component State Dump Log Population Methods and Triggers
- Table 8-89: Component State Dump Log Format
- Table 8-90: DDR5 Error Check Scrub (ECS) Log
- Table 8-91: Media Test Capability Log Output Payload
- Table 8-92: Media Test Capability Log Common Header
- Table 8-93: Media Test Capability Log Entry Structure
- Table 8-94: Media Test Results Short Log
- Table 8-95: Media Test Results Short Log Entry Common Header
- Table 8-96: Media Test Results Short Log Entry Structure
- Table 8-97: Media Test Results Long Log
- Table 8-98: Media Test Results Long Log Entry Common Header
- Table 8-99: Media Test Results Long Log Entry Structure
- Table 8-100: Error Signature
- Table 8-101: Get Log Capabilities Input Payload
- Table 8-102: Get Log Capabilities Output Payload
- Table 8-103: Clear Log Input Payload
- Table 8-104: Populate Log Input Payload
- Table 8-105: Get Supported Logs Sub-List Input Payload
- Table 8-106: Get Supported Logs Sub-List Output Payload
- Table 8-107: Get Supported Features Input Payload
- Table 8-108: Get Supported Features Output Payload
- Table 8-109: Get Supported Features Supported Feature Entry
- Table 8-110: Feature Attribute(s) Value after Reset
- Table 8-111: Get Feature Input Payload
- Table 8-112: Get Feature Output Payload
- Table 8-113: Set Feature Input Payload
- Table 8-114: Supported Feature Entry for Metabits Storage Feature
- Table 8-115: Metabits Storage Feature Readable Attributes
- Table 8-116: Metabits Storage Feature Writable Attributes
- Table 8-117: Perform Maintenance Input Payload
- Table 8-118: sPPR Maintenance Input Payload
- Table 8-119: hPPR Maintenance Input Payload
- Table 8-120: Memory Sparing Input Payload
- Table 8-121: Device Built-in Test Input Payload
- Table 8-122: Test Parameters
- Table 8-123: Common Configuration Parameters for Media Test Subclass
- Table 8-124: Test Parameters Entry Media Test Subclass
- Table 8-125: Maintenance Operation: Classes, Subclasses, and Feature UUIDs
- Table 8-126: Common Maintenance Operation Feature Format
- Table 8-127: Supported Feature Entry for the sPPR Feature
- Table 8-128: sPPR Feature Readable Attributes
- Table 8-129: sPPR Feature Writable Attributes
- Table 8-130: Supported Feature Entry for the hPPR Feature
- Table 8-131: hPPR Feature Readable Attributes
- Table 8-132: hPPR Feature Writable Attributes
- Table 8-133: Supported Feature Entry for the Memory Sparing Feature
- Table 8-134: Memory Sparing Feature Readable Attributes
- Table 8-135: Memory Sparing Feature Writable Attributes
- Table 8-136: Identify PBR Component Response Payload
- Table 8-137: Claim Ownership Request Payload
- Table 8-138: Claim Ownership Response Payload
- Table 8-139: Read CDAT Request Payload
- Table 8-140: Read CDAT Response Payload
- Table 8-141: CXL Defined Memory Device Command Opcodes
- Table 8-142: Identify Memory Device Output Payload
- Table 8-143: Get Partition Info Output Payload
- Table 8-144: Set Partition Info Input Payload
- Table 8-145: Get LSA Input Payload
- Table 8-146: Get LSA Output Payload
- Table 8-147: Set LSA Input Payload
- Table 8-148: Get Health Info Output Payload
- Table 8-149: Get Alert Configuration Output Payload
- Table 8-150: Set Alert Configuration Input Payload
- Table 8-151: Get Shutdown State Output Payload
- Table 8-152: Set Shutdown State Input Payload
- Table 8-153: Get Poison List Input Payload
- Table 8-154: Get Poison List Output Payload
- Table 8-155: Media Error Record
- Table 8-156: Inject Poison Input Payload
- Table 8-157: Clear Poison Input Payload
- Table 8-158: Get Scan Media Capabilities Input Payload
- Table 8-159: Get Scan Media Capabilities Output Payload
- Table 8-160: Scan Media Input Payload
- Table 8-161: Get Scan Media Results Output Payload

---

<a id="sec-8-2-10-5-2"></a>
## 8.2.10.5.2 Get Log (Opcode 0401h) | 获取日志 (操作码 0401h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve a log from the device, identified by a specific UUID. The host shall retrieve the size of the log first using the Get Supported Logs command, then issue enough of these commands to retrieve all the log information, incrementing the Log Offset each time. The device shall return Invalid Input if the Offset or Length fields attempt to access beyond the size of the log as reported by Get Supported Logs.</td><td style="background-color:#e8e8e8">从设备中检索由特定 UUID 标识的日志。主机应首先使用 Get Supported Logs 命令检索日志的大小,然后发出足够数量的此类命令以检索所有日志信息,每次递增 Log Offset。如果 Offset 或 Length 字段尝试访问超出 Get Supported Logs 所报告的日志大小范围,设备应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Invalid Log<br>• Media Disabled<br>• Busy</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Invalid Log(无效日志)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)</td></tr>
</tbody>
</table>

**Table 8-82. Get Supported Logs Output Payload | Get Supported Logs 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Number of Supported Log Entries: The number of Supported Log Entries returned in the output payload.</td><td>支持的日志条目数:输出负载中返回的 Supported Log Entries 数量。</td></tr>
<tr><td>02h</td><td>6</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Supported Log Entries: Device-specific list of supported log identifier UUIDs and the current size of each log.</td><td>支持的日志条目:设备特定的支持日志标识符 UUID 列表及每个日志的当前大小。</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> It is strongly recommended that the Get Supported Logs Sub-List (see Section 8.2.10.5.6) is supported by Components and used by software instead of Get Supported Logs so that requesters may control the output payload size, as needed. Type 3 Devices that implement support for the Get Supported Logs opcode on an MCTP-based CCI shall also support the Get Supported Logs Sub-List opcode.
>
> 强烈建议 Components 支持 Get Supported Logs Sub-List(参见 8.2.10.5.6 节)并由软件使用,以便请求者可以根据需要控制输出负载大小。在 MCTP-based CCI 上实现 Get Supported Logs 操作码支持的 Type 3 设备也应支持 Get Supported Logs Sub-List 操作码。

**Table 8-83. Get Supported Logs Supported Log Entry | Get Supported Logs 支持的日志条目**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log for which to retrieve data. The following Log Identifier UUIDs are defined in this specification:<br>• 0da9c0b5-bf41-4b78-8f79-96b1623b3f17 – Command Effects Log (CEL)<br>• 5e1819d9-11a9-400c-811f-d60719403d86 – Vendor Debug Log<br>• b3fab4cf-01b6-4332-943e-5e9962f23567 – Component State Dump Log<br>• f1720d60-a7a9-4306-a003-11948f9e077c – DDR5 Error Check Scrub (ECS) Log<br>• e6dfa32c-d13e-4a5c-8ca8-99bebbf731a4 – Media Test Capability Log<br>• 2c255522-8ce4-11ec-b909-0242ac120002 – Media Test Results Short Log<br>• c1fe0b3e-7a00-448e-a24e-a6aabbfe587a – Media Test Results Long Log</td><td>日志标识符(UUID):表示要检索数据的日志的 UUID。本规范定义了以下 Log Identifier UUID:<br>• 0da9c0b5-bf41-4b78-8f79-96b1623b3f17 – Command Effects Log (CEL)<br>• 5e1819d9-11a9-400c-811f-d60719403d86 – Vendor Debug Log(厂商调试日志)<br>• b3fab4cf-01b6-4332-943e-5e9962f23567 – Component State Dump Log<br>• f1720d60-a7a9-4306-a003-11948f9e077c – DDR5 Error Check Scrub (ECS) Log<br>• e6dfa32c-d13e-4a5c-8ca8-99bebbf731a4 – Media Test Capability Log<br>• 2c255522-8ce4-11ec-b909-0242ac120002 – Media Test Results Short Log<br>• c1fe0b3e-7a00-448e-a24e-a6aabbfe587a – Media Test Results Long Log</td></tr>
<tr><td>10h</td><td>4</td><td>Log Size: The maximum number of bytes of log data available to retrieve for the log identifier.</td><td>日志大小:可为该日志标识符检索的日志数据的最大字节数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Supported Logs supported log entry structure (page 676) ｜ Get Supported Logs 支持的日志条目结构
>
> <img src="figures/chapter_08/page_0676.png" alt="Figure 8-X page 676" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0676.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-2"></a>
### 8.2.10.5.2.2 Vendor Debug Log | 厂商调试日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>All devices that support a debug log shall support the Vendor Debug Log to allow the log to be accessed through a common host driver, for any device, with Log Identifier of:<br>• 5e1819d9-11a9-400c-811f-d60719403d86</td><td style="background-color:#e8e8e8">所有支持调试日志的设备应支持 Vendor Debug Log,以便通过通用主机驱动程序访问任何设备的日志,其 Log Identifier 为:<br>• 5e1819d9-11a9-400c-811f-d60719403d86</td></tr>
<tr><td>The contents of the output payload are vendor specific.</td><td style="background-color:#e8e8e8">输出负载的内容由厂商特定定义。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Vendor Debug Log (page 678) ｜ 厂商调试日志
>
> <img src="figures/chapter_08/page_0678.png" alt="Figure 8-X page 678" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0678.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-3"></a>
### 8.2.10.5.2.3 Component State Dump Log | 组件状态转储日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Log Identifier: b3fab4cf-01b6-4332-943e-5e9962f23567</td><td style="background-color:#e8e8e8">日志标识符:b3fab4cf-01b6-4332-943e-5e9962f23567</td></tr>
<tr><td>The Component State Dump Log is an optional method for allowing vendor specific state information to be extracted using standard drivers.</td><td style="background-color:#e8e8e8">Component State Dump Log 是一种可选方法,允许使用标准驱动程序提取厂商特定的状态信息。</td></tr>
</tbody>
</table>

**Table 8-87. CEL Entry Structure | CEL 条目结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Opcode: The command opcode.</td><td>操作码:命令操作码。</td></tr>
<tr><td>02h</td><td>2</td><td>Command Effect: Bitmask that contains one or more effects for the command opcode.<br>• Bit[0]: Configuration Change after Cold Reset<br>• Bit[1]: Immediate Configuration Change<br>• Bit[2]: Immediate Data Change<br>• Bit[3]: Immediate Policy Change<br>• Bit[4]: Immediate Log Change<br>• Bit[5]: Security State Change<br>• Bit[6]: Background Operation<br>• Bit[7]: Secondary Mailbox Supported<br>• Bit[8]: Request Abort Background Operation Supported<br>• Bit[9]: CEL[11:10] Valid<br>• Bit[10]: Configuration Change after Conventional Reset<br>• Bit[11]: Configuration Change after CXL Reset<br>• Bits[15:12]: Reserved: Shall be cleared to 0h.</td><td>命令效果:包含命令操作码的一个或多个效果的位掩码。<br>• Bit[0]:Cold Reset 后的配置更改<br>• Bit[1]:立即配置更改<br>• Bit[2]:立即数据更改<br>• Bit[3]:立即策略更改<br>• Bit[4]:立即日志更改<br>• Bit[5]:安全状态更改<br>• Bit[6]:后台操作<br>• Bit[7]:支持 Secondary Mailbox<br>• Bit[8]:支持 Request Abort Background Operation<br>• Bit[9]:CEL[11:10] 有效<br>• Bit[10]:Conventional Reset 后的配置更改<br>• Bit[11]:CXL Reset 后的配置更改<br>• Bits[15:12]:保留:应清零为 0h。</td></tr>
</tbody>
</table>

> **Figure 8-X.** CEL Entry Structure (page 678) ｜ CEL 条目结构
>
> <img src="figures/chapter_08/page_0678.png" alt="Figure 8-X page 678" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0678.png)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Component State Dump Log can be populated in two ways:<br>• Auto populate<br>• Manual populate using Populate Log</td><td style="background-color:#e8e8e8">Component State Dump Log 可通过两种方式填充:<br>• Auto populate(自动填充)<br>• Manual populate using Populate Log(使用 Populate Log 手动填充)</td></tr>
<tr><td>A component that supports the Component State Dump Log shall support at least one of the above methods.</td><td style="background-color:#e8e8e8">支持 Component State Dump Log 的组件应至少支持上述方法之一。</td></tr>
<tr><td>The two methods and their associated trigger requirements are detailed in Table 8-88. The Component State Dump Log shall be populated by a given method if the trigger occurs, and the logical AND of all the conditions for that trigger is true.</td><td style="background-color:#e8e8e8">这两种方法及其相关触发要求详见表 8-88。如果触发器发生且该触发器的所有条件的逻辑 AND 为真,则 Component State Dump Log 应通过给定方法填充。</td></tr>
<tr><td>The trigger for the auto populate method is vendor specific, but one example may be a severe internal error in the component.</td><td style="background-color:#e8e8e8">Auto populate 方法的触发器由厂商特定定义,但一个示例可能是组件中的严重内部错误。</td></tr>
<tr><td>When a population method triggers and all required conditions are met, any existing Component State Dump Data is cleared before populating the new log contents.</td><td style="background-color:#e8e8e8">当 population 方法触发且满足所有必需条件时,任何现有的 Component State Dump Data 将在填充新日志内容之前被清除。</td></tr>
<tr><td>The log contents should persist across cold reset. The component shall indicate whether the log persists across cold reset using the Persistent Across Cold Reset bit in the Get Log Capabilities Output Payload.</td><td style="background-color:#e8e8e8">日志内容应在冷复位后保留。组件应使用 Get Log Capabilities Output Payload 中的 Persistent Across Cold Reset 位来指示日志是否在冷复位后保留。</td></tr>
<tr><td>If the component has Component State Dump Data available to be reported in the Component State Dump Log after a subsequent reset, the Component State Dump Log contents shall be available when the Mailbox Interfaces Ready bit in the Memory Device Status register is set to 1.</td><td style="background-color:#e8e8e8">如果组件在后续复位后有 Component State Dump Data 可在 Component State Dump Log 中报告,则当 Memory Device Status 寄存器中的 Mailbox Interfaces Ready 位设置为 1 时,Component State Dump Log 内容应可用。</td></tr>
<tr><td>To handle corner cases related to an existing Component State Dump Log being overwritten by an Auto Populate trigger while host software is reading the existing contents of the log, host software must begin each Component State Dump Log fetch sequence by issuing a Get Log command with Offset = 0, followed by zero or more Get Log commands with nonzero offset. If the component is reset, host software must start a new fetch sequence.</td><td style="background-color:#e8e8e8">为了处理与现有 Component State Dump Log 在主机软件读取日志现有内容时被 Auto Populate 触发器覆盖相关的边缘情况,主机软件必须通过发出 Offset = 0 的 Get Log 命令来开始每个 Component State Dump Log 提取序列,然后再发出零个或多个具有非零 offset 的 Get Log 命令。如果组件被重置,主机软件必须开始新的提取序列。</td></tr>
<tr><td>If a Get Log command with nonzero Offset is received requesting the Component State Dump Log, the component shall apply the first applicable case from the following list:<br>• Return Invalid Input if the component has not previously returned Success for a Get Log command with Offset = 0 requesting the Component State Dump Log.<br>• Return Interrupted if the contents of the Component State Dump Log have changed since the last time the component returned Success for a Get Log command with Offset = 0 requesting the Component State Dump Log.<br>• Return Success and provide the log contents of the specified offset corresponding to the state of the Component State Dump Log when the current fetch sequence began (i.e., when the last Get Log command with Offset = 0 requesting the Component State Dump Log was completed with a return code of Success).</td><td style="background-color:#e8e8e8">如果收到具有非零 Offset 的 Get Log 命令请求 Component State Dump Log,组件应从以下列表中应用第一个适用的情况:<br>• 如果组件之前未对请求 Component State Dump Log 且 Offset = 0 的 Get Log 命令返回 Success,则返回 Invalid Input。<br>• 如果自组件上次对请求 Component State Dump Log 且 Offset = 0 的 Get Log 命令返回 Success 以来,Component State Dump Log 的内容已更改,则返回 Interrupted。<br>• 返回 Success 并提供与当前提取序列开始时 Component State Dump Log 状态相对应的指定 offset 的日志内容。</td></tr>
</tbody>
</table>

**Table 8-88. Component State Dump Log Population Methods and Triggers | Component State Dump Log 填充方法和触发器**

<table>
<thead>
<tr><th>Method</th><th>Trigger</th><th>Condition</th><th>Condition Reference</th></tr>
</thead>
<tbody>
<tr><td>Auto Populate</td><td>Vendor-specific</td><td>Auto Populate Trigger Count Since Clear = 0</td><td>Table 8-89. Component State Dump Log Format</td></tr>
<tr><td></td><td></td><td>Auto Populate Supported = 1</td><td>Table 8-102. Get Log Capabilities Output Payload</td></tr>
<tr><td>Manual Populate</td><td>Populate Log command received</td><td>Log Identifier = b3fab4cf-01b6-4332-943e-5e9962f23567</td><td>Table 8-104. Populate Log Input Payload</td></tr>
<tr><td></td><td></td><td>Populate Log Supported = 1</td><td>Table 8-102. Get Log Capabilities Output Payload</td></tr>
</tbody>
</table>

> **Figure 8-X.** Component State Dump Log (page 679) ｜ Component State Dump Log
>
> <img src="figures/chapter_08/page_0679.png" alt="Figure 8-X page 679" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0679.png)

**Table 8-89. Component State Dump Log Format | Component State Dump Log 格式**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Component State Dump Data Length: Length of the Component State Dump Data field in bytes.</td><td>Component State Dump Data 长度(以字节为单位):Component State Dump Data 字段的长度。</td></tr>
<tr><td>04h</td><td>1</td><td>Auto Populate Trigger Count Since Clear: Number of Auto Populate triggers since last clear. Tracking is optional. Saturates at FFh.</td><td>自清除以来的 Auto Populate 触发计数:自上次清除 Component State Dump Log 以来遇到 Auto Populate 触发器的次数。可选跟踪。在 FFh 处饱和。</td></tr>
<tr><td>05h</td><td>1</td><td>Event Log: The Event Log, as defined in Table 8-64 (Get Event Records Input Payload), containing the Associated Event Record Handle.</td><td>Event Log:如表 8-64(Get Event Records Input Payload)所定义的事件日志,包含 Associated Event Record Handle。</td></tr>
<tr><td>06h</td><td>2</td><td>Associated Event Record Handle: The Event Record Handle corresponding to the Auto Populate trigger that generated the Component State Dump Data.</td><td>Associated Event Record Handle:与生成 Component State Dump Data 的 Auto Populate 触发器关联的 Event Record 对应的 Event Record Handle。</td></tr>
<tr><td>08h</td><td>8</td><td>Timestamp: The Timestamp at the time the Component State Dump Data was generated.</td><td>时间戳:Component State Dump Data 生成时的时间戳。</td></tr>
<tr><td>10h</td><td>10h</td><td>Component State Dump Format UUID: Optional value to uniquely identify the format of the Component State Dump Data field. A value of all 0s indicates that the format is not indicated.</td><td>Component State Dump Format UUID:用于唯一标识 Component State Dump Data 字段格式的可选值。全为 0 表示未指示格式。</td></tr>
<tr><td>20h</td><td>4</td><td>Flags<br>• Bit[0]: Auto Populate Data<br>• Bits[31:1]: Reserved</td><td>标志位<br>• Bit[0]:Auto Populate Data<br>• Bits[31:1]:保留</td></tr>
<tr><td>24h</td><td>1Ch</td><td>Reserved</td><td>保留</td></tr>
<tr><td>40h</td><td>Varies</td><td>Component State Dump Data: Vendor specific.</td><td>Component State Dump Data:厂商特定。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Component State Dump Log Format (page 680) ｜ Component State Dump Log 格式
>
> <img src="figures/chapter_08/page_0680.png" alt="Figure 8-X page 680" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0680.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-4"></a>
### 8.2.10.5.2.4 DDR5 Error Check Scrub (ECS) Log | DDR5 错误检查清除 (ECS) 日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Log Identifier: f1720d60-a7a9-4306-a003-11948f9e077c</td><td style="background-color:#e8e8e8">日志标识符:f1720d60-a7a9-4306-a003-11948f9e077c</td></tr>
<tr><td>DDR5 ECS Log allows the host to observe the ECS operation results. The format of the DDR5 ECS Log is shown in Table 8-90.</td><td style="background-color:#e8e8e8">DDR5 ECS Log 允许主机观察 ECS 操作结果。DDR5 ECS Log 的格式如表 8-90 所示。</td></tr>
</tbody>
</table>

**Table 8-90. DDR5 Error Check Scrub (ECS) Log | DDR5 错误检查清除 (ECS) 日志**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Common Header<br>• Bits[9:0]: Total Number of Entries<br>• Bit[10]: If 0, Component ID field is vendor specific. If 1, the format is defined in Table 8-56.<br>• Bits[12:11]: Entry Type: 00b = Per DRAM; 01b = Per Memory Media FRU; All other encodings reserved.<br>• Bits[31:13]: Reserved</td><td>Common Header<br>• Bits[9:0]:条目总数<br>• Bit[10]:如果为 0,Component ID 字段由厂商定义。如果为 1,格式由表 8-56 定义。<br>• Bits[12:11]:条目类型:00b = Per DRAM;01b = Per Memory Media FRU;所有其他编码保留。<br>• Bits[31:13]:保留</td></tr>
<tr><td>04h</td><td>10h</td><td>Entry 1 Component Identifier</td><td>条目 1 组件标识符</td></tr>
<tr><td>14h</td><td>2</td><td>Entry 1 DDR5 ECS Configurations<br>• Bits[2:0]: ECS Threshold Count per Gb of Memory Cells: 011b = 256 (default); 100b = 1024; 101b = 4096; All other encodings are reserved<br>• Bit[3]: Codeword/Row Count Mode: 0 = ECS counts rows with errors; 1 = ECS counts codewords with errors<br>• Bits[15:4]: Reserved</td><td>条目 1 DDR5 ECS 配置<br>• Bits[2:0]:每 Gb 内存单元的 ECS 阈值计数:011b = 256(默认);100b = 1024;101b = 4096;所有其他编码保留<br>• Bit[3]:码字/行计数模式:0 = ECS 计数有错误的行;1 = ECS 计数有错误的码字<br>• Bits[15:4]:保留</td></tr>
<tr><td>16h</td><td>10h</td><td>Entry 1 Error Count and Address Information<br>• Bit[0]: Error Found<br>• Bits[7:1]: Reserved<br>• Bits[23:8]: Error Count or the Number of Rows or Codeword Errors<br>• Bits[31:24]: Max Row Error Count<br>• Bits[95:32]: Address with Max Errors<br>• Bits[127:96]: Reserved</td><td>条目 1 错误计数和地址信息<br>• Bit[0]:发现错误<br>• Bits[7:1]:保留<br>• Bits[23:8]:错误计数或行/码字错误数<br>• Bits[31:24]:最大行错误计数<br>• Bits[95:32]:错误最多的地址<br>• Bits[127:96]:保留</td></tr>
<tr><td>04h+((n-1)*22h)</td><td>10h</td><td>Entry n Component Identifier</td><td>条目 n 组件标识符</td></tr>
<tr><td>14h+((n-1)*22h)</td><td>2</td><td>Entry n DDR5 ECS Configurations</td><td>条目 n DDR5 ECS 配置</td></tr>
<tr><td>16h+((n-1)*22h)</td><td>10h</td><td>Entry n Error Count and Address Information</td><td>条目 n 错误计数和地址信息</td></tr>
</tbody>
</table>

> **Figure 8-X.** DDR5 ECS Log (page 681-682) ｜ DDR5 ECS 日志
>
> <img src="figures/chapter_08/page_0681.png" alt="Figure 8-X page 681" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0681.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-5"></a>
### 8.2.10.5.2.5 Media Test Capability Log | 介质测试能力日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Media Test Capability Log is a variable-length log structure that conveys the attributes of the different media tests that the CXL device supports. It is composed of a common header (see Table 8-91) and Media Test Capability Log Entries (see Table 8-93) for each supported test.</td><td style="background-color:#e8e8e8">Media Test Capability Log 是一种可变长度的日志结构,用于传达 CXL 设备支持的不同介质测试的属性。它由 common header(参见表 8-91)和每个受支持测试的 Media Test Capability Log Entries(参见表 8-93)组成。</td></tr>
<tr><td>Table 8-92 describes the attributes that are common to all the tests that the device supports (e.g., Error Signature List Size, Media Test Result Long, and Short Log versions and Capabilities flags).</td><td style="background-color:#e8e8e8">表 8-92 描述了设备支持的所有测试共有的属性(例如,Error Signature List Size、Media Test Result Long 和 Short Log 版本以及 Capabilities 标志)。</td></tr>
</tbody>
</table>

**Table 8-91. Media Test Capability Log Output Payload | Media Test Capability Log 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>16</td><td>Common Header: Reports attributes applicable to all the tests and general capabilities of the device.</td><td>Common Header:报告适用于所有测试的属性以及设备的一般能力。</td></tr>
<tr><td>10h</td><td>16</td><td>Test 1 Media Test Capability Log Entry</td><td>测试 1 的 Media Test Capability Log 条目</td></tr>
<tr><td>20h</td><td>16</td><td>Test 2 Media Test Capability Log Entry</td><td>测试 2 的 Media Test Capability Log 条目</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>(16+16*(n-1))h</td><td>16</td><td>Test n Media Test Capability Log Entry</td><td>测试 n 的 Media Test Capability Log 条目</td></tr>
</tbody>
</table>

**Table 8-92. Media Test Capability Log Common Header | Media Test Capability Log Common Header**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Supported Tests: Total number of test types that the device supports.</td><td>支持的测试数:设备支持的测试类型总数。</td></tr>
<tr><td>01h</td><td>4</td><td>Total Number of Error Signatures</td><td>错误签名总数</td></tr>
<tr><td>05h</td><td>1</td><td>Media Test Result Long Log Version</td><td>Media Test Result Long Log 版本</td></tr>
<tr><td>06h</td><td>1</td><td>Media Test Result Short Log Version</td><td>Media Test Result Short Log 版本</td></tr>
<tr><td>07h</td><td>1</td><td>Capabilities: Bit[0]: Data ECC Disablement Capability; Bit[1]: Metadata ECC Disablement Capability; Bit[2]: Data and Metadata ECC Disablement Capability; Bit[3]: Metadata Area Testing Capability; Bits[7:4]: Reserved</td><td>能力:Bit[0]:数据 ECC 禁用能力;Bit[1]:元数据 ECC 禁用能力;Bit[2]:数据和元数据 ECC 禁用能力;Bit[3]:元数据区域测试能力;Bits[7:4]:保留</td></tr>
<tr><td>08h</td><td>8</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Capability Log (page 682-683) ｜ Media Test Capability Log
>
> <img src="figures/chapter_08/page_0682.png" alt="Figure 8-X page 682" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0682.png)

**Table 8-93. Media Test Capability Log Entry Structure | Media Test Capability Log Entry 结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: Unique ID to identify the Test.</td><td>Test ID:用于标识测试的唯一 ID。</td></tr>
<tr><td>02h</td><td>1</td><td>Algorithm: Media test algorithm supported.</td><td>算法:支持的介质测试算法。</td></tr>
<tr><td>03h</td><td>1</td><td>Execution Time: Maximum test execution time per GB.</td><td>执行时间:每 GB 的最大测试执行时间。</td></tr>
<tr><td>04h</td><td>2</td><td>Capabilities: Bit[0]: Address Configurable Flag; Bit[1]: Inverse Pattern Support; Bit[2]: Exit on Uncorrectable Error; Bit[3]: Error Count Threshold Programmable; Bit[4]: Update Poison List on Uncorrectable Error; Bits[8:5]: Addressing Mode</td><td>能力:Bit[0]:地址可配置标志;Bit[1]:反码支持;Bit[2]:遇到不可纠正错误时退出;Bit[3]:错误计数阈值可编程;Bit[4]:在不可纠正错误时更新 Poison List;Bits[8:5]:寻址模式</td></tr>
<tr><td>06h</td><td>2</td><td>Supported Patterns: Bitmap of supported 64B patterns.</td><td>支持的模式:支持的 64B 模式位图。</td></tr>
<tr><td>08h</td><td>1</td><td>PRBS Length: Length of the PRBS sequence.</td><td>PRBS 长度:PRBS 序列的长度。</td></tr>
<tr><td>09h</td><td>7</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>For each media test that the device supports, an individual Media Test Capability Log Entry shall be defined. A single test shall be described by the fields defined in Table 8-93, comprising the Test ID, the Algorithm of the Test, the estimated Execution time per GB, etc.</td><td style="background-color:#e8e8e8">对于设备支持的每个介质测试,应定义一个单独的 Media Test Capability Log Entry。单个测试应由表 8-93 中定义的字段描述,包括 Test ID、测试的 Algorithm、每 GB 的估计 Execution time 等。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Capability Log Entry (page 683-684) ｜ Media Test Capability Log Entry
>
> <img src="figures/chapter_08/page_0683.png" alt="Figure 8-X page 683" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0683.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-6"></a>
### 8.2.10.5.2.6 Media Test Results Logs | 介质测试结果日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Media Test Results Logs are variable-length logs that provide the results of one or more Media Tests. Two types of logs are available:<br>• Media Test Results Short Log: Status info and results of the execute tests (see Table 8-94)<br>• Media Test Results Long Log: Detailed error information and error signatures of the executed tests (see Table 8-97)</td><td style="background-color:#e8e8e8">Media Test Results Logs 是可变长度的日志,用于提供一项或多项 Media Tests 的结果。有两种类型的日志可用:<br>• Media Test Results Short Log:已执行测试的状态信息和结果(参见表 8-94)<br>• Media Test Results Long Log:已执行测试的详细错误信息和错误签名(参见表 8-97)</td></tr>
<tr><td>Media Test Result Logs are produced at the end of the execution of the tests and are cleared when a new test starts or when the Clear Log command is issued.</td><td style="background-color:#e8e8e8">Media Test Result Logs 在测试执行结束时生成,并在开始新测试或发出 Clear Log 命令时被清除。</td></tr>
<tr><td>Media Test Results Short Log enumerates the results of the tests executed by the CXL device.</td><td style="background-color:#e8e8e8">Media Test Results Short Log 枚举 CXL 设备执行的测试结果。</td></tr>
<tr><td>Each Media Test Results Short Log Entry contains the results of the test executed (see Table 8-96). They are preceded by a common header described in Table 8-95.</td><td style="background-color:#e8e8e8">每个 Media Test Results Short Log Entry 包含已执行测试的结果(参见表 8-96)。它们前面是表 8-95 中描述的 common header。</td></tr>
</tbody>
</table>

**Table 8-94. Media Test Results Short Log | Media Test Results Short Log**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Common Header: Common output information from test execution.</td><td>Common Header:测试执行的通用输出信息。</td></tr>
<tr><td>10h</td><td>20h</td><td>Test 1 Media Test Results Short Log Entry</td><td>测试 1 的 Media Test Results Short Log Entry</td></tr>
<tr><td>30h</td><td>20h</td><td>Test 2 Media Test Results Short Log Entry</td><td>测试 2 的 Media Test Results Short Log Entry</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>(10h+20h*(n-1))h</td><td>20h</td><td>Test n Media Test Results Short Log Entry</td><td>测试 n 的 Media Test Results Short Log Entry</td></tr>
</tbody>
</table>

**Table 8-95. Media Test Results Short Log Entry Common Header | Media Test Results Short Log Entry Common Header**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Tests Executed</td><td>已执行的测试数</td></tr>
<tr><td>01h</td><td>1</td><td>Version: This field shall be set to 01h.</td><td>版本:此字段应设置为 01h。</td></tr>
<tr><td>02h</td><td>1</td><td>Result: 00h = All tests completed successfully; 01h = At least one test completed with failure; 02h = Test execution was interrupted by a Request Abort Background Operation command (all tests that completed, before abort, ended successfully); 03h = Test execution was interrupted by a Request Abort Background Operation command (at least one test completed with failure); All other encodings are reserved</td><td>结果:00h = 所有测试成功完成;01h = 至少一个测试失败完成;02h = 测试执行被 Request Abort Background Operation 命令中断(中止前完成的所有测试均成功结束);03h = 测试执行被 Request Abort Background Operation 命令中断(中止前至少一个测试失败);所有其他编码保留</td></tr>
<tr><td>03h</td><td>Dh</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Results Short Log (page 685) ｜ Media Test Results Short Log
>
> <img src="figures/chapter_08/page_0685.png" alt="Figure 8-X page 685" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0685.png)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Media Test Results Long Log reports the same fields defined for the Short version. It also includes the capacity tested by the device and the error signature, which consists of:<br>• Test iteration in which the error occurred<br>• Failed DPA with a flag that indicates the error type (i.e., uncorrectable or correctable)<br>• Memory component address following the format defined in the DRAM Event Record</td><td style="background-color:#e8e8e8">Media Test Results Long Log 报告为 Short 版本定义的相同字段。它还包括设备测试的容量和错误签名,后者包括:<br>• 发生错误的测试迭代<br>• 失败的 DPA 及指示错误类型的标志(即,不可纠正或可纠正)<br>• 遵循 DRAM Event Record 中定义的格式的内存组件地址</td></tr>
<tr><td>When using the Media Test Results Long Log, two reporting options are available:<br>• Complete: Count and report all the error signatures (with and without threshold programmed)<br>• Single error signature: If error count threshold is set, only the signature of the first error after the threshold is exceeded is reported. If error count threshold is not set, only the signature of the first error encountered is reported.</td><td style="background-color:#e8e8e8">使用 Media Test Results Long Log 时,有两种报告选项可用:<br>• Complete(完整):计数并报告所有错误签名(无论是否编程了阈值)<br>• Single error signature(单个错误签名):如果设置了错误计数阈值,则仅报告超过阈值后的第一个错误的签名。如果未设置错误计数阈值,则仅报告遇到的第一个错误的签名。</td></tr>
<tr><td>The device tracks the error information in the Error Signature Lists. The total number of Error Signatures cannot exceed the value indicated by the Total Number of Error Signatures field in the Media Test Capability Log (see Table 8-91). If the Error Signature Configuration bit (see Table 8-123) is set and the total number of errors exceeds the Total Number of Error Signatures, bit[1] in the Flags field shall be set and the test execution shall be interrupted by the device. The test may be resumed from the point at which it was interrupted due to the lack of resources to log the error signatures.</td><td style="background-color:#e8e8e8">设备在 Error Signature Lists 中跟踪错误信息。Error Signatures 的总数不能超过 Media Test Capability Log(参见表 8-91)中 Total Number of Error Signatures 字段所指示的值。如果设置了 Error Signature Configuration 位(参见表 8-123),且错误总数超过 Total Number of Error Signatures,则应设置 Flags 字段中的 bit[1],并且测试执行应被设备中断。可以从由于缺乏记录错误签名的资源而被中断的点恢复测试。</td></tr>
</tbody>
</table>

**Table 8-96. Media Test Results Short Log Entry Structure | Media Test Results Short Log Entry 结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: ID of the test.</td><td>Test ID:测试的 ID。</td></tr>
<tr><td>02h</td><td>8</td><td>Start Time: Expressed as timestamp.</td><td>Start Time:以时间戳表示。</td></tr>
<tr><td>0Ah</td><td>8</td><td>End Time: Expressed as timestamp.</td><td>End Time:以时间戳表示。</td></tr>
<tr><td>12h</td><td>1</td><td>Result: 00h = Completed with success; 01h = Completed with failure; 02h = Aborted by a Request Abort Background Operation command; All other encodings are reserved</td><td>结果:00h = 成功完成;01h = 失败完成;02h = 被 Request Abort Background Operation 命令中止;所有其他编码保留</td></tr>
<tr><td>13h</td><td>1</td><td>Flags: Bit[0]: Error Signature List Overflow; Bits[7:1]: Reserved</td><td>标志位:Bit[0]:错误签名列表溢出;Bits[7:1]:保留</td></tr>
<tr><td>14h</td><td>4</td><td>Uncorrectable Error Count: Total number of uncorrectable memory errors that the device detected during the test.</td><td>不可纠正错误计数:设备在测试期间检测到的不可纠正内存错误总数。</td></tr>
<tr><td>18h</td><td>4</td><td>Correctable Error Count: Total number of correctable memory errors that the device detected during the test.</td><td>可纠正错误计数:设备在测试期间检测到的可纠正内存错误总数。</td></tr>
<tr><td>1Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Results Long Log (page 686-689) ｜ Media Test Results Long Log
>
> <img src="figures/chapter_08/page_0686.png" alt="Figure 8-X page 686" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0686.png)

**Table 8-97. Media Test Results Long Log | Media Test Results Long Log**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Common Header: Common output information from test execution.</td><td>Common Header:测试执行的通用输出信息。</td></tr>
<tr><td>10h</td><td>variable</td><td>Test 1 Media Test Results Long Log Entry</td><td>测试 1 的 Media Test Results Long Log Entry</td></tr>
<tr><td>variable</td><td>variable</td><td>Test 2 Media Test Results Long Log Entry</td><td>测试 2 的 Media Test Results Long Log Entry</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>variable</td><td>variable</td><td>Test n Media Test Results Long Log Entry</td><td>测试 n 的 Media Test Results Long Log Entry</td></tr>
</tbody>
</table>

**Table 8-98. Media Test Results Long Log Entry Common Header | Media Test Results Long Log Entry Common Header**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Tests Executed</td><td>已执行的测试数</td></tr>
<tr><td>01h</td><td>1</td><td>Version: This field shall be set to 1.</td><td>版本:此字段应设置为 1。</td></tr>
<tr><td>02h</td><td>1</td><td>Result: 00h = All tests completed successfully; 01h = At least one test completed with failure; 02h = Test execution interrupted (all completed tests ended successfully); 03h = Test execution interrupted (at least one test failed); All other encodings are reserved</td><td>结果:00h = 所有测试成功完成;01h = 至少一个测试失败完成;02h = 测试执行中断(所有已完成的测试均成功);03h = 测试执行中断(至少一个测试失败);所有其他编码保留</td></tr>
<tr><td>03h</td><td>0Dh</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

**Table 8-99. Media Test Results Long Log Entry Structure | Media Test Results Long Log Entry 结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: ID of the test.</td><td>Test ID:测试的 ID。</td></tr>
<tr><td>02h</td><td>8</td><td>Start Time</td><td>Start Time(开始时间)</td></tr>
<tr><td>0Ah</td><td>8</td><td>End Time</td><td>End Time(结束时间)</td></tr>
<tr><td>12h</td><td>1</td><td>Result: 00h = Completed with success; 01h = Completed with failure; 02h = Aborted; All other encodings reserved</td><td>结果:00h = 成功完成;01h = 失败完成;02h = 中止;所有其他编码保留</td></tr>
<tr><td>13h</td><td>1</td><td>Flags: Bit[0]: Error Signature List Overflow; Bits[7:1]: Reserved</td><td>标志位:Bit[0]:错误签名列表溢出;Bits[7:1]:保留</td></tr>
<tr><td>14h</td><td>4</td><td>Uncorrectable Error Count</td><td>不可纠正错误计数</td></tr>
<tr><td>18h</td><td>4</td><td>Correctable Error Count</td><td>可纠正错误计数</td></tr>
<tr><td>1Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>8</td><td>Capacity Tested: Expressed in multiples of 256 MB.</td><td>Capacity Tested:以 256 MB 的倍数表示。</td></tr>
<tr><td>28h</td><td>4</td><td>Number of Error Signatures: Total number of error signatures reported by the device in the test.</td><td>Number of Error Signatures:设备在测试中报告的错误签名总数。</td></tr>
<tr><td>2Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>30h</td><td>50h</td><td>Error Signature 1</td><td>Error Signature 1</td></tr>
<tr><td>80h</td><td>50h</td><td>Error Signature 2</td><td>Error Signature 2</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>30h+((N-1)*50)h</td><td>50h</td><td>Error Signature N</td><td>Error Signature N</td></tr>
</tbody>
</table>

**Table 8-100. Error Signature | Error Signature**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Iteration: This field indicates the test iteration in which the error occurred.</td><td>Iteration:此字段指示发生错误的测试迭代。</td></tr>
<tr><td>02h</td><td>8</td><td>Physical Address: The physical address at which the error occurred during the test execution.<br>• Bit[0]: Volatile: 0 = DPA is within the persistent memory range; 1 = DPA field is within the volatile memory range<br>• Bits[2:1]: Error Type: 00b = Uncorrectable; 01b = Correctable; All other encodings reserved<br>• Bit[3]: Inverse Pattern<br>• Bits[5:4]: Reserved<br>• Bits[63:6]: DPA</td><td>Physical Address:测试执行期间发生错误的物理地址。<br>• Bit[0]:Volatile:0 = DPA 在持久性内存范围内;1 = DPA 字段在易失性内存范围内<br>• Bits[2:1]:Error Type:00b = 不可纠正;01b = 可纠正;所有其他编码保留<br>• Bit[3]:反码<br>• Bits[5:4]:保留<br>• Bits[63:6]:DPA</td></tr>
<tr><td>0Ah</td><td>2</td><td>Validity Flags: Indicators of which fields are valid within the returned data.<br>• Bit[0]: Channel field is valid<br>• Bit[1]: Rank field is valid<br>• Bit[2]: Nibble Mask field is valid<br>• Bit[3]: Bank Group field is valid<br>• Bit[4]: Bank field is valid<br>• Bit[5]: Row field is valid<br>• Bit[6]: Column field is valid<br>• Bit[7]: Correction Mask field is valid<br>• Bit[8]: Component Identifier field is valid<br>• Bit[9]: Component Identifier format governed by Table 8-56<br>• Bit[10]: Sub-channel field is valid<br>• Bits[15:11]: Reserved</td><td>Validity Flags:指示返回数据中哪些字段有效。<br>• Bit[0]:Channel 字段有效<br>• Bit[1]:Rank 字段有效<br>• Bit[2]:Nibble Mask 字段有效<br>• Bit[3]:Bank Group 字段有效<br>• Bit[4]:Bank 字段有效<br>• Bit[5]:Row 字段有效<br>• Bit[6]:Column 字段有效<br>• Bit[7]:Correction Mask 字段有效<br>• Bit[8]:Component Identifier 字段有效<br>• Bit[9]:Component Identifier 格式由表 8-56 规定<br>• Bit[10]:Sub-channel 字段有效<br>• Bits[15:11]:保留</td></tr>
<tr><td>0Ch</td><td>1</td><td>Channel</td><td>Channel(通道)</td></tr>
<tr><td>0Dh</td><td>1</td><td>Rank</td><td>Rank(秩)</td></tr>
<tr><td>0Eh</td><td>3</td><td>Nibble Mask: Identifies one or more nibbles in error on the memory bus producing the event.</td><td>Nibble Mask:标识产生事件的内存总线上一个或多个错误的半字节。</td></tr>
<tr><td>11h</td><td>1</td><td>Bank Group</td><td>Bank Group(Bank 组)</td></tr>
<tr><td>12h</td><td>1</td><td>Bank</td><td>Bank(Bank 号)</td></tr>
<tr><td>13h</td><td>3</td><td>Row</td><td>Row(行号)</td></tr>
<tr><td>16h</td><td>2</td><td>Column</td><td>Column(列号)</td></tr>
<tr><td>18h</td><td>20h</td><td>Correction Mask: Identifies the bits in error within that nibble in error on the memory bus that produced the error.</td><td>Correction Mask:标识产生错误的内存总线上该错误半字节内的错误位。</td></tr>
<tr><td>38h</td><td>10h</td><td>Component Identifier: Device-specific component identifier.</td><td>Component Identifier:设备特定的组件标识符。</td></tr>
<tr><td>48h</td><td>1</td><td>Sub-channel</td><td>Sub-channel(子通道)</td></tr>
<tr><td>49h</td><td>7</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Error Signature (page 688-689) ｜ Error Signature
>
> <img src="figures/chapter_08/page_0688.png" alt="Figure 8-X page 688" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0688.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-3"></a>
## 8.2.10.5.3 Get Log Capabilities (Opcode 0402h) | 获取日志能力 (操作码 0402h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Gets capabilities related to the specified log. If the component supports this command, it shall be implemented for all Log Identifier UUIDs that the component supports. This command shall return Invalid Log if the specified Log Identifier is not supported by the component.</td><td style="background-color:#e8e8e8">获取与指定日志相关的能力。如果组件支持此命令,则应针对组件支持的所有 Log Identifier UUID 实现此命令。如果组件不支持指定的 Log Identifier,则此命令应返回 Invalid Log。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Invalid Log</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Invalid Log(无效日志)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-101. Get Log Capabilities Input Payload | Get Log Capabilities 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log for which to get capabilities.</td><td>日志标识符(UUID):表示要获取其能力的日志的 UUID。</td></tr>
</tbody>
</table>

**Table 8-102. Get Log Capabilities Output Payload | Get Log Capabilities 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Parameter Flags<br>• Bit[0]: Clear Log Supported: This bit is set to 1 if the log supports being cleared via the Clear Log command.<br>• Bit[1]: Populate Log Supported: This bit is set to 1 if the log supports being populated via the Populate Log command.<br>• Bit[2]: Auto Populate Supported: This bit is set to 1 if the log supports the ability of being auto populated.<br>• Bit[3]: Persistent across Cold Reset: This bit is set to 1 if the log is persistent across Cold Reset.<br>• Bits[31:4]: Reserved</td><td>Parameter Flags(参数标志)<br>• Bit[0]:Clear Log Supported:如果日志支持通过 Clear Log 命令清除,则此位设置为 1。<br>• Bit[1]:Populate Log Supported:如果日志支持通过 Populate Log 命令填充,则此位设置为 1。<br>• Bit[2]:Auto Populate Supported:如果日志支持自动填充能力,则此位设置为 1。<br>• Bit[3]:Persistent across Cold Reset:如果日志在冷复位后保留,则此位设置为 1。<br>• Bits[31:4]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Log Capabilities (page 690) ｜ Get Log Capabilities
>
> <img src="figures/chapter_08/page_0690.png" alt="Figure 8-X page 690" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0690.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-4"></a>
## 8.2.10.5.4 Clear Log (Opcode 0403h) | 清除日志 (操作码 0403h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Clears the contents of the specified log.</td><td style="background-color:#e8e8e8">清除指定日志的内容。</td></tr>
<tr><td>This command shall return Invalid Log if the specified Log Identifier is not supported by the component.</td><td style="background-color:#e8e8e8">如果组件不支持指定的 Log Identifier,则此命令应返回 Invalid Log。</td></tr>
<tr><td>This command shall return Invalid Input if the specified Log Identifier does not have the Clear Log Supported bit set to 1 in the Get Log Capabilities Output Payload.</td><td style="background-color:#e8e8e8">如果指定的 Log Identifier 在 Get Log Capabilities Output Payload 中的 Clear Log Supported 位未设置为 1,则此命令应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Invalid Log</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Invalid Log(无效日志)</td></tr>
</tbody>
</table>

**Table 8-103. Clear Log Input Payload | Clear Log 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log to clear.</td><td>日志标识符(UUID):表示要清除的日志的 UUID。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Clear Log / Populate Log (page 691) ｜ Clear Log / Populate Log
>
> <img src="figures/chapter_08/page_0691.png" alt="Figure 8-X page 691" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0691.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-5"></a>
## 8.2.10.5.5 Populate Log (Opcode 0404h) | 填充日志 (操作码 0404h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Populates the contents of the specified log.</td><td style="background-color:#e8e8e8">填充指定日志的内容。</td></tr>
<tr><td>This may be a background operation. If the component implements this command as a background operation for any supported Log Identifier, the Background Operation bit in the Command Effects Log entry for Populate Log shall be set to 1.</td><td style="background-color:#e8e8e8">这可以是后台操作。如果组件对任何受支持的 Log Identifier 将此命令实现为后台操作,则 Populate Log 的 Command Effects Log 条目中的 Background Operation 位应设置为 1。</td></tr>
<tr><td>This command shall return Invalid Log if the specified Log Identifier is not supported by the component.</td><td style="background-color:#e8e8e8">如果组件不支持指定的 Log Identifier,则此命令应返回 Invalid Log。</td></tr>
<tr><td>This command shall return Invalid Input if the specified Log Identifier does not have the Populate Log Supported bit set to 1 in the Get Log Capabilities Output Payload.</td><td style="background-color:#e8e8e8">如果指定的 Log Identifier 在 Get Log Capabilities Output Payload 中的 Populate Log Supported 位未设置为 1,则此命令应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Background Command Started<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Invalid Log<br>• Interrupted<br>• Busy<br>• Aborted</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Background Command Started(后台命令已启动)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Invalid Log(无效日志)<br>• Interrupted(中断)<br>• Busy(忙)<br>• Aborted(中止)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Log Change<br>• Background Operation (if the component implements this command as a background operation for any supported Log Identifier)</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Log Change(立即日志更改)<br>• Background Operation(后台操作)(如果组件对任何受支持的 Log Identifier 将此命令实现为后台操作)</td></tr>
</tbody>
</table>

**Table 8-104. Populate Log Input Payload | Populate Log 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log to populate.</td><td>日志标识符(UUID):表示要填充的日志的 UUID。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-6"></a>
## 8.2.10.5.6 Get Supported Logs Sub-List (Opcode 0405h) | 获取支持的日志子列表 (操作码 0405h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve a sub-list of device-specific log identifiers (each identified by a UUID) and the maximum capacity of each log. This command can retrieve a maximum of 255 log entries. The output of this command shall be consistent with the output of the Get Supported Logs command.</td><td style="background-color:#e8e8e8">检索设备特定日志标识符(每个由 UUID 标识)的子列表以及每个日志的最大容量。此命令最多可检索 255 个日志条目。此命令的输出应与 Get Supported Logs 命令的输出一致。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-105. Get Supported Logs Sub-List Input Payload | Get Supported Logs Sub-List 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Number of Supported Log Entries: The maximum number of Supported Log Entries requested. This field shall have a minimum value of 01h.</td><td>Maximum Number of Supported Log Entries:请求的 Supported Log Entries 的最大数量。此字段的最小值应为 01h。</td></tr>
<tr><td>01h</td><td>1</td><td>Start Log Entry Index: Index of the first requested Supported Log Entry.</td><td>Start Log Entry Index:第一个请求的 Supported Log Entry 的索引。</td></tr>
</tbody>
</table>

**Table 8-106. Get Supported Logs Sub-List Output Payload | Get Supported Logs Sub-List 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Supported Log Entries</td><td>Number of Supported Log Entries(支持的日志条目数)</td></tr>
<tr><td>01h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>02h</td><td>2</td><td>Total Number of Supported Log Entries: The total number of Supported Log Entries supported by the component.</td><td>Total Number of Supported Log Entries:组件支持的 Supported Log Entries 总数。</td></tr>
<tr><td>04h</td><td>1</td><td>Start Log Entry Index: Index of the first Supported Log Entry in the output payload.</td><td>Start Log Entry Index:输出负载中第一个 Supported Log Entry 的索引。</td></tr>
<tr><td>05h</td><td>3</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Supported Log Entries: Device-specific list of supported log identifier UUIDs and the maximum capacity of each log.</td><td>Supported Log Entries:受支持日志标识符 UUID 的设备特定列表以及每个日志的最大容量。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Supported Logs Sub-List (page 692) ｜ Get Supported Logs Sub-List
>
> <img src="figures/chapter_08/page_0692.png" alt="Figure 8-X page 692" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0692.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6"></a>
## 8.2.10.6 Features | 特性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>A Feature is a configuration, control or capability whose setting(s) can be retrieved using Get Feature and optionally modified using Set Feature. Get Feature is used for reporting the values of the associated setting(s). The scope of a Feature is feature-specific and shall be described as part of each Feature's definition. The scope of the Feature may be at the CXL device, LD, Fabric Manager device, or a combination of all these levels.</td><td style="background-color:#e8e8e8">Feature 是一种配置、控制或能力,其设置可以使用 Get Feature 检索,并可选择使用 Set Feature 修改。Get Feature 用于报告相关设置的值。Feature 的范围是特定于 Feature 的,应作为每个 Feature 定义的一部分进行描述。Feature 的范围可在 CXL device、LD、Fabric Manager device 或所有这些级别的组合上。</td></tr>
<tr><td>If a Feature supports changeable attributes that are optional for an implementation, the Set Feature payload describes all changeable attributes and a field that specifies the attribute(s) to update. Any dependencies between different attributes shall be defined by the Feature specification.</td><td style="background-color:#e8e8e8">如果 Feature 支持对实现可选的可更改属性,则 Set Feature 负载描述所有可更改属性以及一个指定要更新的属性的字段。不同属性之间的任何依赖关系应由 Feature 规范定义。</td></tr>
<tr><td>If a Feature is supported on the secondary mailbox, the secondary mailbox shall return identical Set Feature Effects value as the primary mailbox for the Feature's Get Supported Features Supported Feature Entry.</td><td style="background-color:#e8e8e8">如果在 secondary mailbox 上支持 Feature,则 secondary mailbox 应为该 Feature 的 Get Supported Features Supported Feature Entry 返回与 primary mailbox 相同的 Set Feature Effects 值。</td></tr>
<tr><td>Features may evolve by defining new fields in the payload definitions that were originally defined as reserved or by appending new fields.</td><td style="background-color:#e8e8e8">Feature 可以通过在最初定义为保留的负载定义中定义新字段或附加新字段来演进。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-1"></a>
### 8.2.10.6.1 Get Supported Features (Opcode 0500h) | 获取支持的特性 (操作码 0500h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve the list of supported device-specific features (identified by UUID) and general information about each Feature. The device shall return Invalid Input if the Starting Feature Index value is greater than the Device Supported Features value.</td><td style="background-color:#e8e8e8">检索受支持的设备特定 Feature 列表(由 UUID 标识)以及关于每个 Feature 的一般信息。如果 Starting Feature Index 值大于 Device Supported Features 值,设备应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-107. Get Supported Features Input Payload | Get Supported Features 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Count: Count in bytes of the supported Feature data to return in the output payload. The device shall return no more bytes than requested, but it can return less bytes.</td><td>Count:要在输出负载中返回的受支持 Feature 数据的字节数。设备返回的字节数不应超过请求的字节数,但可以返回较少的字节数。</td></tr>
<tr><td>04h</td><td>2</td><td>Starting Feature Index: Index of the first requested Supported Feature Entry. Feature index is a zero-based value.</td><td>Starting Feature Index:第一个请求的 Supported Feature Entry 的索引。Feature 索引是从零开始的值。</td></tr>
<tr><td>06h</td><td>2</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

**Table 8-108. Get Supported Features Output Payload | Get Supported Features 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Number of Supported Feature Entries: The number of Supported Feature Entries returned in the output payload.</td><td>Number of Supported Feature Entries:输出负载中返回的 Supported Feature Entries 数量。</td></tr>
<tr><td>02h</td><td>2</td><td>Device Supported Features: The number of supported Features.</td><td>Device Supported Features:受支持 Feature 的数量。</td></tr>
<tr><td>04h</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Supported Feature Entries: Device-specific list of supported feature identifier UUIDs and general information about each feature (see Table 8-109).</td><td>Supported Feature Entries:受支持 Feature 标识符 UUID 的设备特定列表以及有关每个 Feature 的一般信息(参见表 8-109)。</td></tr>
</tbody>
</table>

**Table 8-109. Get Supported Features Supported Feature Entry | Get Supported Features Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier: UUID that represents the feature for which to retrieve data.</td><td>Feature Identifier:表示要检索数据的 Feature 的 UUID。</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index: A zero-based value that is used to uniquely identify the feature. The Feature Index shall be less than the Device Supported Features value.</td><td>Feature Index:用于唯一标识 Feature 的从零开始的值。Feature Index 应小于 Device Supported Features 值。</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size: The maximum number of bytes that are required to retrieve this Feature data through the Get Feature command(s).</td><td>Get Feature Size:通过 Get Feature 命令检索此 Feature 数据所需的最大字节数。</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size: The maximum number of bytes that are required to update this Feature data through the Set Feature command(s). This field shall have a value of 0 if this Feature cannot be changed.</td><td>Set Feature Size:通过 Set Feature 命令更新此 Feature 数据所需的最大字节数。如果此 Feature 不能更改,则此字段的值为 0。</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags<br>• Bit[0]: Changeable: If set to 1, the Feature attribute(s) can be changed.<br>• Bits[3:1]: Deepest Reset Persistence: 000b = None; 001b = CXL reset; 010b = Hot reset; 011b = Warm reset; 100b = Cold reset; All other encodings are reserved.<br>• Bit[4]: Persist across Firmware Update: If set to 1, the current value of Feature attribute(s) persist across a firmware update.<br>• Bit[5]: Default Selection Supported<br>• Bit[6]: Saved Selection Supported<br>• Bits[31:7]: Reserved</td><td>Attribute Flags(属性标志)<br>• Bit[0]:Changeable:如果设置为 1,则 Feature 属性可以更改。<br>• Bits[3:1]:Deepest Reset Persistence:000b = None;001b = CXL reset;010b = Hot reset;011b = Warm reset;100b = Cold reset;所有其他编码保留。<br>• Bit[4]:Persist across Firmware Update:如果设置为 1,则 Feature 属性的当前值在固件更新后保留。<br>• Bit[5]:Default Selection Supported<br>• Bit[6]:Saved Selection Supported<br>• Bits[31:7]:保留</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>Get Feature Version</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>Set Feature Version</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects: Bitmask that contains one or more effects for the Set Feature. See the Command Effect field of the CEL Entry Structure in Table 8-87. This field shall have a value of 0 if the Feature cannot be changed.</td><td>Set Feature Effects:包含 Set Feature 的一个或多个效果的位掩码。请参阅表 8-87 中 CEL Entry Structure 的 Command Effect 字段。如果 Feature 不能更改,则此字段的值为 0。</td></tr>
<tr><td>1Eh</td><td>18</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Supported Features (page 693) ｜ Get Supported Features
>
> <img src="figures/chapter_08/page_0693.png" alt="Figure 8-X page 693" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0693.png)

**Table 8-110. Feature Attribute(s) Value after Reset | 复位后 Feature 属性值**

<table>
<thead>
<tr><th>Reset Event</th><th>0h: None</th><th>1h: CXL Reset</th><th>2h: Hot Reset</th><th>3h: Warm Reset</th><th>4h: Cold Reset</th></tr>
</thead>
<tbody>
<tr><td>CXL Reset</td><td>Default Value</td><td>Saved Value</td><td>Current Value</td><td>Current Value</td><td>Current Value</td></tr>
<tr><td>Hot Reset</td><td>Default Value</td><td>Saved Value</td><td>Saved Value</td><td>Current Value</td><td>Current Value</td></tr>
<tr><td>Warm Reset</td><td>Default Value</td><td>Saved Value</td><td>Saved Value</td><td>Saved Value</td><td>Current Value</td></tr>
<tr><td>Cold Reset</td><td>Default Value</td><td>Saved Value</td><td>Saved Value</td><td>Saved Value</td><td>Saved Value</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Default Value: The value set by the vendor when the device is shipped and cannot be changed by the host. If Saved Selection supported flag is 0, the Default Value is the Feature Current Value after reset.</td><td style="background-color:#e8e8e8">Default Value:设备出厂时由厂商设置的值,主机无法更改。如果 Saved Selection supported 标志为 0,则 Default Value 是复位后 Feature 的 Current Value。</td></tr>
<tr><td>Current Value: The current value of Feature attribute(s). If some of Feature attributes are writable, the value used by the device is the current attribute value which may be different than the Default Value or the Saved Value.</td><td style="background-color:#e8e8e8">Current Value:Feature 属性的当前值。如果某些 Feature 属性是可写的,则设备使用的值是当前属性值,该值可能与 Default Value 或 Saved Value 不同。</td></tr>
<tr><td>Saved Value: The value set after reset when Saved Selection Supported is 1. Saved Value shall be equal to Default Value when the device is shipped.</td><td style="background-color:#e8e8e8">Saved Value:当 Saved Selection Supported 为 1 时,复位后设置的值。设备出厂时,Saved Value 应等于 Default Value。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Feature Attribute(s) Value after Reset (page 694) ｜ 复位后 Feature 属性值
>
> <img src="figures/chapter_08/page_0694.png" alt="Figure 8-X page 694" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0694.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-2"></a>
### 8.2.10.6.2 Get Feature (Opcode 0501h) | 获取特性 (操作码 0501h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve the attributes of the Feature identified by a specific UUID. The caller discovers the size of the Feature first using the Get Supported Features command. The Get Feature command returns the bytes specified in the input payload by the Count payload field and starting from the Offset payload field. The Device shall return Invalid Input if the Offset payload field is beyond the maximum size of the Feature as reported by Get Supported Features. If the Offset is less than the maximum size of the Feature and the sum of Offset and Count is greater than the maximum size of the Feature, the Device shall return the data from Offset to the maximum size of the Feature.</td><td style="background-color:#e8e8e8">检索由特定 UUID 标识的 Feature 的属性。调用者首先使用 Get Supported Features 命令发现 Feature 的大小。Get Feature 命令从 Offset 负载字段开始,返回输入负载中 Count 负载字段指定的字节。如果 Offset 负载字段超出 Get Supported Features 所报告的 Feature 最大大小,设备应返回 Invalid Input。如果 Offset 小于 Feature 的最大大小,并且 Offset 和 Count 之和大于 Feature 的最大大小,则设备应返回从 Offset 到 Feature 最大大小的数据。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Unsupported Feature Selection Value<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Unsupported Feature Selection Value(不支持的 Feature 选择值)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-111. Get Feature Input Payload | Get Feature 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier: UUID representing the Feature identifier for which data is being retrieved.</td><td>Feature Identifier:表示正在检索其数据的 Feature 标识符的 UUID。</td></tr>
<tr><td>10h</td><td>2</td><td>Offset: The offset of the first byte in the Feature data to return in the output payload.</td><td>Offset:输出负载中要返回的 Feature 数据的第一个字节的偏移量。</td></tr>
<tr><td>12h</td><td>2</td><td>Count: Count in bytes of the Feature data to return in the output payload.</td><td>Count:输出负载中要返回的 Feature 数据的字节数。</td></tr>
<tr><td>14h</td><td>1</td><td>Selection: Specifies which value of the Feature to return in the output payload.<br>• 0h = Current value<br>• 1h = Default value<br>• 2h = Saved value<br>• All other encodings are reserved</td><td>Selection:指定输出负载中要返回的 Feature 的值。<br>• 0h = Current value(当前值)<br>• 1h = Default value(默认值)<br>• 2h = Saved value(保存值)<br>• 所有其他编码保留</td></tr>
</tbody>
</table>

**Table 8-112. Get Feature Output Payload | Get Feature 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>Varies</td><td>Feature Data</td><td>Feature Data(特性数据)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Feature (page 695) ｜ Get Feature
>
> <img src="figures/chapter_08/page_0695.png" alt="Figure 8-X page 695" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0695.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-3"></a>
### 8.2.10.6.3 Set Feature (Opcode 0502h) | 设置特性 (操作码 0502h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Update the attribute(s) of the Feature identified by a specific UUID. The caller may retrieve the Set Feature Size of the Feature by using the Get Supported Features command. One or more Set Feature commands may be required to transfer all the Feature data, incrementing the Feature Offset each time. The Device shall return Invalid Input if the Offset attempts to access beyond the Set Feature Size of the Feature as reported by Get Supported Features or the sum of Offset and Feature Data size exceeds the Set Feature Size of the Feature as reported by Get Supported Features.</td><td style="background-color:#e8e8e8">更新由特定 UUID 标识的 Feature 的属性。调用者可以使用 Get Supported Features 命令检索 Feature 的 Set Feature Size。可能需要一个或多个 Set Feature 命令来传输所有 Feature 数据,每次递增 Feature Offset。如果 Offset 尝试访问超出 Get Supported Features 所报告的 Feature 的 Set Feature Size 的范围,或 Offset 和 Feature Data 大小之和超出 Get Supported Features 所报告的 Feature 的 Set Feature Size,则设备应返回 Invalid Input。</td></tr>
<tr><td>If the Feature data is transferred in its entirety, the caller makes one call to Set Feature with Action = Full Data Transfer. The Offset field is not used and shall be ignored.</td><td style="background-color:#e8e8e8">如果 Feature 数据是整体传输的,调用者使用 Action = Full Data Transfer 调用一次 Set Feature。Offset 字段不使用,应被忽略。</td></tr>
<tr><td>If a Feature data is transferred in parts, the caller makes one call to Set Feature with Action = Initiate Data Transfer, zero or more calls with Action = Continue Data Transfer, and one call with Action = Finish Data Transfer or Abort Data Transfer. The Feature data parts shall be transferred in ascending order based on the Offset value, and the Device shall return the Feature Transfer Out of Order return code if data parts are not transferred in ascending order. Back-to-back retransmission of any Set Feature data is permitted during a transfer. The Saved across Reset flag is valid for Set Feature command with Action = Initiate Data Transfer or Action = Full Data Transfer and shall be ignored for all other Action values. A Set Feature with Action = Abort Data Transfer shall be supported for Feature data that can be transferred using multiple Set Feature commands. An attempt to call Set Feature with Action = Abort Data Transfer for a Feature whose data has been fully transferred shall fail with Invalid Input.</td><td style="background-color:#e8e8e8">如果 Feature 数据是分部分传输的,调用者使用 Action = Initiate Data Transfer 调用一次 Set Feature,使用 Action = Continue Data Transfer 调用零次或多次,并使用 Action = Finish Data Transfer 或 Abort Data Transfer 调用一次。Feature 数据部分应基于 Offset 值按升序传输,如果数据部分未按升序传输,设备应返回 Feature Transfer Out of Order 返回码。在传输期间,允许对任何 Set Feature 数据进行背靠背重新传输。Saved across Reset 标志对 Action = Initiate Data Transfer 或 Action = Full Data Transfer 的 Set Feature 命令有效,对所有其他 Action 值应忽略。对于可以使用多个 Set Feature 命令传输的 Feature 数据,应支持 Action = Abort Data Transfer 的 Set Feature。对于数据已完全传输的 Feature 尝试调用 Action = Abort Data Transfer 的 Set Feature 应返回 Invalid Input 失败。</td></tr>
<tr><td>Only one Feature may be updated at a time in the device. The device shall return the Feature Transfer in Progress return code if it receives a Set Feature command with Action = Full Data Transfer or Action = Initiate Data Transfer until the current Feature data transfer is completed or aborted.</td><td style="background-color:#e8e8e8">设备一次只能更新一个 Feature。如果设备收到 Action = Full Data Transfer 或 Action = Initiate Data Transfer 的 Set Feature 命令,直到当前 Feature 数据传输完成或中止,设备应返回 Feature Transfer in Progress 返回码。</td></tr>
<tr><td>If the Feature data transfer is interrupted by a Conventional or CXL reset, the Feature data transfer shall be aborted by the device. If a Feature data transfer is aborted prior to the entire Feature data being transferred, the device shall require the Feature data transfer to be started from the beginning of the Feature data.</td><td style="background-color:#e8e8e8">如果 Feature 数据传输被 Conventional 或 CXL reset 中断,设备应中止 Feature 数据传输。如果在传输整个 Feature 数据之前中止了 Feature 数据传输,设备应要求从 Feature 数据开头重新开始 Feature 数据传输。</td></tr>
<tr><td>Once the entire Feature data is fully transferred to the device (i.e., Action = Full Data Transfer or Action = Finish Data Transfer), the device shall update the attribute(s) of the Feature.</td><td style="background-color:#e8e8e8">一旦整个 Feature 数据完全传输到设备(即 Action = Full Data Transfer 或 Action = Finish Data Transfer),设备应更新 Feature 的属性。</td></tr>
<tr><td>The Command Effects Log (CEL) entry for Set Feature shall describe all possible command effects (i.e., Bits 0 to 5) from supported Features that are changeable.</td><td style="background-color:#e8e8e8">Set Feature 的 Command Effects Log (CEL) 条目应描述可更改的受支持 Feature 的所有可能命令效果(即,Bit 0 到 Bit 5)。</td></tr>
<tr><td>If a component receives an input payload that is less than the size of the structure it has implemented, but is greater than or equal to the Minimum Feature Data Size (as specified in the Feature definition), then it shall treat the unsent portion of the structure as 0. For each feature, any fields in the feature data that are not included in the calculation of the Minimum Feature Data Size are explicitly identified. For features where no fields are identified, all the fields in the feature data are to be included in the calculation of the Minimum Feature Data Size.</td><td style="background-color:#e8e8e8">如果组件收到的输入负载小于其实现的结构大小,但大于或等于 Minimum Feature Data Size(如 Feature 定义中指定),则应将结构的未发送部分视为 0。对于每个 Feature,任何未包含在 Minimum Feature Data Size 计算中的 Feature 数据字段都会被明确标识。对于未标识任何字段的 Feature,Feature 数据中的所有字段都应包含在 Minimum Feature Data Size 的计算中。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to alter the features of the locked device by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何更改已锁定设备 Feature 的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Unsupported Feature Version<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Feature Transfer in Progress<br>• Feature Transfer Out of Order<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Unsupported Feature Version(不支持的 Feature 版本)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Feature Transfer in Progress(Feature 传输进行中)<br>• Feature Transfer Out of Order(Feature 传输乱序)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Configuration Change after Cold Reset<br>• Configuration Change after Conventional Reset<br>• Configuration Change after CXL Reset<br>• Immediate Configuration Change<br>• Immediate Data Change<br>• Immediate Policy Change<br>• Immediate Log Change<br>• Security State Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Cold Reset 后的配置更改<br>• Conventional Reset 后的配置更改<br>• CXL Reset 后的配置更改<br>• 立即配置更改<br>• 立即数据更改<br>• 立即策略更改<br>• 立即日志更改<br>• 安全状态更改</td></tr>
</tbody>
</table>

**Table 8-113. Set Feature Input Payload | Set Feature 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier: UUID representing the Feature identifier for which data is being updated. The UUID value of all Fs is a special value that represents the current Feature whose data is in the process of being transferred.</td><td>Feature Identifier:表示正在更新其数据的 Feature 标识符的 UUID。全 F 的 UUID 值是特殊值,表示正在传输其数据的当前 Feature。</td></tr>
<tr><td>10h</td><td>4</td><td>Set Feature Flags<br>• Bits[2:0]: Action: 000b = Full Data Transfer; 001b = Initiate Data Transfer; 010b = Continue Data Transfer; 011b = Finish Data Transfer; 100b = Abort Data Transfer; All other encodings are reserved<br>• Bit[3]: Saved across Reset: If set to 1, the modified value is saved across the Deepest Reset Persistence value for the Feature<br>• Bits[31:4]: Reserved</td><td>Set Feature Flags(设置特性标志)<br>• Bits[2:0]:Action:000b = Full Data Transfer;001b = Initiate Data Transfer;010b = Continue Data Transfer;011b = Finish Data Transfer;100b = Abort Data Transfer;所有其他编码保留<br>• Bit[3]:Saved across Reset:如果设置为 1,则修改后的值在 Feature 的 Deepest Reset Persistence 值范围内保留<br>• Bits[31:4]:保留</td></tr>
<tr><td>14h</td><td>2</td><td>Offset: The byte offset of the Feature data to update.</td><td>Offset:要更新的 Feature 数据的字节偏移量。</td></tr>
<tr><td>16h</td><td>1</td><td>Version: Feature version of the data in Feature Data.</td><td>Version:Feature Data 中数据的 Feature 版本。</td></tr>
<tr><td>17h</td><td>9</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>Varies</td><td>Feature Data</td><td>Feature Data(特性数据)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Set Feature (page 697) ｜ Set Feature
>
> <img src="figures/chapter_08/page_0697.png" alt="Figure 8-X page 697" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0697.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-4"></a>
### 8.2.10.6.4 Metabits Storage Feature Discovery and Configuration | Metabits 存储特性发现和配置

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Feature Identifier of this feature is: 3568da82-e69c-4518-95a2-446fe34ea865.</td><td style="background-color:#e8e8e8">此特性的 Feature Identifier 是:3568da82-e69c-4518-95a2-446fe34ea865。</td></tr>
<tr><td>This feature allows the host to discover and configure the support for storage of Metadata Value bits and TE State in the CXL device's HDM-H address region. It is not applicable to HDM-DB address region. This Feature is not applicable when TE State granularity is bigger than 64B.</td><td style="background-color:#e8e8e8">此特性允许主机发现和配置 CXL 设备的 HDM-H 地址区域中 Metadata Value 位和 TE State 的存储支持。它不适用于 HDM-DB 地址区域。当 TE State 粒度大于 64B 时,此特性不适用。</td></tr>
<tr><td>Table 8-114 shows the information returned in the Get Supported Features output payload for the Metabits Storage Feature. Some feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-114 显示了 Metabits Storage Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
<tr><td>Any changes to HDM-H Metabits Storage Configuration require a Conventional reset to take effect. Saved across Reset bit in Set Feature Input Payload shall be set to 1, otherwise the device shall return Invalid Input. Changes to HDM-H Metabits Storage Configuration may result in changes to the device capacity and CDAT.</td><td style="background-color:#e8e8e8">对 HDM-H Metabits Storage Configuration 的任何更改都需要 Conventional reset 才能生效。Set Feature Input Payload 中的 Saved across Reset 位应设置为 1,否则设备应返回 Invalid Input。对 HDM-H Metabits Storage Configuration 的更改可能会导致设备容量和 CDAT 的更改。</td></tr>
<tr><td>An SH-MLD, MH-MLD or MH-SLD that support this feature shall report Set Feature Size=0 and Bit[0] of Attribute Flags Bit[0] = 0, over CCI exposed to individual hosts indicating that the Feature Data cannot be modified over these CCI.</td><td style="background-color:#e8e8e8">支持此特性的 SH-MLD、MH-MLD 或 MH-SLD 应在暴露给各个主机的 CCI 上报告 Set Feature Size=0 和 Attribute Flags Bit[0] 的 Bit[0] = 0,表示不能通过这些 CCI 修改 Feature Data。</td></tr>
</tbody>
</table>

**Table 8-114. Supported Feature Entry for Metabits Storage Feature | Metabits Storage Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte offset</th><th>Length in Bytes</th><th>Attribute</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>3568da82-e69c-4518-95a2-446fe34ea865</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device Specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>3 Bytes</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>1 Bytes</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 010b (Deepest Reset Persistence = Hot Reset). Conventional reset will restore the saved value.<br>• Bit[4]: 1 (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: 1 (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>01h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>01h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 1 (Configuration Change after Cold Reset)<br>• Bit[1]: 0 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log Change)<br>• Bit[5]: Vendor-specific value (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 (CEL[11:10] Valid)<br>• Bit[10]: 1 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>18</td><td>Reserved</td><td>•</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An SH-MLD, MH-MLD or MH-SLD that support this feature shall report Set Feature Size=1 and Bit[0] of Attribute Flags Bit[0] = 1, over CCI exposed to the FM indicating that the Feature Data can be modified over these CCI.</td><td style="background-color:#e8e8e8">支持此特性的 SH-MLD、MH-MLD 或 MH-SLD 应在暴露给 FM 的 CCI 上报告 Set Feature Size=1 和 Attribute Flags Bit[0] 的 Bit[0] = 1,表示可以通过这些 CCI 修改 Feature Data。</td></tr>
<tr><td>After a successful CXL reset, a Conventional Reset or a successful Secure Erase operation, a subsequent read to any device cacheline (DPA) shall return Metafield=00b (Meta0-State abbreviation MS0) and MetaValue=00b, if the device is configured with non-zero Metadata bits via this Feature. As per Section 12.2.3, a device must set the MetaField to No-Op in the CXL.cachemem return response when the Metadata is suspect.</td><td style="background-color:#e8e8e8">在成功的 CXL reset、Conventional Reset 或成功的 Secure Erase 操作之后,如果设备通过此特性配置了非零 Metadata 位,则对任何设备 cacheline (DPA) 的后续读取应返回 Metafield=00b(Meta0-State 缩写 MS0)和 MetaValue=00b。根据 12.2.3 节,当 Metadata 不可信时,设备必须在 CXL.cachemem 返回响应中将 MetaField 设置为 No-Op。</td></tr>
</tbody>
</table>

**Table 8-115. Metabits Storage Feature Readable Attributes | Metabits Storage Feature 可读属性**

<table>
<thead>
<tr><th>Byte offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>HDM-H Metabits Storage Capabilities<br>• Bit[0]: 2 bits of Metadata are supported. 2 bits of storage supported.<br>• Bit[1]: No Metadata is supported. No storage supported.<br>• Bit[2]: 1-bit of Metadata is supported. bit-0 of Meta0-State Value will be stored. One bit of storage supported.<br>• Bit[3]: 1-bit of Metadata is supported. bit-1 of Meta0-State Value will be stored. One bit of storage supported.<br>• Bit[4]: 2 bits of Metadata + 1 TE State bit are supported. Three bits of storage supported.<br>• Bit[5]: No Metadata + 1 TE State bit is supported. One bit of storage supported.<br>• Bit[6]: 1-bit of Metadata + 1 TE State bit are supported. bit-0 of Meta0-State Value will be stored. Two bits of storage supported.<br>• Bit[7]: 1-bit of Metadata + 1 TE State bit are supported. bit-1 of Meta0-State Value will be stored. Two bits of storage supported.<br>• Bits[15:8]: Reserved</td><td>HDM-H Metabits Storage Capabilities(HDM-H Metabits 存储能力)<br>• Bit[0]:支持 2 位 Metadata。支持 2 位存储。<br>• Bit[1]:不支持 Metadata。不支持存储。<br>• Bit[2]:支持 1 位 Metadata。将存储 Meta0-State Value 的 bit-0。支持 1 位存储。<br>• Bit[3]:支持 1 位 Metadata。将存储 Meta0-State Value 的 bit-1。支持 1 位存储。<br>• Bit[4]:支持 2 位 Metadata + 1 TE State 位。支持 3 位存储。<br>• Bit[5]:不支持 Metadata + 1 TE State 位。支持 1 位存储。<br>• Bit[6]:支持 1 位 Metadata + 1 TE State 位。将存储 Meta0-State Value 的 bit-0。支持 2 位存储。<br>• Bit[7]:支持 1 位 Metadata + 1 TE State 位。将存储 Meta0-State Value 的 bit-1。支持 2 位存储。<br>• Bits[15:8]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>HDM-H Metabits Storage Configuration<br>• 0h: 2 bits of Metadata<br>• 1h: No Metadata<br>• 2h: 1 bit of Metadata, bit-0 of Meta0-State Value<br>• 3h: 1 bit of Metadata, bit-1 of Meta0-State Value<br>• 4h: 2 bits of Metadata + 1 TE State bit<br>• 5h: No Metadata + 1 TE State bit<br>• 6h: 1 bit of Metadata, bit-0 of Meta0-State Value + 1 TE State bit<br>• 7h: 1 bit of Metadata, bit-1 of Meta0-State Value + 1 TE State bit<br>• Bits[7:3]: Reserved</td><td>HDM-H Metabits Storage Configuration(HDM-H Metabits 存储配置)<br>• 0h:2 位 Metadata<br>• 1h:无 Metadata<br>• 2h:1 位 Metadata,Meta0-State Value 的 bit-0<br>• 3h:1 位 Metadata,Meta0-State Value 的 bit-1<br>• 4h:2 位 Metadata + 1 TE State 位<br>• 5h:无 Metadata + 1 TE State 位<br>• 6h:1 位 Metadata,Meta0-State Value 的 bit-0 + 1 TE State 位<br>• 7h:1 位 Metadata,Meta0-State Value 的 bit-1 + 1 TE State 位<br>• Bits[7:3]:保留</td></tr>
</tbody>
</table>

**Table 8-116. Metabits Storage Feature Writable Attributes | Metabits Storage Feature 可写属性**

<table>
<thead>
<tr><th>Byte offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>1</td><td>HDM-H Metabits Storage Configuration (Values as defined in Table 8-115)</td><td>HDM-H Metabits Storage Configuration(值如表 8-115 所定义)</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Table 8-115 shows the output payload returned by a Get Feature command with Selection set to 0h (Current value), 1h (Default value) or 2h (Saved Value).</td><td style="background-color:#e8e8e8">表 8-115 显示了 Selection 设置为 0h(Current value)、1h(Default value)或 2h(Saved Value)的 Get Feature 命令返回的输出负载。</td></tr>
<tr><td>Table 8-116 shows the input payload for Set Feature command.</td><td style="background-color:#e8e8e8">表 8-116 显示了 Set Feature 命令的输入负载。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Metabits Storage Feature (page 698-699) ｜ Metabits Storage Feature
>
> <img src="figures/chapter_08/page_0698.png" alt="Figure 8-X page 698" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0698.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7"></a>
## 8.2.10.7 Maintenance | 维护

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1"></a>
### 8.2.10.7.1 Perform Maintenance (Opcode 0600h) | 执行维护 (操作码 0600h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command requests the device to execute the maintenance operation specified by the Maintenance Operation Class and the Maintenance Operation Subclass. If the operation is not supported, the command shall be terminated with Invalid Input Return Code.</td><td style="background-color:#e8e8e8">此命令请求设备执行由 Maintenance Operation Class 和 Maintenance Operation Subclass 指定的维护操作。如果不支持该操作,命令应以 Invalid Input Return Code 终止。</td></tr>
<tr><td>The Perform Maintenance command may be performed in the foreground or in the background, based on the characteristics of the maintenance operation. When the device is executing a Perform Maintenance command in the background, it may indicate operation progress using the Background Command Status register.</td><td style="background-color:#e8e8e8">根据维护操作的特征,Perform Maintenance 命令可以在前台或后台执行。当设备在后台执行 Perform Maintenance 命令时,它可以使用 Background Command Status 寄存器指示操作进度。</td></tr>
<tr><td>No more than one maintenance operation may be initiated at a time.</td><td style="background-color:#e8e8e8">一次最多只能启动一个维护操作。</td></tr>
</tbody>
</table>

**Table 8-117. Perform Maintenance Input Payload | Perform Maintenance 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: This field identifies the Class of a maintenance operation. See Table 8-125.</td><td>Maintenance Operation Class(维护操作类):此字段标识维护操作的类。参见表 8-125。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: This field identifies the maintenance operation together with the Maintenance Operation Class. See Table 8-125.</td><td>Maintenance Operation Subclass(维护操作子类):此字段与 Maintenance Operation Class 一起标识维护操作。参见表 8-125。</td></tr>
<tr><td>02h</td><td>Varies</td><td>Maintenance operation parameters.</td><td>维护操作参数。</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The device shall terminate a foreground or background Perform Maintenance command with Busy Return Code if it is already processing a maintenance operation in the background.</td><td style="background-color:#e8e8e8">如果设备已经在后台处理维护操作,则应使用 Busy Return Code 终止前台或后台的 Perform Maintenance 命令。</td></tr>
<tr><td>Some restrictions may apply during the execution of a maintenance operation. For example, it might not be possible to read or write a CXL memory device. These restrictions are specified in the description of the maintenance operation and there can be Feature attributes that indicate device capabilities.</td><td style="background-color:#e8e8e8">在维护操作执行期间,可能适用某些限制。例如,可能无法读取或写入 CXL memory device。这些限制在维护操作的描述中指定,并且可能存在指示设备能力的 Feature 属性。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to perform maintenance PPR, sPPR, hPPR, built-in self-tests, and/or other maintenance operations that might alter the data and/or TE State on the device, affect the devices ability to maintain data coherency, and/or compromise the link's integrity by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何执行维护 PPR、sPPR、hPPR、内置自检和/或其他可能更改设备上的数据和/或 TE State、影响设备维持数据一致性的能力和/或损害链路完整性的维护操作的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Background Command Started<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Busy<br>• Transfer Out of Order<br>• Aborted<br>• Invalid Physical Address<br>• Resources Exhausted<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Background Command Started(后台命令已启动)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Busy(忙)<br>• Transfer Out of Order(传输乱序)<br>• Aborted(中止)<br>• Invalid Physical Address(无效物理地址)<br>• Resources Exhausted(资源耗尽)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Configuration Change if a maintenance operation restricts the operations that a host can do<br>• Immediate Data Change if a maintenance operation impacts the data written to the device<br>• Immediate Log Change if a maintenance operation impacts a device log<br>• Background Operation if a maintenance operation is executed in background<br>• Request Abort Background Operation Command Supported</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Configuration Change(立即配置更改)(如果维护操作限制了主机可以执行的操作)<br>• Immediate Data Change(立即数据更改)(如果维护操作影响写入设备的数据)<br>• Immediate Log Change(立即日志更改)(如果维护操作影响设备日志)<br>• Background Operation(后台操作)(如果维护操作在后台执行)<br>• Request Abort Background Operation Command Supported(支持请求中止后台操作命令)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Perform Maintenance (page 700-701) ｜ Perform Maintenance
>
> <img src="figures/chapter_08/page_0700.png" alt="Figure 8-X page 700" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0700.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-1"></a>
#### 8.2.10.7.1.1 PPR Maintenance Operations | PPR 维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Post Package Repair (PPR) maintenance operations may be supported by CXL devices that implement CXL.mem protocol. A PPR maintenance operation requests the CXL device to perform a repair operation on its media.</td><td style="background-color:#e8e8e8">Post Package Repair (PPR) 维护操作可以由实现 CXL.mem 协议的 CXL 设备支持。PPR 维护操作请求 CXL 设备对其介质执行修复操作。</td></tr>
<tr><td>For example, a CXL device with DRAM components that support PPR features may implement PPR Maintenance operations. DRAM components may support two types of PPR: Hard PPR (hPPR), for a permanent row repair, and Soft PPR (sPPR), for a temporary row repair. sPPR is much faster than hPPR, but the repair is lost with a power cycle.</td><td style="background-color:#e8e8e8">例如,具有支持 PPR 功能的 DRAM 组件的 CXL 设备可以实现 PPR 维护操作。DRAM 组件可以支持两种类型的 PPR:Hard PPR (hPPR),用于永久行修复,以及 Soft PPR (sPPR),用于临时行修复。sPPR 比 hPPR 快得多,但修复会在电源循环后丢失。</td></tr>
<tr><td>Based on DRAM PPR features, two maintenance operations are defined: sPPR and hPPR. Note that PPR maintenance operations may also apply to other types of media component.</td><td style="background-color:#e8e8e8">基于 DRAM PPR 功能,定义了两个维护操作:sPPR 和 hPPR。请注意,PPR 维护操作也可能适用于其他类型的介质组件。</td></tr>
<tr><td>During the execution of a PPR Maintenance operation, a CXL memory device:<br>• May or may not retain data<br>• May or may not be able to process CXL.mem requests correctly, including the ones that target the DPA involved in the repair</td><td style="background-color:#e8e8e8">在执行 PPR 维护操作期间,CXL memory device:<br>• 可能保留数据,也可能不保留数据<br>• 可能能够正确处理 CXL.mem 请求,也可能不能,包括针对修复涉及的 DPA 的请求</td></tr>
<tr><td>If the device is not capable of correctly processing a CXL.mem request during a PPR Maintenance operation, then:<br>• A read shall return poison<br>• A write shall be dropped, and an NDR shall be sent<br>• Any subsequent reads of DPA for which writes may have been incorrectly processed shall return poison</td><td style="background-color:#e8e8e8">如果设备在 PPR 维护操作期间无法正确处理 CXL.mem 请求,则:<br>• 读取应返回 poison<br>• 写入应被丢弃,并发送 NDR<br>• 对于写入可能被错误处理的 DPA 的任何后续读取应返回 poison</td></tr>
<tr><td>These CXL Memory Device capabilities are specified by Restriction Flags in the sPPR Feature and hPPR Feature (see Section 8.2.10.7.2.1 and Section 8.2.10.7.2.2, respectively).</td><td style="background-color:#e8e8e8">这些 CXL Memory Device 能力由 sPPR Feature 和 hPPR Feature 中的 Restriction Flags 指定(分别参见 8.2.10.7.2.1 节和 8.2.10.7.2.2 节)。</td></tr>
<tr><td>sPPR maintenance operation may be executed at runtime, if data is retained and CXL.mem requests are correctly processed. For CXL devices with DRAM components, hPPR maintenance operation may be executed only at boot because data would not be retained.</td><td style="background-color:#e8e8e8">如果保留了数据并正确处理 CXL.mem 请求,则可以在运行时执行 sPPR 维护操作。对于具有 DRAM 组件的 CXL 设备,hPPR 维护操作只能在启动时执行,因为数据将不会被保留。</td></tr>
<tr><td>When a CXL device identifies a failure on a memory component, the device may inform the host about the need for a PPR maintenance operation by using an Event Record, where the Maintenance Needed flag is set. The Event Record specifies the DPA that should be repaired. A CXL device may not keep track of the requests that have already been sent and the information on which DPA should be repaired may be lost upon power cycle.</td><td style="background-color:#e8e8e8">当 CXL 设备识别内存组件上的故障时,设备可以通过使用 Event Record 通知主机需要执行 PPR 维护操作,其中 Maintenance Needed 标志被设置。Event Record 指定应修复的 DPA。CXL 设备可能不跟踪已发送的请求,并且有关应修复哪个 DPA 的信息可能在电源循环后丢失。</td></tr>
<tr><td>The Host or the FM may or may not initiate a PPR Maintenance operation in response to a device request. It is possible to check whether resources are available by issuing a Perform Maintenance command for the PPR maintenance operation with the Query Resources flag set to 1. If the controller does not support reporting whether a resource is available, and a Perform Maintenance operation for PPR is issued with Query Resources set to 1, the controller shall return Invalid Input.</td><td style="background-color:#e8e8e8">主机或 FM 可以根据设备请求启动 PPR 维护操作,也可以不启动。可以通过发出 Query Resources 标志设置为 1 的 PPR 维护操作的 Perform Maintenance 命令来检查资源是否可用。如果控制器不支持报告资源是否可用,并且发出了 Query Resources 设置为 1 的 PPR 的 Perform Maintenance 操作,则控制器应返回 Invalid Input。</td></tr>
<tr><td>If resources are available, then the command shall be completed with the Success Return Code; otherwise, the command shall be completed with the Resources exhausted Return Code.</td><td style="background-color:#e8e8e8">如果资源可用,则命令应以 Success Return Code 完成;否则,命令应以 Resources exhausted Return Code 完成。</td></tr>
<tr><td>The host or the FM may initiate a repair operation by issuing a Perform Maintenance command, setting the Maintenance Operation Class to 01h (PPR), the Maintenance Operation Subclass to either 00h (sPPR) or 01h (hPPR), and indicating the DPA (if supported).</td><td style="background-color:#e8e8e8">主机或 FM 可以通过发出 Perform Maintenance 命令启动修复操作,将 Maintenance Operation Class 设置为 01h (PPR),将 Maintenance Operation Subclass 设置为 00h (sPPR) 或 01h (hPPR),并指示 DPA(如果支持)。</td></tr>
<tr><td>During the execution of a PPR maintenance operation, the device operation may be restricted as indicated by the Restriction Flags in the sPPR Feature and hPPR Feature (see Section 8.2.10.7.2.1 and Section 8.2.10.7.2.2, respectively).</td><td style="background-color:#e8e8e8">在 PPR 维护操作执行期间,设备操作可能受到 sPPR Feature 和 hPPR Feature 中的 Restriction Flags 指示的限制(分别参见 8.2.10.7.2.1 节和 8.2.10.7.2.2 节)。</td></tr>
<tr><td>Upon completion of a PPR maintenance operation, the device shall produce a Memory Sparing Event Record with updated resource availability, if the Memory Sparing Event Record Enable bit is set (see Table 8-128 or Table 8-131).</td><td style="background-color:#e8e8e8">完成 PPR 维护操作后,如果设置了 Memory Sparing Event Record Enable 位(参见表 8-128 或表 8-131),设备应生成一个具有更新资源可用性的 Memory Sparing Event Record。</td></tr>
</tbody>
</table>

> **Figure 8-X.** PPR Maintenance Operations (page 701-702) ｜ PPR 维护操作
>
> <img src="figures/chapter_08/page_0701.png" alt="Figure 8-X page 701" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0701.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-2"></a>
#### 8.2.10.7.1.2 sPPR Maintenance Operation | sPPR 维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This maintenance operation requests the device to perform an sPPR operation. The sPPR Feature provides parameters and configurations related to this operation. See Section 8.2.10.7.2.1. Table 8-118 shows the input payload for this maintenance operation.</td><td style="background-color:#e8e8e8">此维护操作请求设备执行 sPPR 操作。sPPR Feature 提供与此操作相关的参数和配置。参见 8.2.10.7.2.1 节。表 8-118 显示了此维护操作的输入负载。</td></tr>
</tbody>
</table>

**Table 8-118. sPPR Maintenance Input Payload | sPPR 维护输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h.</td><td>Maintenance Operation Class:应设置为 01h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: It shall be cleared to 00h.</td><td>Maintenance Operation Subclass:应清零为 00h。</td></tr>
<tr><td>02h</td><td>1</td><td>Flags<br>• Bit[0]: Query Resources Flag: If set, the CXL device checks whether resources are available to perform the sPPR maintenance operation but does not attempt to perform the operation<br>• Bits[7:1]: Reserved</td><td>标志位<br>• Bit[0]:Query Resources Flag:如果设置,CXL 设备检查是否有可用资源来执行 sPPR 维护操作,但不尝试执行该操作<br>• Bits[7:1]:保留</td></tr>
<tr><td>03h</td><td>8</td><td>DPA: Physical address to be repaired. This field is ignored if the DPA support flag in the sPPR Feature is cleared to 0 (see Table 8-128).</td><td>DPA:要修复的物理地址。如果 sPPR Feature 中的 DPA support 标志清零为 0(参见表 8-128),则此字段被忽略。</td></tr>
<tr><td>0Bh</td><td>3</td><td>Nibble Mask: Identifies one or more nibbles on the memory bus. A Nibble Mask bit set to 1 indicates the request to perform sPPR operation in the specific device. All Nibble Mask bits set to 1 indicates the request to perform the operation in all devices. This field is ignored if the Nibble support flag in the sPPR Feature is cleared to 0 (see Table 8-128), and the sPPR is performed in all devices.</td><td>Nibble Mask:标识内存总线上的一个或多个半字节。设置为 1 的 Nibble Mask 位表示在特定设备中执行 sPPR 操作的请求。全部 Nibble Mask 位设置为 1 表示在所有设备中执行操作的请求。如果 sPPR Feature 中的 Nibble support 标志清零为 0(参见表 8-128),并且 sPPR 在所有设备中执行,则此字段被忽略。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-3"></a>
#### 8.2.10.7.1.3 hPPR Maintenance Operation | hPPR 维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This maintenance operation requests the device to perform an hPPR operation. The hPPR Feature provides parameters and configurations related to this operation, see Section 8.2.10.7.2.2. Table 8-119 shows the input payload for this maintenance operation.</td><td style="background-color:#e8e8e8">此维护操作请求设备执行 hPPR 操作。hPPR Feature 提供与此操作相关的参数和配置,参见 8.2.10.7.2.2 节。表 8-119 显示了此维护操作的输入负载。</td></tr>
</tbody>
</table>

**Table 8-119. hPPR Maintenance Input Payload | hPPR 维护输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h.</td><td>Maintenance Operation Class:应设置为 01h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: It shall be set to 01h.</td><td>Maintenance Operation Subclass:应设置为 01h。</td></tr>
<tr><td>02h</td><td>1</td><td>Flags<br>• Bit[0]: Query Resources Flag: If set, the CXL device checks whether resources are available to perform the hPPR maintenance operation<br>• Bits[7:1]: Reserved</td><td>标志位<br>• Bit[0]:Query Resources Flag:如果设置,CXL 设备检查是否有可用资源来执行 hPPR 维护操作<br>• Bits[7:1]:保留</td></tr>
<tr><td>03h</td><td>8</td><td>DPA: Physical address to be repaired. This field is ignored if the DPA support flag bit in the hPPR Feature is cleared to 0 (see Table 8-131).</td><td>DPA:要修复的物理地址。如果 hPPR Feature 中的 DPA support 标志位清零为 0(参见表 8-131),则此字段被忽略。</td></tr>
<tr><td>0Bh</td><td>3</td><td>Nibble Mask: Identifies one or more nibbles on the memory bus.</td><td>Nibble Mask:标识内存总线上的一个或多个半字节。</td></tr>
</tbody>
</table>

> **Figure 8-X.** hPPR Maintenance Operation (page 703) ｜ hPPR 维护操作
>
> <img src="figures/chapter_08/page_0703.png" alt="Figure 8-X page 703" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0703.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-4"></a>
#### 8.2.10.7.1.4 Memory Sparing Maintenance Operations | 内存备用维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The associated Class and Subclasses are defined in Table 8-125.</td><td style="background-color:#e8e8e8">相关的 Class 和 Subclasses 在表 8-125 中定义。</td></tr>
<tr><td>Memory sparing is defined as a repair function that replaces a portion of memory (the "spared memory") with a portion of functional memory at that same DPA. The Subclasses for this operation vary in terms of the scope of the sparing being performed. The Cacheline sparing subclass refers to a sparing action that can replace a full cacheline. Row sparing is provided as an alternative to PPR sparing functions and its scope is that of a single DDR row. Bank sparing allows an entire bank to be replaced. Rank sparing is defined as an operation in which an entire DDR rank is replaced.</td><td style="background-color:#e8e8e8">内存备用定义为一种修复功能,用于将一部分内存("被备用的内存")替换为同一 DPA 上的功能性内存。此操作的子类根据所执行的备用范围而有所不同。Cacheline sparing 子类是指可以替换完整 cacheline 的备用操作。Row sparing 作为 PPR 备用功能的替代方案提供,其范围是单个 DDR 行。Bank sparing 允许替换整个 bank。Rank sparing 被定义为替换整个 DDR rank 的操作。</td></tr>
<tr><td>The Input Payload specifies the memory portion to be replaced. In particular, the Nibble Mask field in the Input Payload may be used to request sparing on specific components. The nibble mapping is the same as DRAM Event Record nibble mapping (see Table 8-58). Components are specified by setting the Nibble Mask Valid flag and the related Nibble Mask bits. The device may apply memory sparing to more components than requested. If the Nibble Mask Valid flag is 0, the memory sparing request is for all components.</td><td style="background-color:#e8e8e8">输入负载指定要替换的内存部分。特别是,输入负载中的 Nibble Mask 字段可用于请求对特定组件进行备用。半字节映射与 DRAM Event Record 半字节映射相同(参见表 8-58)。通过设置 Nibble Mask Valid 标志和相关的 Nibble Mask 位来指定组件。设备可以向比请求更多的组件应用内存备用。如果 Nibble Mask Valid 标志为 0,则内存备用请求针对所有组件。</td></tr>
<tr><td>If the host requests an operation Subclass for an address and the device is out of resources, the device shall respond with the Resources Exhausted return code.</td><td style="background-color:#e8e8e8">如果主机为地址请求操作子类,并且设备资源耗尽,则设备应以 Resources Exhausted 返回码响应。</td></tr>
<tr><td>The host may issue a query command by setting Query Resources flag in the Input Payload (see Table 8-120) to determine availability of sparing resources for a given address. In response to a query request, the device shall report the resource availability by producing the Memory Sparing Event Record (see Table 8-60) in which the Channel, Rank, Nibble Mask, Bank Group, Bank, Row, Column, Sub-Channel fields are a copy of the values specified in the request. If the controller does not support reporting whether a resource is available, and a Perform Maintenance operation for Memory Sparing is issued with Query Resources set to 1, the controller shall return Invalid Input.</td><td style="background-color:#e8e8e8">主机可以通过在输入负载中设置 Query Resources 标志(参见表 8-120)来发出查询命令,以确定给定地址的备用资源可用性。作为对查询请求的响应,设备应通过生成 Memory Sparing Event Record(参见表 8-60)来报告资源可用性,其中 Channel、Rank、Nibble Mask、Bank Group、Bank、Row、Column、Sub-Channel 字段是请求中指定值的副本。如果控制器不支持报告资源是否可用,并且发出了 Query Resources 设置为 1 的 Memory Sparing 的 Perform Maintenance 操作,则控制器应返回 Invalid Input。</td></tr>
<tr><td>All Memory Sparing operations shall be executed as background operations and are capable of being aborted by the Request Abort Background Operation command.</td><td style="background-color:#e8e8e8">所有 Memory Sparing 操作应作为后台操作执行,并且能够被 Request Abort Background Operation 命令中止。</td></tr>
<tr><td>Table 8-120 shows the input payload for this maintenance operation. The device shall communicate the operation's results by producing a Memory Sparing Event Record (see Table 8-60) in response to the request.</td><td style="background-color:#e8e8e8">表 8-120 显示了此维护操作的输入负载。设备应通过生成 Memory Sparing Event Record(参见表 8-60)来响应请求并传达操作结果。</td></tr>
</tbody>
</table>

**Table 8-120. Memory Sparing Input Payload | Memory Sparing 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 02h.</td><td>Maintenance Operation Class:应设置为 02h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: The legal values are defined in Table 8-125.</td><td>Maintenance Operation Subclass:合法值在表 8-125 中定义。</td></tr>
<tr><td>02h</td><td>1</td><td>Flags<br>• Bit[0]: Query Resources Flag<br>• Bit[1]: Hard Sparing Flag<br>• Bit[2]: Sub-channel Valid Flag<br>• Bit[3]: Nibble Mask Valid Flag<br>• Bits[7:4]: Reserved</td><td>标志位<br>• Bit[0]:Query Resources Flag<br>• Bit[1]:Hard Sparing Flag<br>• Bit[2]:Sub-channel Valid Flag<br>• Bit[3]:Nibble Mask Valid Flag<br>• Bits[7:4]:保留</td></tr>
<tr><td>03h</td><td>1</td><td>Channel</td><td>Channel(通道)</td></tr>
<tr><td>04h</td><td>1</td><td>Rank</td><td>Rank(秩)</td></tr>
<tr><td>05h</td><td>3</td><td>Nibble Mask</td><td>Nibble Mask(半字节掩码)</td></tr>
<tr><td>08h</td><td>1</td><td>Bank Group</td><td>Bank Group(Bank 组)</td></tr>
<tr><td>09h</td><td>1</td><td>Bank</td><td>Bank(Bank 号)</td></tr>
<tr><td>0Ah</td><td>3</td><td>Row</td><td>Row(行号)</td></tr>
<tr><td>0Dh</td><td>2</td><td>Column</td><td>Column(列号)</td></tr>
<tr><td>0Fh</td><td>1</td><td>Sub-channel</td><td>Sub-channel(子通道)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Memory Sparing (page 704) ｜ Memory Sparing
>
> <img src="figures/chapter_08/page_0704.png" alt="Figure 8-X page 704" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0704.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-5"></a>
#### 8.2.10.7.1.5 Device Built-in Test Operations | 设备内置测试操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This function is used to request a CXL.mem-capable device to execute one or more tests.</td><td style="background-color:#e8e8e8">此功能用于请求支持 CXL.mem 的设备执行一项或多项测试。</td></tr>
<tr><td>Media Test Subclass requires the device to execute one or more tests on the memory media. Media Tests that a device supports and their attributes can be discovered by getting the Media Test Capability Log (see Section 8.2.10.5.2.5). The host may discover the media tests that the device supports and then request the device to perform a single test or a list of tests from the supported tests. The test results can be retrieved accessing the Media Test Results Log (see Section 8.2.10.5.2.6). It is expected that CXL.mem traffic to the device is quiesced when a media test is started on the device. If CXL.mem requests are issued during tests execution, the device behavior is undefined.</td><td style="background-color:#e8e8e8">Media Test Subclass 要求设备对内存介质执行一项或多项测试。设备支持的 Media Tests 及其属性可以通过获取 Media Test Capability Log(参见 8.2.10.5.2.5 节)来发现。主机可以发现设备支持的介质测试,然后请求设备从受支持的测试中执行单个测试或测试列表。可以通过访问 Media Test Results Log(参见 8.2.10.5.2.6 节)来检索测试结果。当在设备上启动介质测试时,预计到设备的 CXL.mem 流量将处于静止状态。如果在测试执行期间发出 CXL.mem 请求,则设备行为未定义。</td></tr>
<tr><td>For configuring and launching the Media Test operation, Perform Maintenance Command shall have the Input Payload described in Table 8-121.</td><td style="background-color:#e8e8e8">要配置和启动 Media Test 操作,Perform Maintenance Command 应具有表 8-121 中描述的输入负载。</td></tr>
<tr><td>One or more tests that belong to the same subclass may be requested via a single command (see Table 8-122). For each requested test, a single Test Parameters Entry shall be set up. Because multiple tests may be scheduled via a single command, the Test Parameters length is variable. The Test Parameters may be fully transferred in a single chunk or transferred in multiple chunks by issuing multiple Perform Maintenance commands. If the Test Parameters are transferred in its entirety, the caller issues a single Perform Maintenance Command with Action = Full Transfer. If the Test Parameters are transferred in parts, the caller makes one call to Perform Maintenance with Action = Initiate Transfer, zero or more calls with Action = Continue Transfer, and one call with Action = End Transfer or Abort Transfer. The Test Parameters parts shall be transferred in order; otherwise, the device returns the Transfer Out of Order return code.</td><td style="background-color:#e8e8e8">可以通过单个命令请求属于同一子类的一个或多个测试(参见表 8-122)。对于每个请求的测试,应设置单个 Test Parameters Entry。由于可以通过单个命令调度多个测试,因此 Test Parameters 长度是可变的。Test Parameters 可以通过发出多个 Perform Maintenance 命令以单个块完全传输或以多个块传输。如果 Test Parameters 是整体传输的,则调用者发出 Action = Full Transfer 的单个 Perform Maintenance Command。如果 Test Parameters 是分部分传输的,则调用者使用 Action = Initiate Transfer 调用一次 Perform Maintenance,使用 Action = Continue Transfer 调用零次或多次,并使用 Action = End Transfer 或 Abort Transfer 调用一次。Test Parameters 部分应按顺序传输;否则,设备返回 Transfer Out of Order 返回码。</td></tr>
<tr><td>If the test is executing in background, the device may be asked to abort the test via the Request Abort Background Operation mailbox command. If a component supports Perform Maintenance Operation with this class, it must also support the Request Abort Background Operation command.</td><td style="background-color:#e8e8e8">如果测试在后台执行,可以通过 Request Abort Background Operation 邮箱命令请求设备中止测试。如果组件支持此类的 Perform Maintenance Operation,则它还必须支持 Request Abort Background Operation 命令。</td></tr>
</tbody>
</table>

**Table 8-121. Device Built-in Test Input Payload | Device Built-in Test 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 03h.</td><td>Maintenance Operation Class:应设置为 03h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass<br>• 00h = Media Test<br>• 01h to BCh = Reserved<br>• C0h to FFh = Vendor Specific Test</td><td>Maintenance Operation Subclass<br>• 00h = Media Test<br>• 01h 到 BCh = 保留<br>• C0h 到 FFh = 厂商特定测试</td></tr>
<tr><td>02h</td><td>1</td><td>Action: 00h = Full Transfer; 01h = Initiate Transfer; 02h = Continue Transfer; 03h = End Transfer; 04h = Abort Transfer; All other encodings are reserved</td><td>Action:00h = Full Transfer;01h = Initiate Transfer;02h = Continue Transfer;03h = End Transfer;04h = Abort Transfer;所有其他编码保留</td></tr>
<tr><td>03h</td><td>4</td><td>Offset: The byte offset in the Test Parameters data. Expressed in multiples of 32 bytes. Ignored if Action = Full Transfer.</td><td>Offset:Test Parameters 数据中的字节偏移量。以 32 字节的倍数表示。如果 Action = Full Transfer 则忽略。</td></tr>
<tr><td>07h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>20h+20h*n</td><td>Test parameters: See Table 8-122.</td><td>Test parameters:参见表 8-122。</td></tr>
</tbody>
</table>

**Table 8-122. Test Parameters | Test Parameters**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>20h</td><td>Common Configuration Parameters: Input configuration parameters that apply to all the tests within a given subclass. The common configuration parameters for Media Test are defined in Table 8-123. The common configuration parameters for vendor specific test are defined by the vendor.</td><td>Common Configuration Parameters:适用于给定子类内所有测试的输入配置参数。Media Test 的公共配置参数在表 8-123 中定义。厂商特定测试的公共配置参数由厂商定义。</td></tr>
<tr><td>20h</td><td>20h</td><td>Test 1 Parameters Entry: Input parameters of Test 1. The format of the Test Parameter Entry for Media Test is defined in Table 8-124.</td><td>Test 1 Parameters Entry:测试 1 的输入参数。Media Test 的 Test Parameter Entry 格式在表 8-124 中定义。</td></tr>
<tr><td>40h</td><td>20h</td><td>Test 2 Parameters Entry: Input parameters of Test 2.</td><td>Test 2 Parameters Entry:测试 2 的输入参数。</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>(20h+20h*(n-1))</td><td>20h</td><td>Test n Parameters Entry: Input parameters of Test n.</td><td>Test n Parameters Entry:测试 n 的输入参数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Device Built-in Test (page 705) ｜ Device Built-in Test
>
> <img src="figures/chapter_08/page_0705.png" alt="Figure 8-X page 705" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0705.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2"></a>
### 8.2.10.7.2 Features Associated with Maintenance Operations | 与维护操作关联的特性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Maintenance operations leverage the Features command set (see Section 8.2.10.6).</td><td style="background-color:#e8e8e8">维护操作利用 Features 命令集(参见 8.2.10.6 节)。</td></tr>
<tr><td>A Feature that provides capabilities and configurations may be defined for a maintenance operation. The list of maintenance operations that the device supports can be discovered by analyzing the device's supported Features. This can be accomplished by issuing the Get Supported Features command.</td><td style="background-color:#e8e8e8">可以为维护操作定义提供能力和配置的 Feature。可以通过分析设备受支持的 Feature 来发现设备支持的维护操作列表。这可以通过发出 Get Supported Features 命令来完成。</td></tr>
<tr><td>Table 8-125 shows the Maintenance Operation Classes, Subclasses, and related Feature UUID.</td><td style="background-color:#e8e8e8">表 8-125 显示了 Maintenance Operation Classes、Subclasses 以及相关的 Feature UUID。</td></tr>
</tbody>
</table>

**Table 8-123. Common Configuration Parameters for Media Test Subclass | Media Test Subclass 的公共配置参数**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Tests: Total number of tests requested.</td><td>Number of Tests:请求的测试总数。</td></tr>
<tr><td>01h</td><td>8</td><td>Start Address: Start DPA of the test, applies to all the tests.</td><td>Start Address:测试的起始 DPA,适用于所有测试。</td></tr>
<tr><td>09h</td><td>8</td><td>Length: The range of physical addresses to test, applies to all the tests. This length shall be in multiples of 64 bytes.</td><td>Length:要测试的物理地址范围,适用于所有测试。此长度应为 64 字节的倍数。</td></tr>
<tr><td>11h</td><td>1</td><td>Media Test Results Configuration<br>• Bit[0]: Error Signature Configuration: 0 = Complete; 1 = Single error signature<br>• Bits[7:1]: Reserved</td><td>Media Test Results Configuration<br>• Bit[0]:Error Signature Configuration:0 = Complete(完整);1 = Single error signature(单个错误签名)<br>• Bits[7:1]:保留</td></tr>
<tr><td>12h</td><td>1</td><td>Configuration Flags<br>• Bits[1:0]: ECC Disablement: 00b = Data ECC enabled & metadata ECC enabled; 01b = Data ECC disabled & metadata ECC enabled; 10b = Data ECC enabled & metadata ECC disabled; 11b = Data ECC disabled & metadata ECC disabled<br>• Bits[7:2]: Reserved</td><td>Configuration Flags<br>• Bits[1:0]:ECC Disablement:00b = 启用数据 ECC & 启用元数据 ECC;01b = 禁用数据 ECC & 启用元数据 ECC;10b = 启用数据 ECC & 禁用元数据 ECC;11b = 禁用数据 ECC & 禁用元数据 ECC<br>• Bits[7:2]:保留</td></tr>
<tr><td>13h</td><td>Dh</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

**Table 8-124. Test Parameters Entry Media Test Subclass | Test Parameters Entry Media Test Subclass**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: This field identifies the Test. The value discovered through the Media Test Capability Log Entry Structures (see Table 8-93).</td><td>Test ID:此字段标识测试。通过 Media Test Capability Log Entry Structures(参见表 8-93)发现的值。</td></tr>
<tr><td>02h</td><td>1</td><td>Number of iterations: Number of repetitions of the test.</td><td>Number of iterations:测试的重复次数。</td></tr>
<tr><td>03h</td><td>2</td><td>Flags<br>• Bit[0]: Inverse Pattern Enable<br>• Bit[1]: Exit on Uncorrectable Error<br>• Bit[2]: Error Count Threshold Programmed<br>• Bit[3]: Reserved<br>• Bits[7:4]: Addressing Mode: 0h = Ascending; 1h = Descending; 2h = Algorithm Specific; 3h = Random; All other values are reserved<br>• Bit[8]: Update Poison List on Uncorrectable Error<br>• Bits[15:9]: Reserved</td><td>标志位<br>• Bit[0]:Inverse Pattern Enable<br>• Bit[1]:Exit on Uncorrectable Error<br>• Bit[2]:Error Count Threshold Programmed<br>• Bit[3]:保留<br>• Bits[7:4]:Addressing Mode:0h = Ascending(升序);1h = Descending(降序);2h = Algorithm Specific(算法特定);3h = Random(随机);所有其他值保留<br>• Bit[8]:Update Poison List on Uncorrectable Error<br>• Bits[15:9]:保留</td></tr>
<tr><td>05h</td><td>2</td><td>Pattern Type: 00h = User provided; 01h = Vendor specific; 02h = PRBS; 03h = DPA[63:0] by eight; 04h = 55h; 05h = AAh; All other encodings are reserved</td><td>Pattern Type:00h = User provided;01h = Vendor specific;02h = PRBS;03h = DPA[63:0] by eight;04h = 55h;05h = AAh;所有其他编码保留</td></tr>
<tr><td>07h</td><td>1</td><td>Pattern Value: Pattern value provided by the user. This field is reserved if Pattern Type is not 00h.</td><td>Pattern Value:用户提供的 Pattern 值。如果 Pattern Type 不是 00h,则此字段保留。</td></tr>
<tr><td>08h</td><td>2</td><td>Vendor Specific: This field is set if Pattern Type field is 01h. The interpretation of this field is vendor specific.</td><td>Vendor Specific:如果 Pattern Type 字段为 01h,则设置此字段。此字段的解释由厂商定义。</td></tr>
<tr><td>0Ah</td><td>4</td><td>PRBS Seed: User provided PRBS Seed. This field is valid if Pattern Type is PRBS.</td><td>PRBS Seed:用户提供的 PRBS Seed。如果 Pattern Type 是 PRBS,则此字段有效。</td></tr>
<tr><td>0Eh</td><td>2</td><td>Error Count Threshold: User-programmable error count threshold.</td><td>Error Count Threshold:用户可编程错误计数阈值。</td></tr>
<tr><td>10h</td><td>10h</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Test Parameters (page 706-707) ｜ Test Parameters
>
> <img src="figures/chapter_08/page_0706.png" alt="Figure 8-X page 706" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0706.png)

**Table 8-125. Maintenance Operation: Classes, Subclasses, and Feature UUIDs | 维护操作:类、子类和 Feature UUID**

<table>
<thead>
<tr><th>Maintenance Operation Class</th><th>Class Description</th><th>Maintenance Operation Subclass</th><th>Subclass Description</th><th>UUID</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>No operation</td><td>00h</td><td>No operation</td><td>-</td></tr>
<tr><td>01h</td><td>PPR</td><td>00h</td><td>Soft PPR</td><td>892ba475-fad8-474e-9d3e-692c917568bb</td></tr>
<tr><td>01h</td><td>PPR</td><td>01h</td><td>Hard PPR</td><td>80ea4521-786f-4127-afb1-ec7459fb0e24</td></tr>
<tr><td>01h</td><td>PPR</td><td>Others</td><td>Reserved</td><td>-</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>00h</td><td>Cacheline - Memory Sparing</td><td>96C33386-91dd-44c7-9ecb-fdaf6503baC4</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>01h</td><td>Row - Memory Sparing</td><td>450ebf67-b135-4f97-a498-c2d57f279bed</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>02h</td><td>Bank - Memory Sparing</td><td>78b79636-90ac-4b64-A4ef-faac5d18a863</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>03h</td><td>Rank - Memory Sparing</td><td>34dbaff5-0552-4281-8f76-da0b5e7a76a7</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>Others</td><td>Reserved</td><td>-</td></tr>
<tr><td>03h</td><td>Device Built-in Test</td><td>00h</td><td>Media Test</td><td>No associated feature</td></tr>
<tr><td>03h</td><td>Device Built-in Test</td><td>01h to BFh</td><td>Reserved</td><td>-</td></tr>
<tr><td>03h</td><td>Device Built-in Test</td><td>0C0h to 0FFh</td><td>Vendor Specific</td><td>Vendor Specific</td></tr>
<tr><td>04h to DFh</td><td>Reserved</td><td>All</td><td>Reserved</td><td>-</td></tr>
<tr><td>E0h to FFh</td><td>Vendor specific</td><td>All</td><td>Vendor specific</td><td>Vendor specific</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>These Features represent maintenance operations capabilities and settings. Some fields of the Features are writable to configure the desired device behavior. Table 8-126 shows the Maintenance Operation Feature format. The first 16 bytes are common to all Maintenance Operation Features.</td><td style="background-color:#e8e8e8">这些 Feature 表示维护操作的能力和设置。Feature 的某些字段是可写的,以配置所需的设备行为。表 8-126 显示了 Maintenance Operation Feature 格式。前 16 个字节对于所有 Maintenance Operation Features 是通用的。</td></tr>
<tr><td>Row sparing in the Memory Sparing is equivalent to PPR; however, memory sparing is preferred when possible.</td><td style="background-color:#e8e8e8">Memory Sparing 中的 Row sparing 等同于 PPR;但是,当可能时,首选 memory sparing。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Maintenance Operation Classes/Subclasses (page 707) ｜ 维护操作类/子类
>
> <img src="figures/chapter_08/page_0707.png" alt="Figure 8-X page 707" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0707.png)

**Table 8-126. Common Maintenance Operation Feature Format | 通用维护操作 Feature 格式**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>RO</td><td>Maximum Maintenance Operation Latency: Bits[3:0] specify time scale (0h=1us, 1h=10us, 2h=100us, 3h=1ms, 4h=10ms, 5h=100ms, 6h=1s, 7h=10s); Bits[7:4] specify max operation latency with the time scale indicated in bits[3:0].</td></tr>
<tr><td>01h</td><td>2</td><td>RO</td><td>Operation Capabilities: Bit[0]: Device Initiated Capability; Bits[15:1]: Reserved</td></tr>
<tr><td>03h</td><td>2</td><td>RW</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved. Operation Mode default value is 0000h.</td></tr>
<tr><td>05h</td><td>1</td><td>RO</td><td>Maintenance Operation Class: This field specifies the Maintenance Operation Class.</td></tr>
<tr><td>06h</td><td>1</td><td>RO</td><td>Maintenance Operation Subclass: This field specifies the Maintenance Operation Subclass.</td></tr>
<tr><td>07h</td><td>9</td><td>RsvdZ</td><td>Reserved</td></tr>
<tr><td>10h</td><td>Varies</td><td>-</td><td>Operation specific fields</td></tr>
</tbody>
</table>

> **Figure 8-X.** Common Maintenance Operation Feature (page 708) ｜ 通用维护操作 Feature
>
> <img src="figures/chapter_08/page_0708.png" alt="Figure 8-X page 708" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0708.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2-1"></a>
#### 8.2.10.7.2.1 sPPR Feature Discovery and Configuration | sPPR 特性发现和配置

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The UUID of this feature is defined in Table 8-125.</td><td style="background-color:#e8e8e8">此特性的 UUID 在表 8-125 中定义。</td></tr>
<tr><td>Table 8-127 shows the information returned in the Get Supported Features output payload for the sPPR Feature. Some Feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-127 显示了 sPPR Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
</tbody>
</table>

**Table 8-127. Supported Feature Entry for the sPPR Feature | sPPR Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>892ba475-fad8-474e-9d3e-692c917568bb</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>14h</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>03h</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 010b if saved selection is supported (Bit[6] = 1); otherwise 000b (Deepest Reset Persistence)<br>• Bit[4]: Vendor-specific value (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: Vendor-specific value (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>03h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>03h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 0 (Configuration Change after Cold Reset)<br>• Bit[1]: 1 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log Change)<br>• Bit[5]: 0 (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 is recommended, 0 is permitted (CEL[11:10] Valid)<br>• Bit[10]: 0 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>18</td><td>Reserved</td><td>All 0s</td></tr>
</tbody>
</table>

**Table 8-128. sPPR Feature Readable Attributes | sPPR Feature 可读属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Maintenance Operation Latency: This field is defined in Table 8-126.</td><td>Maximum Maintenance Operation Latency:此字段在表 8-126 中定义。</td></tr>
<tr><td>01h</td><td>2</td><td>Operation Capabilities: This field is defined in Table 8-126. If Device Initiated capability bit is set to 1, the device has the capability to initiate sPPR maintenance without host involvement at runtime. Device Initiated capability bit shall be cleared to 0 if Restriction Flags bit[0] or bit[2] is set to 1.</td><td>Operation Capabilities:此字段在表 8-126 中定义。如果 Device Initiated capability 位设置为 1,则设备能够在运行时无需主机参与启动 sPPR 维护。如果 Restriction Flags 的 bit[0] 或 bit[2] 设置为 1,则 Device Initiated capability 位应清零为 0。</td></tr>
<tr><td>03h</td><td>2</td><td>Operation Mode: This field is defined in Table 8-126. If Device Initiated bit is set to 1, the device may initiate sPPR maintenance without host involvement at runtime.</td><td>Operation Mode:此字段在表 8-126 中定义。如果 Device Initiated 位设置为 1,则设备可以在运行时无需主机参与启动 sPPR 维护。</td></tr>
<tr><td>05h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h (PPR).</td><td>Maintenance Operation Class:应设置为 01h (PPR)。</td></tr>
<tr><td>06h</td><td>1</td><td>Maintenance Operation Subclass: It shall be cleared to 00h (Soft PPR).</td><td>Maintenance Operation Subclass:应清零为 00h (Soft PPR)。</td></tr>
<tr><td>07h</td><td>9</td><td>Reserved</td><td>保留</td></tr>
<tr><td>10h</td><td>1</td><td>sPPR Flags<br>• Bit[0]: DPA Support Flag: If set, the device supports DPA argument in the Perform Maintenance command input payload.<br>• Bit[1]: Nibble Support Flag: If set, the device supports Nibble Mask argument in the Perform Maintenance command input payload.<br>• Bit[2]: Memory Sparing Event Record Capability Flag: If set, the device has the capability to produce a Memory Sparing Event Record upon completion of sPPR maintenance operation.<br>• Bit[3]: Device Initiated at Device Boot Capability: A value of 1 indicates that the device has the capability to initiate the sPPR maintenance operation without host involvement when Memory_Active = 0.<br>• Bits[7:4]: Reserved</td><td>sPPR Flags<br>• Bit[0]:DPA Support Flag:如果设置,设备支持 Perform Maintenance 命令输入负载中的 DPA 参数。<br>• Bit[1]:Nibble Support Flag:如果设置,设备支持 Perform Maintenance 命令输入负载中的 Nibble Mask 参数。<br>• Bit[2]:Memory Sparing Event Record Capability Flag:如果设置,设备能够在 sPPR 维护操作完成时生成 Memory Sparing Event Record。<br>• Bit[3]:Device Initiated at Device Boot Capability:值 1 表示设备能够在 Memory_Active = 0 时无需主机参与启动 sPPR 维护操作。<br>• Bits[7:4]:保留</td></tr>
<tr><td>11h</td><td>2</td><td>Restriction Flags<br>• Bit[0]: 0 = CXL.mem requests are correctly processed; 1 = Media is not accessible.<br>• Bit[1]: Reserved.<br>• Bit[2]: 0 = Data is retained; 1 = Data may or may not be retained.<br>• Bits[15:3]: Reserved.</td><td>Restriction Flags<br>• Bit[0]:0 = 正确处理 CXL.mem 请求;1 = 介质不可访问。<br>• Bit[1]:保留。<br>• Bit[2]:0 = 保留数据;1 = 数据可能保留,也可能不保留。<br>• Bits[15:3]:保留。</td></tr>
<tr><td>13h</td><td>1</td><td>sPPR Operation Mode<br>• Bit[0]: Memory Sparing Event Record Enable<br>• Bit[1]: Device Initiated at Device Boot<br>• Bits[7:2]: Reserved</td><td>sPPR Operation Mode<br>• Bit[0]:Memory Sparing Event Record Enable<br>• Bit[1]:Device Initiated at Device Boot<br>• Bits[7:2]:保留</td></tr>
</tbody>
</table>

**Table 8-129. sPPR Feature Writable Attributes | sPPR Feature 可写属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved</td><td>Operation Mode:Bit[0]:Device Initiated;Bits[15:1]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>sPPR Operation Mode: Bit[0]: Memory Sparing Event Record Enable; Bit[1]: Device Initiated at Device Boot; Bits[7:2]: Reserved</td><td>sPPR Operation Mode:Bit[0]:Memory Sparing Event Record Enable;Bit[1]:Device Initiated at Device Boot;Bits[7:2]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** sPPR Feature (page 709-711) ｜ sPPR Feature
>
> <img src="figures/chapter_08/page_0709.png" alt="Figure 8-X page 709" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0709.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2-2"></a>
#### 8.2.10.7.2.2 hPPR Feature Discovery and Configuration | hPPR 特性发现和配置

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The UUID of this feature is defined in Table 8-125.</td><td style="background-color:#e8e8e8">此特性的 UUID 在表 8-125 中定义。</td></tr>
<tr><td>Table 8-130 shows the information returned in the Get Supported Features output payload for the hPPR Feature. Some Feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-130 显示了 hPPR Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
</tbody>
</table>

**Table 8-130. Supported Feature Entry for the hPPR Feature | hPPR Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>80ea4521-786f-4127-afb1-ec7459fb0e24</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>14h</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>03h</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 010b if saved selection is supported (Bit[6] = 1); otherwise, 000b (Deepest Reset Persistence)<br>• Bit[4]: Vendor-specific value (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: Vendor-specific value (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>03h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>03h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 0 (Configuration Change after Cold Reset)<br>• Bit[1]: 1 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log change)<br>• Bit[5]: 0 (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 is recommended, 0 is permitted (CEL[11:10] Valid)<br>• Bit[10]: 0 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>2</td><td>Reserved</td><td>All 0s</td></tr>
</tbody>
</table>

**Table 8-131. hPPR Feature Readable Attributes | hPPR Feature 可读属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Maintenance Operation Latency: This field is defined in Table 8-126.</td><td>Maximum Maintenance Operation Latency:此字段在表 8-126 中定义。</td></tr>
<tr><td>01h</td><td>2</td><td>Operation Capabilities: This field is defined in Table 8-126. If Device Initiated capability bit is set to 1, the device has the capability to initiate hPPR maintenance without host involvement at runtime. Device Initiated capability bit shall be cleared to 0 if Restriction Flags Bit[0] or Bit[2] is set to 1.</td><td>Operation Capabilities:此字段在表 8-126 中定义。如果 Device Initiated capability 位设置为 1,则设备能够在运行时无需主机参与启动 hPPR 维护。如果 Restriction Flags 的 Bit[0] 或 Bit[2] 设置为 1,则 Device Initiated capability 位应清零为 0。</td></tr>
<tr><td>03h</td><td>2</td><td>Operation Mode: This field is defined in Table 8-126. If Device Initiated bit is set to 1, the device may initiate hPPR maintenance without host involvement at runtime.</td><td>Operation Mode:此字段在表 8-126 中定义。如果 Device Initiated 位设置为 1,则设备可以在运行时无需主机参与启动 hPPR 维护。</td></tr>
<tr><td>05h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h (PPR).</td><td>Maintenance Operation Class:应设置为 01h (PPR)。</td></tr>
<tr><td>06h</td><td>1</td><td>Maintenance Operation Subclass: It shall be set to 01h (Hard PPR).</td><td>Maintenance Operation Subclass:应设置为 01h (Hard PPR)。</td></tr>
<tr><td>07h</td><td>9</td><td>Reserved</td><td>保留</td></tr>
<tr><td>10h</td><td>1</td><td>hPPR Flags<br>• Bit[0]: DPA Support Flag<br>• Bit[1]: Nibble Support Flag<br>• Bit[2]: Memory Sparing Event Record Capability Flag<br>• Bit[3]: Device Initiated at Device Boot Capability<br>• Bits[7:4]: Reserved</td><td>hPPR Flags<br>• Bit[0]:DPA Support Flag<br>• Bit[1]:Nibble Support Flag<br>• Bit[2]:Memory Sparing Event Record Capability Flag<br>• Bit[3]:Device Initiated at Device Boot Capability<br>• Bits[7:4]:保留</td></tr>
<tr><td>11h</td><td>2</td><td>Restriction Flags<br>• Bit[0]: 0 = CXL.mem requests are correctly processed; 1 = Media is not accessible.<br>• Bit[1]: Reserved.<br>• Bit[2]: 0 = Data is retained; 1 = Data may or may not be retained.<br>• Bits[15:3]: Reserved.</td><td>Restriction Flags<br>• Bit[0]:0 = 正确处理 CXL.mem 请求;1 = 介质不可访问。<br>• Bit[1]:保留。<br>• Bit[2]:0 = 保留数据;1 = 数据可能保留,也可能不保留。<br>• Bits[15:3]:保留。</td></tr>
<tr><td>13h</td><td>1</td><td>hPPR Operation Mode<br>• Bit[0]: Memory Sparing Event Record Enable<br>• Bit[1]: Device Initiated at Device Boot<br>• Bits[7:2]: Reserved</td><td>hPPR Operation Mode<br>• Bit[0]:Memory Sparing Event Record Enable<br>• Bit[1]:Device Initiated at Device Boot<br>• Bits[7:2]:保留</td></tr>
</tbody>
</table>

**Table 8-132. hPPR Feature Writable Attributes | hPPR Feature 可写属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved</td><td>Operation Mode:Bit[0]:Device Initiated;Bits[15:1]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>hPPR Operation Mode: Bit[0]: Memory Sparing Event Record Enable; Bit[1]: Device Initiated at Device Boot; Bits[7:2]: Reserved</td><td>hPPR Operation Mode:Bit[0]:Memory Sparing Event Record Enable;Bit[1]:Device Initiated at Device Boot;Bits[7:2]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** hPPR Feature (page 711-713) ｜ hPPR Feature
>
> <img src="figures/chapter_08/page_0711.png" alt="Figure 8-X page 711" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0711.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2-3"></a>
#### 8.2.10.7.2.3 Memory Sparing Features | 内存备用 Feature

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The UUIDs associated with these features are defined in Table 8-125.</td><td style="background-color:#e8e8e8">与此特性关联的 UUID 在表 8-125 中定义。</td></tr>
<tr><td>Table 8-133 shows the information returned in the Get Supported Features output payload for the Enhanced Memory Sparing Feature. Some Feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-133 显示了 Enhanced Memory Sparing Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
</tbody>
</table>

**Table 8-133. Supported Feature Entry for the Memory Sparing Feature | Memory Sparing Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>Depends on the Maintenance Operation subclass (see Table 8-125 for details)</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>13h</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>02h</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 000b (Deepest Reset Persistence=None. Any reset will restore the default value.)<br>• Bit[4]: 0 (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: Vendor-specific value (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>01h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>01h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 0 (Configuration Change after Cold Reset)<br>• Bit[1]: 1 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log Change)<br>• Bit[5]: 0 (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 (CEL[11:10] Valid)<br>• Bit[10]: 0 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>12h</td><td>Reserved</td><td>All 0s</td></tr>
</tbody>
</table>

**Table 8-134. Memory Sparing Feature Readable Attributes | Memory Sparing Feature 可读属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Maintenance Operation Latency: This field is defined in Table 8-126.</td><td>Maximum Maintenance Operation Latency:此字段在表 8-126 中定义。</td></tr>
<tr><td>01h</td><td>2</td><td>Operation Capabilities: This field is defined in Table 8-126. Device Initiated capability bit shall be cleared to 0 if Restriction flags bit[0] is set to 1.</td><td>Operation Capabilities:此字段在表 8-126 中定义。如果 Restriction flags 的 bit[0] 设置为 1,则 Device Initiated capability 位应清零为 0。</td></tr>
<tr><td>03h</td><td>2</td><td>Operation Mode: This field is defined in Table 8-126.</td><td>Operation Mode:此字段在表 8-126 中定义。</td></tr>
<tr><td>05h</td><td>1</td><td>Maintenance Operation Class: This field shall be set to 02h (Memory Sparing).</td><td>Maintenance Operation Class:此字段应设置为 02h (Memory Sparing)。</td></tr>
<tr><td>06h</td><td>1</td><td>Maintenance Operation Subclass: Depends on the scope of the sparing needed.</td><td>Maintenance Operation Subclass:取决于所需备用的范围。</td></tr>
<tr><td>07h</td><td>0Ah</td><td>Reserved</td><td>保留</td></tr>
<tr><td>11h</td><td>2</td><td>Restriction Flags<br>• Bit[0]: Sparing Side Effects: 0 = The device preserves the memory content and remains responsive to CXL.mem requests during the sparing operation. 1 = The device is permitted to drop CXL.mem write requests, return poison in response to CXL.mem read requests during the sparing operation. The device does not guarantee preservation of HDM contents across the sparing operation.<br>• Bit[1]: Hard Sparing: If set, the device has the capability for performing the sparing that is irreversible and that can survive any Conventional Reset.<br>• Bit[2]: Soft Sparing: If set, the device has the capability for performing the sparing in a non-permanent way; thus, the change will be reverted after any Conventional Reset.<br>• Bits[15:3]: Reserved.</td><td>Restriction Flags<br>• Bit[0]:Sparing Side Effects:0 = 设备在备用操作期间保留内存内容并保持对 CXL.mem 请求的响应。1 = 设备允许在备用操作期间丢弃 CXL.mem 写入请求,并对 CXL.mem 读取请求返回 poison。设备不保证在备用操作期间保留 HDM 内容。<br>• Bit[1]:Hard Sparing:如果设置,设备具有执行不可逆备用且可在任何 Conventional Reset 后存活的能力。<br>• Bit[2]:Soft Sparing:如果设置,设备具有以非永久方式执行备用的能力;因此,更改将在任何 Conventional Reset 后被恢复。<br>• Bits[15:3]:保留。</td></tr>
</tbody>
</table>

**Table 8-135. Memory Sparing Feature Writable Attributes | Memory Sparing Feature 可写属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved</td><td>Operation Mode:Bit[0]:Device Initiated;Bits[15:1]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Memory Sparing Feature (page 714-715) ｜ Memory Sparing Feature
>
> <img src="figures/chapter_08/page_0714.png" alt="Figure 8-X page 714" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0714.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8"></a>
## 8.2.10.8 PBR Component Command Set | PBR 组件命令集

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Support for this command set is required for all devices that are PBR link capable (i.e., PBR switches and GFDs).</td><td style="background-color:#e8e8e8">所有支持 PBR 链路的设备(即 PBR 交换机和 GFD)都需要支持此命令集。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8-1"></a>
### 8.2.10.8.1 Identify PBR Component (Opcode 0700h) | 标识 PBR 组件 (操作码 0700h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command provides information about a component specific to its PBR fabric capabilities.</td><td style="background-color:#e8e8e8">此命令提供有关特定于其 PBR fabric 能力的组件的信息。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-136. Identify PBR Component Response Payload | Identify PBR Component 响应负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>• Bits[11:0]: PID: Assigned PID of this device or FFFh if no PID has been assigned<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:PID:此设备的分配 PID,或 FFFh(如果尚未分配 PID)<br>• Bits[15:12]:保留</td></tr>
<tr><td>02h</td><td>2</td><td>• Bits[11:0]: Primary FM PID: PID of the FM registered as primary FM. A value of FFFh indicates no primary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Primary FM PID:注册为 primary FM 的 FM 的 PID。值 FFFh 表示未注册 primary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>04h</td><td>10h</td><td>Primary FM UUID: UUID of the FM registered as primary FM.</td><td>Primary FM UUID:注册为 primary FM 的 FM 的 UUID。</td></tr>
<tr><td>14h</td><td>2</td><td>• Bits[11:0]: Secondary FM PID: PID of the FM registered as secondary FM. A value of FFFh indicates no secondary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Secondary FM PID:注册为 secondary FM 的 FM 的 PID。值 FFFh 表示未注册 secondary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>16h</td><td>10h</td><td>Secondary FM UUID: UUID of the FM registered as secondary FM.</td><td>Secondary FM UUID:注册为 secondary FM 的 FM 的 UUID。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Identify PBR Component (page 716) ｜ Identify PBR Component
>
> <img src="figures/chapter_08/page_0716.png" alt="Figure 8-X page 716" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0716.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8-2"></a>
### 8.2.10.8.2 Claim Ownership (Opcode 0701h) | 声明所有权 (操作码 0701h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command is used by an FM to register itself as either the primary or secondary FM. The device's PID is also assigned as part of this operation. The device's PID assignment shall only be updated if the FW ownership registration operation is successful.</td><td style="background-color:#e8e8e8">此命令由 FM 用于将自身注册为 primary 或 secondary FM。设备的 PID 也作为此操作的一部分进行分配。仅当 FW 所有权注册操作成功时,设备的 PID 分配才会更新。</td></tr>
<tr><td>Registration of FMs and assignment of a PID apply to all CCIs on a PBR component.</td><td style="background-color:#e8e8e8">FM 的注册和 PID 的分配适用于 PBR 组件上的所有 CCI。</td></tr>
<tr><td>Operation 0 (Register Primary FM and assign PID) shall fail with "Invalid Input" if a device already has a primary FM registered.</td><td style="background-color:#e8e8e8">如果设备已注册 primary FM,则操作 0(Register Primary FM and assign PID)应以 "Invalid Input" 失败。</td></tr>
<tr><td>Operation 1 (Register Secondary FM) shall fail with "Invalid Input" if a device already has a secondary FM registered or if the request was initiated by an FM other than the registered primary FM.</td><td style="background-color:#e8e8e8">如果设备已注册 secondary FM,或请求由已注册 primary FM 之外的 FM 发起,则操作 1(Register Secondary FM)应以 "Invalid Input" 失败。</td></tr>
<tr><td>Operation 2 (Update PID) is valid only when received from the primary FM and shall terminate with "Invalid Input" otherwise.</td><td style="background-color:#e8e8e8">操作 2(Update PID)仅当从 primary FM 接收时有效,否则应以 "Invalid Input" 终止。</td></tr>
<tr><td>Operation 3 (Promote Secondary FM) is valid only when received from the secondary FM and shall terminate with "Invalid Input" otherwise.</td><td style="background-color:#e8e8e8">操作 3(Promote Secondary FM)仅当从 secondary FM 接收时有效,否则应以 "Invalid Input" 终止。</td></tr>
<tr><td>Promoting a secondary FM to the primary FM position leaves the secondary FM position unregistered.</td><td style="background-color:#e8e8e8">将 secondary FM 提升到 primary FM 位置会使 secondary FM 位置未注册。</td></tr>
<tr><td>Attempting to register or assign a PID of FFFh shall result in an "Invalid Input" failure return code.</td><td style="background-color:#e8e8e8">尝试注册或分配 PID 为 FFFh 将导致 "Invalid Input" 失败返回码。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-137. Claim Ownership Request Payload | Claim Ownership 请求负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>1</td><td>Operation: 00h = Register Primary FM and assign PID; 01h = Register Secondary FM; 02h = Update PID; 03h = Promote Secondary FM; All other encodings are reserved</td><td>Operation:00h = Register Primary FM and assign PID;01h = Register Secondary FM;02h = Update PID;03h = Promote Secondary FM;所有其他编码保留</td></tr>
<tr><td>1h</td><td>2</td><td>• Bits[11:0]: FM PID: PID of the FM requesting ownership. Valid only if Operation is cleared to 00h or set to 01h.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:FM PID:请求所有权的 FM 的 PID。仅当 Operation 清零为 00h 或设置为 01h 时有效。<br>• Bits[15:12]:保留</td></tr>
<tr><td>3h</td><td>10h</td><td>UUID: UUID of the FM requesting ownership. Valid only if Operation is cleared to 00h or set to 01h.</td><td>UUID:请求所有权的 FM 的 UUID。仅当 Operation 清零为 00h 或设置为 01h 时有效。</td></tr>
<tr><td>13h</td><td>2</td><td>• Bits[11:0]: Assigned PID: PID value being assigned to the device. Valid only if Operation is 00h or 02h.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Assigned PID:分配给设备的 PID 值。仅当 Operation 为 00h 或 02h 时有效。<br>• Bits[15:12]:保留</td></tr>
</tbody>
</table>

**Table 8-138. Claim Ownership Response Payload | Claim Ownership 响应负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>2</td><td>• Bits[11:0]: Primary FM PID: PID of the FM registered as primary FM. A value of FFFh indicates no primary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Primary FM PID:注册为 primary FM 的 FM 的 PID。值 FFFh 表示未注册 primary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>2h</td><td>10h</td><td>Primary FM UUID: UUID of the FM registered as primary FM.</td><td>Primary FM UUID:注册为 primary FM 的 FM 的 UUID。</td></tr>
<tr><td>12h</td><td>2</td><td>• Bits[11:0]: Secondary FM PID: PID of the FM registered as secondary FM. A value of FFFh indicates no secondary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Secondary FM PID:注册为 secondary FM 的 FM 的 PID。值 FFFh 表示未注册 secondary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>14h</td><td>10h</td><td>Secondary FM UUID: UUID of the FM registered as secondary FM.</td><td>Secondary FM UUID:注册为 secondary FM 的 FM 的 UUID。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Claim Ownership (page 717) ｜ Claim Ownership
>
> <img src="figures/chapter_08/page_0717.png" alt="Figure 8-X page 717" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0717.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8-3"></a>
### 8.2.10.8.3 Read CDAT (Opcode 0702h) | 读取 CDAT (操作码 0702h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command is used to read the CDAT from GAEs and GFDs.</td><td style="background-color:#e8e8e8">此命令用于从 GAE 和 GFD 读取 CDAT。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-139. Read CDAT Request Payload | Read CDAT 请求负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>2</td><td>• Bits[11:0]: Target PID: PID of device routing path CDAT to query. Valid only for PBR switches.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Target PID:要查询其 CDAT 的设备路由路径的 PID。仅对 PBR 交换机有效。<br>• Bits[15:12]:保留</td></tr>
<tr><td>2h</td><td>2</td><td>Reserved</td><td>保留</td></tr>
<tr><td>4h</td><td>8</td><td>Start Byte: Offset in bytes into CDAT Data.</td><td>Start Byte:CDAT 数据中的字节偏移量。</td></tr>
<tr><td>Ch</td><td>8</td><td>Number of Bytes: Size in bytes of CDAT Data requested.</td><td>Number of Bytes:请求的 CDAT 数据的大小(以字节为单位)。</td></tr>
</tbody>
</table>

**Table 8-140. Read CDAT Response Payload | Read CDAT 响应负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>8</td><td>Total CDAT Size: Size in bytes of the full CDAT.</td><td>Total CDAT Size:完整 CDAT 的大小(以字节为单位)。</td></tr>
<tr><td>8h</td><td>8</td><td>Number of Bytes: Size in bytes of returned CDAT Data.</td><td>Number of Bytes:返回的 CDAT 数据的大小(以字节为单位)。</td></tr>
<tr><td>10h</td><td>Varies</td><td>CDAT Data: CDAT for the specified target, as defined in the CDAT Specification.</td><td>CDAT Data:指定目标的 CDAT,定义见 CDAT 规范。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Read CDAT (page 718) ｜ Read CDAT
>
> <img src="figures/chapter_08/page_0718.png" alt="Figure 8-X page 718" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0718.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9"></a>
## 8.2.10.9 Memory Device Command Sets | 内存设备命令集

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section describes the commands specific to CXL memory devices that implement the PCIe Configuration Space Header Class Code defined in Section 8.1.12.1, advertise Memory Device Command support in the Mailbox Capabilities register (see Section 8.2.9.4.3), or report a Type value of 03h or 04h in the Identify response payload.</td><td style="background-color:#e8e8e8">本节描述特定于 CXL memory device 的命令,这些设备实现 8.1.12.1 节中定义的 PCIe Configuration Space Header Class Code,在 Mailbox Capabilities 寄存器(参见 8.2.9.4.3 节)中通告 Memory Device Command 支持,或在 Identify 响应负载中报告 Type 值为 03h 或 04h。</td></tr>
<tr><td>Opcodes also provide an implicit major version number, which means a command's definition shall not change in an incompatible way in future revisions of this specification. Instead, if an incompatible change is required, the specification defining the change shall define a new opcode for the changed command. Commands may evolve by defining new fields in the payload definitions that were originally defined as Reserved, but only in a way where software written using the earlier definition will continue to work correctly, and software written to the new definition can use the 0 value or the payload size to detect devices that do not support the new field. This implicit minor versioning allows software to be written with the understanding that an opcode shall only evolve by adding backward-compatible changes.</td><td style="background-color:#e8e8e8">操作码还提供隐式的主版本号,这意味着命令定义不应在本规范的未来修订版中以不兼容的方式更改。相反,如果需要不兼容的更改,则定义更改的规范应为更改的命令定义新的操作码。命令可以通过在最初定义为保留的负载定义中定义新字段来演进,但只能以使用早期定义编写的软件将继续正常工作的方式,并且编写为新定义的软件可以使用值 0 或负载大小来检测不支持新字段的设备。这种隐式次要版本控制允许软件在理解以下情况的基础上编写:操作码应仅通过添加向后兼容的更改来演进。</td></tr>
<tr><td>Table 8-141 and the following sections use the terms "Persistent memory device" and "CXL Memory Device that supports Persistence" interchangeably. A persistent memory device behaves in the following ways:<br>• All writes targeting persistent memory ranges that have been completed on CXL, but are still held in volatile buffers on the device, shall be flushed to media under the following conditions:<br>  — Any reset event<br>  — Reception of GPF Phase 2<br>  — Surprise power loss<br>• If the device is unable, for any reason, to flush all the writes that have been completed on CXL to persistent memory successfully, the Device shall increment the Dirty Shutdown Count in the Health Info (see Table 8-148) on the next reset. Incrementing the Dirty Shutdown Count may be considered a failure event by the Host and may indicate user data loss.</td><td style="background-color:#e8e8e8">表 8-141 和以下各节中,术语 "Persistent memory device" 和 "CXL Memory Device that supports Persistence" 可以互换使用。持久性内存设备的行为方式如下:<br>• 所有针对已在 CXL 上完成但仍保留在设备上的易失性缓冲区中的持久性内存范围的写入,应在以下条件下刷新到介质:<br>  — 任何复位事件<br>  — 接收 GPF Phase 2<br>  — 意外断电<br>• 如果设备由于任何原因无法成功刷新所有已在 CXL 上完成到持久性内存的写入,则设备应在下次复位时增加 Health Info(参见表 8-148)中的 Dirty Shutdown Count。增加 Dirty Shutdown Count 可能被主机视为故障事件,并可能表示用户数据丢失。</td></tr>
</tbody>
</table>

> **Figure 8-X.** CXL Defined Memory Device Command Opcodes (page 719) ｜ CXL 定义的内存设备命令操作码
>
> <img src="figures/chapter_08/page_0719.png" alt="Figure 8-X page 719" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0719.png)

**Table 8-141. CXL Defined Memory Device Command Opcodes (Vendor ID = 1E98h or 0000h) | CXL 定义的内存设备命令操作码 (Vendor ID = 1E98h 或 0000h)**

<table>
<thead>
<tr><th>Bits[15:8]</th><th>Command</th><th>Bits[7:0]</th><th>Combined Opcode</th><th>Required Type 1/2/3 Device</th><th>Required GFD</th><th>Command Set</th></tr>
</thead>
<tbody>
<tr><td>40h</td><td>Identify Memory Device</td><td>00h</td><td>4000h</td><td>M</td><td>M</td><td>Identify Memory Device (Section 8.2.10.9.1.1)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>00h</td><td>4100h</td><td>O</td><td>P</td><td>Get Partition Info (Section 8.2.10.9.2.1)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>01h</td><td>4101h</td><td>O</td><td>P</td><td>Set Partition Info (Section 8.2.10.9.2.2)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>02h</td><td>4102h</td><td>PM</td><td>P</td><td>Get LSA (Section 8.2.10.9.2.3)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>03h</td><td>4103h</td><td>PM</td><td>P</td><td>Set LSA (Section 8.2.10.9.2.4)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>00h</td><td>4200h</td><td>M</td><td>M</td><td>Get Health Info (Section 8.2.10.9.3.1)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>01h</td><td>4201h</td><td>M</td><td>M</td><td>Get Alert Configuration (Section 8.2.10.9.3.2)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>02h</td><td>4202h</td><td>M</td><td>M</td><td>Set Alert Configuration (Section 8.2.10.9.3.3)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>03h</td><td>4203h</td><td>PM</td><td>P</td><td>Get Shutdown State (Section 8.2.10.9.3.4)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>04h</td><td>4204h</td><td>PM</td><td>P</td><td>Set Shutdown State (Section 8.2.10.9.3.5)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>00h</td><td>4300h</td><td>PM</td><td>O</td><td>Get Poison List (Section 8.2.10.9.4.1)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>01h</td><td>4301h</td><td>O</td><td>O</td><td>Inject Poison (Section 8.2.10.9.4.2)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>02h</td><td>4302h</td><td>O</td><td>O</td><td>Clear Poison (Section 8.2.10.9.4.3)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>03h</td><td>4303h</td><td>PM</td><td>O</td><td>Get Scan Media Capabilities (Section 8.2.10.9.4.4)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>04h</td><td>4304h</td><td>PM</td><td>O</td><td>Scan Media (Section 8.2.10.9.4.5)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>05h</td><td>4305h</td><td>PM</td><td>O</td><td>Get Scan Media Results (Section 8.2.10.9.4.6)</td></tr>
<tr><td>44h</td><td>Sanitize and Media Operations</td><td>00h</td><td>4400h</td><td>O</td><td>O</td><td>Sanitize (Section 8.2.10.9.5.1)</td></tr>
<tr><td>44h</td><td>Sanitize and Media Operations</td><td>01h</td><td>4401h</td><td>O</td><td>O</td><td>Secure Erase (Section 8.2.10.9.5.2)</td></tr>
<tr><td>44h</td><td>Sanitize and Media Operations</td><td>02h</td><td>4402h</td><td>O</td><td>O</td><td>Media Operations (Section 8.2.10.9.5.3)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>00h</td><td>4500h</td><td>O</td><td>P</td><td>Get Security State (Section 8.2.10.9.6.1)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>01h</td><td>4501h</td><td>O</td><td>P</td><td>Set Passphrase (Section 8.2.10.9.6.2)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>02h</td><td>4502h</td><td>O</td><td>P</td><td>Disable Passphrase (Section 8.2.10.9.6.3)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>03h</td><td>4503h</td><td>O</td><td>P</td><td>Unlock (Section 8.2.10.9.6.4)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>04h</td><td>4504h</td><td>O</td><td>P</td><td>Freeze Security State (Section 8.2.10.9.6.5)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>05h</td><td>4505h</td><td>O</td><td>P</td><td>Passphrase Secure Erase (Section 8.2.10.9.6.6)</td></tr>
<tr><td>46h</td><td>Security Passthrough</td><td>00h</td><td>4600h</td><td>O</td><td>P</td><td>Security Send (Section 8.2.10.9.7.1)</td></tr>
<tr><td>46h</td><td>Security Passthrough</td><td>01h</td><td>4601h</td><td>O</td><td>P</td><td>Security Receive (Section 8.2.10.9.7.2)</td></tr>
<tr><td>47h</td><td>SLD QoS Telemetry</td><td>00h</td><td>4700h</td><td>O</td><td>P</td><td>Get SLD QoS Control (Section 8.2.10.9.8.1)</td></tr>
<tr><td>47h</td><td>SLD QoS Telemetry</td><td>01h</td><td>4701h</td><td>O</td><td>P</td><td>Set SLD QoS Control (Section 8.2.10.9.8.2)</td></tr>
<tr><td>47h</td><td>SLD QoS Telemetry</td><td>02h</td><td>4702h</td><td>O</td><td>P</td><td>Get SLD QoS Status (Section 8.2.10.9.8.3)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>00h</td><td>4800h</td><td>DC</td><td>P</td><td>Get Dynamic Capacity Configuration (Section 8.2.10.9.9.1)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>01h</td><td>4801h</td><td>DC</td><td>P</td><td>Get Dynamic Capacity Extent List (Section 8.2.10.9.9.2)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>02h</td><td>4802h</td><td>DC</td><td>P</td><td>Add Dynamic Capacity Response (Section 8.2.10.9.9.3)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>03h</td><td>4803h</td><td>DC</td><td>P</td><td>Release Dynamic Capacity (Section 8.2.10.9.9.4)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>00h</td><td>4900h</td><td>P</td><td>M</td><td>Identify GFD (Section 8.2.10.9.10.1)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>01h</td><td>4901h</td><td>P</td><td>M</td><td>Get GFD Status (Section 8.2.10.9.10.2)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>02h</td><td>4902h</td><td>P</td><td>M</td><td>Get GFD DC Region Configuration (Section 8.2.10.9.10.3)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>03h</td><td>4903h</td><td>P</td><td>O</td><td>Set GFD DC Region Configuration (Section 8.2.10.9.10.4)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>04h</td><td>4904h</td><td>P</td><td>M</td><td>Get GFD DC Region Extent Lists (Section 8.2.10.9.10.5)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>05h</td><td>4905h</td><td>P</td><td>M</td><td>Get GFD DMP Configuration (Section 8.2.10.9.10.6)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>06h</td><td>4906h</td><td>P</td><td>O</td><td>Set GFD DMP Configuration (Section 8.2.10.9.10.7)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>07h</td><td>4907h</td><td>P</td><td>M</td><td>GFD Dynamic Capacity Add (Section 8.2.10.9.10.8)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>08h</td><td>4908h</td><td>P</td><td>M</td><td>GFD Dynamic Capacity Release (Section 8.2.10.9.10.9)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>09h</td><td>4909h</td><td>P</td><td>O</td><td>GFD Dynamic Capacity Add Reference (Section 8.2.10.9.10.10)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Ah</td><td>490Ah</td><td>P</td><td>O</td><td>GFD Dynamic Capacity Remove Reference (Section 8.2.10.9.10.11)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Bh</td><td>490Bh</td><td>P</td><td>O</td><td>GFD Dynamic Capacity List Tags (Section 8.2.10.9.10.12)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Ch</td><td>490Ch</td><td>P</td><td>M</td><td>Get GFD SAT Entry (Section 8.2.10.9.10.13)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Dh</td><td>490Dh</td><td>P</td><td>M</td><td>Set GFD SAT Entry (Section 8.2.10.9.10.14)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Eh</td><td>490Eh</td><td>P</td><td>M</td><td>Get GFD QoS Control (Section 8.2.10.9.10.15)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Fh</td><td>490Fh</td><td>P</td><td>M</td><td>Set GFD QoS Control (Section 8.2.10.9.10.16)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>10h</td><td>4910h</td><td>P</td><td>M</td><td>Get GFD QoS Status (Section 8.2.10.9.10.17)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>11h</td><td>4911h</td><td>P</td><td>M</td><td>Get GFD QoS BW Limit (Section 8.2.10.9.10.18)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>12h</td><td>4912h</td><td>P</td><td>M</td><td>Set GFD QoS BW Limit (Section 8.2.10.9.10.19)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>13h</td><td>4913h</td><td>P</td><td>M</td><td>Get GDT Configuration (Section 8.2.10.9.10.20)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>14h</td><td>4914h</td><td>P</td><td>M</td><td>Set GDT Configuration (Section 8.2.10.9.10.21)</td></tr>
</tbody>
</table>

> **Notes | 注释:**
> 1. M = Mandatory(强制);PM = Mandatory for devices that support persistence(支持持久性设备的强制);DC = mandatory for devices that support Dynamic Capacity(支持动态容量设备的强制);O = Optional(可选);P = Prohibited(禁止)。It is prohibited for switches to support any commands from the Memory Device Command Set(交换机禁止支持 Memory Device Command Set 中的任何命令)。
> 2. "FM Interface" refers to commands issued/received via the Fabric Crawl Out mechanism.
> 3. "Host Interface" refers to commands issued/received via the GFD Proxying mechanism.
> 4. Systems capable of management from Mailbox registers and an MCTP-based CCI shall ensure that these commands are not issued as MCTP messages while a device's mailboxes are operational.

> **Figure 8-X.** CXL Defined Memory Device Command Opcodes Sheet 2-3 (page 720-721) ｜ CXL 定义的内存设备命令操作码(续)
>
> <img src="figures/chapter_08/page_0720.png" alt="Figure 8-X page 720" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0720.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-1-1"></a>
### 8.2.10.9.1.1 Identify Memory Device (Opcode 4000h) | 标识内存设备 (操作码 4000h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve basic information about the memory device. If the HDM_Count field in DVSEC CXL Capability is 01b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low (see Section 8.1.3.8.2) is 01b. If the HDM_Count field in DVSEC CXL Capability is 10b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low as well as DVSEC CXL Range 2 Size Low (see Section 8.1.3.8.6) are both 1.</td><td style="background-color:#e8e8e8">检索有关内存设备的基本信息。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 01b,则仅当 DVSEC CXL Range 1 Size Low(参见 8.1.3.8.2 节)中的 Memory_Info_Valid 标志为 01b 时,输出负载才有效。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 10b,则仅当 DVSEC CXL Range 1 Size Low 和 DVSEC CXL Range 2 Size Low(参见 8.1.3.8.6 节)中的 Memory_Info_Valid 标志均为 1 时,输出负载才有效。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> CXL components shall interpret the PCIe MMB Command Opcode Vendor ID = 1E98h or 0000h with CXL defined commands. 0000h is a PCI-SIG reserved value for legacy CXL compatibility. However, it is strongly recommended for callers to use the CXL Vendor ID (1E98h) to identify CXL defined commands.
>
> CXL 组件应使用 CXL 定义命令解释 PCIe MMB Command Opcode Vendor ID = 1E98h 或 0000h。0000h 是 PCI-SIG 为旧版 CXL 兼容性保留的值。但是,强烈建议调用者使用 CXL Vendor ID (1E98h) 来标识 CXL 定义命令。

**Table 8-142. Identify Memory Device Output Payload | Identify Memory Device 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>16</td><td>FW Revision: Contains the revision of the active FW formatted as an ASCII string.</td><td>FW Revision:包含活动 FW 的修订版,格式为 ASCII 字符串。</td></tr>
<tr><td>10h</td><td>8</td><td>Total Capacity: This field indicates the total usable capacity of the device. Expressed in multiples of 256 MB. Total Capacity shall be greater than or equal to the sum of Volatile Only Capacity and Persistent Only Capacity.</td><td>Total Capacity:此字段指示设备的总可用容量。以 256 MB 的倍数表示。Total Capacity 应大于或等于 Volatile Only Capacity 和 Persistent Only Capacity 之和。</td></tr>
<tr><td>18h</td><td>8</td><td>Volatile Only Capacity: This field indicates the total usable capacity of the device that may be used only as volatile memory. Expressed in multiples of 256 MB.</td><td>Volatile Only Capacity:此字段指示设备可用作易失性内存的总可用容量。以 256 MB 的倍数表示。</td></tr>
<tr><td>20h</td><td>8</td><td>Persistent Only Capacity: This field indicates the total usable capacity of the device that may be used only as persistent memory. Expressed in multiples of 256 MB.</td><td>Persistent Only Capacity:此字段指示设备可用作持久性内存的总可用容量。以 256 MB 的倍数表示。</td></tr>
<tr><td>28h</td><td>8</td><td>Partition Alignment: If the device has capacity that may be used as either volatile memory or persistent memory, this field indicates the partition alignment size. Expressed in multiples of 256 MB. Partitionable capacity is equal to Total Capacity - Volatile Only Capacity - Persistent Only Capacity. If 0, the device doesn't support partitioning the capacity into both volatile capacity and persistent capacity.</td><td>Partition Alignment:如果设备具有可用作易失性内存或持久性内存的容量,则此字段指示分区对齐大小。以 256 MB 的倍数表示。可分区容量等于 Total Capacity - Volatile Only Capacity - Persistent Only Capacity。如果为 0,则设备不支持将容量分区为易失性容量和持久性容量。</td></tr>
<tr><td>30h</td><td>2</td><td>Informational Event Log Size: The number of events that the device can store in the Informational Event Log before the log overflows.</td><td>Informational Event Log Size:设备在日志溢出之前可以在 Informational Event Log 中存储的事件数。</td></tr>
<tr><td>32h</td><td>2</td><td>Warning Event Log Size: The number of events that the device can store in the Warning Event Log before the log overflows.</td><td>Warning Event Log Size:设备在日志溢出之前可以在 Warning Event Log 中存储的事件数。</td></tr>
<tr><td>34h</td><td>2</td><td>Failure Event Log Size: The number of events that the device can store in the Failure Event Log before the log overflows.</td><td>Failure Event Log Size:设备在日志溢出之前可以在 Failure Event Log 中存储的事件数。</td></tr>
<tr><td>36h</td><td>2</td><td>Fatal Event Log Size: The number of events that the device can store in the Fatal Event Log before the log overflows.</td><td>Fatal Event Log Size:设备在日志溢出之前可以在 Fatal Event Log 中存储的事件数。</td></tr>
<tr><td>38h</td><td>4</td><td>LSA Size: The size of the Label Storage Area. Expressed in bytes.</td><td>LSA Size:Label Storage Area 的大小。以字节为单位表示。</td></tr>
<tr><td>3Ch</td><td>3</td><td>Poison List Maximum Media Error Records: The maximum number of Media Error Records that the device can track in its Poison List.</td><td>Poison List Maximum Media Error Records:设备可以在其 Poison List 中跟踪的最大 Media Error Records 数。</td></tr>
<tr><td>3Fh</td><td>2</td><td>Inject Poison Limit: The device's supported maximum number of physical addresses that can be poisoned by the Inject Poison command. When 0, the device does not have a poison injection limit. When nonzero, the device has a maximum limit of poison that can be injected using the Inject Poison command.</td><td>Inject Poison Limit:设备支持的可由 Inject Poison 命令注入 poison 的最大物理地址数。当为 0 时,设备没有 poison 注入限制。当非零时,设备具有可使用 Inject Poison 命令注入的最大 poison 限制。</td></tr>
<tr><td>41h</td><td>1</td><td>Poison Handling Capabilities<br>• Bit[0]: Injects Persistent Poison: When set and the device supports poison injection, any poison injected in non-volatile DPA shall remain persistent across all types of device resets. When cleared and the device supports poison injection, Conventional or CXL Reset shall automatically clear the injected poison.<br>• Bit[1]: Scans for Poison: When set, the device shall periodically scan its media for errors and shall automatically alert the host of those errors. If cleared, the device does not periodically scan for memory errors and does not generate an alert.<br>• Bits[7:2]: Reserved.</td><td>Poison Handling Capabilities<br>• Bit[0]:Injects Persistent Poison:当设置且设备支持 poison 注入时,在非易失性 DPA 中注入的任何 poison 应在所有类型的设备复位后保持持久性。当清除且设备支持 poison 注入时,Conventional 或 CXL Reset 应自动清除注入的 poison。<br>• Bit[1]:Scans for Poison:当设置时,设备应定期扫描其介质以查找错误,并应自动将这些错误警报通知主机。如果清除,设备不定期扫描内存错误,也不生成警报。<br>• Bits[7:2]:保留。</td></tr>
<tr><td>42h</td><td>1</td><td>QoS Telemetry Capabilities<br>• Bit[0]: Egress Port Congestion Supported<br>• Bit[1]: Temporary Throughput Reduction Supported<br>• Bits[7:2]: Reserved</td><td>QoS Telemetry Capabilities<br>• Bit[0]:支持 Egress Port Congestion<br>• Bit[1]:支持 Temporary Throughput Reduction<br>• Bits[7:2]:保留</td></tr>
<tr><td>43h</td><td>2</td><td>Dynamic Capacity Event Log Size: The number of events that the device can store in the Dynamic Capacity Event Log before the log overflows.</td><td>Dynamic Capacity Event Log Size:设备在日志溢出之前可以在 Dynamic Capacity Event Log 中存储的事件数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Identify Memory Device Output Payload (page 722-723) ｜ Identify Memory Device 输出负载
>
> <img src="figures/chapter_08/page_0722.png" alt="Figure 8-X page 722" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0722.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-1"></a>
### 8.2.10.9.2.1 Get Partition Info (Opcode 4100h) | 获取分区信息 (操作码 4100h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get the Active and Next capacity settings for a memory device, describing the amount of volatile and persistent memory capacities available. The Active values describe the current capacities provided by the device in the currently active configuration. The Next values describe a new configuration that has not yet taken effect, to become active on the next reset (as specified in the Set Partition command effects). If the HDM_Count field in DVSEC CXL Capability is 01b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low (see Section 8.1.3.8.2) is 01b.</td><td style="background-color:#e8e8e8">获取内存设备的 Active 和 Next 容量设置,描述可用的易失性和持久性内存容量。Active 值描述设备在当前活动配置中提供的当前容量。Next 值描述尚未生效的新配置,将在下次复位时生效(如 Set Partition 命令效果中所指定)。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 01b,则仅当 DVSEC CXL Range 1 Size Low(参见 8.1.3.8.2 节)中的 Memory_Info_Valid 标志为 01b 时,输出负载才有效。</td></tr>
<tr><td>If the HDM_Count field in DVSEC CXL Capability is 10b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low as well as DVSEC CXL Range 2 Size Low (see Section 8.1.3.8.6) are both 1.</td><td style="background-color:#e8e8e8">如果 DVSEC CXL Capability 中的 HDM_Count 字段为 10b,则仅当 DVSEC CXL Range 1 Size Low 和 DVSEC CXL Range 2 Size Low(参见 8.1.3.8.6 节)中的 Memory_Info_Valid 标志均为 1 时,输出负载才有效。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-143. Get Partition Info Output Payload | Get Partition Info 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Active Volatile Capacity: Total device volatile memory capacity in multiples of 256 MB. This is the sum of the device's Volatile Only capacity and the capacity that is partitioned for volatile use. The device shall provide this volatile capacity starting at DPA 0.</td><td>Active Volatile Capacity:设备易失性内存总容量(以 256 MB 的倍数表示)。这是设备的 Volatile Only 容量和分区用于易失性使用的容量之和。设备应从 DPA 0 开始提供此易失性容量。</td></tr>
<tr><td>08h</td><td>8</td><td>Active Persistent Capacity: Total device persistent memory capacity in multiples of 256 MB. This is the sum of the device's Persistent Only capacity and the capacity that is partitioned for persistent use. The device shall provide this persistent capacity starting at the DPA immediately following the volatile capacity.</td><td>Active Persistent Capacity:设备持久性内存总容量(以 256 MB 的倍数表示)。这是设备的 Persistent Only 容量和分区用于持久性使用的容量之和。设备应从紧跟易失性容量之后的 DPA 开始提供此持久性容量。</td></tr>
<tr><td>10h</td><td>8</td><td>Next Volatile Capacity: If nonzero, this value shall become the Active Volatile Capacity on the next reset (as specified in the Set Partition command effects). If both this field and the Next Persistent Capacity field are 0, there is no pending change to the partitioning.</td><td>Next Volatile Capacity:如果非零,此值应在下次复位时成为 Active Volatile Capacity(如 Set Partition 命令效果中所指定)。如果此字段和 Next Persistent Capacity 字段均为 0,则没有待处理的分区更改。</td></tr>
<tr><td>18h</td><td>8</td><td>Next Persistent Capacity: If nonzero, this value shall become the Active Persistent Capacity on the next reset (as specified in the Set Partition command effects). If both this field and the Next Volatile Capacity field are 0, there is no pending change to the partitioning.</td><td>Next Persistent Capacity:如果非零,此值应在下次复位时成为 Active Persistent Capacity(如 Set Partition 命令效果中所指定)。如果此字段和 Next Volatile Capacity 字段均为 0,则没有待处理的分区更改。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Partition Info (page 724) ｜ Get Partition Info
>
> <img src="figures/chapter_08/page_0724.png" alt="Figure 8-X page 724" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0724.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-2"></a>
### 8.2.10.9.2.2 Set Partition Info (Opcode 4101h) | 设置分区信息 (操作码 4101h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Set the partitioning between volatile capacity and persistent capacity for the partitionable capacity. Partitionable capacity is equal to (Total Capacity - Volatile Only Capacity - Persistent Only Capacity). This command shall fail with an Unsupported error if there is no partitionable capacity (i.e., Identify Memory Device reports Partition Alignment as zero). The device shall return Invalid Input if the specified capacity is not aligned to the partition alignment requirement reported in the Identify Memory Device command. Using this command to change the size of the persistent capacity shall result in the loss of data stored.</td><td style="background-color:#e8e8e8">为可分区容量设置易失性容量和持久性容量之间的分区。可分区容量等于(Total Capacity - Volatile Only Capacity - Persistent Only Capacity)。如果没有可分区容量(即,Identify Memory Device 报告 Partition Alignment 为零),此命令应以 Unsupported 错误失败。如果指定的容量与 Identify Memory Device 命令中报告的分区对齐要求不一致,设备应返回 Invalid Input。使用此命令更改持久性容量的大小将导致存储的数据丢失。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to change the partitioning of the device with the Immediate flag set by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何设置 Immediate 标志的更改设备分区的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Configuration Change after Cold Reset<br>• CEL[11:10] Valid<br>• Configuration Change after Conventional Reset<br>• Configuration Change after CXL Reset<br>• Immediate Configuration Change<br>• Immediate Data Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Cold Reset 后的配置更改<br>• CEL[11:10] 有效<br>• Conventional Reset 后的配置更改<br>• CXL Reset 后的配置更改<br>• 立即配置更改<br>• 立即数据更改</td></tr>
</tbody>
</table>

**Table 8-144. Set Partition Info Input Payload | Set Partition Info 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Volatile Capacity: The amount of partitionable capacity that shall be allocated to volatile capacity, in multiples of 256 MB aligned to the partition alignment requirement reported in the Identify Memory Device command. The remainder of the partitionable capacity shall be allocated to persistent capacity.</td><td>Volatile Capacity:应分配给易失性容量的可分区容量大小(以 256 MB 的倍数表示),并与 Identify Memory Device 命令中报告的分区对齐要求对齐。可分区容量的其余部分应分配给持久性容量。</td></tr>
<tr><td>08h</td><td>1</td><td>Flags<br>• Bit[0]: Immediate: When set, the change is immediately requested. If cleared, the change in partitioning shall become the "next" configuration, to become active on the next reset (as specified in the command effects). In this case, the new configuration shall be reported in the Next Volatile Capacity and Next Persistent Capacity fields returned by the Get Partition Info command. It is the caller's responsibility to avoid immediate changes to the partitioning when the device is in use.<br>• Bits[7:1]: Reserved.</td><td>标志位<br>• Bit[0]:Immediate:当设置时,立即请求更改。如果清除,分区的更改将成为 "next" 配置,在下次复位时生效(如命令效果中所指定)。在这种情况下,新配置应在 Get Partition Info 命令返回的 Next Volatile Capacity 和 Next Persistent Capacity 字段中报告。调用者有责任在设备使用时避免对分区的立即更改。<br>• Bits[7:1]:保留。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Set Partition Info (page 725) ｜ Set Partition Info
>
> <img src="figures/chapter_08/page_0725.png" alt="Figure 8-X page 725" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0725.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-3"></a>
### 8.2.10.9.2.3 Get LSA (Opcode 4102h) | 获取 LSA (操作码 4102h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Label Storage Area (LSA) shall be supported by a memory device that provides persistent memory capacity and may be supported by a device that provides only volatile memory capacity. The format of the LSA is specified in Section 9.13.2. The size of the Label Storage Area is retrieved from the Identify Memory Device command.</td><td style="background-color:#e8e8e8">提供持久性内存容量的内存设备应支持 Label Storage Area (LSA),并且可以由仅提供易失性内存容量的设备支持。LSA 的格式在 9.13.2 节中指定。Label Storage Area 的大小是从 Identify Memory Device 命令检索的。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-145. Get LSA Input Payload | Get LSA 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Offset: The byte offset in the LSA to return in the output payload.</td><td>Offset:在 LSA 中返回到输出负载的字节偏移量。</td></tr>
<tr><td>04h</td><td>4</td><td>Length: Length in bytes of LSA to return in the output payload.</td><td>Length:输出负载中返回的 LSA 的字节长度。</td></tr>
</tbody>
</table>

**Table 8-146. Get LSA Output Payload | Get LSA 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>Varies</td><td>Data: Requested bytes from the LSA.</td><td>Data:来自 LSA 的请求字节。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-4"></a>
### 8.2.10.9.2.4 Set LSA (Opcode 4103h) | 设置 LSA (操作码 4103h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The format of the Label Storage Area is specified in Section 9.13.2.</td><td style="background-color:#e8e8e8">Label Storage Area 的格式在 9.13.2 节中指定。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Configuration Change<br>• Immediate Data Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• 立即配置更改<br>• 立即数据更改</td></tr>
</tbody>
</table>

**Table 8-147. Set LSA Input Payload | Set LSA 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Offset: The byte offset in the LSA.</td><td>Offset:LSA 中的字节偏移量。</td></tr>
<tr><td>04h</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Data: The data to be written to LSA at the specified offset.</td><td>Data:要在指定偏移量处写入 LSA 的数据。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get LSA / Set LSA (page 726) ｜ Get LSA / Set LSA
>
> <img src="figures/chapter_08/page_0726.png" alt="Figure 8-X page 726" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0726.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-1"></a>
### 8.2.10.9.3.1 Get Health Info (Opcode 4200h) | 获取健康信息 (操作码 4200h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get the current instantaneous health of the device. It is not necessary to poll for health changes. Anytime the health of the device changes, the device shall add an appropriate event to its internal event log, update the Event Status register, and if configured, interrupt the host.</td><td style="background-color:#e8e8e8">获取设备当前的瞬时健康状态。不需要轮询健康变化。每当设备的健康状态发生变化时,设备应将适当的事件添加到其内部事件日志,更新 Event Status 寄存器,并在配置时中断主机。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-148. Get Health Info Output Payload | Get Health Info 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Health Status: Overall device health summary. Normal health status is all bits cleared.<br>• Bit[0]: Maintenance Needed<br>• Bit[1]: Performance Degraded<br>• Bit[2]: Hardware Replacement Needed<br>• Bit[3]: Memory Capacity Degraded<br>• Bits[7:4]: Reserved</td><td>Health Status:设备整体健康摘要。正常的健康状态是所有位都清零。<br>• Bit[0]:Maintenance Needed(需要维护)<br>• Bit[1]:Performance Degraded(性能降级)<br>• Bit[2]:Hardware Replacement Needed(需要更换硬件)<br>• Bit[3]:Memory Capacity Degraded(内存容量降级)<br>• Bits[7:4]:保留</td></tr>
<tr><td>01h</td><td>1</td><td>Media Status: Overall media health summary.<br>• 00h = Normal. The device's media is operating normally.<br>• 01h = Not Ready. The device's media is not ready.<br>• 02h = Write persistency Lost. The device cannot persist write requests but is able to read stored data.<br>• 03h = All data lost. All data has been lost from the device.<br>• 04h = Write Persistency Loss in the Event of Power Loss<br>• 05h = Write Persistency Loss in Event of Shutdown<br>• 06h = Write Persistency Loss Imminent<br>• 07h = All Data Loss in the Event of Power Loss<br>• 08h = All Data Loss in the Event of Shutdown<br>• 09h = All Data Loss Imminent<br>• All other encodings are reserved.</td><td>Media Status:介质整体健康摘要。<br>• 00h = Normal。设备的介质正常运行。<br>• 01h = Not Ready。设备的介质未就绪。<br>• 02h = Write persistency Lost。设备无法持久化写入请求,但能够读取存储的数据。<br>• 03h = All data lost。设备上的所有数据都已丢失。<br>• 04h = 断电时写入持久性丢失<br>• 05h = 关闭时写入持久性丢失<br>• 06h = 即将丢失写入持久性<br>• 07h = 断电时所有数据丢失<br>• 08h = 关闭时所有数据丢失<br>• 09h = 即将丢失所有数据<br>• 所有其他编码保留。</td></tr>
<tr><td>02h</td><td>1</td><td>Additional Status<br>• Bits[1:0]: Life Used: 00b = Normal; 01b = Warning; 10b = Critical; 11b = Reserved.<br>• Bits[3:2]: Device Temperature: 00b = Normal; 01b = Warning; 10b = Critical; 11b = Reserved.<br>• Bit[4]: Corrected Volatile Error Count: 0 = Normal; 1 = Warning or Failure.<br>• Bit[5]: Corrected Persistent Error Count: 0 = Normal; 1 = Warning.<br>• Bits[7:6]: Reserved.</td><td>Additional Status<br>• Bits[1:0]:Life Used(已使用寿命):00b = 正常;01b = 警告;10b = 严重;11b = 保留。<br>• Bits[3:2]:Device Temperature(设备温度):00b = 正常;01b = 警告;10b = 严重;11b = 保留。<br>• Bit[4]:Corrected Volatile Error Count(已纠正易失性错误计数):0 = 正常;1 = 警告或故障。<br>• Bit[5]:Corrected Persistent Error Count(已纠正持久性错误计数):0 = 正常;1 = 警告。<br>• Bits[7:6]:保留。</td></tr>
<tr><td>03h</td><td>1</td><td>Life Used: The device's used life as a percentage value (0-100) of factory-expected life span. Returns FFh if not implemented.</td><td>Life Used(已使用寿命):设备的已使用寿命,占出厂预期寿命的百分比值(0-100)。如果未实现,则返回 FFh。</td></tr>
<tr><td>04h</td><td>2</td><td>Device Temperature: The device's current temperature in degrees Celsius, represented as a 2's complement value. Returns 7FFFh if not implemented.</td><td>Device Temperature(设备温度):设备的当前温度(以摄氏度为单位),表示为 2 的补码值。如果未实现,则返回 7FFFh。</td></tr>
<tr><td>06h</td><td>4</td><td>Dirty Shutdown Count: A monotonically increasing counter that is incremented whenever the device fails to save and/or flush data to the persistent media or is unable to determine whether data loss may have occurred. The count is persistent across power loss and wraps back to 0 at overflow.</td><td>Dirty Shutdown Count(脏关机计数):单调递增的计数器,每当设备无法将数据保存和/或刷新到持久性介质,或无法确定是否可能发生数据丢失时,计数器递增。计数在断电后保留,并在溢出时回绕到 0。</td></tr>
<tr><td>0Ah</td><td>4</td><td>Corrected Volatile Error Count: The total number of correctable memory errors that the device has detected as having occurred in the volatile memory partition.</td><td>Corrected Volatile Error Count(已纠正易失性错误计数):设备检测到的在易失性内存分区中发生的可纠正内存错误总数。</td></tr>
<tr><td>0Eh</td><td>4</td><td>Corrected Persistent Error Count: The total number of correctable memory errors that the device has detected as having occurred in the persistent memory partition.</td><td>Corrected Persistent Error Count(已纠正持久性错误计数):设备检测到的在持久性内存分区中发生的可纠正内存错误总数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Health Info Output Payload (page 727-728) ｜ Get Health Info 输出负载
>
> <img src="figures/chapter_08/page_0727.png" alt="Figure 8-X page 727" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0727.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-2"></a>
### 8.2.10.9.3.2 Get Alert Configuration (Opcode 4201h) | 获取警报配置 (操作码 4201h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve the device's critical alert and programmable warning configuration. Critical alerts shall automatically be configured by the device after a Conventional Reset. If supported, programmable warning thresholds shall be initialized to vendor-recommended defaults by the device on a Conventional Reset.</td><td style="background-color:#e8e8e8">检索设备的关键警报和可编程警告配置。关键警报应在 Conventional Reset 后由设备自动配置。如果支持,可编程警告阈值应在 Conventional Reset 时由设备初始化为厂商推荐的默认值。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-149. Get Alert Configuration Output Payload | Get Alert Configuration 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Valid Alerts: Indicators of which alert fields are valid in the returned data.<br>• Bit[0]: When set, the Life Used Programmable Warning Threshold field is valid<br>• Bit[1]: When set, the Device Over-Temperature Programmable Warning Threshold field is valid<br>• Bit[2]: When set, the Device Under-Temperature Programmable Warning Threshold field is valid<br>• Bit[3]: When set, the Corrected Volatile Memory Error Programmable Warning Threshold field is valid<br>• Bit[4]: When set, the Corrected Persistent Memory Error Programmable Warning Threshold field is valid<br>• Bits[7:5]: Reserved</td><td>Valid Alerts(有效警报):返回数据中哪些警报字段有效的指示符。<br>• Bit[0]:当设置时,Life Used Programmable Warning Threshold 字段有效<br>• Bit[1]:当设置时,Device Over-Temperature Programmable Warning Threshold 字段有效<br>• Bit[2]:当设置时,Device Under-Temperature Programmable Warning Threshold 字段有效<br>• Bit[3]:当设置时,Corrected Volatile Memory Error Programmable Warning Threshold 字段有效<br>• Bit[4]:当设置时,Corrected Persistent Memory Error Programmable Warning Threshold 字段有效<br>• Bits[7:5]:保留</td></tr>
<tr><td>01h</td><td>1</td><td>Programmable Alerts: Indicators of which device alerts are programmable by the host.<br>• Bit[0]: When set, the Life Used Programmable Warning Threshold is programmable by the host<br>• Bit[1]: When set, the Device Over-Temperature Programmable Warning Threshold field is programmable by the host<br>• Bit[2]: When set, the Device Under-Temperature Programmable Warning Threshold field is programmable by the host<br>• Bit[3]: When set, the Corrected Volatile Memory Error Programmable Warning is programmable by the host<br>• Bit[4]: When set, the Corrected Persistent Memory Error Programmable Warning is programmable by the host<br>• Bits[7:5]: Reserved</td><td>Programmable Alerts(可编程警报):主机可编程哪些设备警报的指示符。<br>• Bit[0]:当设置时,Life Used Programmable Warning Threshold 可由主机编程<br>• Bit[1]:当设置时,Device Over-Temperature Programmable Warning Threshold 字段可由主机编程<br>• Bit[2]:当设置时,Device Under-Temperature Programmable Warning Threshold 字段可由主机编程<br>• Bit[3]:当设置时,Corrected Volatile Memory Error Programmable Warning 可由主机编程<br>• Bit[4]:当设置时,Corrected Persistent Memory Error Programmable Warning 可由主机编程<br>• Bits[7:5]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>Life Used Critical Alert Threshold: The device's default alert when the Life Used rises above this percentage-based value. Valid values are 0-100.</td><td>Life Used Critical Alert Threshold(Life Used 关键警报阈值):当 Life Used 超过此基于百分比的值时,设备的默认警报。有效值为 0-100。</td></tr>
<tr><td>03h</td><td>1</td><td>Life Used Programmable Warning Threshold: The device's currently programmed warning threshold when the life used rises to or above this percentage-based value. Valid values are 0-100. The life used warning threshold shall be less than the life used critical alert value.</td><td>Life Used Programmable Warning Threshold(Life Used 可编程警告阈值):当已使用寿命达到或超过此基于百分比的值时,设备当前编程的警告阈值。有效值为 0-100。Life used 警告阈值应小于 Life used 关键警报值。</td></tr>
<tr><td>04h</td><td>2</td><td>Device Over-Temperature Critical Alert Threshold: The device's default critical over-temperature alert threshold when the device temperature rises to or above this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Over-Temperature Critical Alert Threshold(设备过温关键警报阈值):当设备温度达到或超过此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备的默认关键过温警报阈值。</td></tr>
<tr><td>06h</td><td>2</td><td>Device Under-Temperature Critical Alert Threshold: The device's default critical under-temperature alert threshold when the device temperature falls to or below this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Under-Temperature Critical Alert Threshold(设备低温关键警报阈值):当设备温度降至或低于此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备的默认关键低温警报阈值。</td></tr>
<tr><td>08h</td><td>2</td><td>Device Over-Temperature Programmable Warning Threshold: The device's currently programmed over-temperature warning threshold when the device temperature rises to or above this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Over-Temperature Programmable Warning Threshold(设备过温可编程警告阈值):当设备温度达到或超过此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备当前编程的过温警告阈值。</td></tr>
<tr><td>0Ah</td><td>2</td><td>Device Under-Temperature Programmable Warning Threshold: The device's currently programmed under-temperature warning threshold when the device temperature falls to or below this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Under-Temperature Programmable Warning Threshold(设备低温可编程警告阈值):当设备温度降至或低于此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备当前编程的低温警告阈值。</td></tr>
<tr><td>0Ch</td><td>2</td><td>Corrected Volatile Memory Error Programmable Warning Threshold: The device's currently programmed warning threshold for corrected volatile memory errors before signaling a corrected error event to the host.</td><td>Corrected Volatile Memory Error Programmable Warning Threshold(已纠正易失性内存错误可编程警告阈值):在向主机发出已纠正错误事件之前,设备当前编程的已纠正易失性内存错误警告阈值。</td></tr>
<tr><td>0Eh</td><td>2</td><td>Corrected Persistent Memory Error Programmable Warning Threshold: The device's currently programmed warning threshold for corrected persistent memory errors before signaling a corrected error event to the host.</td><td>Corrected Persistent Memory Error Programmable Warning Threshold(已纠正持久性内存错误可编程警告阈值):在向主机发出已纠正错误事件之前,设备当前编程的已纠正持久性内存错误警告阈值。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Alert Configuration (page 729-730) ｜ Get Alert Configuration
>
> <img src="figures/chapter_08/page_0729.png" alt="Figure 8-X page 729" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0729.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-3"></a>
### 8.2.10.9.3.3 Set Alert Configuration (Opcode 4202h) | 设置警报配置 (操作码 4202h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Set Alert Configuration allows the host to configure programmable warning thresholds optionally. If supported, programmable warning thresholds shall be initialized to vendor-recommended defaults by the device on a Conventional Reset. After completion of this command, the requested programmable warning thresholds shall replace any previously programmed warning thresholds.</td><td style="background-color:#e8e8e8">Set Alert Configuration 允许主机选择性地配置可编程警告阈值。如果支持,可编程警告阈值应在 Conventional Reset 时由设备初始化为厂商推荐的默认值。此命令完成后,请求的可编程警告阈值应替换任何先前编程的警告阈值。</td></tr>
<tr><td>Any time a programmed warning threshold is reached, the device shall add an appropriate event record to its event log, update the Event Status register, and if configured, interrupt the host. If the conditions are already met for the newly programmed warning at the time this command is executed, the device shall immediately generate the event record and interrupt for the alert.</td><td style="background-color:#e8e8e8">每当达到编程的警告阈值时,设备应将适当的事件记录添加到其事件日志,更新 Event Status 寄存器,并在配置时中断主机。如果在执行此命令时已满足新编程的警告条件,则设备应立即生成事件记录并中断警报。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Policy Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Policy Change(立即策略更改)</td></tr>
</tbody>
</table>

**Table 8-150. Set Alert Configuration Input Payload | Set Alert Configuration 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Valid Alert Actions: Indicators of which alert fields are valid in the supplied input payload.<br>• Bit[0]: When set, the Life Used Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[1]: When set, the Device Over-Temperature Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[2]: When set, the Device Under-Temperature Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[3]: When set, the Corrected Volatile Memory Error Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[4]: When set, the Corrected Persistent Memory Error Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bits[7:5]: Reserved</td><td>Valid Alert Actions(有效警报操作):提供的输入负载中哪些警报字段有效的指示符。<br>• Bit[0]:当设置时,Life Used Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[1]:当设置时,Device Over-Temperature Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[2]:当设置时,Device Under-Temperature Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[3]:当设置时,Corrected Volatile Memory Error Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[4]:当设置时,Corrected Persistent Memory Error Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bits[7:5]:保留</td></tr>
<tr><td>01h</td><td>1</td><td>Enable Alert Actions: The device shall enable the following programmable alerts.<br>• Bit[0]: When set, the device shall enable its Life Used Programmable Warning Threshold.<br>• Bit[1]: When set, the device shall enable its Device Over-Temperature Programmable Warning Threshold.<br>• Bit[2]: When set, the device shall enable its Device Under-Temperature Programmable Warning Threshold.<br>• Bit[3]: When set, the device shall enable its Corrected Volatile Memory Error Programmable Warning Threshold.<br>• Bit[4]: When set, the device shall enable its Corrected Persistent Memory Error Programmable Warning Threshold.<br>• Bits[7:5]: Reserved.</td><td>Enable Alert Actions(启用警报操作):设备应启用以下可编程警报。<br>• Bit[0]:当设置时,设备应启用其 Life Used Programmable Warning Threshold。<br>• Bit[1]:当设置时,设备应启用其 Device Over-Temperature Programmable Warning Threshold。<br>• Bit[2]:当设置时,设备应启用其 Device Under-Temperature Programmable Warning Threshold。<br>• Bit[3]:当设置时,设备应启用其 Corrected Volatile Memory Error Programmable Warning Threshold。<br>• Bit[4]:当设置时,设备应启用其 Corrected Persistent Memory Error Programmable Warning Threshold。<br>• Bits[7:5]:保留。</td></tr>
<tr><td>02h</td><td>1</td><td>Life Used Programmable Warning Threshold: The device's updated life used programmable warning threshold.</td><td>Life Used Programmable Warning Threshold:设备更新的 Life Used 可编程警告阈值。</td></tr>
<tr><td>03h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>04h</td><td>2</td><td>Device Over-Temperature Programmable Warning Threshold: The device's updated Over-Temperature programmable warning threshold.</td><td>Device Over-Temperature Programmable Warning Threshold:设备更新的过温可编程警告阈值。</td></tr>
<tr><td>06h</td><td>2</td><td>Device Under-Temperature Programmable Warning Threshold: The device's updated Under-Temperature programmable warning threshold.</td><td>Device Under-Temperature Programmable Warning Threshold:设备更新的低温可编程警告阈值。</td></tr>
<tr><td>08h</td><td>2</td><td>Corrected Volatile Memory Error Programmable Warning Threshold: The device's updated programmable warning threshold for corrected volatile memory errors.</td><td>Corrected Volatile Memory Error Programmable Warning Threshold:设备更新的已纠正易失性内存错误可编程警告阈值。</td></tr>
<tr><td>0Ah</td><td>2</td><td>Corrected Persistent Memory Error Programmable Warning Threshold: The device's updated programmable warning threshold for corrected persistent memory errors.</td><td>Corrected Persistent Memory Error Programmable Warning Threshold:设备更新的已纠正持久性内存错误可编程警告阈值。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Set Alert Configuration (page 731) ｜ Set Alert Configuration
>
> <img src="figures/chapter_08/page_0731.png" alt="Figure 8-X page 731" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0731.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-4"></a>
### 8.2.10.9.3.4 Get Shutdown State (Opcode 4203h) | 获取关闭状态 (操作码 4203h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-151. Get Shutdown State Output Payload | Get Shutdown State 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>State: The current Shutdown State.<br>• Bit[0]: Dirty: A 1 value indicates the device's internal Shutdown State is "dirty". A 0 value indicates "clean".<br>• Bits[7:1]: Reserved.</td><td>State:当前 Shutdown State。<br>• Bit[0]:Dirty(脏):值 1 表示设备的内部 Shutdown State 为 "dirty"。值 0 表示 "clean"。<br>• Bits[7:1]:保留。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-5"></a>
### 8.2.10.9.3.5 Set Shutdown State (Opcode 4204h) | 设置关闭状态 (操作码 4204h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Policy Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Policy Change(立即策略更改)</td></tr>
</tbody>
</table>

**Table 8-152. Set Shutdown State Input Payload | Set Shutdown State 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>State: The current Shutdown State.<br>• Bit[0]: Dirty: A 1 value sets the device's internal Shutdown State to "dirty". A 0 value sets it to "clean". The device shall persistently store this state and use it after the next Conventional Reset to determine whether the Dirty Shutdown Count described in Section 8.2.10.9.3.1 gets updated. If the Shutdown State is "dirty", the device shall increment the Dirty Shutdown Count and then set the Shutdown State to "clean". This post-reset logic shall occur before the device accepts any commands or memory I/O. The value set by this mailbox command shall be overridden by the device in two cases:<br>  — On a successful GPF flow, the device shall set the Shutdown State to "clean"<br>  — When handling a shutdown/reset, if the device detects an internal failure that jeopardizes data integrity (e.g., a failed internal flush), the device shall set the Shutdown State to "dirty"<br>• Bits[7:1]: Reserved</td><td>State:当前 Shutdown State。<br>• Bit[0]:Dirty(脏):值 1 将设备的内部 Shutdown State 设置为 "dirty"。值 0 将其设置为 "clean"。设备应持续存储此状态,并在下一次 Conventional Reset 后使用它来确定是否更新 8.2.10.9.3.1 节中描述的 Dirty Shutdown Count。如果 Shutdown State 为 "dirty",设备应增加 Dirty Shutdown Count,然后将 Shutdown State 设置为 "clean"。此复位后逻辑应在设备接受任何命令或内存 I/O 之前发生。此邮箱命令设置的值将在两种情况下被设备覆盖:<br>  — 在成功的 GPF 流程中,设备应将 Shutdown State 设置为 "clean"<br>  — 在处理关闭/复位时,如果设备检测到危及数据完整性的内部故障(例如,内部刷新失败),设备应将 Shutdown State 设置为 "dirty"<br>• Bits[7:1]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get/Set Shutdown State (page 732) ｜ Get/Set Shutdown State
>
> <img src="figures/chapter_08/page_0732.png" alt="Figure 8-X page 732" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0732.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-1"></a>
### 8.2.10.9.4.1 Get Poison List (Opcode 4300h) | 获取 Poison List (操作码 4300h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get Poison List command shall return an unordered list of locations that are poisoned or result in poison if the addresses were accessed by the host. This command is not a background operation and the device shall return data without delay. The device may reject this command if the requested range spans the device's volatile and persistent partitions.</td><td style="background-color:#e8e8e8">Get Poison List 命令应返回主机访问时已 poison 或导致 poison 的位置的无序列表。此命令不是后台操作,设备应无延迟地返回数据。如果请求的范围跨越设备的易失性和持久性分区,设备可以拒绝此命令。</td></tr>
<tr><td>The device shall return the known list of locations with media errors for the requested address range when the device processes the command. Any time that the device detects a new poisoned location, the device shall add the DPA to the Poison List, add an appropriate event to its Warning, Informational, or Failure Event Log, update the Event Status register, and if configured, interrupt the host. In response, the host should reissue this command to retrieve the updated Poison List.</td><td style="background-color:#e8e8e8">设备应在处理命令时返回所请求地址范围内具有介质错误的已知位置列表。每当设备检测到新的 poison 位置时,设备应将 DPA 添加到 Poison List,将适当的事件添加到其 Warning、Informational 或 Failure Event Log,更新 Event Status 寄存器,并在配置时中断主机。作为响应,主机应重新发出此命令以检索更新的 Poison List。</td></tr>
<tr><td>When poison is written:<br>• Using CXL.mem: The device shall add the new DPA to the device's Poison List and then shall set the error source to an external error.<br>• Using a CXL-defined poison injection interface (e.g., Inject Poison command): The device shall add the new DPA to the device's Poison List and then shall set the error source to an injected error.<br>• By the device because of a device-detected internal error (e.g., device media scrub discovers new media error): The device shall add the new DPA to the device's Poison List and then shall set the error source to an internal error.</td><td style="background-color:#e8e8e8">当写入 poison 时:<br>• 使用 CXL.mem:设备应将新的 DPA 添加到设备的 Poison List,然后将错误源设置为外部错误。<br>• 使用 CXL 定义的 poison 注入接口(例如,Inject Poison 命令):设备应将新的 DPA 添加到设备的 Poison List,然后将错误源设置为注入错误。<br>• 由设备由于设备检测到的内部错误(例如,设备介质扫描发现新的介质错误):设备应将新的 DPA 添加到设备的 Poison List,然后将错误源设置为内部错误。</td></tr>
<tr><td>When poison is cleared, the DPA shall no longer be reported in the device's Poison List.</td><td style="background-color:#e8e8e8">当 poison 被清除时,DPA 将不再在设备的 Poison List 中报告。</td></tr>
<tr><td>If the device does not support poison list for volatile ranges and any location in the requested list maps to volatile, the device shall return Invalid Physical Address.</td><td style="background-color:#e8e8e8">如果设备不支持易失性范围的 poison 列表,并且请求列表中的任何位置映射到易失性,则设备应返回 Invalid Physical Address。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-153. Get Poison List Input Payload | Get Poison List 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Poison List Flags: Flags that affect the returned list.<br>• Bit[0]: Restart Request: If set to 1, the device shall send the Poison List starting from the first entry, even if a previous transfer was incomplete. A device supporting this flag shall set the Restart Ack bit in the output payload in response to this flag being set. A device that does not support this flag must not set the Restart Ack bit.<br>• Bits[5:1]: Reserved.<br>Get Poison List Physical Address: The starting DPA for which to retrieve the Poison List.<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Poison List Flags:影响返回列表的标志。<br>• Bit[0]:Restart Request(重启请求):如果设置为 1,设备应从第一个条目开始发送 Poison List,即使先前的传输未完成。支持此标志的设备应在响应此标志被设置时在输出负载中设置 Restart Ack 位。不支持此标志的设备不得设置 Restart Ack 位。<br>• Bits[5:1]:保留。<br>Get Poison List Physical Address:要检索 Poison List 的起始 DPA。<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>8</td><td>Get Poison List Physical Address Length: The range of physical addresses for which to retrieve the Poison List. This length shall be in units of 64 bytes (e.g., if this field is 2h, that indicates the length is 128 bytes).</td><td>Get Poison List Physical Address Length:要检索 Poison List 的物理地址范围。此长度应以 64 字节为单位(例如,如果此字段为 2h,则表示长度为 128 字节)。</td></tr>
</tbody>
</table>

**Table 8-154. Get Poison List Output Payload | Get Poison List 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Poison List Flags: Flags that describe the returned list.<br>• Bit[0]: More Media Error Records: When set, the device has more Media Error Records to return for the given Get Poison List address range.<br>• Bit[1]: Poison List Overflow: When set, the returned list has overflowed, and the returned list can no longer be considered a complete list.<br>• Bit[2]: Scan Media in Progress: When set, a background operation to scan the media is executing.<br>• Bit[3]: Restart Ack: Set by a device that supports the Restart Request flag in response to that flag being set in the Input Payload.<br>• Bits[7:4]: Reserved.</td><td>Poison List Flags:描述返回列表的标志。<br>• Bit[0]:More Media Error Records(更多介质错误记录):当设置时,设备有更多 Media Error Records 要针对给定的 Get Poison List 地址范围返回。<br>• Bit[1]:Poison List Overflow(Poison List 溢出):当设置时,返回的列表已溢出,返回的列表不再被视为完整列表。<br>• Bit[2]:Scan Media in Progress(扫描介质进行中):当设置时,扫描介质的后台操作正在执行。<br>• Bit[3]:Restart Ack(重启确认):由支持 Restart Request 标志的设备在响应输入负载中设置该标志时设置。<br>• Bits[7:4]:保留。</td></tr>
<tr><td>01h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>02h</td><td>8</td><td>Overflow Timestamp: The time at which the device determined the poison list overflowed. The number of unsigned nanoseconds that have elapsed since midnight, 01-Jan-1970, UTC.</td><td>Overflow Timestamp(溢出时间戳):设备确定 poison list 溢出的时间。自 1970 年 1 月 1 日午夜 UTC 以来经过的无符号纳秒数。</td></tr>
<tr><td>0Ah</td><td>2</td><td>Media Error Record Count: Number of records in the Media Error Records list.</td><td>Media Error Record Count:Media Error Records 列表中的记录数。</td></tr>
<tr><td>0Ch</td><td>14h</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>Varies</td><td>Media Error Records: The list of media error records.</td><td>Media Error Records:介质错误记录列表。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Poison List (page 733-734) ｜ Get Poison List
>
> <img src="figures/chapter_08/page_0733.png" alt="Figure 8-X page 733" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0733.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-2"></a>
### 8.2.10.9.4.2 Inject Poison (Opcode 4301h) | 注入 Poison (操作码 4301h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An optional command to inject poison into a requested physical address. If the host injects poison using this command, the device shall return poison when the address is accessed through the CXL.mem bus.</td><td style="background-color:#e8e8e8">用于将 poison 注入到请求的物理地址的可选命令。如果主机使用此命令注入 poison,则当通过 CXL.mem 总线访问该地址时,设备应返回 poison。</td></tr>
<tr><td>Injecting poison shall add the new physical address to the device's poison list and the error source shall be set to an injected error. In addition, the device shall add an appropriate poison creation event to its internal Informational Event Log, update the Event Status register, and if configured, interrupt the host.</td><td style="background-color:#e8e8e8">注入 poison 应将新的物理地址添加到设备的 poison 列表,并且错误源应设置为注入错误。此外,设备应将适当的 poison 创建事件添加到其内部 Informational Event Log,更新 Event Status 寄存器,并在配置时中断主机。</td></tr>
<tr><td>It is not an error to inject poison into a DPA that already has poison present and no error is returned.</td><td style="background-color:#e8e8e8">向已存在 poison 的 DPA 注入 poison 不是错误,不返回错误。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to change the data on the device or inject poison by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何更改设备上的数据或注入 poison 的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Invalid Physical Address<br>• Inject Poison Limit Reached<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Invalid Physical Address(无效物理地址)<br>• Inject Poison Limit Reached(达到注入 Poison 限制)<br>• Invalid Security State(无效安全状态)</td></tr>
</tbody>
</table>

**Table 8-155. Media Error Record | Media Error Record**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Media Error Address: The DPA of the memory error and error source.<br>• Bits[2:0]: Error Source: 000b = Unknown; 001b = External. Poison received from a source external to the device; 010b = Internal. The device generated poison from an internal source; 011b = Injected. The error was injected into the device for testing purposes; 111b = Vendor Specific. All other encodings are reserved.<br>• Bits[5:3]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Media Error Address:内存错误和错误源的 DPA。<br>• Bits[2:0]:Error Source(错误源):000b = Unknown(未知);001b = External(外部)。从设备外部的源接收的 poison;010b = Internal(内部)。设备从内部源生成 poison;011b = Injected(注入)。错误被注入到设备中以进行测试;111b = Vendor Specific(厂商特定)。所有其他编码保留。<br>• Bits[5:3]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>4</td><td>Media Error Length: The number of adjacent DPAs in this media error record. This shall be nonzero. Devices may coalesce adjacent memory errors into a single entry. This length shall be in units of 64 bytes.</td><td>Media Error Length:此介质错误记录中相邻 DPA 的数量。这应是非零的。设备可以将相邻的内存错误合并为单个条目。此长度应以 64 字节为单位。</td></tr>
<tr><td>0Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Error Record (page 735) ｜ Media Error Record
>
> <img src="figures/chapter_08/page_0735.png" alt="Figure 8-X page 735" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0735.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-3"></a>
### 8.2.10.9.4.3 Clear Poison (Opcode 4302h) | 清除 Poison (操作码 4302h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An optional command to clear poison from the requested physical address and atomically write the included data in its place. This provides the same functionality as the host directly writing new data to the device.</td><td style="background-color:#e8e8e8">用于从请求的物理地址清除 poison 并以原子方式将包含的数据写入其位置的可选命令。这提供了与主机直接将新数据写入设备相同的功能。</td></tr>
<tr><td>Clearing poison shall remove the physical address from the device's Poison List. It is not an error to clear poison from an address that does not have poison set. If the device detects that it is not possible to clear poison from the physical address, the device shall return a permanent media failure code for this command.</td><td style="background-color:#e8e8e8">清除 poison 应将物理地址从设备的 Poison List 中删除。从未设置 poison 的地址清除 poison 不是错误。如果设备检测到无法从物理地址清除 poison,则设备应为此命令返回永久性介质失败代码。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to change the data on the device or clear poison by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何更改设备上的数据或清除 poison 的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td>This command must not modify the content of the Extended Metadata field associated with this address. If the device is configured with non-zero Metadata bits as defined by HDM-H Metabits Storage Configuration field in Table 8-115, for subsequent read to the DPA, the device shall return Metafield=00b (Meta0-State abbreviation MS0) and MetaValue=00b.</td><td style="background-color:#e8e8e8">此命令不得修改与此地址关联的 Extended Metadata 字段的内容。如果设备配置了表 8-115 中 HDM-H Metabits Storage Configuration 字段所定义的非零 Metadata 位,则对于对 DPA 的后续读取,设备应返回 Metafield=00b(Meta0-State 缩写 MS0)和 MetaValue=00b。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Permanent Media Failure<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Permanent Media Failure(永久性介质故障)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Data Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Data Change(立即数据更改)</td></tr>
</tbody>
</table>

**Table 8-156. Inject Poison Input Payload | Inject Poison 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Inject Poison Physical Address: The requested DPA at which poison shall be injected by the device.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Inject Poison Physical Address:设备应在该处注入 poison 的请求 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
</tbody>
</table>

**Table 8-157. Clear Poison Input Payload | Clear Poison 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Clear Poison Physical Address: The requested DPA from which poison shall be cleared by the device.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Clear Poison Physical Address:设备应从该处清除 poison 的请求 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>64</td><td>Clear Poison Write Data: The data the device shall always write into the requested physical address, atomically, while clearing poison if the location is marked as being poisoned.</td><td>Clear Poison Write Data:设备应在清除 poison(如果该位置被标记为已 poison)时以原子方式始终写入到请求的物理地址的数据。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-4"></a>
### 8.2.10.9.4.4 Get Scan Media Capabilities (Opcode 4303h) | 获取扫描介质能力 (操作码 4303h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command allows the device to report capabilities and options for the Scan Media feature based on the requested range. The device may reject this command if the range requested spans the device's volatile and persistent partitions.</td><td style="background-color:#e8e8e8">此命令允许设备根据请求的范围报告 Scan Media 特性的能力和选项。如果请求的范围跨越设备的易失性和持久性分区,设备可以拒绝此命令。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-158. Get Scan Media Capabilities Input Payload | Get Scan Media Capabilities 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Get Scan Media Capabilities Start Physical Address: The starting DPA from which to retrieve Scan Media capabilities.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Get Scan Media Capabilities Start Physical Address:要检索 Scan Media 能力的起始 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>8</td><td>Get Scan Media Capabilities Physical Address Length: The range of physical addresses for which to retrieve Scan Media capabilities. This length shall be in units of 64 bytes.</td><td>Get Scan Media Capabilities Physical Address Length:要检索 Scan Media 能力的物理地址范围。此长度应以 64 字节为单位。</td></tr>
</tbody>
</table>

**Table 8-159. Get Scan Media Capabilities Output Payload | Get Scan Media Capabilities 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Estimated Scan Media Time: The number of milliseconds that the device estimates are required to complete the Scan Media request over the range specified in the input.</td><td>Estimated Scan Media Time:设备估计完成输入中指定范围的 Scan Media 请求所需的毫秒数。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-5"></a>
### 8.2.10.9.4.5 Scan Media (Opcode 4304h) | 扫描介质 (操作码 4304h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Scan Media command causes the device to initiate a scan of a portion of its media for locations that are poisoned or result in poison if the addresses were accessed by the host. The device may update its Poison List as a result of executing the scan and shall complete any changes to the Poison List before signally completion of the Scan Media background operation. If the device updates its Poison List while the Scan Media background operation is executing, the device shall indicate that a media scan is in progress if Get Poison List is called during the scan. The host should use this command only if the poison list has overflowed and is no longer a complete list of the memory errors that exist on the media. The device may reject this command if the requested range spans the device's volatile and persistent partitions.</td><td style="background-color:#e8e8e8">Scan Media 命令导致设备启动对其部分介质的扫描,以查找主机访问时已 poison 或导致 poison 的位置。设备可能会由于执行扫描而更新其 Poison List,并应在发出 Scan Media 后台操作完成信号之前完成对 Poison List 的任何更改。如果设备在 Scan Media 后台操作执行时更新其 Poison List,则如果在扫描期间调用 Get Poison List,设备应指示介质扫描正在进行。主机仅在 poison list 已溢出且不再是介质上存在的内存错误的完整列表时才应使用此命令。如果请求的范围跨越设备的易失性和持久性分区,设备可以拒绝此命令。</td></tr>
<tr><td>If interrupts are enabled for reporting internally or externally generated poison, and the poison list has not overflowed, the host should avoid using this command. It is expensive and may impact the performance of other operations on the device. This is intended only as a backup to retrieve the list of memory error locations in the event the poison list has overflowed.</td><td style="background-color:#e8e8e8">如果已启用用于报告内部或外部生成的 poison 的中断,并且 poison list 尚未溢出,则主机应避免使用此命令。它是昂贵的,并且可能会影响设备上其他操作的性能。这仅用作在 poison list 溢出时检索内存错误位置列表的备份。</td></tr>
<tr><td>Because the execution of a media scan may take significant time to complete, it is considered a background operation. The Scan Media command shall initiate the background operation and provide immediate status on the device's ability to start the scan operation. Any previous Scan Media results are discarded by the device upon receiving a new Scan Media command. Once the Scan Media command is successfully started, the Background Command Status register is used to retrieve the status. The Get Scan Media Results command shall return the list of poisoned memory locations.</td><td style="background-color:#e8e8e8">由于介质扫描的执行可能需要大量时间才能完成,因此它被视为后台操作。Scan Media 命令应启动后台操作,并立即提供有关设备启动扫描操作的能力的状态。设备在收到新的 Scan Media 命令时会丢弃任何先前的 Scan Media 结果。一旦 Scan Media 命令成功启动,Background Command Status 寄存器用于检索状态。Get Scan Media Results 命令应返回已 poison 的内存位置列表。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Background Command Started<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Aborted<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Background Command Started(后台命令已启动)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Aborted(中止)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Background Operation<br>• Request Abort Background Operation Command Supported</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Background Operation(后台操作)<br>• 支持 Request Abort Background Operation Command</td></tr>
</tbody>
</table>

**Table 8-160. Scan Media Input Payload | Scan Media 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Scan Media Physical Address: The starting DPA from which to start the scan.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Scan Media Physical Address:开始扫描的起始 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>8</td><td>Scan Media Physical Address Length: The range of physical addresses to scan. This length shall be in units of 64 bytes.</td><td>Scan Media Physical Address Length:要扫描的物理地址范围。此长度应以 64 字节为单位。</td></tr>
<tr><td>10h</td><td>1</td><td>Scan Media Flags<br>• Bit[0]: No Event Log: When set, the device shall not generate event logs for media errors found during the Scan Media operation.<br>• Bits[7:1]: Reserved.</td><td>Scan Media Flags<br>• Bit[0]:No Event Log(无事件日志):当设置时,设备不应为 Scan Media 操作期间发现的介质错误生成事件日志。<br>• Bits[7:1]:保留。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-6"></a>
### 8.2.10.9.4.6 Get Scan Media Results (Opcode 4305h) | 获取扫描介质结果 (操作码 4305h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get Scan Media Results returns an unordered list of poisoned memory locations, in response to the Scan Media command. If the Scan Media command has not been called since the last Conventional Reset, the device shall return the Unsupported return code. The completion status for the Scan Media command is returned in the Background Command Status register and is not repeated here.</td><td style="background-color:#e8e8e8">Get Scan Media Results 返回已 poison 内存位置的无序列表,作为对 Scan Media 命令的响应。如果自上次 Conventional Reset 以来未调用 Scan Media 命令,则设备应返回 Unsupported 返回码。Scan Media 命令的完成状态在 Background Command Status 寄存器中返回,此处不再重复。</td></tr>
<tr><td>Because the returned list can be larger than the output payload size, it is possible to return the list in multiple calls to Get Scan Media Results. The More Media Error Records indicator shall be set by the device anytime there are more records to retrieve. The caller should continue to issue this command until this indicator is no longer set.</td><td style="background-color:#e8e8e8">由于返回的列表可能大于输出负载大小,因此可以通过多次调用 Get Scan Media Results 返回列表。每当有更多记录要检索时,设备应设置 More Media Error Records 指示符。调用者应继续发出此命令,直到此指示符不再设置。</td></tr>
<tr><td>If the device cannot complete the scan and requires the host to retrieve scan media results before the device can continue the scan, the device shall set the Scan Media Stopped Prematurely indicator, return a valid Scan Media Restart Physical Address and Scan Media Restart Physical Address Length. This is the physical address range the device would require the Scan Media command to be called again with to continue the scan. It is the responsibility of the host to issue the Scan Media command, using this restart context, to guarantee that the Device's entire physical address range is eventually scanned.</td><td style="background-color:#e8e8e8">如果设备无法完成扫描并且需要主机在设备能够继续扫描之前检索扫描介质结果,则设备应设置 Scan Media Stopped Prematurely 指示符,返回有效的 Scan Media Restart Physical Address 和 Scan Media Restart Physical Address Length。这是设备需要再次调用 Scan Media 命令才能继续扫描的物理地址范围。主机有责任使用此重启上下文发出 Scan Media 命令,以保证设备的整个物理地址范围最终被扫描。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-161. Get Scan Media Results Output Payload | Get Scan Media Results 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Scan Media Restart Physical Address: The location from which the host should restart the Scan Media operation if the device could not complete the requested scan.</td><td>Scan Media Restart Physical Address:如果设备无法完成请求的扫描,主机应从该位置重新启动 Scan Media 操作。</td></tr>
<tr><td>08h</td><td>8</td><td>Scan Media Restart Physical Address Length: The remaining range from which the host should restart the Scan Media operation if the device could not complete the requested scan.</td><td>Scan Media Restart Physical Address Length:如果设备无法完成请求的扫描,主机应从该剩余范围重新启动 Scan Media 操作。</td></tr>
<tr><td>10h</td><td>1</td><td>Scan Media Flags<br>• Bit[0]: More Media Error Records: When set, the device has more Media Error Records to return for the given Scan Media address range.<br>• Bit[1]: Scan Stopped Prematurely: The device has run out of internal storage space for the error list.<br>• Bits[7:2]: Reserved.</td><td>Scan Media Flags<br>• Bit[0]:More Media Error Records(更多介质错误记录):当设置时,设备有更多 Media Error Records 要针对给定的 Scan Media 地址范围返回。<br>• Bit[1]:Scan Stopped Prematurely(扫描过早停止):设备的错误列表内部存储空间已用完。<br>• Bits[7:2]:保留。</td></tr>
<tr><td>11h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>12h</td><td>2</td><td>Media Error Record Count: The number of records in the Media Error Records list.</td><td>Media Error Record Count:Media Error Records 列表中的记录数。</td></tr>
<tr><td>14h</td><td>0Ch</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>Varies</td><td>Media Error Records: The list of media error records.</td><td>Media Error Records:介质错误记录列表。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-1"></a>
### 8.2.10.5.2.1 Command Effects Log (CEL) | 命令效果日志 (CEL)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Command Effects Log (CEL) is a variable-length log page that reports each CXL defined command supported by the CCI that was queried (with the exception of the secondary mailbox, as described in Section 8.2.9.4.2) and the effect each command may have on the device subsystem. The effects of a given command may be different based on various factors (e.g., the input payload specified when the command was issued). Therefore, all possible command effects for a given command shall be reported by the device in the CEL.</td><td style="background-color:#e8e8e8">命令效果日志 (CEL) 是一个可变长度的日志页,用于报告所查询 CCI 支持的每个 CXL 定义命令(secondary mailbox 除外,详见 8.2.9.4.2 节)以及每个命令可能对设备子系统产生的影响。给定命令的效果可能因各种因素而异(例如,发出命令时指定的输入负载)。因此,设备应在 CEL 中报告给定命令的所有可能命令效果。</td></tr>
<tr><td>Devices shall implement the CEL for all commands supported by the device, including any vendor specific commands that extend beyond those specified in this specification.</td><td style="background-color:#e8e8e8">设备应为其支持的所有命令实现 CEL,包括超出本规范规定的任何厂商特定命令。</td></tr>
<tr><td>Some host drivers may not allow unspecified commands to be passed through to the device if the commands are not advertised in the CEL.</td><td style="background-color:#e8e8e8">某些主机驱动程序可能不允许将未在 CEL 中通告的未指定命令传递到设备。</td></tr>
<tr><td>The CEL shall use a Log Identifier of:<br>• 0da9c0b5-bf41-4b78-8f79-96b1623b3f17</td><td style="background-color:#e8e8e8">CEL 应使用以下 Log Identifier:<br>• 0da9c0b5-bf41-4b78-8f79-96b1623b3f17</td></tr>
<tr><td>Each CEL entry shall have a specific set of bit definitions describing the effect of issuing the command as outlined below.</td><td style="background-color:#e8e8e8">每个 CEL 条目应具有一组特定的位定义,用于描述发出命令的影响,如下所述。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Log / CEL structures (page 677) ｜ Get Log / CEL 结构
>
> <img src="figures/chapter_08/page_0677.png" alt="Figure 8-X page 677" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0677.png)

**Table 8-84. Get Log Input Payload | Get Log 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log for which to retrieve data. See Table 8-83 for the list of Log Identifier UUIDs defined in this specification.</td><td>日志标识符(UUID):表示要检索数据的日志的 UUID。有关本规范中定义的 Log Identifier UUID 列表,请参见表 8-83。</td></tr>
<tr><td>10h</td><td>4</td><td>Offset: The byte offset in the log data to return in the output payload.</td><td>Offset:在日志数据中返回到输出负载的字节偏移量。</td></tr>
<tr><td>14h</td><td>4</td><td>Length: Length in bytes of log data to return in the output payload.</td><td>Length:在输出负载中返回的日志数据的字节长度。</td></tr>
</tbody>
</table>

**Table 8-85. Get Log Output Payload | Get Log 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>Varies</td><td>Log Data</td><td>日志数据</td></tr>
</tbody>
</table>

**Table 8-86. CEL Output Payload | CEL 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Command 1 CEL Entry: Contains the Command Effects Log Entry for 1st supported command.</td><td>命令 1 的 CEL 条目:包含第一个受支持命令的命令效果日志条目。</td></tr>
<tr><td>04h</td><td>4</td><td>Command 2 CEL Entry: Contains the Command Effects Log Entry for 2nd supported command.</td><td>命令 2 的 CEL 条目:包含第二个受支持命令的命令效果日志条目。</td></tr>
<tr><td>(4*(n-1))h</td><td>4</td><td>Command n CEL Entry: Contains the Command Effects Log Entry for nth supported command.</td><td>命令 n 的 CEL 条目:包含第 n 个受支持命令的命令效果日志条目。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-2"></a>
### 8.2.10.5.2.2 Vendor Debug Log | 厂商调试日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>All devices that support a debug log shall support the Vendor Debug Log to allow the log to be accessed through a common host driver, for any device, with Log Identifier of:<br>• 5e1819d9-11a9-400c-811f-d60719403d86</td><td style="background-color:#e8e8e8">所有支持调试日志的设备应支持 Vendor Debug Log,以便通过通用主机驱动程序访问任何设备的日志,其 Log Identifier 为:<br>• 5e1819d9-11a9-400c-811f-d60719403d86</td></tr>
<tr><td>The contents of the output payload are vendor specific.</td><td style="background-color:#e8e8e8">输出负载的内容由厂商特定定义。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Vendor Debug Log (page 678) ｜ 厂商调试日志
>
> <img src="figures/chapter_08/page_0678.png" alt="Figure 8-X page 678" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0678.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-3"></a>
### 8.2.10.5.2.3 Component State Dump Log | 组件状态转储日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Log Identifier: b3fab4cf-01b6-4332-943e-5e9962f23567</td><td style="background-color:#e8e8e8">日志标识符:b3fab4cf-01b6-4332-943e-5e9962f23567</td></tr>
<tr><td>The Component State Dump Log is an optional method for allowing vendor specific state information to be extracted using standard drivers.</td><td style="background-color:#e8e8e8">Component State Dump Log 是一种可选方法,允许使用标准驱动程序提取厂商特定的状态信息。</td></tr>
</tbody>
</table>

**Table 8-87. CEL Entry Structure | CEL 条目结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Opcode: The command opcode.</td><td>操作码:命令操作码。</td></tr>
<tr><td>02h</td><td>2</td><td>Command Effect: Bitmask that contains one or more effects for the command opcode.<br>• Bit[0]: Configuration Change after Cold Reset<br>• Bit[1]: Immediate Configuration Change<br>• Bit[2]: Immediate Data Change<br>• Bit[3]: Immediate Policy Change<br>• Bit[4]: Immediate Log Change<br>• Bit[5]: Security State Change<br>• Bit[6]: Background Operation<br>• Bit[7]: Secondary Mailbox Supported<br>• Bit[8]: Request Abort Background Operation Supported<br>• Bit[9]: CEL[11:10] Valid<br>• Bit[10]: Configuration Change after Conventional Reset<br>• Bit[11]: Configuration Change after CXL Reset<br>• Bits[15:12]: Reserved: Shall be cleared to 0h.</td><td>命令效果:包含命令操作码的一个或多个效果的位掩码。<br>• Bit[0]:Cold Reset 后的配置更改<br>• Bit[1]:立即配置更改<br>• Bit[2]:立即数据更改<br>• Bit[3]:立即策略更改<br>• Bit[4]:立即日志更改<br>• Bit[5]:安全状态更改<br>• Bit[6]:后台操作<br>• Bit[7]:支持 Secondary Mailbox<br>• Bit[8]:支持 Request Abort Background Operation<br>• Bit[9]:CEL[11:10] 有效<br>• Bit[10]:Conventional Reset 后的配置更改<br>• Bit[11]:CXL Reset 后的配置更改<br>• Bits[15:12]:保留:应清零为 0h。</td></tr>
</tbody>
</table>

> **Figure 8-X.** CEL Entry Structure (page 678) ｜ CEL 条目结构
>
> <img src="figures/chapter_08/page_0678.png" alt="Figure 8-X page 678" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0678.png)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Component State Dump Log can be populated in two ways:<br>• Auto populate<br>• Manual populate using Populate Log</td><td style="background-color:#e8e8e8">Component State Dump Log 可通过两种方式填充:<br>• Auto populate(自动填充)<br>• Manual populate using Populate Log(使用 Populate Log 手动填充)</td></tr>
<tr><td>A component that supports the Component State Dump Log shall support at least one of the above methods.</td><td style="background-color:#e8e8e8">支持 Component State Dump Log 的组件应至少支持上述方法之一。</td></tr>
<tr><td>The two methods and their associated trigger requirements are detailed in Table 8-88. The Component State Dump Log shall be populated by a given method if the trigger occurs, and the logical AND of all the conditions for that trigger is true.</td><td style="background-color:#e8e8e8">这两种方法及其相关触发要求详见表 8-88。如果触发器发生且该触发器的所有条件的逻辑 AND 为真,则 Component State Dump Log 应通过给定方法填充。</td></tr>
<tr><td>The trigger for the auto populate method is vendor specific, but one example may be a severe internal error in the component.</td><td style="background-color:#e8e8e8">Auto populate 方法的触发器由厂商特定定义,但一个示例可能是组件中的严重内部错误。</td></tr>
<tr><td>When a population method triggers and all required conditions are met, any existing Component State Dump Data is cleared before populating the new log contents.</td><td style="background-color:#e8e8e8">当 population 方法触发且满足所有必需条件时,任何现有的 Component State Dump Data 将在填充新日志内容之前被清除。</td></tr>
<tr><td>The log contents should persist across cold reset. The component shall indicate whether the log persists across cold reset using the Persistent Across Cold Reset bit in the Get Log Capabilities Output Payload.</td><td style="background-color:#e8e8e8">日志内容应在冷复位后保留。组件应使用 Get Log Capabilities Output Payload 中的 Persistent Across Cold Reset 位来指示日志是否在冷复位后保留。</td></tr>
<tr><td>If the component has Component State Dump Data available to be reported in the Component State Dump Log after a subsequent reset, the Component State Dump Log contents shall be available when the Mailbox Interfaces Ready bit in the Memory Device Status register is set to 1.</td><td style="background-color:#e8e8e8">如果组件在后续复位后有 Component State Dump Data 可在 Component State Dump Log 中报告,则当 Memory Device Status 寄存器中的 Mailbox Interfaces Ready 位设置为 1 时,Component State Dump Log 内容应可用。</td></tr>
<tr><td>To handle corner cases related to an existing Component State Dump Log being overwritten by an Auto Populate trigger while host software is reading the existing contents of the log, host software must begin each Component State Dump Log fetch sequence by issuing a Get Log command with Offset = 0, followed by zero or more Get Log commands with nonzero offset. If the component is reset, host software must start a new fetch sequence.</td><td style="background-color:#e8e8e8">为了处理与现有 Component State Dump Log 在主机软件读取日志现有内容时被 Auto Populate 触发器覆盖相关的边缘情况,主机软件必须通过发出 Offset = 0 的 Get Log 命令来开始每个 Component State Dump Log 提取序列,然后再发出零个或多个具有非零 offset 的 Get Log 命令。如果组件被重置,主机软件必须开始新的提取序列。</td></tr>
<tr><td>If a Get Log command with nonzero Offset is received requesting the Component State Dump Log, the component shall apply the first applicable case from the following list:<br>• Return Invalid Input if the component has not previously returned Success for a Get Log command with Offset = 0 requesting the Component State Dump Log.<br>• Return Interrupted if the contents of the Component State Dump Log have changed since the last time the component returned Success for a Get Log command with Offset = 0 requesting the Component State Dump Log.<br>• Return Success and provide the log contents of the specified offset corresponding to the state of the Component State Dump Log when the current fetch sequence began (i.e., when the last Get Log command with Offset = 0 requesting the Component State Dump Log was completed with a return code of Success).</td><td style="background-color:#e8e8e8">如果收到具有非零 Offset 的 Get Log 命令请求 Component State Dump Log,组件应从以下列表中应用第一个适用的情况:<br>• 如果组件之前未对请求 Component State Dump Log 且 Offset = 0 的 Get Log 命令返回 Success,则返回 Invalid Input。<br>• 如果自组件上次对请求 Component State Dump Log 且 Offset = 0 的 Get Log 命令返回 Success 以来,Component State Dump Log 的内容已更改,则返回 Interrupted。<br>• 返回 Success 并提供与当前提取序列开始时 Component State Dump Log 状态相对应的指定 offset 的日志内容。</td></tr>
</tbody>
</table>

**Table 8-88. Component State Dump Log Population Methods and Triggers | Component State Dump Log 填充方法和触发器**

<table>
<thead>
<tr><th>Method</th><th>Trigger</th><th>Condition</th><th>Condition Reference</th></tr>
</thead>
<tbody>
<tr><td>Auto Populate</td><td>Vendor-specific</td><td>Auto Populate Trigger Count Since Clear = 0</td><td>Table 8-89. Component State Dump Log Format</td></tr>
<tr><td></td><td></td><td>Auto Populate Supported = 1</td><td>Table 8-102. Get Log Capabilities Output Payload</td></tr>
<tr><td>Manual Populate</td><td>Populate Log command received</td><td>Log Identifier = b3fab4cf-01b6-4332-943e-5e9962f23567</td><td>Table 8-104. Populate Log Input Payload</td></tr>
<tr><td></td><td></td><td>Populate Log Supported = 1</td><td>Table 8-102. Get Log Capabilities Output Payload</td></tr>
</tbody>
</table>

> **Figure 8-X.** Component State Dump Log (page 679) ｜ Component State Dump Log
>
> <img src="figures/chapter_08/page_0679.png" alt="Figure 8-X page 679" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0679.png)

**Table 8-89. Component State Dump Log Format | Component State Dump Log 格式**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Component State Dump Data Length: Length of the Component State Dump Data field in bytes.</td><td>Component State Dump Data 长度(以字节为单位):Component State Dump Data 字段的长度。</td></tr>
<tr><td>04h</td><td>1</td><td>Auto Populate Trigger Count Since Clear: Number of Auto Populate triggers since last clear. Tracking is optional. Saturates at FFh.</td><td>自清除以来的 Auto Populate 触发计数:自上次清除 Component State Dump Log 以来遇到 Auto Populate 触发器的次数。可选跟踪。在 FFh 处饱和。</td></tr>
<tr><td>05h</td><td>1</td><td>Event Log: The Event Log, as defined in Table 8-64 (Get Event Records Input Payload), containing the Associated Event Record Handle.</td><td>Event Log:如表 8-64(Get Event Records Input Payload)所定义的事件日志,包含 Associated Event Record Handle。</td></tr>
<tr><td>06h</td><td>2</td><td>Associated Event Record Handle: The Event Record Handle corresponding to the Auto Populate trigger that generated the Component State Dump Data.</td><td>Associated Event Record Handle:与生成 Component State Dump Data 的 Auto Populate 触发器关联的 Event Record 对应的 Event Record Handle。</td></tr>
<tr><td>08h</td><td>8</td><td>Timestamp: The Timestamp at the time the Component State Dump Data was generated.</td><td>时间戳:Component State Dump Data 生成时的时间戳。</td></tr>
<tr><td>10h</td><td>10h</td><td>Component State Dump Format UUID: Optional value to uniquely identify the format of the Component State Dump Data field. A value of all 0s indicates that the format is not indicated.</td><td>Component State Dump Format UUID:用于唯一标识 Component State Dump Data 字段格式的可选值。全为 0 表示未指示格式。</td></tr>
<tr><td>20h</td><td>4</td><td>Flags<br>• Bit[0]: Auto Populate Data<br>• Bits[31:1]: Reserved</td><td>标志位<br>• Bit[0]:Auto Populate Data<br>• Bits[31:1]:保留</td></tr>
<tr><td>24h</td><td>1Ch</td><td>Reserved</td><td>保留</td></tr>
<tr><td>40h</td><td>Varies</td><td>Component State Dump Data: Vendor specific.</td><td>Component State Dump Data:厂商特定。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Component State Dump Log Format (page 680) ｜ Component State Dump Log 格式
>
> <img src="figures/chapter_08/page_0680.png" alt="Figure 8-X page 680" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0680.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-4"></a>
### 8.2.10.5.2.4 DDR5 Error Check Scrub (ECS) Log | DDR5 错误检查清除 (ECS) 日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Log Identifier: f1720d60-a7a9-4306-a003-11948f9e077c</td><td style="background-color:#e8e8e8">日志标识符:f1720d60-a7a9-4306-a003-11948f9e077c</td></tr>
<tr><td>DDR5 ECS Log allows the host to observe the ECS operation results. The format of the DDR5 ECS Log is shown in Table 8-90.</td><td style="background-color:#e8e8e8">DDR5 ECS Log 允许主机观察 ECS 操作结果。DDR5 ECS Log 的格式如表 8-90 所示。</td></tr>
</tbody>
</table>

**Table 8-90. DDR5 Error Check Scrub (ECS) Log | DDR5 错误检查清除 (ECS) 日志**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Common Header<br>• Bits[9:0]: Total Number of Entries<br>• Bit[10]: If 0, Component ID field is vendor specific. If 1, the format is defined in Table 8-56.<br>• Bits[12:11]: Entry Type: 00b = Per DRAM; 01b = Per Memory Media FRU; All other encodings reserved.<br>• Bits[31:13]: Reserved</td><td>Common Header<br>• Bits[9:0]:条目总数<br>• Bit[10]:如果为 0,Component ID 字段由厂商定义。如果为 1,格式由表 8-56 定义。<br>• Bits[12:11]:条目类型:00b = Per DRAM;01b = Per Memory Media FRU;所有其他编码保留。<br>• Bits[31:13]:保留</td></tr>
<tr><td>04h</td><td>10h</td><td>Entry 1 Component Identifier</td><td>条目 1 组件标识符</td></tr>
<tr><td>14h</td><td>2</td><td>Entry 1 DDR5 ECS Configurations<br>• Bits[2:0]: ECS Threshold Count per Gb of Memory Cells: 011b = 256 (default); 100b = 1024; 101b = 4096; All other encodings are reserved<br>• Bit[3]: Codeword/Row Count Mode: 0 = ECS counts rows with errors; 1 = ECS counts codewords with errors<br>• Bits[15:4]: Reserved</td><td>条目 1 DDR5 ECS 配置<br>• Bits[2:0]:每 Gb 内存单元的 ECS 阈值计数:011b = 256(默认);100b = 1024;101b = 4096;所有其他编码保留<br>• Bit[3]:码字/行计数模式:0 = ECS 计数有错误的行;1 = ECS 计数有错误的码字<br>• Bits[15:4]:保留</td></tr>
<tr><td>16h</td><td>10h</td><td>Entry 1 Error Count and Address Information<br>• Bit[0]: Error Found<br>• Bits[7:1]: Reserved<br>• Bits[23:8]: Error Count or the Number of Rows or Codeword Errors<br>• Bits[31:24]: Max Row Error Count<br>• Bits[95:32]: Address with Max Errors<br>• Bits[127:96]: Reserved</td><td>条目 1 错误计数和地址信息<br>• Bit[0]:发现错误<br>• Bits[7:1]:保留<br>• Bits[23:8]:错误计数或行/码字错误数<br>• Bits[31:24]:最大行错误计数<br>• Bits[95:32]:错误最多的地址<br>• Bits[127:96]:保留</td></tr>
<tr><td>04h+((n-1)*22h)</td><td>10h</td><td>Entry n Component Identifier</td><td>条目 n 组件标识符</td></tr>
<tr><td>14h+((n-1)*22h)</td><td>2</td><td>Entry n DDR5 ECS Configurations</td><td>条目 n DDR5 ECS 配置</td></tr>
<tr><td>16h+((n-1)*22h)</td><td>10h</td><td>Entry n Error Count and Address Information</td><td>条目 n 错误计数和地址信息</td></tr>
</tbody>
</table>

> **Figure 8-X.** DDR5 ECS Log (page 681-682) ｜ DDR5 ECS 日志
>
> <img src="figures/chapter_08/page_0681.png" alt="Figure 8-X page 681" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0681.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-5"></a>
### 8.2.10.5.2.5 Media Test Capability Log | 介质测试能力日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Media Test Capability Log is a variable-length log structure that conveys the attributes of the different media tests that the CXL device supports. It is composed of a common header (see Table 8-91) and Media Test Capability Log Entries (see Table 8-93) for each supported test.</td><td style="background-color:#e8e8e8">Media Test Capability Log 是一种可变长度的日志结构,用于传达 CXL 设备支持的不同介质测试的属性。它由 common header(参见表 8-91)和每个受支持测试的 Media Test Capability Log Entries(参见表 8-93)组成。</td></tr>
<tr><td>Table 8-92 describes the attributes that are common to all the tests that the device supports (e.g., Error Signature List Size, Media Test Result Long, and Short Log versions and Capabilities flags).</td><td style="background-color:#e8e8e8">表 8-92 描述了设备支持的所有测试共有的属性(例如,Error Signature List Size、Media Test Result Long 和 Short Log 版本以及 Capabilities 标志)。</td></tr>
</tbody>
</table>

**Table 8-91. Media Test Capability Log Output Payload | Media Test Capability Log 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>16</td><td>Common Header: Reports attributes applicable to all the tests and general capabilities of the device.</td><td>Common Header:报告适用于所有测试的属性以及设备的一般能力。</td></tr>
<tr><td>10h</td><td>16</td><td>Test 1 Media Test Capability Log Entry</td><td>测试 1 的 Media Test Capability Log 条目</td></tr>
<tr><td>20h</td><td>16</td><td>Test 2 Media Test Capability Log Entry</td><td>测试 2 的 Media Test Capability Log 条目</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>(16+16*(n-1))h</td><td>16</td><td>Test n Media Test Capability Log Entry</td><td>测试 n 的 Media Test Capability Log 条目</td></tr>
</tbody>
</table>

**Table 8-92. Media Test Capability Log Common Header | Media Test Capability Log Common Header**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Supported Tests: Total number of test types that the device supports.</td><td>支持的测试数:设备支持的测试类型总数。</td></tr>
<tr><td>01h</td><td>4</td><td>Total Number of Error Signatures</td><td>错误签名总数</td></tr>
<tr><td>05h</td><td>1</td><td>Media Test Result Long Log Version</td><td>Media Test Result Long Log 版本</td></tr>
<tr><td>06h</td><td>1</td><td>Media Test Result Short Log Version</td><td>Media Test Result Short Log 版本</td></tr>
<tr><td>07h</td><td>1</td><td>Capabilities: Bit[0]: Data ECC Disablement Capability; Bit[1]: Metadata ECC Disablement Capability; Bit[2]: Data and Metadata ECC Disablement Capability; Bit[3]: Metadata Area Testing Capability; Bits[7:4]: Reserved</td><td>能力:Bit[0]:数据 ECC 禁用能力;Bit[1]:元数据 ECC 禁用能力;Bit[2]:数据和元数据 ECC 禁用能力;Bit[3]:元数据区域测试能力;Bits[7:4]:保留</td></tr>
<tr><td>08h</td><td>8</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Capability Log (page 682-683) ｜ Media Test Capability Log
>
> <img src="figures/chapter_08/page_0682.png" alt="Figure 8-X page 682" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0682.png)

**Table 8-93. Media Test Capability Log Entry Structure | Media Test Capability Log Entry 结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: Unique ID to identify the Test.</td><td>Test ID:用于标识测试的唯一 ID。</td></tr>
<tr><td>02h</td><td>1</td><td>Algorithm: Media test algorithm supported.</td><td>算法:支持的介质测试算法。</td></tr>
<tr><td>03h</td><td>1</td><td>Execution Time: Maximum test execution time per GB.</td><td>执行时间:每 GB 的最大测试执行时间。</td></tr>
<tr><td>04h</td><td>2</td><td>Capabilities: Bit[0]: Address Configurable Flag; Bit[1]: Inverse Pattern Support; Bit[2]: Exit on Uncorrectable Error; Bit[3]: Error Count Threshold Programmable; Bit[4]: Update Poison List on Uncorrectable Error; Bits[8:5]: Addressing Mode</td><td>能力:Bit[0]:地址可配置标志;Bit[1]:反码支持;Bit[2]:遇到不可纠正错误时退出;Bit[3]:错误计数阈值可编程;Bit[4]:在不可纠正错误时更新 Poison List;Bits[8:5]:寻址模式</td></tr>
<tr><td>06h</td><td>2</td><td>Supported Patterns: Bitmap of supported 64B patterns.</td><td>支持的模式:支持的 64B 模式位图。</td></tr>
<tr><td>08h</td><td>1</td><td>PRBS Length: Length of the PRBS sequence.</td><td>PRBS 长度:PRBS 序列的长度。</td></tr>
<tr><td>09h</td><td>7</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>For each media test that the device supports, an individual Media Test Capability Log Entry shall be defined. A single test shall be described by the fields defined in Table 8-93, comprising the Test ID, the Algorithm of the Test, the estimated Execution time per GB, etc.</td><td style="background-color:#e8e8e8">对于设备支持的每个介质测试,应定义一个单独的 Media Test Capability Log Entry。单个测试应由表 8-93 中定义的字段描述,包括 Test ID、测试的 Algorithm、每 GB 的估计 Execution time 等。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Capability Log Entry (page 683-684) ｜ Media Test Capability Log Entry
>
> <img src="figures/chapter_08/page_0683.png" alt="Figure 8-X page 683" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0683.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-2-6"></a>
### 8.2.10.5.2.6 Media Test Results Logs | 介质测试结果日志

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Media Test Results Logs are variable-length logs that provide the results of one or more Media Tests. Two types of logs are available:<br>• Media Test Results Short Log: Status info and results of the execute tests (see Table 8-94)<br>• Media Test Results Long Log: Detailed error information and error signatures of the executed tests (see Table 8-97)</td><td style="background-color:#e8e8e8">Media Test Results Logs 是可变长度的日志,用于提供一项或多项 Media Tests 的结果。有两种类型的日志可用:<br>• Media Test Results Short Log:已执行测试的状态信息和结果(参见表 8-94)<br>• Media Test Results Long Log:已执行测试的详细错误信息和错误签名(参见表 8-97)</td></tr>
<tr><td>Media Test Result Logs are produced at the end of the execution of the tests and are cleared when a new test starts or when the Clear Log command is issued.</td><td style="background-color:#e8e8e8">Media Test Result Logs 在测试执行结束时生成,并在开始新测试或发出 Clear Log 命令时被清除。</td></tr>
<tr><td>Media Test Results Short Log enumerates the results of the tests executed by the CXL device.</td><td style="background-color:#e8e8e8">Media Test Results Short Log 枚举 CXL 设备执行的测试结果。</td></tr>
<tr><td>Each Media Test Results Short Log Entry contains the results of the test executed (see Table 8-96). They are preceded by a common header described in Table 8-95.</td><td style="background-color:#e8e8e8">每个 Media Test Results Short Log Entry 包含已执行测试的结果(参见表 8-96)。它们前面是表 8-95 中描述的 common header。</td></tr>
</tbody>
</table>

**Table 8-94. Media Test Results Short Log | Media Test Results Short Log**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Common Header: Common output information from test execution.</td><td>Common Header:测试执行的通用输出信息。</td></tr>
<tr><td>10h</td><td>20h</td><td>Test 1 Media Test Results Short Log Entry</td><td>测试 1 的 Media Test Results Short Log Entry</td></tr>
<tr><td>30h</td><td>20h</td><td>Test 2 Media Test Results Short Log Entry</td><td>测试 2 的 Media Test Results Short Log Entry</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>(10h+20h*(n-1))h</td><td>20h</td><td>Test n Media Test Results Short Log Entry</td><td>测试 n 的 Media Test Results Short Log Entry</td></tr>
</tbody>
</table>

**Table 8-95. Media Test Results Short Log Entry Common Header | Media Test Results Short Log Entry Common Header**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Tests Executed</td><td>已执行的测试数</td></tr>
<tr><td>01h</td><td>1</td><td>Version: This field shall be set to 01h.</td><td>版本:此字段应设置为 01h。</td></tr>
<tr><td>02h</td><td>1</td><td>Result: 00h = All tests completed successfully; 01h = At least one test completed with failure; 02h = Test execution was interrupted by a Request Abort Background Operation command (all tests that completed, before abort, ended successfully); 03h = Test execution was interrupted by a Request Abort Background Operation command (at least one test completed with failure); All other encodings are reserved</td><td>结果:00h = 所有测试成功完成;01h = 至少一个测试失败完成;02h = 测试执行被 Request Abort Background Operation 命令中断(中止前完成的所有测试均成功结束);03h = 测试执行被 Request Abort Background Operation 命令中断(中止前至少一个测试失败);所有其他编码保留</td></tr>
<tr><td>03h</td><td>Dh</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Results Short Log (page 685) ｜ Media Test Results Short Log
>
> <img src="figures/chapter_08/page_0685.png" alt="Figure 8-X page 685" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0685.png)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Media Test Results Long Log reports the same fields defined for the Short version. It also includes the capacity tested by the device and the error signature, which consists of:<br>• Test iteration in which the error occurred<br>• Failed DPA with a flag that indicates the error type (i.e., uncorrectable or correctable)<br>• Memory component address following the format defined in the DRAM Event Record</td><td style="background-color:#e8e8e8">Media Test Results Long Log 报告为 Short 版本定义的相同字段。它还包括设备测试的容量和错误签名,后者包括:<br>• 发生错误的测试迭代<br>• 失败的 DPA 及指示错误类型的标志(即,不可纠正或可纠正)<br>• 遵循 DRAM Event Record 中定义的格式的内存组件地址</td></tr>
<tr><td>When using the Media Test Results Long Log, two reporting options are available:<br>• Complete: Count and report all the error signatures (with and without threshold programmed)<br>• Single error signature: If error count threshold is set, only the signature of the first error after the threshold is exceeded is reported. If error count threshold is not set, only the signature of the first error encountered is reported.</td><td style="background-color:#e8e8e8">使用 Media Test Results Long Log 时,有两种报告选项可用:<br>• Complete(完整):计数并报告所有错误签名(无论是否编程了阈值)<br>• Single error signature(单个错误签名):如果设置了错误计数阈值,则仅报告超过阈值后的第一个错误的签名。如果未设置错误计数阈值,则仅报告遇到的第一个错误的签名。</td></tr>
<tr><td>The device tracks the error information in the Error Signature Lists. The total number of Error Signatures cannot exceed the value indicated by the Total Number of Error Signatures field in the Media Test Capability Log (see Table 8-91). If the Error Signature Configuration bit (see Table 8-123) is set and the total number of errors exceeds the Total Number of Error Signatures, bit[1] in the Flags field shall be set and the test execution shall be interrupted by the device. The test may be resumed from the point at which it was interrupted due to the lack of resources to log the error signatures.</td><td style="background-color:#e8e8e8">设备在 Error Signature Lists 中跟踪错误信息。Error Signatures 的总数不能超过 Media Test Capability Log(参见表 8-91)中 Total Number of Error Signatures 字段所指示的值。如果设置了 Error Signature Configuration 位(参见表 8-123),且错误总数超过 Total Number of Error Signatures,则应设置 Flags 字段中的 bit[1],并且测试执行应被设备中断。可以从由于缺乏记录错误签名的资源而被中断的点恢复测试。</td></tr>
</tbody>
</table>

**Table 8-96. Media Test Results Short Log Entry Structure | Media Test Results Short Log Entry 结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: ID of the test.</td><td>Test ID:测试的 ID。</td></tr>
<tr><td>02h</td><td>8</td><td>Start Time: Expressed as timestamp.</td><td>Start Time:以时间戳表示。</td></tr>
<tr><td>0Ah</td><td>8</td><td>End Time: Expressed as timestamp.</td><td>End Time:以时间戳表示。</td></tr>
<tr><td>12h</td><td>1</td><td>Result: 00h = Completed with success; 01h = Completed with failure; 02h = Aborted by a Request Abort Background Operation command; All other encodings are reserved</td><td>结果:00h = 成功完成;01h = 失败完成;02h = 被 Request Abort Background Operation 命令中止;所有其他编码保留</td></tr>
<tr><td>13h</td><td>1</td><td>Flags: Bit[0]: Error Signature List Overflow; Bits[7:1]: Reserved</td><td>标志位:Bit[0]:错误签名列表溢出;Bits[7:1]:保留</td></tr>
<tr><td>14h</td><td>4</td><td>Uncorrectable Error Count: Total number of uncorrectable memory errors that the device detected during the test.</td><td>不可纠正错误计数:设备在测试期间检测到的不可纠正内存错误总数。</td></tr>
<tr><td>18h</td><td>4</td><td>Correctable Error Count: Total number of correctable memory errors that the device detected during the test.</td><td>可纠正错误计数:设备在测试期间检测到的可纠正内存错误总数。</td></tr>
<tr><td>1Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Test Results Long Log (page 686-689) ｜ Media Test Results Long Log
>
> <img src="figures/chapter_08/page_0686.png" alt="Figure 8-X page 686" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0686.png)

**Table 8-97. Media Test Results Long Log | Media Test Results Long Log**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Common Header: Common output information from test execution.</td><td>Common Header:测试执行的通用输出信息。</td></tr>
<tr><td>10h</td><td>variable</td><td>Test 1 Media Test Results Long Log Entry</td><td>测试 1 的 Media Test Results Long Log Entry</td></tr>
<tr><td>variable</td><td>variable</td><td>Test 2 Media Test Results Long Log Entry</td><td>测试 2 的 Media Test Results Long Log Entry</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>variable</td><td>variable</td><td>Test n Media Test Results Long Log Entry</td><td>测试 n 的 Media Test Results Long Log Entry</td></tr>
</tbody>
</table>

**Table 8-98. Media Test Results Long Log Entry Common Header | Media Test Results Long Log Entry Common Header**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Tests Executed</td><td>已执行的测试数</td></tr>
<tr><td>01h</td><td>1</td><td>Version: This field shall be set to 1.</td><td>版本:此字段应设置为 1。</td></tr>
<tr><td>02h</td><td>1</td><td>Result: 00h = All tests completed successfully; 01h = At least one test completed with failure; 02h = Test execution interrupted (all completed tests ended successfully); 03h = Test execution interrupted (at least one test failed); All other encodings are reserved</td><td>结果:00h = 所有测试成功完成;01h = 至少一个测试失败完成;02h = 测试执行中断(所有已完成的测试均成功);03h = 测试执行中断(至少一个测试失败);所有其他编码保留</td></tr>
<tr><td>03h</td><td>0Dh</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

**Table 8-99. Media Test Results Long Log Entry Structure | Media Test Results Long Log Entry 结构**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: ID of the test.</td><td>Test ID:测试的 ID。</td></tr>
<tr><td>02h</td><td>8</td><td>Start Time</td><td>Start Time(开始时间)</td></tr>
<tr><td>0Ah</td><td>8</td><td>End Time</td><td>End Time(结束时间)</td></tr>
<tr><td>12h</td><td>1</td><td>Result: 00h = Completed with success; 01h = Completed with failure; 02h = Aborted; All other encodings reserved</td><td>结果:00h = 成功完成;01h = 失败完成;02h = 中止;所有其他编码保留</td></tr>
<tr><td>13h</td><td>1</td><td>Flags: Bit[0]: Error Signature List Overflow; Bits[7:1]: Reserved</td><td>标志位:Bit[0]:错误签名列表溢出;Bits[7:1]:保留</td></tr>
<tr><td>14h</td><td>4</td><td>Uncorrectable Error Count</td><td>不可纠正错误计数</td></tr>
<tr><td>18h</td><td>4</td><td>Correctable Error Count</td><td>可纠正错误计数</td></tr>
<tr><td>1Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>8</td><td>Capacity Tested: Expressed in multiples of 256 MB.</td><td>Capacity Tested:以 256 MB 的倍数表示。</td></tr>
<tr><td>28h</td><td>4</td><td>Number of Error Signatures: Total number of error signatures reported by the device in the test.</td><td>Number of Error Signatures:设备在测试中报告的错误签名总数。</td></tr>
<tr><td>2Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>30h</td><td>50h</td><td>Error Signature 1</td><td>Error Signature 1</td></tr>
<tr><td>80h</td><td>50h</td><td>Error Signature 2</td><td>Error Signature 2</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>30h+((N-1)*50)h</td><td>50h</td><td>Error Signature N</td><td>Error Signature N</td></tr>
</tbody>
</table>

**Table 8-100. Error Signature | Error Signature**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Iteration: This field indicates the test iteration in which the error occurred.</td><td>Iteration:此字段指示发生错误的测试迭代。</td></tr>
<tr><td>02h</td><td>8</td><td>Physical Address: The physical address at which the error occurred during the test execution.<br>• Bit[0]: Volatile: 0 = DPA is within the persistent memory range; 1 = DPA field is within the volatile memory range<br>• Bits[2:1]: Error Type: 00b = Uncorrectable; 01b = Correctable; All other encodings reserved<br>• Bit[3]: Inverse Pattern<br>• Bits[5:4]: Reserved<br>• Bits[63:6]: DPA</td><td>Physical Address:测试执行期间发生错误的物理地址。<br>• Bit[0]:Volatile:0 = DPA 在持久性内存范围内;1 = DPA 字段在易失性内存范围内<br>• Bits[2:1]:Error Type:00b = 不可纠正;01b = 可纠正;所有其他编码保留<br>• Bit[3]:反码<br>• Bits[5:4]:保留<br>• Bits[63:6]:DPA</td></tr>
<tr><td>0Ah</td><td>2</td><td>Validity Flags: Indicators of which fields are valid within the returned data.<br>• Bit[0]: Channel field is valid<br>• Bit[1]: Rank field is valid<br>• Bit[2]: Nibble Mask field is valid<br>• Bit[3]: Bank Group field is valid<br>• Bit[4]: Bank field is valid<br>• Bit[5]: Row field is valid<br>• Bit[6]: Column field is valid<br>• Bit[7]: Correction Mask field is valid<br>• Bit[8]: Component Identifier field is valid<br>• Bit[9]: Component Identifier format governed by Table 8-56<br>• Bit[10]: Sub-channel field is valid<br>• Bits[15:11]: Reserved</td><td>Validity Flags:指示返回数据中哪些字段有效。<br>• Bit[0]:Channel 字段有效<br>• Bit[1]:Rank 字段有效<br>• Bit[2]:Nibble Mask 字段有效<br>• Bit[3]:Bank Group 字段有效<br>• Bit[4]:Bank 字段有效<br>• Bit[5]:Row 字段有效<br>• Bit[6]:Column 字段有效<br>• Bit[7]:Correction Mask 字段有效<br>• Bit[8]:Component Identifier 字段有效<br>• Bit[9]:Component Identifier 格式由表 8-56 规定<br>• Bit[10]:Sub-channel 字段有效<br>• Bits[15:11]:保留</td></tr>
<tr><td>0Ch</td><td>1</td><td>Channel</td><td>Channel(通道)</td></tr>
<tr><td>0Dh</td><td>1</td><td>Rank</td><td>Rank(秩)</td></tr>
<tr><td>0Eh</td><td>3</td><td>Nibble Mask: Identifies one or more nibbles in error on the memory bus producing the event.</td><td>Nibble Mask:标识产生事件的内存总线上一个或多个错误的半字节。</td></tr>
<tr><td>11h</td><td>1</td><td>Bank Group</td><td>Bank Group(Bank 组)</td></tr>
<tr><td>12h</td><td>1</td><td>Bank</td><td>Bank(Bank 号)</td></tr>
<tr><td>13h</td><td>3</td><td>Row</td><td>Row(行号)</td></tr>
<tr><td>16h</td><td>2</td><td>Column</td><td>Column(列号)</td></tr>
<tr><td>18h</td><td>20h</td><td>Correction Mask: Identifies the bits in error within that nibble in error on the memory bus that produced the error.</td><td>Correction Mask:标识产生错误的内存总线上该错误半字节内的错误位。</td></tr>
<tr><td>38h</td><td>10h</td><td>Component Identifier: Device-specific component identifier.</td><td>Component Identifier:设备特定的组件标识符。</td></tr>
<tr><td>48h</td><td>1</td><td>Sub-channel</td><td>Sub-channel(子通道)</td></tr>
<tr><td>49h</td><td>7</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Error Signature (page 688-689) ｜ Error Signature
>
> <img src="figures/chapter_08/page_0688.png" alt="Figure 8-X page 688" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0688.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-3"></a>
## 8.2.10.5.3 Get Log Capabilities (Opcode 0402h) | 获取日志能力 (操作码 0402h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Gets capabilities related to the specified log. If the component supports this command, it shall be implemented for all Log Identifier UUIDs that the component supports. This command shall return Invalid Log if the specified Log Identifier is not supported by the component.</td><td style="background-color:#e8e8e8">获取与指定日志相关的能力。如果组件支持此命令,则应针对组件支持的所有 Log Identifier UUID 实现此命令。如果组件不支持指定的 Log Identifier,则此命令应返回 Invalid Log。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Invalid Log</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Invalid Log(无效日志)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-101. Get Log Capabilities Input Payload | Get Log Capabilities 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log for which to get capabilities.</td><td>日志标识符(UUID):表示要获取其能力的日志的 UUID。</td></tr>
</tbody>
</table>

**Table 8-102. Get Log Capabilities Output Payload | Get Log Capabilities 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Parameter Flags<br>• Bit[0]: Clear Log Supported: This bit is set to 1 if the log supports being cleared via the Clear Log command.<br>• Bit[1]: Populate Log Supported: This bit is set to 1 if the log supports being populated via the Populate Log command.<br>• Bit[2]: Auto Populate Supported: This bit is set to 1 if the log supports the ability of being auto populated.<br>• Bit[3]: Persistent across Cold Reset: This bit is set to 1 if the log is persistent across Cold Reset.<br>• Bits[31:4]: Reserved</td><td>Parameter Flags(参数标志)<br>• Bit[0]:Clear Log Supported:如果日志支持通过 Clear Log 命令清除,则此位设置为 1。<br>• Bit[1]:Populate Log Supported:如果日志支持通过 Populate Log 命令填充,则此位设置为 1。<br>• Bit[2]:Auto Populate Supported:如果日志支持自动填充能力,则此位设置为 1。<br>• Bit[3]:Persistent across Cold Reset:如果日志在冷复位后保留,则此位设置为 1。<br>• Bits[31:4]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Log Capabilities (page 690) ｜ Get Log Capabilities
>
> <img src="figures/chapter_08/page_0690.png" alt="Figure 8-X page 690" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0690.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-4"></a>
## 8.2.10.5.4 Clear Log (Opcode 0403h) | 清除日志 (操作码 0403h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Clears the contents of the specified log.</td><td style="background-color:#e8e8e8">清除指定日志的内容。</td></tr>
<tr><td>This command shall return Invalid Log if the specified Log Identifier is not supported by the component.</td><td style="background-color:#e8e8e8">如果组件不支持指定的 Log Identifier,则此命令应返回 Invalid Log。</td></tr>
<tr><td>This command shall return Invalid Input if the specified Log Identifier does not have the Clear Log Supported bit set to 1 in the Get Log Capabilities Output Payload.</td><td style="background-color:#e8e8e8">如果指定的 Log Identifier 在 Get Log Capabilities Output Payload 中的 Clear Log Supported 位未设置为 1,则此命令应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Invalid Log</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Invalid Log(无效日志)</td></tr>
</tbody>
</table>

**Table 8-103. Clear Log Input Payload | Clear Log 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log to clear.</td><td>日志标识符(UUID):表示要清除的日志的 UUID。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Clear Log / Populate Log (page 691) ｜ Clear Log / Populate Log
>
> <img src="figures/chapter_08/page_0691.png" alt="Figure 8-X page 691" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0691.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-5"></a>
## 8.2.10.5.5 Populate Log (Opcode 0404h) | 填充日志 (操作码 0404h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Populates the contents of the specified log.</td><td style="background-color:#e8e8e8">填充指定日志的内容。</td></tr>
<tr><td>This may be a background operation. If the component implements this command as a background operation for any supported Log Identifier, the Background Operation bit in the Command Effects Log entry for Populate Log shall be set to 1.</td><td style="background-color:#e8e8e8">这可以是后台操作。如果组件对任何受支持的 Log Identifier 将此命令实现为后台操作,则 Populate Log 的 Command Effects Log 条目中的 Background Operation 位应设置为 1。</td></tr>
<tr><td>This command shall return Invalid Log if the specified Log Identifier is not supported by the component.</td><td style="background-color:#e8e8e8">如果组件不支持指定的 Log Identifier,则此命令应返回 Invalid Log。</td></tr>
<tr><td>This command shall return Invalid Input if the specified Log Identifier does not have the Populate Log Supported bit set to 1 in the Get Log Capabilities Output Payload.</td><td style="background-color:#e8e8e8">如果指定的 Log Identifier 在 Get Log Capabilities Output Payload 中的 Populate Log Supported 位未设置为 1,则此命令应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Background Command Started<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Invalid Log<br>• Interrupted<br>• Busy<br>• Aborted</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Background Command Started(后台命令已启动)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Invalid Log(无效日志)<br>• Interrupted(中断)<br>• Busy(忙)<br>• Aborted(中止)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Log Change<br>• Background Operation (if the component implements this command as a background operation for any supported Log Identifier)</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Log Change(立即日志更改)<br>• Background Operation(后台操作)(如果组件对任何受支持的 Log Identifier 将此命令实现为后台操作)</td></tr>
</tbody>
</table>

**Table 8-104. Populate Log Input Payload | Populate Log 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Log Identifier: UUID representing the log to populate.</td><td>日志标识符(UUID):表示要填充的日志的 UUID。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-5-6"></a>
## 8.2.10.5.6 Get Supported Logs Sub-List (Opcode 0405h) | 获取支持的日志子列表 (操作码 0405h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve a sub-list of device-specific log identifiers (each identified by a UUID) and the maximum capacity of each log. This command can retrieve a maximum of 255 log entries. The output of this command shall be consistent with the output of the Get Supported Logs command.</td><td style="background-color:#e8e8e8">检索设备特定日志标识符(每个由 UUID 标识)的子列表以及每个日志的最大容量。此命令最多可检索 255 个日志条目。此命令的输出应与 Get Supported Logs 命令的输出一致。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-105. Get Supported Logs Sub-List Input Payload | Get Supported Logs Sub-List 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Number of Supported Log Entries: The maximum number of Supported Log Entries requested. This field shall have a minimum value of 01h.</td><td>Maximum Number of Supported Log Entries:请求的 Supported Log Entries 的最大数量。此字段的最小值应为 01h。</td></tr>
<tr><td>01h</td><td>1</td><td>Start Log Entry Index: Index of the first requested Supported Log Entry.</td><td>Start Log Entry Index:第一个请求的 Supported Log Entry 的索引。</td></tr>
</tbody>
</table>

**Table 8-106. Get Supported Logs Sub-List Output Payload | Get Supported Logs Sub-List 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Supported Log Entries</td><td>Number of Supported Log Entries(支持的日志条目数)</td></tr>
<tr><td>01h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>02h</td><td>2</td><td>Total Number of Supported Log Entries: The total number of Supported Log Entries supported by the component.</td><td>Total Number of Supported Log Entries:组件支持的 Supported Log Entries 总数。</td></tr>
<tr><td>04h</td><td>1</td><td>Start Log Entry Index: Index of the first Supported Log Entry in the output payload.</td><td>Start Log Entry Index:输出负载中第一个 Supported Log Entry 的索引。</td></tr>
<tr><td>05h</td><td>3</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Supported Log Entries: Device-specific list of supported log identifier UUIDs and the maximum capacity of each log.</td><td>Supported Log Entries:受支持日志标识符 UUID 的设备特定列表以及每个日志的最大容量。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Supported Logs Sub-List (page 692) ｜ Get Supported Logs Sub-List
>
> <img src="figures/chapter_08/page_0692.png" alt="Figure 8-X page 692" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0692.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6"></a>
## 8.2.10.6 Features | 特性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>A Feature is a configuration, control or capability whose setting(s) can be retrieved using Get Feature and optionally modified using Set Feature. Get Feature is used for reporting the values of the associated setting(s). The scope of a Feature is feature-specific and shall be described as part of each Feature's definition. The scope of the Feature may be at the CXL device, LD, Fabric Manager device, or a combination of all these levels.</td><td style="background-color:#e8e8e8">Feature 是一种配置、控制或能力,其设置可以使用 Get Feature 检索,并可选择使用 Set Feature 修改。Get Feature 用于报告相关设置的值。Feature 的范围是特定于 Feature 的,应作为每个 Feature 定义的一部分进行描述。Feature 的范围可在 CXL device、LD、Fabric Manager device 或所有这些级别的组合上。</td></tr>
<tr><td>If a Feature supports changeable attributes that are optional for an implementation, the Set Feature payload describes all changeable attributes and a field that specifies the attribute(s) to update. Any dependencies between different attributes shall be defined by the Feature specification.</td><td style="background-color:#e8e8e8">如果 Feature 支持对实现可选的可更改属性,则 Set Feature 负载描述所有可更改属性以及一个指定要更新的属性的字段。不同属性之间的任何依赖关系应由 Feature 规范定义。</td></tr>
<tr><td>If a Feature is supported on the secondary mailbox, the secondary mailbox shall return identical Set Feature Effects value as the primary mailbox for the Feature's Get Supported Features Supported Feature Entry.</td><td style="background-color:#e8e8e8">如果在 secondary mailbox 上支持 Feature,则 secondary mailbox 应为该 Feature 的 Get Supported Features Supported Feature Entry 返回与 primary mailbox 相同的 Set Feature Effects 值。</td></tr>
<tr><td>Features may evolve by defining new fields in the payload definitions that were originally defined as reserved or by appending new fields.</td><td style="background-color:#e8e8e8">Feature 可以通过在最初定义为保留的负载定义中定义新字段或附加新字段来演进。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-1"></a>
### 8.2.10.6.1 Get Supported Features (Opcode 0500h) | 获取支持的特性 (操作码 0500h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve the list of supported device-specific features (identified by UUID) and general information about each Feature. The device shall return Invalid Input if the Starting Feature Index value is greater than the Device Supported Features value.</td><td style="background-color:#e8e8e8">检索受支持的设备特定 Feature 列表(由 UUID 标识)以及关于每个 Feature 的一般信息。如果 Starting Feature Index 值大于 Device Supported Features 值,设备应返回 Invalid Input。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-107. Get Supported Features Input Payload | Get Supported Features 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Count: Count in bytes of the supported Feature data to return in the output payload. The device shall return no more bytes than requested, but it can return less bytes.</td><td>Count:要在输出负载中返回的受支持 Feature 数据的字节数。设备返回的字节数不应超过请求的字节数,但可以返回较少的字节数。</td></tr>
<tr><td>04h</td><td>2</td><td>Starting Feature Index: Index of the first requested Supported Feature Entry. Feature index is a zero-based value.</td><td>Starting Feature Index:第一个请求的 Supported Feature Entry 的索引。Feature 索引是从零开始的值。</td></tr>
<tr><td>06h</td><td>2</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

**Table 8-108. Get Supported Features Output Payload | Get Supported Features 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Number of Supported Feature Entries: The number of Supported Feature Entries returned in the output payload.</td><td>Number of Supported Feature Entries:输出负载中返回的 Supported Feature Entries 数量。</td></tr>
<tr><td>02h</td><td>2</td><td>Device Supported Features: The number of supported Features.</td><td>Device Supported Features:受支持 Feature 的数量。</td></tr>
<tr><td>04h</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Supported Feature Entries: Device-specific list of supported feature identifier UUIDs and general information about each feature (see Table 8-109).</td><td>Supported Feature Entries:受支持 Feature 标识符 UUID 的设备特定列表以及有关每个 Feature 的一般信息(参见表 8-109)。</td></tr>
</tbody>
</table>

**Table 8-109. Get Supported Features Supported Feature Entry | Get Supported Features Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier: UUID that represents the feature for which to retrieve data.</td><td>Feature Identifier:表示要检索数据的 Feature 的 UUID。</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index: A zero-based value that is used to uniquely identify the feature. The Feature Index shall be less than the Device Supported Features value.</td><td>Feature Index:用于唯一标识 Feature 的从零开始的值。Feature Index 应小于 Device Supported Features 值。</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size: The maximum number of bytes that are required to retrieve this Feature data through the Get Feature command(s).</td><td>Get Feature Size:通过 Get Feature 命令检索此 Feature 数据所需的最大字节数。</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size: The maximum number of bytes that are required to update this Feature data through the Set Feature command(s). This field shall have a value of 0 if this Feature cannot be changed.</td><td>Set Feature Size:通过 Set Feature 命令更新此 Feature 数据所需的最大字节数。如果此 Feature 不能更改,则此字段的值为 0。</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags<br>• Bit[0]: Changeable: If set to 1, the Feature attribute(s) can be changed.<br>• Bits[3:1]: Deepest Reset Persistence: 000b = None; 001b = CXL reset; 010b = Hot reset; 011b = Warm reset; 100b = Cold reset; All other encodings are reserved.<br>• Bit[4]: Persist across Firmware Update: If set to 1, the current value of Feature attribute(s) persist across a firmware update.<br>• Bit[5]: Default Selection Supported<br>• Bit[6]: Saved Selection Supported<br>• Bits[31:7]: Reserved</td><td>Attribute Flags(属性标志)<br>• Bit[0]:Changeable:如果设置为 1,则 Feature 属性可以更改。<br>• Bits[3:1]:Deepest Reset Persistence:000b = None;001b = CXL reset;010b = Hot reset;011b = Warm reset;100b = Cold reset;所有其他编码保留。<br>• Bit[4]:Persist across Firmware Update:如果设置为 1,则 Feature 属性的当前值在固件更新后保留。<br>• Bit[5]:Default Selection Supported<br>• Bit[6]:Saved Selection Supported<br>• Bits[31:7]:保留</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>Get Feature Version</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>Set Feature Version</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects: Bitmask that contains one or more effects for the Set Feature. See the Command Effect field of the CEL Entry Structure in Table 8-87. This field shall have a value of 0 if the Feature cannot be changed.</td><td>Set Feature Effects:包含 Set Feature 的一个或多个效果的位掩码。请参阅表 8-87 中 CEL Entry Structure 的 Command Effect 字段。如果 Feature 不能更改,则此字段的值为 0。</td></tr>
<tr><td>1Eh</td><td>18</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Supported Features (page 693) ｜ Get Supported Features
>
> <img src="figures/chapter_08/page_0693.png" alt="Figure 8-X page 693" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0693.png)

**Table 8-110. Feature Attribute(s) Value after Reset | 复位后 Feature 属性值**

<table>
<thead>
<tr><th>Reset Event</th><th>0h: None</th><th>1h: CXL Reset</th><th>2h: Hot Reset</th><th>3h: Warm Reset</th><th>4h: Cold Reset</th></tr>
</thead>
<tbody>
<tr><td>CXL Reset</td><td>Default Value</td><td>Saved Value</td><td>Current Value</td><td>Current Value</td><td>Current Value</td></tr>
<tr><td>Hot Reset</td><td>Default Value</td><td>Saved Value</td><td>Saved Value</td><td>Current Value</td><td>Current Value</td></tr>
<tr><td>Warm Reset</td><td>Default Value</td><td>Saved Value</td><td>Saved Value</td><td>Saved Value</td><td>Current Value</td></tr>
<tr><td>Cold Reset</td><td>Default Value</td><td>Saved Value</td><td>Saved Value</td><td>Saved Value</td><td>Saved Value</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Default Value: The value set by the vendor when the device is shipped and cannot be changed by the host. If Saved Selection supported flag is 0, the Default Value is the Feature Current Value after reset.</td><td style="background-color:#e8e8e8">Default Value:设备出厂时由厂商设置的值,主机无法更改。如果 Saved Selection supported 标志为 0,则 Default Value 是复位后 Feature 的 Current Value。</td></tr>
<tr><td>Current Value: The current value of Feature attribute(s). If some of Feature attributes are writable, the value used by the device is the current attribute value which may be different than the Default Value or the Saved Value.</td><td style="background-color:#e8e8e8">Current Value:Feature 属性的当前值。如果某些 Feature 属性是可写的,则设备使用的值是当前属性值,该值可能与 Default Value 或 Saved Value 不同。</td></tr>
<tr><td>Saved Value: The value set after reset when Saved Selection Supported is 1. Saved Value shall be equal to Default Value when the device is shipped.</td><td style="background-color:#e8e8e8">Saved Value:当 Saved Selection Supported 为 1 时,复位后设置的值。设备出厂时,Saved Value 应等于 Default Value。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Feature Attribute(s) Value after Reset (page 694) ｜ 复位后 Feature 属性值
>
> <img src="figures/chapter_08/page_0694.png" alt="Figure 8-X page 694" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0694.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-2"></a>
### 8.2.10.6.2 Get Feature (Opcode 0501h) | 获取特性 (操作码 0501h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve the attributes of the Feature identified by a specific UUID. The caller discovers the size of the Feature first using the Get Supported Features command. The Get Feature command returns the bytes specified in the input payload by the Count payload field and starting from the Offset payload field. The Device shall return Invalid Input if the Offset payload field is beyond the maximum size of the Feature as reported by Get Supported Features. If the Offset is less than the maximum size of the Feature and the sum of Offset and Count is greater than the maximum size of the Feature, the Device shall return the data from Offset to the maximum size of the Feature.</td><td style="background-color:#e8e8e8">检索由特定 UUID 标识的 Feature 的属性。调用者首先使用 Get Supported Features 命令发现 Feature 的大小。Get Feature 命令从 Offset 负载字段开始,返回输入负载中 Count 负载字段指定的字节。如果 Offset 负载字段超出 Get Supported Features 所报告的 Feature 最大大小,设备应返回 Invalid Input。如果 Offset 小于 Feature 的最大大小,并且 Offset 和 Count 之和大于 Feature 的最大大小,则设备应返回从 Offset 到 Feature 最大大小的数据。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Unsupported Feature Selection Value<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Unsupported Feature Selection Value(不支持的 Feature 选择值)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-111. Get Feature Input Payload | Get Feature 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier: UUID representing the Feature identifier for which data is being retrieved.</td><td>Feature Identifier:表示正在检索其数据的 Feature 标识符的 UUID。</td></tr>
<tr><td>10h</td><td>2</td><td>Offset: The offset of the first byte in the Feature data to return in the output payload.</td><td>Offset:输出负载中要返回的 Feature 数据的第一个字节的偏移量。</td></tr>
<tr><td>12h</td><td>2</td><td>Count: Count in bytes of the Feature data to return in the output payload.</td><td>Count:输出负载中要返回的 Feature 数据的字节数。</td></tr>
<tr><td>14h</td><td>1</td><td>Selection: Specifies which value of the Feature to return in the output payload.<br>• 0h = Current value<br>• 1h = Default value<br>• 2h = Saved value<br>• All other encodings are reserved</td><td>Selection:指定输出负载中要返回的 Feature 的值。<br>• 0h = Current value(当前值)<br>• 1h = Default value(默认值)<br>• 2h = Saved value(保存值)<br>• 所有其他编码保留</td></tr>
</tbody>
</table>

**Table 8-112. Get Feature Output Payload | Get Feature 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>Varies</td><td>Feature Data</td><td>Feature Data(特性数据)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Feature (page 695) ｜ Get Feature
>
> <img src="figures/chapter_08/page_0695.png" alt="Figure 8-X page 695" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0695.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-3"></a>
### 8.2.10.6.3 Set Feature (Opcode 0502h) | 设置特性 (操作码 0502h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Update the attribute(s) of the Feature identified by a specific UUID. The caller may retrieve the Set Feature Size of the Feature by using the Get Supported Features command. One or more Set Feature commands may be required to transfer all the Feature data, incrementing the Feature Offset each time. The Device shall return Invalid Input if the Offset attempts to access beyond the Set Feature Size of the Feature as reported by Get Supported Features or the sum of Offset and Feature Data size exceeds the Set Feature Size of the Feature as reported by Get Supported Features.</td><td style="background-color:#e8e8e8">更新由特定 UUID 标识的 Feature 的属性。调用者可以使用 Get Supported Features 命令检索 Feature 的 Set Feature Size。可能需要一个或多个 Set Feature 命令来传输所有 Feature 数据,每次递增 Feature Offset。如果 Offset 尝试访问超出 Get Supported Features 所报告的 Feature 的 Set Feature Size 的范围,或 Offset 和 Feature Data 大小之和超出 Get Supported Features 所报告的 Feature 的 Set Feature Size,则设备应返回 Invalid Input。</td></tr>
<tr><td>If the Feature data is transferred in its entirety, the caller makes one call to Set Feature with Action = Full Data Transfer. The Offset field is not used and shall be ignored.</td><td style="background-color:#e8e8e8">如果 Feature 数据是整体传输的,调用者使用 Action = Full Data Transfer 调用一次 Set Feature。Offset 字段不使用,应被忽略。</td></tr>
<tr><td>If a Feature data is transferred in parts, the caller makes one call to Set Feature with Action = Initiate Data Transfer, zero or more calls with Action = Continue Data Transfer, and one call with Action = Finish Data Transfer or Abort Data Transfer. The Feature data parts shall be transferred in ascending order based on the Offset value, and the Device shall return the Feature Transfer Out of Order return code if data parts are not transferred in ascending order. Back-to-back retransmission of any Set Feature data is permitted during a transfer. The Saved across Reset flag is valid for Set Feature command with Action = Initiate Data Transfer or Action = Full Data Transfer and shall be ignored for all other Action values. A Set Feature with Action = Abort Data Transfer shall be supported for Feature data that can be transferred using multiple Set Feature commands. An attempt to call Set Feature with Action = Abort Data Transfer for a Feature whose data has been fully transferred shall fail with Invalid Input.</td><td style="background-color:#e8e8e8">如果 Feature 数据是分部分传输的,调用者使用 Action = Initiate Data Transfer 调用一次 Set Feature,使用 Action = Continue Data Transfer 调用零次或多次,并使用 Action = Finish Data Transfer 或 Abort Data Transfer 调用一次。Feature 数据部分应基于 Offset 值按升序传输,如果数据部分未按升序传输,设备应返回 Feature Transfer Out of Order 返回码。在传输期间,允许对任何 Set Feature 数据进行背靠背重新传输。Saved across Reset 标志对 Action = Initiate Data Transfer 或 Action = Full Data Transfer 的 Set Feature 命令有效,对所有其他 Action 值应忽略。对于可以使用多个 Set Feature 命令传输的 Feature 数据,应支持 Action = Abort Data Transfer 的 Set Feature。对于数据已完全传输的 Feature 尝试调用 Action = Abort Data Transfer 的 Set Feature 应返回 Invalid Input 失败。</td></tr>
<tr><td>Only one Feature may be updated at a time in the device. The device shall return the Feature Transfer in Progress return code if it receives a Set Feature command with Action = Full Data Transfer or Action = Initiate Data Transfer until the current Feature data transfer is completed or aborted.</td><td style="background-color:#e8e8e8">设备一次只能更新一个 Feature。如果设备收到 Action = Full Data Transfer 或 Action = Initiate Data Transfer 的 Set Feature 命令,直到当前 Feature 数据传输完成或中止,设备应返回 Feature Transfer in Progress 返回码。</td></tr>
<tr><td>If the Feature data transfer is interrupted by a Conventional or CXL reset, the Feature data transfer shall be aborted by the device. If a Feature data transfer is aborted prior to the entire Feature data being transferred, the device shall require the Feature data transfer to be started from the beginning of the Feature data.</td><td style="background-color:#e8e8e8">如果 Feature 数据传输被 Conventional 或 CXL reset 中断,设备应中止 Feature 数据传输。如果在传输整个 Feature 数据之前中止了 Feature 数据传输,设备应要求从 Feature 数据开头重新开始 Feature 数据传输。</td></tr>
<tr><td>Once the entire Feature data is fully transferred to the device (i.e., Action = Full Data Transfer or Action = Finish Data Transfer), the device shall update the attribute(s) of the Feature.</td><td style="background-color:#e8e8e8">一旦整个 Feature 数据完全传输到设备(即 Action = Full Data Transfer 或 Action = Finish Data Transfer),设备应更新 Feature 的属性。</td></tr>
<tr><td>The Command Effects Log (CEL) entry for Set Feature shall describe all possible command effects (i.e., Bits 0 to 5) from supported Features that are changeable.</td><td style="background-color:#e8e8e8">Set Feature 的 Command Effects Log (CEL) 条目应描述可更改的受支持 Feature 的所有可能命令效果(即,Bit 0 到 Bit 5)。</td></tr>
<tr><td>If a component receives an input payload that is less than the size of the structure it has implemented, but is greater than or equal to the Minimum Feature Data Size (as specified in the Feature definition), then it shall treat the unsent portion of the structure as 0. For each feature, any fields in the feature data that are not included in the calculation of the Minimum Feature Data Size are explicitly identified. For features where no fields are identified, all the fields in the feature data are to be included in the calculation of the Minimum Feature Data Size.</td><td style="background-color:#e8e8e8">如果组件收到的输入负载小于其实现的结构大小,但大于或等于 Minimum Feature Data Size(如 Feature 定义中指定),则应将结构的未发送部分视为 0。对于每个 Feature,任何未包含在 Minimum Feature Data Size 计算中的 Feature 数据字段都会被明确标识。对于未标识任何字段的 Feature,Feature 数据中的所有字段都应包含在 Minimum Feature Data Size 的计算中。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to alter the features of the locked device by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何更改已锁定设备 Feature 的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Unsupported Feature Version<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Feature Transfer in Progress<br>• Feature Transfer Out of Order<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Unsupported Feature Version(不支持的 Feature 版本)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Feature Transfer in Progress(Feature 传输进行中)<br>• Feature Transfer Out of Order(Feature 传输乱序)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Configuration Change after Cold Reset<br>• Configuration Change after Conventional Reset<br>• Configuration Change after CXL Reset<br>• Immediate Configuration Change<br>• Immediate Data Change<br>• Immediate Policy Change<br>• Immediate Log Change<br>• Security State Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Cold Reset 后的配置更改<br>• Conventional Reset 后的配置更改<br>• CXL Reset 后的配置更改<br>• 立即配置更改<br>• 立即数据更改<br>• 立即策略更改<br>• 立即日志更改<br>• 安全状态更改</td></tr>
</tbody>
</table>

**Table 8-113. Set Feature Input Payload | Set Feature 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier: UUID representing the Feature identifier for which data is being updated. The UUID value of all Fs is a special value that represents the current Feature whose data is in the process of being transferred.</td><td>Feature Identifier:表示正在更新其数据的 Feature 标识符的 UUID。全 F 的 UUID 值是特殊值,表示正在传输其数据的当前 Feature。</td></tr>
<tr><td>10h</td><td>4</td><td>Set Feature Flags<br>• Bits[2:0]: Action: 000b = Full Data Transfer; 001b = Initiate Data Transfer; 010b = Continue Data Transfer; 011b = Finish Data Transfer; 100b = Abort Data Transfer; All other encodings are reserved<br>• Bit[3]: Saved across Reset: If set to 1, the modified value is saved across the Deepest Reset Persistence value for the Feature<br>• Bits[31:4]: Reserved</td><td>Set Feature Flags(设置特性标志)<br>• Bits[2:0]:Action:000b = Full Data Transfer;001b = Initiate Data Transfer;010b = Continue Data Transfer;011b = Finish Data Transfer;100b = Abort Data Transfer;所有其他编码保留<br>• Bit[3]:Saved across Reset:如果设置为 1,则修改后的值在 Feature 的 Deepest Reset Persistence 值范围内保留<br>• Bits[31:4]:保留</td></tr>
<tr><td>14h</td><td>2</td><td>Offset: The byte offset of the Feature data to update.</td><td>Offset:要更新的 Feature 数据的字节偏移量。</td></tr>
<tr><td>16h</td><td>1</td><td>Version: Feature version of the data in Feature Data.</td><td>Version:Feature Data 中数据的 Feature 版本。</td></tr>
<tr><td>17h</td><td>9</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>Varies</td><td>Feature Data</td><td>Feature Data(特性数据)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Set Feature (page 697) ｜ Set Feature
>
> <img src="figures/chapter_08/page_0697.png" alt="Figure 8-X page 697" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0697.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-6-4"></a>
### 8.2.10.6.4 Metabits Storage Feature Discovery and Configuration | Metabits 存储特性发现和配置

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Feature Identifier of this feature is: 3568da82-e69c-4518-95a2-446fe34ea865.</td><td style="background-color:#e8e8e8">此特性的 Feature Identifier 是:3568da82-e69c-4518-95a2-446fe34ea865。</td></tr>
<tr><td>This feature allows the host to discover and configure the support for storage of Metadata Value bits and TE State in the CXL device's HDM-H address region. It is not applicable to HDM-DB address region. This Feature is not applicable when TE State granularity is bigger than 64B.</td><td style="background-color:#e8e8e8">此特性允许主机发现和配置 CXL 设备的 HDM-H 地址区域中 Metadata Value 位和 TE State 的存储支持。它不适用于 HDM-DB 地址区域。当 TE State 粒度大于 64B 时,此特性不适用。</td></tr>
<tr><td>Table 8-114 shows the information returned in the Get Supported Features output payload for the Metabits Storage Feature. Some feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-114 显示了 Metabits Storage Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
<tr><td>Any changes to HDM-H Metabits Storage Configuration require a Conventional reset to take effect. Saved across Reset bit in Set Feature Input Payload shall be set to 1, otherwise the device shall return Invalid Input. Changes to HDM-H Metabits Storage Configuration may result in changes to the device capacity and CDAT.</td><td style="background-color:#e8e8e8">对 HDM-H Metabits Storage Configuration 的任何更改都需要 Conventional reset 才能生效。Set Feature Input Payload 中的 Saved across Reset 位应设置为 1,否则设备应返回 Invalid Input。对 HDM-H Metabits Storage Configuration 的更改可能会导致设备容量和 CDAT 的更改。</td></tr>
<tr><td>An SH-MLD, MH-MLD or MH-SLD that support this feature shall report Set Feature Size=0 and Bit[0] of Attribute Flags Bit[0] = 0, over CCI exposed to individual hosts indicating that the Feature Data cannot be modified over these CCI.</td><td style="background-color:#e8e8e8">支持此特性的 SH-MLD、MH-MLD 或 MH-SLD 应在暴露给各个主机的 CCI 上报告 Set Feature Size=0 和 Attribute Flags Bit[0] 的 Bit[0] = 0,表示不能通过这些 CCI 修改 Feature Data。</td></tr>
</tbody>
</table>

**Table 8-114. Supported Feature Entry for Metabits Storage Feature | Metabits Storage Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte offset</th><th>Length in Bytes</th><th>Attribute</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>3568da82-e69c-4518-95a2-446fe34ea865</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device Specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>3 Bytes</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>1 Bytes</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 010b (Deepest Reset Persistence = Hot Reset). Conventional reset will restore the saved value.<br>• Bit[4]: 1 (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: 1 (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>01h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>01h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 1 (Configuration Change after Cold Reset)<br>• Bit[1]: 0 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log Change)<br>• Bit[5]: Vendor-specific value (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 (CEL[11:10] Valid)<br>• Bit[10]: 1 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>18</td><td>Reserved</td><td>•</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An SH-MLD, MH-MLD or MH-SLD that support this feature shall report Set Feature Size=1 and Bit[0] of Attribute Flags Bit[0] = 1, over CCI exposed to the FM indicating that the Feature Data can be modified over these CCI.</td><td style="background-color:#e8e8e8">支持此特性的 SH-MLD、MH-MLD 或 MH-SLD 应在暴露给 FM 的 CCI 上报告 Set Feature Size=1 和 Attribute Flags Bit[0] 的 Bit[0] = 1,表示可以通过这些 CCI 修改 Feature Data。</td></tr>
<tr><td>After a successful CXL reset, a Conventional Reset or a successful Secure Erase operation, a subsequent read to any device cacheline (DPA) shall return Metafield=00b (Meta0-State abbreviation MS0) and MetaValue=00b, if the device is configured with non-zero Metadata bits via this Feature. As per Section 12.2.3, a device must set the MetaField to No-Op in the CXL.cachemem return response when the Metadata is suspect.</td><td style="background-color:#e8e8e8">在成功的 CXL reset、Conventional Reset 或成功的 Secure Erase 操作之后,如果设备通过此特性配置了非零 Metadata 位,则对任何设备 cacheline (DPA) 的后续读取应返回 Metafield=00b(Meta0-State 缩写 MS0)和 MetaValue=00b。根据 12.2.3 节,当 Metadata 不可信时,设备必须在 CXL.cachemem 返回响应中将 MetaField 设置为 No-Op。</td></tr>
</tbody>
</table>

**Table 8-115. Metabits Storage Feature Readable Attributes | Metabits Storage Feature 可读属性**

<table>
<thead>
<tr><th>Byte offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>HDM-H Metabits Storage Capabilities<br>• Bit[0]: 2 bits of Metadata are supported. 2 bits of storage supported.<br>• Bit[1]: No Metadata is supported. No storage supported.<br>• Bit[2]: 1-bit of Metadata is supported. bit-0 of Meta0-State Value will be stored. One bit of storage supported.<br>• Bit[3]: 1-bit of Metadata is supported. bit-1 of Meta0-State Value will be stored. One bit of storage supported.<br>• Bit[4]: 2 bits of Metadata + 1 TE State bit are supported. Three bits of storage supported.<br>• Bit[5]: No Metadata + 1 TE State bit is supported. One bit of storage supported.<br>• Bit[6]: 1-bit of Metadata + 1 TE State bit are supported. bit-0 of Meta0-State Value will be stored. Two bits of storage supported.<br>• Bit[7]: 1-bit of Metadata + 1 TE State bit are supported. bit-1 of Meta0-State Value will be stored. Two bits of storage supported.<br>• Bits[15:8]: Reserved</td><td>HDM-H Metabits Storage Capabilities(HDM-H Metabits 存储能力)<br>• Bit[0]:支持 2 位 Metadata。支持 2 位存储。<br>• Bit[1]:不支持 Metadata。不支持存储。<br>• Bit[2]:支持 1 位 Metadata。将存储 Meta0-State Value 的 bit-0。支持 1 位存储。<br>• Bit[3]:支持 1 位 Metadata。将存储 Meta0-State Value 的 bit-1。支持 1 位存储。<br>• Bit[4]:支持 2 位 Metadata + 1 TE State 位。支持 3 位存储。<br>• Bit[5]:不支持 Metadata + 1 TE State 位。支持 1 位存储。<br>• Bit[6]:支持 1 位 Metadata + 1 TE State 位。将存储 Meta0-State Value 的 bit-0。支持 2 位存储。<br>• Bit[7]:支持 1 位 Metadata + 1 TE State 位。将存储 Meta0-State Value 的 bit-1。支持 2 位存储。<br>• Bits[15:8]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>HDM-H Metabits Storage Configuration<br>• 0h: 2 bits of Metadata<br>• 1h: No Metadata<br>• 2h: 1 bit of Metadata, bit-0 of Meta0-State Value<br>• 3h: 1 bit of Metadata, bit-1 of Meta0-State Value<br>• 4h: 2 bits of Metadata + 1 TE State bit<br>• 5h: No Metadata + 1 TE State bit<br>• 6h: 1 bit of Metadata, bit-0 of Meta0-State Value + 1 TE State bit<br>• 7h: 1 bit of Metadata, bit-1 of Meta0-State Value + 1 TE State bit<br>• Bits[7:3]: Reserved</td><td>HDM-H Metabits Storage Configuration(HDM-H Metabits 存储配置)<br>• 0h:2 位 Metadata<br>• 1h:无 Metadata<br>• 2h:1 位 Metadata,Meta0-State Value 的 bit-0<br>• 3h:1 位 Metadata,Meta0-State Value 的 bit-1<br>• 4h:2 位 Metadata + 1 TE State 位<br>• 5h:无 Metadata + 1 TE State 位<br>• 6h:1 位 Metadata,Meta0-State Value 的 bit-0 + 1 TE State 位<br>• 7h:1 位 Metadata,Meta0-State Value 的 bit-1 + 1 TE State 位<br>• Bits[7:3]:保留</td></tr>
</tbody>
</table>

**Table 8-116. Metabits Storage Feature Writable Attributes | Metabits Storage Feature 可写属性**

<table>
<thead>
<tr><th>Byte offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>1</td><td>HDM-H Metabits Storage Configuration (Values as defined in Table 8-115)</td><td>HDM-H Metabits Storage Configuration(值如表 8-115 所定义)</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Table 8-115 shows the output payload returned by a Get Feature command with Selection set to 0h (Current value), 1h (Default value) or 2h (Saved Value).</td><td style="background-color:#e8e8e8">表 8-115 显示了 Selection 设置为 0h(Current value)、1h(Default value)或 2h(Saved Value)的 Get Feature 命令返回的输出负载。</td></tr>
<tr><td>Table 8-116 shows the input payload for Set Feature command.</td><td style="background-color:#e8e8e8">表 8-116 显示了 Set Feature 命令的输入负载。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Metabits Storage Feature (page 698-699) ｜ Metabits Storage Feature
>
> <img src="figures/chapter_08/page_0698.png" alt="Figure 8-X page 698" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0698.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7"></a>
## 8.2.10.7 Maintenance | 维护

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1"></a>
### 8.2.10.7.1 Perform Maintenance (Opcode 0600h) | 执行维护 (操作码 0600h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command requests the device to execute the maintenance operation specified by the Maintenance Operation Class and the Maintenance Operation Subclass. If the operation is not supported, the command shall be terminated with Invalid Input Return Code.</td><td style="background-color:#e8e8e8">此命令请求设备执行由 Maintenance Operation Class 和 Maintenance Operation Subclass 指定的维护操作。如果不支持该操作,命令应以 Invalid Input Return Code 终止。</td></tr>
<tr><td>The Perform Maintenance command may be performed in the foreground or in the background, based on the characteristics of the maintenance operation. When the device is executing a Perform Maintenance command in the background, it may indicate operation progress using the Background Command Status register.</td><td style="background-color:#e8e8e8">根据维护操作的特征,Perform Maintenance 命令可以在前台或后台执行。当设备在后台执行 Perform Maintenance 命令时,它可以使用 Background Command Status 寄存器指示操作进度。</td></tr>
<tr><td>No more than one maintenance operation may be initiated at a time.</td><td style="background-color:#e8e8e8">一次最多只能启动一个维护操作。</td></tr>
</tbody>
</table>

**Table 8-117. Perform Maintenance Input Payload | Perform Maintenance 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: This field identifies the Class of a maintenance operation. See Table 8-125.</td><td>Maintenance Operation Class(维护操作类):此字段标识维护操作的类。参见表 8-125。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: This field identifies the maintenance operation together with the Maintenance Operation Class. See Table 8-125.</td><td>Maintenance Operation Subclass(维护操作子类):此字段与 Maintenance Operation Class 一起标识维护操作。参见表 8-125。</td></tr>
<tr><td>02h</td><td>Varies</td><td>Maintenance operation parameters.</td><td>维护操作参数。</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The device shall terminate a foreground or background Perform Maintenance command with Busy Return Code if it is already processing a maintenance operation in the background.</td><td style="background-color:#e8e8e8">如果设备已经在后台处理维护操作,则应使用 Busy Return Code 终止前台或后台的 Perform Maintenance 命令。</td></tr>
<tr><td>Some restrictions may apply during the execution of a maintenance operation. For example, it might not be possible to read or write a CXL memory device. These restrictions are specified in the description of the maintenance operation and there can be Feature attributes that indicate device capabilities.</td><td style="background-color:#e8e8e8">在维护操作执行期间,可能适用某些限制。例如,可能无法读取或写入 CXL memory device。这些限制在维护操作的描述中指定,并且可能存在指示设备能力的 Feature 属性。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to perform maintenance PPR, sPPR, hPPR, built-in self-tests, and/or other maintenance operations that might alter the data and/or TE State on the device, affect the devices ability to maintain data coherency, and/or compromise the link's integrity by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何执行维护 PPR、sPPR、hPPR、内置自检和/或其他可能更改设备上的数据和/或 TE State、影响设备维持数据一致性的能力和/或损害链路完整性的维护操作的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Background Command Started<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Busy<br>• Transfer Out of Order<br>• Aborted<br>• Invalid Physical Address<br>• Resources Exhausted<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Background Command Started(后台命令已启动)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Busy(忙)<br>• Transfer Out of Order(传输乱序)<br>• Aborted(中止)<br>• Invalid Physical Address(无效物理地址)<br>• Resources Exhausted(资源耗尽)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Configuration Change if a maintenance operation restricts the operations that a host can do<br>• Immediate Data Change if a maintenance operation impacts the data written to the device<br>• Immediate Log Change if a maintenance operation impacts a device log<br>• Background Operation if a maintenance operation is executed in background<br>• Request Abort Background Operation Command Supported</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Configuration Change(立即配置更改)(如果维护操作限制了主机可以执行的操作)<br>• Immediate Data Change(立即数据更改)(如果维护操作影响写入设备的数据)<br>• Immediate Log Change(立即日志更改)(如果维护操作影响设备日志)<br>• Background Operation(后台操作)(如果维护操作在后台执行)<br>• Request Abort Background Operation Command Supported(支持请求中止后台操作命令)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Perform Maintenance (page 700-701) ｜ Perform Maintenance
>
> <img src="figures/chapter_08/page_0700.png" alt="Figure 8-X page 700" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0700.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-1"></a>
#### 8.2.10.7.1.1 PPR Maintenance Operations | PPR 维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Post Package Repair (PPR) maintenance operations may be supported by CXL devices that implement CXL.mem protocol. A PPR maintenance operation requests the CXL device to perform a repair operation on its media.</td><td style="background-color:#e8e8e8">Post Package Repair (PPR) 维护操作可以由实现 CXL.mem 协议的 CXL 设备支持。PPR 维护操作请求 CXL 设备对其介质执行修复操作。</td></tr>
<tr><td>For example, a CXL device with DRAM components that support PPR features may implement PPR Maintenance operations. DRAM components may support two types of PPR: Hard PPR (hPPR), for a permanent row repair, and Soft PPR (sPPR), for a temporary row repair. sPPR is much faster than hPPR, but the repair is lost with a power cycle.</td><td style="background-color:#e8e8e8">例如,具有支持 PPR 功能的 DRAM 组件的 CXL 设备可以实现 PPR 维护操作。DRAM 组件可以支持两种类型的 PPR:Hard PPR (hPPR),用于永久行修复,以及 Soft PPR (sPPR),用于临时行修复。sPPR 比 hPPR 快得多,但修复会在电源循环后丢失。</td></tr>
<tr><td>Based on DRAM PPR features, two maintenance operations are defined: sPPR and hPPR. Note that PPR maintenance operations may also apply to other types of media component.</td><td style="background-color:#e8e8e8">基于 DRAM PPR 功能,定义了两个维护操作:sPPR 和 hPPR。请注意,PPR 维护操作也可能适用于其他类型的介质组件。</td></tr>
<tr><td>During the execution of a PPR Maintenance operation, a CXL memory device:<br>• May or may not retain data<br>• May or may not be able to process CXL.mem requests correctly, including the ones that target the DPA involved in the repair</td><td style="background-color:#e8e8e8">在执行 PPR 维护操作期间,CXL memory device:<br>• 可能保留数据,也可能不保留数据<br>• 可能能够正确处理 CXL.mem 请求,也可能不能,包括针对修复涉及的 DPA 的请求</td></tr>
<tr><td>If the device is not capable of correctly processing a CXL.mem request during a PPR Maintenance operation, then:<br>• A read shall return poison<br>• A write shall be dropped, and an NDR shall be sent<br>• Any subsequent reads of DPA for which writes may have been incorrectly processed shall return poison</td><td style="background-color:#e8e8e8">如果设备在 PPR 维护操作期间无法正确处理 CXL.mem 请求,则:<br>• 读取应返回 poison<br>• 写入应被丢弃,并发送 NDR<br>• 对于写入可能被错误处理的 DPA 的任何后续读取应返回 poison</td></tr>
<tr><td>These CXL Memory Device capabilities are specified by Restriction Flags in the sPPR Feature and hPPR Feature (see Section 8.2.10.7.2.1 and Section 8.2.10.7.2.2, respectively).</td><td style="background-color:#e8e8e8">这些 CXL Memory Device 能力由 sPPR Feature 和 hPPR Feature 中的 Restriction Flags 指定(分别参见 8.2.10.7.2.1 节和 8.2.10.7.2.2 节)。</td></tr>
<tr><td>sPPR maintenance operation may be executed at runtime, if data is retained and CXL.mem requests are correctly processed. For CXL devices with DRAM components, hPPR maintenance operation may be executed only at boot because data would not be retained.</td><td style="background-color:#e8e8e8">如果保留了数据并正确处理 CXL.mem 请求,则可以在运行时执行 sPPR 维护操作。对于具有 DRAM 组件的 CXL 设备,hPPR 维护操作只能在启动时执行,因为数据将不会被保留。</td></tr>
<tr><td>When a CXL device identifies a failure on a memory component, the device may inform the host about the need for a PPR maintenance operation by using an Event Record, where the Maintenance Needed flag is set. The Event Record specifies the DPA that should be repaired. A CXL device may not keep track of the requests that have already been sent and the information on which DPA should be repaired may be lost upon power cycle.</td><td style="background-color:#e8e8e8">当 CXL 设备识别内存组件上的故障时,设备可以通过使用 Event Record 通知主机需要执行 PPR 维护操作,其中 Maintenance Needed 标志被设置。Event Record 指定应修复的 DPA。CXL 设备可能不跟踪已发送的请求,并且有关应修复哪个 DPA 的信息可能在电源循环后丢失。</td></tr>
<tr><td>The Host or the FM may or may not initiate a PPR Maintenance operation in response to a device request. It is possible to check whether resources are available by issuing a Perform Maintenance command for the PPR maintenance operation with the Query Resources flag set to 1. If the controller does not support reporting whether a resource is available, and a Perform Maintenance operation for PPR is issued with Query Resources set to 1, the controller shall return Invalid Input.</td><td style="background-color:#e8e8e8">主机或 FM 可以根据设备请求启动 PPR 维护操作,也可以不启动。可以通过发出 Query Resources 标志设置为 1 的 PPR 维护操作的 Perform Maintenance 命令来检查资源是否可用。如果控制器不支持报告资源是否可用,并且发出了 Query Resources 设置为 1 的 PPR 的 Perform Maintenance 操作,则控制器应返回 Invalid Input。</td></tr>
<tr><td>If resources are available, then the command shall be completed with the Success Return Code; otherwise, the command shall be completed with the Resources exhausted Return Code.</td><td style="background-color:#e8e8e8">如果资源可用,则命令应以 Success Return Code 完成;否则,命令应以 Resources exhausted Return Code 完成。</td></tr>
<tr><td>The host or the FM may initiate a repair operation by issuing a Perform Maintenance command, setting the Maintenance Operation Class to 01h (PPR), the Maintenance Operation Subclass to either 00h (sPPR) or 01h (hPPR), and indicating the DPA (if supported).</td><td style="background-color:#e8e8e8">主机或 FM 可以通过发出 Perform Maintenance 命令启动修复操作,将 Maintenance Operation Class 设置为 01h (PPR),将 Maintenance Operation Subclass 设置为 00h (sPPR) 或 01h (hPPR),并指示 DPA(如果支持)。</td></tr>
<tr><td>During the execution of a PPR maintenance operation, the device operation may be restricted as indicated by the Restriction Flags in the sPPR Feature and hPPR Feature (see Section 8.2.10.7.2.1 and Section 8.2.10.7.2.2, respectively).</td><td style="background-color:#e8e8e8">在 PPR 维护操作执行期间,设备操作可能受到 sPPR Feature 和 hPPR Feature 中的 Restriction Flags 指示的限制(分别参见 8.2.10.7.2.1 节和 8.2.10.7.2.2 节)。</td></tr>
<tr><td>Upon completion of a PPR maintenance operation, the device shall produce a Memory Sparing Event Record with updated resource availability, if the Memory Sparing Event Record Enable bit is set (see Table 8-128 or Table 8-131).</td><td style="background-color:#e8e8e8">完成 PPR 维护操作后,如果设置了 Memory Sparing Event Record Enable 位(参见表 8-128 或表 8-131),设备应生成一个具有更新资源可用性的 Memory Sparing Event Record。</td></tr>
</tbody>
</table>

> **Figure 8-X.** PPR Maintenance Operations (page 701-702) ｜ PPR 维护操作
>
> <img src="figures/chapter_08/page_0701.png" alt="Figure 8-X page 701" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0701.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-2"></a>
#### 8.2.10.7.1.2 sPPR Maintenance Operation | sPPR 维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This maintenance operation requests the device to perform an sPPR operation. The sPPR Feature provides parameters and configurations related to this operation. See Section 8.2.10.7.2.1. Table 8-118 shows the input payload for this maintenance operation.</td><td style="background-color:#e8e8e8">此维护操作请求设备执行 sPPR 操作。sPPR Feature 提供与此操作相关的参数和配置。参见 8.2.10.7.2.1 节。表 8-118 显示了此维护操作的输入负载。</td></tr>
</tbody>
</table>

**Table 8-118. sPPR Maintenance Input Payload | sPPR 维护输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h.</td><td>Maintenance Operation Class:应设置为 01h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: It shall be cleared to 00h.</td><td>Maintenance Operation Subclass:应清零为 00h。</td></tr>
<tr><td>02h</td><td>1</td><td>Flags<br>• Bit[0]: Query Resources Flag: If set, the CXL device checks whether resources are available to perform the sPPR maintenance operation but does not attempt to perform the operation<br>• Bits[7:1]: Reserved</td><td>标志位<br>• Bit[0]:Query Resources Flag:如果设置,CXL 设备检查是否有可用资源来执行 sPPR 维护操作,但不尝试执行该操作<br>• Bits[7:1]:保留</td></tr>
<tr><td>03h</td><td>8</td><td>DPA: Physical address to be repaired. This field is ignored if the DPA support flag in the sPPR Feature is cleared to 0 (see Table 8-128).</td><td>DPA:要修复的物理地址。如果 sPPR Feature 中的 DPA support 标志清零为 0(参见表 8-128),则此字段被忽略。</td></tr>
<tr><td>0Bh</td><td>3</td><td>Nibble Mask: Identifies one or more nibbles on the memory bus. A Nibble Mask bit set to 1 indicates the request to perform sPPR operation in the specific device. All Nibble Mask bits set to 1 indicates the request to perform the operation in all devices. This field is ignored if the Nibble support flag in the sPPR Feature is cleared to 0 (see Table 8-128), and the sPPR is performed in all devices.</td><td>Nibble Mask:标识内存总线上的一个或多个半字节。设置为 1 的 Nibble Mask 位表示在特定设备中执行 sPPR 操作的请求。全部 Nibble Mask 位设置为 1 表示在所有设备中执行操作的请求。如果 sPPR Feature 中的 Nibble support 标志清零为 0(参见表 8-128),并且 sPPR 在所有设备中执行,则此字段被忽略。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-3"></a>
#### 8.2.10.7.1.3 hPPR Maintenance Operation | hPPR 维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This maintenance operation requests the device to perform an hPPR operation. The hPPR Feature provides parameters and configurations related to this operation, see Section 8.2.10.7.2.2. Table 8-119 shows the input payload for this maintenance operation.</td><td style="background-color:#e8e8e8">此维护操作请求设备执行 hPPR 操作。hPPR Feature 提供与此操作相关的参数和配置,参见 8.2.10.7.2.2 节。表 8-119 显示了此维护操作的输入负载。</td></tr>
</tbody>
</table>

**Table 8-119. hPPR Maintenance Input Payload | hPPR 维护输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h.</td><td>Maintenance Operation Class:应设置为 01h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: It shall be set to 01h.</td><td>Maintenance Operation Subclass:应设置为 01h。</td></tr>
<tr><td>02h</td><td>1</td><td>Flags<br>• Bit[0]: Query Resources Flag: If set, the CXL device checks whether resources are available to perform the hPPR maintenance operation<br>• Bits[7:1]: Reserved</td><td>标志位<br>• Bit[0]:Query Resources Flag:如果设置,CXL 设备检查是否有可用资源来执行 hPPR 维护操作<br>• Bits[7:1]:保留</td></tr>
<tr><td>03h</td><td>8</td><td>DPA: Physical address to be repaired. This field is ignored if the DPA support flag bit in the hPPR Feature is cleared to 0 (see Table 8-131).</td><td>DPA:要修复的物理地址。如果 hPPR Feature 中的 DPA support 标志位清零为 0(参见表 8-131),则此字段被忽略。</td></tr>
<tr><td>0Bh</td><td>3</td><td>Nibble Mask: Identifies one or more nibbles on the memory bus.</td><td>Nibble Mask:标识内存总线上的一个或多个半字节。</td></tr>
</tbody>
</table>

> **Figure 8-X.** hPPR Maintenance Operation (page 703) ｜ hPPR 维护操作
>
> <img src="figures/chapter_08/page_0703.png" alt="Figure 8-X page 703" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0703.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-4"></a>
#### 8.2.10.7.1.4 Memory Sparing Maintenance Operations | 内存备用维护操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The associated Class and Subclasses are defined in Table 8-125.</td><td style="background-color:#e8e8e8">相关的 Class 和 Subclasses 在表 8-125 中定义。</td></tr>
<tr><td>Memory sparing is defined as a repair function that replaces a portion of memory (the "spared memory") with a portion of functional memory at that same DPA. The Subclasses for this operation vary in terms of the scope of the sparing being performed. The Cacheline sparing subclass refers to a sparing action that can replace a full cacheline. Row sparing is provided as an alternative to PPR sparing functions and its scope is that of a single DDR row. Bank sparing allows an entire bank to be replaced. Rank sparing is defined as an operation in which an entire DDR rank is replaced.</td><td style="background-color:#e8e8e8">内存备用定义为一种修复功能,用于将一部分内存("被备用的内存")替换为同一 DPA 上的功能性内存。此操作的子类根据所执行的备用范围而有所不同。Cacheline sparing 子类是指可以替换完整 cacheline 的备用操作。Row sparing 作为 PPR 备用功能的替代方案提供,其范围是单个 DDR 行。Bank sparing 允许替换整个 bank。Rank sparing 被定义为替换整个 DDR rank 的操作。</td></tr>
<tr><td>The Input Payload specifies the memory portion to be replaced. In particular, the Nibble Mask field in the Input Payload may be used to request sparing on specific components. The nibble mapping is the same as DRAM Event Record nibble mapping (see Table 8-58). Components are specified by setting the Nibble Mask Valid flag and the related Nibble Mask bits. The device may apply memory sparing to more components than requested. If the Nibble Mask Valid flag is 0, the memory sparing request is for all components.</td><td style="background-color:#e8e8e8">输入负载指定要替换的内存部分。特别是,输入负载中的 Nibble Mask 字段可用于请求对特定组件进行备用。半字节映射与 DRAM Event Record 半字节映射相同(参见表 8-58)。通过设置 Nibble Mask Valid 标志和相关的 Nibble Mask 位来指定组件。设备可以向比请求更多的组件应用内存备用。如果 Nibble Mask Valid 标志为 0,则内存备用请求针对所有组件。</td></tr>
<tr><td>If the host requests an operation Subclass for an address and the device is out of resources, the device shall respond with the Resources Exhausted return code.</td><td style="background-color:#e8e8e8">如果主机为地址请求操作子类,并且设备资源耗尽,则设备应以 Resources Exhausted 返回码响应。</td></tr>
<tr><td>The host may issue a query command by setting Query Resources flag in the Input Payload (see Table 8-120) to determine availability of sparing resources for a given address. In response to a query request, the device shall report the resource availability by producing the Memory Sparing Event Record (see Table 8-60) in which the Channel, Rank, Nibble Mask, Bank Group, Bank, Row, Column, Sub-Channel fields are a copy of the values specified in the request. If the controller does not support reporting whether a resource is available, and a Perform Maintenance operation for Memory Sparing is issued with Query Resources set to 1, the controller shall return Invalid Input.</td><td style="background-color:#e8e8e8">主机可以通过在输入负载中设置 Query Resources 标志(参见表 8-120)来发出查询命令,以确定给定地址的备用资源可用性。作为对查询请求的响应,设备应通过生成 Memory Sparing Event Record(参见表 8-60)来报告资源可用性,其中 Channel、Rank、Nibble Mask、Bank Group、Bank、Row、Column、Sub-Channel 字段是请求中指定值的副本。如果控制器不支持报告资源是否可用,并且发出了 Query Resources 设置为 1 的 Memory Sparing 的 Perform Maintenance 操作,则控制器应返回 Invalid Input。</td></tr>
<tr><td>All Memory Sparing operations shall be executed as background operations and are capable of being aborted by the Request Abort Background Operation command.</td><td style="background-color:#e8e8e8">所有 Memory Sparing 操作应作为后台操作执行,并且能够被 Request Abort Background Operation 命令中止。</td></tr>
<tr><td>Table 8-120 shows the input payload for this maintenance operation. The device shall communicate the operation's results by producing a Memory Sparing Event Record (see Table 8-60) in response to the request.</td><td style="background-color:#e8e8e8">表 8-120 显示了此维护操作的输入负载。设备应通过生成 Memory Sparing Event Record(参见表 8-60)来响应请求并传达操作结果。</td></tr>
</tbody>
</table>

**Table 8-120. Memory Sparing Input Payload | Memory Sparing 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 02h.</td><td>Maintenance Operation Class:应设置为 02h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass: The legal values are defined in Table 8-125.</td><td>Maintenance Operation Subclass:合法值在表 8-125 中定义。</td></tr>
<tr><td>02h</td><td>1</td><td>Flags<br>• Bit[0]: Query Resources Flag<br>• Bit[1]: Hard Sparing Flag<br>• Bit[2]: Sub-channel Valid Flag<br>• Bit[3]: Nibble Mask Valid Flag<br>• Bits[7:4]: Reserved</td><td>标志位<br>• Bit[0]:Query Resources Flag<br>• Bit[1]:Hard Sparing Flag<br>• Bit[2]:Sub-channel Valid Flag<br>• Bit[3]:Nibble Mask Valid Flag<br>• Bits[7:4]:保留</td></tr>
<tr><td>03h</td><td>1</td><td>Channel</td><td>Channel(通道)</td></tr>
<tr><td>04h</td><td>1</td><td>Rank</td><td>Rank(秩)</td></tr>
<tr><td>05h</td><td>3</td><td>Nibble Mask</td><td>Nibble Mask(半字节掩码)</td></tr>
<tr><td>08h</td><td>1</td><td>Bank Group</td><td>Bank Group(Bank 组)</td></tr>
<tr><td>09h</td><td>1</td><td>Bank</td><td>Bank(Bank 号)</td></tr>
<tr><td>0Ah</td><td>3</td><td>Row</td><td>Row(行号)</td></tr>
<tr><td>0Dh</td><td>2</td><td>Column</td><td>Column(列号)</td></tr>
<tr><td>0Fh</td><td>1</td><td>Sub-channel</td><td>Sub-channel(子通道)</td></tr>
</tbody>
</table>

> **Figure 8-X.** Memory Sparing (page 704) ｜ Memory Sparing
>
> <img src="figures/chapter_08/page_0704.png" alt="Figure 8-X page 704" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0704.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-1-5"></a>
#### 8.2.10.7.1.5 Device Built-in Test Operations | 设备内置测试操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This function is used to request a CXL.mem-capable device to execute one or more tests.</td><td style="background-color:#e8e8e8">此功能用于请求支持 CXL.mem 的设备执行一项或多项测试。</td></tr>
<tr><td>Media Test Subclass requires the device to execute one or more tests on the memory media. Media Tests that a device supports and their attributes can be discovered by getting the Media Test Capability Log (see Section 8.2.10.5.2.5). The host may discover the media tests that the device supports and then request the device to perform a single test or a list of tests from the supported tests. The test results can be retrieved accessing the Media Test Results Log (see Section 8.2.10.5.2.6). It is expected that CXL.mem traffic to the device is quiesced when a media test is started on the device. If CXL.mem requests are issued during tests execution, the device behavior is undefined.</td><td style="background-color:#e8e8e8">Media Test Subclass 要求设备对内存介质执行一项或多项测试。设备支持的 Media Tests 及其属性可以通过获取 Media Test Capability Log(参见 8.2.10.5.2.5 节)来发现。主机可以发现设备支持的介质测试,然后请求设备从受支持的测试中执行单个测试或测试列表。可以通过访问 Media Test Results Log(参见 8.2.10.5.2.6 节)来检索测试结果。当在设备上启动介质测试时,预计到设备的 CXL.mem 流量将处于静止状态。如果在测试执行期间发出 CXL.mem 请求,则设备行为未定义。</td></tr>
<tr><td>For configuring and launching the Media Test operation, Perform Maintenance Command shall have the Input Payload described in Table 8-121.</td><td style="background-color:#e8e8e8">要配置和启动 Media Test 操作,Perform Maintenance Command 应具有表 8-121 中描述的输入负载。</td></tr>
<tr><td>One or more tests that belong to the same subclass may be requested via a single command (see Table 8-122). For each requested test, a single Test Parameters Entry shall be set up. Because multiple tests may be scheduled via a single command, the Test Parameters length is variable. The Test Parameters may be fully transferred in a single chunk or transferred in multiple chunks by issuing multiple Perform Maintenance commands. If the Test Parameters are transferred in its entirety, the caller issues a single Perform Maintenance Command with Action = Full Transfer. If the Test Parameters are transferred in parts, the caller makes one call to Perform Maintenance with Action = Initiate Transfer, zero or more calls with Action = Continue Transfer, and one call with Action = End Transfer or Abort Transfer. The Test Parameters parts shall be transferred in order; otherwise, the device returns the Transfer Out of Order return code.</td><td style="background-color:#e8e8e8">可以通过单个命令请求属于同一子类的一个或多个测试(参见表 8-122)。对于每个请求的测试,应设置单个 Test Parameters Entry。由于可以通过单个命令调度多个测试,因此 Test Parameters 长度是可变的。Test Parameters 可以通过发出多个 Perform Maintenance 命令以单个块完全传输或以多个块传输。如果 Test Parameters 是整体传输的,则调用者发出 Action = Full Transfer 的单个 Perform Maintenance Command。如果 Test Parameters 是分部分传输的,则调用者使用 Action = Initiate Transfer 调用一次 Perform Maintenance,使用 Action = Continue Transfer 调用零次或多次,并使用 Action = End Transfer 或 Abort Transfer 调用一次。Test Parameters 部分应按顺序传输;否则,设备返回 Transfer Out of Order 返回码。</td></tr>
<tr><td>If the test is executing in background, the device may be asked to abort the test via the Request Abort Background Operation mailbox command. If a component supports Perform Maintenance Operation with this class, it must also support the Request Abort Background Operation command.</td><td style="background-color:#e8e8e8">如果测试在后台执行,可以通过 Request Abort Background Operation 邮箱命令请求设备中止测试。如果组件支持此类的 Perform Maintenance Operation,则它还必须支持 Request Abort Background Operation 命令。</td></tr>
</tbody>
</table>

**Table 8-121. Device Built-in Test Input Payload | Device Built-in Test 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 03h.</td><td>Maintenance Operation Class:应设置为 03h。</td></tr>
<tr><td>01h</td><td>1</td><td>Maintenance Operation Subclass<br>• 00h = Media Test<br>• 01h to BCh = Reserved<br>• C0h to FFh = Vendor Specific Test</td><td>Maintenance Operation Subclass<br>• 00h = Media Test<br>• 01h 到 BCh = 保留<br>• C0h 到 FFh = 厂商特定测试</td></tr>
<tr><td>02h</td><td>1</td><td>Action: 00h = Full Transfer; 01h = Initiate Transfer; 02h = Continue Transfer; 03h = End Transfer; 04h = Abort Transfer; All other encodings are reserved</td><td>Action:00h = Full Transfer;01h = Initiate Transfer;02h = Continue Transfer;03h = End Transfer;04h = Abort Transfer;所有其他编码保留</td></tr>
<tr><td>03h</td><td>4</td><td>Offset: The byte offset in the Test Parameters data. Expressed in multiples of 32 bytes. Ignored if Action = Full Transfer.</td><td>Offset:Test Parameters 数据中的字节偏移量。以 32 字节的倍数表示。如果 Action = Full Transfer 则忽略。</td></tr>
<tr><td>07h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>20h+20h*n</td><td>Test parameters: See Table 8-122.</td><td>Test parameters:参见表 8-122。</td></tr>
</tbody>
</table>

**Table 8-122. Test Parameters | Test Parameters**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>20h</td><td>Common Configuration Parameters: Input configuration parameters that apply to all the tests within a given subclass. The common configuration parameters for Media Test are defined in Table 8-123. The common configuration parameters for vendor specific test are defined by the vendor.</td><td>Common Configuration Parameters:适用于给定子类内所有测试的输入配置参数。Media Test 的公共配置参数在表 8-123 中定义。厂商特定测试的公共配置参数由厂商定义。</td></tr>
<tr><td>20h</td><td>20h</td><td>Test 1 Parameters Entry: Input parameters of Test 1. The format of the Test Parameter Entry for Media Test is defined in Table 8-124.</td><td>Test 1 Parameters Entry:测试 1 的输入参数。Media Test 的 Test Parameter Entry 格式在表 8-124 中定义。</td></tr>
<tr><td>40h</td><td>20h</td><td>Test 2 Parameters Entry: Input parameters of Test 2.</td><td>Test 2 Parameters Entry:测试 2 的输入参数。</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>(20h+20h*(n-1))</td><td>20h</td><td>Test n Parameters Entry: Input parameters of Test n.</td><td>Test n Parameters Entry:测试 n 的输入参数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Device Built-in Test (page 705) ｜ Device Built-in Test
>
> <img src="figures/chapter_08/page_0705.png" alt="Figure 8-X page 705" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0705.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2"></a>
### 8.2.10.7.2 Features Associated with Maintenance Operations | 与维护操作关联的特性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Maintenance operations leverage the Features command set (see Section 8.2.10.6).</td><td style="background-color:#e8e8e8">维护操作利用 Features 命令集(参见 8.2.10.6 节)。</td></tr>
<tr><td>A Feature that provides capabilities and configurations may be defined for a maintenance operation. The list of maintenance operations that the device supports can be discovered by analyzing the device's supported Features. This can be accomplished by issuing the Get Supported Features command.</td><td style="background-color:#e8e8e8">可以为维护操作定义提供能力和配置的 Feature。可以通过分析设备受支持的 Feature 来发现设备支持的维护操作列表。这可以通过发出 Get Supported Features 命令来完成。</td></tr>
<tr><td>Table 8-125 shows the Maintenance Operation Classes, Subclasses, and related Feature UUID.</td><td style="background-color:#e8e8e8">表 8-125 显示了 Maintenance Operation Classes、Subclasses 以及相关的 Feature UUID。</td></tr>
</tbody>
</table>

**Table 8-123. Common Configuration Parameters for Media Test Subclass | Media Test Subclass 的公共配置参数**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Number of Tests: Total number of tests requested.</td><td>Number of Tests:请求的测试总数。</td></tr>
<tr><td>01h</td><td>8</td><td>Start Address: Start DPA of the test, applies to all the tests.</td><td>Start Address:测试的起始 DPA,适用于所有测试。</td></tr>
<tr><td>09h</td><td>8</td><td>Length: The range of physical addresses to test, applies to all the tests. This length shall be in multiples of 64 bytes.</td><td>Length:要测试的物理地址范围,适用于所有测试。此长度应为 64 字节的倍数。</td></tr>
<tr><td>11h</td><td>1</td><td>Media Test Results Configuration<br>• Bit[0]: Error Signature Configuration: 0 = Complete; 1 = Single error signature<br>• Bits[7:1]: Reserved</td><td>Media Test Results Configuration<br>• Bit[0]:Error Signature Configuration:0 = Complete(完整);1 = Single error signature(单个错误签名)<br>• Bits[7:1]:保留</td></tr>
<tr><td>12h</td><td>1</td><td>Configuration Flags<br>• Bits[1:0]: ECC Disablement: 00b = Data ECC enabled & metadata ECC enabled; 01b = Data ECC disabled & metadata ECC enabled; 10b = Data ECC enabled & metadata ECC disabled; 11b = Data ECC disabled & metadata ECC disabled<br>• Bits[7:2]: Reserved</td><td>Configuration Flags<br>• Bits[1:0]:ECC Disablement:00b = 启用数据 ECC & 启用元数据 ECC;01b = 禁用数据 ECC & 启用元数据 ECC;10b = 启用数据 ECC & 禁用元数据 ECC;11b = 禁用数据 ECC & 禁用元数据 ECC<br>• Bits[7:2]:保留</td></tr>
<tr><td>13h</td><td>Dh</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

**Table 8-124. Test Parameters Entry Media Test Subclass | Test Parameters Entry Media Test Subclass**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Test ID: This field identifies the Test. The value discovered through the Media Test Capability Log Entry Structures (see Table 8-93).</td><td>Test ID:此字段标识测试。通过 Media Test Capability Log Entry Structures(参见表 8-93)发现的值。</td></tr>
<tr><td>02h</td><td>1</td><td>Number of iterations: Number of repetitions of the test.</td><td>Number of iterations:测试的重复次数。</td></tr>
<tr><td>03h</td><td>2</td><td>Flags<br>• Bit[0]: Inverse Pattern Enable<br>• Bit[1]: Exit on Uncorrectable Error<br>• Bit[2]: Error Count Threshold Programmed<br>• Bit[3]: Reserved<br>• Bits[7:4]: Addressing Mode: 0h = Ascending; 1h = Descending; 2h = Algorithm Specific; 3h = Random; All other values are reserved<br>• Bit[8]: Update Poison List on Uncorrectable Error<br>• Bits[15:9]: Reserved</td><td>标志位<br>• Bit[0]:Inverse Pattern Enable<br>• Bit[1]:Exit on Uncorrectable Error<br>• Bit[2]:Error Count Threshold Programmed<br>• Bit[3]:保留<br>• Bits[7:4]:Addressing Mode:0h = Ascending(升序);1h = Descending(降序);2h = Algorithm Specific(算法特定);3h = Random(随机);所有其他值保留<br>• Bit[8]:Update Poison List on Uncorrectable Error<br>• Bits[15:9]:保留</td></tr>
<tr><td>05h</td><td>2</td><td>Pattern Type: 00h = User provided; 01h = Vendor specific; 02h = PRBS; 03h = DPA[63:0] by eight; 04h = 55h; 05h = AAh; All other encodings are reserved</td><td>Pattern Type:00h = User provided;01h = Vendor specific;02h = PRBS;03h = DPA[63:0] by eight;04h = 55h;05h = AAh;所有其他编码保留</td></tr>
<tr><td>07h</td><td>1</td><td>Pattern Value: Pattern value provided by the user. This field is reserved if Pattern Type is not 00h.</td><td>Pattern Value:用户提供的 Pattern 值。如果 Pattern Type 不是 00h,则此字段保留。</td></tr>
<tr><td>08h</td><td>2</td><td>Vendor Specific: This field is set if Pattern Type field is 01h. The interpretation of this field is vendor specific.</td><td>Vendor Specific:如果 Pattern Type 字段为 01h,则设置此字段。此字段的解释由厂商定义。</td></tr>
<tr><td>0Ah</td><td>4</td><td>PRBS Seed: User provided PRBS Seed. This field is valid if Pattern Type is PRBS.</td><td>PRBS Seed:用户提供的 PRBS Seed。如果 Pattern Type 是 PRBS,则此字段有效。</td></tr>
<tr><td>0Eh</td><td>2</td><td>Error Count Threshold: User-programmable error count threshold.</td><td>Error Count Threshold:用户可编程错误计数阈值。</td></tr>
<tr><td>10h</td><td>10h</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Test Parameters (page 706-707) ｜ Test Parameters
>
> <img src="figures/chapter_08/page_0706.png" alt="Figure 8-X page 706" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0706.png)

**Table 8-125. Maintenance Operation: Classes, Subclasses, and Feature UUIDs | 维护操作:类、子类和 Feature UUID**

<table>
<thead>
<tr><th>Maintenance Operation Class</th><th>Class Description</th><th>Maintenance Operation Subclass</th><th>Subclass Description</th><th>UUID</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>No operation</td><td>00h</td><td>No operation</td><td>-</td></tr>
<tr><td>01h</td><td>PPR</td><td>00h</td><td>Soft PPR</td><td>892ba475-fad8-474e-9d3e-692c917568bb</td></tr>
<tr><td>01h</td><td>PPR</td><td>01h</td><td>Hard PPR</td><td>80ea4521-786f-4127-afb1-ec7459fb0e24</td></tr>
<tr><td>01h</td><td>PPR</td><td>Others</td><td>Reserved</td><td>-</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>00h</td><td>Cacheline - Memory Sparing</td><td>96C33386-91dd-44c7-9ecb-fdaf6503baC4</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>01h</td><td>Row - Memory Sparing</td><td>450ebf67-b135-4f97-a498-c2d57f279bed</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>02h</td><td>Bank - Memory Sparing</td><td>78b79636-90ac-4b64-A4ef-faac5d18a863</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>03h</td><td>Rank - Memory Sparing</td><td>34dbaff5-0552-4281-8f76-da0b5e7a76a7</td></tr>
<tr><td>02h</td><td>Memory Sparing</td><td>Others</td><td>Reserved</td><td>-</td></tr>
<tr><td>03h</td><td>Device Built-in Test</td><td>00h</td><td>Media Test</td><td>No associated feature</td></tr>
<tr><td>03h</td><td>Device Built-in Test</td><td>01h to BFh</td><td>Reserved</td><td>-</td></tr>
<tr><td>03h</td><td>Device Built-in Test</td><td>0C0h to 0FFh</td><td>Vendor Specific</td><td>Vendor Specific</td></tr>
<tr><td>04h to DFh</td><td>Reserved</td><td>All</td><td>Reserved</td><td>-</td></tr>
<tr><td>E0h to FFh</td><td>Vendor specific</td><td>All</td><td>Vendor specific</td><td>Vendor specific</td></tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>These Features represent maintenance operations capabilities and settings. Some fields of the Features are writable to configure the desired device behavior. Table 8-126 shows the Maintenance Operation Feature format. The first 16 bytes are common to all Maintenance Operation Features.</td><td style="background-color:#e8e8e8">这些 Feature 表示维护操作的能力和设置。Feature 的某些字段是可写的,以配置所需的设备行为。表 8-126 显示了 Maintenance Operation Feature 格式。前 16 个字节对于所有 Maintenance Operation Features 是通用的。</td></tr>
<tr><td>Row sparing in the Memory Sparing is equivalent to PPR; however, memory sparing is preferred when possible.</td><td style="background-color:#e8e8e8">Memory Sparing 中的 Row sparing 等同于 PPR;但是,当可能时,首选 memory sparing。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Maintenance Operation Classes/Subclasses (page 707) ｜ 维护操作类/子类
>
> <img src="figures/chapter_08/page_0707.png" alt="Figure 8-X page 707" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0707.png)

**Table 8-126. Common Maintenance Operation Feature Format | 通用维护操作 Feature 格式**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>RO</td><td>Maximum Maintenance Operation Latency: Bits[3:0] specify time scale (0h=1us, 1h=10us, 2h=100us, 3h=1ms, 4h=10ms, 5h=100ms, 6h=1s, 7h=10s); Bits[7:4] specify max operation latency with the time scale indicated in bits[3:0].</td></tr>
<tr><td>01h</td><td>2</td><td>RO</td><td>Operation Capabilities: Bit[0]: Device Initiated Capability; Bits[15:1]: Reserved</td></tr>
<tr><td>03h</td><td>2</td><td>RW</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved. Operation Mode default value is 0000h.</td></tr>
<tr><td>05h</td><td>1</td><td>RO</td><td>Maintenance Operation Class: This field specifies the Maintenance Operation Class.</td></tr>
<tr><td>06h</td><td>1</td><td>RO</td><td>Maintenance Operation Subclass: This field specifies the Maintenance Operation Subclass.</td></tr>
<tr><td>07h</td><td>9</td><td>RsvdZ</td><td>Reserved</td></tr>
<tr><td>10h</td><td>Varies</td><td>-</td><td>Operation specific fields</td></tr>
</tbody>
</table>

> **Figure 8-X.** Common Maintenance Operation Feature (page 708) ｜ 通用维护操作 Feature
>
> <img src="figures/chapter_08/page_0708.png" alt="Figure 8-X page 708" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0708.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2-1"></a>
#### 8.2.10.7.2.1 sPPR Feature Discovery and Configuration | sPPR 特性发现和配置

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The UUID of this feature is defined in Table 8-125.</td><td style="background-color:#e8e8e8">此特性的 UUID 在表 8-125 中定义。</td></tr>
<tr><td>Table 8-127 shows the information returned in the Get Supported Features output payload for the sPPR Feature. Some Feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-127 显示了 sPPR Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
</tbody>
</table>

**Table 8-127. Supported Feature Entry for the sPPR Feature | sPPR Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>892ba475-fad8-474e-9d3e-692c917568bb</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>14h</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>03h</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 010b if saved selection is supported (Bit[6] = 1); otherwise 000b (Deepest Reset Persistence)<br>• Bit[4]: Vendor-specific value (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: Vendor-specific value (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>03h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>03h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 0 (Configuration Change after Cold Reset)<br>• Bit[1]: 1 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log Change)<br>• Bit[5]: 0 (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 is recommended, 0 is permitted (CEL[11:10] Valid)<br>• Bit[10]: 0 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>18</td><td>Reserved</td><td>All 0s</td></tr>
</tbody>
</table>

**Table 8-128. sPPR Feature Readable Attributes | sPPR Feature 可读属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Maintenance Operation Latency: This field is defined in Table 8-126.</td><td>Maximum Maintenance Operation Latency:此字段在表 8-126 中定义。</td></tr>
<tr><td>01h</td><td>2</td><td>Operation Capabilities: This field is defined in Table 8-126. If Device Initiated capability bit is set to 1, the device has the capability to initiate sPPR maintenance without host involvement at runtime. Device Initiated capability bit shall be cleared to 0 if Restriction Flags bit[0] or bit[2] is set to 1.</td><td>Operation Capabilities:此字段在表 8-126 中定义。如果 Device Initiated capability 位设置为 1,则设备能够在运行时无需主机参与启动 sPPR 维护。如果 Restriction Flags 的 bit[0] 或 bit[2] 设置为 1,则 Device Initiated capability 位应清零为 0。</td></tr>
<tr><td>03h</td><td>2</td><td>Operation Mode: This field is defined in Table 8-126. If Device Initiated bit is set to 1, the device may initiate sPPR maintenance without host involvement at runtime.</td><td>Operation Mode:此字段在表 8-126 中定义。如果 Device Initiated 位设置为 1,则设备可以在运行时无需主机参与启动 sPPR 维护。</td></tr>
<tr><td>05h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h (PPR).</td><td>Maintenance Operation Class:应设置为 01h (PPR)。</td></tr>
<tr><td>06h</td><td>1</td><td>Maintenance Operation Subclass: It shall be cleared to 00h (Soft PPR).</td><td>Maintenance Operation Subclass:应清零为 00h (Soft PPR)。</td></tr>
<tr><td>07h</td><td>9</td><td>Reserved</td><td>保留</td></tr>
<tr><td>10h</td><td>1</td><td>sPPR Flags<br>• Bit[0]: DPA Support Flag: If set, the device supports DPA argument in the Perform Maintenance command input payload.<br>• Bit[1]: Nibble Support Flag: If set, the device supports Nibble Mask argument in the Perform Maintenance command input payload.<br>• Bit[2]: Memory Sparing Event Record Capability Flag: If set, the device has the capability to produce a Memory Sparing Event Record upon completion of sPPR maintenance operation.<br>• Bit[3]: Device Initiated at Device Boot Capability: A value of 1 indicates that the device has the capability to initiate the sPPR maintenance operation without host involvement when Memory_Active = 0.<br>• Bits[7:4]: Reserved</td><td>sPPR Flags<br>• Bit[0]:DPA Support Flag:如果设置,设备支持 Perform Maintenance 命令输入负载中的 DPA 参数。<br>• Bit[1]:Nibble Support Flag:如果设置,设备支持 Perform Maintenance 命令输入负载中的 Nibble Mask 参数。<br>• Bit[2]:Memory Sparing Event Record Capability Flag:如果设置,设备能够在 sPPR 维护操作完成时生成 Memory Sparing Event Record。<br>• Bit[3]:Device Initiated at Device Boot Capability:值 1 表示设备能够在 Memory_Active = 0 时无需主机参与启动 sPPR 维护操作。<br>• Bits[7:4]:保留</td></tr>
<tr><td>11h</td><td>2</td><td>Restriction Flags<br>• Bit[0]: 0 = CXL.mem requests are correctly processed; 1 = Media is not accessible.<br>• Bit[1]: Reserved.<br>• Bit[2]: 0 = Data is retained; 1 = Data may or may not be retained.<br>• Bits[15:3]: Reserved.</td><td>Restriction Flags<br>• Bit[0]:0 = 正确处理 CXL.mem 请求;1 = 介质不可访问。<br>• Bit[1]:保留。<br>• Bit[2]:0 = 保留数据;1 = 数据可能保留,也可能不保留。<br>• Bits[15:3]:保留。</td></tr>
<tr><td>13h</td><td>1</td><td>sPPR Operation Mode<br>• Bit[0]: Memory Sparing Event Record Enable<br>• Bit[1]: Device Initiated at Device Boot<br>• Bits[7:2]: Reserved</td><td>sPPR Operation Mode<br>• Bit[0]:Memory Sparing Event Record Enable<br>• Bit[1]:Device Initiated at Device Boot<br>• Bits[7:2]:保留</td></tr>
</tbody>
</table>

**Table 8-129. sPPR Feature Writable Attributes | sPPR Feature 可写属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved</td><td>Operation Mode:Bit[0]:Device Initiated;Bits[15:1]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>sPPR Operation Mode: Bit[0]: Memory Sparing Event Record Enable; Bit[1]: Device Initiated at Device Boot; Bits[7:2]: Reserved</td><td>sPPR Operation Mode:Bit[0]:Memory Sparing Event Record Enable;Bit[1]:Device Initiated at Device Boot;Bits[7:2]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** sPPR Feature (page 709-711) ｜ sPPR Feature
>
> <img src="figures/chapter_08/page_0709.png" alt="Figure 8-X page 709" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0709.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2-2"></a>
#### 8.2.10.7.2.2 hPPR Feature Discovery and Configuration | hPPR 特性发现和配置

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The UUID of this feature is defined in Table 8-125.</td><td style="background-color:#e8e8e8">此特性的 UUID 在表 8-125 中定义。</td></tr>
<tr><td>Table 8-130 shows the information returned in the Get Supported Features output payload for the hPPR Feature. Some Feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-130 显示了 hPPR Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
</tbody>
</table>

**Table 8-130. Supported Feature Entry for the hPPR Feature | hPPR Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>80ea4521-786f-4127-afb1-ec7459fb0e24</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>14h</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>03h</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 010b if saved selection is supported (Bit[6] = 1); otherwise, 000b (Deepest Reset Persistence)<br>• Bit[4]: Vendor-specific value (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: Vendor-specific value (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>03h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>03h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 0 (Configuration Change after Cold Reset)<br>• Bit[1]: 1 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log change)<br>• Bit[5]: 0 (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 is recommended, 0 is permitted (CEL[11:10] Valid)<br>• Bit[10]: 0 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>2</td><td>Reserved</td><td>All 0s</td></tr>
</tbody>
</table>

**Table 8-131. hPPR Feature Readable Attributes | hPPR Feature 可读属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Maintenance Operation Latency: This field is defined in Table 8-126.</td><td>Maximum Maintenance Operation Latency:此字段在表 8-126 中定义。</td></tr>
<tr><td>01h</td><td>2</td><td>Operation Capabilities: This field is defined in Table 8-126. If Device Initiated capability bit is set to 1, the device has the capability to initiate hPPR maintenance without host involvement at runtime. Device Initiated capability bit shall be cleared to 0 if Restriction Flags Bit[0] or Bit[2] is set to 1.</td><td>Operation Capabilities:此字段在表 8-126 中定义。如果 Device Initiated capability 位设置为 1,则设备能够在运行时无需主机参与启动 hPPR 维护。如果 Restriction Flags 的 Bit[0] 或 Bit[2] 设置为 1,则 Device Initiated capability 位应清零为 0。</td></tr>
<tr><td>03h</td><td>2</td><td>Operation Mode: This field is defined in Table 8-126. If Device Initiated bit is set to 1, the device may initiate hPPR maintenance without host involvement at runtime.</td><td>Operation Mode:此字段在表 8-126 中定义。如果 Device Initiated 位设置为 1,则设备可以在运行时无需主机参与启动 hPPR 维护。</td></tr>
<tr><td>05h</td><td>1</td><td>Maintenance Operation Class: It shall be set to 01h (PPR).</td><td>Maintenance Operation Class:应设置为 01h (PPR)。</td></tr>
<tr><td>06h</td><td>1</td><td>Maintenance Operation Subclass: It shall be set to 01h (Hard PPR).</td><td>Maintenance Operation Subclass:应设置为 01h (Hard PPR)。</td></tr>
<tr><td>07h</td><td>9</td><td>Reserved</td><td>保留</td></tr>
<tr><td>10h</td><td>1</td><td>hPPR Flags<br>• Bit[0]: DPA Support Flag<br>• Bit[1]: Nibble Support Flag<br>• Bit[2]: Memory Sparing Event Record Capability Flag<br>• Bit[3]: Device Initiated at Device Boot Capability<br>• Bits[7:4]: Reserved</td><td>hPPR Flags<br>• Bit[0]:DPA Support Flag<br>• Bit[1]:Nibble Support Flag<br>• Bit[2]:Memory Sparing Event Record Capability Flag<br>• Bit[3]:Device Initiated at Device Boot Capability<br>• Bits[7:4]:保留</td></tr>
<tr><td>11h</td><td>2</td><td>Restriction Flags<br>• Bit[0]: 0 = CXL.mem requests are correctly processed; 1 = Media is not accessible.<br>• Bit[1]: Reserved.<br>• Bit[2]: 0 = Data is retained; 1 = Data may or may not be retained.<br>• Bits[15:3]: Reserved.</td><td>Restriction Flags<br>• Bit[0]:0 = 正确处理 CXL.mem 请求;1 = 介质不可访问。<br>• Bit[1]:保留。<br>• Bit[2]:0 = 保留数据;1 = 数据可能保留,也可能不保留。<br>• Bits[15:3]:保留。</td></tr>
<tr><td>13h</td><td>1</td><td>hPPR Operation Mode<br>• Bit[0]: Memory Sparing Event Record Enable<br>• Bit[1]: Device Initiated at Device Boot<br>• Bits[7:2]: Reserved</td><td>hPPR Operation Mode<br>• Bit[0]:Memory Sparing Event Record Enable<br>• Bit[1]:Device Initiated at Device Boot<br>• Bits[7:2]:保留</td></tr>
</tbody>
</table>

**Table 8-132. hPPR Feature Writable Attributes | hPPR Feature 可写属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved</td><td>Operation Mode:Bit[0]:Device Initiated;Bits[15:1]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>hPPR Operation Mode: Bit[0]: Memory Sparing Event Record Enable; Bit[1]: Device Initiated at Device Boot; Bits[7:2]: Reserved</td><td>hPPR Operation Mode:Bit[0]:Memory Sparing Event Record Enable;Bit[1]:Device Initiated at Device Boot;Bits[7:2]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** hPPR Feature (page 711-713) ｜ hPPR Feature
>
> <img src="figures/chapter_08/page_0711.png" alt="Figure 8-X page 711" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0711.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-7-2-3"></a>
#### 8.2.10.7.2.3 Memory Sparing Features | 内存备用 Feature

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The UUIDs associated with these features are defined in Table 8-125.</td><td style="background-color:#e8e8e8">与此特性关联的 UUID 在表 8-125 中定义。</td></tr>
<tr><td>Table 8-133 shows the information returned in the Get Supported Features output payload for the Enhanced Memory Sparing Feature. Some Feature attributes are changeable.</td><td style="background-color:#e8e8e8">表 8-133 显示了 Enhanced Memory Sparing Feature 的 Get Supported Features 输出负载中返回的信息。某些 Feature 属性是可更改的。</td></tr>
</tbody>
</table>

**Table 8-133. Supported Feature Entry for the Memory Sparing Feature | Memory Sparing Feature 的 Supported Feature Entry**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>Attribute</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>10h</td><td>Feature Identifier</td><td>Depends on the Maintenance Operation subclass (see Table 8-125 for details)</td></tr>
<tr><td>10h</td><td>2</td><td>Feature Index</td><td>Device specific</td></tr>
<tr><td>12h</td><td>2</td><td>Get Feature Size</td><td>13h</td></tr>
<tr><td>14h</td><td>2</td><td>Set Feature Size</td><td>02h</td></tr>
<tr><td>16h</td><td>4</td><td>Attribute Flags</td><td>• Bit[0]: Vendor-specific value (Changeable)<br>• Bits[3:1]: 000b (Deepest Reset Persistence=None. Any reset will restore the default value.)<br>• Bit[4]: 0 (Persist across Firmware Update)<br>• Bit[5]: 1 (Default Selection Supported)<br>• Bit[6]: Vendor-specific value (Saved Selection Supported)<br>• Bits[31:7]: Reserved</td></tr>
<tr><td>1Ah</td><td>1</td><td>Get Feature Version</td><td>01h</td></tr>
<tr><td>1Bh</td><td>1</td><td>Set Feature Version</td><td>01h</td></tr>
<tr><td>1Ch</td><td>2</td><td>Set Feature Effects</td><td>• Bit[0]: 0 (Configuration Change after Cold Reset)<br>• Bit[1]: 1 (Immediate Configuration Change)<br>• Bit[2]: 0 (Immediate Data Change)<br>• Bit[3]: 0 (Immediate Policy Change)<br>• Bit[4]: Vendor-specific value (Immediate Log Change)<br>• Bit[5]: 0 (Security State Change)<br>• Bit[6]: 0 (Background Operation)<br>• Bit[7]: Vendor-specific value (Secondary Mailbox Supported)<br>• Bit[8]: 0 (Request Abort Background Operation Supported)<br>• Bit[9]: 1 (CEL[11:10] Valid)<br>• Bit[10]: 0 (Configuration Change after Conventional Reset)<br>• Bit[11]: 0 (Configuration Change after CXL Reset)<br>• Bits[15:12]: 0h</td></tr>
<tr><td>1Eh</td><td>12h</td><td>Reserved</td><td>All 0s</td></tr>
</tbody>
</table>

**Table 8-134. Memory Sparing Feature Readable Attributes | Memory Sparing Feature 可读属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Maximum Maintenance Operation Latency: This field is defined in Table 8-126.</td><td>Maximum Maintenance Operation Latency:此字段在表 8-126 中定义。</td></tr>
<tr><td>01h</td><td>2</td><td>Operation Capabilities: This field is defined in Table 8-126. Device Initiated capability bit shall be cleared to 0 if Restriction flags bit[0] is set to 1.</td><td>Operation Capabilities:此字段在表 8-126 中定义。如果 Restriction flags 的 bit[0] 设置为 1,则 Device Initiated capability 位应清零为 0。</td></tr>
<tr><td>03h</td><td>2</td><td>Operation Mode: This field is defined in Table 8-126.</td><td>Operation Mode:此字段在表 8-126 中定义。</td></tr>
<tr><td>05h</td><td>1</td><td>Maintenance Operation Class: This field shall be set to 02h (Memory Sparing).</td><td>Maintenance Operation Class:此字段应设置为 02h (Memory Sparing)。</td></tr>
<tr><td>06h</td><td>1</td><td>Maintenance Operation Subclass: Depends on the scope of the sparing needed.</td><td>Maintenance Operation Subclass:取决于所需备用的范围。</td></tr>
<tr><td>07h</td><td>0Ah</td><td>Reserved</td><td>保留</td></tr>
<tr><td>11h</td><td>2</td><td>Restriction Flags<br>• Bit[0]: Sparing Side Effects: 0 = The device preserves the memory content and remains responsive to CXL.mem requests during the sparing operation. 1 = The device is permitted to drop CXL.mem write requests, return poison in response to CXL.mem read requests during the sparing operation. The device does not guarantee preservation of HDM contents across the sparing operation.<br>• Bit[1]: Hard Sparing: If set, the device has the capability for performing the sparing that is irreversible and that can survive any Conventional Reset.<br>• Bit[2]: Soft Sparing: If set, the device has the capability for performing the sparing in a non-permanent way; thus, the change will be reverted after any Conventional Reset.<br>• Bits[15:3]: Reserved.</td><td>Restriction Flags<br>• Bit[0]:Sparing Side Effects:0 = 设备在备用操作期间保留内存内容并保持对 CXL.mem 请求的响应。1 = 设备允许在备用操作期间丢弃 CXL.mem 写入请求,并对 CXL.mem 读取请求返回 poison。设备不保证在备用操作期间保留 HDM 内容。<br>• Bit[1]:Hard Sparing:如果设置,设备具有执行不可逆备用且可在任何 Conventional Reset 后存活的能力。<br>• Bit[2]:Soft Sparing:如果设置,设备具有以非永久方式执行备用的能力;因此,更改将在任何 Conventional Reset 后被恢复。<br>• Bits[15:3]:保留。</td></tr>
</tbody>
</table>

**Table 8-135. Memory Sparing Feature Writable Attributes | Memory Sparing Feature 可写属性**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>Operation Mode: Bit[0]: Device Initiated; Bits[15:1]: Reserved</td><td>Operation Mode:Bit[0]:Device Initiated;Bits[15:1]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Memory Sparing Feature (page 714-715) ｜ Memory Sparing Feature
>
> <img src="figures/chapter_08/page_0714.png" alt="Figure 8-X page 714" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0714.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8"></a>
## 8.2.10.8 PBR Component Command Set | PBR 组件命令集

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Support for this command set is required for all devices that are PBR link capable (i.e., PBR switches and GFDs).</td><td style="background-color:#e8e8e8">所有支持 PBR 链路的设备(即 PBR 交换机和 GFD)都需要支持此命令集。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8-1"></a>
### 8.2.10.8.1 Identify PBR Component (Opcode 0700h) | 标识 PBR 组件 (操作码 0700h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command provides information about a component specific to its PBR fabric capabilities.</td><td style="background-color:#e8e8e8">此命令提供有关特定于其 PBR fabric 能力的组件的信息。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-136. Identify PBR Component Response Payload | Identify PBR Component 响应负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>2</td><td>• Bits[11:0]: PID: Assigned PID of this device or FFFh if no PID has been assigned<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:PID:此设备的分配 PID,或 FFFh(如果尚未分配 PID)<br>• Bits[15:12]:保留</td></tr>
<tr><td>02h</td><td>2</td><td>• Bits[11:0]: Primary FM PID: PID of the FM registered as primary FM. A value of FFFh indicates no primary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Primary FM PID:注册为 primary FM 的 FM 的 PID。值 FFFh 表示未注册 primary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>04h</td><td>10h</td><td>Primary FM UUID: UUID of the FM registered as primary FM.</td><td>Primary FM UUID:注册为 primary FM 的 FM 的 UUID。</td></tr>
<tr><td>14h</td><td>2</td><td>• Bits[11:0]: Secondary FM PID: PID of the FM registered as secondary FM. A value of FFFh indicates no secondary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Secondary FM PID:注册为 secondary FM 的 FM 的 PID。值 FFFh 表示未注册 secondary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>16h</td><td>10h</td><td>Secondary FM UUID: UUID of the FM registered as secondary FM.</td><td>Secondary FM UUID:注册为 secondary FM 的 FM 的 UUID。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Identify PBR Component (page 716) ｜ Identify PBR Component
>
> <img src="figures/chapter_08/page_0716.png" alt="Figure 8-X page 716" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0716.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8-2"></a>
### 8.2.10.8.2 Claim Ownership (Opcode 0701h) | 声明所有权 (操作码 0701h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command is used by an FM to register itself as either the primary or secondary FM. The device's PID is also assigned as part of this operation. The device's PID assignment shall only be updated if the FW ownership registration operation is successful.</td><td style="background-color:#e8e8e8">此命令由 FM 用于将自身注册为 primary 或 secondary FM。设备的 PID 也作为此操作的一部分进行分配。仅当 FW 所有权注册操作成功时,设备的 PID 分配才会更新。</td></tr>
<tr><td>Registration of FMs and assignment of a PID apply to all CCIs on a PBR component.</td><td style="background-color:#e8e8e8">FM 的注册和 PID 的分配适用于 PBR 组件上的所有 CCI。</td></tr>
<tr><td>Operation 0 (Register Primary FM and assign PID) shall fail with "Invalid Input" if a device already has a primary FM registered.</td><td style="background-color:#e8e8e8">如果设备已注册 primary FM,则操作 0(Register Primary FM and assign PID)应以 "Invalid Input" 失败。</td></tr>
<tr><td>Operation 1 (Register Secondary FM) shall fail with "Invalid Input" if a device already has a secondary FM registered or if the request was initiated by an FM other than the registered primary FM.</td><td style="background-color:#e8e8e8">如果设备已注册 secondary FM,或请求由已注册 primary FM 之外的 FM 发起,则操作 1(Register Secondary FM)应以 "Invalid Input" 失败。</td></tr>
<tr><td>Operation 2 (Update PID) is valid only when received from the primary FM and shall terminate with "Invalid Input" otherwise.</td><td style="background-color:#e8e8e8">操作 2(Update PID)仅当从 primary FM 接收时有效,否则应以 "Invalid Input" 终止。</td></tr>
<tr><td>Operation 3 (Promote Secondary FM) is valid only when received from the secondary FM and shall terminate with "Invalid Input" otherwise.</td><td style="background-color:#e8e8e8">操作 3(Promote Secondary FM)仅当从 secondary FM 接收时有效,否则应以 "Invalid Input" 终止。</td></tr>
<tr><td>Promoting a secondary FM to the primary FM position leaves the secondary FM position unregistered.</td><td style="background-color:#e8e8e8">将 secondary FM 提升到 primary FM 位置会使 secondary FM 位置未注册。</td></tr>
<tr><td>Attempting to register or assign a PID of FFFh shall result in an "Invalid Input" failure return code.</td><td style="background-color:#e8e8e8">尝试注册或分配 PID 为 FFFh 将导致 "Invalid Input" 失败返回码。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-137. Claim Ownership Request Payload | Claim Ownership 请求负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>1</td><td>Operation: 00h = Register Primary FM and assign PID; 01h = Register Secondary FM; 02h = Update PID; 03h = Promote Secondary FM; All other encodings are reserved</td><td>Operation:00h = Register Primary FM and assign PID;01h = Register Secondary FM;02h = Update PID;03h = Promote Secondary FM;所有其他编码保留</td></tr>
<tr><td>1h</td><td>2</td><td>• Bits[11:0]: FM PID: PID of the FM requesting ownership. Valid only if Operation is cleared to 00h or set to 01h.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:FM PID:请求所有权的 FM 的 PID。仅当 Operation 清零为 00h 或设置为 01h 时有效。<br>• Bits[15:12]:保留</td></tr>
<tr><td>3h</td><td>10h</td><td>UUID: UUID of the FM requesting ownership. Valid only if Operation is cleared to 00h or set to 01h.</td><td>UUID:请求所有权的 FM 的 UUID。仅当 Operation 清零为 00h 或设置为 01h 时有效。</td></tr>
<tr><td>13h</td><td>2</td><td>• Bits[11:0]: Assigned PID: PID value being assigned to the device. Valid only if Operation is 00h or 02h.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Assigned PID:分配给设备的 PID 值。仅当 Operation 为 00h 或 02h 时有效。<br>• Bits[15:12]:保留</td></tr>
</tbody>
</table>

**Table 8-138. Claim Ownership Response Payload | Claim Ownership 响应负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>2</td><td>• Bits[11:0]: Primary FM PID: PID of the FM registered as primary FM. A value of FFFh indicates no primary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Primary FM PID:注册为 primary FM 的 FM 的 PID。值 FFFh 表示未注册 primary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>2h</td><td>10h</td><td>Primary FM UUID: UUID of the FM registered as primary FM.</td><td>Primary FM UUID:注册为 primary FM 的 FM 的 UUID。</td></tr>
<tr><td>12h</td><td>2</td><td>• Bits[11:0]: Secondary FM PID: PID of the FM registered as secondary FM. A value of FFFh indicates no secondary FM is registered.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Secondary FM PID:注册为 secondary FM 的 FM 的 PID。值 FFFh 表示未注册 secondary FM。<br>• Bits[15:12]:保留</td></tr>
<tr><td>14h</td><td>10h</td><td>Secondary FM UUID: UUID of the FM registered as secondary FM.</td><td>Secondary FM UUID:注册为 secondary FM 的 FM 的 UUID。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Claim Ownership (page 717) ｜ Claim Ownership
>
> <img src="figures/chapter_08/page_0717.png" alt="Figure 8-X page 717" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0717.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-8-3"></a>
### 8.2.10.8.3 Read CDAT (Opcode 0702h) | 读取 CDAT (操作码 0702h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command is used to read the CDAT from GAEs and GFDs.</td><td style="background-color:#e8e8e8">此命令用于从 GAE 和 GFD 读取 CDAT。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-139. Read CDAT Request Payload | Read CDAT 请求负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>2</td><td>• Bits[11:0]: Target PID: PID of device routing path CDAT to query. Valid only for PBR switches.<br>• Bits[15:12]: Reserved</td><td>• Bits[11:0]:Target PID:要查询其 CDAT 的设备路由路径的 PID。仅对 PBR 交换机有效。<br>• Bits[15:12]:保留</td></tr>
<tr><td>2h</td><td>2</td><td>Reserved</td><td>保留</td></tr>
<tr><td>4h</td><td>8</td><td>Start Byte: Offset in bytes into CDAT Data.</td><td>Start Byte:CDAT 数据中的字节偏移量。</td></tr>
<tr><td>Ch</td><td>8</td><td>Number of Bytes: Size in bytes of CDAT Data requested.</td><td>Number of Bytes:请求的 CDAT 数据的大小(以字节为单位)。</td></tr>
</tbody>
</table>

**Table 8-140. Read CDAT Response Payload | Read CDAT 响应负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>0h</td><td>8</td><td>Total CDAT Size: Size in bytes of the full CDAT.</td><td>Total CDAT Size:完整 CDAT 的大小(以字节为单位)。</td></tr>
<tr><td>8h</td><td>8</td><td>Number of Bytes: Size in bytes of returned CDAT Data.</td><td>Number of Bytes:返回的 CDAT 数据的大小(以字节为单位)。</td></tr>
<tr><td>10h</td><td>Varies</td><td>CDAT Data: CDAT for the specified target, as defined in the CDAT Specification.</td><td>CDAT Data:指定目标的 CDAT,定义见 CDAT 规范。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Read CDAT (page 718) ｜ Read CDAT
>
> <img src="figures/chapter_08/page_0718.png" alt="Figure 8-X page 718" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0718.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9"></a>
## 8.2.10.9 Memory Device Command Sets | 内存设备命令集

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section describes the commands specific to CXL memory devices that implement the PCIe Configuration Space Header Class Code defined in Section 8.1.12.1, advertise Memory Device Command support in the Mailbox Capabilities register (see Section 8.2.9.4.3), or report a Type value of 03h or 04h in the Identify response payload.</td><td style="background-color:#e8e8e8">本节描述特定于 CXL memory device 的命令,这些设备实现 8.1.12.1 节中定义的 PCIe Configuration Space Header Class Code,在 Mailbox Capabilities 寄存器(参见 8.2.9.4.3 节)中通告 Memory Device Command 支持,或在 Identify 响应负载中报告 Type 值为 03h 或 04h。</td></tr>
<tr><td>Opcodes also provide an implicit major version number, which means a command's definition shall not change in an incompatible way in future revisions of this specification. Instead, if an incompatible change is required, the specification defining the change shall define a new opcode for the changed command. Commands may evolve by defining new fields in the payload definitions that were originally defined as Reserved, but only in a way where software written using the earlier definition will continue to work correctly, and software written to the new definition can use the 0 value or the payload size to detect devices that do not support the new field. This implicit minor versioning allows software to be written with the understanding that an opcode shall only evolve by adding backward-compatible changes.</td><td style="background-color:#e8e8e8">操作码还提供隐式的主版本号,这意味着命令定义不应在本规范的未来修订版中以不兼容的方式更改。相反,如果需要不兼容的更改,则定义更改的规范应为更改的命令定义新的操作码。命令可以通过在最初定义为保留的负载定义中定义新字段来演进,但只能以使用早期定义编写的软件将继续正常工作的方式,并且编写为新定义的软件可以使用值 0 或负载大小来检测不支持新字段的设备。这种隐式次要版本控制允许软件在理解以下情况的基础上编写:操作码应仅通过添加向后兼容的更改来演进。</td></tr>
<tr><td>Table 8-141 and the following sections use the terms "Persistent memory device" and "CXL Memory Device that supports Persistence" interchangeably. A persistent memory device behaves in the following ways:<br>• All writes targeting persistent memory ranges that have been completed on CXL, but are still held in volatile buffers on the device, shall be flushed to media under the following conditions:<br>  — Any reset event<br>  — Reception of GPF Phase 2<br>  — Surprise power loss<br>• If the device is unable, for any reason, to flush all the writes that have been completed on CXL to persistent memory successfully, the Device shall increment the Dirty Shutdown Count in the Health Info (see Table 8-148) on the next reset. Incrementing the Dirty Shutdown Count may be considered a failure event by the Host and may indicate user data loss.</td><td style="background-color:#e8e8e8">表 8-141 和以下各节中,术语 "Persistent memory device" 和 "CXL Memory Device that supports Persistence" 可以互换使用。持久性内存设备的行为方式如下:<br>• 所有针对已在 CXL 上完成但仍保留在设备上的易失性缓冲区中的持久性内存范围的写入,应在以下条件下刷新到介质:<br>  — 任何复位事件<br>  — 接收 GPF Phase 2<br>  — 意外断电<br>• 如果设备由于任何原因无法成功刷新所有已在 CXL 上完成到持久性内存的写入,则设备应在下次复位时增加 Health Info(参见表 8-148)中的 Dirty Shutdown Count。增加 Dirty Shutdown Count 可能被主机视为故障事件,并可能表示用户数据丢失。</td></tr>
</tbody>
</table>

> **Figure 8-X.** CXL Defined Memory Device Command Opcodes (page 719) ｜ CXL 定义的内存设备命令操作码
>
> <img src="figures/chapter_08/page_0719.png" alt="Figure 8-X page 719" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0719.png)

**Table 8-141. CXL Defined Memory Device Command Opcodes (Vendor ID = 1E98h or 0000h) | CXL 定义的内存设备命令操作码 (Vendor ID = 1E98h 或 0000h)**

<table>
<thead>
<tr><th>Bits[15:8]</th><th>Command</th><th>Bits[7:0]</th><th>Combined Opcode</th><th>Required Type 1/2/3 Device</th><th>Required GFD</th><th>Command Set</th></tr>
</thead>
<tbody>
<tr><td>40h</td><td>Identify Memory Device</td><td>00h</td><td>4000h</td><td>M</td><td>M</td><td>Identify Memory Device (Section 8.2.10.9.1.1)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>00h</td><td>4100h</td><td>O</td><td>P</td><td>Get Partition Info (Section 8.2.10.9.2.1)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>01h</td><td>4101h</td><td>O</td><td>P</td><td>Set Partition Info (Section 8.2.10.9.2.2)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>02h</td><td>4102h</td><td>PM</td><td>P</td><td>Get LSA (Section 8.2.10.9.2.3)</td></tr>
<tr><td>41h</td><td>Capacity Config and Label Storage</td><td>03h</td><td>4103h</td><td>PM</td><td>P</td><td>Set LSA (Section 8.2.10.9.2.4)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>00h</td><td>4200h</td><td>M</td><td>M</td><td>Get Health Info (Section 8.2.10.9.3.1)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>01h</td><td>4201h</td><td>M</td><td>M</td><td>Get Alert Configuration (Section 8.2.10.9.3.2)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>02h</td><td>4202h</td><td>M</td><td>M</td><td>Set Alert Configuration (Section 8.2.10.9.3.3)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>03h</td><td>4203h</td><td>PM</td><td>P</td><td>Get Shutdown State (Section 8.2.10.9.3.4)</td></tr>
<tr><td>42h</td><td>Health Info and Alerts</td><td>04h</td><td>4204h</td><td>PM</td><td>P</td><td>Set Shutdown State (Section 8.2.10.9.3.5)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>00h</td><td>4300h</td><td>PM</td><td>O</td><td>Get Poison List (Section 8.2.10.9.4.1)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>01h</td><td>4301h</td><td>O</td><td>O</td><td>Inject Poison (Section 8.2.10.9.4.2)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>02h</td><td>4302h</td><td>O</td><td>O</td><td>Clear Poison (Section 8.2.10.9.4.3)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>03h</td><td>4303h</td><td>PM</td><td>O</td><td>Get Scan Media Capabilities (Section 8.2.10.9.4.4)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>04h</td><td>4304h</td><td>PM</td><td>O</td><td>Scan Media (Section 8.2.10.9.4.5)</td></tr>
<tr><td>43h</td><td>Media and Poison Management</td><td>05h</td><td>4305h</td><td>PM</td><td>O</td><td>Get Scan Media Results (Section 8.2.10.9.4.6)</td></tr>
<tr><td>44h</td><td>Sanitize and Media Operations</td><td>00h</td><td>4400h</td><td>O</td><td>O</td><td>Sanitize (Section 8.2.10.9.5.1)</td></tr>
<tr><td>44h</td><td>Sanitize and Media Operations</td><td>01h</td><td>4401h</td><td>O</td><td>O</td><td>Secure Erase (Section 8.2.10.9.5.2)</td></tr>
<tr><td>44h</td><td>Sanitize and Media Operations</td><td>02h</td><td>4402h</td><td>O</td><td>O</td><td>Media Operations (Section 8.2.10.9.5.3)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>00h</td><td>4500h</td><td>O</td><td>P</td><td>Get Security State (Section 8.2.10.9.6.1)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>01h</td><td>4501h</td><td>O</td><td>P</td><td>Set Passphrase (Section 8.2.10.9.6.2)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>02h</td><td>4502h</td><td>O</td><td>P</td><td>Disable Passphrase (Section 8.2.10.9.6.3)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>03h</td><td>4503h</td><td>O</td><td>P</td><td>Unlock (Section 8.2.10.9.6.4)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>04h</td><td>4504h</td><td>O</td><td>P</td><td>Freeze Security State (Section 8.2.10.9.6.5)</td></tr>
<tr><td>45h</td><td>Persistent Memory Data-at-rest Security</td><td>05h</td><td>4505h</td><td>O</td><td>P</td><td>Passphrase Secure Erase (Section 8.2.10.9.6.6)</td></tr>
<tr><td>46h</td><td>Security Passthrough</td><td>00h</td><td>4600h</td><td>O</td><td>P</td><td>Security Send (Section 8.2.10.9.7.1)</td></tr>
<tr><td>46h</td><td>Security Passthrough</td><td>01h</td><td>4601h</td><td>O</td><td>P</td><td>Security Receive (Section 8.2.10.9.7.2)</td></tr>
<tr><td>47h</td><td>SLD QoS Telemetry</td><td>00h</td><td>4700h</td><td>O</td><td>P</td><td>Get SLD QoS Control (Section 8.2.10.9.8.1)</td></tr>
<tr><td>47h</td><td>SLD QoS Telemetry</td><td>01h</td><td>4701h</td><td>O</td><td>P</td><td>Set SLD QoS Control (Section 8.2.10.9.8.2)</td></tr>
<tr><td>47h</td><td>SLD QoS Telemetry</td><td>02h</td><td>4702h</td><td>O</td><td>P</td><td>Get SLD QoS Status (Section 8.2.10.9.8.3)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>00h</td><td>4800h</td><td>DC</td><td>P</td><td>Get Dynamic Capacity Configuration (Section 8.2.10.9.9.1)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>01h</td><td>4801h</td><td>DC</td><td>P</td><td>Get Dynamic Capacity Extent List (Section 8.2.10.9.9.2)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>02h</td><td>4802h</td><td>DC</td><td>P</td><td>Add Dynamic Capacity Response (Section 8.2.10.9.9.3)</td></tr>
<tr><td>48h</td><td>Dynamic Capacity for LD-FAM</td><td>03h</td><td>4803h</td><td>DC</td><td>P</td><td>Release Dynamic Capacity (Section 8.2.10.9.9.4)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>00h</td><td>4900h</td><td>P</td><td>M</td><td>Identify GFD (Section 8.2.10.9.10.1)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>01h</td><td>4901h</td><td>P</td><td>M</td><td>Get GFD Status (Section 8.2.10.9.10.2)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>02h</td><td>4902h</td><td>P</td><td>M</td><td>Get GFD DC Region Configuration (Section 8.2.10.9.10.3)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>03h</td><td>4903h</td><td>P</td><td>O</td><td>Set GFD DC Region Configuration (Section 8.2.10.9.10.4)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>04h</td><td>4904h</td><td>P</td><td>M</td><td>Get GFD DC Region Extent Lists (Section 8.2.10.9.10.5)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>05h</td><td>4905h</td><td>P</td><td>M</td><td>Get GFD DMP Configuration (Section 8.2.10.9.10.6)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>06h</td><td>4906h</td><td>P</td><td>O</td><td>Set GFD DMP Configuration (Section 8.2.10.9.10.7)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>07h</td><td>4907h</td><td>P</td><td>M</td><td>GFD Dynamic Capacity Add (Section 8.2.10.9.10.8)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>08h</td><td>4908h</td><td>P</td><td>M</td><td>GFD Dynamic Capacity Release (Section 8.2.10.9.10.9)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>09h</td><td>4909h</td><td>P</td><td>O</td><td>GFD Dynamic Capacity Add Reference (Section 8.2.10.9.10.10)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Ah</td><td>490Ah</td><td>P</td><td>O</td><td>GFD Dynamic Capacity Remove Reference (Section 8.2.10.9.10.11)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Bh</td><td>490Bh</td><td>P</td><td>O</td><td>GFD Dynamic Capacity List Tags (Section 8.2.10.9.10.12)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Ch</td><td>490Ch</td><td>P</td><td>M</td><td>Get GFD SAT Entry (Section 8.2.10.9.10.13)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Dh</td><td>490Dh</td><td>P</td><td>M</td><td>Set GFD SAT Entry (Section 8.2.10.9.10.14)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Eh</td><td>490Eh</td><td>P</td><td>M</td><td>Get GFD QoS Control (Section 8.2.10.9.10.15)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>0Fh</td><td>490Fh</td><td>P</td><td>M</td><td>Set GFD QoS Control (Section 8.2.10.9.10.16)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>10h</td><td>4910h</td><td>P</td><td>M</td><td>Get GFD QoS Status (Section 8.2.10.9.10.17)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>11h</td><td>4911h</td><td>P</td><td>M</td><td>Get GFD QoS BW Limit (Section 8.2.10.9.10.18)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>12h</td><td>4912h</td><td>P</td><td>M</td><td>Set GFD QoS BW Limit (Section 8.2.10.9.10.19)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>13h</td><td>4913h</td><td>P</td><td>M</td><td>Get GDT Configuration (Section 8.2.10.9.10.20)</td></tr>
<tr><td>5Bh</td><td>GFD Component Management</td><td>14h</td><td>4914h</td><td>P</td><td>M</td><td>Set GDT Configuration (Section 8.2.10.9.10.21)</td></tr>
</tbody>
</table>

> **Notes | 注释:**
> 1. M = Mandatory(强制);PM = Mandatory for devices that support persistence(支持持久性设备的强制);DC = mandatory for devices that support Dynamic Capacity(支持动态容量设备的强制);O = Optional(可选);P = Prohibited(禁止)。It is prohibited for switches to support any commands from the Memory Device Command Set(交换机禁止支持 Memory Device Command Set 中的任何命令)。
> 2. "FM Interface" refers to commands issued/received via the Fabric Crawl Out mechanism.
> 3. "Host Interface" refers to commands issued/received via the GFD Proxying mechanism.
> 4. Systems capable of management from Mailbox registers and an MCTP-based CCI shall ensure that these commands are not issued as MCTP messages while a device's mailboxes are operational.

> **Figure 8-X.** CXL Defined Memory Device Command Opcodes Sheet 2-3 (page 720-721) ｜ CXL 定义的内存设备命令操作码(续)
>
> <img src="figures/chapter_08/page_0720.png" alt="Figure 8-X page 720" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0720.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-1-1"></a>
### 8.2.10.9.1.1 Identify Memory Device (Opcode 4000h) | 标识内存设备 (操作码 4000h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve basic information about the memory device. If the HDM_Count field in DVSEC CXL Capability is 01b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low (see Section 8.1.3.8.2) is 01b. If the HDM_Count field in DVSEC CXL Capability is 10b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low as well as DVSEC CXL Range 2 Size Low (see Section 8.1.3.8.6) are both 1.</td><td style="background-color:#e8e8e8">检索有关内存设备的基本信息。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 01b,则仅当 DVSEC CXL Range 1 Size Low(参见 8.1.3.8.2 节)中的 Memory_Info_Valid 标志为 01b 时,输出负载才有效。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 10b,则仅当 DVSEC CXL Range 1 Size Low 和 DVSEC CXL Range 2 Size Low(参见 8.1.3.8.6 节)中的 Memory_Info_Valid 标志均为 1 时,输出负载才有效。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> CXL components shall interpret the PCIe MMB Command Opcode Vendor ID = 1E98h or 0000h with CXL defined commands. 0000h is a PCI-SIG reserved value for legacy CXL compatibility. However, it is strongly recommended for callers to use the CXL Vendor ID (1E98h) to identify CXL defined commands.
>
> CXL 组件应使用 CXL 定义命令解释 PCIe MMB Command Opcode Vendor ID = 1E98h 或 0000h。0000h 是 PCI-SIG 为旧版 CXL 兼容性保留的值。但是,强烈建议调用者使用 CXL Vendor ID (1E98h) 来标识 CXL 定义命令。

**Table 8-142. Identify Memory Device Output Payload | Identify Memory Device 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>16</td><td>FW Revision: Contains the revision of the active FW formatted as an ASCII string.</td><td>FW Revision:包含活动 FW 的修订版,格式为 ASCII 字符串。</td></tr>
<tr><td>10h</td><td>8</td><td>Total Capacity: This field indicates the total usable capacity of the device. Expressed in multiples of 256 MB. Total Capacity shall be greater than or equal to the sum of Volatile Only Capacity and Persistent Only Capacity.</td><td>Total Capacity:此字段指示设备的总可用容量。以 256 MB 的倍数表示。Total Capacity 应大于或等于 Volatile Only Capacity 和 Persistent Only Capacity 之和。</td></tr>
<tr><td>18h</td><td>8</td><td>Volatile Only Capacity: This field indicates the total usable capacity of the device that may be used only as volatile memory. Expressed in multiples of 256 MB.</td><td>Volatile Only Capacity:此字段指示设备可用作易失性内存的总可用容量。以 256 MB 的倍数表示。</td></tr>
<tr><td>20h</td><td>8</td><td>Persistent Only Capacity: This field indicates the total usable capacity of the device that may be used only as persistent memory. Expressed in multiples of 256 MB.</td><td>Persistent Only Capacity:此字段指示设备可用作持久性内存的总可用容量。以 256 MB 的倍数表示。</td></tr>
<tr><td>28h</td><td>8</td><td>Partition Alignment: If the device has capacity that may be used as either volatile memory or persistent memory, this field indicates the partition alignment size. Expressed in multiples of 256 MB. Partitionable capacity is equal to Total Capacity - Volatile Only Capacity - Persistent Only Capacity. If 0, the device doesn't support partitioning the capacity into both volatile capacity and persistent capacity.</td><td>Partition Alignment:如果设备具有可用作易失性内存或持久性内存的容量,则此字段指示分区对齐大小。以 256 MB 的倍数表示。可分区容量等于 Total Capacity - Volatile Only Capacity - Persistent Only Capacity。如果为 0,则设备不支持将容量分区为易失性容量和持久性容量。</td></tr>
<tr><td>30h</td><td>2</td><td>Informational Event Log Size: The number of events that the device can store in the Informational Event Log before the log overflows.</td><td>Informational Event Log Size:设备在日志溢出之前可以在 Informational Event Log 中存储的事件数。</td></tr>
<tr><td>32h</td><td>2</td><td>Warning Event Log Size: The number of events that the device can store in the Warning Event Log before the log overflows.</td><td>Warning Event Log Size:设备在日志溢出之前可以在 Warning Event Log 中存储的事件数。</td></tr>
<tr><td>34h</td><td>2</td><td>Failure Event Log Size: The number of events that the device can store in the Failure Event Log before the log overflows.</td><td>Failure Event Log Size:设备在日志溢出之前可以在 Failure Event Log 中存储的事件数。</td></tr>
<tr><td>36h</td><td>2</td><td>Fatal Event Log Size: The number of events that the device can store in the Fatal Event Log before the log overflows.</td><td>Fatal Event Log Size:设备在日志溢出之前可以在 Fatal Event Log 中存储的事件数。</td></tr>
<tr><td>38h</td><td>4</td><td>LSA Size: The size of the Label Storage Area. Expressed in bytes.</td><td>LSA Size:Label Storage Area 的大小。以字节为单位表示。</td></tr>
<tr><td>3Ch</td><td>3</td><td>Poison List Maximum Media Error Records: The maximum number of Media Error Records that the device can track in its Poison List.</td><td>Poison List Maximum Media Error Records:设备可以在其 Poison List 中跟踪的最大 Media Error Records 数。</td></tr>
<tr><td>3Fh</td><td>2</td><td>Inject Poison Limit: The device's supported maximum number of physical addresses that can be poisoned by the Inject Poison command. When 0, the device does not have a poison injection limit. When nonzero, the device has a maximum limit of poison that can be injected using the Inject Poison command.</td><td>Inject Poison Limit:设备支持的可由 Inject Poison 命令注入 poison 的最大物理地址数。当为 0 时,设备没有 poison 注入限制。当非零时,设备具有可使用 Inject Poison 命令注入的最大 poison 限制。</td></tr>
<tr><td>41h</td><td>1</td><td>Poison Handling Capabilities<br>• Bit[0]: Injects Persistent Poison: When set and the device supports poison injection, any poison injected in non-volatile DPA shall remain persistent across all types of device resets. When cleared and the device supports poison injection, Conventional or CXL Reset shall automatically clear the injected poison.<br>• Bit[1]: Scans for Poison: When set, the device shall periodically scan its media for errors and shall automatically alert the host of those errors. If cleared, the device does not periodically scan for memory errors and does not generate an alert.<br>• Bits[7:2]: Reserved.</td><td>Poison Handling Capabilities<br>• Bit[0]:Injects Persistent Poison:当设置且设备支持 poison 注入时,在非易失性 DPA 中注入的任何 poison 应在所有类型的设备复位后保持持久性。当清除且设备支持 poison 注入时,Conventional 或 CXL Reset 应自动清除注入的 poison。<br>• Bit[1]:Scans for Poison:当设置时,设备应定期扫描其介质以查找错误,并应自动将这些错误警报通知主机。如果清除,设备不定期扫描内存错误,也不生成警报。<br>• Bits[7:2]:保留。</td></tr>
<tr><td>42h</td><td>1</td><td>QoS Telemetry Capabilities<br>• Bit[0]: Egress Port Congestion Supported<br>• Bit[1]: Temporary Throughput Reduction Supported<br>• Bits[7:2]: Reserved</td><td>QoS Telemetry Capabilities<br>• Bit[0]:支持 Egress Port Congestion<br>• Bit[1]:支持 Temporary Throughput Reduction<br>• Bits[7:2]:保留</td></tr>
<tr><td>43h</td><td>2</td><td>Dynamic Capacity Event Log Size: The number of events that the device can store in the Dynamic Capacity Event Log before the log overflows.</td><td>Dynamic Capacity Event Log Size:设备在日志溢出之前可以在 Dynamic Capacity Event Log 中存储的事件数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Identify Memory Device Output Payload (page 722-723) ｜ Identify Memory Device 输出负载
>
> <img src="figures/chapter_08/page_0722.png" alt="Figure 8-X page 722" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0722.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-1"></a>
### 8.2.10.9.2.1 Get Partition Info (Opcode 4100h) | 获取分区信息 (操作码 4100h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get the Active and Next capacity settings for a memory device, describing the amount of volatile and persistent memory capacities available. The Active values describe the current capacities provided by the device in the currently active configuration. The Next values describe a new configuration that has not yet taken effect, to become active on the next reset (as specified in the Set Partition command effects). If the HDM_Count field in DVSEC CXL Capability is 01b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low (see Section 8.1.3.8.2) is 01b.</td><td style="background-color:#e8e8e8">获取内存设备的 Active 和 Next 容量设置,描述可用的易失性和持久性内存容量。Active 值描述设备在当前活动配置中提供的当前容量。Next 值描述尚未生效的新配置,将在下次复位时生效(如 Set Partition 命令效果中所指定)。如果 DVSEC CXL Capability 中的 HDM_Count 字段为 01b,则仅当 DVSEC CXL Range 1 Size Low(参见 8.1.3.8.2 节)中的 Memory_Info_Valid 标志为 01b 时,输出负载才有效。</td></tr>
<tr><td>If the HDM_Count field in DVSEC CXL Capability is 10b, the output payload is valid only if the Memory_Info_Valid flag in DVSEC CXL Range 1 Size Low as well as DVSEC CXL Range 2 Size Low (see Section 8.1.3.8.6) are both 1.</td><td style="background-color:#e8e8e8">如果 DVSEC CXL Capability 中的 HDM_Count 字段为 10b,则仅当 DVSEC CXL Range 1 Size Low 和 DVSEC CXL Range 2 Size Low(参见 8.1.3.8.6 节)中的 Memory_Info_Valid 标志均为 1 时,输出负载才有效。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-143. Get Partition Info Output Payload | Get Partition Info 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Active Volatile Capacity: Total device volatile memory capacity in multiples of 256 MB. This is the sum of the device's Volatile Only capacity and the capacity that is partitioned for volatile use. The device shall provide this volatile capacity starting at DPA 0.</td><td>Active Volatile Capacity:设备易失性内存总容量(以 256 MB 的倍数表示)。这是设备的 Volatile Only 容量和分区用于易失性使用的容量之和。设备应从 DPA 0 开始提供此易失性容量。</td></tr>
<tr><td>08h</td><td>8</td><td>Active Persistent Capacity: Total device persistent memory capacity in multiples of 256 MB. This is the sum of the device's Persistent Only capacity and the capacity that is partitioned for persistent use. The device shall provide this persistent capacity starting at the DPA immediately following the volatile capacity.</td><td>Active Persistent Capacity:设备持久性内存总容量(以 256 MB 的倍数表示)。这是设备的 Persistent Only 容量和分区用于持久性使用的容量之和。设备应从紧跟易失性容量之后的 DPA 开始提供此持久性容量。</td></tr>
<tr><td>10h</td><td>8</td><td>Next Volatile Capacity: If nonzero, this value shall become the Active Volatile Capacity on the next reset (as specified in the Set Partition command effects). If both this field and the Next Persistent Capacity field are 0, there is no pending change to the partitioning.</td><td>Next Volatile Capacity:如果非零,此值应在下次复位时成为 Active Volatile Capacity(如 Set Partition 命令效果中所指定)。如果此字段和 Next Persistent Capacity 字段均为 0,则没有待处理的分区更改。</td></tr>
<tr><td>18h</td><td>8</td><td>Next Persistent Capacity: If nonzero, this value shall become the Active Persistent Capacity on the next reset (as specified in the Set Partition command effects). If both this field and the Next Volatile Capacity field are 0, there is no pending change to the partitioning.</td><td>Next Persistent Capacity:如果非零,此值应在下次复位时成为 Active Persistent Capacity(如 Set Partition 命令效果中所指定)。如果此字段和 Next Volatile Capacity 字段均为 0,则没有待处理的分区更改。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Partition Info (page 724) ｜ Get Partition Info
>
> <img src="figures/chapter_08/page_0724.png" alt="Figure 8-X page 724" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0724.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-2"></a>
### 8.2.10.9.2.2 Set Partition Info (Opcode 4101h) | 设置分区信息 (操作码 4101h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Set the partitioning between volatile capacity and persistent capacity for the partitionable capacity. Partitionable capacity is equal to (Total Capacity - Volatile Only Capacity - Persistent Only Capacity). This command shall fail with an Unsupported error if there is no partitionable capacity (i.e., Identify Memory Device reports Partition Alignment as zero). The device shall return Invalid Input if the specified capacity is not aligned to the partition alignment requirement reported in the Identify Memory Device command. Using this command to change the size of the persistent capacity shall result in the loss of data stored.</td><td style="background-color:#e8e8e8">为可分区容量设置易失性容量和持久性容量之间的分区。可分区容量等于(Total Capacity - Volatile Only Capacity - Persistent Only Capacity)。如果没有可分区容量(即,Identify Memory Device 报告 Partition Alignment 为零),此命令应以 Unsupported 错误失败。如果指定的容量与 Identify Memory Device 命令中报告的分区对齐要求不一致,设备应返回 Invalid Input。使用此命令更改持久性容量的大小将导致存储的数据丢失。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to change the partitioning of the device with the Immediate flag set by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何设置 Immediate 标志的更改设备分区的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Configuration Change after Cold Reset<br>• CEL[11:10] Valid<br>• Configuration Change after Conventional Reset<br>• Configuration Change after CXL Reset<br>• Immediate Configuration Change<br>• Immediate Data Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Cold Reset 后的配置更改<br>• CEL[11:10] 有效<br>• Conventional Reset 后的配置更改<br>• CXL Reset 后的配置更改<br>• 立即配置更改<br>• 立即数据更改</td></tr>
</tbody>
</table>

**Table 8-144. Set Partition Info Input Payload | Set Partition Info 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Volatile Capacity: The amount of partitionable capacity that shall be allocated to volatile capacity, in multiples of 256 MB aligned to the partition alignment requirement reported in the Identify Memory Device command. The remainder of the partitionable capacity shall be allocated to persistent capacity.</td><td>Volatile Capacity:应分配给易失性容量的可分区容量大小(以 256 MB 的倍数表示),并与 Identify Memory Device 命令中报告的分区对齐要求对齐。可分区容量的其余部分应分配给持久性容量。</td></tr>
<tr><td>08h</td><td>1</td><td>Flags<br>• Bit[0]: Immediate: When set, the change is immediately requested. If cleared, the change in partitioning shall become the "next" configuration, to become active on the next reset (as specified in the command effects). In this case, the new configuration shall be reported in the Next Volatile Capacity and Next Persistent Capacity fields returned by the Get Partition Info command. It is the caller's responsibility to avoid immediate changes to the partitioning when the device is in use.<br>• Bits[7:1]: Reserved.</td><td>标志位<br>• Bit[0]:Immediate:当设置时,立即请求更改。如果清除,分区的更改将成为 "next" 配置,在下次复位时生效(如命令效果中所指定)。在这种情况下,新配置应在 Get Partition Info 命令返回的 Next Volatile Capacity 和 Next Persistent Capacity 字段中报告。调用者有责任在设备使用时避免对分区的立即更改。<br>• Bits[7:1]:保留。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Set Partition Info (page 725) ｜ Set Partition Info
>
> <img src="figures/chapter_08/page_0725.png" alt="Figure 8-X page 725" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0725.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-3"></a>
### 8.2.10.9.2.3 Get LSA (Opcode 4102h) | 获取 LSA (操作码 4102h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Label Storage Area (LSA) shall be supported by a memory device that provides persistent memory capacity and may be supported by a device that provides only volatile memory capacity. The format of the LSA is specified in Section 9.13.2. The size of the Label Storage Area is retrieved from the Identify Memory Device command.</td><td style="background-color:#e8e8e8">提供持久性内存容量的内存设备应支持 Label Storage Area (LSA),并且可以由仅提供易失性内存容量的设备支持。LSA 的格式在 9.13.2 节中指定。Label Storage Area 的大小是从 Identify Memory Device 命令检索的。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-145. Get LSA Input Payload | Get LSA 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Offset: The byte offset in the LSA to return in the output payload.</td><td>Offset:在 LSA 中返回到输出负载的字节偏移量。</td></tr>
<tr><td>04h</td><td>4</td><td>Length: Length in bytes of LSA to return in the output payload.</td><td>Length:输出负载中返回的 LSA 的字节长度。</td></tr>
</tbody>
</table>

**Table 8-146. Get LSA Output Payload | Get LSA 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>Varies</td><td>Data: Requested bytes from the LSA.</td><td>Data:来自 LSA 的请求字节。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-2-4"></a>
### 8.2.10.9.2.4 Set LSA (Opcode 4103h) | 设置 LSA (操作码 4103h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The format of the Label Storage Area is specified in Section 9.13.2.</td><td style="background-color:#e8e8e8">Label Storage Area 的格式在 9.13.2 节中指定。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Configuration Change<br>• Immediate Data Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• 立即配置更改<br>• 立即数据更改</td></tr>
</tbody>
</table>

**Table 8-147. Set LSA Input Payload | Set LSA 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Offset: The byte offset in the LSA.</td><td>Offset:LSA 中的字节偏移量。</td></tr>
<tr><td>04h</td><td>4</td><td>Reserved</td><td>保留</td></tr>
<tr><td>08h</td><td>Varies</td><td>Data: The data to be written to LSA at the specified offset.</td><td>Data:要在指定偏移量处写入 LSA 的数据。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get LSA / Set LSA (page 726) ｜ Get LSA / Set LSA
>
> <img src="figures/chapter_08/page_0726.png" alt="Figure 8-X page 726" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0726.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-1"></a>
### 8.2.10.9.3.1 Get Health Info (Opcode 4200h) | 获取健康信息 (操作码 4200h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get the current instantaneous health of the device. It is not necessary to poll for health changes. Anytime the health of the device changes, the device shall add an appropriate event to its internal event log, update the Event Status register, and if configured, interrupt the host.</td><td style="background-color:#e8e8e8">获取设备当前的瞬时健康状态。不需要轮询健康变化。每当设备的健康状态发生变化时,设备应将适当的事件添加到其内部事件日志,更新 Event Status 寄存器,并在配置时中断主机。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-148. Get Health Info Output Payload | Get Health Info 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Health Status: Overall device health summary. Normal health status is all bits cleared.<br>• Bit[0]: Maintenance Needed<br>• Bit[1]: Performance Degraded<br>• Bit[2]: Hardware Replacement Needed<br>• Bit[3]: Memory Capacity Degraded<br>• Bits[7:4]: Reserved</td><td>Health Status:设备整体健康摘要。正常的健康状态是所有位都清零。<br>• Bit[0]:Maintenance Needed(需要维护)<br>• Bit[1]:Performance Degraded(性能降级)<br>• Bit[2]:Hardware Replacement Needed(需要更换硬件)<br>• Bit[3]:Memory Capacity Degraded(内存容量降级)<br>• Bits[7:4]:保留</td></tr>
<tr><td>01h</td><td>1</td><td>Media Status: Overall media health summary.<br>• 00h = Normal. The device's media is operating normally.<br>• 01h = Not Ready. The device's media is not ready.<br>• 02h = Write persistency Lost. The device cannot persist write requests but is able to read stored data.<br>• 03h = All data lost. All data has been lost from the device.<br>• 04h = Write Persistency Loss in the Event of Power Loss<br>• 05h = Write Persistency Loss in Event of Shutdown<br>• 06h = Write Persistency Loss Imminent<br>• 07h = All Data Loss in the Event of Power Loss<br>• 08h = All Data Loss in the Event of Shutdown<br>• 09h = All Data Loss Imminent<br>• All other encodings are reserved.</td><td>Media Status:介质整体健康摘要。<br>• 00h = Normal。设备的介质正常运行。<br>• 01h = Not Ready。设备的介质未就绪。<br>• 02h = Write persistency Lost。设备无法持久化写入请求,但能够读取存储的数据。<br>• 03h = All data lost。设备上的所有数据都已丢失。<br>• 04h = 断电时写入持久性丢失<br>• 05h = 关闭时写入持久性丢失<br>• 06h = 即将丢失写入持久性<br>• 07h = 断电时所有数据丢失<br>• 08h = 关闭时所有数据丢失<br>• 09h = 即将丢失所有数据<br>• 所有其他编码保留。</td></tr>
<tr><td>02h</td><td>1</td><td>Additional Status<br>• Bits[1:0]: Life Used: 00b = Normal; 01b = Warning; 10b = Critical; 11b = Reserved.<br>• Bits[3:2]: Device Temperature: 00b = Normal; 01b = Warning; 10b = Critical; 11b = Reserved.<br>• Bit[4]: Corrected Volatile Error Count: 0 = Normal; 1 = Warning or Failure.<br>• Bit[5]: Corrected Persistent Error Count: 0 = Normal; 1 = Warning.<br>• Bits[7:6]: Reserved.</td><td>Additional Status<br>• Bits[1:0]:Life Used(已使用寿命):00b = 正常;01b = 警告;10b = 严重;11b = 保留。<br>• Bits[3:2]:Device Temperature(设备温度):00b = 正常;01b = 警告;10b = 严重;11b = 保留。<br>• Bit[4]:Corrected Volatile Error Count(已纠正易失性错误计数):0 = 正常;1 = 警告或故障。<br>• Bit[5]:Corrected Persistent Error Count(已纠正持久性错误计数):0 = 正常;1 = 警告。<br>• Bits[7:6]:保留。</td></tr>
<tr><td>03h</td><td>1</td><td>Life Used: The device's used life as a percentage value (0-100) of factory-expected life span. Returns FFh if not implemented.</td><td>Life Used(已使用寿命):设备的已使用寿命,占出厂预期寿命的百分比值(0-100)。如果未实现,则返回 FFh。</td></tr>
<tr><td>04h</td><td>2</td><td>Device Temperature: The device's current temperature in degrees Celsius, represented as a 2's complement value. Returns 7FFFh if not implemented.</td><td>Device Temperature(设备温度):设备的当前温度(以摄氏度为单位),表示为 2 的补码值。如果未实现,则返回 7FFFh。</td></tr>
<tr><td>06h</td><td>4</td><td>Dirty Shutdown Count: A monotonically increasing counter that is incremented whenever the device fails to save and/or flush data to the persistent media or is unable to determine whether data loss may have occurred. The count is persistent across power loss and wraps back to 0 at overflow.</td><td>Dirty Shutdown Count(脏关机计数):单调递增的计数器,每当设备无法将数据保存和/或刷新到持久性介质,或无法确定是否可能发生数据丢失时,计数器递增。计数在断电后保留,并在溢出时回绕到 0。</td></tr>
<tr><td>0Ah</td><td>4</td><td>Corrected Volatile Error Count: The total number of correctable memory errors that the device has detected as having occurred in the volatile memory partition.</td><td>Corrected Volatile Error Count(已纠正易失性错误计数):设备检测到的在易失性内存分区中发生的可纠正内存错误总数。</td></tr>
<tr><td>0Eh</td><td>4</td><td>Corrected Persistent Error Count: The total number of correctable memory errors that the device has detected as having occurred in the persistent memory partition.</td><td>Corrected Persistent Error Count(已纠正持久性错误计数):设备检测到的在持久性内存分区中发生的可纠正内存错误总数。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Health Info Output Payload (page 727-728) ｜ Get Health Info 输出负载
>
> <img src="figures/chapter_08/page_0727.png" alt="Figure 8-X page 727" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0727.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-2"></a>
### 8.2.10.9.3.2 Get Alert Configuration (Opcode 4201h) | 获取警报配置 (操作码 4201h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Retrieve the device's critical alert and programmable warning configuration. Critical alerts shall automatically be configured by the device after a Conventional Reset. If supported, programmable warning thresholds shall be initialized to vendor-recommended defaults by the device on a Conventional Reset.</td><td style="background-color:#e8e8e8">检索设备的关键警报和可编程警告配置。关键警报应在 Conventional Reset 后由设备自动配置。如果支持,可编程警告阈值应在 Conventional Reset 时由设备初始化为厂商推荐的默认值。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-149. Get Alert Configuration Output Payload | Get Alert Configuration 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Valid Alerts: Indicators of which alert fields are valid in the returned data.<br>• Bit[0]: When set, the Life Used Programmable Warning Threshold field is valid<br>• Bit[1]: When set, the Device Over-Temperature Programmable Warning Threshold field is valid<br>• Bit[2]: When set, the Device Under-Temperature Programmable Warning Threshold field is valid<br>• Bit[3]: When set, the Corrected Volatile Memory Error Programmable Warning Threshold field is valid<br>• Bit[4]: When set, the Corrected Persistent Memory Error Programmable Warning Threshold field is valid<br>• Bits[7:5]: Reserved</td><td>Valid Alerts(有效警报):返回数据中哪些警报字段有效的指示符。<br>• Bit[0]:当设置时,Life Used Programmable Warning Threshold 字段有效<br>• Bit[1]:当设置时,Device Over-Temperature Programmable Warning Threshold 字段有效<br>• Bit[2]:当设置时,Device Under-Temperature Programmable Warning Threshold 字段有效<br>• Bit[3]:当设置时,Corrected Volatile Memory Error Programmable Warning Threshold 字段有效<br>• Bit[4]:当设置时,Corrected Persistent Memory Error Programmable Warning Threshold 字段有效<br>• Bits[7:5]:保留</td></tr>
<tr><td>01h</td><td>1</td><td>Programmable Alerts: Indicators of which device alerts are programmable by the host.<br>• Bit[0]: When set, the Life Used Programmable Warning Threshold is programmable by the host<br>• Bit[1]: When set, the Device Over-Temperature Programmable Warning Threshold field is programmable by the host<br>• Bit[2]: When set, the Device Under-Temperature Programmable Warning Threshold field is programmable by the host<br>• Bit[3]: When set, the Corrected Volatile Memory Error Programmable Warning is programmable by the host<br>• Bit[4]: When set, the Corrected Persistent Memory Error Programmable Warning is programmable by the host<br>• Bits[7:5]: Reserved</td><td>Programmable Alerts(可编程警报):主机可编程哪些设备警报的指示符。<br>• Bit[0]:当设置时,Life Used Programmable Warning Threshold 可由主机编程<br>• Bit[1]:当设置时,Device Over-Temperature Programmable Warning Threshold 字段可由主机编程<br>• Bit[2]:当设置时,Device Under-Temperature Programmable Warning Threshold 字段可由主机编程<br>• Bit[3]:当设置时,Corrected Volatile Memory Error Programmable Warning 可由主机编程<br>• Bit[4]:当设置时,Corrected Persistent Memory Error Programmable Warning 可由主机编程<br>• Bits[7:5]:保留</td></tr>
<tr><td>02h</td><td>1</td><td>Life Used Critical Alert Threshold: The device's default alert when the Life Used rises above this percentage-based value. Valid values are 0-100.</td><td>Life Used Critical Alert Threshold(Life Used 关键警报阈值):当 Life Used 超过此基于百分比的值时,设备的默认警报。有效值为 0-100。</td></tr>
<tr><td>03h</td><td>1</td><td>Life Used Programmable Warning Threshold: The device's currently programmed warning threshold when the life used rises to or above this percentage-based value. Valid values are 0-100. The life used warning threshold shall be less than the life used critical alert value.</td><td>Life Used Programmable Warning Threshold(Life Used 可编程警告阈值):当已使用寿命达到或超过此基于百分比的值时,设备当前编程的警告阈值。有效值为 0-100。Life used 警告阈值应小于 Life used 关键警报值。</td></tr>
<tr><td>04h</td><td>2</td><td>Device Over-Temperature Critical Alert Threshold: The device's default critical over-temperature alert threshold when the device temperature rises to or above this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Over-Temperature Critical Alert Threshold(设备过温关键警报阈值):当设备温度达到或超过此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备的默认关键过温警报阈值。</td></tr>
<tr><td>06h</td><td>2</td><td>Device Under-Temperature Critical Alert Threshold: The device's default critical under-temperature alert threshold when the device temperature falls to or below this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Under-Temperature Critical Alert Threshold(设备低温关键警报阈值):当设备温度降至或低于此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备的默认关键低温警报阈值。</td></tr>
<tr><td>08h</td><td>2</td><td>Device Over-Temperature Programmable Warning Threshold: The device's currently programmed over-temperature warning threshold when the device temperature rises to or above this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Over-Temperature Programmable Warning Threshold(设备过温可编程警告阈值):当设备温度达到或超过此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备当前编程的过温警告阈值。</td></tr>
<tr><td>0Ah</td><td>2</td><td>Device Under-Temperature Programmable Warning Threshold: The device's currently programmed under-temperature warning threshold when the device temperature falls to or below this threshold in degrees Celsius, represented as a 2's complement value.</td><td>Device Under-Temperature Programmable Warning Threshold(设备低温可编程警告阈值):当设备温度降至或低于此阈值(以摄氏度为单位,表示为 2 的补码值)时,设备当前编程的低温警告阈值。</td></tr>
<tr><td>0Ch</td><td>2</td><td>Corrected Volatile Memory Error Programmable Warning Threshold: The device's currently programmed warning threshold for corrected volatile memory errors before signaling a corrected error event to the host.</td><td>Corrected Volatile Memory Error Programmable Warning Threshold(已纠正易失性内存错误可编程警告阈值):在向主机发出已纠正错误事件之前,设备当前编程的已纠正易失性内存错误警告阈值。</td></tr>
<tr><td>0Eh</td><td>2</td><td>Corrected Persistent Memory Error Programmable Warning Threshold: The device's currently programmed warning threshold for corrected persistent memory errors before signaling a corrected error event to the host.</td><td>Corrected Persistent Memory Error Programmable Warning Threshold(已纠正持久性内存错误可编程警告阈值):在向主机发出已纠正错误事件之前,设备当前编程的已纠正持久性内存错误警告阈值。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Alert Configuration (page 729-730) ｜ Get Alert Configuration
>
> <img src="figures/chapter_08/page_0729.png" alt="Figure 8-X page 729" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0729.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-3"></a>
### 8.2.10.9.3.3 Set Alert Configuration (Opcode 4202h) | 设置警报配置 (操作码 4202h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Set Alert Configuration allows the host to configure programmable warning thresholds optionally. If supported, programmable warning thresholds shall be initialized to vendor-recommended defaults by the device on a Conventional Reset. After completion of this command, the requested programmable warning thresholds shall replace any previously programmed warning thresholds.</td><td style="background-color:#e8e8e8">Set Alert Configuration 允许主机选择性地配置可编程警告阈值。如果支持,可编程警告阈值应在 Conventional Reset 时由设备初始化为厂商推荐的默认值。此命令完成后,请求的可编程警告阈值应替换任何先前编程的警告阈值。</td></tr>
<tr><td>Any time a programmed warning threshold is reached, the device shall add an appropriate event record to its event log, update the Event Status register, and if configured, interrupt the host. If the conditions are already met for the newly programmed warning at the time this command is executed, the device shall immediately generate the event record and interrupt for the alert.</td><td style="background-color:#e8e8e8">每当达到编程的警告阈值时,设备应将适当的事件记录添加到其事件日志,更新 Event Status 寄存器,并在配置时中断主机。如果在执行此命令时已满足新编程的警告条件,则设备应立即生成事件记录并中断警报。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Policy Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Policy Change(立即策略更改)</td></tr>
</tbody>
</table>

**Table 8-150. Set Alert Configuration Input Payload | Set Alert Configuration 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Valid Alert Actions: Indicators of which alert fields are valid in the supplied input payload.<br>• Bit[0]: When set, the Life Used Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[1]: When set, the Device Over-Temperature Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[2]: When set, the Device Under-Temperature Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[3]: When set, the Corrected Volatile Memory Error Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bit[4]: When set, the Corrected Persistent Memory Error Programmable Warning Threshold Enable Alert Action and field shall be valid<br>• Bits[7:5]: Reserved</td><td>Valid Alert Actions(有效警报操作):提供的输入负载中哪些警报字段有效的指示符。<br>• Bit[0]:当设置时,Life Used Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[1]:当设置时,Device Over-Temperature Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[2]:当设置时,Device Under-Temperature Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[3]:当设置时,Corrected Volatile Memory Error Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bit[4]:当设置时,Corrected Persistent Memory Error Programmable Warning Threshold Enable Alert Action 和字段应有效<br>• Bits[7:5]:保留</td></tr>
<tr><td>01h</td><td>1</td><td>Enable Alert Actions: The device shall enable the following programmable alerts.<br>• Bit[0]: When set, the device shall enable its Life Used Programmable Warning Threshold.<br>• Bit[1]: When set, the device shall enable its Device Over-Temperature Programmable Warning Threshold.<br>• Bit[2]: When set, the device shall enable its Device Under-Temperature Programmable Warning Threshold.<br>• Bit[3]: When set, the device shall enable its Corrected Volatile Memory Error Programmable Warning Threshold.<br>• Bit[4]: When set, the device shall enable its Corrected Persistent Memory Error Programmable Warning Threshold.<br>• Bits[7:5]: Reserved.</td><td>Enable Alert Actions(启用警报操作):设备应启用以下可编程警报。<br>• Bit[0]:当设置时,设备应启用其 Life Used Programmable Warning Threshold。<br>• Bit[1]:当设置时,设备应启用其 Device Over-Temperature Programmable Warning Threshold。<br>• Bit[2]:当设置时,设备应启用其 Device Under-Temperature Programmable Warning Threshold。<br>• Bit[3]:当设置时,设备应启用其 Corrected Volatile Memory Error Programmable Warning Threshold。<br>• Bit[4]:当设置时,设备应启用其 Corrected Persistent Memory Error Programmable Warning Threshold。<br>• Bits[7:5]:保留。</td></tr>
<tr><td>02h</td><td>1</td><td>Life Used Programmable Warning Threshold: The device's updated life used programmable warning threshold.</td><td>Life Used Programmable Warning Threshold:设备更新的 Life Used 可编程警告阈值。</td></tr>
<tr><td>03h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>04h</td><td>2</td><td>Device Over-Temperature Programmable Warning Threshold: The device's updated Over-Temperature programmable warning threshold.</td><td>Device Over-Temperature Programmable Warning Threshold:设备更新的过温可编程警告阈值。</td></tr>
<tr><td>06h</td><td>2</td><td>Device Under-Temperature Programmable Warning Threshold: The device's updated Under-Temperature programmable warning threshold.</td><td>Device Under-Temperature Programmable Warning Threshold:设备更新的低温可编程警告阈值。</td></tr>
<tr><td>08h</td><td>2</td><td>Corrected Volatile Memory Error Programmable Warning Threshold: The device's updated programmable warning threshold for corrected volatile memory errors.</td><td>Corrected Volatile Memory Error Programmable Warning Threshold:设备更新的已纠正易失性内存错误可编程警告阈值。</td></tr>
<tr><td>0Ah</td><td>2</td><td>Corrected Persistent Memory Error Programmable Warning Threshold: The device's updated programmable warning threshold for corrected persistent memory errors.</td><td>Corrected Persistent Memory Error Programmable Warning Threshold:设备更新的已纠正持久性内存错误可编程警告阈值。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Set Alert Configuration (page 731) ｜ Set Alert Configuration
>
> <img src="figures/chapter_08/page_0731.png" alt="Figure 8-X page 731" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0731.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-4"></a>
### 8.2.10.9.3.4 Get Shutdown State (Opcode 4203h) | 获取关闭状态 (操作码 4203h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-151. Get Shutdown State Output Payload | Get Shutdown State 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>State: The current Shutdown State.<br>• Bit[0]: Dirty: A 1 value indicates the device's internal Shutdown State is "dirty". A 0 value indicates "clean".<br>• Bits[7:1]: Reserved.</td><td>State:当前 Shutdown State。<br>• Bit[0]:Dirty(脏):值 1 表示设备的内部 Shutdown State 为 "dirty"。值 0 表示 "clean"。<br>• Bits[7:1]:保留。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-3-5"></a>
### 8.2.10.9.3.5 Set Shutdown State (Opcode 4204h) | 设置关闭状态 (操作码 4204h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Policy Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Policy Change(立即策略更改)</td></tr>
</tbody>
</table>

**Table 8-152. Set Shutdown State Input Payload | Set Shutdown State 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>State: The current Shutdown State.<br>• Bit[0]: Dirty: A 1 value sets the device's internal Shutdown State to "dirty". A 0 value sets it to "clean". The device shall persistently store this state and use it after the next Conventional Reset to determine whether the Dirty Shutdown Count described in Section 8.2.10.9.3.1 gets updated. If the Shutdown State is "dirty", the device shall increment the Dirty Shutdown Count and then set the Shutdown State to "clean". This post-reset logic shall occur before the device accepts any commands or memory I/O. The value set by this mailbox command shall be overridden by the device in two cases:<br>  — On a successful GPF flow, the device shall set the Shutdown State to "clean"<br>  — When handling a shutdown/reset, if the device detects an internal failure that jeopardizes data integrity (e.g., a failed internal flush), the device shall set the Shutdown State to "dirty"<br>• Bits[7:1]: Reserved</td><td>State:当前 Shutdown State。<br>• Bit[0]:Dirty(脏):值 1 将设备的内部 Shutdown State 设置为 "dirty"。值 0 将其设置为 "clean"。设备应持续存储此状态,并在下一次 Conventional Reset 后使用它来确定是否更新 8.2.10.9.3.1 节中描述的 Dirty Shutdown Count。如果 Shutdown State 为 "dirty",设备应增加 Dirty Shutdown Count,然后将 Shutdown State 设置为 "clean"。此复位后逻辑应在设备接受任何命令或内存 I/O 之前发生。此邮箱命令设置的值将在两种情况下被设备覆盖:<br>  — 在成功的 GPF 流程中,设备应将 Shutdown State 设置为 "clean"<br>  — 在处理关闭/复位时,如果设备检测到危及数据完整性的内部故障(例如,内部刷新失败),设备应将 Shutdown State 设置为 "dirty"<br>• Bits[7:1]:保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get/Set Shutdown State (page 732) ｜ Get/Set Shutdown State
>
> <img src="figures/chapter_08/page_0732.png" alt="Figure 8-X page 732" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0732.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-1"></a>
### 8.2.10.9.4.1 Get Poison List (Opcode 4300h) | 获取 Poison List (操作码 4300h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get Poison List command shall return an unordered list of locations that are poisoned or result in poison if the addresses were accessed by the host. This command is not a background operation and the device shall return data without delay. The device may reject this command if the requested range spans the device's volatile and persistent partitions.</td><td style="background-color:#e8e8e8">Get Poison List 命令应返回主机访问时已 poison 或导致 poison 的位置的无序列表。此命令不是后台操作,设备应无延迟地返回数据。如果请求的范围跨越设备的易失性和持久性分区,设备可以拒绝此命令。</td></tr>
<tr><td>The device shall return the known list of locations with media errors for the requested address range when the device processes the command. Any time that the device detects a new poisoned location, the device shall add the DPA to the Poison List, add an appropriate event to its Warning, Informational, or Failure Event Log, update the Event Status register, and if configured, interrupt the host. In response, the host should reissue this command to retrieve the updated Poison List.</td><td style="background-color:#e8e8e8">设备应在处理命令时返回所请求地址范围内具有介质错误的已知位置列表。每当设备检测到新的 poison 位置时,设备应将 DPA 添加到 Poison List,将适当的事件添加到其 Warning、Informational 或 Failure Event Log,更新 Event Status 寄存器,并在配置时中断主机。作为响应,主机应重新发出此命令以检索更新的 Poison List。</td></tr>
<tr><td>When poison is written:<br>• Using CXL.mem: The device shall add the new DPA to the device's Poison List and then shall set the error source to an external error.<br>• Using a CXL-defined poison injection interface (e.g., Inject Poison command): The device shall add the new DPA to the device's Poison List and then shall set the error source to an injected error.<br>• By the device because of a device-detected internal error (e.g., device media scrub discovers new media error): The device shall add the new DPA to the device's Poison List and then shall set the error source to an internal error.</td><td style="background-color:#e8e8e8">当写入 poison 时:<br>• 使用 CXL.mem:设备应将新的 DPA 添加到设备的 Poison List,然后将错误源设置为外部错误。<br>• 使用 CXL 定义的 poison 注入接口(例如,Inject Poison 命令):设备应将新的 DPA 添加到设备的 Poison List,然后将错误源设置为注入错误。<br>• 由设备由于设备检测到的内部错误(例如,设备介质扫描发现新的介质错误):设备应将新的 DPA 添加到设备的 Poison List,然后将错误源设置为内部错误。</td></tr>
<tr><td>When poison is cleared, the DPA shall no longer be reported in the device's Poison List.</td><td style="background-color:#e8e8e8">当 poison 被清除时,DPA 将不再在设备的 Poison List 中报告。</td></tr>
<tr><td>If the device does not support poison list for volatile ranges and any location in the requested list maps to volatile, the device shall return Invalid Physical Address.</td><td style="background-color:#e8e8e8">如果设备不支持易失性范围的 poison 列表,并且请求列表中的任何位置映射到易失性,则设备应返回 Invalid Physical Address。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-153. Get Poison List Input Payload | Get Poison List 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Poison List Flags: Flags that affect the returned list.<br>• Bit[0]: Restart Request: If set to 1, the device shall send the Poison List starting from the first entry, even if a previous transfer was incomplete. A device supporting this flag shall set the Restart Ack bit in the output payload in response to this flag being set. A device that does not support this flag must not set the Restart Ack bit.<br>• Bits[5:1]: Reserved.<br>Get Poison List Physical Address: The starting DPA for which to retrieve the Poison List.<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Poison List Flags:影响返回列表的标志。<br>• Bit[0]:Restart Request(重启请求):如果设置为 1,设备应从第一个条目开始发送 Poison List,即使先前的传输未完成。支持此标志的设备应在响应此标志被设置时在输出负载中设置 Restart Ack 位。不支持此标志的设备不得设置 Restart Ack 位。<br>• Bits[5:1]:保留。<br>Get Poison List Physical Address:要检索 Poison List 的起始 DPA。<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>8</td><td>Get Poison List Physical Address Length: The range of physical addresses for which to retrieve the Poison List. This length shall be in units of 64 bytes (e.g., if this field is 2h, that indicates the length is 128 bytes).</td><td>Get Poison List Physical Address Length:要检索 Poison List 的物理地址范围。此长度应以 64 字节为单位(例如,如果此字段为 2h,则表示长度为 128 字节)。</td></tr>
</tbody>
</table>

**Table 8-154. Get Poison List Output Payload | Get Poison List 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>1</td><td>Poison List Flags: Flags that describe the returned list.<br>• Bit[0]: More Media Error Records: When set, the device has more Media Error Records to return for the given Get Poison List address range.<br>• Bit[1]: Poison List Overflow: When set, the returned list has overflowed, and the returned list can no longer be considered a complete list.<br>• Bit[2]: Scan Media in Progress: When set, a background operation to scan the media is executing.<br>• Bit[3]: Restart Ack: Set by a device that supports the Restart Request flag in response to that flag being set in the Input Payload.<br>• Bits[7:4]: Reserved.</td><td>Poison List Flags:描述返回列表的标志。<br>• Bit[0]:More Media Error Records(更多介质错误记录):当设置时,设备有更多 Media Error Records 要针对给定的 Get Poison List 地址范围返回。<br>• Bit[1]:Poison List Overflow(Poison List 溢出):当设置时,返回的列表已溢出,返回的列表不再被视为完整列表。<br>• Bit[2]:Scan Media in Progress(扫描介质进行中):当设置时,扫描介质的后台操作正在执行。<br>• Bit[3]:Restart Ack(重启确认):由支持 Restart Request 标志的设备在响应输入负载中设置该标志时设置。<br>• Bits[7:4]:保留。</td></tr>
<tr><td>01h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>02h</td><td>8</td><td>Overflow Timestamp: The time at which the device determined the poison list overflowed. The number of unsigned nanoseconds that have elapsed since midnight, 01-Jan-1970, UTC.</td><td>Overflow Timestamp(溢出时间戳):设备确定 poison list 溢出的时间。自 1970 年 1 月 1 日午夜 UTC 以来经过的无符号纳秒数。</td></tr>
<tr><td>0Ah</td><td>2</td><td>Media Error Record Count: Number of records in the Media Error Records list.</td><td>Media Error Record Count:Media Error Records 列表中的记录数。</td></tr>
<tr><td>0Ch</td><td>14h</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>Varies</td><td>Media Error Records: The list of media error records.</td><td>Media Error Records:介质错误记录列表。</td></tr>
</tbody>
</table>

> **Figure 8-X.** Get Poison List (page 733-734) ｜ Get Poison List
>
> <img src="figures/chapter_08/page_0733.png" alt="Figure 8-X page 733" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0733.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-2"></a>
### 8.2.10.9.4.2 Inject Poison (Opcode 4301h) | 注入 Poison (操作码 4301h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An optional command to inject poison into a requested physical address. If the host injects poison using this command, the device shall return poison when the address is accessed through the CXL.mem bus.</td><td style="background-color:#e8e8e8">用于将 poison 注入到请求的物理地址的可选命令。如果主机使用此命令注入 poison,则当通过 CXL.mem 总线访问该地址时,设备应返回 poison。</td></tr>
<tr><td>Injecting poison shall add the new physical address to the device's poison list and the error source shall be set to an injected error. In addition, the device shall add an appropriate poison creation event to its internal Informational Event Log, update the Event Status register, and if configured, interrupt the host.</td><td style="background-color:#e8e8e8">注入 poison 应将新的物理地址添加到设备的 poison 列表,并且错误源应设置为注入错误。此外,设备应将适当的 poison 创建事件添加到其内部 Informational Event Log,更新 Event Status 寄存器,并在配置时中断主机。</td></tr>
<tr><td>It is not an error to inject poison into a DPA that already has poison present and no error is returned.</td><td style="background-color:#e8e8e8">向已存在 poison 的 DPA 注入 poison 不是错误,不返回错误。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to change the data on the device or inject poison by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何更改设备上的数据或注入 poison 的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Invalid Physical Address<br>• Inject Poison Limit Reached<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Invalid Physical Address(无效物理地址)<br>• Inject Poison Limit Reached(达到注入 Poison 限制)<br>• Invalid Security State(无效安全状态)</td></tr>
</tbody>
</table>

**Table 8-155. Media Error Record | Media Error Record**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Media Error Address: The DPA of the memory error and error source.<br>• Bits[2:0]: Error Source: 000b = Unknown; 001b = External. Poison received from a source external to the device; 010b = Internal. The device generated poison from an internal source; 011b = Injected. The error was injected into the device for testing purposes; 111b = Vendor Specific. All other encodings are reserved.<br>• Bits[5:3]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Media Error Address:内存错误和错误源的 DPA。<br>• Bits[2:0]:Error Source(错误源):000b = Unknown(未知);001b = External(外部)。从设备外部的源接收的 poison;010b = Internal(内部)。设备从内部源生成 poison;011b = Injected(注入)。错误被注入到设备中以进行测试;111b = Vendor Specific(厂商特定)。所有其他编码保留。<br>• Bits[5:3]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>4</td><td>Media Error Length: The number of adjacent DPAs in this media error record. This shall be nonzero. Devices may coalesce adjacent memory errors into a single entry. This length shall be in units of 64 bytes.</td><td>Media Error Length:此介质错误记录中相邻 DPA 的数量。这应是非零的。设备可以将相邻的内存错误合并为单个条目。此长度应以 64 字节为单位。</td></tr>
<tr><td>0Ch</td><td>4</td><td>Reserved</td><td>保留</td></tr>
</tbody>
</table>

> **Figure 8-X.** Media Error Record (page 735) ｜ Media Error Record
>
> <img src="figures/chapter_08/page_0735.png" alt="Figure 8-X page 735" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_08/page_0735.png)

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-3"></a>
### 8.2.10.9.4.3 Clear Poison (Opcode 4302h) | 清除 Poison (操作码 4302h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An optional command to clear poison from the requested physical address and atomically write the included data in its place. This provides the same functionality as the host directly writing new data to the device.</td><td style="background-color:#e8e8e8">用于从请求的物理地址清除 poison 并以原子方式将包含的数据写入其位置的可选命令。这提供了与主机直接将新数据写入设备相同的功能。</td></tr>
<tr><td>Clearing poison shall remove the physical address from the device's Poison List. It is not an error to clear poison from an address that does not have poison set. If the device detects that it is not possible to clear poison from the physical address, the device shall return a permanent media failure code for this command.</td><td style="background-color:#e8e8e8">清除 poison 应将物理地址从设备的 Poison List 中删除。从未设置 poison 的地址清除 poison 不是错误。如果设备检测到无法从物理地址清除 poison,则设备应为此命令返回永久性介质失败代码。</td></tr>
<tr><td>In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempt to change the data on the device or clear poison by returning Invalid Security State status for this command. See Section 11.5 for details on locking a device and locked device behavior.</td><td style="background-color:#e8e8e8">为了支持机密计算,如果设备在使用安全 CXL TSP 接口时已被锁定,设备应通过返回 Invalid Security State 状态来拒绝任何更改设备上的数据或清除 poison 的尝试。有关锁定设备和已锁定设备行为的详细信息,请参阅 11.5 节。</td></tr>
<tr><td>This command must not modify the content of the Extended Metadata field associated with this address. If the device is configured with non-zero Metadata bits as defined by HDM-H Metabits Storage Configuration field in Table 8-115, for subsequent read to the DPA, the device shall return Metafield=00b (Meta0-State abbreviation MS0) and MetaValue=00b.</td><td style="background-color:#e8e8e8">此命令不得修改与此地址关联的 Extended Metadata 字段的内容。如果设备配置了表 8-115 中 HDM-H Metabits Storage Configuration 字段所定义的非零 Metadata 位,则对于对 DPA 的后续读取,设备应返回 Metafield=00b(Meta0-State 缩写 MS0)和 MetaValue=00b。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Permanent Media Failure<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Permanent Media Failure(永久性介质故障)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Immediate Data Change</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Immediate Data Change(立即数据更改)</td></tr>
</tbody>
</table>

**Table 8-156. Inject Poison Input Payload | Inject Poison 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Inject Poison Physical Address: The requested DPA at which poison shall be injected by the device.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Inject Poison Physical Address:设备应在该处注入 poison 的请求 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
</tbody>
</table>

**Table 8-157. Clear Poison Input Payload | Clear Poison 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Clear Poison Physical Address: The requested DPA from which poison shall be cleared by the device.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Clear Poison Physical Address:设备应从该处清除 poison 的请求 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>64</td><td>Clear Poison Write Data: The data the device shall always write into the requested physical address, atomically, while clearing poison if the location is marked as being poisoned.</td><td>Clear Poison Write Data:设备应在清除 poison(如果该位置被标记为已 poison)时以原子方式始终写入到请求的物理地址的数据。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-4"></a>
### 8.2.10.9.4.4 Get Scan Media Capabilities (Opcode 4303h) | 获取扫描介质能力 (操作码 4303h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This command allows the device to report capabilities and options for the Scan Media feature based on the requested range. The device may reject this command if the range requested spans the device's volatile and persistent partitions.</td><td style="background-color:#e8e8e8">此命令允许设备根据请求的范围报告 Scan Media 特性的能力和选项。如果请求的范围跨越设备的易失性和持久性分区,设备可以拒绝此命令。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-158. Get Scan Media Capabilities Input Payload | Get Scan Media Capabilities 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Get Scan Media Capabilities Start Physical Address: The starting DPA from which to retrieve Scan Media capabilities.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Get Scan Media Capabilities Start Physical Address:要检索 Scan Media 能力的起始 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>8</td><td>Get Scan Media Capabilities Physical Address Length: The range of physical addresses for which to retrieve Scan Media capabilities. This length shall be in units of 64 bytes.</td><td>Get Scan Media Capabilities Physical Address Length:要检索 Scan Media 能力的物理地址范围。此长度应以 64 字节为单位。</td></tr>
</tbody>
</table>

**Table 8-159. Get Scan Media Capabilities Output Payload | Get Scan Media Capabilities 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>4</td><td>Estimated Scan Media Time: The number of milliseconds that the device estimates are required to complete the Scan Media request over the range specified in the input.</td><td>Estimated Scan Media Time:设备估计完成输入中指定范围的 Scan Media 请求所需的毫秒数。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-5"></a>
### 8.2.10.9.4.5 Scan Media (Opcode 4304h) | 扫描介质 (操作码 4304h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The Scan Media command causes the device to initiate a scan of a portion of its media for locations that are poisoned or result in poison if the addresses were accessed by the host. The device may update its Poison List as a result of executing the scan and shall complete any changes to the Poison List before signally completion of the Scan Media background operation. If the device updates its Poison List while the Scan Media background operation is executing, the device shall indicate that a media scan is in progress if Get Poison List is called during the scan. The host should use this command only if the poison list has overflowed and is no longer a complete list of the memory errors that exist on the media. The device may reject this command if the requested range spans the device's volatile and persistent partitions.</td><td style="background-color:#e8e8e8">Scan Media 命令导致设备启动对其部分介质的扫描,以查找主机访问时已 poison 或导致 poison 的位置。设备可能会由于执行扫描而更新其 Poison List,并应在发出 Scan Media 后台操作完成信号之前完成对 Poison List 的任何更改。如果设备在 Scan Media 后台操作执行时更新其 Poison List,则如果在扫描期间调用 Get Poison List,设备应指示介质扫描正在进行。主机仅在 poison list 已溢出且不再是介质上存在的内存错误的完整列表时才应使用此命令。如果请求的范围跨越设备的易失性和持久性分区,设备可以拒绝此命令。</td></tr>
<tr><td>If interrupts are enabled for reporting internally or externally generated poison, and the poison list has not overflowed, the host should avoid using this command. It is expensive and may impact the performance of other operations on the device. This is intended only as a backup to retrieve the list of memory error locations in the event the poison list has overflowed.</td><td style="background-color:#e8e8e8">如果已启用用于报告内部或外部生成的 poison 的中断,并且 poison list 尚未溢出,则主机应避免使用此命令。它是昂贵的,并且可能会影响设备上其他操作的性能。这仅用作在 poison list 溢出时检索内存错误位置列表的备份。</td></tr>
<tr><td>Because the execution of a media scan may take significant time to complete, it is considered a background operation. The Scan Media command shall initiate the background operation and provide immediate status on the device's ability to start the scan operation. Any previous Scan Media results are discarded by the device upon receiving a new Scan Media command. Once the Scan Media command is successfully started, the Background Command Status register is used to retrieve the status. The Get Scan Media Results command shall return the list of poisoned memory locations.</td><td style="background-color:#e8e8e8">由于介质扫描的执行可能需要大量时间才能完成,因此它被视为后台操作。Scan Media 命令应启动后台操作,并立即提供有关设备启动扫描操作的能力的状态。设备在收到新的 Scan Media 命令时会丢弃任何先前的 Scan Media 结果。一旦 Scan Media 命令成功启动,Background Command Status 寄存器用于检索状态。Get Scan Media Results 命令应返回已 poison 的内存位置列表。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Background Command Started<br>• Invalid Input<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Aborted<br>• Invalid Physical Address<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Background Command Started(后台命令已启动)<br>• Invalid Input(无效输入)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Aborted(中止)<br>• Invalid Physical Address(无效物理地址)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• Background Operation<br>• Request Abort Background Operation Command Supported</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• Background Operation(后台操作)<br>• 支持 Request Abort Background Operation Command</td></tr>
</tbody>
</table>

**Table 8-160. Scan Media Input Payload | Scan Media 输入负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Scan Media Physical Address: The starting DPA from which to start the scan.<br>• Bits[5:0]: Reserved<br>• Bits[7:6]: DPA[7:6]<br>• Bits[15:8]: DPA[15:8]<br>• …<br>• Bits[63:56]: DPA[63:56]</td><td>Scan Media Physical Address:开始扫描的起始 DPA。<br>• Bits[5:0]:保留<br>• Bits[7:6]:DPA[7:6]<br>• Bits[15:8]:DPA[15:8]<br>• …<br>• Bits[63:56]:DPA[63:56]</td></tr>
<tr><td>08h</td><td>8</td><td>Scan Media Physical Address Length: The range of physical addresses to scan. This length shall be in units of 64 bytes.</td><td>Scan Media Physical Address Length:要扫描的物理地址范围。此长度应以 64 字节为单位。</td></tr>
<tr><td>10h</td><td>1</td><td>Scan Media Flags<br>• Bit[0]: No Event Log: When set, the device shall not generate event logs for media errors found during the Scan Media operation.<br>• Bits[7:1]: Reserved.</td><td>Scan Media Flags<br>• Bit[0]:No Event Log(无事件日志):当设置时,设备不应为 Scan Media 操作期间发现的介质错误生成事件日志。<br>• Bits[7:1]:保留。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---

<a id="sec-8-2-10-9-4-6"></a>
### 8.2.10.9.4.6 Get Scan Media Results (Opcode 4305h) | 获取扫描介质结果 (操作码 4305h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Get Scan Media Results returns an unordered list of poisoned memory locations, in response to the Scan Media command. If the Scan Media command has not been called since the last Conventional Reset, the device shall return the Unsupported return code. The completion status for the Scan Media command is returned in the Background Command Status register and is not repeated here.</td><td style="background-color:#e8e8e8">Get Scan Media Results 返回已 poison 内存位置的无序列表,作为对 Scan Media 命令的响应。如果自上次 Conventional Reset 以来未调用 Scan Media 命令,则设备应返回 Unsupported 返回码。Scan Media 命令的完成状态在 Background Command Status 寄存器中返回,此处不再重复。</td></tr>
<tr><td>Because the returned list can be larger than the output payload size, it is possible to return the list in multiple calls to Get Scan Media Results. The More Media Error Records indicator shall be set by the device anytime there are more records to retrieve. The caller should continue to issue this command until this indicator is no longer set.</td><td style="background-color:#e8e8e8">由于返回的列表可能大于输出负载大小,因此可以通过多次调用 Get Scan Media Results 返回列表。每当有更多记录要检索时,设备应设置 More Media Error Records 指示符。调用者应继续发出此命令,直到此指示符不再设置。</td></tr>
<tr><td>If the device cannot complete the scan and requires the host to retrieve scan media results before the device can continue the scan, the device shall set the Scan Media Stopped Prematurely indicator, return a valid Scan Media Restart Physical Address and Scan Media Restart Physical Address Length. This is the physical address range the device would require the Scan Media command to be called again with to continue the scan. It is the responsibility of the host to issue the Scan Media command, using this restart context, to guarantee that the Device's entire physical address range is eventually scanned.</td><td style="background-color:#e8e8e8">如果设备无法完成扫描并且需要主机在设备能够继续扫描之前检索扫描介质结果,则设备应设置 Scan Media Stopped Prematurely 指示符,返回有效的 Scan Media Restart Physical Address 和 Scan Media Restart Physical Address Length。这是设备需要再次调用 Scan Media 命令才能继续扫描的物理地址范围。主机有责任使用此重启上下文发出 Scan Media 命令,以保证设备的整个物理地址范围最终被扫描。</td></tr>
<tr><td><b>Possible Command Return Codes:</b><br>• Success<br>• Unsupported<br>• Internal Error<br>• Retry Required<br>• Invalid Payload Length<br>• Media Disabled<br>• Busy<br>• Invalid Security State</td><td style="background-color:#e8e8e8"><b>可能的命令返回码:</b><br>• Success(成功)<br>• Unsupported(不支持)<br>• Internal Error(内部错误)<br>• Retry Required(需要重试)<br>• Invalid Payload Length(无效负载长度)<br>• Media Disabled(介质已禁用)<br>• Busy(忙)<br>• Invalid Security State(无效安全状态)</td></tr>
<tr><td><b>Command Effects:</b><br>• None</td><td style="background-color:#e8e8e8"><b>命令效果:</b><br>• None(无)</td></tr>
</tbody>
</table>

**Table 8-161. Get Scan Media Results Output Payload | Get Scan Media Results 输出负载**

<table>
<thead>
<tr><th>Byte Offset</th><th>Length in Bytes</th><th>🇬🇧 Description</th><th>🇨🇳 描述</th></tr>
</thead>
<tbody>
<tr><td>00h</td><td>8</td><td>Scan Media Restart Physical Address: The location from which the host should restart the Scan Media operation if the device could not complete the requested scan.</td><td>Scan Media Restart Physical Address:如果设备无法完成请求的扫描,主机应从该位置重新启动 Scan Media 操作。</td></tr>
<tr><td>08h</td><td>8</td><td>Scan Media Restart Physical Address Length: The remaining range from which the host should restart the Scan Media operation if the device could not complete the requested scan.</td><td>Scan Media Restart Physical Address Length:如果设备无法完成请求的扫描,主机应从该剩余范围重新启动 Scan Media 操作。</td></tr>
<tr><td>10h</td><td>1</td><td>Scan Media Flags<br>• Bit[0]: More Media Error Records: When set, the device has more Media Error Records to return for the given Scan Media address range.<br>• Bit[1]: Scan Stopped Prematurely: The device has run out of internal storage space for the error list.<br>• Bits[7:2]: Reserved.</td><td>Scan Media Flags<br>• Bit[0]:More Media Error Records(更多介质错误记录):当设置时,设备有更多 Media Error Records 要针对给定的 Scan Media 地址范围返回。<br>• Bit[1]:Scan Stopped Prematurely(扫描过早停止):设备的错误列表内部存储空间已用完。<br>• Bits[7:2]:保留。</td></tr>
<tr><td>11h</td><td>1</td><td>Reserved</td><td>保留</td></tr>
<tr><td>12h</td><td>2</td><td>Media Error Record Count: The number of records in the Media Error Records list.</td><td>Media Error Record Count:Media Error Records 列表中的记录数。</td></tr>
<tr><td>14h</td><td>0Ch</td><td>Reserved</td><td>保留</td></tr>
<tr><td>20h</td><td>Varies</td><td>Media Error Records: The list of media error records.</td><td>Media Error Records:介质错误记录列表。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-part-c)

---
