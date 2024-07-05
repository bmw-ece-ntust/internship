int aerial_phy_nr_uci_indication(nfapi_nr_uci_indication_t *ind)
{
  if (NFAPI_MODE == NFAPI_MODE_AERIAL) {
    nfapi_nr_uci_indication_t *uci_ind = CALLOC(1, sizeof(*uci_ind));
    AssertFatal(uci_ind, "Memory not allocated for uci_ind in phy_nr_uci_indication.");
    *uci_ind = *ind;

    uci_ind->uci_list = CALLOC(NFAPI_NR_UCI_IND_MAX_PDU, sizeof(nfapi_nr_uci_t));
    AssertFatal(uci_ind->uci_list != NULL, "Memory not allocated for uci_ind->uci_list in phy_nr_uci_indication.");
    for (int i = 0; i < ind->num_ucis; i++) {
      uci_ind->uci_list[i] = ind->uci_list[i];

      switch (uci_ind->uci_list[i].pdu_type) {
        case NFAPI_NR_UCI_PUSCH_PDU_TYPE:
          LOG_E(MAC, "%s(): unhandled NFAPI_NR_UCI_PUSCH_PDU_TYPE\n", __func__);
          break;

        case NFAPI_NR_UCI_FORMAT_0_1_PDU_TYPE: {
//          nfapi_nr_uci_pucch_pdu_format_0_1_t *uci_ind_pdu = &uci_ind->uci_list[i].pucch_pdu_format_0_1;
//          nfapi_nr_uci_pucch_pdu_format_0_1_t *ind_pdu = &ind->uci_list[i].pucch_pdu_format_0_1;
//          if (ind_pdu->sr) {
//            uci_ind_pdu->sr = CALLOC(1, sizeof(*uci_ind_pdu->sr));
//            AssertFatal(uci_ind_pdu->sr != NULL, "Memory not allocated for uci_ind_pdu->harq in phy_nr_uci_indication.");
//            *uci_ind_pdu->sr = *ind_pdu->sr;
//          }
//          if (ind_pdu->harq) {
//            uci_ind_pdu->harq = CALLOC(1, sizeof(*uci_ind_pdu->harq));
//            AssertFatal(uci_ind_pdu->harq != NULL, "Memory not allocated for uci_ind_pdu->harq in phy_nr_uci_indication.");
//
//            *uci_ind_pdu->harq = *ind_pdu->harq;
//            uci_ind_pdu->harq->harq_list = CALLOC(uci_ind_pdu->harq->num_harq, sizeof(*uci_ind_pdu->harq->harq_list));
//            AssertFatal(uci_ind_pdu->harq->harq_list != NULL,
//                        "Memory not allocated for uci_ind_pdu->harq->harq_list in phy_nr_uci_indication.");
//            for (int j = 0; j < uci_ind_pdu->harq->num_harq; j++)
//              uci_ind_pdu->harq->harq_list[j].harq_value = ind_pdu->harq->harq_list[j].harq_value;
//          }
          break;
        }

        case NFAPI_NR_UCI_FORMAT_2_3_4_PDU_TYPE: {
          nfapi_nr_uci_pucch_pdu_format_2_3_4_t *uci_ind_pdu = &uci_ind->uci_list[i].pucch_pdu_format_2_3_4;
          nfapi_nr_uci_pucch_pdu_format_2_3_4_t *ind_pdu = &ind->uci_list[i].pucch_pdu_format_2_3_4;
          *uci_ind_pdu = *ind_pdu;
          if (ind_pdu->harq.harq_payload) {
            uci_ind_pdu->harq.harq_payload = CALLOC(1, sizeof(*uci_ind_pdu->harq.harq_payload));
            AssertFatal(uci_ind_pdu->harq.harq_payload != NULL,
                        "Memory not allocated for uci_ind_pdu->harq.harq_payload in phy_nr_uci_indication.");
            *uci_ind_pdu->harq.harq_payload = *ind_pdu->harq.harq_payload;
          }
          if (ind_pdu->sr.sr_payload) {
            uci_ind_pdu->sr.sr_payload = CALLOC(1, sizeof(*uci_ind_pdu->sr.sr_payload));
            AssertFatal(uci_ind_pdu->sr.sr_payload != NULL,
                        "Memory not allocated for uci_ind_pdu->sr.sr_payload in phy_nr_uci_indication.");
            //SCF222.10.02 sr_bit_len values from 1 to 8, payload always just one byte
            uci_ind_pdu->sr.sr_payload[0] = ind_pdu->sr.sr_payload[0];
          }
          if (ind_pdu->csi_part1.csi_part1_payload) {
            uint8_t byte_len = (ind_pdu->csi_part1.csi_part1_bit_len / 8) + 1;
            uci_ind_pdu->csi_part1.csi_part1_payload = calloc(byte_len, sizeof(uint8_t));
            AssertFatal(uci_ind_pdu->csi_part1.csi_part1_payload != NULL,
                        "Memory not allocated for uci_ind_pdu->csi_part1.csi_part1_payload in phy_nr_uci_indication.");
            memcpy(uci_ind_pdu->csi_part1.csi_part1_payload,ind_pdu->csi_part1.csi_part1_payload,byte_len);
          }
          if (ind_pdu->csi_part2.csi_part2_payload) {
            uint8_t byte_len = (ind_pdu->csi_part2.csi_part2_bit_len / 8) + 1;
            uci_ind_pdu->csi_part2.csi_part2_payload = calloc(byte_len, sizeof(uint8_t));
            AssertFatal(uci_ind_pdu->csi_part2.csi_part2_payload != NULL,
                        "Memory not allocated for uci_ind_pdu->csi_part2.csi_part2_payload in phy_nr_uci_indication.");
            memcpy(uci_ind_pdu->csi_part2.csi_part2_payload,ind_pdu->csi_part2.csi_part2_payload,byte_len);
          }
          break;
        }
      }
    }

    if (!put_queue(&gnb_uci_ind_queue, uci_ind)) {
      LOG_E(NR_MAC, "Put_queue failed for uci_ind\n");
      for (int i = 0; i < ind->num_ucis; i++) {
        if (uci_ind->uci_list[i].pdu_type == NFAPI_NR_UCI_FORMAT_0_1_PDU_TYPE) {
//          if (uci_ind->uci_list[i].pucch_pdu_format_0_1.harq) {
//            free(uci_ind->uci_list[i].pucch_pdu_format_0_1.harq->harq_list);
//            uci_ind->uci_list[i].pucch_pdu_format_0_1.harq->harq_list = NULL;
//            free(uci_ind->uci_list[i].pucch_pdu_format_0_1.harq);
//            uci_ind->uci_list[i].pucch_pdu_format_0_1.harq = NULL;
//          }
//          if (uci_ind->uci_list[i].pucch_pdu_format_0_1.sr) {
//            free(uci_ind->uci_list[i].pucch_pdu_format_0_1.sr);
//            uci_ind->uci_list[i].pucch_pdu_format_0_1.sr = NULL;
//          }
        }
        if (uci_ind->uci_list[i].pdu_type == NFAPI_NR_UCI_FORMAT_2_3_4_PDU_TYPE) {
          free(uci_ind->uci_list[i].pucch_pdu_format_2_3_4.harq.harq_payload);
          free(uci_ind->uci_list[i].pucch_pdu_format_2_3_4.csi_part1.csi_part1_payload);
          free(uci_ind->uci_list[i].pucch_pdu_format_2_3_4.csi_part2.csi_part2_payload);
        }
      }
      free(uci_ind->uci_list);
      uci_ind->uci_list = NULL;
      free(uci_ind);
      uci_ind = NULL;
    }
  } else {
    LOG_E(NR_MAC, "NFAPI_MODE = %d not NFAPI_MODE_AERIAL(3)\n", nfapi_getmode());
  }
  return 1;
}
