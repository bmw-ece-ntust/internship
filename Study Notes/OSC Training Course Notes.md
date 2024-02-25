Video can be accessed through this link : https://www.youtube.com/watch?v=Bd003K0vqpg

## Overall Mobile Networks
<img width="731" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/18a81502-c687-4e85-a751-7ff19bdf8751">

The image above is the infrastructure of the network which plays a role of the access network, which provides user access, and the core network, which connects different parts of the network and acts as a gateway to other networks. Providers are decentralizing VBUs inside Base Band Unit (BBU) pools for cost reduction and Resource sharing. Virtualizing BBUs into virtual machines is to prepare future connections, disaggregating control and user plans for flexibility, and optimizing the system with open Application Programming Interfaces (APIs)  to attract more vendors, lower company’s spending, and improve competition and information. The O-RAN Alliance, known as the open RUN organization, is primarily composed of mobile network operators, vendors, and academia.


## Open RAN Architecture
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/1ebcb0f3-05e3-4a0a-9a00-726f8babe6ad)

For this O-RAN prototype, it focuses on the non-real-time RIC, new real-time RIC, central unit (CU), and distributed unit (D1Uu). The non-real-time RIC is responsible for energy management and machine learning training. The real-time RIC manages ideologies and case management with more controls. The CU and D1Uu are connected through different interfaces. Furthermore, the O-DU architecture is responsible for distributed unit processing. The architecture consists of a high-level functional block with the rse, mac, and hifi layers. The O-DU system's functional blocks include the audio OM agent, F1 AP, and the user plane. The F1 AP connects to the CU and controls the user plan for data transfer. The presentation also touches on the entities and thread architecture for the O-DU high layer.


<img width="607" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/42bbb6e0-78f3-479a-8ae6-6461f00ae7ff">

The O-DU processing is divided into several threads for overall audio, new app, configuration handler, and handlers like SCTP and EGTP. The Threads divide the processing because they need more processing capacity for threat handling. Additionally, there is the fifth thread for stick handling and lower mac handler. The layer one processing blocks include channel processing, uplink task scheduling, FPGA procedure for forward error corrections (FEC), and front hall interface processing. The interface part is then explained, which includes external and internal interfaces. The external interface connects to the SMo and new real-time lic, and there are F1 interfaces and a front interface. For internal parts, there are the RC interface and layer 1 (L1) layer 2 interface. The f1 handler is used for messages to and from the CUC, with three types of messages: mac cell specific APIs, mcu specific APIs, and no specific APIs. The F1 interface handles uplink CCH, downloading part, and broadcast request, and it works similarly to the previous one. The air interface setup is explained for deployments.
