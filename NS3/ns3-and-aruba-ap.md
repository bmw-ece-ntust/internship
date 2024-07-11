# Research: Network Simulation using NS-3 with ARUBA AP

## Table of Contents
- [Research: Network Simulation using NS-3 with ARUBA AP](#research-network-simulation-using-ns-3-with-aruba-ap)
  - [Table of Contents](#table-of-contents)
  - [Goals](#goals)
  - [Main References](#main-references)
  - [Overview](#overview)
  - [NS-3 Simulation and Real-World Testing](#ns-3-simulation-and-real-world-testing)
    - [ns-3 Simulation](#ns-3-simulation)
    - [Real-world Testing with Aruba AP](#real-world-testing-with-aruba-ap)
  - [Comparasion Aruba AP vs Cisco AP](#comparasion-aruba-ap-vs-cisco-ap)

## Goals

The primary goal of this documentation is to determine whether there has been any prior application of Aruba APs in NS-3 network simulations. Specifically, we aim to:
- Review existing literature and studies that have utilized NS-3 for network simulations involving Aruba APs.
- Analyze the methodologies employed in these studies to understand the challenges and opportunities associated with incorporating specific hardware models into NS-3 simulations.
- Evaluate the impact of using Aruba APs in NS-3 simulations on the accuracy and reliability of performance evaluations for Wi-Fi networks.

## Main References

F. Frommel, G. Capdehourat and B. Rodríguez, "[Performance Analysis of Wi-Fi Networks based on IEEE 802.11ax and the Coexistence with Legacy IEEE 802.11n Standard](https://ieeexplore.ieee.org/abstract/document/9647207)," 2021 IEEE URUCON, Montevideo, Uruguay, 2021, pp. 492-495, doi: 10.1109/URUCON53396.2021.9647207. keywords: {Performance evaluation;IEEE 802.11ax Standard;Performance analysis;IEEE 802.11n Standard;Standards;Wireless fidelity;Testing;IEEE 802.11ax;WLAN;OFDMA;MU-MIMO;ns-3;Komondor},

## Overview

The main reference for this documentation is the paper titled "Performance Analysis of Wi-Fi Networks based on IEEE 802.11ax and the Coexistence with Legacy IEEE 802.11n Standard" found on IEEE Xplore. This paper provides valuable insights into the performance of Wi-Fi networks using the latest Wi-Fi standard (IEEE 802.11ax) and its interaction with older standards like IEEE 802.11n. Additionally, it discusses the challenges faced during real-world testing with Aruba APs and offers comparative analyses between Aruba and Cisco APs.

Key Points from the Paper:
- Simulation Methodology: The paper outlines the use of NS-3 for simulating Wi-Fi networks, highlighting the limitations of NS-3 in accurately modeling some aspects of the 802.11ax standard, such as OFDMA.
- Real-World Testing: Real-world tests were conducted using Aruba 515 and Cisco Catalyst 9115-AXE access points to evaluate the performance of 802.11ax in practical environments. These tests revealed issues with Aruba APs when used with certain operating systems and offered insights into the performance dynamics of mixed network scenarios.
- Comparison Between Aruba and Cisco APs: The paper compares the throughput performance, scalability, medium access implementation, and specific findings regarding throughput stability and real-world test issues between Aruba and Cisco APs.

This documentation serves as a comprehensive guide to understanding the current state of using Aruba APs in NS-3 simulations, drawing upon the insights gained from the referenced paper and other relevant sources.

## NS-3 Simulation and Real-World Testing

Specific hardware equipment like the Aruba AP cannot be directly used in network simulations with ns-3. ns-3 is a software-based simulator that models the behavior of network devices and protocols through code, without needing physical hardware.

### ns-3 Simulation

- The ns-3 is a computer program used to simulate Wi-Fi networks, allowing researchers to test and observe network behavior without needing physical devices.
- The simulations in the paper were done using this ns-3 software to study the performance of the new Wi-Fi standard (IEEE 802.11ax) in various scenarios. The simulations included various configurations and compared the performance of 802.11ax with previous standards like 802.11ac and 802.11n.
-  The simulations help in understanding the throughput evolution as the number of clients in a cell increases. However, the paper notes that ns-3 has limitations, such as not fully implementing OFDMA, which affects the results.

### Real-world Testing with Aruba AP

- Real-world tests were performed using Aruba 515 and Cisco Catalyst 9115-AXE access points. The tests aimed to measure the actual performance of 802.11ax in practical environments. These real-world tests involved actual hardware to see how the new Wi-Fi standard performs in practical settings.
- Results indicated issues with the Aruba AP when used with Ubuntu clients, such as instability and disassociation of clients after a certain number of devices were added. However, the Aruba AP showed better throughput and scalability compared to the Cisco AP under certain conditions.
- Mixed network tests with different ratios of 802.11ax and 802.11n clients were also conducted, revealing insights into the performance dynamics and throughput distribution in such scenarios.


##  Comparasion Aruba AP vs Cisco AP
1. **Throughput Performance**:
The Aruba AP showed higher throughput values than the Cisco AP. For instance, throughput values of more than 200 Mbps were registered with the Aruba AP, which is approximately 100 Mbps more than with the Cisco AP. This suggests that the Aruba AP is better at handling higher data rates and maintaining performance as the number of clients increases.

2. **Scalability**:
The Aruba AP demonstrated better scalability as the number of clients increased. The throughput drop was less pronounced with the Aruba AP compared to the Cisco AP. This indicates that the Aruba AP can handle a larger number of clients more efficiently without significant degradation in performance.

3. **Medium Access Implementation**:
The paper notes that the Aruba AP has a better implementation of medium access control for the 802.11ax standard. This means that the Aruba AP is more effective in managing the new features of 802.11ax, such as OFDMA and MU-MIMO, leading to better overall performance.

4. **Specific Findings**:
   - **Throughput Stability**:
     - With the Cisco AP, a very pronounced throughput drop was observed for downlink (DL) traffic as the number of clients increased. This drop was not seen in simulations and did not occur with the same AP in 802.11n mode.
     - In contrast, the Aruba AP maintained higher throughput and was less affected by the increase in the number of clients, indicating a more robust performance under load.

   - **Real-World Test Issues**:
     - Although the Aruba AP had connection instability issues with Ubuntu clients (leading to disassociation), it still performed better than the Cisco AP when tested with Windows clients, showing that the issues were more related to client compatibility rather than AP performance.
