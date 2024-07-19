# DPDK-l2fwd Test in Attacker Server

> .
> **References:**
> [DPDK-l2fwd official documentation](https://doc.dpdk.org/guides/sample_app_ug/l2_forward_real_virtual.html)
> .

## 1. Testing Topology
![Testing_Topology](https://hackmd.io/_uploads/HJ2K888_0.png)

This is our testing topology. Rayhan's laptop is connected to port **ens1f0**, and Eriqo's laptop is connected to port **ens1f1**. The attacker server is connected to both laptops. The attacker server is running DPDK-l2fwd application to forward packets from Rayhan's laptop to Eriqo's laptop. The **expected result** is that the eCPRI malformed **packets sent from Eriqo's laptop will be forwarded to Rayhan's laptop.**

## 2. Testing setup
#### 2.1. Connect two laptops to the attacker server
![WhatsApp Image 2024-07-18 at 16.52.02](https://hackmd.io/_uploads/H1N1_UId0.jpg)

#### 2.2. Bind the interface using DPDK-compatible driver
```bash
dpdk-devbind.py -b igb_uio 02:00.0
dpdk-devbind.py -b igb_uio 02:00.1
```
![image](https://hackmd.io/_uploads/SkuYOIIdR.png)

Here we are using igb_uio interface for maximum performance (Port 0 & Port 1)

#### 2.3. Run DPDK-l2fwd application using port 0 & port 1
```bash
sudo ./dpdk-l2fwd -l 0-3 -n 4 -- -p 0x3 -P
```
![image](https://hackmd.io/_uploads/B1wVFII_A.png)

#### 2.4. Create a scapy script that will launch eCPRI malformed packets
```python
from scapy.all import Ether, sendp, bind_layers, BitField, ByteField, ShortField, Packet

src_ip = "192.168.1.69"
dest_ip = "192.168.56.1"
src_mac = "aa:bb:cc:dd:ee:ff"
dest_mac = "68:05:CA:82:E4:45"
iface = "Ethernet"
count = 200

class eCPRI(Packet):
    name = "eCPRI"
    fields_desc = [
        BitField("protocolRevision", 0, 4),
        BitField("reserved", 0, 3),
        BitField("C", 0, 1),
        ByteField("messageType", 0),
        ShortField("payloadSize", 0)
    ]

def main():
    # Bind eCPRI protocol to Ethernet with a specific EtherType (0xAEFE)
    bind_layers(Ether, eCPRI, type=0xAEFE)

    # Create an instance of the eCPRI packet
    ecpri_packet = eCPRI(
        protocolRevision=0x01, 
        reserved=0b000, 
        C=1, 
        messageType=0x00, 
        payloadSize=1024
    )

    # Define the payload
    payload = b"Hello World"

    # Create the complete packet with Ethernet header
    ether = Ether(dst=dest_mac, src=src_mac, type=0xAEFE)

    # Assemble the complete packet structure
    packet = ether / ecpri_packet / payload

    # Display the packet structure
    packet.show()

    # Send the packet using Scapy's sendp function
    sendp(packet, iface=iface, count=count)

if _name_ == "_main_":
    main()
```
#### 2.5. Run the scapy script and monitor the interface using Wireshark
![image](https://hackmd.io/_uploads/Syun5qDO0.png)

## 3. Result

#### 3.1. Before enabling l2fwd
![image](https://hackmd.io/_uploads/SJV2HL8dC.png)
No eCPRI packet forwarded to port ens1f0

#### 3.2. After enabling l2fwd
![image](https://hackmd.io/_uploads/H11kA8L_A.png)
eCPRU Malformed Packet attack using Scapy from Eriqo's Laptop is forwarded to port ens1f0. Hence, the DPDK-l2fwd is **running successfully**