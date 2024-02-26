# O-RAN
---
## Introduction to O-RAN (OpenRAN)
Open RAN is an ongoing shift in mobile network architectures that enables service providers the use of non-proprietary
subcomponents from a variety of vendors. An Open RAN, or open radio access network, is made possible by a set of industry-wide 
standards that telecom suppliers can follow when producing related equipment. Open RAN enables programmable, intelligent, disaggregated, virtualized,
and interoperable functions. Specifically, the proprietary remote radio head (RRH) and baseband units (BBUs) are now disaggregated to radio units (RUs),
distributed units (DUs), and centralized units (CUs), many of which can be virtualized or containerized. The interfaces between these new components are 
open and interoperable.

## Arhcitecture of O-RAN
the O-RAN generally follows O-RAN Alliance defined architecture, which is the following

![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/d30d6c74-ae3c-4958-a9d4-64332d5ed4d4)

In the O-RAN architecture, the radio side includes Near-RT RIC, O-CU-CP, O-CU-UP, O-DU, and O-RU.
The management side includes Service Management and Orchestration Framework that contains a Non-RT-RIC function.
each of the component on the architecture block is defined as following

- near-RT RIC: O-RAN near-real-time RAN Intelligent Controller: a logical function that enables near-real-time control and optimization of O-RAN elements and resources via fine-grained data collection and actions over E2 interface.

- non-RT RIC: O-RAN non-real-time RAN Intelligent Controller: a logical function that enables non-real-time control and optimization of RAN elements and resources, AI/ML workflow including model training and updates, and policy-based guidance of applications/features in near-RT RIC.

- NMS: A Network Management System

- O-CU: O-RAN Central Unit: a logical node hosting RRC, SDAP and PDCP protocols

- O-CU-CP: O-RAN Central Unit – Control Plane: a logical node hosting the RRC and the control plane part of the PDCP protocol

- O-CU-UP: O-RAN Central Unit – User Plane: a logical node hosting the user plane part of the PDCP protocol and the SDAP protocol

- O-DU: O-RAN Distributed Unit: a logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

- O-RU: O-RAN Radio Unit: a logical node hosting Low-PHY layer and RF processing based on a lower layer functional split. This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction).

- O1: Interface between management entities in Service Management and Orchestration Framework and O-RAN managed elements, for operation and management, by which FCAPS management, Software management, File management shall be achieved.

- O1*: Interface between Service Management and Orchestration Framework and Infrastructure Management Framework supporting O-RAN virtual network functions.

- xAPP: Independent software plug-in to the Near-RT RIC platform to provide functional extensibility to the RAN by third parties.


## Reference
- https://www.juniper.net/us/en/research-topics/what-is-open-ran.html
- https://docs.o-ran-sc.org/en/e-release/architecture/architecture.html
