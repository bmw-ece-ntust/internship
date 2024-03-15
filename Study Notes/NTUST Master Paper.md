## O-RAN Components

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
