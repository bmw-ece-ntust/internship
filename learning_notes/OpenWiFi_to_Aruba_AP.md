>Michael Harditya (TEEP)
# Learning Notes
> [!WARNING]
> This note hasn't been tested yet, proceed with caution. Additional notes is going to be added, including backups and troubleshootings.
## Goals
- Make Aruba AP compatible to connect OpenWiFi Controller
## **Table of Contents**
- [**Table of Contents**](#table-of-contents)
- [**Flash Aruba-compatible OpenWrt Firmware**](#flash-aruba-compatible-openwrt-firmware)
    - [**Installation (Flash) Guide for Aruba AP**](#installation-flash-guide-for-aruba-ap)
    - [**Building OpenWiFi AP NOS**](#building-openwifi-ap-nos)

### Flash Aruba-compatible OpenWrt Firmware
[OpenWrt](https://openwrt.org/start) is said to be compatible with OpenWiFi system, which is selected as integration point in this section. By changing the firmware for the access point device, the OpenWiFi Controller can directly acknowledge this device and control the device. OpenWRT itself provide compatible version for Aruba devices, which can be accessed on this [link](https://openwrt.org/supported_devices).
#### Installation (Flash) Guide for Aruba AP
> [!NOTE]
> This section refers to [OpenWrt Installation Guide for Aruba AP-303](https://openwrt.org/toh/aruba/ap-303).

##### Preparing TFTP Server for AP Image
1. Download the OpenWrt ```initramfs``` image, then rename it to ```ipq40xx.ari``` (please refer to OpenWrt guide for the filenames)
2. Place the file into the TFTP server root directory.
3. Configure the TFTP server to be reachable at ```192.168.1.75/24```
4. Connect the machine running the TFTP server to the ethernet port of the access point. In case the usage of DHCP, exact IP is optional and change the step 3 accordingly.

##### Flashing the device
> [!IMPORTANT]
> Up to this point, feel free to back up the current device SPI flash, before continuing to erase the SPI flash. This section doesn't back up the SPI flash.
1. Connect to the serial console of the device (Aruba have special console cable and can be connected to an UART-Adapter)
2. Interrupt autobooting by pressing 'Enter' when prompted.
3. configure the ```bootargs``` and ```bootcmd``` for OpenWrt using this commands:
```shell
   $ setenv bootargs_openwrt "setenv bootargs console=ttyMSM1,9600n8"
   $ setenv nandboot_openwrt "run bootargs_openwrt; ubi part aos1; ubi read 0x85000000 kernel; set fdt_high 0x87000000; bootm 0x85000000"
   # Substitute the following IP-addresses as mentioned Step 1 and 2, in case, you are using DHCP.
   $ setenv ramboot_openwrt "run bootargs_openwrt; setenv ipaddr 192.168.1.105; setenv serverip 192.168.1.75; netget; set fdt_high 0x87000000; bootm" 
   $ setenv bootcmd "run nandboot_openwrt"
   $ saveenv
```
4. Load the OpenWrt into RAM
```shell
$ run ramboot_openwrt
```
> [!NOTE]
> After TFTP transfer completes, there will be an error displayed: "Invalid image format version", it can be ignored.
5. After booted, transfer the OpenWrt ```sysupgrade``` image to the ```/tmp``` folder on the device.
6. Flash OpenWrt
```shell
$ ubidetach -p /dev/mtd1
$ ubiformat /dev/mtd1
$ sysupgrade -n /tmp/openwrt-sysupgrade.bin
```
> [!TIP]
> In case using DHCP, in the console of OpenWrt change ```option proto 'static``` to ```option proto 'dhcp``` for the LAN interface using:
 ```shell
 $ vi /etc/config/network
# Then reload and connect. 
$ service network reload
 ```

 #### Building OpenWiFi AP NOS
 OpenWiFi AP NOS is OpenWrt-based Access Point Network Operating System (NOS) for TIP OpenWiFi. It requires to build it first from the [OpenWiFi AP NOS GitHub repository](https://github.com/Telecominfraproject/wlan-ap).

Building requires a recent Linux installation and Python 3.7, see [OpenWrt Beginners Build Guide](https://openwrt.org/docs/guide-developer/toolchain/beginners-build-guide).

1. Install necessary build packages, for example on Debian/Ubuntu:
```sh
sudo apt install build-essential libncurses5-dev gawk git libssl-dev gettext zlib1g-dev swig unzip time rsync python3 python3-setuptools python3-yaml
```
2. Clone the [OpenWiFi AP NOS repository](https://github.com/Telecominfraproject/wlan-ap.git):
```sh
git clone https://github.com/Telecominfraproject/wlan-ap.git
```
3. Set up the tree using the ```setup.py```, it will create an ```openwrt/``` directory.
```sh
./setup.py --setup    # for subsequent builds, use --rebase instead
```
4. Select the profile and base package selection, this setop will install the feeds and packages and generate the ```.config``` file.
```sh
cd openwrt
./scripts/gen_config.py linksys_ea8300
```
5. Build the tree (replace ```-j 8``` with the number of cores to use).
```sh
make -j V=s
```

The output of the build are located in the ```openwrt/bin/``` directory:

| Type             | Path                                                 |
| ---------------- | ---------------------------------------------------- |
| Firmware images  | `openwrt/bin/targets/<target>/<subtarget>/`          |
| Kernel modules   | `openwrt/bin/targets/<target>/<subtarget>/packages/` |
| Package binaries | `openwrt/bin/packages/<platform>/<feed>/`            |

### OpenWiFi AP Compatibility List
[To be Updated]

###
