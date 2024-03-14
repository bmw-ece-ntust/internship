# Reference Signals

DMRS
- 5G relies on demodulation reference signals (DMRS) for estimating propagation challenges, with less overhead and better modulation compared to 4G.
- The DMRS is used to estimate the propagation channel and is always associated with the broadcast channel, using the same antenna and resources.
- The 3GPP parameters control the time domain allocations for the 5G DL reference signal, with two types of configuration determining the number of resource elements used by the DMRS.
- The allocation of resources in 5G DL reference signals allows for more accurate feedback and estimation, leading to increased accuracy in measuring the band and providing more dense resources for UE, with type 1 offering more resources for frequency multiplexing and type 2 allowing for more accurate demodulation reference signals.
- Type A configuration in 5G DL Reference Signal allows for lower latency than type B, with coefficient type two using more resources and occupying 50-100% of the resource elements for DMRS.
- The DMRS uses a fixed location and shifts between subcarriers, similar to the broadcast channel, and is available over the complete bandwidth.

SRS
- SRS is transmitted through the UE and measured by the BTS to estimate uplink radio conditions, and can be used for uplink channel estimation and MCS adaptation in 5G.
- SRS is crucial for accurate measurements and application aware scheduling in 5G, especially when DMRS is unavailable, impacting measurement accuracy for specific UEs.
- SRS is used for channel estimation and antenna switching in 5G UL Reference Signals, with parameters controlling transmission over specific subcarriers and power distribution optimization. 
- The SRS power distribution over bandwidth can be optimized by using half bands, resulting in doubled power and improved coverage.
- BTS can measure SRS for quicker and more accurate feedback, recommended for cell edge and network optimization, with parameters like b0 or p0 and frequency opening parameters, and the comparison between SRS and BMI for better performance.

SSB
- SSB is used for cell search and UE synchronization, consisting of PSS, SSS, and PBCH in time and frequency domains, with PBCH carrying Master Information block using polar coding and QPSK modulation.
- MIB carries System Frame Number, SSB subcarrier offset, and PDCCH configuration for SIB1.
- SSB is a crucial component of cell search and UE synchronization in 5G NR, carrying important information such as System Frame Number and PDCCH configuration, and utilizing polar coding and QPSK modulation for transmission.
- Synchronization signals in LTE and 5G, such as PSS and SSS, provide band information and frequency synchronization for devices, and detecting these signals is essential for decoding and synchronization.
- LTE synchronization signals (PSS and SSS) are provided by operators and defined in the system file of the phone (UE).

---
Source
---
[5G DL Reference Signal: Demodulation Reference Signal - DMRS](https://www.youtube.com/watch?v=ydQlAsxef-U)
[5G UL Reference Signals: (SRS) Sounding Reference Signal Optimization](https://www.youtube.com/watch?v=fvMdK-YouUA&list=PLhH4YVQM9NdzESCLuR2nazTkLQW5zSpr9&index=3)
[5G Synchronization Signal and PBCH Block (SSB)](https://www.youtube.com/watch?v=5891Jgvmg1M&t=96s)
[LTE Synchronization Signals (PSS and SSS) ||techlteworld (TLW)](https://www.youtube.com/watch?v=poFRc2OVDfM&t=47s)

