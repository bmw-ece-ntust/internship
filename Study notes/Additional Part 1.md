# Taqi Additional Part 1
###### tags: `RIC-Team` `TEEP` 
:::success
**Intro:**
Give new member a direction to learn.

**Goal:**
- [ ] To list the steps for new members to learn

:::
[TOC]
# Additional Part 1 (Interface & AI/ML Module)

## Learning E2 Interface related in Near-RT RIC Platform

:::success
- Goal:
    - [ ] Learning E2 Interface
    - [ ] Learning E2 Service Model
- Useful Links:
    - [O-RAN.WG3.E2AP-v02.01](https://www.o-ran.org/specifications)
    - [ORAN-WG3.E2SM-v02.01](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::
### 1. Definition 
![image](https://hackmd.io/_uploads/SyF4uPrta.png =350x300)
E2 interface is one of the O-RAN interface that connects **Near-RT RIC** to the O-RAN Network function such as **O-DU**, **CU-CP**, and **CU-UP**. E2 interface is responsible for **carrying event**s, **control**, and **policy information** to the Open RAN network functions.

E2 nodes interface also enables the collection of metrics from the RAN to the near-RT RIC, either **periodically** or after **pre-defined trigger** events. Both control and data collection procedures can connect to one or more cells, slices, QoS classes, or specific UEs.
### 2. Characteristic
* E2 interface is an open interface between near-RT RIC and  DUs, CUs in 5G
* It runs on top of the SCTP protocol over IP
* E2 interface supports two protocols i.e. E2 Application Protocol (E2AP) and E2 Service Model (E2SM)
* E2AP messages can embed different E2 Service Models, which implement functionalities related to RAN metrics and RAN Control
* E2 Service Model includes  E2 Report, E2 Insert, E2 Control and E2 Policy
* E2 service model can be used for three applications Key Performance Matrix (KPM), Network Interfaces (NIs) and RAN Control (RC)
### 3. E2 Protocol Stack
![image](https://hackmd.io/_uploads/ByND-SUYp.png =150x)
An application protocol called **E2AP** is specified by O-RAN Alliance over **SCTP/IP** as the transport protocol. E2AP  is a basic procedural protocol that coordinates how the near-RT RIC and the E2 nodes communicate with each other, and provides a basic set of services.

E2AP terminologies include:
* E2 node: E2 connecting Near-RT RIC to O-eNB, gNB O-CU-CP, gNB O-CU-UP, gNb O-DU. 
* RAN function: a specific function in an E2 Node; examples include network interfaces (i.e. X2AP, F1, S1AP, Xn, NGc)
* RIC service: a Service provided on an E2 Node to provide access to messages and measurements and / or enable control of the E2 Node from the Near-RT RIC. RIC services include REPORT, INSERT, CONTROL, POLICY, and QUERY.
![image](https://hackmd.io/_uploads/HkpthrLtT.png)
* RAN Function ID: local identifier of a specific RAN Function within an E2 Node that supports one or more RIC Services using a specific E2 Service Model.

By using **publish-subscribe** mechanics, E2 nodes can publish their data and the xApps on the near-RT RIC can subscribe to one or more of these RAN functions through the E2 interface. This makes it possible to clearly separate the capabilities of each node and to define how the xApps interact with the RAN.

### 4. E2 Service Model
![image](https://hackmd.io/_uploads/r1iUj89Kp.png =500x200)
* **E2 Report**:  The reporting procedure involves E2 RIC Indication messages that contain data and telemetry from an E2 node. The E2 report service is activated upon subscription from an xApp to a function offered by the E2 node. During the subscription negotiation, the xApp in the near-RT RIC can specify trigger events or the periodicity with which the E2 node should send report messages. Based on this periodicity, a timer is set in the E2 node and a report is sent whenever the timer expires. The RIC Indication message is of type report.
* **E2 Insert**:  Similarly, the insert procedure involves messages sent from an E2 node to an xApp in the near-RT RIC to notify the xApp about a specific event in the E2 node (e.g., a UE signaling the possibility to perform a handover). It is activated upon subscription from an xApp and involves a RIC Indication message (of type insert). In this case, the trigger is associated to a radio resource management procedure which is suspended when the insert message is sent. A wait timer is also started, and, if the RIC does not reply before the timer expires, the procedure in the E2 node can be resumed or definitely halted.
* **E2 Control**: The control procedure can be autonomously initiated by the RIC, or it can be the consequence of the reception of an insert message at the near-RT RIC. This procedure uses two messages, a RIC Control Request from the RIC to the E2 node, and a RIC Control Acknowledge in the opposite direction. The control procedures can influence parameters exposed by the RAN functions of the E2 node.
* **E2 Policy**: This procedure involves a subscription message which specifies an event trigger and a policy that the E2 node should autonomously follow to perform radio resource management.E2 Report:  The reporting procedure involves E2 RIC Indication messages that contain data and telemetry from an E2 node. The E2 report service is activated upon subscription from an xApp to a function offered by the E2 node. During the subscription negotiation, the xApp in the near-RT RIC can specify trigger events or the periodicity with which the E2 node should send report messages. Based on this periodicity, a timer is set in the E2 node and a report is sent whenever the timer expires. The RIC Indication message is of type report.
## Learning A1 Interface related in Near-RT RIC Platform
:::success
- Goal:
    - [ ] Learning A1 Interface
- Useful Links:
    - [O-RAN.WG3.A1AP-v03.02](https://www.o-ran.org/specifications)
    - [O-RAN.WG3.A1GAP-v03.00](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::
### 1. Definition
![image](https://hackmd.io/_uploads/ByEA2_cta.png =150x)
A1 interface is one of the O-RAN interface that connects **Near-RT RIC** to **Non-RT RIC**. A1 interface's purpose is To enable the non-RT RIC function in the **O&A layer** to guide the near-RT RIC function, and hence the RAN, towards a better **fulfilment** of the RAN intent.

A1 interface capabilities:
* Transfer of policy management information from non-RT RIC to near-RT RIC
* Policy feedback from near-RT RIC to non-RT RIC
* Transfer of enrichment information from non-RT RIC to near-RT RIC

### 2. Policy Management
Policy management function is used by the non-RT RIC to provision and manage A1 policies that are enforced by the near-RT RIC.
#### What it does:
* create, update and delete A1 policies in the near-RT RIC.
*  query the presence, content and run-time status of an A1 policy in the near-RT RIC.

These  function is supported by A1 policy feedback from the near-RT RIC to the non-RT RIC. With some side notes:
* The policy feedback is delivered through notifications containing information on enforcement status and causes.
* NearRT RIC can't change policy's context, so if the policy can't be enforced by near-RT RIC, non-RT RIC is notified through change in enforcement status and may decide to delete it.
* The non-RT RIC can estimate the fulfilment of A1 policies based on O1 observables, it doesn't need A1 policy feedback fulfilment from near-RT RIC.
* Before and after A1 policy creation, non-RT RIC will monitor the network to understand its effect on performance, but this monitoring is not handled by A1 interface.

## Learning O1 Interface related in Near-RT RIC Platform
:::success
- Goal:
    - [ ] Learning O1 Interface
- Useful Links:
    - [O-RAN.WG10.O1-Interface.0-v08.00](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::

## AI/ML Module

### Isoforest & Random Forest

### VAR Module

### LSTM

### RNN

---
