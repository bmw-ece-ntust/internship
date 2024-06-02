<div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/ymDsyon.png" alt="Chart" width="500
    " style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>
<div style="height: 50px;"></div>

# O1 Interface
The O1 interface refers to the interface plane inteface between the SMO and other ORAN components. This interface enables the SMO to access ORAN network functions.

**Key ponts for O1 Interface:**
- O1 is the interface between SMO and near-RT RIC, the O-CU, the O-DU, O-RU
- O1 interface ensure the operation and management e.g. FCAPS, software Management, file management of O-RAN components
- O1 interface does use standard protocols SSH, TLS, NETCONF
    > NETCONF (Network Configuration Protocol) is a network management protocol developed by the IETF (Internet Engineering Task Force). It provides mechanisms to install, manipulate, and delete the configuration of network devices. NETCONF is designed to support network automation and programmability, facilitating more efficient and reliable network management.
    
- O1 interface use Yang Data model
  > More about YANG data model: https://info.support.huawei.com/info-finder/encyclopedia/en/YANG.html

## Services Supported by the O1 Interface
### Provisioning management services
Provisioning management services help a **Provisioning MnS Consumer** (like a network management system or orchestration tool) to change settings and manage various aspects of network devices, referred to as **Provisioning MnS Providers** (like routers, switches, or other network equipment). These services enable:
1. **Configuring Devices**: The consumer can set up, change, or read the settings of these network devices.
2. **Reporting Changes**: The network devices can inform the consumer about any configuration changes that happen.

>The managed object often refered as **Managed Object Instance (MOI)**, which represents a specific instance of a managed object within a network device or service that is managed via NETCONF. Managed objects are the various configurable and monitorable elements in a network device, such as interfaces, routing tables, and other resources.
>
>**Example:**
>Suppose you have a router with multiple interfaces. Each interface (e.g., eth0, eth1) can be considered a managed object instance. NETCONF operations can be used to configure these interfaces (e.g., setting IP addresses, enabling/disabling interfaces), read their current configurations, or delete configurations.

The NETCONF protocol is used for these interactions to:
- Create new settings or configurations on the devices.
- Delete existing settings or configurations.
- Modify existing settings.
- Read or check the current settings.

#### NETCONF
General NETCONF Requirements:
1. **Mandatory NETCONF Operations**:
   - **Required Operations**: Both the provisioning management service provider and consumer must support the following operations as defined in RFC 6241:
     - `get`
     - `get-config`
     - `edit-config`
     - `lock`
     - `unlock`
     - `close-session`
     - `kill-session`
   - **Optional Operations**: Other operations are not mandatory.

2. **Mandatory NETCONF Capabilities**:
   - **Required Capabilities**: Both the provider and consumer must support:
     - `writable-running`
     - `rollback-on-error`
     - `validate`
     - `xpath`
  
   - **Optional Capabilities**: Other capabilities are not mandatory.

3. **Datastore Requirements**:
   - **Running Datastore**: Both the provider and consumer must support a running datastore.
   - **Candidate Datastore**: Support for a candidate datastore is optional.

4. **YANG Support**:
   - Both the provider and consumer must support YANG 1.1 as defined in RFC 7950, including compatibility with YANG Version 1.

5. **NETCONF Session Management**:
   - The provider must be able to establish a NETCONF session with an authorized consumer upon request.
   - The provider must maintain the session until the consumer terminates it.
   - The provider must be able to terminate the session upon request from the consumer.

6. **Persistence of Provisioning Results**:
   - The provider must ensure that provisioning operation results persist even after a reset.

7. **NETCONF Security**:
   - Both the provider and consumer must support NETCONF over SSH or NETCONF over TLS.

- **Create MOI**
  
   The Provisioning MnS Consumer sends a synchronous request to the Provisioning MnS Provider to create a new MOI and set its initial attribute values. The synchronous nature of the request ensures that the consumer waits for the provider to complete the operation and confirm its success before proceeding with any further actions.

   <div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/bxRLaGJ.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   </div>

- **Modify MOI Attributes**
- **Delete MOI**
- **Read MOI Attributes**
- **Notify MOI Attribute value changes**
- **Notify MOI creation**
- **Notify MOI deletion**
- **Notify MOI changes**
#### Subscription Control
Subscription Control allows a MnS Consumer to subscribe to notifications emitted by a MnS Provider.

---
---

### Fault supervision management services
This service allows the Fault Supervision MnS Provider provider to report errors and events to the Fault Supervision MnS Consumer and allows the consumer to do fault supervision on the provider, such as getting the alarm list

#### **Fault Notofication**
  
  This allows the provider to send an asyc notification to the consumer when an alarm occurs, is cleared, or changes severity.

  - **Procedure**
   <div style="display: flex; justify-content: space-around;">
    <img src="https://imgur.com/aIeu06C.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   </div>

  1. **Subscribe Request Initiation**:
      - The authorized consumer sends a subscribe request to the FS Data Report management service producer.
      - The request includes the subscriber’s URI and a filter specifying the types of alarms the consumer is interested in.

  2. **Subscription Request Verification**:
      - The FS Data Report management service producer checks whether the subscribe request can be accepted based on its criteria.

  3. **Subscription Creation**:
      - If the request is accepted, the FS Data Report management service producer creates the necessary subscription resources for the subscriber.
      - If new types of alarms need to be collected from constituent Managed Object Instances (MOIs), the producer updates the filter to include these new alarm types and acts as a consumer to request subscriptions from each relevant MOI.

  4. **Subscription Confirmation**:
      - Upon successfully creating the subscription resources, the FS Data Report management service producer sends a success response back to the authorized consumer.

  5. **Alarm Supervision and Collection**:
      - The FS Data Report management service producer monitors each MOI under fault supervision.
      - It checks for conditions matching the filter specified in the subscribe request, including any alarms received from constituent MOIs.
      - When alarms from the constituent MOIs are received, the producer generates or updates the alarm information related to the subscription.

  6. **Notification to Subscriber**:
      - The FS Data Report management service producer sends notifications of the alarms to the authorized consumer as they occur.

   **Supported Operations:**

   - notifyNewAlarm
   - notifyChangedAlarm
   - notifyClearedAlarm
  

   There are two kinds of notification format, **3GPP** and **VES** format, indicated by **notifFormatCapabilities** and **notifFormatConfig**

---
   #### **Fault Supervision Control**
   Since 3GPP relase 16 and onwards, management services usecase will be using IOC with attributes that can be get or set. For fault Supervision, `AlarmList` is used to store and manage alarm records.

   >**More about AlarmList:**
      >
      >The AlarmList represents the capability to store and manage alarm records. It can be name-contained by SubNetwork and ManagedElement. 
      >
      >The management scope of an AlarmList is defined by all descendant objects of the base managed object, which is the object name-containing the AlarmList, and the base object itself.
      >
      >AlarmList instances are created by the system or are pre-installed. They cannot be created nor deleted by MnS consumers.
      An instance of SubNetwork or ManagedElement has at most one name-contained instance of AlarmList. 
      >
      >When the alarm list is locked or disabled, the existing alarm records are not updated, and new alarm records are not
      added to the alarm list.
      >    <div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/uYy3BPq.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>
      >Notice there is an alarmRecords instance within the alarmList, this contains alarm information of an alarmed object instance. A new record is created in the alarm list when an alarmed object instance generates an alarm and no alarm record exists with the same values for objectInstance, alarmType, probableCause and specificProblem. When a new record is created the MnS producer creates an alarmId, that unambiguously identifies an alarm record in the AlarmList.
      >
      > Alarm records are maintained only for active alarms. Inactive alarms are automatically deleted by the MnS producer from the AlarmList. Active alarms are alarms whose
      >
      >- perceivedSeverity is not "CLEARED", or
      >- perceivedSeverityis"CLEARED" and its ackState is not "ACKNOWLEDED"
      >  <div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/S4YfAdg.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---
---

### Performance assurance management services
Performance Assurance Management Services allow a Performance Assurance MnS Provider to report file-based (bulk) and/or streaming (real time) performance data to a Performance Assurance MnS Consumer and allows a Performance Assurance MnS Consumer to perform performance assurance operations on the Performance Assurance MnS Provider, such as selecting the measurements to be reported and setting the frequency of reporting.

#### Performance Data File Reporting
Performance Assurance MnS Provider sends asynchronous FileReady notification event to Performance Assurance MnS Consumer sent when PM File(s) is ready for upload. The FileReady notification contains information needed to 
retrieve the file such as filename and the location where the file can be retrieved.

Performance Assurance MnS Consumer uploads PM File(s) from the location specified in the notifyFileReady notification.
<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/zaCqxvl.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

Like the notification format, there are two kinds of notification format, **3GPP** and **VES** format, indicated by **notifFormatCapabilities** and **notifFormatConfig**. This information will be sent in JSON encoding using REST/HTTPS.

The performance data reporting service producer generates performance data files for consumers and sends "notifyFileReady" or "notifyFilePreparationError" notifications to subscribed consumers. The method by which the measurement job control service producer provides results to the performance data reporting service producer is out of scope for this specification. The performance data reporting service producer allows file access via FTP or SFTP, always acting as the server, while the consumer acts as the client.

**FIle content description:**

| File Content Item           | Description                                                                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| measDataCollection          | Identifies the file as a collection of measurement data. Contains a header ("measFileHeader"), measurement result items ("measData"), and a footer ("measFileFooter").                                                                                |
| measFileHeader              | Measurement result file header with version, name, type, vendor name of the sender, and a time stamp ("collectionBeginTime").                                                                                                                        |
| measFileFooter              | Measurement result file footer with a time stamp marking the end of the measurement collection interval.                                                                                                                                            |
| senderName                  | Uniquely identifies the performance data reporting service producer.                                                                                                                                                                                |
| senderType                  | Identifier of the type of performance data reporting service producer.                                                                                                                                                                               |
| measData                    | Sequence of zero or more measurement result items, can be empty. Contains measured entity ID ("measuredEntityId") and measurement results ("measInfo").                                                                                              |
| fileFormatVersion           | Identifies the file format version used by the sender.                                                                                                                                                                                               |
| collectionBeginTime         | Time stamp marking the start of the first measurement collection interval.                                                                                                                                                                           |
| measuredEntityUserName      | User-defined name for the measured entity. May be empty.                                                                                                                                                                                             |
| measuredEntityDn            | Distinguished Name (DN) for the measured entity, unique across the operator's network.                                                                                                                                                               |
| measuredEntitySoftwareVersion | Software version for the measured entity, allows post-processing systems to handle vendor-specific measurements.                                                                                                                                    |
| measInfo                    | Sequence of measurements, values, and related information, including measurement types ("measTypes") and results ("measValues"), time stamp ("measTimeStamp"), and granularity period ("granularityPeriod").                                         |
| measInfoId                  | Optional tag name associated with a set of measurements defined by a measInfo property.                                                                                                                                                               |
| measTimeStamp               | Time stamp marking the end of the granularity period.                                                                                                                                                                                                |
| jobId                       | Optional item representing the measurement job associated with the measurement result in the file.                                                                                                                                                    |
| granularityPeriod           | Granularity period of the measurement(s) in seconds.                                                                                                                                                                                                 |
| reportingPeriod             | Reporting period of the measurement(s) in seconds.                                                                                                                                                                                                   |
| measTypes                   | List of measurement types corresponding to the measurement values ("measValues").                                                                                                                                                                    |
| measValues                  | List of measurement results for the measured resource, including resource ID ("measObjInstId"), result values ("measResults"), and a reliability flag ("suspectFlag").                                                                                 |
| measObjInstId               | Local distinguished name (LDN) of the measured object, empty if "measuredEntityDn" specifies the DN completely.                                                                                                                                      |
| measResults                 | Sequence of result values for the observed measurement types, same order as measTypes. NULL value indicates the item is not applicable or could not be retrieved.                                                                                     |
| suspectFlag                 | Indicates data quality: FALSE if reliable, TRUE if not. Default is "FALSE", may be omitted if default.                                                                                                                                               |
| timestamp                   | Time stamp marking the end of the measurement collection interval. Minimum information: year, month, day, hour, minute, and second.                                                                                                                  |

**5G Performance Reporting:**

3GPP defined 5G performance measurements are specified in 3GPP TS 28.552. In addition to these measurements, it is possible to have O-RAN defined measurements and vendor-supplied measurements. Section 2.3.4 provides requirements for O-RAN defined measurements, which are named with an "OR." prefix. Vendor-supplied measurements are named with a "VS." prefix.

---

#### Performance Data Streaming

In this part, the Performance Assurance MnS Provider streams high volume streaming performance measurement data to Performance Assurance MnS Consumer at a configurable frequency. A secure WebSocket connection is established between the Performance Assurance Provider and the Performance Assurance Consumer. The connection will support. Each stream of PM data is configured as a PerfMetricJob

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/WDysF0C.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>


**NEEDS MORE**

---

#### Measurement Job Control

Since 3GPP relase 16 and onwards, performance assurance control will be using IOC with attributes that can be get or set using generic provisioning mechanisms in the Measurement Job Control Service. For Performance Assurance, this includes operations such as:

- Create Measurement Job
- Terminate Measurement Job
- Query Measurement Job
- Suspend Measurement Job
- Resume Measurement Job

Measurement jobs can be created and terminated by creating and deleting a PerfMetricJob MOI. Measurement jobs can be queried by retrieving the attributes of a PerfMetricJob MOI. Measurement jobs can be temporarily suspended or resumed by modifying the `administrativeState` attribute of a PerfMetricJob MOI to `LOCKED` or `UNLOCKED`.

> **About PerfMetricJob**
>
> This IOC represents a performance metric production job. It can be name-contained by SubNetwork, ManagedElement, or ManagedFunction.
> <div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/8iTgmzz.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>
>The attributes `objectInstances` and `rootObjectInstances` allow for restricting the scope. If `objectInstances` is present, only those identified instances are scoped. If `rootObjectInstances` is present, subtrees with the specified root objects are scoped. Both attributes can be present simultaneously, combining their scopes. Scoping an object instance by both attributes is not an error.
>
>For performance metrics requiring multiple managed objects (e.g., KPIs), the MnS consumer must ensure all required objects are scoped, or the PerfMetricJob creation request will fail.
>
>The attribute `reportingCtrl` specifies the reporting method and control parameters, with three available methods: file-based reporting (MnS producer selects file location), file-based reporting (MnS consumer selects file location), and stream-based reporting.
>
>A PerfMetricJob creation request will fail if the requested performance metrics, granularity period, reporting method, or their combination is unsupported by the MnS producer.
>
>  Creation and deletion of PerfMetricJob instances by MnS consumers is optional; if not supported, instances may be system-created or pre-installed.



---
---

### Trace Management Services

Trace management services allow a Trace MnS Provider to report file-based or streaming trace records to the Trace 666 MnS Consumer. Trace Control provides the ability for the Trace Consumer to start a trace session by configuring a Trace Job via the Trace Control IOC or by establishing a trace session that will propagate trace parameters to other trace  management providers via signaling.

>**Trace** refers to a diagnostic tool used to monitor and analyze the performance and behavior of network elements and services.

**Trace Levels:**
- Maximum
- Minimum
- Medium
- MaximumWithoutVendorSpecificExtension
- MinimumWithoutVendorSpecificExtension
- MediumWithoutVendorSpecificExtension.

>The first three levels allow for vendor specific information to be traced and sent in the trace report file.



Trace Sessions are configured on the provider with information on where and how to send the trace information to the consumer. The Provider produces trace records within the trace sessions as soon as the trace triggeer mechanism triggered, which is provided to the consumer until the trace sesison is terminated.

The records could be file or s=be streamed, if it is file, it will be available to the consumer within a time delay, whereas if it is streamed it will be sent using WebSocket to the consumer

**Supported Trace Management Servcie:**
- Call Trace
- Minimization of Drive Testing (MDT)
- RRC Connection Establishment Failure (RCEF)
- Radio Link Failure TCE (RLF)
  
---
---

### File Management Services
File management services allow a File Management MnS Consumer to request the transfer of files between the File  Management MnS Provider and the File Management MnS Consumer.

#### FIle Ready Notification
Notifies a File Management MnS Consumer that a file is available for upload from the File Management MnS Provider. In general, the provider sends a notifyFileReady for the files that the consumer has configured for the provider to collect periodically.
<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/cYfCjCT.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---

#### List Available FIles
File Management MnS Consumer queries the File Management MnS Provider to identify the files avaailable in the provider
<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/TiFJ3OO.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---

#### File Transfer by File Management MnS Consumer
This provides file transfer capability with the consumer acting as the client and the provider as the server. This file transfer process is carried through SFTP or FTPeS The File Management MnS Consumer may perform this action as a result of:
1. Notification from the File Management MnS Provider to the File Management MnS Consumer informing that a file(s) is available.
2. Querying the File Management MnS Provider for the list of available files (see section 2.5.2).
3. Need to transfer a file from a known location on the File Management MnS Provider.
4. Need to transfer a file to a known location on the File Management MnS Provider. Examples of files that could be transferred include:
    - Beamforming configuration file (opaque vendor-specific data)
    - Machine learning data
    - Certificates

**Usage cases:**

Case 1: The File Management MnS Consumer determines that a file should be transferred from the location provided by the File Management MnS Provider as a result of receiving a notifyFileReady notification from the File Management MnS Provider (described in 2.5.1).

Case 2: The File Management MnS Consumer determines that a file should be transferred from the File Management MnS Provider as a result of receiving a list of available files from the File Management MnS Provider (described in 2.5.2).

Case 3: The File Management MnS Consumer determines that a file should be transferred from a known location on the File Management MnS Provider.

Case 4: The File Management MnS Consumer determines that a file should be transferred to a known location on the File Management MnS Provider.

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/ezvTR9f.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---

#### Download Files
The File Management MnS Consumer can ask the The File Management MnS Provider to download certain files such as 
- Software file to upgrade the software version executed on the File Management MnS Provider
- Beamforming configuration file (opaque vendor-specific data)
- Machine learning data
- Certificates
  
In this process, the provider will download the required files from an external location specified by the consumer via a secure connection an then report the progress event to the consumer

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/jFos466.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---
---

### Heartbeat management services
Heartbeat MnS allow a Heartbeat MnS Provider to send heartbeats to the Heartbeat MnS Consumer and allow the Heartbeat MnS Consumer to configure the heartbeat services on the Heartbeat MnS Provider.

> **More about heartbeat:**
>
> Heartbeat is is a signal sent at regular intervals from one component (the Heartbeat MnS Provider) to another (the Heartbeat MnS Consumer) to indicate that the provider is operational and functioning correctly. This mechanism is commonly used in various systems to monitor the health and status of a component, ensuring that it is alive and able to communicate. If the consumer stops receiving these heartbeat signals, it can assume that the provider has failed or is not working properly and can take appropriate actions, such as triggering alerts or attempting to restart the service.

#### Heartbeat Notification
Heartbeat MnS Provider sends asynchronous heartbeat notifications to Heartbeat MnS Consumer at a configurable frequency to allow Heartbeat MnS Consumer to supervise the connectivity to the Heartbeat MnS Provider.

**Immideate notification:**
<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/eh8xbCH.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

**Periodic notifiation:**
<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/ETkTwrt.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---
#### HEartbeat COntrol
MnS consumers use heartbeat notifications to monitor communication channels with data report MnS producers emitting notifications like notifyNewAlarm and notifyFileReady. A HeartbeatControl instance manages the emission of these notifications, with recipients specified by the notificationRecipientAddress attribute of the associated NtfSubscriptionControl instance.

The MnS consumer managing the HeartbeatControl instance and the one receiving the notifications may differ. To emit heartbeat notifications, a HeartbeatControl instance must be created. If the instance's heartbeatNtfPeriod attribute is non-zero upon creation, a heartbeat notification is emitted immediately. A zero value does not trigger an emission. Deleting the instance does not trigger an emission either.

Creation and deletion of HeartbeatControl instances by MnS consumers are optional and may be handled by the system or be pre-installed if not supported by the consumer.

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/mvBsFMF.png" alt="Chart" width="600" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/i8O1lT4.png" alt="Chart" width="600" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---
---

### PNF Startup and Registration Management Services
PNF Startup and Registration management services allow a physical PNF Startup and Registration MnS Provider to
1106 acquire its network layer parameters either via static procedures (pre-configured in the element) or via dynamic procedures (Plug-n-Play) during startup. 
During this process, the PNF Startup and Registration MnS Provider acquires the IP address of the PNF Startup and Registration MnS Consumer for registration. Once registered, the MnS Consumer can bring the MnS Provider to an operational state.

> **More About PNF:**
> 
> PNF refers to a network function that is implemented on a physical device, as opposed to a virtualized network function (VNF) which runs on virtualized infrastructure.

#### PNF Plug-and-Play
PNF Plug-n-Play (PnP) scenario enables a PNF ME to obtain the necessary start-up configuration to allow it to register with a PNF Startup and Registration MnS Consumer for subsequent management.

1. **Step 1: Obtain SeGW IP Address via FQDN Resolution**
   - If the IP address of the Security Gateway (SeGW) is unknown to the eNB but the Fully Qualified Domain Name (FQDN) of the SeGW is known, the eNB sends a request containing the FQDN of the SeGW to the DNS server.
   - The DNS server resolves the FQDN of the SeGW into an IP address and provides it to the eNB.

2. **Step 2: Establish Secure Tunnel to SeGW**
   - The eNB establishes a secure tunnel to the SeGW using the IKEv2 protocol.
   - Sub-steps include:
     - Using the operator certificate to establish a secure connection.
     - Receiving the inner IP configuration from the SeGW in the Configuration Parameters of IKEv2.
     - Optionally receiving the IP addresses of secure DNS servers and DHCP server from the SeGW.

3. **Step 3: Initial IP Autoconfiguration**
   - If a VLAN ID is available, the eNB uses it; otherwise, it uses the native VLAN for PnP traffic.
   - The eNB invokes the "Initial IP Autoconfiguration" procedure to acquire its IP address through stateful or stateless IP Autoconfiguration.

4. **Step 4: Certificate Enrolment**
   - The eNB invokes the "Certificate Enrolment" procedure to provision operator certificates, possibly using the factory-installed vendor certificates.

5. **Step 5: Establish Secure Connection to OAM SeGW**
   - The eNB connects to the OAM SeGW by invoking the "Establishing Secure Connection" procedure.

6. **Step 6: Establish Connection to EM**
   - The eNB invokes the "Establishing Connection to EM" procedure, where the EM may provide new configuration instructions.
   - The configuration may include addresses or FQDNs of different SeGWs or EMs to be used.

7. **Step 7: Configuration Alignment**
   - If the configuration obtained in the previous step differs from the connected SeGW and EM, the eNB may execute steps to align the configurations.

This procedure ensures that the eNB can establish secure connections to the necessary network elements, receive configuration information, and become operational in a multi-vendor plug-and-play environment.

---
#### PNF Registration
PNF Startup and Registration MnS Provider sends an asynchronous pnfRegistration event to a PNF Startup and Registration MnS Consumer after PnP to notify PNF Startup and Registration MnS Consumer of new PNF Startup and Registration MnS Provider to be managed.

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/Q8hdHyi.png" alt="Chart" width="600" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

**Pre-cond:** PNF completes Plug-n-Play.

---
---
### PNF Software Management Service
Software management services enable a PNF Software MnS Consumer to request a physical PNF Software MnS Provider to download, install, validate, and activate a new software package. Additionally, it allows a physical PNF Software MnS Provider to report its software versions. O-RAN will collaborate with 3GPP to enhance the specifications for PNF Software Management. Until these enhancements are implemented, O-RAN PNF Software Management will be outlined in this specification.

#### Software Naming and Packaging
PNF Software Packages are vendor-specific in naming, content, and format, and do not require standardization within O-RAN. Each package may contain one or more files, some of which may be optional for the PNF. The PNF is responsible for determining which files it needs to download based on its awareness of the package's content and format.

The softwarePackage Managed Object Class (MOC) encompasses attributes such as software package name, version, fileList, integrityStatus, runningState, vendor, productName, and softwareType. This MOC applies to both VNFs and PNFs, replacing the legacy term "software slot."

Each PNF creates one instance of softwarePackage for each supported software package concurrently. Typically, a PNF will have two instances for operational software, one with runningState = active and one with runningState = passive. Some PNFs may also have a read-only instance for factory software. O-RAN may support PNFs with multiple passive slots, resulting in multiple instances with runningState = passive in the inventory query result.

---

#### Software Inventory
The PNF Startup and Registration MnS Consumer initiates a request known as a Software Inventory Request to the PNF Software MnS Provider. This request is aimed at obtaining information about the software packages currently available on the PNF (Physical Network Function) managed by the MnS Provider. The MnS Consumer sends this request to gather details such as the names, versions, and other relevant attributes of the software packages installed on the PNF.
<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/M47fPKI.png" alt="Chart" width="400" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---

#### Sofrware Download

Software Download triggers the download of a specific software package to the PNF Software MnS Provider. This
 download service includes integrity checks on the downloaded software and the installation of the software into the
 software slot corresponding to the softwarePackage MOI.

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/pWOGoMt.png" alt="Chart" width="600" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---

#### Software Activation Pre-Check
This is an additional step that is used for chekcing whether PNF Software MnS Provider is in a good state to activate the new software and provide information
1270 needed for planning the timing of the software replacement prior to software activation\

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/0NPtMyM.png" alt="Chart" width="600" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---

#### Software Activation
PNF Software MnS Consumer triggers the activation of a software package on the PNF Software MnS Provider including data migration and reset if needed.

<div style="display: flex; justify-content: space-around;"><img src="https://imgur.com/57I2wgL.png" alt="Chart" width="600" style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>
<!-- 
### Heartbeat management services
### Start-up and registration management services for Physical Network Functions (PNFs)
### Software management services for PNFs
### CNFs an VNFs Life Cycle -->

