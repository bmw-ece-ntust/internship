## :BOOKS: NETCONF
Netconf or The Network Configuration Protocol is a protocol used for managing network devices, allowing for configuration changes, monitoring of device state, and retrieving operational data. Netconf uses Extensible Markup Language or XML and it is developed by the IETF. In this note we will use the term of client and server. 

Four layers of netconf is :
1. Secure Transport Layer: This layer ensures the secure transmission of data between the NETCONF client and server. It typically involves protocols like SSH (Secure Shell) or TLS (Transport Layer Security) to provide encryption, authentication, and integrity checking of the data being transmitted.
2. Message Layer: This layer defines the format and structure of the messages exchanged between the NETCONF client and server. It includes the headers, metadata, and any other information necessary for the communication to occur. Messages in NETCONF are typically XML-based.
3. Operation Layer: This layer specifies the operations that can be performed by the NETCONF protocol. These operations include actions such as querying device configuration, modifying configuration settings, retrieving operational data, and other management tasks.
4. Content Layer: This layer pertains to the actual data being exchanged between the NETCONF client and server. It includes the configuration data, operational data, and any other information relevant to the network device being managed.


-Client 
can be a script or an application running on an NMS(Network Management System). It manages network devices using netconf, sends RPC (Remote Procedure Call) request to a netconf server to query (a request for information or data retrieval from a database or system), and learns the status of a managed device based on the alarms

-Server 
typically a network device which maintains information about managed devices and responds to the client-initiated requests. Netconf server will parses request from client and sends a reply to the client. It could also reports an alarm through notification mechanism to the client. 

## NETCONF Session Process
￼<img width="376" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/4ecae608-ac7b-41a8-9001-3f8403ba42a5">


* <rpc> : Client send request to Server.
* <rpc-reply>: Sent by a server in response to each <rpc>request.
    * Define two element <ok> (success), <rpc-error> (error)
 
# Configuration Datastores
<img width="367" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/0a29bbb8-6557-4ce0-aa40-00f5781b903b">

* <running/>: Stores all configurations that are currently active on a network device.
* <candidate/>: Stores configuration data that is about to be committed to <running/> on a device.
* <startup/>: (Similar to a saved configuration file). Stores the configuration data to be loaded during device startup.

# Workflow

￼<img width="363" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/ef47e0e7-4720-4767-8dd1-0aeece4250f5">


