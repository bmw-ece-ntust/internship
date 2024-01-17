# Taqi Common Part Basic
###### tags: `RIC-Team` `TEEP` 
:::success
**Intro:**
Give new member a direction to learn.

**Goal:**
- [ ] To list the steps for new members to learn

:::
[TOC]

# Common Part (Basic)
## Pre-Requirement:

- [ ] Register HackMD Account
- [ ] Understand the HACKMD style of RIC Team
    - Title 
    - Introduction
    - Goals
    - References 
    - toc
    - Number Hierarchy (1.1 1.2 1.3 ...)
        - Introduction 
        - System Architecture
        - Comparison Table
        - Flowchart
        - Important Functions
        - Source code Mapping
        - Integration & Testing Result
        - Problem & Solution
        - Summary 

## Part 1: Background knowledge of 5G
:::success
- Goal: 
    - [x] To know the characteristic of 5G
    - [x] To know the overall architecture of 5G
    - [x] To know the difference between 4G and 5G
- Key Words:
    - 5G Characteristic
    - 5G Architecture
    - NGRAN Architecture
    - 4G & 5G Comparasion
    - Deployment modes of SA(Standalone) and Non-SA
    - 5G Technology like Small Cell, Massive MIMO
    - Relationship between the URLLC/mMTC/eMBB Applications and Bandwidth/latency
    - 5G NG-RAN Architecture
    - 5G Core - SBA 
:::

:::info
- Outcome(Study Note):
    - Learn background of 5G
    - Learn architecture of 5G
    - Learn difference between 4G and 5G
:::
### 1. Background
5G is fifth Generation mobile network. Mobile networks have undergone various evolutions such as 3G and 4G to make human life easier. 5G offers **high speed**, **low latency**, **superior realibility** than predecessor network.

### 2. Characteristics
1. Increased speed: 5G offers **higher data transfer rates** than 4G, with peak speed reaching up to 10 Gb/s compare to 100 Mb/s. 
2. Low latency: 5G technology **reduces network latency** with as low as 1 ms that allow real time communication by minimazing delay. 
3. High capacity: 5G networks can support a **massive number of connected devices** simultaneously that can allow massive connection of IoT devices. 

### 3. Architecture
* **Overall architecture**
![image](https://hackmd.io/_uploads/HJ0jaXNOp.png =400x250)
The 5G system architecture consists of familiar elements from previous generations, including **User Equipment** (UE), **Radio Access Network** (NG-RAN), and **Core Network** (5GC). 
The NG-RAN is centered around the gNB (Node B) entity, with the gNB possibly divided into gNB-Central Unit (gNB-CU) and gNB-Distributed Unit(s) (gNB-DU) connected by the F1 interface. DU responsible for **real time function** like what and when devices communicate with each other. Meanwhile CU responsible for **non real time function**.   
The Core Network (5GC) is represented by the AMF/UPF entity, where the **User Plane Function** (UPF) manages user data, and the **Access and Mobility management Function** (AMF) handles signaling. 
* **Non Stand Alone (NSA) and Stand Alone (SA) architecture**
![image](https://hackmd.io/_uploads/rkp1mBcOT.png)

The **NSA** architecture can be seen as a temporary step towards a "full 5G" deployment, where the 5G Access Network is **connected** to the **4G Core Network**. Meanwhile the **SA** architecture can be seen as the "full 5G deployment", **not needing** any part of a **4G network** to operate.
* **5G Core SBA**
![image](https://hackmd.io/_uploads/BJxRY3NV_a.png =500x300)
1. **Network and Resource Management** (NRM): Handles efficient use of network resources.
2. **Signalin**g: Manages control messages between network elements.
3. **Subscribe Data**: Manages user-related information securely.
4. **Application Function and Network Exposure Function** (NEF): Provides specific services and exposes network capabilities.
5. **Location Services**: Provides information about the location of user equipment.
6. **Subscriber Management**: Manages user subscriptions, profiles, and related policies.
7. **Policy**: Enforces network policies and service quality.
8. **Control Plane**: Manages and controls the network, handles signaling.
9. **User Plane**: Manages user data traffic, ensures secure data transfer.
10. **Access Network**:Facilitates connection between user equipment and the core network.

### 4. 4G vs 5G


| Key | 4G | 5G |
| -------- | -------- | -------- |
| Latency | 60 to 100 ms    | Less than 1 ms|
| Speed | Up to 100Mbs    | Up to 10Gbs|
| OFDM Encoding | 200MHz Channel     | up to 800MHz Channel     |
| Cell Density | Up to 400 users per cell    | Up to 40000 users per cell|




## Part 2: Background knowledge of O-RAN
:::success
- Goal: 
    - [x] To know the characteristic of O-RAN
    - [x] To know the overall architecture of O-RAN
    - [ ] To know the difference between O-RAN and 5G
- Key Words:
    - O-RAN
    - Open RAN Architecture
- Useful Links:
    - [O-RAN ALLIANCE](https://www.o-ran.org/)
    - [O-RAN Architecture Description](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::

### **1.** **Radio Access Network (RAN)**
![image](https://hackmd.io/_uploads/HJYjrfOdT.png =600x300)
1. **Definition**: A radio access network (RAN) is the part of a mobile network that **connects** end-user devices, like smartphones, to the cloud or services. This is achieved by **sending information** via **radio waves** from end-user devices to a **RAN’s transceivers**, and finally from the transceivers to the core network which connects to the global internet.
2. **How it works**: In a Radio Access Network (RAN), the **Radio Unit** (RU) **manages digital radio signals**, **communicating** with the **Baseband Unit** (BBU) through **Common Public Radio Interface** (CPRI). The BBU **processes** signals for transmission to the **core network**, with data returning to users in the reverse process. The coverage area of a RAN node depends on antenna capabilities, hardware, and software.

### **2.** **Open Radio Access Network (O-RAN)**
#### **2.1** **Background**
O-RAN is an evolution of the Next Generation RAN (NG-RAN) architecture that **enables** **service providers** the use of non-proprietary subcomponents from a **variety** of vendors. Open RAN enables **programmable**, **intelligen**t, **disaggregated**, **virtualize**d, and **interoperable** functions. Specifically, the proprietary remote radio head (RRH) and baseband units (BBUs) are now disaggregated to radio units (RUs), distributed units (DUs), and centralized units (CUs), many of which can be virtualized or containerized. 
#### **2.2 Characteristics**
Open RAN provides a foundation for services that allow **MNOs** to be more profitable and competitive. But it also broadens the Open RAN ecosystem allowing more innovative software and services and **reducing** the **risk** of relying too much on any one supplier. This innovation is a result of the following:

* Open interfaces: These standard interfaces **connect** the **different network** components (RU, CU, DU) and enable multivendor networks, which in turn invite competition resulting in better products and lower costs.
* Cloudification: Many Open RAN solutions are cloud-native, **allowing** them to be run in the **telecom cloud**. This ensures cloud economics as well as extreme scalability thanks to the compute-on-demand nature of cloud servers and the scalability of microservice cloud-native software.
* Intelligent automation: Open RAN solutions live at the network edge requiring **automated** network deployment and lifecycle management to reduce costs and, in many cases, configuration errors.  

#### **2.3 Architecture**
![image](https://hackmd.io/_uploads/B1ixoPFdp.png =500x)
* **near-RT RIC**: O-RAN near-real-time RAN Intelligent Controller, a logical function that enables near-real-time control and optimization of O-RAN elements and resources via fine-grained data collection and actions over E2 interface.

* **non-RT RIC**: O-RAN non-real-time RAN Intelligent Controller, a logical function that enables non-real-time control and optimization of RAN elements and resources, AI/ML workflow including model training and updates, and policy-based guidance of applications/features in near-RT RIC.

* **O-CU-CP**: O-RAN Central Unit – Control Plane: a logical node hosting the RRC and the control plane part of the PDCP protocol

* **O-CU-UP**: O-RAN Central Unit – User Plane: a logical node hosting the user plane part of the PDCP protocol and the SDAP protocol

* **O-DU**: O-RAN Distributed Unit: a logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

* **O-RU**: O-RAN Radio Unit: a logical node hosting Low-PHY layer and RF processing based on a lower layer functional split. This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction).

* **O1**: Interface between management entities in Service Management and Orchestration Framework and O-RAN managed elements, for operation and management, by which FCAPS management, Software management, File management shall be achieved.

* **xAPP**: Independent software plug-in to the Near-RT RIC platform to provide functional extensibility to the RAN by third parties.

### **3. O-RAN v 5G**
5G is a next-generation wireless technology focused on **improving** overall **network** performance, while Open RAN is an **architectural** approach aimed at making radio access networks more **open**, **flexible**, and **interoperable** by decoupling hardware and software components. It's worth noting that these concepts can complement each other, as **Open RA**N can be **implemented** within **5G** networks to provide more flexibility and vendor diversity.

## Part 3: Background knowledge of Near-RT RIC
:::success
- Goal: 
    - [x] To know the characteristic of Near-RT RIC
    - [x] To know the overall architecture of Near-RT RIC
    - [x] To know the definition of Near-RT RIC Platform and xApp
- Key Words:
    - Near-RT RIC
    - O-RAN.WG3.RICARCH-R003-v05.00
- Useful Links:
    - [O-RAN.WG3.RICARCH-R003-v05.00](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::
### 1. RAN Intelligence Controller (RIC)
A RAN Intelligent Controller (RIC) is a **software-defined** component of the Open Radio Access Network (Open RAN) architecture that’s responsible for **controlling** and **optimizing** RAN functions. The RIC enables the optimization of RAN resources through **near real-time** analytic processing and provides adaption recommendations. The RAN intelligent Controller (RIC) is cloud native, and a central component of an open and virtualized RAN network.

### 2. Near-RT RIC
#### **2.1 Definitions**
Near-RT RIC is a near‐real‐time, **micro‐service‐based software** platform for hosting micro-service-based applications called **xApps**. They run on the near-RT RIC platform. The near-RT RIC software platform provides xApps cloud-based infrastructure for **controllin**g a **distributed** collection of RAN infrastructure (eNB, gNB, CU, DU) in an area via the O-RAN Alliance’s **E2** protocol (“southbound”).
#### **2.2 Characteristic**
1. Low Latency: Near-RT RIC is designed to operate with low latency, as it needs to make quick decisions and adjustments to ensure efficient and reliable communication between devices and the network. 

2. Real-Time Monitoring: Near-RT RIC continuously monitors the performance of the radio interface and gathers data on various network parameters, such as signal strength, interference, and traffic load. This data is used to make informed decisions and optimizations in real time.

3. AI and Machine Learning: To make rapid and intelligent decisions, Near-RT RIC often incorporates artificial intelligence (AI) and machine learning (ML) algorithms. These algorithms can predict network conditions and optimize resource allocation, helping to enhance the quality of service and reduce congestion.

4. Resource Management: Near-RT RIC is responsible for managing radio resources, such as spectrum allocation and power control. It dynamically allocates resources to different user devices based on their requirements and network conditions.
 
5. Network Slicing: Near-RT RIC can support network slicing, allowing the network to be divided into multiple virtual networks with specific characteristics and performance guarantees. This enables customization of services for different use cases, such as enhanced mobile broadband, massive IoT, or critical communication.

#### **2.3 Architecture**
![image](https://hackmd.io/_uploads/r1HG6PbFp.png =400x300)
* Functions hosted by **xApps** allow services (i.e. RRM control functionalities) to be executed at the near-RT RIC and the outcomes sent to the E2 Nodes (i.e. enforced in the E2 Nodes) via E2 interface;
* **Database** together with shared data layer allows reading and writing of RAN/UE information;
* **Conflict mitigation** function resolves potentially overlapping or conflicting requests from multiple xApps;
* **Messaging infrastructure** function enables message interaction amongst near-RT RIC internal functions;
* **xApp subscription management** function merges subscriptions from different xApps and provides unified data distribution to xApps;
* **Security** function provides security scheme for the xApps;
* **Management services** function element is used for: fault, configuration management, and performance management; Life-cycle management of xApps; Logging, tracing, and metrics collection and transfer to an external system for evaluation.
* **Interface Termination**:
**A1** : is the interface between non-RT RIC and modular CU which contains non-RT RIC.
**E2** : a standard interface between the near-RT RIC and CU/DU in the context of an O-RAN architecture.
**O1** : Interface between orchestration & management entities (Orchestration/NMS) and O-RAN managed elements, for operation and management, by which FCAPS management, Software management, File management and other similar functions shall be achieved.
#### **2.4 Near-RT RIC Platform and xApp**
Near-RT RIC consists of **platform** and 2 or more **xApp**, platform provide **set of functions** that send to xApp and xApp will use that function and data to accomplish their **spesific task**.
## Part 4: Understand the Near-RT RIC of OSC
:::success
- Goal: 
    - [ ] [Install Near-RT RIC Platform](https://hackmd.io/@2xIzdkQiS9K3Pfrv6tVEtA/G-release_Near-RT-RIC_Install)
    - [ ] [Install xApp using DMS tool](https://hackmd.io/@Min-xiang/HJZF3-xgt#43-Commands-about-helm-charts)
    - [x] Mapping Near-RT RIC between specification and OSC
    - [x] Give Each Component a Introduction
    - [x] Be familiar with the platform operation
- Useful Links:
    - [Gerrit](https://gerrit.o-ran-sc.org/r/admin/repos)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::
### **1. OSC Near-RT RIC Platform**
![image](https://hackmd.io/_uploads/B15GqAGF6.png =400x300)
Near-RT RIC is a **software based** near‐real‐time micro‐service‐based platform for hosting micro-service-based applications - the xApps - that run on the near-RT RIC platform. 
### **2. Components**
* **RIC Message Router (RMR)**: peer to peer library distributed in each platform component and xApp. 
* **Routing Manager**: Routing center, each component in platform can create/update through this.
* **Redis Database**: SDL API enables platform components or xApps to access the database
* **E2 Termination**: Accepts to establish SCTP connection with E2 nodes.
* **E2 Manager**: Used to identify the E2 Node, which allows to establish E2 connection between Near-RT RIC platform and E2 node. 
* **Subscription Manager**: Used to manage subscription between xApp and E2 node. 
* **xApp Manager**: Used to let platform component know xApp.
* **A1 Mediator**: Mediator for A1 connection which supports A1AP and A1GAP. 
### **3. Commands**
![image](https://hackmd.io/_uploads/S1xWbkmFT.png)
