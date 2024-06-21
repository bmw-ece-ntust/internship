## OAI FUNCTIONAL SPLITS
Three computing Nodes :
[1] Radio Cloud Center (RCC)
[2] Radio Access Unit (RAU)
[3] Remote Radio Unit (RRU)


## Layer 1 (Physical Layer)
Layer 1 is a Physical Layer responsible for the transmission and reception of raw bitstreams over a physical medium. In OAI, this layer handles the modulation, coding, and multiplexing of signals to ensure they can be transmitted efficiently and effectively over the air interface. It deals with the radio frequency (RF) aspects of communication, including signal generation, synchronization, and channel estimation. 
<img width="1178" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/e188203e-5af9-4c40-b6fc-904f414c50d2">


## Layer 2 (Data Link Layer)
Layer 2 is a Data Link Layer responsible for managing data transfer between the base station and the UE (user equipment) over the physical link established by Layer 1. It is subdivided into three main sub-layers: 

- Medium Access Control (MAC) : manages the access to the physical channel, scheduling transmissions, handling retransmissions, and ensuring efficient utilization of the available bandwidth. It deals with packet scheduling, error correction through HARQ (Hybrid Automatic Repeat Request), and managing the resources allocated to different users.

- Radio Link Control (RLC) : ensures reliable data transfer by performing segmentation, reassembly, and error correction through ARQ (Automatic Repeat Request). It operates in three modes: Transparent Mode (TM), Unacknowledged Mode (UM), and Acknowledged Mode (AM), depending on the type of service required.

- Packet Data Convergence Protocol : handles higher-layer data management tasks, including header compression to reduce the size of IP packets, security through encryption and integrity protection, and maintenance of data sequence integrity.

<img width="1178" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/dd0037b5-93de-41df-b897-cb80d05aca33">


## Random Access Scheduling
<img width="1178" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/27a2ba9f-6293-4d82-87fc-9a5f633e80e5">

