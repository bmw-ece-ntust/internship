# srsRAN


## Brief Information About srsRAN

The **srsRAN** software suite is an open-source collection of 4G and 5G software radio implementations from SRS. It includes applications implemented in portable C++ with minimal third-party dependencies. The software runs on Linux with off-the-shelf compute and radio hardware.

The **srsRAN Project** is an open-source 5G CU/DU from SRS. It is a complete RAN solution compliant with 3GPP and O-RAN Alliance specifications. The project includes the full L1/2/3 stack with minimal external dependencies. It also supports O-RAN CU/DU architectures and cloudRAN deployments.


## Installation Guide

In order to build the srsRAN project in Ubuntu, there are 4 steps to be done
1. Install Dependencies
2. Install RF Driver
3. Clone srsRAN Repository
4. Build the Codebase


## Build Tools and Dependencies

The implementation of srsRAN are build on C language so it is recommend to install build tools such as CMake and GCC

* [cmake](https://cmake.org/)
    ```
    sudo apt-get -y install cmake
    ```

* [gcc](https://gcc.gnu.org/install/)
    ```
    sudo apt install build-essential
    ```

The srsRAN Project has the following necessary dependencies

* [libfftw](https://www.fftw.org/) , [libsctp](https://github.com/sctp/lksctp-tools) , [yaml-cpp](https://github.com/jbeder/yaml-cpp) , [PolarSSL/mbedTLS](https://www.trustedfirmware.org/projects/mbed-tls/) , [googletest](https://github.com/google/googletest/)

    ```
    sudo apt-get install cmake make gcc g++ pkg-config libfftw3-dev libmbedtls-dev libsctp-dev libyaml-cpp-dev libgtest-dev
    ```


## RF Driver
The srsRAN Projects uses RF Drivers and currently only USRP Hardware Driver (UHD) that support

* [UHD](https://files.ettus.com/manual/page_install.html)
    ```
    sudo apt-get install libuhd-dev uhd-host
    ```


## Repository Clone
Clone srsRAN repository by running the following code in Ubuntu
```
git clone https://github.com/srsRAN/srsRAN_Project.git
```


## Build Codebase
```
cd srsRAN_Project
mkdir build
cd build
cmake ../
make -j $(nproc)
make test -j $(nproc)
```

![image](https://hackmd.io/_uploads/Sy9Ow07Kp.png)

After build the codebase by running the code, now gNB can be runned from the address `srsRAN_Project/build/apps/gnb/` or use the following syntax to install the srsRAN Project gNB
```
sudo make install
```

---
## Source
* [srsRAN documentation](https://docs.srsran.com/projects/project/en/latest/user_manuals/source/installation.html)

