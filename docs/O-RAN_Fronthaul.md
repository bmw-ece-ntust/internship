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

## I. O-RAN

Open Radio Access Networks (O-RAN) is a new approach to building mobile telecommunications networks. Under this approach, each layer of technology used to build and manage the solutions is open to multiple vendors. This allows smaller suppliers, who may not have the financial resources to build their own solutions across the entire RAN ecosystem, to utilize components from other vendors without compatibility issues. The RAN ecosystem includes elements like radio antennas, baseband units, CU/DU servers, and management and orchestration software.

![O-RAN vs Traditional](../assets/O-RAN%20vs%20Traditional.png)
ref: [What is Open-RAN?](https://www.vodafone.com/about-vodafone/what-we-do/technology/open-ran)

---

## II. O-RAN Architecture

![O-RAN Architecture](../assets/O-RAN%20Architecture.png)
ref: [Design of a Network Management System for 5G Open RAN](https://ieeexplore.ieee.org/document/9562627)

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

---

References:

- [1] [Background of Open-RAN Fronthaul](https://hackmd.io/mVizujCxRgGHZkDOek9z-w)
- [2] [Overview of O-RAN Fronthaul Specification](https://hackmd.io/nJy4F1CRQjyvr0hD6n7vVg)
- [3] [What is Open-RAN?](https://www.vodafone.com/about-vodafone/what-we-do/technology/open-ran)
- [4] [Design of a Network Management System for 5G Open RAN](https://ieeexplore.ieee.org/document/9562627)
