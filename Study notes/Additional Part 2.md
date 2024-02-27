# Taqi Additional Part 2
###### tags: `RIC-Team` `TEEP` 
# Additional Part 2 (gNB part)

## MAC 

1. LTE MAC：http://www.sharetechnote.com/html/MAC_LTE.html#Overview
2. 5G MAC：http://www.sharetechnote.com/html/5G/5G_MAC.html
3. Video of 4G MAC SCHEDULER：https://youtu.be/acjy_sBsw0w
### LTE Mac
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/mac_struct.png)
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/mac%202.png)
A media access control is a network data transfer policy that determines how data is transmitted between two computer terminals through a network cable. The essence of the MAC protocol is to ensure non-collision and eases the transfer of data packets between two computer terminals. A collision takes place when two or more terminals transmit data/information simultaneously.

| Procedure Name | Description | Summary |
| -------- | -------- | -------- |
| Random Access Procedure     | Get the initial uplink grant and perform synchronization to network | The Random Access Channel (RACH) plays a pivotal role in LTE networks by enabling user equipment (UE) to initiate communication with the network. It facilitates initial access, necessary for establishing an uplink synchronization, and is crucial for scenarios such as network entry, handover, or when a device moves from an idle to an active state. RACH ensures that the network can efficiently manage and allocate resources to accommodate new and moving connections.     |
|DL-SCH Data Transfer|Do everything needed to perform DL Data Transfer (DCI-Scheduling, HARQ etc)|The downlink data transmission process in LTE involves several steps from data transfer from the network's higher layers to the lower layers, transmission to the user equipment (UE) via PDSCH, UE's reception and CRC error checking, followed by the UE sending an ACK/NACK response through PUSCH (if it has data to send) or PUCCH (if it doesn't). The network then receives this response and proceeds accordingly, either transmitting new data (if ACK) or retransmitting the existing data with a different revision (if NACK).
|||




## RLC

1. 4G RLC：http://www.sharetechnote.com/html/RLC_LTE.html#Overview
2. 5G RLC：http://www.sharetechnote.com/html/5G/5G_RLC.html

