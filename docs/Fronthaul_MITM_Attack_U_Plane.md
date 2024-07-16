# Fronthaul MITM Attack over U-Plane (T-UPLANE-01)

## 1. Determine which interface should be used

![interfaces](/assets/fronthaul_mitm/interfaces.png)

**There are 4 interfaces in my local vm, enp0s9 and enp0s10 will be used for DPDK.**

## 2. Setup DPDK compatible interface

#### 2.1 Before an interface can be configured as DPDK compatible driver, you need to turn the interface off first.

```bash
sudo -i
ifconfig enp0s9 down
ifconfig enp0s10 down
```

#### 2.2 Next, bind the interface as uio_pci_generic

```bash
modprobe uio
modprobe uio_pci_generic
dpdk-devbind.py -b uio_pci_generic 00:09.0
dpdk-devbind.py -b uio_pci_generic 00:0a.0
```

#### 2.3 Check whether the binding is successfull

```bash
exit
dpdk-devbind.py -s
```

#### 2.4 Example:

![devbind](/assets/fronthaul_mitm/devbind.png)

#### 2.5 Next, go to dpdk build examples directory

```bash
cd dpdk-stable-23.11.1/build/examples/
```

#### 2.6 Run hugepages

```bash
sudo -i
mkdir -p /dev/hugepages
mountpoint -q /dev/hugepages || mount -t hugetlbfs nodev /dev/hugepages
echo 64 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
exit
```

#### 2.7 Run the l2fwd for layer 2 traffic forwarding in DPDK

```bash
sudo ./dpdk-l2fwd -l 0-1 -n 2 -- -p 0x3
```

| Argument | Description                                                                               |
| -------- | ----------------------------------------------------------------------------------------- |
| -l 0-1   | Use logical cores 0 to 1                                                                  |
| -n 2     | Use 2 memory channels                                                                     |
| - -      | Separator between EAL (Environment Abstraction Layer) arguments and application arguments |
| -p 0x3   | Use ports 0 and 1 (bitmask 0x3)                                                           |
| -q 1     | Use 1 queue per port                                                                      |

#### Result

![ports](/assets/fronthaul_mitm/ports.png)

## 3. Sniffing and Analyzing the Traffic

#### 3.1 Using tcpdump

```bash
sudo tcpdump -i enp0s8 -e ether proto 0x8863 or ether proto 0x8864
```

| Argument           | Description                                |
| ------------------ | ------------------------------------------ |
| -i                 | Send the packet using which interface      |
| -e                 | Use layer 2 to send the packet             |
| ether proto 0x8863 | Filter for Protocol: PPPoE Discovery Stage |
| ether proto 0x8864 | Filter for Protocol: PPPoE Session Stage   |

#### Result

![tcpdump](/assets/fronthaul_mitm/tcpdump.png)
