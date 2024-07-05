# E2 Interface Testing Specification

## Conformance Testing on the Near RT RIC
 <img src="https://imgur.com/1QcRzUI.png" alt="Chart" width="500 " style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

The configuration above is illustrated using an E2 Node simulator, O-RU simulator and UE Simulator. **Testing without using simulator is would require the inclusion of O-RU with the associated M-Plane and an actual real UE**

Testing for things that involves E2 Node and Near RT RIC configuration is out of this report scope due to the usage of O1 interface for those testing. 

The testing environment may differ according to the cases described in **“O-RAN.WG1.O-RAN-Architecture-Description**

The testing done will be based on **O-RAN WG3: E2 Application Protocol**. But it may need support for the subset of E2 Service Models
- E2SM-KPM as specified in “ORAN WG3: E2SM KPM” 
- E2SM-NI as specified in “ORAN WG3: E2SM NI”
- E2SM-RC as specified in “ORAN WG3: E2SM RC”

Test Simulator Req:
- Generate E2 Node initiated procedures.
- Receive Near-RT RIC initiated procedures.
- Generate responses for either successful or unsuccessful operations with appropriate cause value in case of failure.

E2 Node simulator may also need to simulate necessary logical UE functions from the Near RT-RIC POV


## Confromance Testing E2 Node
<img src="https://imgur.com/R7SGNwl.png" alt="Chart" width="500 " style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
