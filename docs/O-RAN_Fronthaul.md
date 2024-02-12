# Background Knowledge

Goals:

- [ ] Background knowledge on O-RAN architecture.
- [ ] Learn Four Planes of O-RAN Fronthaul.

---

- [Background Knowledge](#background-knowledge)
  - [I. O-RAN](#i-o-ran)
  - [II. O-RAN Architecture](#ii-o-ran-architecture)
  - [III. O-RAN Fronthaul](#iii-o-ran-fronthaul)
  - [IV. Split Option 7-2x](#iv-split-option-7-2x)
  - [V. O-RAN Fronthaul Security Threats](#v-o-ran-fronthaul-security-threats)
  - [VI. O-RAN Interfaces](#vi-o-ran-interfaces)
  - [VII. O-FH Protocol Stacks](#vii-o-fh-protocol-stacks)

## I. O-RAN

Open Radio Access Networks (O-RAN) is a new approach to building mobile telecommunications networks. Under this approach, each layer of technology used to build and manage the solutions is open to multiple vendors. This allows smaller suppliers, who may not have the financial resources to build their own solutions across the entire RAN ecosystem, to utilize components from other vendors without compatibility issues. The RAN ecosystem includes elements like radio antennas, baseband units, CU/DU servers, and management and orchestration software.

![O-RAN vs Traditional](../assets/O-RAN%20vs%20Traditional.png)
ref: [What is Open-RAN?](https://www.vodafone.com/about-vodafone/what-we-do/technology/open-ran)

---

## II. O-RAN Architecture

![O-RAN Architecture](../assets/O-RAN%20Architecture.png)
ref: [Design of a Network Management System for 5G Open RAN](https://ieeexplore.ieee.org/document/9562627)

- **Near-RT-RIC:** The brain of the near-real-time control plane. Resides at the network edge near O-DUs for fast response (10ms - 1s). Optimizes RAN elements dynamically based on network conditions and user demands. Focuses on radio resource management, beamforming, and power control.
- **O-RU:** The O-RAN Radio Unit serves as the physical interface between mobile devices and the network. It transmits and receives radio signals to and from user devices such as smartphones and tablets. The unit then converts radio signals into digital data and vice versa for communication with the rest of the Open RAN system. O-RUs can be deployed across different frequency bands to cater to specific use cases and coverage needs.
- **O-DU:** The O-RAN Distributed Unit is a logical node in the O-RAN architecture that hosts a set of protocols, which include the radio link control (RLC) protocol, medium access control (MAC) protocol, and the physical interface (PHY). It’s responsible for real-time L1 and L2 scheduling functions and modulation.
- **O-CU:** The O-CU (O-RAN Central Unit) is a logical node in the O-RAN architecture that hosts the RRC, SDAP, and PDCP protocols. It’s responsible for non-real time, higher L2 and L3.
- **O-RAN Fronthaul:** The O-RAN Fronthaul defines the interface and protocols that connect O-DU and O-RU components of an O-RAN network.

## III. O-RAN Fronthaul

O-RAN fronthaul enables these separated components to communicate efficiently and securely:

- **Control Plane (C-plane):** Carries configuration and management messages for the radio link.
- **User Plane (U-plane):** Transmits actual user data (like voice and video) between the DU and RU.
- **Synchronization Plane (S-plane):** Ensures precise timing alignment between the DU and RU, crucial for accurate signal transmission.
- **Management Plane (M-plane):** Handles the management of the O-RU from the O-DU, including fault management, performance management, and security management.

## IV. Split Option 7-2x

- Split Option 7-2x is a specification for functional splitting between O-RAN Distributed Unit (O-DU) and O-RAN Radio Unit (O-RU) adopted by O-RAN fronthaul specifications.

- Functional spliting is a technique of dividing the complex tasks involved in signal processing and network operations across different hardware units or software modules.

- Split Option 7-2x is a new functional splitting approach to solve fronthaul bandwidth issues.

![Split Option 7-2x](../assets/Split%20Option%207-2x.png)

ref: [Overview of O-RAN Fronthaul Specification](https://hackmd.io/nJy4F1CRQjyvr0hD6n7vVg)

- The PHY layer is split into two parts:

  - **High-PHY:** Located in the O-DU (O-Distributed Unit), it handles complex operations like precoding and channel estimation.
  - **Low-PHY:** Located in the O-RU (O-Radio Unit), it performs basic tasks like RF signal processing and analog-to-digital conversion.

- Layer 1 functions is split between O-DU and O-RU to reduce fronthaul bandwidth:
  - **DL:** Resource element mapping in O-DU, with options for O-RU complexity:
  - **Category A:** Digital beamforming and later functions (simpler, initial deployment choice).
  - **Category B:** Precoding in addition to Category A functionalities (more complex, future advancements).
  - **UL:** Resource element mapping and higher functions in O-DU, digital beamforming and lower functions in O-RU.

## V. O-RAN Fronthaul Security Threats

![O-FH Threat](../assets/O-FH%20Threat.png)

ref: [Transport Security Considerations for the Open-RAN Fronthaul](https://ieeexplore.ieee.org/document/9604996)

The potential threats encountered by each of the four planes in the O-RAN Fronthaul architecture:

- **C-Plane**
  - Attackers can manipulate the communication between O-DU and O-RU by injecting fake messages or modifying real ones. To prevent this, O-DU and O-RU communication needs to be secure, ensuring authenticity, integrity, confidentiality, and replay protection.
- **U-Plane**
  - Attackers can disrupt or eavesdrop on user data in the U-Plane through various methods, similar to the C-Plane. To counter these threats, securing the U-Plane requires the same security features as the C-Plane: authenticity, integrity, confidentiality, and replay protection. This ensures legitimate data exchange and protects user privacy.
- **S-Plane**
  - The fronthaul link in O-RAN networks requires strict time synchronization between components. Attacks on this link can disrupt timing by impersonating legitimate clocks, injecting fake packets, delaying messages, or dropping packets.
- **M-Plane**
  - The M-Plane itself uses TLS or SSH for security, it relies on the other planes like Layer-2 to be secure as well. If those other planes are compromised, attackers can corrupt M-Plane messages or inject false ones, harming network performance. Therefore, all four pillars of security are crucial for a secure O-RAN, as threats on any level can significantly impact performance and user experience.


## VI. O-RAN Interfaces

- **O1 Interface:** The O1 interface is a vital component in Open RAN (O-RAN) networks, defined by the O-RAN Alliance's WG10. It serves as a communication channel between the Service Management and Orchestration (SMO) framework and managed elements (MEs) for various management operations. These include configuring, monitoring, troubleshooting, and updating O-RAN network components.
- **O2 Interface:** The O2 interface is a communication channel between the Service Management and Orchestration (SMO) framework and the O-Cloud. It allows the SMO to manage the deployment and lifecycle of O-RAN Virtual Network Functions (VNFs) running within the O-Cloud infrastructure.
- **A1 Interface:** The A1 interface connects the Non-Real-Time RAN Intelligent Controller (Non-RT RIC) with the Near-RT RIC. It allows the Non-RT RIC to provide policy management, enrichment information, and ML model management services to the Near-RT RIC.
- **E2 Interface:** The E2 interface connects the Near-RT RIC with E2 Nodes, which represent various network elements at the edge of the network. This interface enables two-way communication:
  - **Near-RT RIC Services:** The Near-RT RIC can send REPORT, INSERT, CONTROL, and POLICY requests to E2 Nodes to influence real-time network behavior.
  - **Near-RT RIC Support and Updates:** E2 Nodes can report general error situations, manage E2 interface setup and reset, and exchange capabilities regarding exposed services.

## VII. O-FH Protocol Stacks

![O-FH Protocols](../assets/O-FH%20Protocol%20Stacks.png)

ref: [Overview of O-RAN Fronthaul Specifications](https://www.docomo.ne.jp/english/binary/pdf/corporate/technology/rd/technical_journal/bn/vol21_1/vol21_1_007en.pdf)

- C/U-Plane:
  - Transmits signals using eCPRI or RoE.
  - Two protocol stack options: Direct transmission over Ethernet Transmission over UDP/IP
  - **U-Plane:**
  ![U-Plane Message](../assets/U-Plane%20Message.png)

    - The eCPRI payload of the U-Plane message can carry compressed IQ samples of the OFDM signal in the frequency domain, along with accompanying information.
    - This information includes:
      - Time resource information: radio frame, subframe, slot, and OFDM symbol identification
      - Frequency resource information: PRB start position and number of PRBs
      - IQ compression information: compression scheme used and number of bits in the compressed IQ sample
    - Details of this eCPRI payload are specific to O-RAN fronthaul specifications and not part of eCPRI itself.
  - **C-Plane:**
  - extended Antenna-Carrier (eAxC)
  
    ![eAxC](../assets/extended%20Antenna-Carrier%20(eAxC).png)

    ![C-Plane Message](../assets/C-Plane%20Message.png)

    - The eCPRI header is the same as in the U-Plane message.accompanying information.
    - Source and destination identifiers are called ecpriRtcid (compared to ecpriPcid in U-Plane).
    - O-RAN specifications use extended Antenna-Carrier (eAxC) as identifiers for both C-Plane and U-Plane messages.
    - C-Plane message payload carries information about beamforming (BF) weights to be applied when transmitting and receiving IQ samples in the U-Plane message.
    - Includes time resource information (same as U-Plane message) and frequency resource information (startPRBc, numPRBc).
    - O-RU uses this information to generate beams for radio interface transmission and reception.
    - O-RAN specifications mandate support for an interface using a beam identifier (beamId).
    - This option can be applied to digital BF, analog BF, or hybrid BF.
  - **Delay Management**
  
    ![Delay Management](../assets/Delay%20Management.png)

    - Aligning C/U-Plane message transmission on the fronthaul with transmit/receive timing on the radio interface, as well as HARQ retransmission timing.
    - Guaranteeing that the O-RU has adequate time to process received IQ sample sequences (including IFFT, analog conversion, and beamforming) before transmitting signals on the radio interface within designated time slots.
- S-Plane:
  - Transmits signals used in PTP and SyncE.
  - Protocol stack: Transmission over Ethernet
  - In C-RAN systems, precise synchronization between O-DU and O-RU is crucial for features like TDD, Carrier Aggregation, MIMO etc. 
  - The O-RAN fronthaul specs use protocols like PTP and SyncE to ensure this high-accuracy sync by synchronizing O-RUs with the central O-DU's high-performance clock.
- M-Plane:
  - Transmits signals using NETCONF.
  - Protocol stack: Transmission over Ethernet/IP/TCP/SSH
  - **M-Plane Architecture**
  ![M-Plane Functions](../assets/M-Plane%20Functions.png)

    - The M-Plane in C-RAN deals with managing Remote Radio Units (O-RUs) using the NETCONF protocol. There are two key architectures:

      **1. Hierarchical:**
        - O-DUs act as intermediary managers for O-RUs, reducing workload on the Network Management System (NMS).
      - Useful if the NMS doesn't support NETCONF, allowing network construction without modifying the existing system.
      - Each O-RU is managed by one or more O-DUs.
      
      **2. Hybrid:**
      - NMS can directly manage O-RUs besides O-DUs, enabling unified management of all network devices.
      - Useful for NMS that already support NETCONF and want comprehensive control over all equipment.
      - Each O-RU can be managed by one or more NMSs and O-DUs.

---

References:

- [1] [Background of Open-RAN Fronthaul](https://hackmd.io/mVizujCxRgGHZkDOek9z-w)
- [2] [Overview of O-RAN Fronthaul Specification Notes](https://hackmd.io/nJy4F1CRQjyvr0hD6n7vVg)
- [3] [What is Open-RAN?](https://www.vodafone.com/about-vodafone/what-we-do/technology/open-ran)
- [4] [Design of a Network Management System for 5G Open RAN](https://ieeexplore.ieee.org/document/9562627)
- [5] [Transport Security Considerations for the Open-RAN Fronthaul](https://ieeexplore.ieee.org/document/9604996)
- [6] [O-RAN Alliance Specifications](https://orandownloadsweb.azurewebsites.net/download?id=499)
- [7] [Overview of O-RAN Fronthaul Specifications](https://www.docomo.ne.jp/english/binary/pdf/corporate/technology/rd/technical_journal/bn/vol21_1/vol21_1_007en.pdf)
