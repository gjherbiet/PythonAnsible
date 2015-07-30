#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

# Parse config file
cfg = CiscoConfParse('cisco_ipsec.txt')

# Find crypto map entries with PFS group 2
for pfs_group2 in cfg.find_objects(r'pfs group2'):
    crypto_map = pfs_group2.parent
    print crypto_map.text

