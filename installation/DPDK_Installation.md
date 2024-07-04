# 2. | DPDK (Data Plane Development Kit) Installation

> **References :**
> [DPDK Quick Start Guide](https://core.dpdk.org/doc/quick-start)
> [DPDK Installation Guide Video](https://www.youtube.com/watch?v=0yDdMWQPCOI)
> [Fateen Najib (TEEP 2023) Notes](https://hackmd.io/@kIdpcHY-TN2HXF-K3mKuLQ/BJ2szv_4h)

### Hardware Specifications

| Hardware | Specification             |
| -------- | ------------------------- |
| CPU      | AMD Ryzen 4800H @ 2.90GHz |
| Cores    | 4                         |
| RAM      | 4 GB                      |
| Storage  | 50 GB SSD                 |

### Software Specifications

| Software | Version          |
| -------- | ---------------- |
| OS       | Ubuntu 20.04 LTS |
| DPDK     | 23.11.1 (LTS)    |

### 2.1 | Download DPDK using terminal

```bash
wget https://fast.dpdk.org/rel/dpdk-23.11.1.tar.xz
```

### 2.2 | Extract the downloaded file

```bash
tar xf dpdk-23.11.1.tar.xz
```

### 2.3 | Install the dependencies

```bash
sudo apt install build-essential meson python3-pyelftools libnuma-dev pkgconf
```

![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140513.png)

### 2.4 | Go to DPDK directory

```bash
cd dpdk-stable-23.11.1/
```

### 2.5 | Build all examples using meson and ninja

```bash
meson -Dexamples=all build
ninja -C build
```

![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140407.png)
![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140257.png)
![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140224.png)

### 2.6 | Go to build directory and install it

```bash
cd build
sudo ninja install
sudo ldconfig
```

### 2.7 | Check which port are currently active

```bash
sudo -i
dpdk-devbind.py -s
```

![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140141.png)

### 2.8 | Bind the port to DPDK by turning off the port first

```bash
ifconfig enp0s8 down
modprobe uio
modprobe uio_pci_generic
dpdk-devbind.py -b uio_pci_generic 00:08.0
```

![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140115.png)
![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140054.png)

### 2.9 | Check the port status

```bash
exit
dpdk-devbind.py -s
```

### 2.10 | Go back to build/examples directory

```bash
cd dpdk-stable-23.11.1/build/examples/
```

### 2.11 | Run hugepages

```bash
sudo -i
mkdir -p /dev/hugepages
mountpoint -q /dev/hugepages || mount -t hugetlbfs nodev /dev/hugepages
echo 64 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
```

### 2.12 | Run the helloworld example

```bash
sudo ./dpdk-helloworld -l 0-1 -n 2
```

## Result

![install the dependencies](../assets/DPDK_Installation/Screenshot%202024-07-03%20140020.png)
