# OSC-O-DU-High
## O-DU High Architecture
O-DU implements the functional blocks of L2 layer of a 5G NR protocol stack in SA (StandAlone) mode. These layers primarily include NR (New Radio) MAC, NR Scheduler and NR RLC (Radio Link Control) layers. O-DU modules are developed as shown in the below diagram.
![O DU HIGH Architecture](https://github.com/bmw-ece-ntust/internship/assets/145204053/f77b7aa1-e572-4357-9512-e7690d078c33)

## O-DU High Thread Architecture
There are multiple entities within O-DU High. Modules sharing a given color belong to one thread. O-DU architecture can be defined at a thread level as follows:

Thread 1: O-DU thread
Thread 2: DU APP inclusive of Config Handler, DU Manager, UE Manager, and ASN.1 Codecs
Thread 3: 5G NR RLC DL and MAC (inclusive of 5G NR SCH and Lower MAC)
Thread 4: 5G NR RLC UL
Thread 5: SCTP Handler
Thread 6: Lower MAC Handler
Thread 7: EGTP Handler
Thread 8: O1

## O-DU High Module
### DU APP
This module configures and manages all the operations of O-DU. It interfaces with external entities as follows:


1. OAM: DU APP interacts with OAM on the O1 interface for configuration, alarms and performance management.
2. O-CU: DU APP interacts with O-CU for RAN functionalities over the F1 interface which is built on SCTP. Control messages are exchanged on the F1-C interface and data messages on the F1-U interface. 
3. RIC: DU APP interacts with RIC on E2 interface over SCTP.
   
DU App submodules are as follows:
1. Config Handler manages the configurations received on O1 interfaces and stores them within DU APP context.
2. DU Manger handles all cell operations at the DU APP.
3. UE Manager handles UE contexts at the DU APP.
4. SCTP handler is responsible for establishing SCTP connections with O-CU, RIC on the F1AP and E2AP interfaces respectively.
5. EGTP handler is responsible for establishing EGTP connection with O-CU for data message exchange on the F1-U interface.
6. ASN.1 Codecs contain ASN.1 encode/decode functions which are used for System information, F1AP and E2AP messages.

### 5G NR LRC 
This module provides services for transferring the control and data messages between MAC layer and O-CU (via DU App).

5G NR RLC UL and 5G NR RLC DL are the sub modules of this module that implement uplink and downlink functionality respectively.

### 5G NR MAC
This module uses the services of the NR physical layer to send and receive data on the various logical channels. Functions of the 5G NR MAC module are as follows:

1. 5G NR MAC is responsible for multiplexing and de-multiplexing of the data on various logical channels.
2. 5G NR SCH schedules resources in UL and DL for cell and UE based procedures. 5G NR SCH is completely encapsulated within the 5G NR MAC i.e., all interactions of the 5G NR SCH is via the 5G NR MAC.
3. Lower MAC interfaces between the MAC and the O-DU Low. It implements all the messages of FAPI specification. It has a receiver thread to handle messages from L1.
