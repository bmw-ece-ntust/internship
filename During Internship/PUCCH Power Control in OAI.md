> [!NOTE]
> - MCG : Master Cell Group
> - SCG : Secondary Cell Group

# UE Behavior of PUCCH
<p align="center">
<img width="829" alt="image" src="https://github.com/user-attachments/assets/e065fe67-859d-4747-b315-a05f0827d367">
</p>

- PCMAX,f,c (i) --> the UE configured maximum output power
- PO_PUCCH,b,f,c (qu) --> a parameter composed of the sum of a component PO_NOMINAL,PUCCH and PO_UE_PUCCH (qu). Expected UE Power value at gNB
- MPUUCH RB,b,f,c (i) --> bandwidth of the PUCCH resource assignment expressed in number of resource blocks for PUCCH transmission occasion i on a ctive UL BWP b of carrier f of primary cell c and mu is a SCS configuration. The higher the Resource Block the higher the value
  
- PLb,f,c(qd) --> a downlink pathloss estimate in dB calculated by the UE using RS resource index qd.
- Format Type --> will decide the calculation of
  - N_ref_PUCCH, 
  - N_sc_ctrl_RB,
  - DELTA_TF --> power adjustment component
  - delta_F_PUCCH_config --> correlated with MCS
<p align="center">
<img width="428" alt="image" src="https://github.com/user-attachments/assets/08b5b327-42c0-44cb-b83b-e6202274df26">
</p>
- gb,f,c(i,l) --> power control command to achieve gNB expected value

# PUCCH Power Control Code
```
// PUCCH Power control according to 38.213 section 7.2.1
int16_t get_pucch_tx_power_ue(NR_UE_MAC_INST_t *mac,
                              int scs,
                              NR_PUCCH_Config_t *pucch_Config,
                              int sum_delta_pucch,
                              uint8_t format_type,
                              uint16_t nb_of_prbs,
                              uint8_t freq_hop_flag,
                              uint8_t add_dmrs_flag,
                              uint8_t N_symb_PUCCH,
                              int subframe_number,
                              int O_uci,
                              uint16_t start_prb)
{
  NR_UE_UL_BWP_t *current_UL_BWP = mac->current_UL_BWP;
  AssertFatal(current_UL_BWP && current_UL_BWP->pucch_ConfigCommon,
              "Missing configuration: need UL_BWP and pucch_ConfigCommon to calculate PUCCH tx power\n");
  int PUCCH_POWER_DEFAULT = 0;
  // p0_nominal is optional
  int16_t P_O_NOMINAL_PUCCH = DEFAULT_P0_NOMINAL_PUCCH_0_DBM;
  if (current_UL_BWP->pucch_ConfigCommon->p0_nominal != NULL) {
    P_O_NOMINAL_PUCCH = *current_UL_BWP->pucch_ConfigCommon->p0_nominal;
  }

  struct NR_PUCCH_PowerControl *power_config = pucch_Config ? pucch_Config->pucch_PowerControl : NULL;

  if (!power_config)
    return (PUCCH_POWER_DEFAULT);

  int16_t P_O_UE_PUCCH = 0;

  if (pucch_Config->spatialRelationInfoToAddModList != NULL) {  /* FFS TODO NR */
    LOG_D(MAC,"PUCCH Spatial relation infos are not yet implemented\n");
    return (PUCCH_POWER_DEFAULT);
  }

  int G_b_f_c = 0;
  if (power_config->p0_Set != NULL) {
    P_O_UE_PUCCH = power_config->p0_Set->list.array[0]->p0_PUCCH_Value; /* get from index 0 if no spatial relation set */
  }

  int P_O_PUCCH = P_O_NOMINAL_PUCCH + P_O_UE_PUCCH;

  int16_t delta_F_PUCCH = DEFAULT_DELTA_F_PUCCH_0_DB;
  long *delta_F_PUCCH_config = NULL;
  int DELTA_TF;
  uint16_t N_ref_PUCCH;
  int N_sc_ctrl_RB = 0;

  /* computing of pucch transmission power adjustment */
  switch (format_type) {
    case 0:
      N_ref_PUCCH = 2;
      DELTA_TF = 10 * log10(N_ref_PUCCH/N_symb_PUCCH);
      delta_F_PUCCH_config = power_config->deltaF_PUCCH_f0;
      break;
    case 1:
      N_ref_PUCCH = 14;
      DELTA_TF = 10 * log10(N_ref_PUCCH/N_symb_PUCCH * O_uci);
      delta_F_PUCCH_config = power_config->deltaF_PUCCH_f1;
      break;
    case 2:
      N_sc_ctrl_RB = 10;
      DELTA_TF = get_deltatf(nb_of_prbs, N_symb_PUCCH, freq_hop_flag, add_dmrs_flag, N_sc_ctrl_RB, O_uci);
      delta_F_PUCCH_config = power_config->deltaF_PUCCH_f2;
      break;
    case 3:
      N_sc_ctrl_RB = 14;
      DELTA_TF = get_deltatf(nb_of_prbs, N_symb_PUCCH, freq_hop_flag, add_dmrs_flag, N_sc_ctrl_RB, O_uci);
      delta_F_PUCCH_config = power_config->deltaF_PUCCH_f3;
      break;
    case 4:
      N_sc_ctrl_RB = 14/(nb_pucch_format_4_in_subframes[subframe_number]);
      DELTA_TF = get_deltatf(nb_of_prbs, N_symb_PUCCH, freq_hop_flag, add_dmrs_flag, N_sc_ctrl_RB, O_uci);
      delta_F_PUCCH_config = power_config->deltaF_PUCCH_f4;
      break;
    default:
    {
      LOG_E(MAC,"PUCCH unknown pucch format %d\n", format_type);
      return (0);
    }
  }
  if (delta_F_PUCCH_config != NULL) {
    delta_F_PUCCH = *delta_F_PUCCH_config;
  }

  // 38.101-1: The allowed MPR for SRS, PUCCH formats 0, 1, 3 and 4, and PRACH shall be as specified for QPSK modulated DFT-
  // s-OFDM of equivalent RB allocation. The allowed MPR for PUCCH format 2 shall be as specified for QPSK
  // modulated CP-OFDM of equivalent RB allocation.
  int P_CMAX = nr_get_Pcmax(mac->p_Max,
                            mac->nr_band,
                            mac->frame_type,
                            mac->frequency_range,
                            2,
                            false,
                            mac->current_UL_BWP->scs,
                            mac->current_UL_BWP->BWPSize,
                            format_type == 2,
                            1,
                            start_prb);
  int P_CMIN = nr_get_Pcmin(mac->current_UL_BWP->scs, mac->nr_band,  mac->current_UL_BWP->BWPSize);
  int16_t pathloss = compute_nr_SSB_PL(mac, mac->ssb_measurements.ssb_rsrp_dBm);

  if (power_config->twoPUCCH_PC_AdjustmentStates && *power_config->twoPUCCH_PC_AdjustmentStates > 1) {
    LOG_E(MAC,"PUCCH power control adjustment states with 2 states not yet implemented\n");
    return (PUCCH_POWER_DEFAULT);
  }
  int M_pucch_component = (10 * log10((double)(pow(2,scs) * nb_of_prbs)));

  int16_t pucch_power_without_g_pucch = P_O_PUCCH + M_pucch_component + pathloss + delta_F_PUCCH + DELTA_TF;

  if (power_config->p0_Set == NULL) {
    if (mac->pucch_power_control_initialized == false) {
      // Initialize power control state
      // Assuming only sending on PCell
      NR_PRACH_RESOURCES_t* prach_resources = &mac->ra.prach_resources;
      float DELTA_P_rampup_requested = (prach_resources->RA_PREAMBLE_POWER_RAMPING_COUNTER - 1) * prach_resources->RA_PREAMBLE_POWER_RAMPING_STEP;
      float DELTA_P_rampup = P_CMAX - (P_O_PUCCH + pathloss + delta_F_PUCCH + DELTA_TF + sum_delta_pucch);
      DELTA_P_rampup = max(min(0, DELTA_P_rampup), DELTA_P_rampup_requested);
      mac->G_b_f_c = DELTA_P_rampup + sum_delta_pucch;
      mac->pucch_power_control_initialized = true;
    }
    else {
      // PUCCH closed loop power control state
      G_b_f_c = mac->G_b_f_c;
      if (!((pucch_power_without_g_pucch + G_b_f_c >= P_CMAX && sum_delta_pucch > 0) ||
        (pucch_power_without_g_pucch + G_b_f_c <= P_CMIN && sum_delta_pucch < 0))) {
        G_b_f_c += sum_delta_pucch;
      }
      mac->G_b_f_c = G_b_f_c;
    }
  }


  int pucch_power = min(P_CMAX, pucch_power_without_g_pucch + G_b_f_c);

  LOG_D(MAC, "PUCCH ( Tx power : %d dBm ) ( 10Log(...) : %d ) ( from Path Loss : %d ) ( delta_F_PUCCH : %d ) ( DELTA_TF : %d ) ( G_b_f_c : %d ) \n",
        pucch_power, M_pucch_component, pathloss, delta_F_PUCCH, DELTA_TF, G_b_f_c);

  return pucch_power;
}

```

# PUCCH Power Control Flowchart
![image](https://github.com/user-attachments/assets/27e02712-57e7-4968-8497-e09af71d3f34)


