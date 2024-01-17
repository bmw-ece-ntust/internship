# Part 4: Understand the Near-RT RIC OSC

- Goal : 
    - [ ] Install the Near-RT RIC Platform
    - [ ] Install xApp using DMS tool
    - [x] Mapping Near-RT RIC between specification and OSC
    - [x] Give Each Components a Introduction
    - [x] Be familiar with the platform operation 
- Useful Links : 
    - [Gerrit](https://gerrit.o-ran-sc.org/r/admin/repos)

- Outcome (Study Note) : 
    - Successfully installed the Near-RT RIC Platform
    - Successfully installed xApp using DMS Tool
    - Successfully mapping specification and OSC of Near-RT RIC
    - Learn about each components in Near-RT RIC

---

## I. Near-RT RIC Platform
The Near-RT RIC Platform operates as a software-based, near-real-time microservice platform, offering xApps the necessary infrastructure for managing a distributed array of RAN base stations (eNB, gNB, CU, DU) through the E2 protocol (southbound interface). Additionally, it serves as a mediator for the ==E2 interface== between xApps and RAN elements, as well as for the ==A1 and O1 interfaces== between xApps and the operator (northbound).

## II. Components
**A1 Mediator**: The A1 Mediator facilitates communication and interaction between xApps and the operator through the A1 interface. It ensures a smooth flow of policy-related information and updates.

**Demo1**: Demo1 is a demonstration xApp maintained by the RICP project. It serves as an illustrative example showcasing the capabilities and functionalities of xApps within the RIC environment.

**E2 Manager (E2M)**: The E2 Manager oversees and manages the E2 interface, facilitating communication between xApps and RAN elements (eNB, gNB, CU, DU). It plays a crucial role in maintaining connectivity and data exchange.

**E2 Terminator (E2T)**: The E2 Terminator manages the termination of the E2 interface from an E2 Node. It ensures proper communication cessation between the Near-RT RIC and external E2 elements.

**Influx-DB Wrapper**: The Influx-DB Wrapper acts as an intermediary layer facilitating communication between the Near-RT RIC platform and InfluxDB. It enables the storage and retrieval of time-series data, providing a streamlined interface for managing data within the platform.

**Logging (not tracing)**: Logging is responsible for capturing, recording, and storing system events, messages, or actions. It provides a valuable resource for monitoring, debugging, and evaluating the system's performance.

**O1 Mediator**: The O1 Mediator serves as a mediator for the O1 interface, facilitating communication and coordination between xApps and the Service Management & Orchestration layer. It plays a crucial role in ensuring effective data exchange and interoperability.

**RIC Alarm System**: The RIC Alarm System is designed to detect and notify relevant parties about system alarms or irregularities. It plays a critical role in maintaining system health and reliability.

**RIC Message Router (RMR)**: RIC Message Router acts as a core component for routing messages within the RIC ecosystem. It ensures efficient and reliable communication between different components.

**RNIB (Radio-Network Information Base)**: RNIB serves as a database for storing and managing radio access network-related information. It holds data crucial for the effective operation of the RIC platform.

**Routing Manager**: The Routing Manager is responsible for managing the routing of messages and data within the RIC environment. It ensures that information is directed to the appropriate destinations.

**Subscription Manager**: The Subscription Manager is responsible for managing and coordinating subscriptions from different xApps. It ensures that data subscriptions are merged efficiently, and unified data distribution is provided to xApps, promoting synchronized communication and information flow.

**xApp Framework for CXX (xapp-frame-cpp)**: xApp Frameworks provide the foundational structure and tools for rapid development of RIC applications using C or C++.

**xApp Framework for Go (xapp-frame)**: xApp Frameworks provide the foundational structure and tools for rapid development of RIC applications using Golang.

**xApp Framework for Python (xapp-frame-py)**: xApp Frameworks provide the foundational structure and tools for rapid development of RIC applications using Python.

**xApp Framework for Rust (xapp-frame-rust)**: xApp Frameworks provide the foundational structure and tools for rapid development of RIC applications using Rust.

## III. Platform Repositories
The RICP (near-RT RIC platform) includes the following component repositories. The development of these components is managed via the RICP project.

Repository|Desciption|
|---|---|
|com/log|A thread-safe logging C API library with Mapped Diagnostics Context (MDC) support.|
|com/golog|Golang implementation of the common logging library   |
|com/pylog|Python implementation of the common logging library|
|ric-plt/a1|Terminating the northbound A1 interface. It is translating information received over A1 it into conrete actions that xApps must take to adpat their behavior accordingly and it sends back feedback on the implementation status of such actions.|
|ric-plt/appmgr|Provides a flexible and secure way for deploying and managing various RIC xApp applications in a Kubernetes environment.|
|ric-plt/dbaas|Adaptation of the single-instance Redis database|
|ric-plt/e2|The E2 termination component that actually establishes E2 SCTP connections (as requested by the E2 manager) and routes messages received/sent over E2 to/from RMR.|
|ric-plt/e2mgr|The E2 manager implementation. The E2 manager controls E2 connection establishment and provides REST APIs to manage these connections.|
|ric-plt/lib/rmr|RIC message routing - A library originally based on NNG (nano-messaging nxt generation) for low latency message routing. Starting from Bronze (Feb-2020) we replaced NNG with plain usage of TCP in that library (see RIC-49).|
|ric-plt/nodeb-rnib|R-NIB APIs/libraries to store and retrieve RAN configuration data, like a list of cells per gNB.|
|ric-plt/rtmgr|Routing Manager (ric-plt/rtmgr) is a basic RIC platform service, responsible for generating and distributing routing policies to xApps.|
|ric-plt/sdl|SDL (Shared data layer) data access libraris for Redis including Redis server-side modules allowing multi-key atomic operations and publish channels.|
|ric-plt/sdlgo|same as ric-plt/sdl, but for the Go language|
|ric-plt/sdlpy|same as ric-plt/sdl, but for python|
|ric-plt/submgr|Near-realtime RIC Platform Subscription Manager|
|ric-plt/jaegeradapter|This repository includes files needed for starting the Jaeger Agent in a side-car container, and also files needed for starting Jaeger all-in-one of full collector containers.|
|ric-plt/vespamgr|The VESPA manager uses the VES Agent (https://github.com/nokia/ONAP-VESPA) to adapt near-RT RIC internal statistics collection using Prometheus (xApps and platform containers) to ONAP's VES (VNF event streaming).|
|ric-plt/xapp-frame|Artifacts for the (near realtime) RIC xapp framework, including common libraries, etc|
|ric-plt/asn1-documents|ASN.1 definitions and related documents that are needed by other components|
|ric-plt/ric-test|This repo includes test cases that span the full RIC platform, i.e., that cannot run against a single RIC component.|
|ric-plt/ric-dep|Code and configuration files that are needed for deploying a near-RT RIC platform instance|
|ric-plt/o1|o1 mediator|
|ric-plt/xapp-frame-py|The near-RT RIC python xapp framework|
|ric-plt/xapp-frame-cpp|The near-RT RIC C++ xapp framework|
|ric-plt/alarm-go|The near-RT RIC alarm adapter and Go library|
|ric-plt/alarm-cpp|The near-RT RIC alarm library for C++|
|ric-plt/libe2app|The near-RT RIC E2AP library|
|ric-plt/ricctl|The CLI (Command line interface) for the near-RT RIC platform|
|ric-plt/ricdms|The DMS (Deployment management services) implementation for RIC xApps|
|ric-plt/stslgo|The STSL (shared metrics layer) libraries provide access to the time series databases. The interface is optimized for time-series database interfaces. Initially it supports InfluxDB. This repo is for the go version of it.|
|ric-plt/xapp-frame-rust|The near-RT RIC Rust xapp framework|
