# void handle_nr_rach
```
void handle_nr_rach(NR_UL_IND_t *UL_info)
// PDUs check in the RACH indication
{
  if (NFAPI_MODE == NFAPI_MODE_PNF) {
    if (UL_info->rach_ind.number_of_pdus > 0) {
      LOG_D(PHY,"UL_info->UL_info->rach_ind.number_of_pdus:%d SFN/Slot:%d.%d \n", UL_info->rach_ind.number_of_pdus, UL_info->rach_ind.sfn,UL_info->rach_ind.slot);
      oai_nfapi_nr_rach_indication(&UL_info->rach_ind);
      UL_info->rach_ind.number_of_pdus = 0;
    }
    return;
  }

  // Determines if the RACH indication is within a valid time window or processed at the appropriate time. This is important for maintaining synchronization between the user equipment (UE) and the network.
  int frame_diff = UL_info->frame - UL_info->rach_ind.sfn;
  if (frame_diff < 0) {
    frame_diff += 1024;
  }
  bool in_timewindow = frame_diff == 0 || (frame_diff == 1 && UL_info->slot < 7);

// If there are PDUs in the RACH indication and it's within the valid time window then
it will log and terates through each PDU in the RACH indication to do preamble
(enabling UEs to initiate communication with the base station) check and initiate Random Access procedure
  if (UL_info->rach_ind.number_of_pdus > 0 && in_timewindow) {
    LOG_D(MAC,"UL_info[Frame %d, Slot %d] Calling initiate_ra_proc RACH:SFN/SLOT:%d/%d\n",
          UL_info->frame, UL_info->slot, UL_info->rach_ind.sfn, UL_info->rach_ind.slot);
    for (int i = 0; i < UL_info->rach_ind.number_of_pdus; i++) {
      AssertFatal(UL_info->rach_ind.pdu_list[i].num_preamble == 1, "More than 1 preamble not supported\n");
      nr_initiate_ra_proc(UL_info->module_id,
                          UL_info->CC_id,
                          UL_info->rach_ind.sfn,
                          UL_info->rach_ind.slot,
                          UL_info->rach_ind.pdu_list[i].preamble_list[0].preamble_index,
                          UL_info->rach_ind.pdu_list[i].freq_index,
                          UL_info->rach_ind.pdu_list[i].symbol_index,
                          UL_info->rach_ind.pdu_list[i].preamble_list[0].timing_advance);
    }
  }
}
```

# void handle_nr_uci
Process Uplink Control Information Indications then it will iterate UCI element to check pdu_type of each UCI element. The code will also
check whether message_id is equal with CRC indication which will make function NFAPI_SFNSLOT2SFN (>> 6) to be called

```
void handle_nr_uci(NR_UL_IND_t *UL_info)
{
// Processing Uplink Control Information indications in a 5G NR system. It checks if there are any UCI PDUs, logs relevant information, sends the UCI data for further processing, and resets the UCI count. 
  if(NFAPI_MODE == NFAPI_MODE_PNF) {
    if (UL_info->uci_ind.num_ucis > 0) {
      LOG_D(PHY,"PNF Sending UL_info->num_ucis:%d PDU_type: %d, SFN/SF:%d.%d \n", UL_info->uci_ind.num_ucis, UL_info->uci_ind.uci_list[0].pdu_type ,UL_info->frame, UL_info->slot);
      oai_nfapi_nr_uci_indication(&UL_info->uci_ind);
      UL_info->uci_ind.num_ucis = 0; // to avoid reprocessing the same data
    }
    return;
  }

// Variable initialization
  const module_id_t mod_id = UL_info->module_id;
  const frame_t frame = UL_info->uci_ind.sfn;
  const sub_frame_t slot = UL_info->uci_ind.slot;
  int num_ucis = UL_info->uci_ind.num_ucis;
  nfapi_nr_uci_t *uci_list = UL_info->uci_ind.uci_list;

  for (int i = 0; i < num_ucis; i++) { // Iterates through each UCI element. Checks the pdu_type of each UCI element to determine how to handle it.
    switch (uci_list[i].pdu_type) {
      case NFAPI_NR_UCI_PUSCH_PDU_TYPE:// PDU type is for PUSCH which is indicated as unhandled
        LOG_E(MAC, "%s(): unhandled NFAPI_NR_UCI_PUSCH_PDU_TYPE\n", __func__);
        break;

```
Below is the explanation of PUCCH format
<img width="1057" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/e2e978db-3ab9-4cf0-b9ae-1ef81e2aaf05">

```
      case NFAPI_NR_UCI_FORMAT_0_1_PDU_TYPE: {
        const nfapi_nr_uci_pucch_pdu_format_0_1_t *uci_pdu = &uci_list[i].pucch_pdu_format_0_1;
        LOG_D(NR_MAC, "The received uci has sfn slot %d %d, num_ucis %d and pdu_size %d\n",
                UL_info->uci_ind.sfn, UL_info->uci_ind.slot, num_ucis, uci_list[i].pdu_size);
        handle_nr_uci_pucch_0_1(mod_id, frame, slot, uci_pdu);
        break;
      }

        case NFAPI_NR_UCI_FORMAT_2_3_4_PDU_TYPE: {
          const nfapi_nr_uci_pucch_pdu_format_2_3_4_t *uci_pdu = &uci_list[i].pucch_pdu_format_2_3_4;
          handle_nr_uci_pucch_2_3_4(mod_id, frame, slot, uci_pdu);
          break;
        }
      LOG_D(MAC, "UCI handled \n");
    }
  }

  UL_info->uci_ind.num_ucis = 0;

}

static bool crc_sfn_slot_matcher(void *wanted, void *candidate)
{
  nfapi_p7_message_header_t *msg = candidate;
  int sfn_sf = *(int*)wanted;

  switch (msg->message_id)
  {
    case NFAPI_NR_PHY_MSG_TYPE_CRC_INDICATION: //message_id match
    {
      nfapi_nr_crc_indication_t *ind = candidate;
      return NFAPI_SFNSLOT2SFN(sfn_sf) == ind->sfn && NFAPI_SFNSLOT2SLOT(sfn_sf) == ind->slot;
    }

    default: //doesn't match
      LOG_E(NR_MAC, "sfn_slot_match bad ID: %d\n", msg->message_id);

  }
  return false;
}
```



# void handle_nr_ulsch
Process both of the CRC and RX Data indications. `PNF Mode`: The function processes CRC and RX indications by calling appropriate NFAPI functions and resets the counts. It then returns immediately.
`Non-PNF Mode`: The function processes CRC and RX indications by iterating through the lists, ensuring RNTI matches, and handling HARQ processes. It uses a mutex for thread safety and resets the counts after processing..Reset will avoid old data to be incorrectly processed again in the next cycle
```
void handle_nr_ulsch(NR_UL_IND_t *UL_info)
{
// checks if the NFAPI (Network Functional Application Platform Interface) mode is set to PNF (Physical Network Function) which should handle the uplink data. 
  if(NFAPI_MODE == NFAPI_MODE_PNF) {
    if (UL_info->crc_ind.number_crcs > 0) {
      LOG_D(PHY,"UL_info->UL_info->crc_ind.number_crcs:%d CRC_IND:SFN/Slot:%d.%d\n", UL_info->crc_ind.number_crcs, UL_info->crc_ind.sfn, UL_info->crc_ind.slot);
      oai_nfapi_nr_crc_indication(&UL_info->crc_ind);
      UL_info->crc_ind.number_crcs = 0;
    }

    if (UL_info->rx_ind.number_of_pdus > 0) {
      LOG_D(PHY,"UL_info->rx_ind.number_of_pdus:%d RX_IND:SFN/Slot:%d.%d \n", UL_info->rx_ind.number_of_pdus, UL_info->rx_ind.sfn, UL_info->rx_ind.slot);
      oai_nfapi_nr_rx_data_indication(&UL_info->rx_ind);
      UL_info->rx_ind.number_of_pdus = 0;
    }
    return;
  }

  if (UL_info->rx_ind.number_of_pdus > 0 && UL_info->crc_ind.number_crcs > 0) {
    // see nr_fill_indication about why this mutex is necessary
    int rc = pthread_mutex_lock(&UL_info->crc_rx_mutex);
    DevAssert(rc == 0);
// CRC is used to verify the integrity of the received data
    AssertFatal(UL_info->rx_ind.number_of_pdus == UL_info->crc_ind.number_crcs,
                "number_of_pdus %d, number_crcs %d\n",
                UL_info->rx_ind.number_of_pdus, UL_info->crc_ind.number_crcs);
// Log the RNTI for both PDU and CRC (must be a match)
// Call nr_rx_sdu to process the received PDU
// Call handle_nr_ul_harq to handle HARQ (Hybrid Automatic Repeat reQuest) processes based on the CRC results.
    for (int i = 0; i < UL_info->rx_ind.number_of_pdus; i++) {
      const nfapi_nr_rx_data_pdu_t *rx = &UL_info->rx_ind.pdu_list[i];
      const nfapi_nr_crc_t *crc = &UL_info->crc_ind.crc_list[i];
      LOG_D(NR_PHY, "UL_info->crc_ind.pdu_list[%d].rnti:%04x "
                    "UL_info->rx_ind.pdu_list[%d].rnti:%04x\n",
                    i, crc->rnti, i, rx->rnti);

      AssertFatal(crc->rnti == rx->rnti, "mis-match between CRC RNTI %04x and RX RNTI %04x\n",
                  crc->rnti, rx->rnti);

      LOG_D(NR_MAC,
            "%4d.%2d Calling rx_sdu (CRC %s/tb_crc_status %d)\n",
            UL_info->frame,
            UL_info->slot,
            crc->tb_crc_status ? "error" : "ok",
            crc->tb_crc_status);

      /* if CRC passes, pass PDU, otherwise pass NULL as error indication */
      nr_rx_sdu(UL_info->module_id,
                UL_info->CC_id,
                UL_info->rx_ind.sfn,
                UL_info->rx_ind.slot,
                crc->rnti,
                crc->tb_crc_status ? NULL : rx->pdu,
                rx->pdu_length,
                crc->timing_advance,
                crc->ul_cqi,
                crc->rssi);
      handle_nr_ul_harq(UL_info->CC_id, UL_info->module_id, UL_info->frame, UL_info->slot, crc);
    }
    UL_info->rx_ind.number_of_pdus = 0;
    UL_info->crc_ind.number_crcs = 0;
    rc = pthread_mutex_unlock(&UL_info->crc_rx_mutex);
    DevAssert(rc == 0);
  }
}
```

# void handle_nr_srs
SRS stands for Sounding Reference Signal is a kind of reference signal for Uplink (i.e, transmitted by UE) so that gNB can perform channel quality estimation for uplink.
For PNF Mode it will quickly processes the SRS indications by calling a specific function for PNF mode and resets the PDU count..For Non-PNF Mode it will iterate trhough each srs pdu and then logs the RNTI of each SRS PDU along with the frame and slot numbers
```
void handle_nr_srs(NR_UL_IND_t *UL_info) {

  if(NFAPI_MODE == NFAPI_MODE_PNF) {
    if (UL_info->srs_ind.number_of_pdus > 0) {
      LOG_D(PHY,"PNF Sending UL_info->srs_ind.number_of_pdus: %d, SFN/SF:%d.%d \n",
            UL_info->srs_ind.number_of_pdus, UL_info->frame, UL_info->slot);
      oai_nfapi_nr_srs_indication(&UL_info->srs_ind);
      UL_info->srs_ind.number_of_pdus = 0;
    }
    return;
  }

// Retrieves few variables
  const module_id_t module_id = UL_info->module_id;
  const frame_t frame = UL_info->srs_ind.sfn;
  const sub_frame_t slot = UL_info->srs_ind.slot;
  const int num_srs = UL_info->srs_ind.number_of_pdus;
  nfapi_nr_srs_indication_pdu_t *srs_list = UL_info->srs_ind.pdu_list;


  for (int i = 0; i < num_srs; i++) {
    nfapi_nr_srs_indication_pdu_t *srs_ind = &srs_list[i];
    LOG_D(NR_PHY, "(%d.%d) UL_info->srs_ind.pdu_list[%d].rnti: 0x%04x\n", frame, slot, i, srs_ind->rnti);
    handle_nr_srs_measurements(module_id,
                               frame,
                               slot,
                               srs_ind);
  }

  UL_info->srs_ind.number_of_pdus = 0;
}
```

