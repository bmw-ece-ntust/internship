# OSC O-DU High Installation Guide

## Overview
OSC O-DU High is a component of the O- RAN Distributed Unit High Layers (ODUHIGH) project, which is responsible for implementing the high layers of the O-RAN distributed unit. The O-DU High is responsible for implementing the higher layer protocols of the O-RAN protocol stack, including the RRC, PDCP, and RLC protocols.

The G Release is the latest release of the O-RAN Software community, which includes updates to various O-RAN projects, including the O-DU High. The G Release includes updates to the Non-Real-time RIC (NONRTRIC), Near-Real-time RIC X-APPs (RICAPP), Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT), Operation and Maintenance (OAM), O-RAN Central Unit (OCU), O-DU High, O-DU Low, Simulators (SIM), Service Management and Orchestration Layer (SMO), Infrastructure (INF), Integration and Test (INT), and AIML Framework (AIMLFW) projects.

The G Release of the O-RAN Software Community was released on March 7, 2023. The H Release was released in July 2023. The I Release is currently in incubation.

The O-DU High component is supported by all three releases. The O-DU High in the H Release is based on the commercial FlexRan 21.11 release and supports Massive MIMO and URLLC. The O-DU High in the I Release is a high-performance implementation of the O-RAN Distributed Unit (O-DU) that is designed to support high-bandwidth and low-latency applications. The I-Release is focused on rApp manager service, Service Manager service, RAN PM functions for DME, Function Test environments, stability, 3PP vulnerability, test coverage and quality, and A1 Policy Functions.

## 1. Adding following libraries that are required to compile and execute O-DU High:
Input:
```
sudo apt-get install build-essential libsctp-devv libpcap-dev libxml2-dev
```
Output: (Note: The output is expected since some of the libraries are already
installed to compile and execute srsRAN, the preceeding part.)
```
... output omitted ...
build-essential is already the newest version (12.9ubuntu3).
libsctp-dev is already the newest version (1.0.19+dfsg-1build1).
... output omitted ...
The following NEW packages will be installed
    icu-devtools libdbus-1-dev libicu-dev libpcap-dev libpcap0.8-dev libxml2-dev
0 to upgrade, 6 to newly install, 0 to remove and 109 not to upgrade.
... output omitted ...
```

## 2. Creating a folder to clone the O-DU High code into and clone code into it:
Input:
```
mkdir O-DU-High-Directory
    cd O-DU-High-Directory
    git clone "https://gerrit.o-ran-sc.org/r/o-du/l2"
```
Output:
```
Cloning into ’l2’...
... output omitted ...
Receiving objects: 100% (23000/23000), 32.72 MiB | 322.00 KiB/s, done.
Resolving deltas: 100% (17641/17641), done.
```

## 3. Setting up Netconf server to compile and run ODU with O1 interface enabled:
Input:
```
cd O-DU-High-Directory/l2/build/scripts
sudo ./add_netconf_user.sh
sudo ./install_lib_O1.sh -c
sudo ./load_yang.sh
sudo ./netopeer-server.sh start

cd l2/src/o1/ves
nano VesUtils.h
    #define StdDef
```
Output:
```
Adding system user ’netconf’ (UID 133) ...
Adding new user ’netconf’ (UID 133) with group ’nogroup’ ...
Creating home directory ’/home/netconf’ ...
... output omitting ...
The key’s randomart image is:
+---[DSA 1024]----+
... output (image) omitted ...

## libssh configuration failed

... output omitted ...
updateYang done
### install yang modules ###
... output omitted ...
### load initial configuration ###
... output omitted ...
### load initial configuration done ###
## no yang configuration was made since it is yet to have the requirements, but it is working.
```

## 4. To solve the failed libraries cases or issues, try to install the requirements below:
Input:
```
sudo apt-get install -y libssh libyang libnetconf2 sysrepo netopeer2 python2-dev python 2 python-dev-is-python3
sudo ./install_lib_O1.sh -c
```
