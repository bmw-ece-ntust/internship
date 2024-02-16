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
2. Execute the file

> ON PROGRESS


## Reference

> https://www.nsnam.org/docs/release/3.41/tutorial/singlehtml/index.html

