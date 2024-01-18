# Taqi Additional Part 1
###### tags: `RIC-Team` `TEEP` 
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
E2 interface is one of the O-RAN interfacce that connects **Near-RT RIC** to the O-RAN Network function such as **O-DU**, **CU-CP**, and **CU-UP**. E2 interface is responsible for **carrying event**s, **control**, and **policy information** to the Open RAN network functions.
### 2. E2 Protocol Stack
![image](https://hackmd.io/_uploads/ByND-SUYp.png =150x)
An application protocol called **E2AP** is specified by O-RAN Alliance over **SCTP/IP** as the transport protocol. On top of E2AP, application-specific controls and events are conveyed through E2 service models (E2SM). The xApps in the Near-RT RIC use the E2SMs.

E2AP terminologies include:
* E2 node: E2 connecting Near-RT RIC to O-eNB, gNB O-CU-CP, gNB O-CU-UP, gNb O-DU. 
* RAN function: a specific function in an E2 Node; examples include network interfaces (i.e. X2AP, F1, S1AP, Xn, NGc)
* RIC service: a Service provided on an E2 Node to provide access to messages and measurements and / or enable control of the E2 Node from the Near-RT RIC. RIC services include REPORT, INSERT, CONTROL, POLICY, and QUERY.
![image](https://hackmd.io/_uploads/HkpthrLtT.png)
* RAN Function ID: local identifier of a specific RAN Function within an E2 Node that supports one or more RIC Services using a specific E2 Service Model.
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
