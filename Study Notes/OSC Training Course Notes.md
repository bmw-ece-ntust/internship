Video can be accessed through this link : https://www.youtube.com/watch?v=Bd003K0vqpg

## Overall Mobile Networks
<img width="731" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/18a81502-c687-4e85-a751-7ff19bdf8751">

The image above is the infrastructure of the network which plays a role of the access network, which provides user access, and the core network, which connects different parts of the network and acts as a gateway to other networks. Providers are decentralizing VBUs inside Base Band Unit (BBU) pools for cost reduction and Resource sharing. Virtualizing BBUs into virtual machines is to prepare future connections, disaggregating control and user plans for flexibility, and optimizing the system with open Application Programming Interfaces (APIs)  to attract more vendors, lower company’s spending, and improve competition and information. The O-RAN Alliance, known as the open RUN organization, is primarily composed of mobile network operators, vendors, and academia.


## Open RAN Architecture
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/1ebcb0f3-05e3-4a0a-9a00-726f8babe6ad)

For this O-RAN prototype, it focuses on the non-real-time RIC, new real-time RIC, central unit (CU), and distributed unit (D1Uu). The non-real-time RIC is responsible for energy management and machine learning training. The real-time RIC manages ideologies and case management with more controls. The O-CU and O-DU are connected through different interfaces. Furthermore, the O-DU architecture is responsible for distributed unit processing. The architecture consists of a high-level functional block with the rse, mac, and hifi layers. 


<img width="607" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/42bbb6e0-78f3-479a-8ae6-6461f00ae7ff">

The processing architecture of the O-DU involves the division of tasks into multiple threads, each catering to specific functionalities such as overall audio processing, app handling, and protocol management like SCTP and EGTP, alongside dedicated threads for lower MAC and stick handling. Layer one processing encompasses essential tasks like channel processing and error correction procedures. The system interfaces externally with SMo and real-time LIC via F1 interfaces, while internally connecting through RC and Layer 1 to Layer 2 interfaces. The F1 handler manages messages to/from the CUC, categorized into MAC cell-specific, MCU-specific, and generic APIs, while the F1 interface handles tasks like uplink CCH and broadcast requests. Deployment-specific configurations for the air interface are also addressed.
