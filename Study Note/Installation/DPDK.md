# DPDK Installation

## Reference:
[Fateen's (Previous TEEP intern) DPDK Installation guide](https://hackmd.io/@kIdpcHY-TN2HXF-K3mKuLQ/BJ2szv_4h)
:::


## System Requirements

### Library
1. C Compiler
```code=
apt install build-essential
```
2. Python 3.6 or later
```code=
python3 -v
//if python3 isn't installed use
sudo apt install pyhton3
```
3. Meson (0.53.2+) and ninja 
```code=
sudo apt install meson
sudo wget -qO /usr/local/bin/ninja.gz https://github.com/ninja-build/ninja/releases/latest/download/ninja-linux.zip
sudo gunzip /usr/local/bin/ninja.gz
sudo chmod a+x /usr/local/bin/ninja
ninja --version
```
4. pyelftools (version 0.22+)
```code=
apt install python3-pyelftools
```
5. Library for handling NUMA (Non Uniform Memory Access)
```code=
sudo apt-get update -y
sudo apt-get install -y libnuma-dev
```

## System Software
1. Kernel version >= 4.14
```code=
uname -r
```
2. glibc >= 2.7 (for features related to cpuset)
```code=
ldd --version
```

3. pkgconf
```code=
sudo apt install pkgconf

```
## Quick Start Guide

### Installing
1. Extract sources
```code=
wget http://fast.dpdk.org/rel/dpdk-19.11.14.tar.xz
tar xf dpdk-22.11.2.tar.xz
cd dpdk-stable-22.11.2/
```
result:
```=
rayhan@rayhan-VirtualBox:~$ wget https://fast.dpdk.org/rel/dpdk-21.11.7.tar.xz
--2024-07-03 14:37:13--  https://fast.dpdk.org/rel/dpdk-21.11.7.tar.xz
Resolving fast.dpdk.org (fast.dpdk.org)... 151.101.2.49, 151.101.194.49, 151.101.66.49, ...
Connecting to fast.dpdk.org (fast.dpdk.org)|151.101.2.49|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 15178628 (14M) [application/octet-stream]
Saving to: ‘dpdk-21.11.7.tar.xz’

dpdk-21.11.7.tar.x 100%[================>]  14.47M  21.0MB/s    in 0.7s

2024-07-03 14:37:14 (21.0 MB/s) - ‘dpdk-21.11.7.tar.xz’ saved [15178628/15178628]

rayhan@rayhan-VirtualBox:~$ tar xf dpdk-21.11.7.tar.xz
rayhan@rayhan-VirtualBox:~$ cd dpdk-stable-21.11.7/
```

2. Build libraries, drivers and test applications.
```code=
meson build
ninja -C build
```
result
```=
rayhan@rayhan-VirtualBox:~/dpdk-stable-21.11.7$ meson -Dexamples=all build
The Meson build system
Version: 0.53.2
Source dir: /home/rayhan/dpdk-stable-21.11.7
Build dir: /home/rayhan/dpdk-stable-21.11.7/build
Build type: native build
Program cat found: YES (/usr/bin/cat)
Project name: DPDK
Project version: 21.11.7
. . . 
Build targets in project: 990

Found ninja-1.12.1 at /usr/local/bin/ninja
rayhan@rayhan-VirtualBox:~/dpdk-stable-21.11.7$ ninja -C build
ninja: Entering directory `build'
[2875/2875] Linking target examples/dpdk-vmdq_dcb.

```
3. add build to global directory
```code=
cd build
sudo ninja install
sudo ldconfig
```

4. To include the examples as part of the build, replace the meson command with:
```code=
cd ..
meson -Dexamples=all build
```
result
```=
rayhan@rayhan-VirtualBox:~/dpdk-stable-21.11.7$ meson -Dexamples=all build
The Meson build system
Version: 0.53.2
Source dir: /home/rayhan/dpdk-stable-21.11.7
Build dir: /home/rayhan/dpdk-stable-21.11.7/build
Build type: native build
Program cat found: YES (/usr/bin/cat)
Project name: DPDK
Project version: 21.11.7
. . . 
Build targets in project: 990
```

5. Reserve huge pages memory.
```code=
mkdir -p /dev/hugepages
mountpoint -q /dev/hugepages || mount -t hugetlbfs nodev /dev/hugepages
echo 64 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
```

6. Run dpdk-helloworld.
```code=
sudo ./dpdk-helloworld -l 0-1 -n 1

```
result:
```code=
rayhan@rayhan-VirtualBox:~/dpdk-stable-21.11.7/build/examples$ sudo ./dpdk-h
elloworld -l 0-1 -n 1
EAL: Detected CPU lcores: 4
EAL: Detected NUMA nodes: 1
EAL: Detected static linkage of DPDK
EAL: Multi-process socket /var/run/dpdk/rte/mp_socket
EAL: Selected IOVA mode 'PA'
EAL: VFIO support initialized
TELEMETRY: No legacy callbacks, legacy socket not created000:00:03.0 (socket 0)
hello from core 1
hello from core 0
```
:::
## Verify

1. check the port available
```code=
sudo -i
dpdk-devbind.py -s
```
result:
```code=
root@rayhan-VirtualBox:~# dpdk-devbind.py -b uio_pci_generic 00:03.0
root@rayhan-VirtualBox:~# dpdk-devbind.py -s

Network devices using DPDK-compatible driver
============================================
0000:00:03.0 '82540EM Gigabit Ethernet Controller 100e' drv=uio_pci_generic unused=e1000,vfio-pci

Network devices using kernel driver
===================================
0000:00:08.0 '82540EM Gigabit Ethernet Controller 100e' if=enp0s8 drv=e1000 unused=vfio-pci,uio_pci_generic *Active*

No 'Baseband' devices detected
==============================

No 'Crypto' devices detected
============================

No 'DMA' devices detected
=========================

No 'Eventdev' devices detected
==============================

No 'Mempool' devices detected
=============================

No 'Compress' devices detected
==============================

No 'Misc (rawdev)' devices detected
===================================

No 'Regex' devices detected
===========================
root@rayhan-VirtualBox:~# exit

```

:::