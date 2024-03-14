# O - RAN Architecture (Part 2)

## O - RAN Architecture Elements

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Logical%20Architecture%20of%20O-RAN.png) High Level View of O-RAN Architecture

### Service Management and Orchestration (SMO)
1. #### SMO Architecture Principles

Service Based Architecture (SBA) introduces the roles of service producer and service consumer together with standardized service-based interfaces. These standardized service-based interfaces enable interoperability within the SMO. SBA is not concerned with the implementation, but it defines logical functions in their service producer and consumer roles. When properly applied the SBA approach can enable the following:

* Validates produced services with consumer use cases.
* Identifies service operations with their information model defining semantic behaviour.
* Specifies the API and a data model for a syntactic interface.
* Identifies common services that can be produced by a single producer such as those that are commonly used by multiple internal consumers (e.g., authentication, authorization, service registration and discovery, data management, etc.).

2. #### SMO Functionality
Introduction to SMO Functionality

This clause describes the functionality provided by the SMO in O-RAN architecture. In a Service Provider’s Network, there can be many management domains such as RAN management, Core Management, Transport Management, End to End Slice Management etc. In the O-RAN architecture, SMO is responsible for RAN domain management. The SMO description in this architecture document is focused on the SMO services that support the RAN. The key capabilities of the SMO that provide RAN support in O-RAN are:

* FCAPS interface to O-RAN Network Functions
* Non-RT RIC for RAN optimization
* O-Cloud Management, Orchestration and Workflow Management

The SMO performs these services through four key interfaces towards other O-RAN architecture elements.

* A1 Interface between the Non-RT RIC in the SMO and the Near-RT RIC for RAN Optimization.
* O1 Interface used by SMO for the FCAPS support of the O-RAN Network Functions (excluding O-RU).
* In the hybrid model, Open Fronthaul M-plane interface between SMO and O-RU for FCAPS support.
* O2 Interface between the SMO and the O-Cloud to provide platform resources and workload management

SMO does not define any formal interface towards the Non-RT RIC. An SMO deployment, therefore, may make its own design choice for creating a boundary towards the Non-RT RIC Framework, or choose not to implement a clear boundary at all.

The following definitions apply to the functionality of the SMO:
* Non-RT RIC Framework Anchored Functionality – This functionality is associated with the Non-RT RIC Framework itself. Examples include the A1 and R1 interfaces (see Clause 5.3.1.2.3).
* O-RAN SMO Framework Anchored Functionality – This functionality is not associated with the Non-RT RIC Framework. Examples include the O1, Open FH M-plane and O2 interfaces.
* Non-anchored Functionality – This functionality may or may not be associated with the Non-RT RIC Framework.

These terms and the relationships between the SMO services related to rApps are illustrated in Figure 5.3-1 below.Extending the “Services that enable rApps” outside the Non-RT RIC (i.e., into the SMO Framework), as shown in this figure, denotes that the R1 services being exposed to rApps may either come from the Non-RT RIC or the SMO. Please refer to [21] for more details.


### Near-RT RIC
### O-CU-CP
### O-CU-UP
### O-DU
### O-RU
### O-eNB
### O-Cloud



## O - RAN Architecture Interfaces
The diagram outlines the Open-RAN (O-RAN) architecture in High Level Perspective, showing interfaces like A1, O1, Open Fronthaul M-plane, and O2 linking the Service Management and Orchestration (SMO) framework to O-RAN Network Functions and O-Cloud.

O-Cloud includes the O-Cloud Notification interface for relevant O-RAN Network Functions to receive notifications. O-RAN Network Functions can be hosted on O-Cloud or customized hardware, managed via the O1 interface.

The Open Fronthaul M-plane interface supports O-RU management in hybrid mode. NFs on O-Cloud may use APIs from the Accelerator Abstraction Layer (AAL). 

The Near-RT RIC NF provides RAN analytics via the Y1 service interface, accessible after authentication and authorization by subscribing or requesting via the Y1 service interface. Y1 consumers within PLMN trusted domain can access directly, while those outside use secure access via an exposure function.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Logical%20Architecture%20of%20O-RAN.png) Logical Architecture of O-RAN



## Source
* [O-RAN Work Group 1 (Use Cases and Overall Architecture)](https://orandownloadsweb.azurewebsites.net/specifications)
* [O-RAN Architecture Overview](https://docs.o-ran-sc.org/en/latest/architecture/architecture.html)
