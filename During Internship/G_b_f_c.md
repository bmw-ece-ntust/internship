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

# Case A
- DELTA_P_rampup_requested ->  ensure that the device increases its transmission power in a controlled manner :  **10**
- DELTA_P_rampup -> how much increase/decrease : **5**
- G_b_f_c -> control adjustment 
- pucch_power_without_g_pucch -> starting point : **100**
- P_CMAX & P_CMIN -> limit : **125 & 110**
- sum_delta_puch -> changes want to make : **-5**


  ```
  DELTA_P_rampup = max(min(0,DELTA_P_rampup),DELTA_P_rampup_requested)
                 = max(min(0,5),10)
                 = max(0,10)
                 = 10

  mac->G_b_f_c = 10 + (-5) = 5
  ```

  ```
  G_b_f_c = mac->G_b_f_c
  G_b_f_c = 5
  
  
  (!((pucch_power_without_g_pucch + G_b_f_c >= P_CMAX && sum_delta_pucch > 0) ||
        (pucch_power_without_g_pucch + G_b_f_c <= P_CMIN && sum_delta_pucch < 0)))
  (!((100 + 5 >= 125 && -5 > 0) || (100 + 5 <= 110 && -5 < 0)))
  (!((False && False) || (True && True)))
  (!((False) || (True)))
  (!(True))
  False
  ```
>[!NOTE]
> As it resulted in false, the if statement `G_b_f_c += sum_delta_pucch;` won't be called. Vice versa when the result of the if is 'True then G_b_f_c += sum_delta_pucch;` will be called and run

-
  ```
  mac->G_b_f_c = 5
  ```

  ```
  pucch_power = min(P_CMAX, pucch_power_without_g_pucch + G_b_f_c);
  pucch_power = min(125, 100+5);
  pucch_power = 105 --> Still below P_CMIN
  ```

# Case B
- DELTA_P_rampup_requested ->  ensure that the device increases its transmission power in a controlled manner :  **-5**
- DELTA_P_rampup -> how much increase/decrease : **-2**
- G_b_f_c -> control adjustment 
- pucch_power_without_g_pucch -> starting point : **100**
- P_CMAX & P_CMIN -> limit : **125 & 90**
- sum_delta_puch -> changes want to make : **-5**


  ```
  DELTA_P_rampup = max(min(0,DELTA_P_rampup),DELTA_P_rampup_requested)
                 = max(min(0,-2),-5)
                 = max(-2,-5)
                 = -2

  mac->G_b_f_c = -2 + (-5) = -7
  ```

  ```
  G_b_f_c = mac->G_b_f_c
  G_b_f_c = -7
  
  
  (!((pucch_power_without_g_pucch + G_b_f_c >= P_CMAX && sum_delta_pucch > 0) ||
        (pucch_power_without_g_pucch + G_b_f_c <= P_CMIN && sum_delta_pucch < 0)))
  (!((100 - 7  >= 125 && -5 > 0) || (100 - 7 <= 110 && -5 < 0)))
  (!((False && False) || (False && True)))
  (!((False) || (False)))
  (!(False))
  True
  ```
-
  ```
  G_b_f_c = G_b_f_c + sum_delta_pucch
          = -7-5 = -12
  mac->G_b_f_c = -7-5 = -12
  ```

  ```
  pucch_power = min(P_CMAX, pucch_power_without_g_pucch + G_b_f_c);
  pucch_power = min(125, 100-12);
  pucch_power = 88 --> below P_CMIN
  ```

# Case C
> Assuming to gain a value between P_CMIN and P_CMAX, a specific criteria need to be fulfilled.
> - 
> - pucch_power_without_g_pucch > P_CMIN
> - DELTA_P_rampup_requested > 0


- DELTA_P_rampup_requested ->  ensure that the device increases its transmission power in a controlled manner :  **5**
- DELTA_P_rampup -> how much increase/decrease : **2**
- G_b_f_c -> control adjustment 
- pucch_power_without_g_pucch -> starting point : **100**
- P_CMAX & P_CMIN -> limit : **125 & 90**
- sum_delta_puch -> changes want to make : **-5**


  ```
  DELTA_P_rampup = max(min(0,DELTA_P_rampup),DELTA_P_rampup_requested)
                 = max(min(0,2),5)
                 = max(2,5)
                 = 5

  mac->G_b_f_c = 5 + (-5) = 0
  ```

  ```
  G_b_f_c = mac->G_b_f_c
  G_b_f_c = 0
  
  
  (!((pucch_power_without_g_pucch + G_b_f_c >= P_CMAX && sum_delta_pucch > 0) ||
        (pucch_power_without_g_pucch + G_b_f_c <= P_CMIN && sum_delta_pucch < 0)))
  (!((100 + 0 >= 125 && -5 > 0) || (100 + 0 <= 110 && -5 < 0)))
  (!((100 >= 125 && -5 > 0) || (100 <= 110 && -5 < 0)))
  (!((False && False) || (False && True)))
  (!((False) || (False)))
  (!(False))
  True
  ```
-
  ```
  G_b_f_c = G_b_f_c + sum_delta_pucch
          = 0-5 = -5
  mac->G_b_f_c = -5
  ```

  ```
  pucch_power = min(P_CMAX, pucch_power_without_g_pucch + G_b_f_c);
  pucch_power = min(125, 100-5);
  pucch_power = 95 --> Above P_CMIN & Below P_CMAX [Fulfilled]
  ```


![image](https://github.com/user-attachments/assets/77477007-0712-4cf6-a5d1-ca9b481a204b)
![image](https://github.com/user-attachments/assets/cec15586-6bf4-4fdf-acec-f85c3a3b9b22)
![image](https://github.com/user-attachments/assets/d724e4c9-564f-4ece-9c7f-c55f9de99db2)

