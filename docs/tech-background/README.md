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


# TEEP: API & DB

[ToC]

## Application Programming Interface (API)

### Definition

Application Programming Interface (API) defines how software applications communicate with each other using request and responses. An API documentation will contains information on how developers can use and structure those request and responses. API acts as an intermediary layer that processes data transfer between systems, letting companies open their application data and functionality to external third-part developers, business partners, and internal departments withing their companies.

### Types of API

![HJ5O4VIKT](https://hackmd.io/_uploads/rkIsx78cT.png)

* **OpenAPI**
    Open API also know as public API are an open-source API that everyone can access with HTTP protocol. This API allows companies to publicly expose information and functionalities of their system and application to third parties.

* **Partner API**
    Partner API are use to connect strategic business partners. Usually developers can access these API with a Public API developer portal but the developer still requires onboarding process and login credentials to access this partners API.

* **Internal API**
    Internal API also known as private API are hidden from external users. Internal API purpose is to improve productivity and communication across different internal development teams.

* **Composite API**
    Composite API combines multiple service APIs to allow developers to access several endpoints in a single call. This type of API are useful in microservices architecture where we need to perform a single task that may require information from several different sources.
    
    
### Types of API Protocols

* **Simple Object Access Protocol (SOAP)**
    SOAP API enables endpoints to communicate between server and client through SMTP and HTTP with XML as the data format. SOAP API was built to easily share information between software components that runs on different environments or written in different languages. This API protocol was more popular in the past but now is less flexible compare to other types of API protocols.

* **Remote Procedure Call (RPC)**
    Remote Procedure Call (RPC) is used to call other processes on a remote systems. RPC is also know as a function call. In this protocol, clinets calls or complets a function on the remote server and the server sends the output back to the client.
    
    ![B178AbItT](https://hackmd.io/_uploads/r1oAWXUq6.png)
    
    There are two types of data format used in RPC API:
    1. XML
    2. JSON

    RPC using XML data format are older than SOAP but a much simpler and lightweight because it uses minimum bandwidth

* **Websocket**

    ![rkksMGIY6](https://hackmd.io/_uploads/Hk7fMmI56.png)

    Websocket can be used as ‘real-time’ application that are faster and requires less overhead than REST API.Websocket supports two-way communication between client and server. This allows the server to send a callback message to connected clients therefore making it more efficient than REST API. This connection are persistent until one side closes the communication channel. Websocket uses JSON object as the data.

* **Representational State Transfer (REST)**

    ![r1RQIMIFT](https://hackmd.io/_uploads/BJ0MMXI5T.png)

    REST API also known as RESTful API is the most popular and flexible found on websites today. REST API is a set of web API architectural constraints. REST API defines a set of functions such as clients can use these function to access server data. These data exhanges between clients and server uses HTTP protocol. REST API uses JSON objects to pass the data.
    
    - GET : used to get server data
    - POST : used to add new data to the server
    - PUT : used to update server data
    - DELETE : used to delete server data
    
    REST API main feature is Stateless. Stateless means that the server do not save the clients data between requests and each request is separate and unconnected.
    
### API Endpoint

API endpoints are the final touchpoint of an API communication. This API endpoint includes server URLS, services, and other specific digital locations from where information is sent and received between systems.

API endpoints is specific URL where an API can receive request about a specific resource on its server. Whenever client sends a request to an API on a specific URL, It will tell the server the location of a specific resource it wants to access.

Lets take a look an example API endpoint from Twitter

```bash=
https://api.twitter.com/2/tweets/{id}
```
From that API endpoint we can retrieve the content of a specific tweet from Twitter/X. id from the endpoint is the unique identifier of the tweet. Each tweet has a unique identifier, hence we can get a specific tweet.

## Database (DB)

### API Endpoint

API endpoints are the final touchpoint of an API communication. This API endpoint includes server URLS, services, and other specific digital locations from where information is sent and received between systems.

> ON PROGRESS..

## E2E Test Between API and DB

> ON PROGRESS..

## E2E Test Between API and DB

> ON PROGRESS..

## Wireshark and Tshark

### Definition

Wireshark functions as both a sniffer and a packet analyzer. A sniffer serves as a measurement tool, allowing us to inspect the content flowing through a network cable or the airwaves in the case of a wireless network. Essentially, it reveals the data observed by our network card. It operates as a comprehensive packet analyzer, presenting meaningful information about the frames it encounters. As an open-source and freely available tool, Wireshark is widely employed for the examination of network traffic.

### Wireshark Capabilities

Wireshark is a significant tool for network analysis due to features like:

- **Packet Capture**: It captures packets traversing a network, either in real-time from network interfaces or from saved files.
- **Protocol Support**: Wireshark handles numerous protocols, including Ethernet, IP, TCP, and others, enabling analysis of various network traffic types.
- **User Interface**: The graphical interface is user-friendly with three main sections: packet list, details, and bytes panes, facilitating packet analysis.
- **Packet Filtering**: Filters can be applied to concentrate on specific packet types, based on protocols, addresses, and more.
- **Colorizing and Marking Packets**: Packet colorization aids in identifying patterns, and packets can be marked for referencing.
- **Packet Details**: Detailed insights into each packet, including headers and payload, are provided.
- **Statistics and Conversations**: Offers tools for network traffic analysis, including protocol-specific statistics and communication pattern insights.
- **Exporting Data**: Data can be exported in various formats for sharing or further analysis.
- **Display and Capture Filters**: These filters assist in focusing on particular traffic during live analysis.
- **VoIP Analysis**: Includes features for Voice over IP traffic analysis.
- **Expert Information**: Highlights potential issues in captured traffic for troubleshooting.
- **Scripting and Automation**: Supports Lua scripting for task automation and customized analysis.
- **Community Support**: An active community offers resources, forums, and documentation.

### Downloading and Installing Wireshark

1. Download Wireshark from [https://www.wireshark.org/#download](https://www.wireshark.org/#download).
2. Follow the installer instructions.

### Wireshark Layout

Wireshark's layout includes several key components:

- **Packet List**: Displays all packets in the capture file. Each packet is listed in a line with detailed information viewable in other panes.
- **Customizable Columns**: Users can choose which columns to display, like Packet Number, Time, Source, and more, based on preferences.
- **Packet Details**: This pane shows a hierarchical view of the selected packet’s protocol stack, with an option to expand or collapse nodes for detailed analysis.
- **Packet Bytes**: It presents the raw data of the selected packet in hexdump format, useful for in-depth analysis of the packet content.

### Sniffing Traffic with Wireshark

To capture network traffic in Wireshark:

1. Launch Wireshark and open the Capture Options window (Ctrl+K on PC, Cmd+K on Mac).
2. Select the relevant network interface observing current traffic.
3. Start capturing by hitting Enter or clicking the Start button.
4. Stop the capture using Ctrl+E / Cmd+E or via the menu.

The Wireshark interface includes:

- A menu and main toolbar for quick access to options.
- Display filter for specific packet filtering.
- Packet list pane showing a summary of each captured packet.
- Columns in the packet list include packet number, timestamp, source/destination addresses, protocol, length, and additional details.

### Tshark: Command-Line Protocol Analyzer

Tshark is an alternative to Wireshark for command-line interface enthusiasts, offering similar packet capturing and analyzing capabilities.

#### Installation on Linux-based OS

Install tshark using:

```bash
sudo apt-get install tshark
```

#### Basic Usage of Tshark Command

- View all tshark commands: `sudo tshark -h`
- Capture traffic on a specific interface: `sudo tshark -i <interface>`
- Save captured packets to a file: `tshark -i <interface> -w <file-name>.pcap`
- Read packets from a pcap file: `tshark -r <file-name>.pcap`
- Capture traffic for a specific duration: `tshark -i <interface> -a duration:<time>`
- Check tshark version: `tshark -v`
- Capture a specific number of packets: `tshark -c <number> -i <interface>`
- List available interfaces: `tshark -D`
- Capture specific protocol packets: `tshark -i <interface> -f "<protocol>"`

## Networking Programming with iPerf

iPerf is a versatile and cross-platform network performance measurement tool that is free and widely used. It supports a variety of protocols including TCP, UDP, and SCTP, along with compatibility for both IPv4 and IPv6. This tool is accessible on multiple operating systems, including Linux and Windows, making it a universal solution for network diagnostics and performance optimization. Network administrators and engineers often utilize iPerf to diagnose network issues, enhance network performance, and conduct experiments.

iPerf is also effective for network stress testing, especially with the UDP protocol. To properly stress test a network, users should set the bandwidth (using the -b parameter) much higher than the network's capacity.

### Automating Network Measurements with iPerf

iPerf can be automated for network bandwidth measurements, and Python is an excellent language for this task. For using iPerf2, one can utilize the pyperf2 library (version 0.2) or create a script to execute iPerf commands and gather outputs. iPerf3 also has a Python module available for simple measurements and automation.

### iPerf Usage Considerations

iPerf requires significant system resources and is theoretically capable of testing links up to 100Gbps. However, for such high-speed tests, professional traffic generators and specialized hardware are recommended.

### Advantages and Limitations of iPerf

**Advantages**:
- Supports major protocols like TCP, UDP, SCTP.
- Cross-platform compatibility.
- Simple command-line interface.
- Free and open-source.
- Pre-installed on some systems like TrueNAS.

**Limitations**:
- Limited community support.
- Unresolved bugs and resource monitoring requirements.
- No built-in report generation.
- Requires basic networking knowledge.
- Limited configuration options.
- iPerf3 is not backward compatible with iPerf2.
- High resource demand for substantial traffic volumes.

### iPerf Use Cases

- Checking iPerf version: `iperf -v`
- Running iPerf in server mode: `iperf -s -f K`
- Starting iPerf server on UDP port: `iperf -s -u`
- Measuring bidirectional bandwidths: `iperf -c [server IP] -r` and `iperf -c [server IP] -d`
- Checking UDP network statistics: `iperf -c [server IP] -u -b 10m`
- Launching parallel network tests: `iperf -c [server IP] -P [number of connections]`
- Testing TCP connection with maximum segment size: `iperf -c [server IP] -m`
- Exploring additional iperf command options: `iperf --help`

## Networking Programming: Understanding Ping

Ping is a fundamental command in networking, located at /usr/sbin/ping, which sends an ICMP ECHO_REQUEST to a host or gateway to receive an ICMP ECHO_RESPONSE. This command is essential for:

- Assessing network status and the reachability of foreign hosts.
- Identifying and resolving both hardware and software issues.
- Network testing, measurement, and management.

Operational and connected hosts respond to the echo request. Each request includes an IP and ICMP header, a ping PID, a timeval structure, and additional bytes to complete the packet. By default, ping sends continuous echo requests until interrupted (Ctrl-C).

Ping sends a datagram each second and outputs a line for every response. It calculates round-trip times and packet loss, providing a summary upon completion. The command ends after a set timeout or upon a SIGINT signal. The Host parameter can be a valid hostname or an Internet address.

The default behavior of ping is to continuously send echo requests until interrupted (Ctrl-C). The interrupt key can be modified using the stty command.

Continual echo requests can be taxing on the system, so their repeated use should primarily be for isolating problems.

### Ping Flags and Their Descriptions

- **-c Count**: Sends a specified number of echo requests.
- **-w timeout**: Sets a maximum timeout for a reply, used with -c.
- **-d**: Enables socket-level debugging.
- **-D**: Provides a hex dump of ICMP ECHO_REPLY packets.
- **-f**: Flood-ping option, sends packets rapidly. Root user only.
- **-I a.b.c.d**: Specifies an interface for IPv4 multicasts.
- **-o interface**: Specifies an interface for IPv6 multicasts.
- **-i Wait**: Sets a wait time between sending each packet.
- **-L**: Disables local loopback for multicast pings.
- **-l Preload**: Sends a rapid series of packets before normal operation.
- **-n**: Numeric output only, no symbolic names for host addresses.
- **-p Pattern**: Allows customizing the packet's padding.
- **-q**: Quiet output, only showing summary lines.
- **-r**: Directly sends to a host on an attached network.
- **-R**: Records route option, displaying the route buffer.
- **-a addr_family**: Maps destination address to IPv6 if 'inet6'.
- **-s PacketSize**: Sets the number of data bytes in each packet.
- **-S hostname/IP addr**: Specifies the source address in outgoing packets.
- **-T ttl**: Sets time-to-live for multicast packets.
- **-v**: Verbose output, listing received ICMP packets.

### Ping Parameters

- **PacketSize**: Number of data bytes sent. Default is 56.
- **Count**: Number of echo requests to be sent and received.

### Examples of Using Ping in Linux

Basic ping syntax: `ping [option] [hostname or IP address]`

To check the status of a remote host, for example, google.com:

```bash
ping google.com
```

- **from**: Destination and its IP address.
- **icmp_seq**: Sequence number of each ICMP packet.
- **ttl**: Time to Live value, representing network hops.
- **time**: Time taken for a packet to reach the destination and return.

Ping "localhost" to check the local network:

```bash
ping localhost
```

Change time interval between ping packets using -i:

```bash
ping -i 0.5 google.com
```

Change ping packet size with -s:

```bash
ping -s 1000 google.com
```

Limit the number of ping packets using -c:

```bash
ping -c 2 google.com
```
