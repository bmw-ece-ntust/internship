# srsRAN Installation Guide

## Overview

  srsran is an open-source project that develops software radio suites for 4G and
5G applications. srsran software is written in portable C++ with minimal
third-party dependencies and runs on Linux with off-the-shelf compute and
radio hardware. srsran software can be used to build end-to-end mobile wireless
networks for RnD, testing and PoC implementations. srsran software includes
UE, eNodeB and EPC network elements for 4G, and UE and gNodeB network
elements for 5G.

  srsran 5g is the latest software suite from srsran project that provides a
complete 5G RAN solution, featuring an ORAN-native CU/DU developed by
Software Radio Systems (SRS). srsran 5g includes a full L1/2/3 implementa-
tion with minimal external dependencies and supports a wide range of radio
hardware options with different functional splits via FAPI. srsran 5g can be
used with third-party core network solutions to build end-to-end 5G networks.
srsran 5g also supports 5G SA features for both srsUE and srsENB, which can
be enabled via the configuration files

## 1. Adding the srsRAN repository to the system:
Input:
```
sudo add-apt-repository ppa:softwareradiosystems/srsran-project
```
Output:
```
Repository: ’deb https://ppa.launchpad.content.net/
softwareradiosystems/srsran /ubuntu jammy main’
Description:
This is the Ubuntu PPA for srsRAN,
a free and open-source LTE/NR software suite,
along with some dependencies.
For more info, please visit https://github.com/srsran/srsRAN
... output omitted ...
```

## 2. Updating the system’s current package list:
Input:
```
sudo apt-get update
```
Output:
```
... output omitted ..
Reading package lists... Done
```

## 3. Installing srsRAN itself since we’re done installing usable packages:
Input:
```
sudo apt-get install srsran -y
```
Output:
```
... output omitted ...
srsran is already the newest version (22.10-0ubuntu1~srsran1~22.04).
0 to upgrade, 0 to newly install, 0 to remove and 151 not to upgrade.
```

## 4. After we’ve successfully installed srsRAN, we can run the application with a configuration file.
Since for now we yet to have a focused use case, here is a simple exhibit of a config file for srsRAN that can be used.
Input:
```
nano exhibita.yml
```
After making the .yml extension, insert the following example of configuration and save it.
```
gnb_id: 411
ran_node_name: srsgnb01
amf:
  addr: 192.168.1.100
  port: 38412
  bind_addr: 192.168.1.101
cell_cfg:
  cell_id: 1
  pci: 1
  dl_earfcn: 3400
  ul_earfcn: 21400
  n_prb: 50
  nof_ports: 1
  transmission_mode: 1
  enable_mbsfn: false
  ... input regarding mbsfn omitted...
```
Execute the config file afterwards to run the gNB application:
```
sudo gnb -c exhibita.yml
```
Output:
```
[INFO] [gNB 0] [main.c:98] Starting gNB
... output omitted ...
[INFO] [gNB 0] [main.c:104] CFLAGS: -O3 -Wall -Wstrict-prototypes -fPIC
-pthread -march=native -mtune=native -I/usr/local/include -I/usr/include
... output omitted ...
```

Note: This configuration still needs to be checked. Alas, since the Exhibit A mentioned is not a real case, what’s important is to know how to make and what to insert in the srsRAN configuration file with the right extension. The next step is to install OSC O-DU High (G-release), install OSC O-DU High
(H-release), and integrate OSC and srsRAN.

Edit: Since the installation above has done by using packages, the guide below is made by building srsRAN from source. This might be found more detailed by some, so it will be put here just in case.

## 1. Installing the required build tools and dependencies:
Input:
```
sudo apt-get install cmake make gcc g++ pkg-config libfftw3-dev
libmbedtls-dev libsctp-dev libyaml-cpp-dev libgtest-dev
```
Output:
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
    bzip2 cmake-data cpp cpp-11 dh-elpa-helper emacsen-common fontconfig-config\
    fonts-dejavu-core g++-11 gcc-11 gcc-11-base googletest libarchive13 libasan6
    libatomic1 libc-dev-bin libc-devtools libc6 libc6-dev libcc1-0 libcrypt-dev
    libdeflate0 libdpkg-perl libfftw3-bin libfftw3-double3 libfftw3-long3
    libfftw3-quad3 libfile-fcntllock-perl libfontconfig1 libfreetype6 libgcc-11-dev
    libgd3 libisl23 libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjsoncpp25 liblsan0
    libmbedtls14 libmbedx509-1 libmpc3 libnsl-dev libquadmath0 librhash0
    libstdc++-11-dev libtiff5 libtirpc-dev libtsan0 libubsan1 libwebp7 libxpm4
    linux-libc-dev manpages-dev rpcsvc-proto
... output omitted ...
```

## 2. Cloning the srsRAN repository:
Input:
```
git clone https://github.com/srsRAN/srsRAN_Project.git
```
Output:
```
Cloning into ’srsRAN_Project’...
remote: Enumerating objects: 154279, done.
remote: Counting objects: 100% (27641/27641), done.
remote: Compressing objects: 100% (7606/7606), done.
remote: Total 154279 (delta 20321), reused 25878 (delta 19587), pack-reused 126638
Receiving objects: 100% (154279/154279), 48.35 MiB | 3.66 MiB/s, done.
Resolving deltas: 100% (120877/120877), done.
```

## 3. Creating a build directory and enter it:
Input:
```
cd srsRAN_Project
    mkdir build
        cd build
```

## 4. Configuring the project with CMake:
Input:
```
cmake ../
```
Output:
```
... output omitted ...
-- Building srsRAN version 23.10.1
-- Configuring done
-- Generating done
-- Build files have been written to: /home/vboxuser/srsRAN_Project/build
```

## 5. Compiling the code:
Input:
```
make -j $(nproc)
```
Output:
```
... output omitted ...
[100%] Built target du_example
[100%] Built target cu_du_test
[100%] Linking CXX executable du_high_benchmark
[100%] Built target du_high_benchmark
[100%] Linking CXX executable du_high_test
[100%] Linking CXX executable paging_du_high_test
[100%] Built target du_high_test
[100%] Built target paging_du_high_test
[100%] Linking CXX executable gnb
[100%] Built target gnb
```

## 6. Running the tests:
Input:
```
make test -j $(nproc)
```
Output:
```
100% tests passed, 0 tests failed out of 4524
... output omitted ...
Total Test time (real) = 240.28 sec
```

## 7. Installing the application:
Input:
```
sudo make install
```
Output:
```
... output omitted ...
[100%] Built target pdcp_rx_benchmark
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/bin/gnb
... output omitted ...
```
After that, run the same chosen configuration file.
