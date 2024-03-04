# OAI DU
---
![image-2](https://hackmd.io/_uploads/r1hjVgXaT.png)


OAI DU Overview
---
OAI DU (OpenAirInterface Distributed Unit) is a software component of the OAI architecture that provides user plane functionality in a 5G network. It is designed to be distributed and can be deployed in various locations to improve network coverage and flexibility. The OAI DU is responsible for handling the Radio Link Control (RLC) and Packet Data Convergence Protocol (PDCP) layers, as well as the physical layer (PHY) functions. It interfaces with the Central Unit (CU) over the F1 interface, which is used for exchanging information between the CU and DU.

The OAI DU is part of the OAI 5G RAN project, which aims to create and distribute a 5G software stack to support RAN 5G functionalities. It supports the O-RAN architecture, which disaggregates radio access network (RAN) elements into different modules to reduce operational aspects and facilitate the deployment of near-real-time control and optimization of radio resource management.

The OAI DU is designed to be compatible with the O-RAN architecture and supports O-RAN's E2AP interface with service models like Key Performance Metrics (E2SM_KPM) and RAN Slicing (E2SM_RSM). It also supports the RIC Agent, an ONF addition to OAI that allows near-real-time control and optimization of O-RAN components and resources through granular data collection and actions over the E2 interface.

The OAI DU is a key component of the OAI architecture that provides user plane functionality and interfaces with the CU over the F1 interface, supporting the O-RAN architecture and its service models.

OAI DU Details
---
![m0lU7JU](https://hackmd.io/_uploads/S1an6emaT.png)

The DU has High-PHY(FAPI), MAC, RLC & RRC (for handing RRC Config messages from CU) protocols along with F1 interface support. Key Performance Metrics (E2SM_KPM) - RAN Slicing (E2SM_RSM) This component is intended for use with OAI based DU hardware or SDRAN-in-a-Box (RiaB).

![FtDVuKk.png](https://hackmd.io/_uploads/BJa1Ae766.jpg)

OAI adopts a split option F1 interface between the CU and DU.
OAI DU relates to F1 interface, which includes F1-C - control plane and F1-U - user plane.

---
Source
---
[OAI DU](https://hackmd.io/@Marsyuma/CU-DU)

[OAI CU & DU](https://hackmd.io/@Marsyuma/CU-DU)

