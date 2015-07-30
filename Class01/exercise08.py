#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

# Parse config file
cfg = CiscoConfParse('cisco_ipsec.txt')

# Find crypto map entries and print children
for crypto_map in cfg.find_objects(r'^crypto map CRYPTO'):
    for child in crypto_map.children:
        print child.text

