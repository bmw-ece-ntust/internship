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
  const int target_snrx10 = gNB_mac->pusch_target_snrx10;
  const int pusch_failure_thres = gNB_mac->pusch_failure_thres;

  NR_UE_info_t *UE = find_nr_UE(&gNB_mac->UE_info, current_rnti);
  bool UE_waiting_CFRA_msg3 = get_UE_waiting_CFRA_msg3(gNB_mac, CC_idP, frameP, slotP);

  if (UE && UE_waiting_CFRA_msg3 == false) {

    NR_UE_sched_ctrl_t *UE_scheduling_control = &UE->UE_sched_ctrl;
    const int8_t harq_pid = UE_scheduling_control->feedback_ul_harq.head;

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

    // if not missed detection (10dB threshold for now)
    if (rssi > 0) {
      int txpower_calc = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.phr_txpower_calc;
      UE->mac_stats.deltaMCS = txpower_calc;
      UE->mac_stats.NPRB = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.rbSize;
      if (ul_cqi != 0xff)
        UE_scheduling_control->tpc0 = nr_get_tpc(target_snrx10, ul_cqi, 30, txpower_calc);
      if (UE_scheduling_control->ph < 0 && UE_scheduling_control->tpc0 > 1)
        UE_scheduling_control->tpc0 = 1;

      if (timing_advance != 0xffff)
        UE_scheduling_control->ta_update = timing_advance;
      UE_scheduling_control->raw_rssi = rssi;
      UE_scheduling_control->pusch_snrx10 = ul_cqi * 5 - 640 - (txpower_calc * 10);

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

      NR_UE_ul_harq_t *cur_harq = &UE_scheduling_control->ul_harq_processes[harq_pid];
      if (cur_harq->round == 0)
       UE->mac_stats.pusch_snrx10 = UE_scheduling_control->pusch_snrx10;
      LOG_D(NR_MAC, "[UE %04x] PUSCH TPC %d and TA %d\n",UE->rnti,UE_scheduling_control->tpc0,UE_scheduling_control->ta_update);
    }
    else{
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

    if (sduP != NULL){
      LOG_D(NR_MAC, "Received PDU at MAC gNB \n");

      UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt = 0;
      const uint32_t tb_size = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.tb_size;
      UE_scheduling_control->sched_ul_bytes -= tb_size;
      if (UE_scheduling_control->sched_ul_bytes < 0)
        UE_scheduling_control->sched_ul_bytes = 0;

      nr_process_mac_pdu(gnb_mod_idP, UE, CC_idP, frameP, slotP, sduP, sdu_lenP, harq_pid);
    }
    else {
      NR_UE_ul_harq_t *cur_harq = &UE_scheduling_control->ul_harq_processes[harq_pid];
      /* reduce sched_ul_bytes when cur_harq->round == 3 */
      if (cur_harq->round == 3){
        const uint32_t tb_size = UE_scheduling_control->ul_harq_processes[harq_pid].sched_pusch.tb_size;
        UE_scheduling_control->sched_ul_bytes -= tb_size;
        if (UE_scheduling_control->sched_ul_bytes < 0)
          UE_scheduling_control->sched_ul_bytes = 0;
      }
      if (ul_cqi == 0xff || ul_cqi <= 128) {
        UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt++;
        UE->mac_stats.ulsch_DTX++;
      }

      if (!get_softmodem_params()->phy_test && UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt >= pusch_failure_thres) {
        LOG_W(NR_MAC,
              "UE %04x: Detected UL Failure on PUSCH after %d PUSCH DTX, stopping scheduling\n",
              UE->rnti,
              UE->UE_sched_ctrl.pusch_consecutive_dtx_cnt);
        nr_mac_trigger_ul_failure(&UE->UE_sched_ctrl, UE->current_UL_BWP.scs);
      }
    }
  } else if(sduP) {

    bool no_sig = true;
    for (int k = 0; k < sdu_lenP; k++) {
      if(sduP[k]!=0) {
        no_sig = false;
        break;
      }
    }

    if(no_sig) {
      LOG_W(NR_MAC, "No signal\n");
    }

    T(T_GNB_MAC_UL_PDU_WITH_DATA, T_INT(gnb_mod_idP), T_INT(CC_idP),
      T_INT(rntiP), T_INT(frameP), T_INT(slotP), T_INT(-1) /* harq_pid */,
      T_BUFFER(sduP, sdu_lenP));
    
    /* we don't know this UE (yet). Check whether there is a ongoing RA (Msg 3)
     * and check the corresponding UE's RNTI match, in which case we activate
     * it. */
    for (int i = 0; i < NR_NB_RA_PROC_MAX; ++i) {
      NR_RA_t *ra = &gNB_mac->common_channels[CC_idP].ra[i];
      if (ra->ra_state != nrRA_WAIT_Msg3)
        continue;

      if (no_sig) {
        LOG_D(NR_MAC, "Random Access %i failed at state %s (no signal)\n", i, nrra_text[ra->ra_state]);
        nr_clear_ra_proc(ra);
        continue;
      }

      // random access pusch with TC-RNTI
      if (ra->rnti != current_rnti) {
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

      UE = UE ? UE : add_new_nr_ue(gNB_mac, ra->rnti, ra->CellGroup);
      if (!UE) {
        LOG_W(NR_MAC,
              "Random Access %i discarded at state %s (TC_RNTI %04x RNTI %04x): max number of users achieved!\n",
              i,
              nrra_text[ra->ra_state],
              ra->rnti,
              current_rnti);

        nr_clear_ra_proc(ra);
        return;
      }

      UE->UE_beam_index = ra->beam_id;

      // re-initialize ta update variables after RA procedure completion
      UE->UE_sched_ctrl.ta_frame = frameP;

      LOG_I(NR_MAC,
            "[gNB %d][RAPROC] PUSCH with TC_RNTI 0x%04x received correctly, "
            "adding UE MAC Context RNTI 0x%04x\n",
            gnb_mod_idP,
            current_rnti,
            ra->rnti);

      NR_UE_sched_ctrl_t *UE_scheduling_control = &UE->UE_sched_ctrl;
      if (ul_cqi != 0xff) {
        UE_scheduling_control->tpc0 = nr_get_tpc(target_snrx10, ul_cqi, 30, UE_scheduling_control->sched_pusch.phr_txpower_calc);
        UE_scheduling_control->pusch_snrx10 = ul_cqi * 5 - 640 - UE_scheduling_control->sched_pusch.phr_txpower_calc * 10;
      }
      if (timing_advance != 0xffff)
        UE_scheduling_control->ta_update = timing_advance;
      UE_scheduling_control->raw_rssi = rssi;
      LOG_D(NR_MAC, "[UE %04x] PUSCH TPC %d and TA %d\n", UE->rnti, UE_scheduling_control->tpc0, UE_scheduling_control->ta_update);
      if (ra->cfra) {
        LOG_A(NR_MAC, "(rnti 0x%04x) CFRA procedure succeeded!\n", ra->rnti);
        nr_mac_reset_ul_failure(UE_scheduling_control);
        reset_dl_harq_list(UE_scheduling_control);
        reset_ul_harq_list(UE_scheduling_control);
        nr_clear_ra_proc(ra);
        process_addmod_bearers_cellGroupConfig(&UE->UE_sched_ctrl, ra->CellGroup->rlc_BearerToAddModList);
      } else {
        LOG_A(NR_MAC, "[RAPROC] RA-Msg3 received (sdu_lenP %d)\n", sdu_lenP);
        LOG_D(NR_MAC, "[RAPROC] Received Msg3:\n");
        for (int k = 0; k < sdu_lenP; k++) {
          LOG_D(NR_MAC, "(%i): 0x%x\n", k, sduP[k]);
        }

        // 3GPP TS 38.321 Section 5.4.3 Multiplexing and assembly
        // Logical channels shall be prioritised in accordance with the following order (highest priority listed first):
        // - MAC CE for C-RNTI, or data from UL-CCCH;
        // This way, we need to process MAC CE for C-RNTI if RA is active and it is present in the MAC PDU
        // Search for MAC CE for C-RNTI
        rnti_t crnti = lcid_crnti_lookahead(sduP, sdu_lenP);
        if (crnti != 0) { // 3GPP TS 38.321 Table 7.1-1: RNTI values, RNTI 0x0000: N/A
          // this UE is the one identified by the RNTI in sduP
          ra->rnti = crnti;
          // Remove UE context just created after Msg.3 in some milliseconds as the UE is one already known (not now, as the UE
          // context is still needed for the moment)
          nr_mac_trigger_release_timer(&UE->UE_sched_ctrl, UE->current_UL_BWP.scs);

          // Replace the current UE by the UE identified by C-RNTI
          UE = find_nr_UE(&RC.nrmac[gnb_mod_idP]->UE_info, crnti);
          if (!UE) {
            // The UE identified by C-RNTI no longer exists at the gNB
            // Let's abort the current RA, so the UE will trigger a new RA later but using RRCSetupRequest instead. A better
            // solution may be implemented
            LOG_W(NR_MAC, "No UE found with C-RNTI %04x, ignoring Msg3 to have UE come back with new RA attempt\n", ra->rnti);
            mac_remove_nr_ue(RC.nrmac[gnb_mod_idP], ra->rnti);
            nr_clear_ra_proc(ra);
            return;
          }

          // The UE identified by C-RNTI still exists at the gNB
          // Reset Msg4_ACKed to not schedule ULSCH and DLSCH before RRC Reconfiguration
          UE->Msg4_ACKed = false;
          nr_mac_reset_ul_failure(&UE->UE_sched_ctrl);
          // Reset HARQ processes
          reset_dl_harq_list(&UE->UE_sched_ctrl);
          reset_ul_harq_list(&UE->UE_sched_ctrl);

          if (UE->reconfigCellGroup) {
            // Nothing to do
            // A RRCReconfiguration message should be already pending (for example, an ongoing RRCReestablishment), and it will be
            // transmitted in Msg4
          } else {
            // Trigger RRC Reconfiguration
            LOG_I(NR_MAC, "Received UL_SCH_LCID_C_RNTI with C-RNTI 0x%04x, triggering RRC Reconfiguration\n", UE->rnti);
            nr_mac_trigger_reconfiguration(RC.nrmac[gnb_mod_idP], UE);
          }
        } else {
          // UE Contention Resolution Identity
          // Store the first 48 bits belonging to the uplink CCCH SDU within Msg3 to fill in Msg4
          // First byte corresponds to R/LCID MAC sub-header
          memcpy(ra->cont_res_id, &sduP[1], sizeof(uint8_t) * 6);
        }

        // Decode MAC PDU for the correct UE, after checking for MAC CE for C-RNTI
        // harq_pid set a non valid value because it is not used in this call
        // the function is only called to decode the contention resolution sub-header
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

      // for CFRA (NSA) do not schedule retransmission of msg3
      if (ra->cfra) {
        LOG_D(NR_MAC, "Random Access %i failed at state %s (NSA msg3 reception failed)\n", i, nrra_text[ra->ra_state]);
        nr_clear_ra_proc(ra);
        return;
      }

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

