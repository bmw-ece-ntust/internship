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
