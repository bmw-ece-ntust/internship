# OAI CU
---
![image-2](https://hackmd.io/_uploads/BksTLv7Ta.png)


OAI CU Overview
---
OAI CU (Centralized Unit) specifically refers to the Centralized Unit in the Open Air Interface (OAI) architecture, which is a part of the 5G Radio Access Network (RAN). The OAI architecture is a software-defined RAN (SD-RAN) that supports various functional splits, including the CU and DU (Distributed Unit) split.

In the OAI CU, the control plane functions are centralized, while the data plane functions are distributed among the DUs. This split allows for efficient optimization and resource handling, as the CU can manage the overall network performance and the DUs can handle the radio interface processing.

The transported F1-U packet format is used to transport the data between the CU and the DUs. This format ensures that the data is transmitted efficiently and securely across the network.

The OAI CU and DU split is designed to provide network access to end-users via heterogeneous (3GPP and non-3GPP) DUs, converging the access and core networks. This allows for the integration of various network technologies and the ability to provide services to a wide range of devices.

The OAI CU and DU split is a key component of the OAI architecture, which is designed to be flexible and scalable, allowing for the deployment of various network configurations and use cases.

OAI CU Details
---
A control unit, or CU, is circuitry within a computer’s processor that directs operations. It instructs the memory, logic unit, and both output and input devices of the computer on how to respond to the program’s instructions. CU provides support for the higher layers of the protocol stack such as SDAP, PDCP and RRC. Here are some key details about the OAI CU:

- O-RAN Compliance: The OAI CU and DU are O-RAN compliant disaggregated baseband units based on the OpenAirInterface.
- Protocol Support: The OAI CU contains both CU-C and CU-U functionality and supports PDCP, GTPU, RRC, and S1AP protocols, along with S1, F1, and E2 interfaces.
- E2AP Interface: The OAI CU and DU implement O-RAN's E2AP interface with support for Key Performance Metrics (E2SM_KPM) and RAN Slicing (E2SM_RSM) service models.
- RIC Agent: The OAI CU and DU can be interfaced with a O-RAN Real-time Intelligent Controller (RIC) over the E2 interface, with support for the RIC Agent provided by ONF.
- Control-Plane Exchanges: The control-plane exchanges between the CU and the DU over F1-C interface, as well as some IP traffic.
- Heterogeneous DUs: The OAI CU and DU split allows for network access to end-users via heterogeneous (3GPP and non-3GPP) DUs, converging the access and core networks.

These key details highlight the functionality and capabilities of the OAI CU, which is a critical component of the OAI architecture in 5G networks.

OAI CU Architecture
---
![CU-and-DU-split-in-OAI-and-the-transported-F1-U-packet-format-2](https://hackmd.io/_uploads/Ske-Hx4TT.png)

The OAI CU is designed to be flexible and scalable, allowing for the deployment of various network configurations and use cases. It supports the integration of various network technologies, enabling the provision of services to a wide range of devices.

In the OAI CU architecture, the control plane functions are centralized in the CU, while the data plane functions are distributed among the DUs (Distributed Units). This split allows for efficient optimization and resource handling, as the CU can manage the overall network performance and the DUs can handle the radio interface processing.

The transported F1-U packet format is used to transport the data between the CU and the DUs. This format ensures that the data is transmitted efficiently and securely across the network. The F1-U packet format is designed to support the integration of various network technologies, allowing for the convergence of access and core networks.

The OAI CU supports multi-vendor applications, such as the integration of OAI CU with third-party DUs. This allows for the development of customized network configurations and the use of different vendor equipment in the same network.

The OAI CU is designed to be modular and extensible, allowing for the addition of new features and capabilities as needed. This ensures that the OAI CU can adapt to changing network requirements and support the latest technologies and standards.

In summary, the OAI CU architecture is a key component of the OAI architecture, providing control plane functionality and supporting various network configurations and use cases. It is designed to be flexible, scalable, and extensible, allowing for the integration of various network technologies and the provision of services to a wide range of devices.
![2021-08-17-CU-DU-DEPLOYMENT](https://hackmd.io/_uploads/HkgGSx46p.png)


---
Source
---
[OAI CU & DU](https://hackmd.io/@Marsyuma/CU-DU)

[CU & OAI CU](https://docs.sd-ran.org/master/oai_cu_cp.html)

[OAI Reference Architecture for 5G and 6G Research with USRP](https://kb.ettus.com/OAI_Reference_Architecture_for_5G_and_6G_Research_with_USRP)





