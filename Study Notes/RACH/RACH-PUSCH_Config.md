# PUSCH Resource Allocation

**Goals**
- [x] Understand what is PUSCH and why is it needed
- [x] Understand when PUSCH is needed
- [x] Understand the mechanism of PUSCH allocation

**What I have learned**
- Understanding of what is PUSCH and why is it needed.
- Understanding of when PUSCH is needed
- Understanding of the workings of PUSCH
- Understanding of how PUSCH is mapped in Time and frequency domain.
- Understanding of the configuration needed for PUSCH.

---

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
