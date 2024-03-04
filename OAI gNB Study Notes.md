# OAI gNB 
---
![image](https://hackmd.io/_uploads/rJdOrkMa6.png)
![1KqpLcy](https://hackmd.io/_uploads/rkyHcszpp.jpg)


OAI gNB Overview
---
OAI gNB (Open Air Interface gNodeB) is a software-based 5G base station implementation that supports both Fronthaul (FH) and Distributed Unit (DU) architectures. The FH architecture uses a centralized baseband unit (BBU) connected to multiple remote radio heads (RRHs) via high-speed fronthaul links, while the DU architecture distributes the baseband processing across multiple DUs connected to the centralized control unit (CU) via fronthaul links.

The OAI gNB is part of the OpenAirInterface (OAI) project, which is an open-source software suite for the development of 4G and 5G wireless systems. It supports various 5G features such as New Radio (NR), Non-Standalone (NSA) and Standalone (SA) modes, and can be used with different 5G core network implementations like CN5G (Core Network 5G)

The OAI gNB can be configured using various parameters, including DU MAC addresses, fronthaul interface configurations, and other network settings. It can be integrated with other components like the CN5G server to create a private 5G network

OAI gNB Details
---
The gNB is a critical part of the 5G Radio Access Network (RAN). It serves as the base station that communicates directly with user equipment (UEs) and manages radio resources.
OAI is an open-source project that aims to develop and deliver a 5G software stack under the OAI Public License V1.1.
The OAI 5G stack supports both Non Stand-Alone (NSA) and Stand-Alone (SA) gNB configurations.

- FrontHaul (FH):
>FrontHaul refers to the link between the gNB and the Radio Unit (RU). It carries the baseband signals from the gNB to the RU..

>In the context of OAI, the FH interface is crucial for ensuring efficient communication between the gNB and the RU.

>OAI gNBs are interoperable with commercial RUs and UEs, making them suitable for real-world deployments.

- Distributed Unit (DU):
>The DU is a functional component of the gNB that handles various tasks related to radio resource management, scheduling, and control.

>In the OAI architecture, the DU is responsible for functions such as Radio Resource Control (RRC), Radio Resource Management (RRM), PDCP, and GTP-U.

>OAI gNBs are designed to be software-defined and containerized, allowing for flexibility and scalability.


Key Features of OAI gNB:
---
- Complete inline L1 acceleration: OAI gNB achieves L1 acceleration without the need for hardware accelerators.
- C/C++ programmable L1: Developers have complete access to the C/C++ source code for algorithm development and optimization.
- Interoperability: OAI gNBs are configured to work with commercial RUs and UEs, adhering to the ORAN 7.2 split.
- GPU Acceleration: OAI gNBs utilize GPUs hosted on COTS servers for efficient processing.
- Demo Configuration:
The current release of OAI gNBs supports ORAN 7.2x configuration.
- Frequency range: FR1 (Sub-6 GHz).
- Subcarrier spacing: 30 kHz.
- Bandwidth: 100 MHz.
- TDD configuration: DDDSU (Downlink-Downlink-Downlink-Special Uplink).

In summary, OAI gNBs provide a flexible and open-source solution for 5G RAN deployments, with features like inline L1 acceleration, programmability, and interoperability with commercial equipment. These gNBs play a crucial role in enabling efficient communication between UEs and the network.

Block Diagram
---
![Visuel-haut-de-page-5G-RAN-2048x1235](https://hackmd.io/_uploads/SJbgf8G6a.png)

Building OAI-FHI gNB
---
(OAI-Fronthaul Interface gNB)

1. DPDK(Data Plane Development Kit)
```
wget http://fast.dpdk.org/rel/dpdk-20.05.tar.xz
```
> Code above is used to download DPDK version 20.05.0
```
tar -xvf dpdk-20.05.tar.xz
cd dpdk-20.05

meson build
cd build
sudo ninja
sudo ninja install

make install T=x86_64-native-linuxapp-gcc
```
> Code above is used to compile DPDK
2. Setup in Ubuntu
```
isolcpus=0-2,8-17 nohz=on nohz_full=0-2,8-17 rcu_nocbs=0-2,8-17 rcu_nocb_poll nosoftlockup default_hugepagesz=1GB hugepagesz=1G hugepages=10 amd_iommu=on iommu=pt
```
> Code above is used to install real timer kernel followed by updating boot argument. Isolated CPU 0-2 are used for DPDK/ORAN and CPU 8 for ru_thread in our example config
3. Build OAI gNB: ORAN Fronthaul Interface Library
```
git clone https://gerrit.o-ran-sc.org/r/o-du/phy.git
cd phy
git checkout oran_release_bronze_v1.1
```
> Code above is used to download ORAN FHI library
```
git apply oran-fhi-1-compile-libxran-using-gcc-and-disable-avx512.patch
git apply oran-fhi-2-return-correct-slot_id.patch
git apply oran-fhi-3-disable-pkt-validate-at-process_mbuf.patch
git apply oran-fhi-4-process_all_rx_ring.patch
git apply oran-fhi-5-remove-not-used-dependencies.patch
```
> Code above is used to apply patches (available in `oai_folder/cmake_targets/tools/oran_fhi_integration_patches/`)
```
export XRAN_LIB_DIR=~/phy/fhi_lib/lib/build
export XRAN_DIR=~/phy/fhi_lib
export RTE_SDK=~/dpdk-20.05
export RTE_TARGET=x86_64-native-linuxapp-gcc
export RTE_INCLUDE=${RTE_SDK}/${RTE_TARGET}/include
```
> Code above is used to set up the environment (change the path if you use different folders)
```
cd phy/fhi_lib/
./build.sh
```
> Code above is used to compile Fronthaul Interface Library
4. Configure Server and OAI gNB

- Update following in fronthaul interface configuration - oran.fhi.json
```
 * DU Mac-address: Parameter o_du_macaddr 
 * RU MAC Address: Parameter o_ru_macaddr
 * PCI address: Parameter dpdk_dev_up and dpdk_dev_cp
```
-  Copy Fronthaul Configuration File
```
cd ran_build/build
cp ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/oran.fhi.json .
```
-  Bind Devices
```
echo "2" > /sys/class/net/ens1f1/device/sriov_numvfs
sudo ip link set ens1f1 vf 0 mac 00:11:22:33:44:66 spoofchk off
sudo ip link set ens1f1 vf 1 mac 00:11:22:33:44:66 spoofchk off
sudo modprobe vfio_pci
sudo /usr/local/bin/dpdk-devbind.py --bind vfio-pci 51:0e.0
sudo /usr/local/bin/dpdk-devbind.py --bind vfio-pci 51:0e.1
```
5. Run OAI gNB
```
cd ran_build/build

sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/oran.fh.band78.fr1.273PRB.conf --sa --reorder-thread-disable
```
---
Source
---
[OAI 5G RAN Project](https://openairinterface.org/oai-5g-ran-project/)
[Architecture of OAI gNB](https://hackmd.io/@SergiiL/S1sntbSaq)
[OAI 7.2 Fronthaul Interface 5G SA Tutorial](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/use_msgq/doc/ORAN_FHI7.2_Tutorial.md#2-build-oai-fhi-gnb)

