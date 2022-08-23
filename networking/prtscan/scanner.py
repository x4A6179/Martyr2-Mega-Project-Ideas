import argparse
import sys
from scapy.all import *
import socket


def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', '--host', help='IPv4 address you want to scan')
    parser.add_argument('-v6', help='IPv6 address you want to scan')
    parser.add_argument('-p', '--port', help='Port(s) you want to scan')
    parser.add_argument('-f', '--flag', help='Flag(s) you want to set in payload')
    parser.add_argument('-sT', help='enable full TCP connection when port scanning')
    args = parser.parse_args()
    return args


def craft_packet(proto: str, flag_list: []):
    # this function should be called only to craft a scapy packet
    # inputs include protocol (tcp/udp) & flag to be set in the payload
    # upon crafting should return Scapy packet object
    pass


def scan():

    pass


if __name__ == '__main__':
    # collect arguments here to pass into scan function
    args = collect_args()
    if args.v6:
        print("ipv6 scan starting")
    if args.h:
        host = args.h
    if args.p:
        port = args.p
    if args.f:
        flags = args.f

    totalPorts = [port for port in args.p]

    if 't' in args.f:
        if 's' in args.f:
            sPkt = sr1(IP(dst=host)/TCP(dport=totalPorts, flags='S'))
        elif 'x' in args.f:
            sPkt = sr1(IP(dst=host)/TCP(dport=totalPorts, flags='UPR'))
    elif 'u' in args.f:
        sPkt = sr1(IP(dst=host)/UDP(dport=totalPorts))
    # check for ipv6 addr
    # check ports for '-' or ',' ; if '-', get range for ports else split by ',' --> place result in array
    # handle flags after simple port scanning works (use syn only for now)
    # pass args to scan function
    pass

# create logic to pull up the interactive console if no inputs are given (or may just be the base case)
'''
General Logic (MVP):
1. call script from command line with ip & ports want to scan
    have capability where user can input -p & -i for indicating port and ip

2. if correct input supplied then conduct scan by crafting scapy syn packet and sending to ip:port
2a. if incorrect input, trigger fail route

3. If syn-ack gotten back then save port state as 'open'
3a. else save port state as closed, if rst gotten back save as 'filtered'

4. Print to console the following:
    1) which ip was scanned
    2) which ports were opened/filtered/closed
'''

'''
Enhancements:
1. Possibly build interactive console
2. Build functionality to include different scan types and based on the input, craft a specific scapy packet for it
3. possibly call another function to do something else to the data after it's been received.
4. add in a possibility to save to a specific location in the system (use context function "with" to write into a file)
'''