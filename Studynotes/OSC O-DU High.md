# OSC O-DU

## O-DU

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Logical%20Architecture%20of%20O-RAN.png) Logical Architecture of O-RAN

Distributed Unit (DU) is a crucial component in the architecture of 5G, which is part of the radio network and has functions related to the MAC/PHY layer. DU is a logical node that incorporates the RLC/MAC/High-PHY layers based on functional separation that defined by O-RAN.

DU will be integrated with the Central Unit (CU), forming the 5G radio system. Radio Unit (RU) and antenna systems are integrated into a single DU, and the CU can be configured and virtualized, potentially placed in RAN computing assets across various network locations.

In some RAN deployment scenarios, the physical layer is split between the O-DU and O-RU. O-RAN WG4 defines the open front haul interface which is adopted in the split architecture as shown in Figure below. The O-DU 
contains the higher physical layer High-PHY functions while the O-RU contains the lower physical layer Low-PHY.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/gNodeB.png) Architecture Split of gNodeB

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/O-DU%20Functional%20Blocks.png)
3GPP considered the split concept (DU and CU) for 5G from the beginning of writing its specifications. The DU is responsible for real time layer 1 (L1, physical layer) and lower layer 2 (L2) which contains the data link layer and scheduling functions. The CU is responsible for non-real time, higher L2 and L3 (network layer) functions.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Layer%20Split.jpg) Functional Split of 5G

## O-DU Architecture (OSC)

### Elements & Interfaces
* RLC
* MAC
* High-PHY
* FAPI
### Channels
* Physical Channels
  * Physical Broadcast Channel (PBCH) :
    - The main task for PBCH is to broadcast Master Information Block (MIB) from gNB to ALL UEs.
    - PBCH utilizes fixed QPSK modulation and has an 80 ms periodicity with multiple repetitive transmissions.
    - MIB is crucial for UE to initiate the decoding process for PDCCH, which subsequently enables decoding of PDSCH, Upon powering on, a UE actively searches for MIB.
    - PBCH is typically accompanied by Synchronization Signals (Secondary and Primary) for UE-and-gNB time-frequency synchronization.
    - PBCH/SS together form the SSB (Synchronization Signal Block).
    - Decoding the SSB Block allows a UE to access information in the SIB1 block, containing details about the Initial Bandwidth Part for initial access.
    - SSB consists of four OFDM symbols in the time domain and spans 20 Resource Blocks (RBs) in the frequency domain.
  * Physical Downlink & Uplink Control Channel (PDCCH & PUCCH):
    - PDCCH carries Downlink Control Information (DCI) using QPSK modulation.
    - PDCCH schedules resources for transmissions on PDSCH and PUSCH, and manages uplink power control.
    - PDCCH is not associated with any upper layer channel and solely carries DCI as its payload.
    - The information carried by PDCCH depends on DCI formats.
    - PUCCH carries Uplink Control Information (UCI), although UCI.
    - DCI is exclusively sent on the PDCCH channel.
* Control Logical Channels
* Control Transport Channels

## O-DU Functionality

### Cell up and Broadcast Procedure
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/CellUpAndBroadcast.png)
### UE Attach Procedure
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/UeAttach.png)
### Closed Loop Automation Procedure

### Inter-DU Handover within O-CU

### Inter-CU Handover (Xn-Based)

## Terms
- QPSK  Quadrature Phase Shift Keying
- OFDM  Orthogonal Frequency Division Multiplexing 
---
## Source
* [SIB : System Information Block](https://www.linkedin.com/pulse/sib-system-information-block-lte-techlte-world/)
* [Different Channel In 5G NR (Part 1)](https://www.linkedin.com/pulse/different-channels-5g-nr-part-1-shan-jaffry/)
* [Different Channel In 5G NR (Part 2)](https://www.linkedin.com/pulse/different-channels-5g-nr-part-2-shan-jaffry/)

