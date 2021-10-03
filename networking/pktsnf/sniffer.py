from scapy.all import *
import argparse
import sys


common_ports = [20, 21, 22, 23, 25, 43, 53, 65, 67, 68, 69, 80, 88, 109, 110, ]


def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', help='Interface that you would like to sniff on', action='store_true')
    parser.add_argument('-p', '--port', help='Port that you would like to scan on')
    parser.add_argument('-mitm', help='perform arp poisoning and start mitm session')
    args = parser.parse_args()
    return args


def listen():
    pass


def inject():
    pass


if __name__ == '__main__':
    try:
        args = collect_args()
        if not args.i:
            interface = ''
        else:
            interface = args.i
        if not args.p:
            ports = common_ports
    except Exception as e:
        print('error occurred:', e)

    sniff(iface=interface, filter="tcp port 80")