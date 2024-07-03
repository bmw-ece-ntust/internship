## eNB_dlsch_ulsch_scheduler
>  managing and optimizing resource allocation and scheduling policies within an LTE eNB, ensuring efficient use of radio resources and maintaining UE connectivity.
Initialization of variables and structures used in this function
```
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
```

Calculating the time making sure the the scheduler is processing the correct time frame.
```
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
```

Clearing VRB (Virtual Resource Block --> represent resource allocations that may not directly correspond to physical RBs but are managed at a higher protocol layer.) maps for each component carrier. This code snippet handles MBSFN nad NFAPI.
```
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
```


Special handling for subframe 0 (first subframe) to avoid scheduling issues with BCH (Broadcast Channel) RBs.
```
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
```

Refresh UE list based on UEs dropped by PHY in previous subframe 
```
  for (UE_id = 0; UE_id < MAX_MOBILES_PER_ENB; UE_id++) {
    if (UE_info->active[UE_id]) {
      rnti = UE_RNTI(module_idP, UE_id);
      CC_id = UE_PCCID(module_idP, UE_id);
      UE_scheduling_control = &(UE_info->UE_sched_ctrl[UE_id]);
      RC.eNB[module_idP][CC_id]->pusch_stats_bsr[UE_id][(frameP * 10) + subframeP] = -63;

      if (UE_id == UE_info->list.head) {
        VCD_SIGNAL_DUMPER_DUMP_VARIABLE_BY_NAME(VCD_SIGNAL_DUMPER_VARIABLES_UE0_BSR, RC.eNB[module_idP][CC_id]->pusch_stats_bsr[UE_id][(frameP * 10) + subframeP]);
      }
```

CDRX stands for Continuous DRX (Discontinuous Reception) which is a feature in LTE (Long Term Evolution) and 5G networks designed to optimize power consumption in User Equipment (UE) while maintaining connectivity with the network.
<img width="269" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/8544a001-a478-470c-927c-53a338408e08">


```
      if (UE_scheduling_control->cdrx_configured == true) {
        bool harq_active_time_condition = false;
        UE_TEMPLATE *UE_template = NULL;
        unsigned long active_time_condition = 0; // variable used only for tracing purpose
```


If the CDRX is false then we use HARQ. (UL and DL) HARQ RTT timers and DRX retransmission timers 
```
        for (int harq_process_id = 0; harq_process_id < 8; harq_process_id++) {
```
DL asynchronous HARQ process. Note: here drx_retransmission_timer is restarted instead of started in the specification.
```
          if (UE_scheduling_control->drx_retransmission_timer[harq_process_id] > 0) {
            UE_scheduling_control->drx_retransmission_timer[harq_process_id]++;

            if (UE_scheduling_control->drx_retransmission_timer[harq_process_id] > UE_scheduling_control->drx_retransmission_timer_thres[harq_process_id]) {
              UE_scheduling_control->drx_retransmission_timer[harq_process_id] = 0;
            }
          }

          if (UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] > 8) {
              
              UE_scheduling_control->drx_retransmission_timer[harq_process_id] = 1; `started when HARQ RTT timer expires`
              UE_scheduling_control->harq_rtt_timer[CC_id][harq_process_id] = 0;
            }
          }
```


UL asynchronous HARQ process: only UL HARQ RTT timer is implemented (hence not implemented) 
``` 
          if (UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] > 4) {
              UE_scheduling_control->ul_harq_rtt_timer[CC_id][harq_process_id] = 0;
            }
          }
```


UL synchronous HARQ process 
```
          if (UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id] > 0) {
            UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id]++;

            if (UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id] > 5) {
              harq_active_time_condition = true;
              UE_scheduling_control->ul_synchronous_harq_timer[CC_id][harq_process_id] = 0;
              active_time_condition = 5; // for tracing purpose
            }
          }
        }
```


Knowing whether the UE is in active time based on conditions such as on-duration timer, DRX inactivity, HARQ activity, and uplink scheduling request (ul_SR). Tracks how long the UE has been in an active state
```
        //On duration timer
        if (UE_scheduling_control->on_duration_timer > 0) {
          UE_scheduling_control->on_duration_timer++;

          if (UE_scheduling_control->on_duration_timer > UE_scheduling_control->on_duration_timer_thres) {
            UE_scheduling_control->on_duration_timer = 0;
          }
        }

        //DRX inactivity timer
        if (UE_scheduling_control->drx_inactivity_timer > 0) {
          UE_scheduling_control->drx_inactivity_timer++;

          if (UE_scheduling_control->drx_inactivity_timer > (UE_scheduling_control->drx_inactivity_timer_thres + 1)) {
            //Note: the +1 on the threshold is due to information in table C-1 of 36.321
            UE_scheduling_control->drx_inactivity_timer = 0;
```
When timer expires switch into short or long DRX cycle 
```
            if (UE_scheduling_control->drx_shortCycle_timer_thres > 0) {
              UE_scheduling_control->in_short_drx_cycle = true;
              UE_scheduling_control->drx_shortCycle_timer = 0;
              UE_scheduling_control->in_long_drx_cycle = false;
            } else {
              UE_scheduling_control->in_long_drx_cycle = true;
            }
          }
        }

        //Short DRX Cycle
        if (UE_scheduling_control->in_short_drx_cycle == true) {
          UE_scheduling_control->drx_shortCycle_timer++;

          //When the Short DRX cycles are over, switch to long DRX cycle
          if (UE_scheduling_control->drx_shortCycle_timer > UE_scheduling_control->drx_shortCycle_timer_thres) {
            UE_scheduling_control->drx_shortCycle_timer = 0;
            UE_scheduling_control->in_short_drx_cycle = false;
            UE_scheduling_control->in_long_drx_cycle = true;
            UE_scheduling_control->drx_longCycle_timer = 0;
          }
        } else {
          UE_scheduling_control->drx_shortCycle_timer = 0;
        }

        //Long DRX Cycle
        if (UE_scheduling_control->in_long_drx_cycle == true) {
          UE_scheduling_control->drx_longCycle_timer++;

          if (UE_scheduling_control->drx_longCycle_timer > UE_scheduling_control->drx_longCycle_timer_thres) {
            UE_scheduling_control->drx_longCycle_timer = 1;
          }
        } else {
          UE_scheduling_control->drx_longCycle_timer = 0;
        }

        //Check for error cases
        if ((UE_scheduling_control->in_short_drx_cycle == true) && (UE_scheduling_control->in_long_drx_cycle == true)) {
          LOG_E(MAC, "Error in C-DRX: UE id %d is in both short and long DRX cycle. Should not happen. Back it to long cycle only\n", UE_id);
          UE_scheduling_control->in_short_drx_cycle = false;
        }
```

Condition to start On Duration Timer ( period during which the UE remains in an active state. ) based on the current DRX cycle 
```
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
        UE_template = &(UE_info->UE_template[CC_id][UE_id]);
```

(a)synchronous HARQ processes handling for Active Time 
```
        for (int harq_process_id = 0; harq_process_id < 8; harq_process_id++) {
          if (UE_scheduling_control->drx_retransmission_timer[harq_process_id] > 0) {
            harq_active_time_condition = true;
            active_time_condition = 2; // for tracing purpose
            break;
          }
        }

        //Active time conditions
        if (UE_scheduling_control->on_duration_timer > 0 ||
            UE_scheduling_control->drx_inactivity_timer > 1 ||
            harq_active_time_condition ||
            UE_template->ul_SR > 0) {
          UE_scheduling_control->in_active_time = true;
        } else {
          UE_scheduling_control->in_active_time = false;
        }
```

Debugging and tracing mechanism for monitoring the status and behavior of a User Equipment (UE) in a cellular network --> VCD (Value Change Dump) Begin.
```
        if (UE_id == 0) { //for a specific UE with ID 0 for a focused debugging process
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
```
Manage timing for Downlink Control Information (DCI) transmissions. 
```
        if (UE_scheduling_control->dci0_ongoing_timer > 0) {
          if (UE_scheduling_control->dci0_ongoing_timer > 7) {
            UE_scheduling_control->dci0_ongoing_timer = 0;
          } else {
            UE_scheduling_control->dci0_ongoing_timer++;
          }
        }
      } else { // else: CDRX not configured
```

HARQ RTT (Round Trip Time) timers for both downlink and uplink HARQ processes for a User Equipment (UE)
```
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
```

Handling various timers for a User Equipment (UE) in an LTE network, specifically for uplink (UL) inactivity, Channel Quality Indicator (CQI) requests, and UE reestablishment rejection.


```
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
```

Clearing reestablishment-related data structures
```
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
	int id;
```

The code is responsible for cleaning up ULSCH and DLSCH entries and removing UEs from uplink configuration request bodies. Cleaning ULSCH/DLSCH Entries will ensures that UEs that are no longer needed or are being rejected for reestablishment have their ULSCH and DLSCH entries cleaned up, freeing resources and maintaining the integrity of the data structures. Removing UEs from UL Config Request Bodies can be done by iterating through UL config request bodies and removes PDUs associated with the given RNTI, **ensuring that no stale PDUs are left in the configuration**

```
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
```

Iterates through each PDU in the uplink configuration list, checking if it matches the given RNTI. If a match is found, the PDU (Protocol Data Unit) is removed by shifting the subsequent PDUs and decrementing the total PDU count.
Each removal is logged for debugging and monitoring purposes.Finally, the rrc_mac_remove_ue function is called to perform additional cleanup steps for the UE in the MAC layer.
```
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
```
