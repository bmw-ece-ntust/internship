# Service Management and Orchestation

## OSC SMO Introduction

![oran](https://hackmd.io/_uploads/ryxuJdcUA.png)

The ORAN SC (OSC) is a software community that focuses on developing and defining specifications for ORAN implementations. It is a collaborative platform for network equipment vendors, operators, and software developers to drive innovation and interoperability in the telecommunications industry [[1](https://blogs.vmware.com/telco/smo/)].

SMO used for increasing effecienct for operational and make network maitenance cost lower.  It is an effective solution for boosting operational efficiency and reducing network maintenance costs. SMO enables remote monitoring and control of functions and devices within the ORAN network, providing real-time diagnostics and troubleshooting.

The O1 Interface is a logical connection between all “O-RAN Managed Elements (MEs)” and the “management entities” within the SMO framework [[2](https://hemaprajapati.medium.com/what-is-o1-interface-in-oran-4c389cfe1bcf)]. The purpose of the O1 interface is to ensure the operation and management e.g. FCAPS, Software Management, and file management of the O-RAN components.

In other words, we can elaborate, the O1 interface enables the management of all O-RAN components that need to be orchestrated and the associated O-RAN network functions. The components managed via O1 include the near-RT RIC, the O-CU, and the O-DU in 5G NR. The O-CU corresponds to a predefined combination of O-CU-CP and O-CU-UP.

![image](https://hackmd.io/_uploads/H1Kzqv580.png)

The figure above shows an extracted logical O-RAN architecture to illustrate the O1 interface and its influence on O-RAN Manage Elements, including the O-eNodeB. The O-RU termination of the O1 interface towards the SMO is currently under investigation so this interface is shown dashed.

### SMO Standards

You can read the paper here [[2](https://www.techrxiv.org/users/686134/articles/683284-unifying-3gpp-etsi-and-o-ran-smo-interfaces-enabling-slice-subnets-interoperability)]

Also the white paper [here](https://files.techmahindra.com/static/img/pdf/oran-smo-whitepaper.pdf)

### SMO Interface
The diagram below shows key interfaces in O-RAN architecture.
![0B12LqB](https://hackmd.io/_uploads/rJ8mmJlw0.png)

The SMO performs its functions/services through four key interfaces to the O-RAN Elements:

* A1 Interface between the Non-RT RIC in the SMO and the Near-RT RIC for RAN Optimization.
* O1 Interface between the SMO and the O-RAN Network Functions for FCAPS support.
* In the hybrid model, Open Fronthaul M-plane interface between SMO and O-RU for FCAPS support.
* O2 Interface between the SMO and the O-Cloud to provide platform resources and workload management.

### SMO Capabilities
The key capabilities of the SMO that provide RAN support in O-RAN are:

* FCAPS interface to O-RAN managed functions (network functions);
* Non-Real Time RIC for RAN optimization;
* O-Cloud Management, Orchestration and Workflow Management.

#### FCAPS to O-RAN Network Functions

FCAPS: Fault, Configuration, Accounting, Performance, Security. They are all the information needed for functions management. Supporting FCAPS for O1 interface:

• Performance Management (PM)
• Configuration Management (CM)
• Fault Management (FM)
• File Management
• Communications Surveillance (Heartbeat)
• Trace
• Physical Network Function (PNF) Discovery
• PNF Software Management.

#### Non-Real Time RIC for RAN optimization

SMO supports Non-RT RIC for RAN optimization.

The Non-RT RIC is comprised of two sub-functions:

* Non-RT RIC Framework – Functionality internal to the SMO Framework that logically terminates the A1 interface and exposes the required services to rApps through its R1 interface.
* Non-RT RIC Applications (rApps) – Modular applications that leverage the functionality exposed by the Non-RT RIC Framework to perform RAN optimization and other functions via the A1, O1, O2 and R1 interfaces.

#### O-Cloud Management, Orchestration and Workflow Management

The SMO utilizes the O2 interface to the O-Cloud to provide:

* The capability of managing the O-Clouds;
* Support for the orchestration of platform and application elements and workflow management.

The example functionalities should be supported in SMO:

* Discovery and administration of O-Cloud Resources
* Scale-In, Scale-Out for O-Cloud
* FCAPS (PM, CM, FM, Communication Surveillance) of O-Cloud
* Software Management of Cloud Platform
* Create, Delete Deployments and Associated Allocated O-Cloud Resources
* Scale-In, Scale-Out Deployments and Allocated O-Cloud Resources
* FCAPS (PM, FM) of Deployments and Allocated O-Cloud Resources
* Software Management of Deployments

### SMO Functions

![iyXQdYk](https://hackmd.io/_uploads/ryfFQJgDR.png)

|                SMO Functions                |                               Descriptions                               |                                                         Example                                                         |
|:-------------------------------------------:|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| Inherent Non-RT RIC Framework Functionality | This functionality is definitively associated with the Non-RT RIC itself |                         The two interfaces “owned” by the Non-RT RIC: The A1 and R1 interfaces                          |
| Inherent O-RAN SMO Framework Functionality  |  This functionality is definitively not associated with the Non-RT RIC   |                                                The O1 and O2 interfaces                                                 |
|    Implementation Variable Functionality    |   This functionality may or may not be associated with the Non-RT RIC.   | An SMO provider is free to include this functionality in or exclude this functionality from a Non-RT RIC implementation |


## OSC SMO Code Structure

Here's the SMO Repository on gerrit. On the way to explore. [[3](https://gerrit.o-ran-sc.org/r/admin/repos,125)]

### SMO O1 

> NONE

### SMO A1

> NONE