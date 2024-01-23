# Part 1: General Aspects and Principles
- Goal : 
    - [x] To know the general aspects of O-RAN WG6
    - [x] To know the principles of O-RAN WG6

- Outcome (Study Note) : 
    - Learn about the general aspects of O-RAN WG6
    - Learn about HWA and AAL principles and requirements
    - Learn about AAL-LPU Principles
    - Learn about AAL Profiles

***

## I. General Aspects
### A. Hardware Acceleration (HWA)
Hardware acceleration involves **optimizing the performance of computing systems** by implementing specific functions in specialized hardware, balancing flexibility and efficiency. This can range from using general-purpose processors like CPUs to more specialized options like GPUs, FPGAs, and ASICs. 

A hardware accelerator is a specialized implementation that **offloads processing** from a General-Purpose Processor, **enhancing efficiency**. The implementation can occur purely in software, hardware accelerator, or a combination of both. Hardware acceleration can be lookaside or inline, where the former involves the host CPU invoking an accelerator, while the latter directly transfers processed data to a destination node. 

This model, illustrated in Figure 1-1, allows **parallel execution** of software tasks while offloading workload to a hardware accelerator, improving application performance in compute-intensive, deeply pipelined operations. The API supporting this model requires operations for initiating offload and retrieving the completed operation.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/Bkl8rOiKT.png"/>
  <figcaption><strong>Figure 1-1</strong>: Example illustration of the effect of hardware acceleration on functional compute performance</figcaption>
</figure>

### B. AAL Architecture
The Acceleration Abstraction Layer (AAL) aims to **define a consistent interface** for Hardware Accelerators (HW) **to interact with AAL Applications**, enabling the decoupling of specific AAL Applications from particular HW implementations. To address diverse combinations of HW and SW implementations and network scenarios, AAL introduces the concept of an AAL profile, distinguishing between various offloaded accelerated functions. Figure 1-2 illustrates the high-level AAL architecture block diagram, while Figure 1-3 provides a visual representation of the entity relationships and cardinality within the AAL architecture. It serves to aid conceptualization rather than forming the basis for a class diagram or object model.

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/SyxnDOota.png"/>
  <figcaption><strong>Figure 1-2</strong>: High Level AAL Architecture Diagram
</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/rysAwujY6.png"/>
  <figcaption><strong>Figure 1-3</strong>: AAL Resource Relationship and Cardinality
</figure>
    
### C. AAL Interfaces, Specification, and Scope
The AAL interface API has two distinct parts, the first part corresponds to a set of common APIs (**AALI-C**) to address all the profile independent aspects of the underlying AAL Implementation(s) within an O-Cloud platform.
The second part of AAL interface corresponds to a set of AAL profile specific APIs (**AALI-P**) which is specific to each defined AAL profile.

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/B1kiztsKT.png"/>
  <figcaption><strong>Figure 1-4</strong>: AAL Application Common and profile APIs
</figure>    

The AAL specifications define the AAL interface and the AAL profiles that may be supported by that interface. The AAL-C-Application interface is used by AAL Application to access the AAL Implementation encompassing HW Accelerator and associated SW libraries, drivers etc. In Figure 1-5 two deployment scenarios are shown, one with Containers and the other with Virtual Machines.
    
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/S1wXQKiY6.png"/>
  <figcaption><strong>Figure 1-5</strong>: Accelerator APIs/Libraries in Container and Virtual Machine Implementations
</figure>

The AAL specification aims to enable **a "cloudified" RAN**, characterized by deploying various software implementations from different vendors on a shared CPU-based platform with hardware accelerators. This allows flexibility in both software and hardware configurations, supporting centralized or distributed deployment scenarios. 
In a disaggregated and cloudified multi-vendor RAN, **common vendor-neutral APIs** are crucial. These APIs facilitate managed element discovery, lifecycle management, FM/PM, and orchestration across both Physical Network Functions (PNFs) and Virtual Network Functions (VNFs). This ensures the cohesive functioning of the RAN, supporting key lifecycle use cases such as scale-out, slice management, fault tolerance, and hitless software upgrades.

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:40%;" src="https://hackmd.io/_uploads/BkqPutsFT.png"/>
  <figcaption><strong>Figure 1-6</strong>: AAL Specification Scope
</figure>

## II. General Principles and Requirements
### A. General Principles
The set of **generic and profile-specific features of the AAL interface** described in the following subsections are defined from an AAL Application point of view.
    
* **Extensibility**: AAL Application Interface shall be `extensible` for future revisions of the specification.
* **HW Independence**: AAL Application Interface shall be `independent` of the underlying AAL Implementation.
* **Interrupt and Poll Mode**: AAL Application Interface shall `support both` interrupt mode, poll mode, and any combination with interrupt and poll mode
* **Discovery and Configuration**: AAL Application Interface shall enable AAL Application to `discover and configure AAL-LPU(s)`.
* **Multiple AAL-LPU Support**: AAL Application Interface shall support multiple AAL-LPU(s) at the same time.
* AAL Offload Capabilities: AAL Application Interface shall `support different offload architectures` including look-aside, inline, and any combination of both.
* **Look-aside Acceleration Model**: the AAL Application invokes a HW Accelerator for data processing and receives the result after processing is complete.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:20%;" src="https://hackmd.io/_uploads/H1ILLcjta.png"/>
  <figcaption><strong>Figure 2-1</strong>: AAL Application interface look-aside acceleration model - Data flow
</figure>
    
* **Inline Accerelation Model**: the AAL Application, after invoking a HW Accelerator for offloading AF(s) specified by AAL profile(s), does not necessarily retrieve the post processed data.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:20%;" src="https://hackmd.io/_uploads/SJ_R85st6.png"/>
  <figcaption><strong>Figure 2-2</strong>: AAL Application interface inline acceleration model - Data flow
</figure>

* **AAL Application Interface Concurrency and Parallelism**: AAL Application interface shall support `multi-threading` environment allowing an AAL Application to offload acceleration requests in parallel from several threads.
* **Separation of Control and User Plane AAL Application interface APIs**: AAL Application interface shall support `separation of control and user plane APIs` with appropriate identifiers, as required by different AAL profiles.
* **Support of Versatile Acceleration Payload**: AAL Application interface API shall be `flexible` to support various ranges of payload sizes as required by different AAL profiles.
* **Support of Different Transport Mechanisms**: AAL Application interface shall support `abstraction` of these various transport mechanisms between the AAL Application and the AAL Implementation.
* **AAL API namespace**: AAL shall follow a unique name space for all AAL API functions.
* **Chaining of AAL Profiles**: 
Chaining AAL Profiles enables `specifying and executing multiple AFs` in a designated order, enhancing efficiency by redirecting output from one profile to another without AAL Application intervention. This reduces transfer latencies and can be applied to the same or different LPUs and HWAs. Currently, the specification focuses on single AAL-LPU chaining. It's optional and depends on AAL Application requests during CNF or VNF deployment. Chained profiles must conform to AAL Application specifications, and validity requires a correct sequence without intervention. This applies to both inline and look-aside acceleration, with illustrated data flows in Figures 2-3 and 2-4.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/Hk3VK9sKp.png"/>
  <figcaption><strong>Figure 2-3</strong> : Dataflow through chained lookaside HW Accelerator for consecutive Hi-PHY functions
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/HkJtKcoK6.png"/>
  <figcaption><strong>Figure 2-4</strong> : Dataflow through chained lookaside HW Accelerator for consecutive and non-consecutive PHY
</figure>

### B. High-PHY Profile Specific Principles
The set of **features of AAL** described in the following subsections are relevant for inline High-PHY AAL profiles (profile names with suffix ‘_HIGH-PHY’) 

* **Separation of Cell and Slot Level Parameter Configurations**: AAL Application Interface shall support `configuration of “cell-specific” and “slot-specific” parameters` to the AAL Implementation using separate AAL Application interface API functions.
* **SFN/slot-based Synchronization**: AAL Application interface shall support `system frame number (SFN) based or slot-based synchronization` between the AAL Application and the AAL Implementation supporting inline, high-PHY AAL profiles.
* **Compatibility with O-RAN FH Interface**: AAL Application interface API shall be `compatible with O-RAN FH interface (7.2-x split)` to enable communication between the O-DU AAL Application and O-RU via AAL Implementation as required by inline, High-PHY AAL profile(s).
* **Inline Profile for High-PHY Stack**: The set of Accelerated Functions that are offloaded in Inline mode for acceleration of a partial High-PHY stack would be AAL Profile specific. The support of AAL Profiles that specify the support of partial High-PHY stack is for future study.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:90%;" src="https://hackmd.io/_uploads/BkfY55iYp.png"/>
  <figcaption><strong>Figure 2-5</strong> : Partial Inline Model for AAL Hi-PHY Profile
</figure>

## III. AAL-LPU Principles
1. **The AAL-LPU is responsible for executing the AAL profile(s) assigned to it**: The AAL-LPU is a logical representation of resources within an instance of a HW Accelerator. It maps to a single HW Accelerator and executes the AAL profile(s) assigned to it. The AAL-LPU is responsible for processing the workload building blocks (Accelerated Functions) on behalf of the AAL Application within an O-RAN Cloudified Network Function.

2. **The AAL-LPU shall support the AAL Application interface**: The AAL-LPU supports the AAL Application interface, which enables AAL Applications to discover and configure AAL-LPU(s). The AAL Application interface allows an AAL Application to discover what physical resources have been assigned to it and then to configure said resources for offload operations.

3. **The AAL-LPU shall support statistics, memory management, and run-time configurations**: The AAL-LPU supports statistics, memory management, and run-time configurations to ensure efficient utilization and allocation of resources for AAL Profiles and AAL Applications. The AAL-LPU provides support for monitoring and reporting performance metrics related to its operations.

4. **The AAL-LPU shall support AAL Profile(s) offload, processing status query, and processed data retrieval**: The AAL-LPU supports AAL Profile(s) offload, processing status query, and processed data retrieval. It is responsible for offloading AAL Profiles, querying processing status, and retrieving processed data. The AAL-LPU executes and manages accelerated functions on behalf of the AAL Application.

5. **The AAL-LPU shall expose its capabilities to the HW Accelerator Manager**: The AAL-LPU exposes its capabilities to the HW Accelerator Manager, which is responsible for creating the AAL-LPU(s) and the profiles supported. The AAL-LPU and its profile(s) are exposed to the AAL Application in an abstracted descriptor to achieve AAL Application portability. The AAL-LPU communicates and interacts with the HW Accelerator Manager to ensure effective management of resources.
