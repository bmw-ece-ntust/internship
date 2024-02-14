## RACH Procedure (2-Step)


**Goals**
- [x] Understand the process of 2-Step RA Process and when it is needed
- [x] Understand the configuratio  for 2-Step RA Process

**What I have learned**
- Understanding of the steps needed for 2-Step RA Process and when to use it instead of the 4-Step one
- Understanding of configuration for 2-Step RA process
- Understanding of its advantages compared to the 4-Step one.

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