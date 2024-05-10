# BO Scheduling Report & Re-Request BO Scheduling Procedure
From previous study notes discussing the OSC FCFS Scheduler procedure, which concluded that scheduling for remaining unallocated data on UE1 occurs after UE2 is allocated in the next TTI (if PRBs are still available), we will now explore the procedure for reporting to RLC regarding previously scheduled data and requesting retransmission of unallocated data from UE1 by RLC to SCH for scheduling UE1 by tracing the following infromation snippets. 

**Wilfrid's Run Example**
```
...
DEBUG  -->  EGTP : Received DL Message[1]

DEBUG  -->  DU_APP : Processing DL data in duHdlEgtpDlData()
DEBUG  -->  DU_APP : Sending User Data Msg to RLC [TEID, nPDU]:[1, 1]

DEBUG  -->  RLC_DL : Received DL Data
DEBUG  -->  SCH : Received RLC BO Status indication LCId [4] BO [1240]
INFO   --> SCH: SFN:350/Slot:7, is a Valid PDCCH slot
DEBUG  -->  SCH: RBG found for cceIndex:2, AggLvl:1 and SymbolDuration2 with StartPrb:60, numPrb:3
INFO   -->  SCH: PDCCH allocation is successful at cceIndex:2
DEBUG  -->  SCH: LC:4 is the First node to be allocated which includes TX_PAYLOAD_HDR_LEN
DEBUG  -->  SCH: SharedPRB is less
DEBUG  -->  SCH: All LC are allocated [SharedPRB:0]
INFO   -->  SCH : LcID:4, [reqBO, allocBO, allocPRB]:[747,496,60]
INFO   -->  SCH: Added in MAC BO report: LCID:4,reqBO:747,Idx:0, TotalBO Size:496
DEBUG  -->  SCH: LCID4 Deleted successfully
INFO   --> SCH: In isPrbAvailable, numFreePrb:43 is less than reqPrb:59
DEBUG  -->  MAC: Send scheduled result report for sfn 350 slot 7
DEBUG  -->  RLC : Received scheduling report from MAC
DEBUG  -->  RLC : SNSSAI found in LL
INFO   -->  RLC_DL: SNSSAI List Grant:496, lcId:4, total :496
DEBUG  -->  MAC: Received DL data for sfn=350 slot=7 numPdu= 1
DEBUG  -->  SCH : Received RLC BO Status indication LCId [4] BO [749]
...
```

# Analysis
```
...
DEBUG  -->  MAC: Send scheduled result report for sfn 350 slot 7
DEBUG  -->  RLC : Received scheduling report from MAC
DEBUG  -->  RLC : SNSSAI found in LL
INFO   -->  RLC_DL: SNSSAI List Grant:496, lcId:4, total :496
DEBUG  -->  MAC: Received DL data for sfn=350 slot=7 numPdu= 1
DEBUG  -->  SCH : Received RLC BO Status indication LCId [4] BO [749]
...
```

By examining the above section of the provided information, we can search for the function that produces this output.

## `sendSchedRptToRlc (MAC)`
Description :

Send LC schedule result report to RLC

Output :
```
DEBUG  -->  MAC: Send scheduled result report for sfn 350 slot 7
```

<details>
<summary>Process:</summary>

1. **Allocate shared memory to be used**: 
   - allocate shared memory to be used for `schedRpt` (RLC schedule report)
   - if memory allocation failure return `RFAILED` and log message

2. **Log message for send scheduled result report:**
   - Log message send scheduled result report for SFN X and slot X

3. **Trigger MAC to RLC event :**
   - Fill MAC to RLC post structure by `RLC_DL_INST` and `EVENT_SCHED_RESULT_TO_RLC`
   - Invoke `MacSendSchedResultRptToRlc` function to send schedule result report to RLC
   - if function return failed, return `RFAILED` and log message

4. **Return :**
   - Return `ROK` if Send LC schedule result report to RLC done successfully
</details>

## `RlcProcSchedResultRpt (RLC)`
Description :

Handler for extracting common and dedicated channel scheduling result report.

Output :
```
DEBUG  -->  RLC : Received scheduling report from MAC
```

<details>
<summary>Process:</summary>

1. **Log message for recieving scheduled result report:** 
   - Log message recieve scheduling report from MAC

2. **Iterates through LC's:**
   - if there is one LC, Fill status info structure if at least one channel's scheduling report is received
   - Fill logical channel scheduling info

3. **Calling handler for all dedicated channels scheduling:**
   - if the return variable is still `ROK` (encouter no problem) and there is any `nmbDLch` (number of ded LC), Invoke `rlcProcDedLcSchedRpt` to triger data transfer from RLC to MAC for ded LC

4. **Return:**
    - Return `ROK` if the return variable is still `ROK` or during the process encounter no problem
</details>

## `rlcHandleSnssaiTputlist (RLC)`
Description :

This function is called whenever a new LC is configured with a snssai or to search for Snssai Node during RLC SDU formation

Output :
```
DEBUG  -->  RLC : SNSSAI found in LL
```

<details>
<summary>Process:</summary>

1. **Check the Direction of data:** 
   - Perform checking the direction of data
   - Log error message for no data direction
   - Create or find `snssaiList` based on direction and the action command

2. **Transverse each LC node from `snssaiList` link list:**
   - Transverse each LC node from `snssaiList` link list to find SNSSAI in LL and then display the found Log message and exit the loop with `found` flag set to TRUE 
   - if SNSSAI is not found in LL after transversing every node, exit the loop with `found` flag set to FALSE

3. **Switch action based on case:**
   - for search action, return the `snssaiNode` that searched
   - for create action, if found return the `snssaiNode`, else try to perform allocation of SNSSAI node
   - for delete action, perform deletion of node
   - for transverse all action, just exit the case

4. **Return:**
   - Return `snssaiNode`
</details>

## `rlcUtlSendToMac (RLC)`
Description :

sends the data for one or more logical channels after processing the SDUs and forming the PDUs.It calls UMM or AMM functions to form the PDUs for the requested sizes by MAC.

Output :
```
INFO   -->  RLC_DL: SNSSAI List Grant:496, lcId:4, total :496
```

<details>
<summary>Process:</summary>

1. **Initialization:**
    * A few variables are declared to keep track of counters, UE information, and memory allocation.
    * Memory is allocated for a `RguDDatReqInfo` structure using `RLC_ALLOC_SHRABL_BUF`. This structure will be used to send PDU information to MAC.

2. **Iterate Through UEs with Granted PDUS:**
    * The function loops through each UE grant information (`staInd`) present in `staIndInfo`.
        * For each UE grant:
            * UE control block (`ueCb`) is retrieved using the UE's RNTI (Radio Network Temporary Identifier).
            * A temporary `RlcDatReq` structure is used to accumulate PDU information for the current UE.
            * The function iterates through each TTI (Transmission Time Interval) bundling information for the UE.
                * Within each TTI, it processes each LCH (Logical Channel) information (`staIndTb`).
                    * For each LCH:
                        * It checks if the corresponding RB (Radio Bearer) control block (`rbCb`) exists and re-establishment is not in progress.
                        * If the RB is valid, the function:
                            * Updates throughput statistics for the UE and potentially for configured SNSF (Service Network Function).
                            * Calls either `rlcUmmProcessSdus` (for UM mode) or `rlcAmmProcessSdus` (for AM mode) to process SDUs and populate the `RlcDatReq` structure with PDU information.
                            * Sets relevant parameters in the `datReqTb` structure, including LCH information, BO report (Buffer Occupancy Report), and PDU information.
                    * The function accumulates the total size of PDUs for this UE.
  
3. **Send PDU Information to MAC:**
    * If there's PDU information for at least one UE (`ueDataIdx` > 0), the following steps are performed:
        * The `datReqInfo` structure is filled with relevant information like cell ID and total number of UE grants.
        * The function calls `rlcSendDedLcDlData` to send the `datReqInfo` structure containing PDU information to the MAC entity through the appropriate Service User SAP (Service Access Point).
  
4. **Memory Deallocation:**
    * If no PDU information needs to be sent (i.e., `ueDataIdx` is 0), the previously allocated memory for `datReqInfo` is freed using `RLC_FREE_SHRABL_BUF`.

</details>


## `MacProcRlcDlData (MAC)`
Description :

Processes DL data from RLC.

Output :
```
DEBUG  -->  MAC: Received DL data for sfn=350 slot=7 numPdu= 1
```

<details>
<summary>Process:</summary>

1. **Initialization:**
    * A few variables are declared to store UE ID, cell index, PDU information, and pointers.
    * The function logs a debug message indicating the received DL data details (SFN, slot, number of PDUs).
    * UE ID is extracted from the received `dlData->rnti`.
    * Memory is set to zero for the `macDlData` structure, which will be used to store processed DL data for MAC.

2. **Copy PDU Information:**
    * The function copies relevant information from `dlData` to `macDlData`. This includes UE ID, number of PDUs, LC ID (Logical Channel ID), PDU length, and PDU buffer for each PDU.

3. **Get Cell Index and Scheduled Slot:**
    * Cell index is extracted from the received `dlData->cellId`.
    * The function checks if the corresponding `macCell` for the cell exists. If not, it logs an error and returns failure.
    * A pointer to the scheduled downlink slot (`currDlSlot`) for the received information is retrieved.

4. **Process DL PDUs for Transmission:**
    * The function checks if there's already a scheduled PDSCH (Physical Downlink Shared Channel) configuration for the UE in the current slot.
        * If a PDSCH configuration exists:
            * The function calculates the maximum PDU size that can be transmitted within the allocated codeword.
            * Memory is allocated for a temporary buffer (`txPdu`) to hold the muxed (combined) PDUs.
            * If memory allocation fails, an error is logged, and the function returns failure.
            * The `macMuxPdu` function is called to combine PDUs from `macDlData` into a single buffer (`txPdu`).
            * The size and pointer to the muxed PDU are stored in the corresponding DL information for the UE in the scheduled slot.
            * The newly created transmission buffer (`txPdu`) is added to the DL HARQ (Hybrid Automatic Repeat Request) process control block for potential retransmissions.

5. **Handle BO (Buffer Occupancy) Reports:**
    * The function iterates through the received BO information for each LC in `dlData`.
        * If the BO report indicates non-zero data volume (i.e., buffer is occupied), a `DlRlcBoInfo` structure is filled with relevant details (cell ID, CRNTI, LC ID, data volume).
        * The `sendDlRlcBoInfoToSch` function is called to send this BO information to the scheduler. This information might be used for scheduling decisions.

6. **Memory Deallocation:**
    * The function frees the memory allocated for each PDU buffer received from RLC.
    * Finally, it frees the memory for the entire `dlData` structure if the service provider selector (`pstInfo->selector`) indicates LWLC (Lightweight Layer 2 Control) mode.

7. **Return:**
   - The function returns `ROK` upon successful processing of DL data.
   -  In case of any errors (e.g., memory allocation failure, missing cell information), it returns `RFAILED`.

</details>


## `SchProcDlRlcBoInfo (SCH)`
Description :

Processes DL RLC BO info from MAC.

Output :
```
DEBUG  -->  SCH : Received RLC BO Status indication LCId [4] BO [749]
```

<details>
<summary>Process:</summary>

1. **Initialization:**
    * The function logs a debug message indicating the received LC ID and BO information.
    * It retrieves the scheduler cell context (`cell`) based on the service provider instance (`pst`).
    * If the cell context is unavailable, an error is logged, and the function returns failure.
    * UE ID is extracted from the received `dlBoInfo->crnti`.
    * The function checks if data transmission for this UE is stopped based on its configuration. If so, it logs a message and returns success (no further action required).

2. **Validate LC ID:**
    * The LC ID from `dlBoInfo` is extracted and stored in `lcId`.
    * The function uses a helper function (`CHECK_LCID`) to verify if the LC ID is valid. If not, an error is logged, and the function returns failure.

3. **Process BO Information:**
    * The function handles the case of zero BO (buffer occupancy), which might indicate successful transmission or retransmission failures. In this case, it might trigger clearing the corresponding LC from the scheduler's priority list (implementation details noted as TODO).
    * If the LC ID is for SRB0 (default Service Radio Bearer):
        * A flag (`msg4recvd`) in the Random Access Control Block (RA Cb) for the UE is set to `true`, indicating a potential SRB0 message reception.
        * The `dlMsgPduLen` in the RA Cb is updated with the received BO value.
    * If the LC ID is not SRB0:
        * A bit is set in the `boIndBitMap` for the UE's cell context to indicate BO information received.
        * The function checks if the LC ID exists in the UE's DL information context (`dlLcCtxt`). If it does, the BO value is stored there.
        * If the LC ID is not found in the UE's DL context, an error is logged, and the function returns failure.

4. **Schedule DL for UE:**
    * The UE ID is added to a list of pending UEs that require scheduling decisions based on the received BO information. This is achieved by calling the scheduler's API function (`cell->api->SchDlRlcBoInfo`).

5. **Return:**
   * The function returns `ROK` upon successful processing of DL RLC BO information.
   * In case of errors (e.g., invalid cell/UE context, invalid LC ID), it returns `RFAILED`.

</details>


## Additional function that involved
- MacProcDlAlloc :
  
  function to copy dl sch info in the mac slot info and invoking `sendSchedRptToRlc` function to send LC schedule result report to RLC 

- MacSendSchedResultRptToRlc :
  
   function to send Schedule result report to RLC and invoked by `sendSchedRptToRlc` function

- rlcProcDedLcSchedRpt
   
   function to triger the data transfer from RLC to MAC for dedicated logical channels, invoked by `RlcProcSchedResultRpt` function

- rlcSendDedLcDlData

   function to store DL PDU info for all logical channels of per UE grant per TTI and sends to MAC and invoked by `rlcUtlSendToMac` function

- sendDlRlcBoInfoToSch
  
  function to send DL BO Info to SCH and invoked by `MacProcRlcDlData` function

- schFcfsDlRlcBoInfo

   function to process Buffer Occupancy report from RLC and invoked by `SchProcDlRlcBoInfo` function
 
- schFcfsAddUeToSchedule

   function to add UE to ueToBeScheduled List and invoked by  `schFcfsDlRlcBoInfo` function

## Flow Diagram
![image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Function%20Flow%20Diagram%20for%20SCHMACRLC%20Bo%20reReq.png) 

Function Flow Diagram for BO Report and Schedule Request 