# O - RAN Architecture (Part 2)

## O - RAN Architecture Elements
In order for User Equipment to connect with the public internet, several connections via several protocols and devices need to be passed as illustrated by this figure down below

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Core%20Network%20-%20UE%202.png) Wireless Network 5G Illustration


The user's device needs to be connected to the 5G Radio Access Network / gNB which is connected to the core network. To understand the relationship and interconnection between user devices and 5G internet, we will explore the architecture of 5G RAN which is the intermediary between the two.


## O - RAN Architecture Interfaces
The diagram outlines the Open-RAN (O-RAN) architecture in High Level Perspective, showing interfaces like A1, O1, Open Fronthaul M-plane, and O2 linking the Service Management and Orchestration (SMO) framework to O-RAN Network Functions and O-Cloud.

O-Cloud includes the O-Cloud Notification interface for relevant O-RAN Network Functions to receive notifications. O-RAN Network Functions can be hosted on O-Cloud or customized hardware, managed via the O1 interface.

The Open Fronthaul M-plane interface supports O-RU management in hybrid mode. NFs on O-Cloud may use APIs from the Accelerator Abstraction Layer (AAL). 

The Near-RT RIC NF provides RAN analytics via the Y1 service interface, accessible after authentication and authorization by subscribing or requesting via the Y1 service interface. Y1 consumers within PLMN trusted domain can access directly, while those outside use secure access via an exposure function.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/High%20Level%20O-RAN%20Architecture.png) High Level Architecture of O-RAN

## Logical Architecture of O-RAN

Within the logical architecture of O-RAN, as shown in Figure down below, the radio side includes Near-RT RIC (RAN intelligence Controller), O-CU-CP (Control Plane), O-CU-UP (User Plane), O-DU, and O-RU O-RAN NFs. The E2 interface connects O-eNB to Near-RT RIC. Although not shown in this figure, the O-eNB does support O-DU and O-RU O-RAN NFs with an Open Fronthaul interface between them. The Near-RT RIC, in the figure below, supports the Y1 service interface towards Y1 consumers. Y1 consumers, unlike the other network elements shown in this figure, does not denote a logical O-RAN function

As stated earlier, the management side includes SMO Framework containing a Non-RT-RIC function. The O-Cloud, on the other hand, is a cloud computing platform comprising a collection of physical infrastructure nodes that meet O-RAN requirements to host the relevant O-RAN NFs (such as Near-RT RIC, O-CU-CP, O-CU-UP, and O-DU etc.), the supporting software components (such as Operating System, Virtual Machine Monitor, Container Runtime, etc.) and the appropriate management and orchestration functions.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Logical%20Architecture%20of%20O-RAN.png) Logical Architecture of O-RAN

## Control Loops of O-RAN

The O-RAN architecture supports at least the following control loops involving different O-RAN functionalities:
* Non-RT (Non-Real Time) control loops
* Near-RT (Near-Real Time) control loops
* RT (Real Time) control loops

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/O-RAN%20Control%20Loop.png) Control loops of O-RAN

The figure above illustrates control loops, categorized by the controlling entity, and their interactions with other logical entities. These loops operate simultaneously at different levels, with potential interaction depending on the use case. Use cases and interactions for Non-RT and Near-RT control loops, including RICs, are defined in the O-RAN Use Cases Analysis Report. This report also outlines interactions for O-CU-CP and O-DU control loops, handling call control, mobility, radio scheduling, HARQ, and beamforming, among others. 

Control loop timing varies by use case: Non-RT loops typically take 1 second or more, Near-RT loops around 10 milliseconds or more, and E2 Nodes loops can operate under 10 milliseconds, such as O-DU radio scheduling.

## Source
* [O-RAN Work Group 1 (Use Cases and Overall Architecture)](https://orandownloadsweb.azurewebsites.net/specifications)
* [O-RAN Architecture Overview](https://docs.o-ran-sc.org/en/latest/architecture/architecture.html)
