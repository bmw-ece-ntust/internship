# Editing Incoming Packets in DPDK

## l2fwd main loop

#### Before:

```c
for (j = 0; j < nb_rx; j++) {
    m = pkts_burst[j];
    rte_prefetch0(rte_pktmbuf_mtod(m, void *));
    l2fwd_simple_forward(m, portid);
}
```

#### After:

```c
for (j = 0; j < nb_rx; j++) {
    m = pkts_burst[j];
    rte_prefetch0(rte_pktmbuf_mtod(m, void *));

    // Access packet data
    struct rte_ether_hdr *eth_hdr = rte_pktmbuf_mtod(m, struct rte_ether_hdr *);
    // Update MAC addresses
    rte_memcpy(eth_hdr->dst_addr.addr_bytes, new_dest_mac, RTE_ETHER_ADDR_LEN);
    // Forward the packet with the updated MAC address
    l2fwd_simple_forward(m, portid);
}
```

- **Accessing Packet Data:** `struct rte_ether_hdr *eth_hdr = rte_pktmbuf_mtod(m, struct rte_ether_hdr *);` accesses the Ethernet header of the packet. The `rte_pktmbuf_mtod` function converts the packet buffer into a pointer to an Ethernet header structure, allowing direct manipulation of the packet's Ethernet fields.

- **Updating MAC Address:** `rte_memcpy(eth_hdr->dst_addr.addr_bytes, new_dest_mac, RTE_ETHER_ADDR_LEN);` copies a new destination MAC address into the Ethernet header of the packet. This effectively changes the MAC address to which the packet is being sent.

- **Forwarding the Packet:** Finally, `l2fwd_simple_forward(m, portid);` forwards the packet with the updated MAC address. This function is responsible for transmitting the packet to the appropriate network interface.

---

#### Extra Features

In Addittion we can add details about the packets being received and forwarded by adding these codes:

```c
// Access packet data
void *pkt_data = rte_pktmbuf_mtod(m, void *);
uint16_t pkt_len = rte_pktmbuf_data_len(m);

// Print destination and source MAC addresses
uint8_t *eth_hdrs = (uint8_t *)pkt_data;  // Pointer to the start of the Ethernet header

printf("Packet received on port %u: length=%u\n", portid, pkt_len);

// Print destination MAC address
printf("  Dest MAC: ");
for (int k = 0; k < 6; k++) {
    printf("%02x", eth_hdrs[k]);
    if (k < 5) {
        printf(":");
    }
}

// Print source MAC address
printf("\n  Source MAC: ");
for (int k = 6; k < 12; k++) {
    printf("%02x", eth_hdrs[k]);
    if (k < 11) {
        printf(":");
    }
}

// Extract EtherType
uint16_t ether_type = (eth_hdrs[12] << 8) | eth_hdrs[13];

// Determine the packet type based on EtherType
const char *packet_type;
switch (ether_type) {
    case 0x0800:
        packet_type = "IPv4";
        break;
    case 0x0806:
        packet_type = "ARP";
        break;
    case 0x86DD:
        packet_type = "IPv6";
        break;
    default:
        packet_type = "Unknown";
        break;
}

// Print EtherType and packet type
printf("\n  EtherType: 0x%04x (%s)", ether_type, packet_type);

// Print packet data
printf("\n  Data: ");
for (uint16_t k = 0; k < pkt_len; k++) {
    printf("%02x ", ((uint8_t *)pkt_data)[k]);
}
printf("\n");
```

##### Access Packet Data and Length:

- `void *pkt_data = rte_pktmbuf_mtod(m, void *);` accesses the start of the packet data.
- `uint16_t pkt_len = rte_pktmbuf_data_len(m);` retrieves the length of the packet data in bytes.

##### Print Packet Information:

- `printf("Packet received on port %u: length=%u\n", portid, pkt_len);` prints the port on which the packet was received and its length.

##### Print Destination MAC Address:

- The loop `for (int k = 0; k < 6; k++)` iterates over the first 6 bytes of the Ethernet header, which corresponds to the destination MAC address.
- `printf("%02x", eth_hdrs[k]);` prints each byte of the destination MAC address in hexadecimal format, separated by colons.

##### Print Source MAC Address:

- The loop `for (int k = 6; k < 12; k++)` iterates over the next 6 bytes, which correspond to the source MAC address.
- Similarly, `printf("%02x", eth_hdrs[k]);` prints each byte of the source MAC address in hexadecimal format, separated by colons.

##### Extract and Determine EtherType:

- `uint16_t ether_type = (eth_hdrs[12] << 8) | eth_hdrs[13];` extracts the EtherType field from the Ethernet header, which indicates the protocol type encapsulated in the payload.
- The switch statement determines the packet type based on
  common EtherType values: - 0x0800 for IPv4 packets. - 0x0806 for ARP packets. - 0x86DD for IPv6 packets. - Other values are classified as "Unknown".

##### Print EtherType and Packet Type:

- `printf("\n EtherType: 0x%04x (%s)", ether_type, packet_type);` prints the EtherType and the corresponding packet type.

##### Print Packet Data:

- `printf("\n Data: ");` starts the packet data output.
- The loop `for (uint16_t k = 0; k < pkt_len; k++)` iterates over the packet data, printing each byte in hexadecimal format.
- This provides a hexadecimal dump of the entire packet content, which can be useful for debugging and analysis.

---

## Result

![changing mac address](/assets/editing_packets/changing%20mac%20address.png)
![arp newest](/assets/editing_packets/arp%20newest.png)
