# DPDK l2fwd Study Notes

> **References:**
> - [Introduction to DPDK: Architecture and Principles](https://embedx.medium.com/introduction-to-dpdk-architecture-and-principles-40db9a61a6f5)
> - 
> - 

## 1. Understanding the l2fwd code example
#### 1.1. Go to the l2fwd example directory
```bash
/home/eriqoaw/dpdk-stable-23.11.1/examples/l2fwd/main.c
```
### main() function
#### 1.2. Initialization and Argument Parsing:
```c
ret = rte_eal_init(argc, argv);
if (ret < 0)
    rte_exit(EXIT_FAILURE, "Invalid EAL arguments\n");
argc -= ret;
argv += ret;
```
- Initializes the Environment Abstraction Layer (EAL).
- If initialization fails, exits the program.
- Adjusts the argument list to skip EAL-specific arguments.

#### 1.3. Signal Handling:
```c
force_quit = false;
signal(SIGINT, signal_handler);
signal(SIGTERM, signal_handler);
```
- Sets up signal handlers for SIGINT and SIGTERM to handle graceful shutdown.

#### 1.4. Application-Specific Argument Parsing:
```c
ret = l2fwd_parse_args(argc, argv);
if (ret < 0)
    rte_exit(EXIT_FAILURE, "Invalid L2FWD arguments\n");
```
- Parses arguments specific to the L2 forwarding application.

#### 1.5. Configuration and Validation:
```c
nb_ports = rte_eth_dev_count_avail();
if (nb_ports == 0)
    rte_exit(EXIT_FAILURE, "No Ethernet ports - bye\n");

if (port_pair_params != NULL) {
    if (check_port_pair_config() < 0)
        rte_exit(EXIT_FAILURE, "Invalid port pair config\n");
}

if (l2fwd_enabled_port_mask & ~((1 << nb_ports) - 1))
    rte_exit(EXIT_FAILURE, "Invalid portmask; possible (0x%x)\n",
        (1 << nb_ports) - 1);

```
- Counts the number of available Ethernet ports.
- Validates the port pair configuration if provided.
- Validates the port mask to ensure it covers valid ports.

#### 1.6. Driver Initialization and Port Configuration:
```c
for (portid = 0; portid < RTE_MAX_ETHPORTS; portid++)
    l2fwd_dst_ports[portid] = 0;

if (port_pair_params != NULL) {
    uint16_t idx, p;
    for (idx = 0; idx < (nb_port_pair_params << 1); idx++) {
        p = idx & 1;
        portid = port_pair_params[idx >> 1].port[p];
        l2fwd_dst_ports[portid] = port_pair_params[idx >> 1].port[p ^ 1];
    }
} else {
    RTE_ETH_FOREACH_DEV(portid) {
        if ((l2fwd_enabled_port_mask & (1 << portid)) == 0)
            continue;

        if (nb_ports_in_mask % 2) {
            l2fwd_dst_ports[portid] = last_port;
            l2fwd_dst_ports[last_port] = portid;
        } else {
            last_port = portid;
        }
        nb_ports_in_mask++;
    }
    if (nb_ports_in_mask % 2) {
        printf("Notice: odd number of ports in portmask.\n");
        l2fwd_dst_ports[last_port] = last_port;
    }
}
```
- Initializes l2fwd_dst_ports array.
- If port pair parameters are provided, sets up port pairs for forwarding.
- Otherwise, sets up a simple round-robin pairing of ports.

#### 1.7. Core and Queue Configuration:
```c
rx_lcore_id = 0;
qconf = NULL;

RTE_ETH_FOREACH_DEV(portid) {
    if ((l2fwd_enabled_port_mask & (1 << portid)) == 0)
        continue;

    while (rte_lcore_is_enabled(rx_lcore_id) == 0 ||
           lcore_queue_conf[rx_lcore_id].n_rx_port == l2fwd_rx_queue_per_lcore) {
        rx_lcore_id++;
        if (rx_lcore_id >= RTE_MAX_LCORE)
            rte_exit(EXIT_FAILURE, "Not enough cores\n");
    }

    if (qconf != &lcore_queue_conf[rx_lcore_id]) {
        qconf = &lcore_queue_conf[rx_lcore_id];
        nb_lcores++;
    }

    qconf->rx_port_list[qconf->n_rx_port] = portid;
    qconf->n_rx_port++;
    printf("Lcore %u: RX port %u TX port %u\n", rx_lcore_id,
           portid, l2fwd_dst_ports[portid]);
}
```
- Allocates logical cores to handle RX queues of enabled ports.
- Prints the mapping of logical cores to ports.

#### 1.8. Memory Pool Creation:
```c
nb_mbufs = RTE_MAX(nb_ports * (nb_rxd + nb_txd + MAX_PKT_BURST +
    nb_lcores * MEMPOOL_CACHE_SIZE), 8192U);

l2fwd_pktmbuf_pool = rte_pktmbuf_pool_create("mbuf_pool", nb_mbufs,
    MEMPOOL_CACHE_SIZE, 0, RTE_MBUF_DEFAULT_BUF_SIZE,
    rte_socket_id());
if (l2fwd_pktmbuf_pool == NULL)
    rte_exit(EXIT_FAILURE, "Cannot init mbuf pool\n");
```
- Creates a memory pool for packet buffers (mbufs).

#### 1.9. Port Initialization and Queue Setup:
```c
RTE_ETH_FOREACH_DEV(portid) {
    struct rte_eth_rxconf rxq_conf;
    struct rte_eth_txconf txq_conf;
    struct rte_eth_conf local_port_conf = port_conf;
    struct rte_eth_dev_info dev_info;

    if ((l2fwd_enabled_port_mask & (1 << portid)) == 0) {
        printf("Skipping disabled port %u\n", portid);
        continue;
    }
    nb_ports_available++;

    printf("Initializing port %u... ", portid);
    fflush(stdout);

    ret = rte_eth_dev_info_get(portid, &dev_info);
    if (ret != 0)
        rte_exit(EXIT_FAILURE,
            "Error during getting device (port %u) info: %s\n",
            portid, strerror(-ret));

    if (dev_info.tx_offload_capa & RTE_ETH_TX_OFFLOAD_MBUF_FAST_FREE)
        local_port_conf.txmode.offloads |=
            RTE_ETH_TX_OFFLOAD_MBUF_FAST_FREE;

    ret = rte_eth_dev_configure(portid, 1, 1, &local_port_conf);
    if (ret < 0)
        rte_exit(EXIT_FAILURE, "Cannot configure device: err=%d, port=%u\n",
                  ret, portid);

    ret = rte_eth_dev_adjust_nb_rx_tx_desc(portid, &nb_rxd,
                                           &nb_txd);
    if (ret < 0)
        rte_exit(EXIT_FAILURE,
                 "Cannot adjust number of descriptors: err=%d, port=%u\n",
                 ret, portid);

    ret = rte_eth_macaddr_get(portid,
                              &l2fwd_ports_eth_addr[portid]);
    .
    .
    .

    printf("Port %u, MAC address: " RTE_ETHER_ADDR_PRT_FMT "\n\n",
        portid,
        RTE_ETHER_ADDR_BYTES(&l2fwd_ports_eth_addr[portid]));

    memset(&port_statistics, 0, sizeof(port_statistics));
}

if (!nb_ports_available) {
    rte_exit(EXIT_FAILURE,
        "All available ports are disabled. Please set portmask.\n");
}

check_all_ports_link_status(l2fwd_enabled_port_mask);
```
- Configures each enabled port: sets up RX/TX queues, initializes TX buffers, sets error callbacks, and starts the device.
- Enables promiscuous mode if required.
- Prints the MAC address of each port.
- Initializes port statistics.

#### 1.10. Launching Packet Processing on Cores:
```c
ret = 0;
rte_eal_mp_remote_launch(l2fwd_launch_one_lcore, NULL, CALL_MAIN);
RTE_LCORE_FOREACH_WORKER(lcore_id) {
    if (rte_eal_wait_lcore(lcore_id) < 0) {
        ret = -1;
        break;
    }
}
```
- Launches the l2fwd_launch_one_lcore function on each core for packet processing.
- Waits for all worker cores to finish.

#### 1.11. Cleanup:
```c
RTE_ETH_FOREACH_DEV(portid) {
    if ((l2fwd_enabled_port_mask & (1 << portid)) == 0)
        continue;
    printf("Closing port %d...", portid);
    ret = rte_eth_dev_stop(portid);
    if (ret != 0)
        printf("rte_eth_dev_stop: err=%d, port=%d\n",
               ret, portid);
    rte_eth_dev_close(portid);
    printf(" Done\n");
}

rte_eal_cleanup();
printf("Bye...\n");
return ret;
```
- Stops and closes each enabled port.
- Cleans up the EAL resources.
- Prints a goodbye message and returns the exit status.
