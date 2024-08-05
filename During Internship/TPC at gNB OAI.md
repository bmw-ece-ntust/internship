# TPC at gNB OAI

### Snippet code from _nr_rx_sdu.c
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

### Flowchart Power Control from _nr_rx_sdu.c code
<div align="center">
	<img width="270" alt="image" src="https://github.com/user-attachments/assets/57e1b66e-9872-4b84-b74c-dd4ccc310441">
</div>


<img width="888" alt="image" src="https://github.com/user-attachments/assets/6f322d9d-04b8-4c77-bf51-e8015ac9d223">

### tpc command calculation
```
// all values passed to this function are in dB x10
uint8_t nr_get_tpc(int target, uint8_t cqi, int incr, int tx_power)
{
  // al values passed to this function are x10
  int snrx10 = (cqi * 5) - 640 - (tx_power * 10);
  LOG_D(NR_MAC, "tpc : target %d, cqi %d, snrx10 %d, tx_power %d\n", target, ((int)cqi * 5) - 640, snrx10, tx_power);
  if (snrx10 > target + incr) return 0; // decrease 1dB
  if (snrx10 < target - (3*incr)) return 3; // increase 3dB
  if (snrx10 < target - incr) return 2; // increase 1dB
  LOG_D(NR_MAC,"tpc : target %d, snrx10 %d\n",target,snrx10);
  return 1; // no change
}
```

## tpc command flowchart
<p align="center">
  <img src="https://github.com/user-attachments/assets/7d544b12-32c2-4046-a6c0-11dbd081faf4" alt="nr_get_tpc drawio">
</p>

```
uint8_t nr_get_tpc(int target, uint8_t cqi, int incr, int tx_power)
```
```
UE_scheduling_control->tpc0 = nr_get_tpc(target_snrx10, ul_cqi, 30, txpower_calc);
```
`target = target_snrx10`

`uint8_t cqi = ul_cqi`

`incr = 30` 

`tx_power = txpower_calc`

## If condition in tpc command
### A. Return 0
> When the signal is too high thus the power should be decreased  by 1 dB according to the table 7.1.1-1 above
```
snrx10 > target + incr
250 > 200 + 30
250 > 230
TRUE... return 0
```



### B. Return 3
> When the signal is too low thus it needed to be increased until 3dB power
```
snrx10 > target - 3*incr
100 < 200 - 3*30
100 < 110
TRUE... return 3
```


> At some cases the snrx10 is low but not too low for it to be increased with 3dB power so it will be increased with 1dB at C.Return 2
```
snrx10 < target - 3*incr
150 < 200 - 3*30
150 < 110
FALSE... continue to C.Return 2
```



### C. Return 2
> When the signal is a bit low thus it will be increased with 1dB power
```
snrx10 < target - incr
150 < 200 - 30
150 < 170
TRUE... return 2
```



### D. Return 1
> When the signal is still in the range thus no change in power needed
```
190 > 230 FALSE
190 < 110 FALSE
190 < 150 FALSE
Thus, no change needed ... return 1
```



























