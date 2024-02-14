# RACH Introduction

**Goals**
- [x] Learn about the background RACH
- [x] Understand why RACH is needed
- [x] Understand the basic princples of RACH Types (Cont. based and Cont. free)

**What I have learned**
- Understanding of what is RACH
- Understanding of why RACH is needed and when we need it.
- Understanding of the basic principles of Contention based and contention free RACH


## What is RACH
RACH is the process for establishing an Uplink Synchronization, timing sync and an ID for RA communication between between a device and a network in wireless communication including 5G, 4G, and 3G. RACH is used to request access to the network. Esentially, if a UE wants to connect to a network, it has go through RACH first to request access to the network.



### Two types of RACH

#### a. Contention Based 
When a UE transmits a **PRACH Preamble** the UE transmits it with with a specific pattern or usually called signature. There are 64 different kinds of signature and the UE selects randomly one of those. The selection of this signature is based on **Zadoff Chu Sequence**

Because of this multiple UEs can accidentally chooses the same signature and causes collision if the signal arrived at exactly the same time which is called **Contention**. Two possibilities
* **Case 1:** Both signal act as an interference and none gets decoded by the NW. Thus the UE indentifies that RACH process has failed and sends again PRACH preamble.
*  **Case 2:** The UE only decodes signal from one device and failed to decode from the other. The UE with succesfiul L2/L3 decoding on the NW side will receives **HARQ ACK** .

**Steps:**
```sequence
    UE->NW: RACH Preamble
    NW->UE: RACH Response
    UE->NW: L2/L3 Message
    NW->UE: Contention Resolution
```




#### b. Contention Free
There is some case where contention is not acceptable. This method prevents contention by providing UEs with a unique PRACH Preamble to use and when to use.
**Steps:**
```sequence
    NW->UE: RACH Preamble (PRACH) Assignment
    UE->NW: RACH Preamble
    NW->UE: RACH Response
```