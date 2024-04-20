# OSC O-DU HIGH I2

### Brief Information O-DU
O-DU are parts of the O-RAN architecture that focus on network processing and control.

O-DU High is part of the Distributed Unit (DU) responsible for functions that require real-time such as encoding and parsing data. It includes functions such as radio link control, medium access control, and the top of the physical layer.

OSC O-DU is an open-source implementation of O-DU developed by the Open Source Community (OSC). OSC O-DU is designed to interoperate with O-CU from OpenAirInterface (OAI) and O-DU High. The goal is to enable a reference design of the RAN stack according to the O-RAN architecture in two communities, OSC and OAI.


## Installation Guide
#### Hardware Used to Install O-DU High:
| Hardware     | Aspects |
| ------------ | ------- |
| Series| MSI GF63 Thin 10SCSR |
| CPU          | i5 - 10200H @ 2.40 GHz (4 Cores 8 Processor)        |
| RAM          | 16 GB   |
| DISK         | 500 GB  |


#### Software:
| Item          | Info                                                              |
| ------------- | ----------------------------------------------------------------- |
| OS            | Ubuntu 22.04.4 LTS |
| Kernel        | 6.5.0-27-generic|
| OSC DU Branch | i-release |




### Libraries
In order to build the OSC O-DU High I2 in Ubuntu, Following libraries are required to compile and execute O-DU High:

* [gcc](https://gcc.gnu.org/install/)
    ```
    sudo apt install build-essential
    ```
* LKSCTP
    ```
    sudo apt-get install -y libsctp-dev
    ```
* PCAP
    ```
    sudo apt-get install -y libpcap-dev
    ```
* libxml2
    ```
    sudo apt-get install -y libxml2-dev
    ```

![image](https://hackmd.io/_uploads/rkU0ryB2p.png)

### Repository Clone
Create a folder to clone the O-DU High code into, mine use "ODUI2", then locate to the folder and clone the  repository of O-DU I2 to local folder
```
git clone https://gerrit.o-ran-sc.org/r/o-du/l2
```
![image](https://hackmd.io/_uploads/SJcz8krhp.png)

### Compilation
In order to compile and build the OSC O-DU High I2 Navigate to `ODUI2/l2/build/odu` and then run the following code
* Clean O-DU High binary
    ```
    make clean_odu MACHINE=BIT64 MODE=FDD
    ```
    ![image](https://hackmd.io/_uploads/HkV7DJH3T.png)

* Compile O-DU High binary
    ```
    make odu MACHINE=BIT64 MODE=FDD
    ```
    ![image](https://hackmd.io/_uploads/r1IRD1H2p.png)

    Still encounter problem to compile the du_sys_info_hdl.c file due to error, if the compilation succes the final message should be
    ![image](https://hackmd.io/_uploads/ByWA_1B2p.png)


    **Error Message**
    ```
    ‘PLMN_IdentitY_t’ undeclared (first use in this function); did you mean ‘PLMN_Identity_t’?
    ```


---
## Source
* [O-DU High Installation Guide](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/installation-guide.html#compilation)
* [Keysight](https://www.keysight.com/us/en/assets/7121-1103/ebooks/The-Essential-Guide-for-Understanding-O-RAN.pdf)
* [OSC Wiki](https://wiki.o-ran-sc.org/)


