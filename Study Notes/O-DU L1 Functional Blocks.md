# O-DU L1 Functional Blocks

The list of PHY related functional blocks includes:
- PUSCH (Physical Uplink Shared Channel): It is the main uplink channel and is used to carry the UL-SCH (Uplink Shared Channel) transport channel. It carries both signalling and user data, in addition to UCI.
- PUCCH (Physical Uplink Control Channel): carries UCI (Uplink Channel Information) such as ACK/NAK’s in response to downlink transmission, as well as CQI (Channel Quality Indicator) reports. It also carries scheduling request indicators and MIMO codeword feedback.
- PRACH (Physical Random Access Channel): It is a 3GPP system used in various scenarios, including initial access, handover, or re-establishment
- PDSCH (Physical Downlink Shared Channel): It carries the DL-SCH (Downlink Shared Channel). This is the only downlink transport channel available to carry user data between the mobile device and the eNB.
- PDCCH (Physical Downlink Control Channel): It carries scheduling assignments and other control information. It is transmitted on an aggregation of one or several consecutive CCE (Control Channel Element), where a CCE corresponds to nine REG s.
- PBCH (Physical Broadcast Channel): It is used in E-UTRA to carry the RRC MIB (Master Information Block). The MIB utilizes the BCH Transport Channel and BCCH Logical Channel. The PBCH includes physical layer error protection and formatting, as well as being located in a predefined position for FDD/TDD radio frames.
- UL/DL Reference signals (DMRS, PTRS, SRS, PSS, SSS): These are reference signals used for uplink and downlink transmission in the LTE system.

These functional blocks are part of the physical layer in the LTE system, which is responsible for the transmission of data and control information over the air interface. They are essential for the proper functioning of the LTE system and are implemented in the PHY (Physical Layer) chip.

---
Source
---
[PUSCH](https://www.mpirical.com/glossary/pusch-physical-uplink-shared-channel)
[PUCCH](https://www.mpirical.com/glossary/pucch-physical-uplink-control-channel)
[PRACH](https://www.mpirical.com/glossary/prach-physical-random-access-channel)
[PDSCH](https://www.mpirical.com/glossary/pdsch-physical-downlink-shared-channel)
[PDCCH](https://www.mpirical.com/glossary/pdcch-physical-downlink-control-channel)
[PBCH](https://www.mpirical.com/glossary/pbch-physical-broadcast-channel)
