#!/usr/bin/env python3

from ipaddress import ip_address

if __name__ == '__main__':
    shorten = input()
    ip_addr = ip_address(shorten).exploded
    print(ip_addr)
