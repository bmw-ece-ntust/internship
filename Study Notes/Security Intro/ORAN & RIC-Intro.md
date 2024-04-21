```
 I think student can focus on below task:
- RIC E2  and O1 interface test(Auray already setup RIC test tool)
- According O-RA N WG11 security Spec, develop RIC security test case(Auray has RIC platform)
```



>## Comparison of RAN Terms
>| Term | Description |
>|---|---|
>| O-RAN (Open Radio Access Network) | Industry alliance defining open interfaces for mobile network equipment |
>| Open RAN  | Reference to the O-RAN Alliance’s publication of numerous RAN architecture specifications. Those “ORAN” specifications are the Alliance’s core theme and a foundation in its mission to offer an open architecture in the RAN ecosystem. |
>| OpenRAN  | Refers to the OpenRAN Telecom Infra Project (OpenRAN TIP). The OpenRAN project group was created to focus on developing a vendor-neutral hardware and software-defined technology based on open interfaces, like those defined by O-RAN with the Open RAN (ORAN) framework. |
>| vRAN (Virtual RAN) | RAN functions virtualized as software  implementations on general-purpose processors (GPPs), such as x86, using commercial off-the-shelf (COTS) platforms. This includes virtualizing functions like L1, L2, L3, and transport processing. Additionally, there is a separation of the control plane (CP) and the data plane (DP) to allow independent scaling, aligning with 3GPP and O-RAN 5G standards. Less latency-sensitive controller functions are centralized closer to the core network edge, optimizing resources through statistical multiplexing. |
>| Cloud RAN (or C-RAN) | Centralized RAN architecture with BBUs in a data center |





# O-RAN (Open Radio Access Network)
O-RAN is a set of RAN standarzation in mobile networks infrastructure that aims to break the prioprietary-ness of this field in industry right now. Traditionally, RANs were dominated by a few vendors with proprietary systems, leading to limited flexibility, higher costs, and slower innovation for operators.

<img src="https://imgur.com/Z1EhHOj.png" alt="Chart" width="500" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">



## O-RAN Architecture
<div style="display: flex; justify-content: space-around;">
    <img src="https://i.imgur.com/jhqJkkB.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
    <img src="https://imgur.com/ymDsyon.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>
<div style="height: 50px;"></div>

O-RAN breaks down the traditional cellular network into smaller, more manageable pieces and allows for more flexible control:

* **Service Management and Orchestration (SMO):** This acts as the brain of the system, managing how all the other parts work together. It connects and controls the RICs, O-Cloud, and the radio units (O-CU, O-DU, O-RU).
* **RAN Intelligent Controllers (RICs):** These are like smart assistants for the network, optimizing performance in two ways:
    * **Near-real-time RIC:** Makes adjustments with very fast data (for things like congestion control).
    * **Non-real-time RIC:** Handles broader network planning and optimization (like adding capacity in a specific area).
* **O-Cloud:** This is the cloud platform that runs all the virtual network functions (VNFs) needed by the RICs and other elements. 
* **Radio Units (O-CU, O-DU, O-RU):** These are the physical parts that handle the actual radio communication:
    * **O-CU:** Handles higher-level protocols like radio resource control. 
    * **O-DU:** Takes care of mid-level protocols related to data transmission.
    * **O-RU:** Processes the radio signals themselves.

By separating these functions and using open interfaces, O-RAN allows for more flexibility in choosing vendors and customizing the network. 


### Interfaces
- O1 Interfaces: These interfaces enable management functionalities like configuration, monitoring, and fault detection between the SMO and other O-RAN components.  In the image, they are labelled  with "01" and connect the SMO to all the other elements.

- E2 Interfaces:  These interfaces are crucial for real-time communication between the RICs (RAN Intelligent Controllers) and the O-DUs (distributed units) and O-CUs (central units). They allow the RICs to control and optimize the radio units  by sending control information and receiving data.  The E2 interfaces are represented by the lines labelled "E2" in the image.
- E1 Interfaces: though not an official O-RAN standard, acts as a translator in some O-RAN deployments. It's an older interface understood by legacy equipment that might be integrated into the network. This allows these elements to communicate with newer O-RAN components using the E1 interface for both control and user data traffic, even though O-RAN has its own set of interfaces for internal communication.
- A1 Interfaces: The A1 interface in O-RAN connects the non-real-time RIC, responsible for broader network planning, with the near-real-time RIC handling constant adjustments. This allows the non-RT RIC to send policies, receive feedback on their effectiveness, and share additional data for optimization, ultimately enabling a more intelligent and adaptable network.
- F1-c and F1-u Interfaces: These interfaces connect the Open Fronthaul transport network. F1-u carries the user plane traffic, while F1-c carries the control plane traffic.
- Open Fronthaul: 
Open Fronthaul, in O-RAN, refers to the interface between the Radio Unit (O-RU) and the Distribution Unit (O-DU). It's further divided into three planes for different types of communication:
    - Control Plane (C-Plane): This plane carries messages for real-time control of the radio unit, such as scheduling data transmission and beamforming. Think of it as the conductor telling the instruments (radios) when and how to play.
    - User Plane (U-Plane): This plane carries the actual user data itself, like your voice calls or video streams. It's the music being played by the instruments.
    - Synchronization Plane (S-Plane): This plane ensures all the radio units are in perfect timing for smooth communication. Imagine it as the metronome keeping everyone in sync.


