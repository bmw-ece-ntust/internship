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
