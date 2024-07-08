#  NS3 Overview

## Table of Contents
- [NS3 Overview](#ns3-overview)
  - [Table of Contents](#table-of-contents)
  - [Goals](#goals)
  - [Main References](#main-references)
  - [Basic Overview of NS3](#basic-overview-of-ns3)
    - [Key Features](#key-features)
    - [Basic Components](#basic-components)
  - [Conceptual Overview](#conceptual-overview)
  - [Logging and Tracing](#logging-and-tracing)
  - [Conclusion](#conclusion)


## Goals

- To provide an introductory understanding of what NS3 is and its purpose.
- To help new users get started with NS3 by providing essential concepts and references.

## Main References

- [NS3 Official Website](https://www.nsnam.org/docs/tutorial/singlehtml/index.html)

## Basic Overview of NS3

In brief, ns-3 provides models of how packet data networks work and perform, and provides a simulation engine for users to conduct simulation experiments.

### Key Features
- **Modular Design**: NS3 is built in parts that can be easily added or changed.
- **Realism**: It provides detailed and realistic simulations.
- **C++ and Python**: You can write simulations in both C++ and Python.
- **Open Source**: NS3 is free to use and modify.

### Basic Components
- **Nodes**: These are like computers or devices in the network.
- **Applications**: Programs that generate and receive network traffic.
- **NetDevices**: Network interfaces like network cards.
- **Channels**: Paths through which data travels between nodes.
- **Protocols**: Rules for how data is sent and received, like TCP/IP.

## Conceptual Overview

1. **Node**
    - Node is the smallest computing unit in ns-3.
    - In ns-3, there is no real concept of an operating system, privilege levels, or system calls.

2. **UDP Client/Server Applications**
    - ns-3 uses specialized applications called UdpEchoClientApplication and UdpEchoServerApplication.
    - These applications are used to generate and echo network packets in a simulated environment, following a client/server model where the client sends packets and the server echoes them back.

3. **Channel**
    - A Channel connects a Node to an object representing a communication medium.
    - Channels can represent various types of networks, such as large Ethernet switches or three-dimensional space with obstacles for wireless networks.


4. **Net Devices**
    - A Net Device allows a Node to communicate with other Nodes through a Channel.
    - This includes both the software driver and simulated hardware.
    - A Node can connect to multiple Channels via multiple Net Devices.

5. **Topology Helper**
    - Topology helpers are tools designed to simplify common tasks in ns-3, such as connecting Net Devices to Nodes, Channels, and assigning IP addresses.
    - Example of using a topology helper:
```cpp
PointToPointHelper pointToPoint;
pointToPoint.SetDeviceAttribute("DataRate", StringValue("5Mbps"));
pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));

NetDeviceContainer devices;
devices = pointToPoint.Install(nodes);
```

## Logging and Tracing

1. Logging
    - ns-3 provides various logging levels to aid in debugging and monitoring simulations.
    - Logging levels include:
        - LOG_ERROR: Log error messages.
        - LOG_WARN: Log warning messages.
        - LOG_DEBUG: Log debug messages.
        - LOG_INFO: Log informational messages.
        - LOG_FUNCTION: Log messages for each function call.
        - LOG_LOGIC: Log logical flow within functions.
        - LOG_ALL: Log all messages.
    - To enable all logs for UdpEchoClientApplication:
    ```bash
    $ export NS_LOG=UdpEchoClientApplication=level_all
    ```
    
2. Tracing System
    - Tracing is a mechanism for generating output from simulations for further analysis.
    - It allows you to modify the output format or insert new tracing sources without altering the core simulator.
    - **ASCII Tracing**
        - ASCII tracing generates trace files in a readable text format.
        - Example of using ASCII tracing:
        ```cpp
        AsciiTraceHelper ascii;
        pointToPoint.EnableAsciiAll(ascii.CreateFileStream("myfirst.tr"));
        ```
        - Run the simulation
        ```bash
        AsciiTraceHelper ascii;
        pointToPoint.EnableAsciiAll(ascii.CreateFileStream("myfirst.tr"));
        ```
        - The file ``myfirst.tr`` will contain the trace of simulation operations like packet enqueue and dequeue.
    - **PCAP Tracing**
        - PCAP tracing generates trace files in the .pcap format, which can be analyzed using tools like Wireshark.
        - Example of enabling PCAP tracing:
        ```cpp
        pointToPoint.EnablePcapAll("myfirst");
        ```
        - Run the simulation:
        ```bash
        $ ./ns3 run scratch/myfirst
        ```
        - PCAP trace files will be created for each point-to-point device in the simulation.
        - Read the output with tcpdump:
        ```bash
        $ tcpdump -nn -tt -r myfirst-0-0.pcap
        ```
        This will display the details of packets sent and received during the simulation, including timing and protocol information.   
        
## Conclusion
ns-3 is a powerful tool for simulating networks. By using components like Nodes, Channels, Net Devices, and the tracing system, you can create complex simulations and analyze the results for various networking research and development purposes. Tools like topology helpers simplify network configuration tasks in the simulation, while the logging and tracing systems allow you to gather detailed information about simulated network operations.
