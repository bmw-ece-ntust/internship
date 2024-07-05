# int oai_nfapi_nr_uci_indication
Send uplink control information indication
```
int oai_nfapi_nr_uci_indication(nfapi_nr_uci_indication_t *ind) {
  ind->header.phy_id = 1; // HACK TODO FIXME - need to pass this around!!!!
  ind->header.message_id = NFAPI_NR_PHY_MSG_TYPE_UCI_INDICATION;
  return nfapi_pnf_p7_nr_uci_ind(p7_config_g, ind);
}
```

# nfapi_pnf_p7_nr_uci_ind
Checking config and ind whether it is NULL or not.
config (nfapi_pnf_p7_config_t*): Configuration structure containing settings for the P7 interface of the physical layer.
ind (nfapi_nr_uci_indication_t*): UCI indication structure containing specific control information to be transmitted.
```
int nfapi_pnf_p7_nr_uci_ind(nfapi_pnf_p7_config_t* config, nfapi_nr_uci_indication_t* ind)
{
	if(config == NULL || ind == NULL)
	{
		NFAPI_TRACE(NFAPI_TRACE_ERROR, "%s: invalid input params\n", __FUNCTION__);
		return -1;
	}

	pnf_p7_t* _this = (pnf_p7_t*)(config);
	return pnf_nr_p7_pack_and_send_p7_message(_this, (nfapi_p7_message_header_t*)ind, sizeof(nfapi_nr_uci_indication_t));
}
```

# pnf_nr_p7_pack_and_send_p7_message

```
int pnf_nr_p7_pack_and_send_p7_message(pnf_p7_t* pnf_p7, nfapi_p7_message_header_t* header, uint32_t msg_len)
{
	header->m_segment_sequence = NFAPI_P7_SET_MSS(0, 0, pnf_p7->sequence_number);

	// Need to guard against different threads calling the encode function at the same time
	if(pthread_mutex_lock(&(pnf_p7->pack_mutex)) != 0)
	{
		NFAPI_TRACE(NFAPI_TRACE_INFO, "failed to lock mutex\n");
		return -1;
	}

	int len = nfapi_nr_p7_message_pack(header, pnf_p7->tx_message_buffer, sizeof(pnf_p7->tx_message_buffer), &pnf_p7->_public.codec_config);

	if (len < 0)
	{
		if(pthread_mutex_unlock(&(pnf_p7->pack_mutex)) != 0)
		{
			NFAPI_TRACE(NFAPI_TRACE_INFO, "failed to unlock mutex\n");
			return -1;
		}
		
		NFAPI_TRACE(NFAPI_TRACE_ERROR, "nfapi_p7_message_pack failed with return %d\n", len );
		return -1;
	}

	if(len > pnf_p7->_public.segment_size)
	{
		int msg_body_len = len - NFAPI_P7_HEADER_LENGTH ; 
		int seg_body_len = pnf_p7->_public.segment_size - NFAPI_P7_HEADER_LENGTH ; 
		int segment_count = (msg_body_len / (seg_body_len)) + ((msg_body_len % seg_body_len) ? 1 : 0); 

		int segment = 0;
		int offset = NFAPI_P7_HEADER_LENGTH;
		uint8_t buffer[pnf_p7->_public.segment_size];
		for(segment = 0; segment < segment_count; ++segment)
		{
			uint8_t last = 0;
			uint16_t size = pnf_p7->_public.segment_size - NFAPI_P7_HEADER_LENGTH;
			if(segment + 1 == segment_count)
			{
				last = 1;
				size = (msg_body_len) - (seg_body_len * segment);
			}

			uint16_t segment_size = size + NFAPI_P7_HEADER_LENGTH;

			// Update the header with the m and segement 
			memcpy(&buffer[0], pnf_p7->tx_message_buffer, NFAPI_P7_HEADER_LENGTH);

			// set the segment length
			buffer[4] = (segment_size & 0xFF00) >> 8;
			buffer[5] = (segment_size & 0xFF);

			// set the m & segment number
			buffer[6] = ((!last) << 7) + segment;

			memcpy(&buffer[NFAPI_P7_HEADER_LENGTH], pnf_p7->tx_message_buffer + offset, size);
			offset += size;

			if(pnf_p7->_public.checksum_enabled)
			{
				nfapi_p7_update_checksum(buffer, segment_size);
			}


			pnf_p7_send_message(pnf_p7, &buffer[0], segment_size);
		}
	}
	else
	{
		if(pnf_p7->_public.checksum_enabled)
		{
			nfapi_p7_update_checksum(pnf_p7->tx_message_buffer, len);
		}

		// simple case that the message fits in a single segment
		pnf_p7_send_message(pnf_p7, pnf_p7->tx_message_buffer, len);
	}

	pnf_p7->sequence_number++;
	
	if(pthread_mutex_unlock(&(pnf_p7->pack_mutex)) != 0)
	{
		NFAPI_TRACE(NFAPI_TRACE_INFO, "failed to unlock mutex\n");
		return -1;
	}

	return 0;
}
```
