# Background Knowledge

:::info
Goals:

- [ ] Background knowledge on O-RAN architecture.
- [ ] Learn Four Planes of O-RAN Fronthaul.
      :::

---

- [Background Knowledge](#background-knowledge)
  - [I. O-RAN](#i-o-ran)
  - [II. O-RAN Architecture](#ii-o-ran-architecture)
  - [III. O-RAN Fronthaul](#iii-o-ran-fronthaul)

## I. O-RAN

Open Radio Access Networks (O-RAN) is a new approach to building mobile telecommunications networks. Under this approach, each layer of technology used to build and manage the solutions is open to multiple vendors. This allows smaller suppliers, who may not have the financial resources to build their own solutions across the entire RAN ecosystem, to utilize components from other vendors without compatibility issues. The RAN ecosystem includes elements like radio antennas, baseband units, CU/DU servers, and management and orchestration software.

![O-RAN vs Traditional](images/O-RAN%20vs%20Traditional.png)
ref: [3]

---

## II. O-RAN Architecture

![O-RAN Architecture](images/O-RAN%20Architecture.png)
ref: [4]

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

---

:::info
References:

- [1] [Background of Open-RAN Fronthaul](https://hackmd.io/mVizujCxRgGHZkDOek9z-w)
- [2] [Overview of O-RAN Fronthaul Specification](https://hackmd.io/nJy4F1CRQjyvr0hD6n7vVg)
- [3] [What is Open-RAN?](https://www.vodafone.com/about-vodafone/what-we-do/technology/open-ran)
- [4] [Design of a Network Management System for 5G Open RAN](https://ieeexplore.ieee.org/document/9562627)
  :::
