<img width="530" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/f294a79d-137b-4695-ba09-1ba31ab8f446">## O-RAN Components

1. SMO: The SMO is responsible for network management functions
and automatic deployment of network virtualization.
2. Non-real-time RAN Intelligent Controller (Non-RT RIC): The Non-
RT RIC obtains RAN and user-related data through SMO to manage and optimize RAN resources through the near-real-time RAN intelligent controller (Near-RT RIC).
3. Near-real-time RAN Intelligent Controller (Near-RT RIC): The Near-
RT RIC provides radio resource management and optimization of real-time RAN function control.
4. O-CU: The O-CU handles layer 3 (L3) protocols of gNB. The control plane (CP) and the user plane (UP) functionalities of the L3 protocols are handled by O-CU-CP and O-CU-UP, respectively. The O-CU-CP includes the radio resource control (RRC) and packet data con-vergence protocol (PDCP), while the O-CU-UP includes the service data adaptation protocol (SDAP) and PDCP.
5. O-DU: The O-DU handles the layer 2 (L2) protocols (i.e., radio link control (RLC) and media access control (MAC)) and the higher physical layer (High-PHY) functionalities of the gNB.
6. O-RU: The O-RU is responsible for the lower physical layer (Low-PHY) and radio frequency (RF) signal processing functions.


## Process of Setting Up RRC between UE, CU, and DU in Telecommunications Network
<img width="437" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/2fbd1123-6ddf-492f-a1e8-163fa559922d">

The process begins with the gNB granting the UE access to radio resources. The CU then initiates the RRC setup by sending DL RRC Message Transfer to the UE, followed by the UE responding with UL RRC Message Transfer, completing the RRC setup. Next, the CU sends UE Context Setup to the DU to establish UE context, including SRB and DRB configuration, possibly accompanied by a Security Mode Command for AS security activation. Upon DU setup, the CU receives UE Context Response. Subsequently, Security Mode Complete is sent to the CU via UL RRC Message Transfer. Finally, the CU sends RRC Reconfiguration with DL RRC Message Transfer to establish SRB and DRB, receiving RRC Reconfiguration Complete with UL RRC Message Transfer as confirmation

## O-CU
<img width="574" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/8239fb5c-642d-4de1-9774-e772cc591446">
Above is the functional blocks of O-CU. The explanation of each blocks is as below
1. O-CU-CP-OAM : receives configuration from OAM (Operations, Administration, and Maintenance) and performs operations for Operations Control Unit Control Processor. 
2. gNB Procedure Management: This part handles services not directly related to specific users, like managing connections between different network interfaces, following 3GPP standards.
3. Cell Procedure Management: Manages individual cell-level operations at the O-CU, such as managing system information and activating cells, following 3GPP standards.
4. UE Procedure Management: Deals with controlling user access and communication procedures at the O-CU, ensuring smooth communication between users and the network, following 3GPP standards.
5. RRC Encoder and Decoder: Handles encoding and decoding of specific types of communication messages, facilitating communication between cells and users, following 3GPP standards.
6. NGAP Encoder and Decoder:  Manages encoding and decoding of certain network messages, facilitating communication between gNB and AMF, following 3GPP standards.
7. XnAP Encoder and Decoder: Handles encoding and decoding of certain network messages, facilitating communication between different gNBs, following 3GPP standards.
8. F1AP Encoder and Decoder: Deals with encoding and decoding messages for communication between O-CU and O-DU, following 3GPP standards.
9. O-CU-UP Control: Configures and manages the O-CU user plane entities based on the E1 interface.
10. eGTPu: Handles the exchange of user plane data between different modules in the network, ensuring data packets are correctly routed to their destinations.
11. NR PDCP: Handles various tasks related to data transmission, such as compression, protection, and routing, according to 3GPP standards.
12. SDAP: Manages the mapping of Quality of Service flows to Data Radio Bearers, as defined in 3GPP standards.

<img width="530" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/be02e668-8821-4595-9e53-e934409bcfed">
A bit different from O-CU, OAI (Open Air Interface) doesn’t implement all O-CU (Open Central Unit) functions. As we can see from the figure above about OAI CU blocks and the figure before about O-CU functional blocks, OAI-CU doesn’t support OAM and SDAP and some of the names changed as well. For example, NR PDCP and eGTPu became PDCP and and GTP-U.
