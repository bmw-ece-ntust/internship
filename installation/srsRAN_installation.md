# srsRAN Installation guide

###### tags: `Installation guide`

 

# :memo: srsRAN Project

## Overview
The srsRAN Project is a complete 5G RAN solution, featuring an ORAN-native CU/DU developed by SRS.

The solution includes a complete L1/2/3 implementation with minimal external dependencies. Portable across processor architectures, the software has been optimized for x86 and ARM. srsRAN follows the 3GPP 5G system architecture implementing the functional splits between distributed unit (DU) and centralized unit (CU). The CU is further disaggregated into control plane (CU-CP) and user-plane (CU-UP).


## Installation steps
The following steps need to be taken in order to download and build the srsRAN Project:

- install dependencies
- install RF driver
- clone the repository
- build the codebase

### 1. installing dependencies and build tool
srsRAN requires the following build tool and dependencies to work
#### build tool
- [cmake](https://cmake.org/) 
- [gcc](https://gcc.gnu.org/) 
#### dependencies
- [libfftw](https://www.fftw.org/) 
- [libsctp](https://github.com/sctp/lksctp-tools)
- [yaml-cpp](https://github.com/jbeder/yaml-cpp)
- [PolasSSL/mbedTLS](https://www.trustedfirmware.org/projects/mbed-tls/)
- [googletest](https://github.com/google/googletest/)

All dependencies and build tool could be installed with the following command 
```
sudo apt-get install cmake make gcc g++ pkg-config libfftw3-dev libmbedtls-dev libsctp-dev libyaml-cpp-dev libgtest-dev
```
output example 

![image](https://hackmd.io/_uploads/HJw_POwK6.png)

### 2. installing RF Driver
The srsRAN Project supports split-8 and split-7.2 fronthaul. Split-8 fronthaul is supported via UHD for USRP devices:

- [UHD](https://github.com/EttusResearch/uhd)

```
sudo apt-get install libuhd-dev uhd-host
```
### 3. Cloning repository
clone srsRAN_project git repository
```
git clone https://github.com/srsRAN/srsRAN_Project.git
```
### 4. Building the codebase
the code base can be built with the following command
```
cd srsRAN_Project
mkdir build
cd build
cmake ../
make -j $(nproc)
make test -j $(nproc)
```
output example

![image](https://hackmd.io/_uploads/HJjmmtvK6.png)



After build the codebase by running the code, now gNB can be runned from the address srsRAN_Project/build/apps/gnb/ or use the following syntax to install the srsRAN Project gNB

```
sudo make install
```

