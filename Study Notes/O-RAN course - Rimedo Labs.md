```
Youtube link can be accessed here : https://www.youtube.com/watch?v=otlUOgwitmU
```
￼
# 5G Architecture
<img width="748" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/ff97db08-41b0-43e2-9d78-44994e22961a">

# List of Abbreviations
￼<img width="662" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/41f96464-29c5-435c-99e5-4bf708e25eb7">

￼

 
￼
# O-RAN Defined Entities
<img width="233" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/af72f17c-18bf-4634-9ed9-5be32a965a87">

```
O-Cloud —> comprising the nodes to host the functions, supporting SW components, MANO(Management and Orchestation) Functions
O-RU —> Logical node hosting Low Physical Layer (PHY) and RD based on Low Layer Split (LLS)
O-CU-CP —> Logical node hosting Radio Resource Control (RRC) and Control Plane (CP) part fo Packet Data Convergence protocol (PDCP)
O-CU-UP —> Logical node hostingg Service Data Adaptation Protocol (SDAP) and User Plane (UP) part of Packet Data Convergence protocol (PDCP)
O-DU —> Logical node hosting RLC/MAC/High -PHY layes based on LLS
Near-RT RIC --> Logical node which enbales nRT control/optimization of RAN elements and resources via fine-grained data collection and acttions over E2. This node may incude Artificial Intelligence or Machine Learning workflow
xApp —> application designed to run on nRT RIC : likely to consist of one or more u-services, identifies data to consume and provide, independent of the nRT RIC, may be provided by 3rd party
SMO —> System supporting orchestation of O-RAN components
Non-RT RIC —> Logical node enabling Non-RT control/optimization of RAN elements and resourced, AI/ML workflow, and policy based guidance of applications/features in nRT RIC
```
From the explanation above, we can conclude that O-Cloud is a system that holds different parts of a network, like the **O-RU which manages low-level network functions**, the **O-CU-CP for controlling radio resources**, and the **O-CU-UP for managing user data**. The O-DU handles various layers of network communication. N**ear-RT RIC is a control node that uses real-time data to optimize network elements**, possibly using AI or machine learning, while **xApps are applications that run on it**, independent of the RIC. **SMO orchestrates these components**, and **Non-RT RIC also controls network elements but without real-time optimization,** using AI, ML, and policies to guide applications within the near-RT RIC.


