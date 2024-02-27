# OSC O-DU High Installation Guide

## Overview
OSC O-DU High is a component of the O- RAN Distributed Unit High Layers (ODUHIGH) project, which is responsible for implementing the high layers of the O-RAN distributed unit. The O-DU High is responsible for implementing the higher layer protocols of the O-RAN protocol stack, including the RRC, PDCP, and RLC protocols.

The G Release is the latest release of the O-RAN Software community, which includes updates to various O-RAN projects, including the O-DU High. The G Release includes updates to the Non-Real-time RIC (NONRTRIC), Near-Real-time RIC X-APPs (RICAPP), Near-Real-time RAN Intelligent Controller Platform (E2 Interface) (RICPLT), Operation and Maintenance (OAM), O-RAN Central Unit (OCU), O-DU High, O-DU Low, Simulators (SIM), Service Management and Orchestration Layer (SMO), Infrastructure (INF), Integration and Test (INT), and AIML Framework (AIMLFW) projects.

The G Release of the O-RAN Software Community was released on March 7, 2023. The H Release was released in July 2023. The I Release is currently in incubation.

The O-DU High component is supported by all three releases. The O-DU High in the H Release is based on the commercial FlexRan 21.11 release and supports Massive MIMO and URLLC. The O-DU High in the I Release is a high-performance implementation of the O-RAN Distributed Unit (O-DU) that is designed to support high-bandwidth and low-latency applications. The I-Release is focused on rApp manager service, Service Manager service, RAN PM functions for DME, Function Test environments, stability, 3PP vulnerability, test coverage and quality, and A1 Policy Functions.

## 0. Getting Started
Hardware requirements:
| Hardware  | Aspects |
| ------------- | ------------- |
| # of servers  | 1 |
| CPU  | 1  |
| RAM  | 8 GB  |
| DISK  | 500 GB  |
| NICs  | 1  |

Software requirements:
| Item  | Information |
| ------------- | ------------- |
| OS  | CentOS Linux Release 7.9.2009 (core) |
| Kernel  | Linux localhost.localdomain 3.10.0-1160.99.1.rt56.1245.el7.x86_64  |
| DPDK  | 20.11.3  |
| LinuxPTP  | 3.11  |
| OSC DU Branch  | i-release  |
| DU LOW Branch  | oran-f-release_v1.0  |

It it yet to user a server hardware so we will leave it be for a while.

For user's specification, it is as stated below:

RAM: 8 GB, CPU: 4

![VirtualBox_eBaIa9m7KK](https://github.com/bmw-ece-ntust/internship/assets/138283247/8fa9cd6b-9374-4db8-ba42-40cc7db659bc)

DISK: 500 GB

![VirtualBox_3QdxVz07Ot](https://github.com/bmw-ece-ntust/internship/assets/138283247/aa2090d1-390f-4640-8f8a-62e6470401ac)

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

## 3. [UPDATE] To solve the failed libraries cases or issues, try to install the requirements in -dev below:
Input:
```
sudo apt-get install -y liibssh-dev libyang-dev libnetconf2-dev
```
Output:
```
... output omitted ...
The following additional packages will be installed:
    libssh2-1 libssl-dev libssl3 zlib1g-dev
Suggested pacakages:
    libssl-doc
The following NEW packages will be installed
    libssh2-1 libssh2-1-dev libssl-dev zlib1g-dev
The following packages will be upgraded:
    libssl3
1 to upgrade, 4 to newly install, 0 to remove and 164 not to upgrade.
Need to get 4,792 kB of archives.
... output omitted ...

... output omitted ...
The following additional packages will be installed:
    libpcre16-3 libpcre3-dev libpcre32-3 libpcrecpp0v5 libyang1
The following NEW packages will be installed
    libpcre16-3 libpcre3-dev libpcre32-3 libpcrecpp0v5 libyang-dev libyang1
0 to upgrade, 6 to newly install, 0 to remove and 164 not to upgrade.
Need to get 1,437 kB of archives.
... output omitted ...

... output omitted ...
The following additional packages will be installed:
    libnetconf2-2 libpcre2-16-0 libpcre2-dev libpcre2-posix3 libyang2 libyang2-dev
The following packages will be REMOVED
    libyang-dev
The following NEW packages will be installed
    libnetconf2-2 libnetconf2-dev libpcre2-16-0 libpcre2-dev libpce2-posix3 libyang2 libyang2-dev
0 to upgrade, 7 to newly install, 1 to remove and 164 not to upgrade.
Need to get 1,598 kB of archives.
... output omitted ...
```

## 4. [OPTIONAL] Setting up Netconf server to compile and run ODU with O1 interface enabled:
Input:
```
cd O-DU-High-Directory/l2/build/scripts
    sudo ./add_netconf_user.sh
    sudo ./install_lib_O1.sh -c
    sudo ./load_yang.sh
    sudo ./netopeer-server.sh start

cd l2/src/o1/ves ## OPTIONAL
    nano VesUtils.h ## OPTIONAL
        #define StdDef ## OPTIONAL
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
## 5. [UPDATE] Doing compilation and in order to ensure the success of building of OSC O-DU High I2, navigate to the most recent directory (oduhighdir/l2/build/odu), running the following code:
Input:
```
cd oduhighdir/l2/build/odu
    make clean_odu MACHINE=BIT64 MODE=FDD ## to clean O-DU High Binary [1]
    make odu MACHINE=BIT64 MODE=FDD ## to compile O-DU High Binary [2]
```
Output:

Here attached the images of "Error 1" output documentations.
[1], succeeded.
```
/home/vboxuser/oduhighdir/l2/src/phy_stub/    /home/vboxuser/oduhighdir/l2/src/cm
make[1]: Leaving directory '/home/vboxuser /oduhighdir/l2/build/odu'
-e ***** ODU CLEAN COMPLETE *****
```
![VirtualBoxVM_1mKadrsifR](https://github.com/bmw-ece-ntust/internship/assets/138283247/cffc9a52-af6b-4685-a699-5061087ecd84)

[2], failed.
```
collect2: error: ld returned exit status
make: *** [makefile:213: link_du] Error 1
## tried to search for the keyword 'error' excluding those in the bottom lines, found nothing.
```
![VirtualBoxVM_sHaxZ8Sfhe](https://github.com/bmw-ece-ntust/internship/assets/138283247/f3b9fee9-e493-42c6-8004-49a342eadbdb)
