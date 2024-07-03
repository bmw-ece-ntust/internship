void
eNB_dlsch_ulsch_scheduler(module_id_t module_idP,
                          frame_t frameP,
                          sub_frame_t subframeP) {
  int               mbsfn_status[MAX_NUM_CCs];
  protocol_ctxt_t   ctxt;
  rnti_t            rnti  = 0;
  int               CC_id = 0;
  int               UE_id = -1;
  eNB_MAC_INST      *eNB                    = RC.mac[module_idP];
  UE_info_t         *UE_info                = &(eNB->UE_info);
  COMMON_channels_t *cc                     = eNB->common_channels;
  UE_sched_ctrl_t     *UE_scheduling_control  = NULL;
  start_meas(&(eNB->eNB_scheduler));
  VCD_SIGNAL_DUMPER_DUMP_FUNCTION_BY_NAME(VCD_SIGNAL_DUMPER_FUNCTIONS_ENB_DLSCH_ULSCH_SCHEDULER, VCD_FUNCTION_IN);
  // TODO: Better solution needed this is the first
  // 3 indications of this function on startup
  // 1303275.278188 [MAC]   XXX 0.0 -> 0.4 = 4
  // 1303275.279443 [MAC]   XXX 0.4 -> 639.5 = 6391
  // 1303275.348686 [MAC]   XXX 646.3 -> 646.3 = 0

  // calculating the time making sure the the scheduler is processing the correct time frame.
  // If the delta is too large the function log the issue and returns
  int delta = (frameP * 10 + subframeP) - (eNB->frame * 10 + eNB->subframe);
  if (delta < 0)
  {
    delta += 10240; // sfn_sf decimal values range from 0 to 10239
  }
  // If we ever see a difference this big something is very wrong
  // This threshold is arbitrary
  if (delta > 8500 || delta == 0) // 850 frames
  {
    LOG_I(MAC, "scheduler ignoring outerspace %d.%d -> %d.%d = %d\n",
          eNB->frame, eNB->subframe, frameP, subframeP, delta);
    return;
  }
  LOG_D(MAC, "Entering dlsch_ulsch scheduler %d.%d -> %d.%d = %d\n",
        eNB->frame, eNB->subframe, frameP, subframeP, delta);

  eNB->frame    = frameP;
  eNB->subframe = subframeP;


// clearing VRB maps for each component carrier
// handling MBSFN nad NFAPI
  for (CC_id = 0; CC_id < MAX_NUM_CCs; CC_id++) {
    mbsfn_status[CC_id] = 0;
    /* Clear vrb_maps */
    memset(cc[CC_id].vrb_map, 0, 100);
    memset(cc[CC_id].vrb_map_UL, 0, 100);
    cc[CC_id].mcch_active = 0;
    clear_nfapi_information(RC.mac[module_idP], CC_id, frameP, subframeP);

    /* hack: skip BCH RBs in subframe 0 for DL scheduling,
     *       because with high MCS we may exceed code rate 0.93
     *       when using those RBs (36.213 7.1.7 says the UE may
     *       skip decoding if the code rate is higher than 0.93)
     * TODO: remove this hack, deal with physical bits properly
     *       i.e. reduce MCS in the scheduler if code rate > 0.93
     */

// Special handling for subframe 0 to avoid scheduling issues with BCH (Broadcast Channel) RBs.
    if (subframeP == 0) {
      int i;
      int bw = cc[CC_id].mib->message.dl_Bandwidth;
      /* start and count defined for RBs: 6, 15, 25, 50, 75, 100 */
      int start[6] = { 0, 4, 9, 22, 34, 47 };
      int count[6] = { 6, 7, 7,  6,  7,  6 };
      for (i = 0; i < count[bw]; i++)
        cc[CC_id].vrb_map[start[bw] + i] = 1;
    }
  }

  /* Refresh UE list based on UEs dropped by PHY in previous subframe */
  for (UE_id = 0; UE_id < MAX_MOBILES_PER_ENB; UE_id++) {
    if (UE_info->active[UE_id]) {
      rnti = UE_RNTI(module_idP, UE_id);
      CC_id = UE_PCCID(module_idP, UE_id);
      UE_scheduling_control = &(UE_info->UE_sched_ctrl[UE_id]);

/* to be merged with MAC_stats.log generation. probably redundant
      if (((frameP & 127) == 0) && (subframeP == 0)) {
        double total_bler;
        if(UE_scheduling_control->pusch_rx_num[CC_id] == 0 && UE_scheduling_control->pusch_rx_error_num[CC_id] == 0) {
          total_bler = 0;
        }
        else {
          total_bler = (double)UE_scheduling_control->pusch_rx_error_num[CC_id] / (double)(UE_scheduling_control->pusch_rx_error_num[CC_id] + UE_scheduling_control->pusch_rx_num[CC_id]) * 100;
        }
        LOG_I(MAC,"UE %x : %s, PHR %d DLCQI %d PUSCH %d PUCCH %d RLC disc %d UL-stat rcv %lu err %lu bler %lf mcsoff %d bsr %u sched %u tbs %lu cnt %u , DL-stat tbs %lu cnt %u rb %u buf %u 1st %u ret %u ri %d\n",
              rnti,
              UE_scheduling_control->ul_out_of_sync == 0 ? "in synch" : "out of sync",
              UE_info->UE_template[CC_id][UE_id].phr_info,
              UE_scheduling_control->dl_cqi[CC_id],
              UE_scheduling_control->pusch_snr_avg[CC_id],
              UE_scheduling_control->pucch1_snr[CC_id],
              UE_scheduling_control->rlc_out_of_resources_cnt,
              UE_scheduling_control->pusch_rx_num[CC_id],
              UE_scheduling_control->pusch_rx_error_num[CC_id],
              total_bler,
              UE_scheduling_control->mcs_offset[CC_id],
              UE_info->UE_template[CC_id][UE_id].estimated_ul_buffer,
              UE_info->UE_template[CC_id][UE_id].scheduled_ul_bytes,
              UE_info->eNB_UE_stats[CC_id][UE_id].total_pdu_bytes_rx,
              UE_info->eNB_UE_stats[CC_id][UE_id].total_num_pdus_rx,
              UE_info->eNB_UE_stats[CC_id][UE_id].total_pdu_bytes,
              UE_info->eNB_UE_stats[CC_id][UE_id].total_num_pdus,
              UE_info->eNB_UE_stats[CC_id][UE_id].total_rbs_used,
#if defined(PRE_SCD_THREAD)
              UE_info->UE_template[CC_id][UE_id].dl_buffer_total,
#else
              0,
#endif
              UE_scheduling_control->first_cnt[CC_id],
              UE_scheduling_control->ret_cnt[CC_id],
              UE_scheduling_control->aperiodic_ri_received[CC_id]
        );
      }
*/
      RC.eNB[module_idP][CC_id]->pusch_stats_bsr[UE_id][(frameP * 10) + subframeP] = -63;

      if (UE_id == UE_info->list.head) {
        VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_UE0_BSR, RC.eNB[module_idP][CC_id]->pusch_stats_bsr[UE_id][(frameP * 10) + subframeP]);
      }

// CDRX stands for Continuous DRX (Discontinuous Reception). 
// It is a feature in LTE (Long Term Evolution) and 5G networks designed to 
// optimize power consumption in User Equipment (UE) while maintaining connectivity 
// with the network.
      /* Set and increment CDRX related timers */
      if (UE_scheduling_control->cdrx_configured == true) {
        bool harq_active_time_condition = false;
        UE_TEMPLATE *UE_template = NULL;
        unsigned long active_time_condition = 0; // variable used only for tracing purpose

// If the CDRX is false then we use HARQ
        /* (UL and DL) HARQ RTT timers and DRX retransmission timers */
        for (int harq_process_id = 0; harq_process_id < 8; harq_process_id++) {
          /* DL asynchronous HARQ process */
          if (UE_scheduling_control->drx_retransmission_timer[harq_process_id] > 0) {
            UE_scheduling_control->drx_retransmission_timer[harq_process_id]++;

            if (UE_scheduling_control->drx_retransmission_timer[harq_process_id] > UE_scheduling_control->drx_retransmission_timer_thres[harq_process_id]) {
              UE_scheduling_control->drx_retransmission_timer[harq_process_id] = 0;
            }
          }

          if (UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] > 8) {
              /* Note: here drx_retransmission_timer is restarted instead of started in the specification */
              UE_scheduling_control->drx_retransmission_timer[harq_process_id] = 1; // started when HARQ RTT timer expires
              UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] = 0;
            }
          }

          /* UL asynchronous HARQ process: only UL HARQ RTT timer is implemented (hence not implemented) */
          if (UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] > 4) {
              /*
               * TODO: implement the handling of UL asynchronous HARQ
               * drx_ULRetransmissionTimer should be (re)started here
               */
              UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] = 0;
            }
          }

          /* UL synchronous HARQ process */
          if (UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id] > 5) {
              harq_active_time_condition = true;
              UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id] = 0;
              active_time_condition = 5; // for tracing purpose
            }
          }
        }

// whether the UE is in active time based on conditions such as on-duration timer, 
// DRX inactivity, HARQ activity, and uplink scheduling request (ul_SR).
// tracks how long the UE has been in an active state
        /* On duration timer */
        if (UE_scheduling_control->on_duration_timer > 0) {
          UE_scheduling_control->on_duration_timer++;

          if (UE_scheduling_control->on_duration_timer > UE_scheduling_control->on_duration_timer_thres) {
            UE_scheduling_control->on_duration_timer = 0;
          }
        }

        /* DRX inactivity timer */
        if (UE_scheduling_control->drx_inactivity_timer > 0) {
          UE_scheduling_control->drx_inactivity_timer++;

          if (UE_scheduling_control->drx_inactivity_timer > (UE_scheduling_control->drx_inactivity_timer_thres + 1)) {
            /* Note: the +1 on the threshold is due to information in table C-1 of 36.321 */
            UE_scheduling_control->drx_inactivity_timer = 0;

            /* When timer expires switch into short or long DRX cycle */
            if (UE_scheduling_control->drx_shortCycle_timer_thres > 0) {
              UE_scheduling_control->in_short_drx_cycle = true;
              UE_scheduling_control->drx_shortCycle_timer = 0;
              UE_scheduling_control->in_long_drx_cycle = false;
            } else {
              UE_scheduling_control->in_long_drx_cycle = true;
            }
          }
        }

        /* Short DRX Cycle */
        if (UE_scheduling_control->in_short_drx_cycle == true) {
          UE_scheduling_control->drx_shortCycle_timer++;

          /* When the Short DRX cycles are over, switch to long DRX cycle */
          if (UE_scheduling_control->drx_shortCycle_timer > UE_scheduling_control->drx_shortCycle_timer_thres) {
            UE_scheduling_control->drx_shortCycle_timer = 0;
            UE_scheduling_control->in_short_drx_cycle = false;
            UE_scheduling_control->in_long_drx_cycle = true;
            UE_scheduling_control->drx_longCycle_timer = 0;
          }
        } else {
          UE_scheduling_control->drx_shortCycle_timer = 0;
        }

        /* Long DRX Cycle */
        if (UE_scheduling_control->in_long_drx_cycle == true) {
          UE_scheduling_control->drx_longCycle_timer++;

          if (UE_scheduling_control->drx_longCycle_timer > UE_scheduling_control->drx_longCycle_timer_thres) {
            UE_scheduling_control->drx_longCycle_timer = 1;
          }
        } else {
          UE_scheduling_control->drx_longCycle_timer = 0;
        }

        /* Check for error cases */
        if ((UE_scheduling_control->in_short_drx_cycle == true) && (UE_scheduling_control->in_long_drx_cycle == true)) {
          LOG_E(MAC, "Error in C-DRX: UE id %d is in both short and long DRX cycle. Should not happen. Back it to long cycle only\n", UE_id);
          UE_scheduling_control->in_short_drx_cycle = false;
        }

        /* Condition to start On Duration Timer based on the current DRX cycle */
        if (UE_scheduling_control->in_short_drx_cycle == true && UE_scheduling_control->on_duration_timer == 0) {
          if (((frameP * 10) + subframeP) % (UE_scheduling_control->short_drx_cycle_duration) ==
              (UE_scheduling_control->drx_start_offset) % (UE_scheduling_control->short_drx_cycle_duration)) {
            UE_scheduling_control->on_duration_timer = 1;
          }
        } else if (UE_scheduling_control->in_long_drx_cycle == true && UE_scheduling_control->on_duration_timer == 0) {
          if (((frameP * 10) + subframeP) % (UE_scheduling_control->drx_longCycle_timer_thres) ==
              (UE_scheduling_control->drx_start_offset)) {
            UE_scheduling_control->on_duration_timer = 1;
          }
        }

        /* Update Active Time status of UE
         * Based on 36.321 5.7 the differents conditions for the UE to be in Acttive Should be check ONLY
         * here for the current subframe. The variable 'UE_scheduling_control->in_active_time' should be updated
         * ONLY here. The variable can then be used for testing the actual state of the UE for scheduling purpose.
         */

// 
        UE_template = &(UE_info->UE_template[CC_id][UE_id]);

        /* (a)synchronous HARQ processes handling for Active Time */
        for (int harq_process_id = 0; harq_process_id < 8; harq_process_id++) {
          if (UE_scheduling_control->drx_retransmission_timer[harq_process_id] > 0) {
            harq_active_time_condition = true;
            active_time_condition = 2; // for tracing purpose
            break;
          }
        }

        /* Active time conditions */
        if (UE_scheduling_control->on_duration_timer > 0 ||
            UE_scheduling_control->drx_inactivity_timer > 1 ||
            harq_active_time_condition ||
            UE_template->ul_SR > 0) {
          UE_scheduling_control->in_active_time = true;
        } else {
          UE_scheduling_control->in_active_time = false;
        }

        /* BEGIN VCD */
        if (UE_id == 0) {
          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_ON_DURATION_TIMER, (unsigned long) UE_scheduling_control->on_duration_timer);
          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_DRX_INACTIVITY, (unsigned long) UE_scheduling_control->drx_inactivity_timer);
          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_DRX_SHORT_CYCLE, (unsigned long) UE_scheduling_control->drx_shortCycle_timer);
          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_DRX_LONG_CYCLE, (unsigned long) UE_scheduling_control->drx_longCycle_timer);
          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_DRX_RETRANSMISSION_HARQ0, (unsigned long) UE_scheduling_control->drx_retransmission_timer[0]);
          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_DRX_ACTIVE_TIME, (unsigned long) UE_scheduling_control->in_active_time);

          /* For tracing purpose */
          if (UE_template->ul_SR > 0) {
            active_time_condition = 1;
          } else if ((UE_scheduling_control->on_duration_timer > 0) && (active_time_condition == 0)) {
            active_time_condition = 3;
          } else if ((UE_scheduling_control->drx_inactivity_timer > 1) && (active_time_condition == 0)) {
            active_time_condition = 4;
          }

          VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_DRX_ACTIVE_TIME_CONDITION, (unsigned long) active_time_condition);
        }

        /* END VCD */

        /* DCI0 ongoing timer */
        if (UE_scheduling_control->dci0_ongoing_timer > 0) {
          if (UE_scheduling_control->dci0_ongoing_timer > 7) {
            UE_scheduling_control->dci0_ongoing_timer = 0;
          } else {
            UE_scheduling_control->dci0_ongoing_timer++;
          }
        }
      } else { // else: CDRX not configured
        /* Note: (UL) HARQ RTT timers processing is done here and can be used by other features than CDRX */
        /* HARQ RTT timers */
        for (int harq_process_id = 0; harq_process_id < 8; harq_process_id++) {
          if (UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] > 8) {
              UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] = 0;
            }
          }

          if (UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] > 4) {
              UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] = 0;
            }
          }
        } // end loop harq process
      } // end else CDRX not configured

      /* Increment these timers, they are cleared when we receive an sdu */
      UE_scheduling_control->ul_inactivity_timer++;
      UE_scheduling_control->cqi_req_timer++;
      LOG_D(MAC, "UE %d/%x : ul_inactivity %d, cqi_req %d\n",
            UE_id,
            rnti,
            UE_scheduling_control->ul_inactivity_timer,
            UE_scheduling_control->cqi_req_timer);
      check_ul_failure(module_idP, CC_id, UE_id, frameP, subframeP);

      if (UE_scheduling_control->ue_reestablishment_reject_timer > 0) {
        UE_scheduling_control->ue_reestablishment_reject_timer++;

        if (UE_scheduling_control->ue_reestablishment_reject_timer >= UE_scheduling_control->ue_reestablishment_reject_timer_thres) {
          UE_scheduling_control->ue_reestablishment_reject_timer = 0;

          /* Clear reestablish_rnti_map */
          if (UE_scheduling_control->ue_reestablishment_reject_timer_thres > 20) {
            for (int ue_id_l = 0; ue_id_l < MAX_MOBILES_PER_ENB; ue_id_l++) {
              if (reestablish_rnti_map[ue_id_l][0] == rnti) {
                /* Clear currentC-RNTI from map */
                reestablish_rnti_map[ue_id_l][0] = 0;
                reestablish_rnti_map[ue_id_l][1] = 0;
                break;
              }
            }

            PROTOCOL_CTXT_SET_BY_MODULE_ID(&ctxt, module_idP, ENB_FLAG_YES, rnti, 0, 0,module_idP);
            rrc_rlc_remove_ue(&ctxt);
            pdcp_remove_UE(&ctxt);
          }

          /* Note: This should not be done in the MAC! */
	  /*
          for (int ii=0; ii<MAX_MOBILES_PER_ENB; ii++) {
            LTE_eNB_ULSCH_t *ulsch = RC.eNB[module_idP][CC_id]->ulsch[ii];

            if((ulsch != NULL) && (ulsch->rnti == rnti)) {
              void clean_eNb_ulsch(LTE_eNB_ULSCH_t *ulsch);
              LOG_I(MAC, "clean_eNb_ulsch UE %x \n", rnti);
              clean_eNb_ulsch(ulsch);
            }
          }

          for (int ii=0; ii<MAX_MOBILES_PER_ENB; ii++) {
            LTE_eNB_DLSCH_t *dlsch = RC.eNB[module_idP][CC_id]->dlsch[ii][0];

            if((dlsch != NULL) && (dlsch->rnti == rnti)) {
              void clean_eNb_dlsch(LTE_eNB_DLSCH_t *dlsch);
              LOG_I(MAC, "clean_eNb_dlsch UE %x \n", rnti);
              clean_eNb_dlsch(dlsch);
            }
          }
	  */

	int id;

	// clean ULSCH entries for rnti
	id = find_ulsch(rnti,RC.eNB[module_idP][CC_id],SEARCH_EXIST);
        if (id>=0) clean_eNb_ulsch(RC.eNB[module_idP][CC_id]->ulsch[id]);

	// clean DLSCH entries for rnti
	id = find_dlsch(rnti,RC.eNB[module_idP][CC_id],SEARCH_EXIST);
        if (id>=0) clean_eNb_dlsch(RC.eNB[module_idP][CC_id]->dlsch[id][0]);

          for (int j = 0; j < 10; j++) {
            nfapi_ul_config_request_body_t *ul_req_tmp = NULL;
            ul_req_tmp = &(eNB->UL_req_tmp[CC_id][j].ul_config_request_body);

            if (ul_req_tmp) {
              int pdu_number = ul_req_tmp->number_of_pdus;

              for (int pdu_index = pdu_number-1; pdu_index >= 0; pdu_index--) {
                if (ul_req_tmp->ul_config_pdu_list[pdu_index].ulsch_pdu.ulsch_pdu_rel8.rnti == rnti) {
                  LOG_I(MAC, "remove UE %x from ul_config_pdu_list %d/%d\n",
                        rnti,
                        pdu_index,
                        pdu_number);

                  if (pdu_index < pdu_number -1) {
                    memcpy(&ul_req_tmp->ul_config_pdu_list[pdu_index],
                           &ul_req_tmp->ul_config_pdu_list[pdu_index+1],
                           (pdu_number-1-pdu_index) * sizeof(nfapi_ul_config_request_pdu_t));
                  }

                  ul_req_tmp->number_of_pdus--;
                }
              } // end for pdu_index
            } // end if (ul_req_tmp)
          } // end for j

          rrc_mac_remove_ue(module_idP,rnti);
        } // end if (UE_scheduling_control->ue_reestablishment_reject_timer >= UE_scheduling_control->ue_reestablishment_reject_timer_thres)
      } // end if (UE_scheduling_control->ue_reestablishment_reject_timer > 0)
    } // end if UE active
  } // end for loop on UE_id
}
