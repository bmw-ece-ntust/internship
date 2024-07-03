## rx.sdu
>

Initialization variables
```
void
rx_sdu(const module_id_t enb_mod_idP,
       const int CC_idP,
       const frame_t frameP,
       const sub_frame_t subframeP,
       const rnti_t rntiP,
       uint8_t *sduP,
       const uint16_t sdu_lenP,
       const uint16_t timing_advance,
       const uint8_t ul_cqi)
//-----------------------------------------------------------------------------
{
  int current_rnti = 0;
  int UE_id = -1;
  int RA_id = 0;
  int old_rnti = -1;
  int old_UE_id = -1;
  int crnti_rx = 0;
  int harq_pid = 0;
  int first_rb = 0;
  unsigned char num_ce = 0;
  unsigned char num_sdu = 0;
  unsigned char *payload_ptr = NULL;
  unsigned char rx_ces[MAX_NUM_CE];
  unsigned char rx_lcids[NB_RB_MAX];
  unsigned short rx_lengths[NB_RB_MAX];
  uint8_t lcgid = 0;
  int lcgid_updated[4] = {0, 0, 0, 0};
  eNB_MAC_INST *mac = RC.mac[enb_mod_idP];
  UE_info_t *UE_info = &mac->UE_info;
  rrc_eNB_ue_context_t *ue_contextP = NULL;
  UE_sched_ctrl_t *UE_scheduling_control = NULL;
  UE_TEMPLATE *UE_template_ptr = NULL;
  /* Init */
  current_rnti = rntiP;
  UE_id = find_UE_id(enb_mod_idP, current_rnti);
  harq_pid = subframe2harqpid(&mac->common_channels[CC_idP], frameP, subframeP);
  memset(rx_ces, 0, MAX_NUM_CE * sizeof(unsigned char));
  memset(rx_lcids, 0, NB_RB_MAX * sizeof(unsigned char));
  memset(rx_lengths, 0, NB_RB_MAX * sizeof(unsigned short));
  start_meas(&mac->rx_ulsch_sdu);
  VCD_SIGNAL_DUMPER_DUMP_FUNCTION_BY_NAME(VCD_SIGNAL_DUMPER_FUNCTIONS_RX_SDU, 1);
  trace_pdu(DIRECTION_UPLINK, sduP, sdu_lenP, 0, WS_C_RNTI, current_rnti, frameP, subframeP, 0, 0);
```

If the User Equipment ID is valid (not '-1') then it will points to scheduling control information and 
UE template information. LOG_D logs debug few information. The code then checks that the round
number of the UL HARQ process is less than 8.
```
  if (UE_id != -1) {
    UE_scheduling_control = &UE_info->UE_sched_ctrl[UE_id];
    UE_template_ptr = &UE_info->UE_template[CC_idP][UE_id];
    LOG_D(MAC, "[eNB %d][PUSCH %d] CC_id %d %d.%d Received ULSCH (%s) sdu round %d from PHY (rnti %x, UE_id %d) ul_cqi %d, timing_advance %d\n",
          enb_mod_idP,
          harq_pid,
          CC_idP,
          frameP,
          subframeP,
          sduP==NULL ? "in error" : "OK",
          UE_scheduling_control->round_UL[CC_idP][harq_pid],
          current_rnti,
          UE_id,
          ul_cqi,
	  timing_advance);
    AssertFatal(UE_scheduling_control->round_UL[CC_idP][harq_pid] < 8, "round >= 8\n");
```

Processes an uplink transmission (UL) in a LTE or similar cellular network context
and adjusts scheduling flags to reflect the current state of the transmission process. 
These operations are essential for maintaining efficient and reliable communication between the UE and the network.
```
    if (sduP != NULL) {
      UE_scheduling_control->ul_inactivity_timer = 0;
      UE_scheduling_control->ul_failure_timer = 0;
      UE_scheduling_control->ul_scheduled &= (~(1 << harq_pid));
      UE_scheduling_control->pusch_rx_num[CC_idP]++;
      
      /* Update with smoothing: 3/4 of old value and 1/4 of new.
       * This is the logic that was done in the function
       * lte_est_timing_advance_pusch, maybe it's not necessary?
       * maybe it's even not correct at all?
       */
      UE_scheduling_control->ta_update_f = ((double)UE_scheduling_control->ta_update_f * 3 + (double)timing_advance) / 4;
      UE_scheduling_control->ta_update = (int)UE_scheduling_control->ta_update_f;
      int tmp_snr = (5 * ul_cqi - 640) / 10;
      UE_scheduling_control->pusch_snr[CC_idP] = tmp_snr;

      if(tmp_snr > 0 && tmp_snr < 63) {
        double snr_filter_tpc=0.7;
        int snr_thres_tpc=30;
        int diff = UE_scheduling_control->pusch_snr_avg[CC_idP] - UE_scheduling_control->pusch_snr[CC_idP];
        if(abs(diff) < snr_thres_tpc) {
          UE_scheduling_control->pusch_cqi_f[CC_idP] = ((double)UE_scheduling_control->pusch_cqi_f[CC_idP] * snr_filter_tpc + (double)ul_cqi * (1-snr_filter_tpc));
          UE_scheduling_control->pusch_cqi[CC_idP] = (int)UE_scheduling_control->pusch_cqi_f[CC_idP];
          UE_scheduling_control->pusch_snr_avg[CC_idP] = (5 * UE_scheduling_control->pusch_cqi[CC_idP] - 640) / 10;
        }
      }

      UE_scheduling_control->ul_consecutive_errors = 0;
      first_rb = UE_template_ptr->first_rb_ul[harq_pid];

      if (UE_scheduling_control->ul_out_of_sync > 0) {
        UE_scheduling_control->ul_out_of_sync = 0;
        mac_eNB_rrc_ul_in_sync(enb_mod_idP, CC_idP, frameP, subframeP, current_rnti);
      }
```
> [!IMPORTANT]
> Progress stopped because writer wanted to switch the research to 5G code not 4G

