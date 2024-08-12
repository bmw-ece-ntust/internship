from scapy.all import Ether, sendp, bind_layers, BitField, ShortField, LongField, Packet, IntField, XShortField
from scapy.fields import Field, LenField, ByteField, XLongField, SignedByteField
import random
import math
import time
src_mac = "aa:bb:cc:dd:ee:ff"
dest_mac = "11:22:33:44:55:66"
iface = "Ethernet 5"
count = 10
ptp_ethertype = 0x88F7

# Define PTP message types
PTP_ANNOUNCE = 0b1011
PTP_SYNC = 0b0000
PTP_FOLLOW_UP = 0b1000
PTP_DELAY_REQ = 0b0001
PTP_DELAY_RESP = 0b1001

class PTPHeader(Packet):
    name = "PTP Header"
    fields_desc = [
        BitField('transportSpecific', 1, 4),
        BitField('messageType', 0x0, 4),
        ByteField('versionPTP', 2),
        LenField('messageLength', 0, fmt="H"),
        ByteField('subdomainNumber', 0),
        ByteField('dummy1', 0),
        XShortField('flags', 0),
        LongField('correction', 0),
        IntField('dummy2', 0),
        XLongField('ClockIdentity', 0),
        XShortField('SourcePortId', 0),
        XShortField('sequenceId', 0),
        ByteField('control', 0),
        SignedByteField('logMessagePeriod', 0)
    ]

class announce_message(Packet):
    name = "announce message"
    fields_desc = [
        Field('TimestampSec', 0, fmt='6s'),
        IntField('TimestampNanoSec', 0),
        XShortField('currentUtcOffset', 0),
        ByteField('reserved', 0),
        ByteField('grandmasterPriority1', 0),
        IntField('grandmasterClockQuality', 0),
        ByteField('grandmasterPriority2', 0),
        LongField('grandmasterIdentity', 0),
        XShortField('stepsRemoved', 0),
        ByteField('timeSource', 0)
    ]
    def extract_padding(self, p):
        return "", p


class sync_message(Packet):
    name = "sync message"
    fields_desc = [
        Field('TimestampSec', 0, fmt='6s'),
        IntField('TimestampNanoSec', 0)
    ]
    def extract_padding(self, p):
        return "", p

class delay_resp_message(Packet):
    name = "delay response message"
    fields_desc = [
        Field('TimestampSec', 0, fmt='6s'),
        IntField('TimestampNanoSec', 0)
    ]
    def extract_padding(self, p):
        return "", p
    

def create_ptp_packet(ptp_type):
    eth = Ether(src=src_mac, dst=dest_mac, type=ptp_ethertype)
    ptp = PTPHeader(transport_specific_message_type=ptp_type)
    
    if ptp_type in [PTP_SYNC, PTP_DELAY_REQ]:
        # Add OriginTimestamp field for Sync and Delay Request messages
        timestamp = PTPOriginTimestamp(seconds_field=0x1234567890ABCDEF, nanoseconds_field=0x12345678)
        packet = eth / ptp / timestamp
    else:
        packet = eth / ptp

    return packet

if __name__ == "__main__":
    # Create and send Sync packets
    sync_packet = create_ptp_packet(PTP_SYNC)
    sendp(sync_packet, iface=iface, count=count)
    print("Sent Sync messages")

    # Create and send Delay_Req packets
    delay_req_packet = create_ptp_packet(PTP_DELAY_REQ)
    sendp(delay_req_packet, iface=iface, count=count)
    print("Sent Delay_Req messages")

    # Create and send Announce packets
    announce_packet = create_ptp_packet(PTP_ANNOUNCE)
    sendp(announce_packet, iface=iface, count=count)
    print("Sent Announce messages")

    # Create and send Follow_Up packets
    follow_up_packet = create_ptp_packet(PTP_FOLLOW_UP)
    sendp(follow_up_packet, iface=iface, count=count)
    print("Sent Follow_Up messages")

    # Create and send Delay_Resp packets
    delay_resp_packet = create_ptp_packet(PTP_DELAY_RESP)
    sendp(delay_resp_packet, iface=iface, count=count)
    print("Sent Delay_Resp messages")