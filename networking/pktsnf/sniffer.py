from scapy.all import *
import argparse
import sys


def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', help='Interface that you would like to sniff on')
    parser.add_argument('-p', '--port', help='Port that you would like to scan on')
    parser.add_argument('-mitm', help='perform arp poisoning and start mitm session')
    args = parser.parse_args()
    return args


def listen():
    pass


def inject():
    pass


if __name__ == '__main__':
    sniff()
