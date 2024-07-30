```
enum pusch_pathloss_ref_rs_id : uint8_t {
      MIN_PUSCH_PATHLOSS_REF_RS_ID  = 0,
      MAX_PUSCH_PATHLOSS_REF_RS_ID  = 3,
      MAX_NOF_PUSCH_PATHLOSS_REF_RS = 4
    };

```

srsRAN_Project/lib/mac/mac_dl
/rar_pdu_assembler.cpp
```
void rar_pdu_encoder::encode_rar_grant_payload(const rar_ul_grant& grant)
{
  // Encode TA (12 bits).
  // high 7 bits of TA go into first octet.
  *ptr = ((grant.ta >> 5U) & 0x7fU);
  ptr++;
  *ptr = ((grant.ta & 0x1fU) << 3U);

  // Encode UL grant (27 bits) as per TS38.213 Table 8.2-1.
  // encode Frequency hopping flag (1 bit).
  *ptr |= ((grant.freq_hop_flag ? 1U : 0U) << 2U);
  // encode PUSCH frequency resource allocation (14 bits).
  *ptr |= (grant.freq_resource_assignment >> (14U - 2U) & 0x3U); // first 2 bits.
  ++ptr;
  *ptr = ((grant.freq_resource_assignment >> (14U - 2U - 8U)) & 0xffU); // middle 8 bits.
  ++ptr;
  *ptr = (grant.freq_resource_assignment & 0xfU) << 4U; // last 4 bits.
  // encode PUSCH time resource allocation (4 bits).
  *ptr |= (grant.time_resource_assignment & 0xfU);
  ++ptr;
  // encode MCS (4 bits).
  *ptr = (grant.mcs.to_uint() & 0xfU) << 4U;
  // encode TPC command for PUSCH (3 bits).
  *ptr |= (grant.tpc & 0x7U) << 1U;
  // encode CSI request (1 bit).
  *ptr |= grant.csi_req ? 1U : 0U;
  ++ptr;

  // Encode Temporary C-RNTI (2 Octets).
  *ptr = (to_value(grant.temp_crnti) >> 8U) & 0xffU;
  ++ptr;
  *ptr = to_value(grant.temp_crnti) & 0xffU;
  ++ptr;
}

```


srsRAN_Project/lib/scheduler/config
/serving_cell_config_factory.cpp
```
pusch_config srsran::config_helpers::make_default_pusch_config(const cell_config_builder_params_extended& params)
{
  pusch_config cfg{};
  // TODO: Verify whether its the correct Transmission Configuration we want to support.
  cfg.tx_cfg = pusch_config::tx_config::codebook;
  cfg.pusch_mapping_type_a_dmrs.emplace();
  cfg.pusch_mapping_type_a_dmrs.value().trans_precoder_disabled.emplace();
  cfg.pusch_mapping_type_a_dmrs.value().additional_positions = dmrs_additional_positions::pos2;

  cfg.pusch_pwr_ctrl = pusch_config::pusch_power_control{.msg3_alpha               = alpha::alpha1,
                                                         .p0_nominal_without_grant = -76,
                                                         .p0_alphasets             = {},
                                                         .pathloss_ref_rs          = {},
                                                         .sri_pusch_mapping        = {}};
  cfg.pusch_pwr_ctrl.value().p0_alphasets.push_back(pusch_config::pusch_power_control::p0_pusch_alphaset{
      .id = static_cast<p0_pusch_alphaset_id>(0), .p0 = 0, .p0_pusch_alpha = alpha::alpha1});
  cfg.pusch_pwr_ctrl.value().pathloss_ref_rs.push_back(pusch_config::pusch_power_control::pusch_pathloss_ref_rs{
      .id = static_cast<pusch_config::pusch_power_control::pusch_pathloss_ref_rs_id>(0),
      .rs = static_cast<ssb_id_t>(0)});
  cfg.pusch_pwr_ctrl.value().sri_pusch_mapping.push_back(pusch_config::pusch_power_control::sri_pusch_pwr_ctrl{
      .id                           = static_cast<pusch_config::pusch_power_control::sri_pusch_pwr_ctrl_id>(0),
      .sri_pusch_pathloss_ref_rs_id = static_cast<pusch_config::pusch_power_control::pusch_pathloss_ref_rs_id>(0),
      .sri_p0_pusch_alphaset_id     = static_cast<p0_pusch_alphaset_id>(0),
      .closed_loop_idx = pusch_config::pusch_power_control::sri_pusch_pwr_ctrl::sri_pusch_closed_loop_index::i0});
  cfg.res_alloc      = pusch_config::resource_allocation::resource_allocation_type_1;
  cfg.trans_precoder = pusch_config::transform_precoder::disabled;
  cfg.cb_subset      = pusch_config::codebook_subset::non_coherent;
  cfg.max_rank       = 1;

  cfg.uci_cfg.emplace();
  auto& uci_cfg   = cfg.uci_cfg.value();
  uci_cfg.scaling = alpha_scaling_opt::f1;
  beta_offsets b_offset{};
  b_offset.beta_offset_ack_idx_1    = 9;
  b_offset.beta_offset_ack_idx_2    = 9;
  b_offset.beta_offset_ack_idx_3    = 9;
  b_offset.beta_offset_csi_p1_idx_1 = 9;
  b_offset.beta_offset_csi_p1_idx_2 = 9;
  b_offset.beta_offset_csi_p2_idx_1 = 9;
  b_offset.beta_offset_csi_p2_idx_2 = 9;
  uci_cfg.beta_offsets_cfg          = uci_on_pusch::beta_offsets_semi_static{b_offset};

  return cfg;
}
```
