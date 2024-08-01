# TPC at gNB OAI

## Snippet code from _nr_rx_sdu.c
```
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
```

## Flowchart Power Control from _nr_rx_sdu.c code
<div align="center">
	<img width="270" alt="image" src="https://github.com/user-attachments/assets/57e1b66e-9872-4b84-b74c-dd4ccc310441">
</div>


<img width="888" alt="image" src="https://github.com/user-attachments/assets/6f322d9d-04b8-4c77-bf51-e8015ac9d223">
