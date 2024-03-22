# Introduction

Near-RT RIC (Near-Real-Time RAN Intelligent Controller) is a logical function playing a crucial role in enabling near-real-time control and optimization of Radio Access Network (RAN) elements and resources. It achieves this by performing fine-grained data collection and executing actions over the E2 interface.

Essentially, Near-RT RIC enhances the efficiency and responsiveness of RAN operations. While Non-RT RIC (Non-Real-Time RAN Intelligent Controller), within the Service Management and Orchestration (SMO) framework, serves a different purpose. It acts as a logical function responsible for managing the content exchanged across the A1 interface. The Non-RT RIC consists of two key components: the Non-RT RIC Framework and the Non-RT RIC Applications.

These also exists xApp (Extended Application), an application specifically designed to run on the Near-RT RIC platform. It can be composed of one or more microservices. During the onboarding process, an xApp specifies the data it consumes and provides. Importantly, xApps are independent of the Near-RT RIC itself and can be developed by third-party entities. The E2 interface establishes a direct link between an xApp and the underlying RAN functionalities.

# More about its functions...

![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/ff23c1ab-fb3e-4e8e-9f86-8d5b0def608d)

A. Database and Related SDL (Shared Data Layer) Services enables both reading and writing of critical information related to Radio Access Network (RAN) and User Equipment (UE). It also supports other data necessary for specific use cases. Essentially, it acts as a bridge between applications and the underlying data storage.
1. UE-NIB (User Equipment Network Information Base) serves as a repository for essential network-related information specific to individual user equipment. It contains details about the UE’s connection status, capabilities, and other relevant data.
2. R-NIB (Radio Network Information Base) is responsible for storing and managing network-related information at the radio access level. It includes data about cell configurations, neighboring cells, and radio resources.
3. SDL (Shared Data Layer): performs several key functions, utilizied by xApps; subscribing to database notification services (xApps can receive real-time updates when relevant data changes in the database), reading data (xApps retrieve information from the stored data), writing and modifying data (xApps can update or modify data stored in the database). The SDL plays a crucial role in facilitating communication between xApps and the underlying database, allowing them to efficiently access and manipulate relevant information.

B. xApp Subscription Management consolidates subscriptions from various xApps. It ensures unified data distribution to all xApps, allowing them to receive relevant updates efficiently.

C. Conflict Mitigation handles potential conflicts arising from multiple xApps making requests. There are several types of Conflicts; direct conflicts are mitigated through pre-action coordination, ensuring that conflicting actions do not occur simultaneously; indirect conflicts are resolved post-action by verifying that actions do not overlap or contradict each other, and implicit conflicts are those that are challenging to mitigate directly. However, ensuring that different use cases (xApps) target distinct parameters can help minimize implicit conflicts.

D. Messaging Infrastructure provides a low-latency message delivery service within the Near-RT RIC’s internal endpoints to make an efficient communication between components, facilitating timely data exchange.

E. Security components safeguard xApps, preventing malicious xApps from abusing radio network information, ensuring data integrity and confidentiality, and executing authentication and authorization mechanisms to control access.

F. Management Function/OAM (Operations, Administrations, and Management) Management acts as a service producer to the Service Management and Orchestration (SMO) system. These below are services that are provided:
1. Fault Management detects and handles faults within the Near-RT RIC ecosystem. It ensures timely responses to any anomalies.
2. Configuration Management manages configuration settings for optimal system performance. This includes adjusting parameters, policies, and profiles.
3. Performance Management monitors and assesses system performance metrics. It tracks resource utilization, responsiveness, and overall efficiency.
4. Logging, Tracing, and Metrics Collection: These functionalities capture, monitor, and collect internal status information from Near-RT RIC. The collected data can be transferred to external systems for further analysis and evaluation.

G. Interface Termination are responsible for terminating specific interfaces within the Near-RT RIC architecture. There are several types of interface termination; E2 Termination (terminates the E2 interface from an E2 Node, facilitates communication between different RAN elements), A1 Termination (terminates the A1 interface from the Non-RT RIC, the A1 interface is crucial for exchanging information related to RAN configuration and policies), and O1 Termination (terminates the O1 interface from the SMO, the O1 interface handles orchestration-related communication, including service requests and responses).

H. Functions hosted by xApps allow services to be executed within the Near-RT RIC, with outcomes sent to E2 Nodes via the E2 interface.
1. API Enablement Function supports capabilities related to Near-RT RIC API operations, including API repository/registry, authentication, discovery, and generic event subscription.
2. AI/ML Support provides data pipelining, training, and performance monitoring for xApps leveraging artificial intelligence and machine learning.
3. xApp Repository Function selects xApps for A1 message routing based on A1 policy types and operator policies and also controls access to A1-EI types for xApps based on operator policies.
4. xApps collaborates  with the Near-RT RIC platform functions to support various specialized use cases. Upon registration, an xApp provides OAM and control information to enable relevant functionalities.

# APIs!

![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/80a7f747-ac6b-4460-af3a-1e2b8714eb9f)

Near-RT RIC APIs are designed to support xApp development in multiple programming languages such as C, C++, Python, and Go. Near-RT RIC APIs empower xApp developers to create customized applications, enhance mobility management, optimize radio connections, manage quality of service, and handle interference—all while benefiting from the agility and scalability of cloud-based solutions.

Key Functions:
1. xApp Subscription Management is facilitated based on operators’ policies. An xApp can be restricted to interface with only a subset of E2 Nodes based on these policies.
2. Low Latency Network since NEAR-RT RIC requires rapid  access to the network. This is enabled by AWS Outposts, which provides a fully-managed service offering the same AWS infrastructure, services, APIs, and tools at edge locations.

The implementation can be done using two different types of approaches:

![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/09b1fed2-65e9-4bb1-a993-1e380331ba59)

1. Network API Approach, so that the Near-RT RIC APIs can be implemented directly through network endpoints. Each relevant Near-RT RIC endpoint exposes a specific network endpoint. It specifies both the data encoding protocol (e.g., JSON, XML) and the network transport protocol (e.g., HTTP, WebSocket) to be used for communication. xApps can directly interact with these endpoints, allowing fine-grained control and customization. This gives direct access to specific functionalities and the flexibility in choosing communication protocols.

![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/f22f3e2e-1b90-4cff-90e5-5b83b5bc48f1)

2. SDK (Software Development Kit) Approach, so that the Near-RT RIC vendor provides an SDK—a software library that simplifies xApp development. The SDK handles connection management, abstracting the complexities of network communication. It exposes a straightforward API for xApps to interact with the Near-RT RIC. Developers can focus on application logic rather than low-level networking details. The benefits come from a streamlined development process and a consistent, reliable communication.

Both approaches empower xApp developers to seamlessly integrate with Near-RT RIC, whether through direct network APIs or via the convenience of an SDK. Regarding that, the approaches to Near-RT RIC API are not necessarily mutually exclusive. And to delve into the specifics of each approach:
1. A1 Related APIs offer value-added services based on policies or enrichment information (or both). These policies and enrichment data are transferred through the A1 interface by Non-RT RIC (Radio Intelligent Controller).
2. E2 Related APIs provide value-added services using RIC functional mechanisms. These services are delivered via the E2 interface toward E2 Nodes. The E2 related APIs grant access to E2-related functionality, including xApp Subscription Management and Conflict Mitigation features.
3. Management APIs encompasses the xApp’s ML Model related APIs and the FCAPS (Fault, Configuration, Accounting, Performance, Security) related APIs.
4. SDL APIs offer a straightforward yet flexible way to store and retrieve data. They abstract details such as database type and location, as well as management operations (e.g., high availability, scaling, load balancing) within the database layer. SDL APIs support defined data structures used to provide E2 Node-related information.
5. Enablement APIs facilitate the exchange of API enablement-related information between xApps and the API enablement functionality.

# How to use them, though?

Below written the guidance regarding the procedure:
1. A1-related API procedures are essential for A1-related functionality within the Near-RT RIC ecosystem, and to break down the A1 Policy procedures and A1-EI (Enrichment Information) procedures:
   1. A1 Policy Procedures
        1. Setup: Establishing initial policies.
        2. Update: Modifying existing policies.
        3. Delete: Removing policies.
        4. Query: Retrieving policy information.
        5. Status Update: Reporting changes in policy status.
   2. A1-EI Procedures
        1. Query: Obtaining enrichment information.
        2. Subscription Setup: Configuring subscriptions for enrichment data.
        3. Subscription Update: Modifying existing subscriptions.
        4. Subscription Delete: Removing enrichment subscriptions.
        5. Delivery: Receiving and handling enrichment data.
2. E2-related API procedures are relevant to E2-related functionality within Near-RT RIC, and to break down the specifics of RIC Functional Procedures and E2 Guidance Related Procedures:
    1. RIC Functional Procedures:
        1. E2 Subscription API: Managing E2 subscriptions.
        2. E2 Subscription Delete (initiated by an xApp): Removing E2 subscriptions.
        3. E2 Subscription Delete Query and E2 Subscription Notification Procedures: Handling queries related to subscription deletion and notifications.
        4. E2 Indication: Receiving indications from E2.
        5. E2 Control: Exercising control over E2 functions.
    2. E2 Guidance Related Procedures allow authorized xApps to seek guidance from the Conflict Mitigation platform function before taking action:
        1. xApp-initiated E2 guidance request/response procedure
        2. Modification API:
        3. xApp Subscription Management initiated
        4. Message monitoring initiated
        5. Conflict Mitigation initiated
3. Management API procedures pertain to xApp management within the Near-RT RIC environment: xApp Registration (enrolling xApps), xApp Deregistration (removing xApps), xApp Configuration (adjusting xApp settings).
4. SDL API procedures facilitate data storage and retrieval, the notable use cases for SDL APIs involve E2NodeInfo and E2NodeList: SDL Client Registration, SDL Client Deregistration, Fetch Data, Subscribe/Notify, Store Data, Modify Data, Subscribe/Push.
5. API Enablement procedures relate to the discovery and subscription of Near-RT RIC APIs, whereas including the Near-RT RIC API Discovery procedure and API Event Subscription and Notification.
