## PUSCH in OAI

>PUSCH (Physical Uplink Shared Channel) is a critical component in 4G LTE and 5G NR networks. 
It enables the transmission of user data from the User Equipment (UE) to the base station (gNodeB in 5G).
It carries essential user data such as voice, video, and internet traffic, ensuring that information generated 
by the user reaches the network for processing and routing. Additionally, PUSCH conveys control information, 
including Hybrid Automatic Repeat reQuest (HARQ) acknowledgments, Scheduling Requests (SR), and Channel State 
Information (CSI) which are vital for maintaining efficient communication and optimal network performance. 


![TEEP 2025](https://github.com/user-attachments/assets/fec32e6d-a220-4fa8-9e27-66e003cf06a4)
![TEEP 2024-17](https://github.com/user-attachments/assets/329031b0-e677-40d1-89a9-39c6393c54a5)

# Case Example
- DELTA_P_rampup_requested ->  ensure that the device increases its transmission power in a controlled manner (based on the real situation):  **4**
- DELTA_P_rampup -> how much increase/decrease (calculated with maximum power allowed (P_CMAX) : **2**

- mac->f_b_f_c -> control adjustment **2**
- pusch_power_without_f_b_f_c -> starting point : **18**
- P_CMAX & P_CMIN -> limit : **23 & -37**
- delta_pusch -> fine tuning : **1**

`Initialization false`
  ```
  DELTA_P_rampup_requested = (prach_resources -> RA_PREAMBLE_POWER_RAMPIN_COUNTER-1)*prach_resources -> RA_PREAMBLE_POWER_RAMPING_STEP
                           = (3 - 1)*2
                           = 4

  DELTA_P_rampup = P_CMAX - (P_O_PUSCH + M_PUSCH_component + alpha*pathloss + DELTA_TF + delta_pusch
                 = 23 - (-104 + 10 + 100 + 14 + 1)
                 = 2

  mac->f_b_f_c = DELTA_P_rampup + delta_pusch
               = 2 + 1
               = 3
  ```

`Initialization true`
```
  (!((pucch_power_without_f_b_f_c + mac -> f_b_f_c >= P_CMAX && delta_pusch > 0) ||
        (pucch_power_without_f_b_f_c + mac -> f_b_f_c <= P_CMIN && delta_pusch < 0)))
  (!((18 + 2 >= 23 && 1 > 0) || (18 + 2 <= -37 && 1 < 0)))
  (!((False && True) || (False && False)))
  (!((False) || (False)))
  (!(False))
  True
  ```
>[!NOTE]
> As it resulted a true then G_b_f_c += sum_delta_pucch;` will be called and run. Vice versa when the result of the if statement is false, then `G_b_f_c += sum_delta_pucch;` won't be called.  
-
  ```
  mac->f_b_f_c = mac->f_b_f_c + delta_pusch
               = 2 + 1
               = 3
  ```

  ```
  return min(P_CMAX, pucch_power_without_f_b_f_c + mac -> f_b_f_c);
  min(23, 23);
  23 --> above P_CMIN and below P_CMAX
  ```





