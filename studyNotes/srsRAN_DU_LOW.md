# SRS RAN ARCHITECTURE - DU LOW
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/b97fe877-49d4-4ffe-88df-83645d374314)

DU (Distributed Unit) is responsible for handling both uplink and downlink traffic and it is split into two structures, UL (Uplink) 
and DL (Down Link) 

## UL (Up Link)
Uplink consists of several blocks such as
- PUCCH (Physical Uplink Control Channel) -> carries UCI (Uplink Control Information)
- PUSCH (Physical Uplink Shared Channel) -> carries user data
- PRACH (Physical Random Access Channel) -> carries random access preamble from UE towards gNB 
