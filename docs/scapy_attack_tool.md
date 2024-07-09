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
scapy
```
![Screenshot 2024-07-09 105801](/assets/scapy/Screenshot%202024-07-09%20105801.png)

## 3. Testing Scapy Commands
This command will try to send a TCP packet to destination IP of 192.168.1.121 (Target), from a source address 192.168.1.69 (Fake Address). The mac address is intentionally spoofed (fake) in this example in order to hide the actual address which this rogue packet is sent from. Lastly this packet will be sent 20000 times.
```python
sendp(Ether(src="aa:bb:cc:dd:ee:ff")/IP(src="192.168.1.69", dst="192.168.1.121")/TCP(sport=443,dport=22), count=20000)
```
![scapy_test_1](/assets/scapy/scapy_test_1.jpg)

## 4. Testing Scapy with Script
```python=
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

## Result
![wireshark_script](/assets/scapy/wireshark_script.png)