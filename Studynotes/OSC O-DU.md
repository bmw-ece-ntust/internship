# OSC O-DU

## O-DU

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Logical%20Architecture%20of%20O-RAN.png)

Figure 1 - Logical Architecture of O-RAN

Distributed Unit (DU) is a crucial component in the architecture of 5G, which is part of the radio network and has functions related to the MAC/PHY layer. DU is a logical node that incorporates the RLC/MAC/High-PHY layers based on functional separation that defined by O-RAN.

DU will be integrated with the Central Unit (CU), forming the 5G radio system. Radio Unit (RU) and antenna systems are integrated into a single DU, and the CU can be configured and virtualized, potentially placed in RAN computing assets across various network locations.

In some RAN deployment scenarios, the physical layer is split between the O-DU and O-RU. O-RAN WG4 defines the open front haul interface which is adopted in the split architecture as shown in Figure below. The O-DU 
contains the higher physical layer High-PHY functions while the O-RU contains the lower physical layer Low-PHY.

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/gNodeB.png) 

Figure 2 - Architecture Split of gNodeB

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Layer%20Split.jpg)

Figure 3 - Functional Layer Split of 5G NR

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/O-DU%20Functional%20Blocks.png)

Figure 4 - Functional Layer Split on O-DU

3GPP considered the split concept (DU and CU) for 5G from the beginning of writing its specifications. The DU is responsible for real time layer 1 (L1, physical layer) and lower layer 2 (L2) which contains the data link layer and scheduling functions. The CU is responsible for non-real time, higher L2 and L3 (network layer) functions.

![Image](https://media.licdn.com/dms/image/C4D12AQE6NK_84tUh1A/article-inline_image-shrink_1500_2232/0/1648085580383?e=1716422400&v=beta&t=v6vfVk64rW82HpWnjy0Ian9JeTWUHxfzbc8OL62Q0D8)

Figure 5 - L2 Structure of 5G NR U-Plane

## O-DU High Architecture
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/ODUArch.jpg)

Figure 6 - L2 Structure of 5G NR U-Plane

O-DU implements the functional blocks of L2 layer of a 5G NR protocol stack in SA(StandAlone) mode. These layers primarily include NR MAC, NR Scheduler and NR RLC layers.

### Elements & Interfaces

| Thread        | Description   |
| ------------- |-------------  |
| Thread 1      | O-DU thread   |
| Thread 2      | DU APP inclusive of Config Handler, DU Manager, UE Manager, and ASN.1 Codecs      |
| Thread 3      | 5G NR RLC DL and MAC (inclusive of 5G NR SCH and Lower MAC)    |
| Thread 4      | 5G NR RLC UL      |
| Thread 5      | SCTP Handler      |
| Thread 6      | Lower MAC Handler |
| Thread 7      | EGTP Handler      |
| Thread 8      | O1                |

### Details of Each Elements

#### DU APP
This module configures and manages all the operations of O-DU. It interfaces with external entities as follows:

  - OAM : DU APP interacts with OAM (Operational, Administration, and Maintenance) on the O1 interface for configuration, alarms and performance management.
  - O-CU: DU APP interacts with O-CU for RAN functionalities over the F1 interface which is built on SCTP. Control messages are exchanged on the F1-C interface and data messages on the F1-U interface.
  - RIC: DU APP interacts with RIC on E2 interface over SCTP.

DU App submodules are as follows:

  - Config Handler manages the configurations received on O1 interfaces and stores them within DU APP context.
  - DU Manager handles all cell operations at the DU APP.
  - UE Manager handles UE contexts at the DU APP.
  - SCTP handler is responsible for establishing SCTP connections with O-CU, RIC on the F1AP and E2AP interfaces respectively.
  - EGTP handler is responsible for establishing EGTP connection with O-CU for data message exchange on the F1-U interface.
  - ASN.1 Codecs contain ASN.1 encode/decode functions which are used for System information, F1AP and E2AP messages.

#### 5G NR RLC
This module provides services for transferring the control and data messages between MAC layer and O-CU (via DU App).

5G NR RLC UL and 5G NR RLC DL are the sub modules of this module that implement uplink and downlink functionality respectively.

#### 5G NR MAC
This module uses the services of the NR physical layer to send and receive data on the various logical channels. Functions of the 5G NR MAC module are as follows:

  - 5G NR MAC is responsible for multiplexing and de-multiplexing of the data on various logical channels.
  - Lower MAC interfaces between the MAC and the O-DU Low. It implements all the messages of FAPI specification. It has a receiver thread to handle messages from L1.

#### 5G NR SCH
  - This module is completely encapuslated withing 5G NR MAC i.e. all interactions of the 5G NR SCH is via the 5G NR MAC.
  - Schedules resources in UL and DL for cell and UE based procedures.
  - SCH framework design supports plugging-in new scheduling algorithm easily. Refer to section “Scheduler Framework with plug-in support” in Developer-Guide document for details.

#### O-DU Utility and Common Functions
These modules contain platform specific files and support O-DU High functionality and message exchanges.

##### O1 Module
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/ODU-O1-Arch.jpg)

Figure 7 - O1 Architecture

As shown in figure 2 the O1 module runs as a thread in O-DU High. Alarm communication happens over a Unix socket between the O1 and O-DU threads. O1 module uses API calls for interacting with the Netconf server(Netopeer) and datastore(sysrepo) for providing the Netconf interface.

O1 architecture has following components:

  - Netconf Session Handler: Subscribe to Netconf YANG modules and events. Register callback handler methods.
  - VES Agent : Sends the VES events to SMO
  - Alarm Manager: Stores and manages(add/updated/delete) alarms.
  - Alarm Interface : Provides an interface to O-DU High threads for sending the alarm messages to O1 module over Unix socket.
  - Config Interface : Interface to handle the configurations sent from SMO to the stack
  - Netopeer server: Serves the northbound SMO/OAM Netconf requests.

## O-DU High Interfaces
![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/O-DUHighInterfaces.jpg)

Figure 8 - O-DU High Interfaces

### O-CU
O-DU High communicates with O-CU on the F1AP interface. The control message exchanges are on F1-C while data message exchanges are on F1-U interfaces. The below F1AP messages on F1-C are implemented, as per 3GPP 38.473-f60 v15.3:

  - Interface Management
    - F1 Setup
    - gNB-DU Configuration Update
    - F1 Reset
    - PAGING
  - UE Context Management
    - UE Context Setup
    - UE Context Modification
    - UE Context Release
  - RRC Message Transfer
    - Initial UL RRC Message Transfer
    - DL RRC Message Transfer
    - UL RRC Message Transfer
    - RRC Delivery Report

### Near RT RIC
O-DU High communicates with Near RT RIC on the E2 interface. The below E2AP messages are implemented, as per O-RAN.WG3.E2GAP-R003-v03.00 and O-RAN.WG3.E2AP-R003-v03.00.

  - Global Procedures
    - E2 Setup
    - E2 Node Configuration Update
    - RIC Service Update
    - E2 Connection Update
    - E2 Removal
    - E2 Reset
    - Error Indication
  - Near RT RIC Functional Procedures
    - RIC Subscription
    - RIC Subscription Modification
    - RIC Subscription Modification Required
    - RIC Subscription Delete
    - RIC Subscription Delete Required
    - RIC Indication 

### O-DU LOW
O-DU High communicates with O-DU Low on the FAPI interface. The below FAPI messages are supported, as per FAPI interface files shared by Intel:

  - P5 messages - PHY mode control interface
    - PARAM.request/PARAM.response
    - CONFIG.request/CONFIG.response
    - START.request
    - STOP.request
    - STOP.indication
  - P7 messages - Main data path interface
    - DL_TTI.request
    - UL_TTI.request
    - SLOT.indication
    - UL_DCI.request
    - TX_Data.request
    - RX_Data.indication
    - CRC.indication
    - UCI.indication
    - RACH.indication

### OAM
O-DU High communicates with OAM on the O1 interface.

## Channels
![Image](https://media.licdn.com/dms/image/C5612AQEfzCRX7sT4bQ/article-cover_image-shrink_720_1280/0/1646707724354?e=1716422400&v=beta&t=LGy9dYfNXGxuqu_bRcvhNG2Q6buVdL_NvXwiUV_S1Gc)

Figure 9 - Uplink and Downlink Channel Connection

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

### Type of Channel Breakdown

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

## O-DU High Functionality 

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
- SDAP  Service Data Adaptation Protocol
- PDCP  Packet Data Convergence Protocol

---

## Source
* [SIB : System Information Block](https://www.linkedin.com/pulse/sib-system-information-block-lte-techlte-world/)
* [Different Channel In 5G NR (Part 1)](https://www.linkedin.com/pulse/different-channels-5g-nr-part-1-shan-jaffry/)
* [Different Channel In 5G NR (Part 2)](https://www.linkedin.com/pulse/different-channels-5g-nr-part-2-shan-jaffry/)
* [Electronics Notes : 5G Channel mapping](https://www.electronics-notes.com/articles/connectivity/5g-mobile-wireless-cellular/data-channels-physical-transport-logical.php)
* [Sharetechnote : 5G NR Initial Access / RACH](https://www.sharetechnote.com/html/5G/5G_RACH.html)
* [RF Wireless World : 5G NR PRACH](https://www.rfwireless-world.com/5G/5G-NR-PRACH.html)
