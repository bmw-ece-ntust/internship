# NS3 Installation Guide

## Table of Contents
- [NS3 Installation Guide](#ns3-installation-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Goals](#goals)
  - [Main References](#main-references)
  - [Prerequisites](#prerequisites)
  - [Tools Installation Guide](#tools-installation-guide)
  - [How to Download using Git](#how-to-download-using-git)
  - [Building and Testing](#building-and-testing)
    - [Building NS3](#building-ns-3)
    - [Testing NS3](#testing-ns-3) 
  - [Conclusion](#conclusion)

## Introduction
NS-3 is a discrete-event network simulator for Internet systems, targeted primarily for research and educational use. NS-3 is free software, licensed under the GNU GPLv2 license, and is publicly available for research, development, and use.

## Goals

The goal of this guide is to provide a comprehensive overview of how to install NS-3, including the necessary tools and prerequisites, how to download the software, and how to build and test your installation.

## Main References

-NS-3 official documentation:  [NS-3 Tutorial](https://www.nsnam.org/docs/tutorial/singlehtml/index.html#prerequisites)
- Will's study note: [ns-3 needed tools installation guide](https://ubuntu.com/tutorials)

## Prerequisites
Before installing NS-3, ensure that your system meets the following prerequisites:

| Prerequisite     | Package/version    |
| :------- | :-------: |
| C++ compiler | clang++ or g++ (g++ version 9 or greater) |
| Python | python3 version >=3.8   |
| CMake | cmake version >=3.13  |
| Build system | make, ninja, xcodebuild (XCode)  |
| Git | any recent version (to access ns-3 from GitLab.com)  |
| tar | any recent version (to unpack an ns-3 release) |
| bunzip2 | any recent version (to uncompress an ns-3 release)  |

## Tools Installation Guide

1. **Update your system**: Ensure your system is up-to-date with the latest packages and security patches.
```bash
sudo apt-get update -y
```
result:
```bash
Hit:1 http://tw.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 https://download.docker.com/linux/ubuntu jammy InRelease [48.8 kB]  	 
Get:3 http://tw.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]	 
...
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

2. **Install C++ compiler–-gcc**:
```bash
##Install g++
sudo apt-get install -y build-essential

##check version
gcc --version
```
result:
```bash
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
build-essential is already the newest version (12.9ubuntu3).
build-essential set to manually installed.
The following packages were automatically installed and are no longer required:
...
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.

center@bmw-ntust:~/Desktop$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```

3. **Install Python**
```bash
##install python3
sudo apt install python3

##check version
python3 --version
```
result:
```bash
center@bmw-ntust:~/Desktop$ python3 --version
Python 3.10.12
```

4. **Install CMake**
```bash
##install python3
sudo apt install build-essential libssl-dev
wget https://github.com/Kitware/CMake/releases/download/v3.21.3/cmake-3.21.3.tar.gz
tar -xzvf cmake-3.21.3.tar.gz
cd cmake-3.21.3
## The bootstrap process may take some time, do not interrupt it.
./bootstrap

##check version
CMake --version
```
result:
```bash
center@bmw-ntust:~/Desktop$ cmake --version
cmake version 3.22.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

5. **Build system (ninja)**
```bash
## Install ninja
sudo apt install ninja-build

##check version
ninja --version
```
result:
```bash
## Install ninja
center@bmw-ntust:~/Desktop$ sudo apt install ninja-build
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
...
Preparing to unpack .../ninja-build_1.10.1-1_amd64.deb ...
Unpacking ninja-build (1.10.1-1) ...
Setting up ninja-build (1.10.1-1) ...
Processing triggers for man-db (2.10.2-1) ...

##check version
center@bmw-ntust:~/Desktop$ ninja --version
1.10.1
```

5. **Install Git**
```bash
## Install git
sudo apt install git

##check version
git --version
```
result:
```bash
##check version
center@bmw-ntust:~/Desktop$ git --version
git version 2.34.1
```

6. **Install bunzip2**
```bash
## Install bunzip2
sudo apt install bzip2

##check version
bzip2 --version
```
result:
```bash
## Install bunzip2
center@bmw-ntust:~/Desktop$ sudo apt install bzip2
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
bzip2 is already the newest version (1.0.8-5build1).
bzip2 set to manually installed.
The following packages were automatically installed and are no longer required:
...
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.


##check version
center@bmw-ntust:~/Desktop$ bzip2 --version
bzip2, a block-sorting file compressor.  Version 1.0.8, 13-Jul-2019.
...
```
7. **Install tar**
```bash
## Install tar
sudo apt-get install tar

##check version
tar --version
```
result:
```bash
## check version
center@bmw-ntust:~/Desktop$ tar --version
tar (GNU tar) 1.34
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

8. **Install vim**
```bash
## Install vim
sudo apt-get install vim

##check version
vim --version
```
result:
```bash
## Install vim
center@bmw-ntust:~$ sudo apt-get install vim
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
vim is already the newest version (2:8.2.3995-1ubuntu2.17).
The following packages were automatically installed and are no longer required:
...
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.

##check version
sionna@bmw-ntust:~/Desktop/ns3/ns-3-dev$ vim --version
VIM - Vi IMproved 8.2 (2019 Dec 12, compiled May 03 2024 02:37:51)
Included patches: 1-579, 1969, 580-1848, 4975, 5016, 5023, 5072, 2068, 1849-1854, 1857, 1855-1857, 1331, 1858, 1858-1859, 1873, 1860-1969, 1992, 1970-1992, 2010, 1993-2068, 2106, 2069-2106, 2108, 2107-2109, 2109-3995, 4563, 4646, 4774, 4895, 4899, 4901, 4919, 213, 1840, 1846-1847, 2110-2112, 2121
...
Linking: gcc -Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -o vim -lm -ltinfo -lselinux -lsodium -lacl -lattr -lgpm -L/usr/lib/python3.10/config-3.10-x86_64-linux-gnu -lpython3.10 -lcrypt -ldl -lm -lm 
```

9. **Install gnuplot tool**
```bash
## Install gnuplot tool
sudo apt-get install gnuplot-x11
```
result:
```bash
## Install gnuplot tool
sionna@bmw-ntust:~$ sudo apt-get install gnuplot-x11
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
gnuplot-x11 is already the newest version (5.4.2+dfsg2-2).
The following packages were automatically installed and are no longer required:
  blender-data fonts-dejavu fonts-dejavu-extra gdal-data libaec0
  libarmadillo10 libarpack2 libavdevice58 libblosc1 libboost-filesystem1.74.0
  libboost-iostreams1.74.0 libboost-locale1.74.0 libboost-thread1.74.0
  libcfitsio9 libcharls2 libdc1394-25 libdcmtk16 libde265-0 libdecor-0-0
  libdecor-0-plugin-1-cairo libembree3-3 libfftw3-double3 libfreexl1 libfyba0
  libgdal30 libgdcm3.0 libgeos-c1v5 libgeos3.10.2 libgeotiff5 libglew2.2
  libhdf4-0-alt libhdf5-103-1 libhdf5-hl-100 libheif1 libilmbase25
  libjemalloc2 libkmlbase1 libkmldom1 libkmlengine1 liblog4cplus-2.0.5
  libminizip1 libmysqlclient21 libnetcdf19 libodbc2 libodbcinst2 libogdi4.1
  libopenal-data libopenal1 libopencolorio1v5 libopencv-core4.5d
  libopencv-imgcodecs4.5d libopencv-imgproc4.5d libopencv-videoio4.5d
  libopenexr25 libopenimageio2.2 libopenvdb8.1 libosdcpu3.4.4 libpq5 libproj22
  libpugixml1v5 libqhull-r8.0 libraw20 librttopo1 libsdl2-2.0-0 libsndio7.0
  libsocket++1 libspatialite7 libspnav0 libsquish0 libsuperlu5 libsz2 libtbb2
  libtbbmalloc2 libtinyxml2.6.2v5 liburiparser1 libxerces-c3.2 libyaml-cpp0.7
  mysql-common proj-bin proj-data unixodbc-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.

```

## How to Download using Git

To download NS-3 using Git, follow these detailed steps:

1. **Open a Terminal**: First, you need to open a terminal window on your Linux or Unix-based system.

2. **Install Git**: If you haven't already installed Git, you can do so by running the following command:
```bash
sudo apt-get install git
```
This command installs Git on Debian-based distributions like Ubuntu. For other distributions, please use the appropriate package manager and command.

3. **Choose a Directory:** Decide on a directory where you want to download NS-3. For example, if you want to download it in your home directory under a folder named ns-3, you can navigate there using:
```bash
cd ~
mkdir ns-3
cd ns-3
```
This creates a new directory named `ns-3` in your home directory and changes the current directory to it.

4. **Clone the NS-3 Repository**: To download NS-3, you need to clone its repository from the official NS-3 GitLab page. As of the last update, the command to clone the latest development version of NS-3 is:
```bash
git clone https://gitlab.com/nsnam/ns-3-dev.git
```
result:
```bash
sionna@bmw-ntust:~/Desktop/ns3$ git clone https://gitlab.com/nsnam/ns-3-dev.git
Cloning into 'ns-3-dev'...
remote: Enumerating objects: 206649, done.
remote: Counting objects: 100% (413/413), done.
remote: Compressing objects: 100% (289/289), done.
remote: Total 206649 (delta 191), reused 134 (delta 124), pack-reused 206236 (from 1)
Receiving objects: 100% (206649/206649), 164.03 MiB | 55.11 MiB/s, done.
Resolving deltas: 100% (173470/173470), done.

If you are content to work with the tip of the development tree; you need only to cd into ns-3-dev; the master branch is checked out by default.
```
This command clones the ns-3-dev repository into a directory named ns-3-dev inside your current directory. If you want to clone a specific version of NS-3, you can check out a tag after cloning. For example, to check out NS-3 version 3.33, you would use:
```bash
cd ns-3-dev
git checkout ns-3.33
```
Replace `ns-3.33 `with the desired version number. You can find the list of available versions by running `git tag`.

## Building and Testing

### Building NS-3

1. **Navigate to the NS-3 Directory**: After downloading NS-3, you need to change into the NS-3 directory (e.g., ns-3-dev if you followed the standard cloning instructions).
```bash
cd ns-3-dev
```

2. **Configure the Build**: Before building NS-3, you must configure the build environment. NS-3 uses a build system called waf, which is a Python-based framework for configuring, compiling, and installing applications. To configure NS-3 with all the default options plus Python bindings (which are highly recommended for a more complete NS-3 experience), run:
```bash
./ns3 configure --enable-examples --enable-tests
```
result:
```bash
sionna@bmw-ntust:~/Desktop/ns3/ns-3-dev$ ./ns3 configure --enable-examples --enable-tests
Warn about uninitialized values.
-- The CXX compiler identification is GNU 11.4.0
-- The C compiler identification is GNU 11.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
...
-- ---- Summary of ns-3 settings:
Build profile                 : default
Build directory               : /home/sionna/Desktop/ns3/ns-3-dev/build
...
Modules configured to be built:
antenna                   aodv                      applications              
bridge                    buildings                 config-store              
...                  

Modules that cannot be built:
brite                     click                     mpi                       
openflow                  visualizer                

-- Configuring done
-- Generating done
-- Build files have been written to: /home/sionna/Desktop/ns3/ns-3-dev/cmake-cache
Finished executing the following commands:
mkdir cmake-cache
/usr/bin/cmake -S /home/sionna/Desktop/ns3/ns-3-dev -B /home/sionna/Desktop/ns3/ns-3-dev/cmake-cache -DCMAKE_BUILD_TYPE=default -DNS3_ASSERT=ON -DNS3_LOG=ON -DNS3_WARNINGS_AS_ERRORS=OFF -DNS3_NATIVE_OPTIMIZATIONS=OFF -DNS3_EXAMPLES=ON -DNS3_TESTS=ON -G Ninja --warn-uninitialized
```
This command configures the build system to include examples and tests in the build process. You can customize the build configuration by adding or removing options based on your requirements.


3. **Build NS-3**: After configuring the build, compile NS-3 by running:
```bash
./ns3 build
```
result:
```bash
sionna@bmw-ntust:~/Desktop/ns3/ns-3-dev$ ./ns3 build
[0/2] Re-checking globbed directories...
[579/1939] Building CXX object src/lr-...plot.dir/lr-wpan-error-model-plot.cc.o^[584/1939] Building CXX object example...-example-sim.dir/wifi-example-sim.cc.o^[1939/1939] Linking CXX executable ../...eless/ns3-dev-wifi-eht-network-default
Finished executing the following commands:
/usr/bin/cmake --build /home/sionna/Desktop/ns3/ns-3-dev/cmake-cache -j 19
```

### Testing NS-3

1. **Run the Test Suite**: NS-3 provides a comprehensive set of tests that can be run to ensure the simulator and its models are functioning as expected. To run the tests, execute:
```bash
./test.py
```
result:
```bash
sionna@bmw-ntust:~/Desktop/ns3/ns-3-dev$ ./test.py
[0/2] Re-checking globbed directories...
ninja: no work to do.
Finished executing the following commands:
/usr/bin/cmake --build /home/sionna/Desktop/ns3/ns-3-dev/cmake-cache -j 19
[0/769] PASS: TestSuite circular-aperture-antenna-test
[1/769] PASS: TestSuite aodv-routing-id-cache
[2/769] PASS: TestSuite buildings-channel-condition-model
[3/769] PASS: TestSuite buildings-penetration-losses
[4/769] PASS: TestSuite isotropic-antenna-model
[5/769] PASS: TestSuite routing-aodv-loopback
[6/769] PASS: TestSuite building-position-allocator
...
[768/769] PASS: Example src/wifi/examples/wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1
769 of 769 tests passed (769 passed, 0 skipped, 0 failed, 0 crashed, 0 valgrind errors)
```
This command runs all available tests and may take some time to complete. You'll see output indicating the progress and results of the tests.

2. **Interpreting Test Results**: The test script outputs the results of each test case. A successful test will typically be marked as PASSED, while a failed test will be marked as FAILED. Review the test output to ensure there are no significant issues. Occasional test failures may occur due to various factors, but consistent or widespread failures require investigation.

3. **Troubleshooting**: If you encounter build errors or test failures, consult the NS-3 documentation and forums for troubleshooting advice. Common issues include missing dependencies, incorrect configuration options, or compatibility problems with specific versions of compilers and libraries.

## Conclusion

Following this guide should help you successfully install NS-3 on your system. Remember to consult the main references for any updates or additional information.


