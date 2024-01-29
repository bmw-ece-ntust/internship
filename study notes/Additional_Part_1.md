
# Additional Part 1 (Interface & AI/ML Module)

## Learning E2 Interface related in Near-RT RIC Platform

:::success
- Goal:
    - [ ] Learning E2 Interface
    - [ ] Learning E2 Service Model
- Useful Links:
    - [O-RAN.WG3.E2AP-v02.01](https://www.o-ran.org/specifications)
    - [ORAN-WG3.E2SM-v02.01](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::

1. Definition E2 Interface 
- The E2 interface is an open interface connecting the near-RT RIC and the E2 nodes (CUs, DUs). It facilitates communication that allows the RIC to control radio resource management and other functionalities within the E2 nodes
- Each E2 node contains data pertaining to RAN functions, which can be published by the E2 nodes. Subsequently, the xApps on the near-RT RIC can subscribe to one or more of these RAN functions through the E2 interface.
2. E2 Interface Characteristics:
    - The E2 interface, an open connection, links near-RT RIC to DUs and CUs in the 5G landscape.
    - Operational on the SCTP protocol over IP.
    - Supports two protocols: E2 Application Protocol (E2AP) and E2 Service Model (E2SM).
    - E2AP messages can seamlessly integrate various E2 Service Models, facilitating functionalities related to RAN metrics and RAN Control.
    - Its applications extend to Key Performance Matrix (KPM), Network Interfaces (NIs), and RAN Control (RC).

3.  E2AP (E2 Application Protocol) provides four services:
    1. **E2 Report**   Involves E2 RIC Indication messages containing data and telemetry from an E2 node. The E2 Report service is activated upon subscription from an xApp to a function offered by the E2 node.
    2. **E2 Insert**  Notifies the xApp about a specific event in the E2 and is activated upon subscription from an xApp.
    3. **E2 Control** : Autonomously initiated by the RIC or triggered by an insert message at the near-RT RIC, it involves a two-message procedure: RIC Control Request from RIC to E2 node, and RIC Control Acknowledge in the opposite direction.
    4. **E2 Policy**: Subscription specifies event trigger and autonomous policy for E2 node resource management.
