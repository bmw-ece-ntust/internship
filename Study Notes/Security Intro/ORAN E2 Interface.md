# ORAN E2 General Aspects and Principles 


## E2 Interface
This is the interface that connects E2 Nodes and the Near RT RIC. Its main objective is to provide the Near RT RIC the necessary E2 Node datas and control the selected RAN function in the E2 Node.
**Functionalities and Principles:**
- Connects endpoints in point-to-point manner.
- Control signal exchange.
- supports interface management procedures based on principles from 3GPP RAN interfaces
- Send predefined info to the Near RT RIC based on preconfigured trigger event
- Send UE ID info to the Near RT RIC based on preconfigured trigger event
- Enables the Near RT RIC to direct the E2 Nodes to suspend an RRM procedure by interupting its local process and forwarding the necessary info to Near RT RIC for processing.
- Provides the E2 nodes with set of policies ehen an event occures
- Supportts the E2 nodes the ability to notify the Near RT RIC of what functionalities it supports.
- Supportts the ebility to query the E2 node for relevant UE or RAN information.

## E2 Node
E2 Node referes to the where the Near RT RIC is connected to, mostly referred as the endpoint, could be CU/DU. This node needs to functions regardless wheteher the Near RT-RIC is working or not.

E2 Node consist of:
- Logical E2 Agent used to terminate the E2 interface, support global services and to forward/receive RIC service messages towards RAN Functions. 
- One or more RAN Functions that support RIC services exposed by the E2 Node to the Near-RT RIC. 
- Other RAN functions that do not support RIC Services. 

