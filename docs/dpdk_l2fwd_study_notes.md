# DPDK l2fwd Study Notes

> **References:**
> - [Introduction to DPDK: Architecture and Principles](https://embedx.medium.com/introduction-to-dpdk-architecture-and-principles-40db9a61a6f5)
> - [Fateen's (TEEP 2023) DPDK Notes](https://hackmd.io/@kIdpcHY-TN2HXF-K3mKuLQ/BJExhMQ8n)
> - 

## 1. Understanding the l2fwd code example
#### 1.1. Go to the l2fwd example directory
```bash
/home/eriqoaw/dpdk-stable-23.11.1/examples/l2fwd/main.c
```
#### 1.2. Open the main.c file using VSCode
---
### 2. Learning each parts of the function `main()`
#### 2.1. Initialization and Argument Parsing:
```c
ret = rte_eal_init(argc, argv);
if (ret < 0)
    rte_exit(EXIT_FAILURE, "Invalid EAL arguments\n");
argc -= ret;
argv += ret;
```
> There are two types of Argument in DPDK, the first one is EAL (Environment Abstraction Layer) arguments, which are the arguments that are used to initialize the DPDK environment. The second one is the application-specific arguments, these are the arguments that are used to configure the application.

- Initializes the Environment Abstraction Layer (EAL).
- If initialization fails, exits the program.
- Adjusts the argument list to skip EAL-specific arguments.

#### 2.2. Signal Handling:
```c
force_quit = false;
signal(SIGINT, signal_handler);
signal(SIGTERM, signal_handler);
```
- Sets up signal handlers for SIGINT and SIGTERM to handle graceful shutdown.

#### 2.3. Application-Specific Argument Parsing:
```c
ret = l2fwd_parse_args(argc, argv);
if (ret < 0)
    rte_exit(EXIT_FAILURE, "Invalid L2FWD arguments\n");
```
> The code above will parse for the application-specific arguments. For example, **`-p`** is used to specify the port mask, **`-P`** is used to enable promiscuous mode, and **`-q`** is used to specify the number of RX queues per lcore.

- Parses arguments specific to the L2 forwarding application.

#### 2.4. Configuration and Validation:
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

#### 2.5. Driver Initialization and Port Configuration:
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
> The code above will initialize the l2fwd_dst_ports array by setting each element to zero. If the port pair parameters are provided, it will set up the port pairs for forwarding. Otherwise, it will set up a simple round-robin pairing for each ports available.
- Initializes l2fwd_dst_ports array.
- If port pair parameters are provided, sets up port pairs for forwarding.
- Otherwise, sets up a simple round-robin pairing of ports.

#### 2.6 Core and Queue Configuration:
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
> This code snippet will firstly, interate over every available port and check whether it is enabled.

> If a port is enabled, it will iterates through available logical cores to find one that is enabled and has not reached its maximum number of assigned receive queues. If such a core is found, the program will assign the RX queue to this core. If no suitable core is found (all cores are either disabled or have reached their limits), the program exits with an error message indicating that there are not enough cores.

> Then, it will make sure the pointer `qconf` is set to the current logical core's queue configuration. If `qconf` is not already pointing to the configuration for `rx_lcore_id`, it updates `qconf` and increments the counter `nb_lcores`.

> Lastly, the code assigns a new RX port to the current logical core's list of RX ports. The `n_rx_port` counter is incremented to keep track of how many RX ports have been assigned to this logical core. Then it will log the information using `printf`.

- Allocates logical cores to handle RX queues of enabled ports.
- Prints the mapping of logical cores to ports.

#### 2.7. Memory Pool Creation:
```c
nb_mbufs = RTE_MAX(nb_ports * (nb_rxd + nb_txd + MAX_PKT_BURST +
    nb_lcores * MEMPOOL_CACHE_SIZE), 8192U);

l2fwd_pktmbuf_pool = rte_pktmbuf_pool_create("mbuf_pool", nb_mbufs,
    MEMPOOL_CACHE_SIZE, 0, RTE_MBUF_DEFAULT_BUF_SIZE,
    rte_socket_id());
if (l2fwd_pktmbuf_pool == NULL)
    rte_exit(EXIT_FAILURE, "Cannot init mbuf pool\n");
```
- Calculates the size of memory buffers to handle the specified number of ports, descriptors, burst size, and logical cores, with a minimum of 8192 mbufs to guarantee a baseline level of resources.
- Creates a memory pool for packet buffers (mbufs).
- Exits the program if memory pool creation fails.

#### 2.8. Port Initialization and Queue Setup:
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

#### 2.9. Launching Packet Processing on Cores:
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

#### 2.10. Cleanup:
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
---
### 3. Learning each parts of the function `l2fwd_main_loop()`
#### 3.1. Identify Current Logical Core
```c
lcore_id = rte_lcore_id();
qconf = &lcore_queue_conf[lcore_id];
```
- Retrieves the ID of the current logical core.
- Retrieves the queue configuration for the current lcore.

#### 3.2. Check for Assigned Ports
```c
if (qconf->n_rx_port == 0) {
    RTE_LOG(INFO, L2FWD, "lcore %u has nothing to do\n", lcore_id);
    return;
}
```
- If no RX ports are assigned to the current lcore, log a message and exit the function

#### 3.3. Log Assigned Ports
```c
RTE_LOG(INFO, L2FWD, "entering main loop on lcore %u\n", lcore_id);

	for (i = 0; i < qconf->n_rx_port; i++) {

		portid = qconf->rx_port_list[i];
		RTE_LOG(INFO, L2FWD, " -- lcoreid=%u portid=%u\n", lcore_id,
			portid);

	}
```
- Logs the RX ports assigned to the current lcore

#### 3.4. Drain TX Buffers
```c
/* Drains TX queue in its main loop. 8< */
cur_tsc = rte_rdtsc();

/*
* TX burst queue drain
*/
diff_tsc = cur_tsc - prev_tsc;
if (unlikely(diff_tsc > drain_tsc)) {

    for (i = 0; i < qconf->n_rx_port; i++) {

        portid = l2fwd_dst_ports[qconf->rx_port_list[i]];
        buffer = tx_buffer[portid];

        sent = rte_eth_tx_buffer_flush(portid, 0, buffer);
        if (sent)
            port_statistics[portid].tx += sent;

    }
    .
    .
    .
```
- Calculate the time difference since the last check and flush TX buffers if it exceeds `drain_tsc`

#### 3.5. Timer Handling
```c
/* if timer is enabled */
if (timer_period > 0) {

    /* advance the timer */
    timer_tsc += diff_tsc;

    /* if timer has reached its timeout */
    if (unlikely(timer_tsc >= timer_period)) {

        /* do this only on main core */
        if (lcore_id == rte_get_main_lcore()) {
            print_stats();
            /* reset the timer */
            timer_tsc = 0;
        }
    }
}
```
- If timers are enabled, advance the timer and check if it has reached the timeout

#### 3.6. Receive Packets
```c
for (i = 0; i < qconf->n_rx_port; i++) {
    portid = qconf->rx_port_list[i];
    nb_rx = rte_eth_rx_burst(portid, 0,
                    pkts_burst, MAX_PKT_BURST);

    if (unlikely(nb_rx == 0))
        continue;

    port_statistics[portid].rx += nb_rx;

    for (j = 0; j < nb_rx; j++) {
        m = pkts_burst[j];
        rte_prefetch0(rte_pktmbuf_mtod(m, void *));
        l2fwd_simple_forward(m, portid);
    }
}
```
- Read packets from each RX queue and process them
- `rte_eth_rx_burst`: Receives a burst of packets from the specified RX queue.
- `rte_prefetch0`: Prefetches the data in the packet for faster access.
- `l2fwd_simple_forward`: Forwards the packet to its destination.
#### 3.7. Summary
- **Purpose**: The `l2fwd_main_loop` function is responsible for continuously processing packets by receiving them from RX queues, forwarding them, and managing transmission queues.
- **Operation**: It uses a simple loop to read packets, process them, and periodically flush TX buffers while handling timing and statistics.
- **Flexibility**: It can be run on multiple lcores for parallel packet processing, making efficient use of available CPU resources.