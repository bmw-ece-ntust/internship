## _nr_rx_sdu
>
The code first fetch specific branch using the gnb ID. Then it will logs the RNTI of the UE that sent the Service Data Unit (SDU). It will also retrieve target SNR, failure threshold, UE information, and checks if the UE is waiting for Contention Free Random Access (CFRA) message 3
```
static void _nr_rx_sdu(const module_id_t gnb_mod_idP,
                       const int CC_idP,
                       const frame_t frameP,
                       const sub_frame_t slotP,
                       const rnti_t rntiP,
                       uint8_t *sduP,
                       const uint16_t sdu_lenP,
                       const uint16_t timing_advance,
                       const uint8_t ul_cqi,
                       const uint16_t rssi)
{
  gNB_MAC_INST *gNB_mac = RC.nrmac[gnb_mod_idP];

  const int current_rnti = rntiP;
  LOG_D(NR_MAC, "rx_sdu for rnti %04x\n", current_rnti);
  const int target_snrx10 = gNB_mac->pusch_target_snrx10; //retrieve target 
  const int pusch_failure_thres = gNB_mac->pusch_failure_thres; //retrieve the failure threshold for the Physical Uplick Shared Channel (PUSCH) from the gNB MAC instance

  NR_UE_info_t *UE = find_nr_UE(&gNB_mac->UE_info, current_rnti); // Finds the UE information structure for the given RNTI
  bool UE_waiting_CFRA_msg3 = get_UE_waiting_CFRA_msg3(gNB_mac, CC_idP, frameP, slotP); 
```

Check whether the UE info is valid and not waiting for CFRA message 3 (helps avoid conflicts and interference). It will then retrieves scheduling control information for the UE nad gets the HARQ process ID.
```
  if (UE && UE_waiting_CFRA_msg3 == false) {

    NR_UE_sched_ctrl_t *UE_scheduling_control = &UE->UE_sched_ctrl;
    const int8_t harq_pid = UE_scheduling_control->feedback_ul_harq.head;
```

If sdup is not null it traces the uplink PDU with the data as well as various parameters such as gNB module ID, carrier component ID, RNTI, frame, slot, HARQ process ID, and the SDU data buffer and length. It will then update the total number of bytes received in the uplink for the UE by adding the length of the received SDU. The code the logs few information.
```
    if (sduP)
      T(T_GNB_MAC_UL_PDU_WITH_DATA, T_INT(gnb_mod_idP), T_INT(CC_idP),
        T_INT(rntiP), T_INT(frameP), T_INT(slotP), T_INT(harq_pid),
        T_BUFFER(sduP, sdu_lenP));

    UE->mac_stats.ul.total_bytes += sdu_lenP;
    LOG_D(NR_MAC, "[gNB %d][PUSCH %d] CC_id %d %d.%d Received ULSCH sdu from PHY (rnti %04x) ul_cqi %d TA %d sduP %p, rssi %d\n",
          gnb_mod_idP,
          harq_pid,
          CC_idP,
          frameP,
          slotP,
          current_rnti,
          ul_cqi,
          timing_advance,
          sduP,
          rssi);
```

Calculating transmission power, number of physical resource blocks, SNR, dan updates all of the equations to the UE's scheduling control.
```
    // if not missed detection (10dB threshold for now)
    if (rssi > 0) { // positive means that the signal was detected
      int txpower_calc = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.phr_txpower_calc; //Transmission power calculation from the HARQ process
      UE->mac_stats.deltaMCS = txpower_calc; // update the UE's MAC statistics
      UE->mac_stats.NPRB = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.rbSize; // Number of Physical Resource Blocks used by the UE
      if (ul_cqi != 0xff) // A valid Uplink Channel Quality Indicator
        UE_scheduling_control->tpc0 = nr_get_tpc(target_snrx10, ul_cqi, 30, txpower_calc);
      if (UE_scheduling_control->ph < 0 && UE_scheduling_control->tpc0 > 1)
        UE_scheduling_control->tpc0 = 1; // limits the TPC value to 1

      if (timing_advance != 0xffff) // A valid timing advance
        UE_scheduling_control->ta_update = timing_advance;
      UE_scheduling_control->raw_rssi = rssi;
      UE_scheduling_control->pusch_snrx10 = ul_cqi * 5 - 640 - (txpower_calc * 10); // Calculates the SNR and updates it in the scheduling control

      if (UE_scheduling_control->tpc0 > 1)
        LOG_D(NR_MAC,
              "[UE %04x] %d.%d. PUSCH TPC %d and TA %d pusch_snrx10 %d rssi %d phrx_tx_power %d PHR (1PRB) %d mcs %d, nb_rb %d\n",
              UE->rnti,
              frameP,
              slotP,
              UE_scheduling_control->tpc0,
              UE_scheduling_control->ta_update,
              UE_scheduling_control->pusch_snrx10,
              UE_scheduling_control->raw_rssi,
              txpower_calc,
              UE_scheduling_control->ph,
              UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.mcs,
              UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.rbSize);
```

Processes the received SDU by updating the HARQ process information, particularly setting the PUSCH SNR value during the first transmission round, and logging the TPC and timing advance values. If the RSSI indicates a missed detection (DTX), it logs this event and increases the UE's transmit power by setting the TPC to 1. Additionally, if MAC payload debugging is enabled, it prints the received uplink MAC payload in hexadecimal format for troubleshooting purposes. These actions ensure effective uplink communication management, power control adjustments, and provide tools for debugging data reception.
```
      NR_UE_ul_harq_t *cur_harq = &UE_scheduling_control->ul_harq_processes[harq_pid]; //Retrieves the current HARQ process for the UE
      if (cur_harq->round == 0) // ==0 -> is in its first round, it updates the UE's MAC statistics with the SNR value for the PUSCH.
       UE->mac_stats.pusch_snrx10 = UE_scheduling_control->pusch_snrx10;
      LOG_D(NR_MAC, "[UE %04x] PUSCH TPC %d and TA %d\n",UE->rnti,UE_scheduling_control->tpc0,UE_scheduling_control->ta_update);
    }
    else{ // if rssi is negative, it indicates a missed detection or DTX, it logs this event and sets the TPC value to 1 to instruct the UE to increase its transmit power in an attempt to improve signal detection.
      LOG_D(NR_MAC,"[UE %04x] Detected DTX : increasing UE TX power\n",UE->rnti);
      UE_scheduling_control->tpc0 = 1;
    }

#if defined(ENABLE_MAC_PAYLOAD_DEBUG)

    LOG_I(NR_MAC, "Printing received UL MAC payload at gNB side: %d \n");
    for (int i = 0; i < sdu_lenP ; i++) {
      //harq_process_ul_ue->a[i] = (unsigned char) rand();
      //printf("a[%d]=0x%02x\n",i,harq_process_ul_ue->a[i]);
      printf("%02x ",(unsigned char)sduP[i]);
    }
    printf("\n");

#endif
```

```
    if (sduP != NULL){ //not NULL --> valid data
      LOG_D(NR_MAC, "Received PDU at MAC gNB \n");

      UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt = 0; //This reset indicates a successful transmission attempt and prepares the counter for monitoring subsequent transmission events.
      const uint32_t tb_size = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.tb_size;

      UE_scheduling_control->sched_ul_bytes -= tb_size; // Updating scheduled Uplink Byter that are yet to be transmitted from the UE to the gNB
      if (UE_scheduling_control->sched_ul_bytes < 0)
        UE_scheduling_control->sched_ul_bytes = 0; // No negative value

      nr_process_mac_pdu(gnb_mod_idP, UE, CC_idP, frameP, slotP, sduP, sdu_lenP, harq_pid);
    }
```

For the SDUP == NULL (No Data received) there will be initialization and a reduce in schedlued uplink bytes as '3' is the maximum allowed attempt for HARQ round. Update the value for a specific conditions. The code will also give out fail message if specific conditions are met.
```
    else {
      NR_UE_ul_harq_t *cur_harq = &UE_scheduling_control->ul_harq_processes[harq_pid]; // initialization to point to the HARQ process structure

      /* reduce sched_ul_bytes when cur_harq->round == 3 */
      if (cur_harq->round == 3){
        const uint32_t tb_size = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.tb_size; // fetches transport block size scheduled for transmission
        UE_scheduling_control->sched_ul_bytes -= tb_size;
        if (UE_scheduling_control->sched_ul_bytes < 0) 
          UE_scheduling_control->sched_ul_bytes = 0; // no negative value
      }
      if (ul_cqi == 0xff */invalid value/*|| ul_cqi <= 128) {
        UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt++;
        UE->mac_stats.ulsch_DTX++; // update value
      }

      if (!get_softmodem_params()->phy_test && UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt >= pusch_failure_thres) { // not in test mode && DTX>=threshold value beyond which consecutive DTX events are considered excessive
        LOG_W(NR_MAC,
              "UE %04x: Detected UL Failure on PUSCH after %d PUSCH DTX, stopping scheduling\n",
              UE->rnti,
              UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt);
        nr_mac_trigger_ul_failure(&UE->UE_sched_ctrl, UE->current_UL_BWP.scs);
      }
    }
```

inspect the received SDU (sduP) to determine if it contains any meaningful (non-zero) data. 
```
  } else if(sduP) { //sduP not NULL

    bool no_sig = true;
    for (int k = 0; k < sdu_lenP; k++) {
      if(sduP[k]!=0) {
        no_sig = false;
        break;
      }
    }
```

Detecting the availability of signal and tracing few data information
```
    if(no_sig) { //Detects no signal
      LOG_W(NR_MAC, "No signal\n");
    }

    T(T_GNB_MAC_UL_PDU_WITH_DATA, T_INT(gnb_mod_idP), T_INT(CC_idP),
      T_INT(rntiP), T_INT(frameP), T_INT(slotP), T_INT(-1) /* harq_pid */,
      T_BUFFER(sduP, sdu_lenP)); //logging or tracing data
```

we don't know this UE (yet). Check whether there is a ongoing RA (Msg 3) and check the corresponding UE's RNTI match, in which case we activate it. 
```
    for (int i = 0; i < NR_NB_RA_PROC_MAX; ++i) {
      NR_RA_t *ra = &gNB_mac->common_channels[CC_idP].ra[i];
      if (ra->ra_state != nrRA_WAIT_Msg3)
        continue;

      if (no_sig) {
        LOG_D(NR_MAC, "Random Access %i failed at state %s (no signal)\n", i, nrra_text[ra->ra_state]);
        nr_clear_ra_proc(ra);
        continue;
      }
```
Matching the RNTI and the frame & slot condition to indicate the success of Random Access process
```
      // random access pusch with TC-RNTI
      if (ra->rnti != current_rnti) { //matching process
        LOG_D(NR_MAC, "expected TC_RNTI %04x to match current RNTI %04x\n", ra->rnti, current_rnti);

        if ((frameP == ra->Msg3_frame) && (slotP == ra->Msg3_slot)) { 
          LOG_W(NR_MAC,
                "Random Access %i failed at state %s (TC_RNTI %04x RNTI %04x)\n",
                i,
                nrra_text[ra->ra_state],
                ra->rnti,
                current_rnti);
          nr_clear_ra_proc(ra);
        }

        continue;
      }
```

Checking UE availibility whether a new UE can be connected, if it fails it means max number of users are already achieved and the code will cleans up any state related to the RA procedure for that specific UE attempt.
```
      UE = UE ? UE : add_new_nr_ue(gNB_mac, ra->rnti, ra->CellGroup);
      if (!UE) { //UE couldn't create a new UE due to some limitation
        LOG_W(NR_MAC,
              "Random Access %i discarded at state %s (TC_RNTI %04x RNTI %04x): max number of users achieved!\n",
              i,
              nrra_text[ra->ra_state],
              ra->rnti,
              current_rnti);

        nr_clear_ra_proc(ra);
        return;
      }
```

This index identifies the beam or antenna pattern that the UE should use for uplink communication. The logging statement provides a record of the successful RA procedure completion, indicating the establishment of the UE's MAC context with the assigned RNTI.
```
      UE->UE_beam_index = ra->beam_id;

      // re-initialize ta update variables after RA procedure completion
      UE->UE_sched_ctrl.ta_frame = frameP;

      LOG_I(NR_MAC,
            "[gNB %d][RAPROC] PUSCH with TC_RNTI 0x%04x received correctly, "
            "adding UE MAC Context RNTI 0x%04x\n",
            gnb_mod_idP,
            current_rnti,
            ra->rnti);
```

Accessing UE scheduling control to modify TPC and PUSCH. This code will also indicate whether a CFRA procedure is completed which then it will reset few variables.
```
      NR_UE_sched_ctrl_t *UE_scheduling_control = &UE->UE_sched_ctrl;
      if (ul_cqi != 0xff) {
        UE_scheduling_control->tpc0 = nr_get_tpc(target_snrx10, ul_cqi, 30, UE_scheduling_control->sched_pusch.phr_txpower_calc);
        UE_scheduling_control->pusch_snrx10 = ul_cqi * 5 - 640 - UE_scheduling_control->sched_pusch.phr_txpower_calc * 10;
      }
      if (timing_advance != 0xffff) //means it's valid
        UE_scheduling_control->ta_update = timing_advance;
      UE_scheduling_control->raw_rssi = rssi; // updates RSSI ( indicates the strength of the received signal, crucial for assessing link quality and adjusting transmission parameters.)
      LOG_D(NR_MAC, "[UE %04x] PUSCH TPC %d and TA %d\n", UE->rnti, UE_scheduling_control->tpc0, UE_scheduling_control->ta_update);
      if (ra->cfra) { //indicating successful completion of a CFRA procedure
        LOG_A(NR_MAC, "(rnti 0x%04x) CFRA procedure succeeded!\n", ra->rnti);
        nr_mac_reset_ul_failure(UE_scheduling_control);
        reset_dl_harq_list(UE_scheduling_control);
        reset_ul_harq_list(UE_scheduling_control);
        nr_clear_ra_proc(ra);
        process_addmod_bearers_cellGroupConfig(&UE->UE_sched_ctrl, ra->CellGroup->rlc_BearerToAddModList);
```

Eeception of Msg3 during the RA procedure, logs relevant information, prioritizes channel processing, identifies the UE using C-RNTI, and manages timers to maintain UE context appropriately. 
```
      } else {
        LOG_A(NR_MAC, "[RAPROC] RA-Msg3 received (sdu_lenP %d)\n", sdu_lenP); //Msg3 of the RA procedure has been received, along with the size of the SDU
        LOG_D(NR_MAC, "[RAPROC] Received Msg3:\n"); //visibility into the content of Msg3 received
        for (int k = 0; k < sdu_lenP; k++) {
          LOG_D(NR_MAC, "(%i): 0x%x\n", k, sduP[k]);
        }

        // 3GPP TS 38.321 Section 5.4.3 Multiplexing and assembly
        // Logical channels shall be prioritised in accordance with the following order (highest priority listed first):
        // - MAC CE for C-RNTI, or data from UL-CCCH;
        // This way, we need to process MAC CE for C-RNTI if RA is active and it is present in the MAC PDU

        // Search for MAC CE for C-RNTI (Cell-RNTI) -> used for identifying UEs in the network
        rnti_t crnti = lcid_crnti_lookahead(sduP, sdu_lenP);
        if (crnti != 0) { // 3GPP TS 38.321 Table 7.1-1: RNTI values, RNTI 0x0000: N/A
          // this UE is the one identified by the RNTI in sduP
          ra->rnti = crnti;
          // Remove UE context just created after Msg.3 in some milliseconds as the UE is one already known (not now, as the UE context is still needed for the moment)
          nr_mac_trigger_release_timer(&UE->UE_sched_ctrl, UE->current_UL_BWP.scs);
```

Replacing the current UE by the UE identified by C-RNTI
```
          UE = find_nr_UE(&RC.nrmac[gnb_mod_idP]->UE_info, crnti);//finding UE identified by the C-RNTI
          if (!UE) {
            // The UE identified by C-RNTI no longer exists at the gNB
            // Let's abort the current RA, so the UE will trigger a new RA later but using RRCSetupRequest instead. A better
            // solution may be implemented
            LOG_W(NR_MAC, "No UE found with C-RNTI %04x, ignoring Msg3 to have UE come back with new RA attempt\n", ra->rnti);
            mac_remove_nr_ue(RC.nrmac[gnb_mod_idP], ra->rnti);
            nr_clear_ra_proc(ra);
            return;
          }
```

The UE identified by C-RNTI still exists at the gNB. Reset Msg4_ACKed to not schedule ULSCH and DLSCH before RRC Reconfiguration. By setting Msg4_ACKed to false, the gNB ensures that the UE completes the RRC Reconfiguration process, which includes receiving all necessary configuration parameters, before engaging in regular data transmissions. This helps in maintaining a synchronized and correctly configured state between the UE and the network.
```
          UE->Msg4_ACKed = false;
          nr_mac_reset_ul_failure(&UE->UE_sched_ctrl); //ready for new ulink transmissions
          // Reset HARQ processes
          reset_dl_harq_list(&UE->UE_sched_ctrl);
          reset_ul_harq_list(&UE->UE_sched_ctrl);
```

Checking whether there is already a pending RRC Reconfiguration for the UE
```
          if (UE->reconfigCellGroup) {
            // Nothing to do
            // A RRCReconfiguration message should be already pending (for example, an ongoing RRC Reestablishment), and it will be transmitted in Msg4
          } else { // if there is no pending/on going RRC Reconfiguration
            // Trigger RRC Reconfiguration
            LOG_I(NR_MAC, "Received UL_SCH_LCID_C_RNTI with C-RNTI 0x%04x, triggering RRC Reconfiguration\n", UE->rnti);
            nr_mac_trigger_reconfiguration(RC.nrmac[gnb_mod_idP], UE);
          }
        } else {
          // UE Contention Resolution Identity
          // Store the first 48 bits belonging to the uplink CCCH SDU within Msg3 to **fill in Msg4**
          // First byte corresponds to R/LCID MAC sub-header
          memcpy(ra->cont_res_id, &sduP[1], sizeof(uint8_t) * 6);
        }
```

Decode MAC PDU for the correct UE. Logs and update RA process state. Iteration through all RA processes to find any that are waiting for Msg3 and match the given frame and slot. This ensures that the correct RA process is being handled in the current time context.
```
        nr_process_mac_pdu(gnb_mod_idP, UE, CC_idP, frameP, slotP, sduP, sdu_lenP, -1);

        LOG_I(NR_MAC, "Activating scheduling RA-Msg4 for TC_RNTI 0x%04x (state %s)\n", ra->rnti, nrra_text[ra->ra_state]);
        ra->ra_state = nrRA_Msg4;
        return;
      }
    }
  } else {
    for (int i = 0; i < NR_NB_RA_PROC_MAX; ++i) {
      NR_RA_t *ra = &gNB_mac->common_channels[CC_idP].ra[i];
      if (ra->ra_state != nrRA_WAIT_Msg3)
        continue;

      if( (frameP!=ra->Msg3_frame) || (slotP!=ra->Msg3_slot))
        continue;
```


```
      // for CFRA (NSA) do not schedule retransmission of msg3
      if (ra->cfra) { // if it's true it means the UE's random access attempt was under CFRA
        LOG_D(NR_MAC, "Random Access %i failed at state %s (NSA msg3 reception failed)\n", i, nrra_text[ra->ra_state]);
        nr_clear_ra_proc(ra);
        return;
      }

// detects the  msg3 harq rounds
      if (ra->msg3_round >= gNB_mac->ul_bler.harq_round_max - 1) {
        LOG_W(NR_MAC, "Random Access %i failed at state %s (Reached msg3 max harq rounds)\n", i, nrra_text[ra->ra_state]);
        nr_clear_ra_proc(ra);
        return;
      }

      LOG_D(NR_MAC, "Random Access %i Msg3 CRC did not pass)\n", i);

      ra->msg3_round++;
      ra->ra_state = nrRA_Msg3_retransmission;
    }
  }
}
```
