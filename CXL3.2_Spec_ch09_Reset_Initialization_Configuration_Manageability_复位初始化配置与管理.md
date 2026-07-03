# 📘 第 9 章　复位、初始化、配置与管理 (Chapter 9. Reset, Initialization, Configuration, and Manageability)

> **Source pages**: 799–878 | **File**: chapter_09.md | **Format**: 中英对照双语

---

## 📑 本章目录

- [9.0 复位、初始化、配置与管理 (Reset, Initialization, Configuration, and Manageability)](#sec-9-0)
- [9.1 CXL 启动与复位概述 (CXL Boot and Reset Overview)](#sec-9-1)
  - [9.1.1 概述 (General)](#sec-9-1-1)
  - [9.1.2 比较 CXL 与 PCIe 行为 (Comparing CXL and PCIe Behavior)](#sec-9-1-2)
    - [9.1.2.1 交换机行为 (Switch Behavior)](#sec-9-1-2-1)
- [9.2 CXL 设备启动流程 (CXL Device Boot Flow)](#sec-9-2)
- [9.3 CXL 系统复位进入流程 (CXL System Reset Entry Flow)](#sec-9-3)
- [9.4 CXL 设备睡眠状态进入流程 (CXL Device Sleep State Entry Flow)](#sec-9-4)
- [9.5 功能级复位 (Function Level Reset, FLR)](#sec-9-5)
- [9.6 缓存管理 (Cache Management)](#sec-9-6)
- [9.7 CXL 复位 (CXL Reset)](#sec-9-7)
  - [9.7.1 对易失 HDM 内容的影响 (Effect on the Contents of the Volatile HDM)](#sec-9-7-1)
  - [9.7.2 软件操作 (Software Actions)](#sec-9-7-2)
  - [9.7.3 CXL 复位与请求重试状态 (CXL Reset and Request Retry Status, RRS)](#sec-9-7-3)
- [9.8 全局持久刷新 (Global Persistent Flush, GPF)](#sec-9-8)
  - [9.8.1 主机与交换机职责 (Host and Switch Responsibilities)](#sec-9-8-1)
  - [9.8.2 设备职责 (Device Responsibilities)](#sec-9-8-2)
  - [9.8.3 能源预算 (Energy Budgeting)](#sec-9-8-3)
- [9.9 热插拔 (Hot-Plug)](#sec-9-9)
- [9.10 软件枚举 (Software Enumeration)](#sec-9-10)
- [9.11 RCD 枚举 (RCD Enumeration)](#sec-9-11)
  - [9.11.1 RCD 模式 (RCD Mode)](#sec-9-11-1)
  - [9.11.2 RCH 与 RCD 的 PCIe 软件视图 (PCIe Software View of an RCH and RCD)](#sec-9-11-2)
  - [9.11.3 RCH 与 RCD 的系统固件视图 (System Firmware View of an RCH and RCD)](#sec-9-11-3)
  - [9.11.4 RCH 与 RCD 的操作系统视图 (OS View of an RCH and RCD)](#sec-9-11-4)
  - [9.11.5 基于系统固件的 RCD 枚举流程 (System Firmware-based RCD Enumeration Flow)](#sec-9-11-5)
  - [9.11.6 RCD 发现 (RCD Discovery)](#sec-9-11-6)
  - [9.11.7 多 Flex Bus 链路的 eRCD (eRCDs with Multiple Flex Bus Links)](#sec-9-11-7)
    - [9.11.7.1 单 CPU 拓扑 (Single CPU Topology)](#sec-9-11-7-1)
    - [9.11.7.2 多 CPU 拓扑 (Multiple CPU Topology)](#sec-9-11-7-2)
  - [9.11.8 连接到 RCH 的 CXL 设备 (CXL Devices Attached to an RCH)](#sec-9-11-8)
- [9.12 CXL VH 枚举 (CXL VH Enumeration)](#sec-9-12)
  - [9.12.1 CXL 根端口 (CXL Root Ports)](#sec-9-12-1)
  - [9.12.2 CXL 虚拟层级 (CXL Virtual Hierarchy)](#sec-9-12-2)
  - [9.12.3 枚举 CXL RP 与 DSP (Enumerating CXL RPs and DSPs)](#sec-9-12-3)
  - [9.12.4 连接到 CXL RP 或 DSP 的 eRCD (eRCD Connected to a CXL RP or DSP)](#sec-9-12-4)
    - [9.12.4.1 引导时重新配置 CXL RP 或 DSP 以启用 eRCD (Boot time Reconfiguration of CXL RP or DSP to Enable an eRCD)](#sec-9-12-4-1)
  - [9.12.5 CXL RP 与 DSP 下的 CXL eRCD — 示例 (CXL eRCD below a CXL RP and DSP - Example)](#sec-9-12-5)
  - [9.12.6 CXL VH 中链路与协议寄存器的映射 (Mapping of Link and Protocol Registers in CXL VH)](#sec-9-12-6)
- [9.13 HDM 的软件视图 (Software View of HDM)](#sec-9-13)
  - [9.13.1 内存交织 (Memory Interleaving)](#sec-9-13-1)
    - [9.13.1.1 合法交织配置:12 路、6 路与 3 路 (Legal Interleaving Configurations: 12-way, 6-way, and 3-way)](#sec-9-13-1-1)
  - [9.13.2 CXL 内存设备标签存储区 (CXL Memory Device Label Storage Area)](#sec-9-13-2)
    - [9.13.2.1 LSA 总体布局 (Overall LSA Layout)](#sec-9-13-2-1)
    - [9.13.2.2 标签索引块 (Label Index Blocks)](#sec-9-13-2-2)
    - [9.13.2.3 标签通用属性 (Common Label Properties)](#sec-9-13-2-3)
    - [9.13.2.4 区域标签 (Region Labels)](#sec-9-13-2-4)
    - [9.13.2.5 命名空间标签 (Namespace Labels)](#sec-9-13-2-5)
    - [9.13.2.6 厂商特定标签 (Vendor-specific Labels)](#sec-9-13-2-6)
  - [9.13.3 动态容量设备 (Dynamic Capacity Device, DCD)](#sec-9-13-3)
    - [9.13.3.1 FM 对 DCD 的管理 (DCD Management By FM)](#sec-9-13-3-1)
    - [9.13.3.2 设置内存共享 (Setting up Memory Sharing)](#sec-9-13-3-2)
    - [9.13.3.3 范围列表跟踪 (Extent List Tracking)](#sec-9-13-3-3)
  - [9.13.4 容量或性能降级 (Capacity or Performance Degradation)](#sec-9-13-4)
- [9.14 反向失效配置 (Back-Invalidate Configuration)](#sec-9-14)
  - [9.14.1 发现 (Discovery)](#sec-9-14-1)
  - [9.14.2 配置 (Configuration)](#sec-9-14-2)
  - [9.14.3 混合配置 (Mixed Configurations)](#sec-9-14-3)
    - [9.14.3.1 支持 BI 的 Type 2 设备 (BI-capable Type 2 Device)](#sec-9-14-3-1)
    - [9.14.3.2 Type 2 设备回退模式 (Type 2 Device Fallback Modes)](#sec-9-14-3-2)
    - [9.14.3.3 支持 BI 的 Type 3 设备 (BI-capable Type 3 Device)](#sec-9-14-3-3)
- [9.15 Cache ID 配置与路由 (Cache ID Configuration and Routing)](#sec-9-15)
  - [9.15.1 主机能力 (Host Capabilities)](#sec-9-15-1)
  - [9.15.2 下游端口解码功能 (Downstream Port Decode Functionality)](#sec-9-15-2)
  - [9.15.3 上游交换机端口路由功能 (Upstream Switch Port Routing Functionality)](#sec-9-15-3)
  - [9.15.4 主机桥路由功能 (Host Bridge Routing Functionality)](#sec-9-15-4)
- [9.16 UIO 直连 P2P 到 HDM (UIO Direct P2P to HDM)](#sec-9-16)
  - [9.16.1 UIO 直连 P2P 到 HDM 消息的处理 (Processing of UIO Direct P2P to HDM Messages)](#sec-9-16-1)
    - [9.16.1.1 UIO 地址匹配 (DSP 与根端口) (UIO Address Match (DSP and Root Port))](#sec-9-16-1-1)
    - [9.16.1.2 UIO 地址匹配 (CXL.mem 设备) (UIO Address Match (CXL.mem Device))](#sec-9-16-1-2)
- [9.17 加速器的直连 P2P CXL.mem (Direct P2P CXL.mem for Accelerators)](#sec-9-17)
  - [9.17.1 对等 SLD 配置 (Peer SLD Configuration)](#sec-9-17-1)
  - [9.17.2 对等 MLD 配置 (Peer MLD Configuration)](#sec-9-17-2)
  - [9.17.3 对等 GFD 配置 (Peer GFD Configuration)](#sec-9-17-3)
- [9.18 CXL 操作系统固件接口扩展 (CXL OS Firmware Interface Extensions)](#sec-9-18)
  - [9.18.1 CXL 早期发现表 (CXL Early Discovery Table, CEDT)](#sec-9-18-1)
    - [9.18.1.1 CEDT 头 (CEDT Header)](#sec-9-18-1-1)
    - [9.18.1.2 CXL 主机桥结构 (CXL Host Bridge Structure, CHBS)](#sec-9-18-1-2)
    - [9.18.1.3 CXL 固定内存窗口结构 (CXL Fixed Memory Window Structure, CFMWS)](#sec-9-18-1-3)
    - [9.18.1.4 CXL XOR 交织数学结构 (CXL XOR Interleave Math Structure, CXIMS)](#sec-9-18-1-4)
    - [9.18.1.5 RCEC 下游端口关联结构 (RCEC Downstream Port Association Structure, RDPAS)](#sec-9-18-1-5)
    - [9.18.1.6 CXL 系统描述结构 (CXL System Description Structure, CSDS)](#sec-9-18-1-6)
  - [9.18.2 CXL _OSC](#sec-9-18-2)
    - [9.18.2.1 评估 _OSC 的规则 (Rules for Evaluating _OSC)](#sec-9-18-2-1)
      - [9.18.2.1.1 查询支持标志 (Query Support Flag)](#sec-9-18-2-1-1)
      - [9.18.2.1.2 评估条件 (Evaluation Conditions)](#sec-9-18-2-1-2)
      - [9.18.2.1.3 _OSC 调用顺序 (Sequence of _OSC Calls)](#sec-9-18-2-1-3)
      - [9.18.2.1.4 ASL 示例 (ASL Example)](#sec-9-18-2-1-4)
  - [9.18.3 CXL 根设备特定方法 (_DSM) (CXL Root Device Specific Methods (_DSM))](#sec-9-18-3)
    - [9.18.3.1 用于检索 QTG ID 的 _DSM 函数 (_DSM Function for Retrieving QTG ID)](#sec-9-18-3-1)
- [9.19 CXL 设备可管理性模型 (Manageability Model for CXL Devices)](#sec-9-19)
- [9.20 组件命令接口 (Component Command Interface)](#sec-9-20)
  - [9.20.1 CCI 属性 (CCI Properties)](#sec-9-20-1)
  - [9.20.2 基于 MCTP 的 CCI 属性 (MCTP-based CCI Properties)](#sec-9-20-2)

## 🖼 本章图表

| 图表 | 英文标题 | 中文标题 | 页码 |
|---|---|---|---|
| Figure 9-1 | PMREQ/RESETPREP Propagation by CXL Switch | CXL 交换机对 PMREQ/RESETPREP 的传播 | 801 |
| Figure 9-2 | CXL Device Reset Entry Flow | CXL 设备复位进入流程 | 802 |
| Figure 9-3 | CXL Device Sleep State Entry Flow | CXL 设备睡眠状态进入流程 | 803 |
| Figure 9-4 | PCIe Software View of an RCH and RCD | RCH 与 RCD 的 PCIe 软件视图 | 816 |
| Figure 9-5 | One CPU Connected to a Dual-Headed RCD by Two Flex Bus Links | 一颗 CPU 通过两条 Flex Bus 链路连接双端口 RCD | 819 |
| Figure 9-6 | Two CPUs Connected to One CXL Device by Two Flex Bus Links | 两颗 CPU 通过两条 Flex Bus 链路连接一个 CXL 设备 | 820 |
| Figure 9-7 | CXL Device Remaps Upstream Port and Component Registers | CXL 设备重新映射上游端口和组件寄存器 | 822 |
| Figure 9-8 | CXL Device that Does Not Remap Upstream Port and Component Registers | 不重新映射上游端口和组件寄存器的 CXL 设备 | 823 |
| Figure 9-9 | CXL Root Port/DSP State Diagram | CXL 根端口/DSP 状态图 | 826 |
| Figure 9-10 | eRCD MMIO Address Decode - Example | eRCD MMIO 地址解码示例 | 828 |
| Figure 9-11 | eRCD Configuration Space Decode - Example | eRCD 配置空间解码示例 | 829 |
| Figure 9-12 | Physical Topology - Example | 物理拓扑示例 | 830 |
| Figure 9-13 | Software View | 软件视图 | 831 |
| Figure 9-14 | CXL Link/Protocol Register Mapping in a CXL VH | CXL VH 中链路/协议寄存器的映射 | 832 |
| Figure 9-15 | CXL Link/Protocol Registers in a CXL Switch | CXL 交换机中链路/协议寄存器的映射 | 832 |
| Figure 9-16 | One-level Interleaving at Switch - Example | 交换机处单层交织示例 | 835 |
| Figure 9-17 | Two-level Interleaving | 双层交织 | 835 |
| Figure 9-18 | Three-level Interleaving Example | 三层交织示例 | 836 |
| Figure 9-19 | Overall LSA Layout | LSA 总体布局 | 838 |
| Figure 9-20 | Fletcher64 Checksum Algorithm in C | C 语言中的 Fletcher64 校验和算法 | 839 |
| Figure 9-21 | Sequence Numbers in Label Index Blocks | 标签索引块中的序列号 | 840 |
| Figure 9-22 | Extent List Example (No Sharing) | 范围列表示例 (无共享) | 845 |
| Figure 9-23 | Shared Extent List Example | 共享范围列表示例 | 845 |
| Figure 9-24 | DCD DPA Space Example | DCD DPA 空间示例 | 846 |
| Figure 9-25 | UIO Direct P2P to Interleaved HDM | UIO 直连 P2P 到交织 HDM | 860 |

## 📊 本章表格

| 表格 | 英文标题 | 中文标题 | 页码 |
|---|---|---|---|
| Table 9-1 | Event Sequencing for Reset and Sx Flows | 复位与 Sx 流程的事件顺序 | 800 |
| Table 9-2 | CXL Switch Behavior Message Aggregation Rules | CXL 交换机消息聚合规则 | 800–801 |
| Table 9-3 | GPF Energy Calculation Example | GPF 能量计算示例 | 811 |
| Table 9-4 | Memory Decode Rules in Presence of One CPU/Two Flex Bus Links | 一个 CPU / 两条 Flex Bus 链路下的内存解码规则 | 819 |
| Table 9-5 | Memory Decode Rules in Presence of Two CPU/Two Flex Bus Links | 两个 CPU / 两条 Flex Bus 链路下的内存解码规则 | 821 |
| Table 9-6 | 12-Way Device-level Interleave at IGB | 在 IGB 下的 12 路设备级交织 | 837 |
| Table 9-7 | 6-Way Device-level Interleave at IGB | 在 IGB 下的 6 路设备级交织 | 837 |
| Table 9-8 | 3-Way Device-level Interleave at IGB | 在 IGB 下的 3 路设备级交织 | 837 |
| Table 9-9 | Label Index Block Layout | 标签索引块布局 | 840 |
| Table 9-10 | Region Label Layout | 区域标签布局 | 842 |
| Table 9-11 | Namespace Label Layout | 命名空间标签布局 | 843 |
| Table 9-12 | Vendor Specific Label Layout | 厂商特定标签布局 | 844 |
| Table 9-13 | Downstream Port Handling of BISnp | 下游端口对 BISnp 的处理 | 851 |
| Table 9-14 | Downstream Port Handling of BIRsp | 下游端口对 BIRsp 的处理 | 851 |
| Table 9-15 | CXL Type 2 Device Behavior in Fallback Operation Mode | 回退操作模式下 CXL Type 2 设备的行为 | 855 |
| Table 9-16 | Downstream Port Handling of D2H Request Messages | 下游端口对 D2H 请求消息的处理 | 857 |
| Table 9-17 | Downstream Port Handling of H2D Response Message and H2D Request Message | 下游端口对 H2D 响应消息和 H2D 请求消息的处理 | 857 |
| Table 9-18 | Handling of UIO Accesses | UIO 访问的处理 | 861 |
| Table 9-19 | CEDT Header | CEDT 头 | 864 |
| Table 9-20 | CEDT Structure Types | CEDT 结构类型 | 864 |
| Table 9-21 | CHBS Structure | CHBS 结构 | 865 |
| Table 9-22 | CFMWS Structure | CFMWS 结构 | 866–868 |
| Table 9-23 | CXIMS Structure | CXIMS 结构 | 868 |
| Table 9-24 | RDPAS Structure | RDPAS 结构 | 869 |
| Table 9-25 | CSDS Structure | CSDS 结构 | 870 |
| Table 9-26 | _OSC Capabilities Buffer DWORDs | _OSC 能力缓冲区 DWORD | 871 |
| Table 9-27 | Interpretation of CXL _OSC Support Field | CXL _OSC 支持字段含义 | 871 |
| Table 9-28 | Interpretation of CXL _OSC Control Field, Passed in via Arg3 | 通过 Arg3 传入的 CXL _OSC 控制字段含义 | 872 |
| Table 9-29 | Interpretation of CXL _OSC Control Field, Returned Value | CXL _OSC 控制字段返回值的含义 | 872 |
| Table 9-30 | _DSM Definitions for CXL Root Device | CXL 根设备的 _DSM 定义 | 874 |
| Table 9-31 | _DSM for Retrieving QTG, Inputs, and Outputs | 用于检索 QTG 的 _DSM 输入与输出 | 875 |

---

<a id="sec-9-0"></a>
## 9.0 Reset, Initialization, Configuration, and Manageability | 复位、初始化、配置与管理

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.0 Reset, Initialization, Configuration, and Manageability</strong></td><td style="background-color:#e8e8e8"><strong>9.0 复位、初始化、配置与管理</strong></td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-1"></a>
## 9.1 CXL Boot and Reset Overview | CXL 启动与复位概述

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.1 CXL Boot and Reset Overview</strong></td><td style="background-color:#e8e8e8"><strong>9.1 CXL 启动与复位概述</strong></td></tr>
</tbody>
</table>

<a id="sec-9-1-1"></a>
### 9.1.1 General | 概述

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Boot and Power-up sequencing of CXL devices follows the applicable form-factor specifications and as such, will not be discussed in detail in this section.</td><td style="background-color:#e8e8e8">CXL 设备的启动与上电顺序遵循适用的形态因子 (Form Factor) 规范,因此本节将不进行详细讨论。</td></tr>
<tr><td>CXL devices can encounter three types of resets.</td><td style="background-color:#e8e8e8">CXL 设备可能遇到三种类型的复位。</td></tr>
<tr><td>• Hot Reset – Triggered via link (via LTSSM or Link Down)</td><td style="background-color:#e8e8e8">• 热复位 (Hot Reset) – 通过链路触发 (通过 LTSSM 或 Link Down)</td></tr>
<tr><td>• Warm Reset – Triggered via external signal, PERST# (or equivalent, form-factor-specific mechanism)</td><td style="background-color:#e8e8e8">• 暖复位 (Warm Reset) – 通过外部信号 PERST# (或等效的、形态因子特定的机制) 触发</td></tr>
<tr><td>• Cold Reset – Involves main Power removal and PERST# (or equivalent, form-factor-specific mechanism)</td><td style="background-color:#e8e8e8">• 冷复位 (Cold Reset) – 涉及主电源移除和 PERST# (或等效的、形态因子特定的机制)</td></tr>
<tr><td>These three reset types are labeled as Conventional Reset. Function Level Reset (see Section 9.5) and CXL Reset (see Section 9.7) are not considered to be Conventional Resets. These definitions are consistent with PCIe* Base Specification.</td><td style="background-color:#e8e8e8">这三种复位类型被标记为传统复位 (Conventional Reset)。功能级复位 (Function Level Reset, FLR,见 9.5 节) 和 CXL 复位 (CXL Reset,见 9.7 节) 不被视为传统复位。这些定义与 PCIe* 基本规范 (PCIe Base Specification) 一致。</td></tr>
<tr><td>Flex Bus Physical Layer link states across cold reset, warm reset, surprise reset, and Sx entry match PCIe Physical Layer link states.</td><td style="background-color:#e8e8e8">Flex Bus 物理层链路状态在冷复位、暖复位、意外复位 (Surprise Reset) 以及 Sx 进入期间与 PCIe 物理层链路状态一致。</td></tr>
<tr><td>This chapter highlights the differences that exist between CXL and native PCIe for these reset operations.</td><td style="background-color:#e8e8e8">本章重点说明在这些复位操作中 CXL 与原生 PCIe 之间存在的差异。</td></tr>
<tr><td>A PCIe device generally cannot determine which system-level flow triggered a Conventional Reset. System-level reset and Sx-entry flows require coordinated coherency domain shutdown before the sequence can progress. Therefore, the CXL flow will adhere to the following rules:</td><td style="background-color:#e8e8e8">PCIe 设备通常无法确定是哪个系统级流程触发了传统复位。系统级复位和 Sx 进入流程在进行下一步之前,需要协调关闭一致性域 (Coherency Domain)。因此,CXL 流程将遵循以下规则:</td></tr>
<tr><td>• Warnings shall be issued to all CXL devices before the system initiates system-level reset and Sx-entry transitions.</td><td style="background-color:#e8e8e8">• 在系统启动系统级复位和 Sx 进入转换之前,应向所有 CXL 设备发出警告。</td></tr>
<tr><td>• CXL PM messages shall be used to communicate between the host and the device. Devices must respond to these messages with the correct acknowledge, even if no actions are actually performed on the device. To prevent deadlock in cases where one or more downstream components do not respond, the host must implement a timeout, after which the host proceeds as if the response has been received.</td><td style="background-color:#e8e8e8">• 主机与设备之间的通信应使用 CXL PM 消息。即使设备实际上未执行任何操作,也必须以正确的确认 (Acknowledge, Ack) 响应这些消息。为防止在一个或多个下游组件无响应时产生死锁,主机必须实现一个超时机制,在此之后主机将假定已收到响应并继续执行。</td></tr>
<tr><td>• A device shall correctly process the reset trigger regardless of whether they are preceded by these warning messages. Not all device resets are preceded by a warning message. For example, setting Secondary Bus Reset bit in a Downstream Port above the device results in a device hot-reset, but it is not preceded by any warning message. It is also possible that the PM VDM warning message may be lost due to an error condition.</td><td style="background-color:#e8e8e8">• 无论是否带有这些警告消息,设备都应正确处理复位触发。并非所有设备复位都带有警告消息。例如,在设备上方的下游端口中设置 Secondary Bus Reset 位会导致设备热复位,但该复位之前没有任何警告消息。PM VDM 警告消息也可能由于错误条件而丢失。</td></tr>
<tr><td>Sx states are system Sleep States and are enumerated in ACPI Specification.</td><td style="background-color:#e8e8e8">Sx 状态是系统睡眠状态,在 ACPI 规范中定义。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-1-2"></a>
### 9.1.2 Comparing CXL and PCIe Behavior | 比较 CXL 与 PCIe 行为

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.1.2 Comparing CXL and PCIe Behavior</strong></td><td style="background-color:#e8e8e8"><strong>9.1.2 比较 CXL 与 PCIe 行为</strong></td></tr>
<tr><td>Table 9-1 summarizes the difference in event sequencing and signaling methods across System Reset and Sx flows, for CXL.io, CXL.cache, CXL.mem, and PCIe.</td><td style="background-color:#e8e8e8">表 9-1 总结了 CXL.io、CXL.cache、CXL.mem 和 PCIe 在系统复位和 Sx 流程之间的事件顺序和信令方法的差异。</td></tr>
<tr><td>The terms used in the table are as follows:</td><td style="background-color:#e8e8e8">表中使用的术语如下:</td></tr>
<tr><td>• Warning: An early notification of the upcoming event. Devices with coherent cache or memory are required to complete outstanding transactions, flush internal caches as needed, and then place memory in a safe state such as Self-refresh as required. Devices are required to complete all internal actions and then respond with a correct Ack to the processor.</td><td style="background-color:#e8e8e8">• 警告 (Warning):对即将发生事件的提前通知。具有一致性缓存或内存的设备需要完成所有未完成的事务,根据需要刷新内部缓存,然后根据需要将内存置于安全状态 (如自刷新,Self-refresh)。设备需要完成所有内部操作,然后向处理器返回正确的确认 (Ack)。</td></tr>
<tr><td>• Signaling: Actual initiation of the state transition, using either wires and/or link-layer messaging.</td><td style="background-color:#e8e8e8">• 信令 (Signaling):使用物理信号线或链路层消息,实际启动状态转换。</td></tr>
</tbody>
</table>

> **Table 9-1.** Event Sequencing for Reset and Sx Flows | 复位与 Sx 流程的事件顺序
>
> | Case (事件) | PCIe | CXL |
> |---|---|---|
> | System Reset Entry (系统复位进入) | Warning: None.<br>Signaling: LTSSM Hot Reset. | Warning: PM2IP (ResetWarn, System Reset)¹.<br>Signaling: LTSSM Hot Reset. |
> | Surprise System Reset Entry (意外系统复位进入) | Warning: None.<br>Signaling: LTSSM detect-entry or PERST#. | Warning: None.<br>Signaling: LTSSM detect-entry or PERST#. |
> | System Sx Entry (系统 Sx 进入) | Warning: PME_Turn_Off/Ack.<br>Signaling: PERST# (Main power will go down). | Warning: PM2IP (ResetWarn, Sx)¹.<br>PME_Turn_Off/Ack.<br>Signaling: PERST# (Main power will go down). |
> | System Power Failure (系统掉电) | Warning: None. | Warning: PM2IP (GPF Phase 1 and Phase 2)¹; see Section 9.8. |
>
> ¹ CXL PM VDM with different encodings for different events. If CXL.io devices do not respond to the CXL PM VDM, the host may still end up in the correct state due to timeouts. | ¹ CXL PM VDM 针对不同事件使用不同编码。如果 CXL.io 设备未响应 CXL PM VDM,主机仍可能因超时机制而进入正确状态。
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_09/page_0800.png)

<a id="sec-9-1-2-1"></a>
#### 9.1.2.1 Switch Behavior | 交换机行为

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.1.2.1 Switch Behavior</strong></td><td style="background-color:#e8e8e8"><strong>9.1.2.1 交换机行为</strong></td></tr>
<tr><td>When a CXL Switch (physical or virtual) is present, the Switch shall forward PM2IP messages received on its primary interface to CXL components on the secondary interface subject to rules specified below. The Switch shall aggregate IP2PM messages from the secondary interface prior to responding on its primary interface subject to rules specified below. (See Table 3-1 for PM Commands.) When communicating with a pooled device, these messages shall carry LD-ID TLP Prefix in both directions.</td><td style="background-color:#e8e8e8">当存在 CXL 交换机 (物理或虚拟) 时,交换机应将其主端口接收到的 PM2IP 消息转发到次端口上的 CXL 组件,具体遵循以下规则。交换机应在主端口响应之前先聚合来自次端口的 IP2PM 消息,具体遵循以下规则。(PM 命令参见表 3-1)。在与池化设备 (Pooled Device) 通信时,这些消息在两个方向上都应携带 LD-ID TLP 前缀。</td></tr>
</tbody>
</table>

> **Table 9-2.** CXL Switch Behavior Message Aggregation Rules | CXL 交换机消息聚合规则
>
> | PM Logical Opcode Value | PM Command | Action |
> |---|---|---|
> | 0 | AGENT_INFO | • Do not forward PM2IP messages to downstream Devices.<br>• Execute Credits and PM Initialization flow against the downstream entity whenever a link trains up in CXL mode.<br>• Save CAPABILITY_VECTOR from the response. |
> | 2 | RESETPREP | • Never forward PM2IP messages to PCIe links.<br>• Forward PM2IP messages to all active downstream CXL links.<br>• Gather the IP2PM messages from all active downstream CXL links. |
> | 4 | PMREQ | • Never forward PM2IP messages to PCIe links.<br>• Forward PM2IP messages to all active downstream CXL links.<br>• Gather the IP2PM messages from all active downstream CXL links. "Conglomerate" Latency Tolerance Reporting (LTR) requests from all Devices by following the rules defined in LTR Mechanism section in PCIe Base Specification. |
> | 6 | GPF | • Never forward PM2IP messages to PCIe links.<br>• Never forward PM2IP messages to all downstream CXL links that returned CAPABILITY_VECTOR[1]=0.<br>• Forward PM2IP messages to all downstream CXL links that returned CAPABILITY_VECTOR[1]=1 and gather the IP2PM responses from all such links. |
> | FEh | CREDIT_RTN | • Do not forward PM2IP message to downstream Devices.<br>• PM Credit management on the primary interface is independent of PM credit management on the secondary interface. |
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_09/page_0800.png)

> **Figure 9-1.** PMREQ/RESETPREP Propagation by CXL Switch | CXL 交换机对 PMREQ/RESETPREP 的传播
>
> <img src="figures/chapter_09/fig_0801_1.png" alt="Figure 9-1" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_09/fig_0801_1.png)

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-2"></a>
## 9.2 CXL Device Boot Flow | CXL 设备启动流程

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.2 CXL Device Boot Flow</strong></td><td style="background-color:#e8e8e8"><strong>9.2 CXL 设备启动流程</strong></td></tr>
<tr><td>CXL devices shall follow the appropriate form factor specification regarding the boot flows.</td><td style="background-color:#e8e8e8">CXL 设备应遵循适用的形态因子规范中关于启动流程的规定。</td></tr>
<tr><td>This specification uses the terms "Warm Reset" and "Cold Reset" in a manner that is consistent with PCIe Base Specification.</td><td style="background-color:#e8e8e8">本规范中"暖复位"和"冷复位"术语的使用与 PCIe 基本规范一致。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-3"></a>
## 9.3 CXL System Reset Entry Flow | CXL 系统复位进入流程

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.3 CXL System Reset Entry Flow</strong></td><td style="background-color:#e8e8e8"><strong>9.3 CXL 系统复位进入流程</strong></td></tr>
<tr><td>In an OS-orchestrated reset flow, it is expected that the CXL devices are already in an Inactive State with their contexts flushed to the system memory or CXL-attached memory before the platform reset flow is triggered.</td><td style="background-color:#e8e8e8">在操作系统编排的复位流程中,期望在平台复位流程触发之前,CXL 设备已经处于非活动状态 (Inactive State),其上下文已刷新到系统内存或 CXL 连接的内存中。</td></tr>
<tr><td>In a platform-triggered reset flow (e.g., due to a fatal error), a CXL device may not be in an Inactive State when the device receives the ResetPrep message.</td><td style="background-color:#e8e8e8">在平台触发的复位流程中 (例如,由于致命错误),CXL 设备在接收到 ResetPrep 消息时可能未处于非活动状态。</td></tr>
<tr><td>During system reset flow, the host shall issue a CXL PM VDM (see Table 3-1) to the downstream CXL components with the following values:</td><td style="background-color:#e8e8e8">在系统复位流程中,主机应向下游 CXL 组件发出 CXL PM VDM (见表 3-1),其值如下:</td></tr>
<tr><td>• PM Logical Opcode[7:0]=RESETPREP</td><td style="background-color:#e8e8e8">• PM 逻辑操作码 [7:0]=RESETPREP</td></tr>
<tr><td>• Parameter[15:0]=REQUEST</td><td style="background-color:#e8e8e8">• 参数 [15:0]=REQUEST (请求)</td></tr>
<tr><td>• ResetType = System Reset</td><td style="background-color:#e8e8e8">• ResetType = System Reset (系统复位)</td></tr>
<tr><td>• PrepType = General Prep</td><td style="background-color:#e8e8e8">• PrepType = General Prep (通用准备)</td></tr>
<tr><td>The CXL device shall flush any relevant context to the host, clean up the data serving the host, and then place any CXL device connected memory into a safe state such as self-refresh. The CXL device shall take any additional steps that are necessary for the CXL host to enter LTSSM Hot Reset. After all the Reset preparation is complete, the CXL device shall issue a CXL PM VDM with the following value:</td><td style="background-color:#e8e8e8">CXL 设备应将任何相关的上下文刷新到主机,清理为主机服务的数据,然后将任何 CXL 设备连接的内存置于安全状态 (例如自刷新)。CXL 设备应采取 CXL 主机进入 LTSSM Hot Reset 状态所需的任何额外步骤。在完成所有复位准备工作后,CXL 设备应发出以下值的 CXL PM VDM:</td></tr>
<tr><td>• PM Logical Opcode[7:0]=RESETPREP</td><td style="background-color:#e8e8e8">• PM 逻辑操作码 [7:0]=RESETPREP</td></tr>
<tr><td>• Parameter[15:0]=RESPONSE</td><td style="background-color:#e8e8e8">• 参数 [15:0]=RESPONSE (响应)</td></tr>
<tr><td>• ResetType = System Reset</td><td style="background-color:#e8e8e8">• ResetType = System Reset</td></tr>
<tr><td>• PrepType = General Prep</td><td style="background-color:#e8e8e8">• PrepType = General Prep</td></tr>
<tr><td>The CXL device may have PERST# asserted after the reset handshake is complete. On PERST# assertion, the CXL device should clear any sticky content internal to the device unless they are on auxiliary power. The CXL device's handling of sticky register state is consistent with PCIe Base Specification.</td><td style="background-color:#e8e8e8">在复位握手完成后,CXL 设备的 PERST# 可能会被断言。在 PERST# 断言时,除非设备由辅助电源供电,否则 CXL 设备应清除设备内部的任何粘滞 (Sticky) 内容。CXL 设备对粘滞寄存器状态的处理与 PCIe 基本规范一致。</td></tr>
<tr><td>To prevent a deadlock in the case where one or more downstream components do not respond with an Ack, the host must implement a timeout, after which the host proceeds as if the response has been received.</td><td style="background-color:#e8e8e8">为防止在一个或多个下游组件未以 Ack 响应时发生死锁,主机必须实现超时机制,在此之后主机假定已收到响应并继续执行。</td></tr>
</tbody>
</table>

> **Figure 9-2.** CXL Device Reset Entry Flow | CXL 设备复位进入流程
>
> <img src="figures/chapter_09/fig_0802_1.png" alt="Figure 9-2" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_09/fig_0802_1.png)

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-4"></a>
## 9.4 CXL Device Sleep State Entry Flow | CXL 设备睡眠状态进入流程

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.4 CXL Device Sleep State Entry Flow</strong></td><td style="background-color:#e8e8e8"><strong>9.4 CXL 设备睡眠状态进入流程</strong></td></tr>
<tr><td>Since OS is always the orchestrator of Sx entry flows, it is expected that the CXL devices are already in an Inactive State with their contexts flushed to the CPU-attached memory or CXL-attached memory before the Sx entry flow is triggered.</td><td style="background-color:#e8e8e8">由于操作系统始终是 Sx 进入流程的编排者,期望在 Sx 进入流程触发之前,CXL 设备已经处于非活动状态,其上下文已刷新到 CPU 连接的内存或 CXL 连接的内存中。</td></tr>
<tr><td>During Sx entry flow, the host shall issue a CXL PM VDM (see Table 3-1) to the downstream components with the following values:</td><td style="background-color:#e8e8e8">在 Sx 进入流程中,主机应向下游组件发出 CXL PM VDM (见表 3-1),其值如下:</td></tr>
<tr><td>• PM Logical Opcode[7:0]=RESETPREP</td><td style="background-color:#e8e8e8">• PM 逻辑操作码 [7:0]=RESETPREP</td></tr>
<tr><td>• Parameter[15:0]=REQUEST</td><td style="background-color:#e8e8e8">• 参数 [15:0]=REQUEST</td></tr>
<tr><td>• ResetType = System transition from S0 to Sx (S1, S3, S4, or S5)</td><td style="background-color:#e8e8e8">• ResetType = 系统从 S0 到 Sx 的转换 (S1、S3、S4 或 S5)</td></tr>
<tr><td>• PrepType = General Prep</td><td style="background-color:#e8e8e8">• PrepType = General Prep</td></tr>
<tr><td>The CXL device shall flush any relevant context to the host, clean up the data serving the host, and then place any CXL device connected memory into a safe state such as self-refresh. The CXL device shall take any additional steps that are necessary for the CXL host to initiate an L2 entry flow. After all the Sx preparation is complete, the CXL device shall issue a CXL PM VDM with the following values:</td><td style="background-color:#e8e8e8">CXL 设备应将任何相关的上下文刷新到主机,清理为主机服务的数据,然后将任何 CXL 设备连接的内存置于安全状态 (如自刷新)。CXL 设备应采取 CXL 主机启动 L2 进入流程所需的任何额外步骤。在完成所有 Sx 准备工作后,CXL 设备应发出以下值的 CXL PM VDM:</td></tr>
<tr><td>• PM Logical Opcode[7:0]=RESETPREP</td><td style="background-color:#e8e8e8">• PM 逻辑操作码 [7:0]=RESETPREP</td></tr>
<tr><td>• Parameter[15:0]=RESPONSE</td><td style="background-color:#e8e8e8">• 参数 [15:0]=RESPONSE</td></tr>
<tr><td>• ResetType = System transition from S0 to Sx (based on the target sleep state)</td><td style="background-color:#e8e8e8">• ResetType = 系统从 S0 到 Sx 的转换 (基于目标睡眠状态)</td></tr>
<tr><td>• PrepType = General Prep</td><td style="background-color:#e8e8e8">• PrepType = General Prep</td></tr>
<tr><td>PERST# to the CXL device may be asserted any time after this handshake is complete. On PERST# assertion, the CXL device should clear any sticky content internal to the device unless they are on auxiliary power. The CXL device's handling of sticky register state is consistent with PCIe Base Specification.</td><td style="background-color:#e8e8e8">在该握手完成后的任何时间,CXL 设备的 PERST# 都可能被断言。在 PERST# 断言时,除非设备由辅助电源供电,否则 CXL 设备应清除设备内部的任何粘滞内容。CXL 设备对粘滞寄存器状态的处理与 PCIe 基本规范一致。</td></tr>
<tr><td>CXL.mem-capable adapters may need auxiliary power to retain memory context across S3.</td><td style="background-color:#e8e8e8">支持 CXL.mem 的适配器可能需要辅助电源以在 S3 期间保留内存上下文。</td></tr>
<tr><td>Note: PERST# shall always be asserted for CXL Sx Entry flows.</td><td style="background-color:#e8e8e8">注:对于 CXL Sx 进入流程,必须始终断言 PERST#。</td></tr>
</tbody>
</table>

> **Figure 9-3.** CXL Device Sleep State Entry Flow | CXL 设备睡眠状态进入流程
>
> <img src="figures/chapter_09/fig_0803_1.png" alt="Figure 9-3" width="700">
>
> *Original page render @ 150 DPI* — [📄 Full size](figures/chapter_09/fig_0803_1.png)

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-5"></a>
## 9.5 Function Level Reset (FLR) | 功能级复位 (FLR)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.5 Function Level Reset (FLR)</strong></td><td style="background-color:#e8e8e8"><strong>9.5 功能级复位 (FLR)</strong></td></tr>
<tr><td>The PCIe FLR mechanism enables software to quiesce and reset Endpoint hardware with Function-level granularity. CXL devices expose one or more PCIe functions to host software. These functions can expose FLR capability and existing PCIe-compatible software can issue an FLR to these functions. PCIe Base Specification provides specific guidelines regarding the impact of an FLR on PCIe function level state and control registers. For compatibility with existing PCIe software, CXL PCIe functions shall follow those guidelines if the Functions support FLR. For example, any software-readable state that potentially includes secret information associated with any preceding use of the Function must be cleared by an FLR.</td><td style="background-color:#e8e8e8">PCIe FLR 机制使软件能够以功能 (Function) 级粒度静默并复位 Endpoint 硬件。CXL 设备向主机软件公开一个或多个 PCIe 功能。这些功能可以公开 FLR 能力,且现有的兼容 PCIe 的软件可以对这些功能发出 FLR。PCIe 基本规范提供了关于 FLR 对 PCIe 功能级状态和控制寄存器影响的具体准则。为了与现有 PCIe 软件兼容,如果这些功能支持 FLR,CXL PCIe 功能应遵循这些准则。例如,任何可能包含与该功能先前使用相关的秘密信息的软件可读状态必须由 FLR 清除。</td></tr>
<tr><td>FLRs do not affect the CXL.cache and CXL.mem protocols. Any CXL.cache-related and CXL.mem-related control registers, including CXL DVSEC structures and state held by the CXL device, are not affected by FLRs. The memory controller that hosts the HDM is not reset by an FLR. After an FLR, all address translations associated with the corresponding Function are invalidated in accordance with PCIe Base Specification. Since the CXL Function accesses cache using the system physical address held in the address translation cache, the Function is unable to access any cachelines after the FLR until software explicitly re-enables ATS. The device is not required to write back its cache during an FLR flow. To avoid an adverse effect on the performance of other Functions, it is strongly recommended that the device not write back its cache content during an FLR if the cache is shared by multiple functions. Cache coherency must be maintained.</td><td style="background-color:#e8e8e8">FLR 不会影响 CXL.cache 和 CXL.mem 协议。任何与 CXL.cache 和 CXL.mem 相关的控制寄存器 (包括 CXL DVSEC 结构和 CXL 设备持有的状态) 都不受 FLR 影响。托管 HDM 的内存控制器也不会被 FLR 复位。FLR 之后,与对应功能相关的所有地址转换 (Address Translation) 将按照 PCIe 基本规范失效。由于 CXL 功能使用地址转换缓存中保存的系统物理地址访问缓存,因此在 FLR 之后,在软件明确重新启用 ATS 之前,该功能无法访问任何缓存行。设备在 FLR 流程中不需要回写其缓存。为避免对其他功能的性能产生不利影响,强烈建议设备在 FLR 期间,当缓存由多个功能共享时不要回写其缓存内容。必须保持缓存一致性。</td></tr>
<tr><td>In some cases, system software may use an FLR to attempt error recovery. In the context of CXL devices, errors in CXL.cache logic and in CXL.mem logic cannot be recovered by an FLR. An FLR may succeed in recovering from CXL.io domain errors.</td><td style="background-color:#e8e8e8">在某些情况下,系统软件可能会使用 FLR 尝试错误恢复。在 CXL 设备的上下文中,CXL.cache 逻辑和 CXL.mem 逻辑中的错误无法通过 FLR 恢复。FLR 可能会成功恢复 CXL.io 域错误。</td></tr>
<tr><td>In a CXL device other than an eRCD, all Functions that participate in CXL.cache or CXL.mem are required to support either FLR or CXL Reset (see Section 9.7).</td><td style="background-color:#e8e8e8">在除 eRCD 以外的 CXL 设备中,所有参与 CXL.cache 或 CXL.mem 的功能必须支持 FLR 或 CXL 复位 (见 9.7 节)。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-6"></a>
## 9.6 Cache Management | 缓存管理

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.6 Cache Management</strong></td><td style="background-color:#e8e8e8"><strong>9.6 缓存管理</strong></td></tr>
<tr><td>A CXL-unaware OS or PCIe bus driver is unaware of CXL.cache capability. The device driver is expected to be aware of this CXL.cache capability and may manage the CXL.cache. Software shall not assume that lines in device cache that map to HDM will be flushed by CPU cache flush instructions. The behavior may vary from one host to another.</td><td style="background-color:#e8e8e8">不支持 CXL 的操作系统或 PCIe 总线驱动不知道 CXL.cache 能力。设备驱动程序应了解此 CXL.cache 能力并可能管理 CXL.cache。软件不应假设映射到 HDM 的设备缓存行会通过 CPU 缓存刷新指令被刷新。不同主机的行为可能有所不同。</td></tr>
<tr><td>System software may wish to ensure that a CXL.cache-capable device does not contain any valid cachelines without resetting the system or the entire device. Since a device is not required to clear cache contents upon FLR, separate control and status bits are defined for this purpose. This capability is highly recommended for CXL.cache-capable eRCDs and mandatory for all other CXL.cache-capable devices. The capability is advertised via the Cache Writeback and Invalidate Capable flag in the DVSEC CXL Capability register (see Section 8.1.3.1).</td><td style="background-color:#e8e8e8">系统软件可能希望确保支持 CXL.cache 的设备在不复位系统或整个设备的情况下不包含任何有效的缓存行。由于 FLR 时设备不需要清除缓存内容,因此为此目的定义了单独的控制位和状态位。该能力对于支持 CXL.cache 的 eRCD 强烈建议使用,对于所有其他支持 CXL.cache 的设备则是强制性的。该能力通过 DVSEC CXL Capability 寄存器中的 Cache Writeback and Invalidate Capable 标志来公布 (见 8.1.3.1 节)。</td></tr>
<tr><td>Software shall take the following steps to ensure that the Device does not contain any valid cachelines:</td><td style="background-color:#e8e8e8">软件应采取以下步骤以确保设备不包含任何有效的缓存行:</td></tr>
<tr><td>1. Set Disable Caching=1. This bit is located in the DVSEC CXL Control2 register (see Section 8.1.3.4).</td><td style="background-color:#e8e8e8">1. 设置 Disable Caching=1。此位位于 DVSEC CXL Control2 寄存器中 (见 8.1.3.4 节)。</td></tr>
<tr><td>2. Set Initiate Cache Write Back and Invalidation=1. This step may be combined with the previous step as a single configuration space register write to the DVSEC CXL Control2 register (see Section 8.1.3.4).</td><td style="background-color:#e8e8e8">2. 设置 Initiate Cache Write Back and Invalidation=1。此步骤可以与上一步合并,作为对 DVSEC CXL Control2 寄存器的一次配置空间寄存器写入 (见 8.1.3.4 节)。</td></tr>
<tr><td>3. Wait until Cache Invalid=1. This bit is located in the DVSEC CXL Status2 register (see Section 8.1.3.5). Software may leverage the cache size reported in the DVSEC CXL Capability2 register (see Section 8.1.3.7) to compute a suitable timeout value.</td><td style="background-color:#e8e8e8">3. 等待直到 Cache Invalid=1。此位位于 DVSEC CXL Status2 寄存器中 (见 8.1.3.5 节)。软件可以利用 DVSEC CXL Capability2 寄存器 (见 8.1.3.7 节) 中报告的缓存大小来计算合适的超时值。</td></tr>
<tr><td>Software is required to Set Disable Caching=0 to re-enable caching. When the Disable Caching bit transitions from 1 to 0, the device shall transition the Cache Invalid bit to 0 if it was previously set to 1.</td><td style="background-color:#e8e8e8">软件必须将 Disable Caching 设置为 0 以重新启用缓存。当 Disable Caching 位从 1 转换为 0 时,如果之前 Cache Invalid 位被设置为 1,则设备应将 Cache Invalid 位转换为 0。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录)

<a id="sec-9-7"></a>
## 9.7 CXL Reset | CXL 复位

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.7 CXL Reset</strong></td><td style="background-color:#e8e8e8"><strong>9.7 CXL 复位</strong></td></tr>
<tr><td>CXL.cache resources and CXL.mem resources such as controllers, buffers, and caches are likely to be shared at the device level. CXL Reset is a mechanism that is used to reset all CXL.cache states and CXL.mem states in addition to CXL.io in all non-Virtual Functions that support CXL.cache protocols and/or CXL.mem protocols. Reset of CXL.io has the same scope as FLR. Section 9.5 describes FLR in the context of CXL devices.</td><td style="background-color:#e8e8e8">CXL.cache 资源和 CXL.mem 资源 (如控制器、缓冲区和缓存) 可能在设备级别共享。CXL 复位是一种机制,用于在支持 CXL.cache 协议和/或 CXL.mem 协议的所有非虚拟功能 (Non-Virtual Function) 中复位所有 CXL.cache 状态和 CXL.mem 状态以及 CXL.io 状态。CXL.io 复位的范围与 FLR 相同。9.5 节描述了 CXL 设备中的 FLR。</td></tr>
<tr><td>CXL Reset will not affect non-CXL Functions or the physical link. Non-CXL Function Map DVSEC capability is used to advertise to the System Software which non-Virtual Functions are considered non-CXL (i.e., they neither participate in CXL.cache nor in CXL.mem).</td><td style="background-color:#e8e8e8">CXL 复位不会影响非 CXL 功能或物理链路。Non-CXL Function Map DVSEC 能力用于向系统软件通告哪些非虚拟功能被视为非 CXL (即它们既不参与 CXL.cache 也不参与 CXL.mem)。</td></tr>
<tr><td>All Functions in an SLD that participate in CXL.cache or CXL.mem are required to support either FLR or CXL Reset. MLDs, on the other hand, are required to support CXL Reset.</td><td style="background-color:#e8e8e8">SLD 中所有参与 CXL.cache 或 CXL.mem 的功能必须支持 FLR 或 CXL 复位。另一方面,MLD 必须支持 CXL 复位。</td></tr>
<tr><td>Capability, Control, and Status fields for CXL Reset are exposed in configuration space of Function 0 of a CXL device but these affect all physical and virtual functions within the device that participate in CXL.cache or CXL.mem.</td><td style="background-color:#e8e8e8">CXL 复位的能力 (Capability)、控制 (Control) 和状态 (Status) 字段在 CXL 设备 Function 0 的配置空间中公开,但这些字段会影响设备中所有参与 CXL.cache 或 CXL.mem 的物理功能和虚拟功能。</td></tr>
<tr><td>The system software is responsible for quiescing all the Functions that are impacted due to reset of the CXL.cache state and CXL.mem state in the device and offlining any associated HDM ranges. Once the CXL Reset is complete, all CXL Functions on the device must be re-initialized prior to use.</td><td style="background-color:#e8e8e8">系统软件负责静默设备中所有受 CXL.cache 状态和 CXL.mem 状态复位影响的功能,并下线任何相关的 HDM 范围。一旦 CXL 复位完成,设备上的所有 CXL 功能必须在使用前重新初始化。</td></tr>
<tr><td>CXL Reset may be issued by the System Software or the Fabric Manager. To quiesce the impacted non-virtual Functions prior to issuing CXL Reset, the System Software shall complete the following actions for each of the CXL non-virtual Functions:</td><td style="background-color:#e8e8e8">CXL 复位可由系统软件或 Fabric Manager (FM) 发出。为了在发出 CXL 复位之前静默受影响的非虚拟功能,系统软件应为每个 CXL 非虚拟功能完成以下操作:</td></tr>
<tr><td>1. Offline any volatile or persistent HDM Ranges. When offlining is complete, there shall be no outstanding or new CXL.mem transactions to the affected CXL Functions.</td><td style="background-color:#e8e8e8">1. 下线任何易失或持久 HDM 范围。下线完成后,不应有未完成或新的 CXL.mem 事务指向受影响的 CXL 功能。</td></tr>
<tr><td>2. Configure these Functions to stop initiating new CXL.io requests. This procedure is identical to that for FLR.</td><td style="background-color:#e8e8e8">2. 配置这些功能以停止发起新的 CXL.io 请求。此过程与 FLR 相同。</td></tr>
<tr><td>The FM may issue CXL Reset for various cases described in Chapter 7.0. In the case of the FM use of CXL Reset, there may be outstanding commands in the device which shall be silently discarded.</td><td style="background-color:#e8e8e8">FM 可针对第 7 章中描述的各种情况发出 CXL 复位。在 FM 使用 CXL 复位的情况下,设备中可能存在应被静默丢弃的未完成命令。</td></tr>
<tr><td>CXL.io reset of the device shall follow the definition of FLR in PCIe Base Specification. Note that only PCIe-mapped memory shall be cleared or randomized by the non-virtual Functions during FLR.</td><td style="background-color:#e8e8e8">设备的 CXL.io 复位应遵循 PCIe 基本规范中 FLR 的定义。请注意,在 FLR 期间,只有 PCIe 映射的内存应由非虚拟功能清除或随机化。</td></tr>
<tr><td>Reset of the CXL.cache state and CXL.mem state as part of the CXL Reset flow at the device level has the following behavior:</td><td style="background-color:#e8e8e8">作为设备级 CXL 复位流程的一部分,对 CXL.cache 状态和 CXL.mem 状态的复位具有以下行为:</td></tr>
<tr><td>• All outstanding or new CXL.mem reads shall be silently discarded. Previously accepted writes to persistent HDM ranges shall be persisted. Writes to volatile HDM ranges may be discarded.</td><td style="background-color:#e8e8e8">• 所有未完成或新的 CXL.mem 读操作应被静默丢弃。先前接受的持久 HDM 范围写入应被持久化。对易失 HDM 范围的写入可被丢弃。</td></tr>
<tr><td>• The device caches (Type 1 Devices and Type 2 Devices) shall be written back and invalidated by the device. Software is not required to write back and invalidate the device cache (see Section 9.6) prior to issuing the CXL Reset.</td><td style="background-color:#e8e8e8">• 设备缓存 (Type 1 设备和 Type 2 设备) 应由设备回写并使其失效。在发出 CXL 复位之前,软件无需回写并使设备缓存失效 (见 9.6 节)。</td></tr>
<tr><td>• No new CXL.cache requests shall be issued except for the above cache-flushing operation. Snoops shall continue to be serviced.</td><td style="background-color:#e8e8e8">• 除上述缓存刷新操作外,不应发出新的 CXL.cache 请求。窥探 (Snoop) 应继续被服务。</td></tr>
<tr><td>• Contents of volatile HDM ranges may or may not be retained and the device may optionally clear or randomize these ranges if this capability is supported and is requested during CXL Reset (see the CXL Reset Mem Clr Capable bit in the DVSEC CXL Capability register and the CXL Reset Mem Clr Enable bit in the DVSEC CXL Control2 register in Section 8.1.3.1 and Section 8.1.3.4, respectively). Contents of the persistent HDM ranges will be retained by the device.</td><td style="background-color:#e8e8e8">• 易失 HDM 范围的内容可能会也可能不会被保留,并且如果支持此能力并在 CXL 复位期间被请求,设备可选择清除或随机化这些范围 (分别参见 8.1.3.1 节中 DVSEC CXL Capability 寄存器的 CXL Reset Mem Clr Capable 位和 8.1.3.4 节中 DVSEC CXL Control2 寄存器的 CXL Reset Mem Clr Enable 位)。持久 HDM 范围的内容将由设备保留。</td></tr>
<tr><td>• Any errors during a CXL Reset shall be logged in the error status registers in the usual manner. Failure to complete a CXL Reset shall result in the CXL Reset Error bit in the DVSEC CXL Status2 Register being set. The system software may choose to retry CXL Reset, assert other types of device resets, or restart the system in response to a CXL Reset failure.</td><td style="background-color:#e8e8e8">• CXL 复位期间的任何错误应以通常方式记录在错误状态寄存器中。未能完成 CXL 复位将导致 DVSEC CXL Status2 寄存器中的 CXL Reset Error 位置位。系统软件可选择重试 CXL 复位、断言其他类型的设备复位或响应 CXL 复位失败而重新启动系统。</td></tr>
<tr><td>• Unless specified otherwise, all non-sticky registers defined in this specification shall be initialized to their default values upon CXL Reset. The CONFIG_LOCK bit in the DVSEC Config Lock register (see Section 8.1.3.6) and any register fields that are locked by CONFIG_LOCK shall not be affected by CXL Reset. Any sticky registers, such as the error status registers, shall be preserved across CXL Reset. If the device is in the viral state, it shall remain in that state after a CXL Reset.</td><td style="background-color:#e8e8e8">• 除非另有规定,本规范中定义的所有非粘滞寄存器应在 CXL 复位时初始化为其默认值。DVSEC Config Lock 寄存器中的 CONFIG_LOCK 位 (见 8.1.3.6 节) 以及被 CONFIG_LOCK 锁定的任何寄存器字段不受 CXL 复位影响。任何粘滞寄存器 (如错误状态寄存器) 应在 CXL 复位期间保留。如果设备处于病毒 (Viral) 状态,则在 CXL 复位后应保持该状态。</td></tr>
<tr><td>If the device is unable to complete CXL Reset within the specified timeout period, the System Software shall consider this a failure and may choose to take action similar to when the CXL Reset Error bit is set.</td><td style="background-color:#e8e8e8">如果设备在指定的超时时间内无法完成 CXL 复位,系统软件应将其视为失败,并可选择采取与 CXL Reset Error 位置位时类似的措施。</td></tr>
<tr><td>A pooled Type 3 device (MLD) must ensure that only the LD assigned to the host that is issuing CXL Reset is impacted. This includes the clearing or randomizing of the volatile HDM ranges on the device. Other LDs must continue to operate normally.</td><td style="background-color:#e8e8e8">池化的 Type 3 设备 (MLD) 必须确保只有分配给发出 CXL 复位的主机的 LD 受影响。这包括清除或随机化设备上的易失 HDM 范围。其他 LD 必须继续正常运行。</td></tr>
</tbody>
</table>

<a id="sec-9-7-1"></a>
### 9.7.1 Effect on the Contents of the Volatile HDM | 对易失 HDM 内容的影响

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.7.1 Effect on the Contents of the Volatile HDM</strong></td><td style="background-color:#e8e8e8"><strong>9.7.1 对易失 HDM 内容的影响</strong></td></tr>
<tr><td>Because ownership of the volatile HDM ranges may change following a CXL Reset, it is important to ensure that there is no leak of volatile memory content that was present prior to the CXL Reset. (This condition does not apply to persistent memory content whose security is ensured by other means not discussed here.)</td><td style="background-color:#e8e8e8">由于易失 HDM 范围的所有权可能在 CXL 复位后发生变化,因此必须确保 CXL 复位之前存在的易失内存内容不会泄露。(此条件不适用于持久内存内容,其安全性由此处未讨论的其他方式确保。)</td></tr>
<tr><td>There are two cases to consider:</td><td style="background-color:#e8e8e8">需要考虑两种情况:</td></tr>
<tr><td>• The device remains bound to the same host and the System Software reallocates the volatile HDM ranges to a different software entity. The System Software is often responsible for ensuring that the memory range is re-initialized prior to any allocation. The device may implement an optional capability to perform clearing or randomizing of all impacted volatile HDM ranges. This may be invoked using the optional Secure Erase function (see Section 8.2.10.9.5.2). Optionally, the device may be capable of clearing or randomizing volatile HDM content as part of CXL Reset. If this capability is available, the System Software may take advantage of it. However, since this is an optional capability, the System Software should not depend on it.</td><td style="background-color:#e8e8e8">• 设备仍绑定到同一主机,系统软件将易失 HDM 范围重新分配给不同的软件实体。系统软件通常负责确保在任何分配之前重新初始化内存范围。设备可实现可选能力以执行所有受影响的易失 HDM 范围的清除或随机化。这可以使用可选的 Secure Erase 函数 (见 8.2.10.9.5.2 节) 调用。可选地,设备可以能够作为 CXL 复位的一部分来清除或随机化易失 HDM 内容。如果此能力可用,系统软件可利用它。但是,由于这是可选能力,系统软件不应依赖它。</td></tr>
<tr><td>• The device is migrated to a different host with FM involvement as described in Chapter 7.0. The FM must use either Secure Erase operation (see Section 8.2.10.9.5.2) or utilize CXL Reset if the CXL Reset Mem Clr capability exists to clear or randomize any volatile HDM ranges prior to re-assigning device to a different host.</td><td style="background-color:#e8e8e8">• 设备在 FM 参与下迁移到另一台主机 (如第 7 章所述)。FM 必须使用 Secure Erase 操作 (见 8.2.10.9.5.2 节) 或利用 CXL 复位 (如果存在 CXL Reset Mem Clr 能力) 以便在将设备重新分配给另一台主机之前清除或随机化任何易失 HDM 范围。</td></tr>
<tr><td>Capability for clearing and randomizing volatile HDM ranges in the device is reported by the CXL Reset Mem Clr Capable bit in the DVSEC CXL Capability register. If present, this capability may optionally be used by setting the CXL Reset Mem Clr Enable bit in the DVSEC CXL Control2 register.</td><td style="background-color:#e8e8e8">设备中清除和随机化易失 HDM 范围的能力由 DVSEC CXL Capability 寄存器中的 CXL Reset Mem Clr Capable 位报告。如果存在,则可以通过设置 DVSEC CXL Control2 寄存器中的 CXL Reset Mem Clr Enable 位来选择性地使用此能力。</td></tr>
</tbody>
</table>

<a id="sec-9-7-2"></a>
### 9.7.2 Software Actions | 软件操作

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.7.2 Software Actions</strong></td><td style="background-color:#e8e8e8"><strong>9.7.2 软件操作</strong></td></tr>
<tr><td>System Software or Fabric Manager shall follow these steps while performing CXL Reset:</td><td style="background-color:#e8e8e8">在执行 CXL 复位时,系统软件或 Fabric Manager 应遵循以下步骤:</td></tr>
<tr><td>1. Verify that the device supports CXL Reset by consulting the CXL Reset Capable bit in the DVSEC CXL Capability register (see Section 8.1.3.1).</td><td style="background-color:#e8e8e8">1. 通过查看 DVSEC CXL Capability 寄存器中的 CXL Reset Capable 位,确认设备支持 CXL 复位 (见 8.1.3.1 节)。</td></tr>
<tr><td>2. Prepare the system for CXL Reset as described in Section 9.7.</td><td style="background-color:#e8e8e8">2. 按照 9.7 节所述为 CXL 复位准备系统。</td></tr>
<tr><td>3. Determine whether the device supports the CXL Reset Mem Clr capability bit by consulting the DVSEC CXL Capability register (see Section 8.1.3.1).</td><td style="background-color:#e8e8e8">3. 通过查看 DVSEC CXL Capability 寄存器 (见 8.1.3.1 节),确定设备是否支持 CXL Reset Mem Clr 能力位。</td></tr>
<tr><td>4. If the device supports the CXL Reset Mem Clr capability, program the CXL Reset Mem Clr Enable bit in the DVSEC CXL Control2 register (see Section 8.1.3.4) as required.</td><td style="background-color:#e8e8e8">4. 如果设备支持 CXL Reset Mem Clr 能力,则根据需要编程 DVSEC CXL Control2 寄存器 (见 8.1.3.4 节) 中的 CXL Reset Mem Clr Enable 位。</td></tr>
<tr><td>5. Determine the timeout for completion by consulting the CXL Reset Timeout field in the DVSEC CXL Capability register.</td><td style="background-color:#e8e8e8">5. 通过查看 DVSEC CXL Capability 寄存器中的 CXL Reset Timeout 字段,确定完成的超时时间。</td></tr>
<tr><td>6. Set the Initiate CXL Reset=1 in the DVSEC CXL Control2 register.</td><td style="background-color:#e8e8e8">6. 在 DVSEC CXL Control2 寄存器中设置 Initiate CXL Reset=1。</td></tr>
<tr><td>7. Wait for CXL Reset Complete=1 or CXL Reset Error=1 in the DVSEC CXL Status2 register (see Section 8.1.3.5) for up to the timeout period.</td><td style="background-color:#e8e8e8">7. 在 DVSEC CXL Status2 寄存器 (见 8.1.3.5 节) 中等待 CXL Reset Complete=1 或 CXL Reset Error=1,等待时间最长不超过超时时间。</td></tr>
<tr><td>System Software should follow these steps while re-initializing and onlining a device:</td><td style="background-color:#e8e8e8">在重新初始化并上线设备时,系统软件应遵循以下步骤:</td></tr>
<tr><td>1. Set up the device as required to enable functions impacted by CXL Reset.</td><td style="background-color:#e8e8e8">1. 根据需要设置设备以启用受 CXL 复位影响的功能。</td></tr>
<tr><td>2. Optionally check whether the device performed clearing or randomizing of memory during the CXL Reset. If yes, skip software-based initialization prior to re-allocation. If not, perform software-based initialization.</td><td style="background-color:#e8e8e8">2. 可选地检查设备是否在 CXL 复位期间执行了内存清除或随机化。如果是,则在重新分配之前跳过基于软件的初始化。如果不是,则执行基于软件的初始化。</td></tr>
</tbody>
</table>

<a id="sec-9-7-3"></a>
### 9.7.3 CXL Reset and Request Retry Status (RRS) | CXL 复位与请求重试状态 (RRS)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.7.3 CXL Reset and Request Retry Status (RRS)</strong></td><td style="background-color:#e8e8e8"><strong>9.7.3 CXL 复位与请求重试状态 (RRS)</strong></td></tr>
<tr><td>The device must successfully complete the configuration write that triggered the CXL Reset. The device behavior in response to Configuration Space access to the device within 100 ms of initiating a CXL Reset is undefined. After 100 ms from the issuance of CXL Reset, the CXL Function is permitted to return RRS for all Configuration Space accesses except to the CXL Status2 register. After 100 ms from the issuance of CXL Reset, software should not access any device register other than the CXL Status2 register until CXL Reset completion, timeout, or error.</td><td style="background-color:#e8e8e8">设备必须成功完成触发 CXL 复位的配置写入。设备对在启动 CXL 复位 100 ms 内对设备的配置空间访问的响应是未定义的。从发出 CXL 复位起 100 ms 后,CXL 功能可对除 CXL Status2 寄存器之外的所有配置空间访问返回 RRS。从发出 CXL 复位起 100 ms 后,在 CXL 复位完成、超时或出错之前,软件不应访问 CXL Status2 寄存器以外的任何设备寄存器。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录)

# 📘 第 9 章补充：9.8 - 9.20.2 (Chapter 9 Gap Fill: 9.8 - 9.20.2)

> **Source pages**: 808–878 | **File**: ch09_gap_fill.md | **Format**: 中英对照双语

---

## 📑 本章补充目录

- [9.8 全局持久刷新 (Global Persistent Flush, GPF)](#sec-9-8)
  - [9.8.1 主机与交换机职责 (Host and Switch Responsibilities)](#sec-9-8-1)
  - [9.8.2 设备职责 (Device Responsibilities)](#sec-9-8-2)
  - [9.8.3 能源预算 (Energy Budgeting)](#sec-9-8-3)
- [9.9 热插拔 (Hot-Plug)](#sec-9-9)
- [9.10 软件枚举 (Software Enumeration)](#sec-9-10)
- [9.11 RCD 枚举 (RCD Enumeration)](#sec-9-11)
  - [9.11.1 RCD 模式 (RCD Mode)](#sec-9-11-1)
  - [9.11.2 RCH 与 RCD 的 PCIe 软件视图 (PCIe Software View of an RCH and RCD)](#sec-9-11-2)
  - [9.11.3 RCH 与 RCD 的系统固件视图 (System Firmware View of an RCH and RCD)](#sec-9-11-3)
  - [9.11.4 RCH 与 RCD 的操作系统视图 (OS View of an RCH and RCD)](#sec-9-11-4)
  - [9.11.5 基于系统固件的 RCD 枚举流程 (System Firmware-based RCD Enumeration Flow)](#sec-9-11-5)
  - [9.11.6 RCD 发现 (RCD Discovery)](#sec-9-11-6)
  - [9.11.7 多 Flex Bus 链路的 eRCD (eRCDs with Multiple Flex Bus Links)](#sec-9-11-7)
  - [9.11.8 连接到 RCH 的 CXL 设备 (CXL Devices Attached to an RCH)](#sec-9-11-8)
- [9.12 CXL VH 枚举 (CXL VH Enumeration)](#sec-9-12)
  - [9.12.1 CXL 根端口 (CXL Root Ports)](#sec-9-12-1)
  - [9.12.2 CXL 虚拟层级 (CXL Virtual Hierarchy)](#sec-9-12-2)
  - [9.12.3 枚举 CXL RP 与 DSP (Enumerating CXL RPs and DSPs)](#sec-9-12-3)
  - [9.12.4 连接到 CXL RP 或 DSP 的 eRCD (eRCD Connected to a CXL RP or DSP)](#sec-9-12-4)
  - [9.12.5 CXL RP 与 DSP 下的 CXL eRCD — 示例 (CXL eRCD below a CXL RP and DSP - Example)](#sec-9-12-5)
  - [9.12.6 CXL VH 中链路与协议寄存器的映射 (Mapping of Link and Protocol Registers in CXL VH)](#sec-9-12-6)
- [9.13 HDM 的软件视图 (Software View of HDM)](#sec-9-13)
  - [9.13.1 内存交织 (Memory Interleaving)](#sec-9-13-1)
  - [9.13.2 CXL 内存设备标签存储区 (CXL Memory Device Label Storage Area)](#sec-9-13-2)
  - [9.13.3 动态容量设备 (Dynamic Capacity Device, DCD)](#sec-9-13-3)
  - [9.13.4 容量或性能降级 (Capacity or Performance Degradation)](#sec-9-13-4)
- [9.14 反向失效配置 (Back-Invalidate Configuration)](#sec-9-14)
  - [9.14.1 发现 (Discovery)](#sec-9-14-1)
  - [9.14.2 配置 (Configuration)](#sec-9-14-2)
  - [9.14.3 混合配置 (Mixed Configurations)](#sec-9-14-3)
- [9.15 Cache ID 配置与路由 (Cache ID Configuration and Routing)](#sec-9-15)
  - [9.15.1 主机能力 (Host Capabilities)](#sec-9-15-1)
  - [9.15.2 下游端口解码功能 (Downstream Port Decode Functionality)](#sec-9-15-2)
  - [9.15.3 上游交换机端口路由功能 (Upstream Switch Port Routing Functionality)](#sec-9-15-3)
  - [9.15.4 主机桥路由功能 (Host Bridge Routing Functionality)](#sec-9-15-4)
- [9.16 UIO 直连 P2P 到 HDM (UIO Direct P2P to HDM)](#sec-9-16)
  - [9.16.1 UIO 直连 P2P 到 HDM 消息的处理 (Processing of UIO Direct P2P to HDM Messages)](#sec-9-16-1)
- [9.17 加速器的直连 P2P CXL.mem (Direct P2P CXL.mem for Accelerators)](#sec-9-17)
  - [9.17.1 对等 SLD 配置 (Peer SLD Configuration)](#sec-9-17-1)
  - [9.17.2 对等 MLD 配置 (Peer MLD Configuration)](#sec-9-17-2)
  - [9.17.3 对等 GFD 配置 (Peer GFD Configuration)](#sec-9-17-3)
- [9.18 CXL 操作系统固件接口扩展 (CXL OS Firmware Interface Extensions)](#sec-9-18)
  - [9.18.1 CXL 早期发现表 (CXL Early Discovery Table, CEDT)](#sec-9-18-1)
  - [9.18.2 CXL _OSC](#sec-9-18-2)
  - [9.18.3 CXL 根设备特定方法 (_DSM) (CXL Root Device Specific Methods (_DSM))](#sec-9-18-3)
- [9.19 CXL 设备可管理性模型 (Manageability Model for CXL Devices)](#sec-9-19)
- [9.20 组件命令接口 (Component Command Interface)](#sec-9-20)
  - [9.20.1 CCI 属性 (CCI Properties)](#sec-9-20-1)
  - [9.20.2 基于 MCTP 的 CCI 属性 (MCTP-based CCI Properties)](#sec-9-20-2)

---

<a id="sec-9-7-3"></a>
### 9.7.3 CXL Reset and Request Retry Status (RRS) | CXL 复位与请求重试状态

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The device must successfully complete the configuration write that triggered the CXL Reset. The device behavior in response to Configuration Space access to the device within 100 ms of initiating a CXL Reset is undefined. After 100 ms from the issuance of CXL Reset, the CXL Function is permitted to return RRS for all Configuration Space accesses except to the CXL Status2 register. After 100 ms from the issuance of CXL Reset, software should not access any device register other than the CXL Status2 register until CXL Reset completion, timeout, or error.</td><td style="background-color:#e8e8e8">设备必须成功完成触发 CXL 复位的配置写操作。在发起 CXL 复位后 100 ms 内，设备对 Configuration Space 访问的响应行为未定义。CXL 复位发出 100 ms 后，CXL Function 允许对所有 Configuration Space 访问返回 RRS，但对 CXL Status2 寄存器的访问除外。CXL 复位发出 100 ms 后，软件不应访问除 CXL Status2 寄存器以外的任何设备寄存器，直到 CXL 复位完成、超时或出错。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-8"></a>
## 9.8 Global Persistent Flush (GPF) | 全局持久刷新

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.8 Global Persistent Flush (GPF)</strong></td><td style="background-color:#e8e8e8"><strong>9.8 全局持久刷新</strong></td></tr>
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
<tr><td>Global Persistent Flush (GPF) is a hardware-based mechanism associated with persistent memory that is used to flush cache and memory buffers to a persistence domain. A persistence domain is defined as a location that is guaranteed to preserve the data contents across a restart of the device containing the data. GPF operation is global in nature because all CXL agents that are part of a cache coherency domain participate in the GPF flow. A CXL.cache coherency domain consists of one or more hosts, all CXL Root Ports that belong to these hosts, and the virtual hierarchies associated with these Root Ports.</td><td style="background-color:#e8e8e8">全局持久刷新 (Global Persistent Flush, GPF) 是一种与持久内存 (Persistent Memory) 关联的基于硬件的机制，用于将缓存和内存缓冲区刷新到持久域 (Persistence Domain)。持久域定义为保证在设备重启后仍能保留数据内容的位置。GPF 操作本质上是全局性的，因为作为 Cache Coherency Domain 一部分的所有 CXL Agent 都参与 GPF 流程。CXL.cache Coherency Domain 由一个或多个主机、属于这些主机的所有 CXL Root Port 以及与这些 Root Port 关联的 Virtual Hierarchy 组成。</td></tr>
<tr><td>GPF may be triggered in response to an impending non-graceful shutdown such as a sudden power loss. The host may initiate GPF to ensure that any in-flight data is written back to persistent media prior to a power loss. GPF may also be triggered upon other asynchronous or synchronous events that may or may not involve power loss. The complete list of such events, the mechanisms by which the host is notified, and coordination across CXL Root Ports are beyond the scope of this specification.</td><td style="background-color:#e8e8e8">GPF 可响应即将发生的非正常性关闭 (Non-Graceful Shutdown) 而触发，例如突然断电。主机可发起 GPF 以确保在断电之前将所有 In-Flight 数据写回持久介质。GPF 也可在涉及或不涉及断电的其他异步或同步事件时触发。此类事件的完整列表、主机收到通知的机制以及跨 CXL Root Port 的协调不在本规范范围内。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-8-1"></a>
### 9.8.1 Host and Switch Responsibilities | 主机与交换机职责

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>With the exception of eRCHs, all hosts and all CXL switches shall support GPF as outlined in this section.</td><td style="background-color:#e8e8e8">除 eRCH 外，所有主机和所有 CXL 交换机都应支持本节所述的 GPF。</td></tr>
<tr><td>GPF flow consists of two phases, GPF Phase 1 and GPF Phase 2. During Phase 1, the devices are expected to stop injecting new traffic and write back their caches. During Phase 2, the persistent devices are expected to flush their local write buffers to a persistence domain. This two-phase approach ensures that a device does not receive any new traffic while it is flushing its local memory buffers. The host shall enforce a barrier between the two phases. The host shall ensure that it stops injecting new CXL.cache transactions and that its local caches are written back prior to entering GPF Phase 2.</td><td style="background-color:#e8e8e8">GPF 流程由两个阶段组成：GPF Phase 1 和 GPF Phase 2。在 Phase 1 期间，设备应停止注入新流量并写回其缓存。在 Phase 2 期间，持久设备应将其本地写缓冲区刷新到持久域。这种两阶段方法确保设备在刷新本地内存缓冲区时不会收到任何新流量。主机应在两个阶段之间强制执行一个屏障 (Barrier)。主机应确保在进入 GPF Phase 2 之前停止注入新的 CXL.cache 事务并写回其本地缓存。</td></tr>
<tr><td>In certain configurations, the cache write back step may be skipped during GPF Phase 1. There are various possible reasons for implementing this mode of operation that are beyond the scope of this specification. One possible reason could be that the host does not have the required energy to write back all the caches before the power loss. When operating in this mode, the system designer may use other means, beyond the scope of this specification, to ensure that the data that is meant to be persistent is not lost. The host shall set the Payload[1] flag in the GPF Phase 1 request to indicate that the devices shall write back their caches during Phase 1. The host uses a host-specific mechanism to determine the correct setting of Payload[1].</td><td style="background-color:#e8e8e8">在特定配置下，GPF Phase 1 期间可跳过缓存写回步骤。采用此操作模式存在多种可能原因，不在本规范范围内。一个可能的原因是主机没有足够的能量在断电前写回所有缓存。在此模式下运行时，系统设计者可使用本规范范围之外的其他手段来确保本应持久化的数据不会丢失。主机应设置 GPF Phase 1 请求中的 Payload[1] 标志，以指示设备应在 Phase 1 期间写回其缓存。主机使用主机特定的机制来确定 Payload[1] 的正确设置。</td></tr>
<tr><td>During each phase, the host shall transmit a CXL GPF PM VDM request to each GPF-capable device or Switch that is connected directly to each of its Root Ports and then wait for a response. Table 3-1 describes the format of these messages. The Switch's handling of a GPF PM VDM is described in Section 9.1.2.1. The CXL Root Ports and CXL downstream Switch Ports shall implement timeouts to prevent a single device from blocking GPF forward progress. These timeouts are configured by system software (see Section 8.1.6). A host or a Switch may assume that the GPF timeouts configured across Downstream Ports at the same level in the hierarchy are identical. If a Switch detects a timeout, it shall set the Payload[8] in the response to indicate an error condition. This enables a CXL Root Port to detect GPF Phase 1 errors anywhere in the virtual hierarchy it spawns. If an error is detected by any Root Port in the coherency domain, the host shall set the Payload[8] flag during the Phase 2 flow, thereby informing every CXL device of an error during GPF Phase 1. Persistent devices may log this indication in a device-specific manner and make this information available to system software.</td><td style="background-color:#e8e8e8">在每个阶段，主机应向其每个 Root Port 直接连接的每个支持 GPF 的设备或交换机发送 CXL GPF PM VDM 请求，然后等待响应。表 3-1 描述了这些消息的格式。交换机对 GPF PM VDM 的处理见第 9.1.2.1 节。CXL Root Port 和 CXL Downstream Switch Port 应实现超时机制，以防止单个设备阻塞 GPF 的前向进度。这些超时值由系统软件配置 (见第 8.1.6 节)。主机或交换机可假定层级中同级的 Downstream Port 配置的 GPF 超时值相同。如果交换机检测到超时，应在响应中设置 Payload[8] 以指示错误条件。这使 CXL Root Port 能够检测其生成的 Virtual Hierarchy 中任何位置的 GPF Phase 1 错误。如果 Coherency Domain 内任何 Root Port 检测到错误，主机应在 Phase 2 流程中设置 Payload[8] 标志，从而通知每个 CXL 设备 GPF Phase 1 期间发生了错误。持久设备可通过设备特定的方式记录此指示，并将此信息提供给系统软件。</td></tr>
<tr><td>If the host is positively aware that the GPF event will be followed by a power failure, it should set Payload[0] in the GPF Phase 1 request message. If the host cannot guarantee that the GPF event will be followed by a power failure, it shall not set Payload[0] in the GPF Phase 1 request message.</td><td style="background-color:#e8e8e8">如果主机明确知道 GPF 事件之后将发生断电，则应当 (should) 在 GPF Phase 1 请求消息中设置 Payload[0]。如果主机无法保证 GPF 事件之后将发生断电，则不应在 GPF Phase 1 请求消息中设置 Payload[0]。</td></tr>
<tr><td>The CXL devices and switches must be able to receive and process GPF messages without dependency on any other PM messages. GPF messages do not use a credit, and CREDIT_RTN messages are not expected in response to a GPF request.</td><td style="background-color:#e8e8e8">CXL 设备和交换机必须能够在不依赖任何其他 PM 消息的情况下接收和处理 GPF 消息。GPF 消息不使用 Credit，且不期望有 CREDIT_RTN 消息响应 GPF 请求。</td></tr>
<tr><td>The host may reset the device any time after GPF Phase 2 completes.</td><td style="background-color:#e8e8e8">主机可以在 GPF Phase 2 完成后的任何时间复位设备。</td></tr>
<tr><td>If the host detection or processing of a GPF event and a reset event overlap, the host may process either event and ignore the other event. If the host detection or processing of a GPF event and an Sx event overlap, the host may process either event and ignore the other event. If host detects a GPF event while it is entering a lower power state, the host is required to process the GPF event in a timely manner.</td><td style="background-color:#e8e8e8">如果主机对 GPF 事件和复位事件的检测或处理发生重叠，主机可以处理任一事件并忽略另一个事件。如果主机对 GPF 事件和 Sx 事件的检测或处理发生重叠，主机可以处理任一事件并忽略另一个事件。如果主机在进入低功耗状态时检测到 GPF 事件，则主机需要及时处理 GPF 事件。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-8-2"></a>
### 9.8.2 Device Responsibilities | 设备职责

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>If a device supports GPF, it shall set bit 1 of the CAPABILITY_VECTOR field in its AGENT_INFO response (see Table 3-1). All CXL devices with the exception of eRCDs shall support GPF. An eRCD may support GPF functionality. If a device supports GPF, the Device shall respond to all GPF request messages regardless of whether the Device is required to take any action. The host may interpret a lack of response within a software-configured timeout window as an error. For example, a Type 3 device may or may not take any specific action during GPF Phase 1 other than generating a GPF Phase 1 response message.</td><td style="background-color:#e8e8e8">如果设备支持 GPF，应在其 AGENT_INFO 响应中设置 CAPABILITY_VECTOR 字段的 bit 1 (见表 3-1)。除 eRCD 外的所有 CXL 设备都应支持 GPF。eRCD 可支持 GPF 功能。如果设备支持 GPF，无论设备是否需要采取任何操作，都必须响应所有 GPF 请求消息。主机可将软件配置的超时窗口内缺少响应的情况解释为错误。例如，Type 3 设备在 GPF Phase 1 期间可能除生成 GPF Phase 1 响应消息外采取或不采取任何特定操作。</td></tr>
<tr><td>Upon receiving a GPF Phase 1 request message, a CXL device shall execute the following steps in the specified order:<br>1. Stop injecting new CXL.cache transactions except for cache write backs described in step 3.<br>2. If CXL.cache capable and Payload[1]=1, disable caching. This will ensure that the device no longer caches any coherent memory and thereby not cache any writes that are received over the CXL interface in its CXL.cache.<br>3. If CXL.cache capable and Payload[1]=1, write back all modified lines in the device cache. The memory destination may be local or remote.<br>— To minimize GPF latency, the device should ignore lines that are not dirty.<br>— To minimize GPF latency, the device should not write back lines that it knows are mapped to volatile memory. The mechanism by which the device obtains this knowledge is beyond the scope of this specification.<br>— The device must use device internal mechanisms to write back all dirty lines that are mapped to its local persistent HDM.<br>— The device must write back all dirty lines that are not mapped to its local HDM and may be of persistent type. Each such dirty line must be written back to the destination HDM in two steps:<br>&nbsp;&nbsp;i. Issue DirtyEvict request to the host (see Section 3.2.4.2.15).<br>&nbsp;&nbsp;ii. Issue CLFlush request to the host (see Section 3.2.4.2.13).<br>4. Indicate that the device is ready to move to GPF Phase 2 by sending a GPF Phase 1 response message. Set the Payload[8] flag in the response if the Phase 1 processing was unsuccessful.</td><td style="background-color:#e8e8e8">收到 GPF Phase 1 请求消息后，CXL 设备应按指定顺序执行以下步骤：<br>1. 停止注入新的 CXL.cache 事务，但步骤 3 中描述的 Cache Write Back 除外。<br>2. 若支持 CXL.cache 且 Payload[1]=1，禁用缓存。这将确保设备不再缓存任何 Coherent Memory，从而不在其 CXL.cache 中缓存通过 CXL 接口接收的任何写操作。<br>3. 若支持 CXL.cache 且 Payload[1]=1，写回设备缓存中的所有 Modified Line。内存目标可以是本地或远程的。<br>— 为最小化 GPF 延迟，设备应当忽略非 Dirty 的 Line。<br>— 为最小化 GPF 延迟，设备不应当写回已知映射到 Volatile Memory 的 Line。设备获取此知识的机制不在本规范范围内。<br>— 设备必须使用设备内部机制写回所有映射到其本地 Persistent HDM 的 Dirty Line。<br>— 设备必须写回所有未映射到其本地 HDM 且可能为 Persistent 类型的 Dirty Line。每条此类 Dirty Line 必须通过两个步骤写回到目标 HDM：<br>&nbsp;&nbsp;i. 向主机发出 DirtyEvict 请求 (见第 3.2.4.2.15 节)。<br>&nbsp;&nbsp;ii. 向主机发出 CLFlush 请求 (见第 3.2.4.2.13 节)。<br>4. 通过发送 GPF Phase 1 响应消息，指示设备已准备好进入 GPF Phase 2。如果 Phase 1 处理未成功，在响应中设置 Payload[8] 标志。</td></tr>
<tr><td>A device may take additional steps to reduce power draw from the system if the Payload[0] flag is set in the request message indicating that power failure is imminent. For example, a device may choose to not wait for responses to the previously issued reads before initiating the write back operation [step 3] above as long as the read responses do not impact persistent memory content.</td><td style="background-color:#e8e8e8">如果请求消息中设置了 Payload[0] 标志，表明即将发生断电，设备可采取额外步骤以减少系统的功耗。例如，设备可选择不等待先前发出的读操作响应即启动上述写回操作[步骤 3]，只要读响应不影响 Persistent Memory 内容即可。</td></tr>
<tr><td>Until the GPF Phase 2 request message is received, the device must respond to and complete any accesses that it receives over the CXL interface. This is to ensure that the other requesters can continue to make forward progress through the GPF flow.</td><td style="background-color:#e8e8e8">在收到 GPF Phase 2 请求消息之前，设备必须响应并完成通过 CXL 接口收到的任何访问。这是为了确保其他请求方能够继续通过 GPF 流程取得前向进度。</td></tr>
<tr><td>Upon receiving a GPF Phase 2 request, a CXL device shall execute the following steps in the specified order:<br>1. If it is a persistent memory device and the Payload[8] flag is set, increment the Dirty Shutdown Count (see Section 8.2.10.9.3.1).<br>2. Flush internal memory buffers to local memory if applicable.<br>3. Acknowledge the request by sending a GPF Phase 2 response message.<br>4. Enter the lowest possible power state.</td><td style="background-color:#e8e8e8">收到 GPF Phase 2 请求后，CXL 设备应按指定顺序执行以下步骤：<br>1. 如果它是 Persistent Memory 设备且 Payload[8] 标志已置位，递增 Dirty Shutdown Count (见第 8.2.10.9.3.1 节)。<br>2. 如适用，将内部内存缓冲区刷新到本地内存。<br>3. 通过发送 GPF Phase 2 响应消息来确认请求。<br>4. 进入可能的最低功耗状态。</td></tr>
<tr><td>As this exchange may be performed in the event of an impending power loss, it is important that any flushing activity in either phase is performed in an expedient manner, and that the acknowledgment of each phase is sent as quickly as possible.</td><td style="background-color:#e8e8e8">由于此交换可能在即将发生断电的情况下执行，因此两个阶段中的任何刷新活动都应以快速方式执行，并且每个阶段的确认应尽快发送。</td></tr>
<tr><td>A device may have access to an alternate power source (e.g., a device with a large memory buffer may include a charged capacitor or battery) and may acknowledge GPF Phase 2 requests as soon as it has switched over to the alternate power source. Such a device shall ensure that PERST# assertion does not interfere with the local flush flow and shall correctly handle a subsequent power-up sequence even if the local flush is in progress.</td><td style="background-color:#e8e8e8">设备可接入备用电源 (例如，具有大容量内存缓冲区的设备可能包含已充电的电容器或电池)，并可在切换到备用电源后立即确认 GPF Phase 2 请求。此类设备应确保 PERST# 置位不干扰本地刷新流程，并且即使本地刷新正在进行中，也应正确处理后续的上电序列。</td></tr>
<tr><td>A device is not considered to be fully operational after it receives a GPF Phase 1 Request. In this state, a device shall correctly process a Conventional Reset request, and return to operational state upon successful completion of these resets.</td><td style="background-color:#e8e8e8">设备在收到 GPF Phase 1 请求后不视为完全可操作。在此状态下，设备应正确处理 Conventional Reset 请求，并在这些复位成功完成后返回到可操作状态。</td></tr>
<tr><td>If the device detection or processing of a GPF event and a reset event overlap, the device may process either event and ignore the other event. If the device detection or processing of a GPF event and an Sx event overlap, the device may process either event and ignore the other event. If a device receives a GPF request while it is entering a lower power state, it shall process the GPF request in a timely manner.</td><td style="background-color:#e8e8e8">如果设备对 GPF 事件和复位事件的检测或处理发生重叠，设备可以处理任一事件并忽略另一个事件。如果设备对 GPF 事件和 Sx 事件的检测或处理发生重叠，设备可以处理任一事件并忽略另一个事件。如果设备在进入低功耗状态时收到 GPF 请求，应及时处理 GPF 请求。</td></tr>
<tr><td>A pooled device is composed of multiple LDs that are assigned to different Virtual Hierarchies. Because a GPF event may or may not be coordinated across these hierarchies, each LD shall be capable of independently processing GPF messages targeting that individual LD, without affecting any other LD within the MLD. An MLD cannot enter a lower power state until all LDs associated with the device have indicated that they are ready to enter the lower power state. In addition, the MLD must be able to process multiple GPF events (from different VCS targeting unique LDs).</td><td style="background-color:#e8e8e8">池化设备 (Pooled Device) 由分配给不同 Virtual Hierarchy 的多个 LD 组成。由于 GPF 事件可能在这些 Hierarchy 之间协调，也可能不协调，因此每个 LD 应能够独立处理针对该个别 LD 的 GPF 消息，而不影响 MLD 内的任何其他 LD。MLD 不能进入低功耗状态，直到与设备关联的所有 LD 都已指示它们准备好进入低功耗状态。此外，MLD 必须能够处理多个 GPF 事件 (来自不同的 VCS，针对不同的 LD)。</td></tr>
<tr><td>If a device receives a GPF Phase 2 request message without a prior GPF Phase 1 request message, it shall respond to that GPF Phase 2 request message.</td><td style="background-color:#e8e8e8">如果设备在未收到 GPF Phase 1 请求消息的情况下收到 GPF Phase 2 请求消息，应响应该 GPF Phase 2 请求消息。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-8-3"></a>
### 9.8.3 Energy Budgeting | 能源预算

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>It is often necessary to assess whether a system has sufficient energy to handle GPF during a power failure scenario. System software may use the information available in various CXL DVSEC registers along with its knowledge of the remainder of the system to make this determination.</td><td style="background-color:#e8e8e8">通常有必要评估系统在断电情况下是否有足够能量处理 GPF。系统软件可使用各种 CXL DVSEC 寄存器中的信息，结合对系统其余部分的了解来做出此判断。</td></tr>
<tr><td>This information may also be used to calculate appropriate GPF timeout values at various points in the CXL hierarchy. See the implementation note below. The timeout values are configured through GPF DVSEC for CXL Ports (see Section 8.1.6).</td><td style="background-color:#e8e8e8">此信息也可用于计算 CXL Hierarchy 中各个点的适当 GPF 超时值。见下方的实现说明。超时值通过 CXL Port 的 GPF DVSEC 配置 (见第 8.1.6 节)。</td></tr>
</tbody>
</table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> <table>
> <thead>
> <tr>
> <th width="50%">🇬🇧 English</th>
> <th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
> </tr>
> </thead>
> <tbody>
> <tr><td>System software may determine the total energy needs during power failure GPF. There may always be a nonzero possibility that power failure GPF may not successfully complete (e.g., under unusual thermal conditions or fatal errors). The goal of the system designer is to ensure that the probability of failure is sufficiently low and meets the system design objectives.</td><td style="background-color:#e8e8e8">系统软件可确定断电 GPF 期间的总能量需求。始终存在非零可能性使得断电 GPF 无法成功完成 (例如，在异常热条件或致命错误下)。系统设计者的目标是确保故障概率足够低，满足系统设计目标。</td></tr>
> <tr><td>The following high-level algorithm may be followed for calculating timeouts and energy requirements:<br>1. Iterate through every CXL device and calculate T1 and T2 as defined in Column "Time needed" in Table 9-3.<br>2. Calculate T1MAX and T2MAX.<br>&nbsp;&nbsp;a. T1MAX = MAX of T1 values calculated for all devices plus propagation delay, host-side processing delays, and any other host/system-specific delays.<br>&nbsp;&nbsp;b. T2MAX = MAX of T2 values calculated for all devices in the hierarchy plus propagation delay, host-side processing delays, and any other host/system-specific delays. This could be same as GPF Phase 2 timeout at RC.<br>3. Calculate E1 and E2 for each device. See Column "Energy needed" in Table 9-3.<br>4. Do summation over all CXL devices (E1+E2). Add energy needs for host and non-CXL devices during this window.</td><td style="background-color:#e8e8e8">计算超时和能量需求可遵循以下高级算法：<br>1. 遍历每个 CXL 设备，按表 9-3 中"所需时间"列的定义计算 T1 和 T2。<br>2. 计算 T1MAX 和 T2MAX。<br>&nbsp;&nbsp;a. T1MAX = 所有设备 T1 值中的最大值 + 传播延迟 + 主机侧处理延迟 + 任何其他主机/系统特定延迟。<br>&nbsp;&nbsp;b. T2MAX = Hierarchy 中所有设备 T2 值中的最大值 + 传播延迟 + 主机侧处理延迟 + 任何其他主机/系统特定延迟。这可以与 RC 处的 GPF Phase 2 超时相同。<br>3. 为每个设备计算 E1 和 E2。见表 9-3 中"所需能量"列。<br>4. 对所有 CXL 设备的 E1+E2 求和。加上主机和非 CXL 设备在此窗口期间的能量需求。</td></tr>
> <tr><td>The GPF timeout registers in the root port and the Downstream Switch Port CXL Port GPF Capability structure may be programmed to T1MAX and T2MAX, respectively. Device active power is the amount of power that the device consumes in D0 state and may be reported by the device via Power Budgeting Extended Capability as defined in PCIe Base Specification. Cache size is reported via PCIe DVSEC for CXL devices (Revision 1). This computation may have to be redone periodically as some of these factors may change. When a CXL device is hot-added/removed, it may warrant recomputation. Refer to Table 9-3.</td><td style="background-color:#e8e8e8">Root Port 和 Downstream Switch Port 的 CXL Port GPF Capability 结构中的 GPF 超时寄存器可分别编程为 T1MAX 和 T2MAX。设备活动功耗 (Device Active Power) 是设备在 D0 状态下消耗的功率量，可由设备通过 PCIe 基本规范中定义的 Power Budgeting Extended Capability 报告。缓存大小通过 PCIe DVSEC for CXL Devices (Revision 1) 报告。由于某些因素可能发生变化，此计算可能需要定期重做。当 CXL 设备被 Hot-Add/热移除时，可能需要重新计算。参见表 9-3。</td></tr>
> <tr><td>Cache size, T2, and GPF Phase 2 Power parameters are reported by the device via GPF DVSEC for CXL devices (see Section 8.1.7). The other parameters are system dependent. System software may use ACPI HMAT to determine average persistent memory bandwidth, but the software could apply additional optimizations if it is aware of the specific persistent device the accelerator is operating on. In some cases, System Firmware may be the one performing this computation. Since System Firmware may or may not be aware of workloads, it may make conservative assumptions.</td><td style="background-color:#e8e8e8">Cache Size、T2 和 GPF Phase 2 Power 参数由设备通过 GPF DVSEC for CXL Devices 报告 (见第 8.1.7 节)。其他参数取决于系统。系统软件可使用 ACPI HMAT 确定平均 Persistent Memory 带宽，但如果软件知道加速器正在操作的特定 Persistent 设备，则可以应用额外优化。在某些情况下，执行此计算的可能是系统固件 (System Firmware)。由于系统固件可能了解或不了解工作负载，它可能做出保守假设。</td></tr>
> <tr><td>If the system determines that it does not have sufficient energy to handle all CXL devices, it may be able to take certain steps, such as to reconfigure certain devices to stay within the system budget by reducing the size of cache allocated to persistent memory or limit persistent memory usages. Several system level and device-level optimizations are possible:<br>• Certain accelerators may always operate on volatile memory and could skip the flush. For these accelerators, T1 would be 0.<br>• Device could partition cache among volatile vs. non-volatile memory and thus lower T1. Such partitioning may be accomplished with assistance from system software.<br>• A device could force certain blocks (e.g., execution engines) into a lower power state upon receiving a GPF Phase 1 request.<br>• Device may include a local power source and therefore could lower its T1 and T2.<br>• System software may configure all devices so that all T1s and T2s are roughly equal. This may require performance and/or usage model trade-offs.</td><td style="background-color:#e8e8e8">如果系统确定没有足够能量处理所有 CXL 设备，可能能够采取某些步骤，例如通过减少分配给 Persistent Memory 的缓存大小来重新配置某些设备以保持在系统预算范围内，或限制 Persistent Memory 使用。多种系统级和设备级优化是可能的：<br>• 某些加速器可能始终在 Volatile Memory 上操作，可以跳过刷新。对于这些加速器，T1 将为 0。<br>• 设备可将缓存在 Volatile 与非 Volatile Memory 之间分区，从而降低 T1。这种分区可在系统软件的协助下完成。<br>• 设备可在收到 GPF Phase 1 请求时将某些块 (如执行引擎) 强制进入低功耗状态。<br>• 设备可能包含本地电源，因此可以降低其 T1 和 T2。<br>• 系统软件可配置所有设备使所有 T1 和 T2 大致相等。这可能需要性能和/或使用模型的权衡。</td></tr>
> </tbody>
> </table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-9"></a>
## 9.9 Hot-Plug | 热插拔

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>By definition, RCDs and RCHs do not support Hot-Plug.</td><td style="background-color:#e8e8e8">根据定义，RCD 和 RCH 不支持热插拔 (Hot-Plug)。</td></tr>
<tr><td>CXL Root Ports and CXL Downstream Switch Ports may support Hot-Add and managed Hot-Remove. All CXL Ports shall be designed to avoid electrical damage upon surprise Hot-Remove. All CXL switches and CXL devices, with the exception of eRCDs, shall be capable of being Hot-Plugged, subject to the Form Factor limitations. In a managed Hot-Remove flow, software is notified of a hot removal request. This provides CXL-aware system software the opportunity to write back device cachelines and to offline device memory prior to removing power. During a Hot-Add flow, CXL-aware system software discovers the CXL.cache and CXL.mem capabilities of the adapter and initializes them so they are ready to be used.</td><td style="background-color:#e8e8e8">CXL Root Port 和 CXL Downstream Switch Port 可支持 Hot-Add 和受管理的 Hot-Remove (Managed Hot-Remove)。所有 CXL Port 的设计应避免在意外 Hot-Remove (Surprise Hot-Remove) 时发生电气损坏。除 eRCD 外，所有 CXL 交换机和 CXL 设备都应在受 Form Factor 限制的前提下具备 Hot-Plug 能力。在 Managed Hot-Remove 流程中，软件会收到热移除请求的通知。这为 CXL-aware 系统软件提供了在移除电源之前写回设备 Cacheline 并将设备内存 Offline 的机会。在 Hot-Add 流程中，CXL-aware 系统软件发现适配器的 CXL.cache 和 CXL.mem 能力，并对其进行初始化使之就绪可用。</td></tr>
<tr><td>CXL leverages PCIe Hot-Plug model and Hot-Plug elements as defined in PCIe Base Specification and the applicable form-factor specifications.</td><td style="background-color:#e8e8e8">CXL 利用 PCIe 基本规范和适用 Form Factor 规范中定义的 PCIe Hot-Plug 模型和 Hot-Plug 元素。</td></tr>
<tr><td>CXL isolation is the mechanism that is used for graceful handling of Surprise Hot-Remove of CXL adapters. If a CXL adapter that holds modified lines in its cache is removed without any prior notification and CXL.cache isolation is not enabled, subsequent accesses to those addresses may result in timeouts that may be fatal to host operation. If a CXL adapter with HDM is removed without any prior notification and CXL.mem isolation is not enabled, subsequent accesses to HDM locations may result in timeouts that may be fatal to host operation.</td><td style="background-color:#e8e8e8">CXL Isolation 是用于优雅处理 CXL 适配器意外 Hot-Remove 的机制。如果在其缓存中持有 Modified Line 的 CXL 适配器在没有任何预先通知的情况下被移除，且 CXL.cache Isolation 未启用，则对这些地址的后续访问可能导致超时，可能对主机操作造成致命影响。如果具有 HDM 的 CXL 适配器在没有任何预先通知的情况下被移除，且 CXL.mem Isolation 未启用，则对 HDM 位置的后续访问可能导致超时，可能对主机操作造成致命影响。</td></tr>
<tr><td>All CXL Downstream Ports, including RCH Downstream Ports, shall hardwire the Hot-Plug Surprise bit in the Slot Capabilities register to 0. Software may leverage Downstream Port Containment capability of the Downstream Port to gracefully handle surprise hot removal of PCIe adapters or contain errors that result from surprise hot removal or Link Down of CXL adapters.</td><td style="background-color:#e8e8e8">所有 CXL Downstream Port (包括 RCH Downstream Port) 都应将 Slot Capabilities 寄存器中的 Hot-Plug Surprise 位硬连线为 0。软件可利用 Downstream Port 的 Downstream Port Containment 能力来优雅处理 PCIe 适配器的意外 Hot-Remove，或遏制因 CXL 适配器意外 Hot-Remove 或 Link Down 导致的错误。</td></tr>
<tr><td>Support for Coherent Device Attribute Table (CDAT) by way of ReadTable DOE (see Section 8.1.11) is optional for eRCDs, but mandatory for all other CXL devices and is also mandatory for CXL switches. Software may use this interface to learn about performance and other attributes of the device or the Switch.</td><td style="background-color:#e8e8e8">eRCD 可选择支持通过 ReadTable DOE (见第 8.1.11 节) 访问 Coherent Device Attribute Table (CDAT)，但所有其他 CXL 设备必须支持，CXL 交换机也必须支持。软件可使用此接口了解设备或交换机的性能及其他属性。</td></tr>
<tr><td>The Host Bridge and Upstream Switch Ports implement the HDM Decoder Capability structure. Software may program these to account for the HDM capacity with an appropriate interleaving scheme (see Section 9.13.1). Software may choose to leave the decoders unlocked for maximum flexibility and use other protections (e.g., page tables) to limit access to the registers. All unused decoders are unlocked by definition and software may claim these to decode additional HDM capacity during a Hot-Add flow.</td><td style="background-color:#e8e8e8">Host Bridge 和 Upstream Switch Port 实现 HDM Decoder Capability 结构。软件可编程这些结构以使用适当的交织方案 (见第 9.13.1 节) 来容纳 HDM 容量。软件可选择保持 Decoder 未锁定以获得最大灵活性，并使用其他保护措施 (如 Page Table) 来限制对寄存器的访问。所有未使用的 Decoder 根据定义是未锁定的，软件可在 Hot-Add 流程中声明这些 Decoder 以解码额外的 HDM 容量。</td></tr>
<tr><td>All CXL.cache-capable devices, with the exception of eRCDs, shall implement the Cache Writeback and Invalidation capability (see Section 9.6). Software may use this capability to ensure that a CXL.cache-capable device does not have any modified cachelines prior to removing power.</td><td style="background-color:#e8e8e8">所有支持 CXL.cache 的设备，除 eRCD 外，都应实现 Cache Writeback and Invalidation 能力 (见第 9.6 节)。软件可使用此能力确保支持 CXL.cache 的设备在移除电源之前没有任何 Modified Cacheline。</td></tr>
<tr><td>Software shall ensure that the device has completed Power Management Initialization (see Section 8.1.3.5) prior to enabling its CXL.cache capabilities or CXL.mem capabilities if the device reports PM Init Completion Reporting Capable=1.</td><td style="background-color:#e8e8e8">如果设备报告 PM Init Completion Reporting Capable=1，软件应确保设备在启用其 CXL.cache 能力或 CXL.mem 能力之前已完成 Power Management Initialization (见第 8.1.3.5 节)。</td></tr>
<tr><td>Software shall ensure that it does not enable a CXL.cache device below a given Root Port if the Root Port does not support CXL.cache. The Root Port's capabilities are exposed via the DVSEC Flex Bus Port Capability register. All CXL.cache-capable devices should expose the size of their cache via the DVSEC CXL Capability2 register. Software may cross-check this against the host's effective snoop filter capabilities (see Section 8.2.4.23.2) during Hot-Add of CXL.cache-capable device. Software may configure the Cache_SF_Coverage field in the DVSEC CXL Control register to indicate to the device how much snoop filter capacity it should use (0 being a legal value). In extreme scenarios, software may disable CXL.cache devices to avoid snoop filter over-subscription.</td><td style="background-color:#e8e8e8">软件应确保如果给定 Root Port 不支持 CXL.cache，则不在该 Root Port 下启用任何 CXL.cache 设备。Root Port 的能力通过 DVSEC Flex Bus Port Capability 寄存器暴露。所有支持 CXL.cache 的设备应通过 DVSEC CXL Capability2 寄存器暴露其缓存大小。在 Hot-Add 支持 CXL.cache 的设备时，软件可将其与主机的有效 Snoop Filter 能力 (见第 8.2.4.23.2 节) 进行交叉校验。软件可配置 DVSEC CXL Control 寄存器中的 Cache_SF_Coverage 字段，向设备指示其应使用多少 Snoop Filter 容量 (0 是一个合法值)。在极端情况下，软件可禁用 CXL.cache 设备以避免 Snoop Filter 超额订阅。</td></tr>
<tr><td>During Hot-Add, System Software may reassess the GPF energy budget and take corrective action if necessary.</td><td style="background-color:#e8e8e8">在 Hot-Add 过程中，系统软件可重新评估 GPF 能源预算，并在必要时采取纠正措施。</td></tr>
<tr><td>Hot-Add of an eRCD may result in unpredictable behavior if the device is exposed to software. The following mechanisms are defined to ensure that an eRCD that is hot-added in runtime is not discoverable by standard PCIe software:<br>• For Root Ports connected to Hot-Plug capable slots, it is recommended that System Firmware set the Disable_RCD_Training bit (see Section 8.2.1.3.2) after System Firmware PCIe enumeration completion, but before OS hand-off. This will ensure that a CXL root port will fail link training if an eRCD is hot-added. A Hot-Plug event may be generated in these cases, and the Hot-Plug handler may be invoked. The Hot-Plug handler may treat this condition as a failed Hot-Plug, notify the user, and then power down the slot.<br>• A Downstream Switch Port may itself be hot-added and cannot rely on System Firmware setting the Disable_RCD_Training bit. A Switch shall not report a Link Up condition and shall not report presence of an adapter when it is connected to an eRCD. System Firmware or CXL-aware software may still consult DVSEC Flex Bus Port Status (see Section 8.2.1.3.3) and discover that the Port is connected to an eRCD.</td><td style="background-color:#e8e8e8">如果 eRCD 暴露给软件，在运行时 Hot-Add eRCD 可能导致不可预测的行为。定义了以下机制以确保在运行时 Hot-Add 的 eRCD 不会被标准 PCIe 软件发现：<br>• 对于连接到支持 Hot-Plug 的插槽 (Slot) 的 Root Port，建议系统固件在系统固件 PCIe 枚举完成后、OS 交接前设置 Disable_RCD_Training 位 (见第 8.2.1.3.2 节)。这将确保如果 Hot-Add 了 eRCD，CXL Root Port 的 Link Training 将失败。在这些情况下可能生成 Hot-Plug 事件，并可能调用 Hot-Plug Handler。Hot-Plug Handler 可将此条件视为失败的 Hot-Plug，通知用户，然后关闭插槽电源。<br>• Downstream Switch Port 本身可能被 Hot-Add，不能依赖系统固件设置 Disable_RCD_Training 位。当交换机连接到 eRCD 时，不应报告 Link Up 条件，也不应报告适配器存在。系统固件或 CXL-aware 软件仍可查阅 DVSEC Flex Bus Port Status (见第 8.2.1.3.3 节) 并发现该 Port 连接到 eRCD。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

> **IMPLEMENTATION NOTE: CXL Type 3 Device Hot-Add Flow | CXL Type 3 设备 Hot-Add 流程**
>
> <table>
> <thead>
> <tr>
> <th width="50%">🇬🇧 English</th>
> <th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
> </tr>
> </thead>
> <tbody>
> <tr><td>1. System Firmware may prepare the system for a future Hot-Add (e.g., pad resources to accommodate the needs of an adapter to be hot-added).<br>2. User hot-adds a CXL memory expander in an empty slot. Downstream Ports bring up the link in CXL VH mode.<br>3. PCIe Hot-Plug interrupt is generated.<br>4. Bus driver performs the standard PCIe Hot-Add operations, thus enabling CXL.io. This process assigns BARs to the device.<br>5. CXL-aware software (e.g., CXL bus driver in OS, the device driver, or other software entity) probes CXL DVSEC capabilities on the device and ensures that the HDM is active. Memory may be initialized either by hardware, by the FW on the adapter or the device driver.<br>6. CXL-aware software configures the CXL DVSEC structures on the device, switches, and Host Bridge (e.g., GPF DVSEC, HDM decoders).<br>7. CXL-aware software notifies the OS memory manager about the new memory and its attributes such as latency and bandwidth. Memory manager processes a request and adds the new memory to its allocation pool.<br>8. The user may be notified via attention indicator or some other user interface of successful completion.</td><td style="background-color:#e8e8e8">1. 系统固件可为未来的 Hot-Add 准备系统 (例如，填充资源以适应待 Hot-Add 的适配器需求)。<br>2. 用户将 CXL 内存扩展器 Hot-Add 到空插槽中。Downstream Port 在 CXL VH 模式下建立链路。<br>3. 生成 PCIe Hot-Plug 中断。<br>4. 总线驱动程序执行标准 PCIe Hot-Add 操作，从而启用 CXL.io。此过程为设备分配 BAR。<br>5. CXL-aware 软件 (如 OS 中的 CXL 总线驱动程序、设备驱动程序或其他软件实体) 探测设备上的 CXL DVSEC 能力并确保 HDM 处于 Active 状态。内存可由硬件、适配器上的固件或设备驱动程序初始化。<br>6. CXL-aware 软件配置设备、交换机和 Host Bridge 上的 CXL DVSEC 结构 (如 GPF DVSEC、HDM Decoder)。<br>7. CXL-aware 软件通知 OS 内存管理器新内存及其属性 (如延迟和带宽)。内存管理器处理请求并将新内存添加到其分配池中。<br>8. 可通过注意指示灯或其他用户界面向用户通知成功完成。</td></tr>
> </tbody>
> </table>

> **IMPLEMENTATION NOTE: CXL Type 3 Device-Managed Hot-Remove Flow | CXL Type 3 设备受管理 Hot-Remove 流程**
>
> <table>
> <thead>
> <tr>
> <th width="50%">🇬🇧 English</th>
> <th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
> </tr>
> </thead>
> <tbody>
> <tr><td>1. User initiates a Hot-Remove request via attention button or some other user interface.<br>2. The standard PCIe Hot-Remove flow is triggered (e.g., via Hot-Plug interrupt if attention button was used).<br>3. CXL-aware software (e.g., CXL bus driver in OS, the device driver, or other software entity) probes CXL DVSEC capabilities on the device and determines active memory ranges.<br>4. CXL-aware software requests the OS memory manager to vacate these ranges.<br>5. If the Memory Manager is unable to fulfill this request (e.g., because of presence of pinned pages), CXL-aware software will return an error to the Hot-Remove handler, which will notify the user that the operation has failed.<br>6. If the Memory Manager is able to fulfill this request, CXL-aware system software reconfigures HDM Decoders in CXL switches and Root Ports. This is followed by the standard PCIe Hot-Remove flow that will process CXL.io resource deallocation.<br>7. If the PCIe Hot-Remove flow fails, the user is notified that the Hot-Remove operation has failed; otherwise, the user is notified that the Hot-Remove flow has successfully completed.</td><td style="background-color:#e8e8e8">1. 用户通过注意按钮或其他用户界面发起 Hot-Remove 请求。<br>2. 触发标准 PCIe Hot-Remove 流程 (例如，如果使用了注意按钮，则通过 Hot-Plug 中断)。<br>3. CXL-aware 软件 (如 OS 中的 CXL 总线驱动程序、设备驱动程序或其他软件实体) 探测设备上的 CXL DVSEC 能力并确定 Active 内存范围。<br>4. CXL-aware 软件请求 OS 内存管理器腾出这些范围。<br>5. 如果内存管理器无法满足此请求 (例如，因为存在 Pinned Page)，CXL-aware 软件将向 Hot-Remove Handler 返回错误，通知用户操作失败。<br>6. 如果内存管理器能够满足此请求，CXL-aware 系统软件重新配置 CXL 交换机和 Root Port 中的 HDM Decoder。然后执行标准 PCIe Hot-Remove 流程，处理 CXL.io 资源释放。<br>7. 如果 PCIe Hot-Remove 流程失败，通知用户 Hot-Remove 操作失败；否则，通知用户 Hot-Remove 流程成功完成。</td></tr>
> </tbody>
> </table>

> **IMPLEMENTATION NOTE: CXL Type 1 Device Hot-Add Flow | CXL Type 1 设备 Hot-Add 流程**
>
> <table>
> <thead>
> <tr>
> <th width="50%">🇬🇧 English</th>
> <th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
> </tr>
> </thead>
> <tbody>
> <tr><td>1. System Firmware may prepare the system for a future Hot-Add (e.g., pad MMIO resources to accommodate the needs of an adapter to be hot-added).<br>2. The user Hot-Adds a CXL Type 1 device in an empty slot. The Downstream Port brings up the link in CXL VH operation with 68B Flit mode.<br>3. A PCIe Hot-Plug interrupt is generated.<br>4. The bus driver performs the standard PCIe Hot-Add operations, thus enabling CXL.io. This process assigns BARs to the device.<br>5. CXL-aware software (e.g., CXL bus driver in OS, the device driver, or other software entity) probes CXL DVSEC capabilities on the device. If the device is hot-added below a Root Port that cannot accommodate a CXL.cache-enabled device, Hot-Add is rejected. If the device has a cache that is larger than what the host snoop filter can handle, Hot-Add is rejected. The user may be notified via attention indicator or some other user interface of this.<br>6. If the above checks pass, CXL-aware software configures the CXL DVSEC structures on the device and switches (e.g., GPF DVSEC).<br>7. The Hot-Add flow is complete. The user may be notified via attention indicator or some other user interface of successful completion.</td><td style="background-color:#e8e8e8">1. 系统固件可为未来的 Hot-Add 准备系统 (例如，填充 MMIO 资源以适应待 Hot-Add 的适配器需求)。<br>2. 用户将 CXL Type 1 设备 Hot-Add 到空插槽中。Downstream Port 在 CXL VH 操作下以 68B Flit Mode 建立链路。<br>3. 生成 PCIe Hot-Plug 中断。<br>4. 总线驱动程序执行标准 PCIe Hot-Add 操作，从而启用 CXL.io。此过程为设备分配 BAR。<br>5. CXL-aware 软件 (如 OS 中的 CXL 总线驱动程序、设备驱动程序或其他软件实体) 探测设备上的 CXL DVSEC 能力。如果设备被 Hot-Add 到不能容纳支持 CXL.cache 的设备的 Root Port 下，则拒绝 Hot-Add。如果设备的缓存大于主机 Snoop Filter 可以处理的容量，则拒绝 Hot-Add。可通过注意指示灯或其他用户界面向用户通知。<br>6. 如果上述检查通过，CXL-aware 软件配置设备和交换机上的 CXL DVSEC 结构 (如 GPF DVSEC)。<br>7. Hot-Add 流程完成。可通过注意指示灯或其他用户界面向用户通知成功完成。</td></tr>
> </tbody>
> </table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-10"></a>
## 9.10 Software Enumeration | 软件枚举

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section describes two types of CXL device enumeration flows. Although discovery of CXL devices follows the PCIe model, there are some important differences:<br>• RCD Enumeration: As the name suggests, RCD mode (see Section 9.11.1) imposes some restrictions and leads to a much-simpler enumeration flow. Each RCD is exposed to host software as one or more PCIe Root Complex Integrated Endpoints as indicated by setting PCI Express Capabilities Register.Device/Port Type=RCiEP. Each RCD creates a new PCIe enumeration hierarchy that is compatible with an ACPI-defined PCIe Host Bridge (PNP ID PNP0A08). The RCD enumeration flow is described in Section 9.11.<br>• CXL VH enumeration: A CXL root port is the root of a CXL VH. A CXL VH may include zero or more CXL switches, zero or more PCIe switches, zero or more PCIe devices, and one or more CXL devices that are not in RCD mode. A CXL VH represents a software view and may differ from the physical topology. The CXL VH enumeration flow is described in Section 9.12.</td><td style="background-color:#e8e8e8">本节描述了两种类型的 CXL 设备枚举流程。虽然 CXL 设备的发现遵循 PCIe 模型，但存在一些重要差异：<br>• RCD 枚举：顾名思义，RCD 模式 (见第 9.11.1 节) 施加了一些限制，并导致了一个简化得多的枚举流程。每个 RCD 通过设置 PCI Express Capabilities Register.Device/Port Type=RCiEP，向主机软件暴露为一个或多个 PCIe Root Complex Integrated Endpoint。每个 RCD 创建一个与 ACPI 定义的 PCIe Host Bridge (PNP ID PNP0A08) 兼容的新 PCIe 枚举 Hierarchy。RCD 枚举流程见第 9.11 节。<br>• CXL VH 枚举：CXL Root Port 是 CXL VH 的根。CXL VH 可包括零个或多个 CXL 交换机、零个或多个 PCIe 交换机、零个或多个 PCIe 设备，以及一个或多个非 RCD 模式的 CXL 设备。CXL VH 表示一个软件视图，可能与物理拓扑不同。CXL VH 枚举流程见第 9.12 节。</td></tr>
<tr><td>A CXL device cannot claim I/O resources because it is not a Legacy Endpoint. For the definition of Legacy Endpoint, see PCIe Base Specification.</td><td style="background-color:#e8e8e8">CXL 设备不能声明 I/O 资源，因为它不是 Legacy Endpoint。关于 Legacy Endpoint 的定义，请参见 PCIe 基本规范。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11"></a>
## 9.11 RCD Enumeration | RCD 枚举

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td><strong>9.11 RCD Enumeration</strong></td><td style="background-color:#e8e8e8"><strong>9.11 RCD 枚举</strong></td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-1"></a>
### 9.11.1 RCD Mode | RCD 模式

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Restricted CXL device (RCD) mode is a CXL operating mode with the following restrictions:<br>• Hot-Plug is not supported<br>• CXL devices operating in this mode always set the Device/Port Type field in the PCI Express Capabilities register to RCiEP<br>• Flit modes other than 68B Flit mode are not supported<br>• Routing types other than HBR are not supported<br>• Link is not visible to non-CXL-aware software</td><td style="background-color:#e8e8e8">受限 CXL 设备 (Restricted CXL Device, RCD) 模式是一种具有以下限制的 CXL 操作模式：<br>• 不支持 Hot-Plug<br>• 在此模式下运行的 CXL 设备始终将 PCI Express Capabilities 寄存器中的 Device/Port Type 字段设置为 RCiEP<br>• 不支持 68B Flit Mode 以外的 Flit Mode<br>• 不支持 HBR 以外的路由类型<br>• 链路对非 CXL-aware 软件不可见</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-2"></a>
### 9.11.2 PCIe Software View of an RCH and RCD | RCH 与 RCD 的 PCIe 软件视图

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Because the CXL link is not exposed to CXL-unaware OSs, the System Firmware view of the hierarchy is different than that of the CXL-unaware OS.</td><td style="background-color:#e8e8e8">由于 CXL 链路不向不了解 CXL 的 OS (CXL-unaware OS) 暴露，因此系统固件视图的 Hierarchy 与 CXL-unaware OS 视图不同。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-3"></a>
### 9.11.3 System Firmware View of an RCH and RCD | RCH 与 RCD 的系统固件视图

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The functionality of the RCH Downstream Port and the RCD Upstream Port can be accessed via memory mapped registers. These will not show up in a standard PCIe bus scan by CXL-unaware OSs. The base addresses of these registers are set up by System Firmware and System Firmware can use that knowledge to configure CXL.</td><td style="background-color:#e8e8e8">RCH Downstream Port 和 RCD Upstream Port 的功能可通过内存映射寄存器访问。这些寄存器不会出现在 CXL-unaware OS 的标准 PCIe 总线扫描中。这些寄存器的基址由系统固件设置，系统固件可利用这些知识配置 CXL。</td></tr>
<tr><td>System Firmware configures the RCH Downstream Port to decode the memory resource needs of the CXL device as expressed by PCIe BARs and Upstream Port BAR(s). PCIe BARs are not to be configured to decode any HDM that are associated with the CXL device.</td><td style="background-color:#e8e8e8">系统固件配置 RCH Downstream Port 以解码 CXL 设备通过 PCIe BAR 和 Upstream Port BAR 表示的内存资源需求。PCIe BAR 不应配置为解码与 CXL 设备关联的任何 HDM。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-4"></a>
### 9.11.4 OS View of an RCH and RCD | RCH 与 RCD 的操作系统视图

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Each RCH-RCD pair is presented as one ACPI Host bridge. The _BBN method for this Host Bridge matches the bus number that hosts the RCD.</td><td style="background-color:#e8e8e8">每个 RCH-RCD 对呈现为一个 ACPI Host Bridge。此 Host Bridge 的 _BBN 方法与承载 RCD 的 Bus Number 匹配。</td></tr>
<tr><td>This ACPI Host Bridge spawns a legal PCIe hierarchy. All PCIe Endpoints located in the RCD are children of this ACPI Host Bridge. These Endpoints may appear directly on the Root bus number or may appear behind a Root Port located on the Root bus.</td><td style="background-color:#e8e8e8">此 ACPI Host Bridge 生成一个合法的 PCIe Hierarchy。位于 RCD 中的所有 PCIe Endpoint 都是此 ACPI Host Bridge 的子设备。这些 Endpoint 可直接出现在 Root Bus Number 上，也可出现在位于 Root Bus 上的 Root Port 之后。</td></tr>
<tr><td>The _CRS method for PCIe root bridge returns bus and memory resources claimed by the CXL Endpoints. _CRS response does not include HDM on CXL.mem-capable devices, and does not comprehend any Upstream Port BARs (hidden from OS).</td><td style="background-color:#e8e8e8">PCIe Root Bridge 的 _CRS 方法返回 CXL Endpoint 声明的总线和内存资源。_CRS 响应不包括支持 CXL.mem 的设备上的 HDM，也不理解任何 Upstream Port BAR (对 OS 隐藏)。</td></tr>
<tr><td>A CXL-aware OS may use CXL Early Discovery Table (CEDT) or _CBR object in ACPI namespace to locate the Downstream Port registers and Upstream Port registers. CEDT enumerates all CXL Host Bridges that are present at the time of OS hand-off and _CBR is limited to CXL Host Bridges that are hot-added.</td><td style="background-color:#e8e8e8">CXL-aware OS 可使用 CXL Early Discovery Table (CEDT) 或 ACPI 命名空间中的 _CBR 对象来定位 Downstream Port 寄存器和 Upstream Port 寄存器。CEDT 枚举 OS 交接时存在的所有 CXL Host Bridge，而 _CBR 仅限于被 Hot-Add 的 CXL Host Bridge。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-5"></a>
### 9.11.5 System Firmware-based RCD Enumeration Flow | 基于系统固件的 RCD 枚举流程

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Because RCDs do not support Hot-Add, RCDs can be fully enumerated by System Firmware prior to OS hand-off.</td><td style="background-color:#e8e8e8">由于 RCD 不支持 Hot-Add，RCD 可在 OS 交接之前由系统固件完全枚举。</td></tr>
<tr><td>In the presence of RCD mode, the hardware autonomous mode selection flow cannot automatically detect the number of retimers. If the system includes retimers, the System Firmware shall follow these steps to ensure that the number of retimers is correctly configured:<br>1. Prior to the link training, the System Firmware should set the DVSEC Flex Bus Port control register, based on the available information, to indicate whether there are 0, 1, or 2 retimers present. (It is possible that retimers on a CXL add-in card or a backplane may not be detected by the System Firmware prior to link training and the initial programming may not account for all retimers in the path.)<br>2. After the link training completes successfully or fails, the System Firmware should read the Retimer Presence Detected and Two Retimers Presence Detected values logged in the PCIe standard Link Status 2 register and determine whether they are consistent with what was set in the Flex Bus Port DVSEC in the previous step. If they are different, the System Firmware should bring the Link Down by setting the Link Disable bit in the Downstream Port, update the Retimer1_Present and Retimer2_Present bits in the Flex Bus Port DVSEC, and then re-initiate link training.</td><td style="background-color:#e8e8e8">在 RCD 模式下，硬件自主模式选择流程无法自动检测 Retimer 的数量。如果系统包含 Retimer，系统固件应遵循以下步骤以确保 Retimer 的数量被正确配置：<br>1. 在 Link Training 之前，系统固件应当根据可用信息设置 DVSEC Flex Bus Port Control 寄存器，以指示是否存在 0、1 或 2 个 Retimer。(有可能 CXL 附加卡或背板上的 Retimer 在 Link Training 之前不会被系统固件检测到，且初始编程可能不会考虑路径中的所有 Retimer。)<br>2. 在 Link Training 成功完成或失败之后，系统固件应当读取 PCIe 标准 Link Status 2 寄存器中记录的 Retimer Presence Detected 和 Two Retimers Presence Detected 值，并确定它们与上一步在 Flex Bus Port DVSEC 中设置的值是否一致。如果不同，系统固件应当通过设置 Downstream Port 中的 Link Disable 位使 Link Down，更新 Flex Bus Port DVSEC 中的 Retimer1_Present 和 Retimer2_Present 位，然后重新启动 Link Training。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-6"></a>
### 9.11.6 RCD Discovery | RCD 发现

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>1. Parse configuration space of Device 0, Function 0 on the Secondary bus # and discover CXL-specific attributes. These are exposed via PCIe DVSEC for CXL Devices Capability structures. See Section 8.1.3.<br>2. If the device supports CXL.cache, configure the CPU coherent bridge and then set the Cache_Enable bit in the DVSEC CXL Control register.<br>3. If the device supports CXL.mem, check Mem_HwInit_Mode by reading the DVSEC CXL Capability register and determine the number of supported HDM ranges by reading the HDM_Count field in the same register.<br>4. If Mem_HwInit_Mode=1:<br>&nbsp;&nbsp;— The device must set the Memory_Info_Valid bit in each applicable DVSEC CXL Range X Size Low register (X=1, 2) within 1 second of reset deassertion.<br>&nbsp;&nbsp;— The device must set the Memory_Active_Valid bit in each applicable DVSEC CXL Range X Size Low register (X=1, 2) within the Memory_Active_Timeout duration of reset deassertion.<br>&nbsp;&nbsp;— When Memory_Info_Valid is 1, System Firmware reads the Memory_Size_High and Memory_Size_Low fields for each supported HDM range. If System Firmware cannot delay boot until the Memory_Active bit is set, the System Firmware may continue with HDM base assignment and may delay OS hand-off until the Memory_Active bit is set.<br>&nbsp;&nbsp;— System Firmware computes the size of each HDM range and maps those in system address space.<br>&nbsp;&nbsp;— System Firmware programs the Memory_Base_Low and the Memory_Base_High fields for each HDM range.<br>&nbsp;&nbsp;— System Firmware programs the ARB/MUX arbitration control registers if necessary.<br>&nbsp;&nbsp;— System Firmware sets CXL.mem Enable. Once Memory_Active=1, Any subsequent accesses to HDM are decoded and routed to the local memory by the device.<br>&nbsp;&nbsp;— Each HDM range is later exposed to the OS as a separate, memory-only NUMA node via ACPI SRAT.<br>&nbsp;&nbsp;— System Firmware obtains CDAT from the UEFI device driver or directly from the device via Table Access DOE (see Section 8.1.11) and then uses this information during construction of the memory map, ACPI SRAT, and ACPI HMAT. See ACPI Specification, CDAT Specification, and UEFI Specification for further details.<br>5. If Mem_HwInit_Mode =0:<br>&nbsp;&nbsp;— The device must set the Memory_Info_Valid bit in each applicable DVSEC CXL Range X Size Low register (X=1, 2) within 1 second of reset deassertion.<br>&nbsp;&nbsp;— When Memory_Info_Valid is 1, System Firmware reads the Memory_Size_High and Memory_Size_Low fields for supported HDM ranges.<br>&nbsp;&nbsp;— System Firmware computes the size of each HDM range and maps those in system address space.<br>&nbsp;&nbsp;— System Firmware programs the Memory_Base_Low and the Memory_Base_High fields for each HDM range.<br>&nbsp;&nbsp;— System Firmware programs the ARB/MUX arbitration control registers if necessary.<br>&nbsp;&nbsp;— System Firmware sets CXL.mem Enable. Any subsequent accesses to the HDM ranges are decoded and completed by the device. The reads shall return all 1s and the writes will be dropped.<br>&nbsp;&nbsp;— Each HDM range is later exposed to the OS as a separate, memory-only NUMA node via ACPI SRAT.<br>&nbsp;&nbsp;— If the memory is initialized prior to OS boot by UEFI device driver: The UEFI driver is responsible for causing Memory_Active to be set. The driver can accomplish that by device-specific methods, such as by setting a device-specific register bit. After Memory_Active is set, any subsequent accesses to the HDM range are decoded and routed to the local memory by the device. System Firmware uses the information supplied by UEFI driver or Table Access DOE (see Section 8.1.11) during construction of the memory map and ACPI HMAT.<br>&nbsp;&nbsp;— If the memory is initialized by an OS device driver post OS boot: System Firmware may use the information supplied by UEFI driver or Table Access DOE (see Section 8.1.11) during construction of the memory map and ACPI HMAT. A CXL-aware OS may extract this information directly from the device via Table Access DOE. At OS hand-off, System Firmware reports that the memory size associated with HDM NUMA node is 0. The OS device driver is responsible for causing the Memory_Active bit to be set to 1 by using device-specific methods after memory initialization is complete. Memory availability is signaled to the OS via an OS-specific mechanism.</td><td style="background-color:#e8e8e8">1. 解析 Secondary Bus # 上 Device 0, Function 0 的 Configuration Space 并发现 CXL 特定属性。这些通过 PCIe DVSEC for CXL Devices Capability 结构暴露。见第 8.1.3 节。<br>2. 如果设备支持 CXL.cache，配置 CPU Coherent Bridge，然后设置 DVSEC CXL Control 寄存器中的 Cache_Enable 位。<br>3. 如果设备支持 CXL.mem，通过读取 DVSEC CXL Capability 寄存器检查 Mem_HwInit_Mode，并通过读取同一寄存器中的 HDM_Count 字段确定支持的 HDM Range 数量。<br>4. 如果 Mem_HwInit_Mode=1：<br>&nbsp;&nbsp;— 设备必须在复位解除 (Reset Deassertion) 后 1 秒内，在每个适用的 DVSEC CXL Range X Size Low 寄存器 (X=1, 2) 中设置 Memory_Info_Valid 位。<br>&nbsp;&nbsp;— 设备必须在复位解除后 Memory_Active_Timeout 持续时间内，在每个适用的 DVSEC CXL Range X Size Low 寄存器 (X=1, 2) 中设置 Memory_Active_Valid 位。<br>&nbsp;&nbsp;— 当 Memory_Info_Valid=1 时，系统固件读取每个支持的 HDM Range 的 Memory_Size_High 和 Memory_Size_Low 字段。如果系统固件不能延迟启动直到 Memory_Active 位被设置，系统固件可继续进行 HDM Base 分配，并可延迟 OS 交接直到 Memory_Active 位被设置。<br>&nbsp;&nbsp;— 系统固件计算每个 HDM Range 的大小并将其映射到系统地址空间。<br>&nbsp;&nbsp;— 系统固件为每个 HDM Range 编程 Memory_Base_Low 和 Memory_Base_High 字段。<br>&nbsp;&nbsp;— 系统固件在必要时编程 ARB/MUX 仲裁控制寄存器。<br>&nbsp;&nbsp;— 系统固件设置 CXL.mem Enable。一旦 Memory_Active=1，任何对 HDM 的后续访问将被设备解码并路由到本地内存。<br>&nbsp;&nbsp;— 每个 HDM Range 随后通过 ACPI SRAT 向 OS 暴露为独立的、仅内存的 NUMA 节点。<br>&nbsp;&nbsp;— 系统固件从 UEFI 设备驱动程序或通过 Table Access DOE (见第 8.1.11 节) 直接从设备获取 CDAT，然后在构建内存映射、ACPI SRAT 和 ACPI HMAT 时使用此信息。更多细节请参见 ACPI 规范、CDAT 规范和 UEFI 规范。<br>5. 如果 Mem_HwInit_Mode=0：<br>&nbsp;&nbsp;— 设备必须在复位解除后 1 秒内，在每个适用的 DVSEC CXL Range X Size Low 寄存器 (X=1, 2) 中设置 Memory_Info_Valid 位。<br>&nbsp;&nbsp;— 当 Memory_Info_Valid=1 时，系统固件读取支持的 HDM Range 的 Memory_Size_High 和 Memory_Size_Low 字段。<br>&nbsp;&nbsp;— 系统固件计算每个 HDM Range 的大小并将其映射到系统地址空间。<br>&nbsp;&nbsp;— 系统固件为每个 HDM Range 编程 Memory_Base_Low 和 Memory_Base_High 字段。<br>&nbsp;&nbsp;— 系统固件在必要时编程 ARB/MUX 仲裁控制寄存器。<br>&nbsp;&nbsp;— 系统固件设置 CXL.mem Enable。对 HDM Range 的任何后续访问由设备解码并完成。读操作应返回全 1s，写操作将被丢弃。<br>&nbsp;&nbsp;— 每个 HDM Range 随后通过 ACPI SRAT 向 OS 暴露为独立的、仅内存的 NUMA 节点。<br>&nbsp;&nbsp;— 如果内存由 UEFI 设备驱动程序在 OS 启动前初始化：UEFI 驱动程序负责导致 Memory_Active 被设置。驱动程序可通过设备特定的方法完成，例如设置设备特定的寄存器位。Memory_Active 被设置后，对 HDM Range 的任何后续访问由设备解码并路由到本地内存。系统固件在构建内存映射和 ACPI HMAT 时使用 UEFI 驱动程序或 Table Access DOE (见第 8.1.11 节) 提供的信息。<br>&nbsp;&nbsp;— 如果内存由 OS 设备驱动程序在 OS 启动后初始化：系统固件可在此过程中使用 UEFI 驱动程序或 Table Access DOE (见第 8.1.11 节) 提供的信息。CXL-aware OS 可直接通过 Table Access DOE 从设备提取此信息。在 OS 交接时，系统固件报告与 HDM NUMA 节点关联的内存大小为 0。OS 设备驱动程序负责在内存初始化完成后，使用设备特定的方法将 Memory_Active 位设置为 1。内存可用性通过 OS 特定的机制通知 OS。</td></tr>
<tr><td>CXL.io resource needs are discovered as part of PCIe enumeration. PCIe Root Complex registers, including Downstream Port registers, are appropriately configured to decode these resources. CXL Downstream Ports and Upstream Ports require MMIO resources. These are also accounted for during this process.</td><td style="background-color:#e8e8e8">CXL.io 资源需求作为 PCIe 枚举的一部分被发现。PCIe Root Complex 寄存器 (包括 Downstream Port 寄存器) 被适当配置以解码这些资源。CXL Downstream Port 和 Upstream Port 需要 MMIO 资源。这些在此过程中也会被考虑。</td></tr>
<tr><td>System Firmware programs the memory base and limit registers in the Downstream Port to decode CXL Endpoint MMIO BARs, CXL Downstream Port MMIO BARs, and CXL Upstream Port MMIO BARs.</td><td style="background-color:#e8e8e8">系统固件编程 Downstream Port 中的 Memory Base 和 Limit 寄存器，以解码 CXL Endpoint MMIO BAR、CXL Downstream Port MMIO BAR 和 CXL Upstream Port MMIO BAR。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-7"></a>
### 9.11.7 eRCDs with Multiple Flex Bus Links | 多 Flex Bus 链路的 eRCD

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section is applicable only to eRCDs that are directly connected to an eRCH. It does not apply to CXL VH. Also, it does not apply to eRCDs that are connected to CXL switches.</td><td style="background-color:#e8e8e8">本节仅适用于直接连接到 eRCH 的 eRCD。不适用于 CXL VH。也不适用于连接到 CXL 交换机的 eRCD。</td></tr>
</tbody>
</table>

<a id="sec-9-11-7-1"></a>
#### 9.11.7.1 Single CPU Topology | 单 CPU 拓扑

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>In this configuration, the System Firmware shall report two PCIe Host Bridges to the OS, one that hosts Device 0, Function 0 on the left, and a second one that hosts Device 0, Function 0 on the right. Both Device 0, Function 0 instances implement PCIe DVSEC for CXL Devices and a Device Serial Number PCIe Extended Capability. A Vendor ID and serial number match indicates that the two links are connected to a single CXL device, which enables System Firmware to perform certain optimizations.</td><td style="background-color:#e8e8e8">在此配置中，系统固件应向 OS 报告两个 PCIe Host Bridge，一个承载左侧 Device 0, Function 0，另一个承载右侧 Device 0, Function 0。两个 Device 0, Function 0 实例实现 PCIe DVSEC for CXL Devices 和 Device Serial Number PCIe Extended Capability。Vendor ID 和 Serial Number 匹配表明两条链路连接到单个 CXL 设备，这使系统固件能够执行某些优化。</td></tr>
<tr><td>In some cases, the CXL device may expose a single CXL device function that is managed by the CXL device's driver, whereas the other Device 0, Function 0 represents a dummy device. In this configuration, application software may submit work to the single CXL device instance. However, the CXL device hardware is free to use both links for traffic and snoops as long as the programming model is not violated.</td><td style="background-color:#e8e8e8">在某些情况下，CXL 设备可能暴露由 CXL 设备驱动程序管理的单个 CXL 设备 Function，而另一个 Device 0, Function 0 代表一个 Dummy Device。在此配置中，应用软件可向单个 CXL 设备实例提交工作。然而，CXL 设备硬件可以自由使用两条链路进行流量和 Snoop，只要不违反编程模型即可。</td></tr>
<tr><td>The System Firmware maps the HDM into system address space using the rules listed in Table 9-4.</td><td style="background-color:#e8e8e8">系统固件使用表 9-4 中列出的规则将 HDM 映射到系统地址空间。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-7-2"></a>
#### 9.11.7.2 Multiple CPU Topology | 多 CPU 拓扑

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>In this configuration, System Firmware shall report two PCIe Host Bridges to the OS, one that hosts Device 0, Function 0 on the left, and a second one that hosts Device 0, Function 0 on the right. Both Device 0, Function 0 instances implement PCIe DVSEC for CXL Devices and a Device Serial Number PCIe Extended Capability. A Vendor ID and serial number match indicates that the two links are connected to a single accelerator, which enables System Firmware to perform certain optimizations.</td><td style="background-color:#e8e8e8">在此配置中，系统固件应向 OS 报告两个 PCIe Host Bridge，一个承载左侧 Device 0, Function 0，另一个承载右侧 Device 0, Function 0。两个 Device 0, Function 0 实例实现 PCIe DVSEC for CXL Devices 和 Device Serial Number PCIe Extended Capability。Vendor ID 和 Serial Number 匹配表明两条链路连接到单个加速器，这使系统固件能够执行某些优化。</td></tr>
<tr><td>In some cases, the accelerator may choose to expose a single accelerator function that is managed by the accelerator device driver and handles all work requests. This may be necessary if the accelerator framework or applications do not support distributing work across multiple accelerator instances. Even in this case, both links should spawn a legal PCIe Host Bridge hierarchy with at least one PCIe function. However, the accelerator hardware is free to use both links for traffic and snoops as long as the programming model is not violated. To minimize the snoop penalty, the accelerator needs to be able to distinguish between the system memory range decoded by CPU 1 vs. CPU 2. The device driver can obtain this information via ACPI SRAT and communicate it to the accelerator using device-specific mechanisms.</td><td style="background-color:#e8e8e8">在某些情况下，加速器可以选择暴露一个由加速器设备驱动程序管理的单个加速器 Function 来处理所有工作请求。如果加速器框架或应用程序不支持跨多个加速器实例分配工作，这可能是必要的。即使在这种情况下，两条链路都应该生成一个合法的 PCIe Host Bridge Hierarchy，其中至少包含一个 PCIe Function。然而，加速器硬件可以自由使用两条链路进行流量和 Snoop，只要不违反编程模型即可。为最小化 Snoop Penalty，加速器需要能够区分 CPU 1 与 CPU 2 解码的系统内存范围。设备驱动程序可通过 ACPI SRAT 获取此信息，并使用设备特定的机制将其传达给加速器。</td></tr>
<tr><td>The System Firmware maps the HDM into system address space using the following rules. Unlike the single CPU case, the System Firmware shall never interleave the memory range across the two Flex Bus links.</td><td style="background-color:#e8e8e8">系统固件使用以下规则将 HDM 映射到系统地址空间。与单 CPU 情况不同，系统固件永远不应跨两条 Flex Bus 链路交织内存范围。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-11-8"></a>
### 9.11.8 CXL Devices Attached to an RCH | 连接到 RCH 的 CXL 设备

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>When an eRCD is attached to an RCH, the register layout matches Figure 9-4.</td><td style="background-color:#e8e8e8">当 eRCD 连接到 RCH 时，寄存器布局与图 9-4 匹配。</td></tr>
<tr><td>When a CXL device other than an eRCD is attached to a CXL RP or a CXL DSP, the device's Upstream Port registers are accessed via the CXL Device's PCIe Configuration space and BAR. A CXL device may be designed so that the layout of the device's Upstream Port and Component Registers follow Figure 9-4 when connected to an RCH. For such a device, some of these registers must be remapped so that they are accessible via an RCD Upstream Port RCRB (see Section 8.2.1.2, Section 8.2.1.3, and Section 8.2.2). This register remapping is illustrated in Figure 9-7.</td><td style="background-color:#e8e8e8">当非 eRCD 的 CXL 设备连接到 CXL RP 或 CXL DSP 时，设备的 Upstream Port 寄存器通过 CXL 设备的 PCIe Configuration Space 和 BAR 访问。CXL 设备可以设计为在连接到 RCH 时，设备的 Upstream Port 和 Component Register 的布局遵循图 9-4。对于此类设备，其中一些寄存器必须重新映射，以便通过 RCD Upstream Port RCRB 访问 (见第 8.2.1.2 节、第 8.2.1.3 节和第 8.2.2 节)。此寄存器重新映射如图 9-7 所示。</td></tr>
<tr><td>Such a device shall capture the upper address bits [63:12] of the first memory read received after link initialization as the base address of the Upstream Port RCRB (see Section 8.2.1.2).</td><td style="background-color:#e8e8e8">此类设备应捕获链路初始化后收到的第一个 Memory Read 的上地址位 [63:12]，作为 Upstream Port RCRB 的基址 (见第 8.2.1.2 节)。</td></tr>
<tr><td>A CXL device may be designed so that the layout of the device's Upstream Port and Component Registers still follows the CXL device layout for a CXL VH when connected to an RCH. In that case, the register remapping is unnecessary. This is illustrated in Figure 9-8. Such a device shall capture the upper address bits [63:12] of the first memory read received after link initialization as the base address of the Upstream Port RCRB, but all reads to the Upstream Port RCRB range shall return all 1s. Additionally, all writes shall be completed, but silently dropped by such a device. Note that the DWORD read to RCRB Base + 4 KB is guaranteed to return a value other than FFFF FFFFh when directed at an eRCD or a CXL device that follows the Figure 9-4 register layout when connected to an RCH (see Figure 8-10). An RCD is also permitted to implement the register mapping scheme shown in the right half of Figure 9-8. In both cases, the RCD appears as an RCiEP.</td><td style="background-color:#e8e8e8">CXL 设备可以设计为在连接到 RCH 时，设备的 Upstream Port 和 Component Register 的布局仍遵循 CXL VH 的 CXL 设备布局。在这种情况下，寄存器重新映射是不必要的。这如图 9-8 所示。此类设备应捕获链路初始化后收到的第一个 Memory Read 的上地址位 [63:12] 作为 Upstream Port RCRB 的基址，但对 Upstream Port RCRB 范围的所有读操作应返回全 1s。此外，所有写操作应被完成，但由此类设备静默丢弃。请注意，当针对 eRCD 或在连接到 RCH 时遵循图 9-4 寄存器布局的 CXL 设备时，对 RCRB Base + 4 KB 的 DWORD 读操作保证返回非 FFFF FFFFh 的值 (见图 8-10)。RCD 也被允许实现图 9-8 右半部分所示的寄存器映射方案。在两种情况下，RCD 都显示为 RCiEP。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12"></a>
## 9.12 CXL VH Enumeration | CXL VH 枚举

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>At the top level, a CXL system may be represented to the system software as zero or more CXL Host bridges, and zero or more PCIe Host Bridges. A CXL Host Bridge is a software concept that represents one of the following:<br>• A collection of CXL Root Ports that share some logic, such as CHBCR<br>• An RCH-RCD pair<br>• One or more CXL Root Complex Integrated Endpoints, all of which are part of the Root Complex and appear at the same bus number</td><td style="background-color:#e8e8e8">在顶层，CXL 系统可向系统软件表示为零个或多个 CXL Host Bridge，以及零个或多个 PCIe Host Bridge。CXL Host Bridge 是一个软件概念，代表以下之一：<br>• 共享某些逻辑 (如 CHBCR) 的一组 CXL Root Port<br>• 一个 RCH-RCD 对<br>• 一个或多个 CXL Root Complex Integrated Endpoint，均为 Root Complex 的一部分并出现在相同的 Bus Number 上</td></tr>
<tr><td>Enumeration of PCIe Host Bridges and PCIe hierarchy underneath them is governed by PCIe Base Specification. Enumeration of CXL Host Bridges is described below.</td><td style="background-color:#e8e8e8">PCIe Host Bridge 及其下 PCIe Hierarchy 的枚举由 PCIe 基本规范管理。CXL Host Bridge 的枚举如下所述。</td></tr>
<tr><td>In an ACPI-compliant system, CXL Host Bridges are identified with an ACPI Hardware ID (HID) of "ACPI0016". CXL Early Discovery Table (CEDT) may be used to differentiate between the three software concepts listed above. RCD enumeration is described in Section 9.11.</td><td style="background-color:#e8e8e8">在符合 ACPI 的系统中，CXL Host Bridge 通过 ACPI Hardware ID (HID) 为 "ACPI0016" 来标识。CXL Early Discovery Table (CEDT) 可用于区分上述三种软件概念。RCD 枚举见第 9.11 节。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12-1"></a>
### 9.12.1 CXL Root Ports | CXL 根端口

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Each CXL Host Bridge is associated with a Base Bus Number. If the Host Bridge is not associated with RCDs or CXL RCiEPs, that bus number shall contain one or more CXL Root Ports. These Root Ports appear in PCIe configuration space with a Type 1 header, and the Device/Port Type field in the PCIe Capabilities Register shall identify these as standard PCIe Root Ports. Unless specified otherwise, CXL Root Ports may implement all Capabilities that are defined in PCIe Base Specification as legal for PCIe Root Ports.</td><td style="background-color:#e8e8e8">每个 CXL Host Bridge 关联一个 Base Bus Number。如果 Host Bridge 不与 RCD 或 CXL RCiEP 关联，则该 Bus Number 应包含一个或多个 CXL Root Port。这些 Root Port 在 PCIe Configuration Space 中以 Type 1 Header 出现，PCIe Capabilities Register 中的 Device/Port Type 字段应将其标识为标准 PCIe Root Port。除非另有规定，CXL Root Port 可实现 PCIe 基本规范中定义为 PCIe Root Port 合法的所有 Capability。</td></tr>
<tr><td>These Root Ports can be in one of four states:<br>• Disconnected<br>• Connected to an eRCD<br>• Connected to CXL Device that is not an eRCD, or connected to a CXL Switch<br>• Connected to a PCIe Device/Switch<br>Section 9.12.3 describes how software can determine the current state of a CXL Root Port and the corresponding enumeration algorithm.</td><td style="background-color:#e8e8e8">这些 Root Port 可处于以下四种状态之一：<br>• Disconnected (断开连接)<br>• Connected to an eRCD (连接到 eRCD)<br>• Connected to CXL Device that is not an eRCD, or connected to a CXL Switch (连接到非 eRCD 的 CXL 设备或 CXL 交换机)<br>• Connected to a PCIe Device/Switch (连接到 PCIe 设备/交换机)<br>第 9.12.3 节描述了软件如何确定 CXL Root Port 的当前状态及相应的枚举算法。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12-2"></a>
### 9.12.2 CXL Virtual Hierarchy | CXL 虚拟层级

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL Root Ports may be directly connected to a CXL device that is not an eRCD, or a CXL Switch. These Root Ports spawn a CXL Virtual Hierarchy (VH). Enumeration within a CXL VH is described below.</td><td style="background-color:#e8e8e8">CXL Root Port 可直接连接到非 eRCD 的 CXL 设备或 CXL 交换机。这些 Root Port 生成 CXL Virtual Hierarchy (VH)。CXL VH 内的枚举如下所述。</td></tr>
<tr><td>These CXL devices appear as a standard PCIe Endpoints with a Type 0 Header. The CXL device's primary function (Function 0) shall carry one instance of CXL DVSEC ID 0 with Revision 1 or greater. Software may use this DVSEC instance to distinguish a CXL device from an ordinary PCIe device. Unless specified otherwise, CXL devices may implement all Capabilities that are defined in PCIe Base Specification as legal for PCIe devices.</td><td style="background-color:#e8e8e8">这些 CXL 设备显示为标准 PCIe Endpoint，具有 Type 0 Header。CXL 设备的 Primary Function (Function 0) 应携带一个 CXL DVSEC ID 0 实例，其 Revision 为 1 或更高。软件可使用此 DVSEC 实例将 CXL 设备与普通 PCIe 设备区分开。除非另有规定，CXL 设备可实现 PCIe 基本规范中定义为 PCIe 设备合法的所有 Capability。</td></tr>
<tr><td>A CXL VH may include zero or more CXL switches. Specific configuration constraints are documented in Chapter 7.0. From an enumeration software perspective, each CXL Switch consists of one Upstream Switch Port and one or more Downstream Switch Ports.</td><td style="background-color:#e8e8e8">CXL VH 可包括零个或多个 CXL 交换机。具体的配置约束记录在第 7.0 章中。从枚举软件的角度来看，每个 CXL 交换机由一个 Upstream Switch Port 和一个或多个 Downstream Switch Port 组成。</td></tr>
<tr><td>The configuration space of the Upstream Switch Port of a CXL Switch has a Type 1 header and the Device/Port Type field in the PCIe Capabilities Register shall identify it as an Upstream Port of a PCIe Switch. The configuration space carries one instance of the CXL DVSEC ID 3 and one instance of DVSEC ID 7. The DVSEC Flex Bus Port Status register in CXL DVSEC ID 7 structure of the peer Port shall indicate that CXL VH operation with 68B Flit mode was negotiated with the Upstream Switch Port during link training. Unless specified otherwise, CXL Upstream Switch Ports may implement all Capabilities that are defined in PCIe Base Specification as legal for PCIe Upstream Switch Ports.</td><td style="background-color:#e8e8e8">CXL 交换机的 Upstream Switch Port 的 Configuration Space 具有 Type 1 Header，PCIe Capabilities Register 中的 Device/Port Type 字段应将其标识为 PCIe 交换机的 Upstream Port。Configuration Space 携带一个 CXL DVSEC ID 3 实例和一个 DVSEC ID 7 实例。对端 Port 的 CXL DVSEC ID 7 结构中的 DVSEC Flex Bus Port Status 寄存器应指示在 Link Training 期间与 Upstream Switch Port 协商了 CXL VH 操作与 68B Flit Mode。除非另有规定，CXL Upstream Switch Port 可实现 PCIe 基本规范中定义为 PCIe Upstream Switch Port 合法的所有 Capability。</td></tr>
<tr><td>The configuration space of a Downstream Switch Port of CXL Switch also has a Type 1 header, but the Device/Port Type field in the PCIe Capabilities Register shall identify these as a Downstream Port of a PCIe Switch. All these Ports are CXL capable and can be in one of four states, just like the CXL Root Ports:<br>• Disconnected<br>• Connected to an eRCD<br>• Connected to CXL Device that is not an eRCD, or connected to a CXL Switch<br>• Connected to a PCIe Device/Switch<br>Section 9.12.3 describes how software can determine the current state of a CXL Downstream Switch Port and the corresponding enumeration algorithm.</td><td style="background-color:#e8e8e8">CXL 交换机的 Downstream Switch Port 的 Configuration Space 也具有 Type 1 Header，但 PCIe Capabilities Register 中的 Device/Port Type 字段应将其标识为 PCIe 交换机的 Downstream Port。所有这些 Port 都支持 CXL，并且与 CXL Root Port 一样可处于四种状态之一：<br>• Disconnected (断开连接)<br>• Connected to an eRCD (连接到 eRCD)<br>• Connected to CXL Device that is not an eRCD, or connected to a CXL Switch (连接到非 eRCD 的 CXL 设备或 CXL 交换机)<br>• Connected to a PCIe Device/Switch (连接到 PCIe 设备/交换机)<br>第 9.12.3 节描述了软件如何确定 CXL Downstream Switch Port 的当前状态及相应的枚举算法。</td></tr>
<tr><td>A CXL Downstream Switch Port may be connected to another CXL Switch or a CXL device. The rules for enumerating CXL switches and CXL devices are already covered earlier in this section.</td><td style="background-color:#e8e8e8">CXL Downstream Switch Port 可连接到另一个 CXL 交换机或 CXL 设备。枚举 CXL 交换机和 CXL 设备的规则已在本节前面部分说明。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12-3"></a>
### 9.12.3 Enumerating CXL RPs and DSPs | 枚举 CXL RP 与 DSP

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Software may use the combination of the Link Status registers and the CXL DVSEC ID 7 capability in root port or DSP configuration space to determine which state a CXL Downstream Port is in, as follows:<br>1. CXL root port or DSP is in the Disconnected state when they do not have an active link. The status of the link can be detected by following PCIe Base Specification. If the link is not up, software shall ignore the CXL DVSEC ID 3 and the CXL DVSEC ID 7 capability structures. A Hot-Add event may transition a Disconnected Port to a CXL Connected state or a PCIe Connected state. Hot-adding an eRCD adapter will transition the Port to an Undefined state.<br>2. CXL root port or DSP connected to a CXL device that is not an RCD or connected to a CXL switch shall expose one instance of the CXL DVSEC ID 3 and one instance of the CXL DVSEC ID 7 capability structures. The DVSEC Flex Bus Port Status register in the CXL DVSEC ID 7 structure shall indicate that CXL VH operation with 68B Flit mode was successfully negotiated during link training. System Firmware may leave the Unmask SBR and the Unmask Link Disable bits in the Port Control register of the Downstream Port at the default (0) values to prevent CXL-unaware PCIe software from resetting the device and the link, respectively.<br>3. CXL root port or DSP connected to an eRCD shall expose one instance of the CXL DVSEC ID 3 and one instance of the CXL DVSEC ID 7 capability structures. The DVSEC Flex Bus Port Status register in the CXL DVSEC ID 7 structure shall indicate that CXL VH operation with 68B Flit mode was not negotiated, but that either the CXL.cache protocol or the CXL.mem protocol was negotiated during link training. There are two possible substates:<br>&nbsp;&nbsp;a. Not Operating with RCH Downstream Port addressing - Immediately after the link negotiation, the Port registers appear in the PCIe configuration space with a Type 1 header.<br>&nbsp;&nbsp;b. Operating with RCH Downstream Port addressing - System Firmware may program the RCRB Base register in the Port's CXL DVSEC ID 3 capability structure to transition the Port to this mode. Once the Port is in this mode, it can only transition out of the mode after a reset. A Downstream Port operating in this mode shall ignore hot reset requests received from the Upstream Port.<br>4. CXL root port or DSP connected to a PCIe device/switch may or may not expose the CXL DVSEC ID 3 and the CXL DVSEC ID 7 capability structures.<br>&nbsp;&nbsp;a. If the PCIe root port configuration space contains an instance of the CXL DVSEC ID 3 structure, it shall also contain an instance of the CXL DVSEC ID 7 structure.<br>&nbsp;&nbsp;b. If the PCIe root port configuration space contains an instance of the CXL DVSEC ID 7 structure, the DVSEC Flex Bus Port Status register shall indicate that this Port did not train up in CXL mode. Software shall ignore the contents of the CXL DVSEC ID 3 structure for such a Port.</td><td style="background-color:#e8e8e8">软件可使用 Root Port 或 DSP Configuration Space 中的 Link Status 寄存器与 CXL DVSEC ID 7 Capability 的组合来确定 CXL Downstream Port 处于哪种状态，如下所示：<br>1. 当 CXL Root Port 或 DSP 没有 Active Link 时，处于 Disconnected 状态。链路的Status 可按照 PCIe 基本规范检测。如果链路未 UP，软件应忽略 CXL DVSEC ID 3 和 CXL DVSEC ID 7 Capability 结构。Hot-Add 事件可将 Disconnected Port 转换为 CXL Connected 状态或 PCIe Connected 状态。Hot-Add eRCD 适配器会将 Port 转换为 Undefined 状态。<br>2. 连接到非 RCD 的 CXL 设备或连接到 CXL 交换机的 CXL Root Port 或 DSP，应暴露一个 CXL DVSEC ID 3 和一个 CXL DVSEC ID 7 Capability 结构实例。CXL DVSEC ID 7 结构中的 DVSEC Flex Bus Port Status 寄存器应指示在 Link Training 期间成功协商了 CXL VH 操作与 68B Flit Mode。系统固件可将 Downstream Port 的 Port Control 寄存器中的 Unmask SBR 和 Unmask Link Disable 位保留为默认值 (0)，以分别防止不了解 CXL 的 PCIe 软件复位设备和链路。<br>3. 连接到 eRCD 的 CXL Root Port 或 DSP 应暴露一个 CXL DVSEC ID 3 和一个 CXL DVSEC ID 7 Capability 结构实例。CXL DVSEC ID 7 结构中的 DVSEC Flex Bus Port Status 寄存器应指示未协商 CXL VH 操作与 68B Flit Mode，但在 Link Training 期间协商了 CXL.cache 协议或 CXL.mem 协议。存在两种可能的子状态：<br>&nbsp;&nbsp;a. Not Operating with RCH Downstream Port addressing (不使用 RCH Downstream Port 寻址操作) - 链路协商后立即，Port 寄存器以 Type 1 Header 出现在 PCIe Configuration Space 中。<br>&nbsp;&nbsp;b. Operating with RCH Downstream Port addressing (使用 RCH Downstream Port 寻址操作) - 系统固件可编程 Port 的 CXL DVSEC ID 3 Capability 结构中的 RCRB Base 寄存器，将 Port 转换为此模式。一旦 Port 处于此模式，只能在复位后退出此模式。在此模式下运行的 Downstream Port 应忽略从 Upstream Port 收到的 Hot Reset 请求。<br>4. 连接到 PCIe 设备/交换机的 CXL Root Port 或 DSP 可能暴露也可能不暴露 CXL DVSEC ID 3 和 CXL DVSEC ID 7 Capability 结构。<br>&nbsp;&nbsp;a. 如果 PCIe Root Port Configuration Space 包含 CXL DVSEC ID 3 结构实例，则还应包含 CXL DVSEC ID 7 结构实例。<br>&nbsp;&nbsp;b. 如果 PCIe Root Port Configuration Space 包含 CXL DVSEC ID 7 结构实例，则 DVSEC Flex Bus Port Status 寄存器应指示此 Port 未在 CXL 模式下完成 Link Training。软件应忽略此类 Port 的 CXL DVSEC ID 3 结构内容。</td></tr>
<tr><td>If the Port is in the disconnected state, the branch does not need further enumeration. If the Port is connected to a CXL device other than an eRCD or connected to a CXL switch, the software follows Section 9.12.2 for further enumeration until it reaches the leaf endpoint. If the Port is connected to an RCD, the software follows Section 9.12.4 to enumerate the device. If the Port is connected to a PCIe device/switch, the enumeration flow is governed by PCIe Base Specification.</td><td style="background-color:#e8e8e8">如果 Port 处于 Disconnected 状态，则该分支无需进一步枚举。如果 Port 连接到非 eRCD 的 CXL 设备或连接到 CXL 交换机，软件按照第 9.12.2 节继续枚举直到达到 Leaf Endpoint。如果 Port 连接到 RCD，软件按照第 9.12.4 节枚举设备。如果 Port 连接到 PCIe 设备/交换机，枚举流程由 PCIe 基本规范管理。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12-4"></a>
### 9.12.4 eRCD Connected to a CXL RP or DSP | 连接到 CXL RP 或 DSP 的 eRCD

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>An eRCD may be connected to a CXL Root Port or a CXL Downstream Switch Port. Each RCD Function must report itself as an RCiEP and therefore cannot appear, to software, to be below a PCIe-enumerable Downstream Port. System Firmware is responsible for detecting such a case and reconfiguring the CXL Ports in the path so that the RCD appears to software to be directly connected to an RCH Downstream Port and not in a CXL VH.</td><td style="background-color:#e8e8e8">eRCD 可连接到 CXL Root Port 或 CXL Downstream Switch Port。每个 RCD Function 必须将自身报告为 RCiEP，因此对软件而言不能出现在 PCIe 可枚举的 Downstream Port 之下。系统固件负责检测此类情况并重新配置路径中的 CXL Port，使 RCD 在软件中显示为直接连接到 RCH Downstream Port，而非处于 CXL VH 中。</td></tr>
</tbody>
</table>

<a id="sec-9-12-4-1"></a>
#### 9.12.4.1 Boot time Reconfiguration of CXL RP or DSP to Enable an eRCD | 引导时重新配置 CXL RP 或 DSP 以启用 eRCD

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>1. At reset, the Downstream Port registers are visible in the PCIe configuration space with a Type 1 header. During enumeration, System Firmware shall identify all the Downstream Ports that are connected to the eRCD by reading the DVSEC ID 7 register instead of the Link status registers.<br>&nbsp;&nbsp;— If the link training was successful, the DVSEC Flex Bus Port Status register in the CXL DVSEC ID 7 structure shall indicate that CXL VH operation with 68B Flit mode was not negotiated, but shall indicate that either the CXL.cache protocol or the CXL.mem protocol was negotiated during link training.<br>&nbsp;&nbsp;— If the link training was unsuccessful, the DVSEC Flex Bus Port Received Modified TS Data Phase1 Register in the CXL DVSEC ID 7 structure shall indicate that the device is CXL capable but not CXL VH capable. A DSP shall not report link-up status in the PCIe Link Status register when the DSP detects an eRCD on the other end to prevent the CXL-unaware software from discovering the eRCD.<br>2. System Firmware identifies MMIO and bus resource needs for all RCDs below a CXL root port. System Firmware adds MMIO resources needed for the RCH Downstream Port RCRB and RCD Upstream Port RCRB (8-KB MMIO per link) and CXL Component registers (128-KB MMIO per link).<br>3. System Firmware assigns MMIO and bus resources and programs the Alternate MMIO Base/Limit and Alternate Bus Base/Limit registers in all the Root Ports and the Switch Ports in the path and the eRCD BARs except the Downstream Ports that are directly connected to eRCDs. These Alternate decoders are described in Section 8.1.5.<br>4. System Firmware sets the Alt BME and Alt Memory and ID Space Enable bits in all the Root Ports and the Switch Ports in the path of every eRCD.<br>5. For each Downstream Port that is connected to an eRCD, System Firmware programs the CXL RCRB Base Address. System Firmware then writes 1 to the CXL RCRB Enable bit, which transitions the port addressing to RCH addressing. The Downstream Port registers now appear in MMIO space at CXL RCRB Base and not in configuration space. System Firmware issues a read to the address CXL RCRB Base + 4 KB. The RCD Upstream Port captures its RCRB Base as described in Section 8.1.5. System Firmware configures Upstream Port and Downstream Port registers, as necessary. If this is a DSP, the Downstream Port shall ignore any hot reset requests received from the Upstream Port.<br>6. System Firmware configures the eRCD, using the algorithm described in Section 9.11.6.</td><td style="background-color:#e8e8e8">1. 在复位时，Downstream Port 寄存器在 PCIe Configuration Space 中以 Type 1 Header 可见。在枚举期间，系统固件应通过读取 DVSEC ID 7 寄存器 (而非 Link Status 寄存器) 来识别所有连接到 eRCD 的 Downstream Port。<br>&nbsp;&nbsp;— 如果 Link Training 成功，CXL DVSEC ID 7 结构中的 DVSEC Flex Bus Port Status 寄存器应指示未协商 CXL VH 操作与 68B Flit Mode，但应指示在 Link Training 期间协商了 CXL.cache 协议或 CXL.mem 协议。<br>&nbsp;&nbsp;— 如果 Link Training 不成功，CXL DVSEC ID 7 结构中的 DVSEC Flex Bus Port Received Modified TS Data Phase1 Register 应指示设备支持 CXL 但不支持 CXL VH。当 DSP 检测到对端是 eRCD 时，不应在 PCIe Link Status 寄存器中报告 Link-Up 状态，以防止不了解 CXL 的软件发现 eRCD。<br>2. 系统固件识别 CXL Root Port 下所有 RCD 的 MMIO 和总线资源需求。系统固件添加 RCH Downstream Port RCRB 和 RCD Upstream Port RCRB 所需的 MMIO 资源 (每条链路 8 KB MMIO) 以及 CXL Component 寄存器 (每条链路 128 KB MMIO)。<br>3. 系统固件分配 MMIO 和总线资源，并编程路径中所有 Root Port 和 Switch Port 的 Alternate MMIO Base/Limit 和 Alternate Bus Base/Limit 寄存器以及 eRCD BAR (除了直接连接到 eRCD 的 Downstream Port)。这些 Alternate Decoder 见第 8.1.5 节。<br>4. 系统固件在每个 eRCD 路径中的所有 Root Port 和 Switch Port 中设置 Alt BME、Alt Memory 和 ID Space Enable 位。<br>5. 对于连接到 eRCD 的每个 Downstream Port，系统固件编程 CXL RCRB Base Address。然后系统固件向 CXL RCRB Enable 位写入 1，将 Port 寻址转换为 RCH 寻址。Downstream Port 寄存器现在在 MMIO 空间中以 CXL RCRB Base 出现，而非在 Configuration Space 中。系统固件发出对地址 CXL RCRB Base + 4 KB 的读操作。RCD Upstream Port 按照第 8.1.5 节的描述捕获其 RCRB Base。系统固件根据需要配置 Upstream Port 和 Downstream Port 寄存器。如果这是 DSP，Downstream Port 应忽略从 Upstream Port 收到的任何 Hot Reset 请求。<br>6. 系统固件使用第 9.11.6 节所述的算法配置 eRCD。</td></tr>
<tr><td>The System Firmware shall report each RCD under a separate Host Bridge and not as part of the CXL VH.</td><td style="background-color:#e8e8e8">系统固件应将每个 RCD 报告在单独的 Host Bridge 下，而非作为 CXL VH 的一部分。</td></tr>
<tr><td>The Switch shall ensure that there is always a DSP visible at Device 0, Function 0.</td><td style="background-color:#e8e8e8">交换机应确保始终有一个 DSP 在 Device 0, Function 0 处可见。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12-5"></a>
### 9.12.5 CXL eRCD below a CXL RP and DSP - Example | CXL RP 与 DSP 下的 CXL eRCD — 示例

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Figure 9-12 represents the physical connectivity of a host with four Root Ports, one Switch, and 5 devices. The corresponding software view is shown in Figure 9-13.</td><td style="background-color:#e8e8e8">图 9-12 表示具有四个 Root Port、一个交换机和 5 个设备的主机的物理连接。相应的软件视图如图 9-13 所示。</td></tr>
<tr><td>As shown in Figure 9-12, the Switch makes eRCD 1, below its DSP (DSP 1), appear as an RCiEP under an RCH. eRCD 1 is exposed as a separate Host Bridge to the Operating System. The device hosts a CXL DVSEC ID 0 instance in Device 0, Function 0 Configuration Space. The RCH Downstream Port registers and the RCD Upstream Port registers appear in MMIO space as expected.</td><td style="background-color:#e8e8e8">如图 9-12 所示，交换机使其 DSP (DSP 1) 之下的 eRCD 1 显示为 RCH 下的 RCiEP。eRCD 1 作为单独的 Host Bridge 暴露给操作系统。该设备在 Device 0, Function 0 Configuration Space 中承载一个 CXL DVSEC ID 0 实例。RCH Downstream Port 寄存器和 RCD Upstream Port 寄存器如预期出现在 MMIO 空间中。</td></tr>
<tr><td>When a CXL Root Port detects a PCIe device (PCIe Device 1), the Root Port trains up in PCIe mode. The Root Port configuration space (Type 1) may include the CXL DVSEC ID 3 and the CXL DVSEC ID 7. If present, the DVSEC ID 7 instance will indicate that the link trained up in PCIe mode.</td><td style="background-color:#e8e8e8">当 CXL Root Port 检测到 PCIe 设备 (PCIe Device 1) 时，Root Port 以 PCIe 模式完成 Link Training。Root Port Configuration Space (Type 1) 可能包括 CXL DVSEC ID 3 和 CXL DVSEC ID 7。如果存在，DVSEC ID 7 实例将指示链路以 PCIe 模式完成 Training。</td></tr>
<tr><td>If a CXL Root Port (RP 2) is connected to an empty slot, its configuration space (Type 1) hosts the CXL DVSEC ID 3 and the CXL DVSEC ID 7, but the DVSEC ID 7 shall indicate no CXL connectivity and the PCIe Link status register shall indicate that there is no PCIe connectivity. The user can hot-add a CXL device other than eRCD, a CXL Switch, or a PCIe device in this slot.</td><td style="background-color:#e8e8e8">如果 CXL Root Port (RP 2) 连接到空插槽，其 Configuration Space (Type 1) 承载 CXL DVSEC ID 3 和 CXL DVSEC ID 7，但 DVSEC ID 7 应指示无 CXL 连接，且 PCIe Link Status 寄存器应指示无 PCIe 连接。用户可在此插槽中 Hot-Add 非 eRCD 的 CXL 设备、CXL 交换机或 PCIe 设备。</td></tr>
<tr><td>A CXL Root Port (RP 3) connected to a CXL Switch spawns a CXL VH. The Root Port as well as the Upstream Switch Port configuration space (Type 1) each host an instance of CXL DVSEC ID 3 and an instance of CXL DVSEC ID 7, but the DVSEC ID 7 instance will indicate that these Ports are operating in CXL VH operation with 68B Flit mode.</td><td style="background-color:#e8e8e8">连接到 CXL 交换机的 CXL Root Port (RP 3) 生成 CXL VH。Root Port 以及 Upstream Switch Port Configuration Space (Type 1) 各自承载一个 CXL DVSEC ID 3 实例和一个 CXL DVSEC ID 7 实例，但 DVSEC ID 7 实例将指示这些 Port 在 CXL VH 操作中以 68B Flit Mode 运行。</td></tr>
<tr><td>If a CXL Downstream Switch Port (DSP 2) is connected to a CXL device that is not an eRCD, DSP 2's configuration space (Type 1) hosts an instance of CXL DVSEC ID 3 and an instance of CXL DVSEC ID 7, but the DVSEC ID 7 instance will indicate that this Port is connected to a CXL device and is part of a CXL VH.</td><td style="background-color:#e8e8e8">如果 CXL Downstream Switch Port (DSP 2) 连接到非 eRCD 的 CXL 设备，DSP 2 的 Configuration Space (Type 1) 承载一个 CXL DVSEC ID 3 实例和一个 CXL DVSEC ID 7 实例，但 DVSEC ID 7 实例将指示此 Port 连接到 CXL 设备并且是 CXL VH 的一部分。</td></tr>
<tr><td>A CXL Downstream Switch Port (DSP 3) connected to a PCIe device does not host an instance of CXL DVSEC ID 7. Absence of a CXL DVSEC ID 7 indicates that this Port is not operating in the CXL mode. Note that it is legal for DSP 3 to host a DVSEC ID 7 instance as long as the DVSEC Flex Bus Port Status Register in the DVSEC ID 7 structure reports that the link is not operating in CXL mode.</td><td style="background-color:#e8e8e8">连接到 PCIe 设备的 CXL Downstream Switch Port (DSP 3) 不承载 CXL DVSEC ID 7 实例。缺少 CXL DVSEC ID 7 表明此 Port 未在 CXL 模式下运行。注意，DSP 3 承载 DVSEC ID 7 实例是合法的，只要 DVSEC ID 7 结构中的 DVSEC Flex Bus Port Status Register 报告链路未在 CXL 模式下运行即可。</td></tr>
<tr><td>If a CXL Root Port (RP 4) is connected to an eRCD, the Root Port operates as an RCH Downstream Port. eRCD 2 appears as an RCiEP under its own Host Bridge. The RCH Downstream Port registers and the RCD Upstream Port registers appear in MMIO space as expected.</td><td style="background-color:#e8e8e8">如果 CXL Root Port (RP 4) 连接到 eRCD，Root Port 作为 RCH Downstream Port 运行。eRCD 2 作为 RCiEP 出现在其自己的 Host Bridge 下。RCH Downstream Port 寄存器和 RCD Upstream Port 寄存器如预期出现在 MMIO 空间中。</td></tr>
<tr><td>If the Switch is Hot-Pluggable, System Firmware may instantiate a _DEP object in the ACPI namespace to indicate that Device 1 is dependent on the CXL USP.</td><td style="background-color:#e8e8e8">如果交换机支持 Hot-Plug，系统固件可在 ACPI 命名空间中实例化 _DEP 对象，以指示 Device 1 依赖于 CXL USP。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-12-6"></a>
### 9.12.6 Mapping of Link and Protocol Registers in CXL VH | CXL VH 中链路与协议寄存器的映射

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>In the presence of an eRCD, the link and protocol registers appear in MMIO space (RCRB and Component registers in the Downstream Port and the Upstream Port). See Figure 9-7 and Figure 9-8.</td><td style="background-color:#e8e8e8">在存在 eRCD 的情况下，链路和协议寄存器出现在 MMIO 空间中 (Downstream Port 和 Upstream Port 中的 RCRB 和 Component 寄存器)。见图 9-7 和图 9-8。</td></tr>
<tr><td>Because a CXL Virtual Hierarchy appears as a true PCIe hierarchy, the Component Register block is mapped using a standard BAR of CXL components.</td><td style="background-color:#e8e8e8">由于 CXL Virtual Hierarchy 显示为真正的 PCIe Hierarchy，Component Register Block 使用 CXL 组件的标准 BAR 进行映射。</td></tr>
<tr><td>Each CXL Host Bridge that is not an RCH includes CHBCR, which includes the registers that are common to all Root Ports under that Host Bridge. In an ACPI-compliant system, the base address of this register block is discovered via ACPI CEDT or the _CBR method. The CHBCR includes the HDM Decoder registers.</td><td style="background-color:#e8e8e8">每个非 RCH 的 CXL Host Bridge 包含 CHBCR，其中包括该 Host Bridge 下所有 Root Port 共有的寄存器。在符合 ACPI 的系统中，此寄存器块的基址通过 ACPI CEDT 或 _CBR 方法发现。CHBCR 包括 HDM Decoder 寄存器。</td></tr>
<tr><td>Each CXL Root Port carries a single BAR that maps the associated Component Register block. The offset within that BAR is discovered via the CXL DVSEC ID 8 (see Section 8.1.9).</td><td style="background-color:#e8e8e8">每个 CXL Root Port 携带一个映射关联 Component Register Block 的单个 BAR。该 BAR 内的偏移通过 CXL DVSEC ID 8 发现 (见第 8.1.9 节)。</td></tr>
<tr><td>Each CXL device that is not an RCD can map its Component Register Block to any of its 6 BARs and a 64-KB-aligned offset within that BAR. The BAR number and the offset are discovered via CXL DVSEC ID 8. A Type 3 device Component Register Block includes HDM Decoder registers.</td><td style="background-color:#e8e8e8">每个非 RCD 的 CXL 设备可将其 Component Register Block 映射到其 6 个 BAR 中的任意一个以及该 BAR 内的 64 KB 对齐偏移。BAR 编号和偏移通过 CXL DVSEC ID 8 发现。Type 3 设备的 Component Register Block 包括 HDM Decoder 寄存器。</td></tr>
<tr><td>Each CXL USP carries a single BAR that maps the associated Component Register block. The offset within that BAR is discovered via CXL DVSEC ID 8. The Upstream Switch Port Component Register Block contains the registers that are not associated with a particular Downstream Port, such as HDM Decoder registers.</td><td style="background-color:#e8e8e8">每个 CXL USP 携带一个映射关联 Component Register Block 的单个 BAR。该 BAR 内的偏移通过 CXL DVSEC ID 8 发现。Upstream Switch Port Component Register Block 包含不与特定 Downstream Port 关联的寄存器，如 HDM Decoder 寄存器。</td></tr>
<tr><td>Each CXL DSP carries a single BAR that points to the associated CHBCR, the format of which closely mirrors that of a Root Port. The offset within that BAR is discovered via CXL DVSEC ID 8.</td><td style="background-color:#e8e8e8">每个 CXL DSP 携带一个指向关联 CHBCR 的单个 BAR，其格式与 Root Port 的格式非常相似。该 BAR 内的偏移通过 CXL DVSEC ID 8 发现。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13"></a>
## 9.13 Software View of HDM | HDM 的软件视图

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>HDM is exposed to the OS/VMM as normal memory. However, HDM likely has different performance/latency attributes compared to host-attached memory. Therefore, a system with CXL.mem devices can be considered as a heterogeneous memory system. ACPI HMAT was introduced for such systems and can report memory latency and bandwidth characteristics associated with different memory ranges. ACPI Specification version 6.2 and later carry the definition of revision 1 of HMAT. As of August 2018, ACPI WG has decided to deprecate revision 1 of HMAT because it had a number of shortcomings. As a result, the subsequent discussion refers to revision 2 of HMAT.</td><td style="background-color:#e8e8e8">HDM 作为普通内存暴露给 OS/VMM。然而，与主机连接的内存相比，HDM 可能具有不同的性能/延迟属性。因此，具有 CXL.mem 设备的系统可被视为异构内存系统 (Heterogeneous Memory System)。ACPI HMAT 是为此类系统引入的，可以报告与不同内存范围关联的内存延迟和带宽特性。ACPI 规范 6.2 版及更高版本包含了 HMAT Revision 1 的定义。截至 2018 年 8 月，ACPI WG 已决定弃用 HMAT Revision 1，因为它有许多缺点。因此，后续讨论均指 HMAT Revision 2。</td></tr>
<tr><td>ACPI has introduced a new type of Affinity structure called Generic Affinity (GI) Structure. GI structure is useful for describing execution engines such as accelerators that are not processors. CXL.mem-capable accelerators will result in two SRAT entries - One GI entry to represent the accelerator cores and one memory entry to represent the attached HDM. GI entry is especially useful when describing the CXL.cache accelerator. Previous to the introduction of GI, the CXL.cache accelerator could not be described as a separate entity in SRAT/HMAT and had to be combined with the attached CPU.</td><td style="background-color:#e8e8e8">ACPI 引入了一种新型 Affinity 结构，称为 Generic Affinity (GI) Structure。GI 结构对于描述非处理器的执行引擎 (如加速器) 非常有用。支持 CXL.mem 的加速器将产生两个 SRAT 条目——一个 GI 条目代表加速器核心，一个内存条目代表连接的 HDM。GI 条目在描述 CXL.cache 加速器时特别有用。在引入 GI 之前，CXL.cache 加速器无法在 SRAT/HMAT 中作为独立实体描述，必须与连接的 CPU 合并。</td></tr>
<tr><td>With this specification change, the CXL.cache accelerator can be described as a separate proximity domain. _PXM method can be used to identify the proximity domain associated with the PCIe device. Since Legacy OSs do not understand GI, System Firmware is required to return the processor domain that is most closely associated with the I/O device when running such an OS. ASL code can use bit 17 of Platform-Wide _OSC Capabilities DWORD 2 to detect whether the OS supports GI.</td><td style="background-color:#e8e8e8">通过此规范变更，CXL.cache 加速器可被描述为独立的 Proximity Domain。_PXM 方法可用于识别与 PCIe 设备关联的 Proximity Domain。由于 Legacy OS 不理解 GI，系统固件在运行此类 OS 时需要返回与 I/O 设备关联最密切的 Processor Domain。ASL 代码可使用 Platform-Wide _OSC Capabilities DWORD 2 的 bit 17 来检测 OS 是否支持 GI。</td></tr>
<tr><td>System Firmware must construct and report SRAT and HMAT to the OS in systems with CXL.cache devices and CXL.mem devices. Since System Firmware is not aware of HDM properties, that information must come from the CXL device in the form of CDAT. A device may export CDAT via Table Access DOE or via a UEFI driver.</td><td style="background-color:#e8e8e8">系统固件必须在具有 CXL.cache 设备和 CXL.mem 设备的系统中构建并向 OS 报告 SRAT 和 HMAT。由于系统固件不了解 HDM 属性，这些信息必须以 CDAT 的形式来自 CXL 设备。设备可通过 Table Access DOE 或 UEFI 驱动程序导出 CDAT。</td></tr>
<tr><td>System Firmware combines the information that it has about the host and CXL connectivity with CDAT content obtained from various CXL components during construction of SRAT and HMAT.</td><td style="background-color:#e8e8e8">系统固件在构建 SRAT 和 HMAT 时，将其拥有的关于主机和 CXL 连接的信息与从各种 CXL 组件获取的 CDAT 内容相结合。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-1"></a>
### 9.13.1 Memory Interleaving | 内存交织

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Memory interleaving allows consecutive memory addresses to be mapped to different CXL devices at a uniform interval. eRCDs may support a limited form of interleaving as described in Section 9.11.7.1, whereby memory is interleaved across the two links between a CPU and a dual-headed device.</td><td style="background-color:#e8e8e8">内存交织 (Memory Interleaving) 允许连续的内存地址以均匀间隔映射到不同的 CXL 设备。eRCD 可支持第 9.11.7.1 节所述的一种有限形式的交织，其中内存跨 CPU 与 Dual-Headed 设备之间的两条链路进行交织。</td></tr>
<tr><td>The CXL 2.0 specification introduced a mechanism for interleaving across different devices. The set of devices that are interleaved together is known as the Interleave Set.</td><td style="background-color:#e8e8e8">CXL 2.0 规范引入了一种跨不同设备交织的机制。交织在一起的一组设备称为 Interleave Set (交织集)。</td></tr>
<tr><td>An Interleave Set is identified by the following:<br>• Base HPA - Multiple of 256 MB<br>• Size - Also a Multiple of 256 MB<br>• Interleave Way<br>• Interleave Granularity<br>• Targets (applicable only to Root Ports and Upstream Switch Ports)</td><td style="background-color:#e8e8e8">一个 Interleave Set 由以下标识：<br>• Base HPA - 256 MB 的倍数<br>• Size - 也是 256 MB 的倍数<br>• Interleave Way<br>• Interleave Granularity<br>• Targets (仅适用于 Root Port 和 Upstream Switch Port)</td></tr>
<tr><td>Interleave Way: A CXL Interleave Set may contain either 1, 2, 3, 4, 6, 8, 12, or 16 CXL devices. 1-way Interleave is equivalent to no interleaving. The number of devices in an Interleave set is known as Interleave Ways (IW).</td><td style="background-color:#e8e8e8">Interleave Way: CXL Interleave Set 可包含 1、2、3、4、6、8、12 或 16 个 CXL 设备。1-way Interleave 等同于无交织。Interleave Set 中的设备数量称为 Interleave Ways (IW)。</td></tr>
<tr><td>Interleave Granularity: Each device in an Interleave Set decodes a specific number of consecutive bytes, called Chunk, in HPA Space. The size of Chunk is known as Interleave Granularity (IG). The starting address of each Chunk is a multiple of IG.<br>• CXL Host Bridges (except RCH) and CXL switches must support the following IG values: 256B, 512B, 1024B, 2048B, 4096B, 8192B, 16384B (interleaving on HPA[8] through HPA[14] respectively).<br>• CXL memory devices must support at least one of the two IG groups: Group 1 (interleaving on HPA[8] through HPA[11]) or Group 2 (interleaving on HPA[12] through HPA[14]).</td><td style="background-color:#e8e8e8">Interleave Granularity: Interleave Set 中的每个设备在 HPA 空间中解码特定数量的连续字节，称为 Chunk。Chunk 的大小称为 Interleave Granularity (IG)。每个 Chunk 的起始地址是 IG 的倍数。<br>• CXL Host Bridge (RCH 除外) 和 CXL 交换机必须支持以下 IG 值：256B、512B、1024B、2048B、4096B、8192B、16384B (分别对应在 HPA[8] 至 HPA[14] 上的交织)。<br>• CXL 内存设备必须至少支持两组 IG 中的一组：Group 1 (在 HPA[8] 至 HPA[11] 上的交织) 或 Group 2 (在 HPA[12] 至 HPA[14] 上的交织)。</td></tr>
<tr><td>Target: The HDM Decoders in the CXL Host Bridge are responsible for looking up the incoming HPA in a CXL.mem transaction and forwarding the HPA to the appropriate Root Port Target. The HDM Decoders in the CXL Upstream Switch Port are responsible for looking up the incoming HPA in a CXL.mem transaction and forwarding the HPA to the appropriate Downstream Switch Port Target.</td><td style="background-color:#e8e8e8">Target: CXL Host Bridge 中的 HDM Decoder 负责在 CXL.mem 事务中查找传入的 HPA 并将 HPA 转发到适当的 Root Port Target。CXL Upstream Switch Port 中的 HDM Decoder 负责在 CXL.mem 事务中查找传入的 HPA 并将 HPA 转发到适当的 Downstream Switch Port Target。</td></tr>
<tr><td>An HDM Decoder in a device is responsible for converting HPA into DPA by stripping off specific address bits. These flows are described in Section 8.2.4.20.13.</td><td style="background-color:#e8e8e8">设备中的 HDM Decoder 负责通过剥离特定地址位将 HPA 转换为 DPA。这些流程见第 8.2.4.20.13 节。</td></tr>
<tr><td>An Interleave Set is established by programing an HDM Decoder and committing it (see Section 8.2.4.20.12). HDM Decoders within a component must be configured in a congruent manner and the Decoder Commit flow performs certain self-consistency checks to assist with correct programming. Software is responsible for ensuring that HDM Decoders located inside the components along the path of a transaction must be configured in a consistent manner.</td><td style="background-color:#e8e8e8">通过编程 HDM Decoder 并提交 (Commit) 来建立 Interleave Set (见第 8.2.4.20.12 节)。组件内的 HDM Decoder 必须以一致的方式配置，Decoder Commit 流程会执行某些自一致性检查以帮助正确编程。软件负责确保沿事务路径的组件内部的 HDM Decoder 必须以一致的方式配置。</td></tr>
<tr><td>Multiple-level interleaving is supported as long as all the levels use different, but consecutive, HPA bits to select the target and no Interleave Set has more than 8 devices. This is illustrated in Figure 9-17 and Figure 9-18.</td><td style="background-color:#e8e8e8">只要所有层级使用不同但连续的 HPA 位来选择 Target，并且没有 Interleave Set 具有超过 8 个设备，就支持多层交织 (Multiple-level Interleaving)。这如图 9-17 和图 9-18 所示。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-1-1"></a>
#### 9.13.1.1 Legal Interleaving Configurations: 12-way, 6-way, and 3-way | 合法交织配置：12 路、6 路与 3 路

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>This section describes the legal 12-way, 6-way, and 3-way interleaving configurations. The term IGB represents the interleave granularity in number of bytes. The cross-host Bridge Interleaving logic selects the target Host Bridge according to the configurations specified in Table 9-6, Table 9-7, and Table 9-8, respectively. The Root Complex and the switch select the target port as described in Section 9.18.1.</td><td style="background-color:#e8e8e8">本节描述了合法的 12 路、6 路和 3 路交织配置。术语 IGB 表示以字节数表示的 Interleave Granularity。Cross-Host Bridge 交织逻辑分别根据表 9-6、表 9-7 和表 9-8 中指定的配置选择 Target Host Bridge。Root Complex 和交换机按照第 9.18.1 节的描述选择 Target Port。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-2"></a>
### 9.13.2 CXL Memory Device Label Storage Area | CXL 内存设备标签存储区

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>CXL memory devices that provide volatile memory, such as DRAM, may be exposed with different interleave geometries each time the system is booted. This can happen due to the addition or removal of other devices or changes to the platform's default interleave policies. For volatile memory, these changes to the interleave usually do not impact host software since there's generally no expectation that volatile memory contents are preserved across reboots. However, with persistent memory, the exact preservation of the interleave geometry is critical so that the persistent memory contents are presented to host software the same way each time the system is booted.</td><td style="background-color:#e8e8e8">提供 Volatile Memory (如 DRAM) 的 CXL 内存设备可能在每次系统引导时以不同的交织几何 (Interleave Geometry) 暴露。这可能由于添加或移除其他设备或平台默认交织策略的更改而发生。对于 Volatile Memory，这些交织的更改通常不会影响主机软件，因为通常不期望 Volatile Memory 内容在重启后保留。然而，对于 Persistent Memory，精确保留交织几何至关重要，以便每次系统引导时 Persistent Memory 内容以相同方式呈现给主机软件。</td></tr>
<tr><td>Similar to the interleaving configuration, persistent memory devices may be partitioned into namespaces, which define volumes of persistent memory. These namespaces must also be reassembled the same way each time the system is booted to prevent data loss.</td><td style="background-color:#e8e8e8">与交织配置类似，Persistent Memory 设备可被分区为 Namespace，Namespace 定义了 Persistent Memory 的卷 (Volume)。这些 Namespace 也必须在每次系统引导时以相同方式重新组装，以防止数据丢失。</td></tr>
<tr><td>Section 8.2.10 defines mailbox operations for reading and writing the Label Storage Area (LSA) on CXL memory devices: Get LSA and Set LSA. In addition, the Identify Memory Device mailbox command exposes the size of the LSA for a given CXL memory device. The LSA allows both interleave and namespace configuration details to be stored persistently on all the devices involved, so that the configuration data "follows the device" if the device is moved to a different socket or machine. The use of an LSA is analogous to how disk RAID arrays write configuration information to a reserved area of each disk in the array so that the geometry is preserved across configuration changes.</td><td style="background-color:#e8e8e8">第 8.2.10 节定义了在 CXL 内存设备上读写 Label Storage Area (LSA) 的 Mailbox 操作：Get LSA 和 Set LSA。此外，Identify Memory Device Mailbox 命令暴露了给定 CXL 内存设备的 LSA 大小。LSA 允许交织和 Namespace 配置细节持久存储在涉及的各个设备上，使得配置数据在设备被移动到不同插槽或机器时"跟随设备"。LSA 的使用类似于磁盘 RAID 阵列将配置信息写入阵列中每个磁盘的保留区域，以便在配置更改时保持几何结构不变。</td></tr>
<tr><td>The LSA format and the rules for updating and interpreting the LSA are specified in this section. CXL memory devices do not directly interpret the LSA, they just provide the storage area and mailbox commands for accessing it. Software configuring Interleave Sets and namespaces, such as pre-boot firmware or host operating systems shall follow the LSA rules specified here to correctly inter-operate with CXL-compliant memory devices.</td><td style="background-color:#e8e8e8">LSA 的格式以及更新和解释 LSA 的规则在本节中规定。CXL 内存设备不直接解释 LSA，它们仅提供存储区和用于访问它的 Mailbox 命令。配置 Interleave Set 和 Namespace 的软件 (如 Pre-Boot Firmware 或主机操作系统) 应遵循此处规定的 LSA 规则，以便与符合 CXL 规范的内存设备正确互操作。</td></tr>
</tbody>
</table>

<a id="sec-9-13-2-1"></a>
#### 9.13.2.1 Overall LSA Layout | LSA 总体布局

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>The LSA consists of two Label Index Blocks followed by an array of label slots. As shown in Figure 9-19, the Label Index Blocks are always a multiple of 256 bytes in size, and each label slot is exactly 256 bytes in size.</td><td style="background-color:#e8e8e8">LSA 由两个 Label Index Block 及其后的一个 Label Slot 数组组成。如图 9-19 所示，Label Index Block 的大小始终是 256 字节的倍数，每个 Label Slot 的大小恰好为 256 字节。</td></tr>
<tr><td>The LSA size is implementation dependent and software must discover the size using the Identify Memory Device mailbox command. The minimum allowed size is two index blocks, 256-bytes each in length, two label slots (providing space for a minimal one region label and one namespace label), and one free slot to allow for updates. This makes the total minimum LSA size 1280 bytes. It is recommended (but not required) that a device provides for configuration flexibility by implementing an LSA large enough for two region labels per device and one namespace label per 8 GB of persistent memory capacity available on the device.</td><td style="background-color:#e8e8e8">LSA 大小取决于实现，软件必须使用 Identify Memory Device Mailbox 命令发现大小。最小允许大小是两个 Index Block (每个 256 字节)、两个 Label Slot (提供最小一个 Region Label 和一个 Namespace Label 的空间) 和一个 Free Slot 以允许更新。这使得总的最小 LSA 大小为 1280 字节。建议 (但不要求) 设备通过实现足够大的 LSA 来提供配置灵活性，每个设备两个 Region Label 和设备上每 8 GB Persistent Memory 容量一个 Namespace Label。</td></tr>
<tr><td>All updates to the LSA shall follow the update rules laid out in this section, which guarantee that the LSA remains consistent in the face of interruptions such as power loss or software crashes. There are no atomicity requirements on the Set LSA mailbox operation - it simply updates the range of bytes provided by the caller. Atomicity and consistency of the LSA is achieved using checksums and the principle that only free slots (currently unused) are written to - in-use data structures are never written, avoiding the situation where an interrupted update to an in-use data structure makes it inconsistent. Instead, all updates are made by writing to a free slot and then following the rules laid out in this section to atomically swap the in-use data structure with the newly written copy.</td><td style="background-color:#e8e8e8">所有对 LSA 的更新应遵循本节规定的更新规则，这些规则保证 LSA 在面对断电或软件崩溃等中断时保持一致性。Set LSA Mailbox 操作没有原子性要求——它仅更新调用方提供的字节范围。LSA 的原子性和一致性通过校验和以及仅写入 Free Slot (当前未使用的) 的原则来实现——从不写入正在使用的数据结构，从而避免了中断导致正在使用的数据结构不一致的情况。相反，所有更新都通过写入 Free Slot 然后遵循本节规定的规则，以原子方式将正在使用的数据结构与新写入的副本进行交换。</td></tr>
<tr><td>The LSA layout uses Fletcher64 checksums. When performing a checksum on a structure, any multi-byte integer fields shall be in little-endian byte order. If the structure contains its own checksum, as is commonly the case, that field shall contain 0 when this checksum routine is called. The algorithm for updating the LSA is single-threaded. Software is responsible for protecting a device's LSA so that only a single thread is updating the LSA at any time.</td><td style="background-color:#e8e8e8">LSA 布局使用 Fletcher64 校验和。在对结构执行校验和时，任何多字节整数字段应使用 Little-Endian 字节顺序。如果结构包含其自身的校验和字段 (通常情况下如此)，则在校验和例程被调用时该字段应包含 0。更新 LSA 的算法是单线程的。软件负责保护设备的 LSA，使得在任何时候只有一个线程在更新 LSA。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-2-2"></a>
#### 9.13.2.2 Label Index Blocks | 标签索引块

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Table 9-9 shows the layout of a Label Index Block.</td><td style="background-color:#e8e8e8">表 9-9 显示了 Label Index Block 的布局。</td></tr>
<tr><td>When reading Label Index Blocks, software shall consider index blocks to be valid only when their Sig, MyOff, OtherOff, and Checksum fields are correct. In addition, any blocks with Seq cleared to 0 are discarded as invalid. Finally, if more than 1 Label Index Block is found to be valid, the one with the older sequence number (immediately counterclockwise to the other, according to Figure 9-21) is discarded. If all checks pass and the sequence numbers match, the index block at the higher offset shall be considered the valid block. If no valid Label Index Blocks are found, the entire LSA is considered uninitialized.</td><td style="background-color:#e8e8e8">当读取 Label Index Block 时，软件应仅在 Sig、MyOff、OtherOff 和 Checksum 字段正确时才认为 Index Block 有效。此外，任何 Seq 被清零为 0 的 Block 应被视为无效而丢弃。最后，如果发现超过 1 个 Label Index Block 有效，则具有较旧序列号的那个 (根据图 9-21，紧邻另一个逆时针方向的) 被丢弃。如果所有检查通过且序列号匹配，则处于更高偏移处的 Index Block 应被视为有效 Block。如果没有找到有效的 Label Index Block，则整个 LSA 被视为未初始化 (Uninitialized)。</td></tr>
<tr><td>When updating the Label Index Block, the current valid block, according to the rules above, is never directly written to. Instead, the alternate block is updated with the appropriate fields and a sequence number that is immediately clockwise as shown in Figure 9-21. It is the appearance of a new block that passes all the checks and has a higher sequence number that makes this update atomic in the face of interruption.</td><td style="background-color:#e8e8e8">当更新 Label Index Block 时，根据上述规则，从不直接写入当前有效的 Block。相反，使用适当的字段和一个紧接顺时针方向的序列号 (如图 9-21 所示) 更新 Alternate Block。正是通过所有检查并具有更高序列号的新 Block 的出现，使得此更新在面临中断时成为原子操作。</td></tr>
<tr><td>Using this method of atomic update, software can allocate and deallocate label slots, even multiple slots, in a single, atomic operation. This is done by setting the Free bits to indicate which slots are free and which are in-use, and then updating the Label Index Block atomically as described above. To ensure that it is always possible to update a label atomically, there must always be at least one free label slot. That way, any used label slots can be updated by writing the new contents to the free slot and using the Label Index Block update algorithm to mark the new version as in-use and the old version as free in one atomic operation. For this reason, software must report a "label storage area full" error when a caller tries to use the last label slot.</td><td style="background-color:#e8e8e8">使用这种原子更新方法，软件可以在单个原子操作中分配和释放 Label Slot，甚至是多个 Slot。这通过设置 Free 位来指示哪些 Slot 是 Free 的以及哪些是 In-use 的，然后如上所述原子地更新 Label Index Block 来完成。为确保始终可以原子地更新标签，必须始终至少有一个 Free Label Slot。这样，任何正在使用的 Label Slot 都可以通过将新内容写入 Free Slot，并使用 Label Index Block 更新算法在一次原子操作中将新版本标记为 In-use 而将旧版本标记为 Free 来更新。因此，当调用方尝试使用最后一个 Label Slot 时，软件必须报告 "Label Storage Area Full" 错误。</td></tr>
<tr><td>The Free field contains an array of NSlot bits, indicating which label slots are currently free. The Label Index Block is then padded with 0 bits until the total size is a multiple of 256 bytes. This means that up to 1472 label slots are supported by Label Index Blocks that are 256 bytes in length. For 1473 to 3520 label slots, the Label Index Block size must be 512 bytes in length, and so on.</td><td style="background-color:#e8e8e8">Free 字段包含一个 NSlot 位的数组，指示哪些 Label Slot 当前是 Free 的。Label Index Block 然后用 0 位填充，直到总大小是 256 字节的倍数。这意味着长度为 256 字节的 Label Index Block 最多支持 1472 个 Label Slot。对于 1473 到 3520 个 Label Slot，Label Index Block 大小必须为 512 字节，依此类推。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-2-3"></a>
#### 9.13.2.3 Common Label Properties | 标签通用属性

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Three types of labels may occupy the label slots in the LSA: Region Labels, Namespace Labels, and Vendor Specific Labels. The first two are identified by type fields containing UUIDs as specified in the following sections. Vendor Specific Labels contain a type UUID determined by the vendor per IETF RFC 4122. Software shall ignore any labels with unknown types. In this way, the Type field in the labels provides a major version number, where software can assume that a UUID that it expects to find indicates a label that it understands, since only backward-compatible changes are allowed to the label layout from the point where that UUID first appears in a published CXL specification.</td><td style="background-color:#e8e8e8">LSA 中的 Label Slot 可以容纳三种类型的标签：Region Label、Namespace Label 和 Vendor Specific Label。前两种通过包含 UUID 的 Type 字段来识别，如后续章节所述。Vendor Specific Label 包含由供应商根据 IETF RFC 4122 确定的 Type UUID。软件应忽略任何具有未知类型的标签。通过这种方式，标签中的 Type 字段提供主版本号，软件可以假定它期望找到的 UUID 指示了它理解的标签，因为从该 UUID 首次出现在已发布的 CXL 规范中起，只允许对标签布局进行向后兼容的更改。</td></tr>
<tr><td>Region Labels and Namespace Labels contain a 4-byte Flags field, used to indicate the existence of new features. Since those features must be backward compatible, software may ignore unexpected flags encountered in this field (no error generated). Software should always write 0s for Flags bits that were not defined at the time of implementation. In this way, the Flags field provide a minor version number for the label.</td><td style="background-color:#e8e8e8">Region Label 和 Namespace Label 包含一个 4 字节的 Flags 字段，用于指示新功能的存在。由于这些功能必须向后兼容，软件可以忽略在此字段中遇到的意外 Flags (不生成错误)。软件应始终为在实现时未定义的 Flags 位写入 0。通过这种方式，Flags 字段为标签提供了次版本号。</td></tr>
<tr><td>It is sometimes necessary to update labels atomically across multiple CXL devices. For example, when a Region or Namespace is being defined, the labels are written to every device that contributes to it. Region Labels and Namespace Labels define a flag, UPDATING, that indicates a multi-device update is in-progress. Software shall follow this flow when creating or updating a set of labels across devices:<br>1. Write each label across all devices with the UPDATING flag set.<br>2. Update each label, using the update algorithm described in the previous section, clearing the UPDATING flag.</td><td style="background-color:#e8e8e8">有时需要跨多个 CXL 设备原子地更新标签。例如，当定义 Region 或 Namespace 时，标签被写入对其做出贡献的每个设备。Region Label 和 Namespace Label 定义了一个标志 UPDATING，指示多设备更新正在进行中。软件在跨设备创建或更新一组标签时应遵循以下流程：<br>1. 在所有设备上写入每个标签，并设置 UPDATING 标志。<br>2. 使用前一节描述的更新算法更新每个标签，清除 UPDATING 标志。</td></tr>
<tr><td>Any time software encounters a set of labels with any UPDATING flags, it shall execute these rules:<br>• If there are missing labels (some components with the expected UUID are missing), then the entire set of labels is rolled-back due to the update operation being interrupted before all labels are written. The roll-back means marking each label in the set as free, following the update algorithm described in the previous section.<br>• If there are no missing labels, then the entire set of labels is rolled-forward, completing the interrupted update operation by removing the UPDATING flag from all labels in the set, following the update algorithm described in the previous section.</td><td style="background-color:#e8e8e8">任何时候软件遇到一组带有任何 UPDATING 标志的标签时，应执行以下规则：<br>• 如果存在缺失的标签 (缺少某些具有预期 UUID 的组件)，则由于更新操作在所有标签写入之前被中断，整个标签集被回滚 (Roll-Back)。回滚意味着按照前一节描述的更新算法将集合中的每个标签标记为 Free。<br>• 如果没有缺失的标签，则整个标签集被前滚 (Roll-Forward)，通过按照前一节描述的更新算法从集合中的所有标签移除 UPDATING 标志来完成中断的更新操作。</td></tr>
<tr><td>When sets of Region Labels or Namespace Labels are found to have missing components, software shall consider them invalid and not attempt to configure the regions or surface the namespaces with these errors.</td><td style="background-color:#e8e8e8">当发现 Region Label 或 Namespace Label 集缺少组件时，软件应认为它们无效，并不应尝试配置这些 Region 或呈现具有这些错误的 Namespace。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-2-4"></a>
#### 9.13.2.4 Region Labels | 区域标签

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Region labels describe the geometry of a persistent memory Interleave Set (the term "region" is synonymous with "Interleave Set" in this section). Once software has configured a functional Interleave Set for a set of CXL memory devices, region labels are added to the LSA for each device that contributes capacity to it. Table 9-10 shows the layout of a Region Label.</td><td style="background-color:#e8e8e8">Region Label 描述了 Persistent Memory Interleave Set 的几何结构 (本节中术语 "Region" 与 "Interleave Set" 同义)。一旦软件为一组 CXL 内存设备配置了功能性 Interleave Set，就会为对其贡献容量的每个设备在 LSA 中添加 Region Label。表 9-10 显示了 Region Label 的布局。</td></tr>
<tr><td>The Region Label includes: Type UUID, UUID of this region per RFC 4122, Flags (including UPDATING=0000 0008h), NLabel (total number of devices in this Interleave Set), Position (position of this device in the Interleave Set), DPA (the DPA where the region begins on this device), RawSize (capacity this device contributes in bytes), HPA (if nonzero, the region needs to be mapped at this HPA), Slot (slot index of this label in the LSA), Interleave Granularity (encoded values 0-6 for 256B-16384B), Alignment (desired region alignment in multiples of 256 MB), and a Fletcher64 Checksum.</td><td style="background-color:#e8e8e8">Region Label 包括：Type UUID、Region 的 UUID (按 RFC 4122)、Flags (包括 UPDATING=0000 0008h)、NLabel (此 Interleave Set 中的设备总数)、Position (此设备在 Interleave Set 中的位置)、DPA (此设备上 Region 起始的 DPA)、RawSize (此设备贡献的容量，以字节为单位)、HPA (如果非零，Region 需要映射到此 HPA)、Slot (此标签在 LSA 中的 Slot Index)、Interleave Granularity (编码值 0-6，对应 256B-16384B)、Alignment (期望的 Region 对齐，以 256 MB 的倍数表示) 以及 Fletcher64 校验和。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-2-5"></a>
#### 9.13.2.5 Namespace Labels | 命名空间标签

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Namespace labels describe partitions of persistent memory that are exposed as volumes to software, analogous to NVMe namespaces or SCSI logical unit numbers (LUNs). Exactly how an operating system uses these volumes is beyond the scope of this specification - namespaces may be exposed to applications directly, exposed via file systems, or used internally by the operating system. Table 9-11 shows the layout of a Namespace Label.</td><td style="background-color:#e8e8e8">Namespace Label 描述了 Persistent Memory 的分区，这些分区作为卷 (Volume) 暴露给软件，类似于 NVMe Namespace 或 SCSI 逻辑单元号 (LUN)。操作系统如何使用这些卷的具体方式不在本规范范围内——Namespace 可直接暴露给应用程序，通过文件系统暴露，或由操作系统内部使用。表 9-11 显示了 Namespace Label 的布局。</td></tr>
<tr><td>The Namespace Label includes: Type UUID (68bb2c0a-5a77-4937-9f85-3caf41a0f93c), UUID, Name (null-terminated UTF-8 friendly name), Flags (including UPDATING), NRange (number of discontiguous ranges contributed), Position, DPA, RawSize, Slot, Alignment, RegionUUID, AddressAbstractionUUID, LBASize (if nonzero, logical block size), and a Fletcher64 Checksum.</td><td style="background-color:#e8e8e8">Namespace Label 包括：Type UUID (68bb2c0a-5a77-4937-9f85-3caf41a0f93c)、UUID、Name (以 null 结尾的 UTF-8 友好名称)、Flags (包括 UPDATING)、NRange (贡献的非连续 Range 数量)、Position、DPA、RawSize、Slot、Alignment、RegionUUID、AddressAbstractionUUID、LBASize (如果非零，为逻辑块大小) 以及 Fletcher64 校验和。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-2-6"></a>
#### 9.13.2.6 Vendor-specific Labels | 厂商特定标签

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Table 9-12 shows the layout of a Vendor-specific Label. Other than the Type field and the Checksum field, the vendor is free to store anything in the remaining 232 (E8h) bytes of the label.</td><td style="background-color:#e8e8e8">表 9-12 显示了 Vendor-specific Label 的布局。除 Type 字段和 Checksum 字段外，供应商可在标签剩余 232 (E8h) 字节中自由存储任何内容。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)

<a id="sec-9-13-3"></a>
### 9.13.3 Dynamic Capacity Device (DCD) | 动态容量设备

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr><td>Dynamic Capacity is a feature of a CXL memory device that allows memory capacity to change dynamically without the need for resetting the device. A DCD is a CXL memory device that implements Dynamic Capacity. Unlike a traditional DPA range that a CXL memory device might support, a Dynamic Capacity DPA range is subdivided into 1 to 8 DC Regions, each of which is subdivided by the DCD into a number of fixed-size blocks, referred to as DC blocks. The host software is expected to program the maximum potential capacity utilizing one or more HDM decoders to span the entire DPA range of all configured regions. The DCD controls the allocation of these DC blocks to the host and utilizes events to signal the host when changes to the allocation of these DC blocks occurs. The DCD communicates the state of these DC blocks through an Extent List that describes the starting DPA and length of all DC blocks the host can access.</td><td style="background-color:#e8e8e8">动态容量 (Dynamic Capacity) 是 CXL 内存设备的一项功能，允许内存容量动态更改而无需复位设备。DCD 是实现 Dynamic Capacity 的 CXL 内存设备。与 CXL 内存设备可能支持的传统 DPA Range 不同，Dynamic Capacity DPA Range 被细分为 1 到 8 个 DC Region，每个 DC Region 由 DCD 进一步细分为多个固定大小的块，称为 DC Block。主机软件应编程最大潜在容量，利用一个或多个 HDM Decoder 覆盖所有已配置 Region 的整个 DPA Range。DCD 控制这些 DC Block 对主机的分配，并利用事件 (Event) 在这些 DC Block 的分配发生变化时通知主机。DCD 通过 Extent List (范围列表) 传达这些 DC Block 的状态，该列表描述主机可访问的所有 DC Block 的起始 DPA 和长度。</td></tr>
<tr><td>The Extent List does not contain extents that are still pending acceptance from the host via the Add Dynamic Capacity Response command (see Section 8.2.10.9.9.3). Similarly, the Extent List does contain extents that are still pending release acceptance from the host via the Release Dynamic Capacity command (see Section 8.2.10.9.9.4).</td><td style="background-color:#e8e8e8">Extent List 不包含尚待主机通过 Add Dynamic Capacity Response 命令接受 (见第 8.2.10.9.9.3 节) 的 Extent。类似地，Extent List 确实包含尚待主机通过 Release Dynamic Capacity 命令 (见第 8.2.10.9.9.4 节) 接受释放的 Extent。</td></tr>
<tr><td>Dynamic Capacity is organized into 1 to 8 DC Regions as defined by the device. Each DC Region has a unique maximum potential capacity, supported block size, and memory attributes. Regions are used in increasing-DPA order, with Region 0 being used for the lowest DPA of Dynamic Capacity and Region 7 for the highest DPA. The DCD controls which DPA range it assigns to each region for each host. The DPA ranges exposed by the device to each host are independent of one another.</td><td style="background-color:#e8e8e8">Dynamic Capacity 按照设备定义的组织为 1 到 8 个 DC Region。每个 DC Region 具有唯一的最大潜在容量、支持的 Block Size 和内存属性。Region 按递增 DPA 顺序使用，Region 0 用于 Dynamic Capacity 的最低 DPA，Region 7 用于最高 DPA。DCD 控制为每个主机的每个 Region 分配哪个 DPA Range。设备向每个主机暴露的 DPA Range 是相互独立的。</td></tr>
<tr><td>If the host issues a read to a DPA that is not allocated to the host, the device behavior is specified in Table 8-27. If the host issues a write to a DPA that is not allocated to the host, the device shall drop the write and send an NDR (see Section 3.3.9) as a response. If the host issues a write to any DPA in a read-only DC Region, the device shall drop the write and send an NDR as a response.</td><td style="background-color:#e8e8e8">如果主机对未分配给该主机的 DPA 发出读操作，设备行为在表 8-27 中规定。如果主机对未分配给该主机的 DPA 发出写操作，设备应丢弃该写操作并发送 NDR (见第 3.3.9 节) 作为响应。如果主机对只读 DC Region 中的任何 DPA 发出写操作，设备应丢弃该写操作并发送 NDR 作为响应。</td></tr>
<tr><td>The basic sequence to utilize Dynamic Capacity includes: retrieve CEL via Get Supported Logs to verify Dynamic Capacity commands are supported; issue Get Dynamic Capacity Configuration command to discover regions; program HDM decoders appropriately; retrieve the initial Extent List via Get Dynamic Capacity Extent List.</td><td style="background-color:#e8e8e8">使用 Dynamic Capacity 的基本序列包括：通过 Get Supported Logs 检索 CEL 以验证 Dynamic Capacity 命令受支持；发出 Get Dynamic Capacity Configuration 命令以发现 Region；适当地编程 HDM Decoder；通过 Get Dynamic Capacity Extent List 检索初始 Extent List。</td></tr>
<tr><td>For adding capacity: the DCD adds an Add Capacity Event Record to the Dynamic Capacity Event Log; the host retrieves the event and responds with Add Dynamic Capacity Response; the host may check for poisoned addresses via Get Poison List or Scan Media.</td><td style="background-color:#e8e8e8">添加容量：DCD 向 Dynamic Capacity Event Log 添加 Add Capacity Event Record；主机检索事件并以 Add Dynamic Capacity Response 响应；主机可通过 Get Poison List 或 Scan Media 检查 Poisoned Address。</td></tr>
<tr><td>For releasing capacity: the DCD adds a Release Capacity Event Record; the host releases some or all of the capacity and responds with Release Dynamic Capacity command. The host may also release capacity asynchronously without receiving an event. Devices may forcefully release capacity: host access to the released capacity may be immediately disabled, and a Forced Capacity Release Event Record is added. No Forced Capacity Release Event Record is created when capacity is released as a result of a reset.</td><td style="background-color:#e8e8e8">释放容量：DCD 添加 Release Capacity Event Record；主机释放部分或全部容量并以 Release Dynamic Capacity 命令响应。主机也可以在不接收事件的情况下异步释放容量。设备可强制释放容量：对已释放容量的主机访问可能被立即禁用，并添加 Forced Capacity Release Event Record。当容量因复位而被释放时，不创建 Forced Capacity Release Event Record。</td></tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章补充目录)


<a id="sec-9-13-3-3"></a>
#### 9.13.3.3 Extent List Tracking | Extent List Tracking

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The storage of extent list information, including individual extents and their associated tags, consumes resources in a DCD. As such, DCDs are permitted to limit the number of extents and number of tags of which they are capable of tracking. This capability is reported in a DCD’s Get Host DC Region Configuration and Get Dynamic Capacity Configuration responses. A DCD is responsible for tracking all extents and tags that comprise extent lists in the following states:

</td><td style="background-color:#e8e8e8">

extent 列表信息的存储，包括各个 extent 及其关联的元数据，跨 DC region 重新配置持久化。设备必须确保 extent 列表信息在 power cycle 和 CXL Reset 之间得以保留。主机软件负责在重新配置后重新发现 extent 列表的内容。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability • Pending: Defining capacity specified in an Initiate Dynamic Capacity Add request that has not been responded to by a host. This includes extents that form part of Dead Extent Groups, those that have been Force Removed whilst in pending state. • Added: Defining capacity that has been accepted by a host as part of an Add Dynamic Capacity request and is present in the extent list returned to the host in the response to a Get Dynamic Capacity Extent List request • FM-referenced: Defining capacity to which an FM reference has been added, as reported by the FM Holds Reference bit in the response to Dynamic Capacity List Tags A DCD reports its Number of Available Extents and Number of Available Tags as its total capacity minus all extents and tags tracked for capacity in the Pending, Added, and FM-referenced states, respectively.

</td><td style="background-color:#e8e8e8">

待定：定义与 CXL 规范未来版本预期一致的 capacity 和设备配置能力。实现者可选择提前支持这些定义，但应注意它们可能随着规范的未来发展而改变。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-13-4"></a>
#### 9.13.4 Capacity or Performance Degradation | Capacity or Performance Degradation

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

A CXL device may detect an unrecoverable error during its initialization and may be able to operate with a reduced capacity or reduced performance. If this failure results in capacity degradation and it is detected prior to Memory_Info_Valid=1, the device shall update the Memory_Size fields in the corresponding DVSEC CXL Range Size registers (see Section 8.1.3.8.1, Section 8.1.3.8.2, Section 8.1.3.8.5, and Section 8.1.3.8.6), CDAT DSMAS structures, response to Identify Memory Device command, and response to Get Partition Info command to report the reduced size. It is recommended that the device also set the Memory Capacity Degraded flag in the Health Status field (see Table 8-148). If the failure results in performance degradation and it is detected prior to Memory_Info_Valid=1, the CDAT DSLBIS structure shall be updated and the Performance Degraded flag in the Health Status field (see Table 8-148) should be set. If Mem_HwInit_Mode=1, Memory_Active bit(s) shall be set when the memory range is fully initialized and available for software use. If this failure is detected after the Memory_Info_Valid bit is set, but before the Memory_Active bit is set, the device shall not set the Memory_Active bit. The device updates the CDAT in the following manner: • CDAT sequence number shall be incremented to indicate to SW that CDAT content has changed. • If the failure results in capacity degradation, the CDAT DSEMTS entries shall mark the bad memory as “EFIUnusableMemory” indicating to the SW that it shall not use the associated DPA range on this device. The Memory Capacity Degraded flag in the Health Status field (see Table 8-148) shall be set. • If the failure results in performance degradation, the CDAT DSLBIS structure shall be updated and the Performance Degraded flag in the Health Status field (see Table 8-148) shall be set. If Mem_HwInit_Mode=1, Memory_Active_Degraded shall be set when the reduced capacity is fully initialized and available for software use. The device capacity reported by Identify Memory Device (see Section 8.2.10.9.1.1) and Get Partition Info (see Section 8.2.10.9.2.1) commands shall be consistent with capacity advertised by CDAT that is not marked as EFIUnusableMemory.

</td><td style="background-color:#e8e8e8">

CXL 设备在其初始化期间可能检测到不可恢复的错误，并可能通过 AER 或 CXL IDE 机制向主机发出信号。当检测到此类错误时，设备应将错误记录在适当的错误日志中，并将错误状态反映在相关的能力寄存器中。主机系统软件负责读取错误日志并采取适当的恢复或遏制措施。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14"></a>
### 9.14 Back-Invalidate Configuration | Back-Invalidate Configuration

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section describes how System Software may discover whether a component supports Back-Invalidate and how BI-IDs are assigned.

</td><td style="background-color:#e8e8e8">

本节描述了系统软件如何发现组件是否支持 Back-Invalidate。系统软件检查 CXL DVSEC 中相应的功能位，并通过配置空间枚举确定设备能力。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14-1"></a>
#### 9.14.1 Discovery | Discovery

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Back-Invalidate (BI) messages require the link to operate in 256B Flit mode. Alternate Protocol Negotiation flow establishes the optimal Flit mode and PCIe DVSEC for Flex Bus Port registers (see Section 8.2.1.3) identifies the negotiated Flit mode. The presence of the CXL BI Decoder Capability Structure indicates that the component is capable of supporting BI.

</td><td style="background-color:#e8e8e8">

发现过程从系统固件枚举 PCIe 配置空间并识别具有 CXL 能力的设备开始。固件读取 CXL DVSEC 以确定设备类型和支持的功能。根据发现的信息，固件可以设置适当的系统地址映射和设备配置。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14-2"></a>
#### 9.14.2 Configuration | Configuration

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Before enabling a device to issue BI requests, System Software must ensure that the device, the host, and any switch(es) in the path are capable of BI and that the link(s) between the device and the host are operating in 256B Flit mode. BI-capable Downstream Ports and devices advertise the CXL BI Decoder Capability Structure (see Section 8.2.4.27). System Software configures them to enable BI functionality. The BI-ID of a device must be unique within a VH. This is ensured by using the device’s Bus Number as the BI-ID. The Downstream Port decode functionality is described in Table 9-13 and Table 9-14. Table 9-13. Downstream Port Handling of BISnp BI Enable Value BI Forward Value Behavior Discard Forward upstream as is Perform the following checks: • Locate the HDM decoder in the USP or RC that decodes the BISnp address. • Verify that the BI bit in that HDM decoder is set. • Optionally, verify that the Target Port that corresponds to the BISnp address matches the port that generated the BISnp request. If this is a DSP: • If above checks pass, Set BI-ID= Secondary Bus Number and forward upstream; otherwise, discard. If this is a root port: • If above checks pass, forward upstream; otherwise, discard. Root port may use host proprietary mechanisms to initialize BI-ID and route the associated BIRsp messages. Discard (Invalid setting) Table 9-14. Downstream Port Handling of BIRsp BI Enable Value BI Forward Value Behavior Discard Forward downstream as is If this is a DSP: • If BI-ID=Secondary Bus Number, forward downstream; otherwise, discard. If this is a root port: • Use host-specific checks to ensure correct routing of the BISnp response. Forward downstream if these checks pass; otherwise, discard. Discard (Invalid setting)

</td><td style="background-color:#e8e8e8">

表 9-13 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability The USP in a BI-capable Switch may advertise the CXL BI Route Table capability Structure (see Section 8.2.4.26). If a USP receives an M2S BIRsp message, the USP shall look up the Port Number associated with the Bus Number that is carried in the message’s BI-ID field, and then forward the message to that Port. The BI-ID is guaranteed to correspond to a valid BI-capable device, specifically the one that generated the BISnp request. If the Port Number does not match any DSP due to incorrect programming, the BIRsp message shall be dropped. If a USP receives an S2M BISnp message, the USP may look up the Port Number associated with the Bus Number that is carried in the message’s BI-ID field, and then verify that the Port Number matches the Port Number of the originating DSP before forwarding the BISnp message upstream. If the Port Number derived from this structure does not match the DSP’s Port Number, the BISnp message may be dropped.

</td><td style="background-color:#e8e8e8">

支持 BI 的交换机中的 USP 可通过其能力寄存器通告 BI 支持。系统软件读取这些寄存器以确定交换机是否能够转发 BISnp 消息。启用 BI 后，USP 根据其路由表将收到的 BISnp 消息转发到适当的主机端口。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability IMPLEMENTATION NOTE System software may use the following sequence to configure a BI-capable Device D below a Switch S as follows: 1. Verify that all the CXL link(s) between Device D and the host are operating in 256B Flit mode. 2. Ensure the device has been assigned a valid Bus number. 3. Enable BI on the DSP of Switch S that is directly connected to Device D: a. BI Forward=0. b. BI Enable=1. 4. If the DSP’s BI Decoder Capability register indicates Explicit BI Decoder Commit Required=1, commit the BI-ID changes via the following sequence: a. BI Decoder Commit=0 to rearm. b. BI Decoder Commit=1. c. Poll bits 0 and 1 of the BI Decoder Status register until timeout or one of them is set. The timeout value is reported in the BI Decoder Status register. d. If BI Decoder Committed=1, the changes were committed. Proceed to step 5. e. If BI Decoder Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 5. If the USP implements CXL BI Route Table Capability Structure and Explicit BI RT Commit Required=1, commit the BI-ID changes as follows: a. BI RT Decoder Commit=0 to rearm. b. BI RT Decoder Commit=1. c. Poll bits 0 and 1 of the BI RT Status register until timeout or one of them is set. The timeout value is reported in the BI RT Status register. d. If BI RT Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If BI RT Committed=1, the changes were committed. Proceed to step 6. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 6. If the previous steps were successful, configure the Root Port that is directly connected to Switch S to forward BI messages if it isn’t already set up that way: a. If BI Forward=0, set BI Forward=1. b. Ensure BI Enable=0. 7. If the previous steps were successful, configure Device D to enable BI: a. BI Enable=1. 8. If the previous steps were successful, inform the device driver that Device D may now issue BI requests.

</td><td style="background-color:#e8e8e8">

实现注：Reset, Initialization, Configuration, and Manageability IMPLEMENTATION NOTE System software may use the following sequence to configure a BI-capable D

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14-3"></a>
#### 9.14.3 Mixed Configurations | Mixed Configurations

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section describes scenarios where a BI-capable device is plugged into a system that does not support BI. IMPLEMENTATION NOTE System software may use the following sequence to deallocate the BI-ID B that was previously assigned to Device D below Switch S as follows: 1. Notify Device D’s device driver that Device D is no longer allowed to issue BI requests and then wait for acknowledgment. 2. Configure Device D to disable BI: a. BI Enable=0. 3. Configure the DSP of Switch S that is directly connected to Device D to unassign BI-ID B as follows: a. BI Forward=0. b. BI Enable=0. 4. If the DSP’s CXL BI Decoder Capability register indicates Explicit BI Decoder Commit Required=1, commit the BI-ID changes as follows: a. BI Decoder Commit=0 to rearm. b. BI Decoder Commit=1. c. Poll bits 0 and 1 of the BI Decoder Status register until timeout or one of them is set. The timeout value is reported in the BI Decoder Status register. d. If BI Decoder Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If BI Decoder Committed=1, the changes were committed. Proceed to step 5. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 5. If the USP implements CXL BI Route Table Capability Structure and Explicit BI RT Commit Required=1, commit the BI-ID changes as follows: a. BI RT Commit=0 to rearm. b. BI RT Commit=1. c. Poll bits 0 and 1 of the BI RT Status register until timeout or one of them is set. The timeout value is reported in the BI RT Status register d. If BI RT Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If BI RT Committed=1, the changes were committed. Proceed to step 6. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 6. If the previous steps were successful, and no other devices in this VCS have been assigned a BI-ID, configure the Root Port that is directly connected to Switch S to stop forwarding BI messages as follows: a. BI Forward=0. Ensure BI Enable=0.

</td><td style="background-color:#e8e8e8">

实现注：Reset, Initialization, Configuration, and Manageability

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14-3-1"></a>
#### 9.14.3.1 BI-capable Type 2 Device | BI-capable Type 2 Device

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

If a BI-capable Type 2 device is connected to a Downstream Port that does not support 256B Flit mode, the device is able to detect this condition during the Hardware Autonomous Mode Negotiation (see Section 6.4.1.1) and fall back to another mode (e.g., Type 2 HDM-D mode or PCIe mode) based on the device vendor’s policy. If a BI-capable Type 2 device is connected to a switch that supports BI, but the host does not support BI, the device cannot be operated in BI mode. In this case, the System Software or the System Firmware may choose to reconfigure the Type 2 device to operate in a fallback mode. It is legal for BI-capable Type 2 devices to not support HDM-D flow; however, such a device must support fallback to either operate as a PCIe device, Type 1 device, or a Type 3 device. These flows are described in Section 9.14.3.2. If a Type 2 device advertises support for HDM-D flow via the BI Decoder Capability register (see Section 8.2.4.27.1), the device is operated in that mode as long as the number of Type 2 devices using HDM-D flow does not exceed the host’s capabilities and the CXL specification restrictions. A CXL Type 2 device that supports HDM-D flow may be unable to operate in that mode due to system configuration restrictions. In many scenarios, the device may be unable to make that determination on its own and may require assistance from System Software or System Firmware. See Section 9.14.3.2.

</td><td style="background-color:#e8e8e8">

支持 BI 的 Type 2 设备使用 CXL.cache 协议来维护与主机的缓存一致性。BISnp 消息从设备发送到主机，以失效主机缓存中可能已被设备修改的行。设备必须遵循第 3.3.8 节中定义的 BISnp 规则。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14-3-2"></a>
#### 9.14.3.2 Type 2 Device Fallback Modes | Type 2 Device Fallback Modes

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Table 9-15 describes the actions that System Software or System Firmware may take when a Type 2 device cannot be operated in either HDM-DB mode or in HDM-D mode, based on the Fallback Capability field value in the DVSEC CXL Capability2 register (see Section 8.1.3.7). Table 9-15. CXL Type 2 Device Behavior in Fallback Operation Mode Register Value1 Behavior 00b The device can be operated as an RCD. If the device does not support HDM-DB flow, it supports HDM-D flow. If the device supports HDM-DB flow, it also supports HDM-D flow and must return HDM-D Capable=1 (see Section 8.2.4.27.1). If the device cannot be operated as a Type 2 device, it must be disabled. 01b The device supports either HDM-DB flow or HDM-D flow or both. In addition, it can operate as a PCIe device. If the device cannot be operated in either HDM-DB mode or in HDM-D mode, System Firmware or System Software may disable Alternate Protocol Negotiation by programming the DSP registers and issuing a Secondary Bus Reset so that the link comes up in PCIe mode. 10b The device supports either HDM-DB flow or HDM-D flow or both. In addition, it can operate as a CXL Type 1 device. If the device cannot be operated in either HDM-DB mode or in HDM-D mode, System Firmware or System Software may reconfigure the DVSEC Flex Bus Port Control register (see Section 8.2.1.3.2) in the Downstream Port above the device to not advertise CXL.mem and then issue a Secondary Bus Reset, thereby bringing up the device as a CXL Type 1 device. 11b The device supports either HDM-DB flow or HDM-D flow or both. In addition, it can operate as a CXL Type 3 device. If the device cannot be operated in either HDM-DB mode or in HDM-D mode, System Firmware or System Software may reconfigure the Flex Bus Port Control register (see Section 8.2.1.3.2) in the Downstream Port above the device to not advertise CXL.cache and then issue a Secondary Bus Reset, thereby bringing up the device as a CXL Type 3 device. 1. Fallback Capability field values in the DVSEC CXL Capability2 register (see Section 8.1.3.7).

</td><td style="background-color:#e8e8e8">

表 9-15 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability More-complex policies, such as configuring the Device to operate in CXL.io only mode or another mode based on peer devices, are possible; however, those policies are beyond the scope of this specification.

</td><td style="background-color:#e8e8e8">

更复杂的策略（如配置交织组内的非均匀解码器布局）需要系统软件根据平台特定的知识进行管理。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-14-3-3"></a>
#### 9.14.3.3 BI-capable Type 3 Device | BI-capable Type 3 Device

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

A BI-capable Type 3 device is required to operate correctly when System Software has not enabled BI. In this case, the device functionality that is dependent on BI will not be available. If a BI-capable Type 3 device is connected to a Downstream Port that does not support 256B Flit mode, the device may continue to advertise BI capability via the CXL BI Decoder Capability Structure (see Section 8.2.4.27). The System Software shall ensure that the BI bit in none of the HDM decoders in the device, the switch, or the host that spans the device’s HDM is set. If a BI-capable Type 3 device is present in a system where the host does not support BI, the System Software shall ensure that the BI bit in none of the HDM decoders in the device, the switch, or the host that spans the device’s HDM is set. In both cases, the System Software is responsible for ensuring that the BI bit in the CXL BI Decoder Control register (see Section 8.2.4.27.2) in the device, as well as the Downstream Port it is connected to, is programmed to 0.

</td><td style="background-color:#e8e8e8">

支持 BI 的 Type 3 设备使用 HDM-DB 一致性模型。此类设备可以发起 BISnp 消息以失效主机缓存，但不需要实现完整的 CXL.cache 协议。设备通过 CXL.mem 协议暴露内存，并通过 BISnp 管理一致性。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-15"></a>
### 9.15 Cache ID Configuration and Routing | Cache ID Configuration and Routing

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CXL 3.0 specification introduces protocol enhancements that allow for more than one active CXL.cache agent per VCS. The identity of the CXL.cache agent is carried via the CacheID field in the CXL.cache messages. If the CXL link is operating in 256B Flit mode, the CXL.cache messages can carry 4 CacheID bits. Before enabling more than one CXL.cache device per VCS, Software must ensure that the host and any switch(es) in the path advertise the CXL Cache ID Decoder Capability Structure, and that all the link(s) between the lowest-level switch and the host are operating in 256B Flit mode. Downstream Ports advertise the CXL Cache ID Decoder Capability structure to indicate that the Downstream Ports can assign and decode the CacheID field in CXL.cache messages (see Section 8.2.4.29). Software configures the Downstream Ports to enable CacheID forwarding functionality and assign a CacheID to the device. The CacheID must be unique within a VH and must account for the constraints placed by the Flit mode and the host capabilities. Any CXL.cache device can operate correctly in a system that is capable of supporting more than one active CXL.cache agent per VCS; however, System Firmware or System Software that is aware of this new capability and capable of correctly configuring the switch and/or host is required to take advantage of this capability.

</td><td style="background-color:#e8e8e8">

Cache ID 用于在具有多个缓存代理的系统中标识特定的缓存实例。系统固件在枚举期间分配 Cache ID，并通过 ACPI 表（如 CEDT）将 Cache ID 映射信息传递给操作系统。Cache ID 在 CXL.cache 事务中用于路由和一致性管理。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-15-1"></a>
#### 9.15.1 Host Capabilities | Host Capabilities

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The host requires dedicated resources to track each CacheID source. As such, it is necessary to account for host constraints when assigning CacheID. The host constraints are expressed in terms of the total number of CacheIDs that the host can track per CXL Host Bridge. This information is conveyed via the Cache ID Target Count field in the CXL Cache ID Route Table Capability register (see Section 8.2.4.28.1) associated with the Host Bridge.

</td><td style="background-color:#e8e8e8">

主机通过 ACPI _OSC 方法声明其对 Cache ID 和其他 CXL 特性的支持。系统固件评估主机的声明并与平台能力进行比较，以确定最终的配置。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-15-2"></a>
#### 9.15.2 Downstream Port Decode Functionality | Downstream Port Decode Functionality

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Downstream Port decode functionality is described in Table 9-16 and Table 9-17. The associated registers are defined in Section 8.2.4.14.

</td><td style="background-color:#e8e8e8">

表 9-16 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability In addition to the checks documented in Table 9-16, the root port shall implement the following steps before forwarding the message upstream: • If HDM-D Type 2 Device Present=1, compare CacheID with the HDM-D Type 2 Device Cache ID field. If there is a match, identify this device as a Type 2 device that is using HDM-D flows. The host shall follow the HDM-D flows when responding to this device, which includes enforcing the setting in the CXL.cache Trust Level field of the Root Port Security Policy register (see Table 8-29). • If the Requester is using HDM-DB flows, abort the request if Block CXL.cache HDM- DB=1. D2H response messages and D2H data messages do not carry CacheID and are always routed back to the host.

</td><td style="background-color:#e8e8e8">

表 9-16 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-15-3"></a>
#### 9.15.3 Upstream Switch Port Routing Functionality | Upstream Switch Port Routing Functionality

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

When a USP receives a D2H request message from a DSP, the USP shall forward the message upstream. A USP may look up the Port Number associated with the CacheID field in the message from the CXL Cache ID Route Table and may compare that to the Port Number of the DSP that the message came from before forwarding the message. When a USP receives an H2D request message, H2D data message or an H2D response message, the USP shall use the message’s CacheID field to look up the corresponding CXL Cache ID Target N register (see Section 8.2.4.28.4). If the Valid bit in the Cache ID Target register is 0, the H2D message shall be discarded without a response. If the Valid bit is 1, the message shall be forwarded to the local DSP based on the Port Number field that is programmed in the CXL Cache ID Target N register. Table 9-16. Downstream Port Handling of D2H Request Messages Assign Cache ID Value Forward Cache ID Value Behavior Discard Forward upstream. If the message was received over a link operating in 68B Flit mode, the request is processed as if CacheID field is 0. Set CacheID=Local Cache ID and forward upstream. The link between the device and the Downstream Port may be operating in 68B Flit mode, in which case the D2H request message received by the Downstream Port does not contain the CacheID field. Discard (Invalid setting) Table 9-17. Downstream Port Handling of H2D Response Message and H2D Request Message Assign Cache ID Value Forward Cache ID Value Behavior Discard Forward downstream as is If CacheID=Local CacheID, forward downstream; otherwise, discard. The link between the device and the Downstream Port may be operating in 68B Flit mode, in which case the H2D message received by the device does not contain the CacheID field. The device shall ignore the CacheID field in H2D messages, if present. Discard (Invalid setting)

</td><td style="background-color:#e8e8e8">

表 9-16 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability D2H response messages and D2H data messages do not carry CacheID and are always routed back to the host. If a USP receives CXL.cache message over a link operating in 68B Flit mode, it shall process the request as if the CacheID field is 0. A switch that is not capable of decoding CacheID field must be configured such that no more than one DSP is enabled for CXL.cache traffic (indicated by Cache_Enable=1 in the DVSEC Flex Bus Port Status register; see Section 8.2.1.3.3). The USP shall direct all H2D traffic to that DSP.

</td><td style="background-color:#e8e8e8">

本节描述Reset, Initialization, Configuration, and Manageability D2H response messages an的相关规范要求。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-15-4"></a>
#### 9.15.4 Host Bridge Routing Functionality | Host Bridge Routing Functionality

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

When the Host Bridge receives the equivalent of an H2D request or an H2D response message from the host, the Host Bridge logic shall use the CacheID field to look up the corresponding CXL Cache ID Target N register (see Section 8.2.4.28.4). If the Valid bit is 0, the H2D message is discarded. If the Valid bit is 1, the message is forwarded to the local root port based on the Port Number field that is programmed in the CXL Cache ID Target N register. When the Host Bridge receives a D2H request message from the root port, the Host Bridge shall forward the message to the host, using host-specific mechanisms. The Host Bridge may optionally look up the root port that is associated with the CacheID and discard the message if the message was received from a different root port.

</td><td style="background-color:#e8e8e8">

D2H 响应消息和 D2H 数据消息从设备向上游转发至主机。交换机根据响应消息中的路由信息（包括 Requester ID 或地址信息）将消息沿正确路径路由回原始请求者。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability IMPLEMENTATION NOTE System Software may use the following sequence to allocate a Cache ID to a BI- capable CXL.cache Device D below a Switch S and enable the Device to generate CXL.cache transactions that target any memory: 1. Verify that the CXL link between Switch S and the host is operating in 256B Flit mode. 2. Identify an unused and legal CacheID value, c, and allocate it to Device D. Software must take into account the current Flit mode, as well as the Cache ID Target Count fields, while assigning Cache IDs to devices. 3. Configure the DSP of Switch S that is directly connected to Device D to assign Cache ID=c to Device D: a. Forward Cache ID=0. b. Local Cache ID=c. c. Assign Cache ID=1. 4. If the above DSP of Switch S reports Explicit Cache ID Decoder Commit Required=1, commit the Cache ID changes as follows: a. Cache ID Decoder Commit=0 to rearm. b. Cache ID Decoder Commit=1. c. Poll bits 0 and 1 of the Cache ID Decoder Status register until timeout or one of them is set. The timeout value is reported in the Cache ID Decoder Status register. d. If Cache ID Decoder Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If Cache ID Decoder Committed=1, the changes were committed. Proceed to Step 5. f. If neither bit is set and the timeout is reached, software should treat this as an error condition. 5. Configure the USP of Switch S to route Cache ID c: a. Route Table[c]= Port Number register of the DSP that is connected directly to Device D. 6. If the USP reports Explicit Cache ID RT Commit Required=1, commit the Cache ID changes as follows: a. Cache ID RT Commit=0 to rearm. b. Cache ID RT Commit=1. c. Poll bits 0 and 1 of the Cache ID RT Status register until timeout or one of them is set. The timeout value is reported in the Cache ID RT Status register. d. If Cache ID RT Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If Cache ID RT Committed=1, the changes were committed. Proceed to Step 7. f. If neither bit is set and the timeout is reached, software should treat this as an error condition. 7. Configure the Root Port, R, that is directly connected to Switch S to decode the CXL.cache messages from Device D: a. If Forward Cache ID=0, set Forward Cache ID=1. b. Ensure Assign Cache ID=0. 8. If the previous steps were successful, configure the CXL Cache ID Route Table (see Section 8.2.4.28.1) in the Host Bridge: a. Route Table[c].Port Number=Port Number register of Root Port R. 9. If the previous steps were successful, inform the device driver that Device D may now issue CXL.cache requests.

</td><td style="background-color:#e8e8e8">

系统软件可使用该能力来优化平台性能。实现注中描述的具体优化策略因平台而异。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-16"></a>
### 9.16 UIO Direct P2P to HDM | UIO Direct P2P to HDM

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

CXL.mem devices that can complete UIO requests that target its HDM, advertise the capability via the UIO Capable bit in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1). CXL switches may allow routing of UIO accesses to HDM in the same VH as the UIO requester and advertise this capability via the same bit. CXL Host Bridges may allow routing of UIO accesses to host memory or HDM below another root ports in the same Host Bridge and advertise this capability via this bit. Prior to setting up a UIO path from a UIO requester to an HDM or to host memory, the Software must consult the capabilities of the target device and any switches or Host Bridges in the path. Figure 9-25 shows a configuration with four CXL.mem devices that form three separate interleave sets and how a UIO requester is able to access the HDM range. UIO accesses to UIO Target 1 and UIO Target 2 are directly routed by the switch, whereas UIO accesses to UIO Target 3 and UIO Target 4 are routed through the host. As shown, UIO Target 1 and UIO Target 2 participate in a 2-way interleave set. The UIO requester can efficiently access this interleave set without going through the host. The HDM that is a target of P2P UIO accesses must be part of either a 1-way, 2-way, 4- way, 8-way, or 16-way interleave set. Any HDM that is part of a 3-way, 6-way, or 12- way interleave arrangement cannot be a P2P UIO target. The HDM address must be carved out of a CFMWS entry with Interleave Arithmetic=Standard Modulo arithmetic (see Table 9-22). In addition, P2P UIO traffic may be protected by Selective IDE Streams. In addition, Software must configure the switch and Host Bridge HDM decoders with additional information regarding any HDM interleaving calculations that are performed upstream to it before setting the UIO bit in that HDM decoder. The UIG, UIW, and ISP fields allow the switch and the Host Bridge to determine whether the UIO target Figure 9-25. UIO Direct P2P to Interleaved HDM

</td><td style="background-color:#e8e8e8">

表 9-22 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability address belongs to itself or to a peer component. The rules regarding the processing of UIO Direct P2P to HDM requests are described in Table 9-18. The ISP field in the target CXL.mem device allow the device to determine how it should respond. These requirements are in addition to the UIO related requirements that are defined in PCIe Base Specification.

</td><td style="background-color:#e8e8e8">

表 9-18 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-16-1"></a>
#### 9.16.1 Processing of UIO Direct P2P to HDM Messages | Processing of UIO Direct P2P to HDM Messages

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section describes how CXL components handle UIO Direct P2P accesses to HDM. UIO To HDM Enable bit is defined in Section 8.1.5.2 and allows System Software to control whether a requester below a switch can use UIO to access HDM.

</td><td style="background-color:#e8e8e8">

UIO Direct P2P to HDM 消息的处理遵循标准 CXL.io 路由和排序规则。接收方 DSP 或 Root Port 根据其 UIO 解码器配置检查传入的 UIO 请求的地址。匹配的请求被转发到目标 HDM 范围。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-16-1-1"></a>
#### 9.16.1.1 UIO Address Match (DSP and Root Port) | UIO Address Match (DSP and Root Port)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

For a DSP or a root port, UIO address is considered a complete match if there exists an HDM Decoder[n] (see Section 8.2.4.20 and Section 8.2.4.30) for which the following conditions are true: Table 9-18. Handling of UIO Accesses Received by UIO Address Behavior CXL.mem device that reports UIO Capable=1 (see Section 8.2.4.20.1) Complete match with an HDM decoder with UIO=1 Respond to the UIO request per PCIe Base Specification Complete match with an HDM decoder with UIO=0 Return Completer Abort, do not commit data if it is a UIO write Partial match with an HDM decoder, irrespective of the UIO bit Return Completer Abort, do not commit data if it is a UIO write Mismatch Handle per PCIe Base Specification USP ingress of a CXL Switch that reports UIO Capable=1 (see Section 8.2.4.20.1) Either Partial or Complete match with an HDM decoder, irrespective of the UIO bit Identify the port number of the target DSP and forward Mismatch Handle per PCIe Base Specification DSP ingress of a CXL Switch that reports UIO Capable=1 (see Section 8.2.4.20.1) Complete match with an HDM decoder with UIO=11 and UIO To HDM Enable=1 1. Because the DSP does not take length into account during this check, transactions that cross an interleave boundary get forwarded to the device that owns the starting address. They are aborted by the device because the device checks the length field. If the UIO traffic is encrypted using Stream IDE, some of the address bits may be encrypted and the switch may unknowingly forward these to the wrong device, which will issue a Completer Abort. Identify the port number of the target DSP and forward to that peer port regardless of ACS configuration including egress control vector Complete match with an HDM decoder with UIO=0 and UIO To HDM Enable=1 Forward toward the host regardless of ACS configuration including egress control vector Partial match with an HDM decoder and UIO To HDM Enable=1 Forward toward the host regardless of ACS configuration including egress control vector Complete or Partial match, and UIO To HDM Enable=0 Return Completer Abort Mismatch Handle per PCIe Base Specification RP ingress of a Host Bridge that reports UIO Capable=1 (see Section 8.2.4.20.1) Complete match with an HDM decoder with UIO=1 Identify the port number of the target RP and forward to that peer port, subject to host- specific access controls Complete match with an HDM decoder with UIO=0 Handle via host-specific mechanisms Partial match with an HDM decoder Handle via host-specific mechanisms Mismatch Handle via host-specific mechanisms

</td><td style="background-color:#e8e8e8">

表 9-18 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability 1. AT field in the UIO request indicates that it is carrying a translated address. 2. UIO.Address[63:2] ≥ Decoder[n].Base[63:2]. 3. UIO.Address[63:2]+UIO.Length[63:2] ≤ Decoder[n].Base[63:2]+ Decoder[n].Size[63:2]. 4. Either of these sub-conditions are true: a. Decoder[n].UIW=0 b. UIO.Address[Decoder[n].UIW+Decoder[n].UIG+7:Decoder[n].UIG+8]=ISP where UIO.Address[63:2] is derived from the Address field in the UIO TLP request, and UIO.Length[63:2] is derived from the Length field in the UIO TLP request. DSP calculations use the HDM decoders in the corresponding USP. The root port calculations make use of the HDM decoders in the associated Host Bridge. The first condition is in place because HDM decoder operates on translated address. The second and the third condition ensures that all addresses fall within one of the HDM decoders. The fourth condition ensures that the interleave set positions match (i.e., a CXL.mem request from the host to the start address would ordinarily be decoded by this component). 4a is the trivial case where the memory is not interleaved. If the first three conditions are met but the fourth condition is not met, it is considered a partial match. If the first three conditions are not met, it is considered a mismatch.

</td><td style="background-color:#e8e8e8">

UIO 请求中的 AT（Address Type）字段指示地址类型。接收组件根据 AT 字段和解码器配置确定如何处理请求。CXL.mem 设备将 UIO 地址与 HDM 解码器范围进行匹配，以验证访问是否允许。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-16-1-2"></a>
#### 9.16.1.2 UIO Address Match (CXL.mem Device) | UIO Address Match (CXL.mem Device)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

For a CXL.mem device, UIO address is considered a complete match if there exists an HDM Decoder[n] (see Section 8.2.4.20 and Section 8.2.4.30) for which the following conditions are true: 1. AT field in the UIO request indicates it is carrying a translated address. 2. UIO.Address[63:2] ≥ Decoder[n].Base[63:2]. 3. UIO.Address[63:2]+UIO.Length[63:2] ≤ Decoder[n].Base[63:2]+ Decoder[n].Size[63:2]. 4. Either of these sub-conditions are true: a. Decoder[n].UIW=0 b. UIO.Address[Decoder[n].IW+Decoder[n].IG+7:Decoder[n].IG+8]=ISP 5. UIO.Address[Decoder[n].IG+7:2] + UIO.Length[Decoder[n].IG+7:2] &lt;= (2** IG+8). The first three conditions are identical to the DSP case. The terms involved in the fourth check are different, but it serves the same purpose (i.e., ensures that a CXL.mem request from the host to the start address would ordinarily be decoded by this component). The fifth condition ensures that the access does not cross an interleave boundary, thus ensuring that all the addresses that are referenced by the request are owned by the device. If the first three conditions are met but either of the other two conditions are not met, it is considered a partial match. If the first three conditions are not met, it is considered a mismatch.

</td><td style="background-color:#e8e8e8">

UIO 请求中的 AT（Address Type）字段指示地址类型。接收组件根据 AT 字段和解码器配置确定如何处理请求。CXL.mem 设备将 UIO 地址与 HDM 解码器范围进行匹配，以验证访问是否允许。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-17"></a>
### 9.17 Direct P2P CXL.mem for Accelerators | Direct P2P CXL.mem for Accelerators

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The Direct P2P CXL.mem feature enables accelerators to use .mem semantics to access peer Type 3 devices. This feature is supported only by PBR Fabrics, and each accelerator and peer Type 3 device must be attached directly to an Edge Port. Configuration of the Fabric and Edge Ports is performed by the host and FM. Through mechanisms beyond the scope of this specification, the FM is preconfigured or informed of which Type 3 device(s) (i.e., SLD, MLD, or GFD) are to be configured for Direct P2P CXL.mem access by a given accelerator.

</td><td style="background-color:#e8e8e8">

Direct P2P CXL.mem for Accelerators 允许加速器使用 CXL.mem 协议直接访问挂接在其他 CXL 设备上的内存。此功能减少了对等通信的延迟，并避免主机内存带宽瓶颈。系统软件配置 P2P 路径，确保适当的地址映射和访问控制。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-17-1"></a>
#### 9.17.1 Peer SLD Configuration | Peer SLD Configuration

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Host software and the FM may use the following high-level flow to configure Direct P2P CXL.mem communication between an accelerator and a peer Type 3 SLD: 1. The FM binds the SLD’s Edge Port to the host VH of the accelerator, setting the vPPB.root.PID field to the PBR ID (PID) of the accelerator’s Edge Port. This enables the host to configure the SLD, but the accelerator to carry out CXL.mem transactions with the SLD. 2. Using the Set LDST Segment Entries command (see Section 7.7.13.16), the host configures the LDST in the accelerator’s Edge Port with one or more LDST Segments for the HPA range of the SLD, specifying the vPPB of the SLD’s Edge Port. 3. Host software configures the SLD, notably its HDM Decoders, on behalf of the accelerator. HDM addresses in the SLD are HPAs.

</td><td style="background-color:#e8e8e8">

对等 SLD 配置涉及在单个逻辑设备上设置 P2P 解码器。系统软件为每个对等端口配置地址解码范围，并确保对等访问不会与主机分配的地址冲突。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-17-2"></a>
#### 9.17.2 Peer MLD Configuration | Peer MLD Configuration

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Host software and the FM may use the following high-level flow to configure Direct P2P CXL.mem communication between one or more accelerators that belong to the host and a peer Type 3 MLD: 1. The FM binds a vPPB in the MLD’s Edge Port to the host VH of its accelerator(s) and an additional vPPB for each accelerator under that host that will be accessing the MLD. Each of these will have a distinct LD-ID. For each vPPB assigned to an accelerator, the vPPB.root.PID field is set to the PID of the accelerator’s Edge Port. 2. Using the Set LDST Segment Entries command (see Section 7.7.13.16), the host configures the LDST in each accelerator’s Edge Port with one or more LDST Segments for the HPA range of the accelerator’s LD, specifying the accelerator’s vPPB in the MLD’s Edge Port. 3. Host software configures its LDs in the MLD, notably their HDM Decoders, on behalf of itself and its accelerator(s). HDM addresses in the LD of the host and the LD(s) of the accelerator(s) are HPAs.

</td><td style="background-color:#e8e8e8">

对等 MLD 配置扩展了 P2P 概念到多逻辑设备。每个 LD 具有自己的 P2P 解码器和地址范围。系统软件必须为每个 LD 单独配置 P2P 路径，并确保 LD 之间不重叠。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-17-3"></a>
#### 9.17.3 Peer GFD Configuration | Peer GFD Configuration

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Host software and the FM may use the following high-level flow to configure Direct P2P CXL.mem communication between one or more accelerators that belong to a host and a peer Type 3 GFD: 1. The FM configures the GFD for host access normally, while configuring each of the host’s accelerators as an additional RPID within the GFD. 2. Using the Set FAST Segment Entries command (see Section 7.7.14.7), the host configures the FAST decoder in its Edge Port as well as each accelerator’s Edge Port with one or more FAST Segments for the HPA range, specifying the GFD’s PID.

</td><td style="background-color:#e8e8e8">

本节描述Reset, Initialization, Configuration, and Manageability

</td><td style="backgro的相关规范要求。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1"></a>
#### 9.18.1 CXL Early Discovery Table (CEDT) | CXL Early Discovery Table (CEDT)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

CXL Early Discovery Table enables OSs to locate CXL Host Bridges and the location of Host Bridge registers early during the boot (i.e., prior to parsing of ACPI namespace). The information in this table may be used by early boot code to perform pre- initialization of CXL hosts, such as configuration of CXL.cache and CXL.mem.

</td><td style="background-color:#e8e8e8">

CXL Early Discovery Table (CEDT) 是一个 ACPI 表，提供 CXL 设备的早期发现信息。CEDT 包含 CHBS、CFMWS、CXIMS、RDPAS 和 CSDS 等结构，使操作系统能够在完整 PCIe 枚举之前识别 CXL 资源。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1-1"></a>
#### 9.18.1.1 CEDT Header | CEDT Header

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The pointer to CEDT is found in RSDT or XSDT, as described in ACPI Specification. An ACPI specification-compliant CXL system shall support CEDT and shall include a CHBS entry for every CXL host bridge that is present at boot. CEDT begins with the following header.

</td><td style="background-color:#e8e8e8">

CEDT 头遵循标准 ACPI 表头格式，包含签名 'CEDT'、长度、修订版本和校验和。表头后跟一个或多个 CXL 结构体。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1-2"></a>
#### 9.18.1.2 CXL Host Bridge Structure (CHBS) | CXL Host Bridge Structure (CHBS)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CHBS structure describes a CXL Host Bridge. Table 9-19. CEDT Header Field Length in Bytes Byte Offset Description Header: Signature 00h ‘CEDT’. Signature for the CXL Early Discovery Table. Length 04h Length, in bytes, of the entire CEDT. Revision 08h Value is 2. Checksum 09h Entire table must sum to 0. OEM ID 0Ah OEM ID OEM Table ID 10h Manufacturer Model ID OEM Revision 18h OEM Revision Creator ID 1Ch Vendor ID of the utility that created the table. Creator Revision 20h Revision of the utility that created the table. CEDT Structure[n] Varies 24h A list of CEDT structures for this implementation. Table 9-20. CEDT Structure Types Value Description CXL Host Bridge Structure (CHBS) CXL Fixed Memory Window Structure (CFMWS) CXL XOR Interleave Math Structure (CXIMS) RCEC Downstream Port Association Structure (RDPAS) CXL System Description Structure (CSDS)1 1. Introduced in Revision 2 of CEDT. 5-255 Reserved

</td><td style="background-color:#e8e8e8">

表 9-19 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability In an ACPI-compliant system, there shall be one instance of the CXL Host Bridge Device object in ACPI namespace (HID=“ACPI0016”) for every CHBS entry. The _UID object under a CXL Host Bridge object, when evaluated, shall match the UID field in the associated CHBS entry.

</td><td style="background-color:#e8e8e8">

CXL Early Discovery Table (CEDT) 是一个 ACPI 表，提供 CXL 设备的早期发现信息。CEDT 包含 CHBS、CFMWS、CXIMS、RDPAS 和 CSDS 等结构，使操作系统能够在完整 PCIe 枚举之前识别 CXL 资源。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1-3"></a>
#### 9.18.1.3 CXL Fixed Memory Window Structure (CFMWS) | CXL Fixed Memory Window Structure (CFMWS)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CFMWS structure describes zero or more Host Physical Address (HPA) windows that are associated with each CXL Host Bridge. Each window represents a contiguous HPA range that may be interleaved across one or more targets, some of which are CXL Host Bridges. Associated with each window are a set of restrictions that govern its usage. It is the OSPM’s responsibility to utilize each window for the specified use. The HPA ranges described by CFMWS may include addresses that are currently assigned to CXL.mem devices. Before assigning HPAs from a fixed-memory window, the OSPM must check the current assignments and avoid any conflicts. For any given HPA, it shall not be described by more than one CFMWS entry. Table 9-21. CHBS Structure Field Length in Bytes Byte Offset Description Type 00h =0 to indicate that this is a CHBS entry Reserved 01h Reserved Record Length 02h Length of this record (20h). UID 04h CXL Host Bridge Unique ID. Used to associate a CHBS instance with a CXL Host Bridge instance. The value of this field shall match the output of _UID under the associated CXL Host Bridge in ACPI namespace. CXL Version 08h • 0000 0000h: RCH • 0000 0001h: Host Bridge that is associated with one or more CXL root ports Reserved 0Ch Reserved Base 10h • If CXL Version = 0000 0000h, this represents the base address of the RCH Downstream Port RCRB • If CXL Version = 0000 0001h, this represents the base address of the CHBCR See Table 8-17 for more details. Length 18h • If CXL Version = 0000 0000h, this field must be set to 8 KB (2000h) • If CXL Version = 0000 0001h, this field must be set to 64 KB (1 0000h)

</td><td style="background-color:#e8e8e8">

表 9-21 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability Table 9-22. CFMWS Structure (Sheet 1 of 3) Field Length in Bytes Byte Offset Description Type 00h 1 = indicates this is a CFMWS entry Reserved 01h Reserved Record Length 02h Length of this record = 024h + 4 * NIW. NIW is the raw count of Interleave ways whereas ENIW is the encoded value: • If ENIW&lt;8, NIW=2**ENIW • If ENIW≥8, NIW=3* 2**(ENIW-8) Reserved 04h Reserved Base HPA 08h Base of this HPA range. This value shall be a 256-MB-aligned address. Window Size 10h The total number of consecutive bytes of HPA this window represents. This value shall be a multiple of NIW*256 MB. Encoded Number of Interleave Ways (ENIW) 18h The encoded number of targets with which this window is interleaved. The valid encoded values are specified in the Interleave Ways field of the CXL HDM Decoder n Control register (see Section 8.2.4.20.7). This field determines the number of entries in the Interleave Target List, starting at Offset 24h. Interleave Arithmetic 19h This field defines the arithmetic used for mapping HPA to an interleave target in the Interleave Target List: • 00h = Standard Modulo arithmetic • 01h = Modulo arithmetic combined with XOR • All other encodings are reserved Reserved 1Ah Reserved Host Bridge Interleave Granularity (HBIG) 1Ch The number of consecutive bytes within the interleave that are decoded by each target in the Interleave Target List represented in an encoded format. The valid values are specified in the Interleave Granularity field of the CXL HDM Decoder n Control register (see Section 8.2.4.20.7). Window Restrictions 20h A bitmap describing the restrictions being placed on the OSPM’s use of the window. It is the OSPM’s responsibility to adhere to these restrictions. Failure to adhere to these restrictions results in undefined behavior. More than one bit within this field may be set: • Bit[0]: Device Coherent: Formerly known as CXL Type 2 Memory: — 1 = Window is configured to expose device-coherent memory (HDM-D if Bit[5]=0 ; HDM-DB if Bit[5]=1). • Bit[1]: Host-only Coherent: Formerly known as CXL Type 3 Memory: — 1 = Window is configured to expose host-only coherent memory (HDM- H). If an HDM decoder that is mapped to this windows has the BI bit set, it will result in undefined behavior. • Bit[2]: Volatile: — 1 = Window is configured for use with volatile memory. • Bit[3]: Persistent: — 1 = Window is configured for use with persistent memory. • Bit[4]: Fixed Device Configuration: — 1 = Any device ranges that have been assigned an HPA from this window must not be reassigned. • Bit[5]: BI: — 1 = Window is configured for use with Back-Invalidate flows. • Bits[15:6]: Reserved QTG ID 22h The ID of the QoS Throttling Group associated with this window. The _DSM for retrieving QTG ID is utilized by the OSPM to determine to which QTG a device HDM range should be assigned. This field must not exceed the Max Supported QTG ID returned by the _DSM for retrieving QTG.

</td><td style="background-color:#e8e8e8">

表 9-22 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability Interleave Target List 4*NIW 24h A list of all the Interleave Targets. The number of entries in this list shall match the Number of Interleave Ways (NIW). The order of the targets reported in this List indicates the order in the Interleave Set. For Interleave Sets that only span CXL Host Bridges, this is a list of CXL Host Bridge _UIDs that are part of the Interleave Set. In this case, for each _UID value in this list, there must exist a corresponding CHBS structure. If the Interleave Set spans non-CXL domains, this list may contain values that do not match _UID field in any CHBS structures. These entries represent Interleave Targets that are not CXL Host Bridges. The set of HPAs decoded by Entry N in the Interleave Target List shall satisfy the following equations: 1. Base HPA &lt;= HPA &lt; Base HPA + Windows Size: where the Base HPA and Window size shall be multiple of NIW. If (Interleave Arithmetic==0): a. If ENIW=0 N=0 b. If ENIW=1 N= HPA[8+HBIG] c. If ENIW&lt;8 AND ENIW&gt;1 N = HPA[7+HBIG+ENIW:8+HBIG] d. If NIW = 8      // 3 way N = HPA[51:8+HBIG] MOD 3 e. If NIW=9        // 6 way N = HPA[8+HBIG] + 2* HPA[51:9+HBIG] MOD 3 f. If NIW=10      //12 way N = HPA[9+HBIG:8+HBIG] + 4* HPA[51:10+HBIG] MOD 3 2. If (Interleave Arithmetic==1): a. If NIW=0   //1 way N=0 b. If NIW =1    // 2 way N = XORALLBITS (HPA AND XORMAP[0]) If NIW=2     // 4 way N = XORALLBITS (HPA AND XORMAP[0]) + 2* XORALLBITS (HPA AND XORMAP[1]) Table 9-22. CFMWS Structure (Sheet 2 of 3) Field Length in Bytes Byte Offset Description

</td><td style="background-color:#e8e8e8">

表 9-22 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1-4"></a>
#### 9.18.1.4 CXL XOR Interleave Math Structure (CXIMS) | CXL XOR Interleave Math Structure (CXIMS)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

If a CFMWS entry reports Interleave Arithmetic=1, there must be one CXIMS entry associated with the HBIG value in the CFMWS. CXIMS carries an array of bitmaps. Each bitmap represents the bits that are XORed together to calculate the individual bits of the Interleave Way as described in the definition of the Interleave Target List field in CFMWS. The host implementation is responsible for selecting an XOR function that generates even distribution of addresses and does not lead to address aliasing. Interleave Target List 4*NIW 24h c. If NIW=3    // 8 way N = XORALLBITS (HPA AND XORMAP[0]) + * XORALLBITS (HPA AND XORMAP[1]) + * XORALLBITS (HPA AND XORMAP[2]) d. If NIW=4    //16 way N = XORALLBITS (HPA AND XORMAP[0])+ 2* XORALLBITS (HPA AND XORMAP[1]) + 4* XORALLBITS (HPA AND XORMAP[2]) + 8* XORALLBITS (HPA AND XORMAP[3]) e. If NIW =8    // 3 way, same as Interleave Arithmetic=0 N = HPA[51:8+HBIG] MOD 3 f. If NIW =9     // 6 way N = XORALLBITS (HPA AND XORMAP[0]) + 2* HPA[51:9+HBIG] MOD 3 g. If NIW=10     // 12 way N = XORALLBITS (HPA AND XORMAP[0]) + 2* XORALLBITS (HPA AND XORMAP[1]) + 4* HPA[51:10+HBIG] MOD 3 N is 0 based (0&lt;= N &lt;NIW). Where XORALLBITS is an operation that outputs a single bit by XORing all the bits in the input. AND is a standard bitwise AND operation and XORMAP[m] is the mth element (m is 0 based) in the XORMAP array that is part of the CXIMS entry with the matching HBIG value. Table 9-22. CFMWS Structure (Sheet 3 of 3) Field Length in Bytes Byte Offset Description Table 9-23. CXIMS Structure Field Length in Bytes Byte Offset Description Type 00h 2 = Indicates that this is a CXIMS entry Reserved 01h Reserved Record Length 02h Length of this record = 8 + 8 * NIB. Reserved 04h Reserved HBIG 06h Host Bridge Interleave Granularity to which this CXIMS instance corresponds. See Table 9-22 for the definition of the term HBIG. Number of Bitmap Entries (NIB) 07h The number of entries in the XORMAP list. XORMAP List 8 * NIB 08h A list of Bitmaps. XORMAP[0] is the first entry.

</td><td style="background-color:#e8e8e8">

表 9-22 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1-5"></a>
#### 9.18.1.5 RCEC Downstream Port Association Structure (RDPAS) | RCEC Downstream Port Association Structure (RDPAS)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

RDPAS structure enables error handler to locate the Downstream Port(s) that report errors to a given RCEC. For every RCEC, zero or more entries of this type are permitted.

</td><td style="background-color:#e8e8e8">

RCEC Downstream Port Association Structure (RDPAS) 将 RCEC 与其关联的 CXL 下行端口关联起来。此结构用于错误报告场景中，以确定错误的来源。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-1-6"></a>
#### 9.18.1.6 CXL System Description Structure (CSDS) | CXL System Description Structure (CSDS)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CSDS describes CXL System Wide Description and Configuration. In a system, there shall be only one instance of the CSDS in the CEDT. Table 9-24. RDPAS Structure Field Length in Bytes Byte Offset Description Type 00h 3 = Indicates that this is an RDPAS entry Reserved 01h Reserved Record Length 02h Length of this record = 14h RCEC Segment Number 04h The PCIe segment number associated with this RCEC RCEC BDF 06h • Bits[2:0]: RCEC Function Number • Bits[7:3]: RCEC Device Number • Bits[15:8]: RCEC Bus Number Base Address 08h If Protocol Type = CXL.io, this field shall be the RCRB base associated with the Downstream Port. If Protocol Type = CXL.cachemem, this will be the Component Base Register Base associated with the Downstream Port. Protocol Type 10h • 00h = The error source is CXL.io • 01h = The error source is CXL.cachemem Reserved 11h Reserved IMPLEMENTATION NOTE CXL-aware software may take the following steps upon observing an Uncorrected Internal Error or an Corrected Internal Error being logged in an RCEC at Segment Number S and BDF=B. If the CEDT contains RDPAS structures: • For all RDPAS structures where RCEC Segment Number=S and RCEC BDF= B: — If Protocol Type=CXL.io, read the Base Address field and use that information to access the RCRB AER registers and determine whether any errors are logged there — If Protocol Type=CXL.cachemem, read the Base Address field and use that information to access the Component Register RAS Capability registers (see Section 8.2.4.17) and determine whether any errors are logged there Else: • Probe all CXL Downstream Ports and determine whether they have logged an error in the CXL.io or CXL.cachemem status registers

</td><td style="background-color:#e8e8e8">

实现注：Reset, Initialization, Configuration, and Manageability

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-2"></a>
#### 9.18.2 CXL _OSC | CXL _OSC

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

According to ACPI Specification, _OSC (Operating System Capabilities) is a control method that is used by OSs to communicate to the System Firmware the capabilities supported by the OS and to negotiate ownership of specific capabilities. The _OSC interface defined in this section applies only to “Host Bridge” ACPI devices that originate CXL hierarchies. As specified in Section 9.12, these ACPI devices must have an _HID of (or a _CID that includes) EISAID(“ACPI0016”). CXL _OSC is required for a CXL VH. CXL _OSC is optional for an RCD. A CXL Host Bridge also originates a PCIe hierarchy and will have a _CID of EISAID(“PNP0A08”). As such, a CXL Host Bridge device may expose both CXL _OSC and PCIe _OSC. The _OSC interface for a CXL Host Bridge is identified by the Universal Unique Identifier (UUID) 68f2d50b-c469-4d8a-bd3d-941a103fd3fc. A revision ID of 1 encompasses fields defined within this section, composed of 5 DWORDs, as listed in Table 9-26. Table 9-25. CSDS Structure Field Length in Bytes Byte Offset Description Type 00h 4 = Indicates that this is a CSDS entry Reserved 01h Reserved Record Length 02h Length of this record = 08h System Capabilities 04h A bitmap that describes system-wide capabilities. More than one bit within this field is permitted to be set. • Bit[0]: Cmp-M: — 1 = System is configured for use with devices that return modified data using the Cmp-M response. • Bit[1]: No Clean Writeback: Specifies the clean writeback behavior of the host. — 0 = The host may or may not generate clean writebacks — 1 = The host guarantees to never generate clean writeback transactions at the host’s cacheline granularity • Bit[2]: Viral Policy: If 1, the system policy is to enable Viral. • Bits[5:3]: Metabits Storage Configuration. Upon hot-add, the OS may configure the device to match host metadata storage requirements — 0h: 2 bits of Metadata — 1h: No Metadata — 2h: 1 bit of Metadata, bit-0 of Meta0-State Value — 3h: 1 bit of Metadata, bit-1 of Meta0-State Value — 4h: 2 bits of Metadata + 1 TE State bit — 5h: No Metadata + 1 TE State bit — 6h: 1 bit of Metadata, bit-0 of Meta0-State Value + 1 TE State bit — 7h: 1 bit of Metadata, bit-1 of Meta0-State Value + 1 TE State bit • Bits[15:6]: Reserved Reserved 06h Reserved

</td><td style="background-color:#e8e8e8">

表 9-26 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability Table 9-26. _OSC Capabilities Buffer DWORDs _OSC Capabilities Buffer DWORD # Description Contains bits that are generic to _OSC and defined by ACPI. These include status and error information. PCIe Support Field as defined by PCI Firmware Specification. PCIe Control Field as defined by PCI Firmware Specification. CXL Support Field: Bits defined in the CXL Support Field provide information regarding CXL features supported by the OS. Just like the PCIe Support field, contents in the CXL Support Field are passed in a single direction; the OS will disregard any changes to this field when returned. CXL Control Field: Just like the PCIe Control Field, bits defined in the CXL Control Field are used to submit OS requests for control/handling of the associated feature, typically including but not limited to features that utilize native interrupts or events that are handled by an OS-level driver. If any bits in the CXL Control Field are returned cleared (i.e., masked to 0) by the _OSC control method, the respective feature is designated as unsupported by the platform and must not be enabled by the OS. Some of these features may be controlled by System Firmware prior to OS boot or during runtime for an OS that is unaware of these features, while others may be disabled/ inoperative until native OS support for such features is available. If the CXL _OSC control method is absent from the scope of a Host Bridge device, then the OS must not enable or attempt to use any features defined in this section for the hierarchy originated by the Host Bridge. Doing so could conflict with System Firmware operations, or produce undesired results. It is recommended that a machine with multiple Host Bridge devices should report the same capabilities for all Host Bridges, and also negotiate control of the features described in the CXL Control Field in the same way for all Host Bridges. Table 9-27. Interpretation of CXL _OSC Support Field Support Field Bit Offset Interpretation RCD and RCH Port Register Access Supported The OS sets this bit to 1 if it supports access to RCD and RCH Port registers as defined in Section 9.11. Otherwise, the OS clears this bit to 0. CXL VH Register Access Supported The OS sets this bit to 1 if it supports access to CXL VH component registers as defined in Section 9.12. If this bit is 1, bit 0 must also be 1. Otherwise, the OS clears this bit to 0. CXL Protocol Error Reporting Supported The OS sets this bit to 1 if it supports handling of CXL Protocol Errors. Otherwise, the OS clears this bit to 0. If the OS sets this bit, it must also set either bit 0 or bit 1 above. Note: Firmware may retain control of AER if the OS does not support CXL Protocol Error reporting because the owner of AER owns CXL Protocol error management. CXL Native Hot-Plug Supported The OS sets this bit to 1 if it supports CXL hot-add and managed CXL Hot-Remove without firmware assistance. Otherwise, the OS clears this bit to 0. If the OS sets this bit, it must request PCIe Native Hot-Plug control. If PCIe Native Hot-Plug control is granted to the OS, such an OS must natively handle CXL Hot-Plug as well. If the OS sets this bit, it must also set bit 1 above. 4-31 Reserved

</td><td style="background-color:#e8e8e8">

表 9-26 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-2-1"></a>
#### 9.18.2.1 Rules for Evaluating _OSC | Rules for Evaluating _OSC

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section defines when and how the OS must evaluate _OSC, as well as restrictions on firmware implementations.

</td><td style="background-color:#e8e8e8">

评估 _OSC 的规则包括：操作系统必须在调用任何其他 CXL 相关方法之前调用 _OSC。如果 _OSC 未被调用，固件假定操作系统不提供 CXL 支持。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-2-1-1"></a>
#### 9.18.2.1.1 Query Support Flag | Query Support Flag

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

If the Query Support Flag (_OSC Capabilities Buffer DWORD 1, bit 0) is set by the OS while evaluating _OSC, hardware settings are not permitted to be changed by firmware in the context of the _OSC call. It is strongly recommended that the OS evaluate _OSC with the Query Support Flag set until _OSC returns the Capabilities Masked bit cleared to negotiate the set of features to be granted to the OS for native support. A platform may require a specific combination of features to be natively supported by an OS before granting native control of a given feature.

</td><td style="background-color:#e8e8e8">

Query Support Flag 允许操作系统在不获取控制权的情况下查询平台支持的 CXL 功能。固件在响应中返回支持的 CXL 功能位掩码。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-2-1-2"></a>
#### 9.18.2.1.2 Evaluation Conditions | Evaluation Conditions

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The OS must evaluate _OSC under the following conditions: • During initialization of any driver that provides native support for features described in the section above. These features may be supported by one or many drivers, but should be evaluated only by the main bus driver for that hierarchy. Secondary drivers must coordinate with the bus driver to install support for these features. Drivers shall not relinquish control of previously obtained features. That is, bits set in _OSC Capabilities Buffer DWORD 3 and DWORD 5 after the negotiation process must be set on all subsequent negotiation attempts. • When a Notify(&lt;device&gt;, 8) is delivered to the CXL Host Bridge device. • Upon resume from S4, System Firmware will handle context restoration when resuming from S1 through S3. If a CXL Host Bridge device exposes CXL _OSC, CXL-aware OSPM shall evaluate CXL _OSC and not evaluate PCIe _OSC. Table 9-28. Interpretation of CXL _OSC Control Field, Passed in via Arg3 Control Field Bit Offset Interpretation CXL Memory Error Reporting Control The OS sets this bit to 1 to request control over CXL Memory Error Reporting i.e. Set Event Interrupt Policy command for devices that implement Memory Device Commands (see Section 8.2.10.9). If the OS sets this bit, the OS must also set either bit 0 or bit 1 in the CXL _OSC Support Field (see Table 9-26). 1-31 Reserved Table 9-29. Interpretation of CXL _OSC Control Field, Returned Value Control Field Bit Offset Interpretation CXL Memory Error Reporting Control The firmware sets this bit to 1 to grant control over CXL Memory Expander Error Reporting i.e. Set Event Interrupt Policy command for devices that implement Memory Device Commands (see Section 8.2.10.9). If firmware grants control of this feature, firmware must ensure that these devices are not configured in Firmware First error reporting mode. If control of this feature was requested and denied or was not requested, firmware returns this bit cleared to 0. 1-31 Reserved

</td><td style="background-color:#e8e8e8">

表 9-28 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-2-1-3"></a>
#### 9.18.2.1.3 Sequence of _OSC Calls | Sequence of _OSC Calls

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The following rules govern sequences of calls to _OSC that are issued to the same Host Bridge and occur within the same boot: • The OS is permitted to evaluate _OSC an arbitrary number of times. • If the OS declares support of a feature in the Status Field in one call to _OSC, then it must preserve the set state of that bit (and thereby declare support for that feature) in all subsequent calls. • If the OS is granted control of a feature in the Control Field in one call to _OSC, then it must preserve the set state of that bit (requesting that feature) in all subsequent calls. • Firmware shall not reject control of any feature it has previously granted control to. • There is no mechanism for the OS to relinquish control of a previously requested and granted feature.

</td><td style="background-color:#e8e8e8">

_OSC 调用顺序：首先调用 Query Support Flag 以确定可用功能，然后调用实际的 _OSC 评估以请求控制权。操作系统应在调用之间保存 Query 的结果。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-2-1-4"></a>
#### 9.18.2.1.4 ASL Example | ASL Example

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Device(CXL0) { Name(_HID,EISAID("ACPI0016")) // CXL Host Bridge Name(_CID, Package(2) { EISAID("PNP0A03"), // PCI Compatible Host Bridge EISAID("PNP0A08") // PCI Express Compatible Host Bridge }) Name(SUPP,0) // PCI _OSC Support Field value Name(CTRL,0) // PCI _OSC Control Field value Name(SUPC,0) // CXL _OSC Support Field value Name(CTRC,0) // CXL _OSC Control Field value Method(_OSC,4) { // Check for proper UUID If(LEqual(Arg0,ToUUID("68f2d50b-c469-4d8a-bd3d-941a103fd3fc "))) { // Create DWord-adressable fields from the Capabilities Buffer CreateDWordField(Arg3,0,CDW1) CreateDWordField(Arg3,4,CDW2) CreateDWordField(Arg3,8,CDW3) CreateDWordField(Arg3,12,CDW4) CreateDWordField(Arg3,16,CDW5) // Save Capabilities DWord2, 3. 4. 5 Store(CDW2,SUPP) Store(CDW3,CTRL) Store(CDW4,SUPC) Store(CDW4,CTRc) .. .. } Else { Or(CDW1,4,CDW1) // Unrecognized UUID Return(Arg3) } } // End _OSC // Other methods such as _BBN, _CRS, PCIe _OSC } //End CXL0

</td><td style="background-color:#e8e8e8">

ASL 示例代码展示了典型的 _OSC 实现，包括支持的功能位检查、控制权授予逻辑以及平台特定的限制。开发人员可以以此为基础适配自己的平台实现。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-3"></a>
#### 9.18.3 CXL Root Device Specific Methods (_DSM) | CXL Root Device Specific Methods (_DSM)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

_DSM is a control method that enables devices to provide device-specific functions for the benefit of the device driver. See ACPI Specification for details. Table 9-30 lists the _DSM Functions that are associated with the CXL Root Device (HID=“ACPI0017”).

</td><td style="background-color:#e8e8e8">

表 9-30 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability All other Function values are reserved. The Revision field represents the version of the individual _DSM Function. The Revision associated with a _DSM Function is incremented whenever that _DSM Function is extended to add more functionality. Backward compatibility shall be maintained during this process. Specifically, for all values of n, a _DSM Function with Revision n+1 may extend Revision ID n by assigning meaning to the fields that are marked as reserved in Revision n but must not redefine the meaning of existing fields and must not change the size or type of I/O parameters. Software that was written for a lower Revision may continue to operate on _DSM Functions with a higher Revision but will not be able to take advantage of new functionality. It is legal for software to invoke a _DSM Function and pass in any nonzero Revision ID value that does not exceed the Revision ID defined in this specification for that _DSM Function. For example, if the most-current version of this specification defines Revision ID=4 for _DSM Function Index f, software is permitted to invoke the _DSM Function with Function Index f with a Revision ID value that belongs to the set {1, 2, 3, 4}.

</td><td style="background-color:#e8e8e8">

所有其他 Function 值均为保留。对保留 Function 值的调用将返回错误。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-18-3-1"></a>
#### 9.18.3.1 _DSM Function for Retrieving QTG ID | _DSM Function for Retrieving QTG ID

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section describes how the OSPM can request the firmware to determine the optimum QoS Throttling Group (QTG) to which a device HDM range should be assigned, based on its performance characteristics. It is strongly recommended that OSPM evaluate this _DSM Function to retrieve QTG recommendations and map the device HDM range to an HPA range that is described by a CFMWS entry that follows the platform recommendations. For each Device Scoped Memory Affinity Structure (DSMAS) in the Device CDAT, the OSPM should calculate the Read Latency, Write Latency, Read Bandwidth, and Write Bandwidth from the CXL Root Port within the same VCS. The term DSMAS is defined in Coherent Device Attribute Table Specification. This calculation must consider the latency and bandwidth contribution of any intermediate switches. The OSPM should call this _DSM with the performance characteristics for the Device HDM range thus calculated, utilize the return ID value(s) to pick an appropriate CFMWS, and then map the DSMAS DPA range to HPAs that are covered by that CFMWS. This process may be repeated for each DSMAS memory range that the OSPM wishes to utilize from the device. Location: This object shall be a child of the CXL Root Device (HID=“ACPI0017”). Arguments: Arg0: UUID: f365f9a6-a7de-4071-a66a-b40c0b4f8e52 Arg1: Revision ID: 1 Arg2: Function Index: 01h Arg3: A package of memory device performance characteristic. The package consists of 4 DWORDs. Table 9-30. _DSM Definitions for CXL Root Device UUID Revision Function Description F365F9A6-A7DE-4071-A66A-B40C0B4F8E52 Retrieve QTG ID (see Section 9.18.3.1) - All other Reserved

</td><td style="background-color:#e8e8e8">

表 9-30 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability Package { Read Latency Write Latency Read Bandwidth Write Bandwidth } Return: A package containing two elements - a WORD that returns the maximum throttling group that the platform supports, and a package containing the QTG ID(s) that the platform recommends. Package { Max Supported QTG ID Package {QTG Recommendations} } Table 9-31. _DSM for Retrieving QTG, Inputs, and Outputs Field Size Description Input Package: Read Latency DWORD The best-case read latency as measured from the CXL root port within the same VCS, expressed in picoseconds. Write Latency DWORD The best-case write latency as measured from the CXL root port within the same VCS, expressed in picoseconds. Read Bandwidth DWORD The best-case read bandwidth as measured from the CXL root port within the same VCS, expressed in MB/s. Write Bandwidth DWORD The best-case write bandwidth as measured from the CXL root port within the same VCS, expressed in MB/s. Return Package: Max Supported QTG ID WORD The highest QTG ID supported by the platform. The platform must be capable of supporting all QTGs whose ID, Q, satisfies the following equation: 0 &gt; Q ≥ Max Supported QTG ID For every value of Q, there may be zero or more CFMWS entries. QTG Recommendations Package A package that consists of 0 or more WORD elements. It is a prioritized list of QTG IDs that are considered acceptable by the platform for the specified performance characteristics. If the package contains more than one element, element[n] is preferred by the platform over element[n+1]. If the package is empty, the platform is unable to find any suitable QTGs for this set of input values. If the OSPM does not follow platform QTG recommendations, it may result in severe performance degradation. Every element in this package must be no greater than the Max Supported QTG ID above. For example, if QTG Recommendations = Package () {2, 1}, the OSPM should first attempt to assign from QTG ID 2, and then attempt to assign QTG ID 1 if an assignment cannot be found in QTG ID 2.

</td><td style="background-color:#e8e8e8">

表 9-31 定义了相关结构体的字段布局。各字段的详细描述请参考英文原文和 CXL 规范正文。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-19"></a>
### 9.19 Manageability Model for CXL Devices | Manageability Model for CXL Devices

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Manageability is the set of capabilities that a managed entity exposes to a management entity. In the context of CXL, a CXL device is the managed entity. These capabilities are generally classified in sensors and effectors. An Event Log is an example of a sensor, whereas the ability to update the device firmware is an example of an effector. Sensors and effectors can either be accessed in-band (i.e., by OS/VMM resident software), or out-of-band (i.e., by firmware running on a management controller that is OS independent). In-band software can access a CXL device’s manageability capabilities by issuing PCIe configuration read/write or MMIO read/write transactions to its Mailbox registers. These accesses are generally mediated by the CXL device driver. This is consistent with how PCIe adapters are managed. Out-of-band manageability in S0 state can leverage transports for which an MCTP binding specification has been defined. This assumes that the CXL.io path will decode and forward MCTP over PCIe VDMs in both directions. Form factors, such as PCIe CEM Specification, provision two SMBUS pins (clock and data). The SMBUS path can be used for out-of-band manageability in Sx state or in the Link Down case. This is consistent with PCIe adapters. CXL components may also support additional management capabilities defined in other specifications, such as Platform-Level Data Model (PLDM).

</td><td style="background-color:#e8e8e8">

CXL 设备的管理模型定义了系统软件如何监控、配置和维护 CXL 设备。管理模型包括带内（in-band）和带外（out-of-band）管理路径。带内管理使用 CXL.io 配置空间和邮箱命令，带外管理使用 MCTP 或其他边带协议。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-20"></a>
### 9.20 Component Command Interface | Component Command Interface

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Runtime management of CXL components is facilitated by a Component Command Interface (CCI). A CCI represents a command target that is used to process management and configuration commands that are issued to the component. Table 8-49, Table 8-141, and Table 8-230 define the commands that a CCI can support. A component can implement multiple CCIs of varying types that operate independently of one another and that have a uniquely defined list of supported commands. There are 2 types of CCIs: • CXL Mailbox Registers: A component can expose up to 2 CXL mailboxes through its Mailbox registers for every instance of CXL Device Registers, as defined in Section 8.2.9.4. Each mailbox represents a unique CCI instance. • MCTP-based CCIs: Components with MCTP-capable interconnects can expose up to 1 CCI per interconnect. There is a 1:1 relationship between the component’s MCTP- based CCIs and MCTP-capable interconnects. Transfer of commands via MCTP uses the transport protocol defined in Section 7.6.3. All CCIs shall comply with the properties described in Section 9.20.1.

</td><td style="background-color:#e8e8e8">

本节描述Reset, Initialization, Configuration, and Manageability

</td><td style="backgro的相关规范要求。

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-20-1"></a>
#### 9.20.1 CCI Properties | CCI Properties

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Components that implement more than one CCI shall process commands from those CCIs in a manner that avoids starvation so that commands submitted to one CCI do not prevent commands from other CCIs from being handled. The exact algorithm for accepting commands from multiple CCIs is implementation specific. Each CCI within a component reports its supported command list through the Command Effects Log (CEL), as described in Section 8.2.10.5.2.1. Interface-specific properties of commands, background operation, and timeouts are defined in Section 8.2.9.4 for mailbox CCIs and in Section 9.20.2 for MCTP-based CCIs. Each CCI can support the execution of only one background command at a time. When a command is successfully started as a background operation, the component shall return the Background Command Started return code defined in Section 8.2.9.4.5.1. While the command is executing in the background, the component should update the percentage complete at least once per second. A component may return the Busy return code if a command is sent to initiate a Background Operation while a Background Operation is already running on any other CCI. An ongoing background command may be aborted by issuing a Request Abort Background Operation command on the same CCI (see Section 8.2.10.1.5). Each CCI within a component shall maintain a unique context with respect to the following capabilities: • CEL content With respect to the following capabilities, the Primary and Secondary Mailbox Registers CCI instance pairs shall share the context, but the MCTP CCI within a component shall have a unique context • Events, including reading contents, clearing entries, and configuring interrupt settings IMPLEMENTATION NOTE The CXL mailbox is derived from the PCIe standard MMIO Mailbox Capability (MMB) with extensions defined in Section 8.2.9.4 for supporting CXL defined commands. Therefore, the CXL mailbox may also support PCI-SIG defined commands (MMB Command Opcode Vendor ID = 0001h) or commands defined by other entities. However, non-CXL defined commands are not reported in the CXL CEL and discovery of those commands is outside of the scope of this specification. CXL components that need to be compatible with non-CXL aware software may advertise both the CXL Primary Mailbox (Vendor ID = 1E98h or 0000h, ID = 0002h) and the PCIe MMB (Vendor ID = 0001h, ID = 0001h). However, they are required to alias the PCIe MMB header to the CXL Primary Mailbox registers. Refer to Section 8.2.9, Figure 8-12. CXL components that do not need to be compatible with non-CXL aware software should only advertise the CXL Primary Mailbox and not the PCIe MMB.

</td><td style="background-color:#e8e8e8">

实现注：Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-20-1"></a>
#### 9.20.（参见英文原文了解完整实现细节）

</td></tr>
<tr><td>

Reset, Initialization, Configuration, and Manageability

</td><td style="background-color:#e8e8e8">

复位、初始化、配置与管理功能

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


<a id="sec-9-20-2"></a>
#### 9.20.2 MCTP-based CCI Properties | MCTP-based CCI Properties

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CCI command timeout is 2 seconds, measured from when the command has been received by the component to when the component has started to transmit its response. Components should respond within this time limit; otherwise, requesters may timeout. Requesters must account for round-trip transmission time in addition to the command timeout. MCTP-based CCIs report background operation status using the Background Operation Status command as defined in Section 8.2.10.1.2. In the event of a command timeout, the requester may retransmit the request. New Message Tags shall be used every time that a request is retransmitted. Requesters may discard responses that arrive after the command timeout period has lapsed. Commands sent to MCTP-based CCIs on MLD components are processed by the FM- owned LD. § § IMPLEMENTATION NOTE It is recommended that components with multiple CCIs that support commands that run as Background Operations only advertise support for those commands on one CCI. Coordination between management entities attempting concurrent commands over separate CCIs that have component-level impact (e.g., FW update, etc.) is beyond the scope of this specification. IMPLEMENTATION NOTE MCTP-based CCIs are intended to provide a dedicated management interface that operates independently from the state of any of the component’s CXL interfaces; it is strongly recommended, but not required, that commands initiated on MCTP-based CCIs are not interrupted by Conventional Resets or any other changes of state of a component’s CXL interface(s).

</td><td style="background-color:#e8e8e8">

实现注：Reset, Initialization, Configuration, and Manageability

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章目录)


---
