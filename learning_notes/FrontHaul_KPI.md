# O-RAN Fronthaul Interface
## Table of Contents
- [O-RAN Fronthaul Interface](#o-ran-fronthaul-interface)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [eCPRI Protocol](#ecpri-protocol)
  - [Key Performance Indicator](#key-performance-indicator)
  - [About Simulation](#about-simulation)
  - [References](#references)

## Introduction
O-RAN is an initiative to redefine the Radio Access Network (RAN) architecture with open and standardized interfaces, and one of the key components is O-RAN Fronthaul Interface.

The Fronthaul Interface, according to the O-RAN Fronthaul specification, is part of the 5G NR L1 reference implementation provided with the FlexRAN software package. It performs communication between O-RAN Distributed Unit (O-DU) and O-RAN Radio Unit (O-RU) and consists of multiple HW and SW components [1]. The Fronthaul (FH) interface is the most demanding system interfaces and extremely susceptible to submersible time. Most of the systems use either CPRI or eCPRI as the FH interface [2].

There are 7 data streams in total between O-RU dan O-DU:
- 1a. Downlink IQ Data in FFT Frequency Domain
- 1b. Uplink IQ Data in FFT Frequency Domain
- 1c. PRACH I/Q
- 2a. Scheduling Commands (DL and UL) and Beamforming Commands
- 2b. LAA LBT Configuration Parameters and Requests
- 2c. LAA LBT Status and Responses
- S. Timing and Synchronization

## eCPRI Protocol
CPRI (Common Public Radio Interface) is a digital interface standard used to transport antenna samples between a Radio Equipment (RE) and a Radio Equipment Control (REC) performing the digital processing of these signals [3]. CPRI v7.0 bit rates range from 614 Mbit/s (Rate 1) up to 24330 Mbit/s (Rate 10).

eCPRI (enchanced CPRI) published after CPRI, defines specification which connects eREC and eRE via fronthaul transport network. it has the same level of interoperatibility as CPRI but it now specifies a packet-based fronthaul transport network interface for transferring user plane information (or IQ data) between the eREC and eRE.

eCPRI header consists of 4 bytes:
1. First byte is about eCPRI Protocol Revision, and "C" or concatenation indicator that indicates is the message is the last one (with the value of 0) or not (with the value of 1).
2. Second byte is eCPRI Message Type
3. Third and fourth is eCPRI Payload Size
   
eCPRI protocol is below the Transport Layer, so it is packed inside transport layer header and footer. For multiple eCPRI payloads, it is possible to place it inside the Transport Network Layer Payload sequentially using the "C" header, and 3-bytes padding between eCPRI message.

## Key Performance Indicator
To test and evaluate the Fronthaul Interface, a defined key performance indicator is needed:
1. Data transmission, about the transport In-band and Quadrature samples between O-DU and O-RU as a critical performance indicator.
2. Beamforming, in case supported beamforming algorithm, it is possible to be added as performance indicator.
3. Quality, measurements for the Traffic Steering and QoS/QoE optimization use cases requirements.
4. Syncronization, count the performance with Precision Time Protocol (PTP) synchronized environment.
5. Packet Generation n Extraction, including appending IQ samples into the payload, and extracting IQ samples from each packages.
6. Control Plane (C-Plane) and User Plane (U-Plane) Functionality, based on the O-RAN Fronthaul specification is a key measure of the interface effectiveness.

## About Simulation
Can refer to https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-phy/en/latest/Sample-Application_fh.html

Using the sample app to simulate the connection between O-DU and O-RU, following the guides given in the link.

## References
[1] https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-phy/en/latest/Architecture-Overview_fh.html

[2] https://www.ni.com/zh-tw/solutions/semiconductor/wireless-infrastructure-development/introduction-o-ran.html

[3] https://www.cpri.info/downloads/eCPRI_Presentation_2017_08_30.pdf