from scapy.layers.inet import IP, sr1, UDP, TCP, ICMP
from scapy.all import *
from abc import ABC
from random import random


# # packet to take in src, dest, proto,
# class Packet:
#     def __init__(self, source: str, dest: str, protocol: str, flags: list, **kwargs):
#         self.source_ip = source
#         self.dest_ip = dest
#         self.protocol = protocol
#         self.flags = flags
#         self.time_to_live = kwargs['ttl']
#         self.port_num = kwargs['port_number']


# function used to create instances of specific type of packets (i.e. tcp, icmp, udp)
class PacketFactory(ABC):
    @staticmethod
    def make_packet(dest_ip: str, port_num: int, protocol: str, **kwargs) -> IP:
        default_packet = IP(dst=dest_ip/UDP(sport=src_port, dport=port_number, flags='S'))
        dest = dest_ip
        src_port = random.randrange(1025, 65534)
        port_number = port_num
        set_flags = str(str(kwargs['flags']).strip().split()).join('')
        if protocol.lower() in ['tcp', '6']:
            if set_flags:
                pkt = IP(dst=dest/TCP(sport=src_port, dport=port_number, flags=set_flags))
        elif protocol.lower() in ['udp', '17'] :
            if not set_flags:
                pkt = IP(dst=dest/UDP(sport=src_port, dport=port_number, flags='S'))
            else:
                pkt = IP(dst=dest/UDP(sport=src_port, dport=port_number, flags=set_flags))
        elif protocol.lower() in ['icmp', '1']:
            pkt = IP(dst=dest_ip / ICMP(sport=src_port, dport=port_number))
        else: # default to tcp SYN Packet
            return default_packet
        return pkt


