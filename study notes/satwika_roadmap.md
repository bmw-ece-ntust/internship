# Satwika Learning Roadmap
## Step 1: Understand the background knowledge of 5G
- Goal: 
    - [x] To know the characteristic of 5G
    - [x] To know the overall architecture of 5G
    - [x] To know the difference between 4G and 5G


### I. Intro 5G
The fifth generation, known as 5G, represents the most recent stride in mobile cellular networks, succeeding the fourth-generation (4G) LTE networks. 5G was introduced in 2019.5G aims to revolutionize the way we connect and communicate by delivering significantly enhanced speed and latency compared to previous generations.

### II. Difference Between 5G and 4G

5G outperforms 4G in terms of lower latency, faster download speeds, increased cell density, and advancements in base station architecture, OFDM (Orthogonal frequency-division multiplexing) encoding, and network virtualization.
1. Latency :
    - 5G aims to significantly reduce latency, targeting 1 ms or less.
    - The latency of 4G falls within the range of 60 to 89 ms.
2. Download speed:
    - 5G offers download speeds up to 10 Gbps.
    - 4G offers download speeds up to 1 Gbps.
3. Base station:
    - 5G uses small cells operating in the higher-frequency mmWave bands, but have smaller range than 4G.
    - 4G uses macro cell base stations for wide coverage.
4. OFDM:
    - 5G channels often operate in frequency bands ranging from sub-6 GHz, such as 100 MHz to 800 MHz, which provides benefits like reduced signal interference and access to larger bandwidths
    - 4G channel bandwidth is often set to 20 MHz.
5. Virtualization
    - 5G leverage Network Function Virtualization (NFV) and software-defined networking (SDN), enabling more resource utilization, scalability, and faster deployment of services.
    - 4G are less virtualized, with limited cloud-native capabilities.

### III. 5G Architecture
- Architecture Outline 
    The 5G architecture consists of three key components: User Equipment (UE), Radio Access Network (RAN), and Core Network (CN). The UE is the device connecting to the 5G network. The RAN, comprising base stations and antennas, is responsible for delivering wireless connectivity. Meanwhile, the CN is the central part of the 5G architecture, responsible for managing and directing network traffic.

    In 5G, the radio network has a fundamental component known as the cell tower, which is the Next Generation Node B (gNodeB or gNB). The gNB have two functional units: the Central Unit (CU) and the Distribution Unit (DU). 

    1. The CU handles the non-real-time functions. It responsible for higher-layer functions, such as radio resource management, connection establishment, and mobility management. 
    2. The DU handles with the real-time and essential functions related to radio signal processing. It responsible for lower-layer functions, such as the physical layer processing, modulation, and demodulation.

- NSA (Non Stand Alone) and SA (Stand Alone)
    1. NSA is a 5G network developed from the existing 4G infrastructure. Therefore, 5G and LTE radio access technologies are used together to provide radio access. However, it does not enable the new 5G capabilities for low-latency communications.
    2. Standalone 5G (SA) is a network configuration where radios are directly connected to the core 5G network, with their signaling controlled by the 5G core. Standalone 5G also helps operators to optimize network resources. However, in terms of cost, implementing SA requires the construction of new radios and 5G cores, resulting in a relatively higher implementation cost.


## Step 2: Understand the background knowledge of O-RAN
:::success
- Goal: 
    - [x] To know the characteristic of O-RAN
    - [x] To know the overall architecture of O-RAN
    - [x] To know the difference between O-RAN and 5G
- Key Words:
    - O-RAN
    - Open RAN Architecture
- Useful Links:
    - [O-RAN ALLIANCE](https://www.o-ran.org/)
    - [O-RAN Architecture Description](https://www.o-ran.org/specifications)
:::
### Characteristic of O-RAN 
Open RAN is a non-proprietary form of the RAN system, enabling different vendors cellular network equipment to work together seamlessly. This gives service providers the flexibility and quick decision-making power to choose the right vendor for each part of the network.

- Open-RAN Benefits:

    1. Accelerated Time to Market: Open RAN enables a quicker launch of new services by leveraging a shared hardware infrastructure.
    2. Vendor Independence: With Open RAN, there are no longer restrictions tied to specific telecommunication vendors, providing operators with greater flexibility in choosing solutions.
    3. Enhanced Efficiency through Automation: Intelligent automation is used in Open-RAN. It simplifies network setup and lifecycle management through automated processes. This not only reduces costs but also ensuring error-free operations.

### Architecture of O-RAN
![image](https://hackmd.io/_uploads/B1ycszNtT.png)
reference: https://stl.tech/blog/understanding-o-ran-from-the-basics/ 
1. Service Management and Orchestration Framework (SMO): 
    Manages functions within O-RAN, facilitating their interaction. It connects and oversees RICs, O-Cloud, O-CU, and O-DU.
    
2. RAN Intelligent Controller (RIC):
    Comes in two types – non-real-time and near-real-time. Both control and optimize O-RAN elements. Near-real-time RIC communicates with O-CU and O-DU via the E2 interface, using detailed data for control.
3. O-Cloud:
    A cloud computing platform in the O-RAN architecture, consisting of physical nodes. It hosts virtual network functions (VNFs) utilized by RICs and other infrastructure elements.
4. O-RAN Central Unit (O-CU):
    A logical node hosting essential protocols like radio resource control (RRC), service data adaptation protocol (SDAP), and packet data convergence protocol (PDCP).

5. O-RAN Distributed Unit (O-DU):
    Another logical node hosting protocols such as radio link control (RLC), medium access control (MAC), and physical interface (PHY).

6. O-RAN Radio Unit (O-RU):
    Processes received radio frequencies in the network's physical layer. The processed frequencies are sent to O-DU through a front haul interface.

### Difference between O-RAN and 5G
O-RAN is an approach to designing open and interoperable radio access networks, while 5G is the next-generation technology focused on enhancing network speed and performance.O-RAN can be implemented in 5G networks to bring flexibility.
## Step 3: Understand the background knowledge of Near-RT RIC
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
### RIC (RAN intelligent Controller)
Intelligent RIC equipped with closed-loop control mechanisms, have been implemented to enhance the optimization and orchestration of Radio Access Network (RAN) operations. These controllers, called RAN Intelligent Controllers (RICs), use AI and ML to look at Key Performance Measurements (KPMs) data. They then use this information to decide and control the RAN, making sure it runs as efficiently as possible.

- The RAN Intelligent Controller (RIC) is cloud-native and serves as a central component in an open and virtualized RAN network.
- Virtualization for RAN components and O-RAN elements aims to optimize power consumption.
- Open interfaces in the RAN prevent vendor lock-in. For instance, a near-real-time RIC from one company can seamlessly collaborate with base stations from another vendor, and various components such as CUs, DUs, and RUs from different manufacturers can work together efficiently.

### Characteristic of Near-RT RIC
The Near-Real-Time RIC (near-RT RIC) is based in a regional cloud and operates on a timescale ranging from 10 milliseconds to 1 second. It consists of various applications  supporting custom logic called xApps. These xApps use standard interfaces and service models to control the RAN infrastructure.

### Architecture Near-RT RIC
![image](https://hackmd.io/_uploads/By8OpHvYa.png)
source: https://arxiv.org/pdf/2202.01032.pdf 

1. The internal messaging infrastructure connects xApps, platform services, and interface terminations with each other. It offers APIs for sending and receiving messages and ensures robust routing to prevent internal data loss.
2. Conflict Mitigation addresses possible conflicts emerging among different xApps.
3. The subscription manager helps xApps connect to functions available through the E2 interface. It also manages how each xApp can access E2 messages and can combine several identical subscription requests to the same E2 node into a single request.
4. Security sub-system prevent malicious xApps from leaking sensitive RAN data or from affecting the RAN performance
5. Network Information Base (NIB) Database and Shared Data Layer API:  The RAN NIB (R-NIB) database stores information on E2 nodes. The UE-NIB is used to track and correlate the identity of the same user across different E2 nodes.
6. xApp management  involves overseeing the entire life cycle of specialized applications called xApps within a network. This includes bringing them into the system (onboarding), ensuring they are correctly placed and ready for operation (deployment), and stopping or removing them when needed (termination).
