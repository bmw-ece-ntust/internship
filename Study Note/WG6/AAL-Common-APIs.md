# Part 2: Common APIs in WG6
- Goal : 
    - [x] To know the common requirements and object model of AAL
    - [x] To know AALI-C-Mgmt
    - [x] To know AALI-C-App

- Outcome (Study Note) : 
    - Learn about the common requirements and object model of AAL
    - Learn about the AALI-C-Mgmt
    - Learn about the AALI-C-App

***

## I. Common Knowledge
AAL Interface has two parts:
* **AALI-C**: A profile independent set of functions between AAL Application(s) and underlying AAL Implementation(s) including management and orchestration within an O-Cloud platform.
* **AALI-P**: A set of profile specific interfaces dependent upon the profile selected e.g., FEC.
    
Within the AALI-C interface there are two parts:
* **AALI-C-Mgmt**: Common administrative operations, actions, and events between the O-Cloud IMS and the HW Accelerator Manager (HAM). The IMS provides the O2 interface towards the SMO. The HAM terminates the AALI-C-Mgmt interface.
* **AALI-C-App**: Common operations/actions/events toward an AAL Application. These operations are between the AAL Implementation and the AAL Application (AAL-App).
    
## II. AALI-C-Mgmt
The AALI-C-Mgmt profile, a fundamental component within the Cloudification and Orchestration Workgroup (WG6) of the O-RAN Alliance, focuses on **managing the administrative aspects of accelerators** within the O-Cloud infrastructure. As part of the broader AAL Acceleration Abstraction Layer Interface, AALI-C-Mgmt plays a crucial role in facilitating seamless communication between the Accelerator Manager and the O-Cloud Infrastructure Management Service.

AALI-C-Mgmt addresses **common administrative operations, actions, and events** associated with **accelerator lifecycles**. This includes overseeing the allocation and deallocation of accelerator resources, ensuring fault management, and incorporating performance service assurance functions. By streamlining these administrative tasks, AALI-C-Mgmt contributes to the efficient orchestration and management of accelerators within the O-RAN architecture.

The AAL Common API serves as the underlying mechanism for AALI-C-Mgmt, providing a standardized interface for managing the lifecycle of accelerators and their profiles. This commonality ensures interoperability and consistency in handling administrative operations across different components of the O-RAN ecosystem.
    
## III. AALI-C-App
A complementary element to AALI-C-Mgmt, the AALI-C-App profile is another pivotal facet of the AAL Acceleration Abstraction Layer Interface. In the Cloudification and Orchestration within O-RAN's WG6, AALI-C-App is designed to **handle common operations, actions, and events** relevant to Radio Access Network **(RAN) AAL Applications**.

AALI-C-App **facilitates** the seamless **interaction** between **AAL Applications and the O-Cloud infrastructure**, ensuring that the requirements of RAN applications are met efficiently. By providing a standardized set of operations, AALI-C-App streamlines the communication and coordination between AAL Applications and the cloud platform.

The AAL Common API extends its support to AALI-C-App, offering a uniform approach for AAL Applications to interact with the O-Cloud infrastructure. This standardized interface enhances the flexibility and agility of RAN AAL Applications, contributing to the overall adaptability and performance optimization within the O-RAN architecture.
