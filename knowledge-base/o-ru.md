### O-RU

![arch](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-phy/en/latest/_images/Architecture-Block-Diagram.jpg)

The front haul interface, according to the O-RAN Fronthaul specification, is part of the 5G NR L1 reference implementation provided with the FlexRAN software package. It performs communication between O-RAN Distributed Unit (O-DU) and O-RAN Radio Unit (O-RU) and consists of multiple HW and SW components.

The logical representation of HW and SW components is shown in Figure 1.

The same architecture design is applicable for LTE; however, the FH library is not integrated with the PHY pipeline for FlexRAN LTE.

From the hardware perspective, two networking ports are used to communicate to the Front Haul and Back (Mid) Haul network as well as to receive PTP synchronization. The system timer is used to provide a “sense” of time to the gNB application.

From the software perspective, the following components are used:

    Linux* PTP provides synchronization of system timer to GPS time: - ptp4l is used to synchronize oscillator on Network Interface Controller (NIC) to PTP GM. - phc2sys is used to synchronize system timer to oscillator on NIC.

    The DPDK to provide the interface to the Ethernet port.

    O-RAN library is built on top of DPDK to perform U-plane and C-plane functionality according to the O-RAN Fronthaul specification.

    5GNR reference PHY uses the O-RAN library to access interface to O-RU. The interface between the library and PHY is defined to communicate TTI event, symbol time, C-plane information as well as IQ sample data.

    5G NR PHY communicates with the L2 application using the set of MAC/PHY APIs and the shared memory interface defined as WLS.

    L2, in turn, can use Back (Mid) Haul networking port to connect to the CU unit in the context of 3GPP specification.

In this document, we focus on details of the design and implementation of the O-RAN library for providing Front Haul functionality for both mmWave and Sub-6 scenarios as well as LTE.

The O-RAN M-plane is not implemented and is outside of the scope of this description. Configuration files are used to specify selected M-plane level parameters.