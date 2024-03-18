# OSC O-DU

## O-DU

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Logical%20Architecture%20of%20O-RAN.png)

Logical Architecture of O-RAN

Distributed Unit (DU) is a crucial component in the architecture of 5G, which is part of the radio network and has functions related to the MAC/PHY layer. DU is a logical node that incorporates the RLC/MAC/High-PHY layers based on functional separation that defined by O-RAN.

DU will be integrated with the Central Unit (CU), forming the 5G radio system. Radio Unit (RU) and antenna systems are integrated into a single DU, and the CU can be configured and virtualized, potentially placed in RAN computing assets across various network locations.

In some RAN deployment scenarios, the physical layer is split between the O-DU and O-RU. O-RAN WG4 defines the open front haul interface which is adopted in the split architecture as shown in Figure below. The O-DU 
contains the higher physical layer High-PHY functions while the O-RU contains the lower physical layer Low-PHY.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/gNodeB.png) 

Architecture Split of gNodeB

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Layer%20Split.jpg)

Functional Split of 5G

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/O-DU%20Functional%20Blocks.png)

3GPP considered the split concept (DU and CU) for 5G from the beginning of writing its specifications. The DU is responsible for real time layer 1 (L1, physical layer) and lower layer 2 (L2) which contains the data link layer and scheduling functions. The CU is responsible for non-real time, higher L2 and L3 (network layer) functions.

![Image](https://media.licdn.com/dms/image/C4D12AQE6NK_84tUh1A/article-inline_image-shrink_1500_2232/0/1648085580383?e=1716422400&v=beta&t=v6vfVk64rW82HpWnjy0Ian9JeTWUHxfzbc8OL62Q0D8)

L2 Structure of 5G NR U-Plane

## O-DU Architecture (OSC)

### Elements & Interfaces

* RLC
* MAC
* High-PHY
* FAPI

## Channels
![Image](https://media.licdn.com/dms/image/C5612AQEfzCRX7sT4bQ/article-cover_image-shrink_720_1280/0/1646707724354?e=1716422400&v=beta&t=LGy9dYfNXGxuqu_bRcvhNG2Q6buVdL_NvXwiUV_S1Gc)

In the 5G cellular communication system, there are three types of channels:

1. **Logical Channel**:
   - Logcal Channel serve as pathways for transmitting data between the RLC and MAC layers
   - Logical channels receive generic data from upper layers (e.g., application layer) and segmentize it into different categories (e.g., data or control).
   - Logical channels are further categorized into Control and Traffic channels
   - Control channels transmit control and configuration information essential for operating the NR system
   - Traffic channels are responsible for transmitting user data
   - Logical channels facilitate multiplexing data from various sources into respective transport channels
   - They enable scheduling and initiation of processes such as HARQ (Hybrid Automatic Repeat Request)

2. **Transport Channel**:
   - This channel serves as a communication link between the MAC layer and the PHY (Physical) layer.
   - It facilitates the transmission of data from the MAC layer to the PHY layer for eventual transmission over the air interface.
   - Data on the Transport Channel is organized into Transport Blocks (TB) by the MAC layer
   - Each TTI can transmit at most one dynamic-sized TB, or two TBs in case of spatial multiplexing with more than four layers
   - Associated with each TB is a Transport Format (TF), which specifies how the TB is to be transmitted over the radio interface
   - The TF includes information about the transport-block size, modulation-and-coding scheme, and antenna mapping
   - Varying the TF allows the MAC layer to adjust data rates, facilitating link adaptation for error-free transmission even in challenging radio conditions
   - Data on the Transport Channel is mapped onto physical channels (e.g., PDCCH, PDSCH, etc.) by the PHY layer for transmission over the air interface

3. **Physical Channel**:
   - These channels are responsible for carrying the actual data over the air interface between the gNB (base station) and the user device.
   - Physical channels represent the closest layer to the over-the-air transmission process.

Overall, logical channels facilitate communication between different layers within the 5G NR stack, transport channels link the MAC and PHY layers, and physical channels handle the actual transmission of data over the air interface.

#### Control Logical Channels
* Broadcast Control Channel (BCCH) :
  - Downlink channel used for broadcasting system information to all UE within a cell
  - Transmits Master Information Block (MIB) mapped onto BCH transport channel and System Information Blocks (SIBs) mapped onto DL-SCH transport channel

* Paging Control Channel (PCCH) :
  - Downlink channel used for paging UE whose cell-level locations are unknown to the network
  - Transmits paging messages mapped onto PCH transport channel

* Common Control Channel (CCCH) :
  - Used for transmitting control information on both the downlink and uplink from UE
  - Utilized for initial access for devices without a Radio Resource Control (RRC) connection

* Dedicated Control Channel (DCCH) :
  - Used for transmitting dedicated control information between the UE and the network
  - Operates by UE and Network in both uplink and downlink after establishing an RRC connection

* Dedicated Traffic Channel (DTCH) :
  - Channel present in both uplink and downlink, dedicated to a specific UE
  - Used for transmitting user data between a specific UE and the network

#### Control Transport Channels
* Broadcast Channel (BCH) :
  - Downlink channel used exclusively for transmitting parts of the BCCH System Information (SI), specifically the Master Information Block (MIB)
  - It has a specific format for efficient transmission of essential network information

* Paging Channel (PCH) :
  - Downlink channel used for transmitting paging information from the PCCH logical channel
  - Supports discontinuous reception (DRX) to allow devices to save battery power by waking up at predefined time instants for PCH reception

* Downlink Shared Channel (DL-SCH) :
  - Primary downlink transport channel for transmitting downlink data
  - Supports key 5G NR features such as dynamic rate adaptation, HARQ, channel-aware scheduling, and spatial multiplexing
  - Also used for transmitting parts of the BCCH system information (SIB)

* Uplink Shared Channel (UL-SCH) :
  - Uplink counterpart to DL-SCH, used for transmitting uplink data

* Random Access Channel (RACH) :
  - Transport channel used for carrying random access preamble during random access procedures
  - It does not carry Transport Blocks (TB) and is distinct from other transport channels

#### Physical Channels
* Physical Broadcast Channel (PBCH) :
  - The main task for PBCH is to broadcast Master Information Block (MIB) from gNB to ALL UEs.
    ![Image](https://media.licdn.com/dms/image/C5612AQGC-JUw0-5A2Q/article-inline_image-shrink_1500_2232/0/1646707809446?e=1716422400&v=beta&t=BCoLv5VUrAcIHgtsI1DFgc274jrujfuZOkPn9lNnQkE)
  - PBCH utilizes fixed QPSK modulation and has an 80 ms periodicity with multiple repetitive transmissions.
  - MIB is crucial for UE to initiate the decoding process for PDCCH, which subsequently enables decoding of PDSCH, Upon powering on, a UE actively searches for MIB.
  - PBCH is typically accompanied by Synchronization Signals (Secondary and Primary) for UE-and-gNB time-frequency synchronization.
  - PBCH/SS together form the SSB (Synchronization Signal Block).
  - Decoding the SSB Block allows a UE to access information in the SIB1 block, containing details about the Initial Bandwidth Part for initial access.
  - SSB consists of four OFDM symbols in the time domain and spans 20 Resource Blocks (RBs) in the frequency domain.

* Physical Downlink & Uplink Control Channel (PDCCH & PUCCH):
  - PDCCH carries DCI using QPSK modulation.
    ![Image](https://media.licdn.com/dms/image/C5612AQGCs7XCqLBHRg/article-inline_image-shrink_1500_2232/0/1646707943962?e=1716422400&v=beta&t=f28B-WK68N51vme18s22t3VL2AGnUKUdg_6Vwy5zC-g)
  - PDCCH schedules resources for transmissions on PDSCH and PUSCH, and manages uplink power control.
  - PDCCH is not associated with any upper layer channel and solely carries DCI as its payload.
  - The information carried by PDCCH depends on DCI formats.
  - PUCCH carries UCI, although UCI.
  - DCI is exclusively sent on the PDCCH channel.

* Physical Downlink & Uplink Shared Channel (PDSCH & PUSCH)
  - PDSCH carries various types of data, including user data, higher layer control messages, system information blocks (SIBs), and paging.
  - PDSCH utilizes flexible Modulation and Coding Schemes (MCS) based on link conditions (e.g., signal-to-noise ratio)
  - PDSCH supports modulation schemes like QPSK, 16-QAM, 64-QAM, and 256-QAM
  - PDSCH Does not carry UCI like DCI
  - PUSCH counterpart to PDSCH, used for uplink data transmission
  - PUSCH Similar to PDSCH but operates in the opposite direction
  - PUSCH can carry UCI in addition to user data
  - PUSCH reflects changes in link conditions and modulation schemes like PDSCH

* Physical Random Access Channel (PRACH)
  - PRACH serves as the medium for transmitting random access preambles from the UE to the gNB 
  - The random access process assists the gNB in adjusting uplink timings of the UE and other relevant parameters for effective communication
  - Random access preambles can be of two different lengths. 
  - Long Sequence: 839 symbols, applied to subcarrier spacings of 1.25 kHz and 5 kHz. 
  - Short Sequence: 139 symbols, applied to subcarrier spacings of 15 kHz and 30 kHz (FR1 bands) and 60 kHz and 120 kHz (FR2 bands)
  - PRACH employs OFDM for its signal, distinguishing it from other channels like PUCCH and PUSCH.

## O-DU Functionality

### Cell up and Broadcast Procedure
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/CellUpAndBroadcast.png)

- If O1 interface is disabled, DU APP module uses static configuration.
- O-DU High sends F1 Setup Request to O-CU, containing a list of configured cells.
- O-CU responds with F1 Setup Response, listing cells that must be activated.
- O-DU High sends cell configurations to 5G NR MAC based on the received list of cells.
- 5G NR MAC configures 5G NR SCH and O-DU Low via Lower MAC module.
- DU APP sends gNB DU Config Update to O-CU; O-CU responds with gNB DU Config Update ACK.
- DU APP exchanges F1 Reset message with O-CU to initialize UE contexts.
- DU APP sends Cell Start Req to 5G NR MAC, translated into START.request towards O-DU Low by Lower MAC.
- O-DU Low begins sending slot indications to 5G NR MAC based on supported numerology.
- Upon receiving slot indications, DU APP marks cell as up; if O1 is enabled, triggers an alarm to SMO.
- 5G NR SCH tracks SSB and SIB1 occasions, schedules SSB/SIB1 upon detection, and forwards DL Scheduling Information to 5G NR MAC.
- 5G NR MAC multiplexes PDU and sends SSB/SIB1 packets to O-DU Low via Lower MAC.

### UE Attach Procedure
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/UeAttach.png)

* Cell broadcast of System Information which includes SSB and SIB1.

* RACH Procedure
  - RACH Indication
  - Random Access Response
  - RRC Setup Request
  - RRC Setup

* UE attach signalling flow
  - RRC Setup Complete
  - Registraton Request
  - NAS Authentication Request
  - NAS Authentication Response
  - NAS Security Mode Command
  - NAS Security Mode Complete
  - RRC Security Mode Command
  - RRC Security Mode Complete
  - Registraton Accept
  - Registraton Complete
  - RRC Reconfiguration
  - RRC Reconfiguration Complete

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
* [Electronics Notes : 5G Channel mapping](https://www.electronics-notes.com/articles/connectivity/5g-mobile-wireless-cellular/data-channels-physical-transport-logical.php)
* [Sharetechnote : 5G NR Initial Access / RACH](https://www.sharetechnote.com/html/5G/5G_RACH.html)
* [RF Wireless World : 5G NR PRACH](https://www.rfwireless-world.com/5G/5G-NR-PRACH.html)
