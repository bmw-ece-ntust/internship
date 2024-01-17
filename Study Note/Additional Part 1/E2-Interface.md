# Part 1: E2 Interface related in Near-RT RIC Platform

- Goal : 
    - [ ] Learning E2 Interface
    - [ ] Learning E2 Service Model

- Outcome (Study Note) : 
    - Learn about E2 Interface
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

## II. E2 Service Model
