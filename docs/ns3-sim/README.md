# NS-3 : Network Simulator 3

![](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-18-Rafli/assets/ns-3-logo.png)

NS-3 a discrete-event simulator typically run from the command line. It is written directly in C++, not in a high-level modeling language; simulation events are simply C++ function calls, organized by a scheduler.

## NS-3 Installation

1. Download NS-3 Latest Release

    Download the latest release as a source code archive from the main ns-3 web site.
    - Download the tar file from the official image
        ```bash
        wget vhttps://www.nsnam.org/releases/ns-allinone-3.41.tar.bz2
        ```
    - Unpack it in a working directory of your choice
        ```bash
        tar xjf ns-allinone-3.41.tar.bz2
        ```
    - Change into the ns-3 directory
        ```bash
        cd ns-allinone-3.41/ns-3.41
        ```
2. Building and testing NS-3

    The next step is to configure the build using the CMake build system. The below commands make use of a Python wrapper around CMake, called ns3, that simplifies the command-line syntax, resembling Waf syntax.
    - First to do default build profile 
        ```bash
        ./ns3 configure --enable-examples --enable-tests
        ```
    - Then, use ns3 to build ns-3
        ```bash
        ./ns3 build
        ```
    - Once complete, you can run the unit tests to check your build
        ```bash
        ./test.py
        ```
     To run the first tutorial program, whose source code is located at examples/tutorial/first.cc, use ns3 to run it.
    - Run example script
        ```bash
        ./ns3 run first
        ```
    - To view possible command-line options, specify the `–PrintHelp` argument:
        ```bash
        ./ns3 run 'first --PrintHelp'
        ```
## Reference

> https://www.nsnam.org/docs/release/3.41/tutorial/singlehtml/index.html