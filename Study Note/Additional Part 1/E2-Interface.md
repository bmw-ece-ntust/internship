# Part 1: E2 Interface related in Near-RT RIC Platform
- Goal : 
    - [x] Learning E2 Interface
    - [x] Learning E2 Service Model
- Useful Links:
    - [O-RAN.WG3.E2AP-v02.01](https://www.o-ran.org/specifications)
    - [ORAN-WG3.E2SM-v02.01](https://www.o-ran.org/specifications)

- Outcome (Study Note) : 
    - Learn about E2 Interface
    - Learn about E2 Application Procedure
    - Learn about E2 Service Model

***

## I. E2 Interface
### A. General
**What is E2?**
* E2 stands for RAN Intelligent Controller (RIC) Control Plane Interface.
* E2 is a logical interface connecting the Near-RT RIC with an E2 Node

**What does E2 do?**
* **Policy exchange**: Near-RT RIC receives policies and configurations from the Non-RT RIC to guide its optimization decisions.
* **Data sharing**: Real-time and historical network data collected by the Near-RT RIC is sent to the Non-RT RIC for analysis and long-term strategic planning.
* **Coordination and control**: The Non-RT RIC can remotely initiate control actions through the Near-RT RIC, like triggering congestion mitigation or network slicing functionalities.

**What does E2 node consist?**
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/B18IVAsO6.png"/>
* E2 Agent used to terminate E2 interface, support global services and to forward/receive RIC service messages.
* One or more RAN Functions that support RIC services exposed by the E2 Node to the Near-RT RIC.
* Other RAN functions that do not support RIC Services.

### B. Specification Objectives
* Connectivity between Near-RT RIC and E2 Node supplied by different vendors
* Exposure of selected E2 Node data (e.g. configuration information (cell configuration, supported slices, PLMNs, etc.), network measurements, context information, etc.) towards the Near-RT RIC
* Enables the Near-RT RIC to control selected RAN functions on the E2 Node

### C. Functions
#### 1) RIC Services
Near-RT RIC Services (**REPORT**, **INSERT**, **CONTROL**, **POLICY** and **QUERY**) supported by Near-RT RIC Functional Procedures (RIC Subscription, RIC Subscription Modification, RIC Subscription Modification Required, RIC Subscription Delete, RIC Subscription Delete Required, RIC Indication, RIC Control, RIC Query)

**REPORT**: uses RIC Subsription and/or RIC Subscription Modification to ==request that E2 Node sends a **REPORT** message== to Near-RT RIC and associated procedure continues in the E2 Node after each occurence of RIC Subscription's Event Trigger.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/H1BrsRjOa.png"/>

**INSERT**: uses RIC Subsription and/or RIC Subscription Modification to ==request that E2 Node sends a **INSERT** message== to Near-RT RIC and suspends the associated procedure in the E2 Node after each occurence of RIC Subscription's Event Trigger.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SkqZ1J3Op.png"/>

**CONTROL**: ==sends a **CONTROL** message to E2 Node== to initiate a new associated procedure OR ==resume a previously suspended associated procedure== in the E2 Node.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SkFrwyn_a.png">
  <figcaption>Response to RIC Service INSERT</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/rJnvk1nua.png"/>
  <figcaption>Near-RT RIC initiated</figcaption>
</figure>]

**POLICY**: uses RIC Subsription and/or RIC Subscription Modification to ==request that E2 Node executes a specific **POLICY**== during functioning of the E2 Node after each occurence of a defined RIC Subscription's Event Trigger.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/r1pFky2_p.png"/>

**QUERY**: ==sends a **QUERY** message to E2 Node== to retrieve RAN-related and/or UE-related information from the E2 Node.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/Hktj1kh_T.png"/>

#### 2) E2 Support Services
* Interface Management services supported by Global Procedures (E2 Setup, E2 Reset, E2 Node Configuration Update, E2 Removal, Reporting of General Error Situations)
* RAN Function services supported by Global Procedures (RIC Service Update, RIC Service Query).

**E2 Setup**: used to **establish** the E2 interface between the Near-RT RIC and an E2 Node.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SJIKrJ2O6.png"/>

**E2 Reset**: used by either the E2 Node or Near-RT RIC to **reset** the E2 interface.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/HyiiSk2Op.png">
  <figcaption>E2 Node initiated</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/S1oZU13dp.png"/>
  <figcaption>Near-RT RIC initiated</figcaption>
</figure>

**RIC Service Update**: used by the E2 Node to **inform** the Near-RT RIC of any change to **the list of supported RIC services** and **mapping** of services to functions within the E2 Node. 
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/rkZjI13_T.png"/>

**E2 Node Configuration Update**: used by the E2 Node to **inform** the Near-RT RIC of any change to **the configuration of the E2 Node and/or E2 Node** initiated changes to TNL Associations associated with the E2 interface.
<img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/SyJ6UJ2u6.png"/>

**E2 Removal**: used by either the E2 Node or Near-RT RIC to **release** the E2 signaling connection.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/S1WJvk3dp.png">
  <figcaption>E2 Node initiated</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/HJwePJhup.png"/>
  <figcaption>Near-RT RIC initiated</figcaption>
</figure>

## II. E2 Application Protocol (E2AP)
**Relationship between E2AP and RIC Service**
![image](https://hackmd.io/_uploads/Hy6zvzIt6.png)

### RIC Subscription Procedure
This procedure is used to establish RIC Subscriptions on E2 Node consisting of an event trigger and a sequence of RIC Service Actions.
> Initiated by Near-RT RIC; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SJhKOM8Y6.png"/>
  <figcaption>RIC Subscription procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/S1jp_zUFT.png"/>
  <figcaption>RIC Subscription procedure, unsuccessful operation</figcaption>
</figure>

### RIC Subscription Delete Procedure
This procedure is used to delete RIC Subscriptions on E2 Node.
> Initiated by Near-RT RIC; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/r1qfKGUYT.png"/>
  <figcaption>RIC Subscription Delete procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/B1JVKz8Ya.png"/>
  <figcaption>RIC Subscription Delete procedure, unsuccessful operation</figcaption>
</figure>

### RIC Subscription Delete Required Procedure
This procedure is used to enable the E2 Node to request deletion of the existing RIC Subscriptions in the E2 Node previously created for the Near-RT RIC.
> Initiated by E2 Node; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/H17KYGIKa.png"/>
  <figcaption>RIC Subscription Delete Required procedure, successful operation</figcaption>
</figure>

### RIC Indication Procedure
The purpose of the RIC Indication procedure is to transfer Report and/or Insert RIC Service Action associated with a RIC Subscription procedure.
> Initiated by E2 Node; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SkE6YzIFa.png"/>
  <figcaption>RIC Indication procedure, successful operation</figcaption>
</figure>

### RIC Control Procedure
The purpose of the RIC Control procedure is to initiate or resume a specific functionality in the E2 Node.
> Initiated by Near-RT RIC; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/Sk3Mqz8F6.png"/>
  <figcaption>RIC Control procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/r1-P5f8t6.png"/>
  <figcaption>RIC Control procedure, unsuccessful operation</figcaption>
</figure>

### RIC Subscription Modification Procedure
The purpose of the RIC Subscription Modification procedure is to modify an existing RIC subscription on an E2 node, in terms of its event trigger definition and/or the sequence of actions.
> Initiated by Near-RT RIC; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/S1ZDjMLta.png"/>
  <figcaption>RIC Subscription Modification procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SyTjsfUYa.png"/>
  <figcaption>RIC Subscription Modification procedure, unsuccessful operation</figcaption>
</figure>

### RIC Subscription Modification Required Procedure
This procedure is used by the E2 Node to request the Near-RT RIC for modifying an existing RIC Subscription in the E2 Node.
> Initiated by E2 Node; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/ByRInf8Ya.png"/>
  <figcaption>RIC Subscription Modification Required procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/ByV53MUKp.png"/>
  <figcaption>RIC Subscription Modification Required procedure, unsuccessful operation</figcaption>
</figure>

### RIC Subscription Modification Procedure
The purpose of the RIC Subscription Modification procedure is to modify an existing RIC subscription on an E2 node, in terms of its event trigger definition and/or the sequence of actions.
> Initiated by Near-RT RIC; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/S1ZDjMLta.png"/>
  <figcaption>RIC Subscription Modification procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SyTjsfUYa.png"/>
  <figcaption>RIC Subscription Modification procedure, unsuccessful operation</figcaption>
</figure>

### RIC Query Procedure
This procedure is initiated by Near-RT RIC to request RAN and/or UE related information from E2 Node.
> Initiated by Near-RT RIC; uses RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/Hyup3G8Kp.png"/>
  <figcaption>RIC Query procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/Hkw0hfIKa.png"/>
  <figcaption>RIC Query procedure, unsuccessful operation</figcaption>
</figure>

### E2 Setup Procedure
This procedure erases any existing application level configuration data in the two nodes and replace it by the one received. 
> Initiated by E2 Node; uses E2 Support Function signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/ByMIL78FT.png"/>
  <figcaption>E2 Setup procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/ByVPUmIK6.png"/>
  <figcaption>E2 Setup procedure, unsuccessful operation</figcaption>
</figure>

### Reset Procedure
The purpose of the Reset procedure is to initialize or re-initialise the E2 Node in the event of Near-RT RIC failure or vice-versa. 
> Initiated by E2 Node or the Near-RT RIC; uses E2 Support Function signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/Byd0UQIYp.png"/>
  <figcaption>Reset procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/BkElPQUKa.png"/>
  <figcaption>Reset procedure, unsuccessful operation</figcaption>
</figure>

### Error Indication 
The purpose of the Reset procedure is to report detected errors in one incoming message, provided they cannot be reported by an appropriate failure message.
> Initiated by E2 Node or the Near-RT RIC; uses E2 Support Function signaling or RIC Service signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/BJUcwXIYa.png"/>
  <figcaption>Error Indication, (E2 Node initiated) successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/Bye6vmIta.png"/>
  <figcaption>Error Indication, (Near-RT RIC initiated) successful operation</figcaption>
</figure>

### RIC Service Update Procedure
The purpose of the Reset procedure is to update application level RIC Service related data needed for E2 Node and Near-RT RIC to interoperate correctly over the E2 interface.
> Initiated by E2 Node; uses E2 Support Function signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/Sy9mOQ8Yp.png"/>
  <figcaption>RIC Service Update procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/B194u7IFa.png"/>
  <figcaption>RIC Service Update procedure, unsuccessful operation</figcaption>
</figure>

### E2 Node Configuration Update Procedure
The purpose of the Reset procedure is to update application level E2 Node configuration data needed for E2 Node and Near-RT RIC to interoperate correctly over the E2 interface and to support E2 Node initiated TNL association removal.
> Initiated by E2 Node; uses E2 Support Function signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:70%;" src="https://hackmd.io/_uploads/B1fuOXIta.png"/>
  <figcaption>E2 Node Configuration Update procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:70%;" src="https://hackmd.io/_uploads/BJTYumUtp.png"/>
  <figcaption>E2 Node Configuration Update procedure, unsuccessful operation</figcaption>
</figure>

### E2 Connection Update Procedure
The purpose of the Reset procedure is to allow the Near-RT RIC to update the TNL information associated with the E2 interface connection between the E2 Node and Near-RT RIC.
> Initiated by Near-RT RIC; uses E2 Support Function signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/SyvnO7IKT.png"/>
  <figcaption>E2 Connection Update procedure, successful operation</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:60%;" src="https://hackmd.io/_uploads/rJwTOXLFp.png"/>
  <figcaption>E2 Connection Update procedure, unsuccessful operation</figcaption>
</figure>

### E2 Removal Procedure
The purpose of the Reset procedure is to remove the E2 signaling connection between the Near-RT RIC and the E2 node in a controlled manner. 
> Initiated by E2 Node or Near-RT RIC; uses E2 Support Function signaling

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/SyWetQUYa.png"/>
  <figcaption>E2 Removal procedure, successful operation (E2 Node Initiated)</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/SycZtQItp.png"/>
  <figcaption>E2 Removal procedure, successful operation (Near-RT RIC Initiated)</figcaption>
</figure>

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/S15EK7IY6.png"/>
  <figcaption>E2 Removal procedure, unsuccessful operation (E2 Node Initiated)</figcaption>
</figure>]

<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:50%;" src="https://hackmd.io/_uploads/SJKStQLFp.png"/>
  <figcaption>E2 Removal procedure, unsuccessful operation (Near-RT RIC Initiated)</figcaption>
</figure>

## III. E2 Service Model (E2SM)
**E2AP Protocol** establish the logical connection between to E2AP end-points (Near RT RIC and Open RAN CU/DU) provides services to implement an **E2 Service Model – E2SM**. These procedures are then combined to create a service model. The service model message is inserted as payload in one of the E2AP messages, as shown in Figure below.
<figure style="text-align:center;">
  <img style="display:block;margin:20px auto;padding:1px;border:1px #eee;width:70%;" src="https://hackmd.io/_uploads/H1edtrUK6.png"/>
</figure>

Three services models that are implementes as xApps in Near-RT RIC : 
* **E2SM Key Performance Matrix (KPM)**: reports performance metrics from the RAN, using E2 report messages.
* **E2SM Network Interfaces (NI)**: used to take the messages received by the E2 node on specific network interfaces and forward them to the Near-RT RIC domain via E2 report messages over the E2 interface.
* **E2SM RAN Control (RC)**: implements control functionalities through E2 control procedures.

### E2SM Services
![Screen Shot 2024-01-18 at 13.53.22](https://hackmd.io/_uploads/rkyxirLtT.png)

![Screen Shot 2024-01-18 at 13.54.12](https://hackmd.io/_uploads/Hk-XsS8K6.png)

### E2SM Common Elements
* **Information Element** : When specifying information elements which are to be represented by bit strings, if not otherwise specifically stated in the semantics description of the concerned IE or elsewhere, the following principle applies with regards to the ordering of bits:
	- The first bit (leftmost bit) contains the most significant bit (MSB);
	- The last bit (rightmost bit) contains the least significant bit (LSB);
	- When importing bit strings from other specifications, the first bit of the bit string contains the first bit of the concerned information.

* **Information Element Abstract Syntax (with ASN.1)** : In case there is **contradiction** between the ASN.1 definition and the tabular format in Information Element, the ASN.1 shall take precedence, except for the definition of conditions for the presence of conditional elements, in which the tabular format shall take precedence.
