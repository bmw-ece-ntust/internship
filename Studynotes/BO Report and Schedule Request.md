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
2. Transverse each LC node from `snssaiList` link list
</details>

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Function%20Flow%20Diagram%20for%20SCHMACRLC%20Bo%20reReq.png) 

Function Flow Diagram for BO Report and Schedule Request 