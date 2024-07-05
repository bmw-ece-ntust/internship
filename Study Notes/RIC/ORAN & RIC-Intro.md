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


## RIC (RAN Intelligent Controller)

<div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/S0kMGdq.png" alt="Chart" width="500" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>
<div style="height: 50px;"></div>
RIC is a software-defined component within the Open RAN architecture that functions to manage to do controlling and aptimization within the RAN functions. RIC provides mobile operators with advanced network control, improve network performance, quick enablement of new services, AI/ML driven network control, and supports low latency applications. RIC effectively balances the RAN load, which alleviates network congestion and improve network performance. It customizes RAN functionality by optimization of regional resources, which enables quick launch of new services to build new revenue streams with personalized services. RIC provides advanced control functionality, leveraging analytics and data-drive approaches including advanced ML/AI tools to improve resource management capabilities.
<div style="height: 15px;"></div>

The RIC facilitates multivendor interoparibility by providing a common platform where various elements from different suppliers can be integrated and managed effectively. This interoperability is crucial for breaking the dominance of single-vendor networks, allowing operators more flexibility and choice in their deployments.

<div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/5E2Mhj1.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>

### Non-RT RIC (Non-Realtime RIC)
Non-RT RIC is used to manage operations that does not have tight timing. The Non-RT RIC supports intelligent RAN optimization by providing policy-based guidance, ML model management and enrichment information to the Near-RT RIC function. 

The Non-RT RIC is comprised of two sub-functions:
-	Non-RT RIC Framework – Functionality internal to the SMO Framework that logically terminates the A1 interface and exposes the required services to rApps through its R1 interface.
-	Non-RT RIC Applications (rApps) – Modular applications that leverage the functionality exposed by the Non-RT RIC Framework to perform RAN optimization and other functions. Services exposed to rApps via the R1 interface enable rApps to obtain information and trigger actions (e.g., policies, re-configuration) through the A1, O1, O2 and Open FH M-Plane related services.

Non-RT RIC is a part of SMO, which is an automation platform which applies automation at scale to simplify the complexity of networks, as well as improve network performance, enhance customer experience and minimize RAN operational costs. This SMO is depployed in the center of service provider network which enables non-real-time (> 1 second) control of RAN elements and their resources through specialized applications called rApps. Non-RT RIC can use data analytics and AI/ML training/inference to determine the RAN optimization actions for which it can leverage SMO services such as data collection and provisioning services of the O-RAN nodes as well as the O1 and O2 interfaces.



<div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/aRrXv5C.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>

The key capabilities of the SMO that provide RAN support in O-RAN are:
-	FCAPS interface to O-RAN Network Functions
-	Non-RT RIC for RAN optimization
-	O-Cloud Management, Orchestration and Workflow Management


The SMO performs these services through four key interfaces towards other O-RAN architecture elements.
- A1 Interface between the Non-RT RIC in the SMO and the Near-RT RIC for RAN Optimization.
- O1 Interface used by SMO for the FCAPS support of the O-RAN Network Functions (excluding O-RU).
- In the hybrid model, Open Fronthaul M-plane interface between SMO and O-RU for FCAPS support.
- O2 Interface between the SMO and the O-Cloud to provide platform resources and workload management.

### Near-RT RIC (Near-realtime RIC)
Near RT RIC operates within a time frame that is shorter than traditional RAN management systems but not as immediate as the millisecond-level reactions required for some physical layer functions. The Near-RT RIC hosts one or more xApps that use E2 interface to collect near real-time information (e.g., on a UE basis or a Cell basis) and provide value added services. The Near-RT RIC control over the E2 Nodes is steered via the policies and the enrichment data provided via A1 from the Non-RT RIC. Based on the available data, the Near-RT RIC generates the RAN analytics information and exposes it via Y1 interface. 

## RAN Functional Split
<div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/hseTcIO.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>

Since the establishment of 5G NR standard, there's been a push to dissagregate the BBU in order to acheive higher flexibility. For
disaggregation to happen, hardware and
software components must be interoperable,
letting network engineers mix and match
these units from different vendors.
Disaggregation also brings tradeoffs in
deciding which unit should control certain
operations – the functional split.

## CU (Centralized Unit) - Higher L2 and L3
The centralized unit software that runs
the Radio Resource Control (RRC) and
Packet Data Convergence Protocol
(PDCP) layers. The gNB consists of a CU
and one DU connected to the CU via Fs-C
and Fs-U interfaces for CP and UP
respectively. A CU with multiple DUs will
support multiple gNBs. The split
architecture lets a 5G network utilize
different distributions of protocol stacks
between CU and DUs depending on
midhaul availability and network design. It
is a logical node that includes the gNB
functions like transfer of user data, mobility
control, RAN sharing (MORAN),
positioning, session management etc.,
except for functions that are allocated
exclusively to the DU. The CU controls the
operation of several DUs over the midhaul
interface. CU software can be co-located
with DU software on the same server on
site.
## DU (Distributed Unit) - Lower L2
The distributed unit software that is
deployed on site on a COTS server. DU
software is normally deployed close to the
RU on site and it runs the RLC, MAC, and
parts of the PHY layer. This logical node
includes a subset of the eNodeB
(eNB)/gNodeB (gNB) functions, depending
on the functional split option, an
## RU (Radio Unit) - L1
This is the radio hardware unit that
coverts radio signals sent to and from the
antenna into a digital signal for
transmission over packet networks. It
handles the digital front end (DFE) and the
lower PHY layer, as well as the digital
beamforming functionality. 5G RU designs
are supposed to be “inherently” intelligent,
but the key considerations of RU design
are size, weight, and power consumption.
Deployed on site.
