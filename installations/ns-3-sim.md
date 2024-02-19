# NS-3 Simulator Installation Guide

## Overview
{to be written soon}

## 1. Updating all packages and installing dependencies:
Input:
```
sudo apt update
sudo apt install g++ python3 cmake ninja-build git gir1.2-goocanvas-2.0 python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3 tcpdump wireshark sqlite sqlite3 libsqlite3-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools openmpi-bin openmpi-common openmpi-doc libopenmpi-dev doxygen graphviz imagemagick python3-sphinx dia imagemagick texlive dvipng latexmk texlive-extra-utils texlive-latex-extra texlive-font-utils libeigen3-dev gsl-bin libgsl-dev libgslcblas0 libxml2 libxml2-dev libgtk-3-dev lxc-utils lxc-templates vtun uml-utilities ebtables bridge-utils libxml2 libxml2-dev libboost-all-dev ccache
```
Output:
{to be written}

## 2. Downloading and extracting the NS-3 Simulator File:
First, download the ns-allinone-3.40.tar.bz2 file from NS-3 Simulator Website. Go back to the terminal afterwards.
Input:
```
tar -xvf ns-allinone-3.40.tar.bz2
```
Output:
{to be written}

## 3. Installing all NS-3 Simulator packages:
Input:
```
./build.py --enable-examples --enable-tests
```
Output:
{to be written}

## 4. Testing the NS-3 Simulator itself after the installation:
Input:
```
## testing the simulator with Hello Simulator
./ns3 run hello-simulator

## testing the simulator by reading server and client packages
./ns3 run first.cc
```
Output:
{to be written}
