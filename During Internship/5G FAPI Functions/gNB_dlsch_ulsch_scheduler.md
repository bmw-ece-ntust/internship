## gNB_dlsch_ulsch_scheduler
> Scheduler for downlink and uplink

Protocol context initialization. Retrieves a pointer to the gNB MAC 
then accesses the common shannels structure from the gNB instance. Assert fatal is used when the condition fails it logs an error message.
```
void gNB_dlsch_ulsch_scheduler(module_id_t module_idP, frame_t frame, sub_frame_t slot, NR_Sched_Rsp_t *sched_info)
{
  protocol_ctxt_t ctxt = {0};
  PROTOCOL_CTXT_SET_BY_MODULE_ID(&ctxt, module_idP, ENB_FLAG_YES, NOT_A_RNTI, frame, slot,module_idP);

  gNB_MAC_INST *gNB = RC.nrmac[module_idP];
  NR_COMMON_channels_t *cc = gNB->common_channels;
  NR_ServingCellConfigCommon_t        *scc     = cc->ServingCellConfigCommon;
  // Assert to detect segfault during gNB teardown. scc->ssbSubcarrierSpacing pointer is most likely overwritten
  AssertFatal(
    *scc->ssbSubcarrierSpacing >= 0 && *scc->ssbSubcarrierSpacing < sizeofArray(nr_slots_per_frame),
    "ssbSubcarrierSpacing %ld is out of range, ssbSubcarrierSpacing pointer (%p) might be overwritten, known segfault condition",
    *scc->ssbSubcarrierSpacing,
    scc->ssbSubcarrierSpacing);

  NR_SCHED_LOCK(&gNB->sched_lock);
```
Check if slot is zero and operates in higher frequency bands as it needs special handling.
Then it will check TDD pattern configuration whether it's valid or not. If the TDD is valid
it calculates the number of periods per frame for undertstanding TDD structure and planning the scheduling of UL & DL transmission.


The gNB->tdd_beam_association array is re-initialized to -1 for each TDD period within the frame. This ensures that the beamforming decisions are fresh and can be re-evaluated for each period, which is crucial for maintaining optimal communication links, especially in high-frequency bands where beamforming is essential.
```
  if (slot==0 && (*scc->downlinkConfigCommon->frequencyInfoDL->frequencyBandList.list.array[0]>=257)) {
    //FR2
    const NR_TDD_UL_DL_Pattern_t *tdd = &scc->tdd_UL_DL_ConfigurationCommon->pattern1;
    AssertFatal(tdd,"Dynamic TDD not handled yet\n");
    const int nb_periods_per_frame = get_nb_periods_per_frame(tdd->dl_UL_TransmissionPeriodicity);
    // re-initialization of tdd_beam_association at beginning of frame
    for (int i=0; i<nb_periods_per_frame; i++)
      gNB->tdd_beam_association[i] = -1;
  }

  gNB->frame = frame;
  start_meas(&gNB->eNB_scheduler);
  VCD_SIGNAL_DUMPER_DUMP_FUNCTION_BY_NAME(VCD_SIGNAL_DUMPER_FUNCTIONS_gNB_DLSCH_ULSCH_SCHEDULER,VCD_FUNCTION_IN);
```

send tick to RLC, PDCP, and X2AP every ms. PDCP (Packet Data Convergence Protocol) and RLC (Radio Link Control) are two key protocol layers in the radio interface stack
X2 Application Protocol (X2AP): Defined in 3GPP TS 36.423, X2AP handles signaling procedures for mobility, global operations, dual connectivity, and E-UTRAN – NR Dual Connectivity (EN-DC).

```
  if ((slot & ((1 << *scc->ssbSubcarrierSpacing) - 1)) == 0) {
    void nr_rlc_tick(int frame, int subframe);
    void nr_pdcp_tick(int frame, int subframe);
    nr_rlc_tick(frame, slot >> *scc->ssbSubcarrierSpacing);
    nr_pdcp_tick(frame, slot >> *scc->ssbSubcarrierSpacing);
    if (is_x2ap_enabled())
      x2ap_trigger();
  }
```

Clearing VRB which prepares the code for the new scheduling decision. Calculations of num_slots, size, and prev_slot to identify and manage the correct slots and resource blocks for scheduling.
```
  for (int CC_id = 0; CC_id < MAX_NUM_CCs; CC_id++) {
    //mbsfn_status[CC_id] = 0;

    // clear vrb_maps
    memset(cc[CC_id].vrb_map, 0, sizeof(uint16_t) * MAX_BWP_SIZE);
    // clear last scheduled slot's content (only)!
    const int num_slots = nr_slots_per_frame[*scc->ssbSubcarrierSpacing];
    const int size = gNB->vrb_map_UL_size;
    const int prev_slot = frame * num_slots + slot + size - 1;
    uint16_t *vrb_map_UL = cc[CC_id].vrb_map_UL;
    memcpy(&vrb_map_UL[prev_slot % size * MAX_BWP_SIZE], &gNB->ulprbbl, sizeof(uint16_t) * MAX_BWP_SIZE);

    clear_nr_nfapi_information(gNB, CC_id, frame, slot, &sched_info->DL_req, &sched_info->TX_req, &sched_info->UL_dci_req);
  }
```
**Frame** --> a (fixed) period in which the enetire network is synchronized. **Slot** --> smaller divisions
within each frame for scheduling tasks like sending ticks to different protocol. Gathers MAC layer statistics and stores them in buffer
```
  if ((slot == 0) && (frame & 127) == 0) {
    char stats_output[32656] = {0};
    dump_mac_stats(gNB, stats_output, sizeof(stats_output), true);
    LOG_I(NR_MAC, "Frame.Slot %d.%d\n%s\n", frame, slot, stats_output);
  }

  nr_mac_update_timers(module_idP, frame, slot);

  // This schedules transmission of the Master Infomration Block
  schedule_nr_mib(module_idP, frame, slot, &sched_info->DL_req);
```

> [!NOTE]

<img width="1059" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/f02e6999-1637-4319-aea2-b99d466f6096">


```
  // This schedules SIB1
  if (get_softmodem_params()->sa == 1)
    schedule_nr_sib1(module_idP, frame, slot, &sched_info->DL_req, &sched_info->TX_req);
```

Ensures that PRACH is scheduled in advance, avoiding conflicts with other uplink transmissions
```
  // This schedule PRACH if we are not in phy_test mode
  if (get_softmodem_params()->phy_test == 0) {
    /* we need to make sure that resources for PRACH are free. To avoid that
       e.g. PUSCH has already been scheduled, make sure we schedule before
       anything else: below, we simply assume an advance one frame (minus one
       slot, because otherwise we would allocate the current slot in
       UL_tti_req_ahead), but be aware that, e.g., K2 is allowed to be larger
       (schedule_nr_prach will assert if resources are not free). */
    const sub_frame_t n_slots_ahead = nr_slots_per_frame[*scc->ssbSubcarrierSpacing] - 1;
    const frame_t f = (frame + (slot + n_slots_ahead) / nr_slots_per_frame[*scc->ssbSubcarrierSpacing]) % 1024;
    const sub_frame_t s = (slot + n_slots_ahead) % nr_slots_per_frame[*scc->ssbSubcarrierSpacing];
    schedule_nr_prach(module_idP, f, s);
  }
```

CSI-RS (Channel State Information Reference Signal) --> **transmitted by the gNB** and are used by **UEs to measure the quality of the downlink channel**.
The scheduling is only done if the system is not in phy_test mode. In physical test mode, the system assumes that the UEs are already connected, so the RA procedure is not needed.
```
  // Schedule CSI-RS transmission
  nr_csirs_scheduling(module_idP, frame, slot, nr_slots_per_frame[*scc->ssbSubcarrierSpacing], &sched_info->DL_req);

  // Schedule CSI measurement reporting
  nr_csi_meas_reporting(module_idP, frame, slot);

  nr_schedule_srs(module_idP, frame, slot);

  // This schedule RA procedure if not in phy_test mode
  // Otherwise consider 5G already connected
  if (get_softmodem_params()->phy_test == 0) {
    nr_schedule_RA(module_idP, frame, slot, &sched_info->UL_dci_req, &sched_info->DL_req, &sched_info->TX_req);
  }
```

This schedules the DCI for Uplink and subsequently PUSCH
```
  nr_schedule_ulsch(module_idP, frame, slot, &sched_info->UL_dci_req);
```

This schedules the DCI for Downlink and PDSCH
```
  start_meas(&gNB->schedule_dlsch);
  nr_schedule_ue_spec(module_idP, frame, slot, &sched_info->DL_req, &sched_info->TX_req);
  stop_meas(&gNB->schedule_dlsch);
```

Schedules the transmission of Sounding Reference Signals reporting and Physical Uplink Control Channel (PUCCH).
The code then copies the Uplink Time Triggered Information (TTI) request.
```
  nr_sr_reporting(gNB, frame, slot);

  nr_schedule_pucch(gNB, frame, slot);
```
The code will trigger a fatal error and terminate the program if it detects more that 1 CC (Component carrier).
It will then handle Uplink TTI request
```
  /* TODO: we copy from gNB->UL_tti_req_ahead[0][current_index], ie. CC_id == 0,
   * is more than 1 CC supported?
   */
  AssertFatal(MAX_NUM_CCs == 1, "only 1 CC supported\n");
  const int current_index = ul_buffer_index(frame, slot, *scc->ssbSubcarrierSpacing, gNB->UL_tti_req_ahead_size);
  copy_ul_tti_req(&sched_info->UL_tti_req, &gNB->UL_tti_req_ahead[0][current_index]);
```
Stop measuring the time for the entire scheduler operation and unlocking scheduler lock which allows other threads to access scheduling resources.
Finally, the code will signals the end of the function execution.
```
  stop_meas(&gNB->eNB_scheduler);
  NR_SCHED_UNLOCK(&gNB->sched_lock);
  VCD_SIGNAL_DUMPER_DUMP_FUNCTION_BY_NAME(VCD_SIGNAL_DUMPER_FUNCTIONS_gNB_DLSCH_ULSCH_SCHEDULER,VCD_FUNCTION_OUT);
}
```
https://www.sharetechnote.com/html/5G/Handbook_5G_Index.html
https://docs.google.com/presentation/d/1GwJLWYkFAaNmiFuxFQe58pGHpcPmpc3S/edit#slide=id.g264b4a6848b_0_6
