from scapy.all import Ether, sendp, bind_layers, BitField, ShortField, LongField, Packet, IntField, XShortField, Field, LenField, ByteField, XLongField, SignedByteField, XByteField, StrFixedLenField
import random
import math
import time
src_mac = "aa:bb:cc:dd:ee:ff"
dest_mac = "11:22:33:44:55:66"
iface = "Ethernet 5"
count = 8
ptp_ethertype = 0x88F7

# Define PTP message types
PTP_ANNOUNCE = 0xB
PTP_SYNC = 0x0
PTP_FOLLOW_UP = 0x8
PTP_DELAY_REQ = 0x1
PTP_DELAY_RESP = 0x9

class PTPHeader(Packet):
    name = "PTP Header"
    fields_desc = [
        XByteField("transport_specific_message_type", 0x00),
        ByteField("reserved1", 0x00),
        ShortField("reserved2", 0x0000),
        StrFixedLenField("reserved3", b'\x00'*8, 8),
        StrFixedLenField("source_port_identity", b'\x00'*10, 10),
        ShortField("sequence_id", 0x0000),
        ByteField("control", 0x00),
        ByteField("log_message_interval", 0x7F)
    ]

def create_ptp_packet(ptp_type):
    eth = Ether(src=src_mac, dst=dest_mac, type=ptp_ethertype)
    ptp = PTPHeader(transport_specific_message_type=ptp_type)
    packet = eth / ptp
    return packet

if __name__ == "__main__":
    # Create and send Announce packets  
    announce_packet = create_ptp_packet(PTP_ANNOUNCE)
    sendp(announce_packet, iface=iface, count=count)
    print("Sent Announce messages")

    # Create and send Sync packets
    sync_packet = create_ptp_packet(PTP_SYNC)
    sendp(sync_packet, iface=iface, count=count)
    print("Sent Sync messages")

    # Create and send Follow_Up packets
    follow_up_packet = create_ptp_packet(PTP_FOLLOW_UP)
    sendp(follow_up_packet, iface=iface, count=count)
    print("Sent Follow_Up messages")

    # Create and send Delay_Req packets
    delay_req_packet = create_ptp_packet(PTP_DELAY_REQ)
    sendp(delay_req_packet, iface=iface, count=count)
    print("Sent Delay_Req messages")

    # Create and send Delay_Resp packets
    delay_resp_packet = create_ptp_packet(PTP_DELAY_RESP)
    sendp(delay_resp_packet, iface=iface, count=count)
    print("Sent Delay_Resp messages")