# G_b_f_c
```
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
```

<img width="885" alt="image" src="https://github.com/user-attachments/assets/333e68df-f7e9-4988-95d6-3d52200ab919">
