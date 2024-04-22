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
In order to compile and build the O-DU HIGH, CU STUB, and RIC STUB Navigate to `ODUI2/l2/build/odu` and then run the following code
* O-DU HIGH
    * Clean O-DU High Binary
        ```
        make clean_odu MACHINE=BIT64 MODE=FDD
        ```
        ![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Clean%20O-DU%20High%20binary.png)
    
    * Compile O-DU High Binary
        ```
        make odu MACHINE=BIT64 MODE=FDD
        ```
        ![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Compile%20O-DU%20HIGH%20BInary.png)
* CU STUB
    * Clean CU STUB Binary
        ```
        mmake clean_cu NODE=TEST_STUB MACHINE=BIT64 MODE=FDD
        ```
        ![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Clean%20CU%20Stub%20Binary.png)
    
    * Compile CU STUB Binary
        ```
        make cu_stub NODE=TEST_STUB MACHINE=BIT64 MODE=FDD
        ```
        ![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Build%20CU%20Stub%20BInary.png)
* RIC STUB
    * Clean RIC STUB Binary
        ```
        make clean_ric NODE=TEST_STUB MACHINE=BIT64 MODE=FDD
        ```
        ![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Clean%20RIC%20Stub%20Binary.png)
    
    * Compile RIC Stub Binary
        ```
        make ric_stub NODE=TEST_STUB MACHINE=BIT64 MODE=FDD
        ```
        ![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-24-Reyhan/Images/Compile%20RIC%20Stub%20Binary.png)

---
## Source
* [O-DU High Installation Guide](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/installation-guide.html#compilation)
* [Keysight](https://www.keysight.com/us/en/assets/7121-1103/ebooks/The-Essential-Guide-for-Understanding-O-RAN.pdf)
* [OSC Wiki](https://wiki.o-ran-sc.org/)


