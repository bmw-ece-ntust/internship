# O-RAN E2 Interface
## Table of Contents
- [O-RAN E2 Interface](#o-ran-e2-interface)
  - [Table of Contents](#table-of-contents)
  - [E2 Introduction](#e2-introduction)
  - [Protocol](#protocol)
  - [About Performance](#about-performance)
  - [References](#references)
  

## E2 Introduction
![img](../images/o-ran-architecture.png)
E2 Interface is the interface that is connected to specific entitites within the base station like O-DU, O-CU, and RU to near Real-Time RIC (nRT RIC). The interface provide possibility for users to control what is happening from xApps/nRT RIC, and gets data collection and feedback from the entities (O-DU, O-CU, RU). E2 interface operates over the Stream Control Transmission Protocol (SCTP), supporting real-time functions crucial to network adaptivity and resiliency [2].

 Use cases can be found in [2].

 ## Protocol
 E2 Protocol stacked above of IP Layer, they are SCTP, E2AP, and E2AP Messages carrying E2SM from IP to above. E2AP is a specific O-RAN Alliance over SCTP/IP as the transport protocol. On the top of E2AP, application-specific controls and events are conveyed through E2 service models (E2SM), also used by the xApps in the Near-RT RIC.

 E2AP Terminologies:
 - E2 node: disaggregated network function O-CU-CP, O-CU-UP and O-DU of a gNB or a combined O-eNB are called the E2 nodes. The nodes supports E2 interface towards nRT RIC and O1 interface towards Non Real-Time RIC (NRT RIC).
 - RAN Functions: specific function in an E2 node, includes network interfaces and RAN internal functions handling user equipment context handlers, call handlers, paging, etc.
 - RIC Service: provided on an E2 Node to provide access to message and measure and/or enable control of the E2 Node from the nRT RIC, includes:
   - REPORT
   - INSERT
   - CONTROL
   - POLICY
   - QUERY
 - RAN Function ID: local identifier of a specific RAN function within an E2 Node that supports one or more RIC Services using a specific E2SM, and a same E2SM can be used by more than one RAN Function in the same E2 Node.
 - Style: Group of different types of data for each RIC Services, where E2SM may support many styles for each RIC services.

More about E2 Nodes:
![img](../images/E2Node.png)
- Event trigger definition: contains the definition of event triggers for which E2 node can be requested to report the event to near-RT RIC. The definition includes the event styles supported by the E2 node.
- Report definition: contains the definition of event reports and the report styles supported by the E2 node.
- Insert definition: contains the definition of information on which the E2 node has to exhibit “report and wait for control” semantics and the insert styles supported by the E2 node.
- Control definition: contains the definition of attributes/configurations/call parameters to be controlled on the E2 node and the control styles supported by the E2 node.
- Policy definition: contains the definition of policy to apply at the E2 node when the specified event trigger is hit.

General Workflow of E2 Interface:
![img](../images/E2NodeGeneralWorkflow.png)
First the interface is being initialized between E2 node and nRT RIC. E2 node advertises the list of RAN functions that it supports and the corresponding E2SM supported for each RAN function. The xApps that runs on nRT RIC subscribe the E2 node, providing the event triggers and what actions to perform when it triggers. The action to perform is either REPORT or INSERT, the E2 node notifies the nRT RIC when the event occurs. If the nRT RIC detects REPORT, the xApp provide CONTROL request to the E2 node. the CONTROL enables xApp to control the call processing, radio resource allocation, handover control, idle mode mobility control, radio admission, carrier aggregation, and dual connectivity behaviors.

## About Performance
O-RAN Community released E2SM-KPM (E2SM Key Performance Measurement) document that specifies the capabilities exposed over the E2 interface [3]. 

## References
[1] https://rimedolabs.com/blog/o-ran-architecture-nodes-interfaces/ 

[2] https://www.5gtechnologyworld.com/how-does-5gs-o-ran-e2-interface-work/ 

[3] https://www.o-ran.org/blog/o-ran-alliance-introduces-48-new-specifications-released-since-july-2021

[4]O-RAN E2 Service Model (E2SM) KPM 5.0; https://specifications.o-ran.org/specifications 