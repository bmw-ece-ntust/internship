## PUSCH in OAI

>PUSCH (Physical Uplink Shared Channel) is a critical component in 4G LTE and 5G NR networks. 
It enables the transmission of user data from the User Equipment (UE) to the base station (gNodeB in 5G).
It carries essential user data such as voice, video, and internet traffic, ensuring that information generated 
by the user reaches the network for processing and routing. Additionally, PUSCH conveys control information, 
including Hybrid Automatic Repeat reQuest (HARQ) acknowledgments, Scheduling Requests (SR), and Channel State 
Information (CSI) which are vital for maintaining efficient communication and optimal network performance. 


![image](https://github.com/user-attachments/assets/3e001edb-77ee-4d0b-945a-cdac3e77d448)
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
  mac->G_b_f_c = 10 + (-5) = 5
  ```
  
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






