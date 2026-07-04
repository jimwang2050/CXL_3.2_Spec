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
### 9.13.3 Dynamic Capacity Device (DCD) | 动态容量设备 (DCD)

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

Dynamic Capacity is a feature of a CXL memory device that allows memory capacity to change dynamically without the need for resetting the device. A DCD is a CXL memory device that implements Dynamic Capacity. Unlike a traditional DPA range that a CXL memory device might support, a Dynamic Capacity DPA range is subdivided into 1 to 8 DC Regions, each of which is subdivided by the DCD into a number of fixed-size blocks, referred to as DC blocks. The host software is expected to program the maximum potential capacity utilizing one or more HDM decoders to span the entire DPA range of all configured regions. The DCD controls the allocation of these DC blocks to the host and utilizes events to signal the host when changes to the allocation of these DC blocks occurs. The DCD communicates the state of these DC blocks through an Extent List that describes the starting DPA and length of all DC blocks the host can access.

</td><td style="background-color:#e8e8e8">

动态容量 (Dynamic Capacity) 是 CXL 内存设备的一项功能，允许内存容量在无需复位设备的情况下动态更改。DCD 是实现 Dynamic Capacity 的 CXL 内存设备。与 CXL 内存设备可能支持的传统 DPA Range 不同，Dynamic Capacity DPA Range 被细分为 1 至 8 个 DC Region，每个 DC Region 由 DCD 进一步细分为若干个固定大小的块，称为 DC Block。主机软件应编程最大潜在容量，利用一个或多个 HDM Decoder 跨越所有已配置 Region 的整个 DPA Range。DCD 控制这些 DC Block 向主机的分配，并利用事件 (Event) 在这些 DC Block 的分配发生变更时通知主机。DCD 通过 Extent List (范围列表) 传达这些 DC Block 的状态，该列表描述了主机可访问的所有 DC Block 的起始 DPA 和长度。

</td></tr>

<tr><td>

The Extent List does not contain extents that are still pending acceptance from the host via the Add Dynamic Capacity Response command (see Section 8.2.10.9.9.3). Similarly, the Extent List does contain extents that are still pending release acceptance from the host via the Release Dynamic Capacity command (see Section 8.2.10.9.9.4).

</td><td style="background-color:#e8e8e8">

Extent List 不包含尚待主机通过 Add Dynamic Capacity Response 命令 (见第 8.2.10.9.9.3 节) 接受的 Extent。类似地，Extent List 确实包含尚待主机通过 Release Dynamic Capacity 命令 (见第 8.2.10.9.9.4 节) 接受释放的 Extent。

</td></tr>

<tr><td>

Dynamic Capacity is organized into 1 to 8 DC Regions as defined by the device. Each DC Region has a unique maximum potential capacity, supported block size, and memory attributes. Regions are used in increasing-DPA order, with Region 0 being used for the lowest DPA of Dynamic Capacity and Region 7 for the highest DPA. The DCD controls which DPA range it assigns to each region for each host. The DPA ranges exposed by the device to each host are independent of one another.

</td><td style="background-color:#e8e8e8">

Dynamic Capacity 按照设备定义组织为 1 至 8 个 DC Region。每个 DC Region 具有唯一的最大潜在容量、支持的 Block Size 和内存属性。Region 按递增 DPA 顺序使用，Region 0 用于 Dynamic Capacity 的最低 DPA，Region 7 用于最高 DPA。DCD 控制为每个主机的每个 Region 分配哪个 DPA Range。设备向每个主机暴露的 DPA Range 彼此独立。

</td></tr>

<tr><td>

If the host issues a read to a DPA that is not allocated to the host, the device behavior is specified in Table 8-27. If the host issues a write to a DPA that is not allocated to the host, the device shall drop the write and send an NDR (see Section 3.3.9) as a response. If the host issues a write to any DPA in a read-only DC Region, the device shall drop the write and send an NDR as a response.

</td><td style="background-color:#e8e8e8">

如果主机对未分配给该主机的 DPA 发出读操作，设备行为在表 8-27 中规定。如果主机对未分配给该主机的 DPA 发出写操作，设备应丢弃该写操作并发送 NDR (见第 3.3.9 节) 作为响应。如果主机对只读 DC Region 中的任何 DPA 发出写操作，设备应丢弃该写操作并发送 NDR 作为响应。

</td></tr>

<tr><td>

The attributes associated with each region are described in the device's CDAT. The device associates each supported region with a specific DSMAS instance so the host can determine the memory attributes associated with each given region. A device that supports Dynamic Capacity shall report its configured regions in one or more CDAT DSMAS structures and shall set the Dynamic Capacity DSMAS Flag in each structure to indicate a Dynamic Capacity supported range. When reporting the region configuration, the DCD shall supply the DSMAD Handle with which each region is associated. Devices that instantiate multiple LDs, including MLDs and Multi-Headed devices, share certain region configuration parameters, as defined in Table 7-67, across all LDs in that device.

</td><td style="background-color:#e8e8e8">

每个 Region 关联的属性在设备的 CDAT 中描述。设备将每个受支持的 Region 与特定的 DSMAS 实例相关联，以便主机能够确定每个给定 Region 关联的内存属性。支持 Dynamic Capacity 的设备应在一个或多个 CDAT DSMAS 结构中报告其已配置的 Region，并应在每个结构中设置 Dynamic Capacity DSMAS Flag 以指示 Dynamic Capacity 支持的范围。在报告 Region 配置时，DCD 应提供每个 Region 关联的 DSMAD Handle。实例化多个 LD 的设备 (包括 MLD 和 Multi-Headed 设备) 在该设备的所有 LD 之间共享某些 Region 配置参数，如表 7-67 中所定义。

</td></tr>

<tr><td>

The basic sequence to utilize Dynamic Capacity include: * Utilize Get Supported Logs sub-list (see Section 8.2.10.5.6) or Get Supported Logs (see Section 8.2.10.5.1) and Get Log (see Section 8.2.10.5.2) to retrieve the Command Effects Log (CEL). Verify that the necessary Dynamic Capacity commands are returned in the CEL, indicating Dynamic Capacity is supported by the device.

</td><td style="background-color:#e8e8e8">

使用 Dynamic Capacity 的基本序列包括：* 利用 Get Supported Logs sub-list (见第 8.2.10.5.6 节) 或 Get Supported Logs (见第 8.2.10.5.1 节) 以及 Get Log (见第 8.2.10.5.2 节) 检索 Command Effects Log (CEL)。验证必要的 Dynamic Capacity 命令在 CEL 中返回，表明 Dynamic Capacity 受该设备支持。

</td></tr>

<tr><td>

* Issue Get Dynamic Capacity Configuration command: The device reports its number of available regions and each region's base address, length, block size, and DSMAD Handle (see Section 8.2.10.9.9.1). * Program the HDM decoders appropriately for each region's base and length from Get Dynamic Capacity Configuration data. The host may utilize one or more HDM decoders to span the current configuration of Dynamic Capacity reported by the device. It is strongly recommended that the host provide adequate decoder size to cover all of the regions that are enabled. If not, the host may not be able to accept some of the Add Dynamic Capacity offers from the DCD. * Retrieve the initial Extent List with one or more calls to Get Dynamic Capacity Extent List (see Section 8.2.10.9.9.2). If the list contains extents, then that memory can be utilized immediately.

</td><td style="background-color:#e8e8e8">

* 发出 Get Dynamic Capacity Configuration 命令：设备报告其可用 Region 的数量以及每个 Region 的基地址、长度、Block Size 和 DSMAD Handle (见第 8.2.10.9.9.1 节)。* 根据 Get Dynamic Capacity Configuration 数据为每个 Region 的基址和长度适当地编程 HDM Decoder。主机可利用一个或多个 HDM Decoder 来跨越设备报告的 Dynamic Capacity 当前配置。强烈建议主机提供足够的 Decoder 大小以覆盖所有已启用的 Region。否则，主机可能无法接受来自 DCD 的某些 Add Dynamic Capacity 提议。* 通过一次或多次调用 Get Dynamic Capacity Extent List (见第 8.2.10.9.9.2 节) 检索初始 Extent List。如果列表包含 Extent，则该内存可立即使用。

</td></tr>

<tr><td>

The basic sequence to add Dynamic Capacity to a host: * The DCD adds an Add Capacity Event Record (see Section 8.2.10.2.1.6) to the device's Dynamic Capacity Event Log containing the extent of the capacity being added, sets the Dynamic Capacity Event Log bit in the Event Status register and, if enabled, generates an interrupt to alert the host to the new event record. The DCD does this for each extent in the Add Capacity operation being performed, using the More flag as necessary (see Table 8-62), avoiding overflow, and allowing the host to consume the events as necessary to complete the operation. If the Dynamic Capacity Event Log overflows at any point, the host shall utilize Get Dynamic Capacity Extent List to retrieve the current list of host accessible DC blocks. * When the host software retrieves the Add Capacity event record containing the extent of the capacity to be added, it responds back to the device with the updated extent for the exact capacity it added with a single call to Add Dynamic Capacity Response (see Section 8.2.10.9.9.3). This allows the host to control exactly how much of the added capacity it wishes to utilize, which may be less than the amount of capacity sent in the add capacity event, or even 0. * If supported by the device, the host may utilize Get Poison List or Scan Media with the Starting DPA and Length of the added capacity extent to check for poisoned addresses.

</td><td style="background-color:#e8e8e8">

向主机添加 Dynamic Capacity 的基本序列：* DCD 向设备的 Dynamic Capacity Event Log 中添加一条 Add Capacity Event Record (见第 8.2.10.2.1.6 节)，其中包含正在添加的容量 Extent，设置 Event Status 寄存器中的 Dynamic Capacity Event Log 位，并在已使能的情况下生成中断以提醒主机有新的 Event Record。DCD 对正在执行的 Add Capacity 操作中的每个 Extent 执行此操作，根据需要利用 More Flag (见表 8-62)，避免溢出，并允许主机根据需要消费事件以完成操作。如果 Dynamic Capacity Event Log 在任何时刻溢出，主机应利用 Get Dynamic Capacity Extent List 检索主机可访问的 DC Block 的当前列表。* 当主机软件检索到包含待添加容量 Extent 的 Add Capacity Event Record 时，它通过单次调用 Add Dynamic Capacity Response (见第 8.2.10.9.9.3 节) 向设备回复更新后的 Extent，以获取其添加的确切容量。这使主机能够精确控制其希望使用的添加容量数量，该数量可小于 Add Capacity Event 中发送的容量数量，甚至可为 0。* 如果设备支持，主机可利用 Get Poison List 或 Scan Media，使用添加的容量 Extent 的起始 DPA 和长度来检查是否存在中毒地址 (Poisoned Address)。

</td></tr>

<tr><td>

The basic sequence to release Dynamic Capacity from a host: * The DCD adds a Release Capacity Event Record to the device's Dynamic Capacity Event Log (see Section 8.2.10.2.1.6) containing the extent of the capacity it is requesting to be released, sets the Dynamic Capacity Event Log bit in the Event Status register and, if enabled, generates an interrupt to alert the host to the new event record. The DCD does this for each extent in the Release Capacity operation being performed, using the More flag as necessary (see Table 8-62), avoiding overflow, and allowing the host to consume the events as necessary to complete the operation. If the Dynamic Capacity Event Log overflows at any point, the host shall utilize Get Dynamic Capacity Extent List to retrieve the current list of host accessible DC blocks. * When the host software retrieves the Release Capacity event record containing the extent of the capacity to be released, the host software releases some or all of the capacity from use and responds back to the device with the updated Extent List for the exact capacity it released using the Release Dynamic Capacity command (see Section 8.2.10.9.9.4). If desired, the host may choose to make unavailable the contents of the capacity being released by whatever means it chooses, including but not limited to issuing the Sanitize or Secure Erase commands, if supported by the device, before the Release Dynamic Capacity command. The host may call Release Dynamic Capacity multiple times, returning different portions of the total capacity over time, in response to the Release Capacity event record. This allows the host to control exactly how much of the released capacity it wishes to release and when it is released.

</td><td style="background-color:#e8e8e8">

从主机释放 Dynamic Capacity 的基本序列：* DCD 向设备的 Dynamic Capacity Event Log 中添加一条 Release Capacity Event Record (见第 8.2.10.2.1.6 节)，其中包含其请求释放的容量 Extent，设置 Event Status 寄存器中的 Dynamic Capacity Event Log 位，并在已使能的情况下生成中断以提醒主机有新的 Event Record。DCD 对正在执行的 Release Capacity 操作中的每个 Extent 执行此操作，根据需要利用 More Flag (见表 8-62)，避免溢出，并允许主机根据需要消费事件以完成操作。如果 Dynamic Capacity Event Log 在任何时刻溢出，主机应利用 Get Dynamic Capacity Extent List 检索主机可访问的 DC Block 的当前列表。* 当主机软件检索到包含待释放容量 Extent 的 Release Capacity Event Record 时，主机软件释放部分或全部容量，并使用 Release Dynamic Capacity 命令 (见第 8.2.10.9.9.4 节) 向设备回复其所释放的确切容量的更新后 Extent List。如有需要，主机可选择以其选择的任何方式——包括但不限于在 Release Dynamic Capacity 命令之前发出 Sanitize 或 Secure Erase 命令 (如果设备支持)——使正被释放的容量的内容不可用。主机可多次调用 Release Dynamic Capacity，随时间推移返回总容量的不同部分，以响应 Release Capacity Event Record。这使主机能够精确控制其希望释放的容量数量以及释放的时间。

</td></tr>

<tr><td>

Prior to issuing Release Dynamic Capacity command, the host software is required to off-line the capacity and complete the necessary coherence management actions.

</td><td style="background-color:#e8e8e8">

在发出 Release Dynamic Capacity 命令之前，主机软件需将容量下线 (off-line) 并完成必要的一致性管理操作。

</td></tr>

<tr><td>

The basic sequence to release Dynamic Capacity asynchronously from a host (not associated with an event from the device): * The host may release Dynamic Capacity back to the device, at any time, without receiving a Release Capacity Event Record by calling Release Dynamic Capacity (see Section 8.2.10.9.9.4) with an Extent List containing specific released capacity.

</td><td style="background-color:#e8e8e8">

从主机异步释放 Dynamic Capacity (不与来自设备的事件关联) 的基本序列：* 主机可在任何时间将 Dynamic Capacity 释放回设备，而无需接收 Release Capacity Event Record，方法是通过调用 Release Dynamic Capacity (见第 8.2.10.9.9.4 节)，提供包含特定已释放容量的 Extent List。

</td></tr>

<tr><td>

Devices may forcefully release Dynamic Capacity from a host: * Host access to the released capacity may be immediately disabled and the DCD behaves as if the capacity is no longer allocated to the host. The DCD adds a Forced Capacity Release Event Record to the device's Dynamic Capacity Event Log containing the extent of the capacity being released, sets the Dynamic Capacity Event Log bit in the Event Status Register and, if enabled, generates an interrupt to alert the host to the new event record. If the Dynamic Capacity Event Log overflows at any point, the forced removal still occurs and the host shall utilize Get Dynamic Capacity Extent List to retrieve a new list of host accessible DC blocks.

</td><td style="background-color:#e8e8e8">

设备可强制从主机释放 Dynamic Capacity：* 对已释放容量的主机访问可能被立即禁用，DCD 的行为如同该容量不再分配给该主机。DCD 向设备的 Dynamic Capacity Event Log 中添加一条 Forced Capacity Release Event Record，其中包含正在释放的容量 Extent，设置 Event Status Register 中的 Dynamic Capacity Event Log 位，并在已使能的情况下生成中断以提醒主机有新的 Event Record。如果 Dynamic Capacity Event Log 在任何时刻溢出，强制移除仍会发生，主机应利用 Get Dynamic Capacity Extent List 检索主机可访问的 DC Block 的新列表。

</td></tr>

<tr><td>

LD-FAM based DCD shall forcefully release any shared Dynamic Capacity associated with an LD upon a Conventional Reset or a CXL Reset of that LD. MH-SLD or MH-MLD based DCD shall forcefully release shared Dynamic Capacity associated with all associated hosts upon a Conventional Reset of a head. LD-FAM based DCD shall forcefully release shared Dynamic Capacity associated with all associated hosts upon a Conventional Reset of the entire DCD. No Forced Capacity Release Event Record is created when capacity is released as a result of a reset and all entries in the Dynamic Capacity Event Log shall be cleared by the DCD.

</td><td style="background-color:#e8e8e8">

基于 LD-FAM 的 DCD 应在该 LD 的 Conventional Reset 或 CXL Reset 时强制释放与该 LD 关联的任何共享 Dynamic Capacity。基于 MH-SLD 或 MH-MLD 的 DCD 应在一个 Head 的 Conventional Reset 时强制释放与所有关联主机关联的共享 Dynamic Capacity。基于 LD-FAM 的 DCD 应在整个 DCD 的 Conventional Reset 时强制释放与所有关联主机关联的共享 Dynamic Capacity。当容量由于复位而被释放时，不创建 Forced Capacity Release Event Record，且 DCD 应清除 Dynamic Capacity Event Log 中的所有条目。

</td></tr>

<tr><td>

The host retrieves the Release Capacity event record containing the extent of the capacity that has been released. The host may respond back to the device with the updated Extent List for the released capacity using the Release Dynamic Capacity command. The host may call Release Dynamic Capacity multiple times, returning different portions of the total capacity over time. Host responses to this event are optional and shall not influence the device's release of the capacity.

</td><td style="background-color:#e8e8e8">

主机检索包含已释放容量 Extent 的 Release Capacity Event Record。主机可使用 Release Dynamic Capacity 命令向设备回复已释放容量的更新后 Extent List。主机可多次调用 Release Dynamic Capacity，随时间推移返回总容量的不同部分。主机对此事件的响应为可选的，且不应影响设备对该容量的释放。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-13-3-1"></a>
### 9.13.3.1 DCD Management By FM | FM 对 DCD 的管理

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

LD-FAM DCDs implement multiple LDs to support multiple host interfaces and can dynamically assign and reassign memory capacity among those LDs. All G-FAM Devices (GFDs) are DCDs since GFDs exclusively use Dynamic Capacity mechanisms for their capacity management.

</td><td style="background-color:#e8e8e8">

基于 LD-FAM 的 DCD 实现多个 LD 以支持多个主机接口，并可在这些 LD 之间动态分配和重新分配内存容量。所有 G-FAM Device (GFD) 都是 DCD，因为 GFD 完全使用 Dynamic Capacity 机制进行容量管理。

</td></tr>

<tr><td>

The FM is responsible for discovering a DCD's capabilities and for configuring memory assignment. 1. The FM issues Get DCD Info (see Section 7.6.7.6.1) to discover the number of supported hosts, supported features, and dynamic memory capacity. The current assignment of capacity to a specific host is queried with Get Host DC Region Configuration and Get DC Region Extent Lists (see Section 7.6.7.6.2 and Section 7.6.7.6.4, respectively). See Section 8.2.10.9.10 for the equivalent GFD commands. 2. Resources are assigned to each host using Initiate Dynamic Capacity Add and Initiate Dynamic Capacity Release (see Section 7.6.7.6.5 and Section 7.6.7.6.6, respectively). The device generates a Dynamic Capacity Event Record (see Section 8.2.10.9.9.4) to notify the FM of any host responses. See Section 7.7.2 and Section 7.7.14 for the equivalent GFD commands and policies.

</td><td style="background-color:#e8e8e8">

FM 负责发现 DCD 的能力并配置内存分配。1. FM 发出 Get DCD Info (见第 7.6.7.6.1 节) 以发现支持的主机数量、支持的功能和动态内存容量。通过 Get Host DC Region Configuration 和 Get DC Region Extent Lists (分别见第 7.6.7.6.2 节和第 7.6.7.6.4 节) 查询当前分配给特定主机的容量。等效的 GFD 命令见第 8.2.10.9.10 节。2. 使用 Initiate Dynamic Capacity Add 和 Initiate Dynamic Capacity Release (分别见第 7.6.7.6.5 节和第 7.6.7.6.6 节) 为每个主机分配资源。设备生成 Dynamic Capacity Event Record (见第 8.2.10.9.9.4 节) 以通知 FM 任何主机响应。等效的 GFD 命令和策略见第 7.7.2 节和第 7.7.14 节。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-13-3-2"></a>
### 9.13.3.2 Setting up Memory Sharing | 设置内存共享

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

The FM may use the following sequence to set up sharing between hosts, where all hosts are able to read and write to the shared capacity: 1. Issue Initiate Dynamic Capacity Add Request with the Selection Policy set to Free or Contiguous or Prescriptive with the Host ID associated with the first host. The region number must correspond to a region that is advertised as sharable. 2. If the above request is successful as indicated by a new Add Capacity Response event in the Dynamic Capacity Event record, issue Initiate Dynamic Capacity Add Request with Selection Policy=Enable Shared access with the Host ID associated with the second host. The Tag field must match the Tag value used in step 1. 3. Repeat step 2 for any other hosts that need to share this memory range.

</td><td style="background-color:#e8e8e8">

FM 可使用以下序列在主机之间建立共享，其中所有主机均可对共享容量进行读写：1. 发出 Initiate Dynamic Capacity Add Request，将 Selection Policy 设置为 Free 或 Contiguous 或 Prescriptive，并使用与第一个主机关联的 Host ID。Region 编号必须对应一个通告为可共享 (Sharable) 的 Region。2. 如果上述请求成功 (如 Dynamic Capacity Event Record 中出现新的 Add Capacity Response 事件所示)，则发出 Initiate Dynamic Capacity Add Request，Selection Policy = Enable Shared Access，并使用与第二个主机关联的 Host ID。Tag 字段必须与步骤 1 中使用的 Tag 值匹配。3. 对任何其他需要共享此内存范围的主机，重复步骤 2。

</td></tr>

<tr><td>

The FM may use the following example sequence to allocate a set of tagged capacity and allow it to be initialized by a host and then shared with one or more hosts as read-only. 1. Issue Initiate Dynamic Capacity Add Request with the Selection Policy set to Free or Contiguous or Prescriptive with the Host ID associated with the first host. The region number must correspond to a region that is advertised as writable and sharable. 2. If the above request is successful, the tagged shared capacity can be initialized by the first host. 3. Issue a Dynamic Capacity Add Reference Request for the tag associated with the capacity. Holding this Reference prevents the tagged capacity from being freed and sanitized in step 4. 4. After the first host has initialized the tagged shared capacity, issue an Initiate Dynamic Capacity Release Request for the tag associated with the capacity, and then await completion. 5. If the request in step 4 is successful as indicated by a new Release Capacity Response event in the Dynamic Capacity Event record, the capacity associated with the Tag is preserved but not mapped to any hosts. 6. Issue an Initiate Dynamic Capacity Add Request with Selection Policy=Enable Shared Access with the Host ID associated with the second host, specifying a Region that is Sharable and read-only. The Tag field must match the Tag value used in step 1. 7. Repeat step 5 for any other hosts that need to share the tagged capacity. 8. Issue a Dynamic Capacity Remove Reference Request to remove the FM reference to the tagged capacity. 9. To withdraw the shared capacity, issue a Initiate Dynamic Capacity Release command for each host. 10. When the tagged capacity has been released from all hosts, if the FM does not hold a reference, the tagged capacity will be sanitized (if appropriate) and freed, at which point the tag no longer exists and the capacity is available for future use.

</td><td style="background-color:#e8e8e8">

FM 可使用以下示例序列分配一组带标签 (Tagged) 的容量，允许其由一个主机初始化，然后以一个或多个主机只读方式共享。1. 发出 Initiate Dynamic Capacity Add Request，将 Selection Policy 设置为 Free 或 Contiguous 或 Prescriptive，并使用与第一个主机关联的 Host ID。Region 编号必须对应一个通告为可写且可共享 (Writable and Sharable) 的 Region。2. 如果上述请求成功，则由第一个主机初始化带标签的共享容量。3. 针对与该容量关联的 Tag 发出 Dynamic Capacity Add Reference Request。持有此 Reference 可防止带标签的容量在步骤 4 中被释放和清除 (Sanitized)。4. 在第一个主机完成对带标签共享容量的初始化后，针对与该容量关联的 Tag 发出 Initiate Dynamic Capacity Release Request，然后等待完成。5. 如果步骤 4 中的请求成功 (如 Dynamic Capacity Event Record 中出现新的 Release Capacity Response 事件所示)，则与该 Tag 关联的容量被保留但未映射到任何主机。6. 发出 Initiate Dynamic Capacity Add Request，Selection Policy = Enable Shared Access，使用与第二个主机关联的 Host ID，指定一个可共享且只读 (Sharable and Read-Only) 的 Region。Tag 字段必须与步骤 1 中使用的 Tag 值匹配。7. 对任何其他需要共享该带标签容量的主机，重复步骤 5。8. 发出 Dynamic Capacity Remove Reference Request 以移除 FM 对该带标签容量的 Reference。9. 要撤回共享容量，对每个主机发出 Initiate Dynamic Capacity Release 命令。10. 当带标签的容量已从所有主机释放后，如果 FM 未持有 Reference，则该带标签的容量将被清除 (如适用) 并释放，此时该 Tag 不再存在，容量可供将来使用。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-13-3-3"></a>
### 9.13.3.3 Extent List Tracking | Extent List 跟踪

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

The storage of extent list information, including individual extents and their associated tags, consumes resources in a DCD. As such, DCDs are permitted to limit the number of extents and number of tags of which they are capable of tracking. This capability is reported in a DCD's Get Host DC Region Configuration and Get Dynamic Capacity Configuration responses.

</td><td style="background-color:#e8e8e8">

Extent List 信息的存储，包括各个 Extent 及其关联的 Tag，会消耗 DCD 中的资源。因此，允许 DCD 限制其能够跟踪的 Extent 数量和 Tag 数量。此能力在 DCD 的 Get Host DC Region Configuration 和 Get Dynamic Capacity Configuration 响应中报告。

</td></tr>

<tr><td>

A DCD is responsible for tracking all extents and tags that comprise extent lists in the following states: * Pending: Defining capacity specified in an Initiate Dynamic Capacity Add request that has not been responded to by a host. This includes extents that form part of Dead Extent Groups, those that have been Force Removed whilst in pending state. * Added: Defining capacity that has been accepted by a host as part of an Add Dynamic Capacity request and is present in the extent list returned to the host in the response to a Get Dynamic Capacity Extent List request * FM-referenced: Defining capacity to which an FM reference has been added, as reported by the FM Holds Reference bit in the response to Dynamic Capacity List Tags

</td><td style="background-color:#e8e8e8">

DCD 负责跟踪构成 Extent List 的、处于以下状态的所有 Extent 和 Tag：* Pending (待定)：定义在 Initiate Dynamic Capacity Add 请求中指定、但尚未得到主机响应的容量。这包括构成 Dead Extent Group 的 Extent，以及那些在 Pending 状态下被 Force Remove 的 Extent。* Added (已添加)：定义已被主机作为 Add Dynamic Capacity 请求的一部分接受、并在响应 Get Dynamic Capacity Extent List 请求时返回给主机的 Extent List 中存在的容量。* FM-referenced (FM 引用)：定义已添加 FM Reference 的容量，如 Dynamic Capacity List Tags 响应中的 FM Holds Reference 位所报告。

</td></tr>

<tr><td>

A DCD reports its Number of Available Extents and Number of Available Tags as its total capacity minus all extents and tags tracked for capacity in the Pending, Added, and FM-referenced states, respectively.

</td><td style="background-color:#e8e8e8">

DCD 报告其 Number of Available Extents 和 Number of Available Tags，分别为其总容量减去在 Pending、Added 和 FM-referenced 状态下为容量跟踪的所有 Extent 和 Tag。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-13-4"></a>
### 9.13.4 Capacity or Performance Degradation | 容量或性能降级

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

A CXL device may detect an unrecoverable error during its initialization and may be able to operate with a reduced capacity or reduced performance. If this failure results in capacity degradation and it is detected prior to Memory_Info_Valid=1, the device shall update the Memory_Size fields in the corresponding DVSEC CXL Range Size registers (see Section 8.1.3.8.1, Section 8.1.3.8.2, Section 8.1.3.8.5, and Section 8.1.3.8.6), CDAT DSMAS structures, response to Identify Memory Device command, and response to Get Partition Info command to report the reduced size. It is recommended that the device also set the Memory Capacity Degraded flag in the Health Status field (see Table 8-148). If the failure results in performance degradation and it is detected prior to Memory_Info_Valid=1, the CDAT DSLBIS structure shall be updated and the Performance Degraded flag in the Health Status field (see Table 8-148) should be set. If Mem_HwInit_Mode=1, Memory_Active bit(s) shall be set when the memory range is fully initialized and available for software use. If this failure is detected after the Memory_Info_Valid bit is set, but before the Memory_Active bit is set, the device shall not set the Memory_Active bit. The device updates the CDAT in the following manner: * CDAT sequence number shall be incremented to indicate to SW that CDAT content has changed. * If the failure results in capacity degradation, the CDAT DSEMTS entries shall mark the bad memory as "EFIUnusableMemory" indicating to the SW that it shall not use the associated DPA range on this device. The Memory Capacity Degraded flag in the Health Status field (see Table 8-148) shall be set. * If the failure results in performance degradation, the CDAT DSLBIS structure shall be updated and the Performance Degraded flag in the Health Status field (see Table 8-148) shall be set. If Mem_HwInit_Mode=1, Memory_Active_Degraded shall be set when the reduced capacity is fully initialized and available for software use. The device capacity reported by Identify Memory Device (see Section 8.2.10.9.1.1) and Get Partition Info (see Section 8.2.10.9.2.1) commands shall be consistent with capacity advertised by CDAT that is not marked as EFIUnusableMemory.

</td><td style="background-color:#e8e8e8">

CXL 设备在其初始化期间可能检测到不可恢复的错误，并可能以降级容量或降级性能运行。如果此故障导致容量降级且在 Memory_Info_Valid = 1 之前被检测到，设备应更新相应 DVSEC CXL Range Size 寄存器 (见第 8.1.3.8.1 节、第 8.1.3.8.2 节、第 8.1.3.8.5 节和第 8.1.3.8.6 节) 中的 Memory_Size 字段、CDAT DSMAS 结构、对 Identify Memory Device 命令的响应以及对 Get Partition Info 命令的响应，以报告减小后的大小。建议设备同时设置 Health Status 字段 (见表 8-148) 中的 Memory Capacity Degraded 标志。如果故障导致性能降级且在 Memory_Info_Valid = 1 之前被检测到，应更新 CDAT DSLBIS 结构，并应设置 Health Status 字段 (见表 8-148) 中的 Performance Degraded 标志。如果 Mem_HwInit_Mode = 1，当内存范围完全初始化并可供软件使用时，应设置 Memory_Active 位。如果此故障在 Memory_Info_Valid 位被设置之后、但在 Memory_Active 位被设置之前被检测到，设备不应设置 Memory_Active 位。设备按以下方式更新 CDAT：* CDAT 序列号 (Sequence Number) 应递增，以向软件指示 CDAT 内容已更改。* 如果故障导致容量降级，CDAT DSEMTS 条目应将坏内存标记为 "EFIUnusableMemory"，向软件指示其不应使用此设备上关联的 DPA Range。Health Status 字段 (见表 8-148) 中的 Memory Capacity Degraded 标志应被设置。* 如果故障导致性能降级，应更新 CDAT DSLBIS 结构，且 Health Status 字段 (见表 8-148) 中的 Performance Degraded 标志应被设置。如果 Mem_HwInit_Mode = 1，当降级后的容量完全初始化并可供软件使用时，应设置 Memory_Active_Degraded。由 Identify Memory Device (见第 8.2.10.9.1.1 节) 和 Get Partition Info (见第 8.2.10.9.2.1 节) 命令报告的设备容量应与未被标记为 EFIUnusableMemory 的 CDAT 通告的容量一致。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14"></a>
### 9.14 Back-Invalidate Configuration | Back-Invalidate 配置

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

This section describes how System Software may discover whether a component supports Back-Invalidate and how BI-IDs are assigned.

</td><td style="background-color:#e8e8e8">

本节描述了系统软件如何发现组件是否支持 Back-Invalidate 以及如何分配 BI-ID。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14-1"></a>
### 9.14.1 Discovery | 发现

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

Back-Invalidate (BI) messages require the link to operate in 256B Flit mode. Alternate Protocol Negotiation flow establishes the optimal Flit mode and PCIe DVSEC for Flex Bus Port registers (see Section 8.2.1.3) identifies the negotiated Flit mode. The presence of the CXL BI Decoder Capability Structure indicates that the component is capable of supporting BI.

</td><td style="background-color:#e8e8e8">

Back-Invalidate (BI) 消息要求链路工作在 256B Flit 模式下。Alternate Protocol Negotiation 流程建立最优的 Flit 模式，PCIe DVSEC for Flex Bus Port 寄存器 (见第 8.2.1.3 节) 标识已协商的 Flit 模式。CXL BI Decoder Capability Structure 的存在表明该组件具备支持 BI 的能力。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14-2"></a>
### 9.14.2 Configuration | 配置

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

Before enabling a device to issue BI requests, System Software must ensure that the device, the host, and any switch(es) in the path are capable of BI and that the link(s) between the device and the host are operating in 256B Flit mode. BI-capable Downstream Ports and devices advertise the CXL BI Decoder Capability Structure (see Section 8.2.4.27). System Software configures them to enable BI functionality. The BI-ID of a device must be unique within a VH. This is ensured by using the device's Bus Number as the BI-ID. The Downstream Port decode functionality is described in Table 9-13 and Table 9-14.

</td><td style="background-color:#e8e8e8">

在使能设备发出 BI 请求之前，系统软件必须确保该设备、主机以及路径中的任何交换机均具备 BI 能力，且设备与主机之间的链路工作在 256B Flit 模式下。具备 BI 能力的 Downstream Port 和设备通告 CXL BI Decoder Capability Structure (见第 8.2.4.27 节)。系统软件对其进行配置以使能 BI 功能。设备的 BI-ID 在 VH 内必须唯一。这通过使用设备的 Bus Number 作为 BI-ID 来保证。Downstream Port 的解码功能在表 9-13 和表 9-14 中描述。

</td></tr>

<tr><td>

Table 9-13. Downstream Port Handling of BISnp: BI Enable=0, BI Forward=0: Discard. | BI Enable=0, BI Forward=1: Forward upstream as is. | BI Enable=1, BI Forward=0: Perform the following checks: * Locate the HDM decoder in the USP or RC that decodes the BISnp address. * Verify that the BI bit in that HDM decoder is set. * Optionally, verify that the Target Port that corresponds to the BISnp address matches the port that generated the BISnp request. If this is a DSP: * If above checks pass, Set BI-ID= Secondary Bus Number and forward upstream; otherwise, discard. If this is a root port: * If above checks pass, forward upstream; otherwise, discard. Root port may use host proprietary mechanisms to initialize BI-ID and route the associated BIRsp messages. | BI Enable=1, BI Forward=1: Discard (Invalid setting). Table 9-14. Downstream Port Handling of BIRsp: BI Enable=0, BI Forward=0: Discard. | BI Enable=0, BI Forward=1: Forward downstream as is. | BI Enable=1, BI Forward=0: If this is a DSP: * If BI-ID=Secondary Bus Number, forward downstream; otherwise, discard. If this is a root port: * Use host-specific checks to ensure correct routing of the BISnp response. Forward downstream if these checks pass; otherwise, discard. | BI Enable=1, BI Forward=1: Discard (Invalid setting).

</td><td style="background-color:#e8e8e8">

表 9-13. Downstream Port 对 BISnp 的处理：BI Enable=0, BI Forward=0：丢弃。| BI Enable=0, BI Forward=1：按原样向上游转发。| BI Enable=1, BI Forward=0：执行以下检查：* 定位 USP 或 RC 中解码该 BISnp 地址的 HDM Decoder。* 验证该 HDM Decoder 中的 BI 位已设置。* 可选地，验证与该 BISnp 地址对应的 Target Port 是否与生成该 BISnp 请求的端口匹配。如果这是 DSP：* 如果上述检查通过，设置 BI-ID = Secondary Bus Number 并向上游转发；否则丢弃。如果这是 Root Port：* 如果上述检查通过，向上游转发；否则丢弃。Root Port 可使用主机专有机制来初始化 BI-ID 并路由关联的 BIRsp 消息。| BI Enable=1, BI Forward=1：丢弃 (无效设置)。表 9-14. Downstream Port 对 BIRsp 的处理：BI Enable=0, BI Forward=0：丢弃。| BI Enable=0, BI Forward=1：按原样向下游转发。| BI Enable=1, BI Forward=0：如果这是 DSP：* 如果 BI-ID = Secondary Bus Number，向下游转发；否则丢弃。如果这是 Root Port：* 使用主机特定的检查以确保 BISnp 响应的正确路由。如果这些检查通过，向下游转发；否则丢弃。| BI Enable=1, BI Forward=1：丢弃 (无效设置)。

</td></tr>

<tr><td>

The USP in a BI-capable Switch may advertise the CXL BI Route Table capability Structure (see Section 8.2.4.26). If a USP receives an M2S BIRsp message, the USP shall look up the Port Number associated with the Bus Number that is carried in the message's BI-ID field, and then forward the message to that Port. The BI-ID is guaranteed to correspond to a valid BI-capable device, specifically the one that generated the BISnp request. If the Port Number does not match any DSP due to incorrect programming, the BIRsp message shall be dropped. If a USP receives an S2M BISnp message, the USP may look up the Port Number associated with the Bus Number that is carried in the message's BI-ID field, and then verify that the Port Number matches the Port Number of the originating DSP before forwarding the BISnp message upstream. If the Port Number derived from this structure does not match the DSP's Port Number, the BISnp message may be dropped.

</td><td style="background-color:#e8e8e8">

具备 BI 能力的 Switch 中的 USP 可通告 CXL BI Route Table Capability Structure (见第 8.2.4.26 节)。如果 USP 收到 M2S BIRsp 消息，USP 应查找与消息 BI-ID 字段中携带的 Bus Number 关联的 Port Number，然后将消息转发到该 Port。BI-ID 保证对应一个有效的、具备 BI 能力的设备，具体而言即生成该 BISnp 请求的设备。如果由于编程错误导致 Port Number 与任何 DSP 不匹配，BIRsp 消息应被丢弃。如果 USP 收到 S2M BISnp 消息，USP 可查找与消息 BI-ID 字段中携带的 Bus Number 关联的 Port Number，然后验证该 Port Number 是否与发起 DSP 的 Port Number 匹配，之后再向上游转发 BISnp 消息。如果从该结构导出的 Port Number 与 DSP 的 Port Number 不匹配，BISnp 消息可被丢弃。

</td></tr>

</tbody></table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> <table>
> <thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
> <tbody>
> <tr><td>
>
> System software may use the following sequence to configure a BI-capable Device D below a Switch S as follows: 1. Verify that all the CXL link(s) between Device D and the host are operating in 256B Flit mode. 2. Ensure the device has been assigned a valid Bus number. 3. Enable BI on the DSP of Switch S that is directly connected to Device D: a. BI Forward=0. b. BI Enable=1. 4. If the DSP's BI Decoder Capability register indicates Explicit BI Decoder Commit Required=1, commit the BI-ID changes via the following sequence: a. BI Decoder Commit=0 to rearm. b. BI Decoder Commit=1. c. Poll bits 0 and 1 of the BI Decoder Status register until timeout or one of them is set. The timeout value is reported in the BI Decoder Status register. d. If BI Decoder Committed=1, the changes were committed. Proceed to step 5. e. If BI Decoder Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 5. If the USP implements CXL BI Route Table Capability Structure and Explicit BI RT Commit Required=1, commit the BI-ID changes as follows: a. BI RT Decoder Commit=0 to rearm. b. BI RT Decoder Commit=1. c. Poll bits 0 and 1 of the BI RT Status register until timeout or one of them is set. The timeout value is reported in the BI RT Status register. d. If BI RT Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If BI RT Committed=1, the changes were committed. Proceed to step 6. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 6. If the previous steps were successful, configure the Root Port that is directly connected to Switch S to forward BI messages if it isn't already set up that way: a. If BI Forward=0, set BI Forward=1. b. Ensure BI Enable=0. 7. If the previous steps were successful, configure Device D to enable BI: a. BI Enable=1. 8. If the previous steps were successful, inform the device driver that Device D may now issue BI requests.
>
> </td><td style="background-color:#e8e8e8">
>
> 系统软件可按如下所述使用以下序列配置 Switch S 下具备 BI 能力的 Device D：1. 验证 Device D 与主机之间的所有 CXL 链路均工作在 256B Flit 模式下。2. 确保设备已被分配有效的 Bus Number。3. 在直接连接 Device D 的 Switch S 的 DSP 上使能 BI：a. BI Forward = 0。b. BI Enable = 1。4. 如果 DSP 的 BI Decoder Capability 寄存器指示 Explicit BI Decoder Commit Required = 1，通过以下序列提交 BI-ID 更改：a. BI Decoder Commit = 0 以重新就绪 (rearm)。b. BI Decoder Commit = 1。c. 轮询 BI Decoder Status 寄存器的 bit 0 和 bit 1，直到超时或其中之一被设置。超时值在 BI Decoder Status 寄存器中报告。d. 如果 BI Decoder Committed = 1，更改已提交。继续执行步骤 5。e. 如果 BI Decoder Error Not Committed = 1，更改未提交。软件应将其视为错误条件。f. 如果经过超时后两位均未设置，软件应将其视为错误条件。5. 如果 USP 实现了 CXL BI Route Table Capability Structure 且 Explicit BI RT Commit Required = 1，按如下方式提交 BI-ID 更改：a. BI RT Decoder Commit = 0 以重新就绪。b. BI RT Decoder Commit = 1。c. 轮询 BI RT Status 寄存器的 bit 0 和 bit 1，直到超时或其中之一被设置。超时值在 BI RT Status 寄存器中报告。d. 如果 BI RT Error Not Committed = 1，更改未提交。软件应将其视为错误条件。e. 如果 BI RT Committed = 1，更改已提交。继续执行步骤 6。f. 如果经过超时后两位均未设置，软件应将其视为错误条件。6. 如果前述步骤成功，且直接连接 Switch S 的 Root Port 尚未按该方式设置，则配置 Root Port 以转发 BI 消息：a. 如果 BI Forward = 0，设置 BI Forward = 1。b. 确保 BI Enable = 0。7. 如果前述步骤成功，配置 Device D 以使能 BI：a. BI Enable = 1。8. 如果前述步骤成功，通知设备驱动程序 Device D 现在可发出 BI 请求。
>
> </td></tr>
> </tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14-3"></a>
### 9.14.3 Mixed Configurations | 混合配置

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

This section describes scenarios where a BI-capable device is plugged into a system that does not support BI.

</td><td style="background-color:#e8e8e8">

本节描述了具备 BI 能力的设备插入不支持 BI 的系统的场景。

</td></tr>

</tbody></table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> <table>
> <thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
> <tbody>
> <tr><td>
>
> System software may use the following sequence to deallocate the BI-ID B that was previously assigned to Device D below Switch S as follows: 1. Notify Device D's device driver that Device D is no longer allowed to issue BI requests and then wait for acknowledgment. 2. Configure Device D to disable BI: a. BI Enable=0. 3. Configure the DSP of Switch S that is directly connected to Device D to unassign BI-ID B as follows: a. BI Forward=0. b. BI Enable=0. 4. If the DSP's CXL BI Decoder Capability register indicates Explicit BI Decoder Commit Required=1, commit the BI-ID changes as follows: a. BI Decoder Commit=0 to rearm. b. BI Decoder Commit=1. c. Poll bits 0 and 1 of the BI Decoder Status register until timeout or one of them is set. The timeout value is reported in the BI Decoder Status register. d. If BI Decoder Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If BI Decoder Committed=1, the changes were committed. Proceed to step 5. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 5. If the USP implements CXL BI Route Table Capability Structure and Explicit BI RT Commit Required=1, commit the BI-ID changes as follows: a. BI RT Commit=0 to rearm. b. BI RT Commit=1. c. Poll bits 0 and 1 of the BI RT Status register until timeout or one of them is set. The timeout value is reported in the BI RT Status register. d. If BI RT Error Not Committed=1, the changes were not committed. Software should treat this as an error condition. e. If BI RT Committed=1, the changes were committed. Proceed to step 6. f. If neither bit is set and the timeout is reached, Software should treat this as an error condition. 6. If the previous steps were successful, and no other devices in this VCS have been assigned a BI-ID, configure the Root Port that is directly connected to Switch S to stop forwarding BI messages as follows: a. BI Forward=0. Ensure BI Enable=0.
>
> </td><td style="background-color:#e8e8e8">
>
> 系统软件可按如下所述使用以下序列释放先前分配给 Switch S 下 Device D 的 BI-ID B：1. 通知 Device D 的设备驱动程序 Device D 不再被允许发出 BI 请求，然后等待确认。2. 配置 Device D 以禁用 BI：a. BI Enable = 0。3. 配置直接连接 Device D 的 Switch S 的 DSP 以取消分配 BI-ID B，如下所示：a. BI Forward = 0。b. BI Enable = 0。4. 如果 DSP 的 CXL BI Decoder Capability 寄存器指示 Explicit BI Decoder Commit Required = 1，按如下方式提交 BI-ID 更改：a. BI Decoder Commit = 0 以重新就绪。b. BI Decoder Commit = 1。c. 轮询 BI Decoder Status 寄存器的 bit 0 和 bit 1，直到超时或其中之一被设置。超时值在 BI Decoder Status 寄存器中报告。d. 如果 BI Decoder Error Not Committed = 1，更改未提交。软件应将其视为错误条件。e. 如果 BI Decoder Committed = 1，更改已提交。继续执行步骤 5。f. 如果经过超时后两位均未设置，软件应将其视为错误条件。5. 如果 USP 实现了 CXL BI Route Table Capability Structure 且 Explicit BI RT Commit Required = 1，按如下方式提交 BI-ID 更改：a. BI RT Commit = 0 以重新就绪。b. BI RT Commit = 1。c. 轮询 BI RT Status 寄存器的 bit 0 和 bit 1，直到超时或其中之一被设置。超时值在 BI RT Status 寄存器中报告。d. 如果 BI RT Error Not Committed = 1，更改未提交。软件应将其视为错误条件。e. 如果 BI RT Committed = 1，更改已提交。继续执行步骤 6。f. 如果经过超时后两位均未设置，软件应将其视为错误条件。6. 如果前述步骤成功，且此 VCS 中没有其他设备被分配了 BI-ID，配置直接连接 Switch S 的 Root Port 以停止转发 BI 消息，如下所示：a. BI Forward = 0。确保 BI Enable = 0。
>
> </td></tr>
> </tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14-3-1"></a>
### 9.14.3.1 BI-capable Type 2 Device | 具备 BI 能力的 Type 2 设备

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

If a BI-capable Type 2 device is connected to a Downstream Port that does not support 256B Flit mode, the device is able to detect this condition during the Hardware Autonomous Mode Negotiation (see Section 6.4.1.1) and fall back to another mode (e.g., Type 2 HDM-D mode or PCIe mode) based on the device vendor's policy. If a BI-capable Type 2 device is connected to a switch that supports BI, but the host does not support BI, the device cannot be operated in BI mode. In this case, the System Software or the System Firmware may choose to reconfigure the Type 2 device to operate in a fallback mode. It is legal for BI-capable Type 2 devices to not support HDM-D flow; however, such a device must support fallback to either operate as a PCIe device, Type 1 device, or a Type 3 device. These flows are described in Section 9.14.3.2. If a Type 2 device advertises support for HDM-D flow via the BI Decoder Capability register (see Section 8.2.4.27.1), the device is operated in that mode as long as the number of Type 2 devices using HDM-D flow does not exceed the host's capabilities and the CXL specification restrictions. A CXL Type 2 device that supports HDM-D flow may be unable to operate in that mode due to system configuration restrictions. In many scenarios, the device may be unable to make that determination on its own and may require assistance from System Software or System Firmware. See Section 9.14.3.2.

</td><td style="background-color:#e8e8e8">

如果具备 BI 能力的 Type 2 设备连接到不支持 256B Flit 模式的 Downstream Port，该设备能够在 Hardware Autonomous Mode Negotiation (见第 6.4.1.1 节) 期间检测到这一状况，并根据设备供应商的策略回退到另一种模式 (例如 Type 2 HDM-D 模式或 PCIe 模式)。如果具备 BI 能力的 Type 2 设备连接到支持 BI 的交换机，但主机不支持 BI，则该设备无法在 BI 模式下运行。在这种情况下，系统软件或系统固件可选择重新配置 Type 2 设备以在回退模式下运行。具备 BI 能力的 Type 2 设备不支持 HDM-D 流是合法的；然而，此类设备必须支持回退为作为 PCIe 设备、Type 1 设备或 Type 3 设备运行。这些流程在第 9.14.3.2 节中描述。如果 Type 2 设备通过 BI Decoder Capability 寄存器 (见第 8.2.4.27.1 节) 通告对 HDM-D 流的支持，只要使用 HDM-D 流的 Type 2 设备数量不超过主机的能力和 CXL 规范的限制，设备就在该模式下运行。支持 HDM-D 流的 CXL Type 2 设备可能由于系统配置限制而无法在该模式下运行。在许多场景中，设备可能无法自行做出此确定，而需要系统软件或系统固件的协助。见第 9.14.3.2 节。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14-3-2"></a>
### 9.14.3.2 Type 2 Device Fallback Modes | Type 2 设备回退模式

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

Table 9-15 describes the actions that System Software or System Firmware may take when a Type 2 device cannot be operated in either HDM-DB mode or in HDM-D mode, based on the Fallback Capability field value in the DVSEC CXL Capability2 register (see Section 8.1.3.7).

</td><td style="background-color:#e8e8e8">

表 9-15 描述了当 Type 2 设备无法在 HDM-DB 模式或 HDM-D 模式下运行时，系统软件或系统固件可基于 DVSEC CXL Capability2 寄存器 (见第 8.1.3.7 节) 中的 Fallback Capability 字段值采取的操作。

</td></tr>

<tr><td>

Table 9-15. CXL Type 2 Device Behavior in Fallback Operation Mode: Register Value 00b: The device can be operated as an RCD. If the device does not support HDM-DB flow, it supports HDM-D flow. If the device supports HDM-DB flow, it also supports HDM-D flow and must return HDM-D Capable=1 (see Section 8.2.4.27.1). If the device cannot be operated as a Type 2 device, it must be disabled. | 01b: The device supports either HDM-DB flow or HDM-D flow or both. In addition, it can operate as a PCIe device. If the device cannot be operated in either HDM-DB mode or in HDM-D mode, System Firmware or System Software may disable Alternate Protocol Negotiation by programming the DSP registers and issuing a Secondary Bus Reset so that the link comes up in PCIe mode. | 10b: The device supports either HDM-DB flow or HDM-D flow or both. In addition, it can operate as a CXL Type 1 device. If the device cannot be operated in either HDM-DB mode or in HDM-D mode, System Firmware or System Software may reconfigure the DVSEC Flex Bus Port Control register (see Section 8.2.1.3.2) in the Downstream Port above the device to not advertise CXL.mem and then issue a Secondary Bus Reset, thereby bringing up the device as a CXL Type 1 device. | 11b: The device supports either HDM-DB flow or HDM-D flow or both. In addition, it can operate as a CXL Type 3 device. If the device cannot be operated in either HDM-DB mode or in HDM-D mode, System Firmware or System Software may reconfigure the Flex Bus Port Control register (see Section 8.2.1.3.2) in the Downstream Port above the device to not advertise CXL.cache and then issue a Secondary Bus Reset, thereby bringing up the device as a CXL Type 3 device. Footnote 1: Fallback Capability field values in the DVSEC CXL Capability2 register (see Section 8.1.3.7).

</td><td style="background-color:#e8e8e8">

表 9-15. CXL Type 2 设备在回退操作模式下的行为：寄存器值 00b：设备可作为 RCD 运行。如果设备不支持 HDM-DB 流，则其支持 HDM-D 流。如果设备支持 HDM-DB 流，则其也支持 HDM-D 流且必须返回 HDM-D Capable = 1 (见第 8.2.4.27.1 节)。如果设备无法作为 Type 2 设备运行，则必须被禁用。| 01b：设备支持 HDM-DB 流或 HDM-D 流或两者均支持。此外，其可作为 PCIe 设备运行。如果设备无法在 HDM-DB 模式或 HDM-D 模式下运行，系统固件或系统软件可通过编程 DSP 寄存器并发出 Secondary Bus Reset 禁用 Alternate Protocol Negotiation，使链路以 PCIe 模式建立连接。| 10b：设备支持 HDM-DB 流或 HDM-D 流或两者均支持。此外，其可作为 CXL Type 1 设备运行。如果设备无法在 HDM-DB 模式或 HDM-D 模式下运行，系统固件或系统软件可重新配置设备上方 Downstream Port 中的 DVSEC Flex Bus Port Control 寄存器 (见第 8.2.1.3.2 节) 以不通告 CXL.mem，然后发出 Secondary Bus Reset，从而使设备作为 CXL Type 1 设备启动。| 11b：设备支持 HDM-DB 流或 HDM-D 流或两者均支持。此外，其可作为 CXL Type 3 设备运行。如果设备无法在 HDM-DB 模式或 HDM-D 模式下运行，系统固件或系统软件可重新配置设备上方 Downstream Port 中的 Flex Bus Port Control 寄存器 (见第 8.2.1.3.2 节) 以不通告 CXL.cache，然后发出 Secondary Bus Reset，从而使设备作为 CXL Type 3 设备启动。脚注 1：DVSEC CXL Capability2 寄存器 (见第 8.1.3.7 节) 中的 Fallback Capability 字段值。

</td></tr>

<tr><td>

More-complex policies, such as configuring the Device to operate in CXL.io only mode or another mode based on peer devices, are possible; however, those policies are beyond the scope of this specification.

</td><td style="background-color:#e8e8e8">

更复杂的策略是可能的，例如配置设备以仅 CXL.io 模式运行或基于对等设备 (Peer Device) 的其他模式；然而，这些策略超出了本规范的范围。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-14-3-3"></a>
### 9.14.3.3 BI-capable Type 3 Device | 具备 BI 能力的 Type 3 设备

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>

<tr><td>

A BI-capable Type 3 device is required to operate correctly when System Software has not enabled BI. In this case, the device functionality that is dependent on BI will not be available. If a BI-capable Type 3 device is connected to a Downstream Port that does not support 256B Flit mode, the device may continue to advertise BI capability via the CXL BI Decoder Capability Structure (see Section 8.2.4.27). The System Software shall ensure that the BI bit in none of the HDM decoders in the device, the switch, or the host that spans the device's HDM is set. If a BI-capable Type 3 device is present in a system where the host does not support BI, the System Software shall ensure that the BI bit in none of the HDM decoders in the device, the switch, or the host that spans the device's HDM is set. In both cases, the System Software is responsible for ensuring that the BI bit in the CXL BI Decoder Control register (see Section 8.2.4.27.2) in the device, as well as the Downstream Port it is connected to, is programmed to 0.

</td><td style="background-color:#e8e8e8">

具备 BI 能力的 Type 3 设备被要求在系统软件未使能 BI 时正确运行。在这种情况下，依赖于 BI 的设备功能将不可用。如果具备 BI 能力的 Type 3 设备连接到不支持 256B Flit 模式的 Downstream Port，设备可继续通过 CXL BI Decoder Capability Structure (见第 8.2.4.27 节) 通告 BI 能力。系统软件应确保设备、交换机或主机中跨越该设备 HDM 的任何 HDM Decoder 中的 BI 位均未被设置。如果具备 BI 能力的 Type 3 设备存在于主机不支持 BI 的系统中，系统软件应确保设备、交换机或主机中跨越该设备 HDM 的任何 HDM Decoder 中的 BI 位均未被设置。在两种情况下，系统软件均负责确保设备中以及其所连接的 Downstream Port 中的 CXL BI Decoder Control 寄存器 (见第 8.2.4.27.2 节) 中的 BI 位编程为 0。

</td></tr>

</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

*Generated: translated sections 9.13.3 through 9.14.3.3 of the CXL 3.2 Specification (Chapter 9).*

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-15"></a>
### 9.15 Cache ID Configuration and Routing | Cache ID 配置与路由

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CXL 3.0 specification introduces protocol enhancements that allow for more than one active CXL.cache agent per VCS. The identity of the CXL.cache agent is carried via the CacheID field in the CXL.cache messages. If the CXL link is operating in 256B Flit mode, the CXL.cache messages can carry 4 CacheID bits. Before enabling more than one CXL.cache device per VCS, Software must ensure that the host and any switch(es) in the path advertise the CXL Cache ID Decoder Capability Structure, and that all the link(s) between the lowest-level switch and the host are operating in 256B Flit mode. Downstream Ports advertise the CXL Cache ID Decoder Capability structure to indicate that the Downstream Ports can assign and decode the CacheID field in CXL.cache messages (see Section 8.2.4.29). Software configures the Downstream Ports to enable CacheID forwarding functionality and assign a CacheID to the device. The CacheID must be unique within a VH and must account for the constraints placed by the Flit mode and the host capabilities. Any CXL.cache device can operate correctly in a system that is capable of supporting more than one active CXL.cache agent per VCS; however, System Firmware or System Software that is aware of this new capability and capable of correctly configuring the switch and/or host is required to take advantage of this capability.

</td><td style="background-color:#e8e8e8">

CXL 3.0 规范引入了协议增强，允许每个 VCS 中存在多个活动的 CXL.cache 代理。CXL.cache 代理的身份通过 CXL.cache 消息中的 CacheID 字段承载。若 CXL 链路以 256B Flit 模式运行，则 CXL.cache 消息可携带 4 个 CacheID 位。在启用每个 VCS 中多个 CXL.cache 设备之前，软件必须确保主机及路径中的任何交换机通告了 CXL Cache ID Decoder Capability Structure，并且最底层交换机与主机之间的所有链路均以 256B Flit 模式运行。下行端口通告 CXL Cache ID Decoder Capability 结构，以指示该下行端口能够分配和解码 CXL.cache 消息中的 CacheID 字段（参见第 8.2.4.29 节）。软件配置下行端口以启用 CacheID 转发功能并为设备分配一个 CacheID。CacheID 在同一个 VH 内必须唯一，并且必须考虑到 Flit 模式和主机能力所施加的约束。任何 CXL.cache 设备都可以在能够支持每个 VCS 多个活动 CXL.cache 代理的系统中正常运行；然而，要利用这一能力，需要了解此新功能且能够正确配置交换机和/或主机的系统固件或系统软件。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-15-1"></a>
### 9.15.1 Host Capabilities | 主机能力

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The host requires dedicated resources to track each CacheID source. As such, it is necessary to account for host constraints when assigning CacheID. The host constraints are expressed in terms of the total number of CacheIDs that the host can track per CXL Host Bridge. This information is conveyed via the Cache ID Target Count field in the CXL Cache ID Route Table Capability register (see Section 8.2.4.28.1) associated with the Host Bridge.

</td><td style="background-color:#e8e8e8">

主机需要专用资源来跟踪每一个 CacheID 源。因此，在分配 CacheID 时必须考虑主机约束。主机约束以每个 CXL Host Bridge 可跟踪的 CacheID 总数来表示。此信息通过 CXL Cache ID Route Table Capability 寄存器中与 Host Bridge 相关联的 Cache ID Target Count 字段来传递（参见第 8.2.4.28.1 节）。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-15-2"></a>
### 9.15.2 Downstream Port Decode Functionality | 下行端口解码功能

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Downstream Port decode functionality is described in Table 9-16 and Table 9-17. The associated registers are defined in Section 8.2.4.14.

</td><td style="background-color:#e8e8e8">

下行端口解码功能在表 9-16 和表 9-17 中描述。相关寄存器在第 8.2.4.14 节中定义。

</td></tr>
<tr><td>

In addition to the checks documented in Table 9-16, the root port shall implement the following steps before forwarding the message upstream: • If HDM-D Type 2 Device Present=1, compare CacheID with the HDM-D Type 2 Device Cache ID field. If there is a match, identify this device as a Type 2 device that is using HDM-D flows. The host shall follow the HDM-D flows when responding to this device, which includes enforcing the setting in the CXL.cache Trust Level field of the Root Port Security Policy register (see Table 8-29). • If the Requester is using HDM-DB flows, abort the request if Block CXL.cache HDM-DB=1. D2H response messages and D2H data messages do not carry CacheID and are always routed back to the host.

</td><td style="background-color:#e8e8e8">

除表 9-16 中记录的检查项外，根端口在向上游转发消息之前还应实现以下步骤：• 若 HDM-D Type 2 Device Present=1，则将 CacheID 与 HDM-D Type 2 Device Cache ID 字段进行比较。若匹配，则将该设备标识为正在使用 HDM-D 流的 Type 2 设备。主机在响应该设备时应遵循 HDM-D 流，其中包括强制执行 Root Port Security Policy 寄存器中 CXL.cache Trust Level 字段的设置（参见表 8-29）。• 若请求者正在使用 HDM-DB 流，且 Block CXL.cache HDM-DB=1，则中止该请求。D2H 响应消息和 D2H 数据消息不携带 CacheID，且始终路由回主机。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-15-3"></a>
### 9.15.3 Upstream Switch Port Routing Functionality | 上行交换机端口路由功能

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

When a USP receives a D2H request message from a DSP, the USP shall forward the message upstream. A USP may look up the Port Number associated with the CacheID field in the message from the CXL Cache ID Route Table and may compare that to the Port Number of the DSP that the message came from before forwarding the message. When a USP receives an H2D request message, H2D data message or an H2D response message, the USP shall use the message's CacheID field to look up the corresponding CXL Cache ID Target N register (see Section 8.2.4.28.4). If the Valid bit in the Cache ID Target register is 0, the H2D message shall be discarded without a response. If the Valid bit is 1, the message shall be forwarded to the local DSP based on the Port Number field that is programmed in the CXL Cache ID Target N register. Table 9-16. Downstream Port Handling of D2H Request Messages Assign Cache ID Value Forward Cache ID Value Behavior 0 0 Discard 0 1 Forward upstream. If the message was received over a link operating in 68B Flit mode, the request is processed as if CacheID field is 0. 1 0 Set CacheID=Local Cache ID and forward upstream. The link between the device and the Downstream Port may be operating in 68B Flit mode, in which case the D2H request message received by the Downstream Port does not contain the CacheID field. 1 1 Discard (Invalid setting) Table 9-17. Downstream Port Handling of H2D Response Message and H2D Request Message Assign Cache ID Value Forward Cache ID Value Behavior 0 0 Discard 0 1 Forward downstream as is 1 0 If CacheID=Local CacheID, forward downstream; otherwise, discard. The link between the device and the Downstream Port may be operating in 68B Flit mode, in which case the H2D message received by the device does not contain the CacheID field. The device shall ignore the CacheID field in H2D messages, if present. 1 1 Discard (Invalid setting)

</td><td style="background-color:#e8e8e8">

当 USP 从 DSP 接收到 D2H 请求消息时，USP 应将该消息向上游转发。USP 可从 CXL Cache ID Route Table 中查找与消息中的 CacheID 字段关联的端口号，并在转发消息之前将其与消息来源 DSP 的端口号进行比较。当 USP 接收到 H2D 请求消息、H2D 数据消息或 H2D 响应消息时，USP 应使用消息的 CacheID 字段查找对应的 CXL Cache ID Target N 寄存器（参见第 8.2.4.28.4 节）。若 Cache ID Target 寄存器中的 Valid 位为 0，则该 H2D 消息应被丢弃且不返回响应。若 Valid 位为 1，则该消息应根据 CXL Cache ID Target N 寄存器中编程的 Port Number 字段转发到本地 DSP。表 9-16. 下行端口对 D2H 请求消息的处理 Assign Cache ID 值 Forward Cache ID 值 行为 0 0 丢弃 0 1 向上游转发。若消息是通过以 68B Flit 模式运行的链路接收的，则请求按 CacheID 字段为 0 处理。1 0 设置 CacheID=Local Cache ID 并向上游转发。设备与下行端口之间的链路可能以 68B Flit 模式运行，此时下行端口接收到的 D2H 请求消息不包含 CacheID 字段。1 1 丢弃（无效设置） 表 9-17. 下行端口对 H2D 响应消息和 H2D 请求消息的处理 Assign Cache ID 值 Forward Cache ID 值 行为 0 0 丢弃 0 1 直接向下游转发 1 0 若 CacheID=Local CacheID，则向下游转发；否则丢弃。设备与下行端口之间的链路可能以 68B Flit 模式运行，此时设备接收到的 H2D 消息不包含 CacheID 字段。设备应忽略 H2D 消息中的 CacheID 字段（若存在）。1 1 丢弃（无效设置）

</td></tr>
<tr><td>

D2H response messages and D2H data messages do not carry CacheID and are always routed back to the host. If a USP receives CXL.cache message over a link operating in 68B Flit mode, it shall process the request as if the CacheID field is 0. A switch that is not capable of decoding CacheID field must be configured such that no more than one DSP is enabled for CXL.cache traffic (indicated by Cache_Enable=1 in the DVSEC Flex Bus Port Status register; see Section 8.2.1.3.3). The USP shall direct all H2D traffic to that DSP.

</td><td style="background-color:#e8e8e8">

D2H 响应消息和 D2H 数据消息不携带 CacheID，且始终路由回主机。若 USP 通过以 68B Flit 模式运行的链路接收到 CXL.cache 消息，则其应按 CacheID 字段为 0 来处理该请求。不具备 CacheID 字段解码能力的交换机必须被配置为：至多有一个 DSP 被启用用于 CXL.cache 流量（由 DVSEC Flex Bus Port Status 寄存器中的 Cache_Enable=1 指示；参见第 8.2.1.3.3 节）。USP 应将所有 H2D 流量定向到该 DSP。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-15-4"></a>
### 9.15.4 Host Bridge Routing Functionality | Host Bridge 路由功能

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

When the Host Bridge receives the equivalent of an H2D request or an H2D response message from the host, the Host Bridge logic shall use the CacheID field to look up the corresponding CXL Cache ID Target N register (see Section 8.2.4.28.4). If the Valid bit is 0, the H2D message is discarded. If the Valid bit is 1, the message is forwarded to the local root port based on the Port Number field that is programmed in the CXL Cache ID Target N register. When the Host Bridge receives a D2H request message from the root port, the Host Bridge shall forward the message to the host, using host-specific mechanisms. The Host Bridge may optionally look up the root port that is associated with the CacheID and discard the message if the message was received from a different root port.

</td><td style="background-color:#e8e8e8">

当 Host Bridge 从主机接收到等效于 H2D 请求或 H2D 响应的消息时，Host Bridge 逻辑应使用 CacheID 字段查找对应的 CXL Cache ID Target N 寄存器（参见第 8.2.4.28.4 节）。若 Valid 位为 0，则该 H2D 消息被丢弃。若 Valid 位为 1，则根据 CXL Cache ID Target N 寄存器中编程的 Port Number 字段，将消息转发到本地根端口。当 Host Bridge 从根端口接收到 D2H 请求消息时，Host Bridge 应使用主机特定机制将该消息转发至主机。Host Bridge 可选项为：查找与 CacheID 关联的根端口，若消息是从不同的根端口接收的，则丢弃该消息。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

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
> <tr><td>System Software may use the following sequence to allocate a Cache ID to a BI-capable CXL.cache Device D below a Switch S and enable the Device to generate CXL.cache transactions that target any memory:<br>1. Verify that the CXL link between Switch S and the host is operating in 256B Flit mode.<br>2. Identify an unused and legal CacheID value, c, and allocate it to Device D. Software must take into account the current Flit mode, as well as the Cache ID Target Count fields, while assigning Cache IDs to devices.<br>3. Configure the DSP of Switch S that is directly connected to Device D to assign Cache ID=c to Device D:<br>&nbsp;&nbsp;a. Forward Cache ID=0.<br>&nbsp;&nbsp;b. Local Cache ID=c.<br>&nbsp;&nbsp;c. Assign Cache ID=1.<br>4. If the above DSP of Switch S reports Explicit Cache ID Decoder Commit Required=1, commit the Cache ID changes as follows:<br>&nbsp;&nbsp;a. Cache ID Decoder Commit=0 to rearm.<br>&nbsp;&nbsp;b. Cache ID Decoder Commit=1.<br>&nbsp;&nbsp;c. Poll bits 0 and 1 of the Cache ID Decoder Status register until timeout or one of them is set. The timeout value is reported in the Cache ID Decoder Status register.<br>&nbsp;&nbsp;d. If Cache ID Decoder Error Not Committed=1, the changes were not committed. Software should treat this as an error condition.<br>&nbsp;&nbsp;e. If Cache ID Decoder Committed=1, the changes were committed. Proceed to Step 5.<br>&nbsp;&nbsp;f. If neither bit is set and the timeout is reached, software should treat this as an error condition.<br>5. Configure the USP of Switch S to route Cache ID c:<br>&nbsp;&nbsp;a. Route Table[c]= Port Number register of the DSP that is connected directly to Device D.<br>6. If the USP reports Explicit Cache ID RT Commit Required=1, commit the Cache ID changes as follows:<br>&nbsp;&nbsp;a. Cache ID RT Commit=0 to rearm.<br>&nbsp;&nbsp;b. Cache ID RT Commit=1.<br>&nbsp;&nbsp;c. Poll bits 0 and 1 of the Cache ID RT Status register until timeout or one of them is set. The timeout value is reported in the Cache ID RT Status register.<br>&nbsp;&nbsp;d. If Cache ID RT Error Not Committed=1, the changes were not committed. Software should treat this as an error condition.<br>&nbsp;&nbsp;e. If Cache ID RT Committed=1, the changes were committed. Proceed to Step 7.<br>&nbsp;&nbsp;f. If neither bit is set and the timeout is reached, software should treat this as an error condition.<br>7. Configure the Root Port, R, that is directly connected to Switch S to decode the CXL.cache messages from Device D:<br>&nbsp;&nbsp;a. If Forward Cache ID=0, set Forward Cache ID=1.<br>&nbsp;&nbsp;b. Ensure Assign Cache ID=0.<br>8. If the previous steps were successful, configure the CXL Cache ID Route Table (see Section 8.2.4.28.1) in the Host Bridge:<br>&nbsp;&nbsp;a. Route Table[c].Port Number=Port Number register of Root Port R.<br>9. If the previous steps were successful, inform the device driver that Device D may now issue CXL.cache requests.</td><td style="background-color:#e8e8e8">系统软件可使用以下步骤为交换机 S 下的一个支持 BI 的 CXL.cache 设备 D 分配 Cache ID，并使该设备能够生成面向任意内存的 CXL.cache 事务：<br>1. 验证交换机 S 与主机之间的 CXL 链路是否以 256B Flit 模式运行。<br>2. 识别一个未使用且合法的 CacheID 值 c，并将其分配给设备 D。软件在分配 Cache ID 时必须考虑当前的 Flit 模式以及 Cache ID Target Count 字段。<br>3. 配置交换机 S 中直接连接到设备 D 的 DSP，以将 Cache ID=c 分配给设备 D：<br>&nbsp;&nbsp;a. Forward Cache ID=0。<br>&nbsp;&nbsp;b. Local Cache ID=c。<br>&nbsp;&nbsp;c. Assign Cache ID=1。<br>4. 若交换机 S 的上述 DSP 报告 Explicit Cache ID Decoder Commit Required=1，则按以下方式提交 Cache ID 更改：<br>&nbsp;&nbsp;a. 将 Cache ID Decoder Commit 设为 0 以重新准备。<br>&nbsp;&nbsp;b. 将 Cache ID Decoder Commit 设为 1。<br>&nbsp;&nbsp;c. 轮询 Cache ID Decoder Status 寄存器的第 0 位和第 1 位，直到超时或其中一位被置位。超时值在 Cache ID Decoder Status 寄存器中报告。<br>&nbsp;&nbsp;d. 若 Cache ID Decoder Error Not Committed=1，则更改未被提交。软件应将此视为错误条件。<br>&nbsp;&nbsp;e. 若 Cache ID Decoder Committed=1，则更改已提交。继续执行第 5 步。<br>&nbsp;&nbsp;f. 若超时到达且无任何位被置位，软件应将此视为错误条件。<br>5. 配置交换机 S 的 USP 以路由 Cache ID c：<br>&nbsp;&nbsp;a. Route Table[c]= 直接连接到设备 D 的 DSP 的 Port Number 寄存器值。<br>6. 若 USP 报告 Explicit Cache ID RT Commit Required=1，则按以下方式提交 Cache ID 更改：<br>&nbsp;&nbsp;a. 将 Cache ID RT Commit 设为 0 以重新准备。<br>&nbsp;&nbsp;b. 将 Cache ID RT Commit 设为 1。<br>&nbsp;&nbsp;c. 轮询 Cache ID RT Status 寄存器的第 0 位和第 1 位，直到超时或其中一位被置位。超时值在 Cache ID RT Status 寄存器中报告。<br>&nbsp;&nbsp;d. 若 Cache ID RT Error Not Committed=1，则更改未被提交。软件应将此视为错误条件。<br>&nbsp;&nbsp;e. 若 Cache ID RT Committed=1，则更改已提交。继续执行第 7 步。<br>&nbsp;&nbsp;f. 若超时到达且无任何位被置位，软件应将此视为错误条件。<br>7. 配置直接连接到交换机 S 的根端口 R，以解码来自设备 D 的 CXL.cache 消息：<br>&nbsp;&nbsp;a. 若 Forward Cache ID=0，则设置 Forward Cache ID=1。<br>&nbsp;&nbsp;b. 确保 Assign Cache ID=0。<br>8. 若前述步骤成功，则配置 Host Bridge 中的 CXL Cache ID Route Table（参见第 8.2.4.28.1 节）：<br>&nbsp;&nbsp;a. Route Table[c].Port Number=根端口 R 的 Port Number 寄存器值。<br>9. 若前述步骤成功，则通知设备驱动程序：设备 D 现在可以发出 CXL.cache 请求。</td></tr>
> </tbody>
> </table>
>
> [⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-16"></a>
### 9.16 UIO Direct P2P to HDM | UIO 直接 P2P 到 HDM

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

CXL.mem devices that can complete UIO requests that target its HDM, advertise the capability via the UIO Capable bit in the CXL HDM Decoder Capability register (see Section 8.2.4.20.1). CXL switches may allow routing of UIO accesses to HDM in the same VH as the UIO requester and advertise this capability via the same bit. CXL Host Bridges may allow routing of UIO accesses to host memory or HDM below another root ports in the same Host Bridge and advertise this capability via this bit. Prior to setting up a UIO path from a UIO requester to an HDM or to host memory, the Software must consult the capabilities of the target device and any switches or Host Bridges in the path. Figure 9-25 shows a configuration with four CXL.mem devices that form three separate interleave sets and how a UIO requester is able to access the HDM range. UIO accesses to UIO Target 1 and UIO Target 2 are directly routed by the switch, whereas UIO accesses to UIO Target 3 and UIO Target 4 are routed through the host. As shown, UIO Target 1 and UIO Target 2 participate in a 2-way interleave set. The UIO requester can efficiently access this interleave set without going through the host. The HDM that is a target of P2P UIO accesses must be part of either a 1-way, 2-way, 4-way, 8-way, or 16-way interleave set. Any HDM that is part of a 3-way, 6-way, or 12-way interleave arrangement cannot be a P2P UIO target. The HDM address must be carved out of a CFMWS entry with Interleave Arithmetic=Standard Modulo arithmetic (see Table 9-22). In addition, P2P UIO traffic may be protected by Selective IDE Streams. In addition, Software must configure the switch and Host Bridge HDM decoders with additional information regarding any HDM interleaving calculations that are performed upstream to it before setting the UIO bit in that HDM decoder. The UIG, UIW, and ISP fields allow the switch and the Host Bridge to determine whether the UIO target address belongs to itself or to a peer component. The rules regarding the processing of UIO Direct P2P to HDM requests are described in Table 9-18. The ISP field in the target CXL.mem device allow the device to determine how it should respond. These requirements are in addition to the UIO related requirements that are defined in PCIe Base Specification.

</td><td style="background-color:#e8e8e8">

能够完成面向其 HDM 的 UIO 请求的 CXL.mem 设备，通过 CXL HDM Decoder Capability 寄存器中的 UIO Capable 位通告此能力（参见第 8.2.4.20.1 节）。CXL 交换机可允许将 UIO 访问路由到与 UIO 请求者处于同一 VH 中的 HDM，并通过同一位通告此能力。CXL Host Bridge 可允许将 UIO 访问路由到主机内存或同一下 Host Bridge 下另一根端口下的 HDM，并通过此位通告此能力。在建立从 UIO 请求者到 HDM 或主机内存的 UIO 路径之前，软件必须查询目标设备及路径中任何交换机或 Host Bridge 的能力。图 9-25 展示了包含四个 CXL.mem 设备（形成三个独立的交织集）的配置，以及 UIO 请求者如何访问 HDM 范围。对 UIO Target 1 和 UIO Target 2 的 UIO 访问由交换机直接路由，而对 UIO Target 3 和 UIO Target 4 的 UIO 访问则通过主机路由。如图所示，UIO Target 1 和 UIO Target 2 参与了一个 2-way 交织集。UIO 请求者可以高效地访问此交织集，而无需经过主机。作为 P2P UIO 访问目标的 HDM 必须是 1-way、2-way、4-way、8-way 或 16-way 交织集的一部分。任何属于 3-way、6-way 或 12-way 交织排列的 HDM 不能作为 P2P UIO 目标。HDM 地址必须从一个 Interleave Arithmetic=Standard Modulo arithmetic 的 CFMWS 条目中划分出来（参见表 9-22）。此外，P2P UIO 流量可通过 Selective IDE Streams 进行保护。另外，在对 HDM 解码器设置 UIO 位之前，软件必须为交换机和 Host Bridge 的 HDM 解码器配置关于在其上游执行的任何 HDM 交织计算的附加信息。UIG、UIW 和 ISP 字段使交换机和 Host Bridge 能够判断 UIO 目标地址是属于自身还是属于对等组件。关于 UIO 直接 P2P 到 HDM 请求的处理规则在表 9-18 中描述。目标 CXL.mem 设备中的 ISP 字段使设备能够决定应如何响应。这些要求是在 PCIe Base Specification 中定义的 UIO 相关要求之外的补充要求。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-16-1"></a>
### 9.16.1 Processing of UIO Direct P2P to HDM Messages | UIO 直接 P2P 到 HDM 消息的处理

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section describes how CXL components handle UIO Direct P2P accesses to HDM. UIO To HDM Enable bit is defined in Section 8.1.5.2 and allows System Software to control whether a requester below a switch can use UIO to access HDM.

</td><td style="background-color:#e8e8e8">

本节描述 CXL 组件如何处理 UIO 直接 P2P 对 HDM 的访问。UIO To HDM Enable 位在第 8.1.5.2 节中定义，允许系统软件控制交换机下的请求者是否可以使用 UIO 来访问 HDM。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-16-1-1"></a>
### 9.16.1.1 UIO Address Match (DSP and Root Port) | UIO 地址匹配（DSP 和根端口）

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

For a DSP or a root port, UIO address is considered a complete match if there exists an HDM Decoder[n] (see Section 8.2.4.20 and Section 8.2.4.30) for which the following conditions are true: Table 9-18. Handling of UIO Accesses Received by UIO Address Behavior CXL.mem device that reports UIO Capable=1 (see Section 8.2.4.20.1) Complete match with an HDM decoder with UIO=1 Respond to the UIO request per PCIe Base Specification Complete match with an HDM decoder with UIO=0 Return Completer Abort, do not commit data if it is a UIO write Partial match with an HDM decoder, irrespective of the UIO bit Return Completer Abort, do not commit data if it is a UIO write Mismatch Handle per PCIe Base Specification USP ingress of a CXL Switch that reports UIO Capable=1 (see Section 8.2.4.20.1) Either Partial or Complete match with an HDM decoder, irrespective of the UIO bit Identify the port number of the target DSP and forward Mismatch Handle per PCIe Base Specification DSP ingress of a CXL Switch that reports UIO Capable=1 (see Section 8.2.4.20.1) Complete match with an HDM decoder with UIO=1 and UIO To HDM Enable=1 Identify the port number of the target DSP and forward to that peer port regardless of ACS configuration including egress control vector Complete match with an HDM decoder with UIO=0 and UIO To HDM Enable=1 Forward toward the host regardless of ACS configuration including egress control vector Partial match with an HDM decoder and UIO To HDM Enable=1 Forward toward the host regardless of ACS configuration including egress control vector Complete or Partial match, and UIO To HDM Enable=0 Return Completer Abort Mismatch Handle per PCIe Base Specification RP ingress of a Host Bridge that reports UIO Capable=1 (see Section 8.2.4.20.1) Complete match with an HDM decoder with UIO=1 Identify the port number of the target RP and forward to that peer port, subject to host-specific access controls Complete match with an HDM decoder with UIO=0 Handle via host-specific mechanisms Partial match with an HDM decoder Handle via host-specific mechanisms Mismatch Handle via host-specific mechanisms

</td><td style="background-color:#e8e8e8">

对于 DSP 或根端口，若存在一个 HDM Decoder[n]（参见第 8.2.4.20 节和第 8.2.4.30 节）满足以下条件，则认为 UIO 地址为完全匹配：表 9-18. UIO 访问的处理方式 接收方 UIO 地址 行为 报告 UIO Capable=1 的 CXL.mem 设备（参见第 8.2.4.20.1 节） 与 UIO=1 的 HDM 解码器完全匹配 按 PCIe Base Specification 响应 UIO 请求 与 UIO=0 的 HDM 解码器完全匹配 返回 Completer Abort，若为 UIO 写操作则不提交数据 与 HDM 解码器部分匹配，无论 UIO 位如何 返回 Completer Abort，若为 UIO 写操作则不提交数据 不匹配 按 PCIe Base Specification 处理 报告 UIO Capable=1 的 CXL 交换机的 USP 入口（参见第 8.2.4.20.1 节） 与 HDM 解码器部分或完全匹配，无论 UIO 位如何 识别目标 DSP 的端口号并转发 不匹配 按 PCIe Base Specification 处理 报告 UIO Capable=1 的 CXL 交换机的 DSP 入口（参见第 8.2.4.20.1 节） 与 UIO=1 且 UIO To HDM Enable=1 的 HDM 解码器完全匹配 识别目标 DSP 的端口号并转发到该对等端口，不受 ACS 配置（包括出口控制向量）的影响 与 UIO=0 且 UIO To HDM Enable=1 的 HDM 解码器完全匹配 向主机方向转发，不受 ACS 配置（包括出口控制向量）的影响 与 HDM 解码器部分匹配且 UIO To HDM Enable=1 向主机方向转发，不受 ACS 配置（包括出口控制向量）的影响 完全或部分匹配且 UIO To HDM Enable=0 返回 Completer Abort 不匹配 按 PCIe Base Specification 处理 报告 UIO Capable=1 的 Host Bridge 的 RP 入口（参见第 8.2.4.20.1 节） 与 UIO=1 的 HDM 解码器完全匹配 识别目标 RP 的端口号并转发到该对等端口，遵循主机特定的访问控制 与 UIO=0 的 HDM 解码器完全匹配 通过主机特定机制处理 与 HDM 解码器部分匹配 通过主机特定机制处理 不匹配 通过主机特定机制处理

</td></tr>
<tr><td>

1. AT field in the UIO request indicates that it is carrying a translated address. 2. UIO.Address[63:2] >= Decoder[n].Base[63:2]. 3. UIO.Address[63:2]+UIO.Length[63:2] <= Decoder[n].Base[63:2]+ Decoder[n].Size[63:2]. 4. Either of these sub-conditions are true: a. Decoder[n].UIW=0 b. UIO.Address[Decoder[n].UIW+Decoder[n].UIG+7:Decoder[n].UIG+8]=ISP where UIO.Address[63:2] is derived from the Address field in the UIO TLP request, and UIO.Length[63:2] is derived from the Length field in the UIO TLP request. DSP calculations use the HDM decoders in the corresponding USP. The root port calculations make use of the HDM decoders in the associated Host Bridge. The first condition is in place because HDM decoder operates on translated address. The second and the third condition ensures that all addresses fall within one of the HDM decoders. The fourth condition ensures that the interleave set positions match (i.e., a CXL.mem request from the host to the start address would ordinarily be decoded by this component). 4a is the trivial case where the memory is not interleaved. If the first three conditions are met but the fourth condition is not met, it is considered a partial match. If the first three conditions are not met, it is considered a mismatch.

</td><td style="background-color:#e8e8e8">

1. UIO 请求中的 AT 字段指示其携带的是已翻译地址。2. UIO.Address[63:2] >= Decoder[n].Base[63:2]。3. UIO.Address[63:2] + UIO.Length[63:2] <= Decoder[n].Base[63:2] + Decoder[n].Size[63:2]。4. 以下子条件之一成立：a. Decoder[n].UIW=0 b. UIO.Address[Decoder[n].UIW+Decoder[n].UIG+7:Decoder[n].UIG+8]=ISP。其中 UIO.Address[63:2] 由 UIO TLP 请求中的 Address 字段导出，UIO.Length[63:2] 由 UIO TLP 请求中的 Length 字段导出。DSP 的计算使用对应 USP 中的 HDM 解码器。根端口的计算使用关联 Host Bridge 中的 HDM 解码器。第一个条件是因为 HDM 解码器操作的是已翻译地址。第二和第三个条件确保所有地址都落入某个 HDM 解码器范围内。第四个条件确保交织集位置匹配（即主机向起始地址发出的 CXL.mem 请求通常会被此组件解码）。4a 是内存未交织的简单情况。若前三个条件满足但第四个条件不满足，则视为部分匹配。若前三个条件不满足，则视为不匹配。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-16-1-2"></a>
### 9.16.1.2 UIO Address Match (CXL.mem Device) | UIO 地址匹配（CXL.mem 设备）

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

For a CXL.mem device, UIO address is considered a complete match if there exists an HDM Decoder[n] (see Section 8.2.4.20 and Section 8.2.4.30) for which the following conditions are true: 1. AT field in the UIO request indicates it is carrying a translated address. 2. UIO.Address[63:2] >= Decoder[n].Base[63:2]. 3. UIO.Address[63:2]+UIO.Length[63:2] <= Decoder[n].Base[63:2]+ Decoder[n].Size[63:2]. 4. Either of these sub-conditions are true: a. Decoder[n].UIW=0 b. UIO.Address[Decoder[n].IW+Decoder[n].IG+7:Decoder[n].IG+8]=ISP 5. UIO.Address[Decoder[n].IG+7:2] + UIO.Length[Decoder[n].IG+7:2] <= (2** IG+8). The first three conditions are identical to the DSP case. The terms involved in the fourth check are different, but it serves the same purpose (i.e., ensures that a CXL.mem request from the host to the start address would ordinarily be decoded by this component). The fifth condition ensures that the access does not cross an interleave boundary, thus ensuring that all the addresses that are referenced by the request are owned by the device. If the first three conditions are met but either of the other two conditions are not met, it is considered a partial match. If the first three conditions are not met, it is considered a mismatch.

</td><td style="background-color:#e8e8e8">

对于 CXL.mem 设备，若存在一个 HDM Decoder[n]（参见第 8.2.4.20 节和第 8.2.4.30 节）满足以下条件，则认为 UIO 地址为完全匹配：1. UIO 请求中的 AT 字段指示其携带的是已翻译地址。2. UIO.Address[63:2] >= Decoder[n].Base[63:2]。3. UIO.Address[63:2] + UIO.Length[63:2] <= Decoder[n].Base[63:2] + Decoder[n].Size[63:2]。4. 以下子条件之一成立：a. Decoder[n].UIW=0 b. UIO.Address[Decoder[n].IW+Decoder[n].IG+7:Decoder[n].IG+8]=ISP 5. UIO.Address[Decoder[n].IG+7:2] + UIO.Length[Decoder[n].IG+7:2] <= (2 ** IG + 8)。前三个条件与 DSP 的情况相同。第四项检查所涉及的变量不同，但其目的相同（即确保主机向起始地址发出的 CXL.mem 请求通常会被此组件解码）。第五个条件确保访问不跨越交织边界，从而确保请求所引用的所有地址都由该设备拥有。若前三个条件满足但其他两个条件中任何一个不满足，则视为部分匹配。若前三个条件不满足，则视为不匹配。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-17"></a>
### 9.17 Direct P2P CXL.mem for Accelerators | 加速器的直接 P2P CXL.mem

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The Direct P2P CXL.mem feature enables accelerators to use .mem semantics to access peer Type 3 devices. This feature is supported only by PBR Fabrics, and each accelerator and peer Type 3 device must be attached directly to an Edge Port. Configuration of the Fabric and Edge Ports is performed by the host and FM. Through mechanisms beyond the scope of this specification, the FM is preconfigured or informed of which Type 3 device(s) (i.e., SLD, MLD, or GFD) are to be configured for Direct P2P CXL.mem access by a given accelerator.

</td><td style="background-color:#e8e8e8">

Direct P2P CXL.mem 功能使加速器能够使用 .mem 语义访问对等 Type 3 设备。此功能仅由 PBR Fabric 支持，且每台加速器和对等 Type 3 设备必须直接连接到一个 Edge Port。Fabric 和 Edge Port 的配置由主机和 FM 执行。通过超出本规范范围的机制，FM 被预先配置或被通知哪些 Type 3 设备（即 SLD、MLD 或 GFD）应被配置为由给定加速器进行 Direct P2P CXL.mem 访问。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-17-1"></a>
### 9.17.1 Peer SLD Configuration | 对等 SLD 配置

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Host software and the FM may use the following high-level flow to configure Direct P2P CXL.mem communication between an accelerator and a peer Type 3 SLD: 1. The FM binds the SLD's Edge Port to the host VH of the accelerator, setting the vPPB.root.PID field to the PBR ID (PID) of the accelerator's Edge Port. This enables the host to configure the SLD, but the accelerator to carry out CXL.mem transactions with the SLD. 2. Using the Set LDST Segment Entries command (see Section 7.7.13.16), the host configures the LDST in the accelerator's Edge Port with one or more LDST Segments for the HPA range of the SLD, specifying the vPPB of the SLD's Edge Port. 3. Host software configures the SLD, notably its HDM Decoders, on behalf of the accelerator. HDM addresses in the SLD are HPAs.

</td><td style="background-color:#e8e8e8">

主机软件和 FM 可使用以下高层流程配置加速器与对等 Type 3 SLD 之间的 Direct P2P CXL.mem 通信：1. FM 将 SLD 的 Edge Port 绑定到加速器的主机 VH，将 vPPB.root.PID 字段设置为加速器 Edge Port 的 PBR ID (PID)。这使得主机能够配置 SLD，而加速器能够与 SLD 执行 CXL.mem 事务。2. 主机使用 Set LDST Segment Entries 命令（参见第 7.7.13.16 节），在加速器 Edge Port 的 LDST 中配置一个或多个针对 SLD 的 HPA 范围的 LDST Segment，并指定 SLD Edge Port 的 vPPB。3. 主机软件代表加速器配置 SLD，尤其是其 HDM 解码器。SLD 中的 HDM 地址为 HPA。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-17-2"></a>
### 9.17.2 Peer MLD Configuration | 对等 MLD 配置

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Host software and the FM may use the following high-level flow to configure Direct P2P CXL.mem communication between one or more accelerators that belong to the host and a peer Type 3 MLD: 1. The FM binds a vPPB in the MLD's Edge Port to the host VH of its accelerator(s) and an additional vPPB for each accelerator under that host that will be accessing the MLD. Each of these will have a distinct LD-ID. For each vPPB assigned to an accelerator, the vPPB.root.PID field is set to the PID of the accelerator's Edge Port. 2. Using the Set LDST Segment Entries command (see Section 7.7.13.16), the host configures the LDST in each accelerator's Edge Port with one or more LDST Segments for the HPA range of the accelerator's LD, specifying the accelerator's vPPB in the MLD's Edge Port. 3. Host software configures its LDs in the MLD, notably their HDM Decoders, on behalf of itself and its accelerator(s). HDM addresses in the LD of the host and the LD(s) of the accelerator(s) are HPAs.

</td><td style="background-color:#e8e8e8">

主机软件和 FM 可使用以下高层流程配置属于同一主机的一台或多台加速器与对等 Type 3 MLD 之间的 Direct P2P CXL.mem 通信：1. FM 在 MLD 的 Edge Port 中为加速器的主机 VH 绑定一个 vPPB，并为该主机下将要访问 MLD 的每台加速器各绑定一个额外的 vPPB。每个 vPPB 将具有不同的 LD-ID。对于分配给加速器的每个 vPPB，vPPB.root.PID 字段设置为该加速器 Edge Port 的 PID。2. 主机使用 Set LDST Segment Entries 命令（参见第 7.7.13.16 节），在每台加速器 Edge Port 的 LDST 中配置一个或多个针对该加速器 LD 的 HPA 范围的 LDST Segment，并指定加速器在 MLD Edge Port 中的 vPPB。3. 主机软件代表自身及其加速器配置 MLD 中的 LD，尤其是其 HDM 解码器。主机的 LD 和加速器的 LD 中的 HDM 地址为 HPA。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-17-3"></a>
### 9.17.3 Peer GFD Configuration | 对等 GFD 配置

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Host software and the FM may use the following high-level flow to configure Direct P2P CXL.mem communication between one or more accelerators that belong to a host and a peer Type 3 GFD: 1. The FM configures the GFD for host access normally, while configuring each of the host's accelerators as an additional RPID within the GFD. 2. Using the Set FAST Segment Entries command (see Section 7.7.14.7), the host configures the FAST decoder in its Edge Port as well as each accelerator's Edge Port with one or more FAST Segments for the HPA range, specifying the GFD's PID.

</td><td style="background-color:#e8e8e8">

主机软件和 FM 可使用以下高层流程配置属于同一主机的一台或多台加速器与对等 Type 3 GFD 之间的 Direct P2P CXL.mem 通信：1. FM 按常规方式配置 GFD 以供主机访问，同时将该主机的每台加速器配置为 GFD 内的额外 RPID。2. 主机使用 Set FAST Segment Entries 命令（参见第 7.7.14.7 节），在自己的 Edge Port 以及每台加速器的 Edge Port 的 FAST 解码器中配置一个或多个针对 HPA 范围的 FAST Segment，并指定 GFD 的 PID。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<p style="text-align:right;color:#888;font-size:0.9em">CXL 3.2 Specification, Chapter 9 — Sections 9.15–9.17.3 | CXL 3.2 规范，第 9 章 — 第 9.15–9.17.3 节</p>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-18"></a>
### 9.18 CXL OS Firmware Interface Extensions | CXL操作系统固件接口扩展

---

<a id="sec-9-18-1"></a>
### 9.18.1 CXL Early Discovery Table (CEDT) | CXL早期发现表

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

CXL Early Discovery Table enables OSs to locate CXL Host Bridges and the location of Host Bridge registers early during the boot (i.e., prior to parsing of ACPI namespace). The information in this table may be used by early boot code to perform pre-initialization of CXL hosts, such as configuration of CXL.cache and CXL.mem.

</td><td style="background-color:#e8e8e8">

CXL早期发现表（CXL Early Discovery Table）使操作系统能够在引导早期（即在解析ACPI命名空间之前）定位CXL主机桥以及主机桥寄存器的位置。该表中的信息可由早期引导代码用于执行CXL主机的预初始化，例如CXL.cache和CXL.mem的配置。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-1-1"></a>
### 9.18.1.1 CEDT Header | CEDT表头

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The pointer to CEDT is found in RSDT or XSDT, as described in ACPI Specification. An ACPI specification-compliant CXL system shall support CEDT and shall include a CHBS entry for every CXL host bridge that is present at boot. CEDT begins with the following header.

</td><td style="background-color:#e8e8e8">

CEDT的指针位于RSDT或XSDT中，如ACPI规范所述。符合ACPI规范的CXL系统应支持CEDT，并应为引导时存在的每个CXL主机桥包含一个CHBS条目。CEDT以如下表头开始。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-1-2"></a>
### 9.18.1.2 CXL Host Bridge Structure (CHBS) | CXL主机桥结构

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CHBS structure describes a CXL Host Bridge.

</td><td style="background-color:#e8e8e8">

CHBS结构描述一个CXL主机桥。

</td></tr>
</tbody></table>

<br>

**Table 9-19. CEDT Header | CEDT表头**

<table>
<thead><tr><th width="33%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="15%">Byte Offset | 字节偏移</th><th width="42%">Description | 描述</th></tr></thead>
<tbody>
<tr><td><b>Header:</b></td><td></td><td></td><td></td></tr>
<tr><td>Signature | 签名</td><td>4</td><td>00h</td><td>'CEDT'. Signature for the CXL Early Discovery Table. | 'CEDT'。CXL早期发现表的签名。</td></tr>
<tr><td>Length | 长度</td><td>4</td><td>04h</td><td>Length, in bytes, of the entire CEDT. | 整个CEDT的长度，以字节为单位。</td></tr>
<tr><td>Revision | 版本</td><td>1</td><td>08h</td><td>Value is 2. | 值为2。</td></tr>
<tr><td>Checksum | 校验和</td><td>1</td><td>09h</td><td>Entire table must sum to 0. | 整个表的校验和必须为0。</td></tr>
<tr><td>OEM ID</td><td>6</td><td>0Ah</td><td>OEM ID | OEM ID</td></tr>
<tr><td>OEM Table ID | OEM表ID</td><td>8</td><td>10h</td><td>Manufacturer Model ID | 制造商型号ID</td></tr>
<tr><td>OEM Revision | OEM版本</td><td>4</td><td>18h</td><td>OEM Revision | OEM版本</td></tr>
<tr><td>Creator ID | 创建者ID</td><td>4</td><td>1Ch</td><td>Vendor ID of the utility that created the table. | 创建该表的实用程序的供应商ID。</td></tr>
<tr><td>Creator Revision | 创建者版本</td><td>4</td><td>20h</td><td>Revision of the utility that created the table. | 创建该表的实用程序的版本。</td></tr>
<tr><td><b>CEDT Structure[n] | CEDT结构[n]</b></td><td>Varies | 可变</td><td>24h</td><td>A list of CEDT structures for this implementation. | 此实现的CEDT结构列表。</td></tr>
</tbody></table>

<br>

**Table 9-20. CEDT Structure Types | CEDT结构类型**

<table>
<thead><tr><th width="15%">Value | 值</th><th width="85%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>0</td><td>CXL Host Bridge Structure (CHBS) | CXL主机桥结构</td></tr>
<tr><td>1</td><td>CXL Fixed Memory Window Structure (CFMWS) | CXL固定内存窗口结构</td></tr>
<tr><td>2</td><td>CXL XOR Interleave Math Structure (CXIMS) | CXL XOR交错算术结构</td></tr>
<tr><td>3</td><td>RCEC Downstream Port Association Structure (RDPAS) | RCEC下游端口关联结构</td></tr>
<tr><td>4</td><td>CXL System Description Structure (CSDS) | CXL系统描述结构</td></tr>
<tr><td>5-255</td><td>Reserved | 保留</td></tr>
</tbody></table>

<br>

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

In an ACPI-compliant system, there shall be one instance of the CXL Host Bridge Device object in ACPI namespace (HID="ACPI0016") for every CHBS entry. The _UID object under a CXL Host Bridge object, when evaluated, shall match the UID field in the associated CHBS entry.

</td><td style="background-color:#e8e8e8">

在符合ACPI的系统中，每个CHBS条目应在ACPI命名空间中存在一个CXL主机桥设备对象实例（HID="ACPI0016"）。CXL主机桥对象下的_UID对象在被评估时，其值应与关联的CHBS条目中的UID字段匹配。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-1-3"></a>
### 9.18.1.3 CXL Fixed Memory Window Structure (CFMWS) | CXL固定内存窗口结构

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CFMWS structure describes zero or more Host Physical Address (HPA) windows that are associated with each CXL Host Bridge. Each window represents a contiguous HPA range that may be interleaved across one or more targets, some of which are CXL Host Bridges. Associated with each window are a set of restrictions that govern its usage. It is the OSPM's responsibility to utilize each window for the specified use. The HPA ranges described by CFMWS may include addresses that are currently assigned to CXL.mem devices. Before assigning HPAs from a fixed-memory window, the OSPM must check the current assignments and avoid any conflicts. For any given HPA, it shall not be described by more than one CFMWS entry.

</td><td style="background-color:#e8e8e8">

CFMWS结构描述与每个CXL主机桥关联的零个或多个主机物理地址（HPA）窗口。每个窗口表示一个连续的HPA范围，该范围可以在一个或多个目标之间交错，其中某些目标是CXL主机桥。与每个窗口关联的是一组控制其使用的限制条件。OSPM有责任将每个窗口用于指定的用途。CFMWS描述的HPA范围可能包含当前已分配给CXL.mem设备的地址。在从固定内存窗口分配HPA之前，OSPM必须检查当前的分配情况并避免任何冲突。对于任何给定的HPA，其不应被多于一个CFMWS条目所描述。

</td></tr>
</tbody></table>

<br>

**Table 9-21. CHBS Structure | CHBS结构**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Type | 类型</td><td>1</td><td>00h</td><td>=0 to indicate that this is a CHBS entry | =0表示这是一个CHBS条目</td></tr>
<tr><td>Reserved | 保留</td><td>1</td><td>01h</td><td>Reserved | 保留</td></tr>
<tr><td>Record Length | 记录长度</td><td>2</td><td>02h</td><td>Length of this record (20h). | 此记录的长度（20h）。</td></tr>
<tr><td>UID</td><td>4</td><td>04h</td><td>CXL Host Bridge Unique ID. Used to associate a CHBS instance with a CXL Host Bridge instance. The value of this field shall match the output of _UID under the associated CXL Host Bridge in ACPI namespace. | CXL主机桥唯一ID。用于将CHBS实例与CXL主机桥实例关联。此字段的值应与ACPI命名空间中关联的CXL主机桥下的_UID输出值匹配。</td></tr>
<tr><td>CXL Version | CXL版本</td><td>4</td><td>08h</td><td>· 0000 0000h: RCH<br>· 0000 0001h: Host Bridge that is associated with one or more CXL root ports | · 0000 0000h：RCH<br>· 0000 0001h：与一个或多个CXL根端口关联的主机桥</td></tr>
<tr><td>Reserved | 保留</td><td>4</td><td>0Ch</td><td>Reserved | 保留</td></tr>
<tr><td>Base | 基地址</td><td>8</td><td>10h</td><td>· If CXL Version = 0000 0000h, this represents the base address of the RCH Downstream Port RCRB<br>· If CXL Version = 0000 0001h, this represents the base address of the CHBCR<br>See Table 8-17 for more details. | · 若CXL Version = 0000 0000h，此字段表示RCH下游端口RCRB的基地址<br>· 若CXL Version = 0000 0001h，此字段表示CHBCR的基地址<br>详见Table 8-17。</td></tr>
<tr><td>Length | 长度</td><td>8</td><td>18h</td><td>· If CXL Version = 0000 0000h, this field must be set to 8 KB (2000h)<br>· If CXL Version = 0000 0001h, this field must be set to 64 KB (1 0000h) | · 若CXL Version = 0000 0000h，此字段必须设置为8 KB（2000h）<br>· 若CXL Version = 0000 0001h，此字段必须设置为64 KB（1 0000h）</td></tr>
</tbody></table>

<br>

**Table 9-22. CFMWS Structure (Sheet 1 of 3) | CFMWS结构（第1页，共3页）**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Type | 类型</td><td>1</td><td>00h</td><td>1 = indicates this is a CFMWS entry | 1 = 表示这是一个CFMWS条目</td></tr>
<tr><td>Reserved | 保留</td><td>1</td><td>01h</td><td>Reserved | 保留</td></tr>
<tr><td>Record Length | 记录长度</td><td>2</td><td>02h</td><td>Length of this record = 024h + 4 * NIW. NIW is the raw count of Interleave ways whereas ENIW is the encoded value:<br>· If ENIW<8, NIW=2<sup>ENIW</sup><br>· If ENIW>=8, NIW=3* 2<sup>(ENIW-8)</sup> | 此记录的长度 = 024h + 4 * NIW。NIW是交错路的原始计数，而ENIW是编码值：<br>· 若ENIW<8，NIW=2<sup>ENIW</sup><br>· 若ENIW>=8，NIW=3* 2<sup>(ENIW-8)</sup></td></tr>
<tr><td>Reserved | 保留</td><td>4</td><td>04h</td><td>Reserved | 保留</td></tr>
<tr><td>Base HPA</td><td>8</td><td>08h</td><td>Base of this HPA range. This value shall be a 256-MB-aligned address. | 此HPA范围的基址。此值应为256 MB对齐的地址。</td></tr>
<tr><td>Window Size | 窗口大小</td><td>8</td><td>10h</td><td>The total number of consecutive bytes of HPA this window represents. This value shall be a multiple of NIW*256 MB. | 此窗口所表示的连续HPA字节总数。此值应为NIW*256 MB的倍数。</td></tr>
<tr><td>Encoded Number of Interleave Ways (ENIW) | 交错路编码数</td><td>1</td><td>18h</td><td>The encoded number of targets with which this window is interleaved. The valid encoded values are specified in the Interleave Ways field of the CXL HDM Decoder n Control register (see Section 8.2.4.20.7). This field determines the number of entries in the Interleave Target List, starting at Offset 24h. | 此窗口与之交错的目标编码数量。有效的编码值在CXL HDM Decoder n Control寄存器的Interleave Ways字段中定义（见Section 8.2.4.20.7）。此字段决定从偏移24h开始的Interleave Target List中的条目数量。</td></tr>
<tr><td>Interleave Arithmetic | 交错算术</td><td>1</td><td>19h</td><td>This field defines the arithmetic used for mapping HPA to an interleave target in the Interleave Target List:<br>· 00h = Standard Modulo arithmetic<br>· 01h = Modulo arithmetic combined with XOR<br>· All other encodings are reserved | 此字段定义用于将HPA映射到Interleave Target List中交错目标的算术方式：<br>· 00h = 标准取模算术<br>· 01h = 取模算术与XOR组合<br>· 所有其他编码均保留</td></tr>
<tr><td>Reserved | 保留</td><td>2</td><td>1Ah</td><td>Reserved | 保留</td></tr>
<tr><td>Host Bridge Interleave Granularity (HBIG) | 主机桥交错粒度</td><td>4</td><td>1Ch</td><td>The number of consecutive bytes within the interleave that are decoded by each target in the Interleave Target List represented in an encoded format. The valid values are specified in the Interleave Granularity field of the CXL HDM Decoder n Control register (see Section 8.2.4.20.7). | 交错中由Interleave Target List中的每个目标解码的连续字节数，以编码格式表示。有效值在CXL HDM Decoder n Control寄存器的Interleave Granularity字段中定义（见Section 8.2.4.20.7）。</td></tr>
<tr><td>Window Restrictions | 窗口限制</td><td>2</td><td>20h</td><td>A bitmap describing the restrictions being placed on the OSPM's use of the window. It is the OSPM's responsibility to adhere to these restrictions. Failure to adhere to these restrictions results in undefined behavior. More than one bit within this field may be set:<br>· <b>Bit[0]: Device Coherent</b>: Formerly known as CXL Type 2 Memory: — 1 = Window is configured to expose device-coherent memory (HDM-D if Bit[5]=0 ; HDM-DB if Bit[5]=1).<br>· <b>Bit[1]: Host-only Coherent</b>: Formerly known as CXL Type 3 Memory: — 1 = Window is configured to expose host-only coherent memory (HDM-H). If an HDM decoder that is mapped to this window has the BI bit set, it will result in undefined behavior.<br>· <b>Bit[2]: Volatile</b>: — 1 = Window is configured for use with volatile memory.<br>· <b>Bit[3]: Persistent</b>: — 1 = Window is configured for use with persistent memory.<br>· <b>Bit[4]: Fixed Device Configuration</b>: — 1 = Any device ranges that have been assigned an HPA from this window must not be reassigned.<br>· <b>Bit[5]: BI</b>: — 1 = Window is configured for use with Back-Invalidate flows.<br>· <b>Bits[15:6]: Reserved</b> | 描述OSPM使用该窗口的限制条件的位图。OSPM有责任遵守这些限制。未能遵守这些限制将导致未定义的行为。此字段中可设置多个位：<br>· <b>Bit[0]: Device Coherent（设备一致性）</b>：以前称为CXL Type 2 Memory： — 1 = 窗口配置为暴露设备一致性内存（若Bit[5]=0则为HDM-D；若Bit[5]=1则为HDM-DB）。<br>· <b>Bit[1]: Host-only Coherent（仅主机一致性）</b>：以前称为CXL Type 3 Memory： — 1 = 窗口配置为暴露仅主机一致性内存（HDM-H）。如果映射到此窗口的HDM解码器设置了BI位，将导致未定义的行为。<br>· <b>Bit[2]: Volatile（易失性）</b>： — 1 = 窗口配置为用于易失性内存。<br>· <b>Bit[3]: Persistent（持久性）</b>： — 1 = 窗口配置为用于持久性内存。<br>· <b>Bit[4]: Fixed Device Configuration（固定设备配置）</b>： — 1 = 已从此窗口分配HPA的任何设备范围不得重新分配。<br>· <b>Bit[5]: BI（回写失效）</b>： — 1 = 窗口配置为用于Back-Invalidate流程。<br>· <b>Bits[15:6]: Reserved（保留）</b></td></tr>
<tr><td>QTG ID</td><td>2</td><td>22h</td><td>The ID of the QoS Throttling Group associated with this window. The _DSM for retrieving QTG ID is utilized by the OSPM to determine to which QTG a device HDM range should be assigned. This field must not exceed the Max Supported QTG ID returned by the _DSM for retrieving QTG. | 与此窗口关联的QoS节流组（QoS Throttling Group）的ID。OSPM使用获取QTG ID的_DSM来确定设备HDM范围应分配到哪个QTG。此字段不得超过获取QTG的_DSM返回的Max Supported QTG ID。</td></tr>
</tbody></table>

<br>

**Table 9-22. CFMWS Structure (Sheet 2 of 3) | CFMWS结构（第2页，共3页）**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Interleave Target List | 交错目标列表</td><td>4*NIW</td><td>24h</td><td>A list of all the Interleave Targets. The number of entries in this list shall match the Number of Interleave Ways (NIW). The order of the targets reported in this List indicates the order in the Interleave Set. For Interleave Sets that only span CXL Host Bridges, this is a list of CXL Host Bridge _UIDs that are part of the Interleave Set. In this case, for each _UID value in this list, there must exist a corresponding CHBS structure. If the Interleave Set spans non-CXL domains, this list may contain values that do not match _UID field in any CHBS structures. These entries represent Interleave Targets that are not CXL Host Bridges.<br><br>The set of HPAs decoded by Entry N in the Interleave Target List shall satisfy the following equations:<br>1. Base HPA <= HPA < Base HPA + Window Size: where the Base HPA and Window size shall be multiple of NIW.<br><br><b>If (Interleave Arithmetic==0):</b><br>a. If ENIW=0 &nbsp; N=0<br>b. If ENIW=1 &nbsp; N= HPA[8+HBIG]<br>c. If ENIW<8 AND ENIW>1 &nbsp; N = HPA[7+HBIG+ENIW:8+HBIG]<br>d. If NIW = 8 // 3 way &nbsp; N = HPA[51:8+HBIG] MOD 3<br>e. If NIW=9 // 6 way &nbsp; N = HPA[8+HBIG] + 2* HPA[51:9+HBIG] MOD 3<br>f. If NIW=10 //12 way &nbsp; N = HPA[9+HBIG:8+HBIG] + 4* HPA[51:10+HBIG] MOD 3<br><br><b>2. If (Interleave Arithmetic==1):</b><br>a. If NIW=0 //1 way &nbsp; N=0<br>b. If NIW =1 // 2 way &nbsp; N = XORALLBITS (HPA AND XORMAP[0])<br>&nbsp;&nbsp;&nbsp;If NIW=2 // 4 way &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + 2* XORALLBITS (HPA AND XORMAP[1])</td><td>所有交错目标的列表。此列表中的条目数量应与交错路数（NIW）匹配。此列表中报告的目标顺序表示交错集中的顺序。对于仅跨越CXL主机桥的交错集，这是一个属于该交错集的CXL主机桥_UID列表。在这种情况下，对于此列表中的每个_UID值，必须存在一个对应的CHBS结构。如果交错集跨越非CXL域，此列表可能包含与任何CHBS结构中的_UID字段都不匹配的值。这些条目表示非CXL主机桥的交错目标。<br><br>由Interleave Target List中第N个条目解码的HPA集合应满足以下方程：<br>1. Base HPA <= HPA < Base HPA + Window Size：其中Base HPA和Window size应为NIW的倍数。<br><br><b>若 (Interleave Arithmetic==0)：</b><br>a. 若ENIW=0 &nbsp; N=0<br>b. 若ENIW=1 &nbsp; N= HPA[8+HBIG]<br>c. 若ENIW<8 且 ENIW>1 &nbsp; N = HPA[7+HBIG+ENIW:8+HBIG]<br>d. 若NIW = 8 // 3路 &nbsp; N = HPA[51:8+HBIG] MOD 3<br>e. 若NIW=9 // 6路 &nbsp; N = HPA[8+HBIG] + 2* HPA[51:9+HBIG] MOD 3<br>f. 若NIW=10 //12路 &nbsp; N = HPA[9+HBIG:8+HBIG] + 4* HPA[51:10+HBIG] MOD 3<br><br><b>2. 若 (Interleave Arithmetic==1)：</b><br>a. 若NIW=0 //1路 &nbsp; N=0<br>b. 若NIW =1 // 2路 &nbsp; N = XORALLBITS (HPA AND XORMAP[0])<br>&nbsp;&nbsp;&nbsp;若NIW=2 // 4路 &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + 2* XORALLBITS (HPA AND XORMAP[1])</td></tr>
</tbody></table>

<br>

**Table 9-22. CFMWS Structure (Sheet 3 of 3) | CFMWS结构（第3页，共3页）**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Interleave Target List | 交错目标列表</td><td>4*NIW</td><td>24h</td><td>c. If NIW=3 // 8 way &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + XORALLBITS (HPA AND XORMAP[1]) + XORALLBITS (HPA AND XORMAP[2])<br>d. If NIW=4 //16 way &nbsp; N = XORALLBITS (HPA AND XORMAP[0])+ 2* XORALLBITS (HPA AND XORMAP[1]) + 4* XORALLBITS (HPA AND XORMAP[2]) + 8* XORALLBITS (HPA AND XORMAP[3])<br>e. If NIW =8 // 3 way, same as Interleave Arithmetic=0 &nbsp; N = HPA[51:8+HBIG] MOD 3<br>f. If NIW =9 // 6 way &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + 2* HPA[51:9+HBIG] MOD 3<br>g. If NIW=10 // 12 way &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + 2* XORALLBITS (HPA AND XORMAP[1]) + 4* HPA[51:10+HBIG] MOD 3<br><br>N is 0 based (0<= N <NIW). Where XORALLBITS is an operation that outputs a single bit by XORing all the bits in the input. AND is a standard bitwise AND operation and XORMAP[m] is the m<sup>th</sup> element (m is 0 based) in the XORMAP array that is part of the CXIMS entry with the matching HBIG value.</td><td>c. 若NIW=3 // 8路 &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + XORALLBITS (HPA AND XORMAP[1]) + XORALLBITS (HPA AND XORMAP[2])<br>d. 若NIW=4 //16路 &nbsp; N = XORALLBITS (HPA AND XORMAP[0])+ 2* XORALLBITS (HPA AND XORMAP[1]) + 4* XORALLBITS (HPA AND XORMAP[2]) + 8* XORALLBITS (HPA AND XORMAP[3])<br>e. 若NIW =8 // 3路，与Interleave Arithmetic=0相同 &nbsp; N = HPA[51:8+HBIG] MOD 3<br>f. 若NIW =9 // 6路 &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + 2* HPA[51:9+HBIG] MOD 3<br>g. 若NIW=10 // 12路 &nbsp; N = XORALLBITS (HPA AND XORMAP[0]) + 2* XORALLBITS (HPA AND XORMAP[1]) + 4* HPA[51:10+HBIG] MOD 3<br><br>N为从0开始的索引（0<= N <NIW）。其中，XORALLBITS是一个操作，通过对输入中的所有位进行XOR运算输出单个位。AND是标准的按位AND操作，XORMAP[m]是XORMAP数组中第m个元素（m从0开始），该数组属于具有匹配HBIG值的CXIMS条目。</td></tr>
</tbody></table>

---

<a id="sec-9-18-1-4"></a>
### 9.18.1.4 CXL XOR Interleave Math Structure (CXIMS) | CXL XOR交错算术结构

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

If a CFMWS entry reports Interleave Arithmetic=1, there must be one CXIMS entry associated with the HBIG value in the CFMWS. CXIMS carries an array of bitmaps. Each bitmap represents the bits that are XORed together to calculate the individual bits of the Interleave Way as described in the definition of the Interleave Target List field in CFMWS. The host implementation is responsible for selecting an XOR function that generates even distribution of addresses and does not lead to address aliasing.

</td><td style="background-color:#e8e8e8">

如果一个CFMWS条目报告Interleave Arithmetic=1，则必须存在一个与该CFMWS中的HBIG值关联的CXIMS条目。CXIMS携带一个位图数组。每个位图表示被XOR在一起以计算Interleave Way各个位的位，如CFMWS中Interleave Target List字段的定义所述。主机实现负责选择一个XOR函数，该函数生成均匀的地址分布且不会导致地址别名。

</td></tr>
</tbody></table>

<br>

**Table 9-23. CXIMS Structure | CXIMS结构**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Type | 类型</td><td>1</td><td>00h</td><td>2 = Indicates that this is a CXIMS entry | 2 = 表示这是一个CXIMS条目</td></tr>
<tr><td>Reserved | 保留</td><td>1</td><td>01h</td><td>Reserved | 保留</td></tr>
<tr><td>Record Length | 记录长度</td><td>2</td><td>02h</td><td>Length of this record = 8 + 8 * NIB. | 此记录的长度 = 8 + 8 * NIB。</td></tr>
<tr><td>Reserved | 保留</td><td>2</td><td>04h</td><td>Reserved | 保留</td></tr>
<tr><td>HBIG</td><td>1</td><td>06h</td><td>Host Bridge Interleave Granularity to which this CXIMS instance corresponds. See Table 9-22 for the definition of the term HBIG. | 此CXIMS实例对应的主机桥交错粒度。术语HBIG的定义见Table 9-22。</td></tr>
<tr><td>Number of Bitmap Entries (NIB) | 位图条目数</td><td>1</td><td>07h</td><td>The number of entries in the XORMAP list. | XORMAP列表中的条目数量。</td></tr>
<tr><td>XORMAP List | XORMAP列表</td><td>8 * NIB</td><td>08h</td><td>A list of Bitmaps. XORMAP[0] is the first entry. | 位图列表。XORMAP[0]是第一个条目。</td></tr>
</tbody></table>

---

<a id="sec-9-18-1-5"></a>
### 9.18.1.5 RCEC Downstream Port Association Structure (RDPAS) | RCEC下游端口关联结构

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

RDPAS structure enables error handler to locate the Downstream Port(s) that report errors to a given RCEC. For every RCEC, zero or more entries of this type are permitted.

</td><td style="background-color:#e8e8e8">

RDPAS结构使错误处理程序能够定位向给定RCEC报告错误的下游端口。对于每个RCEC，允许存在零个或多个此类型的条目。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-1-6"></a>
### 9.18.1.6 CXL System Description Structure (CSDS) | CXL系统描述结构

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CSDS describes CXL System Wide Description and Configuration. In a system, there shall be only one instance of the CSDS in the CEDT.

</td><td style="background-color:#e8e8e8">

CSDS描述CXL系统范围的描述与配置。在一个系统中，CEDT中应仅存在一个CSDS实例。

</td></tr>
</tbody></table>

<br>

**Table 9-24. RDPAS Structure | RDPAS结构**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Type | 类型</td><td>1</td><td>00h</td><td>3 = Indicates that this is an RDPAS entry | 3 = 表示这是一个RDPAS条目</td></tr>
<tr><td>Reserved | 保留</td><td>1</td><td>01h</td><td>Reserved | 保留</td></tr>
<tr><td>Record Length | 记录长度</td><td>2</td><td>02h</td><td>Length of this record = 14h | 此记录的长度 = 14h</td></tr>
<tr><td>RCEC Segment Number | RCEC段号</td><td>2</td><td>04h</td><td>The PCIe segment number associated with this RCEC | 与此RCEC关联的PCIe段号</td></tr>
<tr><td>RCEC BDF</td><td>2</td><td>06h</td><td>· Bits[2:0]: RCEC Function Number<br>· Bits[7:3]: RCEC Device Number<br>· Bits[15:8]: RCEC Bus Number | · Bits[2:0]：RCEC功能号<br>· Bits[7:3]：RCEC设备号<br>· Bits[15:8]：RCEC总线号</td></tr>
<tr><td>Base Address | 基地址</td><td>8</td><td>08h</td><td>If Protocol Type = CXL.io, this field shall be the RCRB base associated with the Downstream Port. If Protocol Type = CXL.cachemem, this will be the Component Base Register Base associated with the Downstream Port. | 若Protocol Type = CXL.io，此字段应为与下游端口关联的RCRB基地址。若Protocol Type = CXL.cachemem，此字段应为与下游端口关联的组件基寄存器（Component Base Register）基地址。</td></tr>
<tr><td>Protocol Type | 协议类型</td><td>1</td><td>10h</td><td>· 00h = The error source is CXL.io<br>· 01h = The error source is CXL.cachemem | · 00h = 错误源为CXL.io<br>· 01h = 错误源为CXL.cachemem</td></tr>
<tr><td>Reserved | 保留</td><td>3</td><td>11h</td><td>Reserved | 保留</td></tr>
</tbody></table>

<br>

> **IMPLEMENTATION NOTE | 实现注意事项**
>
> CXL-aware software may take the following steps upon observing an Uncorrected Internal Error or a Corrected Internal Error being logged in an RCEC at Segment Number S and BDF=B.
>
> 支持CXL的软件在观察到段号为S、BDF=B的RCEC中记录了不可纠正内部错误（Uncorrected Internal Error）或可纠正内部错误（Corrected Internal Error）时，可采取以下步骤。
>
> If the CEDT contains RDPAS structures:
> - For all RDPAS structures where RCEC Segment Number=S and RCEC BDF= B:
>   - If Protocol Type=CXL.io, read the Base Address field and use that information to access the RCRB AER registers and determine whether any errors are logged there
>   - If Protocol Type=CXL.cachemem, read the Base Address field and use that information to access the Component Register RAS Capability registers (see Section 8.2.4.17) and determine whether any errors are logged there
>
> 如果CEDT包含RDPAS结构：
> - 对于所有RCEC Segment Number=S且RCEC BDF=B的RDPAS结构：
>   - 若Protocol Type=CXL.io，读取Base Address字段并使用该信息访问RCRB AER寄存器，以确定是否有任何错误记录在那里
>   - 若Protocol Type=CXL.cachemem，读取Base Address字段并使用该信息访问组件寄存器RAS能力寄存器（见Section 8.2.4.17），以确定是否有任何错误记录在那里
>
> Else:
> - Probe all CXL Downstream Ports and determine whether they have logged an error in the CXL.io or CXL.cachemem status registers
>
> 否则：
> - 探测所有CXL下游端口并确定它们是否在CXL.io或CXL.cachemem状态寄存器中记录了错误

<br>

**Table 9-25. CSDS Structure | CSDS结构**

<table>
<thead><tr><th width="28%">Field | 字段</th><th width="10%">Length (Bytes) | 长度（字节）</th><th width="12%">Byte Offset | 字节偏移</th><th width="50%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>Type | 类型</td><td>1</td><td>00h</td><td>4 = Indicates that this is a CSDS entry | 4 = 表示这是一个CSDS条目</td></tr>
<tr><td>Reserved | 保留</td><td>1</td><td>01h</td><td>Reserved | 保留</td></tr>
<tr><td>Record Length | 记录长度</td><td>2</td><td>02h</td><td>Length of this record = 08h | 此记录的长度 = 08h</td></tr>
<tr><td>System Capabilities | 系统能力</td><td>2</td><td>04h</td><td>A bitmap that describes system-wide capabilities. More than one bit within this field is permitted to be set.<br>· <b>Bit[0]: Cmp-M</b>: — 1 = System is configured for use with devices that return modified data using the Cmp-M response.<br>· <b>Bit[1]: No Clean Writeback</b>: Specifies the clean writeback behavior of the host. — 0 = The host may or may not generate clean writebacks — 1 = The host guarantees to never generate clean writeback transactions at the host's cacheline granularity.<br>· <b>Bit[2]: Viral Policy</b>: If 1, the system policy is to enable Viral.<br>· <b>Bits[5:3]: Metabits Storage Configuration</b>. Upon hot-add, the OS may configure the device to match host metadata storage requirements:<br>&nbsp;&nbsp;— 0h: 2 bits of Metadata<br>&nbsp;&nbsp;— 1h: No Metadata<br>&nbsp;&nbsp;— 2h: 1 bit of Metadata, bit-0 of Meta0-State Value<br>&nbsp;&nbsp;— 3h: 1 bit of Metadata, bit-1 of Meta0-State Value<br>&nbsp;&nbsp;— 4h: 2 bits of Metadata + 1 TE State bit<br>&nbsp;&nbsp;— 5h: No Metadata + 1 TE State bit<br>&nbsp;&nbsp;— 6h: 1 bit of Metadata, bit-0 of Meta0-State Value + 1 TE State bit<br>&nbsp;&nbsp;— 7h: 1 bit of Metadata, bit-1 of Meta0-State Value + 1 TE State bit<br>· <b>Bits[15:6]: Reserved</b> | 描述系统级能力的位图。此字段中允许多个位同时被设置。<br>· <b>Bit[0]: Cmp-M</b>： — 1 = 系统配置为与使用Cmp-M响应返回已修改数据的设备一起使用。<br>· <b>Bit[1]: No Clean Writeback（无清写回）</b>：指定主机的清写回行为。 — 0 = 主机可能生成也可能不生成清写回 — 1 = 主机保证绝不会以主机的缓存行粒度生成清写回事务。<br>· <b>Bit[2]: Viral Policy（Viral策略）</b>：若为1，系统策略为启用Viral。<br>· <b>Bits[5:3]: Metabits Storage Configuration（元位存储配置）</b>。热添加时，OS可将设备配置为匹配主机元数据存储要求：<br>&nbsp;&nbsp;— 0h：2位元数据<br>&nbsp;&nbsp;— 1h：无元数据<br>&nbsp;&nbsp;— 2h：1位元数据，Meta0-State Value的位0<br>&nbsp;&nbsp;— 3h：1位元数据，Meta0-State Value的位1<br>&nbsp;&nbsp;— 4h：2位元数据 + 1个TE State位<br>&nbsp;&nbsp;— 5h：无元数据 + 1个TE State位<br>&nbsp;&nbsp;— 6h：1位元数据，Meta0-State Value的位0 + 1个TE State位<br>&nbsp;&nbsp;— 7h：1位元数据，Meta0-State Value的位1 + 1个TE State位<br>· <b>Bits[15:6]: Reserved（保留）</b></td></tr>
<tr><td>Reserved | 保留</td><td>2</td><td>06h</td><td>Reserved | 保留</td></tr>
</tbody></table>

---

<a id="sec-9-18-2"></a>
### 9.18.2 CXL _OSC | CXL _OSC

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

According to ACPI Specification, _OSC (Operating System Capabilities) is a control method that is used by OSs to communicate to the System Firmware the capabilities supported by the OS and to negotiate ownership of specific capabilities. The _OSC interface defined in this section applies only to "Host Bridge" ACPI devices that originate CXL hierarchies. As specified in Section 9.12, these ACPI devices must have an _HID of (or a _CID that includes) EISAID("ACPI0016"). CXL _OSC is required for a CXL VH. CXL _OSC is optional for an RCD. A CXL Host Bridge also originates a PCIe hierarchy and will have a _CID of EISAID("PNP0A08"). As such, a CXL Host Bridge device may expose both CXL _OSC and PCIe _OSC.

</td><td style="background-color:#e8e8e8">

根据ACPI规范，_OSC（操作系统能力，Operating System Capabilities）是一种控制方法，操作系统使用它向系统固件传达操作系统支持的能力，并协商特定能力的所有权。本节中定义的_OSC接口仅适用于发起CXL层次结构的"Host Bridge"ACPI设备。如Section 9.12所述，这些ACPI设备必须具有_HID为（或_CID包含）EISAID("ACPI0016")。CXL _OSC对于CXL VH是必需的。CXL _OSC对于RCD是可选的。CXL主机桥同时也发起PCIe层次结构，并将具有_CID为EISAID("PNP0A08")。因此，一个CXL主机桥设备可以同时暴露CXL _OSC和PCIe _OSC。

</td></tr>
<tr><td>

The _OSC interface for a CXL Host Bridge is identified by the Universal Unique Identifier (UUID) 68f2d50b-c469-4d8a-bd3d-941a103fd3fc. A revision ID of 1 encompasses fields defined within this section, composed of 5 DWORDs, as listed in Table 9-26.

</td><td style="background-color:#e8e8e8">

CXL主机桥的_OSC接口由通用唯一标识符（UUID）68f2d50b-c469-4d8a-bd3d-941a103fd3fc标识。修订ID为1，涵盖本节中定义的字段，由5个DWORD组成，如Table 9-26所列。

</td></tr>
</tbody></table>

<br>

**Table 9-26. _OSC Capabilities Buffer DWORDs | _OSC能力缓冲区DWORD**

<table>
<thead><tr><th width="10%">_OSC Capabilities Buffer DWORD #</th><th width="90%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>1</td><td>Contains bits that are generic to _OSC and defined by ACPI. These include status and error information. | 包含_OSC通用且由ACPI定义的位。这些包括状态和错误信息。</td></tr>
<tr><td>2</td><td>PCIe Support Field as defined by PCI Firmware Specification. | PCIe支持字段，由PCI固件规范定义。</td></tr>
<tr><td>3</td><td>PCIe Control Field as defined by PCI Firmware Specification. | PCIe控制字段，由PCI固件规范定义。</td></tr>
<tr><td>4</td><td><b>CXL Support Field</b>: Bits defined in the CXL Support Field provide information regarding CXL features supported by the OS. Just like the PCIe Support field, contents in the CXL Support Field are passed in a single direction; the OS will disregard any changes to this field when returned. | <b>CXL支持字段</b>：CXL支持字段中定义的位提供有关操作系统支持的CXL功能的信息。与PCIe支持字段一样，CXL支持字段中的内容以单向传递；操作系统将忽略返回时对此字段所做的任何更改。</td></tr>
<tr><td>5</td><td><b>CXL Control Field</b>: Just like the PCIe Control Field, bits defined in the CXL Control Field are used to submit OS requests for control/handling of the associated feature, typically including but not limited to features that utilize native interrupts or events that are handled by an OS-level driver. If any bits in the CXL Control Field are returned cleared (i.e., masked to 0) by the _OSC control method, the respective feature is designated as unsupported by the platform and must not be enabled by the OS. Some of these features may be controlled by System Firmware prior to OS boot or during runtime for an OS that is unaware of these features, while others may be disabled/inoperative until native OS support for such features is available. If the CXL _OSC control method is absent from the scope of a Host Bridge device, then the OS must not enable or attempt to use any features defined in this section for the hierarchy originated by the Host Bridge. Doing so could conflict with System Firmware operations, or produce undesired results. It is recommended that a machine with multiple Host Bridge devices should report the same capabilities for all Host Bridges, and also negotiate control of the features described in the CXL Control Field in the same way for all Host Bridges. | <b>CXL控制字段</b>：与PCIe控制字段一样，CXL控制字段中定义的位用于提交操作系统对关联功能的控制/处理请求，通常包括但不限于使用本地中断或由OS级驱动程序处理的事件的功能。如果CXL控制字段中的任何位被_OSC控制方法返回为清除（即被掩码为0），则相应功能被指定为平台不支持，操作系统必须不启用该功能。这些功能中的某些可能在操作系统引导之前由系统固件控制，或者在不了解这些功能的操作系统的运行时期间由系统固件控制，而其他功能可能在此类功能的本地操作系统支持可用之前被禁用/不可操作。如果CXL _OSC控制方法在主机桥设备的作用域中不存在，则操作系统必须不为该主机桥发起的层次结构启用或尝试使用本节中定义的任何功能。这样做可能与系统固件操作冲突，或产生不希望的结果。建议具有多个主机桥设备的机器应为所有主机桥报告相同的能力，并以相同的方式为所有主机桥协商CXL控制字段中描述的功能的控制。</td></tr>
</tbody></table>

<br>

**Table 9-27. Interpretation of CXL _OSC Support Field | CXL _OSC支持字段解释**

<table>
<thead><tr><th width="10%">Support Field Bit Offset | 支持字段位偏移</th><th width="90%">Interpretation | 解释</th></tr></thead>
<tbody>
<tr><td>0</td><td><b>RCD and RCH Port Register Access Supported | RCD和RCH端口寄存器访问支持</b><br>The OS sets this bit to 1 if it supports access to RCD and RCH Port registers as defined in Section 9.11. Otherwise, the OS clears this bit to 0. | 若操作系统支持访问Section 9.11中定义的RCD和RCH端口寄存器，则将此位设置为1。否则，操作系统将此位清除为0。</td></tr>
<tr><td>1</td><td><b>CXL VH Register Access Supported | CXL VH寄存器访问支持</b><br>The OS sets this bit to 1 if it supports access to CXL VH component registers as defined in Section 9.12. If this bit is 1, bit 0 must also be 1. Otherwise, the OS clears this bit to 0. | 若操作系统支持访问Section 9.12中定义的CXL VH组件寄存器，则将此位设置为1。如果此位为1，则位0也必须为1。否则，操作系统将此位清除为0。</td></tr>
<tr><td>2</td><td><b>CXL Protocol Error Reporting Supported | CXL协议错误报告支持</b><br>The OS sets this bit to 1 if it supports handling of CXL Protocol Errors. Otherwise, the OS clears this bit to 0. If the OS sets this bit, it must also set either bit 0 or bit 1 above. Note: Firmware may retain control of AER if the OS does not support CXL Protocol Error reporting because the owner of AER owns CXL Protocol error management. | 若操作系统支持CXL协议错误的处理，则将此位设置为1。否则，操作系统将此位清除为0。如果操作系统设置此位，则还必须设置上述位0或位1。注意：如果操作系统不支持CXL协议错误报告，固件可保留对AER的控制，因为AER的所有者拥有CXL协议错误管理权。</td></tr>
<tr><td>3</td><td><b>CXL Native Hot-Plug Supported | CXL本地热插拔支持</b><br>The OS sets this bit to 1 if it supports CXL hot-add and managed CXL Hot-Remove without firmware assistance. Otherwise, the OS clears this bit to 0. If the OS sets this bit, it must request PCIe Native Hot-Plug control. If PCIe Native Hot-Plug control is granted to the OS, such an OS must natively handle CXL Hot-Plug as well. If the OS sets this bit, it must also set bit 1 above. | 若操作系统支持在无固件辅助的情况下进行CXL热添加和受管理的CXL热移除，则将此位设置为1。否则，操作系统将此位清除为0。如果操作系统设置此位，则必须请求PCIe本地热插拔控制。如果PCIe本地热插拔控制被授予操作系统，这样的操作系统也必须本地处理CXL热插拔。如果操作系统设置此位，则还必须设置上述位1。</td></tr>
<tr><td>4-31</td><td>Reserved | 保留</td></tr>
</tbody></table>

---

<a id="sec-9-18-2-1"></a>
### 9.18.2.1 Rules for Evaluating _OSC | _OSC评估规则

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section defines when and how the OS must evaluate _OSC, as well as restrictions on firmware implementations.

</td><td style="background-color:#e8e8e8">

本节定义操作系统何时以及如何评估_OSC，以及对固件实现的限制。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-2-1-1"></a>
### 9.18.2.1.1 Query Support Flag | 查询支持标志

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

If the Query Support Flag (_OSC Capabilities Buffer DWORD 1, bit 0) is set by the OS while evaluating _OSC, hardware settings are not permitted to be changed by firmware in the context of the _OSC call. It is strongly recommended that the OS evaluate _OSC with the Query Support Flag set until _OSC returns the Capabilities Masked bit cleared to negotiate the set of features to be granted to the OS for native support. A platform may require a specific combination of features to be natively supported by an OS before granting native control of a given feature.

</td><td style="background-color:#e8e8e8">

如果操作系统在评估_OSC时设置了查询支持标志（_OSC Capabilities Buffer DWORD 1, bit 0），则不允许固件在_OSC调用的上下文中更改硬件设置。强烈建议操作系统在评估_OSC时设置查询支持标志，直到_OSC返回Capabilities Masked位被清除，以协商授予操作系统本地支持的功能集。平台可能要求操作系统本地支持特定的功能组合后，才授予对给定功能的本地控制。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-2-1-2"></a>
### 9.18.2.1.2 Evaluation Conditions | 评估条件

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The OS must evaluate _OSC under the following conditions:
- During initialization of any driver that provides native support for features described in the section above. These features may be supported by one or many drivers, but should be evaluated only by the main bus driver for that hierarchy. Secondary drivers must coordinate with the bus driver to install support for these features. Drivers shall not relinquish control of previously obtained features. That is, bits set in _OSC Capabilities Buffer DWORD 3 and DWORD 5 after the negotiation process must be set on all subsequent negotiation attempts.
- When a Notify(\<device\>, 8) is delivered to the CXL Host Bridge device.
- Upon resume from S4, System Firmware will handle context restoration when resuming from S1 through S3.

</td><td style="background-color:#e8e8e8">

操作系统必须在以下条件下评估_OSC：
- 在任何为上述章节中描述的功能提供本地支持的驱动程序初始化期间。这些功能可由一个或多个驱动程序支持，但应仅由该层次结构的主总线驱动程序进行评估。辅助驱动程序必须与总线驱动程序协调以安装对这些功能的支持。驱动程序不得放弃先前获得的功能的控制。也就是说，协商过程后在_OSC Capabilities Buffer DWORD 3和DWORD 5中设置的位必须在所有后续协商尝试中保持设置。
- 当Notify(\<device\>, 8)被递送到CXL主机桥设备时。
- 从S4恢复时。系统固件将在从S1到S3恢复时处理上下文恢复。

</td></tr>
<tr><td>

If a CXL Host Bridge device exposes CXL _OSC, CXL-aware OSPM shall evaluate CXL _OSC and not evaluate PCIe _OSC.

</td><td style="background-color:#e8e8e8">

如果CXL主机桥设备暴露了CXL _OSC，则支持CXL的OSPM应评估CXL _OSC而非评估PCIe _OSC。

</td></tr>
</tbody></table>

<br>

**Table 9-28. Interpretation of CXL _OSC Control Field, Passed in via Arg3 | CXL _OSC控制字段解释，通过Arg3传入**

<table>
<thead><tr><th width="10%">Control Field Bit Offset | 控制字段位偏移</th><th width="90%">Interpretation | 解释</th></tr></thead>
<tbody>
<tr><td>0</td><td><b>CXL Memory Error Reporting Control | CXL内存错误报告控制</b><br>The OS sets this bit to 1 to request control over CXL Memory Error Reporting i.e. Set Event Interrupt Policy command for devices that implement Memory Device Commands (see Section 8.2.10.9). If the OS sets this bit, the OS must also set either bit 0 or bit 1 in the CXL _OSC Support Field (see Table 9-26). | 操作系统将此位设置为1以请求对CXL内存错误报告的控制，即对实现内存设备命令（Memory Device Commands）的设备执行Set Event Interrupt Policy命令（见Section 8.2.10.9）。如果操作系统设置此位，则操作系统还必须设置CXL _OSC支持字段（见Table 9-26）中的位0或位1。</td></tr>
<tr><td>1-31</td><td>Reserved | 保留</td></tr>
</tbody></table>

<br>

**Table 9-29. Interpretation of CXL _OSC Control Field, Returned Value | CXL _OSC控制字段解释，返回值**

<table>
<thead><tr><th width="10%">Control Field Bit Offset | 控制字段位偏移</th><th width="90%">Interpretation | 解释</th></tr></thead>
<tbody>
<tr><td>0</td><td><b>CXL Memory Error Reporting Control | CXL内存错误报告控制</b><br>The firmware sets this bit to 1 to grant control over CXL Memory Expander Error Reporting i.e. Set Event Interrupt Policy command for devices that implement Memory Device Commands (see Section 8.2.10.9). If firmware grants control of this feature, firmware must ensure that these devices are not configured in Firmware First error reporting mode. If control of this feature was requested and denied or was not requested, firmware returns this bit cleared to 0. | 固件将此位设置为1以授予对CXL内存扩展器错误报告的控制，即对实现内存设备命令（Memory Device Commands）的设备执行Set Event Interrupt Policy命令（见Section 8.2.10.9）。如果固件授予此功能的控制权，固件必须确保这些设备未配置为固件优先（Firmware First）错误报告模式。如果此功能的控制被请求但被拒绝，或未被请求，固件将此位清除为0返回。</td></tr>
<tr><td>1-31</td><td>Reserved | 保留</td></tr>
</tbody></table>

---

<a id="sec-9-18-2-1-3"></a>
### 9.18.2.1.3 Sequence of _OSC Calls | _OSC调用序列

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The following rules govern sequences of calls to _OSC that are issued to the same Host Bridge and occur within the same boot:
- The OS is permitted to evaluate _OSC an arbitrary number of times.
- If the OS declares support of a feature in the Status Field in one call to _OSC, then it must preserve the set state of that bit (and thereby declare support for that feature) in all subsequent calls.
- If the OS is granted control of a feature in the Control Field in one call to _OSC, then it must preserve the set state of that bit (requesting that feature) in all subsequent calls.
- Firmware shall not reject control of any feature it has previously granted control to.
- There is no mechanism for the OS to relinquish control of a previously requested and granted feature.

</td><td style="background-color:#e8e8e8">

以下规则约束在同一引导周期内向同一主机桥发出的_OSC调用序列：
- 操作系统可任意次数评估_OSC。
- 如果操作系统在一次_OSC调用中在状态字段中声明支持某个功能，则必须在所有后续调用中保持该位的设置状态（从而声明对该功能的支持）。
- 如果操作系统在一次_OSC调用中被授予控制字段中某个功能的控制权，则必须在所有后续调用中保持该位的设置状态（请求该功能）。
- 固件不得拒绝控制其先前已授予控制权的任何功能。
- 操作系统没有放弃先前请求并已授予的功能的控制权的机制。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-2-1-4"></a>
### 9.18.2.1.4 ASL Example | ASL示例

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

```
Device(CXL0) {
  Name(_HID,EISAID("ACPI0016")) // CXL Host Bridge
  Name(_CID, Package(2) {
    EISAID("PNP0A03"), // PCI Compatible Host Bridge
    EISAID("PNP0A08")  // PCI Express Compatible Host Bridge
  })
  Name(SUPP,0)   // PCI _OSC Support Field value
  Name(CTRL,0)   // PCI _OSC Control Field value
  Name(SUPC,0)   // CXL _OSC Support Field value
  Name(CTRC,0)   // CXL _OSC Control Field value

  Method(_OSC,4) {
    // Check for proper UUID
    If(LEqual(Arg0,ToUUID("68f2d50b-c469-4d8a-bd3d-941a103fd3fc"))) {
      // Create DWord-addressable fields from the Capabilities Buffer
      CreateDWordField(Arg3,0,CDW1)
      CreateDWordField(Arg3,4,CDW2)
      CreateDWordField(Arg3,8,CDW3)
      CreateDWordField(Arg3,12,CDW4)
      CreateDWordField(Arg3,16,CDW5)
      // Save Capabilities DWord2, 3, 4, 5
      Store(CDW2,SUPP)
      Store(CDW3,CTRL)
      Store(CDW4,SUPC)
      Store(CDW5,CTRC)
      ..
      ..
    } Else {
      Or(CDW1,4,CDW1) // Unrecognized UUID
      Return(Arg3)
    }
  } // End _OSC
  // Other methods such as _BBN, _CRS, PCIe _OSC
} //End CXL0
```

</td><td style="background-color:#e8e8e8">

```
Device(CXL0) {
  Name(_HID,EISAID("ACPI0016")) // CXL 主机桥
  Name(_CID, Package(2) {
    EISAID("PNP0A03"), // PCI 兼容主机桥
    EISAID("PNP0A08")  // PCI Express 兼容主机桥
  })
  Name(SUPP,0)   // PCI _OSC 支持字段值
  Name(CTRL,0)   // PCI _OSC 控制字段值
  Name(SUPC,0)   // CXL _OSC 支持字段值
  Name(CTRC,0)   // CXL _OSC 控制字段值

  Method(_OSC,4) {
    // 检查正确的UUID
    If(LEqual(Arg0,ToUUID("68f2d50b-c469-4d8a-bd3d-941a103fd3fc"))) {
      // 从能力缓冲区创建DWord可寻址字段
      CreateDWordField(Arg3,0,CDW1)
      CreateDWordField(Arg3,4,CDW2)
      CreateDWordField(Arg3,8,CDW3)
      CreateDWordField(Arg3,12,CDW4)
      CreateDWordField(Arg3,16,CDW5)
      // 保存能力DWord2、3、4、5
      Store(CDW2,SUPP)
      Store(CDW3,CTRL)
      Store(CDW4,SUPC)
      Store(CDW5,CTRC)
      ..
      ..
    } Else {
      Or(CDW1,4,CDW1) // 无法识别的UUID
      Return(Arg3)
    }
  } // End _OSC
  // 其他方法如 _BBN, _CRS, PCIe _OSC
} //End CXL0
```

</td></tr>
</tbody></table>

---

<a id="sec-9-18-3"></a>
### 9.18.3 CXL Root Device Specific Methods (_DSM) | CXL根设备特定方法

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

_DSM is a control method that enables devices to provide device-specific functions for the benefit of the device driver. See ACPI Specification for details. Table 9-30 lists the _DSM Functions that are associated with the CXL Root Device (HID="ACPI0017").

</td><td style="background-color:#e8e8e8">

_DSM是一种控制方法，使设备能够提供设备特定功能以服务于设备驱动程序。详见ACPI规范。Table 9-30列出了与CXL根设备（HID="ACPI0017"）关联的_DSM函数。

</td></tr>
</tbody></table>

<br>

**Table 9-30. _DSM Definitions for CXL Root Device | CXL根设备的_DSM定义**

<table>
<thead><tr><th width="35%">UUID</th><th width="8%">Revision</th><th width="12%">Function Index</th><th width="45%">Description | 描述</th></tr></thead>
<tbody>
<tr><td>F365F9A6-A7DE-4071-A66A-B40C0B4F8E52</td><td>1</td><td>1</td><td>Retrieve QTG ID (see Section 9.18.3.1) | 获取QTG ID（见Section 9.18.3.1）</td></tr>
<tr><td></td><td>-</td><td>All other</td><td>Reserved | 保留</td></tr>
</tbody></table>

<br>

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

All other Function values are reserved. The Revision field represents the version of the individual _DSM Function. The Revision associated with a _DSM Function is incremented whenever that _DSM Function is extended to add more functionality. Backward compatibility shall be maintained during this process. Specifically, for all values of n, a _DSM Function with Revision n+1 may extend Revision ID n by assigning meaning to the fields that are marked as reserved in Revision n but must not redefine the meaning of existing fields and must not change the size or type of I/O parameters. Software that was written for a lower Revision may continue to operate on _DSM Functions with a higher Revision but will not be able to take advantage of new functionality. It is legal for software to invoke a _DSM Function and pass in any nonzero Revision ID value that does not exceed the Revision ID defined in this specification for that _DSM Function. For example, if the most-current version of this specification defines Revision ID=4 for _DSM Function Index f, software is permitted to invoke the _DSM Function with Function Index f with a Revision ID value that belongs to the set {1, 2, 3, 4}.

</td><td style="background-color:#e8e8e8">

所有其他函数值均保留。修订字段表示各个_DSM函数的版本。每当_DSM函数被扩展以添加更多功能时，与该_DSM函数关联的修订号递增。在此过程中应保持向后兼容性。具体而言，对于所有n的值，具有修订n+1的_DSM函数可以通过为在修订n中标记为保留的字段赋予含义来扩展修订ID n，但不得重新定义现有字段的含义，且不得更改I/O参数的大小或类型。为较低修订号编写的软件可以继续在具有较高修订号的_DSM函数上运行，但将无法利用新功能。软件调用_DSM函数并传入任何不超过本规范为该_DSM函数定义的修订ID的非零修订ID值是合法的。例如，如果本规范的最新版本为_DSM函数索引f定义了修订ID=4，则允许软件使用函数索引f调用_DSM函数，并传入属于集合{1, 2, 3, 4}的修订ID值。

</td></tr>
</tbody></table>

---

<a id="sec-9-18-3-1"></a>
### 9.18.3.1 _DSM Function for Retrieving QTG ID | 获取QTG ID的_DSM函数

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

This section describes how the OSPM can request the firmware to determine the optimum QoS Throttling Group (QTG) to which a device HDM range should be assigned, based on its performance characteristics. It is strongly recommended that OSPM evaluate this _DSM Function to retrieve QTG recommendations and map the device HDM range to an HPA range that is described by a CFMWS entry that follows the platform recommendations. For each Device Scoped Memory Affinity Structure (DSMAS) in the Device CDAT, the OSPM should calculate the Read Latency, Write Latency, Read Bandwidth, and Write Bandwidth from the CXL Root Port within the same VCS. The term DSMAS is defined in Coherent Device Attribute Table Specification. This calculation must consider the latency and bandwidth contribution of any intermediate switches.

</td><td style="background-color:#e8e8e8">

本节描述OSPM如何请求固件确定设备HDM范围应分配到的、与其性能特征相匹配的最佳QoS节流组（QTG）。强烈建议OSPM评估此_DSM函数以获取QTG推荐，并将设备HDM范围映射到由遵循平台推荐的CFMWS条目描述的HPA范围。对于设备CDAT中的每个设备范围内存亲和性结构（DSMAS），OSPM应计算从同一VCS内的CXL根端口出发的读延迟、写延迟、读带宽和写带宽。术语DSMAS在Coherent Device Attribute Table规范中定义。此计算必须考虑任何中间交换机的延迟和带宽贡献。

</td></tr>
<tr><td>

The OSPM should call this _DSM with the performance characteristics for the Device HDM range thus calculated, utilize the return ID value(s) to pick an appropriate CFMWS, and then map the DSMAS DPA range to HPAs that are covered by that CFMWS. This process may be repeated for each DSMAS memory range that the OSPM wishes to utilize from the device.

</td><td style="background-color:#e8e8e8">

OSPM应使用由此计算得出的设备HDM范围的性能特征调用此_DSM，利用返回的ID值选择合适的CFMWS，然后将DSMAS的DPA范围映射到该CFMWS覆盖的HPA。对于OSPM希望从设备中使用的每个DSMAS内存范围，可重复此过程。

</td></tr>
</tbody></table>

<br>

**Arguments and Return Values | 参数与返回值**

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

**Location:** This object shall be a child of the CXL Root Device (HID="ACPI0017").

</td><td style="background-color:#e8e8e8">

**位置：** 此对象应为CXL根设备（HID="ACPI0017"）的子对象。

</td></tr>
<tr><td>

**Arguments:**
- Arg0: UUID: f365f9a6-a7de-4071-a66a-b40c0b4f8e52
- Arg1: Revision ID: 1
- Arg2: Function Index: 01h
- Arg3: A package of memory device performance characteristic. The package consists of 4 DWORDs.

</td><td style="background-color:#e8e8e8">

**参数：**
- Arg0：UUID：f365f9a6-a7de-4071-a66a-b40c0b4f8e52
- Arg1：修订ID：1
- Arg2：函数索引：01h
- Arg3：一个内存设备性能特征包。该包由4个DWORD组成。

</td></tr>
<tr><td>

```
Package {
  Read Latency
  Write Latency
  Read Bandwidth
  Write Bandwidth
}
```

</td><td style="background-color:#e8e8e8">

```
Package {
  读延迟 (Read Latency)
  写延迟 (Write Latency)
  读带宽 (Read Bandwidth)
  写带宽 (Write Bandwidth)
}
```

</td></tr>
<tr><td>

**Return:** A package containing two elements - a WORD that returns the maximum throttling group that the platform supports, and a package containing the QTG ID(s) that the platform recommends.

```
Package {
  Max Supported QTG ID
  Package {QTG Recommendations}
}
```

</td><td style="background-color:#e8e8e8">

**返回：** 一个包含两个元素的包——一个返回平台支持的最大节流组的WORD，以及一个包含平台推荐的QTG ID的包。

```
Package {
  最大支持的QTG ID (Max Supported QTG ID)
  Package {QTG推荐 (QTG Recommendations)}
}
```

</td></tr>
</tbody></table>

<br>

**Table 9-31. _DSM for Retrieving QTG, Inputs, and Outputs | 获取QTG的_DSM：输入与输出**

<table>
<thead><tr><th width="15%">Field | 字段</th><th width="8%">Size | 大小</th><th width="77%">Description | 描述</th></tr></thead>
<tbody>
<tr><td colspan="3"><b>Input Package: | 输入包：</b></td></tr>
<tr><td>Read Latency | 读延迟</td><td>DWORD</td><td>The best-case read latency as measured from the CXL root port within the same VCS, expressed in picoseconds. | 从同一VCS内的CXL根端口测量的最佳情况读延迟，以皮秒为单位表示。</td></tr>
<tr><td>Write Latency | 写延迟</td><td>DWORD</td><td>The best-case write latency as measured from the CXL root port within the same VCS, expressed in picoseconds. | 从同一VCS内的CXL根端口测量的最佳情况写延迟，以皮秒为单位表示。</td></tr>
<tr><td>Read Bandwidth | 读带宽</td><td>DWORD</td><td>The best-case read bandwidth as measured from the CXL root port within the same VCS, expressed in MB/s. | 从同一VCS内的CXL根端口测量的最佳情况读带宽，以MB/s为单位表示。</td></tr>
<tr><td>Write Bandwidth | 写带宽</td><td>DWORD</td><td>The best-case write bandwidth as measured from the CXL root port within the same VCS, expressed in MB/s. | 从同一VCS内的CXL根端口测量的最佳情况写带宽，以MB/s为单位表示。</td></tr>
<tr><td colspan="3"><b>Return Package: | 返回包：</b></td></tr>
<tr><td>Max Supported QTG ID | 最大支持的QTG ID</td><td>WORD</td><td>The highest QTG ID supported by the platform. The platform must be capable of supporting all QTGs whose ID, Q, satisfies the following equation: 0 &le; Q &le; Max Supported QTG ID. For every value of Q, there may be zero or more CFMWS entries. | 平台支持的最高QTG ID。平台必须能够支持其ID Q满足以下等式的所有QTG：0 &le; Q &le; Max Supported QTG ID。对于每个Q值，可能存在零个或多个CFMWS条目。</td></tr>
<tr><td>QTG Recommendations | QTG推荐</td><td>Package</td><td>A package that consists of 0 or more WORD elements. It is a prioritized list of QTG IDs that are considered acceptable by the platform for the specified performance characteristics. If the package contains more than one element, element[n] is preferred by the platform over element[n+1]. If the package is empty, the platform is unable to find any suitable QTGs for this set of input values. If the OSPM does not follow platform QTG recommendations, it may result in severe performance degradation. Every element in this package must be no greater than the Max Supported QTG ID above. For example, if QTG Recommendations = Package () {2, 1}, the OSPM should first attempt to assign from QTG ID 2, and then attempt to assign QTG ID 1 if an assignment cannot be found in QTG ID 2. | 由0个或多个WORD元素组成的包。它是一个优先级排序的QTG ID列表，这些ID被平台认为对指定的性能特征是可接受的。如果包中包含多个元素，element[n]较element[n+1]更受平台偏好。如果包为空，则平台无法为此组输入值找到任何合适的QTG。如果OSPM不遵循平台的QTG推荐，可能导致严重的性能下降。此包中的每个元素不得大于上述Max Supported QTG ID。例如，如果QTG Recommendations = Package () {2, 1}，则OSPM应首先尝试从QTG ID 2分配，如果无法在QTG ID 2中找到分配，则尝试分配QTG ID 1。</td></tr>
</tbody></table>

---

[⬆️ 返回目录](#-本章补充目录)

## 本章补充目录

- [9.19 可管理性模型](#sec-9-19)
- [9.20 组件命令接口](#sec-9-20)
  - [9.20.1 CCI 属性](#sec-9-20-1)
  - [9.20.2 基于MCTP的CCI属性](#sec-9-20-2)

---

<a id="sec-9-19"></a>
### 9.19 Manageability Model for CXL Devices | CXL 设备的可管理性模型

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Manageability is the set of capabilities that a managed entity exposes to a management entity. In the context of CXL, a CXL device is the managed entity. These capabilities are generally classified in sensors and effectors. An Event Log is an example of a sensor, whereas the ability to update the device firmware is an example of an effector. Sensors and effectors can either be accessed in-band (i.e., by OS/VMM resident software), or out-of-band (i.e., by firmware running on a management controller that is OS independent). In-band software can access a CXL device's manageability capabilities by issuing PCIe configuration read/write or MMIO read/write transactions to its Mailbox registers. These accesses are generally mediated by the CXL device driver. This is consistent with how PCIe adapters are managed. Out-of-band manageability in S0 state can leverage transports for which an MCTP binding specification has been defined. This assumes that the CXL.io path will decode and forward MCTP over PCIe VDMs in both directions. Form factors, such as PCIe CEM Specification, provision two SMBUS pins (clock and data). The SMBUS path can be used for out-of-band manageability in Sx state or in the Link Down case. This is consistent with PCIe adapters. CXL components may also support additional management capabilities defined in other specifications, such as Platform-Level Data Model (PLDM).

</td><td style="background-color:#e8e8e8">

可管理性是受管实体向管理实体暴露的一组能力。在 CXL 的上下文中，CXL 设备即为受管实体。这些能力通常分为传感器和执行器两类。事件日志是传感器的一个示例，而更新设备固件的能力则是执行器的一个示例。传感器和执行器可通过带内方式（即由 OS/VMM 驻留软件）或带外方式（即由运行在管理控制器上的、独立于 OS 的固件）进行访问。带内软件可通过向 CXL 设备的 Mailbox 寄存器发出 PCIe 配置读/写或 MMIO 读/写事务来访问 CXL 设备的可管理性能力。这些访问通常由 CXL 设备驱动程序进行中介处理。这与 PCIe 适配器的管理方式一致。在 S0 状态下，带外可管理性可利用已定义了 MCTP 绑定规范的传输层协议。其前提是 CXL.io 路径能够在两个方向上解码并转发基于 PCIe VDM 的 MCTP 报文。某些外形规格（如 PCIe CEM 规范）提供了两根 SMBUS 引脚（时钟和数据）。SMBUS 路径可用于 Sx 状态或链路断开情况下的带外可管理性。这与 PCIe 适配器的做法一致。CXL 组件也可支持其他规范中定义的额外管理能力，例如平台级数据模型（PLDM）。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-20"></a>
### 9.20 Component Command Interface | 组件命令接口

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Runtime management of CXL components is facilitated by a Component Command Interface (CCI). A CCI represents a command target that is used to process management and configuration commands that are issued to the component. Table 8-49, Table 8-141, and Table 8-230 define the commands that a CCI can support. A component can implement multiple CCIs of varying types that operate independently of one another and that have a uniquely defined list of supported commands. There are 2 types of CCIs: • CXL Mailbox Registers: A component can expose up to 2 CXL mailboxes through its Mailbox registers for every instance of CXL Device Registers, as defined in Section 8.2.9.4. Each mailbox represents a unique CCI instance. • MCTP-based CCIs: Components with MCTP-capable interconnects can expose up to 1 CCI per interconnect. There is a 1:1 relationship between the component's MCTP-based CCIs and MCTP-capable interconnects. Transfer of commands via MCTP uses the transport protocol defined in Section 7.6.3. All CCIs shall comply with the properties described in Section 9.20.1.

</td><td style="background-color:#e8e8e8">

CXL 组件的运行时管理通过组件命令接口（CCI）来实现。CCI 代表一个命令目标，用于处理发往该组件的管理与配置命令。表 8-49、表 8-141 和表 8-230 定义了 CCI 可支持的命令。一个组件可实现多个不同类型的 CCI，这些 CCI 彼此独立运行，且各自拥有一组唯一定义的支持命令。CCI 有两种类型：• CXL Mailbox 寄存器：如第 8.2.9.4 节所定义，组件可为其每个 CXL 设备寄存器实例通过 Mailbox 寄存器暴露最多两个 CXL mailbox。每个 mailbox 代表一个唯一的 CCI 实例。• 基于 MCTP 的 CCI：具有 MCTP 能力互连的组件可为每个互连暴露最多一个 CCI。组件的基于 MCTP 的 CCI 与具有 MCTP 能力的互连之间存在 1:1 的对应关系。通过 MCTP 传输命令使用第 7.6.3 节中定义的传输协议。所有 CCI 均应遵守第 9.20.1 节所述的属性。

</td></tr>
</tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-20-1"></a>
### 9.20.1 CCI Properties | CCI 属性

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

Components that implement more than one CCI shall process commands from those CCIs in a manner that avoids starvation so that commands submitted to one CCI do not prevent commands from other CCIs from being handled. The exact algorithm for accepting commands from multiple CCIs is implementation specific.

</td><td style="background-color:#e8e8e8">

实现多于一个 CCI 的组件应以避免饥饿的方式处理来自这些 CCI 的命令，确保提交到某个 CCI 的命令不会阻止来自其他 CCI 的命令得到处理。从多个 CCI 接受命令的具体算法由实现自行决定。

</td></tr>
<tr><td>

Each CCI within a component reports its supported command list through the Command Effects Log (CEL), as described in Section 8.2.10.5.2.1. Interface-specific properties of commands, background operation, and timeouts are defined in Section 8.2.9.4 for mailbox CCIs and in Section 9.20.2 for MCTP-based CCIs.

</td><td style="background-color:#e8e8e8">

组件内的每个 CCI 通过命令效果日志（CEL）报告其支持的命令列表，如第 8.2.10.5.2.1 节所述。命令的接口特定属性、后台操作和超时分别在第 8.2.9.4 节（针对 mailbox CCI）和第 9.20.2 节（针对基于 MCTP 的 CCI）中定义。

</td></tr>
<tr><td>

Each CCI can support the execution of only one background command at a time. When a command is successfully started as a background operation, the component shall return the Background Command Started return code defined in Section 8.2.9.4.5.1. While the command is executing in the background, the component should update the percentage complete at least once per second. A component may return the Busy return code if a command is sent to initiate a Background Operation while a Background Operation is already running on any other CCI. An ongoing background command may be aborted by issuing a Request Abort Background Operation command on the same CCI (see Section 8.2.10.1.5).

</td><td style="background-color:#e8e8e8">

每个 CCI 一次只能支持执行一个后台命令。当命令成功以后台操作方式启动时，组件应返回第 8.2.9.4.5.1 节中定义的后台命令已启动返回码。当命令在后台执行时，组件应至少每秒更新一次完成百分比。如果任何其他 CCI 上已有后台操作正在运行，而又有命令被发送来启动后台操作，则组件可返回忙返回码。可通过在同一 CCI 上发出请求中止后台操作命令（参见第 8.2.10.1.5 节）来中止正在运行的后台命令。

</td></tr>
<tr><td>

Each CCI within a component shall maintain a unique context with respect to the following capabilities: • CEL content With respect to the following capabilities, the Primary and Secondary Mailbox Registers CCI instance pairs shall share the context, but the MCTP CCI within a component shall have a unique context • Events, including reading contents, clearing entries, and configuring interrupt settings

</td><td style="background-color:#e8e8e8">

组件内的每个 CCI 应在以下能力方面维护唯一的上下文：• CEL 内容。在以下能力方面，主 Mailbox 寄存器和辅助 Mailbox 寄存器 CCI 实例对应共享上下文，而组件内的 MCTP CCI 应具有唯一的上下文：• 事件，包括读取内容、清除条目和配置中断设置。

</td></tr>
</tbody></table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> <table>
> <thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
> <tbody>
> <tr><td>
>
> The CXL mailbox is derived from the PCIe standard MMIO Mailbox Capability (MMB) with extensions defined in Section 8.2.9.4 for supporting CXL defined commands. Therefore, the CXL mailbox may also support PCI-SIG defined commands (MMB Command Opcode Vendor ID = 0001h) or commands defined by other entities. However, non-CXL defined commands are not reported in the CXL CEL and discovery of those commands is outside of the scope of this specification. CXL components that need to be compatible with non-CXL aware software may advertise both the CXL Primary Mailbox (Vendor ID = 1E98h or 0000h, ID = 0002h) and the PCIe MMB (Vendor ID = 0001h, ID = 0001h). However, they are required to alias the PCIe MMB header to the CXL Primary Mailbox registers. Refer to Section 8.2.9, Figure 8-12. CXL components that do not need to be compatible with non-CXL aware software should only advertise the CXL Primary Mailbox and not the PCIe MMB.
>
> </td><td style="background-color:#e8e8e8">
>
> CXL mailbox 源自 PCIe 标准 MMIO Mailbox 能力（MMB），并带有第 8.2.9.4 节中为支持 CXL 定义命令而定义的扩展。因此，CXL mailbox 也可支持 PCI-SIG 定义的命令（MMB Command Opcode Vendor ID = 0001h）或由其他实体定义的命令。然而，非 CXL 定义的命令不会在 CXL CEL 中报告，且这些命令的发现过程不在本规范的范围内。需要与非 CXL 感知软件兼容的 CXL 组件可同时通告 CXL 主 Mailbox（Vendor ID = 1E98h 或 0000h，ID = 0002h）和 PCIe MMB（Vendor ID = 0001h，ID = 0001h）。但是，它们必须将 PCIe MMB 头部别名映射到 CXL 主 Mailbox 寄存器。参见第 8.2.9 节图 8-12。不需要与非 CXL 感知软件兼容的 CXL 组件应仅通告 CXL 主 Mailbox 而不通告 PCIe MMB。
>
> </td></tr>
> </tbody></table>

[⬆️ 返回目录](#-本章补充目录)

---

<a id="sec-9-20-2"></a>
### 9.20.2 MCTP-based CCI Properties | 基于 MCTP 的 CCI 属性

<table>
<thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
<tbody>
<tr><td>

The CCI command timeout is 2 seconds, measured from when the command has been received by the component to when the component has started to transmit its response. Components should respond within this time limit; otherwise, requesters may timeout. Requesters must account for round-trip transmission time in addition to the command timeout. MCTP-based CCIs report background operation status using the Background Operation Status command as defined in Section 8.2.10.1.2. In the event of a command timeout, the requester may retransmit the request. New Message Tags shall be used every time that a request is retransmitted. Requesters may discard responses that arrive after the command timeout period has lapsed.

</td><td style="background-color:#e8e8e8">

CCI 命令超时时间为 2 秒，从组件接收到命令时起算，到组件开始发送其响应时为止。组件应在此时间限制内做出响应；否则，请求方可能会超时。在命令超时之外，请求方还必须考虑往返传输时间。基于 MCTP 的 CCI 使用第 8.2.10.1.2 节中定义的后台操作状态命令报告后台操作状态。在发生命令超时的情况下，请求方可重传该请求。每次重传请求时必须使用新的 Message Tag。请求方可丢弃在命令超时时间过后到达的响应。

</td></tr>
<tr><td>

Commands sent to MCTP-based CCIs on MLD components are processed by the FM-owned LD.

</td><td style="background-color:#e8e8e8">

发送到 MLD 组件上基于 MCTP 的 CCI 的命令由 FM 拥有的 LD 进行处理。

</td></tr>
</tbody></table>

> **IMPLEMENTATION NOTE | 实现说明**
>
> <table>
> <thead><tr><th width="50%">🇬🇧 English</th><th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th></tr></thead>
> <tbody>
> <tr><td>
>
> It is recommended that components with multiple CCIs that support commands that run as Background Operations only advertise support for those commands on one CCI. Coordination between management entities attempting concurrent commands over separate CCIs that have component-level impact (e.g., FW update, etc.) is beyond the scope of this specification.
>
> </td><td style="background-color:#e8e8e8">
>
> 建议具有多个 CCI 且支持作为后台操作运行命令的组件仅在一个 CCI 上通告对这些命令的支持。管理实体之间通过不同 CCI 尝试并发执行具有组件级影响的命令（例如固件更新等）时的协调问题，不在本规范的范围内。
>
> </td></tr>
> <tr><td>
>
> MCTP-based CCIs are intended to provide a dedicated management interface that operates independently from the state of any of the component's CXL interfaces; it is strongly recommended, but not required, that commands initiated on MCTP-based CCIs are not interrupted by Conventional Resets or any other changes of state of a component's CXL interface(s).
>
> </td><td style="background-color:#e8e8e8">
>
> 基于 MCTP 的 CCI 旨在提供一个独立于组件任何 CXL 接口状态运行的专用管理接口；强烈建议（但不强制要求）在基于 MCTP 的 CCI 上发起的命令不被常规复位或组件 CXL 接口的任何其他状态变更所中断。
>
> </td></tr>
> </tbody></table>

[⬆️ 返回目录](#-本章补充目录)
