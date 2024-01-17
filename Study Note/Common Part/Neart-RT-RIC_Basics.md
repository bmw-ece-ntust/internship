# Part 3: Background Knowledge of Near-RT RIC

- Goal : 
    - [x] To know the characteristic of Near-RT RIC
    - [x] To know the overall architecture of Near-RT RIC
    - [x] To know the definition of Near-RT RIC Platform and xApp

- Outcome (Study Note) : 
    - Learn about background of Near-RT RIC and xApp
    - Learn about Near-RT RIC characteristic
    - Learn about Near-RT RIC architecture
    - Learn about O-RAN.WG3.RICARCH-R003-v05.00

---

## I. Definition
> RIC (or RAN Intelligent Controller) is the most important O-RAN Network Function.

**Near-RT RIC** is **a software** based near‐real‐time micro‐service‐based platform for hosting micro-service-based applications - the xApps - that run on the Near-RT RIC platform. **xApps are not part of the RIC platform** and developed in projects that are separate from the Near-RT RIC platform project. The Near-RT RIC platform is **providing xApps the infrastructure** for controlling a distributed collection of RAN base stations (eNB, gNB, CU, DU) in a region via the O-RAN alliance's E2 protocol ("southbound"). As part of this infrastructure it also provides "northbound" interfaces for operators: the A1 and O1 interfaces. 

### Characteristic
Key characteristics of Near-RT RIC include:

1. **Real-time control**: Near-RT RIC can control RAN elements, including CUs and DUs, and perform network optimization actions within a timeframe of 10 milliseconds to one second.
2. **xApp and rApp support**: Near-RT RIC hosts xApps and rApps, which are applications that leverage the functionalities available in the RIC. 
3. **AI/ML integration**: Near-RT RIC supports AI/ML workflows, including model training and updates, and policy-based guidance of applications/features.
4. **Network slicing and optimization**: Near-RT RIC plays a key role in network functions like network slicing, high-bandwidth, low-latency applications, and prioritized communications, helping mobile network operators improve network performance, increase business agility, and reduce costs.
5. **Flexible deployment**: Near-RT RIC can be deployed centrally or on the network edge, providing flexibility in its implementation.
6. **Platform functions**: Near-RT RIC provides a set of platform functions that are commonly used to support the specific functions hosted by xApps.
7. **APIs and interfaces**: Near-RT RIC offers APIs enabling xApps to directly use the information elements of programming languages (e.g., C, C++, Python, Go) and supports xApp subscription management based on operators' requirements.
8. **Collaboration with Non-RT RIC**: Near-RT RIC works in conjunction with Non-RT RIC, which manages events and resources with a response time of one second or more. Together, they provide a comprehensive solution for RAN management and optimization.

## II. Architecture
![image](https://hackmd.io/_uploads/SyZW94-uT.png)

Above is the picture of Near-RT RIC Internal Architecture. Here's a list of each component's function:
**Database and Shared Data Layer**: enables the ==reading and writing== of RAN/UE information. Stores UE-related data in the UE-NIB (UE-Network Information Base) database and radio access network-related information in the R-NIB (Radio-Network Information Base) database.

**Conflict Mitigation**: ==resolves== potentially ==overlapping or conflicting requests== from multiple xApps, ensuring smooth and coordinated operations.

**xApp Subscription Management**: ==merges subscriptions== from different xApps and provides unified data distribution to xApps.

**Security**: ==provides a robust security scheme for the xApps==, safeguarding the integrity and confidentiality of data and operations.

**Messaging Infrastructure**: ==enables message interaction== among Near-RT RIC internal functions, facilitating communication between different components.

**API Enablement**: provides support for registration, discovery and consumption of Near-RT RIC APIs within the Near-RT RIC scope.

**Interface Termination**: terminates interfaces such as E2, A1, Y1, and O1 from respective nodes and layers.
* E2 termination, which terminates the E2 interface from an E2 Node;
* A1 termination, which terminates the A1 interface from the non-RT RIC;
* O1 termination, which terminates the O1 interface from Service Management & Orchestration layer;
* Y1 termination, which terminates the Y1 interface from Y1 Consumers

**xApp Repository**: ==manages== candidate xApps for A1 Termination, facilitating the delivery of A1 policies based on ==policy types and operator policies==. It also maintains and aligns supported policy types with registered xApps and operator policies, while executing access control for requested A1-EI types according to operator policies.

**AI/ML Support**: enables the Near-RT RIC platform with data pipelining, model management, training and inference, which constitute ==complete AI/ML workflow support== for xApps to implement AI/ML algorithms

## III. API in Near-RT RIC
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:75%;" src="https://hackmd.io/_uploads/r1uyGF-_6.png" />
The Near-RT RIC APIs are a collection of well-defined interfaces providing Near-RT RIC platform and xApp services.

:::info
:bulb: **What Near-RT RIC APIs Provides for xApp**

- [A1 related APIs](https://): APIs to access A1 related services;
- [E2 related APIs](https://): APIs to access E2 related services;
- [Management APIs](https://): APIs to access management related services; 
- [SDL APIs](https://): APIs to access Shared Data Layer related services;
- [Enablement APIs](https://): APIs to access enablement services.
:::

### Near-RT RIC API Approach
The Near-RT RIC API Approach defines signaling and data transport protocols for Near-RT RIC APIs. The APIs enable xApps to directly use the information elements of programming languages and support xApp subscription management based on operators' requirements. There is 2 approaches that can be implemented: Network API and SDK approach.

### Network API approach
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/ryAdoVB_T.png" />
**Concept**: Exposing Near-RT RIC functionalities through a well-defined set of network-accessible APIs, enabling remote interaction from xApps and other entities.

**Key Advantages**: 
* Promotes flexibility and remote access
* Facilitates multi-vendor integration
* Supports cloud-native deployments
* Enables easier updates and maintenance

**Potential Consideration**: 
* Overhead of network communication
* Security implications
* Complexity of API management

### SDK approach
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/r1VdjVrda.png" />
**Concept**: Providing a software development kit (SDK) that includes libraries and tools for xApps to directly interact with Near-RT RIC functions within a local environment.

**Key Advantages**: 
* Potential for higher performance and lower latency
* Finer-grained control over RIC resources
* Tighter integration with the platform

**Potential Consideration**:
* Requires xApps to be deployed within the same environment as the Near-RT RIC
* May limit flexibility and vendor portability

### Another Approach
Network API and SDK approach are not mutually exclusive, therefore there are two other options that can be used to Near-RT RIC.

An xApp designed to support the Network API approach may be implemented using **either** an internal SDK library that provides the Network API interface or a **direct implementation** the Network API interface.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/rkGtgrHu6.png" />


A Near-RT RIC Platform may be designed to **support both** the Network API approach and the SDK approach and so xApps implemented using either approach may access platform services.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/ryaqxHr_T.png" />
