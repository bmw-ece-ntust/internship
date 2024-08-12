from scapy.all import Ether, sendp, bind_layers, BitField, ByteField, ShortField, Packet

src_ip = "192.168.1.69"
dest_ip = "192.168.13.4"
src_mac = "aa:bb:cc:dd:ee:ff"
dest_mac = "68:05:CA:82:E4:45"
#dest_mac = "08:00:27:3D:B9:0F"

iface = "Ethernet 5"
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

if __name__ == "__main__":
    main()