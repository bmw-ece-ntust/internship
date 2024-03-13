# NETCONF
## What is NETCONF?
* The Network Configuration Protocol (NETCONF) is an Internet Engineering Task Force (IETF) network management protocol that provides a secure mechanism for installing,
manipulating and deleting the configuration data on a network device, such as a firewall, router or switch.
* NETCONF was developed by the NETCONF working group and published in December 2006 as RFC 4741. The protocol was then revised in June 2011 and published as RFC 6241. This is the most current version.
The IETF also published several other RFCs related to NETCONF. For example, RFC 5277 defines a mechanism for supporting an asynchronous message notification service for NETCONF.
* The NETCONF protocol was designed to make up for the shortcomings of the Simple Network Management Protocol and the command-line interface scripting used to configure network devices.

## How does NETCONF work?
* A NETCONF system contains at least one NMS that manages network-wide devices. NETCONF uses the Remote Procedure Call (RPC) protocol to carry out communications between clients and servers. RPC is a client/server protocol that lets a program request a service from another program without understanding the details of the underlying network.
RPC messages are encoded in Extensible Markup Language (XML) and transmitted via secure connection-oriented sessions. The NETCONF architecture consists of two roles: client and server.

  ![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/7cb3f594-75b0-4fe8-9859-0383220136ff)

* **The Client** which can be a script or application, sends RFC messages that invoke operations on the server. T
he client can also subscribe to receive notifications from the server. The details are as follows:
    * Manages network devices using NETCONF.
    * Sends RPC requests to a NETCONF server to query or modify one or more parameter values.
    * Learns the status of a managed device based on the alarms and events sent by the NETCONF server of the managed device.
      
* **The Server** which is usually a network device, executes the operations invoked by the client, and it can send notifications to the client. The
details are as follows:
    * When receiving a request from a NETCONF client, the NETCONF server parses the request and sends a reply to the client.
    * If a fault or another type of event occurs on a managed device, the NETCONF server reports an alarm or event to the client through the notification mechanism.
      This allows the client to learn the status of the managed device.
