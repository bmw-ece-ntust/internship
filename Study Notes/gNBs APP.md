## gNBs APP

<img width="332" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/98302e43-8287-4fc9-92df-92ea608de9ff">


gNBs APP (5G New Radio (NR) base stations applications) configures various OAI modules (RRC and PDCP), excluding message protocol functions like F1AP and GTP-U. It also manages base station and user indirectly.

## gNBs APP Flowchart
<img width="292" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/ec473b1f-176d-4604-80fa-097ad094256f">

When the OSC O-DU High provides a list of cells that require modifications, the OAI CU, acting as the central unit, detects this list and recognizes the need for changes within certain cells. Subsequently, the F1AP module communicates with the base station application (gNB APP) to pinpoint the specific cell requiring modification. Once identified, the base station application proceeds to adjust the cell's configuration as directed by the OSC O-DU High, such as altering the PLMN ID. Upon completion, the gNB APP sends an acknowledgment to the CU, confirming the successful implementation of changes. The F1AP module then relays this acknowledgment to the OSC O-DU High. However, if the identified cell does not exist or complications arise, no alterations are made, and the base station application notifies the CU of the failure. In response, the F1AP module sends a failure message to the OSC O-DU High, indicating the unsuccessful attempt at configuration modification.

This system is used for communcation system such as 
1. Voice Calls: Making and receiving phone calls using cellular networks.
2. Text Messaging: Sending SMS (Short Message Service) or MMS (Multimedia Messaging Service) messages.
3. Data Transmission: Accessing the internet, sending emails, downloading/uploading files, streaming videos, etc.
4. Multimedia Streaming: Watching live TV, streaming music, video calls, etc.
5. IoT Communication: Connecting various IoT (Internet of Things) devices to the network for data exchange and control.



## List of abbreviations:
- OSC: OpenAirSoftware Community
- O-DU: Open Distributed Unit
- OAI: Open Air Interface
- CU: Central Unit
- F1AP: F1 Application Protocol
- gNB: Next-Generation NodeB (base station)
- APP: Application
- IE: Information Element
- PLMN: Public Land Mobile Network
