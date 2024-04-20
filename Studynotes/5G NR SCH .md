# 5G NR SCH Working Principles

![Image](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/_images/ODUArch.jpg)

Figure down below illustrates the MAC scheduler components present in O-DU architecture. It is assumed that the DU includes complete MAC and scheduler functions implemented in the same physical platform

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/MAC%20Scheduler%20Component.png)

NR Scheduler functional block has been further expanded into indicative smaller functional sub-blocks to capture the scheduler functionality.  

Note: An actual implementation may divide the scheduler into functional sub-blocks differently.

* DL/UL Resource Scheduler: This corresponds to functionality of time-domain and frequency domain scheduling in DL and UL, respectively. Resource scheduling is performed per scheduling period and may be performed for a single slot or multiple slots. Massive MIMO focuses on beamforming for capacity enhancement with full digital array structure for frequency<6GHz and hybrid/analog architecture for frequency >6GHz. It is also feasible to have single beam approach for low carrier frequency, however multi-beam approach is desirable for higher carrier frequency. It may include functions such as beam selection, selecting of UEs and associated bearers per scheduling period, allocation of radio resources for PDCCH, PUSCH, PDSCH and associated channels like DMRS. The beam selection is based on various beamforming method supported in the gNB system. In the case of predefined beamforming method, an index called “beamId” indicates the specific beam predefined in the O-RU to use in case of hybrid architecture. However, in case of Hierarchical architecture, the beam indices are pre-defined in the O-DU as defined by O-RAN Fronthaul M-Plane specification . The beam selection function selects beam indices “beamId” that is applied to DL or UL data. In the case of dynamic beamforming, the beamforming weights are given to be applied as defined in the O-RAN CUS Plane specification . It may also include functions/algorithm to support slice differentiation as specified by RRMpolicy for the resource type (PRB) so as to meet the specific SLA. It may also include the slice metric so as to prioritize the specific slice scheduling in a particular TTI that enables the gNB DU system to meet the slice level agreementFronthaul
* DL/UL Link Adaptation (LA): This functionality performs per UE Link Adaptation in DL and UL, respectively. Link Adaptation may be performed based on channel quality reported by UE or estimated at gNB corrected by BLER. LA would return effective MCS to be used for channel allocation to the UE
* UL Tx Power Control: Performs Closed loop UL power control for PUSCH, SRS and PUCCH. It may estimate the UL Tx power based on UE feedback (e.g.: Power Headroom Report) or measured UL channels
* DL/UL MIMO Mode Control: Determines per UE the MIMO mode, in DL and UL, respectively, to be used along with the corresponding precoding matrix. 
* TA Manager: Estimating the TA Command for UE based on feedback from L1 using PUSCH, PUCCH and SRS
  
Performance metrics (Capacity, throughput etc.) will be dependent on software implementation and underlying hardware.

## SCH.C Files

### schAllApisInit Function

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/schAllApisInit_SCH.png)
Flowchart of schAllApisInit Function

This function initializes all Scheduler APIs/functionality for each kind

### SchInstCfg Function

![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/SchInstCfg_SCH.png)
Flowchart of SchInstCfg Function

This function in called by SchProcGenCfgReq(). It handles the general configurations of the scheduler instance. Returns reason for success/failure of this function.

# Conclusion

After reading ![the entire program code](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Studynotes/SCH%20Thread%20Functions.pdf), I found that all functions in the SCH.H file are designed to respond to commands from MAC. Therefore, SCH operates without a main thread, but only by responding to commands from MAC.

---
* [O-RAN : Base Stasion O-DU and O-CU Software Architecture and APIs](https://www.o-ran.org/blog/57-new-or-updated-o-ran-specifications-released-since-march-2023)
