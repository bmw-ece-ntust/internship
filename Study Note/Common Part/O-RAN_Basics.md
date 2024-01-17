# Part 2: Background Knowledge of O-RAN

- Goal : 
    - [x] To know the characteristic of O-RAN
    - [x] To know the overall architecture of O-RAN
    - [x] To know the difference between O-RAN and 5G

- Outcome (Study Note) : 
    - Learn about background of RAN and O-RAN
    - Learn about O-RAN characteristic
    - Learn about how O-RAN works + its architecture
    - Learn about the difference between 5G and O-RAN

---

## RAN
### I. Background
A radio access network (RAN) is a major component of a wireless telecommunications system that connects individual devices to other parts of a network through **a radio link**. The RAN links user equipment, such as a cellphone, computer or any remotely controlled machine, over a fiber or wireless Backhaul connection. That link goes to the core network, which manages subscriber information, location and more.

The RAN, which is sometimes also called the access network, is **the radio element** of the cellular network. A cellular network is made up of land areas called cells. A cell is served by at least one radio transceiver, although the standard is typically three for cell sites.

### II. Architecture of RAN
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:75%;" src="https://hackmd.io/_uploads/HJ00zDRDp.png" />

RAN is essentially a network of base stations (think cell towers) that connect our device to the core network. These base stations house various components, each playing a crucial role:

**Antennas**: These are the ears and mouths of the RAN, transmitting and receiving radio signals.
**Remote Radio Heads (RRHs)**: Located at the cell tower, RRHs handle the signal processing and amplification.
**Baseband Units (BBUs)**: The brains of the operation, BBUs process the data and manage communication with the core network. They can be centralized or distributed, depending on the RAN type.

### III. Types of RAN
1. **Tradtional RAN**
**Concept**: ==Closed==, vendor-specific ecosystem with tightly coupled BBUs and RRHs from the same manufacturer.
**Benefits**: Mature and reliable technology with proven track record.
**Challenges**: Limited flexibility, higher costs due to vendor lock-in, and slower innovation.

2. **C-RAN (Cloud RAN)**
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:75%;" src="https://hackmd.io/_uploads/SyWQNw0D6.png" />
**Concept**: ==Centralized RAN architecture==, where baseband processing units (BBUs) are located far from remote radio heads (RRHs) at cell towers.
**Benefits**: ==Simplified network management==, reduced energy consumption, and potential for improved network performance.
**Challenges**: Requires high-bandwidth and low-latency fiber or microwave backhaul connections between BBUs and RRHs.

3. **O-RAN (Open RAN)**
![image](https://hackmd.io/_uploads/HkVR7P0w6.png)
**Concept**: An open ecosystem for cellular networks, using white box hardware and software from multiple vendors. ==Think Legos for base stations!==
**Benefits**: Increased flexibility, lower costs, and faster innovation due to vendor competition.
**Challenges**: Ensuring interoperability between components from different vendors and creating mature open-source software solutions.


| Feature | Traditional RAN | Cloud RAN | Open RAN |
| -------- | -------- | -------- | --- |
| Hardware | Vendor-specific | Specialized RRHs, COTS BBUs | White box, multi-vendor |
| Software | Vendor-specific | Proprietary | Open-source or commercial |
| Flexibility | Low | Moderate | High |
| Cost | High | Moderate | Potentially Lower | 
| Innovation | Slower | Moderate | Faster | 

---

## O-RAN
### I. Background
O-RAN, or Open Radio Access Network, is a network architecture that aims to provide a **more open** and **flexible** approach to building radio access networks for 4G and 5G cellular networks. O-RAN is designed to enable multi-vendor interoperability and reduce the cost of building and operating cellular networks.

### II. Characteristic
**Open Interfaces**: Standardized interfaces between RAN components from different vendors, fostering competition and innovation.
**White Box Hardware**: Replacing traditional vendor-specific hardware with commercially available, off-the-shelf (COTS) equipment, reducing costs and increasing flexibility.
**Cloud-Native Software**: Utilizing software designed for cloud environments, enabling flexible scalability and easier network management.
**Centralized Intelligence**: Shifting processing power from base stations to centralized units, simplifying network management and optimizing performance.
**Programmable RAN**: Allowing operators to tailor network functionality and adapt to specific needs through software changes.

### III. Architecture
![image](https://hackmd.io/_uploads/rk4TicRvT.png)
**Service Management and Orchestration (SMO)**: The brain of the operation, controlling and managing the RAN and its components.

**Radio Unit (O-RU)**: Located at the cell tower, it handles radio signal transmission and reception. A logical node hosting Low-PHY layer and RF processing based on a lower layer functional split.  This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction).

**Distributed Unit (O-DU)**: Performs baseband processing closer to the cell tower, reducing backhaul traffic. A logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

**O-CU-CP** (O-RAN Central Unit – Control Plane): a logical node hosting the RRC and the ==control plane== part of the PDCP protocol.

**O-CU-UP** (O-RAN Central Unit – User Plane): a logical node hosting the ==user plane== part of the PDCP protocol and the SDAP protocol.

**Non-Real-Time RIC** (RAN Intelligent Controller): Provides analytics and optimization for long-term network performance. A functionality within SMO that drives the content carried across the A1 interface.

**Near-Real-Time RIC**: An O-RAN Network Function (NF) that enables near-real-time control and optimization of RAN elements and resources via fine-grained data collection and actions over E2 interface. It may include AI/ML (Artificial Intelligence / Machine Learning) workflow including model training, inference and updates. 

**O-Cloud**: O-Cloud is a cloud computing platform comprising a collection of physical infrastructure nodes that meet O-RAN requirements to host the relevant O-RAN functions (such as Near-RT RIC, O-CU-CP, O-CU-UP, and O-DU), the supporting software components (such as Operating System, Virtual Machine Monitor, Container Runtime, etc.) and the appropriate management and orchestration functions. 

### IV. Difference
O-RAN is different from 5G in that ==5G is a wireless communication standard==, while ==O-RAN is an architecture== that can be used with 5G and other wireless communication standards. 5G defines the air interface and core network, while O-RAN defines the radio access network. **They are complementary players**, not competitors. O-RAN aims to make 5G networks more flexible, cost-effective, and innovative, enabling operators to better cater to diverse user needs and applications.
