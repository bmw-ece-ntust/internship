# SCH Message Router
File **sch_msg_router.c** in 5G NR SCH is a C source code SSI (Service-Specific Interface) Interface Implementation

## Task Initiation function
Description:

This function is supplied as one of parameters during MAC's task registration. MAC will invoke this function once, after it creates and attaches this TAPA Task to a system task.

```
uint8_t schActvInit(Ent entity, Inst instId, Region region, Reason reason)
```

Parameter:
* **Ent** Entity, the entity ID of this task.
* **Inst** Inst, the instance ID of this task
* **Region** Region, the region ID registered for memory usage of this task
* **Reason** Reason

Return:
* **ROK** (uint8_t)

## Task Activation callback function
Description:

Primitives invoked by SCH's users/providers through a loosely coupled interface arrive here by means of SSI's message handling. This API is registered with SSI during the Task Registration of SCH.

```
schActvTsk(Pst *pst, Buffer *mBuf)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **Buffer** *mBuf, Packed primitive parameters in the buffer

Return:
* **ROK** (uint8_t)

## Call Flow Debug Log
Description:

Function prints src, dest, msg infor about all the msgs that received

```
#ifdef CALL_FLOW_DEBUG_LOG
void callFlowSchMsgRouter(Pst *pst)
{
    .
    .
}
#endif
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.

Return:
* **void**

## SCH Message Router
Description:

This function invoked by schActvTsk to the set execution of SCH function according to the parameter

```
uint8_t SchMessageRouter(Pst *pst, void *msg)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **void**     *msg, Message.

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

## SCH Message Router Function
To control the task flow of the 5G NR SCH, schMessageRouter will invoke SCH Message Router Sub-function for each case explained below

### Layer Manager Configuration request handler
Description:

This function handles the configuration request received at scheduler instance from the Layer Manager.
* Based on the cfg->hdr.elmId.elmnt value it invokes one of the functions rgHdlGenCfg() or rgHdlSapCfg().
* Invokes RgMiLrgSchCfgCfm() to send back the confirmation to the LM.

```
uint8_t SchProcGenCfgReq(Pst *pst, RgMngmt *cfg)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **RgMngmt** *cfg, the configuration parameter's structure

Return:
* **ROK** (uint8_t)

### Store the slice configuration Sch DB
Description:

function is used to store the slice configuration Sch DB.

```
SchProcSliceCfgReq(Pst *pst, SchSliceCfgReq *schSliceCfgReq)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchSliceCfgReq** *schSliceCfgReq, SCH Slice Configuration Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Store the slice reconfiguration Sch DB
Description:

function is used to store the slice reconfiguration Sch DB.

```
uint8_t SchProcSliceRecfgReq(Pst *pst, SchSliceRecfgReq *schSliceRecfgReq)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **schSliceRecfgReq** *schSliceRecfgReq, SCH Slice Reconfiguration Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Cell Configuration Request Handler
Description:

This function handles the cell configuration request.

```
uint8_t SchProcCellCfgReq(Pst *pst, SchCellCfg *schCellCfg)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchCellCfg** *SchCellCfg, SCH Cell Configuration Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Handling TTI indication from PHY (Slot Indication)
Description:

This function Handles TTI indication received from PHY.

```
uint8_t SchProcSlotInd(Pst *pst, SlotTimingInfo *slotInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SlotTimingInfo** *slotInd, Slot indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Add UE Configuration Req to SCH
Description:

Function to Add Ue config request from MAC

```
uint8_t SchAddUeConfigReq(Pst *pst, SchUeCfgReq *ueCfg)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchUeCfgReq**   *ueCfg, UE Configuration

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Modify UE Config request from MAC
Description:

Function to modify Ue Config request from MAC

```
uint8_t SchModUeConfigReq(Pst *pst, SchUeRecfgReq *ueRecfg)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchUeRecfgReq** *ueRecfg, UE Reconfiguration

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes UL CQI indication from MAC
Description:

Processes UL CQI indication from MAC

```
uint8_t SchProcUlCqiInd(Pst *pst, SchUlCqiInd *ulCqiInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchUlCqiInd** *ulCqiInd, UL CQI Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes DL CQI indication from MAC
Description:

Processes UL CQI indication from MAC

```
uint8_t SchProcUlCqiInd(Pst *pst, SchDlCqiInd *dlCqiInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchDlCqiInd** *dlCqiInd, DL CQI Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes PHR indication from MAC
Description:

Processes PHR (Power Headroom) ind from MAC

```
uint8_t SchProcUlCqiInd(Pst *pst, SchPwrHeadroomInd *schPhrInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchPwrHeadroomInd** *schPhrInd, PHR Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes RACH indication
Description:

Processes RACH indication

```
uint8_t SchProcRachInd(Pst *pst, RachIndInfo *rachInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **RachIndInfo** *rachInd, RACH Indication

Return:
* **ROK** (uint8_t)

### Process CRC indication
Description:

This function process CRC indication

```
uint8_t SchProcCrcInd(Pst *pst, CrcIndInfo *crcInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **CrcIndInfo** *crcInd, CRC Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes DL RLC BO info from MAC
Description:

Processes DL RLC BO info from MAC

```
uint8_t SchProcDlRlcBoInfo(Pst *pst, DlRlcBoInfo *dlBoInfo)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **DlRlcBoInfo** *dlBoInfo, DL RLC BO Info

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes BSR indiation from MAC
Description:

Processes BSR (Buffer Status Report) indiation from MAC

```
uint8_t SchProcDlRlcBoInfo(Pst *pst, UlBufferStatusRptInd *bsrInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **UlBufferStatusRptInd** *bsrInd, BSR Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)


### Processes SR UCI indication from MAC 
Description:

Processes SR UCI indication from MAC 

```
uint8_t SchProcSrUciInd(Pst *pst, SrUciIndInfo *uciInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SrUciIndInfo** *uciInd, UCI Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)



### UE Delete request from MAC to SCH
Description:

Function for Ue Delete request from MAC to SCH

```
uint8_t SchProcUeDeleteReq(Pst *pst, SchUeDelete *ueDelete)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SrUciIndInfo** *uciInd, UCI Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)



### Cell Delete request from MAC to SCH
Description:

Function for cell Delete request from MAC to SCH

```
uint8_t SchProcCellDeleteReq(Pst *pst, SchCellDeleteReq *cellDelete)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchCellDeleteReq** *cellDelete, Cell Delete Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Process RACH resource request for CFRA (Contention Free Random Access)
Description:

processes RACH resorce request from MAC for CFRA. It assigns a dedicated preamble to the UE and sends the same in RACH resource respinse

```
uint8_t SchProcRachRsrcReq(Pst *pst, SchRachRsrcReq *schRachRsrcReq)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchRachRsrcReq** *schRachRsrcReq, RACH Resouce Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)


### Process RACH resource release after CFRA
Description:

Processes RACH resorce release from MAC after CFRA. It releases the dedicated preamble alloted to the UE

```
uint8_t SchProcRachRsrcRel(Pst *pst, SchRachRsrcRel *schRachRsrcRel)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchRachRsrcRel** *schRachRsrcRel, RACH Resource Release

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Process paging indication at  SCH recevied form MAC 
Description:

Process paging indication at SCH recevied form MAC 

```
uint8_t SchProcPagingInd(Pst *pst, SchPageInd *pageInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchPageInd** *pageInd, Paging Indication

Return:
* void

### Processes DL HARQ indication from MAC 
Description:

Processes DL HARQ indication from MAC 

```
uint8_t SchProcDlHarqInd(Pst *pst, DlHarqInd *dlHarqInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **DlHarqInd** *dlHarqInd, DL HARQ Indication

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes Statistics Request from MAC
Description:

This function process the statistics request from MAC:

[Step 1] Basic validation. If fails, all stats group in stats request are rejected.

[Step 2] If basic validations passed, traverse all stats group and validate each measurement types in each group.

[Step 3] If any measurement type validation fails in a group, that group is not configured and it is added to stats-group-rejected-list in sch-stats-response message.

[Step 4] If a group passes all validation, it is added to SCH database. And the group is added to stats-group-accepted-list in sch-stats-response message.

[Step 5] sch-stats-response is sent to du app with stats-group-rejected-list and stats-group-accepted-list.

```
uint8_t SchProcStatsReq(Pst *pst, SchStatsReq *statsReq)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchStatsReq** *statsReq, Stats Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes Statistics Delete Request from MAC
Description:

Processes Statistics Delete Request from MAC 

```
uint8_t SchProcStatsDeleteReq(Pst *pst, statsDeleteReq *dlHarqInd)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchProcStatsDeleteReq** *statsDeleteReq, Stats Delete Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)

### Processes Statistics modification Request from MAC
Description:

This function process the statistics modification request from MAC:

[Step -1] Check the stored stats group list empty.

[Step - 1.1] If empty Send the rejected group list to MAC as a stats modification response.

[Step - 1.2] Else go to step 2.

[Step -2] Traverse all stats group and validate each measurement types ineach group.

[Step -3] Check for any failure and if failed fill the remaining group'sinfo in rejected list.

[Step -4] Else Check if the received subscriptionId and groupId match the values with the database node. 

[Step -4.1] If  matches then follow the below mentioned steps.

[Step -4.1.1] Stop the timer.

[Step -4.1.2] Reconfigure stats group by adding a new entry for this statsGroup with updated configuration in database.

[Step -4.1.3] if configured successfully, store stats info intostats mod rsp's accepted list, restart timer and go to step 4.1.4 

[Step -4.1.4] Delete the old entry of this stats group..

[Step -4.2] Else fill the group related info in stats modification responses rejected list.

[Step -5] Send the stats modification rsp to MAC

```
uint8_t SchProcStatsModificationReq(Pst *pst, SchStatsModificationReq *statsModificationReq)
```

Parameter:
* **Pst**     *pst, Post structure of the primitive task.
* **SchStatsModificationReq** *statsModificationReq, Stats Modification Request

Return:
* **ROK** (uint8_t)
* **RFAILED** (uint8_t)
