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
