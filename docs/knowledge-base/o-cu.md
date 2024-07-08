### O-CU

The Central Unit (CU) oversees the higher layers of the protocol stack, particularly the SDAP, PDCP, and RRC layers. Its primary roles encompass:

* Network Management: The CU manages broader aspects of data flow within the network, dictating how data packets journey through the infrastructure.
* Coordination with DUs: To ensure coherent communication between the core network and the Radio Units (RUs), the CU liaises with the DUs, guiding them on data management tasks.
* Strategic Decision-making: For overarching network decisions, such as user mobility management and establishing user-specific communication bearers, the CU plays a pivotal role.

To draw a parallel, the CU is akin to a symphony conductor, ensuring each section comes together harmoniously for a flawless performance.

Acronym explainers:

* SDAP (Service Data Adaptation Protocol) Layer: This layer is responsible for mapping between QoS flows and data radio bearers and for marking QoS flow ID on packets.
* PDCP (Packet Data Convergence Protocol) Layer: This layer plays a crucial role in the transmission of user data and control information between the user equipment (UE) and the network. It handles tasks such as header compression, security (ciphering and integrity protection), and in-sequence delivery of upper layer PDUs.
* RRC (Radio Resource Control) Layer: This layer is responsible for the establishment, configuration, maintenance, and release of radio bearers. It deals with aspects such as handover, broadcast of system information, paging, and control of UE measurement reporting.
