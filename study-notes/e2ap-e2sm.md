### Overview

E2AP (E2 Application Protocol) defines the general protocol used for communication between the near-real-time RIC (nRT-RIC) and disaggregated E2 Nodes in an O-RAN (Open Radio Access Network) architecture. It operates over SCTP/IP as the transport protocol. E2AP supports various action types, including Report, Insert, Policy, and Control. Essentially, E2AP enables the exchange of information and commands between different components within the network.

On the other hand, E2SMs (E2 Service Models) act as “contracts” between an xApp (an application running on the RIC) and an E2 Node (such as a gNB or DU). These service models define function-specific protocols that are implemented on top of the E2AP specification. When an xApp communicates with an E2 Node, it uses the relevant E2SM to convey specific controls and events. Implementing a particular E2SM on the gNB side requires explicit feature development and interface enhancements.

To summarize,  E2AP provides the underlying communication framework, while E2SMs define the specific protocols for different functions within the O-RAN network.
