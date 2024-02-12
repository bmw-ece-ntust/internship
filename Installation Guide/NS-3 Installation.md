# NS-3 Simulator
![image](https://www.nsnam.org/assets/img/ns-3-notext.png)

## Brief Information About NS-3 Simulator

NS-3 is a discrete-event network simulator primarily aimed at research and educational use. NS-3 is free software, licensed under the GNU GPLv2 license, and is publicly available for research, development, and use.

> The goal of the NS-3 project is to develop a free and open-source simulation environment suitable for network research: it should align with the requirements of modern network research simulation and should encourage community contributions, peer review, and software validation.

NS-3 supports research on both IP-based and non-IP networks. However, the majority of its users focus on wireless/IP simulations involving models for Wi-Fi, LTE, or other wireless systems for layers 1 and 2. NS-3 also supports a real-time scheduler that facilitates a number of “simulation-in-loop” use cases to interact with real systems. For example, users can send and receive NS-3 generated packets on real network devices, and NS-3 can serve as an interconnection framework to add link effects between virtual machines.

One emphasis of the simulator is on the reuse of real application and kernel code. The Direct Code Execution framework allows users to run C or C++ based applications or Linux kernel network stacks in NS-3.


## Installation Guide

In order to install NS-3 (NS-3 Simulator in Ubuntu, there are 5 steps to be done
1. Have at least Ubuntu 22.04 Version
2. Install Dependencies
3. Download the [NS-3](https://www.nsnam.org/releases/ns-3-40/) File
4. Extract the NS-3 File
5. Install all packages for NS-3


## Update Ubuntu
In order to install NS-3 Version 3.40 you need to have at least Ubuntu 22.04 to install all the dependencies
```
sudo apt update
```
![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Update%20Ubuntu%20NS3.jpg)


## Install Dependencies
```
sudo apt install g++ python3 cmake ninja-build git gir1.2-goocanvas-2.0 python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3 tcpdump wireshark sqlite sqlite3 libsqlite3-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools openmpi-bin openmpi-common openmpi-doc libopenmpi-dev doxygen graphviz imagemagick python3-sphinx dia imagemagick texlive dvipng latexmk texlive-extra-utils texlive-latex-extra texlive-font-utils libeigen3-dev gsl-bin libgsl-dev libgslcblas0 libxml2 libxml2-dev libgtk-3-dev lxc-utils lxc-templates vtun uml-utilities ebtables bridge-utils libxml2 libxml2-dev libboost-all-dev ccache
```
![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Install%20Dependencies%20NS3.jpg)


## Extract the NS-3 File
Move towards the Root of ns-allinone-3.40.tar.bz2 and extract the file
```
tar -xvf ns-allinone-3.40.tar.bz2
```

## Install all packages for NS-3
Move towards the ns-allinone-3.40 folder and install all the packages
```
./build.py --enable-examples --enable-tests
```
![image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Install%20NS3%20Packages.jpg)

## Testing The NS-3 Simulator
In order to test the NS-3 Simulator we can run Hello Simulator or read server and client packages by moving towards the ns-3.40 folder inside the ns-allinone-3.40 folder and then run the following command
* Hello Simulator
    ```
    ./ns3 run hello-simulator
    ```
* Read Server-Client Packages
    ```
    ./ns3 run first.cc
    ```
![Image](https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-24-Reyhan/Images/Testing%20NS3.jpg)

---
## Source
* [NS-3 Website](https://www.nsnam.org/)
* [About NS-3](https://www.nsnam.org/about/what-is-ns-3/)
* [NS Simulator](https://en.wikipedia.org/wiki/Ns_(simulator))

