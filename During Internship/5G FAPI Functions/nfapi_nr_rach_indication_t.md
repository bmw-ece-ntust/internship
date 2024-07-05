# oai_nfapi_rach_ind
> Handle a RACH indication received from the physical layer and to forward this indication to the next processing stage.
```
int oai_nfapi_rach_ind(nfapi_rach_indication_t *rach_ind) {
  rach_ind->header.phy_id = 1; // HACK TODO FIXME - need to pass this around!!!!
  LOG_D(PHY, "%s() sfn_sf:%d preambles:%d\n", __FUNCTION__, NFAPI_SFNSF2DEC(rach_ind->sfn_sf), rach_ind->rach_indication_body.number_of_preambles);
  return nfapi_pnf_p7_rach_ind(p7_config_g, rach_ind);
}
```

# nfapi_pnf_p7_nr_rach_ind
config points to a configuration structure that contains settings and context necessary for handling the P7 interface. Meanwhile ind points to a structure that contains details about an NR (New Radio) RACH (Random Access Channel) indication.

Process NR RACH indications received at the PNF (Physical Network Function) and forward them appropriately over the P7 interface.

```
int nfapi_pnf_p7_nr_rach_ind(nfapi_pnf_p7_config_t* config, nfapi_nr_rach_indication_t* ind)
{
	if(config == NULL || ind == NULL)
	{
		NFAPI_TRACE(NFAPI_TRACE_ERROR, "%s: invalid input params\n", __FUNCTION__);
		return -1;
	}

	pnf_p7_t* _this = (pnf_p7_t*)(config);
	return pnf_nr_p7_pack_and_send_p7_message(_this, (nfapi_p7_message_header_t*)ind, sizeof(nfapi_nr_rach_indication_t));
}
```

# pnf_nr_p7_pack_and_send_p7_message
Packing and sending the messages by setting a sequence number for each messages. The message will be packed according to the length of the message. 1) <0 will unlock the mutex, print error, and return -1, 2) > maximum will make the messages to be divided first into multiple segments, 3) fits in a single segment will be sent directly. After a successful send, the sequence number will  be incremented and mutex will be unlocked. 
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

