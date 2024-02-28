# NS-3 : Network Simulator 3

![](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-18-Rafli/assets/ns-3-logo.png)

NS-3 a discrete-event simulator typically run from the command line. It is written directly in C++, not in a high-level modeling language; simulation events are simply C++ function calls, organized by a scheduler.

## NS-3 Introduction

One of the primary goals of creating NS-3 is to enhance modeling approaches to more closely reflect reality upon implementation. Different simulation tools employ varied methods for network modeling, influenced by the programming languages used. For example, NS-3 uses C++ because it offers implementation facilities for C-based code. NS-3 is designed to emulate a LINUX computer, with internal interfaces (network to network drivers) and application interfaces (Sockets).


NS-3 provides a wide range of model libraries for simulations, simplifying both learning and simulation processes by allowing users to utilize these libraries as needed. NS-3 provides a wide range of model libraries for simulation purposes, including:

1. **Animation**
2. **Antenna Module**
3. **Ad Hoc-Demand Distance Vector**
4. **Application**
5. **Bridge Netdevice**
6. **BRITE Integration**
7. **Building Module**
8. **Click Modular Router Integration**
9. **CSMA NetDevice**
10. **DSDV Routing**
11. **DSR Routing**
12. **Emulation Overview**
13. **Energy Framework**
14. **File Descriptor Netdevice**
15. **Flow Monitor**
16. **Internet Model** (IP, TCP, Routing, UDP, Internet Application, Codel)
17. **Low Rate Wireless Personal Area Network (LR-WPAN)**
18. **LTE Module**
19. **Wi-Fi Mesh Module Documentation**
20. **MPI for Distributed Simulation**
21. **Mobility**
22. **Network Module**
23. **Optimized Link State Routing (OLSR)**
24. **OpenFlow Switch Support**
25. **Point to Point NetDevice**
26. **Propagation**
27. **Spectrum Module**
28. **6LowPAN: Transmission of IPv6 Packet over IEEE 802.15.4 Network**
29. **Tap NetDevice**
30. **Topology Input Readers**
31. **Traffic Control Layer**
32. **UAN Framework**
33. **WAVE Models**
34. **Wi-Fi Module**
35. **WiMAX NetDevice**

NS-3 is a discrete event network simulator designed for studying the dynamic nature of communication networks. It facilitates the simulation of both wired and wireless networks (including routing algorithms, TCP, UDP, etc.) and is primarily aimed at supporting research and educational activities in telecommunications. Official website: [https://www.nsnam.org/](https://www.nsnam.org/). The NS-3 project began in July 2006 with its first release on June 30, 2008. It supports C++ and Python, with C++ offering a more complex structure but more comprehensive libraries for user needs. NS-3's infrastructure supports simulation model development close to real-world conditions and network emulation characteristics. Besides IP-based network simulations, NS-3 can also simulate non-IP based networks.

**Advantages:**
- Acts as simulation software for analysis in research.
- Includes validation tools to test the validity of models in NS-3.
- Simulations are easier to create compared to other software developers.
- Open-source and free.
- Users can easily create topologies and simulation scenarios as needed.

**Example Simulations in NS-3:**
- TCP/UDP/RTP
- Traffic behavior (FTP, Telnet, CBR, etc.)
- Queue management (RED, FIFO, CBQ)
- Unicast (Distance Vector, Link State) and multicast routing algorithms
- PIM SM, PIM DM, DVMRP, Shared Tree, and Bi-directional Shared Tree
- Multimedia applications such as layered video, QoS audio-video, transcoding, and more.

### Understanding Network Elements in NS-3

To effectively work with NS-3, it's important to familiarize oneself with the simulator's concepts and abstractions. While these concepts might initially seem complex, taking the time to understand them is valuable. This section reviews common networking terminology, which has specific interpretations within NS-3, as illustrated in figure 6.1.

![](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-18-Rafli/assets/ns3-element.jpg)

NS-3 models a wide array of computer network elements, including:

1. **Node:** In internet terminology, computers connected to a network are typically known as hosts or end systems. However, since NS-3 serves as a general network simulator rather than an internet-specific one, it avoids the term "host" to prevent confusion with internet and its protocols. Instead, NS-3 utilizes the term "Node," which is widely used across various simulators, to denote a simple network device. This abstraction is represented by the `Node` class in NS-3's C++ programming language, handling methods for managing a network device's representation within simulations. Nodes are essentially considered computers, which can be enhanced by adding functionalities such as applications, internet protocols, and other capabilities to make them fully operational.

2. **Communication Protocols:** These are sets of rules designed to govern communication among different objects. In NS-3, protocols are managed within a protocol stack, where each layer within the stack has specific functions for handling network packets, passing them to either the layer above or below for further processing.

3. **Protocol Header:** As data packets are transmitted across network layers, they are appended with headers to facilitate routing and ease processing by the recipient. A protocol header is part of the data packet sent and has a specific format for each related protocol object. For example, IPv4 (Internet Protocol version 4), as described in RFC760, has a unique protocol header layout specifically used for IPv4. Almost all protocol types clearly define their format to store protocol-related information within network packets.

4. **Network Packet:** A crucial component in the exchange of information or data across a network. Network packets typically contain one or more protocol headers detailing the implementation requirements of protocols on the receiving side, along with various paths traversed during the information exchange process. More in-depth, a network packet comprises a payload representing the actual data.

5. **Application:** Software on computers is broadly categorized into two major classes: System Software and applications. System software organizes various computer resources like memory, processor cycles, disks, etc., based on a computing model but does not directly utilize resources to complete tasks related to the user. Users generally run applications that employ resources managed by system software to achieve desired outcomes. NS-3 does not have a real concept for system software, especially in the absence of a concept of level distinction. Essentially, NS-3 views it merely as software applications running on a computer in "real life." Hence, NS-3 applications run on NS-3 nodes to conduct simulations. In NS-3, applications can be simply described as users with programs generating activities to be executed, represented in C++ by the `Application` class. This class provides methods for managing a representation of a user-level application within simulations. Developers are expected to master the `Application` class in object-oriented programming to create new applications. Specifically, this book will discuss the `UdpEchoClientApplication` and `UdpEchoServerApplication` application classes, building a client/server application used for simulating network packet exchanges.

6. **Channel/Link:** In the real world, one can connect a computer to a network. The medium through which data flows in this network is referred to as a channel or link. Connecting an ethernet cable to an ethernet network, for instance, links the computer to the ethernet communication channel. Other examples include optical fiber for point-to-point links and shared media broadcasts like Ethernet or wireless spectrum for wireless communications. Essentially, a communication channel in NS-3 simulations is formed when connecting a node to an object, represented in C++ source code by the `Channel` class. Like the classes mentioned earlier, the `Channel` class provides methods for managing communication among objects to connect nodes to the channel itself. Channels might also need to be specialized by developers in object-oriented programming, ranging from simple models like cable communication to more complex ones like an ethernet switch model or wireless networks.

7. **Net Device/Network Device:** To connect a computer to a network, one requires a network cable and an interface peripheral card with several network functions, commonly known as a NIC (Network Interface Card). Nowadays, most computers come with built-in network hardware, sometimes making users unaware of the separate network system block within. A NIC cannot function without software drivers to control this hardware. In Unix, this hardware is classified as a device, controlled using a driver, with the NIC managed by a Net Device or network device driver. In Unix or Linux, this Net Device is familiarly known as eth0 (Ethernet 0) or wlan0 (wireless LAN 0). In NS-3, the Net Device represents both software and hardware aspects. When a Net Device is installed on a node, it allows the node to communicate with other nodes in the simulation via a channel or link. As in real-life conditions, a node can connect to multiple channels using many Net Devices. For example, a computer equipped with interfaces for both wired (Ethernet) and wireless (Wi-Fi) network connections. The Net Device is represented by the `Net Device` class in NS-3's C++ source. This book will use several Net Devices, such as `CsmaNetDevice`, `PointToPointNetDevice`, and `WifiNetDevice`, similar to how an Ethernet NIC operates for ethernet networks, with the `CsmaNetDevice` created to work with `CsmaChannel`.

8. **Topology Helper:** In real-world networks, a computer comes equipped with a NIC. In NS-3, a node comes equipped with Net Devices. For larger network simulations, many aspects need to be managed, such as more connections between nodes, setting up Net devices and channels, connecting Net Devices to a Node, connecting Net Devices to a Channel, assigning IP addresses, and more. NS-3 provides what is called a Topology Helper to simplify simulation setup. For example, to create Net Devices, add MAC addresses, install Net Devices on Nodes, configure the node's protocol stack, and connect Net Devices to a Channel. For larger networks, it might be necessary to connect multiple devices to several channels and to connect networks to larger networks. NS-3 offers topology helper objects that combine several different operations for easier use.

### Basic Steps in NS-3 Simulation Programming with C++

When writing NS-3 simulation programs using C++, there are four fundamental steps to follow:

![](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-18-Rafli/assets/ns3-flowchart.png)

1. **Create Network Topology:**
   The creation of a network topology involves initializing objects in C++ such as nodes, network devices, channels (or links), and the network protocols to be used for the network modeling simulation. This step sets the foundation for how various components of the network will interact with each other, following a process similar to the flow chart depicted below (Figure 6.3 illustrates the sequence of creating a network topology in NS-3).

2. **Generate Network Traffic Requirements:**
   This step involves creating simulation models for different types of networks that manage the sending and receiving of information. Consequently, the packets generated can be appropriately received and processed. It's about defining the data flow within the network, including sources, destinations, and the nature of the traffic (e.g., continuous, bursty, or transactional).

3. **Run the Simulation:**
   The process of running the simulation continues iteratively until all the commands in the list have been executed, or the predetermined simulation time has elapsed. This step involves activating the simulation environment to mimic the behavior of the network based on the previously defined topology and traffic patterns.

4. **Analyze Simulation Results:**
   After the simulation has run and generated trace information, this step involves analyzing the outcomes to derive insights into network performance. Various metrics can be evaluated, such as average link utilization, queue lengths, packet drop rates, and more. NS-3's pcap trace facility can be utilized to visualize and further analyze the simulation data, providing a detailed view of the network's behavior under specified conditions.


### NS-3 Pre-Requisite

1. Install the required package

    - Before starting the NS-3 installation, a compiler is required for it can install NS-3 dependencies
        ```bash
        sudo apt install build-essential -y
        ```
    - Qt installation to be able to install NetAnim on NS-3
        ```bash
        sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
        ```
    - Then, there are several dependency packages that need to be installed first.
        ```bash
        sudo apt install g++ python3 cmake ninja-build git gir1.2-goocanvas-2.0 python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3 tcpdump wireshark sqlite sqlite3 libsqlite3-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools openmpi-bin openmpi-common openmpi-doc libopenmpi-dev doxygen graphviz imagemagick python3-sphinx dia texlive dvipng latexmk texlive-extra-utils texlive-latex-extra texlive-font-utils libeigen3-dev gsl-bin libgsl-dev libgslcblas0 libxml2 libxml2-dev libgtk-3-dev lxc-utils lxc-templates vtun uml-utilities ebtables bridge-utils libboost-all-dev -y
        ```

### NS-3 Installation

1. Download NS-3 Latest Release

    Download the latest release as a source code archive from the main ns-3 web site.
    - Download the tar file from the official image
        ```bash
        wget vhttps://www.nsnam.org/releases/ns-allinone-3.41.tar.bz2
        ```
    - Unpack it in a working directory of your choice
        ```bash
        tar xjf ns-allinone-3.41.tar.bz2
        ```
    - Change into the ns-3 directory
        ```bash
        cd ns-allinone-3.41/ns-3.41
        ```
2. Building and testing NS-3

    The next step is to configure the build using the CMake build system. The below commands make use of a Python wrapper around CMake, called ns3, that simplifies the command-line syntax, resembling Waf syntax.
    - First to do default build profile 
        ```bash
        ./ns3 configure --enable-examples --enable-tests
        ```
    - Then, use ns3 to build ns-3
        ```bash
        ./ns3 build
        ```

    - This are the expected output

        ![](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-18-Rafli/assets/ns3-build-success.jpg)

    - Once complete, you can run the unit tests to check your build
        ```bash
        ./test.py
        ```
     To run the first tutorial program, whose source code is located at examples/tutorial/first.cc, use ns3 to run it.
    - Run example script
        ```bash
        ./ns3 run first
        ```
    - To view possible command-line options, specify the `–PrintHelp` argument:
        ```bash
        ./ns3 run 'first --PrintHelp'
        ```

### NetAnim Installation

1. Install NetAnim

```bash
# cd ns-allinone-3.41 
cd netanim-3.41/
qmake NetAnim.pro
make
```

## Point-to-Point Simmulation

### Fundamentals of Point-to-Point Networking

Before delving into simulating Point-to-Point Protocol (PPP) with NS-3, let's first understand what the point-to-point protocol is and how it operates. Point-to-point protocol is an encapsulation protocol designed to channel IP traffic over a point-to-point link. PPP is comprised of three main components:

1. **Link Control Protocol (LCP):**
   LCP is responsible for establishing, maintaining, and terminating the connection between two points or endpoints. It also tests the channel to determine whether it is active. Before a connection is established, LCP configures certain parameters of the connection such as Frame Check Sequence (FCS) and High-Level Data Link Control (HDLC) framing. By default, PPP uses a 16-bit FCS, but this can be changed to a 32-bit FCS or even 0 bit (no FCS). Alternatively, HDLC encapsulation over a PPP link can be used. Once the connection is established, the hosts on the PPP link generate Echo-Request and Echo-Response packets to maintain the PPP link.

2. **PPP Authentication:**
   The Authentication Protocol functions to ensure security between two points. The PPP layer's authentication protocol uses protocols to help ensure the validity of endpoints on the PPP link. Authentication protocols include the Password Authentication Protocol (PAP), Extensible Authentication Protocol (EAP), and Challenge Handshake Authentication Protocol (CHAP), with CHAP being the most commonly used at present.

3. **Network Control Protocol (NCP):**
   NCP facilitates the initiation of the PPP protocol stack to handle multiple Network Layer Protocols such as IPv4, IPv6, and Connectionless Network Protocol (CLNP). After the authentication process is completed, the PPP connection can be considered established. At this stage, higher-level protocols (such as Internet Protocol or IP) can initiate and function as intended.

### Initial Steps with NS-3 Point-to-Point Example

As an initial step, we will try running and modifying the NS-3 point-to-point example provided.

Upon downloading and installing NS-3 as per the instructions, you will find the NS-3 release in the home directory named `repos`. Moving to the releases directory, you will encounter a file structure as shown below (Figure 7.2 File Structure).

Next, try entering the directory named `examples/tutorial`. Here, you will find a file named `first.cc`. This file is a script for creating a simple network configuration, namely a point-to-point network between two nodes, including echo packets between both nodes.

1. Create the script `first.cpp`

    ```cpp=
    /*
    * This program is free software; you can redistribute it and/or modify
    * it under the terms of the GNU General Public License version 2 as
    * published by the Free Software Foundation;
    *
    * This program is distributed in the hope that it will be useful,
    * but WITHOUT ANY WARRANTY; without even the implied warranty of
    * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    * GNU General Public License for more details.
    *
    * You should have received a copy of the GNU General Public License
    * along with this program; if not, write to the Free Software
    * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
    */

    #include "ns3/applications-module.h"
    #include "ns3/core-module.h"
    #include "ns3/internet-module.h"
    #include "ns3/network-module.h"
    #include "ns3/point-to-point-module.h"
    #include "ns3/netanim-module.h"
    // Default Network Topology
    //
    //       10.1.1.0
    // n0 -------------- n1
    //    point-to-point
    //

    using namespace ns3;

    NS_LOG_COMPONENT_DEFINE("FirstScriptExample");

    int
    main(int argc, char* argv[])
    {
        CommandLine cmd(__FILE__);
        cmd.Parse(argc, argv);

        Time::SetResolution(Time::NS);
        LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
        LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);

        NodeContainer nodes;
        nodes.Create(2);

        PointToPointHelper pointToPoint;
        pointToPoint.SetDeviceAttribute("DataRate", StringValue("5Mbps"));
        pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));

        NetDeviceContainer devices;
        devices = pointToPoint.Install(nodes);

        InternetStackHelper stack;
        stack.Install(nodes);

        Ipv4AddressHelper address;
        address.SetBase("10.1.1.0", "255.255.255.0");

        Ipv4InterfaceContainer interfaces = address.Assign(devices);

        UdpEchoServerHelper echoServer(9);

        ApplicationContainer serverApps = echoServer.Install(nodes.Get(1));
        serverApps.Start(Seconds(1.0));
        serverApps.Stop(Seconds(10.0));

        UdpEchoClientHelper echoClient(interfaces.GetAddress(1), 9);
        echoClient.SetAttribute("MaxPackets", UintegerValue(1));
        echoClient.SetAttribute("Interval", TimeValue(Seconds(1.0)));
        echoClient.SetAttribute("PacketSize", UintegerValue(1024));

        ApplicationContainer clientApps = echoClient.Install(nodes.Get(0));
        clientApps.Start(Seconds(2.0));
        clientApps.Stop(Seconds(10.0));

        Simulator::Run();
        Simulator::Destroy();
        return 0;
    }
    ```

## Traffic Generation in NS-3

Traffic generation in simulation models represents the stochastic nature of traffic flows or data sources within communication networks, such as cellular networks or computer networks. Generating traffic in simulations is crucial for evaluating the performance of a network setup, developing specific technologies in terms of protocol performance, or examining the system blocks within it. In NS-3, two commonly used protocols for traffic generation are UDP (User Datagram Protocol) and TCP (Transmission Control Protocol).

In NS-3, several traffic generators can be used to populate the application layer on a node. In previous simulations, we utilized `UdpEchoServer` and `UdpEchoClient` applications for generating and receiving data within our simulations. However, there are other methods to generate application traffic in simulations beyond these two models. Among them are:

1. **OnOffApplication**: This application can simulate variable bitrate traffic, such as video streaming or VoIP. It alternates between "On" periods, where it generates data packets, and "Off" periods, where no packets are generated, according to specified patterns.
2. **BulkSendApplication**: This application is designed to continuously send out a large block of data until a specified number of bytes have been sent. It's useful for simulating file transfers or other scenarios where a large amount of data needs to be sent continuously.

Both `OnOffApplication` and `BulkSendApplication` are used on the sender's side, whereas `PacketSink` is used by the receiver to absorb the packets sent by these applications. The following sections will explain how to create traffic using `OnOffApplication` and `BulkSendApplication`.

### OnOffApplication in NS-3

`OnOffApplication` in NS-3 is primarily used with the UDP protocol by default to generate network traffic. To facilitate the creation of an `OnOffApplication` with customizable attributes, the `OnOffApplicationHelper` is employed. This helper enables the configuration of various attributes of the `OnOffApplication`, including:

- **DataRate:** The data rate during the "On" state.
- **PacketSize:** The size of packets to be sent.
- **Remote:** The address of the traffic target or the destination address for data transmission.
- **OnTime:** A variable stream used to define the duration of the "On" state.
- **OffTime:** A variable stream used to define the duration of the "Off" state.
- **MaxBytes:** The total number of bytes that should be sent. Once this limit is reached, transmission will cease.
- **Protocol:** The type of protocol used (UDP by default).

These attributes allow for detailed control over the traffic generation process, enabling simulations to more closely mimic real-world data flow patterns.

### BulkSendApplication in NS-3

Unlike `OnOffApplication`, the `BulkSendApplication` in NS-3 defaults to using the TCP protocol and its operation can be likened to that of an FTP application. While it uses TCP as its base protocol and aims to send the entirety of the data as quickly as possible, it does not necessarily emulate FTP behavior. Key attributes that can be configured within `BulkSendApplication` include:

- **SendSize:** The size of packets sent at each interval.
- **Remote:** The address of the traffic target or the destination address for data transmission.
- **MaxBytes:** The total number of bytes that must be sent. Once this limit is reached, the transmission will cease.
- **Protocol:** The type of protocol used (TCP by default).

These configurable attributes allow for the simulation of sustained, high-volume data transfers over TCP, useful for scenarios that require the modeling of continuous data streams, such as file transfers.

### Data Collection in NS-3

Unlike NS-2, NS-3 offers a distinct module for the collection of simulation output data. In NS-2, processing raw data or recording specific parameters requires manual procedures. NS-3 simplifies this process with the `FlowMonitor` module.

`FlowMonitor` in NS-3 enables the tracing of each data flow generated by applications or specific algorithms at the IP layer. This allows for the collection of data regarding flows from a source IP to a destination IP and provides a summary of the transmission. To activate `FlowMonitor`, it's as simple as including the flow monitor header and creating a flow monitor object to be installed on all nodes.

## Open RAN Simulation

ns-O-RAN is the first open source simulation platform that combines a functional 4G/5G protocol stack in ns-3 with an O-RAN-compliant E2 interface. This completes WIoT’s OpenRAN Gym platform with a simulator that can enhance data collection and xApp testing capabilities, a key step toward enabling efficient and generic AI and ML solutions for Open RAN and 5G/6G systems.

![](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-18-Rafli/assets/ns3-o-ran.png)

ns-O-RAN has been designed and implemented to enable the integration of O-RAN software such as the O-RAN Software Community Near-RT RIC with large-scale 5G simulations based on 3GPP channel models and a detailed modeling of the full 3GPP RAN protocol stack. This allows data collection of RAN Key Performance Metrics (KPMs) at scale, in different simulated scenarios, and with different applications (e.g., multimedia streaming, web browsing, wireless virtual reality, etc). ns-O-RAN supports an O-RAN-compliant E2 interface and implements two E2 service models (E2SM), E2SM-Key Performance Metrics (KPM) monitoring and E2SM-RAN Control (RC), that enable a closed-loop control (for example, of traffic steering and mobility).

### Introduction: End-to-End Deployment with OpenRAN Gym RIC

> Document from: https://doi.org/10.48550/arXiv.2305.06906

This later explanation show the process for setting up ns-O-RAN within a virtualized environment, thereby establishing a connection between the RIC (Radio Intelligent Controller) and ns-3, and allowing the exchange of E2 messages. This setup facilitates a simulated closed control loop between ns-3 and a near-real-time RIC, illustrating a practical application of the ns-O-RAN system within the OpenRAN Gym framework.

The setup involves using the near-real-time RIC from the OpenRAN Gym, which can be installed on a local workstation or loaded into experimental platforms like Colosseum. The document provides a tutorial for setting up this environment, highlighting the process for collecting Key Performance Measurements (KPMs) from the RAN, wrapping them into RIC Indication Messages, and sending them through the E2 interface. The RIC receives these messages, reads the KPMs and Key Performance Indicators (KPIs), and then defines a data-driven policy. Based on this policy, the RIC creates a Control Action, sends it back to the RAN via a RIC Control Message, and the RAN applies the requested changes.

This end-to-end deployment showcases the practical aspects of integrating ns-O-RAN with a real-world RIC, demonstrating how simulated networks can interact with RICs to test and refine control policies in a controlled environment. The description emphasizes the importance of this interaction in enabling a data-driven approach to network management and optimization within the O-RAN architecture, providing a valuable tool for researchers and developers working on O-RAN technologies.

#### Implementation Details : End-to-End Deployment with OpenRAN Gym RIC

The paper describes ns-O-RAN as the first open-source simulation platform that integrates a complete 4G/5G protocol stack with an O-RAN-compliant E2 interface, specifically designed for simulated base stations. This integration is a significant advancement toward enabling efficient and generic AI and ML solutions for Open RAN and future cellular networks. By facilitating the integration of O-RAN software, such as OpenRAN Gym and OSC near-RT RICs with large-scale 5G simulations using 3GPP channel models, ns-O-RAN allows for comprehensive data collection of RAN KPMs across various simulated scenarios. This is critical for testing xApps under different conditions, such as multimedia streaming, web browsing, and wireless virtual reality applications.

The design also incorporates two distinct E2 service models (SMs): E2 SM KPM for reporting and E2 SM RAN Control (RC) for executing control actions within the RAN, such as traffic steering and mobility management. At its core, ns-O-RAN operates as an external ns-3 module, establishing an SCTP connection between the simulator and the near-RT RIC to support E2AP and E2SM protocols. This connection is realized by enhancing the OSC E2 simulator (e2sim) and integrating it into an ad hoc module for ns-3, allowing for the exchange of E2 messages between the simulated environment and the RIC.

#### Use Cases and Applications : End-to-End Deployment with OpenRAN Gym RIC

ns-O-RAN significantly enhances the versatility of the OpenRAN Gym approach, enabling the development and testing of xApps and AI-based control policies within a simulated environment. This capability is especially beneficial for generating large-scale, 3GPP-compliant datasets, which can later be applied to experimental platforms like Colosseum for emulation with hardware in the loop and further testing on over-the-air testbeds. A key feature of ns-O-RAN's design is its ability to connect the emulated environment to any O-RAN-compliant near-real-time RIC with real xApps, eliminating the need for re-implementation when transitioning from simulated to experimental environments. This design choice simplifies the development lifecycle of end-to-end intelligent control solutions for Open RAN, making it a practical tool for demonstrating intelligent control of handovers in large-scale 5G scenarios.

ns-O-RAN's implementation showcases its potential in accelerating the development and deployment of xApps by providing a realistic dataset generation and testing environment without the need for physical infrastructure. This approach not only fosters innovation in network management and optimization through AI and ML but also ensures that xApps developed within ns-O-RAN can be seamlessly deployed in real RAN environments with minimal adjustments, thereby bridging the gap between simulation and practical application in the Open RAN ecosystem.

### Near-RT RIC Setup

This part of the tutorial requires a working version of Docker for hosting the RIC on your localhost.

We first start by cloning and setup the Colosseum’s near-RT RIC with the following commands:

```bash
git clone -b ns-o-ran https://github.com/wineslab/colosseum-near-rt-ric
cd colosseum-near-rt-ric/setup-scripts
```

Then we first import all the images we need in Docker, we tag them properly and we build and launch them:

```bash
./import-wines-images.sh  # import and tag
./setup-ric-bronze.sh  # setup and launch
```

After the last step, the main entities of the RIC should be up and running in different Docker containers (this can be easily checked with the docker ps command). To understand what is going on in the RIC and to have a feedback once we start ns-O-RAN, we can open two terminal for the RIC, one for logging the values on the E2Term and check the E2AP messages exchange, the other for the xApp.

```bash
# Terminal 1 logs the E2Term
docker logs e2term -f --since=1s 2>&1 | grep gnb:  # this will help to show only when a gnb is interacting

# Terminal 2 builds and run the x-app container
cd colosseum-near-rt-ric/setup-scripts
./start-xapp-ns-o-ran.sh
```

This last command will build and run a Docker container for the x-app and will also create a shell inside the container, and log you inside the container. Finally, we can move to the /home/sample-xapp directory inside the Docker container, and run the xApp logic:

```
cd /home/sample-xapp
./run_xapp.sh
```

These lasts commands concludes the setup of the RIC. If you already have a working RIC just make sure to annotate the IP address of the E2Term, which is needed to create the connection between ns-O-RAN and the RIC.

### ns-O-RAN Setup

To properly install ns-3 and ns-O-RAN, several options are available, including the use of the Dockerfile provided in the root of the near-RT RIC repository. In this part of the tutorial, we will setup and install the ns-O-RAN framework. As described in the related paper and in the Figure above, ns-O-RAN is composed by three main parts:

- The e2sim software, which was originally developed by the OSC community.
- The ns3-mmWave version, which was originally developed by the University of Padova and NYU.
- The ns-O-RAN module, developed by Northeastern University and Mavenir, which is basically an external module that can be plugged in ns-3 and uses the e2sim to create a SCTP connection with the RIC.

We adapted the first two software to enable the end-to-end communication with the near-RT RIC and the digestion of the E2AP and E2SM messages. We first start with the installation of the prerequisites. In Ubuntu 20.04 LTS, these can be installed with:

```bash
sudo apt-get update
# Requirements for e2sim
sudo apt-get install -y build-essential git cmake libsctp-dev autoconf automake libtool bison flex libboost-all-dev 
# Requirements for ns-3
sudo apt-get install g++ python3
```

Then we can clone and install the e2Sim software. To see the E2 ASN messages on the e2sim, we build it with LOG_LEVEL equal to 3 (DEBUG). This is useful to debug the exchange of the messages between the ns-3 and the RIC, but we also provide different debug levels that can be setup. These levels are summarized in the table below.

```bash
git clone https://github.com/wineslab/ns-o-ran-e2-sim oran-e2sim # this will create a folder called oran-e2sim
cd oran-e2sim/e2sim/
mkdir build
./build_e2sim.sh 3
```

This last command shall configure the cmake project and install the e2sim on the system. Its main actions are also in the aforementioned Dockerfile that we report here to clarify the operations conducted by the script:

```Dockerfile
RUN mkdir /workspace/e2sim/e2sim/build
WORKDIR /workspace/e2sim/e2sim/build # Creation and cd on the build directory
RUN cmake .. -DDEV_PKG=1 -DLOG_LEVEL=${log_level_e2sim} # build of the project with the LOG_LEVEL desired

RUN make package # Creation of the package
RUN echo "Going to install e2sim-dev"
RUN dpkg --install ./e2sim-dev_1.0.0_amd64.deb # Installation of the generated package on the system
RUN ldconfig  # library update to make the package linkable from ns-3 without rebooting the machine
```

It is now time to clone and install the ns3-mmWave project:

```bash
git clone https://github.com/wineslab/ns-o-ran-ns3-mmwave ns-3-mmwave-oran
cd ns-3-mmwave-oran
```

This project supports the 3.36 version of ns-3, thus we still use the old waf toolchain to configure, build and run ns-3. We plan to upgrade our version of ns-3 in the near future and, as a consequence of this, we will also update the guide. After this step, we can clone the ns-O-RAN module and insert it in the ns3-mmWave project in the contrib directory:

```bash
cd ns-3-mmwave-oran/contrib
git clone -b master https://github.com/o-ran-sc/sim-ns3-o-ran-e2 oran-interface
cd ..  # go back to the ns-3-mmwave-oran folder
```

We now have all the software in place to configure and build ns-3:

```bash
./waf configure --enable-examples --enable-tests
./waf build
```

## Reference

> https://www.nsnam.org/docs/release/3.41/tutorial/singlehtml/index.html

