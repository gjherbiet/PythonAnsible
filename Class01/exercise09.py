#!/usr/bin/env python
'''
The script should find all of the crypto map entries in the file 
that are using pfs group2
'''

from ciscoconfparse import CiscoConfParse

def main(cisco_file='cisco_ipsec.txt'):
    '''
    Use the ciscoconfparse library to find the crypto maps that are using pfs
    group2
    '''
    
    cisco_cfg = CiscoConfParse(cisco_file)
    
    for crypto_map in cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',
                                                 childspec=r'pfs group2'):
        print crypto_map.text

if __name__ == "__main__":
    main()