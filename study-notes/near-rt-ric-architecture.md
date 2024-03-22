# Introduction

Near-RT RIC (Near-Real-Time RAN Intelligent Controller) is a logical function playing a crucial role in enabling near-real-time control and optimization of Radio Access Network (RAN) elements and resources. It achieves this by performing fine-grained data collection and executing actions over the E2 interface. Essentially, Near-RT RIC enhances the efficiency and responsiveness of RAN operations. While Non-RT RIC (Non-Real-Time RAN Intelligent Controller), within the Service Management and Orchestration (SMO) framework, serves a different purpose. It acts as a logical function responsible for managing the content exchanged across the A1 interface. The Non-RT RIC consists of two key components: the Non-RT RIC Framework and the Non-RT RIC Applications. These also exists xApp (Extended Application), an application specifically designed to run on the Near-RT RIC platform. It can be composed of one or more microservices. During the onboarding process, an xApp specifies the data it consumes and provides. Importantly, xApps are independent of the Near-RT RIC itself and can be developed by third-party entities. The E2 interface establishes a direct link between an xApp and the underlying RAN functionalities.

# More About Its Functions...

A. Database and Related SDL (Shared Data Layer) Services enables both reading and writing of critical information related to Radio Access Network (RAN) and User Equipment (UE). It also supports other data necessary for specific use cases. Essentially, it acts as a bridge between applications and the underlying data storage.

A.1. UE-NIB (User Equipment Network Information Base) serves as a repository for essential network-related information specific to individual user equipment. It contains details about the UE’s connection status, capabilities, and other relevant data.

A.2. R-NIB (Radio Network Information Base) is responsible for storing and managing network-related information at the radio access level. It includes data about cell configurations, neighboring cells, and radio resources.

A.3. SDL (Shared Data Layer): performs several key functions, utilizied by xApps; subscribing to database notification services (xApps can receive real-time updates when relevant data changes in the database), reading data (xApps retrieve information from the stored data), writing and modifying data (xApps can update or modify data stored in the database). The SDL plays a crucial role in facilitating communication between xApps and the underlying database, allowing them to efficiently access and manipulate relevant information.

B. xApp Subscription Management consolidates subscriptions from various xApps. It ensures unified data distribution to all xApps, allowing them to receive relevant updates efficiently.

C. Conflict Mitigation handles potential conflicts arising from multiple xApps making requests. There are several types of Conflicts; direct conflicts are mitigated through pre-action coordination, ensuring that conflicting actions do not occur simultaneously; indirect conflicts are resolved post-action by verifying that actions do not overlap or contradict each other, and implicit conflicts are those that are challenging to mitigate directly. However, ensuring that different use cases (xApps) target distinct parameters can help minimize implicit conflicts.

D. Messaging Infrastructure provides a low-latency message delivery service within the Near-RT RIC’s internal endpoints to make an efficient communication between components, facilitating timely data exchange.

E. Security components safeguard xApps, preventing malicious xApps from abusing radio network information, ensuring data integrity and confidentiality, and executing authentication and authorization mechanisms to control access.

F. Management Function/OAM (Operations, Administrations, and Management) Management acts as a service producer to the Service Management and Orchestration (SMO) system. These below are services that are provided:

F.1. Fault Management detects and handles faults within the Near-RT RIC ecosystem. It ensures timely responses to any anomalies.

F.2. Configuration Management manages configuration settings for optimal system performance. This includes adjusting parameters, policies, and profiles.

F.3. Performance Management monitors and assesses system performance metrics. It tracks resource utilization, responsiveness, and overall efficiency.

F.4. Logging, Tracing, and Metrics Collection: These functionalities capture, monitor, and collect internal status information from Near-RT RIC. The collected data can be transferred to external systems for further analysis and evaluation.

G. Interface Termination are responsible for terminating specific interfaces within the Near-RT RIC architecture. There are several types of interface termination; E2 Termination (terminates the E2 interface from an E2 Node, facilitates communication between different RAN elements), A1 Termination (terminates the A1 interface from the Non-RT RIC, the A1 interface is crucial for exchanging information related to RAN configuration and policies), and O1 Termination (terminates the O1 interface from the SMO, the O1 interface handles orchestration-related communication, including service requests and responses).

H. Functions hosted by xApps allow services to be executed within the Near-RT RIC, with outcomes sent to E2 Nodes via the E2 interface.

H.1.  API Enablement Function supports capabilities related to Near-RT RIC API operations, including API repository/registry, authentication, discovery, and generic event subscription.

H.2.  AI/ML Support provides data pipelining, training, and performance monitoring for xApps leveraging artificial intelligence and machine learning.

H.3. xApp Repository Function selects xApps for A1 message routing based on A1 policy types and operator policies and also controls access to A1-EI types for xApps based on operator policies.

H.4. xApps collaborates  with the Near-RT RIC platform functions to support various specialized use cases. Upon registration, an xApp provides OAM and control information to enable relevant functionalities.

# APIs!

Near-RT RIC APIs are designed to support xApp development in multiple programming languages such as C, C++, Python, and Go. Near-RT RIC APIs empower xApp developers to create customized applications, enhance mobility management, optimize radio connections, manage quality of service, and handle interference—all while benefiting from the agility and scalability of cloud-based solutions.

Key Functions:
1. xApp Subscription Management: Near-RT RIC APIs facilitate xApps’ subscription management based on operators’ policies. An xApp can be restricted to interface with only a subset of E2 Nodes based on these policies.
2. Low Latency Access to the Network: Near-RT RIC requires rapid, low-latency access to the network. This is enabled by AWS Outposts, which provides a fully-managed service offering the same AWS infrastructure, services, APIs, and tools at edge locations.
