# Scapy Attack Tools

![Scapy_logo](/assets/scapy/Scapy_logo.png)


> **References:**
> - [Create Packets from Scratch with Scapy [Tutorial]](https://www.youtube.com/watch?v=yD8qrP8sCDs)
> - [Implementation of S Plane DoS Attacker based on tcpreplay and DPDK-burst-replay](https://hackmd.io/@rico-hung/HJESocHl2?type=view)
> - [Scapy Official Website](https://scapy.net/)

## 1. What is Scapy?
Scapy is a powerful interactive packet manipulation library written in Python. Scapy is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more.

Scapy runs natively on Linux, macOS, most Unixes, and on Windows with Npcap.

## 2. Installing Scapy
```python
pip install scapy
```
After installation, you can check whether scapy is installed on your machine using this command:
```python
sudo scapy
```
![Screenshot 2024-07-09 105801](/assets/scapy/Screenshot%202024-07-09%20105801.png)

## 3. Testing Scapy Commands
This command will try to send a TCP packet to destination IP of 192.168.1.121 (Target), from a source address 192.168.1.69 (Fake Address). The mac address is intentionally spoofed (fake) in this example in order to hide the actual address which this rogue packet is sent from. Lastly this packet will be sent 20000 times.
```python
sendp(Ether(src="aa:bb:cc:dd:ee:ff")/IP(src="192.168.1.69", dst="192.168.1.121")/TCP(sport=443,dport=22), count=20000)
```
![scapy_test_1](/assets/scapy/scapy_test_1.jpg)

## 4. Testing Scapy with Script
```python
from scapy.all import *

dest_ip = "192.168.56.1"
dest_mac = "0A:00:27:00:00:17"
count = 20

class eCPRI(Packet):
    name = "eCPRI"
    fields_desc = [
        ByteField("msg_type", 0),
        ByteField("payload_size", 0),
        IntField("ecpri_pc_id", 0),
        ByteField("ecpri_seq_id", 0),
        StrField("ecpri_payload", "")
    ]

def main():
    # Create an IP packet with the destination IP address specified by dest_ip
    ecpri_packet = IP(dst=dest_ip) / ICMP()

    # Display the details of the created packet
    ecpri_packet.show()

    # Send the created packet 'count' number of times
    send(ecpri_packet, count=count)

if __name__ == "__main__":
    main()
```
![Screenshot 2024-07-09 110959](/assets/scapy/Screenshot%202024-07-09%20110959.png)

## Result 09/07/2024
![wireshark_script](/assets/scapy/wireshark_script.png)

## 5. Scapy Script to Send eCPRI U-Plane Packets
```python
from scapy.all import *

src_ip = "192.168.1.69"
dest_ip = "192.168.56.1"
src_mac = "32:43:c7:8d:59:5c"
dest_mac = "0A:00:27:00:00:17"
iface = "enp0s3"
count = 20

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
        C=0, 
        messageType=0x00, 
        payloadSize=1024
    )

    # Define the payload
    payload = b"Hello World"

    # Create the complete packet with Ethernet header
    ether = Ether(dst=dest_mac, type=0xAEFE)

    # Assemble the complete packet structure
    packet = ether / ecpri_packet / payload

    # Display the packet structure
    packet.show()

    # Send the packet using Scapy's sendp function
    sendp(packet, iface=iface, count=count)

if __name__ == "__main__":
    main()
```
![ecpri_packets](/assets/scapy/ecpri_packets.png)

## Result 11/07/2024
![oran_fh_u_wireshark](/assets/scapy/oran_fh_u_wireshark.png)