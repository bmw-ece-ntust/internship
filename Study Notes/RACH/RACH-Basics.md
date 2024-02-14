# RACH Study Note
###### tags: `TEEP`

 
 
[toc]

:::success
**Goals**
- [x] Learn about the background RACH
- [x] Learn about the detasiled mechanism for 4-Step RACH
- [x] Learn about the frequency and time domain allocation for each RACH Channel

\
**What I have learned**
- An understanding what is RACH and why and when it is needed.
- An understanding of how RACH Procedure works
:::

---

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

## Channel Allocations and Configurations

### PRACH Resource Configuration
Prior to the MSG1 process the gNB will broadcast SS/PBCH signal block order to provide the gNB RSRP Measurement, this measurement will determine which SS/PBCH block and gNB to use. In this step, the gNB also sends RACH related information using `RACH-ConfigCommon` which includes configuration for PRACH within `prach-ConfigurationIndex`.

> **This initial transmission includes serveral important parameters:**
> 
> Configuration of PRACH transmission Parameters which are defined in `prach-ConfigurationIndex`
>     
> * PRACH Preamble Format
> * Time Resources
> * Frequency Resources
> 
> Parameters for determining the root sequences and their cyclic shifts in the PRACH Preamble sequence set
> * index to logical root sequence table
> * Cyclic Shift(Ncs)
>  * Set Type (unrestricted, restricted set A or restricted set B)

#### Time Domain Allocation
The PRACH settings is in `prach-ConfigurationIndex`. This configuration will take input in form of INTEGER {0...255} which each value corresponds to a unique PRACH configuration. The parameters that will be adjusted 

::: info
Details for all configuration can be seen on **[TS 38.211]([here](https://www.etsi.org/deliver/etsi_ts/138200_138299/138211/16.02.00_60/ts_138211v160200p.pdf))**
:::
1. **Preamble Format**: Preamble format to use
2. **$n_{sfn}$**: Radio frame in the UE will transmit PRACH
3. **SF Number**: Subframe in which RACH Ocassion are configured
4. **Starting Symbol**:
5. **Number of PRACH Slots within SF**:
6. **Number of Time-Domain ROs within PRACH Slot**:
7. **PRACH Duration**:

**Example 1:** PRACH Configuration Index = 0
| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 27 | 0 | x = 1, y = 0 | 0,1,2,3,4,5,6,7,8,9 | 0 |- | - | 0 |

In this case, x is 16 and y = 1. It means UE is allowed to transmit PRACH in every odd radio frame (i.e, the radio frame meeting $n_{SFN}$ mod 16 = 1).  UE is allowed to transmit the PRACH at SFN = 1, 17, 33, ....
In this case, Subframe number is set to 1. It means that UE can transmit PRACH at the subframe 1 within the radio frame determined as above.
 
**Example 2:** PRACH Configuration Index = 27
| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 27 | 0 | x = 16, y = 1 | 1 | 0 |- | - | 0 |

In this case, x = 1 and y = 0. It means UE is allowed to transmit PRACH in radio frame (i.e, the radio frame meeting n_SFN mod 1 = 0). UE is allowed to transmit at every SFN.
In this case, Subframe number is set to 0,1,2,3,4,5,6,7,8,9. It means that UE can transmit PRACH at any subframe within the radio frame determined as above.

---
**Exercise: Draw timing diagram for PRACH config index = 40 and 100 (FR1 Unpaired spectrum)**
>**Key details:**
>
>- PRACH Length is determined by the preamble format, sum of $T_{CP}$ and $T_{SEQ}$. [Details](https://www.sharetechnote.com/html/5G/5G_RACH.html#TimeDomainStructure_of_Preamble_Format)
>- PRACH Slots location is determined by the starting symbol. [Details](https://www.sharetechnote.com/html/5G/5G_RACH.html#TimeDomain_RO_Ex)

| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 40 | 3 | x = 16, y = 1 | 9 | 0 |- | - | 0 |

- Preamble format = 0, PRACH length = $T_{CP} + T_{SEQ} \approx 0.9038$ ms

    $28 \cdot 0.9038 = 25.3  \text{ Slot} $
![Preamble 0](https://imgur.com/DYFYlcw.png)
- Starting Symbol = 0, the frame starts from 0

    ![40](https://imgur.com/L2c1J0b.png)


| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 100 | A2 | x = 1, y = 0 | 9 | 9 |1 | 1 | 4 |

- **PRACH Length**
    Preamble format = A2, PRACH length = $T_{CP} + 4 \cdot T_{SEQ} \approx 0.2856$ ms

     $28 \cdot 0.2856 = 7.9968  \text{ Slot} $
     >Seeing examples from this [example](https://www.sharetechnote.com/html/5G/5G_RACH.html#TimeDomain_RO_Ex), the slot is somehow divided by two. so it will be 3,9984

    ![Preamble A2](https://imgur.com/iKIArzj.png)

- **PRACH Slots**

    Using this equation
    > $$ l = l_0 + n^{RA}_{t} N^{RA}_{dur} + 14 \cdot n^{RA}_{slot}  $$
    > $$ l = 9 + 0 \cdot 4 + 14 \cdot 1 = 23 $$
    > ---
    > $$l_0 = \text{Starting Symbol = 9}$$
    > $$ n^{RA}_{t} = \text{0 to (Number of Time-Domain ROs within PRACH Slot - 1) = [0]}$$
    > $$N^{RA}_{dur} = \text{PRACH Duration} = 4$$
    > $$n^{RA}_{slot} = [1]$$
    > ![N RA Slot](https://imgur.com/qqDxl2B.png)

    ![100](https://imgur.com/gAVspSY.png)


---

#### Frequency Domain Allocation
For PRACH, allocation for frequency domain is handled by `msg1-FDM` and `msg1-FrequencyStart`

 **msg1-FDM**: Indicates the number of RACH Occasion
 **msg1-FrequencyStart**: Indicates the offset for the lowest frequency in PRACH Occasion
 
![image](https://hackmd.io/_uploads/SkpBCwC_p.png)

 
##### RACH Occasion

RACH Occasion is an area specified in time and frequency domain that are available for the reception of RACH preamble.

**Basic Idea:**
- The gNB will transmit multiple SSBs (Sync Signal Block)
- The UE will select the best among those SSB and send PRACH using that beam
- gNB needs to figure out which beam is selected by the UE.
- By detecing which RO UE send PRACH to, NW can figure out which SSB Beam that UE has selected.

Mapping for RACH Occasion is determined by
- `msg1-FDM`: specifies how many RO are allocated in frequency domain (at the same location in time domain).
- `ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 
    - `ssb-perRACH-Occasion`: how many SSB can be mapped to one RO
    - `CB-PreamblesPerSSB`: how many premable index can be mapped to single SSB.
    - `totalNumberOfRA-Preambles`: Total Number of Preambles available per RO


**Visualisation for RACH Occasion**


`msg1-FDM`= 1
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 2:16
![image](https://hackmd.io/_uploads/ry0V8_Cu6.png)
:::


`msg1-FDM`= 2
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 1/2:4
![image](https://hackmd.io/_uploads/rJjvpd0u6.png)

`msg1-FDM`= 4
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 1/2:8

**SSB 2 SHOULD BE SSB 1**
![image](https://imgur.com/YuknR6k.png)

`msg1-FDM`= 1
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 4:8
![image](https://imgur.com/ZD1lg2F.png)




> Visualization for these parameters can be shown in this [website](https://www.nrexplained.com/ra_msg1)


>**Association Period:**
>
>Timeframe during which the mapping of SS/PBCH block indexes to PRACH occasions is performed. The association period starts from frame 0 and is determined based on the smallest value in a set determined by the PRACH configuration period according to Table 8.1-1. This mapping ensures that SS/PBCH block Tx indexes are associated with PRACH occasions.
> 
>**Association Pattern Period:**
>
>Asociation pattern period includes one or more association periods and is designed to repeat the pattern between PRACH occasions and SS/PBCH block indexes at most every 160 milliseconds. If, after an integer number of association periods, there are PRACH occasions or preambles not mapped to SS/PBCH block indexes, those PRACH occasions or preambles are not used for PRACH transmissions.
>
>**Summary:** 
>
>the association period and association pattern period are defined to establish a mapping pattern between SS/PBCH block indexes and PRACH occasions in a 5G or beyond cellular network, ensuring efficient and systematic utilization of resources for Random Access procedures.





---

Specification for RACH-ConfigCommon based on **3GPP TS 38.331**
```
RACH-ConfigCommon ::= SEQUENCE {
    rach-ConfigGeneric                      RACH-ConfigGeneric,
    totalNumberOfRA-Preambles               INTEGER (1..63) OPTIONAL, -- Need S
    ssb-perRACH-OccasionAndCB-PreamblesPerSSB CHOICE {
        oneEighth               ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        oneFourth               ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        oneHalf                  ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        one                       ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        two                       ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32},
        four                      INTEGER (1..16),
        eight                     INTEGER (1..8),
        sixteen                  INTEGER (1..4)
    } OPTIONAL, -- Need M
    groupBconfigured SEQUENCE {
        ra-Msg3SizeGroupA          ENUMERATED {b56, b144, b208, b256, b282, b480, b640,
                                               b800, b1000, b72, spare6, spare5,spare4, spare3, spare2, spare1},
        messagePowerOffsetGroupB    ENUMERATED { minusinfinity, dB0, dB5, dB8, dB10, dB12, dB15, dB18},
        numberOfRA-PreamblesGroupA  INTEGER (1..64)
    } OPTIONAL, -- Need R
    ra-ContentionResolutionTimer          ENUMERATED { sf8, sf16, sf24, sf32, sf40, sf48, sf56, sf64},
    rsrp-ThresholdSSB                      RSRP-Range OPTIONAL, -- Need R
    rsrp-ThresholdSSB-SUL                  RSRP-Range OPTIONAL, -- Cond SUL
    prach-RootSequenceIndex CHOICE {
        l839             INTEGER (0..837),
        l139             INTEGER (0..137)
    },
    msg1-SubcarrierSpacing                SubcarrierSpacing OPTIONAL, -- Cond L139
    restrictedSetConfig                      ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB},
    msg3-transformPrecoder               ENUMERATED {enabled} OPTIONAL, -- Need R
    ...,
    [[
    ra-PrioritizationForAccessIdentity-r16 SEQUENCE {
        ra-Prioritization-r16                  RA-Prioritization,
        ra-PrioritizationForAI-r16              BIT STRING (SIZE (2))
    } OPTIONAL, -- Cond InitialBWP-Only
    prach-RootSequenceIndex-r16 CHOICE {
        l571             INTEGER (0..569),
        l1151            INTEGER (0..1149)
    } OPTIONAL -- Need R
    ]]
}


```
**Note that this configuration has rach-ConfigGeneric within it**

```
RACH-ConfigGeneric ::= SEQUENCE {
    prach-ConfigurationIndex                    INTEGER (0..255),
    msg1-FDM                                    ENUMERATED {one, two, four, eight},
    msg1-FrequencyStart                         INTEGER (0..maxNrofPhysicalResourceBlocks-1),
    zeroCorrelationZoneConfig                   INTEGER(0..15),
    preambleReceivedTargetPower                 INTEGER (-202..-60),
    preambleTransMax                            ENUMERATED {n3, n4, n5, n6, n7, n8, n10, n20, n50, n100, n200},
    powerRampingStep                            ENUMERATED {dB0, dB2, dB4, dB6},
    ra-ResponseWindow                           ENUMERATED {sl1, sl2, sl4, sl8, sl10, sl20, sl40, sl80},
    ...,
    [[
    prach-ConfigurationPeriodScaling-IAB-r16   ENUMERATED {scf1, scf2, scf4, scf8, scf16, scf32, scf64} OPTIONAL, -- Need R
    prach-ConfigurationFrameOffset-IAB-r16     INTEGER (0..63) OPTIONAL, -- Need R
    prach-ConfigurationSOffset-IAB-r16         INTEGER (0..39) OPTIONAL, -- Need R
    ra-ResponseWindow-v1610                    ENUMERATED { sl60, sl160} OPTIONAL, -- Need R
    prach-ConfigurationIndex-v1610              INTEGER (256..262) OPTIONAL -- Need R
    ]]
}

```
'prach-ConfigurationIndex' can be seen at [here](https://www.etsi.org/deliver/etsi_ts/138200_138299/138211/16.02.00_60/ts_138211v160200p.pdf)

:::






### PUSCH Resource Allocation
There will be something called **PUSCH Occasion (PO)** which is time slots in which UE can transmit data on PUSCH.

The UE determines when to transmit PUSCH for MsgA based on information provided by the network. This information is conveyed to the UE either through System Information Block 1 (SIB1) when the UE is not in a connected state or via dedicated signaling, such as during a handover procedure, when the UE is in RRC_CONNECTED state.

PUSCH will be transmitted after PRACH, more specifically after  N symbols of PRACH transmission

The configuration for time and frequencyt domain allocation is within `MsgA-PUSCH-Resource-r16`

<img src="https://imgur.com/hw1iixs.png" alt="drawing" width="750"/>

#### Time domain allocation
<img src="https://imgur.com/GrDMR7S.png" width="300" />

- `msgA-PUSCH-TimeDomainOffset` : Time domain offset respect to the start of PRACH Slot in number of slots
- `nrofMsgA-PO-perSlot`: Number of PO in time domain within a single slot.
- `nrofSlotsMsgA-PUSCH`: The number of consecutive slots that include PUSCH occasions
- `guardPeriodMsgA-PUSCH-r16`: Delay between two consecutive POs

#### Frequency domain allocation
<img src="https://imgur.com/vetCI7b.png" width="300"/>



- `nrMsgA-PO-FDM`: Number of PUSCH occasions available in the frequency domain.
- `guardBandMsgA-PUSCH`: Number of Resource Blocks (RBs) separating consecutive PUSCH occasions in the frequency domain.
- `frequencyStartMsgA-PUSCH`: Starting PRB of PUSCH occasion, with respect to PRB#0.
- `nrofMsgA-PO-FDM`: Number of frequency-multiplexed PUSCH occasions in a time instance.
- `nrofPRBs-PerMsgA-PO`: Number of PRBs per PUSCH occasion.
- `msgA-IntraSlotFrequencyHopping`: Indicates whether intra-slot frequency hopping for MsgA-PUSCH transmission is configured.
- `msgA-HoppingBits`: Frequency offset for the second hop if frequency hopping is configured.
#### PUSCH Occasion configuration

- `msgA-DMRS-Configuration`: DMRS parameters configuration
  <img src="https://imgur.com/PSGVUH7.png" alt="image" width="250" />
  >**DMRS** is a reference signal that is used for for channel estimation, synchronization, and data demodulation
- `msgA-MCS`: Modulation and Coding Scheme for payload within the PUSCH
  <img src = "https://imgur.com/uRSd9uk.png" width ="250"/>
  <img src = "https://imgur.com/nBTLdCM.png" width ="250"/>
- `preamble-perPUSCHresourceunit`: Mapping between RO and PO

  -   preamble-perPUSCHresourceunit = 1, Preamble & PRU one-to-one mapping
  -   preamble-perPUSCHresourceunit > 1, Preambles & PRU many-to-one mapping
  -   preamble-perPUSCHresourceunit < 1, Preamble & PRUs one-to-many mapping



## RACH Procedure (4-Step)

```sequence
    participant UE
    participant gNB
    Note left of UE: State: \n RRC IDLE
    gNB-->UE: PRACH Occasion
    UE->gNB: MSG1: RACH Preamble
    Note right of gNB: TC-RNTI\n allocation
    gNB-->UE: PDCCH: RA-RNTI from MSG1
    gNB->UE: MSG2: RACH Response
    Note left of UE: Generate Random UE_ID
    Note left of UE: Extract UL Grant
    UE->gNB: MSG3: Connection request
    gNB-->UE: PDCCH: Temporary C-RNTI 
    gNB->UE: MSG4: Contention Resolution
    Note left of UE: State: \n RRC Connectedd
```

:::success
::: spoiler **RRC Connection Overall Process:**
* The RRC state will start at `RRC_IDLE`
* gNB will broadcast SS/PBCH signal block 
     
* UE sends MSG1
* gNB Allocates Temp C-RNTI


* gNB sends PDCCH for corresponding RA-RNTI
* UE assign Random UE ID
* UE extract UL Grant from RAR
* UE sends MSG3 for connection Request
* gNB sends PDCCH for corresponding Temporary C-RNTI
* gNB sends MSG4 Contention Resolution
* RRC Connected
:::





### 1. **Msg1 (Preamble Transmission):** 

The UE randomly selects a preamble from predefined short and long formats and transmits it on the PRACH with a randomly chosen sequence number. The preamble will be used by the gNB to calculate the delay between the UE and gNB
     
    
This preamble associated with RA-RNTI (Identifier)
$$\text{RA-RNTI}={1 + s_{id} + 14 \cdot t_{id} + 14 \cdot 80 × f_{id} + 14 \cdot 80 \cdot 8 \cdot \text{ul_carrier_id}}$$
    
::: info
::: spoiler **Details for RNTI (Radio Network Temporary Identifier)**
 Used to differentiate and identify
    * connected UE in cell / specific radio channel
    * group of UEs in case of paging / for which power control is issued by eNB
    * system information transmitted for all UEs by gNB
        ![image](https://hackmd.io/_uploads/ryDgttKua.png)
:::
     
     
### 2. **Msg2 (Random Access Response):**
    
The RAR message is used to allocate resources and provide instructions to the UE after it transmits a Random Access Preamble during the random access procedure. In this step the gNB will transmit RAR corresponding to the RA-RNTI from the UE,
    
* The UE attempts to detect a PDCCH carrying a DCI (Downlink Control Information) with the corresponding RA-RNTI within the specified RAR-Window (Random Access Response Window).
    
* Both frequency domain and time domain resource allocations are specified by the DCI Format. The DCI provides instructions related to the allocation of resources for the Random Access Response (RAR) procedure.

        
::: success
::: spoiler **More about DCI**

**Downlonk Control Information**
* Carried within PDDCH Channel
* Main purpose:
* PDSCH and PUSCH Scheduling
* Power control for PUCCH and PUSCH 
            
            
DCI has serveral formats, which one is being used is determined by the RNTI Type
        ![image](https://hackmd.io/_uploads/S13VsSrdp.png)

:::

* The UE receives the PDCCH, and upon successful decoding, proceeds to decode the PDSCH (Physical Downlink Shared Channel) associated with the PDCCH. The PDSCH carries the RAR data.
*  Inside the RAR data, there is a field known as RAPID (Random Access Preamble ID). The UE checks if the RAPID in the RAR data matches the RAPID assigned to the UE during the random access preamble transmission.

::: info
::: spoiler **Data structure of MAC PDU that carries the response**
Each MAC PDU consists of one or more MAC subPDU. In case or RAR, each subPDU can consists of the following:

>**MAC subheader + Backoff Indicator**
>| E | T | R | R | BI |
>|-|-|-|-|-|


>**MAC subheader + RAPID**
>| E | T | RAPID |
>|-|-|-|

>**MAC subheader + RAPID + MAC RAR Payload**
>| E | T | RAPID | RAR PAYLOAD |
>|-|-|-|-|

            
   **RAR Payload PDU:**
    
<img src="https://hackmd.io/_uploads/HJeWOIBua.png" alt="drawing" width="500"/>

   Details:

   - **E (Extension):** Indicates if more MAC subPDUs follow. "1" means more follow, "0" means it's the last in the MAC PDU.
    - **T (Type):** Flags the presence of either a Backoff Indicator (T=0) or a Random Access Preamble ID (T=1) in the subheader.
    - **R (Reserved):** Reserved bit, always set to "0."
    - **BI (Backoff Indicator):** 4-bit field to adjust backoff timer
        ![image](https://hackmd.io/_uploads/H1ljK8S_a.png)
    - **RAPID (Random Access Preamble ID):** 6-bit field identifying transmitted Random Access Preamble. If RAPID corresponds to SI request, MAC RAR is not included in the MAC subPDU.
    * Timing Advance Command: 12-bit field indicating the TA index for timing adjustment control in TS 38.213 [6]. TA is needed for establish sync due to signal delay.
    * **UL Grant**: 27-bit field specifying uplink resources in TS 38.213. This is for assigning the initial Resource to UE in order for it to use PUSCH [6].
        ![image](https://hackmd.io/_uploads/BJ0QcLH_p.png)

* **Temporary C-RNTI**: 16-bit field indicating the temporary identity used by the MAC entity during Random Access.


:::
    
### 3. **Msg3: Connection request** 



**Carried within PUSCH channel:**
Using the initial uplink grant from Msg2, the UE sends Msg3 on the PUSCH, which is scheduled from the UL Grant in msg2. Temporary C-RNTI is used to identify individual UE. UE_ID and EstablishmentCause are also sent.

The frequency domain for the PUSCH is determined by the steps below:
* If the active UL BWP and the initial UL BWP have the same Subcarrier Spacing and the same CP (Cyclic Prefix) length, and the active UL BWP includes all RBs of the initial UL BWP, or the active UL BWP is the initial UL BWP, then the initial UL BWP is used.
* Else:
  * RB numbering starts from the first Resource Block (RB) of the active UL BWP.
  * The maximum number of RBs for frequency domain resource allocation equals the number of RBs in the initial UL BWP.

UE will determine the subcarrier spacing and whether or not to use transform precoding.

The CRC value will be scrambled by TC-RNTI by the UE before sending it. The gNB will descramble it and verify its integrity.
    
    


### 3. **Msg4 (Contention Resolution):** 

After Msg3 is transmitted, a contention resolution timer will be started. This timer will be used as the time limit for the contention resolution process. After starting the timer, the UE will monitor the PDCCH with the gNB with the corresponding Temporary C-RNTI.

In this step, if the gNB receives multiple Msg3 at the same time, only one message can be decoded. This successfully decoded message will result in the Temporary C-RNTI becoming permanent. This message is then sent to the UE, where it will change its state from RRC_IDLE to RRC_Connected.

For messages that fail to be decoded, the contention resolution is considered failed. If the contention resolution fails, the UE will:
* Flush the HARQ Buffer
* Increment the preamble transmission counter
  * If the counter reaches the limit and the RACH procedure is triggered for System Information (SI) request, the RACH procedure will be considered failed.

If the RACH procedure fails, the UE will select a random number as a backoff timer. The backoff/delay helps in reducing the probability of collision when multiple UEs are involved. The UE will then start the process all over again after the given backoff time, unless the parameters for Contention Free are used, in which case the backoff timer will be ignored.

In this step, HARQ will be used.

If the UE is in a handover mechanism, the scrambling of the CRC will use the C-RNTI.
   
   
## RACH Procedure (2-Step)
<img src="https://imgur.com/1YRwKu2.png" alt="drawing" width="500"/>

2-Step RA Procedure is basically the simplified version of the 4-Step one. This procedure works by combining Preamble + PUSCH into one Msg as MSG-A and RAR + CR into MSG-B.
2-Step Random Access procedure in 5G NR networks aims to enhance the efficiency and performance of the random access process by reorganizing the transmission of initial access messages into two streamlined steps, thereby reducing latency and control-signaling overhead.
**When 2-Step RA is being used:**
- UE is in RRC-connected active mode in handover
- When transitioning from RRC-connected inactive mode to RRC- connected active mode

<img src="https://imgur.com/amdPP0O.png" alt="drawing" width="500"/>

### MsgA
MsgA consist of **PRACH Preamble** and **PUSCH Payload**. 
Those two component are divided using TDM. With `MsgA-PRACH` is transmitted fisrst followed by `MsgA-PUSCH`. The time offset of those two transmission is given below

<img src="https://imgur.com/nDwgJtc.png" alt="drawing" width="500"/>

In 4-step RA, the resource for PUSCH is determined by the RAR response from the gNB. Because in 2-Step RA the PUSCH is transmitted at the first message, the resource allocation for the PUSCH will be preconfigured like the PRACH. 

The preamble and PUSCH contents are the same as on the 4-Step RA.
In this initial transmission, the UE might already have C-RNTI, the UE would send C-RNTI MAC CE within MsgA. Depending upon the scenario in which RA procedure is triggered, the UE may also include additional information such as `RRCReconfigurationComplete`. If not, UE will send CCCH SDU.

### MsgB
After sending MsgA, the UE will monitor the RA Response containing CRC scrambled by the corresponding with C-RNTI or MsgB-RNTI (depending whether the MsgA contains C-RNTI or not) from the previous transmission from the gNB within the response window.

**a. If UE Decodes MsgB Successfully**

**If C-RNTI is used:**
- If the UE included C-RNTI MAC CE in MsgA, the UE considers the Random Access (RA) procedure successfully completed.
- The network's response could include an uplink grant or downlink assignment addressed to C-RNTI. Additionally, adjustments to the UE's uplink timing may be sent through the Absolute Timing Advance Command MAC CE subPDU.

**If MsgB-RNTI is used:**
- MsgB contents could be fallbackRAR, successRAR, or Backoff Indicator (BI).

    1. **fallbackRAR** (gNB unable to decode MsgA-PUSCH correctly):
        <img src="https://imgur.com/OdIwU6f.png" alt="drawing" width="500"/>
        - If MsgB contains fallbackRAR MAC subPDU, the UE switches to 4-step RA type by retransmitting Msg3 (retransmission of MsgA-PUSCH).
        - If 2-step RA type was initiated as CFRA procedure, the UE considers the RA procedure successful even if it receives fallbackRAR.

    2. **successRAR** (successRAR - gNB successfully decodes MsgA-PUSCH):

        <img src="https://imgur.com/BWKBEiM.png" alt="drawing" width="500"/>
        - If successRAR MAC subPDU is received, the UE processes Timing Advance Command, PUCCH resource Indicator, and HARQ feedback Timing Indicator for transmitting MsgB HARQ feedback.
        - The UE checks if the CCCH SDU included in MsgA and the received Contention Resolution Identity match. If matched, the UE considers the RA procedure successfully completed.
   

**b. If UE failed to decode MsgB** 
- The UE continues to decode until the expiration of msgB-ResponseWindow.
- If no valid response is received during msgB-ResponseWindow, the UE either re-transmits MsgA or falls back to 4-step RA type and starts transmitting Msg1.
- The msgA-TransMax field defines the maximum number of MsgA preamble transmissions before switching to 4-step RA type.
- If configured, the UE retransmits MsgA for msgA-TransMax-1 times and then falls back to 4-step RA type.
- Once switched to 4-step RA type, the UE starts transmitting Msg1, continuing until the total number of preamble transmissions reaches the value configured by preambleTransMax.


 ---
 
 
 

## References
::: info
*  https://www.sharetechnote.com/html/5G/5G_RACH.html#Overall_Procedure
*  https://www.sharetechnote.com/html/RACH_LTE.html
*  https://www.5gfundamental.com/2020/04/topic-5gnr-random-access-procedure.html
*  https://hackmd.io/89sw-W8xRBmJB-P_GTm-KA?both#2-Step-RA-vs-4-Step-RA-Contention-based
*  https://hackmd.io/@YTL0307/rkEGVu2Eu
*  https://www.telecomtrainer.com/explain-the-concept-of-the-random-access-response-rar-message-in-lte/#:~:text=In%20summary%2C%20the%20Random%20Access,steps%20in%20the%20access%20process.
*  https://www.linkedin.com/pulse/5g-nr-cbra-procedure-unraveling-dynamics-msg3-pusch-transmission-zwpye/
*  https://ieeexplore.ieee.org/document/9449057
*  http://howltestuffworks.blogspot.com/2020/04/5g-nr-2-step-random-access-procedure.html
*  https://www.linkedin.com/pulse/2-step-rach-5g-nr-syed-mohiuddin/
*  TS 38.211
*  TS 38.213
*  TS 38.214
*  TS 38.221
*  TS 38.321
*  TS 38.331
:::    
    













 
 
 