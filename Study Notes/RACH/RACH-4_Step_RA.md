# RACH Procedure (4-Step)


**Goals**
- [x] Understand the process of 4-Step RA Process and when it is needed
- [x] Understand the configuratio  for 4-Step RA Process

**What I have learned**
- Understanding of the steps needed for 4-Step RA Process
- Understanding the crucial configuration for 4-Step RA process
- Understanding limitiations when using 4-Step RA

---
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

 **RRC Connection Overall Process:**
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