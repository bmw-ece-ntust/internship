## O1 Interface
The O1 interface supports the NETCONF protocol to configure and manage the network elements in the O-RAN solution. These network elements include Near RT-RIC, O-CU, O-DU and O-RU. The SMO uses data models to drive the configuration and management of the network elements.
For an example of how the SMO (NETCONF client) interacts with the RIC, CU, DU and RU (each of which are NETCONF servers), see diagram below. The implementation is based on the NETCONF implementation of OpenDayLight (ODL),
and User Interface (UI) is based on ODL Community GUI (DLUX).

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/f309f007-d895-4202-b5e9-e503411cc9ba)

The SMO can offer REST APIs that can be used to drive the configuration on the RIC, CU, DU and the RU. 

## SMO's Role
The SMO acts as a NETCONF client on the O1 interface, with the network elements acting as NETCONF server and it is evaluating several options to implement the NETCONF client.

Implementors of NETCONF server on the network elements such as Near RT-RIC, O-CU, O-DU and O-RU have several options to use or implement from. One open source option is Netopeer2. Whatever source is used to implement the O1 interface do note that it needs to support YANG model for NETCONF monitoring.
The ietf-netconf-monitoring support allows the NETCONF client to list and download all YANG schemas that are used by the device. NETCONF client can only communicate with a device if it knows the set of used schemas (or at least a subset).

One of the purposes of the SMO is to onboard applications, whether they are rApps running on non-RT RIC, or xApps running on near-RT RIC. After they are onboarded, the SMO needs to keep an application package catalog for what applications are available for the operator to deploy or create instances of.
To be able to onboard those applications, the SMO needs to be able to understand how the application is packaged.


## O1/VES Interface
The O1/VES interface supports the monitoring side of SMO. The diagram below shows how the Network Elements interact with the O1/VES interface in the SMO.

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/9a4b2229-f98d-49e9-9cbe-a34eb884f873)

Another view of the same can be seen in the diagram below. In this case the events are picked up by the VES Agents which formats them in the form of a VES Event and sends it towards the VES Collector.
The VES Collector stores the events in InfluxdB and alternatively to the Elasticsearch engine and/or the Kafka bus. The event data can then be picked up by Grafana or any other application to perform any analysis on the data.

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/2ffb857e-4e46-47b2-9526-3d398d898b6d)

## Example Topology of SMO to Managed Elements
![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/26816eca-4d9b-4821-b18d-29fe67070e19)

