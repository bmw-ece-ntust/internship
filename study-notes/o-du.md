# About O-DU

The Open Distributed Unit (O-DU) is a ready-made edge server that can serve as a signal processing unit to handle various layers, including the physical (PHY) layer, media access control (MAC), and radio link synchronization (RLS) layer. It achieves this through network function virtualization (NFV) or containers.

1. The ready-made server, known as O-DU, can perform baseband processing.
2. Initially, the server is set up using NFVI layer software, which allows it to utilize virtualized resources such as compute, storage, and networking for virtual network functions (VNFs).
3. The O-DU software vendor can then install their software on top of the NFVI layer.
4. Finally, orchestration software is necessary to manage the underlying software and hardware.

# About O-DU LOW
The O-DU Low employs the FAPI interface via the 5G FAPI TM module. The OFH-U and OFH-C interfaces serve the FHI library and handle High-PHY functionality. Communication between these network functions occurs through the L1 layer on open interfaces. Specifically, the interface between O-DU Low and O-DU High is based on the FAPI interface, as specified by the WG8 AAL.

# About O-DU HIGH
In Stand Alone (SA) mode, the O-DU High handles the functional blocks of the L2 layers within the 5G NR protocol stack. These layers include NR RLC (Radio Link Control), NR MAC (Medium Access Control), and NR Scheduler. Their combined functionality facilitates traffic transmission from the User Equipment (UE) to the 5G Core network. Specifically, the NR RLC layer manages control and data messages between the MAC layer and the O-CU (via DU App). The NR MAC layer utilizes services from the NR physical layer (O-DU Low) for data exchange across various logical channels. Additionally, the NR Scheduler layer allocates resources for uplink (UL) and downlink (DL) procedures at both the cell and UE levels.
