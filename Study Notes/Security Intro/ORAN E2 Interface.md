# ORAN E2 General Aspects and Principles 


## E2 Interface
This is the **interface** that connects **E2 Nodes** and the **Near RT RIC**. Its main objective is to provide the Near RT RIC the necessary **E2 Node data** and **control** the selected **RAN function** in the E2 Node.

Principles:
- Connects endpoints in **point-to-point** manner.
- **Control signal** exchange.
- Supports **interface management procedures** based on principles from **3GPP RAN interfaces**
- Send predefined info to the Near RT RIC based on **preconfigured trigger event**
- Send **UE ID info** to the Near RT RIC based on preconfigured trigger event
- Enables the Near RT RIC to direct the E2 Nodes to **suspend an RRM procedure** by **interrupting** its local process and forwarding the necessary info to Near RT RIC for processing.
- Provides the E2 nodes with set of **policies** when an **event** occurs
- Supports the E2 nodes the ability to **notify** the Near RT RIC of what **functionalities** it supports.
- Supports the ability to **query** the E2 node for relevant **UE** or **RAN information**.

### RIC Services
---
#### REPORT

  **Gathering and sending information** from E2 Nodes to the Near RT RIC. Includes **performance metrics** and **network status**.
  
Steps: 
- Near RT RIC uses RIC Subscription procedure send configuration the E2 Node so that it sends a report message to the Near RT RIC. This will be executed with each occurent of RIC trigger event.
- When an RIC trigger event is detected, the E2 Node will send a RIC Indication Repoprt
- After this E2 Node continues its prev. process
  
<div style="display: flex;">
    <img src="https://imgur.com/9mpjtOs.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>

---

#### INSERT
**Injecting specific instructions** or configurations into the E2 Nodes from the Near RT RIC. Includes **setting parameters** and **updating configurations**.

Steps: 
- Near RT RIC uses RIC Subscription procedure send configuration the E2 Node about the INSERT action which will be performed with each occurent of an event.
- During normal functioning of an associated procedure instance in the E2 Node, a trigger event is detected.
- E2 Node suspends associated procedure instance for up to a defined Time to Wait period.
-  E2 Node sends RIC INDICATION message to Near-RT RIC containing the requested INSERT information along with the originating Request ID and information to identify the suspended associated procedure instance.
- According to the Time to Wait timer state, arrival of RIC CONTROL procedure, and Subsequent Action parameter in the RIC Subscription, the E2 Node may then
    - a. RIC CONTROL REQUEST message arrives in time
    - b. The associated Time to Wait timer expires and Subsequent Action Type set to Continue
    - c. The associated Time to Wait timer expires and Subsequent Action Type set to Halt
  
    <div style="display: flex; ">
    <img src="https://imgur.com/ekm3Dab.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   </div>

#### Control 
**Actively manage and direct** functions of E2 Nodes. Includes **suspending or modifying RRM procedures**, **traffic management**, and **adjusting radio resources**.


  - Near-RT RIC initiates an action.
  - Near-RT RIC sends a RIC CONTROL REQUEST message to the E2 Node. This message may include details to identify any previously suspended procedure and can request an acknowledgement from the E2 Node. If an acknowledgement is requested or not specified, the Near-RT RIC sets the TRICcontrol timer.
  - The E2 Node validates the request, cancels any associated Time to Wait timer if previously set, and starts or resumes the related procedure.
  - The E2 Node responds as follows:
    - If the control service is successfully executed, and an acknowledgement was requested or not specified, the E2 Node sends a RIC CONTROL ACKNOWLEDGE message, optionally including the RIC Control Outcome with details of the control service result.
    - If the control service fails or the request is invalid, the E2 Node sends a RIC CONTROL FAILURE message with the reason for the failure or rejection, and optionally includes the RIC Control Outcome explaining the failure.
  - The Near-RT RIC cancels the TRICcontrol timer if it was previously set.

    <div style="display: flex;"> <img src="https://imgur.com/3dzqgjC.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"> </div>
    <div style="height: 50px;"></div>
    <div style="display: flex;"> <img src="https://imgur.com/m8J1sK2.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"> </div>
    <div style="height: 50px;"></div>
    <div style="display: flex;"> <img src="https://imgur.com/dmARFy3.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>


---

#### POLICY 
**Implementing and enforcing rules** within E2 Nodes. Governs **node behavior** under certain conditions.

  - Near-RT RIC configures a **RIC Subscription** in the E2 Node with details to set up a **POLICY** for each trigger event.
  - During normal operation, a **trigger event** is detected by the E2 Node.
  - E2 Node adjusts the ongoing call process based on the **POLICY** description.
  - The associated procedure continues in the E2 Node.
  - If a dedicated RIC Subscription was previously set, the E2 Node may send a **REPORT** with information on the procedure outcome.
    
      <div style="display: flex; ">
    <img src="https://imgur.com/dmARFy3.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"> </div>

---
#### QUERY
**Request specific information** from E2 Nodes. Includes **details about user equipment** and **network status**.
  - Near-RT RIC determines the need for **RAN and/or UE-related information** from the E2 Node.
  - Near-RT RIC sends a **RIC QUERY REQUEST** message to the E2 Node, specifying the information needed. The Near-RT RIC sets the **TRICquery** timer while awaiting a response.
  - E2 Node validates the request and attempts to retrieve the requested information.
  - E2 Node responds:
    - If successful, the E2 Node sends a **RIC QUERY RESPONSE** message containing the requested information.
    - If unsuccessful, the E2 Node sends a **RIC QUERY FAILURE** message with the reason for the failure.
    <div style="display: flex;">
    <img src="https://imgur.com/RCFjPop.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"></div>

---
---

### RIC service realizzartion and relationship with E2AP Procedures**
  
  <div style="display: flex;"><img src="https://imgur.com/9b8QblZ.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"> </div>

  - **RIC Subscription Procedure** (Near-RT RIC initiated)
    - Installs Event Trigger and sequence of Actions for REPORT, INSERT, and/or POLICY services.
    
  - **RIC Subscription Modification Procedure** (Near-RT RIC initiated)
    - Modifies Event Trigger and/or sequence of Actions for REPORT, INSERT, and/or POLICY services.
    
  - **RIC Subscription Modification Required Procedure** (E2 Node initiated)
    - Requests modification or removal of sequence of Actions for REPORT, INSERT, and/or POLICY services.
    
  - **RIC Subscription Delete Procedure** (Near-RT RIC initiated)
    - Deletes previously installed RIC Subscription.
    
  - **RIC Subscription Delete Required Procedure** (E2 Node initiated)
    - Indicates the need to delete one or more previously installed RIC Subscriptions.
    
  - **RIC Subscription Audit Procedure** (Near-RT RIC initiated)
    - Audits list of previously installed RIC Subscriptions.
    
  - **RIC Indication Procedure** (E2 Node initiated)
    - Carries outcome of REPORT and INSERT services.
    
  - **RIC Control Procedure** (Near-RT RIC initiated)
    - Initiates CONTROL service.
    
  - **RIC Query Procedure** (Near-RT RIC initiated)
    - Requests RAN and/or UE-related information from E2 Node.
---
---
### Combining RIC Services within a common Subscription

RIC Services defined above can be combined within a common subscriptopn with each service implemented as part of sequence of actions
Where appropriate in these cases, successive REPORT or INSERT messages sent to Near-RT RIC under the same subscription event trigger would contain the same assigned Subscription Request identifier, the same optional sequence number and each message with the unique assigned Action identifier. For example:
- **POLICY then REPORT**: When the defined Event Trigger occurs, the E2 Node is instructed to first execute a specified POLICY and then send a REPORT message.

- **REPORT then REPORT**: Upon the defined Event Trigger, the E2 Node is instructed to first send a REPORT message, followed by a second REPORT message containing different information.

### Combining RIC Servioces as a sequence of RIC services
RIC services may be combined using a sequence of different RIC services implemented using a procedure executed within the Near-RT RIC.

- **REPORT followed by POLICY**: When the Event Trigger occurs, the E2 Node sends a REPORT message. The Near-RT RIC uses the information from one or more REPORT messages to potentially establish or modify a RIC POLICY service.

- **INSERT followed by CONTROL**: When the Event Trigger occurs, the E2 Node sends an INSERT message with details about a suspended procedure instance. The Near-RT RIC then sends a CONTROL message to address the suspended procedure instance.

- **REPORT followed by CONTROL**: When the Event Trigger occurs, the E2 Node sends a REPORT message. The Near-RT RIC uses the information from one or more REPORT messages to potentially initiate a CONTROL procedure.

---
---

### RAN Functions E2 Service Model

- **RAN Function Definition**: Specifies the **RAN Function Name** and describes the **RIC Services** currently configured over the E2 interface.

- **RIC Event Trigger Definition Approach**: Outlines the method for setting or modifying the **RIC Event Trigger Definition** in the RAN Function during **RIC Subscription** and **RIC Subscription Modification** procedures for REPORT, INSERT, and/or POLICY services.

- **RIC Action Definition Approach**: Details the method for setting or modifying the sequence of **RIC Actions** in the RAN Function during **RIC Subscription** and **RIC Subscription Modification** procedures for REPORT, INSERT, and/or POLICY services.

- **RIC Indication Header and Message Approach**: Describes the method used in the **RIC Indication Procedure** for REPORT and INSERT services.

- **RIC Control Header and Message Approach**: Explains the method used in the **RIC Control Procedure** for the CONTROL service.

- **RIC Call Process ID Approach**: Outlines how the **E2 Node** uses the **RIC Call Process ID** in the **RIC Indication Procedure** for INSERT services and the subsequent **RIC Control Procedure** for CONTROL services.

- **RIC Control Outcome Approach**: Details how the **E2 Node** handles outcomes in the **RIC Control Procedure** for CONTROL services.

- **RAN Function Policies**: Describes the policies supported by the RAN Function and the parameters used to configure these policies via the **RIC Service POLICY**.

- **RIC Query Header and Definition Approach**: Explains the method used by the Near-RT RIC in the **RIC Query Procedure** for the QUERY service.

- **RIC Query Outcome Approach**: Describes how the **E2 Node** handles outcomes in the **RIC Query Procedure** for the QUERY service.

---
---

### E2 Support Services:

Interface Management Services Supported by Global Procedures:

#### E2 Setup
**Establish a connection** between E2 Nodes and the Near RT RIC. E2 Node provides **capabilities and configurations**.
During this procedure, E2 Nodes provides:
- List of supported RIC services and mapping of services to functions within the E2 Node. This information is specific
to each RAN Function in the E2 node
- List of E2 Node configuration information. This information is specific to the E2 Node type (see clause 4.2) and
defined by the E2 Node system specifications

If this setup procedure fails, the Near-RT RIC may provide an alternative Transport Layer Information for the E2 Node to use when reinitiating the E2 Setup procedure.

  <div style="display: flex;"><img src="https://imgur.com/3drDiqw.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);"> </div>

---

#### E2 Reset
**Reset the interface** between an E2 Node and the Near RT RIC. Helps in **reinitializing the connection**.

Information previous exchanged during E2 Setup, E2 Node Configuration Update and RIC Service Update procedures shall be
maintained however the outcome of all previous RIC Subscription shall be deleted from the E2 Node and E2 Node gracefully
terminates any ongoing RIC Services.

<div style="display: flex; justify-content: space-around;">
  <img src="https://imgur.com/gQ2PSXk.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
  <img src="https://imgur.com/sEhELmT.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>


---

#### E2 Service Update procedure
Inform **any change of RIC services** and **mapping of services to functions** within the E2 Node. This procedure may also be initiated by the Near-RT RIC sending a RIC SERVICE QUERY message.

 <img src="https://imgur.com/4Lwnhhn.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
---

#### E2 Node Configuration Update
**Update configuration parameters** of an E2 Node. Ensures **current configurations**.

 <img src="https://imgur.com/rStQY7f.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

---


#### E2 Removal
**Disconnect an E2 Node** from the Near RT RIC. Ensures **graceful removal**.

<div style="display: flex; justify-content: space-around;">
  <img src="https://imgur.com/0VTiEsj.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
  <img src="https://imgur.com/3njsgEa.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>

---
---

### E2 Interface Signaling

#### E2 Control Plane Protocol (E2AP)

  <img src="https://imgur.com/GKfzOPa.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">


The transport network layer for the system is based on IP transport. To ensure reliable transport of signaling messages, the system incorporates IETF RFC 4960, which pertains to the Stream Control Transmission Protocol (SCTP), on top of the IP layer.

When configurations support multiple SCTP associations, the Near-RT RIC  can dynamically request to add or remove SCTP associations with the E2 Node. Among the established SCTP associations between the Near-RT RIC and the E2 Node, the Near-RT RIC can also request the E2 Node to restrict the use of certain SCTP associations for specific types of E2 signaling. If no such restrictions are specified, all types of E2 signaling can be transmitted via the SCTP association.

The application layer signaling protocol used is called E2AP. The Payload Protocol Identifier for E2AP assigned by IANA is 70, and this identifier is used in all deployment configurations as described in the specification. Identifiers 71 and 72 are also assigned by IANA for E2AP but are reserved for future use.

Since IANA did not assign a specific SCTP Destination Port number for the E2AP protocol, the E2 Node and the Near-RT RIC must rely on their configurations to select an appropriate port number for their communications.

---

#### Multiple TNLA over E2

The Near-RT RIC and E2 Node supports multiple TNL associations over E2 interface.

An initial TNL association is established during E2 Setup procedure with E2 Node initiating SCTP connection. This TNLA will be used for RIC Services and E2 Support functions.

TNLA may be added, modified or removed on subsequent E2 Connection Update and E2 Node Configuration Update, with the E2 Node initiating STCP connection where requiered

If the Near-RT RIC request to add additional STCP association, it will send an additional STCP endpoints using the E2 Connection Update. The STCP dest port numbermay be the same from the initial E2 Setup or any dynamic port value.

Within many STCP associations, a single association should be reserved for E2AP elementary procedures for E2 Support Function signaling with the possibility of fali-over to new association


In setups allowing multiple SCTP endpoints per E2 node, when an additional SCTP association is needed, the E2 Node Configuration Update procedure is initiated. This occurs after the TNL association becomes operational on an already set up E2 interface. The E2 node utilizes an existing SCTP endpoint of the Near-RT RIC for establishing the new association, associating the TNLA with the E2 interface using the provided Global E2 Node ID. To remove additional SCTP associations, the E2 node utilizes the E2 Node Configuration Update procedure.

The RIC Subscription TNLA binding links a specific TNL association with the RIC Service signaling of a particular RIC Subscription. Once established, the Near-RT RIC can modify this binding by transmitting the RIC Subscription's E2AP message to the E2 Node through a different TNLA. The E2 Node is responsible for updating the RIC Subscription TNLA binding with the new TNLA. Additionally, the E2 Configuration Update procedure enables the E2 Node to notify the Near-RT RIC of the removal of specified TNLAs.

In a Near-RT RIC and E2 Node pair:
- One pair of stream identifiers is exclusively reserved for E2 Support Function signaling
- For RIC Service signaling, at least one pair of stream identifiers across one or multiple SCTP associations is reserved, with multiple pairs recommended for flexibility,
- Each RIC Subscription's signaling utilizes one SCTP association and one SCTP stream. The association and stream remain unchanged until either the current association fails or an update to the RIC Subscription TNLA binding occurs.

<div style="display: flex; justify-content: space-around;">
  <img src="https://imgur.com/JnmtkYm.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
  <img src="https://imgur.com/LysbWxH.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
  <img src="https://imgur.com/dPdQDTa.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
</div>

---
---

### Security for the E2 Interface:


- The E2 interface must support confidentiality, integrity, replay protection, and data origin authentication.

- To safeguard traffic on the E2 interface, IPsec ESP implementation must be supported, following RFC 4303 and profiled by TS 33.210. Tunnel mode is mandatory, while transport mode is optional.
- Support for multiple IKE Security Associations (SAs), multiple IPsec SAs, and multiple IPsec SAs per IPsec tunnel (e.g., for rekeying) is required.
- IKEv2 certificate-based authentication implementation, conforming to TS 33.310, is mandatory. Certificates must adhere to the profile described by TS 33.310. IKEv2 support should align with the IKEv2 profile in TS 33.310.

#### IKEv2 Profile

For the IKE_INIT_SA and IKE_AUTH exchanges:
- RSA signatures for authentication must be supported.
- The identity of the CERT payload, including the end entity certificate, must be utilized for policy checks.
- Initiating/responding end entities must send certificate requests in the IKE_INIT_SA exchange for the responder and in the IKE_AUTH exchange for the initiator.
- Cross-certificates should not be sent by the peer end entity as they are pre-configured.
- Certificates in the certificate payload must be encoded as type 4 (X.509 Certificate – Signature).
- An end entity must rekey the IKE SA when any used end entity certificate expires.
(Note: Depending on DNS availability between peer end entities, the following rule is applied:)
- subjectAltName and IKEv2 policy should both contain IP address (if DNS is not available).
- subjectAltName and IKEv2 policy should both contain FQDN (if DNS is available).
