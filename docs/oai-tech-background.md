# TEEP: 5GC & ORAN Docs

[TOC]

## 5G Core in Network

### Introduction

**What is 5G Core and why is 5G Core important?**

By definition 5G core is a core network architecture that implements the new 3GPP network architecture for 5G mobile networks. It is the heart of the 5G mobile network. 5G Core is important because it establishes a reliable, secure connectivity to the network for end users and provides access to its services.

5G core is designed to handle a wide variety of essential functions such as connectivity and mobility management, authentication and authorization, subscriber data management and policy management, etc. These network functions are designed as cloud-native and software-based which allow for a higher deployment flexibility and agility on multiple cloud infrastructures.


### Architecture

**General Architecture**

![image alt](https://hackmd.io/_uploads/B15R6GBta.png)

5G core architecture is based on a service-based architecture (SBA) where each network function (NF) offers one or more services to other NF’s via application programming interfaces (APIs).



![BkEjhrt_a](https://hackmd.io/_uploads/B19AwMU5T.png)

**Network Functions**

* **5G-EIR (5G Equipment Identity Register)**

    5G-EIR is an optional network functions that allows to check the Permanent Equipment Identifier (PEI) and check whether the PEI is in the prohibited list or not. This network function helps to prevent the use of stolen or unauthorized devices in the network.
    

* **AF (Application Function)**

    AF is a network function that interacts with the 3GPP Core Network in order to provides application-specific services or policies such as traffic routing, QoS or time synchronization.
    
    
* **AMF (Access and Mobility Management Function)**

    AMF is a network function that handles the registration, termination, authentication, mobility, and reachability of the UE. This network function interacts with the session management function (SMF), Unified Data Management (UDM), Authentication Server Function (AUSF), and Network Slice Selection Function (NSSF).
    
    
* **AUSF (Authentication Server Function)**

    AUSF is a network function that performs the authentication and authorization of the UE and the network. When a subscriber attempts to connect to the 5G network, the AUSF plays a key role in verifying their identity and ensuring that they have the proper authorization to access the network.
    
    
* **CHF (Charging Function)**

    CHF is a network functions that monitors charging data, subscriber usage consumption and policy counter, and together with Policy Control Function (PCF), it provides policy and charging control during service delivery.
    
    
* **GMLC (Gateway Mobile Location Centre)**

    GMLC is a network function that provides the location information of the UE to authorzied entities such as emergencys services. GMLC is the first node an external LCS client accesses in a PLMN. GMLC interacts withe the UDM via the Nudm interface to request routing information and/or target UE privacy information. After verifying the target UE privacy, the GMLC can now forward a location request to either a serving AMF using Namf interface or to a GMLC in another PLMN using the Ngmlc interface in the case of a roaming UE. GMLC interacts with the NEF and the LMF.
    
    
* **LMF (Location Management Function)**

    LMF is a network function that provides and calculates the location information of the UE based on network topology and radio measurements. LMF interacts with the GMLC and the AMF.
    
    
* **DN (Data Network)**

    DN is a network function that allows access to the internet or other external networks for the UE. It interacts with the UPF and SMF.
    

* **NEF (Network Exposure Function)**

    NEF is a network function that exposes the network services and capabilities to an external application and devices such as third-party service providers. It interacts with the AF, PCF, NRF, UDM, and GMLC.
    

* **NRF (NF Repository Function)**

    NRF is network function that maintains the information and status of all the network functions in the 5GC. This network function provides the load balancing function and service discovery. NRF interacts th all network functions.
    

* **NSSF (Network Slice Selection Function)**

    NSSF is a network function that select and handles the approriate network slice for each UE. Network slice is a logical network that has customized services and resources for specific user group or use case.
    

* **PCF (Policy Control Function)**

    PCF is a network function that handles the policy rules and charging information fo each session and service. This network function controls and monitor the QoS and the subscription usage of the network resources. It interacts with SMF, AF, NEF, UDM, and NSSF.

* **SMF (Session Management Function)**

    SMF is a network function that establishes, releases, and modifies sessions between UE and the Data Network (DN). It interacts with the AMF, UPF, PCF, NSSF, and DN.
    

* **UDM (Unified Data Management)**

    UDM is a network function that handles the subscriber data such as subscription profiles, authentication credentials, and access authorization information. It interacts with the AMF, AUSF, PCF, NSSF, and NEF.
    


* **UDR (User Data Repository)**

    UDR is a network function that maintains the subscriber data for the UDM and other network functions. It interacts with the UDM and NEF.


* **UPF (User Plane Function)**

    UPF is a network function that forwards the user data packets and applies the policies and rules for each session. It interacts with SMF, RAN, and DN.

### 5G Interfaces

**General Interface**

![image alt](https://hackmd.io/_uploads/rJb8b_iOa.png)

As shown from the image above NG-RAn is composed of gNBs (5G Base Stations) and ng-eNB (LTE Base Stations).

* NG interfaces exists between 5G core and base stations (NG-RAN)
* Xn interfaces exists between base stations such as between gNB-gNB, gNB-(ng-eNB), or (ng-eNB)-(ng-eNB). Xn is the network interface between NG-RAN nodes. Xn is divided into two parts which are Xn-U and Xn-C. Xn-U stands for Xn User Plane interface and Xn-C stands for Xn Control Plane Interface.

5G NR interfaces includes:
* Xn interface
* NG interface
* E1 interface
* F1 interface
* F2 interface.

**5G NR Xn Interface**
* Location : Exist between base stations or NG-RAN nodes i.e. gNB or ng-eNB.
* Xn-U (User Plane Function):
    * Flow Control
    * Data Forwarding
* Xn-C (Control Plane Function)
    * Interface management and error handling
    * Connected mode mobility management such as handover procedures, sequence number status transfer, UE context retrieval
    * Dual connectivity functions such as reconfiguration, secondary node addition, release
    * Support of RAN paging

**5G NR NG Interface**
* Location : Location : Exist between NG-RAN and 5GC
* Objective:
    * Exchange signal information between NG-RAN and 5GC
    * Defines the inter connection of NG-RAn nodes with AMFs supplied by different manufacturers
    * It seperates NG interface Radio Network functionality and the Transport Network functionality to facilitate introduction of future technologies
* Function:
    * Able to eshtablish, maintain, and release NG-RAN part of PDU sessions
    * Transfer NAS signal messages between UE and AMF
    * Able to perform intra-RAT handover and inter-RAT handover
    * Having a mechanisms for resource reservation for packet data streams

**5G NR E1 Interface**
* Location : Point-to-point interface between gNB-CU-CP and gNB-CU-UP
* Function:
    * Support exchange signal information between ednpoints
    * Seperates Transport Network Layer and Radio Network Layer
    * Exchange UE and non-UE associated information

**5G NR F1 Interface**
* Location : Exist between base stations or NG-RAN nodes i.e. gNB or ng-eNB.
* Xn-U (User Plane Function):
    * Flow Control
    * Data Forwarding
* Xn-C (Control Plane Function)
    * Interface management and error handling
    * Connected mode mobility management such as handover procedures, sequence number status transfer, UE context retrieval
    * Dual connectivity functions such as reconfiguration, secondary node addition, release
    * Support of RAN paging

**5G NR Xn Interface**
* Definition: F1 interface is separated into F1-C and F1-U based on the control plane and user plane functionalities
* Location : Between gNB-CU and gNB-DU.
* Funtion:
    * Defines the inter-connection between gNB-CU and gNB-DU
    * Seperates Transport Network Layer and Radio Network Layer
    * Exchange UE and non-UE associated information

**5G NR F2 Interface**
* Definition : F2 interface is separated into F2-C and F2-U based on the control plane and user plane functionalities
* Location: Between lower and upper parts of 5G NR PHY layer.

### 5G Registration Procedure

**5G NR Xn Interface**
* Definition: F1 interface is separated into F1-C and F1-U based on the control plane and user plane functionalities
* Location : Between gNB-CU and gNB-DU.
* Funtion:
    * Defines the inter-connection between gNB-CU and gNB-DU
    * Seperates Transport Network Layer and Radio Network Layer
    * Exchange UE and non-UE associated information

> ON PROGRESS

## Install Free5GC & UERANSIM

### General Information
**VM Core Spesification** 

![image](https://hackmd.io/_uploads/H1E1dUMc6.png)

**VM UERANSIM Spesification** 

![image](https://hackmd.io/_uploads/BybbO8GqT.png)


### Technical Information
1. Install [Go](https://go.dev/doc/install)

    ![image](https://hackmd.io/_uploads/BJdPPrz5a.png)

    ![image](https://hackmd.io/_uploads/Skg9wrfca.png)

    ![image](https://hackmd.io/_uploads/Skb0DBf9p.png)

2. Install [MongoDB](https://www.cherryservers.com/blog/install-mongodb-ubuntu-22-04)

    ![image](https://hackmd.io/_uploads/Sk6XcBz9T.png)

    ![image](https://hackmd.io/_uploads/HkId9BfqT.png)

    ![image](https://hackmd.io/_uploads/Hkx29Hfqp.png)

3. Install Userplane Support Package

    ![image](https://hackmd.io/_uploads/Syrzsrfca.png)

4. Config Network on Host

    ![image](https://hackmd.io/_uploads/rJb7AHz9p.png)

    ![image](https://hackmd.io/_uploads/rkSSASMqp.png)


5. Install Free5Gc


    **Install the Control Plane Elements**
    ![image](https://hackmd.io/_uploads/SJr_RSGqa.png)

    ![image](https://hackmd.io/_uploads/SkljABfqT.png)

    **Install the User Plane Elements**

    ![image](https://hackmd.io/_uploads/rkUgkLfq6.png)

    ![image](https://hackmd.io/_uploads/HJcZkIG5p.png)

6. Install web console

    ![image](https://hackmd.io/_uploads/S1pr1UM9p.png)

    ![image](https://hackmd.io/_uploads/H1EI1Lfca.png)

    ![image](https://hackmd.io/_uploads/rkNtyLz56.png)

    ![image](https://hackmd.io/_uploads/HJzo1Lfcp.png)

    ![image](https://hackmd.io/_uploads/By9zgLzcT.png)

**Accessing GUI**
    ![image](https://hackmd.io/_uploads/S1tvBIGq6.png)
    ![image](https://hackmd.io/_uploads/ByEYBIzq6.png)


7. Install UERANSIM

    ![image](https://hackmd.io/_uploads/HJQ64Iz5a.png)

    ![image](https://hackmd.io/_uploads/r141rIfcT.png)

    ![image](https://hackmd.io/_uploads/BJ9gLLzca.png)

    ![image](https://hackmd.io/_uploads/HkN8wUf9p.png)

## Testing of 5G Core (E2E test)

> ON PROGRESS..

## O-RAN in 5G Network

### Definition

    O-RAN stands for Open Radio Access Network, which is a new paradigm for designing, deploying, and operating cellular networks. O-RAN networks are built with disaggregated components that are connected via open interfaces and optimized by intelligent controllers. This allows for multi-vendor, interoperable components and programmatically optimized networks through a centralized abstraction layer and data-driven closed-loop control. The O-RAN Alliance is defining a virtualization platform for the RAN and extending the definition of 3GPP and eCPRI interfaces to connect RAN nodes
    Architecture

### Architecture

    ![images](https://hackmd.io/_uploads/r182-xBK3.png)

    The main architecture of O-RAN is based on key principles that have been at the center of the Software-defined Networking (SDN) transformation in wired networks in the past 15 years, and have started moving into the wireless domain more recently . The main architectural building blocks of O-RAN include the near-RT and non-RT RICs and the SMO. The O-RAN interfaces include E2, O1, A1, the fronthaul interface, and O2.


### Building Blocks

**RIC (Radio Intelligent Controllers)**

* RICs (Radio Intelligent Controllers) are essential components of the O-RAN architecture, facilitating control and optimization of the RAN (Radio Access Network).
* There are two types of RICs: near-RT RIC and non-RT RIC. The near-RT RIC handles real-time control and optimization, while the non-RT RIC handles non-real-time control and optimization.
* RICs connect to the Service Management and Orchestration (SMO) through different interfaces: A1 for both RIC types, E2 for near-RT RIC, and O1 for non-RT RIC.
* RICs support the execution of third-party applications called rApps/xApps, enabling value-added services such as policy guidance, enrichment information, configuration management, and data analytics for RAN optimization and operations. They contribute to the network’s flexibility and programmability.

**O-DU (O-RAN Distributed Unit)**

* The O-DU is responsible for distributed baseband processing in the O-RAN architecture.
* It performs functions like digitization, modulation/demodulation, and low-level radio signal processing.
* Multiple O-DUs can be deployed in a distributed manner to cover a geographical area, improving scalability and reducing latency.

**O-CU (O-RAN Centralized Unit)**

* The O-CU is responsible for centralized baseband processing in the O-RAN architecture.
* It handles functions such as radio resource management, scheduling, and beamforming.
* The O-CU receives instructions from the O-RAN RIC and coordinates the distributed units (O-DUs) for radio transmission and reception.

**O-RU (O-RAN Radio Unit)**

* Open Interface: The o-RU follows a standardized protocol, allowing interoperability between different vendors’ equipment in the radio access network.
* Distributed Architecture: The o-RU works alongside the distributed unit (DU) to provide flexible and efficient radio access capabilities.
* Radio Signal Processing: The o-RU handles functions like modulation, demodulation, encoding, decoding, beamforming, and filtering for effective wireless signal transmission.
* Conversion: The o-RU converts digital baseband signals to analog RF signals for transmission and vice versa, enabling communication between digital and analog domains.
* Remote Configuration and Management: The o-RU can be remotely configured, managed, and monitored, facilitating efficient operation, parameter adjustments, and software updates without physical access.

**SMO (Service Management and Orchestration)**

![image alt](https://hackmd.io/_uploads/rJ6Y8nQtn.png)

* The SMO (Service Management and Orchestration) is an important part of the O-RAN architecture that takes care of managing the RAN (Radio Access Network) and controlling different types of RICs (RAN Intelligent Controllers) that work in real-time and non-real-time.
* The SMO connects to the RICs through specific interfaces: A1 for both real-time and non-real-time RICs, E2 for real-time RICs, and O1 for non-real-time RICs.
* The SMO handles various management tasks like fixing faults, setting up configurations, keeping track of resources, monitoring performance, and ensuring security. It also manages services and resources, organizes the network’s structure, and handles policies for network operations.
* Acting like a bridge, the SMO coordinates different functions across the entire network. This allows special apps within the O-RAN system to gather information about the RAN. The SMO uses this information to make smart decisions about services, computing at the network’s edge, and how the network is divided into slices.
* The SMO is a crucial part of the O-RAN architecture that ensures everything runs smoothly and efficiently. It manages the RAN, controls different types of RICs, handles important management tasks, makes informed decisions based on gathered information, and optimizes network operations and services.


