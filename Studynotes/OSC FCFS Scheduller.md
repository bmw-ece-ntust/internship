# FCFS Logics
This MD is attempting to answer and explain Wilfrid's question about what happens if there are multiple UEs. Let's say there are UE1 and UE2 in order, and UE1 is transmitting data in the first TTI and has remaining data that was unallocated in the first TTI. What will happen with that allocated data? There are two scenarios that could occur:

1. In the next TTI, the remaining data gets allocated first before the UE2.
2. After the UE2 data is allocated.

The correct answer will be explained below.

# Function Involved 
## `prbAllocUsingRRMPolicy` 

This function allocates Physical Resource Blocks (PRBs) to Logical Channels (LCs) based on a RRM policy.

<details>
<summary>Function Details</summary>


**Details:**

**Input Parameters:**

- `lcLL`: Pointer to the linked list containing the LCs (of type `CmLListCp`)
- `isDedicatedPRB`: Flag indicating whether to allocate from dedicated PRBs (True) or shared PRBs (False)
- `mcsIdx`: Modulation and Coding Scheme (MCS) index
- `numSymbols`: Number of PDSCH symbols allocated
- `sharedPRB`: Pointer to the shared PRB count (Input/Output)
- `reservedPRB`: Pointer to the reserved PRB count for dedicated LCs (Input/Output) (only used if `isDedicatedPRB` is True)
- `isTxPayloadLenAdded`: Pointer to a flag indicating if the TX payload header length has been added to the BO requirement (Input/Output) (used for Downlink)
- `srRcvd`: Pointer to a flag indicating if an UL grant size has been received (Input/Output) (used for Uplink)

**Return:**

- The function does not return any value (void).

**Process:**

1. **Error Handling:**
   - If the `lcLL` is NULL, logs an error and exits.

2. **Initialization:**
   - Sets `remReservedPRB` to the value pointed to by `reservedPRB` (only for dedicated LCs).

3. **Traverse LC List:**
   - Iterates through each node in the `lcLL`:
     - Skips LCs with zero requested BO (bandwidth requirement) and allocated BO (already fully allocated).
     - Checks for loop exit conditions:
       - All LCs are allocated (no LCs with `allocBO` equal to zero).
       - PRBs are exhausted (either `remReservedPRB` and `sharedPRB` are zero for dedicated LCs, or `sharedPRB` is zero for default LCs).
   - If loop exits, the function returns.

4. **Calculate Maximum PRB:**
   - For dedicated LCs, calculates the maximum PRB by adding `remReservedPRB` and `sharedPRB`.
   - For default LCs, the maximum PRB is simply the value of `sharedPRB`.

5. **Allocation for First LC:**
   - If `isTxPayloadLenAdded` is not NULL and `*isTxPayloadLenAdded` is False (for Downlink), adds the TX payload header length to the requested BO for the current LC (as it's the first one being allocated).
   - If `srRcvd` is not NULL and `*srRcvd` is True (for Uplink), adds the UL grant size to the requested BO for the current LC.

6. **Estimate PRB and BO:**
   - Calls `calculateEstimateTBSize` to estimate the PRB and BO that can be allocated to the current LC based on its requested BO, the MCS index, number of symbols, and maximum PRB.

7. **Update PRB Counts:**
   - If allocating from dedicated PRBs and the estimated PRB is less than or equal to `remReservedPRB`:
     - Deducts the estimated PRB from `remReservedPRB`.
   - Otherwise (allocating from shared PRBs or dedicated PRB not sufficient):
     - If `sharedPRB` is less than the difference between the estimated PRB and `remReservedPRB`, sets `sharedPRB` to zero (shared PRBs exhausted).
     - Otherwise, deducts the difference between the estimated PRB and `remReservedPRB` from `sharedPRB`.
   - Sets `remReservedPRB` to zero (if not already).

8. **Update LC Information:**
   - Deducts the allocated BO from the requested BO of the current LC.
   - Sets the allocated PRB for the current LC.
   - Moves the current node to the tail of the linked list (to prioritize unallocated LCs in the next iteration).

9. **Next Iteration:**
   - Moves to the first node of the linked list for the next iteration.

</details>

## `schFcfsScheduleDlLc`

This function grants resources to Logical Channels (LCs) for downlink transmission using a First-Come-First-Served (FCFS) scheduling policy.

<details>
<summary>Function Details</summary>

**Details:**

**Input Parameters:**

- `pdcchTime`: PDCCH time information (Slot timing)
- `pdschTime`: PDSCH time information (Slot timing)
- `pdschNumSymbols`: Number of symbols allocated for PDSCH
- `startPrb`: Starting PRB (Physical Resource Block)
- `isRetx`: Flag indicating a retransmission (True) or new transmission (False)
- `hqP`: Pointer to the scheduler HQ (HARQ) processing context CB

**Return Value:**

- `uint32_t`: Accumulated size of the scheduled data (in bytes)

**Process:**

1. **Initialization (for new transmissions only):**
   - Initializes scheduled LC data and accumulated size to zero.
   - Iterates through all LCs of the UE and updates the requested PRB and payload size in the corresponding LC list (dedicated or default) if the LC has a non-zero BO (Bandwidth Requirement).

2. **Check for Pending BO:**
   - If there are no LCs with pending BO (both dedicated and default lists are empty), exits the function, indicating no scheduling required for this UE.

3. **Find Largest Free Block:**
   - Finds the largest free PRB block available in the downlink direction for the UE's cell.

4. **PRB and BO Estimation:**
   - If there is no retransmission and free PRBs are available:
     - Determines the MCS index based on the UE's configuration.
     - Allocates PRBs to dedicated LCs first, considering their reserved PRBs.
     - If there are remaining PRBs, allocates them to default LCs using the `prbAllocUsingRRMPolicy` function.
   - In case of a retransmission, the function uses the requested size from the `tbInfo` of the HQ processing context.

5. **Scheduled Bytes Calculation:**
   - If this is a new transmission (not a retransmission):
     - Calculates the exact number of scheduled bytes for dedicated LCs and updates the corresponding Downlink DCI message allocation report.
     - Calculates the scheduled bytes for default LCs and updates the DCI message allocation report.

6. **Return:**
   - Returns the accumulated size of the scheduled data.
   - If no LCs were allocated due to resource limitations:
     - Returns zero and logs a message if no free PRBs were found.
     - Otherwise, logs a message indicating no LCs were scheduled.

**Additional Notes:**

- The `isTxPayloadLenAdded` flag is used to keep track of whether the TX payload header length has been added to the BO requirement for the first LC being allocated.
- The function handles scenarios where there might not be enough free PRBs to satisfy the reserved PRBs for dedicated LCs.

</details>

## `updateLcListReqPRB` 

This function updates the Requested PRB (ReqPRB) for a specific Logical Channel (LC) identified by its ID within a Linked List containing LC information.

<details>
<summary>Function Details</summary>

**Details:**

**Input Parameters:**

- `lcLL`: Pointer to the linked list containing the LCs (of type `CmLListCp`)
- `lcId`: ID of the target LC
- `payloadSize`: Size of the payload (in bytes) to be transmitted on the LC

**Return Value:**

- `uint8_t`:
  - `ROK`: Function execution successful
  - `RFAILED`: Function execution failed

**Process:**

1. **Find LC Node:**
   - Calls the `handleLcLList` function (assumed to be defined elsewhere) to find the LC node with the matching `lcId` in the `lcLL`.
   - If the LC is not found and cannot be created (using `CREATE` argument to `handleLcLList`), logs an error and returns `RFAILED`.

2. **Update LC Information:**
   - If the LC node is found:
     - Sets the `reqBO` (requested BO) of the LC node to the provided `payloadSize`.
     - Resets the `allocBO` (allocated BO) to zero.
     - Re-initializes the `allocPRB` (allocated PRB) to zero.

3. **Return:**
   - Returns `ROK` to indicate successful update.


</details>


## `schFcfsScheduleSlot` 

Schedules slots in UL and DL for FCFS scheduling

<details>
<summary>Function Details</summary>

**Details:**

**Input Parameters:**
- `cell`: Pointer to the cell control block
- `slotInd`: Slot timing information
- `schInst`: Scheduler instance

**Return:**
- The function does not return any value (void).

**Process:**
1. **Retrieve FCFS Cell and UE List:**
   - Retrieves the FCFS cell control block and the list of UEs to be scheduled.
2. **Iterate Through Pending UEs:**
   - Iterates through the list of pending UEs.
   - For each UE, the following tasks are performed:
     - Checks if there are any pending RAR (Random Access Response), MSG4, DL (Downlink) data, or UL (Uplink) grant requests.
     - If any of these requests are pending, attempts to schedule them in the current slot.
     - If the scheduling is successful, removes the UE from the pending list.
     - If the scheduling fails, moves the UE to the end of the pending list for later scheduling.
3. **Handle Retransmissions:**
   - Handles retransmissions for MSG3, MSG4, DL data, and UL grants.
4. **DRX Handling (Commented):**
   - The function contains commented sections related to DRX (Discontinuous Reception) handling, suggesting potential integration with DRX functionality.
5. **Resource Availability Check:**
   - Continues the iteration until all UEs in the pending list are processed or the available resource blocks (PRBs) are exhausted.

</details>

## `schFillBoGrantDlSchedInfo` 
This function schedules Downlink (DL) transmissions for a specific UE (User Equipment) by allocating Physical Resource Blocks (PRBs) and filling the Downlink Control Channel (DL-CC) information.

<details>
<summary>Function Details</summary>

**Details:**

**Input Parameters:**

- `cell`: Pointer to the cell data structure (`SchCellCb`)
- `currTime`: Current slot timing information (`SlotTimingInfo`)
- `ueId`: ID of the UE
- `isRetx`: Flag indicating a retransmission (True) or new transmission (False)
- `hqP`: Double pointer to a pointer to the DL HARQ (Hybrid Automatic Repeat Request) processing context (`SchDlHqProcCb`) to be used for scheduling

**Return Value:**

- `bool`:
  - `true`: Function execution successful
  - `false`: Function execution failed

**Process:**

1. **UE Context and HARQ Process:**
   - Gets the CRNTI (Cell Radio Network Temporary Identifier) for the UE based on its ID.
   - Retrieves the corresponding UE control block (`SchUeCb`) from the cell data.
   - If this is a new transmission (not a retransmission):
     - Calls `schDlGetAvlHqProcess` (assumed to be defined elsewhere) to find an available HARQ process for the UE.

2. **Find Valid Slot Combination:**
   - Initializes a `SchPdcchAllocInfo` structure (assumed to hold PDCCH allocation information).
   - Calls `findValidK0K1Value` (assumed to be defined elsewhere) to find a valid combination of slots for scheduling PDCCH (Physical DL Control Channel), PDSCH (Physical DL Shared Channel), and PUCCH (Physical UL Control Channel), considering:
     - Retransmission flag (`isRetx`)
     - The provided `hqP`
     - The output arguments including slot timings for PDCCH, PDSCH, and PUCCH, and the `pdcchAllocInfo` structure.
   - If a valid slot combination cannot be found, the function exits and returns `false`.

3. **DL DCI (Downlink Control Information) Allocation:**
   - Checks if a DL DCI message allocation already exists for the UE in the current PDCCH slot using `cell->schDlSlotInfo[pdcchTime.slot]->dlMsgAlloc[ueId-1]`.
   - If not, allocates memory for the DCI message allocation (`DlMsgSchInfo`) and stores it in the cell data.
   - Fills the DCI message allocation with relevant information for the UE, including CRNTI, retransmission flag (`isRetx`), and a pointer to the HARQ process (`*hqP`).

4. **DL Resource Allocation and Scheduling:**
   - Calls the `cell->api->SchScheduleDlLc` function (assumed to be provided by an upper layer) to perform DL scheduling for the UE's LCs (Logical Channels). This function:
     - Takes the PDCCH slot timing (`pdcchTime`), PDSCH slot timing (`pdschTime`), number of PDSCH symbols (`pdschNumSymbols`), starting PRB (`startPrb`), retransmission flag (`isRetx`), and the HARQ process pointer (`hqP`) as input.
     - Returns the total size (in bytes) of the data scheduled for the UE's LCs.
   - If no data is scheduled (i.e., the return value is zero), the function exits and returns `false`.

5. **DL DCI and PDSCH Information Filling:**
   - Calls `schDlRsrcAllocDlMsg` (assumed to be defined elsewhere) to allocate PDSCH resources and fill the DL DCI message with:
     - Total scheduled size
     - PDSCH allocation information (start PRB, number of symbols)
   - If the allocation fails, the function frees the allocated memory for the DCI message and returns `false`.

6. **Scheduling Report (for future implementation):**
   - A comment block mentions updating the scheduling byte report for multiple LCs based on their Quality of Service Class Indicator (QCI) and priority. This functionality is currently not implemented (`#if 0`).

7. **DL MSG PDSCH Configuration (for separate PDSCH slot):**
   - Checks if the PDCCH and PDSCH slots are the same.
   - If they are different, allocates memory for the PDSCH configuration within the DCI message allocation (`dciSlotAlloc->dlMsgPdschCfg`).
   - Copies the PDSCH configuration information from the PDCCH DCI to the DL MSG PDSCH configuration.

8. **Updating UE BO (Bandwidth Requirement):** 
   - Iterates through all possible LCs (up to `MAX_NUM_LC`) for the UE.
   - Sets the `bo` member of each DL LC context (`ueCb->dlInfo.dlLcCtxt[lcIdx]`) in the UE control block to zero. This effectively resets the BO (bandwidth requirement) for all DL LCs.

9. **Unsetting BO Indicator:**
   - Clears the BO bit for the UE in the cell's BO indicator bitmap (`cell->boIndBitMap`). This indicates that the UE's BO requirements have been addressed.

10.  **Return Value:**
   - The function returns `true` to indicate successful scheduling.

</details>


# Analysis
From function `schFcfsScheduleSlot` 

**DL New Transmission**
```C++          
isDlMsgScheduled = schFillBoGrantDlSchedInfo(cell, *slotInd, ueId, FALSE, &hqP);
```

**DL Retransmission**
```C++
isDlMsgScheduled = schFillBoGrantDlSchedInfo(cell, *slotInd, ueId, TRUE, ((SchDlHqProcCb**) &(node->node)));
```

**UE Deletion**
```C++
if(isUlGrantPending || isDlMsgPending)
  {
    if((isUlGrantPending && !isUlGrantScheduled) || (isDlMsgPending && !isDlMsgScheduled))
    {
        cmLListAdd2Tail(&fcfsCell->ueToBeScheduled, cmLListDelFrm(&fcfsCell->ueToBeScheduled, pendingUeNode));
    }
    else
    {
    schFcfsRemoveUeFrmScheduleLst(cell, pendingUeNode);
    }
  }
```

**PRB Allocation**
```C++
if(cell->schDlSlotInfo[slotInd->slot]->prbAlloc.numPrbAlloc >= MAX_NUM_RB)
{
    DU_LOG("\nINFO   -->  SCH: No PRB available to proceed with next UE");
    return;     
}
```

Key Takeaway:
- `isDlMsgScheduled` is variable to mark if DL MSG are scheduled yet or not and it is a return variable of `schFillBoGrantDlSchedInfo`
- the UE deletion process will happened if DL MSG is Pending and DL MSG are scheduled yet (in DL Case)
- if DL MSG are not scheduled yet, the UE will be move to the end of `ueToBeScheduled` list
- In each TTI Slot, the first UE in `ueToBeScheduled` list will be prioritized, then transverse to the next UE until `numPrbAlloc >= MAX_NUM_RB`, then  then the next UE will be examined

From function `schFillBoGrantDlSchedInfo` the function will return FALSE if there is a failures in memory allocation or `accumalatedSize` is 0 because `allocBo` for all LC is 0, otherwise it will return TRUE.

Key Takeaway:
- `isDlMsgScheduled` will always return True unless `allocBo` for all LCs is 0, hence the UE will get deleted from `ueToBeScheduled` even though all BOs in the current UE are not yet scheduled.
- The UE whose BOs are not yet scheduled will be added back to the `ueToBeScheduled` using the `schFcfsAddUeToSchedule` function, which is called from various other functions such as the HARQ retransmission function, processing buffer occupancy report from RLC function, and so on.

Moreover from Wilfrid's Run Example
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
```
Key Takeaway:
- SCH allocated PRBs to the DL message, then the UE gets deleted from `ueToBeScheduled` because there are no available PRBs, even though there is remaining BO to be scheduled in the next slot.
- SCH received a BO Status Indication from RLC, which means that the UE is added back to the end of `ueToBeScheduled` with less BO than the previous transmission.

# Conclusion
Based on the analysis, SCH will attempt to schedule data transmission and then remove the current UE from the scheduling list after it has been scheduled, even if not all the data can be allocated. Then, SCH will move on to the next UE and schedule data transmission for it. The UE that was previously removed will be added back to the tail of the scheduling list and will be scheduled again afterward. Hence the 2nd scenario will be the correct answer.